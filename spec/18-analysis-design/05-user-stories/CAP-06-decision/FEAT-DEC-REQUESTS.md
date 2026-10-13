---
id: FEAT-DEC-REQUESTS
type: feature
title: "إعداد طلب القرار"
status: DRAFT
version: "0.1"
capability: CAP-06.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إعداد طلب القرار

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-DEC-REQUESTS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-06 إدارة القرار |
| القدرة الفرعية | CAP-06.01 طلبات القرار والخيارات (R1) |
| الأدوار | المحلل؛ المخطِّط؛ المدير؛ النظام |
| الشاشات | SCR-05 طلبات قرار تنتظرني |
| حالات الاستخدام | UC-030، UC-031 |
| القصص | 9: 7 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعرض المحلل أو المخطط على صاحب السلطة سؤالًا واضحًا بخيارات مدعومة بالتقييمات وموعد نهائي.

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
| `US-BC04-DRQ-ADD-OPTION` | إضافة خيار إلى طلب القرار | أمر | مسودة |
| `US-BC04-DRQ-CITE` | الاستشهاد في طلب القرار | أمر | مسودة |
| `US-BC04-DRQ-CREATE` | إنشاء طلب القرار | أمر | مسودة |
| `US-BC04-DRQ-OPEN` | فتح طلب القرار | أمر | مسودة |
| `US-BC04-DRQ-WITHDRAW` | سحب طلب القرار | أمر | مسودة |
| `US-BC04-Q-DRQ-GET` | جلب: Request with options and pinned citations (withheld per policy) | جلب | مسودة |
| `US-DOM-DEC-MY-REQUESTS` | طلبات القرار التي أعددتها وحالتها | جلب | مسودة |
| `US-BC04-S-DECISION-REQUEST-01` | تلقائي: deadline passed (طلب القرار) | نظام | مسودة |
| `US-UI-SCR05-REQUEST-FORM` | إعداد طلب القرار بخياراته واستشهاداته | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC04-DRQ-ADD-OPTION — إضافة خيار إلى طلب القرار

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

<!-- BEGIN GENERATED: refs US-BC04-DRQ-ADD-OPTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/decision-requests/{id}/actions/add-option` | — |
| الأمر | `CMD-DRQ-ADD-OPTION` | إضافة خيار إلى طلب القرار |
| السياسة | `POL-DRQ-ADD-OPTION` | Analyst / Planner / Manager (create, add, cite, open, withdraw)؛ tenant match; object visible; org scope |
| الحدث | `EVT-DRQ-OPTION-ADDED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-DECISION-REQUEST` | طلب القرار |
| الجدول | `operations.decision_requests` | الجدول الرئيسي لطلب القرار |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and… |
| حالات الاستخدام | UC-030، UC-031 | Create Decision Request؛ Evaluate Decision Options |
| الاختبار | TST-DECISION-REQUEST-SM، TST-SLC08-INVARIANTS | دورة حالات طلب القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-DRQ-ADD-OPTION -->

</details>

### 5.2 US-BC04-DRQ-CITE — الاستشهاد في طلب القرار

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

<!-- BEGIN GENERATED: refs US-BC04-DRQ-CITE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/decision-requests/{id}/actions/cite` | — |
| الأمر | `CMD-DRQ-CITE` | الاستشهاد في طلب القرار |
| السياسة | `POL-DRQ-CITE` | Analyst / Planner / Manager (create, add, cite, open, withdraw)؛ tenant match; object visible; org scope |
| الحدث | `EVT-DRQ-CITED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-DECISION-REQUEST` | طلب القرار |
| الجدول | `operations.decision_requests` | الجدول الرئيسي لطلب القرار |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and… |
| حالات الاستخدام | UC-030، UC-031 | Create Decision Request؛ Evaluate Decision Options |
| الاختبار | TST-DECISION-REQUEST-SM، TST-SLC08-INVARIANTS | دورة حالات طلب القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-DRQ-CITE -->

</details>

### 5.3 US-BC04-DRQ-CREATE — إنشاء طلب القرار

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

<!-- BEGIN GENERATED: refs US-BC04-DRQ-CREATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/decision-requests` | — |
| الأمر | `CMD-DRQ-CREATE` | إنشاء طلب القرار |
| السياسة | `POL-DRQ-CREATE` | Analyst / Planner / Manager (create, add, cite, open, withdraw)؛ tenant match; object visible; org scope |
| الحدث | `EVT-DRQ-CREATED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-DECISION-REQUEST` | طلب القرار |
| الجدول | `operations.decision_requests` | الجدول الرئيسي لطلب القرار |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and… |
| حالات الاستخدام | UC-030، UC-031 | Create Decision Request؛ Evaluate Decision Options |
| الاختبار | TST-DECISION-REQUEST-SM، TST-SLC08-INVARIANTS | دورة حالات طلب القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-DRQ-CREATE -->

</details>

### 5.4 US-BC04-DRQ-OPEN — فتح طلب القرار

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

<!-- BEGIN GENERATED: refs US-BC04-DRQ-OPEN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/decision-requests/{id}/actions/open` | — |
| الأمر | `CMD-DRQ-OPEN` | فتح طلب القرار |
| السياسة | `POL-DRQ-OPEN` | Analyst / Planner / Manager (create, add, cite, open, withdraw)؛ tenant match; object visible; org scope |
| الحدث | `EVT-DRQ-OPENED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-DECISION-REQUEST` | طلب القرار |
| الجدول | `operations.decision_requests` | الجدول الرئيسي لطلب القرار |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and… |
| حالات الاستخدام | UC-030، UC-031 | Create Decision Request؛ Evaluate Decision Options |
| الاختبار | TST-DECISION-REQUEST-SM، TST-SLC08-INVARIANTS | دورة حالات طلب القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-DRQ-OPEN -->

