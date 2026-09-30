---
id: AD-05-US-BC08
type: user-stories
title: "قصص المستخدم — BC08"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
generator: 17-system-study/_build/build_analysis_design.py
---

# قصص المستخدم — BC08 Governance — الحوكمة والأمن

مولَّد بالكامل من المصادر بواسطة `17-system-study/_build/build_analysis_design.py`؛ لا يُحرَّر يدويًا. القالب والتصنيف وتعريف ضوابط النوع والفئة في [00-guide.md](00-guide.md).

<!-- BEGIN GENERATED: build_analysis_design.py -->

## ملخص BC08

| نوع العملية | عدد القصص |
|---|---|
| إنشاء | 6 |
| تعديل | 4 |
| جلب | 11 |
| حذف / إنهاء | 8 |
| سير عمل | 10 |
| نظام (SYS) | 14 |
| **المجموع** | **53** |

### AGG-CLASSIFICATION-SCHEME — مخطط التصنيف (Classification Scheme Version)

`03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md` · SLC-01 · الحالات: DRAFT, ACTIVE → SUPERSEDED, DISCARDED

#### US-BC08-CLS-ACTIVATE — تفعيل مخطط التصنيف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Security Officer | `POST /api/v1/governance/classification-schemes/{id}/actions/activate` | POL-CLS-ACTIVATE |

**القصة:** بصفتي **Security Officer**، أريد **تفعيل مخطط التصنيف**، لكي يتحقق غرض مخطط التصنيف: نظام التصنيف لكل مستأجر بإصدارات

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ validation passes; effective_from ≥ now; approver ≠ drafter; previous ACTIVE → SUPERSEDED in same transaction
- **المدخلات:** `effective_from`!: date-time — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-CLS-ACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: approver ≠ drafter؛ الالتزامات: audit; mfa
- **الربط:** `CMD-CLS-ACTIVATE` · `AGG-CLASSIFICATION-SCHEME` · متطلبات: REQ-GOV-001, REQ-GOV-004, REQ-GOV-009 · حالات استخدام: UC-085, UC-086, UC-089
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLS-ACTIVATE succeeds
  Given AGG-CLASSIFICATION-SCHEME in state DRAFT and every guard holds
  When Security Officer sends CMD-CLS-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-CLS-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLS-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLS-ACTIVATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISCARDED, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SCHEME_INVALID | 422 | لم يتحقق الشرط: validation passes; effective_from ≥ now; approver ≠ drafter; previous ACTIVE → SUPERSEDED in same transaction |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: effective_from |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-CLS-DISCARD — تجاهل مسودة مخطط التصنيف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Security Officer | `POST /api/v1/governance/classification-schemes/{id}/actions/discard` | POL-CLS-DISCARD |

**القصة:** بصفتي **Security Officer**، أريد **تجاهل مسودة مخطط التصنيف**، لكي يتحقق غرض مخطط التصنيف: نظام التصنيف لكل مستأجر بإصدارات

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DISCARDED؛ الحدث EVT-CLS-DISCARDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLS-DISCARD` · `AGG-CLASSIFICATION-SCHEME` · متطلبات: REQ-GOV-001, REQ-GOV-004, REQ-GOV-009 · حالات استخدام: UC-085, UC-086, UC-089
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLS-DISCARD succeeds
  Given AGG-CLASSIFICATION-SCHEME in state DRAFT and every guard holds
  When Security Officer sends CMD-CLS-DISCARD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISCARDED
  And EVT-CLS-DISCARDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLS-DISCARD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLS-DISCARD لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISCARDED, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-CLS-DRAFT — إعداد مسودة مخطط التصنيف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | Security Officer | `POST /api/v1/governance/classification-schemes` | POL-CLS-DRAFT |

**القصة:** بصفتي **Security Officer**، أريد **إعداد مسودة مخطط التصنيف**، لكي يتحقق غرض مخطط التصنيف: نظام التصنيف لكل مستأجر بإصدارات

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ Security Officer; at most one DRAFT per tenant
- **المدخلات:** `based_on`: urn — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-CLS-DRAFTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLS-DRAFT` · `AGG-CLASSIFICATION-SCHEME` · متطلبات: REQ-GOV-001, REQ-GOV-004, REQ-GOV-009 · حالات استخدام: UC-085, UC-086, UC-089
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLS-DRAFT succeeds
  Given AGG-CLASSIFICATION-SCHEME in state ∅ and every guard holds
  When Security Officer sends CMD-CLS-DRAFT with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-CLS-DRAFTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLS-DRAFT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLS-DRAFT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DRAFT_EXISTS | 422 | لم يتحقق الشرط: Security Officer; at most one DRAFT per tenant |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-CLS-EDIT — تعديل مخطط التصنيف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | حوكمة وأمن | Security Officer | `POST /api/v1/governance/classification-schemes/{id}/actions/edit` | POL-CLS-EDIT |

**القصة:** بصفتي **Security Officer**، أريد **تعديل مخطط التصنيف**، لكي يتحقق غرض مخطط التصنيف: نظام التصنيف لكل مستأجر بإصدارات

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ codes immutable once used; ranks strictly ordered; removal not allowed, only deprecation
- **المدخلات:** `levels`!: array, `compartments`!: array, `caveats`!: array, `audit_threshold`!: string, `default_level`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CLS-EDITED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLS-EDIT` · `AGG-CLASSIFICATION-SCHEME` · متطلبات: REQ-GOV-001, REQ-GOV-004, REQ-GOV-009 · حالات استخدام: UC-085, UC-086, UC-089
- **ضوابط النوع والفئة:** C-UPD، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLS-EDIT succeeds
  Given AGG-CLASSIFICATION-SCHEME in state DRAFT and every guard holds
  When Security Officer sends CMD-CLS-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-CLS-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLS-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLS-EDIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISCARDED, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SCHEME_INVALID | 422 | لم يتحقق الشرط: codes immutable once used; ranks strictly ordered; removal not allowed, only deprecation |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: levels, compartments, caveats, audit_threshold, default_level |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-S-CLASSIFICATION-SCHEME-01 — تلقائي: successor activated (مخطط التصنيف)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ACTIVE | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «successor activated»، أريد نقل **مخطط التصنيف** إلى SUPERSEDED، لكي يتحقق غرض مخطط التصنيف: نظام التصنيف لكل مستأجر بإصدارات

- **الشرط:** system
- **المخرجات:** الحدث EVT-CLS-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-CLASSIFICATION-SCHEME` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-Q-CLS-ACTIVE — جلب: Active scheme (labels only)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | any user of tenant | `GET /api/v1/governance/classification-scheme` | POL-CLS-ACTIVE |

