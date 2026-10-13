---
id: FEAT-RES-ALLOCATION-REQUEST
type: feature
title: "طلب تخصيص الموارد"
status: DRAFT
version: "0.1"
capability: CAP-08.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# طلب تخصيص الموارد

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-ALLOCATION-REQUEST |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.02 تخصيص الموارد (R2) |
| الأدوار | المخطِّط؛ النظام |
| الشاشات | SCR-41 المجمعات والتخصيص والجدول الزمني للسعة |
| حالات الاستخدام | UC-054 |
| القصص | 9: 5 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يطلب المخطط كمية من الموارد لمهمة أو خطة، فيتحقق النظام من التوفر والسعة والسياسة ويلتزم بها أو يبين سبب الرفض.

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
| QAS-RES-001 | 100 concurrent allocation requests on one pool | 0 over-commitment; deterministic priority order |
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
| `US-BC05-ALC-REQUEST` | طلب تخصيص الموارد | أمر | مسودة |
| `US-BC05-Q-ALC-LIST` | جلب: Allocations by pool, task, plan, state | جلب | مسودة |
| `US-BC05-S-ALLOCATION-01` | تلقائي: all checks passed (تخصيص الموارد) | نظام | مسودة |
| `US-BC05-S-ALLOCATION-03` | تلقائي: a check failed (تخصيص الموارد) | نظام | مسودة |
| `US-BC05-S-ALLOCATION-04` | تلقائي: provisional hold (1 h) elapsed (تخصيص الموارد) | نظام | مسودة |
| `US-UI-SCR41-ALLOCATION-LIST` | قائمة التخصيصات مجمّعة حسب الحالة | واجهة | مسودة |
| `US-UI-SCR41-ALLOCATION-REQUEST` | طلب تخصيص يبين سبب كل فحص فاشل | واجهة | مسودة |
| `US-PLT-ALC-CONTENTION` | لا التزام فوق السعة مع الطلبات المتزامنة | منصة | مسودة |
| `US-OPS-RES-NOTES-MIGRATION` | ترحيل ملاحظات الموارد النصية إلى مراجع | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-ALC-REQUEST — طلب تخصيص الموارد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-ALC-REQUEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/allocations` | — |
| الأمر | `CMD-ALC-REQUEST` | طلب تخصيص الموارد |
| السياسة | `POL-ALC-REQUEST` | Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)؛… |
| الحدث | `EVT-ALC-REQUESTED` | يصل إلى: Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| الكيان | `AGG-ALLOCATION` | تخصيص الموارد |
| الجدول | `readiness.allocations` | الجدول الرئيسي لتخصيص الموارد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-RES-007، REQ-RES-008، REQ-RES-009، REQ-RES-010، REQ-RES-011، REQ-RES-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-ALLOCATION-SM، TST-SLC09-INVARIANTS | دورة حالات تخصيص الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-ALC-REQUEST -->

</details>

### 5.2 US-BC05-Q-ALC-LIST — جلب: Allocations by pool, task, plan, state

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-Q-ALC-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/allocations` | — |
| الاستعلام | `QRY-ALC-LIST` | Allocations by pool, task, plan, state |
| السياسة | `POL-ALC-LIST` | scope |
| الكيان | `AGG-ALLOCATION` | تخصيص الموارد |
| الجدول | `readiness.allocations` | الجدول الرئيسي لتخصيص الموارد |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-007 | When a resource allocation is requested, the system shall verify authorization, type, availability, capacity,… |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-ALLOCATION-SM، TST-SLC09-INVARIANTS | دورة حالات تخصيص الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-Q-ALC-LIST -->

</details>

### 5.3 US-BC05-S-ALLOCATION-01 — تلقائي: all checks passed (تخصيص الموارد)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-S-ALLOCATION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:all checks passed` | SPEC-ALLOCATION §1 checks + capacity ledger reserve in priority order (§2) |
| الانتقال | REQUESTED ← COMMITTED | — |
| الحدث | `EVT-ALC-COMMITTED` | يصل إلى: Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| الكيان | `AGG-ALLOCATION` | تخصيص الموارد |
| الجدول | `readiness.allocations` | الجدول الرئيسي لتخصيص الموارد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-RES-007، REQ-RES-008، REQ-RES-009، REQ-RES-010، REQ-RES-011، REQ-RES-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-ALLOCATION-SM، TST-SLC09-INVARIANTS | دورة حالات تخصيص الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-S-ALLOCATION-01 -->

</details>

### 5.4 US-BC05-S-ALLOCATION-03 — تلقائي: a check failed (تخصيص الموارد)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-S-ALLOCATION-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:a check failed` | reason codes per failed check |
| الانتقال | REQUESTED ← REJECTED | — |
| الحدث | `EVT-ALC-REJECTED` | يصل إلى: Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| الكيان | `AGG-ALLOCATION` | تخصيص الموارد |
| الجدول | `readiness.allocations` | الجدول الرئيسي لتخصيص الموارد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-RES-007، REQ-RES-008، REQ-RES-009، REQ-RES-010، REQ-RES-011، REQ-RES-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-ALLOCATION-SM، TST-SLC09-INVARIANTS | دورة حالات تخصيص الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-S-ALLOCATION-03 -->

