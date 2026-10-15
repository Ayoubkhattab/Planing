---
id: FEAT-COM-SUBSCRIPTIONS
type: feature
title: "اشتراكاتي ومتابعاتي"
status: DRAFT
version: "0.1"
capability: CAP-10.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# اشتراكاتي ومتابعاتي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COM-SUBSCRIPTIONS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-10 الاتصال والمنتجات |
| القدرة الفرعية | CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات)) |
| الأدوار | أي مستخدم مخوَّل؛ النظام |
| الشاشات | SCR-03 صندوق الوارد |
| حالات الاستخدام | UC-099 |
| القصص | 9: 6 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يختار المستخدم ما يتابعه وكيف يصله التنبيه، ويوقفه أو يلغيه متى شاء.

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
| `US-BC04-SUB-PAUSE` | إيقاف الاشتراك مؤقتًا | أمر | مسودة |
| `US-BC04-SUB-RESUME` | استئناف الاشتراك | أمر | مسودة |
| `US-BC04-SUB-SUBSCRIBE` | إنشاء الاشتراك | أمر | مسودة |
| `US-BC04-SUB-UNSUBSCRIBE` | إلغاء الاشتراك | أمر | مسودة |
| `US-BC04-SUB-UPDATE-CHANNELS` | تحديث قنوات الاشتراك | أمر | مسودة |
| `US-DOM-SUB-LIST` | عرض قائمة اشتراكاتي | جلب | مسودة |
| `US-BC04-S-SUBSCRIPTION-01` | تلقائي: subscriber lost visibility of target (الاشتراك) | نظام | مسودة |
| `US-UI-SCR03-SUBSCRIPTIONS` | إدارة اشتراكاتي وقنواتها وساعات الهدوء | واجهة | مسودة |
| `US-UI-SCR12-FOLLOW` | زر متابعة الموقف أو قاعدة التنبيه | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-SUB-PAUSE — إيقاف الاشتراك مؤقتًا

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

<!-- BEGIN GENERATED: refs US-BC04-SUB-PAUSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/subscriptions/{id}/actions/pause` | — |
| الأمر | `CMD-SUB-PAUSE` | إيقاف الاشتراك مؤقتًا |
| السياسة | `POL-SUB-PAUSE` | any user (self) · Administrator (end)؛ tenant match; target visible to subject |
| الحدث | `EVT-SUB-PAUSED` | يصل إلى: Notification fan-out index |
| الكيان | `AGG-SUBSCRIPTION` | الاشتراك |
| الجدول | `operations.subscriptions` | الجدول الرئيسي للاشتراك |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-SUBSCRIPTION-SM، TST-SLC06-INVARIANTS | دورة حالات الاشتراك، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-SUB-PAUSE -->

</details>

### 5.2 US-BC04-SUB-RESUME — استئناف الاشتراك

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

<!-- BEGIN GENERATED: refs US-BC04-SUB-RESUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/subscriptions/{id}/actions/resume` | — |
| الأمر | `CMD-SUB-RESUME` | استئناف الاشتراك |
| السياسة | `POL-SUB-RESUME` | any user (self) · Administrator (end)؛ tenant match; target visible to subject |
| الحدث | `EVT-SUB-RESUMED` | يصل إلى: Notification fan-out index |
| الكيان | `AGG-SUBSCRIPTION` | الاشتراك |
| الجدول | `operations.subscriptions` | الجدول الرئيسي للاشتراك |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-SUBSCRIPTION-SM، TST-SLC06-INVARIANTS | دورة حالات الاشتراك، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-SUB-RESUME -->

</details>

### 5.3 US-BC04-SUB-SUBSCRIBE — إنشاء الاشتراك

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