**القصة:** بصفتي **any user of tenant**، أريد **جلب Active scheme (labels only)**، لكي يتحقق المتطلب: The system shall support a per-tenant classification scheme with ordered levels, an unlimited number of compartments and release caveats

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Active scheme (labels only)؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user of tenant؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CLS-ACTIVE` · `AGG-CLASSIFICATION-SCHEME` · متطلبات: REQ-GOV-001
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-CLS-ACTIVE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CLS-ACTIVE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CLS-ACTIVE is denied
  Given the policy denies the caller
  When the caller sends QRY-CLS-ACTIVE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-DISPOSITION-RUN — تشغيل الإتلاف (Disposition Run)

`03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md` · SLC-12a · الحالات: PLANNED, AWAITING_APPROVAL, APPROVED, EXECUTING → COMPLETED, COMPLETED_WITH_EXCEPTIONS, CANCELLED

#### US-BC08-DSP-APPROVE — اعتماد تشغيل الإتلاف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Records/Legal authority ≠ submitter | `POST /api/v1/governance/disposition-runs/{id}/actions/approve` | POL-DSP-APPROVE |

**القصة:** بصفتي **Records/Legal authority ≠ submitter**، أريد **اعتماد تشغيل الإتلاف**، لكي يتحقق غرض تشغيل الإتلاف: دورة إتلاف: ترشيح، اعتماد، تنفيذ عبر إتلاف مفاتيح الحاويات، شهادة

- **الشروط المسبقة:** الحالة الحالية ∈ {AWAITING_APPROVAL}؛ approver = Records/Legal authority ≠ submitter; re-run HoldCheck at approval
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← APPROVED؛ الحدث EVT-DSP-APPROVED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)؛ الشروط: tenant match؛ فصل المهام: approver ≠ submitter؛ الالتزامات: audit; mfa
- **الربط:** `CMD-DSP-APPROVE` · `AGG-DISPOSITION-RUN` · متطلبات: REQ-GOV-006, REQ-GOV-007 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DSP-APPROVE succeeds
  Given AGG-DISPOSITION-RUN in state AWAITING_APPROVAL and every guard holds
  When Records/Legal authority ≠ submitter sends CMD-DSP-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes APPROVED
  And EVT-DSP-APPROVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DSP-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DSP-APPROVE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DISPOSITION_RUN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, CANCELLED, COMPLETED, COMPLETED_WITH_EXCEPTIONS, EXECUTING, PLANNED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ submitter |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-DSP-CANCEL — إلغاء تشغيل الإتلاف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Archivist | `POST /api/v1/governance/disposition-runs/{id}/actions/cancel` | POL-DSP-CANCEL |

**القصة:** بصفتي **Archivist**، أريد **إلغاء تشغيل الإتلاف**، لكي يتحقق غرض تشغيل الإتلاف: دورة إتلاف: ترشيح، اعتماد، تنفيذ عبر إتلاف مفاتيح الحاويات، شهادة

- **الشروط المسبقة:** الحالة الحالية ∈ {APPROVED, AWAITING_APPROVAL, PLANNED}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-DSP-CANCELLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-DSP-CANCEL` · `AGG-DISPOSITION-RUN` · متطلبات: REQ-GOV-006, REQ-GOV-007 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DSP-CANCEL succeeds
  Given AGG-DISPOSITION-RUN in state APPROVED or AWAITING_APPROVAL or PLANNED and every guard holds
  When Archivist sends CMD-DSP-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-DSP-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DSP-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DSP-CANCEL لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DISPOSITION_RUN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, COMPLETED_WITH_EXCEPTIONS, EXECUTING |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-DSP-SUBMIT — تقديم تشغيل الإتلاف

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Archivist | `POST /api/v1/governance/disposition-runs/{id}/actions/submit` | POL-DSP-SUBMIT |

**القصة:** بصفتي **Archivist**، أريد **تقديم تشغيل الإتلاف**، لكي يتحقق غرض تشغيل الإتلاف: دورة إتلاف: ترشيح، اعتماد، تنفيذ عبر إتلاف مفاتيح الحاويات، شهادة

- **الشروط المسبقة:** الحالة الحالية ∈ {PLANNED}؛ Archivist reviewed candidate summary (counts per class/bucket, REVIEW-action items listed)
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← AWAITING_APPROVAL؛ الحدث EVT-DSP-SUBMITTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-DSP-SUBMIT` · `AGG-DISPOSITION-RUN` · متطلبات: REQ-GOV-006, REQ-GOV-007 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DSP-SUBMIT succeeds
  Given AGG-DISPOSITION-RUN in state PLANNED and every guard holds
  When Archivist sends CMD-DSP-SUBMIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes AWAITING_APPROVAL
  And EVT-DSP-SUBMITTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DSP-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DSP-SUBMIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DISPOSITION_RUN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, AWAITING_APPROVAL, CANCELLED, COMPLETED, COMPLETED_WITH_EXCEPTIONS, EXECUTING |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-S-DISPOSITION-RUN-01 — تلقائي: scheduled evaluation (daily) (تشغيل الإتلاف)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | ∅ | PLANNED |

**القصة:** بصفتي **النظام**، عند «scheduled evaluation (daily)»، أريد نقل **تشغيل الإتلاف** إلى PLANNED، لكي يتحقق غرض تشغيل الإتلاف: دورة إتلاف: ترشيح، اعتماد، تنفيذ عبر إتلاف مفاتيح الحاويات، شهادة

- **الشرط:** candidates = key buckets whose records are all past retention under the ACTIVE schedule; held items identified via HoldCheck
- **المخرجات:** الحدث EVT-DSP-PLANNED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-DISPOSITION-RUN` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-S-DISPOSITION-RUN-02 — تلقائي: execution started (تشغيل الإتلاف)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | APPROVED | EXECUTING |

**القصة:** بصفتي **النظام**، عند «execution started»، أريد نقل **تشغيل الإتلاف** إلى EXECUTING، لكي يتحقق غرض تشغيل الإتلاف: دورة إتلاف: ترشيح، اعتماد، تنفيذ عبر إتلاف مفاتيح الحاويات، شهادة

- **الشرط:** held items in each bucket re-wrapped under hold keys first; then bucket keys destroyed; owners notified to purge plaintext caches and projections; tombstones written
- **المخرجات:** الحدث EVT-DSP-EXECUTING؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-DISPOSITION-RUN` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-S-DISPOSITION-RUN-03 — تلقائي: all buckets processed (تشغيل الإتلاف)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | EXECUTING | COMPLETED |

**القصة:** بصفتي **النظام**، عند «all buckets processed»، أريد نقل **تشغيل الإتلاف** إلى COMPLETED، لكي يتحقق غرض تشغيل الإتلاف: دورة إتلاف: ترشيح، اعتماد، تنفيذ عبر إتلاف مفاتيح الحاويات، شهادة

- **الشرط:** certificate issued (buckets, key ids destroyed, counts, holds excluded)
- **المخرجات:** الحدث EVT-DSP-COMPLETED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-DISPOSITION-RUN` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-S-DISPOSITION-RUN-04 — تلقائي: some buckets failed (تشغيل الإتلاف)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | EXECUTING | COMPLETED_WITH_EXCEPTIONS |

