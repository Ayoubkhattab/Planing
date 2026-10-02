---
id: FEAT-INF-ENTITY-SPLIT
type: feature
title: "فصل الكيانات المدموجة خطأً"
status: DRAFT
version: "0.1"
capability: CAP-03.05
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# فصل الكيانات المدموجة خطأً

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-ENTITY-SPLIT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.05 مطابقة الكيانات (R1) |
| الأدوار | المحلل؛ الشخص الثاني؛ أي مستخدم مخوَّل |
| الشاشات | SCR-26 التعارض ومطابقة الكيانات، SCR-21 الكيانات والأحداث: العرض المحلول |
| حالات الاستخدام | UC-104 |
| القصص | 7: 3 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يستطيع المحلل التراجع عن دمج خاطئ فيعود كل كيان بمعلوماته الخاصة كما كانت.

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
| QAS-PERF-015 | resolved read of clustered entity | ≤ 20 % overhead vs unclustered; p95 ≤ 300 ms |
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
| `US-BC02-ER-REQUEST-SPLIT` | طلب فصل حالة مطابقة الكيانات | أمر | مسودة |
| `US-BC02-ER-SPLIT` | فصل حالة مطابقة الكيانات | أمر | مسودة |
| `US-BC02-Q-CLUSTER-GET` | جلب: Cluster members, canonical URN, links, as known_at | جلب | مسودة |
| `US-UI-SCR26-CLUSTER-VIEW` | عرض أعضاء الهوية الموحدة وطلب فصلها | واجهة | مسودة |
| `US-PLT-CLUSTER-RESOLVED-READ` | قراءة الكيان المدموج دون بطء ملحوظ | منصة | مسودة |
| `US-OPS-CLUSTER-RECONCILE` | اكتشاف اختلاف جدول الهويات وإعادة بنائه | تشغيل | مسودة |
| `US-OPS-ENTITY-BULK-SPLIT` | فصل دفعة دمج خاطئ بقائمة حالات | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-ER-REQUEST-SPLIT — طلب فصل حالة مطابقة الكيانات

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

<!-- BEGIN GENERATED: refs US-BC02-ER-REQUEST-SPLIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/er-cases/{id}/actions/request-split` | — |
| الأمر | `CMD-ER-REQUEST-SPLIT` | طلب فصل حالة مطابقة الكيانات |
| السياسة | `POL-ER-REQUEST-SPLIT` | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ tenant mat… |
| الحدث | `EVT-ER-SPLIT-REQUESTED` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-104 | Split Merged Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-ER-REQUEST-SPLIT -->

</details>

### 5.2 US-BC02-ER-SPLIT — فصل حالة مطابقة الكيانات

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

<!-- BEGIN GENERATED: refs US-BC02-ER-SPLIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/er-cases/{id}/actions/split` | — |
| الأمر | `CMD-ER-SPLIT` | فصل حالة مطابقة الكيانات |
| السياسة | `POL-ER-SPLIT` | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ tenant mat… |
| الحدث | `EVT-ER-SPLIT` | يصل إلى: Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster ch… |
| الكيان | `AGG-ER-CASE` | حالة مطابقة الكيانات |
| الجدول | `information.er_cases` | الجدول الرئيسي لحالة مطابقة الكيانات |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-032، REQ-INF-033، REQ-INF-034 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-104 | Split Merged Entity |
| الاختبار | TST-ER-CASE-SM، TST-SLC04-INVARIANTS | دورة حالات حالة مطابقة الكيانات، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-ER-SPLIT -->

</details>

### 5.3 US-BC02-Q-CLUSTER-GET — جلب: Cluster members, canonical URN, links, as known_at

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

<!-- BEGIN GENERATED: refs US-BC02-Q-CLUSTER-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/entities/{entity_id}/identity-cluster` | — |
| الاستعلام | `QRY-CLUSTER-GET` | Cluster members, canonical URN, links, as known_at |
| السياسة | `POL-CLUSTER-GET` | Analyst; invisible members omitted |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-033 | When entities are matched, the system shall record a same-as link with the decision, reviewer and time, keep… |
| حالة الاستخدام | UC-007 | Resolve Entity |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-CLUSTER-GET -->

</details>

### 5.4 US-UI-SCR26-CLUSTER-VIEW — عرض أعضاء الهوية الموحدة وطلب فصلها

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

<!-- BEGIN GENERATED: refs US-UI-SCR26-CLUSTER-VIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-26 | شاشة التعارض ومطابقة الكيانات |
| الشاشة | SCR-21 | شاشة الكيانات والأحداث: العرض المحلول |
| حالة الاستخدام | UC-104 | Split Merged Entity |
| المصدر | `THR-S04-04` | — |
| المتطلب | REQ-INF-034 | When a match is reversed, the system shall close the same-as link so that each original entity again resolves… |
| حالة الاستخدام | UC-104 | Split Merged Entity |
<!-- END GENERATED: refs US-UI-SCR26-CLUSTER-VIEW -->

</details>

### 5.5 US-PLT-CLUSTER-RESOLVED-READ — قراءة الكيان المدموج دون بطء ملحوظ

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

<!-- BEGIN GENERATED: refs US-PLT-CLUSTER-RESOLVED-READ -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-015 | resolved read of clustered entity → ≤ 20 % overhead vs unclustered; p95 ≤ 300 ms |
<!-- END GENERATED: refs US-PLT-CLUSTER-RESOLVED-READ -->

</details>

### 5.6 US-OPS-CLUSTER-RECONCILE — اكتشاف اختلاف جدول الهويات وإعادة بنائه

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

<!-- BEGIN GENERATED: refs US-OPS-CLUSTER-RECONCILE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `FM-S04-03` | — |
| المصدر | `observability-slc04.md` | — |
<!-- END GENERATED: refs US-OPS-CLUSTER-RECONCILE -->

</details>

### 5.7 US-OPS-ENTITY-BULK-SPLIT — فصل دفعة دمج خاطئ بقائمة حالات

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

<!-- BEGIN GENERATED: refs US-OPS-ENTITY-BULK-SPLIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `FM-S04-04` | — |
| المتطلب | REQ-INF-034 | When a match is reversed, the system shall close the same-as link so that each original entity again resolves… |
| حالة الاستخدام | UC-104 | Split Merged Entity |
<!-- END GENERATED: refs US-OPS-ENTITY-BULK-SPLIT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-032 | When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, m… | `US-BC02-ER-REQUEST-SPLIT`، `US-BC02-ER-SPLIT` | TST-ER-CASE-SM، TST-MATCH-RULESET-SM، TST-SLC04-INVARIANTS |
| REQ-INF-033 | When entities are matched, the system shall record a same-as link with the decision, reviewer and time, keep… | كل قصص الميزة المأخوذة من المواصفة (3) | TST-ER-CASE-SM، TST-SLC04-INVARIANTS |
| REQ-INF-034 | When a match is reversed, the system shall close the same-as link so that each original entity again resolves… | `US-BC02-ER-REQUEST-SPLIT`، `US-BC02-ER-SPLIT`، `US-OPS-ENTITY-BULK-SPLIT`، `US-UI-SCR26-CLUSTER-VIEW` | TST-ER-CASE-SM، TST-SLC04-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
