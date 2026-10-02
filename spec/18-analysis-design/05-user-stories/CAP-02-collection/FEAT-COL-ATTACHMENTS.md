---
id: FEAT-COL-ATTACHMENTS
type: feature
title: "رفع المرفقات وتنزيلها"
status: DRAFT
version: "0.1"
capability: CAP-02.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# رفع المرفقات وتنزيلها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-ATTACHMENTS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) |
| الأدوار | أي مستخدم مخوَّل؛ النظام |
| الشاشات | SCR-22 الادعاء والدليل والمصدر، SCR-23 الملاحظات |
| حالات الاستخدام | UC-005، UC-006، UC-103 |
| القصص | 16: 7 من المواصفة، و9 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح رفع الصور والمستندات والفيديو بأمان مع فحصها والتحقق من سلامتها وتنزيلها للمخولين فقط.

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
| `US-BC02-ATT-COMPLETE-UPLOAD` | إكمال رفع المرفق | أمر | مسودة |
| `US-BC02-ATT-ERASE` | محو المرفق | أمر | مسودة |
| `US-BC02-ATT-INITIATE-UPLOAD` | بدء رفع المرفق | أمر | مسودة |
| `US-BC02-Q-ATT-DOWNLOAD` | جلب: Short-lived signed download target (≤ 5 min); audited | جلب | مسودة |
| `US-BC02-S-ATTACHMENT-01` | تلقائي: scan passed (المرفق) | نظام | مسودة |
| `US-BC02-S-ATTACHMENT-02` | تلقائي: scan failed (المرفق) | نظام | مسودة |
| `US-BC02-S-ATTACHMENT-03` | تلقائي: upload window 24 h elapsed (المرفق) | نظام | مسودة |
| `US-UI-SCR22-SAFE-VIEWER` | معاينة المرفق في عارض معزول | واجهة | مسودة |
| `US-UI-SCR23-UPLOAD-STATE` | متابعة رفع المرفق وفحصه حتى إتاحته | واجهة | مسودة |
| `US-PLT-ATT-CONTENT-SCANNER` | فحص المرفقات محليًا قبل إتاحتها | منصة | مسودة |
| `US-PLT-ATT-DIRECT-UPLOAD` | رفع المرفقات مباشرة إلى مخزن الكائنات | منصة | مسودة |
| `US-PLT-ATT-INTEGRITY-CHECK` | التحقق من بصمة المرفق عند كل استرجاع | منصة | مسودة |
| `US-PLT-ATT-STORE-DEGRADED` | استمرار التسجيل عند تعطل مخزن الكائنات | منصة | مسودة |
| `US-OPS-ATT-QUARANTINE-REVIEW` | مراجعة أمنية لكل مرفق محجور | تشغيل | مسودة |
| `US-OPS-ATT-SCANNER-BACKLOG` | التنبيه عند تأخر فحص المرفقات | تشغيل | مسودة |
| `US-OPS-ATT-SCANNER-SIGNATURES` | تحديث تواقيع الماسح في بيئة معزولة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-ATT-COMPLETE-UPLOAD — إكمال رفع المرفق

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-ATT-COMPLETE-UPLOAD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/attachments/{id}/actions/complete-upload` | دون اتصال: نعم |
| الأمر | `CMD-ATT-COMPLETE-UPLOAD` | إكمال رفع المرفق |
| السياسة | `POL-ATT-COMPLETE-UPLOAD` | user with write permission on the target object؛ tenant match; object visible to subject (label ≤ clearance);… |
| الحدث | `EVT-ATT-UPLOADED` | يصل إلى: Content scanner; Evidence registrar |
| الكيان | `AGG-ATTACHMENT` | المرفق |
| الجدول | `information.attachments` | الجدول الرئيسي للمرفق |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-003، REQ-INF-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-005، UC-006 | Register Observation؛ Manage Evidence |
| الاختبار | TST-ATTACHMENT-SM، TST-SLC02-INVARIANTS | دورة حالات المرفق، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-ATT-COMPLETE-UPLOAD -->

</details>

### 5.2 US-BC02-ATT-ERASE — محو المرفق

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

<!-- BEGIN GENERATED: refs US-BC02-ATT-ERASE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/attachments/{id}/actions/erase` | — |
| الأمر | `CMD-ATT-ERASE` | محو المرفق |
| السياسة | `POL-ATT-ERASE` | user with write permission on the target object؛ tenant match; object visible to subject (label ≤ clearance);… |
| الحدث | `EVT-ATT-ERASED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-ATTACHMENT` | المرفق |
| الجدول | `information.attachments` | الجدول الرئيسي للمرفق |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-003، REQ-INF-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-005، UC-006 | Register Observation؛ Manage Evidence |
| الاختبار | TST-ATTACHMENT-SM، TST-SLC02-INVARIANTS | دورة حالات المرفق، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-ATT-ERASE -->

