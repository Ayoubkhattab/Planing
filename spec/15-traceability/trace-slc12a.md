---
id: TRACE-SLC12A
type: traceability-matrix
title: Traceability — SLC-12a (generated)
wave: W7
slice: SLC-12a
status: GENERATED
---

# Traceability — SLC-12a (generated)

## requirements

_3 items_

| requirement | design_elements | tests | status |
|---|---|---|---|
| REQ-GOV-006 | AGG-DISPOSITION-RUN, AGG-RETENTION-SCHEDULE, QRY-DSP-GET, QRY-RTS-ACTIVE, SPEC-KEYS-DISPOSITION | TST-DISPOSITION-RUN-SM, TST-RETENTION-SCHEDULE-SM, TST-SLC12A-INVARIANTS | TRACED |
| REQ-GOV-007 | AGG-DISPOSITION-RUN, AGG-LEGAL-HOLD, QRY-LHD-CHECK, QRY-LHD-LIST, SPEC-KEYS-DISPOSITION | TST-DISPOSITION-RUN-SM, TST-LEGAL-HOLD-SM, TST-SLC12A-INVARIANTS | TRACED |
| REQ-GOV-008 | AGG-ERASURE-REQUEST, QRY-ERS-GET, SPEC-KEYS-DISPOSITION | TST-ERASURE-REQUEST-SM, TST-SLC12A-INVARIANTS | TRACED |

## gaps

_empty_

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
requirements:
- requirement: REQ-GOV-006
  design_elements:
  - AGG-DISPOSITION-RUN
  - AGG-RETENTION-SCHEDULE
  - QRY-DSP-GET
  - QRY-RTS-ACTIVE
  - SPEC-KEYS-DISPOSITION
  tests:
  - TST-DISPOSITION-RUN-SM
  - TST-RETENTION-SCHEDULE-SM
  - TST-SLC12A-INVARIANTS
  status: TRACED
- requirement: REQ-GOV-007
  design_elements:
  - AGG-DISPOSITION-RUN
  - AGG-LEGAL-HOLD
  - QRY-LHD-CHECK
  - QRY-LHD-LIST
  - SPEC-KEYS-DISPOSITION
  tests:
  - TST-DISPOSITION-RUN-SM
  - TST-LEGAL-HOLD-SM
  - TST-SLC12A-INVARIANTS
  status: TRACED
- requirement: REQ-GOV-008
  design_elements:
  - AGG-ERASURE-REQUEST
  - QRY-ERS-GET
  - SPEC-KEYS-DISPOSITION
  tests:
  - TST-ERASURE-REQUEST-SM
  - TST-SLC12A-INVARIANTS
  status: TRACED
gaps: []
```

</details>
