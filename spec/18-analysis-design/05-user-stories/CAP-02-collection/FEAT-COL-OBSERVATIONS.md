---
id: FEAT-COL-OBSERVATIONS
type: feature
title: "تسجيل الملاحظات"
status: DRAFT
version: "0.1"
capability: CAP-02.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تسجيل الملاحظات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-OBSERVATIONS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) |
| الأدوار | المستخدم الميداني؛ المشغِّل؛ المحلل؛ النظام |
| الشاشات | SCR-23 الملاحظات، SCR-11 الصورة العملياتية المشتركة (COP) |
| حالات الاستخدام | UC-005، UC-090 |
| القصص | 11: 5 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمستخدم الميداني والمحلل تسجيل ما رصده في زمان ومكان محددين مع مرفقاته وتصحيحه بإصدار جديد والبحث فيه.

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
| QAS-PERF-002 | reads a single object or a list page | single object p95 ≤ 300 ms; list page p95 ≤ 1 s |
| QAS-PERF-004 | an object is created or changed | index lag p95 ≤ 30 s |
| QAS-PERF-008 | records an observation (online) | p95 ≤ 30 s |
| QAS-SCAL-004 | observations grow to 1e9 | QAS-PERF-002 holds for queries with a time window ≤ 30 days |
| QAS-USA-001 | records an observation with one photo on the mobile app | median ≤ 60 s in usability test with 10 field users |
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
| `US-BC02-OBS-AMEND` | تعديل الملاحظة بإصدار جديد | أمر | مسودة |
| `US-BC02-OBS-ATTACH-EVIDENCE` | إرفاق دليل بـالملاحظة | أمر | مسودة |
| `US-BC02-OBS-RECORD` | تسجيل الملاحظة | أمر | مسودة |
| `US-BC02-Q-OBS-GET` | جلب: Observation with measurements and attachment refs | جلب | مسودة |
| `US-BC02-Q-OBS-LIST` | جلب: Observations by bbox, time window (mandatory, ≤ 31 days), source, state | جلب | مسودة |
| `US-UI-SCR23-LOCATION-QUALITY` | عرض دقة الموقع وأعلام جودة الملاحظة | واجهة | مسودة |
| `US-UI-SCR23-OBS-LIST` | تصفح الملاحظات بنافذة زمنية ومنطقة | واجهة | مسودة |
| `US-UI-SCR23-QUICK-CAPTURE` | تسجيل ملاحظة بصورة بيد واحدة | واجهة | مسودة |
| `US-PLT-OBS-SEARCHABLE` | ظهور الملاحظة في البحث خلال 30 ثانية | منصة | مسودة |
| `US-PLT-OBS-VOLUME` | ثبات الأداء مع مليار ملاحظة | منصة | مسودة |
| `US-OPS-OBS-SOURCE-SILENCE` | التنبيه عند صمت مصادر الملاحظات | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-OBS-AMEND — تعديل الملاحظة بإصدار جديد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-OBS-AMEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/observations/{id}/actions/amend` | دون اتصال: نعم |
| الأمر | `CMD-OBS-AMEND` | تعديل الملاحظة بإصدار جديد |
| السياسة | `POL-OBS-AMEND` | Field User / Operator / Analyst / adapter service account (amend)؛ tenant match; object visible to subject (l… |
| الحدث | `EVT-OBS-AMENDED` | يصل إلى: Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (… |
| الكيان | `AGG-OBSERVATION` | الملاحظة |
| الجدول | `information.observations` | الجدول الرئيسي للملاحظة |
| وحدة النشر | DU-05 | — |
| المتطلب | REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… |
| حالة الاستخدام | UC-005 | Register Observation |
| الاختبار | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS | دورة حالات الملاحظة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-OBS-AMEND -->

</details>

### 5.2 US-BC02-OBS-ATTACH-EVIDENCE — إرفاق دليل بـالملاحظة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-OBS-ATTACH-EVIDENCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/observations/{id}/actions/attach-evidence` | دون اتصال: نعم |
| الأمر | `CMD-OBS-ATTACH-EVIDENCE` | إرفاق دليل بـالملاحظة |
| السياسة | `POL-OBS-ATTACH-EVIDENCE` | Field User / Operator / Analyst / adapter service account (attach evidence)؛ tenant match; object visible to… |
| الحدث | `EVT-OBS-EVIDENCE-ATTACHED` | يصل إلى: Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (… |
| الكيان | `AGG-OBSERVATION` | الملاحظة |
| الجدول | `information.observations` | الجدول الرئيسي للملاحظة |
| وحدة النشر | DU-05 | — |
| المتطلب | REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… |
| حالة الاستخدام | UC-005 | Register Observation |
| الاختبار | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS | دورة حالات الملاحظة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-OBS-ATTACH-EVIDENCE -->

</details>

### 5.3 US-BC02-OBS-RECORD — تسجيل الملاحظة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-OBS-RECORD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/observations` | دون اتصال: نعم |
| الأمر | `CMD-OBS-RECORD` | تسجيل الملاحظة |
| السياسة | `POL-OBS-RECORD` | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)؛ tenant match… |
| الحدث | `EVT-OBS-RECORDED` | يصل إلى: Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (… |
| الكيان | `AGG-OBSERVATION` | الملاحظة |
| الجدول | `information.observations` | الجدول الرئيسي للملاحظة |
| وحدة النشر | DU-05 | — |
| المتطلب | REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… |
| حالة الاستخدام | UC-005 | Register Observation |
| الاختبار | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS | دورة حالات الملاحظة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-OBS-RECORD -->

</details>

### 5.4 US-BC02-Q-OBS-GET — جلب: Observation with measurements and attachment refs

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

<!-- BEGIN GENERATED: refs US-BC02-Q-OBS-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/observations/{observation_id}` | — |
| الاستعلام | `QRY-OBS-GET` | Observation with measurements and attachment refs |
| السياسة | `POL-OBS-GET` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-OBSERVATION` | الملاحظة |
| الجدول | `information.observations` | الجدول الرئيسي للملاحظة |
| وحدة النشر | DU-05 | — |
| المتطلب | REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… |
| حالة الاستخدام | UC-005 | Register Observation |
| الاختبار | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS | دورة حالات الملاحظة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-OBS-GET -->

</details>

### 5.5 US-BC02-Q-OBS-LIST — جلب: Observations by bbox, time window (mandatory, ≤ 31 days), source, state

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

<!-- BEGIN GENERATED: refs US-BC02-Q-OBS-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/observations` | — |
| الاستعلام | `QRY-OBS-LIST` | Observations by bbox, time window (mandatory, ≤ 31 days), source, state |
| السياسة | `POL-OBS-LIST` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-OBSERVATION` | الملاحظة |
| الجدول | `information.observations` | الجدول الرئيسي للملاحظة |
| وحدة النشر | DU-05 | — |
| المتطلب | REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… |
| حالة الاستخدام | UC-005 | Register Observation |
| الاختبار | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS | دورة حالات الملاحظة، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-OBS-LIST -->

</details>

### 5.6 US-UI-SCR23-LOCATION-QUALITY — عرض دقة الموقع وأعلام جودة الملاحظة

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

<!-- BEGIN GENERATED: refs US-UI-SCR23-LOCATION-QUALITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-23 | شاشة الملاحظات |
| المصدر | `21-ui-design.md §7` | — |
| المصدر | `INV-OBS-04` | — |
| المتطلب | REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… |
| حالة الاستخدام | UC-005 | Register Observation |
<!-- END GENERATED: refs US-UI-SCR23-LOCATION-QUALITY -->

</details>

### 5.7 US-UI-SCR23-OBS-LIST — تصفح الملاحظات بنافذة زمنية ومنطقة

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

<!-- BEGIN GENERATED: refs US-UI-SCR23-OBS-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-23 | شاشة الملاحظات |
| المصدر | `QRY-OBS-LIST` | — |
| المصدر | `21-ui-design.md §6.1` | — |
<!-- END GENERATED: refs US-UI-SCR23-OBS-LIST -->

</details>

### 5.8 US-UI-SCR23-QUICK-CAPTURE — تسجيل ملاحظة بصورة بيد واحدة

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

<!-- BEGIN GENERATED: refs US-UI-SCR23-QUICK-CAPTURE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-23 | شاشة الملاحظات |
| الجودة | QAS-USA-001 | records an observation with one photo on the mobile app → median ≤ 60 s in usability test with 10 field users |
| المصدر | `21-ui-design.md §8.1` | — |
| المصدر | `21-ui-design.md §10` | — |
| المتطلب | REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… |
| حالة الاستخدام | UC-005 | Register Observation |
<!-- END GENERATED: refs US-UI-SCR23-QUICK-CAPTURE -->

</details>

### 5.9 US-PLT-OBS-SEARCHABLE — ظهور الملاحظة في البحث خلال 30 ثانية

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

<!-- BEGIN GENERATED: refs US-PLT-OBS-SEARCHABLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-008 | records an observation (online) → p95 ≤ 30 s |
| الجودة | QAS-PERF-004 | an object is created or changed → index lag p95 ≤ 30 s |
<!-- END GENERATED: refs US-PLT-OBS-SEARCHABLE -->

</details>

### 5.10 US-PLT-OBS-VOLUME — ثبات الأداء مع مليار ملاحظة

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

<!-- BEGIN GENERATED: refs US-PLT-OBS-VOLUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SCAL-004 | observations grow to 1e9 → QAS-PERF-002 holds for queries with a time window ≤ 30 days |
| القرار التقني | TD-01 | PostgreSQL 16+ with PostGIS, btree_gist, range types (tstzrange), RLS, declarative partitioning; one cluster… |
| الجودة | QAS-PERF-002 | reads a single object or a list page → single object p95 ≤ 300 ms; list page p95 ≤ 1 s |
<!-- END GENERATED: refs US-PLT-OBS-VOLUME -->

</details>

### 5.11 US-OPS-OBS-SOURCE-SILENCE — التنبيه عند صمت مصادر الملاحظات

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

<!-- BEGIN GENERATED: refs US-OPS-OBS-SOURCE-SILENCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc02.md` | — |
| المصدر | `FM-S02-05` | — |
<!-- END GENERATED: refs US-OPS-OBS-SOURCE-SILENCE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its… | `US-BC02-OBS-AMEND`، `US-BC02-OBS-ATTACH-EVIDENCE`، `US-BC02-OBS-RECORD`، `US-BC02-Q-OBS-GET`، `US-BC02-Q-OBS-LIST`، `US-UI-SCR23-LOCATION-QUALITY`، `US-UI-SCR23-QUICK-CAPTURE` | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
