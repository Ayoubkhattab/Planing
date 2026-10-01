---
id: CMD-CAT-BC02-SLC15
type: command-catalog
title: Commands — BC02 (SLC-15)
wave: W4
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC02 (SLC-15)

_8 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-CRP-PROPOSE | AGG-CORRELATION-PROPOSAL | `POST /api/v1/information/correlation-proposals` | لا | Analyst (propose, review, accept, reject) | POL-CRP-PROPOSE | `kind!:enum(same_event,co_location,track_association,same_entity_hint) inputs!:array rationale!:string` | EVT-CRP-PROPOSED | AUTHZ_DENIED, CORRELATION_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRP-START-REVIEW | AGG-CORRELATION-PROPOSAL | `POST /api/v1/information/correlation-proposals/{id}/actions/start-review` | لا | Analyst (propose, review, accept, reject) | POL-CRP-START-REVIEW | `—` | EVT-CRP-REVIEW-STARTED | AUTHZ_DENIED, CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REVIEWER_NOT_CLEARED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRP-ACCEPT | AGG-CORRELATION-PROPOSAL | `POST /api/v1/information/correlation-proposals/{id}/actions/accept` | لا | Analyst (propose, review, accept, reject) | POL-CRP-ACCEPT | `note:string` | EVT-CRP-ACCEPTED | AUTHZ_DENIED, CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, OWNER_REJECTED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRP-REJECT | AGG-CORRELATION-PROPOSAL | `POST /api/v1/information/correlation-proposals/{id}/actions/reject` | لا | Analyst (propose, review, accept, reject) | POL-CRP-REJECT | `reason!:string` | EVT-CRP-REJECTED | AUTHZ_DENIED, CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRR-DEFINE | AGG-CORRELATION-RULE | `POST /api/v1/information/correlation-rules` | لا | Analyst lead (define, edit) · second approver (activate) | POL-CRR-DEFINE | `kind!:enum(same_event,co_location,track_association,same_entity_hint) name!:string` | EVT-CRR-DEFINED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RULE_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRR-EDIT | AGG-CORRELATION-RULE | `POST /api/v1/information/correlation-rules/{id}/actions/edit` | لا | Analyst lead (define, edit) · second approver (activate) | POL-CRR-EDIT | `parameters!:object` | EVT-CRR-EDITED | AUTHZ_DENIED, CORRELATION_RULE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, RULE_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRR-ACTIVATE | AGG-CORRELATION-RULE | `POST /api/v1/information/correlation-rules/{id}/actions/activate` | لا | Analyst lead (define, edit) · second approver (activate) | POL-CRR-ACTIVATE | `evaluation_report!:urn` | EVT-CRR-ACTIVATED | AUTHZ_DENIED, CORRELATION_RULE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, RULE_BELOW_TARGET, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CRR-RETIRE | AGG-CORRELATION-RULE | `POST /api/v1/information/correlation-rules/{id}/actions/retire` | لا | Analyst lead | POL-CRR-RETIRE | `reason!:string` | EVT-CRR-RETIRED | AUTHZ_DENIED, CORRELATION_RULE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-CRP-PROPOSE
  aggregate: AGG-CORRELATION-PROPOSAL
  bc: BC02
  transitions:
  - from:
    - ∅
    to: PROPOSED
    guard: analyst; ≥ 2 visible inputs; kind; rationale
    event: EVT-CRP-PROPOSED
  errors:
  - AUTHZ_DENIED
  - CORRELATION_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/correlation-proposals
  internal: false
  policy: POL-CRP-PROPOSE
  actors: Analyst (propose, review, accept, reject)
  payload: kind!:enum(same_event,co_location,track_association,same_entity_hint) inputs!:array
    rationale!:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CRP-START-REVIEW
  aggregate: AGG-CORRELATION-PROPOSAL
  bc: BC02
  transitions:
  - from:
    - PROPOSED
    to: UNDER_REVIEW
    guard: reviewer cleared for every input label
    event: EVT-CRP-REVIEW-STARTED
  errors:
  - AUTHZ_DENIED
  - CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REVIEWER_NOT_CLEARED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/correlation-proposals/{id}/actions/start-review
  internal: false
  policy: POL-CRP-START-REVIEW
  actors: Analyst (propose, review, accept, reject)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRP-ACCEPT
  aggregate: AGG-CORRELATION-PROPOSAL
  bc: BC02
  transitions:
  - from:
    - UNDER_REVIEW
    to: ACCEPTED
    guard: 'effects through owner commands as the reviewer: same_event → Real-World
      Event + participation relationships + fused claims; co_location → relationship;
      same_entity → ER case (SLC-04); lineage lists every contributing source and
      its reliability'
    event: EVT-CRP-ACCEPTED
  errors:
  - AUTHZ_DENIED
  - CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - OWNER_REJECTED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/correlation-proposals/{id}/actions/accept
  internal: false
  policy: POL-CRP-ACCEPT
  actors: Analyst (propose, review, accept, reject)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRP-REJECT
  aggregate: AGG-CORRELATION-PROPOSAL
  bc: BC02
  transitions:
  - from:
    - UNDER_REVIEW
    - PROPOSED
    to: REJECTED
    guard: reason (feeds rule evaluation)
    event: EVT-CRP-REJECTED
  errors:
  - AUTHZ_DENIED
  - CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/correlation-proposals/{id}/actions/reject
  internal: false
  policy: POL-CRP-REJECT
  actors: Analyst (propose, review, accept, reject)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRR-DEFINE
  aggregate: AGG-CORRELATION-RULE
  bc: BC02
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: kind ∈ {same_event, co_location, track_association, same_entity_hint}
    event: EVT-CRR-DEFINED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RULE_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/correlation-rules
  internal: false
  policy: POL-CRR-DEFINE
  actors: Analyst lead (define, edit) · second approver (activate)
  payload: kind!:enum(same_event,co_location,track_association,same_entity_hint) name!:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CRR-EDIT
  aggregate: AGG-CORRELATION-RULE
  bc: BC02
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    to: '='
    guard: 'parameters: max distance (m, accuracy-aware), time window, attribute similarity,
      min distinct sources, threshold; ACTIVE → new version'
    event: EVT-CRR-EDITED
  errors:
  - AUTHZ_DENIED
  - CORRELATION_RULE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - RULE_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/correlation-rules/{id}/actions/edit
  internal: false
  policy: POL-CRR-EDIT
  actors: Analyst lead (define, edit) · second approver (activate)
  payload: parameters!:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRR-ACTIVATE
  aggregate: AGG-CORRELATION-RULE
  bc: BC02
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: 'evaluation on a labelled set: precision ≥ 70 % of proposals (recalibrate
      after pilot); approver ≠ author'
    event: EVT-CRR-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - CORRELATION_RULE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - RULE_BELOW_TARGET
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/correlation-rules/{id}/actions/activate
  internal: false
  policy: POL-CRR-ACTIVATE
  actors: Analyst lead (define, edit) · second approver (activate)
  payload: evaluation_report!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CRR-RETIRE
  aggregate: AGG-CORRELATION-RULE
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    to: RETIRED
    guard: reason
    event: EVT-CRR-RETIRED
  errors:
  - AUTHZ_DENIED
  - CORRELATION_RULE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/correlation-rules/{id}/actions/retire
  internal: false
  policy: POL-CRR-RETIRE
  actors: Analyst lead
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
