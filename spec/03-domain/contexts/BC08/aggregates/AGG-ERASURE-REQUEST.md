---
id: AGG-ERASURE-REQUEST
type: aggregate
title: Erasure Request
wave: W4
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC08
importance_tier: T2
personal_data: true
traces:
  satisfies:
  - REQ-GOV-008
  state_machine: SM-ERASURE-REQUEST
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ERASURE-REQUEST — Erasure Request

**الغرض:** طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه  
**السياق:** BC08 · **المستوى:** T2 · **بيانات شخصية:** نعم

## الثوابت (Invariants)

- **INV-ERS-01** — execution destroys keys, not rows; data becomes unreadable everywhere including backups via the restore gate (CR-51)
- **INV-ERS-02** — blocked while any hold covers the subject
- **INV-ERS-03** — audit facts remain with a pseudonymous subject reference
- **INV-ERS-04** — approval and registration by different persons

## مكونات داخلية

- SubjectKeyRef
- ContextConfirmation

## الحالات

- غير نهائية: RECEIVED, SCOPED, APPROVED, BLOCKED_BY_HOLD, EXECUTING
- نهائية: COMPLETED, REJECTED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ERS-REGISTER | RECEIVED | legal basis reference; subject identification (platform person URN and/or information entity URNs of type person); requester | EVT-ERS-RECEIVED | ERASURE_INVALID |
| RECEIVED | SYS:subject scope resolved | SCOPED | subject keys located in BC01 (persons) and BC02 (entities with personal_data claims); affected record counts per context | EVT-ERS-SCOPED | — |
| SCOPED | CMD-ERS-APPROVE | APPROVED | Legal/Compliance authority ≠ registrar; decision recorded with basis | EVT-ERS-APPROVED | SEGREGATION_OF_DUTIES |
| SCOPED | CMD-ERS-REJECT | REJECTED | reason (e.g. legal obligation to retain) | EVT-ERS-REJECTED | REASON_REQUIRED |
| APPROVED | SYS:hold matches subject | BLOCKED_BY_HOLD | HoldCheck positive | EVT-ERS-BLOCKED | — |
| BLOCKED_BY_HOLD | SYS:hold released | APPROVED | HoldCheck negative | EVT-ERS-UNBLOCKED | — |
| APPROVED | SYS:execution started | EXECUTING | subject DEKs destroyed; owners purge plaintext caches/projections; pseudonymous reference kept for audit facts | EVT-ERS-EXECUTING | — |
| EXECUTING | SYS:all contexts confirmed | COMPLETED | confirmation from each owning context ≤ 24 h (QAS-PRV-001); certificate issued | EVT-ERS-COMPLETED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ERS-REGISTER | SYS:subject scope resolved | CMD-ERS-APPROVE | CMD-ERS-REJECT | SYS:hold matches subject | SYS:hold released | SYS:execution started | SYS:all contexts confirmed |
|---|---|---|---|---|---|---|---|---|
| ∅ | → RECEIVED | — | — | — | — | — | — | — |
| RECEIVED | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | → SCOPED | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION |
| SCOPED | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | → APPROVED | → REJECTED | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION |
| APPROVED | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | → BLOCKED_BY_HOLD | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | → EXECUTING | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION |
| BLOCKED_BY_HOLD | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | → APPROVED | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION |
| EXECUTING | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | → COMPLETED |
| COMPLETED | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION |
| REJECTED | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION | ✗ ERASURE_REQUEST_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-12a.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-ERASURE-REQUEST
bc: BC08
name: Erasure Request
tier: T2
purpose: طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه
states:
- RECEIVED
- SCOPED
- APPROVED
- BLOCKED_BY_HOLD
- EXECUTING
- COMPLETED
- REJECTED
terminal:
- COMPLETED
- REJECTED
invariants:
- 'INV-ERS-01: execution destroys keys, not rows; data becomes unreadable everywhere
  including backups via the restore gate (CR-51)'
- 'INV-ERS-02: blocked while any hold covers the subject'
- 'INV-ERS-03: audit facts remain with a pseudonymous subject reference'
- 'INV-ERS-04: approval and registration by different persons'
entities:
- SubjectKeyRef
- ContextConfirmation
requirements:
- REQ-GOV-008
notes: null
personal_data: true
reachability: PASS
transitions:
- from: ∅
  command: CMD-ERS-REGISTER
  to: RECEIVED
  guard: legal basis reference; subject identification (platform person URN and/or
    information entity URNs of type person); requester
  event: EVT-ERS-RECEIVED
  guard_error: ERASURE_INVALID
- from:
  - RECEIVED
  command: SYS:subject scope resolved
  to: SCOPED
  guard: subject keys located in BC01 (persons) and BC02 (entities with personal_data
    claims); affected record counts per context
  event: EVT-ERS-SCOPED
  guard_error: null
- from:
  - SCOPED
  command: CMD-ERS-APPROVE
  to: APPROVED
  guard: Legal/Compliance authority ≠ registrar; decision recorded with basis
  event: EVT-ERS-APPROVED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - SCOPED
  command: CMD-ERS-REJECT
  to: REJECTED
  guard: reason (e.g. legal obligation to retain)
  event: EVT-ERS-REJECTED
  guard_error: REASON_REQUIRED
- from:
  - APPROVED
  command: SYS:hold matches subject
  to: BLOCKED_BY_HOLD
  guard: HoldCheck positive
  event: EVT-ERS-BLOCKED
  guard_error: null
- from:
  - BLOCKED_BY_HOLD
  command: SYS:hold released
  to: APPROVED
  guard: HoldCheck negative
  event: EVT-ERS-UNBLOCKED
  guard_error: null
- from:
  - APPROVED
  command: SYS:execution started
  to: EXECUTING
  guard: subject DEKs destroyed; owners purge plaintext caches/projections; pseudonymous
    reference kept for audit facts
  event: EVT-ERS-EXECUTING
  guard_error: null
- from:
  - EXECUTING
  command: SYS:all contexts confirmed
  to: COMPLETED
  guard: confirmation from each owning context ≤ 24 h (QAS-PRV-001); certificate issued
  event: EVT-ERS-COMPLETED
  guard_error: null
```

</details>