</details>

### 5.5 US-BC05-S-ALLOCATION-04 — تلقائي: provisional hold (1 h) elapsed (تخصيص الموارد)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-S-ALLOCATION-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:provisional hold (1 h) elapsed` | capacity released |
| الانتقال | PENDING_APPROVAL ← REJECTED | — |
| الحدث | `EVT-ALC-REJECTED` | يصل إلى: Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| الكيان | `AGG-ALLOCATION` | تخصيص الموارد |
| الجدول | `readiness.allocations` | الجدول الرئيسي لتخصيص الموارد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-RES-007، REQ-RES-008، REQ-RES-009، REQ-RES-010، REQ-RES-011، REQ-RES-012 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-ALLOCATION-SM، TST-SLC09-INVARIANTS | دورة حالات تخصيص الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-S-ALLOCATION-04 -->

</details>

### 5.6 US-UI-SCR41-ALLOCATION-LIST — قائمة التخصيصات مجمّعة حسب الحالة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR41-ALLOCATION-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-41 | شاشة المجمعات والتخصيص والجدول الزمني للسعة |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RES-007 | When a resource allocation is requested, the system shall verify authorization, type, availability, capacity,… |
| حالة الاستخدام | UC-054 | Allocate Resource |
<!-- END GENERATED: refs US-UI-SCR41-ALLOCATION-LIST -->

</details>

### 5.7 US-UI-SCR41-ALLOCATION-REQUEST — طلب تخصيص يبين سبب كل فحص فاشل

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR41-ALLOCATION-REQUEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-41 | شاشة المجمعات والتخصيص والجدول الزمني للسعة |
| المصدر | `21-ui-design.md §6.2` | — |
| المتطلب | REQ-RES-007 | When a resource allocation is requested, the system shall verify authorization, type, availability, capacity,… |
| حالة الاستخدام | UC-054 | Allocate Resource |
<!-- END GENERATED: refs US-UI-SCR41-ALLOCATION-REQUEST -->

</details>

### 5.8 US-PLT-ALC-CONTENTION — لا التزام فوق السعة مع الطلبات المتزامنة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-ALC-CONTENTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-RES-001 | 100 concurrent allocation requests on one pool → 0 over-commitment; deterministic priority order |
| المصدر | `23-crosscutting.md §5` | — |
| المتطلب | REQ-RES-008 | If two allocation requests compete for the same capacity, then the system shall commit at most the available… |
| حالة الاستخدام | UC-054 | Allocate Resource |
<!-- END GENERATED: refs US-PLT-ALC-CONTENTION -->

</details>

### 5.9 US-OPS-RES-NOTES-MIGRATION — ترحيل ملاحظات الموارد النصية إلى مراجع

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-RES-NOTES-MIGRATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `DEBT-001` | — |
| المتطلب | REQ-RES-012 | The system shall link resources and assets to tasks as structured references, replacing the text-only resourc… |
| حالة الاستخدام | UC-054 | Allocate Resource |
<!-- END GENERATED: refs US-OPS-RES-NOTES-MIGRATION -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RES-007 | When a resource allocation is requested, the system shall verify authorization, type, availability, capacity,… | `US-BC05-ALC-REQUEST`، `US-BC05-Q-ALC-LIST`، `US-BC05-S-ALLOCATION-01`، `US-BC05-S-ALLOCATION-03`، `US-BC05-S-ALLOCATION-04`، `US-UI-SCR41-ALLOCATION-LIST`، `US-UI-SCR41-ALLOCATION-REQUEST` | TST-ALLOCATION-SM، TST-SLC09-INVARIANTS |
| REQ-RES-008 | If two allocation requests compete for the same capacity, then the system shall commit at most the available… | `US-BC05-ALC-REQUEST`، `US-BC05-S-ALLOCATION-01`، `US-BC05-S-ALLOCATION-03`، `US-BC05-S-ALLOCATION-04`، `US-PLT-ALC-CONTENTION` | TST-ALLOCATION-SM، TST-SLC09-INVARIANTS |
| REQ-RES-009 | When a higher-priority allocation needs capacity already committed at lower priority, the system shall requir… | كل قصص الأوامر والنظام في الميزة (4) | TST-ALLOCATION-SM، TST-SLC09-INVARIANTS |
| REQ-RES-010 | The system shall record resource consumption against allocations with quantity, unit and time. | كل قصص الأوامر والنظام في الميزة (4) | TST-ALLOCATION-SM، TST-SLC09-INVARIANTS |
| REQ-RES-011 | When a task linked to an allocation reaches a terminal state, the system shall release the unused allocation. | كل قصص الأوامر والنظام في الميزة (4) | TST-ALLOCATION-SM، TST-SLC09-INVARIANTS |
| REQ-RES-012 | The system shall link resources and assets to tasks as structured references, replacing the text-only resourc… | `US-BC05-ALC-REQUEST`، `US-BC05-S-ALLOCATION-01`، `US-BC05-S-ALLOCATION-03`، `US-BC05-S-ALLOCATION-04`، `US-OPS-RES-NOTES-MIGRATION` | TST-ALLOCATION-SM، TST-ASSET-ASSIGNMENT-SM، TST-SLC09-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