**القصة:** بصفتي **النظام**، عند «some buckets failed»، أريد نقل **تشغيل الإتلاف** إلى COMPLETED_WITH_EXCEPTIONS، لكي يتحقق غرض تشغيل الإتلاف: دورة إتلاف: ترشيح، اعتماد، تنفيذ عبر إتلاف مفاتيح الحاويات، شهادة

- **الشرط:** failed buckets listed; retried next run
- **المخرجات:** الحدث EVT-DSP-COMPLETED-WITH-EXCEPTIONS؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-DISPOSITION-RUN` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-Q-DSP-GET — جلب: Run with candidate summary, exceptions and certificate

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | Archivist, Legal, Auditor | `GET /api/v1/governance/disposition-runs/{run_id}` | POL-DSP-GET |

**القصة:** بصفتي **Archivist, Legal, Auditor**، أريد **جلب Run with candidate summary, exceptions and certificate**، لكي يتحقق المتطلب: The system shall apply a retention schedule to every record class

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Run with candidate summary, exceptions and certificate
- **الصلاحية:** Archivist, Legal, Auditor؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-DSP-GET` · `AGG-DISPOSITION-RUN` · متطلبات: REQ-GOV-006
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-DSP-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-DSP-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-DSP-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-DSP-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-ERASURE-REQUEST — طلب المحو (Erasure Request)

`03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md` · SLC-12a · الحالات: RECEIVED, SCOPED, APPROVED, BLOCKED_BY_HOLD, EXECUTING → COMPLETED, REJECTED

#### US-BC08-ERS-APPROVE — اعتماد طلب المحو

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Legal authority ≠ registrar | `POST /api/v1/governance/erasure-requests/{id}/actions/approve` | POL-ERS-APPROVE |

**القصة:** بصفتي **Legal authority ≠ registrar**، أريد **اعتماد طلب المحو**، لكي يتحقق غرض طلب المحو: طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه

- **الشروط المسبقة:** الحالة الحالية ∈ {SCOPED}؛ Legal/Compliance authority ≠ registrar; decision recorded with basis
- **المدخلات:** `decision_note`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← APPROVED؛ الحدث EVT-ERS-APPROVED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject)؛ الشروط: tenant match؛ فصل المهام: approver ≠ registrar؛ الالتزامات: audit; mfa
- **الربط:** `CMD-ERS-APPROVE` · `AGG-ERASURE-REQUEST` · متطلبات: REQ-GOV-008 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ERS-APPROVE succeeds
  Given AGG-ERASURE-REQUEST in state SCOPED and every guard holds
  When Legal authority ≠ registrar sends CMD-ERS-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes APPROVED
  And EVT-ERS-APPROVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ERS-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ERS-APPROVE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | ERASURE_REQUEST_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, BLOCKED_BY_HOLD, COMPLETED, EXECUTING, RECEIVED, REJECTED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ registrar |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: decision_note |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-ERS-REGISTER — تسجيل طلب المحو

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | Privacy officer / Legal | `POST /api/v1/governance/erasure-requests` | POL-ERS-REGISTER |

**القصة:** بصفتي **Privacy officer / Legal**، أريد **تسجيل طلب المحو**، لكي يتحقق غرض طلب المحو: طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ legal basis reference; subject identification (platform person URN and/or information entity URNs of type person); requester
- **المدخلات:** `legal_basis`!: string, `person`: urn, `entities`: array, `requester`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← RECEIVED؛ الحدث EVT-ERS-RECEIVED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-ERS-REGISTER` · `AGG-ERASURE-REQUEST` · متطلبات: REQ-GOV-008 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ERS-REGISTER succeeds
  Given AGG-ERASURE-REQUEST in state ∅ and every guard holds
  When Privacy officer / Legal sends CMD-ERS-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes RECEIVED
  And EVT-ERS-RECEIVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ERS-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ERS-REGISTER لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | ERASURE_INVALID | 422 | لم يتحقق الشرط: legal basis reference; subject identification (platform person URN and/or information entity URNs of type person); requester |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: legal_basis, requester |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-ERS-REJECT — رفض طلب المحو

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Legal authority ≠ registrar | `POST /api/v1/governance/erasure-requests/{id}/actions/reject` | POL-ERS-REJECT |

**القصة:** بصفتي **Legal authority ≠ registrar**، أريد **رفض طلب المحو**، لكي يتحقق غرض طلب المحو: طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه

- **الشروط المسبقة:** الحالة الحالية ∈ {SCOPED}؛ reason (e.g. legal obligation to retain)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-ERS-REJECTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-ERS-REJECT` · `AGG-ERASURE-REQUEST` · متطلبات: REQ-GOV-008 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ERS-REJECT succeeds
  Given AGG-ERASURE-REQUEST in state SCOPED and every guard holds
  When Legal authority ≠ registrar sends CMD-ERS-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-ERS-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ERS-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ERS-REJECT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | ERASURE_REQUEST_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, BLOCKED_BY_HOLD, COMPLETED, EXECUTING, RECEIVED, REJECTED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-S-ERASURE-REQUEST-01 — تلقائي: subject scope resolved (طلب المحو)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | RECEIVED | SCOPED |

**القصة:** بصفتي **النظام**، عند «subject scope resolved»، أريد نقل **طلب المحو** إلى SCOPED، لكي يتحقق غرض طلب المحو: طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه

- **الشرط:** subject keys located in BC01 (persons), BC02 (entities with personal_data claims) and BC05 (qualification records of that person, CR-69); affected record counts per context
- **المخرجات:** الحدث EVT-ERS-SCOPED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ERASURE-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-S-ERASURE-REQUEST-02 — تلقائي: hold matches subject (طلب المحو)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | APPROVED | BLOCKED_BY_HOLD |

**القصة:** بصفتي **النظام**، عند «hold matches subject»، أريد نقل **طلب المحو** إلى BLOCKED_BY_HOLD، لكي يتحقق غرض طلب المحو: طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه

- **الشرط:** HoldCheck positive
- **المخرجات:** الحدث EVT-ERS-BLOCKED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ERASURE-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-S-ERASURE-REQUEST-03 — تلقائي: hold released (طلب المحو)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | BLOCKED_BY_HOLD | APPROVED |

**القصة:** بصفتي **النظام**، عند «hold released»، أريد نقل **طلب المحو** إلى APPROVED، لكي يتحقق غرض طلب المحو: طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه

- **الشرط:** HoldCheck negative
- **المخرجات:** الحدث EVT-ERS-UNBLOCKED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ERASURE-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-S-ERASURE-REQUEST-04 — تلقائي: execution started (طلب المحو)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | APPROVED | EXECUTING |

