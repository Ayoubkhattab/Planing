---
id: FEAT-PLT-AIRGAP-UPGRADE
type: feature
title: "التثبيت والترقية دون اتصال"
status: DRAFT
version: "0.1"
capability: CAP-14.02
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# التثبيت والترقية دون اتصال

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-PLT-AIRGAP-UPGRADE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-14 تشغيل المنصة |
| القدرة الفرعية | CAP-14.02 الاعتمادية والتعافي (R1) |
| الأدوار | مشغّل المنصة |
| الشاشات | — |
| حالات الاستخدام | — |
| القصص | 10: 0 من المواصفة، و10 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح تثبيت المنصة وترقيتها وتشغيلها في بيئة معزولة عن الإنترنت مع بقاء الواجهات القديمة تعمل عند إصدار نسخ جديدة.

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
| QAS-EVO-001 | changes an API or event contract | previous major version supported ≥ 6 months after successor |
| QAS-OPS-001 | installs or upgrades in an air-gapped site | offline bundle only; rollback ≤ 1 h |
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
| `US-PLT-AIRGAP-NO-INTERNET` | لا اعتماد على الإنترنت في البناء والتشغيل | منصة | مسودة |
| `US-PLT-API-CURSOR-PAGINATION` | ترقيم القوائم بالمؤشر فقط | منصة | مسودة |
| `US-PLT-API-ERROR-MODEL` | نموذج خطأ موحد في كل الاستجابات | منصة | مسودة |
| `US-PLT-CONTRACT-VERSIONING` | تعايش الإصدار الرئيسي السابق ستة أشهر | منصة | مسودة |
| `US-OPS-CONFIG-GITOPS` | تغيير إعدادات المنصة بمراجعة شخصين | تشغيل | مسودة |
| `US-OPS-ENV-PROMOTION` | ترقية الحزمة نفسها بين البيئات | تشغيل | مسودة |
| `US-OPS-INSTALL-AIRGAPPED` | تثبيت المنصة في شبكة معزولة | تشغيل | مسودة |
| `US-OPS-RELEASE-BUNDLE` | بناء حزمة إصدار واحدة موقعة | تشغيل | مسودة |
| `US-OPS-RELEASE-VERIFY` | التحقق من توقيع الحزمة قبل التثبيت | تشغيل | مسودة |
| `US-OPS-UPGRADE-ROLLBACK` | ترقية دون توقف مع رجوع خلال ساعة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-PLT-AIRGAP-NO-INTERNET — لا اعتماد على الإنترنت في البناء والتشغيل

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

<!-- BEGIN GENERATED: refs US-PLT-AIRGAP-NO-INTERNET -->
| البند | المعرّف | المعنى |
|---|---|---|
| فحص البنية | FIT-12 | No external network dependency at runtime or build (air-gapped) |
| المتطلب | REQ-PLT-001 | The system shall install, upgrade and operate in an air-gapped environment with no dependency on external net… |
<!-- END GENERATED: refs US-PLT-AIRGAP-NO-INTERNET -->

</details>

### 5.2 US-PLT-API-CURSOR-PAGINATION — ترقيم القوائم بالمؤشر فقط

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

<!-- BEGIN GENERATED: refs US-PLT-API-CURSOR-PAGINATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| فحص البنية | FIT-13 | No list API with offset pagination |
| المتطلب | REQ-PLT-008 | The system shall use cursor-based pagination for every list API. |
<!-- END GENERATED: refs US-PLT-API-CURSOR-PAGINATION -->

</details>

### 5.3 US-PLT-API-ERROR-MODEL — نموذج خطأ موحد في كل الاستجابات

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

<!-- BEGIN GENERATED: refs US-PLT-API-ERROR-MODEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| المتطلب | REQ-PLT-009 | The system shall return errors in the standard error model with code, message, details, correlation id, retry… |
<!-- END GENERATED: refs US-PLT-API-ERROR-MODEL -->

</details>

### 5.4 US-PLT-CONTRACT-VERSIONING — تعايش الإصدار الرئيسي السابق ستة أشهر

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

