---
id: AGG-ANALYSIS-CASE
type: aggregate
title: Analysis Case
wave: W4
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC03
importance_tier: T2 lifecycle; T1 selections
personal_data: false
traces:
  satisfies:
  - REQ-ANL-001
  - REQ-ANL-007
  state_machine: SM-ANALYSIS-CASE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ANALYSIS-CASE — Analysis Case

**الغرض:** سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً  
**السياق:** BC03 · **المستوى:** T2 lifecycle; T1 selections · **بيانات شخصية:** لا

> Closing CR-29 for AnalysisCase: PRJ§58 listed 12 components in one aggregate; here the case holds only definition-level parts.

## الثوابت (Invariants)

- **INV-ACS-01** — every evidence selection is pinned with known_at so its content is reproducible (TEMPORAL-MODEL §4)
- **INV-ACS-02** — case label ≥ max label of its selected items (no lower-labelled case exposing higher-labelled selections)
- **INV-ACS-03** — runs, findings and assessments are separate aggregates (CR-29: no God aggregate)
- **INV-ACS-04** — selections and assumptions are never deleted; deselection/retirement closes them with reason

## مكونات داخلية

- Question (VO)
- Scope (VO)
- Hypothesis
- Assumption
- EvidenceSelection (item_urn, known_at, selected_by, closed_at)
- Scenario

## الحالات

- غير نهائية: DRAFT, OPEN, CLOSED
- نهائية: CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ACS-CREATE | DRAFT | title; owner; label | EVT-ACS-CREATED | CASE_INVALID |
| DRAFT, OPEN | CMD-ACS-DEFINE | (بلا تغيير) | question text; spatial extent (optional polygon); time window; new version | EVT-ACS-DEFINED | CASE_INVALID |
| DRAFT | CMD-ACS-OPEN | OPEN | question and scope present (REQ-ANL-001) | EVT-ACS-OPENED | CASE_NOT_DEFINED |
| OPEN | CMD-ACS-ADD-HYPOTHESIS | (بلا تغيير) | statement; hypotheses per case ≤ 20 | EVT-ACS-HYPOTHESIS-ADDED | CASE_INVALID |
| OPEN | CMD-ACS-UPDATE-HYPOTHESIS | (بلا تغيير) | status ∈ {PROPOSED, SUPPORTED, WEAKENED, REJECTED, UNRESOLVED}; rationale; supporting findings refs | EVT-ACS-HYPOTHESIS-UPDATED | REASON_REQUIRED |
| OPEN | CMD-ACS-ADD-ASSUMPTION | (بلا تغيير) | statement; criticality (high/medium/low) | EVT-ACS-ASSUMPTION-ADDED | CASE_INVALID |
| OPEN | CMD-ACS-RETIRE-ASSUMPTION | (بلا تغيير) | reason; runs using it are flagged | EVT-ACS-ASSUMPTION-RETIRED | REASON_REQUIRED |
| OPEN | CMD-ACS-SELECT-EVIDENCE | (بلا تغيير) | items visible to actor; each pinned with known_at = now; item label ≤ case label | EVT-ACS-EVIDENCE-SELECTED | EVIDENCE_ABOVE_CASE_LABEL |
| OPEN | CMD-ACS-DESELECT-EVIDENCE | (بلا تغيير) | reason; selection record closed, not deleted | EVT-ACS-EVIDENCE-DESELECTED | REASON_REQUIRED |
| OPEN | CMD-ACS-DEFINE-SCENARIO | (بلا تغيير) | name; assumption set; parameter overrides (REQ-ANL-007) | EVT-ACS-SCENARIO-DEFINED | CASE_INVALID |
| OPEN | CMD-ACS-CLOSE | CLOSED | reason; no QUEUED or RUNNING runs | EVT-ACS-CLOSED | RUNS_IN_PROGRESS |
| CLOSED | CMD-ACS-REOPEN | OPEN | reason | EVT-ACS-REOPENED | REASON_REQUIRED |
| DRAFT, OPEN | CMD-ACS-CANCEL | CANCELLED | reason; no PUBLISHED assessment references the case | EVT-ACS-CANCELLED | CASE_HAS_PUBLISHED_ASSESSMENT |
| DRAFT, OPEN, CLOSED | CMD-ACS-RECLASSIFY | (بلا تغيير) | new label ≥ max label of selected evidence; authority per policy | EVT-ACS-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ACS-CREATE | CMD-ACS-DEFINE | CMD-ACS-OPEN | CMD-ACS-ADD-HYPOTHESIS | CMD-ACS-UPDATE-HYPOTHESIS | CMD-ACS-ADD-ASSUMPTION | CMD-ACS-RETIRE-ASSUMPTION | CMD-ACS-SELECT-EVIDENCE | CMD-ACS-DESELECT-EVIDENCE | CMD-ACS-DEFINE-SCENARIO | CMD-ACS-CLOSE | CMD-ACS-REOPEN | CMD-ACS-CANCEL | CMD-ACS-RECLASSIFY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — | — | — | — | — | — | — | — |
| DRAFT | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | → DRAFT | → OPEN | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | → CANCELLED | → DRAFT |
| OPEN | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | → OPEN | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | → OPEN | → OPEN | → OPEN | → OPEN | → OPEN | → OPEN | → OPEN | → CLOSED | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | → CANCELLED | → OPEN |
| CLOSED | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | → OPEN | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | → CLOSED |
| CANCELLED | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION | ✗ ANALYSIS_CASE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-07.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-ANALYSIS-CASE
bc: BC03
name: Analysis Case
tier: T2 lifecycle; T1 selections
purpose: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً
states:
- DRAFT
- OPEN
- CLOSED
- CANCELLED
terminal:
- CANCELLED
invariants:
- 'INV-ACS-01: every evidence selection is pinned with known_at so its content is
  reproducible (TEMPORAL-MODEL §4)'
