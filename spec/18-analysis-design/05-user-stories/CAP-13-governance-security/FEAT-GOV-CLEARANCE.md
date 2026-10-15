---
id: FEAT-GOV-CLEARANCE
type: feature
title: "التصاريح الأمنية للمستخدمين"
status: DRAFT
version: "0.1"
capability: CAP-13.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# التصاريح الأمنية للمستخدمين

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-GOV-CLEARANCE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-13 الحوكمة والأمن والامتثال |
| القدرة الفرعية | CAP-13.01 التصنيف والسياسات (R1) |
| الأدوار | مسؤول الأمن؛ أي مستخدم مخوَّل؛ النظام |
| الشاشات | SCR-67 التصنيف والتصاريح والاستثناءات |
| حالات الاستخدام | UC-089، UC-085 |
| القصص | 11: 8 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لمسؤول الأمن منح كل مستخدم مستوى سرية وحجرات محددة واعتمادها وتعديلها وتعليقها وسحبها، فلا يرى إلا ما يسمح به تصريحه.

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
| QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance | 0 leakage in inference suite (counts, facets, ordering, timing, errors) |
| QAS-SEC-003 | removes a user's compartment | effective on next request in every path, independent of index lag |
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
| `US-BC01-CLR-APPROVE` | اعتماد التصريح الأمني | أمر | مسودة |
| `US-BC01-CLR-GRANT` | منح التصريح الأمني | أمر | مسودة |
| `US-BC01-CLR-MODIFY` | تعديل التصريح الأمني | أمر | مسودة |
| `US-BC01-CLR-REINSTATE` | إعادة التصريح الأمني إلى السريان | أمر | مسودة |
| `US-BC01-CLR-REVOKE` | سحب التصريح الأمني | أمر | مسودة |
| `US-BC01-CLR-SUSPEND` | تعليق التصريح الأمني | أمر | مسودة |
| `US-BC01-Q-CLR-GET` | جلب: Current clearance (level/compartments) | جلب | مسودة |
| `US-BC01-S-CLEARANCE-01` | تلقائي: valid_to reached (التصريح الأمني) | نظام | مسودة |
| `US-UI-SCR67-CLEARANCE-VIEW` | عرض تصريح المستخدم وحالة اعتماده | واجهة | مسودة |
| `US-PLT-CLR-READ-RULE` | السماح بالقراءة حسب التصريح والأقسام | منصة | مسودة |
| `US-OPS-CLR-AGGREGATE-REPORT` | تقرير مجمّع بالتصاريح حسب المستوى | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-CLR-APPROVE — اعتماد التصريح الأمني

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

<!-- BEGIN GENERATED: refs US-BC01-CLR-APPROVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/clearances/{id}/actions/approve` | — |
| الأمر | `CMD-CLR-APPROVE` | اعتماد التصريح الأمني |
| السياسة | `POL-CLR-APPROVE` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-CLR-GRANTED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-CLEARANCE` | التصريح الأمني |
| الجدول | `foundation.clearances` | الجدول الرئيسي للتصريح الأمني |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-GOV-003، REQ-GOV-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-085، UC-089 | Manage Classification Scheme & Compartments؛ Manage User Clearance |
| الاختبار | TST-CLEARANCE-SM، TST-SLC01-INVARIANTS | دورة حالات التصريح الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-CLR-APPROVE -->

</details>

### 5.2 US-BC01-CLR-GRANT — منح التصريح الأمني

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

<!-- BEGIN GENERATED: refs US-BC01-CLR-GRANT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/clearances` | — |
| الأمر | `CMD-CLR-GRANT` | منح التصريح الأمني |
| السياسة | `POL-CLR-GRANT` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-CLR-REQUESTED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-CLEARANCE` | التصريح الأمني |
| الجدول | `foundation.clearances` | الجدول الرئيسي للتصريح الأمني |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-GOV-003، REQ-GOV-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-085، UC-089 | Manage Classification Scheme & Compartments؛ Manage User Clearance |
| الاختبار | TST-CLEARANCE-SM، TST-SLC01-INVARIANTS | دورة حالات التصريح الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-CLR-GRANT -->

</details>

### 5.3 US-BC01-CLR-MODIFY — تعديل التصريح الأمني

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

<!-- BEGIN GENERATED: refs US-BC01-CLR-MODIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/clearances/{id}/actions/modify` | — |
| الأمر | `CMD-CLR-MODIFY` | تعديل التصريح الأمني |
| السياسة | `POL-CLR-MODIFY` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-CLR-MODIFIED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-CLEARANCE` | التصريح الأمني |
| الجدول | `foundation.clearances` | الجدول الرئيسي للتصريح الأمني |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-GOV-003، REQ-GOV-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-085، UC-089 | Manage Classification Scheme & Compartments؛ Manage User Clearance |
| الاختبار | TST-CLEARANCE-SM، TST-SLC01-INVARIANTS | دورة حالات التصريح الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-CLR-MODIFY -->

</details>

### 5.4 US-BC01-CLR-REINSTATE — إعادة التصريح الأمني إلى السريان

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

<!-- BEGIN GENERATED: refs US-BC01-CLR-REINSTATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/clearances/{id}/actions/reinstate` | — |
| الأمر | `CMD-CLR-REINSTATE` | إعادة التصريح الأمني إلى السريان |
| السياسة | `POL-CLR-REINSTATE` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-CLR-REINSTATED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-CLEARANCE` | التصريح الأمني |
| الجدول | `foundation.clearances` | الجدول الرئيسي للتصريح الأمني |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-GOV-003، REQ-GOV-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-085، UC-089 | Manage Classification Scheme & Compartments؛ Manage User Clearance |
| الاختبار | TST-CLEARANCE-SM، TST-SLC01-INVARIANTS | دورة حالات التصريح الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-CLR-REINSTATE -->

