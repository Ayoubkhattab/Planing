---
id: AGG-SENSOR-STREAM
type: aggregate
title: Sensor Stream
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC07
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-INT-002
  state_machine: SM-SENSOR-STREAM
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-SENSOR-STREAM — Sensor Stream

**الغرض:** تدفق قياسات حساس مرتبط بمصدر وكمية ووحدة وفحوص جودة  
**السياق:** BC07 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-SNS-01** — sensor readings enter only as observations through BC02 batch commands (≤ 1,000 per batch, per-item idempotency) — REQ-INT-002
- **INV-SNS-02** — quality violations annotate data quality; they never silently drop readings
- **INV-SNS-03** — readings carry the sensor's own time as observed_at and server receipt as recorded_from

## مكونات داخلية

- QualityRules

## الحالات

- غير نهائية: DRAFT, ACTIVE, PAUSED
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-SNS-REGISTER | DRAFT | connection (sensor_gateway) exists; BC02 Source of type sensor ACTIVE; quantity + UCUM unit; expected rate; location or linked entity | EVT-SNS-REGISTERED | STREAM_INVALID |
| DRAFT, ACTIVE, PAUSED | CMD-SNS-SET-QUALITY-RULES | (بلا تغيير) | range, rate-of-change, stale-after, duplicate window; violations become data_quality issues, not rejections | EVT-SNS-QUALITY-RULES-SET | QUALITY_RULES_INVALID |
| DRAFT, PAUSED | CMD-SNS-ACTIVATE | ACTIVE | connection ACTIVE; mapping to CMD-OBS-RECORD batches tested | EVT-SNS-ACTIVATED | CONNECTION_NOT_ACTIVE |
| ACTIVE | CMD-SNS-PAUSE | PAUSED | reason | EVT-SNS-PAUSED | REASON_REQUIRED |
| ACTIVE | SYS:no data beyond stale-after | (بلا تغيير) | stream flagged STALE; alert to owner | EVT-SNS-STALE | — |
| DRAFT, PAUSED | CMD-SNS-RETIRE | RETIRED | reason | EVT-SNS-RETIRED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-SNS-REGISTER | CMD-SNS-SET-QUALITY-RULES | CMD-SNS-ACTIVATE | CMD-SNS-PAUSE | SYS:no data beyond stale-after | CMD-SNS-RETIRE |
|---|---|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — | — | — |
| DRAFT | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | → DRAFT | → ACTIVE | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | → RETIRED |
| ACTIVE | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | → ACTIVE | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | → PAUSED | → ACTIVE | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION |
| PAUSED | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | → PAUSED | → ACTIVE | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | → RETIRED |
| RETIRED | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION | ✗ SENSOR_STREAM_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-16.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-SENSOR-STREAM
bc: BC07
name: Sensor Stream
tier: T2
purpose: تدفق قياسات حساس مرتبط بمصدر وكمية ووحدة وفحوص جودة
states:
- DRAFT
- ACTIVE
- PAUSED
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-SNS-01: sensor readings enter only as observations through BC02 batch commands
  (≤ 1,000 per batch, per-item idempotency) — REQ-INT-002'
- 'INV-SNS-02: quality violations annotate data quality; they never silently drop
  readings'
- 'INV-SNS-03: readings carry the sensor''s own time as observed_at and server receipt
  as recorded_from'
entities:
- QualityRules
requirements:
- REQ-INT-002
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-SNS-REGISTER
  to: DRAFT
  guard: connection (sensor_gateway) exists; BC02 Source of type sensor ACTIVE; quantity
    + UCUM unit; expected rate; location or linked entity
  event: EVT-SNS-REGISTERED
  guard_error: STREAM_INVALID
- from:
  - DRAFT
  - ACTIVE
  - PAUSED
  command: CMD-SNS-SET-QUALITY-RULES
  to: '='
  guard: range, rate-of-change, stale-after, duplicate window; violations become data_quality
    issues, not rejections
  event: EVT-SNS-QUALITY-RULES-SET
  guard_error: QUALITY_RULES_INVALID
- from:
  - DRAFT
  - PAUSED
  command: CMD-SNS-ACTIVATE
  to: ACTIVE
  guard: connection ACTIVE; mapping to CMD-OBS-RECORD batches tested
  event: EVT-SNS-ACTIVATED
  guard_error: CONNECTION_NOT_ACTIVE
- from:
  - ACTIVE
  command: CMD-SNS-PAUSE
  to: PAUSED
  guard: reason
  event: EVT-SNS-PAUSED
  guard_error: REASON_REQUIRED
- from:
  - ACTIVE
  command: SYS:no data beyond stale-after
  to: '='
  guard: stream flagged STALE; alert to owner
  event: EVT-SNS-STALE
  guard_error: null
- from:
  - DRAFT
  - PAUSED
  command: CMD-SNS-RETIRE
  to: RETIRED
  guard: reason
  event: EVT-SNS-RETIRED
  guard_error: REASON_REQUIRED
```

</details>
