---
id: FEAT-COL-REQ-REQUEST
type: feature
title: "طلب حاجة معلوماتية"
status: DRAFT
version: "0.1"
capability: CAP-02.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# طلب حاجة معلوماتية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-REQ-REQUEST |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) |
| الأدوار | المحلل؛ مقدم الطلب |
| الشاشات | SCR-13 لوحة الجمع |
| حالات الاستخدام | UC-120، UC-122 |
| القصص | 8: 6 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمحلل أن يصوغ سؤاله المعلوماتي ومنطقته وموعده ويقدمه للجمع ثم يتابعه حتى يستوفى أو يلغى.

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
| `US-BC02-CRQ-CANCEL` | إلغاء متطلب الجمع | أمر | مسودة |
| `US-BC02-CRQ-DRAFT` | إعداد مسودة متطلب الجمع | أمر | مسودة |
| `US-BC02-CRQ-EDIT` | تعديل متطلب الجمع | أمر | مسودة |
| `US-BC02-CRQ-MARK-SATISFIED` | تعليم متطلب الجمع كمستوفى | أمر | مسودة |
| `US-BC02-CRQ-SUBMIT` | تقديم متطلب الجمع | أمر | مسودة |
| `US-BC02-Q-CRQ-GET` | جلب: Requirement with EEIs and fulfilment computed over observations visible to the caller | جلب | مسودة |
| `US-UI-SCR13-CRQ-FORM` | صياغة طلب الجمع برسم المنطقة وعناصر المعلومات | واجهة | مسودة |
| `US-UI-SCR13-MY-REQUESTS` | متابعة مقدم الطلب لطلباته وحالة استيفائها | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-CRQ-CANCEL — إلغاء متطلب الجمع

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

<!-- BEGIN GENERATED: refs US-BC02-CRQ-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-requirements/{id}/actions/cancel` | — |
| الأمر | `CMD-CRQ-CANCEL` | إلغاء متطلب الجمع |
| السياسة | `POL-CRQ-CANCEL` | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛… |
| الحدث | `EVT-CRQ-CANCELLED` | يصل إلى: Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| الكيان | `AGG-COLLECTION-REQUIREMENT` | متطلب الجمع |
| الجدول | `information.collection_requirements` | الجدول الرئيسي لمتطلب الجمع |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-COL-001، REQ-COL-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-120، UC-122 | Define Collection Requirement؛ Track Requirement Fulfilment |
| الاختبار | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS | دورة حالات متطلب الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CRQ-CANCEL -->

</details>

### 5.2 US-BC02-CRQ-DRAFT — إعداد مسودة متطلب الجمع

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

<!-- BEGIN GENERATED: refs US-BC02-CRQ-DRAFT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-requirements` | — |
| الأمر | `CMD-CRQ-DRAFT` | إعداد مسودة متطلب الجمع |
| السياسة | `POL-CRQ-DRAFT` | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛… |
| الحدث | `EVT-CRQ-DRAFTED` | يصل إلى: Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| الكيان | `AGG-COLLECTION-REQUIREMENT` | متطلب الجمع |
| الجدول | `information.collection_requirements` | الجدول الرئيسي لمتطلب الجمع |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-COL-001، REQ-COL-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-120، UC-122 | Define Collection Requirement؛ Track Requirement Fulfilment |
| الاختبار | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS | دورة حالات متطلب الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CRQ-DRAFT -->

</details>

### 5.3 US-BC02-CRQ-EDIT — تعديل متطلب الجمع

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

<!-- BEGIN GENERATED: refs US-BC02-CRQ-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-requirements/{id}/actions/edit` | — |
| الأمر | `CMD-CRQ-EDIT` | تعديل متطلب الجمع |
| السياسة | `POL-CRQ-EDIT` | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛… |
| الحدث | `EVT-CRQ-EDITED` | يصل إلى: Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| الكيان | `AGG-COLLECTION-REQUIREMENT` | متطلب الجمع |
| الجدول | `information.collection_requirements` | الجدول الرئيسي لمتطلب الجمع |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-COL-001، REQ-COL-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-120، UC-122 | Define Collection Requirement؛ Track Requirement Fulfilment |
| الاختبار | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS | دورة حالات متطلب الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CRQ-EDIT -->

</details>

### 5.4 US-BC02-CRQ-MARK-SATISFIED — تعليم متطلب الجمع كمستوفى

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

<!-- BEGIN GENERATED: refs US-BC02-CRQ-MARK-SATISFIED -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-requirements/{id}/actions/mark-satisfied` | — |
| الأمر | `CMD-CRQ-MARK-SATISFIED` | تعليم متطلب الجمع كمستوفى |
| السياسة | `POL-CRQ-MARK-SATISFIED` | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛… |
| الحدث | `EVT-CRQ-SATISFIED` | يصل إلى: Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| الكيان | `AGG-COLLECTION-REQUIREMENT` | متطلب الجمع |
| الجدول | `information.collection_requirements` | الجدول الرئيسي لمتطلب الجمع |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-COL-001، REQ-COL-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-120، UC-122 | Define Collection Requirement؛ Track Requirement Fulfilment |
| الاختبار | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS | دورة حالات متطلب الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CRQ-MARK-SATISFIED -->

