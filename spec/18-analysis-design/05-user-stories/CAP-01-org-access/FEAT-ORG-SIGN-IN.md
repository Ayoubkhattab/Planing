---
id: FEAT-ORG-SIGN-IN
type: feature
title: "الدخول الموحد وربط الهويات"
status: DRAFT
version: "0.1"
capability: CAP-01.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# الدخول الموحد وربط الهويات

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-SIGN-IN |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.02 الهوية والمصادقة والاتحاد (R1) |
| الأدوار | أي مستخدم مخوَّل؛ مسؤول الإدارة؛ النظام |
| الشاشات | SCR-62 المستخدمون والأدوار والسلطة |
| حالات الاستخدام | UC-084 |
| القصص | 11: 3 من المواصفة، و8 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمستخدم الدخول بحسابه المؤسسي عبر مزود الهوية الخارجي دون كلمة مرور خاصة بالمنصة، ويتيح للمسؤول ربط الهويات الخارجية بالحساب.

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
| `US-BC01-USR-LINK-IDENTITY` | ربط هوية خارجية بـحساب المستخدم | أمر | مسودة |
| `US-BC01-USR-RECORD-FIRST-SIGN-IN` | تسجيل أول دخول لـحساب المستخدم | أمر | مسودة |
| `US-BC01-USR-UNLINK-IDENTITY` | فك ربط هوية خارجية عن حساب المستخدم | أمر | مسودة |
| `US-PLT-SIGNIN-MFA-STEPUP` | المصادقة المعززة دون فقد المدخلات | منصة | مسودة |
| `US-PLT-SIGNIN-SESSION-LIFETIME` | إنهاء الجلسة بعد مدتها وتجديد الرمز | منصة | مسودة |
| `US-INT-IDP-OIDC-FEDERATION` | الدخول عبر مزود هوية المستأجر بـOIDC | تكامل | مسودة |
| `US-INT-IDP-SAML-FEDERATION` | الدخول عبر مزود هوية المستأجر بـSAML | تكامل | مسودة |
| `US-OPS-IDP-HIGH-AVAILABILITY` | توفر وسيط الهوية دون انقطاع | تشغيل | مسودة |
| `US-OPS-IDP-OUTAGE-BREAKGLASS` | تشغيل المنصة عند انقطاع مزود الهوية | تشغيل | مسودة |
| `US-OPS-IDP-TENANT-SETUP` | ربط مزود هوية المستأجر بوسيط الخلية | تشغيل | مسودة |
| `US-OPS-SIGNIN-BRUTE-FORCE` | كشف محاولات الدخول الفاشلة المتكررة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-USR-LINK-IDENTITY — ربط هوية خارجية بـحساب المستخدم

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

<!-- BEGIN GENERATED: refs US-BC01-USR-LINK-IDENTITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/users/{id}/actions/link-identity` | — |
| الأمر | `CMD-USR-LINK-IDENTITY` | ربط هوية خارجية بـحساب المستخدم |
| السياسة | `POL-USR-LINK-IDENTITY` | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer… |
| الحدث | `EVT-USR-IDENTITY-LINKED` | يصل إلى: Search/Directory projection (BC01 read model) |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-005، REQ-FND-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-USR-LINK-IDENTITY -->

</details>

### 5.2 US-BC01-USR-RECORD-FIRST-SIGN-IN — تسجيل أول دخول لـحساب المستخدم

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

<!-- BEGIN GENERATED: refs US-BC01-USR-RECORD-FIRST-SIGN-IN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/users/{id}/actions/record-first-sign-in` | — |
| الأمر | `CMD-USR-RECORD-FIRST-SIGN-IN` | تسجيل أول دخول لـحساب المستخدم |
| السياسة | `POL-USR-RECORD-FIRST-SIGN-IN` | workload identity: scheduler / provisioning saga؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN ope… |
| الحدث | `EVT-USR-ACTIVATED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-005، REQ-FND-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-USR-RECORD-FIRST-SIGN-IN -->

</details>

### 5.3 US-BC01-USR-UNLINK-IDENTITY — فك ربط هوية خارجية عن حساب المستخدم

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

<!-- BEGIN GENERATED: refs US-BC01-USR-UNLINK-IDENTITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/users/{id}/actions/unlink-identity` | — |
| الأمر | `CMD-USR-UNLINK-IDENTITY` | فك ربط هوية خارجية عن حساب المستخدم |
| السياسة | `POL-USR-UNLINK-IDENTITY` | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer… |
| الحدث | `EVT-USR-IDENTITY-UNLINKED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-USER` | حساب المستخدم |
| الجدول | `foundation.users` | الجدول الرئيسي لحساب المستخدم |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-005، REQ-FND-006 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
| الاختبار | TST-USER-SM، TST-SLC01-INVARIANTS | دورة حالات حساب المستخدم، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-USR-UNLINK-IDENTITY -->

