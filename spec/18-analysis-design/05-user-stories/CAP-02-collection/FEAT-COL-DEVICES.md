---
id: FEAT-COL-DEVICES
type: feature
title: "إدارة الأجهزة الميدانية"
status: DRAFT
version: "0.1"
capability: CAP-02.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة الأجهزة الميدانية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-DEVICES |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) |
| الأدوار | المستخدم الميداني؛ مسؤول الإدارة؛ مسؤول الأمن |
| الشاشات | SCR-63 الأجهزة |
| حالات الاستخدام | UC-093 |
| القصص | 12: 7 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح تسجيل الأجهزة الميدانية واعتمادها وتعليقها وتدوير مفاتيحها حتى لا يعمل في الميدان إلا جهاز موثوق.

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
| `US-BC01-DEV-CONFIRM` | تأكيد الجهاز الميداني | أمر | مسودة |
| `US-BC01-DEV-ENROLL` | تسجيل الجهاز الميداني | أمر | مسودة |
| `US-BC01-DEV-REINSTATE` | إعادة الجهاز الميداني إلى السريان | أمر | مسودة |
| `US-BC01-DEV-RETIRE` | إحالة الجهاز الميداني إلى التقاعد | أمر | مسودة |
| `US-BC01-DEV-ROTATE-KEY` | تدوير مفتاح الجهاز الميداني | أمر | مسودة |
| `US-BC01-DEV-SUSPEND` | تعليق الجهاز الميداني | أمر | مسودة |
| `US-BC01-Q-DEV-LIST` | جلب: Devices of a user (self) or in scope (Administrator) | جلب | مسودة |
| `US-UI-SCR63-DEVICE-LIST` | قائمة الأجهزة وحالتها وآخر مزامنة | واجهة | مسودة |
| `US-UI-SCR63-ENROLL-CONFIRM` | تأكيد تسجيل جهاز جديد بعد التحقق منه | واجهة | مسودة |
| `US-PLT-DEVICE-ATTESTATION` | مفتاح جهاز عتادي غير قابل للتصدير مع إثبات | منصة | مسودة |
| `US-INT-MDM-COMPLIANCE` | قبول الجهاز بناءً على امتثال إدارة الأجهزة | تكامل | مسودة |
| `US-OPS-FIELDAPP-RELEASE` | توزيع إصدارات التطبيق الميداني الموقّعة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-DEV-CONFIRM — تأكيد الجهاز الميداني

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

<!-- BEGIN GENERATED: refs US-BC01-DEV-CONFIRM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/devices/{id}/actions/confirm` | — |
| الأمر | `CMD-DEV-CONFIRM` | تأكيد الجهاز الميداني |
| السياسة | `POL-DEV-CONFIRM` | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Offi… |
| الحدث | `EVT-DEV-ACTIVATED` | يصل إلى: Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version… |
| الكيان | `AGG-DEVICE` | الجهاز الميداني |
| الجدول | `foundation.devices` | الجدول الرئيسي للجهاز الميداني |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| الاختبار | TST-DEVICE-SM، TST-SLC11-INVARIANTS | دورة حالات الجهاز الميداني، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC01-DEV-CONFIRM -->

</details>

### 5.2 US-BC01-DEV-ENROLL — تسجيل الجهاز الميداني

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

<!-- BEGIN GENERATED: refs US-BC01-DEV-ENROLL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/devices` | — |
| الأمر | `CMD-DEV-ENROLL` | تسجيل الجهاز الميداني |
| السياسة | `POL-DEV-ENROLL` | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Offi… |
| الحدث | `EVT-DEV-ENROLL-REQUESTED` | يصل إلى: Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version… |
| الكيان | `AGG-DEVICE` | الجهاز الميداني |
| الجدول | `foundation.devices` | الجدول الرئيسي للجهاز الميداني |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| الاختبار | TST-DEVICE-SM، TST-SLC11-INVARIANTS | دورة حالات الجهاز الميداني، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC01-DEV-ENROLL -->

</details>

### 5.3 US-BC01-DEV-REINSTATE — إعادة الجهاز الميداني إلى السريان

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

<!-- BEGIN GENERATED: refs US-BC01-DEV-REINSTATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/devices/{id}/actions/reinstate` | — |
| الأمر | `CMD-DEV-REINSTATE` | إعادة الجهاز الميداني إلى السريان |
| السياسة | `POL-DEV-REINSTATE` | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Offi… |
| الحدث | `EVT-DEV-REINSTATED` | يصل إلى: Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version… |
| الكيان | `AGG-DEVICE` | الجهاز الميداني |
| الجدول | `foundation.devices` | الجدول الرئيسي للجهاز الميداني |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| الاختبار | TST-DEVICE-SM، TST-SLC11-INVARIANTS | دورة حالات الجهاز الميداني، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC01-DEV-REINSTATE -->

</details>

### 5.4 US-BC01-DEV-RETIRE — إحالة الجهاز الميداني إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC01-DEV-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/devices/{id}/actions/retire` | — |
| الأمر | `CMD-DEV-RETIRE` | إحالة الجهاز الميداني إلى التقاعد |
| السياسة | `POL-DEV-RETIRE` | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Offi… |
| الحدث | `EVT-DEV-RETIRED` | يصل إلى: Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version… |
| الكيان | `AGG-DEVICE` | الجهاز الميداني |
| الجدول | `foundation.devices` | الجدول الرئيسي للجهاز الميداني |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| الاختبار | TST-DEVICE-SM، TST-SLC11-INVARIANTS | دورة حالات الجهاز الميداني، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC01-DEV-RETIRE -->

