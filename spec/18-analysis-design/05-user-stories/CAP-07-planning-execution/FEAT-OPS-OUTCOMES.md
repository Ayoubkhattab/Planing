---
id: FEAT-OPS-OUTCOMES
type: feature
title: "قياس النتائج"
status: DRAFT
version: "0.1"
capability: CAP-07.05
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# قياس النتائج

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-OPS-OUTCOMES |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-07 التخطيط والتنفيذ |
| القدرة الفرعية | CAP-07.05 قياس النتائج (R1) |
| الأدوار | المخطِّط؛ مالك الخطة؛ النظام |
| الشاشات | SCR-35 متابعة التنفيذ |
| حالات الاستخدام | UC-101 |
| القصص | 9: 6 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يسجل المخطط قياسات النتائج مقابل أهدافها ويصححها، فتبقى سلسلة القياس صادقة حتى بعد تغيير الخطة.

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
| `US-BC04-OUT-CORRECT` | تصحيح متتبّع النتائج | أمر | مسودة |
| `US-BC04-OUT-RECORD` | تسجيل متتبّع النتائج | أمر | مسودة |
| `US-BC04-Q-OUT-SERIES` | جلب: Measurement series as known_at | جلب | مسودة |
| `US-BC04-S-OUTCOME-TRACKER-01` | تلقائي: outcome baselined (متتبّع النتائج) | نظام | مسودة |
| `US-BC04-S-OUTCOME-TRACKER-02` | تلقائي: target changed by new baseline (متتبّع النتائج) | نظام | مسودة |
| `US-BC04-S-OUTCOME-TRACKER-03` | تلقائي: plan closed or cancelled (متتبّع النتائج) | نظام | مسودة |
| `US-DOM-OPS-OUTCOME-FROM-TASK` | تسجيل قياس من نتيجة مهمة | نظام | مسودة |
| `US-UI-SCR35-OUTCOME-CHART` | منحنى القياسات مقابل المستهدف | واجهة | مسودة |
| `US-PLT-OPS-OUTCOME-UNITS` | تحويل وحدات القياس محليًا | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-OUT-CORRECT — تصحيح متتبّع النتائج

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

<!-- BEGIN GENERATED: refs US-BC04-OUT-CORRECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/outcome-trackers/{id}/actions/correct` | — |
| الأمر | `CMD-OUT-CORRECT` | تصحيح متتبّع النتائج |
| السياسة | `POL-OUT-CORRECT` | Planner / owner (record, correct)؛ tenant match; object visible; org scope |
| الحدث | `EVT-OUT-MEASUREMENT-CORRECTED` | يصل إلى: Plan progress view; Business telemetry (OUT-05) |
| الكيان | `AGG-OUTCOME-TRACKER` | متتبّع النتائج |
| الجدول | `operations.outcome_trackers` | الجدول الرئيسي لمتتبّع النتائج |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
| الاختبار | TST-OUTCOME-TRACKER-SM، TST-SLC08-INVARIANTS | دورة حالات متتبّع النتائج، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-OUT-CORRECT -->

</details>

### 5.2 US-BC04-OUT-RECORD — تسجيل متتبّع النتائج

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

<!-- BEGIN GENERATED: refs US-BC04-OUT-RECORD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/outcome-trackers/{id}/actions/record` | — |
| الأمر | `CMD-OUT-RECORD` | تسجيل متتبّع النتائج |
| السياسة | `POL-OUT-RECORD` | Planner / owner (record, correct)؛ tenant match; object visible; org scope |
| الحدث | `EVT-OUT-MEASURED` | يصل إلى: Plan progress view; Business telemetry (OUT-05) |
| الكيان | `AGG-OUTCOME-TRACKER` | متتبّع النتائج |
| الجدول | `operations.outcome_trackers` | الجدول الرئيسي لمتتبّع النتائج |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
| الاختبار | TST-OUTCOME-TRACKER-SM، TST-SLC08-INVARIANTS | دورة حالات متتبّع النتائج، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-OUT-RECORD -->

</details>

### 5.3 US-BC04-Q-OUT-SERIES — جلب: Measurement series as known_at

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

