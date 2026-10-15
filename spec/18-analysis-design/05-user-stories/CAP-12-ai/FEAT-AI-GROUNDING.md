---
id: FEAT-AI-GROUNDING
type: feature
title: "تأريض الإجابات بالأدلة المخوَّلة"
status: DRAFT
version: "0.1"
capability: CAP-12.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# تأريض الإجابات بالأدلة المخوَّلة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-AI-GROUNDING |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-12 المساعدة بالذكاء الاصطناعي |
| القدرة الفرعية | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) |
| الأدوار | النظام؛ المدقِّق |
| الشاشات | SCR-69 التدقيق، SCR-45 المساعد الذكي |
| حالات الاستخدام | UC-071، UC-072 |
| القصص | 13: 5 من المواصفة، و8 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضمن أن المساعد لا يستخدم إلا البيانات التي يحق للسائل رؤيتها وأن كل عبارة في الإجابة مسندة إلى دليل يمكن تدقيقه.

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
| QAS-AI-001 | evaluation set of 500 questions | ≥ 95 % of cited items actually support the statement |
| QAS-AI-002 | insufficient-evidence and hallucination sets | ≤ 2 % unsupported statements; ≥ 95 % correct 'Insufficient Evidence' |
| QAS-AI-003 | grounded Q&A request | first token ≤ 3 s, full answer p95 ≤ 20 s on local models |
| QAS-AI-004 | prompt-injection, exfiltration and unauthorized-retrieval suites | 0 unauthorized retrievals, 0 tool abuse, 0 cross-tenant leakage |
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
| `US-BC07-Q-AIR-CONTEXT` | جلب: Context package items (URN, version, label) — for audit and review | جلب | مسودة |
| `US-BC07-S-AI-REQUEST-02` | تلقائي: retrieval started (طلب الذكاء الاصطناعي) | نظام | مسودة |
| `US-BC07-S-AI-REQUEST-03` | تلقائي: context package sealed (طلب الذكاء الاصطناعي) | نظام | مسودة |
| `US-BC07-S-AI-REQUEST-05` | تلقائي: output grounded (طلب الذكاء الاصطناعي) | نظام | مسودة |
| `US-BC07-S-AI-REQUEST-06` | تلقائي: output not grounded (طلب الذكاء الاصطناعي) | نظام | مسودة |
| `US-UI-SCR69-AI-LINEAGE` | تتبع العبارة إلى حزمة السياق والنموذج | واجهة | مسودة |
| `US-PLT-AI-AUTONOMY-MATRIX` | فرض حدود استقلالية الذكاء الاصطناعي | منصة | مسودة |
| `US-PLT-AI-GROUNDING-VERIFIER` | التحقق من إسناد كل عبارة قبل عرضها | منصة | مسودة |
| `US-PLT-AI-INJECTION-GUARD` | معاملة المحتوى المسترجع بيانات لا تعليمات | منصة | مسودة |
| `US-PLT-AI-LINEAGE-RECORD` | حفظ أصل كل مخرج آلي مختومًا ومشفرًا | منصة | مسودة |
| `US-PLT-AI-VECTOR-PROJECTION` | استرجاع متجهي بنفس تسميات البحث وتصفيته | منصة | مسودة |
| `US-OPS-AI-INJECTION-ALERT` | إحالة ارتفاع محاولات الحقن إلى الأمن | تشغيل | مسودة |
| `US-OPS-AI-VECTOR-LAG` | مراقبة تأخر الإسقاط المتجهي | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-Q-AIR-CONTEXT — جلب: Context package items (URN, version, label) — for audit and review

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

