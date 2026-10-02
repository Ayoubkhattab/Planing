---
id: FEAT-OPS-EXEC-TRACKING
type: feature
title: "متابعة تنفيذ الخطة"
status: DRAFT
version: "0.1"
capability: CAP-07.05
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# متابعة تنفيذ الخطة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-OPS-EXEC-TRACKING |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-07 التخطيط والتنفيذ |
| القدرة الفرعية | CAP-07.05 قياس النتائج (R1) |
| الأدوار | المدير؛ المخطِّط؛ القيادي التنفيذي |
| الشاشات | SCR-35 متابعة التنفيذ |
| حالات الاستخدام | — |
| القصص | 5: 1 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يرى المدير والتنفيذي تقدم الخطة: المهام حسب حالتها، والمعالم، والنتائج مقابل المستهدف.

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
| QAS-PERF-002 | reads a single object or a list page | single object p95 ≤ 300 ms; list page p95 ≤ 1 s |
| QAS-PERF-021 | plan version baselined with 500 task-generating activities | task synchronization completes ≤ 60 s; idempotent on retry |
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
| `US-BC04-Q-PLN-PROGRESS` | جلب: Tasks by activity and state, milestones, outcome progress vs targets | جلب | مسودة |
| `US-UI-SCR35-DRILLDOWN` | الانتقال من النشاط إلى مهامه | واجهة | مسودة |
| `US-UI-SCR35-EXEC-SUMMARY` | ملخص مجمّع للقيادي التنفيذي | واجهة | مسودة |
| `US-UI-SCR35-PROGRESS-BOARD` | لوحة تقدم الخطة بالمهام والمعالم والنتائج | واجهة | مسودة |
| `US-PLT-OPS-PROGRESS-READ` | قراءة تقدم خطة كبيرة خلال ثانية | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-Q-PLN-PROGRESS — جلب: Tasks by activity and state, milestones, outcome progress vs targets

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

<!-- BEGIN GENERATED: refs US-BC04-Q-PLN-PROGRESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/plans/{plan_id}/progress` | — |
| الاستعلام | `QRY-PLN-PROGRESS` | Tasks by activity and state, milestones, outcome progress vs targets |
| السياسة | `POL-PLN-PROGRESS` | label rule; visible tasks only |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-Q-PLN-PROGRESS -->

</details>

### 5.2 US-UI-SCR35-DRILLDOWN — الانتقال من النشاط إلى مهامه

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR35-DRILLDOWN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-35 | شاشة متابعة التنفيذ |
| الشاشة | SCR-02 | شاشة تفاصيل المهمة وسجلها |
| المصدر | `21-ui-design.md §3` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR35-DRILLDOWN -->

</details>

### 5.3 US-UI-SCR35-EXEC-SUMMARY — ملخص مجمّع للقيادي التنفيذي

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR35-EXEC-SUMMARY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-35 | شاشة متابعة التنفيذ |
| المصدر | `21-ui-design.md §5` | — |
| المصدر | `POL-AGG-STATS` | — |
<!-- END GENERATED: refs US-UI-SCR35-EXEC-SUMMARY -->

</details>

### 5.4 US-UI-SCR35-PROGRESS-BOARD — لوحة تقدم الخطة بالمهام والمعالم والنتائج

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

<!-- BEGIN GENERATED: refs US-UI-SCR35-PROGRESS-BOARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-35 | شاشة متابعة التنفيذ |
| المصدر | `QRY-PLN-PROGRESS` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. |
| حالة الاستخدام | UC-101 | Measure Plan Outcome |
<!-- END GENERATED: refs US-UI-SCR35-PROGRESS-BOARD -->

</details>

### 5.5 US-PLT-OPS-PROGRESS-READ — قراءة تقدم خطة كبيرة خلال ثانية

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

<!-- BEGIN GENERATED: refs US-PLT-OPS-PROGRESS-READ -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-002 | reads a single object or a list page → single object p95 ≤ 300 ms; list page p95 ≤ 1 s |
| الجودة | QAS-PERF-021 | plan version baselined with 500 task-generating activities → task synchronization completes ≤ 60 s; idempoten… |
| المصدر | `QRY-PLN-PROGRESS` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-OPS-PROGRESS-READ -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. | `US-BC04-Q-PLN-PROGRESS`، `US-UI-SCR35-PROGRESS-BOARD` | TST-OUTCOME-TRACKER-SM، TST-SLC08-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
