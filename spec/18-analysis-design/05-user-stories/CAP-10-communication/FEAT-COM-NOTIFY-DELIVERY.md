---
id: FEAT-COM-NOTIFY-DELIVERY
type: feature
title: "إيصال الإشعارات بأمان"
status: DRAFT
version: "0.1"
capability: CAP-10.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إيصال الإشعارات بأمان

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COM-NOTIFY-DELIVERY |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-10 الاتصال والمنتجات |
| القدرة الفرعية | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) |
| الأدوار | النظام |
| الشاشات | SCR-03 صندوق الوارد |
| حالات الاستخدام | UC-099 |
| القصص | 11: 4 من المواصفة، و7 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

تصل الإشعارات داخل التطبيق وعلى الجوال إلى المخوّلين فقط ودون محتوى سري في رسائل الجوال.

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
| QAS-OPS-003 | push gateway unavailable (air-gapped) | in-app inbox current; polling fallback ≤ 60 s |
| QAS-PERF-005 | reports a value that meets a critical alert rule | end-to-end p95 ≤ 5 s |
| QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance | 0 leakage in inference suite (counts, facets, ordering, timing, errors) |
| QAS-SEC-007 | obtains a field device | 0 readable records without authentication; wipe on next connection |
| QAS-SEC-012 | user not cleared for an alert's label | receives no alert, notification, push or count change |
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
| `US-BC04-S-NOTIFICATION-01` | تلقائي: notifiable event for recipient (الإشعار) | نظام | مسودة |
| `US-BC04-S-NOTIFICATION-02` | تلقائي: delivered to channel (الإشعار) | نظام | مسودة |
| `US-BC04-S-NOTIFICATION-03` | تلقائي: recipient no longer authorized at delivery (الإشعار) | نظام | مسودة |
| `US-BC04-S-NOTIFICATION-04` | تلقائي: delivery failed after retries (الإشعار) | نظام | مسودة |
| `US-DOM-NTF-QUIET-HOURS` | تأجيل الدفع في ساعات الهدوء عدا الحرج | نظام | مسودة |
| `US-PLT-NOTIFY-FANOUT` | وصول إشعار التنبيه الحرج خلال خمس ثوانٍ | منصة | مسودة |
| `US-PLT-NOTIFY-SAFE-PAYLOAD` | رسالة الجوال مرجع وعنوان آمن فقط | منصة | مسودة |
| `US-INT-NOTIFY-DEVICE-TOKEN` | ربط الجهاز بالإشعارات وإلغاؤه عند فقده | تكامل | مسودة |
| `US-INT-NOTIFY-PUSH-RELAY` | إرسال الإشعار الفوري عبر مرحّل داخلي | تكامل | مسودة |
| `US-OPS-NOTIFY-DELIVERY-MONITOR` | مراقبة فشل الإشعارات وتعطل المرحّل | تشغيل | مسودة |
| `US-OPS-NOTIFY-LEAK-TEST` | اختبار عدم تسرب التنبيهات لغير المصرح لهم | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-S-NOTIFICATION-01 — تلقائي: notifiable event for recipient (الإشعار)

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

<!-- BEGIN GENERATED: refs US-BC04-S-NOTIFICATION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:notifiable event for recipient` | recipient ACTIVE; recipient authorized for the referenced object at enqueue time |
| الانتقال | ∅ ← QUEUED | — |
| الحدث | `EVT-NTF-QUEUED` | يصل إلى: Push gateway; In-app inbox |
| الكيان | `AGG-NOTIFICATION` | الإشعار |
| الجدول | `operations.notifications` | الجدول الرئيسي للإشعار |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-COM-001، REQ-COM-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS | دورة حالات الإشعار، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-S-NOTIFICATION-01 -->

</details>

### 5.2 US-BC04-S-NOTIFICATION-02 — تلقائي: delivered to channel (الإشعار)

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

<!-- BEGIN GENERATED: refs US-BC04-S-NOTIFICATION-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:delivered to channel` | re-check authorization at delivery (security_version); push payload = reference + classification-safe title t… |
| الانتقال | QUEUED ← SENT | — |
| الحدث | `EVT-NTF-SENT` | يصل إلى: Push gateway; In-app inbox |
| الكيان | `AGG-NOTIFICATION` | الإشعار |
| الجدول | `operations.notifications` | الجدول الرئيسي للإشعار |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-COM-001، REQ-COM-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS | دورة حالات الإشعار، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-S-NOTIFICATION-02 -->

</details>

### 5.3 US-BC04-S-NOTIFICATION-03 — تلقائي: recipient no longer authorized at delivery (الإشعار)

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

<!-- BEGIN GENERATED: refs US-BC04-S-NOTIFICATION-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:recipient no longer authorized at delivery` | re-check failed |
| الانتقال | QUEUED ← WITHHELD | — |
| الحدث | `EVT-NTF-WITHHELD` | يصل إلى: Push gateway; In-app inbox |
| الكيان | `AGG-NOTIFICATION` | الإشعار |
| الجدول | `operations.notifications` | الجدول الرئيسي للإشعار |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-COM-001، REQ-COM-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS | دورة حالات الإشعار، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-S-NOTIFICATION-03 -->

</details>

### 5.4 US-BC04-S-NOTIFICATION-04 — تلقائي: delivery failed after retries (الإشعار)

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

<!-- BEGIN GENERATED: refs US-BC04-S-NOTIFICATION-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:delivery failed after retries` | 5 attempts with exponential backoff; in-app copy remains |
| الانتقال | QUEUED ← FAILED | — |
| الحدث | `EVT-NTF-FAILED` | يصل إلى: Push gateway; In-app inbox |
| الكيان | `AGG-NOTIFICATION` | الإشعار |
| الجدول | `operations.notifications` | الجدول الرئيسي للإشعار |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-COM-001، REQ-COM-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS | دورة حالات الإشعار، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-S-NOTIFICATION-04 -->

