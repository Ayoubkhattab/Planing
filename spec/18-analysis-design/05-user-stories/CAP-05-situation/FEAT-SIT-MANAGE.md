---
id: FEAT-SIT-MANAGE
type: feature
title: "إنشاء المواقف وإدارتها"
status: DRAFT
version: "0.1"
capability: CAP-05.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إنشاء المواقف وإدارتها

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-SIT-MANAGE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-05 الوعي بالموقف |
| القدرة الفرعية | CAP-05.01 تعريف الموقف (R1) |
| الأدوار | المحلل؛ المدير؛ مسؤول الأمن؛ أي مستخدم مخوَّل |
| الشاشات | SCR-10 قائمة المواقف، SCR-12 إدارة الموقف وقواعد التنبيه |
| حالات الاستخدام | UC-020 |
| القصص | 12: 9 من المواصفة، و3 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يحدد المدير أو المحلل الموقف بمنطقته وفترته ومعاييره ويتحكم في تفعيله وإيقافه وإغلاقه.

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
| `US-BC03-SIT-ACTIVATE` | تفعيل الموقف | أمر | مسودة |
| `US-BC03-SIT-CLOSE` | إغلاق الموقف | أمر | مسودة |
| `US-BC03-SIT-CREATE` | إنشاء الموقف | أمر | مسودة |
| `US-BC03-SIT-EDIT-DEFINITION` | تعديل تعريف الموقف | أمر | مسودة |
| `US-BC03-SIT-PAUSE` | إيقاف الموقف مؤقتًا | أمر | مسودة |
| `US-BC03-SIT-RECLASSIFY` | إعادة تصنيف الموقف | أمر | مسودة |
| `US-BC03-SIT-RESUME` | استئناف الموقف | أمر | مسودة |
| `US-BC03-Q-SIT-GET` | جلب: Definition (version at valid_at), counts of visible members by type | جلب | مسودة |
| `US-BC03-Q-SIT-LIST` | جلب: Situations by state, owner, extent intersecting bbox | جلب | مسودة |
| `US-UI-SCR10-SITUATION-LIST` | تصفح المواقف بالحالة والمالك والمنطقة | واجهة | مسودة |
| `US-UI-SCR12-DEFINITION-EDITOR` | رسم منطقة الموقف وتحديد فترته ومعاييره | واجهة | مسودة |
| `US-UI-SCR12-SITUATION-ACTIONS` | إظهار أفعال الموقف المتاحة حسب حالته | واجهة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC03-SIT-ACTIVATE — تفعيل الموقف

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

<!-- BEGIN GENERATED: refs US-BC03-SIT-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/situations/{id}/actions/activate` | — |
| الأمر | `CMD-SIT-ACTIVATE` | تفعيل الموقف |
| السياسة | `POL-SIT-ACTIVATE` | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ tenant match; targe… |
| الحدث | `EVT-SIT-ACTIVATED` | يصل إلى: Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projectio… |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-SIT-ACTIVATE -->

</details>

### 5.2 US-BC03-SIT-CLOSE — إغلاق الموقف

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

<!-- BEGIN GENERATED: refs US-BC03-SIT-CLOSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/situations/{id}/actions/close` | — |
| الأمر | `CMD-SIT-CLOSE` | إغلاق الموقف |
| السياسة | `POL-SIT-CLOSE` | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ tenant match; targe… |
| الحدث | `EVT-SIT-CLOSED` | يصل إلى: Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projectio… |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-SIT-CLOSE -->

</details>

### 5.3 US-BC03-SIT-CREATE — إنشاء الموقف

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

<!-- BEGIN GENERATED: refs US-BC03-SIT-CREATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/situations` | — |
| الأمر | `CMD-SIT-CREATE` | إنشاء الموقف |
| السياسة | `POL-SIT-CREATE` | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ tenant match; targe… |
| الحدث | `EVT-SIT-CREATED` | يصل إلى: Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projectio… |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-SIT-CREATE -->

</details>

### 5.4 US-BC03-SIT-EDIT-DEFINITION — تعديل تعريف الموقف

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

<!-- BEGIN GENERATED: refs US-BC03-SIT-EDIT-DEFINITION -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/situations/{id}/actions/edit-definition` | — |
| الأمر | `CMD-SIT-EDIT-DEFINITION` | تعديل تعريف الموقف |
| السياسة | `POL-SIT-EDIT-DEFINITION` | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ tenant match; targe… |
| الحدث | `EVT-SIT-DEFINITION-CHANGED` | يصل إلى: Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projectio… |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-SIT-EDIT-DEFINITION -->

</details>

### 5.5 US-BC03-SIT-PAUSE — إيقاف الموقف مؤقتًا

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

