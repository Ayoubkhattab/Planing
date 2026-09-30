---
id: AGG-ER-CASE
type: aggregate
title: Entity Resolution Case
wave: W4
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-INF-032
  - REQ-INF-033
  - REQ-INF-034
  state_machine: SM-ER-CASE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ER-CASE — Entity Resolution Case

**الغرض:** حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق  
**السياق:** BC02 · **المستوى:** T2 · **بيانات شخصية:** لا

> Pairwise cases; clusters form transitively. Cluster table is bitemporal (record time) and maintained in the decision transaction (components ≤ 50 → cheap).

## الثوابت (Invariants)

- **INV-ER-01** — claims are never moved or rewritten by merge or split (ER-MODEL §2)
- **INV-ER-02** — identity clusters are connected components of CURRENT MATCH links as known at K; canonical id = smallest ULID in the cluster
- **INV-ER-03** — no cluster may contain two entities joined by a CURRENT NOT_A_MATCH link
- **INV-ER-04** — no automatic merge: MATCHED requires a human decision (W1 Q26, AI-OP-06)
- **INV-ER-05** — a cluster > 50 members requires a second reviewer
- **INV-ER-06** — the decision records decision_basis_level = max label the reviewer could see; a higher-cleared reviewer may request a split

## مكونات داخلية

- SameAsLink (left, right, kind MATCH | NOT_A_MATCH, recorded_from, recorded_to)
- FeatureComparison (per feature: values, similarity, weight)

## الحالات

- غير نهائية: CANDIDATE, UNDER_REVIEW, MATCHED, POSSIBLE_DUPLICATE, SPLIT_REQUIRED
- نهائية: NOT_A_MATCH, SPLIT, WITHDRAWN
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:candidate generator score ≥ propose threshold | CANDIDATE | pair not already in the same cluster; no NOT_A_MATCH link between their clusters; no non-terminal case for the pair | EVT-ER-PROPOSED | — |
| ∅ (إنشاء) | CMD-ER-PROPOSE | CANDIDATE | same conditions; proposer is Analyst or AI suggestion (AIL1, agent recorded) | EVT-ER-PROPOSED | ER_PAIR_INVALID |
| CANDIDATE | CMD-ER-START-REVIEW | UNDER_REVIEW | reviewer cleared for both entity labels | EVT-ER-REVIEW-STARTED | REVIEWER_NOT_CLEARED |
| UNDER_REVIEW | CMD-ER-DECIDE-MATCH | MATCHED | types compatible; neither entity RETIRED; merged cluster contains no NOT_A_MATCH pair; merged cluster size ≤ 50 or second reviewer; reviewer ≠ human proposer; creates MATCH link and recomputes cluster in the same transaction | EVT-ER-MATCHED | MATCH_CONTRADICTS_NOT_A_MATCH |
| UNDER_REVIEW | CMD-ER-DECIDE-NOT-MATCH | NOT_A_MATCH | rationale; creates NOT_A_MATCH link (blocks re-proposal) | EVT-ER-NOT-MATCHED | REASON_REQUIRED |
| UNDER_REVIEW | CMD-ER-PARK | POSSIBLE_DUPLICATE | rationale; insufficient evidence | EVT-ER-PARKED | REASON_REQUIRED |
| POSSIBLE_DUPLICATE | CMD-ER-RESUME | UNDER_REVIEW | new evidence or reason | EVT-ER-RESUMED | REASON_REQUIRED |
| POSSIBLE_DUPLICATE | CMD-ER-DECIDE-NOT-MATCH | NOT_A_MATCH | rationale | EVT-ER-NOT-MATCHED | REASON_REQUIRED |
| MATCHED | CMD-ER-REQUEST-SPLIT | SPLIT_REQUIRED | reason + evidence; requester cleared for both entities | EVT-ER-SPLIT-REQUESTED | REASON_REQUIRED |
| SPLIT_REQUIRED | CMD-ER-CONFIRM-MATCH | MATCHED | reviewer ≠ split requester; rationale | EVT-ER-MATCH-CONFIRMED | SEGREGATION_OF_DUTIES |
| SPLIT_REQUIRED | CMD-ER-SPLIT | SPLIT | reviewer ≠ split requester; closes MATCH link (recorded_to = now); optional NOT_A_MATCH link; recomputes clusters in the same transaction | EVT-ER-SPLIT | SEGREGATION_OF_DUTIES |
| CANDIDATE, UNDER_REVIEW, POSSIBLE_DUPLICATE | CMD-ER-WITHDRAW | WITHDRAWN | reason (e.g. entity retired, duplicate case) | EVT-ER-WITHDRAWN | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:candidate generator score ≥ propose threshold | CMD-ER-PROPOSE | CMD-ER-START-REVIEW | CMD-ER-DECIDE-MATCH | CMD-ER-DECIDE-NOT-MATCH | CMD-ER-PARK | CMD-ER-RESUME | CMD-ER-REQUEST-SPLIT | CMD-ER-CONFIRM-MATCH | CMD-ER-SPLIT | CMD-ER-WITHDRAW |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → CANDIDATE | → CANDIDATE | — | — | — | — | — | — | — | — | — |
| CANDIDATE | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | → UNDER_REVIEW | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | → WITHDRAWN |
| UNDER_REVIEW | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | → MATCHED | → NOT_A_MATCH | → POSSIBLE_DUPLICATE | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | → WITHDRAWN |
| MATCHED | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | → SPLIT_REQUIRED | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION |
| POSSIBLE_DUPLICATE | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | → NOT_A_MATCH | ✗ ER_CASE_INVALID_STATE_TRANSITION | → UNDER_REVIEW | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | → WITHDRAWN |
| SPLIT_REQUIRED | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | → MATCHED | → SPLIT | ✗ ER_CASE_INVALID_STATE_TRANSITION |
| NOT_A_MATCH | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION |
| SPLIT | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION |
| WITHDRAWN | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION | ✗ ER_CASE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-04.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-ER-CASE
bc: BC02
name: Entity Resolution Case
tier: T2
purpose: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق
states:
- CANDIDATE
- UNDER_REVIEW
- MATCHED
- POSSIBLE_DUPLICATE
- SPLIT_REQUIRED
- NOT_A_MATCH
- SPLIT
- WITHDRAWN
terminal:
- NOT_A_MATCH
- SPLIT
- WITHDRAWN
invariants:
- 'INV-ER-01: claims are never moved or rewritten by merge or split (ER-MODEL §2)'
- 'INV-ER-02: identity clusters are connected components of CURRENT MATCH links as
  known at K; canonical id = smallest ULID in the cluster'
