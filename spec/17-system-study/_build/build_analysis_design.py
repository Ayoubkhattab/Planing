#!/usr/bin/env python3
"""Generates the source-derived parts of spec/18-analysis-design/.

Run from anywhere: python3 spec/17-system-study/_build/build_analysis_design.py
Outputs (only the block between GENERATED markers is rewritten; text above it is authored):
  05-user-stories/us-bcNN.md  one story per command, query and SYS: transition
  08-state-models.md          one state diagram per aggregate
  09-business-rules.md        invariants, guards, segregation of duties, reference data, BRL per BC
  14-api-design.md            catalog of every OpenAPI operation
  15-event-design.md          catalog of every event per channel
  16-database-schema.md       tables per schema and ERDs from the logical data model
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from ar_terms import AGGREGATES as AR_AGG, VERBS as AR_VERB, CATEGORIES, COMMAND_PHRASES, ACTORS_AR  # noqa: E402

SPEC = Path(__file__).resolve().parents[2]
OUT = SPEC / "18-analysis-design"
CTX = SPEC / "03-domain" / "contexts"
BEGIN = "<!-- BEGIN GENERATED: build_analysis_design.py -->"
END = "<!-- END GENERATED: build_analysis_design.py -->"
GENERIC = ["AUTHZ_DENIED", "IDEMPOTENCY_KEY_REUSED", "VALIDATION_FAILED", "VERSION_CONFLICT"]
BC_NAMES = {"BC01": "Foundation — الأساس", "BC02": "Information — نواة المعلومات", "BC03": "Intelligence — الوعي والتحليل",
            "BC04": "Operations — التخطيط والتنفيذ", "BC05": "Readiness — الموارد والجاهزية",
            "BC06": "Knowledge — المعرفة والمنتجات", "BC07": "Platform Intelligence — التكامل والذكاء الاصطناعي",
            "BC08": "Governance — الحوكمة والأمن"}
SCHEMA_BC = {"foundation": "BC01", "information": "BC02", "intelligence": "BC03", "operations": "BC04",
             "readiness": "BC05", "knowledge": "BC06", "integration": "BC07", "field": "BC07", "ai": "BC07",
             "governance": "BC08"}


# ------------------------------------------------------------------ parsing helpers
def front_matter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def split_row(line):
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def tables(text):
    header, rows = None, []
    for line in text.splitlines() + [""]:
        s = line.strip()
        if s.startswith("|"):
            if header is None:
                header = split_row(s)
            elif not set(s.replace("|", "").strip()) <= set("-: "):
                rows.append(split_row(s))
            continue
        if header is not None:
            yield header, rows
        header, rows = None, []


def yaml_block(text):
    blocks = re.findall(r"^```yaml\n(.*?)^```", text, re.S | re.M)
    return yaml.safe_load(blocks[-1]) if blocks else {}


def md_records(text, prefix):
    recs = {}
    for block in re.split(r"\n(?=### )", text.split("<details>")[0]):
        m = re.match(rf"### ({prefix}-[A-Za-z0-9-]+)(?: — (.*))?", block)
        if m:
            rec = {"title": (m.group(2) or "").strip()}
            for k, v in re.findall(r"^- \*\*([a-z_]+):\*\* (.*)$", block, re.M):
                rec[k] = v.strip()
            recs[m.group(1)] = rec
    return recs


def split_top(value, sep=","):
    """Splits on sep outside parentheses/brackets."""
    out, depth, cur = [], 0, ""
    for ch in value:
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


def esc(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def anchor(text):
    return re.sub(r"[^a-z0-9-]", "", text.lower().replace(" ", "-"))


# ------------------------------------------------------------------ loaders
def load_aggregates():
    aggs = {}
    for path in sorted(CTX.glob("BC*/aggregates/AGG-*.md")):
        text = path.read_text(encoding="utf-8")
        fm = front_matter(text)
        purpose = re.search(r"\*\*الغرض:\*\* (.*?)\s*$", text, re.M)
        st_open = re.search(r"غير نهائية: (.*)", text)
        st_final = re.search(r"^- نهائية: (.*)", text, re.M)
        final = [s.strip() for s in st_final.group(1).split(",")] if st_final else []
        final = [s for s in final if re.match(r"^[A-Z_]+$", s)]
        a = {"id": fm["id"], "bc": fm["bounded_context"], "slice": fm.get("slice", ""), "title": fm.get("title", ""),
             "purpose": purpose.group(1).strip() if purpose else "", "personal": bool(fm.get("personal_data")), "tier": fm.get("importance_tier", "—"),
             "reqs": list((fm.get("traces") or {}).get("satisfies") or []),
             "open": [s.strip() for s in st_open.group(1).split(",")] if st_open else [], "final": final,
             "exempt": "EXEMPT" in text.split("## الانتقالات")[0], "trans": [], "matrix": {}, "invs": {},
             "path": path.relative_to(SPEC).as_posix()}
        for m in re.finditer(r"^- \*\*(INV-[A-Z0-9-]+)\*\* —\s*(.*)$", text, re.M):
            a["invs"][m.group(1)] = m.group(2).strip()
        for header, rows in tables(text):
            if header[:3] == ["من", "الأمر", "إلى"]:
                for r in rows:
                    frm = ["∅"] if r[0].startswith("∅") else (["*NT"] if r[0].startswith("أي حالة") else
                                                             [s.strip() for s in r[0].split(",")])
                    a["trans"].append({"from": frm, "cmd": r[1], "to": r[2], "guard": r[3], "event": r[4],
                                       "error": r[5] if r[5] not in ("—", "") else None})
            elif header and header[0].startswith("الحالة"):
                cmds = header[1:]
                for r in rows:
                    for c, cell in zip(cmds, r[1:]):
                        a["matrix"][(r[0], c)] = cell
        aggs[a["id"]] = a
    return aggs


def load_catalog(kind, first):
    items = {}
    for path in sorted(CTX.glob(f"BC*/{kind}-*.md")):
        sfx = re.search(r"-(slc[0-9a-z]+)\.md$", path.name).group(1)
        for header, rows in tables(path.read_text(encoding="utf-8")):
            if header and header[0] == first:
                for r in rows:
                    if len(r) == len(header) and re.match(r"(CMD|QRY|EVT)-", r[0]):
                        d = dict(zip(header, r))
                        d.update(_file=path.relative_to(SPEC).as_posix(), _bc=path.parts[-2], _sfx=sfx)
                        items[r[0]] = d
    return items


def load_policies():
    cmd_pol, qry_pol = {}, {}
    for path in sorted((SPEC / "08-security").glob("policies-slc*.md")):
        d = yaml_block(path.read_text(encoding="utf-8"))
        for p in d.get("command_policies") or []:
            cmd_pol[p["command"]] = p
        for p in d.get("query_policies") or []:
            for q in re.findall(r"QRY-[A-Z0-9-]+", str(p.get("query", ""))):
                qry_pol[q] = p
    return cmd_pol, qry_pol


def load_openapi():
    ops = {}
    for path in sorted((SPEC / "05-contracts").glob("openapi-*.md")):
        d = yaml_block(path.read_text(encoding="utf-8"))
        comp = d.get("components") or {}

        def deref(node):
            while isinstance(node, dict) and "$ref" in node:
                kind, name = node["$ref"].split("/")[-2:]
                node = (comp.get(kind) or {}).get(name, {})
            return node or {}

        for p, methods in (d.get("paths") or {}).items():
            for method, op in methods.items():
                if not isinstance(op, dict) or "operationId" not in op:
                    continue
                params = [(x.get("name"), x.get("in"), x.get("required", False))
                          for x in map(deref, op.get("parameters") or []) if "name" in x]
                body = deref((((op.get("requestBody") or {}).get("content") or {}).get("application/json") or {}).get("schema"))
                ops[op["operationId"]] = {"method": method.upper(), "path": p, "params": params,
                                          "body": list((body.get("properties") or {}).keys()),
                                          "required": body.get("required") or [], "responses": sorted((op.get("responses") or {}).keys()),
                                          "offline": bool(op.get("x-offline-capable")), "file": path.name,
                                          "internal": "internal" in path.name or bool(op.get("x-internal"))}
    return ops


def load_asyncapi():
    chan = {}
    for path in sorted((SPEC / "05-contracts").glob("asyncapi-*.md")):
        d = yaml_block(path.read_text(encoding="utf-8"))
        for name, c in (d.get("channels") or {}).items():
            for msg in (c.get("messages") or {}):
                chan[msg] = (name, c.get("address", ""))
    return chan


def load_error_http():
    http = {}
    for path in sorted((SPEC / "05-contracts").glob("errors-*.md")):
        for header, rows in tables(path.read_text(encoding="utf-8")):
            if header and header[0] == "الرمز":
                for r in rows:
                    http.setdefault(r[0].strip("`"), r[1])
    return http


def load_requirements():
    reqs = md_records((SPEC / "02-requirements" / "requirements.md").read_text(encoding="utf-8"), "REQ")
    ucs = md_records((SPEC / "02-requirements" / "use-cases.md").read_text(encoding="utf-8"), "UC")
    return reqs, ucs


# ------------------------------------------------------------------ classification
def agg_ar(aid, aggs):
    return AR_AGG.get(aid, aggs[aid]["title"] if aid in aggs else aid)


def category(aid):
    for cat, members in CATEGORIES.items():
        if aid in members:
            return cat
    return "أساسية"


def verb_of(cmd):
    return cmd.split("-", 2)[2] if cmd.count("-") >= 2 else cmd


def action_phrase(cmd, aid, aggs):
    tmpl = COMMAND_PHRASES.get(cmd) or AR_VERB.get(verb_of(cmd), verb_of(cmd).replace("-", " ").lower() + " {a}")
    return tmpl.format(a=agg_ar(aid, aggs))


def is_create(trs):
    return any(t["from"] == ["∅"] for t in trs)


def closes_and_replaces(trs, a):
    """A command that closes this record and asserts its replacement in the same transaction (e.g. claim correction)."""
    return bool(trs) and all(t["to"] in a["final"] for t in trs) and any(re.search(r"\breplacement\b", t["guard"]) for t in trs)


def op_type(cmd, a, catalog_row):
    trs = [t for t in a["trans"] if t["cmd"] == cmd]
    actor = (catalog_row or {}).get("الفاعل", "")
    if (catalog_row or {}).get("داخلي") == "نعم" or actor.lower().startswith("system"):
        return "نظام"
    if is_create(trs):
        return "إنشاء"
    if verb_of(cmd) in ("ERASE", "DISPOSE"):
        return "حذف / إنهاء"
    if closes_and_replaces(trs, a):
        return "تعديل"
    targets = {t["to"] for t in trs}
    if targets and targets <= set(a["final"]):
        return "حذف / إنهاء"
    if targets == {"="} or targets == {"(بلا تغيير)"}:
        return "تعديل"
    return "سير عمل"


# ---- actor selection: policy subjects list roles with the verbs each may perform, e.g.
# "Planner (request, release) · allocation authority (approve, reject, pre-empt)".
AR_ACTOR_VERBS = {"تبليغ": "report", "إلغاء": "cancel", "تقييم": "assess", "إعادة تقييم": "reassess",
                  "استجابة": "dispatch response", "احتواء": "contain", "حل": "resolve", "إغلاق": "close",
                  "تصعيد": "escalate", "تخفيض": "de-escalate", "تفعيل الاستمرارية": "activate contingency",
                  "تحديد": "identify", "تخطيط المعالجة": "plan treatment"}
QUALIFIERS = ("owner", "in scope", "not self", "self", "scope-limited", "peer", "any", "≠", "platform")
APPROVAL_VERBS = {"approve", "reject", "activate", "confirm", "promote", "publish", "accept"}
VERB_SYNONYMS = {"submit": "draft edit", "discard": "draft edit", "resubmit": "draft edit",
                 "edit": "draft define register create update", "return": "review approve",
                 "reject": "review approve"}


def _stem(word):
    return word.lower().replace("-", "")[:5]


def _verb_list(part):
    """Stems of the verbs in a role's parentheses, or None when the parentheses only qualify the role."""
    m = re.search(r"\(([^)]*)\)", part)
    if not m:
        return None
    items = [x.strip() for x in re.split(r"[,،/]", m.group(1)) if x.strip()]
    if all(x.lower().startswith(QUALIFIERS) for x in items):
        return None
    toks = set()
    for x in items:
        x = AR_ACTOR_VERBS.get(x, x)
        toks |= {_stem(t) for t in re.findall(r"[A-Za-z][A-Za-z-]{2,}", x)}
        toks |= {_stem(t) for t in re.findall(r"[A-Za-z]{3,}", x)}
    return toks


def _role(part):
    return re.sub(r"\s*\((?!in scope|not self|self\b)[^)]*\)", "", part).strip()


def pick_actor(actor, cmd, create=False):
    """Returns (roles, narrowed): the roles allowed to issue this command, and whether the source let us narrow them."""
    vw = [w.lower() for w in verb_of(cmd).split("-")]
    words = {_stem(w) for w in vw if len(w) > 2} | {_stem("".join(vw))}
    words |= {_stem(s) for w in vw for s in VERB_SYNONYMS.get(w, "").split()}
    parts = [p.strip() for p in re.split(r"\s+[·|]\s+|;\s*", actor) if p.strip() and not re.search(r"view only|read only", p)]
    if len(parts) == 1:
        return (parts[0] if _verb_list(parts[0]) is None else _role(parts[0])), True
    hits, bare, textual = {}, [], []
    for i, p in enumerate(parts):
        toks = _verb_list(p)
        if toks is None:
            if "(" not in p and any(_stem(t) == _stem(vw[0]) for t in re.findall(r"[A-Za-z]{3,}", p)):
                textual.append(i)
            elif "(" not in p or _verb_list(p) is None:
                bare.append(i)
            continue
        if words & toks:
            hits[i] = len(words & toks)
    if hits:
        top = max(hits.values())
        general = [i for i in bare if "(" not in parts[i]] if create and vw[0] not in APPROVAL_VERBS else []
        chosen = sorted([i for i, h in hits.items() if h == top] + general)
    elif textual:
        chosen = textual
    elif bare:
        chosen = bare
    else:
        return " · ".join(_role(p) for p in parts), False
    return " · ".join(dict.fromkeys(_role(parts[i]) for i in chosen)), True


def sys_kind(trigger, guard=""):
    t, g = trigger.lower(), guard.lower()
    if re.search(r"condition met|threshold|criteria satisfied|all checks passed", t):
        return "شرطي بعد أمر"
    if re.search(r"\blease\b|worker|\bscan\b|\bjob\b|\bbuild|reproduc|^completed|^failed|error or timeout|integrity|"
                 r"package validated|validation (passed|failed)", t) or re.search(r"\blease\b|worker", g):
        return "مدفوع بعامل"
    if re.search(r"schedul|daily|\bdelay\b|elapsed|expir|reached|deadline|due passed|older than|\bage\b|period|"
                 r"\d+\s*(d|days|h|hours|min|minutes)\b|valid_to|timeout", t + " " + g):
        return "زمني"
    if re.search(r"evt-|event|linked|successor|baselined|committed|released|published|approved|activated|rejected|"
                 r"confirmed|\bhold\b|resolved|closed|retired|arrived|received|delivered|signal|recorded|sealed|annulled|superseded|"
                 r"references|lost visibility", t + " " + g):
        return "مدفوع بحدث"
    return "شرطي بعد أمر"


def expand_from(frm, a):
    if frm == ["*NT"]:
        return [s for s in a["open"]]
    return frm


def show_from(frm):
    return "أي حالة غير نهائية" if frm == ["*NT"] else ", ".join(frm)


def payload_fields(payload):
    out, items, depth, cur = [], [], 0, ""
    for ch in (payload or "").replace("`", "") + " ":
        depth += (ch in "([{") - (ch in ")]}")
        if depth == 0 and (ch.isspace() or ch == ","):
            if cur.strip():
                items.append(cur.strip())
            cur = ""
        else:
            cur += ch
    for item in items:
        m = re.match(r"^(\w+)(!?):(.+)$", item.strip())
        if m:
            out.append((m.group(1), bool(m.group(2)), m.group(3).strip()))
    return out


# ------------------------------------------------------------------ 05 user stories
TYPE_CHECK = {"إنشاء": "C-CRE", "تعديل": "C-UPD", "سير عمل": "C-WF", "حذف / إنهاء": "C-DEL", "جلب": "C-READ",
              "نظام": "C-SYS"}
CAT_CHECK = {"تحليل": "K-ANL", "تقارير ومنتجات": "K-RPT", "تكامل": "K-INT", "حوكمة وأمن": "K-GOV", "أساسية": "K-CORE"}
UNCHANGED = ("=", "(بلا تغيير)")


