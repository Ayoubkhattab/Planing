---
id: AD-17-SECURITY-DESIGN
type: security-design
title: "تصميم الأمن — المصادقة والتخويل والتصنيف والمفاتيح والتدقيق والتهديدات"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 4)"
sources: [08-security/authorization-model.md, 08-security/classification-scheme.md, 08-security/label-derivation-rules.md, 08-security/trust-boundaries.md, 08-security/data-protection.md, 08-security/key-hierarchy-and-disposition.md, 08-security/audit-architecture.md, 08-security/threat-model*.md, 08-security/privacy-threats.md, 08-security/policies-slc*.md, 00-governance/decisions/ADR-P19.md, 12-solution/technology-decisions.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# تصميم الأمن

كيف يحمي النظام البيانات والعمليات: من يدخل (المصادقة)، وماذا يحق له (التخويل)، وما الذي يراه (التصنيف)، وكيف تُحمى البيانات وتُتلف (المفاتيح)، وكيف يُثبت ما حدث (التدقيق)، ومن ماذا نحمي (التهديدات). المصادر المعتمدة في `08-security/`؛ هذا الملف يجمعها في تصميم واحد قابل للتنفيذ، ويحسم ما تركته مفتوحًا.

## 1. المبادئ

| المبدأ | التطبيق | المصدر |
|---|---|---|
| لا ثقة ضمنية داخل الخلية | كل استدعاء بين الخدمات بـmTLS وهوية عبء عمل، وكل تطبيق يتحقق من SecurityContext موقّع | TB-02، `authorization-model.md` §6 |
| القرار قبل أي استرجاع | منفذ التخويل قبل أي قراءة لأمر أو استعلام أو بحث أو خريطة أو تصدير أو اشتراك أو استرجاع AI | REQ-FND-010، FIT-03 |
| الفشل يعني الرفض | تعطل محرك السياسات أو خطؤه → رفض | REQ-FND-013، FIT-16، QAS-SEC-005 |
| عدم الإفصاح | المورد غير المرئي لا يُكشف وجوده بعدد ولا وجه ولا ترتيب ولا توقيت ولا خطأ | ADR-P06، QAS-SEC-002، QAS-SEC-011 |
| حاجزان للمستأجر | فلتر المستأجر في التطبيق + RLS في قاعدة البيانات؛ والخلية المخصصة للمستأجر السيادي أو المخصص، ولأعلى مستوى في مخطط التصنيف (`requires_dedicated_cell`) | ADR-P04، FIT-02، REQ-FND-004 |
| فصل المشغّل عن البيانات | مشغلو المنصة لا يقرؤون بيانات المستأجر ولا يملكون مفاتيحه؛ break-glass بشخصين ومدة وتدقيق | TB-09، THR-014، `data-protection.md` |
| الخصوصية بالتصميم | مفتاح لكل صاحب بيانات، تقييد الغرض، REDACT وAGGREGATE | ADR-P08، PRV-01..07 |

## 2. المصادقة

| الهوية | الآلية | التفاصيل | المصدر |
|---|---|---|---|
| المستخدم البشري | OIDC أو SAML عبر مزوّد هوية المستأجر فقط | Keycloak لكل خلية وسيطًا اتحاديًا؛ رموز قصيرة العمر مربوطة بالجهاز؛ TLS 1.3؛ حماية CSRF؛ حدود معدل عند البوابة | REQ-FND-005، TD-09، TB-01، THR-001 |
| التزويد | SCIM من مزوّد الهوية إلى خدمة التزويد في BC01 (AGG-USER) | حساب SCIM ينشئ مستخدمين PENDING ويربط الهويات فقط، ولا يسند أدوارًا أبدًا (الأدوار عبر `CMD-RAS-ASSIGN` فقط)؛ التعطيل عبر SCIM نافذ خلال ≤ 5 دقائق في كل الجلسات | REQ-FND-005، THR-S01-01، QAS-SEC-008 |
| المصادقة المعززة | 33 أمرًا تشترط `mfa` (§12.3)؛ الجلسة الأضعف تُرفض بـ`401 MFA_STEP_UP_REQUIRED` مع تحدٍ بقوة المصادقة المطلوبة، ثم يعيد العميل المحاولة بنفس `Idempotency-Key` | ADR-P19 |
| الخدمة | هوية عبء عمل لكل تطبيق (mTLS)؛ حسابات الخدمة (AGG-SERVICE-ACCOUNT) للمحوّلات وSCIM بمفاتيح عامة وصلاحية ≤ 90 يومًا (THR-S01-11)؛ الطلب الداخلي يحمل SecurityContext المستخدم الأصلي ولا يرفع الصلاحية باسمه | `authorization-model.md` §6، TB-02، THR-003 |
| الجهاز الميداني | تسجيل الجهاز ومفتاحه (AGG-DEVICE)؛ الأوامر دون اتصال موقّعة بمفتاح الجهاز ومتسلسلة (`seq`، `prev_hash`) | TB-07، THR-S03-05، `openapi-field-slc11.md` |
| مشغّل المنصة | مستوى تشغيل منفصل؛ لا وصول لبيانات المستأجر إلا break-glass بموافقة شخصين ومدة محددة وتدقيق | TB-09 |

البوابة (DU-01) تتحقق من الرمز وتصدر SecurityContext موقّعًا؛ `tenant_id` يُشتق من الرمز لا من الطلب (THR-002)، والتطبيقات لا تثق بترويسة غير موقّعة.

## 3. التخويل

### 3.1 المكوّنات

| المكوّن | الموقع | المسؤولية |
|---|---|---|
| PEP | منفذ التخويل في كل وحدة (ADR-P17) والبوابة | يبني طلب القرار، يستدعي PDP قبل أي استرجاع، يطبق القرار والالتزامات |
| PDP | سياسات OPA مترجمة من جداول القرار إلى Rego، حزم موقّعة، تُقيَّم مضمَّنة في كل وحدة (TD-08)؛ وخدمة القرار `QRY-PDP-DECIDE` في BC08 | يقيّم السياسات النافذة بزمن سريانها؛ 10,000 قرار/ث بزمن p95 ≤ 5 مللي ث مضمَّنًا (QAS-PERF-009) |
| PIP | BC01 (الهوية، التنظيم، السلطة، التصريح)، تسمية الكائن، السياق | سمات الموضوع والمورد |
| Policy Store | BC08 (AGG-POLICY-SET) | سياسات T2 بإصدارات وزمن سريان (REQ-GOV-009) |

### 3.2 ترتيب التقييم

`authorization-model.md` §3: تطابق المستأجر ← قاعدة التصنيف ← الصلاحية (RBAC: الدور يمنح الإجراء على نوع المورد ضمن نطاق تنظيمي) ← السمات (ABAC: الغرض والوقت والجهاز والولاية والتحفظات) ← فصل المهام ← الالتزامات (الأشد يغلب). الصلاحيات الثمانية (View، Edit، Export، Share، Approve، Delete، Retain، Archive) تُمنح منفصلة (REQ-FND-014، §12.2).

### 3.3 في خط الأوامر والاستعلامات

| الخطوة (ADR-P17) | ما يحدث | النتيجة عند الرفض |
|---|---|---|
| 2. تخويل أولي قبل أي وصول | المستأجر والإجراء على نوع المورد | `404` (لم يُحمَّل شيء بعد) |
| 5. تخويل كامل بسمات المورد المحمَّل | التصنيف، المالك، الحالة، المشاركون، فصل المهام | `404` إن كان المورد غير مرئي، `403 AUTHZ_DENIED` إن كان مرئيًا أو كان الأمر إنشاءً (ADR-P19 الذي يعدّل البند 5 من ADR-P06)؛ `SEGREGATION_OF_DUTIES` (422) |
| 6. الالتزامات قبل التنفيذ | `mfa`؛ `legal-hold check` في أوامر المحو | `401 MFA_STEP_UP_REQUIRED`؛ `LEGAL_HOLD_ACTIVE` |
| 9. الحفظ | سجل التدقيق مع الحالة في نفس المعاملة | `AUDIT_UNAVAILABLE` |
| 10. الالتزامات بعد التنفيذ | تفاصيل التدقيق، `watermark`، `notify…` | — |
| الاستعلام | `allowed_scope` من التقييم الجزئي قبل العدّ والترتيب؛ إعادة فحص النتائج (إصدار الأمن للموضوع، `LabelCheck` مجمّعًا لكل صفحة — CR-47) | قائمة بلا المخفي؛ العنصر المخفي `404` |

### 3.4 قرارات السياسة

| القرار | السلوك | المصدر |
|---|---|---|
| ALLOW | تنفيذ مع الالتزامات | REQ-FND-012 |
| DENY | `404` أو `403` كما في §3.3 | ADR-P06 (البند 5 معدَّل)، ADR-P19 |
| CONDITIONAL | شروطه التزامات: قبل التنفيذ (`mfa`، `legal-hold check`) أو بعده | ADR-P19 |
| REDACT | النتيجة بلا الحقول المحجوبة (مثل البيانات الشخصية لغير الغرض المسموح — POL-PERSONAL-DATA) | `authorization-model.md` §4 |
| AGGREGATE | إحصاءات بحد أدنى للمجموعة 5 (PRV-02) | POL-AGG-STATS |
| REQUIRE_APPROVAL | `403 APPROVAL_REQUIRED` باسم دور المعتمِد؛ لا سير موافقة عام. استثناء: Aggregate يمثل الموافقة حالةً ينتقل إليها (AGG-ALLOCATION → `PENDING_APPROVAL`) | ADR-P19 |

### 3.5 ذاكرة القرارات والإلغاء

قرارات ALLOW تُخزن ≤ 60 ثانية بمفتاح يتضمن `security_version` للموضوع والمورد. أي حدث مؤثر أمنيًا (§12.8) يرفع الإصدار، ويُبث `EVT-SEC-VERSION-INCREMENTED` على قناة الأولوية فتُبطل الذاكرة فورًا في كل نقاط الفرض والإسقاطات؛ سحب قسم من مستخدم نافذ في الطلب التالي في كل المسارات بغض النظر عن تأخر الفهارس (QAS-SEC-003).

## 4. التصنيف والتسميات

| البند | التصميم | المصدر |
|---|---|---|
| المخطط | لكل مستأجر: مستويات مرتبة (افتراضيًا PUBLIC، INTERNAL، CONFIDENTIAL، SECRET)، أقسام بلا حد، تحفظات إفراج، عتبة تدقيق القراءة، مستوى افتراضي | `classification-scheme.md` §1، §3 |
| قاعدة القراءة | رتبة التصريح ≥ رتبة المستوى ∧ أقسام التسمية ⊆ أقسام التصريح ∧ كل تحفظ مستوفى ∧ نفس المستأجر ∧ قرار السياسة | REQ-GOV-003، `classification-scheme.md` §2 |
| أعلى مستوى في المخطط | خلية مخصصة (العلم `requires_dedicated_cell`؛ في المخطط الافتراضي SECRET) | ADR-P04، `classification-scheme.md` §1، §3 |
| التركيب | الكائن المركب يأخذ أعلى تصنيف ومجموع الأقسام، إلا بخفض موثق بسلطة يُسجل إصدارًا | REQ-GOV-004 |
| مصدر التسمية | لكل Aggregate مصدر معروف: صريح أو مشتق بقاعدة أو إداري افتراضي (§12.7) | SL-29، `label-derivation-rules.md` |
| تغيير التصنيف | أوامر `*-RECLASSIFY` بسلطة سياسة المستأجر، إصدار جديد، وحدث مؤثر أمنيًا | REQ-GOV-004 |
| المصدر البشري المحمي | هويته افتراضيًا أعلى بدرجة من معلوماته، ولا تظهر في أي استجابة أو تصدير أو نسب دون صلاحية الحماية | QAS-SEC-009 |

## 5. حسم الفاعل للأوامر الـ26

26 سياسة أمر تسرد أدوارًا بأفعالها ولا يشمل أيٌّ منها فعل الأمر (`02-actors-roles.md` §6.6 قبل هذا الحسم). الحسم بقاعدة واحدة: **الفعل المقابل في السياسة نفسها** (resume ↔ pause/suspend، enable ↔ disable، retire ↔ deprecate/define/register، أعمال الصيانة ↔ condition)، مع إبقاء ما يعادل التفعيل للشخص الثاني، وبشرط ألا يخالف الحسم شرط الانتقال (`CMD-DEV-ROTATE-KEY` لا يوقّعه إلا حامل الجهاز). استثناءان معلَّمان في الجدول: `CMD-MDL-RETIRE` و`CMD-TOL-RETIRE`. و`CMD-ADP-RESUME` للشخص الثاني يحتاج قاعدة فصل مهام تضاف بـCR-77. الجدول في §12.1 مولَّد من قائمة واحدة في المولِّد (`ACTOR_RESOLUTION`) تستخدمها قصص المستخدم والفاعلون وحالات الاستخدام. الحسم **قرار تصميم مفوَّض** ينقله CR-77 إلى ملفات السياسات.

## 6. حماية البيانات والمفاتيح

| البند | التصميم | المصدر |
|---|---|---|
| النقل | TLS 1.3 خارجيًا، mTLS داخليًا | `data-protection.md` |
| التخزين | تشفير بمفاتيح المستأجر الملفوفة بمفتاح رئيسي في KMS/HSM محلي (`data-protection.md`)، عبر OpenBao Transit وKEKs في HSM الموقع (TD-07)؛ وتتفرع منها مفاتيح الفئة-الحاوية والموضوع أدناه | `data-protection.md`، TD-07 |
| هرمية المفاتيح | KEK المستأجر في HSM؛ تحته: مفتاح فئة-حاوية (وحدة الإتلاف)، مفتاح الموضوع (وحدة المحو)، مفتاح التجميد (لإعادة لف المجمَّد) | `key-hierarchy-and-disposition.md` §1 |
| البيانات الشخصية | مشفرة مرتين: بمفتاح الموضوع ومفتاح الفئة-الحاوية؛ إتلاف أيهما يكفي | المصدر نفسه |
| الإتلاف | يومي لكل جدول احتفاظ نافذ؛ اعتماد شخصين؛ فحص التجميد قبل التنفيذ؛ إتلاف مفتاح الحاوية وسجل إتلاف وشاهد | §2 من المصدر، QAS-GOV-001 |
| المحو | إتلاف مفاتيح الموضوع في BC01/BC02 وتأكيد كل سياق إفراغ نسخه الواضحة ≤ 24 ساعة؛ النسخ الاحتياطية غير قابلة للاسترجاع فورًا | REQ-GOV-008، QAS-PRV-001 |
| بوابة الاستعادة | سجل إتلاف لا يُستعاد من نسخ أقدم يُعاد تطبيقه قبل فتح أي خدمة بعد استعادة مخزن المفاتيح | CR-51، FIT-19، QAS-PRV-002 |
| الجهاز الميداني | SQLCipher بمفتاح مربوط بالمستخدم والجهاز؛ مسح عن بعد؛ إلغاء الحزم عند خفض التصريح | TD-16، QAS-SEC-007، QAS-OFF-002 |
| السجلات التقنية | بلا محتوى أعمال أو بيانات شخصية؛ معرّفات فقط | `data-protection.md` |

### 6.1 ضوابط إضافية من نماذج التهديد والحماية

| الضابط | التفصيل | المصدر |
|---|---|---|
| روابط التنزيل | موقّعة، صالحة ≤ 5 دقائق، مربوطة بالموضوع والمستأجر | THR-S02-05 |
| فحص المرفقات | فحص البرمجيات الخبيثة وحجر قبل الإتاحة (`SYS:scan passed`) | THR-S02-04، AGG-ATTACHMENT |
| العلامة المائية | على التوزيع والمنتجات حيث تنص السياسة | THR-S12-P2، POL-DST |
| سلسلة الإمداد | صور موقّعة (cosign) ومثبتة بالبصمة من سجل Harbor الداخلي، وSBOM | TD-12، TD-17، THR-019 |
| ذاكرة المفاتيح | ≤ 10 دقائق في الذاكرة، وتُفرَّغ فورًا عند حدث إتلاف | `key-hierarchy-and-disposition.md` §1 |
| نسخ مخزن المفاتيح | ≤ 35 يومًا ثم تختفي فيزيائيًا | المصدر نفسه §4 |
| تدوير المفاتيح | دوري، وإعادة لف فورية عند الاشتباه؛ KMS/HSM في الطبقة الحرجة | `data-protection.md` |
| الإسقاطات | الحقول الشخصية تُفهرس كرموز مطبّعة فقط وفق السياسة؛ الملفات المؤقتة مشفرة وتُحذف بانتهاء المهمة | `data-protection.md` |
| سلامة التدقيق | سجل بحقول ثابتة (الفاعل، الإجراء، المورد، الغرض، قرار السياسة، النتيجة)؛ إعادة حساب السلاسل يوميًا؛ كشف فجوات الشحن بمقارنة العدادات | `audit-architecture.md` القاعدتان 2 و5، REQ-FND-015 |

## 7. التدقيق

كل أمر يكتب سجل تدقيق في `audit_outbox` سياقه في نفس معاملة الحالة؛ ناقل يشحنه إلى مخزن BC08 خلال ≤ 5 ثوانٍ، فيُرقَّم لكل (مستأجر، جزء) ويُسلسل بسلسلة hash، ويُثبَّت جذر Merkle كل 5 دقائق في مخزن لا يُكتب إلا مرة. قراءة بيانات فوق عتبة التدقيق تُدقق أيضًا. تعطل مخزن BC08 لا يوقف الأوامر حتى يتجاوز التراكم 24 ساعة أو 80 % من السعة، فتُرفض الأوامر المغيرة للحالة (`AUDIT_UNAVAILABLE`). البحث في التدقيق للمدقق ومسؤول الأمن، ويُدقَّق بدوره (`audit-architecture.md`، REQ-FND-015/016، QAS-AUD-001، QAS-SEC-006).

## 8. العزل والولاية والحصص

| البند | التصميم | المصدر |
|---|---|---|
| المستأجر | `tenant_id` أول عمود في كل مفتاح وفهرس ووثيقة وحدث ومسار كائن؛ RLS؛ حساب خدمة لكل سياق | FIT-02، TB-03، QAS-SEC-001 |
| الخلية | لا مسار بيانات بين الخلايا؛ الترحيل تصدير واستيراد معتمد | TB-05 |
| الولاية | كل البيانات داخل الولاية المهيأة إلا ما تسمح به سياسة المستأجر صراحة؛ خروج الشبكة مرفوض افتراضيًا عبر بوابة خروج بقائمة سماح، وأي خروج خارجها تنبيه P1 | REQ-GOV-005، `cell-architecture.md` §3 |
| الحصص | حصص وحدود معدل لكل مستأجر للطلبات والتخزين والأحداث والمهام → `RATE_LIMITED` (429) | REQ-FND-018 |
| AI (R2) | صلاحيات المستخدم الطالب فقط، مستوى الاستقلالية (AIL)، سجل Context Package، لا خروج للسياق من الخلية | TB-08، QAS-AI-004 |

## 9. التحقق الأمني

| الآلية | ما تتحقق منه |
|---|---|
| FIT-02، FIT-03، FIT-16، FIT-19، FIT-01، FIT-12 | المستأجر في كل مخزن؛ القرار قبل الوصول؛ الفشل يرفض؛ بوابة الاستعادة؛ لا وصول عابر؛ لا اعتماد على الإنترنت |
| QAS-SEC-001..013 | الفشل المغلق (QAS-SEC-005)، العزل، الاستدلال (الأعداد والأوجه والترتيب والتوقيت)، الإلغاء الفوري، البلاطات، الأجهزة، SCIM، المصادر المحمية، التنبيهات، تشغيلات التحليل |
| QAS-PRV-001/002، QAS-AUD-001، QAS-GOV-001، QAS-AI-004 | المحو، الاستعادة، اكتمال التدقيق، الإتلاف، حقن الأوامر في AI |
| سيناريوهات القبول | رفض `AUTHZ_DENIED` وفصل المهام في كل قصة (`05-user-stories/`) |

## 10. فجوات

| البند | الحالة |
|---|---|
| 5 Aggregates بلا قاعدة اشتقاق تسمية: EXERCISE، LOGISTICS-REQUEST، SCENARIO، SHIPMENT، SIMULATION (شرائح R3) | **[Missing]** — S-26 في `00-index.md` §6 |
| مدة الرموز وسياسة الجلسة بالأرقام | **[Missing]** — «رموز قصيرة العمر» دون رقم (TB-01) |
| آلية break-glass بالتفصيل (من يوافق، المدة القصوى، الإشعار) | **[Missing]** — مبدأ في TB-09 فقط؛ تُفصَّل في `22-deployment-design.md` |
| تصدير جماعي يحتاج موافقة | **[Missing]** — Aggregate صريح لاحقًا (ADR-P19) |
| عدد الأوامر المسموحة دون اتصال (6 أو 12) | محسوم: 12 (قرار مالك المشروع، CR-79، `20-integration-design.md` §7) |

## 11. التطبيق في الكود

`11-hexagonal-reference.md` §5: منافذ Authorization (PEP) وSecurityContext وResult Re-check وEncryption / Keys في حلقة المنافذ؛ ومحوّلاتها (OPA مضمَّن، سمات BC01، OpenBao) في حلقة المحوّلات؛ خط الأوامر يفرض الخطوات 2 و5 و6 و10 بنيويًا، فلا يستطيع معالج أن يتجاوزها (FIT-20).

## 12. الجداول المولَّدة

<!-- BEGIN GENERATED: build_analysis_design.py -->

### 12.1 حسم الفاعل للأوامر الـ26 (CR-77)

| الأمر | الأدوار في السياسة | الفاعل المحسوم | المبرر |
|---|---|---|---|
| `CMD-ADP-RESUME` | Administrator (register, update) · second Administrator (activate) | **second Administrator** | إعادة التشغيل تعادل التفعيل (activate) فتبقى للشخص الثاني؛ يتطلب قاعدة فصل مهام ≠ من أوقفه تضاف بـCR-77 |
| `CMD-ADP-RETIRE` | Administrator (register, update) · second Administrator (activate) | **Administrator** | نهاية دورة حياة يملكها من سجّل المحوّل |
| `CMD-ADP-SUSPEND` | Administrator (register, update) · second Administrator (activate) | **Administrator** | إيقاف فوري للاحتواء، مقابل register/update |
| `CMD-AMT-DEPRECATE` | Analysis lead (register) · second lead or Administrator (activate) | **Analysis lead** | مقابل register؛ التفعيل وحده للشخص الثاني |
| `CMD-AMT-RETIRE` | Analysis lead (register) · second lead or Administrator (activate) | **Analysis lead** | مقابل register |
| `CMD-AST-FAIL-MAINTENANCE` | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | **Resource Manager** | عمليات الحالة الفنية (condition) |
| `CMD-AST-MARK-UNSERVICEABLE` | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | **Resource Manager** | عمليات الحالة الفنية (condition) |
| `CMD-AST-RECOVER` | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | **Resource Manager** | مقابل lost (الإبلاغ عن الفقد) |
| `CMD-AST-RETURN-TO-SERVICE` | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | **Resource Manager** | عمليات الحالة الفنية (condition) |
| `CMD-AST-START-MAINTENANCE` | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify) | **Resource Manager** | عمليات الحالة الفنية (condition) لمدير الموارد |
| `CMD-CRR-RETIRE` | Analyst lead (define, edit) · second approver (activate) | **Analyst lead** | مقابل define/edit؛ التفعيل وحده للمعتمِد الثاني |
| `CMD-DEV-ROTATE-KEY` | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override) | **user** | الشرط «signed by current key; new public key» لا يستوفيه إلا حامل الجهاز |
| `CMD-ER-PARK` | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | **Analyst** | مقابل review/decide؛ الشخص الثاني للتأكيد والتقسيم فقط |
| `CMD-ER-RESUME` | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | **Analyst** | مقابل review/decide |
| `CMD-ER-WITHDRAW` | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | **Analyst** | مقابل propose |
| `CMD-MDL-RETIRE` | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate) | **AI governance authority** | **استثناء من القاعدة** (القاعدة تعطيه للمهندس عبر deprecate): الإيقاف النهائي من حالة DEPRECATED يقابل reinstate لدى سلطة الحوكمة |
| `CMD-OBS-AMEND` | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | **Field User / Operator / Analyst / adapter service account** | تعديل الملاحظة لمن سجّلها (record) |
| `CMD-OBS-ATTACH-EVIDENCE` | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | **Field User / Operator / Analyst / adapter service account** | إرفاق الدليل لمن سجّل الملاحظة (record) |
| `CMD-OBS-RECLASSIFY` | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | **Analyst** | إعادة التصنيف لمن يتحقق من الملاحظة (validate) |
| `CMD-PTM-RETIRE` | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | **Knowledge Manager / Analysis lead** | مقابل define/edit |
| `CMD-SIT-RESUME` | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | **Analyst / Manager** | مقابل pause |
| `CMD-SRC-REINSTATE` | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | **Analyst** | مقابل suspend |
| `CMD-SRC-RETIRE` | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | **Analyst** | مقابل register |
| `CMD-SRC-SUSPEND` | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | **Analyst** | مقابل register/rate؛ المصدر المحمي يبقى لمسؤول الأمن عبر protection |
| `CMD-TOL-ENABLE` | AI platform engineer (register) · Security Officer (activate, disable) | **Security Officer** | مقابل disable |
| `CMD-TOL-RETIRE` | AI platform engineer (register) · Security Officer (activate, disable) | **Security Officer** | **استثناء من القاعدة** (القاعدة تعطيه للمهندس عبر register): تفعيل الأداة وتعطيلها لمسؤول الأمن، فإيقافها النهائي له |

