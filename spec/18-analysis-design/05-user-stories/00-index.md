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

| القدرة | الميزات | القصص من المواصفة | القصص الجديدة | المجلد |
|---|---|---|---|---|
| CAP-01 إدارة المؤسسة والوصول | 13 | 72 | 65 | `CAP-01-org-access` |
| CAP-02 جمع المعلومات | 22 | 116 | 97 | `CAP-02-collection` |
| CAP-03 إدارة المعلومات | 16 | 76 | 80 | `CAP-03-information` |
| CAP-04 التحليل والتقييم | 11 | 57 | 32 | `CAP-04-analysis` |
| CAP-05 الوعي بالموقف | 5 | 27 | 28 | `CAP-05-situation` |
| CAP-06 إدارة القرار | 5 | 26 | 12 | `CAP-06-decision` |
| CAP-07 التخطيط والتنفيذ | 11 | 65 | 46 | `CAP-07-planning-execution` |
| CAP-08 الموارد والجاهزية | 19 | 107 | 62 | `CAP-08-resources` |
| CAP-09 المخاطر والطوارئ | 5 | 22 | 13 | `CAP-09-risk-emergency` |
| CAP-10 الاتصال والمنتجات | 9 | 41 | 36 | `CAP-10-communication` |
| CAP-11 المعرفة والذاكرة المؤسسية | 9 | 50 | 36 | `CAP-11-knowledge` |
| CAP-12 المساعدة بالذكاء الاصطناعي | 11 | 45 | 45 | `CAP-12-ai` |
| CAP-13 الحوكمة والأمن والامتثال | 7 | 32 | 36 | `CAP-13-governance-security` |
| CAP-14 تشغيل المنصة | 8 | 3 | 73 | `CAP-14-platform-ops` |
| **المجموع** | **151** | **739** | **661** | — |

القصص حسب النوع: أمر 489، جلب 157، نظام 143، واجهة 254، منصة 196، تكامل 37، تشغيل 124.

## 2. الميزات حسب القدرة

### 2.1 CAP-01 — إدارة المؤسسة والوصول

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **[الهيكل التنظيمي](CAP-01-org-access/FEAT-ORG-STRUCTURE.md)** `FEAT-ORG-STRUCTURE` | CAP-01.01 إدارة المستأجرين والمؤسسات (R1) | يتيح للمسؤول بناء المؤسسة ووحداتها التنظيمية وتعديلها، ويمكّن كل مستخدم من رؤية شجرة المؤسسة. | مسؤول الإدارة؛ أي مستخدم مخوَّل | 9 + 3 |
| **[دورة حياة المستأجر](CAP-01-org-access/FEAT-ORG-TENANT-LIFECYCLE.md)** `FEAT-ORG-TENANT-LIFECYCLE` | CAP-01.01 إدارة المستأجرين والمؤسسات (R1) | يتيح لمشغل المنصة إنشاء مستأجر جديد معزول وجاهز للاستخدام ومتابعة حالته وتعليقه أو إعادته أو إخراجه من الخدمة بأمان. | مشغّل المنصة؛ مسؤول الإدارة؛ النظام | 9 + 10 |
| **[مزامنة تغييرات الموارد البشرية](CAP-01-org-access/FEAT-ORG-HR-SYNC.md)** `FEAT-ORG-HR-SYNC` | CAP-01.02 الهوية والمصادقة والاتحاد (R1) | يحوّل تغييرات الوظيفة أو الوحدة القادمة من نظام الموارد البشرية إلى مقترحات يعتمدها المسؤول أو يرفضها قبل أن تتغير صلاحيات أي شخص. | مسؤول الإدارة؛ مسؤول الأمن؛ النظام | 6 + 3 |
| **[سجل الأشخاص](CAP-01-org-access/FEAT-ORG-PERSONS.md)** `FEAT-ORG-PERSONS` | CAP-01.02 الهوية والمصادقة والاتحاد (R1) | يتيح للمسؤول تسجيل الأشخاص العاملين في المؤسسة وتحديث بياناتهم وإيقافهم أو إعادتهم بشكل مستقل عن حساباتهم. | مسؤول الإدارة | 4 + 3 |
| **[حسابات الخدمة للأنظمة](CAP-01-org-access/FEAT-ORG-SERVICE-ACCOUNTS.md)** `FEAT-ORG-SERVICE-ACCOUNTS` | CAP-01.02 الهوية والمصادقة والاتحاد (R1) | يتيح للمسؤول منح الأنظمة المتكاملة حسابات خاصة بها يمكن تعطيلها وتجديد بيانات اعتمادها وإغلاقها دون المساس بحسابات الأشخاص. | مسؤول الإدارة | 5 + 4 |
| **[الدخول الموحد وربط الهويات](CAP-01-org-access/FEAT-ORG-SIGN-IN.md)** `FEAT-ORG-SIGN-IN` | CAP-01.02 الهوية والمصادقة والاتحاد (R1) | يتيح للمستخدم الدخول بحسابه المؤسسي عبر مزود الهوية الخارجي دون كلمة مرور خاصة بالمنصة، ويتيح للمسؤول ربط الهويات الخارجية بالحساب. | أي مستخدم مخوَّل؛ مسؤول الإدارة؛ النظام | 3 + 8 |
| **[إدارة حسابات المستخدمين](CAP-01-org-access/FEAT-ORG-USER-ACCOUNTS.md)** `FEAT-ORG-USER-ACCOUNTS` | CAP-01.02 الهوية والمصادقة والاتحاد (R1) | يتيح للمسؤول ومسؤول الأمن إنشاء حسابات المستخدمين وتعطيلها وقفلها وإغلاقها والبحث فيها، مع بقائها متزامنة مع مزود الهوية. | مسؤول الإدارة؛ مسؤول الأمن؛ النظام؛ أي مستخدم مخوَّل | 9 + 5 |
| **[منح صلاحيات القرار](CAP-01-org-access/FEAT-ORG-AUTHORITY-GRANTS.md)** `FEAT-ORG-AUTHORITY-GRANTS` | CAP-01.03 السلطة والتفويض (R1) | يحدد بوضوح من يملك سلطة اتخاذ كل نوع من القرارات وفي أي نطاق وحدود ومدة، مع اعتماد المنح وتعليقه وسحبه وانتهائه تلقائيًا. | صاحب السلطة أو المعتمِد الثاني؛ القيادي التنفيذي؛ مسؤول الإدارة؛ النظام | 8 + 2 |
| **[تفويض السلطة والتحقق منها](CAP-01-org-access/FEAT-ORG-DELEGATION.md)** `FEAT-ORG-DELEGATION` | CAP-01.03 السلطة والتفويض (R1) | يتيح لصاحب السلطة تفويض جزء من سلطته لغيره لمدة محددة دون تجاوز حدوده، ويتيح للمنصة التأكد قبل أي قرار أن صاحبه مخوّل به. | صاحب السلطة أو المعتمِد الثاني؛ المفوَّض إليه؛ النظام | 2 + 2 |
| **[فحص الوصول قبل كل طلب](CAP-01-org-access/FEAT-ORG-ACCESS-ENFORCE.md)** `FEAT-ORG-ACCESS-ENFORCE` | CAP-01.04 سياسات الوصول (R1) | يضمن فحص كل عرض أو بحث أو تصدير أو طلب للخريطة أو للمساعد الذكي قبل جلب البيانات، فيُمنع أو يُحجب جزئيًا ما لا يحق للمستخدم رؤيته ويُرفض الطلب إذا تعذر الفحص. | أي مستخدم مخوَّل؛ النظام | 2 + 17 |
| **[إدارة سياسات الوصول](CAP-01-org-access/FEAT-ORG-ACCESS-POLICY.md)** `FEAT-ORG-ACCESS-POLICY` | CAP-01.04 سياسات الوصول (R1) | يتيح لمسؤول الأمن صياغة قواعد الوصول واختبارها وتقديمها للاعتماد ثم تطبيقها من تاريخ سريان محدد مع حفظ كل نسخة. | مسؤول الأمن؛ المدقِّق؛ النظام | 8 + 5 |
| **[إسناد الأدوار للمستخدمين](CAP-01-org-access/FEAT-ORG-ROLE-ASSIGNMENT.md)** `FEAT-ORG-ROLE-ASSIGNMENT` | CAP-01.04 سياسات الوصول (R1) | يتيح للمسؤول منح المستخدمين أدوارهم في نطاق محدد ولمدة محددة، وسحبها يدويًا أو تلقائيًا عند انتهاء مدتها. | مسؤول الإدارة؛ النظام | 3 + 1 |
| **[تعريف الأدوار وصلاحياتها](CAP-01-org-access/FEAT-ORG-ROLES.md)** `FEAT-ORG-ROLES` | CAP-01.04 سياسات الوصول (R1) | يتيح للمسؤول تعريف أدوار العمل وتحديد ما يسمح به كل دور من عرض وتعديل وتصدير واعتماد، وتفعيل الأدوار أو إحالتها للتقاعد. | مسؤول الإدارة | 4 + 2 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-01 (137)</summary>

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
  - `US-UI-SCR61-TREE-NAVIGATION` — تصفح شجرة المؤسسة متعددة المستويات (واجهة، جديدة)
  - `US-UI-SCR61-UNIT-ACTIONS` — نقل الوحدات وتعديلها من الشجرة (واجهة، جديدة)
  - `US-PLT-ORG-SCOPE-RESOLUTION` — حساب النطاق التنظيمي لصلاحيات الأدوار (منصة، جديدة)
- **دورة حياة المستأجر** `FEAT-ORG-TENANT-LIFECYCLE`
  - `US-BC01-TEN-COMPLETE-DECOMMISSION` — إكمال إخراج المستأجر من الخدمة (أمر)
  - `US-BC01-TEN-COMPLETE-PROVISIONING` — إكمال تهيئة المستأجر (أمر)
  - `US-BC01-TEN-FAIL-PROVISIONING` — تسجيل فشل تهيئة المستأجر (أمر)
  - `US-BC01-TEN-PROVISION` — تهيئة المستأجر (أمر)
  - `US-BC01-TEN-REACTIVATE` — إعادة تفعيل المستأجر (أمر)
  - `US-BC01-TEN-RETRY-PROVISIONING` — إعادة محاولة تهيئة المستأجر (أمر)
  - `US-BC01-TEN-START-DECOMMISSION` — بدء إخراج المستأجر من الخدمة (أمر)
  - `US-BC01-TEN-SUSPEND` — تعليق المستأجر (أمر)
  - `US-BC01-Q-TEN-GET` — جلب: Tenant state, cell, quotas (جلب)
  - `US-DOM-TEN-LIST` — عرض قائمة المستأجرين لمشغل المنصة (جلب، جديدة)
  - `US-UI-SCR60-PROVISIONING-PROGRESS` — متابعة خطوات تهيئة المستأجر وسبب فشلها (واجهة، جديدة)
  - `US-UI-SCR60-TENANT-ACTIONS` — أفعال المستأجر المتاحة حسب حالته (واجهة، جديدة)
  - `US-PLT-TENANT-CELL-BINDING` — رفض طلبات المستأجر من غير خليته (منصة، جديدة)
  - `US-PLT-TENANT-DECOMMISSION-PURGE` — محو كل بيانات المستأجر عند إخراجه (منصة، جديدة)
  - `US-PLT-TENANT-DEDICATED-CELL` — تشغيل المستأجر المخصص في خلية مستقلة (منصة، جديدة)
  - `US-PLT-TENANT-ISOLATION-LAYERS` — عزل بيانات كل مستأجر في كل طبقة (منصة، جديدة)
  - `US-PLT-TENANT-PROVISION-ATOMIC` — تهيئة مستأجر آلية ذرية خلال ساعة (منصة، جديدة)
  - `US-OPS-TENANT-ISOLATION-SUITE` — اختبار عزل المستأجرين في كل المسارات (تشغيل، جديدة)
  - `US-OPS-TENANT-PROVISION-ALERT` — تنبيه عند تأخر تهيئة المستأجر (تشغيل، جديدة)
- **مزامنة تغييرات الموارد البشرية** `FEAT-ORG-HR-SYNC`
  - `US-BC01-HRS-APPROVE` — اعتماد مقترح مزامنة الموارد البشرية (أمر)
  - `US-BC01-HRS-REJECT` — رفض مقترح مزامنة الموارد البشرية (أمر)
  - `US-BC01-Q-HRS-QUEUE` — جلب: Pending HR proposals by unit and change kind (leave first) (جلب)
  - `US-BC01-S-HR-SYNC-PROPOSAL-01` — تلقائي: HRIS change received (مقترح مزامنة الموارد البشرية) (نظام)
  - `US-BC01-S-HR-SYNC-PROPOSAL-02` — تلقائي: newer HR change for the same person (مقترح مزامنة الموارد البشرية) (نظام)
  - `US-BC01-S-HR-SYNC-PROPOSAL-03` — تلقائي: 14 days without decision (مقترح مزامنة الموارد البشرية) (نظام)
  - `US-UI-SCR06-HR-PROPOSALS` — مراجعة مقترحات الموارد البشرية بالمقارنة (واجهة، جديدة)
  - `US-INT-HRIS-CHANGE-PROPOSALS` — تحويل تغييرات الموارد البشرية إلى مقترحات (تكامل، جديدة)
  - `US-INT-HRIS-LEAVER-ESCALATION` — تصعيد مغادرة الموظف إلى المسؤول (تكامل، جديدة)
- **سجل الأشخاص** `FEAT-ORG-PERSONS`
  - `US-BC01-PER-DEACTIVATE` — إيقاف تفعيل الشخص (أمر)
  - `US-BC01-PER-REACTIVATE` — إعادة تفعيل الشخص (أمر)
  - `US-BC01-PER-REGISTER` — تسجيل الشخص (أمر)
  - `US-BC01-PER-UPDATE-DETAILS` — تحديث بيانات الشخص (أمر)
  - `US-DOM-PER-LIST` — عرض سجل الأشخاص والبحث فيه (جلب، جديدة)
  - `US-UI-SCR62-PERSON-LINKS` — عرض الشخص وهوياته وحساباته المرتبطة (واجهة، جديدة)
  - `US-INT-HRIS-PERSON-UPDATE` — تحديث بيانات الأشخاص من الموارد البشرية (تكامل، جديدة)
- **حسابات الخدمة للأنظمة** `FEAT-ORG-SERVICE-ACCOUNTS`
  - `US-BC01-SVC-CLOSE` — إغلاق حساب الخدمة (أمر)
  - `US-BC01-SVC-CREATE` — إنشاء حساب الخدمة (أمر)
  - `US-BC01-SVC-DISABLE` — تعطيل حساب الخدمة (أمر)
  - `US-BC01-SVC-ENABLE` — تمكين حساب الخدمة (أمر)
  - `US-BC01-SVC-ROTATE-CREDENTIAL` — تدوير بيانات اعتماد حساب الخدمة (أمر)
  - `US-DOM-SVC-LIST` — عرض حسابات الخدمة وحالة بيانات اعتمادها (جلب، جديدة)
  - `US-UI-SCR62-SERVICE-ACCOUNTS` — إدارة حسابات الخدمة وتجديد بيانات اعتمادها (واجهة، جديدة)
  - `US-INT-SVC-KEY-AUTHENTICATION` — مصادقة الأنظمة المتكاملة بمفتاح حساب الخدمة (تكامل، جديدة)
  - `US-OPS-SVC-CREDENTIAL-EXPIRY` — تنبيه قبل انتهاء بيانات اعتماد حساب الخدمة (تشغيل، جديدة)
- **الدخول الموحد وربط الهويات** `FEAT-ORG-SIGN-IN`
  - `US-BC01-USR-LINK-IDENTITY` — ربط هوية خارجية بـحساب المستخدم (أمر)
  - `US-BC01-USR-RECORD-FIRST-SIGN-IN` — تسجيل أول دخول لـحساب المستخدم (أمر)
  - `US-BC01-USR-UNLINK-IDENTITY` — فك ربط هوية خارجية عن حساب المستخدم (أمر)
  - `US-PLT-SIGNIN-MFA-STEPUP` — المصادقة المعززة دون فقد المدخلات (منصة، جديدة)
  - `US-PLT-SIGNIN-SESSION-LIFETIME` — إنهاء الجلسة بعد مدتها وتجديد الرمز (منصة، جديدة)
  - `US-INT-IDP-OIDC-FEDERATION` — الدخول عبر مزود هوية المستأجر بـOIDC (تكامل، جديدة)
  - `US-INT-IDP-SAML-FEDERATION` — الدخول عبر مزود هوية المستأجر بـSAML (تكامل، جديدة)
  - `US-OPS-IDP-HIGH-AVAILABILITY` — توفر وسيط الهوية دون انقطاع (تشغيل، جديدة)
  - `US-OPS-IDP-OUTAGE-BREAKGLASS` — تشغيل المنصة عند انقطاع مزود الهوية (تشغيل، جديدة)
  - `US-OPS-IDP-TENANT-SETUP` — ربط مزود هوية المستأجر بوسيط الخلية (تشغيل، جديدة)
  - `US-OPS-SIGNIN-BRUTE-FORCE` — كشف محاولات الدخول الفاشلة المتكررة (تشغيل، جديدة)
- **إدارة حسابات المستخدمين** `FEAT-ORG-USER-ACCOUNTS`
  - `US-BC01-USR-CLOSE` — إغلاق حساب المستخدم (أمر)
  - `US-BC01-USR-DISABLE` — تعطيل حساب المستخدم (أمر)
  - `US-BC01-USR-ENABLE` — تمكين حساب المستخدم (أمر)
  - `US-BC01-USR-LINK-PERSON` — ربط شخص بـحساب المستخدم (أمر)
  - `US-BC01-USR-LOCK` — قفل حساب المستخدم (أمر)
  - `US-BC01-USR-PROVISION` — تهيئة حساب المستخدم (أمر)
  - `US-BC01-USR-UNLOCK` — فتح قفل حساب المستخدم (أمر)
  - `US-BC01-Q-USR-GET` — جلب: User with identities (no secrets) (جلب)
  - `US-BC01-Q-USR-LIST` — جلب: Users filtered by state, unit, role (جلب)
  - `US-UI-SCR62-USER-ACTIONS` — أفعال الحساب المتاحة حسب الحالة والدور (واجهة، جديدة)
  - `US-UI-SCR62-USER-LIST` — البحث في المستخدمين وتصفيتهم حسب الحالة (واجهة، جديدة)
  - `US-INT-SCIM-DEPROVISIONING` — تعطيل الحساب من مزود الهوية خلال خمس دقائق (تكامل، جديدة)
  - `US-INT-SCIM-PROVISIONING` — استقبال إنشاء الحسابات من مزود الهوية (تكامل، جديدة)
  - `US-OPS-SCIM-SYNC-ALERT` — تنبيه عند تأخر مزامنة الحسابات (تشغيل، جديدة)
- **منح صلاحيات القرار** `FEAT-ORG-AUTHORITY-GRANTS`
  - `US-BC01-AUT-APPROVE-GRANT` — اعتماد منح السلطة (أمر)
  - `US-BC01-AUT-GRANT` — إصدار منح السلطة (أمر)
  - `US-BC01-AUT-REJECT-GRANT` — رفض منح السلطة (أمر)
  - `US-BC01-AUT-RESUME` — استئناف منح السلطة (أمر)
  - `US-BC01-AUT-REVOKE` — سحب منح السلطة (أمر)
  - `US-BC01-AUT-SUSPEND` — تعليق منح السلطة (أمر)
  - `US-BC01-Q-AUT-LIST` — جلب: Grants by holder / scope / effective at t (جلب)
  - `US-BC01-S-AUTHORITY-GRANT-01` — تلقائي: valid_to reached (منح السلطة) (نظام)
  - `US-UI-SCR62-AUTHORITY-GRANTS` — عرض منح السلطة بنطاقها وحدودها ومدتها (واجهة، جديدة)
  - `US-PLT-AUT-READTIME-VALIDITY` — فرض انتهاء السلطة لحظة التحقق (منصة، جديدة)
- **تفويض السلطة والتحقق منها** `FEAT-ORG-DELEGATION`
  - `US-BC01-AUT-DELEGATE` — تفويض منح السلطة (أمر)
  - `US-BC01-Q-AUT-CHECK` — جلب: AuthorityCheck(actor, decision_type, scope, at, amount?) (جلب)
  - `US-UI-SCR05-ACTING-AUTHORITY` — إظهار سلطة المفوَّض إليه عند القرار (واجهة، جديدة)
  - `US-UI-SCR62-DELEGATION-FORM` — تفويض السلطة ضمن حدود المفوِّض الظاهرة (واجهة، جديدة)
- **فحص الوصول قبل كل طلب** `FEAT-ORG-ACCESS-ENFORCE`
  - `US-BC01-Q-SEC-CONTEXT` — جلب: Caller's resolved SecurityContext (جلب)
  - `US-BC08-Q-PDP-DECIDE` — جلب: DecisionRequest → DecisionResponse (authorization-model §2) (جلب)
  - `US-PLT-ACCESS-ALLOWED-ACTIONS` — إرجاع الأفعال المسموحة مع تفاصيل المورد (منصة، جديدة)
  - `US-PLT-ACCESS-DECISION-CACHE` — نفاذ سحب الصلاحية في الطلب التالي (منصة، جديدة)
  - `US-PLT-ACCESS-FAIL-CLOSED` — رفض الطلب عند تعذر فحص الصلاحية (منصة، جديدة)
  - `US-PLT-ACCESS-OBLIGATIONS` — تطبيق التزامات قرار الوصول (منصة، جديدة)
  - `US-PLT-ACCESS-PDP-PERFORMANCE` — قرار الصلاحية خلال خمسة أجزاء من الثانية (منصة، جديدة)
  - `US-PLT-ACCESS-PEP-EVERY-PATH` — فحص الصلاحية قبل أي استرجاع للبيانات (منصة، جديدة)
  - `US-PLT-ACCESS-QUERY-PREFILTER` — تصفية النتائج دون كشف المحجوب (منصة، جديدة)
  - `US-PLT-ACCESS-SECURITY-CONTEXT` — سياق أمني موقّع يرافق كل طلب (منصة، جديدة)
  - `US-PLT-ACCESS-SHARED-CACHE` — منع مشاركة النتائج المخزنة بين المستخدمين (منصة، جديدة)
  - `US-PLT-ACCESS-STALE-BUNDLE` — تقييد العمل عند تقادم حزمة السياسات (منصة، جديدة)
  - `US-PLT-ACCESS-UI-DENIALS` — عرض الرفض دون كشف وجود المورد (منصة، جديدة)
  - `US-PLT-ACCESS-UI-LOCAL-STORAGE` — منع حفظ البيانات الحساسة في المتصفح (منصة، جديدة)
  - `US-PLT-ACCESS-UI-NAVIGATION` — إظهار مناطق الواجهة حسب صلاحيات المستخدم (منصة، جديدة)
  - `US-PLT-ACCESS-UI-REDACTION` — علامة ثابتة للحقل المحجوب (منصة، جديدة)
  - `US-OPS-ACCESS-INFERENCE-SUITE` — اختبار عدم الاستدلال واختبار الاختراق (تشغيل، جديدة)
  - `US-OPS-ACCESS-MTLS-IDENTITY` — اتصال مشفر بهوية خاصة لكل خدمة (تشغيل، جديدة)
  - `US-OPS-ACCESS-PDP-ALERTS` — تنبيهات أداء محرك السياسات وقفزات الرفض (تشغيل، جديدة)
- **إدارة سياسات الوصول** `FEAT-ORG-ACCESS-POLICY`
  - `US-BC08-POL-APPROVE` — اعتماد مجموعة السياسات (أمر)
  - `US-BC08-POL-DRAFT` — إعداد مسودة مجموعة السياسات (أمر)
  - `US-BC08-POL-EDIT` — تعديل مجموعة السياسات (أمر)
  - `US-BC08-POL-REJECT` — رفض مجموعة السياسات (أمر)
  - `US-BC08-POL-SUBMIT` — تقديم مجموعة السياسات (أمر)
  - `US-BC08-Q-POL-GET` — جلب: Policy set version with tables and tests (جلب)
  - `US-DOM-POL-HISTORY` — عرض تاريخ نسخ السياسات وأزمنة سريانها (جلب، جديدة)
  - `US-BC08-S-POLICY-SET-01` — تلقائي: effective_from reached (مجموعة السياسات) (نظام)
  - `US-BC08-S-POLICY-SET-02` — تلقائي: successor activated (مجموعة السياسات) (نظام)
  - `US-UI-SCR68-POLICY-TESTS` — عرض جداول القرار ونتائج اختباراتها (واجهة، جديدة)
  - `US-UI-SCR68-VERSION-COMPARE` — مقارنة نسخ السياسة وموعد سريانها (واجهة، جديدة)
  - `US-PLT-POL-BUNDLE-DISTRIBUTION` — توزيع حزمة السياسات الموقعة على المقيّمين (منصة، جديدة)
  - `US-OPS-POL-ATTRIBUTE-MATRIX` — اختبار أثر كل سمة على قرار الوصول (تشغيل، جديدة)
- **إسناد الأدوار للمستخدمين** `FEAT-ORG-ROLE-ASSIGNMENT`
  - `US-BC01-RAS-ASSIGN` — تسجيل إسناد الدور (أمر)
  - `US-BC01-RAS-REVOKE` — سحب إسناد الدور (أمر)
  - `US-BC01-S-ROLE-ASSIGNMENT-01` — تلقائي: valid_to reached (إسناد الدور) (نظام)
  - `US-UI-SCR62-ROLE-ASSIGNMENTS` — إسناد الأدوار بنطاق ومدة ومتابعة انتهائها (واجهة، جديدة)
- **تعريف الأدوار وصلاحياتها** `FEAT-ORG-ROLES`
  - `US-BC01-ROL-ACTIVATE` — تفعيل الدور (أمر)
  - `US-BC01-ROL-DEFINE` — تعريف الدور (أمر)
  - `US-BC01-ROL-RETIRE` — إحالة الدور إلى التقاعد (أمر)
  - `US-BC01-ROL-SET-PERMISSIONS` — تحديد صلاحيات الدور (أمر)
  - `US-DOM-ROL-LIST` — عرض الأدوار وصلاحياتها (جلب، جديدة)
  - `US-UI-SCR62-PERMISSION-MATRIX` — ضبط الصلاحيات الثماني للدور منفصلة (واجهة، جديدة)

</details>

### 2.2 CAP-02 — جمع المعلومات

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **[متابعة استيفاء المتطلبات](CAP-02-collection/FEAT-COL-FULFILMENT.md)** `FEAT-COL-FULFILMENT` | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) | يعرض لوحة بالمتطلبات المفتوحة ومدى استيفائها والملاحظات التي أجابت عنها وينبه عند فوات موعدها. | مدير الجمع؛ المحلل؛ النظام | 4 + 3 |
| **[تخطيط أنشطة الجمع](CAP-02-collection/FEAT-COL-PLAN.md)** `FEAT-COL-PLAN` | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) | يتيح لمخطط الجمع أن يحول المتطلب المعتمد إلى خطة أنشطة ومصادر ومهام ميدانية ويتابعها حتى الاكتمال. | مخطط الجمع؛ النظام | 8 + 3 |
| **[اعتماد متطلبات الجمع](CAP-02-collection/FEAT-COL-REQ-APPROVAL.md)** `FEAT-COL-REQ-APPROVAL` | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) | يتيح لمدير الجمع أن يقبل أو يرفض أو يعدل طلبات المعلومات قبل توجيه جهد الجمع إليها. | مدير الجمع | 3 + 1 |
| **[طلب حاجة معلوماتية](CAP-02-collection/FEAT-COL-REQ-REQUEST.md)** `FEAT-COL-REQ-REQUEST` | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) | يتيح للمحلل أن يصوغ سؤاله المعلوماتي ومنطقته وموعده ويقدمه للجمع ثم يتابعه حتى يستوفى أو يلغى. | المحلل؛ مقدم الطلب | 6 + 2 |
| **[حماية هوية المصادر](CAP-02-collection/FEAT-COL-SOURCE-PROTECT.md)** `FEAT-COL-SOURCE-PROTECT` | CAP-02.02 إدارة المصادر (R1) | يتيح لمسؤول الأمن تحديد مستوى حماية المصدر وتصنيفه بحيث لا يرى هويته إلا المخولون. | مسؤول الأمن | 2 + 2 |
| **[سجل المصادر وموثوقيتها](CAP-02-collection/FEAT-COL-SOURCES.md)** `FEAT-COL-SOURCES` | CAP-02.02 إدارة المصادر (R1) | يحفظ لكل مصدر ملفه ونوعه وتقدير موثوقيته عبر الزمن ويتيح تعليقه أو إحالته إلى التقاعد. | المحلل | 7 + 3 |
| **[رفع المرفقات وتنزيلها](CAP-02-collection/FEAT-COL-ATTACHMENTS.md)** `FEAT-COL-ATTACHMENTS` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح رفع الصور والمستندات والفيديو بأمان مع فحصها والتحقق من سلامتها وتنزيلها للمخولين فقط. | أي مستخدم مخوَّل؛ النظام | 7 + 9 |
| **[إدارة الأجهزة الميدانية](CAP-02-collection/FEAT-COL-DEVICES.md)** `FEAT-COL-DEVICES` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح تسجيل الأجهزة الميدانية واعتمادها وتعليقها وتدوير مفاتيحها حتى لا يعمل في الميدان إلا جهاز موثوق. | المستخدم الميداني؛ مسؤول الإدارة؛ مسؤول الأمن | 7 + 5 |
| **[حفظ الأدلة وسلسلة العهدة](CAP-02-collection/FEAT-COL-EVIDENCE.md)** `FEAT-COL-EVIDENCE` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يحفظ الدليل وموقعه ويختمه ويسجل كل نقل لعهدته حتى يبقى موثوقًا ومقبولًا. | المحلل؛ المستخدم الميداني؛ أمين العهدة | 7 + 4 |
| **[المزامنة الميدانية](CAP-02-collection/FEAT-COL-FIELD-SYNC.md)** `FEAT-COL-FIELD-SYNC` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | ينقل ما سجله المستخدم الميداني دون اتصال إلى الخادم بترتيبه الأصلي دون تكرار ويجلب له آخر تحديثات مهامه. | المستخدم الميداني؛ النظام | 6 + 6 |
| **[الإبلاغ عن جهاز مفقود](CAP-02-collection/FEAT-COL-LOST-DEVICE.md)** `FEAT-COL-LOST-DEVICE` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح الإبلاغ عن فقد الجهاز فيمنع مزامنته ويمسح بياناته عن بعد حماية للمعلومات. | المستخدم الميداني؛ مسؤول الإدارة؛ النظام | 3 + 3 |
| **[التحقق من الملاحظات](CAP-02-collection/FEAT-COL-OBS-REVIEW.md)** `FEAT-COL-OBS-REVIEW` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح للمحلل اعتماد الملاحظة أو رفضها أو إعادة تصنيفها قبل أن تعتمد عليها التحليلات. | المحلل | 3 + 1 |
| **[تسجيل الملاحظات](CAP-02-collection/FEAT-COL-OBSERVATIONS.md)** `FEAT-COL-OBSERVATIONS` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح للمستخدم الميداني والمحلل تسجيل ما رصده في زمان ومكان محددين مع مرفقاته وتصحيحه بإصدار جديد والبحث فيه. | المستخدم الميداني؛ المشغِّل؛ المحلل؛ النظام | 5 + 6 |
| **[العمل الميداني دون اتصال](CAP-02-collection/FEAT-COL-OFFLINE-WORK.md)** `FEAT-COL-OFFLINE-WORK` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يبقى الجهاز الميداني صالحًا للعمل حتى 72 ساعة دون شبكة، ببيانات مشفرة عليه تُمسح عن بعد إن فُقد. | المستخدم الميداني | 0 + 9 |
| **[تحميل بيانات المنطقة مسبقًا](CAP-02-collection/FEAT-COL-PRELOAD.md)** `FEAT-COL-PRELOAD` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يتيح للمستخدم الميداني تنزيل بيانات منطقة عمله المصرح بها قبل الخروج لتعمل دون اتصال وتنتهي صلاحيتها تلقائيًا. | المستخدم الميداني؛ مسؤول الإدارة؛ مسؤول الأمن؛ النظام | 8 + 6 |
| **[حل تعارضات المزامنة](CAP-02-collection/FEAT-COL-SYNC-CONFLICTS.md)** `FEAT-COL-SYNC-CONFLICTS` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) | يعرض على المراجع ما تعارض من تسجيلات ميدانية مع الوضع الحالي ليقرر إعادة تطبيقها أو إسقاطها أو حلها يدويًا. | المخطِّط؛ المحلل؛ النظام | 7 + 2 |
| **[إدارة محوّلات البيانات](CAP-02-collection/FEAT-COL-ADAPTERS.md)** `FEAT-COL-ADAPTERS` | CAP-02.04 الاستيعاب والتكامل (R1) | يتيح للمسؤول تسجيل محوّلات البيانات الخارجية وربط حقولها وتفعيلها بموافقة مسؤول ثان. | مسؤول الإدارة | 7 + 6 |
| **[اتصالات الأنظمة الخارجية](CAP-02-collection/FEAT-COL-CONNECTIONS.md)** `FEAT-COL-CONNECTIONS` | CAP-02.04 الاستيعاب والتكامل (R1) | يتيح لمهندس التكامل تسجيل الاتصال بالأنظمة الخارجية واختباره ومراقبة سلامته مع اعتماد أمني قبل تشغيله. | مهندس التكامل؛ مسؤول الأمن؛ مسؤول الإدارة؛ النظام | 10 + 5 |
| **[التكامل مع أنظمة المؤسسة](CAP-02-collection/FEAT-COL-ENTERPRISE-INT.md)** `FEAT-COL-ENTERPRISE-INT` | CAP-02.04 الاستيعاب والتكامل (R1) | يربط أنظمة الموارد البشرية والمالية وإدارة الوثائق بالمنصة دون أن تصبح مرجعًا للحقيقة. | مهندس التكامل؛ مسؤول الإدارة | 0 + 4 |
| **[استيراد الخرائط والطقس](CAP-02-collection/FEAT-COL-GEO-WEATHER.md)** `FEAT-COL-GEO-WEATHER` | CAP-02.04 الاستيعاب والتكامل (R1) | يتيح جلب الطبقات الجغرافية وبيانات الطقس من مزوديها المعتمدين لتظهر في الصورة العملياتية. | مسؤول الإدارة؛ مهندس التكامل | 0 + 8 |
| **[استيراد البيانات والحجر](CAP-02-collection/FEAT-COL-IMPORT.md)** `FEAT-COL-IMPORT` | CAP-02.04 الاستيعاب والتكامل (R1) | يتيح استيراد دفعات بيانات خارجية مع عزل السجلات المعيبة ومعالجتها قبل نشرها. | مسؤول الإدارة؛ النظام | 9 + 5 |
| **[تدفقات الحساسات](CAP-02-collection/FEAT-COL-SENSORS.md)** `FEAT-COL-SENSORS` | CAP-02.04 الاستيعاب والتكامل (R1) | يتيح ربط تدفقات الحساسات وتحديد قواعد جودتها والتنبيه عند انقطاع بياناتها. | مهندس التكامل؛ المحلل؛ النظام | 7 + 4 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-02 (213)</summary>

