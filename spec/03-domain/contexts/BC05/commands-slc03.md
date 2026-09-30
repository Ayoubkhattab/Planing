---
id: CMD-CAT-BC05-SLC03
type: command-catalog
title: Commands — BC05 (SLC-03)
wave: W4
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC05 (SLC-03)

_5 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-QUAL-RECORD | AGG-QUALIFICATION-RECORD | `POST /api/v1/readiness/qualification-records` | لا | Resource Manager / Training Manager | POL-QUAL-RECORD | `person!:urn kind!:enum(competency,qualification,certification) code!:string level!:integer valid_from!:date-time valid_to!:date-time issuer!:string evidence:urn` | EVT-QUAL-RECORDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, QUALIFICATION_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-QUAL-RENEW | AGG-QUALIFICATION-RECORD | `POST /api/v1/readiness/qualification-records/{id}/actions/renew` | لا | Resource Manager / Training Manager | POL-QUAL-RENEW | `valid_to!:date-time evidence:urn` | EVT-QUAL-RENEWED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, QUALIFICATION_INVALID, QUALIFICATION_RECORD_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-QUAL-SUSPEND | AGG-QUALIFICATION-RECORD | `POST /api/v1/readiness/qualification-records/{id}/actions/suspend` | لا | Resource Manager / Training Manager | POL-QUAL-SUSPEND | `reason!:string` | EVT-QUAL-SUSPENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, QUALIFICATION_RECORD_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-QUAL-REINSTATE | AGG-QUALIFICATION-RECORD | `POST /api/v1/readiness/qualification-records/{id}/actions/reinstate` | لا | Resource Manager / Training Manager | POL-QUAL-REINSTATE | `—` | EVT-QUAL-REINSTATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, QUALIFICATION_EXPIRED, QUALIFICATION_RECORD_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-QUAL-REVOKE | AGG-QUALIFICATION-RECORD | `POST /api/v1/readiness/qualification-records/{id}/actions/revoke` | لا | Resource Manager / Training Manager | POL-QUAL-REVOKE | `reason!:string` | EVT-QUAL-REVOKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, QUALIFICATION_RECORD_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-QUAL-RECORD
  aggregate: AGG-QUALIFICATION-RECORD
  bc: BC05
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: person ACTIVE; code in RD-COMPETENCIES; level valid; valid_from < valid_to;
      issuer; evidence ref optional
    event: EVT-QUAL-RECORDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - QUALIFICATION_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/readiness/qualification-records
  internal: false
  policy: POL-QUAL-RECORD
  actors: Resource Manager / Training Manager
  payload: person!:urn kind!:enum(competency,qualification,certification) code!:string
    level!:integer valid_from!:date-time valid_to!:date-time issuer!:string evidence:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-QUAL-RENEW
  aggregate: AGG-QUALIFICATION-RECORD
  bc: BC05
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: new valid_to > old; evidence; new version
    event: EVT-QUAL-RENEWED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - QUALIFICATION_INVALID
  - QUALIFICATION_RECORD_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/qualification-records/{id}/actions/renew
  internal: false
  policy: POL-QUAL-RENEW
  actors: Resource Manager / Training Manager
  payload: valid_to!:date-time evidence:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-QUAL-SUSPEND
  aggregate: AGG-QUALIFICATION-RECORD
  bc: BC05
  transitions:
  - from:
    - ACTIVE
    to: SUSPENDED
    guard: reason
    event: EVT-QUAL-SUSPENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - QUALIFICATION_RECORD_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/qualification-records/{id}/actions/suspend
  internal: false
  policy: POL-QUAL-SUSPEND
  actors: Resource Manager / Training Manager
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-QUAL-REINSTATE
  aggregate: AGG-QUALIFICATION-RECORD
  bc: BC05
  transitions:
  - from:
    - SUSPENDED
    to: ACTIVE
    guard: validity not ended
    event: EVT-QUAL-REINSTATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - QUALIFICATION_EXPIRED
  - QUALIFICATION_RECORD_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/qualification-records/{id}/actions/reinstate
  internal: false
  policy: POL-QUAL-REINSTATE
  actors: Resource Manager / Training Manager
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-QUAL-REVOKE
  aggregate: AGG-QUALIFICATION-RECORD
  bc: BC05
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: REVOKED
    guard: reason
    event: EVT-QUAL-REVOKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - QUALIFICATION_RECORD_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/readiness/qualification-records/{id}/actions/revoke
  internal: false
  policy: POL-QUAL-REVOKE
  actors: Resource Manager / Training Manager
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
