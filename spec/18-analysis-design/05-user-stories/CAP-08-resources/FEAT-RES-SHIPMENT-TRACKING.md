---
id: FEAT-RES-SHIPMENT-TRACKING
type: feature
title: "إرسال الشحنات وتتبعها"
status: DRAFT
version: "0.1"
capability: CAP-08.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إرسال الشحنات وتتبعها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-SHIPMENT-TRACKING |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.03 الإمداد (R3) |
| الأدوار | مسؤول الإرسال؛ الناقل |
| الشاشات | SCR-49 الإمداد والشحنات |
| حالات الاستخدام | UC-151 |
| القصص | 12: 8 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يرسل مسؤول الإرسال الشحنة ويتابع الجميع مسارها نقطة بنقطة حتى وصولها.

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
| QAS-LOG-002 | shipment dispatched to its destination | transit duration within target (tagged: recalibrate after Pilot R1 and R2 — RSK-028) |
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
| `US-BC05-LGR-DISPATCH` | إرسال طلب الإمداد | أمر | مسودة |
| `US-BC05-SHP-CANCEL` | إلغاء الشحنة | أمر | مسودة |
| `US-BC05-SHP-DEPART` | بدء نقل الشحنة | أمر | مسودة |
| `US-BC05-SHP-PLAN` | تخطيط الشحنة | أمر | مسودة |
| `US-BC05-SHP-RECORD-CHECKPOINT` | تسجيل نقطة عبور لـالشحنة | أمر | مسودة |
| `US-BC05-Q-SHP-GET` | جلب: Shipment with current state and delivered/damaged/lost quantity | جلب | مسودة |
| `US-BC05-Q-SHP-LIST` | جلب: Shipments filtered by logistics request, carrier, state, window | جلب | مسودة |
| `US-BC05-Q-SHP-TRACKING` | جلب: Full checkpoint history of a shipment, in order | جلب | مسودة |
| `US-UI-SCR49-DISPATCH` | الإرسال متاح فقط والتخصيص ملتزم | واجهة | مسودة |
| `US-UI-SCR49-TRACKING-MAP` | مسار الشحنة نقطة بنقطة على الخريطة | واجهة | مسودة |
| `US-PLT-SHP-TRANSIT-METRIC` | قياس مدة نقل الشحنات مقابل الهدف | منصة | مسودة |
| `US-INT-CARRIER-CHECKPOINTS` | استقبال نقاط العبور من نظام الناقل | تكامل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-LGR-DISPATCH — إرسال طلب الإمداد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-LGR-DISPATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/logistics-requests/{id}/actions/dispatch` | — |
| الأمر | `CMD-LGR-DISPATCH` | إرسال طلب الإمداد |
| السياسة | `POL-LGR-DISPATCH` | dispatcher؛ tenant match; linked allocation COMMITTED (INV-LGR-02) |
| الحدث | `EVT-LGR-DISPATCHED` | يصل إلى: Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| الكيان | `AGG-LOGISTICS-REQUEST` | طلب الإمداد |
| الجدول | `readiness.logistics_requests` | الجدول الرئيسي لطلب الإمداد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-001، REQ-LOG-002، REQ-LOG-003، REQ-LOG-008، REQ-LOG-009، REQ-LOG-013، REQ-LOG-014 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-150، UC-152 | Request Logistics Items؛ Receive Shipment or Report Loss/Damage |
| الاختبار | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS | دورة حالات طلب الإمداد، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-LGR-DISPATCH -->

</details>

### 5.2 US-BC05-SHP-CANCEL — إلغاء الشحنة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SHP-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/shipments/{id}/actions/cancel` | — |
| الأمر | `CMD-SHP-CANCEL` | إلغاء الشحنة |
| السياسة | `POL-SHP-CANCEL` | dispatcher؛ tenant match; only before departure (INV-SHP-04) |
| الحدث | `EVT-SHP-CANCELLED` | يصل إلى: Logistics Request (fulfillment status); Search projection (SLC-05) |
| الكيان | `AGG-SHIPMENT` | الشحنة |
| الجدول | `readiness.shipments` | الجدول الرئيسي للشحنة |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-004، REQ-LOG-005، REQ-LOG-006، REQ-LOG-007، REQ-LOG-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
| الاختبار | TST-SHIPMENT-SM، TST-SLC18-INVARIANTS | دورة حالات الشحنة، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-SHP-CANCEL -->

</details>

### 5.3 US-BC05-SHP-DEPART — بدء نقل الشحنة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SHP-DEPART -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/shipments/{id}/actions/depart` | — |
| الأمر | `CMD-SHP-DEPART` | بدء نقل الشحنة |
| السياسة | `POL-SHP-DEPART` | carrier operator · dispatcher؛ tenant match |
| الحدث | `EVT-SHP-DEPARTED` | يصل إلى: Logistics Request (fulfillment status); Search projection (SLC-05) |
| الكيان | `AGG-SHIPMENT` | الشحنة |
| الجدول | `readiness.shipments` | الجدول الرئيسي للشحنة |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-004، REQ-LOG-005، REQ-LOG-006، REQ-LOG-007، REQ-LOG-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
| الاختبار | TST-SHIPMENT-SM، TST-SLC18-INVARIANTS | دورة حالات الشحنة، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-SHP-DEPART -->

