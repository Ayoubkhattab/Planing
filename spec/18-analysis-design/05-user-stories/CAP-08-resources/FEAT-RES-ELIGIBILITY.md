---
id: FEAT-RES-ELIGIBILITY
type: feature
title: "التحقق من الأهلية والجاهزية"
status: DRAFT
version: "0.1"
capability: CAP-08.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# التحقق من الأهلية والجاهزية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-ELIGIBILITY |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.04 الكفاءة والأهلية (R1 (الأهلية فقط)) |
| الأدوار | المخطِّط؛ مدير الموارد؛ مدير التدريب |
| الشاشات | SCR-42 التأهيل والأهلية، SCR-48 التمارين والسيناريوهات والمحاكاة والجاهزية، SCR-02 تفاصيل المهمة وسجلها |
| حالات الاستخدام | UC-102 |
| القصص | 6: 2 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعرف المخطط ومدير الموارد فورًا هل الشخص أو الوحدة مؤهل لدور أو مهمة في وقت معين، ولماذا.

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
| `US-BC05-Q-ELIG-CHECK` | جلب: EligibilityCheck(person, task_type version, at) → status + reasons | جلب | مسودة |
| `US-BC05-Q-READINESS` | جلب: Readiness of a person or unit for a role at time t, with gaps | جلب | مسودة |
| `US-UI-SCR42-ELIGIBILITY-CHECK` | فحص أهلية شخص مع الأسباب | واجهة | مسودة |
| `US-UI-SCR48-READINESS` | جاهزية الفرد أو الوحدة وفجواتها | واجهة | مسودة |
| `US-PLT-ELIG-FAIL-CLOSED` | لا إسناد إذا تعذر فحص الأهلية | منصة | مسودة |
| `US-PLT-ELIG-ORACLE` | جداول حالات مرجعية لاختبار الأهلية والجاهزية | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-Q-ELIG-CHECK — جلب: EligibilityCheck(person, task_type version, at) → status + reasons

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

<!-- BEGIN GENERATED: refs US-BC05-Q-ELIG-CHECK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/eligibility-checks` | — |
| الاستعلام | `QRY-ELIG-CHECK` | EligibilityCheck(person, task_type version, at) → status + reasons |
| السياسة | `POL-ELIG-CHECK` | Planner/Manager in scope; internal BC04 (workload identity) |
| المتطلب | REQ-RDY-002 | When eligibility is checked for a person, role or task at a given time, the system shall return ELIGIBLE, CON… |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-BC05-Q-ELIG-CHECK -->

</details>

### 5.2 US-BC05-Q-READINESS — جلب: Readiness of a person or unit for a role at time t, with gaps

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

<!-- BEGIN GENERATED: refs US-BC05-Q-READINESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/readiness-checks` | — |
| الاستعلام | `QRY-READINESS` | Readiness of a person or unit for a role at time t, with gaps |
| السياسة | `POL-READINESS` | Manager / Training Manager in scope; self |
| المتطلب | REQ-RES-013 | The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications,… |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-BC05-Q-READINESS -->

</details>

### 5.3 US-UI-SCR42-ELIGIBILITY-CHECK — فحص أهلية شخص مع الأسباب

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

<!-- BEGIN GENERATED: refs US-UI-SCR42-ELIGIBILITY-CHECK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-42 | شاشة التأهيل والأهلية |
| المتطلب | REQ-RDY-002 | When eligibility is checked for a person, role or task at a given time, the system shall return ELIGIBLE, CON… |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-UI-SCR42-ELIGIBILITY-CHECK -->

</details>

### 5.4 US-UI-SCR48-READINESS — جاهزية الفرد أو الوحدة وفجواتها

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

<!-- BEGIN GENERATED: refs US-UI-SCR48-READINESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-48 | شاشة التمارين والسيناريوهات والمحاكاة والجاهزية |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RES-013 | The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications,… |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-UI-SCR48-READINESS -->

</details>

### 5.5 US-PLT-ELIG-FAIL-CLOSED — لا إسناد إذا تعذر فحص الأهلية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-ELIG-FAIL-CLOSED -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `eligibility-rules.md` | — |
| المتطلب | REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-PLT-ELIG-FAIL-CLOSED -->

</details>

### 5.6 US-PLT-ELIG-ORACLE — جداول حالات مرجعية لاختبار الأهلية والجاهزية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-ELIG-ORACLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المتطلبات | REQ-RDY-002، REQ-RES-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-PLT-ELIG-ORACLE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares r… | `US-PLT-ELIG-FAIL-CLOSED` | TST-SLC03-INVARIANTS، TST-TASK-SM، TST-TASK-TYPE-SM |
| REQ-RDY-002 | When eligibility is checked for a person, role or task at a given time, the system shall return ELIGIBLE, CON… | `US-BC05-Q-ELIG-CHECK`، `US-PLT-ELIG-ORACLE`، `US-UI-SCR42-ELIGIBILITY-CHECK` | TST-QUALIFICATION-RECORD-SM، TST-SLC03-INVARIANTS |
| REQ-RES-013 | The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications,… | `US-BC05-Q-READINESS`، `US-PLT-ELIG-ORACLE`، `US-UI-SCR48-READINESS` | TST-ROLE-REQUIREMENT-SM، TST-SLC09-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
