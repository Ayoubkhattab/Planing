---
id: AGG-KNOWLEDGE-OBJECT
type: aggregate
title: Knowledge Object Version
wave: W4
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC06
importance_tier: T1 content / T2 lifecycle
personal_data: false
traces:
  satisfies:
  - REQ-KNW-001
  - REQ-KNW-002
  - REQ-KNW-003
  state_machine: SM-KNOWLEDGE-OBJECT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-KNOWLEDGE-OBJECT — Knowledge Object Version

**الغرض:** إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات  
**السياق:** BC06 · **المستوى:** T1 content / T2 lifecycle · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-KNO-01** — published versions are immutable; one PUBLISHED version per knowledge object
- **INV-KNO-02** — knowledge statements are not claims about the world (they do not enter BC02 resolution); they cite claims and evidence
- **INV-KNO-03** — policy knowledge describes a policy but never changes authorization (the PDP ignores it) — glossary CR-33

## مكونات داخلية

- Statement
- EvidenceLink
- Relationship (to task type / plan type / entity type / area)

## الحالات

- غير نهائية: DRAFT, IN_REVIEW, PUBLISHED
- نهائية: REJECTED, SUPERSEDED, RETIRED, DISCARDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-KNO-DRAFT | DRAFT | type ∈ {procedure, lesson, best_practice, policy_knowledge}; lessons reference a terminal source (task, plan, incident, or a completed exercise simulation — CR-63) and its evidence (REQ-KNW-002); label ≥ source label | EVT-KNO-DRAFTED | KNOWLEDGE_INVALID |
| DRAFT | CMD-KNO-EDIT | (بلا تغيير) | statements with evidence links; relationships to task types, plan types, entity types, areas | EVT-KNO-EDITED | KNOWLEDGE_INVALID |
| DRAFT | CMD-KNO-SUBMIT | IN_REVIEW | ≥ 1 statement; lessons: ≥ 1 evidence link | EVT-KNO-SUBMITTED | KNOWLEDGE_INCOMPLETE |
| IN_REVIEW | CMD-KNO-RETURN | DRAFT | reviewer; reason | EVT-KNO-RETURNED | REASON_REQUIRED |
| IN_REVIEW | CMD-KNO-PUBLISH | PUBLISHED | reviewer ≠ author; procedures and policy knowledge require the owning authority (Knowledge Manager + domain authority); previous PUBLISHED → SUPERSEDED | EVT-KNO-PUBLISHED | SEGREGATION_OF_DUTIES |
| IN_REVIEW | CMD-KNO-REJECT | REJECTED | reason | EVT-KNO-REJECTED | REASON_REQUIRED |
| PUBLISHED | CMD-KNO-RECORD-REUSE | (بلا تغيير) | target plan/task/product visible; reuse counted (OUT-06) | EVT-KNO-REUSED | TARGET_INVALID |
| PUBLISHED | SYS:newer version published | SUPERSEDED | system | EVT-KNO-SUPERSEDED | — |
| PUBLISHED | CMD-KNO-RETIRE | RETIRED | reason (obsolete, wrong) | EVT-KNO-RETIRED | REASON_REQUIRED |
| DRAFT | CMD-KNO-DISCARD | DISCARDED | author; reason | EVT-KNO-DISCARDED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-KNO-DRAFT | CMD-KNO-EDIT | CMD-KNO-SUBMIT | CMD-KNO-RETURN | CMD-KNO-PUBLISH | CMD-KNO-REJECT | CMD-KNO-RECORD-REUSE | SYS:newer version published | CMD-KNO-RETIRE | CMD-KNO-DISCARD |
|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — | — | — | — |
| DRAFT | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | → DRAFT | → IN_REVIEW | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | → DISCARDED |
| IN_REVIEW | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | → DRAFT | → PUBLISHED | → REJECTED | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
| PUBLISHED | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | → PUBLISHED | → SUPERSEDED | → RETIRED | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
| REJECTED | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
| SUPERSEDED | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
| RETIRED | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
| DISCARDED | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | ✗ KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-12.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-KNOWLEDGE-OBJECT
bc: BC06
name: Knowledge Object Version
tier: T1 content / T2 lifecycle
purpose: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات
states:
- DRAFT
- IN_REVIEW
- PUBLISHED
- REJECTED
- SUPERSEDED
- RETIRED
- DISCARDED
terminal:
- REJECTED
- SUPERSEDED
- RETIRED
- DISCARDED
invariants:
- 'INV-KNO-01: published versions are immutable; one PUBLISHED version per knowledge
  object'
- 'INV-KNO-02: knowledge statements are not claims about the world (they do not enter
  BC02 resolution); they cite claims and evidence'
- 'INV-KNO-03: policy knowledge describes a policy but never changes authorization
  (the PDP ignores it) — glossary CR-33'
entities:
- Statement
- EvidenceLink
- Relationship (to task type / plan type / entity type / area)
requirements:
- REQ-KNW-001
- REQ-KNW-002
- REQ-KNW-003
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-KNO-DRAFT
  to: DRAFT
  guard: type ∈ {procedure, lesson, best_practice, policy_knowledge}; lessons reference
    a terminal source (task, plan, incident, or a completed exercise simulation —
    CR-63) and its evidence (REQ-KNW-002); label ≥ source label
  event: EVT-KNO-DRAFTED
  guard_error: KNOWLEDGE_INVALID
- from:
  - DRAFT
  command: CMD-KNO-EDIT
  to: '='
  guard: statements with evidence links; relationships to task types, plan types,
    entity types, areas
  event: EVT-KNO-EDITED
  guard_error: KNOWLEDGE_INVALID
- from:
  - DRAFT
  command: CMD-KNO-SUBMIT
  to: IN_REVIEW
  guard: '≥ 1 statement; lessons: ≥ 1 evidence link'
  event: EVT-KNO-SUBMITTED
  guard_error: KNOWLEDGE_INCOMPLETE
- from:
  - IN_REVIEW
  command: CMD-KNO-RETURN
  to: DRAFT
  guard: reviewer; reason
  event: EVT-KNO-RETURNED
  guard_error: REASON_REQUIRED
- from:
  - IN_REVIEW
  command: CMD-KNO-PUBLISH
  to: PUBLISHED
  guard: reviewer ≠ author; procedures and policy knowledge require the owning authority
    (Knowledge Manager + domain authority); previous PUBLISHED → SUPERSEDED
  event: EVT-KNO-PUBLISHED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - IN_REVIEW
  command: CMD-KNO-REJECT
  to: REJECTED
  guard: reason
  event: EVT-KNO-REJECTED
  guard_error: REASON_REQUIRED
- from:
  - PUBLISHED
  command: CMD-KNO-RECORD-REUSE
  to: '='
  guard: target plan/task/product visible; reuse counted (OUT-06)
  event: EVT-KNO-REUSED
  guard_error: TARGET_INVALID
- from:
  - PUBLISHED
  command: SYS:newer version published
  to: SUPERSEDED
  guard: system
  event: EVT-KNO-SUPERSEDED
  guard_error: null
- from:
  - PUBLISHED
  command: CMD-KNO-RETIRE
  to: RETIRED
  guard: reason (obsolete, wrong)
  event: EVT-KNO-RETIRED
  guard_error: REASON_REQUIRED
- from:
  - DRAFT
  command: CMD-KNO-DISCARD
  to: DISCARDED
  guard: author; reason
  event: EVT-KNO-DISCARDED
  guard_error: REASON_REQUIRED
```

</details>
