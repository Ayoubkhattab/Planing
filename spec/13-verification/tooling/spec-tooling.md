---
id: SPEC-TOOLING
type: specification-tooling
title: Specification tooling (generators and checkers)
wave: W9
status: BASELINED
---

# أدوات المواصفة

أدوات **مواصفة** لا كود إنتاج (V6§3). ترتيب التشغيل لكل شريحة: `slice_gen.py <slice>_data` ← `slice_contracts.py <slice>_data` ← `acc_gen.py <slice>_data`، ثم `lint_md.py` و`w9_check.py`. تتطلب PyYAML وopenapi-spec-validator. **اختبار ذهاب وإياب نُفذ في W9:** استخراج هذه الأدوات من هذا الملف وإعادة التوليد يعطي عقوداً مطابقة حرفياً.

**ما يُولَّد (لا يُعدَّل يدوياً):** ملفات Aggregates، كتالوجات الأوامر/الاستعلامات/الأحداث، كل ملفات OpenAPI/AsyncAPI/الأخطاء، ملفات القبول `*-state-machine.md`. **ما يُحرَّر كوثائق:** المواصفات، السياسات، وثائق الجودة والأمن والاعتمادية، سجلات الجاهزية، التقارير.

## md_io.py

Markdown ⇄ YAML renderer/loader used by every data file

```python
# -*- coding: utf-8 -*-
"""Render spec data to Markdown (human tables + embedded YAML) and load it back."""
import yaml, re

def _cell(v):
    if v is None: return "—"
    if isinstance(v, bool): return "yes" if v else "no"
    if isinstance(v, list):
        if all(not isinstance(x, (dict, list)) for x in v):
            return ", ".join(str(x) for x in v) if v else "—"
        return yaml.safe_dump(v, allow_unicode=True, default_flow_style=True, width=10**6).strip()
    if isinstance(v, dict):
        return yaml.safe_dump(v, allow_unicode=True, default_flow_style=True, width=10**6).strip()
    return str(v).replace("|", "\\|").replace("\n", " ")

def _is_long(items):
    for it in items:
        for v in it.values():
            if isinstance(v, str) and len(v) > 110: return True
            if isinstance(v, list) and any(isinstance(x, dict) for x in v): return True
    return len(items[0]) > 9 if items else False

def _list_of_dicts(key, items, level=2):
    out = [f"{'#'*level} {key}", "", f"_{len(items)} items_", ""]
    if not items: return out + ["_empty_", ""]
    if _is_long(items):
        for it in items:
            head = it.get("id") or it.get("business_object") or it.get("en") or it.get("dimension") or ""
            name = it.get("title") or it.get("name") or it.get("statement") or ""
            if isinstance(name, str) and len(name) > 90: name = ""
            out.append(f"{'#'*(level+1)} {head}{' — '+name if name else ''}")
            out.append("")
            for k, v in it.items():
                if k in ("id",) or (k in ("title","name") and name): continue
                if isinstance(v, list) and v and isinstance(v[0], dict):
                    out.append(f"- **{k}:**")
                    for d in v: out.append(f"  - {_cell(d)}")
                else:
                    out.append(f"- **{k}:** {_cell(v)}")
            out.append("")
    else:
        cols = []
        for it in items:
            for k in it:
                if k not in cols: cols.append(k)
        out.append("| " + " | ".join(cols) + " |")
        out.append("|" + "---|" * len(cols))
        for it in items:
            out.append("| " + " | ".join(_cell(it.get(c)) for c in cols) + " |")
        out.append("")
    return out

def render(doc):
    meta = doc.get("meta", {})
    lines = ["---", yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=120).strip(), "---", ""]
    lines += [f"# {meta.get('title', meta.get('id',''))}", ""]
    if meta.get("notes"): lines += [f"> {meta['notes']}", ""]
    for k, v in doc.items():
        if k == "meta": continue
        if isinstance(v, list) and v and all(isinstance(x, dict) for x in v):
            lines += _list_of_dicts(k, v)
        elif isinstance(v, list):
            lines += [f"## {k}", ""] + ([f"- {x}" for x in v] if v else ["_empty_"]) + [""]
        elif isinstance(v, dict):
            lines += [f"## {k}", "", "```yaml", yaml.safe_dump(v, allow_unicode=True, sort_keys=False).strip(), "```", ""]
        else:
            lines += [f"**{k}:** {v}", ""]
    body = {k: v for k, v in doc.items() if k != "meta"}
    lines += ["---", "", "<details>", "<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>", "",
              "```yaml", yaml.safe_dump(body, allow_unicode=True, sort_keys=False, width=120).strip(), "```", "", "</details>", ""]
    return "\n".join(lines)

def load(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = yaml.safe_load(m.group(1)) if m else {}
    d = re.search(r"<summary>Machine-readable data.*?```yaml\n(.*?)\n```", text, re.S)
    body = yaml.safe_load(d.group(1)) if d else {}
    doc = {"meta": meta}; doc.update(body or {})
    return doc
```

## slice_gen.py

Slice generator: aggregates, complete matrices, catalogs, lint

