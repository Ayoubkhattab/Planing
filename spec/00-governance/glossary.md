---
id: GLOSSARY
type: glossary
title: Glossary (AR/EN) — binding
wave: W0
tier: T0
owner_role: Orchestrator
status: DRAFT
approved_by: null
approved_at: null
consumers:
- all artifacts (SL-26)
---

# Glossary (AR/EN) — binding

## terms

_90 items_

| en | ar | definition | source | disambiguates | status |
|---|---|---|---|---|---|
| Entity | كيان | شيء له هوية مستمرة ويمثل كائناً أو مفهوماً | PRJ§3.2, V5 A05 | — | PROPOSED |
| Event (Domain Event) | حدث مجال | سجل لشيء وقع في زمن محدد داخل سياق | PRJ§3.2, §14 | — | PROPOSED |
| Integration Event | حدث تكامل | نسخة عامة من حدث تُنشر خارج السياق | PRJ§15 | — | PROPOSED |
| Notification | إشعار | رسالة للمستخدم، ليست حدثاً | PRJ§15 | — | PROPOSED |
| Claim | ادعاء | عبارة عن كيان أو علاقة يدعمها دليل وقد تتعارض مع غيرها | PRJ§3.4 | — | PROPOSED |
| Evidence | دليل | مادة تدعم ادعاءً ولا تساويه | V5 A06 | CR-31 | PROPOSED |
| Source | مصدر | جهة أو نظام أو مستشعر أنتج معلومة | PRJ§7.5 | — | PROPOSED |
| Observation | ملاحظة | ما رصده مصدر في زمن ومكان | PRJ§7.6 | — | PROPOSED |
| Provenance | منشأ | الأصل الذي جاءت منه المعلومة | PRJ§3.6 | — | PROPOSED |
| Lineage | سلسلة الاشتقاق | تسلسل التحويلات من المصدر إلى النتيجة | PRJ§23 | — | PROPOSED |
| Event Time | زمن الحدث | متى وقع الشيء في الواقع | PRJ§3.5 | — | PROPOSED |
| Observation Time | زمن الرصد | متى رُصد | PRJ§3.5 | — | PROPOSED |
| Record Time | زمن التسجيل | متى عرف النظام المعلومة | PRJ§3.5 | ADR-P01 | PROPOSED |
| Valid Time | زمن الصلاحية | الفترة التي تكون فيها المعلومة صحيحة في الواقع | PRJ§3.5 | — | PROPOSED |
| Effective Time | زمن السريان | متى يبدأ أثر قرار أو سياسة | PRJ§3.5 | — | PROPOSED |
| Access Policy | سياسة وصول | قاعدة تقرر السماح أو الرفض لفاعل على مورد | PRJ§7.2 | CR-33 | PROPOSED |
| Governance Policy | سياسة حوكمة | قاعدة مؤسسية (احتفاظ، تصنيف، امتثال) | PRJ§7.25 | CR-33 | PROPOSED |
| Policy Knowledge | معرفة سياساتية | محتوى معرفي يشرح سياسة، لا ينفذها | PRJ§7.21 | CR-33 | PROPOSED |
| Policy Decision | قرار سياسة | ناتج تقييم سياسة: ALLOW/DENY/CONDITIONAL/REDACT/AGGREGATE/REQUIRE_APPROVAL | PRJ§66 | CR-38 | PROPOSED |
| Business Decision | قرار عمل | قرار صادر عن سلطة مختصة بخيار محدد ومبرر | PRJ§61 | CR-38 | PROPOSED |
| Match Decision | قرار مطابقة | نتيجة مراجعة حالة مطابقة كيانات | PRJ§13 | CR-38 | PROPOSED |
| Collection Requirement | متطلب جمع | حاجة معلوماتية تُوجّه نشاط الجمع | PRJ§7.5 | CR-34 | PROPOSED |
| Task Requirement | شرط مهمة | شرط يجب استيفاؤه لتنفيذ أو إكمال مهمة | PRJ§54 | CR-34 | PROPOSED |
| Task Assignment | إسناد مهمة | ربط مهمة بمنفذ | UC-041 | CR-35 | PROPOSED |
| Asset Assignment | إسناد أصل | ربط أصل بمهمة أو وحدة | UC-053 | CR-35 | PROPOSED |
| Analytical Assessment | تقييم تحليلي | حكم تحليلي مبني على نتائج وأدلة مع عدم يقين | PRJ§59 | CR-36 | PROPOSED |
| Competency Assessment | تقييم كفاءة | قياس كفاءة شخص مقابل متطلبات دور | BP40, BP44 | CR-36 | PROPOSED |
| Exercise Evaluation | تقييم تمرين | تقييم أداء في تمرين أو محاكاة | PRJ§7.19 | CR-43 | PROPOSED |
| AI Evaluation | تقييم نموذج | قياس جودة نموذج أو مخرج AI | PRJ§31 | CR-43 | PROPOSED |
| Business Outcome | نتيجة عمل | أثر مؤسسي مستهدف (OUT-01..06) | PRJ§37 | CR-37 | PROPOSED |
| Plan Outcome | نتيجة خطة | نتيجة قابلة للقياس تستهدفها خطة | PRJ§62 | CR-37 | PROPOSED |
| Authority | صلاحية تقرير | حق مؤسسي في اتخاذ نوع قرار معين | PRJ§7.1, §7.10 | CR-32 | PROPOSED |
| Situation | موقف | سياق تشغيلي محدد مكاناً وزماناً يجمع الكيانات والأحداث والمخاطر | PRJ§60 | ADR-P07 | PROPOSED |
| Assessment Confidence | ثقة | بنية متعددة الأبعاد لا رقم واحد | PRJ§3.8, V5§55 | CR-03 | PROPOSED |
| Projection | إسقاط | نسخة مشتقة قابلة لإعادة البناء (بحث، رسم، تحليلات) | V5 A07 | — | PROPOSED |
| Archive | أرشيف | حفظ مؤسسي طويل الأمد؛ ليس نسخاً احتياطياً | BRL-011 | — | PROPOSED |
| Backup | نسخة احتياطية | نسخة لاستعادة التشغيل | BRL-011 | — | PROPOSED |
| Tenant | مستأجر | وحدة العزل العليا في المنصة | PRJ§6 | UNK-018 | PROPOSED |
| Workspace | مساحة عمل | نطاق عمل داخل مستأجر | PRJ§6 | CR-41 | PROPOSED |
| AIL | مستوى استقلالية AI | AIL0–AIL5 لعمليات الذكاء الاصطناعي في المنتج | ADR-P10 | — | PROPOSED |
| DAL | مستوى صلاحية وكيل الدراسة | DAL0–DAL5 لوكلاء الدراسة | ADR-P10 | — | PROPOSED |
| Design Envelope | نطاق التصميم | الحدود التي يجب أن تتحملها المعمارية دون إعادة تصميم؛ أهداف لا توقعات | W1 Q7 | — | PROPOSED |
| Cell | خلية | وحدة نشر مستقلة تخدم مستأجراً أو مجموعة مستأجرين بنفس الكود | W1 Q6, SR-09 | — | PROPOSED |
| Delegated Decision (DEC) | قرار مفوّض | قرار اتخذه صاحب قرار بالتفويض، يتطلب مصادقة المالك عند G6 | W1 | — | PROPOSED |
| EARS | صيغة المتطلبات المنظمة | Easy Approach to Requirements Syntax: Ubiquitous / Event-driven / State-driven / Unwanted / Optional | V6§13.1 | — | PROPOSED |
| Quality Attribute Scenario | سيناريو جودة | مصدر + محفز + بيئة + مكوّن + استجابة + مقياس | V6 A16 | — | PROPOSED |
| RealWorldEvent | حدث واقعي | شيء وقع في العالم؛ ليس Domain Event | CR-44 | CR-44 | APPROVED_DELEGATED |
| SameAsLink | رابط تطابق | قرار مؤرخ بأن معرّفين لنفس الكيان؛ الدمج والفصل عبره | ER-MODEL | — | APPROVED_DELEGATED |
| Identity Cluster | عنقود هوية | مجموعة كيانات مرتبطة بروابط MATCH سارية | ER-MODEL | — | APPROVED_DELEGATED |
| Resolved View | العرض المحلول | إسقاط القيمة الحالية من الادعاءات والتعارضات والعناقيد | META-MODEL §3 | — | APPROVED_DELEGATED |
| Admiralty Scale | مقياس الأميرالية | موثوقية المصدر A–F ومصداقية المعلومة 1–6 | CONFIDENCE-MODEL | — | APPROVED_DELEGATED |
| Security Version | الإصدار الأمني | عداد يرتفع مع أي تغيير في صلاحيات موضوع أو تسمية كائن؛ يبطل الذاكرات ويُفحص على النتائج | ADR-P06 | — | APPROVED_DELEGATED |
| SecurityContext | سياق الأمان | اللغة المنشورة لـ BC01: هوية الطالب وأدواره وتصريحه وإصداره الأمني، عمر ≤ 60 ث | PL-SECURITY-CONTEXT | — | APPROVED_DELEGATED |
| Platform Baseline Policy | سياسة أساس المنصة | قواعد PB-* لا يتجاوزها المستأجر ولا يُستثنى منها | POLICIES-SLC01 | — | APPROVED_DELEGATED |
| Effective Grant | منحة فعالة | منحة ACTIVE ضمن فترتها وأصلها (إن وُجد) فعال في نفس اللحظة | INV-AUT-03 | — | APPROVED_DELEGATED |
| Current Table | جدول الحالي | إسقاط الادعاءات ذات recorded_to = ∞ يُحدَّث في نفس المعاملة | LIB-CLAIMS-KERNEL §6 | — | APPROVED_DELEGATED |
| Generalize (obligation) | التعميم المكاني | استبدال الهندسة بمركز خلية شبكية حتمية بحد أدنى للدقة | LIB-CLAIMS-KERNEL §5 | — | APPROVED_DELEGATED |
| Visibility-first resolution | الحل بعد تطبيق الرؤية | استبعاد الادعاءات غير المرئية قبل حساب الحالة والعدد والاكتمال | LIB-CLAIMS-KERNEL §3 | — | APPROVED_DELEGATED |
| Blocking | الحجب | تجميع الكيانات بمفاتيح مشتركة لتجنب مقارنة كل زوج | SPEC-ER-CANDIDATES | — | APPROVED_DELEGATED |
| Decision Basis Level | مستوى أساس القرار | أعلى تصنيف كان المراجع يراه عند قرار المطابقة | INV-ER-06 | — | APPROVED_DELEGATED |
| Orthogonal flag | علم متعامد | خاصية مستقلة عن حالة الـ Aggregate تقيّد الأوامر دون تغيير الحالة (مثل suspended) | INV-TASK-06 | — | APPROVED_DELEGATED |
| Eligibility Snapshot | لقطة الأهلية | نتيجة فحص الأهلية المحفوظة في المهمة وقت الإسناد | SPEC-ELIGIBILITY §3 | — | APPROVED_DELEGATED |
| Search Fact | حقيقة بحث | ادعاء حالي مفهرس بتسمياته داخل وثيقة كائنه؛ وحدة المطابقة والفلترة | SPEC-DISCOVERY §3.1 | — | APPROVED_DELEGATED |
| LabelCheck | فحص التسمية | عقد OHS لدى كل سياق مالك يعيد الرؤية الحالية لقائمة URNs لموضوع معين | CR-47 | — | APPROVED_DELEGATED |
| Non-inference (formal) | عدم الاستدلال (تعريف رسمي) | إضافة أي بيانات مخفية عن مستخدم لا تغير أي مخرج يراه (P-51..P-53) | PROP-SLC05 | — | APPROVED_DELEGATED |
| Scope Hash | بصمة نطاق الصلاحية | بصمة للمستأجر والتصريح والأقسام والنطاق التنظيمي والتزامات التعميم؛ مفتاح الذاكرة المؤقتة للبلاطات | SPEC-SITUATION §5 | — | APPROVED_DELEGATED |
| Common Operational Picture | صورة العمليات المشتركة | أعضاء الموقف المرئيون للقارئ على الخريطة مع حالتهم | SPEC-SITUATION §4 | — | APPROVED_DELEGATED |
| Input Pin | تثبيت المدخل | مرجع بيانات مع known_at يضمن قراءة نفس الحالة عند إعادة التشغيل | SPEC-ANALYSIS §2 | — | APPROVED_DELEGATED |
| Analytic Confidence | الثقة التحليلية | تقدير جودة الأساس (أدلة ومنهج) لحكم، منفصل عن احتمال الحدث | SPEC-ANALYSIS §4 | Estimative Probability | APPROVED_DELEGATED |
| Decision Basis | أساس القرار | السلطة والاستشهادات المثبتة والادعاءات كما كانت معروفة لحظة تسجيل القرار | SPEC-PLAN §1 | — | APPROVED_DELEGATED |
| Baseline | خط الأساس | إصدار الخطة المعتمد الساري؛ محتواه لا يتغير | BRL-004 | — | APPROVED_DELEGATED |
| Task Synchronization | مزامنة المهام | فرق حتمي بين خطين أساسيين بمعرفات أنشطة ثابتة ينشئ أو يحل أو يعدل المهام | SPEC-PLAN §3 | — | APPROVED_DELEGATED |
| Command Envelope | غلاف الأمر | أمر ميداني بمعرف عميل وتسلسل وإصدار أساس وزمن جهاز وتوقيع وسلسلة hash | SPEC-FIELD-SYNC §1 | — | APPROVED_DELEGATED |
| Preload Package | حزمة التحميل المسبق | بيانات منطقة عمل مفلترة بصلاحية المستخدم وقت البناء، بتاريخ انتهاء | AGG-PRELOAD-PACKAGE | — | APPROVED_DELEGATED |
| Sync Conflict | تعارض مزامنة | أمر ميداني مغير للحالة لم يُطبق لأن الإصدار تغير؛ ينتظر قراراً بشرياً | AGG-SYNC-CONFLICT | Conflict (claims) | APPROVED_DELEGATED |
| Class-Bucket Key | مفتاح حاوية الفئة | مفتاح تشفير لكل (فئة سجلات × شهر المحفز)؛ إتلافه يتلف الحاوية في كل المخازن والنسخ | SPEC-KEYS-DISPOSITION | — | APPROVED_DELEGATED |
| Restore Gate | بوابة الاستعادة | إعادة تطبيق سجل إتلاف المفاتيح على أي مخزن مفاتيح مستعاد قبل تشغيل الخدمات | CR-51 | — | APPROVED_DELEGATED |
| Label Source | مصدر التسمية | صريح، أو مشتق بقاعدة، أو إداري افتراضي — لكل Aggregate | LABEL-DERIVATION | — | APPROVED_DELEGATED |
| Cell Profile | ملف الخلية | shared / dedicated / sovereign — قيم تهيئة لنفس الإصدار | CELL-ARCHITECTURE | — | APPROVED_DELEGATED |
| Reversal Trigger | مُحفّز المراجعة | شرط قياس صريح يعيد فتح قرار تقني | TECH-DECISIONS | — | APPROVED_DELEGATED |
| Capacity Ledger | دفتر السعة | سجل لكل (مجمع، ساعة) بالسعة والملتزم؛ يمنع تجاوز السعة | SPEC-ALLOCATION §2 | — | APPROVED_DELEGATED |
| Pre-emption | الاستباق | سحب سعة ملتزمة لطلب أعلى أولوية، بقرار سلطة فقط | REQ-RES-009 | — | APPROVED_DELEGATED |
| Archive Package (AIP) | حزمة أرشيفية | حزمة BagIt بمحتوى وبيانات وصفية ومنشأ وبصمات وسجل وصول (OAIS) | SPEC-PKA §4 | Backup | APPROVED_DELEGATED |
| Watermark | علامة مائية | علامة مرئية وغير مرئية فريدة لكل نسخة موزعة تربطها بمستلمها | SPEC-PKA §2 | — | APPROVED_DELEGATED |
| Context Package | حزمة السياق | عناصر مسترجعة بصلاحية المستخدم، مثبتة الإصدار، مختومة بـ hash، تُقدَّم للنموذج كبيانات | SPEC-AI §3 | — | APPROVED_DELEGATED |
| Grounding Verifier | مدقق التأريض | نموذج منفصل يتحقق أن كل عبارة مدعومة بعناصرها المستشهد بها | SPEC-AI §4 | — | APPROVED_DELEGATED |
| EEI (Essential Element of Information) | عنصر معلومات أساسي | جزء من متطلب جمع يحدد ما يُعد إجابة عنه | SPEC-COLLECTION §1 | — | APPROVED_DELEGATED |
| Source Independence | استقلال المصادر | مدخلان من نفس المصدر أو أحدهما مشتق من الآخر يُعدّان مصدراً واحداً في التأكيد | INV-CRP-04 | — | APPROVED_DELEGATED |
| Access Scope (coordination) | نطاق وصول المشارك | أقسام حالة التنسيق التي يراها مشارك بعينه | INV-CRD-02 | — | APPROVED_DELEGATED |
| External Release Level | مستوى الإصدار الخارجي | أعلى تصنيف يُسمح بإصداره خارج المنصة لكل مستأجر (CAP) | SPEC-INTEGRATION §4 | — | APPROVED_DELEGATED |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
terms:
- en: Entity
  ar: كيان
  definition: شيء له هوية مستمرة ويمثل كائناً أو مفهوماً
  source: PRJ§3.2, V5 A05
  disambiguates: null
  status: PROPOSED
