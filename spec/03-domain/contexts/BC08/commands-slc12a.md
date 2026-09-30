---
id: CMD-CAT-BC08-SLC12A
type: command-catalog
title: Commands — BC08 (SLC-12a)
wave: W4
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC08 (SLC-12a)

_15 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-RTS-DRAFT | AGG-RETENTION-SCHEDULE | `POST /api/v1/governance/retention-schedules` | لا | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | POL-RTS-DRAFT | `based_on:urn` | EVT-RTS-DRAFTED | AUTHZ_DENIED, DRAFT_EXISTS, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RTS-EDIT | AGG-RETENTION-SCHEDULE | `POST /api/v1/governance/retention-schedules/{id}/actions/edit` | لا | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | POL-RTS-EDIT | `rules!:array` | EVT-RTS-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RETENTION_SCHEDULE_INVALID_STATE_TRANSITION, SCHEDULE_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RTS-ACTIVATE | AGG-RETENTION-SCHEDULE | `POST /api/v1/governance/retention-schedules/{id}/actions/activate` | لا | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | POL-RTS-ACTIVATE | `effective_from!:date-time retroactive_classes:array` | EVT-RTS-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RETENTION_SCHEDULE_INVALID_STATE_TRANSITION, SCHEDULE_INCOMPLETE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RTS-DISCARD | AGG-RETENTION-SCHEDULE | `POST /api/v1/governance/retention-schedules/{id}/actions/discard` | لا | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | POL-RTS-DISCARD | `reason!:string` | EVT-RTS-DISCARDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, RETENTION_SCHEDULE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-LHD-PLACE | AGG-LEGAL-HOLD | `POST /api/v1/governance/legal-holds` | لا | Legal/Compliance authority (place, extend, request/approve/cancel release) | POL-LHD-PLACE | `name!:string legal_reference!:string scope!:array` | EVT-LHD-PLACED | AUTHZ_DENIED, HOLD_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-LHD-EXTEND | AGG-LEGAL-HOLD | `POST /api/v1/governance/legal-holds/{id}/actions/extend` | لا | Legal/Compliance authority (place, extend, request/approve/cancel release) | POL-LHD-EXTEND | `scope!:array reason!:string` | EVT-LHD-EXTENDED | AUTHZ_DENIED, HOLD_INVALID, IDEMPOTENCY_KEY_REUSED, LEGAL_HOLD_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-LHD-REQUEST-RELEASE | AGG-LEGAL-HOLD | `POST /api/v1/governance/legal-holds/{id}/actions/request-release` | لا | Legal/Compliance authority (place, extend, request/approve/cancel release) | POL-LHD-REQUEST-RELEASE | `reason!:string` | EVT-LHD-RELEASE-REQUESTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LEGAL_HOLD_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-LHD-APPROVE-RELEASE | AGG-LEGAL-HOLD | `POST /api/v1/governance/legal-holds/{id}/actions/approve-release` | لا | Legal/Compliance authority (place, extend, request/approve/cancel release) | POL-LHD-APPROVE-RELEASE | `note:string` | EVT-LHD-RELEASED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LEGAL_HOLD_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-LHD-CANCEL-RELEASE | AGG-LEGAL-HOLD | `POST /api/v1/governance/legal-holds/{id}/actions/cancel-release` | لا | Legal/Compliance authority (place, extend, request/approve/cancel release) | POL-LHD-CANCEL-RELEASE | `reason!:string` | EVT-LHD-RELEASE-CANCELLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LEGAL_HOLD_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DSP-SUBMIT | AGG-DISPOSITION-RUN | `POST /api/v1/governance/disposition-runs/{id}/actions/submit` | لا | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve) | POL-DSP-SUBMIT | `note:string` | EVT-DSP-SUBMITTED | AUTHZ_DENIED, DISPOSITION_RUN_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DSP-APPROVE | AGG-DISPOSITION-RUN | `POST /api/v1/governance/disposition-runs/{id}/actions/approve` | لا | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve) | POL-DSP-APPROVE | `note:string` | EVT-DSP-APPROVED | AUTHZ_DENIED, DISPOSITION_RUN_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DSP-CANCEL | AGG-DISPOSITION-RUN | `POST /api/v1/governance/disposition-runs/{id}/actions/cancel` | لا | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve) | POL-DSP-CANCEL | `reason!:string` | EVT-DSP-CANCELLED | AUTHZ_DENIED, DISPOSITION_RUN_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ERS-REGISTER | AGG-ERASURE-REQUEST | `POST /api/v1/governance/erasure-requests` | لا | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject) | POL-ERS-REGISTER | `legal_basis!:string person:urn entities:array requester!:string` | EVT-ERS-RECEIVED | AUTHZ_DENIED, ERASURE_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ERS-APPROVE | AGG-ERASURE-REQUEST | `POST /api/v1/governance/erasure-requests/{id}/actions/approve` | لا | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject) | POL-ERS-APPROVE | `decision_note!:string` | EVT-ERS-APPROVED | AUTHZ_DENIED, ERASURE_REQUEST_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ERS-REJECT | AGG-ERASURE-REQUEST | `POST /api/v1/governance/erasure-requests/{id}/actions/reject` | لا | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject) | POL-ERS-REJECT | `reason!:string` | EVT-ERS-REJECTED | AUTHZ_DENIED, ERASURE_REQUEST_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-RTS-DRAFT
  aggregate: AGG-RETENTION-SCHEDULE
  bc: BC08
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: Archivist; ≤ 1 DRAFT per tenant
    event: EVT-RTS-DRAFTED
  errors:
  - AUTHZ_DENIED
  - DRAFT_EXISTS
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/governance/retention-schedules
  internal: false
  policy: POL-RTS-DRAFT
  actors: Archivist (draft, edit, discard) · Legal/Compliance authority (activate)
  payload: based_on:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-RTS-EDIT
  aggregate: AGG-RETENTION-SCHEDULE
  bc: BC08
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: 'each rule: record class (RD-RECORD-CLASSES), period (ISO 8601 duration),
      trigger ∈ {recorded, closed, superseded, event}, action ∈ {DESTROY, REVIEW,
      ARCHIVE (R2)}, legal basis'
    event: EVT-RTS-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RETENTION_SCHEDULE_INVALID_STATE_TRANSITION
  - SCHEDULE_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/retention-schedules/{id}/actions/edit
  internal: false
  policy: POL-RTS-EDIT
  actors: Archivist (draft, edit, discard) · Legal/Compliance authority (activate)
  payload: rules!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RTS-ACTIVATE
  aggregate: AGG-RETENTION-SCHEDULE
  bc: BC08
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: every record class in RD-RECORD-CLASSES has exactly one rule (REQ-GOV-006);
      approver = Legal/Compliance authority ≠ drafter; previous ACTIVE → SUPERSEDED
      in the same transaction
    event: EVT-RTS-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RETENTION_SCHEDULE_INVALID_STATE_TRANSITION
  - SCHEDULE_INCOMPLETE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/retention-schedules/{id}/actions/activate
  internal: false
  policy: POL-RTS-ACTIVATE
  actors: Archivist (draft, edit, discard) · Legal/Compliance authority (activate)
  payload: effective_from!:date-time retroactive_classes:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RTS-DISCARD
  aggregate: AGG-RETENTION-SCHEDULE
  bc: BC08
  transitions:
  - from:
    - DRAFT
    to: DISCARDED
    guard: reason
    event: EVT-RTS-DISCARDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - RETENTION_SCHEDULE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/retention-schedules/{id}/actions/discard
  internal: false
  policy: POL-RTS-DISCARD
  actors: Archivist (draft, edit, discard) · Legal/Compliance authority (activate)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-LHD-PLACE
  aggregate: AGG-LEGAL-HOLD
  bc: BC08
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: 'Legal/Compliance authority; scope = any of: record classes, object URNs,
      data subjects, org units, time range; legal reference'
    event: EVT-LHD-PLACED
  errors:
  - AUTHZ_DENIED
  - HOLD_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/governance/legal-holds
  internal: false
  policy: POL-LHD-PLACE
  actors: Legal/Compliance authority (place, extend, request/approve/cancel release)
  payload: name!:string legal_reference!:string scope!:array
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-LHD-EXTEND
  aggregate: AGG-LEGAL-HOLD
  bc: BC08
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: added scope items; reason
    event: EVT-LHD-EXTENDED
  errors:
  - AUTHZ_DENIED
  - HOLD_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - LEGAL_HOLD_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/legal-holds/{id}/actions/extend
  internal: false
  policy: POL-LHD-EXTEND
  actors: Legal/Compliance authority (place, extend, request/approve/cancel release)
  payload: scope!:array reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-LHD-REQUEST-RELEASE
  aggregate: AGG-LEGAL-HOLD
  bc: BC08
  transitions:
  - from:
    - ACTIVE
    to: RELEASE_REQUESTED
    guard: reason; requester = Legal authority
    event: EVT-LHD-RELEASE-REQUESTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LEGAL_HOLD_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/legal-holds/{id}/actions/request-release
  internal: false
  policy: POL-LHD-REQUEST-RELEASE
  actors: Legal/Compliance authority (place, extend, request/approve/cancel release)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-LHD-APPROVE-RELEASE
  aggregate: AGG-LEGAL-HOLD
  bc: BC08
  transitions:
  - from:
    - RELEASE_REQUESTED
    to: RELEASED
    guard: second Legal authority ≠ requester
    event: EVT-LHD-RELEASED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LEGAL_HOLD_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/legal-holds/{id}/actions/approve-release
  internal: false
  policy: POL-LHD-APPROVE-RELEASE
  actors: Legal/Compliance authority (place, extend, request/approve/cancel release)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-LHD-CANCEL-RELEASE
  aggregate: AGG-LEGAL-HOLD
  bc: BC08
  transitions:
  - from:
    - RELEASE_REQUESTED
    to: ACTIVE
    guard: reason
    event: EVT-LHD-RELEASE-CANCELLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LEGAL_HOLD_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/legal-holds/{id}/actions/cancel-release
  internal: false
  policy: POL-LHD-CANCEL-RELEASE
  actors: Legal/Compliance authority (place, extend, request/approve/cancel release)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DSP-SUBMIT
  aggregate: AGG-DISPOSITION-RUN
  bc: BC08
  transitions:
  - from:
    - PLANNED
    to: AWAITING_APPROVAL
    guard: Archivist reviewed candidate summary (counts per class/bucket, REVIEW-action
      items listed)
    event: EVT-DSP-SUBMITTED
  errors:
  - AUTHZ_DENIED
  - DISPOSITION_RUN_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/disposition-runs/{id}/actions/submit
  internal: false
  policy: POL-DSP-SUBMIT
  actors: Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DSP-APPROVE
  aggregate: AGG-DISPOSITION-RUN
  bc: BC08
  transitions:
  - from:
    - AWAITING_APPROVAL
    to: APPROVED
    guard: approver = Records/Legal authority ≠ submitter; re-run HoldCheck at approval
    event: EVT-DSP-APPROVED
  errors:
  - AUTHZ_DENIED
  - DISPOSITION_RUN_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/disposition-runs/{id}/actions/approve
  internal: false
  policy: POL-DSP-APPROVE
  actors: Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DSP-CANCEL
  aggregate: AGG-DISPOSITION-RUN
  bc: BC08
  transitions:
  - from:
    - PLANNED
    - AWAITING_APPROVAL
    - APPROVED
    to: CANCELLED
    guard: reason
    event: EVT-DSP-CANCELLED
  errors:
  - AUTHZ_DENIED
  - DISPOSITION_RUN_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/disposition-runs/{id}/actions/cancel
  internal: false
  policy: POL-DSP-CANCEL
  actors: Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ERS-REGISTER
  aggregate: AGG-ERASURE-REQUEST
  bc: BC08
  transitions:
  - from:
    - ∅
    to: RECEIVED
    guard: legal basis reference; subject identification (platform person URN and/or
      information entity URNs of type person); requester
    event: EVT-ERS-RECEIVED
  errors:
  - AUTHZ_DENIED
  - ERASURE_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/governance/erasure-requests
  internal: false
  policy: POL-ERS-REGISTER
  actors: Privacy officer / Legal (register) · Legal authority ≠ registrar (approve,
    reject)
  payload: legal_basis!:string person:urn entities:array requester!:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ERS-APPROVE
  aggregate: AGG-ERASURE-REQUEST
  bc: BC08
  transitions:
  - from:
    - SCOPED
    to: APPROVED
    guard: Legal/Compliance authority ≠ registrar; decision recorded with basis
    event: EVT-ERS-APPROVED
  errors:
  - AUTHZ_DENIED
  - ERASURE_REQUEST_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/erasure-requests/{id}/actions/approve
  internal: false
  policy: POL-ERS-APPROVE
  actors: Privacy officer / Legal (register) · Legal authority ≠ registrar (approve,
    reject)
  payload: decision_note!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ERS-REJECT
  aggregate: AGG-ERASURE-REQUEST
  bc: BC08
  transitions:
  - from:
    - SCOPED
    to: REJECTED
    guard: reason (e.g. legal obligation to retain)
    event: EVT-ERS-REJECTED
  errors:
  - AUTHZ_DENIED
  - ERASURE_REQUEST_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/erasure-requests/{id}/actions/reject
  internal: false
  policy: POL-ERS-REJECT
  actors: Privacy officer / Legal (register) · Legal authority ≠ registrar (approve,
    reject)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
