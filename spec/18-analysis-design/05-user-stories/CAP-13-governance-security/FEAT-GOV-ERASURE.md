---
id: FEAT-GOV-ERASURE
type: feature
title: "محو البيانات الشخصية"
status: DRAFT
version: "0.1"
capability: CAP-13.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# محو البيانات الشخصية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-GOV-ERASURE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-13 الحوكمة والأمن والامتثال |
| القدرة الفرعية | CAP-13.03 الخصوصية والاحتفاظ (R1) |
| الأدوار | السلطة القانونية والامتثال؛ مسؤول الإدارة؛ المدقِّق؛ النظام |
| الشاشات | SCR-70 الاحتفاظ والحجز القانوني والإتلاف والمحو |
| حالات الاستخدام | UC-103، UC-084 |
| القصص | 14: 10 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لمسؤول الخصوصية تسجيل طلب محو بيانات شخص يعتمده مرجع قانوني مستقل، ثم يمحوها من كل أجزاء المنصة مع إصدار شهادة دون فقدان حقائق التدقيق.

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
| QAS-PRV-001 | orders erasure of a data subject | operational & projections ≤ 24 h; backups unrecoverable immediately via key destruction |
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
| `US-BC01-PER-ERASE` | محو الشخص | أمر | مسودة |
| `US-BC08-ERS-APPROVE` | اعتماد طلب المحو | أمر | مسودة |
| `US-BC08-ERS-REGISTER` | تسجيل طلب المحو | أمر | مسودة |
| `US-BC08-ERS-REJECT` | رفض طلب المحو | أمر | مسودة |
| `US-BC08-Q-ERS-GET` | جلب: Request with scope counts, confirmations and certificate (no personal data) | جلب | مسودة |
| `US-BC08-S-ERASURE-REQUEST-01` | تلقائي: subject scope resolved (طلب المحو) | نظام | مسودة |
| `US-BC08-S-ERASURE-REQUEST-02` | تلقائي: hold matches subject (طلب المحو) | نظام | مسودة |
| `US-BC08-S-ERASURE-REQUEST-03` | تلقائي: hold released (طلب المحو) | نظام | مسودة |
| `US-BC08-S-ERASURE-REQUEST-04` | تلقائي: execution started (طلب المحو) | نظام | مسودة |
| `US-BC08-S-ERASURE-REQUEST-05` | تلقائي: all contexts confirmed (طلب المحو) | نظام | مسودة |
| `US-UI-SCR70-ERASURE-PROGRESS` | متابعة تأكيدات المحو وشهادته | واجهة | مسودة |
| `US-PLT-ERASURE-CONTEXT-PURGE` | إفراغ كل جزء نسخه الواضحة خلال يوم | منصة | مسودة |
| `US-PLT-ERASURE-KEY-SHRED` | محو البيانات الشخصية بإتلاف مفتاح صاحبها | منصة | مسودة |
| `US-OPS-ERASURE-DEADLINE-ALERT` | تنبيه عند تأخر تأكيد المحو | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-PER-ERASE — محو الشخص

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

<!-- BEGIN GENERATED: refs US-BC01-PER-ERASE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/persons/{id}/actions/erase` | — |
| الأمر | `CMD-PER-ERASE` | محو الشخص |
| السياسة | `POL-PER-ERASE` | Administrator with org scope ⊇ person's unit؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operati… |
| الحدث | `EVT-PER-ERASED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-PERSON` | الشخص |
| الجدول | `foundation.persons` | الجدول الرئيسي للشخص |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-PERSON-SM، TST-SLC01-INVARIANTS | دورة حالات الشخص، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-PER-ERASE -->

</details>

### 5.2 US-BC08-ERS-APPROVE — اعتماد طلب المحو

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

<!-- BEGIN GENERATED: refs US-BC08-ERS-APPROVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/erasure-requests/{id}/actions/approve` | — |
| الأمر | `CMD-ERS-APPROVE` | اعتماد طلب المحو |
| السياسة | `POL-ERS-APPROVE` | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject)؛ tenant match |
| الحدث | `EVT-ERS-APPROVED` | يصل إلى: Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| الكيان | `AGG-ERASURE-REQUEST` | طلب المحو |
| الجدول | `governance.erasure_requests` | الجدول الرئيسي لطلب المحو |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-ERASURE-REQUEST-SM | دورة حالات طلب المحو، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-ERS-APPROVE -->

