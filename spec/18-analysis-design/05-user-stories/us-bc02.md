---
id: AD-05-US-BC02
type: user-stories
title: "قصص المستخدم — BC02"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
generator: 17-system-study/_build/build_analysis_design.py
---

# قصص المستخدم — BC02 Information — نواة المعلومات

مولَّد بالكامل من المصادر بواسطة `17-system-study/_build/build_analysis_design.py`؛ لا يُحرَّر يدويًا. القالب والتصنيف وتعريف ضوابط النوع والفئة في [00-guide.md](00-guide.md).

<!-- BEGIN GENERATED: build_analysis_design.py -->

## ملخص BC02

| نوع العملية | عدد القصص |
|---|---|
| إنشاء | 18 |
| تعديل | 26 |
| جلب | 27 |
| حذف / إنهاء | 21 |
| سير عمل | 27 |
| نظام (SYS) | 17 |
| **المجموع** | **136** |

### AGG-ATTACHMENT — المرفق (Attachment)

`03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md` · SLC-02 · الحالات: PENDING, SCANNING, STORED → QUARANTINED, EXPIRED, ERASED

#### US-BC02-ATT-COMPLETE-UPLOAD — إكمال رفع المرفق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | user with write permission on the target object | `POST /api/v1/information/attachments/{id}/actions/complete-upload` | POL-ATT-COMPLETE-UPLOAD |

**القصة:** بصفتي **user with write permission on the target object**، أريد **إكمال رفع المرفق**، لكي يتحقق غرض المرفق: ملف في Object Storage، معنون بالمحتوى، يُرفع ويُنزّل مباشرة

- **الشروط المسبقة:** الحالة الحالية: PENDING؛ stored bytes hash = declared sha256; size matches
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SCANNING؛ الحدث EVT-ATT-UPLOADED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** user with write permission on the target object؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ATT-COMPLETE-UPLOAD` · `AGG-ATTACHMENT` · متطلبات: REQ-INF-003, REQ-INF-004, REQ-GOV-008 · حالات استخدام: UC-005, UC-006, UC-103
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ATT-COMPLETE-UPLOAD succeeds
  Given AGG-ATTACHMENT in state PENDING and every guard holds
  When user with write permission on the target object sends CMD-ATT-COMPLETE-UPLOAD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SCANNING
  And EVT-ATT-UPLOADED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ATT-COMPLETE-UPLOAD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ATTACHMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ERASED, EXPIRED, QUARANTINED, SCANNING, STORED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ATT-COMPLETE-UPLOAD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | HASH_MISMATCH | 422 | لم يتحقق الشرط: stored bytes hash = declared sha256 |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ATT-ERASE — محو المرفق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | user with write permission on the target object | `POST /api/v1/information/attachments/{id}/actions/erase` | POL-ATT-ERASE |

**القصة:** بصفتي **user with write permission on the target object**، أريد **محو المرفق**، لكي يتحقق غرض المرفق: ملف في Object Storage، معنون بالمحتوى، يُرفع ويُنزّل مباشرة

- **الشروط المسبقة:** الحالة الحالية: STORED؛ erasure order or disposition; no legal hold; key destroyed (ADR-P08)
- **المدخلات:** `erasure_order_ref`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ERASED؛ الحدث EVT-ATT-ERASED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** user with write permission on the target object؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit; mfa; legal-hold check
- **الربط:** `CMD-ATT-ERASE` · `AGG-ATTACHMENT` · متطلبات: REQ-INF-003, REQ-INF-004, REQ-GOV-008 · حالات استخدام: UC-005, UC-006, UC-103
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ATT-ERASE succeeds
  Given AGG-ATTACHMENT in state STORED and every guard holds
  When user with write permission on the target object sends CMD-ATT-ERASE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ERASED
  And EVT-ATT-ERASED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ATT-ERASE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ATTACHMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ERASED, EXPIRED, PENDING, QUARANTINED, SCANNING |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ATT-ERASE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LEGAL_HOLD_ACTIVE | 422 | لم يتحقق الشرط: no legal hold |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: erasure_order_ref |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
    | MFA_STEP_UP_REQUIRED | 401 | التزام mfa في POL-ATT-ERASE وقوة مصادقة الجلسة أقل من المطلوب؛ يُعاد الطلب بعد المصادقة المعززة بنفس Idempotency-Key (ADR-P19، الخطوة 6) |
```

#### US-BC02-ATT-INITIATE-UPLOAD — بدء رفع المرفق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | user with write permission on the target object | `POST /api/v1/information/attachments` | POL-ATT-INITIATE-UPLOAD |

**القصة:** بصفتي **user with write permission on the target object**، أريد **بدء رفع المرفق**، لكي يتحقق غرض المرفق: ملف في Object Storage، معنون بالمحتوى، يُرفع ويُنزّل مباشرة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ size ≤ tenant limit; mime allowed; returns direct upload target (≤ 5 min); same sha256 already STORED in tenant → returns existing
- **المدخلات:** `client_id`: string, `sha256`!: string, `size_bytes`!: integer, `mime_type`!: string, `file_name`: string, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← PENDING؛ الحدث EVT-ATT-UPLOAD-INITIATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** user with write permission on the target object؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ATT-INITIATE-UPLOAD` · `AGG-ATTACHMENT` · متطلبات: REQ-INF-003, REQ-INF-004, REQ-GOV-008 · حالات استخدام: UC-005, UC-006, UC-103
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ATT-INITIATE-UPLOAD succeeds
  Given AGG-ATTACHMENT does not exist yet and every guard holds
  When user with write permission on the target object sends CMD-ATT-INITIATE-UPLOAD with a valid payload, a new Idempotency-Key
  Then the state becomes PENDING
  And EVT-ATT-UPLOAD-INITIATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ATT-INITIATE-UPLOAD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ATTACHMENT_REJECTED | 422 | لم يتحقق الشرط: size ≤ tenant limit; mime allowed; returns direct upload target (≤ 5 min); same sha256 already STORED in tenant → returns existing |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ATT-INITIATE-UPLOAD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: sha256, size_bytes, mime_type, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-S-ATTACHMENT-01 — تلقائي: scan passed (المرفق)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | SCANNING | STORED |

**القصة:** بصفتي **النظام**، عند «scan passed»، أريد نقل **المرفق** إلى STORED، لكي يتحقق غرض المرفق: ملف في Object Storage، معنون بالمحتوى، يُرفع ويُنزّل مباشرة

- **الشرط:** offline content scanner + format validation
- **المخرجات:** الحدث EVT-ATT-STORED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ATTACHMENT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-S-ATTACHMENT-02 — تلقائي: scan failed (المرفق)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | SCANNING | QUARANTINED |

**القصة:** بصفتي **النظام**، عند «scan failed»، أريد نقل **المرفق** إلى QUARANTINED، لكي يتحقق غرض المرفق: ملف في Object Storage، معنون بالمحتوى، يُرفع ويُنزّل مباشرة

- **الشرط:** scanner verdict
- **المخرجات:** الحدث EVT-ATT-QUARANTINED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ATTACHMENT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-S-ATTACHMENT-03 — تلقائي: upload window 24 h elapsed (المرفق)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | PENDING | EXPIRED |

**القصة:** بصفتي **النظام**، عند «upload window 24 h elapsed»، أريد نقل **المرفق** إلى EXPIRED، لكي يتحقق غرض المرفق: ملف في Object Storage، معنون بالمحتوى، يُرفع ويُنزّل مباشرة

- **الشرط:** scheduler
- **المخرجات:** الحدث EVT-ATT-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ATTACHMENT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-Q-ATT-DOWNLOAD — جلب: Short-lived signed download target (≤ 5 min); audited

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | authorized on the owning evidence/observation | `POST /api/v1/information/attachments/{attachment_id}/download-grants` | POL-ATT-DOWNLOAD |

**القصة:** بصفتي **authorized on the owning evidence/observation**، أريد **جلب Short-lived signed download target (≤ 5 min); audited**، لكي يتحقق المتطلب: When an attachment is stored or retrieved, the system shall compute or verify its content hash

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Short-lived signed download target (≤ 5 min); audited
- **الصلاحية:** authorized on the owning evidence/observation؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ATT-DOWNLOAD` · `AGG-ATTACHMENT` · متطلبات: REQ-INF-004
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-ATT-DOWNLOAD computes its result only over what the caller may see
  Given data inside and outside the caller's allowed_scope
  When the caller sends QRY-ATT-DOWNLOAD
  Then the result neither includes nor reveals data outside allowed_scope

Scenario: QRY-ATT-DOWNLOAD is denied
  Given the policy denies the caller
  When the caller sends QRY-ATT-DOWNLOAD
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-CLAIM — الادعاء (Claim)

`03-domain/contexts/BC02/aggregates/AGG-CLAIM.md` · SLC-02 · الحالات: CURRENT → CLOSED

#### US-BC02-CLM-ASSERT — تسجيل الادعاء

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst · adapter service account · analysis-run identity | `POST /api/v1/information/claims` | POL-CLM-ASSERT |

**القصة:** بصفتي **Analyst · adapter service account · analysis-run identity**، أريد **تسجيل الادعاء**، لكي يتحقق غرض الادعاء: عبارة (موضوع، سمة، قيمة) مؤرخة ثنائياً ومسندة؛ قيمتها لا تتغير

- **الشروط المسبقة:** الحالة الحالية: ∅؛ subject exists; predicate in RD-PREDICATES; value matches predicate type/unit/cardinality; ≥ 1 source, all ACTIVE; valid_from < valid_to; geometry rules; confidence dims valid
- **المدخلات:** `subject`!: urn, `predicate`!: string, `value`!: ClaimValue, `valid`!: Interval, `source_refs`!: array, `derived_from`: array, `confidence`!: Confidence, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← CURRENT؛ الحدث EVT-CLM-ASSERTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLM-ASSERT` · `AGG-CLAIM` · متطلبات: REQ-INF-021, REQ-INF-022, REQ-INF-024, REQ-INF-026, REQ-INF-037 · حالات استخدام: UC-006
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLM-ASSERT succeeds
  Given AGG-CLAIM does not exist yet and every guard holds
  When an authorized actor (Analyst or adapter service account or analysis-run identity) sends CMD-CLM-ASSERT with a valid payload, a new Idempotency-Key
  Then the state becomes CURRENT
  And EVT-CLM-ASSERTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLM-ASSERT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLM-ASSERT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLAIM_INVALID | 422 | لم يتحقق الشرط: subject exists; predicate in RD-PREDICATES; value matches predicate type/unit/cardinality; ≥ 1 source, all ACTIVE; valid_from < valid_to; geometry rules; confidence dims valid |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: subject, predicate, value, valid, source_refs, confidence, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CLM-ASSESS — تقييم الادعاء

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst or verification re-evaluator system identity | `POST /api/v1/information/claims/{id}/actions/assess` | POL-CLM-ASSESS |

**القصة:** بصفتي **Analyst or verification re-evaluator system identity**، أريد **تقييم الادعاء**، لكي يتحقق غرض الادعاء: عبارة (موضوع، سمة، قيمة) مؤرخة ثنائياً ومسندة؛ قيمتها لا تتغير

- **الشروط المسبقة:** الحالة الحالية: CURRENT؛ updates information_confidence / verification_status only (T2 versioned assessment); value and times untouched
- **المدخلات:** `information_confidence`: enum(1,2,3,4,5,6), `verification_status`: enum(UNVERIFIED,PARTIALLY_VERIFIED,VERIFIED,DISPUTED,REFUTED), `rationale`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CLM-ASSESSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLM-ASSESS` · `AGG-CLAIM` · متطلبات: REQ-INF-021, REQ-INF-022, REQ-INF-024, REQ-INF-026, REQ-INF-037 · حالات استخدام: UC-006
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLM-ASSESS succeeds
  Given AGG-CLAIM in state CURRENT and every guard holds
  When Analyst or verification re-evaluator system identity sends CMD-CLM-ASSESS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-CLM-ASSESSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLM-ASSESS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSESSMENT_INVALID | 422 | لم يتحقق الشرط: updates information_confidence / verification_status only (T2 versioned assessment) |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLM-ASSESS ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLAIM_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CLM-CORRECT — تصحيح الادعاء

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst | `POST /api/v1/information/claims/{id}/actions/correct` | POL-CLM-CORRECT |

**القصة:** بصفتي **Analyst**، أريد **تصحيح الادعاء**، لكي يتحقق غرض الادعاء: عبارة (موضوع، سمة، قيمة) مؤرخة ثنائياً ومسندة؛ قيمتها لا تتغير

- **الشروط المسبقة:** الحالة الحالية: CURRENT؛ closes recorded_to = now and asserts the replacement (same subject/predicate) in the same transaction; reason
- **المدخلات:** `value`!: ClaimValue, `valid`: Interval, `source_refs`!: array, `confidence`!: Confidence, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-CLM-CORRECTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLM-CORRECT` · `AGG-CLAIM` · متطلبات: REQ-INF-021, REQ-INF-022, REQ-INF-024, REQ-INF-026, REQ-INF-037 · حالات استخدام: UC-006
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLM-CORRECT succeeds
  Given AGG-CLAIM in state CURRENT and every guard holds
  When Analyst sends CMD-CLM-CORRECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-CLM-CORRECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLM-CORRECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLM-CORRECT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLAIM_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: value, source_refs, confidence, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CLM-RECLASSIFY — إعادة تصنيف الادعاء

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst · adapter service account | `POST /api/v1/information/claims/{id}/actions/reclassify` | POL-CLM-RECLASSIFY |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **إعادة تصنيف الادعاء**، لكي يتحقق غرض الادعاء: عبارة (موضوع، سمة، قيمة) مؤرخة ثنائياً ومسندة؛ قيمتها لا تتغير

- **الشروط المسبقة:** الحالة الحالية: CURRENT, CLOSED؛ authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CLM-RECLASSIFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLM-RECLASSIFY` · `AGG-CLAIM` · متطلبات: REQ-INF-021, REQ-INF-022, REQ-INF-024, REQ-INF-026, REQ-INF-037 · حالات استخدام: UC-006
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLM-RECLASSIFY succeeds
  Given AGG-CLAIM in state CURRENT or CLOSED and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-CLM-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-CLM-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLM-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLM-RECLASSIFY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLAIM_INVALID_STATE_TRANSITION | 409 | لا حالة في المصفوفة يُرفض منها هذا الأمر؛ الرمز لا يُتوقع حدوثه |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per tenant policy (REQ-GOV-004) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CLM-RECORD-CHANGE — تسجيل تغيير في الادعاء

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst | `POST /api/v1/information/claims/{id}/actions/record-change` | POL-CLM-RECORD-CHANGE |

**القصة:** بصفتي **Analyst**، أريد **تسجيل تغيير في الادعاء**، لكي يتحقق غرض الادعاء: عبارة (موضوع، سمة، قيمة) مؤرخة ثنائياً ومسندة؛ قيمتها لا تتغير

- **الشروط المسبقة:** الحالة الحالية: CURRENT؛ t_change ∈ (valid_from, valid_to): closes record, re-records old value with valid_to = t_change, asserts new value from t_change
- **المدخلات:** `t_change`!: date-time, `new_value`!: ClaimValue, `source_refs`!: array, `confidence`!: Confidence — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-CLM-CHANGED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLM-RECORD-CHANGE` · `AGG-CLAIM` · متطلبات: REQ-INF-021, REQ-INF-022, REQ-INF-024, REQ-INF-026, REQ-INF-037 · حالات استخدام: UC-006
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLM-RECORD-CHANGE succeeds
  Given AGG-CLAIM in state CURRENT and every guard holds
  When Analyst sends CMD-CLM-RECORD-CHANGE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-CLM-CHANGED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLM-RECORD-CHANGE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLM-RECORD-CHANGE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CHANGE_TIME_INVALID | 422 | لم يتحقق الشرط: t_change ∈ (valid_from, valid_to): closes record, re-records old value with valid_to = t_change, asserts new value from t_change |
    | CLAIM_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: t_change, new_value, source_refs, confidence |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CLM-RETRACT — سحب الادعاء

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst | `POST /api/v1/information/claims/{id}/actions/retract` | POL-CLM-RETRACT |

**القصة:** بصفتي **Analyst**، أريد **سحب الادعاء**، لكي يتحقق غرض الادعاء: عبارة (موضوع، سمة، قيمة) مؤرخة ثنائياً ومسندة؛ قيمتها لا تتغير

- **الشروط المسبقة:** الحالة الحالية: CURRENT؛ reason; no replacement
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-CLM-RETRACTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLM-RETRACT` · `AGG-CLAIM` · متطلبات: REQ-INF-021, REQ-INF-022, REQ-INF-024, REQ-INF-026, REQ-INF-037 · حالات استخدام: UC-006
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLM-RETRACT succeeds
  Given AGG-CLAIM in state CURRENT and every guard holds
  When Analyst sends CMD-CLM-RETRACT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-CLM-RETRACTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLM-RETRACT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLM-RETRACT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLAIM_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-Q-CLM-GET — جلب: Claim with sources (per protection), evidence links, supersession chain

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user; label-filtered | `GET /api/v1/information/claims/{claim_id}` | POL-CLM-GET |

**القصة:** بصفتي **any user; label-filtered**، أريد **جلب Claim with sources (per protection), evidence links, supersession chain**، لكي يتحقق المتطلب: The system shall represent each attribute value of an importance-tier T1 object as a claim linked to its sources, evidence and confidence

- **المدخلات:** `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Claim with sources (per protection), evidence links, supersession chain
- **الصلاحية:** any user; label-filtered؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-CLM-GET` · `AGG-CLAIM` · متطلبات: REQ-INF-021
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-CLM-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-CLM-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-CLM-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-CLM-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-COLLECTION-PLAN — خطة الجمع (Collection Plan)

`03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md` · SLC-14 · الحالات: DRAFT, ACTIVE → COMPLETED, CANCELLED

#### US-BC02-CPL-ACTIVATE — تفعيل خطة الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | collection planner | `POST /api/v1/information/collection-plans/{id}/actions/activate` | POL-CPL-ACTIVATE |