</details>

### 5.4 US-BC05-SHP-PLAN — تخطيط الشحنة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SHP-PLAN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/shipments` | — |
| الأمر | `CMD-SHP-PLAN` | تخطيط الشحنة |
| السياسة | `POL-SHP-PLAN` | dispatcher؛ tenant match; origin pool scope visible to actor; linked logistics request APPROVED |
| الحدث | `EVT-SHP-PLANNED` | يصل إلى: Logistics Request (fulfillment status); Search projection (SLC-05) |
| الكيان | `AGG-SHIPMENT` | الشحنة |
| الجدول | `readiness.shipments` | الجدول الرئيسي للشحنة |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-004، REQ-LOG-005، REQ-LOG-006، REQ-LOG-007، REQ-LOG-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
| الاختبار | TST-SHIPMENT-SM، TST-SLC18-INVARIANTS | دورة حالات الشحنة، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-SHP-PLAN -->

</details>

### 5.5 US-BC05-SHP-RECORD-CHECKPOINT — تسجيل نقطة عبور لـالشحنة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SHP-RECORD-CHECKPOINT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/shipments/{id}/actions/record-checkpoint` | — |
| الأمر | `CMD-SHP-RECORD-CHECKPOINT` | تسجيل نقطة عبور لـالشحنة |
| السياسة | `POL-SHP-RECORD-CHECKPOINT` | carrier operator · dispatcher؛ tenant match; checkpoint strictly after the previous one (INV-SHP-01) |
| الحدث | `EVT-SHP-CHECKPOINT-RECORDED` | يصل إلى: Logistics Request (fulfillment status); Search projection (SLC-05) |
| الكيان | `AGG-SHIPMENT` | الشحنة |
| الجدول | `readiness.shipments` | الجدول الرئيسي للشحنة |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-004، REQ-LOG-005، REQ-LOG-006، REQ-LOG-007، REQ-LOG-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
| الاختبار | TST-SHIPMENT-SM، TST-SLC18-INVARIANTS | دورة حالات الشحنة، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-SHP-RECORD-CHECKPOINT -->

</details>

### 5.6 US-BC05-Q-SHP-GET — جلب: Shipment with current state and delivered/damaged/lost quantity

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-Q-SHP-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/shipments/{shipment_id}` | — |
| الاستعلام | `QRY-SHP-GET` | Shipment with current state and delivered/damaged/lost quantity |
| السياسة | `POL-SHP-GET` | allowed_scope |
| الكيان | `AGG-SHIPMENT` | الشحنة |
| الجدول | `readiness.shipments` | الجدول الرئيسي للشحنة |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-LOG-011 | The system shall let an authorized actor list and filter shipments by logistics request, carrier, state and w… |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
| الاختبار | TST-SHIPMENT-SM، TST-SLC18-INVARIANTS | دورة حالات الشحنة، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-Q-SHP-GET -->

</details>

### 5.7 US-BC05-Q-SHP-LIST — جلب: Shipments filtered by logistics request, carrier, state, window

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-Q-SHP-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/shipments` | — |
| الاستعلام | `QRY-SHP-LIST` | Shipments filtered by logistics request, carrier, state, window |
| السياسة | `POL-SHP-LIST` | allowed_scope |
| الكيان | `AGG-SHIPMENT` | الشحنة |
| الجدول | `readiness.shipments` | الجدول الرئيسي للشحنة |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-LOG-011 | The system shall let an authorized actor list and filter shipments by logistics request, carrier, state and w… |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
| الاختبار | TST-SHIPMENT-SM، TST-SLC18-INVARIANTS | دورة حالات الشحنة، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-Q-SHP-LIST -->

</details>

