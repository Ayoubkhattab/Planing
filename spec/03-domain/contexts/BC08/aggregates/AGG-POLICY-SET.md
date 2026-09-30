---
id: AGG-POLICY-SET
type: aggregate
title: Policy Set Version
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC08
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-FND-011
  - REQ-FND-012
  - REQ-GOV-009
  state_machine: SM-POLICY-SET
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-POLICY-SET — Policy Set Version

**الغرض:** مجموعة سياسات مستأجر (جداول قرار) بإصدارات  
**السياق:** BC08 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-POL-01** — exactly one ACTIVE policy set version per tenant; platform baseline always applies on top
- **INV-POL-02** — tenant policies can only restrict the platform baseline, except parameters explicitly marked configurable (e.g. SoD toggle)
- **INV-POL-03** — a version cannot be approved by its author
- **INV-POL-04** — every version carries decision-table tests that must pass before review

## مكونات داخلية

- DecisionTable (value object)
- PolicyTest (value object)

## الحالات

- غير نهائية: DRAFT, IN_REVIEW, APPROVED, ACTIVE
- نهائية: SUPERSEDED, REJECTED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-POL-DRAFT | DRAFT | Security Officer | EVT-POL-DRAFTED | — |
| DRAFT | CMD-POL-EDIT | (بلا تغيير) | tables validate against schema | EVT-POL-EDITED | POLICY_INVALID |
| DRAFT | CMD-POL-SUBMIT | IN_REVIEW | embedded policy tests all pass; tenant rules only restrict platform baseline | EVT-POL-SUBMITTED | POLICY_TESTS_FAILED |
| IN_REVIEW | CMD-POL-APPROVE | APPROVED | approver ≠ author; Security Officer | EVT-POL-APPROVED | SEGREGATION_OF_DUTIES |
| IN_REVIEW | CMD-POL-REJECT | REJECTED | reason | EVT-POL-REJECTED | REASON_REQUIRED |
| APPROVED | SYS:effective_from reached | ACTIVE | scheduler; previous ACTIVE → SUPERSEDED | EVT-POL-ACTIVATED | — |
| ACTIVE | SYS:successor activated | SUPERSEDED | system | EVT-POL-SUPERSEDED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-POL-DRAFT | CMD-POL-EDIT | CMD-POL-SUBMIT | CMD-POL-APPROVE | CMD-POL-REJECT | SYS:effective_from reached | SYS:successor activated |
|---|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — | — |
| DRAFT | ✗ POLICY_SET_INVALID_STATE_TRANSITION | → DRAFT | → IN_REVIEW | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION |
| IN_REVIEW | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | → APPROVED | → REJECTED | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION |
| APPROVED | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | → ACTIVE | ✗ POLICY_SET_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | → SUPERSEDED |
| SUPERSEDED | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION |
| REJECTED | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION | ✗ POLICY_SET_INVALID_STATE_TRANSITION |

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
id: AGG-POLICY-SET
bc: BC08
name: Policy Set Version
tier: T2
purpose: مجموعة سياسات مستأجر (جداول قرار) بإصدارات
states:
- DRAFT
- IN_REVIEW
- APPROVED
- ACTIVE
- SUPERSEDED
- REJECTED
terminal:
- SUPERSEDED
- REJECTED
invariants:
- 'INV-POL-01: exactly one ACTIVE policy set version per tenant; platform baseline
  always applies on top'
- 'INV-POL-02: tenant policies can only restrict the platform baseline, except parameters
  explicitly marked configurable (e.g. SoD toggle)'
- 'INV-POL-03: a version cannot be approved by its author'
- 'INV-POL-04: every version carries decision-table tests that must pass before review'
entities:
- DecisionTable (value object)
- PolicyTest (value object)
requirements:
- REQ-FND-011
- REQ-FND-012
- REQ-GOV-009
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-POL-DRAFT
  to: DRAFT
  guard: Security Officer
  event: EVT-POL-DRAFTED
  guard_error: null
- from:
  - DRAFT
  command: CMD-POL-EDIT
  to: '='
  guard: tables validate against schema
  event: EVT-POL-EDITED
  guard_error: POLICY_INVALID
- from:
  - DRAFT
  command: CMD-POL-SUBMIT
  to: IN_REVIEW
  guard: embedded policy tests all pass; tenant rules only restrict platform baseline
  event: EVT-POL-SUBMITTED
  guard_error: POLICY_TESTS_FAILED
- from:
  - IN_REVIEW
  command: CMD-POL-APPROVE
  to: APPROVED
  guard: approver ≠ author; Security Officer
  event: EVT-POL-APPROVED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - IN_REVIEW
  command: CMD-POL-REJECT
  to: REJECTED
  guard: reason
  event: EVT-POL-REJECTED
  guard_error: REASON_REQUIRED
- from:
  - APPROVED
  command: SYS:effective_from reached
  to: ACTIVE
  guard: scheduler; previous ACTIVE → SUPERSEDED
  event: EVT-POL-ACTIVATED
  guard_error: null
- from:
  - ACTIVE
  command: SYS:successor activated
  to: SUPERSEDED
  guard: system
  event: EVT-POL-SUPERSEDED
  guard_error: null
```

</details>