**القصة:** بصفتي **collection planner**، أريد **تفعيل خطة الجمع**، لكي يتحقق غرض خطة الجمع: خطة جمع: أنشطة بأساليب ومصادر وفرق، تولّد مهام ميدانية

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ ≥ 1 activity; creates one field task per activity through SLC-03 with plan_ref = this collection plan (CR-59)
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-CPL-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** collection planner؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CPL-ACTIVATE` · `AGG-COLLECTION-PLAN` · متطلبات: REQ-COL-002 · حالات استخدام: UC-121
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CPL-ACTIVATE succeeds
  Given AGG-COLLECTION-PLAN in state DRAFT and every guard holds
  When collection planner sends CMD-CPL-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-CPL-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CPL-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CPL-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CANCELLED, COMPLETED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_EMPTY | 422 | لم يتحقق الشرط: creates one field task per activity through SLC-03 with plan_ref = this collection plan (CR-59) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CPL-ADD-ACTIVITY — إضافة نشاط إلى خطة الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | collection planner | `POST /api/v1/information/collection-plans/{id}/actions/add-activity` | POL-CPL-ADD-ACTIVITY |

**القصة:** بصفتي **collection planner**، أريد **إضافة نشاط إلى خطة الجمع**، لكي يتحقق غرض خطة الجمع: خطة جمع: أنشطة بأساليب ومصادر وفرق، تولّد مهام ميدانية

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE؛ method in RD-COLLECTION-METHODS; source(s) ACTIVE; area ⊆ requirement areas; window ⊆ requirement windows; assigned unit; task type
- **المدخلات:** `method`!: string, `sources`!: array, `area`!: object, `window`!: Interval, `unit`!: urn, `task_type`!: urn, `eei_refs`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CPL-ACTIVITY-ADDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** collection planner؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CPL-ADD-ACTIVITY` · `AGG-COLLECTION-PLAN` · متطلبات: REQ-COL-002 · حالات استخدام: UC-121
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CPL-ADD-ACTIVITY succeeds
  Given AGG-COLLECTION-PLAN in state DRAFT or ACTIVE and every guard holds
  When collection planner sends CMD-CPL-ADD-ACTIVITY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-CPL-ACTIVITY-ADDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CPL-ADD-ACTIVITY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ACTIVITY_INVALID | 422 | لم يتحقق الشرط: source(s) ACTIVE |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CPL-ADD-ACTIVITY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: method, sources, area, window, unit, task_type, eei_refs |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CPL-CANCEL — إلغاء خطة الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | collection planner | `POST /api/v1/information/collection-plans/{id}/actions/cancel` | POL-CPL-CANCEL |

**القصة:** بصفتي **collection planner**، أريد **إلغاء خطة الجمع**، لكي يتحقق غرض خطة الجمع: خطة جمع: أنشطة بأساليب ومصادر وفرق، تولّد مهام ميدانية

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE؛ reason; open tasks cancelled
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-CPL-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** collection planner؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CPL-CANCEL` · `AGG-COLLECTION-PLAN` · متطلبات: REQ-COL-002 · حالات استخدام: UC-121
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CPL-CANCEL succeeds
  Given AGG-COLLECTION-PLAN in state DRAFT or ACTIVE and every guard holds
  When collection planner sends CMD-CPL-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-CPL-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CPL-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CPL-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CPL-COMPLETE — إكمال خطة الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | collection planner | `POST /api/v1/information/collection-plans/{id}/actions/complete` | POL-CPL-COMPLETE |

**القصة:** بصفتي **collection planner**، أريد **إكمال خطة الجمع**، لكي يتحقق غرض خطة الجمع: خطة جمع: أنشطة بأساليب ومصادر وفرق، تولّد مهام ميدانية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ planner; open tasks cancelled with reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← COMPLETED؛ الحدث EVT-CPL-COMPLETED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** collection planner؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CPL-COMPLETE` · `AGG-COLLECTION-PLAN` · متطلبات: REQ-COL-002 · حالات استخدام: UC-121
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CPL-COMPLETE succeeds
  Given AGG-COLLECTION-PLAN in state ACTIVE and every guard holds
  When collection planner sends CMD-CPL-COMPLETE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes COMPLETED
  And EVT-CPL-COMPLETED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CPL-COMPLETE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CPL-COMPLETE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, DRAFT |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CPL-CREATE — إنشاء خطة الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | collection planner | `POST /api/v1/information/collection-plans` | POL-CPL-CREATE |

**القصة:** بصفتي **collection planner**، أريد **إنشاء خطة الجمع**، لكي يتحقق غرض خطة الجمع: خطة جمع: أنشطة بأساليب ومصادر وفرق، تولّد مهام ميدانية

- **الشروط المسبقة:** الحالة الحالية: ∅؛ ≥ 1 APPROVED collection requirement; planner in scope; label ≥ requirements
- **المدخلات:** `requirements`!: array, `title`!: LocalizedName, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-CPL-CREATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** collection planner؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CPL-CREATE` · `AGG-COLLECTION-PLAN` · متطلبات: REQ-COL-002 · حالات استخدام: UC-121
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CPL-CREATE succeeds
  Given AGG-COLLECTION-PLAN does not exist yet and every guard holds
  When collection planner sends CMD-CPL-CREATE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-CPL-CREATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CPL-CREATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CPL-CREATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REQUIREMENT_NOT_APPROVED | 422 | لم يتحقق الشرط: ≥ 1 APPROVED collection requirement; label ≥ requirements |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: requirements, title, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CPL-REMOVE-ACTIVITY — إزالة نشاط من خطة الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | collection planner | `POST /api/v1/information/collection-plans/{id}/actions/remove-activity` | POL-CPL-REMOVE-ACTIVITY |

**القصة:** بصفتي **collection planner**، أريد **إزالة نشاط من خطة الجمع**، لكي يتحقق غرض خطة الجمع: خطة جمع: أنشطة بأساليب ومصادر وفرق، تولّد مهام ميدانية

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ activity not yet tasked
- **المدخلات:** `activity_id`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CPL-ACTIVITY-REMOVED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** collection planner؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CPL-REMOVE-ACTIVITY` · `AGG-COLLECTION-PLAN` · متطلبات: REQ-COL-002 · حالات استخدام: UC-121
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CPL-REMOVE-ACTIVITY succeeds
  Given AGG-COLLECTION-PLAN in state DRAFT and every guard holds
  When collection planner sends CMD-CPL-REMOVE-ACTIVITY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-CPL-ACTIVITY-REMOVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CPL-REMOVE-ACTIVITY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ACTIVITY_ALREADY_TASKED | 422 | لم يتحقق الشرط: activity not yet tasked |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CPL-REMOVE-ACTIVITY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CANCELLED, COMPLETED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: activity_id |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-S-COLLECTION-PLAN-01 — تلقائي: all activity tasks terminal (خطة الجمع)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ACTIVE | COMPLETED |

**القصة:** بصفتي **النظام**، عند «all activity tasks terminal»، أريد نقل **خطة الجمع** إلى COMPLETED، لكي يتحقق غرض خطة الجمع: خطة جمع: أنشطة بأساليب ومصادر وفرق، تولّد مهام ميدانية

- **الشرط:** SLC-03 events
- **المخرجات:** الحدث EVT-CPL-COMPLETED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-COLLECTION-PLAN` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-Q-CPL-GET — جلب: Plan with activities and linked tasks

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | planner scope | `GET /api/v1/information/collection-plans/{plan_id}` | POL-CPL-GET |

**القصة:** بصفتي **planner scope**، أريد **جلب Plan with activities and linked tasks**، لكي يتحقق المتطلب: When a collection requirement is approved, the system shall allow planning collection activities with methods, sources and assigned field tasks

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Plan with activities and linked tasks
- **الصلاحية:** planner scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CPL-GET` · `AGG-COLLECTION-PLAN` · متطلبات: REQ-COL-002
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-CPL-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-CPL-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-CPL-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-CPL-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-COLLECTION-REQUIREMENT — متطلب الجمع (Collection Requirement)

`03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md` · SLC-14 · الحالات: DRAFT, SUBMITTED, APPROVED → REJECTED, SATISFIED, EXPIRED, CANCELLED

#### US-BC02-CRQ-AMEND — تعديل متطلب الجمع بإصدار جديد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | collection manager | `POST /api/v1/information/collection-requirements/{id}/actions/amend` | POL-CRQ-AMEND |

**القصة:** بصفتي **collection manager**، أريد **تعديل متطلب الجمع بإصدار جديد**، لكي يتحقق غرض متطلب الجمع: حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية

- **الشروط المسبقة:** الحالة الحالية: APPROVED؛ approver; extend due, adjust area or EEIs; recorded as new version
- **المدخلات:** `due`: date-time, `area`: object, `eeis`: array, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CRQ-AMENDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRQ-AMEND` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-001, REQ-COL-003 · حالات استخدام: UC-120, UC-122
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRQ-AMEND succeeds
  Given AGG-COLLECTION-REQUIREMENT in state APPROVED and every guard holds
  When collection manager sends CMD-CRQ-AMEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-CRQ-AMENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRQ-AMEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRQ-AMEND ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, DRAFT, EXPIRED, REJECTED, SATISFIED, SUBMITTED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REQUIREMENT_INVALID | 422 | لم يتحقق الشرط: approver; extend due, adjust area or EEIs; recorded as new version |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRQ-APPROVE — اعتماد متطلب الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | collection manager | `POST /api/v1/information/collection-requirements/{id}/actions/approve` | POL-CRQ-APPROVE |

**القصة:** بصفتي **collection manager**، أريد **اعتماد متطلب الجمع**، لكي يتحقق غرض متطلب الجمع: حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية

- **الشروط المسبقة:** الحالة الحالية: SUBMITTED؛ collection manager with authority in the area scope; approver ≠ requester
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← APPROVED؛ الحدث EVT-CRQ-APPROVED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛ الشروط: tenant match; area within scope؛ فصل المهام: approver ≠ requester؛ الالتزامات: audit
- **الربط:** `CMD-CRQ-APPROVE` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-001, REQ-COL-003 · حالات استخدام: UC-120, UC-122
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRQ-APPROVE succeeds
  Given AGG-COLLECTION-REQUIREMENT in state SUBMITTED and every guard holds
  When collection manager sends CMD-CRQ-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes APPROVED
  And EVT-CRQ-APPROVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRQ-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRQ-APPROVE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, CANCELLED, DRAFT, EXPIRED, REJECTED, SATISFIED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ requester |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRQ-CANCEL — إلغاء متطلب الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst / any requester | `POST /api/v1/information/collection-requirements/{id}/actions/cancel` | POL-CRQ-CANCEL |

**القصة:** بصفتي **Analyst / any requester**، أريد **إلغاء متطلب الجمع**، لكي يتحقق غرض متطلب الجمع: حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية

- **الشروط المسبقة:** الحالة الحالية: DRAFT, SUBMITTED, APPROVED؛ requester or approver; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-CRQ-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRQ-CANCEL` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-001, REQ-COL-003 · حالات استخدام: UC-120, UC-122
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRQ-CANCEL succeeds
  Given AGG-COLLECTION-REQUIREMENT in state DRAFT or SUBMITTED or APPROVED and every guard holds
  When Analyst / any requester sends CMD-CRQ-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-CRQ-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRQ-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRQ-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, EXPIRED, REJECTED, SATISFIED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRQ-DRAFT — إعداد مسودة متطلب الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst / any requester | `POST /api/v1/information/collection-requirements` | POL-CRQ-DRAFT |

**القصة:** بصفتي **Analyst / any requester**، أريد **إعداد مسودة متطلب الجمع**، لكي يتحقق غرض متطلب الجمع: حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية

- **الشروط المسبقة:** الحالة الحالية: ∅؛ question; requester; label
- **المدخلات:** `question`!: LocalizedName, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-CRQ-DRAFTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRQ-DRAFT` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-001, REQ-COL-003 · حالات استخدام: UC-120, UC-122
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRQ-DRAFT succeeds
  Given AGG-COLLECTION-REQUIREMENT does not exist yet and every guard holds
  When Analyst / any requester sends CMD-CRQ-DRAFT with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-CRQ-DRAFTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRQ-DRAFT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRQ-DRAFT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REQUIREMENT_INVALID | 422 | لم يتحقق الشرط: question; requester; label |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: question, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRQ-EDIT — تعديل متطلب الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst / any requester | `POST /api/v1/information/collection-requirements/{id}/actions/edit` | POL-CRQ-EDIT |

**القصة:** بصفتي **Analyst / any requester**، أريد **تعديل متطلب الجمع**، لكي يتحقق غرض متطلب الجمع: حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ area polygon, window, priority 1–5, due, essential elements of information (EEIs)
- **المدخلات:** `area`!: object, `window`!: Interval, `priority`!: integer, `due`!: date-time, `eeis`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CRQ-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRQ-EDIT` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-001, REQ-COL-003 · حالات استخدام: UC-120, UC-122
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRQ-EDIT succeeds
  Given AGG-COLLECTION-REQUIREMENT in state DRAFT and every guard holds
  When Analyst / any requester sends CMD-CRQ-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-CRQ-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRQ-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRQ-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, CANCELLED, EXPIRED, REJECTED, SATISFIED, SUBMITTED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REQUIREMENT_INVALID | 422 | لم يتحقق الشرط: area polygon, window, priority 1–5, due, essential elements of information (EEIs) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: area, window, priority, due, eeis |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRQ-MARK-SATISFIED — تعليم متطلب الجمع كمستوفى

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst / any requester | `POST /api/v1/information/collection-requirements/{id}/actions/mark-satisfied` | POL-CRQ-MARK-SATISFIED |

**القصة:** بصفتي **Analyst / any requester**، أريد **تعليم متطلب الجمع كمستوفى**، لكي يتحقق غرض متطلب الجمع: حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية

- **الشروط المسبقة:** الحالة الحالية: APPROVED؛ requester; fulfilment as seen by the requester is ANSWERED, or PARTIAL with explicit acceptance note
- **المدخلات:** `acceptance_note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SATISFIED؛ الحدث EVT-CRQ-SATISFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRQ-MARK-SATISFIED` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-001, REQ-COL-003 · حالات استخدام: UC-120, UC-122
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRQ-MARK-SATISFIED succeeds
  Given AGG-COLLECTION-REQUIREMENT in state APPROVED and every guard holds
  When Analyst / any requester sends CMD-CRQ-MARK-SATISFIED with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SATISFIED
  And EVT-CRQ-SATISFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRQ-MARK-SATISFIED is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRQ-MARK-SATISFIED ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, DRAFT, EXPIRED, REJECTED, SATISFIED, SUBMITTED |
    | FULFILMENT_INSUFFICIENT | 422 | لم يتحقق الشرط: fulfilment as seen by the requester is ANSWERED, or PARTIAL with explicit acceptance note |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRQ-REJECT — رفض متطلب الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | collection manager | `POST /api/v1/information/collection-requirements/{id}/actions/reject` | POL-CRQ-REJECT |

**القصة:** بصفتي **collection manager**، أريد **رفض متطلب الجمع**، لكي يتحقق غرض متطلب الجمع: حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية

- **الشروط المسبقة:** الحالة الحالية: SUBMITTED؛ reason (duplicate, out of scope, infeasible)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-CRQ-REJECTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRQ-REJECT` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-001, REQ-COL-003 · حالات استخدام: UC-120, UC-122
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRQ-REJECT succeeds
  Given AGG-COLLECTION-REQUIREMENT in state SUBMITTED and every guard holds
  When collection manager sends CMD-CRQ-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-CRQ-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRQ-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRQ-REJECT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, CANCELLED, DRAFT, EXPIRED, REJECTED, SATISFIED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRQ-SUBMIT — تقديم متطلب الجمع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst / any requester | `POST /api/v1/information/collection-requirements/{id}/actions/submit` | POL-CRQ-SUBMIT |

**القصة:** بصفتي **Analyst / any requester**، أريد **تقديم متطلب الجمع**، لكي يتحقق غرض متطلب الجمع: حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ area, window, priority and ≥ 1 EEI present (REQ-COL-001)
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SUBMITTED؛ الحدث EVT-CRQ-SUBMITTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)؛ الشروط: tenant match; area within scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRQ-SUBMIT` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-001, REQ-COL-003 · حالات استخدام: UC-120, UC-122
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRQ-SUBMIT succeeds
  Given AGG-COLLECTION-REQUIREMENT in state DRAFT and every guard holds
  When Analyst / any requester sends CMD-CRQ-SUBMIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUBMITTED
  And EVT-CRQ-SUBMITTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRQ-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRQ-SUBMIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, CANCELLED, EXPIRED, REJECTED, SATISFIED, SUBMITTED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REQUIREMENT_INCOMPLETE | 422 | لم يتحقق الشرط: area, window, priority and ≥ 1 EEI present (REQ-COL-001) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-S-COLLECTION-REQUIREMENT-01 — تلقائي: validated observation matched (متطلب الجمع)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | APPROVED | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «validated observation matched»، أريد تحديث **متطلب الجمع** دون تغيير حالته، لكي يتحقق غرض متطلب الجمع: حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية

- **الشرط:** matching engine links observation to EEIs (SPEC-COLLECTION §2); fulfilment recomputed
- **المخرجات:** الحدث EVT-CRQ-FULFILMENT-UPDATED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-COLLECTION-REQUIREMENT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-S-COLLECTION-REQUIREMENT-02 — تلقائي: due passed (متطلب الجمع)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | APPROVED | EXPIRED |

**القصة:** بصفتي **النظام**، عند «due passed»، أريد نقل **متطلب الجمع** إلى EXPIRED، لكي يتحقق غرض متطلب الجمع: حاجة معلوماتية موجهة للجمع: سؤال، منطقة، نافذة، أولوية، عناصر معلومات أساسية

- **الشرط:** scheduler; based on due date only (never on hidden fulfilment)
- **المخرجات:** الحدث EVT-CRQ-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-COLLECTION-REQUIREMENT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-Q-CRQ-BOARD — جلب: Requirements by area (bbox/polygon), state, priority, due

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/information/collection-requirements` | POL-CRQ-BOARD |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Requirements by area (bbox/polygon), state, priority, due**، لكي يتحقق المتطلب: The system shall record information needs as collection requirements with question, area, time window, priority, requester and due date

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Requirements by area (bbox/polygon), state, priority, due؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CRQ-BOARD` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-CRQ-BOARD returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CRQ-BOARD with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CRQ-BOARD is denied
  Given the policy denies the caller
  When the caller sends QRY-CRQ-BOARD
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC02-Q-CRQ-EVIDENCE — جلب: Fulfilment links per EEI (visible observations only) with lineage

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | requester, collection managers | `GET /api/v1/information/collection-requirements/{requirement_id}/fulfilment` | POL-CRQ-EVIDENCE |

