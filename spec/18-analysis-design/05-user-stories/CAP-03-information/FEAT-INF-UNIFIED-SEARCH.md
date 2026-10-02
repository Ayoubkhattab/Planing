---
id: FEAT-INF-UNIFIED-SEARCH
type: feature
title: "البحث الموحد"
status: DRAFT
version: "0.1"
capability: CAP-03.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# البحث الموحد

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-UNIFIED-SEARCH |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.01 الكيانات والعلاقات (R1) |
| الأدوار | أي مستخدم مخوَّل |
| الشاشات | SCR-20 البحث الموحد |
| حالات الاستخدام | UC-097 |
| القصص | 12: 2 من المواصفة، و10 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يجد المستخدم ما يبحث عنه من كيانات وملاحظات ووثائق وخطط بالنص والمكان والزمن وبالعربية والإنجليزية دون كشف ما لا يحق له.

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
| QAS-PERF-003 | runs a combined text + spatial + temporal search | p95 ≤ 1 s |
| QAS-REL-002 | search projection unavailable | critical tier unaffected; index rebuilt without data loss |
| QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance | 0 leakage in inference suite (counts, facets, ordering, timing, errors) |
| QAS-SEC-003 | removes a user's compartment | effective on next request in every path, independent of index lag |
| QAS-SEC-011 | inference test suite on search, suggestions, facets, graph and paths | 0 disclosures of hidden objects, hidden facts, hidden nodes/edges |
| QAS-USA-002 | searches a name with Arabic spelling variants or Latin transliteration | recall ≥ 95 % on the Arabic name test set |
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
| `US-BC07-Q-SRCH-QUERY` | جلب: Unified search: text + types + polygon/bbox + time window + filters + facets; cursor paging; results and facets over visible facts only | جلب | مسودة |
| `US-BC07-Q-SRCH-SUGGEST` | جلب: Autocomplete from visible facts only | جلب | مسودة |
| `US-UI-SCR20-SEARCH-DEGRADED` | إبلاغ المستخدم حين يكون البحث جزئيًا أو متوقفًا | واجهة | مسودة |
| `US-UI-SCR20-SEARCH-GEO-TIME` | تقييد البحث بمضلع على الخريطة ونافذة زمنية | واجهة | مسودة |
| `US-UI-SCR20-SEARCH-RESULTS` | عرض نتائج البحث مجمعة بالنوع مع الأوجه | واجهة | مسودة |
| `US-PLT-SEARCH-ALL-TYPES` | شمول البحث الخطط والتقييمات والوثائق | منصة | مسودة |
| `US-PLT-SEARCH-ARABIC-MATCH` | مطابقة الأسماء العربية بصيغها ونقحرتها | منصة | مسودة |
| `US-PLT-SEARCH-COMBINED-PERF` | بحث مركب بالنص والمكان والزمن خلال ثانية | منصة | مسودة |
| `US-PLT-SEARCH-NO-INFERENCE` | ألا يكشف البحث المحجوب بالعدد أو التوقيت | منصة | مسودة |
| `US-PLT-SEARCH-REVOCATION-RECHECK` | نفاذ سحب الصلاحية في البحث رغم تأخر الفهرس | منصة | مسودة |
| `US-OPS-SEARCH-HEALTH-WATCH` | مراقبة زمن البحث ونسبة النتائج المسقطة | تشغيل | مسودة |
| `US-OPS-SEARCH-INFERENCE-SUITE` | تشغيل اختبار منع الاستدلال دوريًا مع تنبيه فوري | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-Q-SRCH-QUERY — جلب: Unified search: text + types + polygon/bbox + time window + filters + facets; cursor paging; results and facets over visible facts only

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