</details>

### 5.4 US-PLT-SIGNIN-MFA-STEPUP — المصادقة المعززة دون فقد المدخلات

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-SIGNIN-MFA-STEPUP -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P19 | Handling of Authorization Outcomes (403 vs 404, MFA step-up, approval-required) |
| المصدر | `17-security-design.md §12.3` | — |
| المصدر | `21-ui-design.md §6.2` | — |
<!-- END GENERATED: refs US-PLT-SIGNIN-MFA-STEPUP -->

</details>

### 5.5 US-PLT-SIGNIN-SESSION-LIFETIME — إنهاء الجلسة بعد مدتها وتجديد الرمز

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-SIGNIN-SESSION-LIFETIME -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §10` | — |
| المصدر | `12-solution/ui-architecture.md` | — |
| المصدر | `21-ui-design.md §6.2` | — |
<!-- END GENERATED: refs US-PLT-SIGNIN-SESSION-LIFETIME -->

</details>

### 5.6 US-INT-IDP-OIDC-FEDERATION — الدخول عبر مزود هوية المستأجر بـOIDC

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

<!-- BEGIN GENERATED: refs US-INT-IDP-OIDC-FEDERATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-09 | Keycloak per cell as OIDC/SAML federation broker to tenant IdPs; SCIM via provisioning service in BC01 |
| المصدر | `20-integration-design.md §4` | — |
| المتطلب | REQ-FND-005 | The system shall authenticate human users only through a configured external identity provider using OIDC or… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
<!-- END GENERATED: refs US-INT-IDP-OIDC-FEDERATION -->

</details>

### 5.7 US-INT-IDP-SAML-FEDERATION — الدخول عبر مزود هوية المستأجر بـSAML

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

<!-- BEGIN GENERATED: refs US-INT-IDP-SAML-FEDERATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-09 | Keycloak per cell as OIDC/SAML federation broker to tenant IdPs; SCIM via provisioning service in BC01 |
| المصدر | `20-integration-design.md §4` | — |
| المتطلب | REQ-FND-005 | The system shall authenticate human users only through a configured external identity provider using OIDC or… |
| حالة الاستخدام | UC-084 | Manage User Access & Federation |
<!-- END GENERATED: refs US-INT-IDP-SAML-FEDERATION -->

</details>

### 5.8 US-OPS-IDP-HIGH-AVAILABILITY — توفر وسيط الهوية دون انقطاع

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

<!-- BEGIN GENERATED: refs US-OPS-IDP-HIGH-AVAILABILITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §5` | — |
| القرار التقني | TD-09 | Keycloak per cell as OIDC/SAML federation broker to tenant IdPs; SCIM via provisioning service in BC01 |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-IDP-HIGH-AVAILABILITY -->

</details>

### 5.9 US-OPS-IDP-OUTAGE-BREAKGLASS — تشغيل المنصة عند انقطاع مزود الهوية

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

<!-- BEGIN GENERATED: refs US-OPS-IDP-OUTAGE-BREAKGLASS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §10` | — |
| المصدر | `09-reliability/dr-and-continuity.md §4` | — |
| المصدر | `09-reliability/degradation-slc01.md §matrix` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-IDP-OUTAGE-BREAKGLASS -->

</details>

### 5.10 US-OPS-IDP-TENANT-SETUP — ربط مزود هوية المستأجر بوسيط الخلية

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

<!-- BEGIN GENERATED: refs US-OPS-IDP-TENANT-SETUP -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-09 | Keycloak per cell as OIDC/SAML federation broker to tenant IdPs; SCIM via provisioning service in BC01 |
| المصدر | `17-security-design.md §2` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-IDP-TENANT-SETUP -->

</details>

### 5.11 US-OPS-SIGNIN-BRUTE-FORCE — كشف محاولات الدخول الفاشلة المتكررة

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

<!-- BEGIN GENERATED: refs US-OPS-SIGNIN-BRUTE-FORCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/observability-slc01.md §signals` | — |
| المصدر | `17-security-design.md §2` | — |
<!-- END GENERATED: refs US-OPS-SIGNIN-BRUTE-FORCE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-005 | The system shall authenticate human users only through a configured external identity provider using OIDC or… | `US-BC01-USR-LINK-IDENTITY`، `US-BC01-USR-RECORD-FIRST-SIGN-IN`، `US-BC01-USR-UNLINK-IDENTITY`، `US-INT-IDP-OIDC-FEDERATION`، `US-INT-IDP-SAML-FEDERATION` | TST-USER-SM |
| REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. | كل قصص الميزة المأخوذة من المواصفة (3) | TST-PERSON-SM، TST-SERVICE-ACCOUNT-SM، TST-USER-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
