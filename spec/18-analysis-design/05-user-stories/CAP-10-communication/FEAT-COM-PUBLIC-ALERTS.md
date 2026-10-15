---
id: FEAT-COM-PUBLIC-ALERTS
type: feature
title: "رسائل الإنذار العام"
status: DRAFT
version: "0.1"
capability: CAP-10.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# رسائل الإنذار العام

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COM-PUBLIC-ALERTS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-10 الاتصال والمنتجات |
| القدرة الفرعية | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) |
| الأدوار | ضابط المناوبة؛ المشغِّل؛ صاحب السلطة أو المعتمِد الثاني؛ المدقِّق؛ النظام |
| الشاشات | SCR-14 رسائل الإنذار العام (CAP) |
| حالات الاستخدام | UC-023 |
| القصص | 10: 6 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعد ضابط المناوبة رسالة إنذار عامة بالمعيار الدولي ويطلقها صاحب السلطة إلى الجهات الخارجية مع متابعة وصولها.

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
| `US-BC03-CAP-CANCEL` | إلغاء رسالة CAP الصادرة | أمر | مسودة |
| `US-BC03-CAP-PREPARE` | إعداد رسالة CAP الصادرة | أمر | مسودة |
| `US-BC03-CAP-RELEASE` | تحرير رسالة CAP الصادرة | أمر | مسودة |
| `US-BC03-CAP-RETRY` | إعادة محاولة رسالة CAP الصادرة | أمر | مسودة |
| `US-BC03-Q-CAP-LIST` | جلب: Outbound CAP messages by state | جلب | مسودة |
| `US-BC03-S-CAP-MESSAGE-01` | تلقائي: delivery failed after retries (رسالة CAP الصادرة) | نظام | مسودة |
| `US-UI-SCR14-RELEASE-REVIEW` | معاينة رسالة الإنذار قبل إطلاقها وتتبع وصولها | واجهة | مسودة |
| `US-INT-CAP-INBOUND` | استقبال رسائل الإنذار من الجهات الأخرى | تكامل | مسودة |
| `US-INT-CAP-OUTBOUND` | إرسال رسالة الإنذار العام وتسجيل إقرارها | تكامل | مسودة |
| `US-OPS-CAP-ENDPOINT` | اعتماد منفذ الإنذار الخارجي ومراقبته | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-CAP-CANCEL — إلغاء رسالة CAP الصادرة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC03-CAP-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/cap-messages/{id}/actions/cancel` | — |
| الأمر | `CMD-CAP-CANCEL` | إلغاء رسالة CAP الصادرة |
| السياسة | `POL-CAP-CANCEL` | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)؛ tenant mat… |
| الحدث | `EVT-CAP-CANCELLED` | يصل إلى: CAP gateway; Audit |
| الكيان | `AGG-CAP-MESSAGE` | رسالة CAP الصادرة |
| الجدول | `intelligence.cap_messages` | الجدول الرئيسي لرسالة CAP الصادرة |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-CAP-MESSAGE-SM، TST-SLC16-INVARIANTS | دورة حالات رسالة CAP الصادرة، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC03-CAP-CANCEL -->

</details>

### 5.2 US-BC03-CAP-PREPARE — إعداد رسالة CAP الصادرة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC03-CAP-PREPARE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/cap-messages` | — |
| الأمر | `CMD-CAP-PREPARE` | إعداد رسالة CAP الصادرة |
| السياسة | `POL-CAP-PREPARE` | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)؛ tenant mat… |
| الحدث | `EVT-CAP-PREPARED` | يصل إلى: CAP gateway; Audit |
| الكيان | `AGG-CAP-MESSAGE` | رسالة CAP الصادرة |
| الجدول | `intelligence.cap_messages` | الجدول الرئيسي لرسالة CAP الصادرة |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-CAP-MESSAGE-SM، TST-SLC16-INVARIANTS | دورة حالات رسالة CAP الصادرة، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC03-CAP-PREPARE -->

</details>

### 5.3 US-BC03-CAP-RELEASE — تحرير رسالة CAP الصادرة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC03-CAP-RELEASE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/cap-messages/{id}/actions/release` | — |
| الأمر | `CMD-CAP-RELEASE` | تحرير رسالة CAP الصادرة |
| السياسة | `POL-CAP-RELEASE` | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)؛ tenant mat… |
| الحدث | `EVT-CAP-SENT` | يصل إلى: CAP gateway; Audit |
| الكيان | `AGG-CAP-MESSAGE` | رسالة CAP الصادرة |
| الجدول | `intelligence.cap_messages` | الجدول الرئيسي لرسالة CAP الصادرة |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-CAP-MESSAGE-SM، TST-SLC16-INVARIANTS | دورة حالات رسالة CAP الصادرة، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC03-CAP-RELEASE -->