**القصة:** بصفتي **requester, collection managers**، أريد **جلب Fulfilment links per EEI (visible observations only) with lineage**، لكي يتحقق المتطلب: When observations answering a collection requirement are validated, the system shall update the requirement's fulfilment status

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Fulfilment links per EEI (visible observations only) with lineage؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** requester, collection managers؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CRQ-EVIDENCE` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-003
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-CRQ-EVIDENCE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CRQ-EVIDENCE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CRQ-EVIDENCE is denied
  Given the policy denies the caller
  When the caller sends QRY-CRQ-EVIDENCE
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC02-Q-CRQ-GET — جلب: Requirement with EEIs and fulfilment computed over observations visible to the caller

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/information/collection-requirements/{requirement_id}` | POL-CRQ-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Requirement with EEIs and fulfilment computed over observations visible to the caller**، لكي يتحقق المتطلب: When observations answering a collection requirement are validated, the system shall update the requirement's fulfilment status

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Requirement with EEIs and fulfilment computed over observations visible to the caller
- **الصلاحية:** requester, collection managers; label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CRQ-GET` · `AGG-COLLECTION-REQUIREMENT` · متطلبات: REQ-COL-003
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-CRQ-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-CRQ-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-CRQ-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-CRQ-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-CONFLICT — التعارض (Conflict)

`03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md` · SLC-04 · الحالات: OPEN, UNDER_REVIEW, RESOLVED, ACCEPTED_AS_CONFLICT → SUPERSEDED

#### US-BC02-CNF-ACCEPT — قبول التعارض

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/information/conflicts/{id}/actions/accept` | POL-CNF-ACCEPT |

**القصة:** بصفتي **Analyst**، أريد **قبول التعارض**، لكي يتحقق غرض التعارض: تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة

- **الشروط المسبقة:** الحالة الحالية: UNDER_REVIEW؛ rationale (both accounts shown to users)
- **المدخلات:** `rationale`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACCEPTED_AS_CONFLICT؛ الحدث EVT-CNF-ACCEPTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CNF-ACCEPT` · `AGG-CONFLICT` · متطلبات: REQ-INF-025, REQ-INF-024 · حالات استخدام: UC-008
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CNF-ACCEPT succeeds
  Given AGG-CONFLICT in state UNDER_REVIEW and every guard holds
  When Analyst sends CMD-CNF-ACCEPT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACCEPTED_AS_CONFLICT
  And EVT-CNF-ACCEPTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CNF-ACCEPT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CNF-ACCEPT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONFLICT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED_AS_CONFLICT, OPEN, RESOLVED, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CNF-ASSIGN — إسناد التعارض

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst lead | `POST /api/v1/information/conflicts/{id}/actions/assign` | POL-CNF-ASSIGN |

**القصة:** بصفتي **Analyst lead**، أريد **إسناد التعارض**، لكي يتحقق غرض التعارض: تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة

- **الشروط المسبقة:** الحالة الحالية: OPEN, UNDER_REVIEW؛ reviewer cleared for every member claim label
- **المدخلات:** `reviewer`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CNF-ASSIGNED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ الشروط: tenant match; assignee cleared for every member claim؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CNF-ASSIGN` · `AGG-CONFLICT` · متطلبات: REQ-INF-025, REQ-INF-024 · حالات استخدام: UC-008
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CNF-ASSIGN succeeds
  Given AGG-CONFLICT in state OPEN or UNDER_REVIEW and every guard holds
  When Analyst lead sends CMD-CNF-ASSIGN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-CNF-ASSIGNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CNF-ASSIGN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CNF-ASSIGN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONFLICT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED_AS_CONFLICT, RESOLVED, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REVIEWER_NOT_CLEARED | 422 | لم يتحقق الشرط: reviewer cleared for every member claim label |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reviewer |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CNF-RAISE — رفع التعارض

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analyst | `POST /api/v1/information/conflicts` | POL-CNF-RAISE |

**القصة:** بصفتي **Analyst**، أريد **رفع التعارض**، لكي يتحقق غرض التعارض: تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ analyst names ≥ 2 visible CURRENT claims on the same cluster and predicate with overlapping valid time
- **المدخلات:** `claims`!: array, `predicate`!: string, `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← OPEN؛ الحدث EVT-CNF-RAISED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CNF-RAISE` · `AGG-CONFLICT` · متطلبات: REQ-INF-025, REQ-INF-024 · حالات استخدام: UC-008
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CNF-RAISE succeeds
  Given AGG-CONFLICT does not exist yet and every guard holds
  When Analyst sends CMD-CNF-RAISE with a valid payload, a new Idempotency-Key
  Then the state becomes OPEN
  And EVT-CNF-RAISED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CNF-RAISE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CNF-RAISE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONFLICT_INVALID | 422 | لم يتحقق الشرط: analyst names ≥ 2 visible CURRENT claims on the same cluster and predicate with overlapping valid time |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: claims, predicate |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CNF-REOPEN — إعادة فتح التعارض

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/information/conflicts/{id}/actions/reopen` | POL-CNF-REOPEN |

**القصة:** بصفتي **Analyst**، أريد **إعادة فتح التعارض**، لكي يتحقق غرض التعارض: تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة

- **الشروط المسبقة:** الحالة الحالية: RESOLVED, ACCEPTED_AS_CONFLICT؛ new evidence or reason; closes current resolution record (recorded_to = now)
- **المدخلات:** `reason`!: string, `evidence`: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← UNDER_REVIEW؛ الحدث EVT-CNF-REOPENED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CNF-REOPEN` · `AGG-CONFLICT` · متطلبات: REQ-INF-025, REQ-INF-024 · حالات استخدام: UC-008
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CNF-REOPEN succeeds
  Given AGG-CONFLICT in state RESOLVED or ACCEPTED_AS_CONFLICT and every guard holds
  When Analyst sends CMD-CNF-REOPEN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNDER_REVIEW
  And EVT-CNF-REOPENED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CNF-REOPEN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CNF-REOPEN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONFLICT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: OPEN, SUPERSEDED, UNDER_REVIEW |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CNF-RESOLVE — حل التعارض

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/information/conflicts/{id}/actions/resolve` | POL-CNF-RESOLVE |

**القصة:** بصفتي **Analyst**، أريد **حل التعارض**، لكي يتحقق غرض التعارض: تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة

- **الشروط المسبقة:** الحالة الحالية: UNDER_REVIEW؛ preferred claim ∈ CURRENT members; rationale; reviewer ≠ asserter of the preferred claim (SoD, default on); records resolution with recorded_from = now
- **المدخلات:** `preferred_claim`!: urn, `rationale`!: string, `evidence`: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RESOLVED؛ الحدث EVT-CNF-RESOLVED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ الشروط: tenant match; cleared for every member claim label؛ فصل المهام: reviewer ≠ asserter of preferred claim؛ الالتزامات: audit
- **الربط:** `CMD-CNF-RESOLVE` · `AGG-CONFLICT` · متطلبات: REQ-INF-025, REQ-INF-024 · حالات استخدام: UC-008
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CNF-RESOLVE succeeds
  Given AGG-CONFLICT in state UNDER_REVIEW and every guard holds
  When Analyst sends CMD-CNF-RESOLVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RESOLVED
  And EVT-CNF-RESOLVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CNF-RESOLVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CNF-RESOLVE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONFLICT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED_AS_CONFLICT, OPEN, RESOLVED, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: reviewer ≠ asserter of preferred claim |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: preferred_claim, rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CNF-START-REVIEW — بدء مراجعة التعارض

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/information/conflicts/{id}/actions/start-review` | POL-CNF-START-REVIEW |

**القصة:** بصفتي **Analyst**، أريد **بدء مراجعة التعارض**، لكي يتحقق غرض التعارض: تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ actor = assigned reviewer (or Analyst lead)
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← UNDER_REVIEW؛ الحدث EVT-CNF-REVIEW-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CNF-START-REVIEW` · `AGG-CONFLICT` · متطلبات: REQ-INF-025, REQ-INF-024 · حالات استخدام: UC-008
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CNF-START-REVIEW succeeds
  Given AGG-CONFLICT in state OPEN and every guard holds
  When Analyst sends CMD-CNF-START-REVIEW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNDER_REVIEW
  And EVT-CNF-REVIEW-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CNF-START-REVIEW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CNF-START-REVIEW ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONFLICT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED_AS_CONFLICT, RESOLVED, SUPERSEDED, UNDER_REVIEW |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | NOT_ASSIGNED_REVIEWER | 422 | لم يتحقق الشرط: actor = assigned reviewer (or Analyst lead) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-S-CONFLICT-01 — تلقائي: conflict rule matched (التعارض)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | ∅ | OPEN |

**القصة:** بصفتي **النظام**، عند «conflict rule matched»، أريد نقل **التعارض** إلى OPEN، لكي يتحقق غرض التعارض: تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة

- **الشرط:** rule CF-01..CF-04 on claims of the same identity cluster, same predicate, overlapping valid; no non-terminal conflict with the same (cluster, predicate, window) — otherwise the claim joins it
- **المخرجات:** الحدث EVT-CNF-DETECTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-CONFLICT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-S-CONFLICT-02 — تلقائي: incompatible claim joined (التعارض)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | OPEN, UNDER_REVIEW | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «incompatible claim joined»، أريد تحديث **التعارض** دون تغيير حالته، لكي يتحقق غرض التعارض: تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة

- **الشرط:** new CURRENT claim incompatible with members (same key, overlapping window)
- **المخرجات:** الحدث EVT-CNF-CLAIM-ADDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-CONFLICT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-S-CONFLICT-03 — تلقائي: member set no longer conflicting (التعارض)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | OPEN, UNDER_REVIEW, RESOLVED, ACCEPTED_AS_CONFLICT | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «member set no longer conflicting»، أريد نقل **التعارض** إلى SUPERSEDED، لكي يتحقق غرض التعارض: تعارض بين ادعاءين أو أكثر حول نفس الموضوع والسمة في فترة متداخلة

- **الشرط:** fewer than 2 incompatible CURRENT members (claims closed, split, or corrected)
- **المخرجات:** الحدث EVT-CNF-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-CONFLICT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-Q-CNF-GET — جلب: Conflict with visible members, evidence, resolution history (as known_at)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | Analyst; visibility rule INV-CNF-04 | `GET /api/v1/information/conflicts/{conflict_id}` | POL-CNF-GET |

**القصة:** بصفتي **Analyst; visibility rule INV-CNF-04**، أريد **جلب Conflict with visible members, evidence, resolution history (as known_at)**، لكي يتحقق المتطلب: When two claims about the same subject and attribute overlap in valid time with incompatible values, the system shall open a conflict case and retain both claims

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Conflict with visible members, evidence, resolution history (as known_at)
- **الصلاحية:** Analyst; visibility rule INV-CNF-04؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CNF-GET` · `AGG-CONFLICT` · متطلبات: REQ-INF-025
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-CNF-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-CNF-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-CNF-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-CNF-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC02-Q-CNF-LIST — جلب: Conflicts by subject, predicate, state, assignee

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | Analyst; only conflicts with ≥ 2 visible member claims | `GET /api/v1/information/conflicts` | POL-CNF-LIST |

**القصة:** بصفتي **Analyst; only conflicts with ≥ 2 visible member claims**، أريد **جلب Conflicts by subject, predicate, state, assignee**، لكي يتحقق المتطلب: When two claims about the same subject and attribute overlap in valid time with incompatible values, the system shall open a conflict case and retain both claims

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Conflicts by subject, predicate, state, assignee؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Analyst; only conflicts with ≥ 2 visible member claims؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CNF-LIST` · `AGG-CONFLICT` · متطلبات: REQ-INF-025
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-CNF-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CNF-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CNF-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-CNF-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-CORRELATION-PROPOSAL — مقترح الربط (Correlation Proposal)

`03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md` · SLC-15 · الحالات: PROPOSED, UNDER_REVIEW → ACCEPTED, REJECTED, EXPIRED

#### US-BC02-CRP-ACCEPT — قبول مقترح الربط

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analyst | `POST /api/v1/information/correlation-proposals/{id}/actions/accept` | POL-CRP-ACCEPT |

**القصة:** بصفتي **Analyst**، أريد **قبول مقترح الربط**، لكي يتحقق غرض مقترح الربط: اقتراح ربط ملاحظات/ادعاءات من مصادر متعددة في المكان والزمان

- **الشروط المسبقة:** الحالة الحالية: UNDER_REVIEW؛ effects through owner commands as the reviewer: same_event → Real-World Event + participation relationships + fused claims; co_location → relationship; same_entity → ER case (SLC-04); lineage lists every contributing source and its reliability
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACCEPTED؛ الحدث EVT-CRP-ACCEPTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, accept, reject)؛ الشروط: tenant match; inputs visible؛ فصل المهام: reviewer cleared for all inputs؛ الالتزامات: audit
- **الربط:** `CMD-CRP-ACCEPT` · `AGG-CORRELATION-PROPOSAL` · متطلبات: REQ-FUS-001, REQ-FUS-002 · حالات استخدام: UC-132
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRP-ACCEPT succeeds
  Given AGG-CORRELATION-PROPOSAL in state UNDER_REVIEW and every guard holds
  When Analyst sends CMD-CRP-ACCEPT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACCEPTED
  And EVT-CRP-ACCEPTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRP-ACCEPT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRP-ACCEPT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, EXPIRED, PROPOSED, REJECTED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OWNER_REJECTED | 422 | لم يتحقق الشرط: effects through owner commands as the reviewer: same_event → Real-World Event + participation relationships + fused claims |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRP-PROPOSE — اقتراح مقترح الربط

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analyst | `POST /api/v1/information/correlation-proposals` | POL-CRP-PROPOSE |

**القصة:** بصفتي **Analyst**، أريد **اقتراح مقترح الربط**، لكي يتحقق غرض مقترح الربط: اقتراح ربط ملاحظات/ادعاءات من مصادر متعددة في المكان والزمان

- **الشروط المسبقة:** الحالة الحالية: ∅؛ analyst; ≥ 2 visible inputs; kind; rationale
- **المدخلات:** `kind`!: enum(same_event,co_location,track_association,same_entity_hint), `inputs`!: array, `rationale`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← PROPOSED؛ الحدث EVT-CRP-PROPOSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, accept, reject)؛ الشروط: tenant match; inputs visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRP-PROPOSE` · `AGG-CORRELATION-PROPOSAL` · متطلبات: REQ-FUS-001, REQ-FUS-002 · حالات استخدام: UC-132
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRP-PROPOSE succeeds
  Given AGG-CORRELATION-PROPOSAL does not exist yet and every guard holds
  When Analyst sends CMD-CRP-PROPOSE with a valid payload, a new Idempotency-Key
  Then the state becomes PROPOSED
  And EVT-CRP-PROPOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRP-PROPOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRP-PROPOSE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CORRELATION_INVALID | 422 | لم يتحقق الشرط: analyst; ≥ 2 visible inputs; kind; rationale |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: kind, inputs, rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRP-REJECT — رفض مقترح الربط

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analyst | `POST /api/v1/information/correlation-proposals/{id}/actions/reject` | POL-CRP-REJECT |

**القصة:** بصفتي **Analyst**، أريد **رفض مقترح الربط**، لكي يتحقق غرض مقترح الربط: اقتراح ربط ملاحظات/ادعاءات من مصادر متعددة في المكان والزمان

- **الشروط المسبقة:** الحالة الحالية: UNDER_REVIEW, PROPOSED؛ reason (feeds rule evaluation)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-CRP-REJECTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, accept, reject)؛ الشروط: tenant match; inputs visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRP-REJECT` · `AGG-CORRELATION-PROPOSAL` · متطلبات: REQ-FUS-001, REQ-FUS-002 · حالات استخدام: UC-132
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRP-REJECT succeeds
  Given AGG-CORRELATION-PROPOSAL in state UNDER_REVIEW or PROPOSED and every guard holds
  When Analyst sends CMD-CRP-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-CRP-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRP-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRP-REJECT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, EXPIRED, REJECTED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRP-START-REVIEW — بدء مراجعة مقترح الربط

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/information/correlation-proposals/{id}/actions/start-review` | POL-CRP-START-REVIEW |

**القصة:** بصفتي **Analyst**، أريد **بدء مراجعة مقترح الربط**، لكي يتحقق غرض مقترح الربط: اقتراح ربط ملاحظات/ادعاءات من مصادر متعددة في المكان والزمان

- **الشروط المسبقة:** الحالة الحالية: PROPOSED؛ reviewer cleared for every input label
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← UNDER_REVIEW؛ الحدث EVT-CRP-REVIEW-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, accept, reject)؛ الشروط: tenant match; inputs visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRP-START-REVIEW` · `AGG-CORRELATION-PROPOSAL` · متطلبات: REQ-FUS-001, REQ-FUS-002 · حالات استخدام: UC-132
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRP-START-REVIEW succeeds
  Given AGG-CORRELATION-PROPOSAL in state PROPOSED and every guard holds
  When Analyst sends CMD-CRP-START-REVIEW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNDER_REVIEW
  And EVT-CRP-REVIEW-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRP-START-REVIEW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRP-START-REVIEW ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, EXPIRED, REJECTED, UNDER_REVIEW |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REVIEWER_NOT_CLEARED | 422 | لم يتحقق الشرط: reviewer cleared for every input label |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-S-CORRELATION-PROPOSAL-01 — تلقائي: correlation rule score ≥ threshold (مقترح الربط)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | ∅ | PROPOSED |

**القصة:** بصفتي **النظام**، عند «correlation rule score ≥ threshold»، أريد نقل **مقترح الربط** إلى PROPOSED، لكي يتحقق غرض مقترح الربط: اقتراح ربط ملاحظات/ادعاءات من مصادر متعددة في المكان والزمان

- **الشرط:** inputs from ≥ 2 distinct sources; no identical non-terminal proposal; label = max(input labels)
- **المخرجات:** الحدث EVT-CRP-PROPOSED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-CORRELATION-PROPOSAL` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-S-CORRELATION-PROPOSAL-02 — تلقائي: not reviewed within 30 days (مقترح الربط)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | PROPOSED | EXPIRED |

