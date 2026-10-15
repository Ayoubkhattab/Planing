---
id: FEAT-PLT-MONITORING
type: feature
title: "مراقبة صحة المنصة"
status: DRAFT
version: "0.1"
capability: CAP-14.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# مراقبة صحة المنصة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-PLT-MONITORING |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-14 تشغيل المنصة |
| القدرة الفرعية | CAP-14.01 المراقبة (R1) |
| الأدوار | مشغّل المنصة |
| الشاشات | SCR-71 حالة الإسقاطات (واجهة المشغل) |
| حالات الاستخدام | — |
| القصص | 11: 0 من المواصفة، و11 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يمكّن مشغل المنصة من رؤية صحة كل مكونات المنصة وأدائها وتتبع أي طلب عبرها، ومتابعة مؤشرات نتائج الأعمال.

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
| QAS-AVL-001 | normal operation over a month | ≥ 99.9 % monthly |
| QAS-AVL-002 | normal operation over a month | ≥ 99.5 % monthly |
| QAS-AVL-003 | normal operation over a month | ≥ 99 % monthly |
| QAS-OBS-001 | investigates a failed request | 100 % of requests traceable end to end |
| QAS-PERF-001 | submits a state-changing command | p95 ≤ 300 ms; p99 ≤ 1 s |
| QAS-PERF-002 | reads a single object or a list page | single object p95 ≤ 300 ms; list page p95 ≤ 1 s |
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
| `US-PLT-MON-BUSINESS-TELEMETRY` | قياس مؤشرات نتائج الأعمال | منصة | مسودة |
| `US-PLT-MON-CORRELATION-TRACE` | تتبع أي طلب من بدايته إلى نهايته | منصة | مسودة |
| `US-PLT-MON-LOG-HYGIENE` | سجلات تقنية بلا بيانات شخصية | منصة | مسودة |
| `US-PLT-MON-TELEMETRY` | مقاييس وسجلات موحدة لكل مكوّن | منصة | مسودة |
| `US-OPS-MON-ALERT-SEVERITY` | تصنيف التنبيهات حسب الخطورة والاستدعاء | تشغيل | مسودة |
| `US-OPS-MON-CLOCK-SYNC` | مزامنة ساعات الخلية والتنبيه للانحراف | تشغيل | مسودة |
| `US-OPS-MON-DASHBOARDS` | لوحات صحة لكل وحدة نشر | تشغيل | مسودة |
| `US-OPS-MON-LATENCY-SLO` | تنبيه عند تجاوز أهداف زمن الاستجابة | تشغيل | مسودة |
| `US-OPS-MON-RETENTION` | احتفاظ محدود بالسجلات والتتبع والمقاييس | تشغيل | مسودة |
| `US-OPS-MON-SECURITY-INCIDENT` | الاستجابة للحوادث الأمنية الحرجة | تشغيل | مسودة |
| `US-OPS-MON-SLO-BUDGET` | متابعة أهداف التوفر وميزانية الخطأ | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-PLT-MON-BUSINESS-TELEMETRY — قياس مؤشرات نتائج الأعمال

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

<!-- BEGIN GENERATED: refs US-PLT-MON-BUSINESS-TELEMETRY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `09-reliability/observability-slc01.md §business_telemetry` | — |
| المتطلب | REQ-PLT-003 | The system shall emit metrics, logs and traces carrying a correlation id across every component, plus busines… |
<!-- END GENERATED: refs US-PLT-MON-BUSINESS-TELEMETRY -->

</details>

### 5.2 US-PLT-MON-CORRELATION-TRACE — تتبع أي طلب من بدايته إلى نهايته

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

<!-- BEGIN GENERATED: refs US-PLT-MON-CORRELATION-TRACE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-OBS-001 | investigates a failed request → 100 % of requests traceable end to end |
| المصدر | `23-crosscutting.md §7` | — |
| المتطلب | REQ-PLT-003 | The system shall emit metrics, logs and traces carrying a correlation id across every component, plus busines… |
<!-- END GENERATED: refs US-PLT-MON-CORRELATION-TRACE -->

</details>

### 5.3 US-PLT-MON-LOG-HYGIENE — سجلات تقنية بلا بيانات شخصية

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