def reject_states(a, cmd):
    """States the matrix rejects for cmd, plus terminal states the matrix has no row for."""
    rows = {s for s, _ in a["matrix"]}
    rejected = sorted({s for (s, c), cell in a["matrix"].items() if c == cmd and cell.startswith("✗") and s != "∅"})
    return rejected, [f for f in a["final"] if f not in rows]


def guard_clause(code, guard):
    """The clauses of a guard that belong to one error code."""
    clauses = [c.strip() for c in re.split(r";\s*", guard) if c.strip()]
    if len(clauses) <= 1:
        return guard
    keys = {_stem(w) for w in code.lower().split("_") if len(w) > 3 and w not in ("invalid", "required", "denied")}
    clauses = [c for c in clauses if not re.search(r"\bnotified$", c)] or clauses
    rel = [c for c in clauses if keys & {_stem(t) for t in re.findall(r"[A-Za-z]{4,}", c)}]
    if rel:
        return "; ".join(rel)
    rest = [c for c in clauses if not re.match(r"(actor\b|reason\b|.*\bnotified$)", c, re.I)]
    return "; ".join(rest) or guard


def error_condition(code, cmd, a, pol, trs, mandatory):
    if code == "AUTHZ_DENIED":
        return (f"السياسة {pol.get('id', '—')} ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، "
                "و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`)")
    if code == "VALIDATION_FAILED":
        return "حقل إلزامي مفقود أو غير صالح" + (f": {', '.join(mandatory)}" if mandatory else "")
    if code == "VERSION_CONFLICT":
        return "قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد)"
    if code == "IDEMPOTENCY_KEY_REUSED":
        return "نفس Idempotency-Key مع حمولة مختلفة"
    if code.endswith("_INVALID_STATE_TRANSITION"):
        rejected, missing = reject_states(a, cmd)
        if not rejected and not missing:
            return "لا حالة في المصفوفة يُرفض منها هذا الأمر؛ الرمز لا يُتوقع حدوثه"
        text = "الحالة الحالية واحدة من: " + ", ".join(rejected + missing)
        if missing:
            text += (f" — الحالات النهائية {', '.join(missing)} بلا صف في المصفوفة، وأُضيفت لأن الحالة النهائية "
                     "لا تقبل أوامر **[Derived]**")
        return text
    if code == "SEGREGATION_OF_DUTIES":
        sod = pol.get("segregation_of_duties", "—")
        return f"فصل المهام: {sod}" if sod not in ("—", "", None) else "المنفّذ هو نفسه من يُمنع عليه ذلك (فصل المهام)"
    if code == "REASON_REQUIRED":
        return "لم يُذكر السبب"
    guards = list(dict.fromkeys(guard_clause(code, t["guard"]) for t in trs if t.get("error") == code))
    if guards:
        return "لم يتحقق الشرط: " + " | ".join(guards)
    for inv, text in a["invs"].items():
        if code in text:
            m = re.search(r"except ([A-Z_]+(?:(?:, | and )[A-Z_]+)*)", text)
            exempt = m and verb_of(cmd).replace("-", "_") in re.findall(r"[A-Z_]+", m.group(1))
            if exempt or is_create(trs):
                return (f"لا ينطبق على هذا الأمر وفق {inv} ({esc(text)})؛ ذكره في كتالوج الأوامر يناقض الثابت "
                        "**[Needs Review]**")
            return f"{inv}: {esc(text)}"
    return "انظر شرط الانتقال وكتالوج الأخطاء"


def when_actor(roles):
    names = [r.split("(")[0].strip() for r in roles.split(" · ")]
    return names[0] if len(names) == 1 else "an authorized actor (" + " or ".join(names) + ")"


def command_story(cid, c, a, aggs, pol, reqs_txt, ucs_of, http_of, ops, stats):
    trs = [t for t in a["trans"] if t["cmd"] == cid]
    typ = op_type(cid, a, c)
    cat = category(a["id"])
    create = is_create(trs)
    actor, narrowed = pick_actor(str(pol.get("subject") or c["الفاعل"]), cid, create)
    resolved = cid in ACTOR_RESOLUTION
    if resolved:
        actor, narrowed = ACTOR_RESOLUTION[cid][0], True
    if not narrowed:
        stats["unnarrowed"] += 1
    fields = payload_fields(c.get("الحمولة (! إلزامي)", ""))
    mandatory = [n for n, req, _ in fields if req]
    events = re.findall(r"EVT-[A-Z0-9-]+", c["الأحداث"])
    errors = [e.strip() for e in c["الأخطاء"].split(",") if e.strip() and e.strip() != "—"]
    op = ops.get(cid, {})
    sid = f"US-{a['bc']}-{cid[4:]}"
    to_txt = lambda t: "(بلا تغيير)" if t in UNCHANGED else t  # noqa: E731
    checks = TYPE_CHECK[typ] + ("، C-CRE" if typ == "نظام" and create else "")
    actor_cell = esc(actor) + ("" if narrowed else " **[Needs Review]**") + (" (محسوم: `17-security-design.md` §5)" if resolved else "")
    L = [f"#### {sid} — {action_phrase(cid, a['id'], aggs)}", "",
         "| النوع | الفئة | الفاعل | الواجهة | السياسة |", "|---|---|---|---|---|",
         f"| {typ} | {cat} | {actor_cell} | `{op.get('method', '?')} {op.get('path', c['HTTP'].strip('`'))}` | {pol.get('id', '—')} |", "",
         f"**القصة:** بصفتي **{esc(actor)}**، أريد **{action_phrase(cid, a['id'], aggs)}**، لكي يتحقق غرض {agg_ar(a['id'], aggs)}: {esc(a['purpose']) or '—'}", ""]
    if len(trs) == 1:
        t = trs[0]
        guard = t["guard"] if t["guard"] not in ("—", "") else "لا شروط إضافية"
        L.append(f"- **الشروط المسبقة:** الحالة الحالية: {show_from(t['from'])}؛ {esc(guard)}")
    else:
        L.append("- **الشروط المسبقة (لكل انتقال):**")
        L += [f"  - من {show_from(t['from'])} ← {to_txt(t['to'])}: {esc(t['guard'] if t['guard'] not in ('—', '') else 'لا شروط إضافية')}"
              for t in trs]
    L += [f"- **المدخلات:** " + (", ".join(f"`{n}`{'!' if r else ''}: {esc(t)}" for n, r, t in fields) if fields else "لا حمولة")
          + " — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`" + ("" if create else " و`If-Match`"),
          f"- **المخرجات:** الحالة ← {', '.join(dict.fromkeys(to_txt(t['to']) for t in trs))}؛ الحدث {', '.join(events) or '—'}؛ "
          f"الاستجابة `ResourceRef` (urn، id، version، state)",
          f"- **الصلاحية:** {esc(pol.get('subject', '—'))}؛ الشروط: {esc(pol.get('context_conditions', '—'))}؛ فصل المهام: {esc(pol.get('segregation_of_duties', '—'))}؛ الالتزامات: {esc(pol.get('obligations', '—'))}",
          f"- **الربط:** `{cid}` · `{a['id']}` · متطلبات: {', '.join(a['reqs']) or '—'} · حالات استخدام: {', '.join(ucs_of(a)) or '—'}",
          f"- **ضوابط النوع والفئة:** {checks}، {CAT_CHECK[cat]} (التعريف في [00-guide.md](00-guide.md))", "",
          "```gherkin"]
    send = f"  When {when_actor(actor)} sends {cid} with a valid payload, a new Idempotency-Key" + ("" if create else " and a matching If-Match")
    outbox = f"  And {', '.join(events) or 'no event'} is written to the outbox with one audit record in the same transaction"
    if len(trs) == 1:
        t = trs[0]
        then = "the state is unchanged and the version increases by one" if t["to"] in UNCHANGED else f"the state becomes {t['to']}"
        L += [f"Scenario: {cid} succeeds",
              f"  Given {a['id']} " + ("does not exist yet" if t["from"] == ["∅"] else f"in state {' or '.join(expand_from(t['from'], a))}") + " and every guard holds",
              send, f"  Then {then}", outbox, ""]
    else:
        L += [f"Scenario Outline: {cid} succeeds from each allowed state",
              f"  Given {a['id']} in state <from> and the guard for that transition holds", send,
              "  Then the state becomes <to>",
              "  And <event> is written to the outbox with one audit record in the same transaction", "",
              "  Examples:", "    | from | to | event |"]
        L += [f"    | {f} | {'unchanged' if t['to'] in UNCHANGED else t['to']} | {t['event']} |" for t in trs for f in expand_from(t["from"], a)]
        L.append("")
    L += [f"Scenario Outline: {cid} is rejected",
          "  When the command is sent while <condition>",
          "  Then it is rejected with <code> (HTTP <http>) and nothing changes", "",
          "  Examples:",
          "    | code | http | condition |"]
    for code in errors:
        L.append(f"    | {code} | {http_of.get(code, '?')} | {esc(error_condition(code, cid, a, pol, trs, mandatory))} |")
    L += ["```", ""]
    return sid, typ, cat, L


WHO = "من يحق له (السياسة قبل الاسترجاع — SL-09)"
SCOPE_LIKE = re.compile(r"allowed_scope|^scope\b|label rule|pool scope|^same as|per-node", re.I)


def query_actor(q, pol, pol_q):
    subj = str(pol.get("subject") or "")
    m = re.match(r"same as (QRY-[A-Z0-9-]+)", subj)
    if m:
        subj = str(pol_q.get(m.group(1), {}).get("subject") or "")
    if not subj or SCOPE_LIKE.search(subj):
        subj = q.get(WHO, "")
    if not subj or SCOPE_LIKE.search(subj):
        subj = "مستخدم مخوَّل (ضمن allowed_scope)"
    return subj


def query_story(qid, q, a, aggs, pol, pol_q, reqs, ops):
    op = ops.get(qid, {})
    cat = category(a["id"]) if a else "أساسية"
    subject = query_actor(q, pol, pol_q)
    req_ids = re.findall(r"REQ-[A-Z]+-\d+", q.get("المتطلب", ""))
    why = reqs.get(req_ids[0], {}).get("statement", "") if req_ids else ""
    params = [(n, r) for n, where, r in op.get("params", []) if where == "query"]
    body = [(n, n in op.get("required", [])) for n in op.get("body", [])]
    names = [n for n, _ in params + body]
    paged = any(n in ("cursor", "limit") for n in names)
    asof = [n for n in names if n in ("valid_at", "known_at", "as_of", "at")]
    purpose = any(n == "X-Purpose" for n, _, _ in op.get("params", []))
    method, path = op.get("method", "?"), op.get("path", q["HTTP"].strip("`"))
    kind = "list" if paged else ("check" if method == "POST" else "item")
    bc = a["bc"] if a else q["_bc"]
    sid = f"US-{bc}-Q-{qid[4:]}"
    inputs = ", ".join(f"`{n}`{'!' if r else ''}" for n, r in params + body) or "معاملات المسار فقط"
    L = [f"#### {sid} — جلب: {esc(q.get('يعيد', ''))}", "",
         "| النوع | الفئة | الفاعل | الواجهة | السياسة |", "|---|---|---|---|---|",
         f"| جلب | {cat} | {esc(subject)} | `{method} {path}` | {pol.get('id', '—')} |", "",
         f"**القصة:** بصفتي **{esc(subject)}**، أريد **جلب {esc(q.get('يعيد', ''))}**، لكي يتحقق المتطلب: {esc(why.rstrip('.')) or '—'}", "",
         f"- **المدخلات:** {inputs}" + (" (معاملات الرابط وحقول جسم الطلب؛ `!` = إلزامي)" if body else "") + ("؛ مع ترويسة `X-Purpose`" if purpose else ""),
         f"- **المخرجات:** {esc(q.get('يعيد', ''))}" + ("؛ صفحة بمؤشر (لا offset — FIT-13)" if paged else ""),
         f"- **الصلاحية:** {esc(pol.get('subject', '—'))}؛ النطاق المسموح: {esc(pol.get('allowed_scope', '—'))}؛ عند الرفض: {esc(pol.get('otherwise', 'DENY (not-found shape)'))}",
         f"- **الزمن:** " + (f"استعلام بأثر رجعي عبر {', '.join('`' + x + '`' for x in asof)}" if asof else "الحالة الحالية"),
         f"- **الربط:** `{qid}` · {('`' + a['id'] + '`') if a else 'عابر للـAggregates'} · متطلبات: {', '.join(req_ids) or '—'}",
         f"- **ضوابط النوع والفئة:** C-READ، {CAT_CHECK[cat]}", "", "```gherkin"]
    if kind == "list":
        L += [f"Scenario: {qid} returns only what the caller may see",
              "  Given items inside and outside the caller's allowed_scope",
              f"  When the caller sends {qid} with a cursor",
              "  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)",
              "  And no count, facet or suggestion reveals a hidden item"]
    elif kind == "item":
        L += [f"Scenario: {qid} returns a visible item",
              "  Given the item exists and the policy allows the caller",
              f"  When the caller sends {qid}",
              "  Then the item is returned after the result re-check (security_version, LabelCheck)", "",
              f"Scenario: {qid} hides an item the caller may not see",
              "  Given the item exists but the policy denies the caller",
              f"  When the caller sends {qid}",
              "  Then the response is 404 with the same shape as for a missing item"]
    else:
        L += [f"Scenario: {qid} computes its result only over what the caller may see",
              "  Given data inside and outside the caller's allowed_scope",
              f"  When the caller sends {qid}",
              "  Then the result neither includes nor reveals data outside allowed_scope"]
    if kind != "item":
        L += ["", f"Scenario: {qid} is denied",
              "  Given the policy denies the caller",
              f"  When the caller sends {qid}",
              "  Then the response has the same shape as for a missing item (not-found shape)"]
    L += ["```", ""]
    return sid, L


def sys_story(a, t, aggs, n):
    trig = t["cmd"][4:].strip()
    kind = sys_kind(trig, t["guard"])
    to = "(بلا تغيير)" if t["to"] in UNCHANGED else t["to"]
    sid = f"US-{a['bc']}-S-{a['id'][4:]}-{n:02d}"
    L = [f"#### {sid} — تلقائي: {esc(trig)} ({agg_ar(a['id'], aggs)})", "",
         "| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |", "|---|---|---|---|---|",
         f"| نظام | {kind} | النظام بهوية عبء عمل | {show_from(t['from'])} | {to} |", "",
         f"**القصة:** بصفتي **النظام**، عند «{esc(trig)}»، أريد {'تحديث **' + agg_ar(a['id'], aggs) + '** دون تغيير حالته' if to == '(بلا تغيير)' else 'نقل **' + agg_ar(a['id'], aggs) + '** إلى ' + to}، لكي يتحقق غرض {agg_ar(a['id'], aggs)}: {esc(a['purpose']) or '—'}", "",
         f"- **الشرط:** {esc(t['guard'])}",
         f"- **المخرجات:** الحدث {t['event']}؛ سجل تدقيق بهوية النظام",
         f"- **الربط:** `{a['id']}` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)",
         "- **ضوابط النوع:** C-SYS", ""]
    return sid, L