**القصة:** بصفتي **النظام**، عند «not reviewed within 30 days»، أريد نقل **مقترح الربط** إلى EXPIRED، لكي يتحقق غرض مقترح الربط: اقتراح ربط ملاحظات/ادعاءات من مصادر متعددة في المكان والزمان

- **الشرط:** scheduler
- **المخرجات:** الحدث EVT-CRP-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-CORRELATION-PROPOSAL` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-Q-CRP-GET — جلب: Proposal with inputs, sources, reliabilities, score breakdown

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | reviewer cleared for all inputs | `GET /api/v1/information/correlation-proposals/{proposal_id}` | POL-CRP-GET |

**القصة:** بصفتي **reviewer cleared for all inputs**، أريد **جلب Proposal with inputs, sources, reliabilities, score breakdown**، لكي يتحقق المتطلب: The system shall record for each fused result the contributing sources and their reliabilities

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Proposal with inputs, sources, reliabilities, score breakdown
- **الصلاحية:** reviewer cleared for all inputs؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CRP-GET` · `AGG-CORRELATION-PROPOSAL` · متطلبات: REQ-FUS-002
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-CRP-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-CRP-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-CRP-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-CRP-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC02-Q-CRP-QUEUE — جلب: Proposals by kind, state, area, score (inputs all visible to caller)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | Analyst | `GET /api/v1/information/correlation-proposals` | POL-CRP-QUEUE |

**القصة:** بصفتي **Analyst**، أريد **جلب Proposals by kind, state, area, score (inputs all visible to caller)**، لكي يتحقق المتطلب: The system shall correlate observations and claims across sources in space and time into correlation proposals with method, score and evidence

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Proposals by kind, state, area, score (inputs all visible to caller)؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Analyst؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CRP-QUEUE` · `AGG-CORRELATION-PROPOSAL` · متطلبات: REQ-FUS-001
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-CRP-QUEUE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CRP-QUEUE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CRP-QUEUE is denied
  Given the policy denies the caller
  When the caller sends QRY-CRP-QUEUE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-CORRELATION-RULE — قاعدة الربط (Correlation Rule)

`03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md` · SLC-15 · الحالات: DRAFT, ACTIVE → RETIRED

#### US-BC02-CRR-ACTIVATE — تفعيل قاعدة الربط

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | second approver | `POST /api/v1/information/correlation-rules/{id}/actions/activate` | POL-CRR-ACTIVATE |

**القصة:** بصفتي **second approver**، أريد **تفعيل قاعدة الربط**، لكي يتحقق غرض قاعدة الربط: قاعدة ربط زماني-مكاني بمعاملات وعتبة وتقييم

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ evaluation on a labelled set: precision ≥ 70 % of proposals (recalibrate after pilot); approver ≠ author
- **المدخلات:** `evaluation_report`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-CRR-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead (define, edit) · second approver (activate)؛ الشروط: tenant match; inputs visible؛ فصل المهام: approver ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-CRR-ACTIVATE` · `AGG-CORRELATION-RULE` · متطلبات: REQ-FUS-001 · حالات استخدام: UC-132
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRR-ACTIVATE succeeds
  Given AGG-CORRELATION-RULE in state DRAFT and every guard holds
  When second approver sends CMD-CRR-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-CRR-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRR-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRR-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CORRELATION_RULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RULE_BELOW_TARGET | 422 | لم يتحقق الشرط: evaluation on a labelled set: precision ≥ 70 % of proposals (recalibrate after pilot); approver ≠ author |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: evaluation_report |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRR-DEFINE — تعريف قاعدة الربط

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analyst lead | `POST /api/v1/information/correlation-rules` | POL-CRR-DEFINE |

**القصة:** بصفتي **Analyst lead**، أريد **تعريف قاعدة الربط**، لكي يتحقق غرض قاعدة الربط: قاعدة ربط زماني-مكاني بمعاملات وعتبة وتقييم

- **الشروط المسبقة:** الحالة الحالية: ∅؛ kind ∈ {same_event, co_location, track_association, same_entity_hint}
- **المدخلات:** `kind`!: enum(same_event,co_location,track_association,same_entity_hint), `name`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-CRR-DEFINED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead (define, edit) · second approver (activate)؛ الشروط: tenant match; inputs visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRR-DEFINE` · `AGG-CORRELATION-RULE` · متطلبات: REQ-FUS-001 · حالات استخدام: UC-132
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRR-DEFINE succeeds
  Given AGG-CORRELATION-RULE does not exist yet and every guard holds
  When Analyst lead sends CMD-CRR-DEFINE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-CRR-DEFINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRR-DEFINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRR-DEFINE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RULE_INVALID | 422 | لم يتحقق الشرط: kind ∈ {same_event, co_location, track_association, same_entity_hint} |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: kind, name |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRR-EDIT — تعديل قاعدة الربط

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst lead | `POST /api/v1/information/correlation-rules/{id}/actions/edit` | POL-CRR-EDIT |

**القصة:** بصفتي **Analyst lead**، أريد **تعديل قاعدة الربط**، لكي يتحقق غرض قاعدة الربط: قاعدة ربط زماني-مكاني بمعاملات وعتبة وتقييم

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE؛ parameters: max distance (m, accuracy-aware), time window, attribute similarity, min distinct sources, threshold; ACTIVE → new version
- **المدخلات:** `parameters`!: object — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CRR-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead (define, edit) · second approver (activate)؛ الشروط: tenant match; inputs visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRR-EDIT` · `AGG-CORRELATION-RULE` · متطلبات: REQ-FUS-001 · حالات استخدام: UC-132
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRR-EDIT succeeds
  Given AGG-CORRELATION-RULE in state DRAFT or ACTIVE and every guard holds
  When Analyst lead sends CMD-CRR-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-CRR-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRR-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRR-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CORRELATION_RULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RULE_INVALID | 422 | لم يتحقق الشرط: parameters: max distance (m, accuracy-aware), time window, attribute similarity, min distinct sources, threshold; ACTIVE → new version |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: parameters |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-CRR-RETIRE — إحالة قاعدة الربط إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analyst lead (محسوم: `17-security-design.md` §5) | `POST /api/v1/information/correlation-rules/{id}/actions/retire` | POL-CRR-RETIRE |

**القصة:** بصفتي **Analyst lead**، أريد **إحالة قاعدة الربط إلى التقاعد**، لكي يتحقق غرض قاعدة الربط: قاعدة ربط زماني-مكاني بمعاملات وعتبة وتقييم

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-CRR-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead (retire)؛ الشروط: tenant match; inputs visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRR-RETIRE` · `AGG-CORRELATION-RULE` · متطلبات: REQ-FUS-001 · حالات استخدام: UC-132
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRR-RETIRE succeeds
  Given AGG-CORRELATION-RULE in state ACTIVE and every guard holds
  When Analyst lead sends CMD-CRR-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-CRR-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRR-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRR-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CORRELATION_RULE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DRAFT, RETIRED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

### AGG-ENTITY — الكيان (Entity (identity))

`03-domain/contexts/BC02/aggregates/AGG-ENTITY.md` · SLC-02 · الحالات: ACTIVE, RETIRED → —

#### US-BC02-ENT-CHANGE-TYPE — تغيير نوع الكيان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst · adapter service account | `POST /api/v1/information/entities/{id}/actions/change-type` | POL-ENT-CHANGE-TYPE |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **تغيير نوع الكيان**، لكي يتحقق غرض الكيان: هوية كيان؛ سماته ادعاءات مستقلة

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ compatible type per RD-ENTITY-TYPES; new version; reason
- **المدخلات:** `entity_type`!: string, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ENT-TYPE-CHANGED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ENT-CHANGE-TYPE` · `AGG-ENTITY` · متطلبات: REQ-INF-020, REQ-INF-021, REQ-INF-036 · حالات استخدام: UC-001, UC-002, UC-003, UC-006
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ENT-CHANGE-TYPE succeeds
  Given AGG-ENTITY in state ACTIVE and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-ENT-CHANGE-TYPE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ENT-TYPE-CHANGED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ENT-CHANGE-TYPE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ENT-CHANGE-TYPE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ENTITY_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | ENTITY_TYPE_INCOMPATIBLE | 422 | لم يتحقق الشرط: compatible type per RD-ENTITY-TYPES |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: entity_type, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ENT-RECLASSIFY — إعادة تصنيف الكيان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst · adapter service account | `POST /api/v1/information/entities/{id}/actions/reclassify` | POL-ENT-RECLASSIFY |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **إعادة تصنيف الكيان**، لكي يتحقق غرض الكيان: هوية كيان؛ سماته ادعاءات مستقلة

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, RETIRED؛ authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ENT-RECLASSIFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ENT-RECLASSIFY` · `AGG-ENTITY` · متطلبات: REQ-INF-020, REQ-INF-021, REQ-INF-036 · حالات استخدام: UC-001, UC-002, UC-003, UC-006
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ENT-RECLASSIFY succeeds
  Given AGG-ENTITY in state ACTIVE or RETIRED and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-ENT-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ENT-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ENT-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ENT-RECLASSIFY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per tenant policy (REQ-GOV-004) |
    | ENTITY_INVALID_STATE_TRANSITION | 409 | لا حالة في المصفوفة يُرفض منها هذا الأمر؛ الرمز لا يُتوقع حدوثه |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ENT-REGISTER — تسجيل الكيان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst · adapter service account | `POST /api/v1/information/entities` | POL-ENT-REGISTER |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **تسجيل الكيان**، لكي يتحقق غرض الكيان: هوية كيان؛ سماته ادعاءات مستقلة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ type in RD-ENTITY-TYPES; each initial claim valid as CMD-CLM-ASSERT; Entity + initial Claims created in one unit of work
- **المدخلات:** `entity_type`!: string, `label`!: Label, `initial_claims`: array, `external_ids`: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-ENT-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ENT-REGISTER` · `AGG-ENTITY` · متطلبات: REQ-INF-020, REQ-INF-021, REQ-INF-036 · حالات استخدام: UC-001, UC-002, UC-003, UC-006
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ENT-REGISTER succeeds
  Given AGG-ENTITY does not exist yet and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-ENT-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-ENT-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ENT-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ENT-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ENTITY_INVALID | 422 | لم يتحقق الشرط: type in RD-ENTITY-TYPES; Entity + initial Claims created in one unit of work |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: entity_type, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ENT-REINSTATE — إعادة الكيان إلى السريان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst · adapter service account | `POST /api/v1/information/entities/{id}/actions/reinstate` | POL-ENT-REINSTATE |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **إعادة الكيان إلى السريان**، لكي يتحقق غرض الكيان: هوية كيان؛ سماته ادعاءات مستقلة

- **الشروط المسبقة:** الحالة الحالية: RETIRED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-ENT-REINSTATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ENT-REINSTATE` · `AGG-ENTITY` · متطلبات: REQ-INF-020, REQ-INF-021, REQ-INF-036 · حالات استخدام: UC-001, UC-002, UC-003, UC-006
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ENT-REINSTATE succeeds
  Given AGG-ENTITY in state RETIRED and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-ENT-REINSTATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-ENT-REINSTATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ENT-REINSTATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ENT-REINSTATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ENTITY_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ENT-RETIRE — إحالة الكيان إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst · adapter service account | `POST /api/v1/information/entities/{id}/actions/retire` | POL-ENT-RETIRE |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **إحالة الكيان إلى التقاعد**، لكي يتحقق غرض الكيان: هوية كيان؛ سماته ادعاءات مستقلة

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason (created in error / no longer tracked); claims untouched
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-ENT-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ENT-RETIRE` · `AGG-ENTITY` · متطلبات: REQ-INF-020, REQ-INF-021, REQ-INF-036 · حالات استخدام: UC-001, UC-002, UC-003, UC-006
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ENT-RETIRE succeeds
  Given AGG-ENTITY in state ACTIVE and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-ENT-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-ENT-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ENT-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ENT-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ENTITY_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-Q-CLUSTER-GET — جلب: Cluster members, canonical URN, links, as known_at

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | Analyst; invisible members omitted | `GET /api/v1/information/entities/{entity_id}/identity-cluster` | POL-CLUSTER-GET |

**القصة:** بصفتي **Analyst; invisible members omitted**، أريد **جلب Cluster members, canonical URN, links, as known_at**، لكي يتحقق المتطلب: When entities are matched, the system shall record a same-as link with the decision, reviewer and time, keep all original identifiers valid, and resolve any member identifier to the identity cluster's canonical identifier while reporting the requested identifier

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Cluster members, canonical URN, links, as known_at؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Analyst; invisible members omitted؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CLUSTER-GET` · `AGG-ENTITY` · متطلبات: REQ-INF-033
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-CLUSTER-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CLUSTER-GET with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CLUSTER-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-CLUSTER-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC02-Q-ENT-CLAIMS — جلب: Claim history (predicate, valid_at, known_at, include_closed)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user; label-filtered | `GET /api/v1/information/entities/{entity_id}/claims` | POL-ENT-CLAIMS |

**القصة:** بصفتي **any user; label-filtered**، أريد **جلب Claim history (predicate, valid_at, known_at, include_closed)**، لكي يتحقق المتطلب: The system shall record a valid-time interval and a record-time interval for every T1 claim

- **المدخلات:** `valid_at`, `known_at`, `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Claim history (predicate, valid_at, known_at, include_closed)؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user; label-filtered؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-ENT-CLAIMS` · `AGG-ENTITY` · متطلبات: REQ-INF-022
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-ENT-CLAIMS returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ENT-CLAIMS with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ENT-CLAIMS is denied
  Given the policy denies the caller
  When the caller sends QRY-ENT-CLAIMS
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC02-Q-ENT-LIST — جلب: Entities by type, bbox/polygon of current location, valid_at

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/information/entities` | POL-ENT-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Entities by type, bbox/polygon of current location, valid_at**، لكي يتحقق المتطلب: The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct object types

- **المدخلات:** `valid_at`, `known_at`, `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Entities by type, bbox/polygon of current location, valid_at؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user; allowed_scope pre-filter؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-ENT-LIST` · `AGG-ENTITY` · متطلبات: REQ-INF-020
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-ENT-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ENT-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ENT-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-ENT-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC02-Q-ENT-POSITIONS — جلب: Position history in [from,to) as known_at

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user; label-filtered; geometry generalized by obligation | `GET /api/v1/information/entities/{entity_id}/positions` | POL-ENT-POSITIONS |

**القصة:** بصفتي **any user; label-filtered; geometry generalized by obligation**، أريد **جلب Position history in [from,to) as known_at**، لكي يتحقق المتطلب: The system shall keep the position history of located entities over time

- **المدخلات:** `valid_at`, `known_at`, `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Position history in [from,to) as known_at؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user; label-filtered; geometry generalized by obligation؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-ENT-POSITIONS` · `AGG-ENTITY` · متطلبات: REQ-INF-030
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-ENT-POSITIONS returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ENT-POSITIONS with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ENT-POSITIONS is denied
  Given the policy denies the caller
  When the caller sends QRY-ENT-POSITIONS
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC02-Q-ENT-RESOLVED — جلب: Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED candidates, confidence); resolves through the identity cluster and returns canonical_urn + requested_urn (SLC-04)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user; claims label-filtered (INV-ENT-02) | `GET /api/v1/information/entities/{entity_id}` | POL-ENT-RESOLVED |

**القصة:** بصفتي **any user; claims label-filtered (INV-ENT-02)**، أريد **جلب Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED candidates, confidence); resolves through the identity cluster and returns canonical_urn + requested_urn (SLC-04)**، لكي يتحقق المتطلب: When a query specifies a valid time T, a record time K, or both, the system shall return the state valid at T as known at K, using the current time for any time not specified

- **المدخلات:** `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED candidates, confidence); resolves through the identity cluster and returns canonical_urn + requested_urn (SLC-04)
- **الصلاحية:** any user; claims label-filtered (INV-ENT-02)؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-ENT-RESOLVED` · `AGG-ENTITY` · متطلبات: REQ-INF-023
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-ENT-RESOLVED returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-ENT-RESOLVED
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-ENT-RESOLVED hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-ENT-RESOLVED
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC02-Q-REL-LIST — جلب: Relationships valid_at/known_at, both directions

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user; hidden relationships and endpoints omitted | `GET /api/v1/information/entities/{entity_id}/relationships` | POL-REL-LIST |

**القصة:** بصفتي **any user; hidden relationships and endpoints omitted**، أريد **جلب Relationships valid_at/known_at, both directions**، لكي يتحقق المتطلب: The system shall represent relationships as objects with type, source, target, validity period, evidence, provenance, confidence and classification

- **المدخلات:** `valid_at`, `known_at`, `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Relationships valid_at/known_at, both directions؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user; hidden relationships and endpoints omitted؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-REL-LIST` · `AGG-ENTITY` · متطلبات: REQ-INF-027
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-REL-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-REL-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-REL-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-REL-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-ER-CASE — حالة مطابقة الكيانات (Entity Resolution Case)

`03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md` · SLC-04 · الحالات: CANDIDATE, UNDER_REVIEW, MATCHED, POSSIBLE_DUPLICATE, SPLIT_REQUIRED → NOT_A_MATCH, SPLIT, WITHDRAWN

#### US-BC02-ER-CONFIRM-MATCH — تأكيد تطابق حالة مطابقة الكيانات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | second Analyst | `POST /api/v1/information/er-cases/{id}/actions/confirm-match` | POL-ER-CONFIRM-MATCH |

