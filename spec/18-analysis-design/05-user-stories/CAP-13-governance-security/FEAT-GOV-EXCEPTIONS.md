---
id: FEAT-GOV-EXCEPTIONS
type: feature
title: "الاستثناءات الأمنية المؤقتة"
status: DRAFT
version: "0.1"
capability: CAP-13.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# الاستثناءات الأمنية المؤقتة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-GOV-EXCEPTIONS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-13 الحوكمة والأمن والامتثال |
| القدرة الفرعية | CAP-13.01 التصنيف والسياسات (R1) |
| الأدوار | أي مستخدم مخوَّل؛ مسؤول الأمن؛ المدقِّق؛ النظام |
| الشاشات | SCR-67 التصنيف والتصاريح والاستثناءات |
| حالات الاستخدام | UC-088 |
| القصص | 11: 6 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمستخدم طلب استثناء أمني مؤقت بمبرر واضح يعتمده شخصان مخولان، ويُسحب تلقائيًا عند انتهاء مدته.

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
| `US-BC08-EXC-APPROVE` | اعتماد الاستثناء الأمني | أمر | مسودة |
| `US-BC08-EXC-REJECT` | رفض الاستثناء الأمني | أمر | مسودة |
| `US-BC08-EXC-REQUEST` | طلب الاستثناء الأمني | أمر | مسودة |
| `US-BC08-EXC-REVOKE` | سحب الاستثناء الأمني | أمر | مسودة |
| `US-BC08-Q-EXC-LIST` | جلب: Exceptions by state | جلب | مسودة |
| `US-BC08-S-SECURITY-EXCEPTION-01` | تلقائي: end reached (الاستثناء الأمني) | نظام | مسودة |
| `US-UI-SCR67-EXCEPTIONS` | متابعة الاستثناءات وموعد انتهائها ومعتمديها | واجهة | مسودة |
| `US-PLT-EXC-PDP-APPLY` | تطبيق الاستثناء النشط في قرار الوصول | منصة | مسودة |
| `US-OPS-BREAKGLASS-REVIEW` | مراجعة مستقلة لكل وصول طارئ | تشغيل | مسودة |
| `US-OPS-BREAKGLASS-TENANT-ACCESS` | وصول طارئ مؤقت للمشغل بموافقة الأمن | تشغيل | مسودة |
| `US-OPS-EXC-WEEKLY-REPORT` | تقرير أسبوعي بالاستثناءات النشطة للمدقق | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC08-EXC-APPROVE — اعتماد الاستثناء الأمني

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

<!-- BEGIN GENERATED: refs US-BC08-EXC-APPROVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/security-exceptions/{id}/actions/approve` | — |
| الأمر | `CMD-EXC-APPROVE` | اعتماد الاستثناء الأمني |
| السياسة | `POL-EXC-APPROVE` | authenticated user (request) \| Security Officer (approve/reject/revoke)؛ tenant match; subject ACTIVE; tenant… |
| الحدث | `EVT-EXC-ACTIVATED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الحدث | `EVT-EXC-FIRST-APPROVED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-SECURITY-EXCEPTION` | الاستثناء الأمني |
| الجدول | `governance.security_exceptions` | الجدول الرئيسي للاستثناء الأمني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-FND-017 | When a security exception is requested, the system shall require approval by two distinct authorized persons… |
| حالة الاستخدام | UC-088 | Request & Approve Security Exception |
| الاختبار | TST-SECURITY-EXCEPTION-SM، TST-SLC01-INVARIANTS | دورة حالات الاستثناء الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-EXC-APPROVE -->

</details>

### 5.2 US-BC08-EXC-REJECT — رفض الاستثناء الأمني

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

<!-- BEGIN GENERATED: refs US-BC08-EXC-REJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/security-exceptions/{id}/actions/reject` | — |
| الأمر | `CMD-EXC-REJECT` | رفض الاستثناء الأمني |
| السياسة | `POL-EXC-REJECT` | authenticated user (request) \| Security Officer (approve/reject/revoke)؛ tenant match; subject ACTIVE; tenant… |
| الحدث | `EVT-EXC-REJECTED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-SECURITY-EXCEPTION` | الاستثناء الأمني |
| الجدول | `governance.security_exceptions` | الجدول الرئيسي للاستثناء الأمني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-FND-017 | When a security exception is requested, the system shall require approval by two distinct authorized persons… |
| حالة الاستخدام | UC-088 | Request & Approve Security Exception |
| الاختبار | TST-SECURITY-EXCEPTION-SM، TST-SLC01-INVARIANTS | دورة حالات الاستثناء الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-EXC-REJECT -->

</details>

### 5.3 US-BC08-EXC-REQUEST — طلب الاستثناء الأمني

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

<!-- BEGIN GENERATED: refs US-BC08-EXC-REQUEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/security-exceptions` | — |
| الأمر | `CMD-EXC-REQUEST` | طلب الاستثناء الأمني |
| السياسة | `POL-EXC-REQUEST` | authenticated user (request) \| Security Officer (approve/reject/revoke)؛ tenant match; subject ACTIVE; tenant… |
| الحدث | `EVT-EXC-REQUESTED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-SECURITY-EXCEPTION` | الاستثناء الأمني |
| الجدول | `governance.security_exceptions` | الجدول الرئيسي للاستثناء الأمني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-FND-017 | When a security exception is requested, the system shall require approval by two distinct authorized persons… |
| حالة الاستخدام | UC-088 | Request & Approve Security Exception |
| الاختبار | TST-SECURITY-EXCEPTION-SM، TST-SLC01-INVARIANTS | دورة حالات الاستثناء الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-EXC-REQUEST -->

