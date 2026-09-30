---
id: AGG-EVIDENCE-LINK
type: aggregate
title: Evidence Link
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
  - REQ-INF-021
  state_machine: SM-EVIDENCE-LINK
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-EVIDENCE-LINK — Evidence Link

**الغرض:** ربط دليل بادعاء (يدعم / ينفي / سياق)  
**السياق:** BC02 · **المستوى:** T1 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-EVL-01** — links are bitemporal records; removal closes recorded_to
- **INV-EVL-02** — link label = max(evidence label, claim label)

## الحالات

- غير نهائية: ACTIVE
- نهائية: REMOVED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-EVL-LINK | ACTIVE | evidence not WITHDRAWN; claim exists; stance ∈ {SUPPORTS, REFUTES, CONTEXT}; no ACTIVE duplicate (evidence, claim, stance) | EVT-EVL-LINKED | LINK_DUPLICATE |
| ACTIVE | CMD-EVL-UNLINK | REMOVED | reason; recorded_to closed | EVT-EVL-UNLINKED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-EVL-LINK | CMD-EVL-UNLINK |
|---|---|---|
| ∅ | → ACTIVE | — |
| ACTIVE | ✗ EVIDENCE_LINK_INVALID_STATE_TRANSITION | → REMOVED |
| REMOVED | ✗ EVIDENCE_LINK_INVALID_STATE_TRANSITION | ✗ EVIDENCE_LINK_INVALID_STATE_TRANSITION |

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
id: AGG-EVIDENCE-LINK
bc: BC02
name: Evidence Link
tier: T1
purpose: ربط دليل بادعاء (يدعم / ينفي / سياق)
states:
- ACTIVE
- REMOVED
terminal:
- REMOVED
invariants:
- 'INV-EVL-01: links are bitemporal records; removal closes recorded_to'
- 'INV-EVL-02: link label = max(evidence label, claim label)'
entities: []
requirements:
- REQ-INF-021
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-EVL-LINK
  to: ACTIVE
  guard: evidence not WITHDRAWN; claim exists; stance ∈ {SUPPORTS, REFUTES, CONTEXT};
    no ACTIVE duplicate (evidence, claim, stance)
  event: EVT-EVL-LINKED
  guard_error: LINK_DUPLICATE
- from:
  - ACTIVE
  command: CMD-EVL-UNLINK
  to: REMOVED
  guard: reason; recorded_to closed
  event: EVT-EVL-UNLINKED
  guard_error: REASON_REQUIRED
```

</details>
