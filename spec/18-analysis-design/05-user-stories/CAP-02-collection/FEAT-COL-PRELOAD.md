---
id: FEAT-COL-PRELOAD
type: feature
title: "تحميل بيانات المنطقة مسبقًا"
status: DRAFT
version: "0.1"
capability: CAP-02.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تحميل بيانات المنطقة مسبقًا

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-PRELOAD |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) |
| الأدوار | المستخدم الميداني؛ مسؤول الإدارة؛ مسؤول الأمن؛ النظام |
| الشاشات | SCR-63 الأجهزة، SCR-11 الصورة العملياتية المشتركة (COP) |
| حالات الاستخدام | UC-090، UC-093 |
| القصص | 14: 8 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمستخدم الميداني تنزيل بيانات منطقة عمله المصرح بها قبل الخروج لتعمل دون اتصال وتنتهي صلاحيتها تلقائيًا.

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
| QAS-OFF-002 | user's clearance reduced while device offline | packages revoked and purged on next contact; commands evaluated under current authorization |
| QAS-SEC-007 | obtains a field device | 0 readable records without authentication; wipe on next connection |
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
| `US-BC07-PKG-CONFIRM-DOWNLOAD` | تأكيد تنزيل حزمة التحميل المسبق | أمر | مسودة |
| `US-BC07-PKG-REQUEST` | طلب حزمة التحميل المسبق | أمر | مسودة |
| `US-BC07-PKG-REVOKE` | سحب حزمة التحميل المسبق | أمر | مسودة |
| `US-DOM-PKG-TENANT-LIMITS` | ضبط حدود حزم التحميل للمستأجر | أمر | مسودة |
| `US-BC07-Q-PKG-GET` | جلب: Package manifest and download target (signed, ≤ 5 min) | جلب | مسودة |
| `US-DOM-PKG-LIST` | عرض حزم مستخدم أو جهاز للمسؤول | جلب | مسودة |
| `US-BC07-S-PRELOAD-PACKAGE-01` | تلقائي: build started (حزمة التحميل المسبق) | نظام | مسودة |
| `US-BC07-S-PRELOAD-PACKAGE-02` | تلقائي: build finished (حزمة التحميل المسبق) | نظام | مسودة |
| `US-BC07-S-PRELOAD-PACKAGE-03` | تلقائي: expires_at reached (حزمة التحميل المسبق) | نظام | مسودة |
| `US-BC07-S-PRELOAD-PACKAGE-04` | تلقائي: user security_version changed or device not ACTIVE (حزمة التحميل المسبق) | نظام | مسودة |
| `US-UI-SCR11-PRELOAD-AREA` | اختيار منطقة العمل وتنزيل حزمتها | واجهة | مسودة |
| `US-UI-SCR63-DEVICE-PACKAGES` | عرض حزم الجهاز وسحبها | واجهة | مسودة |
| `US-PLT-PKG-BUILD` | بناء الحزمة بصلاحية المستخدم وقت البناء | منصة | مسودة |
| `US-PLT-PKG-DEVICE-PURGE` | إفراغ الحزم الملغاة والمنتهية من الجهاز | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-PKG-CONFIRM-DOWNLOAD — تأكيد تنزيل حزمة التحميل المسبق

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

<!-- BEGIN GENERATED: refs US-BC07-PKG-CONFIRM-DOWNLOAD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/field/preload-packages/{id}/actions/confirm-download` | — |
| الأمر | `CMD-PKG-CONFIRM-DOWNLOAD` | تأكيد تنزيل حزمة التحميل المسبق |
| السياسة | `POL-PKG-CONFIRM-DOWNLOAD` | field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)؛ tenant match; dev… |
| الحدث | `EVT-PKG-DOWNLOADED` | يصل إلى: Package builder; Sync delta (purge list) |
| الكيان | `AGG-PRELOAD-PACKAGE` | حزمة التحميل المسبق |
| الجدول | `field.preload_packages` | الجدول الرئيسي لحزمة التحميل المسبق |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-002، REQ-OFF-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-093 | Capture Observation Offline؛ Wipe Lost Device |
| الاختبار | TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS | دورة حالات حزمة التحميل المسبق، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-PKG-CONFIRM-DOWNLOAD -->

</details>

### 5.2 US-BC07-PKG-REQUEST — طلب حزمة التحميل المسبق

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

<!-- BEGIN GENERATED: refs US-BC07-PKG-REQUEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/field/preload-packages` | — |
| الأمر | `CMD-PKG-REQUEST` | طلب حزمة التحميل المسبق |
| السياسة | `POL-PKG-REQUEST` | field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)؛ tenant match; dev… |
| الحدث | `EVT-PKG-REQUESTED` | يصل إلى: Package builder; Sync delta (purge list) |
| الكيان | `AGG-PRELOAD-PACKAGE` | حزمة التحميل المسبق |
| الجدول | `field.preload_packages` | الجدول الرئيسي لحزمة التحميل المسبق |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-002، REQ-OFF-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-093 | Capture Observation Offline؛ Wipe Lost Device |
| الاختبار | TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS | دورة حالات حزمة التحميل المسبق، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-PKG-REQUEST -->

