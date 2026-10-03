---
id: FEAT-INF-EXTERNAL-IDS
type: feature
title: "ربط المعرّفات الخارجية"
status: DRAFT
version: "0.1"
capability: CAP-03.01
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# ربط المعرّفات الخارجية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-INF-EXTERNAL-IDS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-03 إدارة المعلومات |
| القدرة الفرعية | CAP-03.01 الكيانات والعلاقات (R1) |
| الأدوار | النظام؛ المحلل |
| الشاشات | SCR-65 المحوّلات والاتصالات والحساسات |
| حالات الاستخدام | — |
| القصص | 9: 3 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

تبقى السجلات الواردة من الأنظمة الخارجية مرتبطة بالعنصر الصحيح لدينا فلا تتكرر ولا تضيع.

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
| `US-BC02-EXT-END` | إنهاء ربط المعرّف الخارجي | أمر | مسودة |
| `US-BC02-EXT-MAP` | تسجيل ربط ربط المعرّف الخارجي | أمر | مسودة |
| `US-BC02-Q-EXT-RESOLVE` | جلب: Object URN mapped at time t (not-found shape if hidden) | جلب | مسودة |
| `US-UI-SCR65-EXTID-LOOKUP` | البحث عن عنصر بمعرّفه في نظام خارجي | واجهة | مسودة |
| `US-PLT-EXTID-UNIQUE-AT-TIME` | معرّف خارجي يشير لعنصر واحد في كل وقت | منصة | مسودة |
| `US-INT-EXTID-IMPORT-UPSERT` | ربط السجل الوارد بالعنصر الموجود دون تكرار | تكامل | مسودة |
| `US-INT-EXTID-MERGED-TARGET` | توجيه السجل الوارد لكيان مدموج إلى هويته الموحدة | تكامل | مسودة |
| `US-INT-EXTID-REASSIGNED` | معالجة إعادة استخدام المعرّف في النظام الخارجي | تكامل | مسودة |
| `US-OPS-EXTID-PROBE-LIMIT` | منع تخمين المعرّفات الخارجية لمعرفة الوجود | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC02-EXT-END — إنهاء ربط المعرّف الخارجي

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

<!-- BEGIN GENERATED: refs US-BC02-EXT-END -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/external-ids/{id}/actions/end` | — |
| الأمر | `CMD-EXT-END` | إنهاء ربط المعرّف الخارجي |
| السياسة | `POL-EXT-END` | adapter service account · Analyst؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-EXT-ENDED` | يصل إلى: Import worker cache |
| الكيان | `AGG-EXTERNAL-ID` | ربط المعرّف الخارجي |
| الجدول | `information.external_ids` | الجدول الرئيسي لربط المعرّف الخارجي |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-036 | The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type… |
| الاختبار | TST-EXTERNAL-ID-SM، TST-SLC02-INVARIANTS | دورة حالات ربط المعرّف الخارجي، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-EXT-END -->

</details>

### 5.2 US-BC02-EXT-MAP — تسجيل ربط ربط المعرّف الخارجي

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

<!-- BEGIN GENERATED: refs US-BC02-EXT-MAP -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/information/external-ids` | — |
| الأمر | `CMD-EXT-MAP` | تسجيل ربط ربط المعرّف الخارجي |
| السياسة | `POL-EXT-MAP` | adapter service account · Analyst؛ tenant match; object visible to subject (label ≤ clearance); write permiss… |
| الحدث | `EVT-EXT-MAPPED` | يصل إلى: Import worker cache |
| الكيان | `AGG-EXTERNAL-ID` | ربط المعرّف الخارجي |
| الجدول | `information.external_ids` | الجدول الرئيسي لربط المعرّف الخارجي |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-036 | The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type… |
| الاختبار | TST-EXTERNAL-ID-SM، TST-SLC02-INVARIANTS | دورة حالات ربط المعرّف الخارجي، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-EXT-MAP -->

</details>

### 5.3 US-BC02-Q-EXT-RESOLVE — جلب: Object URN mapped at time t (not-found shape if hidden)

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

<!-- BEGIN GENERATED: refs US-BC02-Q-EXT-RESOLVE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/information/external-ids/{system}/{external_id}` | — |
| الاستعلام | `QRY-EXT-RESOLVE` | Object URN mapped at time t (not-found shape if hidden) |
| السياسة | `POL-EXT-RESOLVE` | org scope ∩ classification rule; claims filtered by label |
| الكيان | `AGG-EXTERNAL-ID` | ربط المعرّف الخارجي |
| الجدول | `information.external_ids` | الجدول الرئيسي لربط المعرّف الخارجي |
| وحدة النشر | DU-04 | — |
| المتطلب | REQ-INF-036 | The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type… |
| الاختبار | TST-EXTERNAL-ID-SM، TST-SLC02-INVARIANTS | دورة حالات ربط المعرّف الخارجي، وثوابت الشريحة SLC-02 |
<!-- END GENERATED: refs US-BC02-Q-EXT-RESOLVE -->

