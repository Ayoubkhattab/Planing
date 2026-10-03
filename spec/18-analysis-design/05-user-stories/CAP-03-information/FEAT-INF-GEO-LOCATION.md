---
id: FEAT-INF-GEO-LOCATION
type: feature
title: "مواقع الكيانات وتحركاتها"
status: DRAFT
version: "0.1"
capability: CAP-03.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مواقع الكيانات وتحركاتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-GEO-LOCATION |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.03 المعلومات الجغرافية (R1) |
| الأدوار | أي مستخدم مخوَّل؛ المحلل |
| الشاشات | SCR-21 الكيانات والأحداث: العرض المحلول، SCR-11 الصورة العملياتية المشتركة (COP) |
| حالات الاستخدام | — |
| القصص | 8: 1 من المواصفة، و7 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يرى المستخدم أين كان الكيان وكيف تحرّك عبر الزمن بمواقع دقيقة وموثوقة الإحداثيات.

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
| QAS-DQ-001 | submits records with invalid geometry or missing CRS | 100 % of invalid records quarantined; 0 published |
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
| `US-BC02-Q-ENT-POSITIONS` | جلب: Position history in [from,to) as known_at | جلب | مسودة |
| `US-DOM-GEO-TRACK-SUMMARY` | تلخيص المواقع عالية التردد في ادعاء موقع | نظام | مسودة |
| `US-UI-SCR11-COORD-FORMAT` | عرض الإحداثيات بالصيغة التي يختارها المستأجر | واجهة | مسودة |
| `US-UI-SCR21-POSITION-TRACK` | عرض مسار الكيان على الخريطة عبر فترة | واجهة | مسودة |
| `US-PLT-GEO-CRS-CANONICAL` | تحويل الإحداثيات إلى النظام الموحد مع حفظ الأصل | منصة | مسودة |
| `US-PLT-GEO-GEOMETRY-VALIDATE` | رفض الأشكال الجغرافية غير الصالحة أو الناقصة | منصة | مسودة |
| `US-PLT-GEO-SPATIAL-QUALITY` | وسم جودة الموقع بالدقة وسلامة الجهاز | منصة | مسودة |
| `US-INT-GEO-OGC-FEATURES` | إتاحة مواقع الكيانات لأنظمة الخرائط الخارجية | تكامل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-Q-ENT-POSITIONS — جلب: Position history in [from,to) as known_at

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

