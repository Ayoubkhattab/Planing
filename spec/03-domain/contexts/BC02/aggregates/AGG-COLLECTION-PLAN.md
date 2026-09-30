---
id: AGG-COLLECTION-PLAN
type: aggregate
title: Collection Plan
wave: W4
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-COL-002
  state_machine: SM-COLLECTION-PLAN
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-COLLECTION-PLAN — Collection Plan

**الغرض:** خطة جمع: أنشطة بأساليب ومصادر وفرق، تولّد مهام ميدانية  
**السياق:** BC02 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-CPL-01** — every activity serves ≥ 1 EEI of an approved requirement
- **INV-CPL-02** — tasks created by activation link back to the activity (REQ-COL-002)

## مكونات داخلية

- CollectionActivity (method, sources, area, window, unit, task_type, eei_refs, task_ref)

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: COMPLETED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-CPL-CREATE | DRAFT | ≥ 1 APPROVED collection requirement; planner in scope; label ≥ requirements | EVT-CPL-CREATED | REQUIREMENT_NOT_APPROVED |
| DRAFT, ACTIVE | CMD-CPL-ADD-ACTIVITY | (بلا تغيير) | method in RD-COLLECTION-METHODS; source(s) ACTIVE; area ⊆ requirement areas; window ⊆ requirement windows; assigned unit; task type | EVT-CPL-ACTIVITY-ADDED | ACTIVITY_INVALID |
| DRAFT | CMD-CPL-REMOVE-ACTIVITY | (بلا تغيير) | activity not yet tasked | EVT-CPL-ACTIVITY-REMOVED | ACTIVITY_ALREADY_TASKED |
| DRAFT | CMD-CPL-ACTIVATE | ACTIVE | ≥ 1 activity; creates one field task per activity through SLC-03 with plan_ref = this collection plan (CR-59) | EVT-CPL-ACTIVATED | PLAN_EMPTY |
| ACTIVE | SYS:all activity tasks terminal | COMPLETED | SLC-03 events | EVT-CPL-COMPLETED | — |
| ACTIVE | CMD-CPL-COMPLETE | COMPLETED | planner; open tasks cancelled with reason | EVT-CPL-COMPLETED | REASON_REQUIRED |
| DRAFT, ACTIVE | CMD-CPL-CANCEL | CANCELLED | reason; open tasks cancelled | EVT-CPL-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-CPL-CREATE | CMD-CPL-ADD-ACTIVITY | CMD-CPL-REMOVE-ACTIVITY | CMD-CPL-ACTIVATE | SYS:all activity tasks terminal | CMD-CPL-COMPLETE | CMD-CPL-CANCEL |
|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — |
| DRAFT | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | → DRAFT | → DRAFT | → ACTIVE | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | → CANCELLED |
| ACTIVE | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | → ACTIVE | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | → COMPLETED | → COMPLETED | → CANCELLED |
| COMPLETED | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION | ✗ COLLECTION_PLAN_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-14.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-COLLECTION-PLAN
bc: BC02
name: Collection Plan
tier: T2
purpose: 'خطة جمع: أنشطة بأساليب ومصادر وفرق، تولّد مهام ميدانية'
states:
- DRAFT
- ACTIVE
- COMPLETED
- CANCELLED
terminal:
- COMPLETED
- CANCELLED
invariants:
- 'INV-CPL-01: every activity serves ≥ 1 EEI of an approved requirement'
- 'INV-CPL-02: tasks created by activation link back to the activity (REQ-COL-002)'
entities:
- CollectionActivity (method, sources, area, window, unit, task_type, eei_refs, task_ref)
requirements:
- REQ-COL-002
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-CPL-CREATE
  to: DRAFT
  guard: ≥ 1 APPROVED collection requirement; planner in scope; label ≥ requirements
  event: EVT-CPL-CREATED
  guard_error: REQUIREMENT_NOT_APPROVED
- from:
  - DRAFT
  - ACTIVE
  command: CMD-CPL-ADD-ACTIVITY
  to: '='
  guard: method in RD-COLLECTION-METHODS; source(s) ACTIVE; area ⊆ requirement areas;
    window ⊆ requirement windows; assigned unit; task type
  event: EVT-CPL-ACTIVITY-ADDED
  guard_error: ACTIVITY_INVALID
- from:
  - DRAFT
  command: CMD-CPL-REMOVE-ACTIVITY
  to: '='
  guard: activity not yet tasked
  event: EVT-CPL-ACTIVITY-REMOVED
  guard_error: ACTIVITY_ALREADY_TASKED
- from:
  - DRAFT
  command: CMD-CPL-ACTIVATE
  to: ACTIVE
  guard: ≥ 1 activity; creates one field task per activity through SLC-03 with plan_ref
    = this collection plan (CR-59)
  event: EVT-CPL-ACTIVATED
  guard_error: PLAN_EMPTY
- from:
  - ACTIVE
  command: SYS:all activity tasks terminal
  to: COMPLETED
  guard: SLC-03 events
  event: EVT-CPL-COMPLETED
  guard_error: null
- from:
  - ACTIVE
  command: CMD-CPL-COMPLETE
  to: COMPLETED
  guard: planner; open tasks cancelled with reason
  event: EVT-CPL-COMPLETED
  guard_error: REASON_REQUIRED
- from:
  - DRAFT
  - ACTIVE
  command: CMD-CPL-CANCEL
  to: CANCELLED
  guard: reason; open tasks cancelled
  event: EVT-CPL-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