### 12.2 مصفوفة الدور × نوع الصلاحية (REQ-FND-014)

أنواع الصلاحية الثمانية في REQ-FND-014 تُمنح منفصلة. كل أمر يُنسب إلى نوع بفعله **[Derived]** (approve/activate/publish → Approve؛ retire/cancel/erase/dispose → Delete؛ التجميد والاحتفاظ → Retain؛ الأرشفة → Archive؛ التوزيع والتصدير → Export؛ الإشراك والتفويض → Share؛ الباقي → Edit)، وكل استعلام → View عدا التنزيل والاسترجاع (`QRY-ATT-DOWNLOAD`، `QRY-RUN-ARTIFACT`، `QRY-ARC-RETRIEVE`) → Export. الأرقام عدد العمليات.

| الدور | View | Edit | Approve | Delete | Retain | Archive | Export | Share |
|---|---|---|---|---|---|---|---|---|
| ACT-01 Executive | 1 | — | 2 | — | — | — | — | — |
| ACT-02 Manager | 4 | 27 | 5 | 6 | — | — | 1 | 1 |
| ACT-03 Planner | 2 | 48 | 2 | 9 | — | — | — | — |
| ACT-04 Analyst | 11 | 102 | 5 | 21 | — | — | — | — |
| ACT-05 Operator | — | 2 | — | 1 | — | — | — | — |
| ACT-06 Field User | 2 | 5 | — | 1 | — | — | — | — |
| ACT-07 Resource Manager | 1 | 28 | — | 4 | — | — | — | — |
| ACT-08 Logistics User | — | 8 | — | 1 | — | — | — | — |
| ACT-09 Risk Manager | 1 | 1 | — | — | — | — | — | — |
| ACT-10 Training Manager | 1 | 17 | 2 | 4 | — | — | — | — |
| ACT-11 Knowledge Manager | — | 3 | 2 | 2 | — | — | — | — |
| ACT-12 Archivist | 4 | 1 | — | 1 | 3 | 3 | — | — |
| ACT-13 Security Officer | 9 | 19 | 8 | 6 | — | — | — | — |
| ACT-14 Auditor | 14 | 1 | — | 1 | — | — | — | — |
| ACT-15 Administrator | 10 | 41 | 8 | 10 | — | — | — | — |
| PLT-OPS مشغّل المنصة | 2 | 8 | 1 | 2 | — | — | — | — |
| PLT-AI مهندس/حوكمة الذكاء الاصطناعي | 3 | 11 | 2 | 2 | — | — | — | — |
| PLT-INT مهندس التكامل | 2 | 6 | 1 | 1 | — | — | — | — |
| AUTH-LEGAL السلطة القانونية والامتثال | 4 | 2 | 3 | 1 | 6 | — | — | — |
| AUTH-GRANT صاحب سلطة أو معتمِد ثانٍ | 2 | 8 | 9 | 4 | — | 1 | — | 1 |
| REL-TASK المنفّذ والمراجع | 4 | 20 | 5 | 2 | — | — | — | — |
| REL-OWNER المالك والطالب والمشارك | 15 | 30 | 1 | 6 | — | — | 1 | 1 |
| REL-RECIPIENT المستلم والمشترك | 1 | 5 | — | — | — | — | — | — |
| REL-INCIDENT أدوار الحادثة | 1 | 8 | 1 | 1 | — | — | — | — |
| REL-RISK أدوار الخطر | 1 | 4 | — | — | — | — | — | — |
| REL-PEER الشخص الثاني | — | 4 | 1 | — | — | — | — | — |
| ANY-USER أي مستخدم مخوَّل | 71 | 8 | — | 2 | — | — | 3 | — |
| SYS هويات النظام والخدمات | 6 | 31 | — | 4 | — | — | — | — |

