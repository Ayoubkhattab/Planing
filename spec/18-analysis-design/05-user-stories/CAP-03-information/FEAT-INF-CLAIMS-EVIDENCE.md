---
id: FEAT-INF-CLAIMS-EVIDENCE
type: feature
title: "الادعاءات وأدلتها"
status: DRAFT
version: "0.1"
capability: CAP-03.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# الادعاءات وأدلتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-CLAIMS-EVIDENCE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.02 الادعاءات والأدلة (R1) |
| الأدوار | المحلل؛ النظام؛ أي مستخدم مخوَّل |
| الشاشات | SCR-22 الادعاء والدليل والمصدر |
| حالات الاستخدام | UC-006 |
| القصص | 13: 7 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يسجّل المحلل كل معلومة كادعاء مسند إلى مصادره وأدلته ويصححه أو يسحبه دون أن يُمحى أصله.

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
| `US-BC02-CLM-ASSERT` | تسجيل الادعاء | أمر | مسودة |
| `US-BC02-CLM-CORRECT` | تصحيح الادعاء | أمر | مسودة |
| `US-BC02-CLM-RECLASSIFY` | إعادة تصنيف الادعاء | أمر | مسودة |
| `US-BC02-CLM-RETRACT` | سحب الادعاء | أمر | مسودة |
| `US-BC02-EVL-LINK` | ربط رابط الدليل | أمر | مسودة |
| `US-BC02-EVL-UNLINK` | فك ربط رابط الدليل | أمر | مسودة |
| `US-BC02-Q-CLM-GET` | جلب: Claim with sources (per protection), evidence links, supersession chain | جلب | مسودة |
| `US-UI-SCR22-CLAIM-DETAIL` | عرض الادعاء بمصادره وأدلته وسلسلة تصحيحه | واجهة | مسودة |
| `US-UI-SCR22-CLAIM-FORM` | تسجيل ادعاء بمصدره وزمن صحته ودليله | واجهة | مسودة |
| `US-UI-SCR22-CORRECT-OR-CHANGE` | التمييز بين تصحيح القيمة وتغيرها في الواقع | واجهة | مسودة |
| `US-PLT-CLAIMS-IMMUTABLE` | عدم الكتابة فوق ادعاءات المستوى الأول أبدًا | منصة | مسودة |
| `US-INT-CLAIMS-FROM-ADAPTER` | تسجيل قيم الأنظمة الخارجية ادعاءات بمصدرها | تكامل | مسودة |
| `US-OPS-CLAIMS-CURRENT-REBUILD` | إعادة بناء القيم الحالية من التاريخ عند اختلافها | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-CLM-ASSERT — تسجيل الادعاء

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

<!-- BEGIN GENERATED: refs US-BC02-CLM-ASSERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/claims` | — |
| الأمر | `CMD-CLM-ASSERT` | تسجيل الادعاء |
| السياسة | `POL-CLM-ASSERT` | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator sys… |
| الحدث | `EVT-CLM-ASSERTED` | يصل إلى: Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation m… |
| الكيان | `AGG-CLAIM` | الادعاء |
| الجدول | `information.claims` | الجدول الرئيسي للادعاء |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-021، REQ-INF-024 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-006 | Manage Evidence |
| الاختبار | TST-CLAIM-SM، TST-SLC02-INVARIANTS | دورة حالات الادعاء، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-CLM-ASSERT -->

</details>

### 5.2 US-BC02-CLM-CORRECT — تصحيح الادعاء

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

<!-- BEGIN GENERATED: refs US-BC02-CLM-CORRECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/claims/{id}/actions/correct` | — |
| الأمر | `CMD-CLM-CORRECT` | تصحيح الادعاء |
| السياسة | `POL-CLM-CORRECT` | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator sys… |
| الحدث | `EVT-CLM-CORRECTED` | يصل إلى: Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation m… |
| الكيان | `AGG-CLAIM` | الادعاء |
| الجدول | `information.claims` | الجدول الرئيسي للادعاء |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-021، REQ-INF-024 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-006 | Manage Evidence |
| الاختبار | TST-CLAIM-SM، TST-SLC02-INVARIANTS | دورة حالات الادعاء، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-CLM-CORRECT -->

</details>

### 5.3 US-BC02-CLM-RECLASSIFY — إعادة تصنيف الادعاء

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

