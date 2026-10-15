---
id: FEAT-GOV-CLASSIFICATION
type: feature
title: "مخطط التصنيف الأمني"
status: DRAFT
version: "0.1"
capability: CAP-13.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مخطط التصنيف الأمني

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-GOV-CLASSIFICATION |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-13 الحوكمة والأمن والامتثال |
| القدرة الفرعية | CAP-13.01 التصنيف والسياسات (R1) |
| الأدوار | مسؤول الأمن؛ أي مستخدم مخوَّل؛ النظام |
| الشاشات | SCR-67 التصنيف والتصاريح والاستثناءات |
| حالات الاستخدام | UC-085 |
| القصص | 11: 6 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لمسؤول الأمن تحديد مستويات السرية والحجرات وقيود الإفراج الخاصة بالمستأجر واعتمادها، ويعرضها لكل مستخدم.

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
| `US-BC08-CLS-ACTIVATE` | تفعيل مخطط التصنيف | أمر | مسودة |
| `US-BC08-CLS-DISCARD` | تجاهل مسودة مخطط التصنيف | أمر | مسودة |
| `US-BC08-CLS-DRAFT` | إعداد مسودة مخطط التصنيف | أمر | مسودة |
| `US-BC08-CLS-EDIT` | تعديل مخطط التصنيف | أمر | مسودة |
| `US-BC08-Q-CLS-ACTIVE` | جلب: Active scheme (labels only) | جلب | مسودة |
| `US-BC08-S-CLASSIFICATION-SCHEME-01` | تلقائي: successor activated (مخطط التصنيف) | نظام | مسودة |
| `US-UI-SCR67-SCHEME-EDITOR` | تحرير مستويات التصنيف وأقسامه وتحفظاته | واجهة | مسودة |
| `US-PLT-CLS-COMPOSITE-LABEL` | تصنيف الكائن المركب بأعلى مكوناته | منصة | مسودة |
| `US-PLT-CLS-LABEL-REQUIRED` | إلزام التصنيف عند إنشاء الكائنات المهمة | منصة | مسودة |
| `US-PLT-CLS-RECLASSIFY-PROPAGATION` | نفاذ تغيير التصنيف فورًا في كل المسارات | منصة | مسودة |
| `US-PLT-CLS-UI-BADGE` | شارة التصنيف على كل كائن ونموذج | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC08-CLS-ACTIVATE — تفعيل مخطط التصنيف

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

<!-- BEGIN GENERATED: refs US-BC08-CLS-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/classification-schemes/{id}/actions/activate` | — |
| الأمر | `CMD-CLS-ACTIVATE` | تفعيل مخطط التصنيف |
| السياسة | `POL-CLS-ACTIVATE` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-CLS-ACTIVATED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-CLASSIFICATION-SCHEME` | مخطط التصنيف |
| الجدول | `governance.classification_schemes` | الجدول الرئيسي لمخطط التصنيف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-001، REQ-GOV-004، REQ-GOV-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-085 | Manage Classification Scheme & Compartments |
| الاختبار | TST-CLASSIFICATION-SCHEME-SM، TST-SLC01-INVARIANTS | دورة حالات مخطط التصنيف، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-CLS-ACTIVATE -->

</details>

### 5.2 US-BC08-CLS-DISCARD — تجاهل مسودة مخطط التصنيف

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

<!-- BEGIN GENERATED: refs US-BC08-CLS-DISCARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/classification-schemes/{id}/actions/discard` | — |
| الأمر | `CMD-CLS-DISCARD` | تجاهل مسودة مخطط التصنيف |
| السياسة | `POL-CLS-DISCARD` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-CLS-DISCARDED` | يصل إلى: Search/Directory projection (BC01 read model); PDP bundle distributor |
| الكيان | `AGG-CLASSIFICATION-SCHEME` | مخطط التصنيف |
| الجدول | `governance.classification_schemes` | الجدول الرئيسي لمخطط التصنيف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-001، REQ-GOV-004، REQ-GOV-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-085 | Manage Classification Scheme & Compartments |
| الاختبار | TST-CLASSIFICATION-SCHEME-SM، TST-SLC01-INVARIANTS | دورة حالات مخطط التصنيف، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-CLS-DISCARD -->

</details>

### 5.3 US-BC08-CLS-DRAFT — إعداد مسودة مخطط التصنيف

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

