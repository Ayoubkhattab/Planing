---
id: FEAT-COM-PRODUCT-LIBRARY
type: feature
title: "تصفح المنتجات وتنزيلها"
status: DRAFT
version: "0.1"
capability: CAP-10.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تصفح المنتجات وتنزيلها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COM-PRODUCT-LIBRARY |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-10 الاتصال والمنتجات |
| القدرة الفرعية | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) |
| الأدوار | أي مستخدم مخوَّل؛ المحلل؛ المدير؛ النظام |
| الشاشات | SCR-43 المنتجات والتوزيع |
| حالات الاستخدام | UC-112 |
| القصص | 8: 3 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يجد المستخدم المخوّل المنتجات المعتمدة وأحدث نسخها وينزلها بصيغة PDF أو مستند بعلامة مائية باسمه.

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
| `US-DOM-PRD-EXPORT` | تصدير نسخة شخصية بعلامة مائية | أمر | مسودة |
| `US-BC06-Q-PRD-GET` | جلب: Product version with rendered artifacts (download grants) and pinned citations | جلب | مسودة |
| `US-BC06-Q-PRD-LIST` | جلب: Products by kind, state, situation/case, date | جلب | مسودة |
| `US-BC06-S-PRODUCT-03` | تلقائي: newer version approved (المنتج) | نظام | مسودة |
| `US-UI-SCR43-DOWNLOAD` | تنزيل المنتج بالصيغة المسموحة مع تنبيه العلامة | واجهة | مسودة |
| `US-UI-SCR43-LIBRARY` | مكتبة المنتجات المعتمدة بأحدث نسخها | واجهة | مسودة |
| `US-PLT-PRD-WATERMARK` | علامة مائية مرئية وخفية لكل نسخة | منصة | مسودة |
| `US-OPS-PRD-LEAK-TRACE` | تتبع النسخة المسربة إلى مستلمها | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-DOM-PRD-EXPORT — تصدير نسخة شخصية بعلامة مائية

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

<!-- BEGIN GENERATED: refs US-DOM-PRD-EXPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-112 | Distribute / Export Product |
| المصدر | `00-open-questions.md §3` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-PRD-005 | The system shall export approved products as PDF and as documents with a watermark identifying the recipient. |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
<!-- END GENERATED: refs US-DOM-PRD-EXPORT -->

</details>

### 5.2 US-BC06-Q-PRD-GET — جلب: Product version with rendered artifacts (download grants) and pinned citations

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

<!-- BEGIN GENERATED: refs US-BC06-Q-PRD-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/knowledge/products/{product_id}` | — |
| الاستعلام | `QRY-PRD-GET` | Product version with rendered artifacts (download grants) and pinned citations |
| السياسة | `POL-PRD-GET` | audience + label rule |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-PRD-003 | When a product is approved, the system shall freeze its content as an immutable version with its citations pi… |
| حالة الاستخدام | UC-111 | Review & Approve Product |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-Q-PRD-GET -->

</details>

### 5.3 US-BC06-Q-PRD-LIST — جلب: Products by kind, state, situation/case, date

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

<!-- BEGIN GENERATED: refs US-BC06-Q-PRD-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/knowledge/products` | — |
| الاستعلام | `QRY-PRD-LIST` | Products by kind, state, situation/case, date |
| السياسة | `POL-PRD-LIST` | allowed_scope |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-PRD-001 | The system shall produce reports, briefings, map products and analytical products from versioned templates wi… |
| حالة الاستخدام | UC-110 | Generate Product from Template |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-Q-PRD-LIST -->

</details>

### 5.4 US-BC06-S-PRODUCT-03 — تلقائي: newer version approved (المنتج)

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

<!-- BEGIN GENERATED: refs US-BC06-S-PRODUCT-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:newer version approved` | system |
| الانتقال | APPROVED ← SUPERSEDED | — |
| الحدث | `EVT-PRD-SUPERSEDED` | يصل إلى: Distribution; Search projection (SLC-05); Notification (reviewers) |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-001، REQ-PRD-002، REQ-PRD-003 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-110، UC-111 | Generate Product from Template؛ Review & Approve Product |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-PRODUCT-03 -->

</details>

### 5.5 US-UI-SCR43-DOWNLOAD — تنزيل المنتج بالصيغة المسموحة مع تنبيه العلامة

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

<!-- BEGIN GENERATED: refs US-UI-SCR43-DOWNLOAD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-43 | شاشة المنتجات والتوزيع |
| المصدر | `21-ui-design.md §11` | — |
| المتطلب | REQ-PRD-005 | The system shall export approved products as PDF and as documents with a watermark identifying the recipient. |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
<!-- END GENERATED: refs US-UI-SCR43-DOWNLOAD -->

</details>

### 5.6 US-UI-SCR43-LIBRARY — مكتبة المنتجات المعتمدة بأحدث نسخها

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

<!-- BEGIN GENERATED: refs US-UI-SCR43-LIBRARY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-43 | شاشة المنتجات والتوزيع |
| المصدر | `products-knowledge-archive-spec.md §2` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-PRD-003 | When a product is approved, the system shall freeze its content as an immutable version with its citations pi… |
| حالة الاستخدام | UC-111 | Review & Approve Product |
<!-- END GENERATED: refs US-UI-SCR43-LIBRARY -->

</details>

### 5.7 US-PLT-PRD-WATERMARK — علامة مائية مرئية وخفية لكل نسخة

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

<!-- BEGIN GENERATED: refs US-PLT-PRD-WATERMARK -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `products-knowledge-archive-spec.md §2` | — |
| المصدر | `21-ui-design.md §11` | — |
| المتطلب | REQ-PRD-005 | The system shall export approved products as PDF and as documents with a watermark identifying the recipient. |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
<!-- END GENERATED: refs US-PLT-PRD-WATERMARK -->

</details>

### 5.8 US-OPS-PRD-LEAK-TRACE — تتبع النسخة المسربة إلى مستلمها

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

<!-- BEGIN GENERATED: refs US-OPS-PRD-LEAK-TRACE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §12.9` | — |
| المتطلب | REQ-PRD-005 | The system shall export approved products as PDF and as documents with a watermark identifying the recipient. |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
<!-- END GENERATED: refs US-OPS-PRD-LEAK-TRACE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-PRD-001 | The system shall produce reports, briefings, map products and analytical products from versioned templates wi… | `US-BC06-Q-PRD-LIST`، `US-BC06-S-PRODUCT-03` | TST-PRODUCT-SM، TST-PRODUCT-TEMPLATE-SM، TST-SLC12-INVARIANTS |
| REQ-PRD-002 | The system shall set a product's label to at least the highest label of its content and shall render only con… | `US-BC06-S-PRODUCT-03` | TST-PRODUCT-SM، TST-SLC12-INVARIANTS |
| REQ-PRD-003 | When a product is approved, the system shall freeze its content as an immutable version with its citations pi… | `US-BC06-Q-PRD-GET`، `US-BC06-S-PRODUCT-03`، `US-UI-SCR43-LIBRARY` | TST-PRODUCT-SM، TST-SLC12-INVARIANTS |
| REQ-PRD-005 | The system shall export approved products as PDF and as documents with a watermark identifying the recipient. | `US-DOM-PRD-EXPORT`، `US-OPS-PRD-LEAK-TRACE`، `US-PLT-PRD-WATERMARK`، `US-UI-SCR43-DOWNLOAD` | TST-DISTRIBUTION-SM، TST-SLC12-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
