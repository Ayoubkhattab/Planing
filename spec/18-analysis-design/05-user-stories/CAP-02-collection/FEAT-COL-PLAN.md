---
id: FEAT-COL-PLAN
type: feature
title: "تخطيط أنشطة الجمع"
status: DRAFT
version: "0.1"
capability: CAP-02.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تخطيط أنشطة الجمع

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-PLAN |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) |
| الأدوار | مخطط الجمع؛ النظام |
| الشاشات | SCR-13 لوحة الجمع |
| حالات الاستخدام | UC-121 |
| القصص | 11: 8 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لمخطط الجمع أن يحول المتطلب المعتمد إلى خطة أنشطة ومصادر ومهام ميدانية ويتابعها حتى الاكتمال.

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
| QAS-PERF-021 | plan version baselined with 500 task-generating activities | task synchronization completes ≤ 60 s; idempotent on retry |
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
| `US-BC02-CPL-ACTIVATE` | تفعيل خطة الجمع | أمر | مسودة |
| `US-BC02-CPL-ADD-ACTIVITY` | إضافة نشاط إلى خطة الجمع | أمر | مسودة |
| `US-BC02-CPL-CANCEL` | إلغاء خطة الجمع | أمر | مسودة |
| `US-BC02-CPL-COMPLETE` | إكمال خطة الجمع | أمر | مسودة |
| `US-BC02-CPL-CREATE` | إنشاء خطة الجمع | أمر | مسودة |
| `US-BC02-CPL-REMOVE-ACTIVITY` | إزالة نشاط من خطة الجمع | أمر | مسودة |
| `US-BC02-Q-CPL-GET` | جلب: Plan with activities and linked tasks | جلب | مسودة |
| `US-BC02-S-COLLECTION-PLAN-01` | تلقائي: all activity tasks terminal (خطة الجمع) | نظام | مسودة |
| `US-UI-SCR13-PLAN-EDITOR` | إعداد خطة الجمع وأنشطتها على الخريطة | واجهة | مسودة |
| `US-UI-SCR13-PLAN-PROGRESS` | متابعة مهام أنشطة الخطة حتى اكتمالها | واجهة | مسودة |
| `US-PLT-CPL-TASK-SPAWN` | إنشاء مهام الأنشطة مرة واحدة دون تكرار | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-CPL-ACTIVATE — تفعيل خطة الجمع

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

<!-- BEGIN GENERATED: refs US-BC02-CPL-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-plans/{id}/actions/activate` | — |
| الأمر | `CMD-CPL-ACTIVATE` | تفعيل خطة الجمع |
| السياسة | `POL-CPL-ACTIVATE` | collection planner؛ tenant match; area within scope |
| الحدث | `EVT-CPL-ACTIVATED` | يصل إلى: Task creation (SLC-03); Notification (units) |
| الكيان | `AGG-COLLECTION-PLAN` | خطة الجمع |
| الجدول | `information.collection_plans` | الجدول الرئيسي لخطة الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
| الاختبار | TST-COLLECTION-PLAN-SM، TST-SLC14-INVARIANTS | دورة حالات خطة الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CPL-ACTIVATE -->

</details>

### 5.2 US-BC02-CPL-ADD-ACTIVITY — إضافة نشاط إلى خطة الجمع

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

<!-- BEGIN GENERATED: refs US-BC02-CPL-ADD-ACTIVITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-plans/{id}/actions/add-activity` | — |
| الأمر | `CMD-CPL-ADD-ACTIVITY` | إضافة نشاط إلى خطة الجمع |
| السياسة | `POL-CPL-ADD-ACTIVITY` | collection planner؛ tenant match; area within scope |
| الحدث | `EVT-CPL-ACTIVITY-ADDED` | يصل إلى: Task creation (SLC-03); Notification (units) |
| الكيان | `AGG-COLLECTION-PLAN` | خطة الجمع |
| الجدول | `information.collection_plans` | الجدول الرئيسي لخطة الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
| الاختبار | TST-COLLECTION-PLAN-SM، TST-SLC14-INVARIANTS | دورة حالات خطة الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CPL-ADD-ACTIVITY -->

</details>

### 5.3 US-BC02-CPL-CANCEL — إلغاء خطة الجمع

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

<!-- BEGIN GENERATED: refs US-BC02-CPL-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-plans/{id}/actions/cancel` | — |
| الأمر | `CMD-CPL-CANCEL` | إلغاء خطة الجمع |
| السياسة | `POL-CPL-CANCEL` | collection planner؛ tenant match; area within scope |
| الحدث | `EVT-CPL-CANCELLED` | يصل إلى: Task creation (SLC-03); Notification (units) |
| الكيان | `AGG-COLLECTION-PLAN` | خطة الجمع |
| الجدول | `information.collection_plans` | الجدول الرئيسي لخطة الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
| الاختبار | TST-COLLECTION-PLAN-SM، TST-SLC14-INVARIANTS | دورة حالات خطة الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CPL-CANCEL -->

</details>

### 5.4 US-BC02-CPL-COMPLETE — إكمال خطة الجمع

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

<!-- BEGIN GENERATED: refs US-BC02-CPL-COMPLETE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-plans/{id}/actions/complete` | — |
| الأمر | `CMD-CPL-COMPLETE` | إكمال خطة الجمع |
| السياسة | `POL-CPL-COMPLETE` | collection planner؛ tenant match; area within scope |
| الحدث | `EVT-CPL-COMPLETED` | يصل إلى: Task creation (SLC-03); Notification (units) |
| الكيان | `AGG-COLLECTION-PLAN` | خطة الجمع |
| الجدول | `information.collection_plans` | الجدول الرئيسي لخطة الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
| الاختبار | TST-COLLECTION-PLAN-SM، TST-SLC14-INVARIANTS | دورة حالات خطة الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CPL-COMPLETE -->

