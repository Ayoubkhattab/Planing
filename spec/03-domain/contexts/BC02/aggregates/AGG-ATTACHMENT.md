---
id: AGG-ATTACHMENT
type: aggregate
title: Attachment
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T1 metadata
personal_data: false
traces:
  satisfies:
  - REQ-INF-003
  - REQ-INF-004
  - REQ-GOV-008
  state_machine: SM-ATTACHMENT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ATTACHMENT — Attachment

**الغرض:** ملف في Object Storage، معنون بالمحتوى، يُرفع ويُنزّل مباشرة  
**السياق:** BC02 · **المستوى:** T1 metadata · **بيانات شخصية:** لا

> Direct-to-storage transfer removes the application tier from the bandwidth path (SR-05).

## الثوابت (Invariants)

- **INV-ATT-01** — (tenant, sha256) unique among non-terminal attachments
- **INV-ATT-02** — bytes never pass through application servers (direct transfer, signed targets ≤ 5 min)
- **INV-ATT-03** — only STORED attachments can back evidence or observations
- **INV-ATT-04** — every download is authorized per request and audited

## الحالات

- غير نهائية: PENDING, SCANNING, STORED
- نهائية: QUARANTINED, EXPIRED, ERASED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ATT-INITIATE-UPLOAD | PENDING | size ≤ tenant limit; mime allowed; returns direct upload target (≤ 5 min); same sha256 already STORED in tenant → returns existing | EVT-ATT-UPLOAD-INITIATED | ATTACHMENT_REJECTED |
| PENDING | CMD-ATT-COMPLETE-UPLOAD | SCANNING | stored bytes hash = declared sha256; size matches | EVT-ATT-UPLOADED | HASH_MISMATCH |
| SCANNING | SYS:scan passed | STORED | offline content scanner + format validation | EVT-ATT-STORED | — |
| SCANNING | SYS:scan failed | QUARANTINED | scanner verdict | EVT-ATT-QUARANTINED | — |
| PENDING | SYS:upload window 24 h elapsed | EXPIRED | scheduler | EVT-ATT-EXPIRED | — |
| STORED | CMD-ATT-ERASE | ERASED | erasure order or disposition; no legal hold; key destroyed (ADR-P08) | EVT-ATT-ERASED | LEGAL_HOLD_ACTIVE |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ATT-INITIATE-UPLOAD | CMD-ATT-COMPLETE-UPLOAD | SYS:scan passed | SYS:scan failed | SYS:upload window 24 h elapsed | CMD-ATT-ERASE |
|---|---|---|---|---|---|---|
| ∅ | → PENDING | — | — | — | — | — |
| PENDING | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | → SCANNING | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | → EXPIRED | ✗ ATTACHMENT_INVALID_STATE_TRANSITION |
| SCANNING | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | → STORED | → QUARANTINED | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION |
| STORED | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | → ERASED |
| QUARANTINED | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION |
| EXPIRED | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION |
| ERASED | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION | ✗ ATTACHMENT_INVALID_STATE_TRANSITION |

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
id: AGG-ATTACHMENT
bc: BC02
name: Attachment
tier: T1 metadata
purpose: ملف في Object Storage، معنون بالمحتوى، يُرفع ويُنزّل مباشرة
states:
- PENDING
- SCANNING
- STORED
- QUARANTINED
- EXPIRED
- ERASED
terminal:
- QUARANTINED
- EXPIRED
- ERASED
invariants:
- 'INV-ATT-01: (tenant, sha256) unique among non-terminal attachments'
- 'INV-ATT-02: bytes never pass through application servers (direct transfer, signed
  targets ≤ 5 min)'
- 'INV-ATT-03: only STORED attachments can back evidence or observations'
- 'INV-ATT-04: every download is authorized per request and audited'
entities: []
requirements:
- REQ-INF-003
- REQ-INF-004
- REQ-GOV-008
notes: Direct-to-storage transfer removes the application tier from the bandwidth
  path (SR-05).
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-ATT-INITIATE-UPLOAD
  to: PENDING
  guard: size ≤ tenant limit; mime allowed; returns direct upload target (≤ 5 min);
    same sha256 already STORED in tenant → returns existing
  event: EVT-ATT-UPLOAD-INITIATED
  guard_error: ATTACHMENT_REJECTED
- from:
  - PENDING
  command: CMD-ATT-COMPLETE-UPLOAD
  to: SCANNING
  guard: stored bytes hash = declared sha256; size matches
  event: EVT-ATT-UPLOADED
  guard_error: HASH_MISMATCH
- from:
  - SCANNING
  command: SYS:scan passed
  to: STORED
  guard: offline content scanner + format validation
  event: EVT-ATT-STORED
  guard_error: null
- from:
  - SCANNING
  command: SYS:scan failed
  to: QUARANTINED
  guard: scanner verdict
  event: EVT-ATT-QUARANTINED
  guard_error: null
- from:
  - PENDING
  command: SYS:upload window 24 h elapsed
  to: EXPIRED
  guard: scheduler
  event: EVT-ATT-EXPIRED
  guard_error: null
- from:
  - STORED
  command: CMD-ATT-ERASE
  to: ERASED
  guard: erasure order or disposition; no legal hold; key destroyed (ADR-P08)
  event: EVT-ATT-ERASED
  guard_error: LEGAL_HOLD_ACTIVE
```

</details>
