---
id: FEAT-RES-ASSET-CUSTODY
type: feature
title: "إسناد الأصول وعهدتها"
status: DRAFT
version: "0.1"
capability: CAP-08.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إسناد الأصول وعهدتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-ASSET-CUSTODY |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.01 إدارة الأصول (R2) |
| الأدوار | مدير الموارد؛ المخطِّط؛ النظام |
| الشاشات | SCR-40 الأصول وتوفرها والصيانة، SCR-02 تفاصيل المهمة وسجلها |
| حالات الاستخدام | UC-053 |
| القصص | 8: 5 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعرف الجميع من يحمل الأصل الآن ولأي مهمة أُسند، مع سلسلة عهدة متصلة بلا فجوات.

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
| `US-BC05-ASG-ASSIGN` | تسجيل إسناد الأصل | أمر | مسودة |
| `US-BC05-ASG-CANCEL` | إلغاء إسناد الأصل | أمر | مسودة |
| `US-BC05-ASG-RETURN` | إرجاع الأصل وإنهاء إسناد الأصل | أمر | مسودة |
| `US-BC05-AST-TRANSFER-CUSTODY` | نقل عهدة الأصل | أمر | مسودة |
| `US-BC05-S-ASSET-ASSIGNMENT-01` | تلقائي: linked task terminal (إسناد الأصل) | نظام | مسودة |
| `US-UI-SCR02-TASK-ASSETS` | أصول المهمة المسندة وإرجاعها من تفاصيل المهمة | واجهة | مسودة |
| `US-UI-SCR40-CUSTODY-CHAIN` | سلسلة عهدة الأصل متصلة بلا فجوات | واجهة | مسودة |
| `US-OPS-AST-CUSTODY-CHECK` | فحص دوري لاتصال سلاسل العهدة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-ASG-ASSIGN — تسجيل إسناد الأصل

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

<!-- BEGIN GENERATED: refs US-BC05-ASG-ASSIGN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/asset-assignments` | — |
| الأمر | `CMD-ASG-ASSIGN` | تسجيل إسناد الأصل |
| السياسة | `POL-ASG-ASSIGN` | Resource Manager / Planner؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-ASG-ASSIGNED` | يصل إلى: Availability view; Task (SLC-03) |
| الكيان | `AGG-ASSET-ASSIGNMENT` | إسناد الأصل |
| الجدول | `readiness.asset_assignments` | الجدول الرئيسي لإسناد الأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-003 | When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavai… |
| حالة الاستخدام | UC-053 | Assign Asset |
| الاختبار | TST-ASSET-ASSIGNMENT-SM، TST-SLC09-INVARIANTS | دورة حالات إسناد الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-ASG-ASSIGN -->

</details>

### 5.2 US-BC05-ASG-CANCEL — إلغاء إسناد الأصل

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

<!-- BEGIN GENERATED: refs US-BC05-ASG-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/asset-assignments/{id}/actions/cancel` | — |
| الأمر | `CMD-ASG-CANCEL` | إلغاء إسناد الأصل |
| السياسة | `POL-ASG-CANCEL` | Resource Manager / Planner؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-ASG-CANCELLED` | يصل إلى: Availability view; Task (SLC-03) |
| الكيان | `AGG-ASSET-ASSIGNMENT` | إسناد الأصل |
| الجدول | `readiness.asset_assignments` | الجدول الرئيسي لإسناد الأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-003 | When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavai… |
| حالة الاستخدام | UC-053 | Assign Asset |
| الاختبار | TST-ASSET-ASSIGNMENT-SM، TST-SLC09-INVARIANTS | دورة حالات إسناد الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-ASG-CANCEL -->

</details>

### 5.3 US-BC05-ASG-RETURN — إرجاع الأصل وإنهاء إسناد الأصل

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

<!-- BEGIN GENERATED: refs US-BC05-ASG-RETURN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/asset-assignments/{id}/actions/return` | — |
| الأمر | `CMD-ASG-RETURN` | إرجاع الأصل وإنهاء إسناد الأصل |
| السياسة | `POL-ASG-RETURN` | Resource Manager / Planner؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-ASG-RETURNED` | يصل إلى: Availability view; Task (SLC-03) |
| الكيان | `AGG-ASSET-ASSIGNMENT` | إسناد الأصل |
| الجدول | `readiness.asset_assignments` | الجدول الرئيسي لإسناد الأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-003 | When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavai… |
| حالة الاستخدام | UC-053 | Assign Asset |
| الاختبار | TST-ASSET-ASSIGNMENT-SM، TST-SLC09-INVARIANTS | دورة حالات إسناد الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-ASG-RETURN -->

</details>

### 5.4 US-BC05-AST-TRANSFER-CUSTODY — نقل عهدة الأصل

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