</details>

### 5.3 US-BC08-ERS-REGISTER — تسجيل طلب المحو

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

<!-- BEGIN GENERATED: refs US-BC08-ERS-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/erasure-requests` | — |
| الأمر | `CMD-ERS-REGISTER` | تسجيل طلب المحو |
| السياسة | `POL-ERS-REGISTER` | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject)؛ tenant match |
| الحدث | `EVT-ERS-RECEIVED` | يصل إلى: Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| الكيان | `AGG-ERASURE-REQUEST` | طلب المحو |
| الجدول | `governance.erasure_requests` | الجدول الرئيسي لطلب المحو |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-ERASURE-REQUEST-SM | دورة حالات طلب المحو، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-ERS-REGISTER -->

</details>

### 5.4 US-BC08-ERS-REJECT — رفض طلب المحو

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

<!-- BEGIN GENERATED: refs US-BC08-ERS-REJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/erasure-requests/{id}/actions/reject` | — |
| الأمر | `CMD-ERS-REJECT` | رفض طلب المحو |
| السياسة | `POL-ERS-REJECT` | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject)؛ tenant match |
| الحدث | `EVT-ERS-REJECTED` | يصل إلى: Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| الكيان | `AGG-ERASURE-REQUEST` | طلب المحو |
| الجدول | `governance.erasure_requests` | الجدول الرئيسي لطلب المحو |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-ERASURE-REQUEST-SM | دورة حالات طلب المحو، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-ERS-REJECT -->

</details>

### 5.5 US-BC08-Q-ERS-GET — جلب: Request with scope counts, confirmations and certificate (no personal data)

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

