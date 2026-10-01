---
id: CMD-CAT-BC08-SLC01
type: command-catalog
title: Commands — BC08 (SLC-01)
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC08 (SLC-01)

_13 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-CLS-DRAFT | AGG-CLASSIFICATION-SCHEME | `POST /api/v1/governance/classification-schemes` | لا | Security Officer | POL-CLS-DRAFT | `based_on:urn` | EVT-CLS-DRAFTED | AUTHZ_DENIED, DRAFT_EXISTS, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLS-EDIT | AGG-CLASSIFICATION-SCHEME | `POST /api/v1/governance/classification-schemes/{id}/actions/edit` | لا | Security Officer | POL-CLS-EDIT | `levels!:array compartments!:array caveats!:array audit_threshold!:string default_level!:string` | EVT-CLS-EDITED | AUTHZ_DENIED, CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SCHEME_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLS-ACTIVATE | AGG-CLASSIFICATION-SCHEME | `POST /api/v1/governance/classification-schemes/{id}/actions/activate` | لا | Security Officer | POL-CLS-ACTIVATE | `effective_from!:date-time` | EVT-CLS-ACTIVATED | AUTHZ_DENIED, CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SCHEME_INVALID, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLS-DISCARD | AGG-CLASSIFICATION-SCHEME | `POST /api/v1/governance/classification-schemes/{id}/actions/discard` | لا | Security Officer | POL-CLS-DISCARD | `—` | EVT-CLS-DISCARDED | AUTHZ_DENIED, CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-POL-DRAFT | AGG-POLICY-SET | `POST /api/v1/governance/policy-sets` | لا | Security Officer | POL-POL-DRAFT | `based_on:urn` | EVT-POL-DRAFTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-POL-EDIT | AGG-POLICY-SET | `POST /api/v1/governance/policy-sets/{id}/actions/edit` | لا | Security Officer | POL-POL-EDIT | `decision_tables!:array tests!:array` | EVT-POL-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, POLICY_INVALID, POLICY_SET_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-POL-SUBMIT | AGG-POLICY-SET | `POST /api/v1/governance/policy-sets/{id}/actions/submit` | لا | Security Officer | POL-POL-SUBMIT | `effective_from!:date-time` | EVT-POL-SUBMITTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, POLICY_SET_INVALID_STATE_TRANSITION, POLICY_TESTS_FAILED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-POL-APPROVE | AGG-POLICY-SET | `POST /api/v1/governance/policy-sets/{id}/actions/approve` | لا | Security Officer | POL-POL-APPROVE | `—` | EVT-POL-APPROVED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, POLICY_SET_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-POL-REJECT | AGG-POLICY-SET | `POST /api/v1/governance/policy-sets/{id}/actions/reject` | لا | Security Officer | POL-POL-REJECT | `reason!:string` | EVT-POL-REJECTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, POLICY_SET_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EXC-REQUEST | AGG-SECURITY-EXCEPTION | `POST /api/v1/governance/security-exceptions` | لا | any authorized requester; Security Officers approve | POL-EXC-REQUEST | `policy_rule!:string subject_scope!:object justification!:string starts_at!:date-time ends_at!:date-time` | EVT-EXC-REQUESTED | AUTHZ_DENIED, EXCEPTION_NOT_ALLOWED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EXC-APPROVE | AGG-SECURITY-EXCEPTION | `POST /api/v1/governance/security-exceptions/{id}/actions/approve` | لا | any authorized requester; Security Officers approve | POL-EXC-APPROVE | `note:string` | EVT-EXC-ACTIVATED, EVT-EXC-FIRST-APPROVED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SECURITY_EXCEPTION_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EXC-REJECT | AGG-SECURITY-EXCEPTION | `POST /api/v1/governance/security-exceptions/{id}/actions/reject` | لا | any authorized requester; Security Officers approve | POL-EXC-REJECT | `reason!:string` | EVT-EXC-REJECTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SECURITY_EXCEPTION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EXC-REVOKE | AGG-SECURITY-EXCEPTION | `POST /api/v1/governance/security-exceptions/{id}/actions/revoke` | لا | any authorized requester; Security Officers approve | POL-EXC-REVOKE | `reason!:string` | EVT-EXC-REVOKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SECURITY_EXCEPTION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-CLS-DRAFT
  aggregate: AGG-CLASSIFICATION-SCHEME
  bc: BC08
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: Security Officer; at most one DRAFT per tenant
    event: EVT-CLS-DRAFTED
  errors:
  - AUTHZ_DENIED
  - DRAFT_EXISTS
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/governance/classification-schemes
  internal: false
  policy: POL-CLS-DRAFT
  actors: Security Officer
  payload: based_on:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CLS-EDIT
  aggregate: AGG-CLASSIFICATION-SCHEME
  bc: BC08
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: codes immutable once used; ranks strictly ordered; removal not allowed,
      only deprecation
    event: EVT-CLS-EDITED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SCHEME_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/classification-schemes/{id}/actions/edit
  internal: false
  policy: POL-CLS-EDIT
  actors: Security Officer
  payload: levels!:array compartments!:array caveats!:array audit_threshold!:string
    default_level!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLS-ACTIVATE
  aggregate: AGG-CLASSIFICATION-SCHEME
  bc: BC08
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: validation passes; effective_from ≥ now; approver ≠ drafter; previous ACTIVE
      → SUPERSEDED in same transaction
    event: EVT-CLS-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SCHEME_INVALID
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/classification-schemes/{id}/actions/activate
  internal: false
  policy: POL-CLS-ACTIVATE
  actors: Security Officer
  payload: effective_from!:date-time
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLS-DISCARD
  aggregate: AGG-CLASSIFICATION-SCHEME
  bc: BC08
  transitions:
  - from:
    - DRAFT
    to: DISCARDED
    guard: —
    event: EVT-CLS-DISCARDED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/classification-schemes/{id}/actions/discard
  internal: false
  policy: POL-CLS-DISCARD
  actors: Security Officer
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-POL-DRAFT
  aggregate: AGG-POLICY-SET
  bc: BC08
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: Security Officer
    event: EVT-POL-DRAFTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/governance/policy-sets
  internal: false
  policy: POL-POL-DRAFT
  actors: Security Officer
  payload: based_on:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-POL-EDIT
  aggregate: AGG-POLICY-SET
  bc: BC08
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: tables validate against schema
    event: EVT-POL-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - POLICY_INVALID
  - POLICY_SET_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/policy-sets/{id}/actions/edit
  internal: false
  policy: POL-POL-EDIT
  actors: Security Officer
  payload: decision_tables!:array tests!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-POL-SUBMIT
  aggregate: AGG-POLICY-SET
  bc: BC08
  transitions:
  - from:
    - DRAFT
    to: IN_REVIEW
    guard: embedded policy tests all pass; tenant rules only restrict platform baseline
    event: EVT-POL-SUBMITTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - POLICY_SET_INVALID_STATE_TRANSITION
  - POLICY_TESTS_FAILED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/policy-sets/{id}/actions/submit
  internal: false
  policy: POL-POL-SUBMIT
  actors: Security Officer
  payload: effective_from!:date-time
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-POL-APPROVE
  aggregate: AGG-POLICY-SET
  bc: BC08
  transitions:
  - from:
    - IN_REVIEW
    to: APPROVED
    guard: approver ≠ author; Security Officer
    event: EVT-POL-APPROVED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - POLICY_SET_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/policy-sets/{id}/actions/approve
  internal: false
  policy: POL-POL-APPROVE
  actors: Security Officer
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-POL-REJECT
  aggregate: AGG-POLICY-SET
  bc: BC08
  transitions:
  - from:
    - IN_REVIEW
    to: REJECTED
    guard: reason
    event: EVT-POL-REJECTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - POLICY_SET_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/policy-sets/{id}/actions/reject
  internal: false
  policy: POL-POL-REJECT
  actors: Security Officer
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EXC-REQUEST
  aggregate: AGG-SECURITY-EXCEPTION
  bc: BC08
  transitions:
  - from:
    - ∅
    to: REQUESTED
    guard: targets a tenant policy rule (not platform baseline); duration ≤ 30 days;
      justification
    event: EVT-EXC-REQUESTED
  errors:
  - AUTHZ_DENIED
  - EXCEPTION_NOT_ALLOWED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/governance/security-exceptions
  internal: false
  policy: POL-EXC-REQUEST
  actors: any authorized requester; Security Officers approve
  payload: policy_rule!:string subject_scope!:object justification!:string starts_at!:date-time
    ends_at!:date-time
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-EXC-APPROVE
  aggregate: AGG-SECURITY-EXCEPTION
  bc: BC08
  transitions:
  - from:
    - REQUESTED
    to: FIRST_APPROVED
    guard: approver authorized; approver ≠ requester
    event: EVT-EXC-FIRST-APPROVED
  - from:
    - FIRST_APPROVED
    to: ACTIVE
    guard: approver authorized; approver ∉ {requester, first approver}
    event: EVT-EXC-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SECURITY_EXCEPTION_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/security-exceptions/{id}/actions/approve
  internal: false
  policy: POL-EXC-APPROVE
  actors: any authorized requester; Security Officers approve
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EXC-REJECT
  aggregate: AGG-SECURITY-EXCEPTION
  bc: BC08
  transitions:
  - from:
    - REQUESTED
    - FIRST_APPROVED
    to: REJECTED
    guard: reason
    event: EVT-EXC-REJECTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SECURITY_EXCEPTION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/security-exceptions/{id}/actions/reject
  internal: false
  policy: POL-EXC-REJECT
  actors: any authorized requester; Security Officers approve
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EXC-REVOKE
  aggregate: AGG-SECURITY-EXCEPTION
  bc: BC08
  transitions:
  - from:
    - ACTIVE
    to: REVOKED
    guard: Security Officer; reason
    event: EVT-EXC-REVOKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SECURITY_EXCEPTION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/governance/security-exceptions/{id}/actions/revoke
  internal: false
  policy: POL-EXC-REVOKE
  actors: any authorized requester; Security Officers approve
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
