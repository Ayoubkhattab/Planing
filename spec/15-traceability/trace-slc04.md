---
id: TRACE-SLC04
type: traceability-matrix
title: Traceability — SLC-04 (generated)
wave: W7
slice: SLC-04
status: GENERATED
---

# Traceability — SLC-04 (generated)

## requirements

_6 items_

| requirement | design_elements | tests | status |
|---|---|---|---|
| REQ-INF-024 | AGG-CONFLICT | TST-CONFLICT-SM, TST-SLC04-INVARIANTS | TRACED |
| REQ-INF-025 | AGG-CONFLICT, QRY-CNF-GET, QRY-CNF-LIST, SPEC-CONFLICT-DETECTION | TST-CONFLICT-SM, TST-SLC04-INVARIANTS | TRACED |
| REQ-INF-032 | AGG-ER-CASE, AGG-MATCH-RULESET, QRY-ER-GET, QRY-ER-QUEUE, QRY-MRS-GET, SPEC-ER-CANDIDATES | TST-ER-CASE-SM, TST-MATCH-RULESET-SM, TST-SLC04-INVARIANTS | TRACED |
| REQ-INF-033 | AGG-ER-CASE, LIB-CLAIMS-KERNEL §7, QRY-CLUSTER-GET | TST-ER-CASE-SM, TST-SLC04-INVARIANTS | TRACED |
| REQ-INF-034 | AGG-ER-CASE | TST-ER-CASE-SM, TST-SLC04-INVARIANTS | TRACED |
| REQ-SRC-003 | AGG-MATCH-RULESET | TST-MATCH-RULESET-SM, TST-SLC04-INVARIANTS | TRACED |

## gaps

_empty_

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
requirements:
- requirement: REQ-INF-024
  design_elements:
  - AGG-CONFLICT
  tests:
  - TST-CONFLICT-SM
  - TST-SLC04-INVARIANTS
  status: TRACED
- requirement: REQ-INF-025
  design_elements:
  - AGG-CONFLICT
  - QRY-CNF-GET
  - QRY-CNF-LIST
  - SPEC-CONFLICT-DETECTION
  tests:
  - TST-CONFLICT-SM
  - TST-SLC04-INVARIANTS
  status: TRACED
- requirement: REQ-INF-032
  design_elements:
  - AGG-ER-CASE
  - AGG-MATCH-RULESET
  - QRY-ER-GET
  - QRY-ER-QUEUE
  - QRY-MRS-GET
  - SPEC-ER-CANDIDATES
  tests:
  - TST-ER-CASE-SM
  - TST-MATCH-RULESET-SM
  - TST-SLC04-INVARIANTS
  status: TRACED
- requirement: REQ-INF-033
  design_elements:
  - AGG-ER-CASE
  - LIB-CLAIMS-KERNEL §7
  - QRY-CLUSTER-GET
  tests:
  - TST-ER-CASE-SM
  - TST-SLC04-INVARIANTS
  status: TRACED
- requirement: REQ-INF-034
  design_elements:
  - AGG-ER-CASE
  tests:
  - TST-ER-CASE-SM
  - TST-SLC04-INVARIANTS
  status: TRACED
- requirement: REQ-SRC-003
  design_elements:
  - AGG-MATCH-RULESET
  tests:
  - TST-MATCH-RULESET-SM
  - TST-SLC04-INVARIANTS
  status: TRACED
gaps: []
```

</details>
