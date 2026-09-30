---
id: AGG-CAP-MESSAGE
type: aggregate
title: CAP Message (outbound)
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC03
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-INT-003
  state_machine: SM-CAP-MESSAGE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-CAP-MESSAGE — CAP Message (outbound)

**الغرض:** رسالة تنبيه بصيغة CAP 1.2 تُصدر لنقطة خارجية مسموحة  
**السياق:** BC03 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-CAP-01** — nothing leaves the platform without a release decision by someone other than the preparer
- **INV-CAP-02** — CAP content is generated from a reviewed template and the alert's releasable fields only
- **INV-CAP-03** — inbound CAP messages arrive through an adapter as observations of a CAP source (SLC-02), never as direct alerts

## مكونات داخلية

- CapPayload

## الحالات

- غير نهائية: PREPARED, FAILED
- نهائية: SENT, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-CAP-PREPARE | PREPARED | tenant CAP enabled; alert RAISED/ACKNOWLEDGED; alert label ≤ tenant external release level; content = CAP fields from a reviewed template (no free text from classified sources); target connection cap_endpoint ACTIVE | EVT-CAP-PREPARED | RELEASE_NOT_ALLOWED |
| PREPARED | CMD-CAP-RELEASE | SENT | release authority ≠ preparer; valid CAP 1.2 (schema validated); delivery acknowledged | EVT-CAP-SENT | SEGREGATION_OF_DUTIES |
| PREPARED | SYS:delivery failed after retries | FAILED | 5 retries with backoff | EVT-CAP-FAILED | — |
| FAILED | CMD-CAP-RETRY | PREPARED | operator | EVT-CAP-RETRY | — |
| PREPARED, FAILED | CMD-CAP-CANCEL | CANCELLED | reason | EVT-CAP-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-CAP-PREPARE | CMD-CAP-RELEASE | SYS:delivery failed after retries | CMD-CAP-RETRY | CMD-CAP-CANCEL |
|---|---|---|---|---|---|
| ∅ | → PREPARED | — | — | — | — |
| PREPARED | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | → SENT | → FAILED | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | → CANCELLED |
| SENT | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION |
| FAILED | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | → PREPARED | → CANCELLED |
| CANCELLED | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION | ✗ CAP_MESSAGE_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-16.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-CAP-MESSAGE
bc: BC03
name: CAP Message (outbound)
tier: T2
purpose: رسالة تنبيه بصيغة CAP 1.2 تُصدر لنقطة خارجية مسموحة
states:
- PREPARED
- SENT
- FAILED
- CANCELLED
terminal:
- SENT
- CANCELLED
invariants:
- 'INV-CAP-01: nothing leaves the platform without a release decision by someone other
  than the preparer'
- 'INV-CAP-02: CAP content is generated from a reviewed template and the alert''s
  releasable fields only'
- 'INV-CAP-03: inbound CAP messages arrive through an adapter as observations of a
  CAP source (SLC-02), never as direct alerts'
entities:
- CapPayload
requirements:
- REQ-INT-003
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-CAP-PREPARE
  to: PREPARED
  guard: tenant CAP enabled; alert RAISED/ACKNOWLEDGED; alert label ≤ tenant external
    release level; content = CAP fields from a reviewed template (no free text from
    classified sources); target connection cap_endpoint ACTIVE
  event: EVT-CAP-PREPARED
  guard_error: RELEASE_NOT_ALLOWED
- from:
  - PREPARED
  command: CMD-CAP-RELEASE
  to: SENT
  guard: release authority ≠ preparer; valid CAP 1.2 (schema validated); delivery
    acknowledged
  event: EVT-CAP-SENT
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - PREPARED
  command: SYS:delivery failed after retries
  to: FAILED
  guard: 5 retries with backoff
  event: EVT-CAP-FAILED
  guard_error: null
- from:
  - FAILED
  command: CMD-CAP-RETRY
  to: PREPARED
  guard: operator
  event: EVT-CAP-RETRY
  guard_error: null
- from:
  - PREPARED
  - FAILED
  command: CMD-CAP-CANCEL
  to: CANCELLED
  guard: reason
  event: EVT-CAP-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
