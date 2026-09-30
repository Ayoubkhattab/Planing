---
id: CMD-CAT-BC07-SLC02
type: command-catalog
title: Commands — BC07 (SLC-02)
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC07 (SLC-02)

_6 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-ADP-REGISTER | AGG-ADAPTER | `POST /api/v1/integration/adapters` | لا | Administrator (register, update) · second Administrator (activate) | POL-ADP-REGISTER | `name!:string source!:urn service_account!:urn mapping!:object` | EVT-ADP-REGISTERED | ADAPTER_INVALID, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ADP-UPDATE-MAPPING | AGG-ADAPTER | `POST /api/v1/integration/adapters/{id}/actions/update-mapping` | لا | Administrator (register, update) · second Administrator (activate) | POL-ADP-UPDATE-MAPPING | `mapping!:object tests!:array` | EVT-ADP-MAPPING-UPDATED | ADAPTER_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MAPPING_TESTS_FAILED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ADP-ACTIVATE | AGG-ADAPTER | `POST /api/v1/integration/adapters/{id}/actions/activate` | لا | Administrator (register, update) · second Administrator (activate) | POL-ADP-ACTIVATE | `—` | EVT-ADP-ACTIVATED | ADAPTER_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ADP-SUSPEND | AGG-ADAPTER | `POST /api/v1/integration/adapters/{id}/actions/suspend` | لا | Administrator (register, update) · second Administrator (activate) | POL-ADP-SUSPEND | `reason!:string` | EVT-ADP-SUSPENDED | ADAPTER_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ADP-RESUME | AGG-ADAPTER | `POST /api/v1/integration/adapters/{id}/actions/resume` | لا | Administrator (register, update) · second Administrator (activate) | POL-ADP-RESUME | `—` | EVT-ADP-RESUMED | ADAPTER_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ADP-RETIRE | AGG-ADAPTER | `POST /api/v1/integration/adapters/{id}/actions/retire` | لا | Administrator (register, update) · second Administrator (activate) | POL-ADP-RETIRE | `reason!:string` | EVT-ADP-RETIRED | ADAPTER_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-ADP-REGISTER
  aggregate: AGG-ADAPTER
  bc: BC07
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: source ACTIVE; service account ACTIVE; mapping spec present
    event: EVT-ADP-REGISTERED
  errors:
  - ADAPTER_INVALID
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/integration/adapters
  internal: false
  policy: POL-ADP-REGISTER
  actors: Administrator (register, update) · second Administrator (activate)
  payload: name!:string source!:urn service_account!:urn mapping!:object
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ADP-UPDATE-MAPPING
  aggregate: AGG-ADAPTER
  bc: BC07
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    to: '='
    guard: mapping tests pass; new immutable mapping version
    event: EVT-ADP-MAPPING-UPDATED
  errors:
  - ADAPTER_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MAPPING_TESTS_FAILED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/adapters/{id}/actions/update-mapping
  internal: false
  policy: POL-ADP-UPDATE-MAPPING
  actors: Administrator (register, update) · second Administrator (activate)
  payload: mapping!:object tests!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ADP-ACTIVATE
  aggregate: AGG-ADAPTER
  bc: BC07
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: mapping tests pass; approver ≠ author
    event: EVT-ADP-ACTIVATED
  errors:
  - ADAPTER_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/adapters/{id}/actions/activate
  internal: false
  policy: POL-ADP-ACTIVATE
  actors: Administrator (register, update) · second Administrator (activate)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ADP-SUSPEND
  aggregate: AGG-ADAPTER
  bc: BC07
  transitions:
  - from:
    - ACTIVE
    to: SUSPENDED
    guard: reason
    event: EVT-ADP-SUSPENDED
  errors:
  - ADAPTER_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/adapters/{id}/actions/suspend
  internal: false
  policy: POL-ADP-SUSPEND
  actors: Administrator (register, update) · second Administrator (activate)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ADP-RESUME
  aggregate: AGG-ADAPTER
  bc: BC07
  transitions:
  - from:
    - SUSPENDED
    to: ACTIVE
    guard: —
    event: EVT-ADP-RESUMED
  errors:
  - ADAPTER_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/adapters/{id}/actions/resume
  internal: false
  policy: POL-ADP-RESUME
  actors: Administrator (register, update) · second Administrator (activate)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ADP-RETIRE
  aggregate: AGG-ADAPTER
  bc: BC07
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    - SUSPENDED
    to: RETIRED
    guard: reason
    event: EVT-ADP-RETIRED
  errors:
  - ADAPTER_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/integration/adapters/{id}/actions/retire
  internal: false
  policy: POL-ADP-RETIRE
  actors: Administrator (register, update) · second Administrator (activate)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
