---
id: FEAT-ORG-STRUCTURE
type: feature
title: "الهيكل التنظيمي"
status: DRAFT
version: "0.1"
capability: CAP-01.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# الهيكل التنظيمي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-STRUCTURE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.01 إدارة المستأجرين والمؤسسات (R1) |
| الأدوار | مسؤول الإدارة؛ أي مستخدم مخوَّل |
| الشاشات | SCR-61 شجرة المؤسسة |
| حالات الاستخدام | UC-081 |
| القصص | 12: 9 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمسؤول بناء المؤسسة ووحداتها التنظيمية وتعديلها، ويمكّن كل مستخدم من رؤية شجرة المؤسسة.

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
| `US-BC01-ORG-ADD-UNIT` | إضافة وحدة تنظيمية إلى المؤسسة | أمر | مسودة |
| `US-BC01-ORG-CREATE` | إنشاء المؤسسة | أمر | مسودة |
| `US-BC01-ORG-DEACTIVATE` | إيقاف تفعيل المؤسسة | أمر | مسودة |
| `US-BC01-ORG-DEACTIVATE-UNIT` | إيقاف وحدة تنظيمية في المؤسسة | أمر | مسودة |
| `US-BC01-ORG-MOVE-UNIT` | نقل وحدة تنظيمية في المؤسسة | أمر | مسودة |
| `US-BC01-ORG-REACTIVATE` | إعادة تفعيل المؤسسة | أمر | مسودة |
| `US-BC01-ORG-RENAME` | إعادة تسمية المؤسسة | أمر | مسودة |
| `US-BC01-ORG-RENAME-UNIT` | إعادة تسمية وحدة تنظيمية في المؤسسة | أمر | مسودة |
| `US-BC01-Q-ORG-TREE` | جلب: Unit tree (cursor pagination on flattened order) | جلب | مسودة |
| `US-UI-SCR61-TREE-NAVIGATION` | تصفح شجرة المؤسسة متعددة المستويات | واجهة | مسودة |
| `US-UI-SCR61-UNIT-ACTIONS` | نقل الوحدات وتعديلها من الشجرة | واجهة | مسودة |
| `US-PLT-ORG-SCOPE-RESOLUTION` | حساب النطاق التنظيمي لصلاحيات الأدوار | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-ORG-ADD-UNIT — إضافة وحدة تنظيمية إلى المؤسسة

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

<!-- BEGIN GENERATED: refs US-BC01-ORG-ADD-UNIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/organizations/{id}/actions/add-unit` | — |
| الأمر | `CMD-ORG-ADD-UNIT` | إضافة وحدة تنظيمية إلى المؤسسة |
| السياسة | `POL-ORG-ADD-UNIT` | Administrator with org scope ⊇ target؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by… |
| الحدث | `EVT-ORG-UNIT-ADDED` | يصل إلى: Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| الكيان | `AGG-ORGANIZATION` | المؤسسة |
| الجدول | `foundation.organizations` | الجدول الرئيسي للمؤسسة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الاختبار | TST-ORGANIZATION-SM، TST-SLC01-INVARIANTS | دورة حالات المؤسسة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ORG-ADD-UNIT -->

</details>

### 5.2 US-BC01-ORG-CREATE — إنشاء المؤسسة

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

<!-- BEGIN GENERATED: refs US-BC01-ORG-CREATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/organizations` | — |
| الأمر | `CMD-ORG-CREATE` | إنشاء المؤسسة |
| السياسة | `POL-ORG-CREATE` | Administrator with org scope ⊇ target؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by… |
| الحدث | `EVT-ORG-CREATED` | يصل إلى: Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| الكيان | `AGG-ORGANIZATION` | المؤسسة |
| الجدول | `foundation.organizations` | الجدول الرئيسي للمؤسسة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الاختبار | TST-ORGANIZATION-SM، TST-SLC01-INVARIANTS | دورة حالات المؤسسة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ORG-CREATE -->

</details>

