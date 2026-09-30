---
id: AGG-ASSET-RESERVATION
type: aggregate
title: Asset Reservation
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
  - REQ-RES-014
  state_machine: SM-ASSET-RESERVATION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ASSET-RESERVATION — Asset Reservation

**الغرض:** حجز أصل لنافذة زمنية قبل الاستخدام  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-RSV-01** — no two HELD/CONFIRMED reservations of one asset overlap in time (exclusion on (asset, window)) — REQ-RES-014
- **INV-RSV-02** — a HELD reservation expires after 24 h unless confirmed (W4 delegated decision)

## الحالات

- غير نهائية: HELD, CONFIRMED
- نهائية: RELEASED, EXPIRED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-RSV-HOLD | HELD | asset available for the window (INV-AST-01); purpose; requester authorized in asset owner scope | EVT-RSV-HELD | ASSET_RESERVED |
| HELD | CMD-RSV-CONFIRM | CONFIRMED | linked to a task or plan activity | EVT-RSV-CONFIRMED | LINK_REQUIRED |
| HELD | SYS:hold expiry (24 h) reached | EXPIRED | scheduler | EVT-RSV-EXPIRED | — |
| CONFIRMED | CMD-RSV-RELEASE | RELEASED | requester or linked task terminal | EVT-RSV-RELEASED | — |
| CONFIRMED | SYS:linked task or plan terminal | RELEASED | SLC-03/SLC-08 events | EVT-RSV-RELEASED | — |
| HELD, CONFIRMED | CMD-RSV-CANCEL | CANCELLED | requester or asset owner; reason | EVT-RSV-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-RSV-HOLD | CMD-RSV-CONFIRM | SYS:hold expiry (24 h) reached | CMD-RSV-RELEASE | SYS:linked task or plan terminal | CMD-RSV-CANCEL |
|---|---|---|---|---|---|---|
| ∅ | → HELD | — | — | — | — | — |
| HELD | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | → CONFIRMED | → EXPIRED | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | → CANCELLED |
| CONFIRMED | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | → RELEASED | → RELEASED | → CANCELLED |
| RELEASED | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION |
| EXPIRED | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION | ✗ ASSET_RESERVATION_INVALID_STATE_TRANSITION |

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
id: AGG-ASSET-RESERVATION
bc: BC05
name: Asset Reservation
tier: T2
purpose: حجز أصل لنافذة زمنية قبل الاستخدام
states:
- HELD
- CONFIRMED
- RELEASED
- EXPIRED
- CANCELLED
terminal:
- RELEASED
- EXPIRED
- CANCELLED
invariants:
- 'INV-RSV-01: no two HELD/CONFIRMED reservations of one asset overlap in time (exclusion
  on (asset, window)) — REQ-RES-014'
- 'INV-RSV-02: a HELD reservation expires after 24 h unless confirmed (W4 delegated
  decision)'
entities: []
requirements:
- REQ-RES-014
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-RSV-HOLD
  to: HELD
  guard: asset available for the window (INV-AST-01); purpose; requester authorized
    in asset owner scope
  event: EVT-RSV-HELD
  guard_error: ASSET_RESERVED
- from:
  - HELD
  command: CMD-RSV-CONFIRM
  to: CONFIRMED
  guard: linked to a task or plan activity
  event: EVT-RSV-CONFIRMED
  guard_error: LINK_REQUIRED
- from:
  - HELD
  command: SYS:hold expiry (24 h) reached
  to: EXPIRED
  guard: scheduler
  event: EVT-RSV-EXPIRED
  guard_error: null
- from:
  - CONFIRMED
  command: CMD-RSV-RELEASE
  to: RELEASED
  guard: requester or linked task terminal
  event: EVT-RSV-RELEASED
  guard_error: null
- from:
  - CONFIRMED
  command: SYS:linked task or plan terminal
  to: RELEASED
  guard: SLC-03/SLC-08 events
  event: EVT-RSV-RELEASED
  guard_error: null
- from:
  - HELD
  - CONFIRMED
  command: CMD-RSV-CANCEL
  to: CANCELLED
  guard: requester or asset owner; reason
  event: EVT-RSV-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
