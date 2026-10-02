---
id: FEAT-INF-ENTITY-REGISTRY
type: feature
title: "إدارة الكيانات وملفاتها"
status: DRAFT
version: "0.1"
capability: CAP-03.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة الكيانات وملفاتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-ENTITY-REGISTRY |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.01 الكيانات والعلاقات (R1) |
| الأدوار | المحلل؛ النظام؛ أي مستخدم مخوَّل |
| الشاشات | SCR-21 الكيانات والأحداث: العرض المحلول |
| حالات الاستخدام | UC-001 |
| القصص | 14: 7 من المواصفة، و7 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يسجّل المحلل الأشخاص والجهات والأماكن ويعدّلها ويطّلع على ملف كل منها بقيمه المؤكدة والمتنازع عليها.

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
| QAS-PERF-013 | resolved entity read (current) | p95 ≤ 300 ms end-to-end |
| QAS-SEC-010 | user sees an entity but not some of its claims | hidden claims affect neither status, counts, completeness nor timing (inference suite) |
| QAS-TMP-001 | asks for state as of valid time T known at record time K | 100 % agreement with temporal oracle corpus |
| QAS-USA-002 | searches a name with Arabic spelling variants or Latin transliteration | recall ≥ 95 % on the Arabic name test set |
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
| `US-BC02-ENT-CHANGE-TYPE` | تغيير نوع الكيان | أمر | مسودة |
| `US-BC02-ENT-RECLASSIFY` | إعادة تصنيف الكيان | أمر | مسودة |
| `US-BC02-ENT-REGISTER` | تسجيل الكيان | أمر | مسودة |
| `US-BC02-ENT-REINSTATE` | إعادة الكيان إلى السريان | أمر | مسودة |
| `US-BC02-ENT-RETIRE` | إحالة الكيان إلى التقاعد | أمر | مسودة |
| `US-BC02-Q-ENT-LIST` | جلب: Entities by type, bbox/polygon of current location, valid_at | جلب | مسودة |
| `US-BC02-Q-ENT-RESOLVED` | جلب: Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED candidates, confidence); resolves through the identity cluster and returns canonical_urn + requested_urn (SLC-04) | جلب | مسودة |
| `US-UI-SCR21-ENTITY-ACTIONS` | إظهار أفعال الكيان المتاحة حسب حالته | واجهة | مسودة |
| `US-UI-SCR21-ENTITY-LIST` | تصفح الكيانات وتصفيتها بالنوع والمكان والزمن | واجهة | مسودة |
| `US-UI-SCR21-RESOLVED-VIEW` | عرض ملف الكيان بقيمه المؤكدة والمتنازع عليها | واجهة | مسودة |
| `US-PLT-ENTITY-HIDDEN-CLAIMS` | ألا تكشف الادعاءات المحجوبة عبر ملف الكيان | منصة | مسودة |
| `US-PLT-ENTITY-RESOLVED-READ` | فتح ملف الكيان خلال 300 ميلي ثانية | منصة | مسودة |
| `US-PLT-NAMES-NORMALIZE` | حفظ الأسماء بصيغها الأصلية والموحدة والمنقولة | منصة | مسودة |
| `US-OPS-NAMES-NORM-UPGRADE` | ترقية قواعد توحيد الأسماء وإعادة الفهرسة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-ENT-CHANGE-TYPE — تغيير نوع الكيان

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

<!-- BEGIN GENERATED: refs US-BC02-ENT-CHANGE-TYPE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/entities/{id}/actions/change-type` | — |
| الأمر | `CMD-ENT-CHANGE-TYPE` | تغيير نوع الكيان |
| السياسة | `POL-ENT-CHANGE-TYPE` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-ENT-TYPE-CHANGED` | يصل إلى: ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-020، REQ-INF-036 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-001 | Manage Entity |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-ENT-CHANGE-TYPE -->

</details>

### 5.2 US-BC02-ENT-RECLASSIFY — إعادة تصنيف الكيان

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

