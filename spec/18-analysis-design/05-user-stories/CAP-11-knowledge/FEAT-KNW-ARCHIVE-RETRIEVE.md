---
id: FEAT-KNW-ARCHIVE-RETRIEVE
type: feature
title: "استرجاع السجلات التاريخية"
status: DRAFT
version: "0.1"
capability: CAP-11.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# استرجاع السجلات التاريخية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-KNW-ARCHIVE-RETRIEVE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-11 المعرفة والذاكرة المؤسسية |
| القدرة الفرعية | CAP-11.03 الأرشيف وإعادة البناء التاريخي (R2) |
| الأدوار | أي مستخدم مخوَّل؛ أمين الأرشيف |
| الشاشات | SCR-44 المعرفة والأرشيف |
| حالات الاستخدام | UC-064 |
| القصص | 7: 2 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يمكّن المستخدم المخوَّل من البحث في فهرس الأرشيف واسترجاع سجل تاريخي ضمن الوقت المستهدف مع تسجيل كل وصول.

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
| QAS-ARC-001 | retrieve an archived record | ≤ 1 min for warm, ≤ 24 h for cold/offline media |
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
| `US-BC06-Q-ARC-RETRIEVE` | جلب: Retrieve package content (warm: signed grant; cold: staged job) — access logged | جلب | مسودة |
| `US-BC06-Q-ARC-SEARCH` | جلب: Archive catalogue (metadata only) by class, period, org | جلب | مسودة |
| `US-UI-SCR44-ARCHIVE-SEARCH` | البحث في فهرس الأرشيف ومعرفة زمن الاسترجاع | واجهة | مسودة |
| `US-UI-SCR44-COLD-RETRIEVAL` | متابعة طلب استرجاع من الأرشيف البارد | واجهة | مسودة |
| `US-PLT-ARCHIVE-COLD-STAGE` | تجهيز السجل البارد خلال 24 ساعة | منصة | مسودة |
| `US-PLT-ARCHIVE-WARM-RETRIEVE` | استرجاع السجل الدافئ خلال دقيقة | منصة | مسودة |
| `US-OPS-ARCHIVE-RETRIEVAL-SLO` | مراقبة زمن استرجاع الأرشيف لكل طبقة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC06-Q-ARC-RETRIEVE — جلب: Retrieve package content (warm: signed grant; cold: staged job) — access logged

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-Q-ARC-RETRIEVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/archive-packages/{package_id}/retrievals` | — |
| الاستعلام | `QRY-ARC-RETRIEVE` | Retrieve package content (warm: signed grant; cold: staged job) — access logged |
| السياسة | `POL-ARC-RETRIEVE` | authorized by package label and purpose |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-ARC-003 | When an authorized user requests a historical record, the system shall retrieve it within the archive retriev… |
| حالة الاستخدام | UC-064 | Retrieve Historical Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-Q-ARC-RETRIEVE -->

</details>

### 5.2 US-BC06-Q-ARC-SEARCH — جلب: Archive catalogue (metadata only) by class, period, org

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-Q-ARC-SEARCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/knowledge/archive-packages` | — |
| الاستعلام | `QRY-ARC-SEARCH` | Archive catalogue (metadata only) by class, period, org |
| السياسة | `POL-ARC-SEARCH` | Archivist; label rule |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-ARC-003 | When an authorized user requests a historical record, the system shall retrieve it within the archive retriev… |
| حالة الاستخدام | UC-064 | Retrieve Historical Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-Q-ARC-SEARCH -->

</details>

### 5.3 US-UI-SCR44-ARCHIVE-SEARCH — البحث في فهرس الأرشيف ومعرفة زمن الاسترجاع

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR44-ARCHIVE-SEARCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-064 | Retrieve Historical Record |
| الشاشة | SCR-44 | شاشة المعرفة والأرشيف |
| الجودة | QAS-ARC-001 | retrieve an archived record → ≤ 1 min for warm, ≤ 24 h for cold/offline media |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ARC-003 | When an authorized user requests a historical record, the system shall retrieve it within the archive retriev… |
| حالة الاستخدام | UC-064 | Retrieve Historical Record |
<!-- END GENERATED: refs US-UI-SCR44-ARCHIVE-SEARCH -->

</details>

### 5.4 US-UI-SCR44-COLD-RETRIEVAL — متابعة طلب استرجاع من الأرشيف البارد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR44-COLD-RETRIEVAL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-ARC-001 | retrieve an archived record → ≤ 1 min for warm, ≤ 24 h for cold/offline media |
| المصدر | `09-reliability/fmea-slc12.md FM-S12-P2` | — |
| الشاشة | SCR-44 | شاشة المعرفة والأرشيف |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ARC-003 | When an authorized user requests a historical record, the system shall retrieve it within the archive retriev… |
| حالة الاستخدام | UC-064 | Retrieve Historical Record |
<!-- END GENERATED: refs US-UI-SCR44-COLD-RETRIEVAL -->

</details>

### 5.5 US-PLT-ARCHIVE-COLD-STAGE — تجهيز السجل البارد خلال 24 ساعة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-ARCHIVE-COLD-STAGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-ARC-001 | retrieve an archived record → ≤ 1 min for warm, ≤ 24 h for cold/offline media |
| المصدر | `09-reliability/fmea-slc12.md FM-S12-P2` | — |
| المتطلب | REQ-ARC-003 | When an authorized user requests a historical record, the system shall retrieve it within the archive retriev… |
| حالة الاستخدام | UC-064 | Retrieve Historical Record |
<!-- END GENERATED: refs US-PLT-ARCHIVE-COLD-STAGE -->

</details>

### 5.6 US-PLT-ARCHIVE-WARM-RETRIEVE — استرجاع السجل الدافئ خلال دقيقة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-ARCHIVE-WARM-RETRIEVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-ARC-001 | retrieve an archived record → ≤ 1 min for warm, ≤ 24 h for cold/offline media |
| المصدر | `US-BC06-Q-ARC-RETRIEVE` | — |
| المتطلب | REQ-ARC-003 | When an authorized user requests a historical record, the system shall retrieve it within the archive retriev… |
| حالة الاستخدام | UC-064 | Retrieve Historical Record |
<!-- END GENERATED: refs US-PLT-ARCHIVE-WARM-RETRIEVE -->

</details>

### 5.7 US-OPS-ARCHIVE-RETRIEVAL-SLO — مراقبة زمن استرجاع الأرشيف لكل طبقة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R2 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-ARCHIVE-RETRIEVAL-SLO -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-ARC-001 | retrieve an archived record → ≤ 1 min for warm, ≤ 24 h for cold/offline media |
| المصدر | `09-reliability/observability-slc12.md` | — |
<!-- END GENERATED: refs US-OPS-ARCHIVE-RETRIEVAL-SLO -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-ARC-003 | When an authorized user requests a historical record, the system shall retrieve it within the archive retriev… | `US-BC06-Q-ARC-RETRIEVE`، `US-BC06-Q-ARC-SEARCH`، `US-PLT-ARCHIVE-COLD-STAGE`، `US-PLT-ARCHIVE-WARM-RETRIEVE`، `US-UI-SCR44-ARCHIVE-SEARCH`، `US-UI-SCR44-COLD-RETRIEVAL` | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
