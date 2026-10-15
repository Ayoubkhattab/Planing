---
id: FEAT-PLT-EVENT-DELIVERY
type: feature
title: "موثوقية الأحداث والإسقاطات"
status: DRAFT
version: "0.1"
capability: CAP-14.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# موثوقية الأحداث والإسقاطات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-PLT-EVENT-DELIVERY |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-14 تشغيل المنصة |
| القدرة الفرعية | CAP-14.02 الاعتمادية والتعافي (R1) |
| الأدوار | مشغّل المنصة؛ النظام |
| الشاشات | SCR-71 حالة الإسقاطات (واجهة المشغل) |
| حالات الاستخدام | — |
| القصص | 14: 0 من المواصفة، و14 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضمن وصول كل حدث مرة واحدة فعليًا إلى الأجزاء المعنية، ويحجز الرسائل التي يتعذر معالجتها حتى تُعالج، فلا يضيع أي تحديث.

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
| QAS-REL-001 | event bus unavailable for 30 min | 0 lost events; 0 duplicates with effect |
| QAS-REL-003 | update the same object from the same version | 0 silent overwrites |
| QAS-SCAL-002 | event burst of 50,000/s for 60 s | 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PERF-005 ≤ 5 min after |
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
| `US-UI-SCR71-DEAD-LETTERS` | عرض الرسائل المحجوزة للمشغل دون محتواها | واجهة | مسودة |
| `US-PLT-EVENT-BACKPRESSURE` | تحمل اندفاع الأحداث دون فقد | منصة | مسودة |
| `US-PLT-EVENT-CIRCUIT-BREAKER` | إيقاف المستهلك مؤقتًا عند تعطل اعتمادياته | منصة | مسودة |
| `US-PLT-EVENT-DERIVED-KEYS` | مفتاح حتمي للأوامر الناتجة عن الأحداث | منصة | مسودة |
| `US-PLT-EVENT-INBOX-DEDUP` | معالجة الحدث المكرر مرة واحدة فقط | منصة | مسودة |
| `US-PLT-EVENT-OUTBOX` | نشر الحدث مع التغيير في معاملة واحدة | منصة | مسودة |
| `US-PLT-EVENT-PARKED-KEYS` | إيقاف رسائل المفتاح المتعثر وحده | منصة | مسودة |
| `US-PLT-EVENT-RETRY-DLQ` | إعادة المحاولة ثم حجز الرسالة الفاشلة | منصة | مسودة |
| `US-PLT-IDEMPOTENCY-KEY-STORE` | منع تنفيذ الأمر نفسه مرتين | منصة | مسودة |
| `US-PLT-UI-COMMAND-SUBMIT` | إرسال الأوامر من الواجهة دون تكرار | منصة | مسودة |
| `US-OPS-EVENT-DLQ-ALERT` | تنبيه لكل رسالة محجوزة حسب الطبقة | تشغيل | مسودة |
| `US-OPS-EVENT-DLQ-DISCARD` | تجاهل رسالة محجوزة بقرار مدقق | تشغيل | مسودة |
| `US-OPS-EVENT-DLQ-REPLAY` | إعادة تشغيل الرسائل المحجوزة بتدقيق | تشغيل | مسودة |
| `US-OPS-EVENT-PARTITIONS` | زيادة أقسام الأحداث دون فقد الترتيب | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-UI-SCR71-DEAD-LETTERS — عرض الرسائل المحجوزة للمشغل دون محتواها

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

<!-- BEGIN GENERATED: refs US-UI-SCR71-DEAD-LETTERS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §2` | — |
| القرار المعماري | ADR-P20 | Event Consumer Retry and Dead-Letter Policy |
| الشاشة | SCR-71 | شاشة حالة الإسقاطات (واجهة المشغل) |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR71-DEAD-LETTERS -->

</details>

### 5.2 US-PLT-EVENT-BACKPRESSURE — تحمل اندفاع الأحداث دون فقد

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

<!-- BEGIN GENERATED: refs US-PLT-EVENT-BACKPRESSURE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SCAL-002 | event burst of 50,000/s for 60 s → 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PER… |
<!-- END GENERATED: refs US-PLT-EVENT-BACKPRESSURE -->

</details>

### 5.3 US-PLT-EVENT-CIRCUIT-BREAKER — إيقاف المستهلك مؤقتًا عند تعطل اعتمادياته

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

<!-- BEGIN GENERATED: refs US-PLT-EVENT-CIRCUIT-BREAKER -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P20 | Event Consumer Retry and Dead-Letter Policy |
| المصدر | `23-crosscutting.md §6.1` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-EVENT-CIRCUIT-BREAKER -->

</details>

### 5.4 US-PLT-EVENT-DERIVED-KEYS — مفتاح حتمي للأوامر الناتجة عن الأحداث

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

<!-- BEGIN GENERATED: refs US-PLT-EVENT-DERIVED-KEYS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §3` | — |
| القرار المعماري | ADR-P17 | Internal Service Architecture (Hexagonal / Ports & Adapters) |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-EVENT-DERIVED-KEYS -->