</details>

### 5.5 US-BC02-CPL-CREATE — إنشاء خطة الجمع

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

<!-- BEGIN GENERATED: refs US-BC02-CPL-CREATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-plans` | — |
| الأمر | `CMD-CPL-CREATE` | إنشاء خطة الجمع |
| السياسة | `POL-CPL-CREATE` | collection planner؛ tenant match; area within scope |
| الحدث | `EVT-CPL-CREATED` | يصل إلى: Task creation (SLC-03); Notification (units) |
| الكيان | `AGG-COLLECTION-PLAN` | خطة الجمع |
| الجدول | `information.collection_plans` | الجدول الرئيسي لخطة الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
| الاختبار | TST-COLLECTION-PLAN-SM، TST-SLC14-INVARIANTS | دورة حالات خطة الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CPL-CREATE -->

</details>

### 5.6 US-BC02-CPL-REMOVE-ACTIVITY — إزالة نشاط من خطة الجمع

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

<!-- BEGIN GENERATED: refs US-BC02-CPL-REMOVE-ACTIVITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/collection-plans/{id}/actions/remove-activity` | — |
| الأمر | `CMD-CPL-REMOVE-ACTIVITY` | إزالة نشاط من خطة الجمع |
| السياسة | `POL-CPL-REMOVE-ACTIVITY` | collection planner؛ tenant match; area within scope |
| الحدث | `EVT-CPL-ACTIVITY-REMOVED` | يصل إلى: Task creation (SLC-03); Notification (units) |
| الكيان | `AGG-COLLECTION-PLAN` | خطة الجمع |
| الجدول | `information.collection_plans` | الجدول الرئيسي لخطة الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
| الاختبار | TST-COLLECTION-PLAN-SM، TST-SLC14-INVARIANTS | دورة حالات خطة الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-CPL-REMOVE-ACTIVITY -->

</details>

### 5.7 US-BC02-Q-CPL-GET — جلب: Plan with activities and linked tasks

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

<!-- BEGIN GENERATED: refs US-BC02-Q-CPL-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/collection-plans/{plan_id}` | — |
| الاستعلام | `QRY-CPL-GET` | Plan with activities and linked tasks |
| السياسة | `POL-CPL-GET` | planner scope |
| الكيان | `AGG-COLLECTION-PLAN` | خطة الجمع |
| الجدول | `information.collection_plans` | الجدول الرئيسي لخطة الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
| الاختبار | TST-COLLECTION-PLAN-SM، TST-SLC14-INVARIANTS | دورة حالات خطة الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-Q-CPL-GET -->

</details>

### 5.8 US-BC02-S-COLLECTION-PLAN-01 — تلقائي: all activity tasks terminal (خطة الجمع)

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

<!-- BEGIN GENERATED: refs US-BC02-S-COLLECTION-PLAN-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:all activity tasks terminal` | SLC-03 events |
| الانتقال | ACTIVE ← COMPLETED | — |
| الحدث | `EVT-CPL-COMPLETED` | يصل إلى: Task creation (SLC-03); Notification (units) |
| الكيان | `AGG-COLLECTION-PLAN` | خطة الجمع |
| الجدول | `information.collection_plans` | الجدول الرئيسي لخطة الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
| الاختبار | TST-COLLECTION-PLAN-SM، TST-SLC14-INVARIANTS | دورة حالات خطة الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-S-COLLECTION-PLAN-01 -->

</details>

### 5.9 US-UI-SCR13-PLAN-EDITOR — إعداد خطة الجمع وأنشطتها على الخريطة

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

<!-- BEGIN GENERATED: refs US-UI-SCR13-PLAN-EDITOR -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-13 | شاشة لوحة الجمع |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
<!-- END GENERATED: refs US-UI-SCR13-PLAN-EDITOR -->

</details>

### 5.10 US-UI-SCR13-PLAN-PROGRESS — متابعة مهام أنشطة الخطة حتى اكتمالها

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

<!-- BEGIN GENERATED: refs US-UI-SCR13-PLAN-PROGRESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-13 | شاشة لوحة الجمع |
| المصدر | `QRY-CPL-GET` | — |
| المصدر | `collection-spec.md §3` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR13-PLAN-PROGRESS -->

</details>

### 5.11 US-PLT-CPL-TASK-SPAWN — إنشاء مهام الأنشطة مرة واحدة دون تكرار

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

<!-- BEGIN GENERATED: refs US-PLT-CPL-TASK-SPAWN -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `collection-spec.md §3` | — |
| المصدر | `CR-59` | — |
| الجودة | QAS-PERF-021 | plan version baselined with 500 task-generating activities → task synchronization completes ≤ 60 s; idempoten… |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… |
| حالة الاستخدام | UC-121 | Plan Collection Activities |
<!-- END GENERATED: refs US-PLT-CPL-TASK-SPAWN -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods… | `US-BC02-CPL-ACTIVATE`، `US-BC02-CPL-ADD-ACTIVITY`، `US-BC02-CPL-CANCEL`، `US-BC02-CPL-COMPLETE`، `US-BC02-CPL-CREATE`، `US-BC02-CPL-REMOVE-ACTIVITY`، `US-BC02-Q-CPL-GET`، `US-BC02-S-COLLECTION-PLAN-01`، `US-PLT-CPL-TASK-SPAWN`، `US-UI-SCR13-PLAN-EDITOR` | TST-COLLECTION-PLAN-SM، TST-SLC14-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
