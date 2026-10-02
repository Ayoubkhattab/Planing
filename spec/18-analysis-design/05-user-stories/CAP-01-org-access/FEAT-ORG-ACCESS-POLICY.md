---
id: FEAT-ORG-ACCESS-POLICY
type: feature
title: "إدارة سياسات الوصول"
status: DRAFT
version: "0.1"
capability: CAP-01.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة سياسات الوصول

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-ACCESS-POLICY |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.04 سياسات الوصول (R1) |
| الأدوار | مسؤول الأمن؛ المدقِّق؛ النظام |
| الشاشات | SCR-68 سياسات الوصول |
| حالات الاستخدام | UC-086 |
| القصص | 13: 8 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لمسؤول الأمن صياغة قواعد الوصول واختبارها وتقديمها للاعتماد ثم تطبيقها من تاريخ سريان محدد مع حفظ كل نسخة.

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
| `US-BC08-POL-APPROVE` | اعتماد مجموعة السياسات | أمر | مسودة |
| `US-BC08-POL-DRAFT` | إعداد مسودة مجموعة السياسات | أمر | مسودة |
| `US-BC08-POL-EDIT` | تعديل مجموعة السياسات | أمر | مسودة |
| `US-BC08-POL-REJECT` | رفض مجموعة السياسات | أمر | مسودة |
| `US-BC08-POL-SUBMIT` | تقديم مجموعة السياسات | أمر | مسودة |
| `US-BC08-Q-POL-GET` | جلب: Policy set version with tables and tests | جلب | مسودة |
| `US-DOM-POL-HISTORY` | عرض تاريخ نسخ السياسات وأزمنة سريانها | جلب | مسودة |
| `US-BC08-S-POLICY-SET-01` | تلقائي: effective_from reached (مجموعة السياسات) | نظام | مسودة |
| `US-BC08-S-POLICY-SET-02` | تلقائي: successor activated (مجموعة السياسات) | نظام | مسودة |
| `US-UI-SCR68-POLICY-TESTS` | عرض جداول القرار ونتائج اختباراتها | واجهة | مسودة |
| `US-UI-SCR68-VERSION-COMPARE` | مقارنة نسخ السياسة وموعد سريانها | واجهة | مسودة |
| `US-PLT-POL-BUNDLE-DISTRIBUTION` | توزيع حزمة السياسات الموقعة على المقيّمين | منصة | مسودة |
| `US-OPS-POL-ATTRIBUTE-MATRIX` | اختبار أثر كل سمة على قرار الوصول | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC08-POL-APPROVE — اعتماد مجموعة السياسات

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

<!-- BEGIN GENERATED: refs US-BC08-POL-APPROVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/policy-sets/{id}/actions/approve` | — |
| الأمر | `CMD-POL-APPROVE` | اعتماد مجموعة السياسات |
| السياسة | `POL-POL-APPROVE` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-POL-APPROVED` | يصل إلى: Search/Directory projection (BC01 read model); PDP bundle distributor |
| الكيان | `AGG-POLICY-SET` | مجموعة السياسات |
| الجدول | `governance.policy_sets` | الجدول الرئيسي لمجموعة السياسات |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-FND-011، REQ-FND-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-POLICY-SET-SM، TST-SLC01-INVARIANTS | دورة حالات مجموعة السياسات، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-POL-APPROVE -->

</details>

### 5.2 US-BC08-POL-DRAFT — إعداد مسودة مجموعة السياسات

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

<!-- BEGIN GENERATED: refs US-BC08-POL-DRAFT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/policy-sets` | — |
| الأمر | `CMD-POL-DRAFT` | إعداد مسودة مجموعة السياسات |
| السياسة | `POL-POL-DRAFT` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-POL-DRAFTED` | يصل إلى: Search/Directory projection (BC01 read model); PDP bundle distributor |
| الكيان | `AGG-POLICY-SET` | مجموعة السياسات |
| الجدول | `governance.policy_sets` | الجدول الرئيسي لمجموعة السياسات |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-FND-011، REQ-FND-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-POLICY-SET-SM، TST-SLC01-INVARIANTS | دورة حالات مجموعة السياسات، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-POL-DRAFT -->

</details>

### 5.3 US-BC08-POL-EDIT — تعديل مجموعة السياسات

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

