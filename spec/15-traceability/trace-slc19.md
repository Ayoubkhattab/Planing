---
id: TRACE-SLC19
type: traceability-matrix
title: Traceability — SLC-19 (generated)
wave: W7
slice: SLC-19
status: GENERATED
---

# Traceability — SLC-19 (generated)

## requirements

_15 items_

| requirement | design_elements | tests | status |
|---|---|---|---|
| REQ-TRX-001 | AGG-SCENARIO | TST-SCENARIO-SM | TRACED |
| REQ-TRX-002 | AGG-SCENARIO, AGG-EXERCISE | TST-SCENARIO-SM, TST-SLC19-INVARIANTS | TRACED |
| REQ-TRX-003 | AGG-EXERCISE | TST-EXERCISE-SM, TST-SLC19-INVARIANTS | TRACED |
| REQ-TRX-004 | AGG-EXERCISE | TST-EXERCISE-SM | TRACED |
| REQ-TRX-005 | AGG-EXERCISE, AGG-SIMULATION | TST-EXERCISE-SM, TST-SLC19-INVARIANTS | TRACED |
| REQ-TRX-006 | AGG-EXERCISE | TST-EXERCISE-SM, TST-SLC19-INVARIANTS | TRACED |
| REQ-TRX-007 | AGG-EXERCISE | TST-EXERCISE-SM | TRACED |
| REQ-TRX-008 | AGG-SIMULATION | TST-SIMULATION-SM | TRACED |
| REQ-TRX-009 | AGG-SIMULATION | TST-SIMULATION-SM | TRACED |
| REQ-TRX-010 | AGG-SIMULATION | TST-SIMULATION-SM, TST-SLC19-INVARIANTS | TRACED |
| REQ-TRX-011 | AGG-SIMULATION | TST-SIMULATION-SM | TRACED |
| REQ-TRX-012 | AGG-QUALIFICATION-RECORD (SLC-03, unmodified), SPEC-TRAINING-EXERCISE | TST-SLC19-INVARIANTS | TRACED |
| REQ-TRX-013 | AGG-KNOWLEDGE-OBJECT (SLC-12, CR-63), SPEC-TRAINING-EXERCISE | TST-SLC19-INVARIANTS | TRACED |
| REQ-TRX-014 | QRY-SCN-GET, QRY-SCN-LIST, QRY-EXR-GET, QRY-EXR-LIST, QRY-SIM-GET, QRY-SIM-LIST | contract lint (OpenAPI operationId presence, allowed_scope enforcement) | TRACED |
| REQ-TRX-015 | QRY-SIM-TIMELINE | contract lint (OpenAPI operationId presence) | TRACED |

## gaps

_empty_

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
requirements:
- requirement: REQ-TRX-001
  design_elements:
  - AGG-SCENARIO
  tests:
  - TST-SCENARIO-SM
  status: TRACED
- requirement: REQ-TRX-002
  design_elements:
  - AGG-SCENARIO
  - AGG-EXERCISE
  tests:
  - TST-SCENARIO-SM
  - TST-SLC19-INVARIANTS
  status: TRACED
- requirement: REQ-TRX-003
  design_elements:
  - AGG-EXERCISE
  tests:
  - TST-EXERCISE-SM
  - TST-SLC19-INVARIANTS
  status: TRACED
- requirement: REQ-TRX-004
  design_elements:
  - AGG-EXERCISE
  tests:
  - TST-EXERCISE-SM
  status: TRACED
- requirement: REQ-TRX-005
  design_elements:
  - AGG-EXERCISE
  - AGG-SIMULATION
  tests:
  - TST-EXERCISE-SM
  - TST-SLC19-INVARIANTS
  status: TRACED
- requirement: REQ-TRX-006
  design_elements:
  - AGG-EXERCISE
  tests:
  - TST-EXERCISE-SM
  - TST-SLC19-INVARIANTS
  status: TRACED
- requirement: REQ-TRX-007
  design_elements:
  - AGG-EXERCISE
  tests:
  - TST-EXERCISE-SM
  status: TRACED
- requirement: REQ-TRX-008
  design_elements:
  - AGG-SIMULATION
  tests:
  - TST-SIMULATION-SM
  status: TRACED
- requirement: REQ-TRX-009
  design_elements:
  - AGG-SIMULATION
  tests:
  - TST-SIMULATION-SM
  status: TRACED
- requirement: REQ-TRX-010
  design_elements:
  - AGG-SIMULATION
  tests:
  - TST-SIMULATION-SM
  - TST-SLC19-INVARIANTS
  status: TRACED
- requirement: REQ-TRX-011
  design_elements:
  - AGG-SIMULATION
  tests:
  - TST-SIMULATION-SM
  status: TRACED
- requirement: REQ-TRX-012
  design_elements:
  - AGG-QUALIFICATION-RECORD (SLC-03, unmodified)
  - SPEC-TRAINING-EXERCISE
  tests:
  - TST-SLC19-INVARIANTS
  status: TRACED
- requirement: REQ-TRX-013
  design_elements:
  - AGG-KNOWLEDGE-OBJECT (SLC-12, CR-63)
  - SPEC-TRAINING-EXERCISE
  tests:
  - TST-SLC19-INVARIANTS
  status: TRACED
- requirement: REQ-TRX-014
  design_elements:
  - QRY-SCN-GET
  - QRY-SCN-LIST
  - QRY-EXR-GET
  - QRY-EXR-LIST
  - QRY-SIM-GET
  - QRY-SIM-LIST
  tests:
  - contract lint (OpenAPI operationId presence, allowed_scope enforcement)
  status: TRACED
- requirement: REQ-TRX-015
  design_elements:
  - QRY-SIM-TIMELINE
  tests:
  - contract lint (OpenAPI operationId presence)
  status: TRACED
gaps: []
```

</details>
