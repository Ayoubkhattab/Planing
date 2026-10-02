---
id: AD-05-INDEX
type: feature-index
title: "فهرس الميزات والقصص — خريطة الميزات"
status: DRAFT
version: "0.1"
phase: "Phase 3.8 — إعادة هيكلة الميزات والقصص (المرحلة 2)"
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv, 01-business/capabilities.md, 02-requirements/requirements.md, 02-requirements/use-cases.md, 18-analysis-design/21-ui-design.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# فهرس الميزات والقصص

| البند | القيمة |
|---|---|
| المعرّف | AD-05-INDEX |
| الإصدار | 0.1 |
| الحالة | مسودة: خريطة الميزات تنتظر موافقة المالك قبل كتابة أي قصة |
| المصدر | `features.csv` و`feature_map.csv` في `17-system-study/_build/` |

## الغرض

هذه خريطة الميزات: كل ميزة هدف يعرفه المستخدم، وتحتها القصص التي تخدمه. وقد بُنيت من القدرات الفرعية الأربع والخمسين، وحالات الاستخدام، والشاشات. ووُزعت عليها القصص الحالية الـ739 كلها، كل قصة في ميزة واحدة.

**كيف تُقرأ:**
- **القسم 1** يعطي الأرقام لكل قدرة.
- **القسم 2** يسرد ميزات كل قدرة: اسمها، وقيمتها للمستخدم، وأدوارها، وعدد قصصها. وتحت كل جدول قائمة مطوية بقصص ميزات القدرة.
- **القسم 3** يسرد الميزات التي لا تقابلها اليوم أي قصة، لأن متطلباتها لم تُكتب لها قصص بعد.

**ما المطلوب من المالك:** مراجعة أسماء الميزات وحدودها. فتعديل الخريطة الآن أرخص بكثير من تعديلها بعد كتابة القصص. ونقل قصة من ميزة إلى أخرى يتم بتعديل سطرها في `feature_map.csv` ثم إعادة التوليد.

القواعد التي بُنيت عليها الخريطة في `00-standard.md` §2 و§3. والقرارات التي تحتاج تأكيدًا في `00-open-questions.md`.

<!-- BEGIN GENERATED: build_analysis_design.py -->

## 1. الأرقام

| القدرة | الميزات | القصص الحالية | قصص جديدة متوقعة | المجلد |
|---|---|---|---|---|
| CAP-01 إدارة المؤسسة والوصول | 13 | 72 | 55 | `CAP-01-org-access` |
| CAP-02 جمع المعلومات | 22 | 116 | 100 | `CAP-02-collection` |
| CAP-03 إدارة المعلومات | 16 | 76 | 75 | `CAP-03-information` |
| CAP-04 التحليل والتقييم | 11 | 57 | 40 | `CAP-04-analysis` |
| CAP-05 الوعي بالموقف | 5 | 27 | 23 | `CAP-05-situation` |
| CAP-06 إدارة القرار | 5 | 26 | 19 | `CAP-06-decision` |
| CAP-07 التخطيط والتنفيذ | 11 | 65 | 43 | `CAP-07-planning-execution` |
| CAP-08 الموارد والجاهزية | 19 | 107 | 56 | `CAP-08-resources` |
| CAP-09 المخاطر والطوارئ | 5 | 22 | 24 | `CAP-09-risk-emergency` |
| CAP-10 الاتصال والمنتجات | 9 | 41 | 33 | `CAP-10-communication` |
| CAP-11 المعرفة والذاكرة المؤسسية | 9 | 50 | 36 | `CAP-11-knowledge` |
| CAP-12 المساعدة بالذكاء الاصطناعي | 11 | 45 | 39 | `CAP-12-ai` |
| CAP-13 الحوكمة والأمن والامتثال | 7 | 32 | 32 | `CAP-13-governance-security` |
| CAP-14 تشغيل المنصة | 8 | 3 | 40 | `CAP-14-platform-ops` |
| **المجموع** | **151** | **739** | **615** | |

القصص الجديدة المتوقعة تقدير أولي لكل ميزة حسب الطبقة: واجهة 265، منصة 136، تكامل 55، تشغيل وأمن 159. ولا يشمل قصص التقسيم. يُراجع التقدير في المرحلة 3.

## 2. الميزات حسب القدرة

### 2.1 CAP-01 — إدارة المؤسسة والوصول

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **الهيكل التنظيمي** `FEAT-ORG-STRUCTURE` | CAP-01.01 إدارة المستأجرين والمؤسسات (R1) | يتيح للمسؤول بناء المؤسسة ووحداتها التنظيمية وتعديلها، ويمكّن كل مستخدم من رؤية شجرة المؤسسة. | المسؤول؛ مستخدم المستأجر | 9 + 5 |
| **دورة حياة المستأجر** `FEAT-ORG-TENANT-LIFECYCLE` | CAP-01.01 إدارة المستأجرين والمؤسسات (R1) | يتيح لمشغل المنصة إنشاء مستأجر جديد معزول وجاهز للاستخدام ومتابعة حالته وتعليقه أو إعادته أو إخراجه من الخدمة بأمان. | مشغل المنصة؛ مسؤول المستأجر؛ النظام | 9 + 7 |
| **مزامنة تغييرات الموارد البشرية** `FEAT-ORG-HR-SYNC` | CAP-01.02 الهوية والمصادقة والاتحاد (R1) | يحوّل تغييرات الوظيفة أو الوحدة القادمة من نظام الموارد البشرية إلى مقترحات يعتمدها المسؤول أو يرفضها قبل أن تتغير صلاحيات أي شخص. | المسؤول؛ مسؤول الأمن؛ النظام | 6 + 4 |
| **سجل الأشخاص** `FEAT-ORG-PERSONS` | CAP-01.02 الهوية والمصادقة والاتحاد (R1) | يتيح للمسؤول تسجيل الأشخاص العاملين في المؤسسة وتحديث بياناتهم وإيقافهم أو إعادتهم بشكل مستقل عن حساباتهم. | المسؤول | 4 + 3 |
| **حسابات الخدمة للأنظمة** `FEAT-ORG-SERVICE-ACCOUNTS` | CAP-01.02 الهوية والمصادقة والاتحاد (R1) | يتيح للمسؤول منح الأنظمة المتكاملة حسابات خاصة بها يمكن تعطيلها وتجديد بيانات اعتمادها وإغلاقها دون المساس بحسابات الأشخاص. | المسؤول | 5 + 4 |
| **الدخول الموحد وربط الهويات** `FEAT-ORG-SIGN-IN` | CAP-01.02 الهوية والمصادقة والاتحاد (R1) | يتيح للمستخدم الدخول بحسابه المؤسسي عبر مزود الهوية الخارجي دون كلمة مرور خاصة بالمنصة، ويتيح للمسؤول ربط الهويات الخارجية بالحساب. | المستخدم؛ المسؤول؛ النظام | 3 + 8 |
| **إدارة حسابات المستخدمين** `FEAT-ORG-USER-ACCOUNTS` | CAP-01.02 الهوية والمصادقة والاتحاد (R1) | يتيح للمسؤول ومسؤول الأمن إنشاء حسابات المستخدمين وتعطيلها وقفلها وإغلاقها والبحث فيها، مع بقائها متزامنة مع مزود الهوية. | المسؤول؛ مسؤول الأمن؛ خدمة مزامنة الحسابات (SCIM)؛ المستخدم | 9 + 5 |
| **منح صلاحيات القرار** `FEAT-ORG-AUTHORITY-GRANTS` | CAP-01.03 السلطة والتفويض (R1) | يحدد بوضوح من يملك سلطة اتخاذ كل نوع من القرارات وفي أي نطاق وحدود ومدة، مع اعتماد المنح وتعليقه وسحبه وانتهائه تلقائيًا. | حامل صلاحية منح السلطة؛ التنفيذي؛ المسؤول؛ صاحب السلطة؛ النظام | 8 + 2 |
| **تفويض السلطة والتحقق منها** `FEAT-ORG-DELEGATION` | CAP-01.03 السلطة والتفويض (R1) | يتيح لصاحب السلطة تفويض جزء من سلطته لغيره لمدة محددة دون تجاوز حدوده، ويتيح للمنصة التأكد قبل أي قرار أن صاحبه مخوّل به. | صاحب السلطة؛ المفوَّض إليه؛ الخدمات الداخلية | 2 + 4 |
| **فحص الوصول قبل كل طلب** `FEAT-ORG-ACCESS-ENFORCE` | CAP-01.04 سياسات الوصول (R1) | يضمن فحص كل عرض أو بحث أو تصدير أو طلب للخريطة أو للمساعد الذكي قبل جلب البيانات، فيُمنع أو يُحجب جزئيًا ما لا يحق للمستخدم رؤيته ويُرفض الطلب إذا تعذر الفحص. | المستخدم؛ النظام | 2 + 6 |
| **إدارة سياسات الوصول** `FEAT-ORG-ACCESS-POLICY` | CAP-01.04 سياسات الوصول (R1) | يتيح لمسؤول الأمن صياغة قواعد الوصول واختبارها وتقديمها للاعتماد ثم تطبيقها من تاريخ سريان محدد مع حفظ كل نسخة. | مسؤول الأمن؛ المدقق؛ النظام | 8 + 3 |
| **إسناد الأدوار للمستخدمين** `FEAT-ORG-ROLE-ASSIGNMENT` | CAP-01.04 سياسات الوصول (R1) | يتيح للمسؤول منح المستخدمين أدوارهم في نطاق محدد ولمدة محددة، وسحبها يدويًا أو تلقائيًا عند انتهاء مدتها. | المسؤول؛ النظام | 3 + 2 |
| **تعريف الأدوار وصلاحياتها** `FEAT-ORG-ROLES` | CAP-01.04 سياسات الوصول (R1) | يتيح للمسؤول تعريف أدوار العمل وتحديد ما يسمح به كل دور من عرض وتعديل وتصدير واعتماد، وتفعيل الأدوار أو إحالتها للتقاعد. | المسؤول | 4 + 2 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-01 (72)</summary>

- **الهيكل التنظيمي** `FEAT-ORG-STRUCTURE`
  - `US-BC01-ORG-ADD-UNIT` — إضافة وحدة تنظيمية إلى المؤسسة (أمر)
  - `US-BC01-ORG-CREATE` — إنشاء المؤسسة (أمر)
  - `US-BC01-ORG-DEACTIVATE` — إيقاف تفعيل المؤسسة (أمر)
  - `US-BC01-ORG-DEACTIVATE-UNIT` — إيقاف وحدة تنظيمية في المؤسسة (أمر)
  - `US-BC01-ORG-MOVE-UNIT` — نقل وحدة تنظيمية في المؤسسة (أمر)
  - `US-BC01-ORG-REACTIVATE` — إعادة تفعيل المؤسسة (أمر)
  - `US-BC01-ORG-RENAME` — إعادة تسمية المؤسسة (أمر)
  - `US-BC01-ORG-RENAME-UNIT` — إعادة تسمية وحدة تنظيمية في المؤسسة (أمر)
  - `US-BC01-Q-ORG-TREE` — جلب: Unit tree (cursor pagination on flattened order) (جلب)
- **دورة حياة المستأجر** `FEAT-ORG-TENANT-LIFECYCLE`
  - `US-BC01-Q-TEN-GET` — جلب: Tenant state, cell, quotas (جلب)
  - `US-BC01-TEN-COMPLETE-DECOMMISSION` — إكمال إخراج المستأجر من الخدمة (نظام)
  - `US-BC01-TEN-COMPLETE-PROVISIONING` — إكمال تهيئة المستأجر (نظام)
  - `US-BC01-TEN-FAIL-PROVISIONING` — تسجيل فشل تهيئة المستأجر (نظام)
  - `US-BC01-TEN-PROVISION` — تهيئة المستأجر (أمر)
  - `US-BC01-TEN-REACTIVATE` — إعادة تفعيل المستأجر (أمر)
  - `US-BC01-TEN-RETRY-PROVISIONING` — إعادة محاولة تهيئة المستأجر (أمر)
  - `US-BC01-TEN-START-DECOMMISSION` — بدء إخراج المستأجر من الخدمة (أمر)
  - `US-BC01-TEN-SUSPEND` — تعليق المستأجر (أمر)
- **مزامنة تغييرات الموارد البشرية** `FEAT-ORG-HR-SYNC`
  - `US-BC01-HRS-APPROVE` — اعتماد مقترح مزامنة الموارد البشرية (أمر)
  - `US-BC01-HRS-REJECT` — رفض مقترح مزامنة الموارد البشرية (أمر)
  - `US-BC01-Q-HRS-QUEUE` — جلب: Pending HR proposals by unit and change kind (leave first) (جلب)
  - `US-BC01-S-HR-SYNC-PROPOSAL-01` — تلقائي: HRIS change received (مقترح مزامنة الموارد البشرية) (نظام)
  - `US-BC01-S-HR-SYNC-PROPOSAL-02` — تلقائي: newer HR change for the same person (مقترح مزامنة الموارد البشرية) (نظام)
  - `US-BC01-S-HR-SYNC-PROPOSAL-03` — تلقائي: 14 days without decision (مقترح مزامنة الموارد البشرية) (نظام)
- **سجل الأشخاص** `FEAT-ORG-PERSONS`
  - `US-BC01-PER-DEACTIVATE` — إيقاف تفعيل الشخص (أمر)
  - `US-BC01-PER-REACTIVATE` — إعادة تفعيل الشخص (أمر)
  - `US-BC01-PER-REGISTER` — تسجيل الشخص (أمر)
  - `US-BC01-PER-UPDATE-DETAILS` — تحديث بيانات الشخص (أمر)
- **حسابات الخدمة للأنظمة** `FEAT-ORG-SERVICE-ACCOUNTS`
  - `US-BC01-SVC-CLOSE` — إغلاق حساب الخدمة (أمر)
  - `US-BC01-SVC-CREATE` — إنشاء حساب الخدمة (أمر)
  - `US-BC01-SVC-DISABLE` — تعطيل حساب الخدمة (أمر)
  - `US-BC01-SVC-ENABLE` — تمكين حساب الخدمة (أمر)
  - `US-BC01-SVC-ROTATE-CREDENTIAL` — تدوير بيانات اعتماد حساب الخدمة (أمر)
- **الدخول الموحد وربط الهويات** `FEAT-ORG-SIGN-IN`
  - `US-BC01-USR-LINK-IDENTITY` — ربط هوية خارجية بـحساب المستخدم (أمر)
  - `US-BC01-USR-RECORD-FIRST-SIGN-IN` — تسجيل أول دخول لـحساب المستخدم (نظام)
  - `US-BC01-USR-UNLINK-IDENTITY` — فك ربط هوية خارجية عن حساب المستخدم (أمر)
- **إدارة حسابات المستخدمين** `FEAT-ORG-USER-ACCOUNTS`
  - `US-BC01-Q-USR-GET` — جلب: User with identities (no secrets) (جلب)
  - `US-BC01-Q-USR-LIST` — جلب: Users filtered by state, unit, role (جلب)
  - `US-BC01-USR-CLOSE` — إغلاق حساب المستخدم (أمر)
  - `US-BC01-USR-DISABLE` — تعطيل حساب المستخدم (أمر)
  - `US-BC01-USR-ENABLE` — تمكين حساب المستخدم (أمر)
  - `US-BC01-USR-LINK-PERSON` — ربط شخص بـحساب المستخدم (أمر)
  - `US-BC01-USR-LOCK` — قفل حساب المستخدم (أمر)
  - `US-BC01-USR-PROVISION` — تهيئة حساب المستخدم (أمر)
  - `US-BC01-USR-UNLOCK` — فتح قفل حساب المستخدم (أمر)
- **منح صلاحيات القرار** `FEAT-ORG-AUTHORITY-GRANTS`
  - `US-BC01-AUT-APPROVE-GRANT` — اعتماد منح السلطة (أمر)
  - `US-BC01-AUT-GRANT` — إصدار منح السلطة (أمر)
  - `US-BC01-AUT-REJECT-GRANT` — رفض منح السلطة (أمر)
  - `US-BC01-AUT-RESUME` — استئناف منح السلطة (أمر)
  - `US-BC01-AUT-REVOKE` — سحب منح السلطة (أمر)
  - `US-BC01-AUT-SUSPEND` — تعليق منح السلطة (أمر)
  - `US-BC01-Q-AUT-LIST` — جلب: Grants by holder / scope / effective at t (جلب)
  - `US-BC01-S-AUTHORITY-GRANT-01` — تلقائي: valid_to reached (منح السلطة) (نظام)
- **تفويض السلطة والتحقق منها** `FEAT-ORG-DELEGATION`
  - `US-BC01-AUT-DELEGATE` — تفويض منح السلطة (أمر)
  - `US-BC01-Q-AUT-CHECK` — جلب: AuthorityCheck(actor, decision_type, scope, at, amount?) (جلب)
- **فحص الوصول قبل كل طلب** `FEAT-ORG-ACCESS-ENFORCE`
  - `US-BC01-Q-SEC-CONTEXT` — جلب: Caller's resolved SecurityContext (جلب)
  - `US-BC08-Q-PDP-DECIDE` — جلب: DecisionRequest → DecisionResponse (authorization-model §2) (جلب)
- **إدارة سياسات الوصول** `FEAT-ORG-ACCESS-POLICY`
  - `US-BC08-POL-APPROVE` — اعتماد مجموعة السياسات (أمر)
  - `US-BC08-POL-DRAFT` — إعداد مسودة مجموعة السياسات (أمر)
  - `US-BC08-POL-EDIT` — تعديل مجموعة السياسات (أمر)
  - `US-BC08-POL-REJECT` — رفض مجموعة السياسات (أمر)
  - `US-BC08-POL-SUBMIT` — تقديم مجموعة السياسات (أمر)
  - `US-BC08-Q-POL-GET` — جلب: Policy set version with tables and tests (جلب)
  - `US-BC08-S-POLICY-SET-01` — تلقائي: effective_from reached (مجموعة السياسات) (نظام)
  - `US-BC08-S-POLICY-SET-02` — تلقائي: successor activated (مجموعة السياسات) (نظام)
- **إسناد الأدوار للمستخدمين** `FEAT-ORG-ROLE-ASSIGNMENT`
  - `US-BC01-RAS-ASSIGN` — تسجيل إسناد الدور (أمر)
  - `US-BC01-RAS-REVOKE` — سحب إسناد الدور (أمر)
  - `US-BC01-S-ROLE-ASSIGNMENT-01` — تلقائي: valid_to reached (إسناد الدور) (نظام)
- **تعريف الأدوار وصلاحياتها** `FEAT-ORG-ROLES`
  - `US-BC01-ROL-ACTIVATE` — تفعيل الدور (أمر)
  - `US-BC01-ROL-DEFINE` — تعريف الدور (أمر)
  - `US-BC01-ROL-RETIRE` — إحالة الدور إلى التقاعد (أمر)
  - `US-BC01-ROL-SET-PERMISSIONS` — تحديد صلاحيات الدور (أمر)

</details>

