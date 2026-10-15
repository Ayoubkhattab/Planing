---
id: FEAT-GOV-DATA-RESIDENCY
type: feature
title: "إقامة البيانات وسيادتها"
status: DRAFT
version: "0.1"
capability: CAP-13.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إقامة البيانات وسيادتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-GOV-DATA-RESIDENCY |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-13 الحوكمة والأمن والامتثال |
| القدرة الفرعية | CAP-13.04 السيادة وإقامة البيانات (R1) |
| الأدوار | مسؤول الأمن؛ مشغّل المنصة؛ النظام |
| الشاشات | SCR-60 المستأجر والحصص (واجهة المشغل) |
| حالات الاستخدام | — |
| القصص | 8: 0 من المواصفة، و8 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضمن بقاء جميع بيانات الجهة داخل نطاقها الجغرافي والقانوني المحدد وعدم نقلها خارجه إلا بسياسة صريحة من المستأجر.

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
| `US-UI-SCR60-RESIDENCY` | عرض ولاية المستأجر وخليته ونمطها | واجهة | مسودة |
| `US-PLT-RESIDENCY-EGRESS-DENY` | منع خروج البيانات خارج الولاية افتراضيًا | منصة | مسودة |
| `US-PLT-RESIDENCY-TRANSFER-POLICY` | السماح بالنقل الخارجي بسياسة صريحة فقط | منصة | مسودة |
| `US-OPS-KEYS-ROTATION` | تدوير المفاتيح دوريًا وعند الاشتباه | تشغيل | مسودة |
| `US-OPS-KEYS-TENANT-HIERARCHY` | مفاتيح تشفير خاصة بكل مستأجر | تشغيل | مسودة |
| `US-OPS-RESIDENCY-DR-SITE` | بقاء النسخ وموقع التعافي داخل الولاية | تشغيل | مسودة |
| `US-OPS-RESIDENCY-EGRESS-ALERT` | مراقبة خروج الشبكة والتنبيه الفوري | تشغيل | مسودة |
| `US-OPS-SECRETS-STORE` | حفظ الأسرار خارج الكود والصور | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-UI-SCR60-RESIDENCY — عرض ولاية المستأجر وخليته ونمطها

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

<!-- BEGIN GENERATED: refs US-UI-SCR60-RESIDENCY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-60 | شاشة المستأجر والحصص (واجهة المشغل) |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-005 | The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data… |
<!-- END GENERATED: refs US-UI-SCR60-RESIDENCY -->

</details>

### 5.2 US-PLT-RESIDENCY-EGRESS-DENY — منع خروج البيانات خارج الولاية افتراضيًا

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

<!-- BEGIN GENERATED: refs US-PLT-RESIDENCY-EGRESS-DENY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §8` | — |
| المصدر | `22-deployment-design.md §9` | — |
| المتطلب | REQ-GOV-005 | The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data… |
<!-- END GENERATED: refs US-PLT-RESIDENCY-EGRESS-DENY -->

</details>

### 5.3 US-PLT-RESIDENCY-TRANSFER-POLICY — السماح بالنقل الخارجي بسياسة صريحة فقط

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

<!-- BEGIN GENERATED: refs US-PLT-RESIDENCY-TRANSFER-POLICY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-005 | The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data… |
<!-- END GENERATED: refs US-PLT-RESIDENCY-TRANSFER-POLICY -->

</details>

### 5.4 US-OPS-KEYS-ROTATION — تدوير المفاتيح دوريًا وعند الاشتباه

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

<!-- BEGIN GENERATED: refs US-OPS-KEYS-ROTATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §6.1` | — |
<!-- END GENERATED: refs US-OPS-KEYS-ROTATION -->

</details>

### 5.5 US-OPS-KEYS-TENANT-HIERARCHY — مفاتيح تشفير خاصة بكل مستأجر

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

<!-- BEGIN GENERATED: refs US-OPS-KEYS-TENANT-HIERARCHY -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-07 | OpenBao (MPL, open fork of Vault) Transit engine for envelope encryption; KEKs in site HSM via PKCS#11; DEKs… |
| المصدر | `17-security-design.md §6` | — |
<!-- END GENERATED: refs US-OPS-KEYS-TENANT-HIERARCHY -->

</details>

### 5.6 US-OPS-RESIDENCY-DR-SITE — بقاء النسخ وموقع التعافي داخل الولاية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-RESIDENCY-DR-SITE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §1.2` | — |
| المصدر | `22-deployment-design.md §5` | — |
| المتطلب | REQ-GOV-005 | The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data… |
<!-- END GENERATED: refs US-OPS-RESIDENCY-DR-SITE -->

</details>

### 5.7 US-OPS-RESIDENCY-EGRESS-ALERT — مراقبة خروج الشبكة والتنبيه الفوري

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-RESIDENCY-EGRESS-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §3` | — |
| المتطلب | REQ-GOV-005 | The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data… |
<!-- END GENERATED: refs US-OPS-RESIDENCY-EGRESS-ALERT -->

</details>

### 5.8 US-OPS-SECRETS-STORE — حفظ الأسرار خارج الكود والصور

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

<!-- BEGIN GENERATED: refs US-OPS-SECRETS-STORE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §8` | — |
| المصدر | `12-solution/release-configuration-migration.md §2` | — |
<!-- END GENERATED: refs US-OPS-SECRETS-STORE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-GOV-005 | The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data… | `US-OPS-RESIDENCY-DR-SITE`، `US-OPS-RESIDENCY-EGRESS-ALERT`، `US-PLT-RESIDENCY-EGRESS-DENY`، `US-PLT-RESIDENCY-TRANSFER-POLICY`، `US-UI-SCR60-RESIDENCY` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
