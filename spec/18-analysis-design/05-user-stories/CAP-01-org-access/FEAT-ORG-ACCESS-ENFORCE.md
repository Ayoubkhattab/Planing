---
id: FEAT-ORG-ACCESS-ENFORCE
type: feature
title: "فحص الوصول قبل كل طلب"
status: DRAFT
version: "0.1"
capability: CAP-01.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# فحص الوصول قبل كل طلب

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-ORG-ACCESS-ENFORCE |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-01 إدارة المؤسسة والوصول |
| القدرة الفرعية | CAP-01.04 سياسات الوصول (R1) |
| الأدوار | أي مستخدم مخوَّل؛ النظام |
| الشاشات | — |
| حالات الاستخدام | — |
| القصص | 19: 2 من المواصفة، و17 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يضمن فحص كل عرض أو بحث أو تصدير أو طلب للخريطة أو للمساعد الذكي قبل جلب البيانات، فيُمنع أو يُحجب جزئيًا ما لا يحق للمستخدم رؤيته ويُرفض الطلب إذا تعذر الفحص.

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
| QAS-PERF-009 | PEP requests a policy decision | p95 ≤ 5 ms with embedded evaluator; ≤ 20 ms remote |
| QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance | 0 leakage in inference suite (counts, facets, ordering, timing, errors) |
| QAS-SEC-003 | removes a user's compartment | effective on next request in every path, independent of index lag |
| QAS-SEC-004 | request the same map tile | 0 cross-scope cache hits |
| QAS-SEC-005 | policy engine unavailable | 100 % fail-closed |
| QAS-SEC-011 | inference test suite on search, suggestions, facets, graph and paths | 0 disclosures of hidden objects, hidden facts, hidden nodes/edges |
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
| `US-BC01-Q-SEC-CONTEXT` | جلب: Caller's resolved SecurityContext | جلب | مسودة |
| `US-BC08-Q-PDP-DECIDE` | جلب: DecisionRequest → DecisionResponse (authorization-model §2) | جلب | مسودة |
| `US-PLT-ACCESS-ALLOWED-ACTIONS` | إرجاع الأفعال المسموحة مع تفاصيل المورد | منصة | مسودة |
| `US-PLT-ACCESS-DECISION-CACHE` | نفاذ سحب الصلاحية في الطلب التالي | منصة | مسودة |
| `US-PLT-ACCESS-FAIL-CLOSED` | رفض الطلب عند تعذر فحص الصلاحية | منصة | مسودة |
| `US-PLT-ACCESS-OBLIGATIONS` | تطبيق التزامات قرار الوصول | منصة | مسودة |
| `US-PLT-ACCESS-PDP-PERFORMANCE` | قرار الصلاحية خلال خمسة أجزاء من الثانية | منصة | مسودة |
| `US-PLT-ACCESS-PEP-EVERY-PATH` | فحص الصلاحية قبل أي استرجاع للبيانات | منصة | مسودة |
| `US-PLT-ACCESS-QUERY-PREFILTER` | تصفية النتائج دون كشف المحجوب | منصة | مسودة |
| `US-PLT-ACCESS-SECURITY-CONTEXT` | سياق أمني موقّع يرافق كل طلب | منصة | مسودة |
| `US-PLT-ACCESS-SHARED-CACHE` | منع مشاركة النتائج المخزنة بين المستخدمين | منصة | مسودة |
| `US-PLT-ACCESS-STALE-BUNDLE` | تقييد العمل عند تقادم حزمة السياسات | منصة | مسودة |
| `US-PLT-ACCESS-UI-DENIALS` | عرض الرفض دون كشف وجود المورد | منصة | مسودة |
| `US-PLT-ACCESS-UI-LOCAL-STORAGE` | منع حفظ البيانات الحساسة في المتصفح | منصة | مسودة |
| `US-PLT-ACCESS-UI-NAVIGATION` | إظهار مناطق الواجهة حسب صلاحيات المستخدم | منصة | مسودة |
| `US-PLT-ACCESS-UI-REDACTION` | علامة ثابتة للحقل المحجوب | منصة | مسودة |
| `US-OPS-ACCESS-INFERENCE-SUITE` | اختبار عدم الاستدلال واختبار الاختراق | تشغيل | مسودة |
| `US-OPS-ACCESS-MTLS-IDENTITY` | اتصال مشفر بهوية خاصة لكل خدمة | تشغيل | مسودة |
| `US-OPS-ACCESS-PDP-ALERTS` | تنبيهات أداء محرك السياسات وقفزات الرفض | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC01-Q-SEC-CONTEXT — جلب: Caller's resolved SecurityContext

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

