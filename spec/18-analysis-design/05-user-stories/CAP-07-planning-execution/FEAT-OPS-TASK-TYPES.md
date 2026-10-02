---
id: FEAT-OPS-TASK-TYPES
type: feature
title: "أنواع المهام وخطوات اعتمادها"
status: DRAFT
version: "0.1"
capability: CAP-07.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# أنواع المهام وخطوات اعتمادها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-OPS-TASK-TYPES |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-07 التخطيط والتنفيذ |
| القدرة الفرعية | CAP-07.04 سير العمل (R1) |
| الأدوار | مسؤول الإدارة؛ قائد المخططين؛ أي مستخدم مخوَّل |
| الشاشات | SCR-66 أنواع المهام |
| حالات الاستخدام | UC-034، UC-041، UC-044، UC-102 |
| القصص | 10: 5 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يحدد المسؤول لكل نوع مهمة متطلبات الأهلية ومعايير الإكمال وخطوات المراجعة والاعتماد الخاصة بالجهة.

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
| `US-BC04-TTY-ACTIVATE` | تفعيل نوع المهمة | أمر | مسودة |
| `US-BC04-TTY-DEFINE` | تعريف نوع المهمة | أمر | مسودة |
| `US-BC04-TTY-EDIT` | تعديل نوع المهمة | أمر | مسودة |
| `US-BC04-TTY-RETIRE` | إحالة نوع المهمة إلى التقاعد | أمر | مسودة |
| `US-DOM-OPS-APPROVAL-STEPS-SET` | ضبط خطوات اعتماد الخطط للمستأجر | أمر | مسودة |
| `US-BC04-Q-TTY-GET` | جلب: Task type version | جلب | مسودة |
| `US-DOM-OPS-APPROVAL-STEPS-GET` | عرض خطوات الاعتماد السارية وإصداراتها | جلب | مسودة |
| `US-DOM-OPS-TTY-LIST` | قائمة أنواع المهام النشطة | جلب | مسودة |
| `US-UI-SCR66-APPROVAL-STEPS` | شاشة خطوات اعتماد الخطط | واجهة | مسودة |
| `US-UI-SCR66-EDITOR` | تحرير نوع المهمة ومعاييره وتصعيده | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-TTY-ACTIVATE — تفعيل نوع المهمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-TTY-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/task-types/{id}/actions/activate` | — |
| الأمر | `CMD-TTY-ACTIVATE` | تفعيل نوع المهمة |
| السياسة | `POL-TTY-ACTIVATE` | Administrator / Planner lead؛ tenant match; task visible; org scope |
| الحدث | `EVT-TTY-ACTIVATED` | يصل إلى: Task command handler cache |
| الكيان | `AGG-TASK-TYPE` | نوع المهمة |
| الجدول | `operations.task_types` | الجدول الرئيسي لنوع المهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-014 | The system shall allow each tenant to configure review and approval steps for plans and tasks within the limi… |
| حالات الاستخدام | UC-034، UC-044 | Review Plan؛ Review Task |
| الاختبار | TST-TASK-TYPE-SM، TST-SLC03-INVARIANTS | دورة حالات نوع المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TTY-ACTIVATE -->

</details>

### 5.2 US-BC04-TTY-DEFINE — تعريف نوع المهمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-TTY-DEFINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/task-types` | — |
| الأمر | `CMD-TTY-DEFINE` | تعريف نوع المهمة |
| السياسة | `POL-TTY-DEFINE` | Administrator / Planner lead؛ tenant match; task visible; org scope |
| الحدث | `EVT-TTY-DEFINED` | يصل إلى: Task command handler cache |
| الكيان | `AGG-TASK-TYPE` | نوع المهمة |
| الجدول | `operations.task_types` | الجدول الرئيسي لنوع المهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-014 | The system shall allow each tenant to configure review and approval steps for plans and tasks within the limi… |
| حالات الاستخدام | UC-034، UC-044 | Review Plan؛ Review Task |
| الاختبار | TST-TASK-TYPE-SM، TST-SLC03-INVARIANTS | دورة حالات نوع المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TTY-DEFINE -->

</details>

### 5.3 US-BC04-TTY-EDIT — تعديل نوع المهمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-TTY-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/task-types/{id}/actions/edit` | — |
| الأمر | `CMD-TTY-EDIT` | تعديل نوع المهمة |
| السياسة | `POL-TTY-EDIT` | Administrator / Planner lead؛ tenant match; task visible; org scope |
| الحدث | `EVT-TTY-EDITED` | يصل إلى: Task command handler cache |
| الكيان | `AGG-TASK-TYPE` | نوع المهمة |
| الجدول | `operations.task_types` | الجدول الرئيسي لنوع المهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-014 | The system shall allow each tenant to configure review and approval steps for plans and tasks within the limi… |
| حالات الاستخدام | UC-034، UC-044 | Review Plan؛ Review Task |
| الاختبار | TST-TASK-TYPE-SM، TST-SLC03-INVARIANTS | دورة حالات نوع المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TTY-EDIT -->

</details>

