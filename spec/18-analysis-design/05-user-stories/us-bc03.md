---
id: AD-05-US-BC03
type: user-stories
title: "قصص المستخدم — BC03"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
generator: 17-system-study/_build/build_analysis_design.py
---

# قصص المستخدم — BC03 Intelligence — الوعي والتحليل

مولَّد بالكامل من المصادر بواسطة `17-system-study/_build/build_analysis_design.py`؛ لا يُحرَّر يدويًا. القالب والتصنيف وتعريف ضوابط النوع والفئة في [00-guide.md](00-guide.md).

<!-- BEGIN GENERATED: build_analysis_design.py -->

## ملخص BC03

| نوع العملية | عدد القصص |
|---|---|
| إنشاء | 9 |
| تعديل | 14 |
| جلب | 17 |
| حذف / إنهاء | 12 |
| سير عمل | 17 |
| نظام (SYS) | 9 |
| **المجموع** | **78** |

### AGG-ALERT — التنبيه (Alert)

`03-domain/contexts/BC03/aggregates/AGG-ALERT.md` · SLC-06 · الحالات: RAISED, ACKNOWLEDGED → RESOLVED, DISMISSED

#### US-BC03-ALR-ACKNOWLEDGE — الإقرار باستلام التنبيه

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | recipient | `POST /api/v1/intelligence/alerts/{id}/actions/acknowledge` | POL-ALR-ACKNOWLEDGE |

**القصة:** بصفتي **recipient**، أريد **الإقرار باستلام التنبيه**، لكي يتحقق غرض التنبيه: تنبيه صادر عن قاعدة، بدورة حياة مدققة

- **الشروط المسبقة:** الحالة الحالية: RAISED؛ actor is a recipient
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACKNOWLEDGED؛ الحدث EVT-ALR-ACKNOWLEDGED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** recipient؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ALR-ACKNOWLEDGE` · `AGG-ALERT` · متطلبات: REQ-SIT-004, REQ-SIT-005, REQ-SIT-006 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ALR-ACKNOWLEDGE succeeds
  Given AGG-ALERT in state RAISED and every guard holds
  When recipient sends CMD-ALR-ACKNOWLEDGE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACKNOWLEDGED
  And EVT-ALR-ACKNOWLEDGED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ALR-ACKNOWLEDGE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALERT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACKNOWLEDGED, DISMISSED, RESOLVED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ALR-ACKNOWLEDGE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | NOT_A_RECIPIENT | 422 | لم يتحقق الشرط: actor is a recipient |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ALR-DISMISS — صرف النظر عن التنبيه

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | recipient | `POST /api/v1/intelligence/alerts/{id}/actions/dismiss` | POL-ALR-DISMISS |

**القصة:** بصفتي **recipient**، أريد **صرف النظر عن التنبيه**، لكي يتحقق غرض التنبيه: تنبيه صادر عن قاعدة، بدورة حياة مدققة

- **الشروط المسبقة:** الحالة الحالية: RAISED, ACKNOWLEDGED؛ actor is a recipient; reason (REQ-SIT-005)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DISMISSED؛ الحدث EVT-ALR-DISMISSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** recipient؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ALR-DISMISS` · `AGG-ALERT` · متطلبات: REQ-SIT-004, REQ-SIT-005, REQ-SIT-006 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ALR-DISMISS succeeds
  Given AGG-ALERT in state RAISED or ACKNOWLEDGED and every guard holds
  When recipient sends CMD-ALR-DISMISS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISMISSED
  And EVT-ALR-DISMISSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ALR-DISMISS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALERT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISMISSED, RESOLVED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ALR-DISMISS ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ALR-RESOLVE — حل التنبيه

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | recipient | `POST /api/v1/intelligence/alerts/{id}/actions/resolve` | POL-ALR-RESOLVE |

**القصة:** بصفتي **recipient**، أريد **حل التنبيه**، لكي يتحقق غرض التنبيه: تنبيه صادر عن قاعدة، بدورة حياة مدققة

- **الشروط المسبقة:** الحالة الحالية: RAISED, ACKNOWLEDGED؛ actor is a recipient; note
- **المدخلات:** `note`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RESOLVED؛ الحدث EVT-ALR-RESOLVED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** recipient؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ALR-RESOLVE` · `AGG-ALERT` · متطلبات: REQ-SIT-004, REQ-SIT-005, REQ-SIT-006 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ALR-RESOLVE succeeds
  Given AGG-ALERT in state RAISED or ACKNOWLEDGED and every guard holds
  When recipient sends CMD-ALR-RESOLVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RESOLVED
  And EVT-ALR-RESOLVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ALR-RESOLVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALERT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISMISSED, RESOLVED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ALR-RESOLVE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | NOT_A_RECIPIENT | 422 | لم يتحقق الشرط: actor is a recipient |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: note |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-S-ALERT-01 — تلقائي: rule condition met (التنبيه)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | ∅ | RAISED |

**القصة:** بصفتي **النظام**، عند «rule condition met»، أريد نقل **التنبيه** إلى RAISED، لكي يتحقق غرض التنبيه: تنبيه صادر عن قاعدة، بدورة حياة مدققة

- **الشرط:** no non-terminal alert for (rule, subject) inside dedupe window; label = max(rule label, triggering object labels)
- **المخرجات:** الحدث EVT-ALR-RAISED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ALERT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC03-S-ALERT-02 — تلقائي: condition met again within dedupe window (التنبيه)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | RAISED, ACKNOWLEDGED | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «condition met again within dedupe window»، أريد تحديث **التنبيه** دون تغيير حالته، لكي يتحقق غرض التنبيه: تنبيه صادر عن قاعدة، بدورة حياة مدققة

- **الشرط:** occurrence counter + last_occurrence updated
- **المخرجات:** الحدث EVT-ALR-REPEATED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ALERT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC03-S-ALERT-03 — تلقائي: unacknowledged beyond escalation delay (التنبيه)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | RAISED | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «unacknowledged beyond escalation delay»، أريد تحديث **التنبيه** دون تغيير حالته، لكي يتحقق غرض التنبيه: تنبيه صادر عن قاعدة، بدورة حياة مدققة

- **الشرط:** escalates to the rule's escalation recipients
- **المخرجات:** الحدث EVT-ALR-ESCALATED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ALERT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC03-S-ALERT-04 — تلقائي: condition cleared and rule auto_resolve (التنبيه)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | RAISED, ACKNOWLEDGED | RESOLVED |

**القصة:** بصفتي **النظام**، عند «condition cleared and rule auto_resolve»، أريد نقل **التنبيه** إلى RESOLVED، لكي يتحقق غرض التنبيه: تنبيه صادر عن قاعدة، بدورة حياة مدققة

- **الشرط:** system
- **المخرجات:** الحدث EVT-ALR-RESOLVED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ALERT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC03-Q-ALR-LIST — جلب: My alerts by state, severity, situation

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/intelligence/alerts` | POL-ALR-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب My alerts by state, severity, situation**، لكي يتحقق المتطلب: The system shall manage alerts through the states RAISED, ACKNOWLEDGED, RESOLVED and DISMISSED, requiring a reason for dismissal, and shall audit every transition

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** My alerts by state, severity, situation؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** recipient; label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ALR-LIST` · `AGG-ALERT` · متطلبات: REQ-SIT-005
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-ALR-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ALR-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ALR-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-ALR-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-ALERT-RULE — قاعدة التنبيه (Alert Rule)

`03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md` · SLC-06 · الحالات: DRAFT, ACTIVE, DISABLED → RETIRED

#### US-BC03-ARL-ACTIVATE — تفعيل قاعدة التنبيه

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst lead / Manager | `POST /api/v1/intelligence/alert-rules/{id}/actions/activate` | POL-ARL-ACTIVATE |

**القصة:** بصفتي **Analyst lead / Manager**، أريد **تفعيل قاعدة التنبيه**، لكي يتحقق غرض قاعدة التنبيه: قاعدة تنبيه على موقف أو على نطاق المستأجر

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ dry-run on last 24 h of events completed and reviewed (expected alert volume shown)
- **المدخلات:** `dry_run_ref`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-ARL-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead / Manager؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ARL-ACTIVATE` · `AGG-ALERT-RULE` · متطلبات: REQ-SIT-004 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ARL-ACTIVATE succeeds
  Given AGG-ALERT-RULE in state DRAFT and every guard holds
  When Analyst lead / Manager sends CMD-ARL-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-ARL-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ARL-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALERT_RULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISABLED, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ARL-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | DRY_RUN_REQUIRED | 422 | لم يتحقق الشرط: dry-run on last 24 h of events completed and reviewed (expected alert volume shown) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: dry_run_ref |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ARL-DEFINE — تعريف قاعدة التنبيه

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst lead / Manager | `POST /api/v1/intelligence/alert-rules` | POL-ARL-DEFINE |

**القصة:** بصفتي **Analyst lead / Manager**، أريد **تعريف قاعدة التنبيه**، لكي يتحقق غرض قاعدة التنبيه: قاعدة تنبيه على موقف أو على نطاق المستأجر

