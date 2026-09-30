---
id: AGG-RETENTION-SCHEDULE
type: aggregate
title: Retention Schedule Version
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
  - REQ-GOV-006
  state_machine: SM-RETENTION-SCHEDULE
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-RETENTION-SCHEDULE — Retention Schedule Version

**الغرض:** جدول الاحتفاظ لكل مستأجر: لكل فئة سجلات مدة ومحفز وإجراء إتلاف وأساس قانوني  
**السياق:** BC08 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-RTS-01** — exactly one ACTIVE schedule version per tenant; every record class covered
- **INV-RTS-02** — shortening a period applies only to records whose trigger occurs after activation unless the approver explicitly marks it retroactive (legal decision recorded)
- **INV-RTS-03** — schedule versions are immutable once ACTIVE

## مكونات داخلية

- RetentionRule (record_class, period, trigger, action, legal_basis)

## الحالات

- غير نهائية: DRAFT, ACTIVE
- نهائية: SUPERSEDED, DISCARDED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-RTS-DRAFT | DRAFT | Archivist; ≤ 1 DRAFT per tenant | EVT-RTS-DRAFTED | DRAFT_EXISTS |
| DRAFT | CMD-RTS-EDIT | (بلا تغيير) | each rule: record class (RD-RECORD-CLASSES), period (ISO 8601 duration), trigger ∈ {recorded, closed, superseded, event}, action ∈ {DESTROY, REVIEW, ARCHIVE (R2)}, legal basis | EVT-RTS-EDITED | SCHEDULE_INVALID |
| DRAFT | CMD-RTS-ACTIVATE | ACTIVE | every record class in RD-RECORD-CLASSES has exactly one rule (REQ-GOV-006); approver = Legal/Compliance authority ≠ drafter; previous ACTIVE → SUPERSEDED in the same transaction | EVT-RTS-ACTIVATED | SCHEDULE_INCOMPLETE |
| DRAFT | CMD-RTS-DISCARD | DISCARDED | reason | EVT-RTS-DISCARDED | REASON_REQUIRED |
| ACTIVE | SYS:successor activated | SUPERSEDED | system | EVT-RTS-SUPERSEDED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-RTS-DRAFT | CMD-RTS-EDIT | CMD-RTS-ACTIVATE | CMD-RTS-DISCARD | SYS:successor activated |
|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — |
| DRAFT | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | → DISCARDED | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | → SUPERSEDED |
| SUPERSEDED | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
| DISCARDED | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | ✗ RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |

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
id: AGG-RETENTION-SCHEDULE
bc: BC08
name: Retention Schedule Version
tier: T2
purpose: 'جدول الاحتفاظ لكل مستأجر: لكل فئة سجلات مدة ومحفز وإجراء إتلاف وأساس قانوني'
states:
- DRAFT
- ACTIVE
- SUPERSEDED
- DISCARDED
terminal:
- SUPERSEDED
- DISCARDED
invariants:
- 'INV-RTS-01: exactly one ACTIVE schedule version per tenant; every record class
  covered'
- 'INV-RTS-02: shortening a period applies only to records whose trigger occurs after
  activation unless the approver explicitly marks it retroactive (legal decision recorded)'
- 'INV-RTS-03: schedule versions are immutable once ACTIVE'
entities:
- RetentionRule (record_class, period, trigger, action, legal_basis)
requirements:
- REQ-GOV-006
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-RTS-DRAFT
  to: DRAFT
  guard: Archivist; ≤ 1 DRAFT per tenant
  event: EVT-RTS-DRAFTED
  guard_error: DRAFT_EXISTS
- from:
  - DRAFT
  command: CMD-RTS-EDIT
  to: '='
  guard: 'each rule: record class (RD-RECORD-CLASSES), period (ISO 8601 duration),
    trigger ∈ {recorded, closed, superseded, event}, action ∈ {DESTROY, REVIEW, ARCHIVE
    (R2)}, legal basis'
  event: EVT-RTS-EDITED
  guard_error: SCHEDULE_INVALID
- from:
  - DRAFT
  command: CMD-RTS-ACTIVATE
  to: ACTIVE
  guard: every record class in RD-RECORD-CLASSES has exactly one rule (REQ-GOV-006);
    approver = Legal/Compliance authority ≠ drafter; previous ACTIVE → SUPERSEDED
    in the same transaction
  event: EVT-RTS-ACTIVATED
  guard_error: SCHEDULE_INCOMPLETE
- from:
  - DRAFT
  command: CMD-RTS-DISCARD
  to: DISCARDED
  guard: reason
  event: EVT-RTS-DISCARDED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  command: SYS:successor activated
  to: SUPERSEDED
  guard: system
  event: EVT-RTS-SUPERSEDED
  guard_error: null
```

</details>