<!-- BEGIN GENERATED: refs US-BC02-ENT-RECLASSIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/entities/{id}/actions/reclassify` | — |
| الأمر | `CMD-ENT-RECLASSIFY` | إعادة تصنيف الكيان |
| السياسة | `POL-ENT-RECLASSIFY` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-ENT-RECLASSIFIED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-020، REQ-INF-036 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-001 | Manage Entity |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-ENT-RECLASSIFY -->

</details>

### 5.3 US-BC02-ENT-REGISTER — تسجيل الكيان

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

<!-- BEGIN GENERATED: refs US-BC02-ENT-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/entities` | — |
| الأمر | `CMD-ENT-REGISTER` | تسجيل الكيان |
| السياسة | `POL-ENT-REGISTER` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-ENT-REGISTERED` | يصل إلى: ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-020، REQ-INF-036 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-001 | Manage Entity |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-ENT-REGISTER -->

</details>

### 5.4 US-BC02-ENT-REINSTATE — إعادة الكيان إلى السريان

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

<!-- BEGIN GENERATED: refs US-BC02-ENT-REINSTATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/entities/{id}/actions/reinstate` | — |
| الأمر | `CMD-ENT-REINSTATE` | إعادة الكيان إلى السريان |
| السياسة | `POL-ENT-REINSTATE` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-ENT-REINSTATED` | يصل إلى: ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-020، REQ-INF-036 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-001 | Manage Entity |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-ENT-REINSTATE -->

</details>

### 5.5 US-BC02-ENT-RETIRE — إحالة الكيان إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC02-ENT-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/entities/{id}/actions/retire` | — |
| الأمر | `CMD-ENT-RETIRE` | إحالة الكيان إلى التقاعد |
| السياسة | `POL-ENT-RETIRE` | Analyst · adapter service account؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-ENT-RETIRED` | يصل إلى: ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-INF-020، REQ-INF-036 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-001 | Manage Entity |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-ENT-RETIRE -->

</details>

### 5.6 US-BC02-Q-ENT-LIST — جلب: Entities by type, bbox/polygon of current location, valid_at

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

<!-- BEGIN GENERATED: refs US-BC02-Q-ENT-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/entities` | — |
| الاستعلام | `QRY-ENT-LIST` | Entities by type, bbox/polygon of current location, valid_at |
| السياسة | `POL-ENT-LIST` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… |
| حالة الاستخدام | UC-001 | Manage Entity |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-ENT-LIST -->

</details>

### 5.7 US-BC02-Q-ENT-RESOLVED — جلب: Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED candidates, confidence); resolves through the identity cluster and returns canonical_urn + requested_urn (SLC-04)

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

<!-- BEGIN GENERATED: refs US-BC02-Q-ENT-RESOLVED -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/entities/{entity_id}` | — |
| الاستعلام | `QRY-ENT-RESOLVED` | Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED candidates, confidence); resol… |
| السياسة | `POL-ENT-RESOLVED` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-ENTITY` | الكيان |
| الجدول | `information.entities` | الجدول الرئيسي للكيان |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-023 | When a query specifies a valid time T, a record time K, or both, the system shall return the state valid at T… |
| حالة الاستخدام | UC-096 | Query State As-Of / As-Known-At |
| الاختبار | TST-ENTITY-SM، TST-SLC02-INVARIANTS | دورة حالات الكيان، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-ENT-RESOLVED -->

</details>

### 5.8 US-UI-SCR21-ENTITY-ACTIONS — إظهار أفعال الكيان المتاحة حسب حالته

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

<!-- BEGIN GENERATED: refs US-UI-SCR21-ENTITY-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-21 | شاشة الكيانات والأحداث: العرض المحلول |
| المصدر | `21-ui-design.md §6.3` | — |
<!-- END GENERATED: refs US-UI-SCR21-ENTITY-ACTIONS -->

</details>

### 5.9 US-UI-SCR21-ENTITY-LIST — تصفح الكيانات وتصفيتها بالنوع والمكان والزمن

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

<!-- BEGIN GENERATED: refs US-UI-SCR21-ENTITY-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-21 | شاشة الكيانات والأحداث: العرض المحلول |
| المصدر | `21-ui-design.md §6.1` | — |
| المتطلب | REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… |
| حالة الاستخدام | UC-001 | Manage Entity |
<!-- END GENERATED: refs US-UI-SCR21-ENTITY-LIST -->

</details>

### 5.10 US-UI-SCR21-RESOLVED-VIEW — عرض ملف الكيان بقيمه المؤكدة والمتنازع عليها

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

<!-- BEGIN GENERATED: refs US-UI-SCR21-RESOLVED-VIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-21 | شاشة الكيانات والأحداث: العرض المحلول |
| المصدر | `21-ui-design.md §1` | — |
| المصدر | `21-ui-design.md §11` | — |
| المتطلبات | REQ-INF-021، REQ-INF-033 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-006، UC-007 | Manage Evidence؛ Resolve Entity |
<!-- END GENERATED: refs US-UI-SCR21-RESOLVED-VIEW -->

