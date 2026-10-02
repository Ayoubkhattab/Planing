---
id: FEAT-COL-FULFILMENT
type: feature
title: "متابعة استيفاء المتطلبات"
status: DRAFT
version: "0.1"
capability: CAP-02.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# متابعة استيفاء المتطلبات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-FULFILMENT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2) |
| الأدوار | مدير الجمع؛ المحلل؛ النظام |
| الشاشات | SCR-13 لوحة الجمع |
| حالات الاستخدام | UC-122 |
| القصص | 7: 4 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعرض لوحة بالمتطلبات المفتوحة ومدى استيفائها والملاحظات التي أجابت عنها وينبه عند فوات موعدها.

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
| QAS-COL-001 | collection requirement fulfilment | 100 % of fulfilment links traceable to validated observations |
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
| `US-BC02-Q-CRQ-BOARD` | جلب: Requirements by area (bbox/polygon), state, priority, due | جلب | مسودة |
| `US-BC02-Q-CRQ-EVIDENCE` | جلب: Fulfilment links per EEI (visible observations only) with lineage | جلب | مسودة |
| `US-BC02-S-COLLECTION-REQUIREMENT-01` | تلقائي: validated observation matched (متطلب الجمع) | نظام | مسودة |
| `US-BC02-S-COLLECTION-REQUIREMENT-02` | تلقائي: due passed (متطلب الجمع) | نظام | مسودة |
| `US-UI-SCR13-BOARD-MAP` | لوحة مكانية للمتطلبات المفتوحة حسب الأولوية والموعد | واجهة | مسودة |
| `US-UI-SCR13-FULFILMENT-EEI` | عرض استيفاء كل عنصر معلومات بملاحظاته | واجهة | مسودة |
| `US-PLT-CRQ-MATCH-INDEX` | مطابقة الملاحظات المعتمدة مع مناطق المتطلبات بسرعة | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-Q-CRQ-BOARD — جلب: Requirements by area (bbox/polygon), state, priority, due

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

<!-- BEGIN GENERATED: refs US-BC02-Q-CRQ-BOARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/collection-requirements` | — |
| الاستعلام | `QRY-CRQ-BOARD` | Requirements by area (bbox/polygon), state, priority, due |
| السياسة | `POL-CRQ-BOARD` | allowed_scope |
| الكيان | `AGG-COLLECTION-REQUIREMENT` | متطلب الجمع |
| الجدول | `information.collection_requirements` | الجدول الرئيسي لمتطلب الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-001 | The system shall record information needs as collection requirements with question, area, time window, priori… |
| حالة الاستخدام | UC-120 | Define Collection Requirement |
| الاختبار | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS | دورة حالات متطلب الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-Q-CRQ-BOARD -->

</details>

### 5.2 US-BC02-Q-CRQ-EVIDENCE — جلب: Fulfilment links per EEI (visible observations only) with lineage

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

<!-- BEGIN GENERATED: refs US-BC02-Q-CRQ-EVIDENCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/collection-requirements/{requirement_id}/fulfilment` | — |
| الاستعلام | `QRY-CRQ-EVIDENCE` | Fulfilment links per EEI (visible observations only) with lineage |
| السياسة | `POL-CRQ-EVIDENCE` | requester, collection managers |
| الكيان | `AGG-COLLECTION-REQUIREMENT` | متطلب الجمع |
| الجدول | `information.collection_requirements` | الجدول الرئيسي لمتطلب الجمع |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-COL-003 | When observations answering a collection requirement are validated, the system shall update the requirement's… |
| حالة الاستخدام | UC-122 | Track Requirement Fulfilment |
| الاختبار | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS | دورة حالات متطلب الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-Q-CRQ-EVIDENCE -->

</details>

### 5.3 US-BC02-S-COLLECTION-REQUIREMENT-01 — تلقائي: validated observation matched (متطلب الجمع)

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

