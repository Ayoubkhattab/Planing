---
id: FEAT-ORG-TENANT-LIFECYCLE
type: feature
title: "دورة حياة المستأجر"
status: DRAFT
version: "0.1"
capability: CAP-01.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# دورة حياة المستأجر

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-TENANT-LIFECYCLE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.01 إدارة المستأجرين والمؤسسات (R1) |
| الأدوار | مشغّل المنصة؛ مسؤول الإدارة؛ النظام |
| الشاشات | SCR-60 المستأجر والحصص (واجهة المشغل) |
| حالات الاستخدام | UC-080 |
| القصص | 19: 9 من المواصفة، و10 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لمشغل المنصة إنشاء مستأجر جديد معزول وجاهز للاستخدام ومتابعة حالته وتعليقه أو إعادته أو إخراجه من الخدمة بأمان.

### 1.2 النطاق

**[للكتابة]**

### 1.3 خريطة الميزة

**[للكتابة]**

## 2. القواعد المشتركة

تنطبق على كل قصص الميزة، فلا تتكرر داخل القصص. وكل قصة تذكر ما يخصها فقط.

### 2.1 السياق المشترك

كل قصة تبدأ من ثلاثة شروط: مستأجر نشط، وحزمة السياسات الأساسية مفعّلة، ومستخدم مسجّل الدخول ومخوَّل. وتشير إليها القصص بخطوة واحدة: «بفرض السياق المشترك للميزة».

### 2.2 الصلاحية وعدم الإفصاح

- من لا يحق له رؤية العنصر يتلقى ردًا بشكل «غير متاح» تمامًا، فلا يعرف أنه موجود.
- من يرى العنصر ولا يحق له الإجراء يتلقى «لا تملك صلاحية هذا الإجراء».

### 2.3 أوامر تغيير الحالة

- **منع التكرار:** يُرسل كل أمر بمفتاح فريد، فإعادة الطلب نفسه لا تُنفَّذ مرتين.
- **حماية التعديل المتزامن:** يُرسل كل أمر بإصدار البيانات الذي يراه المستخدم. فإن عدّلها غيره في الأثناء، يُرفض الأمر.
- **السجل:** إن نجح الأمر، يُكتب حدثه وسجل التدقيق في المعاملة نفسها.

### 2.4 الرفض المشترك

```gherkin
# language: ar
خاصية: الرفض المشترك لأوامر الميزة

  سيناريو مخطط: رفض مشترك لكل أمر في الميزة
    بفرض السياق المشترك للميزة
    و <الحالة>
    عندما يُرسل المستخدم أي أمر من أوامر الميزة
    اذاً يُرفض برمز <الرمز> ويرى "<الرسالة>"
    و لا يتغير شيء

    امثلة:
      | الحالة                                  | الرمز                  | الرسالة                                                 |
      | العنصر خارج صلاحياته                    | NOT_FOUND              | غير متاح                                                |
      | العنصر مرئي له ولا يحق له الإجراء       | AUTHZ_DENIED           | لا تملك صلاحية هذا الإجراء                              |
      | غيره عدّل العنصر بعد أن فتحه            | VERSION_CONFLICT       | تغيّرت البيانات منذ فتحتها. راجع التغييرات ثم أعد المحاولة |
      | أعاد مفتاح منع التكرار بمحتوى مختلف     | IDEMPOTENCY_KEY_REUSED | طلب مكرر بمحتوى مختلف                                   |
      | البيانات ناقصة أو غير صحيحة             | VALIDATION_FAILED      | بعض البيانات ناقصة أو غير صحيحة. راجع الحقول المعلَّمة      |

  سيناريو: إعادة الطلب نفسه لا تُنفَّذ مرتين
    بفرض السياق المشترك للميزة
    و أمر نجح بمفتاح منع تكرار
    عندما يُعاد الطلب نفسه بالمفتاح نفسه
    اذاً تُعاد النتيجة الأولى ولا يُكتب حدث ثانٍ
```

## 3. الجودة وتعريف الاكتمال

### 3.1 متطلبات الجودة

