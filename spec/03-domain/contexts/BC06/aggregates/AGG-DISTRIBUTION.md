---
id: AGG-DISTRIBUTION
type: aggregate
title: Distribution
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
  - REQ-PRD-004
  - REQ-PRD-005
  state_machine: SM-DISTRIBUTION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-DISTRIBUTION — Distribution

**الغرض:** توزيع نسخة معتمدة لمستلمين بعلامة مائية لكل مستلم  
**السياق:** BC06 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-DST-01** — a recipient receives a product only if cleared for its label and within its audience (REQ-PRD-004)
- **INV-DST-02** — every delivered copy carries a unique recipient watermark (REQ-PRD-005)
- **INV-DST-03** — withdrawn products stop being downloadable; recipients are notified

## مكونات داخلية

- Delivery (recipient, format, watermark id, delivered_at)

## الحالات

- غير نهائية: PREPARING
- نهائية: COMPLETED, COMPLETED_WITH_EXCLUSIONS, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-DST-DISTRIBUTE | PREPARING | product APPROVED; recipients (users, org units); formats ⊆ {pdf, docx, in_app}; distributor authorized | EVT-DST-STARTED | PRODUCT_NOT_APPROVED |
| PREPARING | SYS:all recipients authorized and delivered | COMPLETED | per-recipient watermark (recipient id, product version, time) embedded; delivery logged | EVT-DST-COMPLETED | — |
| PREPARING | SYS:some recipients not authorized | COMPLETED_WITH_EXCLUSIONS | unauthorized recipients excluded and listed to the distributor; others delivered | EVT-DST-COMPLETED-WITH-EXCLUSIONS | — |
| PREPARING | CMD-DST-CANCEL | CANCELLED | distributor; reason | EVT-DST-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-DST-DISTRIBUTE | SYS:all recipients authorized and delivered | SYS:some recipients not authorized | CMD-DST-CANCEL |
|---|---|---|---|---|
| ∅ | → PREPARING | — | — | — |
| PREPARING | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION | → COMPLETED | → COMPLETED_WITH_EXCLUSIONS | → CANCELLED |
| COMPLETED | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION |
| COMPLETED_WITH_EXCLUSIONS | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION | ✗ DISTRIBUTION_INVALID_STATE_TRANSITION |

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
id: AGG-DISTRIBUTION
bc: BC06
name: Distribution
tier: T2
purpose: توزيع نسخة معتمدة لمستلمين بعلامة مائية لكل مستلم
states:
- PREPARING
- COMPLETED
- COMPLETED_WITH_EXCLUSIONS
- CANCELLED
terminal:
- COMPLETED
- COMPLETED_WITH_EXCLUSIONS
- CANCELLED
invariants:
- 'INV-DST-01: a recipient receives a product only if cleared for its label and within
  its audience (REQ-PRD-004)'
- 'INV-DST-02: every delivered copy carries a unique recipient watermark (REQ-PRD-005)'
- 'INV-DST-03: withdrawn products stop being downloadable; recipients are notified'
entities:
- Delivery (recipient, format, watermark id, delivered_at)
requirements:
- REQ-PRD-004
- REQ-PRD-005
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-DST-DISTRIBUTE
  to: PREPARING
  guard: product APPROVED; recipients (users, org units); formats ⊆ {pdf, docx, in_app};
    distributor authorized
  event: EVT-DST-STARTED
  guard_error: PRODUCT_NOT_APPROVED
- from:
  - PREPARING
  command: SYS:all recipients authorized and delivered
  to: COMPLETED
  guard: per-recipient watermark (recipient id, product version, time) embedded; delivery
    logged
  event: EVT-DST-COMPLETED
  guard_error: null
- from:
  - PREPARING
  command: SYS:some recipients not authorized
  to: COMPLETED_WITH_EXCLUSIONS
  guard: unauthorized recipients excluded and listed to the distributor; others delivered
  event: EVT-DST-COMPLETED-WITH-EXCLUSIONS
  guard_error: null
- from:
  - PREPARING
  command: CMD-DST-CANCEL
  to: CANCELLED
  guard: distributor; reason
  event: EVT-DST-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