### 2.2 CAP-02 — جمع المعلومات

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **متابعة استيفاء المتطلبات** `FEAT-COL-FULFILMENT` | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) | يعرض لوحة بالمتطلبات المفتوحة ومدى استيفائها والملاحظات التي أجابت عنها وينبه عند فوات موعدها. | مدير الجمع؛ المحلل؛ النظام | 4 + 4 |
| **تخطيط أنشطة الجمع** `FEAT-COL-PLAN` | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) | يتيح لمخطط الجمع أن يحول المتطلب المعتمد إلى خطة أنشطة ومصادر ومهام ميدانية ويتابعها حتى الاكتمال. | مخطط الجمع؛ النظام | 8 + 3 |
| **اعتماد متطلبات الجمع** `FEAT-COL-REQ-APPROVAL` | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) | يتيح لمدير الجمع أن يقبل أو يرفض أو يعدل طلبات المعلومات قبل توجيه جهد الجمع إليها. | مدير الجمع | 3 + 2 |
| **طلب حاجة معلوماتية** `FEAT-COL-REQ-REQUEST` | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) | يتيح للمحلل أن يصوغ سؤاله المعلوماتي ومنطقته وموعده ويقدمه للجمع ثم يتابعه حتى يستوفى أو يلغى. | المحلل؛ مقدم الطلب | 6 + 3 |
| **حماية هوية المصادر** `FEAT-COL-SOURCE-PROTECT` | CAP-02.02 إدارة المصادر (R1) | يتيح لمسؤول الأمن تحديد مستوى حماية المصدر وتصنيفه بحيث لا يرى هويته إلا المخولون. | مسؤول الأمن | 2 + 3 |
| **سجل المصادر وموثوقيتها** `FEAT-COL-SOURCES` | CAP-02.02 إدارة المصادر (R1) | يحفظ لكل مصدر ملفه ونوعه وتقدير موثوقيته عبر الزمن ويتيح تعليقه أو إحالته إلى التقاعد. | المحلل | 7 + 3 |
| **رفع المرفقات وتنزيلها** `FEAT-COL-ATTACHMENTS` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح رفع الصور والمستندات والفيديو بأمان مع فحصها والتحقق من سلامتها وتنزيلها للمخولين فقط. | المستخدم صاحب صلاحية الكتابة؛ النظام | 7 + 7 |
| **إدارة الأجهزة الميدانية** `FEAT-COL-DEVICES` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح تسجيل الأجهزة الميدانية واعتمادها وتعليقها وتدوير مفاتيحها حتى لا يعمل في الميدان إلا جهاز موثوق. | المستخدم الميداني؛ المسؤول؛ مسؤول الأمن | 7 + 6 |
| **حفظ الأدلة وسلسلة العهدة** `FEAT-COL-EVIDENCE` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يحفظ الدليل وموقعه ويختمه ويسجل كل نقل لعهدته حتى يبقى موثوقًا ومقبولًا. | المحلل؛ المستخدم الميداني؛ أمين العهدة | 7 + 4 |
| **المزامنة الميدانية** `FEAT-COL-FIELD-SYNC` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | ينقل ما سجله المستخدم الميداني دون اتصال إلى الخادم بترتيبه الأصلي دون تكرار ويجلب له آخر تحديثات مهامه. | المستخدم الميداني؛ الجهاز الميداني؛ النظام | 6 + 6 |
| **الإبلاغ عن جهاز مفقود** `FEAT-COL-LOST-DEVICE` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح الإبلاغ عن فقد الجهاز فيمنع مزامنته ويمسح بياناته عن بعد حماية للمعلومات. | المستخدم الميداني؛ المسؤول؛ النظام | 3 + 4 |
| **التحقق من الملاحظات** `FEAT-COL-OBS-REVIEW` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح للمحلل اعتماد الملاحظة أو رفضها أو إعادة تصنيفها قبل أن تعتمد عليها التحليلات. | المحلل | 3 + 3 |
| **تسجيل الملاحظات** `FEAT-COL-OBSERVATIONS` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح للمستخدم الميداني والمحلل تسجيل ما رصده في زمان ومكان محددين مع مرفقاته وتصحيحه بإصدار جديد والبحث فيه. | المستخدم الميداني؛ المشغل؛ المحلل؛ حساب المحوّل | 5 + 6 |
| **العمل الميداني دون اتصال** `FEAT-COL-OFFLINE-WORK` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح للمستخدم الميداني مواصلة العمل حتى 72 ساعة دون شبكة مع حفظ بياناته مشفرة على الجهاز. | المستخدم الميداني | 0 + 9 |
| **تحميل بيانات المنطقة مسبقًا** `FEAT-COL-PRELOAD` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح للمستخدم الميداني تنزيل بيانات منطقة عمله المصرح بها قبل الخروج لتعمل دون اتصال وتنتهي صلاحيتها تلقائيًا. | المستخدم الميداني؛ المسؤول؛ مسؤول الأمن؛ النظام | 8 + 5 |
| **حل تعارضات المزامنة** `FEAT-COL-SYNC-CONFLICTS` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يعرض على المراجع ما تعارض من تسجيلات ميدانية مع الوضع الحالي ليقرر إعادة تطبيقها أو إسقاطها أو حلها يدويًا. | المخطط؛ المحلل؛ النظام | 7 + 2 |
| **إدارة محوّلات البيانات** `FEAT-COL-ADAPTERS` | CAP-02.04 الاستيعاب والتكامل (R1) | يتيح للمسؤول تسجيل محوّلات البيانات الخارجية وربط حقولها وتفعيلها بموافقة مسؤول ثان. | المسؤول | 7 + 4 |
| **اتصالات الأنظمة الخارجية** `FEAT-COL-CONNECTIONS` | CAP-02.04 الاستيعاب والتكامل (R1) | يتيح لمهندس التكامل تسجيل الاتصال بالأنظمة الخارجية واختباره ومراقبة سلامته مع اعتماد أمني قبل تشغيله. | مهندس التكامل؛ مسؤول الأمن؛ المسؤول؛ النظام | 10 + 4 |
| **التكامل مع أنظمة المؤسسة** `FEAT-COL-ENTERPRISE-INT` | CAP-02.04 الاستيعاب والتكامل (R1) | يربط أنظمة الموارد البشرية والمالية وإدارة الوثائق بالمنصة دون أن تصبح مرجعًا للحقيقة. | مهندس التكامل؛ المسؤول | 0 + 5 |
| **استيراد الخرائط والطقس** `FEAT-COL-GEO-WEATHER` | CAP-02.04 الاستيعاب والتكامل (R1) | يتيح جلب الطبقات الجغرافية وبيانات الطقس من مزوديها المعتمدين لتظهر في الصورة العملياتية. | المسؤول؛ مهندس التكامل | 0 + 7 |
| **استيراد البيانات والحجر** `FEAT-COL-IMPORT` | CAP-02.04 الاستيعاب والتكامل (R1) | يتيح استيراد دفعات بيانات خارجية مع عزل السجلات المعيبة ومعالجتها قبل نشرها. | المسؤول؛ حساب المحوّل؛ النظام | 9 + 5 |
| **تدفقات الحساسات** `FEAT-COL-SENSORS` | CAP-02.04 الاستيعاب والتكامل (R1) | يتيح ربط تدفقات الحساسات وتحديد قواعد جودتها والتنبيه عند انقطاع بياناتها. | مهندس التكامل؛ المحلل؛ النظام | 7 + 5 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-02 (116)</summary>

- **متابعة استيفاء المتطلبات** `FEAT-COL-FULFILMENT`
  - `US-BC02-Q-CRQ-BOARD` — جلب: Requirements by area (bbox/polygon), state, priority, due (جلب)
  - `US-BC02-Q-CRQ-EVIDENCE` — جلب: Fulfilment links per EEI (visible observations only) with lineage (جلب)
  - `US-BC02-S-COLLECTION-REQUIREMENT-01` — تلقائي: validated observation matched (متطلب الجمع) (نظام)
  - `US-BC02-S-COLLECTION-REQUIREMENT-02` — تلقائي: due passed (متطلب الجمع) (نظام)
- **تخطيط أنشطة الجمع** `FEAT-COL-PLAN`
  - `US-BC02-CPL-ACTIVATE` — تفعيل خطة الجمع (أمر)
  - `US-BC02-CPL-ADD-ACTIVITY` — إضافة نشاط إلى خطة الجمع (أمر)
  - `US-BC02-CPL-CANCEL` — إلغاء خطة الجمع (أمر)
  - `US-BC02-CPL-COMPLETE` — إكمال خطة الجمع (أمر)
  - `US-BC02-CPL-CREATE` — إنشاء خطة الجمع (أمر)
  - `US-BC02-CPL-REMOVE-ACTIVITY` — إزالة نشاط من خطة الجمع (أمر)
  - `US-BC02-Q-CPL-GET` — جلب: Plan with activities and linked tasks (جلب)
  - `US-BC02-S-COLLECTION-PLAN-01` — تلقائي: all activity tasks terminal (خطة الجمع) (نظام)
- **اعتماد متطلبات الجمع** `FEAT-COL-REQ-APPROVAL`
  - `US-BC02-CRQ-AMEND` — تعديل متطلب الجمع بإصدار جديد (أمر)
  - `US-BC02-CRQ-APPROVE` — اعتماد متطلب الجمع (أمر)
  - `US-BC02-CRQ-REJECT` — رفض متطلب الجمع (أمر)
- **طلب حاجة معلوماتية** `FEAT-COL-REQ-REQUEST`
  - `US-BC02-CRQ-CANCEL` — إلغاء متطلب الجمع (أمر)
  - `US-BC02-CRQ-DRAFT` — إعداد مسودة متطلب الجمع (أمر)
  - `US-BC02-CRQ-EDIT` — تعديل متطلب الجمع (أمر)
  - `US-BC02-CRQ-MARK-SATISFIED` — تعليم متطلب الجمع كمستوفى (أمر)
  - `US-BC02-CRQ-SUBMIT` — تقديم متطلب الجمع (أمر)
  - `US-BC02-Q-CRQ-GET` — جلب: Requirement with EEIs and fulfilment computed over observations visible to the caller (جلب)
- **حماية هوية المصادر** `FEAT-COL-SOURCE-PROTECT`
  - `US-BC02-SRC-RECLASSIFY` — إعادة تصنيف المصدر (أمر)
  - `US-BC02-SRC-SET-PROTECTION` — تحديد مستوى حماية المصدر (أمر)
- **سجل المصادر وموثوقيتها** `FEAT-COL-SOURCES`
  - `US-BC02-Q-SRC-GET` — جلب: Source; identity only with source-protection permission (جلب)
  - `US-BC02-SRC-RATE-RELIABILITY` — تقدير موثوقية المصدر (أمر)
  - `US-BC02-SRC-REGISTER` — تسجيل المصدر (أمر)
  - `US-BC02-SRC-REINSTATE` — إعادة المصدر إلى السريان (أمر)
  - `US-BC02-SRC-RETIRE` — إحالة المصدر إلى التقاعد (أمر)
  - `US-BC02-SRC-SUSPEND` — تعليق المصدر (أمر)
  - `US-BC02-SRC-UPDATE-PROFILE` — تحديث ملف المصدر (أمر)
- **رفع المرفقات وتنزيلها** `FEAT-COL-ATTACHMENTS`
  - `US-BC02-ATT-COMPLETE-UPLOAD` — إكمال رفع المرفق (أمر)
  - `US-BC02-ATT-ERASE` — محو المرفق (أمر)
  - `US-BC02-ATT-INITIATE-UPLOAD` — بدء رفع المرفق (أمر)
  - `US-BC02-Q-ATT-DOWNLOAD` — جلب: Short-lived signed download target (≤ 5 min); audited (جلب)
  - `US-BC02-S-ATTACHMENT-01` — تلقائي: scan passed (المرفق) (نظام)
  - `US-BC02-S-ATTACHMENT-02` — تلقائي: scan failed (المرفق) (نظام)
  - `US-BC02-S-ATTACHMENT-03` — تلقائي: upload window 24 h elapsed (المرفق) (نظام)
- **إدارة الأجهزة الميدانية** `FEAT-COL-DEVICES`
  - `US-BC01-DEV-CONFIRM` — تأكيد الجهاز الميداني (أمر)
  - `US-BC01-DEV-ENROLL` — تسجيل الجهاز الميداني (أمر)
  - `US-BC01-DEV-REINSTATE` — إعادة الجهاز الميداني إلى السريان (أمر)
  - `US-BC01-DEV-RETIRE` — إحالة الجهاز الميداني إلى التقاعد (أمر)
  - `US-BC01-DEV-ROTATE-KEY` — تدوير مفتاح الجهاز الميداني (أمر)
  - `US-BC01-DEV-SUSPEND` — تعليق الجهاز الميداني (أمر)
  - `US-BC01-Q-DEV-LIST` — جلب: Devices of a user (self) or in scope (Administrator) (جلب)
- **حفظ الأدلة وسلسلة العهدة** `FEAT-COL-EVIDENCE`
  - `US-BC02-EVD-RECLASSIFY` — إعادة تصنيف الدليل (أمر)
  - `US-BC02-EVD-REGISTER` — تسجيل الدليل (أمر)
  - `US-BC02-EVD-SEAL` — ختم الدليل (أمر)
  - `US-BC02-EVD-TRANSFER-CUSTODY` — نقل عهدة الدليل (أمر)
  - `US-BC02-EVD-UPDATE-LOCATOR` — تحديث محدِّد موقع الدليل (أمر)
  - `US-BC02-EVD-WITHDRAW` — سحب الدليل (أمر)
  - `US-BC02-Q-EVD-GET` — جلب: Evidence metadata and custody chain (جلب)
- **المزامنة الميدانية** `FEAT-COL-FIELD-SYNC`
  - `US-BC07-Q-SYN-DELTA` — جلب: Server → device: my task changes, package updates, purge list, conflict notices, wipe/stop instruction (جلب)
  - `US-BC07-S-SYNC-SESSION-02` — تلقائي: all uploaded commands processed without conflict (جلسة المزامنة) (نظام)
  - `US-BC07-S-SYNC-SESSION-03` — تلقائي: all processed with ≥ 1 sync conflict (جلسة المزامنة) (نظام)
  - `US-BC07-S-SYNC-SESSION-04` — تلقائي: idle timeout (5 min) or transport loss (جلسة المزامنة) (نظام)
  - `US-BC07-SYN-OPEN` — فتح جلسة المزامنة (أمر)
  - `US-BC07-SYN-UPLOAD-BATCH` — رفع دفعة إلى جلسة المزامنة (أمر)
- **الإبلاغ عن جهاز مفقود** `FEAT-COL-LOST-DEVICE`
  - `US-BC01-DEV-REPORT-LOST` — الإبلاغ عن فقد الجهاز الميداني (أمر)
  - `US-BC01-S-DEVICE-01` — تلقائي: wipe confirmed by device (الجهاز الميداني) (نظام)
  - `US-BC07-S-SYNC-SESSION-01` — تلقائي: device LOST or SUSPENDED at handshake (جلسة المزامنة) (نظام)
- **التحقق من الملاحظات** `FEAT-COL-OBS-REVIEW`
  - `US-BC02-OBS-RECLASSIFY` — إعادة تصنيف الملاحظة (أمر)
  - `US-BC02-OBS-REJECT` — رفض الملاحظة (أمر)
  - `US-BC02-OBS-VALIDATE` — التحقق من الملاحظة (أمر)
- **تسجيل الملاحظات** `FEAT-COL-OBSERVATIONS`
  - `US-BC02-OBS-AMEND` — تعديل الملاحظة بإصدار جديد (أمر)
  - `US-BC02-OBS-ATTACH-EVIDENCE` — إرفاق دليل بـالملاحظة (أمر)
  - `US-BC02-OBS-RECORD` — تسجيل الملاحظة (أمر)
  - `US-BC02-Q-OBS-GET` — جلب: Observation with measurements and attachment refs (جلب)
  - `US-BC02-Q-OBS-LIST` — جلب: Observations by bbox, time window (mandatory, ≤ 31 days), source, state (جلب)
- **العمل الميداني دون اتصال** `FEAT-COL-OFFLINE-WORK` — بلا قصص حالية
- **تحميل بيانات المنطقة مسبقًا** `FEAT-COL-PRELOAD`
  - `US-BC07-PKG-CONFIRM-DOWNLOAD` — تأكيد تنزيل حزمة التحميل المسبق (أمر)
  - `US-BC07-PKG-REQUEST` — طلب حزمة التحميل المسبق (أمر)
  - `US-BC07-PKG-REVOKE` — سحب حزمة التحميل المسبق (أمر)
  - `US-BC07-Q-PKG-GET` — جلب: Package manifest and download target (signed, ≤ 5 min) (جلب)
  - `US-BC07-S-PRELOAD-PACKAGE-01` — تلقائي: build started (حزمة التحميل المسبق) (نظام)
  - `US-BC07-S-PRELOAD-PACKAGE-02` — تلقائي: build finished (حزمة التحميل المسبق) (نظام)
  - `US-BC07-S-PRELOAD-PACKAGE-03` — تلقائي: expires_at reached (حزمة التحميل المسبق) (نظام)
  - `US-BC07-S-PRELOAD-PACKAGE-04` — تلقائي: user security_version changed or device not ACTIVE (حزمة التحميل المسبق) (نظام)
- **حل تعارضات المزامنة** `FEAT-COL-SYNC-CONFLICTS`
  - `US-BC07-Q-SCF-GET` — جلب: Original envelope, current state snapshot, owner rejection reason (جلب)
  - `US-BC07-Q-SCF-LIST` — جلب: Open sync conflicts by target type, assignee (جلب)
  - `US-BC07-S-SYNC-CONFLICT-01` — تلقائي: stale state-changing command (تعارض المزامنة) (نظام)
  - `US-BC07-SCF-ASSIGN` — إسناد تعارض المزامنة (أمر)
  - `US-BC07-SCF-DISCARD` — حسم تعارض المزامنة بإسقاط الأمر الميداني (أمر)
  - `US-BC07-SCF-REAPPLY` — إعادة تطبيق تعارض المزامنة (أمر)
  - `US-BC07-SCF-RESOLVE-MANUALLY` — حل تعارض المزامنة يدويًا (أمر)
- **إدارة محوّلات البيانات** `FEAT-COL-ADAPTERS`
  - `US-BC07-ADP-ACTIVATE` — تفعيل المحوّل (أمر)
  - `US-BC07-ADP-REGISTER` — تسجيل المحوّل (أمر)
  - `US-BC07-ADP-RESUME` — استئناف المحوّل (أمر)
  - `US-BC07-ADP-RETIRE` — إحالة المحوّل إلى التقاعد (أمر)
  - `US-BC07-ADP-SUSPEND` — تعليق المحوّل (أمر)
  - `US-BC07-ADP-UPDATE-MAPPING` — تحديث ربط حقول المحوّل (أمر)
  - `US-BC07-Q-ADP-GET` — جلب: Adapter with mapping versions (جلب)
- **اتصالات الأنظمة الخارجية** `FEAT-COL-CONNECTIONS`
  - `US-BC07-CON-ACTIVATE` — تفعيل اتصال التكامل (أمر)
  - `US-BC07-CON-FAIL-TEST` — تسجيل فشل اختبار اتصال التكامل (أمر)
  - `US-BC07-CON-REGISTER` — تسجيل اتصال التكامل (أمر)
  - `US-BC07-CON-RESUME` — استئناف اتصال التكامل (أمر)
  - `US-BC07-CON-RETIRE` — إحالة اتصال التكامل إلى التقاعد (أمر)
  - `US-BC07-CON-SUSPEND` — تعليق اتصال التكامل (أمر)
  - `US-BC07-CON-TEST` — اختبار اتصال التكامل (أمر)
  - `US-BC07-Q-CON-LIST` — جلب: Connections with state, health, allow-list entry (جلب)
  - `US-BC07-S-INTEGRATION-CONNECTION-01` — تلقائي: health checks failing 5 min (اتصال التكامل) (نظام)
  - `US-BC07-S-INTEGRATION-CONNECTION-02` — تلقائي: health restored (اتصال التكامل) (نظام)
- **التكامل مع أنظمة المؤسسة** `FEAT-COL-ENTERPRISE-INT` — بلا قصص حالية
- **استيراد الخرائط والطقس** `FEAT-COL-GEO-WEATHER` — بلا قصص حالية
- **استيراد البيانات والحجر** `FEAT-COL-IMPORT`
  - `US-BC02-IMP-ACCEPT-QUARANTINE` — قبول العناصر المعزولة في دفعة الاستيراد (أمر)
  - `US-BC02-IMP-CANCEL` — إلغاء دفعة الاستيراد (أمر)
  - `US-BC02-IMP-REPROCESS-QUARANTINE` — إعادة معالجة العناصر المعزولة في دفعة الاستيراد (أمر)
  - `US-BC02-IMP-SUBMIT` — تقديم دفعة الاستيراد (أمر)
  - `US-BC02-Q-IMP-GET` — جلب: Batch status, counts, quarantine records (paged) (جلب)
  - `US-BC02-S-IMPORT-BATCH-01` — تلقائي: processing started (دفعة الاستيراد) (نظام)
  - `US-BC02-S-IMPORT-BATCH-02` — تلقائي: all records applied (دفعة الاستيراد) (نظام)
  - `US-BC02-S-IMPORT-BATCH-03` — تلقائي: finished with invalid records (دفعة الاستيراد) (نظام)
  - `US-BC02-S-IMPORT-BATCH-04` — تلقائي: unrecoverable error (دفعة الاستيراد) (نظام)
