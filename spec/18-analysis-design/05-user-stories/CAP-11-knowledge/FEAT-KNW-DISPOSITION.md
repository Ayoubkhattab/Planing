---
id: FEAT-KNW-DISPOSITION
type: feature
title: "إتلاف السجلات المنتهية"
status: DRAFT
version: "0.1"
capability: CAP-11.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إتلاف السجلات المنتهية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-KNW-DISPOSITION |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-11 المعرفة والذاكرة المؤسسية |
| القدرة الفرعية | CAP-11.02 السجلات والاحتفاظ (R1 (الاحتفاظ والتجميد)) |
| الأدوار | أمين الأرشيف؛ السلطة القانونية والامتثال؛ المدقِّق؛ النظام |
| الشاشات | SCR-70 الاحتفاظ والحجز القانوني والإتلاف والمحو |
| حالات الاستخدام | UC-103 |
| القصص | 13: 8 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

ينفذ إتلاف أو أرشفة السجلات التي انتهت مدة حفظها بموافقة جهة مستقلة وبشهادة موثقة، مع استثناء المجمد منها.

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
| QAS-GOV-001 | daily disposition evaluation | candidates computed ≤ 1 h; 0 held records destroyed |
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
| `US-BC08-DSP-APPROVE` | اعتماد تشغيل الإتلاف | أمر | مسودة |
| `US-BC08-DSP-CANCEL` | إلغاء تشغيل الإتلاف | أمر | مسودة |
| `US-BC08-DSP-SUBMIT` | تقديم تشغيل الإتلاف | أمر | مسودة |
| `US-BC08-Q-DSP-GET` | جلب: Run with candidate summary, exceptions and certificate | جلب | مسودة |
| `US-BC08-S-DISPOSITION-RUN-01` | تلقائي: scheduled evaluation (daily) (تشغيل الإتلاف) | نظام | مسودة |
| `US-BC08-S-DISPOSITION-RUN-02` | تلقائي: execution started (تشغيل الإتلاف) | نظام | مسودة |
| `US-BC08-S-DISPOSITION-RUN-03` | تلقائي: all buckets processed (تشغيل الإتلاف) | نظام | مسودة |
| `US-BC08-S-DISPOSITION-RUN-04` | تلقائي: some buckets failed (تشغيل الإتلاف) | نظام | مسودة |
| `US-UI-SCR70-DISPOSITION-RUN` | مراجعة دورة الإتلاف قبل اعتمادها | واجهة | مسودة |
| `US-PLT-DISPOSITION-EVAL-1H` | حساب مرشحي الإتلاف اليومي خلال ساعة | منصة | مسودة |
| `US-PLT-DISPOSITION-PURGE-COPIES` | إزالة نسخ السجلات المتلفة من الفهارس والذاكرات | منصة | مسودة |
| `US-OPS-DISPOSITION-CERT-EVIDENCE` | حفظ شهادة الإتلاف دليلًا غير قابل للتغيير | تشغيل | مسودة |
| `US-OPS-DISPOSITION-FAILURE-ALERT` | التنبيه إلى فشل إتلاف بعض الحاويات | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC08-DSP-APPROVE — اعتماد تشغيل الإتلاف

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

<!-- BEGIN GENERATED: refs US-BC08-DSP-APPROVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/disposition-runs/{id}/actions/approve` | — |
| الأمر | `CMD-DSP-APPROVE` | اعتماد تشغيل الإتلاف |
| السياسة | `POL-DSP-APPROVE` | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)؛ tenant match |
| الحدث | `EVT-DSP-APPROVED` | يصل إلى: Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| الكيان | `AGG-DISPOSITION-RUN` | تشغيل الإتلاف |
| الجدول | `governance.disposition_runs` | الجدول الرئيسي لتشغيل الإتلاف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-006، REQ-GOV-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-DISPOSITION-RUN-SM | دورة حالات تشغيل الإتلاف، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-DSP-APPROVE -->

</details>

### 5.2 US-BC08-DSP-CANCEL — إلغاء تشغيل الإتلاف

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

<!-- BEGIN GENERATED: refs US-BC08-DSP-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/disposition-runs/{id}/actions/cancel` | — |
| الأمر | `CMD-DSP-CANCEL` | إلغاء تشغيل الإتلاف |
| السياسة | `POL-DSP-CANCEL` | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)؛ tenant match |
| الحدث | `EVT-DSP-CANCELLED` | يصل إلى: Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| الكيان | `AGG-DISPOSITION-RUN` | تشغيل الإتلاف |
| الجدول | `governance.disposition_runs` | الجدول الرئيسي لتشغيل الإتلاف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-006، REQ-GOV-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-DISPOSITION-RUN-SM | دورة حالات تشغيل الإتلاف، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-DSP-CANCEL -->

