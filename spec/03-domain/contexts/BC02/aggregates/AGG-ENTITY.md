---
id: AGG-ENTITY
type: aggregate
title: Entity (identity)
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T2 identity; attributes T1 as claims
personal_data: false
traces:
  satisfies:
  - REQ-INF-020
  - REQ-INF-021
  - REQ-INF-036
  state_machine: SM-ENTITY
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ENTITY — Entity (identity)

**الغرض:** هوية كيان؛ سماته ادعاءات مستقلة  
**السياق:** BC02 · **المستوى:** T2 identity; attributes T1 as claims · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-ENT-01** — an entity holds no attribute values; all T1 attributes are claims
- **INV-ENT-02** — claims hidden from a reader are invisible everywhere, including completeness and counts
- **INV-ENT-03** — RETIRED entities remain resolvable for history and as-of queries

## الحالات

- غير نهائية: ACTIVE, RETIRED
- نهائية: — (perpetual)
- قابلية الوصول لحالة نهائية (SL-06): **EXEMPT: identity persists for history and as-of queries; RETIRED is reversible (SL-06 exemption, justified)**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-ENT-REGISTER | ACTIVE | type in RD-ENTITY-TYPES; each initial claim valid as CMD-CLM-ASSERT; Entity + initial Claims created in one unit of work | EVT-ENT-REGISTERED | ENTITY_INVALID |
| ACTIVE | CMD-ENT-CHANGE-TYPE | (بلا تغيير) | compatible type per RD-ENTITY-TYPES; new version; reason | EVT-ENT-TYPE-CHANGED | ENTITY_TYPE_INCOMPATIBLE |
| ACTIVE, RETIRED | CMD-ENT-RECLASSIFY | (بلا تغيير) | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | EVT-ENT-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| ACTIVE | CMD-ENT-RETIRE | RETIRED | reason (created in error / no longer tracked); claims untouched | EVT-ENT-RETIRED | REASON_REQUIRED |
| RETIRED | CMD-ENT-REINSTATE | ACTIVE | reason | EVT-ENT-REINSTATED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-ENT-REGISTER | CMD-ENT-CHANGE-TYPE | CMD-ENT-RECLASSIFY | CMD-ENT-RETIRE | CMD-ENT-REINSTATE |
|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — |
| ACTIVE | ✗ ENTITY_INVALID_STATE_TRANSITION | → ACTIVE | → ACTIVE | → RETIRED | ✗ ENTITY_INVALID_STATE_TRANSITION |
| RETIRED | ✗ ENTITY_INVALID_STATE_TRANSITION | ✗ ENTITY_INVALID_STATE_TRANSITION | → RETIRED | ✗ ENTITY_INVALID_STATE_TRANSITION | → ACTIVE |

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
id: AGG-ENTITY
bc: BC02
name: Entity (identity)
tier: T2 identity; attributes T1 as claims
purpose: هوية كيان؛ سماته ادعاءات مستقلة
states:
- ACTIVE
- RETIRED
terminal: []
invariants:
- 'INV-ENT-01: an entity holds no attribute values; all T1 attributes are claims'
- 'INV-ENT-02: claims hidden from a reader are invisible everywhere, including completeness
  and counts'
- 'INV-ENT-03: RETIRED entities remain resolvable for history and as-of queries'
entities: []
requirements:
- REQ-INF-020
- REQ-INF-021
- REQ-INF-036
notes: null
personal_data: false
reachability: 'EXEMPT: identity persists for history and as-of queries; RETIRED is
  reversible (SL-06 exemption, justified)'
transitions:
- from: ∅
  command: CMD-ENT-REGISTER
  to: ACTIVE
  guard: type in RD-ENTITY-TYPES; each initial claim valid as CMD-CLM-ASSERT; Entity
    + initial Claims created in one unit of work
  event: EVT-ENT-REGISTERED
  guard_error: ENTITY_INVALID
- from:
  - ACTIVE
  command: CMD-ENT-CHANGE-TYPE
  to: '='
  guard: compatible type per RD-ENTITY-TYPES; new version; reason
  event: EVT-ENT-TYPE-CHANGED
  guard_error: ENTITY_TYPE_INCOMPATIBLE
- from:
  - ACTIVE
  - RETIRED
  command: CMD-ENT-RECLASSIFY
  to: '='
  guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
  event: EVT-ENT-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
- from:
  - ACTIVE
  command: CMD-ENT-RETIRE
  to: RETIRED
  guard: reason (created in error / no longer tracked); claims untouched
  event: EVT-ENT-RETIRED
  guard_error: REASON_REQUIRED
- from:
  - RETIRED
  command: CMD-ENT-REINSTATE
  to: ACTIVE
  guard: reason
  event: EVT-ENT-REINSTATED
  guard_error: REASON_REQUIRED
```

</details>
