---
id: FEAT-AI-MODEL-APPROVAL
type: feature
title: "تقييم النماذج واعتمادها"
status: DRAFT
version: "0.1"
capability: CAP-12.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تقييم النماذج واعتمادها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-AI-MODEL-APPROVAL |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-12 المساعدة بالذكاء الاصطناعي |
| القدرة الفرعية | CAP-12.04 تقييم AI وحوكمته (R2) |
| الأدوار | مهندس الذكاء الاصطناعي وحوكمته؛ المدقِّق |
| الشاشات | SCR-51 النماذج والتوجيه والأدوات والاستهلاك |
| حالات الاستخدام | UC-075 |
| القصص | 10: 7 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضمن ألا يدخل أي نموذج ذكاء اصطناعي إلى الاستخدام الفعلي إلا بعد تقييم موثق لدقته وتكلفته وموافقة بشرية.

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
| `US-BC07-MDL-APPROVE` | اعتماد إصدار النموذج | أمر | مسودة |
| `US-BC07-MDL-FAIL-EVALUATION` | تسجيل فشل تقييم إصدار النموذج | أمر | مسودة |
| `US-BC07-MDL-PROMOTE` | ترقية إصدار النموذج | أمر | مسودة |
| `US-BC07-MDL-REGISTER` | تسجيل إصدار النموذج | أمر | مسودة |
| `US-BC07-MDL-STAGE` | تجهيز إصدار النموذج للإنتاج | أمر | مسودة |
| `US-BC07-MDL-START-EVALUATION` | بدء تقييم إصدار النموذج | أمر | مسودة |
| `US-BC07-Q-MDL-LIST` | جلب: Model versions with state, evaluation summary, hosting | جلب | مسودة |
| `US-UI-SCR51-MODEL-LIFECYCLE` | متابعة إصدارات النماذج وتقييمها | واجهة | مسودة |
| `US-PLT-AI-CANARY-SPLIT` | توجيه حصة تجريبية إلى النموذج المجهز | منصة | مسودة |
| `US-OPS-AI-MODEL-BUNDLE` | تثبيت أوزان النموذج موقعة في حزمة الإصدار | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-MDL-APPROVE — اعتماد إصدار النموذج

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

<!-- BEGIN GENERATED: refs US-BC07-MDL-APPROVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/models/{id}/actions/approve` | — |
| الأمر | `CMD-MDL-APPROVE` | اعتماد إصدار النموذج |
| السياسة | `POL-MDL-APPROVE` | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, rein… |
| الحدث | `EVT-MDL-APPROVED` | يصل إلى: Inference servers (load/unload); Routing validation |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-MDL-APPROVE -->

</details>

### 5.2 US-BC07-MDL-FAIL-EVALUATION — تسجيل فشل تقييم إصدار النموذج

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

<!-- BEGIN GENERATED: refs US-BC07-MDL-FAIL-EVALUATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/models/{id}/actions/fail-evaluation` | — |
| الأمر | `CMD-MDL-FAIL-EVALUATION` | تسجيل فشل تقييم إصدار النموذج |
| السياسة | `POL-MDL-FAIL-EVALUATION` | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, rein… |
| الحدث | `EVT-MDL-EVALUATION-FAILED` | يصل إلى: Inference servers (load/unload); Routing validation |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-MDL-FAIL-EVALUATION -->

</details>

### 5.3 US-BC07-MDL-PROMOTE — ترقية إصدار النموذج

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

<!-- BEGIN GENERATED: refs US-BC07-MDL-PROMOTE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/models/{id}/actions/promote` | — |
| الأمر | `CMD-MDL-PROMOTE` | ترقية إصدار النموذج |
| السياسة | `POL-MDL-PROMOTE` | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, rein… |
| الحدث | `EVT-MDL-PROMOTED` | يصل إلى: Inference servers (load/unload); Routing validation |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-MDL-PROMOTE -->

</details>

### 5.4 US-BC07-MDL-REGISTER — تسجيل إصدار النموذج

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

<!-- BEGIN GENERATED: refs US-BC07-MDL-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/models` | — |
| الأمر | `CMD-MDL-REGISTER` | تسجيل إصدار النموذج |
| السياسة | `POL-MDL-REGISTER` | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, rein… |
| الحدث | `EVT-MDL-REGISTERED` | يصل إلى: Inference servers (load/unload); Routing validation |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-MDL-REGISTER -->

</details>

### 5.5 US-BC07-MDL-STAGE — تجهيز إصدار النموذج للإنتاج

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

