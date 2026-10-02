---
id: FEAT-ORG-ROLES
type: feature
title: "تعريف الأدوار وصلاحياتها"
status: DRAFT
version: "0.1"
capability: CAP-01.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تعريف الأدوار وصلاحياتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-ROLES |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.04 سياسات الوصول (R1) |
| الأدوار | مسؤول الإدارة |
| الشاشات | SCR-62 المستخدمون والأدوار والسلطة |
| حالات الاستخدام | UC-086 |
| القصص | 6: 4 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمسؤول تعريف أدوار العمل وتحديد ما يسمح به كل دور من عرض وتعديل وتصدير واعتماد، وتفعيل الأدوار أو إحالتها للتقاعد.

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
| `US-BC01-ROL-ACTIVATE` | تفعيل الدور | أمر | مسودة |
| `US-BC01-ROL-DEFINE` | تعريف الدور | أمر | مسودة |
| `US-BC01-ROL-RETIRE` | إحالة الدور إلى التقاعد | أمر | مسودة |
| `US-BC01-ROL-SET-PERMISSIONS` | تحديد صلاحيات الدور | أمر | مسودة |
| `US-DOM-ROL-LIST` | عرض الأدوار وصلاحياتها | جلب | مسودة |
| `US-UI-SCR62-PERMISSION-MATRIX` | ضبط الصلاحيات الثماني للدور منفصلة | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-ROL-ACTIVATE — تفعيل الدور

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

<!-- BEGIN GENERATED: refs US-BC01-ROL-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/roles/{id}/actions/activate` | — |
| الأمر | `CMD-ROL-ACTIVATE` | تفعيل الدور |
| السياسة | `POL-ROL-ACTIVATE` | Administrator (tenant-wide)؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-ROL-ACTIVATED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-ROLE` | الدور |
| الجدول | `foundation.roles` | الجدول الرئيسي للدور |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-014 | The system shall treat View, Edit, Export, Share, Approve, Delete, Retain and Archive as separately grantable… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-ROLE-SM، TST-SLC01-INVARIANTS | دورة حالات الدور، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ROL-ACTIVATE -->

</details>

### 5.2 US-BC01-ROL-DEFINE — تعريف الدور

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

<!-- BEGIN GENERATED: refs US-BC01-ROL-DEFINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/roles` | — |
| الأمر | `CMD-ROL-DEFINE` | تعريف الدور |
| السياسة | `POL-ROL-DEFINE` | Administrator (tenant-wide)؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-ROL-DEFINED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-ROLE` | الدور |
| الجدول | `foundation.roles` | الجدول الرئيسي للدور |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-014 | The system shall treat View, Edit, Export, Share, Approve, Delete, Retain and Archive as separately grantable… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-ROLE-SM، TST-SLC01-INVARIANTS | دورة حالات الدور، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ROL-DEFINE -->

</details>

### 5.3 US-BC01-ROL-RETIRE — إحالة الدور إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC01-ROL-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/roles/{id}/actions/retire` | — |
| الأمر | `CMD-ROL-RETIRE` | إحالة الدور إلى التقاعد |
| السياسة | `POL-ROL-RETIRE` | Administrator (tenant-wide)؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-ROL-RETIRED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-ROLE` | الدور |
| الجدول | `foundation.roles` | الجدول الرئيسي للدور |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-014 | The system shall treat View, Edit, Export, Share, Approve, Delete, Retain and Archive as separately grantable… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-ROLE-SM، TST-SLC01-INVARIANTS | دورة حالات الدور، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ROL-RETIRE -->

</details>

### 5.4 US-BC01-ROL-SET-PERMISSIONS — تحديد صلاحيات الدور

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

<!-- BEGIN GENERATED: refs US-BC01-ROL-SET-PERMISSIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/roles/{id}/actions/set-permissions` | — |
| الأمر | `CMD-ROL-SET-PERMISSIONS` | تحديد صلاحيات الدور |
| السياسة | `POL-ROL-SET-PERMISSIONS` | Administrator (tenant-wide)؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-ROL-PERMISSIONS-CHANGED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-ROLE` | الدور |
| الجدول | `foundation.roles` | الجدول الرئيسي للدور |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-014 | The system shall treat View, Edit, Export, Share, Approve, Delete, Retain and Archive as separately grantable… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-ROLE-SM، TST-SLC01-INVARIANTS | دورة حالات الدور، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ROL-SET-PERMISSIONS -->

</details>

### 5.5 US-DOM-ROL-LIST — عرض الأدوار وصلاحياتها

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

<!-- BEGIN GENERATED: refs US-DOM-ROL-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-014 | The system shall treat View, Edit, Export, Share, Approve, Delete, Retain and Archive as separately grantable… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
<!-- END GENERATED: refs US-DOM-ROL-LIST -->

</details>

### 5.6 US-UI-SCR62-PERMISSION-MATRIX — ضبط الصلاحيات الثماني للدور منفصلة

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

<!-- BEGIN GENERATED: refs US-UI-SCR62-PERMISSION-MATRIX -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| المصدر | `17-security-design.md §12.2` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-014 | The system shall treat View, Edit, Export, Share, Approve, Delete, Retain and Archive as separately grantable… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
<!-- END GENERATED: refs US-UI-SCR62-PERMISSION-MATRIX -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-014 | The system shall treat View, Edit, Export, Share, Approve, Delete, Retain and Archive as separately grantable… | `US-BC01-ROL-ACTIVATE`، `US-BC01-ROL-DEFINE`، `US-BC01-ROL-RETIRE`، `US-BC01-ROL-SET-PERMISSIONS`، `US-DOM-ROL-LIST`، `US-UI-SCR62-PERMISSION-MATRIX` | TST-ROLE-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
