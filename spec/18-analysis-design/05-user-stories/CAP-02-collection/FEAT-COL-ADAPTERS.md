---
id: FEAT-COL-ADAPTERS
type: feature
title: "إدارة محوّلات البيانات"
status: DRAFT
version: "0.1"
capability: CAP-02.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة محوّلات البيانات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-ADAPTERS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.04 الاستيعاب والتكامل (R1) |
| الأدوار | مسؤول الإدارة |
| الشاشات | SCR-65 المحوّلات والاتصالات والحساسات |
| حالات الاستخدام | UC-094 |
| القصص | 13: 7 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمسؤول تسجيل محوّلات البيانات الخارجية وربط حقولها وتفعيلها بموافقة مسؤول ثان.

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
| `US-BC07-ADP-ACTIVATE` | تفعيل المحوّل | أمر | مسودة |
| `US-BC07-ADP-REGISTER` | تسجيل المحوّل | أمر | مسودة |
| `US-BC07-ADP-RESUME` | استئناف المحوّل | أمر | مسودة |
| `US-BC07-ADP-RETIRE` | إحالة المحوّل إلى التقاعد | أمر | مسودة |
| `US-BC07-ADP-SUSPEND` | تعليق المحوّل | أمر | مسودة |
| `US-BC07-ADP-UPDATE-MAPPING` | تحديث ربط حقول المحوّل | أمر | مسودة |
| `US-BC07-Q-ADP-GET` | جلب: Adapter with mapping versions | جلب | مسودة |
| `US-DOM-ADP-LIST` | عرض المحوّلات المسجلة وحالاتها | جلب | مسودة |
| `US-UI-SCR65-ADAPTER-MAPPING` | مراجعة إصدارات الربط ونتائج اختبارها | واجهة | مسودة |
| `US-PLT-ADAPTER-MAPPING-TESTS` | تشغيل اختبارات الربط قبل التفعيل | منصة | مسودة |
| `US-INT-ADAPTER-RUNTIME` | سحب البيانات وترجمتها وتسليمها دفعات | تكامل | مسودة |
| `US-OPS-ADAPTER-CRED-ROTATION` | تدوير مفاتيح حسابات خدمة المحوّلات | تشغيل | مسودة |
| `US-OPS-ADAPTER-DEPLOY` | نشر كل محوّل بصورة موقّعة مستقلة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-ADP-ACTIVATE — تفعيل المحوّل

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

