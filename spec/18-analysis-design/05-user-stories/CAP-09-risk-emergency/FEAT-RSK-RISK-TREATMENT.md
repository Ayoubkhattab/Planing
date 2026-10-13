---
id: FEAT-RSK-RISK-TREATMENT
type: feature
title: "تقييم المخاطر ومعالجتها"
status: DRAFT
version: "0.1"
capability: CAP-09.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تقييم المخاطر ومعالجتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RSK-RISK-TREATMENT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-09 المخاطر والطوارئ |
| القدرة الفرعية | CAP-09.01 إدارة المخاطر (R3) |
| الأدوار | مقيّم الخطر؛ موافق المعالجة؛ مدير المخاطر |
| الشاشات | SCR-47 سجل المخاطر والحوادث |
| حالات الاستخدام | UC-140، UC-141 |
| القصص | 5: 4 من المواصفة، و1 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يقيّم المقيّم الخطر — غير من سجّله — ويخطط لمعالجته ثم يغلقه بمبرر صريح.

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
| `US-BC04-RIS-ASSESS` | تقييم الخطر | أمر | مسودة |
| `US-BC04-RIS-CLOSE` | إغلاق الخطر | أمر | مسودة |
| `US-BC04-RIS-PLAN-TREATMENT` | تخطيط معالجة الخطر | أمر | مسودة |
| `US-BC04-RIS-REASSESS` | إعادة تقييم الخطر | أمر | مسودة |
| `US-UI-SCR47-RISK-TREATMENT` | تقييم الخطر ومعالجته وإغلاقه بمبرر | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-RIS-ASSESS — تقييم الخطر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-RIS-ASSESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/risks/{id}/actions/assess` | — |
| الأمر | `CMD-RIS-ASSESS` | تقييم الخطر |
| السياسة | `POL-RIS-ASSESS` | مقيّم (تقييم، إعادة تقييم)؛ tenant match; scope_refs visible to actor |
| الحدث | `EVT-RIS-ASSESSED` | يصل إلى: Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| الكيان | `AGG-RISK` | الخطر |
| الجدول | `operations.risks` | الجدول الرئيسي للخطر |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-001، REQ-RCM-002، REQ-RCM-003، REQ-RCM-004، REQ-RCM-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-140، UC-141 | Identify & Assess Risk؛ Treat & Close Risk |
| الاختبار | TST-RISK-SM، TST-SLC17-INVARIANTS | دورة حالات الخطر، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-RIS-ASSESS -->

</details>

### 5.2 US-BC04-RIS-CLOSE — إغلاق الخطر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-RIS-CLOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/risks/{id}/actions/close` | — |
| الأمر | `CMD-RIS-CLOSE` | إغلاق الخطر |
| السياسة | `POL-RIS-CLOSE` | مدير المخاطر؛ tenant match; scope_refs visible to actor |
| الحدث | `EVT-RIS-CLOSED` | يصل إلى: Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| الكيان | `AGG-RISK` | الخطر |
| الجدول | `operations.risks` | الجدول الرئيسي للخطر |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-001، REQ-RCM-002، REQ-RCM-003، REQ-RCM-004، REQ-RCM-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-140، UC-141 | Identify & Assess Risk؛ Treat & Close Risk |
| الاختبار | TST-RISK-SM، TST-SLC17-INVARIANTS | دورة حالات الخطر، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-RIS-CLOSE -->

</details>

### 5.3 US-BC04-RIS-PLAN-TREATMENT — تخطيط معالجة الخطر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-RIS-PLAN-TREATMENT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/risks/{id}/actions/plan-treatment` | — |
| الأمر | `CMD-RIS-PLAN-TREATMENT` | تخطيط معالجة الخطر |
| السياسة | `POL-RIS-PLAN-TREATMENT` | موافق المعالجة مخوَّل؛ tenant match; scope_refs visible to actor |
| الحدث | `EVT-RIS-TREATMENT-PLANNED` | يصل إلى: Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| الكيان | `AGG-RISK` | الخطر |
| الجدول | `operations.risks` | الجدول الرئيسي للخطر |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-001، REQ-RCM-002، REQ-RCM-003، REQ-RCM-004، REQ-RCM-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-140، UC-141 | Identify & Assess Risk؛ Treat & Close Risk |
| الاختبار | TST-RISK-SM، TST-SLC17-INVARIANTS | دورة حالات الخطر، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-RIS-PLAN-TREATMENT -->

</details>

### 5.4 US-BC04-RIS-REASSESS — إعادة تقييم الخطر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-RIS-REASSESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/risks/{id}/actions/reassess` | — |
| الأمر | `CMD-RIS-REASSESS` | إعادة تقييم الخطر |
| السياسة | `POL-RIS-REASSESS` | مقيّم (تقييم، إعادة تقييم)؛ tenant match; scope_refs visible to actor |
| الحدث | `EVT-RIS-REASSESSED` | يصل إلى: Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| الكيان | `AGG-RISK` | الخطر |
| الجدول | `operations.risks` | الجدول الرئيسي للخطر |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-001، REQ-RCM-002، REQ-RCM-003، REQ-RCM-004، REQ-RCM-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-140، UC-141 | Identify & Assess Risk؛ Treat & Close Risk |
| الاختبار | TST-RISK-SM، TST-SLC17-INVARIANTS | دورة حالات الخطر، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-RIS-REASSESS -->

</details>

### 5.5 US-UI-SCR47-RISK-TREATMENT — تقييم الخطر ومعالجته وإغلاقه بمبرر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR47-RISK-TREATMENT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-RCM-002، REQ-RCM-004، REQ-RCM-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-140، UC-141 | Identify & Assess Risk؛ Treat & Close Risk |
<!-- END GENERATED: refs US-UI-SCR47-RISK-TREATMENT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RCM-001 | The system shall allow an authorized actor to identify a risk with a hazard category, description, and at lea… | كل قصص الميزة المأخوذة من المواصفة (4) | TST-RISK-SM |
| REQ-RCM-002 | The system shall require a likelihood and an impact rating (1-5) to assess a risk, and shall compute the risk… | `US-BC04-RIS-ASSESS`، `US-BC04-RIS-CLOSE`، `US-BC04-RIS-PLAN-TREATMENT`، `US-BC04-RIS-REASSESS`، `US-UI-SCR47-RISK-TREATMENT` | TST-RISK-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-003 | Where tenant policy requires segregation of duties, the system shall reject a risk assessment or reassessment… | كل قصص الميزة المأخوذة من المواصفة (4) | TST-RISK-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-004 | The system shall require at least one treatment action for a risk moving to treated status, unless the chosen… | `US-BC04-RIS-ASSESS`، `US-BC04-RIS-CLOSE`، `US-BC04-RIS-PLAN-TREATMENT`، `US-BC04-RIS-REASSESS`، `US-UI-SCR47-RISK-TREATMENT` | TST-RISK-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-005 | The system shall require an explicit rationale to close a risk, and shall provide no command to reopen a clos… | `US-BC04-RIS-ASSESS`، `US-BC04-RIS-CLOSE`، `US-BC04-RIS-PLAN-TREATMENT`، `US-BC04-RIS-REASSESS`، `US-UI-SCR47-RISK-TREATMENT` | TST-RISK-SM، TST-SLC17-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
