---
id: FEAT-KNW-ARCHIVE-PRESERVE
type: feature
title: "حفظ الأرشيف وسلامته"
status: DRAFT
version: "0.1"
capability: CAP-11.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# حفظ الأرشيف وسلامته

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-KNW-ARCHIVE-PRESERVE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-11 المعرفة والذاكرة المؤسسية |
| القدرة الفرعية | CAP-11.03 الأرشيف وإعادة البناء التاريخي (R2) |
| الأدوار | أمين الأرشيف؛ الجهة المحيلة؛ النظام |
| الشاشات | SCR-44 المعرفة والأرشيف |
| حالات الاستخدام | UC-063 |
| القصص | 15: 9 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضمن نقل السجلات المؤرشفة إلى حزم محفوظة بصيغ دائمة يُتحقق من سلامتها دوريًا وتُصلح أو تُرحَّل عند الحاجة.

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
| QAS-ARC-003 | yearly archive integrity verification | 0 unreported corruption; repair from replica |
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
| `US-BC06-ARC-MIGRATE-FORMAT` | ترحيل صيغة الحزمة الأرشيفية | أمر | مسودة |
| `US-BC06-ARC-REPAIR` | إصلاح الحزمة الأرشيفية | أمر | مسودة |
| `US-BC06-ARC-RETRY-INGEST` | إعادة محاولة استيعاب الحزمة الأرشيفية | أمر | مسودة |
| `US-BC06-ARC-TRANSFER` | نقل الحزمة الأرشيفية | أمر | مسودة |
| `US-BC06-S-ARCHIVE-PACKAGE-01` | تلقائي: disposition action ARCHIVE for a bucket or record set (الحزمة الأرشيفية) | نظام | مسودة |
| `US-BC06-S-ARCHIVE-PACKAGE-02` | تلقائي: package validated (الحزمة الأرشيفية) | نظام | مسودة |
| `US-BC06-S-ARCHIVE-PACKAGE-03` | تلقائي: validation failed (الحزمة الأرشيفية) | نظام | مسودة |
| `US-BC06-S-ARCHIVE-PACKAGE-04` | تلقائي: integrity check failed (الحزمة الأرشيفية) | نظام | مسودة |
| `US-BC06-S-ARCHIVE-PACKAGE-05` | تلقائي: disposition DESTROY executed for the package bucket (الحزمة الأرشيفية) | نظام | مسودة |
| `US-UI-SCR44-ARCHIVE-PACKAGE` | متابعة حالة الحزمة الأرشيفية وأحداث حفظها | واجهة | مسودة |
| `US-PLT-ARCHIVE-FIXITY-SCHEDULE` | التحقق الدوري من سلامة كل الحزم | منصة | مسودة |
| `US-PLT-ARCHIVE-PACKAGE-BUILD` | بناء الحزمة الأرشيفية بصيغ الحفظ الدائمة | منصة | مسودة |
| `US-PLT-ARCHIVE-WORM-REPLICA` | تخزين الأرشيف مقفلًا مع نسخة في موقع التعافي | منصة | مسودة |
| `US-INT-ARCHIVE-TRANSFER-EXPORT` | تسليم الحزمة إلى أرشيف مستلم بإيصال | تكامل | مسودة |
| `US-OPS-ARCHIVE-FIXITY-ALERT` | التنبيه الفوري لأي خلل في سلامة الأرشيف | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC06-ARC-MIGRATE-FORMAT — ترحيل صيغة الحزمة الأرشيفية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-ARC-MIGRATE-FORMAT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/archive-packages/{id}/actions/migrate-format` | — |
| الأمر | `CMD-ARC-MIGRATE-FORMAT` | ترحيل صيغة الحزمة الأرشيفية |
| السياسة | `POL-ARC-MIGRATE-FORMAT` | Archivist (retry, repair, migrate) · transfer authority (transfer)؛ tenant match; object visible |
| الحدث | `EVT-ARC-FORMAT-MIGRATED` | يصل إلى: Archive catalogue; Disposition (SLC-12a); Audit |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-ARC-001، REQ-ARC-002، REQ-ARC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-063 | Archive Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-ARC-MIGRATE-FORMAT -->

</details>

### 5.2 US-BC06-ARC-REPAIR — إصلاح الحزمة الأرشيفية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-ARC-REPAIR -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/archive-packages/{id}/actions/repair` | — |
| الأمر | `CMD-ARC-REPAIR` | إصلاح الحزمة الأرشيفية |
| السياسة | `POL-ARC-REPAIR` | Archivist (retry, repair, migrate) · transfer authority (transfer)؛ tenant match; object visible |
| الحدث | `EVT-ARC-REPAIRED` | يصل إلى: Archive catalogue; Disposition (SLC-12a); Audit |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-ARC-001، REQ-ARC-002، REQ-ARC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-063 | Archive Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-ARC-REPAIR -->