- **الشروط المسبقة:** الحالة الحالية: ∅؛ condition kind in RD-ALERT-RULE-TYPES; parameters valid; severity; dedupe window; situation ACTIVE or tenant-wide scope
- **المدخلات:** `situation`: urn, `scope`!: enum(situation,tenant), `kind`!: string, `parameters`!: object, `severity`!: enum(info,warning,critical), `dedupe_window`!: string, `escalation`: object, `auto_resolve`!: boolean, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-ARL-DEFINED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead / Manager؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ARL-DEFINE` · `AGG-ALERT-RULE` · متطلبات: REQ-SIT-004 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ARL-DEFINE succeeds
  Given AGG-ALERT-RULE does not exist yet and every guard holds
  When Analyst lead / Manager sends CMD-ARL-DEFINE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-ARL-DEFINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ARL-DEFINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALERT_RULE_INVALID | 422 | لم يتحقق الشرط: condition kind in RD-ALERT-RULE-TYPES |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ARL-DEFINE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: scope, kind, parameters, severity, dedupe_window, auto_resolve, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ARL-DISABLE — تعطيل قاعدة التنبيه

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst lead / Manager | `POST /api/v1/intelligence/alert-rules/{id}/actions/disable` | POL-ARL-DISABLE |

**القصة:** بصفتي **Analyst lead / Manager**، أريد **تعطيل قاعدة التنبيه**، لكي يتحقق غرض قاعدة التنبيه: قاعدة تنبيه على موقف أو على نطاق المستأجر

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DISABLED؛ الحدث EVT-ARL-DISABLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead / Manager؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ARL-DISABLE` · `AGG-ALERT-RULE` · متطلبات: REQ-SIT-004 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ARL-DISABLE succeeds
  Given AGG-ALERT-RULE in state ACTIVE and every guard holds
  When Analyst lead / Manager sends CMD-ARL-DISABLE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISABLED
  And EVT-ARL-DISABLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ARL-DISABLE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALERT_RULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISABLED, DRAFT, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ARL-DISABLE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ARL-EDIT — تعديل قاعدة التنبيه

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst lead / Manager | `POST /api/v1/intelligence/alert-rules/{id}/actions/edit` | POL-ARL-EDIT |

**القصة:** بصفتي **Analyst lead / Manager**، أريد **تعديل قاعدة التنبيه**، لكي يتحقق غرض قاعدة التنبيه: قاعدة تنبيه على موقف أو على نطاق المستأجر

- **الشروط المسبقة:** الحالة الحالية: DRAFT, DISABLED؛ same validation; new version
- **المدخلات:** `parameters`!: object, `severity`: enum(info,warning,critical), `dedupe_window`: string, `escalation`: object — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ARL-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead / Manager؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ARL-EDIT` · `AGG-ALERT-RULE` · متطلبات: REQ-SIT-004 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ARL-EDIT succeeds
  Given AGG-ALERT-RULE in state DRAFT or DISABLED and every guard holds
  When Analyst lead / Manager sends CMD-ARL-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ARL-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ARL-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALERT_RULE_INVALID | 422 | لم يتحقق الشرط: same validation; new version |
    | ALERT_RULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ARL-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: parameters |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ARL-ENABLE — تمكين قاعدة التنبيه

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst lead / Manager | `POST /api/v1/intelligence/alert-rules/{id}/actions/enable` | POL-ARL-ENABLE |

**القصة:** بصفتي **Analyst lead / Manager**، أريد **تمكين قاعدة التنبيه**، لكي يتحقق غرض قاعدة التنبيه: قاعدة تنبيه على موقف أو على نطاق المستأجر

- **الشروط المسبقة:** الحالة الحالية: DISABLED؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-ARL-ENABLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead / Manager؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ARL-ENABLE` · `AGG-ALERT-RULE` · متطلبات: REQ-SIT-004 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ARL-ENABLE succeeds
  Given AGG-ALERT-RULE in state DISABLED and every guard holds
  When Analyst lead / Manager sends CMD-ARL-ENABLE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-ARL-ENABLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ARL-ENABLE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALERT_RULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DRAFT, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ARL-ENABLE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ARL-RETIRE — إحالة قاعدة التنبيه إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst lead / Manager | `POST /api/v1/intelligence/alert-rules/{id}/actions/retire` | POL-ARL-RETIRE |

**القصة:** بصفتي **Analyst lead / Manager**، أريد **إحالة قاعدة التنبيه إلى التقاعد**، لكي يتحقق غرض قاعدة التنبيه: قاعدة تنبيه على موقف أو على نطاق المستأجر

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE, DISABLED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-ARL-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead / Manager؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ARL-RETIRE` · `AGG-ALERT-RULE` · متطلبات: REQ-SIT-004 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ARL-RETIRE succeeds
  Given AGG-ALERT-RULE in state DRAFT or ACTIVE or DISABLED and every guard holds
  When Analyst lead / Manager sends CMD-ARL-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-ARL-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ARL-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALERT_RULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ARL-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

### AGG-ANALYSIS-CASE — حالة التحليل (Analysis Case)

`03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md` · SLC-07 · الحالات: DRAFT, OPEN, CLOSED → CANCELLED

#### US-BC03-ACS-ADD-ASSUMPTION — إضافة افتراض إلى حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/add-assumption` | POL-ACS-ADD-ASSUMPTION |

**القصة:** بصفتي **Analyst**، أريد **إضافة افتراض إلى حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ statement; criticality (high/medium/low)
- **المدخلات:** `statement`!: LocalizedName, `criticality`!: enum(high,medium,low) — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ACS-ASSUMPTION-ADDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-ADD-ASSUMPTION` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-ADD-ASSUMPTION succeeds
  Given AGG-ANALYSIS-CASE in state OPEN and every guard holds
  When Analyst sends CMD-ACS-ADD-ASSUMPTION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ACS-ASSUMPTION-ADDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-ADD-ASSUMPTION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, DRAFT |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-ADD-ASSUMPTION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CASE_INVALID | 422 | لم يتحقق الشرط: statement; criticality (high/medium/low) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: statement, criticality |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-ADD-HYPOTHESIS — إضافة فرضية إلى حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/add-hypothesis` | POL-ACS-ADD-HYPOTHESIS |

**القصة:** بصفتي **Analyst**، أريد **إضافة فرضية إلى حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ statement; hypotheses per case ≤ 20
- **المدخلات:** `statement`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ACS-HYPOTHESIS-ADDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-ADD-HYPOTHESIS` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-ADD-HYPOTHESIS succeeds
  Given AGG-ANALYSIS-CASE in state OPEN and every guard holds
  When Analyst sends CMD-ACS-ADD-HYPOTHESIS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ACS-HYPOTHESIS-ADDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-ADD-HYPOTHESIS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, DRAFT |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-ADD-HYPOTHESIS ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CASE_INVALID | 422 | لم يتحقق الشرط: hypotheses per case ≤ 20 |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: statement |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-CANCEL — إلغاء حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/cancel` | POL-ACS-CANCEL |

**القصة:** بصفتي **Analyst**، أريد **إلغاء حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: DRAFT, OPEN؛ reason; no PUBLISHED assessment references the case
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-ACS-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-CANCEL` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-CANCEL succeeds
  Given AGG-ANALYSIS-CASE in state DRAFT or OPEN and every guard holds
  When Analyst sends CMD-ACS-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-ACS-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CASE_HAS_PUBLISHED_ASSESSMENT | 422 | لم يتحقق الشرط: no PUBLISHED assessment references the case |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-CLOSE — إغلاق حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/close` | POL-ACS-CLOSE |

**القصة:** بصفتي **Analyst**، أريد **إغلاق حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ reason; no QUEUED or RUNNING runs
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-ACS-CLOSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-CLOSE` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-CLOSE succeeds
  Given AGG-ANALYSIS-CASE in state OPEN and every guard holds
  When Analyst sends CMD-ACS-CLOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-ACS-CLOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-CLOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, DRAFT |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-CLOSE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RUNS_IN_PROGRESS | 422 | لم يتحقق الشرط: no QUEUED or RUNNING runs |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-CREATE — إنشاء حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases` | POL-ACS-CREATE |

**القصة:** بصفتي **Analyst**، أريد **إنشاء حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: ∅؛ title; owner; label
- **المدخلات:** `title`!: LocalizedName, `owner`!: urn, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-ACS-CREATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-CREATE` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-CREATE succeeds
  Given AGG-ANALYSIS-CASE does not exist yet and every guard holds
  When Analyst sends CMD-ACS-CREATE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-ACS-CREATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-CREATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-CREATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CASE_INVALID | 422 | لم يتحقق الشرط: title; owner; label |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: title, owner, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-DEFINE — تعريف حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/define` | POL-ACS-DEFINE |

**القصة:** بصفتي **Analyst**، أريد **تعريف حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: DRAFT, OPEN؛ question text; spatial extent (optional polygon); time window; new version
- **المدخلات:** `question`!: LocalizedName, `extent`: object, `window`!: Interval — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ACS-DEFINED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-DEFINE` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-DEFINE succeeds
  Given AGG-ANALYSIS-CASE in state DRAFT or OPEN and every guard holds
  When Analyst sends CMD-ACS-DEFINE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ACS-DEFINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-DEFINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-DEFINE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CASE_INVALID | 422 | لم يتحقق الشرط: question text; spatial extent (optional polygon); time window; new version |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: question, window |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-DEFINE-SCENARIO — تعريف سيناريو ضمن حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/define-scenario` | POL-ACS-DEFINE-SCENARIO |

