---
id: FEAT-RES-SUPPLY-REQUEST
type: feature
title: "طلب الإمداد"
status: DRAFT
version: "0.1"
capability: CAP-08.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# طلب الإمداد

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-SUPPLY-REQUEST |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.03 الإمداد (R3) |
| الأدوار | ضابط الإمداد؛ المخطِّط؛ النظام |
| الشاشات | SCR-49 الإمداد والشحنات |
| حالات الاستخدام | UC-150 |
| القصص | 13: 9 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يطلب ضابط الإمداد أو المخطط كمية من صنف إلى وجهة ويتابع موافقتها أو رفضها حتى تصبح جاهزة للإرسال.

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
| `US-BC05-LGR-CANCEL` | إلغاء طلب الإمداد | أمر | مسودة |
| `US-BC05-LGR-REQUEST` | تقديم طلب الإمداد | أمر | مسودة |
| `US-BC05-Q-LGR-GET` | جلب: Logistics request with linked allocation and shipment refs | جلب | مسودة |
| `US-BC05-Q-LGR-LIST` | جلب: Logistics requests filtered by item, destination, state, priority | جلب | مسودة |
| `US-BC05-S-LOGISTICS-REQUEST-01` | تلقائي: linked allocation committed (طلب الإمداد) | نظام | مسودة |
| `US-BC05-S-LOGISTICS-REQUEST-02` | تلقائي: linked allocation requires approval (طلب الإمداد) | نظام | مسودة |
| `US-BC05-S-LOGISTICS-REQUEST-03` | تلقائي: linked allocation rejected (طلب الإمداد) | نظام | مسودة |
| `US-BC05-S-LOGISTICS-REQUEST-04` | تلقائي: linked allocation committed (طلب الإمداد) | نظام | مسودة |
| `US-BC05-S-LOGISTICS-REQUEST-05` | تلقائي: linked allocation rejected (طلب الإمداد) | نظام | مسودة |
| `US-DOM-LGR-LABEL` | اشتقاق تصنيف طلب الإمداد والشحنة | نظام | مسودة |
| `US-UI-SCR49-REQUEST-FORM` | طلب إمداد من فهرس الأصناف وحالة تخصيصه | واجهة | مسودة |
| `US-UI-SCR49-REQUEST-LIST` | قائمة طلبات الإمداد بمرشحاتها وروابطها | واجهة | مسودة |
| `US-INT-ERP-INVENTORY` | مقارنة مخزون الأصناف في ERP بالمجمعات | تكامل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-LGR-CANCEL — إلغاء طلب الإمداد

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

<!-- BEGIN GENERATED: refs US-BC05-LGR-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/logistics-requests/{id}/actions/cancel` | — |
| الأمر | `CMD-LGR-CANCEL` | إلغاء طلب الإمداد |
| السياسة | `POL-LGR-CANCEL` | requester · logistics authority؛ tenant match |
| الحدث | `EVT-LGR-CANCELLED` | يصل إلى: Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| الكيان | `AGG-LOGISTICS-REQUEST` | طلب الإمداد |
| الجدول | `readiness.logistics_requests` | الجدول الرئيسي لطلب الإمداد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-001، REQ-LOG-002، REQ-LOG-003، REQ-LOG-008، REQ-LOG-009، REQ-LOG-013، REQ-LOG-014 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-150 | Request Logistics Items |
| الاختبار | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS | دورة حالات طلب الإمداد، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-LGR-CANCEL -->

</details>

### 5.2 US-BC05-LGR-REQUEST — تقديم طلب الإمداد

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

<!-- BEGIN GENERATED: refs US-BC05-LGR-REQUEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/logistics-requests` | — |
| الأمر | `CMD-LGR-REQUEST` | تقديم طلب الإمداد |
| السياسة | `POL-LGR-REQUEST` | Logistics Officer / Planner؛ tenant match; item_pool visible to actor |
| الحدث | `EVT-LGR-REQUESTED` | يصل إلى: Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| الكيان | `AGG-LOGISTICS-REQUEST` | طلب الإمداد |
| الجدول | `readiness.logistics_requests` | الجدول الرئيسي لطلب الإمداد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-001، REQ-LOG-002، REQ-LOG-003، REQ-LOG-008، REQ-LOG-009، REQ-LOG-013، REQ-LOG-014 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-150 | Request Logistics Items |
| الاختبار | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS | دورة حالات طلب الإمداد، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-LGR-REQUEST -->