- 'INV-ACS-02: case label ≥ max label of its selected items (no lower-labelled case
  exposing higher-labelled selections)'
- 'INV-ACS-03: runs, findings and assessments are separate aggregates (CR-29: no God
  aggregate)'
- 'INV-ACS-04: selections and assumptions are never deleted; deselection/retirement
  closes them with reason'
entities:
- Question (VO)
- Scope (VO)
- Hypothesis
- Assumption
- EvidenceSelection (item_urn, known_at, selected_by, closed_at)
- Scenario
requirements:
- REQ-ANL-001
- REQ-ANL-007
notes: 'Closing CR-29 for AnalysisCase: PRJ§58 listed 12 components in one aggregate;
  here the case holds only definition-level parts.'
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-ACS-CREATE
  to: DRAFT
  guard: title; owner; label
  event: EVT-ACS-CREATED
  guard_error: CASE_INVALID
- from:
  - DRAFT
  - OPEN
  command: CMD-ACS-DEFINE
  to: '='
  guard: question text; spatial extent (optional polygon); time window; new version
  event: EVT-ACS-DEFINED
  guard_error: CASE_INVALID
- from:
  - DRAFT
  command: CMD-ACS-OPEN
  to: OPEN
  guard: question and scope present (REQ-ANL-001)
  event: EVT-ACS-OPENED
  guard_error: CASE_NOT_DEFINED
- from:
  - OPEN
  command: CMD-ACS-ADD-HYPOTHESIS
  to: '='
  guard: statement; hypotheses per case ≤ 20
  event: EVT-ACS-HYPOTHESIS-ADDED
  guard_error: CASE_INVALID
- from:
  - OPEN
  command: CMD-ACS-UPDATE-HYPOTHESIS
  to: '='
  guard: status ∈ {PROPOSED, SUPPORTED, WEAKENED, REJECTED, UNRESOLVED}; rationale;
    supporting findings refs
  event: EVT-ACS-HYPOTHESIS-UPDATED
  guard_error: REASON_REQUIRED
- from:
  - OPEN
  command: CMD-ACS-ADD-ASSUMPTION
  to: '='
  guard: statement; criticality (high/medium/low)
  event: EVT-ACS-ASSUMPTION-ADDED
  guard_error: CASE_INVALID
- from:
  - OPEN
  command: CMD-ACS-RETIRE-ASSUMPTION
  to: '='
  guard: reason; runs using it are flagged
  event: EVT-ACS-ASSUMPTION-RETIRED
  guard_error: REASON_REQUIRED
- from:
  - OPEN
  command: CMD-ACS-SELECT-EVIDENCE
  to: '='
  guard: items visible to actor; each pinned with known_at = now; item label ≤ case
    label
  event: EVT-ACS-EVIDENCE-SELECTED
  guard_error: EVIDENCE_ABOVE_CASE_LABEL
- from:
  - OPEN
  command: CMD-ACS-DESELECT-EVIDENCE
  to: '='
  guard: reason; selection record closed, not deleted
  event: EVT-ACS-EVIDENCE-DESELECTED
  guard_error: REASON_REQUIRED
- from:
  - OPEN
  command: CMD-ACS-DEFINE-SCENARIO
  to: '='
  guard: name; assumption set; parameter overrides (REQ-ANL-007)
  event: EVT-ACS-SCENARIO-DEFINED
  guard_error: CASE_INVALID
- from:
  - OPEN
  command: CMD-ACS-CLOSE
  to: CLOSED
  guard: reason; no QUEUED or RUNNING runs
  event: EVT-ACS-CLOSED
  guard_error: RUNS_IN_PROGRESS
- from:
  - CLOSED
  command: CMD-ACS-REOPEN
  to: OPEN
  guard: reason
  event: EVT-ACS-REOPENED
  guard_error: REASON_REQUIRED
- from:
  - DRAFT
  - OPEN
  command: CMD-ACS-CANCEL
  to: CANCELLED
  guard: reason; no PUBLISHED assessment references the case
  event: EVT-ACS-CANCELLED
  guard_error: CASE_HAS_PUBLISHED_ASSESSMENT
- from:
  - DRAFT
  - OPEN
  - CLOSED
  command: CMD-ACS-RECLASSIFY
  to: '='
  guard: new label ≥ max label of selected evidence; authority per policy
  event: EVT-ACS-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
```

</details>