**القصة:** بصفتي **Analyst**، أريد **تعريف سيناريو ضمن حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ name; assumption set; parameter overrides (REQ-ANL-007)
- **المدخلات:** `name`!: string, `assumptions`!: array, `parameter_overrides`: object — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ACS-SCENARIO-DEFINED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-DEFINE-SCENARIO` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-DEFINE-SCENARIO succeeds
  Given AGG-ANALYSIS-CASE in state OPEN and every guard holds
  When Analyst sends CMD-ACS-DEFINE-SCENARIO with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ACS-SCENARIO-DEFINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-DEFINE-SCENARIO is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, DRAFT |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-DEFINE-SCENARIO ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CASE_INVALID | 422 | لم يتحقق الشرط: name; assumption set; parameter overrides (REQ-ANL-007) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: name, assumptions |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-DESELECT-EVIDENCE — استبعاد دليل من حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/deselect-evidence` | POL-ACS-DESELECT-EVIDENCE |

**القصة:** بصفتي **Analyst**، أريد **استبعاد دليل من حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ reason; selection record closed, not deleted
- **المدخلات:** `selection_id`!: string, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ACS-EVIDENCE-DESELECTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-DESELECT-EVIDENCE` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-DESELECT-EVIDENCE succeeds
  Given AGG-ANALYSIS-CASE in state OPEN and every guard holds
  When Analyst sends CMD-ACS-DESELECT-EVIDENCE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ACS-EVIDENCE-DESELECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-DESELECT-EVIDENCE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, DRAFT |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-DESELECT-EVIDENCE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: selection_id, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-OPEN — فتح حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/open` | POL-ACS-OPEN |

**القصة:** بصفتي **Analyst**، أريد **فتح حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ question and scope present (REQ-ANL-001)
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← OPEN؛ الحدث EVT-ACS-OPENED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-OPEN` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-OPEN succeeds
  Given AGG-ANALYSIS-CASE in state DRAFT and every guard holds
  When Analyst sends CMD-ACS-OPEN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes OPEN
  And EVT-ACS-OPENED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-OPEN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, OPEN |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-OPEN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CASE_NOT_DEFINED | 422 | لم يتحقق الشرط: question and scope present (REQ-ANL-001) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-RECLASSIFY — إعادة تصنيف حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Security Officer | `POST /api/v1/intelligence/analysis-cases/{id}/actions/reclassify` | POL-ACS-RECLASSIFY |

**القصة:** بصفتي **Security Officer**، أريد **إعادة تصنيف حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: DRAFT, OPEN, CLOSED؛ new label ≥ max label of selected evidence; authority per policy
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ACS-RECLASSIFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-RECLASSIFY` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-RECLASSIFY succeeds
  Given AGG-ANALYSIS-CASE in state DRAFT or OPEN or CLOSED and every guard holds
  When Security Officer sends CMD-ACS-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ACS-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-RECLASSIFY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per policy |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-REOPEN — إعادة فتح حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/reopen` | POL-ACS-REOPEN |

**القصة:** بصفتي **Analyst**، أريد **إعادة فتح حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: CLOSED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← OPEN؛ الحدث EVT-ACS-REOPENED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-REOPEN` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-REOPEN succeeds
  Given AGG-ANALYSIS-CASE in state CLOSED and every guard holds
  When Analyst sends CMD-ACS-REOPEN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes OPEN
  And EVT-ACS-REOPENED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-REOPEN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, DRAFT, OPEN |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-REOPEN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-RETIRE-ASSUMPTION — سحب افتراض من حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/retire-assumption` | POL-ACS-RETIRE-ASSUMPTION |

**القصة:** بصفتي **Analyst**، أريد **سحب افتراض من حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ reason; runs using it are flagged
- **المدخلات:** `assumption_id`!: string, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ACS-ASSUMPTION-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-RETIRE-ASSUMPTION` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-RETIRE-ASSUMPTION succeeds
  Given AGG-ANALYSIS-CASE in state OPEN and every guard holds
  When Analyst sends CMD-ACS-RETIRE-ASSUMPTION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ACS-ASSUMPTION-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-RETIRE-ASSUMPTION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, DRAFT |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-RETIRE-ASSUMPTION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: assumption_id, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-SELECT-EVIDENCE — اختيار دليل لـحالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/select-evidence` | POL-ACS-SELECT-EVIDENCE |

**القصة:** بصفتي **Analyst**، أريد **اختيار دليل لـحالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ items visible to actor; each pinned with known_at = now; item label ≤ case label
- **المدخلات:** `items`!: array, `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ACS-EVIDENCE-SELECTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-SELECT-EVIDENCE` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-SELECT-EVIDENCE succeeds
  Given AGG-ANALYSIS-CASE in state OPEN and every guard holds
  When Analyst sends CMD-ACS-SELECT-EVIDENCE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ACS-EVIDENCE-SELECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-SELECT-EVIDENCE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, DRAFT |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-SELECT-EVIDENCE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVIDENCE_ABOVE_CASE_LABEL | 422 | لم يتحقق الشرط: item label ≤ case label |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: items |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ACS-UPDATE-HYPOTHESIS — تحديث فرضية في حالة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst | `POST /api/v1/intelligence/analysis-cases/{id}/actions/update-hypothesis` | POL-ACS-UPDATE-HYPOTHESIS |

**القصة:** بصفتي **Analyst**، أريد **تحديث فرضية في حالة التحليل**، لكي يتحقق غرض حالة التحليل: سؤال تحليلي بنطاق وفرضيات وافتراضات وأدلة مختارة مثبتة زمنياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ status ∈ {PROPOSED, SUPPORTED, WEAKENED, REJECTED, UNRESOLVED}; rationale; supporting findings refs
- **المدخلات:** `hypothesis_id`!: string, `status`!: enum(PROPOSED,SUPPORTED,WEAKENED,REJECTED,UNRESOLVED), `rationale`!: string, `findings`: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ACS-HYPOTHESIS-UPDATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (owner) · Security Officer (reclassify)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ACS-UPDATE-HYPOTHESIS` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001, REQ-ANL-007 · حالات استخدام: UC-010, UC-011, UC-012, UC-016
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ACS-UPDATE-HYPOTHESIS succeeds
  Given AGG-ANALYSIS-CASE in state OPEN and every guard holds
  When Analyst sends CMD-ACS-UPDATE-HYPOTHESIS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ACS-HYPOTHESIS-UPDATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ACS-UPDATE-HYPOTHESIS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, DRAFT |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ACS-UPDATE-HYPOTHESIS ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: hypothesis_id, status, rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-Q-ACS-GET — جلب: Case with question, scope, hypotheses, assumptions, visible selections, scenarios

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/intelligence/analysis-cases/{case_id}` | POL-ACS-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Case with question, scope, hypotheses, assumptions, visible selections, scenarios**، لكي يتحقق المتطلب: The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumptions and evidence references

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Case with question, scope, hypotheses, assumptions, visible selections, scenarios
- **الصلاحية:** case label rule; selections filtered؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ACS-GET` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-ACS-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-ACS-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-ACS-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-ACS-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC03-Q-ACS-LIST — جلب: Cases by owner, state, extent

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/intelligence/analysis-cases` | POL-ACS-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Cases by owner, state, extent**، لكي يتحقق المتطلب: The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumptions and evidence references

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Cases by owner, state, extent؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ACS-LIST` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-001
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-ACS-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ACS-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ACS-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-ACS-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC03-Q-FND-LIST — جلب: Findings with sources

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/intelligence/analysis-cases/{case_id}/findings` | POL-FND-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Findings with sources**، لكي يتحقق المتطلب: The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, methodology, limitations, reviewer and version

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Findings with sources؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-FND-LIST` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-005
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-FND-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-FND-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-FND-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-FND-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC03-Q-SCN-COMPARE — جلب: Side-by-side results of runs per scenario with differing inputs

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/intelligence/analysis-cases/{case_id}/scenario-comparison` | POL-SCN-COMPARE |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Side-by-side results of runs per scenario with differing inputs**، لكي يتحقق المتطلب: The system shall allow comparison of alternative scenarios within an analysis case

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Side-by-side results of runs per scenario with differing inputs؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** case label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SCN-COMPARE` · `AGG-ANALYSIS-CASE` · متطلبات: REQ-ANL-007
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-SCN-COMPARE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SCN-COMPARE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SCN-COMPARE is denied
  Given the policy denies the caller
  When the caller sends QRY-SCN-COMPARE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-ANALYSIS-METHOD — طريقة التحليل (Analysis Method Version)

`03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md` · SLC-07 · الحالات: DRAFT, ACTIVE, DEPRECATED → RETIRED

#### US-BC03-AMT-ACTIVATE — تفعيل طريقة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | second lead or Administrator | `POST /api/v1/intelligence/analysis-methods/{id}/actions/activate` | POL-AMT-ACTIVATE |