</details>

### 5.3 US-BC05-Q-LGR-GET — جلب: Logistics request with linked allocation and shipment refs

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

<!-- BEGIN GENERATED: refs US-BC05-Q-LGR-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/logistics-requests/{request_id}` | — |
| الاستعلام | `QRY-LGR-GET` | Logistics request with linked allocation and shipment refs |
| السياسة | `POL-LGR-GET` | allowed_scope; requester |
| الكيان | `AGG-LOGISTICS-REQUEST` | طلب الإمداد |
| الجدول | `readiness.logistics_requests` | الجدول الرئيسي لطلب الإمداد |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-LOG-010 | The system shall let an authorized actor list and filter logistics requests by item, destination, state and p… |
| حالة الاستخدام | UC-150 | Request Logistics Items |
| الاختبار | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS | دورة حالات طلب الإمداد، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-Q-LGR-GET -->

</details>

### 5.4 US-BC05-Q-LGR-LIST — جلب: Logistics requests filtered by item, destination, state, priority

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

<!-- BEGIN GENERATED: refs US-BC05-Q-LGR-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/logistics-requests` | — |
| الاستعلام | `QRY-LGR-LIST` | Logistics requests filtered by item, destination, state, priority |
| السياسة | `POL-LGR-LIST` | allowed_scope |
| الكيان | `AGG-LOGISTICS-REQUEST` | طلب الإمداد |
| الجدول | `readiness.logistics_requests` | الجدول الرئيسي لطلب الإمداد |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-LOG-010 | The system shall let an authorized actor list and filter logistics requests by item, destination, state and p… |
| حالة الاستخدام | UC-150 | Request Logistics Items |
| الاختبار | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS | دورة حالات طلب الإمداد، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-Q-LGR-LIST -->

</details>

### 5.5 US-BC05-S-LOGISTICS-REQUEST-01 — تلقائي: linked allocation committed (طلب الإمداد)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-S-LOGISTICS-REQUEST-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:linked allocation committed` | SLC-09 EVT-ALC-COMMITTED for the linked allocation |
| الانتقال | REQUESTED ← APPROVED | — |
| الحدث | `EVT-LGR-APPROVED` | يصل إلى: Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| الكيان | `AGG-LOGISTICS-REQUEST` | طلب الإمداد |
| الجدول | `readiness.logistics_requests` | الجدول الرئيسي لطلب الإمداد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-001، REQ-LOG-002، REQ-LOG-003، REQ-LOG-008، REQ-LOG-009، REQ-LOG-013، REQ-LOG-014 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-150 | Request Logistics Items |
| الاختبار | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS | دورة حالات طلب الإمداد، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-S-LOGISTICS-REQUEST-01 -->

</details>

### 5.6 US-BC05-S-LOGISTICS-REQUEST-02 — تلقائي: linked allocation requires approval (طلب الإمداد)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-S-LOGISTICS-REQUEST-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:linked allocation requires approval` | SLC-09 EVT-ALC-APPROVAL-REQUIRED for the linked allocation |
| الانتقال | REQUESTED ← PENDING_APPROVAL | — |
| الحدث | `EVT-LGR-PENDING-APPROVAL` | يصل إلى: Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| الكيان | `AGG-LOGISTICS-REQUEST` | طلب الإمداد |
| الجدول | `readiness.logistics_requests` | الجدول الرئيسي لطلب الإمداد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-001، REQ-LOG-002، REQ-LOG-003، REQ-LOG-008، REQ-LOG-009، REQ-LOG-013، REQ-LOG-014 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-150 | Request Logistics Items |
| الاختبار | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS | دورة حالات طلب الإمداد، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-S-LOGISTICS-REQUEST-02 -->

</details>