### 5.3 US-BC01-ORG-DEACTIVATE — إيقاف تفعيل المؤسسة

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

<!-- BEGIN GENERATED: refs US-BC01-ORG-DEACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/organizations/{id}/actions/deactivate` | — |
| الأمر | `CMD-ORG-DEACTIVATE` | إيقاف تفعيل المؤسسة |
| السياسة | `POL-ORG-DEACTIVATE` | Administrator with org scope ⊇ target؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by… |
| الحدث | `EVT-ORG-DEACTIVATED` | يصل إلى: Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| الكيان | `AGG-ORGANIZATION` | المؤسسة |
| الجدول | `foundation.organizations` | الجدول الرئيسي للمؤسسة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الاختبار | TST-ORGANIZATION-SM، TST-SLC01-INVARIANTS | دورة حالات المؤسسة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ORG-DEACTIVATE -->

</details>

### 5.4 US-BC01-ORG-DEACTIVATE-UNIT — إيقاف وحدة تنظيمية في المؤسسة

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

<!-- BEGIN GENERATED: refs US-BC01-ORG-DEACTIVATE-UNIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/organizations/{id}/actions/deactivate-unit` | — |
| الأمر | `CMD-ORG-DEACTIVATE-UNIT` | إيقاف وحدة تنظيمية في المؤسسة |
| السياسة | `POL-ORG-DEACTIVATE-UNIT` | Administrator with org scope ⊇ target؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by… |
| الحدث | `EVT-ORG-UNIT-DEACTIVATED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-ORGANIZATION` | المؤسسة |
| الجدول | `foundation.organizations` | الجدول الرئيسي للمؤسسة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الاختبار | TST-ORGANIZATION-SM، TST-SLC01-INVARIANTS | دورة حالات المؤسسة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ORG-DEACTIVATE-UNIT -->

</details>

### 5.5 US-BC01-ORG-MOVE-UNIT — نقل وحدة تنظيمية في المؤسسة

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

<!-- BEGIN GENERATED: refs US-BC01-ORG-MOVE-UNIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/organizations/{id}/actions/move-unit` | — |
| الأمر | `CMD-ORG-MOVE-UNIT` | نقل وحدة تنظيمية في المؤسسة |
| السياسة | `POL-ORG-MOVE-UNIT` | Administrator with org scope ⊇ target؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by… |
| الحدث | `EVT-ORG-UNIT-MOVED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-ORGANIZATION` | المؤسسة |
| الجدول | `foundation.organizations` | الجدول الرئيسي للمؤسسة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الاختبار | TST-ORGANIZATION-SM، TST-SLC01-INVARIANTS | دورة حالات المؤسسة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ORG-MOVE-UNIT -->

</details>

### 5.6 US-BC01-ORG-REACTIVATE — إعادة تفعيل المؤسسة

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

<!-- BEGIN GENERATED: refs US-BC01-ORG-REACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/organizations/{id}/actions/reactivate` | — |
| الأمر | `CMD-ORG-REACTIVATE` | إعادة تفعيل المؤسسة |
| السياسة | `POL-ORG-REACTIVATE` | Administrator with org scope ⊇ target؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by… |
| الحدث | `EVT-ORG-REACTIVATED` | يصل إلى: Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| الكيان | `AGG-ORGANIZATION` | المؤسسة |
| الجدول | `foundation.organizations` | الجدول الرئيسي للمؤسسة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الاختبار | TST-ORGANIZATION-SM، TST-SLC01-INVARIANTS | دورة حالات المؤسسة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ORG-REACTIVATE -->

</details>

### 5.7 US-BC01-ORG-RENAME — إعادة تسمية المؤسسة

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

