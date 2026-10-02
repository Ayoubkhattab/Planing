---
id: FEAT-COL-SENSORS
type: feature
title: "تدفقات الحساسات"
status: DRAFT
version: "0.1"
capability: CAP-02.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تدفقات الحساسات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-SENSORS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.04 الاستيعاب والتكامل (R1) |
| الأدوار | مهندس التكامل؛ المحلل؛ النظام |
| الشاشات | SCR-65 المحوّلات والاتصالات والحساسات |
| حالات الاستخدام | UC-094 |
| القصص | 11: 7 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح ربط تدفقات الحساسات وتحديد قواعد جودتها والتنبيه عند انقطاع بياناتها.

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
| QAS-PERF-012 | batch of 1,000 observations | batch commit p95 ≤ 1 s; 0 duplicates on retry |
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
| `US-BC07-SNS-ACTIVATE` | تفعيل تدفق الحسّاس | أمر | مسودة |
| `US-BC07-SNS-PAUSE` | إيقاف تدفق الحسّاس مؤقتًا | أمر | مسودة |
| `US-BC07-SNS-REGISTER` | تسجيل تدفق الحسّاس | أمر | مسودة |
| `US-BC07-SNS-RETIRE` | إحالة تدفق الحسّاس إلى التقاعد | أمر | مسودة |
| `US-BC07-SNS-SET-QUALITY-RULES` | تحديد قواعد جودة تدفق الحسّاس | أمر | مسودة |
| `US-BC07-Q-SNS-LIST` | جلب: Streams with rate, staleness, quality violation counts | جلب | مسودة |
| `US-BC07-S-SENSOR-STREAM-01` | تلقائي: no data beyond stale-after (تدفق الحسّاس) | نظام | مسودة |
| `US-UI-SCR65-SENSOR-STREAMS` | متابعة تدفقات الحساسات وجودتها | واجهة | مسودة |
| `US-PLT-SENSOR-QUALITY-EVAL` | تقييم جودة القراءات دون حذفها | منصة | مسودة |
| `US-PLT-SENSOR-THROUGHPUT` | استيعاب خمسة آلاف قراءة في الثانية | منصة | مسودة |
| `US-INT-SENSOR-GATEWAY` | استقبال قراءات بوابة الحساسات كملاحظات | تكامل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-SNS-ACTIVATE — تفعيل تدفق الحسّاس

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

<!-- BEGIN GENERATED: refs US-BC07-SNS-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/sensor-streams/{id}/actions/activate` | — |
| الأمر | `CMD-SNS-ACTIVATE` | تفعيل تدفق الحسّاس |
| السياسة | `POL-SNS-ACTIVATE` | integration engineer؛ tenant match |
| الحدث | `EVT-SNS-ACTIVATED` | يصل إلى: Ingestion workers (SLC-02 batches); Operations alerting |
| الكيان | `AGG-SENSOR-STREAM` | تدفق الحسّاس |
| الجدول | `integration.sensor_streams` | الجدول الرئيسي لتدفق الحسّاس |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-SENSOR-STREAM-SM، TST-SLC16-INVARIANTS | دورة حالات تدفق الحسّاس، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-SNS-ACTIVATE -->

</details>

### 5.2 US-BC07-SNS-PAUSE — إيقاف تدفق الحسّاس مؤقتًا

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

<!-- BEGIN GENERATED: refs US-BC07-SNS-PAUSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/sensor-streams/{id}/actions/pause` | — |
| الأمر | `CMD-SNS-PAUSE` | إيقاف تدفق الحسّاس مؤقتًا |
| السياسة | `POL-SNS-PAUSE` | integration engineer؛ tenant match |
| الحدث | `EVT-SNS-PAUSED` | يصل إلى: Ingestion workers (SLC-02 batches); Operations alerting |
| الكيان | `AGG-SENSOR-STREAM` | تدفق الحسّاس |
| الجدول | `integration.sensor_streams` | الجدول الرئيسي لتدفق الحسّاس |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-SENSOR-STREAM-SM، TST-SLC16-INVARIANTS | دورة حالات تدفق الحسّاس، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-SNS-PAUSE -->

</details>

### 5.3 US-BC07-SNS-REGISTER — تسجيل تدفق الحسّاس

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

<!-- BEGIN GENERATED: refs US-BC07-SNS-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/sensor-streams` | — |
| الأمر | `CMD-SNS-REGISTER` | تسجيل تدفق الحسّاس |
| السياسة | `POL-SNS-REGISTER` | integration engineer؛ tenant match |
| الحدث | `EVT-SNS-REGISTERED` | يصل إلى: Ingestion workers (SLC-02 batches); Operations alerting |
| الكيان | `AGG-SENSOR-STREAM` | تدفق الحسّاس |
| الجدول | `integration.sensor_streams` | الجدول الرئيسي لتدفق الحسّاس |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-SENSOR-STREAM-SM، TST-SLC16-INVARIANTS | دورة حالات تدفق الحسّاس، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-SNS-REGISTER -->

</details>

### 5.4 US-BC07-SNS-RETIRE — إحالة تدفق الحسّاس إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC07-SNS-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/sensor-streams/{id}/actions/retire` | — |
| الأمر | `CMD-SNS-RETIRE` | إحالة تدفق الحسّاس إلى التقاعد |
| السياسة | `POL-SNS-RETIRE` | integration engineer؛ tenant match |
| الحدث | `EVT-SNS-RETIRED` | يصل إلى: Ingestion workers (SLC-02 batches); Operations alerting |
| الكيان | `AGG-SENSOR-STREAM` | تدفق الحسّاس |
| الجدول | `integration.sensor_streams` | الجدول الرئيسي لتدفق الحسّاس |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-SENSOR-STREAM-SM، TST-SLC16-INVARIANTS | دورة حالات تدفق الحسّاس، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-SNS-RETIRE -->

