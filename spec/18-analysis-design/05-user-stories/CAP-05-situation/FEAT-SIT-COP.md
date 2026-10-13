---
id: FEAT-SIT-COP
type: feature
title: "الصورة العملياتية المشتركة"
status: DRAFT
version: "0.1"
capability: CAP-05.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# الصورة العملياتية المشتركة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-SIT-COP |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-05 الوعي بالموقف |
| القدرة الفرعية | CAP-05.03 صورة العمليات المشتركة (الخرائط) (R1) |
| الأدوار | أي مستخدم مخوَّل؛ المستخدم الميداني |
| الشاشات | SCR-11 الصورة العملياتية المشتركة (COP) |
| حالات الاستخدام | UC-024، UC-098 |
| القصص | 13: 3 من المواصفة، و10 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يرى كل مخوَّل الموقف على خريطة واحدة تجمع الكيانات والأحداث والمهام والتنبيهات بحسب صلاحيته.

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
| QAS-PERF-006 | a situation member changes | p95 ≤ 10 s |
| QAS-PERF-007 | pans or zooms the operational map | tile p95 ≤ 500 ms |
| QAS-PERF-019 | situation picture read (≤ 2,000 visible members) | p95 ≤ 1 s |
| QAS-SEC-003 | removes a user's compartment | effective on next request in every path, independent of index lag |
| QAS-SEC-004 | request the same map tile | 0 cross-scope cache hits |
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
| `US-BC03-Q-BASE-TILE` | جلب: Base-map tile (layers marked unclassified only; shared cache) | جلب | مسودة |
| `US-BC03-Q-SIT-COP` | جلب: Common operational picture: visible members (entities, events, observations, tasks, assessments, alerts) with resolved, possibly generalized geometry | جلب | مسودة |
| `US-BC03-Q-SIT-TILE` | جلب: Vector tile of operational layer for the caller's security scope | جلب | مسودة |
| `US-UI-SCR11-FEATURE-CARD` | بطاقة العنصر بدقته وجودته وحالة تعميمه | واجهة | مسودة |
| `US-UI-SCR11-LAYERS` | تشغيل طبقات الخريطة وتجميع العناصر عند التصغير | واجهة | مسودة |
| `US-UI-SCR11-TABLE-VIEW` | بديل جدولي للخريطة لسهولة الوصول | واجهة | مسودة |
| `US-UI-SCR11-TIME-SLIDER` | منزلق زمني لعرض الصورة في وقت سابق | واجهة | مسودة |
| `US-PLT-COP-PICTURE-READ` | فتح صورة الموقف خلال ثانية | منصة | مسودة |
| `US-PLT-COP-TILE-INVALIDATE` | تحديث البلاطات فور تغير العضوية أو الموقع | منصة | مسودة |
| `US-PLT-COP-TILE-PERF` | بلاطات الخريطة خلال نصف ثانية عند التحريك | منصة | مسودة |
| `US-PLT-COP-TILE-SCOPE-CACHE` | عدم مشاركة البلاطات بين نطاقات صلاحية مختلفة | منصة | مسودة |
| `US-INT-COP-OGC-TILES` | إتاحة طبقات الموقف لأنظمة الخرائط الخارجية | تكامل | مسودة |
| `US-OPS-COP-TILE-WATCH` | مراقبة زمن البلاطات ونسبة إصابة الذاكرة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-Q-BASE-TILE — جلب: Base-map tile (layers marked unclassified only; shared cache)

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