<!-- BEGIN GENERATED: refs US-BC04-SUB-SUBSCRIBE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/subscriptions` | — |
| الأمر | `CMD-SUB-SUBSCRIBE` | إنشاء الاشتراك |
| السياسة | `POL-SUB-SUBSCRIBE` | any user (self) · Administrator (end)؛ tenant match; target visible to subject |
| الحدث | `EVT-SUB-SUBSCRIBED` | يصل إلى: Notification fan-out index |
| الكيان | `AGG-SUBSCRIPTION` | الاشتراك |
| الجدول | `operations.subscriptions` | الجدول الرئيسي للاشتراك |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-SUBSCRIPTION-SM، TST-SLC06-INVARIANTS | دورة حالات الاشتراك، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-SUB-SUBSCRIBE -->

</details>

### 5.4 US-BC04-SUB-UNSUBSCRIBE — إلغاء الاشتراك

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

<!-- BEGIN GENERATED: refs US-BC04-SUB-UNSUBSCRIBE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/subscriptions/{id}/actions/unsubscribe` | — |
| الأمر | `CMD-SUB-UNSUBSCRIBE` | إلغاء الاشتراك |
| السياسة | `POL-SUB-UNSUBSCRIBE` | any user (self) · Administrator (end)؛ tenant match; target visible to subject |
| الحدث | `EVT-SUB-ENDED` | يصل إلى: Notification fan-out index |
| الكيان | `AGG-SUBSCRIPTION` | الاشتراك |
| الجدول | `operations.subscriptions` | الجدول الرئيسي للاشتراك |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-SUBSCRIPTION-SM، TST-SLC06-INVARIANTS | دورة حالات الاشتراك، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-SUB-UNSUBSCRIBE -->

</details>

### 5.5 US-BC04-SUB-UPDATE-CHANNELS — تحديث قنوات الاشتراك

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

<!-- BEGIN GENERATED: refs US-BC04-SUB-UPDATE-CHANNELS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/subscriptions/{id}/actions/update-channels` | — |
| الأمر | `CMD-SUB-UPDATE-CHANNELS` | تحديث قنوات الاشتراك |
| السياسة | `POL-SUB-UPDATE-CHANNELS` | any user (self) · Administrator (end)؛ tenant match; target visible to subject |
| الحدث | `EVT-SUB-CHANNELS-UPDATED` | يصل إلى: Notification fan-out index |
| الكيان | `AGG-SUBSCRIPTION` | الاشتراك |
| الجدول | `operations.subscriptions` | الجدول الرئيسي للاشتراك |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-SUBSCRIPTION-SM، TST-SLC06-INVARIANTS | دورة حالات الاشتراك، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-SUB-UPDATE-CHANNELS -->

</details>

### 5.6 US-DOM-SUB-LIST — عرض قائمة اشتراكاتي

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R1 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-SUB-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-099 | Receive Notification |
| المصدر | `00-open-questions.md §4` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-DOM-SUB-LIST -->

</details>

### 5.7 US-BC04-S-SUBSCRIPTION-01 — تلقائي: subscriber lost visibility of target (الاشتراك)

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

<!-- BEGIN GENERATED: refs US-BC04-S-SUBSCRIPTION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:subscriber lost visibility of target` | security-version change or reclassification |
| الانتقال | ACTIVE, PAUSED ← ENDED | — |
| الحدث | `EVT-SUB-ENDED` | يصل إلى: Notification fan-out index |
| الكيان | `AGG-SUBSCRIPTION` | الاشتراك |
| الجدول | `operations.subscriptions` | الجدول الرئيسي للاشتراك |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… |
| حالة الاستخدام | UC-099 | Receive Notification |
| الاختبار | TST-SUBSCRIPTION-SM، TST-SLC06-INVARIANTS | دورة حالات الاشتراك، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC04-S-SUBSCRIPTION-01 -->

</details>

### 5.8 US-UI-SCR03-SUBSCRIPTIONS — إدارة اشتراكاتي وقنواتها وساعات الهدوء

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

<!-- BEGIN GENERATED: refs US-UI-SCR03-SUBSCRIPTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-03 | شاشة صندوق الوارد |
| حالة الاستخدام | UC-099 | Receive Notification |
| المصدر | `00-open-questions.md §4` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR03-SUBSCRIPTIONS -->

</details>

### 5.9 US-UI-SCR12-FOLLOW — زر متابعة الموقف أو قاعدة التنبيه

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

<!-- BEGIN GENERATED: refs US-UI-SCR12-FOLLOW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-12 | شاشة إدارة الموقف وقواعد التنبيه |
| حالة الاستخدام | UC-099 | Receive Notification |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR12-FOLLOW -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authoriz… | كل قصص الميزة المأخوذة من المواصفة (6) | TST-NOTIFICATION-SM، TST-SLC06-INVARIANTS، TST-SUBSCRIPTION-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
