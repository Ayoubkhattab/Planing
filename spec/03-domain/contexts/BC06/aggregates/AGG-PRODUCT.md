---
id: AGG-PRODUCT
type: aggregate
title: Product Version
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
  - REQ-PRD-001
  - REQ-PRD-002
  - REQ-PRD-003
  state_machine: SM-PRODUCT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-PRODUCT — Product Version

**الغرض:** منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد  
**السياق:** BC06 · **المستوى:** T1 content / T2 lifecycle · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-PRD-01** — an APPROVED version is immutable; changes are new versions (REQ-PRD-003)
- **INV-PRD-02** — product label ≥ every included content label; content above the label is excluded, and exclusions are not counted in the product (REQ-PRD-002, A21)
- **INV-PRD-03** — data is pinned at generation (known_at), so the product reproduces exactly what was generated
- **INV-PRD-04** — approver ≠ author

## مكونات داخلية

- RenderedArtifact (format, hash)
- Citation (pinned)
- ExclusionRecord (internal, audit only)

## الحالات

- غير نهائية: DRAFT, GENERATING, GENERATED, GENERATION_FAILED, IN_REVIEW, APPROVED
- نهائية: SUPERSEDED, WITHDRAWN, DISCARDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-PRD-CREATE | DRAFT | template ACTIVE (version pinned); parameters valid; audience (org units/roles); target label ≥ labels of scope objects referenced in parameters; optional revises = APPROVED version | EVT-PRD-CREATED | PRODUCT_INVALID |
| DRAFT, GENERATED, GENERATION_FAILED | CMD-PRD-GENERATE | GENERATING | author; async job with the author's authority | EVT-PRD-GENERATION-STARTED | — |
| GENERATING | SYS:generation succeeded | GENERATED | every binding executed as known_at = generation time; content items with label > product label excluded; rendered artifacts hashed | EVT-PRD-GENERATED | — |
| GENERATING | SYS:generation failed | GENERATION_FAILED | error recorded | EVT-PRD-GENERATION-FAILED | — |
| GENERATED | CMD-PRD-EDIT-NARRATIVE | (بلا تغيير) | only narrative sections; data sections change only by regeneration | EVT-PRD-NARRATIVE-EDITED | SECTION_NOT_EDITABLE |
| GENERATED | CMD-PRD-SUBMIT | IN_REVIEW | all required sections present; AI-drafted sections reviewed (REQ-AI-005) | EVT-PRD-SUBMITTED | PRODUCT_INCOMPLETE |
| IN_REVIEW | CMD-PRD-RETURN | GENERATED | reviewer; reason | EVT-PRD-RETURNED | REASON_REQUIRED |
| IN_REVIEW | CMD-PRD-APPROVE | APPROVED | reviewer ≠ author; content frozen with pinned citations; previous APPROVED version of the same product → SUPERSEDED | EVT-PRD-APPROVED | SEGREGATION_OF_DUTIES |
| APPROVED | SYS:newer version approved | SUPERSEDED | system | EVT-PRD-SUPERSEDED | — |
| APPROVED | CMD-PRD-WITHDRAW | WITHDRAWN | reason; recipients notified | EVT-PRD-WITHDRAWN | REASON_REQUIRED |
| DRAFT, GENERATED, GENERATION_FAILED | CMD-PRD-DISCARD | DISCARDED | author; reason | EVT-PRD-DISCARDED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-PRD-CREATE | CMD-PRD-GENERATE | SYS:generation succeeded | SYS:generation failed | CMD-PRD-EDIT-NARRATIVE | CMD-PRD-SUBMIT | CMD-PRD-RETURN | CMD-PRD-APPROVE | SYS:newer version approved | CMD-PRD-WITHDRAW | CMD-PRD-DISCARD |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — | — | — | — | — |
| DRAFT | ✗ PRODUCT_INVALID_STATE_TRANSITION | → GENERATING | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | → DISCARDED |
| GENERATING | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | → GENERATED | → GENERATION_FAILED | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION |
| GENERATED | ✗ PRODUCT_INVALID_STATE_TRANSITION | → GENERATING | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | → GENERATED | → IN_REVIEW | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | → DISCARDED |
| GENERATION_FAILED | ✗ PRODUCT_INVALID_STATE_TRANSITION | → GENERATING | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | → DISCARDED |
| IN_REVIEW | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | → GENERATED | → APPROVED | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION |
| APPROVED | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | → SUPERSEDED | → WITHDRAWN | ✗ PRODUCT_INVALID_STATE_TRANSITION |
| SUPERSEDED | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION |
| WITHDRAWN | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION |
| DISCARDED | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION | ✗ PRODUCT_INVALID_STATE_TRANSITION |

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
id: AGG-PRODUCT
bc: BC06
name: Product Version
tier: T1 content / T2 lifecycle
purpose: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد
states:
- DRAFT
- GENERATING
- GENERATED
- GENERATION_FAILED
- IN_REVIEW
- APPROVED
- SUPERSEDED
- WITHDRAWN
- DISCARDED
terminal:
- SUPERSEDED
- WITHDRAWN
- DISCARDED
invariants:
- 'INV-PRD-01: an APPROVED version is immutable; changes are new versions (REQ-PRD-003)'
- 'INV-PRD-02: product label ≥ every included content label; content above the label
  is excluded, and exclusions are not counted in the product (REQ-PRD-002, A21)'