**القصة:** بصفتي **second Analyst**، أريد **تأكيد تطابق حالة مطابقة الكيانات**، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشروط المسبقة:** الحالة الحالية: SPLIT_REQUIRED؛ reviewer ≠ split requester; rationale
- **المدخلات:** `rationale`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← MATCHED؛ الحدث EVT-ER-MATCH-CONFIRMED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ الشروط: tenant match; object visible؛ فصل المهام: reviewer ≠ split requester؛ الالتزامات: audit
- **الربط:** `CMD-ER-CONFIRM-MATCH` · `AGG-ER-CASE` · متطلبات: REQ-INF-032, REQ-INF-033, REQ-INF-034 · حالات استخدام: UC-007, UC-104
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ER-CONFIRM-MATCH succeeds
  Given AGG-ER-CASE in state SPLIT_REQUIRED and every guard holds
  When second Analyst sends CMD-ER-CONFIRM-MATCH with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes MATCHED
  And EVT-ER-MATCH-CONFIRMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ER-CONFIRM-MATCH is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ER-CONFIRM-MATCH ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ER_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANDIDATE, MATCHED, NOT_A_MATCH, POSSIBLE_DUPLICATE, SPLIT, UNDER_REVIEW, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: reviewer ≠ split requester |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ER-DECIDE-MATCH — الحكم بتطابق حالة مطابقة الكيانات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/information/er-cases/{id}/actions/decide-match` | POL-ER-DECIDE-MATCH |

**القصة:** بصفتي **Analyst**، أريد **الحكم بتطابق حالة مطابقة الكيانات**، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشروط المسبقة:** الحالة الحالية: UNDER_REVIEW؛ types compatible; neither entity RETIRED; merged cluster contains no NOT_A_MATCH pair; merged cluster size ≤ 50 or second reviewer; reviewer ≠ human proposer; creates MATCH link and recomputes cluster in the same transaction
- **المدخلات:** `rationale`!: string, `second_reviewer`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← MATCHED؛ الحدث EVT-ER-MATCHED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ الشروط: tenant match; cleared for both entity labels؛ فصل المهام: reviewer ≠ human proposer; second reviewer if cluster > 50؛ الالتزامات: audit
- **الربط:** `CMD-ER-DECIDE-MATCH` · `AGG-ER-CASE` · متطلبات: REQ-INF-032, REQ-INF-033, REQ-INF-034 · حالات استخدام: UC-007, UC-104
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ER-DECIDE-MATCH succeeds
  Given AGG-ER-CASE in state UNDER_REVIEW and every guard holds
  When Analyst sends CMD-ER-DECIDE-MATCH with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes MATCHED
  And EVT-ER-MATCHED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ER-DECIDE-MATCH is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ER-DECIDE-MATCH ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ER_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANDIDATE, MATCHED, NOT_A_MATCH, POSSIBLE_DUPLICATE, SPLIT, SPLIT_REQUIRED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MATCH_CONTRADICTS_NOT_A_MATCH | 422 | لم يتحقق الشرط: merged cluster contains no NOT_A_MATCH pair; creates MATCH link and recomputes cluster in the same transaction |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: reviewer ≠ human proposer; second reviewer if cluster > 50 |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ER-DECIDE-NOT-MATCH — الحكم بعدم تطابق حالة مطابقة الكيانات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analyst | `POST /api/v1/information/er-cases/{id}/actions/decide-not-match` | POL-ER-DECIDE-NOT-MATCH |

**القصة:** بصفتي **Analyst**، أريد **الحكم بعدم تطابق حالة مطابقة الكيانات**، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشروط المسبقة (لكل انتقال):**
  - من UNDER_REVIEW ← NOT_A_MATCH: rationale; creates NOT_A_MATCH link (blocks re-proposal)
  - من POSSIBLE_DUPLICATE ← NOT_A_MATCH: rationale
- **المدخلات:** `rationale`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← NOT_A_MATCH؛ الحدث EVT-ER-NOT-MATCHED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ER-DECIDE-NOT-MATCH` · `AGG-ER-CASE` · متطلبات: REQ-INF-032, REQ-INF-033, REQ-INF-034 · حالات استخدام: UC-007, UC-104
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario Outline: CMD-ER-DECIDE-NOT-MATCH succeeds from each allowed state
  Given AGG-ER-CASE in state <from> and the guard for that transition holds
  When Analyst sends CMD-ER-DECIDE-NOT-MATCH with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes <to>
  And <event> is written to the outbox with one audit record in the same transaction

  Examples:
    | from | to | event |
    | UNDER_REVIEW | NOT_A_MATCH | EVT-ER-NOT-MATCHED |
    | POSSIBLE_DUPLICATE | NOT_A_MATCH | EVT-ER-NOT-MATCHED |

Scenario Outline: CMD-ER-DECIDE-NOT-MATCH is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ER-DECIDE-NOT-MATCH ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ER_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANDIDATE, MATCHED, NOT_A_MATCH, SPLIT, SPLIT_REQUIRED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ER-PARK — تأجيل حالة مطابقة الكيانات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst (محسوم: `17-security-design.md` §5) | `POST /api/v1/information/er-cases/{id}/actions/park` | POL-ER-PARK |

**القصة:** بصفتي **Analyst**، أريد **تأجيل حالة مطابقة الكيانات**، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشروط المسبقة:** الحالة الحالية: UNDER_REVIEW؛ rationale; insufficient evidence
- **المدخلات:** `rationale`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← POSSIBLE_DUPLICATE؛ الحدث EVT-ER-PARKED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (park)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ER-PARK` · `AGG-ER-CASE` · متطلبات: REQ-INF-032, REQ-INF-033, REQ-INF-034 · حالات استخدام: UC-007, UC-104
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ER-PARK succeeds
  Given AGG-ER-CASE in state UNDER_REVIEW and every guard holds
  When Analyst sends CMD-ER-PARK with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes POSSIBLE_DUPLICATE
  And EVT-ER-PARKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ER-PARK is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ER-PARK ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ER_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANDIDATE, MATCHED, NOT_A_MATCH, POSSIBLE_DUPLICATE, SPLIT, SPLIT_REQUIRED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ER-PROPOSE — اقتراح حالة مطابقة الكيانات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analyst | `POST /api/v1/information/er-cases` | POL-ER-PROPOSE |

**القصة:** بصفتي **Analyst**، أريد **اقتراح حالة مطابقة الكيانات**، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشروط المسبقة:** الحالة الحالية: ∅؛ same conditions; proposer is Analyst or AI suggestion (AIL1, agent recorded)
- **المدخلات:** `left`!: urn, `right`!: urn, `rationale`!: string, `agent`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← CANDIDATE؛ الحدث EVT-ER-PROPOSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ER-PROPOSE` · `AGG-ER-CASE` · متطلبات: REQ-INF-032, REQ-INF-033, REQ-INF-034 · حالات استخدام: UC-007, UC-104
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ER-PROPOSE succeeds
  Given AGG-ER-CASE does not exist yet and every guard holds
  When Analyst sends CMD-ER-PROPOSE with a valid payload, a new Idempotency-Key
  Then the state becomes CANDIDATE
  And EVT-ER-PROPOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ER-PROPOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ER-PROPOSE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ER_PAIR_INVALID | 422 | لم يتحقق الشرط: same conditions; proposer is Analyst or AI suggestion (AIL1, agent recorded) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: left, right, rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ER-REQUEST-SPLIT — طلب فصل حالة مطابقة الكيانات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/information/er-cases/{id}/actions/request-split` | POL-ER-REQUEST-SPLIT |

**القصة:** بصفتي **Analyst**، أريد **طلب فصل حالة مطابقة الكيانات**، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشروط المسبقة:** الحالة الحالية: MATCHED؛ reason + evidence; requester cleared for both entities
- **المدخلات:** `reason`!: string, `evidence`: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SPLIT_REQUIRED؛ الحدث EVT-ER-SPLIT-REQUESTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ الشروط: tenant match; cleared for both entity labels؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ER-REQUEST-SPLIT` · `AGG-ER-CASE` · متطلبات: REQ-INF-032, REQ-INF-033, REQ-INF-034 · حالات استخدام: UC-007, UC-104
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ER-REQUEST-SPLIT succeeds
  Given AGG-ER-CASE in state MATCHED and every guard holds
  When Analyst sends CMD-ER-REQUEST-SPLIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SPLIT_REQUIRED
  And EVT-ER-SPLIT-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ER-REQUEST-SPLIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ER-REQUEST-SPLIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ER_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANDIDATE, NOT_A_MATCH, POSSIBLE_DUPLICATE, SPLIT, SPLIT_REQUIRED, UNDER_REVIEW, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ER-RESUME — استئناف حالة مطابقة الكيانات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst (محسوم: `17-security-design.md` §5) | `POST /api/v1/information/er-cases/{id}/actions/resume` | POL-ER-RESUME |

**القصة:** بصفتي **Analyst**، أريد **استئناف حالة مطابقة الكيانات**، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشروط المسبقة:** الحالة الحالية: POSSIBLE_DUPLICATE؛ new evidence or reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← UNDER_REVIEW؛ الحدث EVT-ER-RESUMED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (resume)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ER-RESUME` · `AGG-ER-CASE` · متطلبات: REQ-INF-032, REQ-INF-033, REQ-INF-034 · حالات استخدام: UC-007, UC-104
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ER-RESUME succeeds
  Given AGG-ER-CASE in state POSSIBLE_DUPLICATE and every guard holds
  When Analyst sends CMD-ER-RESUME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNDER_REVIEW
  And EVT-ER-RESUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ER-RESUME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ER-RESUME ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ER_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANDIDATE, MATCHED, NOT_A_MATCH, SPLIT, SPLIT_REQUIRED, UNDER_REVIEW, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ER-SPLIT — فصل حالة مطابقة الكيانات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analyst · second Analyst | `POST /api/v1/information/er-cases/{id}/actions/split` | POL-ER-SPLIT |

**القصة:** بصفتي **Analyst · second Analyst**، أريد **فصل حالة مطابقة الكيانات**، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشروط المسبقة:** الحالة الحالية: SPLIT_REQUIRED؛ reviewer ≠ split requester; closes MATCH link (recorded_to = now); optional NOT_A_MATCH link; recomputes clusters in the same transaction
- **المدخلات:** `rationale`!: string, `record_not_a_match`!: boolean — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SPLIT؛ الحدث EVT-ER-SPLIT؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ الشروط: tenant match; object visible؛ فصل المهام: reviewer ≠ split requester؛ الالتزامات: audit
- **الربط:** `CMD-ER-SPLIT` · `AGG-ER-CASE` · متطلبات: REQ-INF-032, REQ-INF-033, REQ-INF-034 · حالات استخدام: UC-007, UC-104
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ER-SPLIT succeeds
  Given AGG-ER-CASE in state SPLIT_REQUIRED and every guard holds
  When an authorized actor (Analyst or second Analyst) sends CMD-ER-SPLIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SPLIT
  And EVT-ER-SPLIT is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ER-SPLIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ER-SPLIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ER_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANDIDATE, MATCHED, NOT_A_MATCH, POSSIBLE_DUPLICATE, SPLIT, UNDER_REVIEW, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: reviewer ≠ split requester |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: rationale, record_not_a_match |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ER-START-REVIEW — بدء مراجعة حالة مطابقة الكيانات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Analyst | `POST /api/v1/information/er-cases/{id}/actions/start-review` | POL-ER-START-REVIEW |

**القصة:** بصفتي **Analyst**، أريد **بدء مراجعة حالة مطابقة الكيانات**، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشروط المسبقة:** الحالة الحالية: CANDIDATE؛ reviewer cleared for both entity labels
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← UNDER_REVIEW؛ الحدث EVT-ER-REVIEW-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)؛ الشروط: tenant match; cleared for both entity labels؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ER-START-REVIEW` · `AGG-ER-CASE` · متطلبات: REQ-INF-032, REQ-INF-033, REQ-INF-034 · حالات استخدام: UC-007, UC-104
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ER-START-REVIEW succeeds
  Given AGG-ER-CASE in state CANDIDATE and every guard holds
  When Analyst sends CMD-ER-START-REVIEW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNDER_REVIEW
  And EVT-ER-REVIEW-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ER-START-REVIEW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ER-START-REVIEW ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ER_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: MATCHED, NOT_A_MATCH, POSSIBLE_DUPLICATE, SPLIT, SPLIT_REQUIRED, UNDER_REVIEW, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REVIEWER_NOT_CLEARED | 422 | لم يتحقق الشرط: reviewer cleared for both entity labels |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-ER-WITHDRAW — سحب حالة مطابقة الكيانات

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | Analyst (محسوم: `17-security-design.md` §5) | `POST /api/v1/information/er-cases/{id}/actions/withdraw` | POL-ER-WITHDRAW |

**القصة:** بصفتي **Analyst**، أريد **سحب حالة مطابقة الكيانات**، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشروط المسبقة:** الحالة الحالية: CANDIDATE, UNDER_REVIEW, POSSIBLE_DUPLICATE؛ reason (e.g. entity retired, duplicate case)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← WITHDRAWN؛ الحدث EVT-ER-WITHDRAWN؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (withdraw)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ER-WITHDRAW` · `AGG-ER-CASE` · متطلبات: REQ-INF-032, REQ-INF-033, REQ-INF-034 · حالات استخدام: UC-007, UC-104
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ER-WITHDRAW succeeds
  Given AGG-ER-CASE in state CANDIDATE or UNDER_REVIEW or POSSIBLE_DUPLICATE and every guard holds
  When Analyst sends CMD-ER-WITHDRAW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes WITHDRAWN
  And EVT-ER-WITHDRAWN is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ER-WITHDRAW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ER-WITHDRAW ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | ER_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: MATCHED, NOT_A_MATCH, SPLIT, SPLIT_REQUIRED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-S-ER-CASE-01 — تلقائي: candidate generator score ≥ propose threshold (حالة مطابقة الكيانات)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | ∅ | CANDIDATE |

**القصة:** بصفتي **النظام**، عند «candidate generator score ≥ propose threshold»، أريد نقل **حالة مطابقة الكيانات** إلى CANDIDATE، لكي يتحقق غرض حالة مطابقة الكيانات: حالة مطابقة بين كيانين؛ قرارها ينشئ أو يغلق روابط التطابق

- **الشرط:** pair not already in the same cluster; no NOT_A_MATCH link between their clusters; no non-terminal case for the pair
- **المخرجات:** الحدث EVT-ER-PROPOSED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ER-CASE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-Q-ER-GET — جلب: Case with side-by-side feature comparison (visible claims only)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | Analyst; both entities visible | `GET /api/v1/information/er-cases/{case_id}` | POL-ER-GET |

**القصة:** بصفتي **Analyst; both entities visible**، أريد **جلب Case with side-by-side feature comparison (visible claims only)**، لكي يتحقق المتطلب: When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, method, features, score and evidence, and shall not merge entities without a recorded decision

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Case with side-by-side feature comparison (visible claims only)
- **الصلاحية:** Analyst; both entities visible؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ER-GET` · `AGG-ER-CASE` · متطلبات: REQ-INF-032
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-ER-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-ER-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-ER-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-ER-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC02-Q-ER-QUEUE — جلب: Review queue by state, entity type, score, ruleset

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | Analyst; cases where both entities are visible | `GET /api/v1/information/er-cases` | POL-ER-QUEUE |

**القصة:** بصفتي **Analyst; cases where both entities are visible**، أريد **جلب Review queue by state, entity type, score, ruleset**، لكي يتحقق المتطلب: When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, method, features, score and evidence, and shall not merge entities without a recorded decision

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Review queue by state, entity type, score, ruleset؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Analyst; cases where both entities are visible؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ER-QUEUE` · `AGG-ER-CASE` · متطلبات: REQ-INF-032
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-ER-QUEUE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ER-QUEUE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ER-QUEUE is denied
  Given the policy denies the caller
  When the caller sends QRY-ER-QUEUE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-EVIDENCE — الدليل (Evidence)

`03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md` · SLC-02 · الحالات: REGISTERED, SEALED → WITHDRAWN

#### US-BC02-EVD-RECLASSIFY — إعادة تصنيف الدليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst | `POST /api/v1/information/evidence/{id}/actions/reclassify` | POL-EVD-RECLASSIFY |

**القصة:** بصفتي **Analyst**، أريد **إعادة تصنيف الدليل**، لكي يتحقق غرض الدليل: مادة تدعم أو تنفي ادعاءً، بسلسلة حيازة

- **الشروط المسبقة:** الحالة الحالية: REGISTERED, SEALED, WITHDRAWN؛ authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-EVD-RECLASSIFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · Field User (register) · custodian role (custody)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EVD-RECLASSIFY` · `AGG-EVIDENCE` · متطلبات: REQ-INF-003, REQ-INF-004 · حالات استخدام: UC-005, UC-006
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVD-RECLASSIFY succeeds
  Given AGG-EVIDENCE in state REGISTERED or SEALED or WITHDRAWN and every guard holds
  When Analyst sends CMD-EVD-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-EVD-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVD-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVD-RECLASSIFY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per tenant policy (REQ-GOV-004) |
    | EVIDENCE_INVALID_STATE_TRANSITION | 409 | لا حالة في المصفوفة يُرفض منها هذا الأمر؛ الرمز لا يُتوقع حدوثه |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-EVD-REGISTER — تسجيل الدليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst · Field User | `POST /api/v1/information/evidence` | POL-EVD-REGISTER |

