---
id: AD-05-US-BC06
type: user-stories
title: "قصص المستخدم — BC06"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
generator: 17-system-study/_build/build_analysis_design.py
---

# قصص المستخدم — BC06 Knowledge — المعرفة والمنتجات

مولَّد بالكامل من المصادر بواسطة `17-system-study/_build/build_analysis_design.py`؛ لا يُحرَّر يدويًا. القالب والتصنيف وتعريف ضوابط النوع والفئة في [00-guide.md](00-guide.md).

<!-- BEGIN GENERATED: build_analysis_design.py -->

## ملخص BC06

| نوع العملية | عدد القصص |
|---|---|
| إنشاء | 5 |
| تعديل | 5 |
| جلب | 8 |
| حذف / إنهاء | 9 |
| سير عمل | 10 |
| نظام (SYS) | 14 |
| **المجموع** | **51** |

### AGG-ARCHIVE-PACKAGE — الحزمة الأرشيفية (Archive Package (AIP))

`03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md` · SLC-12 · الحالات: INGESTING, INGEST_FAILED, ARCHIVED, INTEGRITY_FAILED → TRANSFERRED, DISPOSED

#### US-BC06-ARC-MIGRATE-FORMAT — ترحيل صيغة الحزمة الأرشيفية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تقارير ومنتجات | Archivist | `POST /api/v1/knowledge/archive-packages/{id}/actions/migrate-format` | POL-ARC-MIGRATE-FORMAT |

**القصة:** بصفتي **Archivist**، أريد **ترحيل صيغة الحزمة الأرشيفية**، لكي يتحقق غرض الحزمة الأرشيفية: حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول

- **الشروط المسبقة:** الحالة الحالية: ARCHIVED؛ new preservation representation added; originals kept; preservation event recorded
- **المدخلات:** `target_format`!: string, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ARC-FORMAT-MIGRATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Archivist (retry, repair, migrate) · transfer authority (transfer)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ARC-MIGRATE-FORMAT` · `AGG-ARCHIVE-PACKAGE` · متطلبات: REQ-ARC-001, REQ-ARC-002, REQ-ARC-003 · حالات استخدام: UC-063, UC-064
- **ضوابط النوع والفئة:** C-UPD، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ARC-MIGRATE-FORMAT succeeds
  Given AGG-ARCHIVE-PACKAGE in state ARCHIVED and every guard holds
  When Archivist sends CMD-ARC-MIGRATE-FORMAT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ARC-FORMAT-MIGRATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ARC-MIGRATE-FORMAT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, INGESTING, INGEST_FAILED, INTEGRITY_FAILED, TRANSFERRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ARC-MIGRATE-FORMAT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | FORMAT_INVALID | 422 | لم يتحقق الشرط: new preservation representation added; originals kept; preservation event recorded |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: target_format, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-ARC-REPAIR — إصلاح الحزمة الأرشيفية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تقارير ومنتجات | Archivist | `POST /api/v1/knowledge/archive-packages/{id}/actions/repair` | POL-ARC-REPAIR |

**القصة:** بصفتي **Archivist**، أريد **إصلاح الحزمة الأرشيفية**، لكي يتحقق غرض الحزمة الأرشيفية: حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول

- **الشروط المسبقة:** الحالة الحالية: INTEGRITY_FAILED؛ restored from replica; fixity re-verified
- **المدخلات:** `replica_ref`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ARCHIVED؛ الحدث EVT-ARC-REPAIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Archivist (retry, repair, migrate) · transfer authority (transfer)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ARC-REPAIR` · `AGG-ARCHIVE-PACKAGE` · متطلبات: REQ-ARC-001, REQ-ARC-002, REQ-ARC-003 · حالات استخدام: UC-063, UC-064
- **ضوابط النوع والفئة:** C-WF، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ARC-REPAIR succeeds
  Given AGG-ARCHIVE-PACKAGE in state INTEGRITY_FAILED and every guard holds
  When Archivist sends CMD-ARC-REPAIR with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ARCHIVED
  And EVT-ARC-REPAIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ARC-REPAIR is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ARCHIVED, DISPOSED, INGESTING, INGEST_FAILED, TRANSFERRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ARC-REPAIR ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | FIXITY_MISMATCH | 422 | لم يتحقق الشرط: fixity re-verified |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: replica_ref |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-ARC-RETRY-INGEST — إعادة محاولة استيعاب الحزمة الأرشيفية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تقارير ومنتجات | Archivist | `POST /api/v1/knowledge/archive-packages/{id}/actions/retry-ingest` | POL-ARC-RETRY-INGEST |

**القصة:** بصفتي **Archivist**، أريد **إعادة محاولة استيعاب الحزمة الأرشيفية**، لكي يتحقق غرض الحزمة الأرشيفية: حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول

