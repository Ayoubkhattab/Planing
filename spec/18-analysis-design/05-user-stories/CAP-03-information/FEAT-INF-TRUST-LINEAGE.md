---
id: FEAT-INF-TRUST-LINEAGE
type: feature
title: "الثقة بالمعلومة ومنشؤها"
status: DRAFT
version: "0.1"
capability: CAP-03.07
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# الثقة بالمعلومة ومنشؤها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-TRUST-LINEAGE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.07 المنشأ والثقة (R1) |
| الأدوار | المحلل؛ المدقِّق؛ النظام |
| الشاشات | SCR-25 النسب (lineage)، SCR-22 الادعاء والدليل والمصدر |
| حالات الاستخدام | — |
| القصص | 8: 2 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يقيّم المحلل درجة الثقة بالمعلومة وحالة التحقق منها ويتتبّع من أين جاءت وكيف اشتُقّت.

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
| QAS-PERF-014 | lineage trace depth 5 | p95 ≤ 2 s |
| QAS-TRC-001 | follows a decision back to its sources | 100 % of decisions and T1 derived objects traceable to sources |
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
| `US-BC02-CLM-ASSESS` | تقييم الادعاء | أمر | مسودة |
| `US-BC02-Q-LIN-TRACE` | جلب: Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy | جلب | مسودة |
| `US-UI-SCR22-CONFIDENCE-BADGE` | شارة ثقة تفتح على أبعادها السبعة | واجهة | مسودة |
| `US-UI-SCR25-LINEAGE-GRAPH` | تتبع منشأ المعلومة صعودًا ونزولًا | واجهة | مسودة |
| `US-PLT-CONFIDENCE-DIMENSIONS` | إرجاع أبعاد الثقة منفصلة دون درجة إلزامية | منصة | مسودة |
| `US-PLT-LINEAGE-RECORD` | تسجيل منشأ كل عنصر مشتق تلقائيًا | منصة | مسودة |
| `US-PLT-LINEAGE-TRACE-PERF` | تتبع المنشأ بعمق خمسة خلال ثانيتين | منصة | مسودة |
| `US-OPS-LINEAGE-COMPLETENESS` | فحص دوري لاكتمال سجلات المنشأ | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-CLM-ASSESS — تقييم الادعاء

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

<!-- BEGIN GENERATED: refs US-BC02-CLM-ASSESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/claims/{id}/actions/assess` | — |
| الأمر | `CMD-CLM-ASSESS` | تقييم الادعاء |
| السياسة | `POL-CLM-ASSESS` | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator sys… |
| الحدث | `EVT-CLM-ASSESSED` | يصل إلى: Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation m… |
| الكيان | `AGG-CLAIM` | الادعاء |
| الجدول | `information.claims` | الجدول الرئيسي للادعاء |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-026، REQ-INF-037 | معانيها في القسم 6. التتبع |
| الاختبار | TST-CLAIM-SM، TST-SLC02-INVARIANTS | دورة حالات الادعاء، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-CLM-ASSESS -->

</details>

### 5.2 US-BC02-Q-LIN-TRACE — جلب: Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy

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

<!-- BEGIN GENERATED: refs US-BC02-Q-LIN-TRACE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/lineage/{object_urn}` | — |
| الاستعلام | `QRY-LIN-TRACE` | Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy |
| السياسة | `POL-LIN-TRACE` | org scope ∩ classification rule; claims filtered by label |
| المتطلب | REQ-INF-035 | The system shall record lineage for every derived object: inputs and their versions, the transformation and i… |
<!-- END GENERATED: refs US-BC02-Q-LIN-TRACE -->

</details>

### 5.3 US-UI-SCR22-CONFIDENCE-BADGE — شارة ثقة تفتح على أبعادها السبعة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR22-CONFIDENCE-BADGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| المصدر | `21-ui-design.md §12` | — |
| المتطلب | REQ-INF-026 | The system shall expose confidence as separate dimensions: source reliability, information confidence, data q… |
<!-- END GENERATED: refs US-UI-SCR22-CONFIDENCE-BADGE -->

</details>

### 5.4 US-UI-SCR25-LINEAGE-GRAPH — تتبع منشأ المعلومة صعودًا ونزولًا

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R1 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR25-LINEAGE-GRAPH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-25 | شاشة النسب (lineage) |
| الجودة | QAS-TRC-001 | follows a decision back to its sources → 100 % of decisions and T1 derived objects traceable to sources |
| المتطلب | REQ-INF-035 | The system shall record lineage for every derived object: inputs and their versions, the transformation and i… |
<!-- END GENERATED: refs US-UI-SCR25-LINEAGE-GRAPH -->

</details>

### 5.5 US-PLT-CONFIDENCE-DIMENSIONS — إرجاع أبعاد الثقة منفصلة دون درجة إلزامية

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

<!-- BEGIN GENERATED: refs US-PLT-CONFIDENCE-DIMENSIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `confidence-model.md` | — |
| المتطلب | REQ-INF-026 | The system shall expose confidence as separate dimensions: source reliability, information confidence, data q… |
<!-- END GENERATED: refs US-PLT-CONFIDENCE-DIMENSIONS -->

</details>

### 5.6 US-PLT-LINEAGE-RECORD — تسجيل منشأ كل عنصر مشتق تلقائيًا

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

<!-- BEGIN GENERATED: refs US-PLT-LINEAGE-RECORD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-TRC-001 | follows a decision back to its sources → 100 % of decisions and T1 derived objects traceable to sources |
| المتطلب | REQ-INF-035 | The system shall record lineage for every derived object: inputs and their versions, the transformation and i… |
<!-- END GENERATED: refs US-PLT-LINEAGE-RECORD -->

</details>

### 5.7 US-PLT-LINEAGE-TRACE-PERF — تتبع المنشأ بعمق خمسة خلال ثانيتين

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

<!-- BEGIN GENERATED: refs US-PLT-LINEAGE-TRACE-PERF -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-014 | lineage trace depth 5 → p95 ≤ 2 s |
<!-- END GENERATED: refs US-PLT-LINEAGE-TRACE-PERF -->

</details>

### 5.8 US-OPS-LINEAGE-COMPLETENESS — فحص دوري لاكتمال سجلات المنشأ

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-LINEAGE-COMPLETENESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-TRC-001 | follows a decision back to its sources → 100 % of decisions and T1 derived objects traceable to sources |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-035 | The system shall record lineage for every derived object: inputs and their versions, the transformation and i… |
<!-- END GENERATED: refs US-OPS-LINEAGE-COMPLETENESS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-026 | The system shall expose confidence as separate dimensions: source reliability, information confidence, data q… | `US-BC02-CLM-ASSESS`، `US-PLT-CONFIDENCE-DIMENSIONS`، `US-UI-SCR22-CONFIDENCE-BADGE` | TST-CLAIM-SM، TST-SLC02-INVARIANTS |
| REQ-INF-035 | The system shall record lineage for every derived object: inputs and their versions, the transformation and i… | `US-BC02-Q-LIN-TRACE`، `US-OPS-LINEAGE-COMPLETENESS`، `US-PLT-LINEAGE-RECORD`، `US-UI-SCR25-LINEAGE-GRAPH` | TST-ANALYSIS-RUN-SM، TST-FINDING-SM، TST-SLC02-INVARIANTS، TST-SLC07-INVARIANTS |
| REQ-INF-037 | If a T1 object is submitted without a source reference, then the system shall reject it. | `US-BC02-CLM-ASSESS` | TST-CLAIM-SM، TST-SLC02-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