<!-- BEGIN GENERATED: quality -->
| المرجع | الموقف | المطلوب |
|---|---|---|
| QAS-SCAL-003 | provisions a new tenant | automated; ≤ 1 hour; no code or schema change |
| QAS-SEC-001 | attempts to access tenant B data by any path | 0 leaks in tenant-isolation suite |
<!-- END GENERATED: quality -->

### 3.2 تعريف الاكتمال

القصة مكتملة حين تتحقق الشروط الخمسة:

1. سيناريوهاتها والقواعد المشتركة تمر في الاختبار الآلي.
2. فحوص البنية المعمارية تمر.
3. نصوص الواجهة والرسائل موجودة بالعربية والإنجليزية.
4. مراجعة الكود مكتملة.
5. ما تضيفه القصة نفسها في قسم «القواعد» تحقق.

## 4. فهرس القصص

<!-- BEGIN GENERATED: story-index -->
| المعرّف | القصة | النوع | الحالة |
|---|---|---|---|
| `US-BC01-TEN-COMPLETE-DECOMMISSION` | إكمال إخراج المستأجر من الخدمة | أمر | مسودة |
| `US-BC01-TEN-COMPLETE-PROVISIONING` | إكمال تهيئة المستأجر | أمر | مسودة |
| `US-BC01-TEN-FAIL-PROVISIONING` | تسجيل فشل تهيئة المستأجر | أمر | مسودة |
| `US-BC01-TEN-PROVISION` | تهيئة المستأجر | أمر | مسودة |
| `US-BC01-TEN-REACTIVATE` | إعادة تفعيل المستأجر | أمر | مسودة |
| `US-BC01-TEN-RETRY-PROVISIONING` | إعادة محاولة تهيئة المستأجر | أمر | مسودة |
| `US-BC01-TEN-START-DECOMMISSION` | بدء إخراج المستأجر من الخدمة | أمر | مسودة |
| `US-BC01-TEN-SUSPEND` | تعليق المستأجر | أمر | مسودة |
| `US-BC01-Q-TEN-GET` | جلب: Tenant state, cell, quotas | جلب | مسودة |
| `US-DOM-TEN-LIST` | عرض قائمة المستأجرين لمشغل المنصة | جلب | مسودة |
| `US-UI-SCR60-PROVISIONING-PROGRESS` | متابعة خطوات تهيئة المستأجر وسبب فشلها | واجهة | مسودة |
| `US-UI-SCR60-TENANT-ACTIONS` | أفعال المستأجر المتاحة حسب حالته | واجهة | مسودة |
| `US-PLT-TENANT-CELL-BINDING` | رفض طلبات المستأجر من غير خليته | منصة | مسودة |
| `US-PLT-TENANT-DECOMMISSION-PURGE` | محو كل بيانات المستأجر عند إخراجه | منصة | مسودة |
| `US-PLT-TENANT-DEDICATED-CELL` | تشغيل المستأجر المخصص في خلية مستقلة | منصة | مسودة |
| `US-PLT-TENANT-ISOLATION-LAYERS` | عزل بيانات كل مستأجر في كل طبقة | منصة | مسودة |
| `US-PLT-TENANT-PROVISION-ATOMIC` | تهيئة مستأجر آلية ذرية خلال ساعة | منصة | مسودة |
| `US-OPS-TENANT-ISOLATION-SUITE` | اختبار عزل المستأجرين في كل المسارات | تشغيل | مسودة |
| `US-OPS-TENANT-PROVISION-ALERT` | تنبيه عند تأخر تهيئة المستأجر | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-TEN-COMPLETE-DECOMMISSION — إكمال إخراج المستأجر من الخدمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC01-TEN-COMPLETE-DECOMMISSION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants/{id}/actions/complete-decommission` | — |
| الأمر | `CMD-TEN-COMPLETE-DECOMMISSION` | إكمال إخراج المستأجر من الخدمة |
| السياسة | `POL-TEN-COMPLETE-DECOMMISSION` | workload identity: scheduler / provisioning saga؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN ope… |
| الحدث | `EVT-TEN-DECOMMISSIONED` | يصل إلى: Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-001، REQ-FND-003، REQ-FND-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-080 | Provision Tenant |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-COMPLETE-DECOMMISSION -->

</details>

### 5.2 US-BC01-TEN-COMPLETE-PROVISIONING — إكمال تهيئة المستأجر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC01-TEN-COMPLETE-PROVISIONING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants/{id}/actions/complete-provisioning` | — |
| الأمر | `CMD-TEN-COMPLETE-PROVISIONING` | إكمال تهيئة المستأجر |
| السياسة | `POL-TEN-COMPLETE-PROVISIONING` | workload identity: scheduler / provisioning saga؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN ope… |
| الحدث | `EVT-TEN-ACTIVATED` | يصل إلى: Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-001، REQ-FND-003، REQ-FND-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-080 | Provision Tenant |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-COMPLETE-PROVISIONING -->

