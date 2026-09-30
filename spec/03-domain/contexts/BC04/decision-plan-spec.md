---
id: SPEC-PLAN
type: component-specification
title: Decision Basis, Change Classification, Task Synchronization, Outcome Progress
wave: W4
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {rules: [BRL-003, BRL-004, BRL-005], requirements: [REQ-DEC-001, REQ-DEC-002, REQ-DEC-003, REQ-DEC-004, REQ-OPS-001, REQ-OPS-002, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-013], corrects: [CR-29]}
---

# Decision → Plan → Baseline → Tasks

## 1. أساس القرار (Decision basis) — "ماذا كان معروفاً؟"
```text
basis(decision D) =
  authority: AuthorityCheck(D.decider, D.type, D.scope, at = D.recorded_at)   -- stored snapshot + re-verifiable
  citations: for each c in D.citations → c.ref @ c.version                      -- pinned; later versions ignored
  claims:    for each assessment cited → its key claims resolved with known_at = D.recorded_at (LIB §3)
```
`QRY-DEC-BASIS` يعيد هذا كله، فيستطيع المدقق مقارنة ما عرفه صاحب القرار بما نعرفه الآن (TEMPORAL-MODEL §5). هذا تحقيق OUT-04 عملياً.

## 2. تصنيف التغيير (BRL-005)
عند SUBMIT تُحسب الفروق بين الإصدار المقدم والخط الأساسي الحالي:
| العنصر | تغيير = |
|---|---|
| objectives، outcomes (metric/target/due) | **major** |
| phases (إضافة/حذف/نافذة) | **major** |
| milestones (التاريخ) | **major** |
| activities (إضافة/حذف، task_generating، نافذة، completion_criteria) | **major** |
| resource_notes (التزامات موارد) | **major** |
| الأوصاف، الملاحظات، المرفقات | minor |

- أي major → إصدار جديد يحتاج اعتماداً (INV-PLV-04).
- إصدار مقدم بفروق minor فقط → مسموح، لكن الأبسط `CMD-PLV-AMEND-MINOR` على الخط الأساسي.
- `QRY-PLV-DIFF` يعرض التصنيف ومعاينة مزامنة المهام قبل الاعتماد.

## 3. مزامنة المهام عند الاعتماد (Task synchronization)
معرّفات الأنشطة ثابتة عبر الإصدارات (INV-PLV-03)، فالمزامنة فرق حتمي بين الخط الأساسي السابق والجديد:

| الحالة | الإجراء (بأوامر SLC-03 بهوية المزامن) |
|---|---|
| نشاط جديد task_generating | `CMD-TASK-CREATE` (plan_ref = plan@version، task type من النشاط، المعايير من النشاط) → DRAFT → MARK-READY |
| نشاط محذوف | المهام غير النهائية → SUPERSEDED (SYS في SM-TASK) |
| نشاط مستمر بلا تغيير في معاييره | لا شيء؛ plan_ref يُحدَّث للإصدار الجديد (تعليق T3) |
| نشاط مستمر وتغيرت معاييره | المهام غير المسندة: تُعدل (DRAFT/READY). المسندة فما بعد: المعايير مجمّدة (INV-TASK-09) → SUPERSEDED + مهمة جديدة |
| نافذة النشاط تغيرت | `CMD-TASK-SET-DUE` للمهام غير النهائية |

- **خاصية:** المزامنة idempotent — تشغيلها مرتين على نفس الانتقال لا ينتج شيئاً إضافياً (P-82).
- المزامنة تجري بعد التزام الاعتماد عبر حدث EVT-PLV-BASELINED (نهائية الاتساق)، مع معرّف تشغيل ثابت لكل (plan, from_version, to_version).
- تعليق الخطة يعلّق مهامها (علم)، وإلغاؤها يلغي مهامها غير النهائية.

## 4. تقدم النتائج
- `progress(outcome, T, K)` = آخر قياس معروف عند K ذو measured_at ≤ T، مقابل الهدف الساري عند T.
- القياسات تُصحح بإغلاق وإضافة (لا كتابة فوق)، فتقارير التقدم التاريخية تبقى قابلة لإعادة الإنتاج.
- مصدر القياس: يدوي، أو نتيجة مهمة (قياس من SLC-03 ADD-RESULT-ITEM kind=measurement)، أو ملاحظة.

## 5. سلسلة السلطة
- تسجيل القرار: `AuthorityCheck` وقت التسجيل؛ فشل أو تعذر الوصول → رفض (fail-closed، AUTHORITY_REQUIRED).
- اعتماد إصدار الخطة: نوع قرار `plan-approval` في نطاق الخطة.
- إلغاء قرار (annul): سلطة لنفس نوع القرار في نطاق أعلى.
