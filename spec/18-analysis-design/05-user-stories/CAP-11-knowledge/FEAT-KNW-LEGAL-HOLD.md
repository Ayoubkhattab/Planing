---
id: FEAT-KNW-LEGAL-HOLD
type: feature
title: "التجميد القانوني"
status: DRAFT
version: "0.1"
capability: CAP-11.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# التجميد القانوني

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-KNW-LEGAL-HOLD |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-11 المعرفة والذاكرة المؤسسية |
| القدرة الفرعية | CAP-11.02 السجلات والاحتفاظ (R1 (الاحتفاظ والتجميد)) |
| الأدوار | السلطة القانونية والامتثال؛ أمين الأرشيف؛ المدقِّق؛ النظام |
| الشاشات | SCR-70 الاحتفاظ والحجز القانوني والإتلاف والمحو |
| حالات الاستخدام | UC-103 |
| القصص | 11: 7 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يمنع إتلاف أو محو أو تعديل السجلات المطلوبة لقضية أو تحقيق حتى ترفع الجهة القانونية التجميد.

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
| QAS-GOV-001 | daily disposition evaluation | candidates computed ≤ 1 h; 0 held records destroyed |
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
| `US-BC08-LHD-APPROVE-RELEASE` | اعتماد رفع التجميد القانوني | أمر | مسودة |
| `US-BC08-LHD-CANCEL-RELEASE` | إلغاء طلب رفع التجميد القانوني | أمر | مسودة |
| `US-BC08-LHD-EXTEND` | تمديد التجميد القانوني | أمر | مسودة |
| `US-BC08-LHD-PLACE` | إنشاء التجميد القانوني | أمر | مسودة |
| `US-BC08-LHD-REQUEST-RELEASE` | طلب رفع التجميد القانوني | أمر | مسودة |
| `US-DOM-LEGALHOLD-BLOCK-MODIFY` | منع تعديل السجلات المجمدة | أمر | مسودة |
| `US-BC08-Q-LHD-CHECK` | جلب: HoldCheck OHS: URNs / subjects / (class, bucket) → held? with hold ids | جلب | مسودة |
| `US-BC08-Q-LHD-LIST` | جلب: Holds by state and scope | جلب | مسودة |
| `US-UI-SCR70-LEGAL-HOLD` | متابعة التجميدات القانونية والتحقق من سجل | واجهة | مسودة |
| `US-PLT-LEGALHOLD-CHECK-CACHE` | فحص التجميد في كل سياق مع الإغلاق عند التعطل | منصة | مسودة |
| `US-OPS-LEGALHOLD-BLOCKED-REPORT` | إبلاغ الجهة القانونية بمحاولات المساس بالمجمد | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC08-LHD-APPROVE-RELEASE — اعتماد رفع التجميد القانوني

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

<!-- BEGIN GENERATED: refs US-BC08-LHD-APPROVE-RELEASE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/legal-holds/{id}/actions/approve-release` | — |
| الأمر | `CMD-LHD-APPROVE-RELEASE` | اعتماد رفع التجميد القانوني |
| السياسة | `POL-LHD-APPROVE-RELEASE` | Legal/Compliance authority (place, extend, request/approve/cancel release)؛ tenant match |
| الحدث | `EVT-LHD-RELEASED` | يصل إلى: HoldCheck cache (all owners); Disposition planner; Erasure executor |
| الكيان | `AGG-LEGAL-HOLD` | التجميد القانوني |
| الجدول | `governance.legal_holds` | الجدول الرئيسي للتجميد القانوني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-LEGAL-HOLD-SM | دورة حالات التجميد القانوني، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-LHD-APPROVE-RELEASE -->

</details>

### 5.2 US-BC08-LHD-CANCEL-RELEASE — إلغاء طلب رفع التجميد القانوني

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

<!-- BEGIN GENERATED: refs US-BC08-LHD-CANCEL-RELEASE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/legal-holds/{id}/actions/cancel-release` | — |
| الأمر | `CMD-LHD-CANCEL-RELEASE` | إلغاء طلب رفع التجميد القانوني |
| السياسة | `POL-LHD-CANCEL-RELEASE` | Legal/Compliance authority (place, extend, request/approve/cancel release)؛ tenant match |
| الحدث | `EVT-LHD-RELEASE-CANCELLED` | يصل إلى: HoldCheck cache (all owners); Disposition planner; Erasure executor |
| الكيان | `AGG-LEGAL-HOLD` | التجميد القانوني |
| الجدول | `governance.legal_holds` | الجدول الرئيسي للتجميد القانوني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-LEGAL-HOLD-SM | دورة حالات التجميد القانوني، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-LHD-CANCEL-RELEASE -->

