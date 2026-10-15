---
id: FEAT-KNW-KNOWLEDGE-REUSE
type: feature
title: "البحث في المعرفة وإعادة استخدامها"
status: DRAFT
version: "0.1"
capability: CAP-11.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# البحث في المعرفة وإعادة استخدامها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-KNW-KNOWLEDGE-REUSE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-11 المعرفة والذاكرة المؤسسية |
| القدرة الفرعية | CAP-11.01 الدروس والمعرفة (R2) |
| الأدوار | المخطِّط؛ أي مستخدم مخوَّل |
| الشاشات | SCR-44 المعرفة والأرشيف، SCR-20 البحث الموحد، SCR-34 الخطة ونسخها |
| حالات الاستخدام | UC-062 |
| القصص | 7: 3 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يساعد المخطط والمستخدمين على إيجاد المعرفة المنشورة ذات الصلة بعملهم وتلقي اقتراحات منها وتسجيل الاستفادة منها.

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
| QAS-KNW-001 | planner creates a plan for a known task type | relevant published lessons suggested in ≥ 80 % of cases in pilot |
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
| `US-BC06-KNO-RECORD-REUSE` | تسجيل إعادة استخدام كائن المعرفة | أمر | مسودة |
| `US-BC06-Q-KNO-SEARCH` | جلب: Published knowledge by type, text, relationships | جلب | مسودة |
| `US-BC06-Q-KNO-SUGGEST` | جلب: Published knowledge relevant to a task type / plan / area (by relationships) | جلب | مسودة |
| `US-UI-SCR34-KNOWLEDGE-SUGGEST` | اقتراح الدروس للمخطط أثناء إعداد الخطة | واجهة | مسودة |
| `US-UI-SCR44-KNOWLEDGE-SEARCH` | البحث في المعرفة المنشورة وتصفيتها | واجهة | مسودة |
| `US-PLT-KNOWLEDGE-SEARCH-DOC` | ظهور المعرفة المنشورة في البحث الموحد | منصة | مسودة |
| `US-OPS-KNOWLEDGE-REUSE-METRIC` | قياس إعادة استخدام المعرفة ونجاح الاقتراحات | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC06-KNO-RECORD-REUSE — تسجيل إعادة استخدام كائن المعرفة

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

<!-- BEGIN GENERATED: refs US-BC06-KNO-RECORD-REUSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/record-reuse` | — |
| الأمر | `CMD-KNO-RECORD-REUSE` | تسجيل إعادة استخدام كائن المعرفة |
| السياسة | `POL-KNO-RECORD-REUSE` | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ tenant match… |
| الحدث | `EVT-KNO-REUSED` | يصل إلى: Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| الكيان | `AGG-KNOWLEDGE-OBJECT` | كائن المعرفة |
| الجدول | `knowledge.knowledge_objects` | الجدول الرئيسي لكائن المعرفة |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-KNW-001، REQ-KNW-002، REQ-KNW-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-062 | Publish Knowledge |
| الاختبار | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS | دورة حالات كائن المعرفة، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-KNO-RECORD-REUSE -->

</details>

### 5.2 US-BC06-Q-KNO-SEARCH — جلب: Published knowledge by type, text, relationships

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-Q-KNO-SEARCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/knowledge/knowledge-objects` | — |
| الاستعلام | `QRY-KNO-SEARCH` | Published knowledge by type, text, relationships |
| السياسة | `POL-KNO-SEARCH` | any user; label rule |
| الكيان | `AGG-KNOWLEDGE-OBJECT` | كائن المعرفة |
| الجدول | `knowledge.knowledge_objects` | الجدول الرئيسي لكائن المعرفة |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-KNW-001 | The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims w… |
| حالة الاستخدام | UC-062 | Publish Knowledge |
| الاختبار | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS | دورة حالات كائن المعرفة، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-Q-KNO-SEARCH -->

</details>