- 'INV-ER-03: no cluster may contain two entities joined by a CURRENT NOT_A_MATCH
  link'
- 'INV-ER-04: no automatic merge: MATCHED requires a human decision (W1 Q26, AI-OP-06)'
- 'INV-ER-05: a cluster > 50 members requires a second reviewer'
- 'INV-ER-06: the decision records decision_basis_level = max label the reviewer could
  see; a higher-cleared reviewer may request a split'
entities:
- SameAsLink (left, right, kind MATCH | NOT_A_MATCH, recorded_from, recorded_to)
- 'FeatureComparison (per feature: values, similarity, weight)'
requirements:
- REQ-INF-032
- REQ-INF-033
- REQ-INF-034
notes: Pairwise cases; clusters form transitively. Cluster table is bitemporal (record
  time) and maintained in the decision transaction (components ≤ 50 → cheap).
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: SYS:candidate generator score ≥ propose threshold
  to: CANDIDATE
  guard: pair not already in the same cluster; no NOT_A_MATCH link between their clusters;
    no non-terminal case for the pair
  event: EVT-ER-PROPOSED
  guard_error: null
- from: ∅
  command: CMD-ER-PROPOSE
  to: CANDIDATE
  guard: same conditions; proposer is Analyst or AI suggestion (AIL1, agent recorded)
  event: EVT-ER-PROPOSED
  guard_error: ER_PAIR_INVALID
- from:
  - CANDIDATE
  command: CMD-ER-START-REVIEW
  to: UNDER_REVIEW
  guard: reviewer cleared for both entity labels
  event: EVT-ER-REVIEW-STARTED
  guard_error: REVIEWER_NOT_CLEARED
- from:
  - UNDER_REVIEW
  command: CMD-ER-DECIDE-MATCH
  to: MATCHED
  guard: types compatible; neither entity RETIRED; merged cluster contains no NOT_A_MATCH
    pair; merged cluster size ≤ 50 or second reviewer; reviewer ≠ human proposer;
    creates MATCH link and recomputes cluster in the same transaction
  event: EVT-ER-MATCHED
  guard_error: MATCH_CONTRADICTS_NOT_A_MATCH
- from:
  - UNDER_REVIEW
  command: CMD-ER-DECIDE-NOT-MATCH
  to: NOT_A_MATCH
  guard: rationale; creates NOT_A_MATCH link (blocks re-proposal)
  event: EVT-ER-NOT-MATCHED
  guard_error: REASON_REQUIRED
- from:
  - UNDER_REVIEW
  command: CMD-ER-PARK
  to: POSSIBLE_DUPLICATE
  guard: rationale; insufficient evidence
  event: EVT-ER-PARKED
  guard_error: REASON_REQUIRED
- from:
  - POSSIBLE_DUPLICATE
  command: CMD-ER-RESUME
  to: UNDER_REVIEW
  guard: new evidence or reason
  event: EVT-ER-RESUMED
  guard_error: REASON_REQUIRED
- from:
  - POSSIBLE_DUPLICATE
  command: CMD-ER-DECIDE-NOT-MATCH
  to: NOT_A_MATCH
  guard: rationale
  event: EVT-ER-NOT-MATCHED
  guard_error: REASON_REQUIRED
- from:
  - MATCHED
  command: CMD-ER-REQUEST-SPLIT
  to: SPLIT_REQUIRED
  guard: reason + evidence; requester cleared for both entities
  event: EVT-ER-SPLIT-REQUESTED
  guard_error: REASON_REQUIRED
- from:
  - SPLIT_REQUIRED
  command: CMD-ER-CONFIRM-MATCH
  to: MATCHED
  guard: reviewer ≠ split requester; rationale
  event: EVT-ER-MATCH-CONFIRMED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - SPLIT_REQUIRED
  command: CMD-ER-SPLIT
  to: SPLIT
  guard: reviewer ≠ split requester; closes MATCH link (recorded_to = now); optional
    NOT_A_MATCH link; recomputes clusters in the same transaction
  event: EVT-ER-SPLIT
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - CANDIDATE
  - UNDER_REVIEW
  - POSSIBLE_DUPLICATE
  command: CMD-ER-WITHDRAW
  to: WITHDRAWN
  guard: reason (e.g. entity retired, duplicate case)
  event: EVT-ER-WITHDRAWN
  guard_error: REASON_REQUIRED
```

</details>