- **متابعة استيفاء المتطلبات** `FEAT-COL-FULFILMENT`
  - `US-BC02-Q-CRQ-BOARD` — جلب: Requirements by area (bbox/polygon), state, priority, due (جلب)
  - `US-BC02-Q-CRQ-EVIDENCE` — جلب: Fulfilment links per EEI (visible observations only) with lineage (جلب)
  - `US-BC02-S-COLLECTION-REQUIREMENT-01` — تلقائي: validated observation matched (متطلب الجمع) (نظام)
  - `US-BC02-S-COLLECTION-REQUIREMENT-02` — تلقائي: due passed (متطلب الجمع) (نظام)
  - `US-UI-SCR13-BOARD-MAP` — لوحة مكانية للمتطلبات المفتوحة حسب الأولوية والموعد (واجهة، جديدة)
  - `US-UI-SCR13-FULFILMENT-EEI` — عرض استيفاء كل عنصر معلومات بملاحظاته (واجهة، جديدة)
  - `US-PLT-CRQ-MATCH-INDEX` — مطابقة الملاحظات المعتمدة مع مناطق المتطلبات بسرعة (منصة، جديدة)
- **تخطيط أنشطة الجمع** `FEAT-COL-PLAN`
  - `US-BC02-CPL-ACTIVATE` — تفعيل خطة الجمع (أمر)
  - `US-BC02-CPL-ADD-ACTIVITY` — إضافة نشاط إلى خطة الجمع (أمر)
  - `US-BC02-CPL-CANCEL` — إلغاء خطة الجمع (أمر)
  - `US-BC02-CPL-COMPLETE` — إكمال خطة الجمع (أمر)
  - `US-BC02-CPL-CREATE` — إنشاء خطة الجمع (أمر)
  - `US-BC02-CPL-REMOVE-ACTIVITY` — إزالة نشاط من خطة الجمع (أمر)
  - `US-BC02-Q-CPL-GET` — جلب: Plan with activities and linked tasks (جلب)
  - `US-BC02-S-COLLECTION-PLAN-01` — تلقائي: all activity tasks terminal (خطة الجمع) (نظام)
  - `US-UI-SCR13-PLAN-EDITOR` — إعداد خطة الجمع وأنشطتها على الخريطة (واجهة، جديدة)
  - `US-UI-SCR13-PLAN-PROGRESS` — متابعة مهام أنشطة الخطة حتى اكتمالها (واجهة، جديدة)
  - `US-PLT-CPL-TASK-SPAWN` — إنشاء مهام الأنشطة مرة واحدة دون تكرار (منصة، جديدة)
- **اعتماد متطلبات الجمع** `FEAT-COL-REQ-APPROVAL`
  - `US-BC02-CRQ-AMEND` — تعديل متطلب الجمع بإصدار جديد (أمر)
  - `US-BC02-CRQ-APPROVE` — اعتماد متطلب الجمع (أمر)
  - `US-BC02-CRQ-REJECT` — رفض متطلب الجمع (أمر)
  - `US-UI-SCR13-CRQ-REVIEW` — مراجعة الطلبات المقدمة واعتمادها أو رفضها (واجهة، جديدة)
- **طلب حاجة معلوماتية** `FEAT-COL-REQ-REQUEST`
  - `US-BC02-CRQ-CANCEL` — إلغاء متطلب الجمع (أمر)
  - `US-BC02-CRQ-DRAFT` — إعداد مسودة متطلب الجمع (أمر)
  - `US-BC02-CRQ-EDIT` — تعديل متطلب الجمع (أمر)
  - `US-BC02-CRQ-MARK-SATISFIED` — تعليم متطلب الجمع كمستوفى (أمر)
  - `US-BC02-CRQ-SUBMIT` — تقديم متطلب الجمع (أمر)
  - `US-BC02-Q-CRQ-GET` — جلب: Requirement with EEIs and fulfilment computed over observations visible to the caller (جلب)
  - `US-UI-SCR13-CRQ-FORM` — صياغة طلب الجمع برسم المنطقة وعناصر المعلومات (واجهة، جديدة)
  - `US-UI-SCR13-MY-REQUESTS` — متابعة مقدم الطلب لطلباته وحالة استيفائها (واجهة، جديدة)
- **حماية هوية المصادر** `FEAT-COL-SOURCE-PROTECT`
  - `US-BC02-SRC-RECLASSIFY` — إعادة تصنيف المصدر (أمر)
  - `US-BC02-SRC-SET-PROTECTION` — تحديد مستوى حماية المصدر (أمر)
  - `US-UI-SCR22-SOURCE-REDACTED` — إخفاء هوية المصدر المحمي في الشاشة (واجهة، جديدة)
  - `US-PLT-SRCPROT-NO-LEAK` — منع تسرب هوية المصدر المحمي من أي مسار (منصة، جديدة)
- **سجل المصادر وموثوقيتها** `FEAT-COL-SOURCES`
  - `US-BC02-SRC-RATE-RELIABILITY` — تقدير موثوقية المصدر (أمر)
  - `US-BC02-SRC-REGISTER` — تسجيل المصدر (أمر)
  - `US-BC02-SRC-REINSTATE` — إعادة المصدر إلى السريان (أمر)
  - `US-BC02-SRC-RETIRE` — إحالة المصدر إلى التقاعد (أمر)
  - `US-BC02-SRC-SUSPEND` — تعليق المصدر (أمر)
  - `US-BC02-SRC-UPDATE-PROFILE` — تحديث ملف المصدر (أمر)
  - `US-BC02-Q-SRC-GET` — جلب: Source; identity only with source-protection permission (جلب)
  - `US-DOM-SRC-LIST` — عرض سجل المصادر وتصفيته (جلب، جديدة)
  - `US-UI-SCR22-SOURCE-LIST` — تصفح المصادر حسب النوع والحالة والموثوقية (واجهة، جديدة)
  - `US-UI-SCR22-SOURCE-PROFILE` — ملف المصدر وتاريخ تقديرات موثوقيته (واجهة، جديدة)
- **رفع المرفقات وتنزيلها** `FEAT-COL-ATTACHMENTS`
  - `US-BC02-ATT-COMPLETE-UPLOAD` — إكمال رفع المرفق (أمر)
  - `US-BC02-ATT-ERASE` — محو المرفق (أمر)
  - `US-BC02-ATT-INITIATE-UPLOAD` — بدء رفع المرفق (أمر)
  - `US-BC02-Q-ATT-DOWNLOAD` — جلب: Short-lived signed download target (≤ 5 min); audited (جلب)
  - `US-BC02-S-ATTACHMENT-01` — تلقائي: scan passed (المرفق) (نظام)
  - `US-BC02-S-ATTACHMENT-02` — تلقائي: scan failed (المرفق) (نظام)
  - `US-BC02-S-ATTACHMENT-03` — تلقائي: upload window 24 h elapsed (المرفق) (نظام)
  - `US-UI-SCR22-SAFE-VIEWER` — معاينة المرفق في عارض معزول (واجهة، جديدة)
  - `US-UI-SCR23-UPLOAD-STATE` — متابعة رفع المرفق وفحصه حتى إتاحته (واجهة، جديدة)
  - `US-PLT-ATT-CONTENT-SCANNER` — فحص المرفقات محليًا قبل إتاحتها (منصة، جديدة)
  - `US-PLT-ATT-DIRECT-UPLOAD` — رفع المرفقات مباشرة إلى مخزن الكائنات (منصة، جديدة)
  - `US-PLT-ATT-INTEGRITY-CHECK` — التحقق من بصمة المرفق عند كل استرجاع (منصة، جديدة)
  - `US-PLT-ATT-STORE-DEGRADED` — استمرار التسجيل عند تعطل مخزن الكائنات (منصة، جديدة)
  - `US-OPS-ATT-QUARANTINE-REVIEW` — مراجعة أمنية لكل مرفق محجور (تشغيل، جديدة)
  - `US-OPS-ATT-SCANNER-BACKLOG` — التنبيه عند تأخر فحص المرفقات (تشغيل، جديدة)
  - `US-OPS-ATT-SCANNER-SIGNATURES` — تحديث تواقيع الماسح في بيئة معزولة (تشغيل، جديدة)
- **إدارة الأجهزة الميدانية** `FEAT-COL-DEVICES`
  - `US-BC01-DEV-CONFIRM` — تأكيد الجهاز الميداني (أمر)
  - `US-BC01-DEV-ENROLL` — تسجيل الجهاز الميداني (أمر)
  - `US-BC01-DEV-REINSTATE` — إعادة الجهاز الميداني إلى السريان (أمر)
  - `US-BC01-DEV-RETIRE` — إحالة الجهاز الميداني إلى التقاعد (أمر)
  - `US-BC01-DEV-ROTATE-KEY` — تدوير مفتاح الجهاز الميداني (أمر)
  - `US-BC01-DEV-SUSPEND` — تعليق الجهاز الميداني (أمر)
  - `US-BC01-Q-DEV-LIST` — جلب: Devices of a user (self) or in scope (Administrator) (جلب)
  - `US-UI-SCR63-DEVICE-LIST` — قائمة الأجهزة وحالتها وآخر مزامنة (واجهة، جديدة)
  - `US-UI-SCR63-ENROLL-CONFIRM` — تأكيد تسجيل جهاز جديد بعد التحقق منه (واجهة، جديدة)
  - `US-PLT-DEVICE-ATTESTATION` — مفتاح جهاز عتادي غير قابل للتصدير مع إثبات (منصة، جديدة)
  - `US-INT-MDM-COMPLIANCE` — قبول الجهاز بناءً على امتثال إدارة الأجهزة (تكامل، جديدة)
  - `US-OPS-FIELDAPP-RELEASE` — توزيع إصدارات التطبيق الميداني الموقّعة (تشغيل، جديدة)
- **حفظ الأدلة وسلسلة العهدة** `FEAT-COL-EVIDENCE`
  - `US-BC02-EVD-RECLASSIFY` — إعادة تصنيف الدليل (أمر)
  - `US-BC02-EVD-REGISTER` — تسجيل الدليل (أمر)
  - `US-BC02-EVD-SEAL` — ختم الدليل (أمر)
  - `US-BC02-EVD-TRANSFER-CUSTODY` — نقل عهدة الدليل (أمر)
  - `US-BC02-EVD-UPDATE-LOCATOR` — تحديث محدِّد موقع الدليل (أمر)
  - `US-BC02-EVD-WITHDRAW` — سحب الدليل (أمر)
  - `US-BC02-Q-EVD-GET` — جلب: Evidence metadata and custody chain (جلب)
  - `US-UI-SCR22-CUSTODY-CHAIN` — عرض سلسلة عهدة الدليل وحالة ختمه (واجهة، جديدة)
  - `US-PLT-EVD-SEAL-VERIFY` — كشف أي تعديل على الدليل بعد ختمه (منصة، جديدة)
  - `US-OPS-EVD-FIXITY-CHECK` — فحص دوري لسلامة الأدلة المختومة (تشغيل، جديدة)
  - `US-OPS-EVD-INTEGRITY-INCIDENT` — الاستجابة لاكتشاف دليل تالف (تشغيل، جديدة)
- **المزامنة الميدانية** `FEAT-COL-FIELD-SYNC`
  - `US-BC07-SYN-OPEN` — فتح جلسة المزامنة (أمر)
  - `US-BC07-SYN-UPLOAD-BATCH` — رفع دفعة إلى جلسة المزامنة (أمر)
  - `US-BC07-Q-SYN-DELTA` — جلب: Server → device: my task changes, package updates, purge list, conflict notices, wipe/stop instruction (جلب)
  - `US-BC07-S-SYNC-SESSION-02` — تلقائي: all uploaded commands processed without conflict (جلسة المزامنة) (نظام)
  - `US-BC07-S-SYNC-SESSION-03` — تلقائي: all processed with ≥ 1 sync conflict (جلسة المزامنة) (نظام)
  - `US-BC07-S-SYNC-SESSION-04` — تلقائي: idle timeout (5 min) or transport loss (جلسة المزامنة) (نظام)
  - `US-UI-SCR01-SYNC-DETAILS` — شاشة المزامنة وتقدمها وما بقي معلقًا (واجهة، جديدة)
  - `US-PLT-SYNC-GATEWAY-SCALE` — استيعاب عودة آلاف الأجهزة معًا (منصة، جديدة)
  - `US-PLT-SYNC-IDEMPOTENCY-STORE` — عدم تكرار الأوامر مهما انقطعت المزامنة (منصة، جديدة)
  - `US-PLT-SYNC-THROUGHPUT` — مزامنة ألف أمر خلال عشر دقائق (منصة، جديدة)
  - `US-OPS-SYNC-HEALTH-ALERTS` — مراقبة زمن المزامنة وانحراف ساعات الأجهزة (تشغيل، جديدة)
  - `US-OPS-SYNC-SIGNATURE-INCIDENT` — معاملة فشل توقيع الأوامر كحادث أمني (تشغيل، جديدة)
- **الإبلاغ عن جهاز مفقود** `FEAT-COL-LOST-DEVICE`
  - `US-BC01-DEV-REPORT-LOST` — الإبلاغ عن فقد الجهاز الميداني (أمر)
  - `US-BC01-S-DEVICE-01` — تلقائي: wipe confirmed by device (الجهاز الميداني) (نظام)
  - `US-BC07-S-SYNC-SESSION-01` — تلقائي: device LOST or SUSPENDED at handshake (جلسة المزامنة) (نظام)
  - `US-UI-SCR63-REPORT-LOST` — الإبلاغ عن فقد جهاز ومتابعة مسحه (واجهة، جديدة)
  - `US-PLT-LOST-DEVICE-TOKEN-REVOKE` — إبطال جلسات الجهاز المفقود فورًا (منصة، جديدة)
  - `US-OPS-LOST-DEVICE-REVIEW` — مراجعة أمنية لكل جهاز مفقود (تشغيل، جديدة)
- **التحقق من الملاحظات** `FEAT-COL-OBS-REVIEW`
  - `US-BC02-OBS-RECLASSIFY` — إعادة تصنيف الملاحظة (أمر)
  - `US-BC02-OBS-REJECT` — رفض الملاحظة (أمر)
  - `US-BC02-OBS-VALIDATE` — التحقق من الملاحظة (أمر)
  - `US-UI-SCR23-VALIDATION-QUEUE` — طابور الملاحظات المنتظرة للتحقق (واجهة، جديدة)
- **تسجيل الملاحظات** `FEAT-COL-OBSERVATIONS`
  - `US-BC02-OBS-AMEND` — تعديل الملاحظة بإصدار جديد (أمر)
  - `US-BC02-OBS-ATTACH-EVIDENCE` — إرفاق دليل بـالملاحظة (أمر)
  - `US-BC02-OBS-RECORD` — تسجيل الملاحظة (أمر)
  - `US-BC02-Q-OBS-GET` — جلب: Observation with measurements and attachment refs (جلب)
  - `US-BC02-Q-OBS-LIST` — جلب: Observations by bbox, time window (mandatory, ≤ 31 days), source, state (جلب)
  - `US-UI-SCR23-LOCATION-QUALITY` — عرض دقة الموقع وأعلام جودة الملاحظة (واجهة، جديدة)
  - `US-UI-SCR23-OBS-LIST` — تصفح الملاحظات بنافذة زمنية ومنطقة (واجهة، جديدة)
  - `US-UI-SCR23-QUICK-CAPTURE` — تسجيل ملاحظة بصورة بيد واحدة (واجهة، جديدة)
  - `US-PLT-OBS-SEARCHABLE` — ظهور الملاحظة في البحث خلال 30 ثانية (منصة، جديدة)
  - `US-PLT-OBS-VOLUME` — ثبات الأداء مع مليار ملاحظة (منصة، جديدة)
  - `US-OPS-OBS-SOURCE-SILENCE` — التنبيه عند صمت مصادر الملاحظات (تشغيل، جديدة)
- **العمل الميداني دون اتصال** `FEAT-COL-OFFLINE-WORK`
  - `US-UI-SCR23-OFFLINE-STALE` — التسجيل بعد 72 ساعة دون عرض المحمّل (واجهة، جديدة)
  - `US-UI-SCR23-OFFLINE-STATUS` — حالة إرسال كل ملاحظة ومرفق دون اتصال (واجهة، جديدة)
  - `US-PLT-DEVICE-STORE` — المخزن المحلي المشفر والمسح عن بعد (منصة، جديدة)
  - `US-PLT-OFFLINE-ATTACH-STORE` — حفظ صور الميدان مشفرة حتى رفعها (منصة، جديدة)
  - `US-PLT-OFFLINE-CAPACITY` — سعة الجهاز لعمل 72 ساعة دون اتصال (منصة، جديدة)
  - `US-PLT-OFFLINE-COMMAND-QUEUE` — طابور أوامر موقّع ومتسلسل على الجهاز (منصة، جديدة)
  - `US-PLT-OFFLINE-QUEUE-BACKUP` — نسخ احتياطي مشفر لطابور الجهاز (منصة، جديدة)
  - `US-PLT-OFFLINE-TIME-LIMIT` — استمرار الالتقاط بعد 72 ساعة وإيقاف القراءة (منصة، جديدة)
  - `US-OPS-OFFLINE-DEVICE-TEST` — اختبار العمل دون اتصال على أجهزة حقيقية (تشغيل، جديدة)
- **تحميل بيانات المنطقة مسبقًا** `FEAT-COL-PRELOAD`
  - `US-BC07-PKG-CONFIRM-DOWNLOAD` — تأكيد تنزيل حزمة التحميل المسبق (أمر)
  - `US-BC07-PKG-REQUEST` — طلب حزمة التحميل المسبق (أمر)
  - `US-BC07-PKG-REVOKE` — سحب حزمة التحميل المسبق (أمر)
  - `US-DOM-PKG-TENANT-LIMITS` — ضبط حدود حزم التحميل للمستأجر (أمر، جديدة)
  - `US-BC07-Q-PKG-GET` — جلب: Package manifest and download target (signed, ≤ 5 min) (جلب)
  - `US-DOM-PKG-LIST` — عرض حزم مستخدم أو جهاز للمسؤول (جلب، جديدة)
  - `US-BC07-S-PRELOAD-PACKAGE-01` — تلقائي: build started (حزمة التحميل المسبق) (نظام)
  - `US-BC07-S-PRELOAD-PACKAGE-02` — تلقائي: build finished (حزمة التحميل المسبق) (نظام)
  - `US-BC07-S-PRELOAD-PACKAGE-03` — تلقائي: expires_at reached (حزمة التحميل المسبق) (نظام)
  - `US-BC07-S-PRELOAD-PACKAGE-04` — تلقائي: user security_version changed or device not ACTIVE (حزمة التحميل المسبق) (نظام)
  - `US-UI-SCR11-PRELOAD-AREA` — اختيار منطقة العمل وتنزيل حزمتها (واجهة، جديدة)
  - `US-UI-SCR63-DEVICE-PACKAGES` — عرض حزم الجهاز وسحبها (واجهة، جديدة)
  - `US-PLT-PKG-BUILD` — بناء الحزمة بصلاحية المستخدم وقت البناء (منصة، جديدة)
  - `US-PLT-PKG-DEVICE-PURGE` — إفراغ الحزم الملغاة والمنتهية من الجهاز (منصة، جديدة)
- **حل تعارضات المزامنة** `FEAT-COL-SYNC-CONFLICTS`
  - `US-BC07-SCF-ASSIGN` — إسناد تعارض المزامنة (أمر)
  - `US-BC07-SCF-DISCARD` — حسم تعارض المزامنة بإسقاط الأمر الميداني (أمر)
  - `US-BC07-SCF-REAPPLY` — إعادة تطبيق تعارض المزامنة (أمر)
  - `US-BC07-SCF-RESOLVE-MANUALLY` — حل تعارض المزامنة يدويًا (أمر)
  - `US-BC07-Q-SCF-GET` — جلب: Original envelope, current state snapshot, owner rejection reason (جلب)
  - `US-BC07-Q-SCF-LIST` — جلب: Open sync conflicts by target type, assignee (جلب)
  - `US-BC07-S-SYNC-CONFLICT-01` — تلقائي: stale state-changing command (تعارض المزامنة) (نظام)
  - `US-UI-SCR06-SYNC-CONFLICT` — مقارنة الأمر المتعارض بالحالة الحالية وحسمه (واجهة، جديدة)
  - `US-OPS-SCF-RATIO-ALERT` — التنبيه عند ارتفاع نسبة التعارضات (تشغيل، جديدة)
- **إدارة محوّلات البيانات** `FEAT-COL-ADAPTERS`
  - `US-BC07-ADP-ACTIVATE` — تفعيل المحوّل (أمر)
  - `US-BC07-ADP-REGISTER` — تسجيل المحوّل (أمر)
  - `US-BC07-ADP-RESUME` — استئناف المحوّل (أمر)
  - `US-BC07-ADP-RETIRE` — إحالة المحوّل إلى التقاعد (أمر)
  - `US-BC07-ADP-SUSPEND` — تعليق المحوّل (أمر)
  - `US-BC07-ADP-UPDATE-MAPPING` — تحديث ربط حقول المحوّل (أمر)
  - `US-BC07-Q-ADP-GET` — جلب: Adapter with mapping versions (جلب)
  - `US-DOM-ADP-LIST` — عرض المحوّلات المسجلة وحالاتها (جلب، جديدة)
  - `US-UI-SCR65-ADAPTER-MAPPING` — مراجعة إصدارات الربط ونتائج اختبارها (واجهة، جديدة)
  - `US-PLT-ADAPTER-MAPPING-TESTS` — تشغيل اختبارات الربط قبل التفعيل (منصة، جديدة)
  - `US-INT-ADAPTER-RUNTIME` — سحب البيانات وترجمتها وتسليمها دفعات (تكامل، جديدة)
  - `US-OPS-ADAPTER-CRED-ROTATION` — تدوير مفاتيح حسابات خدمة المحوّلات (تشغيل، جديدة)
  - `US-OPS-ADAPTER-DEPLOY` — نشر كل محوّل بصورة موقّعة مستقلة (تشغيل، جديدة)
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
  - `US-UI-SCR65-CONNECTION-HEALTH` — متابعة سلامة الاتصالات وتراكمها (واجهة، جديدة)
  - `US-INT-CONN-BACKLOG-REPLAY` — استعادة التراكم بلا فقد بعد انقطاع النظام (تكامل، جديدة)
  - `US-OPS-CONN-BACKLOG-ALERT` — التنبيه عند تقادم تراكم الاتصال (تشغيل، جديدة)
  - `US-OPS-CONN-EGRESS-RULE` — تطبيق قاعدة السماح لكل اتصال في بوابة الخروج (تشغيل، جديدة)
  - `US-OPS-CONN-SECRETS` — حفظ بيانات اعتماد الاتصالات في الخزنة فقط (تشغيل، جديدة)
- **التكامل مع أنظمة المؤسسة** `FEAT-COL-ENTERPRISE-INT`
  - `US-INT-DMS-CLASS-MAPPING` — تحويل تصنيف الوثائق الخارجية بأمان (تكامل، جديدة)
  - `US-INT-DMS-DOCUMENTS` — استيراد الوثائق من نظام إدارة الوثائق (تكامل، جديدة)
  - `US-INT-ERP-MASTER-DATA` — استيراد بيانات المؤسسة الرئيسية من ERP (تكامل، جديدة)
  - `US-OPS-ENTINT-NO-WRITEBACK` — التحقق من عدم الكتابة إلى الأنظمة الخارجية (تشغيل، جديدة)
- **استيراد الخرائط والطقس** `FEAT-COL-GEO-WEATHER`
  - `US-UI-SCR11-WEATHER-LAYER` — عرض طبقات الطقس والخرائط المستوردة (واجهة، جديدة)
  - `US-PLT-GEO-REPROJECT` — توحيد إحداثيات الطبقات المستوردة (منصة، جديدة)
  - `US-INT-GEO-FILE-IMPORT` — استيراد ملفات GeoJSON وGeoPackage وKML (تكامل، جديدة)
  - `US-INT-GEO-OGC-EXCHANGE` — إتاحة البيانات الجغرافية لأنظمة GIS المؤسسية (تكامل، جديدة)
  - `US-INT-GEO-OGC-IMPORT` — جلب الطبقات من خدمات OGC وWMS/WFS (تكامل، جديدة)
  - `US-INT-GEO-RASTER-IMPORT` — استيراد الصور النقطية GeoTIFF وCOG (تكامل، جديدة)
  - `US-INT-WEATHER-FEED` — جلب بيانات الطقس من مزودها المعتمد (تكامل، جديدة)
  - `US-OPS-GEO-BASEMAP-UPDATE` — تحديث الخرائط الأساس دون إنترنت (تشغيل، جديدة)
- **استيراد البيانات والحجر** `FEAT-COL-IMPORT`
  - `US-BC02-IMP-ACCEPT-QUARANTINE` — قبول العناصر المعزولة في دفعة الاستيراد (أمر)
  - `US-BC02-IMP-CANCEL` — إلغاء دفعة الاستيراد (أمر)
  - `US-BC02-IMP-REPROCESS-QUARANTINE` — إعادة معالجة العناصر المعزولة في دفعة الاستيراد (أمر)
  - `US-BC02-IMP-SUBMIT` — تقديم دفعة الاستيراد (أمر)
  - `US-BC02-Q-IMP-GET` — جلب: Batch status, counts, quarantine records (paged) (جلب)
  - `US-DOM-IMP-LIST` — عرض دفعات الاستيراد حسب المحوّل والحالة (جلب، جديدة)
  - `US-BC02-S-IMPORT-BATCH-01` — تلقائي: processing started (دفعة الاستيراد) (نظام)
  - `US-BC02-S-IMPORT-BATCH-02` — تلقائي: all records applied (دفعة الاستيراد) (نظام)
  - `US-BC02-S-IMPORT-BATCH-03` — تلقائي: finished with invalid records (دفعة الاستيراد) (نظام)
  - `US-BC02-S-IMPORT-BATCH-04` — تلقائي: unrecoverable error (دفعة الاستيراد) (نظام)
  - `US-UI-SCR64-QUARANTINE-REVIEW` — مراجعة سجلات الحجر وقبولها أو إعادة معالجتها (واجهة، جديدة)
  - `US-PLT-IMP-ASYNC-JOB` — تنفيذ الاستيراد مهمة غير متزامنة قابلة للاستئناف (منصة، جديدة)
  - `US-PLT-IMP-LIMITS` — حماية المنصة من الدفعات الضخمة والمعيبة (منصة، جديدة)
  - `US-OPS-IMP-QUARANTINE-RATIO` — التنبيه عند ارتفاع نسبة الحجر لمحوّل (تشغيل، جديدة)
- **تدفقات الحساسات** `FEAT-COL-SENSORS`
  - `US-BC07-SNS-ACTIVATE` — تفعيل تدفق الحسّاس (أمر)
  - `US-BC07-SNS-PAUSE` — إيقاف تدفق الحسّاس مؤقتًا (أمر)
  - `US-BC07-SNS-REGISTER` — تسجيل تدفق الحسّاس (أمر)
  - `US-BC07-SNS-RETIRE` — إحالة تدفق الحسّاس إلى التقاعد (أمر)
  - `US-BC07-SNS-SET-QUALITY-RULES` — تحديد قواعد جودة تدفق الحسّاس (أمر)
  - `US-BC07-Q-SNS-LIST` — جلب: Streams with rate, staleness, quality violation counts (جلب)
  - `US-BC07-S-SENSOR-STREAM-01` — تلقائي: no data beyond stale-after (تدفق الحسّاس) (نظام)
  - `US-UI-SCR65-SENSOR-STREAMS` — متابعة تدفقات الحساسات وجودتها (واجهة، جديدة)
  - `US-PLT-SENSOR-QUALITY-EVAL` — تقييم جودة القراءات دون حذفها (منصة، جديدة)
  - `US-PLT-SENSOR-THROUGHPUT` — استيعاب خمسة آلاف قراءة في الثانية (منصة، جديدة)
  - `US-INT-SENSOR-GATEWAY` — استقبال قراءات بوابة الحساسات كملاحظات (تكامل، جديدة)