```python
# -*- coding: utf-8 -*-
import os, yaml, json, re, collections
import importlib, sys
D = importlib.import_module(sys.argv[1])
SL = D.SLICE; SFX = SL.lower().replace('-', '')
W = "work"
BY = "Claude (acting decision owner, delegated by project owner)"
COMMON_ERR = ["VALIDATION_FAILED", "AUTHZ_DENIED", "VERSION_CONFLICT", "IDEMPOTENCY_KEY_REUSED"]

def fm(meta): return "---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).strip() + "\n---\n\n"
def write(p, t):
    os.makedirs(os.path.dirname(f"{W}/{p}"), exist_ok=True); open(f"{W}/{p}", "w", encoding="utf-8").write(t)
def meta(i, t, title, wave="W4", tier="T1", extra=None):
    m = {"id": i, "type": t, "title": title, "wave": wave, "slice": SL, "tier": tier, "status": "APPROVED_DELEGATED",
         "approved_by": BY, "approved_at": "2026-09-24"}
    if extra: m.update(extra)
    return m
def slug(c): return c.split("-", 2)[2].lower()
def err_code(a, name="INVALID_STATE_TRANSITION"): return a["id"].replace("AGG-", "") .replace("-", "_") + "_" + name

# ---------- derive command, event catalogs ----------
COMMANDS = {}; EVENTS = {}
for a in D.AGGS.values():
    nt = [s for s in a["states"] if s not in a["terminal"]]
    for fr, cmd, to, guard, evt, gerr in a["transitions"]:
        frs = ["∅"] if fr == "∅" else (nt if fr == "*NT" else fr)
        EVENTS.setdefault(evt, {"id": evt, "aggregate": a["id"], "bc": a["bc"], "produced_by": [], "security_affecting": evt in D.SECURITY_AFFECTING})
        EVENTS[evt]["produced_by"].append(cmd)
        if cmd.startswith("SYS"): continue
        c = COMMANDS.setdefault(cmd, {"id": cmd, "aggregate": a["id"], "bc": a["bc"], "transitions": [], "errors": set(COMMON_ERR), "creates": False})
        c["transitions"].append({"from": frs, "to": to, "guard": guard, "event": evt})
        if gerr: c["errors"].add(gerr)
        if fr == "∅": c["creates"] = True
        else: c["errors"].add(err_code(a))
for c in COMMANDS.values():
    ctx, res = D.RESOURCE[c["aggregate"]]
    if c["id"] in getattr(D, "PATH_OVERRIDE", {}):
        c["http"] = ("POST", D.PATH_OVERRIDE[c["id"]])
    elif c["id"] == "CMD-AUT-DELEGATE":
        c["http"] = ("POST", f"/api/v1/{ctx}/{res}/{{id}}/actions/delegate")
    elif c["creates"]:
        c["http"] = ("POST", f"/api/v1/{ctx}/{res}")
    else:
        c["http"] = ("POST", f"/api/v1/{ctx}/{res}/{{id}}/actions/{slug(c['id'])}")
    c["internal"] = c["id"] in D.SYSTEM_CMDS
    c["policy"] = "POL-" + c["id"][4:]
    c["actors"] = "system (workload identity)" if c["internal"] else D.ACTORS[c["id"].split("-")[1]]
    c["payload"] = D.P[c["id"]]
    c["errors"] = sorted(set(c["errors"]) | set(getattr(D, "EXTRA_ERRORS", {}).get(c["aggregate"], [])))
    c["offline_capable"] = c["id"] in getattr(D, "OFFLINE", set())
    c["idempotency_key"] = "required"
    c["expected_version"] = "not applicable (creation)" if c["creates"] else "required (If-Match)"
for e in EVENTS.values():
    cons = list(getattr(D, "CONSUMERS", {}).get(e["aggregate"], getattr(D, "CONSUMERS", {}).get("default", ["Search/Directory projection (BC01 read model)"])))
    if e["security_affecting"]: cons = ["Security-version service (EVT-SEC-VERSION-INCREMENTED)", "PEP decision caches", "Projection security-version table"] + cons
    if e["aggregate"] in ("AGG-POLICY-SET", "AGG-CLASSIFICATION-SCHEME"): cons.append("PDP bundle distributor")
    if e["aggregate"] == "AGG-TENANT": cons.append("Provisioning saga / cell controller")
    if e["aggregate"] == "AGG-ORGANIZATION": cons.append("All contexts' org-scope read models")
    if e["aggregate"] == "AGG-AUTHORITY-GRANT": cons.append("Notification (delegates informed on revoke/expire)")
    e["consumers"] = cons
    e["schema"] = f"asyncapi-{SFX}.md#/components/messages/{e['id']}"
    e["version"] = 1
    e["partition_key"] = "tenant_id + aggregate.id"
if SL == "SLC-01": EVENTS["EVT-SEC-VERSION-INCREMENTED"] = {"id": "EVT-SEC-VERSION-INCREMENTED", "aggregate": "(derived) SecurityVersion", "bc": "BC01", "produced_by": ["security-version service on any security-affecting event"],
    "security_affecting": True, "consumers": ["All PEPs", "Projection security-version tables", "SecurityContext cache"], "schema": "asyncapi-{SFX}.md#/components/messages/EVT-SEC-VERSION-INCREMENTED",
    "version": 1, "partition_key": "tenant_id + subject_urn", "priority": "high (dedicated channel)"}

# ---------- matrix + reachability ----------
def matrix(a):
    nt = [s for s in a["states"] if s not in a["terminal"]]
    cmds = []
    for fr, cmd, to, g, evt, ge in a["transitions"]:
        if cmd not in cmds: cmds.append(cmd)
    rows = {}
    for s in a["states"]:
        rows[s] = {}
        for c in cmds:
            rows[s][c] = f"✗ {err_code(a)}"
    create = {}
    for fr, cmd, to, g, evt, ge in a["transitions"]:
        if fr == "∅": create[cmd] = (to, evt); continue
        frs = nt if fr == "*NT" else fr
        for s in frs:
            rows[s][cmd] = f"→ {s if to == '=' else to}"
    return cmds, rows, create

def reach(a):
    if a["id"] in D.PERPETUAL: return "EXEMPT: " + D.PERPETUAL[a["id"]]
    nt = [s for s in a["states"] if s not in a["terminal"]]
    g = collections.defaultdict(set)
    for fr, cmd, to, *_ in a["transitions"]:
        if fr == "∅" or to == "=": continue
        for s in (nt if fr == "*NT" else fr): g[s].add(to)
    bad = []
    for s in nt:
        seen, st = set(), [s]
        while st:
            x = st.pop()
            if x in seen: continue
            seen.add(x); st += list(g[x])
        if not seen & set(a["terminal"]): bad.append(s)
    return "PASS" if not bad else "FAIL: " + ", ".join(bad)

# ---------- write aggregate files ----------
LINT = {"SL-02": [], "SL-03": [], "SL-04": [], "SL-05": [], "SL-06": [], "SL-24": []}
for a in D.AGGS.values():
    cmds, rows, create = matrix(a)
    r = reach(a); a["reachability"] = r
    if r.startswith("FAIL"): LINT["SL-06"].append(a["id"])
    if len(a["entities"]) > 7: LINT["SL-24"].append(a["id"])
    for fr, cmd, to, g, evt, ge in a["transitions"]:
        if not evt or not g: LINT["SL-04"].append(f"{a['id']}:{cmd}")
    L = [fm(meta(a["id"], "aggregate", a["name"], extra={"bounded_context": a["bc"], "importance_tier": a["tier"], "personal_data": a["personal_data"],
          "traces": {"satisfies": a["requirements"], "state_machine": "SM-" + a["id"][4:], "decided_by": ["ADR-P01", "ADR-P02", "ADR-P03", "ADR-P13"]}})),
         f"# {a['id']} — {a['name']}", "", f"**الغرض:** {a['purpose']}  ", f"**السياق:** {a['bc']} · **المستوى:** {a['tier']} · **بيانات شخصية:** {'نعم' if a['personal_data'] else 'لا'}", ""]
    if a["notes"]: L += [f"> {a['notes']}", ""]
    L += ["## الثوابت (Invariants)", ""] + [f"- **{i.split(':')[0]}** —{i.split(':',1)[1]}" for i in a["invariants"]] + [""]
    if a["entities"]: L += ["## مكونات داخلية", ""] + [f"- {e}" for e in a["entities"]] + [""]
    L += ["## الحالات", "", f"- غير نهائية: {', '.join(s for s in a['states'] if s not in a['terminal'])}", f"- نهائية: {', '.join(a['terminal']) or '— (perpetual)'}",
          f"- قابلية الوصول لحالة نهائية (SL-06): **{r}**", "", "## الانتقالات", "", "| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |", "|---|---|---|---|---|---|"]
    for fr, cmd, to, g, evt, ge in a["transitions"]:
        frs = "∅ (إنشاء)" if fr == "∅" else ("أي حالة غير نهائية" if fr == "*NT" else ", ".join(fr))
        L.append(f"| {frs} | {cmd} | {'(بلا تغيير)' if to == '=' else to} | {g} | {evt} | {ge or '—'} |")
    L += ["", "## مصفوفة الحالات × الأوامر (كاملة — SL-05)", "", "كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.", ""]
    L.append("| الحالة \\ الأمر | " + " | ".join(cmds) + " |"); L.append("|---|" + "---|" * len(cmds))
    for c in cmds:
        pass
    creation_row = ["∅"] + [("→ " + create[c][0]) if c in create else "—" for c in cmds]
    L.append("| " + " | ".join(creation_row) + " |")
    for s in a["states"]:
        L.append(f"| {s} | " + " | ".join(rows[s][c] for c in cmds) + " |")
    L += ["", "## التزامن وعدم التكرار", "", "- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.",
          "- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).",
          "- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.", "",
          "## الحفظ", "", "- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).",
          f"- النموذج المنطقي: `06-data/logical-model/{SL.lower()}.md`.", ""]
    L += ["---", "", "<details>", "<summary>Machine-readable data (YAML)</summary>", "", "```yaml",
          yaml.safe_dump({k: v for k, v in a.items() if k != "transitions"} | {"transitions": [dict(zip(["from", "command", "to", "guard", "event", "guard_error"], t)) for t in a["transitions"]]},
                         allow_unicode=True, sort_keys=False).strip(), "```", "", "</details>", ""]
    write(f"03-domain/contexts/{a['bc']}/aggregates/{a['id']}.md", "\n".join(L))