### 12.3 أوامر تشترط المصادقة المعززة (33)

التزام `mfa` قبل التنفيذ: جلسة بقوة مصادقة أدنى تُرفض بـ`401 MFA_STEP_UP_REQUIRED` (ADR-P19، الخطوة 6 في خط الأوامر).

| الأمر | السياق | الالتزامات | الفاعل |
|---|---|---|---|
| `CMD-ATT-ERASE` | BC02 | audit; mfa; legal-hold check | user with write permission on the target object |
| `CMD-AUT-APPROVE-GRANT` | BC01 | audit; mfa | Executive in scope |
| `CMD-CAP-RELEASE` | BC03 | audit; mfa | release authority |
| `CMD-CLR-APPROVE` | BC01 | audit; mfa | Security Officer |
| `CMD-CLR-GRANT` | BC01 | audit; mfa | Security Officer |
| `CMD-CLS-ACTIVATE` | BC08 | audit; mfa | Security Officer |
| `CMD-CON-ACTIVATE` | BC07 | audit; mfa | Security Officer ≠ requester |
| `CMD-DEC-ANNUL` | BC04 | audit; mfa | higher authority |
| `CMD-DEC-RECORD` | BC04 | audit; mfa | authority holder |
| `CMD-DEV-CONFIRM` | BC01 | audit; mfa | Administrator / MDM policy |
| `CMD-DEV-RETIRE` | BC01 | audit; mfa | Administrator / MDM policy · Security Officer |
| `CMD-DSP-APPROVE` | BC08 | audit; mfa | Records/Legal authority ≠ submitter |
| `CMD-DSP-CANCEL` | BC08 | audit; mfa | Archivist |
| `CMD-DSP-SUBMIT` | BC08 | audit; mfa | Archivist |
| `CMD-ERS-APPROVE` | BC08 | audit; mfa | Legal authority ≠ registrar |
| `CMD-ERS-REGISTER` | BC08 | audit; mfa | Privacy officer / Legal |
| `CMD-ERS-REJECT` | BC08 | audit; mfa | Legal authority ≠ registrar |
| `CMD-EXC-APPROVE` | BC08 | audit; mfa | Security Officer |
| `CMD-LHD-APPROVE-RELEASE` | BC08 | audit; mfa | Legal/Compliance authority |
| `CMD-LHD-CANCEL-RELEASE` | BC08 | audit; mfa | Legal/Compliance authority |
| `CMD-LHD-EXTEND` | BC08 | audit; mfa | Legal/Compliance authority |
| `CMD-LHD-PLACE` | BC08 | audit; mfa | Legal/Compliance authority |
| `CMD-LHD-REQUEST-RELEASE` | BC08 | audit; mfa | Legal/Compliance authority |
| `CMD-PER-ERASE` | BC01 | audit; mfa; legal-hold check | Administrator with org scope ⊇ person's unit |
| `CMD-PLV-APPROVE` | BC04 | audit; mfa | approver with plan-approval authority ≠ author |
| `CMD-POL-APPROVE` | BC08 | audit; mfa | Security Officer |
| `CMD-PRJ-PROMOTE` | BC07 | audit; mfa for PROMOTE | Platform Operator (platform tenant) |
| `CMD-RTS-ACTIVATE` | BC08 | audit; mfa | Legal/Compliance authority |
| `CMD-RTS-DISCARD` | BC08 | audit; mfa | Archivist |
| `CMD-RTS-DRAFT` | BC08 | audit; mfa | Archivist |
| `CMD-RTS-EDIT` | BC08 | audit; mfa | Archivist |
| `CMD-SRC-SET-PROTECTION` | BC02 | audit; mfa | Security Officer |
| `CMD-TEN-START-DECOMMISSION` | BC01 | audit; mfa | Platform Operator (platform tenant) |

### 12.4 قواعد فصل المهام (44)

تُقيَّم في منفذ التخويل بعد تحميل المورد (الخطوة 5)، ويعيد المجال فحص ما يقابلها من ثوابت (`09-business-rules.md`).

