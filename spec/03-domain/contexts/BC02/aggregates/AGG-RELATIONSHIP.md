---
id: AGG-RELATIONSHIP
type: aggregate
title: Relationship (identity)
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T1
personal_data: false
traces:
  satisfies:
  - REQ-INF-027
  state_machine: SM-RELATIONSHIP
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-RELATIONSHIP — Relationship (identity)

**الغرض:** رابط موجّه بين كائنين؛ وجوده ادعاء  
**السياق:** BC02 · **المستوى:** T1 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-REL-01** — validity comes from the existence claim; the identity carries type, endpoints and label
- **INV-REL-02** — a relationship may be labelled above both endpoints and is then invisible without clearance

## الحالات

- غير نهائية: ACTIVE, RETIRED
- نهائية: — (perpetual)
- قابلية الوصول لحالة نهائية (SL-06): **EXEMPT: same as Entity; validity lives in the existence claim**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-REL-REGISTER | ACTIVE | type in RD-RELATIONSHIP-TYPES; endpoint types allowed; creates identity + existence claim (valid interval, sources ≥ 1) | EVT-REL-REGISTERED | RELATIONSHIP_INVALID |
| ACTIVE, RETIRED | CMD-REL-RECLASSIFY | (بلا تغيير) | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | EVT-REL-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| ACTIVE | CMD-REL-RETIRE | RETIRED | created in error only; ending in reality = CMD-CLM-RECORD-CHANGE on the existence claim | EVT-REL-RETIRED | REASON_REQUIRED |
| RETIRED | CMD-REL-REINSTATE | ACTIVE | reason | EVT-REL-REINSTATED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-REL-REGISTER | CMD-REL-RECLASSIFY | CMD-REL-RETIRE | CMD-REL-REINSTATE |
|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — |
| ACTIVE | ✗ RELATIONSHIP_INVALID_STATE_TRANSITION | → ACTIVE | → RETIRED | ✗ RELATIONSHIP_INVALID_STATE_TRANSITION |
| RETIRED | ✗ RELATIONSHIP_INVALID_STATE_TRANSITION | → RETIRED | ✗ RELATIONSHIP_INVALID_STATE_TRANSITION | → ACTIVE |

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
id: AGG-RELATIONSHIP
bc: BC02
name: Relationship (identity)
tier: T1
purpose: رابط موجّه بين كائنين؛ وجوده ادعاء
states:
- ACTIVE
- RETIRED
terminal: []
invariants:
- 'INV-REL-01: validity comes from the existence claim; the identity carries type,
  endpoints and label'
- 'INV-REL-02: a relationship may be labelled above both endpoints and is then invisible
  without clearance'
entities: []
requirements:
- REQ-INF-027
notes: null
personal_data: false
reachability: 'EXEMPT: same as Entity; validity lives in the existence claim'
transitions:
- from: ∅
  command: CMD-REL-REGISTER
  to: ACTIVE
  guard: type in RD-RELATIONSHIP-TYPES; endpoint types allowed; creates identity +
    existence claim (valid interval, sources ≥ 1)
  event: EVT-REL-REGISTERED
  guard_error: RELATIONSHIP_INVALID
- from:
  - ACTIVE
  - RETIRED
  command: CMD-REL-RECLASSIFY
  to: '='
  guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
  event: EVT-REL-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
- from:
  - ACTIVE
  command: CMD-REL-RETIRE
  to: RETIRED
  guard: created in error only; ending in reality = CMD-CLM-RECORD-CHANGE on the existence
    claim
  event: EVT-REL-RETIRED
  guard_error: REASON_REQUIRED
- from:
  - RETIRED
  command: CMD-REL-REINSTATE
  to: ACTIVE
  guard: reason
  event: EVT-REL-REINSTATED
  guard_error: REASON_REQUIRED
```

</details>
