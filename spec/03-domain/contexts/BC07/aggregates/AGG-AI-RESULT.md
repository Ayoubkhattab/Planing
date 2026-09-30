---
id: AGG-AI-RESULT
type: aggregate
title: AI Result (reviewable)
wave: W4
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC07
importance_tier: T1
personal_data: false
traces:
  satisfies:
  - REQ-AI-005
  - REQ-AI-006
  - REQ-AI-008
  state_machine: SM-AI-RESULT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-AI-RESULT — AI Result (reviewable)

**الغرض:** مخرج AI يحتاج مراجعة بشرية قبل أن يؤثر: مسودة، استخراج، ترجمة كدليل، اقتراح مطابقة  
**السياق:** BC07 · **المستوى:** T1 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-AIRS-01** — no AI result changes business state without an accepting human (AIL ≤ 3 in R2; REQ-AI-005/006/008)
- **INV-AIRS-02** — accepted effects keep lineage to request, context package and model version
- **INV-AIRS-03** — review outcomes are fed to the evaluation data set (human feedback)

## مكونات داخلية

- ResultItem (kind, payload, citations, decision)

## الحالات

- غير نهائية: PROPOSED, UNDER_REVIEW
- نهائية: ACCEPTED, PARTIALLY_ACCEPTED, REJECTED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:request COMPLETED for a reviewable operation | PROPOSED | operation ∈ {AI-OP-03 draft, AI-OP-04 extract, AI-OP-05 translation used as evidence, AI-OP-06 match suggestion} | EVT-AIRS-PROPOSED | — |
| PROPOSED | CMD-AIRS-START-REVIEW | UNDER_REVIEW | reviewer authorized for the target and cleared for the result label | EVT-AIRS-REVIEW-STARTED | REVIEWER_NOT_CLEARED |
| UNDER_REVIEW | CMD-AIRS-ACCEPT | ACCEPTED | effects applied through owner commands as the reviewer, with agent = model version in lineage (e.g. CMD-CLM-ASSERT, product section, CMD-ER-PROPOSE) | EVT-AIRS-ACCEPTED | OWNER_REJECTED |
| UNDER_REVIEW | CMD-AIRS-ACCEPT-PARTIALLY | PARTIALLY_ACCEPTED | selected items only; rejected items recorded with reasons | EVT-AIRS-PARTIALLY-ACCEPTED | OWNER_REJECTED |
| PROPOSED, UNDER_REVIEW | CMD-AIRS-REJECT | REJECTED | reason (feeds evaluation) | EVT-AIRS-REJECTED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:request COMPLETED for a reviewable operation | CMD-AIRS-START-REVIEW | CMD-AIRS-ACCEPT | CMD-AIRS-ACCEPT-PARTIALLY | CMD-AIRS-REJECT |
|---|---|---|---|---|---|
| ∅ | → PROPOSED | — | — | — | — |
| PROPOSED | ✗ AI_RESULT_INVALID_STATE_TRANSITION | → UNDER_REVIEW | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | → REJECTED |
| UNDER_REVIEW | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | → ACCEPTED | → PARTIALLY_ACCEPTED | → REJECTED |
| ACCEPTED | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION |
| PARTIALLY_ACCEPTED | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION |
| REJECTED | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION | ✗ AI_RESULT_INVALID_STATE_TRANSITION |

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
id: AGG-AI-RESULT
bc: BC07
name: AI Result (reviewable)
tier: T1
purpose: 'مخرج AI يحتاج مراجعة بشرية قبل أن يؤثر: مسودة، استخراج، ترجمة كدليل، اقتراح
  مطابقة'
states:
- PROPOSED
- UNDER_REVIEW
- ACCEPTED
- PARTIALLY_ACCEPTED
- REJECTED
terminal:
- ACCEPTED
- PARTIALLY_ACCEPTED
- REJECTED
invariants:
- 'INV-AIRS-01: no AI result changes business state without an accepting human (AIL
  ≤ 3 in R2; REQ-AI-005/006/008)'
- 'INV-AIRS-02: accepted effects keep lineage to request, context package and model
  version'
- 'INV-AIRS-03: review outcomes are fed to the evaluation data set (human feedback)'
entities:
- ResultItem (kind, payload, citations, decision)
requirements:
- REQ-AI-005
- REQ-AI-006
- REQ-AI-008
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: SYS:request COMPLETED for a reviewable operation
  to: PROPOSED
  guard: operation ∈ {AI-OP-03 draft, AI-OP-04 extract, AI-OP-05 translation used
    as evidence, AI-OP-06 match suggestion}
  event: EVT-AIRS-PROPOSED
  guard_error: null
- from:
  - PROPOSED
  command: CMD-AIRS-START-REVIEW
  to: UNDER_REVIEW
  guard: reviewer authorized for the target and cleared for the result label
  event: EVT-AIRS-REVIEW-STARTED
  guard_error: REVIEWER_NOT_CLEARED
- from:
  - UNDER_REVIEW
  command: CMD-AIRS-ACCEPT
  to: ACCEPTED
  guard: effects applied through owner commands as the reviewer, with agent = model
    version in lineage (e.g. CMD-CLM-ASSERT, product section, CMD-ER-PROPOSE)
  event: EVT-AIRS-ACCEPTED
  guard_error: OWNER_REJECTED
- from:
  - UNDER_REVIEW
  command: CMD-AIRS-ACCEPT-PARTIALLY
  to: PARTIALLY_ACCEPTED
  guard: selected items only; rejected items recorded with reasons
  event: EVT-AIRS-PARTIALLY-ACCEPTED
  guard_error: OWNER_REJECTED
- from:
  - PROPOSED
  - UNDER_REVIEW
  command: CMD-AIRS-REJECT
  to: REJECTED
  guard: reason (feeds evaluation)
  event: EVT-AIRS-REJECTED
  guard_error: REASON_REQUIRED
```

</details>
