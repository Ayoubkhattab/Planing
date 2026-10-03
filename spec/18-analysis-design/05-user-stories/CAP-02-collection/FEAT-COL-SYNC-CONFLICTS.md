---
id: FEAT-COL-SYNC-CONFLICTS
type: feature
title: "حل تعارضات المزامنة"
status: DRAFT
version: "0.1"
capability: CAP-02.03
sources: [17-system-study/_build/features.csv, 17-system-study/_build/feature_map.csv]
generator: 17-system-study/_build/build_analysis_design.py
---

# حل تعارضات المزامنة

<!-- BEGIN GENERATED: doc -->
| البند | القيمة |
|---|---|
| المعرّف | FEAT-COL-SYNC-CONFLICTS |
| الإصدار | 0.1 |
| الحالة | مسودة |
| القدرة | CAP-02 جمع المعلومات |
| القدرة الفرعية | CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1) |
| الأدوار | المخطِّط؛ المحلل؛ النظام |
| الشاشات | SCR-06 قوائم المراجعة |
| حالات الاستخدام | UC-092 |
| القصص | 9: 7 من المواصفة، و2 جديدة |
<!-- END GENERATED: doc -->

## 1. نظرة عامة

### 1.1 القيمة

يعرض على المراجع ما تعارض من تسجيلات ميدانية مع الوضع الحالي ليقرر إعادة تطبيقها أو إسقاطها أو حلها يدويًا.

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
| `US-BC07-SCF-ASSIGN` | إسناد تعارض المزامنة | أمر | مسودة |
| `US-BC07-SCF-DISCARD` | حسم تعارض المزامنة بإسقاط الأمر الميداني | أمر | مسودة |
| `US-BC07-SCF-REAPPLY` | إعادة تطبيق تعارض المزامنة | أمر | مسودة |
| `US-BC07-SCF-RESOLVE-MANUALLY` | حل تعارض المزامنة يدويًا | أمر | مسودة |
| `US-BC07-Q-SCF-GET` | جلب: Original envelope, current state snapshot, owner rejection reason | جلب | مسودة |
| `US-BC07-Q-SCF-LIST` | جلب: Open sync conflicts by target type, assignee | جلب | مسودة |
| `US-BC07-S-SYNC-CONFLICT-01` | تلقائي: stale state-changing command (تعارض المزامنة) | نظام | مسودة |
| `US-UI-SCR06-SYNC-CONFLICT` | مقارنة الأمر المتعارض بالحالة الحالية وحسمه | واجهة | مسودة |
| `US-OPS-SCF-RATIO-ALERT` | التنبيه عند ارتفاع نسبة التعارضات | تشغيل | مسودة |
<!-- END GENERATED: story-index -->

## 5. القصص

### 5.1 US-BC07-SCF-ASSIGN — إسناد تعارض المزامنة

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

<!-- BEGIN GENERATED: refs US-BC07-SCF-ASSIGN -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/field/sync-conflicts/{id}/actions/assign` | — |
| الأمر | `CMD-SCF-ASSIGN` | إسناد تعارض المزامنة |
| السياسة | `POL-SCF-ASSIGN` | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)؛ tenant match; dev… |
| الحدث | `EVT-SCF-ASSIGNED` | يصل إلى: Reviewer notification; Sync delta (conflict notice to field user) |
| الكيان | `AGG-SYNC-CONFLICT` | تعارض المزامنة |
| الجدول | `field.sync_conflicts` | الجدول الرئيسي لتعارض المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلب | REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… |
| حالة الاستخدام | UC-092 | Review Synchronization Conflict |
| الاختبار | TST-SYNC-CONFLICT-SM، TST-SLC11-INVARIANTS | دورة حالات تعارض المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-SCF-ASSIGN -->

</details>

### 5.2 US-BC07-SCF-DISCARD — حسم تعارض المزامنة بإسقاط الأمر الميداني

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

<!-- BEGIN GENERATED: refs US-BC07-SCF-DISCARD -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/field/sync-conflicts/{id}/actions/discard` | — |
| الأمر | `CMD-SCF-DISCARD` | حسم تعارض المزامنة بإسقاط الأمر الميداني |
| السياسة | `POL-SCF-DISCARD` | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)؛ tenant match; dev… |
| الحدث | `EVT-SCF-DISCARDED` | يصل إلى: Reviewer notification; Sync delta (conflict notice to field user) |
| الكيان | `AGG-SYNC-CONFLICT` | تعارض المزامنة |
| الجدول | `field.sync_conflicts` | الجدول الرئيسي لتعارض المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلب | REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… |
| حالة الاستخدام | UC-092 | Review Synchronization Conflict |
| الاختبار | TST-SYNC-CONFLICT-SM، TST-SLC11-INVARIANTS | دورة حالات تعارض المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-SCF-DISCARD -->

