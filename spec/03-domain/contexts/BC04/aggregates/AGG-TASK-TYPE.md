---
id: AGG-TASK-TYPE
type: aggregate
title: Task Type
wave: W4
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC04
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-OPS-007
  - REQ-OPS-014
  state_machine: SM-TASK-TYPE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-TASK-TYPE — Task Type

**الغرض:** قالب نوع مهمة: متطلبات الأهلية، معايير الإكمال، التصعيد، الانتهاء  
**السياق:** BC04 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-TTY-01** — tasks pin the task-type version at creation
- **INV-TTY-02** — expires_on_due defaults to false; escalation defaults: at due and due + 24 h
- **INV-TTY-03** — offline-capable commands are limited to ACCEPT, START, BLOCK, RESUME, ADD-RESULT-ITEM, SUBMIT

## مكونات داخلية

- QualificationRequirement (code, min_level, supervision_allowed)
- CriterionTemplate
- EscalationPolicy

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-TTY-DEFINE | DRAFT | code unique in tenant | EVT-TTY-DEFINED | TASK_TYPE_CODE_TAKEN |
| DRAFT, ACTIVE | CMD-TTY-EDIT | (بلا تغيير) | required qualifications exist in RD-COMPETENCIES; criteria templates valid; ACTIVE → new version (existing tasks keep their pinned version) | EVT-TTY-EDITED | TASK_TYPE_INVALID |
| DRAFT | CMD-TTY-ACTIVATE | ACTIVE | ≥ 1 completion criterion template | EVT-TTY-ACTIVATED | TASK_TYPE_INVALID |
| ACTIVE | CMD-TTY-RETIRE | RETIRED | reason; existing tasks unaffected | EVT-TTY-RETIRED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-TTY-DEFINE | CMD-TTY-EDIT | CMD-TTY-ACTIVATE | CMD-TTY-RETIRE |
|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — |
| DRAFT | ✗ TASK_TYPE_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ TASK_TYPE_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ TASK_TYPE_INVALID_STATE_TRANSITION | → ACTIVE | ✗ TASK_TYPE_INVALID_STATE_TRANSITION | → RETIRED |
| RETIRED | ✗ TASK_TYPE_INVALID_STATE_TRANSITION | ✗ TASK_TYPE_INVALID_STATE_TRANSITION | ✗ TASK_TYPE_INVALID_STATE_TRANSITION | ✗ TASK_TYPE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-03.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-TASK-TYPE
bc: BC04
name: Task Type
tier: T2
purpose: 'قالب نوع مهمة: متطلبات الأهلية، معايير الإكمال، التصعيد، الانتهاء'
states:
- DRAFT
- ACTIVE
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-TTY-01: tasks pin the task-type version at creation'
- 'INV-TTY-02: expires_on_due defaults to false; escalation defaults: at due and due
  + 24 h'
- 'INV-TTY-03: offline-capable commands are limited to ACCEPT, START, BLOCK, RESUME,
  ADD-RESULT-ITEM, SUBMIT'
entities:
- QualificationRequirement (code, min_level, supervision_allowed)
- CriterionTemplate
- EscalationPolicy
requirements:
- REQ-OPS-007
- REQ-OPS-014
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-TTY-DEFINE
  to: DRAFT
  guard: code unique in tenant
  event: EVT-TTY-DEFINED
  guard_error: TASK_TYPE_CODE_TAKEN
- from:
  - DRAFT
  - ACTIVE
  command: CMD-TTY-EDIT
  to: '='
  guard: required qualifications exist in RD-COMPETENCIES; criteria templates valid;
    ACTIVE → new version (existing tasks keep their pinned version)
  event: EVT-TTY-EDITED
  guard_error: TASK_TYPE_INVALID
- from:
  - DRAFT
  command: CMD-TTY-ACTIVATE
  to: ACTIVE
  guard: ≥ 1 completion criterion template
  event: EVT-TTY-ACTIVATED
  guard_error: TASK_TYPE_INVALID
- from:
  - ACTIVE
  command: CMD-TTY-RETIRE
  to: RETIRED
  guard: reason; existing tasks unaffected
  event: EVT-TTY-RETIRED
  guard_error: REASON_REQUIRED
```

</details>