<!-- BEGIN GENERATED: refs US-BC08-POL-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/policy-sets/{id}/actions/edit` | — |
| الأمر | `CMD-POL-EDIT` | تعديل مجموعة السياسات |
| السياسة | `POL-POL-EDIT` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-POL-EDITED` | يصل إلى: Search/Directory projection (BC01 read model); PDP bundle distributor |
| الكيان | `AGG-POLICY-SET` | مجموعة السياسات |
| الجدول | `governance.policy_sets` | الجدول الرئيسي لمجموعة السياسات |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-FND-011، REQ-FND-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-POLICY-SET-SM، TST-SLC01-INVARIANTS | دورة حالات مجموعة السياسات، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-POL-EDIT -->

</details>

### 5.4 US-BC08-POL-REJECT — رفض مجموعة السياسات

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

<!-- BEGIN GENERATED: refs US-BC08-POL-REJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/policy-sets/{id}/actions/reject` | — |
| الأمر | `CMD-POL-REJECT` | رفض مجموعة السياسات |
| السياسة | `POL-POL-REJECT` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-POL-REJECTED` | يصل إلى: Search/Directory projection (BC01 read model); PDP bundle distributor |
| الكيان | `AGG-POLICY-SET` | مجموعة السياسات |
| الجدول | `governance.policy_sets` | الجدول الرئيسي لمجموعة السياسات |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-FND-011، REQ-FND-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-POLICY-SET-SM، TST-SLC01-INVARIANTS | دورة حالات مجموعة السياسات، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-POL-REJECT -->

</details>

### 5.5 US-BC08-POL-SUBMIT — تقديم مجموعة السياسات

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

<!-- BEGIN GENERATED: refs US-BC08-POL-SUBMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/policy-sets/{id}/actions/submit` | — |
| الأمر | `CMD-POL-SUBMIT` | تقديم مجموعة السياسات |
| السياسة | `POL-POL-SUBMIT` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-POL-SUBMITTED` | يصل إلى: Search/Directory projection (BC01 read model); PDP bundle distributor |
| الكيان | `AGG-POLICY-SET` | مجموعة السياسات |
| الجدول | `governance.policy_sets` | الجدول الرئيسي لمجموعة السياسات |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-FND-011، REQ-FND-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-POLICY-SET-SM، TST-SLC01-INVARIANTS | دورة حالات مجموعة السياسات، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-POL-SUBMIT -->

</details>

### 5.6 US-BC08-Q-POL-GET — جلب: Policy set version with tables and tests

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

<!-- BEGIN GENERATED: refs US-BC08-Q-POL-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/governance/policy-sets/{version_id}` | — |
| الاستعلام | `QRY-POL-GET` | Policy set version with tables and tests |
| السياسة | `POL-POL-GET` | org scope of subject roles ∩ classification rule |
| الكيان | `AGG-POLICY-SET` | مجموعة السياسات |
| الجدول | `governance.policy_sets` | الجدول الرئيسي لمجموعة السياسات |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-009 | The system shall version, audit and time-stamp every policy and configuration change and apply each change fr… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-POLICY-SET-SM، TST-SLC01-INVARIANTS | دورة حالات مجموعة السياسات، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-Q-POL-GET -->

</details>

### 5.7 US-DOM-POL-HISTORY — عرض تاريخ نسخ السياسات وأزمنة سريانها

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

<!-- BEGIN GENERATED: refs US-DOM-POL-HISTORY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-68 | شاشة سياسات الوصول |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-009 | The system shall version, audit and time-stamp every policy and configuration change and apply each change fr… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
<!-- END GENERATED: refs US-DOM-POL-HISTORY -->

</details>

### 5.8 US-BC08-S-POLICY-SET-01 — تلقائي: effective_from reached (مجموعة السياسات)

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

<!-- BEGIN GENERATED: refs US-BC08-S-POLICY-SET-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:effective_from reached` | scheduler; previous ACTIVE → SUPERSEDED |
| الانتقال | APPROVED ← ACTIVE | — |
| الحدث | `EVT-POL-ACTIVATED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-POLICY-SET` | مجموعة السياسات |
| الجدول | `governance.policy_sets` | الجدول الرئيسي لمجموعة السياسات |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-FND-011، REQ-FND-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-POLICY-SET-SM، TST-SLC01-INVARIANTS | دورة حالات مجموعة السياسات، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-S-POLICY-SET-01 -->

</details>

### 5.9 US-BC08-S-POLICY-SET-02 — تلقائي: successor activated (مجموعة السياسات)

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

