---
id: AGG-LOGISTICS-REQUEST
type: aggregate
title: Logistics Request
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
  - REQ-LOG-001
  - REQ-LOG-002
  - REQ-LOG-003
  - REQ-LOG-008
  - REQ-LOG-009
  - REQ-LOG-013
  - REQ-LOG-014
  state_machine: SM-LOGISTICS-REQUEST
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-LOGISTICS-REQUEST — Logistics Request

**الغرض:** طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-LGR-01** — every REQUESTED logistics request creates exactly one linked resource allocation in the same unit of work, targeting this request (CR-62); the two never diverge except through each other's own system-driven events
- **INV-LGR-02** — dispatch (IN_TRANSIT) is only possible from APPROVED, only while the linked allocation is still COMMITTED, and only for a ship_quantity not exceeding the requested quantity
- **INV-LGR-03** — FULFILLED requires delivered_quantity = requested quantity; anything less, including a total loss, is PARTIALLY_FULFILLED — never silently marked FULFILLED
- **INV-LGR-04** — cancellation always releases or lets expire the linked allocation; a CANCELLED request never leaves a dangling COMMITTED allocation
- **INV-LGR-05** — consumption is recorded on the linked allocation only from confirmed shipment outcomes (SLC-18 EVT-SHP-DELIVERED/-DAMAGED/-LOST), never speculatively at dispatch time

## الحالات

- غير نهائية: REQUESTED, PENDING_APPROVAL, APPROVED, IN_TRANSIT
- نهائية: FULFILLED, PARTIALLY_FULFILLED, REJECTED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-LGR-REQUEST | REQUESTED | item pool ACTIVE (AGG-RESOURCE-POOL, resource_type in RD-LOGISTICS-ITEM-TYPES); quantity > 0 in pool unit; destination; needed_by; priority 1–5; requester; justification; system issues a linked allocation request in the same unit of work (CMD-ALC-REQUEST, target = this request — CR-62) | EVT-LGR-REQUESTED | LOGISTICS_REQUEST_INVALID |
| REQUESTED | SYS:linked allocation committed | APPROVED | SLC-09 EVT-ALC-COMMITTED for the linked allocation | EVT-LGR-APPROVED | — |
| REQUESTED | SYS:linked allocation requires approval | PENDING_APPROVAL | SLC-09 EVT-ALC-APPROVAL-REQUIRED for the linked allocation | EVT-LGR-PENDING-APPROVAL | — |
| REQUESTED | SYS:linked allocation rejected | REJECTED | SLC-09 EVT-ALC-REJECTED for the linked allocation; reason codes carried over | EVT-LGR-REJECTED | — |
| PENDING_APPROVAL | SYS:linked allocation committed | APPROVED | SLC-09 EVT-ALC-COMMITTED for the linked allocation | EVT-LGR-APPROVED | — |
| PENDING_APPROVAL | SYS:linked allocation rejected | REJECTED | SLC-09 EVT-ALC-REJECTED for the linked allocation (approval denied or provisional hold elapsed) | EVT-LGR-REJECTED | — |
| APPROVED | CMD-LGR-DISPATCH | IN_TRANSIT | dispatcher; linked allocation still COMMITTED; creates a Shipment (AGG-SHIPMENT) referencing this request and the allocation; ship_quantity ≤ requested quantity | EVT-LGR-DISPATCHED | ALLOCATION_NOT_COMMITTED |
| IN_TRANSIT | SYS:linked shipment delivered in full | FULFILLED | SLC-18 EVT-SHP-DELIVERED with delivered_quantity = requested quantity; records consumption on the linked allocation (CMD-ALC-RECORD-CONSUMPTION) | EVT-LGR-FULFILLED | — |
| IN_TRANSIT | SYS:linked shipment resolved short | PARTIALLY_FULFILLED | SLC-18 EVT-SHP-DELIVERED with delivered_quantity < requested quantity, or EVT-SHP-DAMAGED / EVT-SHP-LOST; records consumption for the quantity actually delivered before the incident (possibly zero) | EVT-LGR-PARTIALLY-FULFILLED | — |
| REQUESTED, PENDING_APPROVAL, APPROVED | CMD-LGR-CANCEL | CANCELLED | requester or logistics authority; reason; releases the linked allocation if COMMITTED (CMD-ALC-RELEASE), or leaves a PENDING_APPROVAL allocation to its own provisional-hold expiry | EVT-LGR-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-LGR-REQUEST | SYS:linked allocation committed | SYS:linked allocation requires approval | SYS:linked allocation rejected | CMD-LGR-DISPATCH | SYS:linked shipment delivered in full | SYS:linked shipment resolved short | CMD-LGR-CANCEL |
|---|---|---|---|---|---|---|---|---|
| ∅ | → REQUESTED | — | — | — | — | — | — | — |
| REQUESTED | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | → APPROVED | → PENDING_APPROVAL | → REJECTED | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | → CANCELLED |
| PENDING_APPROVAL | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | → APPROVED | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | → REJECTED | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | → CANCELLED |
| APPROVED | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | → IN_TRANSIT | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | → CANCELLED |
| IN_TRANSIT | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | → FULFILLED | → PARTIALLY_FULFILLED | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
| FULFILLED | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
| PARTIALLY_FULFILLED | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
| REJECTED | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | ✗ LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |

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
id: AGG-LOGISTICS-REQUEST
bc: BC05
name: Logistics Request
tier: T2
purpose: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09)
  وشحنة تُنفّذه
