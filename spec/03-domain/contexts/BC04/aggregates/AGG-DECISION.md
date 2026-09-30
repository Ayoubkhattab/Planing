---
id: AGG-DECISION
type: aggregate
title: Decision
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
  - REQ-DEC-002
  - REQ-DEC-003
  - REQ-DEC-004
  state_machine: SM-DECISION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-DECISION — Decision

**الغرض:** قرار مسجل بسلطة مختصة وخيار ومبرر وسريان؛ غير قابل للتعديل  
**السياق:** BC04 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-DEC-01** — immutable after recording (REQ-DEC-004); changes are new decisions that supersede
- **INV-DEC-02** — authority snapshot (grant chain, delegation depth, limits) is stored and remains verifiable as-of recorded_at
- **INV-DEC-03** — every decision links to ≥ 1 assessment or evidence (REQ-DEC-003, OUT-04 target 100 %)
- **INV-DEC-04** — effective time and record time are distinct; retroactive effect limited to 1 h unless tenant policy allows longer

## مكونات داخلية

- AuthoritySnapshot
- Citation (pinned)

## الحالات

- غير نهائية: RECORDED
- نهائية: SUPERSEDED, ANNULLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-DEC-RECORD | RECORDED | AuthorityCheck(decider, decision type, scope, now) = authorized — grant chain stored as authority snapshot (BRL-003, REQ-DEC-002); request OPEN (or ad-hoc with rationale and ≥ 1 citation); selected option ∈ request options; rationale; effective_from ≥ now − 1 h; supersedes (optional) is RECORDED and same scope | EVT-DEC-RECORDED | AUTHORITY_REQUIRED |
| RECORDED | SYS:superseding decision recorded | SUPERSEDED | new decision references this one in supersedes | EVT-DEC-SUPERSEDED | — |
| RECORDED | CMD-DEC-ANNUL | ANNULLED | recorded in error; actor holds authority for the same decision type at a higher scope; reason; plans implementing it are flagged | EVT-DEC-ANNULLED | AUTHORITY_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-DEC-RECORD | SYS:superseding decision recorded | CMD-DEC-ANNUL |
|---|---|---|---|
| ∅ | → RECORDED | — | — |
| RECORDED | ✗ DECISION_INVALID_STATE_TRANSITION | → SUPERSEDED | → ANNULLED |
| SUPERSEDED | ✗ DECISION_INVALID_STATE_TRANSITION | ✗ DECISION_INVALID_STATE_TRANSITION | ✗ DECISION_INVALID_STATE_TRANSITION |
| ANNULLED | ✗ DECISION_INVALID_STATE_TRANSITION | ✗ DECISION_INVALID_STATE_TRANSITION | ✗ DECISION_INVALID_STATE_TRANSITION |

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
id: AGG-DECISION
bc: BC04
name: Decision
tier: T2
purpose: قرار مسجل بسلطة مختصة وخيار ومبرر وسريان؛ غير قابل للتعديل
states:
- RECORDED
- SUPERSEDED
- ANNULLED
terminal:
- SUPERSEDED
- ANNULLED
invariants:
- 'INV-DEC-01: immutable after recording (REQ-DEC-004); changes are new decisions
  that supersede'
- 'INV-DEC-02: authority snapshot (grant chain, delegation depth, limits) is stored
  and remains verifiable as-of recorded_at'
- 'INV-DEC-03: every decision links to ≥ 1 assessment or evidence (REQ-DEC-003, OUT-04
  target 100 %)'
- 'INV-DEC-04: effective time and record time are distinct; retroactive effect limited
  to 1 h unless tenant policy allows longer'
entities:
- AuthoritySnapshot
- Citation (pinned)
requirements:
- REQ-DEC-002
- REQ-DEC-003
- REQ-DEC-004
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-DEC-RECORD
  to: RECORDED
  guard: AuthorityCheck(decider, decision type, scope, now) = authorized — grant chain
    stored as authority snapshot (BRL-003, REQ-DEC-002); request OPEN (or ad-hoc with
    rationale and ≥ 1 citation); selected option ∈ request options; rationale; effective_from
    ≥ now − 1 h; supersedes (optional) is RECORDED and same scope
  event: EVT-DEC-RECORDED
  guard_error: AUTHORITY_REQUIRED
- from:
  - RECORDED
  command: SYS:superseding decision recorded
  to: SUPERSEDED
  guard: new decision references this one in supersedes
  event: EVT-DEC-SUPERSEDED
  guard_error: null
- from:
  - RECORDED
  command: CMD-DEC-ANNUL
  to: ANNULLED
  guard: recorded in error; actor holds authority for the same decision type at a
    higher scope; reason; plans implementing it are flagged
  event: EVT-DEC-ANNULLED
  guard_error: AUTHORITY_REQUIRED
```

</details>