- en: Event (Domain Event)
  ar: حدث مجال
  definition: سجل لشيء وقع في زمن محدد داخل سياق
  source: PRJ§3.2, §14
  disambiguates: null
  status: PROPOSED
- en: Integration Event
  ar: حدث تكامل
  definition: نسخة عامة من حدث تُنشر خارج السياق
  source: PRJ§15
  disambiguates: null
  status: PROPOSED
- en: Notification
  ar: إشعار
  definition: رسالة للمستخدم، ليست حدثاً
  source: PRJ§15
  disambiguates: null
  status: PROPOSED
- en: Claim
  ar: ادعاء
  definition: عبارة عن كيان أو علاقة يدعمها دليل وقد تتعارض مع غيرها
  source: PRJ§3.4
  disambiguates: null
  status: PROPOSED
- en: Evidence
  ar: دليل
  definition: مادة تدعم ادعاءً ولا تساويه
  source: V5 A06
  disambiguates: CR-31
  status: PROPOSED
- en: Source
  ar: مصدر
  definition: جهة أو نظام أو مستشعر أنتج معلومة
  source: PRJ§7.5
  disambiguates: null
  status: PROPOSED
- en: Observation
  ar: ملاحظة
  definition: ما رصده مصدر في زمن ومكان
  source: PRJ§7.6
  disambiguates: null
  status: PROPOSED
