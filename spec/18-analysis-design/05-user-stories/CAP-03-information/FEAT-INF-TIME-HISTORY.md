---
id: FEAT-INF-TIME-HISTORY
type: feature
title: "تاريخ المعلومة عبر الزمن"
status: DRAFT
version: "0.1"
capability: CAP-03.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تاريخ المعلومة عبر الزمن

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-TIME-HISTORY |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.04 الزمن والتاريخ (R1) |
| الأدوار | المحلل؛ أي مستخدم مخوَّل |
| الشاشات | SCR-21 الكيانات والأحداث: العرض المحلول، SCR-22 الادعاء والدليل والمصدر |
| حالات الاستخدام | UC-096 |
| القصص | 6: 2 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعرف المستخدم ما كان صحيحًا في أي وقت وما كان معروفًا عنه حينها ويسجّل المحلل تغيّر القيم بمرور الزمن.

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
| QAS-TMP-001 | asks for state as of valid time T known at record time K | 100 % agreement with temporal oracle corpus |
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
| `US-BC02-CLM-RECORD-CHANGE` | تسجيل تغيير في الادعاء | أمر | مسودة |
| `US-BC02-Q-ENT-CLAIMS` | جلب: Claim history (predicate, valid_at, known_at, include_closed) | جلب | مسودة |
| `US-UI-SCR21-AS-OF` | عرض الكيان كما كان في وقت سابق | واجهة | مسودة |
| `US-UI-SCR22-CLAIM-TIMELINE` | خط زمني لصحة الادعاء وتسجيله وتصحيحاته | واجهة | مسودة |
| `US-PLT-TIME-INTERVALS` | فترتا الصحة والتسجيل لكل ادعاء دون تداخل | منصة | مسودة |
| `US-PLT-TIME-ORACLE` | مطابقة استعلامات الزمن لمرجع الاختبار كاملًا | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-CLM-RECORD-CHANGE — تسجيل تغيير في الادعاء

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

<!-- BEGIN GENERATED: refs US-BC02-CLM-RECORD-CHANGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/claims/{id}/actions/record-change` | — |
| الأمر | `CMD-CLM-RECORD-CHANGE` | تسجيل تغيير في الادعاء |
| السياسة | `POL-CLM-RECORD-CHANGE` | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator sys… |
| الحدث | `EVT-CLM-CHANGED` | يصل إلى: Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation m… |
| الكيان | `AGG-CLAIM` | الادعاء |
| الجدول | `information.claims` | الجدول الرئيسي للادعاء |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-022 | The system shall record a valid-time interval and a record-time interval for every T1 claim. |
| الاختبار | TST-CLAIM-SM، TST-SLC02-INVARIANTS | دورة حالات الادعاء، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-CLM-RECORD-CHANGE -->

</details>

### 5.2 US-BC02-Q-ENT-CLAIMS — جلب: Claim history (predicate, valid_at, known_at, include_closed)

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

<!-- BEGIN GENERATED: refs US-BC02-Q-ENT-CLAIMS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/entities/{entity_id}/claims` | — |
| الاستعلام | `QRY-ENT-CLAIMS` | Claim history (predicate, valid_at, known_at, include_closed) |
| السياسة | `POL-ENT-CLAIMS` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-022 | The system shall record a valid-time interval and a record-time interval for every T1 claim. |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-ENT-CLAIMS -->

</details>

### 5.3 US-UI-SCR21-AS-OF — عرض الكيان كما كان في وقت سابق

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

<!-- BEGIN GENERATED: refs US-UI-SCR21-AS-OF -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-096 | Query State As-Of / As-Known-At |
| الشاشة | SCR-21 | شاشة الكيانات والأحداث: العرض المحلول |
| المصدر | `21-ui-design.md §3` | — |
| المتطلب | REQ-INF-023 | When a query specifies a valid time T, a record time K, or both, the system shall return the state valid at T… |
| حالة الاستخدام | UC-096 | Query State As-Of / As-Known-At |
<!-- END GENERATED: refs US-UI-SCR21-AS-OF -->

</details>

### 5.4 US-UI-SCR22-CLAIM-TIMELINE — خط زمني لصحة الادعاء وتسجيله وتصحيحاته

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

<!-- BEGIN GENERATED: refs US-UI-SCR22-CLAIM-TIMELINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| المصدر | `temporal-model.md §3` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-022 | The system shall record a valid-time interval and a record-time interval for every T1 claim. |
<!-- END GENERATED: refs US-UI-SCR22-CLAIM-TIMELINE -->

</details>

### 5.5 US-PLT-TIME-INTERVALS — فترتا الصحة والتسجيل لكل ادعاء دون تداخل

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

<!-- BEGIN GENERATED: refs US-PLT-TIME-INTERVALS -->
| البند | المعرّف | المعنى |
|---|---|---|
| فحص البنية | FIT-09 | No created_at/updated_at used as business time |
| المصدر | `temporal-model.md §2` | — |
| المتطلب | REQ-INF-022 | The system shall record a valid-time interval and a record-time interval for every T1 claim. |
<!-- END GENERATED: refs US-PLT-TIME-INTERVALS -->

</details>

### 5.6 US-PLT-TIME-ORACLE — مطابقة استعلامات الزمن لمرجع الاختبار كاملًا

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

<!-- BEGIN GENERATED: refs US-PLT-TIME-ORACLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-TMP-001 | asks for state as of valid time T known at record time K → 100 % agreement with temporal oracle corpus |
| حالة الاستخدام | UC-096 | Query State As-Of / As-Known-At |
| المتطلب | REQ-INF-023 | When a query specifies a valid time T, a record time K, or both, the system shall return the state valid at T… |
| حالة الاستخدام | UC-096 | Query State As-Of / As-Known-At |
<!-- END GENERATED: refs US-PLT-TIME-ORACLE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-022 | The system shall record a valid-time interval and a record-time interval for every T1 claim. | `US-BC02-CLM-RECORD-CHANGE`، `US-BC02-Q-ENT-CLAIMS`، `US-PLT-TIME-INTERVALS`، `US-UI-SCR22-CLAIM-TIMELINE` | TST-CLAIM-SM، TST-SLC02-INVARIANTS |
| REQ-INF-023 | When a query specifies a valid time T, a record time K, or both, the system shall return the state valid at T… | `US-PLT-TIME-ORACLE`، `US-UI-SCR21-AS-OF` | TST-SLC02-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
