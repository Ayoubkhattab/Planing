---
id: AGG-SCENARIO
type: aggregate
title: Scenario
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
  - REQ-TRX-001
  - REQ-TRX-002
  state_machine: SM-SCENARIO
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SCENARIO — Scenario

**الغرض:** تعريف قابل لإعادة الاستخدام لتمرين تدريبي: موقف، أهداف، كفاءات مستهدفة، وحقن مرتبة زمنياً  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-SCN-01** — injects are ordered by strictly increasing offset from exercise start; no simultaneous or decreasing offsets
- **INV-SCN-02** — target competencies reference RD-COMPETENCIES codes; no invented closed catalog

## مكونات داخلية

- Inject (offset_minutes, description, expected_response)

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-SCN-DEFINE | DRAFT | title; exercise_type_ref in RD-EXERCISE-TYPES; situation; target_competencies ⊆ RD-COMPETENCIES; injects ordered by strictly increasing offset (INV-SCN-01) | EVT-SCN-DEFINED | SCENARIO_INVALID |
| DRAFT, ACTIVE | CMD-SCN-EDIT | (بلا تغيير) | same validations as DEFINE; editing an ACTIVE scenario creates a new version — exercises already planned against the prior version keep their frozen reference (INV-EXR-01) | EVT-SCN-EDITED | SCENARIO_INVALID |
| DRAFT | CMD-SCN-ACTIVATE | ACTIVE | approver ≠ author | EVT-SCN-ACTIVATED | SEGREGATION_OF_DUTIES |
| ACTIVE | CMD-SCN-RETIRE | RETIRED | reason | EVT-SCN-RETIRED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-SCN-DEFINE | CMD-SCN-EDIT | CMD-SCN-ACTIVATE | CMD-SCN-RETIRE |
|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — |
| DRAFT | ✗ SCENARIO_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ SCENARIO_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ SCENARIO_INVALID_STATE_TRANSITION | → ACTIVE | ✗ SCENARIO_INVALID_STATE_TRANSITION | → RETIRED |
| RETIRED | ✗ SCENARIO_INVALID_STATE_TRANSITION | ✗ SCENARIO_INVALID_STATE_TRANSITION | ✗ SCENARIO_INVALID_STATE_TRANSITION | ✗ SCENARIO_INVALID_STATE_TRANSITION |

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
id: AGG-SCENARIO
bc: BC05
name: Scenario
tier: T2
purpose: تعريف قابل لإعادة الاستخدام لتمرين تدريبي: موقف، أهداف، كفاءات مستهدفة، وحقن مرتبة زمنياً
states:
- DRAFT
- ACTIVE
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-SCN-01: injects are ordered by strictly increasing offset from exercise start;
  no simultaneous or decreasing offsets'
- 'INV-SCN-02: target competencies reference RD-COMPETENCIES codes; no invented closed
  catalog'
entities:
- Inject (offset_minutes, description, expected_response)
requirements:
- REQ-TRX-001
- REQ-TRX-002
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-SCN-DEFINE
  to: DRAFT
  guard: title; exercise_type_ref in RD-EXERCISE-TYPES; situation; target_competencies
    ⊆ RD-COMPETENCIES; injects ordered by strictly increasing offset (INV-SCN-01)
  event: EVT-SCN-DEFINED
  guard_error: SCENARIO_INVALID
- from:
  - DRAFT
  - ACTIVE
  command: CMD-SCN-EDIT
  to: '='
  guard: same validations as DEFINE; editing an ACTIVE scenario creates a new version
    — exercises already planned against the prior version keep their frozen reference
    (INV-EXR-01)
  event: EVT-SCN-EDITED
  guard_error: SCENARIO_INVALID
- from:
  - DRAFT
  command: CMD-SCN-ACTIVATE
  to: ACTIVE
  guard: approver ≠ author
  event: EVT-SCN-ACTIVATED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - ACTIVE
  command: CMD-SCN-RETIRE
  to: RETIRED
  guard: reason
  event: EVT-SCN-RETIRED
  guard_error: REASON_REQUIRED
```

</details>
