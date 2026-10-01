---
id: AGG-INCIDENT
type: aggregate
title: Incident
wave: W4
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
bounded_context: BC04
importance_tier: T1
personal_data: false
traces:
  satisfies:
  - REQ-RCM-006
  - REQ-RCM-007
  - REQ-RCM-008
  - REQ-RCM-009
  - REQ-RCM-010
  - REQ-RCM-011
  - REQ-RCM-012
  - REQ-RCM-013
  state_machine: SM-INCIDENT
  decided_by:
  - ADR-P01
  - ADR-P02
  - ADR-P03
  - ADR-P13
---


# AGG-INCIDENT — Incident

**الغرض:** تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي  
**السياق:** BC04 · **المستوى:** T1 · **بيانات شخصية:** لا

## الثوابت (Invariants)

- **INV-INC-01** — severity تزداد فقط عبر CMD-INC-ESCALATE وتنقص فقط عبر CMD-INC-DE-ESCALATE؛ لا تتغير كأثر جانبي لأي أمر آخر
- **INV-INC-02** — CLOSED فقط عندما تكون كل مهمة استجابة مرتبطة في حالة نهائية (يماثل PLAN.COMPLETE وTASK.CLOSE)
- **INV-INC-03** — تفعيل خطة الاستمرارية أمر صريح مخوَّل دائماً، ليس أثراً تلقائياً لتصعيد الخطورة وحده
- **INV-INC-04** — خطر مرتبط (risk_ref) لا تتغير حالته تلقائياً أبداً بإنشاء هذه الحادثة أو تصعيدها أو إغلاقها؛ مالك الخطر يتصرف بأمر منفصل (يماثل INV-RIS-05)
- **INV-INC-05** — كل أمر مقبول ينتج حدثاً واحداً بالضبط وسجل تدقيق واحداً

## مكونات داخلية

- SeverityHistory (from, to, at, reason)

## الحالات

- غير نهائية: REPORTED, ASSESSED, RESPONDING, CONTAINED, RESOLVED
- نهائية: CLOSED, CANCELLED
- قابلية الوصول لحالة نهائية (SL-06): **PASS**

## الانتقالات

| من | الأمر | إلى | الشرط (Guard) | الحدث | خطأ فشل الشرط |
|---|---|---|---|---|---|
| ∅ (إنشاء) | CMD-INC-REPORT | REPORTED | category_ref (RD-HAZARD-CATEGORIES)؛ description؛ scope_refs ≥ 1؛ risk_ref اختياري (خطر تحقَّق)؛ severity ابتدائية MINOR؛ label ≥ تصنيف النطاق | EVT-INC-REPORTED | INCIDENT_INVALID |
| REPORTED | CMD-INC-ASSESS | ASSESSED | severity ∈ {MINOR,MAJOR,EMERGENCY,CRISIS}؛ affected_scope_refs؛ مقيّم مخوَّل | EVT-INC-ASSESSED | INCIDENT_INVALID |
| ASSESSED | CMD-INC-DISPATCH-RESPONSE | RESPONDING | commander؛ ≥ 1 response_task_ref (مهام SLC-03 مرتبطة عبر incident_ref — CR-61) | EVT-INC-RESPONSE-DISPATCHED | RESPONSE_REQUIRED |
| RESPONDING | CMD-INC-CONTAIN | CONTAINED | القائد يؤكد الاحتواء؛ ملاحظة احتواء | EVT-INC-CONTAINED | REASON_REQUIRED |
| CONTAINED | CMD-INC-RESOLVE | RESOLVED | كل مهام الاستجابة في حالة نهائية (INV-INC-02)؛ ملاحظة حل | EVT-INC-RESOLVED | RESPONSE_TASKS_OPEN |
| RESOLVED | CMD-INC-CLOSE | CLOSED | ملاحظة إغلاق؛ after_action_ref اختياري (كائن معرفة، SLC-12 — R3-Q5) | EVT-INC-CLOSED | REASON_REQUIRED |
| REPORTED | CMD-INC-CANCEL | CANCELLED | سبب (إنذار كاذب) | EVT-INC-CANCELLED | REASON_REQUIRED |
| أي حالة غير نهائية | CMD-INC-ESCALATE | (بلا تغيير) | سبب؛ new_severity أعلى من الحالية فقط (INV-INC-01)؛ إشعار المستوى الأعلى | EVT-INC-ESCALATED | SEVERITY_MUST_INCREASE |
| أي حالة غير نهائية | CMD-INC-DE-ESCALATE | (بلا تغيير) | سلطة؛ سبب؛ new_severity أدنى بمستوى واحد كحد أقصى (INV-INC-01) | EVT-INC-DE-ESCALATED | REASON_REQUIRED |
| أي حالة غير نهائية | CMD-INC-ACTIVATE-CONTINGENCY | (بلا تغيير) | سلطة؛ ينشئ/يربط Plan (SLC-08، plan_kind=CONTINGENCY، triggered_by=هذه الحادثة — CR-60)؛ أمر صريح دائماً، ليس أثراً تلقائياً للتصعيد (INV-INC-03) | EVT-INC-CONTINGENCY-ACTIVATED | PLAN_LINK_INVALID |
| REPORTED, ASSESSED | SYS:response SLA elapsed without dispatch | (بلا تغيير) | المجدول؛ SLA حسب severity، موسوم 'تُعاد معايرته بعد Pilot R1/R2' (RSK-028) | EVT-INC-SLA-BREACHED | — |

