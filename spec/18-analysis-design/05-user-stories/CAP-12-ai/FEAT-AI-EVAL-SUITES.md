---
id: FEAT-AI-EVAL-SUITES
type: feature
title: "حزم تقييم الذكاء الاصطناعي"
status: DRAFT
version: "0.1"
capability: CAP-12.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# حزم تقييم الذكاء الاصطناعي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-AI-EVAL-SUITES |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-12 المساعدة بالذكاء الاصطناعي |
| القدرة الفرعية | CAP-12.04 تقييم AI وحوكمته (R2) |
| الأدوار | مهندس الذكاء الاصطناعي وحوكمته؛ صاحب السلطة أو المعتمِد الثاني؛ النظام |
| الشاشات | SCR-51 النماذج والتوجيه والأدوات والاستهلاك |
| حالات الاستخدام | UC-076 |
| القصص | 8: 4 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يحدد معايير ثابتة ومعتمدة لقياس جودة النماذج كالتأريض ودقة الاستشهاد ومعدل الهلوسة.

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
| QAS-AI-004 | prompt-injection, exfiltration and unauthorized-retrieval suites | 0 unauthorized retrievals, 0 tool abuse, 0 cross-tenant leakage |
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
| `US-BC07-EVS-ACTIVATE` | تفعيل حزمة التقييم | أمر | مسودة |
| `US-BC07-EVS-DRAFT` | إعداد مسودة حزمة التقييم | أمر | مسودة |
| `US-BC07-EVS-EDIT` | تعديل حزمة التقييم | أمر | مسودة |
| `US-DOM-AI-THRESHOLD-CALIBRATE` | معايرة عتبات التأريض باعتماد موثق | أمر | مسودة |
| `US-BC07-S-EVAL-SUITE-01` | تلقائي: successor activated (حزمة التقييم) | نظام | مسودة |
| `US-UI-SCR51-EVAL-SUITES` | مراجعة اكتمال حزمة التقييم قبل تفعيلها | واجهة | مسودة |
| `US-PLT-AI-EVAL-HARNESS` | تشغيل حزمة التقييم على إصدار نموذج | منصة | مسودة |
| `US-OPS-AI-SECURITY-SUITE-GATE` | تشغيل حزم أمن الذكاء الاصطناعي قبل كل إصدار | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-EVS-ACTIVATE — تفعيل حزمة التقييم

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

<!-- BEGIN GENERATED: refs US-BC07-EVS-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/evaluation-suites/{id}/actions/activate` | — |
| الأمر | `CMD-EVS-ACTIVATE` | تفعيل حزمة التقييم |
| السياسة | `POL-EVS-ACTIVATE` | AI governance (draft, edit) · second authority (activate)؛ tenant match; object visible |
| الحدث | `EVT-EVS-ACTIVATED` | يصل إلى: Evaluation runner |
| الكيان | `AGG-EVAL-SUITE` | حزمة التقييم |
| الجدول | `ai.eval_suites` | الجدول الرئيسي لحزمة التقييم |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-010 | When a model version is proposed for production, the system shall require evaluation results for groundedness… |
| حالة الاستخدام | UC-076 | Manage AI Evaluation Suites |
| الاختبار | TST-EVAL-SUITE-SM، TST-SLC10-INVARIANTS | دورة حالات حزمة التقييم، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-EVS-ACTIVATE -->

</details>

### 5.2 US-BC07-EVS-DRAFT — إعداد مسودة حزمة التقييم

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

<!-- BEGIN GENERATED: refs US-BC07-EVS-DRAFT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/evaluation-suites` | — |
| الأمر | `CMD-EVS-DRAFT` | إعداد مسودة حزمة التقييم |
| السياسة | `POL-EVS-DRAFT` | AI governance (draft, edit) · second authority (activate)؛ tenant match; object visible |
| الحدث | `EVT-EVS-DRAFTED` | يصل إلى: Evaluation runner |
| الكيان | `AGG-EVAL-SUITE` | حزمة التقييم |
| الجدول | `ai.eval_suites` | الجدول الرئيسي لحزمة التقييم |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-010 | When a model version is proposed for production, the system shall require evaluation results for groundedness… |
| حالة الاستخدام | UC-076 | Manage AI Evaluation Suites |
| الاختبار | TST-EVAL-SUITE-SM، TST-SLC10-INVARIANTS | دورة حالات حزمة التقييم، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-EVS-DRAFT -->

</details>

### 5.3 US-BC07-EVS-EDIT — تعديل حزمة التقييم

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

