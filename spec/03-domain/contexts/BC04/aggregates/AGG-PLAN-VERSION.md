---
id: AGG-PLAN-VERSION
type: aggregate
title: Plan Version
wave: W4
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC04
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-OPS-001
  - REQ-OPS-003
  - REQ-OPS-004
  - REQ-OPS-005
  - REQ-OPS-014
  state_machine: SM-PLAN-VERSION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-PLAN-VERSION — Plan Version

**الغرض:** محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس  
**السياق:** BC04 · **المستوى:** T2 · **بيانات شخصية:** لا

> CR-29 closed for Plan: the 14 components of PRJ§62 are version content (7 internal entity kinds, SL-24 ≤ 7).

## الثوابت (Invariants)

- **INV-PLV-01** — content is immutable from IN_REVIEW onwards; BASELINED content never changes (BRL-004, REQ-OPS-003)
- **INV-PLV-02** — exactly one BASELINED version per plan
- **INV-PLV-03** — activity ids are stable across versions, so task synchronization is a deterministic diff
- **INV-PLV-04** — a major change (objectives, outcomes, phases, milestone dates, resource commitments) is possible only through a new version (BRL-005)
- **INV-PLV-05** — dependencies acyclic; all dates inside the plan window

## مكونات داخلية

- Objective
- Outcome (metric, unit, target, due)
- Phase
- Activity (stable id, task_generating, task_type)
- Milestone
- Dependency
- ResourceNote (text, R1 — DEBT-001)

## الحالات

- غير نهائية: DRAFT, IN_REVIEW, BASELINED
- نهائية: SUPERSEDED, REJECTED, DISCARDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-PLV-DRAFT | DRAFT | plan not CLOSED/CANCELLED; new or revision copying the BASELINED version (activity ids preserved); ≤ 1 DRAFT/IN_REVIEW per plan | EVT-PLV-DRAFTED | DRAFT_EXISTS |
| DRAFT | CMD-PLV-EDIT | (بلا تغيير) | objectives, outcomes (metric, unit, target, due), phases, activities (stable ids, task_generating flag, task type), milestones, schedule within plan window, acyclic dependencies | EVT-PLV-EDITED | PLAN_VERSION_INVALID |
| DRAFT | CMD-PLV-SUBMIT | IN_REVIEW | complete per REQ-OPS-001; change classification computed vs current baseline (major/minor, BRL-005) | EVT-PLV-SUBMITTED | PLAN_VERSION_INCOMPLETE |
| IN_REVIEW | CMD-PLV-RETURN | DRAFT | reviewer; reason | EVT-PLV-RETURNED | REASON_REQUIRED |
| IN_REVIEW | CMD-PLV-APPROVE | BASELINED | approver ≠ author (REQ-OPS-005); AuthorityCheck(approver, plan-approval type, scope); previous BASELINED → SUPERSEDED in the same transaction; task synchronization started (SPEC-PLAN §3) | EVT-PLV-BASELINED | SEGREGATION_OF_DUTIES |
| IN_REVIEW | CMD-PLV-REJECT | REJECTED | reason | EVT-PLV-REJECTED | REASON_REQUIRED |
| BASELINED | CMD-PLV-AMEND-MINOR | (بلا تغيير) | only minor fields (descriptions, notes, attachments) per BRL-005; recorded as annotation, baseline content unchanged | EVT-PLV-MINOR-AMENDED | MAJOR_CHANGE_REQUIRES_VERSION |
| BASELINED | SYS:newer version baselined | SUPERSEDED | system | EVT-PLV-SUPERSEDED | — |
| DRAFT | CMD-PLV-DISCARD | DISCARDED | author; reason | EVT-PLV-DISCARDED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-PLV-DRAFT | CMD-PLV-EDIT | CMD-PLV-SUBMIT | CMD-PLV-RETURN | CMD-PLV-APPROVE | CMD-PLV-REJECT | CMD-PLV-AMEND-MINOR | SYS:newer version baselined | CMD-PLV-DISCARD |
|---|---|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — | — | — |
| DRAFT | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | → DRAFT | → IN_REVIEW | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | → DISCARDED |
| IN_REVIEW | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | → DRAFT | → BASELINED | → REJECTED | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION |
| BASELINED | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | → BASELINED | → SUPERSEDED | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION |
| SUPERSEDED | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION |
| REJECTED | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION |
| DISCARDED | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION | ✗ PLAN_VERSION_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-08.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-PLAN-VERSION
bc: BC04
name: Plan Version
tier: T2
purpose: 'محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات،
  مقاييس'
