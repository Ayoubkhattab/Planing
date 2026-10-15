---
id: FEAT-KNW-RECONSTRUCTION
type: feature
title: "إعادة البناء التاريخي"
status: DRAFT
version: "0.1"
capability: CAP-11.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إعادة البناء التاريخي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-KNW-RECONSTRUCTION |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-11 المعرفة والذاكرة المؤسسية |
| القدرة الفرعية | CAP-11.03 الأرشيف وإعادة البناء التاريخي (R2) |
| الأدوار | المدقِّق؛ السلطة القانونية والامتثال؛ المحلل؛ النظام |
| الشاشات | SCR-50 إعادة البناء التاريخي |
| حالات الاستخدام | UC-065 |
| القصص | 11: 6 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يجيب عن سؤال «ماذا كنا نعرف عن الوضع في وقت معيّن» بتقرير يميّز ما هو مسجل فعلًا عمّا أُعيد بناؤه.

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
| QAS-ARC-001 | retrieve an archived record | ≤ 1 min for warm, ≤ 24 h for cold/offline media |
| QAS-ARC-002 | historical reconstruction scenarios | 100 % agreement with oracle; every element labelled |
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
| `US-BC06-REC-CANCEL` | إلغاء إعادة البناء التاريخي | أمر | مسودة |
| `US-BC06-REC-REQUEST` | طلب إعادة البناء التاريخي | أمر | مسودة |
| `US-BC06-Q-REC-REPORT` | جلب: Labelled reconstruction report | جلب | مسودة |
| `US-BC06-S-RECONSTRUCTION-01` | تلقائي: worker started (إعادة البناء التاريخي) | نظام | مسودة |
| `US-BC06-S-RECONSTRUCTION-02` | تلقائي: completed (إعادة البناء التاريخي) | نظام | مسودة |
| `US-BC06-S-RECONSTRUCTION-03` | تلقائي: failed (إعادة البناء التاريخي) | نظام | مسودة |
| `US-UI-SCR50-LABELLED-REPORT` | تمييز المسجل عن المعاد بناؤه في التقرير | واجهة | مسودة |
| `US-UI-SCR50-REQUEST-FORM` | تحديد لحظة الموقف ولحظة المعرفة للطلب | واجهة | مسودة |
| `US-PLT-RECONSTRUCTION-ARCHIVE-READ` | إدخال السجلات المؤرشفة في إعادة البناء | منصة | مسودة |
| `US-PLT-RECONSTRUCTION-WORKER` | تنفيذ إعادة البناء مهمة غير متزامنة حتمية | منصة | مسودة |
| `US-OPS-RECONSTRUCTION-ORACLE-CHECK` | فحص دوري لمطابقة إعادة البناء للمرجع | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC06-REC-CANCEL — إلغاء إعادة البناء التاريخي

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

<!-- BEGIN GENERATED: refs US-BC06-REC-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/reconstructions/{id}/actions/cancel` | — |
| الأمر | `CMD-REC-CANCEL` | إلغاء إعادة البناء التاريخي |
| السياسة | `POL-REC-CANCEL` | Auditor / Legal / Analyst (request, cancel)؛ tenant match; object visible |
| الحدث | `EVT-REC-CANCELLED` | يصل إلى: Requester notification; Audit |
| الكيان | `AGG-RECONSTRUCTION` | إعادة البناء التاريخي |
| الجدول | `knowledge.reconstructions` | الجدول الرئيسي لإعادة البناء التاريخي |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
| الاختبار | TST-RECONSTRUCTION-SM، TST-SLC12-INVARIANTS | دورة حالات إعادة البناء التاريخي، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-REC-CANCEL -->

</details>

### 5.2 US-BC06-REC-REQUEST — طلب إعادة البناء التاريخي

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

<!-- BEGIN GENERATED: refs US-BC06-REC-REQUEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/knowledge/reconstructions` | — |
| الأمر | `CMD-REC-REQUEST` | طلب إعادة البناء التاريخي |
| السياسة | `POL-REC-REQUEST` | Auditor / Legal / Analyst (request, cancel)؛ tenant match; object visible |
| الحدث | `EVT-REC-REQUESTED` | يصل إلى: Requester notification; Audit |
| الكيان | `AGG-RECONSTRUCTION` | إعادة البناء التاريخي |
| الجدول | `knowledge.reconstructions` | الجدول الرئيسي لإعادة البناء التاريخي |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
| الاختبار | TST-RECONSTRUCTION-SM، TST-SLC12-INVARIANTS | دورة حالات إعادة البناء التاريخي، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-REC-REQUEST -->

