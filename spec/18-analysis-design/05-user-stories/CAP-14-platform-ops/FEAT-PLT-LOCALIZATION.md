---
id: FEAT-PLT-LOCALIZATION
type: feature
title: "واجهة عربية وإنجليزية"
status: DRAFT
version: "0.1"
capability: CAP-14.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# واجهة عربية وإنجليزية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-PLT-LOCALIZATION |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-14 تشغيل المنصة |
| القدرة الفرعية | CAP-14.01 المراقبة (R1) |
| الأدوار | أي مستخدم مخوَّل |
| الشاشات | — |
| حالات الاستخدام | — |
| القصص | 11: 0 من المواصفة، و11 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لكل مستخدم العمل بالعربية أو الإنجليزية باتجاه الكتابة المناسب مع إمكانية عرض التاريخ الهجري.

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
| QAS-ACC-001 | uses R1 web screens | WCAG 2.2 level AA conformance (AR and EN) |
| QAS-USA-001 | records an observation with one photo on the mobile app | median ≤ 60 s in usability test with 10 field users |
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
| `US-PLT-A11Y-FIELD-TOUCH` | أهداف لمس كبيرة للاستعمال بيد واحدة | منصة | مسودة |
| `US-PLT-A11Y-NOT-COLOR-ONLY` | الحالة والخطورة لا تعتمدان على اللون | منصة | مسودة |
| `US-PLT-A11Y-WCAG-AA` | توافق شاشات الويب مع WCAG 2.2 AA | منصة | مسودة |
| `US-PLT-L10N-BIDI-ISOLATION` | عرض النص المختلط دون انقلاب الجملة | منصة | مسودة |
| `US-PLT-L10N-EMBEDDED-FONT` | خط عربي ولاتيني مضمّن دون إنترنت | منصة | مسودة |
| `US-PLT-L10N-HIJRI-DATES` | عرض التاريخ الهجري اختياريًا | منصة | مسودة |
| `US-PLT-L10N-LANGUAGE-SWITCH` | تبديل لغة الواجهة لكل مستخدم | منصة | مسودة |
| `US-PLT-L10N-NUMERALS` | أرقام عربية أو لاتينية حسب التفضيل | منصة | مسودة |
| `US-PLT-L10N-RTL-LAYOUT` | اتجاه الصفحة الصحيح في كل الشاشات | منصة | مسودة |
| `US-PLT-L10N-TIME-ZONE` | عرض الوقت بتوقيت المستخدم المحلي | منصة | مسودة |
| `US-PLT-UI-RESPONSIVE` | الواجهة تعمل من عرض 360 بكسل | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-PLT-A11Y-FIELD-TOUCH — أهداف لمس كبيرة للاستعمال بيد واحدة

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

<!-- BEGIN GENERATED: refs US-PLT-A11Y-FIELD-TOUCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §10` | — |
| الجودة | QAS-USA-001 | records an observation with one photo on the mobile app → median ≤ 60 s in usability test with 10 field users |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-A11Y-FIELD-TOUCH -->

</details>

### 5.2 US-PLT-A11Y-NOT-COLOR-ONLY — الحالة والخطورة لا تعتمدان على اللون

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

<!-- BEGIN GENERATED: refs US-PLT-A11Y-NOT-COLOR-ONLY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §10` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-A11Y-NOT-COLOR-ONLY -->

</details>

### 5.3 US-PLT-A11Y-WCAG-AA — توافق شاشات الويب مع WCAG 2.2 AA

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

<!-- BEGIN GENERATED: refs US-PLT-A11Y-WCAG-AA -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-ACC-001 | uses R1 web screens → WCAG 2.2 level AA conformance (AR and EN) |
| المصدر | `21-ui-design.md §10` | — |
<!-- END GENERATED: refs US-PLT-A11Y-WCAG-AA -->

</details>

### 5.4 US-PLT-L10N-BIDI-ISOLATION — عرض النص المختلط دون انقلاب الجملة

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

