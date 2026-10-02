---
id: FEAT-OPS-TASK-CONTROL
type: feature
title: "متابعة المهام والتدخل"
status: DRAFT
version: "0.1"
capability: CAP-07.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# متابعة المهام والتدخل

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-OPS-TASK-CONTROL |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-07 التخطيط والتنفيذ |
| القدرة الفرعية | CAP-07.03 إدارة المهام (R1) |
| الأدوار | المخطِّط؛ المدير؛ مالك المهمة؛ المسند إليه؛ النظام |
| الشاشات | SCR-02 تفاصيل المهمة وسجلها |
| حالات الاستخدام | UC-046 |
| القصص | 13: 8 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتدخل المخطط أو المدير في مهام جارية فيعلّقها أو يلغيها أو يصعّدها، ويغلق النظام المهام المنتهية أو المتجاوزة آليًا.

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
| QAS-OPS-002 | task reaches due_at | escalation event ≤ 60 s after due |
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
| `US-BC04-TASK-CANCEL` | إلغاء المهمة | أمر | مسودة |
| `US-BC04-TASK-CLOSE` | إغلاق المهمة | أمر | مسودة |
| `US-BC04-TASK-ESCALATE` | تصعيد المهمة | أمر | مسودة |
| `US-BC04-TASK-SUSPEND` | تعليق المهمة | أمر | مسودة |
| `US-BC04-TASK-UNSUSPEND` | رفع تعليق المهمة | أمر | مسودة |
| `US-BC04-S-TASK-02` | تلقائي: follow-up window (7 d) elapsed without open follow-ups (المهمة) | نظام | مسودة |
| `US-BC04-S-TASK-03` | تلقائي: due passed and task type expires_on_due (المهمة) | نظام | مسودة |
| `US-BC04-S-TASK-04` | تلقائي: plan version baselined without this task (المهمة) | نظام | مسودة |
| `US-DOM-OPS-TASK-DEP-ESCALATE` | تصعيد المهام التابعة عند إلغاء سابقتها | نظام | مسودة |
| `US-UI-SCR02-CONTROL-ACTIONS` | أفعال التدخل في المهمة حسب الدور والحالة | واجهة | مسودة |
| `US-UI-SCR02-ESCALATION-NOTICE` | إظهار تصعيد المهمة ومستواه وسببه | واجهة | مسودة |
| `US-PLT-TASK-TIMERS` | مؤقتات المهام تعمل خلال 60 ثانية | منصة | مسودة |
| `US-OPS-TASK-TIMER-LAG` | تنبيه عند تأخر مؤقتات المهام | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-TASK-CANCEL — إلغاء المهمة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/cancel` | — |
| الأمر | `CMD-TASK-CANCEL` | إلغاء المهمة |
| السياسة | `POL-TASK-CANCEL` | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ tenant match; task visible; org sc… |
| الحدث | `EVT-TASK-CANCELLED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-006، REQ-OPS-007، REQ-OPS-008، REQ-OPS-009، REQ-OPS-010، REQ-OPS-011، REQ-OPS-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM، TST-SLC03-INVARIANTS | دورة حالات المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-CANCEL -->

</details>