</details>

### 5.3 US-BC02-ATT-INITIATE-UPLOAD — بدء رفع المرفق

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R1 | Must | نعم | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC02-ATT-INITIATE-UPLOAD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/attachments` | دون اتصال: نعم |
| الأمر | `CMD-ATT-INITIATE-UPLOAD` | بدء رفع المرفق |
| السياسة | `POL-ATT-INITIATE-UPLOAD` | user with write permission on the target object؛ tenant match; object visible to subject (label ≤ clearance);… |
| الحدث | `EVT-ATT-UPLOAD-INITIATED` | يصل إلى: Content scanner; Evidence registrar |
| الكيان | `AGG-ATTACHMENT` | المرفق |
| الجدول | `information.attachments` | الجدول الرئيسي للمرفق |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-003، REQ-INF-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-005، UC-006 | Register Observation؛ Manage Evidence |
| الاختبار | TST-ATTACHMENT-SM، TST-SLC02-INVARIANTS | دورة حالات المرفق، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-ATT-INITIATE-UPLOAD -->

</details>

### 5.4 US-BC02-Q-ATT-DOWNLOAD — جلب: Short-lived signed download target (≤ 5 min); audited

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

<!-- BEGIN GENERATED: refs US-BC02-Q-ATT-DOWNLOAD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/attachments/{attachment_id}/download-grants` | — |
| الاستعلام | `QRY-ATT-DOWNLOAD` | Short-lived signed download target (≤ 5 min); audited |
| السياسة | `POL-ATT-DOWNLOAD` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-ATTACHMENT` | المرفق |
| الجدول | `information.attachments` | الجدول الرئيسي للمرفق |
| وحدة النشر | DU-05 | — |
| المتطلب | REQ-INF-004 | When an attachment is stored or retrieved, the system shall compute or verify its content hash. |
| حالة الاستخدام | UC-006 | Manage Evidence |
| الاختبار | TST-ATTACHMENT-SM، TST-SLC02-INVARIANTS | دورة حالات المرفق، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-ATT-DOWNLOAD -->

</details>

### 5.5 US-BC02-S-ATTACHMENT-01 — تلقائي: scan passed (المرفق)

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

<!-- BEGIN GENERATED: refs US-BC02-S-ATTACHMENT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:scan passed` | offline content scanner + format validation |
| الانتقال | SCANNING ← STORED | — |
| الحدث | `EVT-ATT-STORED` | يصل إلى: Content scanner; Evidence registrar |
| الكيان | `AGG-ATTACHMENT` | المرفق |
| الجدول | `information.attachments` | الجدول الرئيسي للمرفق |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-003، REQ-INF-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-005، UC-006 | Register Observation؛ Manage Evidence |
| الاختبار | TST-ATTACHMENT-SM، TST-SLC02-INVARIANTS | دورة حالات المرفق، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-S-ATTACHMENT-01 -->

</details>