## مصفوفة الحالات × الأوامر (كاملة — SL-05)

كل خلية حُكم صريح: `→ حالة` مسموح، `✗ رمز` مرفوض. لا خلايا فارغة.

| الحالة \ الأمر | CMD-INC-REPORT | CMD-INC-ASSESS | CMD-INC-DISPATCH-RESPONSE | CMD-INC-CONTAIN | CMD-INC-RESOLVE | CMD-INC-CLOSE | CMD-INC-CANCEL | CMD-INC-ESCALATE | CMD-INC-DE-ESCALATE | CMD-INC-ACTIVATE-CONTINGENCY | SYS:response SLA elapsed without dispatch |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ∅ | → REPORTED | — | — | — | — | — | — | — | — | — | — |
| REPORTED | ✗ INCIDENT_INVALID_STATE_TRANSITION | → ASSESSED | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | → CANCELLED | → REPORTED | → REPORTED | → REPORTED | → REPORTED |
| ASSESSED | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | → RESPONDING | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | → ASSESSED | → ASSESSED | → ASSESSED | → ASSESSED |
| RESPONDING | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | → CONTAINED | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | → RESPONDING | → RESPONDING | → RESPONDING | ✗ INCIDENT_INVALID_STATE_TRANSITION |
| CONTAINED | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | → RESOLVED | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | → CONTAINED | → CONTAINED | → CONTAINED | ✗ INCIDENT_INVALID_STATE_TRANSITION |
| RESOLVED | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | → CLOSED | ✗ INCIDENT_INVALID_STATE_TRANSITION | → RESOLVED | → RESOLVED | → RESOLVED | ✗ INCIDENT_INVALID_STATE_TRANSITION |
| CLOSED | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION |
| CANCELLED | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION | ✗ INCIDENT_INVALID_STATE_TRANSITION |

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
id: AGG-INCIDENT
bc: BC04
name: Incident
tier: T1
purpose: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة
  والتعافي
states:
- REPORTED
- ASSESSED
- RESPONDING
- CONTAINED
- RESOLVED
- CLOSED
- CANCELLED
terminal:
- CLOSED
- CANCELLED
invariants:
- 'INV-INC-01: severity تزداد فقط عبر CMD-INC-ESCALATE وتنقص فقط عبر CMD-INC-DE-ESCALATE؛
  لا تتغير كأثر جانبي لأي أمر آخر'
- 'INV-INC-02: CLOSED فقط عندما تكون كل مهمة استجابة مرتبطة في حالة نهائية (يماثل
  PLAN.COMPLETE وTASK.CLOSE)'
- 'INV-INC-03: تفعيل خطة الاستمرارية أمر صريح مخوَّل دائماً، ليس أثراً تلقائياً لتصعيد
  الخطورة وحده'
- 'INV-INC-04: خطر مرتبط (risk_ref) لا تتغير حالته تلقائياً أبداً بإنشاء هذه الحادثة
  أو تصعيدها أو إغلاقها؛ مالك الخطر يتصرف بأمر منفصل (يماثل INV-RIS-05)'
