---
id: FEAT-COM-INBOX
type: feature
title: "صندوق إشعاراتي"
status: DRAFT
version: "0.1"
capability: CAP-10.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# صندوق إشعاراتي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COM-INBOX |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-10 الاتصال والمنتجات |
| القدرة الفرعية | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) |
| الأدوار | أي مستخدم مخوَّل؛ النظام |
| الشاشات | SCR-03 صندوق الوارد |
| حالات الاستخدام | UC-099 |
| القصص | 7: 3 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يرى كل مستخدم إشعاراته في مكان واحد ويعلّمها كمقروءة، وتُنظف القديمة تلقائيًا.

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
| QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance | 0 leakage in inference suite (counts, facets, ordering, timing, errors) |
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
| `US-BC04-NTF-MARK-READ` | تعليم الإشعار كمقروء | أمر | مسودة |
| `US-BC04-Q-NTF-INBOX` | جلب: My notifications (references + templates) | جلب | مسودة |
| `US-BC04-S-NOTIFICATION-05` | تلقائي: TTL (30 d) elapsed (الإشعار) | نظام | مسودة |
| `US-UI-SCR03-LIST` | صندوق الوارد غير المقروء أولًا | واجهة | مسودة |
| `US-UI-SCR03-OFFLINE` | الإشعارات في التطبيق الميداني دون اتصال | واجهة | مسودة |
| `US-UI-SCR03-UNREAD-BADGE` | عداد غير المقروء يتحدث تلقائيًا | واجهة | مسودة |
| `US-PLT-INBOX-POLL-FALLBACK` | صندوق الوارد حالي بسحب احتياطي كل دقيقة | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-NTF-MARK-READ — تعليم الإشعار كمقروء

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

<!-- BEGIN GENERATED: refs US-BC04-NTF-MARK-READ -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/notifications/{id}/actions/mark-read` | — |
| الأمر | `CMD-NTF-MARK-READ` | تعليم الإشعار كمقروء |
| السياسة | `POL-NTF-MARK-READ` | recipient؛ tenant match; target visible to subject |
| الحدث | `EVT-NTF-READ` | يصل إلى: Push gateway; In-app inbox |
| الكيان | `AGG-NOTIFICATION` | الإشعار |
| الجدول | `operations.notifications` | الجدول الرئيسي للإشعار |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-COM-001، REQ-COM-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS | دورة حالات الإشعار، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-NTF-MARK-READ -->

</details>

### 5.2 US-BC04-Q-NTF-INBOX — جلب: My notifications (references + templates)

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

<!-- BEGIN GENERATED: refs US-BC04-Q-NTF-INBOX -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/notifications` | — |
| الاستعلام | `QRY-NTF-INBOX` | My notifications (references + templates) |
| السياسة | `POL-NTF-INBOX` | recipient |
| الكيان | `AGG-NOTIFICATION` | الإشعار |
| الجدول | `operations.notifications` | الجدول الرئيسي للإشعار |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS | دورة حالات الإشعار، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-Q-NTF-INBOX -->

</details>

### 5.3 US-BC04-S-NOTIFICATION-05 — تلقائي: TTL (30 d) elapsed (الإشعار)

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

<!-- BEGIN GENERATED: refs US-BC04-S-NOTIFICATION-05 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:TTL (30 d) elapsed` | scheduler |
| الانتقال | QUEUED, SENT ← EXPIRED | — |
| الحدث | `EVT-NTF-EXPIRED` | يصل إلى: Push gateway; In-app inbox |
| الكيان | `AGG-NOTIFICATION` | الإشعار |
| الجدول | `operations.notifications` | الجدول الرئيسي للإشعار |
| وحدة النشر | DU-08 | — |
| المتطلبات | REQ-COM-001، REQ-COM-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS | دورة حالات الإشعار، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-S-NOTIFICATION-05 -->

</details>

### 5.4 US-UI-SCR03-LIST — صندوق الوارد غير المقروء أولًا

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

<!-- BEGIN GENERATED: refs US-UI-SCR03-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-03 | شاشة صندوق الوارد |
| حالة الاستخدام | UC-099 | Receive Notification |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-COM-002 | The system shall not include classified content in mobile push payloads and shall limit notification content… |
| حالة الاستخدام | UC-099 | Receive Notification |
<!-- END GENERATED: refs US-UI-SCR03-LIST -->

</details>

### 5.5 US-UI-SCR03-OFFLINE — الإشعارات في التطبيق الميداني دون اتصال

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

<!-- BEGIN GENERATED: refs US-UI-SCR03-OFFLINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-03 | شاشة صندوق الوارد |
| المصدر | `21-ui-design.md §8` | — |
| المصدر | `20-integration-design.md §6` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR03-OFFLINE -->

</details>

### 5.6 US-UI-SCR03-UNREAD-BADGE — عداد غير المقروء يتحدث تلقائيًا

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

<!-- BEGIN GENERATED: refs US-UI-SCR03-UNREAD-BADGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-03 | شاشة صندوق الوارد |
| الجودة | QAS-SEC-012 | user not cleared for an alert's label → receives no alert, notification, push or count change |
| المصدر | `21-ui-design.md §13` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR03-UNREAD-BADGE -->

</details>

### 5.7 US-PLT-INBOX-POLL-FALLBACK — صندوق الوارد حالي بسحب احتياطي كل دقيقة

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

<!-- BEGIN GENERATED: refs US-PLT-INBOX-POLL-FALLBACK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-OPS-003 | push gateway unavailable (air-gapped) → in-app inbox current; polling fallback ≤ 60 s |
| المصدر | `21-ui-design.md §13` | — |
<!-- END GENERATED: refs US-PLT-INBOX-POLL-FALLBACK -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… | كل قصص الميزة المأخوذة من المواصفة (3) | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS، TST-SUBSCRIPTION-SM |
| REQ-COM-002 | The system shall not include classified content in mobile push payloads and shall limit notification content… | `US-BC04-NTF-MARK-READ`، `US-BC04-S-NOTIFICATION-05`، `US-UI-SCR03-LIST` | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
