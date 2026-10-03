---
id: FEAT-ANL-CORRELATION-REVIEW
type: feature
title: "مراجعة مقترحات الربط"
status: DRAFT
version: "0.1"
capability: CAP-04.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مراجعة مقترحات الربط

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ANL-CORRELATION-REVIEW |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-04 التحليل والتقييم |
| القدرة الفرعية | CAP-04.04 الدمج والربط (R2) |
| الأدوار | المحلل؛ النظام |
| الشاشات | SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-132 |
| القصص | 11: 8 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يراجع المحلل ما يقترحه النظام من ربط بين ملاحظات ومصادر مختلفة فيقبله أو يرفضه بناءً على الأدلة والدرجة.

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
| QAS-PERF-012 | batch of 1,000 observations | batch commit p95 ≤ 1 s; 0 duplicates on retry |
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
| `US-BC02-CRP-ACCEPT` | قبول مقترح الربط | أمر | مسودة |
| `US-BC02-CRP-PROPOSE` | اقتراح مقترح الربط | أمر | مسودة |
| `US-BC02-CRP-REJECT` | رفض مقترح الربط | أمر | مسودة |
| `US-BC02-CRP-START-REVIEW` | بدء مراجعة مقترح الربط | أمر | مسودة |
| `US-BC02-Q-CRP-GET` | جلب: Proposal with inputs, sources, reliabilities, score breakdown | جلب | مسودة |
| `US-BC02-Q-CRP-QUEUE` | جلب: Proposals by kind, state, area, score (inputs all visible to caller) | جلب | مسودة |
| `US-BC02-S-CORRELATION-PROPOSAL-01` | تلقائي: correlation rule score ≥ threshold (مقترح الربط) | نظام | مسودة |
| `US-BC02-S-CORRELATION-PROPOSAL-02` | تلقائي: not reviewed within 30 days (مقترح الربط) | نظام | مسودة |
| `US-UI-SCR06-CORRELATION-DETAIL` | تفصيل درجة الربط ومصادره وموثوقيتها | واجهة | مسودة |
| `US-UI-SCR06-CORRELATION-MAP` | عرض عناصر مقترح الربط على الخريطة والزمن | واجهة | مسودة |
| `US-PLT-ANL-CORRELATION-BUCKETS` | فهرسة مكانية زمنية لمرشحي الربط | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-CRP-ACCEPT — قبول مقترح الربط

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-CRP-ACCEPT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/correlation-proposals/{id}/actions/accept` | — |
| الأمر | `CMD-CRP-ACCEPT` | قبول مقترح الربط |
| السياسة | `POL-CRP-ACCEPT` | Analyst (propose, review, accept, reject)؛ tenant match; inputs visible |
| الحدث | `EVT-CRP-ACCEPTED` | يصل إلى: Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| الكيان | `AGG-CORRELATION-PROPOSAL` | مقترح الربط |
| الجدول | `information.correlation_proposals` | الجدول الرئيسي لمقترح الربط |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-FUS-001، REQ-FUS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-PROPOSAL-SM، TST-SLC15-INVARIANTS | دورة حالات مقترح الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-CRP-ACCEPT -->

</details>

### 5.2 US-BC02-CRP-PROPOSE — اقتراح مقترح الربط

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-CRP-PROPOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/correlation-proposals` | — |
| الأمر | `CMD-CRP-PROPOSE` | اقتراح مقترح الربط |
| السياسة | `POL-CRP-PROPOSE` | Analyst (propose, review, accept, reject)؛ tenant match; inputs visible |
| الحدث | `EVT-CRP-PROPOSED` | يصل إلى: Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| الكيان | `AGG-CORRELATION-PROPOSAL` | مقترح الربط |
| الجدول | `information.correlation_proposals` | الجدول الرئيسي لمقترح الربط |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-FUS-001، REQ-FUS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-PROPOSAL-SM، TST-SLC15-INVARIANTS | دورة حالات مقترح الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-CRP-PROPOSE -->

</details>

### 5.3 US-BC02-CRP-REJECT — رفض مقترح الربط

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-CRP-REJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/correlation-proposals/{id}/actions/reject` | — |
| الأمر | `CMD-CRP-REJECT` | رفض مقترح الربط |
| السياسة | `POL-CRP-REJECT` | Analyst (propose, review, accept, reject)؛ tenant match; inputs visible |
| الحدث | `EVT-CRP-REJECTED` | يصل إلى: Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| الكيان | `AGG-CORRELATION-PROPOSAL` | مقترح الربط |
| الجدول | `information.correlation_proposals` | الجدول الرئيسي لمقترح الربط |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-FUS-001، REQ-FUS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-PROPOSAL-SM، TST-SLC15-INVARIANTS | دورة حالات مقترح الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-CRP-REJECT -->

</details>

### 5.4 US-BC02-CRP-START-REVIEW — بدء مراجعة مقترح الربط

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-CRP-START-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/correlation-proposals/{id}/actions/start-review` | — |
| الأمر | `CMD-CRP-START-REVIEW` | بدء مراجعة مقترح الربط |
| السياسة | `POL-CRP-START-REVIEW` | Analyst (propose, review, accept, reject)؛ tenant match; inputs visible |
| الحدث | `EVT-CRP-REVIEW-STARTED` | يصل إلى: Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| الكيان | `AGG-CORRELATION-PROPOSAL` | مقترح الربط |
| الجدول | `information.correlation_proposals` | الجدول الرئيسي لمقترح الربط |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-FUS-001، REQ-FUS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-PROPOSAL-SM، TST-SLC15-INVARIANTS | دورة حالات مقترح الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-CRP-START-REVIEW -->