<!-- BEGIN GENERATED: refs US-BC08-Q-ERS-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/governance/erasure-requests/{request_id}` | — |
| الاستعلام | `QRY-ERS-GET` | Request with scope counts, confirmations and certificate (no personal data) |
| السياسة | `POL-ERS-GET` | Legal, Auditor |
| الكيان | `AGG-ERASURE-REQUEST` | طلب المحو |
| الجدول | `governance.erasure_requests` | الجدول الرئيسي لطلب المحو |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-ERASURE-REQUEST-SM | دورة حالات طلب المحو، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-Q-ERS-GET -->

</details>

### 5.6 US-BC08-S-ERASURE-REQUEST-01 — تلقائي: subject scope resolved (طلب المحو)

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

<!-- BEGIN GENERATED: refs US-BC08-S-ERASURE-REQUEST-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:subject scope resolved` | subject keys located in BC01 (persons), BC02 (entities with personal_data claims) and BC05 (qualification rec… |
| الانتقال | RECEIVED ← SCOPED | — |
| الحدث | `EVT-ERS-SCOPED` | يصل إلى: Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| الكيان | `AGG-ERASURE-REQUEST` | طلب المحو |
| الجدول | `governance.erasure_requests` | الجدول الرئيسي لطلب المحو |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-ERASURE-REQUEST-SM | دورة حالات طلب المحو، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-S-ERASURE-REQUEST-01 -->

</details>

### 5.7 US-BC08-S-ERASURE-REQUEST-02 — تلقائي: hold matches subject (طلب المحو)

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

<!-- BEGIN GENERATED: refs US-BC08-S-ERASURE-REQUEST-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:hold matches subject` | HoldCheck positive |
| الانتقال | APPROVED ← BLOCKED_BY_HOLD | — |
| الحدث | `EVT-ERS-BLOCKED` | يصل إلى: Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| الكيان | `AGG-ERASURE-REQUEST` | طلب المحو |
| الجدول | `governance.erasure_requests` | الجدول الرئيسي لطلب المحو |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-ERASURE-REQUEST-SM | دورة حالات طلب المحو، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-S-ERASURE-REQUEST-02 -->

</details>

### 5.8 US-BC08-S-ERASURE-REQUEST-03 — تلقائي: hold released (طلب المحو)

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

<!-- BEGIN GENERATED: refs US-BC08-S-ERASURE-REQUEST-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:hold released` | HoldCheck negative |
| الانتقال | BLOCKED_BY_HOLD ← APPROVED | — |
| الحدث | `EVT-ERS-UNBLOCKED` | يصل إلى: Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| الكيان | `AGG-ERASURE-REQUEST` | طلب المحو |
| الجدول | `governance.erasure_requests` | الجدول الرئيسي لطلب المحو |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-ERASURE-REQUEST-SM | دورة حالات طلب المحو، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-S-ERASURE-REQUEST-03 -->

</details>

### 5.9 US-BC08-S-ERASURE-REQUEST-04 — تلقائي: execution started (طلب المحو)

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

<!-- BEGIN GENERATED: refs US-BC08-S-ERASURE-REQUEST-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:execution started` | subject DEKs destroyed; owners purge plaintext caches/projections; pseudonymous reference kept for audit facts |
| الانتقال | APPROVED ← EXECUTING | — |
| الحدث | `EVT-ERS-EXECUTING` | يصل إلى: Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| الكيان | `AGG-ERASURE-REQUEST` | طلب المحو |
| الجدول | `governance.erasure_requests` | الجدول الرئيسي لطلب المحو |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-ERASURE-REQUEST-SM | دورة حالات طلب المحو، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-S-ERASURE-REQUEST-04 -->

</details>

### 5.10 US-BC08-S-ERASURE-REQUEST-05 — تلقائي: all contexts confirmed (طلب المحو)

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

<!-- BEGIN GENERATED: refs US-BC08-S-ERASURE-REQUEST-05 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:all contexts confirmed` | confirmation from each owning context ≤ 24 h (QAS-PRV-001); certificate issued |
| الانتقال | EXECUTING ← COMPLETED | — |
| الحدث | `EVT-ERS-COMPLETED` | يصل إلى: Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| الكيان | `AGG-ERASURE-REQUEST` | طلب المحو |
| الجدول | `governance.erasure_requests` | الجدول الرئيسي لطلب المحو |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-ERASURE-REQUEST-SM | دورة حالات طلب المحو، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-S-ERASURE-REQUEST-05 -->

</details>

### 5.11 US-UI-SCR70-ERASURE-PROGRESS — متابعة تأكيدات المحو وشهادته

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

<!-- BEGIN GENERATED: refs US-UI-SCR70-ERASURE-PROGRESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الشاشة | SCR-70 | شاشة الاحتفاظ والحجز القانوني والإتلاف والمحو |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
<!-- END GENERATED: refs US-UI-SCR70-ERASURE-PROGRESS -->

</details>

### 5.12 US-PLT-ERASURE-CONTEXT-PURGE — إفراغ كل جزء نسخه الواضحة خلال يوم

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

<!-- BEGIN GENERATED: refs US-PLT-ERASURE-CONTEXT-PURGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PRV-001 | orders erasure of a data subject → operational & projections ≤ 24 h; backups unrecoverable immediately via ke… |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
<!-- END GENERATED: refs US-PLT-ERASURE-CONTEXT-PURGE -->

</details>

### 5.13 US-PLT-ERASURE-KEY-SHRED — محو البيانات الشخصية بإتلاف مفتاح صاحبها

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

<!-- BEGIN GENERATED: refs US-PLT-ERASURE-KEY-SHRED -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P08 | Erasure vs Immutability |
| المصدر | `17-security-design.md §6` | — |
| المتطلب | REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
<!-- END GENERATED: refs US-PLT-ERASURE-KEY-SHRED -->

</details>

### 5.14 US-OPS-ERASURE-DEADLINE-ALERT — تنبيه عند تأخر تأكيد المحو

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

<!-- BEGIN GENERATED: refs US-OPS-ERASURE-DEADLINE-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PRV-001 | orders erasure of a data subject → operational & projections ≤ 24 h; backups unrecoverable immediately via ke… |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-ERASURE-DEADLINE-ALERT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operationa… | `US-BC01-PER-ERASE`، `US-BC08-ERS-APPROVE`، `US-BC08-ERS-REGISTER`، `US-BC08-ERS-REJECT`، `US-BC08-Q-ERS-GET`، `US-BC08-S-ERASURE-REQUEST-01`، `US-BC08-S-ERASURE-REQUEST-02`، `US-BC08-S-ERASURE-REQUEST-03`، `US-BC08-S-ERASURE-REQUEST-04`، `US-BC08-S-ERASURE-REQUEST-05`، `US-PLT-ERASURE-CONTEXT-PURGE`، `US-PLT-ERASURE-KEY-SHRED`، `US-UI-SCR70-ERASURE-PROGRESS` | TST-ATTACHMENT-SM، TST-ERASURE-REQUEST-SM، TST-PERSON-SM، TST-SLC12A-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