- **تدفقات الحساسات** `FEAT-COL-SENSORS`
  - `US-BC07-Q-SNS-LIST` — جلب: Streams with rate, staleness, quality violation counts (جلب)
  - `US-BC07-S-SENSOR-STREAM-01` — تلقائي: no data beyond stale-after (تدفق الحسّاس) (نظام)
  - `US-BC07-SNS-ACTIVATE` — تفعيل تدفق الحسّاس (أمر)
  - `US-BC07-SNS-PAUSE` — إيقاف تدفق الحسّاس مؤقتًا (أمر)
  - `US-BC07-SNS-REGISTER` — تسجيل تدفق الحسّاس (أمر)
  - `US-BC07-SNS-RETIRE` — إحالة تدفق الحسّاس إلى التقاعد (أمر)
  - `US-BC07-SNS-SET-QUALITY-RULES` — تحديد قواعد جودة تدفق الحسّاس (أمر)

</details>

### 2.3 CAP-03 — إدارة المعلومات

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **إدارة الكيانات وملفاتها** `FEAT-INF-ENTITY-REGISTRY` | CAP-03.01 الكيانات والعلاقات (R1) | يسجّل المحلل الأشخاص والجهات والأماكن ويعدّلها ويطّلع على ملف كل منها بقيمه المؤكدة والمتنازع عليها. | المحلل؛ خدمة المحوّل؛ كل مستخدم مخوَّل | 7 + 7 |
| **ربط المعرّفات الخارجية** `FEAT-INF-EXTERNAL-IDS` | CAP-03.01 الكيانات والعلاقات (R1) | تبقى السجلات الواردة من الأنظمة الخارجية مرتبطة بالعنصر الصحيح لدينا فلا تتكرر ولا تضيع. | خدمة المحوّل؛ المحلل | 3 + 5 |
| **استكشاف شبكة العلاقات** `FEAT-INF-GRAPH-EXPLORE` | CAP-03.01 الكيانات والعلاقات (R1) | يستكشف المحلل محيط الكيان والمسارات التي تربط كيانين دون أن يرى ما لا يحق له. | المحلل | 2 + 6 |
| **إعادة بناء فهارس البحث** `FEAT-INF-INDEX-REBUILD` | CAP-03.01 الكيانات والعلاقات (R1) | يعيد مشغل المنصة بناء فهارس البحث والرسم البياني من المصدر الأصلي دون فقد بيانات ويراقب تأخرها. | مشغل المنصة؛ النظام | 9 + 7 |
| **تسجيل الأحداث الواقعية** `FEAT-INF-REAL-EVENTS` | CAP-03.01 الكيانات والعلاقات (R1) | يوثّق المحلل الأحداث التي وقعت في الواقع ويصنّفها ويعرض صورتها الموحّدة. | المحلل؛ خدمة المحوّل؛ كل مستخدم مخوَّل | 6 + 4 |
| **إدارة العلاقات بين الكيانات** `FEAT-INF-RELATIONSHIPS` | CAP-03.01 الكيانات والعلاقات (R1) | يربط المحلل الكيانات بعلاقات موثقة ومؤرخة ويرى كل علاقات الكيان في الاتجاهين. | المحلل؛ خدمة المحوّل؛ كل مستخدم مخوَّل | 5 + 3 |
| **البحث الموحد** `FEAT-INF-UNIFIED-SEARCH` | CAP-03.01 الكيانات والعلاقات (R1) | يجد المستخدم ما يبحث عنه من كيانات وملاحظات ووثائق وخطط بالنص والمكان والزمن وبالعربية والإنجليزية دون كشف ما لا يحق له. | كل مستخدم مخوَّل | 2 + 8 |
| **الادعاءات وأدلتها** `FEAT-INF-CLAIMS-EVIDENCE` | CAP-03.02 الادعاءات والأدلة (R1) | يسجّل المحلل كل معلومة كادعاء مسند إلى مصادره وأدلته ويصححه أو يسحبه دون أن يُمحى أصله. | المحلل؛ خدمة المحوّل؛ هوية تشغيل التحليل؛ كل مستخدم مخوَّل | 7 + 6 |
| **مواقع الكيانات وتحركاتها** `FEAT-INF-GEO-LOCATION` | CAP-03.03 المعلومات الجغرافية (R1) | يرى المستخدم أين كان الكيان وكيف تحرّك عبر الزمن بمواقع دقيقة وموثوقة الإحداثيات. | كل مستخدم مخوَّل؛ المحلل | 1 + 6 |
| **تاريخ المعلومة عبر الزمن** `FEAT-INF-TIME-HISTORY` | CAP-03.04 الزمن والتاريخ (R1) | يعرف المستخدم ما كان صحيحًا في أي وقت وما كان معروفًا عنه حينها ويسجّل المحلل تغيّر القيم بمرور الزمن. | المحلل؛ كل مستخدم مخوَّل | 2 + 4 |
| **فصل الكيانات المدموجة خطأً** `FEAT-INF-ENTITY-SPLIT` | CAP-03.05 مطابقة الكيانات (R1) | يستطيع المحلل التراجع عن دمج خاطئ فيعود كل كيان بمعلوماته الخاصة كما كانت. | المحلل؛ المحلل الثاني؛ كل مستخدم مخوَّل | 3 + 3 |
| **مراجعة تطابق الكيانات** `FEAT-INF-MATCH-REVIEW` | CAP-03.05 مطابقة الكيانات (R1) | يراجع المحللون الكيانات المشتبه بأنها الشيء نفسه ويقررون دمجها أو فصلها بقرار موثق ومؤكد من محلل ثانٍ. | المحلل؛ المحلل الثاني؛ النظام | 11 + 4 |
| **قواعد المطابقة** `FEAT-INF-MATCH-RULES` | CAP-03.05 مطابقة الكيانات (R1) | يضبط قائد المحللين قواعد اكتشاف التطابق ويقيس دقتها قبل أن يفعّلها مسؤول آخر. | قائد المحللين؛ المسؤول؛ النظام | 5 + 3 |
| **كشف تعارض المعلومات** `FEAT-INF-CONFLICT-DETECT` | CAP-03.06 إدارة التعارض (R1) | يُكشف تلقائيًا أو يدويًا كل تناقض بين معلومتين عن الشيء نفسه فيُحفظ الطرفان ولا يُخفى أحدهما. | النظام؛ المحلل | 5 + 2 |
| **حل التعارضات** `FEAT-INF-CONFLICT-RESOLVE` | CAP-03.06 إدارة التعارض (R1) | يُسند قائد المحللين التعارض لمحلل يدرسه ويحسمه أو يقبله مع إمكانية إعادة فتحه. | قائد المحللين؛ المحلل | 6 + 2 |
| **الثقة بالمعلومة ومنشؤها** `FEAT-INF-TRUST-LINEAGE` | CAP-03.07 المنشأ والثقة (R1) | يقيّم المحلل درجة الثقة بالمعلومة وحالة التحقق منها ويتتبّع من أين جاءت وكيف اشتُقّت. | المحلل؛ المدقق؛ النظام | 2 + 5 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-03 (76)</summary>

- **إدارة الكيانات وملفاتها** `FEAT-INF-ENTITY-REGISTRY`
  - `US-BC02-ENT-CHANGE-TYPE` — تغيير نوع الكيان (أمر)
  - `US-BC02-ENT-RECLASSIFY` — إعادة تصنيف الكيان (أمر)
  - `US-BC02-ENT-REGISTER` — تسجيل الكيان (أمر)
  - `US-BC02-ENT-REINSTATE` — إعادة الكيان إلى السريان (أمر)
  - `US-BC02-ENT-RETIRE` — إحالة الكيان إلى التقاعد (أمر)
  - `US-BC02-Q-ENT-LIST` — جلب: Entities by type, bbox/polygon of current location, valid_at (جلب)
  - `US-BC02-Q-ENT-RESOLVED` — جلب: Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED candidates, confidence); resolves through the identity cluster and returns canonical_urn + requested_urn (SLC-04) (جلب)
- **ربط المعرّفات الخارجية** `FEAT-INF-EXTERNAL-IDS`
  - `US-BC02-EXT-END` — إنهاء ربط المعرّف الخارجي (أمر)
  - `US-BC02-EXT-MAP` — تسجيل ربط ربط المعرّف الخارجي (أمر)
  - `US-BC02-Q-EXT-RESOLVE` — جلب: Object URN mapped at time t (not-found shape if hidden) (جلب)
- **استكشاف شبكة العلاقات** `FEAT-INF-GRAPH-EXPLORE`
  - `US-BC07-Q-GRAPH-NEIGHBORHOOD` — جلب: Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges cut (جلب)
  - `US-BC07-Q-GRAPH-PATHS` — جلب: Paths between two entities, ≤ 4 hops, only through visible nodes and edges (جلب)
- **إعادة بناء فهارس البحث** `FEAT-INF-INDEX-REBUILD`
  - `US-BC07-PRJ-CANCEL-BUILD` — إلغاء بناء إصدار الإسقاط (أمر)
  - `US-BC07-PRJ-CREATE-VERSION` — إنشاء إصدار جديد من إصدار الإسقاط (أمر)
  - `US-BC07-PRJ-PROMOTE` — ترقية إصدار الإسقاط (أمر)
  - `US-BC07-PRJ-RETIRE` — إحالة إصدار الإسقاط إلى التقاعد (أمر)
  - `US-BC07-Q-PRJ-STATUS` — جلب: Projection versions, lag, state (جلب)
  - `US-BC07-S-PROJECTION-VERSION-01` — تلقائي: full rebuild reached live checkpoint (إصدار الإسقاط) (نظام)
  - `US-BC07-S-PROJECTION-VERSION-02` — تلقائي: build failed (إصدار الإسقاط) (نظام)
  - `US-BC07-S-PROJECTION-VERSION-03` — تلقائي: lag above threshold (إصدار الإسقاط) (نظام)
  - `US-BC07-S-PROJECTION-VERSION-04` — تلقائي: lag back within target (إصدار الإسقاط) (نظام)
- **تسجيل الأحداث الواقعية** `FEAT-INF-REAL-EVENTS`
  - `US-BC02-Q-RWE-GET` — جلب: Resolved real-world event (جلب)
  - `US-BC02-RWE-CHANGE-TYPE` — تغيير نوع الحدث الواقعي (أمر)
  - `US-BC02-RWE-RECLASSIFY` — إعادة تصنيف الحدث الواقعي (أمر)
  - `US-BC02-RWE-REGISTER` — تسجيل الحدث الواقعي (أمر)
  - `US-BC02-RWE-REINSTATE` — إعادة الحدث الواقعي إلى السريان (أمر)
  - `US-BC02-RWE-RETIRE` — إحالة الحدث الواقعي إلى التقاعد (أمر)
- **إدارة العلاقات بين الكيانات** `FEAT-INF-RELATIONSHIPS`
  - `US-BC02-Q-REL-LIST` — جلب: Relationships valid_at/known_at, both directions (جلب)
  - `US-BC02-REL-RECLASSIFY` — إعادة تصنيف العلاقة (أمر)
  - `US-BC02-REL-REGISTER` — تسجيل العلاقة (أمر)
  - `US-BC02-REL-REINSTATE` — إعادة العلاقة إلى السريان (أمر)
  - `US-BC02-REL-RETIRE` — إحالة العلاقة إلى التقاعد (أمر)
- **البحث الموحد** `FEAT-INF-UNIFIED-SEARCH`
  - `US-BC07-Q-SRCH-QUERY` — جلب: Unified search: text + types + polygon/bbox + time window + filters + facets; cursor paging; results and facets over visible facts only (جلب)
  - `US-BC07-Q-SRCH-SUGGEST` — جلب: Autocomplete from visible facts only (جلب)
- **الادعاءات وأدلتها** `FEAT-INF-CLAIMS-EVIDENCE`
  - `US-BC02-CLM-ASSERT` — تسجيل الادعاء (أمر)
  - `US-BC02-CLM-CORRECT` — تصحيح الادعاء (أمر)
  - `US-BC02-CLM-RECLASSIFY` — إعادة تصنيف الادعاء (أمر)
  - `US-BC02-CLM-RETRACT` — سحب الادعاء (أمر)
  - `US-BC02-EVL-LINK` — ربط رابط الدليل (أمر)
  - `US-BC02-EVL-UNLINK` — فك ربط رابط الدليل (أمر)
  - `US-BC02-Q-CLM-GET` — جلب: Claim with sources (per protection), evidence links, supersession chain (جلب)
- **مواقع الكيانات وتحركاتها** `FEAT-INF-GEO-LOCATION`
  - `US-BC02-Q-ENT-POSITIONS` — جلب: Position history in [from,to) as known_at (جلب)
- **تاريخ المعلومة عبر الزمن** `FEAT-INF-TIME-HISTORY`
  - `US-BC02-CLM-RECORD-CHANGE` — تسجيل تغيير في الادعاء (أمر)
  - `US-BC02-Q-ENT-CLAIMS` — جلب: Claim history (predicate, valid_at, known_at, include_closed) (جلب)
- **فصل الكيانات المدموجة خطأً** `FEAT-INF-ENTITY-SPLIT`
  - `US-BC02-ER-REQUEST-SPLIT` — طلب فصل حالة مطابقة الكيانات (أمر)
  - `US-BC02-ER-SPLIT` — فصل حالة مطابقة الكيانات (أمر)
  - `US-BC02-Q-CLUSTER-GET` — جلب: Cluster members, canonical URN, links, as known_at (جلب)
- **مراجعة تطابق الكيانات** `FEAT-INF-MATCH-REVIEW`
  - `US-BC02-ER-CONFIRM-MATCH` — تأكيد تطابق حالة مطابقة الكيانات (أمر)
  - `US-BC02-ER-DECIDE-MATCH` — الحكم بتطابق حالة مطابقة الكيانات (أمر)
  - `US-BC02-ER-DECIDE-NOT-MATCH` — الحكم بعدم تطابق حالة مطابقة الكيانات (أمر)
  - `US-BC02-ER-PARK` — تأجيل حالة مطابقة الكيانات (أمر)
  - `US-BC02-ER-PROPOSE` — اقتراح حالة مطابقة الكيانات (أمر)
  - `US-BC02-ER-RESUME` — استئناف حالة مطابقة الكيانات (أمر)
  - `US-BC02-ER-START-REVIEW` — بدء مراجعة حالة مطابقة الكيانات (أمر)
  - `US-BC02-ER-WITHDRAW` — سحب حالة مطابقة الكيانات (أمر)
  - `US-BC02-Q-ER-GET` — جلب: Case with side-by-side feature comparison (visible claims only) (جلب)
  - `US-BC02-Q-ER-QUEUE` — جلب: Review queue by state, entity type, score, ruleset (جلب)
  - `US-BC02-S-ER-CASE-01` — تلقائي: candidate generator score ≥ propose threshold (حالة مطابقة الكيانات) (نظام)
- **قواعد المطابقة** `FEAT-INF-MATCH-RULES`
  - `US-BC02-MRS-ACTIVATE` — تفعيل مجموعة قواعد المطابقة (أمر)
  - `US-BC02-MRS-DRAFT` — إعداد مسودة مجموعة قواعد المطابقة (أمر)
  - `US-BC02-MRS-EDIT` — تعديل مجموعة قواعد المطابقة (أمر)
  - `US-BC02-Q-MRS-GET` — جلب: Ruleset with evaluation report (جلب)
  - `US-BC02-S-MATCH-RULESET-01` — تلقائي: successor activated (مجموعة قواعد المطابقة) (نظام)
- **كشف تعارض المعلومات** `FEAT-INF-CONFLICT-DETECT`
  - `US-BC02-CNF-RAISE` — رفع التعارض (أمر)
  - `US-BC02-Q-CNF-LIST` — جلب: Conflicts by subject, predicate, state, assignee (جلب)
  - `US-BC02-S-CONFLICT-01` — تلقائي: conflict rule matched (التعارض) (نظام)
  - `US-BC02-S-CONFLICT-02` — تلقائي: incompatible claim joined (التعارض) (نظام)
  - `US-BC02-S-CONFLICT-03` — تلقائي: member set no longer conflicting (التعارض) (نظام)
- **حل التعارضات** `FEAT-INF-CONFLICT-RESOLVE`
  - `US-BC02-CNF-ACCEPT` — قبول التعارض (أمر)
  - `US-BC02-CNF-ASSIGN` — إسناد التعارض (أمر)
  - `US-BC02-CNF-REOPEN` — إعادة فتح التعارض (أمر)
  - `US-BC02-CNF-RESOLVE` — حل التعارض (أمر)
  - `US-BC02-CNF-START-REVIEW` — بدء مراجعة التعارض (أمر)
  - `US-BC02-Q-CNF-GET` — جلب: Conflict with visible members, evidence, resolution history (as known_at) (جلب)
- **الثقة بالمعلومة ومنشؤها** `FEAT-INF-TRUST-LINEAGE`
  - `US-BC02-CLM-ASSESS` — تقييم الادعاء (أمر)
  - `US-BC02-Q-LIN-TRACE` — جلب: Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy (جلب)

</details>

### 2.4 CAP-04 — التحليل والتقييم

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **الفرضيات والافتراضات والأدلة** `FEAT-ANL-ARGUMENT` | CAP-04.01 حالات التحليل (R1) | يبني المحلل حجته بفرضيات وافتراضات صريحة وأدلة مختارة، فيعرف القارئ على ماذا يستند الاستنتاج. | المحلل | 6 + 3 |
| **فتح حالة تحليل وإدارتها** `FEAT-ANL-CASE-SETUP` | CAP-04.01 حالات التحليل (R1) | يبدأ المحلل عمله التحليلي من حالة واحدة تحدد السؤال والنطاق، ويتابعها حتى الإغلاق أو إعادة الفتح. | المحلل؛ مسؤول الأمن؛ المستخدم المخوَّل | 9 + 6 |
| **السيناريوهات ومقارنة النتائج** `FEAT-ANL-SCENARIOS` | CAP-04.01 حالات التحليل (R1) | يقارن المحلل نتائج سيناريوهات مختلفة جنبًا إلى جنب ويرى الاستنتاجات مع مصادرها. | المحلل؛ المستخدم المخوَّل | 2 + 3 |
| **إدارة طرق التحليل** `FEAT-ANL-METHODS` | CAP-04.02 التنفيذ وإعادة الإنتاج (R1) | يعتمد قائد التحليل الطرق المسموح بها وإصداراتها، فلا يُستخدم إلا ما رُوجع واعتُمد. | قائد التحليل؛ المسؤول؛ المحلل | 5 + 2 |
| **تشغيل التحليل وإعادة إنتاجه** `FEAT-ANL-RUNS` | CAP-04.02 التنفيذ وإعادة الإنتاج (R1) | يشغّل المحلل تحليلًا طويلًا دون انتظار، ويتابع تقدمه، ويعيد تشغيله لاحقًا ليحصل على النتيجة نفسها أو يعرف ما الذي اختلف. | المحلل؛ النظام | 8 + 7 |
| **إعداد التقييم** `FEAT-ANL-ASSESSMENT-DRAFT` | CAP-04.03 إنتاج التقييم (R1) | يكتب المحلل تقييمه بالاستنتاجات والأدلة ودرجة الثقة وحدودها، ثم يقدمه للمراجعة. | المحلل | 4 + 2 |
| **الاطلاع على التقييمات ونسخها** `FEAT-ANL-ASSESSMENT-READ` | CAP-04.03 إنتاج التقييم (R1) | يقرأ المدير ومتخذ القرار التقييم المنشور أو نسخة سابقة منه، مع حجب ما لا يحق له رؤيته من الأدلة. | المدير؛ المحلل؛ المستخدم المخوَّل | 2 + 4 |
| **مراجعة التقييم ونشره** `FEAT-ANL-ASSESSMENT-REVIEW` | CAP-04.03 إنتاج التقييم (R1) | يراجع قائد التحليل التقييم فيعيده للتحسين أو ينشره نسخة ثابتة لا تتغير، أو يسحبه إن لزم. | المراجع؛ قائد التحليل؛ النظام | 4 + 3 |
| **النتائج التحليلية** `FEAT-ANL-FINDINGS` | CAP-04.03 إنتاج التقييم (R1) | يسجّل المحلل كل نتيجة بمصادرها ودرجة عدم اليقين فيها، ويراجعها زميل قبل أن يُبنى عليها تقييم. | المحلل؛ المراجع النظير | 5 + 3 |
| **مراجعة مقترحات الربط** `FEAT-ANL-CORRELATION-REVIEW` | CAP-04.04 الدمج والربط (R2) | يراجع المحلل ما يقترحه النظام من ربط بين ملاحظات ومصادر مختلفة فيقبله أو يرفضه بناءً على الأدلة والدرجة. | المحلل؛ النظام | 8 + 4 |
| **قواعد الربط الآلي** `FEAT-ANL-CORRELATION-RULES` | CAP-04.04 الدمج والربط (R2) | يضبط قائد التحليل قواعد الربط الآلي ويعتمدها بموافقة ثانية، فلا تُولَّد مقترحات من قواعد غير معتمدة. | قائد التحليل؛ الموافق الثاني | 4 + 3 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-04 (57)</summary>

