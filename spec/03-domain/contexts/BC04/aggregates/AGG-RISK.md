---
id: AGG-RISK
type: aggregate
title: Risk
wave: W4
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC04
importance_tier: T2
personal_data: false
traces:
  satisfies:
  - REQ-RCM-001
  - REQ-RCM-002
  - REQ-RCM-003
  - REQ-RCM-004
  - REQ-RCM-005
  state_machine: SM-RISK
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-RISK — Risk

**الغرض:** تسجيل وتقييم ومعالجة مخاطر محتملة قبل وقوعها (استباقي، لا حادثة فعلية)  
**السياق:** BC04 · **المستوى:** T2 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-RIS-01** — المقيّم ≠ المحدِّد عند سياسة المستأجر لفصل الواجبات (يماثل INV-TASK-07)
- **INV-RIS-02** — risk_score = likelihood × impact، محسوب عند كل تقييم، لا يُدخله الفاعل مباشرة
- **INV-RIS-03** — TREATED يتطلب ≥ 1 إجراء معالجة مرتبط إلا إذا كانت الاستراتيجية accept بموافقة مخوَّلة صريحة
- **INV-RIS-04** — CLOSED يتطلب rationale صريحاً دائماً؛ لا يوجد أمر لإعادة فتح خطر مُغلَق — إعادة تحديده تنشئ Risk جديداً
- **INV-RIS-05** — ربط حادثة متحقِّقة بهذا الخطر (risk_ref) لا يغيّر حالة الخطر تلقائياً أبداً؛ مالك الخطر يتصرف بأمر منفصل (لا أثر جانبي صامت — درس SLC-09)

## مكونات داخلية

- TreatmentAction (treatment_task_ref, status)

## الحالات

- غير نهائية: IDENTIFIED, ASSESSED, TREATED
- نهائية: CLOSED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-RIS-IDENTIFY | IDENTIFIED | category_ref (RD-HAZARD-CATEGORIES، مرجع لكل مستأجر — نمط R2-Q1)؛ description؛ scope_refs ≥ 1 (أصل/منطقة/منظمة/خطة)؛ label ≥ تصنيف النطاق | EVT-RIS-IDENTIFIED | RISK_INVALID |
| IDENTIFIED | CMD-RIS-ASSESS | ASSESSED | likelihood ∈ 1..5؛ impact ∈ 1..5؛ risk_score محسوب لا يُدخَل مباشرة (INV-RIS-02)؛ المقيّم ≠ المحدِّد عند سياسة فصل الواجبات (INV-RIS-01) | EVT-RIS-ASSESSED | SEGREGATION_OF_DUTIES |
| ASSESSED | CMD-RIS-PLAN-TREATMENT | TREATED | treatment_strategy ∈ {avoid,reduce,transfer,accept}؛ ≥ 1 إجراء معالجة إلا عند accept (INV-RIS-03)؛ موافق مخوَّل | EVT-RIS-TREATMENT-PLANNED | TREATMENT_INVALID |
| ASSESSED, TREATED | CMD-RIS-REASSESS | ASSESSED | likelihood/impact جديدان؛ سبب؛ المقيّم ≠ المحدِّد عند سياسة فصل الواجبات | EVT-RIS-REASSESSED | SEGREGATION_OF_DUTIES |
| IDENTIFIED, ASSESSED, TREATED | CMD-RIS-CLOSE | CLOSED | rationale ∈ {retired,accepted_permanently,materialized}؛ إن كان materialized فـ incident_ref إلزامي (INV-RIS-04)؛ لا أمر لإعادة الفتح — الخطر المُعاد تحديده خطر جديد | EVT-RIS-CLOSED | RATIONALE_REQUIRED |
| أي حالة غير نهائية | SYS:incident references this risk as risk_ref | (بلا تغيير) | رابط تلقائي عند تسجيل حادثة تحقَّق منها هذا الخطر؛ لا يغيّر حالة الخطر تلقائياً أبداً (INV-RIS-05) | EVT-RIS-MATERIALIZATION-LINKED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-RIS-IDENTIFY | CMD-RIS-ASSESS | CMD-RIS-PLAN-TREATMENT | CMD-RIS-REASSESS | CMD-RIS-CLOSE | SYS:incident references this risk as risk_ref |
|---|---|---|---|---|---|---|
| ∅ | → IDENTIFIED | — | — | — | — | — |
| IDENTIFIED | ✗ RISK_INVALID_STATE_TRANSITION | → ASSESSED | ✗ RISK_INVALID_STATE_TRANSITION | ✗ RISK_INVALID_STATE_TRANSITION | → CLOSED | → IDENTIFIED |
| ASSESSED | ✗ RISK_INVALID_STATE_TRANSITION | ✗ RISK_INVALID_STATE_TRANSITION | → TREATED | → ASSESSED | → CLOSED | → ASSESSED |
| TREATED | ✗ RISK_INVALID_STATE_TRANSITION | ✗ RISK_INVALID_STATE_TRANSITION | ✗ RISK_INVALID_STATE_TRANSITION | → ASSESSED | → CLOSED | → TREATED |
| CLOSED | ✗ RISK_INVALID_STATE_TRANSITION | ✗ RISK_INVALID_STATE_TRANSITION | ✗ RISK_INVALID_STATE_TRANSITION | ✗ RISK_INVALID_STATE_TRANSITION | ✗ RISK_INVALID_STATE_TRANSITION | ✗ RISK_INVALID_STATE_TRANSITION |

