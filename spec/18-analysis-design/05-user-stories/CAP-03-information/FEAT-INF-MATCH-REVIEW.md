---
id: FEAT-INF-MATCH-REVIEW
type: feature
title: "مراجعة تطابق الكيانات"
status: DRAFT
version: "0.1"
capability: CAP-03.05
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مراجعة تطابق الكيانات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-MATCH-REVIEW |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.05 مطابقة الكيانات (R1) |
| الأدوار | المحلل؛ الشخص الثاني؛ النظام |
| الشاشات | SCR-06 قوائم المراجعة، SCR-26 التعارض ومطابقة الكيانات |
| حالات الاستخدام | UC-007 |
| القصص | 15: 11 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يراجع المحللون الكيانات المشتبه بأنها الشيء نفسه ويقررون دمجها أو فصلها بقرار موثق ومؤكد من محلل ثانٍ.

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
| QAS-ER-001 | candidate recall on labelled AR/EN test set | ≥ 95 % of true matches proposed |
| QAS-ER-003 | new entity registered | candidates visible p95 ≤ 60 s |
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
| `US-BC02-ER-CONFIRM-MATCH` | تأكيد تطابق حالة مطابقة الكيانات | أمر | مسودة |
| `US-BC02-ER-DECIDE-MATCH` | الحكم بتطابق حالة مطابقة الكيانات | أمر | مسودة |
| `US-BC02-ER-DECIDE-NOT-MATCH` | الحكم بعدم تطابق حالة مطابقة الكيانات | أمر | مسودة |
| `US-BC02-ER-PARK` | تأجيل حالة مطابقة الكيانات | أمر | مسودة |
| `US-BC02-ER-PROPOSE` | اقتراح حالة مطابقة الكيانات | أمر | مسودة |
| `US-BC02-ER-RESUME` | استئناف حالة مطابقة الكيانات | أمر | مسودة |
| `US-BC02-ER-START-REVIEW` | بدء مراجعة حالة مطابقة الكيانات | أمر | مسودة |
| `US-BC02-ER-WITHDRAW` | سحب حالة مطابقة الكيانات | أمر | مسودة |
| `US-BC02-Q-ER-GET` | جلب: Case with side-by-side feature comparison (visible claims only) | جلب | مسودة |
| `US-BC02-Q-ER-QUEUE` | جلب: Review queue by state, entity type, score, ruleset | جلب | مسودة |
| `US-BC02-S-ER-CASE-01` | تلقائي: candidate generator score ≥ propose threshold (حالة مطابقة الكيانات) | نظام | مسودة |
| `US-UI-SCR06-ER-QUEUE` | قائمة حالات المطابقة مرتبة بالدرجة والنوع | واجهة | مسودة |
| `US-UI-SCR26-ER-COMPARE` | مقارنة الكيانين جنبًا إلى جنب واتخاذ القرار | واجهة | مسودة |
| `US-PLT-ER-CANDIDATES` | اقتراح المطابقات المحتملة خلال دقيقة | منصة | مسودة |
| `US-OPS-ER-QUEUE-WATCH` | مراقبة تأخر اقتراح المطابقات وحجم قائمة المراجعة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-ER-CONFIRM-MATCH — تأكيد تطابق حالة مطابقة الكيانات

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

<!-- BEGIN GENERATED: refs US-BC02-ER-CONFIRM-MATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/er-cases/{id}/actions/confirm-match` | — |
| الأمر | `CMD-ER-CONFIRM-MATCH` | تأكيد تطابق حالة مطابقة الكيانات |
| السياسة | `POL-ER-CONFIRM-MATCH` | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ tenant mat… |
| الحدث | `EVT-ER-MATCH-CONFIRMED` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-ER-CONFIRM-MATCH -->

</details>

### 5.2 US-BC02-ER-DECIDE-MATCH — الحكم بتطابق حالة مطابقة الكيانات

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

<!-- BEGIN GENERATED: refs US-BC02-ER-DECIDE-MATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/er-cases/{id}/actions/decide-match` | — |
| الأمر | `CMD-ER-DECIDE-MATCH` | الحكم بتطابق حالة مطابقة الكيانات |
| السياسة | `POL-ER-DECIDE-MATCH` | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ tenant mat… |
| الحدث | `EVT-ER-MATCHED` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-ER-DECIDE-MATCH -->