<!-- BEGIN GENERATED: refs US-BC07-EVS-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/evaluation-suites/{id}/actions/edit` | — |
| الأمر | `CMD-EVS-EDIT` | تعديل حزمة التقييم |
| السياسة | `POL-EVS-EDIT` | AI governance (draft, edit) · second authority (activate)؛ tenant match; object visible |
| الحدث | `EVT-EVS-EDITED` | يصل إلى: Evaluation runner |
| الكيان | `AGG-EVAL-SUITE` | حزمة التقييم |
| الجدول | `ai.eval_suites` | الجدول الرئيسي لحزمة التقييم |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-010 | When a model version is proposed for production, the system shall require evaluation results for groundedness… |
| حالة الاستخدام | UC-076 | Manage AI Evaluation Suites |
| الاختبار | TST-EVAL-SUITE-SM، TST-SLC10-INVARIANTS | دورة حالات حزمة التقييم، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-EVS-EDIT -->

</details>

### 5.4 US-DOM-AI-THRESHOLD-CALIBRATE — معايرة عتبات التأريض باعتماد موثق

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

<!-- BEGIN GENERATED: refs US-DOM-AI-THRESHOLD-CALIBRATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `03-domain/contexts/BC07/grounded-ai-spec.md §4` | — |
| المصدر | `RSK-027` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-AI-003 | If the retrieved evidence is insufficient to answer, then the system shall return 'Insufficient Evidence' ins… |
| حالة الاستخدام | UC-072 | Generate AI Result |
<!-- END GENERATED: refs US-DOM-AI-THRESHOLD-CALIBRATE -->

</details>

### 5.5 US-BC07-S-EVAL-SUITE-01 — تلقائي: successor activated (حزمة التقييم)

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

<!-- BEGIN GENERATED: refs US-BC07-S-EVAL-SUITE-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:successor activated` | system |
| الانتقال | ACTIVE ← SUPERSEDED | — |
| الحدث | `EVT-EVS-SUPERSEDED` | يصل إلى: Evaluation runner |
| الكيان | `AGG-EVAL-SUITE` | حزمة التقييم |
| الجدول | `ai.eval_suites` | الجدول الرئيسي لحزمة التقييم |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-010 | When a model version is proposed for production, the system shall require evaluation results for groundedness… |
| حالة الاستخدام | UC-076 | Manage AI Evaluation Suites |
| الاختبار | TST-EVAL-SUITE-SM، TST-SLC10-INVARIANTS | دورة حالات حزمة التقييم، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-EVAL-SUITE-01 -->

</details>

### 5.6 US-UI-SCR51-EVAL-SUITES — مراجعة اكتمال حزمة التقييم قبل تفعيلها

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

<!-- BEGIN GENERATED: refs US-UI-SCR51-EVAL-SUITES -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-076 | Manage AI Evaluation Suites |
| المصدر | `US-BC07-EVS-EDIT` | — |
| الشاشة | SCR-51 | شاشة النماذج والتوجيه والأدوات والاستهلاك |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR51-EVAL-SUITES -->

</details>

### 5.7 US-PLT-AI-EVAL-HARNESS — تشغيل حزمة التقييم على إصدار نموذج

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

<!-- BEGIN GENERATED: refs US-PLT-AI-EVAL-HARNESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AI-001 | evaluation set of 500 questions → ≥ 95 % of cited items actually support the statement |
| الجودة | QAS-AI-002 | insufficient-evidence and hallucination sets → ≤ 2 % unsupported statements; ≥ 95 % correct 'Insufficient Evi… |
| المصدر | `US-BC07-MDL-START-EVALUATION` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-AI-010 | When a model version is proposed for production, the system shall require evaluation results for groundedness… |
| حالة الاستخدام | UC-076 | Manage AI Evaluation Suites |
<!-- END GENERATED: refs US-PLT-AI-EVAL-HARNESS -->

</details>

### 5.8 US-OPS-AI-SECURITY-SUITE-GATE — تشغيل حزم أمن الذكاء الاصطناعي قبل كل إصدار

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-AI-SECURITY-SUITE-GATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AI-004 | prompt-injection, exfiltration and unauthorized-retrieval suites → 0 unauthorized retrievals, 0 tool abuse, 0… |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-AI-012، REQ-AI-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-071 | Retrieve Authorized Context |
<!-- END GENERATED: refs US-OPS-AI-SECURITY-SUITE-GATE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-AI-002 | The system shall build context packages only from data retrieved with the requesting user's authorization, in… | `US-OPS-AI-SECURITY-SUITE-GATE` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-003 | If the retrieved evidence is insufficient to answer, then the system shall return 'Insufficient Evidence' ins… | `US-DOM-AI-THRESHOLD-CALIBRATE` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-010 | When a model version is proposed for production, the system shall require evaluation results for groundedness… | `US-BC07-EVS-ACTIVATE`، `US-BC07-EVS-DRAFT`، `US-BC07-EVS-EDIT`، `US-BC07-S-EVAL-SUITE-01`، `US-PLT-AI-EVAL-HARNESS` | TST-EVAL-SUITE-SM، TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS |
| REQ-AI-012 | If content retrieved into a context package contains instructions, then the system shall treat it as data and… | `US-OPS-AI-SECURITY-SUITE-GATE` | TST-AI-REQUEST-SM، TST-AI-TOOL-SM، TST-SLC10-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