</details>

### 5.5 US-BC04-DRQ-WITHDRAW — سحب طلب القرار

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

<!-- BEGIN GENERATED: refs US-BC04-DRQ-WITHDRAW -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/operations/decision-requests/{id}/actions/withdraw` | — |
| الأمر | `CMD-DRQ-WITHDRAW` | سحب طلب القرار |
| السياسة | `POL-DRQ-WITHDRAW` | Analyst / Planner / Manager (create, add, cite, open, withdraw)؛ tenant match; object visible; org scope |
| الحدث | `EVT-DRQ-WITHDRAWN` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-DECISION-REQUEST` | طلب القرار |
| الجدول | `operations.decision_requests` | الجدول الرئيسي لطلب القرار |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and… |
| حالات الاستخدام | UC-030، UC-031 | Create Decision Request؛ Evaluate Decision Options |
| الاختبار | TST-DECISION-REQUEST-SM، TST-SLC08-INVARIANTS | دورة حالات طلب القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-DRQ-WITHDRAW -->

</details>

### 5.6 US-BC04-Q-DRQ-GET — جلب: Request with options and pinned citations (withheld per policy)

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

<!-- BEGIN GENERATED: refs US-BC04-Q-DRQ-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/operations/decision-requests/{request_id}` | — |
| الاستعلام | `QRY-DRQ-GET` | Request with options and pinned citations (withheld per policy) |
| السياسة | `POL-DRQ-GET` | label rule; required-authority holders in scope |
| الكيان | `AGG-DECISION-REQUEST` | طلب القرار |
| الجدول | `operations.decision_requests` | الجدول الرئيسي لطلب القرار |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and… |
| حالات الاستخدام | UC-030، UC-031 | Create Decision Request؛ Evaluate Decision Options |
| الاختبار | TST-DECISION-REQUEST-SM، TST-SLC08-INVARIANTS | دورة حالات طلب القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-Q-DRQ-GET -->

</details>

### 5.7 US-DOM-DEC-MY-REQUESTS — طلبات القرار التي أعددتها وحالتها

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

<!-- BEGIN GENERATED: refs US-DOM-DEC-MY-REQUESTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-030 | Create Decision Request |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and… |
| حالات الاستخدام | UC-030، UC-031 | Create Decision Request؛ Evaluate Decision Options |
<!-- END GENERATED: refs US-DOM-DEC-MY-REQUESTS -->

</details>

### 5.8 US-BC04-S-DECISION-REQUEST-01 — تلقائي: deadline passed (طلب القرار)

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

<!-- BEGIN GENERATED: refs US-BC04-S-DECISION-REQUEST-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:deadline passed` | escalates to holders of the required authority in scope |
| الانتقال | OPEN ← (بلا تغيير) | — |
| الحدث | `EVT-DRQ-ESCALATED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-DECISION-REQUEST` | طلب القرار |
| الجدول | `operations.decision_requests` | الجدول الرئيسي لطلب القرار |
| وحدة النشر | DU-08 | — |
| المتطلب | REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and… |
| حالات الاستخدام | UC-030، UC-031 | Create Decision Request؛ Evaluate Decision Options |
| الاختبار | TST-DECISION-REQUEST-SM، TST-SLC08-INVARIANTS | دورة حالات طلب القرار، وثوابت الشريحة SLC-08 |
<!-- END GENERATED: refs US-BC04-S-DECISION-REQUEST-01 -->

</details>

### 5.9 US-UI-SCR05-REQUEST-FORM — إعداد طلب القرار بخياراته واستشهاداته

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

<!-- BEGIN GENERATED: refs US-UI-SCR05-REQUEST-FORM -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-05 | شاشة طلبات قرار تنتظرني |
| المصدر | `THR-S08-05` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and… |
| حالات الاستخدام | UC-030، UC-031 | Create Decision Request؛ Evaluate Decision Options |
<!-- END GENERATED: refs US-UI-SCR05-REQUEST-FORM -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and… | `US-BC04-DRQ-ADD-OPTION`، `US-BC04-DRQ-CITE`، `US-BC04-DRQ-CREATE`، `US-BC04-DRQ-OPEN`، `US-BC04-DRQ-WITHDRAW`، `US-BC04-Q-DRQ-GET`، `US-BC04-S-DECISION-REQUEST-01`، `US-DOM-DEC-MY-REQUESTS`، `US-UI-SCR05-REQUEST-FORM` | TST-DECISION-REQUEST-SM، TST-SLC08-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