def build_user_stories(aggs, cmds, qrys, pol_c, pol_q, reqs, ucs, http_of, ops):
    req_to_uc = defaultdict(set)
    for rid, r in reqs.items():
        for u in re.findall(r"UC-\d+", r.get("use_cases", "")):
            req_to_uc[rid].add(u)
    ucs_of = lambda a: sorted({u for r in a["reqs"] for u in req_to_uc.get(r, ())})  # noqa: E731
    prefix_agg, path_agg = {}, defaultdict(set)
    for cid, c in cmds.items():
        prefix_agg.setdefault((c["_bc"], cid.split("-")[1]), c["Aggregate"])
        if cid in ops:
            path_agg["/".join(ops[cid]["path"].split("/")[:5])].add(c["Aggregate"])

    def home(qid):
        """The aggregate a query belongs to: the one whose commands share its resource path, else its ID prefix."""
        owners = path_agg.get("/".join(ops.get(qid, {}).get("path", "").split("/")[:5]), set())
        if len(owners) == 1:
            return next(iter(owners))
        return prefix_agg.get((qrys[qid]["_bc"], qid.split("-")[1]))
    counters = defaultdict(int)
    stats = defaultdict(lambda: defaultdict(int))
    per_bc = defaultdict(list)
    story_ids = {}
    for bc in sorted(BC_NAMES):
        members = sorted(x for x in aggs if aggs[x]["bc"] == bc)
        L = []
        for aid in members:
            a = aggs[aid]
            L += [f"### {aid} — {agg_ar(aid, aggs)} ({a['title']})", "",
                  f"`{a['path']}` · {a['slice']} · الحالات: {', '.join(a['open'])} → {', '.join(a['final']) or '—'}", ""]
            for cid in sorted(c for c in cmds if cmds[c]["Aggregate"] == aid):
                sid, typ, cat, block = command_story(cid, cmds[cid], a, aggs, pol_c.get(cid, {}), reqs, ucs_of, http_of, ops, counters)
                L += block
                stats[bc][typ] += 1
                story_ids[cid] = sid
            n = 0
            for t in a["trans"]:
                if t["cmd"].startswith("SYS:"):
                    n += 1
                    sid, block = sys_story(a, t, aggs, n)
                    L += block
                    stats[bc]["نظام (SYS)"] += 1
            for qid in sorted(q for q in qrys if qrys[q]["_bc"] == bc and home(q) == aid):
                sid, block = query_story(qid, qrys[qid], a, aggs, pol_q.get(qid, {}), pol_q, reqs, ops)
                L += block
                stats[bc]["جلب"] += 1
                story_ids[qid] = sid
        orphan_q = sorted(q for q in qrys if qrys[q]["_bc"] == bc and q not in story_ids)
        if orphan_q:
            L += ["### استعلامات عابرة للـAggregates", ""]
            for qid in orphan_q:
                sid, block = query_story(qid, qrys[qid], None, aggs, pol_q.get(qid, {}), pol_q, reqs, ops)
                L += block
                stats[bc]["جلب"] += 1
                story_ids[qid] = sid
        per_bc[bc] = L
    cat_rows = defaultdict(list)
    for aid in sorted(aggs):
        cat_rows[category(aid)].append(f"{agg_ar(aid, aggs)} (`{aid[4:]}`)")
    totals = defaultdict(int)
    for v in stats.values():
        for k, n in v.items():
            totals[k] += n
    sys_rows = [(a["id"], t["cmd"]) for a in aggs.values() for t in a["trans"] if t["cmd"].startswith("SYS:")]
    write_generated(OUT / "05-user-stories" / "00-guide.md", None, "\n".join(
        [BEGIN, "| الفئة | الـAggregates | العدد |", "|---|---|---|"] +
        [f"| {c} | {'، '.join(v)} | {len(v)} |" for c, v in sorted(cat_rows.items())] +
        ["", "**الأعداد الحالية (مولَّدة):** " + "، ".join(f"{k}: {v}" for k, v in sorted(totals.items())) +
         f"؛ المجموع {sum(totals.values())}. قواعد `SYS:` {len(sys_rows)} صفًا ({len(set(sys_rows))} محفِّزًا مميزًا؛ "
         "الصف المكرر محفِّز واحد من حالتين إلى هدفين مختلفين). "
         f"أوامر لم يُحدَّد فاعلها بدقة من المصدر: {counters['unnarrowed']} (معلَّمة **[Needs Review]** في جدول القصة).", END]))
    for bc, L in per_bc.items():
        head = [BEGIN, "", f"## ملخص {bc}", "", "| نوع العملية | عدد القصص |", "|---|---|"]
        head += [f"| {k} | {v} |" for k, v in sorted(stats[bc].items())] + [f"| **المجموع** | **{sum(stats[bc].values())}** |", ""]
        write_generated(OUT / "05-user-stories" / f"us-{bc.lower()}.md",
                        f"---\nid: AD-05-US-{bc}\ntype: user-stories\ntitle: \"قصص المستخدم — {bc}\"\nstatus: DRAFT\n"
                        "phase: \"Phase 3.8 — 18-analysis-design (المرحلة 2)\"\ngenerator: 17-system-study/_build/build_analysis_design.py\n---\n\n"
                        f"# قصص المستخدم — {bc} {BC_NAMES[bc]}\n\n"
                        "مولَّد بالكامل من المصادر بواسطة `17-system-study/_build/build_analysis_design.py`؛ لا يُحرَّر يدويًا. "
                        "القالب والتصنيف وتعريف ضوابط النوع والفئة في [00-guide.md](00-guide.md).\n",
                        "\n".join(head + L + [END]))
    return stats, story_ids


# ------------------------------------------------------------------ 08 state models
def mm_label(text):
    return re.sub(r"[:;#{}\"]", " ", text).strip()


def build_state_models(aggs):
    L = [BEGIN, "", "## الفهرس", "", "| BC | Aggregates |", "|---|---|"]
    for bc in sorted(BC_NAMES):
        L.append(f"| {bc} | " + " · ".join(f"[{x[4:]}](#{anchor(x)})" for x in sorted(aggs) if aggs[x]["bc"] == bc) + " |")
    for bc in sorted(BC_NAMES):
        L += ["", f"## {bc} — {BC_NAMES[bc]}"]
        for aid in sorted(x for x in aggs if aggs[x]["bc"] == bc):
            a = aggs[aid]
            edges, selfs, groups = defaultdict(list), [], {}
            for t in a["trans"]:
                label = t["cmd"][4:].strip() if t["cmd"].startswith("SYS:") else verb_of(t["cmd"])
                label = ("SYS " if t["cmd"].startswith("SYS:") else "") + mm_label(label)
                froms = expand_from(t["from"], a)
                if t["to"] in ("=", "(بلا تغيير)"):
                    selfs += [(f, label) for f in froms]
                elif t["from"] == ["*NT"] or (len(froms) >= 3 and set(froms) == set(a["open"])):
                    edges[("ANY_NT", t["to"])].append(label)
                elif len(froms) >= 4:
                    key = tuple(sorted(froms))
                    groups.setdefault(key, f"G{len(groups) + 1}")
                    edges[(groups[key], t["to"])].append(label)
                else:
                    for f in froms:
                        edges[("[*]" if f == "∅" else f, t["to"])].append(label)
            L += ["", f"### {aid}", "", f"**{agg_ar(aid, aggs)}** — {a['title']} · `{a['path']}`" +
                  (" · **SL-06 EXEMPT** (لا حالة نهائية بالتصميم)" if a["exempt"] else ""), "", "```mermaid", "stateDiagram-v2"]
            if any(f == "ANY_NT" for f, _ in edges):
                L.append('  state "any non-terminal state" as ANY_NT')
            for key, gid in groups.items():
                L.append(f'  state "any of {len(key)} states" as {gid}')
            for (f, t), labels in edges.items():
                L.append(f"  {f} --> {t} : {' / '.join(dict.fromkeys(labels))}")
            for s in a["final"]:
                L.append(f"  {s} --> [*]")
            L += ["```", ""]
            if groups:
                L += ["مجموعات الحالات في المخطط: " + "؛ ".join(f"**{gid}** = {', '.join(key)}" for key, gid in groups.items()), ""]
            if selfs:
                grouped = defaultdict(set)
                for f, lab in selfs:
                    grouped[lab].add(f)
                L += ["أوامر لا تغيّر الحالة: " + "؛ ".join(f"«{lab}» في {', '.join(sorted(fs))}" for lab, fs in sorted(grouped.items())), ""]
    L.append(END)
    write_generated(OUT / "08-state-models.md", None, "\n".join(L))


# ------------------------------------------------------------------ 09 business rules
def build_business_rules(aggs, cmds, pol_c, reqs):
    brl = md_records((SPEC / "01-business" / "business-rules.md").read_text(encoding="utf-8"), "BRL")
    req_aggs = defaultdict(list)
    for aid, a in aggs.items():
        for r in a["reqs"]:
            req_aggs[r].append(aid)
    agg_text = {aid: (SPEC / a["path"]).read_text(encoding="utf-8") for aid, a in aggs.items()}
    L = [BEGIN, "", "## 1. قواعد العمل العليا (BRL)", "",
         "«يُنفِّذها» من حقل `enforced_by` في القاعدة؛ «متطلبات تذكرها كمصدر» متطلبات حقل `source` فيها يسمّي القاعدة ولا يذكرها "
         "`enforced_by` (فجوة ربط في المصدر **[Needs Review]**)؛ الـAggregates **[Derived]**: ما يحقق أحد هذه المتطلبات، أو يذكر القاعدة نصًا.", "",
         "| القاعدة | النص | يُنفِّذها | متطلبات تذكرها كمصدر | الـAggregates |", "|---|---|---|---|---|"]
    for bid, b in sorted(brl.items()):
        enf = re.findall(r"REQ-[A-Z]+-\d+", b.get("enforced_by", ""))
        extra = sorted(r for r, v in reqs.items() if re.search(rf"\b{bid}\b", v.get("source", "")) and r not in enf)
        ag = sorted({x for r in enf + extra for x in req_aggs.get(r, [])} |
                    {aid for aid, t in agg_text.items() if re.search(rf"\b{bid}\b", t)})
        L.append(f"| {bid} | {esc(b.get('statement', ''))} | {', '.join(enf) or esc(b.get('enforced_by', '—'))} | "
                 f"{', '.join(extra) or '—'} | {', '.join(ag) or '—'} |")
    rd_ids = set(re.findall(r"RD-[A-Z0-9-]*[A-Z0-9]", (SPEC / "04-information" / "reference-data.md").read_text(encoding="utf-8")))
    total_inv = sum(len(a["invs"]) for a in aggs.values())
    L += ["", f"## 2. القواعد حسب الـAggregate ({total_inv} ثابتًا)", ""]
    for bc in sorted(BC_NAMES):
        L += [f"### {bc} — {BC_NAMES[bc]}", ""]
        for aid in sorted(x for x in aggs if aggs[x]["bc"] == bc):
            a = aggs[aid]
            L += [f"#### {aid} — {agg_ar(aid, aggs)}", ""]
            if a["invs"]:
                L += ["**الثوابت:**", ""] + [f"- **{k}** — {esc(v)}" for k, v in a["invs"].items()] + [""]
            guards = [t for t in a["trans"] if t["guard"] not in ("—", "")]
            if guards:
                L += ["**شروط الانتقال (قواعد التحقق):**", "", "| الأمر / المحفِّز | من | الشرط | خطأ الفشل |", "|---|---|---|---|"]
                L += [f"| {t['cmd']} | {show_from(t['from'])} | {esc(t['guard'])} | {t['error'] or '—'} |" for t in guards] + [""]
            sod = [(c, pol_c[c]["segregation_of_duties"]) for c in sorted(cmds) if cmds[c]["Aggregate"] == aid
                   and c in pol_c and str(pol_c[c].get("segregation_of_duties", "—")) not in ("—", "", "None")]
            if sod:
                L += ["**فصل المهام:** " + "؛ ".join(f"{c}: {esc(s)}" for c, s in sod), ""]
            cited = set(re.findall(r"(?<![A-Z-])RD-[A-Z][A-Z0-9-]*[A-Z0-9]", " ".join(t["guard"] for t in a["trans"])))
            if cited:
                bits = ([", ".join(sorted(cited & rd_ids)) + " (`04-information/reference-data.md`)"] if cited & rd_ids else []) + \
                       (["غير معرَّفة في `reference-data.md` **[Missing]**: " + ", ".join(sorted(cited - rd_ids))] if cited - rd_ids else [])
                L += ["**بيانات مرجعية مستخدمة:** " + " · ".join(bits), ""]
    L.append(END)
    write_generated(OUT / "09-business-rules.md", None, "\n".join(L))
    return total_inv


# ------------------------------------------------------------------ 14 API design
def build_api(ops, cmds, qrys, pol_c, pol_q, aggs):
    bc_of = {**{k: v["_bc"] for k, v in cmds.items()}, **{k: v["_bc"] for k, v in qrys.items()}}
    by_bc = defaultdict(list)
    for oid, o in ops.items():
        by_bc[bc_of.get(oid, "—")].append((oid, o))
    L = [BEGIN, "", "### ملخص الكتالوج", "", f"إجمالي العمليات: **{len(ops)}**.", "",
         "| BC | أوامر | استعلامات | داخلية | المجموع |", "|---|---|---|---|---|"]
    for bc in sorted(by_bc):
        items = by_bc[bc]
        L.append(f"| {bc} | {sum(1 for o, _ in items if o.startswith('CMD-'))} | {sum(1 for o, _ in items if o.startswith('QRY-'))} | "
                 f"{sum(1 for _, x in items if x['internal'])} | {len(items)} |")
    for bc in sorted(by_bc):
        L += ["", f"#### {bc} — {BC_NAMES.get(bc, 'عقود عابرة')}", ""]
        groups = defaultdict(list)
        for oid, o in by_bc[bc]:
            seg = o["path"].split("/")
            groups["/".join(seg[:5])].append((oid, o))
        for res in sorted(groups):
            L += [f"##### `{res}`", "", "| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |",
                  "|---|---|---|---|---|---|---|---|"]
            for oid, o in sorted(groups[res], key=lambda x: (x[1]["path"], x[1]["method"])):
                if oid.startswith("CMD-"):
                    c = cmds.get(oid, {})
                    kind = op_type(oid, aggs[c["Aggregate"]], c) if c.get("Aggregate") in aggs else "أمر"
                    pol = pol_c.get(oid, {}).get("id", "—")
                    fields = payload_fields(c.get("الحمولة (! إلزامي)", ""))
                    inputs = ", ".join(f"{n}{'!' if r else ''}" for n, r, _ in fields) or "—"
                    special = ", ".join(e.strip() for e in c.get("الأخطاء", "").split(",") if e.strip() not in GENERIC + ["", "—"]) or "—"
                else:
                    kind, pol = "جلب", pol_q.get(oid, {}).get("id", "—")
                    inputs = ", ".join([f"{n}{'!' if r else ''}" for n, where, r in o["params"] if where == "query"] +
                                       [f"{n}{'!' if n in o['required'] else ''}" for n in o["body"]]) or "—"
                    special = "—"
                if o["internal"]:
                    kind += " (داخلي)"
                if o["offline"]:
                    kind += " · دون اتصال"
                L.append(f"| {o['method']} | `{o['path']}` | {oid} | {kind} | {pol} | {esc(inputs)} | {', '.join(o['responses'])} | {esc(special)} |")
            L.append("")
    L.append(END)
    write_generated(OUT / "14-api-design.md", None, "\n".join(L))


# ------------------------------------------------------------------ 15 event design
def build_events(evts, chan, aggs):
    by_ch = defaultdict(list)
    for eid, e in evts.items():
        by_ch[chan.get(eid, ("—", "—"))].append((eid, e))
    L = [BEGIN, "", "### ملخص القنوات", "", "| القناة | العنوان | عدد الأحداث |", "|---|---|---|"]
    L += [f"| {c[0]} | `{c[1]}` | {len(v)} |" for c, v in sorted(by_ch.items())]
    for c, items in sorted(by_ch.items()):
        L += ["", f"#### {c[0]} — `{c[1]}`", "", "| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |", "|---|---|---|---|---|"]
        for eid, e in sorted(items):
            L.append(f"| {eid} | {e['Aggregate']} | {esc(e['ينتجه'])} | {esc(e['يؤثر أمنياً'])} | {esc(e['المستهلكون'])} |")
    L += ["", END]
    write_generated(OUT / "15-event-design.md", None, "\n".join(L))
    return len(evts)


# ------------------------------------------------------------------ 16 database schema
def col_type(col):
    c = col.lower()
    if "**pii**" in c or "pii" in c:
        return "json_pii" if "json" in c else "text_pii"
    if "(enc)" in c or "wrapped_key" in c:
        return "bytes_encrypted"
    if "json" in c:
        return "json"
    if c.startswith(("geom", "geometry", "footprint", "area_geom", "location_geom")) or "(4326)" in c:
        return "geometry(4326)"
    if c.endswith("[]") or "(array)" in c or "[]" in c:
        return "array"
    base = clean_col(c).lower()
    if base in ("window", "period", "validity") or base.endswith("_window") or "tstzrange" in c:
        return "period"
    if base.endswith("_at") or base in ("valid_from", "valid_to", "window_from", "window_to", "needed_by", "due",
                                        "recorded_from", "recorded_to", "known_at", "observed_month"):
        return "timestamptz"
    if base.endswith(("_id", "_ref", "_urn", "_by")) or base in ("urn", "owner", "requester", "assignee", "reviewer", "actor",
                                                                  "approver", "author", "holder", "follow_up_of", "subject"):
        return "urn"
    if base in ("version", "seq", "attempt", "attempts", "depth", "priority", "occurrences") or base.endswith(("_version", "_count")):
        return "integer"
    if base in ("state", "kind", "status", "severity", "result", "purpose", "direction", "protocol"):
        return "enum"
    if base == "label" or base.endswith("_label"):
        return "security_label"
    if base.startswith(("is_", "has_", "include_", "requires_")) or base in ("delegable", "locked", "sealed", "suspended", "enabled"):
        return "boolean"
    if base.endswith("quantity") or base in ("likelihood", "impact", "score", "risk_score"):
        return "numeric"
    return "text"