**القصة:** بصفتي **النظام**، عند «execution started»، أريد نقل **طلب المحو** إلى EXECUTING، لكي يتحقق غرض طلب المحو: طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه

- **الشرط:** subject DEKs destroyed; owners purge plaintext caches/projections; pseudonymous reference kept for audit facts
- **المخرجات:** الحدث EVT-ERS-EXECUTING؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ERASURE-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-S-ERASURE-REQUEST-05 — تلقائي: all contexts confirmed (طلب المحو)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | EXECUTING | COMPLETED |

**القصة:** بصفتي **النظام**، عند «all contexts confirmed»، أريد نقل **طلب المحو** إلى COMPLETED، لكي يتحقق غرض طلب المحو: طلب محو البيانات الشخصية لصاحب بيانات عبر إتلاف مفتاحه

- **الشرط:** confirmation from each owning context ≤ 24 h (QAS-PRV-001); certificate issued
- **المخرجات:** الحدث EVT-ERS-COMPLETED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ERASURE-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-Q-ERS-GET — جلب: Request with scope counts, confirmations and certificate (no personal data)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | Legal, Auditor | `GET /api/v1/governance/erasure-requests/{request_id}` | POL-ERS-GET |

**القصة:** بصفتي **Legal, Auditor**، أريد **جلب Request with scope counts, confirmations and certificate (no personal data)**، لكي يتحقق المتطلب: When the personal data of a data subject must be erased, the system shall make it unrecoverable in operational stores, projections, backups and archives while retaining non-personal audit facts

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Request with scope counts, confirmations and certificate (no personal data)
- **الصلاحية:** Legal, Auditor؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ERS-GET` · `AGG-ERASURE-REQUEST` · متطلبات: REQ-GOV-008
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-ERS-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ERS-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ERS-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-ERS-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-LEGAL-HOLD — التجميد القانوني (Legal Hold)

`03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md` · SLC-12a · الحالات: ACTIVE, RELEASE_REQUESTED → RELEASED

#### US-BC08-LHD-APPROVE-RELEASE — اعتماد إصدار التجميد القانوني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Legal/Compliance authority | `POST /api/v1/governance/legal-holds/{id}/actions/approve-release` | POL-LHD-APPROVE-RELEASE |

**القصة:** بصفتي **Legal/Compliance authority**، أريد **اعتماد إصدار التجميد القانوني**، لكي يتحقق غرض التجميد القانوني: تجميد قانوني يمنع إتلاف ومحو ما يشمله

- **الشروط المسبقة:** الحالة الحالية ∈ {RELEASE_REQUESTED}؛ second Legal authority ≠ requester
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← RELEASED؛ الحدث EVT-LHD-RELEASED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Legal/Compliance authority (place, extend, request/approve/cancel release)؛ الشروط: tenant match؛ فصل المهام: approver ≠ requester؛ الالتزامات: audit; mfa
- **الربط:** `CMD-LHD-APPROVE-RELEASE` · `AGG-LEGAL-HOLD` · متطلبات: REQ-GOV-007 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-LHD-APPROVE-RELEASE succeeds
  Given AGG-LEGAL-HOLD in state RELEASE_REQUESTED and every guard holds
  When Legal/Compliance authority sends CMD-LHD-APPROVE-RELEASE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RELEASED
  And EVT-LHD-RELEASED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-LHD-APPROVE-RELEASE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-LHD-APPROVE-RELEASE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LEGAL_HOLD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RELEASED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ requester |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-LHD-CANCEL-RELEASE — إلغاء إصدار التجميد القانوني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Legal/Compliance authority | `POST /api/v1/governance/legal-holds/{id}/actions/cancel-release` | POL-LHD-CANCEL-RELEASE |

**القصة:** بصفتي **Legal/Compliance authority**، أريد **إلغاء إصدار التجميد القانوني**، لكي يتحقق غرض التجميد القانوني: تجميد قانوني يمنع إتلاف ومحو ما يشمله

- **الشروط المسبقة:** الحالة الحالية ∈ {RELEASE_REQUESTED}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-LHD-RELEASE-CANCELLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Legal/Compliance authority (place, extend, request/approve/cancel release)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-LHD-CANCEL-RELEASE` · `AGG-LEGAL-HOLD` · متطلبات: REQ-GOV-007 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-LHD-CANCEL-RELEASE succeeds
  Given AGG-LEGAL-HOLD in state RELEASE_REQUESTED and every guard holds
  When Legal/Compliance authority sends CMD-LHD-CANCEL-RELEASE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-LHD-RELEASE-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-LHD-CANCEL-RELEASE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-LHD-CANCEL-RELEASE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LEGAL_HOLD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RELEASED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-LHD-EXTEND — تمديد التجميد القانوني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | حوكمة وأمن | Legal/Compliance authority | `POST /api/v1/governance/legal-holds/{id}/actions/extend` | POL-LHD-EXTEND |

**القصة:** بصفتي **Legal/Compliance authority**، أريد **تمديد التجميد القانوني**، لكي يتحقق غرض التجميد القانوني: تجميد قانوني يمنع إتلاف ومحو ما يشمله

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ added scope items; reason
- **المدخلات:** `scope`!: array, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-LHD-EXTENDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Legal/Compliance authority (place, extend, request/approve/cancel release)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-LHD-EXTEND` · `AGG-LEGAL-HOLD` · متطلبات: REQ-GOV-007 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-UPD، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-LHD-EXTEND succeeds
  Given AGG-LEGAL-HOLD in state ACTIVE and every guard holds
  When Legal/Compliance authority sends CMD-LHD-EXTEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-LHD-EXTENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-LHD-EXTEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-LHD-EXTEND لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | HOLD_INVALID | 422 | لم يتحقق الشرط: added scope items; reason |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LEGAL_HOLD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RELEASED, RELEASE_REQUESTED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: scope, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-LHD-PLACE — إنشاء التجميد القانوني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | Legal/Compliance authority | `POST /api/v1/governance/legal-holds` | POL-LHD-PLACE |

**القصة:** بصفتي **Legal/Compliance authority**، أريد **إنشاء التجميد القانوني**، لكي يتحقق غرض التجميد القانوني: تجميد قانوني يمنع إتلاف ومحو ما يشمله

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ Legal/Compliance authority; scope = any of: record classes, object URNs, data subjects, org units, time range; legal reference
- **المدخلات:** `name`!: string, `legal_reference`!: string, `scope`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-LHD-PLACED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Legal/Compliance authority (place, extend, request/approve/cancel release)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-LHD-PLACE` · `AGG-LEGAL-HOLD` · متطلبات: REQ-GOV-007 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-LHD-PLACE succeeds
  Given AGG-LEGAL-HOLD in state ∅ and every guard holds
  When Legal/Compliance authority sends CMD-LHD-PLACE with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-LHD-PLACED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-LHD-PLACE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-LHD-PLACE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | HOLD_INVALID | 422 | لم يتحقق الشرط: Legal/Compliance authority; scope = any of: record classes, object URNs, data subjects, org units, time range; legal reference |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: name, legal_reference, scope |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-LHD-REQUEST-RELEASE — طلب إصدار التجميد القانوني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Legal/Compliance authority | `POST /api/v1/governance/legal-holds/{id}/actions/request-release` | POL-LHD-REQUEST-RELEASE |

