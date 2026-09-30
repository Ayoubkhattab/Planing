---
id: AGG-EVAL-SUITE
type: aggregate
title: Evaluation Suite
wave: W4
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC07
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-AI-010
  state_machine: SM-EVAL-SUITE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-EVAL-SUITE — Evaluation Suite

**الغرض:** مجموعات تقييم مُصدرة: تأريض، استشهاد، أدلة غير كافية، حقن، تسريب، عربي/إنجليزي  
**السياق:** BC07 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-EVS-01** — suites are immutable once ACTIVE; every evaluation report names its suite version
- **INV-EVS-02** — suites include tenant samples before a model serves that tenant (RSK-021 analogue for AI)

## مكونات داخلية

- EvalItem (set, input, expected, labels)

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: SUPERSEDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-EVS-DRAFT | DRAFT | AI governance | EVT-EVS-DRAFTED | — |
| DRAFT | CMD-EVS-EDIT | (بلا تغيير) | sets: groundedness (≥ 500 items), citation, insufficient-evidence, prompt-injection, exfiltration, cross-tenant, Arabic/English/mixed; each item labelled with expected behaviour | EVT-EVS-EDITED | SUITE_INVALID |
| DRAFT | CMD-EVS-ACTIVATE | ACTIVE | approver ≠ author; previous ACTIVE → SUPERSEDED | EVT-EVS-ACTIVATED | SEGREGATION_OF_DUTIES |
| ACTIVE | SYS:successor activated | SUPERSEDED | system | EVT-EVS-SUPERSEDED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-EVS-DRAFT | CMD-EVS-EDIT | CMD-EVS-ACTIVATE | SYS:successor activated |
|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — |
| DRAFT | ✗ EVAL_SUITE_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ EVAL_SUITE_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ EVAL_SUITE_INVALID_STATE_TRANSITION | ✗ EVAL_SUITE_INVALID_STATE_TRANSITION | ✗ EVAL_SUITE_INVALID_STATE_TRANSITION | → SUPERSEDED |
| SUPERSEDED | ✗ EVAL_SUITE_INVALID_STATE_TRANSITION | ✗ EVAL_SUITE_INVALID_STATE_TRANSITION | ✗ EVAL_SUITE_INVALID_STATE_TRANSITION | ✗ EVAL_SUITE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-10.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-EVAL-SUITE
bc: BC07
name: Evaluation Suite
tier: T2
purpose: 'مجموعات تقييم مُصدرة: تأريض، استشهاد، أدلة غير كافية، حقن، تسريب، عربي/إنجليزي'
states:
- DRAFT
- ACTIVE
- SUPERSEDED
terminal:
- SUPERSEDED
invariants:
- 'INV-EVS-01: suites are immutable once ACTIVE; every evaluation report names its
  suite version'
- 'INV-EVS-02: suites include tenant samples before a model serves that tenant (RSK-021
  analogue for AI)'
entities:
- EvalItem (set, input, expected, labels)
requirements:
- REQ-AI-010
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-EVS-DRAFT
  to: DRAFT
  guard: AI governance
  event: EVT-EVS-DRAFTED
  guard_error: null
- from:
  - DRAFT
  command: CMD-EVS-EDIT
  to: '='
  guard: 'sets: groundedness (≥ 500 items), citation, insufficient-evidence, prompt-injection,
    exfiltration, cross-tenant, Arabic/English/mixed; each item labelled with expected
    behaviour'
  event: EVT-EVS-EDITED
  guard_error: SUITE_INVALID
- from:
  - DRAFT
  command: CMD-EVS-ACTIVATE
  to: ACTIVE
  guard: approver ≠ author; previous ACTIVE → SUPERSEDED
  event: EVT-EVS-ACTIVATED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - ACTIVE
  command: SYS:successor activated
  to: SUPERSEDED
  guard: system
  event: EVT-EVS-SUPERSEDED
  guard_error: null
```

</details>