<!-- BEGIN GENERATED: refs US-PLT-CONTRACT-VERSIONING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-EVO-001 | changes an API or event contract → previous major version supported ≥ 6 months after successor |
| فحص البنية | FIT-14 | No breaking contract change without new major version |
| المتطلب | REQ-PLT-007 | The system shall version every API and event contract and shall introduce breaking changes only as a new majo… |
<!-- END GENERATED: refs US-PLT-CONTRACT-VERSIONING -->

</details>

### 5.5 US-OPS-CONFIG-GITOPS — تغيير إعدادات المنصة بمراجعة شخصين

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

<!-- BEGIN GENERATED: refs US-OPS-CONFIG-GITOPS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §8` | — |
| القرار التقني | TD-17 | Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps… |
| المصدر | `12-solution/release-configuration-migration.md §2` | — |
<!-- END GENERATED: refs US-OPS-CONFIG-GITOPS -->

</details>

### 5.6 US-OPS-ENV-PROMOTION — ترقية الحزمة نفسها بين البيئات

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

<!-- BEGIN GENERATED: refs US-OPS-ENV-PROMOTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §8` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-ENV-PROMOTION -->

</details>

### 5.7 US-OPS-INSTALL-AIRGAPPED — تثبيت المنصة في شبكة معزولة

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

<!-- BEGIN GENERATED: refs US-OPS-INSTALL-AIRGAPPED -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-OPS-001 | installs or upgrades in an air-gapped site → offline bundle only; rollback ≤ 1 h |
| المتطلب | REQ-PLT-001 | The system shall install, upgrade and operate in an air-gapped environment with no dependency on external net… |
<!-- END GENERATED: refs US-OPS-INSTALL-AIRGAPPED -->

</details>

### 5.8 US-OPS-RELEASE-BUNDLE — بناء حزمة إصدار واحدة موقعة

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

<!-- BEGIN GENERATED: refs US-OPS-RELEASE-BUNDLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P18 | Repository and Module Structure (single repository, context packages composed into deployment units) |
| القرار التقني | TD-17 | Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps… |
| المصدر | `22-deployment-design.md §7` | — |
<!-- END GENERATED: refs US-OPS-RELEASE-BUNDLE -->

</details>

### 5.9 US-OPS-RELEASE-VERIFY — التحقق من توقيع الحزمة قبل التثبيت

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

<!-- BEGIN GENERATED: refs US-OPS-RELEASE-VERIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-12 | Kubernetes Jobs with Kueue (fair sharing, per-tenant quotas); images from internal Harbor registry, signed (c… |
| القرار التقني | TD-17 | Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps… |
| المصدر | `22-deployment-design.md §7` | — |
<!-- END GENERATED: refs US-OPS-RELEASE-VERIFY -->

</details>

### 5.10 US-OPS-UPGRADE-ROLLBACK — ترقية دون توقف مع رجوع خلال ساعة

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

<!-- BEGIN GENERATED: refs US-OPS-UPGRADE-ROLLBACK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-OPS-001 | installs or upgrades in an air-gapped site → offline bundle only; rollback ≤ 1 h |
| القرار التقني | TD-17 | Signed images (cosign) + SBOM (Syft); offline bundles with Zarf (air-gapped install/upgrade/rollback); GitOps… |
| المصدر | `12-solution/release-configuration-migration.md §1` | — |
<!-- END GENERATED: refs US-OPS-UPGRADE-ROLLBACK -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-PLT-001 | The system shall install, upgrade and operate in an air-gapped environment with no dependency on external net… | `US-OPS-INSTALL-AIRGAPPED`، `US-PLT-AIRGAP-NO-INTERNET` | — |
| REQ-PLT-007 | The system shall version every API and event contract and shall introduce breaking changes only as a new majo… | `US-PLT-CONTRACT-VERSIONING` | — |
| REQ-PLT-008 | The system shall use cursor-based pagination for every list API. | `US-PLT-API-CURSOR-PAGINATION` | — |
| REQ-PLT-009 | The system shall return errors in the standard error model with code, message, details, correlation id, retry… | `US-PLT-API-ERROR-MODEL` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