</details>

### 5.3 US-BC06-Q-REC-REPORT — جلب: Labelled reconstruction report

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

<!-- BEGIN GENERATED: refs US-BC06-Q-REC-REPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/knowledge/reconstructions/{reconstruction_id}/report` | — |
| الاستعلام | `QRY-REC-REPORT` | Labelled reconstruction report |
| السياسة | `POL-REC-REPORT` | requester, Auditor |
| الكيان | `AGG-RECONSTRUCTION` | إعادة البناء التاريخي |
| الجدول | `knowledge.reconstructions` | الجدول الرئيسي لإعادة البناء التاريخي |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
| الاختبار | TST-RECONSTRUCTION-SM، TST-SLC12-INVARIANTS | دورة حالات إعادة البناء التاريخي، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-Q-REC-REPORT -->

</details>

### 5.4 US-BC06-S-RECONSTRUCTION-01 — تلقائي: worker started (إعادة البناء التاريخي)

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

<!-- BEGIN GENERATED: refs US-BC06-S-RECONSTRUCTION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:worker started` | runs with the requester's authority |
| الانتقال | REQUESTED ← RUNNING | — |
| الحدث | `EVT-REC-STARTED` | يصل إلى: Requester notification; Audit |
| الكيان | `AGG-RECONSTRUCTION` | إعادة البناء التاريخي |
| الجدول | `knowledge.reconstructions` | الجدول الرئيسي لإعادة البناء التاريخي |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
| الاختبار | TST-RECONSTRUCTION-SM، TST-SLC12-INVARIANTS | دورة حالات إعادة البناء التاريخي، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-RECONSTRUCTION-01 -->

</details>

### 5.5 US-BC06-S-RECONSTRUCTION-02 — تلقائي: completed (إعادة البناء التاريخي)

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

<!-- BEGIN GENERATED: refs US-BC06-S-RECONSTRUCTION-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:completed` | report: every element labelled RECORDED / RECONSTRUCTED / INFERRED (with rule) / UNKNOWN; archive retrievals… |
| الانتقال | RUNNING ← COMPLETED | — |
| الحدث | `EVT-REC-COMPLETED` | يصل إلى: Requester notification; Audit |
| الكيان | `AGG-RECONSTRUCTION` | إعادة البناء التاريخي |
| الجدول | `knowledge.reconstructions` | الجدول الرئيسي لإعادة البناء التاريخي |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
| الاختبار | TST-RECONSTRUCTION-SM، TST-SLC12-INVARIANTS | دورة حالات إعادة البناء التاريخي، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-RECONSTRUCTION-02 -->

</details>

### 5.6 US-BC06-S-RECONSTRUCTION-03 — تلقائي: failed (إعادة البناء التاريخي)

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

<!-- BEGIN GENERATED: refs US-BC06-S-RECONSTRUCTION-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:failed` | error recorded |
| الانتقال | RUNNING ← FAILED | — |
| الحدث | `EVT-REC-FAILED` | يصل إلى: Requester notification; Audit |
| الكيان | `AGG-RECONSTRUCTION` | إعادة البناء التاريخي |
| الجدول | `knowledge.reconstructions` | الجدول الرئيسي لإعادة البناء التاريخي |
| وحدة النشر | DU-15 | — |
| المتطلب | REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
| الاختبار | TST-RECONSTRUCTION-SM، TST-SLC12-INVARIANTS | دورة حالات إعادة البناء التاريخي، وثوابت الشريحة SLC-12 |
<!-- END GENERATED: refs US-BC06-S-RECONSTRUCTION-03 -->

