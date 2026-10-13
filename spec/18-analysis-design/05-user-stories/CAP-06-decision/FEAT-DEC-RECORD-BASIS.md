---
id: FEAT-DEC-RECORD-BASIS
type: feature
title: "سجل القرار وأساسه"
status: DRAFT
version: "0.1"
capability: CAP-06.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# سجل القرار وأساسه

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-DEC-RECORD-BASIS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-06 إدارة القرار |
| القدرة الفرعية | CAP-06.02 تسجيل القرار والتحقق من السلطة (R1) |
| الأدوار | المدير؛ المدقِّق؛ صاحب السلطة أو المعتمِد الثاني؛ النظام |
| الشاشات | SCR-33 القرار وأساسه |
| حالات الاستخدام | UC-032 |
| القصص | 8: 4 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعرف المدير والمدقق ما الذي قُرر ولماذا وما كان معروفًا وقت القرار، ويُبطل صاحب السلطة الأعلى القرار عند الحاجة.

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
| QAS-TMP-001 | asks for state as of valid time T known at record time K | 100 % agreement with temporal oracle corpus |
| QAS-TRC-001 | follows a decision back to its sources | 100 % of decisions and T1 derived objects traceable to sources |
| QAS-TRC-003 | auditor asks for a decision's basis | authority chain, pinned citations and claims as known at decision time returned; 100 % of decisions |
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
| `US-BC04-DEC-ANNUL` | إبطال القرار | أمر | مسودة |
| `US-BC04-Q-DEC-BASIS` | جلب: What was known at decision time: cited assessments (pinned versions) and their key claims resolved known_at = decision.recorded_at | جلب | مسودة |
| `US-BC04-Q-DEC-GET` | جلب: Decision with authority snapshot, citations (pinned) and supersession chain | جلب | مسودة |
| `US-DOM-DEC-LIST` | سجل القرارات للمدير والمدقق | جلب | مسودة |
| `US-BC04-S-DECISION-01` | تلقائي: superseding decision recorded (القرار) | نظام | مسودة |
| `US-UI-SCR33-BASIS-COMPARE` | مقارنة ما عُرف وقت القرار بما يُعرف الآن | واجهة | مسودة |
| `US-UI-SCR33-SUPERSESSION` | التنقل في سلسلة القرارات المستبدلة | واجهة | مسودة |
| `US-PLT-DEC-BASIS-TEMPORAL` | استرجاع أساس القرار كما كان معروفًا | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-DEC-ANNUL — إبطال القرار

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

<!-- BEGIN GENERATED: refs US-BC04-DEC-ANNUL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/decisions/{id}/actions/annul` | — |
| الأمر | `CMD-DEC-ANNUL` | إبطال القرار |
| السياسة | `POL-DEC-ANNUL` | authority holder (record) · higher authority (annul)؛ tenant match; object visible; org scope |
| الحدث | `EVT-DEC-ANNULLED` | يصل إلى: Decision request (DECIDED); Plans implementing it (review flag on supersede/annul); Search projectio… |
| الكيان | `AGG-DECISION` | القرار |
| الجدول | `operations.decisions` | الجدول الرئيسي للقرار |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-DEC-002، REQ-DEC-003، REQ-DEC-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-032 | Record Decision |
| الاختبار | TST-DECISION-SM، TST-SLC08-INVARIANTS | دورة حالات القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-DEC-ANNUL -->

</details>

### 5.2 US-BC04-Q-DEC-BASIS — جلب: What was known at decision time: cited assessments (pinned versions) and their key claims resolved known_at = decision.recorded_at

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

<!-- BEGIN GENERATED: refs US-BC04-Q-DEC-BASIS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/decisions/{decision_id}/basis` | — |
| الاستعلام | `QRY-DEC-BASIS` | What was known at decision time: cited assessments (pinned versions) and their key claims resolved known_at =… |
| السياسة | `POL-DEC-BASIS` | label rule; Auditor |
| الكيان | `AGG-DECISION` | القرار |
| الجدول | `operations.decisions` | الجدول الرئيسي للقرار |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-DEC-003 | The system shall record for each decision the selected option, rationale, authority, approval, effective time… |
| حالة الاستخدام | UC-032 | Record Decision |
| الاختبار | TST-DECISION-SM، TST-SLC08-INVARIANTS | دورة حالات القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-Q-DEC-BASIS -->

</details>

### 5.3 US-BC04-Q-DEC-GET — جلب: Decision with authority snapshot, citations (pinned) and supersession chain

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

