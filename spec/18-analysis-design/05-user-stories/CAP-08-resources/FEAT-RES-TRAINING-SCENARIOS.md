---
id: FEAT-RES-TRAINING-SCENARIOS
type: feature
title: "سيناريوهات التدريب"
status: DRAFT
version: "0.1"
capability: CAP-08.05
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# سيناريوهات التدريب

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-TRAINING-SCENARIOS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.05 التدريب والتمارين (R3) |
| الأدوار | مدير التدريب؛ مدير التمرين |
| الشاشات | SCR-48 التمارين والسيناريوهات والمحاكاة والجاهزية |
| حالات الاستخدام | UC-160 |
| القصص | 8: 6 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يُعد مدير التدريب سيناريوهات تدريب بأحداثها والكفاءات المستهدفة، ويعتمدها مدير التمرين قبل استخدامها.

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
| `US-BC05-SCN-ACTIVATE` | تفعيل سيناريو التدريب | أمر | مسودة |
| `US-BC05-SCN-DEFINE` | تعريف سيناريو التدريب | أمر | مسودة |
| `US-BC05-SCN-EDIT` | تعديل سيناريو التدريب | أمر | مسودة |
| `US-BC05-SCN-RETIRE` | إحالة سيناريو التدريب إلى التقاعد | أمر | مسودة |
| `US-BC05-Q-SCN-GET` | جلب: Scenario with injects and target competencies | جلب | مسودة |
| `US-BC05-Q-SCN-LIST` | جلب: Scenarios filtered by exercise type, state | جلب | مسودة |
| `US-UI-SCR48-SCENARIO-EDITOR` | تحرير السيناريو وأحداثه بترتيبها الزمني | واجهة | مسودة |
| `US-UI-SCR48-SCENARIO-VERSIONS` | نسخ السيناريو والتمارين المرتبطة بكل نسخة | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-SCN-ACTIVATE — تفعيل سيناريو التدريب

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SCN-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/scenarios/{id}/actions/activate` | — |
| الأمر | `CMD-SCN-ACTIVATE` | تفعيل سيناريو التدريب |
| السياسة | `POL-SCN-ACTIVATE` | Exercise Director؛ tenant match; approver ≠ author (INV-SCN via segregation of duties) |
| الحدث | `EVT-SCN-ACTIVATED` | يصل إلى: Exercise (frozen scenario reference on plan); Search projection (SLC-05) |
| الكيان | `AGG-SCENARIO` | سيناريو التدريب |
| الجدول | `readiness.scenarios` | الجدول الرئيسي لسيناريو التدريب |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-001، REQ-TRX-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-160 | Define Training Scenario |
| الاختبار | TST-SCENARIO-SM، TST-SLC19-INVARIANTS | دورة حالات سيناريو التدريب، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-SCN-ACTIVATE -->

</details>

### 5.2 US-BC05-SCN-DEFINE — تعريف سيناريو التدريب

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SCN-DEFINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/scenarios` | — |
| الأمر | `CMD-SCN-DEFINE` | تعريف سيناريو التدريب |
| السياسة | `POL-SCN-DEFINE` | Training Manager؛ tenant match |
| الحدث | `EVT-SCN-DEFINED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-SCENARIO` | سيناريو التدريب |
| الجدول | `readiness.scenarios` | الجدول الرئيسي لسيناريو التدريب |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-001، REQ-TRX-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-160 | Define Training Scenario |
| الاختبار | TST-SCENARIO-SM، TST-SLC19-INVARIANTS | دورة حالات سيناريو التدريب، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-SCN-DEFINE -->

</details>

