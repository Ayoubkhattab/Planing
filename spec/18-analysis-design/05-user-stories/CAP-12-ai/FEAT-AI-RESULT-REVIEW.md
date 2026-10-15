---
id: FEAT-AI-RESULT-REVIEW
type: feature
title: "مراجعة نتائج الذكاء الاصطناعي"
status: DRAFT
version: "0.1"
capability: CAP-12.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مراجعة نتائج الذكاء الاصطناعي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-AI-RESULT-REVIEW |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-12 المساعدة بالذكاء الاصطناعي |
| القدرة الفرعية | CAP-12.02 الصياغة والتلخيص (R2) |
| الأدوار | المراجع؛ النظام |
| الشاشات | SCR-46 مراجعة نتيجة ذكية، SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-073، UC-074 |
| القصص | 9: 6 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضمن ألا تُعتمد أو تُنشر أي نتيجة من الذكاء الاصطناعي إلا بعد أن يراجعها إنسان ويقبلها كليًا أو جزئيًا أو يرفضها بسبب.

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
لا متطلبات جودة مرتبطة بمتطلبات هذه الميزة مباشرة. تنطبق متطلبات المنصة العامة (`FEAT-PLT-*`).
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
| `US-BC07-AIRS-ACCEPT` | قبول نتيجة الذكاء الاصطناعي | أمر | مسودة |
| `US-BC07-AIRS-ACCEPT-PARTIALLY` | قبول نتيجة الذكاء الاصطناعي جزئيًا | أمر | مسودة |
| `US-BC07-AIRS-REJECT` | رفض نتيجة الذكاء الاصطناعي | أمر | مسودة |
| `US-BC07-AIRS-START-REVIEW` | بدء مراجعة نتيجة الذكاء الاصطناعي | أمر | مسودة |
| `US-BC07-Q-AIRS-QUEUE` | جلب: Reviewable AI results by state, operation, target | جلب | مسودة |
| `US-BC07-S-AI-RESULT-01` | تلقائي: request COMPLETED for a reviewable operation (نتيجة الذكاء الاصطناعي) | نظام | مسودة |
| `US-UI-SCR06-AI-QUEUE` | قائمة نتائج الذكاء الاصطناعي المنتظرة للمراجعة | واجهة | مسودة |
| `US-UI-SCR46-ITEM-SELECT` | قبول عناصر محددة من النتيجة ورفض الباقي | واجهة | مسودة |
| `US-OPS-AI-REJECTION-FEEDBACK` | تغذية أسباب الرفض إلى تقييم النماذج | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-AIRS-ACCEPT — قبول نتيجة الذكاء الاصطناعي

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

<!-- BEGIN GENERATED: refs US-BC07-AIRS-ACCEPT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/results/{id}/actions/accept` | — |
| الأمر | `CMD-AIRS-ACCEPT` | قبول نتيجة الذكاء الاصطناعي |
| السياسة | `POL-AIRS-ACCEPT` | reviewer authorized on the target (review, accept, reject)؛ tenant match; object visible |
| الحدث | `EVT-AIRS-ACCEPTED` | يصل إلى: Owner contexts (effects on acceptance); Evaluation feedback store |
| الكيان | `AGG-AI-RESULT` | نتيجة الذكاء الاصطناعي |
| الجدول | `ai.ai_results` | الجدول الرئيسي لنتيجة الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… |
| حالات الاستخدام | UC-073، UC-074 | Review AI Result؛ Approve AI-Assisted Result |
| الاختبار | TST-AI-RESULT-SM، TST-SLC10-INVARIANTS | دورة حالات نتيجة الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-AIRS-ACCEPT -->

</details>

### 5.2 US-BC07-AIRS-ACCEPT-PARTIALLY — قبول نتيجة الذكاء الاصطناعي جزئيًا

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

<!-- BEGIN GENERATED: refs US-BC07-AIRS-ACCEPT-PARTIALLY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/results/{id}/actions/accept-partially` | — |
| الأمر | `CMD-AIRS-ACCEPT-PARTIALLY` | قبول نتيجة الذكاء الاصطناعي جزئيًا |
| السياسة | `POL-AIRS-ACCEPT-PARTIALLY` | reviewer authorized on the target (review, accept, reject)؛ tenant match; object visible |
| الحدث | `EVT-AIRS-PARTIALLY-ACCEPTED` | يصل إلى: Owner contexts (effects on acceptance); Evaluation feedback store |
| الكيان | `AGG-AI-RESULT` | نتيجة الذكاء الاصطناعي |
| الجدول | `ai.ai_results` | الجدول الرئيسي لنتيجة الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… |
| حالات الاستخدام | UC-073، UC-074 | Review AI Result؛ Approve AI-Assisted Result |
| الاختبار | TST-AI-RESULT-SM، TST-SLC10-INVARIANTS | دورة حالات نتيجة الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-AIRS-ACCEPT-PARTIALLY -->

</details>

### 5.3 US-BC07-AIRS-REJECT — رفض نتيجة الذكاء الاصطناعي

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

