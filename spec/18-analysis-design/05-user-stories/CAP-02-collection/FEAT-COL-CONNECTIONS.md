---
id: FEAT-COL-CONNECTIONS
type: feature
title: "اتصالات الأنظمة الخارجية"
status: DRAFT
version: "0.1"
capability: CAP-02.04
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# اتصالات الأنظمة الخارجية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-CONNECTIONS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.04 الاستيعاب والتكامل (R1) |
| الأدوار | مهندس التكامل؛ مسؤول الأمن؛ مسؤول الإدارة؛ النظام |
| الشاشات | SCR-65 المحوّلات والاتصالات والحساسات |
| حالات الاستخدام | UC-094 |
| القصص | 15: 10 من المواصفة، و5 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يتيح لمهندس التكامل تسجيل الاتصال بالأنظمة الخارجية واختباره ومراقبة سلامته مع اعتماد أمني قبل تشغيله.

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
| QAS-INT-001 | ERP adapter outage 4 h | no data loss; backlog processed ≤ 1 h after recovery |
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
| `US-BC07-CON-ACTIVATE` | تفعيل اتصال التكامل | أمر | مسودة |
| `US-BC07-CON-FAIL-TEST` | تسجيل فشل اختبار اتصال التكامل | أمر | مسودة |
| `US-BC07-CON-REGISTER` | تسجيل اتصال التكامل | أمر | مسودة |
| `US-BC07-CON-RESUME` | استئناف اتصال التكامل | أمر | مسودة |
| `US-BC07-CON-RETIRE` | إحالة اتصال التكامل إلى التقاعد | أمر | مسودة |
| `US-BC07-CON-SUSPEND` | تعليق اتصال التكامل | أمر | مسودة |
| `US-BC07-CON-TEST` | اختبار اتصال التكامل | أمر | مسودة |
| `US-BC07-Q-CON-LIST` | جلب: Connections with state, health, allow-list entry | جلب | مسودة |
| `US-BC07-S-INTEGRATION-CONNECTION-01` | تلقائي: health checks failing 5 min (اتصال التكامل) | نظام | مسودة |
| `US-BC07-S-INTEGRATION-CONNECTION-02` | تلقائي: health restored (اتصال التكامل) | نظام | مسودة |
| `US-UI-SCR65-CONNECTION-HEALTH` | متابعة سلامة الاتصالات وتراكمها | واجهة | مسودة |
| `US-INT-CONN-BACKLOG-REPLAY` | استعادة التراكم بلا فقد بعد انقطاع النظام | تكامل | مسودة |
| `US-OPS-CONN-BACKLOG-ALERT` | التنبيه عند تقادم تراكم الاتصال | تشغيل | مسودة |
| `US-OPS-CONN-EGRESS-RULE` | تطبيق قاعدة السماح لكل اتصال في بوابة الخروج | تشغيل | مسودة |
| `US-OPS-CONN-SECRETS` | حفظ بيانات اعتماد الاتصالات في الخزنة فقط | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-CON-ACTIVATE — تفعيل اتصال التكامل

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

<!-- BEGIN GENERATED: refs US-BC07-CON-ACTIVATE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/connections/{id}/actions/activate` | — |
| الأمر | `CMD-CON-ACTIVATE` | تفعيل اتصال التكامل |
| السياسة | `POL-CON-ACTIVATE` | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, res… |
| الحدث | `EVT-CON-ACTIVATED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-INTEGRATION-CONNECTION` | اتصال التكامل |
| الجدول | `integration.integration_connections` | الجدول الرئيسي لاتصال التكامل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS | دورة حالات اتصال التكامل، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-CON-ACTIVATE -->

</details>

### 5.2 US-BC07-CON-FAIL-TEST — تسجيل فشل اختبار اتصال التكامل

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

<!-- BEGIN GENERATED: refs US-BC07-CON-FAIL-TEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/connections/{id}/actions/fail-test` | — |
| الأمر | `CMD-CON-FAIL-TEST` | تسجيل فشل اختبار اتصال التكامل |
| السياسة | `POL-CON-FAIL-TEST` | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, res… |
| الحدث | `EVT-CON-TEST-FAILED` | يصل إلى: Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| الكيان | `AGG-INTEGRATION-CONNECTION` | اتصال التكامل |
| الجدول | `integration.integration_connections` | الجدول الرئيسي لاتصال التكامل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS | دورة حالات اتصال التكامل، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-CON-FAIL-TEST -->

