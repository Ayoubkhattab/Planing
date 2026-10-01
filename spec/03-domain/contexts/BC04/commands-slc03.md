---
id: CMD-CAT-BC04-SLC03
type: command-catalog
title: Commands — BC04 (SLC-03)
wave: W4
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC04 (SLC-03)

_28 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-TASK-CREATE | AGG-TASK | `POST /api/v1/operations/tasks` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-CREATE | `task_type!:urn title!:LocalizedName description:LocalizedName plan_ref:urn incident_ref:urn ad_hoc_reason:string owner!:urn org_scope!:urn due_at:date-time dependencies:array follow_up_of:urn label!:Label` | EVT-TASK-CREATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TASK_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-EDIT | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/edit` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-EDIT | `title:LocalizedName description:LocalizedName criteria:array dependencies:array` | EVT-TASK-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TASK_INVALID, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-MARK-READY | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/mark-ready` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-MARK-READY | `—` | EVT-TASK-READIED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TASK_INVALID_STATE_TRANSITION, TASK_NOT_READY, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-ASSIGN | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/assign` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-ASSIGN | `assignee!:urn note:string` | EVT-TASK-ASSIGNED | ASSIGNEE_NOT_ELIGIBLE, AUTHZ_DENIED, ELIGIBILITY_UNAVAILABLE, IDEMPOTENCY_KEY_REUSED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-REASSIGN | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/reassign` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-REASSIGN | `assignee!:urn reason!:string` | EVT-TASK-REASSIGNED | ASSIGNEE_NOT_ELIGIBLE, AUTHZ_DENIED, ELIGIBILITY_UNAVAILABLE, IDEMPOTENCY_KEY_REUSED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-ACCEPT | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/accept` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-ACCEPT | `—` | EVT-TASK-ACCEPTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, NOT_ASSIGNEE, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-DECLINE | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/decline` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-DECLINE | `reason!:string` | EVT-TASK-DECLINED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-START | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/start` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-START | `—` | EVT-TASK-STARTED | AUTHZ_DENIED, DEPENDENCIES_NOT_MET, IDEMPOTENCY_KEY_REUSED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-BLOCK | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/block` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-BLOCK | `reason!:string` | EVT-TASK-BLOCKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-RESUME | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/resume` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-RESUME | `note!:string` | EVT-TASK-RESUMED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-ADD-RESULT-ITEM | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/add-result-item` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-ADD-RESULT-ITEM | `kind!:enum(note,evidence,observation,measurement) ref:urn note:LocalizedName measurement:object` | EVT-TASK-RESULT-ITEM-ADDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RESULT_ITEM_INVALID, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-SUBMIT | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/submit` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-SUBMIT | `summary!:LocalizedName` | EVT-TASK-SUBMITTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RESULT_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-START-REVIEW | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/start-review` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-START-REVIEW | `—` | EVT-TASK-REVIEW-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-RETURN | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/return` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-RETURN | `reason!:string` | EVT-TASK-RETURNED-FOR-REWORK | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-APPROVE | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/approve` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-APPROVE | `note:string` | EVT-TASK-APPROVED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-REJECT | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/reject` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-REJECT | `reason!:string create_follow_up!:boolean` | EVT-TASK-REJECTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-COMPLETE | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/complete` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-COMPLETE | `attestations!:array` | EVT-TASK-COMPLETED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TASK_CRITERIA_NOT_MET, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-CLOSE | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/close` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-CLOSE | `note:string` | EVT-TASK-CLOSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OPEN_FOLLOW_UPS, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-CANCEL | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/cancel` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-CANCEL | `reason!:string` | EVT-TASK-CANCELLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-ESCALATE | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/escalate` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-ESCALATE | `reason!:string` | EVT-TASK-ESCALATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-SET-DUE | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/set-due` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-SET-DUE | `due_at!:date-time reason!:string` | EVT-TASK-DUE-CHANGED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-SUSPEND | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/suspend` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-SUSPEND | `reason!:string` | EVT-TASK-SUSPENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-UNSUSPEND | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/unsuspend` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-UNSUSPEND | `reason!:string` | EVT-TASK-UNSUSPENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, NOT_SUSPENDED, TASK_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TASK-RECLASSIFY | AGG-TASK | `POST /api/v1/operations/tasks/{id}/actions/reclassify` | لا | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) · assignee (accept, decline, start, block, resume, add result, submit) · reviewer (review, return, approve, reject, complete) | POL-TASK-RECLASSIFY | `label!:Label reason!:string` | EVT-TASK-RECLASSIFIED | AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, IDEMPOTENCY_KEY_REUSED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TTY-DEFINE | AGG-TASK-TYPE | `POST /api/v1/operations/task-types` | لا | Administrator / Planner lead | POL-TTY-DEFINE | `code!:string name!:LocalizedName` | EVT-TTY-DEFINED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TASK_TYPE_CODE_TAKEN, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TTY-EDIT | AGG-TASK-TYPE | `POST /api/v1/operations/task-types/{id}/actions/edit` | لا | Administrator / Planner lead | POL-TTY-EDIT | `qualification_requirements!:array criteria_templates!:array escalation!:object expires_on_due!:boolean review_steps:integer` | EVT-TTY-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TASK_TYPE_INVALID, TASK_TYPE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TTY-ACTIVATE | AGG-TASK-TYPE | `POST /api/v1/operations/task-types/{id}/actions/activate` | لا | Administrator / Planner lead | POL-TTY-ACTIVATE | `—` | EVT-TTY-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TASK_TYPE_INVALID, TASK_TYPE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TTY-RETIRE | AGG-TASK-TYPE | `POST /api/v1/operations/task-types/{id}/actions/retire` | لا | Administrator / Planner lead | POL-TTY-RETIRE | `reason!:string` | EVT-TTY-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TASK_TYPE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-TASK-CREATE
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: task type ACTIVE (version pinned); plan_ref (operations, collection or
      contingency plan — CR-59, CR-61) or incident_ref (direct response task under
      an Incident, SLC-17 — CR-61), or ad_hoc_reason + accountable owner (REQ-OPS-010);
      label ≤ creator clearance
    event: EVT-TASK-CREATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TASK_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/operations/tasks
  internal: false
  policy: POL-TASK-CREATE
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: task_type!:urn title!:LocalizedName description:LocalizedName plan_ref:urn
    incident_ref:urn ad_hoc_reason:string owner!:urn org_scope!:urn due_at:date-time
    dependencies:array follow_up_of:urn label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-TASK-EDIT
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - DRAFT
    - READY
    to: '='
    guard: creator or Planner; completion criteria editable only in DRAFT/READY; new
      version
    event: EVT-TASK-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TASK_INVALID
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/edit
  internal: false
  policy: POL-TASK-EDIT
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: title:LocalizedName description:LocalizedName criteria:array dependencies:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-MARK-READY
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - DRAFT
    to: READY
    guard: title, ≥ 1 completion criterion, owner; dependencies reference existing
      tasks without cycle
    event: EVT-TASK-READIED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_NOT_READY
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/mark-ready
  internal: false
  policy: POL-TASK-MARK-READY
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-ASSIGN
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - READY
    to: ASSIGNED
    guard: assignee ACTIVE user; assignee clearance ≥ task label; EligibilityCheck(assignee,
      task type, now) ∈ {ELIGIBLE, CONDITIONALLY_ELIGIBLE with condition met} (REQ-OPS-007);
      actor authorized in scope
    event: EVT-TASK-ASSIGNED
  errors:
  - ASSIGNEE_NOT_ELIGIBLE
  - AUTHZ_DENIED
  - ELIGIBILITY_UNAVAILABLE
  - IDEMPOTENCY_KEY_REUSED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/assign
  internal: false
  policy: POL-TASK-ASSIGN
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: assignee!:urn note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-REASSIGN
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - ASSIGNED
    - ACCEPTED
    - IN_PROGRESS
    - BLOCKED
    to: ASSIGNED
    guard: same checks as assign for the new assignee; reason; previous assignee notified
    event: EVT-TASK-REASSIGNED
  errors:
  - ASSIGNEE_NOT_ELIGIBLE
  - AUTHZ_DENIED
  - ELIGIBILITY_UNAVAILABLE
  - IDEMPOTENCY_KEY_REUSED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/reassign
  internal: false
  policy: POL-TASK-REASSIGN
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: assignee!:urn reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-ACCEPT
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - ASSIGNED
    to: ACCEPTED
    guard: actor = assignee
    event: EVT-TASK-ACCEPTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - NOT_ASSIGNEE
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/accept
  internal: false
  policy: POL-TASK-ACCEPT
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: ''
  offline_capable: true
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-DECLINE
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - ASSIGNED
    to: READY
    guard: actor = assignee; reason
    event: EVT-TASK-DECLINED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/decline
  internal: false
  policy: POL-TASK-DECLINE
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-START
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - ACCEPTED
    to: IN_PROGRESS
    guard: actor = assignee; all predecessor tasks COMPLETED or CLOSED
    event: EVT-TASK-STARTED
  errors:
  - AUTHZ_DENIED
  - DEPENDENCIES_NOT_MET
  - IDEMPOTENCY_KEY_REUSED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/start
  internal: false
  policy: POL-TASK-START
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: ''
  offline_capable: true
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-BLOCK
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - IN_PROGRESS
    to: BLOCKED
    guard: actor = assignee; blocking reason
    event: EVT-TASK-BLOCKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/block
  internal: false
  policy: POL-TASK-BLOCK
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: reason!:string
  offline_capable: true
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-RESUME
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - BLOCKED
    to: IN_PROGRESS
    guard: actor = assignee; resolution note
    event: EVT-TASK-RESUMED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/resume
  internal: false
  policy: POL-TASK-RESUME
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: note!:string
  offline_capable: true
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-ADD-RESULT-ITEM
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - IN_PROGRESS
    - BLOCKED
    to: '='
    guard: actor = assignee; item = note | evidence URN | observation URN | measurement
    event: EVT-TASK-RESULT-ITEM-ADDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RESULT_ITEM_INVALID
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/add-result-item
  internal: false
  policy: POL-TASK-ADD-RESULT-ITEM
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: kind!:enum(note,evidence,observation,measurement) ref:urn note:LocalizedName
    measurement:object
  offline_capable: true
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-SUBMIT
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - IN_PROGRESS
    to: SUBMITTED
    guard: actor = assignee; result has ≥ 1 item
    event: EVT-TASK-SUBMITTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RESULT_REQUIRED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/submit
  internal: false
  policy: POL-TASK-SUBMIT
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: summary!:LocalizedName
  offline_capable: true
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-START-REVIEW
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - SUBMITTED
    to: UNDER_REVIEW
    guard: actor has review permission in scope; actor ≠ assignee
    event: EVT-TASK-REVIEW-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/start-review
  internal: false
  policy: POL-TASK-START-REVIEW
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-RETURN
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - UNDER_REVIEW
    to: IN_PROGRESS
    guard: reviewer; rework reason
    event: EVT-TASK-RETURNED-FOR-REWORK
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/return
  internal: false
  policy: POL-TASK-RETURN
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-APPROVE
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - UNDER_REVIEW
    to: APPROVED
    guard: reviewer ≠ assignee unless tenant policy disables SoD (REQ-OPS-009)
    event: EVT-TASK-APPROVED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/approve
  internal: false
  policy: POL-TASK-APPROVE
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-REJECT
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - UNDER_REVIEW
    to: REJECTED
    guard: reviewer; reason; follow-up task may be created linked by follow_up_of
      (OQ-033)
    event: EVT-TASK-REJECTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/reject
  internal: false
  policy: POL-TASK-REJECT
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: reason!:string create_follow_up!:boolean
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-COMPLETE
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - APPROVED
    to: COMPLETED
    guard: attestation-type criteria confirmed by an authorized actor; all criteria
      satisfied (BRL-006)
    event: EVT-TASK-COMPLETED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TASK_CRITERIA_NOT_MET
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/complete
  internal: false
  policy: POL-TASK-COMPLETE
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: attestations!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-CLOSE
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - COMPLETED
    to: CLOSED
    guard: no open follow-up tasks
    event: EVT-TASK-CLOSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OPEN_FOLLOW_UPS
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/close
  internal: false
  policy: POL-TASK-CLOSE
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-CANCEL
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - DRAFT
    - READY
    - ASSIGNED
    - ACCEPTED
    - IN_PROGRESS
    - BLOCKED
    - SUBMITTED
    - UNDER_REVIEW
    - APPROVED
    to: CANCELLED
    guard: actor has cancel authority in scope; reason
    event: EVT-TASK-CANCELLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TASK_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/cancel
  internal: false
  policy: POL-TASK-CANCEL
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-ESCALATE
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from: &id001
    - DRAFT
    - READY
    - ASSIGNED
    - ACCEPTED
    - IN_PROGRESS
    - BLOCKED
    - SUBMITTED
    - UNDER_REVIEW
    - APPROVED
    - COMPLETED
    to: '='
    guard: reason; notifies next authority level (REQ-OPS-012)
    event: EVT-TASK-ESCALATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/escalate
  internal: false
  policy: POL-TASK-ESCALATE
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-SET-DUE
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from:
    - DRAFT
    - READY
    - ASSIGNED
    - ACCEPTED
    - IN_PROGRESS
    - BLOCKED
    to: '='
    guard: Planner or owner; reason
    event: EVT-TASK-DUE-CHANGED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/set-due
  internal: false
  policy: POL-TASK-SET-DUE
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: due_at!:date-time reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-SUSPEND
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from: *id001
    to: '='
    guard: suspend authority; reason; sets suspended = true
    event: EVT-TASK-SUSPENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/suspend
  internal: false
  policy: POL-TASK-SUSPEND
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-UNSUSPEND
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from: *id001
    to: '='
    guard: suspend authority; suspended = true
    event: EVT-TASK-UNSUSPENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - NOT_SUSPENDED
  - TASK_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/unsuspend
  internal: false
  policy: POL-TASK-UNSUSPEND
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TASK-RECLASSIFY
  aggregate: AGG-TASK
  bc: BC04
  transitions:
  - from: *id001
    to: '='
    guard: authority per tenant policy; assignee clearance ≥ new label, else reassignment
      required first
    event: EVT-TASK-RECLASSIFIED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - IDEMPOTENCY_KEY_REUSED
  - TASK_INVALID_STATE_TRANSITION
  - TASK_SUSPENDED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/tasks/{id}/actions/reclassify
  internal: false
  policy: POL-TASK-RECLASSIFY
  actors: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
    · assignee (accept, decline, start, block, resume, add result, submit) · reviewer
    (review, return, approve, reject, complete)
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TTY-DEFINE
  aggregate: AGG-TASK-TYPE
  bc: BC04
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: code unique in tenant
    event: EVT-TTY-DEFINED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TASK_TYPE_CODE_TAKEN
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/operations/task-types
  internal: false
  policy: POL-TTY-DEFINE
  actors: Administrator / Planner lead
  payload: code!:string name!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-TTY-EDIT
  aggregate: AGG-TASK-TYPE
  bc: BC04
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    to: '='
    guard: required qualifications exist in RD-COMPETENCIES; criteria templates valid;
      ACTIVE → new version (existing tasks keep their pinned version)
    event: EVT-TTY-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TASK_TYPE_INVALID
  - TASK_TYPE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/task-types/{id}/actions/edit
  internal: false
  policy: POL-TTY-EDIT
  actors: Administrator / Planner lead
  payload: qualification_requirements!:array criteria_templates!:array escalation!:object
    expires_on_due!:boolean review_steps:integer
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TTY-ACTIVATE
  aggregate: AGG-TASK-TYPE
  bc: BC04
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: ≥ 1 completion criterion template
    event: EVT-TTY-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TASK_TYPE_INVALID
  - TASK_TYPE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/task-types/{id}/actions/activate
  internal: false
  policy: POL-TTY-ACTIVATE
  actors: Administrator / Planner lead
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TTY-RETIRE
  aggregate: AGG-TASK-TYPE
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    to: RETIRED
    guard: reason; existing tasks unaffected
    event: EVT-TTY-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TASK_TYPE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/task-types/{id}/actions/retire
  internal: false
  policy: POL-TTY-RETIRE
  actors: Administrator / Planner lead
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
