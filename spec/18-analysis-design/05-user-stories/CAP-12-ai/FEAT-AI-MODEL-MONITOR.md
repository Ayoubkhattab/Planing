---
id: FEAT-AI-MODEL-MONITOR
type: feature
title: "مراقبة النماذج وإيقافها"
status: DRAFT
version: "0.1"
capability: CAP-12.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مراقبة النماذج وإيقافها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-AI-MODEL-MONITOR |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-12 المساعدة بالذكاء الاصطناعي |
| القدرة الفرعية | CAP-12.04 تقييم AI وحوكمته (R2) |
| الأدوار | مهندس الذكاء الاصطناعي وحوكمته؛ النظام |
| الشاشات | SCR-51 النماذج والتوجيه والأدوات والاستهلاك |
| حالات الاستخدام | UC-075 |
| القصص | 9: 5 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

ينبه إلى تراجع أداء النموذج أثناء التشغيل ويتيح إيقاف استخدامه أو إعادته أو إحالته إلى التقاعد.

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
| QAS-AI-001 | evaluation set of 500 questions | ≥ 95 % of cited items actually support the statement |
| QAS-AI-002 | insufficient-evidence and hallucination sets | ≤ 2 % unsupported statements; ≥ 95 % correct 'Insufficient Evidence' |
| QAS-AI-003 | grounded Q&A request | first token ≤ 3 s, full answer p95 ≤ 20 s on local models |
| QAS-AI-005 | AI usage per tenant | GPU-hours and cost per request reported per tenant |
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
| `US-BC07-MDL-DEPRECATE` | إهمال إصدار النموذج (إيقاف الاستخدام الجديد) | أمر | مسودة |
| `US-BC07-MDL-REINSTATE` | إعادة إصدار النموذج إلى السريان | أمر | مسودة |
| `US-BC07-MDL-RETIRE` | إحالة إصدار النموذج إلى التقاعد | أمر | مسودة |
| `US-BC07-Q-AI-USAGE` | جلب: GPU-hours, requests, cost indicators per tenant and operation | جلب | مسودة |
| `US-BC07-S-MODEL-VERSION-01` | تلقائي: monitoring drift detected (إصدار النموذج) | نظام | مسودة |
| `US-UI-SCR51-USAGE` | متابعة استهلاك الذكاء الاصطناعي وتكلفته | واجهة | مسودة |
| `US-PLT-AI-USAGE-METERING` | قياس ساعات GPU والطلبات لكل مستأجر | منصة | مسودة |
| `US-OPS-AI-DRIFT-SAMPLE` | عينة تقييم أسبوعية للنموذج في الإنتاج | تشغيل | مسودة |
| `US-OPS-AI-QUALITY-ALERTS` | التنبيه إلى تراجع جودة النموذج أو سرعته | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-MDL-DEPRECATE — إهمال إصدار النموذج (إيقاف الاستخدام الجديد)

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

<!-- BEGIN GENERATED: refs US-BC07-MDL-DEPRECATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/models/{id}/actions/deprecate` | — |
| الأمر | `CMD-MDL-DEPRECATE` | إهمال إصدار النموذج (إيقاف الاستخدام الجديد) |
| السياسة | `POL-MDL-DEPRECATE` | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, rein… |
| الحدث | `EVT-MDL-DEPRECATED` | يصل إلى: Inference servers (load/unload); Routing validation |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-MDL-DEPRECATE -->

</details>

### 5.2 US-BC07-MDL-REINSTATE — إعادة إصدار النموذج إلى السريان

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

<!-- BEGIN GENERATED: refs US-BC07-MDL-REINSTATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/models/{id}/actions/reinstate` | — |
| الأمر | `CMD-MDL-REINSTATE` | إعادة إصدار النموذج إلى السريان |
| السياسة | `POL-MDL-REINSTATE` | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, rein… |
| الحدث | `EVT-MDL-REINSTATED` | يصل إلى: Inference servers (load/unload); Routing validation |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-MDL-REINSTATE -->

</details>