- **الفرضيات والافتراضات والأدلة** `FEAT-ANL-ARGUMENT`
  - `US-BC03-ACS-ADD-ASSUMPTION` — إضافة افتراض إلى حالة التحليل (أمر)
  - `US-BC03-ACS-ADD-HYPOTHESIS` — إضافة فرضية إلى حالة التحليل (أمر)
  - `US-BC03-ACS-DESELECT-EVIDENCE` — استبعاد دليل من حالة التحليل (أمر)
  - `US-BC03-ACS-RETIRE-ASSUMPTION` — سحب افتراض من حالة التحليل (أمر)
  - `US-BC03-ACS-SELECT-EVIDENCE` — اختيار دليل لـحالة التحليل (أمر)
  - `US-BC03-ACS-UPDATE-HYPOTHESIS` — تحديث فرضية في حالة التحليل (أمر)
- **فتح حالة تحليل وإدارتها** `FEAT-ANL-CASE-SETUP`
  - `US-BC03-ACS-CANCEL` — إلغاء حالة التحليل (أمر)
  - `US-BC03-ACS-CLOSE` — إغلاق حالة التحليل (أمر)
  - `US-BC03-ACS-CREATE` — إنشاء حالة التحليل (أمر)
  - `US-BC03-ACS-DEFINE` — تعريف حالة التحليل (أمر)
  - `US-BC03-ACS-OPEN` — فتح حالة التحليل (أمر)
  - `US-BC03-ACS-RECLASSIFY` — إعادة تصنيف حالة التحليل (أمر)
  - `US-BC03-ACS-REOPEN` — إعادة فتح حالة التحليل (أمر)
  - `US-BC03-Q-ACS-GET` — جلب: Case with question, scope, hypotheses, assumptions, visible selections, scenarios (جلب)
  - `US-BC03-Q-ACS-LIST` — جلب: Cases by owner, state, extent (جلب)
- **السيناريوهات ومقارنة النتائج** `FEAT-ANL-SCENARIOS`
  - `US-BC03-ACS-DEFINE-SCENARIO` — تعريف سيناريو ضمن حالة التحليل (أمر)
  - `US-BC03-Q-SCN-COMPARE` — جلب: Side-by-side results of runs per scenario with differing inputs (جلب)
- **إدارة طرق التحليل** `FEAT-ANL-METHODS`
  - `US-BC03-AMT-ACTIVATE` — تفعيل طريقة التحليل (أمر)
  - `US-BC03-AMT-DEPRECATE` — إهمال طريقة التحليل (إيقاف الاستخدام الجديد) (أمر)
  - `US-BC03-AMT-REGISTER` — تسجيل طريقة التحليل (أمر)
  - `US-BC03-AMT-RETIRE` — إحالة طريقة التحليل إلى التقاعد (أمر)
  - `US-BC03-Q-AMT-LIST` — جلب: Methods and versions (جلب)
- **تشغيل التحليل وإعادة إنتاجه** `FEAT-ANL-RUNS`
  - `US-BC03-Q-RUN-ARTIFACT` — جلب: Short-lived download target for a result artifact (جلب)
  - `US-BC03-Q-RUN-GET` — جلب: Run with pins, parameters, steps, status, artifacts, reproduction report (جلب)
  - `US-BC03-RUN-CANCEL` — إلغاء تشغيل التحليل (أمر)
  - `US-BC03-RUN-REPRODUCE` — إعادة إنتاج تشغيل التحليل (أمر)
  - `US-BC03-RUN-SUBMIT` — تقديم تشغيل التحليل (أمر)
  - `US-BC03-S-ANALYSIS-RUN-01` — تلقائي: worker lease acquired (تشغيل التحليل) (نظام)
  - `US-BC03-S-ANALYSIS-RUN-02` — تلقائي: completed (تشغيل التحليل) (نظام)
  - `US-BC03-S-ANALYSIS-RUN-03` — تلقائي: error or timeout (تشغيل التحليل) (نظام)
- **إعداد التقييم** `FEAT-ANL-ASSESSMENT-DRAFT`
  - `US-BC03-ASM-DISCARD` — تجاهل مسودة التقييم (أمر)
  - `US-BC03-ASM-DRAFT` — إعداد مسودة التقييم (أمر)
  - `US-BC03-ASM-EDIT` — تعديل التقييم (أمر)
  - `US-BC03-ASM-SUBMIT` — تقديم التقييم (أمر)
- **الاطلاع على التقييمات ونسخها** `FEAT-ANL-ASSESSMENT-READ`
  - `US-BC03-Q-ASM-GET` — جلب: Assessment version (default: current PUBLISHED; or version / known_at) (جلب)
  - `US-BC03-Q-ASM-VERSIONS` — جلب: Version history with states and times (جلب)
- **مراجعة التقييم ونشره** `FEAT-ANL-ASSESSMENT-REVIEW`
  - `US-BC03-ASM-PUBLISH` — نشر التقييم (أمر)
  - `US-BC03-ASM-RETURN` — إعادة التقييم للمراجعة (أمر)
  - `US-BC03-ASM-WITHDRAW` — سحب التقييم (أمر)
  - `US-BC03-S-ASSESSMENT-01` — تلقائي: newer version published (التقييم) (نظام)
- **النتائج التحليلية** `FEAT-ANL-FINDINGS`
  - `US-BC03-FND-ACCEPT` — قبول النتيجة التحليلية (أمر)
  - `US-BC03-FND-EDIT` — تعديل النتيجة التحليلية (أمر)
  - `US-BC03-FND-RECORD` — تسجيل النتيجة التحليلية (أمر)
  - `US-BC03-FND-WITHDRAW` — سحب النتيجة التحليلية (أمر)
  - `US-BC03-Q-FND-LIST` — جلب: Findings with sources (جلب)
- **مراجعة مقترحات الربط** `FEAT-ANL-CORRELATION-REVIEW`
  - `US-BC02-CRP-ACCEPT` — قبول مقترح الربط (أمر)
  - `US-BC02-CRP-PROPOSE` — اقتراح مقترح الربط (أمر)
  - `US-BC02-CRP-REJECT` — رفض مقترح الربط (أمر)
  - `US-BC02-CRP-START-REVIEW` — بدء مراجعة مقترح الربط (أمر)
  - `US-BC02-Q-CRP-GET` — جلب: Proposal with inputs, sources, reliabilities, score breakdown (جلب)
  - `US-BC02-Q-CRP-QUEUE` — جلب: Proposals by kind, state, area, score (inputs all visible to caller) (جلب)
  - `US-BC02-S-CORRELATION-PROPOSAL-01` — تلقائي: correlation rule score ≥ threshold (مقترح الربط) (نظام)
  - `US-BC02-S-CORRELATION-PROPOSAL-02` — تلقائي: not reviewed within 30 days (مقترح الربط) (نظام)
- **قواعد الربط الآلي** `FEAT-ANL-CORRELATION-RULES`
  - `US-BC02-CRR-ACTIVATE` — تفعيل قاعدة الربط (أمر)
  - `US-BC02-CRR-DEFINE` — تعريف قاعدة الربط (أمر)
  - `US-BC02-CRR-EDIT` — تعديل قاعدة الربط (أمر)
  - `US-BC02-CRR-RETIRE` — إحالة قاعدة الربط إلى التقاعد (أمر)

</details>

### 2.5 CAP-05 — الوعي بالموقف

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **إنشاء المواقف وإدارتها** `FEAT-SIT-MANAGE` | CAP-05.01 تعريف الموقف (R1) | يحدد المدير أو المحلل الموقف بمنطقته وفترته ومعاييره ويتحكم في تفعيله وإيقافه وإغلاقه. | المحلل؛ المدير؛ مسؤول الأمن؛ كل مستخدم مخوَّل | 9 + 4 |
| **قواعد التنبيه** `FEAT-SIT-ALERT-RULES` | CAP-05.02 المراقبة والتنبيه (R1) | يحدد قائد المحللين أو المدير متى يجب إطلاق تنبيه ولمن ويفعّل القاعدة أو يعطّلها. | قائد المحللين؛ المدير | 6 + 2 |
| **متابعة تغيرات الموقف** `FEAT-SIT-CHANGES` | CAP-05.02 المراقبة والتنبيه (R1) | يعرف المتابع ما دخل الموقف وما خرج منه أولًا بأول دون أن يراجع كل شيء يدويًا. | المحلل؛ المدير؛ النظام | 1 + 4 |
| **تنبيهاتي** `FEAT-SIT-MY-ALERTS` | CAP-05.02 المراقبة والتنبيه (R1) | يصل المستخدم تنبيه فوري حين يقع ما يهمه فيقرّ به أو يحله أو يصرفه بسبب ويُصعَّد إن أهمله. | مستلم التنبيه؛ النظام | 8 + 5 |
| **الصورة العملياتية المشتركة** `FEAT-SIT-COP` | CAP-05.03 صورة العمليات المشتركة (الخرائط) (R1) | يرى كل مخوَّل الموقف على خريطة واحدة تجمع الكيانات والأحداث والمهام والتنبيهات بحسب صلاحيته. | كل مستخدم مخوَّل؛ المستخدم الميداني | 3 + 8 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-05 (27)</summary>

- **إنشاء المواقف وإدارتها** `FEAT-SIT-MANAGE`
  - `US-BC03-Q-SIT-GET` — جلب: Definition (version at valid_at), counts of visible members by type (جلب)
  - `US-BC03-Q-SIT-LIST` — جلب: Situations by state, owner, extent intersecting bbox (جلب)
  - `US-BC03-SIT-ACTIVATE` — تفعيل الموقف (أمر)
  - `US-BC03-SIT-CLOSE` — إغلاق الموقف (أمر)
  - `US-BC03-SIT-CREATE` — إنشاء الموقف (أمر)
  - `US-BC03-SIT-EDIT-DEFINITION` — تعديل تعريف الموقف (أمر)
  - `US-BC03-SIT-PAUSE` — إيقاف الموقف مؤقتًا (أمر)
  - `US-BC03-SIT-RECLASSIFY` — إعادة تصنيف الموقف (أمر)
  - `US-BC03-SIT-RESUME` — استئناف الموقف (أمر)
- **قواعد التنبيه** `FEAT-SIT-ALERT-RULES`
  - `US-BC03-ARL-ACTIVATE` — تفعيل قاعدة التنبيه (أمر)
  - `US-BC03-ARL-DEFINE` — تعريف قاعدة التنبيه (أمر)
  - `US-BC03-ARL-DISABLE` — تعطيل قاعدة التنبيه (أمر)
  - `US-BC03-ARL-EDIT` — تعديل قاعدة التنبيه (أمر)
  - `US-BC03-ARL-ENABLE` — تمكين قاعدة التنبيه (أمر)
  - `US-BC03-ARL-RETIRE` — إحالة قاعدة التنبيه إلى التقاعد (أمر)
- **متابعة تغيرات الموقف** `FEAT-SIT-CHANGES`
  - `US-BC03-Q-SIT-CHANGES` — جلب: Membership change log (visible members only) since cursor/time (جلب)
- **تنبيهاتي** `FEAT-SIT-MY-ALERTS`
  - `US-BC03-ALR-ACKNOWLEDGE` — الإقرار باستلام التنبيه (أمر)
  - `US-BC03-ALR-DISMISS` — صرف النظر عن التنبيه (أمر)
  - `US-BC03-ALR-RESOLVE` — حل التنبيه (أمر)
  - `US-BC03-Q-ALR-LIST` — جلب: My alerts by state, severity, situation (جلب)
  - `US-BC03-S-ALERT-01` — تلقائي: rule condition met (التنبيه) (نظام)
  - `US-BC03-S-ALERT-02` — تلقائي: condition met again within dedupe window (التنبيه) (نظام)
  - `US-BC03-S-ALERT-03` — تلقائي: unacknowledged beyond escalation delay (التنبيه) (نظام)
  - `US-BC03-S-ALERT-04` — تلقائي: condition cleared and rule auto_resolve (التنبيه) (نظام)
- **الصورة العملياتية المشتركة** `FEAT-SIT-COP`
  - `US-BC03-Q-BASE-TILE` — جلب: Base-map tile (layers marked unclassified only; shared cache) (جلب)
  - `US-BC03-Q-SIT-COP` — جلب: Common operational picture: visible members (entities, events, observations, tasks, assessments, alerts) with resolved, possibly generalized geometry (جلب)
  - `US-BC03-Q-SIT-TILE` — جلب: Vector tile of operational layer for the caller's security scope (جلب)

</details>

### 2.6 CAP-06 — إدارة القرار

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **إعداد طلب القرار** `FEAT-DEC-REQUESTS` | CAP-06.01 طلبات القرار والخيارات (R1) | يعرض المحلل أو المخطط على صاحب السلطة سؤالًا واضحًا بخيارات مدعومة بالتقييمات وموعد نهائي. | المحلل؛ المخطط؛ المدير؛ النظام | 7 + 3 |
| **قرارات تنتظرني** `FEAT-DEC-MY-PENDING` | CAP-06.02 تسجيل القرار والتحقق من السلطة (R1) | يرى صاحب السلطة الطلبات التي تنتظر قراره مرتبة بالموعد، ويسجل قراره بعد التحقق من أنه يملك السلطة. | صاحب السلطة؛ النظام | 3 + 4 |
| **سجل القرار وأساسه** `FEAT-DEC-RECORD-BASIS` | CAP-06.02 تسجيل القرار والتحقق من السلطة (R1) | يعرف المدير والمدقق ما الذي قُرر ولماذا وما كان معروفًا وقت القرار، ويُبطل صاحب السلطة الأعلى القرار عند الحاجة. | المدير؛ المدقق؛ السلطة الأعلى؛ النظام | 4 + 5 |
| **المشاركة في التنسيق** `FEAT-DEC-COORD-PARTICIPATE` | CAP-06.03 التنسيق (R2) | ترى الجهة المشاركة ما يخصها من حالة التنسيق، وتحدّث مسؤولياتها، وتطلب قرارًا من سلطة جهة أخرى. | الجهات المشاركة؛ مدير الجهة القائدة؛ النظام | 5 + 4 |
| **إدارة حالة التنسيق** `FEAT-DEC-COORDINATION` | CAP-06.03 التنسيق (R2) | يجمع مدير الجهة القائدة الجهات التي يجب أن تعمل معًا، ويوزع المسؤوليات بينها ويتابع الحالة حتى إغلاقها. | مدير الجهة القائدة | 7 + 3 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-06 (26)</summary>

- **إعداد طلب القرار** `FEAT-DEC-REQUESTS`
  - `US-BC04-DRQ-ADD-OPTION` — إضافة خيار إلى طلب القرار (أمر)
  - `US-BC04-DRQ-CITE` — الاستشهاد في طلب القرار (أمر)
  - `US-BC04-DRQ-CREATE` — إنشاء طلب القرار (أمر)
  - `US-BC04-DRQ-OPEN` — فتح طلب القرار (أمر)
  - `US-BC04-DRQ-WITHDRAW` — سحب طلب القرار (أمر)
  - `US-BC04-Q-DRQ-GET` — جلب: Request with options and pinned citations (withheld per policy) (جلب)
  - `US-BC04-S-DECISION-REQUEST-01` — تلقائي: deadline passed (طلب القرار) (نظام)
- **قرارات تنتظرني** `FEAT-DEC-MY-PENDING`
  - `US-BC04-DEC-RECORD` — تسجيل القرار (أمر)
  - `US-BC04-Q-DRQ-LIST` — جلب: My pending requests (as authority holder), by deadline (جلب)
  - `US-BC04-S-DECISION-REQUEST-02` — تلقائي: decision recorded for this request (طلب القرار) (نظام)
- **سجل القرار وأساسه** `FEAT-DEC-RECORD-BASIS`
  - `US-BC04-DEC-ANNUL` — إبطال القرار (أمر)
  - `US-BC04-Q-DEC-BASIS` — جلب: What was known at decision time: cited assessments (pinned versions) and their key claims resolved known_at = decision.recorded_at (جلب)
  - `US-BC04-Q-DEC-GET` — جلب: Decision with authority snapshot, citations (pinned) and supersession chain (جلب)
  - `US-BC04-S-DECISION-01` — تلقائي: superseding decision recorded (القرار) (نظام)
- **المشاركة في التنسيق** `FEAT-DEC-COORD-PARTICIPATE`
  - `US-BC04-CRD-REQUEST-DECISION` — طلب قرار ضمن حالة التنسيق (أمر)
  - `US-BC04-CRD-UPDATE-RESPONSIBILITY` — تحديث مسؤولية ضمن حالة التنسيق (أمر)
  - `US-BC04-Q-CRD-GET` — جلب: Case filtered to the caller's participant scope (جلب)
  - `US-BC04-Q-CRD-LIST` — جلب: Cases where the caller's unit participates (جلب)
  - `US-BC04-S-COORDINATION-CASE-01` — تلقائي: linked decision recorded (حالة التنسيق) (نظام)
- **إدارة حالة التنسيق** `FEAT-DEC-COORDINATION`
  - `US-BC04-CRD-ACTIVATE` — تفعيل حالة التنسيق (أمر)
  - `US-BC04-CRD-ADD-PARTICIPANT` — إضافة مشارك إلى حالة التنسيق (أمر)
  - `US-BC04-CRD-ASSIGN-RESPONSIBILITY` — إسناد مسؤولية ضمن حالة التنسيق (أمر)
  - `US-BC04-CRD-CANCEL` — إلغاء حالة التنسيق (أمر)
  - `US-BC04-CRD-CLOSE` — إغلاق حالة التنسيق (أمر)
  - `US-BC04-CRD-OPEN` — فتح حالة التنسيق (أمر)
  - `US-BC04-CRD-REMOVE-PARTICIPANT` — إزالة مشارك من حالة التنسيق (أمر)

</details>

### 2.7 CAP-07 — التخطيط والتنفيذ

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **إعداد الخطة** `FEAT-OPS-PLAN-AUTHORING` | CAP-07.01 الأهداف والتخطيط (R1) | يصوغ المخطط خطة بأهدافها ومراحلها وأنشطتها ومواردها وجدولها، ثم يقدمها للاعتماد. | المخطط؛ مالك الخطة | 6 + 4 |
| **إدارة حالة الخطة** `FEAT-OPS-PLAN-LIFECYCLE` | CAP-07.01 الأهداف والتخطيط (R1) | يعلّق المخطط الخطة أو يستأنفها أو يكملها أو يغلقها، ويُنبَّه إن أُبطل قرار تقوم عليه. | المخطط؛ مالك الخطة؛ صاحب السلطة؛ مسؤول الأمن؛ النظام | 7 + 2 |
| **اعتماد الخطة** `FEAT-OPS-PLAN-APPROVAL` | CAP-07.02 إصدارات الخطة وخط الأساس (R1) | يعتمد صاحب الصلاحية — غير كاتب الخطة — نسخة الخطة فتصبح خط أساس ثابتًا، أو يعيدها أو يرفضها. | معتمد الخطة؛ النظام | 5 + 4 |
| **تعديل الخطة المعتمدة ونسخها** `FEAT-OPS-PLAN-VERSIONS` | CAP-07.02 إصدارات الخطة وخط الأساس (R1) | يعدّل المخطط خطة معتمدة تعديلًا طفيفًا أو يرى الفرق عن خط الأساس وأثره على المهام قبل اعتماد نسخة جديدة. | المخطط؛ المدير | 3 + 3 |
| **مهامي** `FEAT-OPS-MY-TASKS` | CAP-07.03 إدارة المهام (R1) | المستخدم الميداني ينفّذ عمله من قائمة واحدة، حتى 72 ساعة دون شبكة، ولا يضيع ما سجّله. | المُسند إليه؛ المستخدم الميداني؛ النظام | 11 + 7 |
| **متابعة المهام والتدخل** `FEAT-OPS-TASK-CONTROL` | CAP-07.03 إدارة المهام (R1) | يتدخل المخطط أو المدير في مهام جارية فيعلّقها أو يلغيها أو يصعّدها، ويغلق النظام المهام المنتهية أو المتجاوزة آليًا. | المخطط؛ المدير؛ مالك المهمة؛ المُسند إليه؛ النظام | 8 + 4 |
| **تخطيط المهام وإسنادها** `FEAT-OPS-TASK-PLANNING` | CAP-07.03 إدارة المهام (R1) | ينشئ المخطط المهام ويحدد مواعيدها ويسندها لمن هو مؤهل لها، ويعيد إسنادها عند الحاجة. | المخطط؛ المدير | 7 + 5 |
| **مراجعة نتيجة المهمة** `FEAT-OPS-TASK-REVIEW` | CAP-07.03 إدارة المهام (R1) | يراجع المراجع — غير منفّذ المهمة — نتيجتها فيعتمدها أو يعيدها أو يرفضها، ولا تكتمل إلا باستيفاء معاييرها. | المراجع؛ صاحب دور الإقرار؛ النظام | 6 + 3 |
| **أنواع المهام وخطوات اعتمادها** `FEAT-OPS-TASK-TYPES` | CAP-07.04 سير العمل (R1) | يحدد المسؤول لكل نوع مهمة متطلبات الأهلية ومعايير الإكمال وخطوات المراجعة والاعتماد الخاصة بالجهة. | المسؤول؛ قائد المخططين؛ المستخدم | 5 + 3 |
| **متابعة تنفيذ الخطة** `FEAT-OPS-EXEC-TRACKING` | CAP-07.05 قياس النتائج (R1) | يرى المدير والتنفيذي تقدم الخطة: المهام حسب حالتها، والمعالم، والنتائج مقابل المستهدف. | المدير؛ المخطط؛ التنفيذي | 1 + 5 |
| **قياس النتائج** `FEAT-OPS-OUTCOMES` | CAP-07.05 قياس النتائج (R1) | يسجل المخطط قياسات النتائج مقابل أهدافها ويصححها، فتبقى سلسلة القياس صادقة حتى بعد تغيير الخطة. | المخطط؛ مالك الخطة؛ النظام | 6 + 3 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-07 (65)</summary>

