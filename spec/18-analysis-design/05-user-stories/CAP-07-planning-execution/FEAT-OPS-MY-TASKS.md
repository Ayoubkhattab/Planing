---
id: FEAT-OPS-MY-TASKS
type: feature
title: "مهامي"
status: DRAFT
version: "0.1"
capability: CAP-07.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مهامي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-OPS-MY-TASKS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-07 التخطيط والتنفيذ |
| القدرة الفرعية | CAP-07.03 إدارة المهام (R1) |
| الأدوار | المسند إليه؛ المستخدم الميداني؛ النظام |
| الشاشات | SCR-01 مهامي، SCR-02 تفاصيل المهمة وسجلها |
| حالات الاستخدام | UC-042، UC-043، UC-046 |
| القصص | 11: 11 من المواصفة، و0 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يرى المسند إليه كل مهامه في قائمة واحدة، وينفّذها خطوة بخطوة حتى تقديم نتيجتها، ولا يضيع شيء مما سجّله.

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
| QAS-REL-003 | update the same object from the same version | 0 silent overwrites |
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
| `US-BC04-TASK-ACCEPT` | قبول المهمة | أمر | مسودة |
| `US-BC04-TASK-ADD-RESULT-ITEM` | إضافة بند نتيجة إلى المهمة | أمر | مسودة |
| `US-BC04-TASK-BLOCK` | تعليق المهمة كمحجوب | أمر | مسودة |
| `US-BC04-TASK-DECLINE` | رفض قبول المهمة | أمر | مسودة |
| `US-BC04-TASK-RESUME` | استئناف المهمة | أمر | مسودة |
| `US-BC04-TASK-START` | بدء المهمة | أمر | مسودة |
| `US-BC04-TASK-SUBMIT` | تقديم المهمة | أمر | مسودة |
| `US-BC04-Q-TASK-GET` | جلب: Task with criteria status, result, eligibility snapshot, dependencies | جلب | مسودة |
| `US-BC04-Q-TASK-HISTORY` | جلب: State history; state as of t (RECONSTRUCTED) | جلب | مسودة |
| `US-BC04-Q-TASK-LIST` | جلب: Tasks by assignee (me), plan, state, due_before, unit | جلب | مسودة |
| `US-BC04-S-TASK-05` | تلقائي: due passed (escalation policy) (المهمة) | نظام | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-TASK-ACCEPT — قبول المهمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-TASK-ACCEPT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/accept` | دون اتصال: نعم |
| الأمر | `CMD-TASK-ACCEPT` | قبول المهمة |
| السياسة | `POL-TASK-ACCEPT` | assignee؛ tenant match; task visible; org scope; offline allowed |
| الحدث | `EVT-TASK-ACCEPTED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| المتطلب | REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… |
| المتطلب | REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. |
| المتطلب | REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… |
| المتطلب | REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… |
| المتطلب | REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… |
| المتطلب | REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-ACCEPT -->

</details>