<!-- BEGIN GENERATED: refs US-BC07-Q-AIR-CONTEXT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/ai/requests/{request_id}/context` | — |
| الاستعلام | `QRY-AIR-CONTEXT` | Context package items (URN, version, label) — for audit and review |
| السياسة | `POL-AIR-CONTEXT` | requester if cleared; Auditor |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-002 | The system shall build context packages only from data retrieved with the requesting user's authorization, in… |
| حالة الاستخدام | UC-071 | Retrieve Authorized Context |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-Q-AIR-CONTEXT -->

</details>

### 5.2 US-BC07-S-AI-REQUEST-02 — تلقائي: retrieval started (طلب الذكاء الاصطناعي)

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

<!-- BEGIN GENERATED: refs US-BC07-S-AI-REQUEST-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:retrieval started` | authorized hybrid retrieval as the user (SPEC-AI §2) |
| الانتقال | RECEIVED ← RETRIEVING | — |
| الحدث | `EVT-AIR-RETRIEVING` | يصل إلى: AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-001، REQ-AI-002، REQ-AI-003، REQ-AI-004، REQ-AI-008، REQ-AI-011، REQ-AI-012 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-071، UC-072 | Retrieve Authorized Context؛ Generate AI Result |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-AI-REQUEST-02 -->

</details>

### 5.3 US-BC07-S-AI-REQUEST-03 — تلقائي: context package sealed (طلب الذكاء الاصطناعي)

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

<!-- BEGIN GENERATED: refs US-BC07-S-AI-REQUEST-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:context package sealed` | context items pinned (URN + version/known_at + label); package hash; token budget respected |
| الانتقال | RETRIEVING ← GENERATING | — |
| الحدث | `EVT-AIR-CONTEXT-SEALED` | يصل إلى: AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-001، REQ-AI-002، REQ-AI-003، REQ-AI-004، REQ-AI-008، REQ-AI-011، REQ-AI-012 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-071، UC-072 | Retrieve Authorized Context؛ Generate AI Result |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-AI-REQUEST-03 -->

</details>

### 5.4 US-BC07-S-AI-REQUEST-05 — تلقائي: output grounded (طلب الذكاء الاصطناعي)

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

<!-- BEGIN GENERATED: refs US-BC07-S-AI-REQUEST-05 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:output grounded` | every statement cites ≥ 1 context item; citation check passed; output label = max(context labels); guard chec… |
| الانتقال | GENERATING ← COMPLETED | — |
| الحدث | `EVT-AIR-COMPLETED` | يصل إلى: AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-001، REQ-AI-002، REQ-AI-003، REQ-AI-004، REQ-AI-008، REQ-AI-011، REQ-AI-012 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-071، UC-072 | Retrieve Authorized Context؛ Generate AI Result |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-AI-REQUEST-05 -->

</details>

### 5.5 US-BC07-S-AI-REQUEST-06 — تلقائي: output not grounded (طلب الذكاء الاصطناعي)

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

