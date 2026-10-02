---
id: FEAT-ORG-HR-SYNC
type: feature
title: "مزامنة تغييرات الموارد البشرية"
status: DRAFT
version: "0.1"
capability: CAP-01.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مزامنة تغييرات الموارد البشرية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-HR-SYNC |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.02 الهوية والمصادقة والاتحاد (R1) |
| الأدوار | مسؤول الإدارة؛ مسؤول الأمن؛ النظام |
| الشاشات | SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-084 |
| القصص | 9: 6 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يحوّل تغييرات الوظيفة أو الوحدة القادمة من نظام الموارد البشرية إلى مقترحات يعتمدها المسؤول أو يرفضها قبل أن تتغير صلاحيات أي شخص.

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
| `US-BC01-HRS-APPROVE` | اعتماد مقترح مزامنة الموارد البشرية | أمر | مسودة |
| `US-BC01-HRS-REJECT` | رفض مقترح مزامنة الموارد البشرية | أمر | مسودة |
| `US-BC01-Q-HRS-QUEUE` | جلب: Pending HR proposals by unit and change kind (leave first) | جلب | مسودة |
| `US-BC01-S-HR-SYNC-PROPOSAL-01` | تلقائي: HRIS change received (مقترح مزامنة الموارد البشرية) | نظام | مسودة |
| `US-BC01-S-HR-SYNC-PROPOSAL-02` | تلقائي: newer HR change for the same person (مقترح مزامنة الموارد البشرية) | نظام | مسودة |
| `US-BC01-S-HR-SYNC-PROPOSAL-03` | تلقائي: 14 days without decision (مقترح مزامنة الموارد البشرية) | نظام | مسودة |
| `US-UI-SCR06-HR-PROPOSALS` | مراجعة مقترحات الموارد البشرية بالمقارنة | واجهة | مسودة |
| `US-INT-HRIS-CHANGE-PROPOSALS` | تحويل تغييرات الموارد البشرية إلى مقترحات | تكامل | مسودة |
| `US-INT-HRIS-LEAVER-ESCALATION` | تصعيد مغادرة الموظف إلى المسؤول | تكامل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-HRS-APPROVE — اعتماد مقترح مزامنة الموارد البشرية

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

<!-- BEGIN GENERATED: refs US-BC01-HRS-APPROVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/hr-sync-proposals/{id}/actions/approve` | — |
| الأمر | `CMD-HRS-APPROVE` | اعتماد مقترح مزامنة الموارد البشرية |
| السياسة | `POL-HRS-APPROVE` | Administrator in scope؛ tenant match |
| الحدث | `EVT-HRS-APPROVED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-HR-SYNC-PROPOSAL` | مقترح مزامنة الموارد البشرية |
| الجدول | `foundation.hr_sync_proposals` | الجدول الرئيسي لمقترح مزامنة الموارد البشرية |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-INT-004 | When HRIS reports a change of role or organization for a person, the system shall propose the corresponding r… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-HR-SYNC-PROPOSAL-SM، TST-SLC16-INVARIANTS | دورة حالات مقترح مزامنة الموارد البشرية، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC01-HRS-APPROVE -->

</details>

### 5.2 US-BC01-HRS-REJECT — رفض مقترح مزامنة الموارد البشرية

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

<!-- BEGIN GENERATED: refs US-BC01-HRS-REJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/hr-sync-proposals/{id}/actions/reject` | — |
| الأمر | `CMD-HRS-REJECT` | رفض مقترح مزامنة الموارد البشرية |
| السياسة | `POL-HRS-REJECT` | Administrator in scope؛ tenant match |
| الحدث | `EVT-HRS-REJECTED` | يصل إلى: Role assignments / users (BC01); Security Officer notification (leave) |
| الكيان | `AGG-HR-SYNC-PROPOSAL` | مقترح مزامنة الموارد البشرية |
| الجدول | `foundation.hr_sync_proposals` | الجدول الرئيسي لمقترح مزامنة الموارد البشرية |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-INT-004 | When HRIS reports a change of role or organization for a person, the system shall propose the corresponding r… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-HR-SYNC-PROPOSAL-SM، TST-SLC16-INVARIANTS | دورة حالات مقترح مزامنة الموارد البشرية، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC01-HRS-REJECT -->

</details>

### 5.3 US-BC01-Q-HRS-QUEUE — جلب: Pending HR proposals by unit and change kind (leave first)

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

