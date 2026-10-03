---
id: FEAT-ANL-CASE-SETUP
type: feature
title: "فتح حالة تحليل وإدارتها"
status: DRAFT
version: "0.1"
capability: CAP-04.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# فتح حالة تحليل وإدارتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ANL-CASE-SETUP |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-04 التحليل والتقييم |
| القدرة الفرعية | CAP-04.01 حالات التحليل (R1) |
| الأدوار | المحلل؛ مسؤول الأمن؛ أي مستخدم مخوَّل |
| الشاشات | SCR-30 الحالة التحليلية والتشغيلات |
| حالات الاستخدام | UC-010، UC-011 |
| القصص | 12: 9 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يبدأ المحلل عمله التحليلي من حالة واحدة تحدد السؤال والنطاق، ويتابعها حتى الإغلاق أو إعادة الفتح.

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
| `US-BC03-ACS-CANCEL` | إلغاء حالة التحليل | أمر | مسودة |
| `US-BC03-ACS-CLOSE` | إغلاق حالة التحليل | أمر | مسودة |
| `US-BC03-ACS-CREATE` | إنشاء حالة التحليل | أمر | مسودة |
| `US-BC03-ACS-DEFINE` | تعريف حالة التحليل | أمر | مسودة |
| `US-BC03-ACS-OPEN` | فتح حالة التحليل | أمر | مسودة |
| `US-BC03-ACS-RECLASSIFY` | إعادة تصنيف حالة التحليل | أمر | مسودة |
| `US-BC03-ACS-REOPEN` | إعادة فتح حالة التحليل | أمر | مسودة |
| `US-BC03-Q-ACS-GET` | جلب: Case with question, scope, hypotheses, assumptions, visible selections, scenarios | جلب | مسودة |
| `US-BC03-Q-ACS-LIST` | جلب: Cases by owner, state, extent | جلب | مسودة |
| `US-UI-SCR30-CASE-ACTIONS` | أفعال الحالة المتاحة حسب وضعها | واجهة | مسودة |
| `US-UI-SCR30-CASE-LIST` | قائمة حالات التحليل حسب الحالة والنطاق | واجهة | مسودة |
| `US-UI-SCR30-SCOPE-MAP` | رسم النطاق المكاني والزمني للحالة على الخريطة | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-ACS-CANCEL — إلغاء حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/cancel` | — |
| الأمر | `CMD-ACS-CANCEL` | إلغاء حالة التحليل |
| السياسة | `POL-ACS-CANCEL` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-CANCELLED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-CANCEL -->

</details>

### 5.2 US-BC03-ACS-CLOSE — إغلاق حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-CLOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/close` | — |
| الأمر | `CMD-ACS-CLOSE` | إغلاق حالة التحليل |
| السياسة | `POL-ACS-CLOSE` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-CLOSED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-CLOSE -->

</details>

### 5.3 US-BC03-ACS-CREATE — إنشاء حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-CREATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases` | — |
| الأمر | `CMD-ACS-CREATE` | إنشاء حالة التحليل |
| السياسة | `POL-ACS-CREATE` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-CREATED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-CREATE -->

</details>

### 5.4 US-BC03-ACS-DEFINE — تعريف حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-DEFINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/define` | — |
| الأمر | `CMD-ACS-DEFINE` | تعريف حالة التحليل |
| السياسة | `POL-ACS-DEFINE` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-DEFINED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-DEFINE -->

</details>

### 5.5 US-BC03-ACS-OPEN — فتح حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-OPEN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/open` | — |
| الأمر | `CMD-ACS-OPEN` | فتح حالة التحليل |
| السياسة | `POL-ACS-OPEN` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-OPENED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-OPEN -->

</details>

### 5.6 US-BC03-ACS-RECLASSIFY — إعادة تصنيف حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-RECLASSIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/reclassify` | — |
| الأمر | `CMD-ACS-RECLASSIFY` | إعادة تصنيف حالة التحليل |
| السياسة | `POL-ACS-RECLASSIFY` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-RECLASSIFIED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-RECLASSIFY -->

</details>

### 5.7 US-BC03-ACS-REOPEN — إعادة فتح حالة التحليل

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

