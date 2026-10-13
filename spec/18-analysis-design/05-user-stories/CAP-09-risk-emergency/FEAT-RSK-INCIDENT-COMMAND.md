---
id: FEAT-RSK-INCIDENT-COMMAND
type: feature
title: "قيادة الاستجابة للحادثة"
status: DRAFT
version: "0.1"
capability: CAP-09.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# قيادة الاستجابة للحادثة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RSK-INCIDENT-COMMAND |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-09 المخاطر والطوارئ |
| القدرة الفرعية | CAP-09.02 الحوادث والاستجابة (R3) |
| الأدوار | قائد الحادثة؛ النظام |
| الشاشات | SCR-47 سجل المخاطر والحوادث، SCR-01 مهامي |
| حالات الاستخدام | UC-143 |
| القصص | 11: 7 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يوجّه قائد الحادثة الاستجابة ويصعّد الخطورة أو يخفضها حتى الاحتواء والحل والإغلاق، ويُنبَّه إن تأخر التوجيه.

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
| QAS-RCM-001 | CRISIS-severity incident assessed | response dispatched within the severity's SLA (tagged: recalibrate after Pilot R1 and R2 — RSK-028) |
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
| `US-BC04-INC-CLOSE` | إغلاق الحادثة | أمر | مسودة |
| `US-BC04-INC-CONTAIN` | احتواء الحادثة | أمر | مسودة |
| `US-BC04-INC-DE-ESCALATE` | خفض خطورة الحادثة | أمر | مسودة |
| `US-BC04-INC-DISPATCH-RESPONSE` | توجيه الاستجابة لـالحادثة | أمر | مسودة |
| `US-BC04-INC-ESCALATE` | تصعيد الحادثة | أمر | مسودة |
| `US-BC04-INC-RESOLVE` | حل الحادثة | أمر | مسودة |
| `US-BC04-S-INCIDENT-01` | تلقائي: response SLA elapsed without dispatch (الحادثة) | نظام | مسودة |
| `US-UI-SCR47-COMMAND-ACTIONS` | أفعال قائد الحادثة حسب حالتها | واجهة | مسودة |
| `US-UI-SCR47-DISPATCH` | توجيه الاستجابة بقائد ومهام مرتبطة | واجهة | مسودة |
| `US-UI-SCR47-SEVERITY-HISTORY` | سجل تغير خطورة الحادثة | واجهة | مسودة |
| `US-OPS-RSK-SLA-RECALIBRATE` | ضبط مهل الاستجابة حسب الخطورة بعد التجربة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-INC-CLOSE — إغلاق الحادثة

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

<!-- BEGIN GENERATED: refs US-BC04-INC-CLOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/incidents/{id}/actions/close` | — |
| الأمر | `CMD-INC-CLOSE` | إغلاق الحادثة |
| السياسة | `POL-INC-CLOSE` | قائد الحادثة؛ tenant match |
| الحدث | `EVT-INC-CLOSED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-006، REQ-RCM-007، REQ-RCM-008، REQ-RCM-009، REQ-RCM-010، REQ-RCM-012، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-143 | Command Incident Response |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-INC-CLOSE -->

</details>

### 5.2 US-BC04-INC-CONTAIN — احتواء الحادثة

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

<!-- BEGIN GENERATED: refs US-BC04-INC-CONTAIN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/incidents/{id}/actions/contain` | — |
| الأمر | `CMD-INC-CONTAIN` | احتواء الحادثة |
| السياسة | `POL-INC-CONTAIN` | قائد الحادثة؛ tenant match |
| الحدث | `EVT-INC-CONTAINED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-006، REQ-RCM-007، REQ-RCM-008، REQ-RCM-009، REQ-RCM-010، REQ-RCM-012، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-143 | Command Incident Response |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-INC-CONTAIN -->

</details>

### 5.3 US-BC04-INC-DE-ESCALATE — خفض خطورة الحادثة

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