| الأمر | السياق | القاعدة |
|---|---|---|
| `CMD-ADP-ACTIVATE` | BC07 | approver ≠ author |
| `CMD-ALC-APPROVE` | BC05 | approver ≠ requester |
| `CMD-AMT-ACTIVATE` | BC03 | approver ≠ author |
| `CMD-ASM-PUBLISH` | BC03 | reviewer ≠ author |
| `CMD-AUT-APPROVE-GRANT` | BC01 | approver ≠ requester |
| `CMD-AUT-DELEGATE` | BC01 | delegate ≠ delegator |
| `CMD-CAP-RELEASE` | BC03 | release authority ≠ preparer |
| `CMD-CLR-APPROVE` | BC01 | approver ≠ requester ≠ subject (top rank) |
| `CMD-CLR-GRANT` | BC01 | requester ≠ subject |
| `CMD-CLS-ACTIVATE` | BC08 | approver ≠ drafter |
| `CMD-CNF-RESOLVE` | BC02 | reviewer ≠ asserter of preferred claim |
| `CMD-CON-ACTIVATE` | BC07 | Security Officer ≠ requester |
| `CMD-CRQ-APPROVE` | BC02 | approver ≠ requester |
| `CMD-CRR-ACTIVATE` | BC02 | approver ≠ author |
| `CMD-DSP-APPROVE` | BC08 | approver ≠ submitter |
| `CMD-ER-CONFIRM-MATCH` | BC02 | reviewer ≠ split requester |
| `CMD-ER-DECIDE-MATCH` | BC02 | reviewer ≠ human proposer; second reviewer if cluster > 50 |
| `CMD-ER-SPLIT` | BC02 | reviewer ≠ split requester |
| `CMD-ERS-APPROVE` | BC08 | approver ≠ registrar |
| `CMD-EVS-ACTIVATE` | BC07 | approver ≠ author |
| `CMD-EXC-APPROVE` | BC08 | approver ∉ {requester, first approver} |
| `CMD-FND-ACCEPT` | BC03 | reviewer ≠ author |
| `CMD-KNO-PUBLISH` | BC06 | reviewer ≠ author; domain authority for procedures/policy knowledge |
| `CMD-LHD-APPROVE-RELEASE` | BC08 | approver ≠ requester |
| `CMD-MDL-APPROVE` | BC07 | approver ≠ registrar |
| `CMD-MDL-PROMOTE` | BC07 | approver ≠ stager |
| `CMD-MRS-ACTIVATE` | BC02 | approver ≠ author |
| `CMD-OBS-VALIDATE` | BC02 | validator ≠ observer (unless system auto-validation policy) |
| `CMD-PLV-APPROVE` | BC04 | approver ≠ author (REQ-OPS-005); AuthorityCheck plan-approval |
| `CMD-POL-APPROVE` | BC08 | approver ≠ author |
| `CMD-PRD-APPROVE` | BC06 | reviewer ≠ author |
| `CMD-PTM-ACTIVATE` | BC06 | approver ≠ author |
| `CMD-RAS-ASSIGN` | BC01 | assigner ≠ user; SoD role pairs |
| `CMD-RIS-ASSESS` | BC04 | assessor ≠ identifier when tenant policy requires it (INV-RIS-01) |
| `CMD-RIS-REASSESS` | BC04 | assessor ≠ identifier when tenant policy requires it (INV-RIS-01) |
| `CMD-RRQ-ACTIVATE` | BC05 | approver ≠ author |
| `CMD-RTG-ACTIVATE` | BC07 | approver ≠ author |
| `CMD-RTS-ACTIVATE` | BC08 | approver ≠ drafter |
| `CMD-SCN-ACTIVATE` | BC05 | approver ≠ author |
| `CMD-SIM-RECORD-EVALUATION` | BC05 | evaluator ≠ participant |
| `CMD-SRC-SET-PROTECTION` | BC02 | decrease needs second Security Officer |
| `CMD-TASK-APPROVE` | BC04 | reviewer ≠ assignee (PB-06) |
| `CMD-TASK-START-REVIEW` | BC04 | reviewer ≠ assignee |
| `CMD-TEN-START-DECOMMISSION` | BC01 | two distinct platform operators |

قيود سلطة أو تصريح مسجلة في حقل `segregation_of_duties` وليست فصل مهام (10):

| الأمر | القيد |
|---|---|
| `CMD-ALC-PREEMPT` | decision by pool-scope authority |
| `CMD-ARC-TRANSFER` | transfer authority decision |
| `CMD-AST-DISPOSE` | asset-disposal authority |
| `CMD-CRP-ACCEPT` | reviewer cleared for all inputs |
| `CMD-DEC-ANNUL` | authority at higher scope |
| `CMD-DEC-RECORD` | AuthorityCheck (BRL-003) |
| `CMD-RUN-REPRODUCE` | reproducer cleared for source run label |
| `CMD-TASK-ASSIGN` | assignee clearance ≥ task label |
| `CMD-TASK-REASSIGN` | assignee clearance ≥ task label |
| `CMD-TOL-ACTIVATE` | Security Officer |

### 12.5 التزامات أخرى

| الأمر | الالتزامات |
|---|---|
| `CMD-ATT-ERASE` | audit; mfa; legal-hold check |
| `CMD-DST-DISTRIBUTE` | audit; watermark |
| `CMD-EVD-WITHDRAW` | audit; notify owners of dependent claims |
| `CMD-INC-ESCALATE` | audit; notify next authority level |
| `CMD-PER-ERASE` | audit; mfa; legal-hold check |
| `CMD-PRJ-CANCEL-BUILD` | audit; mfa for PROMOTE |
| `CMD-PRJ-CREATE-VERSION` | audit; mfa for PROMOTE |
| `CMD-PRJ-PROMOTE` | audit; mfa for PROMOTE |
| `CMD-PRJ-RETIRE` | audit; mfa for PROMOTE |

### 12.6 سياسات الاستعلامات

`allowed_scope` يُطبَّق قبل العدّ والترتيب؛ «عند الرفض» شكل الاستجابة (ADR-P06).

| الاستعلام | السياق | الموضوع | النطاق المسموح | عند الرفض |
|---|---|---|---|---|
| `QRY-ACS-GET` | BC03 | case label rule; selections filtered | — | DENY (not-found shape) |
| `QRY-ACS-LIST` | BC03 | allowed_scope | — | DENY (not-found shape) |
| `QRY-ADP-GET` | BC07 | Administrator | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-AI-USAGE` | BC07 | Administrator, finance | — | DENY (not-found shape) |
| `QRY-AIR-CONTEXT` | BC07 | requester if cleared; Auditor | — | DENY (not-found shape) |
| `QRY-AIR-GET` | BC07 | requester; Auditor (metadata) | — | DENY (not-found shape) |
| `QRY-AIRS-QUEUE` | BC07 | reviewers authorized on targets | — | DENY (not-found shape) |
| `QRY-ALC-LIST` | BC05 | scope | — | DENY (not-found shape) |
| `QRY-ALR-LIST` | BC03 | recipient; label rule | — | DENY (not-found shape) |
| `QRY-AMT-LIST` | BC03 | any analyst | — | DENY (not-found shape) |
| `QRY-ARC-RETRIEVE` | BC06 | authorized by package label and purpose | — | DENY (not-found shape) |
| `QRY-ARC-SEARCH` | BC06 | Archivist; label rule | — | DENY (not-found shape) |
| `QRY-ASM-GET` | BC03 | label rule; REDACT obligation for uncleared citations | — | DENY (not-found shape) |
| `QRY-ASM-VERSIONS` | BC03 | label rule | — | DENY (not-found shape) |
| `QRY-AST-AVAILABILITY` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-AST-GET` | BC05 | label rule | — | DENY (not-found shape) |
| `QRY-ATT-DOWNLOAD` | BC02 | authorized on the owning evidence/observation | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-AUD-SEARCH` | BC08 | Auditor, Security Officer (itself audited) | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-AUD-VERIFY` | BC08 | Auditor | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-AUT-CHECK` | BC01 | internal services (workload identity) or self | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-AUT-LIST` | BC01 | Executive or Administrator in scope, or holder | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-BASE-TILE` | BC03 | any user of tenant | — | DENY (not-found shape) |
| `QRY-CAP-LIST` | BC03 | release authority, Auditor | — | DENY |
| `QRY-CLM-GET` | BC02 | any user; label-filtered | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-CLR-GET` | BC01 | Security Officer or self | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-CLS-ACTIVE` | BC08 | any user of tenant | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-CLUSTER-GET` | BC02 | Analyst; invisible members omitted | — | DENY (not-found shape) |
| `QRY-CNF-GET` | BC02 | Analyst; visibility rule INV-CNF-04 | — | DENY (not-found shape) |
| `QRY-CNF-LIST` | BC02 | Analyst; only conflicts with ≥ 2 visible member claims | — | DENY (not-found shape) |
| `QRY-CON-LIST` | BC07 | integration engineers, Security Officer | — | DENY |
| `QRY-CPL-GET` | BC02 | planner scope | — | DENY (not-found shape) |
| `QRY-CRD-GET` | BC04 | participants (scope-limited); lead | — | DENY (not-found shape) |
| `QRY-CRD-LIST` | BC04 | allowed_scope | — | DENY (not-found shape) |
| `QRY-CRP-GET` | BC02 | reviewer cleared for all inputs | — | DENY (not-found shape) |
| `QRY-CRP-QUEUE` | BC02 | Analyst | — | DENY (not-found shape) |
| `QRY-CRQ-BOARD` | BC02 | allowed_scope | — | DENY (not-found shape) |
| `QRY-CRQ-EVIDENCE` | BC02 | requester, collection managers | — | DENY (not-found shape) |
| `QRY-CRQ-GET` | BC02 | requester, collection managers; label rule | — | DENY (not-found shape) |
| `QRY-DEC-BASIS` | BC04 | label rule; Auditor | — | DENY (not-found shape) |
| `QRY-DEC-GET` | BC04 | label rule | — | DENY (not-found shape) |
| `QRY-DEV-LIST` | BC01 | self; Administrator in scope | — | DENY |
| `QRY-DRQ-GET` | BC04 | label rule; required-authority holders in scope | — | DENY (not-found shape) |
| `QRY-DRQ-LIST` | BC04 | allowed_scope | — | DENY (not-found shape) |
| `QRY-DSP-GET` | BC08 | Archivist, Legal, Auditor | — | DENY |
| `QRY-DST-LOG` | BC06 | distributor, Security Officer, Auditor | — | DENY (not-found shape) |
| `QRY-ELIG-CHECK` | BC05 | Planner/Manager in scope; internal BC04 (workload identity) | — | DENY (not-found shape) |
| `QRY-ENT-CLAIMS` | BC02 | any user; label-filtered | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-ENT-LIST` | BC02 | any user; allowed_scope pre-filter | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-ENT-POSITIONS` | BC02 | any user; label-filtered; geometry generalized by obligation | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-ENT-RESOLVED` | BC02 | any user; claims label-filtered (INV-ENT-02) | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-ER-GET` | BC02 | Analyst; both entities visible | — | DENY (not-found shape) |
| `QRY-ER-QUEUE` | BC02 | Analyst; cases where both entities are visible | — | DENY (not-found shape) |
| `QRY-ERS-GET` | BC08 | Legal, Auditor | — | DENY |
| `QRY-EVD-GET` | BC02 | any user; label-filtered | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-EXC-LIST` | BC08 | Security Officer, Auditor | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-EXR-GET` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-EXR-LIST` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-EXT-RESOLVE` | BC02 | adapter service accounts; Analyst | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-FND-LIST` | BC03 | label rule | — | DENY (not-found shape) |
| `QRY-GRAPH-NEIGHBORHOOD` | BC07 | any user; per-node and per-edge authorization | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page | DENY (not-found shape) |
| `QRY-GRAPH-PATHS` | BC07 | any user; per-node and per-edge authorization | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page | DENY (not-found shape) |
| `QRY-HRS-QUEUE` | BC01 | Administrator in scope, Security Officer | — | DENY |
| `QRY-IMP-GET` | BC02 | adapter owner; Administrator | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-INC-GET` | BC04 | allowed_scope | — | DENY (not-found shape) |
| `QRY-INC-LIST` | BC04 | allowed_scope | — | DENY (not-found shape) |
| `QRY-INC-RECOVERY-STATUS` | BC04 | القائد؛ مالك الاستمرارية | — | DENY (not-found shape) |
| `QRY-KNO-SEARCH` | BC06 | any user; label rule | — | DENY (not-found shape) |
| `QRY-KNO-SUGGEST` | BC06 | planner; label rule | — | DENY (not-found shape) |
| `QRY-LABEL-CHECK` | كل المالكين | discovery service workload identity only | returns visibility for the subject passed in the request context | DENY |
| `QRY-LGR-GET` | BC05 | allowed_scope; requester | — | DENY (not-found shape) |
| `QRY-LGR-LIST` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-LHD-CHECK` | BC08 | owner contexts (workload identity); Archivist | — | DENY |
| `QRY-LHD-LIST` | BC08 | Legal, Archivist, Auditor | — | DENY |
| `QRY-LIN-TRACE` | BC02 | any user; per-node authorization | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-MDL-LIST` | BC07 | AI governance, Auditor | — | DENY (not-found shape) |
| `QRY-MNT-SCHEDULE` | BC05 | asset owner scope | — | DENY (not-found shape) |
| `QRY-MRS-GET` | BC02 | Analyst lead, Administrator | — | DENY (not-found shape) |
| `QRY-NTF-INBOX` | BC04 | recipient | — | DENY (not-found shape) |
| `QRY-OBS-GET` | BC02 | any user; label-filtered | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-OBS-LIST` | BC02 | any user; allowed_scope pre-filter | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-ORG-TREE` | BC01 | any user of tenant (view org structure) | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-OUT-SERIES` | BC04 | label rule | — | DENY (not-found shape) |
| `QRY-PDP-DECIDE` | BC08 | internal PEPs only (workload identity) | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-PKG-GET` | BC07 | package owner device + user | — | DENY |
| `QRY-PLN-GET` | BC04 | label rule | — | DENY (not-found shape) |
| `QRY-PLN-PROGRESS` | BC04 | label rule; visible tasks only | — | DENY (not-found shape) |
| `QRY-PLV-DIFF` | BC04 | label rule | — | DENY (not-found shape) |
| `QRY-PLV-LIST` | BC04 | label rule | — | DENY (not-found shape) |
| `QRY-POL-GET` | BC08 | Security Officer, Auditor | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-POL-TIMELINE` | BC05 | pool scope | — | DENY (not-found shape) |
| `QRY-PRD-GET` | BC06 | audience + label rule | — | DENY (not-found shape) |
| `QRY-PRD-LIST` | BC06 | allowed_scope | — | DENY (not-found shape) |
| `QRY-PRJ-STATUS` | BC07 | platform operator | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page | DENY (not-found shape) |
| `QRY-QUAL-LIST` | BC05 | Manager/Resource Manager in scope; self | — | DENY (not-found shape) |
| `QRY-READINESS` | BC05 | Manager / Training Manager in scope; self | — | DENY (not-found shape) |
| `QRY-REC-REPORT` | BC06 | requester, Auditor | — | DENY (not-found shape) |
| `QRY-REL-LIST` | BC02 | any user; hidden relationships and endpoints omitted | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-RIS-GET` | BC04 | مالك النطاق؛ مدير المخاطر | — | DENY (not-found shape) |
| `QRY-RIS-REGISTER` | BC04 | allowed_scope | — | DENY (not-found shape) |
| `QRY-RTG-ACTIVE` | BC07 | AI governance, Security Officer | — | DENY (not-found shape) |
| `QRY-RTS-ACTIVE` | BC08 | Archivist, Legal, Auditor | — | DENY |
| `QRY-RUN-ARTIFACT` | BC03 | run label rule; audited | — | DENY (not-found shape) |
| `QRY-RUN-GET` | BC03 | run label rule | — | DENY (not-found shape) |
| `QRY-RWE-GET` | BC02 | any user; label-filtered | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-SCF-GET` | BC07 | reviewer authorized on target | — | DENY |
| `QRY-SCF-LIST` | BC07 | reviewers authorized on targets | — | DENY |
| `QRY-SCN-COMPARE` | BC03 | case label rule | — | DENY (not-found shape) |
| `QRY-SCN-GET` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-SCN-LIST` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-SEC-CONTEXT` | BC01 | self | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-SHP-GET` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-SHP-LIST` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-SHP-TRACKING` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-SIM-GET` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-SIM-LIST` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-SIM-TIMELINE` | BC05 | allowed_scope | — | DENY (not-found shape) |
| `QRY-SIT-CHANGES` | BC03 | cleared for situation; per-member filtering | — | DENY (not-found shape) |
| `QRY-SIT-COP` | BC03 | cleared for situation; per-member filtering | — | DENY (not-found shape) |
| `QRY-SIT-GET` | BC03 | cleared for situation label | — | DENY (not-found shape) |
| `QRY-SIT-LIST` | BC03 | any user; situation label rule | — | DENY (not-found shape) |
| `QRY-SIT-TILE` | BC03 | cleared for situation; scope-keyed cache (ADR-P06 §6) | — | DENY (not-found shape) |
| `QRY-SNS-LIST` | BC07 | integration engineers, Analyst | — | DENY |
| `QRY-SRC-GET` | BC02 | Analyst and above; protection policy | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| `QRY-SRCH-QUERY` | BC07 | any user; allowed_scope pre-filter + authoritative re-check | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page | DENY (not-found shape) |
| `QRY-SRCH-SUGGEST` | BC07 | any user; same filter | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page | DENY (not-found shape) |
| `QRY-SYN-DELTA` | BC07 | device + user of the session | — | DENY |
| `QRY-TASK-GET` | BC04 | assignee, reviewer, Planner/Manager in scope; label rule | — | DENY (not-found shape) |
| `QRY-TASK-HISTORY` | BC04 | same as QRY-TASK-GET | — | DENY (not-found shape) |
| `QRY-TASK-LIST` | BC04 | allowed_scope pre-filter | — | DENY (not-found shape) |
| `QRY-TEN-GET` | BC01 | platform operator or tenant Administrator of that tenant | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-TOL-LIST` | BC07 | AI governance, Security Officer | — | DENY (not-found shape) |
| `QRY-TTY-GET` | BC04 | any user of tenant | — | DENY (not-found shape) |
| `QRY-USR-GET` | BC01 | Administrator in scope or self | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| `QRY-USR-LIST` | BC01 | Administrator in scope | org scope of subject roles ∩ classification rule | DENY (not-found shape) |