</details>

### 2.3 CAP-03 — إدارة المعلومات

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **[إدارة الكيانات وملفاتها](CAP-03-information/FEAT-INF-ENTITY-REGISTRY.md)** `FEAT-INF-ENTITY-REGISTRY` | CAP-03.01 الكيانات والعلاقات (R1) | يسجّل المحلل الأشخاص والجهات والأماكن ويعدّلها ويطّلع على ملف كل منها بقيمه المؤكدة والمتنازع عليها. | المحلل؛ النظام؛ أي مستخدم مخوَّل | 7 + 7 |
| **[ربط المعرّفات الخارجية](CAP-03-information/FEAT-INF-EXTERNAL-IDS.md)** `FEAT-INF-EXTERNAL-IDS` | CAP-03.01 الكيانات والعلاقات (R1) | تبقى السجلات الواردة من الأنظمة الخارجية مرتبطة بالعنصر الصحيح لدينا فلا تتكرر ولا تضيع. | النظام؛ المحلل | 3 + 6 |
| **[استكشاف شبكة العلاقات](CAP-03-information/FEAT-INF-GRAPH-EXPLORE.md)** `FEAT-INF-GRAPH-EXPLORE` | CAP-03.01 الكيانات والعلاقات (R1) | يستكشف المحلل محيط الكيان والمسارات التي تربط كيانين دون أن يرى ما لا يحق له. | المحلل | 2 + 6 |
| **[إعادة بناء فهارس البحث](CAP-03-information/FEAT-INF-INDEX-REBUILD.md)** `FEAT-INF-INDEX-REBUILD` | CAP-03.01 الكيانات والعلاقات (R1) | يعيد مشغل المنصة بناء فهارس البحث والرسم البياني من المصدر الأصلي دون فقد بيانات ويراقب تأخرها. | مشغّل المنصة؛ النظام | 9 + 7 |
| **[تسجيل الأحداث الواقعية](CAP-03-information/FEAT-INF-REAL-EVENTS.md)** `FEAT-INF-REAL-EVENTS` | CAP-03.01 الكيانات والعلاقات (R1) | يوثّق المحلل الأحداث التي وقعت في الواقع ويصنّفها ويعرض صورتها الموحّدة. | المحلل؛ النظام؛ أي مستخدم مخوَّل | 6 + 2 |
| **[إدارة العلاقات بين الكيانات](CAP-03-information/FEAT-INF-RELATIONSHIPS.md)** `FEAT-INF-RELATIONSHIPS` | CAP-03.01 الكيانات والعلاقات (R1) | يربط المحلل الكيانات بعلاقات موثقة ومؤرخة ويرى كل علاقات الكيان في الاتجاهين. | المحلل؛ النظام؛ أي مستخدم مخوَّل | 5 + 3 |
| **[البحث الموحد](CAP-03-information/FEAT-INF-UNIFIED-SEARCH.md)** `FEAT-INF-UNIFIED-SEARCH` | CAP-03.01 الكيانات والعلاقات (R1) | يجد المستخدم ما يبحث عنه من كيانات وملاحظات ووثائق وخطط بالنص والمكان والزمن وبالعربية والإنجليزية دون كشف ما لا يحق له. | أي مستخدم مخوَّل | 2 + 10 |
| **[الادعاءات وأدلتها](CAP-03-information/FEAT-INF-CLAIMS-EVIDENCE.md)** `FEAT-INF-CLAIMS-EVIDENCE` | CAP-03.02 الادعاءات والأدلة (R1) | يسجّل المحلل كل معلومة كادعاء مسند إلى مصادره وأدلته ويصححه أو يسحبه دون أن يُمحى أصله. | المحلل؛ النظام؛ أي مستخدم مخوَّل | 7 + 6 |
| **[مواقع الكيانات وتحركاتها](CAP-03-information/FEAT-INF-GEO-LOCATION.md)** `FEAT-INF-GEO-LOCATION` | CAP-03.03 المعلومات الجغرافية (R1) | يرى المستخدم أين كان الكيان وكيف تحرّك عبر الزمن بمواقع دقيقة وموثوقة الإحداثيات. | أي مستخدم مخوَّل؛ المحلل | 1 + 7 |
| **[تاريخ المعلومة عبر الزمن](CAP-03-information/FEAT-INF-TIME-HISTORY.md)** `FEAT-INF-TIME-HISTORY` | CAP-03.04 الزمن والتاريخ (R1) | يعرف المستخدم ما كان صحيحًا في أي وقت وما كان معروفًا عنه حينها ويسجّل المحلل تغيّر القيم بمرور الزمن. | المحلل؛ أي مستخدم مخوَّل | 2 + 4 |
| **[فصل الكيانات المدموجة خطأً](CAP-03-information/FEAT-INF-ENTITY-SPLIT.md)** `FEAT-INF-ENTITY-SPLIT` | CAP-03.05 مطابقة الكيانات (R1) | يستطيع المحلل التراجع عن دمج خاطئ فيعود كل كيان بمعلوماته الخاصة كما كانت. | المحلل؛ الشخص الثاني؛ أي مستخدم مخوَّل | 3 + 4 |
| **[مراجعة تطابق الكيانات](CAP-03-information/FEAT-INF-MATCH-REVIEW.md)** `FEAT-INF-MATCH-REVIEW` | CAP-03.05 مطابقة الكيانات (R1) | يراجع المحللون الكيانات المشتبه بأنها الشيء نفسه ويقررون دمجها أو فصلها بقرار موثق ومؤكد من محلل ثانٍ. | المحلل؛ الشخص الثاني؛ النظام | 11 + 4 |
| **[قواعد المطابقة](CAP-03-information/FEAT-INF-MATCH-RULES.md)** `FEAT-INF-MATCH-RULES` | CAP-03.05 مطابقة الكيانات (R1) | يضبط قائد المحللين قواعد اكتشاف التطابق ويقيس دقتها قبل أن يفعّلها مسؤول آخر. | قائد المحللين؛ مسؤول الإدارة؛ النظام | 5 + 3 |
| **[كشف تعارض المعلومات](CAP-03-information/FEAT-INF-CONFLICT-DETECT.md)** `FEAT-INF-CONFLICT-DETECT` | CAP-03.06 إدارة التعارض (R1) | يُكشف تلقائيًا أو يدويًا كل تناقض بين معلومتين عن الشيء نفسه فيُحفظ الطرفان ولا يُخفى أحدهما. | النظام؛ المحلل | 5 + 3 |
| **[حل التعارضات](CAP-03-information/FEAT-INF-CONFLICT-RESOLVE.md)** `FEAT-INF-CONFLICT-RESOLVE` | CAP-03.06 إدارة التعارض (R1) | يُسند قائد المحللين التعارض لمحلل يدرسه ويحسمه أو يقبله مع إمكانية إعادة فتحه. | قائد المحللين؛ المحلل | 6 + 2 |
| **[الثقة بالمعلومة ومنشؤها](CAP-03-information/FEAT-INF-TRUST-LINEAGE.md)** `FEAT-INF-TRUST-LINEAGE` | CAP-03.07 المنشأ والثقة (R1) | يقيّم المحلل درجة الثقة بالمعلومة وحالة التحقق منها ويتتبّع من أين جاءت وكيف اشتُقّت. | المحلل؛ المدقِّق؛ النظام | 2 + 6 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-03 (156)</summary>

- **إدارة الكيانات وملفاتها** `FEAT-INF-ENTITY-REGISTRY`
  - `US-BC02-ENT-CHANGE-TYPE` — تغيير نوع الكيان (أمر)
  - `US-BC02-ENT-RECLASSIFY` — إعادة تصنيف الكيان (أمر)
  - `US-BC02-ENT-REGISTER` — تسجيل الكيان (أمر)
  - `US-BC02-ENT-REINSTATE` — إعادة الكيان إلى السريان (أمر)
  - `US-BC02-ENT-RETIRE` — إحالة الكيان إلى التقاعد (أمر)
  - `US-BC02-Q-ENT-LIST` — جلب: Entities by type, bbox/polygon of current location, valid_at (جلب)
  - `US-BC02-Q-ENT-RESOLVED` — جلب: Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED candidates, confidence); resolves through the identity cluster and returns canonical_urn + requested_urn (SLC-04) (جلب)
  - `US-UI-SCR21-ENTITY-ACTIONS` — إظهار أفعال الكيان المتاحة حسب حالته (واجهة، جديدة)
  - `US-UI-SCR21-ENTITY-LIST` — تصفح الكيانات وتصفيتها بالنوع والمكان والزمن (واجهة، جديدة)
  - `US-UI-SCR21-RESOLVED-VIEW` — عرض ملف الكيان بقيمه المؤكدة والمتنازع عليها (واجهة، جديدة)
  - `US-PLT-ENTITY-HIDDEN-CLAIMS` — ألا تكشف الادعاءات المحجوبة عبر ملف الكيان (منصة، جديدة)
  - `US-PLT-ENTITY-RESOLVED-READ` — فتح ملف الكيان خلال 300 ميلي ثانية (منصة، جديدة)
  - `US-PLT-NAMES-NORMALIZE` — حفظ الأسماء بصيغها الأصلية والموحدة والمنقولة (منصة، جديدة)
  - `US-OPS-NAMES-NORM-UPGRADE` — ترقية قواعد توحيد الأسماء وإعادة الفهرسة (تشغيل، جديدة)
- **ربط المعرّفات الخارجية** `FEAT-INF-EXTERNAL-IDS`
  - `US-BC02-EXT-END` — إنهاء ربط المعرّف الخارجي (أمر)
  - `US-BC02-EXT-MAP` — تسجيل ربط ربط المعرّف الخارجي (أمر)
  - `US-BC02-Q-EXT-RESOLVE` — جلب: Object URN mapped at time t (not-found shape if hidden) (جلب)
  - `US-UI-SCR65-EXTID-LOOKUP` — البحث عن عنصر بمعرّفه في نظام خارجي (واجهة، جديدة)
  - `US-PLT-EXTID-UNIQUE-AT-TIME` — معرّف خارجي يشير لعنصر واحد في كل وقت (منصة، جديدة)
  - `US-INT-EXTID-IMPORT-UPSERT` — ربط السجل الوارد بالعنصر الموجود دون تكرار (تكامل، جديدة)
  - `US-INT-EXTID-MERGED-TARGET` — توجيه السجل الوارد لكيان مدموج إلى هويته الموحدة (تكامل، جديدة)
  - `US-INT-EXTID-REASSIGNED` — معالجة إعادة استخدام المعرّف في النظام الخارجي (تكامل، جديدة)
  - `US-OPS-EXTID-PROBE-LIMIT` — منع تخمين المعرّفات الخارجية لمعرفة الوجود (تشغيل، جديدة)
- **استكشاف شبكة العلاقات** `FEAT-INF-GRAPH-EXPLORE`
  - `US-BC07-Q-GRAPH-NEIGHBORHOOD` — جلب: Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges cut (جلب)
  - `US-BC07-Q-GRAPH-PATHS` — جلب: Paths between two entities, ≤ 4 hops, only through visible nodes and edges (جلب)
  - `US-UI-SCR24-GRAPH-EXPAND` — توسيع شبكة الكيان خطوة بخطوة (واجهة، جديدة)
  - `US-UI-SCR24-GRAPH-LIST-VIEW` — بديل جدولي للرسم البياني لسهولة الوصول (واجهة، جديدة)
  - `US-UI-SCR24-GRAPH-PATHS` — إيجاد المسارات بين كيانين وعرضها (واجهة، جديدة)
  - `US-PLT-GRAPH-INFERENCE-SUITE` — اختبار عدم كشف العقد والحواف المخفية (منصة، جديدة)
  - `US-PLT-GRAPH-NEIGHBORHOOD-PERF` — جوار الكيان بعمق اثنين خلال ثانية (منصة، جديدة)
  - `US-OPS-GRAPH-LATENCY-WATCH` — مراقبة زمن استعلامات الرسم وكثافة الجوار (تشغيل، جديدة)
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
  - `US-UI-SCR71-PROJECTION-BOARD` — متابعة إصدارات الإسقاطات وتأخرها وترقيتها (واجهة، جديدة)
  - `US-PLT-INDEX-LAG` — ظهور التغييرات في البحث خلال 30 ثانية (منصة، جديدة)
  - `US-PLT-INDEX-REBUILD-LIVE` — إعادة البناء الكاملة دون توقف خدمة البحث (منصة، جديدة)
  - `US-PLT-INDEX-REBUILD-PARITY` — إعادة البناء تعطي نتائج مطابقة للمصدر (منصة، جديدة)
  - `US-OPS-INDEX-ACCESS-ISOLATION` — حصر الوصول إلى الفهارس بخدمة البحث وحدها (تشغيل، جديدة)
  - `US-OPS-INDEX-LAG-WATCH` — التنبيه عند تأخر الإسقاطات أو تدهورها (تشغيل، جديدة)
  - `US-OPS-INDEX-RECONCILE` — مطابقة الفهرس مع المصدر ليلًا وإصلاح الفروق (تشغيل، جديدة)
- **تسجيل الأحداث الواقعية** `FEAT-INF-REAL-EVENTS`
  - `US-BC02-RWE-CHANGE-TYPE` — تغيير نوع الحدث الواقعي (أمر)
  - `US-BC02-RWE-RECLASSIFY` — إعادة تصنيف الحدث الواقعي (أمر)
  - `US-BC02-RWE-REGISTER` — تسجيل الحدث الواقعي (أمر)
  - `US-BC02-RWE-REINSTATE` — إعادة الحدث الواقعي إلى السريان (أمر)
  - `US-BC02-RWE-RETIRE` — إحالة الحدث الواقعي إلى التقاعد (أمر)
  - `US-BC02-Q-RWE-GET` — جلب: Resolved real-world event (جلب)
  - `US-UI-SCR21-EVENT-FUZZY-TIME` — إدخال زمن الحدث التقريبي وعرضه بدقته (واجهة، جديدة)
  - `US-PLT-EVENTS-FUZZY-OVERLAP` — مطابقة الأزمنة التقريبية بثلاث نتائج (منصة، جديدة)
- **إدارة العلاقات بين الكيانات** `FEAT-INF-RELATIONSHIPS`
  - `US-BC02-REL-RECLASSIFY` — إعادة تصنيف العلاقة (أمر)
  - `US-BC02-REL-REGISTER` — تسجيل العلاقة (أمر)
  - `US-BC02-REL-REINSTATE` — إعادة العلاقة إلى السريان (أمر)
  - `US-BC02-REL-RETIRE` — إحالة العلاقة إلى التقاعد (أمر)
  - `US-BC02-Q-REL-LIST` — جلب: Relationships valid_at/known_at, both directions (جلب)
  - `US-UI-SCR21-RELATION-FORM` — ربط كيانين بعلاقة مؤرخة من صفحة الكيان (واجهة، جديدة)
  - `US-UI-SCR21-RELATIONS-PANEL` — عرض علاقات الكيان في الاتجاهين مجمعة بالنوع (واجهة، جديدة)
  - `US-PLT-REL-HIGHER-LABEL` — إخفاء العلاقة الأعلى تصنيفًا من طرفيها (منصة، جديدة)
- **البحث الموحد** `FEAT-INF-UNIFIED-SEARCH`
  - `US-BC07-Q-SRCH-QUERY` — جلب: Unified search: text + types + polygon/bbox + time window + filters + facets; cursor paging; results and facets over visible facts only (جلب)
  - `US-BC07-Q-SRCH-SUGGEST` — جلب: Autocomplete from visible facts only (جلب)
  - `US-UI-SCR20-SEARCH-DEGRADED` — إبلاغ المستخدم حين يكون البحث جزئيًا أو متوقفًا (واجهة، جديدة)
  - `US-UI-SCR20-SEARCH-GEO-TIME` — تقييد البحث بمضلع على الخريطة ونافذة زمنية (واجهة، جديدة)
  - `US-UI-SCR20-SEARCH-RESULTS` — عرض نتائج البحث مجمعة بالنوع مع الأوجه (واجهة، جديدة)
  - `US-PLT-SEARCH-ALL-TYPES` — شمول البحث الخطط والتقييمات والوثائق (منصة، جديدة)
  - `US-PLT-SEARCH-ARABIC-MATCH` — مطابقة الأسماء العربية بصيغها ونقحرتها (منصة، جديدة)
  - `US-PLT-SEARCH-COMBINED-PERF` — بحث مركب بالنص والمكان والزمن خلال ثانية (منصة، جديدة)
  - `US-PLT-SEARCH-NO-INFERENCE` — ألا يكشف البحث المحجوب بالعدد أو التوقيت (منصة، جديدة)
  - `US-PLT-SEARCH-REVOCATION-RECHECK` — نفاذ سحب الصلاحية في البحث رغم تأخر الفهرس (منصة، جديدة)
  - `US-OPS-SEARCH-HEALTH-WATCH` — مراقبة زمن البحث ونسبة النتائج المسقطة (تشغيل، جديدة)
  - `US-OPS-SEARCH-INFERENCE-SUITE` — تشغيل اختبار منع الاستدلال دوريًا مع تنبيه فوري (تشغيل، جديدة)
- **الادعاءات وأدلتها** `FEAT-INF-CLAIMS-EVIDENCE`
  - `US-BC02-CLM-ASSERT` — تسجيل الادعاء (أمر)
  - `US-BC02-CLM-CORRECT` — تصحيح الادعاء (أمر)
  - `US-BC02-CLM-RECLASSIFY` — إعادة تصنيف الادعاء (أمر)
  - `US-BC02-CLM-RETRACT` — سحب الادعاء (أمر)
  - `US-BC02-EVL-LINK` — ربط رابط الدليل (أمر)
  - `US-BC02-EVL-UNLINK` — فك ربط رابط الدليل (أمر)
  - `US-BC02-Q-CLM-GET` — جلب: Claim with sources (per protection), evidence links, supersession chain (جلب)
  - `US-UI-SCR22-CLAIM-DETAIL` — عرض الادعاء بمصادره وأدلته وسلسلة تصحيحه (واجهة، جديدة)
  - `US-UI-SCR22-CLAIM-FORM` — تسجيل ادعاء بمصدره وزمن صحته ودليله (واجهة، جديدة)
  - `US-UI-SCR22-CORRECT-OR-CHANGE` — التمييز بين تصحيح القيمة وتغيرها في الواقع (واجهة، جديدة)
  - `US-PLT-CLAIMS-IMMUTABLE` — عدم الكتابة فوق ادعاءات المستوى الأول أبدًا (منصة، جديدة)
  - `US-INT-CLAIMS-FROM-ADAPTER` — تسجيل قيم الأنظمة الخارجية ادعاءات بمصدرها (تكامل، جديدة)
  - `US-OPS-CLAIMS-CURRENT-REBUILD` — إعادة بناء القيم الحالية من التاريخ عند اختلافها (تشغيل، جديدة)
- **مواقع الكيانات وتحركاتها** `FEAT-INF-GEO-LOCATION`
  - `US-BC02-Q-ENT-POSITIONS` — جلب: Position history in [from,to) as known_at (جلب)
  - `US-DOM-GEO-TRACK-SUMMARY` — تلخيص المواقع عالية التردد في ادعاء موقع (نظام، جديدة)
  - `US-UI-SCR11-COORD-FORMAT` — عرض الإحداثيات بالصيغة التي يختارها المستأجر (واجهة، جديدة)
  - `US-UI-SCR21-POSITION-TRACK` — عرض مسار الكيان على الخريطة عبر فترة (واجهة، جديدة)
  - `US-PLT-GEO-CRS-CANONICAL` — تحويل الإحداثيات إلى النظام الموحد مع حفظ الأصل (منصة، جديدة)
  - `US-PLT-GEO-GEOMETRY-VALIDATE` — رفض الأشكال الجغرافية غير الصالحة أو الناقصة (منصة، جديدة)
  - `US-PLT-GEO-SPATIAL-QUALITY` — وسم جودة الموقع بالدقة وسلامة الجهاز (منصة، جديدة)
  - `US-INT-GEO-OGC-FEATURES` — إتاحة مواقع الكيانات لأنظمة الخرائط الخارجية (تكامل، جديدة)
- **تاريخ المعلومة عبر الزمن** `FEAT-INF-TIME-HISTORY`
  - `US-BC02-CLM-RECORD-CHANGE` — تسجيل تغيير في الادعاء (أمر)
  - `US-BC02-Q-ENT-CLAIMS` — جلب: Claim history (predicate, valid_at, known_at, include_closed) (جلب)
  - `US-UI-SCR21-AS-OF` — عرض الكيان كما كان في وقت سابق (واجهة، جديدة)
  - `US-UI-SCR22-CLAIM-TIMELINE` — خط زمني لصحة الادعاء وتسجيله وتصحيحاته (واجهة، جديدة)
  - `US-PLT-TIME-INTERVALS` — فترتا الصحة والتسجيل لكل ادعاء دون تداخل (منصة، جديدة)
  - `US-PLT-TIME-ORACLE` — مطابقة استعلامات الزمن لمرجع الاختبار كاملًا (منصة، جديدة)
- **فصل الكيانات المدموجة خطأً** `FEAT-INF-ENTITY-SPLIT`
  - `US-BC02-ER-REQUEST-SPLIT` — طلب فصل حالة مطابقة الكيانات (أمر)
  - `US-BC02-ER-SPLIT` — فصل حالة مطابقة الكيانات (أمر)
  - `US-BC02-Q-CLUSTER-GET` — جلب: Cluster members, canonical URN, links, as known_at (جلب)
  - `US-UI-SCR26-CLUSTER-VIEW` — عرض أعضاء الهوية الموحدة وطلب فصلها (واجهة، جديدة)
  - `US-PLT-CLUSTER-RESOLVED-READ` — قراءة الكيان المدموج دون بطء ملحوظ (منصة، جديدة)
  - `US-OPS-CLUSTER-RECONCILE` — اكتشاف اختلاف جدول الهويات وإعادة بنائه (تشغيل، جديدة)
  - `US-OPS-ENTITY-BULK-SPLIT` — فصل دفعة دمج خاطئ بقائمة حالات (تشغيل، جديدة)
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
  - `US-UI-SCR06-ER-QUEUE` — قائمة حالات المطابقة مرتبة بالدرجة والنوع (واجهة، جديدة)
  - `US-UI-SCR26-ER-COMPARE` — مقارنة الكيانين جنبًا إلى جنب واتخاذ القرار (واجهة، جديدة)
  - `US-PLT-ER-CANDIDATES` — اقتراح المطابقات المحتملة خلال دقيقة (منصة، جديدة)
  - `US-OPS-ER-QUEUE-WATCH` — مراقبة تأخر اقتراح المطابقات وحجم قائمة المراجعة (تشغيل، جديدة)
- **قواعد المطابقة** `FEAT-INF-MATCH-RULES`
  - `US-BC02-MRS-ACTIVATE` — تفعيل مجموعة قواعد المطابقة (أمر)
  - `US-BC02-MRS-DRAFT` — إعداد مسودة مجموعة قواعد المطابقة (أمر)
  - `US-BC02-MRS-EDIT` — تعديل مجموعة قواعد المطابقة (أمر)
  - `US-DOM-MRS-EVALUATE` — تشغيل تقييم قواعد المطابقة على مجموعة الاختبار (أمر، جديدة)
  - `US-BC02-Q-MRS-GET` — جلب: Ruleset with evaluation report (جلب)
  - `US-BC02-S-MATCH-RULESET-01` — تلقائي: successor activated (مجموعة قواعد المطابقة) (نظام)
  - `US-UI-SCR26-RULESET-EVAL` — عرض تقرير تقييم القواعد قبل تفعيلها (واجهة، جديدة)
  - `US-OPS-ER-SPLIT-RATE` — تنبيه لمراجعة القواعد عند كثرة الفصل (تشغيل، جديدة)
- **كشف تعارض المعلومات** `FEAT-INF-CONFLICT-DETECT`
  - `US-BC02-CNF-RAISE` — رفع التعارض (أمر)
  - `US-BC02-Q-CNF-LIST` — جلب: Conflicts by subject, predicate, state, assignee (جلب)
  - `US-BC02-S-CONFLICT-01` — تلقائي: conflict rule matched (التعارض) (نظام)
  - `US-BC02-S-CONFLICT-02` — تلقائي: incompatible claim joined (التعارض) (نظام)
  - `US-BC02-S-CONFLICT-03` — تلقائي: member set no longer conflicting (التعارض) (نظام)
  - `US-UI-SCR06-INFO-CONFLICTS` — قائمة التعارضات مصفاة بالموضوع والحالة والمسند إليه (واجهة، جديدة)
  - `US-PLT-CONFLICT-DETECT-LATENCY` — فتح التعارض خلال 30 ثانية دون فقد (منصة، جديدة)
  - `US-OPS-CONFLICT-LAG-WATCH` — مراقبة تأخر كشف التعارضات (تشغيل، جديدة)
- **حل التعارضات** `FEAT-INF-CONFLICT-RESOLVE`
  - `US-BC02-CNF-ACCEPT` — قبول التعارض (أمر)
  - `US-BC02-CNF-ASSIGN` — إسناد التعارض (أمر)
  - `US-BC02-CNF-REOPEN` — إعادة فتح التعارض (أمر)
  - `US-BC02-CNF-RESOLVE` — حل التعارض (أمر)
  - `US-BC02-CNF-START-REVIEW` — بدء مراجعة التعارض (أمر)
  - `US-BC02-Q-CNF-GET` — جلب: Conflict with visible members, evidence, resolution history (as known_at) (جلب)
  - `US-UI-SCR26-CONFLICT-COMPARE` — مقارنة طرفي التعارض وحسمه أو قبوله (واجهة، جديدة)
  - `US-OPS-CONFLICT-BACKLOG-WATCH` — مراقبة تراكم التعارضات المفتوحة (تشغيل، جديدة)
- **الثقة بالمعلومة ومنشؤها** `FEAT-INF-TRUST-LINEAGE`
  - `US-BC02-CLM-ASSESS` — تقييم الادعاء (أمر)
  - `US-BC02-Q-LIN-TRACE` — جلب: Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy (جلب)
  - `US-UI-SCR22-CONFIDENCE-BADGE` — شارة ثقة تفتح على أبعادها السبعة (واجهة، جديدة)
  - `US-UI-SCR25-LINEAGE-GRAPH` — تتبع منشأ المعلومة صعودًا ونزولًا (واجهة، جديدة)
  - `US-PLT-CONFIDENCE-DIMENSIONS` — إرجاع أبعاد الثقة منفصلة دون درجة إلزامية (منصة، جديدة)
  - `US-PLT-LINEAGE-RECORD` — تسجيل منشأ كل عنصر مشتق تلقائيًا (منصة، جديدة)
  - `US-PLT-LINEAGE-TRACE-PERF` — تتبع المنشأ بعمق خمسة خلال ثانيتين (منصة، جديدة)
  - `US-OPS-LINEAGE-COMPLETENESS` — فحص دوري لاكتمال سجلات المنشأ (تشغيل، جديدة)

</details>

### 2.4 CAP-04 — التحليل والتقييم

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **[الفرضيات والافتراضات والأدلة](CAP-04-analysis/FEAT-ANL-ARGUMENT.md)** `FEAT-ANL-ARGUMENT` | CAP-04.01 حالات التحليل (R1) | يبني المحلل حجته بفرضيات وافتراضات صريحة وأدلة مختارة، فيعرف القارئ على ماذا يستند الاستنتاج. | المحلل | 6 + 2 |
| **[فتح حالة تحليل وإدارتها](CAP-04-analysis/FEAT-ANL-CASE-SETUP.md)** `FEAT-ANL-CASE-SETUP` | CAP-04.01 حالات التحليل (R1) | يبدأ المحلل عمله التحليلي من حالة واحدة تحدد السؤال والنطاق، ويتابعها حتى الإغلاق أو إعادة الفتح. | المحلل؛ مسؤول الأمن؛ أي مستخدم مخوَّل | 9 + 3 |
| **[السيناريوهات ومقارنة النتائج](CAP-04-analysis/FEAT-ANL-SCENARIOS.md)** `FEAT-ANL-SCENARIOS` | CAP-04.01 حالات التحليل (R1) | يقارن المحلل نتائج سيناريوهات مختلفة جنبًا إلى جنب ويرى الاستنتاجات مع مصادرها. | المحلل؛ أي مستخدم مخوَّل | 2 + 2 |
| **[إدارة طرق التحليل](CAP-04-analysis/FEAT-ANL-METHODS.md)** `FEAT-ANL-METHODS` | CAP-04.02 التنفيذ وإعادة الإنتاج (R1) | يعتمد قائد التحليل الطرق المسموح بها وإصداراتها، فلا يُستخدم إلا ما رُوجع واعتُمد. | قائد المحللين؛ مسؤول الإدارة؛ المحلل | 5 + 2 |
| **[تشغيل التحليل وإعادة إنتاجه](CAP-04-analysis/FEAT-ANL-RUNS.md)** `FEAT-ANL-RUNS` | CAP-04.02 التنفيذ وإعادة الإنتاج (R1) | يشغّل المحلل تحليلًا طويلًا دون انتظار، ويتابع تقدمه، ويعيد تشغيله لاحقًا ليحصل على النتيجة نفسها أو يعرف ما الذي اختلف. | المحلل؛ النظام | 8 + 7 |
| **[إعداد التقييم](CAP-04-analysis/FEAT-ANL-ASSESSMENT-DRAFT.md)** `FEAT-ANL-ASSESSMENT-DRAFT` | CAP-04.03 إنتاج التقييم (R1) | يكتب المحلل تقييمه بالاستنتاجات والأدلة ودرجة الثقة وحدودها، ثم يقدمه للمراجعة. | المحلل | 4 + 2 |
| **[الاطلاع على التقييمات وإصداراتها](CAP-04-analysis/FEAT-ANL-ASSESSMENT-READ.md)** `FEAT-ANL-ASSESSMENT-READ` | CAP-04.03 إنتاج التقييم (R1) | يقرأ المدير ومتخذ القرار التقييم المنشور أو نسخة سابقة منه، مع حجب ما لا يحق له رؤيته من الأدلة. | المدير؛ المحلل؛ أي مستخدم مخوَّل | 2 + 2 |
| **[مراجعة التقييم ونشره](CAP-04-analysis/FEAT-ANL-ASSESSMENT-REVIEW.md)** `FEAT-ANL-ASSESSMENT-REVIEW` | CAP-04.03 إنتاج التقييم (R1) | يراجع قائد التحليل التقييم فيعيده للتحسين أو ينشره نسخة ثابتة لا تتغير، أو يسحبه إن لزم. | المراجع؛ قائد المحللين؛ النظام | 4 + 3 |
| **[النتائج التحليلية](CAP-04-analysis/FEAT-ANL-FINDINGS.md)** `FEAT-ANL-FINDINGS` | CAP-04.03 إنتاج التقييم (R1) | يسجّل المحلل كل نتيجة بمصادرها ودرجة عدم اليقين فيها، ويراجعها زميل قبل أن يُبنى عليها تقييم. | المحلل؛ الشخص الثاني | 5 + 2 |
| **[مراجعة مقترحات الربط](CAP-04-analysis/FEAT-ANL-CORRELATION-REVIEW.md)** `FEAT-ANL-CORRELATION-REVIEW` | CAP-04.04 الدمج والربط (R2) | يراجع المحلل ما يقترحه النظام من ربط بين ملاحظات ومصادر مختلفة فيقبله أو يرفضه بناءً على الأدلة والدرجة. | المحلل؛ النظام | 8 + 3 |
| **[قواعد الربط الآلي](CAP-04-analysis/FEAT-ANL-CORRELATION-RULES.md)** `FEAT-ANL-CORRELATION-RULES` | CAP-04.04 الدمج والربط (R2) | يضبط قائد التحليل قواعد الربط الآلي ويعتمدها بموافقة ثانية، فلا تُولَّد مقترحات من قواعد غير معتمدة. | قائد المحللين؛ صاحب السلطة أو المعتمِد الثاني | 4 + 4 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-04 (89)</summary>