<!-- BEGIN GENERATED: refs US-PLT-MON-LOG-HYGIENE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §7` | — |
| المصدر | `17-security-design.md §6` | — |
<!-- END GENERATED: refs US-PLT-MON-LOG-HYGIENE -->

</details>

### 5.4 US-PLT-MON-TELEMETRY — مقاييس وسجلات موحدة لكل مكوّن

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

<!-- BEGIN GENERATED: refs US-PLT-MON-TELEMETRY -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-14 | OpenTelemetry SDK + Collector; VictoriaMetrics (metrics), VictoriaLogs (logs), Jaeger (traces), Grafana dashb… |
| المصدر | `23-crosscutting.md §7` | — |
| المتطلب | REQ-PLT-003 | The system shall emit metrics, logs and traces carrying a correlation id across every component, plus busines… |
<!-- END GENERATED: refs US-PLT-MON-TELEMETRY -->

</details>

### 5.5 US-OPS-MON-ALERT-SEVERITY — تصنيف التنبيهات حسب الخطورة والاستدعاء

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

<!-- BEGIN GENERATED: refs US-OPS-MON-ALERT-SEVERITY -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §7` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-MON-ALERT-SEVERITY -->

</details>

### 5.6 US-OPS-MON-CLOCK-SYNC — مزامنة ساعات الخلية والتنبيه للانحراف

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

<!-- BEGIN GENERATED: refs US-OPS-MON-CLOCK-SYNC -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §4` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-MON-CLOCK-SYNC -->

</details>

### 5.7 US-OPS-MON-DASHBOARDS — لوحات صحة لكل وحدة نشر

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

<!-- BEGIN GENERATED: refs US-OPS-MON-DASHBOARDS -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار التقني | TD-14 | OpenTelemetry SDK + Collector; VictoriaMetrics (metrics), VictoriaLogs (logs), Jaeger (traces), Grafana dashb… |
| المصدر | `23-crosscutting.md §7` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-MON-DASHBOARDS -->

</details>

### 5.8 US-OPS-MON-LATENCY-SLO — تنبيه عند تجاوز أهداف زمن الاستجابة

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

<!-- BEGIN GENERATED: refs US-OPS-MON-LATENCY-SLO -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-PERF-001 | submits a state-changing command → p95 ≤ 300 ms; p99 ≤ 1 s |
| الجودة | QAS-PERF-002 | reads a single object or a list page → single object p95 ≤ 300 ms; list page p95 ≤ 1 s |
| المصدر | `21-ui-design.md §13` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-MON-LATENCY-SLO -->

</details>

### 5.9 US-OPS-MON-RETENTION — احتفاظ محدود بالسجلات والتتبع والمقاييس

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

<!-- BEGIN GENERATED: refs US-OPS-MON-RETENTION -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `22-deployment-design.md §11` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-MON-RETENTION -->

</details>

### 5.10 US-OPS-MON-SECURITY-INCIDENT — الاستجابة للحوادث الأمنية الحرجة

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

<!-- BEGIN GENERATED: refs US-OPS-MON-SECURITY-INCIDENT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md §7` | — |
| المصدر | `17-security-design.md §8` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-MON-SECURITY-INCIDENT -->

</details>

### 5.11 US-OPS-MON-SLO-BUDGET — متابعة أهداف التوفر وميزانية الخطأ

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

<!-- BEGIN GENERATED: refs US-OPS-MON-SLO-BUDGET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-AVL-001 | normal operation over a month → ≥ 99.9 % monthly |
| الجودة | QAS-AVL-002 | normal operation over a month → ≥ 99.5 % monthly |
| الجودة | QAS-AVL-003 | normal operation over a month → ≥ 99 % monthly |
| المصدر | `23-crosscutting.md §7` | — |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-OPS-MON-SLO-BUDGET -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-PLT-003 | The system shall emit metrics, logs and traces carrying a correlation id across every component, plus busines… | `US-PLT-MON-BUSINESS-TELEMETRY`، `US-PLT-MON-CORRELATION-TRACE`، `US-PLT-MON-TELEMETRY` | — |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