<!-- BEGIN GENERATED: refs US-BC02-Q-ENT-POSITIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/entities/{entity_id}/positions` | — |
| الاستعلام | `QRY-ENT-POSITIONS` | Position history in [from,to) as known_at |
| السياسة | `POL-ENT-POSITIONS` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-030 | The system shall keep the position history of located entities over time. |
| حالة الاستخدام | UC-096 | Query State As-Of / As-Known-At |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-ENT-POSITIONS -->

</details>

### 5.2 US-DOM-GEO-TRACK-SUMMARY — تلخيص المواقع عالية التردد في ادعاء موقع

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

<!-- BEGIN GENERATED: refs US-DOM-GEO-TRACK-SUMMARY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `spatial-model.md §4` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-030 | The system shall keep the position history of located entities over time. |
| حالة الاستخدام | UC-096 | Query State As-Of / As-Known-At |
<!-- END GENERATED: refs US-DOM-GEO-TRACK-SUMMARY -->

</details>

### 5.3 US-UI-SCR11-COORD-FORMAT — عرض الإحداثيات بالصيغة التي يختارها المستأجر

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

<!-- BEGIN GENERATED: refs US-UI-SCR11-COORD-FORMAT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-11 | شاشة الصورة العملياتية المشتركة (COP) |
| المصدر | `21-ui-design.md §7` | — |
| القرار المعماري | ADR-P16 | Canonical CRS |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR11-COORD-FORMAT -->

</details>

### 5.4 US-UI-SCR21-POSITION-TRACK — عرض مسار الكيان على الخريطة عبر فترة

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

<!-- BEGIN GENERATED: refs US-UI-SCR21-POSITION-TRACK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-21 | شاشة الكيانات والأحداث: العرض المحلول |
| المصدر | `21-ui-design.md §7` | — |
| المتطلب | REQ-INF-030 | The system shall keep the position history of located entities over time. |
| حالة الاستخدام | UC-096 | Query State As-Of / As-Known-At |
<!-- END GENERATED: refs US-UI-SCR21-POSITION-TRACK -->

</details>

### 5.5 US-PLT-GEO-CRS-CANONICAL — تحويل الإحداثيات إلى النظام الموحد مع حفظ الأصل

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

<!-- BEGIN GENERATED: refs US-PLT-GEO-CRS-CANONICAL -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P16 | Canonical CRS |
| فحص البنية | FIT-08 | Every geometry has CRS and accuracy; canonical EPSG:4326 |
| المصدر | `spatial-model.md §2` | — |
| المتطلب | REQ-INF-029 | The system shall store each geometry in the canonical CRS WGS 84 (EPSG:4326) and shall keep the original CRS… |
<!-- END GENERATED: refs US-PLT-GEO-CRS-CANONICAL -->

</details>

### 5.6 US-PLT-GEO-GEOMETRY-VALIDATE — رفض الأشكال الجغرافية غير الصالحة أو الناقصة

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

<!-- BEGIN GENERATED: refs US-PLT-GEO-GEOMETRY-VALIDATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-DQ-001 | submits records with invalid geometry or missing CRS → 100 % of invalid records quarantined; 0 published |
| فحص البنية | FIT-08 | Every geometry has CRS and accuracy; canonical EPSG:4326 |
| المصدر | `spatial-model.md §3` | — |
| المتطلب | REQ-INF-028 | The system shall require every geometry to carry a CRS and a positional accuracy, and shall reject invalid ge… |
<!-- END GENERATED: refs US-PLT-GEO-GEOMETRY-VALIDATE -->

</details>

### 5.7 US-PLT-GEO-SPATIAL-QUALITY — وسم جودة الموقع بالدقة وسلامة الجهاز

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

<!-- BEGIN GENERATED: refs US-PLT-GEO-SPATIAL-QUALITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `spatial-model.md §7` | — |
| المتطلب | REQ-INF-028 | The system shall require every geometry to carry a CRS and a positional accuracy, and shall reject invalid ge… |
<!-- END GENERATED: refs US-PLT-GEO-SPATIAL-QUALITY -->

</details>

### 5.8 US-INT-GEO-OGC-FEATURES — إتاحة مواقع الكيانات لأنظمة الخرائط الخارجية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-GEO-OGC-FEATURES -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P12 | Map Serving & Tile Security |
| القرار التقني | TD-10 | Dynamic operational vector tiles from PostGIS (ST_AsMVT) via Martin tile server with scope-keyed cache; base… |
| المصدر | `20-integration-design.md §2` | — |
<!-- END GENERATED: refs US-INT-GEO-OGC-FEATURES -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-028 | The system shall require every geometry to carry a CRS and a positional accuracy, and shall reject invalid ge… | `US-PLT-GEO-GEOMETRY-VALIDATE`، `US-PLT-GEO-SPATIAL-QUALITY` | TST-OBSERVATION-SM، TST-SLC02-INVARIANTS |
| REQ-INF-029 | The system shall store each geometry in the canonical CRS WGS 84 (EPSG:4326) and shall keep the original CRS… | `US-PLT-GEO-CRS-CANONICAL` | TST-SLC02-INVARIANTS |
| REQ-INF-030 | The system shall keep the position history of located entities over time. | `US-BC02-Q-ENT-POSITIONS`، `US-DOM-GEO-TRACK-SUMMARY`، `US-UI-SCR21-POSITION-TRACK` | TST-SLC02-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