**القصة:** بصفتي **second lead or Administrator**، أريد **تفعيل طريقة التحليل**، لكي يتحقق غرض طريقة التحليل: طريقة تحليل بإصدار وبيئة تنفيذ ثابتة

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ validation suite passed; approver ≠ author
- **المدخلات:** `validation_report`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-AMT-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analysis lead (register) · second lead or Administrator (activate)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: approver ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-AMT-ACTIVATE` · `AGG-ANALYSIS-METHOD` · متطلبات: REQ-ANL-002, REQ-ANL-003 · حالات استخدام: UC-013
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AMT-ACTIVATE succeeds
  Given AGG-ANALYSIS-METHOD in state DRAFT and every guard holds
  When second lead or Administrator sends CMD-AMT-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-AMT-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AMT-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_METHOD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DEPRECATED, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AMT-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: validation_report |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-AMT-DEPRECATE — إهمال طريقة التحليل (إيقاف الاستخدام الجديد)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analysis lead (محسوم: `17-security-design.md` §5) | `POST /api/v1/intelligence/analysis-methods/{id}/actions/deprecate` | POL-AMT-DEPRECATE |

**القصة:** بصفتي **Analysis lead**، أريد **إهمال طريقة التحليل (إيقاف الاستخدام الجديد)**، لكي يتحقق غرض طريقة التحليل: طريقة تحليل بإصدار وبيئة تنفيذ ثابتة

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason; no new runs; reproduction still allowed
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DEPRECATED؛ الحدث EVT-AMT-DEPRECATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analysis lead (deprecate) — issuing role named by CR-77؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AMT-DEPRECATE` · `AGG-ANALYSIS-METHOD` · متطلبات: REQ-ANL-002, REQ-ANL-003 · حالات استخدام: UC-013
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AMT-DEPRECATE succeeds
  Given AGG-ANALYSIS-METHOD in state ACTIVE and every guard holds
  When Analysis lead sends CMD-AMT-DEPRECATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DEPRECATED
  And EVT-AMT-DEPRECATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AMT-DEPRECATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_METHOD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DEPRECATED, DRAFT, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AMT-DEPRECATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-AMT-REGISTER — تسجيل طريقة التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analysis lead | `POST /api/v1/intelligence/analysis-methods` | POL-AMT-REGISTER |

**القصة:** بصفتي **Analysis lead**، أريد **تسجيل طريقة التحليل**، لكي يتحقق غرض طريقة التحليل: طريقة تحليل بإصدار وبيئة تنفيذ ثابتة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ code + version unique; parameter JSON schema; execution image digest from internal registry; deterministic flag
- **المدخلات:** `code`!: string, `version`!: string, `parameter_schema`!: object, `image_digest`!: string, `deterministic`!: boolean, `description`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-AMT-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analysis lead (register) · second lead or Administrator (activate)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AMT-REGISTER` · `AGG-ANALYSIS-METHOD` · متطلبات: REQ-ANL-002, REQ-ANL-003 · حالات استخدام: UC-013
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AMT-REGISTER succeeds
  Given AGG-ANALYSIS-METHOD does not exist yet and every guard holds
  When Analysis lead sends CMD-AMT-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-AMT-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AMT-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AMT-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | METHOD_INVALID | 422 | لم يتحقق الشرط: code + version unique; parameter JSON schema; execution image digest from internal registry; deterministic flag |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: code, version, parameter_schema, image_digest, deterministic, description |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-AMT-RETIRE — إحالة طريقة التحليل إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analysis lead (محسوم: `17-security-design.md` §5) | `POST /api/v1/intelligence/analysis-methods/{id}/actions/retire` | POL-AMT-RETIRE |

**القصة:** بصفتي **Analysis lead**، أريد **إحالة طريقة التحليل إلى التقاعد**، لكي يتحقق غرض طريقة التحليل: طريقة تحليل بإصدار وبيئة تنفيذ ثابتة

- **الشروط المسبقة:** الحالة الحالية: DEPRECATED؛ no run of this version backs a PUBLISHED or SUPERSEDED assessment (reproducibility preserved)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-AMT-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analysis lead (retire) — issuing role named by CR-77؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AMT-RETIRE` · `AGG-ANALYSIS-METHOD` · متطلبات: REQ-ANL-002, REQ-ANL-003 · حالات استخدام: UC-013
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AMT-RETIRE succeeds
  Given AGG-ANALYSIS-METHOD in state DEPRECATED and every guard holds
  When Analysis lead sends CMD-AMT-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-AMT-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AMT-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_METHOD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DRAFT, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AMT-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | METHOD_BACKS_PUBLISHED_WORK | 422 | لم يتحقق الشرط: no run of this version backs a PUBLISHED or SUPERSEDED assessment (reproducibility preserved) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-Q-AMT-LIST — جلب: Methods and versions

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | any analyst | `GET /api/v1/intelligence/analysis-methods` | POL-AMT-LIST |

**القصة:** بصفتي **any analyst**، أريد **جلب Methods and versions**، لكي يتحقق المتطلب: When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and version, layers, filters, time and spatial extent, assumptions, steps, results, analyst and execution time

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Methods and versions؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any analyst؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AMT-LIST` · `AGG-ANALYSIS-METHOD` · متطلبات: REQ-ANL-002
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-AMT-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-AMT-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-AMT-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-AMT-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-ANALYSIS-RUN — تشغيل التحليل (Analysis Run)

`03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md` · SLC-07 · الحالات: QUEUED, RUNNING → SUCCEEDED, FAILED, CANCELLED

#### US-BC03-RUN-CANCEL — إلغاء تشغيل التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analyst | `POST /api/v1/intelligence/analysis-runs/{id}/actions/cancel` | POL-RUN-CANCEL |

**القصة:** بصفتي **Analyst**، أريد **إلغاء تشغيل التحليل**، لكي يتحقق غرض تشغيل التحليل: تنفيذ طريقة على مدخلات مثبتة، كمهمة غير متزامنة

- **الشروط المسبقة:** الحالة الحالية: QUEUED, RUNNING؛ submitter or case owner; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-RUN-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (submit, reproduce, cancel)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RUN-CANCEL` · `AGG-ANALYSIS-RUN` · متطلبات: REQ-ANL-002, REQ-ANL-003, REQ-ANL-004, REQ-INF-035 · حالات استخدام: UC-013
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RUN-CANCEL succeeds
  Given AGG-ANALYSIS-RUN in state QUEUED or RUNNING and every guard holds
  When Analyst sends CMD-RUN-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-RUN-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RUN-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ANALYSIS_RUN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, FAILED, SUCCEEDED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RUN-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-RUN-REPRODUCE — إعادة إنتاج تشغيل التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analyst | `POST /api/v1/intelligence/analysis-runs/{id}/actions/reproduce` | POL-RUN-REPRODUCE |

**القصة:** بصفتي **Analyst**، أريد **إعادة إنتاج تشغيل التحليل**، لكي يتحقق غرض تشغيل التحليل: تنفيذ طريقة على مدخلات مثبتة، كمهمة غير متزامنة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ source run SUCCEEDED; reproducer cleared for source run label; method version ACTIVE or DEPRECATED; copies inputs/parameters/seed exactly
- **المدخلات:** `source_run`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← QUEUED؛ الحدث EVT-RUN-QUEUED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (submit, reproduce, cancel)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: reproducer cleared for source run label؛ الالتزامات: audit
- **الربط:** `CMD-RUN-REPRODUCE` · `AGG-ANALYSIS-RUN` · متطلبات: REQ-ANL-002, REQ-ANL-003, REQ-ANL-004, REQ-INF-035 · حالات استخدام: UC-013
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RUN-REPRODUCE succeeds
  Given AGG-ANALYSIS-RUN does not exist yet and every guard holds
  When Analyst sends CMD-RUN-REPRODUCE with a valid payload, a new Idempotency-Key
  Then the state becomes QUEUED
  And EVT-RUN-QUEUED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RUN-REPRODUCE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RUN-REPRODUCE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REPRODUCTION_NOT_ALLOWED | 422 | لم يتحقق الشرط: reproducer cleared for source run label |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: source_run |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-RUN-SUBMIT — تقديم تشغيل التحليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analyst | `POST /api/v1/intelligence/analysis-runs` | POL-RUN-SUBMIT |

**القصة:** بصفتي **Analyst**، أريد **تقديم تشغيل التحليل**، لكي يتحقق غرض تشغيل التحليل: تنفيذ طريقة على مدخلات مثبتة، كمهمة غير متزامنة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ case OPEN; method ACTIVE; parameters valid against schema; inputs pinned (dataset refs with known_at = submission time, filters, layers, extent, time window, assumptions); run label ≥ max input label; tenant job quota
- **المدخلات:** `case`!: urn, `method`!: urn, `parameters`!: object, `inputs`!: array, `scenario`: string, `assumptions`: array, `seed`: integer, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← QUEUED؛ الحدث EVT-RUN-QUEUED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (submit, reproduce, cancel)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RUN-SUBMIT` · `AGG-ANALYSIS-RUN` · متطلبات: REQ-ANL-002, REQ-ANL-003, REQ-ANL-004, REQ-INF-035 · حالات استخدام: UC-013
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RUN-SUBMIT succeeds
  Given AGG-ANALYSIS-RUN does not exist yet and every guard holds
  When Analyst sends CMD-RUN-SUBMIT with a valid payload, a new Idempotency-Key
  Then the state becomes QUEUED
  And EVT-RUN-QUEUED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RUN-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RUN-SUBMIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RUN_INVALID | 422 | لم يتحقق الشرط: case OPEN; method ACTIVE; parameters valid against schema; inputs pinned (dataset refs with known_at = submission time, filters, layers, extent, time window, assumptions); run label ≥ max input label; tenant job quota |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: case, method, parameters, inputs, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-S-ANALYSIS-RUN-01 — تلقائي: worker lease acquired (تشغيل التحليل)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | QUEUED | RUNNING |

**القصة:** بصفتي **النظام**، عند «worker lease acquired»، أريد نقل **تشغيل التحليل** إلى RUNNING، لكي يتحقق غرض تشغيل التحليل: تنفيذ طريقة على مدخلات مثبتة، كمهمة غير متزامنة

- **الشرط:** executes with the submitter's authorization (visibility), never with system privileges
- **المخرجات:** الحدث EVT-RUN-STARTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ANALYSIS-RUN` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC03-S-ANALYSIS-RUN-02 — تلقائي: completed (تشغيل التحليل)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | RUNNING | SUCCEEDED |

