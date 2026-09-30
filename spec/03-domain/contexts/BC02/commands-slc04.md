---
id: CMD-CAT-BC02-SLC04
type: command-catalog
title: Commands — BC02 (SLC-04)
wave: W4
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC02 (SLC-04)

_19 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-CNF-RAISE | AGG-CONFLICT | `POST /api/v1/information/conflicts` | لا | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-RAISE | `claims!:array predicate!:string note:string` | EVT-CNF-RAISED | AUTHZ_DENIED, CONFLICT_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CNF-ASSIGN | AGG-CONFLICT | `POST /api/v1/information/conflicts/{id}/actions/assign` | لا | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-ASSIGN | `reviewer!:urn` | EVT-CNF-ASSIGNED | AUTHZ_DENIED, CONFLICT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REVIEWER_NOT_CLEARED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CNF-START-REVIEW | AGG-CONFLICT | `POST /api/v1/information/conflicts/{id}/actions/start-review` | لا | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-START-REVIEW | `—` | EVT-CNF-REVIEW-STARTED | AUTHZ_DENIED, CONFLICT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, NOT_ASSIGNED_REVIEWER, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CNF-RESOLVE | AGG-CONFLICT | `POST /api/v1/information/conflicts/{id}/actions/resolve` | لا | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-RESOLVE | `preferred_claim!:urn rationale!:string evidence:array` | EVT-CNF-RESOLVED | AUTHZ_DENIED, CONFLICT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CNF-ACCEPT | AGG-CONFLICT | `POST /api/v1/information/conflicts/{id}/actions/accept` | لا | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-ACCEPT | `rationale!:string` | EVT-CNF-ACCEPTED | AUTHZ_DENIED, CONFLICT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CNF-REOPEN | AGG-CONFLICT | `POST /api/v1/information/conflicts/{id}/actions/reopen` | لا | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | POL-CNF-REOPEN | `reason!:string evidence:array` | EVT-CNF-REOPENED | AUTHZ_DENIED, CONFLICT_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ER-PROPOSE | AGG-ER-CASE | `POST /api/v1/information/er-cases` | لا | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-PROPOSE | `left!:urn right!:urn rationale!:string agent:urn` | EVT-ER-PROPOSED | AUTHZ_DENIED, ER_PAIR_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ER-START-REVIEW | AGG-ER-CASE | `POST /api/v1/information/er-cases/{id}/actions/start-review` | لا | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-START-REVIEW | `—` | EVT-ER-REVIEW-STARTED | AUTHZ_DENIED, ER_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REVIEWER_NOT_CLEARED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ER-DECIDE-MATCH | AGG-ER-CASE | `POST /api/v1/information/er-cases/{id}/actions/decide-match` | لا | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-DECIDE-MATCH | `rationale!:string second_reviewer:urn` | EVT-ER-MATCHED | AUTHZ_DENIED, ER_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, MATCH_CONTRADICTS_NOT_A_MATCH, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ER-DECIDE-NOT-MATCH | AGG-ER-CASE | `POST /api/v1/information/er-cases/{id}/actions/decide-not-match` | لا | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-DECIDE-NOT-MATCH | `rationale!:string` | EVT-ER-NOT-MATCHED | AUTHZ_DENIED, ER_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ER-PARK | AGG-ER-CASE | `POST /api/v1/information/er-cases/{id}/actions/park` | لا | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-PARK | `rationale!:string` | EVT-ER-PARKED | AUTHZ_DENIED, ER_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ER-RESUME | AGG-ER-CASE | `POST /api/v1/information/er-cases/{id}/actions/resume` | لا | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-RESUME | `reason!:string` | EVT-ER-RESUMED | AUTHZ_DENIED, ER_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ER-REQUEST-SPLIT | AGG-ER-CASE | `POST /api/v1/information/er-cases/{id}/actions/request-split` | لا | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-REQUEST-SPLIT | `reason!:string evidence:array` | EVT-ER-SPLIT-REQUESTED | AUTHZ_DENIED, ER_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ER-CONFIRM-MATCH | AGG-ER-CASE | `POST /api/v1/information/er-cases/{id}/actions/confirm-match` | لا | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-CONFIRM-MATCH | `rationale!:string` | EVT-ER-MATCH-CONFIRMED | AUTHZ_DENIED, ER_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ER-SPLIT | AGG-ER-CASE | `POST /api/v1/information/er-cases/{id}/actions/split` | لا | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-SPLIT | `rationale!:string record_not_a_match!:boolean` | EVT-ER-SPLIT | AUTHZ_DENIED, ER_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ER-WITHDRAW | AGG-ER-CASE | `POST /api/v1/information/er-cases/{id}/actions/withdraw` | لا | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | POL-ER-WITHDRAW | `reason!:string` | EVT-ER-WITHDRAWN | AUTHZ_DENIED, ER_CASE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MRS-DRAFT | AGG-MATCH-RULESET | `POST /api/v1/information/match-rulesets` | لا | Analyst lead (draft, edit) · Administrator ≠ author (activate) | POL-MRS-DRAFT | `entity_type!:string based_on:urn` | EVT-MRS-DRAFTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MRS-EDIT | AGG-MATCH-RULESET | `POST /api/v1/information/match-rulesets/{id}/actions/edit` | لا | Analyst lead (draft, edit) · Administrator ≠ author (activate) | POL-MRS-EDIT | `blocking_keys!:array features!:array thresholds!:object evaluation_attachment!:urn` | EVT-MRS-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MATCH_RULESET_INVALID_STATE_TRANSITION, RULESET_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-MRS-ACTIVATE | AGG-MATCH-RULESET | `POST /api/v1/information/match-rulesets/{id}/actions/activate` | لا | Analyst lead (draft, edit) · Administrator ≠ author (activate) | POL-MRS-ACTIVATE | `—` | EVT-MRS-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MATCH_RULESET_INVALID_STATE_TRANSITION, RULESET_BELOW_TARGET, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-CNF-RAISE
  aggregate: AGG-CONFLICT
  bc: BC02
  transitions:
  - from:
    - ∅
    to: OPEN
    guard: analyst names ≥ 2 visible CURRENT claims on the same cluster and predicate
      with overlapping valid time
    event: EVT-CNF-RAISED
  errors:
  - AUTHZ_DENIED
  - CONFLICT_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/conflicts
  internal: false
  policy: POL-CNF-RAISE
  actors: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  payload: claims!:array predicate!:string note:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CNF-ASSIGN
  aggregate: AGG-CONFLICT
  bc: BC02
  transitions:
  - from:
    - OPEN
    - UNDER_REVIEW
    to: '='
    guard: reviewer cleared for every member claim label
    event: EVT-CNF-ASSIGNED
  errors:
  - AUTHZ_DENIED
  - CONFLICT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REVIEWER_NOT_CLEARED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/conflicts/{id}/actions/assign
  internal: false
  policy: POL-CNF-ASSIGN
  actors: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  payload: reviewer!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CNF-START-REVIEW
  aggregate: AGG-CONFLICT
  bc: BC02
  transitions:
  - from:
    - OPEN
    to: UNDER_REVIEW
    guard: actor = assigned reviewer (or Analyst lead)
    event: EVT-CNF-REVIEW-STARTED
  errors:
  - AUTHZ_DENIED
  - CONFLICT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - NOT_ASSIGNED_REVIEWER
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/conflicts/{id}/actions/start-review
  internal: false
  policy: POL-CNF-START-REVIEW
  actors: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CNF-RESOLVE
  aggregate: AGG-CONFLICT
  bc: BC02
  transitions:
  - from:
    - UNDER_REVIEW
    to: RESOLVED
    guard: preferred claim ∈ CURRENT members; rationale; reviewer ≠ asserter of the
      preferred claim (SoD, default on); records resolution with recorded_from = now
    event: EVT-CNF-RESOLVED
  errors:
  - AUTHZ_DENIED
  - CONFLICT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/conflicts/{id}/actions/resolve
  internal: false
  policy: POL-CNF-RESOLVE
  actors: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  payload: preferred_claim!:urn rationale!:string evidence:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CNF-ACCEPT
  aggregate: AGG-CONFLICT
  bc: BC02
  transitions:
  - from:
    - UNDER_REVIEW
    to: ACCEPTED_AS_CONFLICT
    guard: rationale (both accounts shown to users)
    event: EVT-CNF-ACCEPTED
  errors:
  - AUTHZ_DENIED
  - CONFLICT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/conflicts/{id}/actions/accept
  internal: false
  policy: POL-CNF-ACCEPT
  actors: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  payload: rationale!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CNF-REOPEN
  aggregate: AGG-CONFLICT
  bc: BC02
  transitions:
  - from:
    - RESOLVED
    - ACCEPTED_AS_CONFLICT
    to: UNDER_REVIEW
    guard: new evidence or reason; closes current resolution record (recorded_to =
      now)
    event: EVT-CNF-REOPENED
  errors:
  - AUTHZ_DENIED
  - CONFLICT_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/conflicts/{id}/actions/reopen
  internal: false
  policy: POL-CNF-REOPEN
  actors: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  payload: reason!:string evidence:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ER-PROPOSE
  aggregate: AGG-ER-CASE
  bc: BC02
  transitions:
  - from:
    - ∅
    to: CANDIDATE
    guard: same conditions; proposer is Analyst or AI suggestion (AIL1, agent recorded)
    event: EVT-ER-PROPOSED
  errors:
  - AUTHZ_DENIED
  - ER_PAIR_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/er-cases
  internal: false
  policy: POL-ER-PROPOSE
  actors: Analyst (propose, review, decide, request split) · second Analyst (confirm/split,
    large clusters)
  payload: left!:urn right!:urn rationale!:string agent:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ER-START-REVIEW
  aggregate: AGG-ER-CASE
  bc: BC02
  transitions:
  - from:
    - CANDIDATE
    to: UNDER_REVIEW
    guard: reviewer cleared for both entity labels
    event: EVT-ER-REVIEW-STARTED
  errors:
  - AUTHZ_DENIED
  - ER_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REVIEWER_NOT_CLEARED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/er-cases/{id}/actions/start-review
  internal: false
  policy: POL-ER-START-REVIEW
  actors: Analyst (propose, review, decide, request split) · second Analyst (confirm/split,
    large clusters)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ER-DECIDE-MATCH
  aggregate: AGG-ER-CASE
  bc: BC02
  transitions:
  - from:
    - UNDER_REVIEW
    to: MATCHED
    guard: types compatible; neither entity RETIRED; merged cluster contains no NOT_A_MATCH
      pair; merged cluster size ≤ 50 or second reviewer; reviewer ≠ human proposer;
      creates MATCH link and recomputes cluster in the same transaction
    event: EVT-ER-MATCHED
  errors:
  - AUTHZ_DENIED
  - ER_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - MATCH_CONTRADICTS_NOT_A_MATCH
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/er-cases/{id}/actions/decide-match
  internal: false
  policy: POL-ER-DECIDE-MATCH
  actors: Analyst (propose, review, decide, request split) · second Analyst (confirm/split,
    large clusters)
  payload: rationale!:string second_reviewer:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ER-DECIDE-NOT-MATCH
  aggregate: AGG-ER-CASE
  bc: BC02
  transitions:
  - from:
    - UNDER_REVIEW
    to: NOT_A_MATCH
    guard: rationale; creates NOT_A_MATCH link (blocks re-proposal)
    event: EVT-ER-NOT-MATCHED
  - from:
    - POSSIBLE_DUPLICATE
    to: NOT_A_MATCH
    guard: rationale
    event: EVT-ER-NOT-MATCHED
  errors:
  - AUTHZ_DENIED
  - ER_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/er-cases/{id}/actions/decide-not-match
  internal: false
  policy: POL-ER-DECIDE-NOT-MATCH
  actors: Analyst (propose, review, decide, request split) · second Analyst (confirm/split,
    large clusters)
  payload: rationale!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ER-PARK
  aggregate: AGG-ER-CASE
  bc: BC02
  transitions:
  - from:
    - UNDER_REVIEW
    to: POSSIBLE_DUPLICATE
    guard: rationale; insufficient evidence
    event: EVT-ER-PARKED
  errors:
  - AUTHZ_DENIED
  - ER_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/er-cases/{id}/actions/park
  internal: false
  policy: POL-ER-PARK
  actors: Analyst (propose, review, decide, request split) · second Analyst (confirm/split,
    large clusters)
  payload: rationale!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ER-RESUME
  aggregate: AGG-ER-CASE
  bc: BC02
  transitions:
  - from:
    - POSSIBLE_DUPLICATE
    to: UNDER_REVIEW
    guard: new evidence or reason
    event: EVT-ER-RESUMED
  errors:
  - AUTHZ_DENIED
  - ER_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/er-cases/{id}/actions/resume
  internal: false
  policy: POL-ER-RESUME
  actors: Analyst (propose, review, decide, request split) · second Analyst (confirm/split,
    large clusters)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ER-REQUEST-SPLIT
  aggregate: AGG-ER-CASE
  bc: BC02
  transitions:
  - from:
    - MATCHED
    to: SPLIT_REQUIRED
    guard: reason + evidence; requester cleared for both entities
    event: EVT-ER-SPLIT-REQUESTED
  errors:
  - AUTHZ_DENIED
  - ER_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/er-cases/{id}/actions/request-split
  internal: false
  policy: POL-ER-REQUEST-SPLIT
  actors: Analyst (propose, review, decide, request split) · second Analyst (confirm/split,
    large clusters)
  payload: reason!:string evidence:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ER-CONFIRM-MATCH
  aggregate: AGG-ER-CASE
  bc: BC02
  transitions:
  - from:
    - SPLIT_REQUIRED
    to: MATCHED
    guard: reviewer ≠ split requester; rationale
    event: EVT-ER-MATCH-CONFIRMED
  errors:
  - AUTHZ_DENIED
  - ER_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/er-cases/{id}/actions/confirm-match
  internal: false
  policy: POL-ER-CONFIRM-MATCH
  actors: Analyst (propose, review, decide, request split) · second Analyst (confirm/split,
    large clusters)
  payload: rationale!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ER-SPLIT
  aggregate: AGG-ER-CASE
  bc: BC02
  transitions:
  - from:
    - SPLIT_REQUIRED
    to: SPLIT
    guard: reviewer ≠ split requester; closes MATCH link (recorded_to = now); optional
      NOT_A_MATCH link; recomputes clusters in the same transaction
    event: EVT-ER-SPLIT
  errors:
  - AUTHZ_DENIED
  - ER_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/er-cases/{id}/actions/split
  internal: false
  policy: POL-ER-SPLIT
  actors: Analyst (propose, review, decide, request split) · second Analyst (confirm/split,
    large clusters)
  payload: rationale!:string record_not_a_match!:boolean
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ER-WITHDRAW
  aggregate: AGG-ER-CASE
  bc: BC02
  transitions:
  - from:
    - CANDIDATE
    - UNDER_REVIEW
    - POSSIBLE_DUPLICATE
    to: WITHDRAWN
    guard: reason (e.g. entity retired, duplicate case)
    event: EVT-ER-WITHDRAWN
  errors:
  - AUTHZ_DENIED
  - ER_CASE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/er-cases/{id}/actions/withdraw
  internal: false
  policy: POL-ER-WITHDRAW
  actors: Analyst (propose, review, decide, request split) · second Analyst (confirm/split,
    large clusters)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MRS-DRAFT
  aggregate: AGG-MATCH-RULESET
  bc: BC02
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: entity type exists
    event: EVT-MRS-DRAFTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/match-rulesets
  internal: false
  policy: POL-MRS-DRAFT
  actors: Analyst lead (draft, edit) · Administrator ≠ author (activate)
  payload: entity_type!:string based_on:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-MRS-EDIT
  aggregate: AGG-MATCH-RULESET
  bc: BC02
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: blocking keys, features, weights, thresholds valid; evaluation run on labelled
      test set attached
    event: EVT-MRS-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MATCH_RULESET_INVALID_STATE_TRANSITION
  - RULESET_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/match-rulesets/{id}/actions/edit
  internal: false
  policy: POL-MRS-EDIT
  actors: Analyst lead (draft, edit) · Administrator ≠ author (activate)
  payload: blocking_keys!:array features!:array thresholds!:object evaluation_attachment!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-MRS-ACTIVATE
  aggregate: AGG-MATCH-RULESET
  bc: BC02
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: evaluation meets QAS-ER-001 (candidate recall ≥ 95 %) and QAS-ER-002; approver
      ≠ author; previous ACTIVE → SUPERSEDED
    event: EVT-MRS-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MATCH_RULESET_INVALID_STATE_TRANSITION
  - RULESET_BELOW_TARGET
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/match-rulesets/{id}/actions/activate
  internal: false
  policy: POL-MRS-ACTIVATE
  actors: Analyst lead (draft, edit) · Administrator ≠ author (activate)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
