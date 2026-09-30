---
id: AGG-COLLECTION-REQUIREMENT
type: aggregate
title: Collection Requirement
wave: W4
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-COL-001
  - REQ-COL-003
  state_machine: SM-COLLECTION-REQUIREMENT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-COLLECTION-REQUIREMENT — Collection Requirement

**الغرض:** حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية  
**السياق:** BC02 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-CRQ-01** — fulfilment is computed per viewer over the observations that viewer may see (visibility first) — no leakage of hidden collection
- **INV-CRQ-02** — every fulfilment link points to a VALIDATED observation (or a claim derived from one) with lineage (QAS-COL-001)
- **INV-CRQ-03** — expiry depends only on the due date
- **INV-CRQ-04** — approver ≠ requester

## مكونات داخلية

- EEI (id, entity_types, predicates, observation_methods, quantities)
- FulfilmentLink (eei, observation, matched_at)

## الحالات

- غير نهائية: DRAFT, SUBMITTED, APPROVED
- نهائية: REJECTED, SATISFIED, EXPIRED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-CRQ-DRAFT | DRAFT | question; requester; label | EVT-CRQ-DRAFTED | REQUIREMENT_INVALID |
| DRAFT | CMD-CRQ-EDIT | (بلا تغيير) | area polygon, window, priority 1–5, due, essential elements of information (EEIs) | EVT-CRQ-EDITED | REQUIREMENT_INVALID |
| DRAFT | CMD-CRQ-SUBMIT | SUBMITTED | area, window, priority and ≥ 1 EEI present (REQ-COL-001) | EVT-CRQ-SUBMITTED | REQUIREMENT_INCOMPLETE |
| SUBMITTED | CMD-CRQ-APPROVE | APPROVED | collection manager with authority in the area scope; approver ≠ requester | EVT-CRQ-APPROVED | SEGREGATION_OF_DUTIES |
| SUBMITTED | CMD-CRQ-REJECT | REJECTED | reason (duplicate, out of scope, infeasible) | EVT-CRQ-REJECTED | REASON_REQUIRED |
| APPROVED | CMD-CRQ-AMEND | (بلا تغيير) | approver; extend due, adjust area or EEIs; recorded as new version | EVT-CRQ-AMENDED | REQUIREMENT_INVALID |
| APPROVED | SYS:validated observation matched | (بلا تغيير) | matching engine links observation to EEIs (SPEC-COLLECTION §2); fulfilment recomputed | EVT-CRQ-FULFILMENT-UPDATED | — |
| APPROVED | CMD-CRQ-MARK-SATISFIED | SATISFIED | requester; fulfilment as seen by the requester is ANSWERED, or PARTIAL with explicit acceptance note | EVT-CRQ-SATISFIED | FULFILMENT_INSUFFICIENT |
| APPROVED | SYS:due passed | EXPIRED | scheduler; based on due date only (never on hidden fulfilment) | EVT-CRQ-EXPIRED | — |
| DRAFT, SUBMITTED, APPROVED | CMD-CRQ-CANCEL | CANCELLED | requester or approver; reason | EVT-CRQ-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-CRQ-DRAFT | CMD-CRQ-EDIT | CMD-CRQ-SUBMIT | CMD-CRQ-APPROVE | CMD-CRQ-REJECT | CMD-CRQ-AMEND | SYS:validated observation matched | CMD-CRQ-MARK-SATISFIED | SYS:due passed | CMD-CRQ-CANCEL |
|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — | — | — | — |
| DRAFT | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | → DRAFT | → SUBMITTED | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | → CANCELLED |
| SUBMITTED | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | → APPROVED | → REJECTED | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | → CANCELLED |
| APPROVED | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | → APPROVED | → APPROVED | → SATISFIED | → EXPIRED | → CANCELLED |
| REJECTED | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
| SATISFIED | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
| EXPIRED | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-14.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-COLLECTION-REQUIREMENT
bc: BC02
name: Collection Requirement
tier: T2
purpose: 'حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية'
states:
- DRAFT
- SUBMITTED
- APPROVED
- REJECTED
- SATISFIED
- EXPIRED
- CANCELLED
terminal:
- REJECTED
- SATISFIED
- EXPIRED
- CANCELLED
invariants:
- 'INV-CRQ-01: fulfilment is computed per viewer over the observations that viewer
  may see (visibility first) — no leakage of hidden collection'
- 'INV-CRQ-02: every fulfilment link points to a VALIDATED observation (or a claim
  derived from one) with lineage (QAS-COL-001)'
- 'INV-CRQ-03: expiry depends only on the due date'
- 'INV-CRQ-04: approver ≠ requester'
entities:
- EEI (id, entity_types, predicates, observation_methods, quantities)
- FulfilmentLink (eei, observation, matched_at)
requirements:
- REQ-COL-001
- REQ-COL-003
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-CRQ-DRAFT
  to: DRAFT
  guard: question; requester; label
  event: EVT-CRQ-DRAFTED
  guard_error: REQUIREMENT_INVALID
- from:
  - DRAFT
  command: CMD-CRQ-EDIT
  to: '='
  guard: area polygon, window, priority 1–5, due, essential elements of information
    (EEIs)
  event: EVT-CRQ-EDITED
  guard_error: REQUIREMENT_INVALID
- from:
  - DRAFT
  command: CMD-CRQ-SUBMIT
  to: SUBMITTED
  guard: area, window, priority and ≥ 1 EEI present (REQ-COL-001)
  event: EVT-CRQ-SUBMITTED
  guard_error: REQUIREMENT_INCOMPLETE
- from:
  - SUBMITTED
  command: CMD-CRQ-APPROVE
  to: APPROVED
  guard: collection manager with authority in the area scope; approver ≠ requester
  event: EVT-CRQ-APPROVED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - SUBMITTED
  command: CMD-CRQ-REJECT
  to: REJECTED
  guard: reason (duplicate, out of scope, infeasible)
  event: EVT-CRQ-REJECTED
  guard_error: REASON_REQUIRED
- from:
  - APPROVED
  command: CMD-CRQ-AMEND
  to: '='
  guard: approver; extend due, adjust area or EEIs; recorded as new version
  event: EVT-CRQ-AMENDED
  guard_error: REQUIREMENT_INVALID
- from:
  - APPROVED
  command: SYS:validated observation matched
  to: '='
  guard: matching engine links observation to EEIs (SPEC-COLLECTION §2); fulfilment
    recomputed
  event: EVT-CRQ-FULFILMENT-UPDATED
  guard_error: null
- from:
  - APPROVED
  command: CMD-CRQ-MARK-SATISFIED
  to: SATISFIED
  guard: requester; fulfilment as seen by the requester is ANSWERED, or PARTIAL with
    explicit acceptance note
  event: EVT-CRQ-SATISFIED
  guard_error: FULFILMENT_INSUFFICIENT
- from:
  - APPROVED
  command: SYS:due passed
  to: EXPIRED
  guard: scheduler; based on due date only (never on hidden fulfilment)
  event: EVT-CRQ-EXPIRED
  guard_error: null
- from:
  - DRAFT
  - SUBMITTED
  - APPROVED
  command: CMD-CRQ-CANCEL
  to: CANCELLED
  guard: requester or approver; reason
  event: EVT-CRQ-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