<!-- BEGIN GENERATED: refs US-BC03-ACS-REOPEN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/analysis-cases/{id}/actions/reopen` | — |
| الأمر | `CMD-ACS-REOPEN` | إعادة فتح حالة التحليل |
| السياسة | `POL-ACS-REOPEN` | Analyst (owner) · Security Officer (reclassify)؛ tenant match; case visible; label rules |
| الحدث | `EVT-ACS-REOPENED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-ANL-001، REQ-ANL-007 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-ACS-REOPEN -->

</details>

### 5.8 US-BC03-Q-ACS-GET — جلب: Case with question, scope, hypotheses, assumptions, visible selections, scenarios

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

<!-- BEGIN GENERATED: refs US-BC03-Q-ACS-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/analysis-cases/{case_id}` | — |
| الاستعلام | `QRY-ACS-GET` | Case with question, scope, hypotheses, assumptions, visible selections, scenarios |
| السياسة | `POL-ACS-GET` | case label rule; selections filtered |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-ANL-001 | The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumpti… |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-Q-ACS-GET -->

</details>

### 5.9 US-BC03-Q-ACS-LIST — جلب: Cases by owner, state, extent

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

<!-- BEGIN GENERATED: refs US-BC03-Q-ACS-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/analysis-cases` | — |
| الاستعلام | `QRY-ACS-LIST` | Cases by owner, state, extent |
| السياسة | `POL-ACS-LIST` | allowed_scope |
| الكيان | `AGG-ANALYSIS-CASE` | حالة التحليل |
| الجدول | `intelligence.analysis_cases` | الجدول الرئيسي لحالة التحليل |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-ANL-001 | The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumpti… |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
| الاختبار | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS | دورة حالات حالة التحليل، وثوابت الشريحة SLC-07 |
<!-- END GENERATED: refs US-BC03-Q-ACS-LIST -->

</details>

### 5.10 US-UI-SCR30-CASE-ACTIONS — أفعال الحالة المتاحة حسب وضعها

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

<!-- BEGIN GENERATED: refs US-UI-SCR30-CASE-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-30 | شاشة الحالة التحليلية والتشغيلات |
| المصدر | `21-ui-design.md §6.3` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-001 | The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumpti… |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
<!-- END GENERATED: refs US-UI-SCR30-CASE-ACTIONS -->

</details>

### 5.11 US-UI-SCR30-CASE-LIST — قائمة حالات التحليل حسب الحالة والنطاق

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

<!-- BEGIN GENERATED: refs US-UI-SCR30-CASE-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-30 | شاشة الحالة التحليلية والتشغيلات |
| المصدر | `21-ui-design.md §6.1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-001 | The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumpti… |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
<!-- END GENERATED: refs US-UI-SCR30-CASE-LIST -->

</details>

### 5.12 US-UI-SCR30-SCOPE-MAP — رسم النطاق المكاني والزمني للحالة على الخريطة

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

<!-- BEGIN GENERATED: refs US-UI-SCR30-SCOPE-MAP -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-30 | شاشة الحالة التحليلية والتشغيلات |
| المصدر | `21-ui-design.md §7` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ANL-001 | The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumpti… |
| حالات الاستخدام | UC-010، UC-011 | Create Analysis Case؛ Define Analytical Question |
<!-- END GENERATED: refs US-UI-SCR30-SCOPE-MAP -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-ANL-001 | The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumpti… | `US-BC03-ACS-CANCEL`، `US-BC03-ACS-CLOSE`، `US-BC03-ACS-CREATE`، `US-BC03-ACS-DEFINE`، `US-BC03-ACS-OPEN`، `US-BC03-ACS-RECLASSIFY`، `US-BC03-ACS-REOPEN`، `US-BC03-Q-ACS-GET`، `US-BC03-Q-ACS-LIST`، `US-UI-SCR30-CASE-ACTIONS`، `US-UI-SCR30-CASE-LIST`، `US-UI-SCR30-SCOPE-MAP` | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS |
| REQ-ANL-007 | The system shall allow comparison of alternative scenarios within an analysis case. | كل قصص الأوامر والنظام في الميزة (7) | TST-ANALYSIS-CASE-SM، TST-SLC07-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