</details>

### 5.4 US-BC08-EXC-REVOKE — سحب الاستثناء الأمني

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

<!-- BEGIN GENERATED: refs US-BC08-EXC-REVOKE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/security-exceptions/{id}/actions/revoke` | — |
| الأمر | `CMD-EXC-REVOKE` | سحب الاستثناء الأمني |
| السياسة | `POL-EXC-REVOKE` | authenticated user (request) \| Security Officer (approve/reject/revoke)؛ tenant match; subject ACTIVE; tenant… |
| الحدث | `EVT-EXC-REVOKED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-SECURITY-EXCEPTION` | الاستثناء الأمني |
| الجدول | `governance.security_exceptions` | الجدول الرئيسي للاستثناء الأمني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-FND-017 | When a security exception is requested, the system shall require approval by two distinct authorized persons… |
| حالة الاستخدام | UC-088 | Request & Approve Security Exception |
| الاختبار | TST-SECURITY-EXCEPTION-SM، TST-SLC01-INVARIANTS | دورة حالات الاستثناء الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-EXC-REVOKE -->

</details>

### 5.5 US-BC08-Q-EXC-LIST — جلب: Exceptions by state

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

<!-- BEGIN GENERATED: refs US-BC08-Q-EXC-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/governance/security-exceptions` | — |
| الاستعلام | `QRY-EXC-LIST` | Exceptions by state |
| السياسة | `POL-EXC-LIST` | org scope of subject roles ∩ classification rule |
| الكيان | `AGG-SECURITY-EXCEPTION` | الاستثناء الأمني |
| الجدول | `governance.security_exceptions` | الجدول الرئيسي للاستثناء الأمني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-FND-017 | When a security exception is requested, the system shall require approval by two distinct authorized persons… |
| حالة الاستخدام | UC-088 | Request & Approve Security Exception |
| الاختبار | TST-SECURITY-EXCEPTION-SM، TST-SLC01-INVARIANTS | دورة حالات الاستثناء الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-Q-EXC-LIST -->

</details>

### 5.6 US-BC08-S-SECURITY-EXCEPTION-01 — تلقائي: end reached (الاستثناء الأمني)

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

<!-- BEGIN GENERATED: refs US-BC08-S-SECURITY-EXCEPTION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:end reached` | scheduler |
| الانتقال | ACTIVE ← EXPIRED | — |
| الحدث | `EVT-EXC-EXPIRED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-SECURITY-EXCEPTION` | الاستثناء الأمني |
| الجدول | `governance.security_exceptions` | الجدول الرئيسي للاستثناء الأمني |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-FND-017 | When a security exception is requested, the system shall require approval by two distinct authorized persons… |
| حالة الاستخدام | UC-088 | Request & Approve Security Exception |
| الاختبار | TST-SECURITY-EXCEPTION-SM، TST-SLC01-INVARIANTS | دورة حالات الاستثناء الأمني، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-S-SECURITY-EXCEPTION-01 -->

</details>

### 5.7 US-UI-SCR67-EXCEPTIONS — متابعة الاستثناءات وموعد انتهائها ومعتمديها

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

<!-- BEGIN GENERATED: refs US-UI-SCR67-EXCEPTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-088 | Request & Approve Security Exception |
| الشاشة | SCR-67 | شاشة التصنيف والتصاريح والاستثناءات |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-017 | When a security exception is requested, the system shall require approval by two distinct authorized persons… |
| حالة الاستخدام | UC-088 | Request & Approve Security Exception |
<!-- END GENERATED: refs US-UI-SCR67-EXCEPTIONS -->

</details>

### 5.8 US-PLT-EXC-PDP-APPLY — تطبيق الاستثناء النشط في قرار الوصول

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

<!-- BEGIN GENERATED: refs US-PLT-EXC-PDP-APPLY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §3.1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-017 | When a security exception is requested, the system shall require approval by two distinct authorized persons… |
| حالة الاستخدام | UC-088 | Request & Approve Security Exception |
<!-- END GENERATED: refs US-PLT-EXC-PDP-APPLY -->

</details>

### 5.9 US-OPS-BREAKGLASS-REVIEW — مراجعة مستقلة لكل وصول طارئ

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

<!-- BEGIN GENERATED: refs US-OPS-BREAKGLASS-REVIEW -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §10` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-BREAKGLASS-REVIEW -->

</details>

### 5.10 US-OPS-BREAKGLASS-TENANT-ACCESS — وصول طارئ مؤقت للمشغل بموافقة الأمن

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

<!-- BEGIN GENERATED: refs US-OPS-BREAKGLASS-TENANT-ACCESS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §10` | — |
| المصدر | `17-security-design.md §1` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-BREAKGLASS-TENANT-ACCESS -->

</details>

### 5.11 US-OPS-EXC-WEEKLY-REPORT — تقرير أسبوعي بالاستثناءات النشطة للمدقق

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

<!-- BEGIN GENERATED: refs US-OPS-EXC-WEEKLY-REPORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/observability-slc01.md §signals` | — |
<!-- END GENERATED: refs US-OPS-EXC-WEEKLY-REPORT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-017 | When a security exception is requested, the system shall require approval by two distinct authorized persons… | `US-BC08-EXC-APPROVE`، `US-BC08-EXC-REJECT`، `US-BC08-EXC-REQUEST`، `US-BC08-EXC-REVOKE`، `US-BC08-Q-EXC-LIST`، `US-BC08-S-SECURITY-EXCEPTION-01`، `US-PLT-EXC-PDP-APPLY`، `US-UI-SCR67-EXCEPTIONS` | TST-SECURITY-EXCEPTION-SM، TST-SLC01-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
