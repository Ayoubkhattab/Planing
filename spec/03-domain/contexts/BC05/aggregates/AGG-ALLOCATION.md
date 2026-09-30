---
id: AGG-ALLOCATION
type: aggregate
title: Resource Allocation
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
  - REQ-RES-007
  - REQ-RES-008
  - REQ-RES-009
  - REQ-RES-010
  - REQ-RES-011
  - REQ-RES-012
  state_machine: SM-ALLOCATION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ALLOCATION — Resource Allocation

**الغرض:** التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-ALC-01** — COMMITTED quantity is reserved in the capacity ledger for every hour of its window; release returns the unused part
- **INV-ALC-02** — contention is resolved by priority, then request time, inside each pool's ordering window (SPEC-ALLOCATION §2)
- **INV-ALC-03** — pre-emption only through a recorded decision with authority; never automatic
- **INV-ALC-04** — approver ≠ requester when approval is required

## مكونات داخلية

- CheckResult
- ConsumptionRecord

## الحالات

- غير نهائية: REQUESTED, PENDING_APPROVAL, COMMITTED
- نهائية: REJECTED, PREEMPTED, RELEASED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ALC-REQUEST | REQUESTED | pool ACTIVE; quantity > 0 in pool unit; window; priority 1–5; target task/activity/logistics-request (CR-62, SLC-18); requester | EVT-ALC-REQUESTED | ALLOCATION_INVALID |
| REQUESTED | SYS:all checks passed | COMMITTED | SPEC-ALLOCATION §1 checks + capacity ledger reserve in priority order (§2) | EVT-ALC-COMMITTED | — |
| REQUESTED | SYS:checks passed, policy requires approval | PENDING_APPROVAL | PDP obligation REQUIRE_APPROVAL; capacity provisionally held ≤ 1 h | EVT-ALC-APPROVAL-REQUIRED | — |
| REQUESTED | SYS:a check failed | REJECTED | reason codes per failed check | EVT-ALC-REJECTED | — |
| PENDING_APPROVAL | CMD-ALC-APPROVE | COMMITTED | approver with allocation authority ≠ requester; capacity still available | EVT-ALC-COMMITTED | CAPACITY_UNAVAILABLE |
| PENDING_APPROVAL | CMD-ALC-REJECT | REJECTED | reason | EVT-ALC-REJECTED | REASON_REQUIRED |
| PENDING_APPROVAL | SYS:provisional hold (1 h) elapsed | REJECTED | capacity released | EVT-ALC-REJECTED | — |
| COMMITTED | CMD-ALC-RECORD-CONSUMPTION | (بلا تغيير) | quantity in pool unit; time; consumption beyond commitment flagged (REQ-RES-010) | EVT-ALC-CONSUMED | CONSUMPTION_INVALID |
| COMMITTED | CMD-ALC-PREEMPT | PREEMPTED | pre-emption decision (BC04 Decision) by an authority for the pool scope; higher-priority allocation reference; owners notified (REQ-RES-009) | EVT-ALC-PREEMPTED | AUTHORITY_REQUIRED |
| COMMITTED | CMD-ALC-RELEASE | RELEASED | requester or task owner; unused quantity returned to the ledger | EVT-ALC-RELEASED | — |
| COMMITTED | SYS:linked task terminal | RELEASED | SLC-03 events (REQ-RES-011) | EVT-ALC-RELEASED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ALC-REQUEST | SYS:all checks passed | SYS:checks passed, policy requires approval | SYS:a check failed | CMD-ALC-APPROVE | CMD-ALC-REJECT | SYS:provisional hold (1 h) elapsed | CMD-ALC-RECORD-CONSUMPTION | CMD-ALC-PREEMPT | CMD-ALC-RELEASE | SYS:linked task terminal |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → REQUESTED | — | — | — | — | — | — | — | — | — | — |
| REQUESTED | ✗ ALLOCATION_INVALID_STATE_TRANSITION | → COMMITTED | → PENDING_APPROVAL | → REJECTED | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION |
| PENDING_APPROVAL | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | → COMMITTED | → REJECTED | → REJECTED | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION |
| COMMITTED | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | → COMMITTED | → PREEMPTED | → RELEASED | → RELEASED |
| REJECTED | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION |
| PREEMPTED | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION |
| RELEASED | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION | ✗ ALLOCATION_INVALID_STATE_TRANSITION |

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
id: AGG-ALLOCATION
bc: BC05
name: Resource Allocation
tier: T2
purpose: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية
states:
- REQUESTED
- PENDING_APPROVAL
- COMMITTED
- REJECTED
- PREEMPTED
- RELEASED
terminal:
- REJECTED
- PREEMPTED
- RELEASED
invariants:
- 'INV-ALC-01: COMMITTED quantity is reserved in the capacity ledger for every hour
  of its window; release returns the unused part'