<!-- BEGIN GENERATED: refs US-BC01-Q-SEC-CONTEXT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/foundation/me/security-context` | — |
| الاستعلام | `QRY-SEC-CONTEXT` | Caller's resolved SecurityContext |
| السياسة | `POL-SEC-CONTEXT` | org scope of subject roles ∩ classification rule |
| المتطلب | REQ-FND-010 | The system shall evaluate authorization before retrieving data for every command, query, search, map request,… |
<!-- END GENERATED: refs US-BC01-Q-SEC-CONTEXT -->

</details>

### 5.2 US-BC08-Q-PDP-DECIDE — جلب: DecisionRequest → DecisionResponse (authorization-model §2)

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

<!-- BEGIN GENERATED: refs US-BC08-Q-PDP-DECIDE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/governance/policy-decisions` | — |
| الاستعلام | `QRY-PDP-DECIDE` | DecisionRequest → DecisionResponse (authorization-model §2) |
| السياسة | `POL-PDP-DECIDE` | org scope of subject roles ∩ classification rule |
| المتطلب | REQ-FND-010 | The system shall evaluate authorization before retrieving data for every command, query, search, map request,… |
<!-- END GENERATED: refs US-BC08-Q-PDP-DECIDE -->

</details>

### 5.3 US-PLT-ACCESS-ALLOWED-ACTIONS — إرجاع الأفعال المسموحة مع تفاصيل المورد

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-ALLOWED-ACTIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §6.3` | — |
| الجودة | QAS-PERF-009 | PEP requests a policy decision → p95 ≤ 5 ms with embedded evaluator; ≤ 20 ms remote |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-ACCESS-ALLOWED-ACTIONS -->

</details>

### 5.4 US-PLT-ACCESS-DECISION-CACHE — نفاذ سحب الصلاحية في الطلب التالي

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-DECISION-CACHE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-003 | removes a user's compartment → effective on next request in every path, independent of index lag |
| المصدر | `17-security-design.md §3.5` | — |
| المصدر | `23-crosscutting.md §6.1` | — |
<!-- END GENERATED: refs US-PLT-ACCESS-DECISION-CACHE -->

</details>

### 5.5 US-PLT-ACCESS-FAIL-CLOSED — رفض الطلب عند تعذر فحص الصلاحية

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-FAIL-CLOSED -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-005 | policy engine unavailable → 100 % fail-closed |
| فحص البنية | FIT-16 | Policy engine failure denies |
| المتطلب | REQ-FND-013 | If the policy decision point is unavailable or returns an error, then the system shall deny the request. |
<!-- END GENERATED: refs US-PLT-ACCESS-FAIL-CLOSED -->

</details>

### 5.6 US-PLT-ACCESS-OBLIGATIONS — تطبيق التزامات قرار الوصول

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-OBLIGATIONS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §3.4` | — |
| المتطلب | REQ-FND-012 | The system shall return a policy decision of ALLOW, DENY, CONDITIONAL, REDACT, AGGREGATE or REQUIRE_APPROVAL,… |
| حالة الاستخدام | UC-086 | Manage Access Policy |
<!-- END GENERATED: refs US-PLT-ACCESS-OBLIGATIONS -->

</details>

### 5.7 US-PLT-ACCESS-PDP-PERFORMANCE — قرار الصلاحية خلال خمسة أجزاء من الثانية

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-PDP-PERFORMANCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-009 | PEP requests a policy decision → p95 ≤ 5 ms with embedded evaluator; ≤ 20 ms remote |
| القرار التقني | TD-08 | Open Policy Agent: decision tables compiled to Rego; signed bundles; embedded evaluation (WASM/library) in ea… |
<!-- END GENERATED: refs US-PLT-ACCESS-PDP-PERFORMANCE -->

</details>

### 5.8 US-PLT-ACCESS-PEP-EVERY-PATH — فحص الصلاحية قبل أي استرجاع للبيانات

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-PEP-EVERY-PATH -->
| البند | المعرّف | المعنى |
|---|---|---|
| فحص البنية | FIT-03 | Every retrieval path passes a PEP before data access |
| فحص البنية | FIT-20 | Module-boundary rules (complements FIT-10): no contexts→contexts or services→services imports; platform holds no context ports or business types; migrations touch only their own schema; command handlers reach repositories and the PDP only through the command pipeline; contracts/ equals the contract generator's output |
| القرار المعماري | ADR-P17 | Internal Service Architecture (Hexagonal / Ports & Adapters) |
| المتطلب | REQ-FND-010 | The system shall evaluate authorization before retrieving data for every command, query, search, map request,… |
<!-- END GENERATED: refs US-PLT-ACCESS-PEP-EVERY-PATH -->

</details>

