---
id: AGG-EXERCISE
type: aggregate
title: Exercise
wave: W4
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
bounded_context: BC05
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-TRX-003
  - REQ-TRX-004
  - REQ-TRX-005
  - REQ-TRX-006
  - REQ-TRX-007
  state_machine: SM-EXERCISE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-EXERCISE — Exercise

**الغرض:** حدث تدريبي/جاهزية مجدوَل ينفّذ سيناريو محدَّداً لمجموعة مشاركين  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-EXR-01** — an exercise is planned only against a scenario that is ACTIVE at that instant; the reference is frozen — later scenario edits (new versions) never retroactively change an already-planned exercise
- **INV-EXR-02** — an exercise's terminal outcome (COMPLETED vs ABORTED) is always driven exclusively by its linked simulation's own outcome; no human command sets either state directly

## الحالات

- غير نهائية: PLANNED, SCHEDULED, IN_PROGRESS
- نهائية: COMPLETED, ABORTED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-EXR-PLAN | PLANNED | scenario ACTIVE at this instant, frozen thereafter (INV-EXR-01); objectives; participants; purpose; role_ref optional (readiness comparison reuses SLC-09's AGG-ROLE-REQUIREMENT read-only, no new eligibility mechanism) | EVT-EXR-PLANNED | EXERCISE_INVALID |
| PLANNED | CMD-EXR-SCHEDULE | SCHEDULED | window.from < window.to; location; participants confirmed | EVT-EXR-SCHEDULED | EXERCISE_INVALID |
| SCHEDULED | CMD-EXR-START | IN_PROGRESS | scheduled window reached (or authorized override); system creates a linked Simulation in the same unit of work (CMD-SIM-START, exercise_ref = this, scenario_ref = the frozen scenario — mirrors the linked-creation pattern of CR-62) | EVT-EXR-STARTED | EXERCISE_INVALID |
| IN_PROGRESS | SYS:linked simulation completed | COMPLETED | system; driven exclusively by the linked Simulation's own EVT-SIM-COMPLETED (INV-EXR-02) | EVT-EXR-COMPLETED | — |
| IN_PROGRESS | SYS:linked simulation aborted | ABORTED | system; driven exclusively by the linked Simulation's own EVT-SIM-ABORTED (INV-EXR-02) | EVT-EXR-ABORTED | — |
| PLANNED, SCHEDULED | CMD-EXR-CANCEL | CANCELLED | reason | EVT-EXR-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-EXR-PLAN | CMD-EXR-SCHEDULE | CMD-EXR-START | CMD-EXR-CANCEL | SYS:linked simulation completed | SYS:linked simulation aborted |
|---|---|---|---|---|---|---|
| ∅ | → PLANNED | — | — | — | — | — |
| PLANNED | ✗ EXERCISE_INVALID_STATE_TRANSITION | → SCHEDULED | ✗ EXERCISE_INVALID_STATE_TRANSITION | → CANCELLED | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION |
| SCHEDULED | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | → IN_PROGRESS | → CANCELLED | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION |
| IN_PROGRESS | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | → COMPLETED | → ABORTED |
| COMPLETED | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION |
| ABORTED | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION | ✗ EXERCISE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-19.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-EXERCISE
bc: BC05
name: Exercise
tier: T2
purpose: حدث تدريبي/جاهزية مجدوَل ينفّذ سيناريو محدَّداً لمجموعة مشاركين
states:
- PLANNED
- SCHEDULED
- IN_PROGRESS
- COMPLETED
- ABORTED
- CANCELLED
terminal:
- COMPLETED
- ABORTED
- CANCELLED
invariants:
- 'INV-EXR-01: an exercise is planned only against a scenario that is ACTIVE at that
  instant; the reference is frozen — later scenario edits (new versions) never retroactively
  change an already-planned exercise'
- 'INV-EXR-02: an exercise''s terminal outcome (COMPLETED vs ABORTED) is always driven
  exclusively by its linked simulation''s own outcome; no human command sets either
  state directly'
entities: []
requirements:
- REQ-TRX-003
- REQ-TRX-004
- REQ-TRX-005
- REQ-TRX-006
- REQ-TRX-007
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-EXR-PLAN
  to: PLANNED
  guard: scenario ACTIVE at this instant, frozen thereafter (INV-EXR-01); objectives;
    participants; purpose; role_ref optional (readiness comparison reuses SLC-09's
    AGG-ROLE-REQUIREMENT read-only, no new eligibility mechanism)
  event: EVT-EXR-PLANNED
  guard_error: EXERCISE_INVALID
- from:
  - PLANNED
  command: CMD-EXR-SCHEDULE
  to: SCHEDULED
  guard: window.from < window.to; location; participants confirmed
  event: EVT-EXR-SCHEDULED
  guard_error: EXERCISE_INVALID
- from:
  - SCHEDULED
  command: CMD-EXR-START
  to: IN_PROGRESS
  guard: scheduled window reached (or authorized override); system creates a linked
    Simulation in the same unit of work (CMD-SIM-START, exercise_ref = this, scenario_ref
    = the frozen scenario — mirrors the linked-creation pattern of CR-62)
  event: EVT-EXR-STARTED
  guard_error: EXERCISE_INVALID
- from:
  - IN_PROGRESS
  command: 'SYS:linked simulation completed'
  to: COMPLETED
  guard: system; driven exclusively by the linked Simulation's own EVT-SIM-COMPLETED
    (INV-EXR-02)
  event: EVT-EXR-COMPLETED
  guard_error: null
- from:
  - IN_PROGRESS
  command: 'SYS:linked simulation aborted'
  to: ABORTED
  guard: system; driven exclusively by the linked Simulation's own EVT-SIM-ABORTED
    (INV-EXR-02)
  event: EVT-EXR-ABORTED
  guard_error: null
- from:
  - PLANNED
  - SCHEDULED
  command: CMD-EXR-CANCEL
  to: CANCELLED
  guard: reason
  event: EVT-EXR-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
