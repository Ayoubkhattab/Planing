---
id: G6-SLC-19
type: slice-readiness
title: Slice Readiness — SLC-19 Training, Competency & Exercises (R3)
wave: W7
slice: SLC-19
status: DESIGN_COMPLETE — G6 HELD until R1 pilot review AND R2 pilot review (RSK-028)
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
traces: {depends_on: [G6-SLC-03, G6-SLC-09, G6-SLC-12]}
---

# SLC-19 — Training, Competency & Exercises

## الحكم: **DESIGN COMPLETE** — G6 محجوز حتى مراجعة Pilot R1 **و** R2 (RSK-028)

| الشرط | الحالة (محسوب) |
|---|---|
| Aggregates / ثوابت | 3 / 7 |
| الفحص | 0 مخالفات — 15 أمراً، 17 حدثاً، 7 استعلامات |
| OpenAPI | 22 عملية — valid |
| سيناريوهات مكتوبة يدوياً | 10 + 5 خصائص |
| التتبع | 15 متطلباً، 0 بلا اختبار |
| تصحيحات عابرة للشرائح | CR-63 (SLC-12 AGG-KNOWLEDGE-OBJECT، نص الشرط ونص REQ-KNW-002 فقط — صيغة الحمولة `source:urn` لم تتغير) — مطبَّق ومُعاد توليده؛ اختبار ذهاب وإياب: الفرق الوحيد سطر نص الشرط في AGG-KNOWLEDGE-OBJECT.md وسطر الحمولة الوصفية في commands-slc12.md؛ كل ملفات SLC-12 الأخرى (OpenAPI، AsyncAPI، الأخطاء، سيناريوهات القبول) طابقت الأصل حرفياً. **SLC-03 وSLC-09 بلا أي تصحيح** — الحقلان المُعاد استخدامهما (`evidence:urn`، `code:string`) كانا عامّين بما يكفي منذ التعريف الأول |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-SCENARIO | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-EXERCISE | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-SIMULATION | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| Competency/Qualification/Certification (DOM-18) | لا Aggregate جديد؛ AGG-QUALIFICATION-RECORD (SLC-03) بلا تعديل |
| Readiness/Eligibility (DOM-18) | لا Aggregate جديد؛ AGG-ROLE-REQUIREMENT (SLC-09) وEligibilityCheck (SLC-03) بلا تعديل |
| Training كنشاط | لا كيان مستقل؛ دليل عبر `evidence:urn` العام أصلاً في CMD-QUAL-RECORD/RENEW، يشير إلى محاكاة مكتملة (SLC-19) |
| Exercise/Scenario/Simulation | ثلاث aggregates — مبرَّرة بنيوياً (لا لمجرد R3-Q4): Scenario مرجعي قابل لإعادة الاستخدام؛ Exercise تنسيق/جدولة (يماثل Logistics Request)؛ Simulation تنفيذ فعلي بتاريخ append-only (يماثل Shipment) — نفس نمط الانقسام الذي أثبت نفسه في SLC-18 |
| Evaluation | كيان داخلي ضمن Simulation، بلا Aggregate رابع |
| تفويض النتيجة النهائية للتمرين | لا أمر بشري يحدد COMPLETED/ABORTED؛ حصراً حدث نظامي من Simulation المرتبطة (INV-EXR-02) — يكرر نمط CR-62/SLC-18 على أصل جديد بالكامل، لا توسيع |
| After Action Review (DOM-19) | Knowledge Object من نوع lesson في BC06 (SLC-12)؛ محاكاة مكتملة مصدر نهائي رابع (CR-63)؛ لا كيان جديد |
| إعادة المحاولة بعد الإجهاض | لا إعادة جدولة تلقائية؛ تغطية تمرين مُجهَض تتطلب CMD-EXR-PLAN جديداً صريحاً (A17، مثل SLC-18) |

## ملاحظة صريحة حول التعرّض الفعلي لـ RSK-028 (الأدنى بين شرائح R3 الثلاث)
خلافاً لـ SLC-18 (التي تعتمد بنيوياً على دفتر سعة SLC-09 غير المقاس)، اعتماديات SLC-19 التقنية الفعلية على SLC-03 وSLC-09 وSLC-12 **محدودة بحقل عام واحد لكل منها** — لا آلية تنافس، لا دفتر سعة، لا قرار تخصيص مشترك. هذا يعني أن أي إعادة معايرة بعد Pilot R1/R2 لتلك الشرائح الثلاث **لا تمس** تصميم SLC-19 نفسه إطلاقاً — التعرّض الوحيد الحقيقي هنا هو قيم SLC-19 الإشارية الخاصة بها (مدة محاكاة، زمن استجابة تسليم حقنة)، لا بنية موروثة. الحجز المحفظي على G6 يبقى قائماً على مستوى R3 ككل (RSK-028)، لكن الأساس الفني الذي يبرره هنا هو الأضعف بين الشرائح الثلاث — انظر `03-domain/contexts/BC05/training-exercise-spec.md` §6.
