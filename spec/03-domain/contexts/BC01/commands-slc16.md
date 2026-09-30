---
id: CMD-CAT-BC01-SLC16
type: command-catalog
title: Commands — BC01 (SLC-16)
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC01 (SLC-16)

_2 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-HRS-APPROVE | AGG-HR-SYNC-PROPOSAL | `POST /api/v1/foundation/hr-sync-proposals/{id}/actions/approve` | لا | Administrator in scope | POL-HRS-APPROVE | `note:string` | EVT-HRS-APPROVED | AUTHZ_DENIED, HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, OWNER_REJECTED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-HRS-REJECT | AGG-HR-SYNC-PROPOSAL | `POST /api/v1/foundation/hr-sync-proposals/{id}/actions/reject` | لا | Administrator in scope | POL-HRS-REJECT | `reason!:string` | EVT-HRS-REJECTED | AUTHZ_DENIED, HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-HRS-APPROVE
  aggregate: AGG-HR-SYNC-PROPOSAL
  bc: BC01
  transitions:
  - from:
    - PROPOSED
    to: APPROVED
    guard: Administrator in scope of the affected units; applies CMD-RAS-ASSIGN /
      CMD-RAS-REVOKE and, for leave, CMD-USR-DISABLE — each through its own guards
    event: EVT-HRS-APPROVED
  errors:
  - AUTHZ_DENIED
  - HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - OWNER_REJECTED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/hr-sync-proposals/{id}/actions/approve
  internal: false
  policy: POL-HRS-APPROVE
  actors: Administrator in scope
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-HRS-REJECT
  aggregate: AGG-HR-SYNC-PROPOSAL
  bc: BC01
  transitions:
  - from:
    - PROPOSED
    to: REJECTED
    guard: reason
    event: EVT-HRS-REJECTED
  errors:
  - AUTHZ_DENIED
  - HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/hr-sync-proposals/{id}/actions/reject
  internal: false
  policy: POL-HRS-REJECT
  actors: Administrator in scope
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
