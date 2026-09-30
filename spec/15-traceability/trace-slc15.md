---
id: TRACE-SLC15
type: traceability-matrix
title: Traceability — SLC-15 (generated)
wave: W7
slice: SLC-15
status: GENERATED
---

# Traceability — SLC-15 (generated)

## requirements

_4 items_

| requirement | design_elements | tests | status |
|---|---|---|---|
| REQ-CRD-001 | AGG-COORDINATION-CASE, QRY-CRD-GET, QRY-CRD-LIST, SPEC-FUSION | TST-COORDINATION-CASE-SM, TST-SLC15-INVARIANTS | TRACED |
| REQ-CRD-002 | AGG-COORDINATION-CASE, SPEC-FUSION | TST-COORDINATION-CASE-SM, TST-SLC15-INVARIANTS | TRACED |
| REQ-FUS-001 | AGG-CORRELATION-PROPOSAL, AGG-CORRELATION-RULE, QRY-CRP-QUEUE, SPEC-FUSION | TST-CORRELATION-PROPOSAL-SM, TST-CORRELATION-RULE-SM, TST-SLC15-INVARIANTS | TRACED |
| REQ-FUS-002 | AGG-CORRELATION-PROPOSAL, QRY-CRP-GET, SPEC-FUSION | TST-CORRELATION-PROPOSAL-SM, TST-SLC15-INVARIANTS | TRACED |

## gaps

_empty_

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
requirements:
- requirement: REQ-CRD-001
  design_elements:
  - AGG-COORDINATION-CASE
  - QRY-CRD-GET
  - QRY-CRD-LIST
  - SPEC-FUSION
  tests:
  - TST-COORDINATION-CASE-SM
  - TST-SLC15-INVARIANTS
  status: TRACED
- requirement: REQ-CRD-002
  design_elements:
  - AGG-COORDINATION-CASE
  - SPEC-FUSION
  tests:
  - TST-COORDINATION-CASE-SM
  - TST-SLC15-INVARIANTS
  status: TRACED
- requirement: REQ-FUS-001
  design_elements:
  - AGG-CORRELATION-PROPOSAL
  - AGG-CORRELATION-RULE
  - QRY-CRP-QUEUE
  - SPEC-FUSION
  tests:
  - TST-CORRELATION-PROPOSAL-SM
  - TST-CORRELATION-RULE-SM
  - TST-SLC15-INVARIANTS
  status: TRACED
- requirement: REQ-FUS-002
  design_elements:
  - AGG-CORRELATION-PROPOSAL
  - QRY-CRP-GET
  - SPEC-FUSION
  tests:
  - TST-CORRELATION-PROPOSAL-SM
  - TST-SLC15-INVARIANTS
  status: TRACED
gaps: []
```

</details>
