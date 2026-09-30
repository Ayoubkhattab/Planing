---
id: POLICIES-SLC18
type: policy-decision-tables
title: Policy Decision Tables — SLC-18
wave: W6
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
recalibrate_after_pilot: true
---

# Policy Decision Tables — SLC-18

## command_policies

_10 items_

### POL-LGR-REQUEST

- **command:** CMD-LGR-REQUEST
- **subject:** Logistics Officer / Planner
- **resource:** AGG-LOGISTICS-REQUEST
- **context_conditions:** tenant match; item_pool visible to actor
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-LGR-DISPATCH

- **command:** CMD-LGR-DISPATCH
- **subject:** dispatcher
- **resource:** AGG-LOGISTICS-REQUEST
- **context_conditions:** tenant match; linked allocation COMMITTED (INV-LGR-02)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-LGR-CANCEL

- **command:** CMD-LGR-CANCEL
- **subject:** requester · logistics authority
- **resource:** AGG-LOGISTICS-REQUEST
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SHP-PLAN

- **command:** CMD-SHP-PLAN
- **subject:** dispatcher
- **resource:** AGG-SHIPMENT
- **context_conditions:** tenant match; origin pool scope visible to actor; linked logistics request APPROVED
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SHP-DEPART

- **command:** CMD-SHP-DEPART
- **subject:** carrier operator · dispatcher
- **resource:** AGG-SHIPMENT
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SHP-RECORD-CHECKPOINT

- **command:** CMD-SHP-RECORD-CHECKPOINT
- **subject:** carrier operator · dispatcher
- **resource:** AGG-SHIPMENT
- **context_conditions:** tenant match; checkpoint strictly after the previous one (INV-SHP-01)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SHP-DELIVER

- **command:** CMD-SHP-DELIVER
- **subject:** receiving party
- **resource:** AGG-SHIPMENT
- **context_conditions:** tenant match; delivered_quantity ≤ planned quantity (INV-SHP-02)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SHP-REPORT-DAMAGE

- **command:** CMD-SHP-REPORT-DAMAGE
- **subject:** carrier operator · dispatcher
- **resource:** AGG-SHIPMENT
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SHP-REPORT-LOST

- **command:** CMD-SHP-REPORT-LOST
- **subject:** carrier operator · dispatcher
- **resource:** AGG-SHIPMENT
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SHP-CANCEL

- **command:** CMD-SHP-CANCEL
- **subject:** dispatcher
- **resource:** AGG-SHIPMENT
- **context_conditions:** tenant match; only before departure (INV-SHP-04)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

## query_policies

_5 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-LGR-GET | QRY-LGR-GET | allowed_scope; requester | DENY (not-found shape) |
| POL-LGR-LIST | QRY-LGR-LIST | allowed_scope | DENY (not-found shape) |
| POL-SHP-GET | QRY-SHP-GET | allowed_scope | DENY (not-found shape) |
| POL-SHP-LIST | QRY-SHP-LIST | allowed_scope | DENY (not-found shape) |
| POL-SHP-TRACKING | QRY-SHP-TRACKING | allowed_scope | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-LGR-REQUEST
  command: CMD-LGR-REQUEST
  subject: Logistics Officer / Planner
  resource: AGG-LOGISTICS-REQUEST
  context_conditions: tenant match; item_pool visible to actor
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-LGR-DISPATCH
  command: CMD-LGR-DISPATCH
  subject: dispatcher
  resource: AGG-LOGISTICS-REQUEST
  context_conditions: tenant match; linked allocation COMMITTED (INV-LGR-02)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-LGR-CANCEL
  command: CMD-LGR-CANCEL
  subject: requester · logistics authority
  resource: AGG-LOGISTICS-REQUEST
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SHP-PLAN
  command: CMD-SHP-PLAN
  subject: dispatcher
  resource: AGG-SHIPMENT
  context_conditions: tenant match; origin pool scope visible to actor; linked logistics request APPROVED
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SHP-DEPART
  command: CMD-SHP-DEPART
  subject: carrier operator · dispatcher
  resource: AGG-SHIPMENT
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SHP-RECORD-CHECKPOINT
  command: CMD-SHP-RECORD-CHECKPOINT
  subject: carrier operator · dispatcher
  resource: AGG-SHIPMENT
  context_conditions: tenant match; checkpoint strictly after the previous one (INV-SHP-01)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SHP-DELIVER
  command: CMD-SHP-DELIVER
  subject: receiving party
  resource: AGG-SHIPMENT
  context_conditions: tenant match; delivered_quantity ≤ planned quantity (INV-SHP-02)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SHP-REPORT-DAMAGE
  command: CMD-SHP-REPORT-DAMAGE
  subject: carrier operator · dispatcher
  resource: AGG-SHIPMENT
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SHP-REPORT-LOST
  command: CMD-SHP-REPORT-LOST
  subject: carrier operator · dispatcher
  resource: AGG-SHIPMENT
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SHP-CANCEL
  command: CMD-SHP-CANCEL
  subject: dispatcher
  resource: AGG-SHIPMENT
  context_conditions: tenant match; only before departure (INV-SHP-04)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-LGR-GET
  query: QRY-LGR-GET
  subject: allowed_scope; requester
  otherwise: DENY (not-found shape)
- id: POL-LGR-LIST
  query: QRY-LGR-LIST
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-SHP-GET
  query: QRY-SHP-GET
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-SHP-LIST
  query: QRY-SHP-LIST
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-SHP-TRACKING
  query: QRY-SHP-TRACKING
  subject: allowed_scope
  otherwise: DENY (not-found shape)
```

</details>