- **إعداد الخطة** `FEAT-OPS-PLAN-AUTHORING`
  - `US-BC04-PLN-CREATE` — إنشاء الخطة (أمر)
  - `US-BC04-PLV-DISCARD` — تجاهل مسودة إصدار الخطة (أمر)
  - `US-BC04-PLV-DRAFT` — إعداد مسودة إصدار الخطة (أمر)
  - `US-BC04-PLV-EDIT` — تعديل إصدار الخطة (أمر)
  - `US-BC04-PLV-SUBMIT` — تقديم إصدار الخطة (أمر)
  - `US-BC04-Q-PLN-GET` — جلب: Plan with current baseline, draft (if any), implemented decisions (جلب)
- **إدارة حالة الخطة** `FEAT-OPS-PLAN-LIFECYCLE`
  - `US-BC04-PLN-CANCEL` — إلغاء الخطة (أمر)
  - `US-BC04-PLN-CLOSE` — إغلاق الخطة (أمر)
  - `US-BC04-PLN-COMPLETE` — إكمال الخطة (أمر)
  - `US-BC04-PLN-RECLASSIFY` — إعادة تصنيف الخطة (أمر)
  - `US-BC04-PLN-RESUME` — استئناف الخطة (أمر)
  - `US-BC04-PLN-SUSPEND` — تعليق الخطة (أمر)
  - `US-BC04-S-PLAN-02` — تلقائي: implemented decision annulled or superseded (الخطة) (نظام)
- **اعتماد الخطة** `FEAT-OPS-PLAN-APPROVAL`
  - `US-BC04-PLV-APPROVE` — اعتماد إصدار الخطة (أمر)
  - `US-BC04-PLV-REJECT` — رفض إصدار الخطة (أمر)
  - `US-BC04-PLV-RETURN` — إعادة إصدار الخطة للمراجعة (أمر)
  - `US-BC04-S-PLAN-01` — تلقائي: first version baselined (الخطة) (نظام)
  - `US-BC04-S-PLAN-VERSION-01` — تلقائي: newer version baselined (إصدار الخطة) (نظام)
- **تعديل الخطة المعتمدة ونسخها** `FEAT-OPS-PLAN-VERSIONS`
  - `US-BC04-PLV-AMEND-MINOR` — تعديل طفيف على إصدار الخطة (أمر)
  - `US-BC04-Q-PLV-DIFF` — جلب: Diff vs baseline with major/minor classification and task synchronization preview (جلب)
  - `US-BC04-Q-PLV-LIST` — جلب: Versions with states and times (جلب)
- **مهامي** `FEAT-OPS-MY-TASKS`
  - `US-BC04-Q-TASK-GET` — جلب: Task with criteria status, result, eligibility snapshot, dependencies (جلب)
  - `US-BC04-Q-TASK-HISTORY` — جلب: State history; state as of t (RECONSTRUCTED) (جلب)
  - `US-BC04-Q-TASK-LIST` — جلب: Tasks by assignee (me), plan, state, due_before, unit (جلب)
  - `US-BC04-S-TASK-05` — تلقائي: due passed (escalation policy) (المهمة) (نظام)
  - `US-BC04-TASK-ACCEPT` — قبول المهمة (أمر)
  - `US-BC04-TASK-ADD-RESULT-ITEM` — إضافة بند نتيجة إلى المهمة (أمر)
  - `US-BC04-TASK-BLOCK` — تعليق المهمة كمحجوب (أمر)
  - `US-BC04-TASK-DECLINE` — رفض قبول المهمة (أمر)
  - `US-BC04-TASK-RESUME` — استئناف المهمة (أمر)
  - `US-BC04-TASK-START` — بدء المهمة (أمر)
  - `US-BC04-TASK-SUBMIT` — تقديم المهمة (أمر)
- **متابعة المهام والتدخل** `FEAT-OPS-TASK-CONTROL`
  - `US-BC04-S-TASK-02` — تلقائي: follow-up window (7 d) elapsed without open follow-ups (المهمة) (نظام)
  - `US-BC04-S-TASK-03` — تلقائي: due passed and task type expires_on_due (المهمة) (نظام)
  - `US-BC04-S-TASK-04` — تلقائي: plan version baselined without this task (المهمة) (نظام)
  - `US-BC04-TASK-CANCEL` — إلغاء المهمة (أمر)
  - `US-BC04-TASK-CLOSE` — إغلاق المهمة (أمر)
  - `US-BC04-TASK-ESCALATE` — تصعيد المهمة (أمر)
  - `US-BC04-TASK-SUSPEND` — تعليق المهمة (أمر)
  - `US-BC04-TASK-UNSUSPEND` — رفع تعليق المهمة (أمر)
- **تخطيط المهام وإسنادها** `FEAT-OPS-TASK-PLANNING`
  - `US-BC04-TASK-ASSIGN` — إسناد المهمة (أمر)
  - `US-BC04-TASK-CREATE` — إنشاء المهمة (أمر)
  - `US-BC04-TASK-EDIT` — تعديل المهمة (أمر)
  - `US-BC04-TASK-MARK-READY` — تعليم المهمة كجاهز (أمر)
  - `US-BC04-TASK-REASSIGN` — إعادة إسناد المهمة (أمر)
  - `US-BC04-TASK-RECLASSIFY` — إعادة تصنيف المهمة (أمر)
  - `US-BC04-TASK-SET-DUE` — تحديد موعد استحقاق المهمة (أمر)
- **مراجعة نتيجة المهمة** `FEAT-OPS-TASK-REVIEW`
  - `US-BC04-S-TASK-01` — تلقائي: all completion criteria satisfied (المهمة) (نظام)
  - `US-BC04-TASK-APPROVE` — اعتماد المهمة (أمر)
  - `US-BC04-TASK-COMPLETE` — إكمال المهمة (أمر)
  - `US-BC04-TASK-REJECT` — رفض المهمة (أمر)
  - `US-BC04-TASK-RETURN` — إعادة المهمة للمراجعة (أمر)
  - `US-BC04-TASK-START-REVIEW` — بدء مراجعة المهمة (أمر)
- **أنواع المهام وخطوات اعتمادها** `FEAT-OPS-TASK-TYPES`
  - `US-BC04-Q-TTY-GET` — جلب: Task type version (جلب)
  - `US-BC04-TTY-ACTIVATE` — تفعيل نوع المهمة (أمر)
  - `US-BC04-TTY-DEFINE` — تعريف نوع المهمة (أمر)
  - `US-BC04-TTY-EDIT` — تعديل نوع المهمة (أمر)
  - `US-BC04-TTY-RETIRE` — إحالة نوع المهمة إلى التقاعد (أمر)
- **متابعة تنفيذ الخطة** `FEAT-OPS-EXEC-TRACKING`
  - `US-BC04-Q-PLN-PROGRESS` — جلب: Tasks by activity and state, milestones, outcome progress vs targets (جلب)
- **قياس النتائج** `FEAT-OPS-OUTCOMES`
  - `US-BC04-OUT-CORRECT` — تصحيح متتبّع النتائج (أمر)
  - `US-BC04-OUT-RECORD` — تسجيل متتبّع النتائج (أمر)
  - `US-BC04-Q-OUT-SERIES` — جلب: Measurement series as known_at (جلب)
  - `US-BC04-S-OUTCOME-TRACKER-01` — تلقائي: outcome baselined (متتبّع النتائج) (نظام)
  - `US-BC04-S-OUTCOME-TRACKER-02` — تلقائي: target changed by new baseline (متتبّع النتائج) (نظام)
  - `US-BC04-S-OUTCOME-TRACKER-03` — تلقائي: plan closed or cancelled (متتبّع النتائج) (نظام)

</details>

### 2.8 CAP-08 — الموارد والجاهزية

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **حجز الأصول وتوفرها** `FEAT-RES-ASSET-BOOKING` | CAP-08.01 إدارة الأصول (R2) | يرى المخطط الأصول المتاحة في نافذة زمنية ويحجزها مسبقًا دون تعارض مع حجوزات أخرى. | المخطط؛ مدير الموارد؛ النظام | 7 + 3 |
| **إسناد الأصول وعهدتها** `FEAT-RES-ASSET-CUSTODY` | CAP-08.01 إدارة الأصول (R2) | يعرف الجميع من يحمل الأصل الآن ولأي مهمة أُسند، مع سلسلة عهدة متصلة بلا فجوات. | مدير الموارد؛ المخطط؛ النظام | 5 + 3 |
| **صيانة الأصول** `FEAT-RES-ASSET-MAINTENANCE` | CAP-08.01 إدارة الأصول (R2) | يخطط مدير الموارد والفني لصيانة الأصول ويتابعونها حتى تعود جاهزة، فلا يُحجز أصل وهو قيد الصيانة. | مدير الموارد؛ الفني | 8 + 3 |
| **سجل الأصول** `FEAT-RES-ASSET-REGISTRY` | CAP-08.01 إدارة الأصول (R2) | يعرف مدير الموارد كل أصل ونوعه وحالته الفنية وشهاداته وتصنيفه الأمني حتى نهاية عمره والتخلص منه. | مدير الموارد؛ مسؤول الأمن؛ سلطة التخلص | 6 + 6 |
| **صلاحية الأصل وفقده** `FEAT-RES-ASSET-SERVICE` | CAP-08.01 إدارة الأصول (R2) | يمنع استخدام أصل معطّل أو مفقود في أي إسناد جديد ويعيده للخدمة عند إصلاحه أو استعادته. | مدير الموارد | 4 + 2 |
| **اعتماد التخصيص وأولويته** `FEAT-RES-ALLOCATION-APPROVAL` | CAP-08.02 تخصيص الموارد (R2) | تعتمد سلطة التخصيص الطلبات التي تحتاج موافقة وتحسم التنافس بإعطاء الأولوية للأهم مع إشعار المتأثرين. | سلطة التخصيص؛ النظام | 4 + 3 |
| **طلب تخصيص الموارد** `FEAT-RES-ALLOCATION-REQUEST` | CAP-08.02 تخصيص الموارد (R2) | يطلب المخطط كمية من الموارد لمهمة أو خطة، فيتحقق النظام من التوفر والسعة والسياسة ويلتزم بها أو يبين سبب الرفض. | المخطط؛ النظام | 5 + 3 |
| **استهلاك الموارد وتحريرها** `FEAT-RES-CONSUMPTION` | CAP-08.02 تخصيص الموارد (R2) | يسجل منفذ المهمة ما استهلكه فعلًا، ويُعاد غير المستخدم إلى المجمع عند انتهاء المهمة. | المُسند إليه المهمة؛ المخطط؛ النظام | 3 + 2 |
| **إدارة مجمعات الموارد** `FEAT-RES-RESOURCE-POOLS` | CAP-08.02 تخصيص الموارد (R2) | يدير مدير الموارد مخزون كل نوع من الموارد وسعته ويرى المتاح والملتزم به ساعة بساعة. | مدير الموارد؛ المخطط | 6 + 3 |
| **استلام الشحنات والخسائر** `FEAT-RES-SHIPMENT-RECEIPT` | CAP-08.03 الإمداد (R3) | تسجل الجهة المستلمة ما وصل فعلًا أو ما تلف أو فُقد، فيُغلق طلب الإمداد كاملًا أو جزئيًا بدقة. | الجهة المستلمة؛ مشغل الناقل؛ مسؤول الإرسال؛ النظام | 5 + 2 |
| **إرسال الشحنات وتتبعها** `FEAT-RES-SHIPMENT-TRACKING` | CAP-08.03 الإمداد (R3) | يرسل مسؤول الإرسال الشحنة ويتابع الجميع مسارها نقطة بنقطة حتى وصولها. | مسؤول الإرسال؛ مشغل الناقل | 8 + 5 |
| **طلب الإمداد** `FEAT-RES-SUPPLY-REQUEST` | CAP-08.03 الإمداد (R3) | يطلب ضابط الإمداد أو المخطط كمية من صنف إلى وجهة ويتابع موافقتها أو رفضها حتى تصبح جاهزة للإرسال. | ضابط الإمداد؛ المخطط؛ النظام | 9 + 3 |
| **التحقق من الأهلية والجاهزية** `FEAT-RES-ELIGIBILITY` | CAP-08.04 الكفاءة والأهلية (R1 (الأهلية فقط)) | يعرف المخطط ومدير الموارد فورًا هل الشخص أو الوحدة مؤهل لدور أو مهمة في وقت معين، ولماذا. | المخطط؛ مدير الموارد؛ مدير التدريب | 2 + 3 |
| **سجلات تأهيل الأفراد** `FEAT-RES-QUALIFICATIONS` | CAP-08.04 الكفاءة والأهلية (R1 (الأهلية فقط)) | يحفظ مدير الموارد أو مدير التدريب مؤهلات كل فرد وشهاداته وصلاحيتها، وتنتهي تلقائيًا عند انقضاء مدتها. | مدير الموارد؛ مدير التدريب؛ المدير؛ الفرد نفسه؛ النظام | 7 + 4 |
| **متطلبات الأدوار** `FEAT-RES-ROLE-REQUIREMENTS` | CAP-08.04 الكفاءة والأهلية (R1 (الأهلية فقط)) | يحدد مدير التدريب ما يلزم كل دور من مؤهلات وخبرات، ليُبنى عليه الحكم بالأهلية. | مدير التدريب؛ المسؤول | 4 + 1 |
| **إدارة تنفيذ التمرين** `FEAT-RES-EXERCISE-CONDUCT` | CAP-08.05 التدريب والتمارين (R3) | يدير مراقب التمرين سير التمرين الحي، فيرسل الأحداث ويوقف ويستأنف وينهي، وتُسجل النتيجة النهائية للتمرين تلقائيًا. | مراقب التمرين؛ النظام | 10 + 4 |
| **تقييم المشاركين ونتائج التمرين** `FEAT-RES-EXERCISE-EVALUATION` | CAP-08.05 التدريب والتمارين (R3) | يقيّم المقيّم أداء كل مشارك في كل كفاءة، وتُستخدم النتائج دليلًا على التأهيل ودروسًا مستفادة. | المقيّم؛ مدير التدريب | 2 + 2 |
| **تخطيط التمارين وجدولتها** `FEAT-RES-EXERCISE-PLANNING` | CAP-08.05 التدريب والتمارين (R3) | يخطط مدير التمرين للتمرين ويحدد موعده ومكانه ومشاركيه ثم يطلقه في وقته. | مدير التمرين؛ مدير التدريب | 6 + 2 |
| **سيناريوهات التدريب** `FEAT-RES-TRAINING-SCENARIOS` | CAP-08.05 التدريب والتمارين (R3) | يُعد مدير التدريب سيناريوهات تدريب بأحداثها والكفاءات المستهدفة، ويعتمدها مدير التمرين قبل استخدامها. | مدير التدريب؛ مدير التمرين | 6 + 2 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-08 (107)</summary>

- **حجز الأصول وتوفرها** `FEAT-RES-ASSET-BOOKING`
  - `US-BC05-Q-AST-AVAILABILITY` — جلب: Assets of type/capability available in a window (and optional bbox), with blocking reasons for others visible to caller (جلب)
  - `US-BC05-RSV-CANCEL` — إلغاء حجز الأصل (أمر)
  - `US-BC05-RSV-CONFIRM` — تأكيد حجز الأصل (أمر)
  - `US-BC05-RSV-HOLD` — إنشاء حجز الأصل مبدئيًا (أمر)
  - `US-BC05-RSV-RELEASE` — تحرير حجز الأصل (أمر)
  - `US-BC05-S-ASSET-RESERVATION-01` — تلقائي: hold expiry (24 h) reached (حجز الأصل) (نظام)
  - `US-BC05-S-ASSET-RESERVATION-02` — تلقائي: linked task or plan terminal (حجز الأصل) (نظام)
- **إسناد الأصول وعهدتها** `FEAT-RES-ASSET-CUSTODY`
  - `US-BC05-ASG-ASSIGN` — تسجيل إسناد الأصل (أمر)
  - `US-BC05-ASG-CANCEL` — إلغاء إسناد الأصل (أمر)
  - `US-BC05-ASG-RETURN` — إرجاع الأصل وإنهاء إسناد الأصل (أمر)
  - `US-BC05-AST-TRANSFER-CUSTODY` — نقل عهدة الأصل (أمر)
  - `US-BC05-S-ASSET-ASSIGNMENT-01` — تلقائي: linked task terminal (إسناد الأصل) (نظام)
- **صيانة الأصول** `FEAT-RES-ASSET-MAINTENANCE`
  - `US-BC05-AST-FAIL-MAINTENANCE` — تسجيل فشل صيانة الأصل (أمر)
  - `US-BC05-AST-START-MAINTENANCE` — بدء صيانة الأصل (أمر)
  - `US-BC05-MNT-CANCEL` — إلغاء أمر الصيانة (أمر)
  - `US-BC05-MNT-COMPLETE` — إكمال أمر الصيانة (أمر)
  - `US-BC05-MNT-PLAN` — تخطيط أمر الصيانة (أمر)
  - `US-BC05-MNT-RESCHEDULE` — إعادة جدولة أمر الصيانة (أمر)
  - `US-BC05-MNT-START` — بدء أمر الصيانة (أمر)
  - `US-BC05-Q-MNT-SCHEDULE` — جلب: Maintenance orders by asset, window, state (جلب)
- **سجل الأصول** `FEAT-RES-ASSET-REGISTRY`
  - `US-BC05-AST-DISPOSE` — التخلص من الأصل (أمر)
  - `US-BC05-AST-RECLASSIFY` — إعادة تصنيف الأصل (أمر)
  - `US-BC05-AST-REGISTER` — تسجيل الأصل (أمر)
  - `US-BC05-AST-SET-CERTIFICATION` — تحديد شهادة الأصل (أمر)
  - `US-BC05-AST-UPDATE-CONDITION` — تحديث حالة الأصل الفنية (أمر)
  - `US-BC05-Q-AST-GET` — جلب: Asset with status, condition, certifications, custody chain, linked entity (جلب)
- **صلاحية الأصل وفقده** `FEAT-RES-ASSET-SERVICE`
  - `US-BC05-AST-MARK-UNSERVICEABLE` — تعليم الأصل كغير صالح للخدمة (أمر)
  - `US-BC05-AST-RECOVER` — استعادة الأصل (أمر)
  - `US-BC05-AST-REPORT-LOST` — الإبلاغ عن فقد الأصل (أمر)
  - `US-BC05-AST-RETURN-TO-SERVICE` — إعادة الأصل إلى الخدمة (أمر)