### 5.6 US-BC02-S-ATTACHMENT-02 — تلقائي: scan failed (المرفق)

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

<!-- BEGIN GENERATED: refs US-BC02-S-ATTACHMENT-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:scan failed` | scanner verdict |
| الانتقال | SCANNING ← QUARANTINED | — |
| الحدث | `EVT-ATT-QUARANTINED` | يصل إلى: Content scanner; Evidence registrar |
| الكيان | `AGG-ATTACHMENT` | المرفق |
| الجدول | `information.attachments` | الجدول الرئيسي للمرفق |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-003، REQ-INF-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-005، UC-006 | Register Observation؛ Manage Evidence |
| الاختبار | TST-ATTACHMENT-SM، TST-SLC02-INVARIANTS | دورة حالات المرفق، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-S-ATTACHMENT-02 -->

</details>

### 5.7 US-BC02-S-ATTACHMENT-03 — تلقائي: upload window 24 h elapsed (المرفق)

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

<!-- BEGIN GENERATED: refs US-BC02-S-ATTACHMENT-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:upload window 24 h elapsed` | scheduler |
| الانتقال | PENDING ← EXPIRED | — |
| الحدث | `EVT-ATT-EXPIRED` | يصل إلى: Content scanner; Evidence registrar |
| الكيان | `AGG-ATTACHMENT` | المرفق |
| الجدول | `information.attachments` | الجدول الرئيسي للمرفق |
| وحدة النشر | DU-05 | — |
| المتطلبات | REQ-INF-003، REQ-INF-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-005، UC-006 | Register Observation؛ Manage Evidence |
| الاختبار | TST-ATTACHMENT-SM، TST-SLC02-INVARIANTS | دورة حالات المرفق، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-S-ATTACHMENT-03 -->

</details>

### 5.8 US-UI-SCR22-SAFE-VIEWER — معاينة المرفق في عارض معزول

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

<!-- BEGIN GENERATED: refs US-UI-SCR22-SAFE-VIEWER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-22 | شاشة الادعاء والدليل والمصدر |
| المصدر | `THR-S02-04` | — |
| المصدر | `THR-S02-05` | — |
| المصدر | `QRY-ATT-DOWNLOAD` | — |
<!-- END GENERATED: refs US-UI-SCR22-SAFE-VIEWER -->

</details>

### 5.9 US-UI-SCR23-UPLOAD-STATE — متابعة رفع المرفق وفحصه حتى إتاحته

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

<!-- BEGIN GENERATED: refs US-UI-SCR23-UPLOAD-STATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-23 | شاشة الملاحظات |
| المصدر | `AGG-ATTACHMENT` | — |
| المصدر | `FM-S02-02` | — |
| المصدر | `degradation-slc02.md` | — |
<!-- END GENERATED: refs US-UI-SCR23-UPLOAD-STATE -->

</details>

### 5.10 US-PLT-ATT-CONTENT-SCANNER — فحص المرفقات محليًا قبل إتاحتها

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

<!-- BEGIN GENERATED: refs US-PLT-ATT-CONTENT-SCANNER -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `THR-S02-04` | — |
| المصدر | `FM-S02-02` | — |
| فحص البنية | FIT-12 | No external network dependency at runtime or build (air-gapped) |
| المصدر | `17-security-design.md §6.1` | — |
<!-- END GENERATED: refs US-PLT-ATT-CONTENT-SCANNER -->

</details>

### 5.11 US-PLT-ATT-DIRECT-UPLOAD — رفع المرفقات مباشرة إلى مخزن الكائنات

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

<!-- BEGIN GENERATED: refs US-PLT-ATT-DIRECT-UPLOAD -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-06 | S3-compatible API as the contract; default implementation Ceph RGW (sites with Ceph) or MinIO (smaller cells)… |
| المصدر | `field-sync-protocol.md §1` | — |
| المتطلب | REQ-INF-003 | The system shall store attachments (documents, images, video, raster) in object storage and reference them by… |
| حالات الاستخدام | UC-005، UC-006 | Register Observation؛ Manage Evidence |
<!-- END GENERATED: refs US-PLT-ATT-DIRECT-UPLOAD -->