- en: Provenance
  ar: منشأ
  definition: الأصل الذي جاءت منه المعلومة
  source: PRJ§3.6
  disambiguates: null
  status: PROPOSED
- en: Lineage
  ar: سلسلة الاشتقاق
  definition: تسلسل التحويلات من المصدر إلى النتيجة
  source: PRJ§23
  disambiguates: null
  status: PROPOSED
- en: Event Time
  ar: زمن الحدث
  definition: متى وقع الشيء في الواقع
  source: PRJ§3.5
  disambiguates: null
  status: PROPOSED
- en: Observation Time
  ar: زمن الرصد
  definition: متى رُصد
  source: PRJ§3.5
  disambiguates: null
  status: PROPOSED
- en: Record Time
  ar: زمن التسجيل
  definition: متى عرف النظام المعلومة
  source: PRJ§3.5
  disambiguates: ADR-P01
  status: PROPOSED
- en: Valid Time
  ar: زمن الصلاحية
  definition: الفترة التي تكون فيها المعلومة صحيحة في الواقع
  source: PRJ§3.5
  disambiguates: null
  status: PROPOSED
- en: Effective Time
  ar: زمن السريان
  definition: متى يبدأ أثر قرار أو سياسة
  source: PRJ§3.5
  disambiguates: null
  status: PROPOSED
