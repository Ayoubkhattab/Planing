---
id: FEAT-INF-REAL-EVENTS
type: feature
title: "تسجيل الأحداث الواقعية"
status: DRAFT
version: "0.1"
capability: CAP-03.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تسجيل الأحداث الواقعية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-REAL-EVENTS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.01 الكيانات والعلاقات (R1) |
| الأدوار | المحلل؛ النظام؛ أي مستخدم مخوَّل |
| الشاشات | SCR-21 الكيانات والأحداث: العرض المحلول |
| حالات الاستخدام | UC-002 |
| القصص | 8: 6 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يوثّق المحلل الأحداث التي وقعت في الواقع ويصنّفها ويعرض صورتها الموحّدة.

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
| `US-BC02-RWE-CHANGE-TYPE` | تغيير نوع الحدث الواقعي | أمر | مسودة |
| `US-BC02-RWE-RECLASSIFY` | إعادة تصنيف الحدث الواقعي | أمر | مسودة |
| `US-BC02-RWE-REGISTER` | تسجيل الحدث الواقعي | أمر | مسودة |
| `US-BC02-RWE-REINSTATE` | إعادة الحدث الواقعي إلى السريان | أمر | مسودة |
| `US-BC02-RWE-RETIRE` | إحالة الحدث الواقعي إلى التقاعد | أمر | مسودة |
| `US-BC02-Q-RWE-GET` | جلب: Resolved real-world event | جلب | مسودة |
| `US-UI-SCR21-EVENT-FUZZY-TIME` | إدخال زمن الحدث التقريبي وعرضه بدقته | واجهة | مسودة |
| `US-PLT-EVENTS-FUZZY-OVERLAP` | مطابقة الأزمنة التقريبية بثلاث نتائج | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-RWE-CHANGE-TYPE — تغيير نوع الحدث الواقعي

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

<!-- BEGIN GENERATED: refs US-BC02-RWE-CHANGE-TYPE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/events/{id}/actions/change-type` | — |
| الأمر | `CMD-RWE-CHANGE-TYPE` | تغيير نوع الحدث الواقعي |
| السياسة | `POL-RWE-CHANGE-TYPE` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-RWE-TYPE-CHANGED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-REALWORLD-EVENT` | الحدث الواقعي |
| الجدول | `information.realworld_events` | الجدول الرئيسي للحدث الواقعي |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… |
| حالة الاستخدام | UC-002 | Manage Event |
| الاختبار | TST-REALWORLD-EVENT-SM، TST-SLC02-INVARIANTS | دورة حالات الحدث الواقعي، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-RWE-CHANGE-TYPE -->

</details>

### 5.2 US-BC02-RWE-RECLASSIFY — إعادة تصنيف الحدث الواقعي

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

<!-- BEGIN GENERATED: refs US-BC02-RWE-RECLASSIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/events/{id}/actions/reclassify` | — |
| الأمر | `CMD-RWE-RECLASSIFY` | إعادة تصنيف الحدث الواقعي |
| السياسة | `POL-RWE-RECLASSIFY` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-RWE-RECLASSIFIED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-REALWORLD-EVENT` | الحدث الواقعي |
| الجدول | `information.realworld_events` | الجدول الرئيسي للحدث الواقعي |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… |
| حالة الاستخدام | UC-002 | Manage Event |
| الاختبار | TST-REALWORLD-EVENT-SM، TST-SLC02-INVARIANTS | دورة حالات الحدث الواقعي، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-RWE-RECLASSIFY -->

</details>

### 5.3 US-BC02-RWE-REGISTER — تسجيل الحدث الواقعي

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

<!-- BEGIN GENERATED: refs US-BC02-RWE-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/events` | — |
| الأمر | `CMD-RWE-REGISTER` | تسجيل الحدث الواقعي |
| السياسة | `POL-RWE-REGISTER` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-RWE-REGISTERED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-REALWORLD-EVENT` | الحدث الواقعي |
| الجدول | `information.realworld_events` | الجدول الرئيسي للحدث الواقعي |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… |
| حالة الاستخدام | UC-002 | Manage Event |
| الاختبار | TST-REALWORLD-EVENT-SM، TST-SLC02-INVARIANTS | دورة حالات الحدث الواقعي، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-RWE-REGISTER -->