**القصة:** بصفتي **Legal/Compliance authority**، أريد **طلب إصدار التجميد القانوني**، لكي يتحقق غرض التجميد القانوني: تجميد قانوني يمنع إتلاف ومحو ما يشمله

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ reason; requester = Legal authority
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← RELEASE_REQUESTED؛ الحدث EVT-LHD-RELEASE-REQUESTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Legal/Compliance authority (place, extend, request/approve/cancel release)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-LHD-REQUEST-RELEASE` · `AGG-LEGAL-HOLD` · متطلبات: REQ-GOV-007 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-LHD-REQUEST-RELEASE succeeds
  Given AGG-LEGAL-HOLD in state ACTIVE and every guard holds
  When Legal/Compliance authority sends CMD-LHD-REQUEST-RELEASE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RELEASE_REQUESTED
  And EVT-LHD-RELEASE-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-LHD-REQUEST-RELEASE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-LHD-REQUEST-RELEASE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LEGAL_HOLD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RELEASED, RELEASE_REQUESTED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-Q-LHD-CHECK — جلب: HoldCheck OHS: URNs / subjects / (class, bucket) → held? with hold ids

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | owner contexts (workload identity); Archivist | `POST /api/v1/governance/hold-checks` | POL-LHD-CHECK |

**القصة:** بصفتي **owner contexts (workload identity); Archivist**، أريد **جلب HoldCheck OHS: URNs / subjects / (class, bucket) → held? with hold ids**، لكي يتحقق المتطلب: When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modification until the hold is released

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** HoldCheck OHS: URNs / subjects / (class, bucket) → held? with hold ids
- **الصلاحية:** owner contexts (workload identity); Archivist؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-LHD-CHECK` · `AGG-LEGAL-HOLD` · متطلبات: REQ-GOV-007
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-LHD-CHECK returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-LHD-CHECK
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-LHD-CHECK is denied
  Given the policy denies the caller
  When the caller sends QRY-LHD-CHECK
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC08-Q-LHD-LIST — جلب: Holds by state and scope

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | Legal, Archivist, Auditor | `GET /api/v1/governance/legal-holds` | POL-LHD-LIST |

**القصة:** بصفتي **Legal, Archivist, Auditor**، أريد **جلب Holds by state and scope**، لكي يتحقق المتطلب: When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modification until the hold is released

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Holds by state and scope؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Legal, Archivist, Auditor؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-LHD-LIST` · `AGG-LEGAL-HOLD` · متطلبات: REQ-GOV-007
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-LHD-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-LHD-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-LHD-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-LHD-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-POLICY-SET — مجموعة السياسات (Policy Set Version)

`03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md` · SLC-01 · الحالات: DRAFT, IN_REVIEW, APPROVED, ACTIVE → SUPERSEDED, REJECTED

#### US-BC08-POL-APPROVE — اعتماد مجموعة السياسات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Security Officer | `POST /api/v1/governance/policy-sets/{id}/actions/approve` | POL-POL-APPROVE |

**القصة:** بصفتي **Security Officer**، أريد **اعتماد مجموعة السياسات**، لكي يتحقق غرض مجموعة السياسات: مجموعة سياسات مستأجر (جداول قرار) بإصدارات

- **الشروط المسبقة:** الحالة الحالية ∈ {IN_REVIEW}؛ approver ≠ author; Security Officer
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← APPROVED؛ الحدث EVT-POL-APPROVED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: approver ≠ author؛ الالتزامات: audit; mfa
- **الربط:** `CMD-POL-APPROVE` · `AGG-POLICY-SET` · متطلبات: REQ-FND-011, REQ-FND-012, REQ-GOV-009 · حالات استخدام: UC-086
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-POL-APPROVE succeeds
  Given AGG-POLICY-SET in state IN_REVIEW and every guard holds
  When Security Officer sends CMD-POL-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes APPROVED
  And EVT-POL-APPROVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-POL-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-POL-APPROVE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | POLICY_SET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, APPROVED, DRAFT, REJECTED, SUPERSEDED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-POL-DRAFT — إعداد مسودة مجموعة السياسات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | Security Officer | `POST /api/v1/governance/policy-sets` | POL-POL-DRAFT |

**القصة:** بصفتي **Security Officer**، أريد **إعداد مسودة مجموعة السياسات**، لكي يتحقق غرض مجموعة السياسات: مجموعة سياسات مستأجر (جداول قرار) بإصدارات

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ Security Officer
- **المدخلات:** `based_on`: urn — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-POL-DRAFTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-POL-DRAFT` · `AGG-POLICY-SET` · متطلبات: REQ-FND-011, REQ-FND-012, REQ-GOV-009 · حالات استخدام: UC-086
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-POL-DRAFT succeeds
  Given AGG-POLICY-SET in state ∅ and every guard holds
  When Security Officer sends CMD-POL-DRAFT with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-POL-DRAFTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-POL-DRAFT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-POL-DRAFT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-POL-EDIT — تعديل مجموعة السياسات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | حوكمة وأمن | Security Officer | `POST /api/v1/governance/policy-sets/{id}/actions/edit` | POL-POL-EDIT |

**القصة:** بصفتي **Security Officer**، أريد **تعديل مجموعة السياسات**، لكي يتحقق غرض مجموعة السياسات: مجموعة سياسات مستأجر (جداول قرار) بإصدارات

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ tables validate against schema
- **المدخلات:** `decision_tables`!: array, `tests`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-POL-EDITED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-POL-EDIT` · `AGG-POLICY-SET` · متطلبات: REQ-FND-011, REQ-FND-012, REQ-GOV-009 · حالات استخدام: UC-086
- **ضوابط النوع والفئة:** C-UPD، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-POL-EDIT succeeds
  Given AGG-POLICY-SET in state DRAFT and every guard holds
  When Security Officer sends CMD-POL-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-POL-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-POL-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-POL-EDIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | POLICY_INVALID | 422 | لم يتحقق الشرط: tables validate against schema |
    | POLICY_SET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, APPROVED, IN_REVIEW, REJECTED, SUPERSEDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: decision_tables, tests |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-POL-REJECT — رفض مجموعة السياسات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Security Officer | `POST /api/v1/governance/policy-sets/{id}/actions/reject` | POL-POL-REJECT |

**القصة:** بصفتي **Security Officer**، أريد **رفض مجموعة السياسات**، لكي يتحقق غرض مجموعة السياسات: مجموعة سياسات مستأجر (جداول قرار) بإصدارات

- **الشروط المسبقة:** الحالة الحالية ∈ {IN_REVIEW}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-POL-REJECTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-POL-REJECT` · `AGG-POLICY-SET` · متطلبات: REQ-FND-011, REQ-FND-012, REQ-GOV-009 · حالات استخدام: UC-086
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-POL-REJECT succeeds
  Given AGG-POLICY-SET in state IN_REVIEW and every guard holds
  When Security Officer sends CMD-POL-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-POL-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-POL-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-POL-REJECT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | POLICY_SET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, APPROVED, DRAFT, REJECTED, SUPERSEDED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-POL-SUBMIT — تقديم مجموعة السياسات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Security Officer | `POST /api/v1/governance/policy-sets/{id}/actions/submit` | POL-POL-SUBMIT |

