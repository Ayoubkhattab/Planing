---
id: FEAT-ORG-SERVICE-ACCOUNTS
type: feature
title: "حسابات الخدمة للأنظمة"
status: DRAFT
version: "0.1"
capability: CAP-01.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# حسابات الخدمة للأنظمة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-SERVICE-ACCOUNTS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.02 الهوية والمصادقة والاتحاد (R1) |
| الأدوار | مسؤول الإدارة |
| الشاشات | SCR-62 المستخدمون والأدوار والسلطة، SCR-65 المحوّلات والاتصالات والحساسات |
| حالات الاستخدام | UC-084 |
| القصص | 9: 5 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمسؤول منح الأنظمة المتكاملة حسابات خاصة بها يمكن تعطيلها وتجديد بيانات اعتمادها وإغلاقها دون المساس بحسابات الأشخاص.

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
| `US-BC01-SVC-CLOSE` | إغلاق حساب الخدمة | أمر | مسودة |
| `US-BC01-SVC-CREATE` | إنشاء حساب الخدمة | أمر | مسودة |
| `US-BC01-SVC-DISABLE` | تعطيل حساب الخدمة | أمر | مسودة |
| `US-BC01-SVC-ENABLE` | تمكين حساب الخدمة | أمر | مسودة |
| `US-BC01-SVC-ROTATE-CREDENTIAL` | تدوير بيانات اعتماد حساب الخدمة | أمر | مسودة |
| `US-DOM-SVC-LIST` | عرض حسابات الخدمة وحالة بيانات اعتمادها | جلب | مسودة |
| `US-UI-SCR62-SERVICE-ACCOUNTS` | إدارة حسابات الخدمة وتجديد بيانات اعتمادها | واجهة | مسودة |
| `US-INT-SVC-KEY-AUTHENTICATION` | مصادقة الأنظمة المتكاملة بمفتاح حساب الخدمة | تكامل | مسودة |
| `US-OPS-SVC-CREDENTIAL-EXPIRY` | تنبيه قبل انتهاء بيانات اعتماد حساب الخدمة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-SVC-CLOSE — إغلاق حساب الخدمة

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

<!-- BEGIN GENERATED: refs US-BC01-SVC-CLOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/service-accounts/{id}/actions/close` | — |
| الأمر | `CMD-SVC-CLOSE` | إغلاق حساب الخدمة |
| السياسة | `POL-SVC-CLOSE` | Administrator؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-SVC-CLOSED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-SERVICE-ACCOUNT` | حساب الخدمة |
| الجدول | `foundation.service_accounts` | الجدول الرئيسي لحساب الخدمة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-SERVICE-ACCOUNT-SM، TST-SLC01-INVARIANTS | دورة حالات حساب الخدمة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-SVC-CLOSE -->

</details>

### 5.2 US-BC01-SVC-CREATE — إنشاء حساب الخدمة

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

<!-- BEGIN GENERATED: refs US-BC01-SVC-CREATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/service-accounts` | — |
| الأمر | `CMD-SVC-CREATE` | إنشاء حساب الخدمة |
| السياسة | `POL-SVC-CREATE` | Administrator؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-SVC-CREATED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-SERVICE-ACCOUNT` | حساب الخدمة |
| الجدول | `foundation.service_accounts` | الجدول الرئيسي لحساب الخدمة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-SERVICE-ACCOUNT-SM، TST-SLC01-INVARIANTS | دورة حالات حساب الخدمة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-SVC-CREATE -->

</details>

### 5.3 US-BC01-SVC-DISABLE — تعطيل حساب الخدمة

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

<!-- BEGIN GENERATED: refs US-BC01-SVC-DISABLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/service-accounts/{id}/actions/disable` | — |
| الأمر | `CMD-SVC-DISABLE` | تعطيل حساب الخدمة |
| السياسة | `POL-SVC-DISABLE` | Administrator؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-SVC-DISABLED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-SERVICE-ACCOUNT` | حساب الخدمة |
| الجدول | `foundation.service_accounts` | الجدول الرئيسي لحساب الخدمة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-SERVICE-ACCOUNT-SM، TST-SLC01-INVARIANTS | دورة حالات حساب الخدمة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-SVC-DISABLE -->