- **اعتماد التخصيص وأولويته** `FEAT-RES-ALLOCATION-APPROVAL`
  - `US-BC05-ALC-APPROVE` — اعتماد تخصيص الموارد (أمر)
  - `US-BC05-ALC-PREEMPT` — استباق تخصيص الموارد بأولوية أعلى (أمر)
  - `US-BC05-ALC-REJECT` — رفض تخصيص الموارد (أمر)
  - `US-BC05-S-ALLOCATION-02` — تلقائي: checks passed, policy requires approval (تخصيص الموارد) (نظام)
- **طلب تخصيص الموارد** `FEAT-RES-ALLOCATION-REQUEST`
  - `US-BC05-ALC-REQUEST` — طلب تخصيص الموارد (أمر)
  - `US-BC05-Q-ALC-LIST` — جلب: Allocations by pool, task, plan, state (جلب)
  - `US-BC05-S-ALLOCATION-01` — تلقائي: all checks passed (تخصيص الموارد) (نظام)
  - `US-BC05-S-ALLOCATION-03` — تلقائي: a check failed (تخصيص الموارد) (نظام)
  - `US-BC05-S-ALLOCATION-04` — تلقائي: provisional hold (1 h) elapsed (تخصيص الموارد) (نظام)
- **استهلاك الموارد وتحريرها** `FEAT-RES-CONSUMPTION`
  - `US-BC05-ALC-RECORD-CONSUMPTION` — تسجيل استهلاك تخصيص الموارد (أمر)
  - `US-BC05-ALC-RELEASE` — تحرير تخصيص الموارد (أمر)
  - `US-BC05-S-ALLOCATION-05` — تلقائي: linked task terminal (تخصيص الموارد) (نظام)
- **إدارة مجمعات الموارد** `FEAT-RES-RESOURCE-POOLS`
  - `US-BC05-Q-POL-TIMELINE` — جلب: Capacity, committed and available quantity per hour in a window (جلب)
  - `US-BC05-RPL-ADJUST-CAPACITY` — تعديل سعة مجمع الموارد (أمر)
  - `US-BC05-RPL-CLOSE` — إغلاق مجمع الموارد (أمر)
  - `US-BC05-RPL-CREATE` — إنشاء مجمع الموارد (أمر)
  - `US-BC05-RPL-RESUME` — استئناف مجمع الموارد (أمر)
  - `US-BC05-RPL-SUSPEND` — تعليق مجمع الموارد (أمر)
- **استلام الشحنات والخسائر** `FEAT-RES-SHIPMENT-RECEIPT`
  - `US-BC05-S-LOGISTICS-REQUEST-06` — تلقائي: linked shipment delivered in full (طلب الإمداد) (نظام)
  - `US-BC05-S-LOGISTICS-REQUEST-07` — تلقائي: linked shipment resolved short (طلب الإمداد) (نظام)
  - `US-BC05-SHP-DELIVER` — تسليم الشحنة (أمر)
  - `US-BC05-SHP-REPORT-DAMAGE` — الإبلاغ عن تلف الشحنة (أمر)
  - `US-BC05-SHP-REPORT-LOST` — الإبلاغ عن فقد الشحنة (أمر)
- **إرسال الشحنات وتتبعها** `FEAT-RES-SHIPMENT-TRACKING`
  - `US-BC05-LGR-DISPATCH` — إرسال طلب الإمداد (أمر)
  - `US-BC05-Q-SHP-GET` — جلب: Shipment with current state and delivered/damaged/lost quantity (جلب)
  - `US-BC05-Q-SHP-LIST` — جلب: Shipments filtered by logistics request, carrier, state, window (جلب)
  - `US-BC05-Q-SHP-TRACKING` — جلب: Full checkpoint history of a shipment, in order (جلب)
  - `US-BC05-SHP-CANCEL` — إلغاء الشحنة (أمر)
  - `US-BC05-SHP-DEPART` — بدء نقل الشحنة (أمر)
  - `US-BC05-SHP-PLAN` — تخطيط الشحنة (أمر)
  - `US-BC05-SHP-RECORD-CHECKPOINT` — تسجيل نقطة عبور لـالشحنة (أمر)
- **طلب الإمداد** `FEAT-RES-SUPPLY-REQUEST`
  - `US-BC05-LGR-CANCEL` — إلغاء طلب الإمداد (أمر)
  - `US-BC05-LGR-REQUEST` — تقديم طلب الإمداد (أمر)
  - `US-BC05-Q-LGR-GET` — جلب: Logistics request with linked allocation and shipment refs (جلب)
  - `US-BC05-Q-LGR-LIST` — جلب: Logistics requests filtered by item, destination, state, priority (جلب)
  - `US-BC05-S-LOGISTICS-REQUEST-01` — تلقائي: linked allocation committed (طلب الإمداد) (نظام)
  - `US-BC05-S-LOGISTICS-REQUEST-02` — تلقائي: linked allocation requires approval (طلب الإمداد) (نظام)
  - `US-BC05-S-LOGISTICS-REQUEST-03` — تلقائي: linked allocation rejected (طلب الإمداد) (نظام)
  - `US-BC05-S-LOGISTICS-REQUEST-04` — تلقائي: linked allocation committed (طلب الإمداد) (نظام)
  - `US-BC05-S-LOGISTICS-REQUEST-05` — تلقائي: linked allocation rejected (طلب الإمداد) (نظام)
- **التحقق من الأهلية والجاهزية** `FEAT-RES-ELIGIBILITY`
  - `US-BC05-Q-ELIG-CHECK` — جلب: EligibilityCheck(person, task_type version, at) → status + reasons (جلب)
  - `US-BC05-Q-READINESS` — جلب: Readiness of a person or unit for a role at time t, with gaps (جلب)
- **سجلات تأهيل الأفراد** `FEAT-RES-QUALIFICATIONS`
  - `US-BC05-Q-QUAL-LIST` — جلب: Qualification records as of t (جلب)
  - `US-BC05-QUAL-RECORD` — تسجيل سجل التأهيل (أمر)
  - `US-BC05-QUAL-REINSTATE` — إعادة سجل التأهيل إلى السريان (أمر)
  - `US-BC05-QUAL-RENEW` — تجديد سجل التأهيل (أمر)
  - `US-BC05-QUAL-REVOKE` — سحب سجل التأهيل (أمر)
  - `US-BC05-QUAL-SUSPEND` — تعليق سجل التأهيل (أمر)
  - `US-BC05-S-QUALIFICATION-RECORD-01` — تلقائي: valid_to reached (سجل التأهيل) (نظام)
- **متطلبات الأدوار** `FEAT-RES-ROLE-REQUIREMENTS`
  - `US-BC05-RRQ-ACTIVATE` — تفعيل متطلبات الدور (أمر)
  - `US-BC05-RRQ-DEFINE` — تعريف متطلبات الدور (أمر)
  - `US-BC05-RRQ-EDIT` — تعديل متطلبات الدور (أمر)
  - `US-BC05-RRQ-RETIRE` — إحالة متطلبات الدور إلى التقاعد (أمر)
- **إدارة تنفيذ التمرين** `FEAT-RES-EXERCISE-CONDUCT`
  - `US-BC05-Q-SIM-GET` — جلب: Simulation with current state and evaluation summary (جلب)
  - `US-BC05-Q-SIM-LIST` — جلب: Simulations filtered by exercise, state, window (جلب)
  - `US-BC05-S-EXERCISE-01` — تلقائي: linked simulation completed (التمرين) (نظام)
  - `US-BC05-S-EXERCISE-02` — تلقائي: linked simulation aborted (التمرين) (نظام)
  - `US-BC05-SIM-ABORT` — إيقاف تشغيل المحاكاة نهائيًا مع السبب (أمر)
  - `US-BC05-SIM-COMPLETE` — إكمال تشغيل المحاكاة (أمر)
  - `US-BC05-SIM-DELIVER-INJECT` — تسليم حقنة سيناريو ضمن تشغيل المحاكاة (أمر)
  - `US-BC05-SIM-PAUSE` — إيقاف تشغيل المحاكاة مؤقتًا (أمر)
  - `US-BC05-SIM-RESUME` — استئناف تشغيل المحاكاة (أمر)
  - `US-BC05-SIM-START` — بدء تشغيل المحاكاة (نظام)
- **تقييم المشاركين ونتائج التمرين** `FEAT-RES-EXERCISE-EVALUATION`
  - `US-BC05-Q-SIM-TIMELINE` — جلب: Full, ordered timeline of inject deliveries and evaluations for a simulation (جلب)
  - `US-BC05-SIM-RECORD-EVALUATION` — تسجيل تقييم ضمن تشغيل المحاكاة (أمر)
- **تخطيط التمارين وجدولتها** `FEAT-RES-EXERCISE-PLANNING`
  - `US-BC05-EXR-CANCEL` — إلغاء التمرين (أمر)
  - `US-BC05-EXR-PLAN` — تخطيط التمرين (أمر)
  - `US-BC05-EXR-SCHEDULE` — جدولة التمرين (أمر)
  - `US-BC05-EXR-START` — بدء التمرين (أمر)
  - `US-BC05-Q-EXR-GET` — جلب: Exercise with frozen scenario reference, participants, current state (جلب)
  - `US-BC05-Q-EXR-LIST` — جلب: Exercises filtered by scenario, state, window (جلب)
- **سيناريوهات التدريب** `FEAT-RES-TRAINING-SCENARIOS`
  - `US-BC05-Q-SCN-GET` — جلب: Scenario with injects and target competencies (جلب)
  - `US-BC05-Q-SCN-LIST` — جلب: Scenarios filtered by exercise type, state (جلب)
  - `US-BC05-SCN-ACTIVATE` — تفعيل سيناريو التدريب (أمر)
  - `US-BC05-SCN-DEFINE` — تعريف سيناريو التدريب (أمر)
  - `US-BC05-SCN-EDIT` — تعديل سيناريو التدريب (أمر)
  - `US-BC05-SCN-RETIRE` — إحالة سيناريو التدريب إلى التقاعد (أمر)

</details>

### 2.9 CAP-09 — المخاطر والطوارئ

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **سجل المخاطر** `FEAT-RSK-RISK-REGISTER` | CAP-09.01 إدارة المخاطر (R3) | يسجل المستخدم المخوَّل خطرًا محتملًا بنطاقه، ويتصفح سجل المخاطر مصفّى حسب ما يحق له رؤيته. | محدِّد الخطر؛ مدير المخاطر؛ مالك النطاق؛ النظام | 4 + 4 |
| **تقييم المخاطر ومعالجتها** `FEAT-RSK-RISK-TREATMENT` | CAP-09.01 إدارة المخاطر (R3) | يقيّم المقيّم الخطر — غير من سجّله — ويخطط لمعالجته ثم يغلقه بمبرر صريح. | المقيّم؛ موافق المعالجة؛ مدير المخاطر | 4 + 2 |
| **قيادة الاستجابة للحادثة** `FEAT-RSK-INCIDENT-COMMAND` | CAP-09.02 الحوادث والاستجابة (R3) | يوجّه قائد الحادثة الاستجابة ويصعّد الخطورة أو يخفضها حتى الاحتواء والحل والإغلاق، ويُنبَّه إن تأخر التوجيه. | قائد الحادثة؛ النظام | 7 + 6 |
| **الإبلاغ عن الحوادث وتقييمها** `FEAT-RSK-INCIDENT-REPORT` | CAP-09.02 الحوادث والاستجابة (R3) | يبلّغ أي مستخدم مخوَّل عن حادثة فورًا، ويحدد المقيّم خطورتها، ويتابع الجميع الحوادث ضمن نطاقهم. | المُبلِّغ؛ مقيّم الحادثة؛ المستخدم المخوَّل | 5 + 6 |
| **تفعيل الاستمرارية ومتابعة التعافي** `FEAT-RSK-CONTINUITY` | CAP-09.03 الاستمرارية والتعافي (R3) | يفعّل قائد الحادثة خطة الاستمرارية بقرار صريح، ويتابع مع مالك الاستمرارية تقدم التعافي مقارنة بزمن بدء الحادثة. | قائد الحادثة؛ مالك الاستمرارية | 2 + 6 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-09 (22)</summary>

- **سجل المخاطر** `FEAT-RSK-RISK-REGISTER`
  - `US-BC04-Q-RIS-GET` — جلب: Risk بنطاقه المرئي للطالب (جلب)
  - `US-BC04-Q-RIS-REGISTER` — جلب: سجل المخاطر مصفّى بالفئة/النطاق/الدرجة (جلب)
  - `US-BC04-RIS-IDENTIFY` — تحديد الخطر (أمر)
  - `US-BC04-S-RISK-01` — تلقائي: incident references this risk as risk_ref (الخطر) (نظام)
- **تقييم المخاطر ومعالجتها** `FEAT-RSK-RISK-TREATMENT`
  - `US-BC04-RIS-ASSESS` — تقييم الخطر (أمر)
  - `US-BC04-RIS-CLOSE` — إغلاق الخطر (أمر)
  - `US-BC04-RIS-PLAN-TREATMENT` — تخطيط معالجة الخطر (أمر)
  - `US-BC04-RIS-REASSESS` — إعادة تقييم الخطر (أمر)
- **قيادة الاستجابة للحادثة** `FEAT-RSK-INCIDENT-COMMAND`
  - `US-BC04-INC-CLOSE` — إغلاق الحادثة (أمر)
  - `US-BC04-INC-CONTAIN` — احتواء الحادثة (أمر)
  - `US-BC04-INC-DE-ESCALATE` — خفض خطورة الحادثة (أمر)
  - `US-BC04-INC-DISPATCH-RESPONSE` — توجيه الاستجابة لـالحادثة (أمر)
  - `US-BC04-INC-ESCALATE` — تصعيد الحادثة (أمر)
  - `US-BC04-INC-RESOLVE` — حل الحادثة (أمر)
  - `US-BC04-S-INCIDENT-01` — تلقائي: response SLA elapsed without dispatch (الحادثة) (نظام)
- **الإبلاغ عن الحوادث وتقييمها** `FEAT-RSK-INCIDENT-REPORT`
  - `US-BC04-INC-ASSESS` — تقييم الحادثة (أمر)
  - `US-BC04-INC-CANCEL` — إلغاء الحادثة (أمر)
  - `US-BC04-INC-REPORT` — الإبلاغ عن الحادثة (أمر)
  - `US-BC04-Q-INC-GET` — جلب: Incident بنطاقه المرئي للطالب (جلب)
  - `US-BC04-Q-INC-LIST` — جلب: حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق (جلب)
- **تفعيل الاستمرارية ومتابعة التعافي** `FEAT-RSK-CONTINUITY`
  - `US-BC04-INC-ACTIVATE-CONTINGENCY` — تفعيل خطة الاستمرارية لـالحادثة (أمر)
  - `US-BC04-Q-INC-RECOVERY-STATUS` — جلب: تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء الحادثة (RTO/RPO تقديرية) (جلب)

</details>

### 2.10 CAP-10 — الاتصال والمنتجات

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **صندوق إشعاراتي** `FEAT-COM-INBOX` | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) | يرى كل مستخدم إشعاراته في مكان واحد ويعلّمها كمقروءة، وتُنظف القديمة تلقائيًا. | المستخدم؛ النظام | 3 + 3 |
| **إيصال الإشعارات بأمان** `FEAT-COM-NOTIFY-DELIVERY` | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) | تصل الإشعارات داخل التطبيق وعلى الجوال إلى المخوّلين فقط ودون محتوى سري في رسائل الجوال. | النظام | 4 + 7 |
| **رسائل الإنذار العام** `FEAT-COM-PUBLIC-ALERTS` | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) | يعد ضابط المناوبة رسالة إنذار عامة بالمعيار الدولي ويطلقها صاحب السلطة إلى الجهات الخارجية مع متابعة وصولها. | ضابط المناوبة؛ المشغل؛ صاحب سلطة الإصدار؛ المدقق؛ النظام | 6 + 4 |
| **اشتراكاتي ومتابعاتي** `FEAT-COM-SUBSCRIPTIONS` | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) | يختار المستخدم ما يتابعه وكيف يصله التنبيه، ويوقفه أو يلغيه متى شاء. | المستخدم؛ النظام | 6 + 2 |
| **توزيع المنتجات** `FEAT-COM-DISTRIBUTION` | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) | يوزع المدير أو مالك المنتج المنتج المعتمد على المخوّلين فقط، مع سجل كامل لمن استلمه. | المدير؛ مالك المنتج؛ مسؤول الأمن؛ المدقق؛ النظام | 5 + 4 |
| **إعداد التقارير والإحاطات** `FEAT-COM-PRODUCT-AUTHORING` | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) | يولد المحلل أو المخطط تقريرًا أو إحاطة أو خريطة من قالب ببياناته وأدلته، ويحرر نصه ثم يقدمه للمراجعة. | المحلل؛ المخطط؛ النظام | 7 + 4 |
| **تصفح المنتجات وتنزيلها** `FEAT-COM-PRODUCT-LIBRARY` | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) | يجد المستخدم المخوّل المنتجات المعتمدة وأحدث نسخها وينزلها بصيغة PDF أو مستند بعلامة مائية باسمه. | المستخدم المخوّل؛ المحلل؛ المدير؛ النظام | 3 + 4 |
| **مراجعة المنتجات واعتمادها** `FEAT-COM-PRODUCT-REVIEW` | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) | يراجع المراجع المنتج فيعتمده نسخة نهائية مجمدة أو يعيده للتعديل، ويستطيع المدير سحبه. | المراجع؛ المدير | 3 + 3 |
| **قوالب المنتجات** `FEAT-COM-PRODUCT-TEMPLATES` | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) | يعد مدير المعرفة قوالب موحدة للتقارير والإحاطات والخرائط، ويعتمدها شخص ثانٍ قبل استخدامها. | مدير المعرفة؛ قائد التحليل؛ المعتمد الثاني | 4 + 2 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-10 (41)</summary>

- **صندوق إشعاراتي** `FEAT-COM-INBOX`
  - `US-BC04-NTF-MARK-READ` — تعليم الإشعار كمقروء (أمر)
  - `US-BC04-Q-NTF-INBOX` — جلب: My notifications (references + templates) (جلب)
  - `US-BC04-S-NOTIFICATION-05` — تلقائي: TTL (30 d) elapsed (الإشعار) (نظام)
- **إيصال الإشعارات بأمان** `FEAT-COM-NOTIFY-DELIVERY`
  - `US-BC04-S-NOTIFICATION-01` — تلقائي: notifiable event for recipient (الإشعار) (نظام)
  - `US-BC04-S-NOTIFICATION-02` — تلقائي: delivered to channel (الإشعار) (نظام)
  - `US-BC04-S-NOTIFICATION-03` — تلقائي: recipient no longer authorized at delivery (الإشعار) (نظام)
  - `US-BC04-S-NOTIFICATION-04` — تلقائي: delivery failed after retries (الإشعار) (نظام)
- **رسائل الإنذار العام** `FEAT-COM-PUBLIC-ALERTS`
  - `US-BC03-CAP-CANCEL` — إلغاء رسالة CAP الصادرة (أمر)
  - `US-BC03-CAP-PREPARE` — إعداد رسالة CAP الصادرة (أمر)
  - `US-BC03-CAP-RELEASE` — تحرير رسالة CAP الصادرة (أمر)
  - `US-BC03-CAP-RETRY` — إعادة محاولة رسالة CAP الصادرة (أمر)
  - `US-BC03-Q-CAP-LIST` — جلب: Outbound CAP messages by state (جلب)
  - `US-BC03-S-CAP-MESSAGE-01` — تلقائي: delivery failed after retries (رسالة CAP الصادرة) (نظام)
- **اشتراكاتي ومتابعاتي** `FEAT-COM-SUBSCRIPTIONS`
  - `US-BC04-S-SUBSCRIPTION-01` — تلقائي: subscriber lost visibility of target (الاشتراك) (نظام)
  - `US-BC04-SUB-PAUSE` — إيقاف الاشتراك مؤقتًا (أمر)
  - `US-BC04-SUB-RESUME` — استئناف الاشتراك (أمر)
  - `US-BC04-SUB-SUBSCRIBE` — إنشاء الاشتراك (أمر)
  - `US-BC04-SUB-UNSUBSCRIBE` — إلغاء الاشتراك (أمر)
  - `US-BC04-SUB-UPDATE-CHANNELS` — تحديث قنوات الاشتراك (أمر)