</details>

### 5.3 US-BC01-TEN-FAIL-PROVISIONING — تسجيل فشل تهيئة المستأجر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC01-TEN-FAIL-PROVISIONING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants/{id}/actions/fail-provisioning` | — |
| الأمر | `CMD-TEN-FAIL-PROVISIONING` | تسجيل فشل تهيئة المستأجر |
| السياسة | `POL-TEN-FAIL-PROVISIONING` | workload identity: scheduler / provisioning saga؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN ope… |
| الحدث | `EVT-TEN-PROVISIONING-FAILED` | يصل إلى: Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-001، REQ-FND-003، REQ-FND-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-080 | Provision Tenant |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-FAIL-PROVISIONING -->

</details>

### 5.4 US-BC01-TEN-PROVISION — تهيئة المستأجر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC01-TEN-PROVISION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants` | — |
| الأمر | `CMD-TEN-PROVISION` | تهيئة المستأجر |
| السياسة | `POL-TEN-PROVISION` | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ tenant match; subject ACTIVE… |
| الحدث | `EVT-TEN-PROVISIONING-STARTED` | يصل إلى: Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-001، REQ-FND-003، REQ-FND-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-080 | Provision Tenant |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-PROVISION -->

</details>

### 5.5 US-BC01-TEN-REACTIVATE — إعادة تفعيل المستأجر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC01-TEN-REACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants/{id}/actions/reactivate` | — |
| الأمر | `CMD-TEN-REACTIVATE` | إعادة تفعيل المستأجر |
| السياسة | `POL-TEN-REACTIVATE` | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ tenant match; subject ACTIVE… |
| الحدث | `EVT-TEN-REACTIVATED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-001، REQ-FND-003، REQ-FND-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-080 | Provision Tenant |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-REACTIVATE -->

</details>

### 5.6 US-BC01-TEN-RETRY-PROVISIONING — إعادة محاولة تهيئة المستأجر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC01-TEN-RETRY-PROVISIONING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants/{id}/actions/retry-provisioning` | — |
| الأمر | `CMD-TEN-RETRY-PROVISIONING` | إعادة محاولة تهيئة المستأجر |
| السياسة | `POL-TEN-RETRY-PROVISIONING` | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ tenant match; subject ACTIVE… |
| الحدث | `EVT-TEN-PROVISIONING-STARTED` | يصل إلى: Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-001، REQ-FND-003، REQ-FND-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-080 | Provision Tenant |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-RETRY-PROVISIONING -->

</details>

### 5.7 US-BC01-TEN-START-DECOMMISSION — بدء إخراج المستأجر من الخدمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC01-TEN-START-DECOMMISSION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants/{id}/actions/start-decommission` | — |
| الأمر | `CMD-TEN-START-DECOMMISSION` | بدء إخراج المستأجر من الخدمة |
| السياسة | `POL-TEN-START-DECOMMISSION` | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ tenant match; subject ACTIVE… |
| الحدث | `EVT-TEN-DECOMMISSION-STARTED` | يصل إلى: Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-001، REQ-FND-003، REQ-FND-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-080 | Provision Tenant |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-START-DECOMMISSION -->

</details>