# ---------- lint over commands/events/queries ----------
for c in COMMANDS.values():
    if not c["aggregate"] or not c["policy"]: LINT["SL-02"].append(c["id"])
    if not all(t["event"] for t in c["transitions"]): LINT["SL-03"].append(c["id"])
SL07 = [e for e, v in EVENTS.items() if not v["consumers"] or not v["schema"]]
SL08 = []  # every API is generated from CMD/QRY → 0 by construction; checked again against OpenAPI later
SL09 = [q[0] for q in D.QUERIES if not q[5]]

# ---------- catalogs ----------
for bc in sorted({a["bc"] for a in D.AGGS.values()}):
    cs = [c for c in COMMANDS.values() if c["bc"] == bc]
    L = [fm(meta(f"CMD-CAT-{bc}-{SFX.upper()}", "command-catalog", f"Commands — {bc} ({SL})", wave="W4")), f"# Commands — {bc} ({SL})", "", f"_{len(cs)} commands_", "",
         "| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |", "|---|---|---|---|---|---|---|---|---|"]
    for c in cs:
        L.append(f"| {c['id']} | {c['aggregate']} | `{c['http'][0]} {c['http'][1]}` | {'نعم' if c['internal'] else 'لا'} | {c['actors']} | {c['policy']} | `{c['payload'] or '—'}` | {', '.join(sorted({t['event'] for t in c['transitions']}))} | {', '.join(c['errors'])} |")
    L += ["", "**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.", "",
          "---", "", "<details>", "<summary>Machine-readable data (YAML)</summary>", "", "```yaml",
          yaml.safe_dump({"commands": [{**c, "http": list(c["http"])} for c in cs]}, allow_unicode=True, sort_keys=False).strip(), "```", "", "</details>", ""]
    write(f"03-domain/contexts/{bc}/commands-{SFX}.md", "\n".join(L))
    qs = [q for q in D.QUERIES if q[1] == bc]
    L = [fm(meta(f"QRY-CAT-{bc}-{SFX.upper()}", "query-catalog", f"Queries — {bc} ({SL})")), f"# Queries — {bc} ({SL})", "",
         "| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |", "|---|---|---|---|---|"]
    for q in qs: L.append(f"| {q[0]} | `{q[2]} {q[3]}` | {q[4]} | {q[5]} | {q[6]} |")
    L += ["", "كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).", ""]
    write(f"03-domain/contexts/{bc}/queries-{SFX}.md", "\n".join(L))
    es = [e for e in EVENTS.values() if e["bc"] == bc]
    L = [fm(meta(f"EVT-CAT-{bc}-{SFX.upper()}", "event-catalog", f"Domain Events — {bc} ({SL})")), f"# Domain Events — {bc} ({SL})", "", f"_{len(es)} events_", "",
         "| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |", "|---|---|---|---|---|---|"]
    for e in es: L.append(f"| {e['id']} | {e['aggregate']} | {', '.join(e['produced_by'])} | {'نعم' if e['security_affecting'] else '—'} | {'; '.join(e['consumers'])} | {e['partition_key']} |")
    L += ["", "المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).", ""]
    write(f"03-domain/contexts/{bc}/events-{SFX}.md", "\n".join(L))

json.dump({"LINT": LINT, "SL-07": SL07, "SL-09": SL09, "n_cmd": len(COMMANDS), "n_evt": len(EVENTS), "n_qry": len(D.QUERIES),
           "reach": {a: v["reachability"] for a, v in D.AGGS.items()}}, open(f"/tmp/{SFX}_lint.json", "w"), ensure_ascii=False, indent=1, default=list)
import pickle; pickle.dump((COMMANDS, EVENTS), open(f"/tmp/{SFX}_cat.pkl", "wb"))
print(open(f"/tmp/{SFX}_lint.json").read())
```

## slice_contracts.py

OpenAPI 3.1 / AsyncAPI 3 / error catalog generator with validation, path-collision guard and slice enrichment hook

```python
# -*- coding: utf-8 -*-
import pickle, yaml, re, json, copy
import importlib, sys
D = importlib.import_module(sys.argv[1])
SL = D.SLICE; SFX = SL.lower().replace('-', '')
from openapi_spec_validator import validate
COMMANDS, EVENTS = pickle.load(open(f"/tmp/{SFX}_cat.pkl", "rb"))
BY = "Claude (acting decision owner, delegated by project owner)"
W = "work"

ITEMS = {"permissions": {"$ref": "#/components/schemas/Permission"}, "names": {"$ref": "#/components/schemas/LocalizedName"},
         "levels": {"$ref": "#/components/schemas/Level"}, "caveats": {"$ref": "#/components/schemas/Caveat"},
         "decision_tables": {"type": "object"}, "tests": {"type": "object"},
         "initial_claims": {"$ref": "#/components/schemas/ClaimInput"}, "measurements": {"$ref": "#/components/schemas/Measurement"},
         "source_refs": {"$ref": "#/components/schemas/Urn"}, "attachments": {"$ref": "#/components/schemas/Urn"}, "derived_from": {"$ref": "#/components/schemas/Urn"},
         "external_ids": {"type": "object"}, "corrections": {"type": "object"}}
