---
id: FEAT-OPS-PLAN-AUTHORING
type: feature
title: "إعداد الخطة"
status: DRAFT
version: "0.1"
capability: CAP-07.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إعداد الخطة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-OPS-PLAN-AUTHORING |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-07 التخطيط والتنفيذ |
| القدرة الفرعية | CAP-07.01 الأهداف والتخطيط (R1) |
| الأدوار | المخطِّط؛ مالك الخطة |
| الشاشات | SCR-34 الخطة ونسخها |
| حالات الاستخدام | UC-033 |
| القصص | 11: 6 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يصوغ المخطط خطة بأهدافها ومراحلها وأنشطتها ومواردها وجدولها، ثم يقدمها للاعتماد.

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
| `US-BC04-PLN-CREATE` | إنشاء الخطة | أمر | مسودة |
| `US-BC04-PLV-DISCARD` | تجاهل مسودة إصدار الخطة | أمر | مسودة |
| `US-BC04-PLV-DRAFT` | إعداد مسودة إصدار الخطة | أمر | مسودة |
| `US-BC04-PLV-EDIT` | تعديل إصدار الخطة | أمر | مسودة |
| `US-BC04-PLV-SUBMIT` | تقديم إصدار الخطة | أمر | مسودة |
| `US-BC04-Q-PLN-GET` | جلب: Plan with current baseline, draft (if any), implemented decisions | جلب | مسودة |
| `US-DOM-OPS-PLAN-LIST` | قائمة الخطط المرئية حسب الحالة والنوع | جلب | مسودة |
| `US-UI-SCR34-CREATE-FORM` | إنشاء خطة مرتبطة بقرار أو هدف | واجهة | مسودة |
| `US-UI-SCR34-EDITOR` | تحرير محتوى الخطة وفحص اكتماله قبل التقديم | واجهة | مسودة |
| `US-UI-SCR34-PLAN-LIST` | تصفح الخطط وتصفيتها حسب الحالة والنوع | واجهة | مسودة |
| `US-UI-SCR34-TIMELINE` | الجدول الزمني للمراحل والأنشطة والمعالم | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-PLN-CREATE — إنشاء الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLN-CREATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plans` | — |
| الأمر | `CMD-PLN-CREATE` | إنشاء الخطة |
| السياسة | `POL-PLN-CREATE` | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassif… |
| الحدث | `EVT-PLN-CREATED` | يصل إلى: Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assigne… |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-001، REQ-OPS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLN-CREATE -->

</details>

### 5.2 US-BC04-PLV-DISCARD — تجاهل مسودة إصدار الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLV-DISCARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plan-versions/{id}/actions/discard` | — |
| الأمر | `CMD-PLV-DISCARD` | تجاهل مسودة إصدار الخطة |
| السياسة | `POL-PLV-DISCARD` | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve… |
| الحدث | `EVT-PLV-DISCARDED` | يصل إلى: Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (S… |
| الكيان | `AGG-PLAN-VERSION` | إصدار الخطة |
| الجدول | `operations.plan_versions` | الجدول الرئيسي لإصدار الخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,… |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-VERSION-SM، TST-SLC08-INVARIANTS | دورة حالات إصدار الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLV-DISCARD -->

</details>

### 5.3 US-BC04-PLV-DRAFT — إعداد مسودة إصدار الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLV-DRAFT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plan-versions` | — |
| الأمر | `CMD-PLV-DRAFT` | إعداد مسودة إصدار الخطة |
| السياسة | `POL-PLV-DRAFT` | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve… |
| الحدث | `EVT-PLV-DRAFTED` | يصل إلى: Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (S… |
| الكيان | `AGG-PLAN-VERSION` | إصدار الخطة |
| الجدول | `operations.plan_versions` | الجدول الرئيسي لإصدار الخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,… |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-VERSION-SM، TST-SLC08-INVARIANTS | دورة حالات إصدار الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLV-DRAFT -->

</details>

### 5.4 US-BC04-PLV-EDIT — تعديل إصدار الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLV-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plan-versions/{id}/actions/edit` | — |
| الأمر | `CMD-PLV-EDIT` | تعديل إصدار الخطة |
| السياسة | `POL-PLV-EDIT` | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve… |
| الحدث | `EVT-PLV-EDITED` | يصل إلى: Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (S… |
| الكيان | `AGG-PLAN-VERSION` | إصدار الخطة |
| الجدول | `operations.plan_versions` | الجدول الرئيسي لإصدار الخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,… |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-VERSION-SM، TST-SLC08-INVARIANTS | دورة حالات إصدار الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLV-EDIT -->

</details>

### 5.5 US-BC04-PLV-SUBMIT — تقديم إصدار الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLV-SUBMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plan-versions/{id}/actions/submit` | — |
| الأمر | `CMD-PLV-SUBMIT` | تقديم إصدار الخطة |
| السياسة | `POL-PLV-SUBMIT` | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve… |
| الحدث | `EVT-PLV-SUBMITTED` | يصل إلى: Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (S… |
| الكيان | `AGG-PLAN-VERSION` | إصدار الخطة |
| الجدول | `operations.plan_versions` | الجدول الرئيسي لإصدار الخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,… |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-VERSION-SM، TST-SLC08-INVARIANTS | دورة حالات إصدار الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLV-SUBMIT -->

</details>

### 5.6 US-BC04-Q-PLN-GET — جلب: Plan with current baseline, draft (if any), implemented decisions

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

<!-- BEGIN GENERATED: refs US-BC04-Q-PLN-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/plans/{plan_id}` | — |
| الاستعلام | `QRY-PLN-GET` | Plan with current baseline, draft (if any), implemented decisions |
| السياسة | `POL-PLN-GET` | label rule |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,… |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-Q-PLN-GET -->

</details>

### 5.7 US-DOM-OPS-PLAN-LIST — قائمة الخطط المرئية حسب الحالة والنوع

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

<!-- BEGIN GENERATED: refs US-DOM-OPS-PLAN-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-033 | Create Plan |
| الشاشة | SCR-34 | شاشة الخطة ونسخها |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,… |
| حالة الاستخدام | UC-033 | Create Plan |
<!-- END GENERATED: refs US-DOM-OPS-PLAN-LIST -->

</details>

### 5.8 US-UI-SCR34-CREATE-FORM — إنشاء خطة مرتبطة بقرار أو هدف

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

<!-- BEGIN GENERATED: refs US-UI-SCR34-CREATE-FORM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-34 | شاشة الخطة ونسخها |
| حالة الاستخدام | UC-033 | Create Plan |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-002 | The system shall link every approved plan to the decisions or objectives it implements. |
| حالة الاستخدام | UC-033 | Create Plan |
<!-- END GENERATED: refs US-UI-SCR34-CREATE-FORM -->

</details>

### 5.9 US-UI-SCR34-EDITOR — تحرير محتوى الخطة وفحص اكتماله قبل التقديم

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

<!-- BEGIN GENERATED: refs US-UI-SCR34-EDITOR -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-34 | شاشة الخطة ونسخها |
| حالة الاستخدام | UC-033 | Create Plan |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,… |
| حالة الاستخدام | UC-033 | Create Plan |
<!-- END GENERATED: refs US-UI-SCR34-EDITOR -->

</details>

### 5.10 US-UI-SCR34-PLAN-LIST — تصفح الخطط وتصفيتها حسب الحالة والنوع

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

<!-- BEGIN GENERATED: refs US-UI-SCR34-PLAN-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-34 | شاشة الخطة ونسخها |
| المصدر | `21-ui-design.md §6.1` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR34-PLAN-LIST -->

</details>

### 5.11 US-UI-SCR34-TIMELINE — الجدول الزمني للمراحل والأنشطة والمعالم

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

<!-- BEGIN GENERATED: refs US-UI-SCR34-TIMELINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-34 | شاشة الخطة ونسخها |
| المصدر | `21-ui-design.md §10` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,… |
| حالة الاستخدام | UC-033 | Create Plan |
<!-- END GENERATED: refs US-UI-SCR34-TIMELINE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,… | `US-BC04-PLN-CREATE`، `US-BC04-PLV-DISCARD`، `US-BC04-PLV-DRAFT`، `US-BC04-PLV-EDIT`، `US-BC04-PLV-SUBMIT`، `US-BC04-Q-PLN-GET`، `US-DOM-OPS-PLAN-LIST`، `US-UI-SCR34-EDITOR`، `US-UI-SCR34-TIMELINE` | TST-PLAN-SM، TST-PLAN-VERSION-SM، TST-SLC08-INVARIANTS |
| REQ-OPS-002 | The system shall link every approved plan to the decisions or objectives it implements. | `US-BC04-PLN-CREATE`، `US-UI-SCR34-CREATE-FORM` | TST-PLAN-SM، TST-SLC08-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