### 5.8 US-BC01-TEN-SUSPEND — تعليق المستأجر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC01-TEN-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants/{id}/actions/suspend` | — |
| الأمر | `CMD-TEN-SUSPEND` | تعليق المستأجر |
| السياسة | `POL-TEN-SUSPEND` | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ tenant match; subject ACTIVE… |
| الحدث | `EVT-TEN-SUSPENDED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-001، REQ-FND-003، REQ-FND-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-080 | Provision Tenant |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-SUSPEND -->

</details>

### 5.9 US-BC01-Q-TEN-GET — جلب: Tenant state, cell, quotas

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC01-Q-TEN-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/foundation/tenants/{tenant_id}` | — |
| الاستعلام | `QRY-TEN-GET` | Tenant state, cell, quotas |
| السياسة | `POL-TEN-GET` | org scope of subject roles ∩ classification rule |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-001 | The system shall isolate each tenant's data, policies, configuration, projections, files, events and audit re… |
| حالة الاستخدام | UC-080 | Provision Tenant |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-Q-TEN-GET -->

</details>

### 5.10 US-DOM-TEN-LIST — عرض قائمة المستأجرين لمشغل المنصة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-TEN-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-080 | Provision Tenant |
| المصدر | `21-ui-design.md §4.6` | — |
| الشاشة | SCR-60 | شاشة المستأجر والحصص (واجهة المشغل) |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-DOM-TEN-LIST -->

</details>

### 5.11 US-UI-SCR60-PROVISIONING-PROGRESS — متابعة خطوات تهيئة المستأجر وسبب فشلها

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR60-PROVISIONING-PROGRESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-080 | Provision Tenant |
| الشاشة | SCR-60 | شاشة المستأجر والحصص (واجهة المشغل) |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-003 | When a tenant is provisioned, the system shall create its isolation boundary, classification scheme, default… |
| حالة الاستخدام | UC-080 | Provision Tenant |
<!-- END GENERATED: refs US-UI-SCR60-PROVISIONING-PROGRESS -->

</details>

### 5.12 US-UI-SCR60-TENANT-ACTIONS — أفعال المستأجر المتاحة حسب حالته

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR60-TENANT-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-080 | Provision Tenant |
| الشاشة | SCR-60 | شاشة المستأجر والحصص (واجهة المشغل) |
| المصدر | `21-ui-design.md §6.3` | — |
<!-- END GENERATED: refs US-UI-SCR60-TENANT-ACTIONS -->

</details>

