---
id: FEAT-RES-QUALIFICATIONS
type: feature
title: "سجلات تأهيل الأفراد"
status: DRAFT
version: "0.1"
capability: CAP-08.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# سجلات تأهيل الأفراد

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-QUALIFICATIONS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.04 الكفاءة والأهلية (R1 (الأهلية فقط)) |
| الأدوار | مدير الموارد؛ مدير التدريب؛ المدير؛ الفرد نفسه؛ النظام |
| الشاشات | SCR-42 التأهيل والأهلية |
| حالات الاستخدام | UC-102 |
| القصص | 11: 7 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يحفظ مدير الموارد أو مدير التدريب مؤهلات كل فرد وشهاداته وصلاحيتها، وتنتهي تلقائيًا عند انقضاء مدتها.

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
| `US-BC05-QUAL-RECORD` | تسجيل سجل التأهيل | أمر | مسودة |
| `US-BC05-QUAL-REINSTATE` | إعادة سجل التأهيل إلى السريان | أمر | مسودة |
| `US-BC05-QUAL-RENEW` | تجديد سجل التأهيل | أمر | مسودة |
| `US-BC05-QUAL-REVOKE` | سحب سجل التأهيل | أمر | مسودة |
| `US-BC05-QUAL-SUSPEND` | تعليق سجل التأهيل | أمر | مسودة |
| `US-BC05-Q-QUAL-LIST` | جلب: Qualification records as of t | جلب | مسودة |
| `US-BC05-S-QUALIFICATION-RECORD-01` | تلقائي: valid_to reached (سجل التأهيل) | نظام | مسودة |
| `US-DOM-QUAL-EXPIRY-NOTICE` | تنبيه الفرد ومديره قبل انتهاء المؤهل | نظام | مسودة |
| `US-UI-SCR42-MY-QUALS` | الفرد يرى مؤهلاته وشهاداته | واجهة | مسودة |
| `US-UI-SCR42-QUAL-LIST` | مؤهلات الفرد وصلاحيتها في تاريخ معين | واجهة | مسودة |
| `US-INT-HR-QUALIFICATIONS` | استيراد المؤهلات من نظام الموارد البشرية | تكامل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-QUAL-RECORD — تسجيل سجل التأهيل

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

<!-- BEGIN GENERATED: refs US-BC05-QUAL-RECORD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/qualification-records` | — |
| الأمر | `CMD-QUAL-RECORD` | تسجيل سجل التأهيل |
| السياسة | `POL-QUAL-RECORD` | Resource Manager / Training Manager؛ tenant match; task visible; org scope |
| الحدث | `EVT-QUAL-RECORDED` | يصل إلى: Eligibility cache invalidation; Task assignment re-check report |
| الكيان | `AGG-QUALIFICATION-RECORD` | سجل التأهيل |
| الجدول | `readiness.qualification_records` | الجدول الرئيسي لسجل التأهيل |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RDY-001، REQ-RDY-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-QUALIFICATION-RECORD-SM، TST-SLC03-INVARIANTS | دورة حالات سجل التأهيل، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC05-QUAL-RECORD -->

</details>

### 5.2 US-BC05-QUAL-REINSTATE — إعادة سجل التأهيل إلى السريان

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

<!-- BEGIN GENERATED: refs US-BC05-QUAL-REINSTATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/qualification-records/{id}/actions/reinstate` | — |
| الأمر | `CMD-QUAL-REINSTATE` | إعادة سجل التأهيل إلى السريان |
| السياسة | `POL-QUAL-REINSTATE` | Resource Manager / Training Manager؛ tenant match; task visible; org scope |
| الحدث | `EVT-QUAL-REINSTATED` | يصل إلى: Eligibility cache invalidation; Task assignment re-check report |
| الكيان | `AGG-QUALIFICATION-RECORD` | سجل التأهيل |
| الجدول | `readiness.qualification_records` | الجدول الرئيسي لسجل التأهيل |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RDY-001، REQ-RDY-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-QUALIFICATION-RECORD-SM، TST-SLC03-INVARIANTS | دورة حالات سجل التأهيل، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC05-QUAL-REINSTATE -->