</details>

### 5.3 US-BC08-DSP-SUBMIT — تقديم تشغيل الإتلاف

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

<!-- BEGIN GENERATED: refs US-BC08-DSP-SUBMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/disposition-runs/{id}/actions/submit` | — |
| الأمر | `CMD-DSP-SUBMIT` | تقديم تشغيل الإتلاف |
| السياسة | `POL-DSP-SUBMIT` | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)؛ tenant match |
| الحدث | `EVT-DSP-SUBMITTED` | يصل إلى: Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| الكيان | `AGG-DISPOSITION-RUN` | تشغيل الإتلاف |
| الجدول | `governance.disposition_runs` | الجدول الرئيسي لتشغيل الإتلاف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-006، REQ-GOV-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-DISPOSITION-RUN-SM | دورة حالات تشغيل الإتلاف، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-DSP-SUBMIT -->

</details>

### 5.4 US-BC08-Q-DSP-GET — جلب: Run with candidate summary, exceptions and certificate

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

<!-- BEGIN GENERATED: refs US-BC08-Q-DSP-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/governance/disposition-runs/{run_id}` | — |
| الاستعلام | `QRY-DSP-GET` | Run with candidate summary, exceptions and certificate |
| السياسة | `POL-DSP-GET` | Archivist, Legal, Auditor |
| الكيان | `AGG-DISPOSITION-RUN` | تشغيل الإتلاف |
| الجدول | `governance.disposition_runs` | الجدول الرئيسي لتشغيل الإتلاف |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-006 | The system shall apply a retention schedule to every record class. |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-DISPOSITION-RUN-SM | دورة حالات تشغيل الإتلاف، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-Q-DSP-GET -->

</details>

### 5.5 US-BC08-S-DISPOSITION-RUN-01 — تلقائي: scheduled evaluation (daily) (تشغيل الإتلاف)

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

<!-- BEGIN GENERATED: refs US-BC08-S-DISPOSITION-RUN-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:scheduled evaluation (daily)` | candidates = key buckets whose records are all past retention under the ACTIVE schedule; held items identifie… |
| الانتقال | ∅ ← PLANNED | — |
| الحدث | `EVT-DSP-PLANNED` | يصل إلى: Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| الكيان | `AGG-DISPOSITION-RUN` | تشغيل الإتلاف |
| الجدول | `governance.disposition_runs` | الجدول الرئيسي لتشغيل الإتلاف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-006، REQ-GOV-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-DISPOSITION-RUN-SM | دورة حالات تشغيل الإتلاف، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-S-DISPOSITION-RUN-01 -->

</details>

### 5.6 US-BC08-S-DISPOSITION-RUN-02 — تلقائي: execution started (تشغيل الإتلاف)

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

<!-- BEGIN GENERATED: refs US-BC08-S-DISPOSITION-RUN-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:execution started` | held items in each bucket re-wrapped under hold keys first; then bucket keys destroyed; owners notified to pu… |
| الانتقال | APPROVED ← EXECUTING | — |
| الحدث | `EVT-DSP-EXECUTING` | يصل إلى: Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| الكيان | `AGG-DISPOSITION-RUN` | تشغيل الإتلاف |
| الجدول | `governance.disposition_runs` | الجدول الرئيسي لتشغيل الإتلاف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-006، REQ-GOV-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-DISPOSITION-RUN-SM | دورة حالات تشغيل الإتلاف، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-S-DISPOSITION-RUN-02 -->

</details>

### 5.7 US-BC08-S-DISPOSITION-RUN-03 — تلقائي: all buckets processed (تشغيل الإتلاف)

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

