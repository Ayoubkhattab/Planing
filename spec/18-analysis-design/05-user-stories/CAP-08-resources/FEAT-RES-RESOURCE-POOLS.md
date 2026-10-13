---
id: FEAT-RES-RESOURCE-POOLS
type: feature
title: "إدارة مجمعات الموارد"
status: DRAFT
version: "0.1"
capability: CAP-08.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة مجمعات الموارد

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-RESOURCE-POOLS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.02 تخصيص الموارد (R2) |
| الأدوار | مدير الموارد؛ المخطِّط |
| الشاشات | SCR-41 المجمعات والتخصيص والجدول الزمني للسعة |
| حالات الاستخدام | UC-054 |
| القصص | 11: 6 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يدير مدير الموارد مخزون كل نوع من الموارد وسعته ويرى المتاح والملتزم به ساعة بساعة.

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
| `US-BC05-RPL-ADJUST-CAPACITY` | تعديل سعة مجمع الموارد | أمر | مسودة |
| `US-BC05-RPL-CLOSE` | إغلاق مجمع الموارد | أمر | مسودة |
| `US-BC05-RPL-CREATE` | إنشاء مجمع الموارد | أمر | مسودة |
| `US-BC05-RPL-RESUME` | استئناف مجمع الموارد | أمر | مسودة |
| `US-BC05-RPL-SUSPEND` | تعليق مجمع الموارد | أمر | مسودة |
| `US-BC05-Q-POL-TIMELINE` | جلب: Capacity, committed and available quantity per hour in a window | جلب | مسودة |
| `US-DOM-RPL-GET` | عرض تفاصيل مجمع موارد واحد | جلب | مسودة |
| `US-DOM-RPL-LIST` | قائمة مجمعات الموارد ضمن نطاقي | جلب | مسودة |
| `US-UI-SCR41-CAPACITY-TIMELINE` | مخطط السعة والملتزم والمتاح ساعة بساعة | واجهة | مسودة |
| `US-UI-SCR41-POOL-VIEW` | صفحة مجمع واحد بسعته وحالته | واجهة | مسودة |
| `US-OPS-RPL-LEDGER-RECONCILE` | مطابقة دفتر السعة مع الالتزامات | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-RPL-ADJUST-CAPACITY — تعديل سعة مجمع الموارد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-RPL-ADJUST-CAPACITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/resource-pools/{id}/actions/adjust-capacity` | — |
| الأمر | `CMD-RPL-ADJUST-CAPACITY` | تعديل سعة مجمع الموارد |
| السياسة | `POL-RPL-ADJUST-CAPACITY` | Resource Manager؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RPL-CAPACITY-ADJUSTED` | يصل إلى: Capacity ledger |
| الكيان | `AGG-RESOURCE-POOL` | مجمع الموارد |
| الجدول | `readiness.resource_pools` | الجدول الرئيسي لمجمع الموارد |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-RESOURCE-POOL-SM، TST-SLC09-INVARIANTS | دورة حالات مجمع الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RPL-ADJUST-CAPACITY -->

</details>

### 5.2 US-BC05-RPL-CLOSE — إغلاق مجمع الموارد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-RPL-CLOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/resource-pools/{id}/actions/close` | — |
| الأمر | `CMD-RPL-CLOSE` | إغلاق مجمع الموارد |
| السياسة | `POL-RPL-CLOSE` | Resource Manager؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RPL-CLOSED` | يصل إلى: Capacity ledger |
| الكيان | `AGG-RESOURCE-POOL` | مجمع الموارد |
| الجدول | `readiness.resource_pools` | الجدول الرئيسي لمجمع الموارد |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-RESOURCE-POOL-SM، TST-SLC09-INVARIANTS | دورة حالات مجمع الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RPL-CLOSE -->

</details>

### 5.3 US-BC05-RPL-CREATE — إنشاء مجمع الموارد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-RPL-CREATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/resource-pools` | — |
| الأمر | `CMD-RPL-CREATE` | إنشاء مجمع الموارد |
| السياسة | `POL-RPL-CREATE` | Resource Manager؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RPL-CREATED` | يصل إلى: Capacity ledger |
| الكيان | `AGG-RESOURCE-POOL` | مجمع الموارد |
| الجدول | `readiness.resource_pools` | الجدول الرئيسي لمجمع الموارد |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-RESOURCE-POOL-SM، TST-SLC09-INVARIANTS | دورة حالات مجمع الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RPL-CREATE -->

</details>

### 5.4 US-BC05-RPL-RESUME — استئناف مجمع الموارد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-RPL-RESUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/resource-pools/{id}/actions/resume` | — |
| الأمر | `CMD-RPL-RESUME` | استئناف مجمع الموارد |
| السياسة | `POL-RPL-RESUME` | Resource Manager؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RPL-RESUMED` | يصل إلى: Capacity ledger |
| الكيان | `AGG-RESOURCE-POOL` | مجمع الموارد |
| الجدول | `readiness.resource_pools` | الجدول الرئيسي لمجمع الموارد |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-RESOURCE-POOL-SM، TST-SLC09-INVARIANTS | دورة حالات مجمع الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RPL-RESUME -->

</details>

### 5.5 US-BC05-RPL-SUSPEND — تعليق مجمع الموارد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-RPL-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/resource-pools/{id}/actions/suspend` | — |
| الأمر | `CMD-RPL-SUSPEND` | تعليق مجمع الموارد |
| السياسة | `POL-RPL-SUSPEND` | Resource Manager؛ tenant match; object visible; owner/pool scope |
| الحدث | `EVT-RPL-SUSPENDED` | يصل إلى: Capacity ledger |
| الكيان | `AGG-RESOURCE-POOL` | مجمع الموارد |
| الجدول | `readiness.resource_pools` | الجدول الرئيسي لمجمع الموارد |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-RESOURCE-POOL-SM، TST-SLC09-INVARIANTS | دورة حالات مجمع الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-RPL-SUSPEND -->

