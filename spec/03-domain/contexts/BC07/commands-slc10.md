---
id: CMD-CAT-BC07-SLC10
type: command-catalog
title: Commands — BC07 (SLC-10)
wave: W4
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC07 (SLC-10)

_27 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-AIR-SUBMIT | AGG-AI-REQUEST | `POST /api/v1/ai/requests` | لا | any authorized user (submit, cancel) | POL-AIR-SUBMIT | `operation!:string input!:LocalizedName scope:object purpose!:string target:urn` | EVT-AIR-RECEIVED | AI_OPERATION_NOT_ALLOWED, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AIR-CANCEL | AGG-AI-REQUEST | `POST /api/v1/ai/requests/{id}/actions/cancel` | لا | any authorized user (submit, cancel) | POL-AIR-CANCEL | `—` | EVT-AIR-CANCELLED | AI_REQUEST_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AIRS-START-REVIEW | AGG-AI-RESULT | `POST /api/v1/ai/results/{id}/actions/start-review` | لا | reviewer authorized on the target (review, accept, reject) | POL-AIRS-START-REVIEW | `—` | EVT-AIRS-REVIEW-STARTED | AI_RESULT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REVIEWER_NOT_CLEARED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AIRS-ACCEPT | AGG-AI-RESULT | `POST /api/v1/ai/results/{id}/actions/accept` | لا | reviewer authorized on the target (review, accept, reject) | POL-AIRS-ACCEPT | `note:string` | EVT-AIRS-ACCEPTED | AI_RESULT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OWNER_REJECTED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AIRS-ACCEPT-PARTIALLY | AGG-AI-RESULT | `POST /api/v1/ai/results/{id}/actions/accept-partially` | لا | reviewer authorized on the target (review, accept, reject) | POL-AIRS-ACCEPT-PARTIALLY | `accepted_items!:array rejected_items!:array` | EVT-AIRS-PARTIALLY-ACCEPTED | AI_RESULT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OWNER_REJECTED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AIRS-REJECT | AGG-AI-RESULT | `POST /api/v1/ai/results/{id}/actions/reject` | لا | reviewer authorized on the target (review, accept, reject) | POL-AIRS-REJECT | `reason!:string` | EVT-AIRS-REJECTED | AI_RESULT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MDL-REGISTER | AGG-MODEL-VERSION | `POST /api/v1/ai/models` | لا | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-REGISTER | `family!:string version!:string weights_digest!:string licence!:string languages!:array context_tokens!:integer hosting!:enum(local,external_allowed) roles!:array` | EVT-MDL-REGISTERED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MODEL_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MDL-START-EVALUATION | AGG-MODEL-VERSION | `POST /api/v1/ai/models/{id}/actions/start-evaluation` | لا | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-START-EVALUATION | `suite!:urn` | EVT-MDL-EVALUATION-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MODEL_VERSION_INVALID_STATE_TRANSITION, SUITE_NOT_ACTIVE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MDL-APPROVE | AGG-MODEL-VERSION | `POST /api/v1/ai/models/{id}/actions/approve` | لا | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-APPROVE | `report!:urn` | EVT-MDL-APPROVED | AUTHZ_DENIED, EVALUATION_BELOW_THRESHOLD, IDEMPOTENCY_KEY_REUSED, MODEL_VERSION_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MDL-FAIL-EVALUATION | AGG-MODEL-VERSION | `POST /api/v1/ai/models/{id}/actions/fail-evaluation` | لا | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-FAIL-EVALUATION | `report!:urn` | EVT-MDL-EVALUATION-FAILED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MODEL_VERSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MDL-STAGE | AGG-MODEL-VERSION | `POST /api/v1/ai/models/{id}/actions/stage` | لا | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-STAGE | `canary_share!:number operations!:array` | EVT-MDL-STAGED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MODEL_VERSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MDL-PROMOTE | AGG-MODEL-VERSION | `POST /api/v1/ai/models/{id}/actions/promote` | لا | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-PROMOTE | `canary_report!:urn` | EVT-MDL-PROMOTED | AUTHZ_DENIED, CANARY_BELOW_THRESHOLD, IDEMPOTENCY_KEY_REUSED, MODEL_VERSION_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MDL-DEPRECATE | AGG-MODEL-VERSION | `POST /api/v1/ai/models/{id}/actions/deprecate` | لا | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-DEPRECATE | `reason!:string` | EVT-MDL-DEPRECATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MODEL_IN_ACTIVE_ROUTE, MODEL_VERSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MDL-REINSTATE | AGG-MODEL-VERSION | `POST /api/v1/ai/models/{id}/actions/reinstate` | لا | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | POL-MDL-REINSTATE | `reason!:string` | EVT-MDL-REINSTATED | AUTHZ_DENIED, EVALUATION_TOO_OLD, IDEMPOTENCY_KEY_REUSED, MODEL_VERSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MDL-RETIRE | AGG-MODEL-VERSION | `POST /api/v1/ai/models/{id}/actions/retire` | لا | AI governance authority | POL-MDL-RETIRE | `reason!:string` | EVT-MDL-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MODEL_VERSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RTG-DRAFT | AGG-AI-ROUTING | `POST /api/v1/ai/routings` | لا | AI governance authority (draft, edit) · second authority (activate) | POL-RTG-DRAFT | `based_on:urn` | EVT-RTG-DRAFTED | AUTHZ_DENIED, DRAFT_EXISTS, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RTG-EDIT | AGG-AI-ROUTING | `POST /api/v1/ai/routings/{id}/actions/edit` | لا | AI governance authority (draft, edit) · second authority (activate) | POL-RTG-EDIT | `routes!:array` | EVT-RTG-EDITED | AI_ROUTING_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ROUTING_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RTG-ACTIVATE | AGG-AI-ROUTING | `POST /api/v1/ai/routings/{id}/actions/activate` | لا | AI governance authority (draft, edit) · second authority (activate) | POL-RTG-ACTIVATE | `—` | EVT-RTG-ACTIVATED | AI_ROUTING_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RTG-DISCARD | AGG-AI-ROUTING | `POST /api/v1/ai/routings/{id}/actions/discard` | لا | AI governance authority (draft, edit) · second authority (activate) | POL-RTG-DISCARD | `reason!:string` | EVT-RTG-DISCARDED | AI_ROUTING_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TOL-REGISTER | AGG-AI-TOOL | `POST /api/v1/ai/tools` | لا | AI platform engineer (register) · Security Officer (activate, disable) | POL-TOL-REGISTER | `name!:string description!:LocalizedName input_schema!:object binding!:string effect!:enum(read,propose) permission!:string max_ail!:integer` | EVT-TOL-REGISTERED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TOOL_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TOL-ACTIVATE | AGG-AI-TOOL | `POST /api/v1/ai/tools/{id}/actions/activate` | لا | AI platform engineer (register) · Security Officer (activate, disable) | POL-TOL-ACTIVATE | `review_ref!:string` | EVT-TOL-ACTIVATED | AI_TOOL_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SECURITY_REVIEW_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TOL-DISABLE | AGG-AI-TOOL | `POST /api/v1/ai/tools/{id}/actions/disable` | لا | AI platform engineer (register) · Security Officer (activate, disable) | POL-TOL-DISABLE | `reason!:string` | EVT-TOL-DISABLED | AI_TOOL_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TOL-ENABLE | AGG-AI-TOOL | `POST /api/v1/ai/tools/{id}/actions/enable` | لا | Security Officer | POL-TOL-ENABLE | `—` | EVT-TOL-ENABLED | AI_TOOL_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TOL-RETIRE | AGG-AI-TOOL | `POST /api/v1/ai/tools/{id}/actions/retire` | لا | Security Officer | POL-TOL-RETIRE | `reason!:string` | EVT-TOL-RETIRED | AI_TOOL_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVS-DRAFT | AGG-EVAL-SUITE | `POST /api/v1/ai/evaluation-suites` | لا | AI governance (draft, edit) · second authority (activate) | POL-EVS-DRAFT | `based_on:urn` | EVT-EVS-DRAFTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVS-EDIT | AGG-EVAL-SUITE | `POST /api/v1/ai/evaluation-suites/{id}/actions/edit` | لا | AI governance (draft, edit) · second authority (activate) | POL-EVS-EDIT | `sets!:array` | EVT-EVS-EDITED | AUTHZ_DENIED, EVAL_SUITE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SUITE_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVS-ACTIVATE | AGG-EVAL-SUITE | `POST /api/v1/ai/evaluation-suites/{id}/actions/activate` | لا | AI governance (draft, edit) · second authority (activate) | POL-EVS-ACTIVATE | `—` | EVT-EVS-ACTIVATED | AUTHZ_DENIED, EVAL_SUITE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-AIR-SUBMIT
  aggregate: AGG-AI-REQUEST
  bc: BC07
  transitions:
  - from:
    - ∅
    to: RECEIVED
    guard: operation ∈ AI autonomy matrix and allowed at the tenant's routing; user
      authenticated; purpose; input size ≤ limit; per-tenant AI quota
    event: EVT-AIR-RECEIVED
  errors:
  - AI_OPERATION_NOT_ALLOWED
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/ai/requests
  internal: false
  policy: POL-AIR-SUBMIT
  actors: any authorized user (submit, cancel)
  payload: operation!:string input!:LocalizedName scope:object purpose!:string target:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-AIR-CANCEL
  aggregate: AGG-AI-REQUEST
  bc: BC07
  transitions:
  - from:
    - RECEIVED
    - RETRIEVING
    - GENERATING
    to: CANCELLED
    guard: requester
    event: EVT-AIR-CANCELLED
  errors:
  - AI_REQUEST_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/requests/{id}/actions/cancel
  internal: false
  policy: POL-AIR-CANCEL
  actors: any authorized user (submit, cancel)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AIRS-START-REVIEW
  aggregate: AGG-AI-RESULT
  bc: BC07
  transitions:
  - from:
    - PROPOSED
    to: UNDER_REVIEW
    guard: reviewer authorized for the target and cleared for the result label
    event: EVT-AIRS-REVIEW-STARTED
  errors:
  - AI_RESULT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REVIEWER_NOT_CLEARED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/results/{id}/actions/start-review
  internal: false
  policy: POL-AIRS-START-REVIEW
  actors: reviewer authorized on the target (review, accept, reject)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AIRS-ACCEPT
  aggregate: AGG-AI-RESULT
  bc: BC07
  transitions:
  - from:
    - UNDER_REVIEW
    to: ACCEPTED
    guard: effects applied through owner commands as the reviewer, with agent = model
      version in lineage (e.g. CMD-CLM-ASSERT, product section, CMD-ER-PROPOSE)
    event: EVT-AIRS-ACCEPTED
  errors:
  - AI_RESULT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OWNER_REJECTED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/results/{id}/actions/accept
  internal: false
  policy: POL-AIRS-ACCEPT
  actors: reviewer authorized on the target (review, accept, reject)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AIRS-ACCEPT-PARTIALLY
  aggregate: AGG-AI-RESULT
  bc: BC07
  transitions:
  - from:
    - UNDER_REVIEW
    to: PARTIALLY_ACCEPTED
    guard: selected items only; rejected items recorded with reasons
    event: EVT-AIRS-PARTIALLY-ACCEPTED
  errors:
  - AI_RESULT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OWNER_REJECTED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/results/{id}/actions/accept-partially
  internal: false
  policy: POL-AIRS-ACCEPT-PARTIALLY
  actors: reviewer authorized on the target (review, accept, reject)
  payload: accepted_items!:array rejected_items!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AIRS-REJECT
  aggregate: AGG-AI-RESULT
  bc: BC07
  transitions:
  - from:
    - PROPOSED
    - UNDER_REVIEW
    to: REJECTED
    guard: reason (feeds evaluation)
    event: EVT-AIRS-REJECTED
  errors:
  - AI_RESULT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/results/{id}/actions/reject
  internal: false
  policy: POL-AIRS-REJECT
  actors: reviewer authorized on the target (review, accept, reject)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MDL-REGISTER
  aggregate: AGG-MODEL-VERSION
  bc: BC07
  transitions:
  - from:
    - ∅
    to: REGISTERED
    guard: family, version, weights digest in internal registry, licence reviewed,
      languages (must include ar and en for generative roles), context size, hosting
      ∈ {local, external_allowed}
    event: EVT-MDL-REGISTERED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MODEL_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/ai/models
  internal: false
  policy: POL-MDL-REGISTER
  actors: AI platform engineer (register, evaluate, stage, deprecate) · AI governance
    authority (approve, promote, reinstate)
  payload: family!:string version!:string weights_digest!:string licence!:string languages!:array
    context_tokens!:integer hosting!:enum(local,external_allowed) roles!:array
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-MDL-START-EVALUATION
  aggregate: AGG-MODEL-VERSION
  bc: BC07
  transitions:
  - from:
    - REGISTERED
    to: EVALUATING
    guard: evaluation suite ACTIVE (AGG-EVAL-SUITE)
    event: EVT-MDL-EVALUATION-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MODEL_VERSION_INVALID_STATE_TRANSITION
  - SUITE_NOT_ACTIVE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/models/{id}/actions/start-evaluation
  internal: false
  policy: POL-MDL-START-EVALUATION
  actors: AI platform engineer (register, evaluate, stage, deprecate) · AI governance
    authority (approve, promote, reinstate)
  payload: suite!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MDL-APPROVE
  aggregate: AGG-MODEL-VERSION
  bc: BC07
  transitions:
  - from:
    - EVALUATING
    to: APPROVED
    guard: 'report meets thresholds: citation accuracy ≥ 95 %, hallucination ≤ 2 %,
      insufficient-evidence recall ≥ 95 %, 0 injection/exfiltration successes, latency
      and cost recorded (REQ-AI-010); AI governance authority ≠ registrar'
    event: EVT-MDL-APPROVED
  errors:
  - AUTHZ_DENIED
  - EVALUATION_BELOW_THRESHOLD
  - IDEMPOTENCY_KEY_REUSED
  - MODEL_VERSION_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/models/{id}/actions/approve
  internal: false
  policy: POL-MDL-APPROVE
  actors: AI platform engineer (register, evaluate, stage, deprecate) · AI governance
    authority (approve, promote, reinstate)
  payload: report!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MDL-FAIL-EVALUATION
  aggregate: AGG-MODEL-VERSION
  bc: BC07
  transitions:
  - from:
    - EVALUATING
    to: EVALUATION_FAILED
    guard: report attached
    event: EVT-MDL-EVALUATION-FAILED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MODEL_VERSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/models/{id}/actions/fail-evaluation
  internal: false
  policy: POL-MDL-FAIL-EVALUATION
  actors: AI platform engineer (register, evaluate, stage, deprecate) · AI governance
    authority (approve, promote, reinstate)
  payload: report!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MDL-STAGE
  aggregate: AGG-MODEL-VERSION
  bc: BC07
  transitions:
  - from:
    - APPROVED
    to: STAGED
    guard: canary share ≤ 10 % of the target operations
    event: EVT-MDL-STAGED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MODEL_VERSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/models/{id}/actions/stage
  internal: false
  policy: POL-MDL-STAGE
  actors: AI platform engineer (register, evaluate, stage, deprecate) · AI governance
    authority (approve, promote, reinstate)
  payload: canary_share!:number operations!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MDL-PROMOTE
  aggregate: AGG-MODEL-VERSION
  bc: BC07
  transitions:
  - from:
    - STAGED
    to: PRODUCTION
    guard: canary metrics within thresholds for ≥ 7 days; approver ≠ stager
    event: EVT-MDL-PROMOTED
  errors:
  - AUTHZ_DENIED
  - CANARY_BELOW_THRESHOLD
  - IDEMPOTENCY_KEY_REUSED
  - MODEL_VERSION_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/models/{id}/actions/promote
  internal: false
  policy: POL-MDL-PROMOTE
  actors: AI platform engineer (register, evaluate, stage, deprecate) · AI governance
    authority (approve, promote, reinstate)
  payload: canary_report!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MDL-DEPRECATE
  aggregate: AGG-MODEL-VERSION
  bc: BC07
  transitions:
  - from:
    - PRODUCTION
    - STAGED
    - APPROVED
    to: DEPRECATED
    guard: reason; routes using it must be switched first
    event: EVT-MDL-DEPRECATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MODEL_IN_ACTIVE_ROUTE
  - MODEL_VERSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/models/{id}/actions/deprecate
  internal: false
  policy: POL-MDL-DEPRECATE
  actors: AI platform engineer (register, evaluate, stage, deprecate) · AI governance
    authority (approve, promote, reinstate)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MDL-REINSTATE
  aggregate: AGG-MODEL-VERSION
  bc: BC07
  transitions:
  - from:
    - DEPRECATED
    to: PRODUCTION
    guard: rollback; evaluation ≤ 90 days old
    event: EVT-MDL-REINSTATED
  errors:
  - AUTHZ_DENIED
  - EVALUATION_TOO_OLD
  - IDEMPOTENCY_KEY_REUSED
  - MODEL_VERSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/models/{id}/actions/reinstate
  internal: false
  policy: POL-MDL-REINSTATE
  actors: AI platform engineer (register, evaluate, stage, deprecate) · AI governance
    authority (approve, promote, reinstate)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MDL-RETIRE
  aggregate: AGG-MODEL-VERSION
  bc: BC07
  transitions:
  - from:
    - DEPRECATED
    to: RETIRED
    guard: weights archived (cold) if referenced by lineage of accepted results; record
      kept
    event: EVT-MDL-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MODEL_VERSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/models/{id}/actions/retire
  internal: false
  policy: POL-MDL-RETIRE
  actors: AI governance authority
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RTG-DRAFT
  aggregate: AGG-AI-ROUTING
  bc: BC07
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: AI governance authority; ≤ 1 DRAFT per tenant
    event: EVT-RTG-DRAFTED
  errors:
  - AUTHZ_DENIED
  - DRAFT_EXISTS
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/ai/routings
  internal: false
  policy: POL-RTG-DRAFT
  actors: AI governance authority (draft, edit) · second authority (activate)
  payload: based_on:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-RTG-EDIT
  aggregate: AGG-AI-ROUTING
  bc: BC07
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: 'for each operation: model version in PRODUCTION (or STAGED with canary
      share), prompt template version, allowed tools, max AIL ≤ autonomy matrix, external
      model allowed only for unclassified and only if tenant policy allows'
    event: EVT-RTG-EDITED
  errors:
  - AI_ROUTING_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ROUTING_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/routings/{id}/actions/edit
  internal: false
  policy: POL-RTG-EDIT
  actors: AI governance authority (draft, edit) · second authority (activate)
  payload: routes!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RTG-ACTIVATE
  aggregate: AGG-AI-ROUTING
  bc: BC07
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: approver ≠ author; previous ACTIVE → SUPERSEDED
    event: EVT-RTG-ACTIVATED
  errors:
  - AI_ROUTING_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/routings/{id}/actions/activate
  internal: false
  policy: POL-RTG-ACTIVATE
  actors: AI governance authority (draft, edit) · second authority (activate)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RTG-DISCARD
  aggregate: AGG-AI-ROUTING
  bc: BC07
  transitions:
  - from:
    - DRAFT
    to: DISCARDED
    guard: reason
    event: EVT-RTG-DISCARDED
  errors:
  - AI_ROUTING_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/routings/{id}/actions/discard
  internal: false
  policy: POL-RTG-DISCARD
  actors: AI governance authority (draft, edit) · second authority (activate)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TOL-REGISTER
  aggregate: AGG-AI-TOOL
  bc: BC07
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: name; input JSON schema; underlying platform query or command; effect ∈
      {read, propose}; required permission; max AIL
    event: EVT-TOL-REGISTERED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TOOL_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/ai/tools
  internal: false
  policy: POL-TOL-REGISTER
  actors: AI platform engineer (register) · Security Officer (activate, disable)
  payload: name!:string description!:LocalizedName input_schema!:object binding!:string
    effect!:enum(read,propose) permission!:string max_ail!:integer
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-TOL-ACTIVATE
  aggregate: AGG-AI-TOOL
  bc: BC07
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: security review passed (injection, exfiltration, scope); approver = Security
      Officer
    event: EVT-TOL-ACTIVATED
  errors:
  - AI_TOOL_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SECURITY_REVIEW_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/tools/{id}/actions/activate
  internal: false
  policy: POL-TOL-ACTIVATE
  actors: AI platform engineer (register) · Security Officer (activate, disable)
  payload: review_ref!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TOL-DISABLE
  aggregate: AGG-AI-TOOL
  bc: BC07
  transitions:
  - from:
    - ACTIVE
    to: DISABLED
    guard: reason
    event: EVT-TOL-DISABLED
  errors:
  - AI_TOOL_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/tools/{id}/actions/disable
  internal: false
  policy: POL-TOL-DISABLE
  actors: AI platform engineer (register) · Security Officer (activate, disable)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TOL-ENABLE
  aggregate: AGG-AI-TOOL
  bc: BC07
  transitions:
  - from:
    - DISABLED
    to: ACTIVE
    guard: —
    event: EVT-TOL-ENABLED
  errors:
  - AI_TOOL_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/tools/{id}/actions/enable
  internal: false
  policy: POL-TOL-ENABLE
  actors: Security Officer
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TOL-RETIRE
  aggregate: AGG-AI-TOOL
  bc: BC07
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    - DISABLED
    to: RETIRED
    guard: reason
    event: EVT-TOL-RETIRED
  errors:
  - AI_TOOL_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/tools/{id}/actions/retire
  internal: false
  policy: POL-TOL-RETIRE
  actors: Security Officer
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EVS-DRAFT
  aggregate: AGG-EVAL-SUITE
  bc: BC07
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: AI governance
    event: EVT-EVS-DRAFTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/ai/evaluation-suites
  internal: false
  policy: POL-EVS-DRAFT
  actors: AI governance (draft, edit) · second authority (activate)
  payload: based_on:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-EVS-EDIT
  aggregate: AGG-EVAL-SUITE
  bc: BC07
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: 'sets: groundedness (≥ 500 items), citation, insufficient-evidence, prompt-injection,
      exfiltration, cross-tenant, Arabic/English/mixed; each item labelled with expected
      behaviour'
    event: EVT-EVS-EDITED
  errors:
  - AUTHZ_DENIED
  - EVAL_SUITE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SUITE_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/evaluation-suites/{id}/actions/edit
  internal: false
  policy: POL-EVS-EDIT
  actors: AI governance (draft, edit) · second authority (activate)
  payload: sets!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EVS-ACTIVATE
  aggregate: AGG-EVAL-SUITE
  bc: BC07
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: approver ≠ author; previous ACTIVE → SUPERSEDED
    event: EVT-EVS-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - EVAL_SUITE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/ai/evaluation-suites/{id}/actions/activate
  internal: false
  policy: POL-EVS-ACTIVATE
  actors: AI governance (draft, edit) · second authority (activate)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
