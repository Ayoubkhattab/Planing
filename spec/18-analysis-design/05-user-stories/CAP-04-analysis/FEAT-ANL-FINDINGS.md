---
id: FEAT-ANL-FINDINGS
type: feature
title: "النتائج التحليلية"
status: DRAFT
version: "0.1"
capability: CAP-04.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# النتائج التحليلية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ANL-FINDINGS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-04 التحليل والتقييم |
| القدرة الفرعية | CAP-04.03 إنتاج التقييم (R1) |
| الأدوار | المحلل؛ الشخص الثاني |
| الشاشات | SCR-30 الحالة التحليلية والتشغيلات |
| حالات الاستخدام | UC-014، UC-015 |
| القصص | 7: 5 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يسجّل المحلل كل نتيجة بمصادرها ودرجة عدم اليقين فيها، ويراجعها زميل قبل أن يُبنى عليها تقييم.

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
| `US-BC03-FND-ACCEPT` | قبول النتيجة التحليلية | أمر | مسودة |
| `US-BC03-FND-EDIT` | تعديل النتيجة التحليلية | أمر | مسودة |
| `US-BC03-FND-RECORD` | تسجيل النتيجة التحليلية | أمر | مسودة |
| `US-BC03-FND-WITHDRAW` | سحب النتيجة التحليلية | أمر | مسودة |
| `US-BC03-Q-FND-LIST` | جلب: Findings with sources | جلب | مسودة |
| `US-DOM-ANL-FND-WITHDRAW-FLAG` | تعليم التقييمات المستشهدة بنتيجة مسحوبة للمراجعة | نظام | مسودة |
| `US-UI-SCR30-FINDINGS` | قائمة النتائج بمصادرها وعدم اليقين وحالة القبول | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-FND-ACCEPT — قبول النتيجة التحليلية

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

<!-- BEGIN GENERATED: refs US-BC03-FND-ACCEPT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/findings/{id}/actions/accept` | — |
| الأمر | `CMD-FND-ACCEPT` | قبول النتيجة التحليلية |
| السياسة | `POL-FND-ACCEPT` | Analyst (record, edit, withdraw) · peer Analyst (accept)؛ tenant match; case visible; label rules |
| الحدث | `EVT-FND-ACCEPTED` | يصل إلى: Assessment review flags |
| الكيان | `AGG-FINDING` | النتيجة التحليلية |
| الجدول | `intelligence.findings` | الجدول الرئيسي للنتيجة التحليلية |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, met… |
| حالات الاستخدام | UC-014، UC-015 | Assess Uncertainty؛ Produce Assessment |
| الاختبار | TST-FINDING-SM، TST-SLC07-INVARIANTS | دورة حالات النتيجة التحليلية، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-FND-ACCEPT -->

</details>

### 5.2 US-BC03-FND-EDIT — تعديل النتيجة التحليلية

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

<!-- BEGIN GENERATED: refs US-BC03-FND-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/findings/{id}/actions/edit` | — |
| الأمر | `CMD-FND-EDIT` | تعديل النتيجة التحليلية |
| السياسة | `POL-FND-EDIT` | Analyst (record, edit, withdraw) · peer Analyst (accept)؛ tenant match; case visible; label rules |
| الحدث | `EVT-FND-EDITED` | يصل إلى: Assessment review flags |
| الكيان | `AGG-FINDING` | النتيجة التحليلية |
| الجدول | `intelligence.findings` | الجدول الرئيسي للنتيجة التحليلية |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, met… |
| حالات الاستخدام | UC-014، UC-015 | Assess Uncertainty؛ Produce Assessment |
| الاختبار | TST-FINDING-SM، TST-SLC07-INVARIANTS | دورة حالات النتيجة التحليلية، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-FND-EDIT -->

</details>

### 5.3 US-BC03-FND-RECORD — تسجيل النتيجة التحليلية

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

