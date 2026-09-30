---
id: AGG-ANALYSIS-RUN
type: aggregate
title: Analysis Run
wave: W4
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC03
importance_tier: T1 results / T2 lifecycle
personal_data: false
traces:
  satisfies:
  - REQ-ANL-002
  - REQ-ANL-003
  - REQ-ANL-004
  - REQ-INF-035
  state_machine: SM-ANALYSIS-RUN
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ANALYSIS-RUN — Analysis Run

**الغرض:** تنفيذ طريقة على مدخلات مثبتة، كمهمة غير متزامنة  
**السياق:** BC03 · **المستوى:** T1 results / T2 lifecycle · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-RUN-01** — inputs are pinned by known_at, so re-execution sees exactly the same data (REQ-ANL-003)
- **INV-RUN-02** — a run reads only what its submitter may see; results label ≥ max input label
- **INV-RUN-03** — a reproduction compares result hashes and reports REPRODUCED or DIFFERENT with the differing inputs/method/environment
- **INV-RUN-04** — SUCCEEDED results are immutable

## مكونات داخلية

- InputPin (ref, known_at, filters)
- StepLog
- ResultArtifact (hash, kind)
- ReproductionReport

## الحالات

- غير نهائية: QUEUED, RUNNING
- نهائية: SUCCEEDED, FAILED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-RUN-SUBMIT | QUEUED | case OPEN; method ACTIVE; parameters valid against schema; inputs pinned (dataset refs with known_at = submission time, filters, layers, extent, time window, assumptions); run label ≥ max input label; tenant job quota | EVT-RUN-QUEUED | RUN_INVALID |
| ∅ (إنشاء) | CMD-RUN-REPRODUCE | QUEUED | source run SUCCEEDED; reproducer cleared for source run label; method version ACTIVE or DEPRECATED; copies inputs/parameters/seed exactly | EVT-RUN-QUEUED | REPRODUCTION_NOT_ALLOWED |
| QUEUED | SYS:worker lease acquired | RUNNING | executes with the submitter's authorization (visibility), never with system privileges | EVT-RUN-STARTED | — |
| RUNNING | SYS:completed | SUCCEEDED | results stored as hashed artifacts; steps log; lineage record written (inputs+known_at, method version, image digest, parameters, seed, actor, times) | EVT-RUN-SUCCEEDED | — |
| RUNNING | SYS:error or timeout | FAILED | error recorded; partial artifacts discarded | EVT-RUN-FAILED | — |
| QUEUED, RUNNING | CMD-RUN-CANCEL | CANCELLED | submitter or case owner; reason | EVT-RUN-CANCELLED | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-RUN-SUBMIT | CMD-RUN-REPRODUCE | SYS:worker lease acquired | SYS:completed | SYS:error or timeout | CMD-RUN-CANCEL |
|---|---|---|---|---|---|---|
| ∅ | → QUEUED | → QUEUED | — | — | — | — |
| QUEUED | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | → RUNNING | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | → CANCELLED |
| RUNNING | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | → SUCCEEDED | → FAILED | → CANCELLED |
| SUCCEEDED | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION |
| FAILED | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION | ✗ ANALYSIS_RUN_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-07.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-ANALYSIS-RUN
bc: BC03
name: Analysis Run
tier: T1 results / T2 lifecycle
purpose: تنفيذ طريقة على مدخلات مثبتة، كمهمة غير متزامنة
states:
- QUEUED
- RUNNING
- SUCCEEDED
- FAILED
- CANCELLED
terminal:
- SUCCEEDED
- FAILED
- CANCELLED
invariants:
- 'INV-RUN-01: inputs are pinned by known_at, so re-execution sees exactly the same
  data (REQ-ANL-003)'
- 'INV-RUN-02: a run reads only what its submitter may see; results label ≥ max input
  label'
- 'INV-RUN-03: a reproduction compares result hashes and reports REPRODUCED or DIFFERENT
  with the differing inputs/method/environment'
- 'INV-RUN-04: SUCCEEDED results are immutable'
entities:
- InputPin (ref, known_at, filters)
- StepLog
- ResultArtifact (hash, kind)
- ReproductionReport
requirements:
- REQ-ANL-002
- REQ-ANL-003
- REQ-ANL-004
- REQ-INF-035
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-RUN-SUBMIT
  to: QUEUED
  guard: case OPEN; method ACTIVE; parameters valid against schema; inputs pinned
    (dataset refs with known_at = submission time, filters, layers, extent, time window,
    assumptions); run label ≥ max input label; tenant job quota
  event: EVT-RUN-QUEUED
  guard_error: RUN_INVALID
- from: ∅
  command: CMD-RUN-REPRODUCE
  to: QUEUED
  guard: source run SUCCEEDED; reproducer cleared for source run label; method version
    ACTIVE or DEPRECATED; copies inputs/parameters/seed exactly
  event: EVT-RUN-QUEUED
  guard_error: REPRODUCTION_NOT_ALLOWED
- from:
  - QUEUED
  command: SYS:worker lease acquired
  to: RUNNING
  guard: executes with the submitter's authorization (visibility), never with system
    privileges
  event: EVT-RUN-STARTED
  guard_error: null
- from:
  - RUNNING
  command: SYS:completed
  to: SUCCEEDED
  guard: results stored as hashed artifacts; steps log; lineage record written (inputs+known_at,
    method version, image digest, parameters, seed, actor, times)
  event: EVT-RUN-SUCCEEDED
  guard_error: null
- from:
  - RUNNING
  command: SYS:error or timeout
  to: FAILED
  guard: error recorded; partial artifacts discarded
  event: EVT-RUN-FAILED
  guard_error: null
- from:
  - QUEUED
  - RUNNING
  command: CMD-RUN-CANCEL
  to: CANCELLED
  guard: submitter or case owner; reason
  event: EVT-RUN-CANCELLED
  guard_error: REASON_REQUIRED
```

</details>