- en: Access Policy
  ar: سياسة وصول
  definition: قاعدة تقرر السماح أو الرفض لفاعل على مورد
  source: PRJ§7.2
  disambiguates: CR-33
  status: PROPOSED
- en: Governance Policy
  ar: سياسة حوكمة
  definition: قاعدة مؤسسية (احتفاظ، تصنيف، امتثال)
  source: PRJ§7.25
  disambiguates: CR-33
  status: PROPOSED
- en: Policy Knowledge
  ar: معرفة سياساتية
  definition: محتوى معرفي يشرح سياسة، لا ينفذها
  source: PRJ§7.21
  disambiguates: CR-33
  status: PROPOSED
- en: Policy Decision
  ar: قرار سياسة
  definition: 'ناتج تقييم سياسة: ALLOW/DENY/CONDITIONAL/REDACT/AGGREGATE/REQUIRE_APPROVAL'
  source: PRJ§66
  disambiguates: CR-38
  status: PROPOSED
- en: Business Decision
  ar: قرار عمل
  definition: قرار صادر عن سلطة مختصة بخيار محدد ومبرر
  source: PRJ§61
  disambiguates: CR-38
  status: PROPOSED
- en: Match Decision
  ar: قرار مطابقة
  definition: نتيجة مراجعة حالة مطابقة كيانات
  source: PRJ§13
  disambiguates: CR-38
  status: PROPOSED
