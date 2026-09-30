---
id: SPEC-TRAINING-EXERCISE
type: component-specification
title: Training, Competency & Exercises Rules — reuse of Qualification Record/Role Requirement, Scenario/Exercise/Simulation, After Action Review
wave: W4
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
slice: SLC-19
traces: {closes: [R3-Q4, R3-Q5], corrects: [CR-63], requirements: [REQ-TRX-001, REQ-TRX-003, REQ-TRX-005, REQ-TRX-012, REQ-TRX-013]}
recalibrate_after_pilot: true
---

# Training, Competency & Exercises Rules

## 1. لماذا Competency/Qualification/Certification/Readiness/Eligibility (DOM-18) لا تحصل على Aggregate جديد
كل عنصر من عناصر DOM-18 الستة مغطى فعلياً ببنية موجودة قبل هذه الشريحة:
- **Competency/Qualification/Certification** = `AGG-QUALIFICATION-RECORD` (SLC-03)، بلا أي تعديل على تعريفه.
- **Readiness/Eligibility** = `AGG-ROLE-REQUIREMENT` (SLC-09) وآلية `EligibilityCheck` (`eligibility-rules.md`، SLC-03)، كلاهما بلا تعديل.

هذا يطابق حرفياً وصف `01-business/release-3-scope.md` §2 لهذه الشريحة: **"أعلى إعادة استخدام بين شرائح R3 الثلاث"**. لا حاجة اختراع مفهوم "Training" ككيان مستقل: التدريب هو **نشاط** (Exercise/Simulation، §3 أدناه) ينتج **دليلاً** يُستشهد به عند تسجيل أو تجديد سجل تأهيل قائم — الدليل يمر عبر الحقل العام الموجود أصلاً `evidence:urn` في `CMD-QUAL-RECORD`/`CMD-QUAL-RENEW` (SLC-03)، وهو غير مكتوب النوع أصلاً، تماماً كما كان `target!:urn` في `CMD-ALC-REQUEST` قبل CR-62. **لا حاجة لأي تصحيح على SLC-03 هنا** — الحقل عام بما يكفي دون أي تغيير.

## 2. لماذا Exercise/Scenario/Simulation ثلاث Aggregates، لا اثنان
`01-business/release-3-scope.md` §4 (R3-Q4) سمّى الثلاثة صراحة كـ aggregates جديدة قبل بدء التصميم الفعلي — خلافاً لـ SLC-17 وSLC-18، حيث بدأ كل منهما بقائمة عناصر DOM أكبر ثم **قُلِّصت** فعلياً أثناء التصميم (DOM-17: 8 عناصر → 2 aggregate؛ DOM-16: 6 عناصر → 2 aggregate). هنا جرى نفس الفحص النقدي أثناء التصميم الفعلي، لا القبول الأعمى لعدد R3-Q4 المفترَض مسبقاً — والنتيجة أن الفصل الثلاثي **مبرَّر بنيوياً بحد ذاته**، لا لمجرد اتباع القرار المسبق:
- **Scenario** كائن **مرجعي قابل لإعادة الاستخدام** عبر عدد غير محدود من التمارين المستقبلية، بدورة حياة استقلالية (DRAFT/ACTIVE/RETIRED) لا علاقة لها بزمن أي تمرين بعينه — يماثل بنيوياً `AGG-PLAN`/`AGG-KNOWLEDGE-OBJECT` أكثر مما يماثل الحدث الواحد.
- **Exercise** كائن **تنسيق/جدولة** (participants، نافذة زمنية، موقع) — يماثل بنيوياً `AGG-LOGISTICS-REQUEST` من SLC-18: طلب/تنسيق لا ينفّذ العملية بنفسه.
- **Simulation** كائن **تنفيذ فعلي** بتاريخ داخلي append-only (تسليم الحقن) ونتيجة تُحسب من تقييمات — يماثل بنيوياً `AGG-SHIPMENT` من SLC-18: التنفيذ الفعلي بمساره الخاص للأحداث، لا التنسيق.

هذا **هو نفس نمط الانقسام الذي أثبت نفسه في SLC-18** (Logistics Request كتنسيق مقابل Shipment كتنفيذ)، معاد استخدامه هنا حرفياً حتى في آلية التفويض: `AGG-EXERCISE` لا يقرر نتيجته النهائية (COMPLETED/ABORTED) بأمر بشري مباشر — ينتقل حصراً بحدث نظامي `SYS:` مصدره `AGG-SIMULATION` (INV-EXR-02)، تماماً كما كان انتقال `AGG-LOGISTICS-REQUEST` إلى APPROVED/PENDING_APPROVAL/REJECTED مدفوعاً حصراً بأحداث `AGG-ALLOCATION` (CR-62، SLC-18). **لا Aggregate رابع لـ Evaluation**: التقييم كيان داخلي ضمن Simulation (`Evaluation`)، بلا هوية أو دورة حياة مستقلة عن المحاكاة التي أُنتج فيها — يماثل `Statement` داخل `AGG-KNOWLEDGE-OBJECT` أو `Requirement` داخل `AGG-ROLE-REQUIREMENT`.