- **الشروط المسبقة:** الحالة الحالية: INGEST_FAILED؛ archivist; corrective note
- **المدخلات:** `note`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← INGESTING؛ الحدث EVT-ARC-INGEST-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Archivist (retry, repair, migrate) · transfer authority (transfer)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ARC-RETRY-INGEST` · `AGG-ARCHIVE-PACKAGE` · متطلبات: REQ-ARC-001, REQ-ARC-002, REQ-ARC-003 · حالات استخدام: UC-063, UC-064
- **ضوابط النوع والفئة:** C-WF، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ARC-RETRY-INGEST succeeds
  Given AGG-ARCHIVE-PACKAGE in state INGEST_FAILED and every guard holds
  When Archivist sends CMD-ARC-RETRY-INGEST with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes INGESTING
  And EVT-ARC-INGEST-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ARC-RETRY-INGEST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ARCHIVED, DISPOSED, INGESTING, INTEGRITY_FAILED, TRANSFERRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ARC-RETRY-INGEST ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: note |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-ARC-TRANSFER — نقل الحزمة الأرشيفية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تقارير ومنتجات | transfer authority | `POST /api/v1/knowledge/archive-packages/{id}/actions/transfer` | POL-ARC-TRANSFER |

**القصة:** بصفتي **transfer authority**، أريد **نقل الحزمة الأرشيفية**، لكي يتحقق غرض الحزمة الأرشيفية: حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول

- **الشروط المسبقة:** الحالة الحالية: ARCHIVED؛ transfer authority decision; receipt from the receiving archive
- **المدخلات:** `decision`!: urn, `receiving_archive`!: string, `receipt`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← TRANSFERRED؛ الحدث EVT-ARC-TRANSFERRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Archivist (retry, repair, migrate) · transfer authority (transfer)؛ الشروط: tenant match; object visible؛ فصل المهام: transfer authority decision؛ الالتزامات: audit
- **الربط:** `CMD-ARC-TRANSFER` · `AGG-ARCHIVE-PACKAGE` · متطلبات: REQ-ARC-001, REQ-ARC-002, REQ-ARC-003 · حالات استخدام: UC-063, UC-064
- **ضوابط النوع والفئة:** C-DEL، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ARC-TRANSFER succeeds
  Given AGG-ARCHIVE-PACKAGE in state ARCHIVED and every guard holds
  When transfer authority sends CMD-ARC-TRANSFER with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes TRANSFERRED
  And EVT-ARC-TRANSFERRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ARC-TRANSFER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, INGESTING, INGEST_FAILED, INTEGRITY_FAILED, TRANSFERRED |
    | AUTHORITY_REQUIRED | 422 | لم يتحقق الشرط: transfer authority decision |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ARC-TRANSFER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: decision, receiving_archive, receipt |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-S-ARCHIVE-PACKAGE-01 — تلقائي: disposition action ARCHIVE for a bucket or record set (الحزمة الأرشيفية)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | ∅ | INGESTING |

**القصة:** بصفتي **النظام**، عند «disposition action ARCHIVE for a bucket or record set»، أريد نقل **الحزمة الأرشيفية** إلى INGESTING، لكي يتحقق غرض الحزمة الأرشيفية: حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول

- **الشرط:** SIP assembled from owner exports: content, metadata, provenance, access history
- **المخرجات:** الحدث EVT-ARC-INGEST-STARTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ARCHIVE-PACKAGE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-S-ARCHIVE-PACKAGE-02 — تلقائي: package validated (الحزمة الأرشيفية)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | INGESTING | ARCHIVED |

**القصة:** بصفتي **النظام**، عند «package validated»، أريد نقل **الحزمة الأرشيفية** إلى ARCHIVED، لكي يتحقق غرض الحزمة الأرشيفية: حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول

- **الشرط:** BagIt structure valid; every file fixity (SHA-256) recorded; preservation formats (R2-Q6) produced alongside originals
- **المخرجات:** الحدث EVT-ARC-ARCHIVED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ARCHIVE-PACKAGE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-S-ARCHIVE-PACKAGE-03 — تلقائي: validation failed (الحزمة الأرشيفية)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | INGESTING | INGEST_FAILED |

**القصة:** بصفتي **النظام**، عند «validation failed»، أريد نقل **الحزمة الأرشيفية** إلى INGEST_FAILED، لكي يتحقق غرض الحزمة الأرشيفية: حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول

- **الشرط:** errors recorded
- **المخرجات:** الحدث EVT-ARC-INGEST-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ARCHIVE-PACKAGE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-S-ARCHIVE-PACKAGE-04 — تلقائي: integrity check failed (الحزمة الأرشيفية)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | ARCHIVED | INTEGRITY_FAILED |

**القصة:** بصفتي **النظام**، عند «integrity check failed»، أريد نقل **الحزمة الأرشيفية** إلى INTEGRITY_FAILED، لكي يتحقق غرض الحزمة الأرشيفية: حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول

- **الشرط:** fixity mismatch on any file
- **المخرجات:** الحدث EVT-ARC-INTEGRITY-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ARCHIVE-PACKAGE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-S-ARCHIVE-PACKAGE-05 — تلقائي: disposition DESTROY executed for the package bucket (الحزمة الأرشيفية)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ARCHIVED, INTEGRITY_FAILED | DISPOSED |

**القصة:** بصفتي **النظام**، عند «disposition DESTROY executed for the package bucket»، أريد نقل **الحزمة الأرشيفية** إلى DISPOSED، لكي يتحقق غرض الحزمة الأرشيفية: حزمة أرشيفية بمعيار OAIS: محتوى، بيانات وصفية، منشأ، بصمات، سجل وصول

- **الشرط:** SLC-12a key destruction; no active hold
- **المخرجات:** الحدث EVT-ARC-DISPOSED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ARCHIVE-PACKAGE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-Q-ARC-RETRIEVE — جلب: Retrieve package content (warm: signed grant; cold: staged job) — access logged

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تقارير ومنتجات | authorized by package label and purpose | `POST /api/v1/knowledge/archive-packages/{package_id}/retrievals` | POL-ARC-RETRIEVE |

**القصة:** بصفتي **authorized by package label and purpose**، أريد **جلب Retrieve package content (warm: signed grant; cold: staged job) — access logged**، لكي يتحقق المتطلب: When an authorized user requests a historical record, the system shall retrieve it within the archive retrieval target and audit the access

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Retrieve package content (warm: signed grant; cold: staged job) — access logged
- **الصلاحية:** authorized by package label and purpose؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ARC-RETRIEVE` · `AGG-ARCHIVE-PACKAGE` · متطلبات: REQ-ARC-003
- **ضوابط النوع والفئة:** C-READ، K-RPT

```gherkin
Scenario: QRY-ARC-RETRIEVE computes its result only over what the caller may see
  Given data inside and outside the caller's allowed_scope
  When the caller sends QRY-ARC-RETRIEVE
  Then the result neither includes nor reveals data outside allowed_scope

Scenario: QRY-ARC-RETRIEVE is denied
  Given the policy denies the caller
  When the caller sends QRY-ARC-RETRIEVE
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC06-Q-ARC-SEARCH — جلب: Archive catalogue (metadata only) by class, period, org

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تقارير ومنتجات | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/knowledge/archive-packages` | POL-ARC-SEARCH |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Archive catalogue (metadata only) by class, period, org**، لكي يتحقق المتطلب: When an authorized user requests a historical record, the system shall retrieve it within the archive retrieval target and audit the access

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Archive catalogue (metadata only) by class, period, org؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Archivist; label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ARC-SEARCH` · `AGG-ARCHIVE-PACKAGE` · متطلبات: REQ-ARC-003
- **ضوابط النوع والفئة:** C-READ، K-RPT

```gherkin
Scenario: QRY-ARC-SEARCH returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ARC-SEARCH with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ARC-SEARCH is denied
  Given the policy denies the caller
  When the caller sends QRY-ARC-SEARCH
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-DISTRIBUTION — التوزيع (Distribution)

`03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md` · SLC-12 · الحالات: PREPARING → COMPLETED, COMPLETED_WITH_EXCLUSIONS, CANCELLED

#### US-BC06-DST-CANCEL — إلغاء التوزيع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تقارير ومنتجات | Manager / product owner | `POST /api/v1/knowledge/distributions/{id}/actions/cancel` | POL-DST-CANCEL |

**القصة:** بصفتي **Manager / product owner**، أريد **إلغاء التوزيع**، لكي يتحقق غرض التوزيع: توزيع نسخة معتمدة لمستلمين بعلامة مائية لكل مستلم