- en: Collection Requirement
  ar: متطلب جمع
  definition: حاجة معلوماتية تُوجّه نشاط الجمع
  source: PRJ§7.5
  disambiguates: CR-34
  status: PROPOSED
- en: Task Requirement
  ar: شرط مهمة
  definition: شرط يجب استيفاؤه لتنفيذ أو إكمال مهمة
  source: PRJ§54
  disambiguates: CR-34
  status: PROPOSED
- en: Task Assignment
  ar: إسناد مهمة
  definition: ربط مهمة بمنفذ
  source: UC-041
  disambiguates: CR-35
  status: PROPOSED
- en: Asset Assignment
  ar: إسناد أصل
  definition: ربط أصل بمهمة أو وحدة
  source: UC-053
  disambiguates: CR-35
  status: PROPOSED
- en: Analytical Assessment
  ar: تقييم تحليلي
  definition: حكم تحليلي مبني على نتائج وأدلة مع عدم يقين
  source: PRJ§59
  disambiguates: CR-36
  status: PROPOSED
- en: Competency Assessment
  ar: تقييم كفاءة
  definition: قياس كفاءة شخص مقابل متطلبات دور
  source: BP40, BP44
  disambiguates: CR-36
  status: PROPOSED
- en: Exercise Evaluation
  ar: تقييم تمرين
  definition: تقييم أداء في تمرين أو محاكاة
  source: PRJ§7.19
  disambiguates: CR-43
  status: PROPOSED
