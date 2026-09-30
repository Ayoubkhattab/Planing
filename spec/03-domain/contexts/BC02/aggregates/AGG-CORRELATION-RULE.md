---
id: AGG-CORRELATION-RULE
type: aggregate
title: Correlation Rule
wave: W4
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-FUS-001
  state_machine: SM-CORRELATION-RULE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-CORRELATION-RULE — Correlation Rule

**الغرض:** قاعدة ربط زماني-مكاني بمعاملات وعتبة وتقييم  
**السياق:** BC02 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-CRR-01** — proposals record the rule version
- **INV-CRR-02** — activation requires an evaluation report

## مكونات داخلية

- Parameters
- EvaluationReport

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-CRR-DEFINE | DRAFT | kind ∈ {same_event, co_location, track_association, same_entity_hint} | EVT-CRR-DEFINED | RULE_INVALID |
| DRAFT, ACTIVE | CMD-CRR-EDIT | (بلا تغيير) | parameters: max distance (m, accuracy-aware), time window, attribute similarity, min distinct sources, threshold; ACTIVE → new version | EVT-CRR-EDITED | RULE_INVALID |
| DRAFT | CMD-CRR-ACTIVATE | ACTIVE | evaluation on a labelled set: precision ≥ 70 % of proposals (recalibrate after pilot); approver ≠ author | EVT-CRR-ACTIVATED | RULE_BELOW_TARGET |
| ACTIVE | CMD-CRR-RETIRE | RETIRED | reason | EVT-CRR-RETIRED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-CRR-DEFINE | CMD-CRR-EDIT | CMD-CRR-ACTIVATE | CMD-CRR-RETIRE |
|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — |
| DRAFT | ✗ CORRELATION_RULE_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ CORRELATION_RULE_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ CORRELATION_RULE_INVALID_STATE_TRANSITION | → ACTIVE | ✗ CORRELATION_RULE_INVALID_STATE_TRANSITION | → RETIRED |
| RETIRED | ✗ CORRELATION_RULE_INVALID_STATE_TRANSITION | ✗ CORRELATION_RULE_INVALID_STATE_TRANSITION | ✗ CORRELATION_RULE_INVALID_STATE_TRANSITION | ✗ CORRELATION_RULE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-15.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-CORRELATION-RULE
bc: BC02
name: Correlation Rule
tier: T2
purpose: قاعدة ربط زماني-مكاني بمعاملات وعتبة وتقييم
states:
- DRAFT
- ACTIVE
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-CRR-01: proposals record the rule version'
- 'INV-CRR-02: activation requires an evaluation report'
entities:
- Parameters
- EvaluationReport
requirements:
- REQ-FUS-001
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-CRR-DEFINE
  to: DRAFT
  guard: kind ∈ {same_event, co_location, track_association, same_entity_hint}
  event: EVT-CRR-DEFINED
  guard_error: RULE_INVALID
- from:
  - DRAFT
  - ACTIVE
  command: CMD-CRR-EDIT
  to: '='
  guard: 'parameters: max distance (m, accuracy-aware), time window, attribute similarity,
    min distinct sources, threshold; ACTIVE → new version'
  event: EVT-CRR-EDITED
  guard_error: RULE_INVALID
- from:
  - DRAFT
  command: CMD-CRR-ACTIVATE
  to: ACTIVE
  guard: 'evaluation on a labelled set: precision ≥ 70 % of proposals (recalibrate
    after pilot); approver ≠ author'
  event: EVT-CRR-ACTIVATED
  guard_error: RULE_BELOW_TARGET
- from:
  - ACTIVE
  command: CMD-CRR-RETIRE
  to: RETIRED
  guard: reason
  event: EVT-CRR-RETIRED
  guard_error: REASON_REQUIRED
```

</details>
