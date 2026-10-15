---
id: FEAT-PLT-TENANT-QUOTAS
type: feature
title: "حصص المستأجر وحدود الاستخدام"
status: DRAFT
version: "0.1"
capability: CAP-14.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# حصص المستأجر وحدود الاستخدام

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-PLT-TENANT-QUOTAS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-14 تشغيل المنصة |
| القدرة الفرعية | CAP-14.03 تهيئة المستأجرين والحصص (R1) |
| الأدوار | مشغّل المنصة؛ مسؤول الإدارة؛ النظام |
| الشاشات | SCR-60 المستأجر والحصص (واجهة المشغل) |
| حالات الاستخدام | UC-105 |
| القصص | 9: 1 من المواصفة، و8 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لمشغل المنصة تحديد حصص كل مستأجر من الطلبات والتخزين والأحداث والمهام وفرضها، حتى لا يؤثر مستأجر على غيره.

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
| QAS-COST-001 | requests monthly cost per tenant | computed from telemetry with no manual input |
| QAS-PERF-020 | tenant submits 100 runs | no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s |
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
| `US-BC01-TEN-UPDATE-QUOTAS` | تحديث حصص المستأجر | أمر | مسودة |
| `US-UI-SCR60-QUOTA-USAGE` | عرض الاستهلاك مقابل الحصص والسعة | واجهة | مسودة |
| `US-PLT-QUOTA-COST-REPORT` | تقرير كلفة شهري لكل مستأجر | منصة | مسودة |
| `US-PLT-QUOTA-DEFAULTS` | حصص افتراضية من ملف الخلية | منصة | مسودة |
| `US-PLT-QUOTA-JOB-FAIR-SHARE` | حصص عادلة للمهام بين المستأجرين | منصة | مسودة |
| `US-PLT-QUOTA-RATE-LIMIT` | حد معدل الطلبات لكل مستأجر | منصة | مسودة |
| `US-PLT-QUOTA-STORAGE-EVENTS` | فرض حصص التخزين والأحداث | منصة | مسودة |
| `US-OPS-QUOTA-NOISY-NEIGHBOR` | اختبار عدم تأثر المستأجرين بالمستأجر المزعج | تشغيل | مسودة |
| `US-OPS-QUOTA-USAGE-ALERT` | تنبيه عند اقتراب المستأجر من حصته | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-TEN-UPDATE-QUOTAS — تحديث حصص المستأجر

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

<!-- BEGIN GENERATED: refs US-BC01-TEN-UPDATE-QUOTAS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/tenants/{id}/actions/update-quotas` | — |
| الأمر | `CMD-TEN-UPDATE-QUOTAS` | تحديث حصص المستأجر |
| السياسة | `POL-TEN-UPDATE-QUOTAS` | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ tenant match; subject ACTIVE… |
| الحدث | `EVT-TEN-QUOTAS-UPDATED` | يصل إلى: Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| الكيان | `AGG-TENANT` | المستأجر |
| الجدول | `foundation.tenants` | الجدول الرئيسي للمستأجر |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-018 | The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs. |
| حالة الاستخدام | UC-105 | Manage Tenant Quotas |
| الاختبار | TST-TENANT-SM، TST-SLC01-INVARIANTS | دورة حالات المستأجر، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-TEN-UPDATE-QUOTAS -->

</details>

### 5.2 US-UI-SCR60-QUOTA-USAGE — عرض الاستهلاك مقابل الحصص والسعة

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

<!-- BEGIN GENERATED: refs US-UI-SCR60-QUOTA-USAGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-105 | Manage Tenant Quotas |
| الشاشة | SCR-60 | شاشة المستأجر والحصص (واجهة المشغل) |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR60-QUOTA-USAGE -->

</details>

### 5.3 US-PLT-QUOTA-COST-REPORT — تقرير كلفة شهري لكل مستأجر

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

<!-- BEGIN GENERATED: refs US-PLT-QUOTA-COST-REPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-COST-001 | requests monthly cost per tenant → computed from telemetry with no manual input |
| المصدر | `22-deployment-design.md §12` | — |
| المتطلب | REQ-PLT-013 | The system shall compute resource consumption and cost per tenant from telemetry. |
<!-- END GENERATED: refs US-PLT-QUOTA-COST-REPORT -->

</details>

### 5.4 US-PLT-QUOTA-DEFAULTS — حصص افتراضية من ملف الخلية

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

<!-- BEGIN GENERATED: refs US-PLT-QUOTA-DEFAULTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §1.3` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-QUOTA-DEFAULTS -->

</details>

### 5.5 US-PLT-QUOTA-JOB-FAIR-SHARE — حصص عادلة للمهام بين المستأجرين

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

<!-- BEGIN GENERATED: refs US-PLT-QUOTA-JOB-FAIR-SHARE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-020 | tenant submits 100 runs → no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s |
| القرار التقني | TD-12 | Kubernetes Jobs with Kueue (fair sharing, per-tenant quotas); images from internal Harbor registry, signed (c… |
| المتطلب | REQ-FND-018 | The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs. |
| حالة الاستخدام | UC-105 | Manage Tenant Quotas |
<!-- END GENERATED: refs US-PLT-QUOTA-JOB-FAIR-SHARE -->

</details>

### 5.6 US-PLT-QUOTA-RATE-LIMIT — حد معدل الطلبات لكل مستأجر

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

<!-- BEGIN GENERATED: refs US-PLT-QUOTA-RATE-LIMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §1.3` | — |
| المصدر | `23-crosscutting.md §10` | — |
| المتطلب | REQ-FND-018 | The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs. |
| حالة الاستخدام | UC-105 | Manage Tenant Quotas |
<!-- END GENERATED: refs US-PLT-QUOTA-RATE-LIMIT -->

</details>

### 5.7 US-PLT-QUOTA-STORAGE-EVENTS — فرض حصص التخزين والأحداث

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

<!-- BEGIN GENERATED: refs US-PLT-QUOTA-STORAGE-EVENTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-018 | The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs. |
| حالة الاستخدام | UC-105 | Manage Tenant Quotas |
<!-- END GENERATED: refs US-PLT-QUOTA-STORAGE-EVENTS -->

</details>

### 5.8 US-OPS-QUOTA-NOISY-NEIGHBOR — اختبار عدم تأثر المستأجرين بالمستأجر المزعج

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

<!-- BEGIN GENERATED: refs US-OPS-QUOTA-NOISY-NEIGHBOR -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SCAL-005 | exceeds its quota by 10× → other tenants stay within QAS-PERF-001 |
| المصدر | `22-deployment-design.md §2.2` | — |
<!-- END GENERATED: refs US-OPS-QUOTA-NOISY-NEIGHBOR -->

</details>

### 5.9 US-OPS-QUOTA-USAGE-ALERT — تنبيه عند اقتراب المستأجر من حصته

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

<!-- BEGIN GENERATED: refs US-OPS-QUOTA-USAGE-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §7` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-018 | The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs. |
| حالة الاستخدام | UC-105 | Manage Tenant Quotas |
<!-- END GENERATED: refs US-OPS-QUOTA-USAGE-ALERT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-018 | The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs. | `US-BC01-TEN-UPDATE-QUOTAS`، `US-OPS-QUOTA-USAGE-ALERT`، `US-PLT-QUOTA-JOB-FAIR-SHARE`، `US-PLT-QUOTA-RATE-LIMIT`، `US-PLT-QUOTA-STORAGE-EVENTS` | TST-TENANT-SM |
| REQ-PLT-013 | The system shall compute resource consumption and cost per tenant from telemetry. | `US-PLT-QUOTA-COST-REPORT` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
