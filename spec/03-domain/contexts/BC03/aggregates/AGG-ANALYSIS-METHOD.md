---
id: AGG-ANALYSIS-METHOD
type: aggregate
title: Analysis Method Version
wave: W4
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC03
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-ANL-002
  - REQ-ANL-003
  state_machine: SM-ANALYSIS-METHOD
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-ANALYSIS-METHOD — Analysis Method Version

**الغرض:** طريقة تحليل بإصدار وبيئة تنفيذ ثابتة  
**السياق:** BC03 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-AMT-01** — a method version is immutable (image digest, parameter schema, code)
- **INV-AMT-02** — a version backing published work stays executable (DEPRECATED at most)

## مكونات داخلية

- ParameterSchema
- ExecutionImage (digest)

## الحالات

- غير نهائية: DRAFT, ACTIVE, DEPRECATED
- نهائية: RETIRED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-AMT-REGISTER | DRAFT | code + version unique; parameter JSON schema; execution image digest from internal registry; deterministic flag | EVT-AMT-REGISTERED | METHOD_INVALID |
| DRAFT | CMD-AMT-ACTIVATE | ACTIVE | validation suite passed; approver ≠ author | EVT-AMT-ACTIVATED | SEGREGATION_OF_DUTIES |
| ACTIVE | CMD-AMT-DEPRECATE | DEPRECATED | reason; no new runs; reproduction still allowed | EVT-AMT-DEPRECATED | REASON_REQUIRED |
| DEPRECATED | CMD-AMT-RETIRE | RETIRED | no run of this version backs a PUBLISHED or SUPERSEDED assessment (reproducibility preserved) | EVT-AMT-RETIRED | METHOD_BACKS_PUBLISHED_WORK |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-AMT-REGISTER | CMD-AMT-ACTIVATE | CMD-AMT-DEPRECATE | CMD-AMT-RETIRE |
|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — |
| DRAFT | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION | → ACTIVE | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
| ACTIVE | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION | → DEPRECATED | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
| DEPRECATED | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION | → RETIRED |
| RETIRED | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION | ✗ ANALYSIS_METHOD_INVALID_STATE_TRANSITION |

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
id: AGG-ANALYSIS-METHOD
bc: BC03
name: Analysis Method Version
tier: T2
purpose: طريقة تحليل بإصدار وبيئة تنفيذ ثابتة
states:
- DRAFT
- ACTIVE
- DEPRECATED
- RETIRED
terminal:
- RETIRED
invariants:
- 'INV-AMT-01: a method version is immutable (image digest, parameter schema, code)'
- 'INV-AMT-02: a version backing published work stays executable (DEPRECATED at most)'
entities:
- ParameterSchema
- ExecutionImage (digest)
requirements:
- REQ-ANL-002
- REQ-ANL-003
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-AMT-REGISTER
  to: DRAFT
  guard: code + version unique; parameter JSON schema; execution image digest from
    internal registry; deterministic flag
  event: EVT-AMT-REGISTERED
  guard_error: METHOD_INVALID
- from:
  - DRAFT
  command: CMD-AMT-ACTIVATE
  to: ACTIVE
  guard: validation suite passed; approver ≠ author
  event: EVT-AMT-ACTIVATED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - ACTIVE
  command: CMD-AMT-DEPRECATE
  to: DEPRECATED
  guard: reason; no new runs; reproduction still allowed
  event: EVT-AMT-DEPRECATED
  guard_error: REASON_REQUIRED
- from:
  - DEPRECATED
  command: CMD-AMT-RETIRE
  to: RETIRED
  guard: no run of this version backs a PUBLISHED or SUPERSEDED assessment (reproducibility
    preserved)
  event: EVT-AMT-RETIRED
  guard_error: METHOD_BACKS_PUBLISHED_WORK
```

</details>
