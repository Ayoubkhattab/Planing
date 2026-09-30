---
id: AGG-ROLE-ASSIGNMENT
type: aggregate
title: Role Assignment
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
  - REQ-FND-011
  - REQ-OPS-005
  - REQ-OPS-009
  state_machine: SM-ROLE-ASSIGNMENT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ROLE-ASSIGNMENT — Role Assignment

**الغرض:** إسناد دور لمستخدم ضمن نطاق وحدة تنظيمية لفترة  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-RAS-01** — an assigner cannot assign a role outside units they administer, nor to themselves
- **INV-RAS-02** — SoD-incompatible roles cannot be active together for one user (default: Auditor × Administrator, Auditor × Security Officer)
- **INV-RAS-03** — assignment and revocation increment the user's security_version

## الحالات

- غير نهائية: ACTIVE
- نهائية: EXPIRED, REVOKED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-RAS-ASSIGN | ACTIVE | role ACTIVE; user not CLOSED; scope unit ACTIVE; assigner administers the scope; no SoD-incompatible active role | EVT-RAS-ASSIGNED | SOD_ROLE_CONFLICT |
| ACTIVE | CMD-RAS-REVOKE | REVOKED | assigner administers the scope; reason | EVT-RAS-REVOKED | REASON_REQUIRED |
| ACTIVE | SYS:valid_to reached | EXPIRED | system scheduler | EVT-RAS-EXPIRED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-RAS-ASSIGN | CMD-RAS-REVOKE | SYS:valid_to reached |
|---|---|---|---|
| ∅ | → ACTIVE | — | — |
| ACTIVE | ✗ ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION | → REVOKED | → EXPIRED |
| EXPIRED | ✗ ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION | ✗ ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION | ✗ ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION |
| REVOKED | ✗ ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION | ✗ ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION | ✗ ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION |

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
id: AGG-ROLE-ASSIGNMENT
bc: BC01
name: Role Assignment
tier: T2
purpose: إسناد دور لمستخدم ضمن نطاق وحدة تنظيمية لفترة
states:
- ACTIVE
- EXPIRED
- REVOKED
terminal:
- EXPIRED
- REVOKED
invariants:
- 'INV-RAS-01: an assigner cannot assign a role outside units they administer, nor
  to themselves'
- 'INV-RAS-02: SoD-incompatible roles cannot be active together for one user (default:
  Auditor × Administrator, Auditor × Security Officer)'
- 'INV-RAS-03: assignment and revocation increment the user''s security_version'
entities: []
requirements:
- REQ-FND-011
- REQ-OPS-005
- REQ-OPS-009
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-RAS-ASSIGN
  to: ACTIVE
  guard: role ACTIVE; user not CLOSED; scope unit ACTIVE; assigner administers the
    scope; no SoD-incompatible active role
  event: EVT-RAS-ASSIGNED
  guard_error: SOD_ROLE_CONFLICT
- from:
  - ACTIVE
  command: CMD-RAS-REVOKE
  to: REVOKED
  guard: assigner administers the scope; reason
  event: EVT-RAS-REVOKED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  command: SYS:valid_to reached
  to: EXPIRED
  guard: system scheduler
  event: EVT-RAS-EXPIRED
  guard_error: null
```

</details>
