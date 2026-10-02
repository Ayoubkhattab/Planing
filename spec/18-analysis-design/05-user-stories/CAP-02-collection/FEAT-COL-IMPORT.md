---
id: FEAT-COL-IMPORT
type: feature
title: "استيراد البيانات والحجر"
status: DRAFT
version: "0.1"
capability: CAP-02.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# استيراد البيانات والحجر

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-IMPORT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.04 الاستيعاب والتكامل (R1) |
| الأدوار | مسؤول الإدارة؛ النظام |
| الشاشات | SCR-64 الاستيراد والحجر |
| حالات الاستخدام | UC-094 |
| القصص | 14: 9 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح استيراد دفعات بيانات خارجية مع عزل السجلات المعيبة ومعالجتها قبل نشرها.

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
| QAS-DQ-001 | submits records with invalid geometry or missing CRS | 100 % of invalid records quarantined; 0 published |
| QAS-SCAL-002 | event burst of 50,000/s for 60 s | 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PERF-005 ≤ 5 min after |
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
| `US-BC02-IMP-ACCEPT-QUARANTINE` | قبول العناصر المعزولة في دفعة الاستيراد | أمر | مسودة |
| `US-BC02-IMP-CANCEL` | إلغاء دفعة الاستيراد | أمر | مسودة |
| `US-BC02-IMP-REPROCESS-QUARANTINE` | إعادة معالجة العناصر المعزولة في دفعة الاستيراد | أمر | مسودة |
| `US-BC02-IMP-SUBMIT` | تقديم دفعة الاستيراد | أمر | مسودة |
| `US-BC02-Q-IMP-GET` | جلب: Batch status, counts, quarantine records (paged) | جلب | مسودة |
| `US-DOM-IMP-LIST` | عرض دفعات الاستيراد حسب المحوّل والحالة | جلب | مسودة |
| `US-BC02-S-IMPORT-BATCH-01` | تلقائي: processing started (دفعة الاستيراد) | نظام | مسودة |
| `US-BC02-S-IMPORT-BATCH-02` | تلقائي: all records applied (دفعة الاستيراد) | نظام | مسودة |
| `US-BC02-S-IMPORT-BATCH-03` | تلقائي: finished with invalid records (دفعة الاستيراد) | نظام | مسودة |
| `US-BC02-S-IMPORT-BATCH-04` | تلقائي: unrecoverable error (دفعة الاستيراد) | نظام | مسودة |
| `US-UI-SCR64-QUARANTINE-REVIEW` | مراجعة سجلات الحجر وقبولها أو إعادة معالجتها | واجهة | مسودة |
| `US-PLT-IMP-ASYNC-JOB` | تنفيذ الاستيراد مهمة غير متزامنة قابلة للاستئناف | منصة | مسودة |
| `US-PLT-IMP-LIMITS` | حماية المنصة من الدفعات الضخمة والمعيبة | منصة | مسودة |
| `US-OPS-IMP-QUARANTINE-RATIO` | التنبيه عند ارتفاع نسبة الحجر لمحوّل | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-IMP-ACCEPT-QUARANTINE — قبول العناصر المعزولة في دفعة الاستيراد

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

