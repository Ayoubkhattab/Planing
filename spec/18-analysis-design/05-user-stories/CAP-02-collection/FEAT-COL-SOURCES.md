---
id: FEAT-COL-SOURCES
type: feature
title: "سجل المصادر وموثوقيتها"
status: DRAFT
version: "0.1"
capability: CAP-02.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# سجل المصادر وموثوقيتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-SOURCES |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.02 إدارة المصادر (R1) |
| الأدوار | المحلل |
| الشاشات | SCR-22 الادعاء والدليل والمصدر |
| حالات الاستخدام | UC-004، UC-095 |
| القصص | 10: 7 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يحفظ لكل مصدر ملفه ونوعه وتقدير موثوقيته عبر الزمن ويتيح تعليقه أو إحالته إلى التقاعد.

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
| `US-BC02-SRC-RATE-RELIABILITY` | تقدير موثوقية المصدر | أمر | مسودة |
| `US-BC02-SRC-REGISTER` | تسجيل المصدر | أمر | مسودة |
| `US-BC02-SRC-REINSTATE` | إعادة المصدر إلى السريان | أمر | مسودة |
| `US-BC02-SRC-RETIRE` | إحالة المصدر إلى التقاعد | أمر | مسودة |
| `US-BC02-SRC-SUSPEND` | تعليق المصدر | أمر | مسودة |
| `US-BC02-SRC-UPDATE-PROFILE` | تحديث ملف المصدر | أمر | مسودة |
| `US-BC02-Q-SRC-GET` | جلب: Source; identity only with source-protection permission | جلب | مسودة |
| `US-DOM-SRC-LIST` | عرض سجل المصادر وتصفيته | جلب | مسودة |
| `US-UI-SCR22-SOURCE-LIST` | تصفح المصادر حسب النوع والحالة والموثوقية | واجهة | مسودة |
| `US-UI-SCR22-SOURCE-PROFILE` | ملف المصدر وتاريخ تقديرات موثوقيته | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-SRC-RATE-RELIABILITY — تقدير موثوقية المصدر

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

<!-- BEGIN GENERATED: refs US-BC02-SRC-RATE-RELIABILITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/sources/{id}/actions/rate-reliability` | — |
| الأمر | `CMD-SRC-RATE-RELIABILITY` | تقدير موثوقية المصدر |
| السياسة | `POL-SRC-RATE-RELIABILITY` | Analyst (register, rate, profile) · Security Officer (protection, reclassify)؛ tenant match; object visible t… |
| الحدث | `EVT-SRC-RELIABILITY-RATED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-SOURCE` | المصدر |
| الجدول | `information.sources` | الجدول الرئيسي للمصدر |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالات الاستخدام | UC-004، UC-095 | Manage Source؛ Rate Source Reliability |
| الاختبار | TST-SOURCE-SM، TST-SLC02-INVARIANTS | دورة حالات المصدر، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-SRC-RATE-RELIABILITY -->

</details>

### 5.2 US-BC02-SRC-REGISTER — تسجيل المصدر

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

<!-- BEGIN GENERATED: refs US-BC02-SRC-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/sources` | — |
| الأمر | `CMD-SRC-REGISTER` | تسجيل المصدر |
| السياسة | `POL-SRC-REGISTER` | Analyst (register, rate, profile) · Security Officer (protection, reclassify)؛ tenant match; object visible t… |
| الحدث | `EVT-SRC-REGISTERED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-SOURCE` | المصدر |
| الجدول | `information.sources` | الجدول الرئيسي للمصدر |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالات الاستخدام | UC-004، UC-095 | Manage Source؛ Rate Source Reliability |
| الاختبار | TST-SOURCE-SM، TST-SLC02-INVARIANTS | دورة حالات المصدر، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-SRC-REGISTER -->

</details>

### 5.3 US-BC02-SRC-REINSTATE — إعادة المصدر إلى السريان

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

<!-- BEGIN GENERATED: refs US-BC02-SRC-REINSTATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/sources/{id}/actions/reinstate` | — |
| الأمر | `CMD-SRC-REINSTATE` | إعادة المصدر إلى السريان |
| السياسة | `POL-SRC-REINSTATE` | Analyst (reinstate)؛ tenant match; object visible to subject (label ≤ clearance); write permission in org sco… |
| الحدث | `EVT-SRC-REINSTATED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-SOURCE` | المصدر |
| الجدول | `information.sources` | الجدول الرئيسي للمصدر |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالات الاستخدام | UC-004، UC-095 | Manage Source؛ Rate Source Reliability |
| الاختبار | TST-SOURCE-SM، TST-SLC02-INVARIANTS | دورة حالات المصدر، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-SRC-REINSTATE -->

</details>

### 5.4 US-BC02-SRC-RETIRE — إحالة المصدر إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC02-SRC-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/sources/{id}/actions/retire` | — |
| الأمر | `CMD-SRC-RETIRE` | إحالة المصدر إلى التقاعد |
| السياسة | `POL-SRC-RETIRE` | Analyst (retire)؛ tenant match; object visible to subject (label ≤ clearance); write permission in org scope |
| الحدث | `EVT-SRC-RETIRED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-SOURCE` | المصدر |
| الجدول | `information.sources` | الجدول الرئيسي للمصدر |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالات الاستخدام | UC-004، UC-095 | Manage Source؛ Rate Source Reliability |
| الاختبار | TST-SOURCE-SM، TST-SLC02-INVARIANTS | دورة حالات المصدر، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-SRC-RETIRE -->

