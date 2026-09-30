---
id: CMD-CAT-BC05-SLC19
type: command-catalog
title: Commands — BC05 (SLC-19)
wave: W4
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
---


# Commands — BC05 (SLC-19)

_15 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-SCN-DEFINE | AGG-SCENARIO | `POST /api/v1/readiness/scenarios` | لا | Training Manager (define, edit) · Exercise Director (activate, retire) | POL-SCN-DEFINE | `title!:LocalizedName exercise_type_ref!:urn situation!:string target_competencies!:array injects!:array` | EVT-SCN-DEFINED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SCENARIO_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SCN-EDIT | AGG-SCENARIO | `POST /api/v1/readiness/scenarios/{id}/actions/edit` | لا | Training Manager (define, edit) · Exercise Director (activate, retire) | POL-SCN-EDIT | `title:LocalizedName situation:string target_competencies:array injects:array` | EVT-SCN-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SCENARIO_INVALID, SCENARIO_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SCN-ACTIVATE | AGG-SCENARIO | `POST /api/v1/readiness/scenarios/{id}/actions/activate` | لا | Training Manager (define, edit) · Exercise Director (activate, retire) | POL-SCN-ACTIVATE | `—` | EVT-SCN-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SCENARIO_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SCN-RETIRE | AGG-SCENARIO | `POST /api/v1/readiness/scenarios/{id}/actions/retire` | لا | Training Manager (define, edit) · Exercise Director (activate, retire) | POL-SCN-RETIRE | `reason!:string` | EVT-SCN-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SCENARIO_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EXR-PLAN | AGG-EXERCISE | `POST /api/v1/readiness/exercises` | لا | Exercise Director / Training Manager | POL-EXR-PLAN | `scenario!:urn objectives!:string participants!:array purpose!:enum(drill,certification,assessment) role_ref:urn` | EVT-EXR-PLANNED | AUTHZ_DENIED, EXERCISE_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EXR-SCHEDULE | AGG-EXERCISE | `POST /api/v1/readiness/exercises/{id}/actions/schedule` | لا | Exercise Director / Training Manager | POL-EXR-SCHEDULE | `window!:Interval location!:LocalizedName participants!:array` | EVT-EXR-SCHEDULED | AUTHZ_DENIED, EXERCISE_INVALID, EXERCISE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EXR-START | AGG-EXERCISE | `POST /api/v1/readiness/exercises/{id}/actions/start` | لا | Exercise Director / Training Manager | POL-EXR-START | `note:string` | EVT-EXR-STARTED | AUTHZ_DENIED, EXERCISE_INVALID, EXERCISE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EXR-CANCEL | AGG-EXERCISE | `POST /api/v1/readiness/exercises/{id}/actions/cancel` | لا | Exercise Director / Training Manager | POL-EXR-CANCEL | `reason!:string` | EVT-EXR-CANCELLED | AUTHZ_DENIED, EXERCISE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIM-START | AGG-SIMULATION | `POST /api/v1/readiness/simulations` | نعم | system (workload identity, invoked by CMD-EXR-START in the same unit of work) | POL-SIM-START | `exercise!:urn scenario!:urn started_at!:date-time` | EVT-SIM-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SIMULATION_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIM-DELIVER-INJECT | AGG-SIMULATION | `POST /api/v1/readiness/simulations/{id}/actions/deliver-inject` | لا | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-DELIVER-INJECT | `inject_ref!:urn delivered_at!:date-time note:string` | EVT-SIM-INJECT-DELIVERED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INJECT_INVALID, SIMULATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIM-RECORD-EVALUATION | AGG-SIMULATION | `POST /api/v1/readiness/simulations/{id}/actions/record-evaluation` | لا | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-RECORD-EVALUATION | `participant!:urn competency_code!:string result!:enum(MET,PARTIAL,NOT_MET) notes:string` | EVT-SIM-EVALUATION-RECORDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, SIMULATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIM-PAUSE | AGG-SIMULATION | `POST /api/v1/readiness/simulations/{id}/actions/pause` | لا | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-PAUSE | `reason!:string` | EVT-SIM-PAUSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SIMULATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIM-RESUME | AGG-SIMULATION | `POST /api/v1/readiness/simulations/{id}/actions/resume` | لا | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-RESUME | `—` | EVT-SIM-RESUMED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SIMULATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIM-COMPLETE | AGG-SIMULATION | `POST /api/v1/readiness/simulations/{id}/actions/complete` | لا | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-COMPLETE | `—` | EVT-SIM-COMPLETED | AUTHZ_DENIED, EVALUATION_MISSING, IDEMPOTENCY_KEY_REUSED, SIMULATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIM-ABORT | AGG-SIMULATION | `POST /api/v1/readiness/simulations/{id}/actions/abort` | لا | Exercise Controller (start, deliver-inject, pause, resume, complete, abort) · Evaluator (record-evaluation) | POL-SIM-ABORT | `reason!:string` | EVT-SIM-ABORTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SIMULATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-SCN-DEFINE
  aggregate: AGG-SCENARIO
  bc: BC05
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: title; exercise_type_ref in RD-EXERCISE-TYPES; situation; target_competencies
      ⊆ RD-COMPETENCIES; injects ordered by strictly increasing offset (INV-SCN-01)
    event: EVT-SCN-DEFINED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SCENARIO_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/scenarios
  internal: false
  policy: POL-SCN-DEFINE
  actors: Training Manager (define, edit) · Exercise Director (activate, retire)
  payload: title!:LocalizedName exercise_type_ref!:urn situation!:string target_competencies!:array
    injects!:array
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-SCN-EDIT
  aggregate: AGG-SCENARIO
  bc: BC05
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    to: '='
    guard: same validations as DEFINE; editing an ACTIVE scenario creates a new version
    event: EVT-SCN-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SCENARIO_INVALID
  - SCENARIO_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/scenarios/{id}/actions/edit
  internal: false
  policy: POL-SCN-EDIT
  actors: Training Manager (define, edit) · Exercise Director (activate, retire)
  payload: title:LocalizedName situation:string target_competencies:array injects:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SCN-ACTIVATE
  aggregate: AGG-SCENARIO
  bc: BC05
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: approver ≠ author
    event: EVT-SCN-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SCENARIO_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/scenarios/{id}/actions/activate
  internal: false
  policy: POL-SCN-ACTIVATE
  actors: Training Manager (define, edit) · Exercise Director (activate, retire)
  payload: '—'
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SCN-RETIRE
  aggregate: AGG-SCENARIO
  bc: BC05
  transitions:
  - from:
    - ACTIVE
    to: RETIRED
    guard: reason
    event: EVT-SCN-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SCENARIO_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/scenarios/{id}/actions/retire
  internal: false
  policy: POL-SCN-RETIRE
  actors: Training Manager (define, edit) · Exercise Director (activate, retire)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EXR-PLAN
  aggregate: AGG-EXERCISE
  bc: BC05
  transitions:
  - from:
    - ∅
    to: PLANNED
    guard: scenario ACTIVE at this instant, frozen thereafter (INV-EXR-01); objectives;
      participants; purpose; role_ref optional
    event: EVT-EXR-PLANNED
  errors:
  - AUTHZ_DENIED
  - EXERCISE_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/exercises
  internal: false
  policy: POL-EXR-PLAN
  actors: Exercise Director / Training Manager
  payload: scenario!:urn objectives!:string participants!:array purpose!:enum(drill,certification,assessment)
    role_ref:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-EXR-SCHEDULE
  aggregate: AGG-EXERCISE
  bc: BC05
  transitions:
  - from:
    - PLANNED
    to: SCHEDULED
    guard: window.from < window.to; location; participants confirmed
    event: EVT-EXR-SCHEDULED
  errors:
  - AUTHZ_DENIED
  - EXERCISE_INVALID
  - EXERCISE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/exercises/{id}/actions/schedule
  internal: false
  policy: POL-EXR-SCHEDULE
  actors: Exercise Director / Training Manager
  payload: window!:Interval location!:LocalizedName participants!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EXR-START
  aggregate: AGG-EXERCISE
  bc: BC05
  transitions:
  - from:
    - SCHEDULED
    to: IN_PROGRESS
    guard: scheduled window reached (or authorized override); system creates a linked
      Simulation in the same unit of work (CMD-SIM-START)
    event: EVT-EXR-STARTED
  errors:
  - AUTHZ_DENIED
  - EXERCISE_INVALID
  - EXERCISE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/exercises/{id}/actions/start
  internal: false
  policy: POL-EXR-START
  actors: Exercise Director / Training Manager
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EXR-CANCEL
  aggregate: AGG-EXERCISE
  bc: BC05
  transitions:
  - from:
    - PLANNED
    - SCHEDULED
    to: CANCELLED
    guard: reason
    event: EVT-EXR-CANCELLED
  errors:
  - AUTHZ_DENIED
  - EXERCISE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/exercises/{id}/actions/cancel
  internal: false
  policy: POL-EXR-CANCEL
  actors: Exercise Director / Training Manager
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIM-START
  aggregate: AGG-SIMULATION
  bc: BC05
  transitions:
  - from:
    - ∅
    to: IN_PROGRESS
    guard: system-issued in the same unit of work as CMD-EXR-START; exercise_ref SCHEDULED
      transitioning to IN_PROGRESS; scenario_ref = the exercise's frozen scenario;
      started_at
    event: EVT-SIM-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SIMULATION_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/simulations
  internal: true
  policy: POL-SIM-START
  actors: system (workload identity, invoked by CMD-EXR-START in the same unit of
    work)
  payload: exercise!:urn scenario!:urn started_at!:date-time
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-SIM-DELIVER-INJECT
  aggregate: AGG-SIMULATION
  bc: BC05
  transitions:
  - from:
    - IN_PROGRESS
    to: '='
    guard: inject_ref belongs to the linked scenario; delivered_at strictly after
      the previous delivery (INV-SIM-01)
    event: EVT-SIM-INJECT-DELIVERED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INJECT_INVALID
  - SIMULATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/simulations/{id}/actions/deliver-inject
  internal: false
  policy: POL-SIM-DELIVER-INJECT
  actors: Exercise Controller (start, deliver-inject, pause, resume, complete, abort)
    · Evaluator (record-evaluation)
  payload: inject_ref!:urn delivered_at!:date-time note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIM-RECORD-EVALUATION
  aggregate: AGG-SIMULATION
  bc: BC05
  transitions:
  - from:
    - IN_PROGRESS
    - PAUSED
    to: '='
    guard: participant_ref is one of the linked exercise's participants; competency_code
      in RD-COMPETENCIES; result ∈ {MET, PARTIAL, NOT_MET}; evaluator ≠ participant
      (INV-SIM-03)
    event: EVT-SIM-EVALUATION-RECORDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - SIMULATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/simulations/{id}/actions/record-evaluation
  internal: false
  policy: POL-SIM-RECORD-EVALUATION
  actors: Exercise Controller (start, deliver-inject, pause, resume, complete, abort)
    · Evaluator (record-evaluation)
  payload: participant!:urn competency_code!:string result!:enum(MET,PARTIAL,NOT_MET)
    notes:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIM-PAUSE
  aggregate: AGG-SIMULATION
  bc: BC05
  transitions:
  - from:
    - IN_PROGRESS
    to: PAUSED
    guard: reason
    event: EVT-SIM-PAUSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SIMULATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/simulations/{id}/actions/pause
  internal: false
  policy: POL-SIM-PAUSE
  actors: Exercise Controller (start, deliver-inject, pause, resume, complete, abort)
    · Evaluator (record-evaluation)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIM-RESUME
  aggregate: AGG-SIMULATION
  bc: BC05
  transitions:
  - from:
    - PAUSED
    to: IN_PROGRESS
    guard: —
    event: EVT-SIM-RESUMED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SIMULATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/simulations/{id}/actions/resume
  internal: false
  policy: POL-SIM-RESUME
  actors: Exercise Controller (start, deliver-inject, pause, resume, complete, abort)
    · Evaluator (record-evaluation)
  payload: '—'
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIM-COMPLETE
  aggregate: AGG-SIMULATION
  bc: BC05
  transitions:
  - from:
    - IN_PROGRESS
    - PAUSED
    to: COMPLETED
    guard: every participant on the linked exercise has ≥ 1 recorded evaluation (INV-SIM-02)
    event: EVT-SIM-COMPLETED
  errors:
  - AUTHZ_DENIED
  - EVALUATION_MISSING
  - IDEMPOTENCY_KEY_REUSED
  - SIMULATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/simulations/{id}/actions/complete
  internal: false
  policy: POL-SIM-COMPLETE
  actors: Exercise Controller (start, deliver-inject, pause, resume, complete, abort)
    · Evaluator (record-evaluation)
  payload: '—'
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIM-ABORT
  aggregate: AGG-SIMULATION
  bc: BC05
  transitions:
  - from:
    - IN_PROGRESS
    - PAUSED
    to: ABORTED
    guard: reason
    event: EVT-SIM-ABORTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SIMULATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/simulations/{id}/actions/abort
  internal: false
  policy: POL-SIM-ABORT
  actors: Exercise Controller (start, deliver-inject, pause, resume, complete, abort)
    · Evaluator (record-evaluation)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
