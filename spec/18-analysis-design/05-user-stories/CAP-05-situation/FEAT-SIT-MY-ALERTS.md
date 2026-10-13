---
id: FEAT-SIT-MY-ALERTS
type: feature
title: "تنبيهاتي"
status: DRAFT
version: "0.1"
capability: CAP-05.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تنبيهاتي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-SIT-MY-ALERTS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-05 الوعي بالموقف |
| القدرة الفرعية | CAP-05.02 المراقبة والتنبيه (R1) |
| الأدوار | مستلم التنبيه؛ النظام |
| الشاشات | SCR-04 تنبيهاتي، SCR-03 صندوق الوارد |
| حالات الاستخدام | UC-023 |
| القصص | 13: 8 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يصل المستخدم تنبيه فوري حين يقع ما يهمه فيقرّ به أو يحله أو يصرفه بسبب ويُصعَّد إن أهمله.

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
| QAS-SCAL-002 | event burst of 50,000/s for 60 s | 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PERF-005 ≤ 5 min after |
| QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance | 0 leakage in inference suite (counts, facets, ordering, timing, errors) |
| QAS-SEC-012 | user not cleared for an alert's label | receives no alert, notification, push or count change |
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
| `US-BC03-ALR-ACKNOWLEDGE` | الإقرار باستلام التنبيه | أمر | مسودة |
| `US-BC03-ALR-DISMISS` | صرف النظر عن التنبيه | أمر | مسودة |
| `US-BC03-ALR-RESOLVE` | حل التنبيه | أمر | مسودة |
| `US-BC03-Q-ALR-LIST` | جلب: My alerts by state, severity, situation | جلب | مسودة |
| `US-BC03-S-ALERT-01` | تلقائي: rule condition met (التنبيه) | نظام | مسودة |
| `US-BC03-S-ALERT-02` | تلقائي: condition met again within dedupe window (التنبيه) | نظام | مسودة |
| `US-BC03-S-ALERT-03` | تلقائي: unacknowledged beyond escalation delay (التنبيه) | نظام | مسودة |
| `US-BC03-S-ALERT-04` | تلقائي: condition cleared and rule auto_resolve (التنبيه) | نظام | مسودة |
| `US-UI-SCR04-ALERT-ACTIONS` | أفعال التنبيه حسب حالته مع سبب الصرف | واجهة | مسودة |
| `US-UI-SCR04-ALERT-LIST` | تنبيهاتي مرتبة بالخطورة والحالة وتصل فورًا | واجهة | مسودة |
| `US-PLT-ALERT-CLEARED-ONLY` | وصول التنبيه للمصرح لهم فقط دون أي أثر | منصة | مسودة |
| `US-PLT-ALERT-LATENCY` | إطلاق التنبيه الحرج خلال خمس ثوان | منصة | مسودة |
| `US-OPS-ALERT-LATENCY-WATCH` | مراقبة تأخر التنبيهات الحرجة والتصعيد | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-ALR-ACKNOWLEDGE — الإقرار باستلام التنبيه

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

<!-- BEGIN GENERATED: refs US-BC03-ALR-ACKNOWLEDGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/alerts/{id}/actions/acknowledge` | — |
| الأمر | `CMD-ALR-ACKNOWLEDGE` | الإقرار باستلام التنبيه |
| السياسة | `POL-ALR-ACKNOWLEDGE` | recipient؛ tenant match; target visible to subject |
| الحدث | `EVT-ALR-ACKNOWLEDGED` | يصل إلى: Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| الكيان | `AGG-ALERT` | التنبيه |
| الجدول | `intelligence.alerts` | الجدول الرئيسي للتنبيه |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-SIT-004، REQ-SIT-005، REQ-SIT-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-SM، TST-SLC06-INVARIANTS | دورة حالات التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-ALR-ACKNOWLEDGE -->

</details>

### 5.2 US-BC03-ALR-DISMISS — صرف النظر عن التنبيه

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

<!-- BEGIN GENERATED: refs US-BC03-ALR-DISMISS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/alerts/{id}/actions/dismiss` | — |
| الأمر | `CMD-ALR-DISMISS` | صرف النظر عن التنبيه |
| السياسة | `POL-ALR-DISMISS` | recipient؛ tenant match; target visible to subject |
| الحدث | `EVT-ALR-DISMISSED` | يصل إلى: Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| الكيان | `AGG-ALERT` | التنبيه |
| الجدول | `intelligence.alerts` | الجدول الرئيسي للتنبيه |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-SIT-004، REQ-SIT-005، REQ-SIT-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-SM، TST-SLC06-INVARIANTS | دورة حالات التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-ALR-DISMISS -->