- **الشروط المسبقة:** الحالة الحالية: PREPARING؛ distributor; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-DST-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Manager / product owner؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DST-CANCEL` · `AGG-DISTRIBUTION` · متطلبات: REQ-PRD-004, REQ-PRD-005 · حالات استخدام: UC-112
- **ضوابط النوع والفئة:** C-DEL، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DST-CANCEL succeeds
  Given AGG-DISTRIBUTION in state PREPARING and every guard holds
  When Manager / product owner sends CMD-DST-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-DST-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DST-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DST-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | DISTRIBUTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, COMPLETED_WITH_EXCLUSIONS |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-DST-DISTRIBUTE — تنفيذ التوزيع

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تقارير ومنتجات | Manager / product owner | `POST /api/v1/knowledge/distributions` | POL-DST-DISTRIBUTE |

**القصة:** بصفتي **Manager / product owner**، أريد **تنفيذ التوزيع**، لكي يتحقق غرض التوزيع: توزيع نسخة معتمدة لمستلمين بعلامة مائية لكل مستلم

- **الشروط المسبقة:** الحالة الحالية: ∅؛ product APPROVED; recipients (users, org units); formats ⊆ {pdf, docx, in_app}; distributor authorized
- **المدخلات:** `product`!: urn, `recipients`!: array, `formats`!: array, `message`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← PREPARING؛ الحدث EVT-DST-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Manager / product owner؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit; watermark
- **الربط:** `CMD-DST-DISTRIBUTE` · `AGG-DISTRIBUTION` · متطلبات: REQ-PRD-004, REQ-PRD-005 · حالات استخدام: UC-112
- **ضوابط النوع والفئة:** C-CRE، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DST-DISTRIBUTE succeeds
  Given AGG-DISTRIBUTION does not exist yet and every guard holds
  When Manager / product owner sends CMD-DST-DISTRIBUTE with a valid payload, a new Idempotency-Key
  Then the state becomes PREPARING
  And EVT-DST-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DST-DISTRIBUTE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DST-DISTRIBUTE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_NOT_APPROVED | 422 | لم يتحقق الشرط: product APPROVED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: product, recipients, formats |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-S-DISTRIBUTION-01 — تلقائي: all recipients authorized and delivered (التوزيع)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | PREPARING | COMPLETED |

**القصة:** بصفتي **النظام**، عند «all recipients authorized and delivered»، أريد نقل **التوزيع** إلى COMPLETED، لكي يتحقق غرض التوزيع: توزيع نسخة معتمدة لمستلمين بعلامة مائية لكل مستلم

- **الشرط:** per-recipient watermark (recipient id, product version, time) embedded; delivery logged
- **المخرجات:** الحدث EVT-DST-COMPLETED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-DISTRIBUTION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-S-DISTRIBUTION-02 — تلقائي: some recipients not authorized (التوزيع)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | PREPARING | COMPLETED_WITH_EXCLUSIONS |

**القصة:** بصفتي **النظام**، عند «some recipients not authorized»، أريد نقل **التوزيع** إلى COMPLETED_WITH_EXCLUSIONS، لكي يتحقق غرض التوزيع: توزيع نسخة معتمدة لمستلمين بعلامة مائية لكل مستلم

- **الشرط:** unauthorized recipients excluded and listed to the distributor; others delivered
- **المخرجات:** الحدث EVT-DST-COMPLETED-WITH-EXCLUSIONS؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-DISTRIBUTION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

### AGG-KNOWLEDGE-OBJECT — كائن المعرفة (Knowledge Object Version)

`03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md` · SLC-12 · الحالات: DRAFT, IN_REVIEW, PUBLISHED → REJECTED, SUPERSEDED, RETIRED, DISCARDED

#### US-BC06-KNO-DISCARD — تجاهل مسودة كائن المعرفة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تقارير ومنتجات | any user | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/discard` | POL-KNO-DISCARD |

**القصة:** بصفتي **any user**، أريد **تجاهل مسودة كائن المعرفة**، لكي يتحقق غرض كائن المعرفة: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ author; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DISCARDED؛ الحدث EVT-KNO-DISCARDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-KNO-DISCARD` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-001, REQ-KNW-002, REQ-KNW-003 · حالات استخدام: UC-060, UC-061, UC-062
- **ضوابط النوع والفئة:** C-DEL، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-KNO-DISCARD succeeds
  Given AGG-KNOWLEDGE-OBJECT in state DRAFT and every guard holds
  When any user sends CMD-KNO-DISCARD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISCARDED
  And EVT-KNO-DISCARDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-KNO-DISCARD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-KNO-DISCARD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, IN_REVIEW, PUBLISHED, REJECTED, RETIRED, SUPERSEDED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-KNO-DRAFT — إعداد مسودة كائن المعرفة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تقارير ومنتجات | any user | `POST /api/v1/knowledge/knowledge-objects` | POL-KNO-DRAFT |

**القصة:** بصفتي **any user**، أريد **إعداد مسودة كائن المعرفة**، لكي يتحقق غرض كائن المعرفة: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات

- **الشروط المسبقة:** الحالة الحالية: ∅؛ type ∈ {procedure, lesson, best_practice, policy_knowledge}; lessons reference a terminal source (task, plan, incident, or a completed exercise simulation — CR-63) and its evidence (REQ-KNW-002); label ≥ source label
- **المدخلات:** `knowledge_type`!: enum(procedure,lesson,best_practice,policy_knowledge), `title`!: LocalizedName, `source`: urn, `revises`: urn, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-KNO-DRAFTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-KNO-DRAFT` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-001, REQ-KNW-002, REQ-KNW-003 · حالات استخدام: UC-060, UC-061, UC-062
- **ضوابط النوع والفئة:** C-CRE، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-KNO-DRAFT succeeds
  Given AGG-KNOWLEDGE-OBJECT does not exist yet and every guard holds
  When any user sends CMD-KNO-DRAFT with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-KNO-DRAFTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-KNO-DRAFT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-KNO-DRAFT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | KNOWLEDGE_INVALID | 422 | لم يتحقق الشرط: type ∈ {procedure, lesson, best_practice, policy_knowledge} |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: knowledge_type, title, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-KNO-EDIT — تعديل كائن المعرفة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تقارير ومنتجات | any user | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/edit` | POL-KNO-EDIT |

**القصة:** بصفتي **any user**، أريد **تعديل كائن المعرفة**، لكي يتحقق غرض كائن المعرفة: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ statements with evidence links; relationships to task types, plan types, entity types, areas
- **المدخلات:** `statements`!: array, `relationships`: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-KNO-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-KNO-EDIT` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-001, REQ-KNW-002, REQ-KNW-003 · حالات استخدام: UC-060, UC-061, UC-062
- **ضوابط النوع والفئة:** C-UPD، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-KNO-EDIT succeeds
  Given AGG-KNOWLEDGE-OBJECT in state DRAFT and every guard holds
  When any user sends CMD-KNO-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-KNO-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-KNO-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-KNO-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | KNOWLEDGE_INVALID | 422 | لم يتحقق الشرط: statements with evidence links; relationships to task types, plan types, entity types, areas |
    | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, IN_REVIEW, PUBLISHED, REJECTED, RETIRED, SUPERSEDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: statements |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-KNO-PUBLISH — نشر كائن المعرفة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تقارير ومنتجات | Knowledge Manager | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/publish` | POL-KNO-PUBLISH |

**القصة:** بصفتي **Knowledge Manager**، أريد **نشر كائن المعرفة**، لكي يتحقق غرض كائن المعرفة: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات

- **الشروط المسبقة:** الحالة الحالية: IN_REVIEW؛ reviewer ≠ author; procedures and policy knowledge require the owning authority (Knowledge Manager + domain authority); previous PUBLISHED → SUPERSEDED
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PUBLISHED؛ الحدث EVT-KNO-PUBLISHED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ الشروط: tenant match; object visible؛ فصل المهام: reviewer ≠ author; domain authority for procedures/policy knowledge؛ الالتزامات: audit
- **الربط:** `CMD-KNO-PUBLISH` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-001, REQ-KNW-002, REQ-KNW-003 · حالات استخدام: UC-060, UC-061, UC-062
- **ضوابط النوع والفئة:** C-WF، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-KNO-PUBLISH succeeds
  Given AGG-KNOWLEDGE-OBJECT in state IN_REVIEW and every guard holds
  When Knowledge Manager sends CMD-KNO-PUBLISH with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PUBLISHED
  And EVT-KNO-PUBLISHED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-KNO-PUBLISH is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-KNO-PUBLISH ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, DRAFT, PUBLISHED, REJECTED, RETIRED, SUPERSEDED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: reviewer ≠ author; domain authority for procedures/policy knowledge |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-KNO-RECORD-REUSE — تسجيل إعادة استخدام كائن المعرفة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تقارير ومنتجات | planner | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/record-reuse` | POL-KNO-RECORD-REUSE |

