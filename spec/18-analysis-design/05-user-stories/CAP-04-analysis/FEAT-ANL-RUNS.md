---
id: FEAT-ANL-RUNS
type: feature
title: "تشغيل التحليل وإعادة إنتاجه"
status: DRAFT
version: "0.1"
capability: CAP-04.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تشغيل التحليل وإعادة إنتاجه

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ANL-RUNS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-04 التحليل والتقييم |
| القدرة الفرعية | CAP-04.02 التنفيذ وإعادة الإنتاج (R1) |
| الأدوار | المحلل؛ النظام |
| الشاشات | SCR-30 الحالة التحليلية والتشغيلات |
| حالات الاستخدام | UC-013 |
| القصص | 15: 8 من المواصفة، و7 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يشغّل المحلل تحليلًا طويلًا دون انتظار، ويتابع تقدمه، ويعيد تشغيله لاحقًا ليحصل على النتيجة نفسها أو يعرف ما الذي اختلف.

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
| QAS-PERF-001 | submits a state-changing command | p95 ≤ 300 ms; p99 ≤ 1 s |
| QAS-PERF-020 | tenant submits 100 runs | no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s |
| QAS-SEC-013 | run submitted by user U | run reads only data visible to U; results labelled ≥ max input label |
| QAS-TRC-002 | re-executes a recorded deterministic analysis run | 100 % |
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
| `US-BC03-RUN-CANCEL` | إلغاء تشغيل التحليل | أمر | مسودة |
| `US-BC03-RUN-REPRODUCE` | إعادة إنتاج تشغيل التحليل | أمر | مسودة |
| `US-BC03-RUN-SUBMIT` | تقديم تشغيل التحليل | أمر | مسودة |
| `US-DOM-ANL-RUN-RETRY` | إعادة محاولة تشغيل تحليل فشل | أمر | مسودة |
| `US-BC03-Q-RUN-ARTIFACT` | جلب: Short-lived download target for a result artifact | جلب | مسودة |
| `US-BC03-Q-RUN-GET` | جلب: Run with pins, parameters, steps, status, artifacts, reproduction report | جلب | مسودة |
| `US-BC03-S-ANALYSIS-RUN-01` | تلقائي: worker lease acquired (تشغيل التحليل) | نظام | مسودة |
| `US-BC03-S-ANALYSIS-RUN-02` | تلقائي: completed (تشغيل التحليل) | نظام | مسودة |
| `US-BC03-S-ANALYSIS-RUN-03` | تلقائي: error or timeout (تشغيل التحليل) | نظام | مسودة |
| `US-UI-SCR30-REPRODUCE-REPORT` | عرض تقرير إعادة الإنتاج وما اختلف | واجهة | مسودة |
| `US-UI-SCR30-RUN-PROGRESS` | عرض تقدم التشغيل وإلغاؤه وسبب فشله | واجهة | مسودة |
| `US-PLT-ANL-REPRO-CHECK` | فحص دوري لقابلية إعادة إنتاج التشغيلات | منصة | مسودة |
| `US-PLT-ANL-RUN-DELEGATION` | تشغيل التحليل بصلاحيات مقدّمه فقط | منصة | مسودة |
| `US-PLT-ANL-RUN-FAIRSHARE` | توزيع عادل للحوسبة بحصة لكل مستأجر | منصة | مسودة |
| `US-PLT-ANL-RUN-STATUS` | متابعة حالة التشغيل وتقدمه بالسحب والاشتراك | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-RUN-CANCEL — إلغاء تشغيل التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-RUN-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-runs/{id}/actions/cancel` | — |
| الأمر | `CMD-RUN-CANCEL` | إلغاء تشغيل التحليل |
| السياسة | `POL-RUN-CANCEL` | Analyst (submit, reproduce, cancel)؛ tenant match; case visible; label rules |
| الحدث | `EVT-RUN-CANCELLED` | يصل إلى: Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| الكيان | `AGG-ANALYSIS-RUN` | تشغيل التحليل |
| الجدول | `intelligence.analysis_runs` | الجدول الرئيسي لتشغيل التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-002، REQ-ANL-003، REQ-ANL-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS | دورة حالات تشغيل التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-RUN-CANCEL -->

</details>

### 5.2 US-BC03-RUN-REPRODUCE — إعادة إنتاج تشغيل التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-RUN-REPRODUCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-runs/{id}/actions/reproduce` | — |
| الأمر | `CMD-RUN-REPRODUCE` | إعادة إنتاج تشغيل التحليل |
| السياسة | `POL-RUN-REPRODUCE` | Analyst (submit, reproduce, cancel)؛ tenant match; case visible; label rules |
| الحدث | `EVT-RUN-QUEUED` | يصل إلى: Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| الكيان | `AGG-ANALYSIS-RUN` | تشغيل التحليل |
| الجدول | `intelligence.analysis_runs` | الجدول الرئيسي لتشغيل التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-002، REQ-ANL-003، REQ-ANL-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS | دورة حالات تشغيل التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-RUN-REPRODUCE -->