<!-- BEGIN GENERATED: refs US-BC07-ADP-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/adapters/{id}/actions/activate` | — |
| الأمر | `CMD-ADP-ACTIVATE` | تفعيل المحوّل |
| السياسة | `POL-ADP-ACTIVATE` | Administrator (register, update) · second Administrator (activate)؛ tenant match; object visible to subject (… |
| الحدث | `EVT-ADP-ACTIVATED` | يصل إلى: Import worker |
| الكيان | `AGG-ADAPTER` | المحوّل |
| الجدول | `integration.adapters` | الجدول الرئيسي للمحوّل |
| وحدة النشر | DU-11 | — |
| المتطلبات | REQ-INF-005، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-ADAPTER-SM، TST-SLC02-INVARIANTS | دورة حالات المحوّل، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC07-ADP-ACTIVATE -->

</details>

### 5.2 US-BC07-ADP-REGISTER — تسجيل المحوّل

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

<!-- BEGIN GENERATED: refs US-BC07-ADP-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/adapters` | — |
| الأمر | `CMD-ADP-REGISTER` | تسجيل المحوّل |
| السياسة | `POL-ADP-REGISTER` | Administrator (register, update) · second Administrator (activate)؛ tenant match; object visible to subject (… |
| الحدث | `EVT-ADP-REGISTERED` | يصل إلى: Import worker |
| الكيان | `AGG-ADAPTER` | المحوّل |
| الجدول | `integration.adapters` | الجدول الرئيسي للمحوّل |
| وحدة النشر | DU-11 | — |
| المتطلبات | REQ-INF-005، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-ADAPTER-SM، TST-SLC02-INVARIANTS | دورة حالات المحوّل، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC07-ADP-REGISTER -->

</details>

### 5.3 US-BC07-ADP-RESUME — استئناف المحوّل

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

<!-- BEGIN GENERATED: refs US-BC07-ADP-RESUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/adapters/{id}/actions/resume` | — |
| الأمر | `CMD-ADP-RESUME` | استئناف المحوّل |
| السياسة | `POL-ADP-RESUME` | second Administrator (resume)؛ tenant match; object visible to subject (label ≤ clearance); write permission… |
| الحدث | `EVT-ADP-RESUMED` | يصل إلى: Import worker |
| الكيان | `AGG-ADAPTER` | المحوّل |
| الجدول | `integration.adapters` | الجدول الرئيسي للمحوّل |
| وحدة النشر | DU-11 | — |
| المتطلبات | REQ-INF-005، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-ADAPTER-SM، TST-SLC02-INVARIANTS | دورة حالات المحوّل، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC07-ADP-RESUME -->

</details>

### 5.4 US-BC07-ADP-RETIRE — إحالة المحوّل إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC07-ADP-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/adapters/{id}/actions/retire` | — |
| الأمر | `CMD-ADP-RETIRE` | إحالة المحوّل إلى التقاعد |
| السياسة | `POL-ADP-RETIRE` | Administrator (retire)؛ tenant match; object visible to subject (label ≤ clearance); write permission in org… |
| الحدث | `EVT-ADP-RETIRED` | يصل إلى: Import worker |
| الكيان | `AGG-ADAPTER` | المحوّل |
| الجدول | `integration.adapters` | الجدول الرئيسي للمحوّل |
| وحدة النشر | DU-11 | — |
| المتطلبات | REQ-INF-005، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-ADAPTER-SM، TST-SLC02-INVARIANTS | دورة حالات المحوّل، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC07-ADP-RETIRE -->

</details>

### 5.5 US-BC07-ADP-SUSPEND — تعليق المحوّل

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

<!-- BEGIN GENERATED: refs US-BC07-ADP-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/adapters/{id}/actions/suspend` | — |
| الأمر | `CMD-ADP-SUSPEND` | تعليق المحوّل |
| السياسة | `POL-ADP-SUSPEND` | Administrator (suspend)؛ tenant match; object visible to subject (label ≤ clearance); write permission in org… |
| الحدث | `EVT-ADP-SUSPENDED` | يصل إلى: Import worker |
| الكيان | `AGG-ADAPTER` | المحوّل |
| الجدول | `integration.adapters` | الجدول الرئيسي للمحوّل |
| وحدة النشر | DU-11 | — |
| المتطلبات | REQ-INF-005، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-ADAPTER-SM، TST-SLC02-INVARIANTS | دورة حالات المحوّل، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC07-ADP-SUSPEND -->

</details>

### 5.6 US-BC07-ADP-UPDATE-MAPPING — تحديث ربط حقول المحوّل

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

<!-- BEGIN GENERATED: refs US-BC07-ADP-UPDATE-MAPPING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/adapters/{id}/actions/update-mapping` | — |
| الأمر | `CMD-ADP-UPDATE-MAPPING` | تحديث ربط حقول المحوّل |
| السياسة | `POL-ADP-UPDATE-MAPPING` | Administrator (register, update) · second Administrator (activate)؛ tenant match; object visible to subject (… |
| الحدث | `EVT-ADP-MAPPING-UPDATED` | يصل إلى: Import worker |
| الكيان | `AGG-ADAPTER` | المحوّل |
| الجدول | `integration.adapters` | الجدول الرئيسي للمحوّل |
| وحدة النشر | DU-11 | — |
| المتطلبات | REQ-INF-005، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-ADAPTER-SM، TST-SLC02-INVARIANTS | دورة حالات المحوّل، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC07-ADP-UPDATE-MAPPING -->

</details>

### 5.7 US-BC07-Q-ADP-GET — جلب: Adapter with mapping versions

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

<!-- BEGIN GENERATED: refs US-BC07-Q-ADP-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/integration/adapters/{adapter_id}` | — |
| الاستعلام | `QRY-ADP-GET` | Adapter with mapping versions |
| السياسة | `POL-ADP-GET` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-ADAPTER` | المحوّل |
| الجدول | `integration.adapters` | الجدول الرئيسي للمحوّل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INF-005 | The system shall ingest external data only through registered adapters or bulk import jobs that record source… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-ADAPTER-SM، TST-SLC02-INVARIANTS | دورة حالات المحوّل، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC07-Q-ADP-GET -->

</details>

### 5.8 US-DOM-ADP-LIST — عرض المحوّلات المسجلة وحالاتها

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

<!-- BEGIN GENERATED: refs US-DOM-ADP-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-65 | شاشة المحوّلات والاتصالات والحساسات |
| حالة الاستخدام | UC-094 | Ingest External Data |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-005 | The system shall ingest external data only through registered adapters or bulk import jobs that record source… |
| حالة الاستخدام | UC-094 | Ingest External Data |
<!-- END GENERATED: refs US-DOM-ADP-LIST -->

</details>

### 5.9 US-UI-SCR65-ADAPTER-MAPPING — مراجعة إصدارات الربط ونتائج اختبارها

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

<!-- BEGIN GENERATED: refs US-UI-SCR65-ADAPTER-MAPPING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-65 | شاشة المحوّلات والاتصالات والحساسات |
| المصدر | `AGG-ADAPTER` | — |
| المصدر | `21-ui-design.md §6.3` | — |
<!-- END GENERATED: refs US-UI-SCR65-ADAPTER-MAPPING -->

</details>

### 5.10 US-PLT-ADAPTER-MAPPING-TESTS — تشغيل اختبارات الربط قبل التفعيل

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

<!-- BEGIN GENERATED: refs US-PLT-ADAPTER-MAPPING-TESTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `AGG-ADAPTER` | — |
| فحص البنية | FIT-12 | No external network dependency at runtime or build (air-gapped) |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
<!-- END GENERATED: refs US-PLT-ADAPTER-MAPPING-TESTS -->

</details>

### 5.11 US-INT-ADAPTER-RUNTIME — سحب البيانات وترجمتها وتسليمها دفعات

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-ADAPTER-RUNTIME -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §3` | — |
| المصدر | `INV-ADP-01` | — |
| المصدر | `INV-ADP-02` | — |
| المتطلب | REQ-INF-005 | The system shall ingest external data only through registered adapters or bulk import jobs that record source… |
| حالة الاستخدام | UC-094 | Ingest External Data |
<!-- END GENERATED: refs US-INT-ADAPTER-RUNTIME -->

</details>

### 5.12 US-OPS-ADAPTER-CRED-ROTATION — تدوير مفاتيح حسابات خدمة المحوّلات

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

<!-- BEGIN GENERATED: refs US-OPS-ADAPTER-CRED-ROTATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §2` | — |
| المصدر | `THR-S01-11` | — |
| المصدر | `INV-CON-03` | — |
<!-- END GENERATED: refs US-OPS-ADAPTER-CRED-ROTATION -->

</details>

### 5.13 US-OPS-ADAPTER-DEPLOY — نشر كل محوّل بصورة موقّعة مستقلة

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

<!-- BEGIN GENERATED: refs US-OPS-ADAPTER-DEPLOY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md` | — |
| القرار التقني | TD-17 | Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps… |
| القرار التقني | TD-12 | Kubernetes Jobs with Kueue (fair sharing, per-tenant quotas); images from internal Harbor registry, signed (c… |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-ADAPTER-DEPLOY -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-005 | The system shall ingest external data only through registered adapters or bulk import jobs that record source… | `US-BC07-ADP-ACTIVATE`، `US-BC07-ADP-REGISTER`، `US-BC07-ADP-RESUME`، `US-BC07-ADP-RETIRE`، `US-BC07-ADP-SUSPEND`، `US-BC07-ADP-UPDATE-MAPPING`، `US-BC07-Q-ADP-GET`، `US-DOM-ADP-LIST`، `US-INT-ADAPTER-RUNTIME` | TST-ADAPTER-SM، TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS |
| REQ-INF-008 | The system shall import geospatial data via OGC API Features/Maps/Tiles, WMS/WFS, GeoJSON, GeoPackage, GeoTIF… | كل قصص الأوامر والنظام في الميزة (6) | TST-ADAPTER-SM، TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS |
| REQ-INF-009 | The system shall ingest weather data through an adapter and register the provider as a source. | كل قصص الأوامر والنظام في الميزة (6) | TST-ADAPTER-SM، TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS |
| REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… | `US-PLT-ADAPTER-MAPPING-TESTS` | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