- **الفرضيات والافتراضات والأدلة** `FEAT-ANL-ARGUMENT`
  - `US-BC03-ACS-ADD-ASSUMPTION` — إضافة افتراض إلى حالة التحليل (أمر)
  - `US-BC03-ACS-ADD-HYPOTHESIS` — إضافة فرضية إلى حالة التحليل (أمر)
  - `US-BC03-ACS-DESELECT-EVIDENCE` — استبعاد دليل من حالة التحليل (أمر)
  - `US-BC03-ACS-RETIRE-ASSUMPTION` — سحب افتراض من حالة التحليل (أمر)
  - `US-BC03-ACS-SELECT-EVIDENCE` — اختيار دليل لـحالة التحليل (أمر)
  - `US-BC03-ACS-UPDATE-HYPOTHESIS` — تحديث فرضية في حالة التحليل (أمر)
  - `US-UI-SCR22-SELECT-EVIDENCE` — اختيار دليل للحالة من شاشة الدليل (واجهة، جديدة)
  - `US-UI-SCR30-HYPOTHESES` — عرض الفرضيات والافتراضات وحالتها في الحالة (واجهة، جديدة)
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
  - `US-UI-SCR30-CASE-ACTIONS` — أفعال الحالة المتاحة حسب وضعها (واجهة، جديدة)
  - `US-UI-SCR30-CASE-LIST` — قائمة حالات التحليل حسب الحالة والنطاق (واجهة، جديدة)
  - `US-UI-SCR30-SCOPE-MAP` — رسم النطاق المكاني والزمني للحالة على الخريطة (واجهة، جديدة)
- **السيناريوهات ومقارنة النتائج** `FEAT-ANL-SCENARIOS`
  - `US-BC03-ACS-DEFINE-SCENARIO` — تعريف سيناريو ضمن حالة التحليل (أمر)
  - `US-BC03-Q-SCN-COMPARE` — جلب: Side-by-side results of runs per scenario with differing inputs (جلب)
  - `US-UI-SCR32-COMPARE` — مقارنة سيناريوهين جنبًا إلى جنب (واجهة، جديدة)
  - `US-UI-SCR32-FINDINGS-SOURCES` — عرض الاستنتاجات مع مصادرها في السيناريو (واجهة، جديدة)
- **إدارة طرق التحليل** `FEAT-ANL-METHODS`
  - `US-BC03-AMT-ACTIVATE` — تفعيل طريقة التحليل (أمر)
  - `US-BC03-AMT-DEPRECATE` — إهمال طريقة التحليل (إيقاف الاستخدام الجديد) (أمر)
  - `US-BC03-AMT-REGISTER` — تسجيل طريقة التحليل (أمر)
  - `US-BC03-AMT-RETIRE` — إحالة طريقة التحليل إلى التقاعد (أمر)
  - `US-BC03-Q-AMT-LIST` — جلب: Methods and versions (جلب)
  - `US-UI-SCR30-METHODS` — كتالوج طرق التحليل وإصداراتها وحالتها (واجهة، جديدة)
  - `US-OPS-ANL-METHOD-IMAGES` — صور طرق التحليل موقعة ومثبتة البصمة (تشغيل، جديدة)
- **تشغيل التحليل وإعادة إنتاجه** `FEAT-ANL-RUNS`
  - `US-BC03-RUN-CANCEL` — إلغاء تشغيل التحليل (أمر)
  - `US-BC03-RUN-REPRODUCE` — إعادة إنتاج تشغيل التحليل (أمر)
  - `US-BC03-RUN-SUBMIT` — تقديم تشغيل التحليل (أمر)
  - `US-DOM-ANL-RUN-RETRY` — إعادة محاولة تشغيل تحليل فشل (أمر، جديدة)
  - `US-BC03-Q-RUN-ARTIFACT` — جلب: Short-lived download target for a result artifact (جلب)
  - `US-BC03-Q-RUN-GET` — جلب: Run with pins, parameters, steps, status, artifacts, reproduction report (جلب)
  - `US-BC03-S-ANALYSIS-RUN-01` — تلقائي: worker lease acquired (تشغيل التحليل) (نظام)
  - `US-BC03-S-ANALYSIS-RUN-02` — تلقائي: completed (تشغيل التحليل) (نظام)
  - `US-BC03-S-ANALYSIS-RUN-03` — تلقائي: error or timeout (تشغيل التحليل) (نظام)
  - `US-UI-SCR30-REPRODUCE-REPORT` — عرض تقرير إعادة الإنتاج وما اختلف (واجهة، جديدة)
  - `US-UI-SCR30-RUN-PROGRESS` — عرض تقدم التشغيل وإلغاؤه وسبب فشله (واجهة، جديدة)
  - `US-PLT-ANL-REPRO-CHECK` — فحص دوري لقابلية إعادة إنتاج التشغيلات (منصة، جديدة)
  - `US-PLT-ANL-RUN-DELEGATION` — تشغيل التحليل بصلاحيات مقدّمه فقط (منصة، جديدة)
  - `US-PLT-ANL-RUN-FAIRSHARE` — توزيع عادل للحوسبة بحصة لكل مستأجر (منصة، جديدة)
  - `US-PLT-ANL-RUN-STATUS` — متابعة حالة التشغيل وتقدمه بالسحب والاشتراك (منصة، جديدة)
- **إعداد التقييم** `FEAT-ANL-ASSESSMENT-DRAFT`
  - `US-BC03-ASM-DISCARD` — تجاهل مسودة التقييم (أمر)
  - `US-BC03-ASM-DRAFT` — إعداد مسودة التقييم (أمر)
  - `US-BC03-ASM-EDIT` — تعديل التقييم (أمر)
  - `US-BC03-ASM-SUBMIT` — تقديم التقييم (أمر)
  - `US-UI-SCR31-COMPLETENESS` — قائمة اكتمال التقييم قبل تقديمه (واجهة، جديدة)
  - `US-UI-SCR31-EDITOR` — كتابة الأحكام بمصطلح الاحتمال ودرجة الثقة (واجهة، جديدة)
- **الاطلاع على التقييمات وإصداراتها** `FEAT-ANL-ASSESSMENT-READ`
  - `US-BC03-Q-ASM-GET` — جلب: Assessment version (default: current PUBLISHED; or version / known_at) (جلب)
  - `US-BC03-Q-ASM-VERSIONS` — جلب: Version history with states and times (جلب)
  - `US-UI-SCR31-VERSIONS` — التنقل بين نسخ التقييم المنشورة (واجهة، جديدة)
  - `US-UI-SCR31-WITHHELD` — حجب الأدلة غير المصرح بها في التقييم (واجهة، جديدة)
- **مراجعة التقييم ونشره** `FEAT-ANL-ASSESSMENT-REVIEW`
  - `US-BC03-ASM-PUBLISH` — نشر التقييم (أمر)
  - `US-BC03-ASM-RETURN` — إعادة التقييم للمراجعة (أمر)
  - `US-BC03-ASM-WITHDRAW` — سحب التقييم (أمر)
  - `US-DOM-ANL-ASM-REVIEW-QUEUE` — تقييمات مقدَّمة تنتظر مراجعتي (جلب، جديدة)
  - `US-BC03-S-ASSESSMENT-01` — تلقائي: newer version published (التقييم) (نظام)
  - `US-UI-SCR06-ASSESSMENT-REVIEWS` — طابور مراجعة التقييمات في قوائم المراجعة (واجهة، جديدة)
  - `US-UI-SCR31-REVIEW-ACTIONS` — أفعال المراجعة حسب الحالة وفصل المهام (واجهة، جديدة)
- **النتائج التحليلية** `FEAT-ANL-FINDINGS`
  - `US-BC03-FND-ACCEPT` — قبول النتيجة التحليلية (أمر)
  - `US-BC03-FND-EDIT` — تعديل النتيجة التحليلية (أمر)
  - `US-BC03-FND-RECORD` — تسجيل النتيجة التحليلية (أمر)
  - `US-BC03-FND-WITHDRAW` — سحب النتيجة التحليلية (أمر)
  - `US-BC03-Q-FND-LIST` — جلب: Findings with sources (جلب)
  - `US-DOM-ANL-FND-WITHDRAW-FLAG` — تعليم التقييمات المستشهدة بنتيجة مسحوبة للمراجعة (نظام، جديدة)
  - `US-UI-SCR30-FINDINGS` — قائمة النتائج بمصادرها وعدم اليقين وحالة القبول (واجهة، جديدة)
- **مراجعة مقترحات الربط** `FEAT-ANL-CORRELATION-REVIEW`
  - `US-BC02-CRP-ACCEPT` — قبول مقترح الربط (أمر)
  - `US-BC02-CRP-PROPOSE` — اقتراح مقترح الربط (أمر)
  - `US-BC02-CRP-REJECT` — رفض مقترح الربط (أمر)
  - `US-BC02-CRP-START-REVIEW` — بدء مراجعة مقترح الربط (أمر)
  - `US-BC02-Q-CRP-GET` — جلب: Proposal with inputs, sources, reliabilities, score breakdown (جلب)
  - `US-BC02-Q-CRP-QUEUE` — جلب: Proposals by kind, state, area, score (inputs all visible to caller) (جلب)
  - `US-BC02-S-CORRELATION-PROPOSAL-01` — تلقائي: correlation rule score ≥ threshold (مقترح الربط) (نظام)
  - `US-BC02-S-CORRELATION-PROPOSAL-02` — تلقائي: not reviewed within 30 days (مقترح الربط) (نظام)
  - `US-UI-SCR06-CORRELATION-DETAIL` — تفصيل درجة الربط ومصادره وموثوقيتها (واجهة، جديدة)
  - `US-UI-SCR06-CORRELATION-MAP` — عرض عناصر مقترح الربط على الخريطة والزمن (واجهة، جديدة)
  - `US-PLT-ANL-CORRELATION-BUCKETS` — فهرسة مكانية زمنية لمرشحي الربط (منصة، جديدة)
- **قواعد الربط الآلي** `FEAT-ANL-CORRELATION-RULES`
  - `US-BC02-CRR-ACTIVATE` — تفعيل قاعدة الربط (أمر)
  - `US-BC02-CRR-DEFINE` — تعريف قاعدة الربط (أمر)
  - `US-BC02-CRR-EDIT` — تعديل قاعدة الربط (أمر)
  - `US-BC02-CRR-RETIRE` — إحالة قاعدة الربط إلى التقاعد (أمر)
  - `US-DOM-ANL-CRR-LIST` — عرض قواعد الربط وإصداراتها (جلب، جديدة)
  - `US-UI-SCR26-CORRELATION-RULES` — إدارة قواعد الربط بجوار قواعد المطابقة (واجهة، جديدة)
  - `US-UI-SCR26-CRR-APPROVAL` — مراجعة القاعدة واعتمادها من شخص ثانٍ (واجهة، جديدة)
  - `US-OPS-ANL-CORRELATION-CALIBRATE` — إعادة معايرة عتبات الربط بعد التجربة (تشغيل، جديدة)

</details>

### 2.5 CAP-05 — الوعي بالموقف

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **إنشاء المواقف وإدارتها** `FEAT-SIT-MANAGE` | CAP-05.01 تعريف الموقف (R1) | يحدد المدير أو المحلل الموقف بمنطقته وفترته ومعاييره ويتحكم في تفعيله وإيقافه وإغلاقه. | المحلل؛ المدير؛ مسؤول الأمن؛ أي مستخدم مخوَّل | 9 + 3 |
| **قواعد التنبيه** `FEAT-SIT-ALERT-RULES` | CAP-05.02 المراقبة والتنبيه (R1) | يحدد قائد المحللين أو المدير متى يجب إطلاق تنبيه ولمن ويفعّل القاعدة أو يعطّلها. | قائد المحللين؛ المدير | 6 + 3 |
| **متابعة تغيرات الموقف** `FEAT-SIT-CHANGES` | CAP-05.02 المراقبة والتنبيه (R1) | يعرف المتابع ما دخل الموقف وما خرج منه أولًا بأول دون أن يراجع كل شيء يدويًا. | المحلل؛ المدير؛ النظام | 1 + 7 |
| **تنبيهاتي** `FEAT-SIT-MY-ALERTS` | CAP-05.02 المراقبة والتنبيه (R1) | يصل المستخدم تنبيه فوري حين يقع ما يهمه فيقرّ به أو يحله أو يصرفه بسبب ويُصعَّد إن أهمله. | مستلم التنبيه؛ النظام | 8 + 5 |
| **الصورة العملياتية المشتركة** `FEAT-SIT-COP` | CAP-05.03 صورة العمليات المشتركة (الخرائط) (R1) | يرى كل مخوَّل الموقف على خريطة واحدة تجمع الكيانات والأحداث والمهام والتنبيهات بحسب صلاحيته. | أي مستخدم مخوَّل؛ المستخدم الميداني | 3 + 10 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-05 (55)</summary>

- **إنشاء المواقف وإدارتها** `FEAT-SIT-MANAGE`
  - `US-BC03-SIT-ACTIVATE` — تفعيل الموقف (أمر)
  - `US-BC03-SIT-CLOSE` — إغلاق الموقف (أمر)
  - `US-BC03-SIT-CREATE` — إنشاء الموقف (أمر)
  - `US-BC03-SIT-EDIT-DEFINITION` — تعديل تعريف الموقف (أمر)
  - `US-BC03-SIT-PAUSE` — إيقاف الموقف مؤقتًا (أمر)
  - `US-BC03-SIT-RECLASSIFY` — إعادة تصنيف الموقف (أمر)
  - `US-BC03-SIT-RESUME` — استئناف الموقف (أمر)
  - `US-BC03-Q-SIT-GET` — جلب: Definition (version at valid_at), counts of visible members by type (جلب)
  - `US-BC03-Q-SIT-LIST` — جلب: Situations by state, owner, extent intersecting bbox (جلب)
  - `US-UI-SCR10-SITUATION-LIST` — تصفح المواقف بالحالة والمالك والمنطقة (واجهة، جديدة)
  - `US-UI-SCR12-DEFINITION-EDITOR` — رسم منطقة الموقف وتحديد فترته ومعاييره (واجهة، جديدة)
  - `US-UI-SCR12-SITUATION-ACTIONS` — إظهار أفعال الموقف المتاحة حسب حالته (واجهة، جديدة)
- **قواعد التنبيه** `FEAT-SIT-ALERT-RULES`
  - `US-BC03-ARL-ACTIVATE` — تفعيل قاعدة التنبيه (أمر)
  - `US-BC03-ARL-DEFINE` — تعريف قاعدة التنبيه (أمر)
  - `US-BC03-ARL-DISABLE` — تعطيل قاعدة التنبيه (أمر)
  - `US-BC03-ARL-EDIT` — تعديل قاعدة التنبيه (أمر)
  - `US-BC03-ARL-ENABLE` — تمكين قاعدة التنبيه (أمر)
  - `US-BC03-ARL-RETIRE` — إحالة قاعدة التنبيه إلى التقاعد (أمر)
  - `US-DOM-ARL-DRY-RUN` — تجربة قاعدة التنبيه على أحداث آخر يوم (جلب، جديدة)
  - `US-UI-SCR12-ALERT-RULE-EDITOR` — تعريف شرط التنبيه ومعاينة حجمه قبل التفعيل (واجهة، جديدة)
  - `US-OPS-ALERT-STORM-LIMIT` — حد معدل لكل قاعدة يمنع سيل التنبيهات (تشغيل، جديدة)
- **متابعة تغيرات الموقف** `FEAT-SIT-CHANGES`
  - `US-BC03-Q-SIT-CHANGES` — جلب: Membership change log (visible members only) since cursor/time (جلب)
  - `US-DOM-SIT-BUFFER-FOLLOW` — تحريك منطقة الموقف مع الكيان المرجعي (نظام، جديدة)
  - `US-DOM-SIT-MEMBERSHIP-RECOMPUTE` — إعادة حساب العضوية بعد تعديل التعريف أو الاستئناف (نظام، جديدة)
  - `US-DOM-SIT-MEMBERSHIP-UPDATE` — تحديث أعضاء الموقف تلقائيًا عند تغير الكائنات (نظام، جديدة)
  - `US-UI-SCR11-CHANGE-FEED` — متابعة ما دخل الموقف وما خرج منه مباشرة (واجهة، جديدة)
  - `US-UI-SCR12-RECOMPUTE-STATUS` — إظهار تقدم إعادة حساب العضوية بعد التعديل (واجهة، جديدة)
  - `US-PLT-SIT-MEMBERSHIP-LATENCY` — انعكاس تغير العضو في الموقف خلال عشر ثوان (منصة، جديدة)
  - `US-PLT-SIT-MEMBERSHIP-RECOVERY` — استئناف تقييم العضوية من آخر نقطة بعد العطل (منصة، جديدة)
- **تنبيهاتي** `FEAT-SIT-MY-ALERTS`
  - `US-BC03-ALR-ACKNOWLEDGE` — الإقرار باستلام التنبيه (أمر)
  - `US-BC03-ALR-DISMISS` — صرف النظر عن التنبيه (أمر)
  - `US-BC03-ALR-RESOLVE` — حل التنبيه (أمر)
  - `US-BC03-Q-ALR-LIST` — جلب: My alerts by state, severity, situation (جلب)
  - `US-BC03-S-ALERT-01` — تلقائي: rule condition met (التنبيه) (نظام)
  - `US-BC03-S-ALERT-02` — تلقائي: condition met again within dedupe window (التنبيه) (نظام)
  - `US-BC03-S-ALERT-03` — تلقائي: unacknowledged beyond escalation delay (التنبيه) (نظام)
  - `US-BC03-S-ALERT-04` — تلقائي: condition cleared and rule auto_resolve (التنبيه) (نظام)
  - `US-UI-SCR04-ALERT-ACTIONS` — أفعال التنبيه حسب حالته مع سبب الصرف (واجهة، جديدة)
  - `US-UI-SCR04-ALERT-LIST` — تنبيهاتي مرتبة بالخطورة والحالة وتصل فورًا (واجهة، جديدة)
  - `US-PLT-ALERT-CLEARED-ONLY` — وصول التنبيه للمصرح لهم فقط دون أي أثر (منصة، جديدة)
  - `US-PLT-ALERT-LATENCY` — إطلاق التنبيه الحرج خلال خمس ثوان (منصة، جديدة)
  - `US-OPS-ALERT-LATENCY-WATCH` — مراقبة تأخر التنبيهات الحرجة والتصعيد (تشغيل، جديدة)
- **الصورة العملياتية المشتركة** `FEAT-SIT-COP`
  - `US-BC03-Q-BASE-TILE` — جلب: Base-map tile (layers marked unclassified only; shared cache) (جلب)
  - `US-BC03-Q-SIT-COP` — جلب: Common operational picture: visible members (entities, events, observations, tasks, assessments, alerts) with resolved, possibly generalized geometry (جلب)
  - `US-BC03-Q-SIT-TILE` — جلب: Vector tile of operational layer for the caller's security scope (جلب)
  - `US-UI-SCR11-FEATURE-CARD` — بطاقة العنصر بدقته وجودته وحالة تعميمه (واجهة، جديدة)
  - `US-UI-SCR11-LAYERS` — تشغيل طبقات الخريطة وتجميع العناصر عند التصغير (واجهة، جديدة)
  - `US-UI-SCR11-TABLE-VIEW` — بديل جدولي للخريطة لسهولة الوصول (واجهة، جديدة)
  - `US-UI-SCR11-TIME-SLIDER` — منزلق زمني لعرض الصورة في وقت سابق (واجهة، جديدة)
  - `US-PLT-COP-PICTURE-READ` — فتح صورة الموقف خلال ثانية (منصة، جديدة)
  - `US-PLT-COP-TILE-INVALIDATE` — تحديث البلاطات فور تغير العضوية أو الموقع (منصة، جديدة)
  - `US-PLT-COP-TILE-PERF` — بلاطات الخريطة خلال نصف ثانية عند التحريك (منصة، جديدة)
  - `US-PLT-COP-TILE-SCOPE-CACHE` — عدم مشاركة البلاطات بين نطاقات صلاحية مختلفة (منصة، جديدة)
  - `US-INT-COP-OGC-TILES` — إتاحة طبقات الموقف لأنظمة الخرائط الخارجية (تكامل، جديدة)
  - `US-OPS-COP-TILE-WATCH` — مراقبة زمن البلاطات ونسبة إصابة الذاكرة (تشغيل، جديدة)

</details>

### 2.6 CAP-06 — إدارة القرار

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **إعداد طلب القرار** `FEAT-DEC-REQUESTS` | CAP-06.01 طلبات القرار والخيارات (R1) | يعرض المحلل أو المخطط على صاحب السلطة سؤالًا واضحًا بخيارات مدعومة بالتقييمات وموعد نهائي. | المحلل؛ المخطِّط؛ المدير؛ النظام | 7 + 2 |
| **قرارات تنتظرني** `FEAT-DEC-MY-PENDING` | CAP-06.02 تسجيل القرار والتحقق من السلطة (R1) | يرى صاحب السلطة الطلبات التي تنتظر قراره مرتبة بالموعد، ويسجل قراره بعد التحقق من أنه يملك السلطة. | صاحب السلطة أو المعتمِد الثاني؛ النظام | 3 + 3 |
| **سجل القرار وأساسه** `FEAT-DEC-RECORD-BASIS` | CAP-06.02 تسجيل القرار والتحقق من السلطة (R1) | يعرف المدير والمدقق ما الذي قُرر ولماذا وما كان معروفًا وقت القرار، ويُبطل صاحب السلطة الأعلى القرار عند الحاجة. | المدير؛ المدقِّق؛ صاحب السلطة أو المعتمِد الثاني؛ النظام | 4 + 4 |
| **المشاركة في التنسيق** `FEAT-DEC-COORD-PARTICIPATE` | CAP-06.03 التنسيق (R2) | ترى الجهة المشاركة ما يخصها من حالة التنسيق، وتحدّث مسؤولياتها، وتطلب قرارًا من سلطة جهة أخرى. | الجهة المشاركة؛ مدير الجهة القائدة؛ النظام | 5 + 2 |
| **إدارة حالة التنسيق** `FEAT-DEC-COORDINATION` | CAP-06.03 التنسيق (R2) | يجمع مدير الجهة القائدة الجهات التي يجب أن تعمل معًا، ويوزع المسؤوليات بينها ويتابع الحالة حتى إغلاقها. | مدير الجهة القائدة | 7 + 1 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-06 (38)</summary>

- **إعداد طلب القرار** `FEAT-DEC-REQUESTS`
  - `US-BC04-DRQ-ADD-OPTION` — إضافة خيار إلى طلب القرار (أمر)
  - `US-BC04-DRQ-CITE` — الاستشهاد في طلب القرار (أمر)
  - `US-BC04-DRQ-CREATE` — إنشاء طلب القرار (أمر)
  - `US-BC04-DRQ-OPEN` — فتح طلب القرار (أمر)
  - `US-BC04-DRQ-WITHDRAW` — سحب طلب القرار (أمر)
  - `US-BC04-Q-DRQ-GET` — جلب: Request with options and pinned citations (withheld per policy) (جلب)
  - `US-DOM-DEC-MY-REQUESTS` — طلبات القرار التي أعددتها وحالتها (جلب، جديدة)
  - `US-BC04-S-DECISION-REQUEST-01` — تلقائي: deadline passed (طلب القرار) (نظام)
  - `US-UI-SCR05-REQUEST-FORM` — إعداد طلب القرار بخياراته واستشهاداته (واجهة، جديدة)
- **قرارات تنتظرني** `FEAT-DEC-MY-PENDING`
  - `US-BC04-DEC-RECORD` — تسجيل القرار (أمر)
  - `US-BC04-Q-DRQ-LIST` — جلب: My pending requests (as authority holder), by deadline (جلب)
  - `US-BC04-S-DECISION-REQUEST-02` — تلقائي: decision recorded for this request (طلب القرار) (نظام)
  - `US-UI-SCR05-PENDING-LIST` — طلبات تنتظر قراري مرتبة بالموعد (واجهة، جديدة)
  - `US-UI-SCR05-RECORD-FORM` — تسجيل القرار دون فقد المدخلات (واجهة، جديدة)
  - `US-PLT-DEC-AUTHORITY-CHECK` — فحص السلطة وقت القرار بإغلاق آمن (منصة، جديدة)
- **سجل القرار وأساسه** `FEAT-DEC-RECORD-BASIS`
  - `US-BC04-DEC-ANNUL` — إبطال القرار (أمر)
  - `US-BC04-Q-DEC-BASIS` — جلب: What was known at decision time: cited assessments (pinned versions) and their key claims resolved known_at = decision.recorded_at (جلب)
  - `US-BC04-Q-DEC-GET` — جلب: Decision with authority snapshot, citations (pinned) and supersession chain (جلب)
  - `US-DOM-DEC-LIST` — سجل القرارات للمدير والمدقق (جلب، جديدة)
  - `US-BC04-S-DECISION-01` — تلقائي: superseding decision recorded (القرار) (نظام)
  - `US-UI-SCR33-BASIS-COMPARE` — مقارنة ما عُرف وقت القرار بما يُعرف الآن (واجهة، جديدة)
  - `US-UI-SCR33-SUPERSESSION` — التنقل في سلسلة القرارات المستبدلة (واجهة، جديدة)
  - `US-PLT-DEC-BASIS-TEMPORAL` — استرجاع أساس القرار كما كان معروفًا (منصة، جديدة)
- **المشاركة في التنسيق** `FEAT-DEC-COORD-PARTICIPATE`
  - `US-BC04-CRD-REQUEST-DECISION` — طلب قرار ضمن حالة التنسيق (أمر)
  - `US-BC04-CRD-UPDATE-RESPONSIBILITY` — تحديث مسؤولية ضمن حالة التنسيق (أمر)
  - `US-BC04-Q-CRD-GET` — جلب: Case filtered to the caller's participant scope (جلب)
  - `US-BC04-Q-CRD-LIST` — جلب: Cases where the caller's unit participates (جلب)
  - `US-BC04-S-COORDINATION-CASE-01` — تلقائي: linked decision recorded (حالة التنسيق) (نظام)
  - `US-UI-SCR36-DECISION-ROUTING` — متابعة مسؤولية تنتظر قرار جهة أخرى (واجهة، جديدة)
  - `US-UI-SCR36-PARTICIPANT-VIEW` — عرض الجهة المشاركة لما يخصها فقط (واجهة، جديدة)
- **إدارة حالة التنسيق** `FEAT-DEC-COORDINATION`
  - `US-BC04-CRD-ACTIVATE` — تفعيل حالة التنسيق (أمر)
  - `US-BC04-CRD-ADD-PARTICIPANT` — إضافة مشارك إلى حالة التنسيق (أمر)
  - `US-BC04-CRD-ASSIGN-RESPONSIBILITY` — إسناد مسؤولية ضمن حالة التنسيق (أمر)
  - `US-BC04-CRD-CANCEL` — إلغاء حالة التنسيق (أمر)
  - `US-BC04-CRD-CLOSE` — إغلاق حالة التنسيق (أمر)
  - `US-BC04-CRD-OPEN` — فتح حالة التنسيق (أمر)
  - `US-BC04-CRD-REMOVE-PARTICIPANT` — إزالة مشارك من حالة التنسيق (أمر)
  - `US-UI-SCR36-COORD-BOARD` — لوحة المشاركين والمسؤوليات وحالة التنسيق (واجهة، جديدة)

</details>

### 2.7 CAP-07 — التخطيط والتنفيذ

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **[إعداد الخطة](CAP-07-planning-execution/FEAT-OPS-PLAN-AUTHORING.md)** `FEAT-OPS-PLAN-AUTHORING` | CAP-07.01 الأهداف والتخطيط (R1) | يصوغ المخطط خطة بأهدافها ومراحلها وأنشطتها ومواردها وجدولها، ثم يقدمها للاعتماد. | المخطِّط؛ مالك الخطة | 6 + 5 |
| **[إدارة حالة الخطة](CAP-07-planning-execution/FEAT-OPS-PLAN-LIFECYCLE.md)** `FEAT-OPS-PLAN-LIFECYCLE` | CAP-07.01 الأهداف والتخطيط (R1) | يعلّق المخطط الخطة أو يستأنفها أو يكملها أو يغلقها، ويُنبَّه إن أُبطل قرار تقوم عليه. | المخطِّط؛ مالك الخطة؛ صاحب السلطة أو المعتمِد الثاني؛ مسؤول الأمن؛ النظام | 7 + 2 |
| **[اعتماد الخطة](CAP-07-planning-execution/FEAT-OPS-PLAN-APPROVAL.md)** `FEAT-OPS-PLAN-APPROVAL` | CAP-07.02 إصدارات الخطة وخط الأساس (R1) | يعتمد صاحب الصلاحية — غير كاتب الخطة — نسخة الخطة فتصبح خط أساس ثابتًا، أو يعيدها أو يرفضها. | صاحب السلطة أو المعتمِد الثاني؛ النظام | 5 + 6 |
| **[تعديل الخطة المعتمدة وإصداراتها](CAP-07-planning-execution/FEAT-OPS-PLAN-VERSIONS.md)** `FEAT-OPS-PLAN-VERSIONS` | CAP-07.02 إصدارات الخطة وخط الأساس (R1) | يعدّل المخطط خطة معتمدة تعديلًا طفيفًا أو يرى الفرق عن خط الأساس وأثره على المهام قبل اعتماد نسخة جديدة. | المخطِّط؛ المدير | 3 + 3 |
| **[مهامي](CAP-07-planning-execution/FEAT-OPS-MY-TASKS.md)** `FEAT-OPS-MY-TASKS` | CAP-07.03 إدارة المهام (R1) | يرى المسند إليه كل مهامه في قائمة واحدة، وينفّذها خطوة بخطوة حتى تقديم نتيجتها، ولا يضيع شيء مما سجّله. | المسند إليه؛ المستخدم الميداني؛ النظام | 11 + 6 |
| **[متابعة المهام والتدخل](CAP-07-planning-execution/FEAT-OPS-TASK-CONTROL.md)** `FEAT-OPS-TASK-CONTROL` | CAP-07.03 إدارة المهام (R1) | يتدخل المخطط أو المدير في مهام جارية فيعلّقها أو يلغيها أو يصعّدها، ويغلق النظام المهام المنتهية أو المتجاوزة آليًا. | المخطِّط؛ المدير؛ مالك المهمة؛ المسند إليه؛ النظام | 8 + 5 |
| **[تخطيط المهام وإسنادها](CAP-07-planning-execution/FEAT-OPS-TASK-PLANNING.md)** `FEAT-OPS-TASK-PLANNING` | CAP-07.03 إدارة المهام (R1) | ينشئ المخطط المهام ويحدد مواعيدها ويسندها لمن هو مؤهل لها، ويعيد إسنادها عند الحاجة. | المخطِّط؛ المدير | 7 + 4 |
| **[مراجعة نتيجة المهمة](CAP-07-planning-execution/FEAT-OPS-TASK-REVIEW.md)** `FEAT-OPS-TASK-REVIEW` | CAP-07.03 إدارة المهام (R1) | يراجع المراجع — غير منفّذ المهمة — نتيجتها فيعتمدها أو يعيدها أو يرفضها، ولا تكتمل إلا باستيفاء معاييرها. | المراجع؛ صاحب دور الإقرار؛ النظام | 6 + 3 |
| **[أنواع المهام وخطوات اعتمادها](CAP-07-planning-execution/FEAT-OPS-TASK-TYPES.md)** `FEAT-OPS-TASK-TYPES` | CAP-07.04 سير العمل (R1) | يحدد المسؤول لكل نوع مهمة متطلبات الأهلية ومعايير الإكمال وخطوات المراجعة والاعتماد الخاصة بالجهة. | مسؤول الإدارة؛ قائد المخططين؛ أي مستخدم مخوَّل | 5 + 5 |
| **[متابعة تنفيذ الخطة](CAP-07-planning-execution/FEAT-OPS-EXEC-TRACKING.md)** `FEAT-OPS-EXEC-TRACKING` | CAP-07.05 قياس النتائج (R1) | يرى المدير والتنفيذي تقدم الخطة: المهام حسب حالتها، والمعالم، والنتائج مقابل المستهدف. | المدير؛ المخطِّط؛ القيادي التنفيذي | 1 + 4 |
| **[قياس النتائج](CAP-07-planning-execution/FEAT-OPS-OUTCOMES.md)** `FEAT-OPS-OUTCOMES` | CAP-07.05 قياس النتائج (R1) | يسجل المخطط قياسات النتائج مقابل أهدافها ويصححها، فتبقى سلسلة القياس صادقة حتى بعد تغيير الخطة. | المخطِّط؛ مالك الخطة؛ النظام | 6 + 3 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-07 (111)</summary>