### 12.7 البيانات الشخصية والتصنيف

- **Aggregates ببيانات شخصية (4):** `AGG-ERASURE-REQUEST`, `AGG-HR-SYNC-PROPOSAL`, `AGG-PERSON`, `AGG-QUALIFICATION-RECORD` — حقولها الشخصية مشفرة بمفتاح الموضوع (ADR-P08) ومحوها بإتلافه، عدا ما يبقى بمرجع مستعار في طلب المحو نفسه (INV-ERS-03). `key-hierarchy-and-disposition.md` §1 يمد مفتاح الموضوع إلى ادعاءات الكيانات من نوع شخص في BC02، بينما AGG-CLAIM وAGG-ENTITY معلَّمان `personal_data: false` **[Needs Review]** (S-28).
- **مستوى الأهمية** (REQ-GOV-002: كل كائن T1/T2 يحمل تصنيفًا): T1: AI-REQUEST, AI-RESULT, ANALYSIS-RUN, ARCHIVE-PACKAGE, ASSESSMENT, ATTACHMENT, CLAIM, CORRELATION-PROPOSAL, EVIDENCE, EVIDENCE-LINK, FINDING, INCIDENT, KNOWLEDGE-OBJECT, OBSERVATION, PRODUCT, RELATIONSHIP, SOURCE؛ T2: ADAPTER, AI-ROUTING, AI-TOOL, ALERT, ALERT-RULE, ALLOCATION, ANALYSIS-CASE, ANALYSIS-METHOD, ASSET, ASSET-ASSIGNMENT, ASSET-RESERVATION, AUTHORITY-GRANT, CAP-MESSAGE, CLASSIFICATION-SCHEME, CLEARANCE, COLLECTION-PLAN, COLLECTION-REQUIREMENT, CONFLICT, COORDINATION-CASE, CORRELATION-RULE, DECISION, DECISION-REQUEST, DEVICE, DISPOSITION-RUN, DISTRIBUTION, ENTITY, ER-CASE, ERASURE-REQUEST, EVAL-SUITE, EXERCISE, EXTERNAL-ID, HR-SYNC-PROPOSAL, IMPORT-BATCH, INTEGRATION-CONNECTION, LEGAL-HOLD, LOGISTICS-REQUEST, MAINTENANCE-ORDER, MATCH-RULESET, MODEL-VERSION, ORGANIZATION, OUTCOME-TRACKER, PERSON, PLAN, PLAN-VERSION, POLICY-SET, PRELOAD-PACKAGE, PRODUCT-TEMPLATE, QUALIFICATION-RECORD, REALWORLD-EVENT, RECONSTRUCTION, RESOURCE-POOL, RETENTION-SCHEDULE, RISK, ROLE, ROLE-ASSIGNMENT, ROLE-REQUIREMENT, SCENARIO, SECURITY-EXCEPTION, SENSOR-STREAM, SERVICE-ACCOUNT, SHIPMENT, SIMULATION, SITUATION, SYNC-CONFLICT, SYNC-SESSION, TASK, TASK-TYPE, TENANT, USER؛ T3: NOTIFICATION, PROJECTION-VERSION, SUBSCRIPTION

**مصدر التصنيف لكل Aggregate** (`08-security/label-derivation-rules.md`، القاعدة SL-29):

| مصدر التصنيف | العدد | الـAggregates |
|---|---|---|
| **[Missing]** (S-26) | 5 | EXERCISE, LOGISTICS-REQUEST, SCENARIO, SHIPMENT, SIMULATION |
| T3 — غير ملزم بتصنيف | 2 | PROJECTION-VERSION, SUBSCRIPTION |
| administrative | 33 | ADAPTER, AI-ROUTING, AI-TOOL, ANALYSIS-METHOD, AUTHORITY-GRANT, CLASSIFICATION-SCHEME, CLEARANCE, CORRELATION-RULE, DEVICE, DISPOSITION-RUN, ERASURE-REQUEST, EXTERNAL-ID, HR-SYNC-PROPOSAL, IMPORT-BATCH, INTEGRATION-CONNECTION, LEGAL-HOLD, MATCH-RULESET, MODEL-VERSION, ORGANIZATION, PERSON, POLICY-SET, PRODUCT-TEMPLATE, QUALIFICATION-RECORD, RETENTION-SCHEDULE, ROLE, ROLE-ASSIGNMENT, ROLE-REQUIREMENT, SECURITY-EXCEPTION, SERVICE-ACCOUNT, SYNC-SESSION, TASK-TYPE, TENANT, USER |
| explicit | 28 | ALERT-RULE, ANALYSIS-CASE, ANALYSIS-RUN, ASSESSMENT, ASSET, ASSET-RESERVATION, ATTACHMENT, CLAIM, COLLECTION-PLAN, COLLECTION-REQUIREMENT, COORDINATION-CASE, DECISION, DECISION-REQUEST, ENTITY, EVIDENCE, FINDING, INCIDENT, KNOWLEDGE-OBJECT, OBSERVATION, PLAN, PRODUCT, REALWORLD-EVENT, RELATIONSHIP, RESOURCE-POOL, RISK, SITUATION, SOURCE, TASK |
| مشتق (= تصنيف كائن مرتبط) | 21 | AI-REQUEST, AI-RESULT, ALERT, ALLOCATION, ARCHIVE-PACKAGE, ASSET-ASSIGNMENT, CAP-MESSAGE, CONFLICT, CORRELATION-PROPOSAL, DISTRIBUTION, ER-CASE, EVAL-SUITE, EVIDENCE-LINK, MAINTENANCE-ORDER, NOTIFICATION, OUTCOME-TRACKER, PLAN-VERSION, PRELOAD-PACKAGE, RECONSTRUCTION, SENSOR-STREAM, SYNC-CONFLICT |

### 12.8 الأحداث المؤثرة أمنيًا (55)