<!-- BEGIN GENERATED: refs US-BC04-INC-DE-ESCALATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/incidents/{id}/actions/de-escalate` | — |
| الأمر | `CMD-INC-DE-ESCALATE` | خفض خطورة الحادثة |
| السياسة | `POL-INC-DE-ESCALATE` | قائد الحادثة بسلطة صريحة؛ tenant match; new_severity أدنى بمستوى واحد كحد أقصى (INV-INC-01) |
| الحدث | `EVT-INC-DE-ESCALATED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-006، REQ-RCM-007، REQ-RCM-008، REQ-RCM-009، REQ-RCM-010، REQ-RCM-012، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-143 | Command Incident Response |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-INC-DE-ESCALATE -->

</details>

### 5.4 US-BC04-INC-DISPATCH-RESPONSE — توجيه الاستجابة لـالحادثة

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

<!-- BEGIN GENERATED: refs US-BC04-INC-DISPATCH-RESPONSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/incidents/{id}/actions/dispatch-response` | — |
| الأمر | `CMD-INC-DISPATCH-RESPONSE` | توجيه الاستجابة لـالحادثة |
| السياسة | `POL-INC-DISPATCH-RESPONSE` | قائد الحادثة؛ tenant match; commander authorized in scope |
| الحدث | `EVT-INC-RESPONSE-DISPATCHED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-006، REQ-RCM-007، REQ-RCM-008، REQ-RCM-009، REQ-RCM-010، REQ-RCM-012، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-143 | Command Incident Response |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-INC-DISPATCH-RESPONSE -->

</details>

### 5.5 US-BC04-INC-ESCALATE — تصعيد الحادثة

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

<!-- BEGIN GENERATED: refs US-BC04-INC-ESCALATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/incidents/{id}/actions/escalate` | — |
| الأمر | `CMD-INC-ESCALATE` | تصعيد الحادثة |
| السياسة | `POL-INC-ESCALATE` | قائد الحادثة؛ tenant match; new_severity أعلى فقط (INV-INC-01) |
| الحدث | `EVT-INC-ESCALATED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-006، REQ-RCM-007، REQ-RCM-008، REQ-RCM-009، REQ-RCM-010، REQ-RCM-012، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-143 | Command Incident Response |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-INC-ESCALATE -->

</details>

### 5.6 US-BC04-INC-RESOLVE — حل الحادثة

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

<!-- BEGIN GENERATED: refs US-BC04-INC-RESOLVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/incidents/{id}/actions/resolve` | — |
| الأمر | `CMD-INC-RESOLVE` | حل الحادثة |
| السياسة | `POL-INC-RESOLVE` | قائد الحادثة؛ tenant match; كل مهام الاستجابة نهائية (INV-INC-02) |
| الحدث | `EVT-INC-RESOLVED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-006، REQ-RCM-007، REQ-RCM-008، REQ-RCM-009، REQ-RCM-010، REQ-RCM-012، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-143 | Command Incident Response |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-INC-RESOLVE -->

</details>

### 5.7 US-BC04-S-INCIDENT-01 — تلقائي: response SLA elapsed without dispatch (الحادثة)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC04-S-INCIDENT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:response SLA elapsed without dispatch` | المجدول؛ SLA حسب severity، موسوم 'تُعاد معايرته بعد Pilot R1/R2' (RSK-028) |
| الانتقال | REPORTED, ASSESSED ← (بلا تغيير) | — |
| الحدث | `EVT-INC-SLA-BREACHED` | يصل إلى: Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q… |
| الكيان | `AGG-INCIDENT` | الحادثة |
| الجدول | `operations.incidents` | الجدول الرئيسي للحادثة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-006، REQ-RCM-007، REQ-RCM-008، REQ-RCM-009، REQ-RCM-010، REQ-RCM-012، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-143 | Command Incident Response |
| الاختبار | TST-INCIDENT-SM، TST-SLC17-INVARIANTS | دورة حالات الحادثة، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-S-INCIDENT-01 -->

</details>

### 5.8 US-UI-SCR47-COMMAND-ACTIONS — أفعال قائد الحادثة حسب حالتها

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

<!-- BEGIN GENERATED: refs US-UI-SCR47-COMMAND-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| المصدر | `21-ui-design.md §6.3` | — |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-RCM-009، REQ-RCM-010 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-143 | Command Incident Response |
<!-- END GENERATED: refs US-UI-SCR47-COMMAND-ACTIONS -->