</details>

### 5.5 US-BC01-CLR-REVOKE — سحب التصريح الأمني

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

<!-- BEGIN GENERATED: refs US-BC01-CLR-REVOKE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/clearances/{id}/actions/revoke` | — |
| الأمر | `CMD-CLR-REVOKE` | سحب التصريح الأمني |
| السياسة | `POL-CLR-REVOKE` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-CLR-REVOKED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-CLEARANCE` | التصريح الأمني |
| الجدول | `foundation.clearances` | الجدول الرئيسي للتصريح الأمني |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-GOV-003، REQ-GOV-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-085، UC-089 | Manage Classification Scheme & Compartments؛ Manage User Clearance |
| الاختبار | TST-CLEARANCE-SM، TST-SLC01-INVARIANTS | دورة حالات التصريح الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-CLR-REVOKE -->

</details>

### 5.6 US-BC01-CLR-SUSPEND — تعليق التصريح الأمني

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

<!-- BEGIN GENERATED: refs US-BC01-CLR-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/clearances/{id}/actions/suspend` | — |
| الأمر | `CMD-CLR-SUSPEND` | تعليق التصريح الأمني |
| السياسة | `POL-CLR-SUSPEND` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-CLR-SUSPENDED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-CLEARANCE` | التصريح الأمني |
| الجدول | `foundation.clearances` | الجدول الرئيسي للتصريح الأمني |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-GOV-003، REQ-GOV-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-085، UC-089 | Manage Classification Scheme & Compartments؛ Manage User Clearance |
| الاختبار | TST-CLEARANCE-SM، TST-SLC01-INVARIANTS | دورة حالات التصريح الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-CLR-SUSPEND -->

</details>

### 5.7 US-BC01-Q-CLR-GET — جلب: Current clearance (level/compartments)

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

<!-- BEGIN GENERATED: refs US-BC01-Q-CLR-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/foundation/users/{user_id}/clearance` | — |
| الاستعلام | `QRY-CLR-GET` | Current clearance (level/compartments) |
| السياسة | `POL-CLR-GET` | org scope of subject roles ∩ classification rule |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-GOV-003 | The system shall permit read access to an object only if the subject's clearance is at least the object's lev… |
| حالة الاستخدام | UC-089 | Manage User Clearance |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-Q-CLR-GET -->

</details>

### 5.8 US-BC01-S-CLEARANCE-01 — تلقائي: valid_to reached (التصريح الأمني)

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

<!-- BEGIN GENERATED: refs US-BC01-S-CLEARANCE-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:valid_to reached` | system |
| الانتقال | ACTIVE, SUSPENDED ← EXPIRED | — |
| الحدث | `EVT-CLR-EXPIRED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-CLEARANCE` | التصريح الأمني |
| الجدول | `foundation.clearances` | الجدول الرئيسي للتصريح الأمني |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-GOV-003، REQ-GOV-004 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-085، UC-089 | Manage Classification Scheme & Compartments؛ Manage User Clearance |
| الاختبار | TST-CLEARANCE-SM، TST-SLC01-INVARIANTS | دورة حالات التصريح الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-S-CLEARANCE-01 -->

</details>

### 5.9 US-UI-SCR67-CLEARANCE-VIEW — عرض تصريح المستخدم وحالة اعتماده

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

<!-- BEGIN GENERATED: refs US-UI-SCR67-CLEARANCE-VIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-089 | Manage User Clearance |
| الشاشة | SCR-67 | شاشة التصنيف والتصاريح والاستثناءات |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR67-CLEARANCE-VIEW -->

</details>

### 5.10 US-PLT-CLR-READ-RULE — السماح بالقراءة حسب التصريح والأقسام

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

<!-- BEGIN GENERATED: refs US-PLT-CLR-READ-RULE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance → 0 leakage in inference suite (cou… |
| المصدر | `17-security-design.md §4` | — |
| المتطلب | REQ-GOV-003 | The system shall permit read access to an object only if the subject's clearance is at least the object's lev… |
| حالة الاستخدام | UC-089 | Manage User Clearance |
<!-- END GENERATED: refs US-PLT-CLR-READ-RULE -->

</details>

### 5.11 US-OPS-CLR-AGGREGATE-REPORT — تقرير مجمّع بالتصاريح حسب المستوى

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

<!-- BEGIN GENERATED: refs US-OPS-CLR-AGGREGATE-REPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/observability-slc01.md §business_telemetry` | — |
<!-- END GENERATED: refs US-OPS-CLR-AGGREGATE-REPORT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-GOV-003 | The system shall permit read access to an object only if the subject's clearance is at least the object's lev… | `US-BC01-CLR-APPROVE`، `US-BC01-CLR-GRANT`، `US-BC01-CLR-MODIFY`، `US-BC01-CLR-REINSTATE`، `US-BC01-CLR-REVOKE`، `US-BC01-CLR-SUSPEND`، `US-BC01-Q-CLR-GET`، `US-BC01-S-CLEARANCE-01`، `US-PLT-CLR-READ-RULE` | TST-CLEARANCE-SM، TST-SLC01-INVARIANTS |
| REQ-GOV-004 | When the classification of an object is changed, the system shall require the authority defined by tenant pol… | كل قصص الأوامر والنظام في الميزة (7) | TST-CLASSIFICATION-SCHEME-SM، TST-CLEARANCE-SM، TST-SLC01-INVARIANTS، TST-SLC05-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