</details>

### 5.3 US-BC05-QUAL-RENEW — تجديد سجل التأهيل

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

<!-- BEGIN GENERATED: refs US-BC05-QUAL-RENEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/qualification-records/{id}/actions/renew` | — |
| الأمر | `CMD-QUAL-RENEW` | تجديد سجل التأهيل |
| السياسة | `POL-QUAL-RENEW` | Resource Manager / Training Manager؛ tenant match; task visible; org scope |
| الحدث | `EVT-QUAL-RENEWED` | يصل إلى: Eligibility cache invalidation; Task assignment re-check report |
| الكيان | `AGG-QUALIFICATION-RECORD` | سجل التأهيل |
| الجدول | `readiness.qualification_records` | الجدول الرئيسي لسجل التأهيل |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RDY-001، REQ-RDY-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-QUALIFICATION-RECORD-SM، TST-SLC03-INVARIANTS | دورة حالات سجل التأهيل، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC05-QUAL-RENEW -->

</details>

### 5.4 US-BC05-QUAL-REVOKE — سحب سجل التأهيل

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

<!-- BEGIN GENERATED: refs US-BC05-QUAL-REVOKE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/qualification-records/{id}/actions/revoke` | — |
| الأمر | `CMD-QUAL-REVOKE` | سحب سجل التأهيل |
| السياسة | `POL-QUAL-REVOKE` | Resource Manager / Training Manager؛ tenant match; task visible; org scope |
| الحدث | `EVT-QUAL-REVOKED` | يصل إلى: Eligibility cache invalidation; Task assignment re-check report |
| الكيان | `AGG-QUALIFICATION-RECORD` | سجل التأهيل |
| الجدول | `readiness.qualification_records` | الجدول الرئيسي لسجل التأهيل |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RDY-001، REQ-RDY-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-QUALIFICATION-RECORD-SM، TST-SLC03-INVARIANTS | دورة حالات سجل التأهيل، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC05-QUAL-REVOKE -->

</details>

### 5.5 US-BC05-QUAL-SUSPEND — تعليق سجل التأهيل

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

<!-- BEGIN GENERATED: refs US-BC05-QUAL-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/qualification-records/{id}/actions/suspend` | — |
| الأمر | `CMD-QUAL-SUSPEND` | تعليق سجل التأهيل |
| السياسة | `POL-QUAL-SUSPEND` | Resource Manager / Training Manager؛ tenant match; task visible; org scope |
| الحدث | `EVT-QUAL-SUSPENDED` | يصل إلى: Eligibility cache invalidation; Task assignment re-check report |
| الكيان | `AGG-QUALIFICATION-RECORD` | سجل التأهيل |
| الجدول | `readiness.qualification_records` | الجدول الرئيسي لسجل التأهيل |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RDY-001، REQ-RDY-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-QUALIFICATION-RECORD-SM، TST-SLC03-INVARIANTS | دورة حالات سجل التأهيل، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC05-QUAL-SUSPEND -->

</details>

### 5.6 US-BC05-Q-QUAL-LIST — جلب: Qualification records as of t

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

<!-- BEGIN GENERATED: refs US-BC05-Q-QUAL-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/persons/{person_id}/qualifications` | — |
| الاستعلام | `QRY-QUAL-LIST` | Qualification records as of t |
| السياسة | `POL-QUAL-LIST` | Manager/Resource Manager in scope; self |
| الكيان | `AGG-QUALIFICATION-RECORD` | سجل التأهيل |
| الجدول | `readiness.qualification_records` | الجدول الرئيسي لسجل التأهيل |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-RDY-001 | The system shall record each person's competencies, qualifications and certifications with their validity per… |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-QUALIFICATION-RECORD-SM، TST-SLC03-INVARIANTS | دورة حالات سجل التأهيل، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC05-Q-QUAL-LIST -->