**القصة:** بصفتي **planner**، أريد **تسجيل إعادة استخدام كائن المعرفة**، لكي يتحقق غرض كائن المعرفة: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات

- **الشروط المسبقة:** الحالة الحالية: PUBLISHED؛ target plan/task/product visible; reuse counted (OUT-06)
- **المدخلات:** `target`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-KNO-REUSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-KNO-RECORD-REUSE` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-001, REQ-KNW-002, REQ-KNW-003 · حالات استخدام: UC-060, UC-061, UC-062
- **ضوابط النوع والفئة:** C-UPD، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-KNO-RECORD-REUSE succeeds
  Given AGG-KNOWLEDGE-OBJECT in state PUBLISHED and every guard holds
  When planner sends CMD-KNO-RECORD-REUSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-KNO-REUSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-KNO-RECORD-REUSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-KNO-RECORD-REUSE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, DRAFT, IN_REVIEW, REJECTED, RETIRED, SUPERSEDED |
    | TARGET_INVALID | 422 | لم يتحقق الشرط: target plan/task/product visible |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: target |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-KNO-REJECT — رفض كائن المعرفة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تقارير ومنتجات | Knowledge Manager | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/reject` | POL-KNO-REJECT |

**القصة:** بصفتي **Knowledge Manager**، أريد **رفض كائن المعرفة**، لكي يتحقق غرض كائن المعرفة: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات

- **الشروط المسبقة:** الحالة الحالية: IN_REVIEW؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-KNO-REJECTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-KNO-REJECT` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-001, REQ-KNW-002, REQ-KNW-003 · حالات استخدام: UC-060, UC-061, UC-062
- **ضوابط النوع والفئة:** C-DEL، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-KNO-REJECT succeeds
  Given AGG-KNOWLEDGE-OBJECT in state IN_REVIEW and every guard holds
  When Knowledge Manager sends CMD-KNO-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-KNO-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-KNO-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-KNO-REJECT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, DRAFT, PUBLISHED, REJECTED, RETIRED, SUPERSEDED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-KNO-RETIRE — إحالة كائن المعرفة إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تقارير ومنتجات | Knowledge Manager | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/retire` | POL-KNO-RETIRE |

**القصة:** بصفتي **Knowledge Manager**، أريد **إحالة كائن المعرفة إلى التقاعد**، لكي يتحقق غرض كائن المعرفة: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات

- **الشروط المسبقة:** الحالة الحالية: PUBLISHED؛ reason (obsolete, wrong)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-KNO-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-KNO-RETIRE` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-001, REQ-KNW-002, REQ-KNW-003 · حالات استخدام: UC-060, UC-061, UC-062
- **ضوابط النوع والفئة:** C-DEL، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-KNO-RETIRE succeeds
  Given AGG-KNOWLEDGE-OBJECT in state PUBLISHED and every guard holds
  When Knowledge Manager sends CMD-KNO-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-KNO-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-KNO-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-KNO-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, DRAFT, IN_REVIEW, REJECTED, RETIRED, SUPERSEDED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-KNO-RETURN — إعادة كائن المعرفة للمراجعة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تقارير ومنتجات | Knowledge Manager | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/return` | POL-KNO-RETURN |

**القصة:** بصفتي **Knowledge Manager**، أريد **إعادة كائن المعرفة للمراجعة**، لكي يتحقق غرض كائن المعرفة: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات

- **الشروط المسبقة:** الحالة الحالية: IN_REVIEW؛ reviewer; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-KNO-RETURNED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-KNO-RETURN` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-001, REQ-KNW-002, REQ-KNW-003 · حالات استخدام: UC-060, UC-061, UC-062
- **ضوابط النوع والفئة:** C-WF، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-KNO-RETURN succeeds
  Given AGG-KNOWLEDGE-OBJECT in state IN_REVIEW and every guard holds
  When Knowledge Manager sends CMD-KNO-RETURN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DRAFT
  And EVT-KNO-RETURNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-KNO-RETURN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-KNO-RETURN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, DRAFT, PUBLISHED, REJECTED, RETIRED, SUPERSEDED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-KNO-SUBMIT — تقديم كائن المعرفة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تقارير ومنتجات | any user | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/submit` | POL-KNO-SUBMIT |