<!-- BEGIN GENERATED: refs US-BC03-Q-BASE-TILE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/base-maps/{layer}/{z}/{x}/{y}` | — |
| الاستعلام | `QRY-BASE-TILE` | Base-map tile (layers marked unclassified only; shared cache) |
| السياسة | `POL-BASE-TILE` | any user of tenant |
| المتطلب | REQ-SIT-007 | The system shall serve map layers filtered by the requesting user's authorization and shall not share cached… |
| حالة الاستخدام | UC-098 | View Common Operational Picture |
<!-- END GENERATED: refs US-BC03-Q-BASE-TILE -->

</details>

### 5.2 US-BC03-Q-SIT-COP — جلب: Common operational picture: visible members (entities, events, observations, tasks, assessments, alerts) with resolved, possibly generalized geometry

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

<!-- BEGIN GENERATED: refs US-BC03-Q-SIT-COP -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/situations/{situation_id}/picture` | — |
| الاستعلام | `QRY-SIT-COP` | Common operational picture: visible members (entities, events, observations, tasks, assessments, alerts) with… |
| السياسة | `POL-SIT-COP` | cleared for situation; per-member filtering |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-003 | The system shall present each situation as a map-based common operational picture of its entities, events, ri… |
| حالات الاستخدام | UC-024، UC-098 | Produce Situation View؛ View Common Operational Picture |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-Q-SIT-COP -->

</details>

### 5.3 US-BC03-Q-SIT-TILE — جلب: Vector tile of operational layer for the caller's security scope

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