def clean_col(col):
    name = re.sub(r"\(.*", "", col).strip()
    toks = name.replace("**", "").strip().split()
    name = (toks[0] + "_" + toks[1] if len(toks) > 1 and toks[1] in ("ref", "refs", "id", "ids", "urn", "urns") else
            (toks[0] if toks else "")).rstrip("?").strip()
    return re.sub(r"[^A-Za-z0-9_]", "_", name).strip("_")


def key_cols(key):
    return [clean_col(c) for c in key.strip().strip("()").split(",") if clean_col(c)]


def _stemcol(name):
    return re.sub(r"_(ref|id|urn)$", "", name)


STANDARD_TABLES = ("outbox", "audit_outbox", "inbox", "idempotency_keys")


def load_ldm():
    """Tables per (schema, name), merging later-slice extensions; returns tables, projections, device stores,
    naming drift between slices, and the standard / history tables that were not catalogued."""
    tables_out, projections, client, drift, skipped = {}, [], [], [], defaultdict(set)
    for path in sorted((SPEC / "06-data" / "logical-model").glob("slc-*.md")):
        text = path.read_text(encoding="utf-8")
        title = re.search(r"^# .*$", text, re.M)
        file_schema = re.findall(r"`([a-z]+)`", title.group(0)) if title else []
        current = file_schema[0] if len(file_schema) == 1 else None
        sfx = path.stem
        for block in re.split(r"\n(?=## )", text):
            h = re.match(r"## (BC0\d)(?: — (?:schema )?`?([a-z]+)`?)?", block)
            if h:
                current = h.group(2) or {"BC03": "intelligence", "BC04": "operations"}.get(h.group(1), current)
            if block.startswith("## Device"):
                for header, rows in tables(block):
                    client += [(r[0], r[1]) for r in rows]
                continue
            for header, rows in tables(block):
                if not header or header[0] not in ("الجدول", "الوثيقة / الجدول") or len(header) < 4:
                    continue
                for r in rows:
                    raw = r[0]
                    tag = re.search(r"\(([a-z]+)[,)]", raw)
                    if tag and tag.group(1) in SCHEMA_BC:
                        current = tag.group(1)
                    name = re.sub(r"\s*\(.*\)", "", raw).strip()
                    if header[0].startswith("الوثيقة") or "BC07 store" in raw or name.startswith("projection_") or "projection docs" in name:
                        projections.append({"name": name, "key": r[1], "cols": r[2], "notes": r[3], "slice": sfx})
                        continue
                    if name.startswith("*_") or name in STANDARD_TABLES or name.startswith("security_versions") or name.endswith("_history"):
                        skipped[name].add(sfx)
                        continue
                    schema = current or "—"
                    if "." in name:
                        schema, name = name.split(".", 1)
                    ephemeral = "ephemeral" in raw
                    cols = [c for c in split_top(r[2]) if not c.startswith("...")]
                    key, _, part = r[1].partition("·")
                    key, part = key.strip(), part.replace("**", "").strip()
                    if not part and re.search(r"partition", r[3], re.I):
                        part = next(x.strip() for x in re.split(r"[;.]", r[3]) if re.search(r"partition", x, re.I))
                    tid = (schema, name)
                    if tid in tables_out:
                        t = tables_out[tid]
                        have = {clean_col(x): x for x in t["cols"]}
                        for c in cols:
                            cn = clean_col(c)
                            if cn in have:
                                continue
                            twin = next((h for h in have if _stemcol(h) == _stemcol(cn)), None)
                            if twin:
                                drift.append((f"{schema}.{name}", f"`{twin}` ({t['slice']}) / `{cn}` ({sfx})"))
                            else:
                                t["cols"].append(c)
                        if key_cols(key) != key_cols(t["key"]):
                            drift.append((f"{schema}.{name}", f"المفتاح `{t['key']}` ({t['slice']}) / `{key}` ({sfx})"))
                        t["ext"].append(f"{sfx}: {r[3]}")
                    else:
                        tables_out[tid] = {"schema": schema, "name": name, "key": key, "cols": cols,
                                           "constraints": r[3], "slice": sfx, "ephemeral": ephemeral, "partition": part,
                                           "ext": [f"{sfx}: {r[3]}"] if "extended" in raw or "unchanged" in raw else []}
    return tables_out, projections, client, drift, skipped


def infer_fks(items):
    """FK = column x_id whose owner table in the same schema is keyed (tenant_id, x_id) and named after x
    (x → xs, x_ies, *_xs). *_ref columns are URNs that may point to several types or contexts, so they are not FKs."""
    owners = {}
    for t in items:
        k = [c for c in key_cols(t["key"]) if c != "tenant_id"]
        if len(k) == 1 and k[0].endswith("_id"):
            owners.setdefault(k[0], []).append(t["name"])
    rels = []
    for t in items:
        own = [c for c in key_cols(t["key"]) if c != "tenant_id"]
        for cn in dict.fromkeys(key_cols(t["key"]) + [clean_col(c) for c in t["cols"]]):
            if cn == "tenant_id" or own == [cn] or not cn.endswith("_id"):
                continue
            base = cn[:-3]
            base = base[len("parent_"):] if base.startswith("parent_") else base
            names = (base + "s", base + "es", base[:-1] + "ies", base)
            cands = [n for n in owners.get(base + "_id", []) if n in names or n.endswith(tuple("_" + x for x in names))]
            if len(cands) == 1:
                rels.append((t["name"], cands[0], cn))
    return rels


def build_database(aggs):
    tabs, projections, client, drift, skipped = load_ldm()
    by_schema = defaultdict(list)
    for (schema, name), t in sorted(tabs.items()):
        by_schema[schema].append(t)
    docs = [p for p in projections if p["name"].endswith(("Doc", "docs"))]
    pg = [p for p in projections if p not in docs]
    no_tenant = sorted(f"{t['schema']}.{t['name']}" for t in tabs.values() if "tenant_id" not in key_cols(t["key"]))
    L = [BEGIN, "", "### الملخص", "", "| الـschema | السياق المالك | الجداول |", "|---|---|---|"]
    L += [f"| `{s}` | {SCHEMA_BC.get(s, 'BC08 (مخزن مفاتيح لكل خلية)' if s == 'key_store' else '—')} | {len(v)} |" for s, v in sorted(by_schema.items())]
    L += [f"| إسقاطات PostgreSQL (اسم الـschema **[Missing]**) | BC07 | {len(pg)} |",
          f"| وثائق OpenSearch | BC07 | {len(docs)} |", "",
          f"**جداول مفتاحها بلا `tenant_id`** (مستوى المنصة أو الخلية، أو مؤقتة): {', '.join(f'`{x}`' for x in no_tenant) or 'لا شيء'}.", "",
          "**جداول لم تُدرج في الكتالوج:** " + "؛ ".join(f"`{n}` ({', '.join(sorted(s))})" for n, s in sorted(skipped.items())) +
          " — الجداول القياسية وجداول التاريخ (§3)، ومخزن `security_versions` (BC01، مصدر حقيقة الإلغاء لنقاط فرض السياسة).", ""]
    if drift:
        L += ["**اختلاف تسمية بين الشرائح للجدول نفسه** (لم يُدمج كأعمدة جديدة؛ يُحسم في المصدر) **[Needs Review]**:", "",
              "| الجدول | الاختلاف |", "|---|---|"] + [f"| `{a}` | {b} |" for a, b in drift] + [""]
    for schema, items in sorted(by_schema.items()):
        L += ["", f"### schema `{schema}` — {SCHEMA_BC.get(schema, 'BC08' if schema == 'key_store' else '—')}", ""]
        if schema == "key_store":
            L += ["مخزن المفاتيح لكل خلية لا لكل مستأجر (`slc-12a.md`: «key store per cell»؛ TD-07)؛ أُفرد هنا لأن الاسم في المصدر "
                  "`key_store.<table>` لا يقع في schema `governance` الخاص بالمستأجر.", ""]
        rels = infer_fks(items)
        L += ["```mermaid", "erDiagram"]
        for t in items:
            ent = re.sub(r"[^A-Za-z0-9_]", "_", t["name"])
            kcols = key_cols(t["key"])
            fks = {cn for (src, _, cn) in rels if src == t["name"]}
            L.append(f"  {ent} {{")
            for k in kcols:
                L.append(f"    {col_type(k)} {k} PK" + (", FK" if k in fks else ""))
            for fk in sorted(fks - set(kcols)):
                L.append(f"    urn {fk} FK")
            L.append("  }")
        for src, dst, cn in rels:
            L.append(f"  {re.sub(r'[^A-Za-z0-9_]', '_', dst)} ||--o{{ {re.sub(r'[^A-Za-z0-9_]', '_', src)} : \"{cn}\"")
        L += ["```", "", "العلاقات مستنتَجة وفق §5 **[Derived]**؛ الأنواع وفق §4 **[Derived]**.", ""]
        for t in items:
            L += [f"#### `{schema}.{t['name']}`" + (" — مؤقت (ephemeral)" if t["ephemeral"] else ""), "",
                  f"- **المفتاح:** `{t['key']}` · **المصدر:** `06-data/logical-model/{t['slice']}.md`" +
                  (f" · **التقسيم:** {esc(t['partition'])}" if t["partition"] else "") +
                  (" · **امتدادات:** " + "؛ ".join(esc(x) for x in t["ext"]) if t["ext"] else ""), "",
                  "| العمود | النوع (مستنتَج) | اختياري | ملاحظة |", "|---|---|---|---|"]
            for c in t["cols"]:
                note = []
                if "pii" in c.lower():
                    note.append("بيانات شخصية — مشفرة بمفتاح الموضوع (ADR-P08)")
                if "(enc)" in c:
                    note.append("مشفر")
                extra = re.search(r"\((.*)\)", c)
                if extra and "pii" not in extra.group(1) and extra.group(1) not in ("json", "enc", "array"):
                    note.append(esc(extra.group(1)))
                L.append(f"| `{clean_col(c)}` | {col_type(c)} | {'نعم' if '?' in c else '—'} | {'؛ '.join(note) or '—'} |")
            L += ["", f"**القيود:** {esc(t['constraints'])}", ""]
    L += ["", "### إسقاطات BC07 في PostgreSQL", "",
          "اسم الـschema غير محدد في `06-data/logical-model/slc-05.md` («BC07 store») **[Missing]**. جداول الرسم البياني بلا قاعدة رسم بياني "
          "(TD-03)؛ كل ما هنا قابل لإعادة البناء من المالكين (FIT-11).", "",
          "| الجدول | المفتاح | الحقول | ملاحظات |", "|---|---|---|---|"]
    L += [f"| {p['name']} | `{esc(p['key'])}` | {esc(p['cols'])} | {esc(p['notes'])} |" for p in pg]
    L += ["", "### وثائق OpenSearch (BC07)", "",
          "وثائق البحث والمتجهات في OpenSearch (TD-02، TD-19)، بفهارس مفصولة حسب إصدار الإسقاط؛ قابلة لإعادة البناء (FIT-11).", "",
          "| الوثيقة | المفتاح | الحقول | ملاحظات |", "|---|---|---|---|"]
    L += [f"| {p['name']} | `{esc(p['key'])}` | {esc(p['cols'])} | {esc(p['notes'])} |" for p in docs]
    L += ["", "### المخزن على الجهاز الميداني (مشفر)", "", "| المخزن | المحتوى |", "|---|---|"]
    L += [f"| {a} | {esc(b)} |" for a, b in client]
    L += ["", END]
    write_generated(OUT / "16-database-schema.md", None, "\n".join(L))
    return sum(len(v) for v in by_schema.values())


# ------------------------------------------------------------------ 02 actors and roles
ROLE_RULES = [  # (label, regex) — checked in order; qualifiers after "≠" are removed first
    ("ACT-01", r"\bexecutive\b"),
    ("ACT-02", r"(?<!resource )(?<!training )(?<!knowledge )(?<!risk )\bmanagers?\b|product owner"),
    ("ACT-03", r"\bplanner\b"),
    ("ACT-04", r"\banaly(st|sis lead)|analyst lead"),
    ("ACT-05", r"(?<!platform )(?<!carrier )\boperator\b|duty officer"),
    ("ACT-06", r"field (user|device)|device \+ user"),
    ("ACT-07", r"resource manager|technician"),
    ("ACT-08", r"logistics (user|officer)|dispatcher|carrier|receiving party"),
    ("ACT-09", r"risk manager|مدير المخاطر"),
    ("ACT-10", r"training manager|exercise (director|controller)|\bevaluator\b"),
    ("ACT-11", r"knowledge manager"),
    ("ACT-12", r"archivist"),
    ("ACT-13", r"security officer"),
    ("ACT-14", r"\bauditor\b"),
    ("ACT-15", r"administrator|mdm policy"),
    ("PLT-OPS", r"platform operator"),
    ("PLT-AI", r"ai platform engineer|ai governance"),
    ("PLT-INT", r"integration engineer"),
    ("AUTH-LEGAL", r"legal|compliance|privacy officer"),
    ("AUTH-GRANT", r"authority|approver|second (approver|lead)|\bholder\b"),
    ("REL-TASK", r"assignee|reviewer|attestation role"),
    ("REL-OWNER", r"\bowner\b|requester|custodian|(?<![a-z])self\b|participant|lead organization|^lead$|write permission|distributor"),
    ("REL-RECIPIENT", r"recipient|subscriber"),
    ("REL-INCIDENT", r"الحادثة|مُبلِّغ|القائد|مالك الاستمرارية"),
    ("REL-RISK", r"محدِّد الخطر|^مقيّم$|موافق المعالجة|مالك النطاق"),
    ("REL-PEER", r"\bsecond (analyst|administrator)|peer analyst"),
    ("ANY-USER", r"any (authorized )?user|authenticated user|^user$|user \(|مستخدم مخوَّل|any analyst|cleared for|authorized (on|by)|user of tenant|and above|^planner scope$|asset owner scope"),
    ("SYS", r"service account|workload identity|^system$|analysis-run identity|system identity|internal (peps|services)|owner contexts|adapter owner|scim"),
]
ROLE_LABELS = {
    "PLT-OPS": ("مشغّل المنصة", "Platform Operator — فرق المنصة (SH-05)"),
    "PLT-AI": ("مهندس/حوكمة الذكاء الاصطناعي", "AI platform engineer، AI governance authority"),
    "PLT-INT": ("مهندس التكامل", "integration engineer"),
    "AUTH-LEGAL": ("السلطة القانونية والامتثال", "Legal/Compliance authority، Privacy officer"),
    "AUTH-GRANT": ("صاحب سلطة أو معتمِد ثانٍ", "حامل منح سلطة في BC01 أو معتمِد ≠ المُعد (allocation/disposal/transfer/release authority، second approver…)"),
    "REL-TASK": ("المنفّذ والمراجع", "assignee، reviewer — دور يحدده المورد نفسه"),
    "REL-OWNER": ("المالك والطالب والمشارك", "owner، requester، custodian، participant، self"),
    "REL-RECIPIENT": ("المستلم والمشترك", "recipient، subscriber"),
    "REL-INCIDENT": ("أدوار الحادثة", "المُبلِّغ، مقيّم الحادثة، قائد الحادثة"),
    "REL-RISK": ("أدوار الخطر", "محدِّد الخطر، المقيّم، موافق المعالجة، مالك النطاق — أدوار منفصلة بفصل المهام (INV-RIS-01: المقيّم ≠ المحدِّد)"),
    "REL-PEER": ("الشخص الثاني", "second Analyst / Administrator، peer Analyst — لفصل المهام"),
    "ANY-USER": ("أي مستخدم مخوَّل", "أي مستخدم ضمن `allowed_scope` أو مصرَّح له بعلامة المورد"),
    "SYS": ("هويات النظام والخدمات", "adapter/SCIM service accounts، workload identities، analysis-run identity، internal PEPs"),
}
ROLE_GROUPS = [("A", "الفاعلون الأعمال (ACT-01..15 — `01-business/stakeholders.md`)", lambda k: k.startswith("ACT-")),
               ("B", "أدوار المنصة", lambda k: k.startswith("PLT-")),
               ("C", "أدوار السلطة والاعتماد", lambda k: k.startswith("AUTH-")),
               ("D", "أدوار العلاقة بالمورد (سمات للمورد يقيّمها قرار السياسة — ABAC عبر PIP، `08-security/authorization-model.md` §1–3)", lambda k: k.startswith(("REL-", "ANY-"))),
               ("E", "الفاعلون النظاميون", lambda k: k == "SYS")]