<!-- BEGIN GENERATED: refs US-BC02-S-COLLECTION-REQUIREMENT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:validated observation matched` | matching engine links observation to EEIs (SPEC-COLLECTION §2); fulfilment recomputed |
| الانتقال | APPROVED ← (بلا تغيير) | — |
| الحدث | `EVT-CRQ-FULFILMENT-UPDATED` | يصل إلى: Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| الكيان | `AGG-COLLECTION-REQUIREMENT` | متطلب الجمع |
| الجدول | `information.collection_requirements` | الجدول الرئيسي لمتطلب الجمع |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-COL-001، REQ-COL-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-122 | Track Requirement Fulfilment |
| الاختبار | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS | دورة حالات متطلب الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-S-COLLECTION-REQUIREMENT-01 -->

</details>

### 5.4 US-BC02-S-COLLECTION-REQUIREMENT-02 — تلقائي: due passed (متطلب الجمع)

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

<!-- BEGIN GENERATED: refs US-BC02-S-COLLECTION-REQUIREMENT-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:due passed` | scheduler; based on due date only (never on hidden fulfilment) |
| الانتقال | APPROVED ← EXPIRED | — |
| الحدث | `EVT-CRQ-EXPIRED` | يصل إلى: Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| الكيان | `AGG-COLLECTION-REQUIREMENT` | متطلب الجمع |
| الجدول | `information.collection_requirements` | الجدول الرئيسي لمتطلب الجمع |
| وحدة النشر | DU-04 | — |
| المتطلبات | REQ-COL-001، REQ-COL-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-122 | Track Requirement Fulfilment |
| الاختبار | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS | دورة حالات متطلب الجمع، وثوابت الشريحة SLC-14 |
<!-- END GENERATED: refs US-BC02-S-COLLECTION-REQUIREMENT-02 -->

</details>

### 5.5 US-UI-SCR13-BOARD-MAP — لوحة مكانية للمتطلبات المفتوحة حسب الأولوية والموعد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR13-BOARD-MAP -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-13 | شاشة لوحة الجمع |
| المصدر | `collection-spec.md §4` | — |
| المصدر | `21-ui-design.md §1` | — |
| القرار المعماري | ADR-P06 | Security Inside Projections |
<!-- END GENERATED: refs US-UI-SCR13-BOARD-MAP -->

</details>

### 5.6 US-UI-SCR13-FULFILMENT-EEI — عرض استيفاء كل عنصر معلومات بملاحظاته

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

<!-- BEGIN GENERATED: refs US-UI-SCR13-FULFILMENT-EEI -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-13 | شاشة لوحة الجمع |
| الجودة | QAS-COL-001 | collection requirement fulfilment → 100 % of fulfilment links traceable to validated observations |
| المصدر | `collection-spec.md §2` | — |
| المتطلب | REQ-COL-003 | When observations answering a collection requirement are validated, the system shall update the requirement's… |
| حالة الاستخدام | UC-122 | Track Requirement Fulfilment |
<!-- END GENERATED: refs US-UI-SCR13-FULFILMENT-EEI -->

</details>

### 5.7 US-PLT-CRQ-MATCH-INDEX — مطابقة الملاحظات المعتمدة مع مناطق المتطلبات بسرعة

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

<!-- BEGIN GENERATED: refs US-PLT-CRQ-MATCH-INDEX -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `collection-spec.md §2` | — |
| الجودة | QAS-COL-001 | collection requirement fulfilment → 100 % of fulfilment links traceable to validated observations |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-COL-003 | When observations answering a collection requirement are validated, the system shall update the requirement's… |
| حالة الاستخدام | UC-122 | Track Requirement Fulfilment |
<!-- END GENERATED: refs US-PLT-CRQ-MATCH-INDEX -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-COL-001 | The system shall record information needs as collection requirements with question, area, time window, priori… | `US-BC02-Q-CRQ-BOARD`، `US-BC02-S-COLLECTION-REQUIREMENT-01`، `US-BC02-S-COLLECTION-REQUIREMENT-02` | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS |
| REQ-COL-003 | When observations answering a collection requirement are validated, the system shall update the requirement's… | `US-BC02-Q-CRQ-EVIDENCE`، `US-BC02-S-COLLECTION-REQUIREMENT-01`، `US-BC02-S-COLLECTION-REQUIREMENT-02`، `US-PLT-CRQ-MATCH-INDEX`، `US-UI-SCR13-FULFILMENT-EEI` | TST-COLLECTION-REQUIREMENT-SM، TST-SLC14-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