</details>

### 5.3 US-BC08-LHD-EXTEND — تمديد التجميد القانوني

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

<!-- BEGIN GENERATED: refs US-BC08-LHD-EXTEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/legal-holds/{id}/actions/extend` | — |
| الأمر | `CMD-LHD-EXTEND` | تمديد التجميد القانوني |
| السياسة | `POL-LHD-EXTEND` | Legal/Compliance authority (place, extend, request/approve/cancel release)؛ tenant match |
| الحدث | `EVT-LHD-EXTENDED` | يصل إلى: HoldCheck cache (all owners); Disposition planner; Erasure executor |
| الكيان | `AGG-LEGAL-HOLD` | التجميد القانوني |
| الجدول | `governance.legal_holds` | الجدول الرئيسي للتجميد القانوني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-LEGAL-HOLD-SM | دورة حالات التجميد القانوني، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-LHD-EXTEND -->

</details>

### 5.4 US-BC08-LHD-PLACE — إنشاء التجميد القانوني

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

<!-- BEGIN GENERATED: refs US-BC08-LHD-PLACE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/legal-holds` | — |
| الأمر | `CMD-LHD-PLACE` | إنشاء التجميد القانوني |
| السياسة | `POL-LHD-PLACE` | Legal/Compliance authority (place, extend, request/approve/cancel release)؛ tenant match |
| الحدث | `EVT-LHD-PLACED` | يصل إلى: HoldCheck cache (all owners); Disposition planner; Erasure executor |
| الكيان | `AGG-LEGAL-HOLD` | التجميد القانوني |
| الجدول | `governance.legal_holds` | الجدول الرئيسي للتجميد القانوني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-LEGAL-HOLD-SM | دورة حالات التجميد القانوني، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-LHD-PLACE -->

</details>

### 5.5 US-BC08-LHD-REQUEST-RELEASE — طلب رفع التجميد القانوني

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

<!-- BEGIN GENERATED: refs US-BC08-LHD-REQUEST-RELEASE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/legal-holds/{id}/actions/request-release` | — |
| الأمر | `CMD-LHD-REQUEST-RELEASE` | طلب رفع التجميد القانوني |
| السياسة | `POL-LHD-REQUEST-RELEASE` | Legal/Compliance authority (place, extend, request/approve/cancel release)؛ tenant match |
| الحدث | `EVT-LHD-RELEASE-REQUESTED` | يصل إلى: HoldCheck cache (all owners); Disposition planner; Erasure executor |
| الكيان | `AGG-LEGAL-HOLD` | التجميد القانوني |
| الجدول | `governance.legal_holds` | الجدول الرئيسي للتجميد القانوني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-LEGAL-HOLD-SM | دورة حالات التجميد القانوني، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-LHD-REQUEST-RELEASE -->

</details>

### 5.6 US-DOM-LEGALHOLD-BLOCK-MODIFY — منع تعديل السجلات المجمدة

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

<!-- BEGIN GENERATED: refs US-DOM-LEGALHOLD-BLOCK-MODIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| المصدر | `03-domain/contexts/BC01/aggregates/AGG-PERSON.md` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
<!-- END GENERATED: refs US-DOM-LEGALHOLD-BLOCK-MODIFY -->

</details>

### 5.7 US-BC08-Q-LHD-CHECK — جلب: HoldCheck OHS: URNs / subjects / (class, bucket) → held? with hold ids

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

<!-- BEGIN GENERATED: refs US-BC08-Q-LHD-CHECK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/hold-checks` | — |
| الاستعلام | `QRY-LHD-CHECK` | HoldCheck OHS: URNs / subjects / (class, bucket) → held? with hold ids |
| السياسة | `POL-LHD-CHECK` | owner contexts (workload identity); Archivist |
| الكيان | `AGG-LEGAL-HOLD` | التجميد القانوني |
| الجدول | `governance.legal_holds` | الجدول الرئيسي للتجميد القانوني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-LEGAL-HOLD-SM | دورة حالات التجميد القانوني، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-Q-LHD-CHECK -->