</details>

### 5.3 US-BC07-CON-REGISTER — تسجيل اتصال التكامل

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

<!-- BEGIN GENERATED: refs US-BC07-CON-REGISTER -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/connections` | — |
| الأمر | `CMD-CON-REGISTER` | تسجيل اتصال التكامل |
| السياسة | `POL-CON-REGISTER` | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, res… |
| الحدث | `EVT-CON-REGISTERED` | يصل إلى: Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| الكيان | `AGG-INTEGRATION-CONNECTION` | اتصال التكامل |
| الجدول | `integration.integration_connections` | الجدول الرئيسي لاتصال التكامل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS | دورة حالات اتصال التكامل، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-CON-REGISTER -->

</details>

### 5.4 US-BC07-CON-RESUME — استئناف اتصال التكامل

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

<!-- BEGIN GENERATED: refs US-BC07-CON-RESUME -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/connections/{id}/actions/resume` | — |
| الأمر | `CMD-CON-RESUME` | استئناف اتصال التكامل |
| السياسة | `POL-CON-RESUME` | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, res… |
| الحدث | `EVT-CON-RESUMED` | يصل إلى: Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| الكيان | `AGG-INTEGRATION-CONNECTION` | اتصال التكامل |
| الجدول | `integration.integration_connections` | الجدول الرئيسي لاتصال التكامل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS | دورة حالات اتصال التكامل، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-CON-RESUME -->

</details>

### 5.5 US-BC07-CON-RETIRE — إحالة اتصال التكامل إلى التقاعد

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

<!-- BEGIN GENERATED: refs US-BC07-CON-RETIRE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/connections/{id}/actions/retire` | — |
| الأمر | `CMD-CON-RETIRE` | إحالة اتصال التكامل إلى التقاعد |
| السياسة | `POL-CON-RETIRE` | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, res… |
| الحدث | `EVT-CON-RETIRED` | يصل إلى: Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| الكيان | `AGG-INTEGRATION-CONNECTION` | اتصال التكامل |
| الجدول | `integration.integration_connections` | الجدول الرئيسي لاتصال التكامل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS | دورة حالات اتصال التكامل، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-CON-RETIRE -->

</details>

### 5.6 US-BC07-CON-SUSPEND — تعليق اتصال التكامل

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

<!-- BEGIN GENERATED: refs US-BC07-CON-SUSPEND -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/connections/{id}/actions/suspend` | — |
| الأمر | `CMD-CON-SUSPEND` | تعليق اتصال التكامل |
| السياسة | `POL-CON-SUSPEND` | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, res… |
| الحدث | `EVT-CON-SUSPENDED` | يصل إلى: Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-ver… |
| الكيان | `AGG-INTEGRATION-CONNECTION` | اتصال التكامل |
| الجدول | `integration.integration_connections` | الجدول الرئيسي لاتصال التكامل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS | دورة حالات اتصال التكامل، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-CON-SUSPEND -->

</details>

### 5.7 US-BC07-CON-TEST — اختبار اتصال التكامل

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

<!-- BEGIN GENERATED: refs US-BC07-CON-TEST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/integration/connections/{id}/actions/test` | — |
| الأمر | `CMD-CON-TEST` | اختبار اتصال التكامل |
| السياسة | `POL-CON-TEST` | integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, res… |
| الحدث | `EVT-CON-TEST-STARTED` | يصل إلى: Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| الكيان | `AGG-INTEGRATION-CONNECTION` | اتصال التكامل |
| الجدول | `integration.integration_connections` | الجدول الرئيسي لاتصال التكامل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS | دورة حالات اتصال التكامل، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-CON-TEST -->

</details>

### 5.8 US-BC07-Q-CON-LIST — جلب: Connections with state, health, allow-list entry

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

<!-- BEGIN GENERATED: refs US-BC07-Q-CON-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/integration/connections` | — |
| الاستعلام | `QRY-CON-LIST` | Connections with state, health, allow-list entry |
| السياسة | `POL-CON-LIST` | integration engineers, Security Officer |
| الكيان | `AGG-INTEGRATION-CONNECTION` | اتصال التكامل |
| الجدول | `integration.integration_connections` | الجدول الرئيسي لاتصال التكامل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS | دورة حالات اتصال التكامل، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-Q-CON-LIST -->

</details>

### 5.9 US-BC07-S-INTEGRATION-CONNECTION-01 — تلقائي: health checks failing 5 min (اتصال التكامل)

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

