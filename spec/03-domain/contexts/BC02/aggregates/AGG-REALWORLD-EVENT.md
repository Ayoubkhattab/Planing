---
id: AGG-REALWORLD-EVENT
type: aggregate
title: Real-World Event (identity)
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T2 identity; attributes T1
personal_data: false
traces:
  satisfies:
  - REQ-INF-020
  state_machine: SM-REALWORLD-EVENT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-REALWORLD-EVENT — Real-World Event (identity)

**الغرض:** حدث وقع في العالم (ليس Domain Event)  
**السياق:** BC02 · **المستوى:** T2 identity; attributes T1 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-RWE-01** — event_time is a fuzzy-interval claim with precision
- **INV-RWE-02** — participants are relationships, not embedded lists

## الحالات

- غير نهائية: ACTIVE, RETIRED
- نهائية: — (perpetual)
- قابلية الوصول لحالة نهائية (SL-06): **EXEMPT: same as Entity**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-RWE-REGISTER | ACTIVE | type in RD-EVENT-TYPES; initial claims include event_time (fuzzy) and location | EVT-RWE-REGISTERED | EVENT_INVALID |
| ACTIVE | CMD-RWE-CHANGE-TYPE | (بلا تغيير) | compatible type; reason | EVT-RWE-TYPE-CHANGED | EVENT_TYPE_INCOMPATIBLE |
| ACTIVE, RETIRED | CMD-RWE-RECLASSIFY | (بلا تغيير) | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | EVT-RWE-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| ACTIVE | CMD-RWE-RETIRE | RETIRED | reason | EVT-RWE-RETIRED | REASON_REQUIRED |
| RETIRED | CMD-RWE-REINSTATE | ACTIVE | reason | EVT-RWE-REINSTATED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-RWE-REGISTER | CMD-RWE-CHANGE-TYPE | CMD-RWE-RECLASSIFY | CMD-RWE-RETIRE | CMD-RWE-REINSTATE |
|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — |
| ACTIVE | ✗ REALWORLD_EVENT_INVALID_STATE_TRANSITION | → ACTIVE | → ACTIVE | → RETIRED | ✗ REALWORLD_EVENT_INVALID_STATE_TRANSITION |
| RETIRED | ✗ REALWORLD_EVENT_INVALID_STATE_TRANSITION | ✗ REALWORLD_EVENT_INVALID_STATE_TRANSITION | → RETIRED | ✗ REALWORLD_EVENT_INVALID_STATE_TRANSITION | → ACTIVE |

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
id: AGG-REALWORLD-EVENT
bc: BC02
name: Real-World Event (identity)
tier: T2 identity; attributes T1
purpose: حدث وقع في العالم (ليس Domain Event)
states:
- ACTIVE
- RETIRED
terminal: []
invariants:
- 'INV-RWE-01: event_time is a fuzzy-interval claim with precision'
- 'INV-RWE-02: participants are relationships, not embedded lists'
entities: []
requirements:
- REQ-INF-020
notes: null
personal_data: false
reachability: 'EXEMPT: same as Entity'
transitions:
- from: ∅
  command: CMD-RWE-REGISTER
  to: ACTIVE
  guard: type in RD-EVENT-TYPES; initial claims include event_time (fuzzy) and location
  event: EVT-RWE-REGISTERED
  guard_error: EVENT_INVALID
- from:
  - ACTIVE
  command: CMD-RWE-CHANGE-TYPE
  to: '='
  guard: compatible type; reason
  event: EVT-RWE-TYPE-CHANGED
  guard_error: EVENT_TYPE_INCOMPATIBLE
- from:
  - ACTIVE
  - RETIRED
  command: CMD-RWE-RECLASSIFY
  to: '='
  guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
  event: EVT-RWE-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
- from:
  - ACTIVE
  command: CMD-RWE-RETIRE
  to: RETIRED
  guard: reason
  event: EVT-RWE-RETIRED
  guard_error: REASON_REQUIRED
- from:
  - RETIRED
  command: CMD-RWE-REINSTATE
  to: ACTIVE
  guard: reason
  event: EVT-RWE-REINSTATED
  guard_error: REASON_REQUIRED
```

</details>
