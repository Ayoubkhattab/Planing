---
id: AGG-LEGAL-HOLD
type: aggregate
title: Legal Hold
wave: W4
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC08
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-GOV-007
  state_machine: SM-LEGAL-HOLD
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-LEGAL-HOLD — Legal Hold

**الغرض:** تجميد قانوني يمنع إتلاف ومحو ما يشمله  
**السياق:** BC08 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-LHD-01** — while ACTIVE or RELEASE_REQUESTED, no matching record can be disposed, erased or have its key destroyed (REQ-GOV-007)
- **INV-LHD-02** — holds never block versioned changes (history is preserved); they block destructive actions only
- **INV-LHD-03** — scope can only grow while ACTIVE; narrowing = release + new hold
- **INV-LHD-04** — release needs two distinct Legal authorities

## مكونات داخلية

- HoldScopeItem

## الحالات

- غير نهائية: ACTIVE, RELEASE_REQUESTED
- نهائية: RELEASED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-LHD-PLACE | ACTIVE | Legal/Compliance authority; scope = any of: record classes, object URNs, data subjects, org units, time range; legal reference | EVT-LHD-PLACED | HOLD_INVALID |
| ACTIVE | CMD-LHD-EXTEND | (بلا تغيير) | added scope items; reason | EVT-LHD-EXTENDED | HOLD_INVALID |
| ACTIVE | CMD-LHD-REQUEST-RELEASE | RELEASE_REQUESTED | reason; requester = Legal authority | EVT-LHD-RELEASE-REQUESTED | REASON_REQUIRED |
| RELEASE_REQUESTED | CMD-LHD-APPROVE-RELEASE | RELEASED | second Legal authority ≠ requester | EVT-LHD-RELEASED | SEGREGATION_OF_DUTIES |
| RELEASE_REQUESTED | CMD-LHD-CANCEL-RELEASE | ACTIVE | reason | EVT-LHD-RELEASE-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-LHD-PLACE | CMD-LHD-EXTEND | CMD-LHD-REQUEST-RELEASE | CMD-LHD-APPROVE-RELEASE | CMD-LHD-CANCEL-RELEASE |
|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — |
| ACTIVE | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION | → ACTIVE | → RELEASE_REQUESTED | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION |
| RELEASE_REQUESTED | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION | → RELEASED | → ACTIVE |
| RELEASED | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION | ✗ LEGAL_HOLD_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-12a.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-LEGAL-HOLD
bc: BC08
name: Legal Hold
tier: T2
purpose: تجميد قانوني يمنع إتلاف ومحو ما يشمله
states:
- ACTIVE
- RELEASE_REQUESTED
- RELEASED
terminal:
- RELEASED
invariants:
- 'INV-LHD-01: while ACTIVE or RELEASE_REQUESTED, no matching record can be disposed,
  erased or have its key destroyed (REQ-GOV-007)'
- 'INV-LHD-02: holds never block versioned changes (history is preserved); they block
  destructive actions only'
- 'INV-LHD-03: scope can only grow while ACTIVE; narrowing = release + new hold'
- 'INV-LHD-04: release needs two distinct Legal authorities'
entities:
- HoldScopeItem
requirements:
- REQ-GOV-007
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-LHD-PLACE
  to: ACTIVE
  guard: 'Legal/Compliance authority; scope = any of: record classes, object URNs,
    data subjects, org units, time range; legal reference'
  event: EVT-LHD-PLACED
  guard_error: HOLD_INVALID
- from:
  - ACTIVE
  command: CMD-LHD-EXTEND
  to: '='
  guard: added scope items; reason
  event: EVT-LHD-EXTENDED
  guard_error: HOLD_INVALID
- from:
  - ACTIVE
  command: CMD-LHD-REQUEST-RELEASE
  to: RELEASE_REQUESTED
  guard: reason; requester = Legal authority
  event: EVT-LHD-RELEASE-REQUESTED
  guard_error: REASON_REQUIRED
- from:
  - RELEASE_REQUESTED
  command: CMD-LHD-APPROVE-RELEASE
  to: RELEASED
  guard: second Legal authority ≠ requester
  event: EVT-LHD-RELEASED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - RELEASE_REQUESTED
  command: CMD-LHD-CANCEL-RELEASE
  to: ACTIVE
  guard: reason
  event: EVT-LHD-RELEASE-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