<!-- BEGIN GENERATED: refs US-BC07-MDL-STAGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/models/{id}/actions/stage` | — |
| الأمر | `CMD-MDL-STAGE` | تجهيز إصدار النموذج للإنتاج |
| السياسة | `POL-MDL-STAGE` | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, rein… |
| الحدث | `EVT-MDL-STAGED` | يصل إلى: Inference servers (load/unload); Routing validation |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-MDL-STAGE -->

</details>

### 5.6 US-BC07-MDL-START-EVALUATION — بدء تقييم إصدار النموذج

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

<!-- BEGIN GENERATED: refs US-BC07-MDL-START-EVALUATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/models/{id}/actions/start-evaluation` | — |
| الأمر | `CMD-MDL-START-EVALUATION` | بدء تقييم إصدار النموذج |
| السياسة | `POL-MDL-START-EVALUATION` | AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, rein… |
| الحدث | `EVT-MDL-EVALUATION-STARTED` | يصل إلى: Inference servers (load/unload); Routing validation |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-MDL-START-EVALUATION -->

</details>

### 5.7 US-BC07-Q-MDL-LIST — جلب: Model versions with state, evaluation summary, hosting

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

<!-- BEGIN GENERATED: refs US-BC07-Q-MDL-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/ai/models` | — |
| الاستعلام | `QRY-MDL-LIST` | Model versions with state, evaluation summary, hosting |
| السياسة | `POL-MDL-LIST` | AI governance, Auditor |
| الكيان | `AGG-MODEL-VERSION` | إصدار النموذج |
| الجدول | `ai.model_versions` | الجدول الرئيسي لإصدار النموذج |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-009 | The system shall manage models through the lifecycle REGISTERED, EVALUATING, APPROVED, STAGED, PRODUCTION, MO… |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الاختبار | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS | دورة حالات إصدار النموذج، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-Q-MDL-LIST -->

</details>

### 5.8 US-UI-SCR51-MODEL-LIFECYCLE — متابعة إصدارات النماذج وتقييمها

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

<!-- BEGIN GENERATED: refs US-UI-SCR51-MODEL-LIFECYCLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
| الشاشة | SCR-51 | شاشة النماذج والتوجيه والأدوات والاستهلاك |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-AI-009، REQ-AI-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-075 | Govern AI Model Lifecycle |
<!-- END GENERATED: refs US-UI-SCR51-MODEL-LIFECYCLE -->

</details>

### 5.9 US-PLT-AI-CANARY-SPLIT — توجيه حصة تجريبية إلى النموذج المجهز

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

<!-- BEGIN GENERATED: refs US-PLT-AI-CANARY-SPLIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `US-BC07-MDL-STAGE` | — |
| المصدر | `US-BC07-MDL-PROMOTE` | — |
| المصدر | `13-verification/acceptance/SLC-10/invariants-slc10.md` | — |
<!-- END GENERATED: refs US-PLT-AI-CANARY-SPLIT -->

</details>

### 5.10 US-OPS-AI-MODEL-BUNDLE — تثبيت أوزان النموذج موقعة في حزمة الإصدار

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

<!-- BEGIN GENERATED: refs US-OPS-AI-MODEL-BUNDLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `THR-S10-05` | — |
| القرار التقني | TD-17 | Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps… |
| المصدر | `22-deployment-design.md §7` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-AI-MODEL-BUNDLE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-AI-009 | The system shall manage models through the lifecycle REGISTERED, EVALUATING, APPROVED, STAGED, PRODUCTION, MO… | `US-BC07-MDL-APPROVE`، `US-BC07-MDL-FAIL-EVALUATION`، `US-BC07-MDL-PROMOTE`، `US-BC07-MDL-REGISTER`، `US-BC07-MDL-STAGE`، `US-BC07-MDL-START-EVALUATION`، `US-BC07-Q-MDL-LIST`، `US-UI-SCR51-MODEL-LIFECYCLE` | TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS |
| REQ-AI-010 | When a model version is proposed for production, the system shall require evaluation results for groundedness… | `US-BC07-MDL-APPROVE`، `US-BC07-MDL-FAIL-EVALUATION`، `US-BC07-MDL-PROMOTE`، `US-BC07-MDL-REGISTER`، `US-BC07-MDL-STAGE`، `US-BC07-MDL-START-EVALUATION`، `US-UI-SCR51-MODEL-LIFECYCLE` | TST-EVAL-SUITE-SM، TST-MODEL-VERSION-SM، TST-SLC10-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
