---
id: FEAT-ORG-ROLE-ASSIGNMENT
type: feature
title: "إسناد الأدوار للمستخدمين"
status: DRAFT
version: "0.1"
capability: CAP-01.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إسناد الأدوار للمستخدمين

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-ROLE-ASSIGNMENT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.04 سياسات الوصول (R1) |
| الأدوار | مسؤول الإدارة؛ النظام |
| الشاشات | SCR-62 المستخدمون والأدوار والسلطة |
| حالات الاستخدام | UC-086، UC-035، UC-044 |
| القصص | 4: 3 من المواصفة، و1 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمسؤول منح المستخدمين أدوارهم في نطاق محدد ولمدة محددة، وسحبها يدويًا أو تلقائيًا عند انتهاء مدتها.

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
| `US-BC01-RAS-ASSIGN` | تسجيل إسناد الدور | أمر | مسودة |
| `US-BC01-RAS-REVOKE` | سحب إسناد الدور | أمر | مسودة |
| `US-BC01-S-ROLE-ASSIGNMENT-01` | تلقائي: valid_to reached (إسناد الدور) | نظام | مسودة |
| `US-UI-SCR62-ROLE-ASSIGNMENTS` | إسناد الأدوار بنطاق ومدة ومتابعة انتهائها | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-RAS-ASSIGN — تسجيل إسناد الدور

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

<!-- BEGIN GENERATED: refs US-BC01-RAS-ASSIGN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/role-assignments` | — |
| الأمر | `CMD-RAS-ASSIGN` | تسجيل إسناد الدور |
| السياسة | `POL-RAS-ASSIGN` | Administrator with scope ⊇ assignment scope؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operatio… |
| الحدث | `EVT-RAS-ASSIGNED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-ROLE-ASSIGNMENT` | إسناد الدور |
| الجدول | `foundation.role_assignments` | الجدول الرئيسي لإسناد الدور |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-011 | The system shall base authorization decisions on subject, action, resource, purpose, context, classification,… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-ROLE-ASSIGNMENT-SM، TST-SLC01-INVARIANTS | دورة حالات إسناد الدور، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-RAS-ASSIGN -->

</details>

### 5.2 US-BC01-RAS-REVOKE — سحب إسناد الدور

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

<!-- BEGIN GENERATED: refs US-BC01-RAS-REVOKE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/role-assignments/{id}/actions/revoke` | — |
| الأمر | `CMD-RAS-REVOKE` | سحب إسناد الدور |
| السياسة | `POL-RAS-REVOKE` | Administrator with scope ⊇ assignment scope؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operatio… |
| الحدث | `EVT-RAS-REVOKED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-ROLE-ASSIGNMENT` | إسناد الدور |
| الجدول | `foundation.role_assignments` | الجدول الرئيسي لإسناد الدور |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-011 | The system shall base authorization decisions on subject, action, resource, purpose, context, classification,… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-ROLE-ASSIGNMENT-SM، TST-SLC01-INVARIANTS | دورة حالات إسناد الدور، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-RAS-REVOKE -->

</details>

### 5.3 US-BC01-S-ROLE-ASSIGNMENT-01 — تلقائي: valid_to reached (إسناد الدور)

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

<!-- BEGIN GENERATED: refs US-BC01-S-ROLE-ASSIGNMENT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:valid_to reached` | system scheduler |
| الانتقال | ACTIVE ← EXPIRED | — |
| الحدث | `EVT-RAS-EXPIRED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-ROLE-ASSIGNMENT` | إسناد الدور |
| الجدول | `foundation.role_assignments` | الجدول الرئيسي لإسناد الدور |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-011 | The system shall base authorization decisions on subject, action, resource, purpose, context, classification,… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-ROLE-ASSIGNMENT-SM، TST-SLC01-INVARIANTS | دورة حالات إسناد الدور، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-S-ROLE-ASSIGNMENT-01 -->

</details>

### 5.4 US-UI-SCR62-ROLE-ASSIGNMENTS — إسناد الأدوار بنطاق ومدة ومتابعة انتهائها

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

<!-- BEGIN GENERATED: refs US-UI-SCR62-ROLE-ASSIGNMENTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR62-ROLE-ASSIGNMENTS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-011 | The system shall base authorization decisions on subject, action, resource, purpose, context, classification,… | كل قصص الميزة المأخوذة من المواصفة (3) | TST-POLICY-SET-SM، TST-ROLE-ASSIGNMENT-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
