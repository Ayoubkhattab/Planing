---
id: AGG-ASSESSMENT
type: aggregate
title: Assessment Version
wave: W4
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC03
importance_tier: T1 content / T2 lifecycle
personal_data: false
traces:
  satisfies:
  - REQ-ANL-005
  - REQ-ANL-006
  - REQ-ANL-008
  state_machine: SM-ASSESSMENT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ASSESSMENT — Assessment Version

**الغرض:** تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت  
**السياق:** BC03 · **المستوى:** T1 content / T2 lifecycle · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-ASM-01** — a PUBLISHED version is immutable; changes are new versions (REQ-ANL-006)
- **INV-ASM-02** — exactly one PUBLISHED version per assessment at a time; history of versions retained
- **INV-ASM-03** — references from decisions pin the version (URN + version) — superseding never changes what a past decision relied on
- **INV-ASM-04** — readers not cleared for some cited evidence get the assessment with those references withheld per policy (REQ-ANL-008)

## مكونات داخلية

- KeyJudgment (statement, probability term, confidence)
- Citation (finding | evidence, pinned version)

## الحالات

- غير نهائية: DRAFT, IN_REVIEW, PUBLISHED
- نهائية: SUPERSEDED, WITHDRAWN, DISCARDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ASM-DRAFT | DRAFT | case exists; either new assessment or revision of a PUBLISHED version (copies content); at most one DRAFT/IN_REVIEW per assessment | EVT-ASM-DRAFTED | DRAFT_EXISTS |
| DRAFT | CMD-ASM-EDIT | (بلا تغيير) | key judgments use RD-ESTIMATIVE-PROBABILITY terms and analytic confidence (low/moderate/high) | EVT-ASM-EDITED | ASSESSMENT_INVALID |
| DRAFT | CMD-ASM-SUBMIT | IN_REVIEW | findings ≥ 1 (ACCEPTED), evidence, assumptions, uncertainty, confidence, methodology, limitations all present (REQ-ANL-005) | EVT-ASM-SUBMITTED | ASSESSMENT_INCOMPLETE |
| IN_REVIEW | CMD-ASM-RETURN | DRAFT | reviewer; reason | EVT-ASM-RETURNED | REASON_REQUIRED |
| IN_REVIEW | CMD-ASM-PUBLISH | PUBLISHED | reviewer ≠ author; label ≥ max(findings, evidence); previous PUBLISHED version → SUPERSEDED in the same transaction | EVT-ASM-PUBLISHED | SEGREGATION_OF_DUTIES |
| PUBLISHED | SYS:newer version published | SUPERSEDED | system | EVT-ASM-SUPERSEDED | — |
| PUBLISHED | CMD-ASM-WITHDRAW | WITHDRAWN | reason; decisions and products referencing it are notified | EVT-ASM-WITHDRAWN | REASON_REQUIRED |
| DRAFT | CMD-ASM-DISCARD | DISCARDED | author; reason | EVT-ASM-DISCARDED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ASM-DRAFT | CMD-ASM-EDIT | CMD-ASM-SUBMIT | CMD-ASM-RETURN | CMD-ASM-PUBLISH | SYS:newer version published | CMD-ASM-WITHDRAW | CMD-ASM-DISCARD |
|---|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — | — |
| DRAFT | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | → DRAFT | → IN_REVIEW | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | → DISCARDED |
| IN_REVIEW | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | → DRAFT | → PUBLISHED | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION |
| PUBLISHED | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | → SUPERSEDED | → WITHDRAWN | ✗ ASSESSMENT_INVALID_STATE_TRANSITION |
| SUPERSEDED | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION |
| WITHDRAWN | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION |
| DISCARDED | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION | ✗ ASSESSMENT_INVALID_STATE_TRANSITION |

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
id: AGG-ASSESSMENT
bc: BC03
name: Assessment Version
tier: T1 content / T2 lifecycle
purpose: تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت
states:
- DRAFT
- IN_REVIEW
- PUBLISHED
- SUPERSEDED
- WITHDRAWN
- DISCARDED
terminal:
- SUPERSEDED
- WITHDRAWN
- DISCARDED
invariants:
- 'INV-ASM-01: a PUBLISHED version is immutable; changes are new versions (REQ-ANL-006)'
- 'INV-ASM-02: exactly one PUBLISHED version per assessment at a time; history of
  versions retained'
- 'INV-ASM-03: references from decisions pin the version (URN + version) — superseding
  never changes what a past decision relied on'
- 'INV-ASM-04: readers not cleared for some cited evidence get the assessment with
  those references withheld per policy (REQ-ANL-008)'
entities:
- KeyJudgment (statement, probability term, confidence)
- Citation (finding | evidence, pinned version)
requirements:
- REQ-ANL-005
- REQ-ANL-006
- REQ-ANL-008
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-ASM-DRAFT
  to: DRAFT
  guard: case exists; either new assessment or revision of a PUBLISHED version (copies
    content); at most one DRAFT/IN_REVIEW per assessment
  event: EVT-ASM-DRAFTED
  guard_error: DRAFT_EXISTS
- from:
  - DRAFT
  command: CMD-ASM-EDIT
  to: '='
  guard: key judgments use RD-ESTIMATIVE-PROBABILITY terms and analytic confidence
    (low/moderate/high)
  event: EVT-ASM-EDITED
  guard_error: ASSESSMENT_INVALID
- from:
  - DRAFT
  command: CMD-ASM-SUBMIT
  to: IN_REVIEW
  guard: findings ≥ 1 (ACCEPTED), evidence, assumptions, uncertainty, confidence,
    methodology, limitations all present (REQ-ANL-005)
  event: EVT-ASM-SUBMITTED
  guard_error: ASSESSMENT_INCOMPLETE
- from:
  - IN_REVIEW
  command: CMD-ASM-RETURN
  to: DRAFT
  guard: reviewer; reason
  event: EVT-ASM-RETURNED
  guard_error: REASON_REQUIRED
- from:
  - IN_REVIEW
  command: CMD-ASM-PUBLISH
  to: PUBLISHED
  guard: reviewer ≠ author; label ≥ max(findings, evidence); previous PUBLISHED version
    → SUPERSEDED in the same transaction
  event: EVT-ASM-PUBLISHED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - PUBLISHED
  command: SYS:newer version published
  to: SUPERSEDED
  guard: system
  event: EVT-ASM-SUPERSEDED
  guard_error: null
- from:
  - PUBLISHED
  command: CMD-ASM-WITHDRAW
  to: WITHDRAWN
  guard: reason; decisions and products referencing it are notified
  event: EVT-ASM-WITHDRAWN
  guard_error: REASON_REQUIRED
- from:
  - DRAFT
  command: CMD-ASM-DISCARD
  to: DISCARDED
  guard: author; reason
  event: EVT-ASM-DISCARDED
  guard_error: REASON_REQUIRED
```

</details>