</details>

### 5.3 US-BC06-ARC-RETRY-INGEST — إعادة محاولة استيعاب الحزمة الأرشيفية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-ARC-RETRY-INGEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/archive-packages/{id}/actions/retry-ingest` | — |
| الأمر | `CMD-ARC-RETRY-INGEST` | إعادة محاولة استيعاب الحزمة الأرشيفية |
| السياسة | `POL-ARC-RETRY-INGEST` | Archivist (retry, repair, migrate) · transfer authority (transfer)؛ tenant match; object visible |
| الحدث | `EVT-ARC-INGEST-STARTED` | يصل إلى: Archive catalogue; Disposition (SLC-12a); Audit |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-ARC-001، REQ-ARC-002، REQ-ARC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-063 | Archive Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-ARC-RETRY-INGEST -->

</details>

### 5.4 US-BC06-ARC-TRANSFER — نقل الحزمة الأرشيفية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-ARC-TRANSFER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/archive-packages/{id}/actions/transfer` | — |
| الأمر | `CMD-ARC-TRANSFER` | نقل الحزمة الأرشيفية |
| السياسة | `POL-ARC-TRANSFER` | Archivist (retry, repair, migrate) · transfer authority (transfer)؛ tenant match; object visible |
| الحدث | `EVT-ARC-TRANSFERRED` | يصل إلى: Archive catalogue; Disposition (SLC-12a); Audit |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-ARC-001، REQ-ARC-002، REQ-ARC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-063 | Archive Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-ARC-TRANSFER -->

</details>

### 5.5 US-BC06-S-ARCHIVE-PACKAGE-01 — تلقائي: disposition action ARCHIVE for a bucket or record set (الحزمة الأرشيفية)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-S-ARCHIVE-PACKAGE-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:disposition action ARCHIVE for a bucket or record set` | SIP assembled from owner exports: content, metadata, provenance, access history |
| الانتقال | ∅ ← INGESTING | — |
| الحدث | `EVT-ARC-INGEST-STARTED` | يصل إلى: Archive catalogue; Disposition (SLC-12a); Audit |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-ARC-001، REQ-ARC-002، REQ-ARC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-063 | Archive Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-ARCHIVE-PACKAGE-01 -->

</details>

### 5.6 US-BC06-S-ARCHIVE-PACKAGE-02 — تلقائي: package validated (الحزمة الأرشيفية)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-S-ARCHIVE-PACKAGE-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:package validated` | BagIt structure valid; every file fixity (SHA-256) recorded; preservation formats (R2-Q6) produced alongside… |
| الانتقال | INGESTING ← ARCHIVED | — |
| الحدث | `EVT-ARC-ARCHIVED` | يصل إلى: Archive catalogue; Disposition (SLC-12a); Audit |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-ARC-001، REQ-ARC-002، REQ-ARC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-063 | Archive Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-ARCHIVE-PACKAGE-02 -->

</details>