states:
- REQUESTED
- PENDING_APPROVAL
- APPROVED
- IN_TRANSIT
- FULFILLED
- PARTIALLY_FULFILLED
- REJECTED
- CANCELLED
terminal:
- FULFILLED
- PARTIALLY_FULFILLED
- REJECTED
- CANCELLED
invariants:
- 'INV-LGR-01: every REQUESTED logistics request creates exactly one linked resource
  allocation in the same unit of work, targeting this request (CR-62); the two never
  diverge except through each other''s own system-driven events'
- 'INV-LGR-02: dispatch (IN_TRANSIT) is only possible from APPROVED, only while the
  linked allocation is still COMMITTED, and only for a ship_quantity not exceeding
  the requested quantity'
- 'INV-LGR-03: FULFILLED requires delivered_quantity = requested quantity; anything
  less, including a total loss, is PARTIALLY_FULFILLED — never silently marked FULFILLED'
- 'INV-LGR-04: cancellation always releases or lets expire the linked allocation;
  a CANCELLED request never leaves a dangling COMMITTED allocation'
- 'INV-LGR-05: consumption is recorded on the linked allocation only from confirmed
  shipment outcomes (SLC-18 EVT-SHP-DELIVERED/-DAMAGED/-LOST), never speculatively
  at dispatch time'
entities: []
requirements:
- REQ-LOG-001
- REQ-LOG-002
- REQ-LOG-003
- REQ-LOG-008
- REQ-LOG-009
- REQ-LOG-013
- REQ-LOG-014
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-LGR-REQUEST
  to: REQUESTED
  guard: item pool ACTIVE (AGG-RESOURCE-POOL, resource_type in RD-LOGISTICS-ITEM-TYPES);
    quantity > 0 in pool unit; destination; needed_by; priority 1–5; requester; justification;
    system issues a linked allocation request in the same unit of work (CMD-ALC-REQUEST,
    target = this request — CR-62)
  event: EVT-LGR-REQUESTED
  guard_error: LOGISTICS_REQUEST_INVALID
- from:
  - REQUESTED
  command: SYS:linked allocation committed
  to: APPROVED
  guard: SLC-09 EVT-ALC-COMMITTED for the linked allocation
  event: EVT-LGR-APPROVED
  guard_error: null
- from:
  - REQUESTED
  command: SYS:linked allocation requires approval
  to: PENDING_APPROVAL
  guard: SLC-09 EVT-ALC-APPROVAL-REQUIRED for the linked allocation
  event: EVT-LGR-PENDING-APPROVAL
  guard_error: null
- from:
  - REQUESTED
  command: SYS:linked allocation rejected
  to: REJECTED
  guard: SLC-09 EVT-ALC-REJECTED for the linked allocation; reason codes carried over
  event: EVT-LGR-REJECTED
  guard_error: null
- from:
  - PENDING_APPROVAL
  command: SYS:linked allocation committed
  to: APPROVED
  guard: SLC-09 EVT-ALC-COMMITTED for the linked allocation
  event: EVT-LGR-APPROVED
  guard_error: null
- from:
  - PENDING_APPROVAL
  command: SYS:linked allocation rejected
  to: REJECTED
  guard: SLC-09 EVT-ALC-REJECTED for the linked allocation (approval denied or provisional
    hold elapsed)
  event: EVT-LGR-REJECTED
  guard_error: null
- from:
  - APPROVED
  command: CMD-LGR-DISPATCH
  to: IN_TRANSIT
  guard: dispatcher; linked allocation still COMMITTED; creates a Shipment (AGG-SHIPMENT)
    referencing this request and the allocation; ship_quantity ≤ requested quantity
  event: EVT-LGR-DISPATCHED
  guard_error: ALLOCATION_NOT_COMMITTED
- from:
  - IN_TRANSIT
  command: SYS:linked shipment delivered in full
  to: FULFILLED
  guard: SLC-18 EVT-SHP-DELIVERED with delivered_quantity = requested quantity; records
    consumption on the linked allocation (CMD-ALC-RECORD-CONSUMPTION)
  event: EVT-LGR-FULFILLED
  guard_error: null
- from:
  - IN_TRANSIT
  command: SYS:linked shipment resolved short
  to: PARTIALLY_FULFILLED
  guard: SLC-18 EVT-SHP-DELIVERED with delivered_quantity < requested quantity, or
    EVT-SHP-DAMAGED / EVT-SHP-LOST; records consumption for the quantity actually
    delivered before the incident (possibly zero)
  event: EVT-LGR-PARTIALLY-FULFILLED
  guard_error: null
- from:
  - REQUESTED
  - PENDING_APPROVAL
  - APPROVED
  command: CMD-LGR-CANCEL
  to: CANCELLED
  guard: requester or logistics authority; reason; releases the linked allocation
    if COMMITTED (CMD-ALC-RELEASE), or leaves a PENDING_APPROVAL allocation to its
    own provisional-hold expiry
  event: EVT-LGR-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