<!-- BEGIN GENERATED: refs US-BC02-CLM-RECLASSIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/claims/{id}/actions/reclassify` | — |
| الأمر | `CMD-CLM-RECLASSIFY` | إعادة تصنيف الادعاء |
| السياسة | `POL-CLM-RECLASSIFY` | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator sys… |
| الحدث | `EVT-CLM-RECLASSIFIED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-CLAIM` | الادعاء |
| الجدول | `information.claims` | الجدول الرئيسي للادعاء |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-021، REQ-INF-024 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-006 | Manage Evidence |
| الاختبار | TST-CLAIM-SM، TST-SLC02-INVARIANTS | دورة حالات الادعاء، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-CLM-RECLASSIFY -->

</details>

### 5.4 US-BC02-CLM-RETRACT — سحب الادعاء

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

<!-- BEGIN GENERATED: refs US-BC02-CLM-RETRACT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/claims/{id}/actions/retract` | — |
| الأمر | `CMD-CLM-RETRACT` | سحب الادعاء |
| السياسة | `POL-CLM-RETRACT` | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator sys… |
| الحدث | `EVT-CLM-RETRACTED` | يصل إلى: Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation m… |
| الكيان | `AGG-CLAIM` | الادعاء |
| الجدول | `information.claims` | الجدول الرئيسي للادعاء |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-021، REQ-INF-024 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-006 | Manage Evidence |
| الاختبار | TST-CLAIM-SM، TST-SLC02-INVARIANTS | دورة حالات الادعاء، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-CLM-RETRACT -->

</details>

### 5.5 US-BC02-EVL-LINK — ربط رابط الدليل

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

<!-- BEGIN GENERATED: refs US-BC02-EVL-LINK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/evidence-links` | — |
| الأمر | `CMD-EVL-LINK` | ربط رابط الدليل |
| السياسة | `POL-EVL-LINK` | Analyst؛ tenant match; object visible to subject (label ≤ clearance); write permission in org scope |
| الحدث | `EVT-EVL-LINKED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-EVIDENCE-LINK` | رابط الدليل |
| الجدول | `information.evidence_links` | الجدول الرئيسي لرابط الدليل |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-021 | The system shall represent each attribute value of an importance-tier T1 object as a claim linked to its sour… |
| حالة الاستخدام | UC-006 | Manage Evidence |
| الاختبار | TST-EVIDENCE-LINK-SM، TST-SLC02-INVARIANTS | دورة حالات رابط الدليل، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-EVL-LINK -->

</details>

### 5.6 US-BC02-EVL-UNLINK — فك ربط رابط الدليل

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

<!-- BEGIN GENERATED: refs US-BC02-EVL-UNLINK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/evidence-links/{id}/actions/unlink` | — |
| الأمر | `CMD-EVL-UNLINK` | فك ربط رابط الدليل |
| السياسة | `POL-EVL-UNLINK` | Analyst؛ tenant match; object visible to subject (label ≤ clearance); write permission in org scope |
| الحدث | `EVT-EVL-UNLINKED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-EVIDENCE-LINK` | رابط الدليل |
| الجدول | `information.evidence_links` | الجدول الرئيسي لرابط الدليل |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-021 | The system shall represent each attribute value of an importance-tier T1 object as a claim linked to its sour… |
| حالة الاستخدام | UC-006 | Manage Evidence |
| الاختبار | TST-EVIDENCE-LINK-SM، TST-SLC02-INVARIANTS | دورة حالات رابط الدليل، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-EVL-UNLINK -->

</details>

### 5.7 US-BC02-Q-CLM-GET — جلب: Claim with sources (per protection), evidence links, supersession chain

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

<!-- BEGIN GENERATED: refs US-BC02-Q-CLM-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/claims/{claim_id}` | — |
| الاستعلام | `QRY-CLM-GET` | Claim with sources (per protection), evidence links, supersession chain |
| السياسة | `POL-CLM-GET` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-CLAIM` | الادعاء |
| الجدول | `information.claims` | الجدول الرئيسي للادعاء |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-021 | The system shall represent each attribute value of an importance-tier T1 object as a claim linked to its sour… |
| حالة الاستخدام | UC-006 | Manage Evidence |
| الاختبار | TST-CLAIM-SM، TST-SLC02-INVARIANTS | دورة حالات الادعاء، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-CLM-GET -->

</details>

### 5.8 US-UI-SCR22-CLAIM-DETAIL — عرض الادعاء بمصادره وأدلته وسلسلة تصحيحه

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

<!-- BEGIN GENERATED: refs US-UI-SCR22-CLAIM-DETAIL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| المصدر | `21-ui-design.md §11` | — |
| المتطلب | REQ-INF-021 | The system shall represent each attribute value of an importance-tier T1 object as a claim linked to its sour… |
| حالة الاستخدام | UC-006 | Manage Evidence |
<!-- END GENERATED: refs US-UI-SCR22-CLAIM-DETAIL -->