</details>

### 5.5 US-PLT-EVENT-INBOX-DEDUP — معالجة الحدث المكرر مرة واحدة فقط

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

<!-- BEGIN GENERATED: refs US-PLT-EVENT-INBOX-DEDUP -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §3` | — |
| المتطلب | REQ-PLT-006 | The system shall publish domain events through a transactional outbox and shall process received events idemp… |
<!-- END GENERATED: refs US-PLT-EVENT-INBOX-DEDUP -->

</details>

### 5.6 US-PLT-EVENT-OUTBOX — نشر الحدث مع التغيير في معاملة واحدة

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

<!-- BEGIN GENERATED: refs US-PLT-EVENT-OUTBOX -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-REL-001 | event bus unavailable for 30 min → 0 lost events; 0 duplicates with effect |
| فحص البنية | FIT-04 | State change, audit record and outbox entry commit atomically |
| القرار المعماري | ADR-P02 | Persistence Style |
| المتطلب | REQ-PLT-006 | The system shall publish domain events through a transactional outbox and shall process received events idemp… |
<!-- END GENERATED: refs US-PLT-EVENT-OUTBOX -->

</details>

### 5.7 US-PLT-EVENT-PARKED-KEYS — إيقاف رسائل المفتاح المتعثر وحده

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

<!-- BEGIN GENERATED: refs US-PLT-EVENT-PARKED-KEYS -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P20 | Event Consumer Retry and Dead-Letter Policy |
| المصدر | `23-crosscutting.md §6.1` | — |
<!-- END GENERATED: refs US-PLT-EVENT-PARKED-KEYS -->

</details>

### 5.8 US-PLT-EVENT-RETRY-DLQ — إعادة المحاولة ثم حجز الرسالة الفاشلة

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

<!-- BEGIN GENERATED: refs US-PLT-EVENT-RETRY-DLQ -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P20 | Event Consumer Retry and Dead-Letter Policy |
| المصدر | `23-crosscutting.md §6.1` | — |
<!-- END GENERATED: refs US-PLT-EVENT-RETRY-DLQ -->

</details>

### 5.9 US-PLT-IDEMPOTENCY-KEY-STORE — منع تنفيذ الأمر نفسه مرتين

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

<!-- BEGIN GENERATED: refs US-PLT-IDEMPOTENCY-KEY-STORE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §3` | — |
| الجودة | QAS-REL-003 | update the same object from the same version → 0 silent overwrites |
<!-- END GENERATED: refs US-PLT-IDEMPOTENCY-KEY-STORE -->

</details>

### 5.10 US-PLT-UI-COMMAND-SUBMIT — إرسال الأوامر من الواجهة دون تكرار

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

<!-- BEGIN GENERATED: refs US-PLT-UI-COMMAND-SUBMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §6.1` | — |
| المصدر | `21-ui-design.md §6.2` | — |
| الجودة | QAS-REL-003 | update the same object from the same version → 0 silent overwrites |
<!-- END GENERATED: refs US-PLT-UI-COMMAND-SUBMIT -->

</details>

### 5.11 US-OPS-EVENT-DLQ-ALERT — تنبيه لكل رسالة محجوزة حسب الطبقة

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

<!-- BEGIN GENERATED: refs US-OPS-EVENT-DLQ-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P20 | Event Consumer Retry and Dead-Letter Policy |
| المصدر | `23-crosscutting.md §6.1` | — |
<!-- END GENERATED: refs US-OPS-EVENT-DLQ-ALERT -->

</details>

### 5.12 US-OPS-EVENT-DLQ-DISCARD — تجاهل رسالة محجوزة بقرار مدقق

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

<!-- BEGIN GENERATED: refs US-OPS-EVENT-DLQ-DISCARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P20 | Event Consumer Retry and Dead-Letter Policy |
| المصدر | `23-crosscutting.md §6.1` | — |
<!-- END GENERATED: refs US-OPS-EVENT-DLQ-DISCARD -->

</details>

### 5.13 US-OPS-EVENT-DLQ-REPLAY — إعادة تشغيل الرسائل المحجوزة بتدقيق

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

<!-- BEGIN GENERATED: refs US-OPS-EVENT-DLQ-REPLAY -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P20 | Event Consumer Retry and Dead-Letter Policy |
| المصدر | `22-deployment-design.md §6` | — |
<!-- END GENERATED: refs US-OPS-EVENT-DLQ-REPLAY -->

</details>

### 5.14 US-OPS-EVENT-PARTITIONS — زيادة أقسام الأحداث دون فقد الترتيب

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

<!-- BEGIN GENERATED: refs US-OPS-EVENT-PARTITIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §6` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-EVENT-PARTITIONS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-PLT-006 | The system shall publish domain events through a transactional outbox and shall process received events idemp… | `US-PLT-EVENT-INBOX-DEDUP`، `US-PLT-EVENT-OUTBOX` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
