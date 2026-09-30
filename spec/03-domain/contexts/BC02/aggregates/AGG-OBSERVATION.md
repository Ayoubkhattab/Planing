---
id: AGG-OBSERVATION
type: aggregate
title: Observation
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
  - REQ-INF-002
  - REQ-INF-028
  state_machine: SM-OBSERVATION
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-OBSERVATION — Observation

**الغرض:** ما رصده مصدر في زمن ومكان؛ غير قابل للتعديل بعد الاعتماد  
**السياق:** BC02 · **المستوى:** T1 · **بيانات شخصية:** لا

> High-rate feeds send CMD-OBS-RECORD in batches of ≤ 1,000 items, each with its own idempotency key (QAS-PERF-012).

## الثوابت (Invariants)

- **INV-OBS-01** — recorded_from is server-assigned; observed_at comes from the source/device
- **INV-OBS-02** — content is immutable once VALIDATED or REJECTED (reclassification versions the label only)
- **INV-OBS-03** — every derived claim references the observation in lineage
- **INV-OBS-04** — device clock skew > 5 min adds data_quality issue DEVICE_CLOCK_SUSPECT

## مكونات داخلية

- Measurement (quantity, value, UCUM unit, uncertainty)
- Location (spatial envelope)

## الحالات

- غير نهائية: RECORDED
- نهائية: VALIDATED, REJECTED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-OBS-RECORD | RECORDED | source ACTIVE; location with CRS + accuracy + valid geometry; UCUM units; observed_at ≤ server time + 5 min; recorded_from by server | EVT-OBS-RECORDED | OBSERVATION_INVALID |
| RECORDED | CMD-OBS-AMEND | (بلا تغيير) | actor = observer or Analyst; new version; reason | EVT-OBS-AMENDED | REASON_REQUIRED |
| RECORDED | CMD-OBS-ATTACH-EVIDENCE | (بلا تغيير) | evidence REGISTERED or SEALED | EVT-OBS-EVIDENCE-ATTACHED | EVIDENCE_INVALID |
| RECORDED, VALIDATED, REJECTED | CMD-OBS-RECLASSIFY | (بلا تغيير) | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version | EVT-OBS-RECLASSIFIED | CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| RECORDED | CMD-OBS-VALIDATE | VALIDATED | Analyst ≠ observer, or system auto-validation for sensor sources rated A/B under tenant policy | EVT-OBS-VALIDATED | SEGREGATION_OF_DUTIES |
| RECORDED | CMD-OBS-REJECT | REJECTED | reason | EVT-OBS-REJECTED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-OBS-RECORD | CMD-OBS-AMEND | CMD-OBS-ATTACH-EVIDENCE | CMD-OBS-RECLASSIFY | CMD-OBS-VALIDATE | CMD-OBS-REJECT |
|---|---|---|---|---|---|---|
| ∅ | → RECORDED | — | — | — | — | — |
| RECORDED | ✗ OBSERVATION_INVALID_STATE_TRANSITION | → RECORDED | → RECORDED | → RECORDED | → VALIDATED | → REJECTED |
| VALIDATED | ✗ OBSERVATION_INVALID_STATE_TRANSITION | ✗ OBSERVATION_INVALID_STATE_TRANSITION | ✗ OBSERVATION_INVALID_STATE_TRANSITION | → VALIDATED | ✗ OBSERVATION_INVALID_STATE_TRANSITION | ✗ OBSERVATION_INVALID_STATE_TRANSITION |
| REJECTED | ✗ OBSERVATION_INVALID_STATE_TRANSITION | ✗ OBSERVATION_INVALID_STATE_TRANSITION | ✗ OBSERVATION_INVALID_STATE_TRANSITION | → REJECTED | ✗ OBSERVATION_INVALID_STATE_TRANSITION | ✗ OBSERVATION_INVALID_STATE_TRANSITION |

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
id: AGG-OBSERVATION
bc: BC02
name: Observation
tier: T1
purpose: ما رصده مصدر في زمن ومكان؛ غير قابل للتعديل بعد الاعتماد
states:
- RECORDED
- VALIDATED
- REJECTED
terminal:
- VALIDATED
- REJECTED
invariants:
- 'INV-OBS-01: recorded_from is server-assigned; observed_at comes from the source/device'
- 'INV-OBS-02: content is immutable once VALIDATED or REJECTED (reclassification versions
  the label only)'
- 'INV-OBS-03: every derived claim references the observation in lineage'
- 'INV-OBS-04: device clock skew > 5 min adds data_quality issue DEVICE_CLOCK_SUSPECT'
entities:
- Measurement (quantity, value, UCUM unit, uncertainty)
- Location (spatial envelope)
requirements:
- REQ-INF-002
- REQ-INF-028
notes: High-rate feeds send CMD-OBS-RECORD in batches of ≤ 1,000 items, each with
  its own idempotency key (QAS-PERF-012).
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-OBS-RECORD
  to: RECORDED
  guard: source ACTIVE; location with CRS + accuracy + valid geometry; UCUM units;
    observed_at ≤ server time + 5 min; recorded_from by server
  event: EVT-OBS-RECORDED
  guard_error: OBSERVATION_INVALID
- from:
  - RECORDED
  command: CMD-OBS-AMEND
  to: '='
  guard: actor = observer or Analyst; new version; reason
  event: EVT-OBS-AMENDED
  guard_error: REASON_REQUIRED
- from:
  - RECORDED
  command: CMD-OBS-ATTACH-EVIDENCE
  to: '='
  guard: evidence REGISTERED or SEALED
  event: EVT-OBS-EVIDENCE-ATTACHED
  guard_error: EVIDENCE_INVALID
- from:
  - RECORDED
  - VALIDATED
  - REJECTED
  command: CMD-OBS-RECLASSIFY
  to: '='
  guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
  event: EVT-OBS-RECLASSIFIED
  guard_error: CLASSIFICATION_CHANGE_NOT_AUTHORIZED
- from:
  - RECORDED
  command: CMD-OBS-VALIDATE
  to: VALIDATED
  guard: Analyst ≠ observer, or system auto-validation for sensor sources rated A/B
    under tenant policy
  event: EVT-OBS-VALIDATED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - RECORDED
  command: CMD-OBS-REJECT
  to: REJECTED
  guard: reason
  event: EVT-OBS-REJECTED
  guard_error: REASON_REQUIRED
```

</details>
