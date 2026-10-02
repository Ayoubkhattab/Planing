---
id: FEAT-COL-FIELD-SYNC
type: feature
title: "المزامنة الميدانية"
status: DRAFT
version: "0.1"
capability: CAP-02.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# المزامنة الميدانية

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-FIELD-SYNC |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) |
| الأدوار | المستخدم الميداني؛ النظام |
| الشاشات | SCR-01 مهامي |
| حالات الاستخدام | UC-090، UC-091 |
| القصص | 12: 6 من المواصفة، و6 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

ينقل ما سجله المستخدم الميداني دون اتصال إلى الخادم بترتيبه الأصلي دون تكرار ويجلب له آخر تحديثات مهامه.

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
| QAS-OFF-001 | works 72 h offline then reconnects on a 1 Mbps link | 1,000 queued commands synced ≤ 10 min; 0 silent overwrites; 0 duplicates |
| QAS-OFF-003 | 5,000 devices reconnect within 10 min | all sessions complete ≤ 30 min; oldest-offline devices first; no data loss |
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
| `US-BC07-SYN-OPEN` | فتح جلسة المزامنة | أمر | مسودة |
| `US-BC07-SYN-UPLOAD-BATCH` | رفع دفعة إلى جلسة المزامنة | أمر | مسودة |
| `US-BC07-Q-SYN-DELTA` | جلب: Server → device: my task changes, package updates, purge list, conflict notices, wipe/stop instruction | جلب | مسودة |
| `US-BC07-S-SYNC-SESSION-02` | تلقائي: all uploaded commands processed without conflict (جلسة المزامنة) | نظام | مسودة |
| `US-BC07-S-SYNC-SESSION-03` | تلقائي: all processed with ≥ 1 sync conflict (جلسة المزامنة) | نظام | مسودة |
| `US-BC07-S-SYNC-SESSION-04` | تلقائي: idle timeout (5 min) or transport loss (جلسة المزامنة) | نظام | مسودة |
| `US-UI-SCR01-SYNC-DETAILS` | شاشة المزامنة وتقدمها وما بقي معلقًا | واجهة | مسودة |
| `US-PLT-SYNC-GATEWAY-SCALE` | استيعاب عودة آلاف الأجهزة معًا | منصة | مسودة |
| `US-PLT-SYNC-IDEMPOTENCY-STORE` | عدم تكرار الأوامر مهما انقطعت المزامنة | منصة | مسودة |
| `US-PLT-SYNC-THROUGHPUT` | مزامنة ألف أمر خلال عشر دقائق | منصة | مسودة |
| `US-OPS-SYNC-HEALTH-ALERTS` | مراقبة زمن المزامنة وانحراف ساعات الأجهزة | تشغيل | مسودة |
| `US-OPS-SYNC-SIGNATURE-INCIDENT` | معاملة فشل توقيع الأوامر كحادث أمني | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-SYN-OPEN — فتح جلسة المزامنة

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

<!-- BEGIN GENERATED: refs US-BC07-SYN-OPEN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/field/sync-sessions` | — |
| الأمر | `CMD-SYN-OPEN` | فتح جلسة المزامنة |
| السياسة | `POL-SYN-OPEN` | field device + user (open, upload)؛ tenant match; device ACTIVE where applicable; device signature for SYN |
| الحدث | `EVT-SYN-OPENED` | يصل إلى: Owner contexts (commands applied via their APIs); Field telemetry |
| الكيان | `AGG-SYNC-SESSION` | جلسة المزامنة |
| الجدول | `field.sync_sessions` | الجدول الرئيسي لجلسة المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-001، REQ-OFF-003، REQ-OFF-004، REQ-OFF-006 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-091 | Capture Observation Offline؛ Synchronize Field Device |
| الاختبار | TST-SYNC-SESSION-SM، TST-SLC11-INVARIANTS | دورة حالات جلسة المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-SYN-OPEN -->

</details>

### 5.2 US-BC07-SYN-UPLOAD-BATCH — رفع دفعة إلى جلسة المزامنة

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

<!-- BEGIN GENERATED: refs US-BC07-SYN-UPLOAD-BATCH -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/field/sync-sessions/{id}/actions/upload-batch` | — |
| الأمر | `CMD-SYN-UPLOAD-BATCH` | رفع دفعة إلى جلسة المزامنة |
| السياسة | `POL-SYN-UPLOAD-BATCH` | field device + user (open, upload)؛ tenant match; device ACTIVE where applicable; device signature for SYN |
| الحدث | `EVT-SYN-BATCH-RECEIVED` | يصل إلى: Owner contexts (commands applied via their APIs); Field telemetry |
| الكيان | `AGG-SYNC-SESSION` | جلسة المزامنة |
| الجدول | `field.sync_sessions` | الجدول الرئيسي لجلسة المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-001، REQ-OFF-003، REQ-OFF-004، REQ-OFF-006 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-091 | Capture Observation Offline؛ Synchronize Field Device |
| الاختبار | TST-SYNC-SESSION-SM، TST-SLC11-INVARIANTS | دورة حالات جلسة المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-SYN-UPLOAD-BATCH -->

