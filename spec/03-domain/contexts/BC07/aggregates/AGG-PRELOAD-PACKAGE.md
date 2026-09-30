---
id: AGG-PRELOAD-PACKAGE
type: aggregate
title: Preload Package
wave: W4
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC07
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-OFF-002
  - REQ-OFF-005
  state_machine: SM-PRELOAD-PACKAGE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-PRELOAD-PACKAGE — Preload Package

**الغرض:** حزمة بيانات منطقة عمل للاستخدام دون اتصال، مفلترة بصلاحية المستخدم وقت البناء  
**السياق:** BC07 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-PKG-01** — package content never exceeds the user's authorization at build time nor the tenant offline level (REQ-OFF-002)
- **INV-PKG-02** — packages expire; expired or revoked data becomes unreadable on the device (local key discarded)
- **INV-PKG-03** — any change of the user's security_version revokes all their packages

## مكونات داخلية

- Manifest (items, hashes, labels, expires_at)

## الحالات

- غير نهائية: REQUESTED, BUILDING, READY, DOWNLOADED
- نهائية: EXPIRED, REVOKED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-PKG-REQUEST | REQUESTED | device ACTIVE; area polygon ≤ tenant max area; layers; time window; requested level ≤ tenant offline max level (default INTERNAL, POL-OFFLINE-PRELOAD) | EVT-PKG-REQUESTED | PRELOAD_NOT_ALLOWED |
| REQUESTED | SYS:build started | BUILDING | worker | EVT-PKG-BUILDING | — |
| BUILDING | SYS:build finished | READY | content = objects visible to the user at build time and ≤ requested level; manifest with hashes, labels, security_version, expires_at (≤ 72 h R1) | EVT-PKG-READY | — |
| READY | CMD-PKG-CONFIRM-DOWNLOAD | DOWNLOADED | device acknowledges manifest hash | EVT-PKG-DOWNLOADED | MANIFEST_MISMATCH |
| READY, DOWNLOADED | SYS:expires_at reached | EXPIRED | device purges at expiry (local enforcement) and confirms on next contact | EVT-PKG-EXPIRED | — |
| REQUESTED, BUILDING, READY, DOWNLOADED | SYS:user security_version changed or device not ACTIVE | REVOKED | purge instruction on next contact | EVT-PKG-REVOKED | — |
| REQUESTED, BUILDING, READY, DOWNLOADED | CMD-PKG-REVOKE | REVOKED | user, Administrator or Security Officer; reason | EVT-PKG-REVOKED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-PKG-REQUEST | SYS:build started | SYS:build finished | CMD-PKG-CONFIRM-DOWNLOAD | SYS:expires_at reached | SYS:user security_version changed or device not ACTIVE | CMD-PKG-REVOKE |
|---|---|---|---|---|---|---|---|
| ∅ | → REQUESTED | — | — | — | — | — | — |
| REQUESTED | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | → BUILDING | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | → REVOKED | → REVOKED |
| BUILDING | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | → READY | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | → REVOKED | → REVOKED |
| READY | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | → DOWNLOADED | → EXPIRED | → REVOKED | → REVOKED |
| DOWNLOADED | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | → EXPIRED | → REVOKED | → REVOKED |
| EXPIRED | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
| REVOKED | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | ✗ PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-11.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-PRELOAD-PACKAGE
bc: BC07
name: Preload Package
tier: T2
purpose: حزمة بيانات منطقة عمل للاستخدام دون اتصال، مفلترة بصلاحية المستخدم وقت البناء
states:
- REQUESTED
- BUILDING
- READY
- DOWNLOADED
- EXPIRED
- REVOKED
terminal:
- EXPIRED
- REVOKED
invariants:
- 'INV-PKG-01: package content never exceeds the user''s authorization at build time
  nor the tenant offline level (REQ-OFF-002)'
- 'INV-PKG-02: packages expire; expired or revoked data becomes unreadable on the
  device (local key discarded)'
- 'INV-PKG-03: any change of the user''s security_version revokes all their packages'
entities:
- Manifest (items, hashes, labels, expires_at)
requirements:
- REQ-OFF-002
- REQ-OFF-005
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-PKG-REQUEST
  to: REQUESTED
  guard: device ACTIVE; area polygon ≤ tenant max area; layers; time window; requested
    level ≤ tenant offline max level (default INTERNAL, POL-OFFLINE-PRELOAD)
  event: EVT-PKG-REQUESTED
  guard_error: PRELOAD_NOT_ALLOWED
- from:
  - REQUESTED
  command: SYS:build started
  to: BUILDING
  guard: worker
  event: EVT-PKG-BUILDING
  guard_error: null
- from:
  - BUILDING
  command: SYS:build finished
  to: READY
  guard: content = objects visible to the user at build time and ≤ requested level;
    manifest with hashes, labels, security_version, expires_at (≤ 72 h R1)
  event: EVT-PKG-READY
  guard_error: null
- from:
  - READY
  command: CMD-PKG-CONFIRM-DOWNLOAD
  to: DOWNLOADED
  guard: device acknowledges manifest hash
  event: EVT-PKG-DOWNLOADED
  guard_error: MANIFEST_MISMATCH
- from:
  - READY
  - DOWNLOADED
  command: SYS:expires_at reached
  to: EXPIRED
  guard: device purges at expiry (local enforcement) and confirms on next contact
  event: EVT-PKG-EXPIRED
  guard_error: null
- from:
  - REQUESTED
  - BUILDING
  - READY
  - DOWNLOADED
  command: SYS:user security_version changed or device not ACTIVE
  to: REVOKED
  guard: purge instruction on next contact
  event: EVT-PKG-REVOKED
  guard_error: null
- from:
  - REQUESTED
  - BUILDING
  - READY
  - DOWNLOADED
  command: CMD-PKG-REVOKE
  to: REVOKED
  guard: user, Administrator or Security Officer; reason
  event: EVT-PKG-REVOKED
  guard_error: REASON_REQUIRED
```

</details>
