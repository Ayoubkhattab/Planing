---
id: AGG-SHIPMENT
type: aggregate
title: Shipment
wave: W4
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
bounded_context: BC05
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-LOG-004
  - REQ-LOG-005
  - REQ-LOG-006
  - REQ-LOG-007
  - REQ-LOG-009
  state_machine: SM-SHIPMENT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SHIPMENT — Shipment

**الغرض:** نقل كمية من صنف إمداد من موقع تخزين إلى وجهة تلبيةً لطلب إمداد، بتتبع نقاط حركة  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-SHP-01** — movement history (checkpoints) is append-only and chronologically gapless; no checkpoint is ever edited or removed (mirrors INV-AST-02's gapless custody chain)
- **INV-SHP-02** — delivered, damaged or lost quantity never exceeds the shipment's planned quantity; a shortfall at delivery is recorded on the event, never silently rounded up to delivered in full
- **INV-SHP-03** — departure (IN_TRANSIT) requires the linked logistics request's allocation to still be COMMITTED for at least the shipped quantity at that instant — no shipment ever moves against capacity that was never actually reserved
- **INV-SHP-04** — cancellation is only possible before departure (PLANNED); once IN_TRANSIT the shipment must resolve to DELIVERED, DAMAGED or LOST — never silently cancelled mid-transit

## مكونات داخلية

- MovementEvent (location, at, note)

## الحالات

- غير نهائية: PLANNED, IN_TRANSIT
- نهائية: DELIVERED, DAMAGED, LOST, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-SHP-PLAN | PLANNED | logistics_request APPROVED; origin pool with sufficient COMMITTED allocation quantity for the linked request; destination; carrier; planned_quantity ≤ the linked allocation's committed quantity | EVT-SHP-PLANNED | SHIPMENT_INVALID |
| PLANNED | CMD-SHP-DEPART | IN_TRANSIT | carrier confirmed; departure checkpoint recorded | EVT-SHP-DEPARTED | DEPARTURE_INVALID |
| IN_TRANSIT | CMD-SHP-RECORD-CHECKPOINT | (بلا تغيير) | checkpoint strictly after the previous checkpoint in time (append-only, gapless — mirrors INV-AST-02); location; at; note | EVT-SHP-CHECKPOINT-RECORDED | CHECKPOINT_INVALID |
| IN_TRANSIT | CMD-SHP-DELIVER | DELIVERED | receiving party confirms; delivered_quantity ≤ planned quantity; a shortfall is recorded, never hidden (INV-SHP-02) | EVT-SHP-DELIVERED | DELIVERY_INVALID |
| IN_TRANSIT | CMD-SHP-REPORT-DAMAGE | DAMAGED | reason; damaged_quantity ≤ planned quantity; evidence | EVT-SHP-DAMAGED | REASON_REQUIRED |
| IN_TRANSIT | CMD-SHP-REPORT-LOST | LOST | reason | EVT-SHP-LOST | REASON_REQUIRED |
| PLANNED | CMD-SHP-CANCEL | CANCELLED | reason; only before departure | EVT-SHP-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-SHP-PLAN | CMD-SHP-DEPART | CMD-SHP-RECORD-CHECKPOINT | CMD-SHP-DELIVER | CMD-SHP-REPORT-DAMAGE | CMD-SHP-REPORT-LOST | CMD-SHP-CANCEL |
|---|---|---|---|---|---|---|---|
| ∅ | → PLANNED | — | — | — | — | — | — |
| PLANNED | ✗ SHIPMENT_INVALID_STATE_TRANSITION | → IN_TRANSIT | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | → CANCELLED |
| IN_TRANSIT | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | → IN_TRANSIT | → DELIVERED | → DAMAGED | → LOST | ✗ SHIPMENT_INVALID_STATE_TRANSITION |
| DELIVERED | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION |
| DAMAGED | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION |
| LOST | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION | ✗ SHIPMENT_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-18.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-SHIPMENT
bc: BC05
name: Shipment
tier: T2
purpose: نقل كمية من صنف إمداد من موقع تخزين إلى وجهة تلبيةً لطلب إمداد، بتتبع نقاط
  حركة
states:
- PLANNED
- IN_TRANSIT
- DELIVERED
- DAMAGED
- LOST
- CANCELLED
terminal:
- DELIVERED
- DAMAGED
- LOST
- CANCELLED
invariants:
- 'INV-SHP-01: movement history (checkpoints) is append-only and chronologically gapless;
  no checkpoint is ever edited or removed (mirrors INV-AST-02''s gapless custody chain)'
- 'INV-SHP-02: delivered, damaged or lost quantity never exceeds the shipment''s planned
  quantity; a shortfall at delivery is recorded on the event, never silently rounded
  up to delivered in full'
- 'INV-SHP-03: departure (IN_TRANSIT) requires the linked logistics request''s allocation
  to still be COMMITTED for at least the shipped quantity at that instant — no shipment
  ever moves against capacity that was never actually reserved'
- 'INV-SHP-04: cancellation is only possible before departure (PLANNED); once IN_TRANSIT
  the shipment must resolve to DELIVERED, DAMAGED or LOST — never silently cancelled
  mid-transit'
entities:
- MovementEvent (location, at, note)
requirements:
- REQ-LOG-004
- REQ-LOG-005
- REQ-LOG-006
- REQ-LOG-007
- REQ-LOG-009
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-SHP-PLAN
  to: PLANNED
  guard: logistics_request APPROVED; origin pool with sufficient COMMITTED allocation
    quantity for the linked request; destination; carrier; planned_quantity ≤ the
    linked allocation's committed quantity
  event: EVT-SHP-PLANNED
  guard_error: SHIPMENT_INVALID
- from:
  - PLANNED
  command: CMD-SHP-DEPART
  to: IN_TRANSIT
  guard: carrier confirmed; departure checkpoint recorded
  event: EVT-SHP-DEPARTED
  guard_error: DEPARTURE_INVALID
- from:
  - IN_TRANSIT
  command: CMD-SHP-RECORD-CHECKPOINT
  to: '='
  guard: checkpoint strictly after the previous checkpoint in time (append-only, gapless
    — mirrors INV-AST-02); location; at; note
  event: EVT-SHP-CHECKPOINT-RECORDED
  guard_error: CHECKPOINT_INVALID
- from:
  - IN_TRANSIT
  command: CMD-SHP-DELIVER
  to: DELIVERED
  guard: receiving party confirms; delivered_quantity ≤ planned quantity; a shortfall
    is recorded, never hidden (INV-SHP-02)
  event: EVT-SHP-DELIVERED
  guard_error: DELIVERY_INVALID
- from:
  - IN_TRANSIT
  command: CMD-SHP-REPORT-DAMAGE
  to: DAMAGED
  guard: reason; damaged_quantity ≤ planned quantity; evidence
  event: EVT-SHP-DAMAGED
  guard_error: REASON_REQUIRED
- from:
  - IN_TRANSIT
  command: CMD-SHP-REPORT-LOST
  to: LOST
  guard: reason
  event: EVT-SHP-LOST
  guard_error: REASON_REQUIRED
- from:
  - PLANNED
  command: CMD-SHP-CANCEL
  to: CANCELLED
  guard: reason; only before departure
  event: EVT-SHP-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
