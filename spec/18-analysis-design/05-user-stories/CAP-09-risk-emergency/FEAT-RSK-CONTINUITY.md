---
id: FEAT-RSK-CONTINUITY
type: feature
title: "تفعيل خطة الطوارئ ومتابعة التعافي"
status: DRAFT
version: "0.1"
capability: CAP-09.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تفعيل خطة الطوارئ ومتابعة التعافي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RSK-CONTINUITY |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-09 المخاطر والطوارئ |
| القدرة الفرعية | CAP-09.03 الاستمرارية والتعافي (R3) |
| الأدوار | قائد الحادثة؛ مالك الاستمرارية |
| الشاشات | SCR-47 سجل المخاطر والحوادث، SCR-35 متابعة التنفيذ |
| حالات الاستخدام | UC-144 |
| القصص | 4: 2 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يفعّل قائد الحادثة خطة الطوارئ بقرار صريح، ويتابع مع مالك الاستمرارية تقدم التعافي مقارنة بزمن بدء الحادثة.

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
| `US-BC04-INC-ACTIVATE-CONTINGENCY` | تفعيل خطة الاستمرارية لـالحادثة | أمر | مسودة |
| `US-BC04-Q-INC-RECOVERY-STATUS` | جلب: تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء الحادثة (RTO/RPO تقديرية) | جلب | مسودة |
| `US-UI-SCR47-ACTIVATE-CONTINGENCY` | تفعيل خطة الطوارئ بقرار صريح | واجهة | مسودة |
| `US-UI-SCR47-RECOVERY-STATUS` | تقدم التعافي مقابل زمن بدء الحادثة | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-INC-ACTIVATE-CONTINGENCY — تفعيل خطة الاستمرارية لـالحادثة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-INC-ACTIVATE-CONTINGENCY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/incidents/{id}/actions/activate-contingency` | — |
| الأمر | `CMD-INC-ACTIVATE-CONTINGENCY` | تفعيل خطة الاستمرارية لـالحادثة |
| السياسة | `POL-INC-ACTIVATE-CONTINGENCY` | قائد الحادثة بسلطة صريحة لتفعيل الاستمرارية؛ tenant match; أمر صريح دائماً (INV-INC-03) |
| الحدث | `EVT-INC-CONTINGENCY-ACTIVATED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-RCM-011 | The system shall never activate a contingency plan automatically as a side effect of a severity escalation; a… |
| حالة الاستخدام | UC-144 | Activate Contingency & Track Recovery |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-INC-ACTIVATE-CONTINGENCY -->

</details>

### 5.2 US-BC04-Q-INC-RECOVERY-STATUS — جلب: تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء الحادثة (RTO/RPO تقديرية)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R3 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-Q-INC-RECOVERY-STATUS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/incidents/{incident_id}/recovery-status` | — |
| الاستعلام | `QRY-INC-RECOVERY-STATUS` | تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء الحادثة (RTO/RPO تقديرية) |
| السياسة | `POL-INC-RECOVERY-STATUS` | القائد؛ مالك الاستمرارية |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-RCM-016 | The system shall compute an incident's recovery status from its linked contingency plan's task completion aga… |
| حالة الاستخدام | UC-144 | Activate Contingency & Track Recovery |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-Q-INC-RECOVERY-STATUS -->

</details>

### 5.3 US-UI-SCR47-ACTIVATE-CONTINGENCY — تفعيل خطة الطوارئ بقرار صريح

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR47-ACTIVATE-CONTINGENCY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| المصدر | `THR-S17-02` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RCM-011 | The system shall never activate a contingency plan automatically as a side effect of a severity escalation; a… |
| حالة الاستخدام | UC-144 | Activate Contingency & Track Recovery |
<!-- END GENERATED: refs US-UI-SCR47-ACTIVATE-CONTINGENCY -->

</details>

### 5.4 US-UI-SCR47-RECOVERY-STATUS — تقدم التعافي مقابل زمن بدء الحادثة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R3 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR47-RECOVERY-STATUS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| الشاشة | SCR-35 | شاشة متابعة التنفيذ |
| المصدر | `risk-contingency-spec.md §5` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RCM-016 | The system shall compute an incident's recovery status from its linked contingency plan's task completion aga… |
| حالة الاستخدام | UC-144 | Activate Contingency & Track Recovery |
<!-- END GENERATED: refs US-UI-SCR47-RECOVERY-STATUS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RCM-011 | The system shall never activate a contingency plan automatically as a side effect of a severity escalation; a… | `US-BC04-INC-ACTIVATE-CONTINGENCY`، `US-UI-SCR47-ACTIVATE-CONTINGENCY` | TST-INCIDENT-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-016 | The system shall compute an incident's recovery status from its linked contingency plan's task completion aga… | `US-BC04-Q-INC-RECOVERY-STATUS`، `US-UI-SCR47-RECOVERY-STATUS` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