### 5.13 US-PLT-TENANT-CELL-BINDING — رفض طلبات المستأجر من غير خليته

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-TENANT-CELL-BINDING -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §2.1` | — |
| القرار المعماري | ADR-P04 | Tenant Isolation |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-TENANT-CELL-BINDING -->

</details>

### 5.14 US-PLT-TENANT-DECOMMISSION-PURGE — محو كل بيانات المستأجر عند إخراجه

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-TENANT-DECOMMISSION-PURGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P08 | Erasure vs Immutability |
| المصدر | `17-security-design.md §6` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-001 | The system shall isolate each tenant's data, policies, configuration, projections, files, events and audit re… |
| حالة الاستخدام | UC-080 | Provision Tenant |
<!-- END GENERATED: refs US-PLT-TENANT-DECOMMISSION-PURGE -->

</details>

### 5.15 US-PLT-TENANT-DEDICATED-CELL — تشغيل المستأجر المخصص في خلية مستقلة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-TENANT-DEDICATED-CELL -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P04 | Tenant Isolation |
| المصدر | `22-deployment-design.md §2.1` | — |
| المتطلب | REQ-FND-004 | Where a tenant is designated dedicated or sovereign, the system shall run that tenant in its own cell with no… |
| حالة الاستخدام | UC-080 | Provision Tenant |
<!-- END GENERATED: refs US-PLT-TENANT-DEDICATED-CELL -->

</details>

### 5.16 US-PLT-TENANT-ISOLATION-LAYERS — عزل بيانات كل مستأجر في كل طبقة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-TENANT-ISOLATION-LAYERS -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P04 | Tenant Isolation |
| فحص البنية | FIT-02 | tenant_id present in every table, partition key, index doc, event and object path |
| المصدر | `23-crosscutting.md §1.1` | — |
| المتطلب | REQ-FND-001 | The system shall isolate each tenant's data, policies, configuration, projections, files, events and audit re… |
| حالة الاستخدام | UC-080 | Provision Tenant |
<!-- END GENERATED: refs US-PLT-TENANT-ISOLATION-LAYERS -->

</details>

### 5.17 US-PLT-TENANT-PROVISION-ATOMIC — تهيئة مستأجر آلية ذرية خلال ساعة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-TENANT-PROVISION-ATOMIC -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SCAL-003 | provisions a new tenant → automated; ≤ 1 hour; no code or schema change |
| المتطلب | REQ-FND-003 | When a tenant is provisioned, the system shall create its isolation boundary, classification scheme, default… |
| حالة الاستخدام | UC-080 | Provision Tenant |
<!-- END GENERATED: refs US-PLT-TENANT-PROVISION-ATOMIC -->

</details>

### 5.18 US-OPS-TENANT-ISOLATION-SUITE — اختبار عزل المستأجرين في كل المسارات

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-TENANT-ISOLATION-SUITE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-001 | attempts to access tenant B data by any path → 0 leaks in tenant-isolation suite |
| المصدر | `17-security-design.md §9` | — |
| المتطلب | REQ-FND-001 | The system shall isolate each tenant's data, policies, configuration, projections, files, events and audit re… |
| حالة الاستخدام | UC-080 | Provision Tenant |
<!-- END GENERATED: refs US-OPS-TENANT-ISOLATION-SUITE -->

</details>

### 5.19 US-OPS-TENANT-PROVISION-ALERT — تنبيه عند تأخر تهيئة المستأجر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-TENANT-PROVISION-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SCAL-003 | provisions a new tenant → automated; ≤ 1 hour; no code or schema change |
| المصدر | `09-reliability/observability-slc01.md §signals` | — |
<!-- END GENERATED: refs US-OPS-TENANT-PROVISION-ALERT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-001 | The system shall isolate each tenant's data, policies, configuration, projections, files, events and audit re… | `US-BC01-Q-TEN-GET`، `US-BC01-TEN-COMPLETE-DECOMMISSION`، `US-BC01-TEN-COMPLETE-PROVISIONING`، `US-BC01-TEN-FAIL-PROVISIONING`، `US-BC01-TEN-PROVISION`، `US-BC01-TEN-REACTIVATE`، `US-BC01-TEN-RETRY-PROVISIONING`، `US-BC01-TEN-START-DECOMMISSION`، `US-BC01-TEN-SUSPEND`، `US-OPS-TENANT-ISOLATION-SUITE`، `US-PLT-TENANT-DECOMMISSION-PURGE`، `US-PLT-TENANT-ISOLATION-LAYERS` | TST-SLC01-INVARIANTS، TST-TENANT-SM |
| REQ-FND-003 | When a tenant is provisioned, the system shall create its isolation boundary, classification scheme, default… | `US-BC01-TEN-COMPLETE-DECOMMISSION`، `US-BC01-TEN-COMPLETE-PROVISIONING`، `US-BC01-TEN-FAIL-PROVISIONING`، `US-BC01-TEN-PROVISION`، `US-BC01-TEN-REACTIVATE`، `US-BC01-TEN-RETRY-PROVISIONING`، `US-BC01-TEN-START-DECOMMISSION`، `US-BC01-TEN-SUSPEND`، `US-PLT-TENANT-PROVISION-ATOMIC`، `US-UI-SCR60-PROVISIONING-PROGRESS` | TST-SLC01-INVARIANTS، TST-TENANT-SM |
| REQ-FND-004 | Where a tenant is designated dedicated or sovereign, the system shall run that tenant in its own cell with no… | `US-BC01-TEN-COMPLETE-DECOMMISSION`، `US-BC01-TEN-COMPLETE-PROVISIONING`، `US-BC01-TEN-FAIL-PROVISIONING`، `US-BC01-TEN-PROVISION`، `US-BC01-TEN-REACTIVATE`، `US-BC01-TEN-RETRY-PROVISIONING`، `US-BC01-TEN-START-DECOMMISSION`، `US-BC01-TEN-SUSPEND`، `US-PLT-TENANT-DEDICATED-CELL` | TST-TENANT-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