<!-- BEGIN GENERATED: refs US-BC08-CLS-DRAFT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/classification-schemes` | — |
| الأمر | `CMD-CLS-DRAFT` | إعداد مسودة مخطط التصنيف |
| السياسة | `POL-CLS-DRAFT` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-CLS-DRAFTED` | يصل إلى: Search/Directory projection (BC01 read model); PDP bundle distributor |
| الكيان | `AGG-CLASSIFICATION-SCHEME` | مخطط التصنيف |
| الجدول | `governance.classification_schemes` | الجدول الرئيسي لمخطط التصنيف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-001، REQ-GOV-004، REQ-GOV-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-085 | Manage Classification Scheme & Compartments |
| الاختبار | TST-CLASSIFICATION-SCHEME-SM، TST-SLC01-INVARIANTS | دورة حالات مخطط التصنيف، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-CLS-DRAFT -->

</details>

### 5.4 US-BC08-CLS-EDIT — تعديل مخطط التصنيف

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

<!-- BEGIN GENERATED: refs US-BC08-CLS-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/classification-schemes/{id}/actions/edit` | — |
| الأمر | `CMD-CLS-EDIT` | تعديل مخطط التصنيف |
| السياسة | `POL-CLS-EDIT` | Security Officer؛ tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform) |
| الحدث | `EVT-CLS-EDITED` | يصل إلى: Search/Directory projection (BC01 read model); PDP bundle distributor |
| الكيان | `AGG-CLASSIFICATION-SCHEME` | مخطط التصنيف |
| الجدول | `governance.classification_schemes` | الجدول الرئيسي لمخطط التصنيف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-001، REQ-GOV-004، REQ-GOV-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-085 | Manage Classification Scheme & Compartments |
| الاختبار | TST-CLASSIFICATION-SCHEME-SM، TST-SLC01-INVARIANTS | دورة حالات مخطط التصنيف، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-CLS-EDIT -->

</details>

### 5.5 US-BC08-Q-CLS-ACTIVE — جلب: Active scheme (labels only)

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

<!-- BEGIN GENERATED: refs US-BC08-Q-CLS-ACTIVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/governance/classification-scheme` | — |
| الاستعلام | `QRY-CLS-ACTIVE` | Active scheme (labels only) |
| السياسة | `POL-CLS-ACTIVE` | org scope of subject roles ∩ classification rule |
| الكيان | `AGG-CLASSIFICATION-SCHEME` | مخطط التصنيف |
| الجدول | `governance.classification_schemes` | الجدول الرئيسي لمخطط التصنيف |
| وحدة النشر | DU-03 | — |
| المتطلب | REQ-GOV-001 | The system shall support a per-tenant classification scheme with ordered levels, an unlimited number of compa… |
| حالة الاستخدام | UC-085 | Manage Classification Scheme & Compartments |
| الاختبار | TST-CLASSIFICATION-SCHEME-SM، TST-SLC01-INVARIANTS | دورة حالات مخطط التصنيف، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-Q-CLS-ACTIVE -->

</details>

### 5.6 US-BC08-S-CLASSIFICATION-SCHEME-01 — تلقائي: successor activated (مخطط التصنيف)

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

<!-- BEGIN GENERATED: refs US-BC08-S-CLASSIFICATION-SCHEME-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:successor activated` | system |
| الانتقال | ACTIVE ← SUPERSEDED | — |
| الحدث | `EVT-CLS-SUPERSEDED` | يصل إلى: Search/Directory projection (BC01 read model); PDP bundle distributor |
| الكيان | `AGG-CLASSIFICATION-SCHEME` | مخطط التصنيف |
| الجدول | `governance.classification_schemes` | الجدول الرئيسي لمخطط التصنيف |
| وحدة النشر | DU-03 | — |
| المتطلبات | REQ-GOV-001، REQ-GOV-004، REQ-GOV-009 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-085 | Manage Classification Scheme & Compartments |
| الاختبار | TST-CLASSIFICATION-SCHEME-SM، TST-SLC01-INVARIANTS | دورة حالات مخطط التصنيف، وثوابت الشريحة SLC-01 |
<!-- END GENERATED: refs US-BC08-S-CLASSIFICATION-SCHEME-01 -->

</details>

### 5.7 US-UI-SCR67-SCHEME-EDITOR — تحرير مستويات التصنيف وأقسامه وتحفظاته

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

<!-- BEGIN GENERATED: refs US-UI-SCR67-SCHEME-EDITOR -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-085 | Manage Classification Scheme & Compartments |
| الشاشة | SCR-67 | شاشة التصنيف والتصاريح والاستثناءات |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-GOV-001 | The system shall support a per-tenant classification scheme with ordered levels, an unlimited number of compa… |
| حالة الاستخدام | UC-085 | Manage Classification Scheme & Compartments |
<!-- END GENERATED: refs US-UI-SCR67-SCHEME-EDITOR -->

</details>

### 5.8 US-PLT-CLS-COMPOSITE-LABEL — تصنيف الكائن المركب بأعلى مكوناته

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

<!-- BEGIN GENERATED: refs US-PLT-CLS-COMPOSITE-LABEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §4` | — |
| المتطلب | REQ-GOV-004 | When the classification of an object is changed, the system shall require the authority defined by tenant pol… |
| حالة الاستخدام | UC-085 | Manage Classification Scheme & Compartments |
<!-- END GENERATED: refs US-PLT-CLS-COMPOSITE-LABEL -->

