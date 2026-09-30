#!/usr/bin/env python3
"""Regenerates the per-aggregate relationship chains in 02-relationship-index.md.

Run from anywhere: python3 spec/17-system-study/_build/build_relationships.py
Only the block between the GENERATED markers is rewritten.
"""
import re
from collections import defaultdict
from pathlib import Path

import yaml

SPEC = Path(__file__).resolve().parents[2]
STUDY = SPEC / "17-system-study"
CTX = SPEC / "03-domain" / "contexts"
TARGET = STUDY / "02-relationship-index.md"
BEGIN = "<!-- BEGIN GENERATED: build_relationships.py -->"
END = "<!-- END GENERATED: build_relationships.py -->"

BC_FILES = {
    "BC01": "bc01-foundation.md",
    "BC02": "bc02-information-core.md",
    "BC03": "bc03-situational-awareness.md",
    "BC04": "bc04-planning-execution.md",
    "BC05": "bc05-resources-readiness.md",
    "BC06": "bc06-knowledge-products.md",
    "BC07": "bc07-integration-ai-discovery.md",
    "BC08": "bc08-governance-security.md",
}

ID = r"[A-Z][A-Z0-9]*(?:-[A-Za-z0-9]+)+"


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def table_rows(text, first_col_prefix):
    """Yields dicts for every markdown table row whose first cell starts with the prefix."""
    header = None
    for line in text.splitlines():
        if not line.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if set(line.replace("|", "").strip()) <= set("-: "):
            continue
        if cells[0].startswith(first_col_prefix) and len(cells) == len(header):
            yield dict(zip(header, cells))


def md_records(text, prefix):
    """Parses '### <ID> — title' sections with '- **key:** value' bullets."""
    recs = {}
    for block in re.split(r"\n(?=### )", text):
        m = re.match(rf"### ({prefix}-[A-Za-z0-9-]+)(?: — (.*))?", block)
        if not m:
            continue
        rec = {"title": (m.group(2) or "").strip()}
        for k, v in re.findall(r"^- \*\*([a-z_]+):\*\* (.*)$", block, re.M):
            rec[k] = v.strip()
        recs[m.group(1)] = rec
    return recs


def ids(value, prefix):
    return re.findall(rf"\b{prefix}-[A-Za-z0-9.]+(?:-[A-Za-z0-9]+)*", value or "")


def load():
    aggs = {}
    for path in sorted(CTX.glob("BC*/aggregates/AGG-*.md")):
        text = path.read_text(encoding="utf-8")
        fm = front_matter(text)
        traces = fm.get("traces") or {}
        states_open = re.search(r"غير نهائية: (.*)", text)
        states_final = re.search(r"^- نهائية: (.*)", text, re.M)
        aggs[fm["id"]] = {
            "title": fm.get("title", ""),
            "bc": fm.get("bounded_context") or path.parts[-3],
            "slice": fm.get("slice", ""),
            "tier": fm.get("importance_tier", ""),
            "personal": fm.get("personal_data"),
            "status": fm.get("status", ""),
            "reqs": list(traces.get("satisfies") or []),
            "adrs": list(traces.get("decided_by") or []),
            "sm": traces.get("state_machine", ""),
            "invs": sorted(set(re.findall(r"^- \*\*(INV-[A-Z0-9-]+)\*\*", text, re.M))),
            "states_open": states_open.group(1).strip() if states_open else "",
            "states_final": states_final.group(1).strip() if states_final else "",
            "path": path.relative_to(SPEC).as_posix(),
            "cmds": [], "evts": [], "qrys": [], "thrs": set(), "ucs": set(), "caps": set(),
        }

    cmd_prefix = {}
    for path in sorted(CTX.glob("BC*/commands-*.md")):
        for r in table_rows(path.read_text(encoding="utf-8"), "CMD-"):
            agg = r["Aggregate"]
            if agg not in aggs:
                continue
            aggs[agg]["cmds"].append({
                "id": r["الأمر"], "actor": r["الفاعل"], "policy": r["السياسة"],
                "internal": r["داخلي"], "http": r["HTTP"].strip("`"),
                "events": ids(r["الأحداث"], "EVT"),
            })
            cmd_prefix.setdefault(r["الأمر"].split("-")[1], agg)

    evt_index = {}
    for path in sorted(CTX.glob("BC*/events-*.md")):
        for r in table_rows(path.read_text(encoding="utf-8"), "EVT-"):
            agg = r["Aggregate"]
            if agg not in aggs:
                continue
            e = {"id": r["الحدث"], "producers": ids(r["ينتجه"], "CMD") or [r["ينتجه"]],
                 "security": r["يؤثر أمنياً"], "consumers": r["المستهلكون"]}
            aggs[agg]["evts"].append(e)
            evt_index[e["id"]] = agg

    unmapped_q = defaultdict(list)
    for path in sorted(CTX.glob("BC*/queries-*.md")):
        bc = path.parts[-2]
        for r in table_rows(path.read_text(encoding="utf-8"), "QRY-"):
            q = {"id": r["الاستعلام"], "reqs": ids(r["المتطلب"], "REQ")}
            agg = cmd_prefix.get(q["id"].split("-")[1])
            if agg and aggs[agg]["bc"] == bc:
                aggs[agg]["qrys"].append(q)
            else:
                unmapped_q[bc].append(q["id"])

    reqs = md_records((SPEC / "02-requirements" / "requirements.md").read_text(encoding="utf-8"), "REQ")
    ucs = md_records((SPEC / "02-requirements" / "use-cases.md").read_text(encoding="utf-8"), "UC")
    req_to_ucs = defaultdict(set)
    for rid, r in reqs.items():
        for u in ids(r.get("use_cases"), "UC"):
            req_to_ucs[rid].add(u)
    for uid, u in ucs.items():
        for rid in ids(u.get("requirements"), "REQ"):
            req_to_ucs[rid].add(uid)

    threats = {}
    for path in sorted((SPEC / "08-security").glob("threat-model-slc*.md")):
        text = path.read_text(encoding="utf-8")
        for r in table_rows(text, "THR-"):
            threats[r["id"]] = r.get("threat", "") + " " + r.get("controls", "")
        for tid, body in re.findall(r"^### (THR-[A-Z0-9-]+)\n(.*?)(?=^### |\Z)", text, re.M | re.S):
            threats[tid] = body

    for aid, a in aggs.items():
        own_ids = {aid, *a["invs"], *(c["id"] for c in a["cmds"]), *(q["id"] for q in a["qrys"])}
        for tid, body in threats.items():
            if own_ids & set(re.findall(ID, body)):
                a["thrs"].add(tid)
        for rid in a["reqs"]:
            a["ucs"] |= req_to_ucs.get(rid, set())
            cap = reqs.get(rid, {}).get("capability")
            if cap:
                a["caps"].add(cap)

    linked = {t for a in aggs.values() for t in a["thrs"]}
    unlinked_thr = sorted(t for t in threats if t not in linked)
    return aggs, reqs, ucs, req_to_ucs, unmapped_q, unlinked_thr, evt_index


