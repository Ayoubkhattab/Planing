---
id: FEAT-INF-CONFLICT-DETECT
type: feature
title: "كشف تعارض المعلومات"
status: DRAFT
version: "0.1"
capability: CAP-03.06
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# كشف تعارض المعلومات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-CONFLICT-DETECT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.06 إدارة التعارض (R1) |
| الأدوار | النظام؛ المحلل |
| الشاشات | SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-008 |
| القصص | 8: 5 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يُكشف تلقائيًا أو يدويًا كل تناقض بين معلومتين عن الشيء نفسه فيُحفظ الطرفان ولا يُخفى أحدهما.

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
| QAS-CNF-001 | incompatible claim committed | conflict opened p95 ≤ 30 s |
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
| `US-BC02-CNF-RAISE` | رفع التعارض | أمر | مسودة |
| `US-BC02-Q-CNF-LIST` | جلب: Conflicts by subject, predicate, state, assignee | جلب | مسودة |
| `US-BC02-S-CONFLICT-01` | تلقائي: conflict rule matched (التعارض) | نظام | مسودة |
| `US-BC02-S-CONFLICT-02` | تلقائي: incompatible claim joined (التعارض) | نظام | مسودة |
| `US-BC02-S-CONFLICT-03` | تلقائي: member set no longer conflicting (التعارض) | نظام | مسودة |
| `US-UI-SCR06-INFO-CONFLICTS` | قائمة التعارضات مصفاة بالموضوع والحالة والمسند إليه | واجهة | مسودة |
| `US-PLT-CONFLICT-DETECT-LATENCY` | فتح التعارض خلال 30 ثانية دون فقد | منصة | مسودة |
| `US-OPS-CONFLICT-LAG-WATCH` | مراقبة تأخر كشف التعارضات | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-CNF-RAISE — رفع التعارض

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

<!-- BEGIN GENERATED: refs US-BC02-CNF-RAISE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/conflicts` | — |
| الأمر | `CMD-CNF-RAISE` | رفع التعارض |
| السياسة | `POL-CNF-RAISE` | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ tenant match; object visible |
| الحدث | `EVT-CNF-RAISED` | يصل إلى: Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED m… |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-CNF-RAISE -->

</details>

### 5.2 US-BC02-Q-CNF-LIST — جلب: Conflicts by subject, predicate, state, assignee

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

<!-- BEGIN GENERATED: refs US-BC02-Q-CNF-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/conflicts` | — |
| الاستعلام | `QRY-CNF-LIST` | Conflicts by subject, predicate, state, assignee |
| السياسة | `POL-CNF-LIST` | Analyst; only conflicts with ≥ 2 visible member claims |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-Q-CNF-LIST -->

</details>

### 5.3 US-BC02-S-CONFLICT-01 — تلقائي: conflict rule matched (التعارض)

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

<!-- BEGIN GENERATED: refs US-BC02-S-CONFLICT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:conflict rule matched` | rule CF-01..CF-04 on claims of the same identity cluster, same predicate, overlapping valid; no non-terminal… |
| الانتقال | ∅ ← OPEN | — |
| الحدث | `EVT-CNF-DETECTED` | يصل إلى: Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED m… |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-S-CONFLICT-01 -->

</details>

### 5.4 US-BC02-S-CONFLICT-02 — تلقائي: incompatible claim joined (التعارض)

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

<!-- BEGIN GENERATED: refs US-BC02-S-CONFLICT-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:incompatible claim joined` | new CURRENT claim incompatible with members (same key, overlapping window) |
| الانتقال | OPEN, UNDER_REVIEW ← (بلا تغيير) | — |
| الحدث | `EVT-CNF-CLAIM-ADDED` | يصل إلى: Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED m… |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-S-CONFLICT-02 -->

</details>

### 5.5 US-BC02-S-CONFLICT-03 — تلقائي: member set no longer conflicting (التعارض)

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

<!-- BEGIN GENERATED: refs US-BC02-S-CONFLICT-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:member set no longer conflicting` | fewer than 2 incompatible CURRENT members (claims closed, split, or corrected) |
| الانتقال | OPEN, UNDER_REVIEW, RESOLVED, ACCEPTED_AS_CONFLICT ← SUPERSEDED | — |
| الحدث | `EVT-CNF-SUPERSEDED` | يصل إلى: Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED m… |
| الكيان | `AGG-CONFLICT` | التعارض |
| الجدول | `information.conflicts` | الجدول الرئيسي للتعارض |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
| الاختبار | TST-CONFLICT-SM، TST-SLC04-INVARIANTS | دورة حالات التعارض، وثوابت الشريحة SLC-04 |
<!-- END GENERATED: refs US-BC02-S-CONFLICT-03 -->

</details>

### 5.6 US-UI-SCR06-INFO-CONFLICTS — قائمة التعارضات مصفاة بالموضوع والحالة والمسند إليه

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

<!-- BEGIN GENERATED: refs US-UI-SCR06-INFO-CONFLICTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `THR-S04-03` | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
<!-- END GENERATED: refs US-UI-SCR06-INFO-CONFLICTS -->

</details>

### 5.7 US-PLT-CONFLICT-DETECT-LATENCY — فتح التعارض خلال 30 ثانية دون فقد

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

<!-- BEGIN GENERATED: refs US-PLT-CONFLICT-DETECT-LATENCY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-CNF-001 | incompatible claim committed → conflict opened p95 ≤ 30 s |
| المصدر | `FM-S04-01` | — |
| المتطلب | REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… |
| حالة الاستخدام | UC-008 | Resolve Conflict |
<!-- END GENERATED: refs US-PLT-CONFLICT-DETECT-LATENCY -->

</details>

### 5.8 US-OPS-CONFLICT-LAG-WATCH — مراقبة تأخر كشف التعارضات

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

<!-- BEGIN GENERATED: refs US-OPS-CONFLICT-LAG-WATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc04.md` | — |
| المصدر | `FM-S04-01` | — |
<!-- END GENERATED: refs US-OPS-CONFLICT-LAG-WATCH -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the syst… | `US-BC02-CNF-RAISE`، `US-BC02-Q-CNF-LIST`، `US-BC02-S-CONFLICT-01`، `US-BC02-S-CONFLICT-02`، `US-BC02-S-CONFLICT-03`، `US-PLT-CONFLICT-DETECT-LATENCY`، `US-UI-SCR06-INFO-CONFLICTS` | TST-CONFLICT-SM، TST-SLC04-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
