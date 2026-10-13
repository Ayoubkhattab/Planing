---
id: FEAT-DEC-COORD-PARTICIPATE
type: feature
title: "المشاركة في التنسيق"
status: DRAFT
version: "0.1"
capability: CAP-06.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# المشاركة في التنسيق

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-DEC-COORD-PARTICIPATE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-06 إدارة القرار |
| القدرة الفرعية | CAP-06.03 التنسيق (R2) |
| الأدوار | الجهة المشاركة؛ مدير الجهة القائدة؛ النظام |
| الشاشات | SCR-36 حالات التنسيق |
| حالات الاستخدام | UC-130، UC-131 |
| القصص | 7: 5 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

ترى الجهة المشاركة ما يخصها من حالة التنسيق، وتحدّث مسؤولياتها، وتطلب قرارًا من سلطة جهة أخرى.

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
| `US-BC04-CRD-REQUEST-DECISION` | طلب قرار ضمن حالة التنسيق | أمر | مسودة |
| `US-BC04-CRD-UPDATE-RESPONSIBILITY` | تحديث مسؤولية ضمن حالة التنسيق | أمر | مسودة |
| `US-BC04-Q-CRD-GET` | جلب: Case filtered to the caller's participant scope | جلب | مسودة |
| `US-BC04-Q-CRD-LIST` | جلب: Cases where the caller's unit participates | جلب | مسودة |
| `US-BC04-S-COORDINATION-CASE-01` | تلقائي: linked decision recorded (حالة التنسيق) | نظام | مسودة |
| `US-UI-SCR36-DECISION-ROUTING` | متابعة مسؤولية تنتظر قرار جهة أخرى | واجهة | مسودة |
| `US-UI-SCR36-PARTICIPANT-VIEW` | عرض الجهة المشاركة لما يخصها فقط | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-CRD-REQUEST-DECISION — طلب قرار ضمن حالة التنسيق

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

<!-- BEGIN GENERATED: refs US-BC04-CRD-REQUEST-DECISION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/coordination-cases/{id}/actions/request-decision` | — |
| الأمر | `CMD-CRD-REQUEST-DECISION` | طلب قرار ضمن حالة التنسيق |
| السياسة | `POL-CRD-REQUEST-DECISION` | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update… |
| الحدث | `EVT-CRD-DECISION-REQUESTED` | يصل إلى: Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-CRD-001، REQ-CRD-002 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-130، UC-131 | Manage Coordination Case؛ Request Cross-Organization Decision |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-CRD-REQUEST-DECISION -->

</details>

### 5.2 US-BC04-CRD-UPDATE-RESPONSIBILITY — تحديث مسؤولية ضمن حالة التنسيق

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

<!-- BEGIN GENERATED: refs US-BC04-CRD-UPDATE-RESPONSIBILITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/coordination-cases/{id}/actions/update-responsibility` | — |
| الأمر | `CMD-CRD-UPDATE-RESPONSIBILITY` | تحديث مسؤولية ضمن حالة التنسيق |
| السياسة | `POL-CRD-UPDATE-RESPONSIBILITY` | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update… |
| الحدث | `EVT-CRD-RESPONSIBILITY-UPDATED` | يصل إلى: Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-CRD-001، REQ-CRD-002 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-130، UC-131 | Manage Coordination Case؛ Request Cross-Organization Decision |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-CRD-UPDATE-RESPONSIBILITY -->

</details>

### 5.3 US-BC04-Q-CRD-GET — جلب: Case filtered to the caller's participant scope

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

<!-- BEGIN GENERATED: refs US-BC04-Q-CRD-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/coordination-cases/{case_id}` | — |
| الاستعلام | `QRY-CRD-GET` | Case filtered to the caller's participant scope |
| السياسة | `POL-CRD-GET` | participants (scope-limited); lead |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-CRD-001 | The system shall manage coordination cases linking decisions, plans and organizations that must act together,… |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-Q-CRD-GET -->

</details>

### 5.4 US-BC04-Q-CRD-LIST — جلب: Cases where the caller's unit participates

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

<!-- BEGIN GENERATED: refs US-BC04-Q-CRD-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/coordination-cases` | — |
| الاستعلام | `QRY-CRD-LIST` | Cases where the caller's unit participates |
| السياسة | `POL-CRD-LIST` | allowed_scope |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-CRD-001 | The system shall manage coordination cases linking decisions, plans and organizations that must act together,… |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-Q-CRD-LIST -->

</details>

### 5.5 US-BC04-S-COORDINATION-CASE-01 — تلقائي: linked decision recorded (حالة التنسيق)

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

<!-- BEGIN GENERATED: refs US-BC04-S-COORDINATION-CASE-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:linked decision recorded` | decision references the request created by the case; outcome stored on the responsibility |
| الانتقال | ACTIVE ← (بلا تغيير) | — |
| الحدث | `EVT-CRD-DECISION-RECORDED` | يصل إلى: Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-CRD-001، REQ-CRD-002 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-130، UC-131 | Manage Coordination Case؛ Request Cross-Organization Decision |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-S-COORDINATION-CASE-01 -->

</details>

### 5.6 US-UI-SCR36-DECISION-ROUTING — متابعة مسؤولية تنتظر قرار جهة أخرى

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

<!-- BEGIN GENERATED: refs US-UI-SCR36-DECISION-ROUTING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-36 | شاشة حالات التنسيق |
| حالة الاستخدام | UC-131 | Request Cross-Organization Decision |
| المصدر | `THR-S15-02` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-CRD-002 | When a coordination action requires another organization's authority, the system shall route it for that auth… |
| حالة الاستخدام | UC-131 | Request Cross-Organization Decision |
<!-- END GENERATED: refs US-UI-SCR36-DECISION-ROUTING -->

</details>

### 5.7 US-UI-SCR36-PARTICIPANT-VIEW — عرض الجهة المشاركة لما يخصها فقط

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

<!-- BEGIN GENERATED: refs US-UI-SCR36-PARTICIPANT-VIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-36 | شاشة حالات التنسيق |
| المصدر | `THR-S15-01` | — |
| المصدر | `correlation-fusion-spec.md §1` | — |
| المتطلب | REQ-CRD-001 | The system shall manage coordination cases linking decisions, plans and organizations that must act together,… |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
<!-- END GENERATED: refs US-UI-SCR36-PARTICIPANT-VIEW -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-CRD-001 | The system shall manage coordination cases linking decisions, plans and organizations that must act together,… | `US-BC04-CRD-REQUEST-DECISION`، `US-BC04-CRD-UPDATE-RESPONSIBILITY`، `US-BC04-Q-CRD-GET`، `US-BC04-Q-CRD-LIST`، `US-BC04-S-COORDINATION-CASE-01`، `US-UI-SCR36-PARTICIPANT-VIEW` | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS |
| REQ-CRD-002 | When a coordination action requires another organization's authority, the system shall route it for that auth… | `US-BC04-CRD-REQUEST-DECISION`، `US-BC04-CRD-UPDATE-RESPONSIBILITY`، `US-BC04-S-COORDINATION-CASE-01`، `US-UI-SCR36-DECISION-ROUTING` | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
