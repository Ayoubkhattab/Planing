---
id: AGG-CONFLICT
type: aggregate
title: Conflict
wave: W4
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T2 (bitemporal resolution records)
personal_data: false
traces:
  satisfies:
  - REQ-INF-025
  - REQ-INF-024
  state_machine: SM-CONFLICT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-CONFLICT — Conflict

**الغرض:** تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة  
**السياق:** BC02 · **المستوى:** T2 (bitemporal resolution records) · **بيانات شخصية:** لا

> Detection runs on EVT-CLM-ASSERTED/CORRECTED/CHANGED and on identity-cluster changes (a merge can reveal conflicts between members' claims).

## الثوابت (Invariants)

- **INV-CNF-01** — a conflict never modifies, closes or re-labels any claim
- **INV-CNF-02** — at most one non-terminal conflict per (tenant, identity cluster, predicate, overlapping valid window)
- **INV-CNF-03** — resolutions are bitemporal records: resolve(T, K) uses the resolution known at K
- **INV-CNF-04** — label = max(member claim labels); a reader sees the conflict only if the reader sees ≥ 2 incompatible member claims (A21)
- **INV-CNF-05** — the preferred claim of a RESOLVED conflict is CURRENT; if it closes, the conflict is re-evaluated (SUPERSEDED or back to OPEN via detection)

## مكونات داخلية

- ResolutionRecord (preferred_claim, rationale, decided_by, recorded_from, recorded_to)
- MemberClaim (claim_ref, joined_at)

## الحالات

- غير نهائية: OPEN, UNDER_REVIEW, RESOLVED, ACCEPTED_AS_CONFLICT
- نهائية: SUPERSEDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:conflict rule matched | OPEN | rule CF-01..CF-04 on claims of the same identity cluster, same predicate, overlapping valid; no non-terminal conflict with the same (cluster, predicate, window) — otherwise the claim joins it | EVT-CNF-DETECTED | — |
| ∅ (إنشاء) | CMD-CNF-RAISE | OPEN | analyst names ≥ 2 visible CURRENT claims on the same cluster and predicate with overlapping valid time | EVT-CNF-RAISED | CONFLICT_INVALID |
| OPEN, UNDER_REVIEW | SYS:incompatible claim joined | (بلا تغيير) | new CURRENT claim incompatible with members (same key, overlapping window) | EVT-CNF-CLAIM-ADDED | — |
| OPEN, UNDER_REVIEW | CMD-CNF-ASSIGN | (بلا تغيير) | reviewer cleared for every member claim label | EVT-CNF-ASSIGNED | REVIEWER_NOT_CLEARED |
| OPEN | CMD-CNF-START-REVIEW | UNDER_REVIEW | actor = assigned reviewer (or Analyst lead) | EVT-CNF-REVIEW-STARTED | NOT_ASSIGNED_REVIEWER |
| UNDER_REVIEW | CMD-CNF-RESOLVE | RESOLVED | preferred claim ∈ CURRENT members; rationale; reviewer ≠ asserter of the preferred claim (SoD, default on); records resolution with recorded_from = now | EVT-CNF-RESOLVED | SEGREGATION_OF_DUTIES |
| UNDER_REVIEW | CMD-CNF-ACCEPT | ACCEPTED_AS_CONFLICT | rationale (both accounts shown to users) | EVT-CNF-ACCEPTED | REASON_REQUIRED |
| RESOLVED, ACCEPTED_AS_CONFLICT | CMD-CNF-REOPEN | UNDER_REVIEW | new evidence or reason; closes current resolution record (recorded_to = now) | EVT-CNF-REOPENED | REASON_REQUIRED |
| OPEN, UNDER_REVIEW, RESOLVED, ACCEPTED_AS_CONFLICT | SYS:member set no longer conflicting | SUPERSEDED | fewer than 2 incompatible CURRENT members (claims closed, split, or corrected) | EVT-CNF-SUPERSEDED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:conflict rule matched | CMD-CNF-RAISE | SYS:incompatible claim joined | CMD-CNF-ASSIGN | CMD-CNF-START-REVIEW | CMD-CNF-RESOLVE | CMD-CNF-ACCEPT | CMD-CNF-REOPEN | SYS:member set no longer conflicting |
|---|---|---|---|---|---|---|---|---|---|
| ∅ | → OPEN | → OPEN | — | — | — | — | — | — | — |
| OPEN | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | → OPEN | → OPEN | → UNDER_REVIEW | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | → SUPERSEDED |
| UNDER_REVIEW | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | → UNDER_REVIEW | → UNDER_REVIEW | ✗ CONFLICT_INVALID_STATE_TRANSITION | → RESOLVED | → ACCEPTED_AS_CONFLICT | ✗ CONFLICT_INVALID_STATE_TRANSITION | → SUPERSEDED |
| RESOLVED | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | → UNDER_REVIEW | → SUPERSEDED |
| ACCEPTED_AS_CONFLICT | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | → UNDER_REVIEW | → SUPERSEDED |
| SUPERSEDED | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION | ✗ CONFLICT_INVALID_STATE_TRANSITION |

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
id: AGG-CONFLICT
bc: BC02
name: Conflict
tier: T2 (bitemporal resolution records)
purpose: تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة
states:
- OPEN
- UNDER_REVIEW
- RESOLVED
- ACCEPTED_AS_CONFLICT
- SUPERSEDED
terminal:
- SUPERSEDED
invariants:
- 'INV-CNF-01: a conflict never modifies, closes or re-labels any claim'
- 'INV-CNF-02: at most one non-terminal conflict per (tenant, identity cluster, predicate,
  overlapping valid window)'