**القصة:** بصفتي **Security Officer**، أريد **تقديم مجموعة السياسات**، لكي يتحقق غرض مجموعة السياسات: مجموعة سياسات مستأجر (جداول قرار) بإصدارات

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ embedded policy tests all pass; tenant rules only restrict platform baseline
- **المدخلات:** `effective_from`!: date-time — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← IN_REVIEW؛ الحدث EVT-POL-SUBMITTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-POL-SUBMIT` · `AGG-POLICY-SET` · متطلبات: REQ-FND-011, REQ-FND-012, REQ-GOV-009 · حالات استخدام: UC-086
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-POL-SUBMIT succeeds
  Given AGG-POLICY-SET in state DRAFT and every guard holds
  When Security Officer sends CMD-POL-SUBMIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_REVIEW
  And EVT-POL-SUBMITTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-POL-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-POL-SUBMIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | POLICY_SET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, APPROVED, IN_REVIEW, REJECTED, SUPERSEDED |
    | POLICY_TESTS_FAILED | 422 | لم يتحقق الشرط: embedded policy tests all pass; tenant rules only restrict platform baseline |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: effective_from |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-S-POLICY-SET-01 — تلقائي: effective_from reached (مجموعة السياسات)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | APPROVED | ACTIVE |

**القصة:** بصفتي **النظام**، عند «effective_from reached»، أريد نقل **مجموعة السياسات** إلى ACTIVE، لكي يتحقق غرض مجموعة السياسات: مجموعة سياسات مستأجر (جداول قرار) بإصدارات

- **الشرط:** scheduler; previous ACTIVE → SUPERSEDED
- **المخرجات:** الحدث EVT-POL-ACTIVATED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-POLICY-SET` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-S-POLICY-SET-02 — تلقائي: successor activated (مجموعة السياسات)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ACTIVE | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «successor activated»، أريد نقل **مجموعة السياسات** إلى SUPERSEDED، لكي يتحقق غرض مجموعة السياسات: مجموعة سياسات مستأجر (جداول قرار) بإصدارات

- **الشرط:** system
- **المخرجات:** الحدث EVT-POL-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-POLICY-SET` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-Q-POL-GET — جلب: Policy set version with tables and tests

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | Security Officer, Auditor | `GET /api/v1/governance/policy-sets/{version_id}` | POL-POL-GET |

**القصة:** بصفتي **Security Officer, Auditor**، أريد **جلب Policy set version with tables and tests**، لكي يتحقق المتطلب: The system shall version, audit and time-stamp every policy and configuration change and apply each change from its effective time

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Policy set version with tables and tests
- **الصلاحية:** Security Officer, Auditor؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-POL-GET` · `AGG-POLICY-SET` · متطلبات: REQ-GOV-009
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-POL-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-POL-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-POL-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-POL-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-RETENTION-SCHEDULE — جدول الاحتفاظ (Retention Schedule Version)

`03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md` · SLC-12a · الحالات: DRAFT, ACTIVE → SUPERSEDED, DISCARDED

#### US-BC08-RTS-ACTIVATE — تفعيل جدول الاحتفاظ

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Legal/Compliance authority | `POST /api/v1/governance/retention-schedules/{id}/actions/activate` | POL-RTS-ACTIVATE |

**القصة:** بصفتي **Legal/Compliance authority**، أريد **تفعيل جدول الاحتفاظ**، لكي يتحقق غرض جدول الاحتفاظ: جدول الاحتفاظ لكل مستأجر: لكل فئة سجلات مدة ومحفز وإجراء إتلاف وأساس قانوني

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ every record class in RD-RECORD-CLASSES has exactly one rule (REQ-GOV-006); approver = Legal/Compliance authority ≠ drafter; previous ACTIVE → SUPERSEDED in the same transaction
- **المدخلات:** `effective_from`!: date-time, `retroactive_classes`: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-RTS-ACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Archivist (draft, edit, discard) · Legal/Compliance authority (activate)؛ الشروط: tenant match؛ فصل المهام: approver ≠ drafter؛ الالتزامات: audit; mfa
- **الربط:** `CMD-RTS-ACTIVATE` · `AGG-RETENTION-SCHEDULE` · متطلبات: REQ-GOV-006 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RTS-ACTIVATE succeeds
  Given AGG-RETENTION-SCHEDULE in state DRAFT and every guard holds
  When Legal/Compliance authority sends CMD-RTS-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-RTS-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RTS-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RTS-ACTIVATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISCARDED, SUPERSEDED |
    | SCHEDULE_INCOMPLETE | 422 | لم يتحقق الشرط: every record class in RD-RECORD-CLASSES has exactly one rule (REQ-GOV-006); approver = Legal/Compliance authority ≠ drafter; previous ACTIVE → SUPERSEDED in the same transaction |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: effective_from |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-RTS-DISCARD — تجاهل مسودة جدول الاحتفاظ

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Archivist | `POST /api/v1/governance/retention-schedules/{id}/actions/discard` | POL-RTS-DISCARD |

