---
id: FEAT-COL-OBS-REVIEW
type: feature
title: "التحقق من الملاحظات"
status: DRAFT
version: "0.1"
capability: CAP-02.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# التحقق من الملاحظات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-OBS-REVIEW |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) |
| الأدوار | المحلل |
| الشاشات | SCR-23 الملاحظات، SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-005 |
| القصص | 4: 3 من المواصفة، و1 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمحلل اعتماد الملاحظة أو رفضها أو إعادة تصنيفها قبل أن تعتمد عليها التحليلات.

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
| `US-BC02-OBS-RECLASSIFY` | إعادة تصنيف الملاحظة | أمر | مسودة |
| `US-BC02-OBS-REJECT` | رفض الملاحظة | أمر | مسودة |
| `US-BC02-OBS-VALIDATE` | التحقق من الملاحظة | أمر | مسودة |
| `US-UI-SCR23-VALIDATION-QUEUE` | طابور الملاحظات المنتظرة للتحقق | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-OBS-RECLASSIFY — إعادة تصنيف الملاحظة

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

<!-- BEGIN GENERATED: refs US-BC02-OBS-RECLASSIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/observations/{id}/actions/reclassify` | — |
| الأمر | `CMD-OBS-RECLASSIFY` | إعادة تصنيف الملاحظة |
| السياسة | `POL-OBS-RECLASSIFY` | Analyst (reclassify)؛ tenant match; object visible to subject (label ≤ clearance); write permission in org sc… |
| الحدث | `EVT-OBS-RECLASSIFIED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-OBSERVATION` | الملاحظة |
| الجدول | `information.observations` | الجدول الرئيسي للملاحظة |
| وحدة النشر | DU-05 | — |
| المتطلب | REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… |
| حالة الاستخدام | UC-005 | Register Observation |
| الاختبار | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS | دورة حالات الملاحظة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-OBS-RECLASSIFY -->

</details>

### 5.2 US-BC02-OBS-REJECT — رفض الملاحظة

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

<!-- BEGIN GENERATED: refs US-BC02-OBS-REJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/observations/{id}/actions/reject` | — |
| الأمر | `CMD-OBS-REJECT` | رفض الملاحظة |
| السياسة | `POL-OBS-REJECT` | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)؛ tenant match… |
| الحدث | `EVT-OBS-REJECTED` | يصل إلى: Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (… |
| الكيان | `AGG-OBSERVATION` | الملاحظة |
| الجدول | `information.observations` | الجدول الرئيسي للملاحظة |
| وحدة النشر | DU-05 | — |
| المتطلب | REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… |
| حالة الاستخدام | UC-005 | Register Observation |
| الاختبار | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS | دورة حالات الملاحظة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-OBS-REJECT -->

</details>

### 5.3 US-BC02-OBS-VALIDATE — التحقق من الملاحظة

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

<!-- BEGIN GENERATED: refs US-BC02-OBS-VALIDATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/observations/{id}/actions/validate` | — |
| الأمر | `CMD-OBS-VALIDATE` | التحقق من الملاحظة |
| السياسة | `POL-OBS-VALIDATE` | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)؛ tenant match… |
| الحدث | `EVT-OBS-VALIDATED` | يصل إلى: Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (… |
| الكيان | `AGG-OBSERVATION` | الملاحظة |
| الجدول | `information.observations` | الجدول الرئيسي للملاحظة |
| وحدة النشر | DU-05 | — |
| المتطلب | REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… |
| حالة الاستخدام | UC-005 | Register Observation |
| الاختبار | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS | دورة حالات الملاحظة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-OBS-VALIDATE -->

</details>

### 5.4 US-UI-SCR23-VALIDATION-QUEUE — طابور الملاحظات المنتظرة للتحقق

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

<!-- BEGIN GENERATED: refs US-UI-SCR23-VALIDATION-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-23 | شاشة الملاحظات |
| المصدر | `THR-S02-07` | — |
| المصدر | `21-ui-design.md §6.3` | — |
| حالة الاستخدام | UC-005 | Register Observation |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR23-VALIDATION-QUEUE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… | كل قصص الميزة المأخوذة من المواصفة (3) | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
