---
id: AGG-RESOURCE-POOL
type: aggregate
title: Resource Pool
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
  - REQ-RES-006
  state_machine: SM-RESOURCE-POOL
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-RESOURCE-POOL — Resource Pool

**الغرض:** مجمع موارد قابلة للعد أو القياس بسعة متغيرة زمنياً  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-RPL-01** — capacity is a time series (valid_from); history kept (bitemporal record)
- **INV-RPL-02** — for every time bucket, Σ committed quantity ≤ capacity (enforced by the capacity ledger — SPEC-ALLOCATION §2)

## مكونات داخلية

- CapacitySeries
- CapacityLedgerBucket (hour)

## الحالات

- غير نهائية: ACTIVE, SUSPENDED
- نهائية: CLOSED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-RPL-CREATE | ACTIVE | type in RD-RESOURCE-TYPES; unit (UCUM); org scope; initial capacity; label | EVT-RPL-CREATED | POOL_INVALID |
| ACTIVE, SUSPENDED | CMD-RPL-ADJUST-CAPACITY | (بلا تغيير) | new capacity with valid_from; reason; a reduction below committed quantity requires pre-emption decisions first | EVT-RPL-CAPACITY-ADJUSTED | CAPACITY_BELOW_COMMITMENTS |
| ACTIVE | CMD-RPL-SUSPEND | SUSPENDED | reason; no new allocations | EVT-RPL-SUSPENDED | REASON_REQUIRED |
| SUSPENDED | CMD-RPL-RESUME | ACTIVE | — | EVT-RPL-RESUMED | — |
| ACTIVE, SUSPENDED | CMD-RPL-CLOSE | CLOSED | no COMMITTED or PENDING allocations | EVT-RPL-CLOSED | POOL_HAS_COMMITMENTS |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-RPL-CREATE | CMD-RPL-ADJUST-CAPACITY | CMD-RPL-SUSPEND | CMD-RPL-RESUME | CMD-RPL-CLOSE |
|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — |
| ACTIVE | ✗ RESOURCE_POOL_INVALID_STATE_TRANSITION | → ACTIVE | → SUSPENDED | ✗ RESOURCE_POOL_INVALID_STATE_TRANSITION | → CLOSED |
| SUSPENDED | ✗ RESOURCE_POOL_INVALID_STATE_TRANSITION | → SUSPENDED | ✗ RESOURCE_POOL_INVALID_STATE_TRANSITION | → ACTIVE | → CLOSED |
| CLOSED | ✗ RESOURCE_POOL_INVALID_STATE_TRANSITION | ✗ RESOURCE_POOL_INVALID_STATE_TRANSITION | ✗ RESOURCE_POOL_INVALID_STATE_TRANSITION | ✗ RESOURCE_POOL_INVALID_STATE_TRANSITION | ✗ RESOURCE_POOL_INVALID_STATE_TRANSITION |

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
id: AGG-RESOURCE-POOL
bc: BC05
name: Resource Pool
tier: T2
purpose: مجمع موارد قابلة للعد أو القياس بسعة متغيرة زمنياً
states:
- ACTIVE
- SUSPENDED
- CLOSED
terminal:
- CLOSED
invariants:
- 'INV-RPL-01: capacity is a time series (valid_from); history kept (bitemporal record)'
- 'INV-RPL-02: for every time bucket, Σ committed quantity ≤ capacity (enforced by
  the capacity ledger — SPEC-ALLOCATION §2)'
entities:
- CapacitySeries
- CapacityLedgerBucket (hour)
requirements:
- REQ-RES-006
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-RPL-CREATE
  to: ACTIVE
  guard: type in RD-RESOURCE-TYPES; unit (UCUM); org scope; initial capacity; label
  event: EVT-RPL-CREATED
  guard_error: POOL_INVALID
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-RPL-ADJUST-CAPACITY
  to: '='
  guard: new capacity with valid_from; reason; a reduction below committed quantity
    requires pre-emption decisions first
  event: EVT-RPL-CAPACITY-ADJUSTED
  guard_error: CAPACITY_BELOW_COMMITMENTS
- from:
  - ACTIVE
  command: CMD-RPL-SUSPEND
  to: SUSPENDED
  guard: reason; no new allocations
  event: EVT-RPL-SUSPENDED
  guard_error: REASON_REQUIRED
- from:
  - SUSPENDED
  command: CMD-RPL-RESUME
  to: ACTIVE
  guard: —
  event: EVT-RPL-RESUMED
  guard_error: null
- from:
  - ACTIVE
  - SUSPENDED
  command: CMD-RPL-CLOSE
  to: CLOSED
  guard: no COMMITTED or PENDING allocations
  event: EVT-RPL-CLOSED
  guard_error: POOL_HAS_COMMITMENTS
```

</details>
