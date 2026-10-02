---
id: FEAT-ORG-AUTHORITY-GRANTS
type: feature
title: "منح صلاحيات القرار"
status: DRAFT
version: "0.1"
capability: CAP-01.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# منح صلاحيات القرار

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-AUTHORITY-GRANTS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.03 السلطة والتفويض (R1) |
| الأدوار | صاحب السلطة أو المعتمِد الثاني؛ القيادي التنفيذي؛ مسؤول الإدارة؛ النظام |
| الشاشات | SCR-62 المستخدمون والأدوار والسلطة |
| حالات الاستخدام | UC-082، UC-032، UC-035 |
| القصص | 10: 8 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يحدد بوضوح من يملك سلطة اتخاذ كل نوع من القرارات وفي أي نطاق وحدود ومدة، مع اعتماد المنح وتعليقه وسحبه وانتهائه تلقائيًا.

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
| `US-BC01-AUT-APPROVE-GRANT` | اعتماد منح السلطة | أمر | مسودة |
| `US-BC01-AUT-GRANT` | إصدار منح السلطة | أمر | مسودة |
| `US-BC01-AUT-REJECT-GRANT` | رفض منح السلطة | أمر | مسودة |
| `US-BC01-AUT-RESUME` | استئناف منح السلطة | أمر | مسودة |
| `US-BC01-AUT-REVOKE` | سحب منح السلطة | أمر | مسودة |
| `US-BC01-AUT-SUSPEND` | تعليق منح السلطة | أمر | مسودة |
| `US-BC01-Q-AUT-LIST` | جلب: Grants by holder / scope / effective at t | جلب | مسودة |
| `US-BC01-S-AUTHORITY-GRANT-01` | تلقائي: valid_to reached (منح السلطة) | نظام | مسودة |
| `US-UI-SCR62-AUTHORITY-GRANTS` | عرض منح السلطة بنطاقها وحدودها ومدتها | واجهة | مسودة |
| `US-PLT-AUT-READTIME-VALIDITY` | فرض انتهاء السلطة لحظة التحقق | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-AUT-APPROVE-GRANT — اعتماد منح السلطة

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

<!-- BEGIN GENERATED: refs US-BC01-AUT-APPROVE-GRANT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/authority-grants/{id}/actions/approve-grant` | — |
| الأمر | `CMD-AUT-APPROVE-GRANT` | اعتماد منح السلطة |
| السياسة | `POL-AUT-APPROVE-GRANT` | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delega… |
| الحدث | `EVT-AUT-GRANTED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-AUTHORITY-GRANT` | منح السلطة |
| الجدول | `foundation.authority_grants` | الجدول الرئيسي لمنح السلطة |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-007، REQ-FND-008، REQ-FND-009 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-032، UC-035، UC-082 | Record Decision؛ Approve Plan؛ Manage Role & Authority |
| الاختبار | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS | دورة حالات منح السلطة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-AUT-APPROVE-GRANT -->

</details>

### 5.2 US-BC01-AUT-GRANT — إصدار منح السلطة

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

<!-- BEGIN GENERATED: refs US-BC01-AUT-GRANT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/authority-grants` | — |
| الأمر | `CMD-AUT-GRANT` | إصدار منح السلطة |
| السياسة | `POL-AUT-GRANT` | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delega… |
| الحدث | `EVT-AUT-GRANT-REQUESTED` | يصل إلى: Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| الكيان | `AGG-AUTHORITY-GRANT` | منح السلطة |
| الجدول | `foundation.authority_grants` | الجدول الرئيسي لمنح السلطة |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-007، REQ-FND-008، REQ-FND-009 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-032، UC-035، UC-082 | Record Decision؛ Approve Plan؛ Manage Role & Authority |
| الاختبار | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS | دورة حالات منح السلطة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-AUT-GRANT -->

</details>

### 5.3 US-BC01-AUT-REJECT-GRANT — رفض منح السلطة

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

<!-- BEGIN GENERATED: refs US-BC01-AUT-REJECT-GRANT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/authority-grants/{id}/actions/reject-grant` | — |
| الأمر | `CMD-AUT-REJECT-GRANT` | رفض منح السلطة |
| السياسة | `POL-AUT-REJECT-GRANT` | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delega… |
| الحدث | `EVT-AUT-GRANT-REJECTED` | يصل إلى: Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| الكيان | `AGG-AUTHORITY-GRANT` | منح السلطة |
| الجدول | `foundation.authority_grants` | الجدول الرئيسي لمنح السلطة |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-007، REQ-FND-008، REQ-FND-009 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-032، UC-035، UC-082 | Record Decision؛ Approve Plan؛ Manage Role & Authority |
| الاختبار | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS | دورة حالات منح السلطة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-AUT-REJECT-GRANT -->

</details>

### 5.4 US-BC01-AUT-RESUME — استئناف منح السلطة

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

<!-- BEGIN GENERATED: refs US-BC01-AUT-RESUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/authority-grants/{id}/actions/resume` | — |
| الأمر | `CMD-AUT-RESUME` | استئناف منح السلطة |
| السياسة | `POL-AUT-RESUME` | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delega… |
| الحدث | `EVT-AUT-RESUMED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-AUTHORITY-GRANT` | منح السلطة |
| الجدول | `foundation.authority_grants` | الجدول الرئيسي لمنح السلطة |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-007، REQ-FND-008، REQ-FND-009 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-032، UC-035، UC-082 | Record Decision؛ Approve Plan؛ Manage Role & Authority |
| الاختبار | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS | دورة حالات منح السلطة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-AUT-RESUME -->