</details>

### 5.3 US-BC07-PKG-REVOKE — سحب حزمة التحميل المسبق

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

<!-- BEGIN GENERATED: refs US-BC07-PKG-REVOKE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/field/preload-packages/{id}/actions/revoke` | — |
| الأمر | `CMD-PKG-REVOKE` | سحب حزمة التحميل المسبق |
| السياسة | `POL-PKG-REVOKE` | field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)؛ tenant match; dev… |
| الحدث | `EVT-PKG-REVOKED` | يصل إلى: Package builder; Sync delta (purge list) |
| الكيان | `AGG-PRELOAD-PACKAGE` | حزمة التحميل المسبق |
| الجدول | `field.preload_packages` | الجدول الرئيسي لحزمة التحميل المسبق |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-002، REQ-OFF-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-093 | Capture Observation Offline؛ Wipe Lost Device |
| الاختبار | TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS | دورة حالات حزمة التحميل المسبق، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-PKG-REVOKE -->

</details>

### 5.4 US-DOM-PKG-TENANT-LIMITS — ضبط حدود حزم التحميل للمستأجر

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

<!-- BEGIN GENERATED: refs US-DOM-PKG-TENANT-LIMITS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `AGG-PRELOAD-PACKAGE` | — |
| المصدر | `POL-OFFLINE-PRELOAD` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OFF-002 | The system shall let field users preload authorized area-of-interest data, which shall respect the user's aut… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
<!-- END GENERATED: refs US-DOM-PKG-TENANT-LIMITS -->

</details>

### 5.5 US-BC07-Q-PKG-GET — جلب: Package manifest and download target (signed, ≤ 5 min)

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

<!-- BEGIN GENERATED: refs US-BC07-Q-PKG-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/field/preload-packages/{package_id}` | — |
| الاستعلام | `QRY-PKG-GET` | Package manifest and download target (signed, ≤ 5 min) |
| السياسة | `POL-PKG-GET` | package owner device + user |
| الكيان | `AGG-PRELOAD-PACKAGE` | حزمة التحميل المسبق |
| الجدول | `field.preload_packages` | الجدول الرئيسي لحزمة التحميل المسبق |
| وحدة النشر | DU-10 | — |
| المتطلب | REQ-OFF-002 | The system shall let field users preload authorized area-of-interest data, which shall respect the user's aut… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
| الاختبار | TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS | دورة حالات حزمة التحميل المسبق، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-Q-PKG-GET -->

</details>

### 5.6 US-DOM-PKG-LIST — عرض حزم مستخدم أو جهاز للمسؤول

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

<!-- BEGIN GENERATED: refs US-DOM-PKG-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `AGG-PRELOAD-PACKAGE` | — |
| المصدر | `CMD-PKG-REVOKE` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OFF-002 | The system shall let field users preload authorized area-of-interest data, which shall respect the user's aut… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
<!-- END GENERATED: refs US-DOM-PKG-LIST -->

</details>

### 5.7 US-BC07-S-PRELOAD-PACKAGE-01 — تلقائي: build started (حزمة التحميل المسبق)

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

<!-- BEGIN GENERATED: refs US-BC07-S-PRELOAD-PACKAGE-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:build started` | worker |
| الانتقال | REQUESTED ← BUILDING | — |
| الحدث | `EVT-PKG-BUILDING` | يصل إلى: Package builder; Sync delta (purge list) |
| الكيان | `AGG-PRELOAD-PACKAGE` | حزمة التحميل المسبق |
| الجدول | `field.preload_packages` | الجدول الرئيسي لحزمة التحميل المسبق |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-002، REQ-OFF-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-093 | Capture Observation Offline؛ Wipe Lost Device |
| الاختبار | TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS | دورة حالات حزمة التحميل المسبق، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-S-PRELOAD-PACKAGE-01 -->

</details>

### 5.8 US-BC07-S-PRELOAD-PACKAGE-02 — تلقائي: build finished (حزمة التحميل المسبق)

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

<!-- BEGIN GENERATED: refs US-BC07-S-PRELOAD-PACKAGE-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:build finished` | content = objects visible to the user at build time and ≤ requested level; manifest with hashes, labels, secu… |
| الانتقال | BUILDING ← READY | — |
| الحدث | `EVT-PKG-READY` | يصل إلى: Package builder; Sync delta (purge list) |
| الكيان | `AGG-PRELOAD-PACKAGE` | حزمة التحميل المسبق |
| الجدول | `field.preload_packages` | الجدول الرئيسي لحزمة التحميل المسبق |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-002، REQ-OFF-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-093 | Capture Observation Offline؛ Wipe Lost Device |
| الاختبار | TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS | دورة حالات حزمة التحميل المسبق، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-S-PRELOAD-PACKAGE-02 -->

</details>

### 5.9 US-BC07-S-PRELOAD-PACKAGE-03 — تلقائي: expires_at reached (حزمة التحميل المسبق)

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

