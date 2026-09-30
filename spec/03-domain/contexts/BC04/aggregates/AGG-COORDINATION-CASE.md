---
id: AGG-COORDINATION-CASE
type: aggregate
title: Coordination Case
wave: W4
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC04
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-CRD-001
  - REQ-CRD-002
  state_machine: SM-COORDINATION-CASE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-COORDINATION-CASE — Coordination Case

**الغرض:** تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة  
**السياق:** BC04 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-CRD-01** — coordination is within one tenant; cross-tenant coordination uses product distribution/export only (R2 decision)
- **INV-CRD-02** — each participant sees only its access scope (sections) and objects its members may see (REQ-CRD-001)
- **INV-CRD-03** — an action needing another organization's authority is never marked done without that authority's recorded decision (REQ-CRD-002, BRL-003)
- **INV-CRD-04** — the case links decisions and plans; it never replaces them

## مكونات داخلية

- Participant (org unit, role, access scope)
- Responsibility (item, participant, due, requires_authority, decision_request, status)

## الحالات

- غير نهائية: OPEN, ACTIVE
- نهائية: CLOSED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-CRD-OPEN | OPEN | title; purpose; lead organization; linked decisions/plans/situations visible to the opener; label | EVT-CRD-OPENED | COORDINATION_INVALID |
| OPEN, ACTIVE | CMD-CRD-ADD-PARTICIPANT | (بلا تغيير) | org unit in the same tenant; participant role; access scope (sections); participant's members cleared for case label | EVT-CRD-PARTICIPANT-ADDED | PARTICIPANT_INVALID |
| OPEN, ACTIVE | CMD-CRD-REMOVE-PARTICIPANT | (بلا تغيير) | not the lead; no open responsibilities | EVT-CRD-PARTICIPANT-REMOVED | PARTICIPANT_HAS_RESPONSIBILITIES |
| OPEN | CMD-CRD-ACTIVATE | ACTIVE | ≥ 2 participants | EVT-CRD-ACTIVATED | PARTICIPANTS_REQUIRED |
| ACTIVE | CMD-CRD-ASSIGN-RESPONSIBILITY | (بلا تغيير) | participant exists; item, due; flag requires_authority (decision type) when the action needs that organization's authority | EVT-CRD-RESPONSIBILITY-ASSIGNED | RESPONSIBILITY_INVALID |
| ACTIVE | CMD-CRD-UPDATE-RESPONSIBILITY | (بلا تغيير) | actor belongs to the responsible participant; status ∈ {in_progress, done, waived with reason}; items requiring authority cannot be done before the decision is recorded | EVT-CRD-RESPONSIBILITY-UPDATED | DECISION_PENDING |
| ACTIVE | CMD-CRD-REQUEST-DECISION | (بلا تغيير) | responsibility requires authority; creates a Decision Request (SLC-08) in the participant's scope with the required decision type | EVT-CRD-DECISION-REQUESTED | RESPONSIBILITY_INVALID |
| ACTIVE | SYS:linked decision recorded | (بلا تغيير) | decision references the request created by the case; outcome stored on the responsibility | EVT-CRD-DECISION-RECORDED | — |
| ACTIVE | CMD-CRD-CLOSE | CLOSED | all responsibilities done or waived; closing note | EVT-CRD-CLOSED | OPEN_RESPONSIBILITIES |
| OPEN, ACTIVE | CMD-CRD-CANCEL | CANCELLED | lead; reason | EVT-CRD-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-CRD-OPEN | CMD-CRD-ADD-PARTICIPANT | CMD-CRD-REMOVE-PARTICIPANT | CMD-CRD-ACTIVATE | CMD-CRD-ASSIGN-RESPONSIBILITY | CMD-CRD-UPDATE-RESPONSIBILITY | CMD-CRD-REQUEST-DECISION | SYS:linked decision recorded | CMD-CRD-CLOSE | CMD-CRD-CANCEL |
|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → OPEN | — | — | — | — | — | — | — | — | — |
| OPEN | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | → OPEN | → OPEN | → ACTIVE | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | → CANCELLED |
| ACTIVE | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | → ACTIVE | → ACTIVE | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | → ACTIVE | → ACTIVE | → ACTIVE | → ACTIVE | → CLOSED | → CANCELLED |
| CLOSED | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION | ✗ COORDINATION_CASE_INVALID_STATE_TRANSITION |

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
id: AGG-COORDINATION-CASE
bc: BC04
name: Coordination Case
tier: T2
purpose: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة
states:
- OPEN
- ACTIVE
- CLOSED
- CANCELLED
terminal:
- CLOSED
- CANCELLED
invariants:
- 'INV-CRD-01: coordination is within one tenant; cross-tenant coordination uses product
  distribution/export only (R2 decision)'
