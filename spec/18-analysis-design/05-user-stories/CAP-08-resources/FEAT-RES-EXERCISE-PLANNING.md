---
id: FEAT-RES-EXERCISE-PLANNING
type: feature
title: "تخطيط التمارين وجدولتها"
status: DRAFT
version: "0.1"
capability: CAP-08.05
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تخطيط التمارين وجدولتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-EXERCISE-PLANNING |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.05 التدريب والتمارين (R3) |
| الأدوار | مدير التمرين؛ مدير التدريب |
| الشاشات | SCR-48 التمارين والسيناريوهات والمحاكاة والجاهزية |
| حالات الاستخدام | UC-161 |
| القصص | 9: 6 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يخطط مدير التمرين للتمرين ويحدد موعده ومكانه ومشاركيه ثم يطلقه في وقته.

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
| `US-BC05-EXR-CANCEL` | إلغاء التمرين | أمر | مسودة |
| `US-BC05-EXR-PLAN` | تخطيط التمرين | أمر | مسودة |
| `US-BC05-EXR-SCHEDULE` | جدولة التمرين | أمر | مسودة |
| `US-BC05-EXR-START` | بدء التمرين | أمر | مسودة |
| `US-BC05-Q-EXR-GET` | جلب: Exercise with frozen scenario reference, participants, current state | جلب | مسودة |
| `US-BC05-Q-EXR-LIST` | جلب: Exercises filtered by scenario, state, window | جلب | مسودة |
| `US-DOM-TRX-LABEL` | اشتقاق تصنيف السيناريو والتمرين والمحاكاة | نظام | مسودة |
| `US-UI-SCR48-EXERCISE-CALENDAR` | تقويم التمارين حسب الحالة والموعد | واجهة | مسودة |
| `US-UI-SCR48-EXERCISE-SETUP` | تجهيز التمرين وزر البدء حسب الجاهزية | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-EXR-CANCEL — إلغاء التمرين

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

<!-- BEGIN GENERATED: refs US-BC05-EXR-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/exercises/{id}/actions/cancel` | — |
| الأمر | `CMD-EXR-CANCEL` | إلغاء التمرين |
| السياسة | `POL-EXR-CANCEL` | Exercise Director / Training Manager؛ tenant match |
| الحدث | `EVT-EXR-CANCELLED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-EXERCISE` | التمرين |
| الجدول | `readiness.exercises` | الجدول الرئيسي للتمرين |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-003، REQ-TRX-004، REQ-TRX-005، REQ-TRX-006، REQ-TRX-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
| الاختبار | TST-EXERCISE-SM، TST-SLC19-INVARIANTS | دورة حالات التمرين، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-EXR-CANCEL -->

</details>

### 5.2 US-BC05-EXR-PLAN — تخطيط التمرين

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

<!-- BEGIN GENERATED: refs US-BC05-EXR-PLAN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/exercises` | — |
| الأمر | `CMD-EXR-PLAN` | تخطيط التمرين |
| السياسة | `POL-EXR-PLAN` | Exercise Director / Training Manager؛ tenant match; scenario ACTIVE and visible to actor |
| الحدث | `EVT-EXR-PLANNED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-EXERCISE` | التمرين |
| الجدول | `readiness.exercises` | الجدول الرئيسي للتمرين |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-003، REQ-TRX-004، REQ-TRX-005، REQ-TRX-006، REQ-TRX-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
| الاختبار | TST-EXERCISE-SM، TST-SLC19-INVARIANTS | دورة حالات التمرين، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-EXR-PLAN -->

</details>

### 5.3 US-BC05-EXR-SCHEDULE — جدولة التمرين

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

<!-- BEGIN GENERATED: refs US-BC05-EXR-SCHEDULE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/exercises/{id}/actions/schedule` | — |
| الأمر | `CMD-EXR-SCHEDULE` | جدولة التمرين |
| السياسة | `POL-EXR-SCHEDULE` | Exercise Director / Training Manager؛ tenant match |
| الحدث | `EVT-EXR-SCHEDULED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-EXERCISE` | التمرين |
| الجدول | `readiness.exercises` | الجدول الرئيسي للتمرين |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-003، REQ-TRX-004، REQ-TRX-005، REQ-TRX-006، REQ-TRX-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
| الاختبار | TST-EXERCISE-SM، TST-SLC19-INVARIANTS | دورة حالات التمرين، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-EXR-SCHEDULE -->

</details>

### 5.4 US-BC05-EXR-START — بدء التمرين

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

<!-- BEGIN GENERATED: refs US-BC05-EXR-START -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/exercises/{id}/actions/start` | — |
| الأمر | `CMD-EXR-START` | بدء التمرين |
| السياسة | `POL-EXR-START` | Exercise Director / Training Manager؛ tenant match |
| الحدث | `EVT-EXR-STARTED` | يصل إلى: Simulation (creation trigger); Search projection (SLC-05) |
| الكيان | `AGG-EXERCISE` | التمرين |
| الجدول | `readiness.exercises` | الجدول الرئيسي للتمرين |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-003، REQ-TRX-004، REQ-TRX-005، REQ-TRX-006، REQ-TRX-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
| الاختبار | TST-EXERCISE-SM، TST-SLC19-INVARIANTS | دورة حالات التمرين، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-EXR-START -->

