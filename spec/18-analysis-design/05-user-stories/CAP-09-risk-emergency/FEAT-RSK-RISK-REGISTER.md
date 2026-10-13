---
id: FEAT-RSK-RISK-REGISTER
type: feature
title: "سجل المخاطر"
status: DRAFT
version: "0.1"
capability: CAP-09.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# سجل المخاطر

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RSK-RISK-REGISTER |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-09 المخاطر والطوارئ |
| القدرة الفرعية | CAP-09.01 إدارة المخاطر (R3) |
| الأدوار | محدِّد الخطر؛ مدير المخاطر؛ مالك النطاق؛ النظام |
| الشاشات | SCR-47 سجل المخاطر والحوادث |
| حالات الاستخدام | UC-140 |
| القصص | 7: 4 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يسجل المستخدم المخوَّل خطرًا محتملًا بنطاقه، ويتصفح سجل المخاطر مصفّى حسب ما يحق له رؤيته.

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
| `US-BC04-RIS-IDENTIFY` | تحديد الخطر | أمر | مسودة |
| `US-BC04-Q-RIS-GET` | جلب: Risk بنطاقه المرئي للطالب | جلب | مسودة |
| `US-BC04-Q-RIS-REGISTER` | جلب: سجل المخاطر مصفّى بالفئة/النطاق/الدرجة | جلب | مسودة |
| `US-BC04-S-RISK-01` | تلقائي: incident references this risk as risk_ref (الخطر) | نظام | مسودة |
| `US-UI-SCR47-RISK-FORM` | تسجيل خطر بفئته ونطاقه | واجهة | مسودة |
| `US-UI-SCR47-RISK-REGISTER` | سجل المخاطر بالتصفية ومصفوفة الدرجة | واجهة | مسودة |
| `US-OPS-RSK-HAZARD-CATALOG` | تحميل فئات الخطر للمستأجر عند التهيئة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-RIS-IDENTIFY — تحديد الخطر

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

<!-- BEGIN GENERATED: refs US-BC04-RIS-IDENTIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/risks` | — |
| الأمر | `CMD-RIS-IDENTIFY` | تحديد الخطر |
| السياسة | `POL-RIS-IDENTIFY` | محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق)؛ t… |
| الحدث | `EVT-RIS-IDENTIFIED` | يصل إلى: Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| الكيان | `AGG-RISK` | الخطر |
| الجدول | `operations.risks` | الجدول الرئيسي للخطر |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-001، REQ-RCM-002، REQ-RCM-003، REQ-RCM-004، REQ-RCM-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-140 | Identify & Assess Risk |
| الاختبار | TST-RISK-SM، TST-SLC17-INVARIANTS | دورة حالات الخطر، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-RIS-IDENTIFY -->

</details>

### 5.2 US-BC04-Q-RIS-GET — جلب: Risk بنطاقه المرئي للطالب

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

<!-- BEGIN GENERATED: refs US-BC04-Q-RIS-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/risks/{risk_id}` | — |
| الاستعلام | `QRY-RIS-GET` | Risk بنطاقه المرئي للطالب |
| السياسة | `POL-RIS-GET` | مالك النطاق؛ مدير المخاطر |
| الكيان | `AGG-RISK` | الخطر |
| الجدول | `operations.risks` | الجدول الرئيسي للخطر |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-RCM-014 | The system shall let an authorized actor list and filter the risk register by category, scope and score, rest… |
| حالة الاستخدام | UC-140 | Identify & Assess Risk |
| الاختبار | TST-RISK-SM، TST-SLC17-INVARIANTS | دورة حالات الخطر، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-Q-RIS-GET -->

</details>

### 5.3 US-BC04-Q-RIS-REGISTER — جلب: سجل المخاطر مصفّى بالفئة/النطاق/الدرجة

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

