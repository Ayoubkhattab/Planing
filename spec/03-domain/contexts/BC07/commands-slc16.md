---
id: CMD-CAT-BC07-SLC16
type: command-catalog
title: Commands — BC07 (SLC-16)
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC07 (SLC-16)

_12 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-CON-REGISTER | AGG-INTEGRATION-CONNECTION | `POST /api/v1/integration/connections` | لا | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-REGISTER | `name!:string system_kind!:enum(erp,hris,dms,cmms,sensor_gateway,cap_endpoint) endpoint!:string protocol!:string direction!:enum(inbound,outbound) credentials_ref!:string` | EVT-CON-REGISTERED | AUTHZ_DENIED, CONNECTION_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CON-TEST | AGG-INTEGRATION-CONNECTION | `POST /api/v1/integration/connections/{id}/actions/test` | لا | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-TEST | `—` | EVT-CON-TEST-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CON-ACTIVATE | AGG-INTEGRATION-CONNECTION | `POST /api/v1/integration/connections/{id}/actions/activate` | لا | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-ACTIVATE | `allow_list_entry!:object` | EVT-CON-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CON-FAIL-TEST | AGG-INTEGRATION-CONNECTION | `POST /api/v1/integration/connections/{id}/actions/fail-test` | لا | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-FAIL-TEST | `errors!:array` | EVT-CON-TEST-FAILED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CON-SUSPEND | AGG-INTEGRATION-CONNECTION | `POST /api/v1/integration/connections/{id}/actions/suspend` | لا | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-SUSPEND | `reason!:string` | EVT-CON-SUSPENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CON-RESUME | AGG-INTEGRATION-CONNECTION | `POST /api/v1/integration/connections/{id}/actions/resume` | لا | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-RESUME | `—` | EVT-CON-RESUMED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CON-RETIRE | AGG-INTEGRATION-CONNECTION | `POST /api/v1/integration/connections/{id}/actions/retire` | لا | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire) | POL-CON-RETIRE | `reason!:string` | EVT-CON-RETIRED | AUTHZ_DENIED, CONNECTION_IN_USE, IDEMPOTENCY_KEY_REUSED, INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SNS-REGISTER | AGG-SENSOR-STREAM | `POST /api/v1/integration/sensor-streams` | لا | integration engineer | POL-SNS-REGISTER | `connection!:urn source!:urn quantity!:string unit!:string expected_rate!:number location:object linked_entity:urn` | EVT-SNS-REGISTERED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, STREAM_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SNS-SET-QUALITY-RULES | AGG-SENSOR-STREAM | `POST /api/v1/integration/sensor-streams/{id}/actions/set-quality-rules` | لا | integration engineer | POL-SNS-SET-QUALITY-RULES | `rules!:object` | EVT-SNS-QUALITY-RULES-SET | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, QUALITY_RULES_INVALID, SENSOR_STREAM_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SNS-ACTIVATE | AGG-SENSOR-STREAM | `POST /api/v1/integration/sensor-streams/{id}/actions/activate` | لا | integration engineer | POL-SNS-ACTIVATE | `—` | EVT-SNS-ACTIVATED | AUTHZ_DENIED, CONNECTION_NOT_ACTIVE, IDEMPOTENCY_KEY_REUSED, SENSOR_STREAM_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SNS-PAUSE | AGG-SENSOR-STREAM | `POST /api/v1/integration/sensor-streams/{id}/actions/pause` | لا | integration engineer | POL-SNS-PAUSE | `reason!:string` | EVT-SNS-PAUSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SENSOR_STREAM_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SNS-RETIRE | AGG-SENSOR-STREAM | `POST /api/v1/integration/sensor-streams/{id}/actions/retire` | لا | integration engineer | POL-SNS-RETIRE | `reason!:string` | EVT-SNS-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SENSOR_STREAM_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-CON-REGISTER
  aggregate: AGG-INTEGRATION-CONNECTION
  bc: BC07
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: system kind ∈ {erp, hris, dms, cmms, sensor_gateway, cap_endpoint}; endpoint
      on an internal network; protocol; direction ∈ {inbound, outbound}, outbound
      only for cap_endpoint in R2 (INV-CON-02); credentials stored in OpenBao (reference
      only)
    event: EVT-CON-REGISTERED
  errors:
  - AUTHZ_DENIED
  - CONNECTION_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/integration/connections
  internal: false
  policy: POL-CON-REGISTER
  actors: integration engineer (register, test) · Security Officer ≠ requester (activate)
    · Administrator (suspend, resume, retire)
  payload: name!:string system_kind!:enum(erp,hris,dms,cmms,sensor_gateway,cap_endpoint)
    endpoint!:string protocol!:string direction!:enum(inbound,outbound) credentials_ref!:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CON-TEST
  aggregate: AGG-INTEGRATION-CONNECTION
  bc: BC07
  transitions:
  - from:
    - DRAFT
    to: TESTING
    guard: integration engineer; connectivity and schema probe run
    event: EVT-CON-TEST-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/connections/{id}/actions/test
  internal: false
  policy: POL-CON-TEST
  actors: integration engineer (register, test) · Security Officer ≠ requester (activate)
    · Administrator (suspend, resume, retire)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CON-ACTIVATE
  aggregate: AGG-INTEGRATION-CONNECTION
  bc: BC07
  transitions:
  - from:
    - TESTING
    to: ACTIVE
    guard: probe passed; egress allow-list entry approved by Security Officer ≠ requester
      (GOV-005)
    event: EVT-CON-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/connections/{id}/actions/activate
  internal: false
  policy: POL-CON-ACTIVATE
  actors: integration engineer (register, test) · Security Officer ≠ requester (activate)
    · Administrator (suspend, resume, retire)
  payload: allow_list_entry!:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CON-FAIL-TEST
  aggregate: AGG-INTEGRATION-CONNECTION
  bc: BC07
  transitions:
  - from:
    - TESTING
    to: DRAFT
    guard: probe failed; errors recorded
    event: EVT-CON-TEST-FAILED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/connections/{id}/actions/fail-test
  internal: false
  policy: POL-CON-FAIL-TEST
  actors: integration engineer (register, test) · Security Officer ≠ requester (activate)
    · Administrator (suspend, resume, retire)
  payload: errors!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CON-SUSPEND
  aggregate: AGG-INTEGRATION-CONNECTION
  bc: BC07
  transitions:
  - from:
    - ACTIVE
    - DEGRADED
    to: SUSPENDED
    guard: reason; egress rule disabled
    event: EVT-CON-SUSPENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/connections/{id}/actions/suspend
  internal: false
  policy: POL-CON-SUSPEND
  actors: integration engineer (register, test) · Security Officer ≠ requester (activate)
    · Administrator (suspend, resume, retire)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CON-RESUME
  aggregate: AGG-INTEGRATION-CONNECTION
  bc: BC07
  transitions:
  - from:
    - SUSPENDED
    to: ACTIVE
    guard: egress rule re-enabled after re-check
    event: EVT-CON-RESUMED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/connections/{id}/actions/resume
  internal: false
  policy: POL-CON-RESUME
  actors: integration engineer (register, test) · Security Officer ≠ requester (activate)
    · Administrator (suspend, resume, retire)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CON-RETIRE
  aggregate: AGG-INTEGRATION-CONNECTION
  bc: BC07
  transitions:
  - from:
    - DRAFT
    - SUSPENDED
    to: RETIRED
    guard: no ACTIVE adapter or stream bound; egress rule removed
    event: EVT-CON-RETIRED
  errors:
  - AUTHZ_DENIED
  - CONNECTION_IN_USE
  - IDEMPOTENCY_KEY_REUSED
  - INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/connections/{id}/actions/retire
  internal: false
  policy: POL-CON-RETIRE
  actors: integration engineer (register, test) · Security Officer ≠ requester (activate)
    · Administrator (suspend, resume, retire)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SNS-REGISTER
  aggregate: AGG-SENSOR-STREAM
  bc: BC07
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: connection (sensor_gateway) exists; BC02 Source of type sensor ACTIVE;
      quantity + UCUM unit; expected rate; location or linked entity
    event: EVT-SNS-REGISTERED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - STREAM_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/integration/sensor-streams
  internal: false
  policy: POL-SNS-REGISTER
  actors: integration engineer
  payload: connection!:urn source!:urn quantity!:string unit!:string expected_rate!:number
    location:object linked_entity:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-SNS-SET-QUALITY-RULES
  aggregate: AGG-SENSOR-STREAM
  bc: BC07
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    - PAUSED
    to: '='
    guard: range, rate-of-change, stale-after, duplicate window; violations become
      data_quality issues, not rejections
    event: EVT-SNS-QUALITY-RULES-SET
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - QUALITY_RULES_INVALID
  - SENSOR_STREAM_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/sensor-streams/{id}/actions/set-quality-rules
  internal: false
  policy: POL-SNS-SET-QUALITY-RULES
  actors: integration engineer
  payload: rules!:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SNS-ACTIVATE
  aggregate: AGG-SENSOR-STREAM
  bc: BC07
  transitions:
  - from:
    - DRAFT
    - PAUSED
    to: ACTIVE
    guard: connection ACTIVE; mapping to CMD-OBS-RECORD batches tested
    event: EVT-SNS-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - CONNECTION_NOT_ACTIVE
  - IDEMPOTENCY_KEY_REUSED
  - SENSOR_STREAM_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/sensor-streams/{id}/actions/activate
  internal: false
  policy: POL-SNS-ACTIVATE
  actors: integration engineer
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SNS-PAUSE
  aggregate: AGG-SENSOR-STREAM
  bc: BC07
  transitions:
  - from:
    - ACTIVE
    to: PAUSED
    guard: reason
    event: EVT-SNS-PAUSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SENSOR_STREAM_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/sensor-streams/{id}/actions/pause
  internal: false
  policy: POL-SNS-PAUSE
  actors: integration engineer
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SNS-RETIRE
  aggregate: AGG-SENSOR-STREAM
  bc: BC07
  transitions:
  - from:
    - DRAFT
    - PAUSED
    to: RETIRED
    guard: reason
    event: EVT-SNS-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SENSOR_STREAM_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/sensor-streams/{id}/actions/retire
  internal: false
  policy: POL-SNS-RETIRE
  actors: integration engineer
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
