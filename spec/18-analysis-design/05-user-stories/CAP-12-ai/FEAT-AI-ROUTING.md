---
id: FEAT-AI-ROUTING
type: feature
title: "توجيه نماذج الذكاء الاصطناعي"
status: DRAFT
version: "0.2"
capability: CAP-12.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv, 18-analysis-design/05-user-stories/us-bc07.md, 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md, 03-domain/contexts/BC07/grounded-ai-spec.md, 02-requirements/requirements.md, 08-security/policies-slc10.md, 08-security/threat-model-slc10.md, 18-analysis-design/21-ui-design.md, 13-verification/acceptance/SLC-10/invariants-slc10.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# توجيه نماذج الذكاء الاصطناعي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-AI-ROUTING |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-12 المساعدة بالذكاء الاصطناعي |
| القدرة الفرعية | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) |
| الأدوار | مهندس الذكاء الاصطناعي وحوكمته؛ صاحب السلطة أو المعتمِد الثاني؛ مسؤول الأمن؛ النظام |
| الشاشات | SCR-51 النماذج والتوجيه والأدوات والاستهلاك |
| حالات الاستخدام | UC-077 |
| القصص | 10: 6 من المواصفة، و4 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يحدد لكل مستأجر أي نموذج يخدم أي نوع من الطلبات، محليًا افتراضيًا، ولا يُسمح بنموذج خارجي إلا بسياسة صريحة وبيانات غير مصنفة.

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
| QAS-AI-003 | grounded Q&A request | first token ≤ 3 s, full answer p95 ≤ 20 s on local models |
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
| `US-BC07-RTG-ACTIVATE` | تفعيل توجيه الذكاء الاصطناعي | أمر | مسودة |
| `US-BC07-RTG-DISCARD` | تجاهل مسودة توجيه الذكاء الاصطناعي | أمر | مسودة |
| `US-BC07-RTG-DRAFT` | إعداد مسودة توجيه الذكاء الاصطناعي | أمر | مسودة |
| `US-BC07-RTG-EDIT` | تعديل توجيه الذكاء الاصطناعي | أمر | مسودة |
| `US-DOM-AI-PROMPT-TEMPLATE` | إدارة نسخ قوالب التعليمات | أمر | مسودة |
| `US-BC07-Q-RTG-ACTIVE` | جلب: Active routing for the tenant | جلب | مسودة |
| `US-BC07-S-AI-ROUTING-01` | تلقائي: successor activated (توجيه الذكاء الاصطناعي) | نظام | مسودة |
| `US-UI-SCR51-ROUTING` | مراجعة توجيه كل عملية قبل تفعيله | واجهة | مسودة |
| `US-INT-AI-EXTERNAL-MODEL` | استدعاء نموذج خارجي بسياسة وبيانات غير مصنفة فقط | تكامل | مسودة |
| `US-OPS-AI-EGRESS-MONITOR` | رصد أي خروج إلى نموذج خارجي دون سياسة | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-RTG-ACTIVATE — تفعيل توجيه الذكاء الاصطناعي

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC07-RTG-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/routings/{id}/actions/activate` | — |
| الأمر | `CMD-RTG-ACTIVATE` | تفعيل توجيه الذكاء الاصطناعي |
| السياسة | `POL-RTG-ACTIVATE` | AI governance authority (draft, edit) · second authority (activate)؛ tenant match; object visible |
| الحدث | `EVT-RTG-ACTIVATED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-AI-ROUTING` | توجيه الذكاء الاصطناعي |
| الجدول | `ai.ai_routings` | الجدول الرئيسي لتوجيه الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-008، REQ-AI-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-077 | Configure AI Routing & Tool Registry |
| الاختبار | TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS | دورة حالات توجيه الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-RTG-ACTIVATE -->

</details>

### 5.2 US-BC07-RTG-DISCARD — تجاهل مسودة توجيه الذكاء الاصطناعي

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC07-RTG-DISCARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/routings/{id}/actions/discard` | — |
| الأمر | `CMD-RTG-DISCARD` | تجاهل مسودة توجيه الذكاء الاصطناعي |
| السياسة | `POL-RTG-DISCARD` | AI governance authority (draft, edit) · second authority (activate)؛ tenant match; object visible |
| الحدث | `EVT-RTG-DISCARDED` | يصل إلى: Model router; PEP cache |
| الكيان | `AGG-AI-ROUTING` | توجيه الذكاء الاصطناعي |
| الجدول | `ai.ai_routings` | الجدول الرئيسي لتوجيه الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-008، REQ-AI-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-077 | Configure AI Routing & Tool Registry |
| الاختبار | TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS | دورة حالات توجيه الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-RTG-DISCARD -->

