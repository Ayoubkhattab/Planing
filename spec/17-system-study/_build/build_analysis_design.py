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
from ar_terms import AGGREGATES as AR_AGG, VERBS as AR_VERB, CATEGORIES  # noqa: E402

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
             "purpose": purpose.group(1).strip() if purpose else "", "personal": bool(fm.get("personal_data")),
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
                                          "required": body.get("required") or [], "responses": list((op.get("responses") or {}).keys()),
                                          "offline": bool(op.get("x-offline-capable")), "file": path.name,
                                          "internal": "internal" in path.name or p.startswith("/internal")}
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
    tmpl = AR_VERB.get(verb_of(cmd), verb_of(cmd).replace("-", " ").lower() + " {a}")
    return tmpl.format(a=agg_ar(aid, aggs))


def op_type(cmd, a, catalog_row):
    trs = [t for t in a["trans"] if t["cmd"] == cmd]
    actor = (catalog_row or {}).get("الفاعل", "")
    if (catalog_row or {}).get("داخلي") == "نعم" or actor.lower().startswith("system"):
        return "نظام"
    if any(t["from"] == ["∅"] for t in trs):
        return "إنشاء"
    if verb_of(cmd) in ("ERASE", "DISPOSE"):
        return "حذف / إنهاء"
    targets = {t["to"] for t in trs}
    if targets and targets <= set(a["final"]):
        return "حذف / إنهاء"
    if targets == {"="} or targets == {"(بلا تغيير)"}:
        return "تعديل"
    return "سير عمل"


def pick_actor(actor, cmd):
    """Returns the actor part whose verb list matches the command, without that list."""
    words = {w.lower()[:5] for w in verb_of(cmd).split("-") if len(w) > 2}
    parts = [p.strip() for p in actor.split(" · ") if p.strip()]
    best, score = None, 0
    for p in parts:
        m = re.search(r"\(([^)]*)\)", p)
        if not m:
            continue
        toks = {t.lower()[:5] for t in re.findall(r"[A-Za-z]{3,}", m.group(1))}
        hit = len(words & toks)
        if hit > score:
            best, score = p, hit
    if best is None:
        return re.sub(r"\s*\((?!in scope|owner|not self)[^)]*\)", "", actor).strip() if len(parts) > 1 else actor
    return re.sub(r"\s*\([^)]*\)", "", best).strip()


def sys_kind(trigger):
    t = trigger.lower()
    if re.search(r"lease|worker|error or timeout|^completed|package validated|validation failed|integrity check|build", t):
        return "مدفوع بعامل"
    if re.search(r"reached|passed|elapsed|expir|timeout|window|due|deadline|period|after \d|older than|age", t):
        return "زمني"
    if re.search(r"linked|successor|baselined|committed|released|published|activated|rejected|confirmed|hold |matches|"
                 r"approval|resolved|closed|retired|disposition|event|arrived|received|delivered|signal", t):
        return "مدفوع بحدث"
    return "شرطي"


def expand_from(frm, a):
    if frm == ["*NT"]:
        return [s for s in a["open"]]
    return frm


def payload_fields(payload):
    return [(m.group(1), bool(m.group(2)), m.group(3)) for m in re.finditer(r"(\w+)(!?):([^\s,`]+)", (payload or "").replace("`", ""))]


# ------------------------------------------------------------------ 05 user stories
TYPE_CHECK = {"إنشاء": "C-CRE", "تعديل": "C-UPD", "سير عمل": "C-WF", "حذف / إنهاء": "C-DEL", "جلب": "C-READ",
              "نظام": "C-SYS"}
CAT_CHECK = {"تحليل": "K-ANL", "تقارير ومنتجات": "K-RPT", "تكامل": "K-INT", "حوكمة وأمن": "K-GOV", "أساسية": "K-CORE"}


def reject_states(a, cmd):
    return sorted({s for (s, c), cell in a["matrix"].items() if c == cmd and cell.startswith("✗") and s != "∅"})