</details>

### 5.3 US-BC03-ALR-RESOLVE — حل التنبيه

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

<!-- BEGIN GENERATED: refs US-BC03-ALR-RESOLVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/alerts/{id}/actions/resolve` | — |
| الأمر | `CMD-ALR-RESOLVE` | حل التنبيه |
| السياسة | `POL-ALR-RESOLVE` | recipient؛ tenant match; target visible to subject |
| الحدث | `EVT-ALR-RESOLVED` | يصل إلى: Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| الكيان | `AGG-ALERT` | التنبيه |
| الجدول | `intelligence.alerts` | الجدول الرئيسي للتنبيه |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-SIT-004، REQ-SIT-005، REQ-SIT-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-SM، TST-SLC06-INVARIANTS | دورة حالات التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-ALR-RESOLVE -->

</details>

### 5.4 US-BC03-Q-ALR-LIST — جلب: My alerts by state, severity, situation

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

<!-- BEGIN GENERATED: refs US-BC03-Q-ALR-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/alerts` | — |
| الاستعلام | `QRY-ALR-LIST` | My alerts by state, severity, situation |
| السياسة | `POL-ALR-LIST` | recipient; label rule |
| الكيان | `AGG-ALERT` | التنبيه |
| الجدول | `intelligence.alerts` | الجدول الرئيسي للتنبيه |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-005 | The system shall manage alerts through the states RAISED, ACKNOWLEDGED, RESOLVED and DISMISSED, requiring a r… |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-SM، TST-SLC06-INVARIANTS | دورة حالات التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-Q-ALR-LIST -->

</details>

### 5.5 US-BC03-S-ALERT-01 — تلقائي: rule condition met (التنبيه)

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

<!-- BEGIN GENERATED: refs US-BC03-S-ALERT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:rule condition met` | no non-terminal alert for (rule, subject) inside dedupe window; label = max(rule label, triggering object lab… |
| الانتقال | ∅ ← RAISED | — |
| الحدث | `EVT-ALR-RAISED` | يصل إلى: Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| الكيان | `AGG-ALERT` | التنبيه |
| الجدول | `intelligence.alerts` | الجدول الرئيسي للتنبيه |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-SIT-004، REQ-SIT-005، REQ-SIT-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-SM، TST-SLC06-INVARIANTS | دورة حالات التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-S-ALERT-01 -->

</details>

### 5.6 US-BC03-S-ALERT-02 — تلقائي: condition met again within dedupe window (التنبيه)

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

<!-- BEGIN GENERATED: refs US-BC03-S-ALERT-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:condition met again within dedupe window` | occurrence counter + last_occurrence updated |
| الانتقال | RAISED, ACKNOWLEDGED ← (بلا تغيير) | — |
| الحدث | `EVT-ALR-REPEATED` | يصل إلى: Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| الكيان | `AGG-ALERT` | التنبيه |
| الجدول | `intelligence.alerts` | الجدول الرئيسي للتنبيه |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-SIT-004، REQ-SIT-005، REQ-SIT-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-SM، TST-SLC06-INVARIANTS | دورة حالات التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-S-ALERT-02 -->

</details>

### 5.7 US-BC03-S-ALERT-03 — تلقائي: unacknowledged beyond escalation delay (التنبيه)

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

<!-- BEGIN GENERATED: refs US-BC03-S-ALERT-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:unacknowledged beyond escalation delay` | escalates to the rule's escalation recipients |
| الانتقال | RAISED ← (بلا تغيير) | — |
| الحدث | `EVT-ALR-ESCALATED` | يصل إلى: Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| الكيان | `AGG-ALERT` | التنبيه |
| الجدول | `intelligence.alerts` | الجدول الرئيسي للتنبيه |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-SIT-004، REQ-SIT-005، REQ-SIT-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-SM، TST-SLC06-INVARIANTS | دورة حالات التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-S-ALERT-03 -->

</details>

### 5.8 US-BC03-S-ALERT-04 — تلقائي: condition cleared and rule auto_resolve (التنبيه)

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

<!-- BEGIN GENERATED: refs US-BC03-S-ALERT-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:condition cleared and rule auto_resolve` | system |
| الانتقال | RAISED, ACKNOWLEDGED ← RESOLVED | — |
| الحدث | `EVT-ALR-RESOLVED` | يصل إلى: Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| الكيان | `AGG-ALERT` | التنبيه |
| الجدول | `intelligence.alerts` | الجدول الرئيسي للتنبيه |
| وحدة النشر | DU-06 | — |
| المتطلبات | REQ-SIT-004، REQ-SIT-005، REQ-SIT-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-ALERT-SM، TST-SLC06-INVARIANTS | دورة حالات التنبيه، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-S-ALERT-04 -->

