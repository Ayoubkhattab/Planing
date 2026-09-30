---
id: AGG-SITUATION
type: aggregate
title: Situation
wave: W4
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC03
importance_tier: T2 definition; content is a projection
personal_data: false
traces:
  satisfies:
  - REQ-SIT-001
  - REQ-SIT-002
  - REQ-SIT-003
  state_machine: SM-SITUATION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SITUATION — Situation

**الغرض:** سياق تشغيلي بامتداد وزمن ومعايير عضوية؛ محتواه إسقاط (ADR-P07)  
**السياق:** BC03 · **المستوى:** T2 definition; content is a projection · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-SIT-01** — members stay owned by their contexts; the situation stores only definition, membership records and change log
- **INV-SIT-02** — a reader sees a situation only if cleared for its label, and sees each member only if cleared for that member (per-member filtering)
- **INV-SIT-03** — membership is evaluated against the definition version that was ACTIVE at the evaluation time (history reproducible)
- **INV-SIT-04** — a CLOSED situation keeps its final snapshot and change log

## مكونات داخلية

- DefinitionVersion (extent, window, criteria)
- MembershipRecord (member_urn, from, to, cause)
- SituationChange

## الحالات

- غير نهائية: DRAFT, ACTIVE, PAUSED
- نهائية: CLOSED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-SIT-CREATE | DRAFT | name; extent (polygon or buffer around an entity); time window; criteria valid per SPEC-SITUATION §2; owner; label | EVT-SIT-CREATED | SITUATION_INVALID |
| DRAFT, ACTIVE, PAUSED | CMD-SIT-EDIT-DEFINITION | (بلا تغيير) | criteria/extent/window valid; new definition version; membership recomputed from the new version | EVT-SIT-DEFINITION-CHANGED | SITUATION_INVALID |
| DRAFT | CMD-SIT-ACTIVATE | ACTIVE | definition complete; active situations per tenant ≤ quota | EVT-SIT-ACTIVATED | QUOTA_EXCEEDED |
| ACTIVE | CMD-SIT-PAUSE | PAUSED | reason; membership frozen, alerts of its rules suspended | EVT-SIT-PAUSED | REASON_REQUIRED |
| PAUSED | CMD-SIT-RESUME | ACTIVE | membership re-evaluated from current state | EVT-SIT-RESUMED | — |
| DRAFT, ACTIVE, PAUSED | CMD-SIT-CLOSE | CLOSED | reason; final membership snapshot recorded | EVT-SIT-CLOSED | REASON_REQUIRED |
| DRAFT, ACTIVE, PAUSED | CMD-SIT-RECLASSIFY | (بلا تغيير) | authority per tenant policy; subscribers without clearance are unsubscribed | EVT-SIT-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-SIT-CREATE | CMD-SIT-EDIT-DEFINITION | CMD-SIT-ACTIVATE | CMD-SIT-PAUSE | CMD-SIT-RESUME | CMD-SIT-CLOSE | CMD-SIT-RECLASSIFY |
|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — |
| DRAFT | ✗ SITUATION_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ SITUATION_INVALID_STATE_TRANSITION | ✗ SITUATION_INVALID_STATE_TRANSITION | → CLOSED | → DRAFT |
| ACTIVE | ✗ SITUATION_INVALID_STATE_TRANSITION | → ACTIVE | ✗ SITUATION_INVALID_STATE_TRANSITION | → PAUSED | ✗ SITUATION_INVALID_STATE_TRANSITION | → CLOSED | → ACTIVE |
| PAUSED | ✗ SITUATION_INVALID_STATE_TRANSITION | → PAUSED | ✗ SITUATION_INVALID_STATE_TRANSITION | ✗ SITUATION_INVALID_STATE_TRANSITION | → ACTIVE | → CLOSED | → PAUSED |
| CLOSED | ✗ SITUATION_INVALID_STATE_TRANSITION | ✗ SITUATION_INVALID_STATE_TRANSITION | ✗ SITUATION_INVALID_STATE_TRANSITION | ✗ SITUATION_INVALID_STATE_TRANSITION | ✗ SITUATION_INVALID_STATE_TRANSITION | ✗ SITUATION_INVALID_STATE_TRANSITION | ✗ SITUATION_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-06.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-SITUATION
bc: BC03
name: Situation
tier: T2 definition; content is a projection
purpose: سياق تشغيلي بامتداد وزمن ومعايير عضوية؛ محتواه إسقاط (ADR-P07)
states:
- DRAFT
- ACTIVE
- PAUSED
- CLOSED
terminal:
- CLOSED
invariants:
- 'INV-SIT-01: members stay owned by their contexts; the situation stores only definition,
  membership records and change log'
- 'INV-SIT-02: a reader sees a situation only if cleared for its label, and sees each
  member only if cleared for that member (per-member filtering)'
- 'INV-SIT-03: membership is evaluated against the definition version that was ACTIVE
  at the evaluation time (history reproducible)'
- 'INV-SIT-04: a CLOSED situation keeps its final snapshot and change log'
entities:
- DefinitionVersion (extent, window, criteria)
- MembershipRecord (member_urn, from, to, cause)
- SituationChange
requirements:
- REQ-SIT-001
- REQ-SIT-002
- REQ-SIT-003
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-SIT-CREATE
  to: DRAFT
  guard: name; extent (polygon or buffer around an entity); time window; criteria
    valid per SPEC-SITUATION §2; owner; label
  event: EVT-SIT-CREATED
  guard_error: SITUATION_INVALID
- from:
  - DRAFT
  - ACTIVE
  - PAUSED
  command: CMD-SIT-EDIT-DEFINITION
  to: '='
  guard: criteria/extent/window valid; new definition version; membership recomputed
    from the new version
  event: EVT-SIT-DEFINITION-CHANGED
  guard_error: SITUATION_INVALID
- from:
  - DRAFT
  command: CMD-SIT-ACTIVATE
  to: ACTIVE
  guard: definition complete; active situations per tenant ≤ quota
  event: EVT-SIT-ACTIVATED
  guard_error: QUOTA_EXCEEDED
- from:
  - ACTIVE
  command: CMD-SIT-PAUSE
  to: PAUSED
  guard: reason; membership frozen, alerts of its rules suspended
  event: EVT-SIT-PAUSED
  guard_error: REASON_REQUIRED
- from:
  - PAUSED
  command: CMD-SIT-RESUME
  to: ACTIVE
  guard: membership re-evaluated from current state
  event: EVT-SIT-RESUMED
  guard_error: null
- from:
  - DRAFT
  - ACTIVE
  - PAUSED
  command: CMD-SIT-CLOSE
  to: CLOSED
  guard: reason; final membership snapshot recorded
  event: EVT-SIT-CLOSED
  guard_error: REASON_REQUIRED
- from:
  - DRAFT
  - ACTIVE
  - PAUSED
  command: CMD-SIT-RECLASSIFY
  to: '='
  guard: authority per tenant policy; subscribers without clearance are unsubscribed
  event: EVT-SIT-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
```

</details>
