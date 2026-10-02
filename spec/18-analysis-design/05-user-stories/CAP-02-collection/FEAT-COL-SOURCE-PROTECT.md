---
id: FEAT-COL-SOURCE-PROTECT
type: feature
title: "حماية هوية المصادر"
status: DRAFT
version: "0.1"
capability: CAP-02.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# حماية هوية المصادر

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-SOURCE-PROTECT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.02 إدارة المصادر (R1) |
| الأدوار | مسؤول الأمن |
| الشاشات | SCR-22 الادعاء والدليل والمصدر |
| حالات الاستخدام | UC-004 |
| القصص | 4: 2 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لمسؤول الأمن تحديد مستوى حماية المصدر وتصنيفه بحيث لا يرى هويته إلا المخولون.

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
| المرجع | الموقف | المطلوب |
|---|---|---|
| QAS-SEC-009 | user without source-protection permission reads claims of a protected human source | 0 identity attributes disclosed in any response, export or lineage |
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
| `US-BC02-SRC-RECLASSIFY` | إعادة تصنيف المصدر | أمر | مسودة |
| `US-BC02-SRC-SET-PROTECTION` | تحديد مستوى حماية المصدر | أمر | مسودة |
| `US-UI-SCR22-SOURCE-REDACTED` | إخفاء هوية المصدر المحمي في الشاشة | واجهة | مسودة |
| `US-PLT-SRCPROT-NO-LEAK` | منع تسرب هوية المصدر المحمي من أي مسار | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-SRC-RECLASSIFY — إعادة تصنيف المصدر

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

<!-- BEGIN GENERATED: refs US-BC02-SRC-RECLASSIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/sources/{id}/actions/reclassify` | — |
| الأمر | `CMD-SRC-RECLASSIFY` | إعادة تصنيف المصدر |
| السياسة | `POL-SRC-RECLASSIFY` | Analyst (register, rate, profile) · Security Officer (protection, reclassify)؛ tenant match; object visible t… |
| الحدث | `EVT-SRC-RECLASSIFIED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-SOURCE` | المصدر |
| الجدول | `information.sources` | الجدول الرئيسي للمصدر |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالة الاستخدام | UC-004 | Manage Source |
| الاختبار | TST-SOURCE-SM، TST-SLC02-INVARIANTS | دورة حالات المصدر، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-SRC-RECLASSIFY -->

</details>

### 5.2 US-BC02-SRC-SET-PROTECTION — تحديد مستوى حماية المصدر

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

<!-- BEGIN GENERATED: refs US-BC02-SRC-SET-PROTECTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/sources/{id}/actions/set-protection` | — |
| الأمر | `CMD-SRC-SET-PROTECTION` | تحديد مستوى حماية المصدر |
| السياسة | `POL-SRC-SET-PROTECTION` | Analyst (register, rate, profile) · Security Officer (protection, reclassify)؛ tenant match; object visible t… |
| الحدث | `EVT-SRC-PROTECTION-CHANGED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-SOURCE` | المصدر |
| الجدول | `information.sources` | الجدول الرئيسي للمصدر |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… |
| حالة الاستخدام | UC-004 | Manage Source |
| الاختبار | TST-SOURCE-SM، TST-SLC02-INVARIANTS | دورة حالات المصدر، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-SRC-SET-PROTECTION -->

</details>

### 5.3 US-UI-SCR22-SOURCE-REDACTED — إخفاء هوية المصدر المحمي في الشاشة

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

<!-- BEGIN GENERATED: refs US-UI-SCR22-SOURCE-REDACTED -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| المصدر | `21-ui-design.md §11` | — |
| المصدر | `PB-08` | — |
| الجودة | QAS-SEC-009 | user without source-protection permission reads claims of a protected human source → 0 identity attributes di… |
<!-- END GENERATED: refs US-UI-SCR22-SOURCE-REDACTED -->

</details>

### 5.4 US-PLT-SRCPROT-NO-LEAK — منع تسرب هوية المصدر المحمي من أي مسار

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

<!-- BEGIN GENERATED: refs US-PLT-SRCPROT-NO-LEAK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-009 | user without source-protection permission reads claims of a protected human source → 0 identity attributes di… |
| المصدر | `THR-S02-02` | — |
| المصدر | `PB-08` | — |
| المصدر | `PB-11` | — |
| المصدر | `17-security-design.md §4` | — |
<!-- END GENERATED: refs US-PLT-SRCPROT-NO-LEAK -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the… | `US-BC02-SRC-RECLASSIFY`، `US-BC02-SRC-SET-PROTECTION` | TST-SLC02-INVARIANTS، TST-SOURCE-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
