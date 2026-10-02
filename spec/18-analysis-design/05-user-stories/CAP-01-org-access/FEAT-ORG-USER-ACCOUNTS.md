---
id: FEAT-ORG-USER-ACCOUNTS
type: feature
title: "إدارة حسابات المستخدمين"
status: DRAFT
version: "0.1"
capability: CAP-01.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة حسابات المستخدمين

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-USER-ACCOUNTS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.02 الهوية والمصادقة والاتحاد (R1) |
| الأدوار | مسؤول الإدارة؛ مسؤول الأمن؛ النظام؛ أي مستخدم مخوَّل |
| الشاشات | SCR-62 المستخدمون والأدوار والسلطة |
| حالات الاستخدام | UC-084 |
| القصص | 14: 9 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمسؤول ومسؤول الأمن إنشاء حسابات المستخدمين وتعطيلها وقفلها وإغلاقها والبحث فيها، مع بقائها متزامنة مع مزود الهوية.

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
| QAS-SEC-008 | user disabled via SCIM | next request from any session denied; SCIM-to-effect ≤ 5 min (REQ-FND-005) |
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
| `US-BC01-USR-CLOSE` | إغلاق حساب المستخدم | أمر | مسودة |
| `US-BC01-USR-DISABLE` | تعطيل حساب المستخدم | أمر | مسودة |
| `US-BC01-USR-ENABLE` | تمكين حساب المستخدم | أمر | مسودة |
| `US-BC01-USR-LINK-PERSON` | ربط شخص بـحساب المستخدم | أمر | مسودة |
| `US-BC01-USR-LOCK` | قفل حساب المستخدم | أمر | مسودة |
| `US-BC01-USR-PROVISION` | تهيئة حساب المستخدم | أمر | مسودة |
| `US-BC01-USR-UNLOCK` | فتح قفل حساب المستخدم | أمر | مسودة |
| `US-BC01-Q-USR-GET` | جلب: User with identities (no secrets) | جلب | مسودة |
| `US-BC01-Q-USR-LIST` | جلب: Users filtered by state, unit, role | جلب | مسودة |
| `US-UI-SCR62-USER-ACTIONS` | أفعال الحساب المتاحة حسب الحالة والدور | واجهة | مسودة |
| `US-UI-SCR62-USER-LIST` | البحث في المستخدمين وتصفيتهم حسب الحالة | واجهة | مسودة |
| `US-INT-SCIM-DEPROVISIONING` | تعطيل الحساب من مزود الهوية خلال خمس دقائق | تكامل | مسودة |
| `US-INT-SCIM-PROVISIONING` | استقبال إنشاء الحسابات من مزود الهوية | تكامل | مسودة |
| `US-OPS-SCIM-SYNC-ALERT` | تنبيه عند تأخر مزامنة الحسابات | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-USR-CLOSE — إغلاق حساب المستخدم

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

<!-- BEGIN GENERATED: refs US-BC01-USR-CLOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/users/{id}/actions/close` | — |
| الأمر | `CMD-USR-CLOSE` | إغلاق حساب المستخدم |
| السياسة | `POL-USR-CLOSE` | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer… |
| الحدث | `EVT-USR-CLOSED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-005، REQ-FND-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-USR-CLOSE -->

</details>

### 5.2 US-BC01-USR-DISABLE — تعطيل حساب المستخدم

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

<!-- BEGIN GENERATED: refs US-BC01-USR-DISABLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/users/{id}/actions/disable` | — |
| الأمر | `CMD-USR-DISABLE` | تعطيل حساب المستخدم |
| السياسة | `POL-USR-DISABLE` | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer… |
| الحدث | `EVT-USR-DISABLED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-005، REQ-FND-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-USR-DISABLE -->

</details>

### 5.3 US-BC01-USR-ENABLE — تمكين حساب المستخدم

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

<!-- BEGIN GENERATED: refs US-BC01-USR-ENABLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/users/{id}/actions/enable` | — |
| الأمر | `CMD-USR-ENABLE` | تمكين حساب المستخدم |
| السياسة | `POL-USR-ENABLE` | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer… |
| الحدث | `EVT-USR-ENABLED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-005، REQ-FND-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-USR-ENABLE -->

</details>

### 5.4 US-BC01-USR-LINK-PERSON — ربط شخص بـحساب المستخدم

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

<!-- BEGIN GENERATED: refs US-BC01-USR-LINK-PERSON -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/users/{id}/actions/link-person` | — |
| الأمر | `CMD-USR-LINK-PERSON` | ربط شخص بـحساب المستخدم |
| السياسة | `POL-USR-LINK-PERSON` | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer… |
| الحدث | `EVT-USR-PERSON-LINKED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-005، REQ-FND-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-USR-LINK-PERSON -->

</details>

### 5.5 US-BC01-USR-LOCK — قفل حساب المستخدم

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