<!-- BEGIN GENERATED: refs US-BC05-AST-TRANSFER-CUSTODY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/assets/{id}/actions/transfer-custody` | — |
| الأمر | `CMD-AST-TRANSFER-CUSTODY` | نقل عهدة الأصل |
| السياسة | `POL-AST-TRANSFER-CUSTODY` | Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Securit… |
| الحدث | `EVT-AST-CUSTODY-TRANSFERRED` | يصل إلى: Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignm… |
| الكيان | `AGG-ASSET` | الأصل |
| الجدول | `readiness.assets` | الجدول الرئيسي للأصل |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-RES-001، REQ-RES-002، REQ-RES-003، REQ-RES-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-053 | Assign Asset |
| الاختبار | TST-ASSET-SM، TST-SLC09-INVARIANTS | دورة حالات الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-AST-TRANSFER-CUSTODY -->

</details>

### 5.5 US-BC05-S-ASSET-ASSIGNMENT-01 — تلقائي: linked task terminal (إسناد الأصل)

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

<!-- BEGIN GENERATED: refs US-BC05-S-ASSET-ASSIGNMENT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:linked task terminal` | condition report requested from last holder (follow-up task) |
| الانتقال | ACTIVE ← RETURNED | — |
| الحدث | `EVT-ASG-RETURNED` | يصل إلى: Availability view; Task (SLC-03) |
| الكيان | `AGG-ASSET-ASSIGNMENT` | إسناد الأصل |
| الجدول | `readiness.asset_assignments` | الجدول الرئيسي لإسناد الأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-003 | When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavai… |
| حالة الاستخدام | UC-053 | Assign Asset |
| الاختبار | TST-ASSET-ASSIGNMENT-SM، TST-SLC09-INVARIANTS | دورة حالات إسناد الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-S-ASSET-ASSIGNMENT-01 -->

</details>

### 5.6 US-UI-SCR02-TASK-ASSETS — أصول المهمة المسندة وإرجاعها من تفاصيل المهمة

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

<!-- BEGIN GENERATED: refs US-UI-SCR02-TASK-ASSETS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-02 | شاشة تفاصيل المهمة وسجلها |
| حالة الاستخدام | UC-053 | Assign Asset |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RES-012 | The system shall link resources and assets to tasks as structured references, replacing the text-only resourc… |
| حالة الاستخدام | UC-053 | Assign Asset |
<!-- END GENERATED: refs US-UI-SCR02-TASK-ASSETS -->

</details>

### 5.7 US-UI-SCR40-CUSTODY-CHAIN — سلسلة عهدة الأصل متصلة بلا فجوات

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

<!-- BEGIN GENERATED: refs US-UI-SCR40-CUSTODY-CHAIN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-40 | شاشة الأصول وتوفرها والصيانة |
| المصدر | `17-security-design.md §12.9` | — |
| المتطلب | REQ-RES-002 | When custody of an asset is transferred, the system shall record the previous holder, the new holder, the tim… |
| حالة الاستخدام | UC-053 | Assign Asset |
<!-- END GENERATED: refs US-UI-SCR40-CUSTODY-CHAIN -->

</details>

### 5.8 US-OPS-AST-CUSTODY-CHECK — فحص دوري لاتصال سلاسل العهدة

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

<!-- BEGIN GENERATED: refs US-OPS-AST-CUSTODY-CHECK -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §12.9` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RES-002 | When custody of an asset is transferred, the system shall record the previous holder, the new holder, the tim… |
| حالة الاستخدام | UC-053 | Assign Asset |
<!-- END GENERATED: refs US-OPS-AST-CUSTODY-CHECK -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RES-001 | The system shall register each asset with type, ownership, custody holder, status, condition, location, capab… | `US-BC05-AST-TRANSFER-CUSTODY` | TST-ASSET-SM، TST-SLC09-INVARIANTS |
| REQ-RES-002 | When custody of an asset is transferred, the system shall record the previous holder, the new holder, the tim… | `US-BC05-AST-TRANSFER-CUSTODY`، `US-OPS-AST-CUSTODY-CHECK`، `US-UI-SCR40-CUSTODY-CHAIN` | TST-ASSET-SM، TST-SLC09-INVARIANTS |
| REQ-RES-003 | When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavai… | كل قصص الميزة المأخوذة من المواصفة (5) | TST-ASSET-ASSIGNMENT-SM، TST-ASSET-SM، TST-SLC09-INVARIANTS |
| REQ-RES-005 | The system shall keep asset location as bitemporal claims so that the location of an asset at any past time i… | `US-BC05-AST-TRANSFER-CUSTODY` | TST-ASSET-SM، TST-SLC09-INVARIANTS |
| REQ-RES-012 | The system shall link resources and assets to tasks as structured references, replacing the text-only resourc… | `US-UI-SCR02-TASK-ASSETS` | TST-ALLOCATION-SM، TST-ASSET-ASSIGNMENT-SM، TST-SLC09-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