### 5.3 US-BC06-Q-KNO-SUGGEST — جلب: Published knowledge relevant to a task type / plan / area (by relationships)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-Q-KNO-SUGGEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/knowledge-suggestions` | — |
| الاستعلام | `QRY-KNO-SUGGEST` | Published knowledge relevant to a task type / plan / area (by relationships) |
| السياسة | `POL-KNO-SUGGEST` | planner; label rule |
| الكيان | `AGG-KNOWLEDGE-OBJECT` | كائن المعرفة |
| الجدول | `knowledge.knowledge_objects` | الجدول الرئيسي لكائن المعرفة |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-KNW-003 | When a published knowledge object is relevant to a new plan or task type, the system shall suggest it to the… |
| حالة الاستخدام | UC-062 | Publish Knowledge |
| الاختبار | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS | دورة حالات كائن المعرفة، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-Q-KNO-SUGGEST -->

</details>

### 5.4 US-UI-SCR34-KNOWLEDGE-SUGGEST — اقتراح الدروس للمخطط أثناء إعداد الخطة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR34-KNOWLEDGE-SUGGEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-KNW-001 | planner creates a plan for a known task type → relevant published lessons suggested in ≥ 80 % of cases in pil… |
| الشاشة | SCR-34 | شاشة الخطة ونسخها |
| المصدر | `03-domain/contexts/BC06/products-knowledge-archive-spec.md §3` | — |
| المتطلب | REQ-KNW-003 | When a published knowledge object is relevant to a new plan or task type, the system shall suggest it to the… |
| حالة الاستخدام | UC-062 | Publish Knowledge |
<!-- END GENERATED: refs US-UI-SCR34-KNOWLEDGE-SUGGEST -->

</details>

### 5.5 US-UI-SCR44-KNOWLEDGE-SEARCH — البحث في المعرفة المنشورة وتصفيتها

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

<!-- BEGIN GENERATED: refs US-UI-SCR44-KNOWLEDGE-SEARCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-062 | Publish Knowledge |
| الشاشة | SCR-44 | شاشة المعرفة والأرشيف |
| المصدر | `US-BC06-Q-KNO-SEARCH` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-KNW-001 | The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims w… |
| حالة الاستخدام | UC-062 | Publish Knowledge |
<!-- END GENERATED: refs US-UI-SCR44-KNOWLEDGE-SEARCH -->

</details>

### 5.6 US-PLT-KNOWLEDGE-SEARCH-DOC — ظهور المعرفة المنشورة في البحث الموحد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-KNOWLEDGE-SEARCH-DOC -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-20 | شاشة البحث الموحد |
| المصدر | `03-domain/contexts/BC07/discovery-architecture.md §3.1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-KNW-001 | The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims w… |
| حالة الاستخدام | UC-062 | Publish Knowledge |
<!-- END GENERATED: refs US-PLT-KNOWLEDGE-SEARCH-DOC -->

</details>

### 5.7 US-OPS-KNOWLEDGE-REUSE-METRIC — قياس إعادة استخدام المعرفة ونجاح الاقتراحات

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R2 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-KNOWLEDGE-REUSE-METRIC -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-KNW-001 | planner creates a plan for a known task type → relevant published lessons suggested in ≥ 80 % of cases in pil… |
| المصدر | `09-reliability/observability-slc12.md` | — |
| المتطلب | REQ-KNW-003 | When a published knowledge object is relevant to a new plan or task type, the system shall suggest it to the… |
| حالة الاستخدام | UC-062 | Publish Knowledge |
<!-- END GENERATED: refs US-OPS-KNOWLEDGE-REUSE-METRIC -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-KNW-001 | The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims w… | `US-BC06-KNO-RECORD-REUSE`، `US-BC06-Q-KNO-SEARCH`، `US-PLT-KNOWLEDGE-SEARCH-DOC`، `US-UI-SCR44-KNOWLEDGE-SEARCH` | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS |
| REQ-KNW-002 | When a task, plan, incident, or exercise simulation is closed or completed, the system shall allow capturing… | `US-BC06-KNO-RECORD-REUSE` | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS |
| REQ-KNW-003 | When a published knowledge object is relevant to a new plan or task type, the system shall suggest it to the… | `US-BC06-KNO-RECORD-REUSE`، `US-BC06-Q-KNO-SUGGEST`، `US-OPS-KNOWLEDGE-REUSE-METRIC`، `US-UI-SCR34-KNOWLEDGE-SUGGEST` | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