**القصة:** بصفتي **Archivist**، أريد **تجاهل مسودة جدول الاحتفاظ**، لكي يتحقق غرض جدول الاحتفاظ: جدول الاحتفاظ لكل مستأجر: لكل فئة سجلات مدة ومحفز وإجراء إتلاف وأساس قانوني

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DISCARDED؛ الحدث EVT-RTS-DISCARDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Archivist (draft, edit, discard) · Legal/Compliance authority (activate)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-RTS-DISCARD` · `AGG-RETENTION-SCHEDULE` · متطلبات: REQ-GOV-006 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RTS-DISCARD succeeds
  Given AGG-RETENTION-SCHEDULE in state DRAFT and every guard holds
  When Archivist sends CMD-RTS-DISCARD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISCARDED
  And EVT-RTS-DISCARDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RTS-DISCARD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RTS-DISCARD لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISCARDED, SUPERSEDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-RTS-DRAFT — إعداد مسودة جدول الاحتفاظ

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | Archivist | `POST /api/v1/governance/retention-schedules` | POL-RTS-DRAFT |

**القصة:** بصفتي **Archivist**، أريد **إعداد مسودة جدول الاحتفاظ**، لكي يتحقق غرض جدول الاحتفاظ: جدول الاحتفاظ لكل مستأجر: لكل فئة سجلات مدة ومحفز وإجراء إتلاف وأساس قانوني

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ Archivist; ≤ 1 DRAFT per tenant
- **المدخلات:** `based_on`: urn — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-RTS-DRAFTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Archivist (draft, edit, discard) · Legal/Compliance authority (activate)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-RTS-DRAFT` · `AGG-RETENTION-SCHEDULE` · متطلبات: REQ-GOV-006 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RTS-DRAFT succeeds
  Given AGG-RETENTION-SCHEDULE in state ∅ and every guard holds
  When Archivist sends CMD-RTS-DRAFT with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-RTS-DRAFTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RTS-DRAFT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RTS-DRAFT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DRAFT_EXISTS | 422 | لم يتحقق الشرط: Archivist; ≤ 1 DRAFT per tenant |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-RTS-EDIT — تعديل جدول الاحتفاظ

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | حوكمة وأمن | Archivist | `POST /api/v1/governance/retention-schedules/{id}/actions/edit` | POL-RTS-EDIT |

**القصة:** بصفتي **Archivist**، أريد **تعديل جدول الاحتفاظ**، لكي يتحقق غرض جدول الاحتفاظ: جدول الاحتفاظ لكل مستأجر: لكل فئة سجلات مدة ومحفز وإجراء إتلاف وأساس قانوني

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ each rule: record class (RD-RECORD-CLASSES), period (ISO 8601 duration), trigger ∈ {recorded, closed, superseded, event}, action ∈ {DESTROY, REVIEW, ARCHIVE (R2)}, legal basis
- **المدخلات:** `rules`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-RTS-EDITED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Archivist (draft, edit, discard) · Legal/Compliance authority (activate)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-RTS-EDIT` · `AGG-RETENTION-SCHEDULE` · متطلبات: REQ-GOV-006 · حالات استخدام: UC-103
- **ضوابط النوع والفئة:** C-UPD، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RTS-EDIT succeeds
  Given AGG-RETENTION-SCHEDULE in state DRAFT and every guard holds
  When Archivist sends CMD-RTS-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-RTS-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RTS-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RTS-EDIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISCARDED, SUPERSEDED |
    | SCHEDULE_INVALID | 422 | لم يتحقق الشرط: each rule: record class (RD-RECORD-CLASSES), period (ISO 8601 duration), trigger ∈ {recorded, closed, superseded, event}, action ∈ {DESTROY, REVIEW, ARCHIVE (R2)}, legal basis |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: rules |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-S-RETENTION-SCHEDULE-01 — تلقائي: successor activated (جدول الاحتفاظ)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ACTIVE | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «successor activated»، أريد نقل **جدول الاحتفاظ** إلى SUPERSEDED، لكي يتحقق غرض جدول الاحتفاظ: جدول الاحتفاظ لكل مستأجر: لكل فئة سجلات مدة ومحفز وإجراء إتلاف وأساس قانوني

- **الشرط:** system
- **المخرجات:** الحدث EVT-RTS-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-RETENTION-SCHEDULE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-Q-RTS-ACTIVE — جلب: Active schedule version with rules

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | Archivist, Legal, Auditor | `GET /api/v1/governance/retention-schedule` | POL-RTS-ACTIVE |

**القصة:** بصفتي **Archivist, Legal, Auditor**، أريد **جلب Active schedule version with rules**، لكي يتحقق المتطلب: The system shall apply a retention schedule to every record class

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Active schedule version with rules؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Archivist, Legal, Auditor؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-RTS-ACTIVE` · `AGG-RETENTION-SCHEDULE` · متطلبات: REQ-GOV-006
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-RTS-ACTIVE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-RTS-ACTIVE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-RTS-ACTIVE is denied
  Given the policy denies the caller
  When the caller sends QRY-RTS-ACTIVE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-SECURITY-EXCEPTION — الاستثناء الأمني (Security Exception)

`03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md` · SLC-01 · الحالات: REQUESTED, FIRST_APPROVED, ACTIVE → REJECTED, EXPIRED, REVOKED

#### US-BC08-EXC-APPROVE — اعتماد الاستثناء الأمني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | authenticated user (request) \| Security Officer (approve/reject/revoke) | `POST /api/v1/governance/security-exceptions/{id}/actions/approve` | POL-EXC-APPROVE |

**القصة:** بصفتي **authenticated user (request) \| Security Officer (approve/reject/revoke)**، أريد **اعتماد الاستثناء الأمني**، لكي يتحقق غرض الاستثناء الأمني: استثناء مؤقت من سياسة مستأجر بموافقة شخصين

- **الشروط المسبقة:** الحالة الحالية ∈ {FIRST_APPROVED, REQUESTED}؛ approver authorized; approver ∉ {requester, first approver}؛ approver authorized; approver ≠ requester
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE, FIRST_APPROVED؛ الحدث EVT-EXC-ACTIVATED, EVT-EXC-FIRST-APPROVED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** authenticated user (request) \| Security Officer (approve/reject/revoke)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: approver ∉ {requester, first approver}؛ الالتزامات: audit; mfa
- **الربط:** `CMD-EXC-APPROVE` · `AGG-SECURITY-EXCEPTION` · متطلبات: REQ-FND-017 · حالات استخدام: UC-088
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EXC-APPROVE succeeds
  Given AGG-SECURITY-EXCEPTION in state FIRST_APPROVED or REQUESTED and every guard holds
  When authenticated user sends CMD-EXC-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE or FIRST_APPROVED
  And EVT-EXC-ACTIVATED, EVT-EXC-FIRST-APPROVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EXC-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EXC-APPROVE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, EXPIRED, REJECTED, REVOKED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ∉ {requester, first approver} |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-EXC-REJECT — رفض الاستثناء الأمني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | authenticated user (request) \| Security Officer (approve/reject/revoke) | `POST /api/v1/governance/security-exceptions/{id}/actions/reject` | POL-EXC-REJECT |

**القصة:** بصفتي **authenticated user (request) \| Security Officer (approve/reject/revoke)**، أريد **رفض الاستثناء الأمني**، لكي يتحقق غرض الاستثناء الأمني: استثناء مؤقت من سياسة مستأجر بموافقة شخصين

