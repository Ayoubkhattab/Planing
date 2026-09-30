---
id: AGG-CLEARANCE
type: aggregate
title: Clearance
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
  - REQ-GOV-003
  - REQ-GOV-004
  state_machine: SM-CLEARANCE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-CLEARANCE — Clearance

**الغرض:** مستوى التصريح والأقسام لمستخدم  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-CLR-01** — at most one non-terminal clearance per user
- **INV-CLR-02** — no one grants or approves their own clearance
- **INV-CLR-03** — top-rank clearance requires two distinct Security Officers (W4 delegated decision)
- **INV-CLR-04** — every change increments the user's security_version

## الحالات

- غير نهائية: PENDING_APPROVAL, ACTIVE, SUSPENDED
- نهائية: EXPIRED, REVOKED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-CLR-GRANT | PENDING_APPROVAL | Security Officer; level and compartments exist in ACTIVE scheme; subject has no other non-terminal clearance | EVT-CLR-REQUESTED | CLEARANCE_EXISTS |
| PENDING_APPROVAL | CMD-CLR-APPROVE | ACTIVE | second Security Officer ≠ requester when level is top rank; else requester may self-confirm | EVT-CLR-GRANTED | SEGREGATION_OF_DUTIES |
| ACTIVE | CMD-CLR-MODIFY | (بلا تغيير) | same rules as grant; creates new version | EVT-CLR-MODIFIED | CLEARANCE_INVALID |
| ACTIVE | CMD-CLR-SUSPEND | SUSPENDED | reason | EVT-CLR-SUSPENDED | REASON_REQUIRED |
| SUSPENDED | CMD-CLR-REINSTATE | ACTIVE | period not ended | EVT-CLR-REINSTATED | — |
| PENDING_APPROVAL, ACTIVE, SUSPENDED | CMD-CLR-REVOKE | REVOKED | reason | EVT-CLR-REVOKED | REASON_REQUIRED |
| ACTIVE, SUSPENDED | SYS:valid_to reached | EXPIRED | system | EVT-CLR-EXPIRED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-CLR-GRANT | CMD-CLR-APPROVE | CMD-CLR-MODIFY | CMD-CLR-SUSPEND | CMD-CLR-REINSTATE | CMD-CLR-REVOKE | SYS:valid_to reached |
|---|---|---|---|---|---|---|---|
| ∅ | → PENDING_APPROVAL | — | — | — | — | — | — |
| PENDING_APPROVAL | ✗ CLEARANCE_INVALID_STATE_TRANSITION | → ACTIVE | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | → REVOKED | ✗ CLEARANCE_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | → ACTIVE | → SUSPENDED | ✗ CLEARANCE_INVALID_STATE_TRANSITION | → REVOKED | → EXPIRED |
| SUSPENDED | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | → ACTIVE | → REVOKED | → EXPIRED |
| EXPIRED | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION |
| REVOKED | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION | ✗ CLEARANCE_INVALID_STATE_TRANSITION |

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
id: AGG-CLEARANCE
bc: BC01
name: Clearance
tier: T2
purpose: مستوى التصريح والأقسام لمستخدم
states:
- PENDING_APPROVAL
- ACTIVE
- SUSPENDED
- EXPIRED
- REVOKED
terminal:
- EXPIRED
- REVOKED
invariants:
- 'INV-CLR-01: at most one non-terminal clearance per user'
- 'INV-CLR-02: no one grants or approves their own clearance'
- 'INV-CLR-03: top-rank clearance requires two distinct Security Officers (W4 delegated
  decision)'
- 'INV-CLR-04: every change increments the user''s security_version'
entities: []
requirements:
- REQ-GOV-003
- REQ-GOV-004
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-CLR-GRANT
  to: PENDING_APPROVAL
  guard: Security Officer; level and compartments exist in ACTIVE scheme; subject
    has no other non-terminal clearance
  event: EVT-CLR-REQUESTED
  guard_error: CLEARANCE_EXISTS
- from:
  - PENDING_APPROVAL
  command: CMD-CLR-APPROVE
  to: ACTIVE
  guard: second Security Officer ≠ requester when level is top rank; else requester
    may self-confirm
  event: EVT-CLR-GRANTED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - ACTIVE
  command: CMD-CLR-MODIFY
  to: '='
  guard: same rules as grant; creates new version
  event: EVT-CLR-MODIFIED
  guard_error: CLEARANCE_INVALID
- from:
  - ACTIVE
  command: CMD-CLR-SUSPEND
  to: SUSPENDED
  guard: reason
  event: EVT-CLR-SUSPENDED
  guard_error: REASON_REQUIRED
- from:
  - SUSPENDED
  command: CMD-CLR-REINSTATE
  to: ACTIVE
  guard: period not ended
  event: EVT-CLR-REINSTATED
  guard_error: null
- from:
  - PENDING_APPROVAL
  - ACTIVE
  - SUSPENDED
  command: CMD-CLR-REVOKE
  to: REVOKED
  guard: reason
  event: EVT-CLR-REVOKED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  - SUSPENDED
  command: SYS:valid_to reached
  to: EXPIRED
  guard: system
  event: EVT-CLR-EXPIRED
  guard_error: null
```

</details>
