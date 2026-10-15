---
id: FEAT-PLT-BACKUP-RESTORE
type: feature
title: "النسخ الاحتياطي والاستعادة"
status: DRAFT
version: "0.1"
capability: CAP-14.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# النسخ الاحتياطي والاستعادة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-PLT-BACKUP-RESTORE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-14 تشغيل المنصة |
| القدرة الفرعية | CAP-14.02 الاعتمادية والتعافي (R1) |
| الأدوار | مشغّل المنصة؛ النظام |
| الشاشات | — |
| حالات الاستخدام | — |
| القصص | 8: 0 من المواصفة، و8 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضمن نسخ جميع البيانات احتياطيًا حسب أهميتها والتحقق آليًا من إمكانية استعادتها ضمن المدد المتفق عليها.

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
| QAS-AVL-001 | normal operation over a month | ≥ 99.9 % monthly |
| QAS-AVL-002 | normal operation over a month | ≥ 99.5 % monthly |
| QAS-AVL-003 | normal operation over a month | ≥ 99 % monthly |
| QAS-PRV-002 | restore of a key-store backup older than a key destruction | destroyed keys unusable before any service reads data (restore gate) |
| QAS-REC-001 | primary site lost | RPO ≤ 5 min; RTO ≤ 1 h |
| QAS-REC-002 | primary site lost | RPO ≤ 15 min; RTO ≤ 4 h |
| QAS-REC-003 | primary site lost | RPO ≤ 24 h; RTO ≤ 24 h |
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
| `US-PLT-BACKUP-KEYSTORE` | نسخ مخزن المفاتيح مع سجل الإتلاف | منصة | مسودة |
| `US-PLT-BACKUP-SEARCH-SNAPSHOTS` | لقطات فهارس البحث كل ربع ساعة | منصة | مسودة |
| `US-PLT-BACKUP-STORES` | نسخ كل المخازن حسب طبقة خدمتها | منصة | مسودة |
| `US-OPS-BACKUP-RESTORE-GATE` | منع عودة المفاتيح المتلفة بعد الاستعادة | تشغيل | مسودة |
| `US-OPS-BACKUP-RESTORE-TEST` | اختبار استعادة آلي أسبوعي | تشغيل | مسودة |
| `US-OPS-DR-QUARTERLY-DRILL` | تمرين تعافٍ ربع سنوي ضمن الأهداف | تشغيل | مسودة |
| `US-OPS-DR-TIER-ASSIGNMENT` | طبقة خدمة محددة لكل قدرة | تشغيل | مسودة |
| `US-OPS-HA-REDUNDANCY` | نسختان على الأقل لكل وحدة حرجة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-PLT-BACKUP-KEYSTORE — نسخ مخزن المفاتيح مع سجل الإتلاف

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

<!-- BEGIN GENERATED: refs US-PLT-BACKUP-KEYSTORE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §5` | — |
| المصدر | `17-security-design.md §6.1` | — |
<!-- END GENERATED: refs US-PLT-BACKUP-KEYSTORE -->

</details>

### 5.2 US-PLT-BACKUP-SEARCH-SNAPSHOTS — لقطات فهارس البحث كل ربع ساعة

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

<!-- BEGIN GENERATED: refs US-PLT-BACKUP-SEARCH-SNAPSHOTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/dr-and-continuity.md §3` | — |
| الجودة | QAS-REC-002 | primary site lost → RPO ≤ 15 min; RTO ≤ 4 h |
<!-- END GENERATED: refs US-PLT-BACKUP-SEARCH-SNAPSHOTS -->

</details>

### 5.3 US-PLT-BACKUP-STORES — نسخ كل المخازن حسب طبقة خدمتها

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

<!-- BEGIN GENERATED: refs US-PLT-BACKUP-STORES -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §5` | — |
| المصدر | `09-reliability/dr-and-continuity.md §2` | — |
| المتطلب | REQ-PLT-012 | The system shall back up all stores according to their service tier and shall verify restores automatically. |
<!-- END GENERATED: refs US-PLT-BACKUP-STORES -->

</details>

### 5.4 US-OPS-BACKUP-RESTORE-GATE — منع عودة المفاتيح المتلفة بعد الاستعادة

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

<!-- BEGIN GENERATED: refs US-OPS-BACKUP-RESTORE-GATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| فحص البنية | FIT-19 | Restore gate: after any key-store restore, every key in the destruction log is unusable before services start |
| الجودة | QAS-PRV-002 | restore of a key-store backup older than a key destruction → destroyed keys unusable before any service reads… |
| المصدر | `17-security-design.md §6` | — |
<!-- END GENERATED: refs US-OPS-BACKUP-RESTORE-GATE -->

</details>

### 5.5 US-OPS-BACKUP-RESTORE-TEST — اختبار استعادة آلي أسبوعي

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

<!-- BEGIN GENERATED: refs US-OPS-BACKUP-RESTORE-TEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-REC-001 | primary site lost → RPO ≤ 5 min; RTO ≤ 1 h |
| المصدر | `09-reliability/dr-and-continuity.md §2` | — |
| المتطلب | REQ-PLT-012 | The system shall back up all stores according to their service tier and shall verify restores automatically. |
<!-- END GENERATED: refs US-OPS-BACKUP-RESTORE-TEST -->

</details>

### 5.6 US-OPS-DR-QUARTERLY-DRILL — تمرين تعافٍ ربع سنوي ضمن الأهداف

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

<!-- BEGIN GENERATED: refs US-OPS-DR-QUARTERLY-DRILL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-REC-001 | primary site lost → RPO ≤ 5 min; RTO ≤ 1 h |
| الجودة | QAS-REC-002 | primary site lost → RPO ≤ 15 min; RTO ≤ 4 h |
| الجودة | QAS-REC-003 | primary site lost → RPO ≤ 24 h; RTO ≤ 24 h |
| المتطلب | REQ-PLT-004 | The system shall assign every capability to one of the service tiers defined in QAS-AVL-001..003 (critical, i… |
<!-- END GENERATED: refs US-OPS-DR-QUARTERLY-DRILL -->

</details>

### 5.7 US-OPS-DR-TIER-ASSIGNMENT — طبقة خدمة محددة لكل قدرة

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

<!-- BEGIN GENERATED: refs US-OPS-DR-TIER-ASSIGNMENT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/dr-and-continuity.md §1` | — |
| المتطلب | REQ-PLT-004 | The system shall assign every capability to one of the service tiers defined in QAS-AVL-001..003 (critical, i… |
<!-- END GENERATED: refs US-OPS-DR-TIER-ASSIGNMENT -->

</details>

### 5.8 US-OPS-HA-REDUNDANCY — نسختان على الأقل لكل وحدة حرجة

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

<!-- BEGIN GENERATED: refs US-OPS-HA-REDUNDANCY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AVL-001 | normal operation over a month → ≥ 99.9 % monthly |
| المصدر | `22-deployment-design.md §3` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-HA-REDUNDANCY -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-PLT-004 | The system shall assign every capability to one of the service tiers defined in QAS-AVL-001..003 (critical, i… | `US-OPS-DR-QUARTERLY-DRILL`، `US-OPS-DR-TIER-ASSIGNMENT` | — |
| REQ-PLT-012 | The system shall back up all stores according to their service tier and shall verify restores automatically. | `US-OPS-BACKUP-RESTORE-TEST`، `US-PLT-BACKUP-STORES` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
