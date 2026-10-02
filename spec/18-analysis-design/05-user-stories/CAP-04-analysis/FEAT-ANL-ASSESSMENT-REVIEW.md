---
id: FEAT-ANL-ASSESSMENT-REVIEW
type: feature
title: "مراجعة التقييم ونشره"
status: DRAFT
version: "0.1"
capability: CAP-04.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مراجعة التقييم ونشره

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ANL-ASSESSMENT-REVIEW |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-04 التحليل والتقييم |
| القدرة الفرعية | CAP-04.03 إنتاج التقييم (R1) |
| الأدوار | المراجع؛ قائد المحللين؛ النظام |
| الشاشات | SCR-31 التقييم ونسخه، SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-015 |
| القصص | 7: 4 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يراجع قائد التحليل التقييم فيعيده للتحسين أو ينشره نسخة ثابتة لا تتغير، أو يسحبه إن لزم.

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
| QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance | 0 leakage in inference suite (counts, facets, ordering, timing, errors) |
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
| `US-BC03-ASM-PUBLISH` | نشر التقييم | أمر | مسودة |
| `US-BC03-ASM-RETURN` | إعادة التقييم للمراجعة | أمر | مسودة |
| `US-BC03-ASM-WITHDRAW` | سحب التقييم | أمر | مسودة |
| `US-DOM-ANL-ASM-REVIEW-QUEUE` | تقييمات مقدَّمة تنتظر مراجعتي | جلب | مسودة |
| `US-BC03-S-ASSESSMENT-01` | تلقائي: newer version published (التقييم) | نظام | مسودة |
| `US-UI-SCR06-ASSESSMENT-REVIEWS` | طابور مراجعة التقييمات في قوائم المراجعة | واجهة | مسودة |
| `US-UI-SCR31-REVIEW-ACTIONS` | أفعال المراجعة حسب الحالة وفصل المهام | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-ASM-PUBLISH — نشر التقييم

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

<!-- BEGIN GENERATED: refs US-BC03-ASM-PUBLISH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/assessments/{id}/actions/publish` | — |
| الأمر | `CMD-ASM-PUBLISH` | نشر التقييم |
| السياسة | `POL-ASM-PUBLISH` | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)؛ tenant match;… |
| الحدث | `EVT-ASM-PUBLISHED` | يصل إلى: Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search proje… |
| الكيان | `AGG-ASSESSMENT` | التقييم |
| الجدول | `intelligence.assessment_versions` | الجدول الرئيسي للتقييم |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-005، REQ-ANL-006، REQ-ANL-008 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-015 | Produce Assessment |
| الاختبار | TST-ASSESSMENT-SM، TST-SLC07-INVARIANTS | دورة حالات التقييم، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ASM-PUBLISH -->

</details>

### 5.2 US-BC03-ASM-RETURN — إعادة التقييم للمراجعة

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

<!-- BEGIN GENERATED: refs US-BC03-ASM-RETURN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/assessments/{id}/actions/return` | — |
| الأمر | `CMD-ASM-RETURN` | إعادة التقييم للمراجعة |
| السياسة | `POL-ASM-RETURN` | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)؛ tenant match;… |
| الحدث | `EVT-ASM-RETURNED` | يصل إلى: Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search proje… |
| الكيان | `AGG-ASSESSMENT` | التقييم |
| الجدول | `intelligence.assessment_versions` | الجدول الرئيسي للتقييم |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-005، REQ-ANL-006، REQ-ANL-008 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-015 | Produce Assessment |
| الاختبار | TST-ASSESSMENT-SM، TST-SLC07-INVARIANTS | دورة حالات التقييم، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ASM-RETURN -->

</details>

### 5.3 US-BC03-ASM-WITHDRAW — سحب التقييم

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

