---
id: FEAT-SIT-ALERT-RULES
type: feature
title: "قواعد التنبيه"
status: DRAFT
version: "0.1"
capability: CAP-05.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# قواعد التنبيه

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-SIT-ALERT-RULES |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-05 الوعي بالموقف |
| القدرة الفرعية | CAP-05.02 المراقبة والتنبيه (R1) |
| الأدوار | قائد المحللين؛ المدير |
| الشاشات | SCR-12 إدارة الموقف وقواعد التنبيه |
| حالات الاستخدام | UC-023 |
| القصص | 9: 6 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يحدد قائد المحللين أو المدير متى يجب إطلاق تنبيه ولمن ويفعّل القاعدة أو يعطّلها.

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
| QAS-PERF-005 | reports a value that meets a critical alert rule | end-to-end p95 ≤ 5 s |
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
| `US-BC03-ARL-ACTIVATE` | تفعيل قاعدة التنبيه | أمر | مسودة |
| `US-BC03-ARL-DEFINE` | تعريف قاعدة التنبيه | أمر | مسودة |
| `US-BC03-ARL-DISABLE` | تعطيل قاعدة التنبيه | أمر | مسودة |
| `US-BC03-ARL-EDIT` | تعديل قاعدة التنبيه | أمر | مسودة |
| `US-BC03-ARL-ENABLE` | تمكين قاعدة التنبيه | أمر | مسودة |
| `US-BC03-ARL-RETIRE` | إحالة قاعدة التنبيه إلى التقاعد | أمر | مسودة |
| `US-DOM-ARL-DRY-RUN` | تجربة قاعدة التنبيه على أحداث آخر يوم | جلب | مسودة |
| `US-UI-SCR12-ALERT-RULE-EDITOR` | تعريف شرط التنبيه ومعاينة حجمه قبل التفعيل | واجهة | مسودة |
| `US-OPS-ALERT-STORM-LIMIT` | حد معدل لكل قاعدة يمنع سيل التنبيهات | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-ARL-ACTIVATE — تفعيل قاعدة التنبيه

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

<!-- BEGIN GENERATED: refs US-BC03-ARL-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/alert-rules/{id}/actions/activate` | — |
| الأمر | `CMD-ARL-ACTIVATE` | تفعيل قاعدة التنبيه |
| السياسة | `POL-ARL-ACTIVATE` | Analyst lead / Manager؛ tenant match; target visible to subject |
| الحدث | `EVT-ARL-ACTIVATED` | يصل إلى: Alert evaluator (reload rules) |
| الكيان | `AGG-ALERT-RULE` | قاعدة التنبيه |
| الجدول | `intelligence.alert_rules` | الجدول الرئيسي لقاعدة التنبيه |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-RULE-SM، TST-SLC06-INVARIANTS | دورة حالات قاعدة التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-ARL-ACTIVATE -->

</details>

### 5.2 US-BC03-ARL-DEFINE — تعريف قاعدة التنبيه

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

<!-- BEGIN GENERATED: refs US-BC03-ARL-DEFINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/alert-rules` | — |
| الأمر | `CMD-ARL-DEFINE` | تعريف قاعدة التنبيه |
| السياسة | `POL-ARL-DEFINE` | Analyst lead / Manager؛ tenant match; target visible to subject |
| الحدث | `EVT-ARL-DEFINED` | يصل إلى: Alert evaluator (reload rules) |
| الكيان | `AGG-ALERT-RULE` | قاعدة التنبيه |
| الجدول | `intelligence.alert_rules` | الجدول الرئيسي لقاعدة التنبيه |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-RULE-SM، TST-SLC06-INVARIANTS | دورة حالات قاعدة التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-ARL-DEFINE -->

</details>

### 5.3 US-BC03-ARL-DISABLE — تعطيل قاعدة التنبيه

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