<!-- BEGIN GENERATED: refs US-BC07-S-INTEGRATION-CONNECTION-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:health checks failing 5 min` | backlog buffered by adapters (QAS-INT-001) |
| الانتقال | ACTIVE ← DEGRADED | — |
| الحدث | `EVT-CON-DEGRADED` | يصل إلى: Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| الكيان | `AGG-INTEGRATION-CONNECTION` | اتصال التكامل |
| الجدول | `integration.integration_connections` | الجدول الرئيسي لاتصال التكامل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS | دورة حالات اتصال التكامل، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-S-INTEGRATION-CONNECTION-01 -->

</details>

### 5.10 US-BC07-S-INTEGRATION-CONNECTION-02 — تلقائي: health restored (اتصال التكامل)

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

<!-- BEGIN GENERATED: refs US-BC07-S-INTEGRATION-CONNECTION-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:health restored` | backlog replayed |
| الانتقال | DEGRADED ← ACTIVE | — |
| الحدث | `EVT-CON-RECOVERED` | يصل إلى: Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| الكيان | `AGG-INTEGRATION-CONNECTION` | اتصال التكامل |
| الجدول | `integration.integration_connections` | الجدول الرئيسي لاتصال التكامل |
| وحدة النشر | DU-11 | — |
| المتطلب | REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… |
| حالة الاستخدام | UC-094 | Ingest External Data |
| الاختبار | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS | دورة حالات اتصال التكامل، وثوابت الشريحة SLC-16 |
<!-- END GENERATED: refs US-BC07-S-INTEGRATION-CONNECTION-02 -->

</details>

### 5.11 US-UI-SCR65-CONNECTION-HEALTH — متابعة سلامة الاتصالات وتراكمها

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

<!-- BEGIN GENERATED: refs US-UI-SCR65-CONNECTION-HEALTH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-65 | شاشة المحوّلات والاتصالات والحساسات |
| المصدر | `QRY-CON-LIST` | — |
| المصدر | `21-ui-design.md §6.3` | — |
<!-- END GENERATED: refs US-UI-SCR65-CONNECTION-HEALTH -->

</details>

### 5.12 US-INT-CONN-BACKLOG-REPLAY — استعادة التراكم بلا فقد بعد انقطاع النظام

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Should | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-CONN-BACKLOG-REPLAY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-INT-001 | ERP adapter outage 4 h → no data loss; backlog processed ≤ 1 h after recovery |
| المصدر | `FM-S16-01` | — |
| المصدر | `enterprise-integration-spec.md §3` | — |
| المصدر | `20-integration-design.md §3` | — |
<!-- END GENERATED: refs US-INT-CONN-BACKLOG-REPLAY -->

</details>

### 5.13 US-OPS-CONN-BACKLOG-ALERT — التنبيه عند تقادم تراكم الاتصال

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

<!-- BEGIN GENERATED: refs US-OPS-CONN-BACKLOG-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc16.md` | — |
| الجودة | QAS-INT-001 | ERP adapter outage 4 h → no data loss; backlog processed ≤ 1 h after recovery |
<!-- END GENERATED: refs US-OPS-CONN-BACKLOG-ALERT -->

</details>

### 5.14 US-OPS-CONN-EGRESS-RULE — تطبيق قاعدة السماح لكل اتصال في بوابة الخروج

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

<!-- BEGIN GENERATED: refs US-OPS-CONN-EGRESS-RULE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `enterprise-integration-spec.md §5` | — |
| المصدر | `INV-CON-01` | — |
| المصدر | `THR-S16-04` | — |
| المصدر | `17-security-design.md §8` | — |
<!-- END GENERATED: refs US-OPS-CONN-EGRESS-RULE -->

</details>

### 5.15 US-OPS-CONN-SECRETS — حفظ بيانات اعتماد الاتصالات في الخزنة فقط

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

<!-- BEGIN GENERATED: refs US-OPS-CONN-SECRETS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `INV-CON-03` | — |
| القرار التقني | TD-07 | OpenBao (MPL, open fork of Vault) Transit engine for envelope encryption; KEKs in site HSM via PKCS#11; DEKs… |
<!-- END GENERATED: refs US-OPS-CONN-SECRETS -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,… | كل قصص الميزة المأخوذة من المواصفة (10) | TST-INTEGRATION-CONNECTION-SM، TST-SLC16-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