<!-- BEGIN GENERATED: refs US-BC02-IMP-ACCEPT-QUARANTINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/import-batches/{id}/actions/accept-quarantine` | — |
| الأمر | `CMD-IMP-ACCEPT-QUARANTINE` | قبول العناصر المعزولة في دفعة الاستيراد |
| السياسة | `POL-IMP-ACCEPT-QUARANTINE` | adapter service account · Administrator؛ tenant match; object visible to subject (label ≤ clearance); write p… |
| الحدث | `EVT-IMP-QUARANTINE-ACCEPTED` | يصل إلى: Import worker; Adapter owner notification |
| الكيان | `AGG-IMPORT-BATCH` | دفعة الاستيراد |
| الجدول | `information.import_batches` | الجدول الرئيسي لدفعة الاستيراد |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-005، REQ-INF-006، REQ-INF-007، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS | دورة حالات دفعة الاستيراد، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-IMP-ACCEPT-QUARANTINE -->

</details>

### 5.2 US-BC02-IMP-CANCEL — إلغاء دفعة الاستيراد

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

<!-- BEGIN GENERATED: refs US-BC02-IMP-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/import-batches/{id}/actions/cancel` | — |
| الأمر | `CMD-IMP-CANCEL` | إلغاء دفعة الاستيراد |
| السياسة | `POL-IMP-CANCEL` | adapter service account · Administrator؛ tenant match; object visible to subject (label ≤ clearance); write p… |
| الحدث | `EVT-IMP-CANCELLED` | يصل إلى: Import worker; Adapter owner notification |
| الكيان | `AGG-IMPORT-BATCH` | دفعة الاستيراد |
| الجدول | `information.import_batches` | الجدول الرئيسي لدفعة الاستيراد |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-005، REQ-INF-006، REQ-INF-007، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS | دورة حالات دفعة الاستيراد، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-IMP-CANCEL -->

</details>

### 5.3 US-BC02-IMP-REPROCESS-QUARANTINE — إعادة معالجة العناصر المعزولة في دفعة الاستيراد

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

<!-- BEGIN GENERATED: refs US-BC02-IMP-REPROCESS-QUARANTINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/import-batches/{id}/actions/reprocess-quarantine` | — |
| الأمر | `CMD-IMP-REPROCESS-QUARANTINE` | إعادة معالجة العناصر المعزولة في دفعة الاستيراد |
| السياسة | `POL-IMP-REPROCESS-QUARANTINE` | adapter service account · Administrator؛ tenant match; object visible to subject (label ≤ clearance); write p… |
| الحدث | `EVT-IMP-REPROCESSING` | يصل إلى: Import worker; Adapter owner notification |
| الكيان | `AGG-IMPORT-BATCH` | دفعة الاستيراد |
| الجدول | `information.import_batches` | الجدول الرئيسي لدفعة الاستيراد |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-005، REQ-INF-006، REQ-INF-007، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS | دورة حالات دفعة الاستيراد، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-IMP-REPROCESS-QUARANTINE -->

</details>

### 5.4 US-BC02-IMP-SUBMIT — تقديم دفعة الاستيراد

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

<!-- BEGIN GENERATED: refs US-BC02-IMP-SUBMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/import-batches` | — |
| الأمر | `CMD-IMP-SUBMIT` | تقديم دفعة الاستيراد |
| السياسة | `POL-IMP-SUBMIT` | adapter service account · Administrator؛ tenant match; object visible to subject (label ≤ clearance); write p… |
| الحدث | `EVT-IMP-RECEIVED` | يصل إلى: Import worker; Adapter owner notification |
| الكيان | `AGG-IMPORT-BATCH` | دفعة الاستيراد |
| الجدول | `information.import_batches` | الجدول الرئيسي لدفعة الاستيراد |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-005، REQ-INF-006، REQ-INF-007، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS | دورة حالات دفعة الاستيراد، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-IMP-SUBMIT -->

</details>

### 5.5 US-BC02-Q-IMP-GET — جلب: Batch status, counts, quarantine records (paged)

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

<!-- BEGIN GENERATED: refs US-BC02-Q-IMP-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/import-batches/{batch_id}` | — |
| الاستعلام | `QRY-IMP-GET` | Batch status, counts, quarantine records (paged) |
| السياسة | `POL-IMP-GET` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-IMPORT-BATCH` | دفعة الاستيراد |
| الجدول | `information.import_batches` | الجدول الرئيسي لدفعة الاستيراد |
| وحدة النشر | DU-05 | — |
| المتطلب | REQ-INF-006 | If an ingested record fails validation, then the system shall quarantine it with the failure reason and shall… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS | دورة حالات دفعة الاستيراد، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-IMP-GET -->

</details>

### 5.6 US-DOM-IMP-LIST — عرض دفعات الاستيراد حسب المحوّل والحالة

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