### 5.2 US-BC04-TASK-CLOSE — إغلاق المهمة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-CLOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/close` | — |
| الأمر | `CMD-TASK-CLOSE` | إغلاق المهمة |
| السياسة | `POL-TASK-CLOSE` | owner / Planner؛ tenant match; task visible; org scope |
| الحدث | `EVT-TASK-CLOSED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-006، REQ-OPS-007، REQ-OPS-008، REQ-OPS-009، REQ-OPS-010، REQ-OPS-011، REQ-OPS-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM، TST-SLC03-INVARIANTS | دورة حالات المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-CLOSE -->

</details>

### 5.3 US-BC04-TASK-ESCALATE — تصعيد المهمة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-ESCALATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/escalate` | — |
| الأمر | `CMD-TASK-ESCALATE` | تصعيد المهمة |
| السياسة | `POL-TASK-ESCALATE` | assignee, owner, Planner؛ tenant match; task visible; org scope |
| الحدث | `EVT-TASK-ESCALATED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-006، REQ-OPS-007، REQ-OPS-008، REQ-OPS-009، REQ-OPS-010، REQ-OPS-011، REQ-OPS-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM، TST-SLC03-INVARIANTS | دورة حالات المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-ESCALATE -->

</details>

### 5.4 US-BC04-TASK-SUSPEND — تعليق المهمة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/suspend` | — |
| الأمر | `CMD-TASK-SUSPEND` | تعليق المهمة |
| السياسة | `POL-TASK-SUSPEND` | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ tenant match; task visible; org sc… |
| الحدث | `EVT-TASK-SUSPENDED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-006، REQ-OPS-007، REQ-OPS-008، REQ-OPS-009، REQ-OPS-010، REQ-OPS-011، REQ-OPS-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM، TST-SLC03-INVARIANTS | دورة حالات المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-SUSPEND -->

</details>

### 5.5 US-BC04-TASK-UNSUSPEND — رفع تعليق المهمة

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

<!-- BEGIN GENERATED: refs US-BC04-TASK-UNSUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/tasks/{id}/actions/unsuspend` | — |
| الأمر | `CMD-TASK-UNSUSPEND` | رفع تعليق المهمة |
| السياسة | `POL-TASK-UNSUSPEND` | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ tenant match; task visible; org sc… |
| الحدث | `EVT-TASK-UNSUSPENDED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-006، REQ-OPS-007، REQ-OPS-008، REQ-OPS-009، REQ-OPS-010، REQ-OPS-011، REQ-OPS-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM، TST-SLC03-INVARIANTS | دورة حالات المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-TASK-UNSUSPEND -->

</details>

### 5.6 US-BC04-S-TASK-02 — تلقائي: follow-up window (7 d) elapsed without open follow-ups (المهمة)

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

<!-- BEGIN GENERATED: refs US-BC04-S-TASK-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:follow-up window (7 d) elapsed without open follow-ups` | scheduler |
| الانتقال | COMPLETED ← CLOSED | — |
| الحدث | `EVT-TASK-CLOSED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-006، REQ-OPS-007، REQ-OPS-008، REQ-OPS-009، REQ-OPS-010، REQ-OPS-011، REQ-OPS-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM، TST-SLC03-INVARIANTS | دورة حالات المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-S-TASK-02 -->

</details>

### 5.7 US-BC04-S-TASK-03 — تلقائي: due passed and task type expires_on_due (المهمة)

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

<!-- BEGIN GENERATED: refs US-BC04-S-TASK-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:due passed and task type expires_on_due` | scheduler; only when the task type declares expires_on_due = true (OQ-032) |
| الانتقال | DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED, SUBMITTED, UNDER_REVIEW ← EXPIRED | — |
| الحدث | `EVT-TASK-EXPIRED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-006، REQ-OPS-007، REQ-OPS-008، REQ-OPS-009، REQ-OPS-010، REQ-OPS-011، REQ-OPS-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM، TST-SLC03-INVARIANTS | دورة حالات المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-S-TASK-03 -->

</details>

### 5.8 US-BC04-S-TASK-04 — تلقائي: plan version baselined without this task (المهمة)

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

<!-- BEGIN GENERATED: refs US-BC04-S-TASK-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:plan version baselined without this task` | SLC-08 trigger |
| الانتقال | DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED, SUBMITTED, UNDER_REVIEW, APPROVED ← SUPERSEDED | — |
| الحدث | `EVT-TASK-SUPERSEDED` | يصل إلى: Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projecti… |
| الكيان | `AGG-TASK` | المهمة |
| الجدول | `operations.tasks` | الجدول الرئيسي للمهمة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-006، REQ-OPS-007، REQ-OPS-008، REQ-OPS-009، REQ-OPS-010، REQ-OPS-011، REQ-OPS-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-046 | Escalate Task |
| الاختبار | TST-TASK-SM، TST-SLC03-INVARIANTS | دورة حالات المهمة، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC04-S-TASK-04 -->

</details>

### 5.9 US-DOM-OPS-TASK-DEP-ESCALATE — تصعيد المهام التابعة عند إلغاء سابقتها

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