</details>

### 5.5 US-BC05-Q-EXR-GET — جلب: Exercise with frozen scenario reference, participants, current state

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

<!-- BEGIN GENERATED: refs US-BC05-Q-EXR-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/exercises/{exercise_id}` | — |
| الاستعلام | `QRY-EXR-GET` | Exercise with frozen scenario reference, participants, current state |
| السياسة | `POL-EXR-GET` | allowed_scope |
| الكيان | `AGG-EXERCISE` | التمرين |
| الجدول | `readiness.exercises` | الجدول الرئيسي للتمرين |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
| الاختبار | TST-EXERCISE-SM، TST-SLC19-INVARIANTS | دورة حالات التمرين، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-Q-EXR-GET -->

</details>

### 5.6 US-BC05-Q-EXR-LIST — جلب: Exercises filtered by scenario, state, window

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

<!-- BEGIN GENERATED: refs US-BC05-Q-EXR-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/exercises` | — |
| الاستعلام | `QRY-EXR-LIST` | Exercises filtered by scenario, state, window |
| السياسة | `POL-EXR-LIST` | allowed_scope |
| الكيان | `AGG-EXERCISE` | التمرين |
| الجدول | `readiness.exercises` | الجدول الرئيسي للتمرين |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
| الاختبار | TST-EXERCISE-SM، TST-SLC19-INVARIANTS | دورة حالات التمرين، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-Q-EXR-LIST -->

</details>

### 5.7 US-DOM-TRX-LABEL — اشتقاق تصنيف السيناريو والتمرين والمحاكاة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-TRX-LABEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §10` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-002 | The system shall require a classification on every object of importance tier T1 or T2. |
<!-- END GENERATED: refs US-DOM-TRX-LABEL -->

</details>

### 5.8 US-UI-SCR48-EXERCISE-CALENDAR — تقويم التمارين حسب الحالة والموعد

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

<!-- BEGIN GENERATED: refs US-UI-SCR48-EXERCISE-CALENDAR -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-48 | شاشة التمارين والسيناريوهات والمحاكاة والجاهزية |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
<!-- END GENERATED: refs US-UI-SCR48-EXERCISE-CALENDAR -->

</details>

### 5.9 US-UI-SCR48-EXERCISE-SETUP — تجهيز التمرين وزر البدء حسب الجاهزية

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

<!-- BEGIN GENERATED: refs US-UI-SCR48-EXERCISE-SETUP -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-48 | شاشة التمارين والسيناريوهات والمحاكاة والجاهزية |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-TRX-003، REQ-TRX-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
<!-- END GENERATED: refs US-UI-SCR48-EXERCISE-SETUP -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-GOV-002 | The system shall require a classification on every object of importance tier T1 or T2. | `US-DOM-TRX-LABEL` | — |
| REQ-TRX-003 | An exercise shall be planned only against a scenario that is ACTIVE at that instant; the scenario reference s… | `US-BC05-EXR-CANCEL`، `US-BC05-EXR-PLAN`، `US-BC05-EXR-SCHEDULE`، `US-BC05-EXR-START`، `US-UI-SCR48-EXERCISE-SETUP` | TST-EXERCISE-SM، TST-SLC19-INVARIANTS |
| REQ-TRX-004 | An exercise shall be scheduled with a valid time window, a location and confirmed participants before it can… | `US-BC05-EXR-CANCEL`، `US-BC05-EXR-PLAN`، `US-BC05-EXR-SCHEDULE`، `US-BC05-EXR-START`، `US-UI-SCR48-EXERCISE-SETUP` | TST-EXERCISE-SM |
| REQ-TRX-005 | Starting a scheduled exercise shall create exactly one linked simulation run, in the same unit of work. | كل قصص الأوامر والنظام في الميزة (4) | TST-EXERCISE-SM، TST-SLC19-INVARIANTS |
| REQ-TRX-006 | An exercise's terminal outcome (COMPLETED or ABORTED) shall be driven exclusively by its linked simulation's… | كل قصص الأوامر والنظام في الميزة (4) | TST-EXERCISE-SM، TST-SLC19-INVARIANTS |
| REQ-TRX-007 | An exercise shall be cancellable with a reason before it starts, and never once it is in progress. | كل قصص الأوامر والنظام في الميزة (4) | TST-EXERCISE-SM |
| REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… | `US-BC05-Q-EXR-GET`، `US-BC05-Q-EXR-LIST`، `US-UI-SCR48-EXERCISE-CALENDAR` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
