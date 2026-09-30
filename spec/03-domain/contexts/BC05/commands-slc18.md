---
id: CMD-CAT-BC05-SLC18
type: command-catalog
title: Commands — BC05 (SLC-18)
wave: W4
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
---


# Commands — BC05 (SLC-18)

_10 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-LGR-REQUEST | AGG-LOGISTICS-REQUEST | `POST /api/v1/readiness/logistics-requests` | لا | Logistics Officer / Planner (request, cancel) · dispatcher (dispatch) | POL-LGR-REQUEST | `item_pool!:urn quantity!:number destination!:LocalizedName needed_by!:date-time priority!:integer justification:string` | EVT-LGR-REQUESTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LOGISTICS_REQUEST_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-LGR-DISPATCH | AGG-LOGISTICS-REQUEST | `POST /api/v1/readiness/logistics-requests/{id}/actions/dispatch` | لا | Logistics Officer / Planner (request, cancel) · dispatcher (dispatch) | POL-LGR-DISPATCH | `carrier!:string ship_quantity!:number` | EVT-LGR-DISPATCHED | ALLOCATION_NOT_COMMITTED, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LOGISTICS_REQUEST_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-LGR-CANCEL | AGG-LOGISTICS-REQUEST | `POST /api/v1/readiness/logistics-requests/{id}/actions/cancel` | لا | Logistics Officer / Planner (request, cancel) · dispatcher (dispatch) | POL-LGR-CANCEL | `reason!:string` | EVT-LGR-CANCELLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LOGISTICS_REQUEST_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SHP-PLAN | AGG-SHIPMENT | `POST /api/v1/readiness/shipments` | لا | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-PLAN | `logistics_request!:urn origin_pool!:urn destination!:LocalizedName carrier!:string planned_quantity!:number` | EVT-SHP-PLANNED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SHIPMENT_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SHP-DEPART | AGG-SHIPMENT | `POST /api/v1/readiness/shipments/{id}/actions/depart` | لا | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-DEPART | `note:string` | EVT-SHP-DEPARTED | AUTHZ_DENIED, DEPARTURE_INVALID, IDEMPOTENCY_KEY_REUSED, SHIPMENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SHP-RECORD-CHECKPOINT | AGG-SHIPMENT | `POST /api/v1/readiness/shipments/{id}/actions/record-checkpoint` | لا | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-RECORD-CHECKPOINT | `location!:LocalizedName at!:date-time note:string` | EVT-SHP-CHECKPOINT-RECORDED | AUTHZ_DENIED, CHECKPOINT_INVALID, IDEMPOTENCY_KEY_REUSED, SHIPMENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SHP-DELIVER | AGG-SHIPMENT | `POST /api/v1/readiness/shipments/{id}/actions/deliver` | لا | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-DELIVER | `delivered_quantity!:number received_by!:urn note:string` | EVT-SHP-DELIVERED | AUTHZ_DENIED, DELIVERY_INVALID, IDEMPOTENCY_KEY_REUSED, SHIPMENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SHP-REPORT-DAMAGE | AGG-SHIPMENT | `POST /api/v1/readiness/shipments/{id}/actions/report-damage` | لا | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-REPORT-DAMAGE | `damaged_quantity!:number reason!:string evidence:urn` | EVT-SHP-DAMAGED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SHIPMENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SHP-REPORT-LOST | AGG-SHIPMENT | `POST /api/v1/readiness/shipments/{id}/actions/report-lost` | لا | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-REPORT-LOST | `reason!:string` | EVT-SHP-LOST | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SHIPMENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SHP-CANCEL | AGG-SHIPMENT | `POST /api/v1/readiness/shipments/{id}/actions/cancel` | لا | dispatcher / carrier operator (plan, depart, checkpoint, deliver, report damage, report lost, cancel) | POL-SHP-CANCEL | `reason!:string` | EVT-SHP-CANCELLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SHIPMENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-LGR-REQUEST
  aggregate: AGG-LOGISTICS-REQUEST
  bc: BC05
  transitions:
  - from:
    - ∅
    to: REQUESTED
    guard: item pool ACTIVE (AGG-RESOURCE-POOL, resource_type in RD-LOGISTICS-ITEM-TYPES);
      quantity > 0 in pool unit; destination; needed_by; priority 1–5; requester;
      justification; system issues a linked allocation request in the same unit of
      work (CMD-ALC-REQUEST, target = this request — CR-62)
    event: EVT-LGR-REQUESTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LOGISTICS_REQUEST_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/logistics-requests
  internal: false
  policy: POL-LGR-REQUEST
  actors: Logistics Officer / Planner (request, cancel) · dispatcher (dispatch)
  payload: item_pool!:urn quantity!:number destination!:LocalizedName needed_by!:date-time
    priority!:integer justification:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-LGR-DISPATCH
  aggregate: AGG-LOGISTICS-REQUEST
  bc: BC05
  transitions:
  - from:
    - APPROVED
    to: IN_TRANSIT
    guard: dispatcher; linked allocation still COMMITTED; creates a Shipment (AGG-SHIPMENT)
      referencing this request and the allocation; ship_quantity ≤ requested quantity
    event: EVT-LGR-DISPATCHED
  errors:
  - ALLOCATION_NOT_COMMITTED
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LOGISTICS_REQUEST_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/logistics-requests/{id}/actions/dispatch
  internal: false
  policy: POL-LGR-DISPATCH
  actors: Logistics Officer / Planner (request, cancel) · dispatcher (dispatch)
  payload: carrier!:string ship_quantity!:number
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-LGR-CANCEL
  aggregate: AGG-LOGISTICS-REQUEST
  bc: BC05
  transitions:
  - from:
    - REQUESTED
    - PENDING_APPROVAL
    - APPROVED
    to: CANCELLED
    guard: requester or logistics authority; reason; releases the linked allocation
      if COMMITTED (CMD-ALC-RELEASE), or leaves a PENDING_APPROVAL allocation to its
      own provisional-hold expiry
    event: EVT-LGR-CANCELLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LOGISTICS_REQUEST_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/logistics-requests/{id}/actions/cancel
  internal: false
  policy: POL-LGR-CANCEL
  actors: Logistics Officer / Planner (request, cancel) · dispatcher (dispatch)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SHP-PLAN
  aggregate: AGG-SHIPMENT
  bc: BC05
  transitions:
  - from:
    - ∅
    to: PLANNED
    guard: logistics_request APPROVED; origin pool with sufficient COMMITTED allocation
      quantity for the linked request; destination; carrier; planned_quantity ≤ the
      linked allocation's committed quantity
    event: EVT-SHP-PLANNED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SHIPMENT_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/shipments
  internal: false
  policy: POL-SHP-PLAN
  actors: dispatcher / carrier operator (plan, depart, checkpoint, deliver, report
    damage, report lost, cancel)
  payload: logistics_request!:urn origin_pool!:urn destination!:LocalizedName carrier!:string
    planned_quantity!:number
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-SHP-DEPART
  aggregate: AGG-SHIPMENT
  bc: BC05
  transitions:
  - from:
    - PLANNED
    to: IN_TRANSIT
    guard: carrier confirmed; departure checkpoint recorded
    event: EVT-SHP-DEPARTED
  errors:
  - AUTHZ_DENIED
  - DEPARTURE_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - SHIPMENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/shipments/{id}/actions/depart
  internal: false
  policy: POL-SHP-DEPART
  actors: dispatcher / carrier operator (plan, depart, checkpoint, deliver, report
    damage, report lost, cancel)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SHP-RECORD-CHECKPOINT
  aggregate: AGG-SHIPMENT
  bc: BC05
  transitions:
  - from:
    - IN_TRANSIT
    to: '='
    guard: checkpoint strictly after the previous checkpoint in time (append-only,
      gapless — mirrors INV-AST-02); location; at; note
    event: EVT-SHP-CHECKPOINT-RECORDED
  errors:
  - AUTHZ_DENIED
  - CHECKPOINT_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - SHIPMENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/shipments/{id}/actions/record-checkpoint
  internal: false
  policy: POL-SHP-RECORD-CHECKPOINT
  actors: dispatcher / carrier operator (plan, depart, checkpoint, deliver, report
    damage, report lost, cancel)
  payload: location!:LocalizedName at!:date-time note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SHP-DELIVER
  aggregate: AGG-SHIPMENT
  bc: BC05
  transitions:
  - from:
    - IN_TRANSIT
    to: DELIVERED
    guard: receiving party confirms; delivered_quantity ≤ planned quantity; a shortfall
      is recorded, never hidden (INV-SHP-02)
    event: EVT-SHP-DELIVERED
  errors:
  - AUTHZ_DENIED
  - DELIVERY_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - SHIPMENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/shipments/{id}/actions/deliver
  internal: false
  policy: POL-SHP-DELIVER
  actors: dispatcher / carrier operator (plan, depart, checkpoint, deliver, report
    damage, report lost, cancel)
  payload: delivered_quantity!:number received_by!:urn note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SHP-REPORT-DAMAGE
  aggregate: AGG-SHIPMENT
  bc: BC05
  transitions:
  - from:
    - IN_TRANSIT
    to: DAMAGED
    guard: reason; damaged_quantity ≤ planned quantity; evidence
    event: EVT-SHP-DAMAGED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SHIPMENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/shipments/{id}/actions/report-damage
  internal: false
  policy: POL-SHP-REPORT-DAMAGE
  actors: dispatcher / carrier operator (plan, depart, checkpoint, deliver, report
    damage, report lost, cancel)
  payload: damaged_quantity!:number reason!:string evidence:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SHP-REPORT-LOST
  aggregate: AGG-SHIPMENT
  bc: BC05
  transitions:
  - from:
    - IN_TRANSIT
    to: LOST
    guard: reason
    event: EVT-SHP-LOST
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SHIPMENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/shipments/{id}/actions/report-lost
  internal: false
  policy: POL-SHP-REPORT-LOST
  actors: dispatcher / carrier operator (plan, depart, checkpoint, deliver, report
    damage, report lost, cancel)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SHP-CANCEL
  aggregate: AGG-SHIPMENT
  bc: BC05
  transitions:
  - from:
    - PLANNED
    to: CANCELLED
    guard: reason; only before departure
    event: EVT-SHP-CANCELLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SHIPMENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/shipments/{id}/actions/cancel
  internal: false
  policy: POL-SHP-CANCEL
  actors: dispatcher / carrier operator (plan, depart, checkpoint, deliver, report
    damage, report lost, cancel)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
