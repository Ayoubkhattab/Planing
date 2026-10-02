---
id: FEAT-ORG-DELEGATION
type: feature
title: "تفويض السلطة والتحقق منها"
status: DRAFT
version: "0.1"
capability: CAP-01.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تفويض السلطة والتحقق منها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-DELEGATION |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.03 السلطة والتفويض (R1) |
| الأدوار | صاحب السلطة أو المعتمِد الثاني؛ المفوَّض إليه؛ النظام |
| الشاشات | SCR-62 المستخدمون والأدوار والسلطة، SCR-05 طلبات قرار تنتظرني |
| حالات الاستخدام | UC-083، UC-032، UC-035 |
| القصص | 4: 2 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لصاحب السلطة تفويض جزء من سلطته لغيره لمدة محددة دون تجاوز حدوده، ويتيح للمنصة التأكد قبل أي قرار أن صاحبه مخوّل به.

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
| `US-BC01-AUT-DELEGATE` | تفويض منح السلطة | أمر | مسودة |
| `US-BC01-Q-AUT-CHECK` | جلب: AuthorityCheck(actor, decision_type, scope, at, amount?) | جلب | مسودة |
| `US-UI-SCR05-ACTING-AUTHORITY` | إظهار سلطة المفوَّض إليه عند القرار | واجهة | مسودة |
| `US-UI-SCR62-DELEGATION-FORM` | تفويض السلطة ضمن حدود المفوِّض الظاهرة | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-AUT-DELEGATE — تفويض منح السلطة

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

<!-- BEGIN GENERATED: refs US-BC01-AUT-DELEGATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/authority-grants/{id}/actions/delegate` | — |
| الأمر | `CMD-AUT-DELEGATE` | تفويض منح السلطة |
| السياسة | `POL-AUT-DELEGATE` | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delega… |
| الحدث | `EVT-AUT-DELEGATED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-AUTHORITY-GRANT` | منح السلطة |
| الجدول | `foundation.authority_grants` | الجدول الرئيسي لمنح السلطة |
| وحدة النشر | DU-02 | — |
| المتطلبات | REQ-FND-007، REQ-FND-008، REQ-FND-009 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-032، UC-035، UC-083 | Record Decision؛ Approve Plan؛ Delegate Authority |
| الاختبار | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS | دورة حالات منح السلطة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-AUT-DELEGATE -->

</details>

### 5.2 US-BC01-Q-AUT-CHECK — جلب: AuthorityCheck(actor, decision_type, scope, at, amount?)

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

<!-- BEGIN GENERATED: refs US-BC01-Q-AUT-CHECK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/foundation/authority-checks` | — |
| الاستعلام | `QRY-AUT-CHECK` | AuthorityCheck(actor, decision_type, scope, at, amount?) |
| السياسة | `POL-AUT-CHECK` | org scope of subject roles ∩ classification rule |
| الكيان | `AGG-AUTHORITY-GRANT` | منح السلطة |
| الجدول | `foundation.authority_grants` | الجدول الرئيسي لمنح السلطة |
| وحدة النشر | DU-02 | — |
| المتطلب | REQ-FND-009 | The system shall provide an authority check returning whether an actor holds authority for a given decision t… |
| حالات الاستخدام | UC-032، UC-035 | Record Decision؛ Approve Plan |
| الاختبار | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS | دورة حالات منح السلطة، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC01-Q-AUT-CHECK -->

</details>

### 5.3 US-UI-SCR05-ACTING-AUTHORITY — إظهار سلطة المفوَّض إليه عند القرار

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

<!-- BEGIN GENERATED: refs US-UI-SCR05-ACTING-AUTHORITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-083 | Delegate Authority |
| الشاشة | SCR-05 | شاشة طلبات قرار تنتظرني |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-009 | The system shall provide an authority check returning whether an actor holds authority for a given decision t… |
| حالات الاستخدام | UC-032، UC-035 | Record Decision؛ Approve Plan |
<!-- END GENERATED: refs US-UI-SCR05-ACTING-AUTHORITY -->

</details>

### 5.4 US-UI-SCR62-DELEGATION-FORM — تفويض السلطة ضمن حدود المفوِّض الظاهرة

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

<!-- BEGIN GENERATED: refs US-UI-SCR62-DELEGATION-FORM -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-083 | Delegate Authority |
| الشاشة | SCR-62 | شاشة المستخدمون والأدوار والسلطة |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-FND-008 | When an authority holder delegates authority, the system shall record delegator, delegate, scope, limits and… |
| حالة الاستخدام | UC-083 | Delegate Authority |
<!-- END GENERATED: refs US-UI-SCR62-DELEGATION-FORM -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-007 | The system shall record authority as a grant stating decision type, organizational scope, limits and validity… | `US-BC01-AUT-DELEGATE` | TST-AUTHORITY-GRANT-SM |
| REQ-FND-008 | When an authority holder delegates authority, the system shall record delegator, delegate, scope, limits and… | `US-BC01-AUT-DELEGATE`، `US-UI-SCR62-DELEGATION-FORM` | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS |
| REQ-FND-009 | The system shall provide an authority check returning whether an actor holds authority for a given decision t… | `US-BC01-AUT-DELEGATE`، `US-BC01-Q-AUT-CHECK`، `US-UI-SCR05-ACTING-AUTHORITY` | TST-AUTHORITY-GRANT-SM، TST-SLC01-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