- **إعداد الخطة** `FEAT-OPS-PLAN-AUTHORING`
  - `US-BC04-PLN-CREATE` — إنشاء الخطة (أمر)
  - `US-BC04-PLV-DISCARD` — تجاهل مسودة إصدار الخطة (أمر)
  - `US-BC04-PLV-DRAFT` — إعداد مسودة إصدار الخطة (أمر)
  - `US-BC04-PLV-EDIT` — تعديل محتوى مسودة إصدار الخطة (أمر)
  - `US-BC04-PLV-SUBMIT` — تقديم إصدار الخطة للاعتماد (أمر)
  - `US-BC04-Q-PLN-GET` — عرض الخطة بخط أساسها ومسودتها والقرارات التي تنفذها (جلب)
  - `US-DOM-OPS-PLAN-LIST` — قائمة الخطط المرئية حسب الحالة والنوع (جلب، جديدة)
  - `US-UI-SCR34-CREATE-FORM` — نموذج إنشاء خطة مرتبطة بقرار أو هدف (واجهة، جديدة)
  - `US-UI-SCR34-EDITOR` — محرر محتوى الخطة وفحص اكتماله قبل التقديم (واجهة، جديدة)
  - `US-UI-SCR34-PLAN-LIST` — تصفح الخطط وتصفيتها حسب الحالة والنوع (واجهة، جديدة)
  - `US-UI-SCR34-TIMELINE` — الجدول الزمني للمراحل والأنشطة والمعالم (واجهة، جديدة)
- **إدارة حالة الخطة** `FEAT-OPS-PLAN-LIFECYCLE`
  - `US-BC04-PLN-CANCEL` — إلغاء الخطة (أمر)
  - `US-BC04-PLN-CLOSE` — إغلاق الخطة (أمر)
  - `US-BC04-PLN-COMPLETE` — إكمال الخطة (أمر)
  - `US-BC04-PLN-RECLASSIFY` — إعادة تصنيف الخطة (أمر)
  - `US-BC04-PLN-RESUME` — استئناف الخطة (أمر)
  - `US-BC04-PLN-SUSPEND` — تعليق الخطة (أمر)
  - `US-BC04-S-PLAN-02` — وسم الخطة للمراجعة عند إبطال قرارها أو استبداله (نظام)
  - `US-UI-SCR34-LIFECYCLE-ACTIONS` — أفعال حالة الخطة وأثرها على المهام (واجهة، جديدة)
  - `US-UI-SCR34-REVIEW-FLAG` — تنبيه الخطة عند إبطال قرارها (واجهة، جديدة)
- **اعتماد الخطة** `FEAT-OPS-PLAN-APPROVAL`
  - `US-BC04-PLV-APPROVE` — اعتماد إصدار الخطة (أمر)
  - `US-BC04-PLV-REJECT` — رفض إصدار الخطة (أمر)
  - `US-BC04-PLV-RETURN` — إعادة إصدار الخطة إلى كاتبه للتصحيح (أمر)
  - `US-DOM-OPS-PLAN-MULTI-APPROVAL` — خطوة اعتماد ثانية للخطة حسب إعداد المستأجر (أمر، جديدة)
  - `US-BC04-S-PLAN-01` — تفعيل الخطة عند اعتماد أول إصدار لها (نظام)
  - `US-BC04-S-PLAN-VERSION-01` — استبدال خط الأساس السابق عند اعتماد إصدار أحدث (نظام)
  - `US-DOM-OPS-PLAN-TASK-SYNC` — مزامنة مهام الخطة عند اعتماد إصدار (نظام، جديدة)
  - `US-UI-SCR34-APPROVAL-PANEL` — مراجعة الفرق وأثره قبل اعتماد الخطة (واجهة، جديدة)
  - `US-UI-SCR34-BASELINE-VIEW` — عرض خط الأساس الثابت للخطة (واجهة، جديدة)
  - `US-PLT-OPS-PLAN-SYNC-LOAD` — مزامنة 500 نشاط خلال دقيقة (منصة، جديدة)
  - `US-OPS-PLAN-SYNC-REPLAY` — مراقبة مزامنة المهام وإعادة تشغيلها (تشغيل، جديدة)
- **تعديل الخطة المعتمدة وإصداراتها** `FEAT-OPS-PLAN-VERSIONS`
  - `US-BC04-PLV-AMEND-MINOR` — تعديل طفيف على خط الأساس (أمر)
  - `US-BC04-Q-PLV-DIFF` — الفرق عن خط الأساس بتصنيف التغيير ومعاينة أثره على المهام (جلب)
  - `US-BC04-Q-PLV-LIST` — إصدارات الخطة بحالاتها وأوقاتها (جلب)
  - `US-UI-SCR34-VERSION-DIFF` — شاشة الفرق عن خط الأساس بتصنيف التغيير (واجهة، جديدة)
  - `US-UI-SCR34-VERSION-HISTORY` — سجل إصدارات الخطة وحالاتها (واجهة، جديدة)
  - `US-PLT-OPS-PLAN-DIFF-READ` — حساب الفرق ومعاينة المزامنة لخطة كبيرة (منصة، جديدة)
- **مهامي** `FEAT-OPS-MY-TASKS`
  - `US-BC04-TASK-ACCEPT` — قبول المهمة (أمر)
  - `US-BC04-TASK-ADD-RESULT-ITEM` — إضافة بند نتيجة إلى المهمة (أمر)
  - `US-BC04-TASK-BLOCK` — حجب المهمة بسبب عائق (أمر)
  - `US-BC04-TASK-DECLINE` — رفض قبول المهمة (أمر)
  - `US-BC04-TASK-RESUME` — استئناف المهمة بعد الحجب (أمر)
  - `US-BC04-TASK-START` — بدء المهمة (أمر)
  - `US-BC04-TASK-SUBMIT` — تقديم المهمة للمراجعة (أمر)
  - `US-BC04-Q-TASK-GET` — تفاصيل المهمة (جلب)
  - `US-BC04-Q-TASK-HISTORY` — سجل حالات المهمة (جلب)
  - `US-BC04-Q-TASK-LIST` — قائمة مهامي (جلب)
  - `US-BC04-S-TASK-05` — تصعيد المهمة عند فوات موعدها (نظام)
  - `US-UI-SCR01-ACTIONS` — الأزرار المتاحة حسب حالة المهمة (واجهة، جديدة)
  - `US-UI-SCR01-ERRORS` — الاستجابة لرفض الخادم في مهامي (واجهة، جديدة)
  - `US-UI-SCR01-LIST` — قائمة مهامي مجمّعة حسب الحالة (واجهة، جديدة)
  - `US-UI-SCR01-OFFLINE` — العمل وحالة المزامنة دون اتصال (واجهة، جديدة)
  - `US-UI-SCR02-RESULT` — تسجيل النتيجة بيد واحدة (واجهة، جديدة)
  - `US-PLT-MYTASKS-READ` — فتح مهامي خلال 500 ms (منصة، جديدة)
- **متابعة المهام والتدخل** `FEAT-OPS-TASK-CONTROL`
  - `US-BC04-TASK-CANCEL` — إلغاء المهمة (أمر)
  - `US-BC04-TASK-CLOSE` — إغلاق المهمة (أمر)
  - `US-BC04-TASK-ESCALATE` — تصعيد المهمة يدويًا (أمر)
  - `US-BC04-TASK-SUSPEND` — تعليق المهمة (أمر)
  - `US-BC04-TASK-UNSUSPEND` — رفع تعليق المهمة (أمر)
  - `US-BC04-S-TASK-02` — إغلاق المهمة المكتملة آليًا بعد 7 أيام (نظام)
  - `US-BC04-S-TASK-03` — انتهاء المهمة عند موعدها حين يقرر نوعها ذلك (نظام)
  - `US-BC04-S-TASK-04` — استبدال المهمة عند اعتماد إصدار خطة لا يتضمنها (نظام)
  - `US-DOM-OPS-TASK-DEP-ESCALATE` — تصعيد المهام التابعة عند إلغاء سابقتها (نظام، جديدة)
  - `US-UI-SCR02-CONTROL-ACTIONS` — أفعال التدخل في المهمة حسب الدور والحالة (واجهة، جديدة)
  - `US-UI-SCR02-ESCALATION-NOTICE` — إظهار تصعيد المهمة ومستواه وسببه (واجهة، جديدة)
  - `US-PLT-TASK-TIMERS` — مؤقتات المهام تعمل خلال 60 ثانية (منصة، جديدة)
  - `US-OPS-TASK-TIMER-LAG` — تنبيه عند تأخر مؤقتات المهام (تشغيل، جديدة)
- **تخطيط المهام وإسنادها** `FEAT-OPS-TASK-PLANNING`
  - `US-BC04-TASK-ASSIGN` — إسناد المهمة لشخص مؤهل (أمر)
  - `US-BC04-TASK-CREATE` — إنشاء المهمة (أمر)
  - `US-BC04-TASK-EDIT` — تعديل المهمة قبل إسنادها (أمر)
  - `US-BC04-TASK-MARK-READY` — تعليم المهمة جاهزة للإسناد (أمر)
  - `US-BC04-TASK-REASSIGN` — إعادة إسناد المهمة (أمر)
  - `US-BC04-TASK-RECLASSIFY` — تغيير التصنيف الأمني للمهمة (أمر)
  - `US-BC04-TASK-SET-DUE` — تحديد موعد استحقاق المهمة (أمر)
  - `US-UI-SCR02-ASSIGNEE-PICKER` — اختيار المسند إليه مع أهليته وسببها (واجهة، جديدة)
  - `US-UI-SCR02-CREATE-FORM` — نموذج إنشاء المهمة بنوعها وارتباطها (واجهة، جديدة)
  - `US-UI-SCR02-ELIG-UNAVAILABLE` — تعذّر فحص الأهلية دون فقد الإسناد (واجهة، جديدة)
  - `US-PLT-TASK-ASSIGN-ELIG` — إسناد مع فحص الأهلية خلال 500 ms (منصة، جديدة)
- **مراجعة نتيجة المهمة** `FEAT-OPS-TASK-REVIEW`
  - `US-BC04-TASK-APPROVE` — اعتماد نتيجة المهمة (أمر)
  - `US-BC04-TASK-COMPLETE` — إكمال المهمة بإثبات معاييرها (أمر)
  - `US-BC04-TASK-REJECT` — رفض نتيجة المهمة (أمر)
  - `US-BC04-TASK-RETURN` — إعادة المهمة إلى المسند إليه لاستكمالها (أمر)
  - `US-BC04-TASK-START-REVIEW` — بدء مراجعة المهمة (أمر)
  - `US-DOM-OPS-TASK-MULTI-REVIEW` — خطوة مراجعة ثانية حسب نوع المهمة (أمر، جديدة)
  - `US-BC04-S-TASK-01` — إكمال المهمة تلقائيًا عند استيفاء معاييرها (نظام)
  - `US-UI-SCR02-REVIEW-PANEL` — مراجعة المعايير والإقرارات قبل الإكمال (واجهة، جديدة)
  - `US-UI-SCR06-TASK-REVIEWS` — مهام مقدَّمة تنتظر مراجعتي (واجهة، جديدة)
- **أنواع المهام وخطوات اعتمادها** `FEAT-OPS-TASK-TYPES`
  - `US-BC04-TTY-ACTIVATE` — تفعيل نوع المهمة (أمر)
  - `US-BC04-TTY-DEFINE` — تعريف نوع المهمة (أمر)
  - `US-BC04-TTY-EDIT` — تعديل نوع المهمة (أمر)
  - `US-BC04-TTY-RETIRE` — إحالة نوع المهمة إلى التقاعد (أمر)
  - `US-DOM-OPS-APPROVAL-STEPS-SET` — ضبط خطوات اعتماد الخطط للمستأجر (أمر، جديدة)
  - `US-BC04-Q-TTY-GET` — عرض نوع المهمة وإصداره (جلب)
  - `US-DOM-OPS-APPROVAL-STEPS-GET` — عرض خطوات الاعتماد السارية وإصداراتها (جلب، جديدة)
  - `US-DOM-OPS-TTY-LIST` — قائمة أنواع المهام النشطة (جلب، جديدة)
  - `US-UI-SCR66-APPROVAL-STEPS` — شاشة خطوات اعتماد الخطط (واجهة، جديدة)
  - `US-UI-SCR66-EDITOR` — تحرير نوع المهمة ومعاييره وتصعيده (واجهة، جديدة)
- **متابعة تنفيذ الخطة** `FEAT-OPS-EXEC-TRACKING`
  - `US-BC04-Q-PLN-PROGRESS` — تقدم الخطة: المهام والمعالم والنتائج (جلب)
  - `US-UI-SCR35-DRILLDOWN` — الانتقال من النشاط إلى مهامه (واجهة، جديدة)
  - `US-UI-SCR35-EXEC-SUMMARY` — ملخص مجمّع للقيادي التنفيذي (واجهة، جديدة)
  - `US-UI-SCR35-PROGRESS-BOARD` — لوحة تقدم الخطة بالمهام والمعالم والنتائج (واجهة، جديدة)
  - `US-PLT-OPS-PROGRESS-READ` — قراءة تقدم خطة كبيرة خلال ثانية (منصة، جديدة)
- **قياس النتائج** `FEAT-OPS-OUTCOMES`
  - `US-BC04-OUT-CORRECT` — تصحيح قياس نتيجة (أمر)
  - `US-BC04-OUT-RECORD` — تسجيل قياس نتيجة (أمر)
  - `US-BC04-Q-OUT-SERIES` — سلسلة قياسات النتيجة مقابل المستهدف (جلب)
  - `US-BC04-S-OUTCOME-TRACKER-01` — إنشاء متتبّع النتيجة عند اعتماد الخطة (نظام)
  - `US-BC04-S-OUTCOME-TRACKER-02` — إضافة المستهدف الجديد عند خط أساس جديد (نظام)
  - `US-BC04-S-OUTCOME-TRACKER-03` — إغلاق المتتبّع عند إغلاق الخطة أو إلغائها (نظام)
  - `US-DOM-OPS-OUTCOME-FROM-TASK` — تسجيل قياس من نتيجة مهمة (نظام، جديدة)
  - `US-UI-SCR35-OUTCOME-CHART` — منحنى القياسات مقابل المستهدف (واجهة، جديدة)
  - `US-PLT-OPS-OUTCOME-UNITS` — تحويل وحدات القياس محليًا (منصة، جديدة)

</details>

### 2.8 CAP-08 — الموارد والجاهزية

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **حجز الأصول وتوفرها** `FEAT-RES-ASSET-BOOKING` | CAP-08.01 إدارة الأصول (R2) | يرى المخطط الأصول المتاحة في نافذة زمنية ويحجزها مسبقًا دون تعارض مع حجوزات أخرى. | المخطِّط؛ مدير الموارد؛ النظام | 7 + 4 |
| **إسناد الأصول وعهدتها** `FEAT-RES-ASSET-CUSTODY` | CAP-08.01 إدارة الأصول (R2) | يعرف الجميع من يحمل الأصل الآن ولأي مهمة أُسند، مع سلسلة عهدة متصلة بلا فجوات. | مدير الموارد؛ المخطِّط؛ النظام | 5 + 3 |
| **صيانة الأصول** `FEAT-RES-ASSET-MAINTENANCE` | CAP-08.01 إدارة الأصول (R2) | يخطط مدير الموارد والفني لصيانة الأصول ويتابعونها حتى تعود جاهزة، فلا يُحجز أصل وهو قيد الصيانة. | مدير الموارد؛ الفني | 8 + 3 |
| **سجل الأصول** `FEAT-RES-ASSET-REGISTRY` | CAP-08.01 إدارة الأصول (R2) | يعرف مدير الموارد كل أصل ونوعه وحالته الفنية وشهاداته وتصنيفه الأمني حتى نهاية عمره والتخلص منه. | مدير الموارد؛ مسؤول الأمن؛ صاحب السلطة أو المعتمِد الثاني | 6 + 5 |
| **صلاحية الأصل وفقده** `FEAT-RES-ASSET-SERVICE` | CAP-08.01 إدارة الأصول (R2) | يمنع استخدام أصل معطّل أو مفقود في أي إسناد جديد ويعيده للخدمة عند إصلاحه أو استعادته. | مدير الموارد | 4 + 2 |
| **اعتماد التخصيص وأولويته** `FEAT-RES-ALLOCATION-APPROVAL` | CAP-08.02 تخصيص الموارد (R2) | تعتمد سلطة التخصيص الطلبات التي تحتاج موافقة وتحسم التنافس بإعطاء الأولوية للأهم مع إشعار المتأثرين. | صاحب السلطة أو المعتمِد الثاني؛ النظام | 4 + 2 |
| **طلب تخصيص الموارد** `FEAT-RES-ALLOCATION-REQUEST` | CAP-08.02 تخصيص الموارد (R2) | يطلب المخطط كمية من الموارد لمهمة أو خطة، فيتحقق النظام من التوفر والسعة والسياسة ويلتزم بها أو يبين سبب الرفض. | المخطِّط؛ النظام | 5 + 4 |
| **استهلاك الموارد وتحريرها** `FEAT-RES-CONSUMPTION` | CAP-08.02 تخصيص الموارد (R2) | يسجل منفذ المهمة ما استهلكه فعلًا، ويُعاد غير المستخدم إلى المجمع عند انتهاء المهمة. | المسند إليه؛ المخطِّط؛ النظام | 3 + 3 |
| **إدارة مجمعات الموارد** `FEAT-RES-RESOURCE-POOLS` | CAP-08.02 تخصيص الموارد (R2) | يدير مدير الموارد مخزون كل نوع من الموارد وسعته ويرى المتاح والملتزم به ساعة بساعة. | مدير الموارد؛ المخطِّط | 6 + 5 |
| **استلام الشحنات والخسائر** `FEAT-RES-SHIPMENT-RECEIPT` | CAP-08.03 الإمداد (R3) | تسجل الجهة المستلمة ما وصل فعلًا أو ما تلف أو فُقد، فيُغلق طلب الإمداد كاملًا أو جزئيًا بدقة. | الجهة المستلمة؛ الناقل؛ مسؤول الإرسال؛ النظام | 5 + 2 |
| **إرسال الشحنات وتتبعها** `FEAT-RES-SHIPMENT-TRACKING` | CAP-08.03 الإمداد (R3) | يرسل مسؤول الإرسال الشحنة ويتابع الجميع مسارها نقطة بنقطة حتى وصولها. | مسؤول الإرسال؛ الناقل | 8 + 4 |
| **طلب الإمداد** `FEAT-RES-SUPPLY-REQUEST` | CAP-08.03 الإمداد (R3) | يطلب ضابط الإمداد أو المخطط كمية من صنف إلى وجهة ويتابع موافقتها أو رفضها حتى تصبح جاهزة للإرسال. | ضابط الإمداد؛ المخطِّط؛ النظام | 9 + 4 |
| **التحقق من الأهلية والجاهزية** `FEAT-RES-ELIGIBILITY` | CAP-08.04 الكفاءة والأهلية (R1 (الأهلية فقط)) | يعرف المخطط ومدير الموارد فورًا هل الشخص أو الوحدة مؤهل لدور أو مهمة في وقت معين، ولماذا. | المخطِّط؛ مدير الموارد؛ مدير التدريب | 2 + 4 |
| **سجلات تأهيل الأفراد** `FEAT-RES-QUALIFICATIONS` | CAP-08.04 الكفاءة والأهلية (R1 (الأهلية فقط)) | يحفظ مدير الموارد أو مدير التدريب مؤهلات كل فرد وشهاداته وصلاحيتها، وتنتهي تلقائيًا عند انقضاء مدتها. | مدير الموارد؛ مدير التدريب؛ المدير؛ الفرد نفسه؛ النظام | 7 + 4 |
| **متطلبات الأدوار** `FEAT-RES-ROLE-REQUIREMENTS` | CAP-08.04 الكفاءة والأهلية (R1 (الأهلية فقط)) | يحدد مدير التدريب ما يلزم كل دور من مؤهلات وخبرات، ليُبنى عليه الحكم بالأهلية. | مدير التدريب؛ مسؤول الإدارة | 4 + 2 |
| **إدارة تنفيذ التمرين** `FEAT-RES-EXERCISE-CONDUCT` | CAP-08.05 التدريب والتمارين (R3) | يدير مراقب التمرين سير التمرين الحي، فيرسل الأحداث ويوقف ويستأنف وينهي، وتُسجل النتيجة النهائية للتمرين تلقائيًا. | مراقب التمرين؛ النظام | 10 + 4 |
| **تقييم المشاركين ونتائج التمرين** `FEAT-RES-EXERCISE-EVALUATION` | CAP-08.05 التدريب والتمارين (R3) | يقيّم المقيّم أداء كل مشارك في كل كفاءة، وتُستخدم النتائج دليلًا على التأهيل ودروسًا مستفادة. | مقيّم التمرين؛ مدير التدريب | 2 + 2 |
| **تخطيط التمارين وجدولتها** `FEAT-RES-EXERCISE-PLANNING` | CAP-08.05 التدريب والتمارين (R3) | يخطط مدير التمرين للتمرين ويحدد موعده ومكانه ومشاركيه ثم يطلقه في وقته. | مدير التمرين؛ مدير التدريب | 6 + 3 |
| **سيناريوهات التدريب** `FEAT-RES-TRAINING-SCENARIOS` | CAP-08.05 التدريب والتمارين (R3) | يُعد مدير التدريب سيناريوهات تدريب بأحداثها والكفاءات المستهدفة، ويعتمدها مدير التمرين قبل استخدامها. | مدير التدريب؛ مدير التمرين | 6 + 2 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-08 (169)</summary>

- **حجز الأصول وتوفرها** `FEAT-RES-ASSET-BOOKING`
  - `US-BC05-RSV-CANCEL` — إلغاء حجز الأصل (أمر)
  - `US-BC05-RSV-CONFIRM` — تأكيد حجز الأصل (أمر)
  - `US-BC05-RSV-HOLD` — إنشاء حجز الأصل مبدئيًا (أمر)
  - `US-BC05-RSV-RELEASE` — تحرير حجز الأصل (أمر)
  - `US-BC05-Q-AST-AVAILABILITY` — جلب: Assets of type/capability available in a window (and optional bbox), with blocking reasons for others visible to caller (جلب)
  - `US-BC05-S-ASSET-RESERVATION-01` — تلقائي: hold expiry (24 h) reached (حجز الأصل) (نظام)
  - `US-BC05-S-ASSET-RESERVATION-02` — تلقائي: linked task or plan terminal (حجز الأصل) (نظام)
  - `US-UI-SCR40-AVAILABILITY` — عرض توفر الأصول في نافذة زمنية (واجهة، جديدة)
  - `US-UI-SCR40-RESERVE-HOLD` — الحجز المبدئي ومهلته ورسالة التعارض (واجهة، جديدة)
  - `US-PLT-AST-AVAILABILITY-PERF` — استعلام توفر ألف أصل خلال ثانية (منصة، جديدة)
  - `US-PLT-AST-EXCLUSION` — منع تداخل حجوزات الأصل تحت التزامن (منصة، جديدة)
- **إسناد الأصول وعهدتها** `FEAT-RES-ASSET-CUSTODY`
  - `US-BC05-ASG-ASSIGN` — تسجيل إسناد الأصل (أمر)
  - `US-BC05-ASG-CANCEL` — إلغاء إسناد الأصل (أمر)
  - `US-BC05-ASG-RETURN` — إرجاع الأصل وإنهاء إسناد الأصل (أمر)
  - `US-BC05-AST-TRANSFER-CUSTODY` — نقل عهدة الأصل (أمر)
  - `US-BC05-S-ASSET-ASSIGNMENT-01` — تلقائي: linked task terminal (إسناد الأصل) (نظام)
  - `US-UI-SCR02-TASK-ASSETS` — أصول المهمة المسندة وإرجاعها من تفاصيل المهمة (واجهة، جديدة)
  - `US-UI-SCR40-CUSTODY-CHAIN` — سلسلة عهدة الأصل متصلة بلا فجوات (واجهة، جديدة)
  - `US-OPS-AST-CUSTODY-CHECK` — فحص دوري لاتصال سلاسل العهدة (تشغيل، جديدة)
- **صيانة الأصول** `FEAT-RES-ASSET-MAINTENANCE`
  - `US-BC05-AST-FAIL-MAINTENANCE` — تسجيل فشل صيانة الأصل (أمر)
  - `US-BC05-AST-START-MAINTENANCE` — بدء صيانة الأصل (أمر)
  - `US-BC05-MNT-CANCEL` — إلغاء أمر الصيانة (أمر)
  - `US-BC05-MNT-COMPLETE` — إكمال أمر الصيانة (أمر)
  - `US-BC05-MNT-PLAN` — تخطيط أمر الصيانة (أمر)
  - `US-BC05-MNT-RESCHEDULE` — إعادة جدولة أمر الصيانة (أمر)
  - `US-BC05-MNT-START` — بدء أمر الصيانة (أمر)
  - `US-BC05-Q-MNT-SCHEDULE` — جلب: Maintenance orders by asset, window, state (جلب)
  - `US-UI-SCR40-CMMS-ORIGIN` — تمييز أوامر الصيانة الواردة من نظام الصيانة (واجهة، جديدة)
  - `US-UI-SCR40-MAINTENANCE-CALENDAR` — تقويم صيانة الأصول وتعارضها مع الحجوزات (واجهة، جديدة)
  - `US-INT-CMMS-MAINTENANCE` — مزامنة أوامر الصيانة مع نظام الصيانة المؤسسي (تكامل، جديدة)
- **سجل الأصول** `FEAT-RES-ASSET-REGISTRY`
  - `US-BC05-AST-DISPOSE` — التخلص من الأصل (أمر)
  - `US-BC05-AST-RECLASSIFY` — إعادة تصنيف الأصل (أمر)
  - `US-BC05-AST-REGISTER` — تسجيل الأصل (أمر)
  - `US-BC05-AST-SET-CERTIFICATION` — تحديد شهادة الأصل (أمر)
  - `US-BC05-AST-UPDATE-CONDITION` — تحديث حالة الأصل الفنية (أمر)
  - `US-BC05-Q-AST-GET` — جلب: Asset with status, condition, certifications, custody chain, linked entity (جلب)
  - `US-DOM-AST-LIST` — البحث في سجل الأصول وتصفيته (جلب، جديدة)
  - `US-UI-SCR40-ASSET-DETAIL` — تفاصيل الأصل والأفعال المتاحة حسب حالته (واجهة، جديدة)
  - `US-UI-SCR40-ASSET-LIST` — قائمة الأصول بحالتها وشهاداتها (واجهة، جديدة)
  - `US-UI-SCR40-LOCATION-HISTORY` — موقع الأصل في أي وقت سابق على الخريطة (واجهة، جديدة)
  - `US-INT-ERP-ASSET-IMPORT` — تحميل بيانات الأصول من نظام المؤسسة (تكامل، جديدة)
- **صلاحية الأصل وفقده** `FEAT-RES-ASSET-SERVICE`
  - `US-BC05-AST-MARK-UNSERVICEABLE` — تعليم الأصل كغير صالح للخدمة (أمر)
  - `US-BC05-AST-RECOVER` — استعادة الأصل (أمر)
  - `US-BC05-AST-REPORT-LOST` — الإبلاغ عن فقد الأصل (أمر)
  - `US-BC05-AST-RETURN-TO-SERVICE` — إعادة الأصل إلى الخدمة (أمر)
  - `US-DOM-AST-CERT-EXPIRY` — الأصل منتهي الشهادة لا يُسند من لحظة الانتهاء (نظام، جديدة)
  - `US-UI-SCR40-SERVICE-STATE` — عرض الأصل المعطّل أو المفقود وسبب حالته (واجهة، جديدة)
- **اعتماد التخصيص وأولويته** `FEAT-RES-ALLOCATION-APPROVAL`
  - `US-BC05-ALC-APPROVE` — اعتماد تخصيص الموارد (أمر)
  - `US-BC05-ALC-PREEMPT` — استباق تخصيص الموارد بأولوية أعلى (أمر)
  - `US-BC05-ALC-REJECT` — رفض تخصيص الموارد (أمر)
  - `US-BC05-S-ALLOCATION-02` — تلقائي: checks passed, policy requires approval (تخصيص الموارد) (نظام)
  - `US-UI-SCR06-ALLOCATION-APPROVAL` — تخصيصات تنتظر اعتمادي في قائمة المراجعة (واجهة، جديدة)
  - `US-UI-SCR41-PREEMPT` — الاستباق بقرار مع عرض المتأثرين قبل التأكيد (واجهة، جديدة)
- **طلب تخصيص الموارد** `FEAT-RES-ALLOCATION-REQUEST`
  - `US-BC05-ALC-REQUEST` — طلب تخصيص الموارد (أمر)
  - `US-BC05-Q-ALC-LIST` — جلب: Allocations by pool, task, plan, state (جلب)
  - `US-BC05-S-ALLOCATION-01` — تلقائي: all checks passed (تخصيص الموارد) (نظام)
  - `US-BC05-S-ALLOCATION-03` — تلقائي: a check failed (تخصيص الموارد) (نظام)
  - `US-BC05-S-ALLOCATION-04` — تلقائي: provisional hold (1 h) elapsed (تخصيص الموارد) (نظام)
  - `US-UI-SCR41-ALLOCATION-LIST` — قائمة التخصيصات مجمّعة حسب الحالة (واجهة، جديدة)
  - `US-UI-SCR41-ALLOCATION-REQUEST` — طلب تخصيص يبين سبب كل فحص فاشل (واجهة، جديدة)
  - `US-PLT-ALC-CONTENTION` — لا التزام فوق السعة مع الطلبات المتزامنة (منصة، جديدة)
  - `US-OPS-RES-NOTES-MIGRATION` — ترحيل ملاحظات الموارد النصية إلى مراجع (تشغيل، جديدة)