</details>

### 5.9 US-UI-SCR22-CLAIM-FORM — تسجيل ادعاء بمصدره وزمن صحته ودليله

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

<!-- BEGIN GENERATED: refs US-UI-SCR22-CLAIM-FORM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| المصدر | `21-ui-design.md §6.1` | — |
| المتطلبات | REQ-INF-021، REQ-INF-037، REQ-GOV-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-006 | Manage Evidence |
<!-- END GENERATED: refs US-UI-SCR22-CLAIM-FORM -->

</details>

### 5.10 US-UI-SCR22-CORRECT-OR-CHANGE — التمييز بين تصحيح القيمة وتغيرها في الواقع

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

<!-- BEGIN GENERATED: refs US-UI-SCR22-CORRECT-OR-CHANGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| المصدر | `temporal-model.md §3` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-024 | The system shall never overwrite a T1 claim; a correction shall close the record-time interval of the previou… |
<!-- END GENERATED: refs US-UI-SCR22-CORRECT-OR-CHANGE -->

</details>

### 5.11 US-PLT-CLAIMS-IMMUTABLE — عدم الكتابة فوق ادعاءات المستوى الأول أبدًا

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

<!-- BEGIN GENERATED: refs US-PLT-CLAIMS-IMMUTABLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| فحص البنية | FIT-05 | T1 claims are never updated in place except closing recorded_to |
| فحص البنية | FIT-06 | Every attribute declares importance tier |
| المتطلبات | REQ-INF-024، REQ-INF-021 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-006 | Manage Evidence |
<!-- END GENERATED: refs US-PLT-CLAIMS-IMMUTABLE -->

</details>

### 5.12 US-INT-CLAIMS-FROM-ADAPTER — تسجيل قيم الأنظمة الخارجية ادعاءات بمصدرها

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-CLAIMS-FROM-ADAPTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §1` | — |
| المصدر | `THR-S02-01` | — |
| المتطلب | REQ-INF-005 | The system shall ingest external data only through registered adapters or bulk import jobs that record source… |
| حالة الاستخدام | UC-094 | Ingest External Data |
<!-- END GENERATED: refs US-INT-CLAIMS-FROM-ADAPTER -->

</details>

### 5.13 US-OPS-CLAIMS-CURRENT-REBUILD — إعادة بناء القيم الحالية من التاريخ عند اختلافها

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-CLAIMS-CURRENT-REBUILD -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `FM-S02-03` | — |
| المصدر | `temporal-model.md §9` | — |
<!-- END GENERATED: refs US-OPS-CLAIMS-CURRENT-REBUILD -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-GOV-002 | The system shall require a classification on every object of importance tier T1 or T2. | `US-UI-SCR22-CLAIM-FORM` | — |
| REQ-INF-005 | The system shall ingest external data only through registered adapters or bulk import jobs that record source… | `US-INT-CLAIMS-FROM-ADAPTER` | TST-ADAPTER-SM، TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS |
| REQ-INF-021 | The system shall represent each attribute value of an importance-tier T1 object as a claim linked to its sour… | `US-BC02-CLM-ASSERT`، `US-BC02-CLM-CORRECT`، `US-BC02-CLM-RECLASSIFY`، `US-BC02-CLM-RETRACT`، `US-BC02-EVL-LINK`، `US-BC02-EVL-UNLINK`، `US-BC02-Q-CLM-GET`، `US-PLT-CLAIMS-IMMUTABLE`، `US-UI-SCR22-CLAIM-DETAIL`، `US-UI-SCR22-CLAIM-FORM` | TST-CLAIM-SM، TST-ENTITY-SM، TST-EVIDENCE-LINK-SM، TST-SLC02-INVARIANTS |
| REQ-INF-024 | The system shall never overwrite a T1 claim; a correction shall close the record-time interval of the previou… | `US-BC02-CLM-ASSERT`، `US-BC02-CLM-CORRECT`، `US-BC02-CLM-RECLASSIFY`، `US-BC02-CLM-RETRACT`، `US-PLT-CLAIMS-IMMUTABLE`، `US-UI-SCR22-CORRECT-OR-CHANGE` | TST-CLAIM-SM، TST-CONFLICT-SM، TST-SLC02-INVARIANTS، TST-SLC04-INVARIANTS |
| REQ-INF-037 | If a T1 object is submitted without a source reference, then the system shall reject it. | `US-UI-SCR22-CLAIM-FORM` | TST-CLAIM-SM، TST-SLC02-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
