---
id: CMD-CAT-BC03-SLC06
type: command-catalog
title: Commands — BC03 (SLC-06)
wave: W4
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC03 (SLC-06)

_16 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-SIT-CREATE | AGG-SITUATION | `POST /api/v1/intelligence/situations` | لا | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-CREATE | `name!:LocalizedName extent!:object window!:Interval criteria!:object owner!:urn label!:Label` | EVT-SIT-CREATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SITUATION_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIT-EDIT-DEFINITION | AGG-SITUATION | `POST /api/v1/intelligence/situations/{id}/actions/edit-definition` | لا | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-EDIT-DEFINITION | `extent:object window:Interval criteria:object reason!:string` | EVT-SIT-DEFINITION-CHANGED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SITUATION_INVALID, SITUATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIT-ACTIVATE | AGG-SITUATION | `POST /api/v1/intelligence/situations/{id}/actions/activate` | لا | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-ACTIVATE | `—` | EVT-SIT-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, QUOTA_EXCEEDED, SITUATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIT-PAUSE | AGG-SITUATION | `POST /api/v1/intelligence/situations/{id}/actions/pause` | لا | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-PAUSE | `reason!:string` | EVT-SIT-PAUSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SITUATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIT-RESUME | AGG-SITUATION | `POST /api/v1/intelligence/situations/{id}/actions/resume` | لا | Analyst / Manager | POL-SIT-RESUME | `—` | EVT-SIT-RESUMED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SITUATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIT-CLOSE | AGG-SITUATION | `POST /api/v1/intelligence/situations/{id}/actions/close` | لا | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-CLOSE | `reason!:string` | EVT-SIT-CLOSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SITUATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SIT-RECLASSIFY | AGG-SITUATION | `POST /api/v1/intelligence/situations/{id}/actions/reclassify` | لا | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | POL-SIT-RECLASSIFY | `label!:Label reason!:string` | EVT-SIT-RECLASSIFIED | AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, IDEMPOTENCY_KEY_REUSED, SITUATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ARL-DEFINE | AGG-ALERT-RULE | `POST /api/v1/intelligence/alert-rules` | لا | Analyst lead / Manager | POL-ARL-DEFINE | `situation:urn scope!:enum(situation,tenant) kind!:string parameters!:object severity!:enum(info,warning,critical) dedupe_window!:string escalation:object auto_resolve!:boolean label!:Label` | EVT-ARL-DEFINED | ALERT_RULE_INVALID, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ARL-EDIT | AGG-ALERT-RULE | `POST /api/v1/intelligence/alert-rules/{id}/actions/edit` | لا | Analyst lead / Manager | POL-ARL-EDIT | `parameters!:object severity:enum(info,warning,critical) dedupe_window:string escalation:object` | EVT-ARL-EDITED | ALERT_RULE_INVALID, ALERT_RULE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ARL-ACTIVATE | AGG-ALERT-RULE | `POST /api/v1/intelligence/alert-rules/{id}/actions/activate` | لا | Analyst lead / Manager | POL-ARL-ACTIVATE | `dry_run_ref!:string` | EVT-ARL-ACTIVATED | ALERT_RULE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, DRY_RUN_REQUIRED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ARL-DISABLE | AGG-ALERT-RULE | `POST /api/v1/intelligence/alert-rules/{id}/actions/disable` | لا | Analyst lead / Manager | POL-ARL-DISABLE | `reason!:string` | EVT-ARL-DISABLED | ALERT_RULE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ARL-ENABLE | AGG-ALERT-RULE | `POST /api/v1/intelligence/alert-rules/{id}/actions/enable` | لا | Analyst lead / Manager | POL-ARL-ENABLE | `—` | EVT-ARL-ENABLED | ALERT_RULE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ARL-RETIRE | AGG-ALERT-RULE | `POST /api/v1/intelligence/alert-rules/{id}/actions/retire` | لا | Analyst lead / Manager | POL-ARL-RETIRE | `reason!:string` | EVT-ARL-RETIRED | ALERT_RULE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ALR-ACKNOWLEDGE | AGG-ALERT | `POST /api/v1/intelligence/alerts/{id}/actions/acknowledge` | لا | recipient | POL-ALR-ACKNOWLEDGE | `note:string` | EVT-ALR-ACKNOWLEDGED | ALERT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, NOT_A_RECIPIENT, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ALR-RESOLVE | AGG-ALERT | `POST /api/v1/intelligence/alerts/{id}/actions/resolve` | لا | recipient | POL-ALR-RESOLVE | `note!:string` | EVT-ALR-RESOLVED | ALERT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, NOT_A_RECIPIENT, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ALR-DISMISS | AGG-ALERT | `POST /api/v1/intelligence/alerts/{id}/actions/dismiss` | لا | recipient | POL-ALR-DISMISS | `reason!:string` | EVT-ALR-DISMISSED | ALERT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-SIT-CREATE
  aggregate: AGG-SITUATION
  bc: BC03
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: name; extent (polygon or buffer around an entity); time window; criteria
      valid per SPEC-SITUATION §2; owner; label
    event: EVT-SIT-CREATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SITUATION_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/intelligence/situations
  internal: false
  policy: POL-SIT-CREATE
  actors: Analyst / Manager (create, edit, activate, pause, close) · Security Officer
    (reclassify)
  payload: name!:LocalizedName extent!:object window!:Interval criteria!:object owner!:urn
    label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-SIT-EDIT-DEFINITION
  aggregate: AGG-SITUATION
  bc: BC03
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    - PAUSED
    to: '='
    guard: criteria/extent/window valid; new definition version; membership recomputed
      from the new version
    event: EVT-SIT-DEFINITION-CHANGED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SITUATION_INVALID
  - SITUATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/situations/{id}/actions/edit-definition
  internal: false
  policy: POL-SIT-EDIT-DEFINITION
  actors: Analyst / Manager (create, edit, activate, pause, close) · Security Officer
    (reclassify)
  payload: extent:object window:Interval criteria:object reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIT-ACTIVATE
  aggregate: AGG-SITUATION
  bc: BC03
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: definition complete; active situations per tenant ≤ quota
    event: EVT-SIT-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - QUOTA_EXCEEDED
  - SITUATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/situations/{id}/actions/activate
  internal: false
  policy: POL-SIT-ACTIVATE
  actors: Analyst / Manager (create, edit, activate, pause, close) · Security Officer
    (reclassify)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIT-PAUSE
  aggregate: AGG-SITUATION
  bc: BC03
  transitions:
  - from:
    - ACTIVE
    to: PAUSED
    guard: reason; membership frozen, alerts of its rules suspended
    event: EVT-SIT-PAUSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SITUATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/situations/{id}/actions/pause
  internal: false
  policy: POL-SIT-PAUSE
  actors: Analyst / Manager (create, edit, activate, pause, close) · Security Officer
    (reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIT-RESUME
  aggregate: AGG-SITUATION
  bc: BC03
  transitions:
  - from:
    - PAUSED
    to: ACTIVE
    guard: membership re-evaluated from current state
    event: EVT-SIT-RESUMED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SITUATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/situations/{id}/actions/resume
  internal: false
  policy: POL-SIT-RESUME
  actors: Analyst / Manager
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIT-CLOSE
  aggregate: AGG-SITUATION
  bc: BC03
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    - PAUSED
    to: CLOSED
    guard: reason; final membership snapshot recorded
    event: EVT-SIT-CLOSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SITUATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/situations/{id}/actions/close
  internal: false
  policy: POL-SIT-CLOSE
  actors: Analyst / Manager (create, edit, activate, pause, close) · Security Officer
    (reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SIT-RECLASSIFY
  aggregate: AGG-SITUATION
  bc: BC03
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    - PAUSED
    to: '='
    guard: authority per tenant policy; subscribers without clearance are unsubscribed
    event: EVT-SIT-RECLASSIFIED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - IDEMPOTENCY_KEY_REUSED
  - SITUATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/situations/{id}/actions/reclassify
  internal: false
  policy: POL-SIT-RECLASSIFY
  actors: Analyst / Manager (create, edit, activate, pause, close) · Security Officer
    (reclassify)
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ARL-DEFINE
  aggregate: AGG-ALERT-RULE
  bc: BC03
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: condition kind in RD-ALERT-RULE-TYPES; parameters valid; severity; dedupe
      window; situation ACTIVE or tenant-wide scope
    event: EVT-ARL-DEFINED
  errors:
  - ALERT_RULE_INVALID
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/intelligence/alert-rules
  internal: false
  policy: POL-ARL-DEFINE
  actors: Analyst lead / Manager
  payload: situation:urn scope!:enum(situation,tenant) kind!:string parameters!:object
    severity!:enum(info,warning,critical) dedupe_window!:string escalation:object
    auto_resolve!:boolean label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ARL-EDIT
  aggregate: AGG-ALERT-RULE
  bc: BC03
  transitions:
  - from:
    - DRAFT
    - DISABLED
    to: '='
    guard: same validation; new version
    event: EVT-ARL-EDITED
  errors:
  - ALERT_RULE_INVALID
  - ALERT_RULE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/alert-rules/{id}/actions/edit
  internal: false
  policy: POL-ARL-EDIT
  actors: Analyst lead / Manager
  payload: parameters!:object severity:enum(info,warning,critical) dedupe_window:string
    escalation:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ARL-ACTIVATE
  aggregate: AGG-ALERT-RULE
  bc: BC03
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: dry-run on last 24 h of events completed and reviewed (expected alert volume
      shown)
    event: EVT-ARL-ACTIVATED
  errors:
  - ALERT_RULE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - DRY_RUN_REQUIRED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/alert-rules/{id}/actions/activate
  internal: false
  policy: POL-ARL-ACTIVATE
  actors: Analyst lead / Manager
  payload: dry_run_ref!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ARL-DISABLE
  aggregate: AGG-ALERT-RULE
  bc: BC03
  transitions:
  - from:
    - ACTIVE
    to: DISABLED
    guard: reason
    event: EVT-ARL-DISABLED
  errors:
  - ALERT_RULE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/alert-rules/{id}/actions/disable
  internal: false
  policy: POL-ARL-DISABLE
  actors: Analyst lead / Manager
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ARL-ENABLE
  aggregate: AGG-ALERT-RULE
  bc: BC03
  transitions:
  - from:
    - DISABLED
    to: ACTIVE
    guard: —
    event: EVT-ARL-ENABLED
  errors:
  - ALERT_RULE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/alert-rules/{id}/actions/enable
  internal: false
  policy: POL-ARL-ENABLE
  actors: Analyst lead / Manager
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ARL-RETIRE
  aggregate: AGG-ALERT-RULE
  bc: BC03
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    - DISABLED
    to: RETIRED
    guard: reason
    event: EVT-ARL-RETIRED
  errors:
  - ALERT_RULE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/alert-rules/{id}/actions/retire
  internal: false
  policy: POL-ARL-RETIRE
  actors: Analyst lead / Manager
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ALR-ACKNOWLEDGE
  aggregate: AGG-ALERT
  bc: BC03
  transitions:
  - from:
    - RAISED
    to: ACKNOWLEDGED
    guard: actor is a recipient
    event: EVT-ALR-ACKNOWLEDGED
  errors:
  - ALERT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - NOT_A_RECIPIENT
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/alerts/{id}/actions/acknowledge
  internal: false
  policy: POL-ALR-ACKNOWLEDGE
  actors: recipient
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ALR-RESOLVE
  aggregate: AGG-ALERT
  bc: BC03
  transitions:
  - from:
    - RAISED
    - ACKNOWLEDGED
    to: RESOLVED
    guard: actor is a recipient; note
    event: EVT-ALR-RESOLVED
  errors:
  - ALERT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - NOT_A_RECIPIENT
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/alerts/{id}/actions/resolve
  internal: false
  policy: POL-ALR-RESOLVE
  actors: recipient
  payload: note!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ALR-DISMISS
  aggregate: AGG-ALERT
  bc: BC03
  transitions:
  - from:
    - RAISED
    - ACKNOWLEDGED
    to: DISMISSED
    guard: actor is a recipient; reason (REQ-SIT-005)
    event: EVT-ALR-DISMISSED
  errors:
  - ALERT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/alerts/{id}/actions/dismiss
  internal: false
  policy: POL-ALR-DISMISS
  actors: recipient
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