def ftype(name, t):
    if t == "string": return {"type": "string"}
    if t == "boolean": return {"type": "boolean"}
    if t == "integer": return {"type": "integer"}
    if t == "number": return {"type": "number"}
    if t == "urn": return {"$ref": "#/components/schemas/Urn"}
    if t == "date-time": return {"type": "string", "format": "date-time"}
    if t == "object": return {"type": "object"}
    if t == "array": return {"type": "array", "items": ITEMS.get(name, {"type": "string"})}
    if t.startswith("enum("): return {"type": "string", "enum": t[5:-1].split(",")}
    return {"$ref": f"#/components/schemas/{t}"}
def body_schema(payload):
    props, req = {}, []
    for f in payload.split():
        n, t = f.split(":", 1)
        if n.endswith("!"): n = n[:-1]; req.append(n)
        props[n] = ftype(n, t)
    s = {"type": "object", "properties": props, "additionalProperties": False}
    if req: s["required"] = req
    return s

HDR = {"Idempotency-Key": {"name": "Idempotency-Key", "in": "header", "required": True, "schema": {"type": "string", "maxLength": 128}},
       "If-Match": {"name": "If-Match", "in": "header", "required": True, "description": "expected aggregate version", "schema": {"type": "string"}},
       "X-Purpose": {"name": "X-Purpose", "in": "header", "required": True, "schema": {"type": "string"}},
       "X-Correlation-Id": {"name": "X-Correlation-Id", "in": "header", "required": True, "schema": {"type": "string"}},
       "Cursor": {"name": "cursor", "in": "query", "required": False, "schema": {"type": "string"}},
       "Limit": {"name": "limit", "in": "query", "required": False, "schema": {"type": "integer", "minimum": 1, "maximum": 200, "default": 50}},
       "Id": {"name": "id", "in": "path", "required": True, "schema": {"type": "string"}}}
def ref(n): return {"$ref": f"#/components/parameters/{n}"}

BASE_SCHEMAS = {
 "Urn": {"type": "string", "pattern": "^urn:[a-z0-9-]+:[a-z0-9-]+:[0-9A-HJKMNP-TV-Z]{26}$"},
 "LocalizedName": {"type": "object", "required": ["original", "lang"], "properties": {"original": {"type": "string"}, "lang": {"type": "string"},
     "normalized": {"type": "string", "readOnly": True}, "transliterations": {"type": "array", "items": {"type": "object", "properties": {"scheme": {"type": "string"}, "value": {"type": "string"}}}}}},
 "TenantQuotas": {"type": "object", "required": ["requests_per_s", "storage_gb", "events_per_s", "concurrent_jobs"],
     "properties": {k: {"type": "integer", "minimum": 0} for k in ["requests_per_s", "storage_gb", "events_per_s", "concurrent_jobs"]}},
 "Permission": {"type": "object", "required": ["action", "resource_type"], "properties": {"action": {"type": "string"}, "resource_type": {"type": "string"}}},
 "Level": {"type": "object", "required": ["code", "rank"], "properties": {"code": {"type": "string"}, "rank": {"type": "integer"}, "label_ar": {"type": "string"},
     "label_en": {"type": "string"}, "requires_dedicated_cell": {"type": "boolean"}, "deprecated": {"type": "boolean"}}},
 "Caveat": {"type": "object", "required": ["code"], "properties": {"code": {"type": "string"}, "releasable_to": {"type": "array", "items": {"type": "string"}},
     "not_releasable_to": {"type": "array", "items": {"type": "string"}}}},
 "ResourceRef": {"type": "object", "required": ["urn", "id", "version", "state"], "properties": {"urn": {"$ref": "#/components/schemas/Urn"}, "id": {"type": "string"},
     "version": {"type": "integer"}, "state": {"type": "string"}}},
 "ApiError": {"type": "object", "required": ["code", "message", "correlation_id", "retryable"], "properties": {"code": {"type": "string"}, "message": {"type": "string"},
     "details": {"type": "object"}, "correlation_id": {"type": "string"}, "trace_id": {"type": "string"}, "retryable": {"type": "boolean"},
     "policy": {"type": "object", "properties": {"decision": {"type": "string"}, "reason_code": {"type": "string"}}}}},
 "Page": {"type": "object", "required": ["items"], "properties": {"items": {"type": "array", "items": {"type": "object"}}, "next_cursor": {"type": ["string", "null"]}}},
 "AuthorityCheckRequest": {"type": "object", "required": ["actor", "decision_type", "scope", "at"], "properties": {"actor": {"$ref": "#/components/schemas/Urn"},
     "decision_type": {"type": "string"}, "scope": {"$ref": "#/components/schemas/Urn"}, "at": {"type": "string", "format": "date-time"}, "amount": {"type": "number"}}},
 "AuthorityCheckResponse": {"type": "object", "required": ["authorized", "reason"], "properties": {"authorized": {"type": "boolean"},
     "grant_chain": {"type": "array", "items": {"$ref": "#/components/schemas/Urn"}}, "reason": {"type": "string"}}},
 "DecisionRequest": {"type": "object", "required": ["subject", "action", "resource", "purpose", "context"], "properties": {"subject": {"type": "object"}, "action": {"type": "string"},
     "resource": {"type": "object"}, "purpose": {"type": "string"}, "context": {"type": "object"}}},
 "DecisionResponse": {"type": "object", "required": ["decision", "reason_code", "policy_version"], "properties": {"decision": {"enum": ["ALLOW", "DENY", "CONDITIONAL", "REDACT", "AGGREGATE", "REQUIRE_APPROVAL"]},
     "obligations": {"type": "array", "items": {"type": "object"}}, "allowed_scope": {"type": ["object", "null"]}, "reason_code": {"type": "string"}, "policy_version": {"type": "string"}}},
}

