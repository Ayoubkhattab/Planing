---
id: FEAT-KNW-KNOWLEDGE-REVIEW
type: feature
title: "مراجعة المعرفة ونشرها"
status: DRAFT
version: "0.1"
capability: CAP-11.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مراجعة المعرفة ونشرها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-KNW-KNOWLEDGE-REVIEW |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-11 المعرفة والذاكرة المؤسسية |
| القدرة الفرعية | CAP-11.01 الدروس والمعرفة (R2) |
| الأدوار | مدير المعرفة؛ النظام |
| الشاشات | SCR-44 المعرفة والأرشيف، SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-061، UC-062 |
| القصص | 8: 5 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضمن أن ما يُنشر من معرفة مؤسسية قد راجعه مدير المعرفة واعتمده، وأن القديم منه يُسحب أو يُستبدل بنسخة أحدث.

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
| `US-BC06-KNO-PUBLISH` | نشر كائن المعرفة | أمر | مسودة |
| `US-BC06-KNO-REJECT` | رفض كائن المعرفة | أمر | مسودة |
| `US-BC06-KNO-RETIRE` | إحالة كائن المعرفة إلى التقاعد | أمر | مسودة |
| `US-BC06-KNO-RETURN` | إعادة كائن المعرفة للمراجعة | أمر | مسودة |
| `US-DOM-KNO-REVIEW-QUEUE` | عرض المعرفة المنتظرة للمراجعة | جلب | مسودة |
| `US-BC06-S-KNOWLEDGE-OBJECT-01` | تلقائي: newer version published (كائن المعرفة) | نظام | مسودة |
| `US-UI-SCR06-KNOWLEDGE-QUEUE` | قائمة مراجعة المعرفة لمدير المعرفة | واجهة | مسودة |
| `US-UI-SCR44-KNOWLEDGE-REVIEW` | مراجعة كائن المعرفة ومقارنته بنسخته السابقة | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC06-KNO-PUBLISH — نشر كائن المعرفة

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

<!-- BEGIN GENERATED: refs US-BC06-KNO-PUBLISH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/publish` | — |
| الأمر | `CMD-KNO-PUBLISH` | نشر كائن المعرفة |
| السياسة | `POL-KNO-PUBLISH` | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ tenant match… |
| الحدث | `EVT-KNO-PUBLISHED` | يصل إلى: Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| الكيان | `AGG-KNOWLEDGE-OBJECT` | كائن المعرفة |
| الجدول | `knowledge.knowledge_objects` | الجدول الرئيسي لكائن المعرفة |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-KNW-001، REQ-KNW-002، REQ-KNW-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-061، UC-062 | Validate Knowledge؛ Publish Knowledge |
| الاختبار | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS | دورة حالات كائن المعرفة، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-KNO-PUBLISH -->

</details>

### 5.2 US-BC06-KNO-REJECT — رفض كائن المعرفة

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

<!-- BEGIN GENERATED: refs US-BC06-KNO-REJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/reject` | — |
| الأمر | `CMD-KNO-REJECT` | رفض كائن المعرفة |
| السياسة | `POL-KNO-REJECT` | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ tenant match… |
| الحدث | `EVT-KNO-REJECTED` | يصل إلى: Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| الكيان | `AGG-KNOWLEDGE-OBJECT` | كائن المعرفة |
| الجدول | `knowledge.knowledge_objects` | الجدول الرئيسي لكائن المعرفة |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-KNW-001، REQ-KNW-002، REQ-KNW-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-061، UC-062 | Validate Knowledge؛ Publish Knowledge |
| الاختبار | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS | دورة حالات كائن المعرفة، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-KNO-REJECT -->

</details>

### 5.3 US-BC06-KNO-RETIRE — إحالة كائن المعرفة إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC06-KNO-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/retire` | — |
| الأمر | `CMD-KNO-RETIRE` | إحالة كائن المعرفة إلى التقاعد |
| السياسة | `POL-KNO-RETIRE` | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ tenant match… |
| الحدث | `EVT-KNO-RETIRED` | يصل إلى: Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| الكيان | `AGG-KNOWLEDGE-OBJECT` | كائن المعرفة |
| الجدول | `knowledge.knowledge_objects` | الجدول الرئيسي لكائن المعرفة |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-KNW-001، REQ-KNW-002، REQ-KNW-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-061، UC-062 | Validate Knowledge؛ Publish Knowledge |
| الاختبار | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS | دورة حالات كائن المعرفة، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-KNO-RETIRE -->