### 5.4 US-BC04-TTY-RETIRE — إحالة نوع المهمة إلى التقاعد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-TTY-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/task-types/{id}/actions/retire` | — |
| الأمر | `CMD-TTY-RETIRE` | إحالة نوع المهمة إلى التقاعد |
| السياسة | `POL-TTY-RETIRE` | Administrator / Planner lead؛ tenant match; task visible; org scope |
| الحدث | `EVT-TTY-RETIRED` | يصل إلى: Task command handler cache |
| الكيان | `AGG-TASK-TYPE` | نوع المهمة |
| الجدول | `operations.task_types` | الجدول الرئيسي لنوع المهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-014 | The system shall allow each tenant to configure review and approval steps for plans and tasks within the limi… |
| حالات الاستخدام | UC-034، UC-044 | Review Plan؛ Review Task |
| الاختبار | TST-TASK-TYPE-SM، TST-SLC03-INVARIANTS | دورة حالات نوع المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TTY-RETIRE -->

</details>

### 5.5 US-DOM-OPS-APPROVAL-STEPS-SET — ضبط خطوات اعتماد الخطط للمستأجر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-OPS-APPROVAL-STEPS-SET -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `00-open-questions.md §3` | — |
| حالة الاستخدام | UC-034 | Review Plan |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-014 | The system shall allow each tenant to configure review and approval steps for plans and tasks within the limi… |
| حالات الاستخدام | UC-034، UC-044 | Review Plan؛ Review Task |
<!-- END GENERATED: refs US-DOM-OPS-APPROVAL-STEPS-SET -->

</details>

### 5.6 US-BC04-Q-TTY-GET — جلب: Task type version

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-Q-TTY-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/task-types/{task_type_id}` | — |
| الاستعلام | `QRY-TTY-GET` | Task type version |
| السياسة | `POL-TTY-GET` | any user of tenant |
| الكيان | `AGG-TASK-TYPE` | نوع المهمة |
| الجدول | `operations.task_types` | الجدول الرئيسي لنوع المهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-014 | The system shall allow each tenant to configure review and approval steps for plans and tasks within the limi… |
| حالات الاستخدام | UC-034، UC-044 | Review Plan؛ Review Task |
| الاختبار | TST-TASK-TYPE-SM، TST-SLC03-INVARIANTS | دورة حالات نوع المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-Q-TTY-GET -->

</details>

### 5.7 US-DOM-OPS-APPROVAL-STEPS-GET — عرض خطوات الاعتماد السارية وإصداراتها

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-OPS-APPROVAL-STEPS-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `00-open-questions.md §3` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-014 | The system shall allow each tenant to configure review and approval steps for plans and tasks within the limi… |
| حالات الاستخدام | UC-034، UC-044 | Review Plan؛ Review Task |
<!-- END GENERATED: refs US-DOM-OPS-APPROVAL-STEPS-GET -->

</details>

### 5.8 US-DOM-OPS-TTY-LIST — قائمة أنواع المهام النشطة

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

<!-- BEGIN GENERATED: refs US-DOM-OPS-TTY-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-66 | شاشة أنواع المهام |
| حالة الاستخدام | UC-040 | Create Task |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… |
| حالات الاستخدام | UC-041، UC-102 | Assign Task؛ Check Eligibility |
<!-- END GENERATED: refs US-DOM-OPS-TTY-LIST -->

</details>

### 5.9 US-UI-SCR66-APPROVAL-STEPS — شاشة خطوات اعتماد الخطط

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

<!-- BEGIN GENERATED: refs US-UI-SCR66-APPROVAL-STEPS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-66 | شاشة أنواع المهام |
| المصدر | `00-open-questions.md §3` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-014 | The system shall allow each tenant to configure review and approval steps for plans and tasks within the limi… |
| حالات الاستخدام | UC-034، UC-044 | Review Plan؛ Review Task |
<!-- END GENERATED: refs US-UI-SCR66-APPROVAL-STEPS -->

</details>

### 5.10 US-UI-SCR66-EDITOR — تحرير نوع المهمة ومعاييره وتصعيده

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

<!-- BEGIN GENERATED: refs US-UI-SCR66-EDITOR -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-66 | شاشة أنواع المهام |
| المصدر | `task-lifecycle-rules.md §2` | — |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-OPS-007، REQ-OPS-014 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-034، UC-041، UC-044، UC-102 | Review Plan؛ Assign Task؛ Review Task؛ Check Eligibility |
<!-- END GENERATED: refs US-UI-SCR66-EDITOR -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… | `US-DOM-OPS-TTY-LIST`، `US-UI-SCR66-EDITOR` | TST-SLC03-INVARIANTS، TST-TASK-SM، TST-TASK-TYPE-SM |
| REQ-OPS-014 | The system shall allow each tenant to configure review and approval steps for plans and tasks within the limi… | `US-BC04-Q-TTY-GET`، `US-BC04-TTY-ACTIVATE`، `US-BC04-TTY-DEFINE`، `US-BC04-TTY-EDIT`، `US-BC04-TTY-RETIRE`، `US-DOM-OPS-APPROVAL-STEPS-GET`، `US-DOM-OPS-APPROVAL-STEPS-SET`، `US-UI-SCR66-APPROVAL-STEPS`، `US-UI-SCR66-EDITOR` | TST-PLAN-VERSION-SM، TST-SLC03-INVARIANTS، TST-SLC08-INVARIANTS، TST-TASK-TYPE-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