### 5.7 US-BC05-S-LOGISTICS-REQUEST-03 — تلقائي: linked allocation rejected (طلب الإمداد)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-S-LOGISTICS-REQUEST-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:linked allocation rejected` | SLC-09 EVT-ALC-REJECTED for the linked allocation; reason codes carried over |
| الانتقال | REQUESTED ← REJECTED | — |
| الحدث | `EVT-LGR-REJECTED` | يصل إلى: Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| الكيان | `AGG-LOGISTICS-REQUEST` | طلب الإمداد |
| الجدول | `readiness.logistics_requests` | الجدول الرئيسي لطلب الإمداد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-001، REQ-LOG-002، REQ-LOG-003، REQ-LOG-008، REQ-LOG-009، REQ-LOG-013، REQ-LOG-014 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-150 | Request Logistics Items |
| الاختبار | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS | دورة حالات طلب الإمداد، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-S-LOGISTICS-REQUEST-03 -->

</details>

### 5.8 US-BC05-S-LOGISTICS-REQUEST-04 — تلقائي: linked allocation committed (طلب الإمداد)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-S-LOGISTICS-REQUEST-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:linked allocation committed` | SLC-09 EVT-ALC-COMMITTED for the linked allocation |
| الانتقال | PENDING_APPROVAL ← APPROVED | — |
| الحدث | `EVT-LGR-APPROVED` | يصل إلى: Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| الكيان | `AGG-LOGISTICS-REQUEST` | طلب الإمداد |
| الجدول | `readiness.logistics_requests` | الجدول الرئيسي لطلب الإمداد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-001، REQ-LOG-002، REQ-LOG-003، REQ-LOG-008، REQ-LOG-009، REQ-LOG-013، REQ-LOG-014 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-150 | Request Logistics Items |
| الاختبار | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS | دورة حالات طلب الإمداد، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-S-LOGISTICS-REQUEST-04 -->

</details>

### 5.9 US-BC05-S-LOGISTICS-REQUEST-05 — تلقائي: linked allocation rejected (طلب الإمداد)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-S-LOGISTICS-REQUEST-05 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:linked allocation rejected` | SLC-09 EVT-ALC-REJECTED for the linked allocation (approval denied or provisional hold elapsed) |
| الانتقال | PENDING_APPROVAL ← REJECTED | — |
| الحدث | `EVT-LGR-REJECTED` | يصل إلى: Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| الكيان | `AGG-LOGISTICS-REQUEST` | طلب الإمداد |
| الجدول | `readiness.logistics_requests` | الجدول الرئيسي لطلب الإمداد |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-LOG-001، REQ-LOG-002، REQ-LOG-003، REQ-LOG-008، REQ-LOG-009، REQ-LOG-013، REQ-LOG-014 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-150 | Request Logistics Items |
| الاختبار | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS | دورة حالات طلب الإمداد، وثوابت الشريحة SLC-18 |
<!-- END GENERATED: refs US-BC05-S-LOGISTICS-REQUEST-05 -->

</details>

### 5.10 US-DOM-LGR-LABEL — اشتقاق تصنيف طلب الإمداد والشحنة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-LGR-LABEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §10` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-002 | The system shall require a classification on every object of importance tier T1 or T2. |
<!-- END GENERATED: refs US-DOM-LGR-LABEL -->

</details>

### 5.11 US-UI-SCR49-REQUEST-FORM — طلب إمداد من فهرس الأصناف وحالة تخصيصه

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

<!-- BEGIN GENERATED: refs US-UI-SCR49-REQUEST-FORM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-49 | شاشة الإمداد والشحنات |
| المتطلبات | REQ-LOG-001، REQ-LOG-003، REQ-LOG-013 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-150 | Request Logistics Items |
<!-- END GENERATED: refs US-UI-SCR49-REQUEST-FORM -->

</details>

### 5.12 US-UI-SCR49-REQUEST-LIST — قائمة طلبات الإمداد بمرشحاتها وروابطها

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

<!-- BEGIN GENERATED: refs US-UI-SCR49-REQUEST-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-49 | شاشة الإمداد والشحنات |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-LOG-010 | The system shall let an authorized actor list and filter logistics requests by item, destination, state and p… |
| حالة الاستخدام | UC-150 | Request Logistics Items |
<!-- END GENERATED: refs US-UI-SCR49-REQUEST-LIST -->