**القصة:** بصفتي **النظام**، عند «completed»، أريد نقل **تشغيل التحليل** إلى SUCCEEDED، لكي يتحقق غرض تشغيل التحليل: تنفيذ طريقة على مدخلات مثبتة، كمهمة غير متزامنة

- **الشرط:** results stored as hashed artifacts; steps log; lineage record written (inputs+known_at, method version, image digest, parameters, seed, actor, times)
- **المخرجات:** الحدث EVT-RUN-SUCCEEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ANALYSIS-RUN` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC03-S-ANALYSIS-RUN-03 — تلقائي: error or timeout (تشغيل التحليل)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | RUNNING | FAILED |

**القصة:** بصفتي **النظام**، عند «error or timeout»، أريد نقل **تشغيل التحليل** إلى FAILED، لكي يتحقق غرض تشغيل التحليل: تنفيذ طريقة على مدخلات مثبتة، كمهمة غير متزامنة

- **الشرط:** error recorded; partial artifacts discarded
- **المخرجات:** الحدث EVT-RUN-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ANALYSIS-RUN` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC03-Q-RUN-ARTIFACT — جلب: Short-lived download target for a result artifact

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | مستخدم مخوَّل (ضمن allowed_scope) | `POST /api/v1/intelligence/analysis-runs/{run_id}/artifact-grants` | POL-RUN-ARTIFACT |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Short-lived download target for a result artifact**، لكي يتحقق المتطلب: When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and version, layers, filters, time and spatial extent, assumptions, steps, results, analyst and execution time

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Short-lived download target for a result artifact
- **الصلاحية:** run label rule; audited؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-RUN-ARTIFACT` · `AGG-ANALYSIS-RUN` · متطلبات: REQ-ANL-002
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-RUN-ARTIFACT computes its result only over what the caller may see
  Given data inside and outside the caller's allowed_scope
  When the caller sends QRY-RUN-ARTIFACT
  Then the result neither includes nor reveals data outside allowed_scope

Scenario: QRY-RUN-ARTIFACT is denied
  Given the policy denies the caller
  When the caller sends QRY-RUN-ARTIFACT
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC03-Q-RUN-GET — جلب: Run with pins, parameters, steps, status, artifacts, reproduction report

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/intelligence/analysis-runs/{run_id}` | POL-RUN-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Run with pins, parameters, steps, status, artifacts, reproduction report**، لكي يتحقق المتطلب: When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and version, layers, filters, time and spatial extent, assumptions, steps, results, analyst and execution time

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Run with pins, parameters, steps, status, artifacts, reproduction report
- **الصلاحية:** run label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-RUN-GET` · `AGG-ANALYSIS-RUN` · متطلبات: REQ-ANL-002
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-RUN-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-RUN-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-RUN-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-RUN-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-ASSESSMENT — التقييم (Assessment Version)

`03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md` · SLC-07 · الحالات: DRAFT, IN_REVIEW, PUBLISHED → SUPERSEDED, WITHDRAWN, DISCARDED

#### US-BC03-ASM-DISCARD — تجاهل مسودة التقييم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analyst | `POST /api/v1/intelligence/assessments/{id}/actions/discard` | POL-ASM-DISCARD |

**القصة:** بصفتي **Analyst**، أريد **تجاهل مسودة التقييم**، لكي يتحقق غرض التقييم: تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ author; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DISCARDED؛ الحدث EVT-ASM-DISCARDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ASM-DISCARD` · `AGG-ASSESSMENT` · متطلبات: REQ-ANL-005, REQ-ANL-006, REQ-ANL-008 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ASM-DISCARD succeeds
  Given AGG-ASSESSMENT in state DRAFT and every guard holds
  When Analyst sends CMD-ASM-DISCARD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISCARDED
  And EVT-ASM-DISCARDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ASM-DISCARD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSESSMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, IN_REVIEW, PUBLISHED, SUPERSEDED, WITHDRAWN |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ASM-DISCARD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ASM-DRAFT — إعداد مسودة التقييم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analyst | `POST /api/v1/intelligence/assessments` | POL-ASM-DRAFT |

**القصة:** بصفتي **Analyst**، أريد **إعداد مسودة التقييم**، لكي يتحقق غرض التقييم: تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت

- **الشروط المسبقة:** الحالة الحالية: ∅؛ case exists; either new assessment or revision of a PUBLISHED version (copies content); at most one DRAFT/IN_REVIEW per assessment
- **المدخلات:** `case`!: urn, `assessment`: urn, `title`!: LocalizedName, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-ASM-DRAFTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ASM-DRAFT` · `AGG-ASSESSMENT` · متطلبات: REQ-ANL-005, REQ-ANL-006, REQ-ANL-008 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ASM-DRAFT succeeds
  Given AGG-ASSESSMENT does not exist yet and every guard holds
  When Analyst sends CMD-ASM-DRAFT with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-ASM-DRAFTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ASM-DRAFT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ASM-DRAFT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | DRAFT_EXISTS | 422 | لم يتحقق الشرط: case exists; at most one DRAFT/IN_REVIEW per assessment |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: case, title, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ASM-EDIT — تعديل التقييم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst | `POST /api/v1/intelligence/assessments/{id}/actions/edit` | POL-ASM-EDIT |

**القصة:** بصفتي **Analyst**، أريد **تعديل التقييم**، لكي يتحقق غرض التقييم: تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ key judgments use RD-ESTIMATIVE-PROBABILITY terms and analytic confidence (low/moderate/high)
- **المدخلات:** `key_judgments`!: array, `citations`!: array, `assumptions`!: array, `uncertainty`!: object, `confidence`!: enum(low,moderate,high), `methodology`!: LocalizedName, `limitations`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ASM-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ASM-EDIT` · `AGG-ASSESSMENT` · متطلبات: REQ-ANL-005, REQ-ANL-006, REQ-ANL-008 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ASM-EDIT succeeds
  Given AGG-ASSESSMENT in state DRAFT and every guard holds
  When Analyst sends CMD-ASM-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ASM-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ASM-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSESSMENT_INVALID | 422 | لم يتحقق الشرط: key judgments use RD-ESTIMATIVE-PROBABILITY terms and analytic confidence (low/moderate/high) |
    | ASSESSMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, IN_REVIEW, PUBLISHED, SUPERSEDED, WITHDRAWN |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ASM-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: key_judgments, citations, assumptions, uncertainty, confidence, methodology, limitations |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ASM-PUBLISH — نشر التقييم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | reviewer / Analysis lead | `POST /api/v1/intelligence/assessments/{id}/actions/publish` | POL-ASM-PUBLISH |

**القصة:** بصفتي **reviewer / Analysis lead**، أريد **نشر التقييم**، لكي يتحقق غرض التقييم: تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت

- **الشروط المسبقة:** الحالة الحالية: IN_REVIEW؛ reviewer ≠ author; label ≥ max(findings, evidence); previous PUBLISHED version → SUPERSEDED in the same transaction
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PUBLISHED؛ الحدث EVT-ASM-PUBLISHED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: reviewer ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-ASM-PUBLISH` · `AGG-ASSESSMENT` · متطلبات: REQ-ANL-005, REQ-ANL-006, REQ-ANL-008 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ASM-PUBLISH succeeds
  Given AGG-ASSESSMENT in state IN_REVIEW and every guard holds
  When reviewer / Analysis lead sends CMD-ASM-PUBLISH with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PUBLISHED
  And EVT-ASM-PUBLISHED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ASM-PUBLISH is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSESSMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, DRAFT, PUBLISHED, SUPERSEDED, WITHDRAWN |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ASM-PUBLISH ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: reviewer ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ASM-RETURN — إعادة التقييم للمراجعة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | reviewer / Analysis lead | `POST /api/v1/intelligence/assessments/{id}/actions/return` | POL-ASM-RETURN |

**القصة:** بصفتي **reviewer / Analysis lead**، أريد **إعادة التقييم للمراجعة**، لكي يتحقق غرض التقييم: تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت

- **الشروط المسبقة:** الحالة الحالية: IN_REVIEW؛ reviewer; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-ASM-RETURNED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ASM-RETURN` · `AGG-ASSESSMENT` · متطلبات: REQ-ANL-005, REQ-ANL-006, REQ-ANL-008 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ASM-RETURN succeeds
  Given AGG-ASSESSMENT in state IN_REVIEW and every guard holds
  When reviewer / Analysis lead sends CMD-ASM-RETURN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DRAFT
  And EVT-ASM-RETURNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ASM-RETURN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSESSMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, DRAFT, PUBLISHED, SUPERSEDED, WITHDRAWN |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ASM-RETURN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ASM-SUBMIT — تقديم التقييم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/intelligence/assessments/{id}/actions/submit` | POL-ASM-SUBMIT |

**القصة:** بصفتي **Analyst**، أريد **تقديم التقييم**، لكي يتحقق غرض التقييم: تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ findings ≥ 1 (ACCEPTED), evidence, assumptions, uncertainty, confidence, methodology, limitations all present (REQ-ANL-005)
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← IN_REVIEW؛ الحدث EVT-ASM-SUBMITTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ASM-SUBMIT` · `AGG-ASSESSMENT` · متطلبات: REQ-ANL-005, REQ-ANL-006, REQ-ANL-008 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ASM-SUBMIT succeeds
  Given AGG-ASSESSMENT in state DRAFT and every guard holds
  When Analyst sends CMD-ASM-SUBMIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_REVIEW
  And EVT-ASM-SUBMITTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ASM-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSESSMENT_INCOMPLETE | 422 | لم يتحقق الشرط: findings ≥ 1 (ACCEPTED), evidence, assumptions, uncertainty, confidence, methodology, limitations all present (REQ-ANL-005) |
    | ASSESSMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, IN_REVIEW, PUBLISHED, SUPERSEDED, WITHDRAWN |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ASM-SUBMIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-ASM-WITHDRAW — سحب التقييم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | reviewer / Analysis lead | `POST /api/v1/intelligence/assessments/{id}/actions/withdraw` | POL-ASM-WITHDRAW |