## 3. الربط بين Exercise وSimulation (نمط CR-62 نفسه، بلا تصحيح جديد هنا)
`CMD-EXR-START` **لا** يُنشئ Simulation عبر منطق مخفي: يُصدر `CMD-SIM-START` صراحة ضمن نفس معاملة قاعدة البيانات (نفس وحدة العمل)، بحمولة `exercise_ref`/`scenario_ref` (السيناريو المجمَّد وقت التخطيط — INV-EXR-01). لأن `AGG-SIMULATION` جديد بالكامل في هذه الشريحة (لا يوجد تعريف سابق لتوسيعه)، **لا حاجة لأي Correction من نوع CR-62** هنا — الحقلان كانا عامّين منذ التعريف الأول. هذا يوثّق فارقاً مهماً عن SLC-18: إعادة الاستخدام هناك كانت *توسيع تعريف قائم*؛ هنا هي *تكرار نمط تصميم مُثبَت* على أصل جديد بالكامل — كلاهما "إعادة استخدام" بمعنى A17، لكن بآلية مختلفة (توسيع عقد مقابل تكرار نمط).

## 4. مراجعة ما بعد الحدث (After Action Review) — CR-63
DOM-19 يسمّي After Action Review كعنصر مستقل خامس. القرار R3-Q5 (مثبَّت مسبقاً في نطاق R3): **تُخزَّن كـ Knowledge Object من نوع lesson في BC06 (SLC-12)، لا ككيان جديد هنا** — بنفس منطق §1 أعلاه (لا اختراع كيان لما تغطيه بنية قائمة).

`AGG-KNOWLEDGE-OBJECT`'s `CMD-KNO-DRAFT` guard كان يقيّد المصادر النهائية لـ lesson بثلاثة أنواع فقط: **task، plan، incident** (`REQ-KNW-002`). محاكاة مكتملة (`AGG-SIMULATION` بحالة COMPLETED) هي مصدر نهائي رابع منطقياً — الحدث `EVT-SIM-COMPLETED` نهائي، وله أدلة (التقييمات المسجَّلة). **CR-63** يوسّع نص الشرط ليشمل `simulation` كبديل رابع، ويوسّع نص `REQ-KNW-002` بالمثل. حقل المصدر نفسه (`source:urn` في `CMD-KNO-DRAFT`) كان عاماً أصلاً — **لا تغيير على صيغة الحمولة**، فقط نص الشرط والمتطلب، بنفس أثر CR-62 الأدنى (SLC-09 لم يتغير سوى سطرين نصيين). هذا **هو التصحيح العابر للشرائح الوحيد في هذه الشريحة** — ولا يمس لا SLC-03 ولا SLC-09 إطلاقاً، بما يطابق وصف "أعلى إعادة استخدام" حرفياً: التوسيعان الآخران (Qualification Record وRole Requirement) لم يحتاجا حتى تصحيح نص.

## 5. لا إعادة إرسال تلقائية أو إعادة محاولة للمحاكاة المُجهَضة
إن أُجهضت محاكاة (`CMD-SIM-ABORT`)، ينتقل التمرين المرتبط بها إلى ABORTED نهائياً (INV-EXR-02) — لا محاولة تلقائية ثانية، ولا إعادة فتح للتمرين. تغطية تمرين فاشل تتطلب `CMD-EXR-PLAN` جديداً صريحاً — نفس تبسيط SLC-18 المتعمَّد لعدم إعادة الإرسال التلقائي للكمية الناقصة (منطق A17، لا خلل).

## 6. قيم إشارية غير مقاسة
مثل SLC-17 وSLC-18 (RSK-028): أي هدف زمني (مدة محاكاة، زمن استجابة تسليم حقنة) في هذه الشريحة **إشاري غير مقاس**. خلافاً لـ SLC-18 (التي اعتمدت مباشرة على بنية SLC-09/R2 غير المقاسة)، اعتماديات SLC-19 التقنية الفعلية على SLC-03 وSLC-09 وSLC-12 **محدودة بحقل عام واحد لكل منها** (`evidence:urn`، `code:string` في Requirement، `source:urn`) — لا اعتماد بنيوي على آليات تنافس أو دفاتر سعة تلك الشرائح. هذا يجعل التعرّض الفعلي لـ RSK-028 هنا **الأدنى بين شرائح R3 الثلاث**، رغم بقاء الحجز المحفظي نفسه قائماً على مستوى R3 ككل (انظر `14-slices/SLC-19/readiness.md`).