- **استهلاك الموارد وتحريرها** `FEAT-RES-CONSUMPTION`
  - `US-BC05-ALC-RECORD-CONSUMPTION` — تسجيل استهلاك تخصيص الموارد (أمر)
  - `US-BC05-ALC-RELEASE` — تحرير تخصيص الموارد (أمر)
  - `US-BC05-S-ALLOCATION-05` — تلقائي: linked task terminal (تخصيص الموارد) (نظام)
  - `US-DOM-ALC-OVERRUN-FLAG` — وسم الاستهلاك الزائد للمراجعة بدل رفضه (نظام، جديدة)
  - `US-UI-SCR02-CONSUMPTION` — تسجيل الاستهلاك من تفاصيل المهمة (واجهة، جديدة)
  - `US-UI-SCR41-OVERRUN-REVIEW` — مراجعة الاستهلاك المتجاوز للتخصيص (واجهة، جديدة)
- **إدارة مجمعات الموارد** `FEAT-RES-RESOURCE-POOLS`
  - `US-BC05-RPL-ADJUST-CAPACITY` — تعديل سعة مجمع الموارد (أمر)
  - `US-BC05-RPL-CLOSE` — إغلاق مجمع الموارد (أمر)
  - `US-BC05-RPL-CREATE` — إنشاء مجمع الموارد (أمر)
  - `US-BC05-RPL-RESUME` — استئناف مجمع الموارد (أمر)
  - `US-BC05-RPL-SUSPEND` — تعليق مجمع الموارد (أمر)
  - `US-BC05-Q-POL-TIMELINE` — جلب: Capacity, committed and available quantity per hour in a window (جلب)
  - `US-DOM-RPL-GET` — عرض تفاصيل مجمع موارد واحد (جلب، جديدة)
  - `US-DOM-RPL-LIST` — قائمة مجمعات الموارد ضمن نطاقي (جلب، جديدة)
  - `US-UI-SCR41-CAPACITY-TIMELINE` — مخطط السعة والملتزم والمتاح ساعة بساعة (واجهة، جديدة)
  - `US-UI-SCR41-POOL-VIEW` — صفحة مجمع واحد بسعته وحالته (واجهة، جديدة)
  - `US-OPS-RPL-LEDGER-RECONCILE` — مطابقة دفتر السعة مع الالتزامات (تشغيل، جديدة)
- **استلام الشحنات والخسائر** `FEAT-RES-SHIPMENT-RECEIPT`
  - `US-BC05-SHP-DELIVER` — تسليم الشحنة (أمر)
  - `US-BC05-SHP-REPORT-DAMAGE` — الإبلاغ عن تلف الشحنة (أمر)
  - `US-BC05-SHP-REPORT-LOST` — الإبلاغ عن فقد الشحنة (أمر)
  - `US-BC05-S-LOGISTICS-REQUEST-06` — تلقائي: linked shipment delivered in full (طلب الإمداد) (نظام)
  - `US-BC05-S-LOGISTICS-REQUEST-07` — تلقائي: linked shipment resolved short (طلب الإمداد) (نظام)
  - `US-UI-SCR49-OUTCOME-SUMMARY` — ملخص نتيجة الطلب كاملًا أو جزئيًا (واجهة، جديدة)
  - `US-UI-SCR49-RECEIPT` — تسجيل المستلم فعلًا والتالف والمفقود (واجهة، جديدة)
- **إرسال الشحنات وتتبعها** `FEAT-RES-SHIPMENT-TRACKING`
  - `US-BC05-LGR-DISPATCH` — إرسال طلب الإمداد (أمر)
  - `US-BC05-SHP-CANCEL` — إلغاء الشحنة (أمر)
  - `US-BC05-SHP-DEPART` — بدء نقل الشحنة (أمر)
  - `US-BC05-SHP-PLAN` — تخطيط الشحنة (أمر)
  - `US-BC05-SHP-RECORD-CHECKPOINT` — تسجيل نقطة عبور لـالشحنة (أمر)
  - `US-BC05-Q-SHP-GET` — جلب: Shipment with current state and delivered/damaged/lost quantity (جلب)
  - `US-BC05-Q-SHP-LIST` — جلب: Shipments filtered by logistics request, carrier, state, window (جلب)
  - `US-BC05-Q-SHP-TRACKING` — جلب: Full checkpoint history of a shipment, in order (جلب)
  - `US-UI-SCR49-DISPATCH` — الإرسال متاح فقط والتخصيص ملتزم (واجهة، جديدة)
  - `US-UI-SCR49-TRACKING-MAP` — مسار الشحنة نقطة بنقطة على الخريطة (واجهة، جديدة)
  - `US-PLT-SHP-TRANSIT-METRIC` — قياس مدة نقل الشحنات مقابل الهدف (منصة، جديدة)
  - `US-INT-CARRIER-CHECKPOINTS` — استقبال نقاط العبور من نظام الناقل (تكامل، جديدة)
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
  - `US-DOM-LGR-LABEL` — اشتقاق تصنيف طلب الإمداد والشحنة (نظام، جديدة)
  - `US-UI-SCR49-REQUEST-FORM` — طلب إمداد من فهرس الأصناف وحالة تخصيصه (واجهة، جديدة)
  - `US-UI-SCR49-REQUEST-LIST` — قائمة طلبات الإمداد بمرشحاتها وروابطها (واجهة، جديدة)
  - `US-INT-ERP-INVENTORY` — مقارنة مخزون الأصناف في ERP بالمجمعات (تكامل، جديدة)
- **التحقق من الأهلية والجاهزية** `FEAT-RES-ELIGIBILITY`
  - `US-BC05-Q-ELIG-CHECK` — جلب: EligibilityCheck(person, task_type version, at) → status + reasons (جلب)
  - `US-BC05-Q-READINESS` — جلب: Readiness of a person or unit for a role at time t, with gaps (جلب)
  - `US-UI-SCR42-ELIGIBILITY-CHECK` — فحص أهلية شخص مع الأسباب (واجهة، جديدة)
  - `US-UI-SCR48-READINESS` — جاهزية الفرد أو الوحدة وفجواتها (واجهة، جديدة)
  - `US-PLT-ELIG-FAIL-CLOSED` — لا إسناد إذا تعذر فحص الأهلية (منصة، جديدة)
  - `US-PLT-ELIG-ORACLE` — جداول حالات مرجعية لاختبار الأهلية والجاهزية (منصة، جديدة)
- **سجلات تأهيل الأفراد** `FEAT-RES-QUALIFICATIONS`
  - `US-BC05-QUAL-RECORD` — تسجيل سجل التأهيل (أمر)
  - `US-BC05-QUAL-REINSTATE` — إعادة سجل التأهيل إلى السريان (أمر)
  - `US-BC05-QUAL-RENEW` — تجديد سجل التأهيل (أمر)
  - `US-BC05-QUAL-REVOKE` — سحب سجل التأهيل (أمر)
  - `US-BC05-QUAL-SUSPEND` — تعليق سجل التأهيل (أمر)
  - `US-BC05-Q-QUAL-LIST` — جلب: Qualification records as of t (جلب)
  - `US-BC05-S-QUALIFICATION-RECORD-01` — تلقائي: valid_to reached (سجل التأهيل) (نظام)
  - `US-DOM-QUAL-EXPIRY-NOTICE` — تنبيه الفرد ومديره قبل انتهاء المؤهل (نظام، جديدة)
  - `US-UI-SCR42-MY-QUALS` — الفرد يرى مؤهلاته وشهاداته (واجهة، جديدة)
  - `US-UI-SCR42-QUAL-LIST` — مؤهلات الفرد وصلاحيتها في تاريخ معين (واجهة، جديدة)
  - `US-INT-HR-QUALIFICATIONS` — استيراد المؤهلات من نظام الموارد البشرية (تكامل، جديدة)
- **متطلبات الأدوار** `FEAT-RES-ROLE-REQUIREMENTS`
  - `US-BC05-RRQ-ACTIVATE` — تفعيل متطلبات الدور (أمر)
  - `US-BC05-RRQ-DEFINE` — تعريف متطلبات الدور (أمر)
  - `US-BC05-RRQ-EDIT` — تعديل متطلبات الدور (أمر)
  - `US-BC05-RRQ-RETIRE` — إحالة متطلبات الدور إلى التقاعد (أمر)
  - `US-DOM-RRQ-LIST` — عرض متطلبات الأدوار ونسخها (جلب، جديدة)
  - `US-UI-SCR42-ROLE-REQUIREMENTS` — تحرير متطلبات الدور ونسخها واعتمادها (واجهة، جديدة)
- **إدارة تنفيذ التمرين** `FEAT-RES-EXERCISE-CONDUCT`
  - `US-BC05-SIM-ABORT` — إيقاف تشغيل المحاكاة نهائيًا مع السبب (أمر)
  - `US-BC05-SIM-COMPLETE` — إكمال تشغيل المحاكاة (أمر)
  - `US-BC05-SIM-DELIVER-INJECT` — تسليم حقنة سيناريو ضمن تشغيل المحاكاة (أمر)
  - `US-BC05-SIM-PAUSE` — إيقاف تشغيل المحاكاة مؤقتًا (أمر)
  - `US-BC05-SIM-RESUME` — استئناف تشغيل المحاكاة (أمر)
  - `US-BC05-SIM-START` — بدء تشغيل المحاكاة (أمر)
  - `US-BC05-Q-SIM-GET` — جلب: Simulation with current state and evaluation summary (جلب)
  - `US-BC05-Q-SIM-LIST` — جلب: Simulations filtered by exercise, state, window (جلب)
  - `US-BC05-S-EXERCISE-01` — تلقائي: linked simulation completed (التمرين) (نظام)
  - `US-BC05-S-EXERCISE-02` — تلقائي: linked simulation aborted (التمرين) (نظام)
  - `US-UI-SCR48-COMPLETE-GUARD` — عرض المشاركين غير المقيَّمين قبل الإكمال (واجهة، جديدة)
  - `US-UI-SCR48-CONTROL-CONSOLE` — لوحة مراقب التمرين لإدارة الأحداث الحية (واجهة، جديدة)
  - `US-UI-SCR48-LIVE-TIMELINE` — خط زمني حي للأحداث والتقييمات (واجهة، جديدة)
  - `US-PLT-SIM-INJECT-LATENCY` — تسجيل الحدث المرسل خلال الزمن المستهدف (منصة، جديدة)
- **تقييم المشاركين ونتائج التمرين** `FEAT-RES-EXERCISE-EVALUATION`
  - `US-BC05-SIM-RECORD-EVALUATION` — تسجيل تقييم ضمن تشغيل المحاكاة (أمر)
  - `US-BC05-Q-SIM-TIMELINE` — جلب: Full, ordered timeline of inject deliveries and evaluations for a simulation (جلب)
  - `US-UI-SCR48-APPLY-RESULTS` — استخدام نتائج التمرين دليل تأهيل ودرسًا مستفادًا (واجهة، جديدة)
  - `US-UI-SCR48-EVALUATION-FORM` — نموذج تقييم المشارك لكل كفاءة (واجهة، جديدة)
- **تخطيط التمارين وجدولتها** `FEAT-RES-EXERCISE-PLANNING`
  - `US-BC05-EXR-CANCEL` — إلغاء التمرين (أمر)
  - `US-BC05-EXR-PLAN` — تخطيط التمرين (أمر)
  - `US-BC05-EXR-SCHEDULE` — جدولة التمرين (أمر)
  - `US-BC05-EXR-START` — بدء التمرين (أمر)
  - `US-BC05-Q-EXR-GET` — جلب: Exercise with frozen scenario reference, participants, current state (جلب)
  - `US-BC05-Q-EXR-LIST` — جلب: Exercises filtered by scenario, state, window (جلب)
  - `US-DOM-TRX-LABEL` — اشتقاق تصنيف السيناريو والتمرين والمحاكاة (نظام، جديدة)
  - `US-UI-SCR48-EXERCISE-CALENDAR` — تقويم التمارين حسب الحالة والموعد (واجهة، جديدة)
  - `US-UI-SCR48-EXERCISE-SETUP` — تجهيز التمرين وزر البدء حسب الجاهزية (واجهة، جديدة)
- **سيناريوهات التدريب** `FEAT-RES-TRAINING-SCENARIOS`
  - `US-BC05-SCN-ACTIVATE` — تفعيل سيناريو التدريب (أمر)
  - `US-BC05-SCN-DEFINE` — تعريف سيناريو التدريب (أمر)
  - `US-BC05-SCN-EDIT` — تعديل سيناريو التدريب (أمر)
  - `US-BC05-SCN-RETIRE` — إحالة سيناريو التدريب إلى التقاعد (أمر)
  - `US-BC05-Q-SCN-GET` — جلب: Scenario with injects and target competencies (جلب)
  - `US-BC05-Q-SCN-LIST` — جلب: Scenarios filtered by exercise type, state (جلب)
  - `US-UI-SCR48-SCENARIO-EDITOR` — تحرير السيناريو وأحداثه بترتيبها الزمني (واجهة، جديدة)
  - `US-UI-SCR48-SCENARIO-VERSIONS` — نسخ السيناريو والتمارين المرتبطة بكل نسخة (واجهة، جديدة)

</details>

### 2.9 CAP-09 — المخاطر والطوارئ

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **سجل المخاطر** `FEAT-RSK-RISK-REGISTER` | CAP-09.01 إدارة المخاطر (R3) | يسجل المستخدم المخوَّل خطرًا محتملًا بنطاقه، ويتصفح سجل المخاطر مصفّى حسب ما يحق له رؤيته. | محدِّد الخطر؛ مدير المخاطر؛ مالك النطاق؛ النظام | 4 + 3 |
| **تقييم المخاطر ومعالجتها** `FEAT-RSK-RISK-TREATMENT` | CAP-09.01 إدارة المخاطر (R3) | يقيّم المقيّم الخطر — غير من سجّله — ويخطط لمعالجته ثم يغلقه بمبرر صريح. | مقيّم الخطر؛ موافق المعالجة؛ مدير المخاطر | 4 + 1 |
| **قيادة الاستجابة للحادثة** `FEAT-RSK-INCIDENT-COMMAND` | CAP-09.02 الحوادث والاستجابة (R3) | يوجّه قائد الحادثة الاستجابة ويصعّد الخطورة أو يخفضها حتى الاحتواء والحل والإغلاق، ويُنبَّه إن تأخر التوجيه. | قائد الحادثة؛ النظام | 7 + 4 |
| **الإبلاغ عن الحوادث وتقييمها** `FEAT-RSK-INCIDENT-REPORT` | CAP-09.02 الحوادث والاستجابة (R3) | يبلّغ أي مستخدم مخوَّل عن حادثة فورًا، ويحدد المقيّم خطورتها، ويتابع الجميع الحوادث ضمن نطاقهم. | المُبلِّغ؛ مقيّم الحادثة؛ أي مستخدم مخوَّل | 5 + 3 |
| **تفعيل خطة الطوارئ ومتابعة التعافي** `FEAT-RSK-CONTINUITY` | CAP-09.03 الاستمرارية والتعافي (R3) | يفعّل قائد الحادثة خطة الطوارئ بقرار صريح، ويتابع مع مالك الاستمرارية تقدم التعافي مقارنة بزمن بدء الحادثة. | قائد الحادثة؛ مالك الاستمرارية | 2 + 2 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-09 (35)</summary>

- **سجل المخاطر** `FEAT-RSK-RISK-REGISTER`
  - `US-BC04-RIS-IDENTIFY` — تحديد الخطر (أمر)
  - `US-BC04-Q-RIS-GET` — جلب: Risk بنطاقه المرئي للطالب (جلب)
  - `US-BC04-Q-RIS-REGISTER` — جلب: سجل المخاطر مصفّى بالفئة/النطاق/الدرجة (جلب)
  - `US-BC04-S-RISK-01` — تلقائي: incident references this risk as risk_ref (الخطر) (نظام)
  - `US-UI-SCR47-RISK-FORM` — تسجيل خطر بفئته ونطاقه (واجهة، جديدة)
  - `US-UI-SCR47-RISK-REGISTER` — سجل المخاطر بالتصفية ومصفوفة الدرجة (واجهة، جديدة)
  - `US-OPS-RSK-HAZARD-CATALOG` — تحميل فئات الخطر للمستأجر عند التهيئة (تشغيل، جديدة)
- **تقييم المخاطر ومعالجتها** `FEAT-RSK-RISK-TREATMENT`
  - `US-BC04-RIS-ASSESS` — تقييم الخطر (أمر)
  - `US-BC04-RIS-CLOSE` — إغلاق الخطر (أمر)
  - `US-BC04-RIS-PLAN-TREATMENT` — تخطيط معالجة الخطر (أمر)
  - `US-BC04-RIS-REASSESS` — إعادة تقييم الخطر (أمر)
  - `US-UI-SCR47-RISK-TREATMENT` — تقييم الخطر ومعالجته وإغلاقه بمبرر (واجهة، جديدة)
- **قيادة الاستجابة للحادثة** `FEAT-RSK-INCIDENT-COMMAND`
  - `US-BC04-INC-CLOSE` — إغلاق الحادثة (أمر)
  - `US-BC04-INC-CONTAIN` — احتواء الحادثة (أمر)
  - `US-BC04-INC-DE-ESCALATE` — خفض خطورة الحادثة (أمر)
  - `US-BC04-INC-DISPATCH-RESPONSE` — توجيه الاستجابة لـالحادثة (أمر)
  - `US-BC04-INC-ESCALATE` — تصعيد الحادثة (أمر)
  - `US-BC04-INC-RESOLVE` — حل الحادثة (أمر)
  - `US-BC04-S-INCIDENT-01` — تلقائي: response SLA elapsed without dispatch (الحادثة) (نظام)
  - `US-UI-SCR47-COMMAND-ACTIONS` — أفعال قائد الحادثة حسب حالتها (واجهة، جديدة)
  - `US-UI-SCR47-DISPATCH` — توجيه الاستجابة بقائد ومهام مرتبطة (واجهة، جديدة)
  - `US-UI-SCR47-SEVERITY-HISTORY` — سجل تغير خطورة الحادثة (واجهة، جديدة)
  - `US-OPS-RSK-SLA-RECALIBRATE` — ضبط مهل الاستجابة حسب الخطورة بعد التجربة (تشغيل، جديدة)
- **الإبلاغ عن الحوادث وتقييمها** `FEAT-RSK-INCIDENT-REPORT`
  - `US-BC04-INC-ASSESS` — تقييم الحادثة (أمر)
  - `US-BC04-INC-CANCEL` — إلغاء الحادثة (أمر)
  - `US-BC04-INC-REPORT` — الإبلاغ عن الحادثة (أمر)
  - `US-BC04-Q-INC-GET` — جلب: Incident بنطاقه المرئي للطالب (جلب)
  - `US-BC04-Q-INC-LIST` — جلب: حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق (جلب)
  - `US-UI-SCR47-INCIDENT-LIST` — قائمة الحوادث بالتصفية والخطورة (واجهة، جديدة)
  - `US-UI-SCR47-INCIDENT-MAP` — عرض الحوادث ضمن نطاقي على الخريطة (واجهة، جديدة)
  - `US-UI-SCR47-QUICK-REPORT` — إبلاغ سريع عن حادثة بأقل الحقول (واجهة، جديدة)
- **تفعيل خطة الطوارئ ومتابعة التعافي** `FEAT-RSK-CONTINUITY`
  - `US-BC04-INC-ACTIVATE-CONTINGENCY` — تفعيل خطة الاستمرارية لـالحادثة (أمر)
  - `US-BC04-Q-INC-RECOVERY-STATUS` — جلب: تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء الحادثة (RTO/RPO تقديرية) (جلب)
  - `US-UI-SCR47-ACTIVATE-CONTINGENCY` — تفعيل خطة الطوارئ بقرار صريح (واجهة، جديدة)
  - `US-UI-SCR47-RECOVERY-STATUS` — تقدم التعافي مقابل زمن بدء الحادثة (واجهة، جديدة)

</details>

### 2.10 CAP-10 — الاتصال والمنتجات

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **صندوق إشعاراتي** `FEAT-COM-INBOX` | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) | يرى كل مستخدم إشعاراته في مكان واحد ويعلّمها كمقروءة، وتُنظف القديمة تلقائيًا. | أي مستخدم مخوَّل؛ النظام | 3 + 4 |
| **إيصال الإشعارات بأمان** `FEAT-COM-NOTIFY-DELIVERY` | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) | تصل الإشعارات داخل التطبيق وعلى الجوال إلى المخوّلين فقط ودون محتوى سري في رسائل الجوال. | النظام | 4 + 7 |
| **رسائل الإنذار العام** `FEAT-COM-PUBLIC-ALERTS` | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) | يعد ضابط المناوبة رسالة إنذار عامة بالمعيار الدولي ويطلقها صاحب السلطة إلى الجهات الخارجية مع متابعة وصولها. | ضابط المناوبة؛ المشغِّل؛ صاحب السلطة أو المعتمِد الثاني؛ المدقِّق؛ النظام | 6 + 4 |
| **اشتراكاتي ومتابعاتي** `FEAT-COM-SUBSCRIPTIONS` | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) | يختار المستخدم ما يتابعه وكيف يصله التنبيه، ويوقفه أو يلغيه متى شاء. | أي مستخدم مخوَّل؛ النظام | 6 + 3 |
| **توزيع المنتجات** `FEAT-COM-DISTRIBUTION` | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) | يوزع المدير أو مالك المنتج المنتج المعتمد على المخوّلين فقط، مع سجل كامل لمن استلمه. | المدير؛ مالك المنتج؛ مسؤول الأمن؛ المدقِّق؛ النظام | 5 + 2 |
| **إعداد التقارير والإحاطات** `FEAT-COM-PRODUCT-AUTHORING` | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) | يولد المحلل أو المخطط تقريرًا أو إحاطة أو خريطة من قالب ببياناته وأدلته، ويحرر نصه ثم يقدمه للمراجعة. | المحلل؛ المخطِّط؛ النظام | 7 + 5 |
| **تصفح المنتجات وتنزيلها** `FEAT-COM-PRODUCT-LIBRARY` | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) | يجد المستخدم المخوّل المنتجات المعتمدة وأحدث نسخها وينزلها بصيغة PDF أو مستند بعلامة مائية باسمه. | أي مستخدم مخوَّل؛ المحلل؛ المدير؛ النظام | 3 + 5 |
| **مراجعة المنتجات واعتمادها** `FEAT-COM-PRODUCT-REVIEW` | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) | يراجع المراجع المنتج فيعتمده نسخة نهائية مجمدة أو يعيده للتعديل، ويستطيع المدير سحبه. | المراجع؛ المدير | 3 + 3 |
| **قوالب المنتجات** `FEAT-COM-PRODUCT-TEMPLATES` | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) | يعد مدير المعرفة قوالب موحدة للتقارير والإحاطات والخرائط، ويعتمدها شخص ثانٍ قبل استخدامها. | مدير المعرفة؛ قائد المحللين؛ صاحب السلطة أو المعتمِد الثاني | 4 + 3 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-10 (77)</summary>

- **صندوق إشعاراتي** `FEAT-COM-INBOX`
  - `US-BC04-NTF-MARK-READ` — تعليم الإشعار كمقروء (أمر)
  - `US-BC04-Q-NTF-INBOX` — جلب: My notifications (references + templates) (جلب)
  - `US-BC04-S-NOTIFICATION-05` — تلقائي: TTL (30 d) elapsed (الإشعار) (نظام)
  - `US-UI-SCR03-LIST` — صندوق الوارد غير المقروء أولًا (واجهة، جديدة)
  - `US-UI-SCR03-OFFLINE` — الإشعارات في التطبيق الميداني دون اتصال (واجهة، جديدة)
  - `US-UI-SCR03-UNREAD-BADGE` — عداد غير المقروء يتحدث تلقائيًا (واجهة، جديدة)
  - `US-PLT-INBOX-POLL-FALLBACK` — صندوق الوارد حالي بسحب احتياطي كل دقيقة (منصة، جديدة)
- **إيصال الإشعارات بأمان** `FEAT-COM-NOTIFY-DELIVERY`
  - `US-BC04-S-NOTIFICATION-01` — تلقائي: notifiable event for recipient (الإشعار) (نظام)
  - `US-BC04-S-NOTIFICATION-02` — تلقائي: delivered to channel (الإشعار) (نظام)
  - `US-BC04-S-NOTIFICATION-03` — تلقائي: recipient no longer authorized at delivery (الإشعار) (نظام)
  - `US-BC04-S-NOTIFICATION-04` — تلقائي: delivery failed after retries (الإشعار) (نظام)
  - `US-DOM-NTF-QUIET-HOURS` — تأجيل الدفع في ساعات الهدوء عدا الحرج (نظام، جديدة)
  - `US-PLT-NOTIFY-FANOUT` — وصول إشعار التنبيه الحرج خلال خمس ثوانٍ (منصة، جديدة)
  - `US-PLT-NOTIFY-SAFE-PAYLOAD` — رسالة الجوال مرجع وعنوان آمن فقط (منصة، جديدة)
  - `US-INT-NOTIFY-DEVICE-TOKEN` — ربط الجهاز بالإشعارات وإلغاؤه عند فقده (تكامل، جديدة)
  - `US-INT-NOTIFY-PUSH-RELAY` — إرسال الإشعار الفوري عبر مرحّل داخلي (تكامل، جديدة)
  - `US-OPS-NOTIFY-DELIVERY-MONITOR` — مراقبة فشل الإشعارات وتعطل المرحّل (تشغيل، جديدة)
  - `US-OPS-NOTIFY-LEAK-TEST` — اختبار عدم تسرب التنبيهات لغير المصرح لهم (تشغيل، جديدة)
- **رسائل الإنذار العام** `FEAT-COM-PUBLIC-ALERTS`
  - `US-BC03-CAP-CANCEL` — إلغاء رسالة CAP الصادرة (أمر)
  - `US-BC03-CAP-PREPARE` — إعداد رسالة CAP الصادرة (أمر)
  - `US-BC03-CAP-RELEASE` — تحرير رسالة CAP الصادرة (أمر)
  - `US-BC03-CAP-RETRY` — إعادة محاولة رسالة CAP الصادرة (أمر)
  - `US-BC03-Q-CAP-LIST` — جلب: Outbound CAP messages by state (جلب)
  - `US-BC03-S-CAP-MESSAGE-01` — تلقائي: delivery failed after retries (رسالة CAP الصادرة) (نظام)
  - `US-UI-SCR14-RELEASE-REVIEW` — معاينة رسالة الإنذار قبل إطلاقها وتتبع وصولها (واجهة، جديدة)
  - `US-INT-CAP-INBOUND` — استقبال رسائل الإنذار من الجهات الأخرى (تكامل، جديدة)
  - `US-INT-CAP-OUTBOUND` — إرسال رسالة الإنذار العام وتسجيل إقرارها (تكامل، جديدة)
  - `US-OPS-CAP-ENDPOINT` — اعتماد منفذ الإنذار الخارجي ومراقبته (تشغيل، جديدة)
- **اشتراكاتي ومتابعاتي** `FEAT-COM-SUBSCRIPTIONS`
  - `US-BC04-SUB-PAUSE` — إيقاف الاشتراك مؤقتًا (أمر)
  - `US-BC04-SUB-RESUME` — استئناف الاشتراك (أمر)
  - `US-BC04-SUB-SUBSCRIBE` — إنشاء الاشتراك (أمر)
  - `US-BC04-SUB-UNSUBSCRIBE` — إلغاء الاشتراك (أمر)
  - `US-BC04-SUB-UPDATE-CHANNELS` — تحديث قنوات الاشتراك (أمر)
  - `US-DOM-SUB-LIST` — عرض قائمة اشتراكاتي (جلب، جديدة)
  - `US-BC04-S-SUBSCRIPTION-01` — تلقائي: subscriber lost visibility of target (الاشتراك) (نظام)
  - `US-UI-SCR03-SUBSCRIPTIONS` — إدارة اشتراكاتي وقنواتها وساعات الهدوء (واجهة، جديدة)
  - `US-UI-SCR12-FOLLOW` — زر متابعة الموقف أو قاعدة التنبيه (واجهة، جديدة)
- **توزيع المنتجات** `FEAT-COM-DISTRIBUTION`
  - `US-BC06-DST-CANCEL` — إلغاء التوزيع (أمر)
  - `US-BC06-DST-DISTRIBUTE` — تنفيذ التوزيع (أمر)
  - `US-BC06-Q-DST-LOG` — جلب: Distribution and delivery log with watermark ids (جلب)
  - `US-BC06-S-DISTRIBUTION-01` — تلقائي: all recipients authorized and delivered (التوزيع) (نظام)
  - `US-BC06-S-DISTRIBUTION-02` — تلقائي: some recipients not authorized (التوزيع) (نظام)
  - `US-UI-SCR43-DISTRIBUTE` — اختيار المستلمين ورؤية المستبعدين بعد التوزيع (واجهة، جديدة)
  - `US-UI-SCR43-RECIPIENT-VIEW` — المستلم يفتح المنتج الموزَّع إليه (واجهة، جديدة)
- **إعداد التقارير والإحاطات** `FEAT-COM-PRODUCT-AUTHORING`
  - `US-BC06-PRD-CREATE` — إنشاء المنتج (أمر)
  - `US-BC06-PRD-DISCARD` — تجاهل مسودة المنتج (أمر)
  - `US-BC06-PRD-EDIT-NARRATIVE` — تعديل سرد المنتج (أمر)
  - `US-BC06-PRD-GENERATE` — توليد المنتج (أمر)
  - `US-BC06-PRD-SUBMIT` — تقديم المنتج (أمر)
  - `US-BC06-S-PRODUCT-01` — تلقائي: generation succeeded (المنتج) (نظام)
  - `US-BC06-S-PRODUCT-02` — تلقائي: generation failed (المنتج) (نظام)
  - `US-UI-SCR43-CITATIONS` — كل عنصر في المنتج يقود إلى مصدره (واجهة، جديدة)
  - `US-UI-SCR43-GENERATION-STATUS` — تقدم توليد المنتج وسبب فشله (واجهة، جديدة)
  - `US-UI-SCR43-NARRATIVE-EDIT` — تحرير السرد فقط ووسم مسودة الذكاء الاصطناعي (واجهة، جديدة)
  - `US-PLT-PRD-LABEL-SUITE` — اختبار عدم تجاوز محتوى المنتج تصنيفه (منصة، جديدة)
  - `US-PLT-PRD-RENDER` — توليد منتج ثلاثين صفحة خلال دقيقتين (منصة، جديدة)
- **تصفح المنتجات وتنزيلها** `FEAT-COM-PRODUCT-LIBRARY`
  - `US-DOM-PRD-EXPORT` — تصدير نسخة شخصية بعلامة مائية (أمر، جديدة)
  - `US-BC06-Q-PRD-GET` — جلب: Product version with rendered artifacts (download grants) and pinned citations (جلب)
  - `US-BC06-Q-PRD-LIST` — جلب: Products by kind, state, situation/case, date (جلب)
  - `US-BC06-S-PRODUCT-03` — تلقائي: newer version approved (المنتج) (نظام)
  - `US-UI-SCR43-DOWNLOAD` — تنزيل المنتج بالصيغة المسموحة مع تنبيه العلامة (واجهة، جديدة)
  - `US-UI-SCR43-LIBRARY` — مكتبة المنتجات المعتمدة بأحدث نسخها (واجهة، جديدة)
  - `US-PLT-PRD-WATERMARK` — علامة مائية مرئية وخفية لكل نسخة (منصة، جديدة)
  - `US-OPS-PRD-LEAK-TRACE` — تتبع النسخة المسربة إلى مستلمها (تشغيل، جديدة)
