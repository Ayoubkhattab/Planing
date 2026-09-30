---
id: AGG-CLAIM
type: aggregate
title: Claim
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T1
personal_data: false
traces:
  satisfies:
  - REQ-INF-021
  - REQ-INF-022
  - REQ-INF-024
  - REQ-INF-026
  - REQ-INF-037
  state_machine: SM-CLAIM
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-CLAIM — Claim

**الغرض:** عبارة (موضوع، سمة، قيمة) مؤرخة ثنائياً ومسندة؛ قيمتها لا تتغير  
**السياق:** BC02 · **المستوى:** T1 · **بيانات شخصية:** لا

> CLOSED is terminal for content; re-labelling a CLOSED claim is allowed so history can be reclassified.

## الثوابت (Invariants)

- **INV-CLM-01** — subject, predicate, value, valid interval and sources are immutable
- **INV-CLM-02** — recorded_from/recorded_to are server-assigned; CLOSED ⇔ recorded_to ≠ null
- **INV-CLM-03** — ≥ 1 source; each cited source was ACTIVE at assertion
- **INV-CLM-04** — successors reference their predecessor (supersedes chain)
- **INV-CLM-05** — source identity protection never leaks through the claim

## مكونات داخلية

- Value (typed)
- ConfidenceAssessment (T2 versioned)

## الحالات

- غير نهائية: CURRENT
- نهائية: CLOSED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-CLM-ASSERT | CURRENT | subject exists; predicate in RD-PREDICATES; value matches predicate type/unit/cardinality; ≥ 1 source, all ACTIVE; valid_from < valid_to; geometry rules; confidence dims valid | EVT-CLM-ASSERTED | CLAIM_INVALID |
| CURRENT | CMD-CLM-CORRECT | CLOSED | closes recorded_to = now and asserts the replacement (same subject/predicate) in the same transaction; reason | EVT-CLM-CORRECTED | REASON_REQUIRED |
| CURRENT | CMD-CLM-RECORD-CHANGE | CLOSED | t_change ∈ (valid_from, valid_to): closes record, re-records old value with valid_to = t_change, asserts new value from t_change | EVT-CLM-CHANGED | CHANGE_TIME_INVALID |
| CURRENT | CMD-CLM-RETRACT | CLOSED | reason; no replacement | EVT-CLM-RETRACTED | REASON_REQUIRED |
| CURRENT | CMD-CLM-ASSESS | (بلا تغيير) | updates information_confidence / verification_status only (T2 versioned assessment); value and times untouched | EVT-CLM-ASSESSED | ASSESSMENT_INVALID |
| CURRENT, CLOSED | CMD-CLM-RECLASSIFY | (بلا تغيير) | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | EVT-CLM-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-CLM-ASSERT | CMD-CLM-CORRECT | CMD-CLM-RECORD-CHANGE | CMD-CLM-RETRACT | CMD-CLM-ASSESS | CMD-CLM-RECLASSIFY |
|---|---|---|---|---|---|---|
| ∅ | → CURRENT | — | — | — | — | — |
| CURRENT | ✗ CLAIM_INVALID_STATE_TRANSITION | → CLOSED | → CLOSED | → CLOSED | → CURRENT | → CURRENT |
| CLOSED | ✗ CLAIM_INVALID_STATE_TRANSITION | ✗ CLAIM_INVALID_STATE_TRANSITION | ✗ CLAIM_INVALID_STATE_TRANSITION | ✗ CLAIM_INVALID_STATE_TRANSITION | ✗ CLAIM_INVALID_STATE_TRANSITION | → CLOSED |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-02.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-CLAIM
bc: BC02
name: Claim
tier: T1
purpose: عبارة (موضوع، سمة، قيمة) مؤرخة ثنائياً ومسندة؛ قيمتها لا تتغير
states:
- CURRENT
- CLOSED
terminal:
- CLOSED
invariants:
- 'INV-CLM-01: subject, predicate, value, valid interval and sources are immutable'
- 'INV-CLM-02: recorded_from/recorded_to are server-assigned; CLOSED ⇔ recorded_to
  ≠ null'
- 'INV-CLM-03: ≥ 1 source; each cited source was ACTIVE at assertion'
- 'INV-CLM-04: successors reference their predecessor (supersedes chain)'
- 'INV-CLM-05: source identity protection never leaks through the claim'
entities:
- Value (typed)
- ConfidenceAssessment (T2 versioned)
requirements:
- REQ-INF-021
- REQ-INF-022
- REQ-INF-024
- REQ-INF-026
- REQ-INF-037
notes: CLOSED is terminal for content; re-labelling a CLOSED claim is allowed so history
  can be reclassified.
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-CLM-ASSERT
  to: CURRENT
  guard: subject exists; predicate in RD-PREDICATES; value matches predicate type/unit/cardinality;
    ≥ 1 source, all ACTIVE; valid_from < valid_to; geometry rules; confidence dims
    valid
  event: EVT-CLM-ASSERTED
  guard_error: CLAIM_INVALID
- from:
  - CURRENT
  command: CMD-CLM-CORRECT
  to: CLOSED
  guard: closes recorded_to = now and asserts the replacement (same subject/predicate)
    in the same transaction; reason
  event: EVT-CLM-CORRECTED
  guard_error: REASON_REQUIRED
- from:
  - CURRENT
  command: CMD-CLM-RECORD-CHANGE
  to: CLOSED
  guard: 't_change ∈ (valid_from, valid_to): closes record, re-records old value with
    valid_to = t_change, asserts new value from t_change'
  event: EVT-CLM-CHANGED
  guard_error: CHANGE_TIME_INVALID
- from:
  - CURRENT
  command: CMD-CLM-RETRACT
  to: CLOSED
  guard: reason; no replacement
  event: EVT-CLM-RETRACTED
  guard_error: REASON_REQUIRED
- from:
  - CURRENT
  command: CMD-CLM-ASSESS
  to: '='
  guard: updates information_confidence / verification_status only (T2 versioned assessment);
    value and times untouched
  event: EVT-CLM-ASSESSED
  guard_error: ASSESSMENT_INVALID
- from:
  - CURRENT
  - CLOSED
  command: CMD-CLM-RECLASSIFY
  to: '='
  guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
  event: EVT-CLM-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
```

</details>