</details>

### 5.7 US-UI-SCR50-LABELLED-REPORT — تمييز المسجل عن المعاد بناؤه في التقرير

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

<!-- BEGIN GENERATED: refs US-UI-SCR50-LABELLED-REPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §12` | — |
| المصدر | `21-ui-design.md §10` | — |
| الشاشة | SCR-50 | شاشة إعادة البناء التاريخي |
| المتطلب | REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
<!-- END GENERATED: refs US-UI-SCR50-LABELLED-REPORT -->

</details>

### 5.8 US-UI-SCR50-REQUEST-FORM — تحديد لحظة الموقف ولحظة المعرفة للطلب

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

<!-- BEGIN GENERATED: refs US-UI-SCR50-REQUEST-FORM -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
| الشاشة | SCR-50 | شاشة إعادة البناء التاريخي |
| المصدر | `US-BC06-REC-REQUEST` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
<!-- END GENERATED: refs US-UI-SCR50-REQUEST-FORM -->

</details>

### 5.9 US-PLT-RECONSTRUCTION-ARCHIVE-READ — إدخال السجلات المؤرشفة في إعادة البناء

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

<!-- BEGIN GENERATED: refs US-PLT-RECONSTRUCTION-ARCHIVE-READ -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `03-domain/contexts/BC06/products-knowledge-archive-spec.md §5` | — |
| المتطلبات | REQ-ARC-004، REQ-ARC-003 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
<!-- END GENERATED: refs US-PLT-RECONSTRUCTION-ARCHIVE-READ -->

</details>

### 5.10 US-PLT-RECONSTRUCTION-WORKER — تنفيذ إعادة البناء مهمة غير متزامنة حتمية

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

<!-- BEGIN GENERATED: refs US-PLT-RECONSTRUCTION-WORKER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-ARC-002 | historical reconstruction scenarios → 100 % agreement with oracle; every element labelled |
| المصدر | `03-domain/contexts/BC06/products-knowledge-archive-spec.md §5` | — |
| المتطلب | REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
<!-- END GENERATED: refs US-PLT-RECONSTRUCTION-WORKER -->

</details>

### 5.11 US-OPS-RECONSTRUCTION-ORACLE-CHECK — فحص دوري لمطابقة إعادة البناء للمرجع

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

<!-- BEGIN GENERATED: refs US-OPS-RECONSTRUCTION-ORACLE-CHECK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-ARC-002 | historical reconstruction scenarios → 100 % agreement with oracle; every element labelled |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… |
| حالة الاستخدام | UC-065 | Reconstruct Historical State |
<!-- END GENERATED: refs US-OPS-RECONSTRUCTION-ORACLE-CHECK -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-ARC-003 | When an authorized user requests a historical record, the system shall retrieve it within the archive retriev… | `US-PLT-RECONSTRUCTION-ARCHIVE-READ` | TST-ARCHIVE-PACKAGE-SM، TST-SLC12-INVARIANTS |
| REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the stat… | `US-BC06-Q-REC-REPORT`، `US-BC06-REC-CANCEL`، `US-BC06-REC-REQUEST`، `US-BC06-S-RECONSTRUCTION-01`، `US-BC06-S-RECONSTRUCTION-02`، `US-BC06-S-RECONSTRUCTION-03`، `US-OPS-RECONSTRUCTION-ORACLE-CHECK`، `US-PLT-RECONSTRUCTION-ARCHIVE-READ`، `US-PLT-RECONSTRUCTION-WORKER`، `US-UI-SCR50-LABELLED-REPORT`، `US-UI-SCR50-REQUEST-FORM` | TST-RECONSTRUCTION-SM، TST-SLC12-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