- en: AI Evaluation
  ar: تقييم نموذج
  definition: قياس جودة نموذج أو مخرج AI
  source: PRJ§31
  disambiguates: CR-43
  status: PROPOSED
- en: Business Outcome
  ar: نتيجة عمل
  definition: أثر مؤسسي مستهدف (OUT-01..06)
  source: PRJ§37
  disambiguates: CR-37
  status: PROPOSED
- en: Plan Outcome
  ar: نتيجة خطة
  definition: نتيجة قابلة للقياس تستهدفها خطة
  source: PRJ§62
  disambiguates: CR-37
  status: PROPOSED
- en: Authority
  ar: صلاحية تقرير
  definition: حق مؤسسي في اتخاذ نوع قرار معين
  source: PRJ§7.1, §7.10
  disambiguates: CR-32
  status: PROPOSED
- en: Situation
  ar: موقف
  definition: سياق تشغيلي محدد مكاناً وزماناً يجمع الكيانات والأحداث والمخاطر
  source: PRJ§60
  disambiguates: ADR-P07
  status: PROPOSED
- en: Assessment Confidence
  ar: ثقة
  definition: بنية متعددة الأبعاد لا رقم واحد
  source: PRJ§3.8, V5§55
  disambiguates: CR-03
  status: PROPOSED
- en: Projection
  ar: إسقاط
  definition: نسخة مشتقة قابلة لإعادة البناء (بحث، رسم، تحليلات)
  source: V5 A07
  disambiguates: null
  status: PROPOSED
- en: Archive
  ar: أرشيف
  definition: حفظ مؤسسي طويل الأمد؛ ليس نسخاً احتياطياً
  source: BRL-011
  disambiguates: null
  status: PROPOSED
- en: Backup
  ar: نسخة احتياطية
  definition: نسخة لاستعادة التشغيل
  source: BRL-011
  disambiguates: null
  status: PROPOSED
- en: Tenant
  ar: مستأجر
  definition: وحدة العزل العليا في المنصة
  source: PRJ§6
  disambiguates: UNK-018
  status: PROPOSED
- en: Workspace
  ar: مساحة عمل
  definition: نطاق عمل داخل مستأجر
  source: PRJ§6
  disambiguates: CR-41
  status: PROPOSED
- en: AIL
  ar: مستوى استقلالية AI
  definition: AIL0–AIL5 لعمليات الذكاء الاصطناعي في المنتج
  source: ADR-P10
  disambiguates: null
  status: PROPOSED
- en: DAL
  ar: مستوى صلاحية وكيل الدراسة
  definition: DAL0–DAL5 لوكلاء الدراسة
  source: ADR-P10
  disambiguates: null
  status: PROPOSED
- en: Design Envelope
  ar: نطاق التصميم
  definition: الحدود التي يجب أن تتحملها المعمارية دون إعادة تصميم؛ أهداف لا توقعات
  source: W1 Q7
  disambiguates: null
  status: PROPOSED
- en: Cell
  ar: خلية
  definition: وحدة نشر مستقلة تخدم مستأجراً أو مجموعة مستأجرين بنفس الكود
  source: W1 Q6, SR-09
  disambiguates: null
  status: PROPOSED
- en: Delegated Decision (DEC)
  ar: قرار مفوّض
  definition: قرار اتخذه صاحب قرار بالتفويض، يتطلب مصادقة المالك عند G6
  source: W1
  disambiguates: null
  status: PROPOSED
- en: EARS
  ar: صيغة المتطلبات المنظمة
  definition: 'Easy Approach to Requirements Syntax: Ubiquitous / Event-driven / State-driven / Unwanted / Optional'
  source: V6§13.1
  disambiguates: null
  status: PROPOSED
- en: Quality Attribute Scenario
  ar: سيناريو جودة
  definition: مصدر + محفز + بيئة + مكوّن + استجابة + مقياس
  source: V6 A16
  disambiguates: null
  status: PROPOSED
- en: RealWorldEvent
  ar: حدث واقعي
  definition: شيء وقع في العالم؛ ليس Domain Event
  source: CR-44
  disambiguates: CR-44
  status: APPROVED_DELEGATED