<!-- BEGIN GENERATED: refs US-BC01-ORG-RENAME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/organizations/{id}/actions/rename` | — |
| الأمر | `CMD-ORG-RENAME` | إعادة تسمية المؤسسة |
| السياسة | `POL-ORG-RENAME` | Administrator with org scope ⊇ target؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by… |
| الحدث | `EVT-ORG-RENAMED` | يصل إلى: Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| الكيان | `AGG-ORGANIZATION` | المؤسسة |
| الجدول | `foundation.organizations` | الجدول الرئيسي للمؤسسة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الاختبار | TST-ORGANIZATION-SM، TST-SLC01-INVARIANTS | دورة حالات المؤسسة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ORG-RENAME -->

</details>

### 5.8 US-BC01-ORG-RENAME-UNIT — إعادة تسمية وحدة تنظيمية في المؤسسة

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

<!-- BEGIN GENERATED: refs US-BC01-ORG-RENAME-UNIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/organizations/{id}/actions/rename-unit` | — |
| الأمر | `CMD-ORG-RENAME-UNIT` | إعادة تسمية وحدة تنظيمية في المؤسسة |
| السياسة | `POL-ORG-RENAME-UNIT` | Administrator with org scope ⊇ target؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by… |
| الحدث | `EVT-ORG-UNIT-RENAMED` | يصل إلى: Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| الكيان | `AGG-ORGANIZATION` | المؤسسة |
| الجدول | `foundation.organizations` | الجدول الرئيسي للمؤسسة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الاختبار | TST-ORGANIZATION-SM، TST-SLC01-INVARIANTS | دورة حالات المؤسسة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-ORG-RENAME-UNIT -->

</details>

### 5.9 US-BC01-Q-ORG-TREE — جلب: Unit tree (cursor pagination on flattened order)

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

<!-- BEGIN GENERATED: refs US-BC01-Q-ORG-TREE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/foundation/organizations/{org_id}/units` | — |
| الاستعلام | `QRY-ORG-TREE` | Unit tree (cursor pagination on flattened order) |
| السياسة | `POL-ORG-TREE` | org scope of subject roles ∩ classification rule |
| الكيان | `AGG-ORGANIZATION` | المؤسسة |
| الجدول | `foundation.organizations` | الجدول الرئيسي للمؤسسة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الاختبار | TST-ORGANIZATION-SM، TST-SLC01-INVARIANTS | دورة حالات المؤسسة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-Q-ORG-TREE -->

</details>

### 5.10 US-UI-SCR61-TREE-NAVIGATION — تصفح شجرة المؤسسة متعددة المستويات

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

<!-- BEGIN GENERATED: refs US-UI-SCR61-TREE-NAVIGATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الشاشة | SCR-61 | شاشة شجرة المؤسسة |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
<!-- END GENERATED: refs US-UI-SCR61-TREE-NAVIGATION -->

</details>

### 5.11 US-UI-SCR61-UNIT-ACTIONS — نقل الوحدات وتعديلها من الشجرة

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

<!-- BEGIN GENERATED: refs US-UI-SCR61-UNIT-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-081 | Manage Organization & Units |
| الشاشة | SCR-61 | شاشة شجرة المؤسسة |
| المصدر | `21-ui-design.md §6.3` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR61-UNIT-ACTIONS -->

</details>

### 5.12 US-PLT-ORG-SCOPE-RESOLUTION — حساب النطاق التنظيمي لصلاحيات الأدوار

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

<!-- BEGIN GENERATED: refs US-PLT-ORG-SCOPE-RESOLUTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §3.2` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… |
| حالة الاستخدام | UC-081 | Manage Organization & Units |
<!-- END GENERATED: refs US-PLT-ORG-SCOPE-RESOLUTION -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational… | `US-BC01-ORG-ADD-UNIT`، `US-BC01-ORG-CREATE`، `US-BC01-ORG-DEACTIVATE`، `US-BC01-ORG-DEACTIVATE-UNIT`، `US-BC01-ORG-MOVE-UNIT`، `US-BC01-ORG-REACTIVATE`، `US-BC01-ORG-RENAME`، `US-BC01-ORG-RENAME-UNIT`، `US-BC01-Q-ORG-TREE`، `US-PLT-ORG-SCOPE-RESOLUTION`، `US-UI-SCR61-TREE-NAVIGATION` | TST-ORGANIZATION-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