<!-- BEGIN GENERATED: refs US-DOM-IMP-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-64 | شاشة الاستيراد والحجر |
| حالة الاستخدام | UC-094 | Ingest External Data |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-006 | If an ingested record fails validation, then the system shall quarantine it with the failure reason and shall… |
| حالة الاستخدام | UC-094 | Ingest External Data |
<!-- END GENERATED: refs US-DOM-IMP-LIST -->

</details>

### 5.7 US-BC02-S-IMPORT-BATCH-01 — تلقائي: processing started (دفعة الاستيراد)

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

<!-- BEGIN GENERATED: refs US-BC02-S-IMPORT-BATCH-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:processing started` | worker lease acquired |
| الانتقال | RECEIVED ← PROCESSING | — |
| الحدث | `EVT-IMP-PROCESSING-STARTED` | يصل إلى: Import worker; Adapter owner notification |
| الكيان | `AGG-IMPORT-BATCH` | دفعة الاستيراد |
| الجدول | `information.import_batches` | الجدول الرئيسي لدفعة الاستيراد |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-005، REQ-INF-006، REQ-INF-007، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS | دورة حالات دفعة الاستيراد، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-S-IMPORT-BATCH-01 -->

</details>

### 5.8 US-BC02-S-IMPORT-BATCH-02 — تلقائي: all records applied (دفعة الاستيراد)

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

<!-- BEGIN GENERATED: refs US-BC02-S-IMPORT-BATCH-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:all records applied` | each record applied idempotently with lineage (adapter, batch, mapping version) |
| الانتقال | PROCESSING ← COMPLETED | — |
| الحدث | `EVT-IMP-COMPLETED` | يصل إلى: Import worker; Adapter owner notification |
| الكيان | `AGG-IMPORT-BATCH` | دفعة الاستيراد |
| الجدول | `information.import_batches` | الجدول الرئيسي لدفعة الاستيراد |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-005، REQ-INF-006، REQ-INF-007، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS | دورة حالات دفعة الاستيراد، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-S-IMPORT-BATCH-02 -->

</details>

### 5.9 US-BC02-S-IMPORT-BATCH-03 — تلقائي: finished with invalid records (دفعة الاستيراد)

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

<!-- BEGIN GENERATED: refs US-BC02-S-IMPORT-BATCH-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:finished with invalid records` | invalid records quarantined with reason codes |
| الانتقال | PROCESSING ← COMPLETED_WITH_QUARANTINE | — |
| الحدث | `EVT-IMP-COMPLETED-WITH-QUARANTINE` | يصل إلى: Import worker; Adapter owner notification |
| الكيان | `AGG-IMPORT-BATCH` | دفعة الاستيراد |
| الجدول | `information.import_batches` | الجدول الرئيسي لدفعة الاستيراد |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-005، REQ-INF-006، REQ-INF-007، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS | دورة حالات دفعة الاستيراد، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-S-IMPORT-BATCH-03 -->

</details>

### 5.10 US-BC02-S-IMPORT-BATCH-04 — تلقائي: unrecoverable error (دفعة الاستيراد)

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

<!-- BEGIN GENERATED: refs US-BC02-S-IMPORT-BATCH-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:unrecoverable error` | applied records remain; re-submit resumes idempotently |
| الانتقال | PROCESSING ← FAILED | — |
| الحدث | `EVT-IMP-FAILED` | يصل إلى: Import worker; Adapter owner notification |
| الكيان | `AGG-IMPORT-BATCH` | دفعة الاستيراد |
| الجدول | `information.import_batches` | الجدول الرئيسي لدفعة الاستيراد |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-005، REQ-INF-006، REQ-INF-007، REQ-INF-008، REQ-INF-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS | دورة حالات دفعة الاستيراد، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-S-IMPORT-BATCH-04 -->

</details>

### 5.11 US-UI-SCR64-QUARANTINE-REVIEW — مراجعة سجلات الحجر وقبولها أو إعادة معالجتها

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

