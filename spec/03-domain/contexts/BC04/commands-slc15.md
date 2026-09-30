---
id: CMD-CAT-BC04-SLC15
type: command-catalog
title: Commands — BC04 (SLC-15)
wave: W4
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC04 (SLC-15)

_9 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-CRD-OPEN | AGG-COORDINATION-CASE | `POST /api/v1/operations/coordination-cases` | لا | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-OPEN | `title!:LocalizedName purpose!:LocalizedName lead_org!:urn links:array label!:Label` | EVT-CRD-OPENED | AUTHZ_DENIED, COORDINATION_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRD-ADD-PARTICIPANT | AGG-COORDINATION-CASE | `POST /api/v1/operations/coordination-cases/{id}/actions/add-participant` | لا | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-ADD-PARTICIPANT | `org_unit!:urn role!:string access_scope!:array` | EVT-CRD-PARTICIPANT-ADDED | AUTHZ_DENIED, COORDINATION_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, PARTICIPANT_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRD-REMOVE-PARTICIPANT | AGG-COORDINATION-CASE | `POST /api/v1/operations/coordination-cases/{id}/actions/remove-participant` | لا | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-REMOVE-PARTICIPANT | `org_unit!:urn reason!:string` | EVT-CRD-PARTICIPANT-REMOVED | AUTHZ_DENIED, COORDINATION_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, PARTICIPANT_HAS_RESPONSIBILITIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRD-ACTIVATE | AGG-COORDINATION-CASE | `POST /api/v1/operations/coordination-cases/{id}/actions/activate` | لا | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-ACTIVATE | `—` | EVT-CRD-ACTIVATED | AUTHZ_DENIED, COORDINATION_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, PARTICIPANTS_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRD-ASSIGN-RESPONSIBILITY | AGG-COORDINATION-CASE | `POST /api/v1/operations/coordination-cases/{id}/actions/assign-responsibility` | لا | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-ASSIGN-RESPONSIBILITY | `participant!:urn item!:LocalizedName due!:date-time requires_authority:string` | EVT-CRD-RESPONSIBILITY-ASSIGNED | AUTHZ_DENIED, COORDINATION_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, RESPONSIBILITY_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRD-UPDATE-RESPONSIBILITY | AGG-COORDINATION-CASE | `POST /api/v1/operations/coordination-cases/{id}/actions/update-responsibility` | لا | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-UPDATE-RESPONSIBILITY | `responsibility_id!:string status!:enum(in_progress,done,waived) note:string` | EVT-CRD-RESPONSIBILITY-UPDATED | AUTHZ_DENIED, COORDINATION_CASE_INVALID_STATE_TRANSITION, DECISION_PENDING, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRD-REQUEST-DECISION | AGG-COORDINATION-CASE | `POST /api/v1/operations/coordination-cases/{id}/actions/request-decision` | لا | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-REQUEST-DECISION | `responsibility_id!:string question!:LocalizedName options!:array` | EVT-CRD-DECISION-REQUESTED | AUTHZ_DENIED, COORDINATION_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, RESPONSIBILITY_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRD-CLOSE | AGG-COORDINATION-CASE | `POST /api/v1/operations/coordination-cases/{id}/actions/close` | لا | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-CLOSE | `note!:LocalizedName` | EVT-CRD-CLOSED | AUTHZ_DENIED, COORDINATION_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, OPEN_RESPONSIBILITIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRD-CANCEL | AGG-COORDINATION-CASE | `POST /api/v1/operations/coordination-cases/{id}/actions/cancel` | لا | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision) | POL-CRD-CANCEL | `reason!:string` | EVT-CRD-CANCELLED | AUTHZ_DENIED, COORDINATION_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-CRD-OPEN
  aggregate: AGG-COORDINATION-CASE
  bc: BC04
  transitions:
  - from:
    - ∅
    to: OPEN
    guard: title; purpose; lead organization; linked decisions/plans/situations visible
      to the opener; label
    event: EVT-CRD-OPENED
  errors:
  - AUTHZ_DENIED
  - COORDINATION_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/operations/coordination-cases
  internal: false
  policy: POL-CRD-OPEN
  actors: lead organization Manager (open, participants, activate, assign, close,
    cancel) · participant members (update, request decision)
  payload: title!:LocalizedName purpose!:LocalizedName lead_org!:urn links:array label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CRD-ADD-PARTICIPANT
  aggregate: AGG-COORDINATION-CASE
  bc: BC04
  transitions:
  - from:
    - OPEN
    - ACTIVE
    to: '='
    guard: org unit in the same tenant; participant role; access scope (sections);
      participant's members cleared for case label
    event: EVT-CRD-PARTICIPANT-ADDED
  errors:
  - AUTHZ_DENIED
  - COORDINATION_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - PARTICIPANT_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/coordination-cases/{id}/actions/add-participant
  internal: false
  policy: POL-CRD-ADD-PARTICIPANT
  actors: lead organization Manager (open, participants, activate, assign, close,
    cancel) · participant members (update, request decision)
  payload: org_unit!:urn role!:string access_scope!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRD-REMOVE-PARTICIPANT
  aggregate: AGG-COORDINATION-CASE
  bc: BC04
  transitions:
  - from:
    - OPEN
    - ACTIVE
    to: '='
    guard: not the lead; no open responsibilities
    event: EVT-CRD-PARTICIPANT-REMOVED
  errors:
  - AUTHZ_DENIED
  - COORDINATION_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - PARTICIPANT_HAS_RESPONSIBILITIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/coordination-cases/{id}/actions/remove-participant
  internal: false
  policy: POL-CRD-REMOVE-PARTICIPANT
  actors: lead organization Manager (open, participants, activate, assign, close,
    cancel) · participant members (update, request decision)
  payload: org_unit!:urn reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRD-ACTIVATE
  aggregate: AGG-COORDINATION-CASE
  bc: BC04
  transitions:
  - from:
    - OPEN
    to: ACTIVE
    guard: ≥ 2 participants
    event: EVT-CRD-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - COORDINATION_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - PARTICIPANTS_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/coordination-cases/{id}/actions/activate
  internal: false
  policy: POL-CRD-ACTIVATE
  actors: lead organization Manager (open, participants, activate, assign, close,
    cancel) · participant members (update, request decision)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRD-ASSIGN-RESPONSIBILITY
  aggregate: AGG-COORDINATION-CASE
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: participant exists; item, due; flag requires_authority (decision type)
      when the action needs that organization's authority
    event: EVT-CRD-RESPONSIBILITY-ASSIGNED
  errors:
  - AUTHZ_DENIED
  - COORDINATION_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - RESPONSIBILITY_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/coordination-cases/{id}/actions/assign-responsibility
  internal: false
  policy: POL-CRD-ASSIGN-RESPONSIBILITY
  actors: lead organization Manager (open, participants, activate, assign, close,
    cancel) · participant members (update, request decision)
  payload: participant!:urn item!:LocalizedName due!:date-time requires_authority:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRD-UPDATE-RESPONSIBILITY
  aggregate: AGG-COORDINATION-CASE
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: actor belongs to the responsible participant; status ∈ {in_progress, done,
      waived with reason}; items requiring authority cannot be done before the decision
      is recorded
    event: EVT-CRD-RESPONSIBILITY-UPDATED
  errors:
  - AUTHZ_DENIED
  - COORDINATION_CASE_INVALID_STATE_TRANSITION
  - DECISION_PENDING
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/coordination-cases/{id}/actions/update-responsibility
  internal: false
  policy: POL-CRD-UPDATE-RESPONSIBILITY
  actors: lead organization Manager (open, participants, activate, assign, close,
    cancel) · participant members (update, request decision)
  payload: responsibility_id!:string status!:enum(in_progress,done,waived) note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRD-REQUEST-DECISION
  aggregate: AGG-COORDINATION-CASE
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: responsibility requires authority; creates a Decision Request (SLC-08)
      in the participant's scope with the required decision type
    event: EVT-CRD-DECISION-REQUESTED
  errors:
  - AUTHZ_DENIED
  - COORDINATION_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - RESPONSIBILITY_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/coordination-cases/{id}/actions/request-decision
  internal: false
  policy: POL-CRD-REQUEST-DECISION
  actors: lead organization Manager (open, participants, activate, assign, close,
    cancel) · participant members (update, request decision)
  payload: responsibility_id!:string question!:LocalizedName options!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRD-CLOSE
  aggregate: AGG-COORDINATION-CASE
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    to: CLOSED
    guard: all responsibilities done or waived; closing note
    event: EVT-CRD-CLOSED
  errors:
  - AUTHZ_DENIED
  - COORDINATION_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - OPEN_RESPONSIBILITIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/coordination-cases/{id}/actions/close
  internal: false
  policy: POL-CRD-CLOSE
  actors: lead organization Manager (open, participants, activate, assign, close,
    cancel) · participant members (update, request decision)
  payload: note!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRD-CANCEL
  aggregate: AGG-COORDINATION-CASE
  bc: BC04
  transitions:
  - from:
    - OPEN
    - ACTIVE
    to: CANCELLED
    guard: lead; reason
    event: EVT-CRD-CANCELLED
  errors:
  - AUTHZ_DENIED
  - COORDINATION_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/coordination-cases/{id}/actions/cancel
  internal: false
  policy: POL-CRD-CANCEL
  actors: lead organization Manager (open, participants, activate, assign, close,
    cancel) · participant members (update, request decision)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
