---
id: AGG-CORRELATION-PROPOSAL
type: aggregate
title: Correlation Proposal
wave: W4
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T1
personal_data: false
traces:
  satisfies:
  - REQ-FUS-001
  - REQ-FUS-002
  state_machine: SM-CORRELATION-PROPOSAL
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-CORRELATION-PROPOSAL — Correlation Proposal

**الغرض:** اقتراح ربط ملاحظات/ادعاءات من مصادر متعددة في المكان والزمان  
**السياق:** BC02 · **المستوى:** T1 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-CRP-01** — a proposal never changes claims, observations or entities; acceptance acts only through owner commands (REQ-FUS-001)
- **INV-CRP-02** — fused results record every contributing source and its reliability at fusion time (REQ-FUS-002)
- **INV-CRP-03** — no automatic acceptance
- **INV-CRP-04** — independence: two inputs derived from the same source (or one from the other) count as one source for corroboration

## مكونات داخلية

- ProposalInput (urn, source, reliability, label)
- ScoreBreakdown

## الحالات

- غير نهائية: PROPOSED, UNDER_REVIEW
- نهائية: ACCEPTED, REJECTED, EXPIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:correlation rule score ≥ threshold | PROPOSED | inputs from ≥ 2 distinct sources; no identical non-terminal proposal; label = max(input labels) | EVT-CRP-PROPOSED | — |
| ∅ (إنشاء) | CMD-CRP-PROPOSE | PROPOSED | analyst; ≥ 2 visible inputs; kind; rationale | EVT-CRP-PROPOSED | CORRELATION_INVALID |
| PROPOSED | CMD-CRP-START-REVIEW | UNDER_REVIEW | reviewer cleared for every input label | EVT-CRP-REVIEW-STARTED | REVIEWER_NOT_CLEARED |
| UNDER_REVIEW | CMD-CRP-ACCEPT | ACCEPTED | effects through owner commands as the reviewer: same_event → Real-World Event + participation relationships + fused claims; co_location → relationship; same_entity → ER case (SLC-04); lineage lists every contributing source and its reliability | EVT-CRP-ACCEPTED | OWNER_REJECTED |
| UNDER_REVIEW, PROPOSED | CMD-CRP-REJECT | REJECTED | reason (feeds rule evaluation) | EVT-CRP-REJECTED | REASON_REQUIRED |
| PROPOSED | SYS:not reviewed within 30 days | EXPIRED | scheduler | EVT-CRP-EXPIRED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:correlation rule score ≥ threshold | CMD-CRP-PROPOSE | CMD-CRP-START-REVIEW | CMD-CRP-ACCEPT | CMD-CRP-REJECT | SYS:not reviewed within 30 days |
|---|---|---|---|---|---|---|
| ∅ | → PROPOSED | → PROPOSED | — | — | — | — |
| PROPOSED | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | → UNDER_REVIEW | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | → REJECTED | → EXPIRED |
| UNDER_REVIEW | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | → ACCEPTED | → REJECTED | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
| ACCEPTED | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
| REJECTED | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
| EXPIRED | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | ✗ CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |

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
id: AGG-CORRELATION-PROPOSAL
bc: BC02
name: Correlation Proposal
tier: T1
purpose: اقتراح ربط ملاحظات/ادعاءات من مصادر متعددة في المكان والزمان
states:
- PROPOSED
- UNDER_REVIEW
- ACCEPTED
- REJECTED
- EXPIRED
terminal:
- ACCEPTED
- REJECTED
- EXPIRED
invariants:
- 'INV-CRP-01: a proposal never changes claims, observations or entities; acceptance
  acts only through owner commands (REQ-FUS-001)'
- 'INV-CRP-02: fused results record every contributing source and its reliability
  at fusion time (REQ-FUS-002)'
- 'INV-CRP-03: no automatic acceptance'
- 'INV-CRP-04: independence: two inputs derived from the same source (or one from
  the other) count as one source for corroboration'
entities:
- ProposalInput (urn, source, reliability, label)
- ScoreBreakdown
requirements:
- REQ-FUS-001
- REQ-FUS-002
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: SYS:correlation rule score ≥ threshold
  to: PROPOSED
  guard: inputs from ≥ 2 distinct sources; no identical non-terminal proposal; label
    = max(input labels)
  event: EVT-CRP-PROPOSED
  guard_error: null
- from: ∅
  command: CMD-CRP-PROPOSE
  to: PROPOSED
  guard: analyst; ≥ 2 visible inputs; kind; rationale
  event: EVT-CRP-PROPOSED
  guard_error: CORRELATION_INVALID
- from:
  - PROPOSED
  command: CMD-CRP-START-REVIEW
  to: UNDER_REVIEW
  guard: reviewer cleared for every input label
  event: EVT-CRP-REVIEW-STARTED
  guard_error: REVIEWER_NOT_CLEARED
- from:
  - UNDER_REVIEW
  command: CMD-CRP-ACCEPT
  to: ACCEPTED
  guard: 'effects through owner commands as the reviewer: same_event → Real-World
    Event + participation relationships + fused claims; co_location → relationship;
    same_entity → ER case (SLC-04); lineage lists every contributing source and its
    reliability'
  event: EVT-CRP-ACCEPTED
  guard_error: OWNER_REJECTED
- from:
  - UNDER_REVIEW
  - PROPOSED
  command: CMD-CRP-REJECT
  to: REJECTED
  guard: reason (feeds rule evaluation)
  event: EVT-CRP-REJECTED
  guard_error: REASON_REQUIRED
- from:
  - PROPOSED
  command: SYS:not reviewed within 30 days
  to: EXPIRED
  guard: scheduler
  event: EVT-CRP-EXPIRED
  guard_error: null
```

</details>