</details>

### 5.3 US-BC07-RTG-DRAFT — إعداد مسودة توجيه الذكاء الاصطناعي

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC07-RTG-DRAFT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/routings` | — |
| الأمر | `CMD-RTG-DRAFT` | إعداد مسودة توجيه الذكاء الاصطناعي |
| السياسة | `POL-RTG-DRAFT` | AI governance authority (draft, edit) · second authority (activate)؛ tenant match; object visible |
| الحدث | `EVT-RTG-DRAFTED` | يصل إلى: Model router; PEP cache |
| الكيان | `AGG-AI-ROUTING` | توجيه الذكاء الاصطناعي |
| الجدول | `ai.ai_routings` | الجدول الرئيسي لتوجيه الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-008، REQ-AI-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-077 | Configure AI Routing & Tool Registry |
| الاختبار | TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS | دورة حالات توجيه الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-RTG-DRAFT -->

</details>

### 5.4 US-BC07-RTG-EDIT — تعديل توجيه الذكاء الاصطناعي

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC07-RTG-EDIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/routings/{id}/actions/edit` | — |
| الأمر | `CMD-RTG-EDIT` | تعديل توجيه الذكاء الاصطناعي |
| السياسة | `POL-RTG-EDIT` | AI governance authority (draft, edit) · second authority (activate)؛ tenant match; object visible |
| الحدث | `EVT-RTG-EDITED` | يصل إلى: Model router; PEP cache |
| الكيان | `AGG-AI-ROUTING` | توجيه الذكاء الاصطناعي |
| الجدول | `ai.ai_routings` | الجدول الرئيسي لتوجيه الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-008، REQ-AI-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-077 | Configure AI Routing & Tool Registry |
| الاختبار | TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS | دورة حالات توجيه الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-RTG-EDIT -->

</details>

### 5.5 US-DOM-AI-PROMPT-TEMPLATE — إدارة نسخ قوالب التعليمات

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| أمر | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-DOM-AI-PROMPT-TEMPLATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md INV-RTG-02` | — |
| حالة الاستخدام | UC-077 | Configure AI Routing & Tool Registry |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-AI-001 | The system shall process every AI request through identity, policy, authorized retrieval, context package, mo… |
| حالات الاستخدام | UC-070، UC-071، UC-072 | Submit AI Request؛ Retrieve Authorized Context؛ Generate AI Result |
<!-- END GENERATED: refs US-DOM-AI-PROMPT-TEMPLATE -->

</details>

### 5.6 US-BC07-Q-RTG-ACTIVE — جلب: Active routing for the tenant

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| جلب | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC07-Q-RTG-ACTIVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/ai/routing` | — |
| الاستعلام | `QRY-RTG-ACTIVE` | Active routing for the tenant |
| السياسة | `POL-RTG-ACTIVE` | AI governance, Security Officer |
| الكيان | `AGG-AI-ROUTING` | توجيه الذكاء الاصطناعي |
| الجدول | `ai.ai_routings` | الجدول الرئيسي لتوجيه الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-008 | The system shall enforce the AI autonomy matrix, allowing at most AIL3 in R2 and forbidding AIL5. |
| حالة الاستخدام | UC-074 | Approve AI-Assisted Result |
| الاختبار | TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS | دورة حالات توجيه الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-Q-RTG-ACTIVE -->