- en: SameAsLink
  ar: رابط تطابق
  definition: قرار مؤرخ بأن معرّفين لنفس الكيان؛ الدمج والفصل عبره
  source: ER-MODEL
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Identity Cluster
  ar: عنقود هوية
  definition: مجموعة كيانات مرتبطة بروابط MATCH سارية
  source: ER-MODEL
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Resolved View
  ar: العرض المحلول
  definition: إسقاط القيمة الحالية من الادعاءات والتعارضات والعناقيد
  source: META-MODEL §3
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Admiralty Scale
  ar: مقياس الأميرالية
  definition: موثوقية المصدر A–F ومصداقية المعلومة 1–6
  source: CONFIDENCE-MODEL
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Security Version
  ar: الإصدار الأمني
  definition: عداد يرتفع مع أي تغيير في صلاحيات موضوع أو تسمية كائن؛ يبطل الذاكرات ويُفحص على النتائج
  source: ADR-P06
  disambiguates: null
  status: APPROVED_DELEGATED
- en: SecurityContext
  ar: سياق الأمان
  definition: 'اللغة المنشورة لـ BC01: هوية الطالب وأدواره وتصريحه وإصداره الأمني، عمر ≤ 60 ث'
  source: PL-SECURITY-CONTEXT
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Platform Baseline Policy
  ar: سياسة أساس المنصة
  definition: قواعد PB-* لا يتجاوزها المستأجر ولا يُستثنى منها
  source: POLICIES-SLC01
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Effective Grant
  ar: منحة فعالة
  definition: منحة ACTIVE ضمن فترتها وأصلها (إن وُجد) فعال في نفس اللحظة
  source: INV-AUT-03
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Current Table
  ar: جدول الحالي
  definition: إسقاط الادعاءات ذات recorded_to = ∞ يُحدَّث في نفس المعاملة
  source: LIB-CLAIMS-KERNEL §6
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Generalize (obligation)
  ar: التعميم المكاني
  definition: استبدال الهندسة بمركز خلية شبكية حتمية بحد أدنى للدقة
  source: LIB-CLAIMS-KERNEL §5
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Visibility-first resolution
  ar: الحل بعد تطبيق الرؤية
  definition: استبعاد الادعاءات غير المرئية قبل حساب الحالة والعدد والاكتمال
  source: LIB-CLAIMS-KERNEL §3
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Blocking
  ar: الحجب
  definition: تجميع الكيانات بمفاتيح مشتركة لتجنب مقارنة كل زوج
  source: SPEC-ER-CANDIDATES
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Decision Basis Level
  ar: مستوى أساس القرار
  definition: أعلى تصنيف كان المراجع يراه عند قرار المطابقة
  source: INV-ER-06
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Orthogonal flag
  ar: علم متعامد
  definition: خاصية مستقلة عن حالة الـ Aggregate تقيّد الأوامر دون تغيير الحالة (مثل suspended)
  source: INV-TASK-06
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Eligibility Snapshot
  ar: لقطة الأهلية
  definition: نتيجة فحص الأهلية المحفوظة في المهمة وقت الإسناد
  source: SPEC-ELIGIBILITY §3
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Search Fact
  ar: حقيقة بحث
  definition: ادعاء حالي مفهرس بتسمياته داخل وثيقة كائنه؛ وحدة المطابقة والفلترة
  source: SPEC-DISCOVERY §3.1
  disambiguates: null
  status: APPROVED_DELEGATED
- en: LabelCheck
  ar: فحص التسمية
  definition: عقد OHS لدى كل سياق مالك يعيد الرؤية الحالية لقائمة URNs لموضوع معين
  source: CR-47
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Non-inference (formal)
  ar: عدم الاستدلال (تعريف رسمي)
  definition: إضافة أي بيانات مخفية عن مستخدم لا تغير أي مخرج يراه (P-51..P-53)
  source: PROP-SLC05
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Scope Hash
  ar: بصمة نطاق الصلاحية
  definition: بصمة للمستأجر والتصريح والأقسام والنطاق التنظيمي والتزامات التعميم؛ مفتاح الذاكرة المؤقتة للبلاطات
  source: SPEC-SITUATION §5
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Common Operational Picture
  ar: صورة العمليات المشتركة
  definition: أعضاء الموقف المرئيون للقارئ على الخريطة مع حالتهم
  source: SPEC-SITUATION §4
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Input Pin
  ar: تثبيت المدخل
  definition: مرجع بيانات مع known_at يضمن قراءة نفس الحالة عند إعادة التشغيل
  source: SPEC-ANALYSIS §2
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Analytic Confidence
  ar: الثقة التحليلية
  definition: تقدير جودة الأساس (أدلة ومنهج) لحكم، منفصل عن احتمال الحدث
  source: SPEC-ANALYSIS §4
  disambiguates: Estimative Probability
  status: APPROVED_DELEGATED