</details>

### 5.5 US-BC01-DEV-ROTATE-KEY — تدوير مفتاح الجهاز الميداني

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

<!-- BEGIN GENERATED: refs US-BC01-DEV-ROTATE-KEY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/devices/{id}/actions/rotate-key` | — |
| الأمر | `CMD-DEV-ROTATE-KEY` | تدوير مفتاح الجهاز الميداني |
| السياسة | `POL-DEV-ROTATE-KEY` | user (rotate key)؛ tenant match; device ACTIVE where applicable; device signature for SYN |
| الحدث | `EVT-DEV-KEY-ROTATED` | يصل إلى: Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version… |
| الكيان | `AGG-DEVICE` | الجهاز الميداني |
| الجدول | `foundation.devices` | الجدول الرئيسي للجهاز الميداني |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| الاختبار | TST-DEVICE-SM، TST-SLC11-INVARIANTS | دورة حالات الجهاز الميداني، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC01-DEV-ROTATE-KEY -->

</details>

### 5.6 US-BC01-DEV-SUSPEND — تعليق الجهاز الميداني

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

<!-- BEGIN GENERATED: refs US-BC01-DEV-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/devices/{id}/actions/suspend` | — |
| الأمر | `CMD-DEV-SUSPEND` | تعليق الجهاز الميداني |
| السياسة | `POL-DEV-SUSPEND` | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Offi… |
| الحدث | `EVT-DEV-SUSPENDED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-DEVICE` | الجهاز الميداني |
| الجدول | `foundation.devices` | الجدول الرئيسي للجهاز الميداني |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| الاختبار | TST-DEVICE-SM، TST-SLC11-INVARIANTS | دورة حالات الجهاز الميداني، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC01-DEV-SUSPEND -->

</details>

### 5.7 US-BC01-Q-DEV-LIST — جلب: Devices of a user (self) or in scope (Administrator)

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

<!-- BEGIN GENERATED: refs US-BC01-Q-DEV-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/foundation/devices` | — |
| الاستعلام | `QRY-DEV-LIST` | Devices of a user (self) or in scope (Administrator) |
| السياسة | `POL-DEV-LIST` | self; Administrator in scope |
| الكيان | `AGG-DEVICE` | الجهاز الميداني |
| الجدول | `foundation.devices` | الجدول الرئيسي للجهاز الميداني |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| الاختبار | TST-DEVICE-SM، TST-SLC11-INVARIANTS | دورة حالات الجهاز الميداني، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC01-Q-DEV-LIST -->

</details>

### 5.8 US-UI-SCR63-DEVICE-LIST — قائمة الأجهزة وحالتها وآخر مزامنة

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

<!-- BEGIN GENERATED: refs US-UI-SCR63-DEVICE-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-63 | شاشة الأجهزة |
| المصدر | `QRY-DEV-LIST` | — |
| المصدر | `21-ui-design.md §6.3` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR63-DEVICE-LIST -->

</details>

### 5.9 US-UI-SCR63-ENROLL-CONFIRM — تأكيد تسجيل جهاز جديد بعد التحقق منه

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

<!-- BEGIN GENERATED: refs US-UI-SCR63-ENROLL-CONFIRM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-63 | شاشة الأجهزة |
| المصدر | `US-BC01-DEV-CONFIRM` | — |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR63-ENROLL-CONFIRM -->

</details>

### 5.10 US-PLT-DEVICE-ATTESTATION — مفتاح جهاز عتادي غير قابل للتصدير مع إثبات

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

<!-- BEGIN GENERATED: refs US-PLT-DEVICE-ATTESTATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-16 | Web: React + MapLibre GL JS, i18n with ICU messages, RTL via CSS logical properties, Hijri display via Intl (… |
| المصدر | `TB-07` | — |
| المصدر | `US-BC01-DEV-CONFIRM` | — |
| المصدر | `THR-S11-02` | — |
<!-- END GENERATED: refs US-PLT-DEVICE-ATTESTATION -->

</details>

### 5.11 US-INT-MDM-COMPLIANCE — قبول الجهاز بناءً على امتثال إدارة الأجهزة

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

<!-- BEGIN GENERATED: refs US-INT-MDM-COMPLIANCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §2` | — |
| المصدر | `US-BC01-DEV-CONFIRM` | — |
| فحص البنية | FIT-12 | No external network dependency at runtime or build (air-gapped) |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-INT-MDM-COMPLIANCE -->

</details>

### 5.12 US-OPS-FIELDAPP-RELEASE — توزيع إصدارات التطبيق الميداني الموقّعة

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

<!-- BEGIN GENERATED: refs US-OPS-FIELDAPP-RELEASE -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-17 | Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps… |
| القرار التقني | TD-16 | Web: React + MapLibre GL JS, i18n with ICU messages, RTL via CSS logical properties, Hijri display via Intl (… |
| المصدر | `22-deployment-design.md` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-FIELDAPP-RELEASE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. | كل قصص الميزة المأخوذة من المواصفة (7) | TST-DEVICE-SM، TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
