---
id: FEAT-INF-INDEX-REBUILD
type: feature
title: "إعادة بناء فهارس البحث"
status: DRAFT
version: "0.1"
capability: CAP-03.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إعادة بناء فهارس البحث

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-INDEX-REBUILD |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.01 الكيانات والعلاقات (R1) |
| الأدوار | مشغّل المنصة؛ النظام |
| الشاشات | SCR-71 حالة الإسقاطات (واجهة المشغل) |
| حالات الاستخدام | UC-078 |
| القصص | 16: 9 من المواصفة، و7 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعيد مشغل المنصة بناء فهارس البحث والرسم البياني من المصدر الأصلي دون فقد بيانات ويراقب تأخرها.

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
| QAS-PERF-004 | an object is created or changed | index lag p95 ≤ 30 s |
| QAS-REL-002 | search projection unavailable | critical tier unaffected; index rebuilt without data loss |
| QAS-REL-004 | full projection rebuild | ≤ 24 h to READY with no loss of query service (old version stays ACTIVE) |
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
| `US-BC07-PRJ-CANCEL-BUILD` | إلغاء بناء إصدار الإسقاط | أمر | مسودة |
| `US-BC07-PRJ-CREATE-VERSION` | إنشاء إصدار جديد من إصدار الإسقاط | أمر | مسودة |
| `US-BC07-PRJ-PROMOTE` | ترقية إصدار الإسقاط | أمر | مسودة |
| `US-BC07-PRJ-RETIRE` | إحالة إصدار الإسقاط إلى التقاعد | أمر | مسودة |
| `US-BC07-Q-PRJ-STATUS` | جلب: Projection versions, lag, state | جلب | مسودة |
| `US-BC07-S-PROJECTION-VERSION-01` | تلقائي: full rebuild reached live checkpoint (إصدار الإسقاط) | نظام | مسودة |
| `US-BC07-S-PROJECTION-VERSION-02` | تلقائي: build failed (إصدار الإسقاط) | نظام | مسودة |
| `US-BC07-S-PROJECTION-VERSION-03` | تلقائي: lag above threshold (إصدار الإسقاط) | نظام | مسودة |
| `US-BC07-S-PROJECTION-VERSION-04` | تلقائي: lag back within target (إصدار الإسقاط) | نظام | مسودة |
| `US-UI-SCR71-PROJECTION-BOARD` | متابعة إصدارات الإسقاطات وتأخرها وترقيتها | واجهة | مسودة |
| `US-PLT-INDEX-LAG` | ظهور التغييرات في البحث خلال 30 ثانية | منصة | مسودة |
| `US-PLT-INDEX-REBUILD-LIVE` | إعادة البناء الكاملة دون توقف خدمة البحث | منصة | مسودة |
| `US-PLT-INDEX-REBUILD-PARITY` | إعادة البناء تعطي نتائج مطابقة للمصدر | منصة | مسودة |
| `US-OPS-INDEX-ACCESS-ISOLATION` | حصر الوصول إلى الفهارس بخدمة البحث وحدها | تشغيل | مسودة |
| `US-OPS-INDEX-LAG-WATCH` | التنبيه عند تأخر الإسقاطات أو تدهورها | تشغيل | مسودة |
| `US-OPS-INDEX-RECONCILE` | مطابقة الفهرس مع المصدر ليلًا وإصلاح الفروق | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-PRJ-CANCEL-BUILD — إلغاء بناء إصدار الإسقاط

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