</details>

### 5.4 US-UI-SCR65-EXTID-LOOKUP — البحث عن عنصر بمعرّفه في نظام خارجي

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

<!-- BEGIN GENERATED: refs US-UI-SCR65-EXTID-LOOKUP -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-65 | شاشة المحوّلات والاتصالات والحساسات |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-036 | The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type… |
<!-- END GENERATED: refs US-UI-SCR65-EXTID-LOOKUP -->

</details>

### 5.5 US-PLT-EXTID-UNIQUE-AT-TIME — معرّف خارجي يشير لعنصر واحد في كل وقت

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

<!-- BEGIN GENERATED: refs US-PLT-EXTID-UNIQUE-AT-TIME -->
| البند | المعرّف | المعنى |
|---|---|---|
| فحص البنية | FIT-07 | Identifiers are ULID + URN; no id rewrite on merge |
| القرار المعماري | ADR-P13 | Identifiers |
| المتطلب | REQ-INF-036 | The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type… |
<!-- END GENERATED: refs US-PLT-EXTID-UNIQUE-AT-TIME -->

</details>

### 5.6 US-INT-EXTID-IMPORT-UPSERT — ربط السجل الوارد بالعنصر الموجود دون تكرار

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-EXTID-IMPORT-UPSERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §3` | — |
| المتطلبات | REQ-INF-036، REQ-INF-005 | معانيها في القسم 6. التتبع |
| حالة الاستخدام | UC-094 | Ingest External Data |
<!-- END GENERATED: refs US-INT-EXTID-IMPORT-UPSERT -->

</details>

### 5.7 US-INT-EXTID-MERGED-TARGET — توجيه السجل الوارد لكيان مدموج إلى هويته الموحدة

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-EXTID-MERGED-TARGET -->
| البند | المعرّف | المعنى |
|---|---|---|
| القرار المعماري | ADR-P13 | Identifiers |
| المصدر | `20-integration-design.md §3` | — |
| المتطلب | REQ-INF-033 | When entities are matched, the system shall record a same-as link with the decision, reviewer and time, keep… |
| حالة الاستخدام | UC-007 | Resolve Entity |
<!-- END GENERATED: refs US-INT-EXTID-MERGED-TARGET -->

</details>

### 5.8 US-INT-EXTID-REASSIGNED — معالجة إعادة استخدام المعرّف في النظام الخارجي

| النوع | الإصدار | الأولوية | دون اتصال | الحالة |
|---|---|---|---|---|
| تكامل | R1 | Must | لا ينطبق | مسودة |

> **كـ** **[للكتابة]**، **أريد** **[للكتابة]**، **حتى** **[للكتابة]**.

**باختصار:** **[للكتابة]**

#### القواعد

**[للكتابة]**

#### معايير القبول

**[للكتابة]**

<details><summary>المراجع التقنية والتتبع</summary>

<!-- BEGIN GENERATED: refs US-INT-EXTID-REASSIGNED -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `20-integration-design.md §3` | — |
| المصدر | `[Derived]` | — |
| المتطلب | REQ-INF-036 | The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type… |
<!-- END GENERATED: refs US-INT-EXTID-REASSIGNED -->

</details>

### 5.9 US-OPS-EXTID-PROBE-LIMIT — منع تخمين المعرّفات الخارجية لمعرفة الوجود

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

<!-- BEGIN GENERATED: refs US-OPS-EXTID-PROBE-LIMIT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `THR-S02-09` | — |
<!-- END GENERATED: refs US-OPS-EXTID-PROBE-LIMIT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-INF-005 | The system shall ingest external data only through registered adapters or bulk import jobs that record source… | `US-INT-EXTID-IMPORT-UPSERT` | TST-ADAPTER-SM، TST-IMPORT-BATCH-SM، TST-SLC02-INVARIANTS |
| REQ-INF-033 | When entities are matched, the system shall record a same-as link with the decision, reviewer and time, keep… | `US-INT-EXTID-MERGED-TARGET` | TST-ER-CASE-SM، TST-SLC04-INVARIANTS |
| REQ-INF-036 | The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type… | `US-BC02-EXT-END`، `US-BC02-EXT-MAP`، `US-BC02-Q-EXT-RESOLVE`، `US-INT-EXTID-IMPORT-UPSERT`، `US-INT-EXTID-REASSIGNED`، `US-PLT-EXTID-UNIQUE-AT-TIME`، `US-UI-SCR65-EXTID-LOOKUP` | TST-ENTITY-SM، TST-EXTERNAL-ID-SM، TST-SLC02-INVARIANTS |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