## التزامن وعدم التكرار

- Optimistic concurrency: `If-Match: <version>`؛ عدم التطابق → `VERSION_CONFLICT` (HTTP 409) دون تغيير.
- كل أمر يحمل `Idempotency-Key`؛ التكرار يعيد النتيجة الأصلية؛ نفس المفتاح بحمولة مختلفة → `IDEMPOTENCY_KEY_REUSED` (HTTP 422).
- الأوامر التي تبدأ بـ `SYS:` يطلقها المجدول بهوية عبء عمل، وتخضع لنفس الثوابت.

## الحفظ

- State + history (إصدار غير قابل للتعديل لكل تغيير، ADR-P02) + outbox + audit outbox في نفس المعاملة (FIT-04).
- النموذج المنطقي: `06-data/logical-model/slc-17.md`.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
id: AGG-RISK
bc: BC04
name: Risk
tier: T2
purpose: تسجيل وتقييم ومعالجة مخاطر محتملة قبل وقوعها (استباقي، لا حادثة فعلية)
states:
- IDENTIFIED
- ASSESSED
- TREATED
- CLOSED
terminal:
- CLOSED
invariants:
- 'INV-RIS-01: المقيّم ≠ المحدِّد عند سياسة المستأجر لفصل الواجبات (يماثل INV-TASK-07)'
- 'INV-RIS-02: risk_score = likelihood × impact، محسوب عند كل تقييم، لا يُدخله الفاعل
  مباشرة'
- 'INV-RIS-03: TREATED يتطلب ≥ 1 إجراء معالجة مرتبط إلا إذا كانت الاستراتيجية accept
  بموافقة مخوَّلة صريحة'
- 'INV-RIS-04: CLOSED يتطلب rationale صريحاً دائماً؛ لا يوجد أمر لإعادة فتح خطر مُغلَق
  — إعادة تحديده تنشئ Risk جديداً'
- 'INV-RIS-05: ربط حادثة متحقِّقة بهذا الخطر (risk_ref) لا يغيّر حالة الخطر تلقائياً
  أبداً؛ مالك الخطر يتصرف بأمر منفصل (لا أثر جانبي صامت — درس SLC-09)'
entities:
- TreatmentAction (treatment_task_ref, status)
requirements:
- REQ-RCM-001
- REQ-RCM-002
- REQ-RCM-003
- REQ-RCM-004
- REQ-RCM-005
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-RIS-IDENTIFY
  to: IDENTIFIED
  guard: category_ref (RD-HAZARD-CATEGORIES، مرجع لكل مستأجر — نمط R2-Q1)؛ description؛
    scope_refs ≥ 1 (أصل/منطقة/منظمة/خطة)؛ label ≥ تصنيف النطاق
  event: EVT-RIS-IDENTIFIED
  guard_error: RISK_INVALID
- from:
  - IDENTIFIED
  command: CMD-RIS-ASSESS
  to: ASSESSED
  guard: likelihood ∈ 1..5؛ impact ∈ 1..5؛ risk_score محسوب لا يُدخَل مباشرة (INV-RIS-02)؛
    المقيّم ≠ المحدِّد عند سياسة فصل الواجبات (INV-RIS-01)
  event: EVT-RIS-ASSESSED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - ASSESSED
  command: CMD-RIS-PLAN-TREATMENT
  to: TREATED
  guard: treatment_strategy ∈ {avoid,reduce,transfer,accept}؛ ≥ 1 إجراء معالجة إلا
    عند accept (INV-RIS-03)؛ موافق مخوَّل
  event: EVT-RIS-TREATMENT-PLANNED
  guard_error: TREATMENT_INVALID
- from:
  - ASSESSED
  - TREATED
  command: CMD-RIS-REASSESS
  to: ASSESSED
  guard: likelihood/impact جديدان؛ سبب؛ المقيّم ≠ المحدِّد عند سياسة فصل الواجبات
  event: EVT-RIS-REASSESSED
  guard_error: SEGREGATION_OF_DUTIES
- from:
  - IDENTIFIED
  - ASSESSED
  - TREATED
  command: CMD-RIS-CLOSE
  to: CLOSED
  guard: rationale ∈ {retired,accepted_permanently,materialized}؛ إن كان materialized
    فـ incident_ref إلزامي (INV-RIS-04)؛ لا أمر لإعادة الفتح — الخطر المُعاد تحديده
    خطر جديد
  event: EVT-RIS-CLOSED
  guard_error: RATIONALE_REQUIRED
- from: '*NT'
  command: SYS:incident references this risk as risk_ref
  to: '='
  guard: رابط تلقائي عند تسجيل حادثة تحقَّق منها هذا الخطر؛ لا يغيّر حالة الخطر تلقائياً
    أبداً (INV-RIS-05)
  event: EVT-RIS-MATERIALIZATION-LINKED
  guard_error: null
```

</details>