**القصة:** بصفتي **reviewer / Analysis lead**، أريد **سحب التقييم**، لكي يتحقق غرض التقييم: تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت

- **الشروط المسبقة:** الحالة الحالية: PUBLISHED؛ reason; decisions and products referencing it are notified
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← WITHDRAWN؛ الحدث EVT-ASM-WITHDRAWN؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ASM-WITHDRAW` · `AGG-ASSESSMENT` · متطلبات: REQ-ANL-005, REQ-ANL-006, REQ-ANL-008 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ASM-WITHDRAW succeeds
  Given AGG-ASSESSMENT in state PUBLISHED and every guard holds
  When reviewer / Analysis lead sends CMD-ASM-WITHDRAW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes WITHDRAWN
  And EVT-ASM-WITHDRAWN is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ASM-WITHDRAW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSESSMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, DRAFT, IN_REVIEW, SUPERSEDED, WITHDRAWN |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ASM-WITHDRAW ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-S-ASSESSMENT-01 — تلقائي: newer version published (التقييم)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | PUBLISHED | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «newer version published»، أريد نقل **التقييم** إلى SUPERSEDED، لكي يتحقق غرض التقييم: تقييم تحليلي بإصدارات؛ الإصدار المنشور ثابت

- **الشرط:** system
- **المخرجات:** الحدث EVT-ASM-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ASSESSMENT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC03-Q-ASM-GET — جلب: Assessment version (default: current PUBLISHED; or version / known_at)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/intelligence/assessments/{assessment_id}` | POL-ASM-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Assessment version (default: current PUBLISHED; or version / known_at)**، لكي يتحقق المتطلب: If an assessment references evidence the reader is not authorized to view, then the system shall withhold that evidence according to policy and shall indicate the omission only where the policy permits

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Assessment version (default: current PUBLISHED; or version / known_at)
- **الصلاحية:** label rule; REDACT obligation for uncleared citations؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ASM-GET` · `AGG-ASSESSMENT` · متطلبات: REQ-ANL-008
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-ASM-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-ASM-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-ASM-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-ASM-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC03-Q-ASM-VERSIONS — جلب: Version history with states and times

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/intelligence/assessments/{assessment_id}/versions` | POL-ASM-VERSIONS |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Version history with states and times**، لكي يتحقق المتطلب: When an assessment is published, the system shall make that version immutable; later changes shall create a new version

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Version history with states and times؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ASM-VERSIONS` · `AGG-ASSESSMENT` · متطلبات: REQ-ANL-006
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-ASM-VERSIONS returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ASM-VERSIONS with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ASM-VERSIONS is denied
  Given the policy denies the caller
  When the caller sends QRY-ASM-VERSIONS
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-CAP-MESSAGE — رسالة CAP الصادرة (CAP Message (outbound))

`03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md` · SLC-16 · الحالات: PREPARED, FAILED → SENT, CANCELLED

#### US-BC03-CAP-CANCEL — إلغاء رسالة CAP الصادرة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | operator | `POST /api/v1/intelligence/cap-messages/{id}/actions/cancel` | POL-CAP-CANCEL |

**القصة:** بصفتي **operator**، أريد **إلغاء رسالة CAP الصادرة**، لكي يتحقق غرض رسالة CAP الصادرة: رسالة تنبيه بصيغة CAP 1.2 تُصدر لنقطة خارجية مسموحة

- **الشروط المسبقة:** الحالة الحالية: PREPARED, FAILED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-CAP-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CAP-CANCEL` · `AGG-CAP-MESSAGE` · متطلبات: REQ-INT-003 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CAP-CANCEL succeeds
  Given AGG-CAP-MESSAGE in state PREPARED or FAILED and every guard holds
  When operator sends CMD-CAP-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-CAP-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CAP-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CAP-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CAP_MESSAGE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, SENT |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-CAP-PREPARE — إعداد رسالة CAP الصادرة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تكامل | alert recipient / duty officer | `POST /api/v1/intelligence/cap-messages` | POL-CAP-PREPARE |

**القصة:** بصفتي **alert recipient / duty officer**، أريد **إعداد رسالة CAP الصادرة**، لكي يتحقق غرض رسالة CAP الصادرة: رسالة تنبيه بصيغة CAP 1.2 تُصدر لنقطة خارجية مسموحة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ tenant CAP enabled; alert RAISED/ACKNOWLEDGED; alert label ≤ tenant external release level; content = CAP fields from a reviewed template (no free text from classified sources); target connection cap_endpoint ACTIVE
- **المدخلات:** `alert`!: urn, `template`!: string, `connection`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← PREPARED؛ الحدث EVT-CAP-PREPARED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CAP-PREPARE` · `AGG-CAP-MESSAGE` · متطلبات: REQ-INT-003 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-CRE، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CAP-PREPARE succeeds
  Given AGG-CAP-MESSAGE does not exist yet and every guard holds
  When alert recipient / duty officer sends CMD-CAP-PREPARE with a valid payload, a new Idempotency-Key
  Then the state becomes PREPARED
  And EVT-CAP-PREPARED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CAP-PREPARE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CAP-PREPARE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RELEASE_NOT_ALLOWED | 422 | لم يتحقق الشرط: alert label ≤ tenant external release level |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: alert, template, connection |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-CAP-RELEASE — تحرير رسالة CAP الصادرة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | release authority | `POST /api/v1/intelligence/cap-messages/{id}/actions/release` | POL-CAP-RELEASE |

**القصة:** بصفتي **release authority**، أريد **تحرير رسالة CAP الصادرة**، لكي يتحقق غرض رسالة CAP الصادرة: رسالة تنبيه بصيغة CAP 1.2 تُصدر لنقطة خارجية مسموحة

- **الشروط المسبقة:** الحالة الحالية: PREPARED؛ release authority ≠ preparer; valid CAP 1.2 (schema validated); delivery acknowledged
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SENT؛ الحدث EVT-CAP-SENT؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)؛ الشروط: tenant match؛ فصل المهام: release authority ≠ preparer؛ الالتزامات: audit; mfa
- **الربط:** `CMD-CAP-RELEASE` · `AGG-CAP-MESSAGE` · متطلبات: REQ-INT-003 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CAP-RELEASE succeeds
  Given AGG-CAP-MESSAGE in state PREPARED and every guard holds
  When release authority sends CMD-CAP-RELEASE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SENT
  And EVT-CAP-SENT is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CAP-RELEASE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CAP-RELEASE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CAP_MESSAGE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, FAILED, SENT |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: release authority ≠ preparer |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-CAP-RETRY — إعادة محاولة رسالة CAP الصادرة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | operator | `POST /api/v1/intelligence/cap-messages/{id}/actions/retry` | POL-CAP-RETRY |

**القصة:** بصفتي **operator**، أريد **إعادة محاولة رسالة CAP الصادرة**، لكي يتحقق غرض رسالة CAP الصادرة: رسالة تنبيه بصيغة CAP 1.2 تُصدر لنقطة خارجية مسموحة

- **الشروط المسبقة:** الحالة الحالية: FAILED؛ operator
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PREPARED؛ الحدث EVT-CAP-RETRY؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CAP-RETRY` · `AGG-CAP-MESSAGE` · متطلبات: REQ-INT-003 · حالات استخدام: UC-023
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CAP-RETRY succeeds
  Given AGG-CAP-MESSAGE in state FAILED and every guard holds
  When operator sends CMD-CAP-RETRY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PREPARED
  And EVT-CAP-RETRY is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CAP-RETRY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CAP-RETRY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CAP_MESSAGE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, PREPARED, SENT |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-S-CAP-MESSAGE-01 — تلقائي: delivery failed after retries (رسالة CAP الصادرة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | PREPARED | FAILED |

**القصة:** بصفتي **النظام**، عند «delivery failed after retries»، أريد نقل **رسالة CAP الصادرة** إلى FAILED، لكي يتحقق غرض رسالة CAP الصادرة: رسالة تنبيه بصيغة CAP 1.2 تُصدر لنقطة خارجية مسموحة

- **الشرط:** 5 retries with backoff
- **المخرجات:** الحدث EVT-CAP-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-CAP-MESSAGE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC03-Q-CAP-LIST — جلب: Outbound CAP messages by state

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | release authority, Auditor | `GET /api/v1/intelligence/cap-messages` | POL-CAP-LIST |

**القصة:** بصفتي **release authority, Auditor**، أريد **جلب Outbound CAP messages by state**، لكي يتحقق المتطلب: Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2)

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Outbound CAP messages by state؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** release authority, Auditor؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CAP-LIST` · `AGG-CAP-MESSAGE` · متطلبات: REQ-INT-003
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-CAP-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CAP-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CAP-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-CAP-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-FINDING — النتيجة التحليلية (Finding)

`03-domain/contexts/BC03/aggregates/AGG-FINDING.md` · SLC-07 · الحالات: DRAFT, ACCEPTED → WITHDRAWN

#### US-BC03-FND-ACCEPT — قبول النتيجة التحليلية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | peer Analyst | `POST /api/v1/intelligence/findings/{id}/actions/accept` | POL-FND-ACCEPT |

**القصة:** بصفتي **peer Analyst**، أريد **قبول النتيجة التحليلية**، لكي يتحقق غرض النتيجة التحليلية: نتيجة تحليلية مستخلصة من تشغيلات أو أدلة

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ reviewer ≠ author (peer review)
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACCEPTED؛ الحدث EVT-FND-ACCEPTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (record, edit, withdraw) · peer Analyst (accept)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: reviewer ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-FND-ACCEPT` · `AGG-FINDING` · متطلبات: REQ-ANL-005, REQ-INF-035 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-FND-ACCEPT succeeds
  Given AGG-FINDING in state DRAFT and every guard holds
  When peer Analyst sends CMD-FND-ACCEPT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACCEPTED
  And EVT-FND-ACCEPTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-FND-ACCEPT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-FND-ACCEPT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | FINDING_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: reviewer ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-FND-EDIT — تعديل النتيجة التحليلية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst | `POST /api/v1/intelligence/findings/{id}/actions/edit` | POL-FND-EDIT |

