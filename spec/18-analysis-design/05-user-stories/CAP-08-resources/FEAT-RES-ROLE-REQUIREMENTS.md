---
id: FEAT-RES-ROLE-REQUIREMENTS
type: feature
title: "متطلبات الأدوار"
status: DRAFT
version: "0.1"
capability: CAP-08.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# متطلبات الأدوار

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-ROLE-REQUIREMENTS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.04 الكفاءة والأهلية (R1 (الأهلية فقط)) |
| الأدوار | مدير التدريب؛ مسؤول الإدارة |
| الشاشات | SCR-42 التأهيل والأهلية |
| حالات الاستخدام | UC-102 |
| القصص | 6: 4 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يحدد مدير التدريب ما يلزم كل دور من مؤهلات وخبرات، ليُبنى عليه الحكم بالأهلية.

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
| `US-BC05-RRQ-ACTIVATE` | تفعيل متطلبات الدور | أمر | مسودة |
| `US-BC05-RRQ-DEFINE` | تعريف متطلبات الدور | أمر | مسودة |
| `US-BC05-RRQ-EDIT` | تعديل متطلبات الدور | أمر | مسودة |
| `US-BC05-RRQ-RETIRE` | إحالة متطلبات الدور إلى التقاعد | أمر | مسودة |
| `US-DOM-RRQ-LIST` | عرض متطلبات الأدوار ونسخها | جلب | مسودة |
| `US-UI-SCR42-ROLE-REQUIREMENTS` | تحرير متطلبات الدور ونسخها واعتمادها | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-RRQ-ACTIVATE — تفعيل متطلبات الدور

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

<!-- BEGIN GENERATED: refs US-BC05-RRQ-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/role-requirements/{id}/actions/activate` | — |
| الأمر | `CMD-RRQ-ACTIVATE` | تفعيل متطلبات الدور |
| السياسة | `POL-RRQ-ACTIVATE` | Training Manager / Administrator؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RRQ-ACTIVATED` | يصل إلى: Readiness evaluator; Eligibility cache |
| الكيان | `AGG-ROLE-REQUIREMENT` | متطلبات الدور |
| الجدول | `readiness.role_requirements` | الجدول الرئيسي لمتطلبات الدور |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-013 | The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications,… |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-ROLE-REQUIREMENT-SM، TST-SLC09-INVARIANTS | دورة حالات متطلبات الدور، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RRQ-ACTIVATE -->

</details>

### 5.2 US-BC05-RRQ-DEFINE — تعريف متطلبات الدور

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

<!-- BEGIN GENERATED: refs US-BC05-RRQ-DEFINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/role-requirements` | — |
| الأمر | `CMD-RRQ-DEFINE` | تعريف متطلبات الدور |
| السياسة | `POL-RRQ-DEFINE` | Training Manager / Administrator؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RRQ-DEFINED` | يصل إلى: Readiness evaluator; Eligibility cache |
| الكيان | `AGG-ROLE-REQUIREMENT` | متطلبات الدور |
| الجدول | `readiness.role_requirements` | الجدول الرئيسي لمتطلبات الدور |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-013 | The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications,… |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-ROLE-REQUIREMENT-SM، TST-SLC09-INVARIANTS | دورة حالات متطلبات الدور، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RRQ-DEFINE -->

</details>

### 5.3 US-BC05-RRQ-EDIT — تعديل متطلبات الدور

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

<!-- BEGIN GENERATED: refs US-BC05-RRQ-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/role-requirements/{id}/actions/edit` | — |
| الأمر | `CMD-RRQ-EDIT` | تعديل متطلبات الدور |
| السياسة | `POL-RRQ-EDIT` | Training Manager / Administrator؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RRQ-EDITED` | يصل إلى: Readiness evaluator; Eligibility cache |
| الكيان | `AGG-ROLE-REQUIREMENT` | متطلبات الدور |
| الجدول | `readiness.role_requirements` | الجدول الرئيسي لمتطلبات الدور |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-013 | The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications,… |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-ROLE-REQUIREMENT-SM، TST-SLC09-INVARIANTS | دورة حالات متطلبات الدور، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RRQ-EDIT -->

</details>

### 5.4 US-BC05-RRQ-RETIRE — إحالة متطلبات الدور إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC05-RRQ-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/role-requirements/{id}/actions/retire` | — |
| الأمر | `CMD-RRQ-RETIRE` | إحالة متطلبات الدور إلى التقاعد |
| السياسة | `POL-RRQ-RETIRE` | Training Manager / Administrator؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RRQ-RETIRED` | يصل إلى: Readiness evaluator; Eligibility cache |
| الكيان | `AGG-ROLE-REQUIREMENT` | متطلبات الدور |
| الجدول | `readiness.role_requirements` | الجدول الرئيسي لمتطلبات الدور |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-013 | The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications,… |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-ROLE-REQUIREMENT-SM، TST-SLC09-INVARIANTS | دورة حالات متطلبات الدور، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RRQ-RETIRE -->

</details>

### 5.5 US-DOM-RRQ-LIST — عرض متطلبات الأدوار ونسخها

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

<!-- BEGIN GENERATED: refs US-DOM-RRQ-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-42 | شاشة التأهيل والأهلية |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RES-013 | The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications,… |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-DOM-RRQ-LIST -->

</details>

### 5.6 US-UI-SCR42-ROLE-REQUIREMENTS — تحرير متطلبات الدور ونسخها واعتمادها

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

<!-- BEGIN GENERATED: refs US-UI-SCR42-ROLE-REQUIREMENTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-42 | شاشة التأهيل والأهلية |
| حالة الاستخدام | UC-102 | Check Eligibility |
| المصدر | `17-security-design.md §12.4` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR42-ROLE-REQUIREMENTS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RES-013 | The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications,… | `US-BC05-RRQ-ACTIVATE`، `US-BC05-RRQ-DEFINE`، `US-BC05-RRQ-EDIT`، `US-BC05-RRQ-RETIRE`، `US-DOM-RRQ-LIST` | TST-ROLE-REQUIREMENT-SM، TST-SLC09-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
