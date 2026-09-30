---
id: AGG-MODEL-VERSION
type: aggregate
title: Model Version
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
  - REQ-AI-009
  - REQ-AI-010
  state_machine: SM-MODEL-VERSION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-MODEL-VERSION — Model Version

**الغرض:** نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)  
**السياق:** BC07 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-MDL-01** — only PRODUCTION versions serve production routes; STAGED serves canary share only
- **INV-MDL-02** — approval needs an evaluation report meeting thresholds; approver ≠ registrar (REQ-AI-010)
- **INV-MDL-03** — model records are never deleted; lineage always resolves the model version

## مكونات داخلية

- EvaluationReport
- CanaryMetrics

## الحالات

- غير نهائية: REGISTERED, EVALUATING, APPROVED, STAGED, PRODUCTION, DEPRECATED
- نهائية: EVALUATION_FAILED, RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-MDL-REGISTER | REGISTERED | family, version, weights digest in internal registry, licence reviewed, languages (must include ar and en for generative roles), context size, hosting ∈ {local, external_allowed} | EVT-MDL-REGISTERED | MODEL_INVALID |
| REGISTERED | CMD-MDL-START-EVALUATION | EVALUATING | evaluation suite ACTIVE (AGG-EVAL-SUITE) | EVT-MDL-EVALUATION-STARTED | SUITE_NOT_ACTIVE |
| EVALUATING | CMD-MDL-APPROVE | APPROVED | report meets thresholds: citation accuracy ≥ 95 %, hallucination ≤ 2 %, insufficient-evidence recall ≥ 95 %, 0 injection/exfiltration successes, latency and cost recorded (REQ-AI-010); AI governance authority ≠ registrar | EVT-MDL-APPROVED | EVALUATION_BELOW_THRESHOLD |
| EVALUATING | CMD-MDL-FAIL-EVALUATION | EVALUATION_FAILED | report attached | EVT-MDL-EVALUATION-FAILED | — |
| APPROVED | CMD-MDL-STAGE | STAGED | canary share ≤ 10 % of the target operations | EVT-MDL-STAGED | — |
| STAGED | CMD-MDL-PROMOTE | PRODUCTION | canary metrics within thresholds for ≥ 7 days; approver ≠ stager | EVT-MDL-PROMOTED | CANARY_BELOW_THRESHOLD |
| PRODUCTION | SYS:monitoring drift detected | (بلا تغيير) | weekly evaluation sample below threshold → alert, route review | EVT-MDL-DRIFT-DETECTED | — |
| PRODUCTION, STAGED, APPROVED | CMD-MDL-DEPRECATE | DEPRECATED | reason; routes using it must be switched first | EVT-MDL-DEPRECATED | MODEL_IN_ACTIVE_ROUTE |
| DEPRECATED | CMD-MDL-REINSTATE | PRODUCTION | rollback; evaluation ≤ 90 days old | EVT-MDL-REINSTATED | EVALUATION_TOO_OLD |
| DEPRECATED | CMD-MDL-RETIRE | RETIRED | weights archived (cold) if referenced by lineage of accepted results; record kept | EVT-MDL-RETIRED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-MDL-REGISTER | CMD-MDL-START-EVALUATION | CMD-MDL-APPROVE | CMD-MDL-FAIL-EVALUATION | CMD-MDL-STAGE | CMD-MDL-PROMOTE | SYS:monitoring drift detected | CMD-MDL-DEPRECATE | CMD-MDL-REINSTATE | CMD-MDL-RETIRE |
|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → REGISTERED | — | — | — | — | — | — | — | — | — |
| REGISTERED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | → EVALUATING | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION |
| EVALUATING | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | → APPROVED | → EVALUATION_FAILED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION |
| EVALUATION_FAILED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION |
| APPROVED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | → STAGED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | → DEPRECATED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION |
| STAGED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | → PRODUCTION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | → DEPRECATED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION |
| PRODUCTION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | → PRODUCTION | → DEPRECATED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION |
| DEPRECATED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | → PRODUCTION | → RETIRED |
| RETIRED | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION | ✗ MODEL_VERSION_INVALID_STATE_TRANSITION |

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
id: AGG-MODEL-VERSION
bc: BC07
name: Model Version
tier: T2
purpose: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)
states:
- REGISTERED
- EVALUATING
- EVALUATION_FAILED
- APPROVED
- STAGED
- PRODUCTION
- DEPRECATED
- RETIRED
terminal:
- EVALUATION_FAILED
- RETIRED
invariants:
- 'INV-MDL-01: only PRODUCTION versions serve production routes; STAGED serves canary
  share only'