<!-- BEGIN GENERATED: refs US-BC04-Q-RIS-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/risks` | — |
| الاستعلام | `QRY-RIS-REGISTER` | سجل المخاطر مصفّى بالفئة/النطاق/الدرجة |
| السياسة | `POL-RIS-REGISTER` | allowed_scope |
| الكيان | `AGG-RISK` | الخطر |
| الجدول | `operations.risks` | الجدول الرئيسي للخطر |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-RCM-014 | The system shall let an authorized actor list and filter the risk register by category, scope and score, rest… |
| حالة الاستخدام | UC-140 | Identify & Assess Risk |
| الاختبار | TST-RISK-SM، TST-SLC17-INVARIANTS | دورة حالات الخطر، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-Q-RIS-REGISTER -->

</details>

### 5.4 US-BC04-S-RISK-01 — تلقائي: incident references this risk as risk_ref (الخطر)

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

<!-- BEGIN GENERATED: refs US-BC04-S-RISK-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:incident references this risk as risk_ref` | رابط تلقائي عند تسجيل حادثة تحقَّق منها هذا الخطر؛ لا يغيّر حالة الخطر تلقائياً أبداً (INV-RIS-05) |
| الانتقال | أي حالة غير نهائية ← (بلا تغيير) | — |
| الحدث | `EVT-RIS-MATERIALIZATION-LINKED` | يصل إلى: Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| الكيان | `AGG-RISK` | الخطر |
| الجدول | `operations.risks` | الجدول الرئيسي للخطر |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-RCM-001، REQ-RCM-002، REQ-RCM-003، REQ-RCM-004، REQ-RCM-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-140 | Identify & Assess Risk |
| الاختبار | TST-RISK-SM، TST-SLC17-INVARIANTS | دورة حالات الخطر، وثوابت الشريحة SLC-17 |
<!-- END GENERATED: refs US-BC04-S-RISK-01 -->

</details>

### 5.5 US-UI-SCR47-RISK-FORM — تسجيل خطر بفئته ونطاقه

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

<!-- BEGIN GENERATED: refs US-UI-SCR47-RISK-FORM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| المصدر | `risk-contingency-spec.md §1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RCM-001 | The system shall allow an authorized actor to identify a risk with a hazard category, description, and at lea… |
| حالة الاستخدام | UC-140 | Identify & Assess Risk |
<!-- END GENERATED: refs US-UI-SCR47-RISK-FORM -->

</details>

### 5.6 US-UI-SCR47-RISK-REGISTER — سجل المخاطر بالتصفية ومصفوفة الدرجة

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

<!-- BEGIN GENERATED: refs US-UI-SCR47-RISK-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-47 | شاشة سجل المخاطر والحوادث |
| المصدر | `21-ui-design.md §1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RCM-014 | The system shall let an authorized actor list and filter the risk register by category, scope and score, rest… |
| حالة الاستخدام | UC-140 | Identify & Assess Risk |
<!-- END GENERATED: refs US-UI-SCR47-RISK-REGISTER -->

</details>

### 5.7 US-OPS-RSK-HAZARD-CATALOG — تحميل فئات الخطر للمستأجر عند التهيئة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-RSK-HAZARD-CATALOG -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `risk-contingency-spec.md §1` | — |
| المتطلب | REQ-RCM-001 | The system shall allow an authorized actor to identify a risk with a hazard category, description, and at lea… |
| حالة الاستخدام | UC-140 | Identify & Assess Risk |
<!-- END GENERATED: refs US-OPS-RSK-HAZARD-CATALOG -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RCM-001 | The system shall allow an authorized actor to identify a risk with a hazard category, description, and at lea… | `US-BC04-RIS-IDENTIFY`، `US-BC04-S-RISK-01`، `US-OPS-RSK-HAZARD-CATALOG`، `US-UI-SCR47-RISK-FORM` | TST-RISK-SM |
| REQ-RCM-002 | The system shall require a likelihood and an impact rating (1-5) to assess a risk, and shall compute the risk… | `US-BC04-RIS-IDENTIFY`، `US-BC04-S-RISK-01` | TST-RISK-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-003 | Where tenant policy requires segregation of duties, the system shall reject a risk assessment or reassessment… | `US-BC04-RIS-IDENTIFY`، `US-BC04-S-RISK-01` | TST-RISK-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-004 | The system shall require at least one treatment action for a risk moving to treated status, unless the chosen… | `US-BC04-RIS-IDENTIFY`، `US-BC04-S-RISK-01` | TST-RISK-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-005 | The system shall require an explicit rationale to close a risk, and shall provide no command to reopen a clos… | `US-BC04-RIS-IDENTIFY`، `US-BC04-S-RISK-01` | TST-RISK-SM، TST-SLC17-INVARIANTS |
| REQ-RCM-014 | The system shall let an authorized actor list and filter the risk register by category, scope and score, rest… | `US-BC04-Q-RIS-GET`، `US-BC04-Q-RIS-REGISTER`، `US-UI-SCR47-RISK-REGISTER` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
