---
id: CMD-CAT-BC04-SLC06
type: command-catalog
title: Commands — BC04 (SLC-06)
wave: W4
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC04 (SLC-06)

_6 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-SUB-SUBSCRIBE | AGG-SUBSCRIPTION | `POST /api/v1/operations/subscriptions` | لا | any user (self) · Administrator (end) | POL-SUB-SUBSCRIBE | `target!:urn channels!:array quiet_hours:object` | EVT-SUB-SUBSCRIBED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SUBSCRIPTION_EXISTS, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SUB-UPDATE-CHANNELS | AGG-SUBSCRIPTION | `POST /api/v1/operations/subscriptions/{id}/actions/update-channels` | لا | any user (self) · Administrator (end) | POL-SUB-UPDATE-CHANNELS | `channels!:array quiet_hours:object` | EVT-SUB-CHANNELS-UPDATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SUBSCRIPTION_INVALID, SUBSCRIPTION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SUB-PAUSE | AGG-SUBSCRIPTION | `POST /api/v1/operations/subscriptions/{id}/actions/pause` | لا | any user (self) · Administrator (end) | POL-SUB-PAUSE | `—` | EVT-SUB-PAUSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SUBSCRIPTION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SUB-RESUME | AGG-SUBSCRIPTION | `POST /api/v1/operations/subscriptions/{id}/actions/resume` | لا | any user (self) · Administrator (end) | POL-SUB-RESUME | `—` | EVT-SUB-RESUMED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SUBSCRIPTION_INVALID_STATE_TRANSITION, TARGET_NOT_VISIBLE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SUB-UNSUBSCRIBE | AGG-SUBSCRIPTION | `POST /api/v1/operations/subscriptions/{id}/actions/unsubscribe` | لا | any user (self) · Administrator (end) | POL-SUB-UNSUBSCRIBE | `reason:string` | EVT-SUB-ENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SUBSCRIPTION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-NTF-MARK-READ | AGG-NOTIFICATION | `POST /api/v1/operations/notifications/{id}/actions/mark-read` | لا | recipient | POL-NTF-MARK-READ | `—` | EVT-NTF-READ | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, NOTIFICATION_INVALID_STATE_TRANSITION, NOT_RECIPIENT, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-SUB-SUBSCRIBE
  aggregate: AGG-SUBSCRIPTION
  bc: BC04
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: target (situation | alert rule) visible to subscriber; channels ⊆ {in_app,
      push}; one ACTIVE per (user, target)
    event: EVT-SUB-SUBSCRIBED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SUBSCRIPTION_EXISTS
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/operations/subscriptions
  internal: false
  policy: POL-SUB-SUBSCRIBE
  actors: any user (self) · Administrator (end)
  payload: target!:urn channels!:array quiet_hours:object
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-SUB-UPDATE-CHANNELS
  aggregate: AGG-SUBSCRIPTION
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    - PAUSED
    to: '='
    guard: channels valid; quiet hours valid (critical severity bypasses quiet hours)
    event: EVT-SUB-CHANNELS-UPDATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SUBSCRIPTION_INVALID
  - SUBSCRIPTION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/subscriptions/{id}/actions/update-channels
  internal: false
  policy: POL-SUB-UPDATE-CHANNELS
  actors: any user (self) · Administrator (end)
  payload: channels!:array quiet_hours:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SUB-PAUSE
  aggregate: AGG-SUBSCRIPTION
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    to: PAUSED
    guard: —
    event: EVT-SUB-PAUSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SUBSCRIPTION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/subscriptions/{id}/actions/pause
  internal: false
  policy: POL-SUB-PAUSE
  actors: any user (self) · Administrator (end)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SUB-RESUME
  aggregate: AGG-SUBSCRIPTION
  bc: BC04
  transitions:
  - from:
    - PAUSED
    to: ACTIVE
    guard: target still visible
    event: EVT-SUB-RESUMED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SUBSCRIPTION_INVALID_STATE_TRANSITION
  - TARGET_NOT_VISIBLE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/subscriptions/{id}/actions/resume
  internal: false
  policy: POL-SUB-RESUME
  actors: any user (self) · Administrator (end)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SUB-UNSUBSCRIBE
  aggregate: AGG-SUBSCRIPTION
  bc: BC04
  transitions:
  - from:
    - ACTIVE
    - PAUSED
    to: ENDED
    guard: actor = subscriber or Administrator
    event: EVT-SUB-ENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SUBSCRIPTION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/subscriptions/{id}/actions/unsubscribe
  internal: false
  policy: POL-SUB-UNSUBSCRIBE
  actors: any user (self) · Administrator (end)
  payload: reason:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-NTF-MARK-READ
  aggregate: AGG-NOTIFICATION
  bc: BC04
  transitions:
  - from:
    - SENT
    to: READ
    guard: actor = recipient; content fetched through normal authorized query
    event: EVT-NTF-READ
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - NOTIFICATION_INVALID_STATE_TRANSITION
  - NOT_RECIPIENT
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/notifications/{id}/actions/mark-read
  internal: false
  policy: POL-NTF-MARK-READ
  actors: recipient
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