</details>

### 5.5 US-BC02-CRQ-SUBMIT — تقديم متطلب الجمع

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

<!-- BEGIN GENERATED: refs US-BC02-CRQ-SUBMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-requirements/{id}/actions/submit` | — |
| الأمر | `CMD-CRQ-SUBMIT` | تقديم متطلب الجمع |
| السياسة | `POL-CRQ-SUBMIT` | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛… |
| الحدث | `EVT-CRQ-SUBMITTED` | يصل إلى: Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| الكيان | `AGG-COLLECTION-REQUIREMENT` | متطلب الجمع |
| الجدول | `information.collection_requirements` | الجدول الرئيسي لمتطلب الجمع |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-COL-001، REQ-COL-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-120، UC-122 | Define Collection Requirement؛ Track Requirement Fulfilment |
| الاختبار | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS | دورة حالات متطلب الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CRQ-SUBMIT -->

</details>

### 5.6 US-BC02-Q-CRQ-GET — جلب: Requirement with EEIs and fulfilment computed over observations visible to the caller

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

<!-- BEGIN GENERATED: refs US-BC02-Q-CRQ-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/collection-requirements/{requirement_id}` | — |
| الاستعلام | `QRY-CRQ-GET` | Requirement with EEIs and fulfilment computed over observations visible to the caller |
| السياسة | `POL-CRQ-GET` | requester, collection managers; label rule |
| الكيان | `AGG-COLLECTION-REQUIREMENT` | متطلب الجمع |
| الجدول | `information.collection_requirements` | الجدول الرئيسي لمتطلب الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-003 | When observations answering a collection requirement are validated, the system shall update the requirement's… |
| حالة الاستخدام | UC-122 | Track Requirement Fulfilment |
| الاختبار | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS | دورة حالات متطلب الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-Q-CRQ-GET -->

</details>

### 5.7 US-UI-SCR13-CRQ-FORM — صياغة طلب الجمع برسم المنطقة وعناصر المعلومات

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

<!-- BEGIN GENERATED: refs US-UI-SCR13-CRQ-FORM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-13 | شاشة لوحة الجمع |
| المصدر | `collection-spec.md §1` | — |
| حالة الاستخدام | UC-120 | Define Collection Requirement |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-COL-001 | The system shall record information needs as collection requirements with question, area, time window, priori… |
| حالة الاستخدام | UC-120 | Define Collection Requirement |
<!-- END GENERATED: refs US-UI-SCR13-CRQ-FORM -->

</details>

### 5.8 US-UI-SCR13-MY-REQUESTS — متابعة مقدم الطلب لطلباته وحالة استيفائها

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

<!-- BEGIN GENERATED: refs US-UI-SCR13-MY-REQUESTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-13 | شاشة لوحة الجمع |
| حالة الاستخدام | UC-122 | Track Requirement Fulfilment |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-COL-003 | When observations answering a collection requirement are validated, the system shall update the requirement's… |
| حالة الاستخدام | UC-122 | Track Requirement Fulfilment |
<!-- END GENERATED: refs US-UI-SCR13-MY-REQUESTS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-COL-001 | The system shall record information needs as collection requirements with question, area, time window, priori… | `US-BC02-CRQ-CANCEL`، `US-BC02-CRQ-DRAFT`، `US-BC02-CRQ-EDIT`، `US-BC02-CRQ-MARK-SATISFIED`، `US-BC02-CRQ-SUBMIT`، `US-UI-SCR13-CRQ-FORM` | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS |
| REQ-COL-003 | When observations answering a collection requirement are validated, the system shall update the requirement's… | `US-BC02-CRQ-CANCEL`، `US-BC02-CRQ-DRAFT`، `US-BC02-CRQ-EDIT`، `US-BC02-CRQ-MARK-SATISFIED`، `US-BC02-CRQ-SUBMIT`، `US-BC02-Q-CRQ-GET`، `US-UI-SCR13-MY-REQUESTS` | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
