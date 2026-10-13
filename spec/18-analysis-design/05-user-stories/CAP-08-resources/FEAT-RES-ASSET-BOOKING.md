---
id: FEAT-RES-ASSET-BOOKING
type: feature
title: "حجز الأصول وتوفرها"
status: DRAFT
version: "0.1"
capability: CAP-08.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# حجز الأصول وتوفرها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-ASSET-BOOKING |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.01 إدارة الأصول (R2) |
| الأدوار | المخطِّط؛ مدير الموارد؛ النظام |
| الشاشات | SCR-40 الأصول وتوفرها والصيانة |
| حالات الاستخدام | UC-051، UC-052 |
| القصص | 11: 7 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يرى المخطط الأصول المتاحة في نافذة زمنية ويحجزها مسبقًا دون تعارض مع حجوزات أخرى.

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
| QAS-RES-002 | availability query for 1,000 assets over 30 days | p95 ≤ 1 s |
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
| `US-BC05-RSV-CANCEL` | إلغاء حجز الأصل | أمر | مسودة |
| `US-BC05-RSV-CONFIRM` | تأكيد حجز الأصل | أمر | مسودة |
| `US-BC05-RSV-HOLD` | إنشاء حجز الأصل مبدئيًا | أمر | مسودة |
| `US-BC05-RSV-RELEASE` | تحرير حجز الأصل | أمر | مسودة |
| `US-BC05-Q-AST-AVAILABILITY` | جلب: Assets of type/capability available in a window (and optional bbox), with blocking reasons for others visible to caller | جلب | مسودة |
| `US-BC05-S-ASSET-RESERVATION-01` | تلقائي: hold expiry (24 h) reached (حجز الأصل) | نظام | مسودة |
| `US-BC05-S-ASSET-RESERVATION-02` | تلقائي: linked task or plan terminal (حجز الأصل) | نظام | مسودة |
| `US-UI-SCR40-AVAILABILITY` | عرض توفر الأصول في نافذة زمنية | واجهة | مسودة |
| `US-UI-SCR40-RESERVE-HOLD` | الحجز المبدئي ومهلته ورسالة التعارض | واجهة | مسودة |
| `US-PLT-AST-AVAILABILITY-PERF` | استعلام توفر ألف أصل خلال ثانية | منصة | مسودة |
| `US-PLT-AST-EXCLUSION` | منع تداخل حجوزات الأصل تحت التزامن | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-RSV-CANCEL — إلغاء حجز الأصل

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

<!-- BEGIN GENERATED: refs US-BC05-RSV-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/asset-reservations/{id}/actions/cancel` | — |
| الأمر | `CMD-RSV-CANCEL` | إلغاء حجز الأصل |
| السياسة | `POL-RSV-CANCEL` | Planner / Resource Manager؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RSV-CANCELLED` | يصل إلى: Availability view |
| الكيان | `AGG-ASSET-RESERVATION` | حجز الأصل |
| الجدول | `readiness.asset_reservations` | الجدول الرئيسي لحجز الأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-014 | When an asset is reserved for a time window, the system shall reject any other reservation or assignment of t… |
| حالة الاستخدام | UC-052 | Reserve Asset |
| الاختبار | TST-ASSET-RESERVATION-SM، TST-SLC09-INVARIANTS | دورة حالات حجز الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RSV-CANCEL -->

</details>

### 5.2 US-BC05-RSV-CONFIRM — تأكيد حجز الأصل

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

<!-- BEGIN GENERATED: refs US-BC05-RSV-CONFIRM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/asset-reservations/{id}/actions/confirm` | — |
| الأمر | `CMD-RSV-CONFIRM` | تأكيد حجز الأصل |
| السياسة | `POL-RSV-CONFIRM` | Planner / Resource Manager؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RSV-CONFIRMED` | يصل إلى: Availability view |
| الكيان | `AGG-ASSET-RESERVATION` | حجز الأصل |
| الجدول | `readiness.asset_reservations` | الجدول الرئيسي لحجز الأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-014 | When an asset is reserved for a time window, the system shall reject any other reservation or assignment of t… |
| حالة الاستخدام | UC-052 | Reserve Asset |
| الاختبار | TST-ASSET-RESERVATION-SM، TST-SLC09-INVARIANTS | دورة حالات حجز الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RSV-CONFIRM -->

