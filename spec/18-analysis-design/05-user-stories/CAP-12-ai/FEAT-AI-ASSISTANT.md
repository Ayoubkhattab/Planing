---
id: FEAT-AI-ASSISTANT
type: feature
title: "المساعد الذكي"
status: DRAFT
version: "0.1"
capability: CAP-12.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# المساعد الذكي

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-AI-ASSISTANT |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-12 المساعدة بالذكاء الاصطناعي |
| القدرة الفرعية | CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2) |
| الأدوار | أي مستخدم مخوَّل؛ النظام |
| الشاشات | SCR-45 المساعد الذكي |
| حالات الاستخدام | UC-070، UC-072 |
| القصص | 12: 6 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح للمستخدم طرح سؤال على المساعد الذكي والحصول على إجابة مستندة إلى أدلة مع استشهاداتها، أو إبلاغه صراحة بعدم كفاية الأدلة.

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
| `US-BC07-AIR-CANCEL` | إلغاء طلب الذكاء الاصطناعي | أمر | مسودة |
| `US-BC07-AIR-SUBMIT` | تقديم طلب الذكاء الاصطناعي | أمر | مسودة |
| `US-BC07-Q-AIR-GET` | جلب: Request with answer, statements and citations (visible only), status | جلب | مسودة |
| `US-BC07-S-AI-REQUEST-01` | تلقائي: policy denied (طلب الذكاء الاصطناعي) | نظام | مسودة |
| `US-BC07-S-AI-REQUEST-04` | تلقائي: no sufficient evidence retrieved (طلب الذكاء الاصطناعي) | نظام | مسودة |
| `US-BC07-S-AI-REQUEST-07` | تلقائي: error or timeout (طلب الذكاء الاصطناعي) | نظام | مسودة |
| `US-UI-SCR45-AIL-BADGE` | معرفة أن المخرج آلي ومستوى استقلاليته | واجهة | مسودة |
| `US-UI-SCR45-CITATIONS` | فتح استشهاد كل عبارة في الإجابة | واجهة | مسودة |
| `US-UI-SCR45-OUTCOMES` | فهم سبب غياب الإجابة | واجهة | مسودة |
| `US-UI-SCR45-STREAMING` | عرض الإجابة تدريجيًا مع مرحلة المعالجة | واجهة | مسودة |
| `US-PLT-AI-ANSWER-LATENCY` | أول رمز خلال 3 ثوانٍ والإجابة خلال 20 | منصة | مسودة |
| `US-OPS-AI-SERVING-OUTAGE` | استمرار المنصة عند تعطل خدمة الذكاء الاصطناعي | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-AIR-CANCEL — إلغاء طلب الذكاء الاصطناعي

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

<!-- BEGIN GENERATED: refs US-BC07-AIR-CANCEL -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/requests/{id}/actions/cancel` | — |
| الأمر | `CMD-AIR-CANCEL` | إلغاء طلب الذكاء الاصطناعي |
| السياسة | `POL-AIR-CANCEL` | any authorized user (submit, cancel)؛ tenant match; object visible |
| الحدث | `EVT-AIR-CANCELLED` | يصل إلى: AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-001، REQ-AI-002، REQ-AI-003، REQ-AI-004، REQ-AI-008، REQ-AI-011، REQ-AI-012 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-070، UC-072 | Submit AI Request؛ Generate AI Result |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-AIR-CANCEL -->

</details>

### 5.2 US-BC07-AIR-SUBMIT — تقديم طلب الذكاء الاصطناعي

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

<!-- BEGIN GENERATED: refs US-BC07-AIR-SUBMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/ai/requests` | — |
| الأمر | `CMD-AIR-SUBMIT` | تقديم طلب الذكاء الاصطناعي |
| السياسة | `POL-AIR-SUBMIT` | any authorized user (submit, cancel)؛ tenant match; operation allowed by routing and matrix |
| الحدث | `EVT-AIR-RECEIVED` | يصل إلى: AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-001، REQ-AI-002، REQ-AI-003، REQ-AI-004، REQ-AI-008، REQ-AI-011، REQ-AI-012 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-070، UC-072 | Submit AI Request؛ Generate AI Result |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-AIR-SUBMIT -->

</details>

### 5.3 US-BC07-Q-AIR-GET — جلب: Request with answer, statements and citations (visible only), status

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

