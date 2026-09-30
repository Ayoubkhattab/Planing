---
id: AGG-MAINTENANCE-ORDER
type: aggregate
title: Maintenance Order
wave: W4
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC05
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-RES-004
  state_machine: SM-MAINTENANCE-ORDER
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-MAINTENANCE-ORDER — Maintenance Order

**الغرض:** أمر صيانة مجدول أو تصحيحي بنافذة زمنية تحجب التوفر  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

> Integration with an external CMMS goes through an adapter (R2-Q2).

## الثوابت (Invariants)

- **INV-MNT-01** — a PLANNED or IN_PROGRESS window blocks availability (INV-AST-01)
- **INV-MNT-02** — no two non-terminal orders of one asset overlap

## الحالات

- غير نهائية: PLANNED, IN_PROGRESS
- نهائية: COMPLETED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-MNT-PLAN | PLANNED | asset not DISPOSED; kind ∈ {scheduled, corrective}; window; no overlap with another non-terminal order of the asset | EVT-MNT-PLANNED | MAINTENANCE_OVERLAP |
| PLANNED | CMD-MNT-RESCHEDULE | (بلا تغيير) | new window without overlap; affected reservations flagged | EVT-MNT-RESCHEDULED | MAINTENANCE_OVERLAP |
| PLANNED | CMD-MNT-START | IN_PROGRESS | technician; asset moves to UNDER_MAINTENANCE via its own command (policy) | EVT-MNT-STARTED | — |
| IN_PROGRESS | CMD-MNT-COMPLETE | COMPLETED | outcome ∈ {serviceable, failed}; work performed; parts consumed (optional allocation refs) | EVT-MNT-COMPLETED | OUTCOME_REQUIRED |
| PLANNED | CMD-MNT-CANCEL | CANCELLED | reason | EVT-MNT-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-MNT-PLAN | CMD-MNT-RESCHEDULE | CMD-MNT-START | CMD-MNT-COMPLETE | CMD-MNT-CANCEL |
|---|---|---|---|---|---|
| ∅ | → PLANNED | — | — | — | — |
| PLANNED | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | → PLANNED | → IN_PROGRESS | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | → CANCELLED |
| IN_PROGRESS | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | → COMPLETED | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
| COMPLETED | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | ✗ MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-09.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-MAINTENANCE-ORDER
bc: BC05
name: Maintenance Order
tier: T2
purpose: أمر صيانة مجدول أو تصحيحي بنافذة زمنية تحجب التوفر
states:
- PLANNED
- IN_PROGRESS
- COMPLETED
- CANCELLED
terminal:
- COMPLETED
- CANCELLED
invariants:
- 'INV-MNT-01: a PLANNED or IN_PROGRESS window blocks availability (INV-AST-01)'
- 'INV-MNT-02: no two non-terminal orders of one asset overlap'
entities: []
requirements:
- REQ-RES-004
notes: Integration with an external CMMS goes through an adapter (R2-Q2).
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-MNT-PLAN
  to: PLANNED
  guard: asset not DISPOSED; kind ∈ {scheduled, corrective}; window; no overlap with
    another non-terminal order of the asset
  event: EVT-MNT-PLANNED
  guard_error: MAINTENANCE_OVERLAP
- from:
  - PLANNED
  command: CMD-MNT-RESCHEDULE
  to: '='
  guard: new window without overlap; affected reservations flagged
  event: EVT-MNT-RESCHEDULED
  guard_error: MAINTENANCE_OVERLAP
- from:
  - PLANNED
  command: CMD-MNT-START
  to: IN_PROGRESS
  guard: technician; asset moves to UNDER_MAINTENANCE via its own command (policy)
  event: EVT-MNT-STARTED
  guard_error: null
- from:
  - IN_PROGRESS
  command: CMD-MNT-COMPLETE
  to: COMPLETED
  guard: outcome ∈ {serviceable, failed}; work performed; parts consumed (optional
    allocation refs)
  event: EVT-MNT-COMPLETED
  guard_error: OUTCOME_REQUIRED
- from:
  - PLANNED
  command: CMD-MNT-CANCEL
  to: CANCELLED
  guard: reason
  event: EVT-MNT-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
