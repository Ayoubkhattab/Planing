#!/usr/bin/env python3
"""Mechanical verification of the spec against itself; writes 06-verification.md.

Run from anywhere: python3 spec/17-system-study/_build/verify_study.py
Checks:
  V1 acceptance state-machine specs vs aggregate state x command matrices
  V2 command/query catalogs vs OpenAPI contracts (both directions)
  V3 event catalogs vs AsyncAPI contracts (both directions)
  V4 command error lists vs error catalogs, and guard errors vs command error lists
  V5 embedded spec tooling regenerates every generated file byte-for-byte (round trip)
  V6 every front-matter and embedded YAML block in spec/ parses
  V7 every command names exactly one policy, and that policy is defined in 08-security/policies-*.md (SL-02)
  V8 18-analysis-design: generated sections are current, every spec element is covered exactly once, links resolve
  V9 story and feature files: mapping, structure, Arabic Gherkin, no technical codes in story text, glossary messages, sources
"""
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

import yaml

SPEC = Path(__file__).resolve().parents[2]
CTX = SPEC / "03-domain" / "contexts"
ACC = SPEC / "13-verification" / "acceptance"
CONTRACTS = SPEC / "05-contracts"
OUT = SPEC / "17-system-study" / "06-verification.md"
AD = SPEC / "18-analysis-design"


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def tables(text):
    """Yields (header, rows) for every markdown table; rows are lists of cells."""
    header, rows = None, []
    for line in text.splitlines() + [""]:
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s.strip("|"))]
            if header is None:
                header = cells
            elif not set(s.replace("|", "").strip()) <= set("-: "):
                rows.append(cells)
            continue
        if header is not None:
            yield header, rows
        header, rows = None, []