states:
- DRAFT
- IN_REVIEW
- BASELINED
- SUPERSEDED
- REJECTED
- DISCARDED
terminal:
- SUPERSEDED
- REJECTED
- DISCARDED
invariants:
- 'INV-PLV-01: content is immutable from IN_REVIEW onwards; BASELINED content never
  changes (BRL-004, REQ-OPS-003)'
- 'INV-PLV-02: exactly one BASELINED version per plan'
- 'INV-PLV-03: activity ids are stable across versions, so task synchronization is
  a deterministic diff'
- 'INV-PLV-04: a major change (objectives, outcomes, phases, milestone dates, resource
  commitments) is possible only through a new version (BRL-005)'
- 'INV-PLV-05: dependencies acyclic; all dates inside the plan window'
entities:
- Objective
- Outcome (metric, unit, target, due)
- Phase
- Activity (stable id, task_generating, task_type)
- Milestone
- Dependency
- ResourceNote (text, R1 — DEBT-001)
requirements:
- REQ-OPS-001
- REQ-OPS-003
- REQ-OPS-004
- REQ-OPS-005
- REQ-OPS-014
notes: 'CR-29 closed for Plan: the 14 components of PRJ§62 are version content (7
  internal entity kinds, SL-24 ≤ 7).'
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-PLV-DRAFT
  to: DRAFT
  guard: plan not CLOSED/CANCELLED; new or revision copying the BASELINED version
    (activity ids preserved); ≤ 1 DRAFT/IN_REVIEW per plan
  event: EVT-PLV-DRAFTED
  guard_error: DRAFT_EXISTS
- from:
  - DRAFT
  command: CMD-PLV-EDIT
  to: '='
  guard: objectives, outcomes (metric, unit, target, due), phases, activities (stable
    ids, task_generating flag, task type), milestones, schedule within plan window,
    acyclic dependencies
  event: EVT-PLV-EDITED
  guard_error: PLAN_VERSION_INVALID
- from:
  - DRAFT
  command: CMD-PLV-SUBMIT
  to: IN_REVIEW
  guard: complete per REQ-OPS-001; change classification computed vs current baseline
    (major/minor, BRL-005)
  event: EVT-PLV-SUBMITTED
  guard_error: PLAN_VERSION_INCOMPLETE
- from:
  - IN_REVIEW
  command: CMD-PLV-RETURN
  to: DRAFT
  guard: reviewer; reason
  event: EVT-PLV-RETURNED
  guard_error: REASON_REQUIRED
- from:
  - IN_REVIEW
  command: CMD-PLV-APPROVE
  to: BASELINED
  guard: approver ≠ author (REQ-OPS-005); AuthorityCheck(approver, plan-approval type,
    scope); previous BASELINED → SUPERSEDED in the same transaction; task synchronization
    started (SPEC-PLAN §3)
  event: EVT-PLV-BASELINED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - IN_REVIEW
  command: CMD-PLV-REJECT
  to: REJECTED
  guard: reason
  event: EVT-PLV-REJECTED
  guard_error: REASON_REQUIRED
- from:
  - BASELINED
  command: CMD-PLV-AMEND-MINOR
  to: '='
  guard: only minor fields (descriptions, notes, attachments) per BRL-005; recorded
    as annotation, baseline content unchanged
  event: EVT-PLV-MINOR-AMENDED
  guard_error: MAJOR_CHANGE_REQUIRES_VERSION
- from:
  - BASELINED
  command: SYS:newer version baselined
  to: SUPERSEDED
  guard: system
  event: EVT-PLV-SUPERSEDED
  guard_error: null
- from:
  - DRAFT
  command: CMD-PLV-DISCARD
  to: DISCARDED
  guard: author; reason
  event: EVT-PLV-DISCARDED
  guard_error: REASON_REQUIRED
```

</details>