### 5.3 US-BC05-SCN-EDIT — تعديل سيناريو التدريب

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SCN-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/scenarios/{id}/actions/edit` | — |
| الأمر | `CMD-SCN-EDIT` | تعديل سيناريو التدريب |
| السياسة | `POL-SCN-EDIT` | Training Manager؛ tenant match |
| الحدث | `EVT-SCN-EDITED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-SCENARIO` | سيناريو التدريب |
| الجدول | `readiness.scenarios` | الجدول الرئيسي لسيناريو التدريب |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-001، REQ-TRX-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-160 | Define Training Scenario |
| الاختبار | TST-SCENARIO-SM، TST-SLC19-INVARIANTS | دورة حالات سيناريو التدريب، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-SCN-EDIT -->

</details>

### 5.4 US-BC05-SCN-RETIRE — إحالة سيناريو التدريب إلى التقاعد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SCN-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/scenarios/{id}/actions/retire` | — |
| الأمر | `CMD-SCN-RETIRE` | إحالة سيناريو التدريب إلى التقاعد |
| السياسة | `POL-SCN-RETIRE` | Exercise Director؛ tenant match |
| الحدث | `EVT-SCN-RETIRED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-SCENARIO` | سيناريو التدريب |
| الجدول | `readiness.scenarios` | الجدول الرئيسي لسيناريو التدريب |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-001، REQ-TRX-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-160 | Define Training Scenario |
| الاختبار | TST-SCENARIO-SM، TST-SLC19-INVARIANTS | دورة حالات سيناريو التدريب، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-SCN-RETIRE -->

</details>

### 5.5 US-BC05-Q-SCN-GET — جلب: Scenario with injects and target competencies

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-Q-SCN-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/scenarios/{scenario_id}` | — |
| الاستعلام | `QRY-SCN-GET` | Scenario with injects and target competencies |
| السياسة | `POL-SCN-GET` | allowed_scope |
| الكيان | `AGG-SCENARIO` | سيناريو التدريب |
| الجدول | `readiness.scenarios` | الجدول الرئيسي لسيناريو التدريب |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
| الاختبار | TST-SCENARIO-SM، TST-SLC19-INVARIANTS | دورة حالات سيناريو التدريب، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-Q-SCN-GET -->

</details>

### 5.6 US-BC05-Q-SCN-LIST — جلب: Scenarios filtered by exercise type, state

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-Q-SCN-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/scenarios` | — |
| الاستعلام | `QRY-SCN-LIST` | Scenarios filtered by exercise type, state |
| السياسة | `POL-SCN-LIST` | allowed_scope |
| الكيان | `AGG-SCENARIO` | سيناريو التدريب |
| الجدول | `readiness.scenarios` | الجدول الرئيسي لسيناريو التدريب |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
| الاختبار | TST-SCENARIO-SM، TST-SLC19-INVARIANTS | دورة حالات سيناريو التدريب، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-Q-SCN-LIST -->

</details>

### 5.7 US-UI-SCR48-SCENARIO-EDITOR — تحرير السيناريو وأحداثه بترتيبها الزمني

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR48-SCENARIO-EDITOR -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-48 | شاشة التمارين والسيناريوهات والمحاكاة والجاهزية |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-TRX-001 | The system shall allow defining a training scenario with a situation narrative, target competencies and an or… |
| حالة الاستخدام | UC-160 | Define Training Scenario |
<!-- END GENERATED: refs US-UI-SCR48-SCENARIO-EDITOR -->

</details>

### 5.8 US-UI-SCR48-SCENARIO-VERSIONS — نسخ السيناريو والتمارين المرتبطة بكل نسخة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR48-SCENARIO-VERSIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-48 | شاشة التمارين والسيناريوهات والمحاكاة والجاهزية |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-TRX-002 | Editing an ACTIVE scenario shall create a new version; an exercise already planned against a prior version sh… |
| حالة الاستخدام | UC-160 | Define Training Scenario |
<!-- END GENERATED: refs US-UI-SCR48-SCENARIO-VERSIONS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-TRX-001 | The system shall allow defining a training scenario with a situation narrative, target competencies and an or… | `US-BC05-SCN-ACTIVATE`، `US-BC05-SCN-DEFINE`، `US-BC05-SCN-EDIT`، `US-BC05-SCN-RETIRE`، `US-UI-SCR48-SCENARIO-EDITOR` | TST-SCENARIO-SM |
| REQ-TRX-002 | Editing an ACTIVE scenario shall create a new version; an exercise already planned against a prior version sh… | `US-BC05-SCN-ACTIVATE`، `US-BC05-SCN-DEFINE`، `US-BC05-SCN-EDIT`، `US-BC05-SCN-RETIRE`، `US-UI-SCR48-SCENARIO-VERSIONS` | TST-SCENARIO-SM، TST-SLC19-INVARIANTS |
| REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… | `US-BC05-Q-SCN-GET`، `US-BC05-Q-SCN-LIST` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