<!-- BEGIN GENERATED: refs US-BC01-USR-LOCK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/users/{id}/actions/lock` | — |
| الأمر | `CMD-USR-LOCK` | قفل حساب المستخدم |
| السياسة | `POL-USR-LOCK` | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer… |
| الحدث | `EVT-USR-LOCKED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-005، REQ-FND-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-USR-LOCK -->

</details>

### 5.6 US-BC01-USR-PROVISION — تهيئة حساب المستخدم

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

<!-- BEGIN GENERATED: refs US-BC01-USR-PROVISION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/users` | — |
| الأمر | `CMD-USR-PROVISION` | تهيئة حساب المستخدم |
| السياسة | `POL-USR-PROVISION` | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer… |
| الحدث | `EVT-USR-PROVISIONED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-005، REQ-FND-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-USR-PROVISION -->

</details>

### 5.7 US-BC01-USR-UNLOCK — فتح قفل حساب المستخدم

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

<!-- BEGIN GENERATED: refs US-BC01-USR-UNLOCK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/users/{id}/actions/unlock` | — |
| الأمر | `CMD-USR-UNLOCK` | فتح قفل حساب المستخدم |
| السياسة | `POL-USR-UNLOCK` | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer… |
| الحدث | `EVT-USR-UNLOCKED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-005، REQ-FND-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-USR-UNLOCK -->

</details>

### 5.8 US-BC01-Q-USR-GET — جلب: User with identities (no secrets)

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

<!-- BEGIN GENERATED: refs US-BC01-Q-USR-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/foundation/users/{user_id}` | — |
| الاستعلام | `QRY-USR-GET` | User with identities (no secrets) |
| السياسة | `POL-USR-GET` | org scope of subject roles ∩ classification rule |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-Q-USR-GET -->

</details>

### 5.9 US-BC01-Q-USR-LIST — جلب: Users filtered by state, unit, role

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

<!-- BEGIN GENERATED: refs US-BC01-Q-USR-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/foundation/users` | — |
| الاستعلام | `QRY-USR-LIST` | Users filtered by state, unit, role |
| السياسة | `POL-USR-LIST` | org scope of subject roles ∩ classification rule |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-Q-USR-LIST -->

</details>

### 5.10 US-UI-SCR62-USER-ACTIONS — أفعال الحساب المتاحة حسب الحالة والدور

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

<!-- BEGIN GENERATED: refs US-UI-SCR62-USER-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| المصدر | `21-ui-design.md §5` | — |
| المصدر | `21-ui-design.md §6.3` | — |
<!-- END GENERATED: refs US-UI-SCR62-USER-ACTIONS -->

</details>

### 5.11 US-UI-SCR62-USER-LIST — البحث في المستخدمين وتصفيتهم حسب الحالة

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

<!-- BEGIN GENERATED: refs US-UI-SCR62-USER-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| المصدر | `21-ui-design.md §6.1` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR62-USER-LIST -->

</details>

### 5.12 US-INT-SCIM-DEPROVISIONING — تعطيل الحساب من مزود الهوية خلال خمس دقائق

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-SCIM-DEPROVISIONING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-008 | user disabled via SCIM → next request from any session denied; SCIM-to-effect ≤ 5 min (REQ-FND-005) |
| المتطلب | REQ-FND-005 | The system shall authenticate human users only through a configured external identity provider using OIDC or… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
<!-- END GENERATED: refs US-INT-SCIM-DEPROVISIONING -->

</details>

### 5.13 US-INT-SCIM-PROVISIONING — استقبال إنشاء الحسابات من مزود الهوية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-SCIM-PROVISIONING -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §4` | — |
| المصدر | `17-security-design.md §2` | — |
| المتطلب | REQ-FND-005 | The system shall authenticate human users only through a configured external identity provider using OIDC or… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
<!-- END GENERATED: refs US-INT-SCIM-PROVISIONING -->

</details>

### 5.14 US-OPS-SCIM-SYNC-ALERT — تنبيه عند تأخر مزامنة الحسابات

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

<!-- BEGIN GENERATED: refs US-OPS-SCIM-SYNC-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-008 | user disabled via SCIM → next request from any session denied; SCIM-to-effect ≤ 5 min (REQ-FND-005) |
| المصدر | `09-reliability/observability-slc01.md §signals` | — |
<!-- END GENERATED: refs US-OPS-SCIM-SYNC-ALERT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-005 | The system shall authenticate human users only through a configured external identity provider using OIDC or… | `US-BC01-USR-CLOSE`، `US-BC01-USR-DISABLE`، `US-BC01-USR-ENABLE`، `US-BC01-USR-LINK-PERSON`، `US-BC01-USR-LOCK`، `US-BC01-USR-PROVISION`، `US-BC01-USR-UNLOCK`، `US-INT-SCIM-DEPROVISIONING`، `US-INT-SCIM-PROVISIONING` | TST-USER-SM |
| REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. | كل قصص الميزة المأخوذة من المواصفة (9) | TST-PERSON-SM، TST-SERVICE-ACCOUNT-SM، TST-USER-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
