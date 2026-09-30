---
id: CMD-CAT-BC07-SLC05
type: command-catalog
title: Commands — BC07 (SLC-05)
wave: W4
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC07 (SLC-05)

_4 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-PRJ-CREATE-VERSION | AGG-PROJECTION-VERSION | `POST /api/v1/discovery/projection-versions` | لا | Platform Operator | POL-PRJ-CREATE-VERSION | `kind!:enum(search,graph,vector) tenant_group!:string schema_version!:integer normalization_version!:integer reason!:string` | EVT-PRJ-BUILD-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PROJECTION_BUILD_IN_PROGRESS, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRJ-PROMOTE | AGG-PROJECTION-VERSION | `POST /api/v1/discovery/projection-versions/{id}/actions/promote` | لا | Platform Operator | POL-PRJ-PROMOTE | `—` | EVT-PRJ-PROMOTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PROJECTION_NOT_VERIFIED, PROJECTION_VERSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRJ-RETIRE | AGG-PROJECTION-VERSION | `POST /api/v1/discovery/projection-versions/{id}/actions/retire` | لا | Platform Operator | POL-PRJ-RETIRE | `reason!:string` | EVT-PRJ-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LAST_ACTIVE_PROJECTION, PROJECTION_VERSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRJ-CANCEL-BUILD | AGG-PROJECTION-VERSION | `POST /api/v1/discovery/projection-versions/{id}/actions/cancel-build` | لا | Platform Operator | POL-PRJ-CANCEL-BUILD | `reason!:string` | EVT-PRJ-FAILED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PROJECTION_VERSION_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-PRJ-CREATE-VERSION
  aggregate: AGG-PROJECTION-VERSION
  bc: BC07
  transitions:
  - from:
    - ∅
    to: BUILDING
    guard: kind ∈ {search, graph, vector (R2, SLC-10)}; document schema version, embedding
      model version (vector), analyzer/normalization version and source checkpoint
      set; at most one BUILDING version per (tenant group, kind)
    event: EVT-PRJ-BUILD-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PROJECTION_BUILD_IN_PROGRESS
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/discovery/projection-versions
  internal: false
  policy: POL-PRJ-CREATE-VERSION
  actors: Platform Operator
  payload: kind!:enum(search,graph,vector) tenant_group!:string schema_version!:integer
    normalization_version!:integer reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-PRJ-PROMOTE
  aggregate: AGG-PROJECTION-VERSION
  bc: BC07
  transitions:
  - from:
    - READY
    to: ACTIVE
    guard: operator; verification passed; previous ACTIVE of same kind → RETIRED in
      the same step (alias switch)
    event: EVT-PRJ-PROMOTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PROJECTION_NOT_VERIFIED
  - PROJECTION_VERSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/discovery/projection-versions/{id}/actions/promote
  internal: false
  policy: POL-PRJ-PROMOTE
  actors: Platform Operator
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PRJ-RETIRE
  aggregate: AGG-PROJECTION-VERSION
  bc: BC07
  transitions:
  - from:
    - READY
    - ACTIVE
    - DEGRADED
    to: RETIRED
    guard: operator; not the only ACTIVE version of its kind
    event: EVT-PRJ-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LAST_ACTIVE_PROJECTION
  - PROJECTION_VERSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/discovery/projection-versions/{id}/actions/retire
  internal: false
  policy: POL-PRJ-RETIRE
  actors: Platform Operator
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PRJ-CANCEL-BUILD
  aggregate: AGG-PROJECTION-VERSION
  bc: BC07
  transitions:
  - from:
    - BUILDING
    to: FAILED
    guard: operator; reason
    event: EVT-PRJ-FAILED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PROJECTION_VERSION_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/discovery/projection-versions/{id}/actions/cancel-build
  internal: false
  policy: POL-PRJ-CANCEL-BUILD
  actors: Platform Operator
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
