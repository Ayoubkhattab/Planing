---
id: AGG-MATCH-RULESET
type: aggregate
title: Match Ruleset
wave: W4
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC02
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-INF-032
  - REQ-SRC-003
  state_machine: SM-MATCH-RULESET
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-MATCH-RULESET — Match Ruleset

**الغرض:** قواعد توليد المرشحين (الحجب والسمات والأوزان والعتبات) لكل نوع كيان  
**السياق:** BC02 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-MRS-01** — exactly one ACTIVE ruleset per (tenant, entity type)
- **INV-MRS-02** — every proposal records the ruleset version (lineage)
- **INV-MRS-03** — a ruleset cannot be activated without a passing evaluation on a labelled Arabic/English test set

## مكونات داخلية

- BlockingKey
- Feature (name forms, phonetic key, dates, geohash, identifiers)
- Thresholds (propose)

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: SUPERSEDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-MRS-DRAFT | DRAFT | entity type exists | EVT-MRS-DRAFTED | — |
| DRAFT | CMD-MRS-EDIT | (بلا تغيير) | blocking keys, features, weights, thresholds valid; evaluation run on labelled test set attached | EVT-MRS-EDITED | RULESET_INVALID |
| DRAFT | CMD-MRS-ACTIVATE | ACTIVE | evaluation meets QAS-ER-001 (candidate recall ≥ 95 %) and QAS-ER-002; approver ≠ author; previous ACTIVE → SUPERSEDED | EVT-MRS-ACTIVATED | RULESET_BELOW_TARGET |
| ACTIVE | SYS:successor activated | SUPERSEDED | system | EVT-MRS-SUPERSEDED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-MRS-DRAFT | CMD-MRS-EDIT | CMD-MRS-ACTIVATE | SYS:successor activated |
|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — |
| DRAFT | ✗ MATCH_RULESET_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ MATCH_RULESET_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ MATCH_RULESET_INVALID_STATE_TRANSITION | ✗ MATCH_RULESET_INVALID_STATE_TRANSITION | ✗ MATCH_RULESET_INVALID_STATE_TRANSITION | → SUPERSEDED |
| SUPERSEDED | ✗ MATCH_RULESET_INVALID_STATE_TRANSITION | ✗ MATCH_RULESET_INVALID_STATE_TRANSITION | ✗ MATCH_RULESET_INVALID_STATE_TRANSITION | ✗ MATCH_RULESET_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-04.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-MATCH-RULESET
bc: BC02
name: Match Ruleset
tier: T2
purpose: قواعد توليد المرشحين (الحجب والسمات والأوزان والعتبات) لكل نوع كيان
states:
- DRAFT
- ACTIVE
- SUPERSEDED
terminal:
- SUPERSEDED
invariants:
- 'INV-MRS-01: exactly one ACTIVE ruleset per (tenant, entity type)'
- 'INV-MRS-02: every proposal records the ruleset version (lineage)'
- 'INV-MRS-03: a ruleset cannot be activated without a passing evaluation on a labelled
  Arabic/English test set'
entities:
- BlockingKey
- Feature (name forms, phonetic key, dates, geohash, identifiers)
- Thresholds (propose)
requirements:
- REQ-INF-032
- REQ-SRC-003
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-MRS-DRAFT
  to: DRAFT
  guard: entity type exists
  event: EVT-MRS-DRAFTED
  guard_error: null
- from:
  - DRAFT
  command: CMD-MRS-EDIT
  to: '='
  guard: blocking keys, features, weights, thresholds valid; evaluation run on labelled
    test set attached
  event: EVT-MRS-EDITED
  guard_error: RULESET_INVALID
- from:
  - DRAFT
  command: CMD-MRS-ACTIVATE
  to: ACTIVE
  guard: evaluation meets QAS-ER-001 (candidate recall ≥ 95 %) and QAS-ER-002; approver
    ≠ author; previous ACTIVE → SUPERSEDED
  event: EVT-MRS-ACTIVATED
  guard_error: RULESET_BELOW_TARGET
- from:
  - ACTIVE
  command: SYS:successor activated
  to: SUPERSEDED
  guard: system
  event: EVT-MRS-SUPERSEDED
  guard_error: null
```

</details>