</details>

### 5.3 US-BC05-RSV-HOLD — إنشاء حجز الأصل مبدئيًا

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

<!-- BEGIN GENERATED: refs US-BC05-RSV-HOLD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/asset-reservations` | — |
| الأمر | `CMD-RSV-HOLD` | إنشاء حجز الأصل مبدئيًا |
| السياسة | `POL-RSV-HOLD` | Planner / Resource Manager؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RSV-HELD` | يصل إلى: Availability view |
| الكيان | `AGG-ASSET-RESERVATION` | حجز الأصل |
| الجدول | `readiness.asset_reservations` | الجدول الرئيسي لحجز الأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-014 | When an asset is reserved for a time window, the system shall reject any other reservation or assignment of t… |
| حالة الاستخدام | UC-052 | Reserve Asset |
| الاختبار | TST-ASSET-RESERVATION-SM، TST-SLC09-INVARIANTS | دورة حالات حجز الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RSV-HOLD -->

</details>

### 5.4 US-BC05-RSV-RELEASE — تحرير حجز الأصل

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

<!-- BEGIN GENERATED: refs US-BC05-RSV-RELEASE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/asset-reservations/{id}/actions/release` | — |
| الأمر | `CMD-RSV-RELEASE` | تحرير حجز الأصل |
| السياسة | `POL-RSV-RELEASE` | Planner / Resource Manager؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RSV-RELEASED` | يصل إلى: Availability view |
| الكيان | `AGG-ASSET-RESERVATION` | حجز الأصل |
| الجدول | `readiness.asset_reservations` | الجدول الرئيسي لحجز الأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-014 | When an asset is reserved for a time window, the system shall reject any other reservation or assignment of t… |
| حالة الاستخدام | UC-052 | Reserve Asset |
| الاختبار | TST-ASSET-RESERVATION-SM، TST-SLC09-INVARIANTS | دورة حالات حجز الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RSV-RELEASE -->

</details>

### 5.5 US-BC05-Q-AST-AVAILABILITY — جلب: Assets of type/capability available in a window (and optional bbox), with blocking reasons for others visible to caller

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

<!-- BEGIN GENERATED: refs US-BC05-Q-AST-AVAILABILITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/asset-availability-queries` | — |
| الاستعلام | `QRY-AST-AVAILABILITY` | Assets of type/capability available in a window (and optional bbox), with blocking reasons for others visible… |
| السياسة | `POL-AST-AVAILABILITY` | allowed_scope |
| الكيان | `AGG-ASSET` | الأصل |
| الجدول | `readiness.assets` | الجدول الرئيسي للأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-003 | When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavai… |
| حالة الاستخدام | UC-051 | Check Availability |
| الاختبار | TST-ASSET-SM، TST-SLC09-INVARIANTS | دورة حالات الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-Q-AST-AVAILABILITY -->

</details>

### 5.6 US-BC05-S-ASSET-RESERVATION-01 — تلقائي: hold expiry (24 h) reached (حجز الأصل)

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

<!-- BEGIN GENERATED: refs US-BC05-S-ASSET-RESERVATION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:hold expiry (24 h) reached` | scheduler |
| الانتقال | HELD ← EXPIRED | — |
| الحدث | `EVT-RSV-EXPIRED` | يصل إلى: Availability view |
| الكيان | `AGG-ASSET-RESERVATION` | حجز الأصل |
| الجدول | `readiness.asset_reservations` | الجدول الرئيسي لحجز الأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-014 | When an asset is reserved for a time window, the system shall reject any other reservation or assignment of t… |
| حالة الاستخدام | UC-052 | Reserve Asset |
| الاختبار | TST-ASSET-RESERVATION-SM، TST-SLC09-INVARIANTS | دورة حالات حجز الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-S-ASSET-RESERVATION-01 -->

</details>

### 5.7 US-BC05-S-ASSET-RESERVATION-02 — تلقائي: linked task or plan terminal (حجز الأصل)

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