</details>

### 5.7 US-BC05-S-QUALIFICATION-RECORD-01 — تلقائي: valid_to reached (سجل التأهيل)

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

<!-- BEGIN GENERATED: refs US-BC05-S-QUALIFICATION-RECORD-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:valid_to reached` | scheduler (eligibility also checks validity at read time) |
| الانتقال | ACTIVE, SUSPENDED ← EXPIRED | — |
| الحدث | `EVT-QUAL-EXPIRED` | يصل إلى: Eligibility cache invalidation; Task assignment re-check report |
| الكيان | `AGG-QUALIFICATION-RECORD` | سجل التأهيل |
| الجدول | `readiness.qualification_records` | الجدول الرئيسي لسجل التأهيل |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RDY-001، REQ-RDY-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-102 | Check Eligibility |
| الاختبار | TST-QUALIFICATION-RECORD-SM، TST-SLC03-INVARIANTS | دورة حالات سجل التأهيل، وثوابت الشريحة SLC-03 |
<!-- END GENERATED: refs US-BC05-S-QUALIFICATION-RECORD-01 -->

</details>

### 5.8 US-DOM-QUAL-EXPIRY-NOTICE — تنبيه الفرد ومديره قبل انتهاء المؤهل

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

<!-- BEGIN GENERATED: refs US-DOM-QUAL-EXPIRY-NOTICE -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-102 | Check Eligibility |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RDY-001 | The system shall record each person's competencies, qualifications and certifications with their validity per… |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-DOM-QUAL-EXPIRY-NOTICE -->

</details>

### 5.9 US-UI-SCR42-MY-QUALS — الفرد يرى مؤهلاته وشهاداته

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

<!-- BEGIN GENERATED: refs US-UI-SCR42-MY-QUALS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-42 | شاشة التأهيل والأهلية |
| المصدر | `17-security-design.md §12.6` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RDY-001 | The system shall record each person's competencies, qualifications and certifications with their validity per… |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-UI-SCR42-MY-QUALS -->

</details>

### 5.10 US-UI-SCR42-QUAL-LIST — مؤهلات الفرد وصلاحيتها في تاريخ معين

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

<!-- BEGIN GENERATED: refs US-UI-SCR42-QUAL-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-42 | شاشة التأهيل والأهلية |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RDY-001 | The system shall record each person's competencies, qualifications and certifications with their validity per… |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-UI-SCR42-QUAL-LIST -->

</details>

### 5.11 US-INT-HR-QUALIFICATIONS — استيراد المؤهلات من نظام الموارد البشرية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-HR-QUALIFICATIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §4` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RDY-001 | The system shall record each person's competencies, qualifications and certifications with their validity per… |
| حالة الاستخدام | UC-102 | Check Eligibility |
<!-- END GENERATED: refs US-INT-HR-QUALIFICATIONS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RDY-001 | The system shall record each person's competencies, qualifications and certifications with their validity per… | `US-BC05-Q-QUAL-LIST`، `US-BC05-QUAL-RECORD`، `US-BC05-QUAL-REINSTATE`، `US-BC05-QUAL-RENEW`، `US-BC05-QUAL-REVOKE`، `US-BC05-QUAL-SUSPEND`، `US-BC05-S-QUALIFICATION-RECORD-01`، `US-DOM-QUAL-EXPIRY-NOTICE`، `US-INT-HR-QUALIFICATIONS`، `US-UI-SCR42-MY-QUALS`، `US-UI-SCR42-QUAL-LIST` | TST-QUALIFICATION-RECORD-SM، TST-SLC03-INVARIANTS |
| REQ-RDY-002 | When eligibility is checked for a person, role or task at a given time, the system shall return ELIGIBLE, CON… | كل قصص الأوامر والنظام في الميزة (6) | TST-QUALIFICATION-RECORD-SM، TST-SLC03-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