**القصة:** بصفتي **any user**، أريد **تقديم كائن المعرفة**، لكي يتحقق غرض كائن المعرفة: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ ≥ 1 statement; lessons: ≥ 1 evidence link
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← IN_REVIEW؛ الحدث EVT-KNO-SUBMITTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-KNO-SUBMIT` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-001, REQ-KNW-002, REQ-KNW-003 · حالات استخدام: UC-060, UC-061, UC-062
- **ضوابط النوع والفئة:** C-WF، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-KNO-SUBMIT succeeds
  Given AGG-KNOWLEDGE-OBJECT in state DRAFT and every guard holds
  When any user sends CMD-KNO-SUBMIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_REVIEW
  And EVT-KNO-SUBMITTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-KNO-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-KNO-SUBMIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | KNOWLEDGE_INCOMPLETE | 422 | لم يتحقق الشرط: ≥ 1 statement; lessons: ≥ 1 evidence link |
    | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, IN_REVIEW, PUBLISHED, REJECTED, RETIRED, SUPERSEDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-S-KNOWLEDGE-OBJECT-01 — تلقائي: newer version published (كائن المعرفة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | PUBLISHED | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «newer version published»، أريد نقل **كائن المعرفة** إلى SUPERSEDED، لكي يتحقق غرض كائن المعرفة: إجراء أو درس أو ممارسة فضلى أو معرفة سياساتية، كعبارات بأدلة وعلاقات

- **الشرط:** system
- **المخرجات:** الحدث EVT-KNO-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-KNOWLEDGE-OBJECT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-Q-KNO-SEARCH — جلب: Published knowledge by type, text, relationships

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تقارير ومنتجات | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/knowledge/knowledge-objects` | POL-KNO-SEARCH |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Published knowledge by type, text, relationships**، لكي يتحقق المتطلب: The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims with evidence, relationships, versions, review, approval and publication

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Published knowledge by type, text, relationships؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user; label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-KNO-SEARCH` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-001
- **ضوابط النوع والفئة:** C-READ، K-RPT

```gherkin
Scenario: QRY-KNO-SEARCH returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-KNO-SEARCH with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-KNO-SEARCH is denied
  Given the policy denies the caller
  When the caller sends QRY-KNO-SEARCH
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC06-Q-KNO-SUGGEST — جلب: Published knowledge relevant to a task type / plan / area (by relationships)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تقارير ومنتجات | مستخدم مخوَّل (ضمن allowed_scope) | `POST /api/v1/knowledge/knowledge-suggestions` | POL-KNO-SUGGEST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Published knowledge relevant to a task type / plan / area (by relationships)**، لكي يتحقق المتطلب: When a published knowledge object is relevant to a new plan or task type, the system shall suggest it to the planner

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Published knowledge relevant to a task type / plan / area (by relationships)
- **الصلاحية:** planner; label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-KNO-SUGGEST` · `AGG-KNOWLEDGE-OBJECT` · متطلبات: REQ-KNW-003
- **ضوابط النوع والفئة:** C-READ، K-RPT

```gherkin
Scenario: QRY-KNO-SUGGEST computes its result only over what the caller may see
  Given data inside and outside the caller's allowed_scope
  When the caller sends QRY-KNO-SUGGEST
  Then the result neither includes nor reveals data outside allowed_scope

Scenario: QRY-KNO-SUGGEST is denied
  Given the policy denies the caller
  When the caller sends QRY-KNO-SUGGEST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-PRODUCT — المنتج (Product Version)

`03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md` · SLC-12 · الحالات: DRAFT, GENERATING, GENERATED, GENERATION_FAILED, IN_REVIEW, APPROVED → SUPERSEDED, WITHDRAWN, DISCARDED

#### US-BC06-PRD-APPROVE — اعتماد المنتج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تقارير ومنتجات | reviewer | `POST /api/v1/knowledge/products/{id}/actions/approve` | POL-PRD-APPROVE |

**القصة:** بصفتي **reviewer**، أريد **اعتماد المنتج**، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشروط المسبقة:** الحالة الحالية: IN_REVIEW؛ reviewer ≠ author; content frozen with pinned citations; previous APPROVED version of the same product → SUPERSEDED
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← APPROVED؛ الحدث EVT-PRD-APPROVED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)؛ الشروط: tenant match; object visible؛ فصل المهام: reviewer ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-PRD-APPROVE` · `AGG-PRODUCT` · متطلبات: REQ-PRD-001, REQ-PRD-002, REQ-PRD-003 · حالات استخدام: UC-110, UC-111
- **ضوابط النوع والفئة:** C-WF، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRD-APPROVE succeeds
  Given AGG-PRODUCT in state IN_REVIEW and every guard holds
  When reviewer sends CMD-PRD-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes APPROVED
  And EVT-PRD-APPROVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRD-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRD-APPROVE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, DISCARDED, DRAFT, GENERATED, GENERATING, GENERATION_FAILED, SUPERSEDED, WITHDRAWN |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: reviewer ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-PRD-CREATE — إنشاء المنتج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تقارير ومنتجات | Analyst / Planner | `POST /api/v1/knowledge/products` | POL-PRD-CREATE |

**القصة:** بصفتي **Analyst / Planner**، أريد **إنشاء المنتج**، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشروط المسبقة:** الحالة الحالية: ∅؛ template ACTIVE (version pinned); parameters valid; audience (org units/roles); target label ≥ labels of scope objects referenced in parameters; optional revises = APPROVED version
- **المدخلات:** `template`!: urn, `parameters`!: object, `audience`!: array, `title`!: LocalizedName, `revises`: urn, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-PRD-CREATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PRD-CREATE` · `AGG-PRODUCT` · متطلبات: REQ-PRD-001, REQ-PRD-002, REQ-PRD-003 · حالات استخدام: UC-110, UC-111
- **ضوابط النوع والفئة:** C-CRE، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRD-CREATE succeeds
  Given AGG-PRODUCT does not exist yet and every guard holds
  When Analyst / Planner sends CMD-PRD-CREATE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-PRD-CREATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRD-CREATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRD-CREATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_INVALID | 422 | لم يتحقق الشرط: template ACTIVE (version pinned); parameters valid; audience (org units/roles); target label ≥ labels of scope objects referenced in parameters; optional revises = APPROVED version |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: template, parameters, audience, title, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-PRD-DISCARD — تجاهل مسودة المنتج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تقارير ومنتجات | Analyst / Planner | `POST /api/v1/knowledge/products/{id}/actions/discard` | POL-PRD-DISCARD |

**القصة:** بصفتي **Analyst / Planner**، أريد **تجاهل مسودة المنتج**، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشروط المسبقة:** الحالة الحالية: DRAFT, GENERATED, GENERATION_FAILED؛ author; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DISCARDED؛ الحدث EVT-PRD-DISCARDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PRD-DISCARD` · `AGG-PRODUCT` · متطلبات: REQ-PRD-001, REQ-PRD-002, REQ-PRD-003 · حالات استخدام: UC-110, UC-111
- **ضوابط النوع والفئة:** C-DEL، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRD-DISCARD succeeds
  Given AGG-PRODUCT in state DRAFT or GENERATED or GENERATION_FAILED and every guard holds
  When Analyst / Planner sends CMD-PRD-DISCARD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISCARDED
  And EVT-PRD-DISCARDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRD-DISCARD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRD-DISCARD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, DISCARDED, GENERATING, IN_REVIEW, SUPERSEDED, WITHDRAWN |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-PRD-EDIT-NARRATIVE — تعديل سرد المنتج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تقارير ومنتجات | Analyst / Planner | `POST /api/v1/knowledge/products/{id}/actions/edit-narrative` | POL-PRD-EDIT-NARRATIVE |

**القصة:** بصفتي **Analyst / Planner**، أريد **تعديل سرد المنتج**، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشروط المسبقة:** الحالة الحالية: GENERATED؛ only narrative sections; data sections change only by regeneration
- **المدخلات:** `section_id`!: string, `text`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-PRD-NARRATIVE-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PRD-EDIT-NARRATIVE` · `AGG-PRODUCT` · متطلبات: REQ-PRD-001, REQ-PRD-002, REQ-PRD-003 · حالات استخدام: UC-110, UC-111
- **ضوابط النوع والفئة:** C-UPD، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRD-EDIT-NARRATIVE succeeds
  Given AGG-PRODUCT in state GENERATED and every guard holds
  When Analyst / Planner sends CMD-PRD-EDIT-NARRATIVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-PRD-NARRATIVE-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRD-EDIT-NARRATIVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRD-EDIT-NARRATIVE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, DISCARDED, DRAFT, GENERATING, GENERATION_FAILED, IN_REVIEW, SUPERSEDED, WITHDRAWN |
    | SECTION_NOT_EDITABLE | 422 | لم يتحقق الشرط: only narrative sections; data sections change only by regeneration |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: section_id, text |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-PRD-GENERATE — توليد المنتج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تقارير ومنتجات | Analyst / Planner | `POST /api/v1/knowledge/products/{id}/actions/generate` | POL-PRD-GENERATE |