<!-- BEGIN GENERATED: refs US-BC03-ARL-DISABLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/alert-rules/{id}/actions/disable` | — |
| الأمر | `CMD-ARL-DISABLE` | تعطيل قاعدة التنبيه |
| السياسة | `POL-ARL-DISABLE` | Analyst lead / Manager؛ tenant match; target visible to subject |
| الحدث | `EVT-ARL-DISABLED` | يصل إلى: Alert evaluator (reload rules) |
| الكيان | `AGG-ALERT-RULE` | قاعدة التنبيه |
| الجدول | `intelligence.alert_rules` | الجدول الرئيسي لقاعدة التنبيه |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-RULE-SM، TST-SLC06-INVARIANTS | دورة حالات قاعدة التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-ARL-DISABLE -->

</details>

### 5.4 US-BC03-ARL-EDIT — تعديل قاعدة التنبيه

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

<!-- BEGIN GENERATED: refs US-BC03-ARL-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/alert-rules/{id}/actions/edit` | — |
| الأمر | `CMD-ARL-EDIT` | تعديل قاعدة التنبيه |
| السياسة | `POL-ARL-EDIT` | Analyst lead / Manager؛ tenant match; target visible to subject |
| الحدث | `EVT-ARL-EDITED` | يصل إلى: Alert evaluator (reload rules) |
| الكيان | `AGG-ALERT-RULE` | قاعدة التنبيه |
| الجدول | `intelligence.alert_rules` | الجدول الرئيسي لقاعدة التنبيه |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-RULE-SM، TST-SLC06-INVARIANTS | دورة حالات قاعدة التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-ARL-EDIT -->

</details>

### 5.5 US-BC03-ARL-ENABLE — تمكين قاعدة التنبيه

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

<!-- BEGIN GENERATED: refs US-BC03-ARL-ENABLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/alert-rules/{id}/actions/enable` | — |
| الأمر | `CMD-ARL-ENABLE` | تمكين قاعدة التنبيه |
| السياسة | `POL-ARL-ENABLE` | Analyst lead / Manager؛ tenant match; target visible to subject |
| الحدث | `EVT-ARL-ENABLED` | يصل إلى: Alert evaluator (reload rules) |
| الكيان | `AGG-ALERT-RULE` | قاعدة التنبيه |
| الجدول | `intelligence.alert_rules` | الجدول الرئيسي لقاعدة التنبيه |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-RULE-SM، TST-SLC06-INVARIANTS | دورة حالات قاعدة التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-ARL-ENABLE -->

</details>

### 5.6 US-BC03-ARL-RETIRE — إحالة قاعدة التنبيه إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC03-ARL-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/alert-rules/{id}/actions/retire` | — |
| الأمر | `CMD-ARL-RETIRE` | إحالة قاعدة التنبيه إلى التقاعد |
| السياسة | `POL-ARL-RETIRE` | Analyst lead / Manager؛ tenant match; target visible to subject |
| الحدث | `EVT-ARL-RETIRED` | يصل إلى: Alert evaluator (reload rules) |
| الكيان | `AGG-ALERT-RULE` | قاعدة التنبيه |
| الجدول | `intelligence.alert_rules` | الجدول الرئيسي لقاعدة التنبيه |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-RULE-SM، TST-SLC06-INVARIANTS | دورة حالات قاعدة التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-ARL-RETIRE -->

</details>

### 5.7 US-DOM-ARL-DRY-RUN — تجربة قاعدة التنبيه على أحداث آخر يوم

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

<!-- BEGIN GENERATED: refs US-DOM-ARL-DRY-RUN -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `THR-S06-05` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. |
| حالة الاستخدام | UC-023 | Manage Alert |
<!-- END GENERATED: refs US-DOM-ARL-DRY-RUN -->

</details>

### 5.8 US-UI-SCR12-ALERT-RULE-EDITOR — تعريف شرط التنبيه ومعاينة حجمه قبل التفعيل

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

<!-- BEGIN GENERATED: refs US-UI-SCR12-ALERT-RULE-EDITOR -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-12 | شاشة إدارة الموقف وقواعد التنبيه |
| المصدر | `THR-S06-05` | — |
| المصدر | `situation-alerting-spec.md §3` | — |
| المتطلب | REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. |
| حالة الاستخدام | UC-023 | Manage Alert |
<!-- END GENERATED: refs US-UI-SCR12-ALERT-RULE-EDITOR -->

</details>

### 5.9 US-OPS-ALERT-STORM-LIMIT — حد معدل لكل قاعدة يمنع سيل التنبيهات

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

<!-- BEGIN GENERATED: refs US-OPS-ALERT-STORM-LIMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `THR-S06-06` | — |
| المصدر | `observability-slc06.md` | — |
<!-- END GENERATED: refs US-OPS-ALERT-STORM-LIMIT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. | `US-BC03-ARL-ACTIVATE`، `US-BC03-ARL-DEFINE`، `US-BC03-ARL-DISABLE`، `US-BC03-ARL-EDIT`، `US-BC03-ARL-ENABLE`، `US-BC03-ARL-RETIRE`، `US-DOM-ARL-DRY-RUN`، `US-UI-SCR12-ALERT-RULE-EDITOR` | TST-ALERT-RULE-SM، TST-ALERT-SM، TST-SLC06-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