</details>

### 5.3 US-BC02-ER-DECIDE-NOT-MATCH — الحكم بعدم تطابق حالة مطابقة الكيانات

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

<!-- BEGIN GENERATED: refs US-BC02-ER-DECIDE-NOT-MATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/er-cases/{id}/actions/decide-not-match` | — |
| الأمر | `CMD-ER-DECIDE-NOT-MATCH` | الحكم بعدم تطابق حالة مطابقة الكيانات |
| السياسة | `POL-ER-DECIDE-NOT-MATCH` | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ tenant mat… |
| الحدث | `EVT-ER-NOT-MATCHED` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-ER-DECIDE-NOT-MATCH -->

</details>

### 5.4 US-BC02-ER-PARK — تأجيل حالة مطابقة الكيانات

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

<!-- BEGIN GENERATED: refs US-BC02-ER-PARK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/er-cases/{id}/actions/park` | — |
| الأمر | `CMD-ER-PARK` | تأجيل حالة مطابقة الكيانات |
| السياسة | `POL-ER-PARK` | Analyst (park)؛ tenant match; object visible |
| الحدث | `EVT-ER-PARKED` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-ER-PARK -->

</details>

### 5.5 US-BC02-ER-PROPOSE — اقتراح حالة مطابقة الكيانات

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

<!-- BEGIN GENERATED: refs US-BC02-ER-PROPOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/er-cases` | — |
| الأمر | `CMD-ER-PROPOSE` | اقتراح حالة مطابقة الكيانات |
| السياسة | `POL-ER-PROPOSE` | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ tenant mat… |
| الحدث | `EVT-ER-PROPOSED` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-ER-PROPOSE -->

</details>

### 5.6 US-BC02-ER-RESUME — استئناف حالة مطابقة الكيانات

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

<!-- BEGIN GENERATED: refs US-BC02-ER-RESUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/er-cases/{id}/actions/resume` | — |
| الأمر | `CMD-ER-RESUME` | استئناف حالة مطابقة الكيانات |
| السياسة | `POL-ER-RESUME` | Analyst (resume)؛ tenant match; object visible |
| الحدث | `EVT-ER-RESUMED` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-ER-RESUME -->

</details>

### 5.7 US-BC02-ER-START-REVIEW — بدء مراجعة حالة مطابقة الكيانات

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

<!-- BEGIN GENERATED: refs US-BC02-ER-START-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/er-cases/{id}/actions/start-review` | — |
| الأمر | `CMD-ER-START-REVIEW` | بدء مراجعة حالة مطابقة الكيانات |
| السياسة | `POL-ER-START-REVIEW` | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ tenant mat… |
| الحدث | `EVT-ER-REVIEW-STARTED` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-ER-START-REVIEW -->

</details>

### 5.8 US-BC02-ER-WITHDRAW — سحب حالة مطابقة الكيانات

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

<!-- BEGIN GENERATED: refs US-BC02-ER-WITHDRAW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/er-cases/{id}/actions/withdraw` | — |
| الأمر | `CMD-ER-WITHDRAW` | سحب حالة مطابقة الكيانات |
| السياسة | `POL-ER-WITHDRAW` | Analyst (withdraw)؛ tenant match; object visible |
| الحدث | `EVT-ER-WITHDRAWN` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-ER-WITHDRAW -->

</details>

### 5.9 US-BC02-Q-ER-GET — جلب: Case with side-by-side feature comparison (visible claims only)

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

<!-- BEGIN GENERATED: refs US-BC02-Q-ER-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/er-cases/{case_id}` | — |
| الاستعلام | `QRY-ER-GET` | Case with side-by-side feature comparison (visible claims only) |
| السياسة | `POL-ER-GET` | Analyst; both entities visible |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-032 | When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, m… |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-Q-ER-GET -->

</details>

### 5.10 US-BC02-Q-ER-QUEUE — جلب: Review queue by state, entity type, score, ruleset

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

<!-- BEGIN GENERATED: refs US-BC02-Q-ER-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/er-cases` | — |
| الاستعلام | `QRY-ER-QUEUE` | Review queue by state, entity type, score, ruleset |
| السياسة | `POL-ER-QUEUE` | Analyst; cases where both entities are visible |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-032 | When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, m… |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-Q-ER-QUEUE -->

