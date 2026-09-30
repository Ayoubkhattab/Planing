---
id: TRACE-SLC17
type: traceability-matrix
title: Traceability — SLC-17 (generated)
wave: W7
slice: SLC-17
status: GENERATED
---

# Traceability — SLC-17 (generated)

## requirements

_16 items_

| requirement | design_elements | tests | status |
|---|---|---|---|
| REQ-RCM-001 | AGG-RISK, SPEC-RISK-CONTINGENCY | TST-RISK-SM, TST-SLC17-INVARIANTS | TRACED |
| REQ-RCM-002 | AGG-RISK | TST-RISK-SM, TST-SLC17-INVARIANTS | TRACED |
| REQ-RCM-003 | AGG-RISK | TST-RISK-SM, TST-SLC17-INVARIANTS | TRACED |
| REQ-RCM-004 | AGG-RISK | TST-RISK-SM, TST-SLC17-INVARIANTS | TRACED |
| REQ-RCM-005 | AGG-RISK | TST-RISK-SM, TST-SLC17-INVARIANTS | TRACED |
| REQ-RCM-006 | AGG-INCIDENT | TST-INCIDENT-SM | TRACED |
| REQ-RCM-007 | AGG-INCIDENT | TST-INCIDENT-SM | TRACED |
| REQ-RCM-008 | AGG-INCIDENT | TST-INCIDENT-SM | TRACED |
| REQ-RCM-009 | AGG-INCIDENT | TST-INCIDENT-SM, TST-SLC17-INVARIANTS | TRACED |
| REQ-RCM-010 | AGG-INCIDENT | TST-INCIDENT-SM, TST-SLC17-INVARIANTS | TRACED |
| REQ-RCM-011 | AGG-INCIDENT, SPEC-RISK-CONTINGENCY | TST-SLC17-INVARIANTS | TRACED |
| REQ-RCM-012 | AGG-RISK, AGG-INCIDENT | TST-SLC17-INVARIANTS | TRACED |
| REQ-RCM-013 | AGG-TASK, AGG-INCIDENT | TST-SLC17-INVARIANTS | TRACED |
| REQ-RCM-014 | QRY-RIS-GET, QRY-RIS-REGISTER | contract lint (OpenAPI operationId presence, allowed_scope enforcement) | TRACED |
| REQ-RCM-015 | QRY-INC-GET, QRY-INC-LIST | contract lint (OpenAPI operationId presence, allowed_scope enforcement) | TRACED |
| REQ-RCM-016 | QRY-INC-RECOVERY-STATUS, SPEC-RISK-CONTINGENCY | contract lint (OpenAPI operationId presence) | TRACED |

## gaps

_empty_

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
requirements:
- requirement: REQ-RCM-001
  design_elements:
  - AGG-RISK
  - SPEC-RISK-CONTINGENCY
  tests:
  - TST-RISK-SM
  - TST-SLC17-INVARIANTS
  status: TRACED
- requirement: REQ-RCM-002
  design_elements:
  - AGG-RISK
  tests:
  - TST-RISK-SM
  - TST-SLC17-INVARIANTS
  status: TRACED
- requirement: REQ-RCM-003
  design_elements:
  - AGG-RISK
  tests:
  - TST-RISK-SM
  - TST-SLC17-INVARIANTS
  status: TRACED
- requirement: REQ-RCM-004
  design_elements:
  - AGG-RISK
  tests:
  - TST-RISK-SM
  - TST-SLC17-INVARIANTS
  status: TRACED
- requirement: REQ-RCM-005
  design_elements:
  - AGG-RISK
  tests:
  - TST-RISK-SM
  - TST-SLC17-INVARIANTS
  status: TRACED
- requirement: REQ-RCM-006
  design_elements:
  - AGG-INCIDENT
  tests:
  - TST-INCIDENT-SM
  status: TRACED
- requirement: REQ-RCM-007
  design_elements:
  - AGG-INCIDENT
  tests:
  - TST-INCIDENT-SM
  status: TRACED
- requirement: REQ-RCM-008
  design_elements:
  - AGG-INCIDENT
  tests:
  - TST-INCIDENT-SM
  status: TRACED
- requirement: REQ-RCM-009
  design_elements:
  - AGG-INCIDENT
  tests:
  - TST-INCIDENT-SM
  - TST-SLC17-INVARIANTS
  status: TRACED
- requirement: REQ-RCM-010
  design_elements:
  - AGG-INCIDENT
  tests:
  - TST-INCIDENT-SM
  - TST-SLC17-INVARIANTS
  status: TRACED
- requirement: REQ-RCM-011
  design_elements:
  - AGG-INCIDENT
  - SPEC-RISK-CONTINGENCY
  tests:
  - TST-SLC17-INVARIANTS
  status: TRACED
- requirement: REQ-RCM-012
  design_elements:
  - AGG-RISK
  - AGG-INCIDENT
  tests:
  - TST-SLC17-INVARIANTS
  status: TRACED
- requirement: REQ-RCM-013
  design_elements:
  - AGG-TASK
  - AGG-INCIDENT
  tests:
  - TST-SLC17-INVARIANTS
  status: TRACED
- requirement: REQ-RCM-014
  design_elements:
  - QRY-RIS-GET
  - QRY-RIS-REGISTER
  tests:
  - contract lint (OpenAPI operationId presence, allowed_scope enforcement)
  status: TRACED
- requirement: REQ-RCM-015
  design_elements:
  - QRY-INC-GET
  - QRY-INC-LIST
  tests:
  - contract lint (OpenAPI operationId presence, allowed_scope enforcement)
  status: TRACED
- requirement: REQ-RCM-016
  design_elements:
  - QRY-INC-RECOVERY-STATUS
  - SPEC-RISK-CONTINGENCY
  tests:
  - contract lint (OpenAPI operationId presence)
  status: TRACED
gaps: []
```

</details>