</details>

### 5.4 US-BC02-RWE-REINSTATE — إعادة الحدث الواقعي إلى السريان

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

<!-- BEGIN GENERATED: refs US-BC02-RWE-REINSTATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/events/{id}/actions/reinstate` | — |
| الأمر | `CMD-RWE-REINSTATE` | إعادة الحدث الواقعي إلى السريان |
| السياسة | `POL-RWE-REINSTATE` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-RWE-REINSTATED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-REALWORLD-EVENT` | الحدث الواقعي |
| الجدول | `information.realworld_events` | الجدول الرئيسي للحدث الواقعي |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… |
| حالة الاستخدام | UC-002 | Manage Event |
| الاختبار | TST-REALWORLD-EVENT-SM، TST-SLC02-INVARIANTS | دورة حالات الحدث الواقعي، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-RWE-REINSTATE -->

</details>

### 5.5 US-BC02-RWE-RETIRE — إحالة الحدث الواقعي إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC02-RWE-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/events/{id}/actions/retire` | — |
| الأمر | `CMD-RWE-RETIRE` | إحالة الحدث الواقعي إلى التقاعد |
| السياسة | `POL-RWE-RETIRE` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-RWE-RETIRED` | يصل إلى: Search/Graph projections (SLC-05) |
| الكيان | `AGG-REALWORLD-EVENT` | الحدث الواقعي |
| الجدول | `information.realworld_events` | الجدول الرئيسي للحدث الواقعي |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… |
| حالة الاستخدام | UC-002 | Manage Event |
| الاختبار | TST-REALWORLD-EVENT-SM، TST-SLC02-INVARIANTS | دورة حالات الحدث الواقعي، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-RWE-RETIRE -->

</details>

### 5.6 US-BC02-Q-RWE-GET — جلب: Resolved real-world event

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

<!-- BEGIN GENERATED: refs US-BC02-Q-RWE-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/events/{event_id}` | — |
| الاستعلام | `QRY-RWE-GET` | Resolved real-world event |
| السياسة | `POL-RWE-GET` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-REALWORLD-EVENT` | الحدث الواقعي |
| الجدول | `information.realworld_events` | الجدول الرئيسي للحدث الواقعي |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… |
| حالة الاستخدام | UC-002 | Manage Event |
| الاختبار | TST-REALWORLD-EVENT-SM، TST-SLC02-INVARIANTS | دورة حالات الحدث الواقعي، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-RWE-GET -->

</details>

### 5.7 US-UI-SCR21-EVENT-FUZZY-TIME — إدخال زمن الحدث التقريبي وعرضه بدقته

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

<!-- BEGIN GENERATED: refs US-UI-SCR21-EVENT-FUZZY-TIME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-21 | شاشة الكيانات والأحداث: العرض المحلول |
| المصدر | `temporal-model.md §7` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… |
| حالة الاستخدام | UC-002 | Manage Event |
<!-- END GENERATED: refs US-UI-SCR21-EVENT-FUZZY-TIME -->

</details>

### 5.8 US-PLT-EVENTS-FUZZY-OVERLAP — مطابقة الأزمنة التقريبية بثلاث نتائج

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

<!-- BEGIN GENERATED: refs US-PLT-EVENTS-FUZZY-OVERLAP -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `temporal-model.md §7` | — |
| المصدر | `23-crosscutting.md §4` | — |
<!-- END GENERATED: refs US-PLT-EVENTS-FUZZY-OVERLAP -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… | `US-BC02-Q-RWE-GET`، `US-BC02-RWE-CHANGE-TYPE`، `US-BC02-RWE-RECLASSIFY`، `US-BC02-RWE-REGISTER`، `US-BC02-RWE-REINSTATE`، `US-BC02-RWE-RETIRE`، `US-UI-SCR21-EVENT-FUZZY-TIME` | TST-ENTITY-SM، TST-REALWORLD-EVENT-SM، TST-SLC02-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