- 'INV-ALC-02: contention is resolved by priority, then request time, inside each
  pool''s ordering window (SPEC-ALLOCATION §2)'
- 'INV-ALC-03: pre-emption only through a recorded decision with authority; never
  automatic'
- 'INV-ALC-04: approver ≠ requester when approval is required'
entities:
- CheckResult
- ConsumptionRecord
requirements:
- REQ-RES-007
- REQ-RES-008
- REQ-RES-009
- REQ-RES-010
- REQ-RES-011
- REQ-RES-012
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-ALC-REQUEST
  to: REQUESTED
  guard: pool ACTIVE; quantity > 0 in pool unit; window; priority 1–5; target task/activity/logistics-request
    (CR-62, SLC-18); requester
  event: EVT-ALC-REQUESTED
  guard_error: ALLOCATION_INVALID
- from:
  - REQUESTED
  command: SYS:all checks passed
  to: COMMITTED
  guard: SPEC-ALLOCATION §1 checks + capacity ledger reserve in priority order (§2)
  event: EVT-ALC-COMMITTED
  guard_error: null
- from:
  - REQUESTED
  command: SYS:checks passed, policy requires approval
  to: PENDING_APPROVAL
  guard: PDP obligation REQUIRE_APPROVAL; capacity provisionally held ≤ 1 h
  event: EVT-ALC-APPROVAL-REQUIRED
  guard_error: null
- from:
  - REQUESTED
  command: SYS:a check failed
  to: REJECTED
  guard: reason codes per failed check
  event: EVT-ALC-REJECTED
  guard_error: null
- from:
  - PENDING_APPROVAL
  command: CMD-ALC-APPROVE
  to: COMMITTED
  guard: approver with allocation authority ≠ requester; capacity still available
  event: EVT-ALC-COMMITTED
  guard_error: CAPACITY_UNAVAILABLE
- from:
  - PENDING_APPROVAL
  command: CMD-ALC-REJECT
  to: REJECTED
  guard: reason
  event: EVT-ALC-REJECTED
  guard_error: REASON_REQUIRED
- from:
  - PENDING_APPROVAL
  command: SYS:provisional hold (1 h) elapsed
  to: REJECTED
  guard: capacity released
  event: EVT-ALC-REJECTED
  guard_error: null
- from:
  - COMMITTED
  command: CMD-ALC-RECORD-CONSUMPTION
  to: '='
  guard: quantity in pool unit; time; consumption beyond commitment flagged (REQ-RES-010)
  event: EVT-ALC-CONSUMED
  guard_error: CONSUMPTION_INVALID
- from:
  - COMMITTED
  command: CMD-ALC-PREEMPT
  to: PREEMPTED
  guard: pre-emption decision (BC04 Decision) by an authority for the pool scope;
    higher-priority allocation reference; owners notified (REQ-RES-009)
  event: EVT-ALC-PREEMPTED
  guard_error: AUTHORITY_REQUIRED
- from:
  - COMMITTED
  command: CMD-ALC-RELEASE
  to: RELEASED
  guard: requester or task owner; unused quantity returned to the ledger
  event: EVT-ALC-RELEASED
  guard_error: null
- from:
  - COMMITTED
  command: SYS:linked task terminal
  to: RELEASED
  guard: SLC-03 events (REQ-RES-011)
  event: EVT-ALC-RELEASED
  guard_error: null
```

</details>