**القصة:** بصفتي **Analyst / Planner**، أريد **توليد المنتج**، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشروط المسبقة:** الحالة الحالية: DRAFT, GENERATED, GENERATION_FAILED؛ author; async job with the author's authority
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← GENERATING؛ الحدث EVT-PRD-GENERATION-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PRD-GENERATE` · `AGG-PRODUCT` · متطلبات: REQ-PRD-001, REQ-PRD-002, REQ-PRD-003 · حالات استخدام: UC-110, UC-111
- **ضوابط النوع والفئة:** C-WF، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRD-GENERATE succeeds
  Given AGG-PRODUCT in state DRAFT or GENERATED or GENERATION_FAILED and every guard holds
  When Analyst / Planner sends CMD-PRD-GENERATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes GENERATING
  And EVT-PRD-GENERATION-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRD-GENERATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRD-GENERATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, DISCARDED, GENERATING, IN_REVIEW, SUPERSEDED, WITHDRAWN |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-PRD-RETURN — إعادة المنتج للمراجعة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تقارير ومنتجات | reviewer | `POST /api/v1/knowledge/products/{id}/actions/return` | POL-PRD-RETURN |

**القصة:** بصفتي **reviewer**، أريد **إعادة المنتج للمراجعة**، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشروط المسبقة:** الحالة الحالية: IN_REVIEW؛ reviewer; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← GENERATED؛ الحدث EVT-PRD-RETURNED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PRD-RETURN` · `AGG-PRODUCT` · متطلبات: REQ-PRD-001, REQ-PRD-002, REQ-PRD-003 · حالات استخدام: UC-110, UC-111
- **ضوابط النوع والفئة:** C-WF، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRD-RETURN succeeds
  Given AGG-PRODUCT in state IN_REVIEW and every guard holds
  When reviewer sends CMD-PRD-RETURN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes GENERATED
  And EVT-PRD-RETURNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRD-RETURN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRD-RETURN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, DISCARDED, DRAFT, GENERATED, GENERATING, GENERATION_FAILED, SUPERSEDED, WITHDRAWN |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-PRD-SUBMIT — تقديم المنتج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تقارير ومنتجات | Analyst / Planner | `POST /api/v1/knowledge/products/{id}/actions/submit` | POL-PRD-SUBMIT |

**القصة:** بصفتي **Analyst / Planner**، أريد **تقديم المنتج**، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشروط المسبقة:** الحالة الحالية: GENERATED؛ all required sections present; AI-drafted sections reviewed (REQ-AI-005)
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← IN_REVIEW؛ الحدث EVT-PRD-SUBMITTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PRD-SUBMIT` · `AGG-PRODUCT` · متطلبات: REQ-PRD-001, REQ-PRD-002, REQ-PRD-003 · حالات استخدام: UC-110, UC-111
- **ضوابط النوع والفئة:** C-WF، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRD-SUBMIT succeeds
  Given AGG-PRODUCT in state GENERATED and every guard holds
  When Analyst / Planner sends CMD-PRD-SUBMIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_REVIEW
  And EVT-PRD-SUBMITTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRD-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRD-SUBMIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_INCOMPLETE | 422 | لم يتحقق الشرط: all required sections present; AI-drafted sections reviewed (REQ-AI-005) |
    | PRODUCT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, DISCARDED, DRAFT, GENERATING, GENERATION_FAILED, IN_REVIEW, SUPERSEDED, WITHDRAWN |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-PRD-WITHDRAW — سحب المنتج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تقارير ومنتجات | Manager | `POST /api/v1/knowledge/products/{id}/actions/withdraw` | POL-PRD-WITHDRAW |

**القصة:** بصفتي **Manager**، أريد **سحب المنتج**، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشروط المسبقة:** الحالة الحالية: APPROVED؛ reason; recipients notified
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← WITHDRAWN؛ الحدث EVT-PRD-WITHDRAWN؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PRD-WITHDRAW` · `AGG-PRODUCT` · متطلبات: REQ-PRD-001, REQ-PRD-002, REQ-PRD-003 · حالات استخدام: UC-110, UC-111
- **ضوابط النوع والفئة:** C-DEL، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRD-WITHDRAW succeeds
  Given AGG-PRODUCT in state APPROVED and every guard holds
  When Manager sends CMD-PRD-WITHDRAW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes WITHDRAWN
  And EVT-PRD-WITHDRAWN is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRD-WITHDRAW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRD-WITHDRAW ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, DRAFT, GENERATED, GENERATING, GENERATION_FAILED, IN_REVIEW, SUPERSEDED, WITHDRAWN |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-S-PRODUCT-01 — تلقائي: generation succeeded (المنتج)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | GENERATING | GENERATED |

**القصة:** بصفتي **النظام**، عند «generation succeeded»، أريد نقل **المنتج** إلى GENERATED، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشرط:** every binding executed as known_at = generation time; content items with label > product label excluded; rendered artifacts hashed
- **المخرجات:** الحدث EVT-PRD-GENERATED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PRODUCT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-S-PRODUCT-02 — تلقائي: generation failed (المنتج)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | GENERATING | GENERATION_FAILED |

**القصة:** بصفتي **النظام**، عند «generation failed»، أريد نقل **المنتج** إلى GENERATION_FAILED، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشرط:** error recorded
- **المخرجات:** الحدث EVT-PRD-GENERATION-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PRODUCT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-S-PRODUCT-03 — تلقائي: newer version approved (المنتج)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | APPROVED | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «newer version approved»، أريد نقل **المنتج** إلى SUPERSEDED، لكي يتحقق غرض المنتج: منتج (تقرير، إحاطة، خريطة، منتج تحليلي) مولّد من قالب، يُراجع ويُعتمد ويُجمّد