**القصة:** بصفتي **Analyst**، أريد **تعديل النتيجة التحليلية**، لكي يتحقق غرض النتيجة التحليلية: نتيجة تحليلية مستخلصة من تشغيلات أو أدلة

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ same rules; new version
- **المدخلات:** `statement`: LocalizedName, `sources`: array, `uncertainty`: object — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-FND-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (record, edit, withdraw) · peer Analyst (accept)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-FND-EDIT` · `AGG-FINDING` · متطلبات: REQ-ANL-005, REQ-INF-035 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-FND-EDIT succeeds
  Given AGG-FINDING in state DRAFT and every guard holds
  When Analyst sends CMD-FND-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-FND-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-FND-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-FND-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | FINDING_INVALID | 422 | لم يتحقق الشرط: same rules; new version |
    | FINDING_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-FND-RECORD — تسجيل النتيجة التحليلية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analyst | `POST /api/v1/intelligence/findings` | POL-FND-RECORD |

**القصة:** بصفتي **Analyst**، أريد **تسجيل النتيجة التحليلية**، لكي يتحقق غرض النتيجة التحليلية: نتيجة تحليلية مستخلصة من تشغيلات أو أدلة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ statement; ≥ 1 source among SUCCEEDED runs of the case or selected evidence; uncertainty; label ≥ sources
- **المدخلات:** `case`!: urn, `statement`!: LocalizedName, `sources`!: array, `uncertainty`!: object, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-FND-RECORDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (record, edit, withdraw) · peer Analyst (accept)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-FND-RECORD` · `AGG-FINDING` · متطلبات: REQ-ANL-005, REQ-INF-035 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-FND-RECORD succeeds
  Given AGG-FINDING does not exist yet and every guard holds
  When Analyst sends CMD-FND-RECORD with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-FND-RECORDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-FND-RECORD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-FND-RECORD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | FINDING_INVALID | 422 | لم يتحقق الشرط: statement; ≥ 1 source among SUCCEEDED runs of the case or selected evidence; uncertainty; label ≥ sources |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: case, statement, sources, uncertainty, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-FND-WITHDRAW — سحب النتيجة التحليلية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analyst | `POST /api/v1/intelligence/findings/{id}/actions/withdraw` | POL-FND-WITHDRAW |

**القصة:** بصفتي **Analyst**، أريد **سحب النتيجة التحليلية**، لكي يتحقق غرض النتيجة التحليلية: نتيجة تحليلية مستخلصة من تشغيلات أو أدلة

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACCEPTED؛ reason; assessments citing it are flagged for review
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← WITHDRAWN؛ الحدث EVT-FND-WITHDRAWN؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (record, edit, withdraw) · peer Analyst (accept)؛ الشروط: tenant match; case visible; label rules؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-FND-WITHDRAW` · `AGG-FINDING` · متطلبات: REQ-ANL-005, REQ-INF-035 · حالات استخدام: UC-014, UC-015
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-FND-WITHDRAW succeeds
  Given AGG-FINDING in state DRAFT or ACCEPTED and every guard holds
  When Analyst sends CMD-FND-WITHDRAW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes WITHDRAWN
  And EVT-FND-WITHDRAWN is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-FND-WITHDRAW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-FND-WITHDRAW ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | FINDING_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

### AGG-SITUATION — الموقف (Situation)

`03-domain/contexts/BC03/aggregates/AGG-SITUATION.md` · SLC-06 · الحالات: DRAFT, ACTIVE, PAUSED → CLOSED

#### US-BC03-SIT-ACTIVATE — تفعيل الموقف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst / Manager | `POST /api/v1/intelligence/situations/{id}/actions/activate` | POL-SIT-ACTIVATE |

**القصة:** بصفتي **Analyst / Manager**، أريد **تفعيل الموقف**، لكي يتحقق غرض الموقف: سياق تشغيلي بامتداد وزمن ومعايير عضوية؛ محتواه إسقاط (ADR-P07)

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ definition complete; active situations per tenant ≤ quota
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-SIT-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIT-ACTIVATE` · `AGG-SITUATION` · متطلبات: REQ-SIT-001, REQ-SIT-002, REQ-SIT-003 · حالات استخدام: UC-020, UC-021, UC-022, UC-024, UC-098
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIT-ACTIVATE succeeds
  Given AGG-SITUATION in state DRAFT and every guard holds
  When Analyst / Manager sends CMD-SIT-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-SIT-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIT-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIT-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | QUOTA_EXCEEDED | 422 | لم يتحقق الشرط: active situations per tenant ≤ quota |
    | SITUATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CLOSED, PAUSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-SIT-CLOSE — إغلاق الموقف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst / Manager | `POST /api/v1/intelligence/situations/{id}/actions/close` | POL-SIT-CLOSE |

**القصة:** بصفتي **Analyst / Manager**، أريد **إغلاق الموقف**، لكي يتحقق غرض الموقف: سياق تشغيلي بامتداد وزمن ومعايير عضوية؛ محتواه إسقاط (ADR-P07)

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE, PAUSED؛ reason; final membership snapshot recorded
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-SIT-CLOSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIT-CLOSE` · `AGG-SITUATION` · متطلبات: REQ-SIT-001, REQ-SIT-002, REQ-SIT-003 · حالات استخدام: UC-020, UC-021, UC-022, UC-024, UC-098
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIT-CLOSE succeeds
  Given AGG-SITUATION in state DRAFT or ACTIVE or PAUSED and every guard holds
  When Analyst / Manager sends CMD-SIT-CLOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-SIT-CLOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIT-CLOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIT-CLOSE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SITUATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-SIT-CREATE — إنشاء الموقف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst / Manager | `POST /api/v1/intelligence/situations` | POL-SIT-CREATE |

**القصة:** بصفتي **Analyst / Manager**، أريد **إنشاء الموقف**، لكي يتحقق غرض الموقف: سياق تشغيلي بامتداد وزمن ومعايير عضوية؛ محتواه إسقاط (ADR-P07)

- **الشروط المسبقة:** الحالة الحالية: ∅؛ name; extent (polygon or buffer around an entity); time window; criteria valid per SPEC-SITUATION §2; owner; label
- **المدخلات:** `name`!: LocalizedName, `extent`!: object, `window`!: Interval, `criteria`!: object, `owner`!: urn, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-SIT-CREATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIT-CREATE` · `AGG-SITUATION` · متطلبات: REQ-SIT-001, REQ-SIT-002, REQ-SIT-003 · حالات استخدام: UC-020, UC-021, UC-022, UC-024, UC-098
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIT-CREATE succeeds
  Given AGG-SITUATION does not exist yet and every guard holds
  When Analyst / Manager sends CMD-SIT-CREATE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-SIT-CREATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIT-CREATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIT-CREATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SITUATION_INVALID | 422 | لم يتحقق الشرط: criteria valid per SPEC-SITUATION §2 |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: name, extent, window, criteria, owner, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-SIT-EDIT-DEFINITION — تعديل تعريف الموقف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst / Manager | `POST /api/v1/intelligence/situations/{id}/actions/edit-definition` | POL-SIT-EDIT-DEFINITION |

