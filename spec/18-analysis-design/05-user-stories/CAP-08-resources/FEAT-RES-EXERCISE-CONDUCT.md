---
id: FEAT-RES-EXERCISE-CONDUCT
type: feature
title: "إدارة تنفيذ التمرين"
status: DRAFT
version: "0.1"
capability: CAP-08.05
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# إدارة تنفيذ التمرين

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-RES-EXERCISE-CONDUCT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-08 الموارد والجاهزية |
| القدرة الفرعية | CAP-08.05 التدريب والتمارين (R3) |
| الأدوار | مراقب التمرين؛ النظام |
| الشاشات | SCR-48 التمارين والسيناريوهات والمحاكاة والجاهزية |
| حالات الاستخدام | UC-162 |
| القصص | 14: 10 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يدير مراقب التمرين سير التمرين الحي، فيرسل الأحداث ويوقف ويستأنف وينهي، وتُسجل النتيجة النهائية للتمرين تلقائيًا.

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
| QAS-TRX-001 | a simulation run nears completion (CMD-SIM-COMPLETE sent) with at least one exercise participant still unevaluated | 0 simulations reach COMPLETED with a participant lacking at least one recorded evaluation (INV-SIM-02) |
| QAS-TRX-002 | an inject delivered during a live simulation run | 'inject delivery recorded within target latency (tagged: recalibrate after Pilot R1 and R2 — RSK-028)' |
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
| `US-BC05-SIM-ABORT` | إيقاف تشغيل المحاكاة نهائيًا مع السبب | أمر | مسودة |
| `US-BC05-SIM-COMPLETE` | إكمال تشغيل المحاكاة | أمر | مسودة |
| `US-BC05-SIM-DELIVER-INJECT` | تسليم حقنة سيناريو ضمن تشغيل المحاكاة | أمر | مسودة |
| `US-BC05-SIM-PAUSE` | إيقاف تشغيل المحاكاة مؤقتًا | أمر | مسودة |
| `US-BC05-SIM-RESUME` | استئناف تشغيل المحاكاة | أمر | مسودة |
| `US-BC05-SIM-START` | بدء تشغيل المحاكاة | أمر | مسودة |
| `US-BC05-Q-SIM-GET` | جلب: Simulation with current state and evaluation summary | جلب | مسودة |
| `US-BC05-Q-SIM-LIST` | جلب: Simulations filtered by exercise, state, window | جلب | مسودة |
| `US-BC05-S-EXERCISE-01` | تلقائي: linked simulation completed (التمرين) | نظام | مسودة |
| `US-BC05-S-EXERCISE-02` | تلقائي: linked simulation aborted (التمرين) | نظام | مسودة |
| `US-UI-SCR48-COMPLETE-GUARD` | عرض المشاركين غير المقيَّمين قبل الإكمال | واجهة | مسودة |
| `US-UI-SCR48-CONTROL-CONSOLE` | لوحة مراقب التمرين لإدارة الأحداث الحية | واجهة | مسودة |
| `US-UI-SCR48-LIVE-TIMELINE` | خط زمني حي للأحداث والتقييمات | واجهة | مسودة |
| `US-PLT-SIM-INJECT-LATENCY` | تسجيل الحدث المرسل خلال الزمن المستهدف | منصة | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC05-SIM-ABORT — إيقاف تشغيل المحاكاة نهائيًا مع السبب

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SIM-ABORT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/simulations/{id}/actions/abort` | — |
| الأمر | `CMD-SIM-ABORT` | إيقاف تشغيل المحاكاة نهائيًا مع السبب |
| السياسة | `POL-SIM-ABORT` | Exercise Controller؛ tenant match |
| الحدث | `EVT-SIM-ABORTED` | يصل إلى: Exercise (ABORTED trigger); Search projection (SLC-05) |
| الكيان | `AGG-SIMULATION` | تشغيل المحاكاة |
| الجدول | `readiness.simulations` | الجدول الرئيسي لتشغيل المحاكاة |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-008، REQ-TRX-009، REQ-TRX-010، REQ-TRX-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
| الاختبار | TST-SIMULATION-SM، TST-SLC19-INVARIANTS | دورة حالات تشغيل المحاكاة، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-SIM-ABORT -->

</details>

### 5.2 US-BC05-SIM-COMPLETE — إكمال تشغيل المحاكاة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SIM-COMPLETE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/simulations/{id}/actions/complete` | — |
| الأمر | `CMD-SIM-COMPLETE` | إكمال تشغيل المحاكاة |
| السياسة | `POL-SIM-COMPLETE` | Exercise Controller؛ tenant match; every participant evaluated (INV-SIM-02) |
| الحدث | `EVT-SIM-COMPLETED` | يصل إلى: Exercise (COMPLETED trigger); Knowledge Object (optional AAR terminal source, SLC-12 — CR-63); Searc… |
| الكيان | `AGG-SIMULATION` | تشغيل المحاكاة |
| الجدول | `readiness.simulations` | الجدول الرئيسي لتشغيل المحاكاة |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-008، REQ-TRX-009، REQ-TRX-010، REQ-TRX-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
| الاختبار | TST-SIMULATION-SM، TST-SLC19-INVARIANTS | دورة حالات تشغيل المحاكاة، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-SIM-COMPLETE -->

