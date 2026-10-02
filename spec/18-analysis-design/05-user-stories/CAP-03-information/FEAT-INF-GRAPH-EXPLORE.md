---
id: FEAT-INF-GRAPH-EXPLORE
type: feature
title: "استكشاف شبكة العلاقات"
status: DRAFT
version: "0.1"
capability: CAP-03.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# استكشاف شبكة العلاقات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-GRAPH-EXPLORE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.01 الكيانات والعلاقات (R1) |
| الأدوار | المحلل |
| الشاشات | SCR-24 الرسم البياني |
| حالات الاستخدام | — |
| القصص | 8: 2 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يستكشف المحلل محيط الكيان والمسارات التي تربط كيانين دون أن يرى ما لا يحق له.

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
| QAS-ACC-001 | uses R1 web screens | WCAG 2.2 level AA conformance (AR and EN) |
| QAS-PERF-018 | graph neighborhood depth 2 | p95 ≤ 1 s |
| QAS-SEC-011 | inference test suite on search, suggestions, facets, graph and paths | 0 disclosures of hidden objects, hidden facts, hidden nodes/edges |
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
| `US-BC07-Q-GRAPH-NEIGHBORHOOD` | جلب: Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges cut | جلب | مسودة |
| `US-BC07-Q-GRAPH-PATHS` | جلب: Paths between two entities, ≤ 4 hops, only through visible nodes and edges | جلب | مسودة |
| `US-UI-SCR24-GRAPH-EXPAND` | توسيع شبكة الكيان خطوة بخطوة | واجهة | مسودة |
| `US-UI-SCR24-GRAPH-LIST-VIEW` | بديل جدولي للرسم البياني لسهولة الوصول | واجهة | مسودة |
| `US-UI-SCR24-GRAPH-PATHS` | إيجاد المسارات بين كيانين وعرضها | واجهة | مسودة |
| `US-PLT-GRAPH-INFERENCE-SUITE` | اختبار عدم كشف العقد والحواف المخفية | منصة | مسودة |
| `US-PLT-GRAPH-NEIGHBORHOOD-PERF` | جوار الكيان بعمق اثنين خلال ثانية | منصة | مسودة |
| `US-OPS-GRAPH-LATENCY-WATCH` | مراقبة زمن استعلامات الرسم وكثافة الجوار | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-Q-GRAPH-NEIGHBORHOOD — جلب: Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges cut

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

<!-- BEGIN GENERATED: refs US-BC07-Q-GRAPH-NEIGHBORHOOD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/discovery/graph/entities/{entity_id}/neighborhood` | — |
| الاستعلام | `QRY-GRAPH-NEIGHBORHOOD` | Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges cut |
| السياسة | `POL-GRAPH-NEIGHBORHOOD` | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page |
| المتطلب | REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… |
| حالة الاستخدام | UC-003 | Manage Relationship |
<!-- END GENERATED: refs US-BC07-Q-GRAPH-NEIGHBORHOOD -->

</details>

### 5.2 US-BC07-Q-GRAPH-PATHS — جلب: Paths between two entities, ≤ 4 hops, only through visible nodes and edges

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

<!-- BEGIN GENERATED: refs US-BC07-Q-GRAPH-PATHS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/discovery/graph/paths` | — |
| الاستعلام | `QRY-GRAPH-PATHS` | Paths between two entities, ≤ 4 hops, only through visible nodes and edges |
| السياسة | `POL-GRAPH-PATHS` | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page |
| المتطلب | REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… |
| حالة الاستخدام | UC-003 | Manage Relationship |
<!-- END GENERATED: refs US-BC07-Q-GRAPH-PATHS -->

</details>

### 5.3 US-UI-SCR24-GRAPH-EXPAND — توسيع شبكة الكيان خطوة بخطوة

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

<!-- BEGIN GENERATED: refs US-UI-SCR24-GRAPH-EXPAND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-24 | شاشة الرسم البياني |
| المصدر | `discovery-architecture.md §4.4` | — |
| المصدر | `23-crosscutting.md §10` | — |
<!-- END GENERATED: refs US-UI-SCR24-GRAPH-EXPAND -->

</details>

### 5.4 US-UI-SCR24-GRAPH-LIST-VIEW — بديل جدولي للرسم البياني لسهولة الوصول

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

<!-- BEGIN GENERATED: refs US-UI-SCR24-GRAPH-LIST-VIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-24 | شاشة الرسم البياني |
| الجودة | QAS-ACC-001 | uses R1 web screens → WCAG 2.2 level AA conformance (AR and EN) |
| المصدر | `21-ui-design.md §10` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR24-GRAPH-LIST-VIEW -->

</details>

### 5.5 US-UI-SCR24-GRAPH-PATHS — إيجاد المسارات بين كيانين وعرضها

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

<!-- BEGIN GENERATED: refs US-UI-SCR24-GRAPH-PATHS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-24 | شاشة الرسم البياني |
| المصدر | `discovery-architecture.md §4.4` | — |
<!-- END GENERATED: refs US-UI-SCR24-GRAPH-PATHS -->

</details>

### 5.6 US-PLT-GRAPH-INFERENCE-SUITE — اختبار عدم كشف العقد والحواف المخفية

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

<!-- BEGIN GENERATED: refs US-PLT-GRAPH-INFERENCE-SUITE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-011 | inference test suite on search, suggestions, facets, graph and paths → 0 disclosures of hidden objects, hidde… |
| المصدر | `THR-S05-04` | — |
| المصدر | `discovery-architecture.md §4.4` | — |
<!-- END GENERATED: refs US-PLT-GRAPH-INFERENCE-SUITE -->

</details>

### 5.7 US-PLT-GRAPH-NEIGHBORHOOD-PERF — جوار الكيان بعمق اثنين خلال ثانية

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

<!-- BEGIN GENERATED: refs US-PLT-GRAPH-NEIGHBORHOOD-PERF -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-018 | graph neighborhood depth 2 → p95 ≤ 1 s |
| القرار التقني | TD-03 | No graph database in R1: relationship projection tables in PostgreSQL + bounded recursive queries (depth ≤ 3,… |
<!-- END GENERATED: refs US-PLT-GRAPH-NEIGHBORHOOD-PERF -->

</details>

### 5.8 US-OPS-GRAPH-LATENCY-WATCH — مراقبة زمن استعلامات الرسم وكثافة الجوار

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

<!-- BEGIN GENERATED: refs US-OPS-GRAPH-LATENCY-WATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc05.md` | — |
| القرار التقني | TD-03 | No graph database in R1: relationship projection tables in PostgreSQL + bounded recursive queries (depth ≤ 3,… |
<!-- END GENERATED: refs US-OPS-GRAPH-LATENCY-WATCH -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, pro… | `US-BC07-Q-GRAPH-NEIGHBORHOOD`، `US-BC07-Q-GRAPH-PATHS` | TST-RELATIONSHIP-SM، TST-SLC02-INVARIANTS، TST-SLC05-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
