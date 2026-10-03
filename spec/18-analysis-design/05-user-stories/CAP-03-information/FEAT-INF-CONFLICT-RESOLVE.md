---
id: FEAT-INF-CONFLICT-RESOLVE
type: feature
title: "حل التعارضات"
status: DRAFT
version: "0.1"
capability: CAP-03.06
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# حل التعارضات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-CONFLICT-RESOLVE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.06 إدارة التعارض (R1) |
| الأدوار | قائد المحللين؛ المحلل |
| الشاشات | SCR-26 التعارض ومطابقة الكيانات، SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-008 |
| القصص | 8: 6 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يُسند قائد المحللين التعارض لمحلل يدرسه ويحسمه أو يقبله مع إمكانية إعادة فتحه.

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
| `US-BC02-CNF-ACCEPT` | قبول التعارض | أمر | مسودة |
| `US-BC02-CNF-ASSIGN` | إسناد التعارض | أمر | مسودة |
| `US-BC02-CNF-REOPEN` | إعادة فتح التعارض | أمر | مسودة |
| `US-BC02-CNF-RESOLVE` | حل التعارض | أمر | مسودة |
| `US-BC02-CNF-START-REVIEW` | بدء مراجعة التعارض | أمر | مسودة |
| `US-BC02-Q-CNF-GET` | جلب: Conflict with visible members, evidence, resolution history (as known_at) | جلب | مسودة |
| `US-UI-SCR26-CONFLICT-COMPARE` | مقارنة طرفي التعارض وحسمه أو قبوله | واجهة | مسودة |
| `US-OPS-CONFLICT-BACKLOG-WATCH` | مراقبة تراكم التعارضات المفتوحة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-CNF-ACCEPT — قبول التعارض

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

<!-- BEGIN GENERATED: refs US-BC02-CNF-ACCEPT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/conflicts/{id}/actions/accept` | — |
| الأمر | `CMD-CNF-ACCEPT` | قبول التعارض |
| السياسة | `POL-CNF-ACCEPT` | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ tenant match; object visible |
| الحدث | `EVT-CNF-ACCEPTED` | يصل إلى: Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED m… |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-CNF-ACCEPT -->

</details>

### 5.2 US-BC02-CNF-ASSIGN — إسناد التعارض

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

<!-- BEGIN GENERATED: refs US-BC02-CNF-ASSIGN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/conflicts/{id}/actions/assign` | — |
| الأمر | `CMD-CNF-ASSIGN` | إسناد التعارض |
| السياسة | `POL-CNF-ASSIGN` | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ tenant match; assignee cleared for… |
| الحدث | `EVT-CNF-ASSIGNED` | يصل إلى: Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED m… |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-CNF-ASSIGN -->

</details>

### 5.3 US-BC02-CNF-REOPEN — إعادة فتح التعارض

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

<!-- BEGIN GENERATED: refs US-BC02-CNF-REOPEN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/conflicts/{id}/actions/reopen` | — |
| الأمر | `CMD-CNF-REOPEN` | إعادة فتح التعارض |
| السياسة | `POL-CNF-REOPEN` | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ tenant match; object visible |
| الحدث | `EVT-CNF-REOPENED` | يصل إلى: Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED m… |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-CNF-REOPEN -->

</details>

### 5.4 US-BC02-CNF-RESOLVE — حل التعارض

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

<!-- BEGIN GENERATED: refs US-BC02-CNF-RESOLVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/conflicts/{id}/actions/resolve` | — |
| الأمر | `CMD-CNF-RESOLVE` | حل التعارض |
| السياسة | `POL-CNF-RESOLVE` | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ tenant match; cleared for every mem… |
| الحدث | `EVT-CNF-RESOLVED` | يصل إلى: Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED m… |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-CNF-RESOLVE -->

</details>

### 5.5 US-BC02-CNF-START-REVIEW — بدء مراجعة التعارض

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

<!-- BEGIN GENERATED: refs US-BC02-CNF-START-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/conflicts/{id}/actions/start-review` | — |
| الأمر | `CMD-CNF-START-REVIEW` | بدء مراجعة التعارض |
| السياسة | `POL-CNF-START-REVIEW` | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ tenant match; object visible |
| الحدث | `EVT-CNF-REVIEW-STARTED` | يصل إلى: Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED m… |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-CNF-START-REVIEW -->

</details>

### 5.6 US-BC02-Q-CNF-GET — جلب: Conflict with visible members, evidence, resolution history (as known_at)

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

<!-- BEGIN GENERATED: refs US-BC02-Q-CNF-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/conflicts/{conflict_id}` | — |
| الاستعلام | `QRY-CNF-GET` | Conflict with visible members, evidence, resolution history (as known_at) |
| السياسة | `POL-CNF-GET` | Analyst; visibility rule INV-CNF-04 |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-Q-CNF-GET -->

</details>

### 5.7 US-UI-SCR26-CONFLICT-COMPARE — مقارنة طرفي التعارض وحسمه أو قبوله

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

<!-- BEGIN GENERATED: refs US-UI-SCR26-CONFLICT-COMPARE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-26 | شاشة التعارض ومطابقة الكيانات |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
<!-- END GENERATED: refs US-UI-SCR26-CONFLICT-COMPARE -->

</details>

### 5.8 US-OPS-CONFLICT-BACKLOG-WATCH — مراقبة تراكم التعارضات المفتوحة

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

<!-- BEGIN GENERATED: refs US-OPS-CONFLICT-BACKLOG-WATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc04.md` | — |
<!-- END GENERATED: refs US-OPS-CONFLICT-BACKLOG-WATCH -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… | `US-BC02-CNF-ACCEPT`، `US-BC02-CNF-ASSIGN`، `US-BC02-CNF-REOPEN`، `US-BC02-CNF-RESOLVE`، `US-BC02-CNF-START-REVIEW`، `US-BC02-Q-CNF-GET`، `US-UI-SCR26-CONFLICT-COMPARE` | TST-CONFLICT-SM، TST-SLC04-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