</details>

### 5.5 US-BC02-Q-CRP-GET — جلب: Proposal with inputs, sources, reliabilities, score breakdown

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-Q-CRP-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/correlation-proposals/{proposal_id}` | — |
| الاستعلام | `QRY-CRP-GET` | Proposal with inputs, sources, reliabilities, score breakdown |
| السياسة | `POL-CRP-GET` | reviewer cleared for all inputs |
| الكيان | `AGG-CORRELATION-PROPOSAL` | مقترح الربط |
| الجدول | `information.correlation_proposals` | الجدول الرئيسي لمقترح الربط |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-FUS-002 | The system shall record for each fused result the contributing sources and their reliabilities. |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-PROPOSAL-SM، TST-SLC15-INVARIANTS | دورة حالات مقترح الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-Q-CRP-GET -->

</details>

### 5.6 US-BC02-Q-CRP-QUEUE — جلب: Proposals by kind, state, area, score (inputs all visible to caller)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-Q-CRP-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/correlation-proposals` | — |
| الاستعلام | `QRY-CRP-QUEUE` | Proposals by kind, state, area, score (inputs all visible to caller) |
| السياسة | `POL-CRP-QUEUE` | Analyst |
| الكيان | `AGG-CORRELATION-PROPOSAL` | مقترح الربط |
| الجدول | `information.correlation_proposals` | الجدول الرئيسي لمقترح الربط |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-PROPOSAL-SM، TST-SLC15-INVARIANTS | دورة حالات مقترح الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-Q-CRP-QUEUE -->

</details>

### 5.7 US-BC02-S-CORRELATION-PROPOSAL-01 — تلقائي: correlation rule score ≥ threshold (مقترح الربط)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-S-CORRELATION-PROPOSAL-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:correlation rule score ≥ threshold` | inputs from ≥ 2 distinct sources; no identical non-terminal proposal; label = max(input labels) |
| الانتقال | ∅ ← PROPOSED | — |
| الحدث | `EVT-CRP-PROPOSED` | يصل إلى: Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| الكيان | `AGG-CORRELATION-PROPOSAL` | مقترح الربط |
| الجدول | `information.correlation_proposals` | الجدول الرئيسي لمقترح الربط |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-FUS-001، REQ-FUS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-PROPOSAL-SM، TST-SLC15-INVARIANTS | دورة حالات مقترح الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-S-CORRELATION-PROPOSAL-01 -->

</details>

### 5.8 US-BC02-S-CORRELATION-PROPOSAL-02 — تلقائي: not reviewed within 30 days (مقترح الربط)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-S-CORRELATION-PROPOSAL-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:not reviewed within 30 days` | scheduler |
| الانتقال | PROPOSED ← EXPIRED | — |
| الحدث | `EVT-CRP-EXPIRED` | يصل إلى: Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| الكيان | `AGG-CORRELATION-PROPOSAL` | مقترح الربط |
| الجدول | `information.correlation_proposals` | الجدول الرئيسي لمقترح الربط |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-FUS-001، REQ-FUS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-PROPOSAL-SM، TST-SLC15-INVARIANTS | دورة حالات مقترح الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-S-CORRELATION-PROPOSAL-02 -->

</details>

### 5.9 US-UI-SCR06-CORRELATION-DETAIL — تفصيل درجة الربط ومصادره وموثوقيتها

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR06-CORRELATION-DETAIL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `correlation-fusion-spec.md §2` | — |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-FUS-001، REQ-FUS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
<!-- END GENERATED: refs US-UI-SCR06-CORRELATION-DETAIL -->

</details>

### 5.10 US-UI-SCR06-CORRELATION-MAP — عرض عناصر مقترح الربط على الخريطة والزمن

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR06-CORRELATION-MAP -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `21-ui-design.md §7` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
<!-- END GENERATED: refs US-UI-SCR06-CORRELATION-MAP -->

</details>

### 5.11 US-PLT-ANL-CORRELATION-BUCKETS — فهرسة مكانية زمنية لمرشحي الربط

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-ANL-CORRELATION-BUCKETS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `correlation-fusion-spec.md §2` | — |
| الجودة | QAS-PERF-012 | batch of 1,000 observations → batch commit p95 ≤ 1 s; 0 duplicates on retry |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
<!-- END GENERATED: refs US-PLT-ANL-CORRELATION-BUCKETS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… | `US-BC02-CRP-ACCEPT`، `US-BC02-CRP-PROPOSE`، `US-BC02-CRP-REJECT`، `US-BC02-CRP-START-REVIEW`، `US-BC02-Q-CRP-QUEUE`، `US-BC02-S-CORRELATION-PROPOSAL-01`، `US-BC02-S-CORRELATION-PROPOSAL-02`، `US-PLT-ANL-CORRELATION-BUCKETS`، `US-UI-SCR06-CORRELATION-DETAIL`، `US-UI-SCR06-CORRELATION-MAP` | TST-CORRELATION-PROPOSAL-SM، TST-CORRELATION-RULE-SM، TST-SLC15-INVARIANTS |
| REQ-FUS-002 | The system shall record for each fused result the contributing sources and their reliabilities. | `US-BC02-CRP-ACCEPT`، `US-BC02-CRP-PROPOSE`، `US-BC02-CRP-REJECT`، `US-BC02-CRP-START-REVIEW`، `US-BC02-Q-CRP-GET`، `US-BC02-S-CORRELATION-PROPOSAL-01`، `US-BC02-S-CORRELATION-PROPOSAL-02`، `US-UI-SCR06-CORRELATION-DETAIL` | TST-CORRELATION-PROPOSAL-SM، TST-SLC15-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