- 'INV-INC-05: كل أمر مقبول ينتج حدثاً واحداً بالضبط وسجل تدقيق واحداً'
entities:
- SeverityHistory (from, to, at, reason)
requirements:
- REQ-RCM-006
- REQ-RCM-007
- REQ-RCM-008
- REQ-RCM-009
- REQ-RCM-010
- REQ-RCM-011
- REQ-RCM-012
- REQ-RCM-013
notes: null
personal_data: false
reachability: PASS
transitions:
- from: ∅
  command: CMD-INC-REPORT
  to: REPORTED
  guard: category_ref (RD-HAZARD-CATEGORIES)؛ description؛ scope_refs ≥ 1؛ risk_ref
    اختياري (خطر تحقَّق)؛ severity ابتدائية MINOR؛ label ≥ تصنيف النطاق
  event: EVT-INC-REPORTED
  guard_error: INCIDENT_INVALID
- from:
  - REPORTED
  command: CMD-INC-ASSESS
  to: ASSESSED
  guard: severity ∈ {MINOR,MAJOR,EMERGENCY,CRISIS}؛ affected_scope_refs؛ مقيّم مخوَّل
  event: EVT-INC-ASSESSED
  guard_error: INCIDENT_INVALID
- from:
  - ASSESSED
  command: CMD-INC-DISPATCH-RESPONSE
  to: RESPONDING
  guard: commander؛ ≥ 1 response_task_ref (مهام SLC-03 مرتبطة عبر incident_ref — CR-61)
  event: EVT-INC-RESPONSE-DISPATCHED
  guard_error: RESPONSE_REQUIRED
- from:
  - RESPONDING
  command: CMD-INC-CONTAIN
  to: CONTAINED
  guard: القائد يؤكد الاحتواء؛ ملاحظة احتواء
  event: EVT-INC-CONTAINED
  guard_error: REASON_REQUIRED
- from:
  - CONTAINED
  command: CMD-INC-RESOLVE
  to: RESOLVED
  guard: كل مهام الاستجابة في حالة نهائية (INV-INC-02)؛ ملاحظة حل
  event: EVT-INC-RESOLVED
  guard_error: RESPONSE_TASKS_OPEN
- from:
  - RESOLVED
  command: CMD-INC-CLOSE
  to: CLOSED
  guard: ملاحظة إغلاق؛ after_action_ref اختياري (كائن معرفة، SLC-12 — R3-Q5)
  event: EVT-INC-CLOSED
  guard_error: REASON_REQUIRED
- from:
  - REPORTED
  command: CMD-INC-CANCEL
  to: CANCELLED
  guard: سبب (إنذار كاذب)
  event: EVT-INC-CANCELLED
  guard_error: REASON_REQUIRED
- from: '*NT'
  command: CMD-INC-ESCALATE
  to: '='
  guard: سبب؛ new_severity أعلى من الحالية فقط (INV-INC-01)؛ إشعار المستوى الأعلى
  event: EVT-INC-ESCALATED
  guard_error: SEVERITY_MUST_INCREASE
- from: '*NT'
  command: CMD-INC-DE-ESCALATE
  to: '='
  guard: سلطة؛ سبب؛ new_severity أدنى بمستوى واحد كحد أقصى (INV-INC-01)
  event: EVT-INC-DE-ESCALATED
  guard_error: REASON_REQUIRED
- from: '*NT'
  command: CMD-INC-ACTIVATE-CONTINGENCY
  to: '='
  guard: سلطة؛ ينشئ/يربط Plan (SLC-08، plan_kind=CONTINGENCY، triggered_by=هذه الحادثة
    — CR-60)؛ أمر صريح دائماً، ليس أثراً تلقائياً للتصعيد (INV-INC-03)
  event: EVT-INC-CONTINGENCY-ACTIVATED
  guard_error: PLAN_LINK_INVALID
- from:
  - REPORTED
  - ASSESSED
  command: SYS:response SLA elapsed without dispatch
  to: '='
  guard: المجدول؛ SLA حسب severity، موسوم 'تُعاد معايرته بعد Pilot R1/R2' (RSK-028)
  event: EVT-INC-SLA-BREACHED
  guard_error: null
```

</details>
