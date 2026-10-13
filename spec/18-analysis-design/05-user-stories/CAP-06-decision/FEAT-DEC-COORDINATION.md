---
id: FEAT-DEC-COORDINATION
type: feature
title: "إدارة حالة التنسيق"
status: DRAFT
version: "0.1"
capability: CAP-06.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة حالة التنسيق

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-DEC-COORDINATION |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-06 إدارة القرار |
| القدرة الفرعية | CAP-06.03 التنسيق (R2) |
| الأدوار | مدير الجهة القائدة |
| الشاشات | SCR-36 حالات التنسيق |
| حالات الاستخدام | UC-130 |
| القصص | 8: 7 من المواصفة، و1 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يجمع مدير الجهة القائدة الجهات التي يجب أن تعمل معًا، ويوزع المسؤوليات بينها ويتابع الحالة حتى إغلاقها.

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
| `US-BC04-CRD-ACTIVATE` | تفعيل حالة التنسيق | أمر | مسودة |
| `US-BC04-CRD-ADD-PARTICIPANT` | إضافة مشارك إلى حالة التنسيق | أمر | مسودة |
| `US-BC04-CRD-ASSIGN-RESPONSIBILITY` | إسناد مسؤولية ضمن حالة التنسيق | أمر | مسودة |
| `US-BC04-CRD-CANCEL` | إلغاء حالة التنسيق | أمر | مسودة |
| `US-BC04-CRD-CLOSE` | إغلاق حالة التنسيق | أمر | مسودة |
| `US-BC04-CRD-OPEN` | فتح حالة التنسيق | أمر | مسودة |
| `US-BC04-CRD-REMOVE-PARTICIPANT` | إزالة مشارك من حالة التنسيق | أمر | مسودة |
| `US-UI-SCR36-COORD-BOARD` | لوحة المشاركين والمسؤوليات وحالة التنسيق | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-CRD-ACTIVATE — تفعيل حالة التنسيق

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

<!-- BEGIN GENERATED: refs US-BC04-CRD-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/coordination-cases/{id}/actions/activate` | — |
| الأمر | `CMD-CRD-ACTIVATE` | تفعيل حالة التنسيق |
| السياسة | `POL-CRD-ACTIVATE` | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update… |
| الحدث | `EVT-CRD-ACTIVATED` | يصل إلى: Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-CRD-001، REQ-CRD-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-CRD-ACTIVATE -->

</details>

### 5.2 US-BC04-CRD-ADD-PARTICIPANT — إضافة مشارك إلى حالة التنسيق

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

<!-- BEGIN GENERATED: refs US-BC04-CRD-ADD-PARTICIPANT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/coordination-cases/{id}/actions/add-participant` | — |
| الأمر | `CMD-CRD-ADD-PARTICIPANT` | إضافة مشارك إلى حالة التنسيق |
| السياسة | `POL-CRD-ADD-PARTICIPANT` | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update… |
| الحدث | `EVT-CRD-PARTICIPANT-ADDED` | يصل إلى: Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-CRD-001، REQ-CRD-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-CRD-ADD-PARTICIPANT -->

</details>

### 5.3 US-BC04-CRD-ASSIGN-RESPONSIBILITY — إسناد مسؤولية ضمن حالة التنسيق

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

<!-- BEGIN GENERATED: refs US-BC04-CRD-ASSIGN-RESPONSIBILITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/coordination-cases/{id}/actions/assign-responsibility` | — |
| الأمر | `CMD-CRD-ASSIGN-RESPONSIBILITY` | إسناد مسؤولية ضمن حالة التنسيق |
| السياسة | `POL-CRD-ASSIGN-RESPONSIBILITY` | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update… |
| الحدث | `EVT-CRD-RESPONSIBILITY-ASSIGNED` | يصل إلى: Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-CRD-001، REQ-CRD-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-CRD-ASSIGN-RESPONSIBILITY -->

</details>

### 5.4 US-BC04-CRD-CANCEL — إلغاء حالة التنسيق

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

<!-- BEGIN GENERATED: refs US-BC04-CRD-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/coordination-cases/{id}/actions/cancel` | — |
| الأمر | `CMD-CRD-CANCEL` | إلغاء حالة التنسيق |
| السياسة | `POL-CRD-CANCEL` | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update… |
| الحدث | `EVT-CRD-CANCELLED` | يصل إلى: Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-CRD-001، REQ-CRD-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-CRD-CANCEL -->

