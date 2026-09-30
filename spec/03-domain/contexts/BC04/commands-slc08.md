---
id: CMD-CAT-BC04-SLC08
type: command-catalog
title: Commands — BC04 (SLC-08)
wave: W4
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC04 (SLC-08)

_24 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-DRQ-CREATE | AGG-DECISION-REQUEST | `POST /api/v1/operations/decision-requests` | لا | Analyst / Planner / Manager (create, add, cite, open, withdraw) | POL-DRQ-CREATE | `question!:LocalizedName decision_type!:string scope!:urn deadline!:date-time context_refs:array label!:Label` | EVT-DRQ-CREATED | AUTHZ_DENIED, DECISION_REQUEST_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DRQ-ADD-OPTION | AGG-DECISION-REQUEST | `POST /api/v1/operations/decision-requests/{id}/actions/add-option` | لا | Analyst / Planner / Manager (create, add, cite, open, withdraw) | POL-DRQ-ADD-OPTION | `text!:LocalizedName expected_impact:LocalizedName` | EVT-DRQ-OPTION-ADDED | AUTHZ_DENIED, DECISION_REQUEST_INVALID, DECISION_REQUEST_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DRQ-CITE | AGG-DECISION-REQUEST | `POST /api/v1/operations/decision-requests/{id}/actions/cite` | لا | Analyst / Planner / Manager (create, add, cite, open, withdraw) | POL-DRQ-CITE | `citations!:array` | EVT-DRQ-CITED | AUTHZ_DENIED, CITATION_ABOVE_LABEL, DECISION_REQUEST_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DRQ-OPEN | AGG-DECISION-REQUEST | `POST /api/v1/operations/decision-requests/{id}/actions/open` | لا | Analyst / Planner / Manager (create, add, cite, open, withdraw) | POL-DRQ-OPEN | `—` | EVT-DRQ-OPENED | AUTHZ_DENIED, DECISION_REQUEST_INCOMPLETE, DECISION_REQUEST_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DRQ-WITHDRAW | AGG-DECISION-REQUEST | `POST /api/v1/operations/decision-requests/{id}/actions/withdraw` | لا | Analyst / Planner / Manager (create, add, cite, open, withdraw) | POL-DRQ-WITHDRAW | `reason!:string` | EVT-DRQ-WITHDRAWN | AUTHZ_DENIED, DECISION_REQUEST_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DEC-RECORD | AGG-DECISION | `POST /api/v1/operations/decisions` | لا | authority holder (record) · higher authority (annul) | POL-DEC-RECORD | `request:urn selected_option!:string rationale!:LocalizedName effective_from!:date-time citations:array supersedes:urn ad_hoc_reason:string label!:Label` | EVT-DEC-RECORDED | AUTHORITY_REQUIRED, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DEC-ANNUL | AGG-DECISION | `POST /api/v1/operations/decisions/{id}/actions/annul` | لا | authority holder (record) · higher authority (annul) | POL-DEC-ANNUL | `reason!:string` | EVT-DEC-ANNULLED | AUTHORITY_REQUIRED, AUTHZ_DENIED, DECISION_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLN-CREATE | AGG-PLAN | `POST /api/v1/operations/plans` | لا | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-CREATE | `title!:LocalizedName owner!:urn org_scope!:urn implements:array plan_kind!:enum(OPERATIONS,CONTINGENCY) triggered_by:urn window!:Interval label!:Label` | EVT-PLN-CREATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLN-SUSPEND | AGG-PLAN | `POST /api/v1/operations/plans/{id}/actions/suspend` | لا | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-SUSPEND | `reason!:string` | EVT-PLN-SUSPENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLN-RESUME | AGG-PLAN | `POST /api/v1/operations/plans/{id}/actions/resume` | لا | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-RESUME | `reason!:string` | EVT-PLN-RESUMED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLN-COMPLETE | AGG-PLAN | `POST /api/v1/operations/plans/{id}/actions/complete` | لا | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-COMPLETE | `note:string` | EVT-PLN-COMPLETED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_INVALID_STATE_TRANSITION, PLAN_NOT_COMPLETABLE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLN-CLOSE | AGG-PLAN | `POST /api/v1/operations/plans/{id}/actions/close` | لا | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-CLOSE | `after_action_notes:LocalizedName` | EVT-PLN-CLOSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLN-CANCEL | AGG-PLAN | `POST /api/v1/operations/plans/{id}/actions/cancel` | لا | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-CANCEL | `reason!:string` | EVT-PLN-CANCELLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLN-RECLASSIFY | AGG-PLAN | `POST /api/v1/operations/plans/{id}/actions/reclassify` | لا | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify) | POL-PLN-RECLASSIFY | `label!:Label reason!:string` | EVT-PLN-RECLASSIFIED | AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, IDEMPOTENCY_KEY_REUSED, PLAN_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLV-DRAFT | AGG-PLAN-VERSION | `POST /api/v1/operations/plan-versions` | لا | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-DRAFT | `plan!:urn based_on:integer` | EVT-PLV-DRAFTED | AUTHZ_DENIED, DRAFT_EXISTS, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLV-EDIT | AGG-PLAN-VERSION | `POST /api/v1/operations/plan-versions/{id}/actions/edit` | لا | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-EDIT | `objectives!:array outcomes!:array constraints:array assumptions:array phases!:array activities!:array milestones:array dependencies:array resource_notes:array` | EVT-PLV-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_VERSION_INVALID, PLAN_VERSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLV-SUBMIT | AGG-PLAN-VERSION | `POST /api/v1/operations/plan-versions/{id}/actions/submit` | لا | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-SUBMIT | `—` | EVT-PLV-SUBMITTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_VERSION_INCOMPLETE, PLAN_VERSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLV-RETURN | AGG-PLAN-VERSION | `POST /api/v1/operations/plan-versions/{id}/actions/return` | لا | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-RETURN | `reason!:string` | EVT-PLV-RETURNED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_VERSION_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLV-APPROVE | AGG-PLAN-VERSION | `POST /api/v1/operations/plan-versions/{id}/actions/approve` | لا | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-APPROVE | `note:string` | EVT-PLV-BASELINED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_VERSION_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLV-REJECT | AGG-PLAN-VERSION | `POST /api/v1/operations/plan-versions/{id}/actions/reject` | لا | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-REJECT | `reason!:string` | EVT-PLV-REJECTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_VERSION_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLV-AMEND-MINOR | AGG-PLAN-VERSION | `POST /api/v1/operations/plan-versions/{id}/actions/amend-minor` | لا | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-AMEND-MINOR | `annotations!:array` | EVT-PLV-MINOR-AMENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MAJOR_CHANGE_REQUIRES_VERSION, PLAN_VERSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PLV-DISCARD | AGG-PLAN-VERSION | `POST /api/v1/operations/plan-versions/{id}/actions/discard` | لا | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject) | POL-PLV-DISCARD | `reason!:string` | EVT-PLV-DISCARDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PLAN_VERSION_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-OUT-RECORD | AGG-OUTCOME-TRACKER | `POST /api/v1/operations/outcome-trackers/{id}/actions/record` | لا | Planner / owner (record, correct) | POL-OUT-RECORD | `value!:number unit!:string measured_at!:date-time source!:enum(manual,task_result,observation) source_ref:urn note:string` | EVT-OUT-MEASURED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MEASUREMENT_INVALID, OUTCOME_TRACKER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-OUT-CORRECT | AGG-OUTCOME-TRACKER | `POST /api/v1/operations/outcome-trackers/{id}/actions/correct` | لا | Planner / owner (record, correct) | POL-OUT-CORRECT | `measurement_id!:string value!:number unit!:string reason!:string` | EVT-OUT-MEASUREMENT-CORRECTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OUTCOME_TRACKER_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-DRQ-CREATE
  aggregate: AGG-DECISION-REQUEST
  bc: BC04
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: question; required decision type (RD-DECISION-TYPES); scope unit; deadline;
      label
    event: EVT-DRQ-CREATED
  errors:
  - AUTHZ_DENIED
  - DECISION_REQUEST_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/operations/decision-requests
  internal: false
  policy: POL-DRQ-CREATE
  actors: Analyst / Planner / Manager (create, add, cite, open, withdraw)
  payload: question!:LocalizedName decision_type!:string scope!:urn deadline!:date-time
    context_refs:array label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-DRQ-ADD-OPTION
  aggregate: AGG-DECISION-REQUEST
  bc: BC04
  transitions:
  - from:
    - DRAFT
    - OPEN
    to: '='
    guard: option text; expected impact; options ≤ 10
    event: EVT-DRQ-OPTION-ADDED
  errors:
  - AUTHZ_DENIED
  - DECISION_REQUEST_INVALID
  - DECISION_REQUEST_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/decision-requests/{id}/actions/add-option
  internal: false
  policy: POL-DRQ-ADD-OPTION
  actors: Analyst / Planner / Manager (create, add, cite, open, withdraw)
  payload: text!:LocalizedName expected_impact:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DRQ-CITE
  aggregate: AGG-DECISION-REQUEST
  bc: BC04
  transitions:
  - from:
    - DRAFT
    - OPEN
    to: '='
    guard: assessment or evidence visible; pinned URN + version; cited label ≤ request
      label
    event: EVT-DRQ-CITED
  errors:
  - AUTHZ_DENIED
  - CITATION_ABOVE_LABEL
  - DECISION_REQUEST_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/decision-requests/{id}/actions/cite
  internal: false
  policy: POL-DRQ-CITE
  actors: Analyst / Planner / Manager (create, add, cite, open, withdraw)
  payload: citations!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DRQ-OPEN
  aggregate: AGG-DECISION-REQUEST
  bc: BC04
  transitions:
  - from:
    - DRAFT
    to: OPEN
    guard: ≥ 2 options (one may be 'no action'); ≥ 1 citation (REQ-DEC-001, OUT-04)
    event: EVT-DRQ-OPENED
  errors:
  - AUTHZ_DENIED
  - DECISION_REQUEST_INCOMPLETE
  - DECISION_REQUEST_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/decision-requests/{id}/actions/open
  internal: false
  policy: POL-DRQ-OPEN
  actors: Analyst / Planner / Manager (create, add, cite, open, withdraw)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DRQ-WITHDRAW
  aggregate: AGG-DECISION-REQUEST
  bc: BC04
  transitions:
  - from:
    - DRAFT
    - OPEN
    to: WITHDRAWN
    guard: reason
    event: EVT-DRQ-WITHDRAWN
  errors:
  - AUTHZ_DENIED
  - DECISION_REQUEST_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/decision-requests/{id}/actions/withdraw
  internal: false
  policy: POL-DRQ-WITHDRAW
  actors: Analyst / Planner / Manager (create, add, cite, open, withdraw)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DEC-RECORD
  aggregate: AGG-DECISION
  bc: BC04
  transitions:
  - from:
    - ∅
    to: RECORDED
    guard: AuthorityCheck(decider, decision type, scope, now) = authorized — grant
      chain stored as authority snapshot (BRL-003, REQ-DEC-002); request OPEN (or
      ad-hoc with rationale and ≥ 1 citation); selected option ∈ request options;
      rationale; effective_from ≥ now − 1 h; supersedes (optional) is RECORDED and
      same scope
    event: EVT-DEC-RECORDED
  errors:
  - AUTHORITY_REQUIRED
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/operations/decisions
  internal: false
  policy: POL-DEC-RECORD
  actors: authority holder (record) · higher authority (annul)
  payload: request:urn selected_option!:string rationale!:LocalizedName effective_from!:date-time
    citations:array supersedes:urn ad_hoc_reason:string label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-DEC-ANNUL
  aggregate: AGG-DECISION
  bc: BC04
  transitions:
  - from:
    - RECORDED
    to: ANNULLED
    guard: recorded in error; actor holds authority for the same decision type at
      a higher scope; reason; plans implementing it are flagged
    event: EVT-DEC-ANNULLED
  errors:
  - AUTHORITY_REQUIRED
  - AUTHZ_DENIED
  - DECISION_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/decisions/{id}/actions/annul
  internal: false
  policy: POL-DEC-ANNUL
  actors: authority holder (record) · higher authority (annul)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLN-CREATE
  aggregate: AGG-PLAN
  bc: BC04
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: title; owner; org scope; implements ≥ 1 decision (RECORDED) or objective
      (REQ-OPS-002), or for plan_kind=CONTINGENCY a risk_ref or incident_ref trigger
      (CR-60, SLC-17); label ≥ implemented decisions or triggering scope's label
    event: EVT-PLN-CREATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/operations/plans
  internal: false
  policy: POL-PLN-CREATE
  actors: Planner / owner (create, suspend, resume, complete, close) · authority (cancel)
    · Security Officer (reclassify)
  payload: title!:LocalizedName owner!:urn org_scope!:urn implements:array plan_kind!:enum(OPERATIONS,CONTINGENCY)
    triggered_by:urn window!:Interval label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-PLN-SUSPEND
  aggregate: AGG-PLAN
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    to: SUSPENDED
    guard: reason; open tasks suspended (flag, INV-TASK-06)
    event: EVT-PLN-SUSPENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plans/{id}/actions/suspend
  internal: false
  policy: POL-PLN-SUSPEND
  actors: Planner / owner (create, suspend, resume, complete, close) · authority (cancel)
    · Security Officer (reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLN-RESUME
  aggregate: AGG-PLAN
  bc: BC04
  transitions:
  - from:
    - SUSPENDED
    to: ACTIVE
    guard: reason; tasks unsuspended
    event: EVT-PLN-RESUMED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plans/{id}/actions/resume
  internal: false
  policy: POL-PLN-RESUME
  actors: Planner / owner (create, suspend, resume, complete, close) · authority (cancel)
    · Security Officer (reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLN-COMPLETE
  aggregate: AGG-PLAN
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    to: COMPLETED
    guard: all plan tasks terminal; every outcome has ≥ 1 measurement
    event: EVT-PLN-COMPLETED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_INVALID_STATE_TRANSITION
  - PLAN_NOT_COMPLETABLE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plans/{id}/actions/complete
  internal: false
  policy: POL-PLN-COMPLETE
  actors: Planner / owner (create, suspend, resume, complete, close) · authority (cancel)
    · Security Officer (reclassify)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLN-CLOSE
  aggregate: AGG-PLAN
  bc: BC04
  transitions:
  - from:
    - COMPLETED
    to: CLOSED
    guard: after-action notes (optional in R1); outcome trackers closed
    event: EVT-PLN-CLOSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plans/{id}/actions/close
  internal: false
  policy: POL-PLN-CLOSE
  actors: Planner / owner (create, suspend, resume, complete, close) · authority (cancel)
    · Security Officer (reclassify)
  payload: after_action_notes:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLN-CANCEL
  aggregate: AGG-PLAN
  bc: BC04
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    - SUSPENDED
    to: CANCELLED
    guard: authority; reason; open tasks cancelled
    event: EVT-PLN-CANCELLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plans/{id}/actions/cancel
  internal: false
  policy: POL-PLN-CANCEL
  actors: Planner / owner (create, suspend, resume, complete, close) · authority (cancel)
    · Security Officer (reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLN-RECLASSIFY
  aggregate: AGG-PLAN
  bc: BC04
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    - SUSPENDED
    to: '='
    guard: authority; new label ≥ implemented decisions; assignees without clearance
      → reassignment required
    event: EVT-PLN-RECLASSIFIED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plans/{id}/actions/reclassify
  internal: false
  policy: POL-PLN-RECLASSIFY
  actors: Planner / owner (create, suspend, resume, complete, close) · authority (cancel)
    · Security Officer (reclassify)
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLV-DRAFT
  aggregate: AGG-PLAN-VERSION
  bc: BC04
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: plan not CLOSED/CANCELLED; new or revision copying the BASELINED version
      (activity ids preserved); ≤ 1 DRAFT/IN_REVIEW per plan
    event: EVT-PLV-DRAFTED
  errors:
  - AUTHZ_DENIED
  - DRAFT_EXISTS
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/operations/plan-versions
  internal: false
  policy: POL-PLV-DRAFT
  actors: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval
    authority ≠ author (approve, return, reject)
  payload: plan!:urn based_on:integer
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-PLV-EDIT
  aggregate: AGG-PLAN-VERSION
  bc: BC04
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: objectives, outcomes (metric, unit, target, due), phases, activities (stable
      ids, task_generating flag, task type), milestones, schedule within plan window,
      acyclic dependencies
    event: EVT-PLV-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_VERSION_INVALID
  - PLAN_VERSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plan-versions/{id}/actions/edit
  internal: false
  policy: POL-PLV-EDIT
  actors: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval
    authority ≠ author (approve, return, reject)
  payload: objectives!:array outcomes!:array constraints:array assumptions:array phases!:array
    activities!:array milestones:array dependencies:array resource_notes:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLV-SUBMIT
  aggregate: AGG-PLAN-VERSION
  bc: BC04
  transitions:
  - from:
    - DRAFT
    to: IN_REVIEW
    guard: complete per REQ-OPS-001; change classification computed vs current baseline
      (major/minor, BRL-005)
    event: EVT-PLV-SUBMITTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_VERSION_INCOMPLETE
  - PLAN_VERSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plan-versions/{id}/actions/submit
  internal: false
  policy: POL-PLV-SUBMIT
  actors: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval
    authority ≠ author (approve, return, reject)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLV-RETURN
  aggregate: AGG-PLAN-VERSION
  bc: BC04
  transitions:
  - from:
    - IN_REVIEW
    to: DRAFT
    guard: reviewer; reason
    event: EVT-PLV-RETURNED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_VERSION_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plan-versions/{id}/actions/return
  internal: false
  policy: POL-PLV-RETURN
  actors: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval
    authority ≠ author (approve, return, reject)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLV-APPROVE
  aggregate: AGG-PLAN-VERSION
  bc: BC04
  transitions:
  - from:
    - IN_REVIEW
    to: BASELINED
    guard: approver ≠ author (REQ-OPS-005); AuthorityCheck(approver, plan-approval
      type, scope); previous BASELINED → SUPERSEDED in the same transaction; task
      synchronization started (SPEC-PLAN §3)
    event: EVT-PLV-BASELINED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_VERSION_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plan-versions/{id}/actions/approve
  internal: false
  policy: POL-PLV-APPROVE
  actors: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval
    authority ≠ author (approve, return, reject)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLV-REJECT
  aggregate: AGG-PLAN-VERSION
  bc: BC04
  transitions:
  - from:
    - IN_REVIEW
    to: REJECTED
    guard: reason
    event: EVT-PLV-REJECTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_VERSION_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plan-versions/{id}/actions/reject
  internal: false
  policy: POL-PLV-REJECT
  actors: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval
    authority ≠ author (approve, return, reject)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLV-AMEND-MINOR
  aggregate: AGG-PLAN-VERSION
  bc: BC04
  transitions:
  - from:
    - BASELINED
    to: '='
    guard: only minor fields (descriptions, notes, attachments) per BRL-005; recorded
      as annotation, baseline content unchanged
    event: EVT-PLV-MINOR-AMENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MAJOR_CHANGE_REQUIRES_VERSION
  - PLAN_VERSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plan-versions/{id}/actions/amend-minor
  internal: false
  policy: POL-PLV-AMEND-MINOR
  actors: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval
    authority ≠ author (approve, return, reject)
  payload: annotations!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PLV-DISCARD
  aggregate: AGG-PLAN-VERSION
  bc: BC04
  transitions:
  - from:
    - DRAFT
    to: DISCARDED
    guard: author; reason
    event: EVT-PLV-DISCARDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PLAN_VERSION_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/plan-versions/{id}/actions/discard
  internal: false
  policy: POL-PLV-DISCARD
  actors: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval
    authority ≠ author (approve, return, reject)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-OUT-RECORD
  aggregate: AGG-OUTCOME-TRACKER
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: value with unit convertible to metric unit (UCUM); measured_at; source
      = manual | task result | observation ref
    event: EVT-OUT-MEASURED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MEASUREMENT_INVALID
  - OUTCOME_TRACKER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/outcome-trackers/{id}/actions/record
  internal: false
  policy: POL-OUT-RECORD
  actors: Planner / owner (record, correct)
  payload: value!:number unit!:string measured_at!:date-time source!:enum(manual,task_result,observation)
    source_ref:urn note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-OUT-CORRECT
  aggregate: AGG-OUTCOME-TRACKER
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: 'corrects a measurement: previous record closed (recorded_to), corrected
      record added — no overwrite'
    event: EVT-OUT-MEASUREMENT-CORRECTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OUTCOME_TRACKER_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/outcome-trackers/{id}/actions/correct
  internal: false
  policy: POL-OUT-CORRECT
  actors: Planner / owner (record, correct)
  payload: measurement_id!:string value!:number unit!:string reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