<!-- BEGIN GENERATED: refs US-BC07-PRJ-CANCEL-BUILD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/discovery/projection-versions/{id}/actions/cancel-build` | — |
| الأمر | `CMD-PRJ-CANCEL-BUILD` | إلغاء بناء إصدار الإسقاط |
| السياسة | `POL-PRJ-CANCEL-BUILD` | Platform Operator (platform tenant)؛ |
| الحدث | `EVT-PRJ-FAILED` | يصل إلى: Query router (alias switch); Operations alerting |
| الكيان | `AGG-PROJECTION-VERSION` | إصدار الإسقاط |
| وحدة النشر | DU-09 | — |
| المتطلب | REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
| الاختبار | TST-PROJECTION-VERSION-SM، TST-SLC05-INVARIANTS | دورة حالات إصدار الإسقاط، وثوابت الشريحة SLC-05 |
<!-- END GENERATED: refs US-BC07-PRJ-CANCEL-BUILD -->

</details>

### 5.2 US-BC07-PRJ-CREATE-VERSION — إنشاء إصدار جديد من إصدار الإسقاط

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

<!-- BEGIN GENERATED: refs US-BC07-PRJ-CREATE-VERSION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/discovery/projection-versions` | — |
| الأمر | `CMD-PRJ-CREATE-VERSION` | إنشاء إصدار جديد من إصدار الإسقاط |
| السياسة | `POL-PRJ-CREATE-VERSION` | Platform Operator (platform tenant)؛ |
| الحدث | `EVT-PRJ-BUILD-STARTED` | يصل إلى: Query router (alias switch); Operations alerting |
| الكيان | `AGG-PROJECTION-VERSION` | إصدار الإسقاط |
| وحدة النشر | DU-09 | — |
| المتطلب | REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
| الاختبار | TST-PROJECTION-VERSION-SM، TST-SLC05-INVARIANTS | دورة حالات إصدار الإسقاط، وثوابت الشريحة SLC-05 |
<!-- END GENERATED: refs US-BC07-PRJ-CREATE-VERSION -->

</details>

### 5.3 US-BC07-PRJ-PROMOTE — ترقية إصدار الإسقاط

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

<!-- BEGIN GENERATED: refs US-BC07-PRJ-PROMOTE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/discovery/projection-versions/{id}/actions/promote` | — |
| الأمر | `CMD-PRJ-PROMOTE` | ترقية إصدار الإسقاط |
| السياسة | `POL-PRJ-PROMOTE` | Platform Operator (platform tenant)؛ |
| الحدث | `EVT-PRJ-PROMOTED` | يصل إلى: Query router (alias switch); Operations alerting |
| الكيان | `AGG-PROJECTION-VERSION` | إصدار الإسقاط |
| وحدة النشر | DU-09 | — |
| المتطلب | REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
| الاختبار | TST-PROJECTION-VERSION-SM، TST-SLC05-INVARIANTS | دورة حالات إصدار الإسقاط، وثوابت الشريحة SLC-05 |
<!-- END GENERATED: refs US-BC07-PRJ-PROMOTE -->

</details>

### 5.4 US-BC07-PRJ-RETIRE — إحالة إصدار الإسقاط إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC07-PRJ-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/discovery/projection-versions/{id}/actions/retire` | — |
| الأمر | `CMD-PRJ-RETIRE` | إحالة إصدار الإسقاط إلى التقاعد |
| السياسة | `POL-PRJ-RETIRE` | Platform Operator (platform tenant)؛ |
| الحدث | `EVT-PRJ-RETIRED` | يصل إلى: Query router (alias switch); Operations alerting |
| الكيان | `AGG-PROJECTION-VERSION` | إصدار الإسقاط |
| وحدة النشر | DU-09 | — |
| المتطلب | REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
| الاختبار | TST-PROJECTION-VERSION-SM، TST-SLC05-INVARIANTS | دورة حالات إصدار الإسقاط، وثوابت الشريحة SLC-05 |
<!-- END GENERATED: refs US-BC07-PRJ-RETIRE -->

</details>

### 5.5 US-BC07-Q-PRJ-STATUS — جلب: Projection versions, lag, state

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