</details>

### 5.6 US-BC05-Q-POL-TIMELINE — جلب: Capacity, committed and available quantity per hour in a window

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-Q-POL-TIMELINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/resource-pools/{pool_id}/timeline` | — |
| الاستعلام | `QRY-POL-TIMELINE` | Capacity, committed and available quantity per hour in a window |
| السياسة | `POL-POL-TIMELINE` | pool scope |
| الكيان | `AGG-RESOURCE-POOL` | مجمع الموارد |
| الجدول | `readiness.resource_pools` | الجدول الرئيسي لمجمع الموارد |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
| الاختبار | TST-RESOURCE-POOL-SM، TST-SLC09-INVARIANTS | دورة حالات مجمع الموارد، وثوابت الشريحة SLC-09 |
<!-- END GENERATED: refs US-BC05-Q-POL-TIMELINE -->

</details>

### 5.7 US-DOM-RPL-GET — عرض تفاصيل مجمع موارد واحد

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-RPL-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-41 | شاشة المجمعات والتخصيص والجدول الزمني للسعة |
| المصدر | `21-ui-design.md §14` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
<!-- END GENERATED: refs US-DOM-RPL-GET -->

</details>

### 5.8 US-DOM-RPL-LIST — قائمة مجمعات الموارد ضمن نطاقي

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-RPL-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-41 | شاشة المجمعات والتخصيص والجدول الزمني للسعة |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
<!-- END GENERATED: refs US-DOM-RPL-LIST -->

</details>

### 5.9 US-UI-SCR41-CAPACITY-TIMELINE — مخطط السعة والملتزم والمتاح ساعة بساعة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR41-CAPACITY-TIMELINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-41 | شاشة المجمعات والتخصيص والجدول الزمني للسعة |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
<!-- END GENERATED: refs US-UI-SCR41-CAPACITY-TIMELINE -->

</details>

### 5.10 US-UI-SCR41-POOL-VIEW — صفحة مجمع واحد بسعته وحالته

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR41-POOL-VIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-41 | شاشة المجمعات والتخصيص والجدول الزمني للسعة |
| المصدر | `21-ui-design.md §14` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
<!-- END GENERATED: refs US-UI-SCR41-POOL-VIEW -->

</details>

### 5.11 US-OPS-RPL-LEDGER-RECONCILE — مطابقة دفتر السعة مع الالتزامات

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-RPL-LEDGER-RECONCILE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §12.9` | — |
| المتطلب | REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. |
| حالة الاستخدام | UC-054 | Allocate Resource |
<!-- END GENERATED: refs US-OPS-RPL-LEDGER-RECONCILE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. | `US-BC05-Q-POL-TIMELINE`، `US-BC05-RPL-ADJUST-CAPACITY`، `US-BC05-RPL-CLOSE`، `US-BC05-RPL-CREATE`، `US-BC05-RPL-RESUME`، `US-BC05-RPL-SUSPEND`، `US-DOM-RPL-GET`، `US-DOM-RPL-LIST`، `US-OPS-RPL-LEDGER-RECONCILE`، `US-UI-SCR41-CAPACITY-TIMELINE`، `US-UI-SCR41-POOL-VIEW` | TST-RESOURCE-POOL-SM، TST-SLC09-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