- **الشرط:** system
- **المخرجات:** الحدث EVT-PRD-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PRODUCT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-Q-DST-LOG — جلب: Distribution and delivery log with watermark ids

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تقارير ومنتجات | distributor, Security Officer, Auditor | `GET /api/v1/knowledge/products/{product_id}/distributions` | POL-DST-LOG |

**القصة:** بصفتي **distributor, Security Officer, Auditor**، أريد **جلب Distribution and delivery log with watermark ids**، لكي يتحقق المتطلب: When a product is distributed, the system shall deliver it only to recipients authorized for its label and shall record each distribution

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Distribution and delivery log with watermark ids؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** distributor, Security Officer, Auditor؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-DST-LOG` · `AGG-PRODUCT` · متطلبات: REQ-PRD-004
- **ضوابط النوع والفئة:** C-READ، K-RPT

```gherkin
Scenario: QRY-DST-LOG returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-DST-LOG with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-DST-LOG is denied
  Given the policy denies the caller
  When the caller sends QRY-DST-LOG
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC06-Q-PRD-GET — جلب: Product version with rendered artifacts (download grants) and pinned citations

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تقارير ومنتجات | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/knowledge/products/{product_id}` | POL-PRD-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Product version with rendered artifacts (download grants) and pinned citations**، لكي يتحقق المتطلب: When a product is approved, the system shall freeze its content as an immutable version with its citations pinned

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Product version with rendered artifacts (download grants) and pinned citations
- **الصلاحية:** audience + label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-PRD-GET` · `AGG-PRODUCT` · متطلبات: REQ-PRD-003
- **ضوابط النوع والفئة:** C-READ، K-RPT

```gherkin
Scenario: QRY-PRD-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-PRD-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-PRD-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-PRD-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC06-Q-PRD-LIST — جلب: Products by kind, state, situation/case, date

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تقارير ومنتجات | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/knowledge/products` | POL-PRD-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Products by kind, state, situation/case, date**، لكي يتحقق المتطلب: The system shall produce reports, briefings, map products and analytical products from versioned templates with sections, data, evidence, citations, maps and charts

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Products by kind, state, situation/case, date؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-PRD-LIST` · `AGG-PRODUCT` · متطلبات: REQ-PRD-001
- **ضوابط النوع والفئة:** C-READ، K-RPT

```gherkin
Scenario: QRY-PRD-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-PRD-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-PRD-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-PRD-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-PRODUCT-TEMPLATE — قالب المنتج (Product Template)

`03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md` · SLC-12 · الحالات: DRAFT, ACTIVE → RETIRED

#### US-BC06-PTM-ACTIVATE — تفعيل قالب المنتج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تقارير ومنتجات | second approver | `POST /api/v1/knowledge/product-templates/{id}/actions/activate` | POL-PTM-ACTIVATE |