</details>

### 5.9 US-PLT-CLS-LABEL-REQUIRED — إلزام التصنيف عند إنشاء الكائنات المهمة

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

<!-- BEGIN GENERATED: refs US-PLT-CLS-LABEL-REQUIRED -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §4` | — |
| المصدر | `17-security-design.md §10` | — |
| المتطلب | REQ-GOV-002 | The system shall require a classification on every object of importance tier T1 or T2. |
<!-- END GENERATED: refs US-PLT-CLS-LABEL-REQUIRED -->

</details>

### 5.10 US-PLT-CLS-RECLASSIFY-PROPAGATION — نفاذ تغيير التصنيف فورًا في كل المسارات

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

<!-- BEGIN GENERATED: refs US-PLT-CLS-RECLASSIFY-PROPAGATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-003 | removes a user's compartment → effective on next request in every path, independent of index lag |
| المتطلب | REQ-GOV-004 | When the classification of an object is changed, the system shall require the authority defined by tenant pol… |
| حالة الاستخدام | UC-085 | Manage Classification Scheme & Compartments |
<!-- END GENERATED: refs US-PLT-CLS-RECLASSIFY-PROPAGATION -->

</details>

### 5.11 US-PLT-CLS-UI-BADGE — شارة التصنيف على كل كائن ونموذج

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

<!-- BEGIN GENERATED: refs US-PLT-CLS-UI-BADGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §11` | — |
| المتطلب | REQ-GOV-002 | The system shall require a classification on every object of importance tier T1 or T2. |
<!-- END GENERATED: refs US-PLT-CLS-UI-BADGE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-GOV-001 | The system shall support a per-tenant classification scheme with ordered levels, an unlimited number of compa… | `US-BC08-CLS-ACTIVATE`، `US-BC08-CLS-DISCARD`، `US-BC08-CLS-DRAFT`، `US-BC08-CLS-EDIT`، `US-BC08-Q-CLS-ACTIVE`، `US-BC08-S-CLASSIFICATION-SCHEME-01`، `US-UI-SCR67-SCHEME-EDITOR` | TST-CLASSIFICATION-SCHEME-SM |
| REQ-GOV-002 | The system shall require a classification on every object of importance tier T1 or T2. | `US-PLT-CLS-LABEL-REQUIRED`، `US-PLT-CLS-UI-BADGE` | — |
| REQ-GOV-004 | When the classification of an object is changed, the system shall require the authority defined by tenant pol… | `US-BC08-CLS-ACTIVATE`، `US-BC08-CLS-DISCARD`، `US-BC08-CLS-DRAFT`، `US-BC08-CLS-EDIT`، `US-BC08-S-CLASSIFICATION-SCHEME-01`، `US-PLT-CLS-COMPOSITE-LABEL`، `US-PLT-CLS-RECLASSIFY-PROPAGATION` | TST-CLASSIFICATION-SCHEME-SM، TST-CLEARANCE-SM، TST-SLC01-INVARIANTS، TST-SLC05-INVARIANTS |
| REQ-GOV-009 | The system shall version, audit and time-stamp every policy and configuration change and apply each change fr… | كل قصص الأوامر والنظام في الميزة (5) | TST-CLASSIFICATION-SCHEME-SM، TST-POLICY-SET-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
