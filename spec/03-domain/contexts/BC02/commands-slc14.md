---
id: CMD-CAT-BC02-SLC14
type: command-catalog
title: Commands — BC02 (SLC-14)
wave: W4
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC02 (SLC-14)

_14 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-CRQ-DRAFT | AGG-COLLECTION-REQUIREMENT | `POST /api/v1/information/collection-requirements` | لا | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-DRAFT | `question!:LocalizedName label!:Label` | EVT-CRQ-DRAFTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REQUIREMENT_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRQ-EDIT | AGG-COLLECTION-REQUIREMENT | `POST /api/v1/information/collection-requirements/{id}/actions/edit` | لا | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-EDIT | `area!:object window!:Interval priority!:integer due!:date-time eeis!:array` | EVT-CRQ-EDITED | AUTHZ_DENIED, COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REQUIREMENT_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRQ-SUBMIT | AGG-COLLECTION-REQUIREMENT | `POST /api/v1/information/collection-requirements/{id}/actions/submit` | لا | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-SUBMIT | `—` | EVT-CRQ-SUBMITTED | AUTHZ_DENIED, COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REQUIREMENT_INCOMPLETE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRQ-APPROVE | AGG-COLLECTION-REQUIREMENT | `POST /api/v1/information/collection-requirements/{id}/actions/approve` | لا | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-APPROVE | `note:string` | EVT-CRQ-APPROVED | AUTHZ_DENIED, COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRQ-REJECT | AGG-COLLECTION-REQUIREMENT | `POST /api/v1/information/collection-requirements/{id}/actions/reject` | لا | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-REJECT | `reason!:string` | EVT-CRQ-REJECTED | AUTHZ_DENIED, COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRQ-AMEND | AGG-COLLECTION-REQUIREMENT | `POST /api/v1/information/collection-requirements/{id}/actions/amend` | لا | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-AMEND | `due:date-time area:object eeis:array reason!:string` | EVT-CRQ-AMENDED | AUTHZ_DENIED, COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REQUIREMENT_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRQ-MARK-SATISFIED | AGG-COLLECTION-REQUIREMENT | `POST /api/v1/information/collection-requirements/{id}/actions/mark-satisfied` | لا | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-MARK-SATISFIED | `acceptance_note:string` | EVT-CRQ-SATISFIED | AUTHZ_DENIED, COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, FULFILMENT_INSUFFICIENT, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRQ-CANCEL | AGG-COLLECTION-REQUIREMENT | `POST /api/v1/information/collection-requirements/{id}/actions/cancel` | لا | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | POL-CRQ-CANCEL | `reason!:string` | EVT-CRQ-CANCELLED | AUTHZ_DENIED, COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CPL-CREATE | AGG-COLLECTION-PLAN | `POST /api/v1/information/collection-plans` | لا | collection planner | POL-CPL-CREATE | `requirements!:array title!:LocalizedName label!:Label` | EVT-CPL-CREATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REQUIREMENT_NOT_APPROVED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CPL-ADD-ACTIVITY | AGG-COLLECTION-PLAN | `POST /api/v1/information/collection-plans/{id}/actions/add-activity` | لا | collection planner | POL-CPL-ADD-ACTIVITY | `method!:string sources!:array area!:object window!:Interval unit!:urn task_type!:urn eei_refs!:array` | EVT-CPL-ACTIVITY-ADDED | ACTIVITY_INVALID, AUTHZ_DENIED, COLLECTION_PLAN_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CPL-REMOVE-ACTIVITY | AGG-COLLECTION-PLAN | `POST /api/v1/information/collection-plans/{id}/actions/remove-activity` | لا | collection planner | POL-CPL-REMOVE-ACTIVITY | `activity_id!:string` | EVT-CPL-ACTIVITY-REMOVED | ACTIVITY_ALREADY_TASKED, AUTHZ_DENIED, COLLECTION_PLAN_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CPL-ACTIVATE | AGG-COLLECTION-PLAN | `POST /api/v1/information/collection-plans/{id}/actions/activate` | لا | collection planner | POL-CPL-ACTIVATE | `—` | EVT-CPL-ACTIVATED | AUTHZ_DENIED, COLLECTION_PLAN_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, PLAN_EMPTY, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CPL-COMPLETE | AGG-COLLECTION-PLAN | `POST /api/v1/information/collection-plans/{id}/actions/complete` | لا | collection planner | POL-CPL-COMPLETE | `reason!:string` | EVT-CPL-COMPLETED | AUTHZ_DENIED, COLLECTION_PLAN_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CPL-CANCEL | AGG-COLLECTION-PLAN | `POST /api/v1/information/collection-plans/{id}/actions/cancel` | لا | collection planner | POL-CPL-CANCEL | `reason!:string` | EVT-CPL-CANCELLED | AUTHZ_DENIED, COLLECTION_PLAN_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-CRQ-DRAFT
  aggregate: AGG-COLLECTION-REQUIREMENT
  bc: BC02
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: question; requester; label
    event: EVT-CRQ-DRAFTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REQUIREMENT_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/collection-requirements
  internal: false
  policy: POL-CRQ-DRAFT
  actors: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection
    manager (approve, reject, amend)
  payload: question!:LocalizedName label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CRQ-EDIT
  aggregate: AGG-COLLECTION-REQUIREMENT
  bc: BC02
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: area polygon, window, priority 1–5, due, essential elements of information
      (EEIs)
    event: EVT-CRQ-EDITED
  errors:
  - AUTHZ_DENIED
  - COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REQUIREMENT_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-requirements/{id}/actions/edit
  internal: false
  policy: POL-CRQ-EDIT
  actors: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection
    manager (approve, reject, amend)
  payload: area!:object window!:Interval priority!:integer due!:date-time eeis!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRQ-SUBMIT
  aggregate: AGG-COLLECTION-REQUIREMENT
  bc: BC02
  transitions:
  - from:
    - DRAFT
    to: SUBMITTED
    guard: area, window, priority and ≥ 1 EEI present (REQ-COL-001)
    event: EVT-CRQ-SUBMITTED
  errors:
  - AUTHZ_DENIED
  - COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REQUIREMENT_INCOMPLETE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-requirements/{id}/actions/submit
  internal: false
  policy: POL-CRQ-SUBMIT
  actors: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection
    manager (approve, reject, amend)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRQ-APPROVE
  aggregate: AGG-COLLECTION-REQUIREMENT
  bc: BC02
  transitions:
  - from:
    - SUBMITTED
    to: APPROVED
    guard: collection manager with authority in the area scope; approver ≠ requester
    event: EVT-CRQ-APPROVED
  errors:
  - AUTHZ_DENIED
  - COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-requirements/{id}/actions/approve
  internal: false
  policy: POL-CRQ-APPROVE
  actors: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection
    manager (approve, reject, amend)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRQ-REJECT
  aggregate: AGG-COLLECTION-REQUIREMENT
  bc: BC02
  transitions:
  - from:
    - SUBMITTED
    to: REJECTED
    guard: reason (duplicate, out of scope, infeasible)
    event: EVT-CRQ-REJECTED
  errors:
  - AUTHZ_DENIED
  - COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-requirements/{id}/actions/reject
  internal: false
  policy: POL-CRQ-REJECT
  actors: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection
    manager (approve, reject, amend)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRQ-AMEND
  aggregate: AGG-COLLECTION-REQUIREMENT
  bc: BC02
  transitions:
  - from:
    - APPROVED
    to: '='
    guard: approver; extend due, adjust area or EEIs; recorded as new version
    event: EVT-CRQ-AMENDED
  errors:
  - AUTHZ_DENIED
  - COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REQUIREMENT_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-requirements/{id}/actions/amend
  internal: false
  policy: POL-CRQ-AMEND
  actors: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection
    manager (approve, reject, amend)
  payload: due:date-time area:object eeis:array reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRQ-MARK-SATISFIED
  aggregate: AGG-COLLECTION-REQUIREMENT
  bc: BC02
  transitions:
  - from:
    - APPROVED
    to: SATISFIED
    guard: requester; fulfilment as seen by the requester is ANSWERED, or PARTIAL
      with explicit acceptance note
    event: EVT-CRQ-SATISFIED
  errors:
  - AUTHZ_DENIED
  - COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION
  - FULFILMENT_INSUFFICIENT
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-requirements/{id}/actions/mark-satisfied
  internal: false
  policy: POL-CRQ-MARK-SATISFIED
  actors: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection
    manager (approve, reject, amend)
  payload: acceptance_note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRQ-CANCEL
  aggregate: AGG-COLLECTION-REQUIREMENT
  bc: BC02
  transitions:
  - from:
    - DRAFT
    - SUBMITTED
    - APPROVED
    to: CANCELLED
    guard: requester or approver; reason
    event: EVT-CRQ-CANCELLED
  errors:
  - AUTHZ_DENIED
  - COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-requirements/{id}/actions/cancel
  internal: false
  policy: POL-CRQ-CANCEL
  actors: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection
    manager (approve, reject, amend)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CPL-CREATE
  aggregate: AGG-COLLECTION-PLAN
  bc: BC02
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: ≥ 1 APPROVED collection requirement; planner in scope; label ≥ requirements
    event: EVT-CPL-CREATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REQUIREMENT_NOT_APPROVED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/collection-plans
  internal: false
  policy: POL-CPL-CREATE
  actors: collection planner
  payload: requirements!:array title!:LocalizedName label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CPL-ADD-ACTIVITY
  aggregate: AGG-COLLECTION-PLAN
  bc: BC02
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    to: '='
    guard: method in RD-COLLECTION-METHODS; source(s) ACTIVE; area ⊆ requirement areas;
      window ⊆ requirement windows; assigned unit; task type
    event: EVT-CPL-ACTIVITY-ADDED
  errors:
  - ACTIVITY_INVALID
  - AUTHZ_DENIED
  - COLLECTION_PLAN_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-plans/{id}/actions/add-activity
  internal: false
  policy: POL-CPL-ADD-ACTIVITY
  actors: collection planner
  payload: method!:string sources!:array area!:object window!:Interval unit!:urn task_type!:urn
    eei_refs!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CPL-REMOVE-ACTIVITY
  aggregate: AGG-COLLECTION-PLAN
  bc: BC02
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: activity not yet tasked
    event: EVT-CPL-ACTIVITY-REMOVED
  errors:
  - ACTIVITY_ALREADY_TASKED
  - AUTHZ_DENIED
  - COLLECTION_PLAN_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-plans/{id}/actions/remove-activity
  internal: false
  policy: POL-CPL-REMOVE-ACTIVITY
  actors: collection planner
  payload: activity_id!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CPL-ACTIVATE
  aggregate: AGG-COLLECTION-PLAN
  bc: BC02
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: ≥ 1 activity; creates one field task per activity through SLC-03 with plan_ref
      = this collection plan (CR-59)
    event: EVT-CPL-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - COLLECTION_PLAN_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_EMPTY
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-plans/{id}/actions/activate
  internal: false
  policy: POL-CPL-ACTIVATE
  actors: collection planner
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CPL-COMPLETE
  aggregate: AGG-COLLECTION-PLAN
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    to: COMPLETED
    guard: planner; open tasks cancelled with reason
    event: EVT-CPL-COMPLETED
  errors:
  - AUTHZ_DENIED
  - COLLECTION_PLAN_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-plans/{id}/actions/complete
  internal: false
  policy: POL-CPL-COMPLETE
  actors: collection planner
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CPL-CANCEL
  aggregate: AGG-COLLECTION-PLAN
  bc: BC02
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    to: CANCELLED
    guard: reason; open tasks cancelled
    event: EVT-CPL-CANCELLED
  errors:
  - AUTHZ_DENIED
  - COLLECTION_PLAN_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/collection-plans/{id}/actions/cancel
  internal: false
  policy: POL-CPL-CANCEL
  actors: collection planner
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
