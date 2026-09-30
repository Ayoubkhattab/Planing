---
id: CMD-CAT-BC03-SLC16
type: command-catalog
title: Commands — BC03 (SLC-16)
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC03 (SLC-16)

_4 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-CAP-PREPARE | AGG-CAP-MESSAGE | `POST /api/v1/intelligence/cap-messages` | لا | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel) | POL-CAP-PREPARE | `alert!:urn template!:string connection!:urn` | EVT-CAP-PREPARED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RELEASE_NOT_ALLOWED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CAP-RELEASE | AGG-CAP-MESSAGE | `POST /api/v1/intelligence/cap-messages/{id}/actions/release` | لا | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel) | POL-CAP-RELEASE | `note:string` | EVT-CAP-SENT | AUTHZ_DENIED, CAP_MESSAGE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CAP-RETRY | AGG-CAP-MESSAGE | `POST /api/v1/intelligence/cap-messages/{id}/actions/retry` | لا | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel) | POL-CAP-RETRY | `—` | EVT-CAP-RETRY | AUTHZ_DENIED, CAP_MESSAGE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CAP-CANCEL | AGG-CAP-MESSAGE | `POST /api/v1/intelligence/cap-messages/{id}/actions/cancel` | لا | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel) | POL-CAP-CANCEL | `reason!:string` | EVT-CAP-CANCELLED | AUTHZ_DENIED, CAP_MESSAGE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-CAP-PREPARE
  aggregate: AGG-CAP-MESSAGE
  bc: BC03
  transitions:
  - from:
    - ∅
    to: PREPARED
    guard: tenant CAP enabled; alert RAISED/ACKNOWLEDGED; alert label ≤ tenant external
      release level; content = CAP fields from a reviewed template (no free text from
      classified sources); target connection cap_endpoint ACTIVE
    event: EVT-CAP-PREPARED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RELEASE_NOT_ALLOWED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/intelligence/cap-messages
  internal: false
  policy: POL-CAP-PREPARE
  actors: alert recipient / duty officer (prepare) · release authority (release) ·
    operator (retry, cancel)
  payload: alert!:urn template!:string connection!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CAP-RELEASE
  aggregate: AGG-CAP-MESSAGE
  bc: BC03
  transitions:
  - from:
    - PREPARED
    to: SENT
    guard: release authority ≠ preparer; valid CAP 1.2 (schema validated); delivery
      acknowledged
    event: EVT-CAP-SENT
  errors:
  - AUTHZ_DENIED
  - CAP_MESSAGE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/cap-messages/{id}/actions/release
  internal: false
  policy: POL-CAP-RELEASE
  actors: alert recipient / duty officer (prepare) · release authority (release) ·
    operator (retry, cancel)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CAP-RETRY
  aggregate: AGG-CAP-MESSAGE
  bc: BC03
  transitions:
  - from:
    - FAILED
    to: PREPARED
    guard: operator
    event: EVT-CAP-RETRY
  errors:
  - AUTHZ_DENIED
  - CAP_MESSAGE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/cap-messages/{id}/actions/retry
  internal: false
  policy: POL-CAP-RETRY
  actors: alert recipient / duty officer (prepare) · release authority (release) ·
    operator (retry, cancel)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CAP-CANCEL
  aggregate: AGG-CAP-MESSAGE
  bc: BC03
  transitions:
  - from:
    - PREPARED
    - FAILED
    to: CANCELLED
    guard: reason
    event: EVT-CAP-CANCELLED
  errors:
  - AUTHZ_DENIED
  - CAP_MESSAGE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/cap-messages/{id}/actions/cancel
  internal: false
  policy: POL-CAP-CANCEL
  actors: alert recipient / duty officer (prepare) · release authority (release) ·
    operator (retry, cancel)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