def error_condition(code, cmd, a, pol, trs, mandatory):
    if code == "AUTHZ_DENIED":
        return f"السياسة {pol.get('id', '—')} لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له"
    if code == "VALIDATION_FAILED":
        return "حقل إلزامي مفقود أو غير صالح" + (f": {', '.join(mandatory)}" if mandatory else "")
    if code == "VERSION_CONFLICT":
        return "قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل)"
    if code == "IDEMPOTENCY_KEY_REUSED":
        return "نفس Idempotency-Key مع حمولة مختلفة"
    if code.endswith("_INVALID_STATE_TRANSITION"):
        rs = reject_states(a, cmd)
        return "الحالة الحالية واحدة من: " + (", ".join(rs) if rs else "حالات لا يسمح منها الأمر")
    if code == "SEGREGATION_OF_DUTIES":
        sod = pol.get("segregation_of_duties", "—")
        return f"فصل المهام: {sod}" if sod not in ("—", "", None) else "المنفّذ هو نفسه من يُمنع عليه ذلك (فصل المهام)"
    if code == "REASON_REQUIRED":
        return "لم يُذكر السبب"
    guards = [t["guard"] for t in trs if t.get("error") == code]
    if guards:
        return "لم يتحقق الشرط: " + guards[0]
    return "انظر شرط الانتقال وكتالوج الأخطاء"


def command_story(cid, c, a, aggs, pol, reqs_txt, ucs_of, http_of, ops):
    trs = [t for t in a["trans"] if t["cmd"] == cid]
    typ = op_type(cid, a, c)
    cat = category(a["id"])
    actor = pick_actor(str(pol.get("subject") or c["الفاعل"]), cid)
    if " · " in actor and " · " not in pick_actor(c["الفاعل"], cid):
        actor = pick_actor(c["الفاعل"], cid)
    fields = payload_fields(c.get("الحمولة (! إلزامي)", ""))
    mandatory = [n for n, req, _ in fields if req]
    froms = sorted({s for t in trs for s in expand_from(t["from"], a)})
    tos = sorted({t["to"] for t in trs})
    events = [e for e in re.findall(r"EVT-[A-Z0-9-]+", c["الأحداث"])]
    errors = [e.strip() for e in c["الأخطاء"].split(",") if e.strip() and e.strip() != "—"]
    op = ops.get(cid, {})
    sid = f"US-{a['bc']}-{cid[4:]}"
    L = [f"#### {sid} — {action_phrase(cid, a['id'], aggs)}", "",
         f"| النوع | الفئة | الفاعل | الواجهة | السياسة |", "|---|---|---|---|---|",
         f"| {typ} | {cat} | {esc(actor)} | `{op.get('method', '?')} {op.get('path', c['HTTP'].strip('`'))}` | {pol.get('id', '—')} |", "",
         f"**القصة:** بصفتي **{esc(actor)}**، أريد **{action_phrase(cid, a['id'], aggs)}**، لكي يتحقق غرض {agg_ar(a['id'], aggs)}: {esc(a['purpose']) or '—'}", "",
         f"- **الشروط المسبقة:** الحالة الحالية ∈ {{{', '.join(froms)}}}؛ {esc('؛ '.join(sorted({t['guard'] for t in trs if t['guard'] not in ('—', '')})) or 'لا شروط إضافية')}",
         f"- **المدخلات:** " + (", ".join(f"`{n}`{'!' if r else ''}: {esc(t)}" for n, r, t in fields) if fields else "لا حمولة") + " — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء",
         f"- **المخرجات:** الحالة ← {', '.join('(بلا تغيير)' if t in ('=', '(بلا تغيير)') else t for t in tos)}؛ الحدث {', '.join(events) or '—'}؛ الاستجابة `ResourceRef` (id، version)",
         f"- **الصلاحية:** {esc(pol.get('subject', '—'))}؛ الشروط: {esc(pol.get('context_conditions', '—'))}؛ فصل المهام: {esc(pol.get('segregation_of_duties', '—'))}؛ الالتزامات: {esc(pol.get('obligations', '—'))}",
         f"- **الربط:** `{cid}` · `{a['id']}` · متطلبات: {', '.join(a['reqs']) or '—'} · حالات استخدام: {', '.join(ucs_of(a)) or '—'}",
         f"- **ضوابط النوع والفئة:** {TYPE_CHECK[typ]}، {CAT_CHECK[cat]} (التعريف في [00-guide.md](00-guide.md))", "",
         "```gherkin",
         f"Scenario: {cid} succeeds",
         f"  Given {a['id']} in state {' or '.join(froms) if froms else '∅ (new)'} and every guard holds",
         f"  When {actor.split('(')[0].strip()} sends {cid} with a valid payload, a new Idempotency-Key" + ("" if typ == "إنشاء" else " and a matching If-Match"),
         f"  Then the state becomes {' or '.join('unchanged' if t in ('=', '(بلا تغيير)') else t for t in tos)}",
         f"  And {', '.join(events) or 'no event'} is written to the outbox with one audit record in the same transaction", "",
         f"Scenario Outline: {cid} is rejected",
         "  When the command is sent while <condition>",
         "  Then it is rejected with <code> (HTTP <http>) and nothing changes", "",
         "  Examples:",
         "    | code | http | condition |"]
    for code in errors:
        L.append(f"    | {code} | {http_of.get(code, '?')} | {esc(error_condition(code, cid, a, pol, trs, mandatory))} |")
    L += ["```", ""]
    return sid, typ, cat, L


