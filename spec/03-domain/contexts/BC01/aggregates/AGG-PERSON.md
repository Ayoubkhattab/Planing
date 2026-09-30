---
id: AGG-PERSON
type: aggregate
title: Person
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC01
importance_tier: T2
personal_data: true
traces:
  satisfies:
  - REQ-FND-006
  - REQ-GOV-008
  state_machine: SM-PERSON
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-PERSON — Person

**الغرض:** سجل الشخص في المنصة (ليس كيان معلومات من نوع شخص)  
**السياق:** BC01 · **المستوى:** T2 · **بيانات شخصية:** نعم

> Distinct from information Entity of type person (BC02).

## الثوابت (Invariants)

- **INV-PER-01** — personal attributes are flagged personal_data (crypto-shredding, ADR-P08)
- **INV-PER-02** — external HR identifier unique per tenant when present

## الحالات

- غير نهائية: ACTIVE, INACTIVE
- نهائية: ERASED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-PER-REGISTER | ACTIVE | names per language-model; no duplicate HR id | EVT-PER-REGISTERED | PERSON_DUPLICATE |
| ACTIVE | CMD-PER-UPDATE-DETAILS | (بلا تغيير) | — | EVT-PER-DETAILS-UPDATED | — |
| ACTIVE | CMD-PER-DEACTIVATE | INACTIVE | — | EVT-PER-DEACTIVATED | — |
| INACTIVE | CMD-PER-REACTIVATE | ACTIVE | — | EVT-PER-REACTIVATED | — |
| INACTIVE | CMD-PER-ERASE | ERASED | erasure order recorded; no legal hold; destroys subject key (ADR-P08) | EVT-PER-ERASED | LEGAL_HOLD_ACTIVE |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-PER-REGISTER | CMD-PER-UPDATE-DETAILS | CMD-PER-DEACTIVATE | CMD-PER-REACTIVATE | CMD-PER-ERASE |
|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — |
| ACTIVE | ✗ PERSON_INVALID_STATE_TRANSITION | → ACTIVE | → INACTIVE | ✗ PERSON_INVALID_STATE_TRANSITION | ✗ PERSON_INVALID_STATE_TRANSITION |
| INACTIVE | ✗ PERSON_INVALID_STATE_TRANSITION | ✗ PERSON_INVALID_STATE_TRANSITION | ✗ PERSON_INVALID_STATE_TRANSITION | → ACTIVE | → ERASED |
| ERASED | ✗ PERSON_INVALID_STATE_TRANSITION | ✗ PERSON_INVALID_STATE_TRANSITION | ✗ PERSON_INVALID_STATE_TRANSITION | ✗ PERSON_INVALID_STATE_TRANSITION | ✗ PERSON_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-01.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-PERSON
bc: BC01
name: Person
tier: T2
purpose: سجل الشخص في المنصة (ليس كيان معلومات من نوع شخص)
states:
- ACTIVE
- INACTIVE
- ERASED
terminal:
- ERASED
invariants:
- 'INV-PER-01: personal attributes are flagged personal_data (crypto-shredding, ADR-P08)'
- 'INV-PER-02: external HR identifier unique per tenant when present'
entities: []
requirements:
- REQ-FND-006
- REQ-GOV-008
notes: Distinct from information Entity of type person (BC02).
personal_data: true
reachability: PASS
transitions:
- from: ∅
  command: CMD-PER-REGISTER
  to: ACTIVE
  guard: names per language-model; no duplicate HR id
  event: EVT-PER-REGISTERED
  guard_error: PERSON_DUPLICATE
- from:
  - ACTIVE
  command: CMD-PER-UPDATE-DETAILS
  to: '='
  guard: —
  event: EVT-PER-DETAILS-UPDATED
  guard_error: null
- from:
  - ACTIVE
  command: CMD-PER-DEACTIVATE
  to: INACTIVE
  guard: —
  event: EVT-PER-DEACTIVATED
  guard_error: null
- from:
  - INACTIVE
  command: CMD-PER-REACTIVATE
  to: ACTIVE
  guard: —
  event: EVT-PER-REACTIVATED
  guard_error: null
- from:
  - INACTIVE
  command: CMD-PER-ERASE
  to: ERASED
  guard: erasure order recorded; no legal hold; destroys subject key (ADR-P08)
  event: EVT-PER-ERASED
  guard_error: LEGAL_HOLD_ACTIVE
```

</details>