<!-- BEGIN GENERATED: refs US-UI-SCR64-QUARANTINE-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-64 | شاشة الاستيراد والحجر |
| المصدر | `QRY-IMP-GET` | — |
| الجودة | QAS-DQ-001 | submits records with invalid geometry or missing CRS → 100 % of invalid records quarantined; 0 published |
| المتطلب | REQ-INF-006 | If an ingested record fails validation, then the system shall quarantine it with the failure reason and shall… |
| حالة الاستخدام | UC-094 | Ingest External Data |
<!-- END GENERATED: refs US-UI-SCR64-QUARANTINE-REVIEW -->

</details>

### 5.12 US-PLT-IMP-ASYNC-JOB — تنفيذ الاستيراد مهمة غير متزامنة قابلة للاستئناف

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

<!-- BEGIN GENERATED: refs US-PLT-IMP-ASYNC-JOB -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `FM-S02-04` | — |
| القرار التقني | TD-12 | Kubernetes Jobs with Kueue (fair sharing, per-tenant quotas); images from internal Harbor registry, signed (c… |
| المتطلب | REQ-PLT-005 | The system shall run heavy operations (raster processing, bulk import, analysis runs, reconstruction, report… |
<!-- END GENERATED: refs US-PLT-IMP-ASYNC-JOB -->

</details>

### 5.13 US-PLT-IMP-LIMITS — حماية المنصة من الدفعات الضخمة والمعيبة

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

<!-- BEGIN GENERATED: refs US-PLT-IMP-LIMITS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `THR-S02-10` | — |
| المصدر | `THR-010` | — |
| الجودة | QAS-SCAL-002 | event burst of 50,000/s for 60 s → 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PER… |
<!-- END GENERATED: refs US-PLT-IMP-LIMITS -->

</details>

### 5.14 US-OPS-IMP-QUARANTINE-RATIO — التنبيه عند ارتفاع نسبة الحجر لمحوّل

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

<!-- BEGIN GENERATED: refs US-OPS-IMP-QUARANTINE-RATIO -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc02.md` | — |
| المصدر | `THR-S02-01` | — |
<!-- END GENERATED: refs US-OPS-IMP-QUARANTINE-RATIO -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-005 | The system shall ingest external data only through registered adapters or bulk import jobs that record source… | كل قصص الأوامر والنظام في الميزة (8) | TST-ADAPTER-SM، TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS |
| REQ-INF-006 | If an ingested record fails validation, then the system shall quarantine it with the failure reason and shall… | `US-BC02-IMP-ACCEPT-QUARANTINE`، `US-BC02-IMP-CANCEL`، `US-BC02-IMP-REPROCESS-QUARANTINE`، `US-BC02-IMP-SUBMIT`، `US-BC02-Q-IMP-GET`، `US-BC02-S-IMPORT-BATCH-01`، `US-BC02-S-IMPORT-BATCH-02`، `US-BC02-S-IMPORT-BATCH-03`، `US-BC02-S-IMPORT-BATCH-04`، `US-DOM-IMP-LIST`، `US-UI-SCR64-QUARANTINE-REVIEW` | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS |
| REQ-INF-007 | When an ingestion batch is re-submitted, the system shall not create duplicate records. | كل قصص الأوامر والنظام في الميزة (8) | TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS |
| REQ-INF-008 | The system shall import geospatial data via OGC API Features/Maps/Tiles, WMS/WFS, GeoJSON, GeoPackage, GeoTIF… | كل قصص الأوامر والنظام في الميزة (8) | TST-ADAPTER-SM، TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS |
| REQ-INF-009 | The system shall ingest weather data through an adapter and register the provider as a source. | كل قصص الأوامر والنظام في الميزة (8) | TST-ADAPTER-SM، TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS |
| REQ-PLT-005 | The system shall run heavy operations (raster processing, bulk import, analysis runs, reconstruction, report… | `US-PLT-IMP-ASYNC-JOB` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