BASE_SCHEMAS.update({
 "Label": {"type": "object", "required": ["level"], "properties": {"level": {"type": "string"}, "compartments": {"type": "array", "items": {"type": "string"}},
     "caveats": {"type": "array", "items": {"type": "string"}}}},
 "Interval": {"type": "object", "required": ["from"], "properties": {"from": {"type": "string", "format": "date-time"}, "to": {"type": ["string", "null"], "format": "date-time"}}},
 "FuzzyInterval": {"type": "object", "required": ["precision"], "properties": {"start": {"type": ["string", "null"], "format": "date-time"}, "end": {"type": ["string", "null"], "format": "date-time"},
     "precision": {"enum": ["instant", "second", "minute", "hour", "day", "month", "year", "decade", "unknown"]}, "uncertainty_before": {"type": ["string", "null"]}, "uncertainty_after": {"type": ["string", "null"]}}},
 "SpatialEnvelope": {"type": "object", "required": ["geometry", "crs_original", "accuracy_m"], "properties": {"geometry": {"type": "object", "description": "GeoJSON"},
     "crs_original": {"type": "string", "pattern": "^EPSG:[0-9]+$"}, "coordinates_original": {"type": "object"}, "accuracy_m": {"type": "number", "minimum": 0},
     "accuracy_basis": {"enum": ["measured", "reported", "estimated", "unknown"]}}},
 "ClaimValue": {"type": "object", "required": ["kind"], "properties": {"kind": {"enum": ["string", "number", "date", "fuzzy_interval", "geometry", "enum", "ref"]},
     "string": {"$ref": "#/components/schemas/LocalizedName"}, "number": {"type": "number"}, "unit": {"type": "string", "description": "UCUM"},
     "date": {"type": "string", "format": "date-time"}, "fuzzy_interval": {"$ref": "#/components/schemas/FuzzyInterval"},
     "geometry": {"$ref": "#/components/schemas/SpatialEnvelope"}, "enum": {"type": "string"}, "ref": {"$ref": "#/components/schemas/Urn"}}},
 "Confidence": {"type": "object", "required": ["information_confidence"], "properties": {"information_confidence": {"enum": [1, 2, 3, 4, 5, 6]},
     "verification_status": {"enum": ["UNVERIFIED", "PARTIALLY_VERIFIED", "VERIFIED", "DISPUTED", "REFUTED"]}, "uncertainty": {"type": "object"}},
     "description": "source_reliability, data_quality, freshness, completeness are computed by the platform (confidence-model)"},
 "ClaimInput": {"type": "object", "required": ["predicate", "value", "valid", "source_refs", "confidence"], "properties": {"predicate": {"type": "string"},
     "value": {"$ref": "#/components/schemas/ClaimValue"}, "valid": {"$ref": "#/components/schemas/Interval"},
     "source_refs": {"type": "array", "minItems": 1, "items": {"$ref": "#/components/schemas/Urn"}}, "confidence": {"$ref": "#/components/schemas/Confidence"},
     "label": {"$ref": "#/components/schemas/Label"}}},
 "Measurement": {"type": "object", "required": ["quantity", "value", "unit"], "properties": {"quantity": {"type": "string"}, "value": {"type": "number"},
     "unit": {"type": "string"}, "uncertainty": {"type": "number"}}},
 "TemporalParams": {"type": "object", "description": "valid_at, known_at query parameters (ISO 8601; default now)"},
})