- **الشروط المسبقة:** الحالة الحالية ∈ {FIRST_APPROVED, REQUESTED}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-EXC-REJECTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** authenticated user (request) \| Security Officer (approve/reject/revoke)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EXC-REJECT` · `AGG-SECURITY-EXCEPTION` · متطلبات: REQ-FND-017 · حالات استخدام: UC-088
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EXC-REJECT succeeds
  Given AGG-SECURITY-EXCEPTION in state FIRST_APPROVED or REQUESTED and every guard holds
  When authenticated user sends CMD-EXC-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-EXC-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EXC-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EXC-REJECT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, EXPIRED, REJECTED, REVOKED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-EXC-REQUEST — طلب الاستثناء الأمني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | authenticated user \| Security Officer | `POST /api/v1/governance/security-exceptions` | POL-EXC-REQUEST |

**القصة:** بصفتي **authenticated user \| Security Officer**، أريد **طلب الاستثناء الأمني**، لكي يتحقق غرض الاستثناء الأمني: استثناء مؤقت من سياسة مستأجر بموافقة شخصين

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ targets a tenant policy rule (not platform baseline); duration ≤ 30 days; justification
- **المدخلات:** `policy_rule`!: string, `subject_scope`!: object, `justification`!: string, `starts_at`!: date-time, `ends_at`!: date-time — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REQUESTED؛ الحدث EVT-EXC-REQUESTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** authenticated user (request) \| Security Officer (approve/reject/revoke)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EXC-REQUEST` · `AGG-SECURITY-EXCEPTION` · متطلبات: REQ-FND-017 · حالات استخدام: UC-088
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EXC-REQUEST succeeds
  Given AGG-SECURITY-EXCEPTION in state ∅ and every guard holds
  When authenticated user | Security Officer sends CMD-EXC-REQUEST with a valid payload, a new Idempotency-Key
  Then the state becomes REQUESTED
  And EVT-EXC-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EXC-REQUEST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EXC-REQUEST لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | EXCEPTION_NOT_ALLOWED | 422 | لم يتحقق الشرط: targets a tenant policy rule (not platform baseline); duration ≤ 30 days; justification |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: policy_rule, subject_scope, justification, starts_at, ends_at |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-EXC-REVOKE — سحب الاستثناء الأمني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | authenticated user (request) \| Security Officer (approve/reject/revoke) | `POST /api/v1/governance/security-exceptions/{id}/actions/revoke` | POL-EXC-REVOKE |

**القصة:** بصفتي **authenticated user (request) \| Security Officer (approve/reject/revoke)**، أريد **سحب الاستثناء الأمني**، لكي يتحقق غرض الاستثناء الأمني: استثناء مؤقت من سياسة مستأجر بموافقة شخصين

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ Security Officer; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REVOKED؛ الحدث EVT-EXC-REVOKED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** authenticated user (request) \| Security Officer (approve/reject/revoke)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EXC-REVOKE` · `AGG-SECURITY-EXCEPTION` · متطلبات: REQ-FND-017 · حالات استخدام: UC-088
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EXC-REVOKE succeeds
  Given AGG-SECURITY-EXCEPTION in state ACTIVE and every guard holds
  When authenticated user sends CMD-EXC-REVOKE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REVOKED
  And EVT-EXC-REVOKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EXC-REVOKE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EXC-REVOKE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, FIRST_APPROVED, REJECTED, REQUESTED, REVOKED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC08-S-SECURITY-EXCEPTION-01 — تلقائي: end reached (الاستثناء الأمني)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | ACTIVE | EXPIRED |

**القصة:** بصفتي **النظام**، عند «end reached»، أريد نقل **الاستثناء الأمني** إلى EXPIRED، لكي يتحقق غرض الاستثناء الأمني: استثناء مؤقت من سياسة مستأجر بموافقة شخصين

- **الشرط:** scheduler
- **المخرجات:** الحدث EVT-EXC-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-SECURITY-EXCEPTION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC08-Q-EXC-LIST — جلب: Exceptions by state

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | Security Officer, Auditor | `GET /api/v1/governance/security-exceptions` | POL-EXC-LIST |

**القصة:** بصفتي **Security Officer, Auditor**، أريد **جلب Exceptions by state**، لكي يتحقق المتطلب: When a security exception is requested, the system shall require approval by two distinct authorized persons and shall revoke the exception automatically at its expiry

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Exceptions by state؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Security Officer, Auditor؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-EXC-LIST` · `AGG-SECURITY-EXCEPTION` · متطلبات: REQ-FND-017
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-EXC-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-EXC-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-EXC-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-EXC-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### استعلامات عابرة للـAggregates

#### US-BC08-Q-AUD-SEARCH — جلب: Audit records by actor, resource, time, correlation id

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | Auditor, Security Officer (itself audited) | `GET /api/v1/governance/audit-records` | POL-AUD-SEARCH |

**القصة:** بصفتي **Auditor, Security Officer (itself audited)**، أريد **جلب Audit records by actor, resource, time, correlation id**، لكي يتحقق المتطلب: The system shall write an audit record for every state-changing command and for every read of data classified at or above the tenant's audit threshold, containing actor, action, resource, purpose, policy decision, time and correlation id

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Audit records by actor, resource, time, correlation id؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Auditor, Security Officer (itself audited)؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AUD-SEARCH` · عابر للـAggregates · متطلبات: REQ-FND-015
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-AUD-SEARCH returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-AUD-SEARCH with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-AUD-SEARCH is denied
  Given the policy denies the caller
  When the caller sends QRY-AUD-SEARCH
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC08-Q-AUD-VERIFY — جلب: Start integrity verification job; returns job ref

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | Auditor | `POST /api/v1/governance/audit-integrity-checks` | POL-AUD-VERIFY |

**القصة:** بصفتي **Auditor**، أريد **جلب Start integrity verification job; returns job ref**، لكي يتحقق المتطلب: The system shall keep audit records append-only and tamper-evident

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Start integrity verification job; returns job ref
- **الصلاحية:** Auditor؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AUD-VERIFY` · عابر للـAggregates · متطلبات: REQ-FND-016
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-AUD-VERIFY returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-AUD-VERIFY
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-AUD-VERIFY is denied
  Given the policy denies the caller
  When the caller sends QRY-AUD-VERIFY
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC08-Q-PDP-DECIDE — جلب: DecisionRequest → DecisionResponse (authorization-model §2)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | internal PEPs only (workload identity) | `POST /api/v1/governance/policy-decisions` | POL-PDP-DECIDE |

**القصة:** بصفتي **internal PEPs only (workload identity)**، أريد **جلب DecisionRequest → DecisionResponse (authorization-model §2)**، لكي يتحقق المتطلب: The system shall evaluate authorization before retrieving data for every command, query, search, map request, export, event subscription and AI retrieval

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** DecisionRequest → DecisionResponse (authorization-model §2)
- **الصلاحية:** internal PEPs only (workload identity)؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-PDP-DECIDE` · عابر للـAggregates · متطلبات: REQ-FND-010
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-PDP-DECIDE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-PDP-DECIDE
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-PDP-DECIDE is denied
  Given the policy denies the caller
  When the caller sends QRY-PDP-DECIDE
  Then the response has the same shape as for a missing item (not-found shape)
```

<!-- END GENERATED: build_analysis_design.py -->