</details>

### 5.9 US-UI-SCR04-ALERT-ACTIONS — أفعال التنبيه حسب حالته مع سبب الصرف

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

<!-- BEGIN GENERATED: refs US-UI-SCR04-ALERT-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-04 | شاشة تنبيهاتي |
| المصدر | `21-ui-design.md §6.3` | — |
| المتطلب | REQ-SIT-005 | The system shall manage alerts through the states RAISED, ACKNOWLEDGED, RESOLVED and DISMISSED, requiring a r… |
| حالة الاستخدام | UC-023 | Manage Alert |
<!-- END GENERATED: refs US-UI-SCR04-ALERT-ACTIONS -->

</details>

### 5.10 US-UI-SCR04-ALERT-LIST — تنبيهاتي مرتبة بالخطورة والحالة وتصل فورًا

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

<!-- BEGIN GENERATED: refs US-UI-SCR04-ALERT-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-04 | شاشة تنبيهاتي |
| حالة الاستخدام | UC-023 | Manage Alert |
| الجودة | QAS-PERF-005 | reports a value that meets a critical alert rule → end-to-end p95 ≤ 5 s |
<!-- END GENERATED: refs US-UI-SCR04-ALERT-LIST -->

</details>

### 5.11 US-PLT-ALERT-CLEARED-ONLY — وصول التنبيه للمصرح لهم فقط دون أي أثر

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-ALERT-CLEARED-ONLY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-012 | user not cleared for an alert's label → receives no alert, notification, push or count change |
| المصدر | `THR-S06-01` | — |
| المصدر | `situation-alerting-spec.md §3` | — |
| المتطلب | REQ-SIT-006 | If a user is not authorized for the object that triggered an alert, then the system shall not reveal that obj… |
<!-- END GENERATED: refs US-PLT-ALERT-CLEARED-ONLY -->

</details>

### 5.12 US-PLT-ALERT-LATENCY — إطلاق التنبيه الحرج خلال خمس ثوان

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-ALERT-LATENCY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-005 | reports a value that meets a critical alert rule → end-to-end p95 ≤ 5 s |
| الجودة | QAS-SCAL-002 | event burst of 50,000/s for 60 s → 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PER… |
| المصدر | `situation-alerting-spec.md §3` | — |
| المتطلب | REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. |
| حالة الاستخدام | UC-023 | Manage Alert |
<!-- END GENERATED: refs US-PLT-ALERT-LATENCY -->

</details>

### 5.13 US-OPS-ALERT-LATENCY-WATCH — مراقبة تأخر التنبيهات الحرجة والتصعيد

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

<!-- BEGIN GENERATED: refs US-OPS-ALERT-LATENCY-WATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc06.md` | — |
| المصدر | `FM-S06-01` | — |
| المصدر | `FM-S06-05` | — |
<!-- END GENERATED: refs US-OPS-ALERT-LATENCY-WATCH -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. | `US-BC03-ALR-ACKNOWLEDGE`، `US-BC03-ALR-DISMISS`، `US-BC03-ALR-RESOLVE`، `US-BC03-S-ALERT-01`، `US-BC03-S-ALERT-02`، `US-BC03-S-ALERT-03`، `US-BC03-S-ALERT-04`، `US-PLT-ALERT-LATENCY` | TST-ALERT-RULE-SM، TST-ALERT-SM، TST-SLC06-INVARIANTS |
| REQ-SIT-005 | The system shall manage alerts through the states RAISED, ACKNOWLEDGED, RESOLVED and DISMISSED, requiring a r… | `US-BC03-ALR-ACKNOWLEDGE`، `US-BC03-ALR-DISMISS`، `US-BC03-ALR-RESOLVE`، `US-BC03-Q-ALR-LIST`، `US-BC03-S-ALERT-01`، `US-BC03-S-ALERT-02`، `US-BC03-S-ALERT-03`، `US-BC03-S-ALERT-04`، `US-UI-SCR04-ALERT-ACTIONS` | TST-ALERT-SM، TST-SLC06-INVARIANTS |
| REQ-SIT-006 | If a user is not authorized for the object that triggered an alert, then the system shall not reveal that obj… | `US-BC03-ALR-ACKNOWLEDGE`، `US-BC03-ALR-DISMISS`، `US-BC03-ALR-RESOLVE`، `US-BC03-S-ALERT-01`، `US-BC03-S-ALERT-02`، `US-BC03-S-ALERT-03`، `US-BC03-S-ALERT-04`، `US-PLT-ALERT-CLEARED-ONLY` | TST-ALERT-SM، TST-SLC06-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