**القصة:** بصفتي **second approver**، أريد **تفعيل قالب المنتج**، لكي يتحقق غرض قالب المنتج: قالب منتج بأقسام وربط بيانات، بإصدارات

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ sample generation succeeded; approver ≠ author
- **المدخلات:** `sample_ref`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-PTM-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Knowledge Manager / Analysis lead (define, edit) · second approver (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: approver ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-PTM-ACTIVATE` · `AGG-PRODUCT-TEMPLATE` · متطلبات: REQ-PRD-001 · حالات استخدام: UC-110
- **ضوابط النوع والفئة:** C-WF، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PTM-ACTIVATE succeeds
  Given AGG-PRODUCT-TEMPLATE in state DRAFT and every guard holds
  When second approver sends CMD-PTM-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-PTM-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PTM-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PTM-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: sample_ref |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-PTM-DEFINE — تعريف قالب المنتج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تقارير ومنتجات | Knowledge Manager / Analysis lead | `POST /api/v1/knowledge/product-templates` | POL-PTM-DEFINE |

**القصة:** بصفتي **Knowledge Manager / Analysis lead**، أريد **تعريف قالب المنتج**، لكي يتحقق غرض قالب المنتج: قالب منتج بأقسام وربط بيانات، بإصدارات

- **الشروط المسبقة:** الحالة الحالية: ∅؛ code unique; product kind ∈ {report, briefing, map_product, analytical_product}
- **المدخلات:** `code`!: string, `kind`!: enum(report,briefing,map_product,analytical_product), `name`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-PTM-DEFINED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Knowledge Manager / Analysis lead (define, edit) · second approver (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PTM-DEFINE` · `AGG-PRODUCT-TEMPLATE` · متطلبات: REQ-PRD-001 · حالات استخدام: UC-110
- **ضوابط النوع والفئة:** C-CRE، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PTM-DEFINE succeeds
  Given AGG-PRODUCT-TEMPLATE does not exist yet and every guard holds
  When Knowledge Manager / Analysis lead sends CMD-PTM-DEFINE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-PTM-DEFINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PTM-DEFINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PTM-DEFINE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TEMPLATE_INVALID | 422 | لم يتحقق الشرط: code unique; product kind ∈ {report, briefing, map_product, analytical_product} |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: code, kind, name |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-PTM-EDIT — تعديل قالب المنتج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تقارير ومنتجات | Knowledge Manager / Analysis lead | `POST /api/v1/knowledge/product-templates/{id}/actions/edit` | POL-PTM-EDIT |

**القصة:** بصفتي **Knowledge Manager / Analysis lead**، أريد **تعديل قالب المنتج**، لكي يتحقق غرض قالب المنتج: قالب منتج بأقسام وربط بيانات، بإصدارات

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE؛ sections valid (text, map, chart, table, key_judgments, citations); every data binding is a declared platform query with typed parameters; ACTIVE → new version
- **المدخلات:** `sections`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-PTM-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Knowledge Manager / Analysis lead (define, edit) · second approver (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PTM-EDIT` · `AGG-PRODUCT-TEMPLATE` · متطلبات: REQ-PRD-001 · حالات استخدام: UC-110
- **ضوابط النوع والفئة:** C-UPD، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PTM-EDIT succeeds
  Given AGG-PRODUCT-TEMPLATE in state DRAFT or ACTIVE and every guard holds
  When Knowledge Manager / Analysis lead sends CMD-PTM-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-PTM-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PTM-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PTM-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | TEMPLATE_INVALID | 422 | لم يتحقق الشرط: sections valid (text, map, chart, table, key_judgments, citations); every data binding is a declared platform query with typed parameters; ACTIVE → new version |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: sections |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-PTM-RETIRE — إحالة قالب المنتج إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تقارير ومنتجات | Knowledge Manager / Analysis lead (محسوم: `17-security-design.md` §5) | `POST /api/v1/knowledge/product-templates/{id}/actions/retire` | POL-PTM-RETIRE |

**القصة:** بصفتي **Knowledge Manager / Analysis lead**، أريد **إحالة قالب المنتج إلى التقاعد**، لكي يتحقق غرض قالب المنتج: قالب منتج بأقسام وربط بيانات، بإصدارات

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason; existing products keep their pinned version
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-PTM-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Knowledge Manager / Analysis lead (retire) — issuing role named by CR-77؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PTM-RETIRE` · `AGG-PRODUCT-TEMPLATE` · متطلبات: REQ-PRD-001 · حالات استخدام: UC-110
- **ضوابط النوع والفئة:** C-DEL، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PTM-RETIRE succeeds
  Given AGG-PRODUCT-TEMPLATE in state ACTIVE and every guard holds
  When Knowledge Manager / Analysis lead sends CMD-PTM-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-PTM-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PTM-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PTM-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DRAFT, RETIRED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

### AGG-RECONSTRUCTION — إعادة البناء التاريخي (Historical Reconstruction)

`03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md` · SLC-12 · الحالات: REQUESTED, RUNNING → COMPLETED, FAILED, CANCELLED

#### US-BC06-REC-CANCEL — إلغاء إعادة البناء التاريخي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تقارير ومنتجات | Auditor / Legal / Analyst | `POST /api/v1/knowledge/reconstructions/{id}/actions/cancel` | POL-REC-CANCEL |

**القصة:** بصفتي **Auditor / Legal / Analyst**، أريد **إلغاء إعادة البناء التاريخي**، لكي يتحقق غرض إعادة البناء التاريخي: إعادة بناء حالة نطاق كما كانت صحيحة في T وكما كانت معروفة في K

- **الشروط المسبقة:** الحالة الحالية: REQUESTED, RUNNING؛ requester; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-REC-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Auditor / Legal / Analyst (request, cancel)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-REC-CANCEL` · `AGG-RECONSTRUCTION` · متطلبات: REQ-ARC-004 · حالات استخدام: UC-065
- **ضوابط النوع والفئة:** C-DEL، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-REC-CANCEL succeeds
  Given AGG-RECONSTRUCTION in state REQUESTED or RUNNING and every guard holds
  When Auditor / Legal / Analyst sends CMD-REC-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-REC-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-REC-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-REC-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | RECONSTRUCTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, FAILED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-REC-REQUEST — طلب إعادة البناء التاريخي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تقارير ومنتجات | Auditor / Legal / Analyst | `POST /api/v1/knowledge/reconstructions` | POL-REC-REQUEST |

**القصة:** بصفتي **Auditor / Legal / Analyst**، أريد **طلب إعادة البناء التاريخي**، لكي يتحقق غرض إعادة البناء التاريخي: إعادة بناء حالة نطاق كما كانت صحيحة في T وكما كانت معروفة في K

- **الشروط المسبقة:** الحالة الحالية: ∅؛ scope (objects, situation, plan, decision basis); valid_at T; known_at K ≤ now; purpose (audit, legal, lessons); requester authorized
- **المدخلات:** `scope`!: object, `valid_at`!: date-time, `known_at`!: date-time, `purpose`!: enum(audit,legal,lessons,analysis) — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← REQUESTED؛ الحدث EVT-REC-REQUESTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Auditor / Legal / Analyst (request, cancel)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-REC-REQUEST` · `AGG-RECONSTRUCTION` · متطلبات: REQ-ARC-004 · حالات استخدام: UC-065
- **ضوابط النوع والفئة:** C-CRE، K-RPT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-REC-REQUEST succeeds
  Given AGG-RECONSTRUCTION does not exist yet and every guard holds
  When Auditor / Legal / Analyst sends CMD-REC-REQUEST with a valid payload, a new Idempotency-Key
  Then the state becomes REQUESTED
  And EVT-REC-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-REC-REQUEST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-REC-REQUEST ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RECONSTRUCTION_INVALID | 422 | لم يتحقق الشرط: scope (objects, situation, plan, decision basis); valid_at T; known_at K ≤ now; purpose (audit, legal, lessons); requester authorized |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: scope, valid_at, known_at, purpose |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC06-S-RECONSTRUCTION-01 — تلقائي: worker started (إعادة البناء التاريخي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | REQUESTED | RUNNING |

**القصة:** بصفتي **النظام**، عند «worker started»، أريد نقل **إعادة البناء التاريخي** إلى RUNNING، لكي يتحقق غرض إعادة البناء التاريخي: إعادة بناء حالة نطاق كما كانت صحيحة في T وكما كانت معروفة في K

- **الشرط:** runs with the requester's authority
- **المخرجات:** الحدث EVT-REC-STARTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-RECONSTRUCTION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-S-RECONSTRUCTION-02 — تلقائي: completed (إعادة البناء التاريخي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | RUNNING | COMPLETED |

**القصة:** بصفتي **النظام**، عند «completed»، أريد نقل **إعادة البناء التاريخي** إلى COMPLETED، لكي يتحقق غرض إعادة البناء التاريخي: إعادة بناء حالة نطاق كما كانت صحيحة في T وكما كانت معروفة في K

- **الشرط:** report: every element labelled RECORDED / RECONSTRUCTED / INFERRED (with rule) / UNKNOWN; archive retrievals included where needed
- **المخرجات:** الحدث EVT-REC-COMPLETED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-RECONSTRUCTION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-S-RECONSTRUCTION-03 — تلقائي: failed (إعادة البناء التاريخي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | RUNNING | FAILED |

**القصة:** بصفتي **النظام**، عند «failed»، أريد نقل **إعادة البناء التاريخي** إلى FAILED، لكي يتحقق غرض إعادة البناء التاريخي: إعادة بناء حالة نطاق كما كانت صحيحة في T وكما كانت معروفة في K

- **الشرط:** error recorded
- **المخرجات:** الحدث EVT-REC-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-RECONSTRUCTION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC06-Q-REC-REPORT — جلب: Labelled reconstruction report

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تقارير ومنتجات | requester, Auditor | `GET /api/v1/knowledge/reconstructions/{reconstruction_id}/report` | POL-REC-REPORT |

**القصة:** بصفتي **requester, Auditor**، أريد **جلب Labelled reconstruction report**، لكي يتحقق المتطلب: When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the state from versions, events, valid time, effective time and provenance, labelling each element RECORDED, RECONSTRUCTED, INFERRED or UNKNOWN

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Labelled reconstruction report؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** requester, Auditor؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-REC-REPORT` · `AGG-RECONSTRUCTION` · متطلبات: REQ-ARC-004
- **ضوابط النوع والفئة:** C-READ، K-RPT

```gherkin
Scenario: QRY-REC-REPORT returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-REC-REPORT with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-REC-REPORT is denied
  Given the policy denies the caller
  When the caller sends QRY-REC-REPORT
  Then the response has the same shape as for a missing item (not-found shape)
```

<!-- END GENERATED: build_analysis_design.py -->
