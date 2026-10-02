---
id: FEAT-ANL-METHODS
type: feature
title: "إدارة طرق التحليل"
status: DRAFT
version: "0.1"
capability: CAP-04.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة طرق التحليل

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ANL-METHODS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-04 التحليل والتقييم |
| القدرة الفرعية | CAP-04.02 التنفيذ وإعادة الإنتاج (R1) |
| الأدوار | قائد المحللين؛ مسؤول الإدارة؛ المحلل |
| الشاشات | SCR-30 الحالة التحليلية والتشغيلات |
| حالات الاستخدام | UC-013 |
| القصص | 7: 5 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعتمد قائد التحليل الطرق المسموح بها وإصداراتها، فلا يُستخدم إلا ما رُوجع واعتُمد.

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
| QAS-TRC-002 | re-executes a recorded deterministic analysis run | 100 % |
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
| `US-BC03-AMT-ACTIVATE` | تفعيل طريقة التحليل | أمر | مسودة |
| `US-BC03-AMT-DEPRECATE` | إهمال طريقة التحليل (إيقاف الاستخدام الجديد) | أمر | مسودة |
| `US-BC03-AMT-REGISTER` | تسجيل طريقة التحليل | أمر | مسودة |
| `US-BC03-AMT-RETIRE` | إحالة طريقة التحليل إلى التقاعد | أمر | مسودة |
| `US-BC03-Q-AMT-LIST` | جلب: Methods and versions | جلب | مسودة |
| `US-UI-SCR30-METHODS` | كتالوج طرق التحليل وإصداراتها وحالتها | واجهة | مسودة |
| `US-OPS-ANL-METHOD-IMAGES` | صور طرق التحليل موقعة ومثبتة البصمة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-AMT-ACTIVATE — تفعيل طريقة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-AMT-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-methods/{id}/actions/activate` | — |
| الأمر | `CMD-AMT-ACTIVATE` | تفعيل طريقة التحليل |
| السياسة | `POL-AMT-ACTIVATE` | Analysis lead (register) · second lead or Administrator (activate)؛ tenant match; case visible; label rules |
| الحدث | `EVT-AMT-ACTIVATED` | يصل إلى: Job scheduler (image allow-list) |
| الكيان | `AGG-ANALYSIS-METHOD` | طريقة التحليل |
| الجدول | `intelligence.analysis_methods` | الجدول الرئيسي لطريقة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-002، REQ-ANL-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-METHOD-SM، TST-SLC07-INVARIANTS | دورة حالات طريقة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-AMT-ACTIVATE -->

</details>

### 5.2 US-BC03-AMT-DEPRECATE — إهمال طريقة التحليل (إيقاف الاستخدام الجديد)

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

<!-- BEGIN GENERATED: refs US-BC03-AMT-DEPRECATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-methods/{id}/actions/deprecate` | — |
| الأمر | `CMD-AMT-DEPRECATE` | إهمال طريقة التحليل (إيقاف الاستخدام الجديد) |
| السياسة | `POL-AMT-DEPRECATE` | Analysis lead (deprecate)؛ tenant match; case visible; label rules |
| الحدث | `EVT-AMT-DEPRECATED` | يصل إلى: Job scheduler (image allow-list) |
| الكيان | `AGG-ANALYSIS-METHOD` | طريقة التحليل |
| الجدول | `intelligence.analysis_methods` | الجدول الرئيسي لطريقة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-002، REQ-ANL-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-METHOD-SM، TST-SLC07-INVARIANTS | دورة حالات طريقة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-AMT-DEPRECATE -->

</details>

### 5.3 US-BC03-AMT-REGISTER — تسجيل طريقة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-AMT-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-methods` | — |
| الأمر | `CMD-AMT-REGISTER` | تسجيل طريقة التحليل |
| السياسة | `POL-AMT-REGISTER` | Analysis lead (register) · second lead or Administrator (activate)؛ tenant match; case visible; label rules |
| الحدث | `EVT-AMT-REGISTERED` | يصل إلى: Job scheduler (image allow-list) |
| الكيان | `AGG-ANALYSIS-METHOD` | طريقة التحليل |
| الجدول | `intelligence.analysis_methods` | الجدول الرئيسي لطريقة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-002، REQ-ANL-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-METHOD-SM، TST-SLC07-INVARIANTS | دورة حالات طريقة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-AMT-REGISTER -->

</details>

### 5.4 US-BC03-AMT-RETIRE — إحالة طريقة التحليل إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC03-AMT-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-methods/{id}/actions/retire` | — |
| الأمر | `CMD-AMT-RETIRE` | إحالة طريقة التحليل إلى التقاعد |
| السياسة | `POL-AMT-RETIRE` | Analysis lead (retire)؛ tenant match; case visible; label rules |
| الحدث | `EVT-AMT-RETIRED` | يصل إلى: Job scheduler (image allow-list) |
| الكيان | `AGG-ANALYSIS-METHOD` | طريقة التحليل |
| الجدول | `intelligence.analysis_methods` | الجدول الرئيسي لطريقة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-002، REQ-ANL-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-METHOD-SM، TST-SLC07-INVARIANTS | دورة حالات طريقة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-AMT-RETIRE -->

</details>

### 5.5 US-BC03-Q-AMT-LIST — جلب: Methods and versions

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

<!-- BEGIN GENERATED: refs US-BC03-Q-AMT-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/analysis-methods` | — |
| الاستعلام | `QRY-AMT-LIST` | Methods and versions |
| السياسة | `POL-AMT-LIST` | any analyst |
| الكيان | `AGG-ANALYSIS-METHOD` | طريقة التحليل |
| الجدول | `intelligence.analysis_methods` | الجدول الرئيسي لطريقة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-ANL-002 | When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and ver… |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-METHOD-SM، TST-SLC07-INVARIANTS | دورة حالات طريقة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-Q-AMT-LIST -->

</details>

### 5.6 US-UI-SCR30-METHODS — كتالوج طرق التحليل وإصداراتها وحالتها

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

<!-- BEGIN GENERATED: refs US-UI-SCR30-METHODS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-30 | شاشة الحالة التحليلية والتشغيلات |
| المصدر | `QRY-AMT-LIST` | — |
| المصدر | `17-security-design.md §12.4` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR30-METHODS -->

</details>

### 5.7 US-OPS-ANL-METHOD-IMAGES — صور طرق التحليل موقعة ومثبتة البصمة

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

<!-- BEGIN GENERATED: refs US-OPS-ANL-METHOD-IMAGES -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `THR-S07-02` | — |
| القرار التقني | TD-12 | Kubernetes Jobs with Kueue (fair sharing, per-tenant quotas); images from internal Harbor registry, signed (c… |
| القرار التقني | TD-17 | Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps… |
| المصدر | `analysis-reproducibility-spec.md §2` | — |
<!-- END GENERATED: refs US-OPS-ANL-METHOD-IMAGES -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-ANL-002 | When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and ver… | كل قصص الميزة المأخوذة من المواصفة (5) | TST-ANALYSIS-METHOD-SM، TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS |
| REQ-ANL-003 | When a recorded analysis run is re-executed with the same recorded inputs, the system shall produce the same… | كل قصص الأوامر والنظام في الميزة (4) | TST-ANALYSIS-METHOD-SM، TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
