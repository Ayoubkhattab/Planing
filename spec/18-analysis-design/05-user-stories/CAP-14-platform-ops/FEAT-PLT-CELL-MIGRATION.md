---
id: FEAT-PLT-CELL-MIGRATION
type: feature
title: "نقل المستأجر بين خلايا التشغيل"
status: DRAFT
version: "0.1"
capability: CAP-14.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# نقل المستأجر بين خلايا التشغيل

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-PLT-CELL-MIGRATION |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-14 تشغيل المنصة |
| القدرة الفرعية | CAP-14.03 تهيئة المستأجرين والحصص (R1) |
| الأدوار | مشغّل المنصة؛ النظام |
| الشاشات | SCR-60 المستأجر والحصص (واجهة المشغل) |
| حالات الاستخدام | UC-080 |
| القصص | 7: 2 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لمشغل المنصة نقل مستأجر إلى خلية تشغيل أخرى (مشتركة أو مخصصة أو سيادية) دون فقدان بيانات، بنفس نسخة البرنامج في كل البيئات.

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
| QAS-SCAL-001 | load rises from pilot (100 concurrent) to 10× (1,000) and then to design (5,000) | 0 architectural or schema changes needed |
| QAS-SCAL-005 | exceeds its quota by 10× | other tenants stay within QAS-PERF-001 |
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
| `US-BC01-TEN-COMPLETE-CELL-MIGRATION` | إكمال ترحيل المستأجر إلى خلية أخرى | أمر | مسودة |
| `US-BC01-TEN-START-CELL-MIGRATION` | بدء ترحيل المستأجر إلى خلية أخرى | أمر | مسودة |
| `US-UI-SCR60-MIGRATION-PROGRESS` | متابعة نقل المستأجر ونتيجة المطابقة | واجهة | مسودة |
| `US-PLT-CELL-EXPORT-IMPORT` | نقل بيانات المستأجر بالتصدير والمطابقة | منصة | مسودة |
| `US-OPS-CELL-CAPACITY-RECALIBRATE` | إعادة معايرة سعة الخلية عند تجاوز النصف | تشغيل | مسودة |
| `US-OPS-CELL-MIGRATION-CUTOVER` | تحويل المستخدمين والأجهزة إلى الخلية الجديدة | تشغيل | مسودة |
| `US-OPS-CELL-PROFILE-ACCEPTANCE` | اختبار القبول نفسه على أنماط الخلايا الثلاثة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-TEN-COMPLETE-CELL-MIGRATION — إكمال ترحيل المستأجر إلى خلية أخرى

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

<!-- BEGIN GENERATED: refs US-BC01-TEN-COMPLETE-CELL-MIGRATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants/{id}/actions/complete-cell-migration` | — |
| الأمر | `CMD-TEN-COMPLETE-CELL-MIGRATION` | إكمال ترحيل المستأجر إلى خلية أخرى |
| السياسة | `POL-TEN-COMPLETE-CELL-MIGRATION` | workload identity: scheduler / provisioning saga؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN ope… |
| الحدث | `EVT-TEN-MIGRATED` | يصل إلى: Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-018 | The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs. |
| حالة الاستخدام | UC-105 | Manage Tenant Quotas |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-COMPLETE-CELL-MIGRATION -->

</details>

### 5.2 US-BC01-TEN-START-CELL-MIGRATION — بدء ترحيل المستأجر إلى خلية أخرى

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

<!-- BEGIN GENERATED: refs US-BC01-TEN-START-CELL-MIGRATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants/{id}/actions/start-cell-migration` | — |
| الأمر | `CMD-TEN-START-CELL-MIGRATION` | بدء ترحيل المستأجر إلى خلية أخرى |
| السياسة | `POL-TEN-START-CELL-MIGRATION` | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ tenant match; subject ACTIVE… |
| الحدث | `EVT-TEN-MIGRATION-STARTED` | يصل إلى: Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-018 | The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs. |
| حالة الاستخدام | UC-105 | Manage Tenant Quotas |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-START-CELL-MIGRATION -->

</details>

### 5.3 US-UI-SCR60-MIGRATION-PROGRESS — متابعة نقل المستأجر ونتيجة المطابقة

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

<!-- BEGIN GENERATED: refs US-UI-SCR60-MIGRATION-PROGRESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-080 | Provision Tenant |
| الشاشة | SCR-60 | شاشة المستأجر والحصص (واجهة المشغل) |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR60-MIGRATION-PROGRESS -->

</details>

### 5.4 US-PLT-CELL-EXPORT-IMPORT — نقل بيانات المستأجر بالتصدير والمطابقة

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

<!-- BEGIN GENERATED: refs US-PLT-CELL-EXPORT-IMPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P04 | Tenant Isolation |
| المصدر | `23-crosscutting.md §1.2` | — |
<!-- END GENERATED: refs US-PLT-CELL-EXPORT-IMPORT -->

</details>

### 5.5 US-OPS-CELL-CAPACITY-RECALIBRATE — إعادة معايرة سعة الخلية عند تجاوز النصف

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

<!-- BEGIN GENERATED: refs US-OPS-CELL-CAPACITY-RECALIBRATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §2.2` | — |
| الجودة | QAS-SCAL-001 | load rises from pilot (100 concurrent) to 10× (1,000) and then to design (5,000) → 0 architectural or schema… |
<!-- END GENERATED: refs US-OPS-CELL-CAPACITY-RECALIBRATE -->

</details>

### 5.6 US-OPS-CELL-MIGRATION-CUTOVER — تحويل المستخدمين والأجهزة إلى الخلية الجديدة

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

<!-- BEGIN GENERATED: refs US-OPS-CELL-MIGRATION-CUTOVER -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §2.1` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-CELL-MIGRATION-CUTOVER -->

</details>

### 5.7 US-OPS-CELL-PROFILE-ACCEPTANCE — اختبار القبول نفسه على أنماط الخلايا الثلاثة

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

<!-- BEGIN GENERATED: refs US-OPS-CELL-PROFILE-ACCEPTANCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `12-solution/release-configuration-migration.md §1` | — |
| المتطلب | REQ-PLT-002 | The system shall use the same release artifacts for shared, dedicated and sovereign deployments. |
<!-- END GENERATED: refs US-OPS-CELL-PROFILE-ACCEPTANCE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-018 | The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs. | `US-BC01-TEN-COMPLETE-CELL-MIGRATION`، `US-BC01-TEN-START-CELL-MIGRATION` | TST-TENANT-SM |
| REQ-PLT-002 | The system shall use the same release artifacts for shared, dedicated and sovereign deployments. | `US-OPS-CELL-PROFILE-ACCEPTANCE` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