### 5.3 US-BC07-MDL-RETIRE — إحالة إصدار النموذج إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC07-MDL-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/models/{id}/actions/retire` | — |
| الأمر | `CMD-MDL-RETIRE` | إحالة إصدار النموذج إلى التقاعد |
| السياسة | `POL-MDL-RETIRE` | AI governance authority (retire)؛ tenant match; object visible |
| الحدث | `EVT-MDL-RETIRED` | يصل إلى: Inference servers (load/unload); Routing validation |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-MDL-RETIRE -->

</details>

### 5.4 US-BC07-Q-AI-USAGE — جلب: GPU-hours, requests, cost indicators per tenant and operation

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

<!-- BEGIN GENERATED: refs US-BC07-Q-AI-USAGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/ai/usage` | — |
| الاستعلام | `QRY-AI-USAGE` | GPU-hours, requests, cost indicators per tenant and operation |
| السياسة | `POL-AI-USAGE` | Administrator, finance |
| المتطلب | REQ-AI-001 | The system shall process every AI request through identity, policy, authorized retrieval, context package, mo… |
| حالات الاستخدام | UC-070، UC-071، UC-072 | Submit AI Request؛ Retrieve Authorized Context؛ Generate AI Result |
<!-- END GENERATED: refs US-BC07-Q-AI-USAGE -->

</details>

### 5.5 US-BC07-S-MODEL-VERSION-01 — تلقائي: monitoring drift detected (إصدار النموذج)

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

<!-- BEGIN GENERATED: refs US-BC07-S-MODEL-VERSION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:monitoring drift detected` | weekly evaluation sample below threshold → alert, route review |
| الانتقال | PRODUCTION ← (بلا تغيير) | — |
| الحدث | `EVT-MDL-DRIFT-DETECTED` | يصل إلى: Inference servers (load/unload); Routing validation |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-MODEL-VERSION-01 -->

</details>

### 5.6 US-UI-SCR51-USAGE — متابعة استهلاك الذكاء الاصطناعي وتكلفته

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR51-USAGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AI-005 | AI usage per tenant → GPU-hours and cost per request reported per tenant |
| المصدر | `US-BC07-Q-AI-USAGE` | — |
| الشاشة | SCR-51 | شاشة النماذج والتوجيه والأدوات والاستهلاك |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR51-USAGE -->

</details>

### 5.7 US-PLT-AI-USAGE-METERING — قياس ساعات GPU والطلبات لكل مستأجر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-AI-USAGE-METERING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AI-005 | AI usage per tenant → GPU-hours and cost per request reported per tenant |
| المصدر | `03-domain/contexts/BC07/grounded-ai-spec.md §7` | — |
| المصدر | `22-deployment-design.md §12` | — |
<!-- END GENERATED: refs US-PLT-AI-USAGE-METERING -->

</details>

### 5.8 US-OPS-AI-DRIFT-SAMPLE — عينة تقييم أسبوعية للنموذج في الإنتاج

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

<!-- BEGIN GENERATED: refs US-OPS-AI-DRIFT-SAMPLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/fmea-slc10.md FM-S10-04` | — |
| المصدر | `US-BC07-S-MODEL-VERSION-01` | — |
<!-- END GENERATED: refs US-OPS-AI-DRIFT-SAMPLE -->

</details>

### 5.9 US-OPS-AI-QUALITY-ALERTS — التنبيه إلى تراجع جودة النموذج أو سرعته

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

<!-- BEGIN GENERATED: refs US-OPS-AI-QUALITY-ALERTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/observability-slc10.md` | — |
| الجودة | QAS-AI-003 | grounded Q&A request → first token ≤ 3 s, full answer p95 ≤ 20 s on local models |
<!-- END GENERATED: refs US-OPS-AI-QUALITY-ALERTS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-AI-001 | The system shall process every AI request through identity, policy, authorized retrieval, context package, mo… | `US-BC07-Q-AI-USAGE` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-009 | The system shall manage models through the lifecycle REGISTERED, EVALUATING, APPROVED, STAGED, PRODUCTION, MO… | كل قصص الأوامر والنظام في الميزة (4) | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS |
| REQ-AI-010 | When a model version is proposed for production, the system shall require evaluation results for groundedness… | كل قصص الأوامر والنظام في الميزة (4) | TST-EVAL-SUITE-SM، TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
