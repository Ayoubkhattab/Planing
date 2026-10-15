---
id: FEAT-COM-PRODUCT-REVIEW
type: feature
title: "مراجعة المنتجات واعتمادها"
status: DRAFT
version: "0.1"
capability: CAP-10.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مراجعة المنتجات واعتمادها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COM-PRODUCT-REVIEW |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-10 الاتصال والمنتجات |
| القدرة الفرعية | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) |
| الأدوار | المراجع؛ المدير |
| الشاشات | SCR-43 المنتجات والتوزيع، SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-111 |
| القصص | 6: 3 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يراجع المراجع المنتج فيعتمده نسخة نهائية مجمدة أو يعيده للتعديل، ويستطيع المدير سحبه.

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
| `US-BC06-PRD-APPROVE` | اعتماد المنتج | أمر | مسودة |
| `US-BC06-PRD-RETURN` | إعادة المنتج للمراجعة | أمر | مسودة |
| `US-BC06-PRD-WITHDRAW` | سحب المنتج | أمر | مسودة |
| `US-UI-SCR06-PRODUCT-REVIEW` | المنتجات المقدّمة في قائمة مراجعتي | واجهة | مسودة |
| `US-UI-SCR43-FROZEN-VERSION` | النسخة المعتمدة مجمدة وتنبيه بالأحدث | واجهة | مسودة |
| `US-OPS-PRD-INTEGRITY` | التحقق من سلامة ملفات النسخ المعتمدة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC06-PRD-APPROVE — اعتماد المنتج

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

<!-- BEGIN GENERATED: refs US-BC06-PRD-APPROVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/products/{id}/actions/approve` | — |
| الأمر | `CMD-PRD-APPROVE` | اعتماد المنتج |
| السياسة | `POL-PRD-APPROVE` | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)… |
| الحدث | `EVT-PRD-APPROVED` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-111 | Review & Approve Product |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-PRD-APPROVE -->

</details>

### 5.2 US-BC06-PRD-RETURN — إعادة المنتج للمراجعة

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

<!-- BEGIN GENERATED: refs US-BC06-PRD-RETURN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/products/{id}/actions/return` | — |
| الأمر | `CMD-PRD-RETURN` | إعادة المنتج للمراجعة |
| السياسة | `POL-PRD-RETURN` | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)… |
| الحدث | `EVT-PRD-RETURNED` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-111 | Review & Approve Product |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-PRD-RETURN -->

</details>

### 5.3 US-BC06-PRD-WITHDRAW — سحب المنتج

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

<!-- BEGIN GENERATED: refs US-BC06-PRD-WITHDRAW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/products/{id}/actions/withdraw` | — |
| الأمر | `CMD-PRD-WITHDRAW` | سحب المنتج |
| السياسة | `POL-PRD-WITHDRAW` | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)… |
| الحدث | `EVT-PRD-WITHDRAWN` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-111 | Review & Approve Product |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-PRD-WITHDRAW -->

</details>

### 5.4 US-UI-SCR06-PRODUCT-REVIEW — المنتجات المقدّمة في قائمة مراجعتي

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

<!-- BEGIN GENERATED: refs US-UI-SCR06-PRODUCT-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `17-security-design.md §12.4` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-PRD-003 | When a product is approved, the system shall freeze its content as an immutable version with its citations pi… |
| حالة الاستخدام | UC-111 | Review & Approve Product |
<!-- END GENERATED: refs US-UI-SCR06-PRODUCT-REVIEW -->

</details>

### 5.5 US-UI-SCR43-FROZEN-VERSION — النسخة المعتمدة مجمدة وتنبيه بالأحدث

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

<!-- BEGIN GENERATED: refs US-UI-SCR43-FROZEN-VERSION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-43 | شاشة المنتجات والتوزيع |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-PRD-003 | When a product is approved, the system shall freeze its content as an immutable version with its citations pi… |
| حالة الاستخدام | UC-111 | Review & Approve Product |
<!-- END GENERATED: refs US-UI-SCR43-FROZEN-VERSION -->

</details>

### 5.6 US-OPS-PRD-INTEGRITY — التحقق من سلامة ملفات النسخ المعتمدة

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

<!-- BEGIN GENERATED: refs US-OPS-PRD-INTEGRITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `products-knowledge-archive-spec.md §1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-PRD-003 | When a product is approved, the system shall freeze its content as an immutable version with its citations pi… |
| حالة الاستخدام | UC-111 | Review & Approve Product |
<!-- END GENERATED: refs US-OPS-PRD-INTEGRITY -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-PRD-001 | The system shall produce reports, briefings, map products and analytical products from versioned templates wi… | كل قصص الميزة المأخوذة من المواصفة (3) | TST-PRODUCT-SM، TST-PRODUCT-TEMPLATE-SM، TST-SLC12-INVARIANTS |
| REQ-PRD-002 | The system shall set a product's label to at least the highest label of its content and shall render only con… | كل قصص الميزة المأخوذة من المواصفة (3) | TST-PRODUCT-SM، TST-SLC12-INVARIANTS |
| REQ-PRD-003 | When a product is approved, the system shall freeze its content as an immutable version with its citations pi… | `US-BC06-PRD-APPROVE`، `US-BC06-PRD-RETURN`، `US-BC06-PRD-WITHDRAW`، `US-OPS-PRD-INTEGRITY`، `US-UI-SCR06-PRODUCT-REVIEW`، `US-UI-SCR43-FROZEN-VERSION` | TST-PRODUCT-SM، TST-SLC12-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