<!-- BEGIN GENERATED: refs US-BC03-FND-RECORD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/findings` | — |
| الأمر | `CMD-FND-RECORD` | تسجيل النتيجة التحليلية |
| السياسة | `POL-FND-RECORD` | Analyst (record, edit, withdraw) · peer Analyst (accept)؛ tenant match; case visible; label rules |
| الحدث | `EVT-FND-RECORDED` | يصل إلى: Assessment review flags |
| الكيان | `AGG-FINDING` | النتيجة التحليلية |
| الجدول | `intelligence.findings` | الجدول الرئيسي للنتيجة التحليلية |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, met… |
| حالات الاستخدام | UC-014، UC-015 | Assess Uncertainty؛ Produce Assessment |
| الاختبار | TST-FINDING-SM، TST-SLC07-INVARIANTS | دورة حالات النتيجة التحليلية، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-FND-RECORD -->

</details>

### 5.4 US-BC03-FND-WITHDRAW — سحب النتيجة التحليلية

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

<!-- BEGIN GENERATED: refs US-BC03-FND-WITHDRAW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/findings/{id}/actions/withdraw` | — |
| الأمر | `CMD-FND-WITHDRAW` | سحب النتيجة التحليلية |
| السياسة | `POL-FND-WITHDRAW` | Analyst (record, edit, withdraw) · peer Analyst (accept)؛ tenant match; case visible; label rules |
| الحدث | `EVT-FND-WITHDRAWN` | يصل إلى: Assessment review flags |
| الكيان | `AGG-FINDING` | النتيجة التحليلية |
| الجدول | `intelligence.findings` | الجدول الرئيسي للنتيجة التحليلية |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, met… |
| حالات الاستخدام | UC-014، UC-015 | Assess Uncertainty؛ Produce Assessment |
| الاختبار | TST-FINDING-SM، TST-SLC07-INVARIANTS | دورة حالات النتيجة التحليلية، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-FND-WITHDRAW -->

</details>

### 5.5 US-BC03-Q-FND-LIST — جلب: Findings with sources

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

<!-- BEGIN GENERATED: refs US-BC03-Q-FND-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/analysis-cases/{case_id}/findings` | — |
| الاستعلام | `QRY-FND-LIST` | Findings with sources |
| السياسة | `POL-FND-LIST` | label rule |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, met… |
| حالات الاستخدام | UC-014، UC-015 | Assess Uncertainty؛ Produce Assessment |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-Q-FND-LIST -->

</details>

### 5.6 US-DOM-ANL-FND-WITHDRAW-FLAG — تعليم التقييمات المستشهدة بنتيجة مسحوبة للمراجعة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-ANL-FND-WITHDRAW-FLAG -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `analysis-reproducibility-spec.md §6` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, met… |
| حالات الاستخدام | UC-014، UC-015 | Assess Uncertainty؛ Produce Assessment |
<!-- END GENERATED: refs US-DOM-ANL-FND-WITHDRAW-FLAG -->

</details>

### 5.7 US-UI-SCR30-FINDINGS — قائمة النتائج بمصادرها وعدم اليقين وحالة القبول

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

<!-- BEGIN GENERATED: refs US-UI-SCR30-FINDINGS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-30 | شاشة الحالة التحليلية والتشغيلات |
| المصدر | `QRY-FND-LIST` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, met… |
| حالات الاستخدام | UC-014، UC-015 | Assess Uncertainty؛ Produce Assessment |
<!-- END GENERATED: refs US-UI-SCR30-FINDINGS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, met… | `US-BC03-FND-ACCEPT`، `US-BC03-FND-EDIT`، `US-BC03-FND-RECORD`، `US-BC03-FND-WITHDRAW`، `US-BC03-Q-FND-LIST`، `US-DOM-ANL-FND-WITHDRAW-FLAG`، `US-UI-SCR30-FINDINGS` | TST-ASSESSMENT-SM، TST-FINDING-SM، TST-SLC07-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
