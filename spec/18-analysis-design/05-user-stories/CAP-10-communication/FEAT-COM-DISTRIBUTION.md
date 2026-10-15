---
id: FEAT-COM-DISTRIBUTION
type: feature
title: "توزيع المنتجات"
status: DRAFT
version: "0.1"
capability: CAP-10.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# توزيع المنتجات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COM-DISTRIBUTION |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-10 الاتصال والمنتجات |
| القدرة الفرعية | CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2) |
| الأدوار | المدير؛ مالك المنتج؛ مسؤول الأمن؛ المدقِّق؛ النظام |
| الشاشات | SCR-43 المنتجات والتوزيع |
| حالات الاستخدام | UC-112 |
| القصص | 7: 5 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يوزع المدير أو مالك المنتج المنتج المعتمد على المخوّلين فقط، مع سجل كامل لمن استلمه.

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
| `US-BC06-DST-CANCEL` | إلغاء التوزيع | أمر | مسودة |
| `US-BC06-DST-DISTRIBUTE` | تنفيذ التوزيع | أمر | مسودة |
| `US-BC06-Q-DST-LOG` | جلب: Distribution and delivery log with watermark ids | جلب | مسودة |
| `US-BC06-S-DISTRIBUTION-01` | تلقائي: all recipients authorized and delivered (التوزيع) | نظام | مسودة |
| `US-BC06-S-DISTRIBUTION-02` | تلقائي: some recipients not authorized (التوزيع) | نظام | مسودة |
| `US-UI-SCR43-DISTRIBUTE` | اختيار المستلمين ورؤية المستبعدين بعد التوزيع | واجهة | مسودة |
| `US-UI-SCR43-RECIPIENT-VIEW` | المستلم يفتح المنتج الموزَّع إليه | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC06-DST-CANCEL — إلغاء التوزيع

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

<!-- BEGIN GENERATED: refs US-BC06-DST-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/distributions/{id}/actions/cancel` | — |
| الأمر | `CMD-DST-CANCEL` | إلغاء التوزيع |
| السياسة | `POL-DST-CANCEL` | Manager / product owner؛ tenant match; object visible |
| الحدث | `EVT-DST-CANCELLED` | يصل إلى: Notification (recipients); Audit |
| الكيان | `AGG-DISTRIBUTION` | التوزيع |
| الجدول | `knowledge.distributions` | الجدول الرئيسي للتوزيع |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-004، REQ-PRD-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
| الاختبار | TST-DISTRIBUTION-SM، TST-SLC12-INVARIANTS | دورة حالات التوزيع، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-DST-CANCEL -->

</details>

### 5.2 US-BC06-DST-DISTRIBUTE — تنفيذ التوزيع

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

<!-- BEGIN GENERATED: refs US-BC06-DST-DISTRIBUTE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/distributions` | — |
| الأمر | `CMD-DST-DISTRIBUTE` | تنفيذ التوزيع |
| السياسة | `POL-DST-DISTRIBUTE` | Manager / product owner؛ tenant match; object visible |
| الحدث | `EVT-DST-STARTED` | يصل إلى: Notification (recipients); Audit |
| الكيان | `AGG-DISTRIBUTION` | التوزيع |
| الجدول | `knowledge.distributions` | الجدول الرئيسي للتوزيع |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-004، REQ-PRD-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
| الاختبار | TST-DISTRIBUTION-SM، TST-SLC12-INVARIANTS | دورة حالات التوزيع، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-DST-DISTRIBUTE -->

</details>

### 5.3 US-BC06-Q-DST-LOG — جلب: Distribution and delivery log with watermark ids

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