<!-- BEGIN GENERATED: refs US-BC07-AIRS-REJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/results/{id}/actions/reject` | — |
| الأمر | `CMD-AIRS-REJECT` | رفض نتيجة الذكاء الاصطناعي |
| السياسة | `POL-AIRS-REJECT` | reviewer authorized on the target (review, accept, reject)؛ tenant match; object visible |
| الحدث | `EVT-AIRS-REJECTED` | يصل إلى: Owner contexts (effects on acceptance); Evaluation feedback store |
| الكيان | `AGG-AI-RESULT` | نتيجة الذكاء الاصطناعي |
| الجدول | `ai.ai_results` | الجدول الرئيسي لنتيجة الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… |
| حالات الاستخدام | UC-073، UC-074 | Review AI Result؛ Approve AI-Assisted Result |
| الاختبار | TST-AI-RESULT-SM، TST-SLC10-INVARIANTS | دورة حالات نتيجة الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-AIRS-REJECT -->

</details>

### 5.4 US-BC07-AIRS-START-REVIEW — بدء مراجعة نتيجة الذكاء الاصطناعي

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

<!-- BEGIN GENERATED: refs US-BC07-AIRS-START-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/results/{id}/actions/start-review` | — |
| الأمر | `CMD-AIRS-START-REVIEW` | بدء مراجعة نتيجة الذكاء الاصطناعي |
| السياسة | `POL-AIRS-START-REVIEW` | reviewer authorized on the target (review, accept, reject)؛ tenant match; object visible |
| الحدث | `EVT-AIRS-REVIEW-STARTED` | يصل إلى: Owner contexts (effects on acceptance); Evaluation feedback store |
| الكيان | `AGG-AI-RESULT` | نتيجة الذكاء الاصطناعي |
| الجدول | `ai.ai_results` | الجدول الرئيسي لنتيجة الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… |
| حالات الاستخدام | UC-073، UC-074 | Review AI Result؛ Approve AI-Assisted Result |
| الاختبار | TST-AI-RESULT-SM، TST-SLC10-INVARIANTS | دورة حالات نتيجة الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-AIRS-START-REVIEW -->

</details>

### 5.5 US-BC07-Q-AIRS-QUEUE — جلب: Reviewable AI results by state, operation, target

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

<!-- BEGIN GENERATED: refs US-BC07-Q-AIRS-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/ai/results` | — |
| الاستعلام | `QRY-AIRS-QUEUE` | Reviewable AI results by state, operation, target |
| السياسة | `POL-AIRS-QUEUE` | reviewers authorized on targets |
| الكيان | `AGG-AI-RESULT` | نتيجة الذكاء الاصطناعي |
| الجدول | `ai.ai_results` | الجدول الرئيسي لنتيجة الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… |
| حالات الاستخدام | UC-073، UC-074 | Review AI Result؛ Approve AI-Assisted Result |
| الاختبار | TST-AI-RESULT-SM، TST-SLC10-INVARIANTS | دورة حالات نتيجة الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-Q-AIRS-QUEUE -->

</details>

### 5.6 US-BC07-S-AI-RESULT-01 — تلقائي: request COMPLETED for a reviewable operation (نتيجة الذكاء الاصطناعي)

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

<!-- BEGIN GENERATED: refs US-BC07-S-AI-RESULT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:request COMPLETED for a reviewable operation` | operation ∈ {AI-OP-03 draft, AI-OP-04 extract, AI-OP-05 translation used as evidence, AI-OP-06 match suggesti… |
| الانتقال | ∅ ← PROPOSED | — |
| الحدث | `EVT-AIRS-PROPOSED` | يصل إلى: Owner contexts (effects on acceptance); Evaluation feedback store |
| الكيان | `AGG-AI-RESULT` | نتيجة الذكاء الاصطناعي |
| الجدول | `ai.ai_results` | الجدول الرئيسي لنتيجة الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… |
| حالات الاستخدام | UC-073، UC-074 | Review AI Result؛ Approve AI-Assisted Result |
| الاختبار | TST-AI-RESULT-SM، TST-SLC10-INVARIANTS | دورة حالات نتيجة الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-AI-RESULT-01 -->

</details>

### 5.7 US-UI-SCR06-AI-QUEUE — قائمة نتائج الذكاء الاصطناعي المنتظرة للمراجعة

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

<!-- BEGIN GENERATED: refs US-UI-SCR06-AI-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `US-BC07-Q-AIRS-QUEUE` | — |
| المصدر | `21-ui-design.md §6.1` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR06-AI-QUEUE -->

</details>

### 5.8 US-UI-SCR46-ITEM-SELECT — قبول عناصر محددة من النتيجة ورفض الباقي

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

<!-- BEGIN GENERATED: refs US-UI-SCR46-ITEM-SELECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §12` | — |
| الشاشة | SCR-46 | شاشة مراجعة نتيجة ذكية |
| المصدر | `US-BC07-AIRS-ACCEPT-PARTIALLY` | — |
| المتطلب | REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… |
| حالات الاستخدام | UC-073، UC-074 | Review AI Result؛ Approve AI-Assisted Result |
<!-- END GENERATED: refs US-UI-SCR46-ITEM-SELECT -->

</details>

### 5.9 US-OPS-AI-REJECTION-FEEDBACK — تغذية أسباب الرفض إلى تقييم النماذج

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

<!-- BEGIN GENERATED: refs US-OPS-AI-REJECTION-FEEDBACK -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `US-BC07-AIRS-REJECT` | — |
| المصدر | `09-reliability/observability-slc10.md` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-AI-REJECTION-FEEDBACK -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… | `US-BC07-AIRS-ACCEPT`، `US-BC07-AIRS-ACCEPT-PARTIALLY`، `US-BC07-AIRS-REJECT`، `US-BC07-AIRS-START-REVIEW`، `US-BC07-Q-AIRS-QUEUE`، `US-BC07-S-AI-RESULT-01`، `US-UI-SCR46-ITEM-SELECT` | TST-AI-RESULT-SM، TST-SLC10-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
