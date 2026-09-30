---
id: AGG-ARCHIVE-PACKAGE
type: aggregate
title: Archive Package (AIP)
wave: W4
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC06
importance_tier: T1
personal_data: false
traces:
  satisfies:
  - REQ-ARC-001
  - REQ-ARC-002
  - REQ-ARC-003
  state_machine: SM-ARCHIVE-PACKAGE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ARCHIVE-PACKAGE — Archive Package (AIP)

**الغرض:** حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول  
**السياق:** BC06 · **المستوى:** T1 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-ARC-01** — originals are never overwritten; format migration adds representations
- **INV-ARC-02** — every retrieval appends to the package's access history (REQ-ARC-003) and is audited
- **INV-ARC-03** — fixity verified at ingest, on every retrieval and at least yearly (REQ-ARC-002)
- **INV-ARC-04** — archive ≠ backup (BRL-011): packages are institutional records with their own retention

## مكونات داخلية

- BagManifest
- PreservationEvent
- Representation
- AccessEntry

## الحالات

- غير نهائية: INGESTING, INGEST_FAILED, ARCHIVED, INTEGRITY_FAILED
- نهائية: TRANSFERRED, DISPOSED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:disposition action ARCHIVE for a bucket or record set | INGESTING | SIP assembled from owner exports: content, metadata, provenance, access history | EVT-ARC-INGEST-STARTED | — |
| INGESTING | SYS:package validated | ARCHIVED | BagIt structure valid; every file fixity (SHA-256) recorded; preservation formats (R2-Q6) produced alongside originals | EVT-ARC-ARCHIVED | — |
| INGESTING | SYS:validation failed | INGEST_FAILED | errors recorded | EVT-ARC-INGEST-FAILED | — |
| INGEST_FAILED | CMD-ARC-RETRY-INGEST | INGESTING | archivist; corrective note | EVT-ARC-INGEST-STARTED | REASON_REQUIRED |
| ARCHIVED | SYS:integrity check failed | INTEGRITY_FAILED | fixity mismatch on any file | EVT-ARC-INTEGRITY-FAILED | — |
| INTEGRITY_FAILED | CMD-ARC-REPAIR | ARCHIVED | restored from replica; fixity re-verified | EVT-ARC-REPAIRED | FIXITY_MISMATCH |
| ARCHIVED | CMD-ARC-MIGRATE-FORMAT | (بلا تغيير) | new preservation representation added; originals kept; preservation event recorded | EVT-ARC-FORMAT-MIGRATED | FORMAT_INVALID |
| ARCHIVED | CMD-ARC-TRANSFER | TRANSFERRED | transfer authority decision; receipt from the receiving archive | EVT-ARC-TRANSFERRED | AUTHORITY_REQUIRED |
| ARCHIVED, INTEGRITY_FAILED | SYS:disposition DESTROY executed for the package bucket | DISPOSED | SLC-12a key destruction; no active hold | EVT-ARC-DISPOSED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:disposition action ARCHIVE for a bucket or record set | SYS:package validated | SYS:validation failed | CMD-ARC-RETRY-INGEST | SYS:integrity check failed | CMD-ARC-REPAIR | CMD-ARC-MIGRATE-FORMAT | CMD-ARC-TRANSFER | SYS:disposition DESTROY executed for the package bucket |
|---|---|---|---|---|---|---|---|---|---|
| ∅ | → INGESTING | — | — | — | — | — | — | — | — |
| INGESTING | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | → ARCHIVED | → INGEST_FAILED | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
| INGEST_FAILED | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | → INGESTING | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
| ARCHIVED | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | → INTEGRITY_FAILED | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | → ARCHIVED | → TRANSFERRED | → DISPOSED |
| INTEGRITY_FAILED | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | → ARCHIVED | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | → DISPOSED |
| TRANSFERRED | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
| DISPOSED | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | ✗ ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |

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
id: AGG-ARCHIVE-PACKAGE
bc: BC06
name: Archive Package (AIP)
tier: T1
purpose: 'حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول'
states:
- INGESTING
- INGEST_FAILED
- ARCHIVED
- INTEGRITY_FAILED
- TRANSFERRED
- DISPOSED
terminal:
- TRANSFERRED
- DISPOSED
invariants:
- 'INV-ARC-01: originals are never overwritten; format migration adds representations'
- 'INV-ARC-02: every retrieval appends to the package''s access history (REQ-ARC-003)
  and is audited'
- 'INV-ARC-03: fixity verified at ingest, on every retrieval and at least yearly (REQ-ARC-002)'
- 'INV-ARC-04: archive ≠ backup (BRL-011): packages are institutional records with
  their own retention'
entities:
- BagManifest
- PreservationEvent
- Representation
- AccessEntry
requirements:
- REQ-ARC-001
- REQ-ARC-002
- REQ-ARC-003
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: SYS:disposition action ARCHIVE for a bucket or record set
  to: INGESTING
  guard: 'SIP assembled from owner exports: content, metadata, provenance, access
    history'
  event: EVT-ARC-INGEST-STARTED
  guard_error: null
- from:
  - INGESTING
  command: SYS:package validated
  to: ARCHIVED
  guard: BagIt structure valid; every file fixity (SHA-256) recorded; preservation
    formats (R2-Q6) produced alongside originals
  event: EVT-ARC-ARCHIVED
  guard_error: null
- from:
  - INGESTING
  command: SYS:validation failed
  to: INGEST_FAILED
  guard: errors recorded
  event: EVT-ARC-INGEST-FAILED
  guard_error: null
- from:
  - INGEST_FAILED
  command: CMD-ARC-RETRY-INGEST
  to: INGESTING
  guard: archivist; corrective note
  event: EVT-ARC-INGEST-STARTED
  guard_error: REASON_REQUIRED
- from:
  - ARCHIVED
  command: SYS:integrity check failed
  to: INTEGRITY_FAILED
  guard: fixity mismatch on any file
  event: EVT-ARC-INTEGRITY-FAILED
  guard_error: null
- from:
  - INTEGRITY_FAILED
  command: CMD-ARC-REPAIR
  to: ARCHIVED
  guard: restored from replica; fixity re-verified
  event: EVT-ARC-REPAIRED
  guard_error: FIXITY_MISMATCH
- from:
  - ARCHIVED
  command: CMD-ARC-MIGRATE-FORMAT
  to: '='
  guard: new preservation representation added; originals kept; preservation event
    recorded
  event: EVT-ARC-FORMAT-MIGRATED
  guard_error: FORMAT_INVALID
- from:
  - ARCHIVED
  command: CMD-ARC-TRANSFER
  to: TRANSFERRED
  guard: transfer authority decision; receipt from the receiving archive
  event: EVT-ARC-TRANSFERRED
  guard_error: AUTHORITY_REQUIRED
- from:
  - ARCHIVED
  - INTEGRITY_FAILED
  command: SYS:disposition DESTROY executed for the package bucket
  to: DISPOSED
  guard: SLC-12a key destruction; no active hold
  event: EVT-ARC-DISPOSED
  guard_error: null
```

</details>