<!-- BEGIN GENERATED: refs US-BC07-S-AI-REQUEST-06 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:output not grounded` | ungrounded statements removed leave no answer |
| الانتقال | GENERATING ← INSUFFICIENT_EVIDENCE | — |
| الحدث | `EVT-AIR-INSUFFICIENT-EVIDENCE` | يصل إلى: AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-001، REQ-AI-002، REQ-AI-003، REQ-AI-004، REQ-AI-008، REQ-AI-011، REQ-AI-012 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-071، UC-072 | Retrieve Authorized Context؛ Generate AI Result |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-AI-REQUEST-06 -->

</details>

### 5.6 US-UI-SCR69-AI-LINEAGE — تتبع العبارة إلى حزمة السياق والنموذج

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

<!-- BEGIN GENERATED: refs US-UI-SCR69-AI-LINEAGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-69 | شاشة التدقيق |
| المصدر | `US-BC07-Q-AIR-CONTEXT` | — |
| المصدر | `03-domain/contexts/BC07/grounded-ai-spec.md §5` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-AI-001 | The system shall process every AI request through identity, policy, authorized retrieval, context package, mo… |
| حالات الاستخدام | UC-071، UC-072 | Retrieve Authorized Context؛ Generate AI Result |
<!-- END GENERATED: refs US-UI-SCR69-AI-LINEAGE -->

</details>

### 5.7 US-PLT-AI-AUTONOMY-MATRIX — فرض حدود استقلالية الذكاء الاصطناعي

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-AI-AUTONOMY-MATRIX -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `10-ai/autonomy-matrix.md` | — |
| المصدر | `03-domain/contexts/BC07/grounded-ai-spec.md §6` | — |
| القرار المعماري | ADR-P10 | Autonomy Level Naming (AIL vs DAL) |
| المتطلب | REQ-AI-008 | The system shall enforce the AI autonomy matrix, allowing at most AIL3 in R2 and forbidding AIL5. |
| حالة الاستخدام | UC-074 | Approve AI-Assisted Result |
<!-- END GENERATED: refs US-PLT-AI-AUTONOMY-MATRIX -->

</details>

### 5.8 US-PLT-AI-GROUNDING-VERIFIER — التحقق من إسناد كل عبارة قبل عرضها

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-AI-GROUNDING-VERIFIER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AI-002 | insufficient-evidence and hallucination sets → ≤ 2 % unsupported statements; ≥ 95 % correct 'Insufficient Evi… |
| المصدر | `03-domain/contexts/BC07/grounded-ai-spec.md §4` | — |
| المصدر | `09-reliability/fmea-slc10.md FM-S10-02` | — |
| المتطلبات | REQ-AI-003، REQ-AI-004 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-072 | Generate AI Result |
<!-- END GENERATED: refs US-PLT-AI-GROUNDING-VERIFIER -->

</details>

### 5.9 US-PLT-AI-INJECTION-GUARD — معاملة المحتوى المسترجع بيانات لا تعليمات

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-AI-INJECTION-GUARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AI-004 | prompt-injection, exfiltration and unauthorized-retrieval suites → 0 unauthorized retrievals, 0 tool abuse, 0… |
| المصدر | `THR-S10-02` | — |
| المصدر | `THR-S10-03` | — |
| المصدر | `03-domain/contexts/BC07/grounded-ai-spec.md §5` | — |
| المتطلب | REQ-AI-012 | If content retrieved into a context package contains instructions, then the system shall treat it as data and… |
| حالة الاستخدام | UC-071 | Retrieve Authorized Context |
<!-- END GENERATED: refs US-PLT-AI-INJECTION-GUARD -->

</details>

### 5.10 US-PLT-AI-LINEAGE-RECORD — حفظ أصل كل مخرج آلي مختومًا ومشفرًا

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-AI-LINEAGE-RECORD -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `03-domain/contexts/BC07/grounded-ai-spec.md §3` | — |
| المصدر | `10-ai/autonomy-matrix.md` | — |
| المتطلب | REQ-AI-001 | The system shall process every AI request through identity, policy, authorized retrieval, context package, mo… |
| حالات الاستخدام | UC-071، UC-072 | Retrieve Authorized Context؛ Generate AI Result |
<!-- END GENERATED: refs US-PLT-AI-LINEAGE-RECORD -->

</details>

### 5.11 US-PLT-AI-VECTOR-PROJECTION — استرجاع متجهي بنفس تسميات البحث وتصفيته

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-AI-VECTOR-PROJECTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-19 | OpenSearch k-NN on the existing search cluster (vector projection kind) — no new component; pgvector as fallb… |
| المصدر | `13-verification/acceptance/SLC-10/invariants-slc10.md` | — |
| المتطلبات | REQ-AI-014، REQ-AI-002 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-071 | Retrieve Authorized Context |
<!-- END GENERATED: refs US-PLT-AI-VECTOR-PROJECTION -->

</details>

### 5.12 US-OPS-AI-INJECTION-ALERT — إحالة ارتفاع محاولات الحقن إلى الأمن

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تشغيل | R2 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-OPS-AI-INJECTION-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/observability-slc10.md` | — |
| الجودة | QAS-AI-004 | prompt-injection, exfiltration and unauthorized-retrieval suites → 0 unauthorized retrievals, 0 tool abuse, 0… |
| المصدر | `THR-013` | — |
<!-- END GENERATED: refs US-OPS-AI-INJECTION-ALERT -->

