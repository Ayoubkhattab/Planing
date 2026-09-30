---
id: AGG-IMPORT-BATCH
type: aggregate
title: Import Batch
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-INF-005
  - REQ-INF-006
  - REQ-INF-007
  - REQ-INF-008
  - REQ-INF-009
  state_machine: SM-IMPORT-BATCH
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-IMPORT-BATCH — Import Batch

**الغرض:** دفعة استيراد من محول أو ملف، مع حجر وlineage  
**السياق:** BC02 · **المستوى:** T2 · **بيانات شخصية:** لا

> Records match entities via AGG-EXTERNAL-ID; unmatched records create new entities and an ER candidate (SLC-04).

## الثوابت (Invariants)

- **INV-IMP-01** — re-submitting the same batch never duplicates records
- **INV-IMP-02** — no quarantined record appears in queries or projections
- **INV-IMP-03** — every applied record has lineage to batch + mapping version
- **INV-IMP-04** — imported values are claims citing the adapter's source (BRL-013)

## مكونات داخلية

- QuarantineRecord (raw, reason codes)

## الحالات

- غير نهائية: RECEIVED, PROCESSING, COMPLETED_WITH_QUARANTINE
- نهائية: COMPLETED, FAILED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-IMP-SUBMIT | RECEIVED | adapter ACTIVE (or authorized manual import); batch_key unique per adapter: same key + same content hash returns the existing batch; different hash → rejected | EVT-IMP-RECEIVED | BATCH_KEY_REUSED |
| RECEIVED | SYS:processing started | PROCESSING | worker lease acquired | EVT-IMP-PROCESSING-STARTED | — |
| PROCESSING | SYS:all records applied | COMPLETED | each record applied idempotently with lineage (adapter, batch, mapping version) | EVT-IMP-COMPLETED | — |
| PROCESSING | SYS:finished with invalid records | COMPLETED_WITH_QUARANTINE | invalid records quarantined with reason codes | EVT-IMP-COMPLETED-WITH-QUARANTINE | — |
| PROCESSING | SYS:unrecoverable error | FAILED | applied records remain; re-submit resumes idempotently | EVT-IMP-FAILED | — |
| COMPLETED_WITH_QUARANTINE | CMD-IMP-REPROCESS-QUARANTINE | PROCESSING | new mapping version or corrected records | EVT-IMP-REPROCESSING | — |
| COMPLETED_WITH_QUARANTINE | CMD-IMP-ACCEPT-QUARANTINE | COMPLETED | reason; quarantined records dropped, record kept | EVT-IMP-QUARANTINE-ACCEPTED | REASON_REQUIRED |
| RECEIVED | CMD-IMP-CANCEL | CANCELLED | reason | EVT-IMP-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-IMP-SUBMIT | SYS:processing started | SYS:all records applied | SYS:finished with invalid records | SYS:unrecoverable error | CMD-IMP-REPROCESS-QUARANTINE | CMD-IMP-ACCEPT-QUARANTINE | CMD-IMP-CANCEL |
|---|---|---|---|---|---|---|---|---|
| ∅ | → RECEIVED | — | — | — | — | — | — | — |
| RECEIVED | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | → PROCESSING | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | → CANCELLED |
| PROCESSING | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | → COMPLETED | → COMPLETED_WITH_QUARANTINE | → FAILED | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION |
| COMPLETED | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION |
| COMPLETED_WITH_QUARANTINE | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | → PROCESSING | → COMPLETED | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION |
| FAILED | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION | ✗ IMPORT_BATCH_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-02.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-IMPORT-BATCH
bc: BC02
name: Import Batch
tier: T2
purpose: دفعة استيراد من محول أو ملف، مع حجر وlineage
states:
- RECEIVED
- PROCESSING
- COMPLETED
- COMPLETED_WITH_QUARANTINE
- FAILED
- CANCELLED
terminal:
- COMPLETED
- FAILED
- CANCELLED
invariants:
- 'INV-IMP-01: re-submitting the same batch never duplicates records'
- 'INV-IMP-02: no quarantined record appears in queries or projections'
- 'INV-IMP-03: every applied record has lineage to batch + mapping version'
- 'INV-IMP-04: imported values are claims citing the adapter''s source (BRL-013)'
entities:
- QuarantineRecord (raw, reason codes)
requirements:
- REQ-INF-005
- REQ-INF-006
- REQ-INF-007
- REQ-INF-008
- REQ-INF-009
notes: Records match entities via AGG-EXTERNAL-ID; unmatched records create new entities
  and an ER candidate (SLC-04).
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-IMP-SUBMIT
  to: RECEIVED
  guard: 'adapter ACTIVE (or authorized manual import); batch_key unique per adapter:
    same key + same content hash returns the existing batch; different hash → rejected'
  event: EVT-IMP-RECEIVED
  guard_error: BATCH_KEY_REUSED
- from:
  - RECEIVED
  command: SYS:processing started
  to: PROCESSING
  guard: worker lease acquired
  event: EVT-IMP-PROCESSING-STARTED
  guard_error: null
- from:
  - PROCESSING
  command: SYS:all records applied
  to: COMPLETED
  guard: each record applied idempotently with lineage (adapter, batch, mapping version)
  event: EVT-IMP-COMPLETED
  guard_error: null
- from:
  - PROCESSING
  command: SYS:finished with invalid records
  to: COMPLETED_WITH_QUARANTINE
  guard: invalid records quarantined with reason codes
  event: EVT-IMP-COMPLETED-WITH-QUARANTINE
  guard_error: null
- from:
  - PROCESSING
  command: SYS:unrecoverable error
  to: FAILED
  guard: applied records remain; re-submit resumes idempotently
  event: EVT-IMP-FAILED
  guard_error: null
- from:
  - COMPLETED_WITH_QUARANTINE
  command: CMD-IMP-REPROCESS-QUARANTINE
  to: PROCESSING
  guard: new mapping version or corrected records
  event: EVT-IMP-REPROCESSING
  guard_error: null
- from:
  - COMPLETED_WITH_QUARANTINE
  command: CMD-IMP-ACCEPT-QUARANTINE
  to: COMPLETED
  guard: reason; quarantined records dropped, record kept
  event: EVT-IMP-QUARANTINE-ACCEPTED
  guard_error: REASON_REQUIRED
- from:
  - RECEIVED
  command: CMD-IMP-CANCEL
  to: CANCELLED
  guard: reason
  event: EVT-IMP-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