- **توزيع المنتجات** `FEAT-COM-DISTRIBUTION`
  - `US-BC06-DST-CANCEL` — إلغاء التوزيع (أمر)
  - `US-BC06-DST-DISTRIBUTE` — تنفيذ التوزيع (أمر)
  - `US-BC06-Q-DST-LOG` — جلب: Distribution and delivery log with watermark ids (جلب)
  - `US-BC06-S-DISTRIBUTION-01` — تلقائي: all recipients authorized and delivered (التوزيع) (نظام)
  - `US-BC06-S-DISTRIBUTION-02` — تلقائي: some recipients not authorized (التوزيع) (نظام)
- **إعداد التقارير والإحاطات** `FEAT-COM-PRODUCT-AUTHORING`
  - `US-BC06-PRD-CREATE` — إنشاء المنتج (أمر)
  - `US-BC06-PRD-DISCARD` — تجاهل مسودة المنتج (أمر)
  - `US-BC06-PRD-EDIT-NARRATIVE` — تعديل سرد المنتج (أمر)
  - `US-BC06-PRD-GENERATE` — توليد المنتج (أمر)
  - `US-BC06-PRD-SUBMIT` — تقديم المنتج (أمر)
  - `US-BC06-S-PRODUCT-01` — تلقائي: generation succeeded (المنتج) (نظام)
  - `US-BC06-S-PRODUCT-02` — تلقائي: generation failed (المنتج) (نظام)
- **تصفح المنتجات وتنزيلها** `FEAT-COM-PRODUCT-LIBRARY`
  - `US-BC06-Q-PRD-GET` — جلب: Product version with rendered artifacts (download grants) and pinned citations (جلب)
  - `US-BC06-Q-PRD-LIST` — جلب: Products by kind, state, situation/case, date (جلب)
  - `US-BC06-S-PRODUCT-03` — تلقائي: newer version approved (المنتج) (نظام)
- **مراجعة المنتجات واعتمادها** `FEAT-COM-PRODUCT-REVIEW`
  - `US-BC06-PRD-APPROVE` — اعتماد المنتج (أمر)
  - `US-BC06-PRD-RETURN` — إعادة المنتج للمراجعة (أمر)
  - `US-BC06-PRD-WITHDRAW` — سحب المنتج (أمر)
- **قوالب المنتجات** `FEAT-COM-PRODUCT-TEMPLATES`
  - `US-BC06-PTM-ACTIVATE` — تفعيل قالب المنتج (أمر)
  - `US-BC06-PTM-DEFINE` — تعريف قالب المنتج (أمر)
  - `US-BC06-PTM-EDIT` — تعديل قالب المنتج (أمر)
  - `US-BC06-PTM-RETIRE` — إحالة قالب المنتج إلى التقاعد (أمر)

</details>

### 2.11 CAP-11 — المعرفة والذاكرة المؤسسية

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **البحث في المعرفة وإعادة استخدامها** `FEAT-KNW-KNOWLEDGE-REUSE` | CAP-11.01 الدروس والمعرفة (R2) | يساعد المخطط والمستخدمين على إيجاد المعرفة المنشورة ذات الصلة بعملهم وتلقي اقتراحات منها وتسجيل الاستفادة منها. | المخطط;المستخدم المخوَّل | 3 + 3 |
| **مراجعة المعرفة ونشرها** `FEAT-KNW-KNOWLEDGE-REVIEW` | CAP-11.01 الدروس والمعرفة (R2) | يضمن أن ما يُنشر من معرفة مؤسسية قد راجعه مدير المعرفة واعتمده، وأن القديم منه يُسحب أو يُستبدل بنسخة أحدث. | مدير المعرفة;النظام | 5 + 3 |
| **تسجيل الدروس والمعرفة** `FEAT-KNW-LESSON-CAPTURE` | CAP-11.01 الدروس والمعرفة (R2) | يتيح لأي مستخدم توثيق درس أو إجراء أو ممارسة فضلى مرتبطة بمهمة أو خطة أو حادث مع أدلته وتقديمه للمراجعة. | المستخدم | 4 + 3 |
| **إتلاف السجلات المنتهية** `FEAT-KNW-DISPOSITION` | CAP-11.02 السجلات والاحتفاظ (R1 (الاحتفاظ والتجميد)) | ينفذ إتلاف أو أرشفة السجلات التي انتهت مدة حفظها بموافقة جهة مستقلة وبشهادة موثقة، مع استثناء المجمد منها. | أمين الأرشيف;السلطة القانونية;المدقق;النظام | 8 + 4 |
| **التجميد القانوني** `FEAT-KNW-LEGAL-HOLD` | CAP-11.02 السجلات والاحتفاظ (R1 (الاحتفاظ والتجميد)) | يمنع إتلاف أو محو أو تعديل السجلات المطلوبة لقضية أو تحقيق حتى ترفع الجهة القانونية التجميد. | السلطة القانونية;أمين الأرشيف;المدقق;النظام | 7 + 4 |
| **جداول الاحتفاظ بالسجلات** `FEAT-KNW-RETENTION-SCHEDULE` | CAP-11.02 السجلات والاحتفاظ (R1 (الاحتفاظ والتجميد)) | يحدد بوضوح كم تُحفظ كل فئة من السجلات وماذا يحدث لها بعد انتهاء المدة، بموافقة الجهة القانونية. | أمين الأرشيف;السلطة القانونية;المدقق;النظام | 6 + 2 |
| **حفظ الأرشيف وسلامته** `FEAT-KNW-ARCHIVE-PRESERVE` | CAP-11.03 الأرشيف وإعادة البناء التاريخي (R2) | يضمن نقل السجلات المؤرشفة إلى حزم محفوظة بصيغ دائمة يُتحقق من سلامتها دوريًا وتُصلح أو تُرحَّل عند الحاجة. | أمين الأرشيف;جهة النقل;النظام | 9 + 7 |
| **استرجاع السجلات التاريخية** `FEAT-KNW-ARCHIVE-RETRIEVE` | CAP-11.03 الأرشيف وإعادة البناء التاريخي (R2) | يمكّن المستخدم المخوَّل من البحث في فهرس الأرشيف واسترجاع سجل تاريخي ضمن الوقت المستهدف مع تسجيل كل وصول. | المستخدم المخوَّل;أمين الأرشيف | 2 + 5 |
| **إعادة البناء التاريخي** `FEAT-KNW-RECONSTRUCTION` | CAP-11.03 الأرشيف وإعادة البناء التاريخي (R2) | يجيب عن سؤال «ماذا كنا نعرف عن الوضع في وقت معيّن» بتقرير يميّز ما هو مسجل فعلًا عمّا أُعيد بناؤه. | المدقق;القانوني;المحلل;النظام | 6 + 5 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-11 (50)</summary>

- **البحث في المعرفة وإعادة استخدامها** `FEAT-KNW-KNOWLEDGE-REUSE`
  - `US-BC06-KNO-RECORD-REUSE` — تسجيل إعادة استخدام كائن المعرفة (أمر)
  - `US-BC06-Q-KNO-SEARCH` — جلب: Published knowledge by type, text, relationships (جلب)
  - `US-BC06-Q-KNO-SUGGEST` — جلب: Published knowledge relevant to a task type / plan / area (by relationships) (جلب)
- **مراجعة المعرفة ونشرها** `FEAT-KNW-KNOWLEDGE-REVIEW`
  - `US-BC06-KNO-PUBLISH` — نشر كائن المعرفة (أمر)
  - `US-BC06-KNO-REJECT` — رفض كائن المعرفة (أمر)
  - `US-BC06-KNO-RETIRE` — إحالة كائن المعرفة إلى التقاعد (أمر)
  - `US-BC06-KNO-RETURN` — إعادة كائن المعرفة للمراجعة (أمر)
  - `US-BC06-S-KNOWLEDGE-OBJECT-01` — تلقائي: newer version published (كائن المعرفة) (نظام)
- **تسجيل الدروس والمعرفة** `FEAT-KNW-LESSON-CAPTURE`
  - `US-BC06-KNO-DISCARD` — تجاهل مسودة كائن المعرفة (أمر)
  - `US-BC06-KNO-DRAFT` — إعداد مسودة كائن المعرفة (أمر)
  - `US-BC06-KNO-EDIT` — تعديل كائن المعرفة (أمر)
  - `US-BC06-KNO-SUBMIT` — تقديم كائن المعرفة (أمر)
- **إتلاف السجلات المنتهية** `FEAT-KNW-DISPOSITION`
  - `US-BC08-DSP-APPROVE` — اعتماد تشغيل الإتلاف (أمر)
  - `US-BC08-DSP-CANCEL` — إلغاء تشغيل الإتلاف (أمر)
  - `US-BC08-DSP-SUBMIT` — تقديم تشغيل الإتلاف (أمر)
  - `US-BC08-Q-DSP-GET` — جلب: Run with candidate summary, exceptions and certificate (جلب)
  - `US-BC08-S-DISPOSITION-RUN-01` — تلقائي: scheduled evaluation (daily) (تشغيل الإتلاف) (نظام)
  - `US-BC08-S-DISPOSITION-RUN-02` — تلقائي: execution started (تشغيل الإتلاف) (نظام)
  - `US-BC08-S-DISPOSITION-RUN-03` — تلقائي: all buckets processed (تشغيل الإتلاف) (نظام)
  - `US-BC08-S-DISPOSITION-RUN-04` — تلقائي: some buckets failed (تشغيل الإتلاف) (نظام)
- **التجميد القانوني** `FEAT-KNW-LEGAL-HOLD`
  - `US-BC08-LHD-APPROVE-RELEASE` — اعتماد رفع التجميد القانوني (أمر)
  - `US-BC08-LHD-CANCEL-RELEASE` — إلغاء طلب رفع التجميد القانوني (أمر)
  - `US-BC08-LHD-EXTEND` — تمديد التجميد القانوني (أمر)
  - `US-BC08-LHD-PLACE` — إنشاء التجميد القانوني (أمر)
  - `US-BC08-LHD-REQUEST-RELEASE` — طلب رفع التجميد القانوني (أمر)
  - `US-BC08-Q-LHD-CHECK` — جلب: HoldCheck OHS: URNs / subjects / (class, bucket) → held? with hold ids (جلب)
  - `US-BC08-Q-LHD-LIST` — جلب: Holds by state and scope (جلب)
- **جداول الاحتفاظ بالسجلات** `FEAT-KNW-RETENTION-SCHEDULE`
  - `US-BC08-Q-RTS-ACTIVE` — جلب: Active schedule version with rules (جلب)
  - `US-BC08-RTS-ACTIVATE` — تفعيل جدول الاحتفاظ (أمر)
  - `US-BC08-RTS-DISCARD` — تجاهل مسودة جدول الاحتفاظ (أمر)
  - `US-BC08-RTS-DRAFT` — إعداد مسودة جدول الاحتفاظ (أمر)
  - `US-BC08-RTS-EDIT` — تعديل جدول الاحتفاظ (أمر)
  - `US-BC08-S-RETENTION-SCHEDULE-01` — تلقائي: successor activated (جدول الاحتفاظ) (نظام)
- **حفظ الأرشيف وسلامته** `FEAT-KNW-ARCHIVE-PRESERVE`
  - `US-BC06-ARC-MIGRATE-FORMAT` — ترحيل صيغة الحزمة الأرشيفية (أمر)
  - `US-BC06-ARC-REPAIR` — إصلاح الحزمة الأرشيفية (أمر)
  - `US-BC06-ARC-RETRY-INGEST` — إعادة محاولة استيعاب الحزمة الأرشيفية (أمر)
  - `US-BC06-ARC-TRANSFER` — نقل الحزمة الأرشيفية (أمر)
  - `US-BC06-S-ARCHIVE-PACKAGE-01` — تلقائي: disposition action ARCHIVE for a bucket or record set (الحزمة الأرشيفية) (نظام)
  - `US-BC06-S-ARCHIVE-PACKAGE-02` — تلقائي: package validated (الحزمة الأرشيفية) (نظام)
  - `US-BC06-S-ARCHIVE-PACKAGE-03` — تلقائي: validation failed (الحزمة الأرشيفية) (نظام)
  - `US-BC06-S-ARCHIVE-PACKAGE-04` — تلقائي: integrity check failed (الحزمة الأرشيفية) (نظام)
  - `US-BC06-S-ARCHIVE-PACKAGE-05` — تلقائي: disposition DESTROY executed for the package bucket (الحزمة الأرشيفية) (نظام)
- **استرجاع السجلات التاريخية** `FEAT-KNW-ARCHIVE-RETRIEVE`
  - `US-BC06-Q-ARC-RETRIEVE` — جلب: Retrieve package content (warm: signed grant; cold: staged job) — access logged (جلب)
  - `US-BC06-Q-ARC-SEARCH` — جلب: Archive catalogue (metadata only) by class, period, org (جلب)
- **إعادة البناء التاريخي** `FEAT-KNW-RECONSTRUCTION`
  - `US-BC06-Q-REC-REPORT` — جلب: Labelled reconstruction report (جلب)
  - `US-BC06-REC-CANCEL` — إلغاء إعادة البناء التاريخي (أمر)
  - `US-BC06-REC-REQUEST` — طلب إعادة البناء التاريخي (أمر)
  - `US-BC06-S-RECONSTRUCTION-01` — تلقائي: worker started (إعادة البناء التاريخي) (نظام)
  - `US-BC06-S-RECONSTRUCTION-02` — تلقائي: completed (إعادة البناء التاريخي) (نظام)
  - `US-BC06-S-RECONSTRUCTION-03` — تلقائي: failed (إعادة البناء التاريخي) (نظام)

</details>

### 2.12 CAP-12 — المساعدة بالذكاء الاصطناعي

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **المساعد الذكي** `FEAT-AI-ASSISTANT` | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) | يتيح للمستخدم طرح سؤال على المساعد الذكي والحصول على إجابة مستندة إلى أدلة مع استشهاداتها، أو إبلاغه صراحة بعدم كفاية الأدلة. | المستخدم المخوَّل;النظام | 6 + 5 |
| **تأريض الإجابات بالأدلة المخوَّلة** `FEAT-AI-GROUNDING` | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) | يضمن أن المساعد لا يستخدم إلا البيانات التي يحق للسائل رؤيتها وأن كل عبارة في الإجابة مسندة إلى دليل يمكن تدقيقه. | النظام;المدقق | 5 + 6 |
| **توجيه نماذج الذكاء الاصطناعي** `FEAT-AI-ROUTING` | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) | يحدد لكل مستأجر أي نموذج يخدم أي نوع من الطلبات، محليًا افتراضيًا، ولا يُسمح بنموذج خارجي إلا بسياسة صريحة وبيانات غير مصنفة. | حوكمة الذكاء الاصطناعي;سلطة ثانية;مسؤول الأمن;النظام | 6 + 3 |
| **سجل أدوات الذكاء الاصطناعي** `FEAT-AI-TOOLS` | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) | يضمن أن كل أداة يستخدمها الذكاء الاصطناعي مسجلة بصلاحيتها ومستوى استقلاليتها، ويمكن لمسؤول الأمن تفعيلها أو تعطيلها. | مهندس منصة الذكاء الاصطناعي;مسؤول الأمن;حوكمة الذكاء الاصطناعي | 6 + 3 |
| **صياغة المسودات والملخصات** `FEAT-AI-DRAFTING` | CAP-12.02 الصياغة والتلخيص (R2) | يساعد المحلل والمدير على إعداد مسودات التقارير وملخصات الحالات بسرعة، مع وسمها بوضوح كمخرجات ذكاء اصطناعي. | المحلل;المدير;المخطط | 0 + 4 |
| **مراجعة نتائج الذكاء الاصطناعي** `FEAT-AI-RESULT-REVIEW` | CAP-12.02 الصياغة والتلخيص (R2) | يضمن ألا تُعتمد أو تُنشر أي نتيجة من الذكاء الاصطناعي إلا بعد أن يراجعها إنسان ويقبلها كليًا أو جزئيًا أو يرفضها بسبب. | المراجع;النظام | 6 + 3 |
| **استخراج المعلومات من الوثائق** `FEAT-AI-EXTRACTION` | CAP-12.03 الاستخراج والترجمة (R2) | يوفر على المحلل الجهد باستخراج الكيانات والأماكن والتواريخ من الوثائق كادعاءات مقترحة تنتظر قبوله. | المحلل;المراجع | 0 + 4 |
| **الترجمة بين العربية والإنجليزية** `FEAT-AI-TRANSLATION` | CAP-12.03 الاستخراج والترجمة (R2) | يتيح ترجمة النصوص بين العربية والإنجليزية عند الطلب مع بقاء النص الأصلي محفوظًا كما هو. | المستخدم المخوَّل | 0 + 2 |
| **حزم تقييم الذكاء الاصطناعي** `FEAT-AI-EVAL-SUITES` | CAP-12.04 تقييم AI وحوكمته (R2) | يحدد معايير ثابتة ومعتمدة لقياس جودة النماذج كالتأريض ودقة الاستشهاد ومعدل الهلوسة. | حوكمة الذكاء الاصطناعي;سلطة ثانية;النظام | 4 + 2 |
| **تقييم النماذج واعتمادها** `FEAT-AI-MODEL-APPROVAL` | CAP-12.04 تقييم AI وحوكمته (R2) | يضمن ألا يدخل أي نموذج ذكاء اصطناعي إلى الاستخدام الفعلي إلا بعد تقييم موثق لدقته وتكلفته وموافقة بشرية. | مهندس منصة الذكاء الاصطناعي;حوكمة الذكاء الاصطناعي;المدقق | 7 + 3 |
| **مراقبة النماذج وإيقافها** `FEAT-AI-MODEL-MONITOR` | CAP-12.04 تقييم AI وحوكمته (R2) | ينبه إلى تراجع أداء النموذج أثناء التشغيل ويتيح إيقاف استخدامه أو إعادته أو إحالته إلى التقاعد. | حوكمة الذكاء الاصطناعي;مهندس منصة الذكاء الاصطناعي;النظام | 5 + 4 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-12 (45)</summary>

- **المساعد الذكي** `FEAT-AI-ASSISTANT`
  - `US-BC07-AIR-CANCEL` — إلغاء طلب الذكاء الاصطناعي (أمر)
  - `US-BC07-AIR-SUBMIT` — تقديم طلب الذكاء الاصطناعي (أمر)
  - `US-BC07-Q-AIR-GET` — جلب: Request with answer, statements and citations (visible only), status (جلب)
  - `US-BC07-S-AI-REQUEST-01` — تلقائي: policy denied (طلب الذكاء الاصطناعي) (نظام)
  - `US-BC07-S-AI-REQUEST-04` — تلقائي: no sufficient evidence retrieved (طلب الذكاء الاصطناعي) (نظام)
  - `US-BC07-S-AI-REQUEST-07` — تلقائي: error or timeout (طلب الذكاء الاصطناعي) (نظام)
- **تأريض الإجابات بالأدلة المخوَّلة** `FEAT-AI-GROUNDING`
  - `US-BC07-Q-AIR-CONTEXT` — جلب: Context package items (URN, version, label) — for audit and review (جلب)
  - `US-BC07-S-AI-REQUEST-02` — تلقائي: retrieval started (طلب الذكاء الاصطناعي) (نظام)
  - `US-BC07-S-AI-REQUEST-03` — تلقائي: context package sealed (طلب الذكاء الاصطناعي) (نظام)
  - `US-BC07-S-AI-REQUEST-05` — تلقائي: output grounded (طلب الذكاء الاصطناعي) (نظام)
  - `US-BC07-S-AI-REQUEST-06` — تلقائي: output not grounded (طلب الذكاء الاصطناعي) (نظام)
- **توجيه نماذج الذكاء الاصطناعي** `FEAT-AI-ROUTING`
  - `US-BC07-Q-RTG-ACTIVE` — جلب: Active routing for the tenant (جلب)
  - `US-BC07-RTG-ACTIVATE` — تفعيل توجيه الذكاء الاصطناعي (أمر)
  - `US-BC07-RTG-DISCARD` — تجاهل مسودة توجيه الذكاء الاصطناعي (أمر)
  - `US-BC07-RTG-DRAFT` — إعداد مسودة توجيه الذكاء الاصطناعي (أمر)
  - `US-BC07-RTG-EDIT` — تعديل توجيه الذكاء الاصطناعي (أمر)
  - `US-BC07-S-AI-ROUTING-01` — تلقائي: successor activated (توجيه الذكاء الاصطناعي) (نظام)