</details>

### 5.3 US-BC07-SCF-REAPPLY — إعادة تطبيق تعارض المزامنة

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

<!-- BEGIN GENERATED: refs US-BC07-SCF-REAPPLY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/field/sync-conflicts/{id}/actions/reapply` | — |
| الأمر | `CMD-SCF-REAPPLY` | إعادة تطبيق تعارض المزامنة |
| السياسة | `POL-SCF-REAPPLY` | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)؛ tenant match; dev… |
| الحدث | `EVT-SCF-REAPPLIED` | يصل إلى: Reviewer notification; Sync delta (conflict notice to field user) |
| الكيان | `AGG-SYNC-CONFLICT` | تعارض المزامنة |
| الجدول | `field.sync_conflicts` | الجدول الرئيسي لتعارض المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلب | REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… |
| حالة الاستخدام | UC-092 | Review Synchronization Conflict |
| الاختبار | TST-SYNC-CONFLICT-SM، TST-SLC11-INVARIANTS | دورة حالات تعارض المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-SCF-REAPPLY -->

</details>

### 5.4 US-BC07-SCF-RESOLVE-MANUALLY — حل تعارض المزامنة يدويًا

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

<!-- BEGIN GENERATED: refs US-BC07-SCF-RESOLVE-MANUALLY -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `POST /api/v1/field/sync-conflicts/{id}/actions/resolve-manually` | — |
| الأمر | `CMD-SCF-RESOLVE-MANUALLY` | حل تعارض المزامنة يدويًا |
| السياسة | `POL-SCF-RESOLVE-MANUALLY` | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)؛ tenant match; dev… |
| الحدث | `EVT-SCF-RESOLVED-MANUALLY` | يصل إلى: Reviewer notification; Sync delta (conflict notice to field user) |
| الكيان | `AGG-SYNC-CONFLICT` | تعارض المزامنة |
| الجدول | `field.sync_conflicts` | الجدول الرئيسي لتعارض المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلب | REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… |
| حالة الاستخدام | UC-092 | Review Synchronization Conflict |
| الاختبار | TST-SYNC-CONFLICT-SM، TST-SLC11-INVARIANTS | دورة حالات تعارض المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-SCF-RESOLVE-MANUALLY -->

</details>

### 5.5 US-BC07-Q-SCF-GET — جلب: Original envelope, current state snapshot, owner rejection reason

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

<!-- BEGIN GENERATED: refs US-BC07-Q-SCF-GET -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/field/sync-conflicts/{conflict_id}` | — |
| الاستعلام | `QRY-SCF-GET` | Original envelope, current state snapshot, owner rejection reason |
| السياسة | `POL-SCF-GET` | reviewer authorized on target |
| الكيان | `AGG-SYNC-CONFLICT` | تعارض المزامنة |
| الجدول | `field.sync_conflicts` | الجدول الرئيسي لتعارض المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلب | REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… |
| حالة الاستخدام | UC-092 | Review Synchronization Conflict |
| الاختبار | TST-SYNC-CONFLICT-SM، TST-SLC11-INVARIANTS | دورة حالات تعارض المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-Q-SCF-GET -->

</details>

### 5.6 US-BC07-Q-SCF-LIST — جلب: Open sync conflicts by target type, assignee

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