</details>

### 5.3 US-BC03-RUN-SUBMIT — تقديم تشغيل التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-RUN-SUBMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-runs` | — |
| الأمر | `CMD-RUN-SUBMIT` | تقديم تشغيل التحليل |
| السياسة | `POL-RUN-SUBMIT` | Analyst (submit, reproduce, cancel)؛ tenant match; case visible; label rules |
| الحدث | `EVT-RUN-QUEUED` | يصل إلى: Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| الكيان | `AGG-ANALYSIS-RUN` | تشغيل التحليل |
| الجدول | `intelligence.analysis_runs` | الجدول الرئيسي لتشغيل التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-002، REQ-ANL-003، REQ-ANL-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS | دورة حالات تشغيل التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-RUN-SUBMIT -->

</details>

### 5.4 US-DOM-ANL-RUN-RETRY — إعادة محاولة تشغيل تحليل فشل

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

<!-- BEGIN GENERATED: refs US-DOM-ANL-RUN-RETRY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `analysis-reproducibility-spec.md §3` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-004 | The system shall execute long-running analysis runs as asynchronous jobs with status, progress, cancellation… |
| حالة الاستخدام | UC-013 | Execute Analysis |
<!-- END GENERATED: refs US-DOM-ANL-RUN-RETRY -->

</details>

### 5.5 US-BC03-Q-RUN-ARTIFACT — جلب: Short-lived download target for a result artifact

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

<!-- BEGIN GENERATED: refs US-BC03-Q-RUN-ARTIFACT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-runs/{run_id}/artifact-grants` | — |
| الاستعلام | `QRY-RUN-ARTIFACT` | Short-lived download target for a result artifact |
| السياسة | `POL-RUN-ARTIFACT` | run label rule; audited |
| الكيان | `AGG-ANALYSIS-RUN` | تشغيل التحليل |
| الجدول | `intelligence.analysis_runs` | الجدول الرئيسي لتشغيل التحليل |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-ANL-002 | When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and ver… |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS | دورة حالات تشغيل التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-Q-RUN-ARTIFACT -->

</details>

### 5.6 US-BC03-Q-RUN-GET — جلب: Run with pins, parameters, steps, status, artifacts, reproduction report

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

<!-- BEGIN GENERATED: refs US-BC03-Q-RUN-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/analysis-runs/{run_id}` | — |
| الاستعلام | `QRY-RUN-GET` | Run with pins, parameters, steps, status, artifacts, reproduction report |
| السياسة | `POL-RUN-GET` | run label rule |
| الكيان | `AGG-ANALYSIS-RUN` | تشغيل التحليل |
| الجدول | `intelligence.analysis_runs` | الجدول الرئيسي لتشغيل التحليل |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-ANL-002 | When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and ver… |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS | دورة حالات تشغيل التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-Q-RUN-GET -->