ERRS = {"400": "VALIDATION_FAILED", "404": "NOT_FOUND (also returned for forbidden resources — ADR-P06 §5)", "409": "state transition or version conflict", "422": "guard failed / idempotency key reused", "429": "RATE_LIMITED", "503": "AUDIT_UNAVAILABLE / dependency"}
def err_responses():
    return {k: {"description": v, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/ApiError"}}}} for k, v in ERRS.items()}

def build(ctx, bc, title, internal=False):
    paths = {}; schemas = copy.deepcopy(BASE_SCHEMAS)
    for c in COMMANDS.values():
        if c["bc"] != bc or c["internal"] != internal: continue
        m, p = c["http"]; name = "".join(w.capitalize() for w in c["id"][4:].split("-")) + "Command"
        schemas[name] = body_schema(c["payload"])
        params = [ref("Idempotency-Key"), ref("X-Purpose"), ref("X-Correlation-Id")]
        if "{id}" in p: params.insert(0, ref("Id"))
        if not c["creates"] or c["id"] == "CMD-AUT-DELEGATE":
            if c["id"] != "CMD-AUT-DELEGATE": params.append(ref("If-Match"))
        if "{id}" in p and ref("Id") not in params: params.insert(0, ref("Id"))
        ok = "201" if c["creates"] else "202"
        op = {"operationId": c["id"], "summary": c["id"], "x-aggregate": c["aggregate"], "x-policy": c["policy"],
              "x-events": sorted({t["event"] for t in c["transitions"]}), "x-error-codes": c["errors"], "x-offline-capable": c.get("offline_capable", False), "parameters": params,
              "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": f"#/components/schemas/{name}"}}}},
              "responses": {ok: {"description": "accepted", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/ResourceRef"}}}}, **err_responses()}}
        if m.lower() in paths.get(p, {}): raise SystemExit(f"PATH COLLISION: {m} {p} ({paths[p][m.lower()]['operationId']} vs {c['id']})")
        paths.setdefault(p, {})[m.lower()] = op
    if not internal:
        for q in D.QUERIES:
            if q[1] != bc: continue
            _, _, m, p, desc, who, req = q
            params = [ref("X-Purpose"), ref("X-Correlation-Id")] + [{"name": n, "in": "path", "required": True, "schema": {"type": "string"}} for n in re.findall(r"{(\w+)}", p)]
            if SL == "SLC-02" and m == "GET":
                params += [{"name": "valid_at", "in": "query", "required": False, "schema": {"type": "string", "format": "date-time"}},
                           {"name": "known_at", "in": "query", "required": False, "schema": {"type": "string", "format": "date-time"}}]
            resp = {"$ref": "#/components/schemas/Page"} if m == "GET" and not re.search(r"}$", p) else {"type": "object"}
            if q[0] == "QRY-AUT-CHECK": body, resp = "AuthorityCheckRequest", {"$ref": "#/components/schemas/AuthorityCheckResponse"}
            elif q[0] == "QRY-PDP-DECIDE": body, resp = "DecisionRequest", {"$ref": "#/components/schemas/DecisionResponse"}
            elif q[0] == "QRY-SEC-CONTEXT": body, resp = None, {"$ref": "https://platform/schemas/security-context-1.json"} ; resp = {"type": "object", "description": "PL-SECURITY-CONTEXT"}
            else: body = None
            if resp == {"$ref": "#/components/schemas/Page"}: params += [ref("Cursor"), ref("Limit")]
            op = {"operationId": q[0], "summary": desc, "x-authorized": who, "x-requirement": req, "parameters": params,
                  "responses": {"200": {"description": "ok", "content": {"application/json": {"schema": resp}}}, **err_responses()}}
            if m == "POST":
                op["requestBody"] = {"required": True, "content": {"application/json": {"schema": {"$ref": f"#/components/schemas/{body}"}}}} if body else {"required": False, "content": {"application/json": {"schema": {"type": "object"}}}}
                if q[0] == "QRY-AUD-VERIFY": op["responses"]["202"] = op["responses"].pop("200")
            paths.setdefault(p, {})[m.lower()] = op
    return {"openapi": "3.1.0", "info": {"title": title, "version": "1.0.0", "description": f"Generated from {SL} domain specification. Do not edit by hand."},
            "servers": [{"url": "https://{cell}.platform.local", "variables": {"cell": {"default": "cell-1"}}}],
            "security": [{"bearer": []}], "paths": paths,
            "components": {"securitySchemes": {"bearer": {"type": "http", "scheme": "bearer"}}, "parameters": HDR, "schemas": schemas}}

def md(doc_id, title, spec, notes):
    head = {"id": doc_id, "type": "api-contract", "title": title, "wave": "W6", "slice": SL, "tier": "T1", "status": "APPROVED_DELEGATED",
            "approved_by": BY, "approved_at": "2026-09-24", "format": "OpenAPI 3.1 (validated)", "traces": {"decided_by": ["CR-40", "REQ-PLT-007", "REQ-PLT-008", "REQ-PLT-009"]}}
    ops = [(p, m, o["operationId"]) for p, ms in spec["paths"].items() for m, o in ms.items()]
    L = ["---", yaml.safe_dump(head, allow_unicode=True, sort_keys=False).strip(), "---", "", f"# {title}", "", notes, "",
         f"_{len(ops)} operations · validated with openapi-spec-validator_", "", "| Method | Path | Operation |", "|---|---|---|"]
    L += [f"| {m.upper()} | `{p}` | {o} |" for p, m, o in ops]
    L += ["", "```yaml", yaml.safe_dump(spec, allow_unicode=True, sort_keys=False).strip(), "```", ""]
    return "\n".join(L), len(ops)

out = {}
CTX = {"BC01": "foundation", "BC02": "information", "BC03": "intelligence", "BC04": "operations", "BC05": "readiness", "BC06": "knowledge", "BC07": "integration", "BC08": "governance"}
TITLE = {"BC01": "Foundation", "BC02": "Information", "BC03": "Intelligence", "BC04": "Operations", "BC05": "Readiness", "BC06": "Knowledge", "BC07": "Integration", "BC08": "Governance"}
CTX.update({k: v[0] for k, v in getattr(D, "CTX_OVERRIDE", {}).items()}); TITLE.update({k: v[1] for k, v in getattr(D, "CTX_OVERRIDE", {}).items()})
for bc in sorted({a["bc"] for a in D.AGGS.values()}):
    ctx = CTX[bc]; tt = f"{TITLE[bc]} API ({bc}) — {SL}"
    s = build(ctx, bc, tt)
    if hasattr(D, "enrich"): D.enrich(s, bc)          # slice-specific schema enrichment (reproducible)
    validate(s); out[bc] = s
    text, n = md(f"OPENAPI-{bc}-{SFX.upper()}", tt, s, "المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.")
    open(f"{W}/05-contracts/openapi-{ctx}-{SFX}.md", "w", encoding="utf-8").write(text); print(bc, n, "ops valid")
if D.SYSTEM_CMDS:
    s = build("foundation", "BC01", "Foundation Internal API (system commands)", internal=True); validate(s)
    text, n = md("OPENAPI-BC01-INTERNAL", f"Foundation Internal API — system commands ({SL})", s, "أوامر داخلية بهوية عبء عمل فقط.")
    open(f"{W}/05-contracts/openapi-foundation-internal-{SFX}.md", "w", encoding="utf-8").write(text); print("internal", n, "ops valid")

# ---------------- AsyncAPI 3 ----------------
env = {"type": "object", "required": ["event_id", "event_type", "event_version", "producer", "aggregate", "occurred_at", "recorded_at", "tenant_id", "correlation_id", "payload"],
       "properties": {"event_id": {"type": "string"}, "event_type": {"type": "string"}, "event_version": {"type": "integer"}, "producer": {"type": "string"},
                      "aggregate": {"type": "object", "properties": {"type": {"type": "string"}, "id": {"type": "string"}, "version": {"type": "integer"}}},
                      "occurred_at": {"type": "string", "format": "date-time"}, "recorded_at": {"type": "string", "format": "date-time"},
                      "tenant_id": {"type": "string"}, "correlation_id": {"type": "string"}, "causation_id": {"type": ["string", "null"]},
                      "security": {"type": "object", "description": "labels of the aggregate (ADR-P06)"}, "payload": {"type": "object"}}}
payload = {"type": "object", "required": ["aggregate_urn", "from_state", "to_state"], "properties": {"aggregate_urn": {"type": "string"},
           "from_state": {"type": ["string", "null"]}, "to_state": {"type": "string"}, "actor": {"type": "string"}, "reason": {"type": ["string", "null"]}, "changes": {"type": "object"}}}
msgs, ch_msgs = {}, {}
for e in EVENTS.values():
    name = e["id"]
    pl = payload if name != "EVT-SEC-VERSION-INCREMENTED" else {"type": "object", "required": ["subject_urn", "security_version", "cause_event_id"],
         "properties": {"subject_urn": {"type": "string"}, "security_version": {"type": "integer"}, "cause_event_id": {"type": "string"}}}
    msgs[name] = {"name": name, "contentType": "application/json", "payload": {"allOf": [{"$ref": "#/components/schemas/EventEnvelope"}, {"type": "object", "properties": {"payload": pl}}]},
                  "x-consumers": e["consumers"], "x-partition-key": e["partition_key"]}
    ch = "security" if name == "EVT-SEC-VERSION-INCREMENTED" else CTX[e["bc"]]
    ch_msgs.setdefault(ch, {})[name] = {"$ref": f"#/components/messages/{name}"}
asy = {"asyncapi": "3.0.0", "info": {"title": f"{SL} Domain Events", "version": "1.0.0"},
       "channels": {f"{ch}.events" if ch != "security" else "security.versions": {"address": "{cell}." + (f"{ch}.events" if ch != "security" else "security.versions"), "messages": m, "parameters": {"cell": {}}} for ch, m in ch_msgs.items()},
       "operations": {f"publish_{ch}": {"action": "send", "channel": {"$ref": "#/channels/" + (f"{ch}.events" if ch != "security" else "security.versions")}} for ch in ch_msgs},
       "components": {"schemas": {"EventEnvelope": env}, "messages": msgs}}
head = {"id": f"ASYNCAPI-{SFX.upper()}", "type": "event-contract", "title": f"AsyncAPI — {SL} Domain Events", "wave": "W6", "slice": SL, "tier": "T1",
        "status": "APPROVED_DELEGATED", "approved_by": BY, "approved_at": "2026-09-24", "format": "AsyncAPI 3.0"}
L = ["---", yaml.safe_dump(head, allow_unicode=True, sort_keys=False).strip(), "---", "", f"# AsyncAPI — {SL} Domain Events", "",
     f"_{len(msgs)} messages on {len(ch_msgs)} channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._", "",
     "```yaml", yaml.safe_dump(asy, allow_unicode=True, sort_keys=False).strip(), "```", ""]
open(f"{W}/05-contracts/asyncapi-{SFX}.md", "w", encoding="utf-8").write("\n".join(L)); print("asyncapi messages", len(msgs))

# ---------------- errors ----------------
codes = {}
for c in COMMANDS.values():
    for e in c["errors"]: codes.setdefault(e, set()).add(c["id"])
HTTP = lambda e: ("409" if "INVALID_STATE_TRANSITION" in e or e == "VERSION_CONFLICT" else "403→404" if e in ("AUTHZ_DENIED", "PERMISSION_DENIED") else
                  "400" if e == "VALIDATION_FAILED" else "503" if e == "AUDIT_UNAVAILABLE" else "422")
extra = {"NOT_FOUND": "404", "RATE_LIMITED": "429", "AUDIT_UNAVAILABLE": "503", "SEGREGATION_OF_DUTIES": "422", "POLICY_ENGINE_UNAVAILABLE": "503 (request denied)"}
rows = [f"| `{e}` | {HTTP(e)} | {'نعم' if e in ('VERSION_CONFLICT','AUDIT_UNAVAILABLE') else 'لا'} | {len(cs)} | {', '.join(sorted(cs))[:160]}{'…' if len(', '.join(cs))>160 else ''} |" for e, cs in sorted(codes.items())]
rows += [f"| `{e}` | {h} | {'نعم' if e in ('RATE_LIMITED','POLICY_ENGINE_UNAVAILABLE') else 'لا'} | — | platform-wide |" for e, h in extra.items() if e not in codes]
head = {"id": f"ERRORS-{SFX.upper()}", "type": "error-catalog", "title": f"Error Catalog — {SL}", "wave": "W6", "slice": SL, "status": "APPROVED_DELEGATED", "approved_by": BY, "approved_at": "2026-09-24"}
open(f"{W}/05-contracts/errors-{SFX}.md", "w", encoding="utf-8").write("\n".join(["---", yaml.safe_dump(head, allow_unicode=True, sort_keys=False).strip(), "---", "",
  f"# Error Catalog — {SL}", "", "`AUTHZ_DENIED` لا يُعاد للعميل كما هو عند موارد غير مرئية: يُعاد `NOT_FOUND` بنفس الشكل (ADR-P06 §5). يُعاد `403` فقط لمورد يحق للمستخدم رؤيته دون تنفيذ الإجراء.", "",
  "| الرمز | HTTP | retryable | عدد الأوامر | الأوامر |", "|---|---|---|---|---|"] + rows + [""]))
print("error codes", len(codes) + len([e for e in extra if e not in codes]))
json.dump({"n_ops": {k: len(v["paths"]) for k, v in out.items()}}, open("/tmp/contracts.json", "w"))
```

## acc_gen.py

Gherkin acceptance generator from state matrices

```python
import sys, importlib, yaml, os
D = importlib.import_module(sys.argv[1]); SL = D.SLICE; SFX = SL.lower().replace("-", "")
sys.argv = [sys.argv[0], sys.argv[1]]
import slice_gen as G  # re-generates catalogs deterministically; exposes matrix()
BY = "Claude (acting decision owner, delegated by project owner)"
out = f"work/13-verification/acceptance/{SL}"; os.makedirs(out, exist_ok=True)
tok = trej = 0
for a in D.AGGS.values():
    cmds, rows, create = G.matrix(a); ok, rej = [], []
    for s in a["states"]:
        for c in cmds:
            if c.startswith("SYS"): continue
            v = rows[s][c]
            if v.startswith("→"):
                evt = [t[4] for t in a["transitions"] if t[1] == c and ((t[0] == "*NT" and s not in a["terminal"]) or (isinstance(t[0], list) and s in t[0]))][0]
                ok.append((s, c, v[2:], evt))
            else: rej.append((s, c, v[2:]))
    tok += len(ok); trej += len(rej)
    h = {"id": f"TST-{a['id'][4:]}-SM", "type": "acceptance-spec", "title": f"Acceptance — {a['name']} state machine", "wave": "W6", "slice": SL,
         "status": "APPROVED_DELEGATED", "approved_by": BY, "approved_at": "2026-09-24", "generated_from": a["id"], "traces": {"verifies": ["SL-05", a["id"]] + a["requirements"]}}
    L = ["---", yaml.safe_dump(h, allow_unicode=True, sort_keys=False).strip(), "---", "", f"# Acceptance — {a['name']}", "",
         f"مولّدة من مصفوفة {a['id']}: {len(ok)} انتقالاً مسموحاً، {len(rej)} رفضاً.", "", "```gherkin", f"Feature: {a['name']} lifecycle ({a['id']})", "",
         "  Background:", "    Given an ACTIVE tenant, baseline policies, and an authorized actor", "    And every guard of the command is satisfied", "",
         "  Scenario Outline: allowed transition", "    Given a <aggregate> in state <from> at version <v>", "    When the actor sends <command> with a new Idempotency-Key and If-Match <v>",
         "    Then the state becomes <to>", "    And exactly one <event> is written to the outbox", "    And one audit record is written in the same transaction", "", "    Examples:",
         "      | aggregate | from | command | to | event | v |"] + [f"      | {a['name']} | {s} | {c} | {t} | {e} | 3 |" for s, c, t, e in ok]
    if create:
        L += ["", "  Scenario Outline: creation", "    When the actor sends <command> with a valid payload", "    Then a new <aggregate> exists in state <to> at version 1",
              "    And exactly one <event> is written to the outbox", "", "    Examples:", "      | aggregate | command | to | event |"] + [f"      | {a['name']} | {c} | {to} | {e} |" for c, (to, e) in create.items() if not c.startswith("SYS")]
    if rej:
        L += ["", "  Scenario Outline: rejected transition", "    Given a <aggregate> in state <state>", "    When the actor sends <command>",
              "    Then the command is rejected with <error> and HTTP 409", "    And the state and version are unchanged", "    And no event is written", "", "    Examples:",
              "      | aggregate | state | command | error |"] + [f"      | {a['name']} | {s} | {c} | {e} |" for s, c, e in rej]
    L += ["```", ""]
    open(f"{out}/{a['id'][4:].lower()}-state-machine.md", "w", encoding="utf-8").write("\n".join(L))
print("allowed", tok, "rejected", trej)
```

## lint_md.py

Spec lint over the Markdown package (SL-01, SL-15, SL-19, SL-20)

```python
import glob, re, json, yaml
from md_io import load
R="work"
docs={p:open(p,encoding="utf-8").read() for p in glob.glob(R+"/**/*.md",recursive=True)}
data={p:load(t) for p,t in docs.items()}
defined=set()
def walk(o):
    if isinstance(o,dict):
        for k in ("id","business_object"):
            if isinstance(o.get(k),str): defined.add(o[k])
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
for d in data.values(): walk(d)
for p,t in docs.items():
    m=re.search(r'^id: (\S+)',t,re.M)
    if m: defined.add(m.group(1))
alltext="\n".join(docs.values())
refs=set(re.findall(r"(?<!INV-)\b(?:UNK|OQ|CR|RSK|ASM|HAP|ADR-P|BRL|BRQ|SLC|DOM|UC|OUT|FIT|THR|PRV|DEBT|AI-OP|QAS-[A-Z]+|REQ-[A-Z]+)-\d+\b",alltext))
missing=sorted(r for r in refs if r not in defined)
own=data[R+"/03-domain/ownership.md"]["ownership"]
reqs=data[R+"/02-requirements/requirements.md"]["system_requirements"]
appr=[p for p,d in data.items() if str(d["meta"].get("status","")).startswith("APPROVED") and not d["meta"].get("approved_by")]
print(json.dumps({"files":len(docs),"SL-01":len([o for o in own if not o["owner"]]),
 "SL-15":len([r for r in reqs if not r["acceptance_criteria"]]),"SL-19":appr,"SL-20_missing":missing},ensure_ascii=False))
```

## w9_check.py

Cross-artifact consistency checker (W9)

```python
import sys, glob, re, yaml, json, importlib, collections, pickle; sys.path.insert(0,".")
from md_io import load
W="work"
mods=sorted(f[:-3] for f in __import__("os").listdir(".") if f.startswith("slc") and f.endswith("_data.py"))
res=collections.OrderedDict()
# 1 commands in OpenAPI, events in AsyncAPI
op_ids=set(); msg_ids=set()
for f in glob.glob(f"{W}/05-contracts/openapi-*.md"):
    s=yaml.safe_load(re.search(r"```yaml\n(.*?)\n```",open(f,encoding="utf-8").read(),re.S).group(1))
    for p,ms in s["paths"].items():
        for m,o in ms.items(): op_ids.add(o["operationId"])
for f in glob.glob(f"{W}/05-contracts/asyncapi-*.md"):
    s=yaml.safe_load(re.search(r"```yaml\n(.*?)\n```",open(f,encoding="utf-8").read(),re.S).group(1))
    msg_ids|=set(s["components"]["messages"])
cmds=set(); evts=set(); qrys=set(); aggs={}
for m in mods:
    D=importlib.import_module(m); sfx=D.SLICE.lower().replace("-","")
    C,E=pickle.load(open(f"/tmp/{sfx}_cat.pkl","rb"))
    cmds|=set(C); evts|=set(E); qrys|={q[0] for q in D.QUERIES}
    for a in D.AGGS.values(): aggs[a["id"]]=(D.SLICE,a)
res["commands_missing_in_openapi"]=sorted(cmds-op_ids)
res["queries_missing_in_openapi"]=sorted(qrys-op_ids)
res["events_missing_in_asyncapi"]=sorted(evts-msg_ids)
# 2 every aggregate: file, acceptance, policies, label source, ownership (BO mapping loose)
agg_files={re.search(r"(AGG-[A-Z0-9-]+)\.md",f).group(1) for f in glob.glob(f"{W}/03-domain/contexts/*/aggregates/*.md")}
acc={re.search(r"generated_from: (AGG-[A-Z0-9-]+)",open(f,encoding="utf-8").read()).group(1) for f in glob.glob(f"{W}/13-verification/acceptance/**/*-state-machine.md",recursive=True) if "generated_from" in open(f,encoding="utf-8").read()}
labels={r["aggregate"] for r in load(open(f"{W}/08-security/label-derivation-rules.md",encoding="utf-8").read())["rules"]}
pol_text="\n".join(open(f,encoding="utf-8").read() for f in glob.glob(f"{W}/08-security/policies-slc*.md"))
res["aggregates_total"]=len(aggs)
res["aggregate_files_orphan_or_missing"]=sorted(agg_files ^ set(aggs))
res["aggregates_without_acceptance"]=sorted(set(aggs)-acc)
res["aggregates_without_label_source"]=sorted(set(aggs)-labels)
res["commands_without_policy"]=sorted(c for c in cmds if ("POL-"+c[4:]) not in pol_text)
# 3 requirements traced
REQ=load(open(f"{W}/02-requirements/requirements.md",encoding="utf-8").read())["system_requirements"]
reqs=[r["id"] for r in REQ]; rel={r["id"]:r.get("release","R1") for r in REQ}
cov=set()
for f in glob.glob(f"{W}/15-traceability/trace-*.md"):
    for r in load(open(f,encoding="utf-8").read())["requirements"]:
        if r.get("tests") or str(r.get("status","")).startswith("TRACED"): cov.add(r["requirement"])
res["requirements_total"]=len(reqs)
res["requirements_untraced"]=sorted(r for r in set(reqs)-cov if rel[r]=="R1")        # R1 must be 0
res["requirements_untraced_R2_pending_slices"]=len([r for r in set(reqs)-cov if rel[r]=="R2"])
# 4 QAS referenced by some verification artifact
qas=[q["id"] for q in load(open(f"{W}/02-requirements/quality-scenarios.md",encoding="utf-8").read())["scenarios"]]
ver_text="\n".join(open(f,encoding="utf-8").read() for f in glob.glob(f"{W}/13-verification/**/*.md",recursive=True)+glob.glob(f"{W}/07-quality/performance-test-strategy.md")+glob.glob(f"{W}/15-traceability/*.md"))
res["qas_total"]=len(qas); res["qas_without_verification_reference"]=sorted(q for q in qas if q not in ver_text)
# 5 ADRs
adr=[]
for f in glob.glob(f"{W}/00-governance/decisions/ADR-*.md"):
    m=yaml.safe_load(re.match(r"^---\n(.*?)\n---",open(f,encoding="utf-8").read(),re.S).group(1)); adr.append((m["id"],m["status"]))
res["adrs"]=sorted(adr); res["adrs_not_approved"]=[a for a,s in adr if not s.startswith("APPROVED")]
# 6 registers
u=load(open(f"{W}/00-governance/registers/unknowns.md",encoding="utf-8").read())["unknowns"]
res["unknowns_open"]=[(x["id"],x["status"]) for x in u if not x["status"].startswith("closed")]
oq=load(open(f"{W}/00-governance/registers/open-questions.md",encoding="utf-8").read())["open_questions"]
res["open_questions_open"]=[x["id"] for x in oq if x["status"]!="closed"]
cr=load(open(f"{W}/00-governance/registers/corrections.md",encoding="utf-8").read())["corrections"]
res["corrections_total"]=len(cr); res["corrections_not_applied"]=[(x["id"],x["status"]) for x in cr if not re.match(r"(APPLIED|DECIDED|PARTIALLY_APPLIED \(glossary\))",x["status"])]
rk=load(open(f"{W}/00-governance/registers/risks.md",encoding="utf-8").read())["risks"]
res["risks_total"]=len(rk); res["risks_without_mitigation"]=[x["id"] for x in rk if not x.get("mitigation")]
res["risks_open_high_impact"]=[x["id"] for x in rk if x["status"]=="open" and x["impact"]=="H"]
hap=load(open(f"{W}/00-governance/registers/human-approvals.md",encoding="utf-8").read())["approval_points"]
res["haps"]=[(x["id"],x["status"]) for x in hap]
json.dump(res,open("/tmp/w9check.json","w"),ensure_ascii=False,indent=1)
print(json.dumps(res,ensure_ascii=False,indent=1))
```