- 'INV-CRD-02: each participant sees only its access scope (sections) and objects
  its members may see (REQ-CRD-001)'
- 'INV-CRD-03: an action needing another organization''s authority is never marked
  done without that authority''s recorded decision (REQ-CRD-002, BRL-003)'
- 'INV-CRD-04: the case links decisions and plans; it never replaces them'
entities:
- Participant (org unit, role, access scope)
- Responsibility (item, participant, due, requires_authority, decision_request, status)
requirements:
- REQ-CRD-001
- REQ-CRD-002
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-CRD-OPEN
  to: OPEN
  guard: title; purpose; lead organization; linked decisions/plans/situations visible
    to the opener; label
  event: EVT-CRD-OPENED
  guard_error: COORDINATION_INVALID
- from:
  - OPEN
  - ACTIVE
  command: CMD-CRD-ADD-PARTICIPANT
  to: '='
  guard: org unit in the same tenant; participant role; access scope (sections); participant's
    members cleared for case label
  event: EVT-CRD-PARTICIPANT-ADDED
  guard_error: PARTICIPANT_INVALID
- from:
  - OPEN
  - ACTIVE
  command: CMD-CRD-REMOVE-PARTICIPANT
  to: '='
  guard: not the lead; no open responsibilities
  event: EVT-CRD-PARTICIPANT-REMOVED
  guard_error: PARTICIPANT_HAS_RESPONSIBILITIES
- from:
  - OPEN
  command: CMD-CRD-ACTIVATE
  to: ACTIVE
  guard: ≥ 2 participants
  event: EVT-CRD-ACTIVATED
  guard_error: PARTICIPANTS_REQUIRED
- from:
  - ACTIVE
  command: CMD-CRD-ASSIGN-RESPONSIBILITY
  to: '='
  guard: participant exists; item, due; flag requires_authority (decision type) when
    the action needs that organization's authority
  event: EVT-CRD-RESPONSIBILITY-ASSIGNED
  guard_error: RESPONSIBILITY_INVALID
- from:
  - ACTIVE
  command: CMD-CRD-UPDATE-RESPONSIBILITY
  to: '='
  guard: actor belongs to the responsible participant; status ∈ {in_progress, done,
    waived with reason}; items requiring authority cannot be done before the decision
    is recorded
  event: EVT-CRD-RESPONSIBILITY-UPDATED
  guard_error: DECISION_PENDING
- from:
  - ACTIVE
  command: CMD-CRD-REQUEST-DECISION
  to: '='
  guard: responsibility requires authority; creates a Decision Request (SLC-08) in
    the participant's scope with the required decision type
  event: EVT-CRD-DECISION-REQUESTED
  guard_error: RESPONSIBILITY_INVALID
- from:
  - ACTIVE
  command: SYS:linked decision recorded
  to: '='
  guard: decision references the request created by the case; outcome stored on the
    responsibility
  event: EVT-CRD-DECISION-RECORDED
  guard_error: null
- from:
  - ACTIVE
  command: CMD-CRD-CLOSE
  to: CLOSED
  guard: all responsibilities done or waived; closing note
  event: EVT-CRD-CLOSED
  guard_error: OPEN_RESPONSIBILITIES
- from:
  - OPEN
  - ACTIVE
  command: CMD-CRD-CANCEL
  to: CANCELLED
  guard: lead; reason
  event: EVT-CRD-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