def acceptance_path(a):
    name = a["sm"].replace("SM-", "").lower() if a["sm"] else ""
    for p in (SPEC / "13-verification" / "acceptance").glob(f"*/{name}-state-machine.md"):
        return p.relative_to(SPEC).as_posix()
    return None


def fmt(items):
    items = sorted(items)
    return ", ".join(items) if items else "—"


def render(aggs, reqs, ucs, req_to_ucs, unmapped_q, unlinked_thr, evt_index):
    out = [BEGIN, "", "## 21. السلاسل الكاملة لكل Aggregate (مولَّدة آليًا)", ""]
    out.append(
        "هذا القسم مولَّد بالكامل من المصادر بواسطة `_build/build_relationships.py`، ويُعاد توليده "
        "عند تغيّر أي مصدر، فلا يُحرَّر يدويًا. يجيب لكل Aggregate عن الأسئلة: ما القدرات والـUse Cases "
        "والمتطلبات المرتبطة؟ ما الأوامر، ومن ينفّذها، وأي سياسة تحكمها؟ ما الأحداث الناتجة، ومن يستهلكها؟ "
        "ما الثوابت والاستعلامات والتهديدات والاختبارات المرتبطة؟"
    )
    out += ["", "**تصنيف المعرفة لكل حلقة في السلسلة:**", "",
            "| الحلقة | المصدر | التصنيف |", "|---|---|---|",
            "| AGG → REQ، ADR، INV، الحالات | front-matter وجسم ملف الـAggregate | Explicit |",
            "| AGG → CMD (الفاعل، السياسة، الأحداث) | عمود Aggregate في `commands-slcNN.md` | Explicit |",
            "| AGG → EVT → المستهلكون | عمود Aggregate في `events-slcNN.md` | Explicit |",
            "| REQ → UC | `use_cases` في المتطلب و`requirements` في الـUC | Explicit |",
            "| REQ → CAP | حقل `capability` في المتطلب | Explicit |",
            "| AGG → QRY | بادئة المعرّف (QRY-XXX- ↔ CMD-XXX-) داخل نفس الـBC | Derived |",
            "| AGG → THR | تهديد يستشهد نصّه أو ضوابطه بمعرّف من هذا الـAggregate (AGG/CMD/QRY/INV) | Derived |",
            "| AGG → اختبار القبول | `traces.state_machine` ↔ اسم ملف `13-verification/acceptance/*` | Derived |",
            "", "**ما لا يُولَّد هنا:** طبقة Features غير موجودة في المصادر أصلًا (لا يوجد أي كيان `FEAT-*` "
            "في `spec/`)، فالسلسلة تنتقل مباشرة من CAP إلى UC. هذا **[Missing]** في المصدر لا في هذه الدراسة.", ""]

    # coverage summary
    all_aggs = list(aggs.values())
    no_uc = [aid for aid, a in aggs.items() if not a["ucs"]]
    no_cmd = [aid for aid, a in aggs.items() if not a["cmds"]]
    no_evt_consumer = sorted(e["id"] for a in all_aggs for e in a["evts"]
                             if e["consumers"] in ("", "—", "-"))
    missing_acc = [aid for aid, a in aggs.items() if not acceptance_path(a)]
    agg_reqs = {r for a in all_aggs for r in a["reqs"]}
    out += ["### 21.1 ملخص التغطية (محسوب)", "",
            "| المقياس | القيمة |", "|---|---|",
            f"| Aggregates | {len(aggs)} |",
            f"| أوامر مرتبطة بـAggregate | {sum(len(a['cmds']) for a in all_aggs)} |",
            f"| أحداث مرتبطة بـAggregate | {sum(len(a['evts']) for a in all_aggs)} |",
            f"| استعلامات مرتبطة بـAggregate (Derived) | {sum(len(a['qrys']) for a in all_aggs)} |",
            f"| استعلامات لم تُطابَق مع Aggregate بالبادئة | {sum(len(v) for v in unmapped_q.values())} |",
            f"| متطلبات يلبيها Aggregate واحد على الأقل (`traces.satisfies`) | {len(agg_reqs)} من {len(reqs)} |",
            f"| Aggregates بلا أي UC عبر متطلباتها | {len(no_uc)} |",
            f"| Aggregates بلا أوامر | {len(no_cmd)} |",
            f"| أحداث بلا مستهلك مُعلَن | {len(no_evt_consumer)} |",
            f"| Aggregates بلا ملف اختبار قبول مطابق | {len(missing_acc)} |", ""]
    if no_uc:
        out += ["**Aggregates بلا أي Use Case عبر حلقة REQ→UC:** "
                + ", ".join(f"`{x}` ({aggs[x]['bc']})" for x in sorted(no_uc)),
                "",
                "هذه القائمة آلية وتتبع حلقة REQ→UC فقط. قد يربط ملف الـBC حالة استخدام بالـAggregate مباشرة "
                "(Derived، في §5 منه)، فراجعه قبل اعتبار البند فجوة. الفجوات المؤكَّدة يدويًا مسجَّلة في "
                "[05-conflicts.md §6](05-conflicts.md) (CONFLICT-05).", ""]
    if missing_acc:
        out += ["**Aggregates بلا ملف اختبار قبول مطابق بالاسم:** "
                + ", ".join(f"`{x}`" for x in sorted(missing_acc)), ""]
    if no_evt_consumer:
        out += ["**أحداث بلا مستهلك مُعلَن:** " + ", ".join(f"`{x}`" for x in no_evt_consumer), ""]

    out += ["**حسب الـBC (محسوب من المصادر):**", "",
            "| BC | Aggregates | أوامر | أحداث | استعلامات (Derived) | تهديدات مرتبطة بمعرّف (Derived) |",
            "|---|---|---|---|---|---|"]
    for bc in sorted(BC_FILES):
        m = [a for a in all_aggs if a["bc"] == bc]
        out.append(f"| {bc} | {len(m)} | {sum(len(a['cmds']) for a in m)} | {sum(len(a['evts']) for a in m)} | "
                   f"{sum(len(a['qrys']) for a in m)} | {len(set().union(*(a['thrs'] for a in m)))} |")
    out.append("")

    out += [f"**تهديدات لا تستشهد بأي معرّف Aggregate** ({len(unlinked_thr)}): ضوابطها وصفية "
            "(مثل «assign guard: clearance ≥ label») فلا يمكن ربطها آليًا. إسنادها إلى الـBC موثَّق يدويًا في §12 "
            "من ملف كل BC. " + ", ".join(unlinked_thr), ""]

    # requirement -> aggregate reverse index
    req_aggs = defaultdict(list)
    for aid, a in aggs.items():
        for r in a["reqs"]:
            req_aggs[r].append(aid)
    no_agg = sorted(r for r in reqs if r not in req_aggs)
    out += ["### 21.2 متطلبات لا يلبيها أي Aggregate", "",
            f"{len(no_agg)} متطلبًا من {len(reqs)} لا يظهر في `traces.satisfies` لأي Aggregate. "
            "بعضها متطلبات بنية تحتية أو جودة لا نموذج مجال (مثل REQ-GOV-005)، وبعضها من إصدارات لاحقة (R2/R3).", ""]
    by_rel = defaultdict(list)
    for r in no_agg:
        by_rel[reqs[r].get("release", "?")].append(r)
    for rel in sorted(by_rel):
        out.append(f"- **{rel}** ({len(by_rel[rel])}): " + ", ".join(by_rel[rel]))
    out.append("")

    # cross-BC event consumption
    out += ["### 21.3 مستهلكو الأحداث العابرون للـBCs", "",
            "أحداث يذكر عمود «المستهلكون» فيها Bounded Context آخر غير الـBC المنتِج صراحةً (Explicit).", "",
            "| الحدث | المنتِج | المستهلكون |", "|---|---|---|"]
    for aid in sorted(aggs, key=lambda x: (aggs[x]["bc"], x)):
        a = aggs[aid]
        for e in a["evts"]:
            others = sorted(set(re.findall(r"BC0[1-8]", e["consumers"])) - {a["bc"]})
            if others:
                out.append(f"| {e['id']} | {a['bc']} · {aid} | {e['consumers']} |")
    out.append("")

    # per-BC chains
    for bc in sorted(BC_FILES):
        members = sorted(aid for aid, a in aggs.items() if a["bc"] == bc)
        out += [f"### 21.{3 + int(bc[2:])} {bc} — [{BC_FILES[bc]}]({BC_FILES[bc]})", "",
                f"{len(members)} Aggregate. التهديدات المرتبطة آليًا بـAggregates هذا الـBC: "
                f"{fmt(set().union(*(aggs[x]['thrs'] for x in members)))}. القائمة اليدوية الكاملة في §12 من ملفه.", ""]
        if unmapped_q.get(bc):
            out += [f"استعلامات في ملفات {bc} لم تُطابَق مع Aggregate بالبادئة: {fmt(unmapped_q[bc])}.", ""]
        for aid in members:
            a = aggs[aid]
            acc = acceptance_path(a)
            out += [f"#### {aid} — {a['title']}", "",
                    f"`{a['path']}` · {a['slice']} · {a['tier']} · بيانات شخصية: {'نعم' if a['personal'] else 'لا'}", "",
                    "```",
                    f"CAP  {fmt(a['caps'])}",
                    f" └ UC   {fmt(a['ucs'])}",
                    f"    └ REQ  {fmt(a['reqs'])}",
                    f"       └ {aid}",
                    f"          ├ INV  {fmt(a['invs'])}",
                    f"          ├ ADR  {fmt(a['adrs'])}",
                    f"          ├ QRY  {fmt(q['id'] for q in a['qrys'])}",
                    f"          ├ THR  {fmt(a['thrs'])}",
                    f"          └ TEST {acc or '— [Missing]'}",
                    "```", "",
                    f"**الحالات:** غير نهائية: {a['states_open'] or '—'} · نهائية: {a['states_final'] or '—'}", ""]
            if a["cmds"]:
                consumers = {e["id"]: e["consumers"] for e in a["evts"]}
                out += ["| الأمر | الفاعل | السياسة | الحدث الناتج | مستهلكو الحدث |", "|---|---|---|---|---|"]
                for c in a["cmds"]:
                    evs = c["events"] or ["—"]
                    for i, ev in enumerate(evs):
                        cons = consumers.get(ev)
                        if cons is None:
                            owner = evt_index.get(ev)
                            cons = f"(حدث يملكه {owner})" if owner else "—"
                        actor = c["actor"] if i == 0 else "″"
                        out.append(f"| {c['id'] if i == 0 else '″'} | {actor} | "
                                   f"{c['policy'] if i == 0 else '″'} | {ev} | {cons} |")
                out.append("")
            if not a["ucs"]:
                out += [f"> لا Use Case مرتبط بهذا الـAggregate عبر متطلباته. راجع §5 في "
                        f"[{BC_FILES[a['bc']]}]({BC_FILES[a['bc']]}) وCONFLICT-05 قبل اعتباره فجوة.", ""]
    out.append(END)
    return "\n".join(out) + "\n"


def main():
    data = load()
    block = render(*data)
    text = TARGET.read_text(encoding="utf-8")
    if BEGIN in text:
        text = text[: text.index(BEGIN)] + block + text[text.index(END) + len(END) + 1:]
    else:
        text = text.rstrip("\n") + "\n\n" + block
    TARGET.write_text(text, encoding="utf-8")
    aggs = data[0]
    print(f"aggregates={len(aggs)} cmds={sum(len(a['cmds']) for a in aggs.values())} "
          f"evts={sum(len(a['evts']) for a in aggs.values())} qrys={sum(len(a['qrys']) for a in aggs.values())}")


if __name__ == "__main__":
    main()