</details>

### 5.5 US-BC04-CRD-CLOSE — إغلاق حالة التنسيق

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

<!-- BEGIN GENERATED: refs US-BC04-CRD-CLOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/coordination-cases/{id}/actions/close` | — |
| الأمر | `CMD-CRD-CLOSE` | إغلاق حالة التنسيق |
| السياسة | `POL-CRD-CLOSE` | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update… |
| الحدث | `EVT-CRD-CLOSED` | يصل إلى: Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-CRD-001، REQ-CRD-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-CRD-CLOSE -->

</details>

### 5.6 US-BC04-CRD-OPEN — فتح حالة التنسيق

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

<!-- BEGIN GENERATED: refs US-BC04-CRD-OPEN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/coordination-cases` | — |
| الأمر | `CMD-CRD-OPEN` | فتح حالة التنسيق |
| السياسة | `POL-CRD-OPEN` | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update… |
| الحدث | `EVT-CRD-OPENED` | يصل إلى: Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-CRD-001، REQ-CRD-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-CRD-OPEN -->

</details>

### 5.7 US-BC04-CRD-REMOVE-PARTICIPANT — إزالة مشارك من حالة التنسيق

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

<!-- BEGIN GENERATED: refs US-BC04-CRD-REMOVE-PARTICIPANT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/coordination-cases/{id}/actions/remove-participant` | — |
| الأمر | `CMD-CRD-REMOVE-PARTICIPANT` | إزالة مشارك من حالة التنسيق |
| السياسة | `POL-CRD-REMOVE-PARTICIPANT` | lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update… |
| الحدث | `EVT-CRD-PARTICIPANT-REMOVED` | يصل إلى: Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| الكيان | `AGG-COORDINATION-CASE` | حالة التنسيق |
| الجدول | `operations.coordination_cases` | الجدول الرئيسي لحالة التنسيق |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-CRD-001، REQ-CRD-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
| الاختبار | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS | دورة حالات حالة التنسيق، وثوابت الشريحة SLC-15 |
<!-- END GENERATED: refs US-BC04-CRD-REMOVE-PARTICIPANT -->

</details>

### 5.8 US-UI-SCR36-COORD-BOARD — لوحة المشاركين والمسؤوليات وحالة التنسيق

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

<!-- BEGIN GENERATED: refs US-UI-SCR36-COORD-BOARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-36 | شاشة حالات التنسيق |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-CRD-001 | The system shall manage coordination cases linking decisions, plans and organizations that must act together,… |
| حالة الاستخدام | UC-130 | Manage Coordination Case |
<!-- END GENERATED: refs US-UI-SCR36-COORD-BOARD -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-CRD-001 | The system shall manage coordination cases linking decisions, plans and organizations that must act together,… | `US-BC04-CRD-ACTIVATE`، `US-BC04-CRD-ADD-PARTICIPANT`، `US-BC04-CRD-ASSIGN-RESPONSIBILITY`، `US-BC04-CRD-CANCEL`، `US-BC04-CRD-CLOSE`، `US-BC04-CRD-OPEN`، `US-BC04-CRD-REMOVE-PARTICIPANT`، `US-UI-SCR36-COORD-BOARD` | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS |
| REQ-CRD-002 | When a coordination action requires another organization's authority, the system shall route it for that auth… | كل قصص الميزة المأخوذة من المواصفة (7) | TST-COORDINATION-CASE-SM، TST-SLC15-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
