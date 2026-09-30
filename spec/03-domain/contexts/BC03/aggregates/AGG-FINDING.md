---
id: AGG-FINDING
type: aggregate
title: Finding
wave: W4
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC03
importance_tier: T1
personal_data: false
traces:
  satisfies:
  - REQ-ANL-005
  - REQ-INF-035
  state_machine: SM-FINDING
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-FINDING — Finding

**الغرض:** نتيجة تحليلية مستخلصة من تشغيلات أو أدلة  
**السياق:** BC03 · **المستوى:** T1 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-FND-01** — an ACCEPTED finding is immutable
- **INV-FND-02** — every finding traces to runs or evidence (lineage)

## مكونات داخلية

- FindingSource (run_urn | evidence_urn)

## الحالات

- غير نهائية: DRAFT, ACCEPTED
- نهائية: WITHDRAWN
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-FND-RECORD | DRAFT | statement; ≥ 1 source among SUCCEEDED runs of the case or selected evidence; uncertainty; label ≥ sources | EVT-FND-RECORDED | FINDING_INVALID |
| DRAFT | CMD-FND-EDIT | (بلا تغيير) | same rules; new version | EVT-FND-EDITED | FINDING_INVALID |
| DRAFT | CMD-FND-ACCEPT | ACCEPTED | reviewer ≠ author (peer review) | EVT-FND-ACCEPTED | SEGREGATION_OF_DUTIES |
| DRAFT, ACCEPTED | CMD-FND-WITHDRAW | WITHDRAWN | reason; assessments citing it are flagged for review | EVT-FND-WITHDRAWN | REASON_REQUIRED |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-FND-RECORD | CMD-FND-EDIT | CMD-FND-ACCEPT | CMD-FND-WITHDRAW |
|---|---|---|---|---|
| ∅ | → DRAFT | — | — | — |
| DRAFT | ✗ FINDING_INVALID_STATE_TRANSITION | → DRAFT | → ACCEPTED | → WITHDRAWN |
| ACCEPTED | ✗ FINDING_INVALID_STATE_TRANSITION | ✗ FINDING_INVALID_STATE_TRANSITION | ✗ FINDING_INVALID_STATE_TRANSITION | → WITHDRAWN |
| WITHDRAWN | ✗ FINDING_INVALID_STATE_TRANSITION | ✗ FINDING_INVALID_STATE_TRANSITION | ✗ FINDING_INVALID_STATE_TRANSITION | ✗ FINDING_INVALID_STATE_TRANSITION |

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
id: AGG-FINDING
bc: BC03
name: Finding
tier: T1
purpose: نتيجة تحليلية مستخلصة من تشغيلات أو أدلة
states:
- DRAFT
- ACCEPTED
- WITHDRAWN
terminal:
- WITHDRAWN
invariants:
- 'INV-FND-01: an ACCEPTED finding is immutable'
- 'INV-FND-02: every finding traces to runs or evidence (lineage)'
entities:
- FindingSource (run_urn | evidence_urn)
requirements:
- REQ-ANL-005
- REQ-INF-035
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-FND-RECORD
  to: DRAFT
  guard: statement; ≥ 1 source among SUCCEEDED runs of the case or selected evidence;
    uncertainty; label ≥ sources
  event: EVT-FND-RECORDED
  guard_error: FINDING_INVALID
- from:
  - DRAFT
  command: CMD-FND-EDIT
  to: '='
  guard: same rules; new version
  event: EVT-FND-EDITED
  guard_error: FINDING_INVALID
- from:
  - DRAFT
  command: CMD-FND-ACCEPT
  to: ACCEPTED
  guard: reviewer ≠ author (peer review)
  event: EVT-FND-ACCEPTED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - DRAFT
  - ACCEPTED
  command: CMD-FND-WITHDRAW
  to: WITHDRAWN
  guard: reason; assessments citing it are flagged for review
  event: EVT-FND-WITHDRAWN
  guard_error: REASON_REQUIRED
```

</details>
