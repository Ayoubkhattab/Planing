---
id: FEAT-COL-LOST-DEVICE
type: feature
title: "الإبلاغ عن جهاز مفقود"
status: DRAFT
version: "0.1"
capability: CAP-02.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# الإبلاغ عن جهاز مفقود

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-LOST-DEVICE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) |
| الأدوار | المستخدم الميداني؛ مسؤول الإدارة؛ النظام |
| الشاشات | SCR-63 الأجهزة |
| حالات الاستخدام | UC-093 |
| القصص | 6: 3 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح الإبلاغ عن فقد الجهاز فيمنع مزامنته ويمسح بياناته عن بعد حماية للمعلومات.

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
| QAS-OFF-001 | works 72 h offline then reconnects on a 1 Mbps link | 1,000 queued commands synced ≤ 10 min; 0 silent overwrites; 0 duplicates |
| QAS-SEC-003 | removes a user's compartment | effective on next request in every path, independent of index lag |
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
| `US-BC01-DEV-REPORT-LOST` | الإبلاغ عن فقد الجهاز الميداني | أمر | مسودة |
| `US-BC01-S-DEVICE-01` | تلقائي: wipe confirmed by device (الجهاز الميداني) | نظام | مسودة |
| `US-BC07-S-SYNC-SESSION-01` | تلقائي: device LOST or SUSPENDED at handshake (جلسة المزامنة) | نظام | مسودة |
| `US-UI-SCR63-REPORT-LOST` | الإبلاغ عن فقد جهاز ومتابعة مسحه | واجهة | مسودة |
| `US-PLT-LOST-DEVICE-TOKEN-REVOKE` | إبطال جلسات الجهاز المفقود فورًا | منصة | مسودة |
| `US-OPS-LOST-DEVICE-REVIEW` | مراجعة أمنية لكل جهاز مفقود | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-DEV-REPORT-LOST — الإبلاغ عن فقد الجهاز الميداني

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

<!-- BEGIN GENERATED: refs US-BC01-DEV-REPORT-LOST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/devices/{id}/actions/report-lost` | — |
| الأمر | `CMD-DEV-REPORT-LOST` | الإبلاغ عن فقد الجهاز الميداني |
| السياسة | `POL-DEV-REPORT-LOST` | user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Offi… |
| الحدث | `EVT-DEV-REPORTED-LOST` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-DEVICE` | الجهاز الميداني |
| الجدول | `foundation.devices` | الجدول الرئيسي للجهاز الميداني |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| الاختبار | TST-DEVICE-SM، TST-SLC11-INVARIANTS | دورة حالات الجهاز الميداني، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC01-DEV-REPORT-LOST -->

</details>

### 5.2 US-BC01-S-DEVICE-01 — تلقائي: wipe confirmed by device (الجهاز الميداني)

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

<!-- BEGIN GENERATED: refs US-BC01-S-DEVICE-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:wipe confirmed by device` | device acknowledges wipe on next contact |
| الانتقال | LOST ← WIPED | — |
| الحدث | `EVT-DEV-WIPED` | يصل إلى: Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version… |
| الكيان | `AGG-DEVICE` | الجهاز الميداني |
| الجدول | `foundation.devices` | الجدول الرئيسي للجهاز الميداني |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| الاختبار | TST-DEVICE-SM، TST-SLC11-INVARIANTS | دورة حالات الجهاز الميداني، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC01-S-DEVICE-01 -->

</details>

### 5.3 US-BC07-S-SYNC-SESSION-01 — تلقائي: device LOST or SUSPENDED at handshake (جلسة المزامنة)

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

<!-- BEGIN GENERATED: refs US-BC07-S-SYNC-SESSION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:device LOST or SUSPENDED at handshake` | returns wipe (LOST) or stop (SUSPENDED) instruction only |
| الانتقال | ∅ ← REJECTED | — |
| الحدث | `EVT-SYN-REJECTED` | يصل إلى: Owner contexts (commands applied via their APIs); Field telemetry |
| الكيان | `AGG-SYNC-SESSION` | جلسة المزامنة |
| الجدول | `field.sync_sessions` | الجدول الرئيسي لجلسة المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-001، REQ-OFF-003، REQ-OFF-004، REQ-OFF-006 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-091، UC-092 | Capture Observation Offline؛ Synchronize Field Device؛ Review Synchronization Conflict |
| الاختبار | TST-SYNC-SESSION-SM، TST-SLC11-INVARIANTS | دورة حالات جلسة المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-S-SYNC-SESSION-01 -->

</details>

### 5.4 US-UI-SCR63-REPORT-LOST — الإبلاغ عن فقد جهاز ومتابعة مسحه

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

<!-- BEGIN GENERATED: refs US-UI-SCR63-REPORT-LOST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-63 | شاشة الأجهزة |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
| المصدر | `21-ui-design.md §6.2` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
<!-- END GENERATED: refs US-UI-SCR63-REPORT-LOST -->

</details>

### 5.5 US-PLT-LOST-DEVICE-TOKEN-REVOKE — إبطال جلسات الجهاز المفقود فورًا

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

<!-- BEGIN GENERATED: refs US-PLT-LOST-DEVICE-TOKEN-REVOKE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §2` | — |
| المصدر | `17-security-design.md §3.5` | — |
| الجودة | QAS-SEC-003 | removes a user's compartment → effective on next request in every path, independent of index lag |
| المصدر | `THR-S11-04` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-LOST-DEVICE-TOKEN-REVOKE -->

</details>

### 5.6 US-OPS-LOST-DEVICE-REVIEW — مراجعة أمنية لكل جهاز مفقود

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

<!-- BEGIN GENERATED: refs US-OPS-LOST-DEVICE-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc11.md` | — |
| المصدر | `THR-S11-01` | — |
| المصدر | `THR-011` | — |
<!-- END GENERATED: refs US-OPS-LOST-DEVICE-REVIEW -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OFF-001 | Where the mobile field application is used, the system shall allow recording observations with location, time… | `US-BC07-S-SYNC-SESSION-01` | TST-SLC03-INVARIANTS، TST-SLC11-INVARIANTS، TST-SYNC-SESSION-SM، TST-TASK-SM |
| REQ-OFF-003 | When a device reconnects, the system shall receive the device's recorded commands in their original order wit… | `US-BC07-S-SYNC-SESSION-01` | TST-SLC11-INVARIANTS، TST-SYNC-SESSION-SM |
| REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… | `US-BC07-S-SYNC-SESSION-01` | TST-SLC11-INVARIANTS، TST-SYNC-CONFLICT-SM، TST-SYNC-SESSION-SM |
| REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. | `US-BC01-DEV-REPORT-LOST`، `US-BC01-S-DEVICE-01`، `US-UI-SCR63-REPORT-LOST` | TST-DEVICE-SM، TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS |
| REQ-OFF-006 | When a synchronization is interrupted, the system shall resume it without duplicating commands. | `US-BC07-S-SYNC-SESSION-01` | TST-SLC11-INVARIANTS، TST-SYNC-SESSION-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
