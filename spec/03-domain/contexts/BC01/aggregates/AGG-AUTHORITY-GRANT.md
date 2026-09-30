---
id: AGG-AUTHORITY-GRANT
type: aggregate
title: Authority Grant (incl. delegation)
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
  - REQ-FND-007
  - REQ-FND-008
  - REQ-FND-009
  state_machine: SM-AUTHORITY-GRANT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-AUTHORITY-GRANT — Authority Grant (incl. delegation)

**الغرض:** حق تقرير نوع قرار ضمن نطاق وحدود وفترة  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** لا

> Holder may be a user or a role. AuthorityCheck (QRY-AUT-CHECK) evaluates INV-AUT-03 as of any time t, so decisions can be audited later.

## الثوابت (Invariants)

- **INV-AUT-01** — a delegation never exceeds its parent in decision types, scope, limits or period
- **INV-AUT-02** — delegation depth ≤ 2 (W4 delegated decision)
- **INV-AUT-03** — a grant is EFFECTIVE at t ⇔ state ACTIVE at t ∧ t ∈ validity ∧ (no parent ∨ parent EFFECTIVE at t) — revoking a parent makes children ineffective without writing to them
- **INV-AUT-04** — root grants require approval by an Executive other than the requester

## الحالات

- غير نهائية: PENDING_APPROVAL, ACTIVE, SUSPENDED
- نهائية: EXPIRED, REVOKED, REJECTED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-AUT-GRANT | PENDING_APPROVAL | actor has authority.grant permission; decision type exists; scope unit ACTIVE | EVT-AUT-GRANT-REQUESTED | PERMISSION_DENIED |
| PENDING_APPROVAL | CMD-AUT-APPROVE-GRANT | ACTIVE | approver is Executive in scope; approver ≠ requester | EVT-AUT-GRANTED | SEGREGATION_OF_DUTIES |
| PENDING_APPROVAL | CMD-AUT-REJECT-GRANT | REJECTED | reason | EVT-AUT-GRANT-REJECTED | REASON_REQUIRED |
| ∅ (إنشاء) | CMD-AUT-DELEGATE | ACTIVE | parent grant effective and delegable; scope ⊆ parent; limits ≤ parent; period ⊆ parent; depth ≤ 2; delegate ≠ delegator | EVT-AUT-DELEGATED | AUTHORITY_EXCEEDS_DELEGATOR |
| ACTIVE | CMD-AUT-SUSPEND | SUSPENDED | reason | EVT-AUT-SUSPENDED | REASON_REQUIRED |
| SUSPENDED | CMD-AUT-RESUME | ACTIVE | period not ended | EVT-AUT-RESUMED | GRANT_EXPIRED |
| PENDING_APPROVAL, ACTIVE, SUSPENDED | CMD-AUT-REVOKE | REVOKED | granter, delegator or Executive in scope; reason | EVT-AUT-REVOKED | REASON_REQUIRED |
| ACTIVE, SUSPENDED | SYS:valid_to reached | EXPIRED | system scheduler | EVT-AUT-EXPIRED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-AUT-GRANT | CMD-AUT-APPROVE-GRANT | CMD-AUT-REJECT-GRANT | CMD-AUT-DELEGATE | CMD-AUT-SUSPEND | CMD-AUT-RESUME | CMD-AUT-REVOKE | SYS:valid_to reached |
|---|---|---|---|---|---|---|---|---|
| ∅ | → PENDING_APPROVAL | — | — | → ACTIVE | — | — | — | — |
| PENDING_APPROVAL | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | → ACTIVE | → REJECTED | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | → REVOKED | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | → SUSPENDED | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | → REVOKED | → EXPIRED |
| SUSPENDED | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | → ACTIVE | → REVOKED | → EXPIRED |
| EXPIRED | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
| REVOKED | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
| REJECTED | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION | ✗ AUTHORITY_GRANT_INVALID_STATE_TRANSITION |

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
id: AGG-AUTHORITY-GRANT
bc: BC01
name: Authority Grant (incl. delegation)
tier: T2
purpose: حق تقرير نوع قرار ضمن نطاق وحدود وفترة
states:
- PENDING_APPROVAL
- ACTIVE
- SUSPENDED
- EXPIRED
- REVOKED
- REJECTED
terminal:
- EXPIRED
- REVOKED
- REJECTED
invariants:
- 'INV-AUT-01: a delegation never exceeds its parent in decision types, scope, limits
  or period'
- 'INV-AUT-02: delegation depth ≤ 2 (W4 delegated decision)'
- 'INV-AUT-03: a grant is EFFECTIVE at t ⇔ state ACTIVE at t ∧ t ∈ validity ∧ (no
  parent ∨ parent EFFECTIVE at t) — revoking a parent makes children ineffective without
  writing to them'
- 'INV-AUT-04: root grants require approval by an Executive other than the requester'
entities: []
requirements:
- REQ-FND-007
- REQ-FND-008
- REQ-FND-009
notes: Holder may be a user or a role. AuthorityCheck (QRY-AUT-CHECK) evaluates INV-AUT-03
  as of any time t, so decisions can be audited later.
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-AUT-GRANT
  to: PENDING_APPROVAL
  guard: actor has authority.grant permission; decision type exists; scope unit ACTIVE
  event: EVT-AUT-GRANT-REQUESTED
  guard_error: PERMISSION_DENIED
- from:
  - PENDING_APPROVAL
  command: CMD-AUT-APPROVE-GRANT
  to: ACTIVE
  guard: approver is Executive in scope; approver ≠ requester
  event: EVT-AUT-GRANTED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - PENDING_APPROVAL
  command: CMD-AUT-REJECT-GRANT
  to: REJECTED
  guard: reason
  event: EVT-AUT-GRANT-REJECTED
  guard_error: REASON_REQUIRED
- from: ∅
  command: CMD-AUT-DELEGATE
  to: ACTIVE
  guard: parent grant effective and delegable; scope ⊆ parent; limits ≤ parent; period
    ⊆ parent; depth ≤ 2; delegate ≠ delegator
  event: EVT-AUT-DELEGATED
  guard_error: AUTHORITY_EXCEEDS_DELEGATOR
- from:
  - ACTIVE
  command: CMD-AUT-SUSPEND
  to: SUSPENDED
  guard: reason
  event: EVT-AUT-SUSPENDED
  guard_error: REASON_REQUIRED
- from:
  - SUSPENDED
  command: CMD-AUT-RESUME
  to: ACTIVE
  guard: period not ended
  event: EVT-AUT-RESUMED
  guard_error: GRANT_EXPIRED
- from:
  - PENDING_APPROVAL
  - ACTIVE
  - SUSPENDED
  command: CMD-AUT-REVOKE
  to: REVOKED
  guard: granter, delegator or Executive in scope; reason
  event: EVT-AUT-REVOKED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  - SUSPENDED
  command: SYS:valid_to reached
  to: EXPIRED
  guard: system scheduler
  event: EVT-AUT-EXPIRED
  guard_error: null
```

</details>