<!-- BEGIN GENERATED: refs US-DOM-OPS-TASK-DEP-ESCALATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `task-lifecycle-rules.md §4` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. |
| حالة الاستخدام | UC-046 | Escalate Task |
<!-- END GENERATED: refs US-DOM-OPS-TASK-DEP-ESCALATE -->

</details>

### 5.10 US-UI-SCR02-CONTROL-ACTIONS — أفعال التدخل في المهمة حسب الدور والحالة

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

<!-- BEGIN GENERATED: refs US-UI-SCR02-CONTROL-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-02 | شاشة تفاصيل المهمة وسجلها |
| المصدر | `21-ui-design.md §6.3` | — |
| المصدر | `task-lifecycle-rules.md §1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… |
| حالات الاستخدام | UC-040، UC-042، UC-043، UC-044، UC-045 | Create Task؛ Execute Task؛ Submit Task Result؛ Review Task؛ Complete Task |
<!-- END GENERATED: refs US-UI-SCR02-CONTROL-ACTIONS -->

</details>

### 5.11 US-UI-SCR02-ESCALATION-NOTICE — إظهار تصعيد المهمة ومستواه وسببه

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

<!-- BEGIN GENERATED: refs US-UI-SCR02-ESCALATION-NOTICE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-02 | شاشة تفاصيل المهمة وسجلها |
| حالة الاستخدام | UC-046 | Escalate Task |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. |
| حالة الاستخدام | UC-046 | Escalate Task |
<!-- END GENERATED: refs US-UI-SCR02-ESCALATION-NOTICE -->

</details>

### 5.12 US-PLT-TASK-TIMERS — مؤقتات المهام تعمل خلال 60 ثانية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-TASK-TIMERS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-OPS-002 | task reaches due_at → escalation event ≤ 60 s after due |
| القرار التقني | TD-13 | PostgreSQL time buckets + leased workers inside owning units (no workflow engine) |
| المصدر | `task-lifecycle-rules.md §3` | — |
<!-- END GENERATED: refs US-PLT-TASK-TIMERS -->

</details>

### 5.13 US-OPS-TASK-TIMER-LAG — تنبيه عند تأخر مؤقتات المهام

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-TASK-TIMER-LAG -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-OPS-002 | task reaches due_at → escalation event ≤ 60 s after due |
| المصدر | `23-crosscutting.md §7` | — |
| القرار التقني | TD-14 | OpenTelemetry SDK + Collector; VictoriaMetrics (metrics), VictoriaLogs (logs), Jaeger (traces), Grafana dashb… |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-TASK-TIMER-LAG -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined i… | `US-BC04-S-TASK-02`، `US-BC04-S-TASK-03`، `US-BC04-S-TASK-04`، `US-BC04-TASK-CANCEL`، `US-BC04-TASK-CLOSE`، `US-BC04-TASK-ESCALATE`، `US-BC04-TASK-SUSPEND`، `US-BC04-TASK-UNSUSPEND`، `US-UI-SCR02-CONTROL-ACTIONS` | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… | كل قصص الميزة المأخوذة من المواصفة (8) | TST-SLC03-INVARIANTS، TST-TASK-SM، TST-TASK-TYPE-SM |
| REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. | كل قصص الميزة المأخوذة من المواصفة (8) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenan… | كل قصص الميزة المأخوذة من المواصفة (8) | TST-ROLE-ASSIGNMENT-SM، TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reas… | كل قصص الميزة المأخوذة من المواصفة (8) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and sha… | كل قصص الميزة المأخوذة من المواصفة (8) | TST-SLC03-INVARIANTS، TST-TASK-SM |
| REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. | `US-BC04-S-TASK-02`، `US-BC04-S-TASK-03`، `US-BC04-S-TASK-04`، `US-BC04-TASK-CANCEL`، `US-BC04-TASK-CLOSE`، `US-BC04-TASK-ESCALATE`، `US-BC04-TASK-SUSPEND`، `US-BC04-TASK-UNSUSPEND`، `US-DOM-OPS-TASK-DEP-ESCALATE`، `US-UI-SCR02-ESCALATION-NOTICE` | TST-SLC03-INVARIANTS، TST-TASK-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
