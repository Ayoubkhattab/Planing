---
id: SPEC-RISK-CONTINGENCY
type: component-specification
title: Risk & Contingency Rules — hazard catalog, severity, reuse of Plan/Task
wave: W4
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
slice: SLC-17
traces: {closes: [R3-Q2, R3-Q4], corrects: [CR-60, CR-61], requirements: [REQ-RCM-001, REQ-RCM-009, REQ-RCM-011, REQ-RCM-016]}
recalibrate_after_pilot: true
---

# Risk & Contingency Rules

## 1. فئات الخطر (RD-HAZARD-CATEGORIES)
مثل R2-Q1 (RD-ASSET-TYPES/RD-RESOURCE-TYPES): كتالوج مرجعي واحد لكل مستأجر، لا فئات مثبَّتة في الكود. المنصة توفر فئات أساسية مقترحة فقط (طبيعي، تقني، أمني، صحي، بيئي، آخر) — الكتالوج الفعلي يُحمَّل عند تهيئة المستأجر، كما هو الحال مع أنظمة ERP/HRIS الفعلية (R2-Q8). `category_ref` في كل من Risk وIncident يشير لعنصر في هذا الكتالوج، ولا يفترض قائمة مغلقة.

## 2. لماذا لا يوجد Aggregate منفصل لـ Hazard
"Hazard" (المصدر المحتمل للخطر) ليس له دورة حياة خاصة به مستقلة عن الخطر الذي يُعرَّف عنه — فئة الخطر (hazard category) بيانات مرجعية تُستهلَك، لا كائن له حالة. هذا امتداد لنفس منطق R2-Q1، وليس قراراً جديداً.

## 3. لماذا Incident واحد يغطي Emergency وCrisis
DOM-17 يذكر Incident وEmergency وCrisis كمفاهيم منفصلة، لكنها في الممارسة **نفس الهوية تتصاعد خطورتها**، لا كيانات مختلفة: حادثة تُبلَّغ بخطورة MINOR وقد تصعَّد إلى CRISIS دون أن تتغير هويتها أو سجلها التاريخي. فصلها إلى ثلاثة Aggregates كان سيكرر "God Aggregate" بشكل معكوس (Aggregate Fragmentation) — كيانات متعددة لمفهوم واحد متطور. القرار: **aggregate واحد (AGG-INCIDENT) بخاصية severity متغيرة صراحة عبر أمرين فقط** (ESCALATE وDE-ESCALATE)، مع سجل تاريخي كامل (SeverityHistory) للمساءلة.

## 4. لماذا لا يوجد Aggregate جديد للاستمرارية (Continuity)
قرار R3-Q2: خطة الاستمرارية **هي** AGG-PLAN من SLC-08، بامتداد `plan_kind` (CR-60)، لا نموذج مستقل. هذا يعني:
- كل قواعد Plan القائمة (DRAFT→ACTIVE عند أول إصدار خط أساس، الإكمال، الإغلاق، إعادة التصنيف) تنطبق حرفياً على خطط الاستمرارية دون كود إضافي.
- التفعيل (`CMD-INC-ACTIVATE-CONTINGENCY`) ينشئ أو يربط Plan بـ `plan_kind=CONTINGENCY` و`triggered_by` يشير للحادثة — لا حالة "مفعَّلة" منفصلة يحتفظ بها Incident نفسه.
- **الاستثناء الوحيد المتعمَّد (FM-S17-02):** إغلاق الحادثة لا يتطلب إغلاق خطة الاستمرارية المرتبطة؛ التعافي قد يستمر بعد إغلاق الحادثة مشروعاً، وهذا مقصود لا خلل.

## 5. لماذا لا توجد حالة "تعافي" منفصلة
قرار R3-Q4: "التعافي" محسوب لا مخزَّن — `QRY-INC-RECOVERY-STATUS` يقرأ تقدم مهام خطة الاستمرارية المرتبطة (SLC-03 AGG-TASK عبر CR-61 أو خطة SLC-08) مقابل زمن بدء الحادثة، وينتج تقديراً لـ RTO/RPO. لا آلة حالة جديدة، لا جدول تخزين جديد لـ "حالة التعافي" — إعادة استخدام كاملة.

## 6. قواعد الخطورة (severity)
| القاعدة | التفصيل |
|---|---|
| الاتجاه | تزداد فقط عبر `CMD-INC-ESCALATE`؛ تنقص فقط عبر `CMD-INC-DE-ESCALATE` بمستوى واحد كحد أقصى لكل أمر (INV-INC-01) |
| السجل | كل تغيير يُسجَّل في `SeverityHistory` (from, to, at, reason، الفاعل) — لا يُكتب فوق القيمة السابقة |
| التفعيل | تصعيد الخطورة **لا يفعّل** خطة استمرارية تلقائياً؛ فعل منفصل دائماً (INV-INC-03، القسم 4 أعلاه) |
| SLA | زمن الاستجابة (dispatch) بحسب severity — قيمة إشارية غير مقاسة، موسومة لإعادة الاشتقاق بعد Pilot R1 وR2 (RSK-028)، لا تُعتبر التزاماً تعاقدياً |

## 7. عزل الخطر عن الحادثة (INV-RIS-05 / INV-INC-04)
ربط حادثة بخطر متحقِّق (`risk_ref` على Incident، أو `incident_ref` على Risk عند الإغلاق برationale=materialized) هو **رابط معلوماتي فقط**. لا أمر على أحدهما يغيّر حالة أو إصدار أو تصنيف الآخر تلقائياً — كل تغيير على أي منهما يتطلب أمره الخاص من مالكه الخاص. هذا امتداد مباشر لدرس "Silent Pre-emption" من SLC-09 (لا أثر جانبي صامت بين كيانات مرتبطة).
