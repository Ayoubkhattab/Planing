---
id: FEAT-OPS-PLAN-LIFECYCLE
type: feature
title: "إدارة حالة الخطة"
status: DRAFT
version: "0.1"
capability: CAP-07.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة حالة الخطة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-OPS-PLAN-LIFECYCLE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-07 التخطيط والتنفيذ |
| القدرة الفرعية | CAP-07.01 الأهداف والتخطيط (R1) |
| الأدوار | المخطِّط؛ مالك الخطة؛ صاحب السلطة أو المعتمِد الثاني؛ مسؤول الأمن؛ النظام |
| الشاشات | SCR-34 الخطة ونسخها |
| حالات الاستخدام | UC-033 |
| القصص | 9: 7 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعلّق المخطط الخطة أو يستأنفها أو يكملها أو يغلقها، ويُنبَّه إن أُبطل قرار تقوم عليه.

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
| `US-BC04-PLN-CANCEL` | إلغاء الخطة | أمر | مسودة |
| `US-BC04-PLN-CLOSE` | إغلاق الخطة | أمر | مسودة |
| `US-BC04-PLN-COMPLETE` | إكمال الخطة | أمر | مسودة |
| `US-BC04-PLN-RECLASSIFY` | إعادة تصنيف الخطة | أمر | مسودة |
| `US-BC04-PLN-RESUME` | استئناف الخطة | أمر | مسودة |
| `US-BC04-PLN-SUSPEND` | تعليق الخطة | أمر | مسودة |
| `US-BC04-S-PLAN-02` | تلقائي: implemented decision annulled or superseded (الخطة) | نظام | مسودة |
| `US-UI-SCR34-LIFECYCLE-ACTIONS` | أفعال حالة الخطة وأثرها على المهام | واجهة | مسودة |
| `US-UI-SCR34-REVIEW-FLAG` | تنبيه الخطة عند إبطال قرارها | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-PLN-CANCEL — إلغاء الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLN-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plans/{id}/actions/cancel` | — |
| الأمر | `CMD-PLN-CANCEL` | إلغاء الخطة |
| السياسة | `POL-PLN-CANCEL` | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassif… |
| الحدث | `EVT-PLN-CANCELLED` | يصل إلى: Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assigne… |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-001، REQ-OPS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLN-CANCEL -->

</details>

### 5.2 US-BC04-PLN-CLOSE — إغلاق الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLN-CLOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plans/{id}/actions/close` | — |
| الأمر | `CMD-PLN-CLOSE` | إغلاق الخطة |
| السياسة | `POL-PLN-CLOSE` | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassif… |
| الحدث | `EVT-PLN-CLOSED` | يصل إلى: Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assigne… |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-001، REQ-OPS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLN-CLOSE -->

</details>

### 5.3 US-BC04-PLN-COMPLETE — إكمال الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLN-COMPLETE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plans/{id}/actions/complete` | — |
| الأمر | `CMD-PLN-COMPLETE` | إكمال الخطة |
| السياسة | `POL-PLN-COMPLETE` | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassif… |
| الحدث | `EVT-PLN-COMPLETED` | يصل إلى: Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assigne… |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-001، REQ-OPS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLN-COMPLETE -->

</details>

### 5.4 US-BC04-PLN-RECLASSIFY — إعادة تصنيف الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLN-RECLASSIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plans/{id}/actions/reclassify` | — |
| الأمر | `CMD-PLN-RECLASSIFY` | إعادة تصنيف الخطة |
| السياسة | `POL-PLN-RECLASSIFY` | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassif… |
| الحدث | `EVT-PLN-RECLASSIFIED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-001، REQ-OPS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLN-RECLASSIFY -->

</details>

### 5.5 US-BC04-PLN-RESUME — استئناف الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLN-RESUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plans/{id}/actions/resume` | — |
| الأمر | `CMD-PLN-RESUME` | استئناف الخطة |
| السياسة | `POL-PLN-RESUME` | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassif… |
| الحدث | `EVT-PLN-RESUMED` | يصل إلى: Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assigne… |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-001، REQ-OPS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLN-RESUME -->

</details>

### 5.6 US-BC04-PLN-SUSPEND — تعليق الخطة

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

<!-- BEGIN GENERATED: refs US-BC04-PLN-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/plans/{id}/actions/suspend` | — |
| الأمر | `CMD-PLN-SUSPEND` | تعليق الخطة |
| السياسة | `POL-PLN-SUSPEND` | Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassif… |
| الحدث | `EVT-PLN-SUSPENDED` | يصل إلى: Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assigne… |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-001، REQ-OPS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-PLN-SUSPEND -->

</details>

### 5.7 US-BC04-S-PLAN-02 — تلقائي: implemented decision annulled or superseded (الخطة)

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

<!-- BEGIN GENERATED: refs US-BC04-S-PLAN-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:implemented decision annulled or superseded` | plan flagged for review (no automatic change) |
| الانتقال | ACTIVE, SUSPENDED ← (بلا تغيير) | — |
| الحدث | `EVT-PLN-REVIEW-FLAGGED` | يصل إلى: Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assigne… |
| الكيان | `AGG-PLAN` | الخطة |
| الجدول | `operations.plans` | الجدول الرئيسي للخطة |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-OPS-001، REQ-OPS-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-033 | Create Plan |
| الاختبار | TST-PLAN-SM، TST-SLC08-INVARIANTS | دورة حالات الخطة، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-S-PLAN-02 -->

</details>

### 5.8 US-UI-SCR34-LIFECYCLE-ACTIONS — أفعال حالة الخطة وأثرها على المهام

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

<!-- BEGIN GENERATED: refs US-UI-SCR34-LIFECYCLE-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-34 | شاشة الخطة ونسخها |
| المصدر | `21-ui-design.md §6.3` | — |
| المصدر | `decision-plan-spec.md §3` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR34-LIFECYCLE-ACTIONS -->

</details>

### 5.9 US-UI-SCR34-REVIEW-FLAG — تنبيه الخطة عند إبطال قرارها

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

<!-- BEGIN GENERATED: refs US-UI-SCR34-REVIEW-FLAG -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-34 | شاشة الخطة ونسخها |
| المصدر | `US-BC04-S-PLAN-02` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OPS-002 | The system shall link every approved plan to the decisions or objectives it implements. |
| حالة الاستخدام | UC-033 | Create Plan |
<!-- END GENERATED: refs US-UI-SCR34-REVIEW-FLAG -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,… | كل قصص الميزة المأخوذة من المواصفة (7) | TST-PLAN-SM، TST-PLAN-VERSION-SM، TST-SLC08-INVARIANTS |
| REQ-OPS-002 | The system shall link every approved plan to the decisions or objectives it implements. | `US-BC04-PLN-CANCEL`، `US-BC04-PLN-CLOSE`، `US-BC04-PLN-COMPLETE`، `US-BC04-PLN-RECLASSIFY`، `US-BC04-PLN-RESUME`، `US-BC04-PLN-SUSPEND`، `US-BC04-S-PLAN-02`، `US-UI-SCR34-REVIEW-FLAG` | TST-PLAN-SM، TST-SLC08-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