</details>

### 5.4 US-BC06-KNO-RETURN — إعادة كائن المعرفة للمراجعة

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

<!-- BEGIN GENERATED: refs US-BC06-KNO-RETURN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/return` | — |
| الأمر | `CMD-KNO-RETURN` | إعادة كائن المعرفة للمراجعة |
| السياسة | `POL-KNO-RETURN` | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ tenant match… |
| الحدث | `EVT-KNO-RETURNED` | يصل إلى: Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| الكيان | `AGG-KNOWLEDGE-OBJECT` | كائن المعرفة |
| الجدول | `knowledge.knowledge_objects` | الجدول الرئيسي لكائن المعرفة |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-KNW-001، REQ-KNW-002، REQ-KNW-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-061، UC-062 | Validate Knowledge؛ Publish Knowledge |
| الاختبار | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS | دورة حالات كائن المعرفة، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-KNO-RETURN -->

</details>

### 5.5 US-DOM-KNO-REVIEW-QUEUE — عرض المعرفة المنتظرة للمراجعة

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

<!-- BEGIN GENERATED: refs US-DOM-KNO-REVIEW-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-061 | Validate Knowledge |
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `21-ui-design.md §4.1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-KNW-001 | The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims w… |
| حالات الاستخدام | UC-061، UC-062 | Validate Knowledge؛ Publish Knowledge |
<!-- END GENERATED: refs US-DOM-KNO-REVIEW-QUEUE -->

</details>

### 5.6 US-BC06-S-KNOWLEDGE-OBJECT-01 — تلقائي: newer version published (كائن المعرفة)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-S-KNOWLEDGE-OBJECT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:newer version published` | system |
| الانتقال | PUBLISHED ← SUPERSEDED | — |
| الحدث | `EVT-KNO-SUPERSEDED` | يصل إلى: Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| الكيان | `AGG-KNOWLEDGE-OBJECT` | كائن المعرفة |
| الجدول | `knowledge.knowledge_objects` | الجدول الرئيسي لكائن المعرفة |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-KNW-001، REQ-KNW-002، REQ-KNW-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-061، UC-062 | Validate Knowledge؛ Publish Knowledge |
| الاختبار | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS | دورة حالات كائن المعرفة، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-KNOWLEDGE-OBJECT-01 -->

</details>

### 5.7 US-UI-SCR06-KNOWLEDGE-QUEUE — قائمة مراجعة المعرفة لمدير المعرفة

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

<!-- BEGIN GENERATED: refs US-UI-SCR06-KNOWLEDGE-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-061 | Validate Knowledge |
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `21-ui-design.md §6.1` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR06-KNOWLEDGE-QUEUE -->

</details>

### 5.8 US-UI-SCR44-KNOWLEDGE-REVIEW — مراجعة كائن المعرفة ومقارنته بنسخته السابقة

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

<!-- BEGIN GENERATED: refs US-UI-SCR44-KNOWLEDGE-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-061 | Validate Knowledge |
| حالة الاستخدام | UC-062 | Publish Knowledge |
| الشاشة | SCR-44 | شاشة المعرفة والأرشيف |
| المصدر | `17-security-design.md §12.4` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-KNW-001 | The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims w… |
| حالات الاستخدام | UC-061، UC-062 | Validate Knowledge؛ Publish Knowledge |
<!-- END GENERATED: refs US-UI-SCR44-KNOWLEDGE-REVIEW -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-KNW-001 | The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims w… | `US-BC06-KNO-PUBLISH`، `US-BC06-KNO-REJECT`، `US-BC06-KNO-RETIRE`، `US-BC06-KNO-RETURN`، `US-BC06-S-KNOWLEDGE-OBJECT-01`، `US-DOM-KNO-REVIEW-QUEUE`، `US-UI-SCR44-KNOWLEDGE-REVIEW` | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS |
| REQ-KNW-002 | When a task, plan, incident, or exercise simulation is closed or completed, the system shall allow capturing… | كل قصص الميزة المأخوذة من المواصفة (5) | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS |
| REQ-KNW-003 | When a published knowledge object is relevant to a new plan or task type, the system shall suggest it to the… | كل قصص الميزة المأخوذة من المواصفة (5) | TST-KNOWLEDGE-OBJECT-SM، TST-SLC12-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