ترفع إصدار الأمن للموضوع وتبطل ذاكرة القرارات (`15-event-design.md` §7): `EVT-ACS-RECLASSIFIED`, `EVT-AST-RECLASSIFIED`, `EVT-ATT-ERASED`, `EVT-AUT-DELEGATED`, `EVT-AUT-EXPIRED`, `EVT-AUT-GRANTED`, `EVT-AUT-RESUMED`, `EVT-AUT-REVOKED`, `EVT-AUT-SUSPENDED`, `EVT-CLM-RECLASSIFIED`, `EVT-CLR-EXPIRED`, `EVT-CLR-GRANTED`, `EVT-CLR-MODIFIED`, `EVT-CLR-REINSTATED`, `EVT-CLR-REVOKED`, `EVT-CLR-SUSPENDED`, `EVT-CLS-ACTIVATED`, `EVT-CON-ACTIVATED`, `EVT-CON-SUSPENDED`, `EVT-DEV-REPORTED-LOST`, `EVT-DEV-SUSPENDED`, `EVT-ENT-RECLASSIFIED`, `EVT-EVD-RECLASSIFIED`, `EVT-EXC-ACTIVATED`, `EVT-EXC-EXPIRED`, `EVT-EXC-REVOKED`, `EVT-HRS-APPROVED`, `EVT-OBS-RECLASSIFIED`, `EVT-ORG-UNIT-DEACTIVATED`, `EVT-ORG-UNIT-MOVED`, `EVT-PLN-RECLASSIFIED`, `EVT-POL-ACTIVATED`, `EVT-RAS-ASSIGNED`, `EVT-RAS-EXPIRED`, `EVT-RAS-REVOKED`, `EVT-REL-RECLASSIFIED`, `EVT-ROL-PERMISSIONS-CHANGED`, `EVT-RTG-ACTIVATED`, `EVT-RWE-RECLASSIFIED`, `EVT-SEC-VERSION-INCREMENTED`, `EVT-SIT-RECLASSIFIED`, `EVT-SRC-PROTECTION-CHANGED`, `EVT-SRC-RECLASSIFIED`, `EVT-TASK-RECLASSIFIED`, `EVT-TEN-REACTIVATED`, `EVT-TEN-SUSPENDED`, `EVT-TOL-ACTIVATED`, `EVT-TOL-DISABLED`, `EVT-USR-ACTIVATED`, `EVT-USR-CLOSED`, `EVT-USR-DISABLED`, `EVT-USR-ENABLED`, `EVT-USR-IDENTITY-UNLINKED`, `EVT-USR-LOCKED`, `EVT-USR-UNLOCKED`

### 12.9 نموذج التهديدات الموحَّد (134 تهديدًا)

من `08-security/threat-model.md` (النواة، حسب حدود الثقة) و`threat-model-slcNN.md` (لكل شريحة، حسب المكوّن)، بتصنيف STRIDE.

| STRIDE | العدد |
|---|---|
| Info Disclosure | 49 |
| Tampering | 39 |
| Elevation | 23 |
| Repudiation | 12 |
| Spoofing | 5 |
| DoS | 5 |
| Spoofing/Elevation | 1 |

**مخاطر متبقية فوق المنخفض (14):**

| التهديد | المصدر | الحد / المكوّن | STRIDE | التهديد | الضوابط | المتبقي |
|---|---|---|---|---|---|---|
| THR-S01-04 | threat-model-slc01 | Clearance | Elevation | Security Officer grants own or colluding clearance | INV-CLR-02/03 two distinct officers for top rank; MFA; audit review | M |
| THR-S01-11 | threat-model-slc01 | Service account | Spoofing | Leaked long-lived credential | ≤ 90 days; public-key credentials; owner accountability; rotation | M |
| THR-S02-01 | threat-model-slc02 | Adapter / import | Tampering | poisoned external data asserted as facts | claims cite adapter source with reliability; quarantine; no automatic truth (BRL-013); anomaly review | M |
| THR-S02-04 | threat-model-slc02 | Attachments | Tampering | malicious file (malware, polyglot, parser exploit) | offline scanner + format validation; QUARANTINED state; rendering in sandboxed viewer | M |
| THR-S02-07 | threat-model-slc02 | Observation | Spoofing | fabricated observation with forged device time | server record time; clock-skew flag; source reliability; validation SoD | M |
| THR-S05-08 | threat-model-slc05 | Timing | Info Disclosure | response time correlates with hidden matches | pre-filter; re-check only on returned page; residual accepted | M |
| THR-S10-04 | threat-model-slc10 | Output | Tampering | hallucinated statements presented as facts | grounding verifier; insufficient-evidence path; citations; human review for effects | M |
| THR-S11-05 | threat-model-slc11 | Clock | Tampering | device clock manipulated to backdate observations | server record time; offset measured; skew flag | M |
| THR-S12-P2 | threat-model-slc12 | Distribution | Info Disclosure | leaked copy cannot be traced | per-recipient visible + invisible watermark | M |
| THR-S16-05 | threat-model-slc16 | Sensors | Tampering | spoofed sensor readings | gateway authentication; source reliability; quality rules; corroboration (SLC-15) | M |
| THR-009 | threat-model | TB-06 | Tampering | بيانات خارجية مسممة أو مزيفة | ACL، حجر، مصدر وموثوقية، لا ثقة تلقائية | M |
| THR-013 | threat-model | TB-08 | Info Disclosure | حقن أوامر غير مباشر عبر وثيقة يدفع AI لتسريب سياق | AI بصلاحيات الطالب فقط؛ AIL≤2؛ لا أدوات كتابة؛ R2 تفصيل | M |
| THR-017 | threat-model | PDP | DoS | تعطل PDP يوقف المنصة | PDP في critical tier، نسخ متعددة، ذاكرة قرارات قصيرة؛ fail-closed مقبول كخطر متبقٍ | M |
| THR-019 | threat-model | supply chain | Tampering | مكتبة أو صورة حاوية ملوثة | SBOM، توقيع الصور، مرآة داخلية للحزم (بيئة معزولة) | M |

**تهديدات الخصوصية (LINDDUN، 7):**

| التهديد | الفئة | التهديد | الضابط |
|---|---|---|---|
| PRV-01 | Linkability | ربط سجلات شخص عبر مصادر يكشف أكثر مما أذن به الغرض | تقييد الغرض في السياسة؛ REDACT؛ مراجعة مطابقة الكيانات للأشخاص |
| PRV-02 | Identifiability | إعادة تعريف من إحصاءات صغيرة | AGGREGATE بحد أدنى 5 |
| PRV-03 | Non-repudiation (as privacy threat) | تتبع مفرط لنشاط المستخدمين | تدقيق القراءة فقط فوق العتبة؛ وصول مقيد لسجلات التدقيق |
| PRV-04 | Detectability | معرفة أن شخصاً ما في النظام | نفس شكل not-found/forbidden؛ لا اقتراحات بحث خارج النطاق |
| PRV-05 | Disclosure | بيانات شخصية في السجلات التقنية | إخفاء آلي؛ URN فقط |
| PRV-06 | Unawareness | أصحاب البيانات لا يعرفون المعالجة | خارج نطاق التقنية: سياسة المستأجر (UNK-002) |
| PRV-07 | Non-compliance | احتفاظ أطول من المسموح | جداول احتفاظ + crypto-shredding (ADR-P08) |

#### الكتالوج الكامل

