---
id: FEAT-GOV-AUDIT-CAPTURE
type: feature
title: "التسجيل التلقائي للعمليات"
status: DRAFT
version: "0.2"
capability: CAP-13.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv, 18-analysis-design/17-security-design.md, 09-reliability/degradation-slc01.md, 09-reliability/observability-slc01.md, 02-requirements/requirements.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# التسجيل التلقائي للعمليات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-GOV-AUDIT-CAPTURE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-13 الحوكمة والأمن والامتثال |
| القدرة الفرعية | CAP-13.02 التدقيق (R1) |
| الأدوار | النظام |
| الشاشات | — |
| حالات الاستخدام | UC-087 |
| القصص | 6: 0 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضمن تسجيل كل تغيير وكل اطلاع على بيانات حساسة تلقائيًا مع الفاعل والغرض وقرار الوصول، دون أن يتمكن أحد من تعديل السجل أو حذفه.

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
| QAS-AUD-001 | executes a state-changing command | 100 % of commands audited with all fields |
| QAS-SEC-006 | modifies an audit record in storage | detected by next integrity check (≤ 24 h) |
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
| `US-PLT-AUDIT-ATOMIC-WRITE` | سجل تدقيق واحد مع كل تغيير | منصة | مسودة |
| `US-PLT-AUDIT-BUFFER-FAILCLOSED` | الاستمرار عند تعطل مخزن التدقيق ثم الرفض | منصة | مسودة |
| `US-PLT-AUDIT-HASH-CHAIN` | سلسلة لا تقبل التعديل لسجلات التدقيق | منصة | مسودة |
| `US-PLT-AUDIT-SENSITIVE-READS` | تدقيق قراءة البيانات فوق عتبة المستأجر | منصة | مسودة |
| `US-OPS-AUDIT-DAILY-VERIFY` | تحقق يومي من سلاسل التدقيق واكتمالها | تشغيل | مسودة |
| `US-OPS-AUDIT-LAG-ALERT` | تنبيه عند تأخر شحن سجلات التدقيق | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-PLT-AUDIT-ATOMIC-WRITE — سجل تدقيق واحد مع كل تغيير

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

<!-- BEGIN GENERATED: refs US-PLT-AUDIT-ATOMIC-WRITE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AUD-001 | executes a state-changing command → 100 % of commands audited with all fields |
| فحص البنية | FIT-04 | State change, audit record and outbox entry commit atomically |
| المتطلب | REQ-FND-015 | The system shall write an audit record for every state-changing command and for every read of data classified… |
| حالة الاستخدام | UC-087 | Review Audit Trail |
<!-- END GENERATED: refs US-PLT-AUDIT-ATOMIC-WRITE -->

</details>

### 5.2 US-PLT-AUDIT-BUFFER-FAILCLOSED — الاستمرار عند تعطل مخزن التدقيق ثم الرفض

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

<!-- BEGIN GENERATED: refs US-PLT-AUDIT-BUFFER-FAILCLOSED -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §7` | — |
| المصدر | `09-reliability/degradation-slc01.md §matrix` | — |
<!-- END GENERATED: refs US-PLT-AUDIT-BUFFER-FAILCLOSED -->

</details>

### 5.3 US-PLT-AUDIT-HASH-CHAIN — سلسلة لا تقبل التعديل لسجلات التدقيق

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

<!-- BEGIN GENERATED: refs US-PLT-AUDIT-HASH-CHAIN -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §7` | — |
| المتطلب | REQ-FND-016 | The system shall keep audit records append-only and tamper-evident. |
| حالة الاستخدام | UC-087 | Review Audit Trail |
<!-- END GENERATED: refs US-PLT-AUDIT-HASH-CHAIN -->

</details>

### 5.4 US-PLT-AUDIT-SENSITIVE-READS — تدقيق قراءة البيانات فوق عتبة المستأجر

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

<!-- BEGIN GENERATED: refs US-PLT-AUDIT-SENSITIVE-READS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §4` | — |
| المصدر | `17-security-design.md §7` | — |
| المتطلب | REQ-FND-015 | The system shall write an audit record for every state-changing command and for every read of data classified… |
| حالة الاستخدام | UC-087 | Review Audit Trail |
<!-- END GENERATED: refs US-PLT-AUDIT-SENSITIVE-READS -->

</details>

### 5.5 US-OPS-AUDIT-DAILY-VERIFY — تحقق يومي من سلاسل التدقيق واكتمالها

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-AUDIT-DAILY-VERIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-006 | modifies an audit record in storage → detected by next integrity check (≤ 24 h) |
| المصدر | `17-security-design.md §6.1` | — |
| المتطلب | REQ-FND-016 | The system shall keep audit records append-only and tamper-evident. |
| حالة الاستخدام | UC-087 | Review Audit Trail |
<!-- END GENERATED: refs US-OPS-AUDIT-DAILY-VERIFY -->

</details>

### 5.6 US-OPS-AUDIT-LAG-ALERT — تنبيه عند تأخر شحن سجلات التدقيق

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

<!-- BEGIN GENERATED: refs US-OPS-AUDIT-LAG-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/observability-slc01.md §signals` | — |
<!-- END GENERATED: refs US-OPS-AUDIT-LAG-ALERT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-015 | The system shall write an audit record for every state-changing command and for every read of data classified… | `US-PLT-AUDIT-ATOMIC-WRITE`، `US-PLT-AUDIT-SENSITIVE-READS` | TST-SLC01-INVARIANTS |
| REQ-FND-016 | The system shall keep audit records append-only and tamper-evident. | `US-OPS-AUDIT-DAILY-VERIFY`، `US-PLT-AUDIT-HASH-CHAIN` | TST-SLC01-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