</details>

### 5.8 US-BC08-Q-LHD-LIST — جلب: Holds by state and scope

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

<!-- BEGIN GENERATED: refs US-BC08-Q-LHD-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/governance/legal-holds` | — |
| الاستعلام | `QRY-LHD-LIST` | Holds by state and scope |
| السياسة | `POL-LHD-LIST` | Legal, Archivist, Auditor |
| الكيان | `AGG-LEGAL-HOLD` | التجميد القانوني |
| الجدول | `governance.legal_holds` | الجدول الرئيسي للتجميد القانوني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الاختبار | TST-LEGAL-HOLD-SM | دورة حالات التجميد القانوني، وثوابت الشريحة SLC-12a |
<!-- END GENERATED: refs US-BC08-Q-LHD-LIST -->

</details>

### 5.9 US-UI-SCR70-LEGAL-HOLD — متابعة التجميدات القانونية والتحقق من سجل

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

<!-- BEGIN GENERATED: refs US-UI-SCR70-LEGAL-HOLD -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
| الشاشة | SCR-70 | شاشة الاحتفاظ والحجز القانوني والإتلاف والمحو |
| المصدر | `THR-S12-02` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
<!-- END GENERATED: refs US-UI-SCR70-LEGAL-HOLD -->

</details>

### 5.10 US-PLT-LEGALHOLD-CHECK-CACHE — فحص التجميد في كل سياق مع الإغلاق عند التعطل

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

<!-- BEGIN GENERATED: refs US-PLT-LEGALHOLD-CHECK-CACHE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `03-domain/contexts/BC08/events-slc12a.md` | — |
| المصدر | `09-reliability/fmea-slc12a.md FM-S12-02` | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
<!-- END GENERATED: refs US-PLT-LEGALHOLD-CHECK-CACHE -->

</details>

### 5.11 US-OPS-LEGALHOLD-BLOCKED-REPORT — إبلاغ الجهة القانونية بمحاولات المساس بالمجمد

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

<!-- BEGIN GENERATED: refs US-OPS-LEGALHOLD-BLOCKED-REPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-GOV-001 | daily disposition evaluation → candidates computed ≤ 1 h; 0 held records destroyed |
| المصدر | `THR-S12-01` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… |
| حالة الاستخدام | UC-103 | Apply Retention & Legal Hold |
<!-- END GENERATED: refs US-OPS-LEGALHOLD-BLOCKED-REPORT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modif… | `US-BC08-LHD-APPROVE-RELEASE`، `US-BC08-LHD-CANCEL-RELEASE`، `US-BC08-LHD-EXTEND`، `US-BC08-LHD-PLACE`، `US-BC08-LHD-REQUEST-RELEASE`، `US-BC08-Q-LHD-CHECK`، `US-BC08-Q-LHD-LIST`، `US-DOM-LEGALHOLD-BLOCK-MODIFY`، `US-OPS-LEGALHOLD-BLOCKED-REPORT`، `US-PLT-LEGALHOLD-CHECK-CACHE`، `US-UI-SCR70-LEGAL-HOLD` | TST-DISPOSITION-RUN-SM، TST-LEGAL-HOLD-SM، TST-SLC12A-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