<!-- BEGIN GENERATED: refs US-BC01-Q-HRS-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/foundation/hr-sync-proposals` | — |
| الاستعلام | `QRY-HRS-QUEUE` | Pending HR proposals by unit and change kind (leave first) |
| السياسة | `POL-HRS-QUEUE` | Administrator in scope, Security Officer |
| الكيان | `AGG-HR-SYNC-PROPOSAL` | مقترح مزامنة الموارد البشرية |
| الجدول | `foundation.hr_sync_proposals` | الجدول الرئيسي لمقترح مزامنة الموارد البشرية |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-INT-004 | When HRIS reports a change of role or organization for a person, the system shall propose the corresponding r… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-HR-SYNC-PROPOSAL-SM، TST-SLC16-INVARIANTS | دورة حالات مقترح مزامنة الموارد البشرية، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC01-Q-HRS-QUEUE -->

</details>

### 5.4 US-BC01-S-HR-SYNC-PROPOSAL-01 — تلقائي: HRIS change received (مقترح مزامنة الموارد البشرية)

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

<!-- BEGIN GENERATED: refs US-BC01-S-HR-SYNC-PROPOSAL-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:HRIS change received` | person matched to a platform Person by HR identifier; change ∈ {join, leave, move_unit, change_position}; map… |
| الانتقال | ∅ ← PROPOSED | — |
| الحدث | `EVT-HRS-PROPOSED` | يصل إلى: Role assignments / users (BC01); Security Officer notification (leave) |
| الكيان | `AGG-HR-SYNC-PROPOSAL` | مقترح مزامنة الموارد البشرية |
| الجدول | `foundation.hr_sync_proposals` | الجدول الرئيسي لمقترح مزامنة الموارد البشرية |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-INT-004 | When HRIS reports a change of role or organization for a person, the system shall propose the corresponding r… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-HR-SYNC-PROPOSAL-SM، TST-SLC16-INVARIANTS | دورة حالات مقترح مزامنة الموارد البشرية، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC01-S-HR-SYNC-PROPOSAL-01 -->

</details>

### 5.5 US-BC01-S-HR-SYNC-PROPOSAL-02 — تلقائي: newer HR change for the same person (مقترح مزامنة الموارد البشرية)

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

<!-- BEGIN GENERATED: refs US-BC01-S-HR-SYNC-PROPOSAL-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:newer HR change for the same person` | system |
| الانتقال | PROPOSED ← SUPERSEDED | — |
| الحدث | `EVT-HRS-SUPERSEDED` | يصل إلى: Role assignments / users (BC01); Security Officer notification (leave) |
| الكيان | `AGG-HR-SYNC-PROPOSAL` | مقترح مزامنة الموارد البشرية |
| الجدول | `foundation.hr_sync_proposals` | الجدول الرئيسي لمقترح مزامنة الموارد البشرية |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-INT-004 | When HRIS reports a change of role or organization for a person, the system shall propose the corresponding r… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-HR-SYNC-PROPOSAL-SM، TST-SLC16-INVARIANTS | دورة حالات مقترح مزامنة الموارد البشرية، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC01-S-HR-SYNC-PROPOSAL-02 -->

</details>

### 5.6 US-BC01-S-HR-SYNC-PROPOSAL-03 — تلقائي: 14 days without decision (مقترح مزامنة الموارد البشرية)

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

<!-- BEGIN GENERATED: refs US-BC01-S-HR-SYNC-PROPOSAL-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:14 days without decision` | scheduler; escalated to Security Officer for leave events |
| الانتقال | PROPOSED ← EXPIRED | — |
| الحدث | `EVT-HRS-EXPIRED` | يصل إلى: Role assignments / users (BC01); Security Officer notification (leave) |
| الكيان | `AGG-HR-SYNC-PROPOSAL` | مقترح مزامنة الموارد البشرية |
| الجدول | `foundation.hr_sync_proposals` | الجدول الرئيسي لمقترح مزامنة الموارد البشرية |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-INT-004 | When HRIS reports a change of role or organization for a person, the system shall propose the corresponding r… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-HR-SYNC-PROPOSAL-SM، TST-SLC16-INVARIANTS | دورة حالات مقترح مزامنة الموارد البشرية، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC01-S-HR-SYNC-PROPOSAL-03 -->

</details>

### 5.7 US-UI-SCR06-HR-PROPOSALS — مراجعة مقترحات الموارد البشرية بالمقارنة

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

<!-- BEGIN GENERATED: refs US-UI-SCR06-HR-PROPOSALS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INT-004 | When HRIS reports a change of role or organization for a person, the system shall propose the corresponding r… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
<!-- END GENERATED: refs US-UI-SCR06-HR-PROPOSALS -->

</details>

### 5.8 US-INT-HRIS-CHANGE-PROPOSALS — تحويل تغييرات الموارد البشرية إلى مقترحات

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

<!-- BEGIN GENERATED: refs US-INT-HRIS-CHANGE-PROPOSALS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §4` | — |
| المتطلب | REQ-INT-004 | When HRIS reports a change of role or organization for a person, the system shall propose the corresponding r… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
<!-- END GENERATED: refs US-INT-HRIS-CHANGE-PROPOSALS -->

</details>

### 5.9 US-INT-HRIS-LEAVER-ESCALATION — تصعيد مغادرة الموظف إلى المسؤول

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-HRIS-LEAVER-ESCALATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §4` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-INT-HRIS-LEAVER-ESCALATION -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INT-004 | When HRIS reports a change of role or organization for a person, the system shall propose the corresponding r… | `US-BC01-HRS-APPROVE`، `US-BC01-HRS-REJECT`، `US-BC01-Q-HRS-QUEUE`، `US-BC01-S-HR-SYNC-PROPOSAL-01`، `US-BC01-S-HR-SYNC-PROPOSAL-02`، `US-BC01-S-HR-SYNC-PROPOSAL-03`، `US-INT-HRIS-CHANGE-PROPOSALS`، `US-UI-SCR06-HR-PROPOSALS` | TST-HR-SYNC-PROPOSAL-SM، TST-SLC16-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