### 5.2 US-BC04-TASK-ADD-RESULT-ITEM — إضافة بند نتيجة إلى المهمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-TASK-ADD-RESULT-ITEM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/add-result-item` | دون اتصال: نعم |
| الأمر | `CMD-TASK-ADD-RESULT-ITEM` | إضافة بند نتيجة إلى المهمة |
| السياسة | `POL-TASK-ADD-RESULT-ITEM` | assignee؛ tenant match; task visible; org scope; offline allowed |
| الحدث | `EVT-TASK-RESULT-ITEM-ADDED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| المتطلب | REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… |
| المتطلب | REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. |
| المتطلب | REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… |
| المتطلب | REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… |
| المتطلب | REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… |
| المتطلب | REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-ADD-RESULT-ITEM -->

</details>

### 5.3 US-BC04-TASK-BLOCK — تعليق المهمة كمحجوب

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-TASK-BLOCK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/block` | دون اتصال: نعم |
| الأمر | `CMD-TASK-BLOCK` | تعليق المهمة كمحجوب |
| السياسة | `POL-TASK-BLOCK` | assignee؛ tenant match; task visible; org scope; offline allowed |
| الحدث | `EVT-TASK-BLOCKED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| المتطلب | REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… |
| المتطلب | REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. |
| المتطلب | REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… |
| المتطلب | REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… |
| المتطلب | REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… |
| المتطلب | REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-BLOCK -->

</details>

### 5.4 US-BC04-TASK-DECLINE — رفض قبول المهمة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-DECLINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/decline` | — |
| الأمر | `CMD-TASK-DECLINE` | رفض قبول المهمة |
| السياسة | `POL-TASK-DECLINE` | assignee؛ tenant match; task visible; org scope |
| الحدث | `EVT-TASK-DECLINED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| المتطلب | REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… |
| المتطلب | REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. |
| المتطلب | REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… |
| المتطلب | REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… |
| المتطلب | REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… |
| المتطلب | REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-DECLINE -->

</details>

### 5.5 US-BC04-TASK-RESUME — استئناف المهمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-TASK-RESUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/resume` | دون اتصال: نعم |
| الأمر | `CMD-TASK-RESUME` | استئناف المهمة |
| السياسة | `POL-TASK-RESUME` | assignee؛ tenant match; task visible; org scope; offline allowed |
| الحدث | `EVT-TASK-RESUMED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| المتطلب | REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… |
| المتطلب | REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. |
| المتطلب | REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… |
| المتطلب | REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… |
| المتطلب | REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… |
| المتطلب | REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-RESUME -->

</details>

### 5.6 US-BC04-TASK-START — بدء المهمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-TASK-START -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/start` | دون اتصال: نعم |
| الأمر | `CMD-TASK-START` | بدء المهمة |
| السياسة | `POL-TASK-START` | assignee؛ tenant match; task visible; org scope; offline allowed |
| الحدث | `EVT-TASK-STARTED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| المتطلب | REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… |
| المتطلب | REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. |
| المتطلب | REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… |
| المتطلب | REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… |
| المتطلب | REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… |
| المتطلب | REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-START -->

</details>

### 5.7 US-BC04-TASK-SUBMIT — تقديم المهمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-TASK-SUBMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/submit` | دون اتصال: نعم |
| الأمر | `CMD-TASK-SUBMIT` | تقديم المهمة |
| السياسة | `POL-TASK-SUBMIT` | assignee؛ tenant match; task visible; org scope; offline allowed |
| الحدث | `EVT-TASK-SUBMITTED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| المتطلب | REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… |
| المتطلب | REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. |
| المتطلب | REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… |
| المتطلب | REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… |
| المتطلب | REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… |
| المتطلب | REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-SUBMIT -->

</details>

### 5.8 US-BC04-Q-TASK-GET — جلب: Task with criteria status, result, eligibility snapshot, dependencies

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

<!-- BEGIN GENERATED: refs US-BC04-Q-TASK-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/tasks/{task_id}` | — |
| الاستعلام | `QRY-TASK-GET` | Task with criteria status, result, eligibility snapshot, dependencies |
| السياسة | `POL-TASK-GET` | assignee, reviewer, Planner/Manager in scope; label rule |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-Q-TASK-GET -->

</details>

### 5.9 US-BC04-Q-TASK-HISTORY — جلب: State history; state as of t (RECONSTRUCTED)

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

<!-- BEGIN GENERATED: refs US-BC04-Q-TASK-HISTORY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/tasks/{task_id}/history` | — |
| الاستعلام | `QRY-TASK-HISTORY` | State history; state as of t (RECONSTRUCTED) |
| السياسة | `POL-TASK-HISTORY` | same as QRY-TASK-GET |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-Q-TASK-HISTORY -->

</details>

### 5.10 US-BC04-Q-TASK-LIST — جلب: Tasks by assignee (me), plan, state, due_before, unit

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

<!-- BEGIN GENERATED: refs US-BC04-Q-TASK-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/tasks` | — |
| الاستعلام | `QRY-TASK-LIST` | Tasks by assignee (me), plan, state, due_before, unit |
| السياسة | `POL-TASK-LIST` | allowed_scope pre-filter |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-Q-TASK-LIST -->

</details>

### 5.11 US-BC04-S-TASK-05 — تلقائي: due passed (escalation policy) (المهمة)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-S-TASK-05 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:due passed (escalation policy)` | scheduler; at due and at due + grace from task type |
| الانتقال | أي حالة غير نهائية ← (بلا تغيير) | — |
| الحدث | `EVT-TASK-ESCALATED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| المتطلب | REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… |
| المتطلب | REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. |
| المتطلب | REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… |
| المتطلب | REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… |
| المتطلب | REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… |
| المتطلب | REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. |
| حالة الاستخدام | UC-042 | Execute Task |
| حالة الاستخدام | UC-043 | Submit Task Result |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-S-TASK-05 -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… | كل قصص الميزة المأخوذة من المواصفة (11) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… | كل قصص الأوامر والنظام في الميزة (8) | TST-SLC03-INVARIANTS، TST-TASK-SM، TST-TASK-TYPE-SM |
| REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. | كل قصص الأوامر والنظام في الميزة (8) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… | كل قصص الأوامر والنظام في الميزة (8) | TST-ROLE-ASSIGNMENT-SM، TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… | كل قصص الأوامر والنظام في الميزة (8) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… | كل قصص الأوامر والنظام في الميزة (8) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. | كل قصص الأوامر والنظام في الميزة (8) | TST-SLC03-INVARIANTS، TST-TASK-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