def yaml_block(text):
    m = re.search(r"```yaml\n(.*?)```", text, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def split_states(value):
    value = value.replace("∅ (إنشاء)", "∅")
    return [s.strip() for s in value.split(",") if s.strip()]


# ---------------------------------------------------------------- aggregates
def load_aggregates():
    aggs = {}
    for path in sorted(CTX.glob("BC*/aggregates/AGG-*.md")):
        text = path.read_text(encoding="utf-8")
        fm = front_matter(text)
        a = {"id": fm["id"], "bc": fm.get("bounded_context"), "path": path.relative_to(SPEC).as_posix(),
             "sm": (fm.get("traces") or {}).get("state_machine", ""),
             "reqs": set((fm.get("traces") or {}).get("satisfies") or []),
             "allowed": {}, "create": {}, "rejected": {}, "sys": [], "trans": {}, "guard_errors": defaultdict(set)}
        for header, rows in tables(text):
            if header[:3] == ["من", "الأمر", "إلى"]:
                for r in rows:
                    for frm in split_states(r[0]):
                        a["trans"][(frm, r[1])] = (r[2], r[4])
                    if r[5] not in ("—", "-", ""):
                        for code in re.findall(r"[A-Z][A-Z0-9_]{2,}", r[5]):
                            a["guard_errors"][r[1]].add(code)
            elif header and header[0].startswith("الحالة"):
                cmds = header[1:]
                for r in rows:
                    state = r[0]
                    for cmd, cell in zip(cmds, r[1:]):
                        if not cmd.startswith("CMD-"):
                            if cell.startswith("→"):
                                a["sys"].append((state, cmd, cell[1:].strip()))
                            continue
                        if cell.startswith("→"):
                            to = cell[1:].strip()
                            event = a["trans"].get((state, cmd), (None, None))[1]
                            (a["create"] if state == "∅" else a["allowed"])[
                                (cmd,) if state == "∅" else (state, cmd)] = (to, event)
                        elif cell.startswith("✗"):
                            a["rejected"][(state, cmd)] = cell[1:].strip()
        aggs[a["id"]] = a
    return aggs


def load_acceptance():
    specs = {}
    for path in sorted(ACC.glob("*/*-state-machine.md")):
        text = path.read_text(encoding="utf-8")
        fm = front_matter(text)
        s = {"path": path.relative_to(SPEC).as_posix(), "from": fm.get("generated_from"),
             "verifies": set((fm.get("traces") or {}).get("verifies") or []),
             "allowed": {}, "create": {}, "rejected": {}, "sys": [], "text": text}
        for header, rows in tables(text):
            h = [c.lower() for c in header]
            if h[:5] == ["aggregate", "from", "command", "to", "event"]:
                for r in rows:
                    target = s["sys"] if not r[2].startswith("CMD-") else None
                    if target is not None:
                        target.append((r[1], r[2], r[3]))
                    else:
                        s["allowed"][(r[1], r[2])] = (r[3], r[4])
            elif h[:5] == ["aggregate", "from", "trigger", "to", "event"]:
                for r in rows:
                    s["sys"].append((r[1], "SYS:" + r[2], r[3]))
            elif h[:4] == ["aggregate", "command", "to", "event"]:
                for r in rows:
                    s["create"][(r[1],)] = (r[2], r[3])
            elif h[:4] == ["aggregate", "state", "command", "error"]:
                for r in rows:
                    s["rejected"][(r[1], r[2])] = r[3]
        specs[path.stem.replace("-state-machine", "")] = s
    return specs


def v1(aggs, specs):
    rows, issues, sys_gap = [], [], []
    for aid in sorted(aggs):
        a = aggs[aid]
        key = a["sm"].replace("SM-", "").lower()
        s = specs.get(key)
        if not s:
            issues.append(f"`{aid}`: لا ملف قبول مطابق لـ`{a['sm']}`")
            rows.append((aid, a["bc"], "—", "✗ مفقود"))
            continue
        problems = []
        if s["from"] != aid:
            problems.append(f"generated_from = {s['from']}")
        for label, exp, got in (("انتقال مسموح", a["allowed"], s["allowed"]),
                                ("إنشاء", a["create"], s["create"]),
                                ("رفض", a["rejected"], s["rejected"])):
            missing = sorted(set(exp) - set(got))
            extra = sorted(set(got) - set(exp))
            wrong = sorted(k for k in set(exp) & set(got) if exp[k] != got[k]
                           and not (label != "رفض" and exp[k][1] is None and exp[k][0] == got[k][0]))
            if missing:
                problems.append(f"{label} ناقص في القبول: " + "; ".join(" / ".join(k) for k in missing[:4])
                                + (" …" if len(missing) > 4 else ""))
            if extra:
                problems.append(f"{label} زائد في القبول: " + "; ".join(" / ".join(k) for k in extra[:4]))
            for k in wrong[:4]:
                problems.append(f"{label} مختلف عند {' / '.join(k)}: المصفوفة {exp[k]} ≠ القبول {got[k]}")
        miss_req = sorted(a["reqs"] - s["verifies"])
        if miss_req:
            problems.append("متطلبات لا يذكرها `traces.verifies`: " + ", ".join(miss_req))
        if a["sys"]:
            covered = {(f, t) for f, _, t in s["sys"]}
            unc = [x for x in a["sys"] if (x[0], x[2]) not in covered
                   and not re.search(rf"Then \S+ becomes {re.escape(x[2])}\b", s["text"])]
            if unc:
                sys_gap.append((aid, a["bc"], unc, s["path"]))
        counts = f"{len(a['allowed'])}+{len(a['create'])} / {len(a['rejected'])}"
        rows.append((aid, a["bc"], counts, "✅" if not problems else "✗ " + " · ".join(problems)))
        if problems:
            issues.append(f"`{aid}` ({s['path']}): " + " · ".join(problems))
    return rows, issues, sys_gap


# ---------------------------------------------------------------- contracts
def load_catalog(kind, prefix, first_col):
    items = {}
    for path in sorted(CTX.glob(f"BC*/{kind}-*.md")):
        for header, rows in tables(path.read_text(encoding="utf-8")):
            if not header or header[0] != first_col:
                continue
            for r in rows:
                if r[0].startswith(prefix) and len(r) == len(header):
                    d = dict(zip(header, r))
                    d["_file"] = path.relative_to(SPEC).as_posix()
                    items[r[0]] = d
    return items


def load_openapi():
    ops = {}
    for path in sorted(CONTRACTS.glob("openapi-*.md")):
        doc = yaml_block(path.read_text(encoding="utf-8"))
        for p, methods in (doc.get("paths") or {}).items():
            for method, op in methods.items():
                if isinstance(op, dict) and op.get("operationId"):
                    ops.setdefault(op["operationId"], []).append((method.upper(), p, path.name))
    return ops


def load_asyncapi():
    msgs = defaultdict(list)
    for path in sorted(CONTRACTS.glob("asyncapi-*.md")):
        doc = yaml_block(path.read_text(encoding="utf-8"))
        for name in ((doc.get("components") or {}).get("messages") or {}):
            msgs[name].append(path.name)
    return msgs


def load_errors():
    """Returns {slice_suffix: {code: (count, listed_cmds, truncated)}}; long lists end with '…' by design."""
    out = defaultdict(dict)
    for path in sorted(CONTRACTS.glob("errors-*.md")):
        sfx = path.stem.replace("errors-", "")
        for header, rows in tables(path.read_text(encoding="utf-8")):
            if header and header[0] == "الرمز":
                for r in rows:
                    listed = set(re.findall(r"CMD-[A-Z0-9-]+(?=,|$)", r[-1].replace(" ", "")))
                    out[sfx][r[0].strip("`")] = (int(r[3]) if r[3].isdigit() else None, listed, r[-1].endswith("…"))
    return out


def v2(cmds, qrys, ops):
    issues = []
    for cid, c in sorted(cmds.items()):
        http = c["HTTP"].strip("`").split(" ", 1)
        found = ops.get(cid)
        if not found:
            issues.append(("CMD", cid, f"لا عملية OpenAPI بـoperationId = {cid} (داخلي: {c['داخلي']}، `{c['_file']}`)"))
        elif len(http) == 2 and not any(m == http[0] and p == http[1] for m, p, _ in found):
            issues.append(("CMD", cid, f"المسار مختلف: الكتالوج `{' '.join(http)}` ≠ العقد " +
                           ", ".join(f"`{m} {p}` ({f})" for m, p, f in found)))
    for qid, q in sorted(qrys.items()):
        http = q["HTTP"].strip("`").split(" ", 1)
        found = ops.get(qid)
        if not found:
            issues.append(("QRY", qid, f"لا عملية OpenAPI بـoperationId = {qid} (`{q['_file']}`)"))
        elif len(http) == 2 and not any(m == http[0] and p == http[1] for m, p, _ in found):
            issues.append(("QRY", qid, f"المسار مختلف: الكتالوج `{' '.join(http)}` ≠ العقد " +
                           ", ".join(f"`{m} {p}` ({f})" for m, p, f in found)))
    orphans = sorted(o for o in ops if re.match(r"(CMD|QRY)-", o) and o not in cmds and o not in qrys)
    dup = sorted(o for o, v in ops.items() if len(v) > 1)
    return issues, orphans, dup


def v3(evts, msgs):
    missing = sorted(e for e in evts if e not in msgs)
    orphans = sorted(m for m in msgs if m.startswith("EVT-") and m not in evts)
    return missing, orphans


def v4(cmds, codes, aggs):
    not_in_catalog, guard_missing = [], []
    creators = {k[0] for a in aggs.values() for k in a["create"]}
    expected = defaultdict(lambda: defaultdict(set))
    for cid, c in cmds.items():
        sfx = re.search(r"-(slc[0-9a-z]+)\.md$", c["_file"]).group(1)
        for code in (e.strip() for e in c["الأخطاء"].split(",")):
            if code and code != "—":
                expected[sfx][code].add(cid)
    for sfx in sorted(expected):
        for code, want in sorted(expected[sfx].items()):
            count, listed, truncated = codes.get(sfx, {}).get(code, (0, set(), False))
            if count != len(want):
                not_in_catalog.append((sfx, code, f"العدد في الكتالوج {count} ≠ {len(want)} أمرًا يذكره"))
            missing = sorted(want - listed) if not truncated else sorted(listed - want)
            if missing and not truncated:
                not_in_catalog.append((sfx, code, "غير مذكور: " + ", ".join(missing)))
            elif missing:
                not_in_catalog.append((sfx, code, "مذكور في الكتالوج دون أن يذكره الأمر: " + ", ".join(missing)))
    for aid, a in sorted(aggs.items()):
        for cid, gcodes in a["guard_errors"].items():
            if cid not in cmds:
                continue
            listed = {e.strip() for e in cmds[cid]["الأخطاء"].split(",")}
            for code in sorted(gcodes - listed):
                guard_missing.append((aid, cid, code))
    return not_in_catalog, guard_missing, creators


def v5():
    """Extracts the embedded tooling, regenerates every slice in a temp dir, diffs against the spec."""
    try:
        import openapi_spec_validator  # noqa: F401  (required by slice_contracts.py)
    except ImportError:
        return None, "openapi-spec-validator غير مثبَّت — تخطّي V5 (pip install openapi-spec-validator)"
    tooling = SPEC / "13-verification" / "tooling"
    tmp = Path(tempfile.mkdtemp(prefix="spec-roundtrip-"))
    try:
        for name in ("spec-tooling.md", "slice-sources.md"):
            text = (tooling / name).read_text(encoding="utf-8")
            for mod, code in re.findall(r"^## (\S+\.py)\s*\n.*?^```python\n(.*?)^```[ \t]*$", text, re.S | re.M):
                (tmp / mod).write_text(code, encoding="utf-8")
        (tmp / "work" / "05-contracts").mkdir(parents=True)
        failures = []
        for data in sorted(tmp.glob("slc*_data.py")):
            for gen in ("slice_gen", "slice_contracts", "acc_gen"):
                r = subprocess.run([sys.executable, f"{gen}.py", data.stem], cwd=tmp, capture_output=True, text=True)
                if r.returncode:
                    failures.append(f"{gen} {data.stem}: {r.stderr.strip().splitlines()[-1]}")
        work = tmp / "work"
        diffs, new = [], []
        for f in sorted(work.rglob("*.md")):
            rel = f.relative_to(work).as_posix()
            target = SPEC / rel
            if not target.exists():
                new.append(rel)
            elif f.read_bytes() != target.read_bytes():
                diffs.append(rel)
        return {"generated": len(list(work.rglob("*.md"))), "diffs": diffs, "new": new, "failures": failures}, None
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def v7(cmds):
    defined = set()
    for path in sorted((SPEC / "08-security").glob("policies-*.md")):
        text = path.read_text(encoding="utf-8")
        defined |= set(re.findall(r"^### (POL-[A-Z0-9-]+)", text, re.M))
        defined |= set(re.findall(r"^\| (POL-[A-Z0-9-]+) \|", text, re.M))
    missing, multi, used = [], [], defaultdict(list)
    for cid, c in sorted(cmds.items()):
        pols = re.findall(r"POL-[A-Z0-9-]+", c["السياسة"])
        if len(pols) != 1:
            multi.append((cid, c["السياسة"]))
        for pol in pols:
            used[pol].append(cid)
            if pol not in defined:
                missing.append((cid, pol))
    shared = sorted((p, v) for p, v in used.items() if len(v) > 1)
    return len(defined), missing, multi, shared


def v6():
    bad, n = [], 0
    for path in sorted(SPEC.rglob("*.md")):
        if "17-system-study" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        fm = re.match(r"---\n(.*?)\n---", text, re.S)
        blocks = ([("front-matter", fm.group(1))] if fm else []) + \
                 [("yaml", b) for b in re.findall(r"^```yaml\n(.*?)^```", text, re.S | re.M)]
        for kind, b in blocks:
            n += 1
            try:
                yaml.safe_load(b)
            except yaml.YAMLError as e:
                bad.append((path.relative_to(SPEC).as_posix(), kind, str(e).splitlines()[0]))
    return n, bad

def v8(sys_trans):
    """Analysis-design coverage. Freshness re-runs the generator and restores the files it changed."""
    sys.path.insert(0, str(Path(__file__).parent))
    import build_analysis_design as bad
    aggs, ops = bad.load_aggregates(), bad.load_openapi()
    cmds, qrys = bad.load_catalog("commands", "الأمر"), bad.load_catalog("queries", "الاستعلام")
    evts = bad.load_catalog("events", "الحدث")
    files = sorted(AD.rglob("*.md"))
    before = {f: f.read_text(encoding="utf-8") for f in files}
    r = subprocess.run([sys.executable, str(Path(__file__).parent / "build_analysis_design.py")], capture_output=True, text=True)
    stale = [f.relative_to(SPEC).as_posix() for f in files if f.read_text(encoding="utf-8") != before[f]]
    stale += [f.relative_to(SPEC).as_posix() for f in sorted(AD.rglob("*.md")) if f not in before]
    for f, text in before.items():
        f.write_text(text, encoding="utf-8")
    if r.returncode:
        stale.append("generator failed: " + (r.stderr.strip().splitlines() or ["?"])[-1])
    us = "\n".join(p.read_text(encoding="utf-8") for p in sorted((AD / "05-user-stories").glob("us-bc*.md")))
    heads = re.findall(r"^#### (US-BC0\d-[A-Z0-9-]+)", us, re.M)
    gaps = []
    counts = defaultdict(int)
    for h in heads:
        counts[h] += 1
    for cid, c in cmds.items():
        n = counts.get(f"US-{c['_bc']}-{cid[4:]}", 0)
        if n != 1:
            gaps.append(("05", cid, f"{n} قصة"))
    for qid, q in qrys.items():
        n = counts.get(f"US-{q['_bc']}-Q-{qid[4:]}", 0)
        if n != 1:
            gaps.append(("05", qid, f"{n} قصة"))
    sys_stories = sum(1 for h in heads if "-S-" in h)
    sys_rules = sum(1 for a in aggs.values() for t in a["trans"] if t["cmd"].startswith("SYS:"))
    if sys_stories != sys_rules:
        gaps.append(("05", "SYS:", f"{sys_stories} قصة لـ{sys_rules} قاعدة"))
    dup = [h for h, n in counts.items() if n > 1]
    docs = {n: (AD / n).read_text(encoding="utf-8") for n in
            ("08-state-models.md", "09-business-rules.md", "14-api-design.md", "15-event-design.md")}
    for aid in aggs:
        if not re.search(rf"^### {aid}$", docs["08-state-models.md"], re.M):
            gaps.append(("08", aid, "لا مخطط"))
        if not re.search(rf"^#### {aid} — ", docs["09-business-rules.md"], re.M):
            gaps.append(("09", aid, "لا قسم"))
    for inv in sorted({i for a in aggs.values() for i in a["invs"]}):
        if f"**{inv}**" not in docs["09-business-rules.md"]:
            gaps.append(("09", inv, "ثابت غير مذكور"))
    for oid in ops:
        if f"| {oid} |" not in docs["14-api-design.md"]:
            gaps.append(("14", oid, "عملية غير مذكورة"))
    for eid in evts:
        if f"| {eid} |" not in docs["15-event-design.md"]:
            gaps.append(("15", eid, "حدث غير مذكور"))
    reqs, ucs = bad.load_requirements()
    qas = bad.md_records((SPEC / "02-requirements" / "quality-scenarios.md").read_text(encoding="utf-8"), "QAS")
    p3 = {n: (AD / n).read_text(encoding="utf-8") if (AD / n).exists() else "" for n in
          ("02-actors-roles.md", "03-requirements-analysis.md", "04-use-cases.md", "07-domain-model.md")}
    for uid in ucs:
        if not re.search(rf"^##### {uid} — ", p3["04-use-cases.md"], re.M):
            gaps.append(("04", uid, "حالة استخدام غير مذكورة"))
    for rid in reqs:
        if f"| {rid} |" not in p3["03-requirements-analysis.md"]:
            gaps.append(("03", rid, "متطلب غير مذكور"))
    for qid in qas:
        if f"| {qid} |" not in p3["03-requirements-analysis.md"]:
            gaps.append(("03", qid, "سيناريو جودة غير مذكور"))
    for aid in aggs:
        if f"| {aid} |" not in p3["07-domain-model.md"]:
            gaps.append(("07", aid, "Aggregate غير مذكور"))
    sec = (AD / "17-security-design.md").read_text(encoding="utf-8") if (AD / "17-security-design.md").exists() else ""
    for qid in qrys:
        if f"| `{qid}` |" not in sec:
            gaps.append(("17", qid, "سياسة استعلام غير مذكورة"))
    for cid in bad.ACTOR_RESOLUTION:
        if f"| `{cid}` |" not in sec:
            gaps.append(("17", cid, "حسم فاعل غير مذكور"))
    for f in sorted((SPEC / "08-security").glob("threat-model*.md")):
        for tid in re.findall(r"^\| (THR-[A-Z0-9-]+) \|", f.read_text(encoding="utf-8"), re.M):
            if f"| {tid} |" not in sec:
                gaps.append(("17", tid, "تهديد غير مذكور"))
    err = (AD / "18-error-handling.md").read_text(encoding="utf-8") if (AD / "18-error-handling.md").exists() else ""
    for f in sorted(CONTRACTS.glob("errors-*.md")):
        for code in re.findall(r"^\| `([A-Z0-9_]+)` \|", f.read_text(encoding="utf-8"), re.M):
            if f"| `{code}` |" not in err:
                gaps.append(("18", code, "رمز خطأ غير مذكور"))
    comp = (AD / "12-components.md").read_text(encoding="utf-8") if (AD / "12-components.md").exists() else ""
    for aid in aggs:
        if f"| `{aid}` |" not in comp:
            gaps.append(("12", aid, "Aggregate بلا وحدة نشر"))
    trace = (AD / "25-traceability-matrix.md").read_text(encoding="utf-8") if (AD / "25-traceability-matrix.md").exists() else ""
    reqs_all = re.findall(r"^### (REQ-[A-Z0-9-]+)", (SPEC / "02-requirements" / "requirements.md").read_text(encoding="utf-8"), re.M)
    for rid in reqs_all:
        if f"| {rid} |" not in trace:
            gaps.append(("25", rid, "متطلب خارج مصفوفة التتبع"))
    road = (AD / "26-implementation-roadmap.md").read_text(encoding="utf-8") if (AD / "26-implementation-roadmap.md").exists() else ""
    for aid in aggs:
        if f"| `{aid}` |" not in trace:
            gaps.append(("25", aid, "Aggregate خارج مصفوفة التتبع"))
        if f"| `{aid}` |" not in road:
            gaps.append(("26", aid, "Aggregate خارج الـBacklog"))
    actor_lists = p3["02-actors-roles.md"].split("### 6.4")[-1]
    for oid in list(cmds) + list(qrys):
        if f"`{oid}`" not in actor_lists:
            gaps.append(("02", oid, "عملية بلا فاعل"))
    broken = []
    for f in files:
        for target in re.findall(r"\]\((?!https?:|#)([^)#\s]+)", before[f]):
            if not (f.parent / target).resolve().exists():
                broken.append((f.relative_to(SPEC).as_posix(), target))
    return {"stale": stale, "gaps": gaps, "dup": dup, "stories": len(heads), "sys_stories": sys_stories,
            "sys_trans": sys_trans, "broken": broken, "files": len(files), "cmds": len(cmds), "qrys": len(qrys),
            "ops": len(ops), "evts": len(evts), "aggs": len(aggs), "invs": sum(len(a["invs"]) for a in aggs.values())}


def v9():
    """Story and feature files (05-user-stories/00-standard.md §14): mapping, structure, Gherkin, codes, messages, sources."""
    sys.path.insert(0, str(Path(__file__).parent))
    import build_analysis_design as bad
    us = AD / "05-user-stories"
    feats, fmap = bad.load_features()
    reqs, ucs = bad.load_requirements()
    cat, _ = bad.load_ref_catalog(reqs, ucs)
    gloss = {}
    for line in (us / "00-glossary.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| `([A-Z0-9_]+)` \|", line)
        if m:
            gloss[m.group(1)] = line.strip().strip("|").split("|")[-1].strip()
    catalog = set(re.findall(r"^\| `([A-Z0-9_]+)` \| \d{3}", (AD / "18-error-handling.md").read_text(encoding="utf-8"), re.M))
    issues = [("00-glossary.md", c, "رمز خطأ بلا رسالة") for c in sorted(catalog - set(gloss))]
    try:
        from gherkin.parser import Parser
    except ImportError:
        Parser = None
        issues.append(("—", "gherkin", "حزمة gherkin-official غير مثبتة: فحص Gherkin لم يُشغَّل"))
    members = defaultdict(set)
    for sid, row in fmap.items():
        members[row["feature_id"]].add(sid)
        if sid not in bad.STORY_INFO and not sid.startswith("US-BC"):
            for ref in re.findall(r"\b(?:REQ|UC|QAS|SCR|TD|FIT|ADR)-[A-Z0-9-]*\d", row["source"]):
                if ref not in cat:
                    issues.append(("feature_map.csv", sid, f"مصدر غير موجود: {ref}"))
    seen, files, written, total = defaultdict(list), 0, 0, 0
    kinds = set(bad.KIND_ORDER)
    for f in sorted(us.glob("CAP-*/FEAT-*.md")):
        files += 1
        rel = f.relative_to(us).as_posix()
        text = f.read_text(encoding="utf-8")
        fid = f.stem
        if fid not in feats:
            issues.append((rel, fid, "ملف لميزة غير موجودة في features.csv"))
            continue
        if text.count("\n") > 900:
            issues.append((rel, fid, f"{text.count(chr(10))} سطرًا (الحد 900)"))
        if Parser:
            for g in re.findall(r"```gherkin\n(.*?)```", text, re.S):
                try:
                    if Parser().parse(g)["feature"]["language"] != "ar":
                        issues.append((rel, fid, "كتلة Gherkin ليست بالعربية"))
                except Exception as e:  # noqa: BLE001
                    issues.append((rel, fid, "Gherkin لا يُقرأ: " + str(e).splitlines()[-1][:120]))
        parts = re.split(r"(?m)^(?=### 5\.\d+ )", text.split("\n## 6. ")[0])
        ids = []
        for part in parts[1:]:
            m = re.match(r"### 5\.\d+ (US-[A-Za-z0-9-]+) — ", part)
            if not m:
                issues.append((rel, part[:40], "عنوان قصة بغير الصيغة «### 5.n US-… — العنوان»"))
                continue
            sid = m.group(1)
            ids.append(sid)
            seen[sid].append(rel)
            total += 1
            if bad.TODO in part:
                continue
            written += 1
            meta = re.search(r"\n\| النوع \| الإصدار \| الأولوية \| دون اتصال \| الحالة \|\n\|[-|]+\|\n\|([^\n]*)\|", part)
            cells = [c.strip() for c in meta.group(1).split("|")] if meta else []
            if len(cells) != 5:
                issues.append((rel, sid, "جدول البيانات ناقص"))
            elif cells[0].split(" (")[0] not in kinds or cells[4] not in ("مسودة", "قيد المراجعة", "معتمدة", "مستبدلة", "ملغاة"):
                issues.append((rel, sid, f"قيمة غير معتمدة في جدول البيانات: {cells[0]} / {cells[4]}"))
            if "> **كـ**" not in part:
                issues.append((rel, sid, "لا «كـ… أريد… حتى…»"))
            kind = cells[0].split(" (")[0] if cells else ""
            if "**باختصار:**" not in part and kind not in ("منصة", "تشغيل"):
                issues.append((rel, sid, "لا «باختصار»"))
            if kind in ("أمر", "نظام", "تكامل") and "#### القواعد" not in part:
                issues.append((rel, sid, "لا قسم «القواعد»"))
            if "#### معايير القبول" not in part or "```gherkin" not in part:
                issues.append((rel, sid, "لا معايير قبول بـGherkin"))
            if f"<!-- BEGIN GENERATED: refs {sid} -->" not in part:
                issues.append((rel, sid, "لا جدول مراجع مولَّد"))
            narrative = re.sub(r"<details>.*?</details>", "", part, flags=re.S)
            narrative = re.sub(r"(?m)^\s*\|.*\|\s*$", "", narrative)
            for code in sorted(set(re.findall(r"\b(?:CMD|QRY|EVT|POL|AGG)-[A-Z0-9-]+|SYS:", narrative))):
                issues.append((rel, sid, f"رمز تقني في نص القصة: {code}"))
            for g in re.findall(r"```gherkin\n(.*?)```", part, re.S):
                rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in g.splitlines() if ln.strip().startswith("|")]
                if not rows or "الرمز" not in rows[0] or "الرسالة" not in rows[0]:
                    continue
                ci, mi = rows[0].index("الرمز"), rows[0].index("الرسالة")
                for r in rows[1:]:
                    code, msg = r[ci], r[mi].strip('"')
                    if code not in gloss:
                        issues.append((rel, sid, f"رمز خطأ ليس في المسرد: {code}"))
                    elif msg != gloss[code] and not (code == "VALIDATION_FAILED" and re.search(r" (مطلوب|مطلوبة|غير صحيح|غير صحيحة)$", msg)):
                        issues.append((rel, sid, f"رسالة {code} تخالف المسرد: «{msg}»"))
        if set(ids) != members[fid]:
            for s in sorted(members[fid] - set(ids)):
                issues.append((rel, s, "قصة مربوطة بالميزة وليست في ملفها"))
            for s in sorted(set(ids) - members[fid]):
                issues.append((rel, s, "قصة في الملف وليست مربوطة بالميزة"))
    for sid, where in seen.items():
        if len(where) > 1:
            issues.append((", ".join(where), sid, "قصة في أكثر من موضع"))
    return {"issues": issues, "files": files, "features": len(feats), "stories": len(fmap), "in_files": total, "written": written}