def classify_role(role):
    r = role.lower().strip()
    if re.search(dict(ROLE_RULES)["SYS"], r):
        return ["SYS"]
    r = re.sub(r"\s*≠.*$", "", re.sub(r"\((itself[^)]*)\)", "", r)).strip()
    labels = [lab for lab, rx in ROLE_RULES if lab not in ("ANY-USER", "SYS") and re.search(rx, r)]
    if "AUTH-GRANT" in labels and {"AUTH-LEGAL", "PLT-AI"} & set(labels):
        labels.remove("AUTH-GRANT")
    if not labels and re.search(dict(ROLE_RULES)["ANY-USER"], r):
        labels = ["ANY-USER"]
    return labels


def load_actors():
    text = (SPEC / "01-business" / "stakeholders.md").read_text(encoding="utf-8")
    d = yaml_block(text)
    return d


def build_actors(aggs, cmds, qrys, pol_c, pol_q):
    st = load_actors()
    acts = {a["id"]: a for a in st.get("actors", [])}
    groups = {g["id"]: g for g in st.get("stakeholder_groups", [])}
    uses = defaultdict(lambda: {"cmd": defaultdict(list), "qry": defaultdict(list), "types": defaultdict(int)})
    unmapped, seen_roles, unresolved = defaultdict(list), defaultdict(set), []
    for cid, c in sorted(cmds.items()):
        a = aggs[c["Aggregate"]]
        trs = [t for t in a["trans"] if t["cmd"] == cid]
        roles, narrowed = pick_actor(str(pol_c.get(cid, {}).get("subject") or c["الفاعل"]), cid, is_create(trs))
        if cid in ACTOR_RESOLUTION:
            roles, narrowed = ACTOR_RESOLUTION[cid][0], True
        if not narrowed:
            unresolved.append((cid, roles))
            continue
        typ = op_type(cid, a, c)
        labs = set()
        for role in roles.split(" · "):
            got = classify_role(role)
            labs |= set(got)
            seen_roles[role].add(" · ".join(got) or "—")
            if not got:
                unmapped[role].append(cid)
        for lab in labs:
            uses[lab]["cmd"][c["_bc"]].append(cid)
            uses[lab]["types"][typ] += 1
    for qid, q in sorted(qrys.items()):
        labs = set()
        for i, segment in enumerate(re.split(r"\s*[;؛]\s*", query_actor(q, pol_q.get(qid, {}), pol_q))):
            for role in re.split(r"\s*[,،]\s*|\s+or\s+", segment):
                role = re.sub(r"^or\s+", "", role.strip())
                got = classify_role(role) if role else []
                labs |= set(got)
                if role and (got or i == 0):
                    seen_roles[role].add(" · ".join(got) or "—")
                if not got and i == 0 and role:  # later segments are visibility qualifiers unless they name a role
                    unmapped[role].append(qid)
        for lab in labs:
            uses[lab]["qry"][q["_bc"]].append(qid)
            uses[lab]["types"]["جلب"] += 1

    def name(lab):
        if lab in acts:
            return f"{lab} {acts[lab]['name']} — {ACTORS_AR.get(lab, '')}"
        return f"{lab} — {ROLE_LABELS[lab][0]}"

    order = list(dict.fromkeys(lab for lab, _ in ROLE_RULES))
    bcs = sorted(BC_NAMES)
    types = ["إنشاء", "تعديل", "سير عمل", "حذف / إنهاء", "نظام", "جلب"]
    L = [BEGIN, "", "### 6.1 كتالوج الفاعلين والأدوار", "",
         f"العدّ على {len(cmds) - len(unresolved)} أمرًا حُسم فاعلها و{len(qrys)} استعلامًا؛ الأوامر الـ{len(unresolved)} التي لم يُحسم فاعلها في §6.6. "
         "العملية تُحسب مرة لكل دور تنسب إليه، فمجموع الأعمدة أكبر من عدد العمليات.", ""]
    for gid, gtitle, pred in ROLE_GROUPS:
        labs = [lab for lab in order if pred(lab)]
        L += [f"#### ({gid}) {gtitle}", "", "| الفاعل / الدور | الوصف | أوامر | استعلامات | السياقات |", "|---|---|---|---|---|"]
        for lab in labs:
            u = uses.get(lab)
            nc = sum(len(v) for v in u["cmd"].values()) if u else 0
            nq = sum(len(v) for v in u["qry"].values()) if u else 0
            ctx = sorted(set(u["cmd"]) | set(u["qry"])) if u else []
            desc = (f"{groups.get(acts[lab]['group'], {}).get('ar', '')} ({acts[lab]['group']})" if lab in acts
                    else ROLE_LABELS[lab][1])
            L.append(f"| {name(lab)} | {desc} | {nc} | {nq} | {', '.join(ctx) or '—'} |")
        L.append("")
    L += ["### 6.2 مصفوفة الفاعل × السياق (عدد الأوامر / الاستعلامات)", "",
          "| الفاعل / الدور | " + " | ".join(bcs) + " |", "|---|" + "---|" * len(bcs)]
    for lab in order:
        u = uses.get(lab)
        if u:
            L.append(f"| {name(lab)} | " + " | ".join(
                (f"{len(u['cmd'].get(bc, []))} / {len(u['qry'].get(bc, []))}" if u["cmd"].get(bc) or u["qry"].get(bc) else "—") for bc in bcs) + " |")
    L += ["", "### 6.3 مصفوفة الفاعل × نوع العملية", "",
          "| الفاعل / الدور | " + " | ".join(types) + " |", "|---|" + "---|" * len(types)]
    for lab in order:
        u = uses.get(lab)
        if u:
            L.append(f"| {name(lab)} | " + " | ".join(str(u["types"].get(t, 0) or "—") for t in types) + " |")
    L += ["", "### 6.4 عمليات كل فاعل", "",
          "لكل فاعل: الأوامر ثم الاستعلامات حسب السياق. القصة المقابلة لكل معرّف في `05-user-stories/us-bcNN.md`.", ""]
    for lab in order:
        u = uses.get(lab)
        if not u:
            continue
        L += [f"#### {name(lab)}", ""]
        for bc in bcs:
            cs, qs = u["cmd"].get(bc, []), u["qry"].get(bc, [])
            if cs or qs:
                L.append(f"- **{bc}:** " + ", ".join(f"`{x}`" for x in cs + qs))
        L.append("")
    L += ["### 6.5 كل أوصاف الأدوار في السياسات وتصنيفها", "",
          "يكشف هذا الجدول كل مكافأة يفترضها التصنيف (مثل dispatcher ← مستخدم الإمداد، Exercise Controller ← مدير التدريب) **[Derived]**. "
          "الوصف غير المصنَّف يظهر بـ«—».", "", "| الوصف في المصدر | التصنيف |", "|---|---|"]
    L += [f"| {esc(r)} | {', '.join(sorted(v))} |" for r, v in sorted(seen_roles.items(), key=lambda x: x[0].lower())]
    L += ["", "### 6.6 أوامر لم يُحسم فاعلها", "",
          "موضوع السياسة يسرد أدوارًا بأفعالها ولا يشمل أيٌّ منها فعل الأمر؛ لا تُنسب هنا لأي دور، وقصصها معلَّمة **[Needs Review]** "
          "(تُحسم في `17-security-design.md`، المرحلة 4).", "", "| الأمر | الأدوار المذكورة في السياسة |", "|---|---|"]
    L += [f"| `{c}` | {esc(r)} |" for c, r in unresolved] if unresolved else \
        ["| — | لا شيء: الأوامر الـ26 التي لم يحسمها المصدر محسومة في `17-security-design.md` §5 (CR-77) |"]
    L += ["", "### 6.7 أوصاف لم تُصنَّف", "",
          ("| الوصف في المصدر | العمليات |\n|---|---|\n" + "\n".join(f"| {esc(r)} | {', '.join(v)} |" for r, v in sorted(unmapped.items())))
          if unmapped else "لا شيء.", "", END]
    write_generated(OUT / "02-actors-roles.md", None, "\n".join(L))
    return uses


# ------------------------------------------------------------------ 03 requirements analysis
def load_capabilities():
    text = (SPEC / "01-business" / "capabilities.md").read_text(encoding="utf-8").split("<details>")[0]
    caps = {}
    for block in re.split(r"\n(?=### CAP-)", text):
        m = re.match(r"### (CAP-\d+) — (.*)", block)
        if m:
            caps[m.group(1)] = {"name": m.group(2).strip(),
                                "outcomes": re.findall(r"OUT-\d+", (re.search(r"\*\*outcomes:\*\*(.*)", block) or [""])[0] if re.search(r"\*\*outcomes:\*\*(.*)", block) else ""),
                                "subs": re.findall(r"\{id: (CAP-\d+\.\d+), name: ([^,}]+), release: ([^}]+)\}", block)}
    return caps


def load_outcomes():
    text = (SPEC / "01-business" / "outcomes.md").read_text(encoding="utf-8").split("<details>")[0]
    outs = {}
    for block in re.split(r"\n(?=### OUT-)", text):
        m = re.match(r"### (OUT-\d+)", block)
        if m:
            f = dict(re.findall(r"^- \*\*([a-z_0-9]+):\*\* (.*)$", block, re.M))
            outs[m.group(1)] = f
    return outs


def short(text, n=160):
    text = re.sub(r"\s+", " ", text or "").strip()
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def build_requirements(aggs, reqs, ucs, qrys):
    caps, outs = load_capabilities(), load_outcomes()
    qas = md_records((SPEC / "02-requirements" / "quality-scenarios.md").read_text(encoding="utf-8"), "QAS")
    matrix = {}
    for header, rows in tables((SPEC / "15-traceability" / "quality-verification-matrix.md").read_text(encoding="utf-8")):
        if header and header[0] == "qas":
            matrix.update({r[0]: dict(zip(header, r)) for r in rows})
    req_aggs = defaultdict(list)
    for aid, a in aggs.items():
        for r in a["reqs"]:
            req_aggs[r].append(aid)
    req_ucs = {rid: re.findall(r"UC-\d+", r.get("use_cases", "")) for rid, r in reqs.items()}
    by_cap = defaultdict(list)
    for rid, r in sorted(reqs.items()):
        by_cap[(r.get("capability") or "—")[:6]].append(rid)
    count = lambda ids, key, val: sum(1 for i in ids if reqs[i].get(key) == val)  # noqa: E731
    L = [BEGIN, "", "### 3.1 المتطلبات الوظيفية حسب القدرة", "",
         "| القدرة | الاسم | المتطلبات | R1 | R2 | R3 | must | should | بلا Aggregate | بلا حالة استخدام |", "|---|---|---|---|---|---|---|---|---|---|"]
    for cap in sorted(by_cap):
        ids = by_cap[cap]
        L.append(f"| {cap} | {caps.get(cap, {}).get('name', '—')} | {len(ids)} | {count(ids, 'release', 'R1')} | {count(ids, 'release', 'R2')} | "
                 f"{count(ids, 'release', 'R3')} | {count(ids, 'priority', 'must')} | {count(ids, 'priority', 'should')} | "
                 f"{sum(1 for i in ids if not req_aggs.get(i))} | {sum(1 for i in ids if not req_ucs.get(i))} |")
    allids = list(reqs)
    L.append(f"| **المجموع** | | **{len(allids)}** | {count(allids, 'release', 'R1')} | {count(allids, 'release', 'R2')} | "
             f"{count(allids, 'release', 'R3')} | {count(allids, 'priority', 'must')} | {count(allids, 'priority', 'should')} | "
             f"{sum(1 for i in allids if not req_aggs.get(i))} | {sum(1 for i in allids if not req_ucs.get(i))} |")
    pat = defaultdict(int)
    for r in reqs.values():
        pat[r.get("pattern", "—")] += 1
    L += ["", "**أنماط الصياغة (EARS):** " + "، ".join(f"{k}: {v}" for k, v in sorted(pat.items(), key=lambda x: -x[1])) +
          f". **طريقة التحقق:** " + "، ".join(f"{k}: {v}" for k, v in sorted(defaultdict(int, {m: sum(1 for r in reqs.values() if r.get('verification_method') == m) for m in {r.get('verification_method') for r in reqs.values()}}).items())) + ".", ""]
    L += ["### 3.2 من النتائج إلى القدرات إلى المتطلبات", "",
          "حقل `contributing_requirements` في النتائج ما زال TBD (CR-30)، فالربط هنا مشتق عبر حقل `outcomes` في كل قدرة **[Derived]**. "
          "القدرة الواحدة قد تخدم أكثر من نتيجة، فالأعداد متداخلة ولا يساوي مجموعها 210؛ وقدرات بلا نتيجة: " +
          (", ".join(f"{c} ({len(by_cap.get(c, []))} متطلبًا)" for c, v in sorted(caps.items()) if not v["outcomes"]) or "لا شيء") + ".", "",
          "| النتيجة | الاسم | أولوية السنة الأولى | القدرات | المتطلبات عبرها |", "|---|---|---|---|---|"]
    for oid, o in sorted(outs.items()):
        cs = sorted(c for c, v in caps.items() if oid in v["outcomes"])
        L.append(f"| {oid} | {o.get('ar', '')} ({o.get('en', '')}) | {o.get('priority_year1', '—')} | {', '.join(cs) or '—'} | {sum(len(by_cap.get(c, [])) for c in cs)} |")
    L += ["", "### 3.3 المتطلبات حسب القدرة", ""]
    for cap in sorted(by_cap):
        c = caps.get(cap, {})
        L += [f"#### {cap} — {c.get('name', '—')}", "",
              "القدرات الفرعية: " + ("، ".join(f"{i} {n.strip()} ({rel.strip()})" for i, n, rel in c.get("subs", [])) or "—"), "",
              "| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |", "|---|---|---|---|---|---|---|---|"]
        for rid in by_cap[cap]:
            r = reqs[rid]
            L.append(f"| {rid} | {esc(short(r.get('statement', '')))} | {r.get('pattern', '—')} | {r.get('priority', '—')} | {r.get('release', '—')} | "
                     f"{', '.join(req_ucs.get(rid, [])) or '**—**'} | {', '.join(req_aggs.get(rid, [])) or '— (§3.4)'} | {r.get('quality', '—')} |")
        L.append("")
    no_agg = sorted(i for i in allids if not req_aggs.get(i))
    fit_text = (SPEC / "13-verification" / "fitness-functions.md").read_text(encoding="utf-8")
    fits = {m.group(1): m.group(2) for m in re.finditer(r"^\| (FIT-\d+) \|[^|]*\| ([^|]*) \|", fit_text, re.M)}
    trace = defaultdict(set)
    for f in sorted((SPEC / "15-traceability").glob("trace-*.md")):
        for header, rows in tables(f.read_text(encoding="utf-8")):
            if header[:2] == ["requirement", "design_elements"]:
                for r in rows:
                    trace[r[0]] |= {x.strip() for x in split_top(r[1]) if x.strip() and x.strip() != "—"}
        for rid, design in re.findall(r"^- \*\*requirement:\*\* (REQ-[A-Z]+-\d+)\n- \*\*design:\*\* (.*)$", f.read_text(encoding="utf-8"), re.M):
            trace[rid].add(design.strip())
    L += ["### 3.4 فجوات التغطية", "",
          f"**متطلبات لا يحققها أي Aggregate ({len(no_agg)}).** أغلبها قيود منصة أو أمن أو مكتبات مشتركة تتحقق بالبنية لا بـAggregate. "
          "العمود الأخير يسرد عناصر التصميم التي تحققها من ملفات التتبع `15-traceability/trace-*.md` (العمود `design_elements`)، "
          "والاستعلامات التي تذكرها، ودوال اللياقة التي تستند إليها؛ المتطلب بلا أي منها فجوة **[Needs Review]**.", "",
          "| المتطلب | النمط | الإصدار | النص | يتحقق عبر |", "|---|---|---|---|---|"]
    for i in no_agg:
        refs = sorted(trace.get(i, set()) | {q for q, v in qrys.items() if re.search(rf"\b{i}\b", v.get("المتطلب", ""))} |
                      {k for k, v in fits.items() if re.search(rf"\b{i}\b", v)})
        refs = [x for x in refs if not any(y != x and x.startswith(y.split(" ")[0]) and len(y) > len(x) for y in refs)]
        L.append(f"| {i} | {reqs[i].get('pattern', '—')} | {reqs[i].get('release', '—')} | {esc(short(reqs[i].get('statement', ''), 110))} | "
                 f"{esc(', '.join(refs)) or '**[Needs Review]**'} |")
    diff = []
    for rid in sorted(reqs):
        named = {m for x in trace.get(rid, set()) for m in re.findall(r"AGG-[A-Z0-9-]+[A-Z0-9]", x)} & set(aggs)
        own = set(req_aggs.get(rid, []))
        if named and named != own:
            diff.append((rid, own, named))
    L += ["", f"**تعارض بين تتبع المتطلب في الـAggregates (`traces.satisfies`) وفي ملفات التتبع ({len(diff)})** **[Needs Review]** — "
          "مسجل في `00-index.md` §6:", "", "| المتطلب | الـAggregates (satisfies) | الـAggregates (trace-*.md) |", "|---|---|---|"]
    L += [f"| {r} | {', '.join(sorted(o)) or '—'} | {', '.join(sorted(n))} |" for r, o, n in diff]
    L += ["", f"**متطلبات بلا حالة استخدام ({sum(1 for i in allids if not req_ucs.get(i))}):** مسرودة بعلامة **—** في §3.3؛ أغلبها في CAP-14 (تشغيل المنصة) وCAP-03.", ""]
    qual = defaultdict(list)
    for qid, q in sorted(qas.items()):
        qual[q.get("quality", "—")].append(qid)
    L += ["### 3.5 سيناريوهات الجودة", "",
          f"{len(qas)} سيناريو في `02-requirements/quality-scenarios.md`؛ مصفوفة التحقق `15-traceability/quality-verification-matrix.md` تغطي {len(set(qas) & set(matrix))} منها. "
          f"غير المغطاة: {', '.join(sorted(set(qas) - set(matrix))) or 'لا شيء'} **[Missing]**.", "",
          "| الخاصية | العدد | السيناريوهات |", "|---|---|---|"]
    L += [f"| {k} | {len(v)} | {', '.join(v)} |" for k, v in sorted(qual.items(), key=lambda x: (-len(x[1]), x[0]))]
    L += ["", "#### محركات المعمارية (الأولوية H/H)", "", "| السيناريو | الخاصية | المحفِّز | المقياس | التحقق |", "|---|---|---|---|---|"]
    for qid, q in sorted(qas.items()):
        if q.get("priority") == "H/H":
            L.append(f"| {qid} | {q.get('quality')} | {esc(short(q.get('stimulus', ''), 90))} | {esc(q.get('response_measure', ''))} | "
                     f"{esc(matrix.get(qid, {}).get('verification', '**[Missing]**'))} |")
    L += ["", "#### الكتالوج الكامل", "", "| السيناريو | الخاصية | الأولوية | المحفِّز | المقياس | الحمل | التحقق | متى |", "|---|---|---|---|---|---|---|---|"]
    for qid, q in sorted(qas.items()):
        m = matrix.get(qid, {})
        L.append(f"| {qid} | {q.get('quality')} | {q.get('priority', '—')} | {esc(short(q.get('stimulus', ''), 90))} | {esc(q.get('response_measure', ''))} | "
                 f"{q.get('workload', '—')} | {esc(m.get('verification', '**[Missing]**'))} | {esc(m.get('when', '—'))} |")
    L += ["", END]
    write_generated(OUT / "03-requirements-analysis.md", None, "\n".join(L))