</details>

### 5.7 US-BC03-S-ANALYSIS-RUN-01 — تلقائي: worker lease acquired (تشغيل التحليل)

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

<!-- BEGIN GENERATED: refs US-BC03-S-ANALYSIS-RUN-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:worker lease acquired` | executes with the submitter's authorization (visibility), never with system privileges |
| الانتقال | QUEUED ← RUNNING | — |
| الحدث | `EVT-RUN-STARTED` | يصل إلى: Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| الكيان | `AGG-ANALYSIS-RUN` | تشغيل التحليل |
| الجدول | `intelligence.analysis_runs` | الجدول الرئيسي لتشغيل التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-002، REQ-ANL-003، REQ-ANL-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS | دورة حالات تشغيل التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-S-ANALYSIS-RUN-01 -->

</details>

### 5.8 US-BC03-S-ANALYSIS-RUN-02 — تلقائي: completed (تشغيل التحليل)

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

<!-- BEGIN GENERATED: refs US-BC03-S-ANALYSIS-RUN-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:completed` | results stored as hashed artifacts; steps log; lineage record written (inputs+known_at, method version, image… |
| الانتقال | RUNNING ← SUCCEEDED | — |
| الحدث | `EVT-RUN-SUCCEEDED` | يصل إلى: Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| الكيان | `AGG-ANALYSIS-RUN` | تشغيل التحليل |
| الجدول | `intelligence.analysis_runs` | الجدول الرئيسي لتشغيل التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-002، REQ-ANL-003، REQ-ANL-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS | دورة حالات تشغيل التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-S-ANALYSIS-RUN-02 -->

</details>

### 5.9 US-BC03-S-ANALYSIS-RUN-03 — تلقائي: error or timeout (تشغيل التحليل)

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

<!-- BEGIN GENERATED: refs US-BC03-S-ANALYSIS-RUN-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:error or timeout` | error recorded; partial artifacts discarded |
| الانتقال | RUNNING ← FAILED | — |
| الحدث | `EVT-RUN-FAILED` | يصل إلى: Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| الكيان | `AGG-ANALYSIS-RUN` | تشغيل التحليل |
| الجدول | `intelligence.analysis_runs` | الجدول الرئيسي لتشغيل التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-002، REQ-ANL-003، REQ-ANL-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-013 | Execute Analysis |
| الاختبار | TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS | دورة حالات تشغيل التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-S-ANALYSIS-RUN-03 -->

</details>

### 5.10 US-UI-SCR30-REPRODUCE-REPORT — عرض تقرير إعادة الإنتاج وما اختلف

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

<!-- BEGIN GENERATED: refs US-UI-SCR30-REPRODUCE-REPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-30 | شاشة الحالة التحليلية والتشغيلات |
| المصدر | `analysis-reproducibility-spec.md §2` | — |
| المتطلب | REQ-ANL-003 | When a recorded analysis run is re-executed with the same recorded inputs, the system shall produce the same… |
| حالة الاستخدام | UC-013 | Execute Analysis |
<!-- END GENERATED: refs US-UI-SCR30-REPRODUCE-REPORT -->

</details>

### 5.11 US-UI-SCR30-RUN-PROGRESS — عرض تقدم التشغيل وإلغاؤه وسبب فشله

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

<!-- BEGIN GENERATED: refs US-UI-SCR30-RUN-PROGRESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-30 | شاشة الحالة التحليلية والتشغيلات |
| المصدر | `23-crosscutting.md §6` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-004 | The system shall execute long-running analysis runs as asynchronous jobs with status, progress, cancellation… |
| حالة الاستخدام | UC-013 | Execute Analysis |
<!-- END GENERATED: refs US-UI-SCR30-RUN-PROGRESS -->

</details>

### 5.12 US-PLT-ANL-REPRO-CHECK — فحص دوري لقابلية إعادة إنتاج التشغيلات

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

<!-- BEGIN GENERATED: refs US-PLT-ANL-REPRO-CHECK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-TRC-002 | re-executes a recorded deterministic analysis run → 100 % |
| المصدر | `analysis-reproducibility-spec.md §2` | — |
| المتطلب | REQ-ANL-003 | When a recorded analysis run is re-executed with the same recorded inputs, the system shall produce the same… |
| حالة الاستخدام | UC-013 | Execute Analysis |
<!-- END GENERATED: refs US-PLT-ANL-REPRO-CHECK -->

</details>

### 5.13 US-PLT-ANL-RUN-DELEGATION — تشغيل التحليل بصلاحيات مقدّمه فقط

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

<!-- BEGIN GENERATED: refs US-PLT-ANL-RUN-DELEGATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-013 | run submitted by user U → run reads only data visible to U; results labelled ≥ max input label |
| المصدر | `THR-S07-01` | — |
| المصدر | `analysis-reproducibility-spec.md §3` | — |
<!-- END GENERATED: refs US-PLT-ANL-RUN-DELEGATION -->

</details>

### 5.14 US-PLT-ANL-RUN-FAIRSHARE — توزيع عادل للحوسبة بحصة لكل مستأجر

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

<!-- BEGIN GENERATED: refs US-PLT-ANL-RUN-FAIRSHARE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-020 | tenant submits 100 runs → no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s |
| القرار التقني | TD-12 | Kubernetes Jobs with Kueue (fair sharing, per-tenant quotas); images from internal Harbor registry, signed (c… |
| المصدر | `THR-S07-06` | — |
| المصدر | `22-deployment-design.md §3` | — |
<!-- END GENERATED: refs US-PLT-ANL-RUN-FAIRSHARE -->

</details>

### 5.15 US-PLT-ANL-RUN-STATUS — متابعة حالة التشغيل وتقدمه بالسحب والاشتراك

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

<!-- BEGIN GENERATED: refs US-PLT-ANL-RUN-STATUS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-001 | submits a state-changing command → p95 ≤ 300 ms; p99 ≤ 1 s |
| المتطلب | REQ-ANL-004 | The system shall execute long-running analysis runs as asynchronous jobs with status, progress, cancellation… |
| حالة الاستخدام | UC-013 | Execute Analysis |
<!-- END GENERATED: refs US-PLT-ANL-RUN-STATUS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-ANL-002 | When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and ver… | كل قصص الميزة المأخوذة من المواصفة (8) | TST-ANALYSIS-METHOD-SM، TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS |
| REQ-ANL-003 | When a recorded analysis run is re-executed with the same recorded inputs, the system shall produce the same… | `US-BC03-RUN-CANCEL`، `US-BC03-RUN-REPRODUCE`، `US-BC03-RUN-SUBMIT`، `US-BC03-S-ANALYSIS-RUN-01`، `US-BC03-S-ANALYSIS-RUN-02`، `US-BC03-S-ANALYSIS-RUN-03`، `US-PLT-ANL-REPRO-CHECK`، `US-UI-SCR30-REPRODUCE-REPORT` | TST-ANALYSIS-METHOD-SM، TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS |
| REQ-ANL-004 | The system shall execute long-running analysis runs as asynchronous jobs with status, progress, cancellation… | `US-BC03-RUN-CANCEL`، `US-BC03-RUN-REPRODUCE`، `US-BC03-RUN-SUBMIT`، `US-BC03-S-ANALYSIS-RUN-01`، `US-BC03-S-ANALYSIS-RUN-02`، `US-BC03-S-ANALYSIS-RUN-03`، `US-DOM-ANL-RUN-RETRY`، `US-PLT-ANL-RUN-STATUS`، `US-UI-SCR30-RUN-PROGRESS` | TST-ANALYSIS-RUN-SM، TST-SLC07-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
