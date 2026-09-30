---
id: AGG-SECURITY-EXCEPTION
type: aggregate
title: Security Exception
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC08
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-FND-017
  state_machine: SM-SECURITY-EXCEPTION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SECURITY-EXCEPTION — Security Exception

**الغرض:** استثناء مؤقت من سياسة مستأجر بموافقة شخصين  
**السياق:** BC08 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-EXC-01** — activation requires two distinct approvers, both different from the requester (REQ-FND-017)
- **INV-EXC-02** — exceptions never apply to platform baseline rules (tenant isolation, classification rule, audit, fail-closed)
- **INV-EXC-03** — maximum duration 30 days; renewal = new request (W4 delegated decision)

## الحالات

- غير نهائية: REQUESTED, FIRST_APPROVED, ACTIVE
- نهائية: REJECTED, EXPIRED, REVOKED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-EXC-REQUEST | REQUESTED | targets a tenant policy rule (not platform baseline); duration ≤ 30 days; justification | EVT-EXC-REQUESTED | EXCEPTION_NOT_ALLOWED |
| REQUESTED | CMD-EXC-APPROVE | FIRST_APPROVED | approver authorized; approver ≠ requester | EVT-EXC-FIRST-APPROVED | SEGREGATION_OF_DUTIES |
| FIRST_APPROVED | CMD-EXC-APPROVE | ACTIVE | approver authorized; approver ∉ {requester, first approver} | EVT-EXC-ACTIVATED | SEGREGATION_OF_DUTIES |
| REQUESTED, FIRST_APPROVED | CMD-EXC-REJECT | REJECTED | reason | EVT-EXC-REJECTED | REASON_REQUIRED |
| ACTIVE | CMD-EXC-REVOKE | REVOKED | Security Officer; reason | EVT-EXC-REVOKED | REASON_REQUIRED |
| ACTIVE | SYS:end reached | EXPIRED | scheduler | EVT-EXC-EXPIRED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-EXC-REQUEST | CMD-EXC-APPROVE | CMD-EXC-REJECT | CMD-EXC-REVOKE | SYS:end reached |
|---|---|---|---|---|---|
| ∅ | → REQUESTED | — | — | — | — |
| REQUESTED | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | → FIRST_APPROVED | → REJECTED | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
| FIRST_APPROVED | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | → ACTIVE | → REJECTED | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | → REVOKED | → EXPIRED |
| REJECTED | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
| EXPIRED | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
| REVOKED | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | ✗ SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |

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
id: AGG-SECURITY-EXCEPTION
bc: BC08
name: Security Exception
tier: T2
purpose: استثناء مؤقت من سياسة مستأجر بموافقة شخصين
states:
- REQUESTED
- FIRST_APPROVED
- ACTIVE
- REJECTED
- EXPIRED
- REVOKED
terminal:
- REJECTED
- EXPIRED
- REVOKED
invariants:
- 'INV-EXC-01: activation requires two distinct approvers, both different from the
  requester (REQ-FND-017)'
- 'INV-EXC-02: exceptions never apply to platform baseline rules (tenant isolation,
  classification rule, audit, fail-closed)'
- 'INV-EXC-03: maximum duration 30 days; renewal = new request (W4 delegated decision)'
entities: []
requirements:
- REQ-FND-017
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-EXC-REQUEST
  to: REQUESTED
  guard: targets a tenant policy rule (not platform baseline); duration ≤ 30 days;
    justification
  event: EVT-EXC-REQUESTED
  guard_error: EXCEPTION_NOT_ALLOWED
- from:
  - REQUESTED
  command: CMD-EXC-APPROVE
  to: FIRST_APPROVED
  guard: approver authorized; approver ≠ requester
  event: EVT-EXC-FIRST-APPROVED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - FIRST_APPROVED
  command: CMD-EXC-APPROVE
  to: ACTIVE
  guard: approver authorized; approver ∉ {requester, first approver}
  event: EVT-EXC-ACTIVATED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - REQUESTED
  - FIRST_APPROVED
  command: CMD-EXC-REJECT
  to: REJECTED
  guard: reason
  event: EVT-EXC-REJECTED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  command: CMD-EXC-REVOKE
  to: REVOKED
  guard: Security Officer; reason
  event: EVT-EXC-REVOKED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  command: SYS:end reached
  to: EXPIRED
  guard: scheduler
  event: EVT-EXC-EXPIRED
  guard_error: null
```

</details>
