---
id: AGG-PLAN
type: aggregate
title: Plan (identity)
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
  - REQ-OPS-002
  - REQ-OPS-003
  state_machine: SM-PLAN
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-PLAN — Plan (identity)

**الغرض:** هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها  
**السياق:** BC04 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-PLN-01** — ACTIVE ⇔ exactly one BASELINED version exists
- **INV-PLN-02** — a plan implements ≥ 1 decision or objective, or (plan_kind=CONTINGENCY) ≥ 1 risk or incident trigger (CR-60)
- **INV-PLN-03** — plan identity holds no content; content lives in versions (CR-29)
- **INV-PLN-04** — plan_kind ∈ {OPERATIONS, CONTINGENCY}, immutable after creation; only a CONTINGENCY plan may carry a triggered_by reference (CR-60, SLC-17)

## الحالات

- غير نهائية: DRAFT, ACTIVE, SUSPENDED, COMPLETED
- نهائية: CLOSED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-PLN-CREATE | DRAFT | title; owner; org scope; implements ≥ 1 decision (RECORDED) or objective (REQ-OPS-002), or for plan_kind=CONTINGENCY a risk_ref or incident_ref trigger (CR-60, SLC-17); label ≥ implemented decisions or triggering scope's label | EVT-PLN-CREATED | PLAN_INVALID |
| DRAFT | SYS:first version baselined | ACTIVE | EVT-PLV-BASELINED for this plan | EVT-PLN-ACTIVATED | — |
| ACTIVE | CMD-PLN-SUSPEND | SUSPENDED | reason; open tasks suspended (flag, INV-TASK-06) | EVT-PLN-SUSPENDED | REASON_REQUIRED |
| SUSPENDED | CMD-PLN-RESUME | ACTIVE | reason; tasks unsuspended | EVT-PLN-RESUMED | REASON_REQUIRED |
| ACTIVE | CMD-PLN-COMPLETE | COMPLETED | all plan tasks terminal; every outcome has ≥ 1 measurement | EVT-PLN-COMPLETED | PLAN_NOT_COMPLETABLE |
| COMPLETED | CMD-PLN-CLOSE | CLOSED | after-action notes (optional in R1); outcome trackers closed | EVT-PLN-CLOSED | — |
| DRAFT, ACTIVE, SUSPENDED | CMD-PLN-CANCEL | CANCELLED | authority; reason; open tasks cancelled | EVT-PLN-CANCELLED | REASON_REQUIRED |
| DRAFT, ACTIVE, SUSPENDED | CMD-PLN-RECLASSIFY | (بلا تغيير) | authority; new label ≥ implemented decisions; assignees without clearance → reassignment required | EVT-PLN-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| ACTIVE, SUSPENDED | SYS:implemented decision annulled or superseded | (بلا تغيير) | plan flagged for review (no automatic change) | EVT-PLN-REVIEW-FLAGGED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-PLN-CREATE | SYS:first version baselined | CMD-PLN-SUSPEND | CMD-PLN-RESUME | CMD-PLN-COMPLETE | CMD-PLN-CLOSE | CMD-PLN-CANCEL | CMD-PLN-RECLASSIFY | SYS:implemented decision annulled or superseded |
|---|---|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — | — | — |
| DRAFT | ✗ PLAN_INVALID_STATE_TRANSITION | → ACTIVE | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | → CANCELLED | → DRAFT | ✗ PLAN_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | → SUSPENDED | ✗ PLAN_INVALID_STATE_TRANSITION | → COMPLETED | ✗ PLAN_INVALID_STATE_TRANSITION | → CANCELLED | → ACTIVE | → ACTIVE |
| SUSPENDED | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | → ACTIVE | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | → CANCELLED | → SUSPENDED | → SUSPENDED |
| COMPLETED | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | → CLOSED | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION |
| CLOSED | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION | ✗ PLAN_INVALID_STATE_TRANSITION |

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
id: AGG-PLAN
bc: BC04
name: Plan (identity)
tier: T2
purpose: هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها
states:
- DRAFT
- ACTIVE
- SUSPENDED
- COMPLETED
- CLOSED
- CANCELLED
terminal:
- CLOSED
- CANCELLED
invariants:
- 'INV-PLN-01: ACTIVE ⇔ exactly one BASELINED version exists'
- 'INV-PLN-02: a plan implements ≥ 1 decision or objective, or (plan_kind=CONTINGENCY)
  ≥ 1 risk or incident trigger (CR-60)'
- 'INV-PLN-03: plan identity holds no content; content lives in versions (CR-29)'
- 'INV-PLN-04: plan_kind ∈ {OPERATIONS, CONTINGENCY}, immutable after creation; only
  a CONTINGENCY plan may carry a triggered_by reference (CR-60, SLC-17)'
entities: []
requirements:
- REQ-OPS-001
- REQ-OPS-002
- REQ-OPS-003
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-PLN-CREATE
  to: DRAFT
  guard: title; owner; org scope; implements ≥ 1 decision (RECORDED) or objective
    (REQ-OPS-002), or for plan_kind=CONTINGENCY a risk_ref or incident_ref trigger
    (CR-60, SLC-17); label ≥ implemented decisions or triggering scope's label
  event: EVT-PLN-CREATED
  guard_error: PLAN_INVALID
- from:
  - DRAFT
  command: SYS:first version baselined
  to: ACTIVE
  guard: EVT-PLV-BASELINED for this plan
  event: EVT-PLN-ACTIVATED
  guard_error: null
- from:
  - ACTIVE
  command: CMD-PLN-SUSPEND
  to: SUSPENDED
  guard: reason; open tasks suspended (flag, INV-TASK-06)
  event: EVT-PLN-SUSPENDED
  guard_error: REASON_REQUIRED
- from:
  - SUSPENDED
  command: CMD-PLN-RESUME
  to: ACTIVE
  guard: reason; tasks unsuspended
  event: EVT-PLN-RESUMED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  command: CMD-PLN-COMPLETE
  to: COMPLETED
  guard: all plan tasks terminal; every outcome has ≥ 1 measurement
  event: EVT-PLN-COMPLETED
  guard_error: PLAN_NOT_COMPLETABLE
- from:
  - COMPLETED
  command: CMD-PLN-CLOSE
  to: CLOSED
  guard: after-action notes (optional in R1); outcome trackers closed
  event: EVT-PLN-CLOSED
  guard_error: null
- from:
  - DRAFT
  - ACTIVE
  - SUSPENDED
  command: CMD-PLN-CANCEL
  to: CANCELLED
  guard: authority; reason; open tasks cancelled
  event: EVT-PLN-CANCELLED
  guard_error: REASON_REQUIRED
- from:
  - DRAFT
  - ACTIVE
  - SUSPENDED
  command: CMD-PLN-RECLASSIFY
  to: '='
  guard: authority; new label ≥ implemented decisions; assignees without clearance
    → reassignment required
  event: EVT-PLN-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
- from:
  - ACTIVE
  - SUSPENDED
  command: SYS:implemented decision annulled or superseded
  to: '='
  guard: plan flagged for review (no automatic change)
  event: EVT-PLN-REVIEW-FLAGGED
  guard_error: null
```

</details>