**القصة:** بصفتي **Analyst · Field User**، أريد **تسجيل الدليل**، لكي يتحقق غرض الدليل: مادة تدعم أو تنفي ادعاءً، بسلسلة حيازة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ attachment STORED or observation_ref; type in RD-EVIDENCE-TYPES; source ACTIVE
- **المدخلات:** `client_id`: string, `evidence_type`!: string, `attachment`: urn, `observation_ref`: urn, `locator`: object, `source`!: urn, `collected_at`!: date-time, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← REGISTERED؛ الحدث EVT-EVD-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · Field User (register) · custodian role (custody)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EVD-REGISTER` · `AGG-EVIDENCE` · متطلبات: REQ-INF-003, REQ-INF-004 · حالات استخدام: UC-005, UC-006
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVD-REGISTER succeeds
  Given AGG-EVIDENCE does not exist yet and every guard holds
  When an authorized actor (Analyst or Field User) sends CMD-EVD-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes REGISTERED
  And EVT-EVD-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVD-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVD-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVIDENCE_INVALID | 422 | لم يتحقق الشرط: type in RD-EVIDENCE-TYPES |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: evidence_type, source, collected_at, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-EVD-SEAL — ختم الدليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst | `POST /api/v1/information/evidence/{id}/actions/seal` | POL-EVD-SEAL |

**القصة:** بصفتي **Analyst**، أريد **ختم الدليل**، لكي يتحقق غرض الدليل: مادة تدعم أو تنفي ادعاءً، بسلسلة حيازة

- **الشروط المسبقة:** الحالة الحالية: REGISTERED؛ integrity hash over metadata + attachment hash
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SEALED؛ الحدث EVT-EVD-SEALED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · Field User (register) · custodian role (custody)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EVD-SEAL` · `AGG-EVIDENCE` · متطلبات: REQ-INF-003, REQ-INF-004 · حالات استخدام: UC-005, UC-006
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVD-SEAL succeeds
  Given AGG-EVIDENCE in state REGISTERED and every guard holds
  When Analyst sends CMD-EVD-SEAL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SEALED
  And EVT-EVD-SEALED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVD-SEAL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVD-SEAL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVIDENCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: SEALED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-EVD-TRANSFER-CUSTODY — نقل عهدة الدليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | custodian role | `POST /api/v1/information/evidence/{id}/actions/transfer-custody` | POL-EVD-TRANSFER-CUSTODY |

**القصة:** بصفتي **custodian role**، أريد **نقل عهدة الدليل**، لكي يتحقق غرض الدليل: مادة تدعم أو تنفي ادعاءً، بسلسلة حيازة

- **الشروط المسبقة:** الحالة الحالية: REGISTERED, SEALED؛ actor is current holder or custodian role; new holder named
- **المدخلات:** `new_holder`!: urn, `action`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-EVD-CUSTODY-TRANSFERRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · Field User (register) · custodian role (custody)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EVD-TRANSFER-CUSTODY` · `AGG-EVIDENCE` · متطلبات: REQ-INF-003, REQ-INF-004 · حالات استخدام: UC-005, UC-006
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVD-TRANSFER-CUSTODY succeeds
  Given AGG-EVIDENCE in state REGISTERED or SEALED and every guard holds
  When custodian role sends CMD-EVD-TRANSFER-CUSTODY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-EVD-CUSTODY-TRANSFERRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVD-TRANSFER-CUSTODY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVD-TRANSFER-CUSTODY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CUSTODY_INVALID | 422 | لم يتحقق الشرط: actor is current holder or custodian role |
    | EVIDENCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: new_holder, action |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-EVD-UPDATE-LOCATOR — تحديث محدِّد موقع الدليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst | `POST /api/v1/information/evidence/{id}/actions/update-locator` | POL-EVD-UPDATE-LOCATOR |

**القصة:** بصفتي **Analyst**، أريد **تحديث محدِّد موقع الدليل**، لكي يتحقق غرض الدليل: مادة تدعم أو تنفي ادعاءً، بسلسلة حيازة

- **الشروط المسبقة:** الحالة الحالية: REGISTERED؛ locator within attachment bounds
- **المدخلات:** `locator`!: object — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-EVD-LOCATOR-UPDATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · Field User (register) · custodian role (custody)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EVD-UPDATE-LOCATOR` · `AGG-EVIDENCE` · متطلبات: REQ-INF-003, REQ-INF-004 · حالات استخدام: UC-005, UC-006
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVD-UPDATE-LOCATOR succeeds
  Given AGG-EVIDENCE in state REGISTERED and every guard holds
  When Analyst sends CMD-EVD-UPDATE-LOCATOR with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-EVD-LOCATOR-UPDATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVD-UPDATE-LOCATOR is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVD-UPDATE-LOCATOR ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVIDENCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: SEALED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LOCATOR_INVALID | 422 | لم يتحقق الشرط: locator within attachment bounds |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: locator |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-EVD-WITHDRAW — سحب الدليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst | `POST /api/v1/information/evidence/{id}/actions/withdraw` | POL-EVD-WITHDRAW |

**القصة:** بصفتي **Analyst**، أريد **سحب الدليل**، لكي يتحقق غرض الدليل: مادة تدعم أو تنفي ادعاءً، بسلسلة حيازة

- **الشروط المسبقة:** الحالة الحالية: REGISTERED, SEALED؛ reason (e.g. forged); links kept and flagged; dependent verification re-evaluated
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← WITHDRAWN؛ الحدث EVT-EVD-WITHDRAWN؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · Field User (register) · custodian role (custody)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit; notify owners of dependent claims
- **الربط:** `CMD-EVD-WITHDRAW` · `AGG-EVIDENCE` · متطلبات: REQ-INF-003, REQ-INF-004 · حالات استخدام: UC-005, UC-006
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVD-WITHDRAW succeeds
  Given AGG-EVIDENCE in state REGISTERED or SEALED and every guard holds
  When Analyst sends CMD-EVD-WITHDRAW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes WITHDRAWN
  And EVT-EVD-WITHDRAWN is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVD-WITHDRAW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVD-WITHDRAW ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVIDENCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-Q-EVD-GET — جلب: Evidence metadata and custody chain

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user; label-filtered | `GET /api/v1/information/evidence/{evidence_id}` | POL-EVD-GET |

**القصة:** بصفتي **any user; label-filtered**، أريد **جلب Evidence metadata and custody chain**، لكي يتحقق المتطلب: When an attachment is stored or retrieved, the system shall compute or verify its content hash

- **المدخلات:** `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Evidence metadata and custody chain
- **الصلاحية:** any user; label-filtered؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-EVD-GET` · `AGG-EVIDENCE` · متطلبات: REQ-INF-004
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-EVD-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-EVD-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-EVD-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-EVD-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-EVIDENCE-LINK — رابط الدليل (Evidence Link)

`03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md` · SLC-02 · الحالات: ACTIVE → REMOVED

#### US-BC02-EVL-LINK — ربط رابط الدليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst | `POST /api/v1/information/evidence-links` | POL-EVL-LINK |

**القصة:** بصفتي **Analyst**، أريد **ربط رابط الدليل**، لكي يتحقق غرض رابط الدليل: ربط دليل بادعاء (يدعم / ينفي / سياق)

- **الشروط المسبقة:** الحالة الحالية: ∅؛ evidence not WITHDRAWN; claim exists; stance ∈ {SUPPORTS, REFUTES, CONTEXT}; no ACTIVE duplicate (evidence, claim, stance)
- **المدخلات:** `evidence`!: urn, `claim`!: urn, `stance`!: enum(SUPPORTS,REFUTES,CONTEXT), `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-EVL-LINKED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EVL-LINK` · `AGG-EVIDENCE-LINK` · متطلبات: REQ-INF-021 · حالات استخدام: UC-006
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVL-LINK succeeds
  Given AGG-EVIDENCE-LINK does not exist yet and every guard holds
  When Analyst sends CMD-EVL-LINK with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-EVL-LINKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVL-LINK is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVL-LINK ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LINK_DUPLICATE | 422 | لم يتحقق الشرط: no ACTIVE duplicate (evidence, claim, stance) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: evidence, claim, stance |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-EVL-UNLINK — فك ربط رابط الدليل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst | `POST /api/v1/information/evidence-links/{id}/actions/unlink` | POL-EVL-UNLINK |

**القصة:** بصفتي **Analyst**، أريد **فك ربط رابط الدليل**، لكي يتحقق غرض رابط الدليل: ربط دليل بادعاء (يدعم / ينفي / سياق)

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason; recorded_to closed
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← REMOVED؛ الحدث EVT-EVL-UNLINKED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EVL-UNLINK` · `AGG-EVIDENCE-LINK` · متطلبات: REQ-INF-021 · حالات استخدام: UC-006
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVL-UNLINK succeeds
  Given AGG-EVIDENCE-LINK in state ACTIVE and every guard holds
  When Analyst sends CMD-EVL-UNLINK with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REMOVED
  And EVT-EVL-UNLINKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVL-UNLINK is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVL-UNLINK ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVIDENCE_LINK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: REMOVED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

### AGG-EXTERNAL-ID — ربط المعرّف الخارجي (External Identifier Mapping)

`03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md` · SLC-02 · الحالات: ACTIVE → ENDED

#### US-BC02-EXT-END — إنهاء ربط المعرّف الخارجي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | adapter service account · Analyst | `POST /api/v1/information/external-ids/{id}/actions/end` | POL-EXT-END |

**القصة:** بصفتي **adapter service account · Analyst**، أريد **إنهاء ربط المعرّف الخارجي**، لكي يتحقق غرض ربط المعرّف الخارجي: ربط معرّف نظام خارجي بكائن داخلي لفترة

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason; valid_to set
- **المدخلات:** `valid_to`!: date-time, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ENDED؛ الحدث EVT-EXT-ENDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** adapter service account · Analyst؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EXT-END` · `AGG-EXTERNAL-ID` · متطلبات: REQ-INF-036 · حالات استخدام: —
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EXT-END succeeds
  Given AGG-EXTERNAL-ID in state ACTIVE and every guard holds
  When an authorized actor (adapter service account or Analyst) sends CMD-EXT-END with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ENDED
  And EVT-EXT-ENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EXT-END is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EXT-END ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EXTERNAL_ID_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ENDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: valid_to, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-EXT-MAP — تسجيل ربط ربط المعرّف الخارجي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تكامل | adapter service account · Analyst | `POST /api/v1/information/external-ids` | POL-EXT-MAP |

**القصة:** بصفتي **adapter service account · Analyst**، أريد **تسجيل ربط ربط المعرّف الخارجي**، لكي يتحقق غرض ربط المعرّف الخارجي: ربط معرّف نظام خارجي بكائن داخلي لفترة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ (system, external_id) has no ACTIVE mapping; target exists
- **المدخلات:** `system`!: string, `external_id`!: string, `object`!: urn, `valid_from`!: date-time — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-EXT-MAPPED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** adapter service account · Analyst؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EXT-MAP` · `AGG-EXTERNAL-ID` · متطلبات: REQ-INF-036 · حالات استخدام: —
- **ضوابط النوع والفئة:** C-CRE، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EXT-MAP succeeds
  Given AGG-EXTERNAL-ID does not exist yet and every guard holds
  When an authorized actor (adapter service account or Analyst) sends CMD-EXT-MAP with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-EXT-MAPPED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EXT-MAP is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EXT-MAP ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EXTERNAL_ID_TAKEN | 422 | لم يتحقق الشرط: (system, external_id) has no ACTIVE mapping |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: system, external_id, object, valid_from |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-Q-EXT-RESOLVE — جلب: Object URN mapped at time t (not-found shape if hidden)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | adapter service accounts; Analyst | `GET /api/v1/information/external-ids/{system}/{external_id}` | POL-EXT-RESOLVE |

**القصة:** بصفتي **adapter service accounts; Analyst**، أريد **جلب Object URN mapped at time t (not-found shape if hidden)**، لكي يتحقق المتطلب: The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type>:<id>, and shall map external identifiers per source system

- **المدخلات:** `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Object URN mapped at time t (not-found shape if hidden)
- **الصلاحية:** adapter service accounts; Analyst؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-EXT-RESOLVE` · `AGG-EXTERNAL-ID` · متطلبات: REQ-INF-036
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-EXT-RESOLVE returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-EXT-RESOLVE
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-EXT-RESOLVE hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-EXT-RESOLVE
  Then the response is 404 with the same shape as for a missing item
```

### AGG-IMPORT-BATCH — دفعة الاستيراد (Import Batch)

`03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md` · SLC-02 · الحالات: RECEIVED, PROCESSING, COMPLETED_WITH_QUARANTINE → COMPLETED, FAILED, CANCELLED

#### US-BC02-IMP-ACCEPT-QUARANTINE — قبول العناصر المعزولة في دفعة الاستيراد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | adapter service account · Administrator | `POST /api/v1/information/import-batches/{id}/actions/accept-quarantine` | POL-IMP-ACCEPT-QUARANTINE |

**القصة:** بصفتي **adapter service account · Administrator**، أريد **قبول العناصر المعزولة في دفعة الاستيراد**، لكي يتحقق غرض دفعة الاستيراد: دفعة استيراد من محول أو ملف، مع حجر وlineage

- **الشروط المسبقة:** الحالة الحالية: COMPLETED_WITH_QUARANTINE؛ reason; quarantined records dropped, record kept
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← COMPLETED؛ الحدث EVT-IMP-QUARANTINE-ACCEPTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** adapter service account · Administrator؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-IMP-ACCEPT-QUARANTINE` · `AGG-IMPORT-BATCH` · متطلبات: REQ-INF-005, REQ-INF-006, REQ-INF-007, REQ-INF-008, REQ-INF-009 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-IMP-ACCEPT-QUARANTINE succeeds
  Given AGG-IMPORT-BATCH in state COMPLETED_WITH_QUARANTINE and every guard holds
  When an authorized actor (adapter service account or Administrator) sends CMD-IMP-ACCEPT-QUARANTINE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes COMPLETED
  And EVT-IMP-QUARANTINE-ACCEPTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-IMP-ACCEPT-QUARANTINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-IMP-ACCEPT-QUARANTINE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | IMPORT_BATCH_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, FAILED, PROCESSING, RECEIVED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-IMP-CANCEL — إلغاء دفعة الاستيراد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | adapter service account · Administrator | `POST /api/v1/information/import-batches/{id}/actions/cancel` | POL-IMP-CANCEL |

**القصة:** بصفتي **adapter service account · Administrator**، أريد **إلغاء دفعة الاستيراد**، لكي يتحقق غرض دفعة الاستيراد: دفعة استيراد من محول أو ملف، مع حجر وlineage

- **الشروط المسبقة:** الحالة الحالية: RECEIVED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-IMP-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** adapter service account · Administrator؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-IMP-CANCEL` · `AGG-IMPORT-BATCH` · متطلبات: REQ-INF-005, REQ-INF-006, REQ-INF-007, REQ-INF-008, REQ-INF-009 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-IMP-CANCEL succeeds
  Given AGG-IMPORT-BATCH in state RECEIVED and every guard holds
  When an authorized actor (adapter service account or Administrator) sends CMD-IMP-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-IMP-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-IMP-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-IMP-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | IMPORT_BATCH_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, COMPLETED_WITH_QUARANTINE, FAILED, PROCESSING |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-IMP-REPROCESS-QUARANTINE — إعادة معالجة العناصر المعزولة في دفعة الاستيراد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | adapter service account · Administrator | `POST /api/v1/information/import-batches/{id}/actions/reprocess-quarantine` | POL-IMP-REPROCESS-QUARANTINE |

**القصة:** بصفتي **adapter service account · Administrator**، أريد **إعادة معالجة العناصر المعزولة في دفعة الاستيراد**، لكي يتحقق غرض دفعة الاستيراد: دفعة استيراد من محول أو ملف، مع حجر وlineage