</details>

### 5.3 US-BC05-SIM-DELIVER-INJECT — تسليم حقنة سيناريو ضمن تشغيل المحاكاة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SIM-DELIVER-INJECT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/simulations/{id}/actions/deliver-inject` | — |
| الأمر | `CMD-SIM-DELIVER-INJECT` | تسليم حقنة سيناريو ضمن تشغيل المحاكاة |
| السياسة | `POL-SIM-DELIVER-INJECT` | Exercise Controller؛ tenant match; inject_ref belongs to the linked scenario |
| الحدث | `EVT-SIM-INJECT-DELIVERED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-SIMULATION` | تشغيل المحاكاة |
| الجدول | `readiness.simulations` | الجدول الرئيسي لتشغيل المحاكاة |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-008، REQ-TRX-009، REQ-TRX-010، REQ-TRX-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
| الاختبار | TST-SIMULATION-SM، TST-SLC19-INVARIANTS | دورة حالات تشغيل المحاكاة، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-SIM-DELIVER-INJECT -->

</details>

### 5.4 US-BC05-SIM-PAUSE — إيقاف تشغيل المحاكاة مؤقتًا

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SIM-PAUSE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/simulations/{id}/actions/pause` | — |
| الأمر | `CMD-SIM-PAUSE` | إيقاف تشغيل المحاكاة مؤقتًا |
| السياسة | `POL-SIM-PAUSE` | Exercise Controller؛ tenant match |
| الحدث | `EVT-SIM-PAUSED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-SIMULATION` | تشغيل المحاكاة |
| الجدول | `readiness.simulations` | الجدول الرئيسي لتشغيل المحاكاة |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-008، REQ-TRX-009، REQ-TRX-010، REQ-TRX-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
| الاختبار | TST-SIMULATION-SM، TST-SLC19-INVARIANTS | دورة حالات تشغيل المحاكاة، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-SIM-PAUSE -->

</details>

### 5.5 US-BC05-SIM-RESUME — استئناف تشغيل المحاكاة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SIM-RESUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/simulations/{id}/actions/resume` | — |
| الأمر | `CMD-SIM-RESUME` | استئناف تشغيل المحاكاة |
| السياسة | `POL-SIM-RESUME` | Exercise Controller؛ tenant match |
| الحدث | `EVT-SIM-RESUMED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-SIMULATION` | تشغيل المحاكاة |
| الجدول | `readiness.simulations` | الجدول الرئيسي لتشغيل المحاكاة |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-008، REQ-TRX-009، REQ-TRX-010، REQ-TRX-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
| الاختبار | TST-SIMULATION-SM، TST-SLC19-INVARIANTS | دورة حالات تشغيل المحاكاة، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-SIM-RESUME -->

</details>

### 5.6 US-BC05-SIM-START — بدء تشغيل المحاكاة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-SIM-START -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/readiness/simulations` | — |
| الأمر | `CMD-SIM-START` | بدء تشغيل المحاكاة |
| السياسة | `POL-SIM-START` | system (workload identity)؛ tenant match; invoked only within CMD-EXR-START's unit of work |
| الحدث | `EVT-SIM-STARTED` | يصل إلى: Exercise (IN_PROGRESS trigger); Search projection (SLC-05) |
| الكيان | `AGG-SIMULATION` | تشغيل المحاكاة |
| الجدول | `readiness.simulations` | الجدول الرئيسي لتشغيل المحاكاة |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-008، REQ-TRX-009، REQ-TRX-010، REQ-TRX-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
| الاختبار | TST-SIMULATION-SM، TST-SLC19-INVARIANTS | دورة حالات تشغيل المحاكاة، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-SIM-START -->

</details>

