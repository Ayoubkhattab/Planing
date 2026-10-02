---
id: FEAT-OPS-PLAN-APPROVAL
type: feature
title: "اعتماد الخطة"
status: DRAFT
version: "0.1"
capability: CAP-07.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# اعتماد الخطة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-OPS-PLAN-APPROVAL |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-07 التخطيط والتنفيذ |
| القدرة الفرعية | CAP-07.02 إصدارات الخطة وخط الأساس (R1) |
| الأدوار | صاحب السلطة أو المعتمِد الثاني؛ النظام |
| الشاشات | SCR-34 الخطة ونسخها |
| حالات الاستخدام | UC-034، UC-035، UC-036 |
| القصص | 5: 5 من المواصفة، و0 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعتمد صاحب الصلاحية — غير كاتب الخطة — نسخة الخطة فتصبح خط أساس ثابتًا، أو يعيدها أو يرفضها.

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
| `US-BC04-PLV-APPROVE` | اعتماد إصدار الخطة | أمر | مسودة |
| `US-BC04-PLV-REJECT` | رفض إصدار الخطة | أمر | مسودة |
| `US-BC04-PLV-RETURN` | إعادة إصدار الخطة للمراجعة | أمر | مسودة |
| `US-BC04-S-PLAN-01` | تلقائي: first version baselined (الخطة) | نظام | مسودة |
| `US-BC04-S-PLAN-VERSION-01` | تلقائي: newer version baselined (إصدار الخطة) | نظام | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-PLV-APPROVE — اعتماد إصدار الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLV-APPROVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plan-versions/{id}/actions/approve` | — |
| الأمر | `CMD-PLV-APPROVE` | اعتماد إصدار الخطة |
| السياسة | `POL-PLV-APPROVE` | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve… |
| الحدث | `EVT-PLV-BASELINED` | يصل إلى: Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (S… |
| الكيان | `AGG-PLAN-VERSION` | إصدار الخطة |
| الجدول | `operations.plan_versions` | الجدول الرئيسي لإصدار الخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-003 | When a plan is approved, the system shall create an immutable baseline of that plan version. |
| المتطلب | REQ-OPS-004 | When a major change is made to a baselined plan, the system shall create a new plan version that requires app… |
| المتطلب | REQ-OPS-005 | If the approver of a plan is also its author, then the system shall reject the approval unless tenant policy… |
| حالة الاستخدام | UC-034 | Review Plan |
| حالة الاستخدام | UC-035 | Approve Plan |
| حالة الاستخدام | UC-036 | Baseline Plan |
| الاختبار | TST-PLAN-VERSION-SM | اختبار دورة حالات إصدار الخطة |
| الاختبار | TST-SLC08-INVARIANTS | ثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLV-APPROVE -->

</details>

### 5.2 US-BC04-PLV-REJECT — رفض إصدار الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLV-REJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plan-versions/{id}/actions/reject` | — |
| الأمر | `CMD-PLV-REJECT` | رفض إصدار الخطة |
| السياسة | `POL-PLV-REJECT` | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve… |
| الحدث | `EVT-PLV-REJECTED` | يصل إلى: Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (S… |
| الكيان | `AGG-PLAN-VERSION` | إصدار الخطة |
| الجدول | `operations.plan_versions` | الجدول الرئيسي لإصدار الخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-003 | When a plan is approved, the system shall create an immutable baseline of that plan version. |
| المتطلب | REQ-OPS-004 | When a major change is made to a baselined plan, the system shall create a new plan version that requires app… |
| المتطلب | REQ-OPS-005 | If the approver of a plan is also its author, then the system shall reject the approval unless tenant policy… |
| حالة الاستخدام | UC-034 | Review Plan |
| حالة الاستخدام | UC-035 | Approve Plan |
| حالة الاستخدام | UC-036 | Baseline Plan |
| الاختبار | TST-PLAN-VERSION-SM | اختبار دورة حالات إصدار الخطة |
| الاختبار | TST-SLC08-INVARIANTS | ثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLV-REJECT -->

</details>

### 5.3 US-BC04-PLV-RETURN — إعادة إصدار الخطة للمراجعة

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

<!-- BEGIN GENERATED: refs US-BC04-PLV-RETURN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plan-versions/{id}/actions/return` | — |
| الأمر | `CMD-PLV-RETURN` | إعادة إصدار الخطة للمراجعة |
| السياسة | `POL-PLV-RETURN` | Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve… |
| الحدث | `EVT-PLV-RETURNED` | يصل إلى: Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (S… |
| الكيان | `AGG-PLAN-VERSION` | إصدار الخطة |
| الجدول | `operations.plan_versions` | الجدول الرئيسي لإصدار الخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-003 | When a plan is approved, the system shall create an immutable baseline of that plan version. |
| المتطلب | REQ-OPS-004 | When a major change is made to a baselined plan, the system shall create a new plan version that requires app… |
| المتطلب | REQ-OPS-005 | If the approver of a plan is also its author, then the system shall reject the approval unless tenant policy… |
| حالة الاستخدام | UC-034 | Review Plan |
| حالة الاستخدام | UC-035 | Approve Plan |
| حالة الاستخدام | UC-036 | Baseline Plan |
| الاختبار | TST-PLAN-VERSION-SM | اختبار دورة حالات إصدار الخطة |
| الاختبار | TST-SLC08-INVARIANTS | ثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLV-RETURN -->

</details>

### 5.4 US-BC04-S-PLAN-01 — تلقائي: first version baselined (الخطة)

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

<!-- BEGIN GENERATED: refs US-BC04-S-PLAN-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:first version baselined` | EVT-PLV-BASELINED for this plan |
| الانتقال | DRAFT ← ACTIVE | — |
| الحدث | `EVT-PLN-ACTIVATED` | يصل إلى: Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assigne… |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-003 | When a plan is approved, the system shall create an immutable baseline of that plan version. |
| حالة الاستخدام | UC-035 | Approve Plan |
| حالة الاستخدام | UC-036 | Baseline Plan |
| الاختبار | TST-PLAN-SM | اختبار دورة حالات الخطة |
| الاختبار | TST-SLC08-INVARIANTS | ثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-S-PLAN-01 -->

</details>

### 5.5 US-BC04-S-PLAN-VERSION-01 — تلقائي: newer version baselined (إصدار الخطة)

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

<!-- BEGIN GENERATED: refs US-BC04-S-PLAN-VERSION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:newer version baselined` | system |
| الانتقال | BASELINED ← SUPERSEDED | — |
| الحدث | `EVT-PLV-SUPERSEDED` | يصل إلى: Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (S… |
| الكيان | `AGG-PLAN-VERSION` | إصدار الخطة |
| الجدول | `operations.plan_versions` | الجدول الرئيسي لإصدار الخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-003 | When a plan is approved, the system shall create an immutable baseline of that plan version. |
| المتطلب | REQ-OPS-004 | When a major change is made to a baselined plan, the system shall create a new plan version that requires app… |
| المتطلب | REQ-OPS-005 | If the approver of a plan is also its author, then the system shall reject the approval unless tenant policy… |
| حالة الاستخدام | UC-034 | Review Plan |
| حالة الاستخدام | UC-035 | Approve Plan |
| حالة الاستخدام | UC-036 | Baseline Plan |
| الاختبار | TST-PLAN-VERSION-SM | اختبار دورة حالات إصدار الخطة |
| الاختبار | TST-SLC08-INVARIANTS | ثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-S-PLAN-VERSION-01 -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OPS-003 | When a plan is approved, the system shall create an immutable baseline of that plan version. | كل قصص الميزة المأخوذة من المواصفة (5) | TST-PLAN-SM، TST-PLAN-VERSION-SM، TST-SLC08-INVARIANTS |
| REQ-OPS-004 | When a major change is made to a baselined plan, the system shall create a new plan version that requires app… | `US-BC04-PLV-APPROVE`، `US-BC04-PLV-REJECT`، `US-BC04-PLV-RETURN`، `US-BC04-S-PLAN-VERSION-01` | TST-PLAN-VERSION-SM، TST-SLC08-INVARIANTS |
| REQ-OPS-005 | If the approver of a plan is also its author, then the system shall reject the approval unless tenant policy… | `US-BC04-PLV-APPROVE`، `US-BC04-PLV-REJECT`، `US-BC04-PLV-RETURN`، `US-BC04-S-PLAN-VERSION-01` | TST-PLAN-VERSION-SM، TST-ROLE-ASSIGNMENT-SM، TST-SLC08-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