<!-- BEGIN GENERATED: refs US-BC08-S-POLICY-SET-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:successor activated` | system |
| الانتقال | ACTIVE ← SUPERSEDED | — |
| الحدث | `EVT-POL-SUPERSEDED` | يصل إلى: Search/Directory projection (BC01 read model); PDP bundle distributor |
| الكيان | `AGG-POLICY-SET` | مجموعة السياسات |
| الجدول | `governance.policy_sets` | الجدول الرئيسي لمجموعة السياسات |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-FND-011، REQ-FND-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الاختبار | TST-POLICY-SET-SM، TST-SLC01-INVARIANTS | دورة حالات مجموعة السياسات، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-S-POLICY-SET-02 -->

</details>

### 5.10 US-UI-SCR68-POLICY-TESTS — عرض جداول القرار ونتائج اختباراتها

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

<!-- BEGIN GENERATED: refs US-UI-SCR68-POLICY-TESTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الشاشة | SCR-68 | شاشة سياسات الوصول |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-011 | The system shall base authorization decisions on subject, action, resource, purpose, context, classification,… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
<!-- END GENERATED: refs US-UI-SCR68-POLICY-TESTS -->

</details>

### 5.11 US-UI-SCR68-VERSION-COMPARE — مقارنة نسخ السياسة وموعد سريانها

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

<!-- BEGIN GENERATED: refs US-UI-SCR68-VERSION-COMPARE -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-086 | Manage Access Policy |
| الشاشة | SCR-68 | شاشة سياسات الوصول |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-009 | The system shall version, audit and time-stamp every policy and configuration change and apply each change fr… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
<!-- END GENERATED: refs US-UI-SCR68-VERSION-COMPARE -->

</details>

### 5.12 US-PLT-POL-BUNDLE-DISTRIBUTION — توزيع حزمة السياسات الموقعة على المقيّمين

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

<!-- BEGIN GENERATED: refs US-PLT-POL-BUNDLE-DISTRIBUTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-08 | Open Policy Agent: decision tables compiled to Rego; signed bundles; embedded evaluation (WASM/library) in ea… |
| القرار المعماري | ADR-P11 | Policy Engine & Representation |
| المصدر | `23-crosscutting.md §8` | — |
<!-- END GENERATED: refs US-PLT-POL-BUNDLE-DISTRIBUTION -->

</details>

### 5.13 US-OPS-POL-ATTRIBUTE-MATRIX — اختبار أثر كل سمة على قرار الوصول

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-POL-ATTRIBUTE-MATRIX -->
| البند | المعرّف | المعنى |
|---|---|---|
| المتطلبات | REQ-FND-011، REQ-FND-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-086 | Manage Access Policy |
<!-- END GENERATED: refs US-OPS-POL-ATTRIBUTE-MATRIX -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-011 | The system shall base authorization decisions on subject, action, resource, purpose, context, classification,… | `US-BC08-POL-APPROVE`، `US-BC08-POL-DRAFT`، `US-BC08-POL-EDIT`، `US-BC08-POL-REJECT`، `US-BC08-POL-SUBMIT`، `US-BC08-S-POLICY-SET-01`، `US-BC08-S-POLICY-SET-02`، `US-OPS-POL-ATTRIBUTE-MATRIX`، `US-UI-SCR68-POLICY-TESTS` | TST-POLICY-SET-SM، TST-ROLE-ASSIGNMENT-SM |
| REQ-FND-012 | The system shall return a policy decision of ALLOW, DENY, CONDITIONAL, REDACT, AGGREGATE or REQUIRE_APPROVAL,… | `US-BC08-POL-APPROVE`، `US-BC08-POL-DRAFT`، `US-BC08-POL-EDIT`، `US-BC08-POL-REJECT`، `US-BC08-POL-SUBMIT`، `US-BC08-S-POLICY-SET-01`، `US-BC08-S-POLICY-SET-02`، `US-OPS-POL-ATTRIBUTE-MATRIX` | TST-POLICY-SET-SM |
| REQ-GOV-009 | The system shall version, audit and time-stamp every policy and configuration change and apply each change fr… | `US-BC08-Q-POL-GET`، `US-DOM-POL-HISTORY`، `US-UI-SCR68-VERSION-COMPARE` | TST-CLASSIFICATION-SCHEME-SM، TST-POLICY-SET-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