</details>

### 5.13 US-INT-ERP-INVENTORY — مقارنة مخزون الأصناف في ERP بالمجمعات

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-ERP-INVENTORY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §2` | — |
| المصدر | `BRL-013` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-LOG-002 | The system shall track logistics item inventory as a Resource Pool (SLC-09) rather than a separate stock mode… |
| حالة الاستخدام | UC-150 | Request Logistics Items |
<!-- END GENERATED: refs US-INT-ERP-INVENTORY -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-GOV-002 | The system shall require a classification on every object of importance tier T1 or T2. | `US-DOM-LGR-LABEL` | — |
| REQ-LOG-001 | The system shall allow an authorized actor to request a quantity of a logistics item to a destination, and sh… | `US-BC05-LGR-CANCEL`، `US-BC05-LGR-REQUEST`، `US-BC05-S-LOGISTICS-REQUEST-01`، `US-BC05-S-LOGISTICS-REQUEST-02`، `US-BC05-S-LOGISTICS-REQUEST-03`، `US-BC05-S-LOGISTICS-REQUEST-04`، `US-BC05-S-LOGISTICS-REQUEST-05`، `US-UI-SCR49-REQUEST-FORM` | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-002 | The system shall track logistics item inventory as a Resource Pool (SLC-09) rather than a separate stock mode… | `US-BC05-LGR-CANCEL`، `US-BC05-LGR-REQUEST`، `US-BC05-S-LOGISTICS-REQUEST-01`، `US-BC05-S-LOGISTICS-REQUEST-02`، `US-BC05-S-LOGISTICS-REQUEST-03`، `US-BC05-S-LOGISTICS-REQUEST-04`، `US-BC05-S-LOGISTICS-REQUEST-05`، `US-INT-ERP-INVENTORY` | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-003 | A logistics request's approval routing shall exactly follow its linked allocation's approval outcome; no sepa… | `US-BC05-LGR-CANCEL`، `US-BC05-LGR-REQUEST`، `US-BC05-S-LOGISTICS-REQUEST-01`، `US-BC05-S-LOGISTICS-REQUEST-02`، `US-BC05-S-LOGISTICS-REQUEST-03`، `US-BC05-S-LOGISTICS-REQUEST-04`، `US-BC05-S-LOGISTICS-REQUEST-05`، `US-UI-SCR49-REQUEST-FORM` | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-008 | The system shall record consumption on a logistics request's linked allocation only from a confirmed shipment… | كل قصص الأوامر والنظام في الميزة (7) | TST-LOGISTICS-REQUEST-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-009 | The system shall allow cancelling a logistics request before dispatch, releasing its linked allocation, and s… | كل قصص الأوامر والنظام في الميزة (7) | TST-LOGISTICS-REQUEST-SM، TST-SHIPMENT-SM، TST-SLC18-INVARIANTS |
| REQ-LOG-010 | The system shall let an authorized actor list and filter logistics requests by item, destination, state and p… | `US-BC05-Q-LGR-GET`، `US-BC05-Q-LGR-LIST`، `US-UI-SCR49-REQUEST-LIST` | — |
| REQ-LOG-013 | The system shall resolve a logistics item's identity against a per-tenant reference catalog (RD-LOGISTICS-ITE… | `US-BC05-LGR-CANCEL`، `US-BC05-LGR-REQUEST`، `US-BC05-S-LOGISTICS-REQUEST-01`، `US-BC05-S-LOGISTICS-REQUEST-02`، `US-BC05-S-LOGISTICS-REQUEST-03`، `US-BC05-S-LOGISTICS-REQUEST-04`، `US-BC05-S-LOGISTICS-REQUEST-05`، `US-UI-SCR49-REQUEST-FORM` | TST-LOGISTICS-REQUEST-SM |
| REQ-LOG-014 | Contention among logistics requests for the same pool shall be resolved exactly as SLC-09 resolves allocation… | كل قصص الأوامر والنظام في الميزة (7) | TST-LOGISTICS-REQUEST-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