- **الشروط المسبقة:** الحالة الحالية: COMPLETED_WITH_QUARANTINE؛ new mapping version or corrected records
- **المدخلات:** `mapping_version`: string, `corrections`: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PROCESSING؛ الحدث EVT-IMP-REPROCESSING؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** adapter service account · Administrator؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-IMP-REPROCESS-QUARANTINE` · `AGG-IMPORT-BATCH` · متطلبات: REQ-INF-005, REQ-INF-006, REQ-INF-007, REQ-INF-008, REQ-INF-009 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-IMP-REPROCESS-QUARANTINE succeeds
  Given AGG-IMPORT-BATCH in state COMPLETED_WITH_QUARANTINE and every guard holds
  When an authorized actor (adapter service account or Administrator) sends CMD-IMP-REPROCESS-QUARANTINE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PROCESSING
  And EVT-IMP-REPROCESSING is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-IMP-REPROCESS-QUARANTINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-IMP-REPROCESS-QUARANTINE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | IMPORT_BATCH_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, FAILED, PROCESSING, RECEIVED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-IMP-SUBMIT — تقديم دفعة الاستيراد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تكامل | adapter service account · Administrator | `POST /api/v1/information/import-batches` | POL-IMP-SUBMIT |

**القصة:** بصفتي **adapter service account · Administrator**، أريد **تقديم دفعة الاستيراد**، لكي يتحقق غرض دفعة الاستيراد: دفعة استيراد من محول أو ملف، مع حجر وlineage

- **الشروط المسبقة:** الحالة الحالية: ∅؛ adapter ACTIVE (or authorized manual import); batch_key unique per adapter: same key + same content hash returns the existing batch; different hash → rejected
- **المدخلات:** `adapter`!: urn, `batch_key`!: string, `content_sha256`!: string, `format`!: string, `payload_attachment`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← RECEIVED؛ الحدث EVT-IMP-RECEIVED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** adapter service account · Administrator؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-IMP-SUBMIT` · `AGG-IMPORT-BATCH` · متطلبات: REQ-INF-005, REQ-INF-006, REQ-INF-007, REQ-INF-008, REQ-INF-009 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-CRE، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-IMP-SUBMIT succeeds
  Given AGG-IMPORT-BATCH does not exist yet and every guard holds
  When an authorized actor (adapter service account or Administrator) sends CMD-IMP-SUBMIT with a valid payload, a new Idempotency-Key
  Then the state becomes RECEIVED
  And EVT-IMP-RECEIVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-IMP-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-IMP-SUBMIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | BATCH_KEY_REUSED | 422 | لم يتحقق الشرط: batch_key unique per adapter: same key + same content hash returns the existing batch |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: adapter, batch_key, content_sha256, format, payload_attachment |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-S-IMPORT-BATCH-01 — تلقائي: processing started (دفعة الاستيراد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | RECEIVED | PROCESSING |

**القصة:** بصفتي **النظام**، عند «processing started»، أريد نقل **دفعة الاستيراد** إلى PROCESSING، لكي يتحقق غرض دفعة الاستيراد: دفعة استيراد من محول أو ملف، مع حجر وlineage

- **الشرط:** worker lease acquired
- **المخرجات:** الحدث EVT-IMP-PROCESSING-STARTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-IMPORT-BATCH` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-S-IMPORT-BATCH-02 — تلقائي: all records applied (دفعة الاستيراد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | PROCESSING | COMPLETED |

**القصة:** بصفتي **النظام**، عند «all records applied»، أريد نقل **دفعة الاستيراد** إلى COMPLETED، لكي يتحقق غرض دفعة الاستيراد: دفعة استيراد من محول أو ملف، مع حجر وlineage

- **الشرط:** each record applied idempotently with lineage (adapter, batch, mapping version)
- **المخرجات:** الحدث EVT-IMP-COMPLETED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-IMPORT-BATCH` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-S-IMPORT-BATCH-03 — تلقائي: finished with invalid records (دفعة الاستيراد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | PROCESSING | COMPLETED_WITH_QUARANTINE |

**القصة:** بصفتي **النظام**، عند «finished with invalid records»، أريد نقل **دفعة الاستيراد** إلى COMPLETED_WITH_QUARANTINE، لكي يتحقق غرض دفعة الاستيراد: دفعة استيراد من محول أو ملف، مع حجر وlineage

- **الشرط:** invalid records quarantined with reason codes
- **المخرجات:** الحدث EVT-IMP-COMPLETED-WITH-QUARANTINE؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-IMPORT-BATCH` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-S-IMPORT-BATCH-04 — تلقائي: unrecoverable error (دفعة الاستيراد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | PROCESSING | FAILED |

**القصة:** بصفتي **النظام**، عند «unrecoverable error»، أريد نقل **دفعة الاستيراد** إلى FAILED، لكي يتحقق غرض دفعة الاستيراد: دفعة استيراد من محول أو ملف، مع حجر وlineage

- **الشرط:** applied records remain; re-submit resumes idempotently
- **المخرجات:** الحدث EVT-IMP-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-IMPORT-BATCH` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-Q-IMP-GET — جلب: Batch status, counts, quarantine records (paged)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | adapter owner; Administrator | `GET /api/v1/information/import-batches/{batch_id}` | POL-IMP-GET |

**القصة:** بصفتي **adapter owner; Administrator**، أريد **جلب Batch status, counts, quarantine records (paged)**، لكي يتحقق المتطلب: If an ingested record fails validation, then the system shall quarantine it with the failure reason and shall not publish it

- **المدخلات:** `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Batch status, counts, quarantine records (paged)
- **الصلاحية:** adapter owner; Administrator؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-IMP-GET` · `AGG-IMPORT-BATCH` · متطلبات: REQ-INF-006
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-IMP-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-IMP-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-IMP-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-IMP-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-MATCH-RULESET — مجموعة قواعد المطابقة (Match Ruleset)

`03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md` · SLC-04 · الحالات: DRAFT, ACTIVE → SUPERSEDED

#### US-BC02-MRS-ACTIVATE — تفعيل مجموعة قواعد المطابقة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | Administrator ≠ author | `POST /api/v1/information/match-rulesets/{id}/actions/activate` | POL-MRS-ACTIVATE |

**القصة:** بصفتي **Administrator ≠ author**، أريد **تفعيل مجموعة قواعد المطابقة**، لكي يتحقق غرض مجموعة قواعد المطابقة: قواعد توليد المرشحين (الحجب والسمات والأوزان والعتبات) لكل نوع كيان

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ evaluation meets QAS-ER-001 (candidate recall ≥ 95 %) and QAS-ER-002; approver ≠ author; previous ACTIVE → SUPERSEDED
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-MRS-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead (draft, edit) · Administrator ≠ author (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: approver ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-MRS-ACTIVATE` · `AGG-MATCH-RULESET` · متطلبات: REQ-INF-032, REQ-SRC-003 · حالات استخدام: UC-007, UC-097
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MRS-ACTIVATE succeeds
  Given AGG-MATCH-RULESET in state DRAFT and every guard holds
  When Administrator ≠ author sends CMD-MRS-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-MRS-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MRS-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MRS-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MATCH_RULESET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, SUPERSEDED |
    | RULESET_BELOW_TARGET | 422 | لم يتحقق الشرط: evaluation meets QAS-ER-001 (candidate recall ≥ 95 %) and QAS-ER-002; approver ≠ author; previous ACTIVE → SUPERSEDED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-MRS-DRAFT — إعداد مسودة مجموعة قواعد المطابقة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | Analyst lead | `POST /api/v1/information/match-rulesets` | POL-MRS-DRAFT |

**القصة:** بصفتي **Analyst lead**، أريد **إعداد مسودة مجموعة قواعد المطابقة**، لكي يتحقق غرض مجموعة قواعد المطابقة: قواعد توليد المرشحين (الحجب والسمات والأوزان والعتبات) لكل نوع كيان

- **الشروط المسبقة:** الحالة الحالية: ∅؛ entity type exists
- **المدخلات:** `entity_type`!: string, `based_on`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-MRS-DRAFTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead (draft, edit) · Administrator ≠ author (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MRS-DRAFT` · `AGG-MATCH-RULESET` · متطلبات: REQ-INF-032, REQ-SRC-003 · حالات استخدام: UC-007, UC-097
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MRS-DRAFT succeeds
  Given AGG-MATCH-RULESET does not exist yet and every guard holds
  When Analyst lead sends CMD-MRS-DRAFT with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-MRS-DRAFTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MRS-DRAFT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MRS-DRAFT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: entity_type |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-MRS-EDIT — تعديل مجموعة قواعد المطابقة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تحليل | Analyst lead | `POST /api/v1/information/match-rulesets/{id}/actions/edit` | POL-MRS-EDIT |

**القصة:** بصفتي **Analyst lead**، أريد **تعديل مجموعة قواعد المطابقة**، لكي يتحقق غرض مجموعة قواعد المطابقة: قواعد توليد المرشحين (الحجب والسمات والأوزان والعتبات) لكل نوع كيان

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ blocking keys, features, weights, thresholds valid; evaluation run on labelled test set attached
- **المدخلات:** `blocking_keys`!: array, `features`!: array, `thresholds`!: object, `evaluation_attachment`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-MRS-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst lead (draft, edit) · Administrator ≠ author (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MRS-EDIT` · `AGG-MATCH-RULESET` · متطلبات: REQ-INF-032, REQ-SRC-003 · حالات استخدام: UC-007, UC-097
- **ضوابط النوع والفئة:** C-UPD، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MRS-EDIT succeeds
  Given AGG-MATCH-RULESET in state DRAFT and every guard holds
  When Analyst lead sends CMD-MRS-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-MRS-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MRS-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MRS-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MATCH_RULESET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, SUPERSEDED |
    | RULESET_INVALID | 422 | لم يتحقق الشرط: blocking keys, features, weights, thresholds valid; evaluation run on labelled test set attached |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: blocking_keys, features, thresholds, evaluation_attachment |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-S-MATCH-RULESET-01 — تلقائي: successor activated (مجموعة قواعد المطابقة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ACTIVE | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «successor activated»، أريد نقل **مجموعة قواعد المطابقة** إلى SUPERSEDED، لكي يتحقق غرض مجموعة قواعد المطابقة: قواعد توليد المرشحين (الحجب والسمات والأوزان والعتبات) لكل نوع كيان

- **الشرط:** system
- **المخرجات:** الحدث EVT-MRS-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-MATCH-RULESET` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC02-Q-MRS-GET — جلب: Ruleset with evaluation report

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | Analyst lead, Administrator | `GET /api/v1/information/match-rulesets/{ruleset_id}` | POL-MRS-GET |

**القصة:** بصفتي **Analyst lead, Administrator**، أريد **جلب Ruleset with evaluation report**، لكي يتحقق المتطلب: When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, method, features, score and evidence, and shall not merge entities without a recorded decision

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Ruleset with evaluation report
- **الصلاحية:** Analyst lead, Administrator؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-MRS-GET` · `AGG-MATCH-RULESET` · متطلبات: REQ-INF-032
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-MRS-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-MRS-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-MRS-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-MRS-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-OBSERVATION — الملاحظة (Observation)

`03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md` · SLC-02 · الحالات: RECORDED → VALIDATED, REJECTED

#### US-BC02-OBS-AMEND — تعديل الملاحظة بإصدار جديد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Field User / Operator / Analyst / adapter service account (محسوم: `17-security-design.md` §5) | `POST /api/v1/information/observations/{id}/actions/amend` | POL-OBS-AMEND |

**القصة:** بصفتي **Field User / Operator / Analyst / adapter service account**، أريد **تعديل الملاحظة بإصدار جديد**، لكي يتحقق غرض الملاحظة: ما رصده مصدر في زمن ومكان؛ غير قابل للتعديل بعد الاعتماد

- **الشروط المسبقة:** الحالة الحالية: RECORDED؛ actor = observer or Analyst; new version; reason
- **المدخلات:** `changes`!: object, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-OBS-AMENDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Field User / Operator / Analyst / adapter service account (amend)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-OBS-AMEND` · `AGG-OBSERVATION` · متطلبات: REQ-INF-002, REQ-INF-028 · حالات استخدام: UC-005
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-OBS-AMEND succeeds
  Given AGG-OBSERVATION in state RECORDED and every guard holds
  When Field User / Operator / Analyst / adapter service account sends CMD-OBS-AMEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-OBS-AMENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-OBS-AMEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-OBS-AMEND ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OBSERVATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: REJECTED, VALIDATED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: changes, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-OBS-ATTACH-EVIDENCE — إرفاق دليل بـالملاحظة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Field User / Operator / Analyst / adapter service account (محسوم: `17-security-design.md` §5) | `POST /api/v1/information/observations/{id}/actions/attach-evidence` | POL-OBS-ATTACH-EVIDENCE |

**القصة:** بصفتي **Field User / Operator / Analyst / adapter service account**، أريد **إرفاق دليل بـالملاحظة**، لكي يتحقق غرض الملاحظة: ما رصده مصدر في زمن ومكان؛ غير قابل للتعديل بعد الاعتماد

- **الشروط المسبقة:** الحالة الحالية: RECORDED؛ evidence REGISTERED or SEALED
- **المدخلات:** `evidence`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-OBS-EVIDENCE-ATTACHED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Field User / Operator / Analyst / adapter service account (attach evidence)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-OBS-ATTACH-EVIDENCE` · `AGG-OBSERVATION` · متطلبات: REQ-INF-002, REQ-INF-028 · حالات استخدام: UC-005
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-OBS-ATTACH-EVIDENCE succeeds
  Given AGG-OBSERVATION in state RECORDED and every guard holds
  When Field User / Operator / Analyst / adapter service account sends CMD-OBS-ATTACH-EVIDENCE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-OBS-EVIDENCE-ATTACHED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-OBS-ATTACH-EVIDENCE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-OBS-ATTACH-EVIDENCE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVIDENCE_INVALID | 422 | لم يتحقق الشرط: evidence REGISTERED or SEALED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OBSERVATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: REJECTED, VALIDATED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: evidence |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-OBS-RECLASSIFY — إعادة تصنيف الملاحظة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst (محسوم: `17-security-design.md` §5) | `POST /api/v1/information/observations/{id}/actions/reclassify` | POL-OBS-RECLASSIFY |

**القصة:** بصفتي **Analyst**، أريد **إعادة تصنيف الملاحظة**، لكي يتحقق غرض الملاحظة: ما رصده مصدر في زمن ومكان؛ غير قابل للتعديل بعد الاعتماد

- **الشروط المسبقة:** الحالة الحالية: RECORDED, VALIDATED, REJECTED؛ authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-OBS-RECLASSIFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (reclassify)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-OBS-RECLASSIFY` · `AGG-OBSERVATION` · متطلبات: REQ-INF-002, REQ-INF-028 · حالات استخدام: UC-005
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-OBS-RECLASSIFY succeeds
  Given AGG-OBSERVATION in state RECORDED or VALIDATED or REJECTED and every guard holds
  When Analyst sends CMD-OBS-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-OBS-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-OBS-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-OBS-RECLASSIFY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per tenant policy (REQ-GOV-004) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OBSERVATION_INVALID_STATE_TRANSITION | 409 | لا حالة في المصفوفة يُرفض منها هذا الأمر؛ الرمز لا يُتوقع حدوثه |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-OBS-RECORD — تسجيل الملاحظة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Field User / Operator / Analyst / adapter service account | `POST /api/v1/information/observations` | POL-OBS-RECORD |

**القصة:** بصفتي **Field User / Operator / Analyst / adapter service account**، أريد **تسجيل الملاحظة**، لكي يتحقق غرض الملاحظة: ما رصده مصدر في زمن ومكان؛ غير قابل للتعديل بعد الاعتماد

- **الشروط المسبقة:** الحالة الحالية: ∅؛ source ACTIVE; location with CRS + accuracy + valid geometry; UCUM units; observed_at ≤ server time + 5 min; recorded_from by server
- **المدخلات:** `client_id`: string, `source`!: urn, `observer`!: urn, `observed_at`!: date-time, `event_time`: FuzzyInterval, `location`!: SpatialEnvelope, `method`!: string, `measurements`: array, `narrative`: LocalizedName, `attachments`: array, `label`!: Label, `field_session`: urn, `device`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← RECORDED؛ الحدث EVT-OBS-RECORDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-OBS-RECORD` · `AGG-OBSERVATION` · متطلبات: REQ-INF-002, REQ-INF-028 · حالات استخدام: UC-005
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-OBS-RECORD succeeds
  Given AGG-OBSERVATION does not exist yet and every guard holds
  When Field User / Operator / Analyst / adapter service account sends CMD-OBS-RECORD with a valid payload, a new Idempotency-Key
  Then the state becomes RECORDED
  And EVT-OBS-RECORDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-OBS-RECORD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-OBS-RECORD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OBSERVATION_INVALID | 422 | لم يتحقق الشرط: observed_at ≤ server time + 5 min |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: source, observer, observed_at, location, method, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-OBS-REJECT — رفض الملاحظة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst | `POST /api/v1/information/observations/{id}/actions/reject` | POL-OBS-REJECT |

**القصة:** بصفتي **Analyst**، أريد **رفض الملاحظة**، لكي يتحقق غرض الملاحظة: ما رصده مصدر في زمن ومكان؛ غير قابل للتعديل بعد الاعتماد

- **الشروط المسبقة:** الحالة الحالية: RECORDED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-OBS-REJECTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-OBS-REJECT` · `AGG-OBSERVATION` · متطلبات: REQ-INF-002, REQ-INF-028 · حالات استخدام: UC-005
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-OBS-REJECT succeeds
  Given AGG-OBSERVATION in state RECORDED and every guard holds
  When Analyst sends CMD-OBS-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-OBS-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-OBS-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-OBS-REJECT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OBSERVATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: REJECTED, VALIDATED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-OBS-VALIDATE — التحقق من الملاحظة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst | `POST /api/v1/information/observations/{id}/actions/validate` | POL-OBS-VALIDATE |

**القصة:** بصفتي **Analyst**، أريد **التحقق من الملاحظة**، لكي يتحقق غرض الملاحظة: ما رصده مصدر في زمن ومكان؛ غير قابل للتعديل بعد الاعتماد

- **الشروط المسبقة:** الحالة الحالية: RECORDED؛ Analyst ≠ observer, or system auto-validation for sensor sources rated A/B under tenant policy
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← VALIDATED؛ الحدث EVT-OBS-VALIDATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: validator ≠ observer (unless system auto-validation policy)؛ الالتزامات: audit
- **الربط:** `CMD-OBS-VALIDATE` · `AGG-OBSERVATION` · متطلبات: REQ-INF-002, REQ-INF-028 · حالات استخدام: UC-005
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-OBS-VALIDATE succeeds
  Given AGG-OBSERVATION in state RECORDED and every guard holds
  When Analyst sends CMD-OBS-VALIDATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes VALIDATED
  And EVT-OBS-VALIDATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-OBS-VALIDATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-OBS-VALIDATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OBSERVATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: REJECTED, VALIDATED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: validator ≠ observer (unless system auto-validation policy) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-Q-OBS-GET — جلب: Observation with measurements and attachment refs

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user; label-filtered | `GET /api/v1/information/observations/{observation_id}` | POL-OBS-GET |

**القصة:** بصفتي **any user; label-filtered**، أريد **جلب Observation with measurements and attachment refs**، لكي يتحقق المتطلب: When an observation is recorded, the system shall store its observation time, its event time where known, its record time, its location with CRS and positional accuracy, its source, its observer and its attachments

- **المدخلات:** `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Observation with measurements and attachment refs
- **الصلاحية:** any user; label-filtered؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-OBS-GET` · `AGG-OBSERVATION` · متطلبات: REQ-INF-002
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-OBS-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-OBS-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-OBS-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-OBS-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC02-Q-OBS-LIST — جلب: Observations by bbox, time window (mandatory, ≤ 31 days), source, state

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/information/observations` | POL-OBS-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Observations by bbox, time window (mandatory, ≤ 31 days), source, state**، لكي يتحقق المتطلب: When an observation is recorded, the system shall store its observation time, its event time where known, its record time, its location with CRS and positional accuracy, its source, its observer and its attachments

- **المدخلات:** `valid_at`, `known_at`, `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Observations by bbox, time window (mandatory, ≤ 31 days), source, state؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user; allowed_scope pre-filter؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-OBS-LIST` · `AGG-OBSERVATION` · متطلبات: REQ-INF-002
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-OBS-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-OBS-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-OBS-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-OBS-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-REALWORLD-EVENT — الحدث الواقعي (Real-World Event (identity))

`03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md` · SLC-02 · الحالات: ACTIVE, RETIRED → —

#### US-BC02-RWE-CHANGE-TYPE — تغيير نوع الحدث الواقعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst · adapter service account | `POST /api/v1/information/events/{id}/actions/change-type` | POL-RWE-CHANGE-TYPE |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **تغيير نوع الحدث الواقعي**، لكي يتحقق غرض الحدث الواقعي: حدث وقع في العالم (ليس Domain Event)

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ compatible type; reason
- **المدخلات:** `event_type`!: string, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-RWE-TYPE-CHANGED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RWE-CHANGE-TYPE` · `AGG-REALWORLD-EVENT` · متطلبات: REQ-INF-020 · حالات استخدام: UC-001, UC-002, UC-003
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RWE-CHANGE-TYPE succeeds
  Given AGG-REALWORLD-EVENT in state ACTIVE and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-RWE-CHANGE-TYPE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-RWE-TYPE-CHANGED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RWE-CHANGE-TYPE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RWE-CHANGE-TYPE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVENT_TYPE_INCOMPATIBLE | 422 | لم يتحقق الشرط: compatible type |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REALWORLD_EVENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: event_type, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-RWE-RECLASSIFY — إعادة تصنيف الحدث الواقعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst · adapter service account | `POST /api/v1/information/events/{id}/actions/reclassify` | POL-RWE-RECLASSIFY |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **إعادة تصنيف الحدث الواقعي**، لكي يتحقق غرض الحدث الواقعي: حدث وقع في العالم (ليس Domain Event)

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, RETIRED؛ authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-RWE-RECLASSIFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RWE-RECLASSIFY` · `AGG-REALWORLD-EVENT` · متطلبات: REQ-INF-020 · حالات استخدام: UC-001, UC-002, UC-003
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RWE-RECLASSIFY succeeds
  Given AGG-REALWORLD-EVENT in state ACTIVE or RETIRED and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-RWE-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-RWE-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RWE-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RWE-RECLASSIFY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per tenant policy (REQ-GOV-004) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REALWORLD_EVENT_INVALID_STATE_TRANSITION | 409 | لا حالة في المصفوفة يُرفض منها هذا الأمر؛ الرمز لا يُتوقع حدوثه |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-RWE-REGISTER — تسجيل الحدث الواقعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst · adapter service account | `POST /api/v1/information/events` | POL-RWE-REGISTER |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **تسجيل الحدث الواقعي**، لكي يتحقق غرض الحدث الواقعي: حدث وقع في العالم (ليس Domain Event)

- **الشروط المسبقة:** الحالة الحالية: ∅؛ type in RD-EVENT-TYPES; initial claims include event_time (fuzzy) and location
- **المدخلات:** `event_type`!: string, `label`!: Label, `initial_claims`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-RWE-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RWE-REGISTER` · `AGG-REALWORLD-EVENT` · متطلبات: REQ-INF-020 · حالات استخدام: UC-001, UC-002, UC-003
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RWE-REGISTER succeeds
  Given AGG-REALWORLD-EVENT does not exist yet and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-RWE-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-RWE-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RWE-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RWE-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVENT_INVALID | 422 | لم يتحقق الشرط: type in RD-EVENT-TYPES; initial claims include event_time (fuzzy) and location |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: event_type, label, initial_claims |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-RWE-REINSTATE — إعادة الحدث الواقعي إلى السريان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst · adapter service account | `POST /api/v1/information/events/{id}/actions/reinstate` | POL-RWE-REINSTATE |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **إعادة الحدث الواقعي إلى السريان**، لكي يتحقق غرض الحدث الواقعي: حدث وقع في العالم (ليس Domain Event)

- **الشروط المسبقة:** الحالة الحالية: RETIRED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-RWE-REINSTATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RWE-REINSTATE` · `AGG-REALWORLD-EVENT` · متطلبات: REQ-INF-020 · حالات استخدام: UC-001, UC-002, UC-003
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RWE-REINSTATE succeeds
  Given AGG-REALWORLD-EVENT in state RETIRED and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-RWE-REINSTATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-RWE-REINSTATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RWE-REINSTATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RWE-REINSTATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REALWORLD_EVENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-RWE-RETIRE — إحالة الحدث الواقعي إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst · adapter service account | `POST /api/v1/information/events/{id}/actions/retire` | POL-RWE-RETIRE |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **إحالة الحدث الواقعي إلى التقاعد**، لكي يتحقق غرض الحدث الواقعي: حدث وقع في العالم (ليس Domain Event)

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-RWE-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RWE-RETIRE` · `AGG-REALWORLD-EVENT` · متطلبات: REQ-INF-020 · حالات استخدام: UC-001, UC-002, UC-003
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RWE-RETIRE succeeds
  Given AGG-REALWORLD-EVENT in state ACTIVE and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-RWE-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-RWE-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RWE-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RWE-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REALWORLD_EVENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-Q-RWE-GET — جلب: Resolved real-world event

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user; label-filtered | `GET /api/v1/information/events/{event_id}` | POL-RWE-GET |

**القصة:** بصفتي **any user; label-filtered**، أريد **جلب Resolved real-world event**، لكي يتحقق المتطلب: The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct object types

- **المدخلات:** `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Resolved real-world event
- **الصلاحية:** any user; label-filtered؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-RWE-GET` · `AGG-REALWORLD-EVENT` · متطلبات: REQ-INF-020
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-RWE-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-RWE-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-RWE-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-RWE-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-RELATIONSHIP — العلاقة (Relationship (identity))

`03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md` · SLC-02 · الحالات: ACTIVE, RETIRED → —

#### US-BC02-REL-RECLASSIFY — إعادة تصنيف العلاقة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst · adapter service account | `POST /api/v1/information/relationships/{id}/actions/reclassify` | POL-REL-RECLASSIFY |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **إعادة تصنيف العلاقة**، لكي يتحقق غرض العلاقة: رابط موجّه بين كائنين؛ وجوده ادعاء

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, RETIRED؛ authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-REL-RECLASSIFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-REL-RECLASSIFY` · `AGG-RELATIONSHIP` · متطلبات: REQ-INF-027 · حالات استخدام: UC-003
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-REL-RECLASSIFY succeeds
  Given AGG-RELATIONSHIP in state ACTIVE or RETIRED and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-REL-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-REL-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-REL-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-REL-RECLASSIFY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per tenant policy (REQ-GOV-004) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RELATIONSHIP_INVALID_STATE_TRANSITION | 409 | لا حالة في المصفوفة يُرفض منها هذا الأمر؛ الرمز لا يُتوقع حدوثه |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-REL-REGISTER — تسجيل العلاقة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst · adapter service account | `POST /api/v1/information/relationships` | POL-REL-REGISTER |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **تسجيل العلاقة**، لكي يتحقق غرض العلاقة: رابط موجّه بين كائنين؛ وجوده ادعاء

- **الشروط المسبقة:** الحالة الحالية: ∅؛ type in RD-RELATIONSHIP-TYPES; endpoint types allowed; creates identity + existence claim (valid interval, sources ≥ 1)
- **المدخلات:** `relationship_type`!: string, `source_ref`!: urn, `target_ref`!: urn, `valid`!: Interval, `source_refs`!: array, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-REL-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-REL-REGISTER` · `AGG-RELATIONSHIP` · متطلبات: REQ-INF-027 · حالات استخدام: UC-003
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-REL-REGISTER succeeds
  Given AGG-RELATIONSHIP does not exist yet and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-REL-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-REL-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-REL-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-REL-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RELATIONSHIP_INVALID | 422 | لم يتحقق الشرط: type in RD-RELATIONSHIP-TYPES |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: relationship_type, source_ref, target_ref, valid, source_refs, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-REL-REINSTATE — إعادة العلاقة إلى السريان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst · adapter service account | `POST /api/v1/information/relationships/{id}/actions/reinstate` | POL-REL-REINSTATE |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **إعادة العلاقة إلى السريان**، لكي يتحقق غرض العلاقة: رابط موجّه بين كائنين؛ وجوده ادعاء

- **الشروط المسبقة:** الحالة الحالية: RETIRED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-REL-REINSTATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-REL-REINSTATE` · `AGG-RELATIONSHIP` · متطلبات: REQ-INF-027 · حالات استخدام: UC-003
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-REL-REINSTATE succeeds
  Given AGG-RELATIONSHIP in state RETIRED and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-REL-REINSTATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-REL-REINSTATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-REL-REINSTATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-REL-REINSTATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | RELATIONSHIP_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-REL-RETIRE — إحالة العلاقة إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst · adapter service account | `POST /api/v1/information/relationships/{id}/actions/retire` | POL-REL-RETIRE |

**القصة:** بصفتي **Analyst · adapter service account**، أريد **إحالة العلاقة إلى التقاعد**، لكي يتحقق غرض العلاقة: رابط موجّه بين كائنين؛ وجوده ادعاء

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ created in error only; ending in reality = CMD-CLM-RECORD-CHANGE on the existence claim
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-REL-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst · adapter service account؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-REL-RETIRE` · `AGG-RELATIONSHIP` · متطلبات: REQ-INF-027 · حالات استخدام: UC-003
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-REL-RETIRE succeeds
  Given AGG-RELATIONSHIP in state ACTIVE and every guard holds
  When an authorized actor (Analyst or adapter service account) sends CMD-REL-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-REL-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-REL-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-REL-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | RELATIONSHIP_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

### AGG-SOURCE — المصدر (Source)

`03-domain/contexts/BC02/aggregates/AGG-SOURCE.md` · SLC-02 · الحالات: ACTIVE, SUSPENDED → RETIRED

#### US-BC02-SRC-RATE-RELIABILITY — تقدير موثوقية المصدر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst | `POST /api/v1/information/sources/{id}/actions/rate-reliability` | POL-SRC-RATE-RELIABILITY |

**القصة:** بصفتي **Analyst**، أريد **تقدير موثوقية المصدر**، لكي يتحقق غرض المصدر: جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, SUSPENDED؛ rating ∈ A–F; valid_from given; creates bitemporal reliability claim
- **المدخلات:** `reliability`!: enum(A,B,C,D,E,F), `valid_from`!: date-time, `rationale`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SRC-RELIABILITY-RATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SRC-RATE-RELIABILITY` · `AGG-SOURCE` · متطلبات: REQ-INF-001 · حالات استخدام: UC-004, UC-095
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SRC-RATE-RELIABILITY succeeds
  Given AGG-SOURCE in state ACTIVE or SUSPENDED and every guard holds
  When Analyst sends CMD-SRC-RATE-RELIABILITY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SRC-RELIABILITY-RATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SRC-RATE-RELIABILITY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SRC-RATE-RELIABILITY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RATING_INVALID | 422 | لم يتحقق الشرط: rating ∈ A–F |
    | SOURCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reliability, valid_from, rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-SRC-RECLASSIFY — إعادة تصنيف المصدر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Security Officer | `POST /api/v1/information/sources/{id}/actions/reclassify` | POL-SRC-RECLASSIFY |

**القصة:** بصفتي **Security Officer**، أريد **إعادة تصنيف المصدر**، لكي يتحقق غرض المصدر: جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, SUSPENDED؛ authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SRC-RECLASSIFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SRC-RECLASSIFY` · `AGG-SOURCE` · متطلبات: REQ-INF-001 · حالات استخدام: UC-004, UC-095
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SRC-RECLASSIFY succeeds
  Given AGG-SOURCE in state ACTIVE or SUSPENDED and every guard holds
  When Security Officer sends CMD-SRC-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SRC-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SRC-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SRC-RECLASSIFY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per tenant policy (REQ-GOV-004) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SOURCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-SRC-REGISTER — تسجيل المصدر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst | `POST /api/v1/information/sources` | POL-SRC-REGISTER |

**القصة:** بصفتي **Analyst**، أريد **تسجيل المصدر**، لكي يتحقق غرض المصدر: جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية

- **الشروط المسبقة:** الحالة الحالية: ∅؛ type in RD-SOURCE-TYPES; initial reliability A–F; person-type sources get protection_level ≥ 1 and label ≥ tenant default + 1 rank
- **المدخلات:** `type`!: string, `name`!: LocalizedName, `owner_org`!: urn, `reliability`!: enum(A,B,C,D,E,F), `valid_from`!: date-time, `protection_level`: integer, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-SRC-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SRC-REGISTER` · `AGG-SOURCE` · متطلبات: REQ-INF-001 · حالات استخدام: UC-004, UC-095
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SRC-REGISTER succeeds
  Given AGG-SOURCE does not exist yet and every guard holds
  When Analyst sends CMD-SRC-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-SRC-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SRC-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SRC-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SOURCE_INVALID | 422 | لم يتحقق الشرط: type in RD-SOURCE-TYPES; person-type sources get protection_level ≥ 1 and label ≥ tenant default + 1 rank |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: type, name, owner_org, reliability, valid_from, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-SRC-REINSTATE — إعادة المصدر إلى السريان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst (محسوم: `17-security-design.md` §5) | `POST /api/v1/information/sources/{id}/actions/reinstate` | POL-SRC-REINSTATE |

**القصة:** بصفتي **Analyst**، أريد **إعادة المصدر إلى السريان**، لكي يتحقق غرض المصدر: جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية

- **الشروط المسبقة:** الحالة الحالية: SUSPENDED؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-SRC-REINSTATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (reinstate)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SRC-REINSTATE` · `AGG-SOURCE` · متطلبات: REQ-INF-001 · حالات استخدام: UC-004, UC-095
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SRC-REINSTATE succeeds
  Given AGG-SOURCE in state SUSPENDED and every guard holds
  When Analyst sends CMD-SRC-REINSTATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-SRC-REINSTATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SRC-REINSTATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SRC-REINSTATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SOURCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-SRC-RETIRE — إحالة المصدر إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst (محسوم: `17-security-design.md` §5) | `POST /api/v1/information/sources/{id}/actions/retire` | POL-SRC-RETIRE |

**القصة:** بصفتي **Analyst**، أريد **إحالة المصدر إلى التقاعد**، لكي يتحقق غرض المصدر: جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, SUSPENDED؛ reason; history retained
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-SRC-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (retire)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SRC-RETIRE` · `AGG-SOURCE` · متطلبات: REQ-INF-001 · حالات استخدام: UC-004, UC-095
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SRC-RETIRE succeeds
  Given AGG-SOURCE in state ACTIVE or SUSPENDED and every guard holds
  When Analyst sends CMD-SRC-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-SRC-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SRC-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SRC-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SOURCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-SRC-SET-PROTECTION — تحديد مستوى حماية المصدر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Security Officer | `POST /api/v1/information/sources/{id}/actions/set-protection` | POL-SRC-SET-PROTECTION |

**القصة:** بصفتي **Security Officer**، أريد **تحديد مستوى حماية المصدر**، لكي يتحقق غرض المصدر: جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, SUSPENDED؛ Security Officer; decreasing protection requires a second Security Officer
- **المدخلات:** `protection_level`!: integer, `second_approver`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SRC-PROTECTION-CHANGED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: decrease needs second Security Officer؛ الالتزامات: audit; mfa
- **الربط:** `CMD-SRC-SET-PROTECTION` · `AGG-SOURCE` · متطلبات: REQ-INF-001 · حالات استخدام: UC-004, UC-095
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SRC-SET-PROTECTION succeeds
  Given AGG-SOURCE in state ACTIVE or SUSPENDED and every guard holds
  When Security Officer sends CMD-SRC-SET-PROTECTION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SRC-PROTECTION-CHANGED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SRC-SET-PROTECTION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SRC-SET-PROTECTION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: decrease needs second Security Officer |
    | SOURCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: protection_level |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
    | MFA_STEP_UP_REQUIRED | 401 | التزام mfa في POL-SRC-SET-PROTECTION وقوة مصادقة الجلسة أقل من المطلوب؛ يُعاد الطلب بعد المصادقة المعززة بنفس Idempotency-Key (ADR-P19، الخطوة 6) |
```

#### US-BC02-SRC-SUSPEND — تعليق المصدر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst (محسوم: `17-security-design.md` §5) | `POST /api/v1/information/sources/{id}/actions/suspend` | POL-SRC-SUSPEND |

**القصة:** بصفتي **Analyst**، أريد **تعليق المصدر**، لكي يتحقق غرض المصدر: جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SUSPENDED؛ الحدث EVT-SRC-SUSPENDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (suspend)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SRC-SUSPEND` · `AGG-SOURCE` · متطلبات: REQ-INF-001 · حالات استخدام: UC-004, UC-095
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SRC-SUSPEND succeeds
  Given AGG-SOURCE in state ACTIVE and every guard holds
  When Analyst sends CMD-SRC-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUSPENDED
  And EVT-SRC-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SRC-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SRC-SUSPEND ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SOURCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-SRC-UPDATE-PROFILE — تحديث ملف المصدر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst | `POST /api/v1/information/sources/{id}/actions/update-profile` | POL-SRC-UPDATE-PROFILE |

**القصة:** بصفتي **Analyst**، أريد **تحديث ملف المصدر**، لكي يتحقق غرض المصدر: جهة أو نظام أو مستشعر ينتج معلومات، مع موثوقية مؤرخة وحماية هوية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, SUSPENDED؛ لا شروط إضافية
- **المدخلات:** `name`: LocalizedName, `contact`: object — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SRC-PROFILE-UPDATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SRC-UPDATE-PROFILE` · `AGG-SOURCE` · متطلبات: REQ-INF-001 · حالات استخدام: UC-004, UC-095
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SRC-UPDATE-PROFILE succeeds
  Given AGG-SOURCE in state ACTIVE or SUSPENDED and every guard holds
  When Analyst sends CMD-SRC-UPDATE-PROFILE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SRC-PROFILE-UPDATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SRC-UPDATE-PROFILE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SRC-UPDATE-PROFILE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SOURCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC02-Q-SRC-GET — جلب: Source; identity only with source-protection permission

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | Analyst and above; protection policy | `GET /api/v1/information/sources/{source_id}` | POL-SRC-GET |

**القصة:** بصفتي **Analyst and above; protection policy**، أريد **جلب Source; identity only with source-protection permission**، لكي يتحقق المتطلب: The system shall register each source with type, owner, classification and a reliability rating, and keep the history of reliability changes

- **المدخلات:** `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Source; identity only with source-protection permission
- **الصلاحية:** Analyst and above; protection policy؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-SRC-GET` · `AGG-SOURCE` · متطلبات: REQ-INF-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SRC-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-SRC-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-SRC-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-SRC-GET
  Then the response is 404 with the same shape as for a missing item
```

### استعلامات عابرة للـAggregates

#### US-BC02-Q-LIN-TRACE — جلب: Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/information/lineage/{object_urn}` | POL-LIN-TRACE |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy**، لكي يتحقق المتطلب: The system shall record lineage for every derived object: inputs and their versions, the transformation and its version, the actor and the execution time

- **المدخلات:** `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy
- **الصلاحية:** any user; per-node authorization؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-LIN-TRACE` · عابر للـAggregates · متطلبات: REQ-INF-035
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-LIN-TRACE returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-LIN-TRACE
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-LIN-TRACE hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-LIN-TRACE
  Then the response is 404 with the same shape as for a missing item
```

<!-- END GENERATED: build_analysis_design.py -->