</details>

### 5.5 US-DOM-NTF-QUIET-HOURS — تأجيل الدفع في ساعات الهدوء عدا الحرج

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

<!-- BEGIN GENERATED: refs US-DOM-NTF-QUIET-HOURS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `situation-alerting-spec.md §6` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… |
| حالة الاستخدام | UC-099 | Receive Notification |
<!-- END GENERATED: refs US-DOM-NTF-QUIET-HOURS -->

</details>

### 5.6 US-PLT-NOTIFY-FANOUT — وصول إشعار التنبيه الحرج خلال خمس ثوانٍ

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

<!-- BEGIN GENERATED: refs US-PLT-NOTIFY-FANOUT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-005 | reports a value that meets a critical alert rule → end-to-end p95 ≤ 5 s |
| المتطلب | REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… |
| حالة الاستخدام | UC-099 | Receive Notification |
<!-- END GENERATED: refs US-PLT-NOTIFY-FANOUT -->

</details>

### 5.7 US-PLT-NOTIFY-SAFE-PAYLOAD — رسالة الجوال مرجع وعنوان آمن فقط

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

<!-- BEGIN GENERATED: refs US-PLT-NOTIFY-SAFE-PAYLOAD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance → 0 leakage in inference suite (cou… |
| المصدر | `situation-alerting-spec.md §6` | — |
| المتطلب | REQ-COM-002 | The system shall not include classified content in mobile push payloads and shall limit notification content… |
| حالة الاستخدام | UC-099 | Receive Notification |
<!-- END GENERATED: refs US-PLT-NOTIFY-SAFE-PAYLOAD -->

</details>

### 5.8 US-INT-NOTIFY-DEVICE-TOKEN — ربط الجهاز بالإشعارات وإلغاؤه عند فقده

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

<!-- BEGIN GENERATED: refs US-INT-NOTIFY-DEVICE-TOKEN -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §2` | — |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-COM-001، REQ-OFF-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-099 | Receive Notification |
<!-- END GENERATED: refs US-INT-NOTIFY-DEVICE-TOKEN -->

</details>

### 5.9 US-INT-NOTIFY-PUSH-RELAY — إرسال الإشعار الفوري عبر مرحّل داخلي

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

<!-- BEGIN GENERATED: refs US-INT-NOTIFY-PUSH-RELAY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §2` | — |
| فحص البنية | FIT-12 | No external network dependency at runtime or build (air-gapped) |
| المتطلب | REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… |
| حالة الاستخدام | UC-099 | Receive Notification |
<!-- END GENERATED: refs US-INT-NOTIFY-PUSH-RELAY -->

</details>

### 5.10 US-OPS-NOTIFY-DELIVERY-MONITOR — مراقبة فشل الإشعارات وتعطل المرحّل

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

<!-- BEGIN GENERATED: refs US-OPS-NOTIFY-DELIVERY-MONITOR -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §6.2` | — |
| الجودة | QAS-OPS-003 | push gateway unavailable (air-gapped) → in-app inbox current; polling fallback ≤ 60 s |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-NOTIFY-DELIVERY-MONITOR -->

</details>

### 5.11 US-OPS-NOTIFY-LEAK-TEST — اختبار عدم تسرب التنبيهات لغير المصرح لهم

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

<!-- BEGIN GENERATED: refs US-OPS-NOTIFY-LEAK-TEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-012 | user not cleared for an alert's label → receives no alert, notification, push or count change |
| المتطلب | REQ-COM-002 | The system shall not include classified content in mobile push payloads and shall limit notification content… |
| حالة الاستخدام | UC-099 | Receive Notification |
<!-- END GENERATED: refs US-OPS-NOTIFY-LEAK-TEST -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… | `US-BC04-S-NOTIFICATION-01`، `US-BC04-S-NOTIFICATION-02`، `US-BC04-S-NOTIFICATION-03`، `US-BC04-S-NOTIFICATION-04`، `US-DOM-NTF-QUIET-HOURS`، `US-INT-NOTIFY-DEVICE-TOKEN`، `US-INT-NOTIFY-PUSH-RELAY`، `US-PLT-NOTIFY-FANOUT` | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS، TST-SUBSCRIPTION-SM |
| REQ-COM-002 | The system shall not include classified content in mobile push payloads and shall limit notification content… | `US-BC04-S-NOTIFICATION-01`، `US-BC04-S-NOTIFICATION-02`، `US-BC04-S-NOTIFICATION-03`، `US-BC04-S-NOTIFICATION-04`، `US-OPS-NOTIFY-LEAK-TEST`، `US-PLT-NOTIFY-SAFE-PAYLOAD` | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS |
| REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. | `US-INT-NOTIFY-DEVICE-TOKEN` | TST-DEVICE-SM، TST-PRELOAD-PACKAGE-SM، TST-SLC11-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