<!-- BEGIN GENERATED: refs US-BC07-Q-PRJ-STATUS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/discovery/projection-versions` | — |
| الاستعلام | `QRY-PRJ-STATUS` | Projection versions, lag, state |
| السياسة | `POL-PRJ-STATUS` | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page |
| الكيان | `AGG-PROJECTION-VERSION` | إصدار الإسقاط |
| وحدة النشر | DU-09 | — |
| المتطلب | REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
| الاختبار | TST-PROJECTION-VERSION-SM، TST-SLC05-INVARIANTS | دورة حالات إصدار الإسقاط، وثوابت الشريحة SLC-05 |
<!-- END GENERATED: refs US-BC07-Q-PRJ-STATUS -->

</details>

### 5.6 US-BC07-S-PROJECTION-VERSION-01 — تلقائي: full rebuild reached live checkpoint (إصدار الإسقاط)

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

<!-- BEGIN GENERATED: refs US-BC07-S-PROJECTION-VERSION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:full rebuild reached live checkpoint` | all source streams replayed to current checkpoint; verification sample equals source (FIT-11) |
| الانتقال | BUILDING ← READY | — |
| الحدث | `EVT-PRJ-READY` | يصل إلى: Query router (alias switch); Operations alerting |
| الكيان | `AGG-PROJECTION-VERSION` | إصدار الإسقاط |
| وحدة النشر | DU-09 | — |
| المتطلب | REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
| الاختبار | TST-PROJECTION-VERSION-SM، TST-SLC05-INVARIANTS | دورة حالات إصدار الإسقاط، وثوابت الشريحة SLC-05 |
<!-- END GENERATED: refs US-BC07-S-PROJECTION-VERSION-01 -->

</details>

### 5.7 US-BC07-S-PROJECTION-VERSION-02 — تلقائي: build failed (إصدار الإسقاط)

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

<!-- BEGIN GENERATED: refs US-BC07-S-PROJECTION-VERSION-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:build failed` | unrecoverable build error |
| الانتقال | BUILDING ← FAILED | — |
| الحدث | `EVT-PRJ-FAILED` | يصل إلى: Query router (alias switch); Operations alerting |
| الكيان | `AGG-PROJECTION-VERSION` | إصدار الإسقاط |
| وحدة النشر | DU-09 | — |
| المتطلب | REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
| الاختبار | TST-PROJECTION-VERSION-SM، TST-SLC05-INVARIANTS | دورة حالات إصدار الإسقاط، وثوابت الشريحة SLC-05 |
<!-- END GENERATED: refs US-BC07-S-PROJECTION-VERSION-02 -->

</details>

### 5.8 US-BC07-S-PROJECTION-VERSION-03 — تلقائي: lag above threshold (إصدار الإسقاط)

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

<!-- BEGIN GENERATED: refs US-BC07-S-PROJECTION-VERSION-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:lag above threshold` | lag > 5 min or error rate > 1 % for 5 min |
| الانتقال | ACTIVE ← DEGRADED | — |
| الحدث | `EVT-PRJ-DEGRADED` | يصل إلى: Query router (alias switch); Operations alerting |
| الكيان | `AGG-PROJECTION-VERSION` | إصدار الإسقاط |
| وحدة النشر | DU-09 | — |
| المتطلب | REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
| الاختبار | TST-PROJECTION-VERSION-SM، TST-SLC05-INVARIANTS | دورة حالات إصدار الإسقاط، وثوابت الشريحة SLC-05 |
<!-- END GENERATED: refs US-BC07-S-PROJECTION-VERSION-03 -->

</details>

### 5.9 US-BC07-S-PROJECTION-VERSION-04 — تلقائي: lag back within target (إصدار الإسقاط)

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