- 'INV-PRD-03: data is pinned at generation (known_at), so the product reproduces
  exactly what was generated'
- 'INV-PRD-04: approver ≠ author'
entities:
- RenderedArtifact (format, hash)
- Citation (pinned)
- ExclusionRecord (internal, audit only)
requirements:
- REQ-PRD-001
- REQ-PRD-002
- REQ-PRD-003
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-PRD-CREATE
  to: DRAFT
  guard: template ACTIVE (version pinned); parameters valid; audience (org units/roles);
    target label ≥ labels of scope objects referenced in parameters; optional revises
    = APPROVED version
  event: EVT-PRD-CREATED
  guard_error: PRODUCT_INVALID
- from:
  - DRAFT
  - GENERATED
  - GENERATION_FAILED
  command: CMD-PRD-GENERATE
  to: GENERATING
  guard: author; async job with the author's authority
  event: EVT-PRD-GENERATION-STARTED
  guard_error: null
- from:
  - GENERATING
  command: SYS:generation succeeded
  to: GENERATED
  guard: every binding executed as known_at = generation time; content items with
    label > product label excluded; rendered artifacts hashed
  event: EVT-PRD-GENERATED
  guard_error: null
- from:
  - GENERATING
  command: SYS:generation failed
  to: GENERATION_FAILED
  guard: error recorded
  event: EVT-PRD-GENERATION-FAILED
  guard_error: null
- from:
  - GENERATED
  command: CMD-PRD-EDIT-NARRATIVE
  to: '='
  guard: only narrative sections; data sections change only by regeneration
  event: EVT-PRD-NARRATIVE-EDITED
  guard_error: SECTION_NOT_EDITABLE
- from:
  - GENERATED
  command: CMD-PRD-SUBMIT
  to: IN_REVIEW
  guard: all required sections present; AI-drafted sections reviewed (REQ-AI-005)
  event: EVT-PRD-SUBMITTED
  guard_error: PRODUCT_INCOMPLETE
- from:
  - IN_REVIEW
  command: CMD-PRD-RETURN
  to: GENERATED
  guard: reviewer; reason
  event: EVT-PRD-RETURNED
  guard_error: REASON_REQUIRED
- from:
  - IN_REVIEW
  command: CMD-PRD-APPROVE
  to: APPROVED
  guard: reviewer ≠ author; content frozen with pinned citations; previous APPROVED
    version of the same product → SUPERSEDED
  event: EVT-PRD-APPROVED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - APPROVED
  command: SYS:newer version approved
  to: SUPERSEDED
  guard: system
  event: EVT-PRD-SUPERSEDED
  guard_error: null
- from:
  - APPROVED
  command: CMD-PRD-WITHDRAW
  to: WITHDRAWN
  guard: reason; recipients notified
  event: EVT-PRD-WITHDRAWN
  guard_error: REASON_REQUIRED
- from:
  - DRAFT
  - GENERATED
  - GENERATION_FAILED
  command: CMD-PRD-DISCARD
  to: DISCARDED
  guard: author; reason
  event: EVT-PRD-DISCARDED
  guard_error: REASON_REQUIRED
```

</details>