### 5.7 US-BC06-S-ARCHIVE-PACKAGE-03 — تلقائي: validation failed (الحزمة الأرشيفية)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-S-ARCHIVE-PACKAGE-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:validation failed` | errors recorded |
| الانتقال | INGESTING ← INGEST_FAILED | — |
| الحدث | `EVT-ARC-INGEST-FAILED` | يصل إلى: Archive catalogue; Disposition (SLC-12a); Audit |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-ARC-001، REQ-ARC-002، REQ-ARC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-063 | Archive Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-ARCHIVE-PACKAGE-03 -->

</details>

### 5.8 US-BC06-S-ARCHIVE-PACKAGE-04 — تلقائي: integrity check failed (الحزمة الأرشيفية)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-S-ARCHIVE-PACKAGE-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:integrity check failed` | fixity mismatch on any file |
| الانتقال | ARCHIVED ← INTEGRITY_FAILED | — |
| الحدث | `EVT-ARC-INTEGRITY-FAILED` | يصل إلى: Archive catalogue; Disposition (SLC-12a); Audit |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-ARC-001، REQ-ARC-002، REQ-ARC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-063 | Archive Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-ARCHIVE-PACKAGE-04 -->

</details>

### 5.9 US-BC06-S-ARCHIVE-PACKAGE-05 — تلقائي: disposition DESTROY executed for the package bucket (الحزمة الأرشيفية)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC06-S-ARCHIVE-PACKAGE-05 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:disposition DESTROY executed for the package bucket` | SLC-12a key destruction; no active hold |
| الانتقال | ARCHIVED, INTEGRITY_FAILED ← DISPOSED | — |
| الحدث | `EVT-ARC-DISPOSED` | يصل إلى: Archive catalogue; Disposition (SLC-12a); Audit |
| الكيان | `AGG-ARCHIVE-PACKAGE` | الحزمة الأرشيفية |
| الجدول | `knowledge.archive_packages` | الجدول الرئيسي للحزمة الأرشيفية |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-ARC-001، REQ-ARC-002، REQ-ARC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-063 | Archive Record |
| الاختبار | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS | دورة حالات الحزمة الأرشيفية، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-ARCHIVE-PACKAGE-05 -->

</details>

### 5.10 US-UI-SCR44-ARCHIVE-PACKAGE — متابعة حالة الحزمة الأرشيفية وأحداث حفظها

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

<!-- BEGIN GENERATED: refs US-UI-SCR44-ARCHIVE-PACKAGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-063 | Archive Record |
| الشاشة | SCR-44 | شاشة المعرفة والأرشيف |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-ARC-001، REQ-ARC-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-063 | Archive Record |
<!-- END GENERATED: refs US-UI-SCR44-ARCHIVE-PACKAGE -->

</details>

### 5.11 US-PLT-ARCHIVE-FIXITY-SCHEDULE — التحقق الدوري من سلامة كل الحزم

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

<!-- BEGIN GENERATED: refs US-PLT-ARCHIVE-FIXITY-SCHEDULE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-ARC-003 | yearly archive integrity verification → 0 unreported corruption; repair from replica |
| المصدر | `THR-S12-P4` | — |
| المصدر | `09-reliability/fmea-slc12.md FM-S12-P3` | — |
| المتطلب | REQ-ARC-002 | The system shall preserve archive packages in preservation formats and verify their integrity periodically. |
| حالة الاستخدام | UC-063 | Archive Record |
<!-- END GENERATED: refs US-PLT-ARCHIVE-FIXITY-SCHEDULE -->

</details>

### 5.12 US-PLT-ARCHIVE-PACKAGE-BUILD — بناء الحزمة الأرشيفية بصيغ الحفظ الدائمة

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