<!-- BEGIN GENERATED: refs US-BC07-S-PROJECTION-VERSION-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:lag back within target` | lag ≤ 30 s for 5 min |
| الانتقال | DEGRADED ← ACTIVE | — |
| الحدث | `EVT-PRJ-RECOVERED` | يصل إلى: Query router (alias switch); Operations alerting |
| الكيان | `AGG-PROJECTION-VERSION` | إصدار الإسقاط |
| وحدة النشر | DU-09 | — |
| المتطلب | REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
| الاختبار | TST-PROJECTION-VERSION-SM، TST-SLC05-INVARIANTS | دورة حالات إصدار الإسقاط، وثوابت الشريحة SLC-05 |
<!-- END GENERATED: refs US-BC07-S-PROJECTION-VERSION-04 -->

</details>

### 5.10 US-UI-SCR71-PROJECTION-BOARD — متابعة إصدارات الإسقاطات وتأخرها وترقيتها

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

<!-- BEGIN GENERATED: refs US-UI-SCR71-PROJECTION-BOARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-71 | شاشة حالة الإسقاطات (واجهة المشغل) |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
| المصدر | `21-ui-design.md §2` | — |
<!-- END GENERATED: refs US-UI-SCR71-PROJECTION-BOARD -->

</details>

### 5.11 US-PLT-INDEX-LAG — ظهور التغييرات في البحث خلال 30 ثانية

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

<!-- BEGIN GENERATED: refs US-PLT-INDEX-LAG -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-004 | an object is created or changed → index lag p95 ≤ 30 s |
| المصدر | `discovery-architecture.md §2` | — |
<!-- END GENERATED: refs US-PLT-INDEX-LAG -->

</details>

### 5.12 US-PLT-INDEX-REBUILD-LIVE — إعادة البناء الكاملة دون توقف خدمة البحث

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

<!-- BEGIN GENERATED: refs US-PLT-INDEX-REBUILD-LIVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-REL-004 | full projection rebuild → ≤ 24 h to READY with no loss of query service (old version stays ACTIVE) |
| الجودة | QAS-REL-002 | search projection unavailable → critical tier unaffected; index rebuilt without data loss |
| المصدر | `FM-S05-04` | — |
| المصدر | `discovery-architecture.md §2` | — |
<!-- END GENERATED: refs US-PLT-INDEX-REBUILD-LIVE -->

</details>

### 5.13 US-PLT-INDEX-REBUILD-PARITY — إعادة البناء تعطي نتائج مطابقة للمصدر

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

<!-- BEGIN GENERATED: refs US-PLT-INDEX-REBUILD-PARITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| فحص البنية | FIT-11 | Projections rebuildable: rebuild yields identical results on reference set |
| المتطلب | REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… |
| حالة الاستخدام | UC-078 | Rebuild Search & Graph Projections |
<!-- END GENERATED: refs US-PLT-INDEX-REBUILD-PARITY -->

</details>

### 5.14 US-OPS-INDEX-ACCESS-ISOLATION — حصر الوصول إلى الفهارس بخدمة البحث وحدها

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

<!-- BEGIN GENERATED: refs US-OPS-INDEX-ACCESS-ISOLATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `THR-S05-07` | — |
| المصدر | `discovery-architecture.md §1` | — |
<!-- END GENERATED: refs US-OPS-INDEX-ACCESS-ISOLATION -->

</details>

### 5.15 US-OPS-INDEX-LAG-WATCH — التنبيه عند تأخر الإسقاطات أو تدهورها

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

<!-- BEGIN GENERATED: refs US-OPS-INDEX-LAG-WATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc05.md` | — |
| المصدر | `FM-S05-01` | — |
<!-- END GENERATED: refs US-OPS-INDEX-LAG-WATCH -->

</details>

### 5.16 US-OPS-INDEX-RECONCILE — مطابقة الفهرس مع المصدر ليلًا وإصلاح الفروق

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

<!-- BEGIN GENERATED: refs US-OPS-INDEX-RECONCILE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `FM-S05-05` | — |
| المصدر | `observability-slc05.md` | — |
<!-- END GENERATED: refs US-OPS-INDEX-RECONCILE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data l… | `US-BC07-PRJ-CANCEL-BUILD`، `US-BC07-PRJ-CREATE-VERSION`، `US-BC07-PRJ-PROMOTE`، `US-BC07-PRJ-RETIRE`، `US-BC07-Q-PRJ-STATUS`، `US-BC07-S-PROJECTION-VERSION-01`، `US-BC07-S-PROJECTION-VERSION-02`، `US-BC07-S-PROJECTION-VERSION-03`، `US-BC07-S-PROJECTION-VERSION-04`، `US-PLT-INDEX-REBUILD-PARITY` | TST-PROJECTION-VERSION-SM، TST-SLC05-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