### 5.7 US-BC05-Q-SIM-GET — جلب: Simulation with current state and evaluation summary

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-Q-SIM-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/simulations/{simulation_id}` | — |
| الاستعلام | `QRY-SIM-GET` | Simulation with current state and evaluation summary |
| السياسة | `POL-SIM-GET` | allowed_scope |
| الكيان | `AGG-SIMULATION` | تشغيل المحاكاة |
| الجدول | `readiness.simulations` | الجدول الرئيسي لتشغيل المحاكاة |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
| الاختبار | TST-SIMULATION-SM، TST-SLC19-INVARIANTS | دورة حالات تشغيل المحاكاة، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-Q-SIM-GET -->

</details>

### 5.8 US-BC05-Q-SIM-LIST — جلب: Simulations filtered by exercise, state, window

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-Q-SIM-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/readiness/simulations` | — |
| الاستعلام | `QRY-SIM-LIST` | Simulations filtered by exercise, state, window |
| السياسة | `POL-SIM-LIST` | allowed_scope |
| الكيان | `AGG-SIMULATION` | تشغيل المحاكاة |
| الجدول | `readiness.simulations` | الجدول الرئيسي لتشغيل المحاكاة |
| وحدة النشر | DU-14 | — |
| المتطلب | REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… |
| حالة الاستخدام | UC-161 | Plan & Schedule Exercise |
| الاختبار | TST-SIMULATION-SM، TST-SLC19-INVARIANTS | دورة حالات تشغيل المحاكاة، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-Q-SIM-LIST -->

</details>

### 5.9 US-BC05-S-EXERCISE-01 — تلقائي: linked simulation completed (التمرين)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-S-EXERCISE-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:linked simulation completed` | system; driven exclusively by the linked Simulation's own EVT-SIM-COMPLETED (INV-EXR-02) |
| الانتقال | IN_PROGRESS ← COMPLETED | — |
| الحدث | `EVT-EXR-COMPLETED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-EXERCISE` | التمرين |
| الجدول | `readiness.exercises` | الجدول الرئيسي للتمرين |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-003، REQ-TRX-004، REQ-TRX-005، REQ-TRX-006، REQ-TRX-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
| الاختبار | TST-EXERCISE-SM، TST-SLC19-INVARIANTS | دورة حالات التمرين، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-S-EXERCISE-01 -->

</details>

### 5.10 US-BC05-S-EXERCISE-02 — تلقائي: linked simulation aborted (التمرين)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC05-S-EXERCISE-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:linked simulation aborted` | system; driven exclusively by the linked Simulation's own EVT-SIM-ABORTED (INV-EXR-02) |
| الانتقال | IN_PROGRESS ← ABORTED | — |
| الحدث | `EVT-EXR-ABORTED` | يصل إلى: Search projection (SLC-05) |
| الكيان | `AGG-EXERCISE` | التمرين |
| الجدول | `readiness.exercises` | الجدول الرئيسي للتمرين |
| وحدة النشر | DU-14 | — |
| المتطلبات | REQ-TRX-003، REQ-TRX-004، REQ-TRX-005، REQ-TRX-006، REQ-TRX-007 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
| الاختبار | TST-EXERCISE-SM، TST-SLC19-INVARIANTS | دورة حالات التمرين، وثوابت الشريحة SLC-19 |
<!-- END GENERATED: refs US-BC05-S-EXERCISE-02 -->

</details>

### 5.11 US-UI-SCR48-COMPLETE-GUARD — عرض المشاركين غير المقيَّمين قبل الإكمال

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR48-COMPLETE-GUARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-48 | شاشة التمارين والسيناريوهات والمحاكاة والجاهزية |
| الجودة | QAS-TRX-001 | a simulation run nears completion (CMD-SIM-COMPLETE sent) with at least one exercise participant still uneval… |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-TRX-010 | A simulation run shall reach COMPLETED only when every participant listed on its linked exercise has at least… |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
<!-- END GENERATED: refs US-UI-SCR48-COMPLETE-GUARD -->

</details>

### 5.12 US-UI-SCR48-CONTROL-CONSOLE — لوحة مراقب التمرين لإدارة الأحداث الحية

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R3 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR48-CONTROL-CONSOLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-48 | شاشة التمارين والسيناريوهات والمحاكاة والجاهزية |
| المصدر | `[Derived]` | — |
| المتطلبات | REQ-TRX-008، REQ-TRX-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
<!-- END GENERATED: refs US-UI-SCR48-CONTROL-CONSOLE -->

</details>