### 5.9 US-PLT-ACCESS-QUERY-PREFILTER — تصفية النتائج دون كشف المحجوب

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-QUERY-PREFILTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance → 0 leakage in inference suite (cou… |
| الجودة | QAS-SEC-011 | inference test suite on search, suggestions, facets, graph and paths → 0 disclosures of hidden objects, hidde… |
| القرار المعماري | ADR-P06 | Security Inside Projections |
| المصدر | `17-security-design.md §3.3` | — |
<!-- END GENERATED: refs US-PLT-ACCESS-QUERY-PREFILTER -->

</details>

### 5.10 US-PLT-ACCESS-SECURITY-CONTEXT — سياق أمني موقّع يرافق كل طلب

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-SECURITY-CONTEXT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §1.1` | — |
| المصدر | `17-security-design.md §2` | — |
<!-- END GENERATED: refs US-PLT-ACCESS-SECURITY-CONTEXT -->

</details>

### 5.11 US-PLT-ACCESS-SHARED-CACHE — منع مشاركة النتائج المخزنة بين المستخدمين

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-SHARED-CACHE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §9` | — |
| الجودة | QAS-SEC-004 | request the same map tile → 0 cross-scope cache hits |
| القرار المعماري | ADR-P06 | Security Inside Projections |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-ACCESS-SHARED-CACHE -->

</details>

### 5.12 US-PLT-ACCESS-STALE-BUNDLE — تقييد العمل عند تقادم حزمة السياسات

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-STALE-BUNDLE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/degradation-slc01.md §matrix` | — |
| المصدر | `23-crosscutting.md §6.2` | — |
<!-- END GENERATED: refs US-PLT-ACCESS-STALE-BUNDLE -->

</details>

### 5.13 US-PLT-ACCESS-UI-DENIALS — عرض الرفض دون كشف وجود المورد

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-UI-DENIALS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §6.2` | — |
| القرار المعماري | ADR-P19 | Handling of Authorization Outcomes (403 vs 404, MFA step-up, approval-required) |
| القرار المعماري | ADR-P06 | Security Inside Projections |
<!-- END GENERATED: refs US-PLT-ACCESS-UI-DENIALS -->

</details>

### 5.14 US-PLT-ACCESS-UI-LOCAL-STORAGE — منع حفظ البيانات الحساسة في المتصفح

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-UI-LOCAL-STORAGE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §6.1` | — |
| المصدر | `12-solution/ui-architecture.md` | — |
<!-- END GENERATED: refs US-PLT-ACCESS-UI-LOCAL-STORAGE -->

</details>

### 5.15 US-PLT-ACCESS-UI-NAVIGATION — إظهار مناطق الواجهة حسب صلاحيات المستخدم

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-UI-NAVIGATION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §3` | — |
| المصدر | `21-ui-design.md §6.3` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-ACCESS-UI-NAVIGATION -->

</details>

### 5.16 US-PLT-ACCESS-UI-REDACTION — علامة ثابتة للحقل المحجوب

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

<!-- BEGIN GENERATED: refs US-PLT-ACCESS-UI-REDACTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `21-ui-design.md §11` | — |
| القرار المعماري | ADR-P19 | Handling of Authorization Outcomes (403 vs 404, MFA step-up, approval-required) |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-PLT-ACCESS-UI-REDACTION -->

</details>

### 5.17 US-OPS-ACCESS-INFERENCE-SUITE — اختبار عدم الاستدلال واختبار الاختراق

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

<!-- BEGIN GENERATED: refs US-OPS-ACCESS-INFERENCE-SUITE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance → 0 leakage in inference suite (cou… |
| الجودة | QAS-SEC-011 | inference test suite on search, suggestions, facets, graph and paths → 0 disclosures of hidden objects, hidde… |
| المتطلب | REQ-FND-010 | The system shall evaluate authorization before retrieving data for every command, query, search, map request,… |
<!-- END GENERATED: refs US-OPS-ACCESS-INFERENCE-SUITE -->

</details>

### 5.18 US-OPS-ACCESS-MTLS-IDENTITY — اتصال مشفر بهوية خاصة لكل خدمة

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

<!-- BEGIN GENERATED: refs US-OPS-ACCESS-MTLS-IDENTITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `17-security-design.md §1` | — |
| المصدر | `22-deployment-design.md §3` | — |
<!-- END GENERATED: refs US-OPS-ACCESS-MTLS-IDENTITY -->

</details>

### 5.19 US-OPS-ACCESS-PDP-ALERTS — تنبيهات أداء محرك السياسات وقفزات الرفض

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

<!-- BEGIN GENERATED: refs US-OPS-ACCESS-PDP-ALERTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/observability-slc01.md §signals` | — |
<!-- END GENERATED: refs US-OPS-ACCESS-PDP-ALERTS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-FND-010 | The system shall evaluate authorization before retrieving data for every command, query, search, map request,… | `US-BC01-Q-SEC-CONTEXT`، `US-BC08-Q-PDP-DECIDE`، `US-OPS-ACCESS-INFERENCE-SUITE`، `US-PLT-ACCESS-PEP-EVERY-PATH` | TST-SLC01-INVARIANTS، TST-SLC05-INVARIANTS |
| REQ-FND-012 | The system shall return a policy decision of ALLOW, DENY, CONDITIONAL, REDACT, AGGREGATE or REQUIRE_APPROVAL,… | `US-PLT-ACCESS-OBLIGATIONS` | TST-POLICY-SET-SM |
| REQ-FND-013 | If the policy decision point is unavailable or returns an error, then the system shall deny the request. | `US-PLT-ACCESS-FAIL-CLOSED` | TST-SLC01-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
