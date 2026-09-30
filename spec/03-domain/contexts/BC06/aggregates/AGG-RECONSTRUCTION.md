---
id: AGG-RECONSTRUCTION
type: aggregate
title: Historical Reconstruction
wave: W4
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC06
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-ARC-004
  state_machine: SM-RECONSTRUCTION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-RECONSTRUCTION — Historical Reconstruction

**الغرض:** إعادة بناء حالة نطاق كما كانت صحيحة في T وكما كانت معروفة في K  
**السياق:** BC06 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-REC-01** — every element of the report carries its reconstruction label (PRJ§103, CR-25)
- **INV-REC-02** — the report is reproducible: same scope, T and K give the same result
- **INV-REC-03** — the report never exceeds the requester's authorization; hidden elements are absent, not marked

## مكونات داخلية

- ReconstructionElement (urn, value, label, rule?)

## الحالات

- غير نهائية: REQUESTED, RUNNING
- نهائية: COMPLETED, FAILED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-REC-REQUEST | REQUESTED | scope (objects, situation, plan, decision basis); valid_at T; known_at K ≤ now; purpose (audit, legal, lessons); requester authorized | EVT-REC-REQUESTED | RECONSTRUCTION_INVALID |
| REQUESTED | SYS:worker started | RUNNING | runs with the requester's authority | EVT-REC-STARTED | — |
| RUNNING | SYS:completed | COMPLETED | report: every element labelled RECORDED / RECONSTRUCTED / INFERRED (with rule) / UNKNOWN; archive retrievals included where needed | EVT-REC-COMPLETED | — |
| RUNNING | SYS:failed | FAILED | error recorded | EVT-REC-FAILED | — |
| REQUESTED, RUNNING | CMD-REC-CANCEL | CANCELLED | requester; reason | EVT-REC-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-REC-REQUEST | SYS:worker started | SYS:completed | SYS:failed | CMD-REC-CANCEL |
|---|---|---|---|---|---|
| ∅ | → REQUESTED | — | — | — | — |
| REQUESTED | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | → RUNNING | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | → CANCELLED |
| RUNNING | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | → COMPLETED | → FAILED | → CANCELLED |
| COMPLETED | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION |
| FAILED | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION | ✗ RECONSTRUCTION_INVALID_STATE_TRANSITION |

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
id: AGG-RECONSTRUCTION
bc: BC06
name: Historical Reconstruction
tier: T2
purpose: إعادة بناء حالة نطاق كما كانت صحيحة في T وكما كانت معروفة في K
states:
- REQUESTED
- RUNNING
- COMPLETED
- FAILED
- CANCELLED
terminal:
- COMPLETED
- FAILED
- CANCELLED
invariants:
- 'INV-REC-01: every element of the report carries its reconstruction label (PRJ§103,
  CR-25)'
- 'INV-REC-02: the report is reproducible: same scope, T and K give the same result'
- 'INV-REC-03: the report never exceeds the requester''s authorization; hidden elements
  are absent, not marked'
entities:
- ReconstructionElement (urn, value, label, rule?)
requirements:
- REQ-ARC-004
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-REC-REQUEST
  to: REQUESTED
  guard: scope (objects, situation, plan, decision basis); valid_at T; known_at K
    ≤ now; purpose (audit, legal, lessons); requester authorized
  event: EVT-REC-REQUESTED
  guard_error: RECONSTRUCTION_INVALID
- from:
  - REQUESTED
  command: SYS:worker started
  to: RUNNING
  guard: runs with the requester's authority
  event: EVT-REC-STARTED
  guard_error: null
- from:
  - RUNNING
  command: SYS:completed
  to: COMPLETED
  guard: 'report: every element labelled RECORDED / RECONSTRUCTED / INFERRED (with
    rule) / UNKNOWN; archive retrievals included where needed'
  event: EVT-REC-COMPLETED
  guard_error: null
- from:
  - RUNNING
  command: SYS:failed
  to: FAILED
  guard: error recorded
  event: EVT-REC-FAILED
  guard_error: null
- from:
  - REQUESTED
  - RUNNING
  command: CMD-REC-CANCEL
  to: CANCELLED
  guard: requester; reason
  event: EVT-REC-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
