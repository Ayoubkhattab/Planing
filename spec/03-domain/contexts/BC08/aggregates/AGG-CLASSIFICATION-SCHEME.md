---
id: AGG-CLASSIFICATION-SCHEME
type: aggregate
title: Classification Scheme Version
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
  - REQ-GOV-001
  - REQ-GOV-004
  - REQ-GOV-009
  state_machine: SM-CLASSIFICATION-SCHEME
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-CLASSIFICATION-SCHEME — Classification Scheme Version

**الغرض:** نظام التصنيف لكل مستأجر بإصدارات  
**السياق:** BC08 · **المستوى:** T2 · **بيانات شخصية:** لا

> REQ-GOV-004 added to satisfies by CR-65 (2026-09-29): CMD-CLS-ACTIVATE's guard (previous ACTIVE -> SUPERSEDED in same transaction) plus INV-CLS-04 (activation increments security_version of all subjects in the tenant) is the scheme-level enforcement mechanism for REQ-GOV-004's "stop returning the object to newly unauthorized subjects from the moment of the change" -- previously undeclared here despite UC-085 already being listed against REQ-GOV-004 in requirements.md (see CR-64 residual_note).

## الثوابت (Invariants)

- **INV-CLS-01** — exactly one ACTIVE scheme version per tenant
- **INV-CLS-02** — level ranks strictly ordered and unique; codes immutable
- **INV-CLS-03** — levels, compartments and caveats can be deprecated, never removed
- **INV-CLS-04** — activation increments the security_version of all subjects in the tenant

## مكونات داخلية

- Level, Compartment, Caveat (value objects)

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: SUPERSEDED, DISCARDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-CLS-DRAFT | DRAFT | Security Officer; at most one DRAFT per tenant | EVT-CLS-DRAFTED | DRAFT_EXISTS |
| DRAFT | CMD-CLS-EDIT | (بلا تغيير) | codes immutable once used; ranks strictly ordered; removal not allowed, only deprecation | EVT-CLS-EDITED | SCHEME_INVALID |
| DRAFT | CMD-CLS-ACTIVATE | ACTIVE | validation passes; effective_from ≥ now; approver ≠ drafter; previous ACTIVE → SUPERSEDED in same transaction | EVT-CLS-ACTIVATED | SCHEME_INVALID |
| DRAFT | CMD-CLS-DISCARD | DISCARDED | — | EVT-CLS-DISCARDED | — |
| ACTIVE | SYS:successor activated | SUPERSEDED | system | EVT-CLS-SUPERSEDED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-CLS-DRAFT | CMD-CLS-EDIT | CMD-CLS-ACTIVATE | CMD-CLS-DISCARD | SYS:successor activated |
|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — |
| DRAFT | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | → DISCARDED | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | → SUPERSEDED |
| SUPERSEDED | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
| DISCARDED | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | ✗ CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |

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
id: AGG-CLASSIFICATION-SCHEME
bc: BC08
name: Classification Scheme Version
tier: T2
purpose: نظام التصنيف لكل مستأجر بإصدارات
states:
- DRAFT
- ACTIVE
- SUPERSEDED
- DISCARDED
terminal:
- SUPERSEDED
- DISCARDED
invariants:
- 'INV-CLS-01: exactly one ACTIVE scheme version per tenant'
- 'INV-CLS-02: level ranks strictly ordered and unique; codes immutable'
- 'INV-CLS-03: levels, compartments and caveats can be deprecated, never removed'
- 'INV-CLS-04: activation increments the security_version of all subjects in the tenant'
entities:
- Level, Compartment, Caveat (value objects)
requirements:
- REQ-GOV-001
- REQ-GOV-004
- REQ-GOV-009
notes: 'REQ-GOV-004 added to satisfies by CR-65 (2026-09-29): CMD-CLS-ACTIVATE''s
  guard (previous ACTIVE -> SUPERSEDED in same transaction) plus INV-CLS-04 (activation
  increments security_version of all subjects in the tenant) is the scheme-level enforcement
  mechanism for REQ-GOV-004''s "stop returning the object to newly unauthorized subjects
  from the moment of the change" -- previously undeclared here despite UC-085 already
  being listed against REQ-GOV-004 in requirements.md (see CR-64 residual_note).'
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-CLS-DRAFT
  to: DRAFT
  guard: Security Officer; at most one DRAFT per tenant
  event: EVT-CLS-DRAFTED
  guard_error: DRAFT_EXISTS
- from:
  - DRAFT
  command: CMD-CLS-EDIT
  to: '='
  guard: codes immutable once used; ranks strictly ordered; removal not allowed, only
    deprecation
  event: EVT-CLS-EDITED
  guard_error: SCHEME_INVALID
- from:
  - DRAFT
  command: CMD-CLS-ACTIVATE
  to: ACTIVE
  guard: validation passes; effective_from ≥ now; approver ≠ drafter; previous ACTIVE
    → SUPERSEDED in same transaction
  event: EVT-CLS-ACTIVATED
  guard_error: SCHEME_INVALID
- from:
  - DRAFT
  command: CMD-CLS-DISCARD
  to: DISCARDED
  guard: —
  event: EVT-CLS-DISCARDED
  guard_error: null
- from:
  - ACTIVE
  command: SYS:successor activated
  to: SUPERSEDED
  guard: system
  event: EVT-CLS-SUPERSEDED
  guard_error: null
```

</details>