<!-- BEGIN GENERATED: refs US-BC08-S-DISPOSITION-RUN-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:all buckets processed` | certificate issued (buckets, key ids destroyed, counts, holds excluded) |
| الانتقال | EXECUTING ← COMPLETED | — |
| الحدث | `EVT-DSP-COMPLETED` | يصل إلى: Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| الكيان | `AGG-DISPOSITION-RUN` | تشغيل الإتلاف |
| الجدول | `governance.disposition_runs` | الجدول الرئيسي لتشغيل الإتلاف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-006، REQ-GOV-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-DISPOSITION-RUN-SM | دورة حالات تشغيل الإتلاف، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-S-DISPOSITION-RUN-03 -->

</details>

### 5.8 US-BC08-S-DISPOSITION-RUN-04 — تلقائي: some buckets failed (تشغيل الإتلاف)

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

<!-- BEGIN GENERATED: refs US-BC08-S-DISPOSITION-RUN-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:some buckets failed` | failed buckets listed; retried next run |
| الانتقال | EXECUTING ← COMPLETED_WITH_EXCEPTIONS | — |
| الحدث | `EVT-DSP-COMPLETED-WITH-EXCEPTIONS` | يصل إلى: Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| الكيان | `AGG-DISPOSITION-RUN` | تشغيل الإتلاف |
| الجدول | `governance.disposition_runs` | الجدول الرئيسي لتشغيل الإتلاف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-006، REQ-GOV-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-DISPOSITION-RUN-SM | دورة حالات تشغيل الإتلاف، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-S-DISPOSITION-RUN-04 -->

</details>

### 5.9 US-UI-SCR70-DISPOSITION-RUN — مراجعة دورة الإتلاف قبل اعتمادها

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

<!-- BEGIN GENERATED: refs US-UI-SCR70-DISPOSITION-RUN -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الشاشة | SCR-70 | شاشة الاحتفاظ والحجز القانوني والإتلاف والمحو |
| المصدر | `US-BC08-Q-DSP-GET` | — |
| المصدر | `THR-S12-01` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR70-DISPOSITION-RUN -->

</details>

### 5.10 US-PLT-DISPOSITION-EVAL-1H — حساب مرشحي الإتلاف اليومي خلال ساعة

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

<!-- BEGIN GENERATED: refs US-PLT-DISPOSITION-EVAL-1H -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-GOV-001 | daily disposition evaluation → candidates computed ≤ 1 h; 0 held records destroyed |
| المصدر | `22-deployment-design.md §4` | — |
| المتطلب | REQ-GOV-006 | The system shall apply a retention schedule to every record class. |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
<!-- END GENERATED: refs US-PLT-DISPOSITION-EVAL-1H -->

</details>

### 5.11 US-PLT-DISPOSITION-PURGE-COPIES — إزالة نسخ السجلات المتلفة من الفهارس والذاكرات

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

<!-- BEGIN GENERATED: refs US-PLT-DISPOSITION-PURGE-COPIES -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `US-BC08-S-DISPOSITION-RUN-02` | — |
| المصدر | `THR-S12-04` | — |
| فحص البنية | FIT-11 | Projections rebuildable: rebuild yields identical results on reference set |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-DISPOSITION-PURGE-COPIES -->

</details>

### 5.12 US-OPS-DISPOSITION-CERT-EVIDENCE — حفظ شهادة الإتلاف دليلًا غير قابل للتغيير

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

<!-- BEGIN GENERATED: refs US-OPS-DISPOSITION-CERT-EVIDENCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-07 | OpenBao (MPL, open fork of Vault) Transit engine for envelope encryption; KEKs in site HSM via PKCS#11; DEKs… |
| القرار التقني | TD-06 | S3-compatible API as the contract; default implementation Ceph RGW (sites with Ceph) or MinIO (smaller cells)… |
| المصدر | `17-security-design.md §6` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-DISPOSITION-CERT-EVIDENCE -->

</details>

### 5.13 US-OPS-DISPOSITION-FAILURE-ALERT — التنبيه إلى فشل إتلاف بعض الحاويات

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

<!-- BEGIN GENERATED: refs US-OPS-DISPOSITION-FAILURE-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/fmea-slc12a.md FM-S12-01` | — |
| المصدر | `09-reliability/observability-slc12a.md` | — |
| المصدر | `US-BC08-S-DISPOSITION-RUN-04` | — |
<!-- END GENERATED: refs US-OPS-DISPOSITION-FAILURE-ALERT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-GOV-006 | The system shall apply a retention schedule to every record class. | `US-BC08-DSP-APPROVE`، `US-BC08-DSP-CANCEL`، `US-BC08-DSP-SUBMIT`، `US-BC08-Q-DSP-GET`، `US-BC08-S-DISPOSITION-RUN-01`، `US-BC08-S-DISPOSITION-RUN-02`، `US-BC08-S-DISPOSITION-RUN-03`، `US-BC08-S-DISPOSITION-RUN-04`، `US-PLT-DISPOSITION-EVAL-1H` | TST-DISPOSITION-RUN-SM، TST-RETENTION-SCHEDULE-SM، TST-SLC12A-INVARIANTS |
| REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… | كل قصص الأوامر والنظام في الميزة (7) | TST-DISPOSITION-RUN-SM، TST-LEGAL-HOLD-SM، TST-SLC12A-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