<!-- BEGIN GENERATED: refs US-BC06-Q-DST-LOG -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/knowledge/products/{product_id}/distributions` | — |
| الاستعلام | `QRY-DST-LOG` | Distribution and delivery log with watermark ids |
| السياسة | `POL-DST-LOG` | distributor, Security Officer, Auditor |
| الكيان | `AGG-PRODUCT` | المنتج |
| الجدول | `knowledge.products` | الجدول الرئيسي للمنتج |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-PRD-004 | When a product is distributed, the system shall deliver it only to recipients authorized for its label and sh… |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
| الاختبار | TST-PRODUCT-SM، TST-SLC12-INVARIANTS | دورة حالات المنتج، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-Q-DST-LOG -->

</details>

### 5.4 US-BC06-S-DISTRIBUTION-01 — تلقائي: all recipients authorized and delivered (التوزيع)

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

<!-- BEGIN GENERATED: refs US-BC06-S-DISTRIBUTION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:all recipients authorized and delivered` | per-recipient watermark (recipient id, product version, time) embedded; delivery logged |
| الانتقال | PREPARING ← COMPLETED | — |
| الحدث | `EVT-DST-COMPLETED` | يصل إلى: Notification (recipients); Audit |
| الكيان | `AGG-DISTRIBUTION` | التوزيع |
| الجدول | `knowledge.distributions` | الجدول الرئيسي للتوزيع |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-004، REQ-PRD-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
| الاختبار | TST-DISTRIBUTION-SM، TST-SLC12-INVARIANTS | دورة حالات التوزيع، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-DISTRIBUTION-01 -->

</details>

### 5.5 US-BC06-S-DISTRIBUTION-02 — تلقائي: some recipients not authorized (التوزيع)

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

<!-- BEGIN GENERATED: refs US-BC06-S-DISTRIBUTION-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:some recipients not authorized` | unauthorized recipients excluded and listed to the distributor; others delivered |
| الانتقال | PREPARING ← COMPLETED_WITH_EXCLUSIONS | — |
| الحدث | `EVT-DST-COMPLETED-WITH-EXCLUSIONS` | يصل إلى: Notification (recipients); Audit |
| الكيان | `AGG-DISTRIBUTION` | التوزيع |
| الجدول | `knowledge.distributions` | الجدول الرئيسي للتوزيع |
| وحدة النشر | DU-15 | — |
| المتطلبات | REQ-PRD-004، REQ-PRD-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
| الاختبار | TST-DISTRIBUTION-SM، TST-SLC12-INVARIANTS | دورة حالات التوزيع، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-DISTRIBUTION-02 -->

</details>

### 5.6 US-UI-SCR43-DISTRIBUTE — اختيار المستلمين ورؤية المستبعدين بعد التوزيع

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

<!-- BEGIN GENERATED: refs US-UI-SCR43-DISTRIBUTE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-43 | شاشة المنتجات والتوزيع |
| المصدر | `products-knowledge-archive-spec.md §2` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-PRD-004 | When a product is distributed, the system shall deliver it only to recipients authorized for its label and sh… |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
<!-- END GENERATED: refs US-UI-SCR43-DISTRIBUTE -->

</details>

### 5.7 US-UI-SCR43-RECIPIENT-VIEW — المستلم يفتح المنتج الموزَّع إليه

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

<!-- BEGIN GENERATED: refs US-UI-SCR43-RECIPIENT-VIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-43 | شاشة المنتجات والتوزيع |
| الشاشة | SCR-03 | شاشة صندوق الوارد |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-PRD-004 | When a product is distributed, the system shall deliver it only to recipients authorized for its label and sh… |
| حالة الاستخدام | UC-112 | Distribute / Export Product |
<!-- END GENERATED: refs US-UI-SCR43-RECIPIENT-VIEW -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-PRD-004 | When a product is distributed, the system shall deliver it only to recipients authorized for its label and sh… | `US-BC06-DST-CANCEL`، `US-BC06-DST-DISTRIBUTE`، `US-BC06-Q-DST-LOG`، `US-BC06-S-DISTRIBUTION-01`، `US-BC06-S-DISTRIBUTION-02`، `US-UI-SCR43-DISTRIBUTE`، `US-UI-SCR43-RECIPIENT-VIEW` | TST-DISTRIBUTION-SM، TST-SLC12-INVARIANTS |
| REQ-PRD-005 | The system shall export approved products as PDF and as documents with a watermark identifying the recipient. | كل قصص الأوامر والنظام في الميزة (4) | TST-DISTRIBUTION-SM، TST-SLC12-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
