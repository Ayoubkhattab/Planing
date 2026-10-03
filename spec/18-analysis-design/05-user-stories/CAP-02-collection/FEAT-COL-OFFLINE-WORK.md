---
id: FEAT-COL-OFFLINE-WORK
type: feature
title: "العمل الميداني دون اتصال"
status: DRAFT
version: "0.1"
capability: CAP-02.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# العمل الميداني دون اتصال

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-OFFLINE-WORK |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) |
| الأدوار | المستخدم الميداني |
| الشاشات | SCR-01 مهامي، SCR-23 الملاحظات |
| حالات الاستخدام | UC-090 |
| القصص | 9: 0 من المواصفة، و9 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يبقى الجهاز الميداني صالحًا للعمل حتى 72 ساعة دون شبكة، ببيانات مشفرة عليه تُمسح عن بعد إن فُقد.

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
| `US-UI-SCR23-OFFLINE-STALE` | التسجيل بعد 72 ساعة دون عرض المحمّل | واجهة | مسودة |
| `US-UI-SCR23-OFFLINE-STATUS` | حالة إرسال كل ملاحظة ومرفق دون اتصال | واجهة | مسودة |
| `US-PLT-DEVICE-STORE` | المخزن المحلي المشفر والمسح عن بعد | منصة | مسودة |
| `US-PLT-OFFLINE-ATTACH-STORE` | حفظ صور الميدان مشفرة حتى رفعها | منصة | مسودة |
| `US-PLT-OFFLINE-CAPACITY` | سعة الجهاز لعمل 72 ساعة دون اتصال | منصة | مسودة |
| `US-PLT-OFFLINE-COMMAND-QUEUE` | طابور أوامر موقّع ومتسلسل على الجهاز | منصة | مسودة |
| `US-PLT-OFFLINE-QUEUE-BACKUP` | نسخ احتياطي مشفر لطابور الجهاز | منصة | مسودة |
| `US-PLT-OFFLINE-TIME-LIMIT` | استمرار الالتقاط بعد 72 ساعة وإيقاف القراءة | منصة | مسودة |
| `US-OPS-OFFLINE-DEVICE-TEST` | اختبار العمل دون اتصال على أجهزة حقيقية | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-UI-SCR23-OFFLINE-STALE — التسجيل بعد 72 ساعة دون عرض المحمّل

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

<!-- BEGIN GENERATED: refs US-UI-SCR23-OFFLINE-STALE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-23 | شاشة الملاحظات |
| المصدر | `21-ui-design.md §8.2` | — |
| المصدر | `field-sync-protocol.md §1` | — |
<!-- END GENERATED: refs US-UI-SCR23-OFFLINE-STALE -->

</details>

### 5.2 US-UI-SCR23-OFFLINE-STATUS — حالة إرسال كل ملاحظة ومرفق دون اتصال

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

<!-- BEGIN GENERATED: refs US-UI-SCR23-OFFLINE-STATUS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-23 | شاشة الملاحظات |
| المصدر | `21-ui-design.md §8.2` | — |
| القرار المعماري | ADR-P09 | Field Synchronization |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OFF-001 | Where the mobile field application is used, the system shall allow recording observations with location, time… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
<!-- END GENERATED: refs US-UI-SCR23-OFFLINE-STATUS -->

</details>

### 5.3 US-PLT-DEVICE-STORE — المخزن المحلي المشفر والمسح عن بعد

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

