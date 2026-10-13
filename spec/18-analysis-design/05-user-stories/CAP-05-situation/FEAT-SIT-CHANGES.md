---
id: FEAT-SIT-CHANGES
type: feature
title: "متابعة تغيرات الموقف"
status: DRAFT
version: "0.1"
capability: CAP-05.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# متابعة تغيرات الموقف

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-SIT-CHANGES |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-05 الوعي بالموقف |
| القدرة الفرعية | CAP-05.02 المراقبة والتنبيه (R1) |
| الأدوار | المحلل؛ المدير؛ النظام |
| الشاشات | SCR-11 الصورة العملياتية المشتركة (COP)، SCR-12 إدارة الموقف وقواعد التنبيه |
| حالات الاستخدام | UC-021، UC-022 |
| القصص | 8: 1 من المواصفة، و7 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعرف المتابع ما دخل الموقف وما خرج منه أولًا بأول دون أن يراجع كل شيء يدويًا.

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
| QAS-PERF-006 | a situation member changes | p95 ≤ 10 s |
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
| `US-BC03-Q-SIT-CHANGES` | جلب: Membership change log (visible members only) since cursor/time | جلب | مسودة |
| `US-DOM-SIT-BUFFER-FOLLOW` | تحريك منطقة الموقف مع الكيان المرجعي | نظام | مسودة |
| `US-DOM-SIT-MEMBERSHIP-RECOMPUTE` | إعادة حساب العضوية بعد تعديل التعريف أو الاستئناف | نظام | مسودة |
| `US-DOM-SIT-MEMBERSHIP-UPDATE` | تحديث أعضاء الموقف تلقائيًا عند تغير الكائنات | نظام | مسودة |
| `US-UI-SCR11-CHANGE-FEED` | متابعة ما دخل الموقف وما خرج منه مباشرة | واجهة | مسودة |
| `US-UI-SCR12-RECOMPUTE-STATUS` | إظهار تقدم إعادة حساب العضوية بعد التعديل | واجهة | مسودة |
| `US-PLT-SIT-MEMBERSHIP-LATENCY` | انعكاس تغير العضو في الموقف خلال عشر ثوان | منصة | مسودة |
| `US-PLT-SIT-MEMBERSHIP-RECOVERY` | استئناف تقييم العضوية من آخر نقطة بعد العطل | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-Q-SIT-CHANGES — جلب: Membership change log (visible members only) since cursor/time

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

<!-- BEGIN GENERATED: refs US-BC03-Q-SIT-CHANGES -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/situations/{situation_id}/changes` | — |
| الاستعلام | `QRY-SIT-CHANGES` | Membership change log (visible members only) since cursor/time |
| السياسة | `POL-SIT-CHANGES` | cleared for situation; per-member filtering |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-002 | When an object matching a situation's criteria is created or changed, the system shall update the situation m… |
| حالات الاستخدام | UC-021، UC-022 | Monitor Situation؛ Review Situation Change |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-Q-SIT-CHANGES -->

</details>

### 5.2 US-DOM-SIT-BUFFER-FOLLOW — تحريك منطقة الموقف مع الكيان المرجعي

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

<!-- BEGIN GENERATED: refs US-DOM-SIT-BUFFER-FOLLOW -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `situation-alerting-spec.md §2` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
<!-- END GENERATED: refs US-DOM-SIT-BUFFER-FOLLOW -->

</details>

### 5.3 US-DOM-SIT-MEMBERSHIP-RECOMPUTE — إعادة حساب العضوية بعد تعديل التعريف أو الاستئناف

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

<!-- BEGIN GENERATED: refs US-DOM-SIT-MEMBERSHIP-RECOMPUTE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `situation-alerting-spec.md §2` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-SIT-002 | When an object matching a situation's criteria is created or changed, the system shall update the situation m… |
| حالات الاستخدام | UC-021، UC-022 | Monitor Situation؛ Review Situation Change |
<!-- END GENERATED: refs US-DOM-SIT-MEMBERSHIP-RECOMPUTE -->

</details>

### 5.4 US-DOM-SIT-MEMBERSHIP-UPDATE — تحديث أعضاء الموقف تلقائيًا عند تغير الكائنات

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

<!-- BEGIN GENERATED: refs US-DOM-SIT-MEMBERSHIP-UPDATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-006 | a situation member changes → p95 ≤ 10 s |
| القرار المعماري | ADR-P07 | Nature of Situation |
| المصدر | `situation-alerting-spec.md §2` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-SIT-002 | When an object matching a situation's criteria is created or changed, the system shall update the situation m… |
| حالات الاستخدام | UC-021، UC-022 | Monitor Situation؛ Review Situation Change |
<!-- END GENERATED: refs US-DOM-SIT-MEMBERSHIP-UPDATE -->

</details>

### 5.5 US-UI-SCR11-CHANGE-FEED — متابعة ما دخل الموقف وما خرج منه مباشرة

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

<!-- BEGIN GENERATED: refs US-UI-SCR11-CHANGE-FEED -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-11 | شاشة الصورة العملياتية المشتركة (COP) |
| حالة الاستخدام | UC-021 | Monitor Situation |
| حالة الاستخدام | UC-022 | Review Situation Change |
| المصدر | `21-ui-design.md §7` | — |
<!-- END GENERATED: refs US-UI-SCR11-CHANGE-FEED -->

</details>

### 5.6 US-UI-SCR12-RECOMPUTE-STATUS — إظهار تقدم إعادة حساب العضوية بعد التعديل

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

<!-- BEGIN GENERATED: refs US-UI-SCR12-RECOMPUTE-STATUS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-12 | شاشة إدارة الموقف وقواعد التنبيه |
| المصدر | `situation-alerting-spec.md §2` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR12-RECOMPUTE-STATUS -->

</details>

### 5.7 US-PLT-SIT-MEMBERSHIP-LATENCY — انعكاس تغير العضو في الموقف خلال عشر ثوان

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

<!-- BEGIN GENERATED: refs US-PLT-SIT-MEMBERSHIP-LATENCY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-006 | a situation member changes → p95 ≤ 10 s |
| المصدر | `situation-alerting-spec.md §1` | — |
| المصدر | `situation-alerting-spec.md §2` | — |
<!-- END GENERATED: refs US-PLT-SIT-MEMBERSHIP-LATENCY -->

</details>

### 5.8 US-PLT-SIT-MEMBERSHIP-RECOVERY — استئناف تقييم العضوية من آخر نقطة بعد العطل

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

<!-- BEGIN GENERATED: refs US-PLT-SIT-MEMBERSHIP-RECOVERY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `FM-S06-02` | — |
| المصدر | `observability-slc06.md` | — |
<!-- END GENERATED: refs US-PLT-SIT-MEMBERSHIP-RECOVERY -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… | `US-DOM-SIT-BUFFER-FOLLOW` | TST-SITUATION-SM، TST-SLC06-INVARIANTS |
| REQ-SIT-002 | When an object matching a situation's criteria is created or changed, the system shall update the situation m… | `US-BC03-Q-SIT-CHANGES`، `US-DOM-SIT-MEMBERSHIP-RECOMPUTE`، `US-DOM-SIT-MEMBERSHIP-UPDATE` | TST-SITUATION-SM، TST-SLC06-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
