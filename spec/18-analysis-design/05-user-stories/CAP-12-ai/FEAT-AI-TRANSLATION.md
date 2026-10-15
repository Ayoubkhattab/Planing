---
id: FEAT-AI-TRANSLATION
type: feature
title: "الترجمة بين العربية والإنجليزية"
status: DRAFT
version: "0.1"
capability: CAP-12.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# الترجمة بين العربية والإنجليزية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-AI-TRANSLATION |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-12 المساعدة بالذكاء الاصطناعي |
| القدرة الفرعية | CAP-12.03 الاستخراج والترجمة (R2) |
| الأدوار | أي مستخدم مخوَّل |
| الشاشات | SCR-22 الادعاء والدليل والمصدر، SCR-45 المساعد الذكي |
| حالات الاستخدام | UC-072 |
| القصص | 4: 0 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح ترجمة النصوص بين العربية والإنجليزية عند الطلب مع بقاء النص الأصلي محفوظًا كما هو.

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
| `US-DOM-AI-TRANSLATION-EVIDENCE` | اعتماد الترجمة دليلًا بعد مراجعة بشرية | أمر | مسودة |
| `US-DOM-AI-TRANSLATION-LINK` | حفظ الترجمة مرتبطة بأصلها | أمر | مسودة |
| `US-UI-SCR22-AI-TRANSLATE` | عرض الترجمة بجانب النص الأصلي | واجهة | مسودة |
| `US-UI-SCR45-AI-TRANSLATE-TEXT` | ترجمة نص من المساعد مع حفظ الأصل | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-DOM-AI-TRANSLATION-EVIDENCE — اعتماد الترجمة دليلًا بعد مراجعة بشرية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-AI-TRANSLATION-EVIDENCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `10-ai/autonomy-matrix.md AI-OP-05` | — |
| المصدر | `US-BC07-AIRS-ACCEPT` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… |
| حالات الاستخدام | UC-073، UC-074 | Review AI Result؛ Approve AI-Assisted Result |
<!-- END GENERATED: refs US-DOM-AI-TRANSLATION-EVIDENCE -->

</details>

### 5.2 US-DOM-AI-TRANSLATION-LINK — حفظ الترجمة مرتبطة بأصلها

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-AI-TRANSLATION-LINK -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `13-verification/acceptance/SLC-10/invariants-slc10.md` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-AI-007 | The system shall translate between Arabic and English on request without replacing the original text. |
| حالة الاستخدام | UC-072 | Generate AI Result |
<!-- END GENERATED: refs US-DOM-AI-TRANSLATION-LINK -->

</details>

### 5.3 US-UI-SCR22-AI-TRANSLATE — عرض الترجمة بجانب النص الأصلي

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR22-AI-TRANSLATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §9` | — |
| المصدر | `10-ai/autonomy-matrix.md AI-OP-05` | — |
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| المتطلب | REQ-AI-007 | The system shall translate between Arabic and English on request without replacing the original text. |
| حالة الاستخدام | UC-072 | Generate AI Result |
<!-- END GENERATED: refs US-UI-SCR22-AI-TRANSLATE -->

</details>

### 5.4 US-UI-SCR45-AI-TRANSLATE-TEXT — ترجمة نص من المساعد مع حفظ الأصل

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR45-AI-TRANSLATE-TEXT -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-072 | Generate AI Result |
| الشاشة | SCR-45 | شاشة المساعد الذكي |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-AI-007 | The system shall translate between Arabic and English on request without replacing the original text. |
| حالة الاستخدام | UC-072 | Generate AI Result |
<!-- END GENERATED: refs US-UI-SCR45-AI-TRANSLATE-TEXT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… | `US-DOM-AI-TRANSLATION-EVIDENCE` | TST-AI-RESULT-SM، TST-SLC10-INVARIANTS |
| REQ-AI-007 | The system shall translate between Arabic and English on request without replacing the original text. | `US-DOM-AI-TRANSLATION-LINK`، `US-UI-SCR22-AI-TRANSLATE`، `US-UI-SCR45-AI-TRANSLATE-TEXT` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