</details>

### 5.11 US-PLT-ENTITY-HIDDEN-CLAIMS — ألا تكشف الادعاءات المحجوبة عبر ملف الكيان

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

<!-- BEGIN GENERATED: refs US-PLT-ENTITY-HIDDEN-CLAIMS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-010 | user sees an entity but not some of its claims → hidden claims affect neither status, counts, completeness no… |
| المصدر | `THR-S02-03` | — |
<!-- END GENERATED: refs US-PLT-ENTITY-HIDDEN-CLAIMS -->

</details>

### 5.12 US-PLT-ENTITY-RESOLVED-READ — فتح ملف الكيان خلال 300 ميلي ثانية

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

<!-- BEGIN GENERATED: refs US-PLT-ENTITY-RESOLVED-READ -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-013 | resolved entity read (current) → p95 ≤ 300 ms end-to-end |
| المصدر | `temporal-model.md §9` | — |
<!-- END GENERATED: refs US-PLT-ENTITY-RESOLVED-READ -->

</details>

### 5.13 US-PLT-NAMES-NORMALIZE — حفظ الأسماء بصيغها الأصلية والموحدة والمنقولة

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

<!-- BEGIN GENERATED: refs US-PLT-NAMES-NORMALIZE -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P15 | Language & Entity Matching |
| المصدر | `language-model.md §1` | — |
| المصدر | `language-model.md §2` | — |
| المصدر | `language-model.md §3` | — |
| الجودة | QAS-USA-002 | searches a name with Arabic spelling variants or Latin transliteration → recall ≥ 95 % on the Arabic name tes… |
| المتطلبات | REQ-INF-031، REQ-SRC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-097 | Search Authorized Information |
<!-- END GENERATED: refs US-PLT-NAMES-NORMALIZE -->

</details>

### 5.14 US-OPS-NAMES-NORM-UPGRADE — ترقية قواعد توحيد الأسماء وإعادة الفهرسة

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

<!-- BEGIN GENERATED: refs US-OPS-NAMES-NORM-UPGRADE -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P15 | Language & Entity Matching |
| المصدر | `language-model.md §1` | — |
| المصدر | `discovery-architecture.md §5` | — |
| المصدر | `23-crosscutting.md §5` | — |
<!-- END GENERATED: refs US-OPS-NAMES-NORM-UPGRADE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct o… | `US-BC02-ENT-CHANGE-TYPE`، `US-BC02-ENT-RECLASSIFY`، `US-BC02-ENT-REGISTER`، `US-BC02-ENT-REINSTATE`، `US-BC02-ENT-RETIRE`، `US-BC02-Q-ENT-LIST`، `US-UI-SCR21-ENTITY-LIST` | TST-ENTITY-SM، TST-REALWORLD-EVENT-SM، TST-SLC02-INVARIANTS |
| REQ-INF-021 | The system shall represent each attribute value of an importance-tier T1 object as a claim linked to its sour… | `US-UI-SCR21-RESOLVED-VIEW` | TST-CLAIM-SM، TST-ENTITY-SM، TST-EVIDENCE-LINK-SM، TST-SLC02-INVARIANTS |
| REQ-INF-023 | When a query specifies a valid time T, a record time K, or both, the system shall return the state valid at T… | `US-BC02-Q-ENT-RESOLVED` | TST-SLC02-INVARIANTS |
| REQ-INF-031 | The system shall store names in their original form and in normalized and transliterated forms for Arabic and… | `US-PLT-NAMES-NORMALIZE` | TST-SLC02-INVARIANTS |
| REQ-INF-033 | When entities are matched, the system shall record a same-as link with the decision, reviewer and time, keep… | `US-UI-SCR21-RESOLVED-VIEW` | TST-ER-CASE-SM، TST-SLC04-INVARIANTS |
| REQ-INF-036 | The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type… | كل قصص الأوامر والنظام في الميزة (5) | TST-ENTITY-SM، TST-EXTERNAL-ID-SM، TST-SLC02-INVARIANTS |
| REQ-SRC-003 | The system shall match Arabic text regardless of hamza forms, alef maqsura, taa marbuta, diacritics and tatwe… | `US-PLT-NAMES-NORMALIZE` | TST-MATCH-RULESET-SM، TST-SLC04-INVARIANTS، TST-SLC05-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