</details>

### 5.4 US-BC01-SVC-ENABLE — تمكين حساب الخدمة

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

<!-- BEGIN GENERATED: refs US-BC01-SVC-ENABLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/service-accounts/{id}/actions/enable` | — |
| الأمر | `CMD-SVC-ENABLE` | تمكين حساب الخدمة |
| السياسة | `POL-SVC-ENABLE` | Administrator؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-SVC-ENABLED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-SERVICE-ACCOUNT` | حساب الخدمة |
| الجدول | `foundation.service_accounts` | الجدول الرئيسي لحساب الخدمة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-SERVICE-ACCOUNT-SM، TST-SLC01-INVARIANTS | دورة حالات حساب الخدمة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-SVC-ENABLE -->

</details>

### 5.5 US-BC01-SVC-ROTATE-CREDENTIAL — تدوير بيانات اعتماد حساب الخدمة

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

<!-- BEGIN GENERATED: refs US-BC01-SVC-ROTATE-CREDENTIAL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/service-accounts/{id}/actions/rotate-credential` | — |
| الأمر | `CMD-SVC-ROTATE-CREDENTIAL` | تدوير بيانات اعتماد حساب الخدمة |
| السياسة | `POL-SVC-ROTATE-CREDENTIAL` | Administrator؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-SVC-CREDENTIAL-ROTATED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-SERVICE-ACCOUNT` | حساب الخدمة |
| الجدول | `foundation.service_accounts` | الجدول الرئيسي لحساب الخدمة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-SERVICE-ACCOUNT-SM، TST-SLC01-INVARIANTS | دورة حالات حساب الخدمة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-SVC-ROTATE-CREDENTIAL -->

</details>

### 5.6 US-DOM-SVC-LIST — عرض حسابات الخدمة وحالة بيانات اعتمادها

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

<!-- BEGIN GENERATED: refs US-DOM-SVC-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| الشاشة | SCR-65 | شاشة المحوّلات والاتصالات والحساسات |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
<!-- END GENERATED: refs US-DOM-SVC-LIST -->

</details>

### 5.7 US-UI-SCR62-SERVICE-ACCOUNTS — إدارة حسابات الخدمة وتجديد بيانات اعتمادها

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

<!-- BEGIN GENERATED: refs US-UI-SCR62-SERVICE-ACCOUNTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| الشاشة | SCR-65 | شاشة المحوّلات والاتصالات والحساسات |
| المصدر | `17-security-design.md §2` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR62-SERVICE-ACCOUNTS -->

</details>

### 5.8 US-INT-SVC-KEY-AUTHENTICATION — مصادقة الأنظمة المتكاملة بمفتاح حساب الخدمة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-SVC-KEY-AUTHENTICATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §2` | — |
| المصدر | `20-integration-design.md §1` | — |
<!-- END GENERATED: refs US-INT-SVC-KEY-AUTHENTICATION -->

</details>

### 5.9 US-OPS-SVC-CREDENTIAL-EXPIRY — تنبيه قبل انتهاء بيانات اعتماد حساب الخدمة

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

<!-- BEGIN GENERATED: refs US-OPS-SVC-CREDENTIAL-EXPIRY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §2` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-SVC-CREDENTIAL-EXPIRY -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. | `US-BC01-SVC-CLOSE`، `US-BC01-SVC-CREATE`، `US-BC01-SVC-DISABLE`، `US-BC01-SVC-ENABLE`، `US-BC01-SVC-ROTATE-CREDENTIAL`، `US-DOM-SVC-LIST` | TST-PERSON-SM، TST-SERVICE-ACCOUNT-SM، TST-USER-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