<!-- BEGIN GENERATED: refs US-BC07-S-PRELOAD-PACKAGE-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:expires_at reached` | device purges at expiry (local enforcement) and confirms on next contact |
| الانتقال | READY, DOWNLOADED ← EXPIRED | — |
| الحدث | `EVT-PKG-EXPIRED` | يصل إلى: Package builder; Sync delta (purge list) |
| الكيان | `AGG-PRELOAD-PACKAGE` | حزمة التحميل المسبق |
| الجدول | `field.preload_packages` | الجدول الرئيسي لحزمة التحميل المسبق |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-002، REQ-OFF-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-093 | Capture Observation Offline؛ Wipe Lost Device |
| الاختبار | TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS | دورة حالات حزمة التحميل المسبق، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-S-PRELOAD-PACKAGE-03 -->

</details>

### 5.10 US-BC07-S-PRELOAD-PACKAGE-04 — تلقائي: user security_version changed or device not ACTIVE (حزمة التحميل المسبق)

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

<!-- BEGIN GENERATED: refs US-BC07-S-PRELOAD-PACKAGE-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:user security_version changed or device not ACTIVE` | purge instruction on next contact |
| الانتقال | REQUESTED, BUILDING, READY, DOWNLOADED ← REVOKED | — |
| الحدث | `EVT-PKG-REVOKED` | يصل إلى: Package builder; Sync delta (purge list) |
| الكيان | `AGG-PRELOAD-PACKAGE` | حزمة التحميل المسبق |
| الجدول | `field.preload_packages` | الجدول الرئيسي لحزمة التحميل المسبق |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-002، REQ-OFF-005 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-093 | Capture Observation Offline؛ Wipe Lost Device |
| الاختبار | TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS | دورة حالات حزمة التحميل المسبق، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-S-PRELOAD-PACKAGE-04 -->

</details>

### 5.11 US-UI-SCR11-PRELOAD-AREA — اختيار منطقة العمل وتنزيل حزمتها

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

<!-- BEGIN GENERATED: refs US-UI-SCR11-PRELOAD-AREA -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-11 | شاشة الصورة العملياتية المشتركة (COP) |
| المصدر | `21-ui-design.md §8.1` | — |
| المصدر | `AGG-PRELOAD-PACKAGE` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OFF-002 | The system shall let field users preload authorized area-of-interest data, which shall respect the user's aut… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
<!-- END GENERATED: refs US-UI-SCR11-PRELOAD-AREA -->

</details>

### 5.12 US-UI-SCR63-DEVICE-PACKAGES — عرض حزم الجهاز وسحبها

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

<!-- BEGIN GENERATED: refs US-UI-SCR63-DEVICE-PACKAGES -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-63 | شاشة الأجهزة |
| المصدر | `US-BC07-PKG-REVOKE` | — |
| الجودة | QAS-OFF-002 | user's clearance reduced while device offline → packages revoked and purged on next contact; commands evaluat… |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR63-DEVICE-PACKAGES -->

</details>

### 5.13 US-PLT-PKG-BUILD — بناء الحزمة بصلاحية المستخدم وقت البناء

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

<!-- BEGIN GENERATED: refs US-PLT-PKG-BUILD -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `THR-S11-06` | — |
| القرار التقني | TD-10 | Dynamic operational vector tiles from PostGIS (ST_AsMVT) via Martin tile server with scope-keyed cache; base… |
| المتطلبات | REQ-OFF-002، REQ-PLT-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
<!-- END GENERATED: refs US-PLT-PKG-BUILD -->

</details>

### 5.14 US-PLT-PKG-DEVICE-PURGE — إفراغ الحزم الملغاة والمنتهية من الجهاز

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

<!-- BEGIN GENERATED: refs US-PLT-PKG-DEVICE-PURGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-OFF-002 | user's clearance reduced while device offline → packages revoked and purged on next contact; commands evaluat… |
| المصدر | `field-sync-protocol.md §4` | — |
| المتطلب | REQ-OFF-002 | The system shall let field users preload authorized area-of-interest data, which shall respect the user's aut… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
<!-- END GENERATED: refs US-PLT-PKG-DEVICE-PURGE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OFF-002 | The system shall let field users preload authorized area-of-interest data, which shall respect the user's aut… | `US-BC07-PKG-CONFIRM-DOWNLOAD`، `US-BC07-PKG-REQUEST`، `US-BC07-PKG-REVOKE`، `US-BC07-Q-PKG-GET`، `US-BC07-S-PRELOAD-PACKAGE-01`، `US-BC07-S-PRELOAD-PACKAGE-02`، `US-BC07-S-PRELOAD-PACKAGE-03`، `US-BC07-S-PRELOAD-PACKAGE-04`، `US-DOM-PKG-LIST`، `US-DOM-PKG-TENANT-LIMITS`، `US-PLT-PKG-BUILD`، `US-PLT-PKG-DEVICE-PURGE`، `US-UI-SCR11-PRELOAD-AREA` | TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS |
| REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. | كل قصص الأوامر والنظام في الميزة (7) | TST-DEVICE-SM، TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS |
| REQ-PLT-005 | The system shall run heavy operations (raster processing, bulk import, analysis runs, reconstruction, report… | `US-PLT-PKG-BUILD` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
