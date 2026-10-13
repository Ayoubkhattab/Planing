---
id: FEAT-RSK-INCIDENT-REPORT
type: feature
title: "الإبلاغ عن الحوادث وتقييمها"
status: DRAFT
version: "0.1"
capability: CAP-09.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# الإبلاغ عن الحوادث وتقييمها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RSK-INCIDENT-REPORT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-09 المخاطر والطوارئ |
| القدرة الفرعية | CAP-09.02 الحوادث والاستجابة (R3) |
| الأدوار | المُبلِّغ؛ مقيّم الحادثة؛ أي مستخدم مخوَّل |
| الشاشات | SCR-47 سجل المخاطر والحوادث |
| حالات الاستخدام | UC-142 |
| القصص | 8: 5 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يبلّغ أي مستخدم مخوَّل عن حادثة فورًا، ويحدد المقيّم خطورتها، ويتابع الجميع الحوادث ضمن نطاقهم.

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
| `US-BC04-INC-ASSESS` | تقييم الحادثة | أمر | مسودة |
| `US-BC04-INC-CANCEL` | إلغاء الحادثة | أمر | مسودة |
| `US-BC04-INC-REPORT` | الإبلاغ عن الحادثة | أمر | مسودة |
| `US-BC04-Q-INC-GET` | جلب: Incident بنطاقه المرئي للطالب | جلب | مسودة |
| `US-BC04-Q-INC-LIST` | جلب: حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق | جلب | مسودة |
| `US-UI-SCR47-INCIDENT-LIST` | قائمة الحوادث بالتصفية والخطورة | واجهة | مسودة |
| `US-UI-SCR47-INCIDENT-MAP` | عرض الحوادث ضمن نطاقي على الخريطة | واجهة | مسودة |
| `US-UI-SCR47-QUICK-REPORT` | إبلاغ سريع عن حادثة بأقل الحقول | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-INC-ASSESS — تقييم الحادثة

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

<!-- BEGIN GENERATED: refs US-BC04-INC-ASSESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/incidents/{id}/actions/assess` | — |
| الأمر | `CMD-INC-ASSESS` | تقييم الحادثة |
| السياسة | `POL-INC-ASSESS` | مقيّم الحادثة؛ tenant match; affected_scope_refs visible to actor |
| الحدث | `EVT-INC-ASSESSED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-006، REQ-RCM-007، REQ-RCM-008، REQ-RCM-009، REQ-RCM-010، REQ-RCM-012، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-142 | Report & Assess Incident |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-INC-ASSESS -->

</details>

### 5.2 US-BC04-INC-CANCEL — إلغاء الحادثة

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

<!-- BEGIN GENERATED: refs US-BC04-INC-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/incidents/{id}/actions/cancel` | — |
| الأمر | `CMD-INC-CANCEL` | إلغاء الحادثة |
| السياسة | `POL-INC-CANCEL` | أي مُبلِّغ مخوَّل (تبليغ، إلغاء)؛ tenant match |
| الحدث | `EVT-INC-CANCELLED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-006، REQ-RCM-007، REQ-RCM-008، REQ-RCM-009، REQ-RCM-010، REQ-RCM-012، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-142 | Report & Assess Incident |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-INC-CANCEL -->

</details>

### 5.3 US-BC04-INC-REPORT — الإبلاغ عن الحادثة

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

<!-- BEGIN GENERATED: refs US-BC04-INC-REPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/incidents` | — |
| الأمر | `CMD-INC-REPORT` | الإبلاغ عن الحادثة |
| السياسة | `POL-INC-REPORT` | أي مُبلِّغ مخوَّل (تبليغ، إلغاء)؛ tenant match; scope_refs visible to actor |
| الحدث | `EVT-INC-REPORTED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-006، REQ-RCM-007، REQ-RCM-008، REQ-RCM-009، REQ-RCM-010، REQ-RCM-012، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-142 | Report & Assess Incident |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-INC-REPORT -->

</details>