</details>

### 5.11 US-BC02-S-ER-CASE-01 — تلقائي: candidate generator score ≥ propose threshold (حالة مطابقة الكيانات)

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

<!-- BEGIN GENERATED: refs US-BC02-S-ER-CASE-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:candidate generator score ≥ propose threshold` | pair not already in the same cluster; no NOT_A_MATCH link between their clusters; no non-terminal case for th… |
| الانتقال | ∅ ← CANDIDATE | — |
| الحدث | `EVT-ER-PROPOSED` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-S-ER-CASE-01 -->

</details>

### 5.12 US-UI-SCR06-ER-QUEUE — قائمة حالات المطابقة مرتبة بالدرجة والنوع

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

<!-- BEGIN GENERATED: refs US-UI-SCR06-ER-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `THR-S04-02` | — |
| حالة الاستخدام | UC-007 | Resolve Entity |
<!-- END GENERATED: refs US-UI-SCR06-ER-QUEUE -->

</details>

### 5.13 US-UI-SCR26-ER-COMPARE — مقارنة الكيانين جنبًا إلى جنب واتخاذ القرار

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

<!-- BEGIN GENERATED: refs US-UI-SCR26-ER-COMPARE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-26 | شاشة التعارض ومطابقة الكيانات |
| حالة الاستخدام | UC-007 | Resolve Entity |
| المتطلب | REQ-INF-032 | When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, m… |
| حالة الاستخدام | UC-007 | Resolve Entity |
<!-- END GENERATED: refs US-UI-SCR26-ER-COMPARE -->

</details>

### 5.14 US-PLT-ER-CANDIDATES — اقتراح المطابقات المحتملة خلال دقيقة

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

<!-- BEGIN GENERATED: refs US-PLT-ER-CANDIDATES -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-ER-001 | candidate recall on labelled AR/EN test set → ≥ 95 % of true matches proposed |
| الجودة | QAS-ER-003 | new entity registered → candidates visible p95 ≤ 60 s |
| القرار المعماري | ADR-P15 | Language & Entity Matching |
| المتطلب | REQ-INF-032 | When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, m… |
| حالة الاستخدام | UC-007 | Resolve Entity |
<!-- END GENERATED: refs US-PLT-ER-CANDIDATES -->

</details>

### 5.15 US-OPS-ER-QUEUE-WATCH — مراقبة تأخر اقتراح المطابقات وحجم قائمة المراجعة

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

<!-- BEGIN GENERATED: refs US-OPS-ER-QUEUE-WATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc04.md` | — |
| المصدر | `FM-S04-02` | — |
<!-- END GENERATED: refs US-OPS-ER-QUEUE-WATCH -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-032 | When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, m… | `US-BC02-ER-CONFIRM-MATCH`، `US-BC02-ER-DECIDE-MATCH`، `US-BC02-ER-DECIDE-NOT-MATCH`، `US-BC02-ER-PARK`، `US-BC02-ER-PROPOSE`، `US-BC02-ER-RESUME`، `US-BC02-ER-START-REVIEW`، `US-BC02-ER-WITHDRAW`، `US-BC02-Q-ER-GET`، `US-BC02-Q-ER-QUEUE`، `US-BC02-S-ER-CASE-01`، `US-PLT-ER-CANDIDATES`، `US-UI-SCR26-ER-COMPARE` | TST-ER-CASE-SM، TST-MATCH-RULESET-SM، TST-SLC04-INVARIANTS |
| REQ-INF-033 | When entities are matched, the system shall record a same-as link with the decision, reviewer and time, keep… | كل قصص الأوامر والنظام في الميزة (9) | TST-ER-CASE-SM، TST-SLC04-INVARIANTS |
| REQ-INF-034 | When a match is reversed, the system shall close the same-as link so that each original entity again resolves… | كل قصص الأوامر والنظام في الميزة (9) | TST-ER-CASE-SM، TST-SLC04-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
