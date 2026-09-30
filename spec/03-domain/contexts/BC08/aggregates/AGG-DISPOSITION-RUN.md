---
id: AGG-DISPOSITION-RUN
type: aggregate
title: Disposition Run
wave: W4
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC08
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-GOV-006
  - REQ-GOV-007
  state_machine: SM-DISPOSITION-RUN
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-DISPOSITION-RUN — Disposition Run

**الغرض:** دورة إتلاف: ترشيح، اعتماد، تنفيذ عبر إتلاف مفاتيح الحاويات، شهادة  
**السياق:** BC08 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-DSP-01** — destruction is by key (crypto-shredding of time-bucketed class keys), reaching operational stores, projections, archives and backups (ADR-P08, CR-51)
- **INV-DSP-02** — no bucket key is destroyed while any record in it is under hold — held records are re-wrapped first
- **INV-DSP-03** — each destruction is recorded in the append-only key-destruction log used by the restore gate
- **INV-DSP-04** — tombstones keep non-personal facts (class, bucket, count, run, date); audit records are governed by their own class rule

## مكونات داخلية

- BucketCandidate
- DispositionCertificate

## الحالات

- غير نهائية: PLANNED, AWAITING_APPROVAL, APPROVED, EXECUTING
- نهائية: COMPLETED, COMPLETED_WITH_EXCEPTIONS, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:scheduled evaluation (daily) | PLANNED | candidates = key buckets whose records are all past retention under the ACTIVE schedule; held items identified via HoldCheck | EVT-DSP-PLANNED | — |
| PLANNED | CMD-DSP-SUBMIT | AWAITING_APPROVAL | Archivist reviewed candidate summary (counts per class/bucket, REVIEW-action items listed) | EVT-DSP-SUBMITTED | — |
| AWAITING_APPROVAL | CMD-DSP-APPROVE | APPROVED | approver = Records/Legal authority ≠ submitter; re-run HoldCheck at approval | EVT-DSP-APPROVED | SEGREGATION_OF_DUTIES |
| APPROVED | SYS:execution started | EXECUTING | held items in each bucket re-wrapped under hold keys first; then bucket keys destroyed; owners notified to purge plaintext caches and projections; tombstones written | EVT-DSP-EXECUTING | — |
| EXECUTING | SYS:all buckets processed | COMPLETED | certificate issued (buckets, key ids destroyed, counts, holds excluded) | EVT-DSP-COMPLETED | — |
| EXECUTING | SYS:some buckets failed | COMPLETED_WITH_EXCEPTIONS | failed buckets listed; retried next run | EVT-DSP-COMPLETED-WITH-EXCEPTIONS | — |
| PLANNED, AWAITING_APPROVAL, APPROVED | CMD-DSP-CANCEL | CANCELLED | reason | EVT-DSP-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:scheduled evaluation (daily) | CMD-DSP-SUBMIT | CMD-DSP-APPROVE | SYS:execution started | SYS:all buckets processed | SYS:some buckets failed | CMD-DSP-CANCEL |
|---|---|---|---|---|---|---|---|
| ∅ | → PLANNED | — | — | — | — | — | — |
| PLANNED | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | → AWAITING_APPROVAL | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | → CANCELLED |
| AWAITING_APPROVAL | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | → APPROVED | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | → CANCELLED |
| APPROVED | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | → EXECUTING | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | → CANCELLED |
| EXECUTING | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | → COMPLETED | → COMPLETED_WITH_EXCEPTIONS | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION |
| COMPLETED | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION |
| COMPLETED_WITH_EXCEPTIONS | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION | ✗ DISPOSITION_RUN_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-12a.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-DISPOSITION-RUN
bc: BC08
name: Disposition Run
tier: T2
purpose: 'دورة إتلاف: ترشيح، اعتماد، تنفيذ عبر إتلاف مفاتيح الحاويات، شهادة'
states:
- PLANNED
- AWAITING_APPROVAL
- APPROVED
- EXECUTING
- COMPLETED
- COMPLETED_WITH_EXCEPTIONS
- CANCELLED
terminal:
- COMPLETED
- COMPLETED_WITH_EXCEPTIONS
- CANCELLED
invariants:
- 'INV-DSP-01: destruction is by key (crypto-shredding of time-bucketed class keys),
  reaching operational stores, projections, archives and backups (ADR-P08, CR-51)'
- 'INV-DSP-02: no bucket key is destroyed while any record in it is under hold — held
  records are re-wrapped first'
- 'INV-DSP-03: each destruction is recorded in the append-only key-destruction log
  used by the restore gate'
- 'INV-DSP-04: tombstones keep non-personal facts (class, bucket, count, run, date);
  audit records are governed by their own class rule'
entities:
- BucketCandidate
- DispositionCertificate
requirements:
- REQ-GOV-006
- REQ-GOV-007
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: SYS:scheduled evaluation (daily)
  to: PLANNED
  guard: candidates = key buckets whose records are all past retention under the ACTIVE
    schedule; held items identified via HoldCheck
  event: EVT-DSP-PLANNED
  guard_error: null
- from:
  - PLANNED
  command: CMD-DSP-SUBMIT
  to: AWAITING_APPROVAL
  guard: Archivist reviewed candidate summary (counts per class/bucket, REVIEW-action
    items listed)
  event: EVT-DSP-SUBMITTED
  guard_error: null
- from:
  - AWAITING_APPROVAL
  command: CMD-DSP-APPROVE
  to: APPROVED
  guard: approver = Records/Legal authority ≠ submitter; re-run HoldCheck at approval
  event: EVT-DSP-APPROVED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - APPROVED
  command: SYS:execution started
  to: EXECUTING
  guard: held items in each bucket re-wrapped under hold keys first; then bucket keys
    destroyed; owners notified to purge plaintext caches and projections; tombstones
    written
  event: EVT-DSP-EXECUTING
  guard_error: null
- from:
  - EXECUTING
  command: SYS:all buckets processed
  to: COMPLETED
  guard: certificate issued (buckets, key ids destroyed, counts, holds excluded)
  event: EVT-DSP-COMPLETED
  guard_error: null
- from:
  - EXECUTING
  command: SYS:some buckets failed
  to: COMPLETED_WITH_EXCEPTIONS
  guard: failed buckets listed; retried next run
  event: EVT-DSP-COMPLETED-WITH-EXCEPTIONS
  guard_error: null
- from:
  - PLANNED
  - AWAITING_APPROVAL
  - APPROVED
  command: CMD-DSP-CANCEL
  to: CANCELLED
  guard: reason
  event: EVT-DSP-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