### 5.8 US-BC05-Q-SHP-TRACKING — جلب: Full checkpoint history of a shipment, in order

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R3 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-Q-SHP-TRACKING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/shipments/{shipment_id}/checkpoints` | — |
| الاستعلام | `QRY-SHP-TRACKING` | Full checkpoint history of a shipment, in order |
| السياسة | `POL-SHP-TRACKING` | allowed_scope |
| الكيان | `AGG-SHIPMENT` | الشحنة |
| الجدول | `readiness.shipments` | الجدول الرئيسي للشحنة |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-LOG-012 | The system shall provide the full, ordered checkpoint history of a shipment to an authorized actor. |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
| الاختبار | TST-SHIPMENT-SM، TST-SLC18-INVARIANTS | دورة حالات الشحنة، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-Q-SHP-TRACKING -->

</details>

### 5.9 US-UI-SCR49-DISPATCH — الإرسال متاح فقط والتخصيص ملتزم

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR49-DISPATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-49 | شاشة الإمداد والشحنات |
| المتطلب | REQ-LOG-004 | The system shall allow dispatch of an approved logistics request only while its linked allocation remains COM… |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
<!-- END GENERATED: refs US-UI-SCR49-DISPATCH -->

</details>

### 5.10 US-UI-SCR49-TRACKING-MAP — مسار الشحنة نقطة بنقطة على الخريطة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R3 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR49-TRACKING-MAP -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-49 | شاشة الإمداد والشحنات |
| المصدر | `21-ui-design.md §7` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-LOG-012 | The system shall provide the full, ordered checkpoint history of a shipment to an authorized actor. |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
<!-- END GENERATED: refs US-UI-SCR49-TRACKING-MAP -->

</details>

### 5.11 US-PLT-SHP-TRANSIT-METRIC — قياس مدة نقل الشحنات مقابل الهدف

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-SHP-TRANSIT-METRIC -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-LOG-002 | shipment dispatched to its destination → transit duration within target (tagged: recalibrate after Pilot R1 a… |
| المتطلب | REQ-LOG-004 | The system shall allow dispatch of an approved logistics request only while its linked allocation remains COM… |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
<!-- END GENERATED: refs US-PLT-SHP-TRANSIT-METRIC -->

</details>

### 5.12 US-INT-CARRIER-CHECKPOINTS — استقبال نقاط العبور من نظام الناقل

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R3 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-CARRIER-CHECKPOINTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §3` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-LOG-005 | The system shall record a shipment's movement as an append-only, chronologically ordered checkpoint history. |
| حالة الاستخدام | UC-151 | Dispatch & Track Shipment |
<!-- END GENERATED: refs US-INT-CARRIER-CHECKPOINTS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-LOG-001 | The system shall allow an authorized actor to request a quantity of a logistics item to a destination, and sh… | `US-BC05-LGR-DISPATCH` | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-002 | The system shall track logistics item inventory as a Resource Pool (SLC-09) rather than a separate stock mode… | `US-BC05-LGR-DISPATCH` | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-003 | A logistics request's approval routing shall exactly follow its linked allocation's approval outcome; no sepa… | `US-BC05-LGR-DISPATCH` | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-004 | The system shall allow dispatch of an approved logistics request only while its linked allocation remains COM… | `US-BC05-SHP-CANCEL`، `US-BC05-SHP-DEPART`، `US-BC05-SHP-PLAN`، `US-BC05-SHP-RECORD-CHECKPOINT`، `US-PLT-SHP-TRANSIT-METRIC`، `US-UI-SCR49-DISPATCH` | TST-SHIPMENT-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-005 | The system shall record a shipment's movement as an append-only, chronologically ordered checkpoint history. | `US-BC05-SHP-CANCEL`، `US-BC05-SHP-DEPART`، `US-BC05-SHP-PLAN`، `US-BC05-SHP-RECORD-CHECKPOINT`، `US-INT-CARRIER-CHECKPOINTS` | TST-SHIPMENT-SM |
| REQ-LOG-006 | The system shall record the quantity actually delivered at receipt, distinct from the quantity planned, and s… | `US-BC05-SHP-CANCEL`، `US-BC05-SHP-DEPART`، `US-BC05-SHP-PLAN`، `US-BC05-SHP-RECORD-CHECKPOINT` | TST-SHIPMENT-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-007 | The system shall allow reporting a shipment as damaged or lost in transit, recording the reason and, for dama… | `US-BC05-SHP-CANCEL`، `US-BC05-SHP-DEPART`، `US-BC05-SHP-PLAN`، `US-BC05-SHP-RECORD-CHECKPOINT` | TST-SHIPMENT-SM |
| REQ-LOG-008 | The system shall record consumption on a logistics request's linked allocation only from a confirmed shipment… | `US-BC05-LGR-DISPATCH` | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-009 | The system shall allow cancelling a logistics request before dispatch, releasing its linked allocation, and s… | كل قصص الأوامر والنظام في الميزة (5) | TST-LOGISTICS-REQUEST-SM، TST-SHIPMENT-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-011 | The system shall let an authorized actor list and filter shipments by logistics request, carrier, state and w… | `US-BC05-Q-SHP-GET`، `US-BC05-Q-SHP-LIST` | — |
| REQ-LOG-012 | The system shall provide the full, ordered checkpoint history of a shipment to an authorized actor. | `US-BC05-Q-SHP-TRACKING`، `US-UI-SCR49-TRACKING-MAP` | — |
| REQ-LOG-013 | The system shall resolve a logistics item's identity against a per-tenant reference catalog (RD-LOGISTICS-ITE… | `US-BC05-LGR-DISPATCH` | TST-LOGISTICS-REQUEST-SM |
| REQ-LOG-014 | Contention among logistics requests for the same pool shall be resolved exactly as SLC-09 resolves allocation… | `US-BC05-LGR-DISPATCH` | TST-LOGISTICS-REQUEST-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
