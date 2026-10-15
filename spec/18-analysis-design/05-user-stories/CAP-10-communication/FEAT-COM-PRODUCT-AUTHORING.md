---
id: FEAT-COM-PRODUCT-AUTHORING
type: feature
title: "إعداد التقارير والإحاطات"
status: DRAFT
version: "0.1"
capability: CAP-10.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إعداد التقارير والإحاطات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COM-PRODUCT-AUTHORING |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-10 الاتصال والمنتجات |
| القدرة الفرعية | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) |
| الأدوار | المحلل؛ المخطِّط؛ النظام |
| الشاشات | SCR-43 المنتجات والتوزيع |
| حالات الاستخدام | UC-110 |
| القصص | 12: 7 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يولد المحلل أو المخطط تقريرًا أو إحاطة أو خريطة من قالب ببياناته وأدلته، ويحرر نصه ثم يقدمه للمراجعة.

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
| QAS-PRD-001 | generate a 30-page product with 10 maps | ≤ 2 min (async job) |
| QAS-PRD-002 | product rendered for an audience | 0 content above the product label (inference suite on products) |
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
| `US-BC06-PRD-CREATE` | إنشاء المنتج | أمر | مسودة |
| `US-BC06-PRD-DISCARD` | تجاهل مسودة المنتج | أمر | مسودة |
| `US-BC06-PRD-EDIT-NARRATIVE` | تعديل سرد المنتج | أمر | مسودة |
| `US-BC06-PRD-GENERATE` | توليد المنتج | أمر | مسودة |
| `US-BC06-PRD-SUBMIT` | تقديم المنتج | أمر | مسودة |
| `US-BC06-S-PRODUCT-01` | تلقائي: generation succeeded (المنتج) | نظام | مسودة |
| `US-BC06-S-PRODUCT-02` | تلقائي: generation failed (المنتج) | نظام | مسودة |
| `US-UI-SCR43-CITATIONS` | كل عنصر في المنتج يقود إلى مصدره | واجهة | مسودة |
| `US-UI-SCR43-GENERATION-STATUS` | تقدم توليد المنتج وسبب فشله | واجهة | مسودة |
| `US-UI-SCR43-NARRATIVE-EDIT` | تحرير السرد فقط ووسم مسودة الذكاء الاصطناعي | واجهة | مسودة |
| `US-PLT-PRD-LABEL-SUITE` | اختبار عدم تجاوز محتوى المنتج تصنيفه | منصة | مسودة |
| `US-PLT-PRD-RENDER` | توليد منتج ثلاثين صفحة خلال دقيقتين | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC06-PRD-CREATE — إنشاء المنتج

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

<!-- BEGIN GENERATED: refs US-BC06-PRD-CREATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/products` | — |
| الأمر | `CMD-PRD-CREATE` | إنشاء المنتج |
| السياسة | `POL-PRD-CREATE` | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)… |
| الحدث | `EVT-PRD-CREATED` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-110 | Generate Product from Template |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-PRD-CREATE -->

</details>

### 5.2 US-BC06-PRD-DISCARD — تجاهل مسودة المنتج

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

<!-- BEGIN GENERATED: refs US-BC06-PRD-DISCARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/products/{id}/actions/discard` | — |
| الأمر | `CMD-PRD-DISCARD` | تجاهل مسودة المنتج |
| السياسة | `POL-PRD-DISCARD` | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)… |
| الحدث | `EVT-PRD-DISCARDED` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-110 | Generate Product from Template |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-PRD-DISCARD -->

</details>

### 5.3 US-BC06-PRD-EDIT-NARRATIVE — تعديل سرد المنتج

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

<!-- BEGIN GENERATED: refs US-BC06-PRD-EDIT-NARRATIVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/products/{id}/actions/edit-narrative` | — |
| الأمر | `CMD-PRD-EDIT-NARRATIVE` | تعديل سرد المنتج |
| السياسة | `POL-PRD-EDIT-NARRATIVE` | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)… |
| الحدث | `EVT-PRD-NARRATIVE-EDITED` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-110 | Generate Product from Template |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-PRD-EDIT-NARRATIVE -->

</details>

### 5.4 US-BC06-PRD-GENERATE — توليد المنتج

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

<!-- BEGIN GENERATED: refs US-BC06-PRD-GENERATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/products/{id}/actions/generate` | — |
| الأمر | `CMD-PRD-GENERATE` | توليد المنتج |
| السياسة | `POL-PRD-GENERATE` | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)… |
| الحدث | `EVT-PRD-GENERATION-STARTED` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-110 | Generate Product from Template |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-PRD-GENERATE -->

</details>

### 5.5 US-BC06-PRD-SUBMIT — تقديم المنتج

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

<!-- BEGIN GENERATED: refs US-BC06-PRD-SUBMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/products/{id}/actions/submit` | — |
| الأمر | `CMD-PRD-SUBMIT` | تقديم المنتج |
| السياسة | `POL-PRD-SUBMIT` | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)… |
| الحدث | `EVT-PRD-SUBMITTED` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-110 | Generate Product from Template |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-PRD-SUBMIT -->

</details>

### 5.6 US-BC06-S-PRODUCT-01 — تلقائي: generation succeeded (المنتج)

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

<!-- BEGIN GENERATED: refs US-BC06-S-PRODUCT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:generation succeeded` | every binding executed as known_at = generation time; content items with label > product label excluded; rend… |
| الانتقال | GENERATING ← GENERATED | — |
| الحدث | `EVT-PRD-GENERATED` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-110 | Generate Product from Template |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-PRODUCT-01 -->