<!-- BEGIN GENERATED: refs US-BC03-SIT-PAUSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/situations/{id}/actions/pause` | — |
| الأمر | `CMD-SIT-PAUSE` | إيقاف الموقف مؤقتًا |
| السياسة | `POL-SIT-PAUSE` | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ tenant match; targe… |
| الحدث | `EVT-SIT-PAUSED` | يصل إلى: Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projectio… |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-SIT-PAUSE -->

</details>

### 5.6 US-BC03-SIT-RECLASSIFY — إعادة تصنيف الموقف

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

<!-- BEGIN GENERATED: refs US-BC03-SIT-RECLASSIFY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/situations/{id}/actions/reclassify` | — |
| الأمر | `CMD-SIT-RECLASSIFY` | إعادة تصنيف الموقف |
| السياسة | `POL-SIT-RECLASSIFY` | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ tenant match; targe… |
| الحدث | `EVT-SIT-RECLASSIFIED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-SIT-RECLASSIFY -->

</details>

### 5.7 US-BC03-SIT-RESUME — استئناف الموقف

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

<!-- BEGIN GENERATED: refs US-BC03-SIT-RESUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/intelligence/situations/{id}/actions/resume` | — |
| الأمر | `CMD-SIT-RESUME` | استئناف الموقف |
| السياسة | `POL-SIT-RESUME` | Analyst / Manager (resume)؛ tenant match; target visible to subject |
| الحدث | `EVT-SIT-RESUMED` | يصل إلى: Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projectio… |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-SIT-RESUME -->

</details>

### 5.8 US-BC03-Q-SIT-GET — جلب: Definition (version at valid_at), counts of visible members by type

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

<!-- BEGIN GENERATED: refs US-BC03-Q-SIT-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/situations/{situation_id}` | — |
| الاستعلام | `QRY-SIT-GET` | Definition (version at valid_at), counts of visible members by type |
| السياسة | `POL-SIT-GET` | cleared for situation label |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-Q-SIT-GET -->

</details>

### 5.9 US-BC03-Q-SIT-LIST — جلب: Situations by state, owner, extent intersecting bbox

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

<!-- BEGIN GENERATED: refs US-BC03-Q-SIT-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/intelligence/situations` | — |
| الاستعلام | `QRY-SIT-LIST` | Situations by state, owner, extent intersecting bbox |
| السياسة | `POL-SIT-LIST` | any user; situation label rule |
| الكيان | `AGG-SITUATION` | الموقف |
| الجدول | `intelligence.situations` | الجدول الرئيسي للموقف |
| وحدة النشر | DU-06 | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
| الاختبار | TST-SITUATION-SM، TST-SLC06-INVARIANTS | دورة حالات الموقف، وثوابت الشريحة SLC-06 |
<!-- END GENERATED: refs US-BC03-Q-SIT-LIST -->

</details>

### 5.10 US-UI-SCR10-SITUATION-LIST — تصفح المواقف بالحالة والمالك والمنطقة

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

<!-- BEGIN GENERATED: refs US-UI-SCR10-SITUATION-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-10 | شاشة قائمة المواقف |
| حالة الاستخدام | UC-020 | Create Situation |
<!-- END GENERATED: refs US-UI-SCR10-SITUATION-LIST -->

</details>

### 5.11 US-UI-SCR12-DEFINITION-EDITOR — رسم منطقة الموقف وتحديد فترته ومعاييره

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

<!-- BEGIN GENERATED: refs US-UI-SCR12-DEFINITION-EDITOR -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-12 | شاشة إدارة الموقف وقواعد التنبيه |
| المصدر | `situation-alerting-spec.md §2` | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
<!-- END GENERATED: refs US-UI-SCR12-DEFINITION-EDITOR -->

</details>

### 5.12 US-UI-SCR12-SITUATION-ACTIONS — إظهار أفعال الموقف المتاحة حسب حالته

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

<!-- BEGIN GENERATED: refs US-UI-SCR12-SITUATION-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-12 | شاشة إدارة الموقف وقواعد التنبيه |
| المصدر | `21-ui-design.md §6.3` | — |
| المتطلب | REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… |
| حالة الاستخدام | UC-020 | Create Situation |
<!-- END GENERATED: refs US-UI-SCR12-SITUATION-ACTIONS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and class… | `US-BC03-Q-SIT-GET`، `US-BC03-Q-SIT-LIST`، `US-BC03-SIT-ACTIVATE`، `US-BC03-SIT-CLOSE`، `US-BC03-SIT-CREATE`، `US-BC03-SIT-EDIT-DEFINITION`، `US-BC03-SIT-PAUSE`، `US-BC03-SIT-RECLASSIFY`، `US-BC03-SIT-RESUME`، `US-UI-SCR12-DEFINITION-EDITOR`، `US-UI-SCR12-SITUATION-ACTIONS` | TST-SITUATION-SM، TST-SLC06-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