- **مراجعة المنتجات واعتمادها** `FEAT-COM-PRODUCT-REVIEW`
  - `US-BC06-PRD-APPROVE` — اعتماد المنتج (أمر)
  - `US-BC06-PRD-RETURN` — إعادة المنتج للمراجعة (أمر)
  - `US-BC06-PRD-WITHDRAW` — سحب المنتج (أمر)
  - `US-UI-SCR06-PRODUCT-REVIEW` — المنتجات المقدّمة في قائمة مراجعتي (واجهة، جديدة)
  - `US-UI-SCR43-FROZEN-VERSION` — النسخة المعتمدة مجمدة وتنبيه بالأحدث (واجهة، جديدة)
  - `US-OPS-PRD-INTEGRITY` — التحقق من سلامة ملفات النسخ المعتمدة (تشغيل، جديدة)
- **قوالب المنتجات** `FEAT-COM-PRODUCT-TEMPLATES`
  - `US-BC06-PTM-ACTIVATE` — تفعيل قالب المنتج (أمر)
  - `US-BC06-PTM-DEFINE` — تعريف قالب المنتج (أمر)
  - `US-BC06-PTM-EDIT` — تعديل قالب المنتج (أمر)
  - `US-BC06-PTM-RETIRE` — إحالة قالب المنتج إلى التقاعد (أمر)
  - `US-DOM-PTM-LIST` — عرض قوالب المنتجات ونسخها (جلب، جديدة)
  - `US-UI-SCR43-TEMPLATE-EDITOR` — تحرير أقسام القالب وربط بياناته (واجهة، جديدة)
  - `US-UI-SCR43-TEMPLATES` — قائمة قوالب المنتجات وحالاتها (واجهة، جديدة)

</details>

### 2.11 CAP-11 — المعرفة والذاكرة المؤسسية

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **البحث في المعرفة وإعادة استخدامها** `FEAT-KNW-KNOWLEDGE-REUSE` | CAP-11.01 الدروس والمعرفة (R2) | يساعد المخطط والمستخدمين على إيجاد المعرفة المنشورة ذات الصلة بعملهم وتلقي اقتراحات منها وتسجيل الاستفادة منها. | المخطِّط؛ أي مستخدم مخوَّل | 3 + 4 |
| **مراجعة المعرفة ونشرها** `FEAT-KNW-KNOWLEDGE-REVIEW` | CAP-11.01 الدروس والمعرفة (R2) | يضمن أن ما يُنشر من معرفة مؤسسية قد راجعه مدير المعرفة واعتمده، وأن القديم منه يُسحب أو يُستبدل بنسخة أحدث. | مدير المعرفة؛ النظام | 5 + 3 |
| **تسجيل الدروس والمعرفة** `FEAT-KNW-LESSON-CAPTURE` | CAP-11.01 الدروس والمعرفة (R2) | يتيح لأي مستخدم توثيق درس أو إجراء أو ممارسة فضلى مرتبطة بمهمة أو خطة أو حادث مع أدلته وتقديمه للمراجعة. | أي مستخدم مخوَّل | 4 + 2 |
| **إتلاف السجلات المنتهية** `FEAT-KNW-DISPOSITION` | CAP-11.02 السجلات والاحتفاظ (R1 (الاحتفاظ والتجميد)) | ينفذ إتلاف أو أرشفة السجلات التي انتهت مدة حفظها بموافقة جهة مستقلة وبشهادة موثقة، مع استثناء المجمد منها. | أمين الأرشيف؛ السلطة القانونية والامتثال؛ المدقِّق؛ النظام | 8 + 5 |
| **التجميد القانوني** `FEAT-KNW-LEGAL-HOLD` | CAP-11.02 السجلات والاحتفاظ (R1 (الاحتفاظ والتجميد)) | يمنع إتلاف أو محو أو تعديل السجلات المطلوبة لقضية أو تحقيق حتى ترفع الجهة القانونية التجميد. | السلطة القانونية والامتثال؛ أمين الأرشيف؛ المدقِّق؛ النظام | 7 + 4 |
| **جداول الاحتفاظ بالسجلات** `FEAT-KNW-RETENTION-SCHEDULE` | CAP-11.02 السجلات والاحتفاظ (R1 (الاحتفاظ والتجميد)) | يحدد بوضوح كم تُحفظ كل فئة من السجلات وماذا يحدث لها بعد انتهاء المدة، بموافقة الجهة القانونية. | أمين الأرشيف؛ السلطة القانونية والامتثال؛ المدقِّق؛ النظام | 6 + 2 |
| **حفظ الأرشيف وسلامته** `FEAT-KNW-ARCHIVE-PRESERVE` | CAP-11.03 الأرشيف وإعادة البناء التاريخي (R2) | يضمن نقل السجلات المؤرشفة إلى حزم محفوظة بصيغ دائمة يُتحقق من سلامتها دوريًا وتُصلح أو تُرحَّل عند الحاجة. | أمين الأرشيف؛ الجهة المحيلة؛ النظام | 9 + 6 |
| **استرجاع السجلات التاريخية** `FEAT-KNW-ARCHIVE-RETRIEVE` | CAP-11.03 الأرشيف وإعادة البناء التاريخي (R2) | يمكّن المستخدم المخوَّل من البحث في فهرس الأرشيف واسترجاع سجل تاريخي ضمن الوقت المستهدف مع تسجيل كل وصول. | أي مستخدم مخوَّل؛ أمين الأرشيف | 2 + 5 |
| **إعادة البناء التاريخي** `FEAT-KNW-RECONSTRUCTION` | CAP-11.03 الأرشيف وإعادة البناء التاريخي (R2) | يجيب عن سؤال «ماذا كنا نعرف عن الوضع في وقت معيّن» بتقرير يميّز ما هو مسجل فعلًا عمّا أُعيد بناؤه. | المدقِّق؛ السلطة القانونية والامتثال؛ المحلل؛ النظام | 6 + 5 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-11 (86)</summary>

- **البحث في المعرفة وإعادة استخدامها** `FEAT-KNW-KNOWLEDGE-REUSE`
  - `US-BC06-KNO-RECORD-REUSE` — تسجيل إعادة استخدام كائن المعرفة (أمر)
  - `US-BC06-Q-KNO-SEARCH` — جلب: Published knowledge by type, text, relationships (جلب)
  - `US-BC06-Q-KNO-SUGGEST` — جلب: Published knowledge relevant to a task type / plan / area (by relationships) (جلب)
  - `US-UI-SCR34-KNOWLEDGE-SUGGEST` — اقتراح الدروس للمخطط أثناء إعداد الخطة (واجهة، جديدة)
  - `US-UI-SCR44-KNOWLEDGE-SEARCH` — البحث في المعرفة المنشورة وتصفيتها (واجهة، جديدة)
  - `US-PLT-KNOWLEDGE-SEARCH-DOC` — ظهور المعرفة المنشورة في البحث الموحد (منصة، جديدة)
  - `US-OPS-KNOWLEDGE-REUSE-METRIC` — قياس إعادة استخدام المعرفة ونجاح الاقتراحات (تشغيل، جديدة)
- **مراجعة المعرفة ونشرها** `FEAT-KNW-KNOWLEDGE-REVIEW`
  - `US-BC06-KNO-PUBLISH` — نشر كائن المعرفة (أمر)
  - `US-BC06-KNO-REJECT` — رفض كائن المعرفة (أمر)
  - `US-BC06-KNO-RETIRE` — إحالة كائن المعرفة إلى التقاعد (أمر)
  - `US-BC06-KNO-RETURN` — إعادة كائن المعرفة للمراجعة (أمر)
  - `US-DOM-KNO-REVIEW-QUEUE` — عرض المعرفة المنتظرة للمراجعة (جلب، جديدة)
  - `US-BC06-S-KNOWLEDGE-OBJECT-01` — تلقائي: newer version published (كائن المعرفة) (نظام)
  - `US-UI-SCR06-KNOWLEDGE-QUEUE` — قائمة مراجعة المعرفة لمدير المعرفة (واجهة، جديدة)
  - `US-UI-SCR44-KNOWLEDGE-REVIEW` — مراجعة كائن المعرفة ومقارنته بنسخته السابقة (واجهة، جديدة)
- **تسجيل الدروس والمعرفة** `FEAT-KNW-LESSON-CAPTURE`
  - `US-BC06-KNO-DISCARD` — تجاهل مسودة كائن المعرفة (أمر)
  - `US-BC06-KNO-DRAFT` — إعداد مسودة كائن المعرفة (أمر)
  - `US-BC06-KNO-EDIT` — تعديل كائن المعرفة (أمر)
  - `US-BC06-KNO-SUBMIT` — تقديم كائن المعرفة (أمر)
  - `US-UI-SCR02-LESSON-CAPTURE` — تسجيل درس من مهمة أو خطة مغلقة (واجهة، جديدة)
  - `US-UI-SCR44-LESSON-EDITOR` — صياغة عبارات الدرس وربطها بالأدلة (واجهة، جديدة)
- **إتلاف السجلات المنتهية** `FEAT-KNW-DISPOSITION`
  - `US-BC08-DSP-APPROVE` — اعتماد تشغيل الإتلاف (أمر)
  - `US-BC08-DSP-CANCEL` — إلغاء تشغيل الإتلاف (أمر)
  - `US-BC08-DSP-SUBMIT` — تقديم تشغيل الإتلاف (أمر)
  - `US-BC08-Q-DSP-GET` — جلب: Run with candidate summary, exceptions and certificate (جلب)
  - `US-BC08-S-DISPOSITION-RUN-01` — تلقائي: scheduled evaluation (daily) (تشغيل الإتلاف) (نظام)
  - `US-BC08-S-DISPOSITION-RUN-02` — تلقائي: execution started (تشغيل الإتلاف) (نظام)
  - `US-BC08-S-DISPOSITION-RUN-03` — تلقائي: all buckets processed (تشغيل الإتلاف) (نظام)
  - `US-BC08-S-DISPOSITION-RUN-04` — تلقائي: some buckets failed (تشغيل الإتلاف) (نظام)
  - `US-UI-SCR70-DISPOSITION-RUN` — مراجعة دورة الإتلاف قبل اعتمادها (واجهة، جديدة)
  - `US-PLT-DISPOSITION-EVAL-1H` — حساب مرشحي الإتلاف اليومي خلال ساعة (منصة، جديدة)
  - `US-PLT-DISPOSITION-PURGE-COPIES` — إزالة نسخ السجلات المتلفة من الفهارس والذاكرات (منصة، جديدة)
  - `US-OPS-DISPOSITION-CERT-EVIDENCE` — حفظ شهادة الإتلاف دليلًا غير قابل للتغيير (تشغيل، جديدة)
  - `US-OPS-DISPOSITION-FAILURE-ALERT` — التنبيه إلى فشل إتلاف بعض الحاويات (تشغيل، جديدة)
- **التجميد القانوني** `FEAT-KNW-LEGAL-HOLD`
  - `US-BC08-LHD-APPROVE-RELEASE` — اعتماد رفع التجميد القانوني (أمر)
  - `US-BC08-LHD-CANCEL-RELEASE` — إلغاء طلب رفع التجميد القانوني (أمر)
  - `US-BC08-LHD-EXTEND` — تمديد التجميد القانوني (أمر)
  - `US-BC08-LHD-PLACE` — إنشاء التجميد القانوني (أمر)
  - `US-BC08-LHD-REQUEST-RELEASE` — طلب رفع التجميد القانوني (أمر)
  - `US-DOM-LEGALHOLD-BLOCK-MODIFY` — منع تعديل السجلات المجمدة (أمر، جديدة)
  - `US-BC08-Q-LHD-CHECK` — جلب: HoldCheck OHS: URNs / subjects / (class, bucket) → held? with hold ids (جلب)
  - `US-BC08-Q-LHD-LIST` — جلب: Holds by state and scope (جلب)
  - `US-UI-SCR70-LEGAL-HOLD` — متابعة التجميدات القانونية والتحقق من سجل (واجهة، جديدة)
  - `US-PLT-LEGALHOLD-CHECK-CACHE` — فحص التجميد في كل سياق مع الإغلاق عند التعطل (منصة، جديدة)
  - `US-OPS-LEGALHOLD-BLOCKED-REPORT` — إبلاغ الجهة القانونية بمحاولات المساس بالمجمد (تشغيل، جديدة)
- **جداول الاحتفاظ بالسجلات** `FEAT-KNW-RETENTION-SCHEDULE`
  - `US-BC08-RTS-ACTIVATE` — تفعيل جدول الاحتفاظ (أمر)
  - `US-BC08-RTS-DISCARD` — تجاهل مسودة جدول الاحتفاظ (أمر)
  - `US-BC08-RTS-DRAFT` — إعداد مسودة جدول الاحتفاظ (أمر)
  - `US-BC08-RTS-EDIT` — تعديل جدول الاحتفاظ (أمر)
  - `US-BC08-Q-RTS-ACTIVE` — جلب: Active schedule version with rules (جلب)
  - `US-BC08-S-RETENTION-SCHEDULE-01` — تلقائي: successor activated (جدول الاحتفاظ) (نظام)
  - `US-UI-SCR70-RETENTION-RULES` — مراجعة قواعد الاحتفاظ لكل فئة سجلات (واجهة، جديدة)
  - `US-OPS-RETENTION-CLASS-GAP` — التنبيه إلى فئة سجلات بلا قاعدة احتفاظ (تشغيل، جديدة)
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
  - `US-UI-SCR44-ARCHIVE-PACKAGE` — متابعة حالة الحزمة الأرشيفية وأحداث حفظها (واجهة، جديدة)
  - `US-PLT-ARCHIVE-FIXITY-SCHEDULE` — التحقق الدوري من سلامة كل الحزم (منصة، جديدة)
  - `US-PLT-ARCHIVE-PACKAGE-BUILD` — بناء الحزمة الأرشيفية بصيغ الحفظ الدائمة (منصة، جديدة)
  - `US-PLT-ARCHIVE-WORM-REPLICA` — تخزين الأرشيف مقفلًا مع نسخة في موقع التعافي (منصة، جديدة)
  - `US-INT-ARCHIVE-TRANSFER-EXPORT` — تسليم الحزمة إلى أرشيف مستلم بإيصال (تكامل، جديدة)
  - `US-OPS-ARCHIVE-FIXITY-ALERT` — التنبيه الفوري لأي خلل في سلامة الأرشيف (تشغيل، جديدة)
- **استرجاع السجلات التاريخية** `FEAT-KNW-ARCHIVE-RETRIEVE`
  - `US-BC06-Q-ARC-RETRIEVE` — جلب: Retrieve package content (warm: signed grant; cold: staged job) — access logged (جلب)
  - `US-BC06-Q-ARC-SEARCH` — جلب: Archive catalogue (metadata only) by class, period, org (جلب)
  - `US-UI-SCR44-ARCHIVE-SEARCH` — البحث في فهرس الأرشيف ومعرفة زمن الاسترجاع (واجهة، جديدة)
  - `US-UI-SCR44-COLD-RETRIEVAL` — متابعة طلب استرجاع من الأرشيف البارد (واجهة، جديدة)
  - `US-PLT-ARCHIVE-COLD-STAGE` — تجهيز السجل البارد خلال 24 ساعة (منصة، جديدة)
  - `US-PLT-ARCHIVE-WARM-RETRIEVE` — استرجاع السجل الدافئ خلال دقيقة (منصة، جديدة)
  - `US-OPS-ARCHIVE-RETRIEVAL-SLO` — مراقبة زمن استرجاع الأرشيف لكل طبقة (تشغيل، جديدة)
- **إعادة البناء التاريخي** `FEAT-KNW-RECONSTRUCTION`
  - `US-BC06-REC-CANCEL` — إلغاء إعادة البناء التاريخي (أمر)
  - `US-BC06-REC-REQUEST` — طلب إعادة البناء التاريخي (أمر)
  - `US-BC06-Q-REC-REPORT` — جلب: Labelled reconstruction report (جلب)
  - `US-BC06-S-RECONSTRUCTION-01` — تلقائي: worker started (إعادة البناء التاريخي) (نظام)
  - `US-BC06-S-RECONSTRUCTION-02` — تلقائي: completed (إعادة البناء التاريخي) (نظام)
  - `US-BC06-S-RECONSTRUCTION-03` — تلقائي: failed (إعادة البناء التاريخي) (نظام)
  - `US-UI-SCR50-LABELLED-REPORT` — تمييز المسجل عن المعاد بناؤه في التقرير (واجهة، جديدة)
  - `US-UI-SCR50-REQUEST-FORM` — تحديد لحظة الموقف ولحظة المعرفة للطلب (واجهة، جديدة)
  - `US-PLT-RECONSTRUCTION-ARCHIVE-READ` — إدخال السجلات المؤرشفة في إعادة البناء (منصة، جديدة)
  - `US-PLT-RECONSTRUCTION-WORKER` — تنفيذ إعادة البناء مهمة غير متزامنة حتمية (منصة، جديدة)
  - `US-OPS-RECONSTRUCTION-ORACLE-CHECK` — فحص دوري لمطابقة إعادة البناء للمرجع (تشغيل، جديدة)

</details>

### 2.12 CAP-12 — المساعدة بالذكاء الاصطناعي

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **المساعد الذكي** `FEAT-AI-ASSISTANT` | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) | يتيح للمستخدم طرح سؤال على المساعد الذكي والحصول على إجابة مستندة إلى أدلة مع استشهاداتها، أو إبلاغه صراحة بعدم كفاية الأدلة. | أي مستخدم مخوَّل؛ النظام | 6 + 6 |
| **تأريض الإجابات بالأدلة المخوَّلة** `FEAT-AI-GROUNDING` | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) | يضمن أن المساعد لا يستخدم إلا البيانات التي يحق للسائل رؤيتها وأن كل عبارة في الإجابة مسندة إلى دليل يمكن تدقيقه. | النظام؛ المدقِّق | 5 + 8 |
| **توجيه نماذج الذكاء الاصطناعي** `FEAT-AI-ROUTING` | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) | يحدد لكل مستأجر أي نموذج يخدم أي نوع من الطلبات، محليًا افتراضيًا، ولا يُسمح بنموذج خارجي إلا بسياسة صريحة وبيانات غير مصنفة. | مهندس الذكاء الاصطناعي وحوكمته؛ صاحب السلطة أو المعتمِد الثاني؛ مسؤول الأمن؛ النظام | 6 + 4 |
| **سجل أدوات الذكاء الاصطناعي** `FEAT-AI-TOOLS` | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) | يضمن أن كل أداة يستخدمها الذكاء الاصطناعي مسجلة بصلاحيتها ومستوى استقلاليتها، ويمكن لمسؤول الأمن تفعيلها أو تعطيلها. | مهندس الذكاء الاصطناعي وحوكمته؛ مسؤول الأمن | 6 + 3 |
| **صياغة المسودات والملخصات** `FEAT-AI-DRAFTING` | CAP-12.02 الصياغة والتلخيص (R2) | يساعد المحلل والمدير على إعداد مسودات التقارير وملخصات الحالات بسرعة، مع وسمها بوضوح كمخرجات ذكاء اصطناعي. | المحلل؛ المدير؛ المخطِّط | 0 + 3 |
| **مراجعة نتائج الذكاء الاصطناعي** `FEAT-AI-RESULT-REVIEW` | CAP-12.02 الصياغة والتلخيص (R2) | يضمن ألا تُعتمد أو تُنشر أي نتيجة من الذكاء الاصطناعي إلا بعد أن يراجعها إنسان ويقبلها كليًا أو جزئيًا أو يرفضها بسبب. | المراجع؛ النظام | 6 + 3 |
| **استخراج المعلومات من الوثائق** `FEAT-AI-EXTRACTION` | CAP-12.03 الاستخراج والترجمة (R2) | يوفر على المحلل الجهد باستخراج الكيانات والأماكن والتواريخ من الوثائق كادعاءات مقترحة تنتظر قبوله. | المحلل؛ المراجع | 0 + 3 |
| **الترجمة بين العربية والإنجليزية** `FEAT-AI-TRANSLATION` | CAP-12.03 الاستخراج والترجمة (R2) | يتيح ترجمة النصوص بين العربية والإنجليزية عند الطلب مع بقاء النص الأصلي محفوظًا كما هو. | أي مستخدم مخوَّل | 0 + 4 |
| **حزم تقييم الذكاء الاصطناعي** `FEAT-AI-EVAL-SUITES` | CAP-12.04 تقييم AI وحوكمته (R2) | يحدد معايير ثابتة ومعتمدة لقياس جودة النماذج كالتأريض ودقة الاستشهاد ومعدل الهلوسة. | مهندس الذكاء الاصطناعي وحوكمته؛ صاحب السلطة أو المعتمِد الثاني؛ النظام | 4 + 4 |
| **تقييم النماذج واعتمادها** `FEAT-AI-MODEL-APPROVAL` | CAP-12.04 تقييم AI وحوكمته (R2) | يضمن ألا يدخل أي نموذج ذكاء اصطناعي إلى الاستخدام الفعلي إلا بعد تقييم موثق لدقته وتكلفته وموافقة بشرية. | مهندس الذكاء الاصطناعي وحوكمته؛ المدقِّق | 7 + 3 |
| **مراقبة النماذج وإيقافها** `FEAT-AI-MODEL-MONITOR` | CAP-12.04 تقييم AI وحوكمته (R2) | ينبه إلى تراجع أداء النموذج أثناء التشغيل ويتيح إيقاف استخدامه أو إعادته أو إحالته إلى التقاعد. | مهندس الذكاء الاصطناعي وحوكمته؛ النظام | 5 + 4 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-12 (90)</summary>

- **المساعد الذكي** `FEAT-AI-ASSISTANT`
  - `US-BC07-AIR-CANCEL` — إلغاء طلب الذكاء الاصطناعي (أمر)
  - `US-BC07-AIR-SUBMIT` — تقديم طلب الذكاء الاصطناعي (أمر)
  - `US-BC07-Q-AIR-GET` — جلب: Request with answer, statements and citations (visible only), status (جلب)
  - `US-BC07-S-AI-REQUEST-01` — تلقائي: policy denied (طلب الذكاء الاصطناعي) (نظام)
  - `US-BC07-S-AI-REQUEST-04` — تلقائي: no sufficient evidence retrieved (طلب الذكاء الاصطناعي) (نظام)
  - `US-BC07-S-AI-REQUEST-07` — تلقائي: error or timeout (طلب الذكاء الاصطناعي) (نظام)
  - `US-UI-SCR45-AIL-BADGE` — معرفة أن المخرج آلي ومستوى استقلاليته (واجهة، جديدة)
  - `US-UI-SCR45-CITATIONS` — فتح استشهاد كل عبارة في الإجابة (واجهة، جديدة)
  - `US-UI-SCR45-OUTCOMES` — فهم سبب غياب الإجابة (واجهة، جديدة)
  - `US-UI-SCR45-STREAMING` — عرض الإجابة تدريجيًا مع مرحلة المعالجة (واجهة، جديدة)
  - `US-PLT-AI-ANSWER-LATENCY` — أول رمز خلال 3 ثوانٍ والإجابة خلال 20 (منصة، جديدة)
  - `US-OPS-AI-SERVING-OUTAGE` — استمرار المنصة عند تعطل خدمة الذكاء الاصطناعي (تشغيل، جديدة)
- **تأريض الإجابات بالأدلة المخوَّلة** `FEAT-AI-GROUNDING`
  - `US-BC07-Q-AIR-CONTEXT` — جلب: Context package items (URN, version, label) — for audit and review (جلب)
  - `US-BC07-S-AI-REQUEST-02` — تلقائي: retrieval started (طلب الذكاء الاصطناعي) (نظام)
  - `US-BC07-S-AI-REQUEST-03` — تلقائي: context package sealed (طلب الذكاء الاصطناعي) (نظام)
  - `US-BC07-S-AI-REQUEST-05` — تلقائي: output grounded (طلب الذكاء الاصطناعي) (نظام)
  - `US-BC07-S-AI-REQUEST-06` — تلقائي: output not grounded (طلب الذكاء الاصطناعي) (نظام)
  - `US-UI-SCR69-AI-LINEAGE` — تتبع العبارة إلى حزمة السياق والنموذج (واجهة، جديدة)
  - `US-PLT-AI-AUTONOMY-MATRIX` — فرض حدود استقلالية الذكاء الاصطناعي (منصة، جديدة)
  - `US-PLT-AI-GROUNDING-VERIFIER` — التحقق من إسناد كل عبارة قبل عرضها (منصة، جديدة)
  - `US-PLT-AI-INJECTION-GUARD` — معاملة المحتوى المسترجع بيانات لا تعليمات (منصة، جديدة)
  - `US-PLT-AI-LINEAGE-RECORD` — حفظ أصل كل مخرج آلي مختومًا ومشفرًا (منصة، جديدة)
  - `US-PLT-AI-VECTOR-PROJECTION` — استرجاع متجهي بنفس تسميات البحث وتصفيته (منصة، جديدة)
  - `US-OPS-AI-INJECTION-ALERT` — إحالة ارتفاع محاولات الحقن إلى الأمن (تشغيل، جديدة)
  - `US-OPS-AI-VECTOR-LAG` — مراقبة تأخر الإسقاط المتجهي (تشغيل، جديدة)
- **توجيه نماذج الذكاء الاصطناعي** `FEAT-AI-ROUTING`
  - `US-BC07-RTG-ACTIVATE` — تفعيل توجيه الذكاء الاصطناعي (أمر)
  - `US-BC07-RTG-DISCARD` — تجاهل مسودة توجيه الذكاء الاصطناعي (أمر)
  - `US-BC07-RTG-DRAFT` — إعداد مسودة توجيه الذكاء الاصطناعي (أمر)
  - `US-BC07-RTG-EDIT` — تعديل توجيه الذكاء الاصطناعي (أمر)
  - `US-DOM-AI-PROMPT-TEMPLATE` — إدارة نسخ قوالب التعليمات (أمر، جديدة)
  - `US-BC07-Q-RTG-ACTIVE` — جلب: Active routing for the tenant (جلب)
  - `US-BC07-S-AI-ROUTING-01` — تلقائي: successor activated (توجيه الذكاء الاصطناعي) (نظام)
  - `US-UI-SCR51-ROUTING` — مراجعة توجيه كل عملية قبل تفعيله (واجهة، جديدة)
  - `US-INT-AI-EXTERNAL-MODEL` — استدعاء نموذج خارجي بسياسة وبيانات غير مصنفة فقط (تكامل، جديدة)
  - `US-OPS-AI-EGRESS-MONITOR` — رصد أي خروج إلى نموذج خارجي دون سياسة (تشغيل، جديدة)
- **سجل أدوات الذكاء الاصطناعي** `FEAT-AI-TOOLS`
  - `US-BC07-TOL-ACTIVATE` — تفعيل أداة الذكاء الاصطناعي (أمر)
  - `US-BC07-TOL-DISABLE` — تعطيل أداة الذكاء الاصطناعي (أمر)
  - `US-BC07-TOL-ENABLE` — تمكين أداة الذكاء الاصطناعي (أمر)
  - `US-BC07-TOL-REGISTER` — تسجيل أداة الذكاء الاصطناعي (أمر)
  - `US-BC07-TOL-RETIRE` — إحالة أداة الذكاء الاصطناعي إلى التقاعد (أمر)
  - `US-BC07-Q-TOL-LIST` — جلب: Tool registry (جلب)
  - `US-UI-SCR51-TOOLS` — إدارة سجل الأدوات حسب الحالة (واجهة، جديدة)
  - `US-PLT-AI-TOOL-GATE` — منع استدعاء أداة غير مسجلة أو معطلة (منصة، جديدة)
  - `US-OPS-AI-TOOL-REVIEW-EVIDENCE` — توثيق المراجعة الأمنية قبل تفعيل الأداة (تشغيل، جديدة)
- **صياغة المسودات والملخصات** `FEAT-AI-DRAFTING`
  - `US-UI-SCR30-AI-SUMMARY` — تلخيص الحالة التحليلية بمسودة موسومة (واجهة، جديدة)
  - `US-UI-SCR43-AI-DRAFT-SECTION` — طلب مسودة آلية لقسم سردي في المنتج (واجهة، جديدة)
  - `US-UI-SCR45-AI-DRAFT-HANDOFF` — إرسال مسودة من المساعد إلى المراجعة (واجهة، جديدة)
- **مراجعة نتائج الذكاء الاصطناعي** `FEAT-AI-RESULT-REVIEW`
  - `US-BC07-AIRS-ACCEPT` — قبول نتيجة الذكاء الاصطناعي (أمر)
  - `US-BC07-AIRS-ACCEPT-PARTIALLY` — قبول نتيجة الذكاء الاصطناعي جزئيًا (أمر)
  - `US-BC07-AIRS-REJECT` — رفض نتيجة الذكاء الاصطناعي (أمر)
  - `US-BC07-AIRS-START-REVIEW` — بدء مراجعة نتيجة الذكاء الاصطناعي (أمر)
  - `US-BC07-Q-AIRS-QUEUE` — جلب: Reviewable AI results by state, operation, target (جلب)
  - `US-BC07-S-AI-RESULT-01` — تلقائي: request COMPLETED for a reviewable operation (نتيجة الذكاء الاصطناعي) (نظام)
  - `US-UI-SCR06-AI-QUEUE` — قائمة نتائج الذكاء الاصطناعي المنتظرة للمراجعة (واجهة، جديدة)
  - `US-UI-SCR46-ITEM-SELECT` — قبول عناصر محددة من النتيجة ورفض الباقي (واجهة، جديدة)
  - `US-OPS-AI-REJECTION-FEEDBACK` — تغذية أسباب الرفض إلى تقييم النماذج (تشغيل، جديدة)
- **استخراج المعلومات من الوثائق** `FEAT-AI-EXTRACTION`
  - `US-UI-SCR22-AI-EXTRACT` — طلب استخراج الكيانات من وثيقة (واجهة، جديدة)
  - `US-UI-SCR46-EXTRACT-ITEMS` — مراجعة المستخرج مقابل موضعه في الوثيقة (واجهة، جديدة)
  - `US-PLT-AI-EXTRACTION-BATCH` — استخراج دفعي من الوثائق بحصص المستأجر (منصة، جديدة)
- **الترجمة بين العربية والإنجليزية** `FEAT-AI-TRANSLATION`
  - `US-DOM-AI-TRANSLATION-EVIDENCE` — اعتماد الترجمة دليلًا بعد مراجعة بشرية (أمر، جديدة)
  - `US-DOM-AI-TRANSLATION-LINK` — حفظ الترجمة مرتبطة بأصلها (أمر، جديدة)
  - `US-UI-SCR22-AI-TRANSLATE` — عرض الترجمة بجانب النص الأصلي (واجهة، جديدة)
  - `US-UI-SCR45-AI-TRANSLATE-TEXT` — ترجمة نص من المساعد مع حفظ الأصل (واجهة، جديدة)
- **حزم تقييم الذكاء الاصطناعي** `FEAT-AI-EVAL-SUITES`
  - `US-BC07-EVS-ACTIVATE` — تفعيل حزمة التقييم (أمر)
  - `US-BC07-EVS-DRAFT` — إعداد مسودة حزمة التقييم (أمر)
  - `US-BC07-EVS-EDIT` — تعديل حزمة التقييم (أمر)
  - `US-DOM-AI-THRESHOLD-CALIBRATE` — معايرة عتبات التأريض باعتماد موثق (أمر، جديدة)
  - `US-BC07-S-EVAL-SUITE-01` — تلقائي: successor activated (حزمة التقييم) (نظام)
  - `US-UI-SCR51-EVAL-SUITES` — مراجعة اكتمال حزمة التقييم قبل تفعيلها (واجهة، جديدة)
  - `US-PLT-AI-EVAL-HARNESS` — تشغيل حزمة التقييم على إصدار نموذج (منصة، جديدة)
  - `US-OPS-AI-SECURITY-SUITE-GATE` — تشغيل حزم أمن الذكاء الاصطناعي قبل كل إصدار (تشغيل، جديدة)
