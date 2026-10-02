---
id: FEAT-ANL-ARGUMENT
type: feature
title: "الفرضيات والافتراضات والأدلة"
status: DRAFT
version: "0.1"
capability: CAP-04.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# الفرضيات والافتراضات والأدلة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ANL-ARGUMENT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-04 التحليل والتقييم |
| القدرة الفرعية | CAP-04.01 حالات التحليل (R1) |
| الأدوار | المحلل |
| الشاشات | SCR-30 الحالة التحليلية والتشغيلات، SCR-22 الادعاء والدليل والمصدر |
| حالات الاستخدام | UC-011، UC-012 |
| القصص | 8: 6 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يبني المحلل حجته بفرضيات وافتراضات صريحة وأدلة مختارة، فيعرف القارئ على ماذا يستند الاستنتاج.

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
لا متطلبات جودة مرتبطة بمتطلبات هذه الميزة مباشرة. تنطبق متطلبات المنصة العامة (`FEAT-PLT-*`).
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
| `US-BC03-ACS-ADD-ASSUMPTION` | إضافة افتراض إلى حالة التحليل | أمر | مسودة |
| `US-BC03-ACS-ADD-HYPOTHESIS` | إضافة فرضية إلى حالة التحليل | أمر | مسودة |
| `US-BC03-ACS-DESELECT-EVIDENCE` | استبعاد دليل من حالة التحليل | أمر | مسودة |
| `US-BC03-ACS-RETIRE-ASSUMPTION` | سحب افتراض من حالة التحليل | أمر | مسودة |
| `US-BC03-ACS-SELECT-EVIDENCE` | اختيار دليل لـحالة التحليل | أمر | مسودة |
| `US-BC03-ACS-UPDATE-HYPOTHESIS` | تحديث فرضية في حالة التحليل | أمر | مسودة |
| `US-UI-SCR22-SELECT-EVIDENCE` | اختيار دليل للحالة من شاشة الدليل | واجهة | مسودة |
| `US-UI-SCR30-HYPOTHESES` | عرض الفرضيات والافتراضات وحالتها في الحالة | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-ACS-ADD-ASSUMPTION — إضافة افتراض إلى حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-ADD-ASSUMPTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/add-assumption` | — |
| الأمر | `CMD-ACS-ADD-ASSUMPTION` | إضافة افتراض إلى حالة التحليل |
| السياسة | `POL-ACS-ADD-ASSUMPTION` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-ASSUMPTION-ADDED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-011، UC-012 | Define Analytical Question؛ Select Evidence |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-ADD-ASSUMPTION -->

</details>

### 5.2 US-BC03-ACS-ADD-HYPOTHESIS — إضافة فرضية إلى حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-ADD-HYPOTHESIS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/add-hypothesis` | — |
| الأمر | `CMD-ACS-ADD-HYPOTHESIS` | إضافة فرضية إلى حالة التحليل |
| السياسة | `POL-ACS-ADD-HYPOTHESIS` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-HYPOTHESIS-ADDED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-011، UC-012 | Define Analytical Question؛ Select Evidence |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-ADD-HYPOTHESIS -->

</details>

### 5.3 US-BC03-ACS-DESELECT-EVIDENCE — استبعاد دليل من حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-DESELECT-EVIDENCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/deselect-evidence` | — |
| الأمر | `CMD-ACS-DESELECT-EVIDENCE` | استبعاد دليل من حالة التحليل |
| السياسة | `POL-ACS-DESELECT-EVIDENCE` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-EVIDENCE-DESELECTED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-011، UC-012 | Define Analytical Question؛ Select Evidence |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-DESELECT-EVIDENCE -->

</details>

### 5.4 US-BC03-ACS-RETIRE-ASSUMPTION — سحب افتراض من حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-RETIRE-ASSUMPTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/retire-assumption` | — |
| الأمر | `CMD-ACS-RETIRE-ASSUMPTION` | سحب افتراض من حالة التحليل |
| السياسة | `POL-ACS-RETIRE-ASSUMPTION` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-ASSUMPTION-RETIRED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-011، UC-012 | Define Analytical Question؛ Select Evidence |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-RETIRE-ASSUMPTION -->

</details>

### 5.5 US-BC03-ACS-SELECT-EVIDENCE — اختيار دليل لـحالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-SELECT-EVIDENCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/select-evidence` | — |
| الأمر | `CMD-ACS-SELECT-EVIDENCE` | اختيار دليل لـحالة التحليل |
| السياسة | `POL-ACS-SELECT-EVIDENCE` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-EVIDENCE-SELECTED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-011، UC-012 | Define Analytical Question؛ Select Evidence |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-SELECT-EVIDENCE -->

</details>

### 5.6 US-BC03-ACS-UPDATE-HYPOTHESIS — تحديث فرضية في حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-UPDATE-HYPOTHESIS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/update-hypothesis` | — |
| الأمر | `CMD-ACS-UPDATE-HYPOTHESIS` | تحديث فرضية في حالة التحليل |
| السياسة | `POL-ACS-UPDATE-HYPOTHESIS` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-HYPOTHESIS-UPDATED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-011، UC-012 | Define Analytical Question؛ Select Evidence |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-UPDATE-HYPOTHESIS -->

</details>

### 5.7 US-UI-SCR22-SELECT-EVIDENCE — اختيار دليل للحالة من شاشة الدليل

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

<!-- BEGIN GENERATED: refs US-UI-SCR22-SELECT-EVIDENCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| الشاشة | SCR-30 | شاشة الحالة التحليلية والتشغيلات |
| حالة الاستخدام | UC-012 | Select Evidence |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-001 | The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumpti… |
| حالات الاستخدام | UC-011، UC-012 | Define Analytical Question؛ Select Evidence |
<!-- END GENERATED: refs US-UI-SCR22-SELECT-EVIDENCE -->

</details>

### 5.8 US-UI-SCR30-HYPOTHESES — عرض الفرضيات والافتراضات وحالتها في الحالة

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

<!-- BEGIN GENERATED: refs US-UI-SCR30-HYPOTHESES -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-30 | شاشة الحالة التحليلية والتشغيلات |
| حالة الاستخدام | UC-011 | Define Analytical Question |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-001 | The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumpti… |
| حالات الاستخدام | UC-011، UC-012 | Define Analytical Question؛ Select Evidence |
<!-- END GENERATED: refs US-UI-SCR30-HYPOTHESES -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-ANL-001 | The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumpti… | `US-BC03-ACS-ADD-ASSUMPTION`، `US-BC03-ACS-ADD-HYPOTHESIS`، `US-BC03-ACS-DESELECT-EVIDENCE`، `US-BC03-ACS-RETIRE-ASSUMPTION`، `US-BC03-ACS-SELECT-EVIDENCE`، `US-BC03-ACS-UPDATE-HYPOTHESIS`، `US-UI-SCR22-SELECT-EVIDENCE`، `US-UI-SCR30-HYPOTHESES` | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS |
| REQ-ANL-007 | The system shall allow comparison of alternative scenarios within an analysis case. | كل قصص الميزة المأخوذة من المواصفة (6) | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