- 'INV-CNF-03: resolutions are bitemporal records: resolve(T, K) uses the resolution
  known at K'
- 'INV-CNF-04: label = max(member claim labels); a reader sees the conflict only if
  the reader sees ≥ 2 incompatible member claims (A21)'
- 'INV-CNF-05: the preferred claim of a RESOLVED conflict is CURRENT; if it closes,
  the conflict is re-evaluated (SUPERSEDED or back to OPEN via detection)'
entities:
- ResolutionRecord (preferred_claim, rationale, decided_by, recorded_from, recorded_to)
- MemberClaim (claim_ref, joined_at)
requirements:
- REQ-INF-025
- REQ-INF-024
notes: Detection runs on EVT-CLM-ASSERTED/CORRECTED/CHANGED and on identity-cluster
  changes (a merge can reveal conflicts between members' claims).
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: SYS:conflict rule matched
  to: OPEN
  guard: rule CF-01..CF-04 on claims of the same identity cluster, same predicate,
    overlapping valid; no non-terminal conflict with the same (cluster, predicate,
    window) — otherwise the claim joins it
  event: EVT-CNF-DETECTED
  guard_error: null
- from: ∅
  command: CMD-CNF-RAISE
  to: OPEN
  guard: analyst names ≥ 2 visible CURRENT claims on the same cluster and predicate
    with overlapping valid time
  event: EVT-CNF-RAISED
  guard_error: CONFLICT_INVALID
- from:
  - OPEN
  - UNDER_REVIEW
  command: SYS:incompatible claim joined
  to: '='
  guard: new CURRENT claim incompatible with members (same key, overlapping window)
  event: EVT-CNF-CLAIM-ADDED
  guard_error: null
- from:
  - OPEN
  - UNDER_REVIEW
  command: CMD-CNF-ASSIGN
  to: '='
  guard: reviewer cleared for every member claim label
  event: EVT-CNF-ASSIGNED
  guard_error: REVIEWER_NOT_CLEARED
- from:
  - OPEN
  command: CMD-CNF-START-REVIEW
  to: UNDER_REVIEW
  guard: actor = assigned reviewer (or Analyst lead)
  event: EVT-CNF-REVIEW-STARTED
  guard_error: NOT_ASSIGNED_REVIEWER
- from:
  - UNDER_REVIEW
  command: CMD-CNF-RESOLVE
  to: RESOLVED
  guard: preferred claim ∈ CURRENT members; rationale; reviewer ≠ asserter of the
    preferred claim (SoD, default on); records resolution with recorded_from = now
  event: EVT-CNF-RESOLVED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - UNDER_REVIEW
  command: CMD-CNF-ACCEPT
  to: ACCEPTED_AS_CONFLICT
  guard: rationale (both accounts shown to users)
  event: EVT-CNF-ACCEPTED
  guard_error: REASON_REQUIRED
- from:
  - RESOLVED
  - ACCEPTED_AS_CONFLICT
  command: CMD-CNF-REOPEN
  to: UNDER_REVIEW
  guard: new evidence or reason; closes current resolution record (recorded_to = now)
  event: EVT-CNF-REOPENED
  guard_error: REASON_REQUIRED
- from:
  - OPEN
  - UNDER_REVIEW
  - RESOLVED
  - ACCEPTED_AS_CONFLICT
  command: SYS:member set no longer conflicting
  to: SUPERSEDED
  guard: fewer than 2 incompatible CURRENT members (claims closed, split, or corrected)
  event: EVT-CNF-SUPERSEDED
  guard_error: null
```

</details>
