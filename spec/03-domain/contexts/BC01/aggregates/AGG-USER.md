---
id: AGG-USER
type: aggregate
title: User Account
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC01
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-FND-005
  - REQ-FND-006
  state_machine: SM-USER
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-USER — User Account

**الغرض:** حساب دخول مرتبط بهويات خارجية  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-USR-01** — a user belongs to exactly one tenant
- **INV-USR-02** — (issuer, subject) is unique within the tenant
- **INV-USR-03** — an ACTIVE user has ≥ 1 identity and belongs to an ACTIVE tenant
- **INV-USR-04** — every change that affects authorization increments the subject security_version
- **INV-USR-05** — DISABLED, LOCKED and CLOSED users cannot obtain a SecurityContext

## مكونات داخلية

- Identity (entity: issuer, subject, linked_at)

## الحالات

- غير نهائية: PENDING, ACTIVE, LOCKED, DISABLED
- نهائية: CLOSED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-USR-PROVISION | PENDING | tenant ACTIVE; via SCIM or admin | EVT-USR-PROVISIONED | TENANT_NOT_ACTIVE |
| أي حالة غير نهائية | CMD-USR-LINK-IDENTITY | (بلا تغيير) | (issuer, subject) unique in tenant; issuer is a configured IdP | EVT-USR-IDENTITY-LINKED | IDENTITY_ALREADY_LINKED |
| أي حالة غير نهائية | CMD-USR-UNLINK-IDENTITY | (بلا تغيير) | if ACTIVE, at least one identity remains | EVT-USR-IDENTITY-UNLINKED | LAST_IDENTITY |
| أي حالة غير نهائية | CMD-USR-LINK-PERSON | (بلا تغيير) | person ACTIVE, not linked to another user | EVT-USR-PERSON-LINKED | PERSON_ALREADY_LINKED |
| PENDING | CMD-USR-RECORD-FIRST-SIGN-IN | ACTIVE | system; ≥ 1 identity; tenant ACTIVE | EVT-USR-ACTIVATED | — |
| ACTIVE | CMD-USR-LOCK | LOCKED | security officer or system anomaly rule; reason | EVT-USR-LOCKED | REASON_REQUIRED |
| LOCKED | CMD-USR-UNLOCK | ACTIVE | security officer | EVT-USR-UNLOCKED | — |
| PENDING, ACTIVE, LOCKED | CMD-USR-DISABLE | DISABLED | SCIM deactivate or administrator | EVT-USR-DISABLED | — |
| DISABLED | CMD-USR-ENABLE | ACTIVE | ≥ 1 identity; tenant ACTIVE | EVT-USR-ENABLED | LAST_IDENTITY |
| DISABLED | CMD-USR-CLOSE | CLOSED | administrator; audit history retained | EVT-USR-CLOSED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-USR-PROVISION | CMD-USR-LINK-IDENTITY | CMD-USR-UNLINK-IDENTITY | CMD-USR-LINK-PERSON | CMD-USR-RECORD-FIRST-SIGN-IN | CMD-USR-LOCK | CMD-USR-UNLOCK | CMD-USR-DISABLE | CMD-USR-ENABLE | CMD-USR-CLOSE |
|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → PENDING | — | — | — | — | — | — | — | — | — |
| PENDING | ✗ USER_INVALID_STATE_TRANSITION | → PENDING | → PENDING | → PENDING | → ACTIVE | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | → DISABLED | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ USER_INVALID_STATE_TRANSITION | → ACTIVE | → ACTIVE | → ACTIVE | ✗ USER_INVALID_STATE_TRANSITION | → LOCKED | ✗ USER_INVALID_STATE_TRANSITION | → DISABLED | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION |
| LOCKED | ✗ USER_INVALID_STATE_TRANSITION | → LOCKED | → LOCKED | → LOCKED | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | → ACTIVE | → DISABLED | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION |
| DISABLED | ✗ USER_INVALID_STATE_TRANSITION | → DISABLED | → DISABLED | → DISABLED | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | → ACTIVE | → CLOSED |
| CLOSED | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION | ✗ USER_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-01.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-USER
bc: BC01
name: User Account
tier: T2
purpose: حساب دخول مرتبط بهويات خارجية
states:
- PENDING
- ACTIVE
- LOCKED
- DISABLED
- CLOSED
terminal:
- CLOSED
invariants:
- 'INV-USR-01: a user belongs to exactly one tenant'
- 'INV-USR-02: (issuer, subject) is unique within the tenant'
- 'INV-USR-03: an ACTIVE user has ≥ 1 identity and belongs to an ACTIVE tenant'
- 'INV-USR-04: every change that affects authorization increments the subject security_version'
- 'INV-USR-05: DISABLED, LOCKED and CLOSED users cannot obtain a SecurityContext'
entities:
- 'Identity (entity: issuer, subject, linked_at)'
requirements:
- REQ-FND-005
- REQ-FND-006
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-USR-PROVISION
  to: PENDING
  guard: tenant ACTIVE; via SCIM or admin
  event: EVT-USR-PROVISIONED
  guard_error: TENANT_NOT_ACTIVE
- from: '*NT'
  command: CMD-USR-LINK-IDENTITY
  to: '='
  guard: (issuer, subject) unique in tenant; issuer is a configured IdP
  event: EVT-USR-IDENTITY-LINKED
  guard_error: IDENTITY_ALREADY_LINKED
- from: '*NT'
  command: CMD-USR-UNLINK-IDENTITY
  to: '='
  guard: if ACTIVE, at least one identity remains
  event: EVT-USR-IDENTITY-UNLINKED
  guard_error: LAST_IDENTITY
- from: '*NT'
  command: CMD-USR-LINK-PERSON
  to: '='
  guard: person ACTIVE, not linked to another user
  event: EVT-USR-PERSON-LINKED
  guard_error: PERSON_ALREADY_LINKED
- from:
  - PENDING
  command: CMD-USR-RECORD-FIRST-SIGN-IN
  to: ACTIVE
  guard: system; ≥ 1 identity; tenant ACTIVE
  event: EVT-USR-ACTIVATED
  guard_error: null
- from:
  - ACTIVE
  command: CMD-USR-LOCK
  to: LOCKED
  guard: security officer or system anomaly rule; reason
  event: EVT-USR-LOCKED
  guard_error: REASON_REQUIRED
- from:
  - LOCKED
  command: CMD-USR-UNLOCK
  to: ACTIVE
  guard: security officer
  event: EVT-USR-UNLOCKED
  guard_error: null
- from:
  - PENDING
  - ACTIVE
  - LOCKED
  command: CMD-USR-DISABLE
  to: DISABLED
  guard: SCIM deactivate or administrator
  event: EVT-USR-DISABLED
  guard_error: null
- from:
  - DISABLED
  command: CMD-USR-ENABLE
  to: ACTIVE
  guard: ≥ 1 identity; tenant ACTIVE
  event: EVT-USR-ENABLED
  guard_error: LAST_IDENTITY
- from:
  - DISABLED
  command: CMD-USR-CLOSE
  to: CLOSED
  guard: administrator; audit history retained
  event: EVT-USR-CLOSED
  guard_error: null
```

</details>
