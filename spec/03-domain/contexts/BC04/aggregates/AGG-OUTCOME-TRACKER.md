---
id: AGG-OUTCOME-TRACKER
type: aggregate
title: Outcome Tracker
wave: W4
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC04
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-OPS-013
  state_machine: SM-OUTCOME-TRACKER
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-OUTCOME-TRACKER — Outcome Tracker

**الغرض:** سلسلة قياسات لنتيجة خطة مقابل هدفها  
**السياق:** BC04 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-OUT-01** — measurements are bitemporal records; corrections never overwrite
- **INV-OUT-02** — progress = latest measurement known at K vs target valid at T

## مكونات داخلية

- Measurement (value, unit, measured_at, source, recorded_from/to)
- TargetHistory

## الحالات

- غير نهائية: ACTIVE
- نهائية: CLOSED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | SYS:outcome baselined | ACTIVE | one tracker per (plan, outcome id); target copied from baseline | EVT-OUT-TRACKER-CREATED | — |
| ACTIVE | SYS:target changed by new baseline | (بلا تغيير) | target history appended (valid time = baseline time) | EVT-OUT-TARGET-CHANGED | — |
| ACTIVE | CMD-OUT-RECORD | (بلا تغيير) | value with unit convertible to metric unit (UCUM); measured_at; source = manual \| task result \| observation ref | EVT-OUT-MEASURED | MEASUREMENT_INVALID |
| ACTIVE | CMD-OUT-CORRECT | (بلا تغيير) | corrects a measurement: previous record closed (recorded_to), corrected record added — no overwrite | EVT-OUT-MEASUREMENT-CORRECTED | REASON_REQUIRED |
| ACTIVE | SYS:plan closed or cancelled | CLOSED | system | EVT-OUT-TRACKER-CLOSED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | SYS:outcome baselined | SYS:target changed by new baseline | CMD-OUT-RECORD | CMD-OUT-CORRECT | SYS:plan closed or cancelled |
|---|---|---|---|---|---|
| ∅ | → ACTIVE | — | — | — | — |
| ACTIVE | ✗ OUTCOME_TRACKER_INVALID_STATE_TRANSITION | → ACTIVE | → ACTIVE | → ACTIVE | → CLOSED |
| CLOSED | ✗ OUTCOME_TRACKER_INVALID_STATE_TRANSITION | ✗ OUTCOME_TRACKER_INVALID_STATE_TRANSITION | ✗ OUTCOME_TRACKER_INVALID_STATE_TRANSITION | ✗ OUTCOME_TRACKER_INVALID_STATE_TRANSITION | ✗ OUTCOME_TRACKER_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-08.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-OUTCOME-TRACKER
bc: BC04
name: Outcome Tracker
tier: T2
purpose: سلسلة قياسات لنتيجة خطة مقابل هدفها
states:
- ACTIVE
- CLOSED
terminal:
- CLOSED
invariants:
- 'INV-OUT-01: measurements are bitemporal records; corrections never overwrite'
- 'INV-OUT-02: progress = latest measurement known at K vs target valid at T'
entities:
- Measurement (value, unit, measured_at, source, recorded_from/to)
- TargetHistory
requirements:
- REQ-OPS-013
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: SYS:outcome baselined
  to: ACTIVE
  guard: one tracker per (plan, outcome id); target copied from baseline
  event: EVT-OUT-TRACKER-CREATED
  guard_error: null
- from:
  - ACTIVE
  command: SYS:target changed by new baseline
  to: '='
  guard: target history appended (valid time = baseline time)
  event: EVT-OUT-TARGET-CHANGED
  guard_error: null
- from:
  - ACTIVE
  command: CMD-OUT-RECORD
  to: '='
  guard: value with unit convertible to metric unit (UCUM); measured_at; source =
    manual | task result | observation ref
  event: EVT-OUT-MEASURED
  guard_error: MEASUREMENT_INVALID
- from:
  - ACTIVE
  command: CMD-OUT-CORRECT
  to: '='
  guard: 'corrects a measurement: previous record closed (recorded_to), corrected
    record added — no overwrite'
  event: EVT-OUT-MEASUREMENT-CORRECTED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  command: SYS:plan closed or cancelled
  to: CLOSED
  guard: system
  event: EVT-OUT-TRACKER-CLOSED
  guard_error: null
```

</details>