def query_story(qid, q, a, aggs, pol, reqs, ops):
    op = ops.get(qid, {})
    cat = category(a["id"]) if a else "أساسية"
    subject = pol.get("subject", q.get("من يحق له (السياسة قبل الاسترجاع — SL-09)", "—"))
    req_ids = re.findall(r"REQ-[A-Z]+-\d+", q.get("المتطلب", ""))
    why = reqs.get(req_ids[0], {}).get("statement", "") if req_ids else ""
    params = [n for n, where, _ in op.get("params", []) if where == "query"]
    paged = any(p in ("cursor", "limit", "page_size") for p in params)
    asof = [p for p in params if p in ("valid_at", "known_at", "as_of")]
    bc = a["bc"] if a else q["_bc"]
    sid = f"US-{bc}-Q-{qid[4:]}"
    L = [f"#### {sid} — جلب: {esc(q.get('يعيد', ''))}", "",
         "| النوع | الفئة | الفاعل | الواجهة | السياسة |", "|---|---|---|---|---|",
         f"| جلب | {cat} | {esc(subject)} | `{op.get('method', '?')} {op.get('path', q['HTTP'].strip('`'))}` | {pol.get('id', '—')} |", "",
         f"**القصة:** بصفتي **{esc(subject)}**، أريد **جلب {esc(q.get('يعيد', ''))}**، لكي يتحقق المتطلب: {esc(why.rstrip('.')) or '—'}", "",
         f"- **المدخلات:** " + (", ".join(f"`{p}`" for p in params) if params else "معاملات المسار فقط"),
         f"- **المخرجات:** {esc(q.get('يعيد', ''))}" + ("؛ صفحة بمؤشر (لا offset — FIT-13)" if paged else ""),
         f"- **الصلاحية:** {esc(subject)}؛ النطاق المسموح: {esc(pol.get('allowed_scope', '—'))}؛ عند الرفض: {esc(pol.get('otherwise', 'DENY (not-found shape)'))}",
         f"- **الزمن:** " + (f"استعلام بأثر رجعي عبر {', '.join('`'+x+'`' for x in asof)}" if asof else "الحالة الحالية"),
         f"- **الربط:** `{qid}` · {('`'+a['id']+'`') if a else 'عابر للـAggregates'} · متطلبات: {', '.join(req_ids) or '—'}",
         f"- **ضوابط النوع والفئة:** C-READ، {CAT_CHECK[cat]}", "",
         "```gherkin",
         f"Scenario: {qid} returns only what the caller may see",
         "  Given items inside and outside the caller's allowed_scope",
         f"  When the caller sends {qid}" + (" with a cursor" if paged else ""),
         "  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)",
         "  And no count, facet or suggestion reveals a hidden item", "",
         f"Scenario: {qid} is denied",
         "  Given the policy denies the caller",
         f"  When the caller sends {qid}",
         "  Then the response has the same shape as for a missing item (not-found shape)",
         "```", ""]
    return sid, L