</details>

### 5.9 US-UI-SCR47-DISPATCH — توجيه الاستجابة بقائد ومهام مرتبطة

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

<!-- BEGIN GENERATED: refs US-UI-SCR47-DISPATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| الشاشة | SCR-02 | شاشة تفاصيل المهمة وسجلها |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-RCM-008، REQ-RCM-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-143 | Command Incident Response |
<!-- END GENERATED: refs US-UI-SCR47-DISPATCH -->

</details>

### 5.10 US-UI-SCR47-SEVERITY-HISTORY — سجل تغير خطورة الحادثة

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

<!-- BEGIN GENERATED: refs US-UI-SCR47-SEVERITY-HISTORY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| المصدر | `THR-S17-01` | — |
| المصدر | `risk-contingency-spec.md §6` | — |
<!-- END GENERATED: refs US-UI-SCR47-SEVERITY-HISTORY -->

</details>

### 5.11 US-OPS-RSK-SLA-RECALIBRATE — ضبط مهل الاستجابة حسب الخطورة بعد التجربة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R3 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-RSK-SLA-RECALIBRATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-RCM-001 | CRISIS-severity incident assessed → response dispatched within the severity's SLA (tagged: recalibrate after… |
| المصدر | `risk-contingency-spec.md §6` | — |
| المصدر | `US-BC04-S-INCIDENT-01` | — |
<!-- END GENERATED: refs US-OPS-RSK-SLA-RECALIBRATE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RCM-006 | The system shall allow any authorized actor to report an incident with a hazard category, description, at lea… | كل قصص الميزة المأخوذة من المواصفة (7) | TST-INCIDENT-SM |
| REQ-RCM-007 | The system shall require an authorized assessor to set an incident's severity to one of MINOR, MAJOR, EMERGEN… | كل قصص الميزة المأخوذة من المواصفة (7) | TST-INCIDENT-SM |
| REQ-RCM-008 | The system shall require a commander and at least one linked response task before an incident moves to respon… | `US-BC04-INC-CLOSE`، `US-BC04-INC-CONTAIN`، `US-BC04-INC-DE-ESCALATE`، `US-BC04-INC-DISPATCH-RESPONSE`، `US-BC04-INC-ESCALATE`، `US-BC04-INC-RESOLVE`، `US-BC04-S-INCIDENT-01`، `US-UI-SCR47-DISPATCH` | TST-INCIDENT-SM |
| REQ-RCM-009 | When an incident's severity is escalated, the system shall accept only a value higher than the current severi… | `US-BC04-INC-CLOSE`، `US-BC04-INC-CONTAIN`، `US-BC04-INC-DE-ESCALATE`، `US-BC04-INC-DISPATCH-RESPONSE`، `US-BC04-INC-ESCALATE`، `US-BC04-INC-RESOLVE`، `US-BC04-S-INCIDENT-01`، `US-UI-SCR47-COMMAND-ACTIONS` | TST-INCIDENT-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-010 | The system shall reject closing an incident while any of its linked response tasks is not in a terminal state. | `US-BC04-INC-CLOSE`، `US-BC04-INC-CONTAIN`، `US-BC04-INC-DE-ESCALATE`، `US-BC04-INC-DISPATCH-RESPONSE`، `US-BC04-INC-ESCALATE`، `US-BC04-INC-RESOLVE`، `US-BC04-S-INCIDENT-01`، `US-UI-SCR47-COMMAND-ACTIONS` | TST-INCIDENT-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-012 | When an incident references a risk as materialized, the system shall not change that risk's state automatical… | كل قصص الميزة المأخوذة من المواصفة (7) | TST-INCIDENT-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-013 | The system shall allow a response task to be created directly under an incident (incident_ref) without requir… | `US-BC04-INC-CLOSE`، `US-BC04-INC-CONTAIN`، `US-BC04-INC-DE-ESCALATE`، `US-BC04-INC-DISPATCH-RESPONSE`، `US-BC04-INC-ESCALATE`، `US-BC04-INC-RESOLVE`، `US-BC04-S-INCIDENT-01`، `US-UI-SCR47-DISPATCH` | TST-INCIDENT-SM، TST-SLC17-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
