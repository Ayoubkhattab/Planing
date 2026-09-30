---
id: CMD-CAT-BC04-SLC17
type: command-catalog
title: Commands — BC04 (SLC-17)
wave: W4
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC04 (SLC-17)

_15 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-RIS-IDENTIFY | AGG-RISK | `POST /api/v1/operations/risks` | لا | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق) | POL-RIS-IDENTIFY | `category_ref!:urn description!:LocalizedName scope_refs!:array label!:Label` | EVT-RIS-IDENTIFIED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RISK_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RIS-ASSESS | AGG-RISK | `POST /api/v1/operations/risks/{id}/actions/assess` | لا | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق) | POL-RIS-ASSESS | `likelihood!:integer impact!:integer` | EVT-RIS-ASSESSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RISK_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RIS-PLAN-TREATMENT | AGG-RISK | `POST /api/v1/operations/risks/{id}/actions/plan-treatment` | لا | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق) | POL-RIS-PLAN-TREATMENT | `treatment_strategy!:enum(avoid,reduce,transfer,accept) treatment_task_refs:array approver!:urn` | EVT-RIS-TREATMENT-PLANNED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RISK_INVALID_STATE_TRANSITION, TREATMENT_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RIS-REASSESS | AGG-RISK | `POST /api/v1/operations/risks/{id}/actions/reassess` | لا | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق) | POL-RIS-REASSESS | `likelihood!:integer impact!:integer reason!:string` | EVT-RIS-REASSESSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RISK_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RIS-CLOSE | AGG-RISK | `POST /api/v1/operations/risks/{id}/actions/close` | لا | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق) | POL-RIS-CLOSE | `rationale!:enum(retired,accepted_permanently,materialized) incident_ref:urn` | EVT-RIS-CLOSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RATIONALE_REQUIRED, RISK_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-INC-REPORT | AGG-INCIDENT | `POST /api/v1/operations/incidents` | لا | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-REPORT | `category_ref!:urn description!:LocalizedName scope_refs!:array risk_ref:urn label!:Label` | EVT-INC-REPORTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INCIDENT_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-INC-ASSESS | AGG-INCIDENT | `POST /api/v1/operations/incidents/{id}/actions/assess` | لا | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-ASSESS | `severity!:enum(MINOR,MAJOR,EMERGENCY,CRISIS) affected_scope_refs!:array` | EVT-INC-ASSESSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INCIDENT_INVALID, INCIDENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-INC-DISPATCH-RESPONSE | AGG-INCIDENT | `POST /api/v1/operations/incidents/{id}/actions/dispatch-response` | لا | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-DISPATCH-RESPONSE | `commander!:urn response_task_refs!:array` | EVT-INC-RESPONSE-DISPATCHED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INCIDENT_INVALID_STATE_TRANSITION, RESPONSE_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-INC-CONTAIN | AGG-INCIDENT | `POST /api/v1/operations/incidents/{id}/actions/contain` | لا | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-CONTAIN | `containment_note!:string` | EVT-INC-CONTAINED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INCIDENT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-INC-RESOLVE | AGG-INCIDENT | `POST /api/v1/operations/incidents/{id}/actions/resolve` | لا | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-RESOLVE | `resolution_note!:string` | EVT-INC-RESOLVED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INCIDENT_INVALID_STATE_TRANSITION, RESPONSE_TASKS_OPEN, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-INC-CLOSE | AGG-INCIDENT | `POST /api/v1/operations/incidents/{id}/actions/close` | لا | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-CLOSE | `closing_note!:string after_action_ref:urn` | EVT-INC-CLOSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INCIDENT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-INC-CANCEL | AGG-INCIDENT | `POST /api/v1/operations/incidents/{id}/actions/cancel` | لا | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-CANCEL | `reason!:string` | EVT-INC-CANCELLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INCIDENT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-INC-ESCALATE | AGG-INCIDENT | `POST /api/v1/operations/incidents/{id}/actions/escalate` | لا | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-ESCALATE | `reason!:string new_severity!:enum(MINOR,MAJOR,EMERGENCY,CRISIS)` | EVT-INC-ESCALATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INCIDENT_INVALID_STATE_TRANSITION, SEVERITY_MUST_INCREASE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-INC-DE-ESCALATE | AGG-INCIDENT | `POST /api/v1/operations/incidents/{id}/actions/de-escalate` | لا | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-DE-ESCALATE | `reason!:string new_severity!:enum(MINOR,MAJOR,EMERGENCY,CRISIS)` | EVT-INC-DE-ESCALATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INCIDENT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-INC-ACTIVATE-CONTINGENCY | AGG-INCIDENT | `POST /api/v1/operations/incidents/{id}/actions/activate-contingency` | لا | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية) | POL-INC-ACTIVATE-CONTINGENCY | `plan_template_ref!:urn` | EVT-INC-CONTINGENCY-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, INCIDENT_INVALID_STATE_TRANSITION, PLAN_LINK_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-RIS-IDENTIFY
  aggregate: AGG-RISK
  bc: BC04
  transitions:
  - from:
    - ∅
    to: IDENTIFIED
    guard: category_ref (RD-HAZARD-CATEGORIES، مرجع لكل مستأجر — نمط R2-Q1)؛ description؛
      scope_refs ≥ 1 (أصل/منطقة/منظمة/خطة)؛ label ≥ تصنيف النطاق
    event: EVT-RIS-IDENTIFIED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RISK_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/operations/risks
  internal: false
  policy: POL-RIS-IDENTIFY
  actors: محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط
    المعالجة) · مدير المخاطر (إغلاق)
  payload: category_ref!:urn description!:LocalizedName scope_refs!:array label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-RIS-ASSESS
  aggregate: AGG-RISK
  bc: BC04
  transitions:
  - from:
    - IDENTIFIED
    to: ASSESSED
    guard: likelihood ∈ 1..5؛ impact ∈ 1..5؛ risk_score محسوب لا يُدخَل مباشرة (INV-RIS-02)؛
      المقيّم ≠ المحدِّد عند سياسة فصل الواجبات (INV-RIS-01)
    event: EVT-RIS-ASSESSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RISK_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/risks/{id}/actions/assess
  internal: false
  policy: POL-RIS-ASSESS
  actors: محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط
    المعالجة) · مدير المخاطر (إغلاق)
  payload: likelihood!:integer impact!:integer
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RIS-PLAN-TREATMENT
  aggregate: AGG-RISK
  bc: BC04
  transitions:
  - from:
    - ASSESSED
    to: TREATED
    guard: treatment_strategy ∈ {avoid,reduce,transfer,accept}؛ ≥ 1 إجراء معالجة إلا
      عند accept (INV-RIS-03)؛ موافق مخوَّل
    event: EVT-RIS-TREATMENT-PLANNED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RISK_INVALID_STATE_TRANSITION
  - TREATMENT_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/risks/{id}/actions/plan-treatment
  internal: false
  policy: POL-RIS-PLAN-TREATMENT
  actors: محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط
    المعالجة) · مدير المخاطر (إغلاق)
  payload: treatment_strategy!:enum(avoid,reduce,transfer,accept) treatment_task_refs:array
    approver!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RIS-REASSESS
  aggregate: AGG-RISK
  bc: BC04
  transitions:
  - from:
    - ASSESSED
    - TREATED
    to: ASSESSED
    guard: likelihood/impact جديدان؛ سبب؛ المقيّم ≠ المحدِّد عند سياسة فصل الواجبات
    event: EVT-RIS-REASSESSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RISK_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/risks/{id}/actions/reassess
  internal: false
  policy: POL-RIS-REASSESS
  actors: محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط
    المعالجة) · مدير المخاطر (إغلاق)
  payload: likelihood!:integer impact!:integer reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RIS-CLOSE
  aggregate: AGG-RISK
  bc: BC04
  transitions:
  - from:
    - IDENTIFIED
    - ASSESSED
    - TREATED
    to: CLOSED
    guard: rationale ∈ {retired,accepted_permanently,materialized}؛ إن كان materialized
      فـ incident_ref إلزامي (INV-RIS-04)؛ لا أمر لإعادة الفتح — الخطر المُعاد تحديده
      خطر جديد
    event: EVT-RIS-CLOSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RATIONALE_REQUIRED
  - RISK_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/risks/{id}/actions/close
  internal: false
  policy: POL-RIS-CLOSE
  actors: محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط
    المعالجة) · مدير المخاطر (إغلاق)
  payload: rationale!:enum(retired,accepted_permanently,materialized) incident_ref:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-INC-REPORT
  aggregate: AGG-INCIDENT
  bc: BC04
  transitions:
  - from:
    - ∅
    to: REPORTED
    guard: category_ref (RD-HAZARD-CATEGORIES)؛ description؛ scope_refs ≥ 1؛ risk_ref
      اختياري (خطر تحقَّق)؛ severity ابتدائية MINOR؛ label ≥ تصنيف النطاق
    event: EVT-INC-REPORTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INCIDENT_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/operations/incidents
  internal: false
  policy: POL-INC-REPORT
  actors: أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة
    (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)
  payload: category_ref!:urn description!:LocalizedName scope_refs!:array risk_ref:urn
    label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-INC-ASSESS
  aggregate: AGG-INCIDENT
  bc: BC04
  transitions:
  - from:
    - REPORTED
    to: ASSESSED
    guard: severity ∈ {MINOR,MAJOR,EMERGENCY,CRISIS}؛ affected_scope_refs؛ مقيّم مخوَّل
    event: EVT-INC-ASSESSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INCIDENT_INVALID
  - INCIDENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/incidents/{id}/actions/assess
  internal: false
  policy: POL-INC-ASSESS
  actors: أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة
    (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)
  payload: severity!:enum(MINOR,MAJOR,EMERGENCY,CRISIS) affected_scope_refs!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-INC-DISPATCH-RESPONSE
  aggregate: AGG-INCIDENT
  bc: BC04
  transitions:
  - from:
    - ASSESSED
    to: RESPONDING
    guard: commander؛ ≥ 1 response_task_ref (مهام SLC-03 مرتبطة عبر incident_ref —
      CR-61)
    event: EVT-INC-RESPONSE-DISPATCHED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INCIDENT_INVALID_STATE_TRANSITION
  - RESPONSE_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/incidents/{id}/actions/dispatch-response
  internal: false
  policy: POL-INC-DISPATCH-RESPONSE
  actors: أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة
    (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)
  payload: commander!:urn response_task_refs!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-INC-CONTAIN
  aggregate: AGG-INCIDENT
  bc: BC04
  transitions:
  - from:
    - RESPONDING
    to: CONTAINED
    guard: القائد يؤكد الاحتواء؛ ملاحظة احتواء
    event: EVT-INC-CONTAINED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INCIDENT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/incidents/{id}/actions/contain
  internal: false
  policy: POL-INC-CONTAIN
  actors: أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة
    (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)
  payload: containment_note!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-INC-RESOLVE
  aggregate: AGG-INCIDENT
  bc: BC04
  transitions:
  - from:
    - CONTAINED
    to: RESOLVED
    guard: كل مهام الاستجابة في حالة نهائية (INV-INC-02)؛ ملاحظة حل
    event: EVT-INC-RESOLVED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INCIDENT_INVALID_STATE_TRANSITION
  - RESPONSE_TASKS_OPEN
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/incidents/{id}/actions/resolve
  internal: false
  policy: POL-INC-RESOLVE
  actors: أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة
    (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)
  payload: resolution_note!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-INC-CLOSE
  aggregate: AGG-INCIDENT
  bc: BC04
  transitions:
  - from:
    - RESOLVED
    to: CLOSED
    guard: ملاحظة إغلاق؛ after_action_ref اختياري (كائن معرفة، SLC-12 — R3-Q5)
    event: EVT-INC-CLOSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INCIDENT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/incidents/{id}/actions/close
  internal: false
  policy: POL-INC-CLOSE
  actors: أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة
    (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)
  payload: closing_note!:string after_action_ref:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-INC-CANCEL
  aggregate: AGG-INCIDENT
  bc: BC04
  transitions:
  - from:
    - REPORTED
    to: CANCELLED
    guard: سبب (إنذار كاذب)
    event: EVT-INC-CANCELLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INCIDENT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/incidents/{id}/actions/cancel
  internal: false
  policy: POL-INC-CANCEL
  actors: أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة
    (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-INC-ESCALATE
  aggregate: AGG-INCIDENT
  bc: BC04
  transitions:
  - from: &id001
    - REPORTED
    - ASSESSED
    - RESPONDING
    - CONTAINED
    - RESOLVED
    to: '='
    guard: سبب؛ new_severity أعلى من الحالية فقط (INV-INC-01)؛ إشعار المستوى الأعلى
    event: EVT-INC-ESCALATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INCIDENT_INVALID_STATE_TRANSITION
  - SEVERITY_MUST_INCREASE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/incidents/{id}/actions/escalate
  internal: false
  policy: POL-INC-ESCALATE
  actors: أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة
    (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)
  payload: reason!:string new_severity!:enum(MINOR,MAJOR,EMERGENCY,CRISIS)
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-INC-DE-ESCALATE
  aggregate: AGG-INCIDENT
  bc: BC04
  transitions:
  - from: *id001
    to: '='
    guard: سلطة؛ سبب؛ new_severity أدنى بمستوى واحد كحد أقصى (INV-INC-01)
    event: EVT-INC-DE-ESCALATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INCIDENT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/incidents/{id}/actions/de-escalate
  internal: false
  policy: POL-INC-DE-ESCALATE
  actors: أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة
    (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)
  payload: reason!:string new_severity!:enum(MINOR,MAJOR,EMERGENCY,CRISIS)
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-INC-ACTIVATE-CONTINGENCY
  aggregate: AGG-INCIDENT
  bc: BC04
  transitions:
  - from: *id001
    to: '='
    guard: سلطة؛ ينشئ/يربط Plan (SLC-08، plan_kind=CONTINGENCY، triggered_by=هذه الحادثة
      — CR-60)؛ أمر صريح دائماً، ليس أثراً تلقائياً للتصعيد (INV-INC-03)
    event: EVT-INC-CONTINGENCY-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - INCIDENT_INVALID_STATE_TRANSITION
  - PLAN_LINK_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/operations/incidents/{id}/actions/activate-contingency
  internal: false
  policy: POL-INC-ACTIVATE-CONTINGENCY
  actors: أي مُبلِّغ مخوَّل (تبليغ، إلغاء) · مقيّم الحادثة (تقييم) · قائد الحادثة
    (استجابة، احتواء، حل، إغلاق، تصعيد، تخفيض، تفعيل الاستمرارية)
  payload: plan_template_ref!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