| التهديد | المصدر | الحد / المكوّن | STRIDE | التهديد | الاحتمال | الأثر | الضوابط | المتبقي |
|---|---|---|---|---|---|---|---|---|
| THR-S01-01 | threat-model-slc01 | SCIM endpoint | Spoofing/Elevation | SCIM client provisions users with admin roles | M | H | SCIM service account can only create PENDING users and link identities; roles never via SCIM (only via CMD-RAS-ASSIGN) | L |
| THR-S01-02 | threat-model-slc01 | Role assignment | Elevation | Administrator assigns self a higher role or out-of-scope role | M | H | INV-RAS-01 (no self, scope-bound); PB-05; audit | L |
| THR-S01-03 | threat-model-slc01 | Delegation | Elevation | Delegation chain amplifies authority | L | H | INV-AUT-01/02; effective check evaluates chain at time t | L |
| THR-S01-04 | threat-model-slc01 | Clearance | Elevation | Security Officer grants own or colluding clearance | L | H | INV-CLR-02/03 two distinct officers for top rank; MFA; audit review | M |
| THR-S01-05 | threat-model-slc01 | Policy set | Tampering | Tenant weakens platform baseline via policy | M | H | INV-POL-02 restrict-only; PB-* non-overridable; policy tests | L |
| THR-S01-06 | threat-model-slc01 | Security exception | Elevation | Long-lived or chained exceptions | M | M | 30-day max; two approvers; baseline exempt; exception report to Auditor | L |
| THR-S01-07 | threat-model-slc01 | SecurityContext | Spoofing | Forged or replayed internal context | L | H | JWS, ≤ 60 s, mTLS, security_version check | L |
| THR-S01-08 | threat-model-slc01 | Tenant provisioning | Tampering | Namespace squatting / takeover | L | M | platform operator only; namespace immutable; two-person decommission | L |
| THR-S01-09 | threat-model-slc01 | Audit outbox | Repudiation | Application deletes audit before shipping | L | H | insert-only grants; shipping counters reconciliation; ≤ 5 s window | L |
| THR-S01-10 | threat-model-slc01 | Revocation | Info Disclosure | Disabled user keeps access via cached decisions | M | H | security_version checked per request (PL-SECURITY-CONTEXT §2) | L |
| THR-S01-11 | threat-model-slc01 | Service account | Spoofing | Leaked long-lived credential | M | H | ≤ 90 days; public-key credentials; owner accountability; rotation | M |
| THR-S01-12 | threat-model-slc01 | Org tree | Tampering | Moving a unit to widen an admin's scope | M | M | MoveUnit increments security_version of affected subjects; requires Administrator of both old and new parent scopes | L |
| THR-S02-01 | threat-model-slc02 | Adapter / import | Tampering | poisoned external data asserted as facts | M | H | claims cite adapter source with reliability; quarantine; no automatic truth (BRL-013); anomaly review | M |
| THR-S02-02 | threat-model-slc02 | Source | Info Disclosure | identity of protected human source revealed via claims, lineage, exports or search | M | H | PB-08; source label ≥ default+1; lineage cut (PB-11); QAS-SEC-009 | L |
| THR-S02-03 | threat-model-slc02 | Claims | Info Disclosure | hidden claims inferred from DISPUTED status, counts or completeness | M | H | LIB §3 visibility-first filtering; QAS-SEC-010 | L |
| THR-S02-04 | threat-model-slc02 | Attachments | Tampering | malicious file (malware, polyglot, parser exploit) | M | H | offline scanner + format validation; QUARANTINED state; rendering in sandboxed viewer | M |
| THR-S02-05 | threat-model-slc02 | Attachments | Info Disclosure | signed download URL shared or replayed | M | M | ≤ 5 min lifetime; bound to subject + tenant; each grant audited | L |
| THR-S02-06 | threat-model-slc02 | Evidence | Tampering | evidence altered after sealing | L | H | content hash + seal hash; custody chain; verification on retrieval (REQ-INF-004) | L |
| THR-S02-07 | threat-model-slc02 | Observation | Spoofing | fabricated observation with forged device time | M | M | server record time; clock-skew flag; source reliability; validation SoD | M |
| THR-S02-08 | threat-model-slc02 | Location | Info Disclosure | precise positions exposed to lower clearance | M | H | generalize obligation (PB-10) | L |
| THR-S02-09 | threat-model-slc02 | External-id resolve | Info Disclosure | probing external ids to learn existence | M | M | not-found shape; rate limit per subject; audit | L |
| THR-S02-10 | threat-model-slc02 | Import | DoS | oversized or pathological batch | M | M | size limits; streaming parser; per-tenant job quotas | L |
| THR-S03-01 | threat-model-slc03 | Approval | Elevation | assignee approves own work | M | H | PB-06 / INV-TASK-07; audit | L |
| THR-S03-02 | threat-model-slc03 | Criteria | Tampering | criteria weakened after assignment | M | M | INV-TASK-09 frozen from ASSIGNED | L |
| THR-S03-03 | threat-model-slc03 | Assignment | Info Disclosure | task assigned to a user not cleared for its label | M | H | assign guard: clearance ≥ label; reclassify guard | L |
| THR-S03-04 | threat-model-slc03 | Eligibility | Elevation | assignment bypasses eligibility when BC05 is down | M | M | fail-closed ELIGIBILITY_UNAVAILABLE | L |
| THR-S03-05 | threat-model-slc03 | Offline replay | Tampering | forged or replayed offline commands | M | M | base_version + client_command_id + device signature (SLC-11) | L |
| THR-S03-06 | threat-model-slc03 | Task list | Info Disclosure | list counts reveal hidden tasks | M | M | allowed_scope pre-filter (ADR-P06) | L |
| THR-S04-01 | threat-model-slc04 | ER decision | Tampering | deliberate false merge to bury or blend information | L | H | human decision + SoD; reversible split; decision_basis_level; audit; cluster size gate | L |
| THR-S04-02 | threat-model-slc04 | ER queue | Info Disclosure | cases reveal existence of hidden entities | M | H | case visible only if both entities visible; comparison shows visible claims only | L |
| THR-S04-03 | threat-model-slc04 | Conflict | Info Disclosure | conflict existence reveals a hidden claim | M | H | INV-CNF-04: visible only with ≥ 2 visible incompatible members | L |
| THR-S04-04 | threat-model-slc04 | Cluster | Info Disclosure | identity-cluster endpoint lists hidden members | M | H | invisible members omitted; counts over visible members | L |
| THR-S04-05 | threat-model-slc04 | Ruleset | Tampering | weakened ruleset floods queue or hides duplicates | L | M | activation needs evaluation ≥ targets + approver ≠ author | L |
| THR-S04-06 | threat-model-slc04 | Resolution | Repudiation | analyst denies having resolved a conflict | L | M | bitemporal resolution record with decided_by; audit | L |
| THR-S04-07 | threat-model-slc04 | AI proposals (R2) | Tampering | prompt-injected document induces false match proposals | M | M | AI proposes only (AIL1); human decision; proposer recorded | L |
| THR-S05-01 | threat-model-slc05 | Search facts | Info Disclosure | finding a visible entity by the value of a hidden claim | H | H | fact-level filtering (SPEC-DISCOVERY §3.1) | L |
| THR-S05-02 | threat-model-slc05 | Counts/facets | Info Disclosure | inferring hidden objects from totals or facet buckets | H | H | computed on pre-filtered set only | L |
| THR-S05-03 | threat-model-slc05 | Ranking | Info Disclosure | hidden facts boosting rank reveal them | M | M | scoring on visible facts only | L |
| THR-S05-04 | threat-model-slc05 | Graph paths | Info Disclosure | path existence through hidden node reveals connection | M | H | traversal on visible graph only | L |
| THR-S05-05 | threat-model-slc05 | Stale index | Info Disclosure | revoked access still served from lagging index | H | H | LabelCheck re-check + subject security_version (CR-47) | L |
| THR-S05-06 | threat-model-slc05 | Cursor | Tampering | cursor reused by another user or scope | M | M | cursor bound to scope fingerprint | L |
| THR-S05-07 | threat-model-slc05 | Discovery service | Elevation | projection bypass: direct index access | L | H | index reachable only from discovery workload identity (TB-04) | L |
| THR-S05-08 | threat-model-slc05 | Timing | Info Disclosure | response time correlates with hidden matches | L | M | pre-filter; re-check only on returned page; residual accepted | M |
| THR-S06-01 | threat-model-slc06 | Alert fan-out | Info Disclosure | uncleared subscriber learns that something happened | M | H | INV-ALR-02: no delivery at all to uncleared recipients | L |
| THR-S06-02 | threat-model-slc06 | Push payload | Info Disclosure | lock-screen shows sensitive content | H | H | reference + safe template only (INV-NTF-02) | L |
| THR-S06-03 | threat-model-slc06 | Tiles | Info Disclosure | cached tile served across scopes | M | H | scope-hash cache keys; private cache headers | L |
| THR-S06-04 | threat-model-slc06 | COP counts | Info Disclosure | member counts include hidden members | M | H | counts over visible members only | L |
| THR-S06-05 | threat-model-slc06 | Alert rules | Tampering | rule silently changed to suppress alerts | L | H | ACTIVE rules immutable; disable/edit/enable audited; dry-run | L |
| THR-S06-06 | threat-model-slc06 | Alert storm | DoS | flood of alerts hides critical ones | M | M | dedupe; severity priority queue; per-rule rate limit | L |
| THR-S06-07 | threat-model-slc06 | Subscription | Elevation | subscription used to receive data after revocation | M | H | delivery re-check; auto-end on visibility loss | L |
| THR-S07-01 | threat-model-slc07 | Run execution | Elevation | run reads data beyond submitter's clearance using worker privileges | M | H | runs execute with delegated SecurityContext of submitter; PEP on every read | L |
| THR-S07-02 | threat-model-slc07 | Method image | Tampering | malicious or altered analysis image | L | H | digest-pinned images from internal registry; activation SoD; signature verification | L |
| THR-S07-03 | threat-model-slc07 | Reproduction | Info Disclosure | reproduction report reveals inputs hidden from reproducer | M | M | reproducer must be cleared for source run label | L |
| THR-S07-04 | threat-model-slc07 | Assessment | Tampering | published assessment silently edited | L | H | immutability; new versions only; decisions pin versions | L |
| THR-S07-05 | threat-model-slc07 | Citations | Info Disclosure | citation list reveals existence of compartmented evidence | M | M | withhold citations for uncleared readers; no markers by default | L |
| THR-S07-06 | threat-model-slc07 | Compute | DoS | one tenant exhausts compute | M | M | per-tenant quotas; fair scheduling; timeouts | L |
| THR-S08-01 | threat-model-slc08 | Decision | Elevation | decision recorded without competent authority | M | H | AuthorityCheck at record time, fail-closed; snapshot stored | L |
| THR-S08-02 | threat-model-slc08 | Decision | Repudiation | decider denies the basis | L | H | pinned citations; basis query; MFA; audit | L |
| THR-S08-03 | threat-model-slc08 | Plan version | Tampering | baseline changed after approval | L | H | immutability; minor amendments as annotations only | L |
| THR-S08-04 | threat-model-slc08 | Plan approval | Elevation | author approves own plan | M | H | SoD + authority check | L |
| THR-S08-05 | threat-model-slc08 | Decision request | Info Disclosure | citations above request label exposed | M | M | CITATION_ABOVE_LABEL guard; withheld per reader | L |
| THR-S08-06 | threat-model-slc08 | Task sync | Tampering | sync creates tasks outside plan scope | L | M | sync identity limited to plan's org scope; activities' scopes ⊆ plan scope | L |
| THR-S09-01 | threat-model-slc09 | Allocation | Elevation | self-approval or pre-emption without authority | M | H | SoD; decision-backed pre-emption | L |
| THR-S09-02 | threat-model-slc09 | Asset custody | Repudiation | holder denies receiving an asset | L | M | gapless custody chain with actor and time; condition reports | L |
| THR-S09-03 | threat-model-slc09 | Availability | Info Disclosure | availability reveals hidden tasks holding assets | M | M | blocking reasons shown only if the blocking object is visible; otherwise 'unavailable' | L |
| THR-S09-04 | threat-model-slc09 | Capacity ledger | Tampering | direct ledger edits bypass commitments | L | H | ledger writable only by allocation handlers (DB role); reconciliation job | L |
| THR-S10-01 | threat-model-slc10 | Context retrieval | Info Disclosure | model sees data the user may not | M | H | retrieval as user; pre-filter + LabelCheck; PB-12 | L |
| THR-S10-02 | threat-model-slc10 | Retrieved content | Elevation | indirect prompt injection triggers tools or widens scope | H | H | content as data; operation tool allow-list; argument validation; no write tools (INV-TOL-01) | L |
| THR-S10-03 | threat-model-slc10 | Output | Info Disclosure | exfiltration via links or external calls | M | H | no network egress from runtime; link stripping; PB-13 | L |
| THR-S10-04 | threat-model-slc10 | Output | Tampering | hallucinated statements presented as facts | H | H | grounding verifier; insufficient-evidence path; citations; human review for effects | M |
| THR-S10-05 | threat-model-slc10 | Model supply chain | Tampering | poisoned or altered weights | L | H | digest-pinned weights from internal registry; licence and evaluation gates | L |
| THR-S10-06 | threat-model-slc10 | Tenancy | Info Disclosure | cross-tenant leakage via caches or fine-tuning | L | H | no cross-user caches; no training on tenant data in R2 | L |
| THR-S11-01 | threat-model-slc11 | Device | Info Disclosure | stolen device reveals preloaded data | M | H | local encryption; unlock required; package expiry; wipe on contact; level cap | L |
| THR-S11-02 | threat-model-slc11 | Sync | Spoofing | forged commands injected as a device | L | H | per-command device signatures + hash chain; device key revocation | L |
| THR-S11-03 | threat-model-slc11 | Sync | Repudiation | field user denies an offline action | L | M | signed envelopes stored with conflicts and audit | L |
| THR-S11-04 | threat-model-slc11 | Lost device | Tampering | commands created after theft are applied | M | H | INV-SCF-03: post-lost commands always go to review | L |
| THR-S11-05 | threat-model-slc11 | Clock | Tampering | device clock manipulated to backdate observations | M | M | server record time; offset measured; skew flag | M |
| THR-S11-06 | threat-model-slc11 | Preload | Elevation | package built above the user's current authorization | L | H | build-time filtering; revocation on security_version change | L |
| THR-S12-P1 | threat-model-slc12 | Product | Info Disclosure | product includes content above its label or reveals exclusions | M | H | label filter on every binding; no exclusion counts (QAS-PRD-002) | L |
| THR-S12-P2 | threat-model-slc12 | Distribution | Info Disclosure | leaked copy cannot be traced | M | H | per-recipient visible + invisible watermark | M |
| THR-S12-P3 | threat-model-slc12 | Template | Tampering | template binding reads data outside the author's authority | L | H | bindings only to declared queries executed as the author | L |
| THR-S12-P4 | threat-model-slc12 | Archive | Tampering | silent corruption or alteration of archived records | L | H | fixity at ingest/retrieval/yearly; WORM; replica repair | L |
| THR-S12-P5 | threat-model-slc12 | Reconstruction | Info Disclosure | reconstruction reveals hidden elements | M | H | runs with requester authority; hidden elements absent | L |
| THR-S12-01 | threat-model-slc12a | Disposition | Tampering | premature destruction of evidence to hide it | L | H | two-person approval; HoldCheck twice; certificate; audit | L |
| THR-S12-02 | threat-model-slc12a | Legal hold | Elevation | hold released by one person | L | H | two Legal authorities (INV-LHD-04) | L |
| THR-S12-03 | threat-model-slc12a | Key store backup | Info Disclosure | old backup revives destroyed data | M | H | restore gate + key-store backup retention ≤ 35 d (CR-51) | L |
| THR-S12-04 | threat-model-slc12a | Erasure | Repudiation | erasure claimed but plaintext copies remain | M | M | per-context confirmation ≤ 24 h; projection rebuild; verification sample | L |
| THR-S12-05 | threat-model-slc12a | Schedule | Tampering | retention silently shortened | L | H | immutable versions; Legal approval; retroactivity explicit | L |
| THR-S14-01 | threat-model-slc14 | Fulfilment | Info Disclosure | fulfilment status reveals classified collection answering a lower-labelled requirement | M | H | viewer-scoped fulfilment (INV-CRQ-01); expiry by date only | L |
| THR-S14-02 | threat-model-slc14 | Requirement | Info Disclosure | requirement text itself reveals an intelligence interest | M | M | requirement label set by requester; tasks inherit ≥ label; field users see task-level text only | L |
| THR-S15-01 | threat-model-slc15 | Coordination | Info Disclosure | participant sees another organization's sensitive parts | M | H | per-participant access scope + label rule (INV-CRD-02) | L |
| THR-S15-02 | threat-model-slc15 | Coordination | Elevation | action executed without the owning organization's authority | M | H | INV-CRD-03 decision-gated responsibilities | L |
| THR-S15-03 | threat-model-slc15 | Fusion | Tampering | one source counted twice to fake corroboration | M | M | independence via lineage (INV-CRP-04) | L |
| THR-S15-04 | threat-model-slc15 | Correlation queue | Info Disclosure | proposal reveals hidden inputs | M | H | proposal visible only to reviewers cleared for all inputs | L |
| THR-S16-01 | threat-model-slc16 | Outbound | Info Disclosure | classified content leaves via an integration | M | H | only CAP outbound in R2; release level cap; template-only content; two-person release | L |
| THR-S16-02 | threat-model-slc16 | HRIS | Elevation | forged HR change grants access | M | H | proposals only, admin approval, owner guards (INV-HRS-01) | L |
| THR-S16-03 | threat-model-slc16 | DMS | Info Disclosure | unmapped DMS classification ingested too low | M | H | unmapped → highest default level until review | L |
| THR-S16-04 | threat-model-slc16 | Connections | Tampering | new egress path opened silently | L | H | allow-list entry per connection approved by a second person; monitoring (GOV-005) | L |
| THR-S16-05 | threat-model-slc16 | Sensors | Tampering | spoofed sensor readings | M | M | gateway authentication; source reliability; quality rules; corroboration (SLC-15) | M |
| THR-S17-01 | threat-model-slc17 | Incident severity | Tampering | severity silently lowered to hide a crisis from oversight | L | H | severity only decreases via a distinct, separately-authorized CMD-INC-DE-ESCALATE (INV-INC-01) | L |
| THR-S17-02 | threat-model-slc17 | Contingency activation | Elevation | a plan activated automatically as a side effect of escalation, bypassing authorization | M | H | activation is always an explicit command (INV-INC-03); mirrors the SLC-09 Silent Pre-emption lesson | L |
| THR-S17-03 | threat-model-slc17 | Risk register | Repudiation | a risk closed without rationale, later disputed as never having been treated | M | M | CLOSED requires an explicit rationale; no reopen command (INV-RIS-04) | L |
| THR-S17-04 | threat-model-slc17 | Risk / Incident linkage | Info Disclosure | linking an incident to a risk leaks the risk's scope to an actor not cleared for it | M | H | linkage does not change either aggregate's label; each still enforces its own label independently (INV-RIS-05, INV-INC-04) | L |
| THR-S17-05 | threat-model-slc17 | Response tasks | Elevation | a task created with incident_ref bypasses the review/segregation-of-duties checks that plan-linked tasks get | L | M | CMD-TASK-CREATE's guards (assignee eligibility, SoD on approval) apply identically regardless of plan_ref/incident_ref/ad_hoc_reason (CR-61 changes only the creation link, not downstream guards) | L |
| THR-S18-01 | threat-model-slc18 | Logistics Request ↔ Allocation linkage (CR-62) | Tampering | a logistics request forced into APPROVED directly, bypassing the linked allocation's own commitment check | L | H | no human command sets APPROVED; only SYS: transitions driven by SLC-09's own EVT-ALC-COMMITTED (INV-LGR-01); commitment still runs the unchanged SPEC-ALLOCATION §1 checks and capacity-ledger constraint | L |
| THR-S18-02 | threat-model-slc18 | Delivery quantity | Repudiation | a shipment marked delivered in full when the quantity actually received was short, hiding a loss | M | M | delivered_quantity is a required, explicit field on CMD-SHP-DELIVER; INV-SHP-02/INV-LGR-03 force PARTIALLY_FULFILLED whenever less than requested arrives — no state hides a shortfall | L |
| THR-S18-03 | threat-model-slc18 | Dispatch vs. capacity ledger | Elevation | a shipment dispatched for a quantity never actually reserved, bypassing SLC-09's contention and pre-emption rules | M | H | INV-SHP-03 requires the linked allocation still COMMITTED for at least the shipped quantity at departure; CMD-SHP-PLAN's guard checks the same ledger SLC-09 already enforces — no second, weaker capacity check exists | L |
| THR-S18-04 | threat-model-slc18 | Movement checkpoints | Tampering | a checkpoint inserted out of order or edited, obscuring where or when a shipment actually was | L | M | checkpoints are append-only and must be strictly after the previous one (INV-SHP-01), mirroring AGG-ASSET's gapless custody chain; no edit or delete command exists | L |
| THR-S18-05 | threat-model-slc18 | Cancellation mid-transit | Repudiation | a shipment cancelled while IN_TRANSIT to make an in-flight loss disappear without a DAMAGED/LOST record | L | M | CMD-SHP-CANCEL is only accepted from PLANNED (INV-SHP-04); once IN_TRANSIT the only terminal outcomes are DELIVERED, DAMAGED or LOST, each with its own guard and event | L |
| THR-S19-01 | threat-model-slc19 | Scenario ↔ Exercise freeze (INV-EXR-01) | Tampering | a scenario edited after an exercise was planned against it retroactively changes what the exercise is understood to have tested | L | M | scenario_ref is frozen on AGG-EXERCISE at CMD-EXR-PLAN time; editing an ACTIVE scenario always creates a new version rather than mutating the version already referenced by planned exercises | L |
| THR-S19-02 | threat-model-slc19 | Exercise ↔ Simulation outcome delegation (mirrors CR-62/SLC-18) | Elevation | an exercise forced into COMPLETED without a simulation ever actually running, hiding that no training occurred | L | H | no human command sets COMPLETED or ABORTED; only SYS: transitions driven by the linked Simulation's own EVT-SIM-COMPLETED/EVT-SIM-ABORTED (INV-EXR-02) — visible in the full state × command matrix (SL-05), which has no human-triggered cell for either terminal state | L |
| THR-S19-03 | threat-model-slc19 | Evaluation recording | Repudiation | a participant records their own evaluation as MET to fabricate a passing result | M | H | evaluator ≠ participant is a hard guard (INV-SIM-03), enforced by the policy decision point before the command is accepted, rejected with SEGREGATION_OF_DUTIES | L |
| THR-S19-04 | threat-model-slc19 | Simulation completion vs. evaluation coverage | Repudiation | a simulation marked COMPLETED while some participants were never evaluated, silently certifying attendance without assessment | M | M | INV-SIM-02 requires at least one recorded evaluation per participant before COMPLETED; CMD-SIM-COMPLETE's guard fails with EVALUATION_MISSING otherwise — no state hides an unevaluated participant | L |
| THR-S19-05 | threat-model-slc19 | Inject delivery timeline | Tampering | an inject delivery record inserted out of order or backdated to fabricate a different exercise timeline than what actually happened | L | M | inject deliveries are append-only and strictly increasing in time (INV-SIM-01), mirroring AGG-SHIPMENT's checkpoint pattern; no edit or delete command exists | L |
| THR-001 | threat-model | TB-01 | Spoofing | سرقة رمز جلسة | M | H | رموز قصيرة العمر، ربط بالجهاز، MFA لعمليات حساسة | L |
| THR-002 | threat-model | TB-01 | Tampering | تعديل الطلب لتغيير tenant أو urn | M | H | الخادم يشتق tenant من الرمز لا من الطلب؛ تحقق مخطط | L |
| THR-003 | threat-model | TB-02 | Elevation | خدمة داخلية تنتحل صلاحيات أعلى | L | H | mTLS + هوية عبء العمل؛ SecurityContext موقّع | L |
| THR-004 | threat-model | TB-03 | Info Disclosure | استعلام ينسى فلتر المستأجر | M | H | RLS حاجز ثان؛ FIT-02؛ اختبار عزل | L |
| THR-005 | threat-model | TB-04 | Info Disclosure | استدلال على الوجود عبر العدد/الـ Facets/التوقيت | H | H | ADR-P06 pre-filter؛ QAS-SEC-002 | L |
| THR-006 | threat-model | TB-04 | Info Disclosure | إسقاط متأخر يعيد كائناً بعد سحب الصلاحية | H | H | إعادة فحص security_version (ADR-P06 §3) | L |
| THR-007 | threat-model | TB-04 | Info Disclosure | بلاطة خريطة مخزنة تُقدم لمستخدم بصلاحية أقل | M | H | مفتاح cache بنطاق الصلاحية (ADR-P12) | L |
| THR-008 | threat-model | TB-05 | Info Disclosure | تسرب بين الخلايا | L | H | لا مسارات بيانات بين الخلايا | L |
| THR-009 | threat-model | TB-06 | Tampering | بيانات خارجية مسممة أو مزيفة | M | M | ACL، حجر، مصدر وموثوقية، لا ثقة تلقائية | M |
| THR-010 | threat-model | TB-06 | DoS | فيضان بيانات من محول | M | M | حصص، backpressure (QAS-SCAL-002) | L |
| THR-011 | threat-model | TB-07 | Info Disclosure | سرقة جهاز ميداني | M | H | تشفير، انتهاء صلاحية، مسح عن بعد، منع preload فوق INTERNAL | L |
| THR-012 | threat-model | TB-07 | Repudiation | إنكار ملاحظة سُجلت دون اتصال | L | M | توقيع الأوامر بمفتاح الجهاز+المستخدم؛ تدقيق | L |
| THR-013 | threat-model | TB-08 | Info Disclosure | حقن أوامر غير مباشر عبر وثيقة يدفع AI لتسريب سياق | M | H | AI بصلاحيات الطالب فقط؛ AIL≤2؛ لا أدوات كتابة؛ R2 تفصيل | M |
| THR-014 | threat-model | TB-09 | Elevation | مشغل منصة يقرأ بيانات مستأجر | L | H | فصل المفاتيح؛ break-glass بشخصين وتدقيق | L |
| THR-015 | threat-model | TB-10 | Info Disclosure | نسخة احتياطية مسروقة | L | H | تشفير بمفاتيح المستأجر | L |
| THR-016 | threat-model | audit | Tampering | تعديل سجل التدقيق | L | H | سلسلة hash + anchor (QAS-SEC-006) | L |
| THR-017 | threat-model | PDP | DoS | تعطل PDP يوقف المنصة | M | H | PDP في critical tier، نسخ متعددة، ذاكرة قرارات قصيرة؛ fail-closed مقبول كخطر متبقٍ | M |
| THR-018 | threat-model | ER | Tampering | دمج كيانات خاطئ متعمد لإخفاء معلومة | L | M | الدمج قرار مدقق وقابل للعكس؛ حد العنقود | L |
| THR-019 | threat-model | supply chain | Tampering | مكتبة أو صورة حاوية ملوثة | M | H | SBOM، توقيع الصور، مرآة داخلية للحزم (بيئة معزولة) | M |
| THR-020 | threat-model | TB-01 | Info Disclosure | رسالة خطأ تكشف وجود كائن | M | M | نفس شكل not-found/forbidden (ADR-P06 §5) | L |

<!-- END GENERATED: build_analysis_design.py -->
