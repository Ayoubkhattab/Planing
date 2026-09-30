---
id: AGG-ASSET-ASSIGNMENT
type: aggregate
title: Asset Assignment
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
  - REQ-RES-003
  - REQ-RES-012
  state_machine: SM-ASSET-ASSIGNMENT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ASSET-ASSIGNMENT — Asset Assignment

**الغرض:** استخدام فعلي لأصل في مهمة أو وحدة  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-ASG-01** — at most one ACTIVE assignment per asset at a time
- **INV-ASG-02** — assignment respects BRL-007 (asset certification and custody authorization)

## الحالات

- غير نهائية: ACTIVE
- نهائية: RETURNED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ASG-ASSIGN | ACTIVE | asset available (or covered by the caller's CONFIRMED reservation); asset certifications satisfy the task type's asset requirements; custody authorization; assignee cleared for asset label | EVT-ASG-ASSIGNED | ASSET_NOT_AVAILABLE |
| ACTIVE | CMD-ASG-RETURN | RETURNED | condition report; asset condition updated accordingly | EVT-ASG-RETURNED | CONDITION_REPORT_REQUIRED |
| ACTIVE | SYS:linked task terminal | RETURNED | condition report requested from last holder (follow-up task) | EVT-ASG-RETURNED | — |
| ACTIVE | CMD-ASG-CANCEL | CANCELLED | assigned in error; reason | EVT-ASG-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ASG-ASSIGN | CMD-ASG-RETURN | SYS:linked task terminal | CMD-ASG-CANCEL |
|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — |
| ACTIVE | ✗ ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION | → RETURNED | → RETURNED | → CANCELLED |
| RETURNED | ✗ ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION | ✗ ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION | ✗ ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION | ✗ ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION | ✗ ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION | ✗ ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION | ✗ ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION |

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
id: AGG-ASSET-ASSIGNMENT
bc: BC05
name: Asset Assignment
tier: T2
purpose: استخدام فعلي لأصل في مهمة أو وحدة
states:
- ACTIVE
- RETURNED
- CANCELLED
terminal:
- RETURNED
- CANCELLED
invariants:
- 'INV-ASG-01: at most one ACTIVE assignment per asset at a time'
- 'INV-ASG-02: assignment respects BRL-007 (asset certification and custody authorization)'
entities: []
requirements:
- REQ-RES-003
- REQ-RES-012
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-ASG-ASSIGN
  to: ACTIVE
  guard: asset available (or covered by the caller's CONFIRMED reservation); asset
    certifications satisfy the task type's asset requirements; custody authorization;
    assignee cleared for asset label
  event: EVT-ASG-ASSIGNED
  guard_error: ASSET_NOT_AVAILABLE
- from:
  - ACTIVE
  command: CMD-ASG-RETURN
  to: RETURNED
  guard: condition report; asset condition updated accordingly
  event: EVT-ASG-RETURNED
  guard_error: CONDITION_REPORT_REQUIRED
- from:
  - ACTIVE
  command: SYS:linked task terminal
  to: RETURNED
  guard: condition report requested from last holder (follow-up task)
  event: EVT-ASG-RETURNED
  guard_error: null
- from:
  - ACTIVE
  command: CMD-ASG-CANCEL
  to: CANCELLED
  guard: assigned in error; reason
  event: EVT-ASG-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