# ------------------------------------------------------------------ 04 use cases
NEGATIVE = {"CANCEL", "REJECT", "WITHDRAW", "DISCARD", "ABORT", "FAIL", "DECLINE", "SUSPEND", "BLOCK", "RETURN", "REVOKE",
            "EXPIRE", "LOCK", "DISABLE", "PARK", "DEPRECATE", "RECLASSIFY", "REOPEN", "DISPOSE", "ERASE", "PAUSE",
            "RETRACT", "QUARANTINE", "LOST", "DE", "ANNUL", "PREEMPT", "DEACTIVATE", "UNSUBSCRIBE", "REQUEST", "SPLIT",
            "DENY", "DEGRADE"}
NEG_STATE = re.compile(r"CANCEL|REJECT|SUPERSED|EXPIR|WITHDRAW|ABORT|FAIL|ANNUL|REVOK|PREEMPT|REFUS|DENI|LOST|WIPED|ERAS|"
                       r"DESTROY|SPLIT|DISCARD|DECLIN|RETIRE|REMOVED|INACTIVE|DEPRECAT|DISPOS|UNSERVICEABLE|DAMAGED|"
                       r"QUARANTIN|SUSPEND|LOCKED|DISABLED|BLOCKED|RETURNED|DEGRADED|MIGRATING|DECOMMISSION|ESCALATED|"
                       r"UNLINK|PARKED|DISPUTED|OBSOLETE|INSUFFICIENT|NOT_A_MATCH|NOT_MATCH|UNRESOLVED|FAILED")
ENDING = {"RETIRE", "UNLINK", "END", "CORRECT", "RECORD-CHANGE", "SUPERSEDE"}
READ_UC = re.compile(r"^(Check|View|Search|Browse|Query|Retrieve|Discover|Explore|Monitor|Track|Inspect|Verify|See)\b", re.I)


def _ending(t, a):
    return verb_of(t["cmd"]) in ENDING or closes_and_replaces([t], a)


def _positive(t, a):
    if t["to"] in UNCHANGED or NEG_STATE.search(t["to"]):
        return False
    if t["cmd"].startswith("SYS:"):
        return not re.search(r"expir|timeout|fail|reject|cancel|lost|denied|supersed|revok|insufficient|no sufficient", t["cmd"] + t["guard"], re.I)
    words = verb_of(t["cmd"]).split("-")
    return words[0] not in NEGATIVE and not {"NOT", "LOST", "DAMAGE"} & set(words) and not _ending(t, a)


def happy_path(a, verbs=None):
    """Shortest chain of positive transitions from creation to a positive terminal state, else to the deepest
    reachable state. With verbs (from the use case's own scope), only those commands are followed."""
    trs = [t for t in a["trans"] if _positive(t, a) and
           (verbs is None or t["cmd"].startswith("SYS:") or verb_of(t["cmd"]).lower().replace("-", " ") in verbs)]
    starts = [t for t in trs if t["from"] == ["∅"]]
    if verbs is not None and not starts:
        return [t for t in trs if not t["cmd"].startswith("SYS:")]
    if not starts:
        return []
    best, frontier, seen = None, [[starts[0]]], {starts[0]["to"]}
    deepest = [starts[0]]
    while frontier:
        nxt = []
        for path in frontier:
            state = path[-1]["to"]
            if state in a["final"]:
                best = best or path
                continue
            for t in trs:
                if t["from"] != ["∅"] and state in expand_from(t["from"], a) and t["to"] not in seen:
                    seen.add(t["to"])
                    nxt.append(path + [t])
                    deepest = path + [t] if len(path) + 1 > len(deepest) else deepest
        if best:
            break
        frontier = nxt
    return best or deepest


def uc_label(lab, acts):
    return f"{acts[lab]['name']}" if lab in acts else ROLE_LABELS[lab][0]


def scope_verbs(pre):
    """'(AGG-X.md — register, evaluate, approve …; AGG-Y.md — …)' in the catalog → {AGG-X: {verbs}}."""
    out = {}
    for aid, verbs in re.findall(r"(AGG-[A-Z0-9-]+)\.md — ([^;)]+)", pre or ""):
        out[aid] = {re.sub(r"^cmd-[a-z]+-", "", v.strip().lower()).replace("-", " ") for v in
                    re.split(r"[,/]| and ", re.sub(r"\b(a|an|the)\b.*$", "", verbs)) if v.strip()}
    return out


def build_use_cases(aggs, cmds, qrys, pol_c, reqs, ucs):
    acts = {a["id"]: a for a in load_actors().get("actors", [])}
    req_aggs = defaultdict(list)
    for aid, a in aggs.items():
        for r in a["reqs"]:
            req_aggs[r].append(aid)
    cmd_roles = {}
    for cid, c in cmds.items():
        trs = [t for t in aggs[c["Aggregate"]]["trans"] if t["cmd"] == cid]
        roles, narrowed = pick_actor(str(pol_c.get(cid, {}).get("subject") or c["الفاعل"]), cid, is_create(trs))
        if cid in ACTOR_RESOLUTION:
            roles, narrowed = ACTOR_RESOLUTION[cid][0], True
        cmd_roles[cid] = (roles, {lab for r in roles.split(" · ") for lab in classify_role(r)} if narrowed else set())
    by_bc, info = defaultdict(list), {}
    for uid, u in sorted(ucs.items(), key=lambda x: int(x[0][3:])):
        rids = re.findall(r"REQ-[A-Z]+-\d+", u.get("requirements", ""))
        ag = sorted({x for r in rids for x in req_aggs.get(r, [])})
        scope = scope_verbs(u.get("preconditions", ""))
        words = {w.lower()[:5] for w in re.findall(r"[A-Za-z]{4,}", u.get("title", "")) if w.lower() not in ("manage", "management")}
        primary = [x for x in scope if x in aggs] or \
                  [x for x in ag if words & {w.lower()[:5] for w in re.findall(r"[A-Za-z]{4,}", aggs[x]["title"])}] or ag
        reads = sorted(q for q, v in qrys.items() if set(re.findall(r"REQ-[A-Z]+-\d+", v.get("المتطلب", ""))) & set(rids))
        is_read = bool(READ_UC.search(u.get("title", ""))) and bool(reads)
        bcs = defaultdict(int)
        for x in (primary if not is_read else []):
            bcs[aggs[x]["bc"]] += 1
        for q in (reads if is_read else []):
            bcs[qrys[q]["_bc"]] += 1
        bc = max(sorted(bcs), key=lambda k: bcs[k]) if bcs else "—"
        labs = set()
        for x in ([] if is_read else primary):
            for cid in cmds:
                if cmds[cid]["Aggregate"] == x and (x not in scope or verb_of(cid).lower().replace("-", " ") in scope[x]):
                    labs |= cmd_roles[cid][1]
        src_labs = set()
        if u.get("actors", "TBD") not in ("TBD", ""):
            for role in re.split(r"\s+[·|]\s+|\s*[,;،]\s*|\s+/\s+", re.sub(r"\([^)]*\)", "", u["actors"])):
                src_labs |= set(classify_role(role)) if role.strip() else set()
        info[uid] = dict(rids=rids, ag=ag, bc=bc, labs=labs, src=src_labs, primary=primary, scope=scope, reads=reads, is_read=is_read)
        by_bc[bc].append(uid)
    L = [BEGIN, "", "### 2.1 الملخص", "", "| السياق | حالات الاستخدام | R1 | R2 | R3 | فاعلوها في المصدر | مشتقة الفاعلين |", "|---|---|---|---|---|---|---|"]
    for bc in sorted(by_bc):
        ids = by_bc[bc]
        L.append(f"| {bc} | {len(ids)} | " + " | ".join(str(sum(1 for i in ids if ucs[i].get("release") == r)) for r in ("R1", "R2", "R3")) +
                 f" | {sum(1 for i in ids if ucs[i].get('actors', 'TBD') != 'TBD')} | {sum(1 for i in ids if ucs[i].get('actors', 'TBD') == 'TBD')} |")
    L += ["", "### 2.2 مخططات حالات الاستخدام", "",
          "لكل سياق: الفاعلون (يسارًا) وحالات الاستخدام التي يشاركون فيها. الفاعلون من المصدر إن ذكرهم، وإلا من أدوار أوامر الـAggregates الرئيسية "
          "للحالة **[Derived]**. الأدوار العامة (أي مستخدم، هويات النظام) محذوفة من المخططات لتبقى مقروءة، ومذكورة في جدول كل حالة.", ""]
    skip = {"ANY-USER", "SYS"}
    edges = {u: ((i["src"] or i["labs"]) - skip) for u, i in info.items()}
    for bc in sorted(by_bc):
        if bc == "—":
            continue
        L += [f"#### {bc} — {BC_NAMES[bc]}", "", "```mermaid", "flowchart LR"]
        used = sorted({lab for u in by_bc[bc] for lab in edges[u]}, key=lambda k: (not k.startswith("ACT"), k))
        for lab in used:
            L.append(f'  {lab.replace("-", "_")}["{uc_label(lab, acts)}"]')
        L.append(f'  subgraph {bc}["{bc} {BC_NAMES[bc].split(" — ")[0]}"]')
        for u in by_bc[bc]:
            title = re.sub(r"[\"()\[\]{}<>:;|#]", " ", ucs[u].get("title", ""))
            L.append(f'    {u.replace("-", "")}(["{u} {title}"])')
        L.append("  end")
        for u in by_bc[bc]:
            for lab in sorted(edges[u]):
                L.append(f"  {lab.replace('-', '_')} --- {u.replace('-', '')}")
        L += ["```", ""]
    L += ["### 2.3 مواصفة كل حالة استخدام", ""]
    for bc in sorted(by_bc):
        L += [f"#### {bc} — {BC_NAMES.get(bc, 'بلا Aggregate مرتبط')}", ""]
        for uid in by_bc[bc]:
            u, i = ucs[uid], info[uid]
            cap = u.get("capability") or ", ".join(sorted({(reqs[r].get("capability") or "")[:6] for r in i["rids"] if r in reqs} - {""})) + " **[Derived]**"
            src_actors = u.get("actors", "TBD")
            L += [f"##### {uid} — {u.get('title', '')}", "",
                  "| تيار القيمة | القدرة | الإصدار | الحالة | المتطلبات |", "|---|---|---|---|---|",
                  f"| {u.get('value_stream', '—')} | {cap} | {u.get('release', '—')} | {u.get('status', '—')} | {', '.join(i['rids']) or '—'} |", ""]
            derived = ", ".join(uc_label(x, acts) for x in sorted(i["labs"]))
            if src_actors not in ("TBD", ""):
                line = "- **الفاعلون:** " + esc(src_actors) + " (المصدر)"
                extra = (i["src"] - i["labs"]) - skip
                if i["labs"] and extra and not i["is_read"]:
                    line += (f" — **[Needs Review]**: سياسات أوامرها لا تمنح {', '.join(uc_label(x, acts) for x in sorted(extra))}؛ "
                             f"تمنح: {derived}")
                L.append(line)
            else:
                L.append("- **الفاعلون:** " + (derived or ("حسب سياسة كل استعلام" if i["is_read"] else "**[Missing]**")) + " **[Derived]**")
            L.append("- **الـAggregates:** " + (", ".join(f"`{x}`" for x in i["primary"]) or "**[Missing]** — لا Aggregate يحقق متطلباتها") +
                     ("؛ مشاركة عبر المتطلبات نفسها: " + ", ".join(f"`{x}`" for x in i["ag"] if x not in i["primary"]) if set(i["ag"]) - set(i["primary"]) else ""))
            if i["scope"]:
                L.append("- **النطاق في المصدر:** " + "؛ ".join(f"`{x}`: {', '.join(sorted(v))}" for x, v in i["scope"].items()))
            pre = u.get("preconditions", "TBD")
            L.append("- **الشروط المسبقة:** " + (esc(pre) if pre not in ("TBD", "") and not re.match(r"^(SLC-|W\d)", pre) else
                                                 "المستخدم مصادَق عليه داخل المستأجر، وقرار السياسة يسمح بكل خطوة (ADR-P17) **[Derived]**"))
            flow = u.get("main_flow", "TBD")
            if flow not in ("TBD", "") and not re.match(r"^(SLC-|W\d)", flow):
                L.append(f"- **المسار الرئيسي (المصدر):** {esc(flow)}")
            if i["is_read"]:
                L.append("- **المسار الرئيسي** **[Derived]**: الفاعل يستدعي " + "، ".join(f"`{q}` ({esc(short(qrys[q].get('يعيد', ''), 60))})" for q in i["reads"]) +
                         "؛ النتيجة مقيدة بـ`allowed_scope` ومعاد فحصها (C-READ).")
            else:
                alts = []
                L.append("- **المسار الرئيسي** **[Derived]** — مسار لكل Aggregate رئيسي؛ ترتيب الـAggregates وتداخلها في `06-process-models.md`:")
                for x in i["primary"]:
                    a = aggs[x]
                    path = happy_path(a, i["scope"].get(x))
                    if not path:
                        continue
                    L.append(f"  - **{x}:**")
                    for n, t in enumerate(path, 1):
                        who = "النظام" if t["cmd"].startswith("SYS:") else cmd_roles.get(t["cmd"], ("?",))[0]
                        what = f"«{esc(t['cmd'][4:])}»" if t["cmd"].startswith("SYS:") else f"`{t['cmd']}`"
                        frm = show_from(t["from"]) if len(t["from"]) <= 3 or t["from"] == ["*NT"] else f"{len(t['from'])} حالات"
                        L.append(f"    {n}. {esc(who)}: {what} ({frm} → {t['to']}) ⇐ `{t['event']}`")
                    alts += [f"`{t['cmd']}` → {t['to']}" for t in a["trans"] if not t["cmd"].startswith("SYS:") and t not in path
                             and t["to"] not in UNCHANGED and not _positive(t, a)
                             and (x not in i["scope"] or verb_of(t["cmd"]).lower().replace("-", " ") in i["scope"][x])]
                if alts:
                    L.append("- **مسارات بديلة (إلغاء، رفض، إرجاع، إنهاء…):** " + "، ".join(dict.fromkeys(alts)))
            L.append("- **الاستثناءات:** رموز الرفض لكل خطوة في قصة أمرها (`05-user-stories/`، Scenario Outline «is rejected»).")
            L.append("")
    no_ag = [u for u in ucs if not info[u]["ag"] and not info[u]["is_read"]]
    covered = {x for u in info.values() for x in u["ag"]}
    L += ["### 2.4 فجوات التغطية", "",
          f"- **حالات استخدام بلا Aggregate ولا استعلام ({len(no_ag)}):** " + (", ".join(sorted(no_ag, key=lambda x: int(x[3:]))) or "لا شيء"),
          f"- **Aggregates لا تظهر في أي حالة استخدام ({len(set(aggs) - covered)}):** " + (", ".join(sorted(set(aggs) - covered)) or "لا شيء"), "", END]
    write_generated(OUT / "04-use-cases.md", None, "\n".join(L))


