---
id: CMD-CAT-BC05-SLC09
type: command-catalog
title: Commands — BC05 (SLC-09)
wave: W4
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC05 (SLC-09)

_39 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-AST-REGISTER | AGG-ASSET | `POST /api/v1/readiness/assets` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-REGISTER | `asset_type!:string name!:LocalizedName owner_org!:urn custody_holder!:urn linked_entity:urn capabilities!:array serial:string label!:Label` | EVT-AST-REGISTERED | ASSET_INVALID, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-UPDATE-CONDITION | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/update-condition` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-UPDATE-CONDITION | `grade!:string inspector!:urn notes:string` | EVT-AST-CONDITION-UPDATED | ASSET_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CONDITION_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-MARK-UNSERVICEABLE | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/mark-unserviceable` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-MARK-UNSERVICEABLE | `reason!:string` | EVT-AST-UNSERVICEABLE | ASSET_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-START-MAINTENANCE | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/start-maintenance` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-START-MAINTENANCE | `maintenance_order!:urn` | EVT-AST-MAINTENANCE-STARTED | ASSET_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MAINTENANCE_ORDER_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-RETURN-TO-SERVICE | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/return-to-service` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-RETURN-TO-SERVICE | `maintenance_order!:urn` | EVT-AST-RETURNED-TO-SERVICE | ASSET_INVALID_STATE_TRANSITION, ASSET_NOT_SERVICEABLE, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-FAIL-MAINTENANCE | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/fail-maintenance` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-FAIL-MAINTENANCE | `maintenance_order!:urn reason!:string` | EVT-AST-UNSERVICEABLE | ASSET_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-TRANSFER-CUSTODY | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/transfer-custody` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-TRANSFER-CUSTODY | `new_holder!:urn reason!:string` | EVT-AST-CUSTODY-TRANSFERRED | ASSET_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CUSTODY_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-SET-CERTIFICATION | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/set-certification` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-SET-CERTIFICATION | `code!:string issuer!:string valid_from!:date-time valid_to!:date-time evidence:urn` | EVT-AST-CERTIFICATION-SET | ASSET_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CERTIFICATION_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-REPORT-LOST | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/report-lost` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-REPORT-LOST | `reason!:string` | EVT-AST-REPORTED-LOST | ASSET_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-RECOVER | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/recover` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-RECOVER | `note:string` | EVT-AST-RECOVERED | ASSET_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-DISPOSE | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/dispose` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-DISPOSE | `decision!:urn reason!:string` | EVT-AST-DISPOSED | ASSET_INVALID_STATE_TRANSITION, AUTHORITY_REQUIRED, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AST-RECLASSIFY | AGG-ASSET | `POST /api/v1/readiness/assets/{id}/actions/reclassify` | لا | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | POL-AST-RECLASSIFY | `label!:Label reason!:string` | EVT-AST-RECLASSIFIED | ASSET_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MNT-PLAN | AGG-MAINTENANCE-ORDER | `POST /api/v1/readiness/maintenance-orders` | لا | Resource Manager / technician | POL-MNT-PLAN | `asset!:urn kind!:enum(scheduled,corrective) window!:Interval description!:LocalizedName` | EVT-MNT-PLANNED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MAINTENANCE_OVERLAP, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MNT-RESCHEDULE | AGG-MAINTENANCE-ORDER | `POST /api/v1/readiness/maintenance-orders/{id}/actions/reschedule` | لا | Resource Manager / technician | POL-MNT-RESCHEDULE | `window!:Interval reason!:string` | EVT-MNT-RESCHEDULED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MAINTENANCE_ORDER_INVALID_STATE_TRANSITION, MAINTENANCE_OVERLAP, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MNT-START | AGG-MAINTENANCE-ORDER | `POST /api/v1/readiness/maintenance-orders/{id}/actions/start` | لا | Resource Manager / technician | POL-MNT-START | `technician!:urn` | EVT-MNT-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MAINTENANCE_ORDER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MNT-COMPLETE | AGG-MAINTENANCE-ORDER | `POST /api/v1/readiness/maintenance-orders/{id}/actions/complete` | لا | Resource Manager / technician | POL-MNT-COMPLETE | `outcome!:enum(serviceable,failed) work!:LocalizedName parts:array` | EVT-MNT-COMPLETED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MAINTENANCE_ORDER_INVALID_STATE_TRANSITION, OUTCOME_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MNT-CANCEL | AGG-MAINTENANCE-ORDER | `POST /api/v1/readiness/maintenance-orders/{id}/actions/cancel` | لا | Resource Manager / technician | POL-MNT-CANCEL | `reason!:string` | EVT-MNT-CANCELLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MAINTENANCE_ORDER_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RSV-HOLD | AGG-ASSET-RESERVATION | `POST /api/v1/readiness/asset-reservations` | لا | Planner / Resource Manager | POL-RSV-HOLD | `asset!:urn window!:Interval purpose!:string label!:Label` | EVT-RSV-HELD | ASSET_RESERVED, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RSV-CONFIRM | AGG-ASSET-RESERVATION | `POST /api/v1/readiness/asset-reservations/{id}/actions/confirm` | لا | Planner / Resource Manager | POL-RSV-CONFIRM | `link!:urn` | EVT-RSV-CONFIRMED | ASSET_RESERVATION_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LINK_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RSV-RELEASE | AGG-ASSET-RESERVATION | `POST /api/v1/readiness/asset-reservations/{id}/actions/release` | لا | Planner / Resource Manager | POL-RSV-RELEASE | `note:string` | EVT-RSV-RELEASED | ASSET_RESERVATION_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RSV-CANCEL | AGG-ASSET-RESERVATION | `POST /api/v1/readiness/asset-reservations/{id}/actions/cancel` | لا | Planner / Resource Manager | POL-RSV-CANCEL | `reason!:string` | EVT-RSV-CANCELLED | ASSET_RESERVATION_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ASG-ASSIGN | AGG-ASSET-ASSIGNMENT | `POST /api/v1/readiness/asset-assignments` | لا | Resource Manager / Planner | POL-ASG-ASSIGN | `asset!:urn task:urn unit:urn window!:Interval reservation:urn` | EVT-ASG-ASSIGNED | ASSET_NOT_AVAILABLE, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ASG-RETURN | AGG-ASSET-ASSIGNMENT | `POST /api/v1/readiness/asset-assignments/{id}/actions/return` | لا | Resource Manager / Planner | POL-ASG-RETURN | `condition_report!:object` | EVT-ASG-RETURNED | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CONDITION_REPORT_REQUIRED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ASG-CANCEL | AGG-ASSET-ASSIGNMENT | `POST /api/v1/readiness/asset-assignments/{id}/actions/cancel` | لا | Resource Manager / Planner | POL-ASG-CANCEL | `reason!:string` | EVT-ASG-CANCELLED | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RPL-CREATE | AGG-RESOURCE-POOL | `POST /api/v1/readiness/resource-pools` | لا | Resource Manager | POL-RPL-CREATE | `resource_type!:string name!:LocalizedName unit!:string org_scope!:urn capacity!:number label!:Label` | EVT-RPL-CREATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, POOL_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RPL-ADJUST-CAPACITY | AGG-RESOURCE-POOL | `POST /api/v1/readiness/resource-pools/{id}/actions/adjust-capacity` | لا | Resource Manager | POL-RPL-ADJUST-CAPACITY | `capacity!:number valid_from!:date-time reason!:string` | EVT-RPL-CAPACITY-ADJUSTED | AUTHZ_DENIED, CAPACITY_BELOW_COMMITMENTS, IDEMPOTENCY_KEY_REUSED, RESOURCE_POOL_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RPL-SUSPEND | AGG-RESOURCE-POOL | `POST /api/v1/readiness/resource-pools/{id}/actions/suspend` | لا | Resource Manager | POL-RPL-SUSPEND | `reason!:string` | EVT-RPL-SUSPENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, RESOURCE_POOL_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RPL-RESUME | AGG-RESOURCE-POOL | `POST /api/v1/readiness/resource-pools/{id}/actions/resume` | لا | Resource Manager | POL-RPL-RESUME | `—` | EVT-RPL-RESUMED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RESOURCE_POOL_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RPL-CLOSE | AGG-RESOURCE-POOL | `POST /api/v1/readiness/resource-pools/{id}/actions/close` | لا | Resource Manager | POL-RPL-CLOSE | `reason!:string` | EVT-RPL-CLOSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, POOL_HAS_COMMITMENTS, RESOURCE_POOL_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ALC-REQUEST | AGG-ALLOCATION | `POST /api/v1/readiness/allocations` | لا | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-REQUEST | `pool!:urn quantity!:number window!:Interval priority!:integer target!:urn justification:string` | EVT-ALC-REQUESTED | ALLOCATION_INVALID, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ALC-APPROVE | AGG-ALLOCATION | `POST /api/v1/readiness/allocations/{id}/actions/approve` | لا | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-APPROVE | `note:string` | EVT-ALC-COMMITTED | ALLOCATION_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CAPACITY_UNAVAILABLE, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ALC-REJECT | AGG-ALLOCATION | `POST /api/v1/readiness/allocations/{id}/actions/reject` | لا | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-REJECT | `reason!:string` | EVT-ALC-REJECTED | ALLOCATION_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ALC-RECORD-CONSUMPTION | AGG-ALLOCATION | `POST /api/v1/readiness/allocations/{id}/actions/record-consumption` | لا | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-RECORD-CONSUMPTION | `quantity!:number at!:date-time note:string` | EVT-ALC-CONSUMED | ALLOCATION_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CONSUMPTION_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ALC-PREEMPT | AGG-ALLOCATION | `POST /api/v1/readiness/allocations/{id}/actions/preempt` | لا | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-PREEMPT | `decision!:urn preempting_allocation!:urn` | EVT-ALC-PREEMPTED | ALLOCATION_INVALID_STATE_TRANSITION, AUTHORITY_REQUIRED, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ALC-RELEASE | AGG-ALLOCATION | `POST /api/v1/readiness/allocations/{id}/actions/release` | لا | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption) | POL-ALC-RELEASE | `note:string` | EVT-ALC-RELEASED | ALLOCATION_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RRQ-DEFINE | AGG-ROLE-REQUIREMENT | `POST /api/v1/readiness/role-requirements` | لا | Training Manager / Administrator | POL-RRQ-DEFINE | `role!:urn requirements!:array` | EVT-RRQ-DEFINED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ROLE_REQUIREMENT_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RRQ-EDIT | AGG-ROLE-REQUIREMENT | `POST /api/v1/readiness/role-requirements/{id}/actions/edit` | لا | Training Manager / Administrator | POL-RRQ-EDIT | `requirements!:array` | EVT-RRQ-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ROLE_REQUIREMENT_INVALID, ROLE_REQUIREMENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RRQ-ACTIVATE | AGG-ROLE-REQUIREMENT | `POST /api/v1/readiness/role-requirements/{id}/actions/activate` | لا | Training Manager / Administrator | POL-RRQ-ACTIVATE | `—` | EVT-RRQ-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ROLE_REQUIREMENT_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RRQ-RETIRE | AGG-ROLE-REQUIREMENT | `POST /api/v1/readiness/role-requirements/{id}/actions/retire` | لا | Training Manager / Administrator | POL-RRQ-RETIRE | `reason!:string` | EVT-RRQ-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, ROLE_REQUIREMENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-AST-REGISTER
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - ∅
    to: IN_SERVICE
    guard: type in RD-ASSET-TYPES; owner org; custody holder ACTIVE; linked information
      entity (entity_type asset-ref) created or referenced in BC02; capabilities;
      label
    event: EVT-AST-REGISTERED
  errors:
  - ASSET_INVALID
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/assets
  internal: false
  policy: POL-AST-REGISTER
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: asset_type!:string name!:LocalizedName owner_org!:urn custody_holder!:urn
    linked_entity:urn capabilities!:array serial:string label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-AST-UPDATE-CONDITION
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - IN_SERVICE
    - UNSERVICEABLE
    - UNDER_MAINTENANCE
    to: '='
    guard: condition grade in RD-CONDITION-GRADES; inspector; unserviceable grades
      require CMD-AST-MARK-UNSERVICEABLE
    event: EVT-AST-CONDITION-UPDATED
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CONDITION_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/update-condition
  internal: false
  policy: POL-AST-UPDATE-CONDITION
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: grade!:string inspector!:urn notes:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AST-MARK-UNSERVICEABLE
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - IN_SERVICE
    to: UNSERVICEABLE
    guard: reason; active assignments are notified; future reservations flagged
    event: EVT-AST-UNSERVICEABLE
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/mark-unserviceable
  internal: false
  policy: POL-AST-MARK-UNSERVICEABLE
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AST-START-MAINTENANCE
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - IN_SERVICE
    - UNSERVICEABLE
    to: UNDER_MAINTENANCE
    guard: maintenance order IN_PROGRESS for this asset
    event: EVT-AST-MAINTENANCE-STARTED
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MAINTENANCE_ORDER_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/start-maintenance
  internal: false
  policy: POL-AST-START-MAINTENANCE
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: maintenance_order!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AST-RETURN-TO-SERVICE
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - UNDER_MAINTENANCE
    to: IN_SERVICE
    guard: maintenance order COMPLETED; condition serviceable; required certifications
      valid
    event: EVT-AST-RETURNED-TO-SERVICE
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - ASSET_NOT_SERVICEABLE
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/return-to-service
  internal: false
  policy: POL-AST-RETURN-TO-SERVICE
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: maintenance_order!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AST-FAIL-MAINTENANCE
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - UNDER_MAINTENANCE
    to: UNSERVICEABLE
    guard: maintenance order COMPLETED with outcome failed; reason
    event: EVT-AST-UNSERVICEABLE
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/fail-maintenance
  internal: false
  policy: POL-AST-FAIL-MAINTENANCE
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: maintenance_order!:urn reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AST-TRANSFER-CUSTODY
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - IN_SERVICE
    - UNSERVICEABLE
    - UNDER_MAINTENANCE
    to: '='
    guard: actor is current holder or custodian authority; new holder ACTIVE in scope;
      gapless chain
    event: EVT-AST-CUSTODY-TRANSFERRED
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CUSTODY_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/transfer-custody
  internal: false
  policy: POL-AST-TRANSFER-CUSTODY
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: new_holder!:urn reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AST-SET-CERTIFICATION
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - IN_SERVICE
    - UNSERVICEABLE
    - UNDER_MAINTENANCE
    to: '='
    guard: certification code, issuer, valid_from/to; evidence
    event: EVT-AST-CERTIFICATION-SET
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CERTIFICATION_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/set-certification
  internal: false
  policy: POL-AST-SET-CERTIFICATION
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: code!:string issuer!:string valid_from!:date-time valid_to!:date-time evidence:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AST-REPORT-LOST
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - IN_SERVICE
    - UNSERVICEABLE
    to: LOST
    guard: reason; active assignments ended; reservations cancelled
    event: EVT-AST-REPORTED-LOST
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/report-lost
  internal: false
  policy: POL-AST-REPORT-LOST
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AST-RECOVER
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - LOST
    to: UNSERVICEABLE
    guard: found; inspection required before service
    event: EVT-AST-RECOVERED
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/recover
  internal: false
  policy: POL-AST-RECOVER
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AST-DISPOSE
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - UNSERVICEABLE
    - LOST
    to: DISPOSED
    guard: disposal authority (decision type asset-disposal); no active reservation
      or assignment; no legal hold
    event: EVT-AST-DISPOSED
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - AUTHORITY_REQUIRED
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/dispose
  internal: false
  policy: POL-AST-DISPOSE
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: decision!:urn reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AST-RECLASSIFY
  aggregate: AGG-ASSET
  bc: BC05
  transitions:
  - from:
    - IN_SERVICE
    - UNSERVICEABLE
    - UNDER_MAINTENANCE
    - LOST
    to: '='
    guard: authority per policy
    event: EVT-AST-RECLASSIFIED
  errors:
  - ASSET_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/assets/{id}/actions/reclassify
  internal: false
  policy: POL-AST-RECLASSIFY
  actors: Resource Manager (register, condition, custody, certification, lost) · disposal
    authority (dispose) · Security Officer (reclassify)
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MNT-PLAN
  aggregate: AGG-MAINTENANCE-ORDER
  bc: BC05
  transitions:
  - from:
    - ∅
    to: PLANNED
    guard: asset not DISPOSED; kind ∈ {scheduled, corrective}; window; no overlap
      with another non-terminal order of the asset
    event: EVT-MNT-PLANNED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MAINTENANCE_OVERLAP
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/maintenance-orders
  internal: false
  policy: POL-MNT-PLAN
  actors: Resource Manager / technician
  payload: asset!:urn kind!:enum(scheduled,corrective) window!:Interval description!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-MNT-RESCHEDULE
  aggregate: AGG-MAINTENANCE-ORDER
  bc: BC05
  transitions:
  - from:
    - PLANNED
    to: '='
    guard: new window without overlap; affected reservations flagged
    event: EVT-MNT-RESCHEDULED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MAINTENANCE_ORDER_INVALID_STATE_TRANSITION
  - MAINTENANCE_OVERLAP
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/maintenance-orders/{id}/actions/reschedule
  internal: false
  policy: POL-MNT-RESCHEDULE
  actors: Resource Manager / technician
  payload: window!:Interval reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MNT-START
  aggregate: AGG-MAINTENANCE-ORDER
  bc: BC05
  transitions:
  - from:
    - PLANNED
    to: IN_PROGRESS
    guard: technician; asset moves to UNDER_MAINTENANCE via its own command (policy)
    event: EVT-MNT-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MAINTENANCE_ORDER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/maintenance-orders/{id}/actions/start
  internal: false
  policy: POL-MNT-START
  actors: Resource Manager / technician
  payload: technician!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MNT-COMPLETE
  aggregate: AGG-MAINTENANCE-ORDER
  bc: BC05
  transitions:
  - from:
    - IN_PROGRESS
    to: COMPLETED
    guard: outcome ∈ {serviceable, failed}; work performed; parts consumed (optional
      allocation refs)
    event: EVT-MNT-COMPLETED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MAINTENANCE_ORDER_INVALID_STATE_TRANSITION
  - OUTCOME_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/maintenance-orders/{id}/actions/complete
  internal: false
  policy: POL-MNT-COMPLETE
  actors: Resource Manager / technician
  payload: outcome!:enum(serviceable,failed) work!:LocalizedName parts:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MNT-CANCEL
  aggregate: AGG-MAINTENANCE-ORDER
  bc: BC05
  transitions:
  - from:
    - PLANNED
    to: CANCELLED
    guard: reason
    event: EVT-MNT-CANCELLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MAINTENANCE_ORDER_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/maintenance-orders/{id}/actions/cancel
  internal: false
  policy: POL-MNT-CANCEL
  actors: Resource Manager / technician
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RSV-HOLD
  aggregate: AGG-ASSET-RESERVATION
  bc: BC05
  transitions:
  - from:
    - ∅
    to: HELD
    guard: asset available for the window (INV-AST-01); purpose; requester authorized
      in asset owner scope
    event: EVT-RSV-HELD
  errors:
  - ASSET_RESERVED
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/asset-reservations
  internal: false
  policy: POL-RSV-HOLD
  actors: Planner / Resource Manager
  payload: asset!:urn window!:Interval purpose!:string label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-RSV-CONFIRM
  aggregate: AGG-ASSET-RESERVATION
  bc: BC05
  transitions:
  - from:
    - HELD
    to: CONFIRMED
    guard: linked to a task or plan activity
    event: EVT-RSV-CONFIRMED
  errors:
  - ASSET_RESERVATION_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LINK_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/asset-reservations/{id}/actions/confirm
  internal: false
  policy: POL-RSV-CONFIRM
  actors: Planner / Resource Manager
  payload: link!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RSV-RELEASE
  aggregate: AGG-ASSET-RESERVATION
  bc: BC05
  transitions:
  - from:
    - CONFIRMED
    to: RELEASED
    guard: requester or linked task terminal
    event: EVT-RSV-RELEASED
  errors:
  - ASSET_RESERVATION_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/asset-reservations/{id}/actions/release
  internal: false
  policy: POL-RSV-RELEASE
  actors: Planner / Resource Manager
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RSV-CANCEL
  aggregate: AGG-ASSET-RESERVATION
  bc: BC05
  transitions:
  - from:
    - HELD
    - CONFIRMED
    to: CANCELLED
    guard: requester or asset owner; reason
    event: EVT-RSV-CANCELLED
  errors:
  - ASSET_RESERVATION_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/asset-reservations/{id}/actions/cancel
  internal: false
  policy: POL-RSV-CANCEL
  actors: Planner / Resource Manager
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ASG-ASSIGN
  aggregate: AGG-ASSET-ASSIGNMENT
  bc: BC05
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: asset available (or covered by the caller's CONFIRMED reservation); asset
      certifications satisfy the task type's asset requirements; custody authorization;
      assignee cleared for asset label
    event: EVT-ASG-ASSIGNED
  errors:
  - ASSET_NOT_AVAILABLE
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/asset-assignments
  internal: false
  policy: POL-ASG-ASSIGN
  actors: Resource Manager / Planner
  payload: asset!:urn task:urn unit:urn window!:Interval reservation:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ASG-RETURN
  aggregate: AGG-ASSET-ASSIGNMENT
  bc: BC05
  transitions:
  - from:
    - ACTIVE
    to: RETURNED
    guard: condition report; asset condition updated accordingly
    event: EVT-ASG-RETURNED
  errors:
  - ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CONDITION_REPORT_REQUIRED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/asset-assignments/{id}/actions/return
  internal: false
  policy: POL-ASG-RETURN
  actors: Resource Manager / Planner
  payload: condition_report!:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ASG-CANCEL
  aggregate: AGG-ASSET-ASSIGNMENT
  bc: BC05
  transitions:
  - from:
    - ACTIVE
    to: CANCELLED
    guard: assigned in error; reason
    event: EVT-ASG-CANCELLED
  errors:
  - ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/asset-assignments/{id}/actions/cancel
  internal: false
  policy: POL-ASG-CANCEL
  actors: Resource Manager / Planner
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RPL-CREATE
  aggregate: AGG-RESOURCE-POOL
  bc: BC05
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: type in RD-RESOURCE-TYPES; unit (UCUM); org scope; initial capacity; label
    event: EVT-RPL-CREATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - POOL_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/resource-pools
  internal: false
  policy: POL-RPL-CREATE
  actors: Resource Manager
  payload: resource_type!:string name!:LocalizedName unit!:string org_scope!:urn capacity!:number
    label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-RPL-ADJUST-CAPACITY
  aggregate: AGG-RESOURCE-POOL
  bc: BC05
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: '='
    guard: new capacity with valid_from; reason; a reduction below committed quantity
      requires pre-emption decisions first
    event: EVT-RPL-CAPACITY-ADJUSTED
  errors:
  - AUTHZ_DENIED
  - CAPACITY_BELOW_COMMITMENTS
  - IDEMPOTENCY_KEY_REUSED
  - RESOURCE_POOL_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/resource-pools/{id}/actions/adjust-capacity
  internal: false
  policy: POL-RPL-ADJUST-CAPACITY
  actors: Resource Manager
  payload: capacity!:number valid_from!:date-time reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RPL-SUSPEND
  aggregate: AGG-RESOURCE-POOL
  bc: BC05
  transitions:
  - from:
    - ACTIVE
    to: SUSPENDED
    guard: reason; no new allocations
    event: EVT-RPL-SUSPENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - RESOURCE_POOL_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/resource-pools/{id}/actions/suspend
  internal: false
  policy: POL-RPL-SUSPEND
  actors: Resource Manager
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RPL-RESUME
  aggregate: AGG-RESOURCE-POOL
  bc: BC05
  transitions:
  - from:
    - SUSPENDED
    to: ACTIVE
    guard: —
    event: EVT-RPL-RESUMED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RESOURCE_POOL_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/resource-pools/{id}/actions/resume
  internal: false
  policy: POL-RPL-RESUME
  actors: Resource Manager
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RPL-CLOSE
  aggregate: AGG-RESOURCE-POOL
  bc: BC05
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: CLOSED
    guard: no COMMITTED or PENDING allocations
    event: EVT-RPL-CLOSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - POOL_HAS_COMMITMENTS
  - RESOURCE_POOL_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/resource-pools/{id}/actions/close
  internal: false
  policy: POL-RPL-CLOSE
  actors: Resource Manager
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ALC-REQUEST
  aggregate: AGG-ALLOCATION
  bc: BC05
  transitions:
  - from:
    - ∅
    to: REQUESTED
    guard: pool ACTIVE; quantity > 0 in pool unit; window; priority 1–5; target task/activity/logistics-request
      (CR-62, SLC-18); requester
    event: EVT-ALC-REQUESTED
  errors:
  - ALLOCATION_INVALID
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/allocations
  internal: false
  policy: POL-ALC-REQUEST
  actors: Planner (request, release) · allocation authority (approve, reject, pre-empt)
    · task assignee (consumption)
  payload: pool!:urn quantity!:number window!:Interval priority!:integer target!:urn
    justification:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ALC-APPROVE
  aggregate: AGG-ALLOCATION
  bc: BC05
  transitions:
  - from:
    - PENDING_APPROVAL
    to: COMMITTED
    guard: approver with allocation authority ≠ requester; capacity still available
    event: EVT-ALC-COMMITTED
  errors:
  - ALLOCATION_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CAPACITY_UNAVAILABLE
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/allocations/{id}/actions/approve
  internal: false
  policy: POL-ALC-APPROVE
  actors: Planner (request, release) · allocation authority (approve, reject, pre-empt)
    · task assignee (consumption)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ALC-REJECT
  aggregate: AGG-ALLOCATION
  bc: BC05
  transitions:
  - from:
    - PENDING_APPROVAL
    to: REJECTED
    guard: reason
    event: EVT-ALC-REJECTED
  errors:
  - ALLOCATION_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/allocations/{id}/actions/reject
  internal: false
  policy: POL-ALC-REJECT
  actors: Planner (request, release) · allocation authority (approve, reject, pre-empt)
    · task assignee (consumption)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ALC-RECORD-CONSUMPTION
  aggregate: AGG-ALLOCATION
  bc: BC05
  transitions:
  - from:
    - COMMITTED
    to: '='
    guard: quantity in pool unit; time; consumption beyond commitment flagged (REQ-RES-010)
    event: EVT-ALC-CONSUMED
  errors:
  - ALLOCATION_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CONSUMPTION_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/allocations/{id}/actions/record-consumption
  internal: false
  policy: POL-ALC-RECORD-CONSUMPTION
  actors: Planner (request, release) · allocation authority (approve, reject, pre-empt)
    · task assignee (consumption)
  payload: quantity!:number at!:date-time note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ALC-PREEMPT
  aggregate: AGG-ALLOCATION
  bc: BC05
  transitions:
  - from:
    - COMMITTED
    to: PREEMPTED
    guard: pre-emption decision (BC04 Decision) by an authority for the pool scope;
      higher-priority allocation reference; owners notified (REQ-RES-009)
    event: EVT-ALC-PREEMPTED
  errors:
  - ALLOCATION_INVALID_STATE_TRANSITION
  - AUTHORITY_REQUIRED
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/allocations/{id}/actions/preempt
  internal: false
  policy: POL-ALC-PREEMPT
  actors: Planner (request, release) · allocation authority (approve, reject, pre-empt)
    · task assignee (consumption)
  payload: decision!:urn preempting_allocation!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ALC-RELEASE
  aggregate: AGG-ALLOCATION
  bc: BC05
  transitions:
  - from:
    - COMMITTED
    to: RELEASED
    guard: requester or task owner; unused quantity returned to the ledger
    event: EVT-ALC-RELEASED
  errors:
  - ALLOCATION_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/allocations/{id}/actions/release
  internal: false
  policy: POL-ALC-RELEASE
  actors: Planner (request, release) · allocation authority (approve, reject, pre-empt)
    · task assignee (consumption)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RRQ-DEFINE
  aggregate: AGG-ROLE-REQUIREMENT
  bc: BC05
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: role exists (BC01); requirements reference RD-COMPETENCIES
    event: EVT-RRQ-DEFINED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ROLE_REQUIREMENT_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/role-requirements
  internal: false
  policy: POL-RRQ-DEFINE
  actors: Training Manager / Administrator
  payload: role!:urn requirements!:array
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-RRQ-EDIT
  aggregate: AGG-ROLE-REQUIREMENT
  bc: BC05
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    to: '='
    guard: requirements valid; ACTIVE → new version
    event: EVT-RRQ-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ROLE_REQUIREMENT_INVALID
  - ROLE_REQUIREMENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/role-requirements/{id}/actions/edit
  internal: false
  policy: POL-RRQ-EDIT
  actors: Training Manager / Administrator
  payload: requirements!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RRQ-ACTIVATE
  aggregate: AGG-ROLE-REQUIREMENT
  bc: BC05
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: approver ≠ author
    event: EVT-RRQ-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ROLE_REQUIREMENT_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/role-requirements/{id}/actions/activate
  internal: false
  policy: POL-RRQ-ACTIVATE
  actors: Training Manager / Administrator
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RRQ-RETIRE
  aggregate: AGG-ROLE-REQUIREMENT
  bc: BC05
  transitions:
  - from:
    - ACTIVE
    to: RETIRED
    guard: reason
    event: EVT-RRQ-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - ROLE_REQUIREMENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/role-requirements/{id}/actions/retire
  internal: false
  policy: POL-RRQ-RETIRE
  actors: Training Manager / Administrator
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