### 5.4 US-BC04-Q-INC-GET — جلب: Incident بنطاقه المرئي للطالب

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-Q-INC-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/incidents/{incident_id}` | — |
| الاستعلام | `QRY-INC-GET` | Incident بنطاقه المرئي للطالب |
| السياسة | `POL-INC-GET` | allowed_scope |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-RCM-015 | The system shall let an authorized actor list and filter incidents by category, severity, status and scope, r… |
| حالة الاستخدام | UC-142 | Report & Assess Incident |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-Q-INC-GET -->

</details>

### 5.5 US-BC04-Q-INC-LIST — جلب: حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-Q-INC-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/incidents` | — |
| الاستعلام | `QRY-INC-LIST` | حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق |
| السياسة | `POL-INC-LIST` | allowed_scope |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-RCM-015 | The system shall let an authorized actor list and filter incidents by category, severity, status and scope, r… |
| حالة الاستخدام | UC-142 | Report & Assess Incident |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-Q-INC-LIST -->

</details>

### 5.6 US-UI-SCR47-INCIDENT-LIST — قائمة الحوادث بالتصفية والخطورة

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

<!-- BEGIN GENERATED: refs US-UI-SCR47-INCIDENT-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| المصدر | `21-ui-design.md §10` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RCM-015 | The system shall let an authorized actor list and filter incidents by category, severity, status and scope, r… |
| حالة الاستخدام | UC-142 | Report & Assess Incident |
<!-- END GENERATED: refs US-UI-SCR47-INCIDENT-LIST -->

</details>

### 5.7 US-UI-SCR47-INCIDENT-MAP — عرض الحوادث ضمن نطاقي على الخريطة

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

<!-- BEGIN GENERATED: refs US-UI-SCR47-INCIDENT-MAP -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| المصدر | `21-ui-design.md §7` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RCM-015 | The system shall let an authorized actor list and filter incidents by category, severity, status and scope, r… |
| حالة الاستخدام | UC-142 | Report & Assess Incident |
<!-- END GENERATED: refs US-UI-SCR47-INCIDENT-MAP -->

</details>

### 5.8 US-UI-SCR47-QUICK-REPORT — إبلاغ سريع عن حادثة بأقل الحقول

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

<!-- BEGIN GENERATED: refs US-UI-SCR47-QUICK-REPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RCM-006 | The system shall allow any authorized actor to report an incident with a hazard category, description, at lea… |
| حالة الاستخدام | UC-142 | Report & Assess Incident |
<!-- END GENERATED: refs US-UI-SCR47-QUICK-REPORT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RCM-006 | The system shall allow any authorized actor to report an incident with a hazard category, description, at lea… | `US-BC04-INC-ASSESS`، `US-BC04-INC-CANCEL`، `US-BC04-INC-REPORT`، `US-UI-SCR47-QUICK-REPORT` | TST-INCIDENT-SM |
| REQ-RCM-007 | The system shall require an authorized assessor to set an incident's severity to one of MINOR, MAJOR, EMERGEN… | كل قصص الأوامر والنظام في الميزة (3) | TST-INCIDENT-SM |
| REQ-RCM-008 | The system shall require a commander and at least one linked response task before an incident moves to respon… | كل قصص الأوامر والنظام في الميزة (3) | TST-INCIDENT-SM |
| REQ-RCM-009 | When an incident's severity is escalated, the system shall accept only a value higher than the current severi… | كل قصص الأوامر والنظام في الميزة (3) | TST-INCIDENT-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-010 | The system shall reject closing an incident while any of its linked response tasks is not in a terminal state. | كل قصص الأوامر والنظام في الميزة (3) | TST-INCIDENT-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-012 | When an incident references a risk as materialized, the system shall not change that risk's state automatical… | كل قصص الأوامر والنظام في الميزة (3) | TST-INCIDENT-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-013 | The system shall allow a response task to be created directly under an incident (incident_ref) without requir… | كل قصص الأوامر والنظام في الميزة (3) | TST-INCIDENT-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-015 | The system shall let an authorized actor list and filter incidents by category, severity, status and scope, r… | `US-BC04-Q-INC-GET`، `US-BC04-Q-INC-LIST`، `US-UI-SCR47-INCIDENT-LIST`، `US-UI-SCR47-INCIDENT-MAP` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