</details>

### 5.3 US-BC07-Q-SYN-DELTA — جلب: Server → device: my task changes, package updates, purge list, conflict notices, wipe/stop instruction

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

<!-- BEGIN GENERATED: refs US-BC07-Q-SYN-DELTA -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/field/sync-sessions/{session_id}/delta` | — |
| الاستعلام | `QRY-SYN-DELTA` | Server → device: my task changes, package updates, purge list, conflict notices, wipe/stop instruction |
| السياسة | `POL-SYN-DELTA` | device + user of the session |
| الكيان | `AGG-SYNC-SESSION` | جلسة المزامنة |
| الجدول | `field.sync_sessions` | الجدول الرئيسي لجلسة المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلب | REQ-OFF-001 | Where the mobile field application is used, the system shall allow recording observations with location, time… |
| حالة الاستخدام | UC-090 | Capture Observation Offline |
| الاختبار | TST-SYNC-SESSION-SM، TST-SLC11-INVARIANTS | دورة حالات جلسة المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-Q-SYN-DELTA -->

</details>

### 5.4 US-BC07-S-SYNC-SESSION-02 — تلقائي: all uploaded commands processed without conflict (جلسة المزامنة)

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

<!-- BEGIN GENERATED: refs US-BC07-S-SYNC-SESSION-02 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:all uploaded commands processed without conflict` | device declared end of queue; every command applied or idempotently recognized |
| الانتقال | APPLYING ← COMPLETED | — |
| الحدث | `EVT-SYN-COMPLETED` | يصل إلى: Owner contexts (commands applied via their APIs); Field telemetry |
| الكيان | `AGG-SYNC-SESSION` | جلسة المزامنة |
| الجدول | `field.sync_sessions` | الجدول الرئيسي لجلسة المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-001، REQ-OFF-003، REQ-OFF-004، REQ-OFF-006 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-091 | Capture Observation Offline؛ Synchronize Field Device |
| الاختبار | TST-SYNC-SESSION-SM، TST-SLC11-INVARIANTS | دورة حالات جلسة المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-S-SYNC-SESSION-02 -->

</details>

### 5.5 US-BC07-S-SYNC-SESSION-03 — تلقائي: all processed with ≥ 1 sync conflict (جلسة المزامنة)

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

<!-- BEGIN GENERATED: refs US-BC07-S-SYNC-SESSION-03 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:all processed with ≥ 1 sync conflict` | conflicts opened as AGG-SYNC-CONFLICT |
| الانتقال | APPLYING ← COMPLETED_WITH_CONFLICTS | — |
| الحدث | `EVT-SYN-COMPLETED-WITH-CONFLICTS` | يصل إلى: Owner contexts (commands applied via their APIs); Field telemetry |
| الكيان | `AGG-SYNC-SESSION` | جلسة المزامنة |
| الجدول | `field.sync_sessions` | الجدول الرئيسي لجلسة المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-001، REQ-OFF-003، REQ-OFF-004، REQ-OFF-006 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-091 | Capture Observation Offline؛ Synchronize Field Device |
| الاختبار | TST-SYNC-SESSION-SM، TST-SLC11-INVARIANTS | دورة حالات جلسة المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-S-SYNC-SESSION-03 -->

</details>

### 5.6 US-BC07-S-SYNC-SESSION-04 — تلقائي: idle timeout (5 min) or transport loss (جلسة المزامنة)

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

<!-- BEGIN GENERATED: refs US-BC07-S-SYNC-SESSION-04 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:idle timeout (5 min) or transport loss` | acknowledged seq retained; next session resumes (REQ-OFF-006) |
| الانتقال | OPEN, APPLYING ← FAILED | — |
| الحدث | `EVT-SYN-FAILED` | يصل إلى: Owner contexts (commands applied via their APIs); Field telemetry |
| الكيان | `AGG-SYNC-SESSION` | جلسة المزامنة |
| الجدول | `field.sync_sessions` | الجدول الرئيسي لجلسة المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلبات | REQ-OFF-001، REQ-OFF-003، REQ-OFF-004، REQ-OFF-006 | معانيها في القسم 6. التتبع |
| حالات الاستخدام | UC-090، UC-091 | Capture Observation Offline؛ Synchronize Field Device |
| الاختبار | TST-SYNC-SESSION-SM، TST-SLC11-INVARIANTS | دورة حالات جلسة المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-S-SYNC-SESSION-04 -->