- 'INV-MDL-02: approval needs an evaluation report meeting thresholds; approver ≠
  registrar (REQ-AI-010)'
- 'INV-MDL-03: model records are never deleted; lineage always resolves the model
  version'
entities:
- EvaluationReport
- CanaryMetrics
requirements:
- REQ-AI-009
- REQ-AI-010
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-MDL-REGISTER
  to: REGISTERED
  guard: family, version, weights digest in internal registry, licence reviewed, languages
    (must include ar and en for generative roles), context size, hosting ∈ {local,
    external_allowed}
  event: EVT-MDL-REGISTERED
  guard_error: MODEL_INVALID
- from:
  - REGISTERED
  command: CMD-MDL-START-EVALUATION
  to: EVALUATING
  guard: evaluation suite ACTIVE (AGG-EVAL-SUITE)
  event: EVT-MDL-EVALUATION-STARTED
  guard_error: SUITE_NOT_ACTIVE
- from:
  - EVALUATING
  command: CMD-MDL-APPROVE
  to: APPROVED
  guard: 'report meets thresholds: citation accuracy ≥ 95 %, hallucination ≤ 2 %,
    insufficient-evidence recall ≥ 95 %, 0 injection/exfiltration successes, latency
    and cost recorded (REQ-AI-010); AI governance authority ≠ registrar'
  event: EVT-MDL-APPROVED
  guard_error: EVALUATION_BELOW_THRESHOLD
- from:
  - EVALUATING
  command: CMD-MDL-FAIL-EVALUATION
  to: EVALUATION_FAILED
  guard: report attached
  event: EVT-MDL-EVALUATION-FAILED
  guard_error: null
- from:
  - APPROVED
  command: CMD-MDL-STAGE
  to: STAGED
  guard: canary share ≤ 10 % of the target operations
  event: EVT-MDL-STAGED
  guard_error: null
- from:
  - STAGED
  command: CMD-MDL-PROMOTE
  to: PRODUCTION
  guard: canary metrics within thresholds for ≥ 7 days; approver ≠ stager
  event: EVT-MDL-PROMOTED
  guard_error: CANARY_BELOW_THRESHOLD
- from:
  - PRODUCTION
  command: SYS:monitoring drift detected
  to: '='
  guard: weekly evaluation sample below threshold → alert, route review
  event: EVT-MDL-DRIFT-DETECTED
  guard_error: null
- from:
  - PRODUCTION
  - STAGED
  - APPROVED
  command: CMD-MDL-DEPRECATE
  to: DEPRECATED
  guard: reason; routes using it must be switched first
  event: EVT-MDL-DEPRECATED
  guard_error: MODEL_IN_ACTIVE_ROUTE
- from:
  - DEPRECATED
  command: CMD-MDL-REINSTATE
  to: PRODUCTION
  guard: rollback; evaluation ≤ 90 days old
  event: EVT-MDL-REINSTATED
  guard_error: EVALUATION_TOO_OLD
- from:
  - DEPRECATED
  command: CMD-MDL-RETIRE
  to: RETIRED
  guard: weights archived (cold) if referenced by lineage of accepted results; record
    kept
  event: EVT-MDL-RETIRED
  guard_error: null
```

</details>
