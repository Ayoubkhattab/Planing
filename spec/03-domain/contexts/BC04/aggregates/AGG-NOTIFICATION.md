---
id: AGG-NOTIFICATION
type: aggregate
title: Notification
wave: W4
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC04
importance_tier: T3
personal_data: false
traces:
  satisfies:
  - REQ-COM-001
  - REQ-COM-002
  state_machine: SM-NOTIFICATION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-NOTIFICATION — Notification

**الغرض:** رسالة لمستلم واحد؛ الحمولة مرجع فقط  
**السياق:** BC04 · **المستوى:** T3 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-NTF-01** — a notification is not a domain event and never carries business content (glossary)
- **INV-NTF-02** — push payloads contain no classified content: reference URN + template title chosen from a classification-safe list (REQ-COM-002)
- **INV-NTF-03** — opening a notification performs a normal authorized read; a revoked user sees not-found

## الحالات

- غير نهائية: QUEUED, SENT
- نهائية: READ, FAILED, WITHHELD, EXPIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:notifiable event for recipient | QUEUED | recipient ACTIVE; recipient authorized for the referenced object at enqueue time | EVT-NTF-QUEUED | — |
| QUEUED | SYS:delivered to channel | SENT | re-check authorization at delivery (security_version); push payload = reference + classification-safe title template | EVT-NTF-SENT | — |
| QUEUED | SYS:recipient no longer authorized at delivery | WITHHELD | re-check failed | EVT-NTF-WITHHELD | — |
| QUEUED | SYS:delivery failed after retries | FAILED | 5 attempts with exponential backoff; in-app copy remains | EVT-NTF-FAILED | — |
| SENT | CMD-NTF-MARK-READ | READ | actor = recipient; content fetched through normal authorized query | EVT-NTF-READ | NOT_RECIPIENT |
| QUEUED, SENT | SYS:TTL (30 d) elapsed | EXPIRED | scheduler | EVT-NTF-EXPIRED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:notifiable event for recipient | SYS:delivered to channel | SYS:recipient no longer authorized at delivery | SYS:delivery failed after retries | CMD-NTF-MARK-READ | SYS:TTL (30 d) elapsed |
|---|---|---|---|---|---|---|
| ∅ | → QUEUED | — | — | — | — | — |
| QUEUED | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | → SENT | → WITHHELD | → FAILED | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | → EXPIRED |
| SENT | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | → READ | → EXPIRED |
| READ | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION |
| FAILED | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION |
| WITHHELD | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION |
| EXPIRED | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION | ✗ NOTIFICATION_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-06.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-NOTIFICATION
bc: BC04
name: Notification
tier: T3
purpose: رسالة لمستلم واحد؛ الحمولة مرجع فقط
states:
- QUEUED
- SENT
- READ
- FAILED
- WITHHELD
- EXPIRED
terminal:
- READ
- FAILED
- WITHHELD
- EXPIRED
invariants:
- 'INV-NTF-01: a notification is not a domain event and never carries business content
  (glossary)'
- 'INV-NTF-02: push payloads contain no classified content: reference URN + template
  title chosen from a classification-safe list (REQ-COM-002)'
- 'INV-NTF-03: opening a notification performs a normal authorized read; a revoked
  user sees not-found'
entities: []
requirements:
- REQ-COM-001
- REQ-COM-002
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: SYS:notifiable event for recipient
  to: QUEUED
  guard: recipient ACTIVE; recipient authorized for the referenced object at enqueue
    time
  event: EVT-NTF-QUEUED
  guard_error: null
- from:
  - QUEUED
  command: SYS:delivered to channel
  to: SENT
  guard: re-check authorization at delivery (security_version); push payload = reference
    + classification-safe title template
  event: EVT-NTF-SENT
  guard_error: null
- from:
  - QUEUED
  command: SYS:recipient no longer authorized at delivery
  to: WITHHELD
  guard: re-check failed
  event: EVT-NTF-WITHHELD
  guard_error: null
- from:
  - QUEUED
  command: SYS:delivery failed after retries
  to: FAILED
  guard: 5 attempts with exponential backoff; in-app copy remains
  event: EVT-NTF-FAILED
  guard_error: null
- from:
  - SENT
  command: CMD-NTF-MARK-READ
  to: READ
  guard: actor = recipient; content fetched through normal authorized query
  event: EVT-NTF-READ
  guard_error: NOT_RECIPIENT
- from:
  - QUEUED
  - SENT
  command: SYS:TTL (30 d) elapsed
  to: EXPIRED
  guard: scheduler
  event: EVT-NTF-EXPIRED
  guard_error: null
```

</details>