<!-- BEGIN GENERATED: refs US-PLT-L10N-BIDI-ISOLATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §9` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-L10N-BIDI-ISOLATION -->

</details>

### 5.5 US-PLT-L10N-EMBEDDED-FONT — خط عربي ولاتيني مضمّن دون إنترنت

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

<!-- BEGIN GENERATED: refs US-PLT-L10N-EMBEDDED-FONT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §9` | — |
| فحص البنية | FIT-12 | No external network dependency at runtime or build (air-gapped) |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-L10N-EMBEDDED-FONT -->

</details>

### 5.6 US-PLT-L10N-HIJRI-DATES — عرض التاريخ الهجري اختياريًا

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

<!-- BEGIN GENERATED: refs US-PLT-L10N-HIJRI-DATES -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §9` | — |
| المصدر | `12-solution/ui-architecture.md` | — |
| المتطلب | REQ-PLT-010 | The system shall provide its user interfaces in Arabic and English with right-to-left and left-to-right layou… |
<!-- END GENERATED: refs US-PLT-L10N-HIJRI-DATES -->

</details>

### 5.7 US-PLT-L10N-LANGUAGE-SWITCH — تبديل لغة الواجهة لكل مستخدم

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

<!-- BEGIN GENERATED: refs US-PLT-L10N-LANGUAGE-SWITCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §9` | — |
| المصدر | `23-crosscutting.md §5` | — |
| المتطلب | REQ-PLT-010 | The system shall provide its user interfaces in Arabic and English with right-to-left and left-to-right layou… |
<!-- END GENERATED: refs US-PLT-L10N-LANGUAGE-SWITCH -->

</details>

### 5.8 US-PLT-L10N-NUMERALS — أرقام عربية أو لاتينية حسب التفضيل

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

<!-- BEGIN GENERATED: refs US-PLT-L10N-NUMERALS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §9` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-L10N-NUMERALS -->

</details>

### 5.9 US-PLT-L10N-RTL-LAYOUT — اتجاه الصفحة الصحيح في كل الشاشات

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

<!-- BEGIN GENERATED: refs US-PLT-L10N-RTL-LAYOUT -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-16 | Web: React + MapLibre GL JS, i18n with ICU messages, RTL via CSS logical properties, Hijri display via Intl (… |
| المصدر | `21-ui-design.md §9` | — |
| المتطلب | REQ-PLT-010 | The system shall provide its user interfaces in Arabic and English with right-to-left and left-to-right layou… |
<!-- END GENERATED: refs US-PLT-L10N-RTL-LAYOUT -->

</details>

### 5.10 US-PLT-L10N-TIME-ZONE — عرض الوقت بتوقيت المستخدم المحلي

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

<!-- BEGIN GENERATED: refs US-PLT-L10N-TIME-ZONE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §6.1` | — |
| المصدر | `23-crosscutting.md §4` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-L10N-TIME-ZONE -->

</details>

### 5.11 US-PLT-UI-RESPONSIVE — الواجهة تعمل من عرض 360 بكسل

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

<!-- BEGIN GENERATED: refs US-PLT-UI-RESPONSIVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-16 | Web: React + MapLibre GL JS, i18n with ICU messages, RTL via CSS logical properties, Hijri display via Intl (… |
| المتطلب | REQ-PLT-011 | The system shall provide a responsive web application and a mobile field application. |
<!-- END GENERATED: refs US-PLT-UI-RESPONSIVE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-PLT-010 | The system shall provide its user interfaces in Arabic and English with right-to-left and left-to-right layou… | `US-PLT-L10N-HIJRI-DATES`، `US-PLT-L10N-LANGUAGE-SWITCH`، `US-PLT-L10N-RTL-LAYOUT` | — |
| REQ-PLT-011 | The system shall provide a responsive web application and a mobile field application. | `US-PLT-UI-RESPONSIVE` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