</details>

### 5.7 US-UI-SCR01-SYNC-DETAILS — شاشة المزامنة وتقدمها وما بقي معلقًا

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

<!-- BEGIN GENERATED: refs US-UI-SCR01-SYNC-DETAILS -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-01 | شاشة مهامي |
| المصدر | `21-ui-design.md §8.1` | — |
| المصدر | `21-ui-design.md §8.2` | — |
| حالة الاستخدام | UC-091 | Synchronize Field Device |
| المصدر | `[Derived]` | — |
<!-- END GENERATED: refs US-UI-SCR01-SYNC-DETAILS -->

</details>

### 5.8 US-PLT-SYNC-GATEWAY-SCALE — استيعاب عودة آلاف الأجهزة معًا

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

<!-- BEGIN GENERATED: refs US-PLT-SYNC-GATEWAY-SCALE -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-OFF-003 | 5,000 devices reconnect within 10 min → all sessions complete ≤ 30 min; oldest-offline devices first; no data… |
| المصدر | `FM-S11-01` | — |
| المصدر | `field-sync-protocol.md §6` | — |
<!-- END GENERATED: refs US-PLT-SYNC-GATEWAY-SCALE -->

</details>

### 5.9 US-PLT-SYNC-IDEMPOTENCY-STORE — عدم تكرار الأوامر مهما انقطعت المزامنة

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

<!-- BEGIN GENERATED: refs US-PLT-SYNC-IDEMPOTENCY-STORE -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `23-crosscutting.md` | — |
| المصدر | `FM-S11-02` | — |
| المصدر | `FM-S11-03` | — |
| المتطلب | REQ-OFF-006 | When a synchronization is interrupted, the system shall resume it without duplicating commands. |
| حالة الاستخدام | UC-091 | Synchronize Field Device |
<!-- END GENERATED: refs US-PLT-SYNC-IDEMPOTENCY-STORE -->

</details>

### 5.10 US-PLT-SYNC-THROUGHPUT — مزامنة ألف أمر خلال عشر دقائق

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

<!-- BEGIN GENERATED: refs US-PLT-SYNC-THROUGHPUT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الجودة | QAS-OFF-001 | works 72 h offline then reconnects on a 1 Mbps link → 1,000 queued commands synced ≤ 10 min; 0 silent overwri… |
| فحص البنية | FIT-15 | No last-write-wins merge for T1/T2 in sync |
| المصدر | `field-sync-protocol.md §6` | — |
<!-- END GENERATED: refs US-PLT-SYNC-THROUGHPUT -->

</details>

### 5.11 US-OPS-SYNC-HEALTH-ALERTS — مراقبة زمن المزامنة وانحراف ساعات الأجهزة

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

<!-- BEGIN GENERATED: refs US-OPS-SYNC-HEALTH-ALERTS -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc11.md` | — |
| المصدر | `THR-S11-05` | — |
<!-- END GENERATED: refs US-OPS-SYNC-HEALTH-ALERTS -->

</details>

### 5.12 US-OPS-SYNC-SIGNATURE-INCIDENT — معاملة فشل توقيع الأوامر كحادث أمني

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

<!-- BEGIN GENERATED: refs US-OPS-SYNC-SIGNATURE-INCIDENT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc11.md` | — |
| المصدر | `THR-S11-02` | — |
| المصدر | `THR-S03-05` | — |
<!-- END GENERATED: refs US-OPS-SYNC-SIGNATURE-INCIDENT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OFF-001 | Where the mobile field application is used, the system shall allow recording observations with location, time… | كل قصص الميزة المأخوذة من المواصفة (6) | TST-SLC03-INVARIANTS، TST-SLC11-INVARIANTS، TST-SYNC-SESSION-SM، TST-TASK-SM |
| REQ-OFF-003 | When a device reconnects, the system shall receive the device's recorded commands in their original order wit… | كل قصص الأوامر والنظام في الميزة (5) | TST-SLC11-INVARIANTS، TST-SYNC-SESSION-SM |
| REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… | كل قصص الأوامر والنظام في الميزة (5) | TST-SLC11-INVARIANTS، TST-SYNC-CONFLICT-SM، TST-SYNC-SESSION-SM |
| REQ-OFF-006 | When a synchronization is interrupted, the system shall resume it without duplicating commands. | `US-BC07-S-SYNC-SESSION-02`، `US-BC07-S-SYNC-SESSION-03`، `US-BC07-S-SYNC-SESSION-04`، `US-BC07-SYN-OPEN`، `US-BC07-SYN-UPLOAD-BATCH`، `US-PLT-SYNC-IDEMPOTENCY-STORE` | TST-SLC11-INVARIANTS، TST-SYNC-SESSION-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