<!-- BEGIN GENERATED: refs US-BC03-Q-SIT-TILE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/situations/{situation_id}/tiles/{layer}/{z}/{x}/{y}` | — |
| الاستعلام | `QRY-SIT-TILE` | Vector tile of operational layer for the caller's security scope |
| السياسة | `POL-SIT-TILE` | cleared for situation; scope-keyed cache (ADR-P06 §6) |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-007 | The system shall serve map layers filtered by the requesting user's authorization and shall not share cached… |
| حالة الاستخدام | UC-098 | View Common Operational Picture |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-Q-SIT-TILE -->

</details>

### 5.4 US-UI-SCR11-FEATURE-CARD — بطاقة العنصر بدقته وجودته وحالة تعميمه

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

<!-- BEGIN GENERATED: refs US-UI-SCR11-FEATURE-CARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-11 | شاشة الصورة العملياتية المشتركة (COP) |
| المصدر | `21-ui-design.md §7` | — |
| المصدر | `spatial-model.md §7` | — |
<!-- END GENERATED: refs US-UI-SCR11-FEATURE-CARD -->

</details>

### 5.5 US-UI-SCR11-LAYERS — تشغيل طبقات الخريطة وتجميع العناصر عند التصغير

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

<!-- BEGIN GENERATED: refs US-UI-SCR11-LAYERS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-11 | شاشة الصورة العملياتية المشتركة (COP) |
| المصدر | `21-ui-design.md §7` | — |
| المتطلب | REQ-SIT-003 | The system shall present each situation as a map-based common operational picture of its entities, events, ri… |
| حالات الاستخدام | UC-024، UC-098 | Produce Situation View؛ View Common Operational Picture |
<!-- END GENERATED: refs US-UI-SCR11-LAYERS -->

</details>

### 5.6 US-UI-SCR11-TABLE-VIEW — بديل جدولي للخريطة لسهولة الوصول

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

<!-- BEGIN GENERATED: refs US-UI-SCR11-TABLE-VIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-11 | شاشة الصورة العملياتية المشتركة (COP) |
| الجودة | QAS-ACC-001 | uses R1 web screens → WCAG 2.2 level AA conformance (AR and EN) |
| المصدر | `21-ui-design.md §10` | — |
<!-- END GENERATED: refs US-UI-SCR11-TABLE-VIEW -->

</details>

### 5.7 US-UI-SCR11-TIME-SLIDER — منزلق زمني لعرض الصورة في وقت سابق

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

<!-- BEGIN GENERATED: refs US-UI-SCR11-TIME-SLIDER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-11 | شاشة الصورة العملياتية المشتركة (COP) |
| القرار المعماري | ADR-P01 | Temporal Model |
| المصدر | `21-ui-design.md §3` | — |
| المصدر | `21-ui-design.md §7` | — |
<!-- END GENERATED: refs US-UI-SCR11-TIME-SLIDER -->

</details>

### 5.8 US-PLT-COP-PICTURE-READ — فتح صورة الموقف خلال ثانية

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

<!-- BEGIN GENERATED: refs US-PLT-COP-PICTURE-READ -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-019 | situation picture read (≤ 2,000 visible members) → p95 ≤ 1 s |
<!-- END GENERATED: refs US-PLT-COP-PICTURE-READ -->

</details>

### 5.9 US-PLT-COP-TILE-INVALIDATE — تحديث البلاطات فور تغير العضوية أو الموقع

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

<!-- BEGIN GENERATED: refs US-PLT-COP-TILE-INVALIDATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `situation-alerting-spec.md §5` | — |
| الجودة | QAS-PERF-006 | a situation member changes → p95 ≤ 10 s |
<!-- END GENERATED: refs US-PLT-COP-TILE-INVALIDATE -->

</details>

### 5.10 US-PLT-COP-TILE-PERF — بلاطات الخريطة خلال نصف ثانية عند التحريك

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

<!-- BEGIN GENERATED: refs US-PLT-COP-TILE-PERF -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-007 | pans or zooms the operational map → tile p95 ≤ 500 ms |
| المصدر | `FM-S06-04` | — |
| المصدر | `situation-alerting-spec.md §5` | — |
<!-- END GENERATED: refs US-PLT-COP-TILE-PERF -->

</details>

### 5.11 US-PLT-COP-TILE-SCOPE-CACHE — عدم مشاركة البلاطات بين نطاقات صلاحية مختلفة

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

<!-- BEGIN GENERATED: refs US-PLT-COP-TILE-SCOPE-CACHE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-004 | request the same map tile → 0 cross-scope cache hits |
| الجودة | QAS-SEC-003 | removes a user's compartment → effective on next request in every path, independent of index lag |
| القرار المعماري | ADR-P12 | Map Serving & Tile Security |
| المصدر | `THR-S06-03` | — |
| المتطلب | REQ-SIT-007 | The system shall serve map layers filtered by the requesting user's authorization and shall not share cached… |
| حالة الاستخدام | UC-098 | View Common Operational Picture |
<!-- END GENERATED: refs US-PLT-COP-TILE-SCOPE-CACHE -->

</details>

### 5.12 US-INT-COP-OGC-TILES — إتاحة طبقات الموقف لأنظمة الخرائط الخارجية

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

<!-- BEGIN GENERATED: refs US-INT-COP-OGC-TILES -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P12 | Map Serving & Tile Security |
| القرار التقني | TD-10 | Dynamic operational vector tiles from PostGIS (ST_AsMVT) via Martin tile server with scope-keyed cache; base… |
| المتطلب | REQ-SIT-007 | The system shall serve map layers filtered by the requesting user's authorization and shall not share cached… |
| حالة الاستخدام | UC-098 | View Common Operational Picture |
<!-- END GENERATED: refs US-INT-COP-OGC-TILES -->

</details>

### 5.13 US-OPS-COP-TILE-WATCH — مراقبة زمن البلاطات ونسبة إصابة الذاكرة

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

<!-- BEGIN GENERATED: refs US-OPS-COP-TILE-WATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc06.md` | — |
| المصدر | `FM-S06-04` | — |
<!-- END GENERATED: refs US-OPS-COP-TILE-WATCH -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-SIT-003 | The system shall present each situation as a map-based common operational picture of its entities, events, ri… | `US-BC03-Q-SIT-COP`، `US-UI-SCR11-LAYERS` | TST-SITUATION-SM، TST-SLC06-INVARIANTS |
| REQ-SIT-007 | The system shall serve map layers filtered by the requesting user's authorization and shall not share cached… | `US-BC03-Q-BASE-TILE`، `US-BC03-Q-SIT-TILE`، `US-INT-COP-OGC-TILES`، `US-PLT-COP-TILE-SCOPE-CACHE` | TST-SLC06-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
