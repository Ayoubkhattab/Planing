---
id: AGG-ROLE-REQUIREMENT
type: aggregate
title: Role Requirement
wave: W4
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC05
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-RES-013
  state_machine: SM-ROLE-REQUIREMENT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ROLE-REQUIREMENT — Role Requirement

**الغرض:** متطلبات جاهزية دور: كفاءات، مؤهلات، شهادات، تدريب حديث، خبرة  
**السياق:** BC05 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-RRQ-01** — one ACTIVE requirement set per role
- **INV-RRQ-02** — readiness is computed at a time t from records valid at t (as-of readiness)

## مكونات داخلية

- Requirement (kind, code, min_level, recency)

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-RRQ-DEFINE | DRAFT | role exists (BC01); requirements reference RD-COMPETENCIES | EVT-RRQ-DEFINED | ROLE_REQUIREMENT_INVALID |
| DRAFT, ACTIVE | CMD-RRQ-EDIT | (بلا تغيير) | requirements valid; ACTIVE → new version | EVT-RRQ-EDITED | ROLE_REQUIREMENT_INVALID |
| DRAFT | CMD-RRQ-ACTIVATE | ACTIVE | approver ≠ author | EVT-RRQ-ACTIVATED | SEGREGATION_OF_DUTIES |
| ACTIVE | CMD-RRQ-RETIRE | RETIRED | reason | EVT-RRQ-RETIRED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-RRQ-DEFINE | CMD-RRQ-EDIT | CMD-RRQ-ACTIVATE | CMD-RRQ-RETIRE |
|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — |
| DRAFT | ✗ ROLE_REQUIREMENT_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ ROLE_REQUIREMENT_INVALID_STATE_TRANSITION | → ACTIVE | ✗ ROLE_REQUIREMENT_INVALID_STATE_TRANSITION | → RETIRED |
| RETIRED | ✗ ROLE_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ ROLE_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ ROLE_REQUIREMENT_INVALID_STATE_TRANSITION | ✗ ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-09.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-ROLE-REQUIREMENT
bc: BC05
name: Role Requirement
tier: T2
purpose: 'متطلبات جاهزية دور: كفاءات، مؤهلات، شهادات، تدريب حديث، خبرة'
states:
- DRAFT
- ACTIVE
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-RRQ-01: one ACTIVE requirement set per role'
- 'INV-RRQ-02: readiness is computed at a time t from records valid at t (as-of readiness)'
entities:
- Requirement (kind, code, min_level, recency)
requirements:
- REQ-RES-013
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-RRQ-DEFINE
  to: DRAFT
  guard: role exists (BC01); requirements reference RD-COMPETENCIES
  event: EVT-RRQ-DEFINED
  guard_error: ROLE_REQUIREMENT_INVALID
- from:
  - DRAFT
  - ACTIVE
  command: CMD-RRQ-EDIT
  to: '='
  guard: requirements valid; ACTIVE → new version
  event: EVT-RRQ-EDITED
  guard_error: ROLE_REQUIREMENT_INVALID
- from:
  - DRAFT
  command: CMD-RRQ-ACTIVATE
  to: ACTIVE
  guard: approver ≠ author
  event: EVT-RRQ-ACTIVATED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - ACTIVE
  command: CMD-RRQ-RETIRE
  to: RETIRED
  guard: reason
  event: EVT-RRQ-RETIRED
  guard_error: REASON_REQUIRED
```

</details>