</details>

### 5.12 US-PLT-ATT-INTEGRITY-CHECK — التحقق من بصمة المرفق عند كل استرجاع

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

<!-- BEGIN GENERATED: refs US-PLT-ATT-INTEGRITY-CHECK -->
| البند | المعرّف | المعنى |
|---|---|---|
| المتطلب | REQ-INF-004 | When an attachment is stored or retrieved, the system shall compute or verify its content hash. |
| حالة الاستخدام | UC-006 | Manage Evidence |
<!-- END GENERATED: refs US-PLT-ATT-INTEGRITY-CHECK -->

</details>

### 5.13 US-PLT-ATT-STORE-DEGRADED — استمرار التسجيل عند تعطل مخزن الكائنات

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

<!-- BEGIN GENERATED: refs US-PLT-ATT-STORE-DEGRADED -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `degradation-slc02.md` | — |
| المصدر | `FM-S02-01` | — |
| المصدر | `FM-S02-08` | — |
<!-- END GENERATED: refs US-PLT-ATT-STORE-DEGRADED -->

</details>

### 5.14 US-OPS-ATT-QUARANTINE-REVIEW — مراجعة أمنية لكل مرفق محجور

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

<!-- BEGIN GENERATED: refs US-OPS-ATT-QUARANTINE-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc02.md` | — |
| المصدر | `THR-S02-04` | — |
<!-- END GENERATED: refs US-OPS-ATT-QUARANTINE-REVIEW -->

</details>

### 5.15 US-OPS-ATT-SCANNER-BACKLOG — التنبيه عند تأخر فحص المرفقات

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

<!-- BEGIN GENERATED: refs US-OPS-ATT-SCANNER-BACKLOG -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc02.md` | — |
| المصدر | `FM-S02-02` | — |
<!-- END GENERATED: refs US-OPS-ATT-SCANNER-BACKLOG -->

</details>

### 5.16 US-OPS-ATT-SCANNER-SIGNATURES — تحديث تواقيع الماسح في بيئة معزولة

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

<!-- BEGIN GENERATED: refs US-OPS-ATT-SCANNER-SIGNATURES -->
| البند | المعرّف | المعنى |
|---|---|---|
| فحص البنية | FIT-12 | No external network dependency at runtime or build (air-gapped) |
| القرار التقني | TD-17 | Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps… |
| المصدر | `THR-S02-04` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-ATT-SCANNER-SIGNATURES -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-003 | The system shall store attachments (documents, images, video, raster) in object storage and reference them by… | `US-BC02-ATT-COMPLETE-UPLOAD`، `US-BC02-ATT-ERASE`، `US-BC02-ATT-INITIATE-UPLOAD`، `US-BC02-S-ATTACHMENT-01`، `US-BC02-S-ATTACHMENT-02`، `US-BC02-S-ATTACHMENT-03`، `US-PLT-ATT-DIRECT-UPLOAD` | TST-ATTACHMENT-SM، TST-EVIDENCE-SM، TST-SLC02-INVARIANTS |
| REQ-INF-004 | When an attachment is stored or retrieved, the system shall compute or verify its content hash. | `US-BC02-ATT-COMPLETE-UPLOAD`، `US-BC02-ATT-ERASE`، `US-BC02-ATT-INITIATE-UPLOAD`، `US-BC02-Q-ATT-DOWNLOAD`، `US-BC02-S-ATTACHMENT-01`، `US-BC02-S-ATTACHMENT-02`، `US-BC02-S-ATTACHMENT-03`، `US-PLT-ATT-INTEGRITY-CHECK` | TST-ATTACHMENT-SM، TST-EVIDENCE-SM، TST-SLC02-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