<!-- BEGIN GENERATED: refs US-BC07-Q-SRCH-QUERY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/discovery/search-queries` | — |
| الاستعلام | `QRY-SRCH-QUERY` | Unified search: text + types + polygon/bbox + time window + filters + facets; cursor paging; results and face… |
| السياسة | `POL-SRCH-QUERY` | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page |
| المتطلب | REQ-SRC-001 | The system shall provide unified search across entities, observations, documents, assessments, plans and task… |
| حالة الاستخدام | UC-097 | Search Authorized Information |
<!-- END GENERATED: refs US-BC07-Q-SRCH-QUERY -->

</details>

### 5.2 US-BC07-Q-SRCH-SUGGEST — جلب: Autocomplete from visible facts only

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

<!-- BEGIN GENERATED: refs US-BC07-Q-SRCH-SUGGEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/discovery/suggestions` | — |
| الاستعلام | `QRY-SRCH-SUGGEST` | Autocomplete from visible facts only |
| السياسة | `POL-SRCH-SUGGEST` | PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page |
| المتطلب | REQ-SRC-003 | The system shall match Arabic text regardless of hamza forms, alef maqsura, taa marbuta, diacritics and tatwe… |
| حالة الاستخدام | UC-097 | Search Authorized Information |
<!-- END GENERATED: refs US-BC07-Q-SRCH-SUGGEST -->

</details>

### 5.3 US-UI-SCR20-SEARCH-DEGRADED — إبلاغ المستخدم حين يكون البحث جزئيًا أو متوقفًا

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

<!-- BEGIN GENERATED: refs US-UI-SCR20-SEARCH-DEGRADED -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-20 | شاشة البحث الموحد |
| الجودة | QAS-REL-002 | search projection unavailable → critical tier unaffected; index rebuilt without data loss |
| المصدر | `FM-S05-02` | — |
| المصدر | `FM-S05-03` | — |
| المصدر | `discovery-architecture.md §7` | — |
<!-- END GENERATED: refs US-UI-SCR20-SEARCH-DEGRADED -->

</details>

### 5.4 US-UI-SCR20-SEARCH-GEO-TIME — تقييد البحث بمضلع على الخريطة ونافذة زمنية

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

<!-- BEGIN GENERATED: refs US-UI-SCR20-SEARCH-GEO-TIME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-20 | شاشة البحث الموحد |
| المتطلب | REQ-SRC-001 | The system shall provide unified search across entities, observations, documents, assessments, plans and task… |
| حالة الاستخدام | UC-097 | Search Authorized Information |
<!-- END GENERATED: refs US-UI-SCR20-SEARCH-GEO-TIME -->

</details>

### 5.5 US-UI-SCR20-SEARCH-RESULTS — عرض نتائج البحث مجمعة بالنوع مع الأوجه

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

<!-- BEGIN GENERATED: refs US-UI-SCR20-SEARCH-RESULTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-20 | شاشة البحث الموحد |
| حالة الاستخدام | UC-097 | Search Authorized Information |
| المصدر | `discovery-architecture.md §4.1` | — |
| المصدر | `21-ui-design.md §6.1` | — |
<!-- END GENERATED: refs US-UI-SCR20-SEARCH-RESULTS -->

</details>

### 5.6 US-PLT-SEARCH-ALL-TYPES — شمول البحث الخطط والتقييمات والوثائق

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

<!-- BEGIN GENERATED: refs US-PLT-SEARCH-ALL-TYPES -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `discovery-architecture.md §3.1` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-SRC-001 | The system shall provide unified search across entities, observations, documents, assessments, plans and task… |
| حالة الاستخدام | UC-097 | Search Authorized Information |
<!-- END GENERATED: refs US-PLT-SEARCH-ALL-TYPES -->

</details>

### 5.7 US-PLT-SEARCH-ARABIC-MATCH — مطابقة الأسماء العربية بصيغها ونقحرتها

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

<!-- BEGIN GENERATED: refs US-PLT-SEARCH-ARABIC-MATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-USA-002 | searches a name with Arabic spelling variants or Latin transliteration → recall ≥ 95 % on the Arabic name tes… |
| المصدر | `language-model.md §4` | — |
| المصدر | `discovery-architecture.md §5` | — |
| المتطلب | REQ-SRC-003 | The system shall match Arabic text regardless of hamza forms, alef maqsura, taa marbuta, diacritics and tatwe… |
| حالة الاستخدام | UC-097 | Search Authorized Information |
<!-- END GENERATED: refs US-PLT-SEARCH-ARABIC-MATCH -->

</details>

### 5.8 US-PLT-SEARCH-COMBINED-PERF — بحث مركب بالنص والمكان والزمن خلال ثانية

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