<!-- BEGIN GENERATED: refs US-BC04-Q-OUT-SERIES -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/plans/{plan_id}/outcomes/{outcome_id}/measurements` | — |
| الاستعلام | `QRY-OUT-SERIES` | Measurement series as known_at |
| السياسة | `POL-OUT-SERIES` | label rule |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-Q-OUT-SERIES -->

</details>

### 5.4 US-BC04-S-OUTCOME-TRACKER-01 — تلقائي: outcome baselined (متتبّع النتائج)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-S-OUTCOME-TRACKER-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:outcome baselined` | one tracker per (plan, outcome id); target copied from baseline |
| الانتقال | ∅ ← ACTIVE | — |
| الحدث | `EVT-OUT-TRACKER-CREATED` | يصل إلى: Plan progress view; Business telemetry (OUT-05) |
| الكيان | `AGG-OUTCOME-TRACKER` | متتبّع النتائج |
| الجدول | `operations.outcome_trackers` | الجدول الرئيسي لمتتبّع النتائج |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
| الاختبار | TST-OUTCOME-TRACKER-SM، TST-SLC08-INVARIANTS | دورة حالات متتبّع النتائج، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-S-OUTCOME-TRACKER-01 -->

</details>

### 5.5 US-BC04-S-OUTCOME-TRACKER-02 — تلقائي: target changed by new baseline (متتبّع النتائج)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-S-OUTCOME-TRACKER-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:target changed by new baseline` | target history appended (valid time = baseline time) |
| الانتقال | ACTIVE ← (بلا تغيير) | — |
| الحدث | `EVT-OUT-TARGET-CHANGED` | يصل إلى: Plan progress view; Business telemetry (OUT-05) |
| الكيان | `AGG-OUTCOME-TRACKER` | متتبّع النتائج |
| الجدول | `operations.outcome_trackers` | الجدول الرئيسي لمتتبّع النتائج |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
| الاختبار | TST-OUTCOME-TRACKER-SM، TST-SLC08-INVARIANTS | دورة حالات متتبّع النتائج، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-S-OUTCOME-TRACKER-02 -->

</details>

### 5.6 US-BC04-S-OUTCOME-TRACKER-03 — تلقائي: plan closed or cancelled (متتبّع النتائج)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-S-OUTCOME-TRACKER-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:plan closed or cancelled` | system |
| الانتقال | ACTIVE ← CLOSED | — |
| الحدث | `EVT-OUT-TRACKER-CLOSED` | يصل إلى: Plan progress view; Business telemetry (OUT-05) |
| الكيان | `AGG-OUTCOME-TRACKER` | متتبّع النتائج |
| الجدول | `operations.outcome_trackers` | الجدول الرئيسي لمتتبّع النتائج |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
| الاختبار | TST-OUTCOME-TRACKER-SM، TST-SLC08-INVARIANTS | دورة حالات متتبّع النتائج، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-S-OUTCOME-TRACKER-03 -->

</details>

### 5.7 US-DOM-OPS-OUTCOME-FROM-TASK — تسجيل قياس من نتيجة مهمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-OPS-OUTCOME-FROM-TASK -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `decision-plan-spec.md §4` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
<!-- END GENERATED: refs US-DOM-OPS-OUTCOME-FROM-TASK -->

</details>

### 5.8 US-UI-SCR35-OUTCOME-CHART — منحنى القياسات مقابل المستهدف

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

<!-- BEGIN GENERATED: refs US-UI-SCR35-OUTCOME-CHART -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-35 | شاشة متابعة التنفيذ |
| المصدر | `decision-plan-spec.md §4` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
<!-- END GENERATED: refs US-UI-SCR35-OUTCOME-CHART -->

</details>

### 5.9 US-PLT-OPS-OUTCOME-UNITS — تحويل وحدات القياس محليًا

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

<!-- BEGIN GENERATED: refs US-PLT-OPS-OUTCOME-UNITS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `US-BC04-OUT-RECORD` | — |
| فحص البنية | FIT-12 | No external network dependency at runtime or build (air-gapped) |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
<!-- END GENERATED: refs US-PLT-OPS-OUTCOME-UNITS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. | `US-BC04-OUT-CORRECT`، `US-BC04-OUT-RECORD`، `US-BC04-Q-OUT-SERIES`، `US-BC04-S-OUTCOME-TRACKER-01`، `US-BC04-S-OUTCOME-TRACKER-02`، `US-BC04-S-OUTCOME-TRACKER-03`، `US-DOM-OPS-OUTCOME-FROM-TASK`، `US-PLT-OPS-OUTCOME-UNITS`، `US-UI-SCR35-OUTCOME-CHART` | TST-OUTCOME-TRACKER-SM، TST-SLC08-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