<!-- BEGIN GENERATED: refs US-BC04-Q-DEC-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/decisions/{decision_id}` | — |
| الاستعلام | `QRY-DEC-GET` | Decision with authority snapshot, citations (pinned) and supersession chain |
| السياسة | `POL-DEC-GET` | label rule |
| الكيان | `AGG-DECISION` | القرار |
| الجدول | `operations.decisions` | الجدول الرئيسي للقرار |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-DEC-003 | The system shall record for each decision the selected option, rationale, authority, approval, effective time… |
| حالة الاستخدام | UC-032 | Record Decision |
| الاختبار | TST-DECISION-SM، TST-SLC08-INVARIANTS | دورة حالات القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-Q-DEC-GET -->

</details>

### 5.4 US-DOM-DEC-LIST — سجل القرارات للمدير والمدقق

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

<!-- BEGIN GENERATED: refs US-DOM-DEC-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-TRC-001 | follows a decision back to its sources → 100 % of decisions and T1 derived objects traceable to sources |
| حالة الاستخدام | UC-032 | Record Decision |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-DEC-003 | The system shall record for each decision the selected option, rationale, authority, approval, effective time… |
| حالة الاستخدام | UC-032 | Record Decision |
<!-- END GENERATED: refs US-DOM-DEC-LIST -->

</details>

### 5.5 US-BC04-S-DECISION-01 — تلقائي: superseding decision recorded (القرار)

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

<!-- BEGIN GENERATED: refs US-BC04-S-DECISION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:superseding decision recorded` | new decision references this one in supersedes |
| الانتقال | RECORDED ← SUPERSEDED | — |
| الحدث | `EVT-DEC-SUPERSEDED` | يصل إلى: Decision request (DECIDED); Plans implementing it (review flag on supersede/annul); Search projectio… |
| الكيان | `AGG-DECISION` | القرار |
| الجدول | `operations.decisions` | الجدول الرئيسي للقرار |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-DEC-002، REQ-DEC-003، REQ-DEC-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-032 | Record Decision |
| الاختبار | TST-DECISION-SM، TST-SLC08-INVARIANTS | دورة حالات القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-S-DECISION-01 -->

</details>

### 5.6 US-UI-SCR33-BASIS-COMPARE — مقارنة ما عُرف وقت القرار بما يُعرف الآن

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

<!-- BEGIN GENERATED: refs US-UI-SCR33-BASIS-COMPARE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-33 | شاشة القرار وأساسه |
| الجودة | QAS-TRC-003 | auditor asks for a decision's basis → authority chain, pinned citations and claims as known at decision time… |
| المصدر | `decision-plan-spec.md §1` | — |
<!-- END GENERATED: refs US-UI-SCR33-BASIS-COMPARE -->

</details>

### 5.7 US-UI-SCR33-SUPERSESSION — التنقل في سلسلة القرارات المستبدلة

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

<!-- BEGIN GENERATED: refs US-UI-SCR33-SUPERSESSION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-33 | شاشة القرار وأساسه |
| المتطلب | REQ-DEC-004 | The system shall make a recorded decision immutable; a change shall be recorded as a new decision that supers… |
| حالة الاستخدام | UC-032 | Record Decision |
<!-- END GENERATED: refs US-UI-SCR33-SUPERSESSION -->

</details>

### 5.8 US-PLT-DEC-BASIS-TEMPORAL — استرجاع أساس القرار كما كان معروفًا

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

<!-- BEGIN GENERATED: refs US-PLT-DEC-BASIS-TEMPORAL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-TRC-003 | auditor asks for a decision's basis → authority chain, pinned citations and claims as known at decision time… |
| الجودة | QAS-TMP-001 | asks for state as of valid time T known at record time K → 100 % agreement with temporal oracle corpus |
| المصدر | `decision-plan-spec.md §1` | — |
<!-- END GENERATED: refs US-PLT-DEC-BASIS-TEMPORAL -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-DEC-002 | When a decision is recorded, the system shall verify through the authority check that the decider holds the r… | `US-BC04-DEC-ANNUL`، `US-BC04-S-DECISION-01` | TST-DECISION-SM، TST-SLC08-INVARIANTS |
| REQ-DEC-003 | The system shall record for each decision the selected option, rationale, authority, approval, effective time… | `US-BC04-DEC-ANNUL`، `US-BC04-Q-DEC-BASIS`، `US-BC04-Q-DEC-GET`، `US-BC04-S-DECISION-01`، `US-DOM-DEC-LIST` | TST-DECISION-SM، TST-SLC08-INVARIANTS |
| REQ-DEC-004 | The system shall make a recorded decision immutable; a change shall be recorded as a new decision that supers… | `US-BC04-DEC-ANNUL`، `US-BC04-S-DECISION-01`، `US-UI-SCR33-SUPERSESSION` | TST-DECISION-SM، TST-SLC08-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
