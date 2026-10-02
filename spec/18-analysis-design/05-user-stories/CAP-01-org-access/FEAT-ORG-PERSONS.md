---
id: FEAT-ORG-PERSONS
type: feature
title: "سجل الأشخاص"
status: DRAFT
version: "0.1"
capability: CAP-01.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# سجل الأشخاص

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-PERSONS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.02 الهوية والمصادقة والاتحاد (R1) |
| الأدوار | مسؤول الإدارة |
| الشاشات | SCR-62 المستخدمون والأدوار والسلطة |
| حالات الاستخدام | UC-084 |
| القصص | 7: 4 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمسؤول تسجيل الأشخاص العاملين في المؤسسة وتحديث بياناتهم وإيقافهم أو إعادتهم بشكل مستقل عن حساباتهم.

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
| `US-BC01-PER-DEACTIVATE` | إيقاف تفعيل الشخص | أمر | مسودة |
| `US-BC01-PER-REACTIVATE` | إعادة تفعيل الشخص | أمر | مسودة |
| `US-BC01-PER-REGISTER` | تسجيل الشخص | أمر | مسودة |
| `US-BC01-PER-UPDATE-DETAILS` | تحديث بيانات الشخص | أمر | مسودة |
| `US-DOM-PER-LIST` | عرض سجل الأشخاص والبحث فيه | جلب | مسودة |
| `US-UI-SCR62-PERSON-LINKS` | عرض الشخص وهوياته وحساباته المرتبطة | واجهة | مسودة |
| `US-INT-HRIS-PERSON-UPDATE` | تحديث بيانات الأشخاص من الموارد البشرية | تكامل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-PER-DEACTIVATE — إيقاف تفعيل الشخص

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

<!-- BEGIN GENERATED: refs US-BC01-PER-DEACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/persons/{id}/actions/deactivate` | — |
| الأمر | `CMD-PER-DEACTIVATE` | إيقاف تفعيل الشخص |
| السياسة | `POL-PER-DEACTIVATE` | Administrator with org scope ⊇ person's unit؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operati… |
| الحدث | `EVT-PER-DEACTIVATED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-PERSON` | الشخص |
| الجدول | `foundation.persons` | الجدول الرئيسي للشخص |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-PERSON-SM، TST-SLC01-INVARIANTS | دورة حالات الشخص، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-PER-DEACTIVATE -->

</details>

### 5.2 US-BC01-PER-REACTIVATE — إعادة تفعيل الشخص

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

<!-- BEGIN GENERATED: refs US-BC01-PER-REACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/persons/{id}/actions/reactivate` | — |
| الأمر | `CMD-PER-REACTIVATE` | إعادة تفعيل الشخص |
| السياسة | `POL-PER-REACTIVATE` | Administrator with org scope ⊇ person's unit؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operati… |
| الحدث | `EVT-PER-REACTIVATED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-PERSON` | الشخص |
| الجدول | `foundation.persons` | الجدول الرئيسي للشخص |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-PERSON-SM، TST-SLC01-INVARIANTS | دورة حالات الشخص، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-PER-REACTIVATE -->

</details>

### 5.3 US-BC01-PER-REGISTER — تسجيل الشخص

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

<!-- BEGIN GENERATED: refs US-BC01-PER-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/persons` | — |
| الأمر | `CMD-PER-REGISTER` | تسجيل الشخص |
| السياسة | `POL-PER-REGISTER` | Administrator with org scope ⊇ person's unit؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operati… |
| الحدث | `EVT-PER-REGISTERED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-PERSON` | الشخص |
| الجدول | `foundation.persons` | الجدول الرئيسي للشخص |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-PERSON-SM، TST-SLC01-INVARIANTS | دورة حالات الشخص، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-PER-REGISTER -->

</details>

### 5.4 US-BC01-PER-UPDATE-DETAILS — تحديث بيانات الشخص

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

<!-- BEGIN GENERATED: refs US-BC01-PER-UPDATE-DETAILS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/persons/{id}/actions/update-details` | — |
| الأمر | `CMD-PER-UPDATE-DETAILS` | تحديث بيانات الشخص |
| السياسة | `POL-PER-UPDATE-DETAILS` | Administrator with org scope ⊇ person's unit؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operati… |
| الحدث | `EVT-PER-DETAILS-UPDATED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-PERSON` | الشخص |
| الجدول | `foundation.persons` | الجدول الرئيسي للشخص |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-PERSON-SM، TST-SLC01-INVARIANTS | دورة حالات الشخص، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-PER-UPDATE-DETAILS -->

</details>

### 5.5 US-DOM-PER-LIST — عرض سجل الأشخاص والبحث فيه

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

<!-- BEGIN GENERATED: refs US-DOM-PER-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
<!-- END GENERATED: refs US-DOM-PER-LIST -->

</details>

### 5.6 US-UI-SCR62-PERSON-LINKS — عرض الشخص وهوياته وحساباته المرتبطة

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

<!-- BEGIN GENERATED: refs US-UI-SCR62-PERSON-LINKS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
<!-- END GENERATED: refs US-UI-SCR62-PERSON-LINKS -->

</details>

### 5.7 US-INT-HRIS-PERSON-UPDATE — تحديث بيانات الأشخاص من الموارد البشرية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-HRIS-PERSON-UPDATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §2` | — |
| المصدر | `20-integration-design.md §4` | — |
<!-- END GENERATED: refs US-INT-HRIS-PERSON-UPDATE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. | `US-BC01-PER-DEACTIVATE`، `US-BC01-PER-REACTIVATE`، `US-BC01-PER-REGISTER`، `US-BC01-PER-UPDATE-DETAILS`، `US-DOM-PER-LIST`، `US-UI-SCR62-PERSON-LINKS` | TST-PERSON-SM، TST-SERVICE-ACCOUNT-SM، TST-USER-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