# ---------------------------------------------------------------- report
def main():
    aggs = load_aggregates()
    specs = load_acceptance()
    cmds = load_catalog("commands", "CMD-", "الأمر")
    qrys = load_catalog("queries", "QRY-", "الاستعلام")
    evts = load_catalog("events", "EVT-", "الحدث")
    ops, msgs, codes = load_openapi(), load_asyncapi(), load_errors()

    v1_rows, v1_issues, sys_gap = v1(aggs, specs)
    v2_issues, v2_orphans, v2_dup = v2(cmds, qrys, ops)
    v3_missing, v3_orphans = v3(evts, msgs)
    v4_catalog, v4_guard, _ = v4(cmds, codes, aggs)
    rt, rt_skip = v5()
    y_n, y_bad = v6()
    p_n, p_missing, p_multi, p_shared = v7(cmds)
    ad = v8(sum(len(a["sys"]) for a in aggs.values()))
    st = v9()
    rt_known = {p for p in (rt or {}).get("diffs", []) + (rt or {}).get("new", []) if re.search(r"slc19|SLC-19|AGG-(EXERCISE|SCENARIO|SIMULATION)\.md", p)}
    rt_real = sorted(set((rt or {}).get("diffs", []) + (rt or {}).get("new", [])) - rt_known)

    L = ["---", "id: SYS-STUDY-VERIFICATION", "type: verification-report",
         'title: "Phase 3.7 — تحقق آلي من اتساق المواصفات (قبول · عقود · أحداث · أخطاء)"',
         "status: GENERATED", "generated_by: _build/verify_study.py", "---", "",
         "# تحقق آلي من اتساق المواصفات", "",
         "هذا الملف مولَّد بالكامل بواسطة `_build/verify_study.py` ولا يُحرَّر يدويًا. يغطي جولات التحقق التي "
         "بقيت [Missing verification pass] في §20 من ملفات الـBC: مطابقة كل ملف قبول لمصفوفة الـAggregate سطرًا بسطر، "
         "ومطابقة كل أمر واستعلام وحدث ورمز خطأ لعقده. كل فحص هنا **Explicit** (مقارنة جداول حرفية)؛ لا حكم دلالي.", "",
         "## 1. الملخص", "",
         "| الفحص | النطاق | النتيجة |", "|---|---|---|",
         f"| V1 ملفات القبول ↔ مصفوفات الحالات | {len(aggs)} Aggregate، {len(specs)} ملف قبول | "
         f"{sum(1 for r in v1_rows if r[3] == '✅')} مطابق، {len(v1_issues)} بفروق |",
         f"| V1b انتقالات المجدول (`SYS:`) بلا سيناريو قبول | {sum(len(a['sys']) for a in aggs.values())} انتقالًا في "
         f"{sum(1 for a in aggs.values() if a['sys'])} Aggregate | {sum(len(x[2]) for x in sys_gap)} بلا تغطية في {len(sys_gap)} Aggregate |",
         f"| V2 الأوامر والاستعلامات ↔ OpenAPI | {len(cmds)} أمرًا، {len(qrys)} استعلامًا، {len(ops)} عملية | "
         f"{len(v2_issues)} فرقًا؛ {len(v2_orphans)} عملية بلا كتالوج؛ {len(v2_dup)} operationId مكرر |",
         f"| V3 الأحداث ↔ AsyncAPI | {len(evts)} حدثًا، {len(msgs)} رسالة | "
         f"{len(v3_missing)} حدثًا بلا رسالة؛ {len(v3_orphans)} رسالة بلا كتالوج |",
         f"| V4a أخطاء الأوامر ↔ كتالوج الأخطاء | {sum(len(c['الأخطاء'].split(',')) for c in cmds.values())} زوجًا (أمر، رمز) | "
         f"{len(v4_catalog)} فرقًا |",
         f"| V4b أخطاء الشروط (Guards) ↔ أخطاء الأمر | {sum(len(v) for a in aggs.values() for v in a['guard_errors'].values())} رمزًا | "
         f"{len(v4_guard)} رمزًا لا يظهر في قائمة أخطاء الأمر |",
         (f"| V5 ذهاب وإياب أدوات المواصفة | {rt['generated']} ملفًا مولَّدًا من 19 شريحة | "
          f"{len(rt_real)} ملفًا يختلف عن مولِّده خارج SLC-19؛ SLC-19 مستثناة ({len(rt_known)} ملفًا مكتوبًا خارج الأدوات)؛ "
          f"{len(rt['failures'])} فشل تشغيل |") if rt else f"| V5 ذهاب وإياب أدوات المواصفة | — | {rt_skip} |",
         f"| V6 صلاحية كتل YAML المضمَّنة | {y_n} كتلة (front-matter + YAML) | {len(y_bad)} كتلة لا تُقرأ |",
         f"| V7 سياسة لكل أمر (SL-02) | {len(cmds)} أمرًا، {p_n} سياسة معرَّفة | {len(p_missing)} سياسة غير معرَّفة؛ "
         f"{len(p_multi)} أمرًا بغير سياسة واحدة؛ {len(p_shared)} سياسة يتشاركها أكثر من أمر |",
         f"| V8 دراسة التحليل والتصميم (`18-analysis-design/`) | {ad['files']} ملفًا، {ad['stories']} قصة | "
         f"{len(ad['stale'])} ملفًا مولَّدًا غير محدَّث؛ {len(ad['gaps'])} عنصرًا غير مغطى؛ {len(ad['dup'])} قصة مكررة؛ "
         f"{len(ad['broken'])} رابطًا مكسورًا |",
         f"| V9 ملفات الميزات والقصص (`05-user-stories/`) | {st['features']} ميزة، {st['stories']} قصة؛ {st['files']} ملف ميزة "
         f"فيه {st['in_files']} قصة، منها {st['written']} مكتوبة | {len(st['issues'])} مخالفة للمعيار |", ""]

    L += ["## 2. V1 — ملفات القبول مقابل مصفوفات الحالات", "",
          "لكل Aggregate: كل خلية `→ حالة` في مصفوفة الحالات × الأوامر يجب أن تظهر كانتقال مسموح (أو إنشاء من ∅) "
          "بنفس الحالة الهدف والحدث، وكل خلية `✗ رمز` كرفض بنفس الرمز، ولا صف زائد في ملف القبول. "
          "العمود «مسموح+إنشاء / رفض» عدد الخلايا في المصفوفة.", ""]
    if v1_issues:
        L += ["**الفروق:**", ""] + [f"- {i}" for i in v1_issues] + [""]
    L += ["| Aggregate | BC | مسموح+إنشاء / رفض | النتيجة |", "|---|---|---|---|"]
    L += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |" for r in v1_rows]
    L += ["", "### 2.1 V1b — انتقالات المجدول بلا سيناريو قبول", "",
          "مولِّد ملفات القبول في W6 يغطي أوامر الفاعلين فقط؛ الانتقالات التي يطلقها المجدول (`SYS:`، مثل انتهاء "
          "الصلاحية) لا سيناريو لها إلا حيث كُتب يدويًا (SLC-19). هذه **فجوة تغطية اختبار** لا خطأ في التصميم: "
          "الانتقالات موثَّقة في المصفوفات وتخضع لنفس الثوابت. منذ CR-72 يولِّد `acc_gen` سيناريو «system-triggered transition» "
          "لكل انتقال مجدول؛ ويُحتسَب أيضًا السيناريو السردي المكتوب يدويًا (`Then … becomes <state>`) كما في SLC-19.", "",
          "| Aggregate | BC | الانتقالات غير المغطاة |", "|---|---|---|"]
    for aid, bc, unc, _ in sys_gap:
        L.append(f"| {aid} | {bc} | " + "; ".join(f"{f} → {t} ({c})" for f, c, t in unc) + " |")
    L += ["", "## 3. V2 — الأوامر والاستعلامات مقابل OpenAPI", ""]
    if v2_issues:
        L += ["| النوع | المعرّف | الفرق |", "|---|---|---|"] + [f"| {k} | {i} | {d} |" for k, i, d in v2_issues]
    else:
        L += ["كل أمر واستعلام له عملية OpenAPI بنفس الـoperationId والطريقة والمسار."]
    known_orphans = {"QRY-LABEL-CHECK": "عقد OHS مشترك تنفّذه كل السياقات المالكة (POL-LABEL-CHECK في "
                     "`08-security/policies-slc05.md`)؛ لا كتالوج استعلام له لأنه لا يملكه BC واحد — بالتصميم"}
    L += ["", "**عمليات OpenAPI بلا أمر أو استعلام في الكتالوجات:** "
          + ("; ".join(f"{o} — {known_orphans.get(o, '[Needs Review]')}" for o in v2_orphans) or "لا شيء"), "",
          f"**operationId يظهر في أكثر من عقد:** {', '.join(v2_dup) or 'لا شيء'}", "",
          "## 4. V3 — الأحداث مقابل AsyncAPI", "",
          f"**أحداث بلا رسالة AsyncAPI:** {', '.join(v3_missing) or 'لا شيء'}", "",
          f"**رسائل AsyncAPI بلا حدث في الكتالوجات:** {', '.join(v3_orphans) or 'لا شيء'}", "",
          "## 5. V4 — رموز الأخطاء", "",
          "### 5.1 V4a — قوائم أخطاء الأوامر مقابل `errors-slcNN.md`", "",
          "لكل شريحة ورمز: عدد الأوامر في الكتالوج يساوي عدد الأوامر التي تذكر الرمز، وكل أمر مذكور بالاسم. "
          "الكتالوج يقطع القوائم الطويلة بـ«…» عمدًا، فتُقارَن عندها الأعداد والأسماء الظاهرة فقط.", ""]
    if v4_catalog:
        L += ["| الشريحة | الرمز | الفرق |", "|---|---|---|"] + [f"| {a} | {b} | {c} |" for a, b, c in v4_catalog]
    else:
        L.append("لا فروق.")
    L += ["", "### 5.2 V4b — خطأ شرط في جدول الانتقالات لا يظهر في قائمة أخطاء الأمر", ""]
    if v4_guard:
        L += ["| Aggregate | الأمر | الرمز |", "|---|---|---|"] + [f"| {a} | {c} | {e} |" for a, c, e in v4_guard]
    else:
        L.append("لا فروق.")
    L += ["", "## 6. V5 — ذهاب وإياب أدوات المواصفة", "",
          "`13-verification/tooling/spec-tooling.md` يعلن أن ملفات الـAggregates والكتالوجات والعقود وملفات القبول "
          "**مولَّدة لا تُعدَّل يدويًا**، وأن استخراج الأدوات وإعادة التوليد يعطي ملفات مطابقة حرفيًا. هذا الفحص يستخرج "
          "الأدوات من الملفين، يشغّل `slice_gen` ثم `slice_contracts` ثم `acc_gen` لكل شريحة في مجلد مؤقت، ويقارن كل ملف بايتًا ببايت.", ""]
    if rt is None:
        L.append(rt_skip)
    else:
        L += [f"- ملفات مولَّدة: {rt['generated']}",
              f"- تختلف عن مولِّدها خارج SLC-19: {', '.join(f'`{p}`' for p in rt_real) or '**لا شيء — ذهاب وإياب تام**'}",
              f"- فشل تشغيل: {'; '.join(rt['failures']) or 'لا شيء'}",
              f"- **SLC-19 مستثناة ({len(rt_known)} ملفًا):** كُتبت خارج الأدوات (ترتيب أعمدة مختلف، ملاحظات يدوية، "
              "وسيناريوهات قبول لانتقالات المجدول لا يولّدها `acc_gen`). إعادة توليدها كانت ستحذف تلك السيناريوهات، "
              "فهي دَين تقني مسجَّل لا فرق يُصحَّح آليًا."]
    L += ["", "## 7. V6 — صلاحية كتل YAML المضمَّنة", "",
          "كثير من ملفات المواصفة تعلن أن كتلة YAML في آخرها هي «المصدر المعتمد» للملف؛ كتلة لا تُقرأ آليًا تُبطل هذا الادعاء.", "",
          ("\n".join(f"- `{p}` ({k}): {e}" for p, k, e in y_bad) if y_bad else "كل الكتل تُقرأ بلا أخطاء.")]
    L += ["", "## 8. V7 — سياسة واحدة معرَّفة لكل أمر (SL-02)", "",
          (("**سياسات غير معرَّفة:** " + ", ".join(f"{c} → {p}" for c, p in p_missing)) if p_missing else "كل سياسة يسمّيها أمر معرَّفة في `08-security/policies-*.md`."),
          "", (("**أوامر بغير سياسة واحدة:** " + ", ".join(f"{c} ({p})" for c, p in p_multi)) if p_multi else "كل أمر يسمّي سياسة واحدة بالضبط."),
          "", (("**سياسات يتشاركها أكثر من أمر:** " + "; ".join(f"{p}: {', '.join(v)}" for p, v in p_shared)) if p_shared else "لا سياسة يتشاركها أمران.")]
    L += ["", "## 9. V8 — دراسة التحليل والتصميم", "",
          "يعيد تشغيل `build_analysis_design.py` ويقارن ناتجه بالملفات (ثم يعيدها كما كانت)، ويتحقق من أن كل عنصر في "
          "المواصفات يظهر مرة واحدة في موضعه: قصة لكل أمر واستعلام وقاعدة `SYS:`، مخطط وقسم قواعد لكل Aggregate، "
          "كل ثابت في قواعد العمل، كل عملية OpenAPI في تصميم الواجهات، كل حدث في تصميم الأحداث، كل حالة استخدام ومتطلب وسيناريو جودة، "
          "فاعل لكل أمر واستعلام، وكل Aggregate في النموذج المفاهيمي؛ وأن كل رابط نسبي يُحلّ. "
          "رسم مخططات Mermaid يُفحص بأداة منفصلة (mermaid-cli) لأنه يحتاج متصفحًا.", "",
          f"- التغطية: {ad['cmds']} أمرًا + {ad['qrys']} استعلامًا + {ad['sys_stories']} قاعدة `SYS:` (تغطي {ad['sys_trans']} انتقالًا) = "
          f"{ad['stories']} قصة؛ {ad['aggs']} Aggregate؛ {ad['invs']} ثابتًا؛ {ad['ops']} عملية؛ {ad['evts']} رسالة.",
          f"- ملفات مولَّدة غير محدَّثة: {', '.join(f'`{x}`' for x in ad['stale']) or 'لا شيء'}",
          f"- عناصر غير مغطاة: {'; '.join(f'{a} {b} ({c})' for a, b, c in ad['gaps']) or 'لا شيء'}",
          f"- قصص مكررة: {', '.join(ad['dup']) or 'لا شيء'}",
          f"- روابط مكسورة: {'; '.join(f'`{a}` → {b}' for a, b in ad['broken']) or 'لا شيء'}"]
    L += ["", "## 10. V9 — ملفات الميزات والقصص", "",
          "يطبّق قواعد `05-user-stories/00-standard.md` §14 آليًا: كل قصة في `feature_map.csv` في ملف ميزتها مرة واحدة، "
          "وحجم الملف، وكل كتلة Gherkin تُقرأ بالعربية، وأجزاء القصة المكتوبة حسب نوعها، ولا رمز تقني في نصها، "
          "ورسالة كل رمز خطأ في السيناريوهات مطابقة للمسرد، وكل مصدر لقصة جديدة موجود. "
          "القصة التي ما زال فيها «[للكتابة]» تُعد هيكلًا ولا تُفحص أجزاؤها.", "",
          f"- ملفات الميزات: {st['files']} من {st['features']}؛ القصص فيها {st['in_files']}، المكتوبة {st['written']}.", ""]
    L += (["| الملف | العنصر | المخالفة |", "|---|---|---|"] + [f"| `{a}` | {b} | {c} |" for a, b, c in st["issues"]]
          if st["issues"] else ["لا مخالفات."])
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"V1 issues={len(v1_issues)} sys_gap={sum(len(x[2]) for x in sys_gap)} V2={len(v2_issues)} "
          f"orphans={len(v2_orphans)} dup={len(v2_dup)} V3 missing={len(v3_missing)} orphans={len(v3_orphans)} "
          f"V4a={len(v4_catalog)} V4b={len(v4_guard)} V5={'skipped' if rt is None else len(rt_real)} V6={len(y_bad)} V7={len(p_missing)}/{len(p_multi)}/{len(p_shared)} "
          f"V8 stale={len(ad['stale'])} gaps={len(ad['gaps'])} dup={len(ad['dup'])} broken={len(ad['broken'])} "
          f"V9 issues={len(st['issues'])} written={st['written']}/{st['in_files']}")


if __name__ == "__main__":
    main()