- **سجل أدوات الذكاء الاصطناعي** `FEAT-AI-TOOLS`
  - `US-BC07-Q-TOL-LIST` — جلب: Tool registry (جلب)
  - `US-BC07-TOL-ACTIVATE` — تفعيل أداة الذكاء الاصطناعي (أمر)
  - `US-BC07-TOL-DISABLE` — تعطيل أداة الذكاء الاصطناعي (أمر)
  - `US-BC07-TOL-ENABLE` — تمكين أداة الذكاء الاصطناعي (أمر)
  - `US-BC07-TOL-REGISTER` — تسجيل أداة الذكاء الاصطناعي (أمر)
  - `US-BC07-TOL-RETIRE` — إحالة أداة الذكاء الاصطناعي إلى التقاعد (أمر)
- **صياغة المسودات والملخصات** `FEAT-AI-DRAFTING` — بلا قصص حالية
- **مراجعة نتائج الذكاء الاصطناعي** `FEAT-AI-RESULT-REVIEW`
  - `US-BC07-AIRS-ACCEPT` — قبول نتيجة الذكاء الاصطناعي (أمر)
  - `US-BC07-AIRS-ACCEPT-PARTIALLY` — قبول نتيجة الذكاء الاصطناعي جزئيًا (أمر)
  - `US-BC07-AIRS-REJECT` — رفض نتيجة الذكاء الاصطناعي (أمر)
  - `US-BC07-AIRS-START-REVIEW` — بدء مراجعة نتيجة الذكاء الاصطناعي (أمر)
  - `US-BC07-Q-AIRS-QUEUE` — جلب: Reviewable AI results by state, operation, target (جلب)
  - `US-BC07-S-AI-RESULT-01` — تلقائي: request COMPLETED for a reviewable operation (نتيجة الذكاء الاصطناعي) (نظام)
- **استخراج المعلومات من الوثائق** `FEAT-AI-EXTRACTION` — بلا قصص حالية
- **الترجمة بين العربية والإنجليزية** `FEAT-AI-TRANSLATION` — بلا قصص حالية
- **حزم تقييم الذكاء الاصطناعي** `FEAT-AI-EVAL-SUITES`
  - `US-BC07-EVS-ACTIVATE` — تفعيل حزمة التقييم (أمر)
  - `US-BC07-EVS-DRAFT` — إعداد مسودة حزمة التقييم (أمر)
  - `US-BC07-EVS-EDIT` — تعديل حزمة التقييم (أمر)
  - `US-BC07-S-EVAL-SUITE-01` — تلقائي: successor activated (حزمة التقييم) (نظام)
- **تقييم النماذج واعتمادها** `FEAT-AI-MODEL-APPROVAL`
  - `US-BC07-MDL-APPROVE` — اعتماد إصدار النموذج (أمر)
  - `US-BC07-MDL-FAIL-EVALUATION` — تسجيل فشل تقييم إصدار النموذج (أمر)
  - `US-BC07-MDL-PROMOTE` — ترقية إصدار النموذج (أمر)
  - `US-BC07-MDL-REGISTER` — تسجيل إصدار النموذج (أمر)
  - `US-BC07-MDL-STAGE` — تجهيز إصدار النموذج للإنتاج (أمر)
  - `US-BC07-MDL-START-EVALUATION` — بدء تقييم إصدار النموذج (أمر)
  - `US-BC07-Q-MDL-LIST` — جلب: Model versions with state, evaluation summary, hosting (جلب)
- **مراقبة النماذج وإيقافها** `FEAT-AI-MODEL-MONITOR`
  - `US-BC07-MDL-DEPRECATE` — إهمال إصدار النموذج (إيقاف الاستخدام الجديد) (أمر)
  - `US-BC07-MDL-REINSTATE` — إعادة إصدار النموذج إلى السريان (أمر)
  - `US-BC07-MDL-RETIRE` — إحالة إصدار النموذج إلى التقاعد (أمر)
  - `US-BC07-Q-AI-USAGE` — جلب: GPU-hours, requests, cost indicators per tenant and operation (جلب)
  - `US-BC07-S-MODEL-VERSION-01` — تلقائي: monitoring drift detected (إصدار النموذج) (نظام)

</details>

### 2.13 CAP-13 — الحوكمة والأمن والامتثال

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **مخطط التصنيف الأمني** `FEAT-GOV-CLASSIFICATION` | CAP-13.01 التصنيف والسياسات (R1) | يتيح لمسؤول الأمن تحديد مستويات السرية والحجرات وقيود الإفراج الخاصة بالمستأجر واعتمادها، ويعرضها لكل مستخدم. | مسؤول الأمن؛ مستخدم المستأجر؛ النظام | 6 + 2 |
| **التصاريح الأمنية للمستخدمين** `FEAT-GOV-CLEARANCE` | CAP-13.01 التصنيف والسياسات (R1) | يتيح لمسؤول الأمن منح كل مستخدم مستوى سرية وحجرات محددة واعتمادها وتعديلها وتعليقها وسحبها، فلا يرى إلا ما يسمح به تصريحه. | مسؤول الأمن؛ المستخدم؛ النظام | 8 + 4 |
| **الاستثناءات الأمنية المؤقتة** `FEAT-GOV-EXCEPTIONS` | CAP-13.01 التصنيف والسياسات (R1) | يتيح للمستخدم طلب استثناء أمني مؤقت بمبرر واضح يعتمده شخصان مخولان، ويُسحب تلقائيًا عند انتهاء مدته. | المستخدم؛ مسؤول الأمن؛ المدقق؛ النظام | 6 + 2 |
| **التسجيل التلقائي للعمليات** `FEAT-GOV-AUDIT-CAPTURE` | CAP-13.02 التدقيق (R1) | يضمن تسجيل كل تغيير وكل اطلاع على بيانات حساسة تلقائيًا مع الفاعل والغرض وقرار الوصول، دون أن يتمكن أحد من تعديل السجل أو حذفه. | النظام | 0 + 6 |
| **مراجعة سجل التدقيق** `FEAT-GOV-AUDIT-TRAIL` | CAP-13.02 التدقيق (R1) | يتيح للمدقق ومسؤول الأمن البحث في سجل من فعل ماذا ومتى ولماذا والتحقق من أن السجل لم يُعبث به. | المدقق؛ مسؤول الأمن | 2 + 7 |
| **محو البيانات الشخصية** `FEAT-GOV-ERASURE` | CAP-13.03 الخصوصية والاحتفاظ (R1) | يتيح لمسؤول الخصوصية تسجيل طلب محو بيانات شخص يعتمده مرجع قانوني مستقل، ثم يمحوها من كل أجزاء المنصة مع إصدار شهادة دون فقدان حقائق التدقيق. | مسؤول الخصوصية؛ المرجع القانوني؛ المسؤول؛ المدقق؛ النظام | 10 + 5 |
| **إقامة البيانات وسيادتها** `FEAT-GOV-DATA-RESIDENCY` | CAP-13.04 السيادة وإقامة البيانات (R1) | يضمن بقاء جميع بيانات الجهة داخل نطاقها الجغرافي والقانوني المحدد وعدم نقلها خارجه إلا بسياسة صريحة من المستأجر. | مسؤول الأمن؛ مشغل المنصة؛ النظام | 0 + 6 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-13 (32)</summary>

- **مخطط التصنيف الأمني** `FEAT-GOV-CLASSIFICATION`
  - `US-BC08-CLS-ACTIVATE` — تفعيل مخطط التصنيف (أمر)
  - `US-BC08-CLS-DISCARD` — تجاهل مسودة مخطط التصنيف (أمر)
  - `US-BC08-CLS-DRAFT` — إعداد مسودة مخطط التصنيف (أمر)
  - `US-BC08-CLS-EDIT` — تعديل مخطط التصنيف (أمر)
  - `US-BC08-Q-CLS-ACTIVE` — جلب: Active scheme (labels only) (جلب)
  - `US-BC08-S-CLASSIFICATION-SCHEME-01` — تلقائي: successor activated (مخطط التصنيف) (نظام)
- **التصاريح الأمنية للمستخدمين** `FEAT-GOV-CLEARANCE`
  - `US-BC01-CLR-APPROVE` — اعتماد التصريح الأمني (أمر)
  - `US-BC01-CLR-GRANT` — منح التصريح الأمني (أمر)
  - `US-BC01-CLR-MODIFY` — تعديل التصريح الأمني (أمر)
  - `US-BC01-CLR-REINSTATE` — إعادة التصريح الأمني إلى السريان (أمر)
  - `US-BC01-CLR-REVOKE` — سحب التصريح الأمني (أمر)
  - `US-BC01-CLR-SUSPEND` — تعليق التصريح الأمني (أمر)
  - `US-BC01-Q-CLR-GET` — جلب: Current clearance (level/compartments) (جلب)
  - `US-BC01-S-CLEARANCE-01` — تلقائي: valid_to reached (التصريح الأمني) (نظام)
- **الاستثناءات الأمنية المؤقتة** `FEAT-GOV-EXCEPTIONS`
  - `US-BC08-EXC-APPROVE` — اعتماد الاستثناء الأمني (أمر)
  - `US-BC08-EXC-REJECT` — رفض الاستثناء الأمني (أمر)
  - `US-BC08-EXC-REQUEST` — طلب الاستثناء الأمني (أمر)
  - `US-BC08-EXC-REVOKE` — سحب الاستثناء الأمني (أمر)
  - `US-BC08-Q-EXC-LIST` — جلب: Exceptions by state (جلب)
  - `US-BC08-S-SECURITY-EXCEPTION-01` — تلقائي: end reached (الاستثناء الأمني) (نظام)
- **التسجيل التلقائي للعمليات** `FEAT-GOV-AUDIT-CAPTURE` — بلا قصص حالية
- **مراجعة سجل التدقيق** `FEAT-GOV-AUDIT-TRAIL`
  - `US-BC08-Q-AUD-SEARCH` — جلب: Audit records by actor, resource, time, correlation id (جلب)
  - `US-BC08-Q-AUD-VERIFY` — جلب: Start integrity verification job; returns job ref (جلب)
- **محو البيانات الشخصية** `FEAT-GOV-ERASURE`
  - `US-BC01-PER-ERASE` — محو الشخص (أمر)
  - `US-BC08-ERS-APPROVE` — اعتماد طلب المحو (أمر)
  - `US-BC08-ERS-REGISTER` — تسجيل طلب المحو (أمر)
  - `US-BC08-ERS-REJECT` — رفض طلب المحو (أمر)
  - `US-BC08-Q-ERS-GET` — جلب: Request with scope counts, confirmations and certificate (no personal data) (جلب)
  - `US-BC08-S-ERASURE-REQUEST-01` — تلقائي: subject scope resolved (طلب المحو) (نظام)
  - `US-BC08-S-ERASURE-REQUEST-02` — تلقائي: hold matches subject (طلب المحو) (نظام)
  - `US-BC08-S-ERASURE-REQUEST-03` — تلقائي: hold released (طلب المحو) (نظام)
  - `US-BC08-S-ERASURE-REQUEST-04` — تلقائي: execution started (طلب المحو) (نظام)
  - `US-BC08-S-ERASURE-REQUEST-05` — تلقائي: all contexts confirmed (طلب المحو) (نظام)
- **إقامة البيانات وسيادتها** `FEAT-GOV-DATA-RESIDENCY` — بلا قصص حالية

</details>

### 2.14 CAP-14 — تشغيل المنصة

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **واجهة عربية وإنجليزية** `FEAT-PLT-LOCALIZATION` | CAP-14.01 المراقبة (R1) | يتيح لكل مستخدم العمل بالعربية أو الإنجليزية باتجاه الكتابة المناسب مع إمكانية عرض التاريخ الهجري. | المستخدم | 0 + 3 |
| **مراقبة صحة المنصة** `FEAT-PLT-MONITORING` | CAP-14.01 المراقبة (R1) | يمكّن مشغل المنصة من رؤية صحة كل مكونات المنصة وأدائها وتتبع أي طلب عبرها، ومتابعة مؤشرات نتائج الأعمال. | مشغل المنصة | 0 + 8 |
| **التثبيت والترقية دون اتصال** `FEAT-PLT-AIRGAP-UPGRADE` | CAP-14.02 الاعتمادية والتعافي (R1) | يتيح تثبيت المنصة وترقيتها وتشغيلها في بيئة معزولة عن الإنترنت مع بقاء الواجهات القديمة تعمل عند إصدار نسخ جديدة. | مشغل المنصة | 0 + 4 |
| **متابعة العمليات الطويلة** `FEAT-PLT-BACKGROUND-JOBS` | CAP-14.02 الاعتمادية والتعافي (R1) | يتيح للمستخدم متابعة العمليات الثقيلة كالاستيراد الكبير والتقارير والتحليلات وهي تعمل في الخلفية وإعادة محاولتها أو إلغاءها. | المستخدم؛ مشغل المنصة؛ النظام | 0 + 5 |
| **النسخ الاحتياطي والاستعادة** `FEAT-PLT-BACKUP-RESTORE` | CAP-14.02 الاعتمادية والتعافي (R1) | يضمن نسخ جميع البيانات احتياطيًا حسب أهميتها والتحقق آليًا من إمكانية استعادتها ضمن المدد المتفق عليها. | مشغل المنصة؛ النظام | 0 + 5 |
| **موثوقية الأحداث والإسقاطات** `FEAT-PLT-EVENT-DELIVERY` | CAP-14.02 الاعتمادية والتعافي (R1) | يضمن وصول كل حدث مرة واحدة فعليًا إلى الأجزاء المعنية وبقاء شاشات العرض متطابقة مع البيانات الأصلية وإمكانية إعادة بنائها. | مشغل المنصة؛ النظام | 0 + 6 |
| **نقل المستأجر بين خلايا التشغيل** `FEAT-PLT-CELL-MIGRATION` | CAP-14.03 تهيئة المستأجرين والحصص (R1) | يتيح لمشغل المنصة نقل مستأجر إلى خلية تشغيل أخرى (مشتركة أو مخصصة أو سيادية) دون فقدان بيانات، بنفس نسخة البرنامج في كل البيئات. | مشغل المنصة؛ النظام | 2 + 4 |
| **حصص المستأجر وحدود الاستخدام** `FEAT-PLT-TENANT-QUOTAS` | CAP-14.03 تهيئة المستأجرين والحصص (R1) | يتيح لمشغل المنصة تحديد حصص كل مستأجر من الطلبات والتخزين والأحداث والمهام وفرضها، حتى لا يؤثر مستأجر على غيره. | مشغل المنصة؛ مسؤول المستأجر؛ النظام | 1 + 5 |

القصص: الحالية + الجديدة المتوقعة.

<details><summary>قصص ميزات CAP-14 (3)</summary>

- **واجهة عربية وإنجليزية** `FEAT-PLT-LOCALIZATION` — بلا قصص حالية
- **مراقبة صحة المنصة** `FEAT-PLT-MONITORING` — بلا قصص حالية
- **التثبيت والترقية دون اتصال** `FEAT-PLT-AIRGAP-UPGRADE` — بلا قصص حالية
- **متابعة العمليات الطويلة** `FEAT-PLT-BACKGROUND-JOBS` — بلا قصص حالية
- **النسخ الاحتياطي والاستعادة** `FEAT-PLT-BACKUP-RESTORE` — بلا قصص حالية
- **موثوقية الأحداث والإسقاطات** `FEAT-PLT-EVENT-DELIVERY` — بلا قصص حالية
- **نقل المستأجر بين خلايا التشغيل** `FEAT-PLT-CELL-MIGRATION`
  - `US-BC01-TEN-COMPLETE-CELL-MIGRATION` — إكمال ترحيل المستأجر إلى خلية أخرى (نظام)
  - `US-BC01-TEN-START-CELL-MIGRATION` — بدء ترحيل المستأجر إلى خلية أخرى (أمر)
- **حصص المستأجر وحدود الاستخدام** `FEAT-PLT-TENANT-QUOTAS`
  - `US-BC01-TEN-UPDATE-QUOTAS` — تحديث حصص المستأجر (أمر)

</details>

## 3. ميزات بلا قصص حالية

14 ميزة تغطي متطلبات لا تقابلها اليوم أي قصة، وتُملأ بالقصص الجديدة في المرحلة 3:

| الميزة | القدرة الفرعية | القيمة |
|---|---|---|
| **العمل الميداني دون اتصال** `FEAT-COL-OFFLINE-WORK` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) | يتيح للمستخدم الميداني مواصلة العمل حتى 72 ساعة دون شبكة مع حفظ بياناته مشفرة على الجهاز. |
| **التكامل مع أنظمة المؤسسة** `FEAT-COL-ENTERPRISE-INT` | CAP-02.04 الاستيعاب والتكامل | يربط أنظمة الموارد البشرية والمالية وإدارة الوثائق بالمنصة دون أن تصبح مرجعًا للحقيقة. |
| **استيراد الخرائط والطقس** `FEAT-COL-GEO-WEATHER` | CAP-02.04 الاستيعاب والتكامل | يتيح جلب الطبقات الجغرافية وبيانات الطقس من مزوديها المعتمدين لتظهر في الصورة العملياتية. |
| **صياغة المسودات والملخصات** `FEAT-AI-DRAFTING` | CAP-12.02 الصياغة والتلخيص | يساعد المحلل والمدير على إعداد مسودات التقارير وملخصات الحالات بسرعة، مع وسمها بوضوح كمخرجات ذكاء اصطناعي. |
| **استخراج المعلومات من الوثائق** `FEAT-AI-EXTRACTION` | CAP-12.03 الاستخراج والترجمة | يوفر على المحلل الجهد باستخراج الكيانات والأماكن والتواريخ من الوثائق كادعاءات مقترحة تنتظر قبوله. |
| **الترجمة بين العربية والإنجليزية** `FEAT-AI-TRANSLATION` | CAP-12.03 الاستخراج والترجمة | يتيح ترجمة النصوص بين العربية والإنجليزية عند الطلب مع بقاء النص الأصلي محفوظًا كما هو. |
| **التسجيل التلقائي للعمليات** `FEAT-GOV-AUDIT-CAPTURE` | CAP-13.02 التدقيق | يضمن تسجيل كل تغيير وكل اطلاع على بيانات حساسة تلقائيًا مع الفاعل والغرض وقرار الوصول، دون أن يتمكن أحد من تعديل السجل أو حذفه. |
| **إقامة البيانات وسيادتها** `FEAT-GOV-DATA-RESIDENCY` | CAP-13.04 السيادة وإقامة البيانات | يضمن بقاء جميع بيانات الجهة داخل نطاقها الجغرافي والقانوني المحدد وعدم نقلها خارجه إلا بسياسة صريحة من المستأجر. |
| **واجهة عربية وإنجليزية** `FEAT-PLT-LOCALIZATION` | CAP-14.01 المراقبة | يتيح لكل مستخدم العمل بالعربية أو الإنجليزية باتجاه الكتابة المناسب مع إمكانية عرض التاريخ الهجري. |
| **مراقبة صحة المنصة** `FEAT-PLT-MONITORING` | CAP-14.01 المراقبة | يمكّن مشغل المنصة من رؤية صحة كل مكونات المنصة وأدائها وتتبع أي طلب عبرها، ومتابعة مؤشرات نتائج الأعمال. |
| **التثبيت والترقية دون اتصال** `FEAT-PLT-AIRGAP-UPGRADE` | CAP-14.02 الاعتمادية والتعافي | يتيح تثبيت المنصة وترقيتها وتشغيلها في بيئة معزولة عن الإنترنت مع بقاء الواجهات القديمة تعمل عند إصدار نسخ جديدة. |
| **متابعة العمليات الطويلة** `FEAT-PLT-BACKGROUND-JOBS` | CAP-14.02 الاعتمادية والتعافي | يتيح للمستخدم متابعة العمليات الثقيلة كالاستيراد الكبير والتقارير والتحليلات وهي تعمل في الخلفية وإعادة محاولتها أو إلغاءها. |
| **النسخ الاحتياطي والاستعادة** `FEAT-PLT-BACKUP-RESTORE` | CAP-14.02 الاعتمادية والتعافي | يضمن نسخ جميع البيانات احتياطيًا حسب أهميتها والتحقق آليًا من إمكانية استعادتها ضمن المدد المتفق عليها. |
| **موثوقية الأحداث والإسقاطات** `FEAT-PLT-EVENT-DELIVERY` | CAP-14.02 الاعتمادية والتعافي | يضمن وصول كل حدث مرة واحدة فعليًا إلى الأجزاء المعنية وبقاء شاشات العرض متطابقة مع البيانات الأصلية وإمكانية إعادة بنائها. |

<!-- END GENERATED: build_analysis_design.py -->