# ------------------------------------------------------------------ 07 domain model
def agg_slug(aid):
    return aid[4:].lower().replace("-", "_")


MAIN_TABLE_ALIAS = {"AGG-ASSESSMENT": "assessment_versions"}


def main_table(aid, tabs, schemas):
    s = agg_slug(aid)
    names = (MAIN_TABLE_ALIAS[aid],) if aid in MAIN_TABLE_ALIAS else (s + "s", s + "es", s[:-1] + "ies", s)
    for (schema, name), t in tabs.items():
        if schema in schemas and name in names:
            return t
    return None


GENERIC_WORDS = {"object", "item", "record", "type", "version", "request", "case", "source", "target", "subject", "order",
                 "rule", "set", "run", "result", "package", "session", "assignment", "link"}


def ref_target(col, aggs, own, siblings=(), own_key=(), urn_fields=()):
    """Aggregate referenced by a column: <slug>_ref|_id|_urn exactly; a bare <slug> only when the payload types it as a URN;
    else a unique aggregate of the same context whose slug ends with the column's last word (or, across contexts, a unique
    non-generic last word). Skips tenant_id, the aggregate's own key, endpoint pairs and polymorphic refs."""
    if col == "tenant_id" or col in own_key:
        return None
    m = re.match(r"^(?:parent_)?(\w+?)(?:_(ref|id|urn|refs|ids|urns))?$", col)
    if not m or (not m.group(2) and col not in urn_fields):
        return None
    base = m.group(1)
    if base in ("source", "target", "subject", "object", "from", "to") and ({"target_ref", "target_urn", "source"} & set(siblings)):
        return None
    exact = "AGG-" + base.upper().replace("_", "-")
    if exact in aggs:
        return exact if exact != own else None
    last = base.split("_")[-1]
    if len(last) <= 3:
        return None
    cands = [a for a in aggs if a != own and agg_slug(a).split("_")[-1] == last]
    same = [a for a in cands if aggs[a]["bc"] == aggs[own]["bc"]]
    if len(same) == 1:
        return same[0]
    return cands[0] if len(cands) == 1 and last not in GENERIC_WORDS and "_" not in base else None


APPROVED_EDGES = {("BC02", "BC03"), ("BC02", "BC04"), ("BC02", "BC06"), ("BC02", "BC07"), ("BC03", "BC04"), ("BC05", "BC04"),
                  ("BC04", "BC05"), ("BC03", "BC06"), ("BC04", "BC06")}  # upstream → downstream, 03-domain/context-map.md


def build_domain_model(aggs, cmds):
    tabs = load_ldm()[0]
    doms = {}
    for header, rows in tables((SPEC / "03-domain" / "domains.md").read_text(encoding="utf-8")):
        if header and header[0] == "id":
            for r in rows:
                if r[0].startswith("DOM-"):
                    doms[r[0]] = dict(zip(header, r))
    bc_schemas = defaultdict(set)
    for s_, bc in SCHEMA_BC.items():
        bc_schemas[bc].add(s_)
    comps = {}
    for aid, a in aggs.items():
        text = (SPEC / a["path"]).read_text(encoding="utf-8")
        sec = re.search(r"^## مكونات داخلية\n(.*?)(?=^## )", text, re.S | re.M)
        comps[aid] = [n for l in (sec.group(1).splitlines() if sec else []) if re.match(r"-\s*[A-Za-z]", l)
                      for n in re.findall(r"\b([A-Z][A-Za-z0-9]+)\b", re.sub(r"\(.*", "", l))]
    refs = defaultdict(set)  # (from, to) -> columns
    attrs = {}
    proj = {p["name"]: p for p in load_ldm()[1]}
    for aid, a in aggs.items():
        t = main_table(aid, tabs, bc_schemas[a["bc"]])
        if not t and aid == "AGG-PROJECTION-VERSION" and "projection_versions" in proj:
            p_ = proj["projection_versions"]
            t = {"schema": "(مخزن الإسقاطات)", "name": "projection_versions", "key": p_["key"], "cols": split_top(p_["cols"])}
        cols = []
        if t:
            raw = {clean_col(c): c for c in t["cols"]}
            cols = list(raw)
            attrs[aid] = (t, [(c, c) for c in key_cols(t["key"]) if c != "tenant_id"] +
                          [(c, raw[c]) for c in cols if c not in key_cols(t["key"])])
        fields = [n for c in cmds.values() if c["Aggregate"] == aid for n, _, _ in payload_fields(c.get("الحمولة (! إلزامي)", ""))]
        names = list(dict.fromkeys((key_cols(t["key"]) if t else []) + cols + fields))
        own_key = [c for c in key_cols(t["key"]) if c.endswith("_id") and c != "tenant_id"][-1:] if t else []
        urn_fields = {n for c in cmds.values() if c["Aggregate"] == aid
                      for n, _, ty in payload_fields(c.get("الحمولة (! إلزامي)", "")) if ty.startswith("urn")}
        for col in names:
            tgt = ref_target(col, aggs, aid, names, own_key, urn_fields)
            if tgt:
                refs[(aid, tgt)].add(col)
    L = [BEGIN, "", "### 3.1 المجالات والسياقات", "", "| السياق | المجالات (DOM) | عناصرها في `03-domain/domains.md` | الـAggregates |", "|---|---|---|---|"]
    for bc in sorted(BC_NAMES):
        ds = [d for d in doms.values() if d.get("bounded_context") == bc]
        L.append(f"| {bc} {BC_NAMES[bc]} | " + "<br>".join(f"{d['id']} {d['name']}" for d in ds) + " | " +
                 "<br>".join(esc(d.get("elements", "")) for d in ds) + " | " +
                 ", ".join(x[4:] for x in sorted(aggs) if aggs[x]["bc"] == bc) + " |")
    mism = []
    for d in doms.values():
        for el in [e.strip() for e in d.get("elements", "").split(",") if len(e.strip()) >= 5]:
            hits = [x for x in aggs if aggs[x]["title"].lower() in (el.lower(), el.lower() + "s") or
                    (len(el) >= 8 and len(aggs[x]["title"].split()) == 2 and aggs[x]["title"].split()[0].lower() == el.lower())]
            for x in hits:
                if aggs[x]["bc"] != d.get("bounded_context"):
                    mism.append(f"{d['id']} ({d.get('bounded_context')}) يذكر «{el}» بينما `{x}` في {aggs[x]['bc']}")
    if mism:
        L += ["", "**تعارض بين عناصر المجالات وملكية الـAggregates** **[Needs Review]** — عنصر مذكور في مجال سياق ويملكه Aggregate في سياق آخر:", ""]
        L += [f"- {m}" for m in sorted(set(mism))]
    cross = defaultdict(list)
    for (f, t), cs in refs.items():
        if aggs[f]["bc"] != aggs[t]["bc"]:
            cross[(aggs[f]["bc"], aggs[t]["bc"])].append(f"{f[4:]} → {t[4:]} ({', '.join(sorted(cs))})")
    L += ["", "### 3.2 المراجع بين السياقات (مشتقة من البيانات)", "",
          "كل عمود مفتاح أو عمود أو حقل حمولة يشير اسمه إلى Aggregate في سياق آخر **[Derived]** (القاعدة في `ref_target` بالمولِّد). "
          "المرجع URN يُتحقق منه عبر عقد السياق المالك، لا قيد قاعدة بيانات (FIT-01). العمود الأخير يقارن اتجاه الاعتماد بخريطة السياقات المعتمدة (§2): "
          "السياق الذي يحمل المرجع يعتمد على السياق المشار إليه، فيجب أن يكون الثاني upstream له، أو BC01/BC08 اللذين يخدمان الكل.", "",
          "| من | إلى | المراجع | في الخريطة المعتمدة |", "|---|---|---|---|"]
    L += [f"| {a_} | {b_} | {'؛ '.join(sorted(v))} | " +
          ("نعم" if b_ in ("BC01", "BC08") or (b_, a_) in APPROVED_EDGES else "**لا — [Needs Review]**") + " |" for (a_, b_), v in sorted(cross.items())]
    L += ["", "```mermaid", "flowchart LR"]
    for bc in sorted(BC_NAMES):
        L.append(f'  {bc}["{bc} {BC_NAMES[bc].split(" — ")[0]}"]')
    for (a_, b_), v in sorted(cross.items()):
        L.append(f"  {a_} -->|{len(v)}| {b_}")
    L += ["```", "", "### 3.3 مخططات الأصناف (Class diagrams) لكل سياق", "",
          "لكل Aggregate صنف جذر `<<AggregateRoot>>` بمفتاحه وأول ثمانية أعمدة من جدوله الرئيسي في النموذج المنطقي، بأنواع مستنتَجة وفق "
          "`16-database-schema.md` §4 **[Derived]**؛ ومكوناته الداخلية بعلاقة تركيب (`*--`)؛ ومراجعه إلى Aggregates السياق نفسه (`-->` باسم العمود). "
          "المراجع العابرة في §3.2.", ""]
    for bc in sorted(BC_NAMES):
        members = sorted(x for x in aggs if aggs[x]["bc"] == bc)
        L += [f"#### {bc} — {BC_NAMES[bc]}", "", "```mermaid", "classDiagram", "  direction LR"]
        for aid in members:
            cid = aid.replace("-", "_")
            L.append(f'  class {cid}["{aid[4:]} — {aggs[aid]["title"]}"] {{')
            L.append("    <<AggregateRoot>>")
            if aid in attrs:
                for col, raw in attrs[aid][1][:8]:
                    L.append(f"    +{col_type(raw).replace('(4326)', '')} {col}")
            else:
                L.append("    +enum state")
            L.append("  }")
            for comp in comps[aid]:
                L.append(f'  class {cid}__{comp}["{comp}"]')
                L.append(f"  {cid} *-- {cid}__{comp}")
        for (f, t), cs in sorted(refs.items()):
            if aggs[f]["bc"] == bc and aggs[t]["bc"] == bc:
                L.append(f"  {f.replace('-', '_')} --> {t.replace('-', '_')} : {sorted(cs)[0]}")
        L += ["```", ""]
        missing = [x for x in members if x not in attrs]
        L += ["| Aggregate | المستوى | بيانات شخصية | الجدول الرئيسي | المكونات الداخلية |", "|---|---|---|---|---|"]
        for aid in members:
            t = attrs.get(aid, (None,))[0]
            L.append(f"| {aid} | {aggs[aid].get('tier', '—')} | {'نعم' if aggs[aid]['personal'] else '—'} | "
                     f"{('`' + t['schema'] + '.' + t['name'] + '`') if t else ('`projection_versions` (مخزن الإسقاطات، اسم الـschema **[Missing]**)' if aid == 'AGG-PROJECTION-VERSION' else '**[Missing]**')} | {', '.join(comps[aid]) or '—'} |")
        L.append("")
    L += [END]
    write_generated(OUT / "07-domain-model.md", None, "\n".join(L))


# ------------------------------------------------------------------ 17 security design
# Issuing role for the commands whose policy subject lists roles without this command's verb (02-actors-roles.md §6.6).
# Resolved in 17-security-design.md §5 by the paired verb in the same policy; CR-77 carries them back into the policies.
ACTOR_RESOLUTION = {
    "CMD-ADP-SUSPEND": ("Administrator", "إيقاف فوري للاحتواء، مقابل register/update"),
    "CMD-ADP-RESUME": ("second Administrator", "إعادة التشغيل تعادل التفعيل (activate) فتبقى للشخص الثاني"),
    "CMD-ADP-RETIRE": ("Administrator", "نهاية دورة حياة يملكها من سجّل المحوّل"),
    "CMD-AMT-DEPRECATE": ("Analysis lead", "مقابل register؛ التفعيل وحده للشخص الثاني"),
    "CMD-AMT-RETIRE": ("Analysis lead", "مقابل register"),
    "CMD-AST-START-MAINTENANCE": ("Resource Manager", "عمليات الحالة الفنية (condition) لمدير الموارد"),
    "CMD-AST-FAIL-MAINTENANCE": ("Resource Manager", "عمليات الحالة الفنية (condition)"),
    "CMD-AST-RETURN-TO-SERVICE": ("Resource Manager", "عمليات الحالة الفنية (condition)"),
    "CMD-AST-MARK-UNSERVICEABLE": ("Resource Manager", "عمليات الحالة الفنية (condition)"),
    "CMD-AST-RECOVER": ("Resource Manager", "مقابل lost (الإبلاغ عن الفقد)"),
    "CMD-CRR-RETIRE": ("Analyst lead", "مقابل define/edit؛ التفعيل وحده للمعتمِد الثاني"),
    "CMD-DEV-ROTATE-KEY": ("user · Administrator / MDM policy", "صاحب الجهاز أو سياسة MDM التي تدير دورة حياته"),
    "CMD-ER-PARK": ("Analyst", "مقابل review/decide؛ الشخص الثاني للتأكيد والتقسيم فقط"),
    "CMD-ER-RESUME": ("Analyst", "مقابل review/decide"),
    "CMD-ER-WITHDRAW": ("Analyst", "مقابل propose"),
    "CMD-MDL-RETIRE": ("AI governance authority", "الإيقاف النهائي قرار حوكمة كالاعتماد والترقية؛ المهندس يكتفي بـdeprecate"),
    "CMD-OBS-AMEND": ("Field User / Operator / Analyst / adapter service account", "تعديل الملاحظة لمن سجّلها (record)"),
    "CMD-OBS-ATTACH-EVIDENCE": ("Field User / Operator / Analyst / adapter service account", "إرفاق الدليل لمن سجّل الملاحظة (record)"),
    "CMD-OBS-RECLASSIFY": ("Analyst", "إعادة التصنيف لمن يتحقق من الملاحظة (validate)"),
    "CMD-PTM-RETIRE": ("Knowledge Manager / Analysis lead", "مقابل define/edit"),
    "CMD-SIT-RESUME": ("Analyst / Manager", "مقابل pause"),
    "CMD-SRC-SUSPEND": ("Analyst", "مقابل register/rate؛ المصدر المحمي يبقى لمسؤول الأمن عبر protection"),
    "CMD-SRC-REINSTATE": ("Analyst", "مقابل suspend"),
    "CMD-SRC-RETIRE": ("Analyst", "مقابل register"),
    "CMD-TOL-ENABLE": ("Security Officer", "مقابل disable"),
    "CMD-TOL-RETIRE": ("Security Officer", "تفعيل الأداة وتعطيلها لمسؤول الأمن، فإيقافها النهائي له"),
}
PERMISSION_OF = [  # REQ-FND-014 permission kinds, by command verb
    ("Approve", r"^(APPROVE|REJECT|ACTIVATE|CONFIRM|PROMOTE|PUBLISH|BASELINE|DECIDE|ACCEPT)"),
    ("Delete", r"^(ERASE|DISPOSE|DESTROY|RETIRE|CANCEL|WITHDRAW|DISCARD|REVOKE|DECOMMISSION|CLOSE)"),
    ("Retain", r"^(PLACE|EXTEND|RELEASE|REQUEST-RELEASE|APPROVE-RELEASE|CANCEL-RELEASE|HOLD)|RETENTION"),
    ("Archive", r"^(ARCHIVE|TRANSFER|PRESERVE|MIGRATE|SUBMIT-PACKAGE)"),
    ("Export", r"^(EXPORT|DISTRIBUTE|SEND|DELIVER|ISSUE)"),
    ("Share", r"^(SHARE|ADD-PARTICIPANT|SUBSCRIBE|GRANT|DELEGATE)"),
]


def permission_kind(cid, a):
    v = verb_of(cid)
    if a["id"] in ("AGG-LEGAL-HOLD", "AGG-RETENTION-SCHEDULE"):
        return "Retain"
    if a["id"] in ("AGG-ARCHIVE-PACKAGE",):
        return "Archive"
    for kind, rx in PERMISSION_OF:
        if re.search(rx, v):
            return kind
    return "Edit"


