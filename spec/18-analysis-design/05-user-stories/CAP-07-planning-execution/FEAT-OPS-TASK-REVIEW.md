---
id: FEAT-OPS-TASK-REVIEW
type: feature
title: "مراجعة نتيجة المهمة"
status: DRAFT
version: "0.1"
capability: CAP-07.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مراجعة نتيجة المهمة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-OPS-TASK-REVIEW |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-07 التخطيط والتنفيذ |
| القدرة الفرعية | CAP-07.03 إدارة المهام (R1) |
| الأدوار | المراجع؛ صاحب دور الإقرار؛ النظام |
| الشاشات | SCR-02 تفاصيل المهمة وسجلها، SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-044، UC-045 |
| القصص | 6: 6 من المواصفة، و0 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يراجع المراجع — غير منفّذ المهمة — نتيجتها فيعتمدها أو يعيدها أو يرفضها، ولا تكتمل إلا باستيفاء معاييرها.

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
| `US-BC04-TASK-APPROVE` | اعتماد المهمة | أمر | مسودة |
| `US-BC04-TASK-COMPLETE` | إكمال المهمة | أمر | مسودة |
| `US-BC04-TASK-REJECT` | رفض المهمة | أمر | مسودة |
| `US-BC04-TASK-RETURN` | إعادة المهمة للمراجعة | أمر | مسودة |
| `US-BC04-TASK-START-REVIEW` | بدء مراجعة المهمة | أمر | مسودة |
| `US-BC04-S-TASK-01` | تلقائي: all completion criteria satisfied (المهمة) | نظام | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-TASK-APPROVE — اعتماد المهمة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-APPROVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/approve` | — |
| الأمر | `CMD-TASK-APPROVE` | اعتماد المهمة |
| السياسة | `POL-TASK-APPROVE` | reviewer؛ tenant match; task visible; org scope |
| الحدث | `EVT-TASK-APPROVED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
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
| حالة الاستخدام | UC-044 | Review Task |
| حالة الاستخدام | UC-045 | Complete Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-APPROVE -->

</details>

### 5.2 US-BC04-TASK-COMPLETE — إكمال المهمة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-COMPLETE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/complete` | — |
| الأمر | `CMD-TASK-COMPLETE` | إكمال المهمة |
| السياسة | `POL-TASK-COMPLETE` | reviewer or attestation role؛ tenant match; task visible; org scope |
| الحدث | `EVT-TASK-COMPLETED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
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
| حالة الاستخدام | UC-044 | Review Task |
| حالة الاستخدام | UC-045 | Complete Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-COMPLETE -->

</details>

### 5.3 US-BC04-TASK-REJECT — رفض المهمة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-REJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/reject` | — |
| الأمر | `CMD-TASK-REJECT` | رفض المهمة |
| السياسة | `POL-TASK-REJECT` | reviewer؛ tenant match; task visible; org scope |
| الحدث | `EVT-TASK-REJECTED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
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
| حالة الاستخدام | UC-044 | Review Task |
| حالة الاستخدام | UC-045 | Complete Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-REJECT -->

</details>

### 5.4 US-BC04-TASK-RETURN — إعادة المهمة للمراجعة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-RETURN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/return` | — |
| الأمر | `CMD-TASK-RETURN` | إعادة المهمة للمراجعة |
| السياسة | `POL-TASK-RETURN` | reviewer؛ tenant match; task visible; org scope |
| الحدث | `EVT-TASK-RETURNED-FOR-REWORK` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
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
| حالة الاستخدام | UC-044 | Review Task |
| حالة الاستخدام | UC-045 | Complete Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-RETURN -->

</details>

### 5.5 US-BC04-TASK-START-REVIEW — بدء مراجعة المهمة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-START-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/start-review` | — |
| الأمر | `CMD-TASK-START-REVIEW` | بدء مراجعة المهمة |
| السياسة | `POL-TASK-START-REVIEW` | reviewer role in scope؛ tenant match; task visible; org scope |
| الحدث | `EVT-TASK-REVIEW-STARTED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
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
| حالة الاستخدام | UC-044 | Review Task |
| حالة الاستخدام | UC-045 | Complete Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-START-REVIEW -->

</details>

### 5.6 US-BC04-S-TASK-01 — تلقائي: all completion criteria satisfied (المهمة)

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

<!-- BEGIN GENERATED: refs US-BC04-S-TASK-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:all completion criteria satisfied` | system-checkable criteria evaluated at approval and whenever result evidence changes (BRL-006) |
| الانتقال | APPROVED ← COMPLETED | — |
| الحدث | `EVT-TASK-COMPLETED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
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
| حالة الاستخدام | UC-044 | Review Task |
| حالة الاستخدام | UC-045 | Complete Task |
| الاختبار | TST-TASK-SM | اختبار دورة حالات المهمة |
| الاختبار | TST-SLC03-INVARIANTS | ثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-S-TASK-01 -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… | كل قصص الميزة المأخوذة من المواصفة (6) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… | كل قصص الميزة المأخوذة من المواصفة (6) | TST-SLC03-INVARIANTS، TST-TASK-SM، TST-TASK-TYPE-SM |
| REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. | كل قصص الميزة المأخوذة من المواصفة (6) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… | كل قصص الميزة المأخوذة من المواصفة (6) | TST-ROLE-ASSIGNMENT-SM، TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… | كل قصص الميزة المأخوذة من المواصفة (6) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… | كل قصص الميزة المأخوذة من المواصفة (6) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. | كل قصص الميزة المأخوذة من المواصفة (6) | TST-SLC03-INVARIANTS، TST-TASK-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