<!-- BEGIN GENERATED: refs US-BC03-ASM-WITHDRAW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/assessments/{id}/actions/withdraw` | — |
| الأمر | `CMD-ASM-WITHDRAW` | سحب التقييم |
| السياسة | `POL-ASM-WITHDRAW` | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)؛ tenant match;… |
| الحدث | `EVT-ASM-WITHDRAWN` | يصل إلى: Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search proje… |
| الكيان | `AGG-ASSESSMENT` | التقييم |
| الجدول | `intelligence.assessment_versions` | الجدول الرئيسي للتقييم |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-005، REQ-ANL-006، REQ-ANL-008 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-015 | Produce Assessment |
| الاختبار | TST-ASSESSMENT-SM، TST-SLC07-INVARIANTS | دورة حالات التقييم، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ASM-WITHDRAW -->

</details>

### 5.4 US-DOM-ANL-ASM-REVIEW-QUEUE — تقييمات مقدَّمة تنتظر مراجعتي

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

<!-- BEGIN GENERATED: refs US-DOM-ANL-ASM-REVIEW-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-015 | Produce Assessment |
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, met… |
| حالة الاستخدام | UC-015 | Produce Assessment |
<!-- END GENERATED: refs US-DOM-ANL-ASM-REVIEW-QUEUE -->

</details>

### 5.5 US-BC03-S-ASSESSMENT-01 — تلقائي: newer version published (التقييم)

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

<!-- BEGIN GENERATED: refs US-BC03-S-ASSESSMENT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:newer version published` | system |
| الانتقال | PUBLISHED ← SUPERSEDED | — |
| الحدث | `EVT-ASM-SUPERSEDED` | يصل إلى: Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search proje… |
| الكيان | `AGG-ASSESSMENT` | التقييم |
| الجدول | `intelligence.assessment_versions` | الجدول الرئيسي للتقييم |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-005، REQ-ANL-006، REQ-ANL-008 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-015 | Produce Assessment |
| الاختبار | TST-ASSESSMENT-SM، TST-SLC07-INVARIANTS | دورة حالات التقييم، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-S-ASSESSMENT-01 -->

</details>

### 5.6 US-UI-SCR06-ASSESSMENT-REVIEWS — طابور مراجعة التقييمات في قوائم المراجعة

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

<!-- BEGIN GENERATED: refs US-UI-SCR06-ASSESSMENT-REVIEWS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| حالة الاستخدام | UC-015 | Produce Assessment |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR06-ASSESSMENT-REVIEWS -->

</details>

### 5.7 US-UI-SCR31-REVIEW-ACTIONS — أفعال المراجعة حسب الحالة وفصل المهام

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

<!-- BEGIN GENERATED: refs US-UI-SCR31-REVIEW-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-31 | شاشة التقييم ونسخه |
| المصدر | `17-security-design.md §12.4` | — |
| المصدر | `21-ui-design.md §6.3` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-006 | When an assessment is published, the system shall make that version immutable; later changes shall create a n… |
| حالة الاستخدام | UC-015 | Produce Assessment |
<!-- END GENERATED: refs US-UI-SCR31-REVIEW-ACTIONS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, met… | `US-BC03-ASM-PUBLISH`، `US-BC03-ASM-RETURN`، `US-BC03-ASM-WITHDRAW`، `US-BC03-S-ASSESSMENT-01`، `US-DOM-ANL-ASM-REVIEW-QUEUE` | TST-ASSESSMENT-SM، TST-FINDING-SM، TST-SLC07-INVARIANTS |
| REQ-ANL-006 | When an assessment is published, the system shall make that version immutable; later changes shall create a n… | `US-BC03-ASM-PUBLISH`، `US-BC03-ASM-RETURN`، `US-BC03-ASM-WITHDRAW`، `US-BC03-S-ASSESSMENT-01`، `US-UI-SCR31-REVIEW-ACTIONS` | TST-ASSESSMENT-SM، TST-SLC07-INVARIANTS |
| REQ-ANL-008 | If an assessment references evidence the reader is not authorized to view, then the system shall withhold tha… | كل قصص الميزة المأخوذة من المواصفة (4) | TST-ASSESSMENT-SM، TST-SLC07-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