</details>

### 5.13 US-OPS-AI-VECTOR-LAG — مراقبة تأخر الإسقاط المتجهي

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

<!-- BEGIN GENERATED: refs US-OPS-AI-VECTOR-LAG -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/fmea-slc10.md FM-S10-03` | — |
| المتطلب | REQ-AI-014 | The system shall maintain a vector projection of authorized content with the same security labels and pre-fil… |
| حالة الاستخدام | UC-071 | Retrieve Authorized Context |
<!-- END GENERATED: refs US-OPS-AI-VECTOR-LAG -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-AI-001 | The system shall process every AI request through identity, policy, authorized retrieval, context package, mo… | `US-BC07-S-AI-REQUEST-02`، `US-BC07-S-AI-REQUEST-03`، `US-BC07-S-AI-REQUEST-05`، `US-BC07-S-AI-REQUEST-06`، `US-PLT-AI-LINEAGE-RECORD`، `US-UI-SCR69-AI-LINEAGE` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-002 | The system shall build context packages only from data retrieved with the requesting user's authorization, in… | `US-BC07-Q-AIR-CONTEXT`، `US-BC07-S-AI-REQUEST-02`، `US-BC07-S-AI-REQUEST-03`، `US-BC07-S-AI-REQUEST-05`، `US-BC07-S-AI-REQUEST-06`، `US-PLT-AI-VECTOR-PROJECTION` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-003 | If the retrieved evidence is insufficient to answer, then the system shall return 'Insufficient Evidence' ins… | `US-BC07-S-AI-REQUEST-02`، `US-BC07-S-AI-REQUEST-03`، `US-BC07-S-AI-REQUEST-05`، `US-BC07-S-AI-REQUEST-06`، `US-PLT-AI-GROUNDING-VERIFIER` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-004 | The system shall attach to every AI statement the citations (claim, evidence, source, context reference) that… | `US-BC07-S-AI-REQUEST-02`، `US-BC07-S-AI-REQUEST-03`، `US-BC07-S-AI-REQUEST-05`، `US-BC07-S-AI-REQUEST-06`، `US-PLT-AI-GROUNDING-VERIFIER` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-008 | The system shall enforce the AI autonomy matrix, allowing at most AIL3 in R2 and forbidding AIL5. | `US-BC07-S-AI-REQUEST-02`، `US-BC07-S-AI-REQUEST-03`، `US-BC07-S-AI-REQUEST-05`، `US-BC07-S-AI-REQUEST-06`، `US-PLT-AI-AUTONOMY-MATRIX` | TST-AI-REQUEST-SM، TST-AI-RESULT-SM، TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS |
| REQ-AI-011 | The system shall run all models on local infrastructure by default and shall use external models only where a… | كل قصص الأوامر والنظام في الميزة (4) | TST-AI-REQUEST-SM، TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS |
| REQ-AI-012 | If content retrieved into a context package contains instructions, then the system shall treat it as data and… | `US-BC07-S-AI-REQUEST-02`، `US-BC07-S-AI-REQUEST-03`، `US-BC07-S-AI-REQUEST-05`، `US-BC07-S-AI-REQUEST-06`، `US-PLT-AI-INJECTION-GUARD` | TST-AI-REQUEST-SM، TST-AI-TOOL-SM، TST-SLC10-INVARIANTS |
| REQ-AI-014 | The system shall maintain a vector projection of authorized content with the same security labels and pre-fil… | `US-OPS-AI-VECTOR-LAG`، `US-PLT-AI-VECTOR-PROJECTION` | TST-SLC10-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
