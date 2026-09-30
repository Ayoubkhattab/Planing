---
id: AGG-SUBSCRIPTION
type: aggregate
title: Subscription
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
  state_machine: SM-SUBSCRIPTION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SUBSCRIPTION — Subscription

**الغرض:** اشتراك مستخدم في تنبيهات موقف أو قاعدة، بقنوات مفضلة  
**السياق:** BC04 · **المستوى:** T3 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-SUB-01** — a subscription never grants access; delivery re-checks authorization
- **INV-SUB-02** — subscriptions end automatically when the target becomes invisible to the subscriber

## الحالات

- غير نهائية: ACTIVE, PAUSED
- نهائية: ENDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-SUB-SUBSCRIBE | ACTIVE | target (situation | alert rule) visible to subscriber; channels ⊆ {in_app, push}; one ACTIVE per (user, target) | EVT-SUB-SUBSCRIBED | SUBSCRIPTION_EXISTS |
| ACTIVE, PAUSED | CMD-SUB-UPDATE-CHANNELS | (بلا تغيير) | channels valid; quiet hours valid (critical severity bypasses quiet hours) | EVT-SUB-CHANNELS-UPDATED | SUBSCRIPTION_INVALID |
| ACTIVE | CMD-SUB-PAUSE | PAUSED | — | EVT-SUB-PAUSED | — |
| PAUSED | CMD-SUB-RESUME | ACTIVE | target still visible | EVT-SUB-RESUMED | TARGET_NOT_VISIBLE |
| ACTIVE, PAUSED | CMD-SUB-UNSUBSCRIBE | ENDED | actor = subscriber or Administrator | EVT-SUB-ENDED | — |
| ACTIVE, PAUSED | SYS:subscriber lost visibility of target | ENDED | security-version change or reclassification | EVT-SUB-ENDED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-SUB-SUBSCRIBE | CMD-SUB-UPDATE-CHANNELS | CMD-SUB-PAUSE | CMD-SUB-RESUME | CMD-SUB-UNSUBSCRIBE | SYS:subscriber lost visibility of target |
|---|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — | — |
| ACTIVE | ✗ SUBSCRIPTION_INVALID_STATE_TRANSITION | → ACTIVE | → PAUSED | ✗ SUBSCRIPTION_INVALID_STATE_TRANSITION | → ENDED | → ENDED |
| PAUSED | ✗ SUBSCRIPTION_INVALID_STATE_TRANSITION | → PAUSED | ✗ SUBSCRIPTION_INVALID_STATE_TRANSITION | → ACTIVE | → ENDED | → ENDED |
| ENDED | ✗ SUBSCRIPTION_INVALID_STATE_TRANSITION | ✗ SUBSCRIPTION_INVALID_STATE_TRANSITION | ✗ SUBSCRIPTION_INVALID_STATE_TRANSITION | ✗ SUBSCRIPTION_INVALID_STATE_TRANSITION | ✗ SUBSCRIPTION_INVALID_STATE_TRANSITION | ✗ SUBSCRIPTION_INVALID_STATE_TRANSITION |

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
id: AGG-SUBSCRIPTION
bc: BC04
name: Subscription
tier: T3
purpose: اشتراك مستخدم في تنبيهات موقف أو قاعدة، بقنوات مفضلة
states:
- ACTIVE
- PAUSED
- ENDED
terminal:
- ENDED
invariants:
- 'INV-SUB-01: a subscription never grants access; delivery re-checks authorization'
- 'INV-SUB-02: subscriptions end automatically when the target becomes invisible to
  the subscriber'
entities: []
requirements:
- REQ-COM-001
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-SUB-SUBSCRIBE
  to: ACTIVE
  guard: target (situation | alert rule) visible to subscriber; channels ⊆ {in_app,
    push}; one ACTIVE per (user, target)
  event: EVT-SUB-SUBSCRIBED
  guard_error: SUBSCRIPTION_EXISTS
- from:
  - ACTIVE
  - PAUSED
  command: CMD-SUB-UPDATE-CHANNELS
  to: '='
  guard: channels valid; quiet hours valid (critical severity bypasses quiet hours)
  event: EVT-SUB-CHANNELS-UPDATED
  guard_error: SUBSCRIPTION_INVALID
- from:
  - ACTIVE
  command: CMD-SUB-PAUSE
  to: PAUSED
  guard: —
  event: EVT-SUB-PAUSED
  guard_error: null
- from:
  - PAUSED
  command: CMD-SUB-RESUME
  to: ACTIVE
  guard: target still visible
  event: EVT-SUB-RESUMED
  guard_error: TARGET_NOT_VISIBLE
- from:
  - ACTIVE
  - PAUSED
  command: CMD-SUB-UNSUBSCRIBE
  to: ENDED
  guard: actor = subscriber or Administrator
  event: EVT-SUB-ENDED
  guard_error: null
- from:
  - ACTIVE
  - PAUSED
  command: SYS:subscriber lost visibility of target
  to: ENDED
  guard: security-version change or reclassification
  event: EVT-SUB-ENDED
  guard_error: null
```

</details>