<!-- BEGIN GENERATED: refs US-BC07-Q-AIR-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/ai/requests/{request_id}` | — |
| الاستعلام | `QRY-AIR-GET` | Request with answer, statements and citations (visible only), status |
| السياسة | `POL-AIR-GET` | requester; Auditor (metadata) |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلب | REQ-AI-001 | The system shall process every AI request through identity, policy, authorized retrieval, context package, mo… |
| حالات الاستخدام | UC-070، UC-072 | Submit AI Request؛ Generate AI Result |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-Q-AIR-GET -->

</details>

### 5.4 US-BC07-S-AI-REQUEST-01 — تلقائي: policy denied (طلب الذكاء الاصطناعي)

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

<!-- BEGIN GENERATED: refs US-BC07-S-AI-REQUEST-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:policy denied` | PDP on (user, ai.<operation>, scope) denied or AIL above matrix |
| الانتقال | RECEIVED ← REFUSED | — |
| الحدث | `EVT-AIR-REFUSED` | يصل إلى: AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-001، REQ-AI-002، REQ-AI-003، REQ-AI-004، REQ-AI-008، REQ-AI-011، REQ-AI-012 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-070، UC-072 | Submit AI Request؛ Generate AI Result |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-AI-REQUEST-01 -->

</details>

### 5.5 US-BC07-S-AI-REQUEST-04 — تلقائي: no sufficient evidence retrieved (طلب الذكاء الاصطناعي)

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

<!-- BEGIN GENERATED: refs US-BC07-S-AI-REQUEST-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:no sufficient evidence retrieved` | coverage below threshold (SPEC-AI §4) |
| الانتقال | RETRIEVING ← INSUFFICIENT_EVIDENCE | — |
| الحدث | `EVT-AIR-INSUFFICIENT-EVIDENCE` | يصل إلى: AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-001، REQ-AI-002، REQ-AI-003، REQ-AI-004، REQ-AI-008، REQ-AI-011، REQ-AI-012 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-070، UC-072 | Submit AI Request؛ Generate AI Result |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-AI-REQUEST-04 -->

</details>

### 5.6 US-BC07-S-AI-REQUEST-07 — تلقائي: error or timeout (طلب الذكاء الاصطناعي)

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

<!-- BEGIN GENERATED: refs US-BC07-S-AI-REQUEST-07 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:error or timeout` | error recorded |
| الانتقال | RETRIEVING, GENERATING ← FAILED | — |
| الحدث | `EVT-AIR-FAILED` | يصل إلى: AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| الكيان | `AGG-AI-REQUEST` | طلب الذكاء الاصطناعي |
| الجدول | `ai.ai_requests` | الجدول الرئيسي لطلب الذكاء الاصطناعي |
| وحدة النشر | DU-16 | — |
| المتطلبات | REQ-AI-001، REQ-AI-002، REQ-AI-003، REQ-AI-004، REQ-AI-008، REQ-AI-011، REQ-AI-012 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-070، UC-072 | Submit AI Request؛ Generate AI Result |
| الاختبار | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS | دورة حالات طلب الذكاء الاصطناعي، وثوابت الشريحة SLC-10 |
<!-- END GENERATED: refs US-BC07-S-AI-REQUEST-07 -->

</details>

### 5.7 US-UI-SCR45-AIL-BADGE — معرفة أن المخرج آلي ومستوى استقلاليته

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

<!-- BEGIN GENERATED: refs US-UI-SCR45-AIL-BADGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §12` | — |
| المصدر | `10-ai/autonomy-matrix.md` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… |
| حالات الاستخدام | UC-073، UC-074 | Review AI Result؛ Approve AI-Assisted Result |
<!-- END GENERATED: refs US-UI-SCR45-AIL-BADGE -->

</details>

### 5.8 US-UI-SCR45-CITATIONS — فتح استشهاد كل عبارة في الإجابة

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

<!-- BEGIN GENERATED: refs US-UI-SCR45-CITATIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §12` | — |
| الشاشة | SCR-45 | شاشة المساعد الذكي |
| المصدر | `03-domain/contexts/BC07/grounded-ai-spec.md §4` | — |
| المتطلب | REQ-AI-004 | The system shall attach to every AI statement the citations (claim, evidence, source, context reference) that… |
| حالة الاستخدام | UC-072 | Generate AI Result |
<!-- END GENERATED: refs US-UI-SCR45-CITATIONS -->

</details>

### 5.9 US-UI-SCR45-OUTCOMES — فهم سبب غياب الإجابة

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