</details>

### 5.5 US-BC01-AUT-REVOKE — سحب منح السلطة

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

<!-- BEGIN GENERATED: refs US-BC01-AUT-REVOKE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/authority-grants/{id}/actions/revoke` | — |
| الأمر | `CMD-AUT-REVOKE` | سحب منح السلطة |
| السياسة | `POL-AUT-REVOKE` | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delega… |
| الحدث | `EVT-AUT-REVOKED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-AUTHORITY-GRANT` | منح السلطة |
| الجدول | `foundation.authority_grants` | الجدول الرئيسي لمنح السلطة |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-007، REQ-FND-008، REQ-FND-009 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-032، UC-035، UC-082 | Record Decision؛ Approve Plan؛ Manage Role & Authority |
| الاختبار | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS | دورة حالات منح السلطة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-AUT-REVOKE -->

</details>

### 5.6 US-BC01-AUT-SUSPEND — تعليق منح السلطة

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

<!-- BEGIN GENERATED: refs US-BC01-AUT-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/authority-grants/{id}/actions/suspend` | — |
| الأمر | `CMD-AUT-SUSPEND` | تعليق منح السلطة |
| السياسة | `POL-AUT-SUSPEND` | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delega… |
| الحدث | `EVT-AUT-SUSPENDED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-AUTHORITY-GRANT` | منح السلطة |
| الجدول | `foundation.authority_grants` | الجدول الرئيسي لمنح السلطة |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-007، REQ-FND-008، REQ-FND-009 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-032، UC-035، UC-082 | Record Decision؛ Approve Plan؛ Manage Role & Authority |
| الاختبار | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS | دورة حالات منح السلطة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-AUT-SUSPEND -->

</details>

### 5.7 US-BC01-Q-AUT-LIST — جلب: Grants by holder / scope / effective at t

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

<!-- BEGIN GENERATED: refs US-BC01-Q-AUT-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/foundation/authority-grants` | — |
| الاستعلام | `QRY-AUT-LIST` | Grants by holder / scope / effective at t |
| السياسة | `POL-AUT-LIST` | org scope of subject roles ∩ classification rule |
| الكيان | `AGG-AUTHORITY-GRANT` | منح السلطة |
| الجدول | `foundation.authority_grants` | الجدول الرئيسي لمنح السلطة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-007 | The system shall record authority as a grant stating decision type, organizational scope, limits and validity… |
| حالة الاستخدام | UC-082 | Manage Role & Authority |
| الاختبار | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS | دورة حالات منح السلطة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-Q-AUT-LIST -->

</details>

### 5.8 US-BC01-S-AUTHORITY-GRANT-01 — تلقائي: valid_to reached (منح السلطة)

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

<!-- BEGIN GENERATED: refs US-BC01-S-AUTHORITY-GRANT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:valid_to reached` | system scheduler |
| الانتقال | ACTIVE, SUSPENDED ← EXPIRED | — |
| الحدث | `EVT-AUT-EXPIRED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-AUTHORITY-GRANT` | منح السلطة |
| الجدول | `foundation.authority_grants` | الجدول الرئيسي لمنح السلطة |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-007، REQ-FND-008، REQ-FND-009 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-032، UC-035، UC-082 | Record Decision؛ Approve Plan؛ Manage Role & Authority |
| الاختبار | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS | دورة حالات منح السلطة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-S-AUTHORITY-GRANT-01 -->

</details>

### 5.9 US-UI-SCR62-AUTHORITY-GRANTS — عرض منح السلطة بنطاقها وحدودها ومدتها

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

<!-- BEGIN GENERATED: refs US-UI-SCR62-AUTHORITY-GRANTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-082 | Manage Role & Authority |
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| المصدر | `21-ui-design.md §5` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-007 | The system shall record authority as a grant stating decision type, organizational scope, limits and validity… |
| حالة الاستخدام | UC-082 | Manage Role & Authority |
<!-- END GENERATED: refs US-UI-SCR62-AUTHORITY-GRANTS -->

</details>

### 5.10 US-PLT-AUT-READTIME-VALIDITY — فرض انتهاء السلطة لحظة التحقق

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

<!-- BEGIN GENERATED: refs US-PLT-AUT-READTIME-VALIDITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/degradation-slc01.md §matrix` | — |
| المتطلب | REQ-FND-007 | The system shall record authority as a grant stating decision type, organizational scope, limits and validity… |
| حالة الاستخدام | UC-082 | Manage Role & Authority |
<!-- END GENERATED: refs US-PLT-AUT-READTIME-VALIDITY -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-007 | The system shall record authority as a grant stating decision type, organizational scope, limits and validity… | `US-BC01-AUT-APPROVE-GRANT`، `US-BC01-AUT-GRANT`، `US-BC01-AUT-REJECT-GRANT`، `US-BC01-AUT-RESUME`، `US-BC01-AUT-REVOKE`، `US-BC01-AUT-SUSPEND`، `US-BC01-Q-AUT-LIST`، `US-BC01-S-AUTHORITY-GRANT-01`، `US-PLT-AUT-READTIME-VALIDITY`، `US-UI-SCR62-AUTHORITY-GRANTS` | TST-AUTHORITY-GRANT-SM |
| REQ-FND-008 | When an authority holder delegates authority, the system shall record delegator, delegate, scope, limits and… | كل قصص الأوامر والنظام في الميزة (7) | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS |
| REQ-FND-009 | The system shall provide an authority check returning whether an actor holds authority for a given decision t… | كل قصص الأوامر والنظام في الميزة (7) | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