- en: Decision Basis
  ar: أساس القرار
  definition: السلطة والاستشهادات المثبتة والادعاءات كما كانت معروفة لحظة تسجيل القرار
  source: SPEC-PLAN §1
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Baseline
  ar: خط الأساس
  definition: إصدار الخطة المعتمد الساري؛ محتواه لا يتغير
  source: BRL-004
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Task Synchronization
  ar: مزامنة المهام
  definition: فرق حتمي بين خطين أساسيين بمعرفات أنشطة ثابتة ينشئ أو يحل أو يعدل المهام
  source: SPEC-PLAN §3
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Command Envelope
  ar: غلاف الأمر
  definition: أمر ميداني بمعرف عميل وتسلسل وإصدار أساس وزمن جهاز وتوقيع وسلسلة hash
  source: SPEC-FIELD-SYNC §1
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Preload Package
  ar: حزمة التحميل المسبق
  definition: بيانات منطقة عمل مفلترة بصلاحية المستخدم وقت البناء، بتاريخ انتهاء
  source: AGG-PRELOAD-PACKAGE
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Sync Conflict
  ar: تعارض مزامنة
  definition: أمر ميداني مغير للحالة لم يُطبق لأن الإصدار تغير؛ ينتظر قراراً بشرياً
  source: AGG-SYNC-CONFLICT
  disambiguates: Conflict (claims)
  status: APPROVED_DELEGATED
- en: Class-Bucket Key
  ar: مفتاح حاوية الفئة
  definition: مفتاح تشفير لكل (فئة سجلات × شهر المحفز)؛ إتلافه يتلف الحاوية في كل المخازن والنسخ
  source: SPEC-KEYS-DISPOSITION
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Restore Gate
  ar: بوابة الاستعادة
  definition: إعادة تطبيق سجل إتلاف المفاتيح على أي مخزن مفاتيح مستعاد قبل تشغيل الخدمات
  source: CR-51
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Label Source
  ar: مصدر التسمية
  definition: صريح، أو مشتق بقاعدة، أو إداري افتراضي — لكل Aggregate
  source: LABEL-DERIVATION
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Cell Profile
  ar: ملف الخلية
  definition: shared / dedicated / sovereign — قيم تهيئة لنفس الإصدار
  source: CELL-ARCHITECTURE
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Reversal Trigger
  ar: مُحفّز المراجعة
  definition: شرط قياس صريح يعيد فتح قرار تقني
  source: TECH-DECISIONS
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Capacity Ledger
  ar: دفتر السعة
  definition: سجل لكل (مجمع، ساعة) بالسعة والملتزم؛ يمنع تجاوز السعة
  source: SPEC-ALLOCATION §2
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Pre-emption
  ar: الاستباق
  definition: سحب سعة ملتزمة لطلب أعلى أولوية، بقرار سلطة فقط
  source: REQ-RES-009
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Archive Package (AIP)
  ar: حزمة أرشيفية
  definition: حزمة BagIt بمحتوى وبيانات وصفية ومنشأ وبصمات وسجل وصول (OAIS)
  source: SPEC-PKA §4
  disambiguates: Backup
  status: APPROVED_DELEGATED
- en: Watermark
  ar: علامة مائية
  definition: علامة مرئية وغير مرئية فريدة لكل نسخة موزعة تربطها بمستلمها
  source: SPEC-PKA §2
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Context Package
  ar: حزمة السياق
  definition: عناصر مسترجعة بصلاحية المستخدم، مثبتة الإصدار، مختومة بـ hash، تُقدَّم للنموذج كبيانات
  source: SPEC-AI §3
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Grounding Verifier
  ar: مدقق التأريض
  definition: نموذج منفصل يتحقق أن كل عبارة مدعومة بعناصرها المستشهد بها
  source: SPEC-AI §4
  disambiguates: null
  status: APPROVED_DELEGATED
- en: EEI (Essential Element of Information)
  ar: عنصر معلومات أساسي
  definition: جزء من متطلب جمع يحدد ما يُعد إجابة عنه
  source: SPEC-COLLECTION §1
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Source Independence
  ar: استقلال المصادر
  definition: مدخلان من نفس المصدر أو أحدهما مشتق من الآخر يُعدّان مصدراً واحداً في التأكيد
  source: INV-CRP-04
  disambiguates: null
  status: APPROVED_DELEGATED
- en: Access Scope (coordination)
  ar: نطاق وصول المشارك
  definition: أقسام حالة التنسيق التي يراها مشارك بعينه
  source: INV-CRD-02
  disambiguates: null
  status: APPROVED_DELEGATED
- en: External Release Level
  ar: مستوى الإصدار الخارجي
  definition: أعلى تصنيف يُسمح بإصداره خارج المنصة لكل مستأجر (CAP)
  source: SPEC-INTEGRATION §4
  disambiguates: null
  status: APPROVED_DELEGATED
```

</details>