**القصة:** بصفتي **Analyst / Manager**، أريد **تعديل تعريف الموقف**، لكي يتحقق غرض الموقف: سياق تشغيلي بامتداد وزمن ومعايير عضوية؛ محتواه إسقاط (ADR-P07)

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE, PAUSED؛ criteria/extent/window valid; new definition version; membership recomputed from the new version
- **المدخلات:** `extent`: object, `window`: Interval, `criteria`: object, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SIT-DEFINITION-CHANGED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIT-EDIT-DEFINITION` · `AGG-SITUATION` · متطلبات: REQ-SIT-001, REQ-SIT-002, REQ-SIT-003 · حالات استخدام: UC-020, UC-021, UC-022, UC-024, UC-098
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIT-EDIT-DEFINITION succeeds
  Given AGG-SITUATION in state DRAFT or ACTIVE or PAUSED and every guard holds
  When Analyst / Manager sends CMD-SIT-EDIT-DEFINITION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SIT-DEFINITION-CHANGED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIT-EDIT-DEFINITION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIT-EDIT-DEFINITION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SITUATION_INVALID | 422 | لم يتحقق الشرط: criteria/extent/window valid; new definition version; membership recomputed from the new version |
    | SITUATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-SIT-PAUSE — إيقاف الموقف مؤقتًا

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst / Manager | `POST /api/v1/intelligence/situations/{id}/actions/pause` | POL-SIT-PAUSE |

**القصة:** بصفتي **Analyst / Manager**، أريد **إيقاف الموقف مؤقتًا**، لكي يتحقق غرض الموقف: سياق تشغيلي بامتداد وزمن ومعايير عضوية؛ محتواه إسقاط (ADR-P07)

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason; membership frozen, alerts of its rules suspended
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PAUSED؛ الحدث EVT-SIT-PAUSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIT-PAUSE` · `AGG-SITUATION` · متطلبات: REQ-SIT-001, REQ-SIT-002, REQ-SIT-003 · حالات استخدام: UC-020, UC-021, UC-022, UC-024, UC-098
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIT-PAUSE succeeds
  Given AGG-SITUATION in state ACTIVE and every guard holds
  When Analyst / Manager sends CMD-SIT-PAUSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PAUSED
  And EVT-SIT-PAUSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIT-PAUSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIT-PAUSE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SITUATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED, DRAFT, PAUSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-SIT-RECLASSIFY — إعادة تصنيف الموقف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Security Officer | `POST /api/v1/intelligence/situations/{id}/actions/reclassify` | POL-SIT-RECLASSIFY |

**القصة:** بصفتي **Security Officer**، أريد **إعادة تصنيف الموقف**، لكي يتحقق غرض الموقف: سياق تشغيلي بامتداد وزمن ومعايير عضوية؛ محتواه إسقاط (ADR-P07)

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE, PAUSED؛ authority per tenant policy; subscribers without clearance are unsubscribed
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SIT-RECLASSIFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIT-RECLASSIFY` · `AGG-SITUATION` · متطلبات: REQ-SIT-001, REQ-SIT-002, REQ-SIT-003 · حالات استخدام: UC-020, UC-021, UC-022, UC-024, UC-098
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIT-RECLASSIFY succeeds
  Given AGG-SITUATION in state DRAFT or ACTIVE or PAUSED and every guard holds
  When Security Officer sends CMD-SIT-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SIT-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIT-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIT-RECLASSIFY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per tenant policy |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SITUATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-SIT-RESUME — استئناف الموقف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst / Manager (محسوم: `17-security-design.md` §5) | `POST /api/v1/intelligence/situations/{id}/actions/resume` | POL-SIT-RESUME |

**القصة:** بصفتي **Analyst / Manager**، أريد **استئناف الموقف**، لكي يتحقق غرض الموقف: سياق تشغيلي بامتداد وزمن ومعايير عضوية؛ محتواه إسقاط (ADR-P07)

- **الشروط المسبقة:** الحالة الحالية: PAUSED؛ membership re-evaluated from current state
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-SIT-RESUMED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Manager (resume) — issuing role named by CR-77؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIT-RESUME` · `AGG-SITUATION` · متطلبات: REQ-SIT-001, REQ-SIT-002, REQ-SIT-003 · حالات استخدام: UC-020, UC-021, UC-022, UC-024, UC-098
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIT-RESUME succeeds
  Given AGG-SITUATION in state PAUSED and every guard holds
  When Analyst / Manager sends CMD-SIT-RESUME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-SIT-RESUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIT-RESUME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIT-RESUME ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SITUATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CLOSED, DRAFT |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC03-Q-SIT-CHANGES — جلب: Membership change log (visible members only) since cursor/time

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | cleared for situation; per-member filtering | `GET /api/v1/intelligence/situations/{situation_id}/changes` | POL-SIT-CHANGES |

**القصة:** بصفتي **cleared for situation; per-member filtering**، أريد **جلب Membership change log (visible members only) since cursor/time**، لكي يتحقق المتطلب: When an object matching a situation's criteria is created or changed, the system shall update the situation membership and record a situation change

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Membership change log (visible members only) since cursor/time؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** cleared for situation; per-member filtering؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SIT-CHANGES` · `AGG-SITUATION` · متطلبات: REQ-SIT-002
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SIT-CHANGES returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SIT-CHANGES with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SIT-CHANGES is denied
  Given the policy denies the caller
  When the caller sends QRY-SIT-CHANGES
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC03-Q-SIT-COP — جلب: Common operational picture: visible members (entities, events, observations, tasks, assessments, alerts) with resolved, possibly generalized geometry

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | cleared for situation; per-member filtering | `GET /api/v1/intelligence/situations/{situation_id}/picture` | POL-SIT-COP |

**القصة:** بصفتي **cleared for situation; per-member filtering**، أريد **جلب Common operational picture: visible members (entities, events, observations, tasks, assessments, alerts) with resolved, possibly generalized geometry**، لكي يتحقق المتطلب: The system shall present each situation as a map-based common operational picture of its entities, events, risks, tasks, resources, assessments and alerts

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Common operational picture: visible members (entities, events, observations, tasks, assessments, alerts) with resolved, possibly generalized geometry؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** cleared for situation; per-member filtering؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SIT-COP` · `AGG-SITUATION` · متطلبات: REQ-SIT-003
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SIT-COP returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SIT-COP with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SIT-COP is denied
  Given the policy denies the caller
  When the caller sends QRY-SIT-COP
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC03-Q-SIT-GET — جلب: Definition (version at valid_at), counts of visible members by type

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | cleared for situation label | `GET /api/v1/intelligence/situations/{situation_id}` | POL-SIT-GET |

**القصة:** بصفتي **cleared for situation label**، أريد **جلب Definition (version at valid_at), counts of visible members by type**، لكي يتحقق المتطلب: The system shall define each situation by geographic extent, time window, inclusion criteria, owner and classification

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Definition (version at valid_at), counts of visible members by type
- **الصلاحية:** cleared for situation label؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SIT-GET` · `AGG-SITUATION` · متطلبات: REQ-SIT-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SIT-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-SIT-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-SIT-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-SIT-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC03-Q-SIT-LIST — جلب: Situations by state, owner, extent intersecting bbox

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/intelligence/situations` | POL-SIT-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Situations by state, owner, extent intersecting bbox**، لكي يتحقق المتطلب: The system shall define each situation by geographic extent, time window, inclusion criteria, owner and classification

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Situations by state, owner, extent intersecting bbox؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user; situation label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SIT-LIST` · `AGG-SITUATION` · متطلبات: REQ-SIT-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SIT-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SIT-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SIT-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-SIT-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC03-Q-SIT-TILE — جلب: Vector tile of operational layer for the caller's security scope

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | cleared for situation; scope-keyed cache (ADR-P06 §6) | `GET /api/v1/intelligence/situations/{situation_id}/tiles/{layer}/{z}/{x}/{y}` | POL-SIT-TILE |

**القصة:** بصفتي **cleared for situation; scope-keyed cache (ADR-P06 §6)**، أريد **جلب Vector tile of operational layer for the caller's security scope**، لكي يتحقق المتطلب: The system shall serve map layers filtered by the requesting user's authorization and shall not share cached map tiles across different authorization scopes

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Vector tile of operational layer for the caller's security scope
- **الصلاحية:** cleared for situation; scope-keyed cache (ADR-P06 §6)؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SIT-TILE` · `AGG-SITUATION` · متطلبات: REQ-SIT-007
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SIT-TILE returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-SIT-TILE
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-SIT-TILE hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-SIT-TILE
  Then the response is 404 with the same shape as for a missing item
```

### استعلامات عابرة للـAggregates

#### US-BC03-Q-BASE-TILE — جلب: Base-map tile (layers marked unclassified only; shared cache)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user of tenant | `GET /api/v1/intelligence/base-maps/{layer}/{z}/{x}/{y}` | POL-BASE-TILE |

**القصة:** بصفتي **any user of tenant**، أريد **جلب Base-map tile (layers marked unclassified only; shared cache)**، لكي يتحقق المتطلب: The system shall serve map layers filtered by the requesting user's authorization and shall not share cached map tiles across different authorization scopes

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Base-map tile (layers marked unclassified only; shared cache)
- **الصلاحية:** any user of tenant؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-BASE-TILE` · عابر للـAggregates · متطلبات: REQ-SIT-007
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-BASE-TILE returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-BASE-TILE
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-BASE-TILE hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-BASE-TILE
  Then the response is 404 with the same shape as for a missing item
```

<!-- END GENERATED: build_analysis_design.py -->
