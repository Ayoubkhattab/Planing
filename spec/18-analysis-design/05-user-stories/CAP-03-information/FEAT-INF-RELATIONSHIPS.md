---
id: FEAT-INF-RELATIONSHIPS
type: feature
title: "إدارة العلاقات بين الكيانات"
status: DRAFT
version: "0.1"
capability: CAP-03.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة العلاقات بين الكيانات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-RELATIONSHIPS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.01 الكيانات والعلاقات (R1) |
| الأدوار | المحلل؛ النظام؛ أي مستخدم مخوَّل |
| الشاشات | SCR-21 الكيانات والأحداث: العرض المحلول |
| حالات الاستخدام | UC-003 |
| القصص | 8: 5 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يربط المحلل الكيانات بعلاقات موثقة ومؤرخة ويرى كل علاقات الكيان في الاتجاهين.

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
| QAS-SEC-011 | inference test suite on search, suggestions, facets, graph and paths | 0 disclosures of hidden objects, hidden facts, hidden nodes/edges |
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
| `US-BC02-REL-RECLASSIFY` | إعادة تصنيف العلاقة | أمر | مسودة |
| `US-BC02-REL-REGISTER` | تسجيل العلاقة | أمر | مسودة |
| `US-BC02-REL-REINSTATE` | إعادة العلاقة إلى السريان | أمر | مسودة |
| `US-BC02-REL-RETIRE` | إحالة العلاقة إلى التقاعد | أمر | مسودة |
| `US-BC02-Q-REL-LIST` | جلب: Relationships valid_at/known_at, both directions | جلب | مسودة |
| `US-UI-SCR21-RELATION-FORM` | ربط كيانين بعلاقة مؤرخة من صفحة الكيان | واجهة | مسودة |
| `US-UI-SCR21-RELATIONS-PANEL` | عرض علاقات الكيان في الاتجاهين مجمعة بالنوع | واجهة | مسودة |
| `US-PLT-REL-HIGHER-LABEL` | إخفاء العلاقة الأعلى تصنيفًا من طرفيها | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-REL-RECLASSIFY — إعادة تصنيف العلاقة

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

<!-- BEGIN GENERATED: refs US-BC02-REL-RECLASSIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/relationships/{id}/actions/reclassify` | — |
| الأمر | `CMD-REL-RECLASSIFY` | إعادة تصنيف العلاقة |
| السياسة | `POL-REL-RECLASSIFY` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-REL-RECLASSIFIED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-RELATIONSHIP` | العلاقة |
| الجدول | `information.relationships` | الجدول الرئيسي للعلاقة |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… |
| حالة الاستخدام | UC-003 | Manage Relationship |
| الاختبار | TST-RELATIONSHIP-SM، TST-SLC02-INVARIANTS | دورة حالات العلاقة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-REL-RECLASSIFY -->

</details>

### 5.2 US-BC02-REL-REGISTER — تسجيل العلاقة

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

<!-- BEGIN GENERATED: refs US-BC02-REL-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/relationships` | — |
| الأمر | `CMD-REL-REGISTER` | تسجيل العلاقة |
| السياسة | `POL-REL-REGISTER` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-REL-REGISTERED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-RELATIONSHIP` | العلاقة |
| الجدول | `information.relationships` | الجدول الرئيسي للعلاقة |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… |
| حالة الاستخدام | UC-003 | Manage Relationship |
| الاختبار | TST-RELATIONSHIP-SM، TST-SLC02-INVARIANTS | دورة حالات العلاقة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-REL-REGISTER -->

</details>

### 5.3 US-BC02-REL-REINSTATE — إعادة العلاقة إلى السريان

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

<!-- BEGIN GENERATED: refs US-BC02-REL-REINSTATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/relationships/{id}/actions/reinstate` | — |
| الأمر | `CMD-REL-REINSTATE` | إعادة العلاقة إلى السريان |
| السياسة | `POL-REL-REINSTATE` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-REL-REINSTATED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-RELATIONSHIP` | العلاقة |
| الجدول | `information.relationships` | الجدول الرئيسي للعلاقة |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… |
| حالة الاستخدام | UC-003 | Manage Relationship |
| الاختبار | TST-RELATIONSHIP-SM، TST-SLC02-INVARIANTS | دورة حالات العلاقة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-REL-REINSTATE -->

</details>

### 5.4 US-BC02-REL-RETIRE — إحالة العلاقة إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC02-REL-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/relationships/{id}/actions/retire` | — |
| الأمر | `CMD-REL-RETIRE` | إحالة العلاقة إلى التقاعد |
| السياسة | `POL-REL-RETIRE` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-REL-RETIRED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-RELATIONSHIP` | العلاقة |
| الجدول | `information.relationships` | الجدول الرئيسي للعلاقة |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… |
| حالة الاستخدام | UC-003 | Manage Relationship |
| الاختبار | TST-RELATIONSHIP-SM، TST-SLC02-INVARIANTS | دورة حالات العلاقة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-REL-RETIRE -->

</details>

### 5.5 US-BC02-Q-REL-LIST — جلب: Relationships valid_at/known_at, both directions

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

<!-- BEGIN GENERATED: refs US-BC02-Q-REL-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/entities/{entity_id}/relationships` | — |
| الاستعلام | `QRY-REL-LIST` | Relationships valid_at/known_at, both directions |
| السياسة | `POL-REL-LIST` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… |
| حالة الاستخدام | UC-003 | Manage Relationship |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-REL-LIST -->

</details>

### 5.6 US-UI-SCR21-RELATION-FORM — ربط كيانين بعلاقة مؤرخة من صفحة الكيان

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

<!-- BEGIN GENERATED: refs US-UI-SCR21-RELATION-FORM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-21 | شاشة الكيانات والأحداث: العرض المحلول |
| حالة الاستخدام | UC-003 | Manage Relationship |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… |
| حالة الاستخدام | UC-003 | Manage Relationship |
<!-- END GENERATED: refs US-UI-SCR21-RELATION-FORM -->

</details>

### 5.7 US-UI-SCR21-RELATIONS-PANEL — عرض علاقات الكيان في الاتجاهين مجمعة بالنوع

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

<!-- BEGIN GENERATED: refs US-UI-SCR21-RELATIONS-PANEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-21 | شاشة الكيانات والأحداث: العرض المحلول |
| حالة الاستخدام | UC-003 | Manage Relationship |
| المتطلب | REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… |
| حالة الاستخدام | UC-003 | Manage Relationship |
<!-- END GENERATED: refs US-UI-SCR21-RELATIONS-PANEL -->

</details>

### 5.8 US-PLT-REL-HIGHER-LABEL — إخفاء العلاقة الأعلى تصنيفًا من طرفيها

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

<!-- BEGIN GENERATED: refs US-PLT-REL-HIGHER-LABEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-011 | inference test suite on search, suggestions, facets, graph and paths → 0 disclosures of hidden objects, hidde… |
| المتطلب | REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… |
| حالة الاستخدام | UC-003 | Manage Relationship |
<!-- END GENERATED: refs US-PLT-REL-HIGHER-LABEL -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… | `US-BC02-Q-REL-LIST`، `US-BC02-REL-RECLASSIFY`، `US-BC02-REL-REGISTER`، `US-BC02-REL-REINSTATE`، `US-BC02-REL-RETIRE`، `US-PLT-REL-HIGHER-LABEL`، `US-UI-SCR21-RELATION-FORM`، `US-UI-SCR21-RELATIONS-PANEL` | TST-RELATIONSHIP-SM، TST-SLC02-INVARIANTS، TST-SLC05-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