</details>

### 5.5 US-BC02-SRC-SUSPEND — تعليق المصدر

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

<!-- BEGIN GENERATED: refs US-BC02-SRC-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/sources/{id}/actions/suspend` | — |
| الأمر | `CMD-SRC-SUSPEND` | تعليق المصدر |
| السياسة | `POL-SRC-SUSPEND` | Analyst (suspend)؛ tenant match; object visible to subject (label ≤ clearance); write permission in org scope |
| الحدث | `EVT-SRC-SUSPENDED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-SOURCE` | المصدر |
| الجدول | `information.sources` | الجدول الرئيسي للمصدر |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالات الاستخدام | UC-004، UC-095 | Manage Source؛ Rate Source Reliability |
| الاختبار | TST-SOURCE-SM، TST-SLC02-INVARIANTS | دورة حالات المصدر، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-SRC-SUSPEND -->

</details>

### 5.6 US-BC02-SRC-UPDATE-PROFILE — تحديث ملف المصدر

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

<!-- BEGIN GENERATED: refs US-BC02-SRC-UPDATE-PROFILE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/sources/{id}/actions/update-profile` | — |
| الأمر | `CMD-SRC-UPDATE-PROFILE` | تحديث ملف المصدر |
| السياسة | `POL-SRC-UPDATE-PROFILE` | Analyst (register, rate, profile) · Security Officer (protection, reclassify)؛ tenant match; object visible t… |
| الحدث | `EVT-SRC-PROFILE-UPDATED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-SOURCE` | المصدر |
| الجدول | `information.sources` | الجدول الرئيسي للمصدر |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالات الاستخدام | UC-004، UC-095 | Manage Source؛ Rate Source Reliability |
| الاختبار | TST-SOURCE-SM، TST-SLC02-INVARIANTS | دورة حالات المصدر، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-SRC-UPDATE-PROFILE -->

</details>

### 5.7 US-BC02-Q-SRC-GET — جلب: Source; identity only with source-protection permission

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

<!-- BEGIN GENERATED: refs US-BC02-Q-SRC-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/sources/{source_id}` | — |
| الاستعلام | `QRY-SRC-GET` | Source; identity only with source-protection permission |
| السياسة | `POL-SRC-GET` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-SOURCE` | المصدر |
| الجدول | `information.sources` | الجدول الرئيسي للمصدر |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالات الاستخدام | UC-004، UC-095 | Manage Source؛ Rate Source Reliability |
| الاختبار | TST-SOURCE-SM، TST-SLC02-INVARIANTS | دورة حالات المصدر، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-SRC-GET -->

</details>

### 5.8 US-DOM-SRC-LIST — عرض سجل المصادر وتصفيته

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

<!-- BEGIN GENERATED: refs US-DOM-SRC-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-004 | Manage Source |
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالات الاستخدام | UC-004، UC-095 | Manage Source؛ Rate Source Reliability |
<!-- END GENERATED: refs US-DOM-SRC-LIST -->

</details>

### 5.9 US-UI-SCR22-SOURCE-LIST — تصفح المصادر حسب النوع والحالة والموثوقية

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

<!-- BEGIN GENERATED: refs US-UI-SCR22-SOURCE-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| المصدر | `21-ui-design.md §6.1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالات الاستخدام | UC-004، UC-095 | Manage Source؛ Rate Source Reliability |
<!-- END GENERATED: refs US-UI-SCR22-SOURCE-LIST -->

</details>

### 5.10 US-UI-SCR22-SOURCE-PROFILE — ملف المصدر وتاريخ تقديرات موثوقيته

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

<!-- BEGIN GENERATED: refs US-UI-SCR22-SOURCE-PROFILE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| حالة الاستخدام | UC-095 | Rate Source Reliability |
| المصدر | `21-ui-design.md §6.3` | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالات الاستخدام | UC-004، UC-095 | Manage Source؛ Rate Source Reliability |
<!-- END GENERATED: refs US-UI-SCR22-SOURCE-PROFILE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… | `US-BC02-Q-SRC-GET`، `US-BC02-SRC-RATE-RELIABILITY`، `US-BC02-SRC-REGISTER`، `US-BC02-SRC-REINSTATE`، `US-BC02-SRC-RETIRE`، `US-BC02-SRC-SUSPEND`، `US-BC02-SRC-UPDATE-PROFILE`، `US-DOM-SRC-LIST`، `US-UI-SCR22-SOURCE-LIST`، `US-UI-SCR22-SOURCE-PROFILE` | TST-SLC02-INVARIANTS، TST-SOURCE-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