def sys_story(a, t, aggs, n):
    trig = t["cmd"][4:].strip()
    kind = sys_kind(trig)
    froms = expand_from(t["from"], a)
    to = "(بلا تغيير)" if t["to"] in ("=", "(بلا تغيير)") else t["to"]
    sid = f"US-{a['bc']}-S-{a['id'][4:]}-{n:02d}"
    L = [f"#### {sid} — تلقائي: {esc(trig)} ({agg_ar(a['id'], aggs)})", "",
         "| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |", "|---|---|---|---|---|",
         f"| نظام | {kind} | النظام بهوية عبء عمل | {', '.join(froms)} | {to} |", "",
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
    prefix_agg = {}
    for cid, c in cmds.items():
        prefix_agg.setdefault((c["_bc"], cid.split("-")[1]), c["Aggregate"])
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
                sid, typ, cat, block = command_story(cid, cmds[cid], a, aggs, pol_c.get(cid, {}), reqs, ucs_of, http_of, ops)
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
            for qid in sorted(q for q in qrys if qrys[q]["_bc"] == bc and prefix_agg.get((bc, q.split("-")[1])) == aid):
                sid, block = query_story(qid, qrys[qid], a, aggs, pol_q.get(qid, {}), reqs, ops)
                L += block
                stats[bc]["جلب"] += 1
                story_ids[qid] = sid
        orphan_q = sorted(q for q in qrys if qrys[q]["_bc"] == bc and q not in story_ids)
        if orphan_q:
            L += ["### استعلامات عابرة للـAggregates", ""]
            for qid in orphan_q:
                sid, block = query_story(qid, qrys[qid], None, aggs, pol_q.get(qid, {}), reqs, ops)
                L += block
                stats[bc]["جلب"] += 1
                story_ids[qid] = sid
        per_bc[bc] = L
    cat_rows = defaultdict(list)
    for aid in sorted(aggs):
        cat_rows[category(aid)].append(f"{agg_ar(aid, aggs)} (`{aid[4:]}`)")
    write_generated(OUT / "05-user-stories" / "00-guide.md", None, "\n".join(
        [BEGIN, "| الفئة | الـAggregates | العدد |", "|---|---|---|"] +
        [f"| {c} | {'، '.join(v)} | {len(v)} |" for c, v in sorted(cat_rows.items())] + [END]))
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
                L.append(f"  {f} --> {t} : {', '.join(dict.fromkeys(labels))}")
            for s in a["final"]:
                L.append(f"  {s} --> [*]")
            L += ["```", ""]
            if groups:
                L += ["مجموعات الحالات في المخطط: " + "؛ ".join(f"**{gid}** = {', '.join(key)}" for key, gid in groups.items()), ""]
            if selfs:
                grouped = defaultdict(set)
                for f, lab in selfs:
                    grouped[lab].add(f)
                L += ["أوامر لا تغيّر الحالة: " + "؛ ".join(f"{lab} ({', '.join(sorted(fs))})" for lab, fs in sorted(grouped.items())), ""]
    L.append(END)
    write_generated(OUT / "08-state-models.md", None, "\n".join(L))


# ------------------------------------------------------------------ 09 business rules
def build_business_rules(aggs, cmds, pol_c, reqs):
    brl = md_records((SPEC / "01-business" / "business-rules.md").read_text(encoding="utf-8"), "BRL")
    req_aggs = defaultdict(list)
    for aid, a in aggs.items():
        for r in a["reqs"]:
            req_aggs[r].append(aid)
    L = [BEGIN, "", "## 1. قواعد العمل العليا (BRL)", "", "| القاعدة | النص | يُنفِّذها | الـAggregates (Derived عبر المتطلب) |", "|---|---|---|---|"]
    for bid, b in sorted(brl.items()):
        enf = re.findall(r"REQ-[A-Z]+-\d+", b.get("enforced_by", ""))
        ag = sorted({x for r in enf for x in req_aggs.get(r, [])})
        L.append(f"| {bid} | {esc(b.get('statement', ''))} | {', '.join(enf) or esc(b.get('enforced_by', '—'))} | {', '.join(ag) or '—'} |")
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
                L += [f"| {t['cmd']} | {', '.join(t['from'])} | {esc(t['guard'])} | {t['error'] or '—'} |" for t in guards] + [""]
            sod = [(c, pol_c[c]["segregation_of_duties"]) for c in sorted(cmds) if cmds[c]["Aggregate"] == aid
                   and c in pol_c and str(pol_c[c].get("segregation_of_duties", "—")) not in ("—", "", "None")]
            if sod:
                L += ["**فصل المهام:** " + "؛ ".join(f"{c}: {esc(s)}" for c, s in sod), ""]
            rds = sorted(set(re.findall(r"(?<![A-Z-])RD-[A-Z0-9-]*[A-Z0-9]", " ".join(t["guard"] for t in a["trans"]))) & rd_ids)
            if rds:
                L += ["**بيانات مرجعية مستخدمة:** " + ", ".join(rds) + " (`04-information/reference-data.md`)", ""]
    L.append(END)
    write_generated(OUT / "09-business-rules.md", None, "\n".join(L))
    return total_inv


# ------------------------------------------------------------------ 14 API design
def build_api(ops, cmds, qrys, pol_c, pol_q, aggs):
    bc_of = {**{k: v["_bc"] for k, v in cmds.items()}, **{k: v["_bc"] for k, v in qrys.items()}}
    by_bc = defaultdict(list)
    for oid, o in ops.items():
        by_bc[bc_of.get(oid, "—")].append((oid, o))
    L = [BEGIN, "", "## الكتالوج الكامل للعمليات", "", f"إجمالي العمليات: **{len(ops)}**.", "",
         "| BC | أوامر | استعلامات | داخلية | المجموع |", "|---|---|---|---|---|"]
    for bc in sorted(by_bc):
        items = by_bc[bc]
        L.append(f"| {bc} | {sum(1 for o, _ in items if o.startswith('CMD-'))} | {sum(1 for o, _ in items if o.startswith('QRY-'))} | "
                 f"{sum(1 for _, x in items if x['internal'])} | {len(items)} |")
    for bc in sorted(by_bc):
        L += ["", f"### {bc} — {BC_NAMES.get(bc, 'عقود عابرة')}", ""]
        groups = defaultdict(list)
        for oid, o in by_bc[bc]:
            seg = o["path"].split("/")
            groups["/".join(seg[:5])].append((oid, o))
        for res in sorted(groups):
            L += [f"#### `{res}`", "", "| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |",
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
                    inputs = ", ".join([n for n, where, _ in o["params"] if where == "query"] +
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
    L = [BEGIN, "", "## الكتالوج حسب القناة", "", "| القناة | العنوان | عدد الأحداث |", "|---|---|---|"]
    L += [f"| {c[0]} | `{c[1]}` | {len(v)} |" for c, v in sorted(by_ch.items())]
    for c, items in sorted(by_ch.items()):
        L += ["", f"### {c[0]} — `{c[1]}`", "", "| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |", "|---|---|---|---|---|"]
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
    if "(enc)" in c:
        return "bytes_encrypted"
    if "json" in c:
        return "json"
    if c.startswith(("geom", "geometry", "footprint", "area_geom", "location_geom")) or "(4326)" in c:
        return "geometry(4326)"
    if c.endswith("[]") or "(array)" in c or "[]" in c:
        return "array"
    base = re.sub(r"\(.*", "", c).strip().rstrip("?")
    if base.endswith("_at") or base in ("valid_from", "valid_to", "window_from", "window_to", "needed_by", "due"):
        return "timestamptz"
    if base.endswith(("_id", "_ref", "_urn")) or base in ("urn", "owner", "requester", "assignee", "reviewer", "actor"):
        return "urn"
    if base in ("version", "seq", "attempt", "depth", "priority", "occurrences") or base.endswith(("_version", "_count")):
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
    name = name.replace("**", "").rstrip("?").strip()
    return re.sub(r"[^A-Za-z0-9_]", "_", name).strip("_")


def load_ldm():
    tables_out, projections, client = {}, [], []
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
                    if name.startswith("*_") or name in ("outbox", "audit_outbox", "inbox", "idempotency_keys", "security_versions (KV)", "security_versions"):
                        continue
                    ephemeral = "ephemeral" in raw
                    cols = [c for c in split_top(r[2]) if not c.startswith("...")]
                    key, _, part = r[1].partition("·")
                    key, part = key.strip(), part.replace("**", "").strip()
                    tid = (current or "—", name)
                    if tid in tables_out:
                        t = tables_out[tid]
                        t["cols"] += [c for c in cols if clean_col(c) not in {clean_col(x) for x in t["cols"]}]
                        t["ext"].append(f"{sfx}: {r[3]}")
                    else:
                        tables_out[tid] = {"schema": current or "—", "name": name, "key": key, "cols": cols,
                                           "constraints": r[3], "slice": sfx, "ephemeral": ephemeral, "partition": part,
                                           "ext": [f"{sfx}: {r[3]}"] if "extended" in raw or "unchanged" in raw else []}
    return tables_out, projections, client


def build_database(aggs):
    tabs, projections, client = load_ldm()
    by_schema = defaultdict(list)
    for (schema, name), t in sorted(tabs.items()):
        by_schema[schema].append(t)
    L = [BEGIN, "", "## الملخص", "", "| الـschema | السياق المالك | الجداول |", "|---|---|---|"]
    L += [f"| `{s}` | {SCHEMA_BC.get(s, '—')} | {len(v)} |" for s, v in sorted(by_schema.items())]
    L += [f"| مخزن الإسقاطات (الاسم [Missing]) | BC07 | {len(projections)} وثيقة/جدول |", ""]
    for schema, items in sorted(by_schema.items()):
        L += ["", f"## schema `{schema}` — {SCHEMA_BC.get(schema, '—')}", ""]
        keys = {}
        for t in items:
            kcols = [c.strip() for c in t["key"].strip("()").split(",") if c.strip() and c.strip() != "tenant_id"]
            if kcols:
                keys[kcols[-1]] = t["name"]
        rels = []
        for t in items:
            own = clean_col(t["key"].strip("()").split(",")[-1])
            key_cols = [clean_col(c) for c in t["key"].strip("()").split(",")]
            for cn in dict.fromkeys(key_cols + [clean_col(c) for c in t["cols"]]):
                if cn in ("tenant_id", own):
                    continue
                base = cn[:-4] if cn.endswith("_ref") else (cn[:-3] if cn.endswith("_id") else None)
                if base and base.startswith("parent_"):
                    base = base[len("parent_"):]
                target = keys.get(f"{base}_id") if base else None
                if target:
                    rels.append((t["name"], target, cn))
        L += ["```mermaid", "erDiagram"]
        for t in items:
            ent = re.sub(r"[^A-Za-z0-9_]", "_", t["name"])
            kcols = [clean_col(c) for c in t["key"].strip("()").split(",") if clean_col(c)]
            fks = {cn for (src, _, cn) in rels if src == t["name"]}
            L.append(f"  {ent} {{")
            for k in kcols:
                L.append(f"    {col_type(k)} {k} PK" + (", FK" if k in fks else ""))
            for fk in sorted(fks - set(kcols)):
                L.append(f"    urn {fk} FK")
            L.append("  }")
        for src, dst, cn in rels:
            L.append(f"  {re.sub(r'[^A-Za-z0-9_]', '_', dst)} ||--o{{ {re.sub(r'[^A-Za-z0-9_]', '_', src)} : \"{cn}\"")
        L += ["```", "", "العلاقات في المخطط مستنتَجة من أسماء الأعمدة (`x_id` / `x_ref` → مفتاح الجدول المقابل) **[Derived]**؛ الأنواع مستنتَجة من الاصطلاحات (§2) **[Derived]**.", ""]
        for t in items:
            L += [f"### `{schema}.{t['name']}`" + (" — مؤقت (ephemeral)" if t["ephemeral"] else ""), "",
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
    L += ["", "## مخزن الإسقاطات (BC07)", "",
          "اسم الـschema غير محدد في `06-data/logical-model/slc-05.md` **[Missing]**. كل ما فيه قابل لإعادة البناء من المالكين (INV-PRJ-01، FIT-11)، "
          "ومنه إسقاط ميزات البلاطات الذي يقرأه DU-12 (`11-hexagonal-reference.md` §8).", "",
          "| الوثيقة / الجدول | المفتاح | الحقول | ملاحظات |", "|---|---|---|---|"]
    L += [f"| {p['name']} | `{esc(p['key'])}` | {esc(p['cols'])} | {esc(p['notes'])} |" for p in projections]
    L += ["", "## المخزن على الجهاز الميداني (مشفر)", "", "| المخزن | المحتوى |", "|---|---|"]
    L += [f"| {a} | {esc(b)} |" for a, b in client]
    L += ["", END]
    write_generated(OUT / "16-database-schema.md", None, "\n".join(L))
    return sum(len(v) for v in by_schema.values())


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
    total = sum(sum(v.values()) for v in stats.values())
    print(f"stories={total} (commands={sum(1 for k in story_ids if k.startswith('CMD-'))}, "
          f"queries={sum(1 for k in story_ids if k.startswith('QRY-'))}, sys={sum(v.get('نظام (SYS)', 0) for v in stats.values())}) "
          f"aggregates={len(aggs)} invariants={inv} operations={len(ops)} events={ne} tables={nt}")


if __name__ == "__main__":
    main()