<!-- BEGIN GENERATED: refs US-UI-SCR45-OUTCOMES -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §12` | — |
| المصدر | `21-ui-design.md §6.2` | — |
| المصدر | `09-reliability/fmea-slc10.md FM-S10-01` | — |
| المتطلب | REQ-AI-003 | If the retrieved evidence is insufficient to answer, then the system shall return 'Insufficient Evidence' ins… |
| حالة الاستخدام | UC-072 | Generate AI Result |
<!-- END GENERATED: refs US-UI-SCR45-OUTCOMES -->

</details>

### 5.10 US-UI-SCR45-STREAMING — عرض الإجابة تدريجيًا مع مرحلة المعالجة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| واجهة | R2 | Should | لا | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-UI-SCR45-STREAMING -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AI-003 | grounded Q&A request → first token ≤ 3 s, full answer p95 ≤ 20 s on local models |
| المصدر | `21-ui-design.md §13` | — |
| الشاشة | SCR-45 | شاشة المساعد الذكي |
| المصدر | `US-BC07-AIR-CANCEL` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR45-STREAMING -->

</details>

### 5.11 US-PLT-AI-ANSWER-LATENCY — أول رمز خلال 3 ثوانٍ والإجابة خلال 20

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| منصة | R2 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-PLT-AI-ANSWER-LATENCY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AI-003 | grounded Q&A request → first token ≤ 3 s, full answer p95 ≤ 20 s on local models |
| القرار التقني | TD-18 | vLLM (Apache 2.0) on a per-cell GPU pool; open-weight models with Arabic support chosen by evaluation (AGG-MO… |
| المصدر | `03-domain/contexts/BC07/grounded-ai-spec.md §7` | — |
<!-- END GENERATED: refs US-PLT-AI-ANSWER-LATENCY -->

</details>

### 5.12 US-OPS-AI-SERVING-OUTAGE — استمرار المنصة عند تعطل خدمة الذكاء الاصطناعي

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

<!-- BEGIN GENERATED: refs US-OPS-AI-SERVING-OUTAGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/fmea-slc10.md FM-S10-01` | — |
| المصدر | `22-deployment-design.md §4` | — |
<!-- END GENERATED: refs US-OPS-AI-SERVING-OUTAGE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-AI-001 | The system shall process every AI request through identity, policy, authorized retrieval, context package, mo… | كل قصص الميزة المأخوذة من المواصفة (6) | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-002 | The system shall build context packages only from data retrieved with the requesting user's authorization, in… | كل قصص الأوامر والنظام في الميزة (5) | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-003 | If the retrieved evidence is insufficient to answer, then the system shall return 'Insufficient Evidence' ins… | `US-BC07-AIR-CANCEL`، `US-BC07-AIR-SUBMIT`، `US-BC07-S-AI-REQUEST-01`، `US-BC07-S-AI-REQUEST-04`، `US-BC07-S-AI-REQUEST-07`، `US-UI-SCR45-OUTCOMES` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-004 | The system shall attach to every AI statement the citations (claim, evidence, source, context reference) that… | `US-BC07-AIR-CANCEL`، `US-BC07-AIR-SUBMIT`، `US-BC07-S-AI-REQUEST-01`، `US-BC07-S-AI-REQUEST-04`، `US-BC07-S-AI-REQUEST-07`، `US-UI-SCR45-CITATIONS` | TST-AI-REQUEST-SM، TST-SLC10-INVARIANTS |
| REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human… | `US-UI-SCR45-AIL-BADGE` | TST-AI-RESULT-SM، TST-SLC10-INVARIANTS |
| REQ-AI-008 | The system shall enforce the AI autonomy matrix, allowing at most AIL3 in R2 and forbidding AIL5. | كل قصص الأوامر والنظام في الميزة (5) | TST-AI-REQUEST-SM، TST-AI-RESULT-SM، TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS |
| REQ-AI-011 | The system shall run all models on local infrastructure by default and shall use external models only where a… | كل قصص الأوامر والنظام في الميزة (5) | TST-AI-REQUEST-SM، TST-AI-ROUTING-SM، TST-SLC10-INVARIANTS |
| REQ-AI-012 | If content retrieved into a context package contains instructions, then the system shall treat it as data and… | كل قصص الأوامر والنظام في الميزة (5) | TST-AI-REQUEST-SM، TST-AI-TOOL-SM، TST-SLC10-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