<!-- BEGIN GENERATED: refs US-PLT-SEARCH-COMBINED-PERF -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-003 | runs a combined text + spatial + temporal search → p95 ≤ 1 s |
| القرار التقني | TD-02 | OpenSearch (Apache 2.0) — nested fact documents, Arabic analyzer + custom char filters (N1–N8), geo, index al… |
| المصدر | `discovery-architecture.md §8` | — |
| المتطلب | REQ-SRC-001 | The system shall provide unified search across entities, observations, documents, assessments, plans and task… |
| حالة الاستخدام | UC-097 | Search Authorized Information |
<!-- END GENERATED: refs US-PLT-SEARCH-COMBINED-PERF -->

</details>

### 5.9 US-PLT-SEARCH-NO-INFERENCE — ألا يكشف البحث المحجوب بالعدد أو التوقيت

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

<!-- BEGIN GENERATED: refs US-PLT-SEARCH-NO-INFERENCE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-002 | searches, lists, maps or receives alerts touching objects above clearance → 0 leakage in inference suite (cou… |
| الجودة | QAS-SEC-011 | inference test suite on search, suggestions, facets, graph and paths → 0 disclosures of hidden objects, hidde… |
| المصدر | `THR-S05-02` | — |
| المصدر | `THR-S05-03` | — |
| المصدر | `THR-S05-06` | — |
| المصدر | `THR-S05-08` | — |
| المتطلب | REQ-SRC-002 | The system shall not reveal the existence of unauthorized objects through search results, counts, facets, sug… |
| حالة الاستخدام | UC-097 | Search Authorized Information |
<!-- END GENERATED: refs US-PLT-SEARCH-NO-INFERENCE -->

</details>

### 5.10 US-PLT-SEARCH-REVOCATION-RECHECK — نفاذ سحب الصلاحية في البحث رغم تأخر الفهرس

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

<!-- BEGIN GENERATED: refs US-PLT-SEARCH-REVOCATION-RECHECK -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-SEC-003 | removes a user's compartment → effective on next request in every path, independent of index lag |
| المصدر | `THR-S05-05` | — |
| المصدر | `discovery-architecture.md §4.1` | — |
<!-- END GENERATED: refs US-PLT-SEARCH-REVOCATION-RECHECK -->

</details>

### 5.11 US-OPS-SEARCH-HEALTH-WATCH — مراقبة زمن البحث ونسبة النتائج المسقطة

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

<!-- BEGIN GENERATED: refs US-OPS-SEARCH-HEALTH-WATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc05.md` | — |
| المصدر | `FM-S05-03` | — |
<!-- END GENERATED: refs US-OPS-SEARCH-HEALTH-WATCH -->

</details>

### 5.12 US-OPS-SEARCH-INFERENCE-SUITE — تشغيل اختبار منع الاستدلال دوريًا مع تنبيه فوري

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

<!-- BEGIN GENERATED: refs US-OPS-SEARCH-INFERENCE-SUITE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc05.md` | — |
| الجودة | QAS-SEC-011 | inference test suite on search, suggestions, facets, graph and paths → 0 disclosures of hidden objects, hidde… |
| المتطلب | REQ-SRC-002 | The system shall not reveal the existence of unauthorized objects through search results, counts, facets, sug… |
| حالة الاستخدام | UC-097 | Search Authorized Information |
<!-- END GENERATED: refs US-OPS-SEARCH-INFERENCE-SUITE -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-SRC-001 | The system shall provide unified search across entities, observations, documents, assessments, plans and task… | `US-BC07-Q-SRCH-QUERY`، `US-PLT-SEARCH-ALL-TYPES`، `US-PLT-SEARCH-COMBINED-PERF`، `US-UI-SCR20-SEARCH-GEO-TIME` | TST-SLC05-INVARIANTS |
| REQ-SRC-002 | The system shall not reveal the existence of unauthorized objects through search results, counts, facets, sug… | `US-OPS-SEARCH-INFERENCE-SUITE`، `US-PLT-SEARCH-NO-INFERENCE` | TST-SLC05-INVARIANTS |
| REQ-SRC-003 | The system shall match Arabic text regardless of hamza forms, alef maqsura, taa marbuta, diacritics and tatwe… | `US-BC07-Q-SRCH-SUGGEST`، `US-PLT-SEARCH-ARABIC-MATCH` | TST-MATCH-RULESET-SM، TST-SLC04-INVARIANTS، TST-SLC05-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
