---
id: AGG-SIMULATION
type: aggregate
title: Simulation
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
  - REQ-TRX-008
  - REQ-TRX-009
  - REQ-TRX-010
  - REQ-TRX-011
  state_machine: SM-SIMULATION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SIMULATION — Simulation

**الغرض:** تنفيذ فعلي واحد لتمرين: تسليم الحقن، تسجيل التقييمات، والانتهاء إلى نتيجة نهائية  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-SIM-01** — inject deliveries are append-only and strictly increasing in time (mirrors INV-SHP-01's checkpoint pattern); no edit or delete command exists
- **INV-SIM-02** — a simulation reaches COMPLETED only when every participant listed on its linked exercise has at least one recorded evaluation
- **INV-SIM-03** — an evaluator never evaluates themself (segregation of duties, mirrors CMD-RRQ-ACTIVATE/CMD-KNO-PUBLISH's reviewer ≠ author pattern)

## مكونات داخلية

- InjectDelivery (inject_ref, delivered_at, note)
- Evaluation (participant_ref, competency_code, result, evaluator, notes)

## الحالات

- غير نهائية: IN_PROGRESS, PAUSED
- نهائية: COMPLETED, ABORTED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-SIM-START | IN_PROGRESS | system-issued in the same unit of work as CMD-EXR-START; exercise_ref SCHEDULED transitioning to IN_PROGRESS; scenario_ref = the exercise's frozen scenario; started_at | EVT-SIM-STARTED | SIMULATION_INVALID |
| IN_PROGRESS | CMD-SIM-DELIVER-INJECT | (بلا تغيير) | inject_ref belongs to the linked scenario; delivered_at strictly after the previous delivery (INV-SIM-01) | EVT-SIM-INJECT-DELIVERED | INJECT_INVALID |
| IN_PROGRESS, PAUSED | CMD-SIM-RECORD-EVALUATION | (بلا تغيير) | participant_ref is one of the linked exercise's participants; competency_code in RD-COMPETENCIES; result ∈ {MET, PARTIAL, NOT_MET}; evaluator ≠ participant (INV-SIM-03) | EVT-SIM-EVALUATION-RECORDED | SEGREGATION_OF_DUTIES |
| IN_PROGRESS | CMD-SIM-PAUSE | PAUSED | reason | EVT-SIM-PAUSED | REASON_REQUIRED |
| PAUSED | CMD-SIM-RESUME | IN_PROGRESS | — | EVT-SIM-RESUMED | — |
| IN_PROGRESS, PAUSED | CMD-SIM-COMPLETE | COMPLETED | every participant on the linked exercise has ≥ 1 recorded evaluation (INV-SIM-02) | EVT-SIM-COMPLETED | EVALUATION_MISSING |
| IN_PROGRESS, PAUSED | CMD-SIM-ABORT | ABORTED | reason | EVT-SIM-ABORTED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-SIM-START | CMD-SIM-DELIVER-INJECT | CMD-SIM-RECORD-EVALUATION | CMD-SIM-PAUSE | CMD-SIM-RESUME | CMD-SIM-COMPLETE | CMD-SIM-ABORT |
|---|---|---|---|---|---|---|---|
| ∅ | → IN_PROGRESS | — | — | — | — | — | — |
| IN_PROGRESS | ✗ SIMULATION_INVALID_STATE_TRANSITION | → IN_PROGRESS | → IN_PROGRESS | → PAUSED | ✗ SIMULATION_INVALID_STATE_TRANSITION | → COMPLETED | → ABORTED |
| PAUSED | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | → PAUSED | ✗ SIMULATION_INVALID_STATE_TRANSITION | → IN_PROGRESS | → COMPLETED | → ABORTED |
| COMPLETED | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION |
| ABORTED | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION | ✗ SIMULATION_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت. `CMD-SIM-START` نفسه يُصدره النظام ضمن نفس معاملة `CMD-EXR-START` (نمط CR-62)، لكنه يبقى أمراً موصوفاً بالكامل في كتالوج SLC-19 (`internal: true`) — لا أثر جانبي غير موثَّق.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-19.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-SIMULATION
bc: BC05
name: Simulation
tier: T2
purpose: 'تنفيذ فعلي واحد لتمرين: تسليم الحقن، تسجيل التقييمات، والانتهاء إلى نتيجة نهائية'
states:
- IN_PROGRESS
- PAUSED
- COMPLETED
- ABORTED
terminal:
- COMPLETED
- ABORTED
invariants:
- 'INV-SIM-01: inject deliveries are append-only and strictly increasing in time (mirrors
  INV-SHP-01''s checkpoint pattern); no edit or delete command exists'
- 'INV-SIM-02: a simulation reaches COMPLETED only when every participant listed on
  its linked exercise has at least one recorded evaluation'
- 'INV-SIM-03: an evaluator never evaluates themself (segregation of duties, mirrors
  CMD-RRQ-ACTIVATE/CMD-KNO-PUBLISH''s reviewer ≠ author pattern)'
entities:
- InjectDelivery (inject_ref, delivered_at, note)
- Evaluation (participant_ref, competency_code, result, evaluator, notes)
requirements:
- REQ-TRX-008
- REQ-TRX-009
- REQ-TRX-010
- REQ-TRX-011
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-SIM-START
  to: IN_PROGRESS
  guard: system-issued in the same unit of work as CMD-EXR-START; exercise_ref SCHEDULED
    transitioning to IN_PROGRESS; scenario_ref = the exercise's frozen scenario; started_at
  event: EVT-SIM-STARTED
  guard_error: SIMULATION_INVALID
- from:
  - IN_PROGRESS
  command: CMD-SIM-DELIVER-INJECT
  to: '='
  guard: inject_ref belongs to the linked scenario; delivered_at strictly after the
    previous delivery (INV-SIM-01)
  event: EVT-SIM-INJECT-DELIVERED
  guard_error: INJECT_INVALID
- from:
  - IN_PROGRESS
  - PAUSED
  command: CMD-SIM-RECORD-EVALUATION
  to: '='
  guard: participant_ref is one of the linked exercise's participants; competency_code
    in RD-COMPETENCIES; result ∈ {MET, PARTIAL, NOT_MET}; evaluator ≠ participant
    (INV-SIM-03)
  event: EVT-SIM-EVALUATION-RECORDED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - IN_PROGRESS
  command: CMD-SIM-PAUSE
  to: PAUSED
  guard: reason
  event: EVT-SIM-PAUSED
  guard_error: REASON_REQUIRED
- from:
  - PAUSED
  command: CMD-SIM-RESUME
  to: IN_PROGRESS
  guard: —
  event: EVT-SIM-RESUMED
  guard_error: null
- from:
  - IN_PROGRESS
  - PAUSED
  command: CMD-SIM-COMPLETE
  to: COMPLETED
  guard: every participant on the linked exercise has ≥ 1 recorded evaluation (INV-SIM-02)
  event: EVT-SIM-COMPLETED
  guard_error: EVALUATION_MISSING
- from:
  - IN_PROGRESS
  - PAUSED
  command: CMD-SIM-ABORT
  to: ABORTED
  guard: reason
  event: EVT-SIM-ABORTED
  guard_error: REASON_REQUIRED
```

</details>