### 5.13 US-UI-SCR48-LIVE-TIMELINE — خط زمني حي للأحداث والتقييمات

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R3 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR48-LIVE-TIMELINE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-48 | شاشة التمارين والسيناريوهات والمحاكاة والجاهزية |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-TRX-015 | The system shall provide the full, ordered timeline of inject deliveries and evaluations for a simulation run… |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
<!-- END GENERATED: refs US-UI-SCR48-LIVE-TIMELINE -->

</details>

### 5.14 US-PLT-SIM-INJECT-LATENCY — تسجيل الحدث المرسل خلال الزمن المستهدف

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R3 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-SIM-INJECT-LATENCY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-TRX-002 | an inject delivered during a live simulation run → 'inject delivery recorded within target latency (tagged: r… |
| المتطلب | REQ-TRX-008 | A simulation run shall record inject deliveries as an append-only, strictly time-ordered log. |
| حالة الاستخدام | UC-162 | Conduct Exercise Simulation |
<!-- END GENERATED: refs US-PLT-SIM-INJECT-LATENCY -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-TRX-003 | An exercise shall be planned only against a scenario that is ACTIVE at that instant; the scenario reference s… | `US-BC05-S-EXERCISE-01`، `US-BC05-S-EXERCISE-02` | TST-EXERCISE-SM، TST-SLC19-INVARIANTS |
| REQ-TRX-004 | An exercise shall be scheduled with a valid time window, a location and confirmed participants before it can… | `US-BC05-S-EXERCISE-01`، `US-BC05-S-EXERCISE-02` | TST-EXERCISE-SM |
| REQ-TRX-005 | Starting a scheduled exercise shall create exactly one linked simulation run, in the same unit of work. | `US-BC05-S-EXERCISE-01`، `US-BC05-S-EXERCISE-02` | TST-EXERCISE-SM، TST-SLC19-INVARIANTS |
| REQ-TRX-006 | An exercise's terminal outcome (COMPLETED or ABORTED) shall be driven exclusively by its linked simulation's… | `US-BC05-S-EXERCISE-01`، `US-BC05-S-EXERCISE-02` | TST-EXERCISE-SM، TST-SLC19-INVARIANTS |
| REQ-TRX-007 | An exercise shall be cancellable with a reason before it starts, and never once it is in progress. | `US-BC05-S-EXERCISE-01`، `US-BC05-S-EXERCISE-02` | TST-EXERCISE-SM |
| REQ-TRX-008 | A simulation run shall record inject deliveries as an append-only, strictly time-ordered log. | `US-BC05-SIM-ABORT`، `US-BC05-SIM-COMPLETE`، `US-BC05-SIM-DELIVER-INJECT`، `US-BC05-SIM-PAUSE`، `US-BC05-SIM-RESUME`، `US-BC05-SIM-START`، `US-PLT-SIM-INJECT-LATENCY`، `US-UI-SCR48-CONTROL-CONSOLE` | TST-SIMULATION-SM |
| REQ-TRX-009 | A simulation run shall record a per-participant, per-competency evaluation, always by an evaluator distinct f… | `US-BC05-SIM-ABORT`، `US-BC05-SIM-COMPLETE`، `US-BC05-SIM-DELIVER-INJECT`، `US-BC05-SIM-PAUSE`، `US-BC05-SIM-RESUME`، `US-BC05-SIM-START` | TST-SIMULATION-SM |
| REQ-TRX-010 | A simulation run shall reach COMPLETED only when every participant listed on its linked exercise has at least… | `US-BC05-SIM-ABORT`، `US-BC05-SIM-COMPLETE`، `US-BC05-SIM-DELIVER-INJECT`، `US-BC05-SIM-PAUSE`، `US-BC05-SIM-RESUME`، `US-BC05-SIM-START`، `US-UI-SCR48-COMPLETE-GUARD` | TST-SIMULATION-SM، TST-SLC19-INVARIANTS |
| REQ-TRX-011 | A simulation run shall be pausable and resumable, or abortable with a reason, without losing any previously r… | `US-BC05-SIM-ABORT`، `US-BC05-SIM-COMPLETE`، `US-BC05-SIM-DELIVER-INJECT`، `US-BC05-SIM-PAUSE`، `US-BC05-SIM-RESUME`، `US-BC05-SIM-START`، `US-UI-SCR48-CONTROL-CONSOLE` | TST-SIMULATION-SM |
| REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… | `US-BC05-Q-SIM-GET`، `US-BC05-Q-SIM-LIST` | — |
| REQ-TRX-015 | The system shall provide the full, ordered timeline of inject deliveries and evaluations for a simulation run… | `US-UI-SCR48-LIVE-TIMELINE` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
