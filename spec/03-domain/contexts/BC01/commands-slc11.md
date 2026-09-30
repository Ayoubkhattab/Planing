---
id: CMD-CAT-BC01-SLC11
type: command-catalog
title: Commands — BC01 (SLC-11)
wave: W4
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC01 (SLC-11)

_7 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-DEV-ENROLL | AGG-DEVICE | `POST /api/v1/foundation/devices` | لا | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-ENROLL | `user!:urn public_key!:string platform!:enum(android,ios) mdm_ref:string` | EVT-DEV-ENROLL-REQUESTED | AUTHZ_DENIED, DEVICE_LIMIT_REACHED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DEV-CONFIRM | AGG-DEVICE | `POST /api/v1/foundation/devices/{id}/actions/confirm` | لا | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-CONFIRM | `attestation!:string` | EVT-DEV-ACTIVATED | ATTESTATION_FAILED, AUTHZ_DENIED, DEVICE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DEV-ROTATE-KEY | AGG-DEVICE | `POST /api/v1/foundation/devices/{id}/actions/rotate-key` | لا | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-ROTATE-KEY | `new_public_key!:string signature!:string` | EVT-DEV-KEY-ROTATED | AUTHZ_DENIED, DEVICE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SIGNATURE_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DEV-SUSPEND | AGG-DEVICE | `POST /api/v1/foundation/devices/{id}/actions/suspend` | لا | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-SUSPEND | `reason!:string` | EVT-DEV-SUSPENDED | AUTHZ_DENIED, DEVICE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DEV-REINSTATE | AGG-DEVICE | `POST /api/v1/foundation/devices/{id}/actions/reinstate` | لا | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-REINSTATE | `reason!:string` | EVT-DEV-REINSTATED | AUTHZ_DENIED, DEVICE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DEV-REPORT-LOST | AGG-DEVICE | `POST /api/v1/foundation/devices/{id}/actions/report-lost` | لا | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-REPORT-LOST | `lost_at!:date-time note:string` | EVT-DEV-REPORTED-LOST | AUTHZ_DENIED, DEVICE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DEV-RETIRE | AGG-DEVICE | `POST /api/v1/foundation/devices/{id}/actions/retire` | لا | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | POL-DEV-RETIRE | `reason!:string override:boolean` | EVT-DEV-RETIRED | AUTHZ_DENIED, DEVICE_INVALID_STATE_TRANSITION, DEVICE_NOT_WIPED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-DEV-ENROLL
  aggregate: AGG-DEVICE
  bc: BC01
  transitions:
  - from:
    - ∅
    to: PENDING_ENROLLMENT
    guard: user ACTIVE; device public key; platform; MDM reference; ≤ 3 active devices
      per user
    event: EVT-DEV-ENROLL-REQUESTED
  errors:
  - AUTHZ_DENIED
  - DEVICE_LIMIT_REACHED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/devices
  internal: false
  policy: POL-DEV-ENROLL
  actors: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend,
    reinstate, retire) · Security Officer (lost, retire override)
  payload: user!:urn public_key!:string platform!:enum(android,ios) mdm_ref:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-DEV-CONFIRM
  aggregate: AGG-DEVICE
  bc: BC01
  transitions:
  - from:
    - PENDING_ENROLLMENT
    to: ACTIVE
    guard: hardware attestation valid (or MDM compliance); Administrator or MDM policy
    event: EVT-DEV-ACTIVATED
  errors:
  - ATTESTATION_FAILED
  - AUTHZ_DENIED
  - DEVICE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/devices/{id}/actions/confirm
  internal: false
  policy: POL-DEV-CONFIRM
  actors: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend,
    reinstate, retire) · Security Officer (lost, retire override)
  payload: attestation!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DEV-ROTATE-KEY
  aggregate: AGG-DEVICE
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: signed by current key; new public key
    event: EVT-DEV-KEY-ROTATED
  errors:
  - AUTHZ_DENIED
  - DEVICE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SIGNATURE_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/devices/{id}/actions/rotate-key
  internal: false
  policy: POL-DEV-ROTATE-KEY
  actors: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend,
    reinstate, retire) · Security Officer (lost, retire override)
  payload: new_public_key!:string signature!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DEV-SUSPEND
  aggregate: AGG-DEVICE
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: SUSPENDED
    guard: reason; sync rejected while suspended
    event: EVT-DEV-SUSPENDED
  errors:
  - AUTHZ_DENIED
  - DEVICE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/devices/{id}/actions/suspend
  internal: false
  policy: POL-DEV-SUSPEND
  actors: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend,
    reinstate, retire) · Security Officer (lost, retire override)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DEV-REINSTATE
  aggregate: AGG-DEVICE
  bc: BC01
  transitions:
  - from:
    - SUSPENDED
    to: ACTIVE
    guard: reason
    event: EVT-DEV-REINSTATED
  errors:
  - AUTHZ_DENIED
  - DEVICE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/devices/{id}/actions/reinstate
  internal: false
  policy: POL-DEV-REINSTATE
  actors: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend,
    reinstate, retire) · Security Officer (lost, retire override)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DEV-REPORT-LOST
  aggregate: AGG-DEVICE
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: LOST
    guard: user or Security Officer; key revoked immediately; wipe instruction queued;
      queued commands from the device after the lost time require review
    event: EVT-DEV-REPORTED-LOST
  errors:
  - AUTHZ_DENIED
  - DEVICE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/devices/{id}/actions/report-lost
  internal: false
  policy: POL-DEV-REPORT-LOST
  actors: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend,
    reinstate, retire) · Security Officer (lost, retire override)
  payload: lost_at!:date-time note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DEV-RETIRE
  aggregate: AGG-DEVICE
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: RETIRED
    guard: device synced and wiped (confirmation) or Security Officer override
    event: EVT-DEV-RETIRED
  errors:
  - AUTHZ_DENIED
  - DEVICE_INVALID_STATE_TRANSITION
  - DEVICE_NOT_WIPED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/devices/{id}/actions/retire
  internal: false
  policy: POL-DEV-RETIRE
  actors: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend,
    reinstate, retire) · Security Officer (lost, retire override)
  payload: reason!:string override:boolean
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
