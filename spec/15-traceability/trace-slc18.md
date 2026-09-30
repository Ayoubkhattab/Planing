---
id: TRACE-SLC18
type: traceability-matrix
title: Traceability — SLC-18 (generated)
wave: W7
slice: SLC-18
status: GENERATED
---

# Traceability — SLC-18 (generated)

## requirements

_14 items_

| requirement | design_elements | tests | status |
|---|---|---|---|
| REQ-LOG-001 | AGG-LOGISTICS-REQUEST, SPEC-LOGISTICS | TST-LOGISTICS-REQUEST-SM, TST-SLC18-INVARIANTS | TRACED |
| REQ-LOG-002 | AGG-LOGISTICS-REQUEST, AGG-RESOURCE-POOL, AGG-ALLOCATION, SPEC-LOGISTICS | TST-SLC18-INVARIANTS | TRACED |
| REQ-LOG-003 | AGG-LOGISTICS-REQUEST | TST-LOGISTICS-REQUEST-SM, TST-SLC18-INVARIANTS | TRACED |
| REQ-LOG-004 | AGG-LOGISTICS-REQUEST, AGG-SHIPMENT | TST-LOGISTICS-REQUEST-SM, TST-SHIPMENT-SM, TST-SLC18-INVARIANTS | TRACED |
| REQ-LOG-005 | AGG-SHIPMENT | TST-SHIPMENT-SM | TRACED |
| REQ-LOG-006 | AGG-SHIPMENT, AGG-LOGISTICS-REQUEST | TST-SHIPMENT-SM, TST-SLC18-INVARIANTS | TRACED |
| REQ-LOG-007 | AGG-SHIPMENT | TST-SHIPMENT-SM | TRACED |
| REQ-LOG-008 | AGG-ALLOCATION, AGG-SHIPMENT, AGG-LOGISTICS-REQUEST | TST-SLC18-INVARIANTS | TRACED |
| REQ-LOG-009 | AGG-LOGISTICS-REQUEST, AGG-SHIPMENT | TST-LOGISTICS-REQUEST-SM, TST-SHIPMENT-SM, TST-SLC18-INVARIANTS | TRACED |
| REQ-LOG-010 | QRY-LGR-GET, QRY-LGR-LIST | contract lint (OpenAPI operationId presence, allowed_scope enforcement) | TRACED |
| REQ-LOG-011 | QRY-SHP-GET, QRY-SHP-LIST | contract lint (OpenAPI operationId presence, allowed_scope enforcement) | TRACED |
| REQ-LOG-012 | QRY-SHP-TRACKING | contract lint (OpenAPI operationId presence) | TRACED |
| REQ-LOG-013 | AGG-LOGISTICS-REQUEST, SPEC-LOGISTICS | SPEC-LOGISTICS §1 review | TRACED |
| REQ-LOG-014 | AGG-ALLOCATION, SPEC-LOGISTICS | SPEC-LOGISTICS §2 review | TRACED |

## gaps

_empty_

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
requirements:
- requirement: REQ-LOG-001
  design_elements:
  - AGG-LOGISTICS-REQUEST
  - SPEC-LOGISTICS
  tests:
  - TST-LOGISTICS-REQUEST-SM
  - TST-SLC18-INVARIANTS
  status: TRACED
- requirement: REQ-LOG-002
  design_elements:
  - AGG-LOGISTICS-REQUEST
  - AGG-RESOURCE-POOL
  - AGG-ALLOCATION
  - SPEC-LOGISTICS
  tests:
  - TST-SLC18-INVARIANTS
  status: TRACED
- requirement: REQ-LOG-003
  design_elements:
  - AGG-LOGISTICS-REQUEST
  tests:
  - TST-LOGISTICS-REQUEST-SM
  - TST-SLC18-INVARIANTS
  status: TRACED
- requirement: REQ-LOG-004
  design_elements:
  - AGG-LOGISTICS-REQUEST
  - AGG-SHIPMENT
  tests:
  - TST-LOGISTICS-REQUEST-SM
  - TST-SHIPMENT-SM
  - TST-SLC18-INVARIANTS
  status: TRACED
- requirement: REQ-LOG-005
  design_elements:
  - AGG-SHIPMENT
  tests:
  - TST-SHIPMENT-SM
  status: TRACED
- requirement: REQ-LOG-006
  design_elements:
  - AGG-SHIPMENT
  - AGG-LOGISTICS-REQUEST
  tests:
  - TST-SHIPMENT-SM
  - TST-SLC18-INVARIANTS
  status: TRACED
- requirement: REQ-LOG-007
  design_elements:
  - AGG-SHIPMENT
  tests:
  - TST-SHIPMENT-SM
  status: TRACED
- requirement: REQ-LOG-008
  design_elements:
  - AGG-ALLOCATION
  - AGG-SHIPMENT
  - AGG-LOGISTICS-REQUEST
  tests:
  - TST-SLC18-INVARIANTS
  status: TRACED
- requirement: REQ-LOG-009
  design_elements:
  - AGG-LOGISTICS-REQUEST
  - AGG-SHIPMENT
  tests:
  - TST-LOGISTICS-REQUEST-SM
  - TST-SHIPMENT-SM
  - TST-SLC18-INVARIANTS
  status: TRACED
- requirement: REQ-LOG-010
  design_elements:
  - QRY-LGR-GET
  - QRY-LGR-LIST
  tests:
  - contract lint (OpenAPI operationId presence, allowed_scope enforcement)
  status: TRACED
- requirement: REQ-LOG-011
  design_elements:
  - QRY-SHP-GET
  - QRY-SHP-LIST
  tests:
  - contract lint (OpenAPI operationId presence, allowed_scope enforcement)
  status: TRACED
- requirement: REQ-LOG-012
  design_elements:
  - QRY-SHP-TRACKING
  tests:
  - contract lint (OpenAPI operationId presence)
  status: TRACED
- requirement: REQ-LOG-013
  design_elements:
  - AGG-LOGISTICS-REQUEST
  - SPEC-LOGISTICS
  tests:
  - SPEC-LOGISTICS §1 review
  status: TRACED
- requirement: REQ-LOG-014
  design_elements:
  - AGG-ALLOCATION
  - SPEC-LOGISTICS
  tests:
  - SPEC-LOGISTICS §2 review
  status: TRACED
gaps: []
```

</details>