<!-- BEGIN GENERATED: refs US-BC07-Q-SCF-LIST -->
| البند | المعرّف | المعنى |
|---|---|---|
| الواجهة البرمجية | `GET /api/v1/field/sync-conflicts` | — |
| الاستعلام | `QRY-SCF-LIST` | Open sync conflicts by target type, assignee |
| السياسة | `POL-SCF-LIST` | reviewers authorized on targets |
| الكيان | `AGG-SYNC-CONFLICT` | تعارض المزامنة |
| الجدول | `field.sync_conflicts` | الجدول الرئيسي لتعارض المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلب | REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… |
| حالة الاستخدام | UC-092 | Review Synchronization Conflict |
| الاختبار | TST-SYNC-CONFLICT-SM، TST-SLC11-INVARIANTS | دورة حالات تعارض المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-Q-SCF-LIST -->

</details>

### 5.7 US-BC07-S-SYNC-CONFLICT-01 — تلقائي: stale state-changing command (تعارض المزامنة)

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

<!-- BEGIN GENERATED: refs US-BC07-S-SYNC-CONFLICT-01 -->
| البند | المعرّف | المعنى |
|---|---|---|
| المحفِّز | `SYS:stale state-changing command` | rule CF-05: base_version ≠ current; stores original envelope, current state snapshot and owner rejection reas… |
| الانتقال | ∅ ← OPEN | — |
| الحدث | `EVT-SCF-OPENED` | يصل إلى: Reviewer notification; Sync delta (conflict notice to field user) |
| الكيان | `AGG-SYNC-CONFLICT` | تعارض المزامنة |
| الجدول | `field.sync_conflicts` | الجدول الرئيسي لتعارض المزامنة |
| وحدة النشر | DU-10 | — |
| المتطلب | REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… |
| حالة الاستخدام | UC-092 | Review Synchronization Conflict |
| الاختبار | TST-SYNC-CONFLICT-SM، TST-SLC11-INVARIANTS | دورة حالات تعارض المزامنة، وثوابت الشريحة SLC-11 |
<!-- END GENERATED: refs US-BC07-S-SYNC-CONFLICT-01 -->

</details>

### 5.8 US-UI-SCR06-SYNC-CONFLICT — مقارنة الأمر المتعارض بالحالة الحالية وحسمه

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

<!-- BEGIN GENERATED: refs US-UI-SCR06-SYNC-CONFLICT -->
| البند | المعرّف | المعنى |
|---|---|---|
| الشاشة | SCR-06 | شاشة قوائم المراجعة |
| المصدر | `QRY-SCF-GET` | — |
| حالة الاستخدام | UC-092 | Review Synchronization Conflict |
| المصدر | `INV-SCF-03` | — |
<!-- END GENERATED: refs US-UI-SCR06-SYNC-CONFLICT -->

</details>

### 5.9 US-OPS-SCF-RATIO-ALERT — التنبيه عند ارتفاع نسبة التعارضات

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

<!-- BEGIN GENERATED: refs US-OPS-SCF-RATIO-ALERT -->
| البند | المعرّف | المعنى |
|---|---|---|
| المصدر | `observability-slc11.md` | — |
| المتطلب | REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… |
| حالة الاستخدام | UC-092 | Review Synchronization Conflict |
<!-- END GENERATED: refs US-OPS-SCF-RATIO-ALERT -->

</details>

## 6. التتبع

<!-- BEGIN GENERATED: trace -->
| المتطلب | المعنى | القصص | الاختبار |
|---|---|---|---|
| REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict… | `US-BC07-Q-SCF-GET`، `US-BC07-Q-SCF-LIST`، `US-BC07-S-SYNC-CONFLICT-01`، `US-BC07-SCF-ASSIGN`، `US-BC07-SCF-DISCARD`، `US-BC07-SCF-REAPPLY`، `US-BC07-SCF-RESOLVE-MANUALLY`، `US-OPS-SCF-RATIO-ALERT` | TST-SLC11-INVARIANTS، TST-SYNC-CONFLICT-SM، TST-SYNC-SESSION-SM |
<!-- END GENERATED: trace -->

## 7. سجل التغييرات

| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | — | هيكل مولَّد من خريطة الميزات |