<!-- BEGIN GENERATED: refs US-PLT-DEVICE-STORE -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-16 | Web: React + MapLibre GL JS, i18n with ICU messages, RTL via CSS logical properties, Hijri display via Intl (… |
| الجودة | QAS-SEC-007 | obtains a field device → 0 readable records without authentication; wipe on next connection |
| المصدر | `field-sync-protocol.md §1` | — |
| المتطلب | REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. |
| حالة الاستخدام | UC-093 | Wipe Lost Device |
<!-- END GENERATED: refs US-PLT-DEVICE-STORE -->

</details>

### 5.4 US-PLT-OFFLINE-ATTACH-STORE — حفظ صور الميدان مشفرة حتى رفعها

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

<!-- BEGIN GENERATED: refs US-PLT-OFFLINE-ATTACH-STORE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `field-sync-protocol.md §1` | — |
| المتطلب | REQ-OFF-001 | Where the mobile field application is used, the system shall allow recording observations with location, time… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
<!-- END GENERATED: refs US-PLT-OFFLINE-ATTACH-STORE -->

</details>

### 5.5 US-PLT-OFFLINE-CAPACITY — سعة الجهاز لعمل 72 ساعة دون اتصال

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

<!-- BEGIN GENERATED: refs US-PLT-OFFLINE-CAPACITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-OFF-001 | works 72 h offline then reconnects on a 1 Mbps link → 1,000 queued commands synced ≤ 10 min; 0 silent overwri… |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OFF-001 | Where the mobile field application is used, the system shall allow recording observations with location, time… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
<!-- END GENERATED: refs US-PLT-OFFLINE-CAPACITY -->

</details>

### 5.6 US-PLT-OFFLINE-COMMAND-QUEUE — طابور أوامر موقّع ومتسلسل على الجهاز

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

<!-- BEGIN GENERATED: refs US-PLT-OFFLINE-COMMAND-QUEUE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `field-sync-protocol.md §1` | — |
| المصدر | `CR-50` | — |
| المصدر | `20-integration-design.md §7` | — |
| المصدر | `THR-S03-05` | — |
<!-- END GENERATED: refs US-PLT-OFFLINE-COMMAND-QUEUE -->

</details>

### 5.7 US-PLT-OFFLINE-QUEUE-BACKUP — نسخ احتياطي مشفر لطابور الجهاز

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

<!-- BEGIN GENERATED: refs US-PLT-OFFLINE-QUEUE-BACKUP -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `FM-S11-04` | — |
<!-- END GENERATED: refs US-PLT-OFFLINE-QUEUE-BACKUP -->

</details>

### 5.8 US-PLT-OFFLINE-TIME-LIMIT — استمرار الالتقاط بعد 72 ساعة وإيقاف القراءة

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

<!-- BEGIN GENERATED: refs US-PLT-OFFLINE-TIME-LIMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `field-sync-protocol.md §1` | — |
| المصدر | `21-ui-design.md §8.2` | — |
| المتطلب | REQ-OFF-001 | Where the mobile field application is used, the system shall allow recording observations with location, time… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
<!-- END GENERATED: refs US-PLT-OFFLINE-TIME-LIMIT -->

</details>

### 5.9 US-OPS-OFFLINE-DEVICE-TEST — اختبار العمل دون اتصال على أجهزة حقيقية

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

<!-- BEGIN GENERATED: refs US-OPS-OFFLINE-DEVICE-TEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-007 | obtains a field device → 0 readable records without authentication; wipe on next connection |
| الجودة | QAS-OFF-001 | works 72 h offline then reconnects on a 1 Mbps link → 1,000 queued commands synced ≤ 10 min; 0 silent overwri… |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-OFF-001 | Where the mobile field application is used, the system shall allow recording observations with location, time… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
<!-- END GENERATED: refs US-OPS-OFFLINE-DEVICE-TEST -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OFF-001 | Where the mobile field application is used, the system shall allow recording observations with location, time… | `US-OPS-OFFLINE-DEVICE-TEST`، `US-PLT-OFFLINE-ATTACH-STORE`، `US-PLT-OFFLINE-CAPACITY`، `US-PLT-OFFLINE-TIME-LIMIT`، `US-UI-SCR23-OFFLINE-STATUS` | TST-SLC03-INVARIANTS، TST-SLC11-INVARIANTS، TST-SYNC-SESSION-SM، TST-TASK-SM |
| REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. | `US-PLT-DEVICE-STORE` | TST-DEVICE-SM، TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