</details>

### 5.4 US-BC03-CAP-RETRY — إعادة محاولة رسالة CAP الصادرة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC03-CAP-RETRY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/cap-messages/{id}/actions/retry` | — |
| الأمر | `CMD-CAP-RETRY` | إعادة محاولة رسالة CAP الصادرة |
| السياسة | `POL-CAP-RETRY` | alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)؛ tenant mat… |
| الحدث | `EVT-CAP-RETRY` | يصل إلى: CAP gateway; Audit |
| الكيان | `AGG-CAP-MESSAGE` | رسالة CAP الصادرة |
| الجدول | `intelligence.cap_messages` | الجدول الرئيسي لرسالة CAP الصادرة |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-CAP-MESSAGE-SM، TST-SLC16-INVARIANTS | دورة حالات رسالة CAP الصادرة، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC03-CAP-RETRY -->

</details>

### 5.5 US-BC03-Q-CAP-LIST — جلب: Outbound CAP messages by state

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC03-Q-CAP-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/cap-messages` | — |
| الاستعلام | `QRY-CAP-LIST` | Outbound CAP messages by state |
| السياسة | `POL-CAP-LIST` | release authority, Auditor |
| الكيان | `AGG-CAP-MESSAGE` | رسالة CAP الصادرة |
| الجدول | `intelligence.cap_messages` | الجدول الرئيسي لرسالة CAP الصادرة |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-CAP-MESSAGE-SM، TST-SLC16-INVARIANTS | دورة حالات رسالة CAP الصادرة، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC03-Q-CAP-LIST -->

</details>

### 5.6 US-BC03-S-CAP-MESSAGE-01 — تلقائي: delivery failed after retries (رسالة CAP الصادرة)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC03-S-CAP-MESSAGE-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:delivery failed after retries` | 5 retries with backoff |
| الانتقال | PREPARED ← FAILED | — |
| الحدث | `EVT-CAP-FAILED` | يصل إلى: CAP gateway; Audit |
| الكيان | `AGG-CAP-MESSAGE` | رسالة CAP الصادرة |
| الجدول | `intelligence.cap_messages` | الجدول الرئيسي لرسالة CAP الصادرة |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). |
| حالة الاستخدام | UC-023 | Manage Alert |
| الاختبار | TST-CAP-MESSAGE-SM، TST-SLC16-INVARIANTS | دورة حالات رسالة CAP الصادرة، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC03-S-CAP-MESSAGE-01 -->

</details>

### 5.7 US-UI-SCR14-RELEASE-REVIEW — معاينة رسالة الإنذار قبل إطلاقها وتتبع وصولها

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

<!-- BEGIN GENERATED: refs US-UI-SCR14-RELEASE-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-14 | شاشة رسائل الإنذار العام (CAP) |
| المصدر | `20-integration-design.md §5` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). |
| حالة الاستخدام | UC-023 | Manage Alert |
<!-- END GENERATED: refs US-UI-SCR14-RELEASE-REVIEW -->

</details>

### 5.8 US-INT-CAP-INBOUND — استقبال رسائل الإنذار من الجهات الأخرى

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-CAP-INBOUND -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §2` | — |
| المتطلب | REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). |
| حالة الاستخدام | UC-023 | Manage Alert |
<!-- END GENERATED: refs US-INT-CAP-INBOUND -->

</details>

### 5.9 US-INT-CAP-OUTBOUND — إرسال رسالة الإنذار العام وتسجيل إقرارها

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-CAP-OUTBOUND -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §5` | — |
| المتطلب | REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). |
| حالة الاستخدام | UC-023 | Manage Alert |
<!-- END GENERATED: refs US-INT-CAP-OUTBOUND -->

</details>

### 5.10 US-OPS-CAP-ENDPOINT — اعتماد منفذ الإنذار الخارجي ومراقبته

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

<!-- BEGIN GENERATED: refs US-OPS-CAP-ENDPOINT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). |
| حالة الاستخدام | UC-023 | Manage Alert |
<!-- END GENERATED: refs US-OPS-CAP-ENDPOINT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). | `US-BC03-CAP-CANCEL`، `US-BC03-CAP-PREPARE`، `US-BC03-CAP-RELEASE`، `US-BC03-CAP-RETRY`، `US-BC03-Q-CAP-LIST`، `US-BC03-S-CAP-MESSAGE-01`، `US-INT-CAP-INBOUND`، `US-INT-CAP-OUTBOUND`، `US-OPS-CAP-ENDPOINT`، `US-UI-SCR14-RELEASE-REVIEW` | TST-CAP-MESSAGE-SM، TST-SLC16-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