</details>

### 5.5 US-BC07-SNS-SET-QUALITY-RULES — تحديد قواعد جودة تدفق الحسّاس

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

<!-- BEGIN GENERATED: refs US-BC07-SNS-SET-QUALITY-RULES -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/sensor-streams/{id}/actions/set-quality-rules` | — |
| الأمر | `CMD-SNS-SET-QUALITY-RULES` | تحديد قواعد جودة تدفق الحسّاس |
| السياسة | `POL-SNS-SET-QUALITY-RULES` | integration engineer؛ tenant match |
| الحدث | `EVT-SNS-QUALITY-RULES-SET` | يصل إلى: Ingestion workers (SLC-02 batches); Operations alerting |
| الكيان | `AGG-SENSOR-STREAM` | تدفق الحسّاس |
| الجدول | `integration.sensor_streams` | الجدول الرئيسي لتدفق الحسّاس |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-SENSOR-STREAM-SM، TST-SLC16-INVARIANTS | دورة حالات تدفق الحسّاس، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-SNS-SET-QUALITY-RULES -->

</details>

### 5.6 US-BC07-Q-SNS-LIST — جلب: Streams with rate, staleness, quality violation counts

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

<!-- BEGIN GENERATED: refs US-BC07-Q-SNS-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/integration/sensor-streams` | — |
| الاستعلام | `QRY-SNS-LIST` | Streams with rate, staleness, quality violation counts |
| السياسة | `POL-SNS-LIST` | integration engineers, Analyst |
| الكيان | `AGG-SENSOR-STREAM` | تدفق الحسّاس |
| الجدول | `integration.sensor_streams` | الجدول الرئيسي لتدفق الحسّاس |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-SENSOR-STREAM-SM، TST-SLC16-INVARIANTS | دورة حالات تدفق الحسّاس، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-Q-SNS-LIST -->

</details>

### 5.7 US-BC07-S-SENSOR-STREAM-01 — تلقائي: no data beyond stale-after (تدفق الحسّاس)

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

<!-- BEGIN GENERATED: refs US-BC07-S-SENSOR-STREAM-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:no data beyond stale-after` | stream flagged STALE; alert to owner |
| الانتقال | ACTIVE ← (بلا تغيير) | — |
| الحدث | `EVT-SNS-STALE` | يصل إلى: Ingestion workers (SLC-02 batches); Operations alerting |
| الكيان | `AGG-SENSOR-STREAM` | تدفق الحسّاس |
| الجدول | `integration.sensor_streams` | الجدول الرئيسي لتدفق الحسّاس |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-SENSOR-STREAM-SM، TST-SLC16-INVARIANTS | دورة حالات تدفق الحسّاس، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-S-SENSOR-STREAM-01 -->

</details>

### 5.8 US-UI-SCR65-SENSOR-STREAMS — متابعة تدفقات الحساسات وجودتها

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

<!-- BEGIN GENERATED: refs US-UI-SCR65-SENSOR-STREAMS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-65 | شاشة المحوّلات والاتصالات والحساسات |
| المصدر | `QRY-SNS-LIST` | — |
| المصدر | `AGG-SENSOR-STREAM` | — |
<!-- END GENERATED: refs US-UI-SCR65-SENSOR-STREAMS -->

</details>

### 5.9 US-PLT-SENSOR-QUALITY-EVAL — تقييم جودة القراءات دون حذفها

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

<!-- BEGIN GENERATED: refs US-PLT-SENSOR-QUALITY-EVAL -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `INV-SNS-02` | — |
| المصدر | `AGG-SENSOR-STREAM` | — |
| المصدر | `observability-slc16.md` | — |
<!-- END GENERATED: refs US-PLT-SENSOR-QUALITY-EVAL -->

</details>

### 5.10 US-PLT-SENSOR-THROUGHPUT — استيعاب خمسة آلاف قراءة في الثانية

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

<!-- BEGIN GENERATED: refs US-PLT-SENSOR-THROUGHPUT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-012 | batch of 1,000 observations → batch commit p95 ≤ 1 s; 0 duplicates on retry |
| الجودة | QAS-SCAL-002 | event burst of 50,000/s for 60 s → 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PER… |
| المتطلب | REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. |
| حالة الاستخدام | UC-094 | Ingest External Data |
<!-- END GENERATED: refs US-PLT-SENSOR-THROUGHPUT -->

</details>

### 5.11 US-INT-SENSOR-GATEWAY — استقبال قراءات بوابة الحساسات كملاحظات

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

<!-- BEGIN GENERATED: refs US-INT-SENSOR-GATEWAY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `INV-SNS-01` | — |
| المصدر | `INV-SNS-03` | — |
| المصدر | `THR-S16-05` | — |
| المصدر | `enterprise-integration-spec.md §2` | — |
| المتطلب | REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. |
| حالة الاستخدام | UC-094 | Ingest External Data |
<!-- END GENERATED: refs US-INT-SENSOR-GATEWAY -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. | `US-BC07-Q-SNS-LIST`، `US-BC07-S-SENSOR-STREAM-01`، `US-BC07-SNS-ACTIVATE`، `US-BC07-SNS-PAUSE`، `US-BC07-SNS-REGISTER`، `US-BC07-SNS-RETIRE`، `US-BC07-SNS-SET-QUALITY-RULES`، `US-INT-SENSOR-GATEWAY`، `US-PLT-SENSOR-THROUGHPUT` | TST-SENSOR-STREAM-SM، TST-SLC16-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
