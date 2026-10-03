---
id: FEAT-ANL-CORRELATION-RULES
type: feature
title: "قواعد الربط الآلي"
status: DRAFT
version: "0.1"
capability: CAP-04.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# قواعد الربط الآلي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ANL-CORRELATION-RULES |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-04 التحليل والتقييم |
| القدرة الفرعية | CAP-04.04 الدمج والربط (R2) |
| الأدوار | قائد المحللين؛ صاحب السلطة أو المعتمِد الثاني |
| الشاشات | — |
| حالات الاستخدام | UC-132 |
| القصص | 8: 4 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضبط قائد التحليل قواعد الربط الآلي ويعتمدها بموافقة ثانية، فلا تُولَّد مقترحات من قواعد غير معتمدة.

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
| `US-BC02-CRR-ACTIVATE` | تفعيل قاعدة الربط | أمر | مسودة |
| `US-BC02-CRR-DEFINE` | تعريف قاعدة الربط | أمر | مسودة |
| `US-BC02-CRR-EDIT` | تعديل قاعدة الربط | أمر | مسودة |
| `US-BC02-CRR-RETIRE` | إحالة قاعدة الربط إلى التقاعد | أمر | مسودة |
| `US-DOM-ANL-CRR-LIST` | عرض قواعد الربط وإصداراتها | جلب | مسودة |
| `US-UI-SCR26-CORRELATION-RULES` | إدارة قواعد الربط بجوار قواعد المطابقة | واجهة | مسودة |
| `US-UI-SCR26-CRR-APPROVAL` | مراجعة القاعدة واعتمادها من شخص ثانٍ | واجهة | مسودة |
| `US-OPS-ANL-CORRELATION-CALIBRATE` | إعادة معايرة عتبات الربط بعد التجربة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-CRR-ACTIVATE — تفعيل قاعدة الربط

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

<!-- BEGIN GENERATED: refs US-BC02-CRR-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/correlation-rules/{id}/actions/activate` | — |
| الأمر | `CMD-CRR-ACTIVATE` | تفعيل قاعدة الربط |
| السياسة | `POL-CRR-ACTIVATE` | Analyst lead (define, edit) · second approver (activate)؛ tenant match; inputs visible |
| الحدث | `EVT-CRR-ACTIVATED` | يصل إلى: Correlation engine |
| الكيان | `AGG-CORRELATION-RULE` | قاعدة الربط |
| الجدول | `information.correlation_rules` | الجدول الرئيسي لقاعدة الربط |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-RULE-SM، TST-SLC15-INVARIANTS | دورة حالات قاعدة الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-CRR-ACTIVATE -->

</details>

### 5.2 US-BC02-CRR-DEFINE — تعريف قاعدة الربط

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

<!-- BEGIN GENERATED: refs US-BC02-CRR-DEFINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/correlation-rules` | — |
| الأمر | `CMD-CRR-DEFINE` | تعريف قاعدة الربط |
| السياسة | `POL-CRR-DEFINE` | Analyst lead (define, edit) · second approver (activate)؛ tenant match; inputs visible |
| الحدث | `EVT-CRR-DEFINED` | يصل إلى: Correlation engine |
| الكيان | `AGG-CORRELATION-RULE` | قاعدة الربط |
| الجدول | `information.correlation_rules` | الجدول الرئيسي لقاعدة الربط |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-RULE-SM، TST-SLC15-INVARIANTS | دورة حالات قاعدة الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-CRR-DEFINE -->

</details>

### 5.3 US-BC02-CRR-EDIT — تعديل قاعدة الربط

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

<!-- BEGIN GENERATED: refs US-BC02-CRR-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/correlation-rules/{id}/actions/edit` | — |
| الأمر | `CMD-CRR-EDIT` | تعديل قاعدة الربط |
| السياسة | `POL-CRR-EDIT` | Analyst lead (define, edit) · second approver (activate)؛ tenant match; inputs visible |
| الحدث | `EVT-CRR-EDITED` | يصل إلى: Correlation engine |
| الكيان | `AGG-CORRELATION-RULE` | قاعدة الربط |
| الجدول | `information.correlation_rules` | الجدول الرئيسي لقاعدة الربط |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-RULE-SM، TST-SLC15-INVARIANTS | دورة حالات قاعدة الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-CRR-EDIT -->

</details>

### 5.4 US-BC02-CRR-RETIRE — إحالة قاعدة الربط إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC02-CRR-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/correlation-rules/{id}/actions/retire` | — |
| الأمر | `CMD-CRR-RETIRE` | إحالة قاعدة الربط إلى التقاعد |
| السياسة | `POL-CRR-RETIRE` | Analyst lead (retire)؛ tenant match; inputs visible |
| الحدث | `EVT-CRR-RETIRED` | يصل إلى: Correlation engine |
| الكيان | `AGG-CORRELATION-RULE` | قاعدة الربط |
| الجدول | `information.correlation_rules` | الجدول الرئيسي لقاعدة الربط |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| الاختبار | TST-CORRELATION-RULE-SM، TST-SLC15-INVARIANTS | دورة حالات قاعدة الربط، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC02-CRR-RETIRE -->

</details>

### 5.5 US-DOM-ANL-CRR-LIST — عرض قواعد الربط وإصداراتها

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

<!-- BEGIN GENERATED: refs US-DOM-ANL-CRR-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
| المصدر | `00-open-questions.md §4` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
<!-- END GENERATED: refs US-DOM-ANL-CRR-LIST -->

</details>

### 5.6 US-UI-SCR26-CORRELATION-RULES — إدارة قواعد الربط بجوار قواعد المطابقة

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

<!-- BEGIN GENERATED: refs US-UI-SCR26-CORRELATION-RULES -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-26 | شاشة التعارض ومطابقة الكيانات |
| المصدر | `00-open-questions.md §4` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
<!-- END GENERATED: refs US-UI-SCR26-CORRELATION-RULES -->

</details>

### 5.7 US-UI-SCR26-CRR-APPROVAL — مراجعة القاعدة واعتمادها من شخص ثانٍ

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR26-CRR-APPROVAL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-26 | شاشة التعارض ومطابقة الكيانات |
| المصدر | `17-security-design.md §12.4` | — |
| المصدر | `00-open-questions.md §4` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR26-CRR-APPROVAL -->

</details>

### 5.8 US-OPS-ANL-CORRELATION-CALIBRATE — إعادة معايرة عتبات الربط بعد التجربة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-ANL-CORRELATION-CALIBRATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `correlation-fusion-spec.md (recalibrate_after_pilot)` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… |
| حالة الاستخدام | UC-132 | Review Correlation Proposal |
<!-- END GENERATED: refs US-OPS-ANL-CORRELATION-CALIBRATE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposal… | `US-BC02-CRR-ACTIVATE`، `US-BC02-CRR-DEFINE`، `US-BC02-CRR-EDIT`، `US-BC02-CRR-RETIRE`، `US-DOM-ANL-CRR-LIST`، `US-OPS-ANL-CORRELATION-CALIBRATE`، `US-UI-SCR26-CORRELATION-RULES` | TST-CORRELATION-PROPOSAL-SM، TST-CORRELATION-RULE-SM، TST-SLC15-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