</details>

### 5.7 US-BC06-S-PRODUCT-02 — تلقائي: generation failed (المنتج)

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

<!-- BEGIN GENERATED: refs US-BC06-S-PRODUCT-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:generation failed` | error recorded |
| الانتقال | GENERATING ← GENERATION_FAILED | — |
| الحدث | `EVT-PRD-GENERATION-FAILED` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-110 | Generate Product from Template |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-PRODUCT-02 -->

</details>

### 5.8 US-UI-SCR43-CITATIONS — كل عنصر في المنتج يقود إلى مصدره

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

<!-- BEGIN GENERATED: refs US-UI-SCR43-CITATIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-43 | شاشة المنتجات والتوزيع |
| الجودة | QAS-PRD-002 | product rendered for an audience → 0 content above the product label (inference suite on products) |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-PRD-001 | The system shall produce reports, briefings, map products and analytical products from versioned templates wi… |
| حالة الاستخدام | UC-110 | Generate Product from Template |
<!-- END GENERATED: refs US-UI-SCR43-CITATIONS -->

</details>

### 5.9 US-UI-SCR43-GENERATION-STATUS — تقدم توليد المنتج وسبب فشله

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

<!-- BEGIN GENERATED: refs US-UI-SCR43-GENERATION-STATUS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-43 | شاشة المنتجات والتوزيع |
| الجودة | QAS-PRD-001 | generate a 30-page product with 10 maps → ≤ 2 min (async job) |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-PRD-001 | The system shall produce reports, briefings, map products and analytical products from versioned templates wi… |
| حالة الاستخدام | UC-110 | Generate Product from Template |
<!-- END GENERATED: refs US-UI-SCR43-GENERATION-STATUS -->

</details>

### 5.10 US-UI-SCR43-NARRATIVE-EDIT — تحرير السرد فقط ووسم مسودة الذكاء الاصطناعي

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

<!-- BEGIN GENERATED: refs US-UI-SCR43-NARRATIVE-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-43 | شاشة المنتجات والتوزيع |
| المصدر | `products-knowledge-archive-spec.md §1` | — |
| المتطلب | REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… |
| حالات الاستخدام | UC-073، UC-074 | Review AI Result؛ Approve AI-Assisted Result |
<!-- END GENERATED: refs US-UI-SCR43-NARRATIVE-EDIT -->

</details>

### 5.11 US-PLT-PRD-LABEL-SUITE — اختبار عدم تجاوز محتوى المنتج تصنيفه

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

<!-- BEGIN GENERATED: refs US-PLT-PRD-LABEL-SUITE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PRD-002 | product rendered for an audience → 0 content above the product label (inference suite on products) |
| المتطلب | REQ-PRD-002 | The system shall set a product's label to at least the highest label of its content and shall render only con… |
| حالة الاستخدام | UC-110 | Generate Product from Template |
<!-- END GENERATED: refs US-PLT-PRD-LABEL-SUITE -->

</details>

### 5.12 US-PLT-PRD-RENDER — توليد منتج ثلاثين صفحة خلال دقيقتين

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

<!-- BEGIN GENERATED: refs US-PLT-PRD-RENDER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PRD-001 | generate a 30-page product with 10 maps → ≤ 2 min (async job) |
| المتطلب | REQ-PRD-001 | The system shall produce reports, briefings, map products and analytical products from versioned templates wi… |
| حالة الاستخدام | UC-110 | Generate Product from Template |
<!-- END GENERATED: refs US-PLT-PRD-RENDER -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… | `US-UI-SCR43-NARRATIVE-EDIT` | TST-AI-RESULT-SM، TST-SLC10-INVARIANTS |
| REQ-PRD-001 | The system shall produce reports, briefings, map products and analytical products from versioned templates wi… | `US-BC06-PRD-CREATE`، `US-BC06-PRD-DISCARD`، `US-BC06-PRD-EDIT-NARRATIVE`، `US-BC06-PRD-GENERATE`، `US-BC06-PRD-SUBMIT`، `US-BC06-S-PRODUCT-01`، `US-BC06-S-PRODUCT-02`، `US-PLT-PRD-RENDER`، `US-UI-SCR43-CITATIONS`، `US-UI-SCR43-GENERATION-STATUS` | TST-PRODUCT-SM، TST-PRODUCT-TEMPLATE-SM، TST-SLC12-INVARIANTS |
| REQ-PRD-002 | The system shall set a product's label to at least the highest label of its content and shall render only con… | `US-BC06-PRD-CREATE`، `US-BC06-PRD-DISCARD`، `US-BC06-PRD-EDIT-NARRATIVE`، `US-BC06-PRD-GENERATE`، `US-BC06-PRD-SUBMIT`، `US-BC06-S-PRODUCT-01`، `US-BC06-S-PRODUCT-02`، `US-PLT-PRD-LABEL-SUITE` | TST-PRODUCT-SM، TST-SLC12-INVARIANTS |
| REQ-PRD-003 | When a product is approved, the system shall freeze its content as an immutable version with its citations pi… | كل قصص الميزة المأخوذة من المواصفة (7) | TST-PRODUCT-SM، TST-SLC12-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