- **تقييم النماذج واعتمادها** `FEAT-AI-MODEL-APPROVAL`
  - `US-BC07-MDL-APPROVE` — اعتماد إصدار النموذج (أمر)
  - `US-BC07-MDL-FAIL-EVALUATION` — تسجيل فشل تقييم إصدار النموذج (أمر)
  - `US-BC07-MDL-PROMOTE` — ترقية إصدار النموذج (أمر)
  - `US-BC07-MDL-REGISTER` — تسجيل إصدار النموذج (أمر)
  - `US-BC07-MDL-STAGE` — تجهيز إصدار النموذج للإنتاج (أمر)
  - `US-BC07-MDL-START-EVALUATION` — بدء تقييم إصدار النموذج (أمر)
  - `US-BC07-Q-MDL-LIST` — جلب: Model versions with state, evaluation summary, hosting (جلب)
  - `US-UI-SCR51-MODEL-LIFECYCLE` — متابعة إصدارات النماذج وتقييمها (واجهة، جديدة)
  - `US-PLT-AI-CANARY-SPLIT` — توجيه حصة تجريبية إلى النموذج المجهز (منصة، جديدة)
  - `US-OPS-AI-MODEL-BUNDLE` — تثبيت أوزان النموذج موقعة في حزمة الإصدار (تشغيل، جديدة)
- **مراقبة النماذج وإيقافها** `FEAT-AI-MODEL-MONITOR`
  - `US-BC07-MDL-DEPRECATE` — إهمال إصدار النموذج (إيقاف الاستخدام الجديد) (أمر)
  - `US-BC07-MDL-REINSTATE` — إعادة إصدار النموذج إلى السريان (أمر)
  - `US-BC07-MDL-RETIRE` — إحالة إصدار النموذج إلى التقاعد (أمر)
  - `US-BC07-Q-AI-USAGE` — جلب: GPU-hours, requests, cost indicators per tenant and operation (جلب)
  - `US-BC07-S-MODEL-VERSION-01` — تلقائي: monitoring drift detected (إصدار النموذج) (نظام)
  - `US-UI-SCR51-USAGE` — متابعة استهلاك الذكاء الاصطناعي وتكلفته (واجهة، جديدة)
  - `US-PLT-AI-USAGE-METERING` — قياس ساعات GPU والطلبات لكل مستأجر (منصة، جديدة)
  - `US-OPS-AI-DRIFT-SAMPLE` — عينة تقييم أسبوعية للنموذج في الإنتاج (تشغيل، جديدة)
  - `US-OPS-AI-QUALITY-ALERTS` — التنبيه إلى تراجع جودة النموذج أو سرعته (تشغيل، جديدة)

</details>

### 2.13 CAP-13 — الحوكمة والأمن والامتثال

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **مخطط التصنيف الأمني** `FEAT-GOV-CLASSIFICATION` | CAP-13.01 التصنيف والسياسات (R1) | يتيح لمسؤول الأمن تحديد مستويات السرية والحجرات وقيود الإفراج الخاصة بالمستأجر واعتمادها، ويعرضها لكل مستخدم. | مسؤول الأمن؛ أي مستخدم مخوَّل؛ النظام | 6 + 5 |
| **التصاريح الأمنية للمستخدمين** `FEAT-GOV-CLEARANCE` | CAP-13.01 التصنيف والسياسات (R1) | يتيح لمسؤول الأمن منح كل مستخدم مستوى سرية وحجرات محددة واعتمادها وتعديلها وتعليقها وسحبها، فلا يرى إلا ما يسمح به تصريحه. | مسؤول الأمن؛ أي مستخدم مخوَّل؛ النظام | 8 + 3 |
| **الاستثناءات الأمنية المؤقتة** `FEAT-GOV-EXCEPTIONS` | CAP-13.01 التصنيف والسياسات (R1) | يتيح للمستخدم طلب استثناء أمني مؤقت بمبرر واضح يعتمده شخصان مخولان، ويُسحب تلقائيًا عند انتهاء مدته. | أي مستخدم مخوَّل؛ مسؤول الأمن؛ المدقِّق؛ النظام | 6 + 5 |
| **التسجيل التلقائي للعمليات** `FEAT-GOV-AUDIT-CAPTURE` | CAP-13.02 التدقيق (R1) | يضمن تسجيل كل تغيير وكل اطلاع على بيانات حساسة تلقائيًا مع الفاعل والغرض وقرار الوصول، دون أن يتمكن أحد من تعديل السجل أو حذفه. | النظام | 0 + 6 |
| **مراجعة سجل التدقيق** `FEAT-GOV-AUDIT-TRAIL` | CAP-13.02 التدقيق (R1) | يتيح للمدقق ومسؤول الأمن البحث في سجل من فعل ماذا ومتى ولماذا والتحقق من أن السجل لم يُعبث به. | المدقِّق؛ مسؤول الأمن | 2 + 5 |
| **محو البيانات الشخصية** `FEAT-GOV-ERASURE` | CAP-13.03 الخصوصية والاحتفاظ (R1) | يتيح لمسؤول الخصوصية تسجيل طلب محو بيانات شخص يعتمده مرجع قانوني مستقل، ثم يمحوها من كل أجزاء المنصة مع إصدار شهادة دون فقدان حقائق التدقيق. | السلطة القانونية والامتثال؛ مسؤول الإدارة؛ المدقِّق؛ النظام | 10 + 4 |
| **إقامة البيانات وسيادتها** `FEAT-GOV-DATA-RESIDENCY` | CAP-13.04 السيادة وإقامة البيانات (R1) | يضمن بقاء جميع بيانات الجهة داخل نطاقها الجغرافي والقانوني المحدد وعدم نقلها خارجه إلا بسياسة صريحة من المستأجر. | مسؤول الأمن؛ مشغّل المنصة؛ النظام | 0 + 8 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-13 (68)</summary>

- **مخطط التصنيف الأمني** `FEAT-GOV-CLASSIFICATION`
  - `US-BC08-CLS-ACTIVATE` — تفعيل مخطط التصنيف (أمر)
  - `US-BC08-CLS-DISCARD` — تجاهل مسودة مخطط التصنيف (أمر)
  - `US-BC08-CLS-DRAFT` — إعداد مسودة مخطط التصنيف (أمر)
  - `US-BC08-CLS-EDIT` — تعديل مخطط التصنيف (أمر)
  - `US-BC08-Q-CLS-ACTIVE` — جلب: Active scheme (labels only) (جلب)
  - `US-BC08-S-CLASSIFICATION-SCHEME-01` — تلقائي: successor activated (مخطط التصنيف) (نظام)
  - `US-UI-SCR67-SCHEME-EDITOR` — تحرير مستويات التصنيف وأقسامه وتحفظاته (واجهة، جديدة)
  - `US-PLT-CLS-COMPOSITE-LABEL` — تصنيف الكائن المركب بأعلى مكوناته (منصة، جديدة)
  - `US-PLT-CLS-LABEL-REQUIRED` — إلزام التصنيف عند إنشاء الكائنات المهمة (منصة، جديدة)
  - `US-PLT-CLS-RECLASSIFY-PROPAGATION` — نفاذ تغيير التصنيف فورًا في كل المسارات (منصة، جديدة)
  - `US-PLT-CLS-UI-BADGE` — شارة التصنيف على كل كائن ونموذج (منصة، جديدة)
- **التصاريح الأمنية للمستخدمين** `FEAT-GOV-CLEARANCE`
  - `US-BC01-CLR-APPROVE` — اعتماد التصريح الأمني (أمر)
  - `US-BC01-CLR-GRANT` — منح التصريح الأمني (أمر)
  - `US-BC01-CLR-MODIFY` — تعديل التصريح الأمني (أمر)
  - `US-BC01-CLR-REINSTATE` — إعادة التصريح الأمني إلى السريان (أمر)
  - `US-BC01-CLR-REVOKE` — سحب التصريح الأمني (أمر)
  - `US-BC01-CLR-SUSPEND` — تعليق التصريح الأمني (أمر)
  - `US-BC01-Q-CLR-GET` — جلب: Current clearance (level/compartments) (جلب)
  - `US-BC01-S-CLEARANCE-01` — تلقائي: valid_to reached (التصريح الأمني) (نظام)
  - `US-UI-SCR67-CLEARANCE-VIEW` — عرض تصريح المستخدم وحالة اعتماده (واجهة، جديدة)
  - `US-PLT-CLR-READ-RULE` — السماح بالقراءة حسب التصريح والأقسام (منصة، جديدة)
  - `US-OPS-CLR-AGGREGATE-REPORT` — تقرير مجمّع بالتصاريح حسب المستوى (تشغيل، جديدة)
- **الاستثناءات الأمنية المؤقتة** `FEAT-GOV-EXCEPTIONS`
  - `US-BC08-EXC-APPROVE` — اعتماد الاستثناء الأمني (أمر)
  - `US-BC08-EXC-REJECT` — رفض الاستثناء الأمني (أمر)
  - `US-BC08-EXC-REQUEST` — طلب الاستثناء الأمني (أمر)
  - `US-BC08-EXC-REVOKE` — سحب الاستثناء الأمني (أمر)
  - `US-BC08-Q-EXC-LIST` — جلب: Exceptions by state (جلب)
  - `US-BC08-S-SECURITY-EXCEPTION-01` — تلقائي: end reached (الاستثناء الأمني) (نظام)
  - `US-UI-SCR67-EXCEPTIONS` — متابعة الاستثناءات وموعد انتهائها ومعتمديها (واجهة، جديدة)
  - `US-PLT-EXC-PDP-APPLY` — تطبيق الاستثناء النشط في قرار الوصول (منصة، جديدة)
  - `US-OPS-BREAKGLASS-REVIEW` — مراجعة مستقلة لكل وصول طارئ (تشغيل، جديدة)
  - `US-OPS-BREAKGLASS-TENANT-ACCESS` — وصول طارئ مؤقت للمشغل بموافقة الأمن (تشغيل، جديدة)
  - `US-OPS-EXC-WEEKLY-REPORT` — تقرير أسبوعي بالاستثناءات النشطة للمدقق (تشغيل، جديدة)
- **التسجيل التلقائي للعمليات** `FEAT-GOV-AUDIT-CAPTURE`
  - `US-PLT-AUDIT-ATOMIC-WRITE` — سجل تدقيق واحد مع كل تغيير (منصة، جديدة)
  - `US-PLT-AUDIT-BUFFER-FAILCLOSED` — الاستمرار عند تعطل مخزن التدقيق ثم الرفض (منصة، جديدة)
  - `US-PLT-AUDIT-HASH-CHAIN` — سلسلة لا تقبل التعديل لسجلات التدقيق (منصة، جديدة)
  - `US-PLT-AUDIT-SENSITIVE-READS` — تدقيق قراءة البيانات فوق عتبة المستأجر (منصة، جديدة)
  - `US-OPS-AUDIT-DAILY-VERIFY` — تحقق يومي من سلاسل التدقيق واكتمالها (تشغيل، جديدة)
  - `US-OPS-AUDIT-LAG-ALERT` — تنبيه عند تأخر شحن سجلات التدقيق (تشغيل، جديدة)
- **مراجعة سجل التدقيق** `FEAT-GOV-AUDIT-TRAIL`
  - `US-BC08-Q-AUD-SEARCH` — جلب: Audit records by actor, resource, time, correlation id (جلب)
  - `US-BC08-Q-AUD-VERIFY` — جلب: Start integrity verification job; returns job ref (جلب)
  - `US-UI-SCR69-AUDIT-SEARCH` — البحث في سجل التدقيق بمرشحات متعددة (واجهة، جديدة)
  - `US-UI-SCR69-INTEGRITY-RESULT` — عرض نتيجة التحقق من سلامة السجل (واجهة، جديدة)
  - `US-PLT-AUDIT-SEARCH-SELF-AUDIT` — تدقيق كل اطلاع على سجل التدقيق (منصة، جديدة)
  - `US-PLT-AUDIT-TRACE-LINK` — ربط سجل التدقيق بتتبع الطلب (منصة، جديدة)
  - `US-OPS-AUDIT-CHAIN-INCIDENT` — معالجة فشل سلامة السجل حادثًا حرجًا (تشغيل، جديدة)
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
  - `US-UI-SCR70-ERASURE-PROGRESS` — متابعة تأكيدات المحو وشهادته (واجهة، جديدة)
  - `US-PLT-ERASURE-CONTEXT-PURGE` — إفراغ كل جزء نسخه الواضحة خلال يوم (منصة، جديدة)
  - `US-PLT-ERASURE-KEY-SHRED` — محو البيانات الشخصية بإتلاف مفتاح صاحبها (منصة، جديدة)
  - `US-OPS-ERASURE-DEADLINE-ALERT` — تنبيه عند تأخر تأكيد المحو (تشغيل، جديدة)
- **إقامة البيانات وسيادتها** `FEAT-GOV-DATA-RESIDENCY`
  - `US-UI-SCR60-RESIDENCY` — عرض ولاية المستأجر وخليته ونمطها (واجهة، جديدة)
  - `US-PLT-RESIDENCY-EGRESS-DENY` — منع خروج البيانات خارج الولاية افتراضيًا (منصة، جديدة)
  - `US-PLT-RESIDENCY-TRANSFER-POLICY` — السماح بالنقل الخارجي بسياسة صريحة فقط (منصة، جديدة)
  - `US-OPS-KEYS-ROTATION` — تدوير المفاتيح دوريًا وعند الاشتباه (تشغيل، جديدة)
  - `US-OPS-KEYS-TENANT-HIERARCHY` — مفاتيح تشفير خاصة بكل مستأجر (تشغيل، جديدة)
  - `US-OPS-RESIDENCY-DR-SITE` — بقاء النسخ وموقع التعافي داخل الولاية (تشغيل، جديدة)
  - `US-OPS-RESIDENCY-EGRESS-ALERT` — مراقبة خروج الشبكة والتنبيه الفوري (تشغيل، جديدة)
  - `US-OPS-SECRETS-STORE` — حفظ الأسرار خارج الكود والصور (تشغيل، جديدة)

</details>

### 2.14 CAP-14 — تشغيل المنصة

| الميزة | القدرة الفرعية | القيمة | الأدوار | القصص |
|---|---|---|---|---|
| **واجهة عربية وإنجليزية** `FEAT-PLT-LOCALIZATION` | CAP-14.01 المراقبة (R1) | يتيح لكل مستخدم العمل بالعربية أو الإنجليزية باتجاه الكتابة المناسب مع إمكانية عرض التاريخ الهجري. | أي مستخدم مخوَّل | 0 + 11 |
| **مراقبة صحة المنصة** `FEAT-PLT-MONITORING` | CAP-14.01 المراقبة (R1) | يمكّن مشغل المنصة من رؤية صحة كل مكونات المنصة وأدائها وتتبع أي طلب عبرها، ومتابعة مؤشرات نتائج الأعمال. | مشغّل المنصة | 0 + 11 |
| **التثبيت والترقية دون اتصال** `FEAT-PLT-AIRGAP-UPGRADE` | CAP-14.02 الاعتمادية والتعافي (R1) | يتيح تثبيت المنصة وترقيتها وتشغيلها في بيئة معزولة عن الإنترنت مع بقاء الواجهات القديمة تعمل عند إصدار نسخ جديدة. | مشغّل المنصة | 0 + 10 |
| **متابعة العمليات الطويلة** `FEAT-PLT-BACKGROUND-JOBS` | CAP-14.02 الاعتمادية والتعافي (R1) | يتيح للمستخدم متابعة العمليات الثقيلة كالاستيراد الكبير والتقارير والتحليلات وهي تعمل في الخلفية وإعادة محاولتها أو إلغاءها. | أي مستخدم مخوَّل؛ مشغّل المنصة؛ النظام | 0 + 6 |
| **النسخ الاحتياطي والاستعادة** `FEAT-PLT-BACKUP-RESTORE` | CAP-14.02 الاعتمادية والتعافي (R1) | يضمن نسخ جميع البيانات احتياطيًا حسب أهميتها والتحقق آليًا من إمكانية استعادتها ضمن المدد المتفق عليها. | مشغّل المنصة؛ النظام | 0 + 8 |
| **موثوقية الأحداث والإسقاطات** `FEAT-PLT-EVENT-DELIVERY` | CAP-14.02 الاعتمادية والتعافي (R1) | يضمن وصول كل حدث مرة واحدة فعليًا إلى الأجزاء المعنية، ويحجز الرسائل التي يتعذر معالجتها حتى تُعالج، فلا يضيع أي تحديث. | مشغّل المنصة؛ النظام | 0 + 14 |
| **نقل المستأجر بين خلايا التشغيل** `FEAT-PLT-CELL-MIGRATION` | CAP-14.03 تهيئة المستأجرين والحصص (R1) | يتيح لمشغل المنصة نقل مستأجر إلى خلية تشغيل أخرى (مشتركة أو مخصصة أو سيادية) دون فقدان بيانات، بنفس نسخة البرنامج في كل البيئات. | مشغّل المنصة؛ النظام | 2 + 5 |
| **حصص المستأجر وحدود الاستخدام** `FEAT-PLT-TENANT-QUOTAS` | CAP-14.03 تهيئة المستأجرين والحصص (R1) | يتيح لمشغل المنصة تحديد حصص كل مستأجر من الطلبات والتخزين والأحداث والمهام وفرضها، حتى لا يؤثر مستأجر على غيره. | مشغّل المنصة؛ مسؤول الإدارة؛ النظام | 1 + 8 |

القصص: من المواصفة + الجديدة. والعنوان المربوط ميزة لها ملف.

<details><summary>قصص ميزات CAP-14 (76)</summary>

- **واجهة عربية وإنجليزية** `FEAT-PLT-LOCALIZATION`
  - `US-PLT-A11Y-FIELD-TOUCH` — أهداف لمس كبيرة للاستعمال بيد واحدة (منصة، جديدة)
  - `US-PLT-A11Y-NOT-COLOR-ONLY` — الحالة والخطورة لا تعتمدان على اللون (منصة، جديدة)
  - `US-PLT-A11Y-WCAG-AA` — توافق شاشات الويب مع WCAG 2.2 AA (منصة، جديدة)
  - `US-PLT-L10N-BIDI-ISOLATION` — عرض النص المختلط دون انقلاب الجملة (منصة، جديدة)
  - `US-PLT-L10N-EMBEDDED-FONT` — خط عربي ولاتيني مضمّن دون إنترنت (منصة، جديدة)
  - `US-PLT-L10N-HIJRI-DATES` — عرض التاريخ الهجري اختياريًا (منصة، جديدة)
  - `US-PLT-L10N-LANGUAGE-SWITCH` — تبديل لغة الواجهة لكل مستخدم (منصة، جديدة)
  - `US-PLT-L10N-NUMERALS` — أرقام عربية أو لاتينية حسب التفضيل (منصة، جديدة)
  - `US-PLT-L10N-RTL-LAYOUT` — اتجاه الصفحة الصحيح في كل الشاشات (منصة، جديدة)
  - `US-PLT-L10N-TIME-ZONE` — عرض الوقت بتوقيت المستخدم المحلي (منصة، جديدة)
  - `US-PLT-UI-RESPONSIVE` — الواجهة تعمل من عرض 360 بكسل (منصة، جديدة)
- **مراقبة صحة المنصة** `FEAT-PLT-MONITORING`
  - `US-PLT-MON-BUSINESS-TELEMETRY` — قياس مؤشرات نتائج الأعمال (منصة، جديدة)
  - `US-PLT-MON-CORRELATION-TRACE` — تتبع أي طلب من بدايته إلى نهايته (منصة، جديدة)
  - `US-PLT-MON-LOG-HYGIENE` — سجلات تقنية بلا بيانات شخصية (منصة، جديدة)
  - `US-PLT-MON-TELEMETRY` — مقاييس وسجلات موحدة لكل مكوّن (منصة، جديدة)
  - `US-OPS-MON-ALERT-SEVERITY` — تصنيف التنبيهات حسب الخطورة والاستدعاء (تشغيل، جديدة)
  - `US-OPS-MON-CLOCK-SYNC` — مزامنة ساعات الخلية والتنبيه للانحراف (تشغيل، جديدة)
  - `US-OPS-MON-DASHBOARDS` — لوحات صحة لكل وحدة نشر (تشغيل، جديدة)
  - `US-OPS-MON-LATENCY-SLO` — تنبيه عند تجاوز أهداف زمن الاستجابة (تشغيل، جديدة)
  - `US-OPS-MON-RETENTION` — احتفاظ محدود بالسجلات والتتبع والمقاييس (تشغيل، جديدة)
  - `US-OPS-MON-SECURITY-INCIDENT` — الاستجابة للحوادث الأمنية الحرجة (تشغيل، جديدة)
  - `US-OPS-MON-SLO-BUDGET` — متابعة أهداف التوفر وميزانية الخطأ (تشغيل، جديدة)
- **التثبيت والترقية دون اتصال** `FEAT-PLT-AIRGAP-UPGRADE`
  - `US-PLT-AIRGAP-NO-INTERNET` — لا اعتماد على الإنترنت في البناء والتشغيل (منصة، جديدة)
  - `US-PLT-API-CURSOR-PAGINATION` — ترقيم القوائم بالمؤشر فقط (منصة، جديدة)
  - `US-PLT-API-ERROR-MODEL` — نموذج خطأ موحد في كل الاستجابات (منصة، جديدة)
  - `US-PLT-CONTRACT-VERSIONING` — تعايش الإصدار الرئيسي السابق ستة أشهر (منصة، جديدة)
  - `US-OPS-CONFIG-GITOPS` — تغيير إعدادات المنصة بمراجعة شخصين (تشغيل، جديدة)
  - `US-OPS-ENV-PROMOTION` — ترقية الحزمة نفسها بين البيئات (تشغيل، جديدة)
  - `US-OPS-INSTALL-AIRGAPPED` — تثبيت المنصة في شبكة معزولة (تشغيل، جديدة)
  - `US-OPS-RELEASE-BUNDLE` — بناء حزمة إصدار واحدة موقعة (تشغيل، جديدة)
  - `US-OPS-RELEASE-VERIFY` — التحقق من توقيع الحزمة قبل التثبيت (تشغيل، جديدة)
  - `US-OPS-UPGRADE-ROLLBACK` — ترقية دون توقف مع رجوع خلال ساعة (تشغيل، جديدة)
- **متابعة العمليات الطويلة** `FEAT-PLT-BACKGROUND-JOBS`
  - `US-PLT-JOBS-ASYNC-ONLY` — تشغيل العمليات الثقيلة في الخلفية فقط (منصة، جديدة)
  - `US-PLT-JOBS-RETRY-CANCEL` — إعادة العملية الطويلة أو إلغاؤها (منصة، جديدة)
  - `US-PLT-JOBS-STATUS` — متابعة حالة العملية الطويلة وتقدمها (منصة، جديدة)
  - `US-PLT-JOBS-TIMERS-LEASES` — مؤقتات وعمال موثوقون دون محرك سير عمل (منصة، جديدة)
  - `US-PLT-JOBS-UI-PROGRESS` — مكوّن موحد لعرض تقدم العمليات (منصة، جديدة)
  - `US-OPS-JOBS-STUCK-ALERT` — تنبيه عند تجاوز العملية مهلتها (تشغيل، جديدة)
- **النسخ الاحتياطي والاستعادة** `FEAT-PLT-BACKUP-RESTORE`
  - `US-PLT-BACKUP-KEYSTORE` — نسخ مخزن المفاتيح مع سجل الإتلاف (منصة، جديدة)
  - `US-PLT-BACKUP-SEARCH-SNAPSHOTS` — لقطات فهارس البحث كل ربع ساعة (منصة، جديدة)
  - `US-PLT-BACKUP-STORES` — نسخ كل المخازن حسب طبقة خدمتها (منصة، جديدة)
  - `US-OPS-BACKUP-RESTORE-GATE` — منع عودة المفاتيح المتلفة بعد الاستعادة (تشغيل، جديدة)
  - `US-OPS-BACKUP-RESTORE-TEST` — اختبار استعادة آلي أسبوعي (تشغيل، جديدة)
  - `US-OPS-DR-QUARTERLY-DRILL` — تمرين تعافٍ ربع سنوي ضمن الأهداف (تشغيل، جديدة)
  - `US-OPS-DR-TIER-ASSIGNMENT` — طبقة خدمة محددة لكل قدرة (تشغيل، جديدة)
  - `US-OPS-HA-REDUNDANCY` — نسختان على الأقل لكل وحدة حرجة (تشغيل، جديدة)
- **موثوقية الأحداث والإسقاطات** `FEAT-PLT-EVENT-DELIVERY`
  - `US-UI-SCR71-DEAD-LETTERS` — عرض الرسائل المحجوزة للمشغل دون محتواها (واجهة، جديدة)
  - `US-PLT-EVENT-BACKPRESSURE` — تحمل اندفاع الأحداث دون فقد (منصة، جديدة)
  - `US-PLT-EVENT-CIRCUIT-BREAKER` — إيقاف المستهلك مؤقتًا عند تعطل اعتمادياته (منصة، جديدة)
  - `US-PLT-EVENT-DERIVED-KEYS` — مفتاح حتمي للأوامر الناتجة عن الأحداث (منصة، جديدة)
  - `US-PLT-EVENT-INBOX-DEDUP` — معالجة الحدث المكرر مرة واحدة فقط (منصة، جديدة)
  - `US-PLT-EVENT-OUTBOX` — نشر الحدث مع التغيير في معاملة واحدة (منصة، جديدة)
  - `US-PLT-EVENT-PARKED-KEYS` — إيقاف رسائل المفتاح المتعثر وحده (منصة، جديدة)
  - `US-PLT-EVENT-RETRY-DLQ` — إعادة المحاولة ثم حجز الرسالة الفاشلة (منصة، جديدة)
  - `US-PLT-IDEMPOTENCY-KEY-STORE` — منع تنفيذ الأمر نفسه مرتين (منصة، جديدة)
  - `US-PLT-UI-COMMAND-SUBMIT` — إرسال الأوامر من الواجهة دون تكرار (منصة، جديدة)
  - `US-OPS-EVENT-DLQ-ALERT` — تنبيه لكل رسالة محجوزة حسب الطبقة (تشغيل، جديدة)
  - `US-OPS-EVENT-DLQ-DISCARD` — تجاهل رسالة محجوزة بقرار مدقق (تشغيل، جديدة)
  - `US-OPS-EVENT-DLQ-REPLAY` — إعادة تشغيل الرسائل المحجوزة بتدقيق (تشغيل، جديدة)
  - `US-OPS-EVENT-PARTITIONS` — زيادة أقسام الأحداث دون فقد الترتيب (تشغيل، جديدة)
- **نقل المستأجر بين خلايا التشغيل** `FEAT-PLT-CELL-MIGRATION`
  - `US-BC01-TEN-COMPLETE-CELL-MIGRATION` — إكمال ترحيل المستأجر إلى خلية أخرى (أمر)
  - `US-BC01-TEN-START-CELL-MIGRATION` — بدء ترحيل المستأجر إلى خلية أخرى (أمر)
  - `US-UI-SCR60-MIGRATION-PROGRESS` — متابعة نقل المستأجر ونتيجة المطابقة (واجهة، جديدة)
  - `US-PLT-CELL-EXPORT-IMPORT` — نقل بيانات المستأجر بالتصدير والمطابقة (منصة، جديدة)
  - `US-OPS-CELL-CAPACITY-RECALIBRATE` — إعادة معايرة سعة الخلية عند تجاوز النصف (تشغيل، جديدة)
  - `US-OPS-CELL-MIGRATION-CUTOVER` — تحويل المستخدمين والأجهزة إلى الخلية الجديدة (تشغيل، جديدة)
  - `US-OPS-CELL-PROFILE-ACCEPTANCE` — اختبار القبول نفسه على أنماط الخلايا الثلاثة (تشغيل، جديدة)
- **حصص المستأجر وحدود الاستخدام** `FEAT-PLT-TENANT-QUOTAS`
  - `US-BC01-TEN-UPDATE-QUOTAS` — تحديث حصص المستأجر (أمر)
  - `US-UI-SCR60-QUOTA-USAGE` — عرض الاستهلاك مقابل الحصص والسعة (واجهة، جديدة)
  - `US-PLT-QUOTA-COST-REPORT` — تقرير كلفة شهري لكل مستأجر (منصة، جديدة)
  - `US-PLT-QUOTA-DEFAULTS` — حصص افتراضية من ملف الخلية (منصة، جديدة)
  - `US-PLT-QUOTA-JOB-FAIR-SHARE` — حصص عادلة للمهام بين المستأجرين (منصة، جديدة)
  - `US-PLT-QUOTA-RATE-LIMIT` — حد معدل الطلبات لكل مستأجر (منصة، جديدة)
  - `US-PLT-QUOTA-STORAGE-EVENTS` — فرض حصص التخزين والأحداث (منصة، جديدة)
  - `US-OPS-QUOTA-NOISY-NEIGHBOR` — اختبار عدم تأثر المستأجرين بالمستأجر المزعج (تشغيل، جديدة)
  - `US-OPS-QUOTA-USAGE-ALERT` — تنبيه عند اقتراب المستأجر من حصته (تشغيل، جديدة)

</details>

## 3. ميزات بلا قصص من المواصفة

14 ميزة تغطي متطلبات لا يقابلها أمر أو استعلام أو انتقال في المواصفة، وكل قصصها جديدة:

| الميزة | القدرة الفرعية | القصص الجديدة |
|---|---|---|
| **العمل الميداني دون اتصال** `FEAT-COL-OFFLINE-WORK` | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) | 9 |
| **التكامل مع أنظمة المؤسسة** `FEAT-COL-ENTERPRISE-INT` | CAP-02.04 الاستيعاب والتكامل | 4 |
| **استيراد الخرائط والطقس** `FEAT-COL-GEO-WEATHER` | CAP-02.04 الاستيعاب والتكامل | 8 |
| **صياغة المسودات والملخصات** `FEAT-AI-DRAFTING` | CAP-12.02 الصياغة والتلخيص | 3 |
| **استخراج المعلومات من الوثائق** `FEAT-AI-EXTRACTION` | CAP-12.03 الاستخراج والترجمة | 3 |
| **الترجمة بين العربية والإنجليزية** `FEAT-AI-TRANSLATION` | CAP-12.03 الاستخراج والترجمة | 4 |
| **التسجيل التلقائي للعمليات** `FEAT-GOV-AUDIT-CAPTURE` | CAP-13.02 التدقيق | 6 |
| **إقامة البيانات وسيادتها** `FEAT-GOV-DATA-RESIDENCY` | CAP-13.04 السيادة وإقامة البيانات | 8 |
| **واجهة عربية وإنجليزية** `FEAT-PLT-LOCALIZATION` | CAP-14.01 المراقبة | 11 |
| **مراقبة صحة المنصة** `FEAT-PLT-MONITORING` | CAP-14.01 المراقبة | 11 |
| **التثبيت والترقية دون اتصال** `FEAT-PLT-AIRGAP-UPGRADE` | CAP-14.02 الاعتمادية والتعافي | 10 |
| **متابعة العمليات الطويلة** `FEAT-PLT-BACKGROUND-JOBS` | CAP-14.02 الاعتمادية والتعافي | 6 |
| **النسخ الاحتياطي والاستعادة** `FEAT-PLT-BACKUP-RESTORE` | CAP-14.02 الاعتمادية والتعافي | 8 |
| **موثوقية الأحداث والإسقاطات** `FEAT-PLT-EVENT-DELIVERY` | CAP-14.02 الاعتمادية والتعافي | 14 |

<!-- END GENERATED: build_analysis_design.py -->