<!-- BEGIN GENERATED: refs US-PLT-ARCHIVE-PACKAGE-BUILD -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `03-domain/contexts/BC06/products-knowledge-archive-spec.md §4` | — |
| المتطلب | REQ-ARC-001 | The system shall transfer records reaching the ARCHIVE disposition action into archive packages containing co… |
| حالة الاستخدام | UC-063 | Archive Record |
<!-- END GENERATED: refs US-PLT-ARCHIVE-PACKAGE-BUILD -->

</details>

### 5.13 US-PLT-ARCHIVE-WORM-REPLICA — تخزين الأرشيف مقفلًا مع نسخة في موقع التعافي

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

<!-- BEGIN GENERATED: refs US-PLT-ARCHIVE-WORM-REPLICA -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-06 | S3-compatible API as the contract; default implementation Ceph RGW (sites with Ceph) or MinIO (smaller cells)… |
| المصدر | `03-domain/contexts/BC06/products-knowledge-archive-spec.md §4` | — |
| المتطلب | REQ-ARC-002 | The system shall preserve archive packages in preservation formats and verify their integrity periodically. |
| حالة الاستخدام | UC-063 | Archive Record |
<!-- END GENERATED: refs US-PLT-ARCHIVE-WORM-REPLICA -->

</details>

### 5.14 US-INT-ARCHIVE-TRANSFER-EXPORT — تسليم الحزمة إلى أرشيف مستلم بإيصال

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R2 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-ARCHIVE-TRANSFER-EXPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `US-BC06-ARC-TRANSFER` | — |
| حالة الاستخدام | UC-063 | Archive Record |
| المصدر | `20-integration-design.md §8` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-INT-ARCHIVE-TRANSFER-EXPORT -->

</details>

### 5.15 US-OPS-ARCHIVE-FIXITY-ALERT — التنبيه الفوري لأي خلل في سلامة الأرشيف

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

<!-- BEGIN GENERATED: refs US-OPS-ARCHIVE-FIXITY-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-ARC-003 | yearly archive integrity verification → 0 unreported corruption; repair from replica |
| المصدر | `09-reliability/observability-slc12.md` | — |
<!-- END GENERATED: refs US-OPS-ARCHIVE-FIXITY-ALERT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-ARC-001 | The system shall transfer records reaching the ARCHIVE disposition action into archive packages containing co… | `US-BC06-ARC-MIGRATE-FORMAT`، `US-BC06-ARC-REPAIR`، `US-BC06-ARC-RETRY-INGEST`، `US-BC06-ARC-TRANSFER`، `US-BC06-S-ARCHIVE-PACKAGE-01`، `US-BC06-S-ARCHIVE-PACKAGE-02`، `US-BC06-S-ARCHIVE-PACKAGE-03`، `US-BC06-S-ARCHIVE-PACKAGE-04`، `US-BC06-S-ARCHIVE-PACKAGE-05`، `US-PLT-ARCHIVE-PACKAGE-BUILD`، `US-UI-SCR44-ARCHIVE-PACKAGE` | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS |
| REQ-ARC-002 | The system shall preserve archive packages in preservation formats and verify their integrity periodically. | `US-BC06-ARC-MIGRATE-FORMAT`، `US-BC06-ARC-REPAIR`، `US-BC06-ARC-RETRY-INGEST`، `US-BC06-ARC-TRANSFER`، `US-BC06-S-ARCHIVE-PACKAGE-01`، `US-BC06-S-ARCHIVE-PACKAGE-02`، `US-BC06-S-ARCHIVE-PACKAGE-03`، `US-BC06-S-ARCHIVE-PACKAGE-04`، `US-BC06-S-ARCHIVE-PACKAGE-05`، `US-PLT-ARCHIVE-FIXITY-SCHEDULE`، `US-PLT-ARCHIVE-WORM-REPLICA`، `US-UI-SCR44-ARCHIVE-PACKAGE` | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS |
| REQ-ARC-003 | When an authorized user requests a historical record, the system shall retrieve it within the archive retriev… | كل قصص الميزة المأخوذة من المواصفة (9) | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