def build_security(aggs, cmds, qrys, pol_c, pol_q, evts):
    acts = {a["id"]: a for a in load_actors().get("actors", [])}
    order = list(dict.fromkeys(lab for lab, _ in ROLE_RULES))
    name = lambda lab: (f"{lab} {acts[lab]['name']}" if lab in acts else f"{lab} {ROLE_LABELS[lab][0]}")  # noqa: E731
    L = [BEGIN, "", "### 12.1 حسم الفاعل للأوامر الـ26 (CR-77)", "",
         "| الأمر | الأدوار في السياسة | الفاعل المحسوم | المبرر |", "|---|---|---|---|"]
    for cid, (role, why) in sorted(ACTOR_RESOLUTION.items()):
        L.append(f"| `{cid}` | {esc(str(pol_c.get(cid, {}).get('subject', '—')))} | **{esc(role)}** | {why} |")
    perms = ["View", "Edit", "Approve", "Delete", "Retain", "Archive", "Export", "Share"]
    matrix = defaultdict(lambda: defaultdict(int))
    for cid, c in cmds.items():
        a = aggs[c["Aggregate"]]
        trs = [t for t in a["trans"] if t["cmd"] == cid]
        roles, narrowed = pick_actor(str(pol_c.get(cid, {}).get("subject") or c["الفاعل"]), cid, is_create(trs))
        if cid in ACTOR_RESOLUTION:
            roles, narrowed = ACTOR_RESOLUTION[cid][0], True
        for lab in {l_ for r in roles.split(" · ") for l_ in classify_role(r)}:
            matrix[lab][permission_kind(cid, a)] += 1
    for qid, q in qrys.items():
        for lab in {l_ for seg in re.split(r"\s*[;؛,،]\s*|\s+or\s+", query_actor(q, pol_q.get(qid, {}), pol_q)) for l_ in classify_role(seg)}:
            matrix[lab]["View"] += 1
    L += ["", "### 12.2 مصفوفة الدور × نوع الصلاحية (REQ-FND-014)", "",
          "أنواع الصلاحية الثمانية في REQ-FND-014 تُمنح منفصلة. كل أمر يُنسب إلى نوع بفعله **[Derived]** (approve/activate/publish → Approve؛ "
          "retire/cancel/erase/dispose → Delete؛ التجميد والاحتفاظ → Retain؛ الأرشفة والنقل → Archive؛ التوزيع والإرسال → Export؛ "
          "الإشراك والتفويض → Share؛ الباقي → Edit)، وكل استعلام → View. الأرقام عدد العمليات.", "",
          "| الدور | " + " | ".join(perms) + " |", "|---|" + "---|" * len(perms)]
    for lab in order:
        if matrix.get(lab):
            L.append(f"| {name(lab)} | " + " | ".join(str(matrix[lab].get(p, 0) or "—") for p in perms) + " |")
    mfa = [(c, p) for c, p in sorted(pol_c.items()) if "mfa" in str(p.get("obligations", ""))]
    L += ["", f"### 12.3 أوامر تشترط المصادقة المعززة ({len(mfa)})", "",
          "التزام `mfa` قبل التنفيذ: جلسة بقوة مصادقة أدنى تُرفض بـ`401 MFA_STEP_UP_REQUIRED` (ADR-P19، الخطوة 6 في خط الأوامر).", "",
          "| الأمر | السياق | الالتزامات | الفاعل |", "|---|---|---|---|"]
    L += [f"| `{c}` | {cmds[c]['_bc']} | {esc(p.get('obligations'))} | {esc(ACTOR_RESOLUTION.get(c, (pick_actor(str(p.get('subject')), c)[0],))[0])} |" for c, p in mfa]
    sod = [(c, p) for c, p in sorted(pol_c.items()) if str(p.get("segregation_of_duties", "—")) not in ("—", "", "None")]
    L += ["", f"### 12.4 قواعد فصل المهام ({len(sod)})", "",
          "تُقيَّم في منفذ التخويل بعد تحميل المورد (الخطوة 5)، ويعيد المجال فحص ما يقابلها من ثوابت (`09-business-rules.md`).", "",
          "| الأمر | السياق | القاعدة |", "|---|---|---|"]
    L += [f"| `{c}` | {cmds[c]['_bc']} | {esc(p.get('segregation_of_duties'))} |" for c, p in sod]
    other = [(c, p) for c, p in sorted(pol_c.items()) if re.sub(r"\b(audit|mfa)\b|[;\s]", "", str(p.get("obligations", "")))]
    L += ["", "### 12.5 التزامات أخرى", "", "| الأمر | الالتزامات |", "|---|---|"]
    L += [f"| `{c}` | {esc(p.get('obligations'))} |" for c, p in other]
    L += ["", "### 12.6 سياسات الاستعلامات", "",
          "`allowed_scope` يُطبَّق قبل العدّ والترتيب؛ «عند الرفض» شكل الاستجابة (ADR-P06).", "",
          "| الاستعلام | السياق | الموضوع | النطاق المسموح | عند الرفض |", "|---|---|---|---|---|"]
    for qid, q in sorted(qrys.items()):
        p = pol_q.get(qid, {})
        L.append(f"| `{qid}` | {q['_bc']} | {esc(str(p.get('subject', '—')))} | {esc(str(p.get('allowed_scope', '—')))} | {esc(str(p.get('otherwise', '—')))} |")
    personal = sorted(x for x in aggs if aggs[x]["personal"])
    L += ["", "### 12.7 البيانات الشخصية والتصنيف", "",
          f"- **Aggregates ببيانات شخصية ({len(personal)}):** " + ", ".join(f"`{x}`" for x in personal) +
          " — حقولها الشخصية مشفرة بمفتاح الموضوع (ADR-P08) ومحوها بإتلافه.",
          "- **مستوى الأهمية** (REQ-GOV-002: كل كائن T1/T2 يحمل تصنيفًا): " + "؛ ".join(
              f"{t}: {', '.join(x[4:] for x in sorted(aggs) if str(aggs[x].get('tier', '')).startswith(t))}" for t in ("T1", "T2", "T3")), ""]
    labels = {}
    for header, rows in tables((SPEC / "08-security" / "label-derivation-rules.md").read_text(encoding="utf-8")):
        if header and header[0] == "aggregate":
            labels.update({r[0]: dict(zip(header, r)) for r in rows})
    kinds = defaultdict(list)
    for x in sorted(aggs):
        src = labels.get(x, {}).get("label_source", "")
        first = src.split(" ")[0].rstrip(",;")
        first = "=" if first.startswith(("=", "max(", "min(", "≥")) else first
        kinds[{"=": "مشتق (= تصنيف كائن مرتبط)", "T3": "T3 — غير ملزم بتصنيف", "": "**[Missing]** (S-26)"}.get(first, first)].append(x[4:])
    L += ["**مصدر التصنيف لكل Aggregate** (`08-security/label-derivation-rules.md`، القاعدة SL-29):", "",
          "| مصدر التصنيف | العدد | الـAggregates |", "|---|---|---|"]
    L += [f"| {k} | {len(v)} | {', '.join(v)} |" for k, v in sorted(kinds.items())]
    L.append("")
    sec_ev = sorted(e for e, v in evts.items() if v.get("يؤثر أمنياً") == "نعم")
    L += [f"### 12.8 الأحداث المؤثرة أمنيًا ({len(sec_ev)})", "",
          "ترفع إصدار الأمن للموضوع وتبطل ذاكرة القرارات (`15-event-design.md` §7): " + ", ".join(f"`{e}`" for e in sec_ev), ""]
    threats = []
    for f in sorted((SPEC / "08-security").glob("threat-model*.md")):
        for header, rows in tables(f.read_text(encoding="utf-8")):
            if header and header[0] == "id" and "stride" in header:
                for r in rows:
                    d = dict(zip(header, r))
                    d["_src"] = f.stem
                    threats.append(d)
    stride = defaultdict(int)
    for t in threats:
        stride[t.get("stride", "—")] += 1
    L += [f"### 12.9 نموذج التهديدات الموحَّد ({len(threats)} تهديدًا)", "",
          "من `08-security/threat-model.md` (النواة، حسب حدود الثقة) و`threat-model-slcNN.md` (لكل شريحة، حسب المكوّن)، بتصنيف STRIDE.", "",
          "| STRIDE | العدد |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(stride.items(), key=lambda x: -x[1])]
    res = [t for t in threats if t.get("residual_risk", "L") not in ("L", "—")]
    L += ["", f"**مخاطر متبقية فوق المنخفض ({len(res)}):**", "", "| التهديد | المصدر | الحد / المكوّن | STRIDE | التهديد | الضوابط | المتبقي |", "|---|---|---|---|---|---|---|"]
    L += [f"| {t['id']} | {t['_src']} | {esc(t.get('boundary') or t.get('component', '—'))} | {t.get('stride')} | {esc(t.get('threat'))} | {esc(t.get('controls'))} | {t.get('residual_risk')} |" for t in res]
    L += ["", "#### الكتالوج الكامل", "", "| التهديد | المصدر | الحد / المكوّن | STRIDE | التهديد | الاحتمال | الأثر | الضوابط | المتبقي |", "|---|---|---|---|---|---|---|---|---|"]
    L += [f"| {t['id']} | {t['_src']} | {esc(t.get('boundary') or t.get('component', '—'))} | {t.get('stride')} | {esc(t.get('threat'))} | "
          f"{t.get('likelihood', '—')} | {t.get('impact', '—')} | {esc(t.get('controls'))} | {t.get('residual_risk', '—')} |" for t in threats]
    L += ["", END]
    write_generated(OUT / "17-security-design.md", None, "\n".join(L))


# ------------------------------------------------------------------ 18 error handling
def error_category(code, http):
    if code in ("VALIDATION_FAILED",):
        return "1. طلب غير صالح"
    if code in ("AUTHZ_DENIED", "PERMISSION_DENIED", "NOT_FOUND", "SEGREGATION_OF_DUTIES"):
        return "2. تخويل وعدم إفصاح"
    if code in ("VERSION_CONFLICT", "IDEMPOTENCY_KEY_REUSED"):
        return "3. تزامن وعدم تكرار"
    if code.endswith("_INVALID_STATE_TRANSITION"):
        return "4. انتقال حالة غير مسموح"
    if code in ("RATE_LIMITED", "AUDIT_UNAVAILABLE", "POLICY_ENGINE_UNAVAILABLE"):
        return "6. منصة"
    return "5. قاعدة عمل أو شرط انتقال"


def build_errors(aggs, cmds):
    codes = {}
    for f in sorted((SPEC / "05-contracts").glob("errors-*.md")):
        for header, rows in tables(f.read_text(encoding="utf-8")):
            if header and header[0] == "الرمز":
                for r in rows:
                    c = r[0].strip("`")
                    d = codes.setdefault(c, {"http": r[1], "retry": r[2], "slices": []})
                    d["slices"].append(f.stem.replace("errors-", ""))
    users = defaultdict(list)
    for cid, c in cmds.items():
        for e in [x.strip() for x in c["الأخطاء"].split(",") if x.strip() not in ("", "—")]:
            users[e].append(cid)
    guard_of = {}
    for a in aggs.values():
        for t in a["trans"]:
            if t.get("error") and t["error"] not in guard_of and t["guard"] not in ("—", ""):
                guard_of[t["error"]] = (a["id"], guard_clause(t["error"], t["guard"]))
    never = sorted((code, c) for code in codes if code.endswith("_INVALID_STATE_TRANSITION")
                   for c in users.get(code, []) if not any(reject_states(aggs[cmds[c]["Aggregate"]], c)))
    states = {st for a in aggs.values() for st in a["open"] + a["final"] + [x for x, _ in a["matrix"]]}
    referenced = defaultdict(set)
    for f in sorted(SPEC.rglob("*.md")):
        rel = f.relative_to(SPEC).as_posix()
        if rel.startswith(("17-system-study", "18-analysis-design", "05-contracts", "00-governance")):
            continue
        for m in re.findall(r"\b([A-Z]{3,}(?:_[A-Z0-9]+){1,6})\b", f.read_text(encoding="utf-8")):
            if (m.endswith(("_UNAVAILABLE", "_DENIED", "_EXCEEDED", "_REQUIRED", "_CONFLICT", "_TIMEOUT", "_EXPIRED", "_INVALID"))
                    and m not in codes and m not in states):
                referenced[m].add(rel)
    by_cat = defaultdict(list)
    for code, d in codes.items():
        by_cat[error_category(code, d["http"])].append(code)
    L = [BEGIN, "", "### 9.1 الملخص", "", "| الفئة | الرموز | HTTP | قابل لإعادة المحاولة |", "|---|---|---|---|"]
    for cat in sorted(by_cat):
        ids = by_cat[cat]
        L.append(f"| {cat} | {len(ids)} | {', '.join(sorted({codes[c]['http'] for c in ids}))} | "
                 f"{sum(1 for c in ids if codes[c]['retry'] == 'نعم')} |")
    L.append(f"| **المجموع** | **{len(codes)}** | | {sum(1 for c in codes.values() if c['retry'] == 'نعم')} |")
    L += ["", f"**أوامر لا يُطلِق فيها رمز `*_INVALID_STATE_TRANSITION` أبدًا ({len(never)})** — الأمر مسموح من كل حالات المصفوفة (S-03): " +
          ("، ".join(f"`{c}` في `{cmd}`" for c, cmd in never) or "لا شيء") + ".", "",
          f"**رموز تذكرها المواصفات وليست في كتالوج الأخطاء ({len(referenced)})** **[Needs Review]** (S-27):", "",
          "| الرمز | أين يُذكر |", "|---|---|"] + [f"| `{k}` | {', '.join(f'`{x}`' for x in sorted(v)[:3])} |" for k, v in sorted(referenced.items())] + [""]
    for cat in sorted(by_cat):
        L += [f"### {cat.replace(cat.split(' ')[0], '9.' + str(int(cat.split('.')[0]) + 1), 1)}", "",
              "| الرمز | HTTP | إعادة | الأوامر | السياقات | مثال الشرط (Aggregate) |", "|---|---|---|---|---|---|"]
        for code in sorted(by_cat[cat]):
            d, cs = codes[code], users.get(code, [])
            ctx = sorted({cmds[c]["_bc"] for c in cs})
            ex = guard_of.get(code)
            L.append(f"| `{code}` | {d['http']} | {d['retry']} | {len(cs) or '— (منصة)'} | {', '.join(ctx) or '—'} | "
                     f"{esc(short(ex[1], 110)) + ' (' + ex[0][4:] + ')' if ex else '—'} |")
        L.append("")
    L.append(END)
    write_generated(OUT / "18-error-handling.md", None, "\n".join(L))
    return codes, never


# ------------------------------------------------------------------ writer
def write_generated(path, header, block):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if BEGIN in text:
            text = text[: text.index(BEGIN)] + block + text[text.index(END) + len(END):]
            path.write_text(text.rstrip("\n") + "\n", encoding="utf-8")
            return
        base = text.rstrip("\n") + "\n\n"
    else:
        base = (header or "") + "\n"
    path.write_text(base + block + "\n", encoding="utf-8")


def main():
    aggs = load_aggregates()
    cmds = load_catalog("commands", "الأمر")
    qrys = load_catalog("queries", "الاستعلام")
    evts = load_catalog("events", "الحدث")
    pol_c, pol_q = load_policies()
    reqs, ucs = load_requirements()
    ops, chan, http_of = load_openapi(), load_asyncapi(), load_error_http()
    stats, story_ids = build_user_stories(aggs, cmds, qrys, pol_c, pol_q, reqs, ucs, http_of, ops)
    build_state_models(aggs)
    inv = build_business_rules(aggs, cmds, pol_c, reqs)
    build_api(ops, cmds, qrys, pol_c, pol_q, aggs)
    ne = build_events(evts, chan, aggs)
    nt = build_database(aggs)
    build_actors(aggs, cmds, qrys, pol_c, pol_q)
    build_requirements(aggs, reqs, ucs, qrys)
    build_use_cases(aggs, cmds, qrys, pol_c, reqs, ucs)
    build_domain_model(aggs, cmds)
    build_security(aggs, cmds, qrys, pol_c, pol_q, evts)
    build_errors(aggs, cmds)
    total = sum(sum(v.values()) for v in stats.values())
    print(f"stories={total} (commands={sum(1 for k in story_ids if k.startswith('CMD-'))}, "
          f"queries={sum(1 for k in story_ids if k.startswith('QRY-'))}, sys={sum(v.get('نظام (SYS)', 0) for v in stats.values())}) "
          f"aggregates={len(aggs)} invariants={inv} operations={len(ops)} events={ne} tables={nt}")


if __name__ == "__main__":
    main()