<!-- BEGIN GENERATED: refs US-BC05-S-ASSET-RESERVATION-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:linked task or plan terminal` | SLC-03/SLC-08 events |
| الانتقال | CONFIRMED ← RELEASED | — |
| الحدث | `EVT-RSV-RELEASED` | يصل إلى: Availability view |
| الكيان | `AGG-ASSET-RESERVATION` | حجز الأصل |
| الجدول | `readiness.asset_reservations` | الجدول الرئيسي لحجز الأصل |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-014 | When an asset is reserved for a time window, the system shall reject any other reservation or assignment of t… |
| حالة الاستخدام | UC-052 | Reserve Asset |
| الاختبار | TST-ASSET-RESERVATION-SM، TST-SLC09-INVARIANTS | دورة حالات حجز الأصل، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-S-ASSET-RESERVATION-02 -->

</details>

### 5.8 US-UI-SCR40-AVAILABILITY — عرض توفر الأصول في نافذة زمنية

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

<!-- BEGIN GENERATED: refs US-UI-SCR40-AVAILABILITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-40 | شاشة الأصول وتوفرها والصيانة |
| المصدر | `17-security-design.md §12.9` | — |
| المتطلب | REQ-RES-004 | The system shall schedule and record maintenance for assets, and shall mark an asset under maintenance as una… |
| حالة الاستخدام | UC-051 | Check Availability |
<!-- END GENERATED: refs US-UI-SCR40-AVAILABILITY -->

</details>

### 5.9 US-UI-SCR40-RESERVE-HOLD — الحجز المبدئي ومهلته ورسالة التعارض

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

<!-- BEGIN GENERATED: refs US-UI-SCR40-RESERVE-HOLD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-40 | شاشة الأصول وتوفرها والصيانة |
| حالة الاستخدام | UC-052 | Reserve Asset |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RES-014 | When an asset is reserved for a time window, the system shall reject any other reservation or assignment of t… |
| حالة الاستخدام | UC-052 | Reserve Asset |
<!-- END GENERATED: refs US-UI-SCR40-RESERVE-HOLD -->

</details>

### 5.10 US-PLT-AST-AVAILABILITY-PERF — استعلام توفر ألف أصل خلال ثانية

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

<!-- BEGIN GENERATED: refs US-PLT-AST-AVAILABILITY-PERF -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-RES-002 | availability query for 1,000 assets over 30 days → p95 ≤ 1 s |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
<!-- END GENERATED: refs US-PLT-AST-AVAILABILITY-PERF -->

</details>

### 5.11 US-PLT-AST-EXCLUSION — منع تداخل حجوزات الأصل تحت التزامن

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

<!-- BEGIN GENERATED: refs US-PLT-AST-EXCLUSION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-RES-001 | 100 concurrent allocation requests on one pool → 0 over-commitment; deterministic priority order |
| المصدر | `23-crosscutting.md §5` | — |
| المتطلب | REQ-RES-014 | When an asset is reserved for a time window, the system shall reject any other reservation or assignment of t… |
| حالة الاستخدام | UC-052 | Reserve Asset |
<!-- END GENERATED: refs US-PLT-AST-EXCLUSION -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RES-003 | When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavai… | `US-BC05-Q-AST-AVAILABILITY` | TST-ASSET-ASSIGNMENT-SM، TST-ASSET-SM، TST-SLC09-INVARIANTS |
| REQ-RES-004 | The system shall schedule and record maintenance for assets, and shall mark an asset under maintenance as una… | `US-UI-SCR40-AVAILABILITY` | TST-MAINTENANCE-ORDER-SM، TST-SLC09-INVARIANTS |
| REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. | `US-PLT-AST-AVAILABILITY-PERF` | TST-RESOURCE-POOL-SM، TST-SLC09-INVARIANTS |
| REQ-RES-014 | When an asset is reserved for a time window, the system shall reject any other reservation or assignment of t… | `US-BC05-RSV-CANCEL`، `US-BC05-RSV-CONFIRM`، `US-BC05-RSV-HOLD`، `US-BC05-RSV-RELEASE`، `US-BC05-S-ASSET-RESERVATION-01`، `US-BC05-S-ASSET-RESERVATION-02`، `US-PLT-AST-EXCLUSION`، `US-UI-SCR40-RESERVE-HOLD` | TST-ASSET-RESERVATION-SM، TST-SLC09-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