</details>

### 5.7 US-BC07-S-AI-ROUTING-01 — تلقائي: successor activated (توجيه الذكاء الاصطناعي)

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| نظام | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-BC07-S-AI-ROUTING-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:successor activated` | system |
| الانتقال | ACTIVE ← SUPERSEDED | — |
| الحدث | `EVT-RTG-SUPERSEDED` | يصل إلى: Model router; PEP cache |
| الكيان | `AGG-AI-ROUTING` | توجيه الذكاء الاصطناعي |
| الجدول | `ai.ai_routings` | الجدول الرئيسي لتوجيه الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-008، REQ-AI-011 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-077 | Configure AI Routing & Tool Registry |
| الاختبار | TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS | دورة حالات توجيه الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-AI-ROUTING-01 -->

</details>

### 5.8 US-UI-SCR51-ROUTING — مراجعة توجيه كل عملية قبل تفعيله

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Must | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR51-ROUTING -->
| البند | المعرّف | المعنى |
|---|---|---|
| حالة الاستخدام | UC-077 | Configure AI Routing & Tool Registry |
| الشاشة | SCR-51 | شاشة النماذج والتوجيه والأدوات والاستهلاك |
| المصدر | `US-BC07-RTG-EDIT` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-AI-011 | The system shall run all models on local infrastructure by default and shall use external models only where a… |
| حالة الاستخدام | UC-077 | Configure AI Routing & Tool Registry |
<!-- END GENERATED: refs US-UI-SCR51-ROUTING -->

</details>

### 5.9 US-INT-AI-EXTERNAL-MODEL — استدعاء نموذج خارجي بسياسة وبيانات غير مصنفة فقط

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-AI-EXTERNAL-MODEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `PB-13` | — |
| المصدر | `13-verification/acceptance/SLC-10/invariants-slc10.md` | — |
| فحص البنية | FIT-12 | No external network dependency at runtime or build (air-gapped) |
| المتطلب | REQ-AI-011 | The system shall run all models on local infrastructure by default and shall use external models only where a… |
| حالة الاستخدام | UC-077 | Configure AI Routing & Tool Registry |
<!-- END GENERATED: refs US-INT-AI-EXTERNAL-MODEL -->

</details>

### 5.10 US-OPS-AI-EGRESS-MONITOR — رصد أي خروج إلى نموذج خارجي دون سياسة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-AI-EGRESS-MONITOR -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `THR-S10-03` | — |
| المتطلبات | REQ-AI-011، REQ-GOV-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-077 | Configure AI Routing & Tool Registry |
<!-- END GENERATED: refs US-OPS-AI-EGRESS-MONITOR -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-AI-001 | The system shall process every AI request through identity, policy, authorized retrieval, context package, mo… | `US-DOM-AI-PROMPT-TEMPLATE` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-008 | The system shall enforce the AI autonomy matrix, allowing at most AIL3 in R2 and forbidding AIL5. | كل قصص الميزة المأخوذة من المواصفة (6) | TST-AI-REQUEST-SM، TST-AI-RESULT-SM، TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS |
| REQ-AI-011 | The system shall run all models on local infrastructure by default and shall use external models only where a… | `US-BC07-RTG-ACTIVATE`، `US-BC07-RTG-DISCARD`، `US-BC07-RTG-DRAFT`، `US-BC07-RTG-EDIT`، `US-BC07-S-AI-ROUTING-01`، `US-INT-AI-EXTERNAL-MODEL`، `US-OPS-AI-EGRESS-MONITOR`، `US-UI-SCR51-ROUTING` | TST-AI-REQUEST-SM، TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS |
| REQ-GOV-005 | The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data… | `US-OPS-AI-EGRESS-MONITOR` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
