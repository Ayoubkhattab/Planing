---
id: AD-05-US-BC07
type: user-stories
title: "قصص المستخدم — BC07"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
generator: 17-system-study/_build/build_analysis_design.py
---

# قصص المستخدم — BC07 Platform Intelligence — التكامل والذكاء الاصطناعي

مولَّد بالكامل من المصادر بواسطة `17-system-study/_build/build_analysis_design.py`؛ لا يُحرَّر يدويًا. القالب والتصنيف وتعريف ضوابط النوع والفئة في [00-guide.md](00-guide.md).

<!-- BEGIN GENERATED: build_analysis_design.py -->

## ملخص BC07

| نوع العملية | عدد القصص |
|---|---|
| إنشاء | 11 |
| تعديل | 5 |
| جلب | 19 |
| حذف / إنهاء | 17 |
| سير عمل | 25 |
| نظام (SYS) | 27 |
| **المجموع** | **104** |

### AGG-ADAPTER — المحوّل (Adapter)

`03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md` · SLC-02 · الحالات: DRAFT, ACTIVE, SUSPENDED → RETIRED

#### US-BC07-ADP-ACTIVATE — تفعيل المحوّل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | second Administrator | `POST /api/v1/integration/adapters/{id}/actions/activate` | POL-ADP-ACTIVATE |

**القصة:** بصفتي **second Administrator**، أريد **تفعيل المحوّل**، لكي يتحقق غرض المحوّل: محول تكامل مسجل بمصدر وحساب خدمة وإصدار تحويل

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ mapping tests pass; approver ≠ author
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-ADP-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Administrator (register, update) · second Administrator (activate)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: approver ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-ADP-ACTIVATE` · `AGG-ADAPTER` · متطلبات: REQ-INF-005, REQ-INF-008, REQ-INF-009 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ADP-ACTIVATE succeeds
  Given AGG-ADAPTER in state DRAFT and every guard holds
  When second Administrator sends CMD-ADP-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-ADP-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ADP-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ADAPTER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED, SUSPENDED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ADP-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-ADP-REGISTER — تسجيل المحوّل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تكامل | Administrator | `POST /api/v1/integration/adapters` | POL-ADP-REGISTER |

**القصة:** بصفتي **Administrator**، أريد **تسجيل المحوّل**، لكي يتحقق غرض المحوّل: محول تكامل مسجل بمصدر وحساب خدمة وإصدار تحويل

- **الشروط المسبقة:** الحالة الحالية: ∅؛ source ACTIVE; service account ACTIVE; mapping spec present
- **المدخلات:** `name`!: string, `source`!: urn, `service_account`!: urn, `mapping`!: object — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-ADP-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Administrator (register, update) · second Administrator (activate)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ADP-REGISTER` · `AGG-ADAPTER` · متطلبات: REQ-INF-005, REQ-INF-008, REQ-INF-009 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-CRE، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ADP-REGISTER succeeds
  Given AGG-ADAPTER does not exist yet and every guard holds
  When Administrator sends CMD-ADP-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-ADP-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ADP-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ADAPTER_INVALID | 422 | لم يتحقق الشرط: source ACTIVE; service account ACTIVE; mapping spec present |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ADP-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: name, source, service_account, mapping |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-ADP-RESUME — استئناف المحوّل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | second Administrator (محسوم: `17-security-design.md` §5) | `POST /api/v1/integration/adapters/{id}/actions/resume` | POL-ADP-RESUME |

**القصة:** بصفتي **second Administrator**، أريد **استئناف المحوّل**، لكي يتحقق غرض المحوّل: محول تكامل مسجل بمصدر وحساب خدمة وإصدار تحويل

- **الشروط المسبقة:** الحالة الحالية: SUSPENDED؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-ADP-RESUMED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Administrator (register, update) · second Administrator (activate)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ADP-RESUME` · `AGG-ADAPTER` · متطلبات: REQ-INF-005, REQ-INF-008, REQ-INF-009 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ADP-RESUME succeeds
  Given AGG-ADAPTER in state SUSPENDED and every guard holds
  When second Administrator sends CMD-ADP-RESUME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-ADP-RESUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ADP-RESUME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ADAPTER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DRAFT, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ADP-RESUME ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-ADP-RETIRE — إحالة المحوّل إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | Administrator (محسوم: `17-security-design.md` §5) | `POST /api/v1/integration/adapters/{id}/actions/retire` | POL-ADP-RETIRE |

**القصة:** بصفتي **Administrator**، أريد **إحالة المحوّل إلى التقاعد**، لكي يتحقق غرض المحوّل: محول تكامل مسجل بمصدر وحساب خدمة وإصدار تحويل

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE, SUSPENDED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-ADP-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Administrator (register, update) · second Administrator (activate)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ADP-RETIRE` · `AGG-ADAPTER` · متطلبات: REQ-INF-005, REQ-INF-008, REQ-INF-009 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ADP-RETIRE succeeds
  Given AGG-ADAPTER in state DRAFT or ACTIVE or SUSPENDED and every guard holds
  When Administrator sends CMD-ADP-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-ADP-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ADP-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ADAPTER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ADP-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-ADP-SUSPEND — تعليق المحوّل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | Administrator (محسوم: `17-security-design.md` §5) | `POST /api/v1/integration/adapters/{id}/actions/suspend` | POL-ADP-SUSPEND |

**القصة:** بصفتي **Administrator**، أريد **تعليق المحوّل**، لكي يتحقق غرض المحوّل: محول تكامل مسجل بمصدر وحساب خدمة وإصدار تحويل

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SUSPENDED؛ الحدث EVT-ADP-SUSPENDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Administrator (register, update) · second Administrator (activate)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ADP-SUSPEND` · `AGG-ADAPTER` · متطلبات: REQ-INF-005, REQ-INF-008, REQ-INF-009 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ADP-SUSPEND succeeds
  Given AGG-ADAPTER in state ACTIVE and every guard holds
  When Administrator sends CMD-ADP-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUSPENDED
  And EVT-ADP-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ADP-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ADAPTER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DRAFT, RETIRED, SUSPENDED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ADP-SUSPEND ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-ADP-UPDATE-MAPPING — تحديث ربط حقول المحوّل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تكامل | Administrator | `POST /api/v1/integration/adapters/{id}/actions/update-mapping` | POL-ADP-UPDATE-MAPPING |

**القصة:** بصفتي **Administrator**، أريد **تحديث ربط حقول المحوّل**، لكي يتحقق غرض المحوّل: محول تكامل مسجل بمصدر وحساب خدمة وإصدار تحويل

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE؛ mapping tests pass; new immutable mapping version
- **المدخلات:** `mapping`!: object, `tests`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ADP-MAPPING-UPDATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Administrator (register, update) · second Administrator (activate)؛ الشروط: tenant match; object visible to subject (label ≤ clearance); write permission in org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ADP-UPDATE-MAPPING` · `AGG-ADAPTER` · متطلبات: REQ-INF-005, REQ-INF-008, REQ-INF-009 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-UPD، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ADP-UPDATE-MAPPING succeeds
  Given AGG-ADAPTER in state DRAFT or ACTIVE and every guard holds
  When Administrator sends CMD-ADP-UPDATE-MAPPING with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ADP-MAPPING-UPDATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ADP-UPDATE-MAPPING is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ADAPTER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED, SUSPENDED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ADP-UPDATE-MAPPING ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MAPPING_TESTS_FAILED | 422 | لم يتحقق الشرط: mapping tests pass; new immutable mapping version |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: mapping, tests |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-Q-ADP-GET — جلب: Adapter with mapping versions

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | Administrator | `GET /api/v1/integration/adapters/{adapter_id}` | POL-ADP-GET |

**القصة:** بصفتي **Administrator**، أريد **جلب Adapter with mapping versions**، لكي يتحقق المتطلب: The system shall ingest external data only through registered adapters or bulk import jobs that record source, batch, transformation and lineage

- **المدخلات:** `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Adapter with mapping versions
- **الصلاحية:** Administrator؛ النطاق المسموح: org scope ∩ classification rule; claims filtered by label؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-ADP-GET` · `AGG-ADAPTER` · متطلبات: REQ-INF-005
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-ADP-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-ADP-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-ADP-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-ADP-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-AI-REQUEST — طلب الذكاء الاصطناعي (AI Request)

`03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md` · SLC-10 · الحالات: RECEIVED, RETRIEVING, GENERATING → COMPLETED, INSUFFICIENT_EVIDENCE, REFUSED, FAILED, CANCELLED

#### US-BC07-AIR-CANCEL — إلغاء طلب الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | any authorized user | `POST /api/v1/ai/requests/{id}/actions/cancel` | POL-AIR-CANCEL |

**القصة:** بصفتي **any authorized user**، أريد **إلغاء طلب الذكاء الاصطناعي**، لكي يتحقق غرض طلب الذكاء الاصطناعي: طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض

- **الشروط المسبقة:** الحالة الحالية: RECEIVED, RETRIEVING, GENERATING؛ requester
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-AIR-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any authorized user (submit, cancel)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AIR-CANCEL` · `AGG-AI-REQUEST` · متطلبات: REQ-AI-001, REQ-AI-002, REQ-AI-003, REQ-AI-004, REQ-AI-007, REQ-AI-008, REQ-AI-011, REQ-AI-012 · حالات استخدام: UC-070, UC-071, UC-072, UC-074, UC-077
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AIR-CANCEL succeeds
  Given AGG-AI-REQUEST in state RECEIVED or RETRIEVING or GENERATING and every guard holds
  When any authorized user sends CMD-AIR-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-AIR-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AIR-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_REQUEST_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, FAILED, INSUFFICIENT_EVIDENCE, REFUSED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AIR-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-AIR-SUBMIT — تقديم طلب الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تحليل | any authorized user | `POST /api/v1/ai/requests` | POL-AIR-SUBMIT |

**القصة:** بصفتي **any authorized user**، أريد **تقديم طلب الذكاء الاصطناعي**، لكي يتحقق غرض طلب الذكاء الاصطناعي: طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض

- **الشروط المسبقة:** الحالة الحالية: ∅؛ operation ∈ AI autonomy matrix and allowed at the tenant's routing; user authenticated; purpose; input size ≤ limit; per-tenant AI quota
- **المدخلات:** `operation`!: string, `input`!: LocalizedName, `scope`: object, `purpose`!: string, `target`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← RECEIVED؛ الحدث EVT-AIR-RECEIVED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** any authorized user (submit, cancel)؛ الشروط: tenant match; operation allowed by routing and matrix؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AIR-SUBMIT` · `AGG-AI-REQUEST` · متطلبات: REQ-AI-001, REQ-AI-002, REQ-AI-003, REQ-AI-004, REQ-AI-007, REQ-AI-008, REQ-AI-011, REQ-AI-012 · حالات استخدام: UC-070, UC-071, UC-072, UC-074, UC-077
- **ضوابط النوع والفئة:** C-CRE، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AIR-SUBMIT succeeds
  Given AGG-AI-REQUEST does not exist yet and every guard holds
  When any authorized user sends CMD-AIR-SUBMIT with a valid payload, a new Idempotency-Key
  Then the state becomes RECEIVED
  And EVT-AIR-RECEIVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AIR-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_OPERATION_NOT_ALLOWED | 422 | لم يتحقق الشرط: operation ∈ AI autonomy matrix and allowed at the tenant's routing |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AIR-SUBMIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: operation, input, purpose |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-AI-REQUEST-01 — تلقائي: policy denied (طلب الذكاء الاصطناعي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | RECEIVED | REFUSED |

**القصة:** بصفتي **النظام**، عند «policy denied»، أريد نقل **طلب الذكاء الاصطناعي** إلى REFUSED، لكي يتحقق غرض طلب الذكاء الاصطناعي: طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض

- **الشرط:** PDP on (user, ai.<operation>, scope) denied or AIL above matrix
- **المخرجات:** الحدث EVT-AIR-REFUSED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-AI-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-AI-REQUEST-02 — تلقائي: retrieval started (طلب الذكاء الاصطناعي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | RECEIVED | RETRIEVING |

**القصة:** بصفتي **النظام**، عند «retrieval started»، أريد نقل **طلب الذكاء الاصطناعي** إلى RETRIEVING، لكي يتحقق غرض طلب الذكاء الاصطناعي: طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض

- **الشرط:** authorized hybrid retrieval as the user (SPEC-AI §2)
- **المخرجات:** الحدث EVT-AIR-RETRIEVING؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-AI-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-AI-REQUEST-03 — تلقائي: context package sealed (طلب الذكاء الاصطناعي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | RETRIEVING | GENERATING |

**القصة:** بصفتي **النظام**، عند «context package sealed»، أريد نقل **طلب الذكاء الاصطناعي** إلى GENERATING، لكي يتحقق غرض طلب الذكاء الاصطناعي: طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض

- **الشرط:** context items pinned (URN + version/known_at + label); package hash; token budget respected
- **المخرجات:** الحدث EVT-AIR-CONTEXT-SEALED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-AI-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-AI-REQUEST-04 — تلقائي: no sufficient evidence retrieved (طلب الذكاء الاصطناعي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | RETRIEVING | INSUFFICIENT_EVIDENCE |

**القصة:** بصفتي **النظام**، عند «no sufficient evidence retrieved»، أريد نقل **طلب الذكاء الاصطناعي** إلى INSUFFICIENT_EVIDENCE، لكي يتحقق غرض طلب الذكاء الاصطناعي: طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض

- **الشرط:** coverage below threshold (SPEC-AI §4)
- **المخرجات:** الحدث EVT-AIR-INSUFFICIENT-EVIDENCE؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-AI-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-AI-REQUEST-05 — تلقائي: output grounded (طلب الذكاء الاصطناعي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | GENERATING | COMPLETED |

**القصة:** بصفتي **النظام**، عند «output grounded»، أريد نقل **طلب الذكاء الاصطناعي** إلى COMPLETED، لكي يتحقق غرض طلب الذكاء الاصطناعي: طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض

- **الشرط:** every statement cites ≥ 1 context item; citation check passed; output label = max(context labels); guard checks passed (SPEC-AI §5)
- **المخرجات:** الحدث EVT-AIR-COMPLETED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-AI-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-AI-REQUEST-06 — تلقائي: output not grounded (طلب الذكاء الاصطناعي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | GENERATING | INSUFFICIENT_EVIDENCE |

**القصة:** بصفتي **النظام**، عند «output not grounded»، أريد نقل **طلب الذكاء الاصطناعي** إلى INSUFFICIENT_EVIDENCE، لكي يتحقق غرض طلب الذكاء الاصطناعي: طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض

- **الشرط:** ungrounded statements removed leave no answer
- **المخرجات:** الحدث EVT-AIR-INSUFFICIENT-EVIDENCE؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-AI-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-AI-REQUEST-07 — تلقائي: error or timeout (طلب الذكاء الاصطناعي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | RETRIEVING, GENERATING | FAILED |

**القصة:** بصفتي **النظام**، عند «error or timeout»، أريد نقل **طلب الذكاء الاصطناعي** إلى FAILED، لكي يتحقق غرض طلب الذكاء الاصطناعي: طلب ذكاء اصطناعي واحد بمساره الكامل: سياسة، استرجاع مصرّح، حزمة سياق، نموذج، تأريض

- **الشرط:** error recorded
- **المخرجات:** الحدث EVT-AIR-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-AI-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-Q-AIR-CONTEXT — جلب: Context package items (URN, version, label) — for audit and review

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | requester if cleared; Auditor | `GET /api/v1/ai/requests/{request_id}/context` | POL-AIR-CONTEXT |

**القصة:** بصفتي **requester if cleared; Auditor**، أريد **جلب Context package items (URN, version, label) — for audit and review**، لكي يتحقق المتطلب: The system shall build context packages only from data retrieved with the requesting user's authorization, including vector retrieval

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Context package items (URN, version, label) — for audit and review؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** requester if cleared; Auditor؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AIR-CONTEXT` · `AGG-AI-REQUEST` · متطلبات: REQ-AI-002
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-AIR-CONTEXT returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-AIR-CONTEXT with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-AIR-CONTEXT is denied
  Given the policy denies the caller
  When the caller sends QRY-AIR-CONTEXT
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC07-Q-AIR-GET — جلب: Request with answer, statements and citations (visible only), status

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | requester; Auditor (metadata) | `GET /api/v1/ai/requests/{request_id}` | POL-AIR-GET |

**القصة:** بصفتي **requester; Auditor (metadata)**، أريد **جلب Request with answer, statements and citations (visible only), status**، لكي يتحقق المتطلب: The system shall process every AI request through identity, policy, authorized retrieval, context package, model, output, grounding and confidence, and shall record each step

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Request with answer, statements and citations (visible only), status
- **الصلاحية:** requester; Auditor (metadata)؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AIR-GET` · `AGG-AI-REQUEST` · متطلبات: REQ-AI-001
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-AIR-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-AIR-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-AIR-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-AIR-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-AI-RESULT — نتيجة الذكاء الاصطناعي (AI Result (reviewable))

`03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md` · SLC-10 · الحالات: PROPOSED, UNDER_REVIEW → ACCEPTED, PARTIALLY_ACCEPTED, REJECTED

#### US-BC07-AIRS-ACCEPT — قبول نتيجة الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | reviewer authorized on the target | `POST /api/v1/ai/results/{id}/actions/accept` | POL-AIRS-ACCEPT |

**القصة:** بصفتي **reviewer authorized on the target**، أريد **قبول نتيجة الذكاء الاصطناعي**، لكي يتحقق غرض نتيجة الذكاء الاصطناعي: مخرج AI يحتاج مراجعة بشرية قبل أن يؤثر: مسودة، استخراج، ترجمة كدليل، اقتراح مطابقة

- **الشروط المسبقة:** الحالة الحالية: UNDER_REVIEW؛ effects applied through owner commands as the reviewer, with agent = model version in lineage (e.g. CMD-CLM-ASSERT, product section, CMD-ER-PROPOSE)
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACCEPTED؛ الحدث EVT-AIRS-ACCEPTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** reviewer authorized on the target (review, accept, reject)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AIRS-ACCEPT` · `AGG-AI-RESULT` · متطلبات: REQ-AI-005, REQ-AI-006, REQ-AI-008 · حالات استخدام: UC-072, UC-073, UC-074
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AIRS-ACCEPT succeeds
  Given AGG-AI-RESULT in state UNDER_REVIEW and every guard holds
  When reviewer authorized on the target sends CMD-AIRS-ACCEPT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACCEPTED
  And EVT-AIRS-ACCEPTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AIRS-ACCEPT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_RESULT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, PARTIALLY_ACCEPTED, PROPOSED, REJECTED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AIRS-ACCEPT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OWNER_REJECTED | 422 | لم يتحقق الشرط: effects applied through owner commands as the reviewer, with agent = model version in lineage (e.g. CMD-CLM-ASSERT, product section, CMD-ER-PROPOSE) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-AIRS-ACCEPT-PARTIALLY — قبول نتيجة الذكاء الاصطناعي جزئيًا

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | reviewer authorized on the target | `POST /api/v1/ai/results/{id}/actions/accept-partially` | POL-AIRS-ACCEPT-PARTIALLY |

**القصة:** بصفتي **reviewer authorized on the target**، أريد **قبول نتيجة الذكاء الاصطناعي جزئيًا**، لكي يتحقق غرض نتيجة الذكاء الاصطناعي: مخرج AI يحتاج مراجعة بشرية قبل أن يؤثر: مسودة، استخراج، ترجمة كدليل، اقتراح مطابقة

- **الشروط المسبقة:** الحالة الحالية: UNDER_REVIEW؛ selected items only; rejected items recorded with reasons
- **المدخلات:** `accepted_items`!: array, `rejected_items`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PARTIALLY_ACCEPTED؛ الحدث EVT-AIRS-PARTIALLY-ACCEPTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** reviewer authorized on the target (review, accept, reject)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AIRS-ACCEPT-PARTIALLY` · `AGG-AI-RESULT` · متطلبات: REQ-AI-005, REQ-AI-006, REQ-AI-008 · حالات استخدام: UC-072, UC-073, UC-074
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AIRS-ACCEPT-PARTIALLY succeeds
  Given AGG-AI-RESULT in state UNDER_REVIEW and every guard holds
  When reviewer authorized on the target sends CMD-AIRS-ACCEPT-PARTIALLY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PARTIALLY_ACCEPTED
  And EVT-AIRS-PARTIALLY-ACCEPTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AIRS-ACCEPT-PARTIALLY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_RESULT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, PARTIALLY_ACCEPTED, PROPOSED, REJECTED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AIRS-ACCEPT-PARTIALLY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OWNER_REJECTED | 422 | لم يتحقق الشرط: rejected items recorded with reasons |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: accepted_items, rejected_items |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-AIRS-REJECT — رفض نتيجة الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تحليل | reviewer authorized on the target | `POST /api/v1/ai/results/{id}/actions/reject` | POL-AIRS-REJECT |

**القصة:** بصفتي **reviewer authorized on the target**، أريد **رفض نتيجة الذكاء الاصطناعي**، لكي يتحقق غرض نتيجة الذكاء الاصطناعي: مخرج AI يحتاج مراجعة بشرية قبل أن يؤثر: مسودة، استخراج، ترجمة كدليل، اقتراح مطابقة

- **الشروط المسبقة:** الحالة الحالية: PROPOSED, UNDER_REVIEW؛ reason (feeds evaluation)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-AIRS-REJECTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** reviewer authorized on the target (review, accept, reject)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AIRS-REJECT` · `AGG-AI-RESULT` · متطلبات: REQ-AI-005, REQ-AI-006, REQ-AI-008 · حالات استخدام: UC-072, UC-073, UC-074
- **ضوابط النوع والفئة:** C-DEL، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AIRS-REJECT succeeds
  Given AGG-AI-RESULT in state PROPOSED or UNDER_REVIEW and every guard holds
  When reviewer authorized on the target sends CMD-AIRS-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-AIRS-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AIRS-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_RESULT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, PARTIALLY_ACCEPTED, REJECTED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AIRS-REJECT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-AIRS-START-REVIEW — بدء مراجعة نتيجة الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تحليل | reviewer authorized on the target | `POST /api/v1/ai/results/{id}/actions/start-review` | POL-AIRS-START-REVIEW |

**القصة:** بصفتي **reviewer authorized on the target**، أريد **بدء مراجعة نتيجة الذكاء الاصطناعي**، لكي يتحقق غرض نتيجة الذكاء الاصطناعي: مخرج AI يحتاج مراجعة بشرية قبل أن يؤثر: مسودة، استخراج، ترجمة كدليل، اقتراح مطابقة

- **الشروط المسبقة:** الحالة الحالية: PROPOSED؛ reviewer authorized for the target and cleared for the result label
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← UNDER_REVIEW؛ الحدث EVT-AIRS-REVIEW-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** reviewer authorized on the target (review, accept, reject)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AIRS-START-REVIEW` · `AGG-AI-RESULT` · متطلبات: REQ-AI-005, REQ-AI-006, REQ-AI-008 · حالات استخدام: UC-072, UC-073, UC-074
- **ضوابط النوع والفئة:** C-WF، K-ANL (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AIRS-START-REVIEW succeeds
  Given AGG-AI-RESULT in state PROPOSED and every guard holds
  When reviewer authorized on the target sends CMD-AIRS-START-REVIEW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNDER_REVIEW
  And EVT-AIRS-REVIEW-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AIRS-START-REVIEW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_RESULT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, PARTIALLY_ACCEPTED, REJECTED, UNDER_REVIEW |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AIRS-START-REVIEW ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REVIEWER_NOT_CLEARED | 422 | لم يتحقق الشرط: reviewer authorized for the target and cleared for the result label |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-AI-RESULT-01 — تلقائي: request COMPLETED for a reviewable operation (نتيجة الذكاء الاصطناعي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | ∅ | PROPOSED |

**القصة:** بصفتي **النظام**، عند «request COMPLETED for a reviewable operation»، أريد نقل **نتيجة الذكاء الاصطناعي** إلى PROPOSED، لكي يتحقق غرض نتيجة الذكاء الاصطناعي: مخرج AI يحتاج مراجعة بشرية قبل أن يؤثر: مسودة، استخراج، ترجمة كدليل، اقتراح مطابقة

- **الشرط:** operation ∈ {AI-OP-03 draft, AI-OP-04 extract, AI-OP-05 translation used as evidence, AI-OP-06 match suggestion}
- **المخرجات:** الحدث EVT-AIRS-PROPOSED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-AI-RESULT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-Q-AIRS-QUEUE — جلب: Reviewable AI results by state, operation, target

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تحليل | reviewers authorized on targets | `GET /api/v1/ai/results` | POL-AIRS-QUEUE |

**القصة:** بصفتي **reviewers authorized on targets**، أريد **جلب Reviewable AI results by state, operation, target**، لكي يتحقق المتطلب: The system shall label every AI-generated draft as AI output and shall prevent its publication without human review

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Reviewable AI results by state, operation, target؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** reviewers authorized on targets؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AIRS-QUEUE` · `AGG-AI-RESULT` · متطلبات: REQ-AI-005
- **ضوابط النوع والفئة:** C-READ، K-ANL

```gherkin
Scenario: QRY-AIRS-QUEUE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-AIRS-QUEUE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-AIRS-QUEUE is denied
  Given the policy denies the caller
  When the caller sends QRY-AIRS-QUEUE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-AI-ROUTING — توجيه الذكاء الاصطناعي (AI Routing Configuration)

`03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md` · SLC-10 · الحالات: DRAFT, ACTIVE → SUPERSEDED, DISCARDED

#### US-BC07-RTG-ACTIVATE — تفعيل توجيه الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | second authority | `POST /api/v1/ai/routings/{id}/actions/activate` | POL-RTG-ACTIVATE |

**القصة:** بصفتي **second authority**، أريد **تفعيل توجيه الذكاء الاصطناعي**، لكي يتحقق غرض توجيه الذكاء الاصطناعي: ربط كل عملية AI بنموذج إنتاجي وقالب تعليمات وحدود الاستقلالية لكل مستأجر

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ approver ≠ author; previous ACTIVE → SUPERSEDED
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-RTG-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI governance authority (draft, edit) · second authority (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: approver ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-RTG-ACTIVATE` · `AGG-AI-ROUTING` · متطلبات: REQ-AI-008, REQ-AI-011 · حالات استخدام: UC-074, UC-077
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RTG-ACTIVATE succeeds
  Given AGG-AI-ROUTING in state DRAFT and every guard holds
  When second authority sends CMD-RTG-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-RTG-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RTG-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_ROUTING_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISCARDED, SUPERSEDED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RTG-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-RTG-DISCARD — تجاهل مسودة توجيه الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | AI governance authority | `POST /api/v1/ai/routings/{id}/actions/discard` | POL-RTG-DISCARD |

**القصة:** بصفتي **AI governance authority**، أريد **تجاهل مسودة توجيه الذكاء الاصطناعي**، لكي يتحقق غرض توجيه الذكاء الاصطناعي: ربط كل عملية AI بنموذج إنتاجي وقالب تعليمات وحدود الاستقلالية لكل مستأجر

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DISCARDED؛ الحدث EVT-RTG-DISCARDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI governance authority (draft, edit) · second authority (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RTG-DISCARD` · `AGG-AI-ROUTING` · متطلبات: REQ-AI-008, REQ-AI-011 · حالات استخدام: UC-074, UC-077
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RTG-DISCARD succeeds
  Given AGG-AI-ROUTING in state DRAFT and every guard holds
  When AI governance authority sends CMD-RTG-DISCARD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISCARDED
  And EVT-RTG-DISCARDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RTG-DISCARD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_ROUTING_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISCARDED, SUPERSEDED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RTG-DISCARD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-RTG-DRAFT — إعداد مسودة توجيه الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | AI governance authority | `POST /api/v1/ai/routings` | POL-RTG-DRAFT |

**القصة:** بصفتي **AI governance authority**، أريد **إعداد مسودة توجيه الذكاء الاصطناعي**، لكي يتحقق غرض توجيه الذكاء الاصطناعي: ربط كل عملية AI بنموذج إنتاجي وقالب تعليمات وحدود الاستقلالية لكل مستأجر

- **الشروط المسبقة:** الحالة الحالية: ∅؛ AI governance authority; ≤ 1 DRAFT per tenant
- **المدخلات:** `based_on`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-RTG-DRAFTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI governance authority (draft, edit) · second authority (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RTG-DRAFT` · `AGG-AI-ROUTING` · متطلبات: REQ-AI-008, REQ-AI-011 · حالات استخدام: UC-074, UC-077
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RTG-DRAFT succeeds
  Given AGG-AI-ROUTING does not exist yet and every guard holds
  When AI governance authority sends CMD-RTG-DRAFT with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-RTG-DRAFTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RTG-DRAFT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RTG-DRAFT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | DRAFT_EXISTS | 422 | لم يتحقق الشرط: ≤ 1 DRAFT per tenant |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-RTG-EDIT — تعديل توجيه الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | حوكمة وأمن | AI governance authority | `POST /api/v1/ai/routings/{id}/actions/edit` | POL-RTG-EDIT |

**القصة:** بصفتي **AI governance authority**، أريد **تعديل توجيه الذكاء الاصطناعي**، لكي يتحقق غرض توجيه الذكاء الاصطناعي: ربط كل عملية AI بنموذج إنتاجي وقالب تعليمات وحدود الاستقلالية لكل مستأجر

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ for each operation: model version in PRODUCTION (or STAGED with canary share), prompt template version, allowed tools, max AIL ≤ autonomy matrix, external model allowed only for unclassified and only if tenant policy allows
- **المدخلات:** `routes`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-RTG-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI governance authority (draft, edit) · second authority (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RTG-EDIT` · `AGG-AI-ROUTING` · متطلبات: REQ-AI-008, REQ-AI-011 · حالات استخدام: UC-074, UC-077
- **ضوابط النوع والفئة:** C-UPD، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RTG-EDIT succeeds
  Given AGG-AI-ROUTING in state DRAFT and every guard holds
  When AI governance authority sends CMD-RTG-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-RTG-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RTG-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_ROUTING_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISCARDED, SUPERSEDED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RTG-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ROUTING_INVALID | 422 | لم يتحقق الشرط: for each operation: model version in PRODUCTION (or STAGED with canary share), prompt template version, allowed tools, max AIL ≤ autonomy matrix, external model allowed only for unclassified and only if tenant policy allows |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: routes |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-AI-ROUTING-01 — تلقائي: successor activated (توجيه الذكاء الاصطناعي)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ACTIVE | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «successor activated»، أريد نقل **توجيه الذكاء الاصطناعي** إلى SUPERSEDED، لكي يتحقق غرض توجيه الذكاء الاصطناعي: ربط كل عملية AI بنموذج إنتاجي وقالب تعليمات وحدود الاستقلالية لكل مستأجر

- **الشرط:** system
- **المخرجات:** الحدث EVT-RTG-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-AI-ROUTING` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-Q-RTG-ACTIVE — جلب: Active routing for the tenant

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | AI governance, Security Officer | `GET /api/v1/ai/routing` | POL-RTG-ACTIVE |

**القصة:** بصفتي **AI governance, Security Officer**، أريد **جلب Active routing for the tenant**، لكي يتحقق المتطلب: The system shall enforce the AI autonomy matrix, allowing at most AIL3 in R2 and forbidding AIL5

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Active routing for the tenant؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** AI governance, Security Officer؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-RTG-ACTIVE` · `AGG-AI-ROUTING` · متطلبات: REQ-AI-008
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-RTG-ACTIVE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-RTG-ACTIVE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-RTG-ACTIVE is denied
  Given the policy denies the caller
  When the caller sends QRY-RTG-ACTIVE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-AI-TOOL — أداة الذكاء الاصطناعي (AI Tool)

`03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md` · SLC-10 · الحالات: DRAFT, ACTIVE, DISABLED → RETIRED

#### US-BC07-TOL-ACTIVATE — تفعيل أداة الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Security Officer | `POST /api/v1/ai/tools/{id}/actions/activate` | POL-TOL-ACTIVATE |

**القصة:** بصفتي **Security Officer**، أريد **تفعيل أداة الذكاء الاصطناعي**، لكي يتحقق غرض أداة الذكاء الاصطناعي: أداة يمكن لتشغيل AI استدعاؤها، بصلاحية وأثر ومستوى استقلالية

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ security review passed (injection, exfiltration, scope); approver = Security Officer
- **المدخلات:** `review_ref`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-TOL-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register) · Security Officer (activate, disable)؛ الشروط: tenant match; object visible؛ فصل المهام: Security Officer؛ الالتزامات: audit
- **الربط:** `CMD-TOL-ACTIVATE` · `AGG-AI-TOOL` · متطلبات: REQ-AI-013, REQ-AI-012 · حالات استخدام: UC-071, UC-077
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TOL-ACTIVATE succeeds
  Given AGG-AI-TOOL in state DRAFT and every guard holds
  When Security Officer sends CMD-TOL-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-TOL-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TOL-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_TOOL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DISABLED, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TOL-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SECURITY_REVIEW_REQUIRED | 422 | لم يتحقق الشرط: security review passed (injection, exfiltration, scope); approver = Security Officer |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: review_ref |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-TOL-DISABLE — تعطيل أداة الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Security Officer | `POST /api/v1/ai/tools/{id}/actions/disable` | POL-TOL-DISABLE |

**القصة:** بصفتي **Security Officer**، أريد **تعطيل أداة الذكاء الاصطناعي**، لكي يتحقق غرض أداة الذكاء الاصطناعي: أداة يمكن لتشغيل AI استدعاؤها، بصلاحية وأثر ومستوى استقلالية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DISABLED؛ الحدث EVT-TOL-DISABLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register) · Security Officer (activate, disable)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TOL-DISABLE` · `AGG-AI-TOOL` · متطلبات: REQ-AI-013, REQ-AI-012 · حالات استخدام: UC-071, UC-077
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TOL-DISABLE succeeds
  Given AGG-AI-TOOL in state ACTIVE and every guard holds
  When Security Officer sends CMD-TOL-DISABLE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISABLED
  And EVT-TOL-DISABLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TOL-DISABLE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_TOOL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISABLED, DRAFT, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TOL-DISABLE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-TOL-ENABLE — تمكين أداة الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Security Officer (محسوم: `17-security-design.md` §5) | `POST /api/v1/ai/tools/{id}/actions/enable` | POL-TOL-ENABLE |

**القصة:** بصفتي **Security Officer**، أريد **تمكين أداة الذكاء الاصطناعي**، لكي يتحقق غرض أداة الذكاء الاصطناعي: أداة يمكن لتشغيل AI استدعاؤها، بصلاحية وأثر ومستوى استقلالية

- **الشروط المسبقة:** الحالة الحالية: DISABLED؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-TOL-ENABLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register) · Security Officer (activate, disable)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TOL-ENABLE` · `AGG-AI-TOOL` · متطلبات: REQ-AI-013, REQ-AI-012 · حالات استخدام: UC-071, UC-077
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TOL-ENABLE succeeds
  Given AGG-AI-TOOL in state DISABLED and every guard holds
  When Security Officer sends CMD-TOL-ENABLE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-TOL-ENABLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TOL-ENABLE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_TOOL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DRAFT, RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TOL-ENABLE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-TOL-REGISTER — تسجيل أداة الذكاء الاصطناعي

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | AI platform engineer | `POST /api/v1/ai/tools` | POL-TOL-REGISTER |

**القصة:** بصفتي **AI platform engineer**، أريد **تسجيل أداة الذكاء الاصطناعي**، لكي يتحقق غرض أداة الذكاء الاصطناعي: أداة يمكن لتشغيل AI استدعاؤها، بصلاحية وأثر ومستوى استقلالية

- **الشروط المسبقة:** الحالة الحالية: ∅؛ name; input JSON schema; underlying platform query or command; effect ∈ {read, propose}; required permission; max AIL
- **المدخلات:** `name`!: string, `description`!: LocalizedName, `input_schema`!: object, `binding`!: string, `effect`!: enum(read,propose), `permission`!: string, `max_ail`!: integer — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-TOL-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register) · Security Officer (activate, disable)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TOL-REGISTER` · `AGG-AI-TOOL` · متطلبات: REQ-AI-013, REQ-AI-012 · حالات استخدام: UC-071, UC-077
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TOL-REGISTER succeeds
  Given AGG-AI-TOOL does not exist yet and every guard holds
  When AI platform engineer sends CMD-TOL-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-TOL-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TOL-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TOL-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TOOL_INVALID | 422 | لم يتحقق الشرط: name; input JSON schema; underlying platform query or command; effect ∈ {read, propose}; required permission; max AIL |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: name, description, input_schema, binding, effect, permission, max_ail |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-TOL-RETIRE — إحالة أداة الذكاء الاصطناعي إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Security Officer (محسوم: `17-security-design.md` §5) | `POST /api/v1/ai/tools/{id}/actions/retire` | POL-TOL-RETIRE |

**القصة:** بصفتي **Security Officer**، أريد **إحالة أداة الذكاء الاصطناعي إلى التقاعد**، لكي يتحقق غرض أداة الذكاء الاصطناعي: أداة يمكن لتشغيل AI استدعاؤها، بصلاحية وأثر ومستوى استقلالية

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE, DISABLED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-TOL-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register) · Security Officer (activate, disable)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TOL-RETIRE` · `AGG-AI-TOOL` · متطلبات: REQ-AI-013, REQ-AI-012 · حالات استخدام: UC-071, UC-077
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TOL-RETIRE succeeds
  Given AGG-AI-TOOL in state DRAFT or ACTIVE or DISABLED and every guard holds
  When Security Officer sends CMD-TOL-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-TOL-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TOL-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AI_TOOL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TOL-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-Q-TOL-LIST — جلب: Tool registry

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | AI governance, Security Officer | `GET /api/v1/ai/tools` | POL-TOL-LIST |

**القصة:** بصفتي **AI governance, Security Officer**، أريد **جلب Tool registry**، لكي يتحقق المتطلب: The system shall register every tool available to AI runs, with the permission it requires and its autonomy level

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Tool registry؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** AI governance, Security Officer؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-TOL-LIST` · `AGG-AI-TOOL` · متطلبات: REQ-AI-013
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-TOL-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-TOL-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-TOL-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-TOL-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-EVAL-SUITE — حزمة التقييم (Evaluation Suite)

`03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md` · SLC-10 · الحالات: DRAFT, ACTIVE → SUPERSEDED

#### US-BC07-EVS-ACTIVATE — تفعيل حزمة التقييم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | second authority | `POST /api/v1/ai/evaluation-suites/{id}/actions/activate` | POL-EVS-ACTIVATE |

**القصة:** بصفتي **second authority**، أريد **تفعيل حزمة التقييم**، لكي يتحقق غرض حزمة التقييم: مجموعات تقييم مُصدرة: تأريض، استشهاد، أدلة غير كافية، حقن، تسريب، عربي/إنجليزي

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ approver ≠ author; previous ACTIVE → SUPERSEDED
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-EVS-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI governance (draft, edit) · second authority (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: approver ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-EVS-ACTIVATE` · `AGG-EVAL-SUITE` · متطلبات: REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVS-ACTIVATE succeeds
  Given AGG-EVAL-SUITE in state DRAFT and every guard holds
  When second authority sends CMD-EVS-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-EVS-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVS-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVS-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVAL_SUITE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-EVS-DRAFT — إعداد مسودة حزمة التقييم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | AI governance | `POST /api/v1/ai/evaluation-suites` | POL-EVS-DRAFT |

**القصة:** بصفتي **AI governance**، أريد **إعداد مسودة حزمة التقييم**، لكي يتحقق غرض حزمة التقييم: مجموعات تقييم مُصدرة: تأريض، استشهاد، أدلة غير كافية، حقن، تسريب، عربي/إنجليزي

- **الشروط المسبقة:** الحالة الحالية: ∅؛ AI governance
- **المدخلات:** `based_on`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-EVS-DRAFTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI governance (draft, edit) · second authority (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EVS-DRAFT` · `AGG-EVAL-SUITE` · متطلبات: REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVS-DRAFT succeeds
  Given AGG-EVAL-SUITE does not exist yet and every guard holds
  When AI governance sends CMD-EVS-DRAFT with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-EVS-DRAFTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVS-DRAFT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVS-DRAFT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-EVS-EDIT — تعديل حزمة التقييم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | حوكمة وأمن | AI governance | `POST /api/v1/ai/evaluation-suites/{id}/actions/edit` | POL-EVS-EDIT |

**القصة:** بصفتي **AI governance**، أريد **تعديل حزمة التقييم**، لكي يتحقق غرض حزمة التقييم: مجموعات تقييم مُصدرة: تأريض، استشهاد، أدلة غير كافية، حقن، تسريب، عربي/إنجليزي

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ sets: groundedness (≥ 500 items), citation, insufficient-evidence, prompt-injection, exfiltration, cross-tenant, Arabic/English/mixed; each item labelled with expected behaviour
- **المدخلات:** `sets`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-EVS-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI governance (draft, edit) · second authority (activate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EVS-EDIT` · `AGG-EVAL-SUITE` · متطلبات: REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-UPD، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EVS-EDIT succeeds
  Given AGG-EVAL-SUITE in state DRAFT and every guard holds
  When AI governance sends CMD-EVS-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-EVS-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EVS-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EVS-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVAL_SUITE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SUITE_INVALID | 422 | لم يتحقق الشرط: sets: groundedness (≥ 500 items), citation, insufficient-evidence, prompt-injection, exfiltration, cross-tenant, Arabic/English/mixed; each item labelled with expected behaviour |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: sets |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-EVAL-SUITE-01 — تلقائي: successor activated (حزمة التقييم)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ACTIVE | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «successor activated»، أريد نقل **حزمة التقييم** إلى SUPERSEDED، لكي يتحقق غرض حزمة التقييم: مجموعات تقييم مُصدرة: تأريض، استشهاد، أدلة غير كافية، حقن، تسريب، عربي/إنجليزي

- **الشرط:** system
- **المخرجات:** الحدث EVT-EVS-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-EVAL-SUITE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

### AGG-INTEGRATION-CONNECTION — اتصال التكامل (Integration Connection)

`03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md` · SLC-16 · الحالات: DRAFT, TESTING, ACTIVE, DEGRADED, SUSPENDED → RETIRED

#### US-BC07-CON-ACTIVATE — تفعيل اتصال التكامل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | Security Officer ≠ requester | `POST /api/v1/integration/connections/{id}/actions/activate` | POL-CON-ACTIVATE |

**القصة:** بصفتي **Security Officer ≠ requester**، أريد **تفعيل اتصال التكامل**، لكي يتحقق غرض اتصال التكامل: اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)

- **الشروط المسبقة:** الحالة الحالية: TESTING؛ probe passed; egress allow-list entry approved by Security Officer ≠ requester (GOV-005)
- **المدخلات:** `allow_list_entry`!: object — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-CON-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)؛ الشروط: tenant match؛ فصل المهام: Security Officer ≠ requester؛ الالتزامات: audit; mfa
- **الربط:** `CMD-CON-ACTIVATE` · `AGG-INTEGRATION-CONNECTION` · متطلبات: REQ-INT-001 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CON-ACTIVATE succeeds
  Given AGG-INTEGRATION-CONNECTION in state TESTING and every guard holds
  When Security Officer ≠ requester sends CMD-CON-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-CON-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CON-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CON-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DEGRADED, DRAFT, RETIRED, SUSPENDED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: Security Officer ≠ requester |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: allow_list_entry |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-CON-FAIL-TEST — تسجيل فشل اختبار اتصال التكامل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | integration engineer | `POST /api/v1/integration/connections/{id}/actions/fail-test` | POL-CON-FAIL-TEST |

**القصة:** بصفتي **integration engineer**، أريد **تسجيل فشل اختبار اتصال التكامل**، لكي يتحقق غرض اتصال التكامل: اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)

- **الشروط المسبقة:** الحالة الحالية: TESTING؛ probe failed; errors recorded
- **المدخلات:** `errors`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-CON-TEST-FAILED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CON-FAIL-TEST` · `AGG-INTEGRATION-CONNECTION` · متطلبات: REQ-INT-001 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CON-FAIL-TEST succeeds
  Given AGG-INTEGRATION-CONNECTION in state TESTING and every guard holds
  When integration engineer sends CMD-CON-FAIL-TEST with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DRAFT
  And EVT-CON-TEST-FAILED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CON-FAIL-TEST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CON-FAIL-TEST ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DEGRADED, DRAFT, RETIRED, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: errors |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-CON-REGISTER — تسجيل اتصال التكامل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تكامل | integration engineer | `POST /api/v1/integration/connections` | POL-CON-REGISTER |

**القصة:** بصفتي **integration engineer**، أريد **تسجيل اتصال التكامل**، لكي يتحقق غرض اتصال التكامل: اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)

- **الشروط المسبقة:** الحالة الحالية: ∅؛ system kind ∈ {erp, hris, dms, cmms, sensor_gateway, cap_endpoint}; endpoint on an internal network; protocol; direction ∈ {inbound, outbound}, outbound only for cap_endpoint in R2 (INV-CON-02); credentials stored in OpenBao (reference only)
- **المدخلات:** `name`!: string, `system_kind`!: enum(erp,hris,dms,cmms,sensor_gateway,cap_endpoint), `endpoint`!: string, `protocol`!: string, `direction`!: enum(inbound,outbound), `credentials_ref`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-CON-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CON-REGISTER` · `AGG-INTEGRATION-CONNECTION` · متطلبات: REQ-INT-001 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-CRE، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CON-REGISTER succeeds
  Given AGG-INTEGRATION-CONNECTION does not exist yet and every guard holds
  When integration engineer sends CMD-CON-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-CON-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CON-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CON-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONNECTION_INVALID | 422 | لم يتحقق الشرط: system kind ∈ {erp, hris, dms, cmms, sensor_gateway, cap_endpoint}; endpoint on an internal network; protocol; direction ∈ {inbound, outbound}, outbound only for cap_endpoint in R2 (INV-CON-02); credentials stored in OpenBao (reference only) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: name, system_kind, endpoint, protocol, direction, credentials_ref |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-CON-RESUME — استئناف اتصال التكامل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | Administrator | `POST /api/v1/integration/connections/{id}/actions/resume` | POL-CON-RESUME |

**القصة:** بصفتي **Administrator**، أريد **استئناف اتصال التكامل**، لكي يتحقق غرض اتصال التكامل: اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)

- **الشروط المسبقة:** الحالة الحالية: SUSPENDED؛ egress rule re-enabled after re-check
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-CON-RESUMED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CON-RESUME` · `AGG-INTEGRATION-CONNECTION` · متطلبات: REQ-INT-001 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CON-RESUME succeeds
  Given AGG-INTEGRATION-CONNECTION in state SUSPENDED and every guard holds
  When Administrator sends CMD-CON-RESUME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-CON-RESUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CON-RESUME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CON-RESUME ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DEGRADED, DRAFT, RETIRED, TESTING |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-CON-RETIRE — إحالة اتصال التكامل إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | Administrator | `POST /api/v1/integration/connections/{id}/actions/retire` | POL-CON-RETIRE |

**القصة:** بصفتي **Administrator**، أريد **إحالة اتصال التكامل إلى التقاعد**، لكي يتحقق غرض اتصال التكامل: اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)

- **الشروط المسبقة:** الحالة الحالية: DRAFT, SUSPENDED؛ no ACTIVE adapter or stream bound; egress rule removed
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-CON-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CON-RETIRE` · `AGG-INTEGRATION-CONNECTION` · متطلبات: REQ-INT-001 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CON-RETIRE succeeds
  Given AGG-INTEGRATION-CONNECTION in state DRAFT or SUSPENDED and every guard holds
  When Administrator sends CMD-CON-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-CON-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CON-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CON-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONNECTION_IN_USE | 422 | لم يتحقق الشرط: no ACTIVE adapter or stream bound; egress rule removed |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DEGRADED, RETIRED, TESTING |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-CON-SUSPEND — تعليق اتصال التكامل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | Administrator | `POST /api/v1/integration/connections/{id}/actions/suspend` | POL-CON-SUSPEND |

**القصة:** بصفتي **Administrator**، أريد **تعليق اتصال التكامل**، لكي يتحقق غرض اتصال التكامل: اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, DEGRADED؛ reason; egress rule disabled
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SUSPENDED؛ الحدث EVT-CON-SUSPENDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CON-SUSPEND` · `AGG-INTEGRATION-CONNECTION` · متطلبات: REQ-INT-001 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CON-SUSPEND succeeds
  Given AGG-INTEGRATION-CONNECTION in state ACTIVE or DEGRADED and every guard holds
  When Administrator sends CMD-CON-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUSPENDED
  And EVT-CON-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CON-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CON-SUSPEND ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DRAFT, RETIRED, SUSPENDED, TESTING |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-CON-TEST — اختبار اتصال التكامل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | integration engineer | `POST /api/v1/integration/connections/{id}/actions/test` | POL-CON-TEST |

**القصة:** بصفتي **integration engineer**، أريد **اختبار اتصال التكامل**، لكي يتحقق غرض اتصال التكامل: اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ integration engineer; connectivity and schema probe run
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← TESTING؛ الحدث EVT-CON-TEST-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CON-TEST` · `AGG-INTEGRATION-CONNECTION` · متطلبات: REQ-INT-001 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CON-TEST succeeds
  Given AGG-INTEGRATION-CONNECTION in state DRAFT and every guard holds
  When integration engineer sends CMD-CON-TEST with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes TESTING
  And EVT-CON-TEST-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CON-TEST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CON-TEST ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DEGRADED, RETIRED, SUSPENDED, TESTING |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-INTEGRATION-CONNECTION-01 — تلقائي: health checks failing 5 min (اتصال التكامل)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | ACTIVE | DEGRADED |

**القصة:** بصفتي **النظام**، عند «health checks failing 5 min»، أريد نقل **اتصال التكامل** إلى DEGRADED، لكي يتحقق غرض اتصال التكامل: اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)

- **الشرط:** backlog buffered by adapters (QAS-INT-001)
- **المخرجات:** الحدث EVT-CON-DEGRADED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-INTEGRATION-CONNECTION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-INTEGRATION-CONNECTION-02 — تلقائي: health restored (اتصال التكامل)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | DEGRADED | ACTIVE |

**القصة:** بصفتي **النظام**، عند «health restored»، أريد نقل **اتصال التكامل** إلى ACTIVE، لكي يتحقق غرض اتصال التكامل: اتصال بنظام خارجي داخل حدود المؤسسة (ERP، HRIS، DMS، CMMS، بوابة حساسات، نقطة CAP)

- **الشرط:** backlog replayed
- **المخرجات:** الحدث EVT-CON-RECOVERED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-INTEGRATION-CONNECTION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-Q-CON-LIST — جلب: Connections with state, health, allow-list entry

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | integration engineers, Security Officer | `GET /api/v1/integration/connections` | POL-CON-LIST |

**القصة:** بصفتي **integration engineers, Security Officer**، أريد **جلب Connections with state, health, allow-list entry**، لكي يتحقق المتطلب: The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims, persons and documents without making external systems sources of truth

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Connections with state, health, allow-list entry؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** integration engineers, Security Officer؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CON-LIST` · `AGG-INTEGRATION-CONNECTION` · متطلبات: REQ-INT-001
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-CON-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CON-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CON-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-CON-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-MODEL-VERSION — إصدار النموذج (Model Version)

`03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md` · SLC-10 · الحالات: REGISTERED, EVALUATING, APPROVED, STAGED, PRODUCTION, DEPRECATED → EVALUATION_FAILED, RETIRED

#### US-BC07-MDL-APPROVE — اعتماد إصدار النموذج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | AI governance authority | `POST /api/v1/ai/models/{id}/actions/approve` | POL-MDL-APPROVE |

**القصة:** بصفتي **AI governance authority**، أريد **اعتماد إصدار النموذج**، لكي يتحقق غرض إصدار النموذج: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)

- **الشروط المسبقة:** الحالة الحالية: EVALUATING؛ report meets thresholds: citation accuracy ≥ 95 %, hallucination ≤ 2 %, insufficient-evidence recall ≥ 95 %, 0 injection/exfiltration successes, latency and cost recorded (REQ-AI-010); AI governance authority ≠ registrar
- **المدخلات:** `report`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← APPROVED؛ الحدث EVT-MDL-APPROVED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)؛ الشروط: tenant match; object visible؛ فصل المهام: approver ≠ registrar؛ الالتزامات: audit
- **الربط:** `CMD-MDL-APPROVE` · `AGG-MODEL-VERSION` · متطلبات: REQ-AI-009, REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MDL-APPROVE succeeds
  Given AGG-MODEL-VERSION in state EVALUATING and every guard holds
  When AI governance authority sends CMD-MDL-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes APPROVED
  And EVT-MDL-APPROVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MDL-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MDL-APPROVE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVALUATION_BELOW_THRESHOLD | 422 | لم يتحقق الشرط: report meets thresholds: citation accuracy ≥ 95 %, hallucination ≤ 2 %, insufficient-evidence recall ≥ 95 %, 0 injection/exfiltration successes, latency and cost recorded (REQ-AI-010) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MODEL_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, DEPRECATED, EVALUATION_FAILED, PRODUCTION, REGISTERED, RETIRED, STAGED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: report |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-MDL-DEPRECATE — إهمال إصدار النموذج (إيقاف الاستخدام الجديد)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | AI platform engineer | `POST /api/v1/ai/models/{id}/actions/deprecate` | POL-MDL-DEPRECATE |

**القصة:** بصفتي **AI platform engineer**، أريد **إهمال إصدار النموذج (إيقاف الاستخدام الجديد)**، لكي يتحقق غرض إصدار النموذج: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)

- **الشروط المسبقة:** الحالة الحالية: PRODUCTION, STAGED, APPROVED؛ reason; routes using it must be switched first
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DEPRECATED؛ الحدث EVT-MDL-DEPRECATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MDL-DEPRECATE` · `AGG-MODEL-VERSION` · متطلبات: REQ-AI-009, REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MDL-DEPRECATE succeeds
  Given AGG-MODEL-VERSION in state PRODUCTION or STAGED or APPROVED and every guard holds
  When AI platform engineer sends CMD-MDL-DEPRECATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DEPRECATED
  And EVT-MDL-DEPRECATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MDL-DEPRECATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MDL-DEPRECATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MODEL_IN_ACTIVE_ROUTE | 422 | لم يتحقق الشرط: routes using it must be switched first |
    | MODEL_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DEPRECATED, EVALUATING, EVALUATION_FAILED, REGISTERED, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-MDL-FAIL-EVALUATION — تسجيل فشل تقييم إصدار النموذج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | AI platform engineer | `POST /api/v1/ai/models/{id}/actions/fail-evaluation` | POL-MDL-FAIL-EVALUATION |

**القصة:** بصفتي **AI platform engineer**، أريد **تسجيل فشل تقييم إصدار النموذج**، لكي يتحقق غرض إصدار النموذج: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)

- **الشروط المسبقة:** الحالة الحالية: EVALUATING؛ report attached
- **المدخلات:** `report`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← EVALUATION_FAILED؛ الحدث EVT-MDL-EVALUATION-FAILED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MDL-FAIL-EVALUATION` · `AGG-MODEL-VERSION` · متطلبات: REQ-AI-009, REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MDL-FAIL-EVALUATION succeeds
  Given AGG-MODEL-VERSION in state EVALUATING and every guard holds
  When AI platform engineer sends CMD-MDL-FAIL-EVALUATION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes EVALUATION_FAILED
  And EVT-MDL-EVALUATION-FAILED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MDL-FAIL-EVALUATION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MDL-FAIL-EVALUATION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MODEL_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, DEPRECATED, EVALUATION_FAILED, PRODUCTION, REGISTERED, RETIRED, STAGED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: report |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-MDL-PROMOTE — ترقية إصدار النموذج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | AI governance authority | `POST /api/v1/ai/models/{id}/actions/promote` | POL-MDL-PROMOTE |

**القصة:** بصفتي **AI governance authority**، أريد **ترقية إصدار النموذج**، لكي يتحقق غرض إصدار النموذج: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)

- **الشروط المسبقة:** الحالة الحالية: STAGED؛ canary metrics within thresholds for ≥ 7 days; approver ≠ stager
- **المدخلات:** `canary_report`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PRODUCTION؛ الحدث EVT-MDL-PROMOTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)؛ الشروط: tenant match; object visible؛ فصل المهام: approver ≠ stager؛ الالتزامات: audit
- **الربط:** `CMD-MDL-PROMOTE` · `AGG-MODEL-VERSION` · متطلبات: REQ-AI-009, REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MDL-PROMOTE succeeds
  Given AGG-MODEL-VERSION in state STAGED and every guard holds
  When AI governance authority sends CMD-MDL-PROMOTE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PRODUCTION
  And EVT-MDL-PROMOTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MDL-PROMOTE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MDL-PROMOTE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CANARY_BELOW_THRESHOLD | 422 | لم يتحقق الشرط: canary metrics within thresholds for ≥ 7 days |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MODEL_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, DEPRECATED, EVALUATING, EVALUATION_FAILED, PRODUCTION, REGISTERED, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: canary_report |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-MDL-REGISTER — تسجيل إصدار النموذج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | AI platform engineer | `POST /api/v1/ai/models` | POL-MDL-REGISTER |

**القصة:** بصفتي **AI platform engineer**، أريد **تسجيل إصدار النموذج**، لكي يتحقق غرض إصدار النموذج: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)

- **الشروط المسبقة:** الحالة الحالية: ∅؛ family, version, weights digest in internal registry, licence reviewed, languages (must include ar and en for generative roles), context size, hosting ∈ {local, external_allowed}
- **المدخلات:** `family`!: string, `version`!: string, `weights_digest`!: string, `licence`!: string, `languages`!: array, `context_tokens`!: integer, `hosting`!: enum(local,external_allowed), `roles`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← REGISTERED؛ الحدث EVT-MDL-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MDL-REGISTER` · `AGG-MODEL-VERSION` · متطلبات: REQ-AI-009, REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MDL-REGISTER succeeds
  Given AGG-MODEL-VERSION does not exist yet and every guard holds
  When AI platform engineer sends CMD-MDL-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes REGISTERED
  And EVT-MDL-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MDL-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MDL-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MODEL_INVALID | 422 | لم يتحقق الشرط: family, version, weights digest in internal registry, licence reviewed, languages (must include ar and en for generative roles), context size, hosting ∈ {local, external_allowed} |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: family, version, weights_digest, licence, languages, context_tokens, hosting, roles |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-MDL-REINSTATE — إعادة إصدار النموذج إلى السريان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | AI governance authority | `POST /api/v1/ai/models/{id}/actions/reinstate` | POL-MDL-REINSTATE |

**القصة:** بصفتي **AI governance authority**، أريد **إعادة إصدار النموذج إلى السريان**، لكي يتحقق غرض إصدار النموذج: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)

- **الشروط المسبقة:** الحالة الحالية: DEPRECATED؛ rollback; evaluation ≤ 90 days old
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PRODUCTION؛ الحدث EVT-MDL-REINSTATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MDL-REINSTATE` · `AGG-MODEL-VERSION` · متطلبات: REQ-AI-009, REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MDL-REINSTATE succeeds
  Given AGG-MODEL-VERSION in state DEPRECATED and every guard holds
  When AI governance authority sends CMD-MDL-REINSTATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PRODUCTION
  And EVT-MDL-REINSTATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MDL-REINSTATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MDL-REINSTATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVALUATION_TOO_OLD | 422 | لم يتحقق الشرط: evaluation ≤ 90 days old |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MODEL_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, EVALUATING, EVALUATION_FAILED, PRODUCTION, REGISTERED, RETIRED, STAGED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-MDL-RETIRE — إحالة إصدار النموذج إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | AI governance authority (محسوم: `17-security-design.md` §5) | `POST /api/v1/ai/models/{id}/actions/retire` | POL-MDL-RETIRE |

**القصة:** بصفتي **AI governance authority**، أريد **إحالة إصدار النموذج إلى التقاعد**، لكي يتحقق غرض إصدار النموذج: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)

- **الشروط المسبقة:** الحالة الحالية: DEPRECATED؛ weights archived (cold) if referenced by lineage of accepted results; record kept
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-MDL-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MDL-RETIRE` · `AGG-MODEL-VERSION` · متطلبات: REQ-AI-009, REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MDL-RETIRE succeeds
  Given AGG-MODEL-VERSION in state DEPRECATED and every guard holds
  When AI governance authority sends CMD-MDL-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-MDL-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MDL-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MDL-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MODEL_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, EVALUATING, EVALUATION_FAILED, PRODUCTION, REGISTERED, RETIRED, STAGED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-MDL-STAGE — تجهيز إصدار النموذج للإنتاج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | AI platform engineer | `POST /api/v1/ai/models/{id}/actions/stage` | POL-MDL-STAGE |

**القصة:** بصفتي **AI platform engineer**، أريد **تجهيز إصدار النموذج للإنتاج**، لكي يتحقق غرض إصدار النموذج: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)

- **الشروط المسبقة:** الحالة الحالية: APPROVED؛ canary share ≤ 10 % of the target operations
- **المدخلات:** `canary_share`!: number, `operations`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← STAGED؛ الحدث EVT-MDL-STAGED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MDL-STAGE` · `AGG-MODEL-VERSION` · متطلبات: REQ-AI-009, REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MDL-STAGE succeeds
  Given AGG-MODEL-VERSION in state APPROVED and every guard holds
  When AI platform engineer sends CMD-MDL-STAGE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes STAGED
  And EVT-MDL-STAGED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MDL-STAGE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MDL-STAGE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MODEL_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DEPRECATED, EVALUATING, EVALUATION_FAILED, PRODUCTION, REGISTERED, RETIRED, STAGED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: canary_share, operations |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-MDL-START-EVALUATION — بدء تقييم إصدار النموذج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | AI platform engineer | `POST /api/v1/ai/models/{id}/actions/start-evaluation` | POL-MDL-START-EVALUATION |

**القصة:** بصفتي **AI platform engineer**، أريد **بدء تقييم إصدار النموذج**، لكي يتحقق غرض إصدار النموذج: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)

- **الشروط المسبقة:** الحالة الحالية: REGISTERED؛ evaluation suite ACTIVE (AGG-EVAL-SUITE)
- **المدخلات:** `suite`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← EVALUATING؛ الحدث EVT-MDL-EVALUATION-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)؛ الشروط: tenant match; object visible؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MDL-START-EVALUATION` · `AGG-MODEL-VERSION` · متطلبات: REQ-AI-009, REQ-AI-010 · حالات استخدام: UC-075, UC-076
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MDL-START-EVALUATION succeeds
  Given AGG-MODEL-VERSION in state REGISTERED and every guard holds
  When AI platform engineer sends CMD-MDL-START-EVALUATION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes EVALUATING
  And EVT-MDL-EVALUATION-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MDL-START-EVALUATION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MDL-START-EVALUATION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MODEL_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, DEPRECATED, EVALUATING, EVALUATION_FAILED, PRODUCTION, RETIRED, STAGED |
    | SUITE_NOT_ACTIVE | 422 | لم يتحقق الشرط: evaluation suite ACTIVE (AGG-EVAL-SUITE) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: suite |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-MODEL-VERSION-01 — تلقائي: monitoring drift detected (إصدار النموذج)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | PRODUCTION | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «monitoring drift detected»، أريد تحديث **إصدار النموذج** دون تغيير حالته، لكي يتحقق غرض إصدار النموذج: نسخة نموذج بدورة حياة من التسجيل حتى التقاعد (PRJ§30)

- **الشرط:** weekly evaluation sample below threshold → alert, route review
- **المخرجات:** الحدث EVT-MDL-DRIFT-DETECTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-MODEL-VERSION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-Q-MDL-LIST — جلب: Model versions with state, evaluation summary, hosting

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | AI governance, Auditor | `GET /api/v1/ai/models` | POL-MDL-LIST |

**القصة:** بصفتي **AI governance, Auditor**، أريد **جلب Model versions with state, evaluation summary, hosting**، لكي يتحقق المتطلب: The system shall manage models through the lifecycle REGISTERED, EVALUATING, APPROVED, STAGED, PRODUCTION, MONITORED, DEPRECATED, RETIRED

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Model versions with state, evaluation summary, hosting؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** AI governance, Auditor؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-MDL-LIST` · `AGG-MODEL-VERSION` · متطلبات: REQ-AI-009
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-MDL-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-MDL-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-MDL-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-MDL-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-PRELOAD-PACKAGE — حزمة التحميل المسبق (Preload Package)

`03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md` · SLC-11 · الحالات: REQUESTED, BUILDING, READY, DOWNLOADED → EXPIRED, REVOKED

#### US-BC07-PKG-CONFIRM-DOWNLOAD — تأكيد تنزيل حزمة التحميل المسبق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | field user | `POST /api/v1/field/preload-packages/{id}/actions/confirm-download` | POL-PKG-CONFIRM-DOWNLOAD |

**القصة:** بصفتي **field user**، أريد **تأكيد تنزيل حزمة التحميل المسبق**، لكي يتحقق غرض حزمة التحميل المسبق: حزمة بيانات منطقة عمل للاستخدام دون اتصال، مفلترة بصلاحية المستخدم وقت البناء

- **الشروط المسبقة:** الحالة الحالية: READY؛ device acknowledges manifest hash
- **المدخلات:** `manifest_sha256`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DOWNLOADED؛ الحدث EVT-PKG-DOWNLOADED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PKG-CONFIRM-DOWNLOAD` · `AGG-PRELOAD-PACKAGE` · متطلبات: REQ-OFF-002, REQ-OFF-005 · حالات استخدام: UC-090, UC-093
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PKG-CONFIRM-DOWNLOAD succeeds
  Given AGG-PRELOAD-PACKAGE in state READY and every guard holds
  When field user sends CMD-PKG-CONFIRM-DOWNLOAD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DOWNLOADED
  And EVT-PKG-DOWNLOADED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PKG-CONFIRM-DOWNLOAD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PKG-CONFIRM-DOWNLOAD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MANIFEST_MISMATCH | 422 | لم يتحقق الشرط: device acknowledges manifest hash |
    | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: BUILDING, DOWNLOADED, EXPIRED, REQUESTED, REVOKED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: manifest_sha256 |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-PKG-REQUEST — طلب حزمة التحميل المسبق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تكامل | field user | `POST /api/v1/field/preload-packages` | POL-PKG-REQUEST |

**القصة:** بصفتي **field user**، أريد **طلب حزمة التحميل المسبق**، لكي يتحقق غرض حزمة التحميل المسبق: حزمة بيانات منطقة عمل للاستخدام دون اتصال، مفلترة بصلاحية المستخدم وقت البناء

- **الشروط المسبقة:** الحالة الحالية: ∅؛ device ACTIVE; area polygon ≤ tenant max area; layers; time window; requested level ≤ tenant offline max level (default INTERNAL, POL-OFFLINE-PRELOAD)
- **المدخلات:** `device`!: urn, `area`!: object, `layers`!: array, `window`!: Interval, `level`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← REQUESTED؛ الحدث EVT-PKG-REQUESTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PKG-REQUEST` · `AGG-PRELOAD-PACKAGE` · متطلبات: REQ-OFF-002, REQ-OFF-005 · حالات استخدام: UC-090, UC-093
- **ضوابط النوع والفئة:** C-CRE، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PKG-REQUEST succeeds
  Given AGG-PRELOAD-PACKAGE does not exist yet and every guard holds
  When field user sends CMD-PKG-REQUEST with a valid payload, a new Idempotency-Key
  Then the state becomes REQUESTED
  And EVT-PKG-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PKG-REQUEST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PKG-REQUEST ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRELOAD_NOT_ALLOWED | 422 | لم يتحقق الشرط: requested level ≤ tenant offline max level (default INTERNAL, POL-OFFLINE-PRELOAD) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: device, area, layers, window, level |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-PKG-REVOKE — سحب حزمة التحميل المسبق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | field user · Administrator / Security Officer | `POST /api/v1/field/preload-packages/{id}/actions/revoke` | POL-PKG-REVOKE |

**القصة:** بصفتي **field user · Administrator / Security Officer**، أريد **سحب حزمة التحميل المسبق**، لكي يتحقق غرض حزمة التحميل المسبق: حزمة بيانات منطقة عمل للاستخدام دون اتصال، مفلترة بصلاحية المستخدم وقت البناء

- **الشروط المسبقة:** الحالة الحالية: REQUESTED, BUILDING, READY, DOWNLOADED؛ user, Administrator or Security Officer; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← REVOKED؛ الحدث EVT-PKG-REVOKED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PKG-REVOKE` · `AGG-PRELOAD-PACKAGE` · متطلبات: REQ-OFF-002, REQ-OFF-005 · حالات استخدام: UC-090, UC-093
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PKG-REVOKE succeeds
  Given AGG-PRELOAD-PACKAGE in state REQUESTED or BUILDING or READY or DOWNLOADED and every guard holds
  When an authorized actor (field user or Administrator / Security Officer) sends CMD-PKG-REVOKE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REVOKED
  And EVT-PKG-REVOKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PKG-REVOKE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PKG-REVOKE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, REVOKED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-PRELOAD-PACKAGE-01 — تلقائي: build started (حزمة التحميل المسبق)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | REQUESTED | BUILDING |

**القصة:** بصفتي **النظام**، عند «build started»، أريد نقل **حزمة التحميل المسبق** إلى BUILDING، لكي يتحقق غرض حزمة التحميل المسبق: حزمة بيانات منطقة عمل للاستخدام دون اتصال، مفلترة بصلاحية المستخدم وقت البناء

- **الشرط:** worker
- **المخرجات:** الحدث EVT-PKG-BUILDING؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PRELOAD-PACKAGE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-PRELOAD-PACKAGE-02 — تلقائي: build finished (حزمة التحميل المسبق)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | BUILDING | READY |

**القصة:** بصفتي **النظام**، عند «build finished»، أريد نقل **حزمة التحميل المسبق** إلى READY، لكي يتحقق غرض حزمة التحميل المسبق: حزمة بيانات منطقة عمل للاستخدام دون اتصال، مفلترة بصلاحية المستخدم وقت البناء

- **الشرط:** content = objects visible to the user at build time and ≤ requested level; manifest with hashes, labels, security_version, expires_at (≤ 72 h R1)
- **المخرجات:** الحدث EVT-PKG-READY؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PRELOAD-PACKAGE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-PRELOAD-PACKAGE-03 — تلقائي: expires_at reached (حزمة التحميل المسبق)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | READY, DOWNLOADED | EXPIRED |

**القصة:** بصفتي **النظام**، عند «expires_at reached»، أريد نقل **حزمة التحميل المسبق** إلى EXPIRED، لكي يتحقق غرض حزمة التحميل المسبق: حزمة بيانات منطقة عمل للاستخدام دون اتصال، مفلترة بصلاحية المستخدم وقت البناء

- **الشرط:** device purges at expiry (local enforcement) and confirms on next contact
- **المخرجات:** الحدث EVT-PKG-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PRELOAD-PACKAGE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-PRELOAD-PACKAGE-04 — تلقائي: user security_version changed or device not ACTIVE (حزمة التحميل المسبق)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | REQUESTED, BUILDING, READY, DOWNLOADED | REVOKED |

**القصة:** بصفتي **النظام**، عند «user security_version changed or device not ACTIVE»، أريد نقل **حزمة التحميل المسبق** إلى REVOKED، لكي يتحقق غرض حزمة التحميل المسبق: حزمة بيانات منطقة عمل للاستخدام دون اتصال، مفلترة بصلاحية المستخدم وقت البناء

- **الشرط:** purge instruction on next contact
- **المخرجات:** الحدث EVT-PKG-REVOKED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PRELOAD-PACKAGE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-Q-PKG-GET — جلب: Package manifest and download target (signed, ≤ 5 min)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | package owner device + user | `GET /api/v1/field/preload-packages/{package_id}` | POL-PKG-GET |

**القصة:** بصفتي **package owner device + user**، أريد **جلب Package manifest and download target (signed, ≤ 5 min)**، لكي يتحقق المتطلب: The system shall let field users preload authorized area-of-interest data, which shall respect the user's authorization at download time and expire according to tenant policy

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Package manifest and download target (signed, ≤ 5 min)
- **الصلاحية:** package owner device + user؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-PKG-GET` · `AGG-PRELOAD-PACKAGE` · متطلبات: REQ-OFF-002
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-PKG-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-PKG-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-PKG-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-PKG-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-PROJECTION-VERSION — إصدار الإسقاط (Projection Version)

`03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md` · SLC-05 · الحالات: BUILDING, READY, ACTIVE, DEGRADED → FAILED, RETIRED

#### US-BC07-PRJ-CANCEL-BUILD — إلغاء بناء إصدار الإسقاط

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Platform Operator (platform tenant) | `POST /api/v1/discovery/projection-versions/{id}/actions/cancel-build` | POL-PRJ-CANCEL-BUILD |

**القصة:** بصفتي **Platform Operator (platform tenant)**، أريد **إلغاء بناء إصدار الإسقاط**، لكي يتحقق غرض إصدار الإسقاط: إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green

- **الشروط المسبقة:** الحالة الحالية: BUILDING؛ operator; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← FAILED؛ الحدث EVT-PRJ-FAILED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Platform Operator (platform tenant)؛ الشروط: —؛ فصل المهام: —؛ الالتزامات: audit; mfa for PROMOTE
- **الربط:** `CMD-PRJ-CANCEL-BUILD` · `AGG-PROJECTION-VERSION` · متطلبات: REQ-SRC-004 · حالات استخدام: UC-078
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRJ-CANCEL-BUILD succeeds
  Given AGG-PROJECTION-VERSION in state BUILDING and every guard holds
  When Platform Operator sends CMD-PRJ-CANCEL-BUILD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes FAILED
  And EVT-PRJ-FAILED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRJ-CANCEL-BUILD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRJ-CANCEL-BUILD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PROJECTION_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DEGRADED, FAILED, READY, RETIRED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-PRJ-CREATE-VERSION — إنشاء إصدار جديد من إصدار الإسقاط

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Platform Operator (platform tenant) | `POST /api/v1/discovery/projection-versions` | POL-PRJ-CREATE-VERSION |

**القصة:** بصفتي **Platform Operator (platform tenant)**، أريد **إنشاء إصدار جديد من إصدار الإسقاط**، لكي يتحقق غرض إصدار الإسقاط: إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green

- **الشروط المسبقة:** الحالة الحالية: ∅؛ kind ∈ {search, graph, vector (R2, SLC-10)}; document schema version, embedding model version (vector), analyzer/normalization version and source checkpoint set; at most one BUILDING version per (tenant group, kind)
- **المدخلات:** `kind`!: enum(search,graph,vector), `tenant_group`!: string, `schema_version`!: integer, `normalization_version`!: integer, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← BUILDING؛ الحدث EVT-PRJ-BUILD-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Platform Operator (platform tenant)؛ الشروط: —؛ فصل المهام: —؛ الالتزامات: audit; mfa for PROMOTE
- **الربط:** `CMD-PRJ-CREATE-VERSION` · `AGG-PROJECTION-VERSION` · متطلبات: REQ-SRC-004 · حالات استخدام: UC-078
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRJ-CREATE-VERSION succeeds
  Given AGG-PROJECTION-VERSION does not exist yet and every guard holds
  When Platform Operator sends CMD-PRJ-CREATE-VERSION with a valid payload, a new Idempotency-Key
  Then the state becomes BUILDING
  And EVT-PRJ-BUILD-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRJ-CREATE-VERSION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRJ-CREATE-VERSION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PROJECTION_BUILD_IN_PROGRESS | 422 | لم يتحقق الشرط: at most one BUILDING version per (tenant group, kind) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: kind, tenant_group, schema_version, normalization_version, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-PRJ-PROMOTE — ترقية إصدار الإسقاط

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Platform Operator (platform tenant) | `POST /api/v1/discovery/projection-versions/{id}/actions/promote` | POL-PRJ-PROMOTE |

**القصة:** بصفتي **Platform Operator (platform tenant)**، أريد **ترقية إصدار الإسقاط**، لكي يتحقق غرض إصدار الإسقاط: إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green

- **الشروط المسبقة:** الحالة الحالية: READY؛ operator; verification passed; previous ACTIVE of same kind → RETIRED in the same step (alias switch)
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-PRJ-PROMOTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Platform Operator (platform tenant)؛ الشروط: —؛ فصل المهام: —؛ الالتزامات: audit; mfa for PROMOTE
- **الربط:** `CMD-PRJ-PROMOTE` · `AGG-PROJECTION-VERSION` · متطلبات: REQ-SRC-004 · حالات استخدام: UC-078
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRJ-PROMOTE succeeds
  Given AGG-PROJECTION-VERSION in state READY and every guard holds
  When Platform Operator sends CMD-PRJ-PROMOTE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-PRJ-PROMOTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRJ-PROMOTE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRJ-PROMOTE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PROJECTION_NOT_VERIFIED | 422 | لم يتحقق الشرط: verification passed |
    | PROJECTION_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, BUILDING, DEGRADED, FAILED, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-PRJ-RETIRE — إحالة إصدار الإسقاط إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Platform Operator (platform tenant) | `POST /api/v1/discovery/projection-versions/{id}/actions/retire` | POL-PRJ-RETIRE |

**القصة:** بصفتي **Platform Operator (platform tenant)**، أريد **إحالة إصدار الإسقاط إلى التقاعد**، لكي يتحقق غرض إصدار الإسقاط: إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green

- **الشروط المسبقة:** الحالة الحالية: READY, ACTIVE, DEGRADED؛ operator; not the only ACTIVE version of its kind
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-PRJ-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Platform Operator (platform tenant)؛ الشروط: —؛ فصل المهام: —؛ الالتزامات: audit; mfa for PROMOTE
- **الربط:** `CMD-PRJ-RETIRE` · `AGG-PROJECTION-VERSION` · متطلبات: REQ-SRC-004 · حالات استخدام: UC-078
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PRJ-RETIRE succeeds
  Given AGG-PROJECTION-VERSION in state READY or ACTIVE or DEGRADED and every guard holds
  When Platform Operator sends CMD-PRJ-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-PRJ-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PRJ-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PRJ-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LAST_ACTIVE_PROJECTION | 422 | لم يتحقق الشرط: not the only ACTIVE version of its kind |
    | PROJECTION_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: BUILDING, FAILED, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-PROJECTION-VERSION-01 — تلقائي: full rebuild reached live checkpoint (إصدار الإسقاط)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | BUILDING | READY |

**القصة:** بصفتي **النظام**، عند «full rebuild reached live checkpoint»، أريد نقل **إصدار الإسقاط** إلى READY، لكي يتحقق غرض إصدار الإسقاط: إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green

- **الشرط:** all source streams replayed to current checkpoint; verification sample equals source (FIT-11)
- **المخرجات:** الحدث EVT-PRJ-READY؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PROJECTION-VERSION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-PROJECTION-VERSION-02 — تلقائي: build failed (إصدار الإسقاط)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بعامل | النظام بهوية عبء عمل | BUILDING | FAILED |

**القصة:** بصفتي **النظام**، عند «build failed»، أريد نقل **إصدار الإسقاط** إلى FAILED، لكي يتحقق غرض إصدار الإسقاط: إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green

- **الشرط:** unrecoverable build error
- **المخرجات:** الحدث EVT-PRJ-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PROJECTION-VERSION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-PROJECTION-VERSION-03 — تلقائي: lag above threshold (إصدار الإسقاط)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | ACTIVE | DEGRADED |

**القصة:** بصفتي **النظام**، عند «lag above threshold»، أريد نقل **إصدار الإسقاط** إلى DEGRADED، لكي يتحقق غرض إصدار الإسقاط: إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green

- **الشرط:** lag > 5 min or error rate > 1 % for 5 min
- **المخرجات:** الحدث EVT-PRJ-DEGRADED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PROJECTION-VERSION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-PROJECTION-VERSION-04 — تلقائي: lag back within target (إصدار الإسقاط)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | DEGRADED | ACTIVE |

**القصة:** بصفتي **النظام**، عند «lag back within target»، أريد نقل **إصدار الإسقاط** إلى ACTIVE، لكي يتحقق غرض إصدار الإسقاط: إصدار فهرس بحث أو رسم يُبنى ويُرقّى بأسلوب blue/green

- **الشرط:** lag ≤ 30 s for 5 min
- **المخرجات:** الحدث EVT-PRJ-RECOVERED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PROJECTION-VERSION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-Q-PRJ-STATUS — جلب: Projection versions, lag, state

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | platform operator | `GET /api/v1/discovery/projection-versions` | POL-PRJ-STATUS |

**القصة:** بصفتي **platform operator**، أريد **جلب Projection versions, lag, state**، لكي يتحقق المتطلب: The system shall be able to rebuild every search and graph projection from the source of truth without data loss

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Projection versions, lag, state؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** platform operator؛ النطاق المسموح: PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-PRJ-STATUS` · `AGG-PROJECTION-VERSION` · متطلبات: REQ-SRC-004
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-PRJ-STATUS returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-PRJ-STATUS with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-PRJ-STATUS is denied
  Given the policy denies the caller
  When the caller sends QRY-PRJ-STATUS
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-SENSOR-STREAM — تدفق الحسّاس (Sensor Stream)

`03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md` · SLC-16 · الحالات: DRAFT, ACTIVE, PAUSED → RETIRED

#### US-BC07-SNS-ACTIVATE — تفعيل تدفق الحسّاس

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | integration engineer | `POST /api/v1/integration/sensor-streams/{id}/actions/activate` | POL-SNS-ACTIVATE |

**القصة:** بصفتي **integration engineer**، أريد **تفعيل تدفق الحسّاس**، لكي يتحقق غرض تدفق الحسّاس: تدفق قياسات حساس مرتبط بمصدر وكمية ووحدة وفحوص جودة

- **الشروط المسبقة:** الحالة الحالية: DRAFT, PAUSED؛ connection ACTIVE; mapping to CMD-OBS-RECORD batches tested
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-SNS-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SNS-ACTIVATE` · `AGG-SENSOR-STREAM` · متطلبات: REQ-INT-002 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SNS-ACTIVATE succeeds
  Given AGG-SENSOR-STREAM in state DRAFT or PAUSED and every guard holds
  When integration engineer sends CMD-SNS-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-SNS-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SNS-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SNS-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONNECTION_NOT_ACTIVE | 422 | لم يتحقق الشرط: connection ACTIVE |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SENSOR_STREAM_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-SNS-PAUSE — إيقاف تدفق الحسّاس مؤقتًا

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | integration engineer | `POST /api/v1/integration/sensor-streams/{id}/actions/pause` | POL-SNS-PAUSE |

**القصة:** بصفتي **integration engineer**، أريد **إيقاف تدفق الحسّاس مؤقتًا**، لكي يتحقق غرض تدفق الحسّاس: تدفق قياسات حساس مرتبط بمصدر وكمية ووحدة وفحوص جودة

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PAUSED؛ الحدث EVT-SNS-PAUSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SNS-PAUSE` · `AGG-SENSOR-STREAM` · متطلبات: REQ-INT-002 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SNS-PAUSE succeeds
  Given AGG-SENSOR-STREAM in state ACTIVE and every guard holds
  When integration engineer sends CMD-SNS-PAUSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PAUSED
  And EVT-SNS-PAUSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SNS-PAUSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SNS-PAUSE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SENSOR_STREAM_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DRAFT, PAUSED, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-SNS-REGISTER — تسجيل تدفق الحسّاس

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تكامل | integration engineer | `POST /api/v1/integration/sensor-streams` | POL-SNS-REGISTER |

**القصة:** بصفتي **integration engineer**، أريد **تسجيل تدفق الحسّاس**، لكي يتحقق غرض تدفق الحسّاس: تدفق قياسات حساس مرتبط بمصدر وكمية ووحدة وفحوص جودة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ connection (sensor_gateway) exists; BC02 Source of type sensor ACTIVE; quantity + UCUM unit; expected rate; location or linked entity
- **المدخلات:** `connection`!: urn, `source`!: urn, `quantity`!: string, `unit`!: string, `expected_rate`!: number, `location`: object, `linked_entity`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-SNS-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SNS-REGISTER` · `AGG-SENSOR-STREAM` · متطلبات: REQ-INT-002 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-CRE، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SNS-REGISTER succeeds
  Given AGG-SENSOR-STREAM does not exist yet and every guard holds
  When integration engineer sends CMD-SNS-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-SNS-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SNS-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SNS-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | STREAM_INVALID | 422 | لم يتحقق الشرط: connection (sensor_gateway) exists; BC02 Source of type sensor ACTIVE; quantity + UCUM unit; expected rate; location or linked entity |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: connection, source, quantity, unit, expected_rate |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-SNS-RETIRE — إحالة تدفق الحسّاس إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | integration engineer | `POST /api/v1/integration/sensor-streams/{id}/actions/retire` | POL-SNS-RETIRE |

**القصة:** بصفتي **integration engineer**، أريد **إحالة تدفق الحسّاس إلى التقاعد**، لكي يتحقق غرض تدفق الحسّاس: تدفق قياسات حساس مرتبط بمصدر وكمية ووحدة وفحوص جودة

- **الشروط المسبقة:** الحالة الحالية: DRAFT, PAUSED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-SNS-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SNS-RETIRE` · `AGG-SENSOR-STREAM` · متطلبات: REQ-INT-002 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SNS-RETIRE succeeds
  Given AGG-SENSOR-STREAM in state DRAFT or PAUSED and every guard holds
  When integration engineer sends CMD-SNS-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-SNS-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SNS-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SNS-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SENSOR_STREAM_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-SNS-SET-QUALITY-RULES — تحديد قواعد جودة تدفق الحسّاس

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تكامل | integration engineer | `POST /api/v1/integration/sensor-streams/{id}/actions/set-quality-rules` | POL-SNS-SET-QUALITY-RULES |

**القصة:** بصفتي **integration engineer**، أريد **تحديد قواعد جودة تدفق الحسّاس**، لكي يتحقق غرض تدفق الحسّاس: تدفق قياسات حساس مرتبط بمصدر وكمية ووحدة وفحوص جودة

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE, PAUSED؛ range, rate-of-change, stale-after, duplicate window; violations become data_quality issues, not rejections
- **المدخلات:** `rules`!: object — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SNS-QUALITY-RULES-SET؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** integration engineer؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SNS-SET-QUALITY-RULES` · `AGG-SENSOR-STREAM` · متطلبات: REQ-INT-002 · حالات استخدام: UC-094
- **ضوابط النوع والفئة:** C-UPD، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SNS-SET-QUALITY-RULES succeeds
  Given AGG-SENSOR-STREAM in state DRAFT or ACTIVE or PAUSED and every guard holds
  When integration engineer sends CMD-SNS-SET-QUALITY-RULES with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SNS-QUALITY-RULES-SET is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SNS-SET-QUALITY-RULES is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SNS-SET-QUALITY-RULES ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | QUALITY_RULES_INVALID | 422 | لم يتحقق الشرط: violations become data_quality issues, not rejections |
    | SENSOR_STREAM_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: rules |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-SENSOR-STREAM-01 — تلقائي: no data beyond stale-after (تدفق الحسّاس)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | ACTIVE | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «no data beyond stale-after»، أريد تحديث **تدفق الحسّاس** دون تغيير حالته، لكي يتحقق غرض تدفق الحسّاس: تدفق قياسات حساس مرتبط بمصدر وكمية ووحدة وفحوص جودة

- **الشرط:** stream flagged STALE; alert to owner
- **المخرجات:** الحدث EVT-SNS-STALE؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-SENSOR-STREAM` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-Q-SNS-LIST — جلب: Streams with rate, staleness, quality violation counts

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | integration engineers, Analyst | `GET /api/v1/integration/sensor-streams` | POL-SNS-LIST |

**القصة:** بصفتي **integration engineers, Analyst**، أريد **جلب Streams with rate, staleness, quality violation counts**، لكي يتحقق المتطلب: The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Streams with rate, staleness, quality violation counts؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** integration engineers, Analyst؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SNS-LIST` · `AGG-SENSOR-STREAM` · متطلبات: REQ-INT-002
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-SNS-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SNS-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SNS-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-SNS-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-SYNC-CONFLICT — تعارض المزامنة (Sync Conflict)

`03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md` · SLC-11 · الحالات: OPEN → RESOLVED_APPLIED, RESOLVED_DISCARDED, RESOLVED_MANUAL

#### US-BC07-SCF-ASSIGN — إسناد تعارض المزامنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تكامل | reviewer: task owner/Planner, Analyst for observations | `POST /api/v1/field/sync-conflicts/{id}/actions/assign` | POL-SCF-ASSIGN |

**القصة:** بصفتي **reviewer: task owner/Planner, Analyst for observations**، أريد **إسناد تعارض المزامنة**، لكي يتحقق غرض تعارض المزامنة: أمر ميداني لم يُطبق لأن الحالة تغيرت؛ ينتظر قراراً بشرياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ assignee authorized on the target
- **المدخلات:** `reviewer`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SCF-ASSIGNED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SCF-ASSIGN` · `AGG-SYNC-CONFLICT` · متطلبات: REQ-OFF-004 · حالات استخدام: UC-092
- **ضوابط النوع والفئة:** C-UPD، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SCF-ASSIGN succeeds
  Given AGG-SYNC-CONFLICT in state OPEN and every guard holds
  When reviewer: task owner/Planner, Analyst for observations sends CMD-SCF-ASSIGN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SCF-ASSIGNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SCF-ASSIGN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SCF-ASSIGN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REVIEWER_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: assignee authorized on the target |
    | SYNC_CONFLICT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RESOLVED_APPLIED, RESOLVED_DISCARDED, RESOLVED_MANUAL |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reviewer |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-SCF-DISCARD — حسم تعارض المزامنة بإسقاط الأمر الميداني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | reviewer: task owner/Planner, Analyst for observations | `POST /api/v1/field/sync-conflicts/{id}/actions/discard` | POL-SCF-DISCARD |

**القصة:** بصفتي **reviewer: task owner/Planner, Analyst for observations**، أريد **حسم تعارض المزامنة بإسقاط الأمر الميداني**، لكي يتحقق غرض تعارض المزامنة: أمر ميداني لم يُطبق لأن الحالة تغيرت؛ ينتظر قراراً بشرياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ reason; field user notified
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RESOLVED_DISCARDED؛ الحدث EVT-SCF-DISCARDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SCF-DISCARD` · `AGG-SYNC-CONFLICT` · متطلبات: REQ-OFF-004 · حالات استخدام: UC-092
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SCF-DISCARD succeeds
  Given AGG-SYNC-CONFLICT in state OPEN and every guard holds
  When reviewer: task owner/Planner, Analyst for observations sends CMD-SCF-DISCARD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RESOLVED_DISCARDED
  And EVT-SCF-DISCARDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SCF-DISCARD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SCF-DISCARD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SYNC_CONFLICT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RESOLVED_APPLIED, RESOLVED_DISCARDED, RESOLVED_MANUAL |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-SCF-REAPPLY — إعادة تطبيق تعارض المزامنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | reviewer: task owner/Planner, Analyst for observations | `POST /api/v1/field/sync-conflicts/{id}/actions/reapply` | POL-SCF-REAPPLY |

**القصة:** بصفتي **reviewer: task owner/Planner, Analyst for observations**، أريد **إعادة تطبيق تعارض المزامنة**، لكي يتحقق غرض تعارض المزامنة: أمر ميداني لم يُطبق لأن الحالة تغيرت؛ ينتظر قراراً بشرياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ reviewer re-sends the original intent against the current version; owner-context accepts (its guards still apply)
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RESOLVED_APPLIED؛ الحدث EVT-SCF-REAPPLIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SCF-REAPPLY` · `AGG-SYNC-CONFLICT` · متطلبات: REQ-OFF-004 · حالات استخدام: UC-092
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SCF-REAPPLY succeeds
  Given AGG-SYNC-CONFLICT in state OPEN and every guard holds
  When reviewer: task owner/Planner, Analyst for observations sends CMD-SCF-REAPPLY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RESOLVED_APPLIED
  And EVT-SCF-REAPPLIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SCF-REAPPLY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SCF-REAPPLY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OWNER_REJECTED | 422 | لم يتحقق الشرط: owner-context accepts (its guards still apply) |
    | SYNC_CONFLICT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RESOLVED_APPLIED, RESOLVED_DISCARDED, RESOLVED_MANUAL |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-SCF-RESOLVE-MANUALLY — حل تعارض المزامنة يدويًا

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | reviewer: task owner/Planner, Analyst for observations | `POST /api/v1/field/sync-conflicts/{id}/actions/resolve-manually` | POL-SCF-RESOLVE-MANUALLY |

**القصة:** بصفتي **reviewer: task owner/Planner, Analyst for observations**، أريد **حل تعارض المزامنة يدويًا**، لكي يتحقق غرض تعارض المزامنة: أمر ميداني لم يُطبق لأن الحالة تغيرت؛ ينتظر قراراً بشرياً

- **الشروط المسبقة:** الحالة الحالية: OPEN؛ note + reference to the alternative action taken
- **المدخلات:** `note`!: string, `action_ref`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RESOLVED_MANUAL؛ الحدث EVT-SCF-RESOLVED-MANUALLY؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SCF-RESOLVE-MANUALLY` · `AGG-SYNC-CONFLICT` · متطلبات: REQ-OFF-004 · حالات استخدام: UC-092
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SCF-RESOLVE-MANUALLY succeeds
  Given AGG-SYNC-CONFLICT in state OPEN and every guard holds
  When reviewer: task owner/Planner, Analyst for observations sends CMD-SCF-RESOLVE-MANUALLY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RESOLVED_MANUAL
  And EVT-SCF-RESOLVED-MANUALLY is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SCF-RESOLVE-MANUALLY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SCF-RESOLVE-MANUALLY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SYNC_CONFLICT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RESOLVED_APPLIED, RESOLVED_DISCARDED, RESOLVED_MANUAL |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: note |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-SYNC-CONFLICT-01 — تلقائي: stale state-changing command (تعارض المزامنة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | ∅ | OPEN |

**القصة:** بصفتي **النظام**، عند «stale state-changing command»، أريد نقل **تعارض المزامنة** إلى OPEN، لكي يتحقق غرض تعارض المزامنة: أمر ميداني لم يُطبق لأن الحالة تغيرت؛ ينتظر قراراً بشرياً

- **الشرط:** rule CF-05: base_version ≠ current; stores original envelope, current state snapshot and owner rejection reason; reviewer = owner-context default (task: owner/Planner; observation: Analyst)
- **المخرجات:** الحدث EVT-SCF-OPENED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-SYNC-CONFLICT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-Q-SCF-GET — جلب: Original envelope, current state snapshot, owner rejection reason

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | reviewer authorized on target | `GET /api/v1/field/sync-conflicts/{conflict_id}` | POL-SCF-GET |

**القصة:** بصفتي **reviewer authorized on target**، أريد **جلب Original envelope, current state snapshot, owner rejection reason**، لكي يتحقق المتطلب: If a synchronized command conflicts with the current server state, then the system shall route it to conflict review and shall not apply last-write-wins to T1 or T2 data

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Original envelope, current state snapshot, owner rejection reason
- **الصلاحية:** reviewer authorized on target؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SCF-GET` · `AGG-SYNC-CONFLICT` · متطلبات: REQ-OFF-004
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-SCF-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-SCF-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-SCF-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-SCF-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC07-Q-SCF-LIST — جلب: Open sync conflicts by target type, assignee

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | reviewers authorized on targets | `GET /api/v1/field/sync-conflicts` | POL-SCF-LIST |

**القصة:** بصفتي **reviewers authorized on targets**، أريد **جلب Open sync conflicts by target type, assignee**، لكي يتحقق المتطلب: If a synchronized command conflicts with the current server state, then the system shall route it to conflict review and shall not apply last-write-wins to T1 or T2 data

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Open sync conflicts by target type, assignee؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** reviewers authorized on targets؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SCF-LIST` · `AGG-SYNC-CONFLICT` · متطلبات: REQ-OFF-004
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-SCF-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SCF-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SCF-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-SCF-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-SYNC-SESSION — جلسة المزامنة (Sync Session)

`03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md` · SLC-11 · الحالات: OPEN, APPLYING → COMPLETED, COMPLETED_WITH_CONFLICTS, FAILED, REJECTED

#### US-BC07-SYN-OPEN — فتح جلسة المزامنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تكامل | field device + user | `POST /api/v1/field/sync-sessions` | POL-SYN-OPEN |

**القصة:** بصفتي **field device + user**، أريد **فتح جلسة المزامنة**، لكي يتحقق غرض جلسة المزامنة: جلسة مزامنة جهاز: مصافحة، رفع أوامر مرتبة، تطبيقها، ثم تنزيل الفروق

- **الشروط المسبقة:** الحالة الحالية: ∅؛ device ACTIVE; user authenticated (fresh token); device signature on handshake; clock offset measured (server − device); resumes after last acknowledged seq
- **المدخلات:** `device`!: urn, `device_time`!: date-time, `last_acked_seq`!: integer, `queue_length`!: integer, `queue_head_hash`!: string, `signature`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← OPEN؛ الحدث EVT-SYN-OPENED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** field device + user (open, upload)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SYN-OPEN` · `AGG-SYNC-SESSION` · متطلبات: REQ-OFF-001, REQ-OFF-003, REQ-OFF-004, REQ-OFF-006 · حالات استخدام: UC-090, UC-091, UC-092
- **ضوابط النوع والفئة:** C-CRE، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SYN-OPEN succeeds
  Given AGG-SYNC-SESSION does not exist yet and every guard holds
  When field device + user sends CMD-SYN-OPEN with a valid payload, a new Idempotency-Key
  Then the state becomes OPEN
  And EVT-SYN-OPENED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SYN-OPEN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SYN-OPEN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | DEVICE_NOT_ACTIVE | 422 | لم يتحقق الشرط: device ACTIVE; device signature on handshake; clock offset measured (server − device) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: device, device_time, last_acked_seq, queue_length, queue_head_hash, signature |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-SYN-UPLOAD-BATCH — رفع دفعة إلى جلسة المزامنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | field device + user | `POST /api/v1/field/sync-sessions/{id}/actions/upload-batch` | POL-SYN-UPLOAD-BATCH |

**القصة:** بصفتي **field device + user**، أريد **رفع دفعة إلى جلسة المزامنة**، لكي يتحقق غرض جلسة المزامنة: جلسة مزامنة جهاز: مصافحة، رفع أوامر مرتبة، تطبيقها، ثم تنزيل الفروق

- **الشروط المسبقة:** الحالة الحالية: OPEN, APPLYING؛ ≤ 200 commands; contiguous seq after last acknowledged; each envelope signed by device key; batch hash chain continues
- **المدخلات:** `envelopes`!: array, `end_of_queue`!: boolean — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← APPLYING؛ الحدث EVT-SYN-BATCH-RECEIVED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** field device + user (open, upload)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SYN-UPLOAD-BATCH` · `AGG-SYNC-SESSION` · متطلبات: REQ-OFF-001, REQ-OFF-003, REQ-OFF-004, REQ-OFF-006 · حالات استخدام: UC-090, UC-091, UC-092
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SYN-UPLOAD-BATCH succeeds
  Given AGG-SYNC-SESSION in state OPEN or APPLYING and every guard holds
  When field device + user sends CMD-SYN-UPLOAD-BATCH with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes APPLYING
  And EVT-SYN-BATCH-RECEIVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SYN-UPLOAD-BATCH is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SYN-UPLOAD-BATCH ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEQUENCE_GAP | 422 | لم يتحقق الشرط: ≤ 200 commands; contiguous seq after last acknowledged; each envelope signed by device key; batch hash chain continues |
    | SYNC_SESSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: COMPLETED, COMPLETED_WITH_CONFLICTS, FAILED, REJECTED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: envelopes, end_of_queue |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC07-S-SYNC-SESSION-01 — تلقائي: device LOST or SUSPENDED at handshake (جلسة المزامنة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | ∅ | REJECTED |

**القصة:** بصفتي **النظام**، عند «device LOST or SUSPENDED at handshake»، أريد نقل **جلسة المزامنة** إلى REJECTED، لكي يتحقق غرض جلسة المزامنة: جلسة مزامنة جهاز: مصافحة، رفع أوامر مرتبة، تطبيقها، ثم تنزيل الفروق

- **الشرط:** returns wipe (LOST) or stop (SUSPENDED) instruction only
- **المخرجات:** الحدث EVT-SYN-REJECTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-SYNC-SESSION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-SYNC-SESSION-02 — تلقائي: all uploaded commands processed without conflict (جلسة المزامنة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | APPLYING | COMPLETED |

**القصة:** بصفتي **النظام**، عند «all uploaded commands processed without conflict»، أريد نقل **جلسة المزامنة** إلى COMPLETED، لكي يتحقق غرض جلسة المزامنة: جلسة مزامنة جهاز: مصافحة، رفع أوامر مرتبة، تطبيقها، ثم تنزيل الفروق

- **الشرط:** device declared end of queue; every command applied or idempotently recognized
- **المخرجات:** الحدث EVT-SYN-COMPLETED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-SYNC-SESSION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-SYNC-SESSION-03 — تلقائي: all processed with ≥ 1 sync conflict (جلسة المزامنة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | APPLYING | COMPLETED_WITH_CONFLICTS |

**القصة:** بصفتي **النظام**، عند «all processed with ≥ 1 sync conflict»، أريد نقل **جلسة المزامنة** إلى COMPLETED_WITH_CONFLICTS، لكي يتحقق غرض جلسة المزامنة: جلسة مزامنة جهاز: مصافحة، رفع أوامر مرتبة، تطبيقها، ثم تنزيل الفروق

- **الشرط:** conflicts opened as AGG-SYNC-CONFLICT
- **المخرجات:** الحدث EVT-SYN-COMPLETED-WITH-CONFLICTS؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-SYNC-SESSION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-S-SYNC-SESSION-04 — تلقائي: idle timeout (5 min) or transport loss (جلسة المزامنة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | OPEN, APPLYING | FAILED |

**القصة:** بصفتي **النظام**، عند «idle timeout (5 min) or transport loss»، أريد نقل **جلسة المزامنة** إلى FAILED، لكي يتحقق غرض جلسة المزامنة: جلسة مزامنة جهاز: مصافحة، رفع أوامر مرتبة، تطبيقها، ثم تنزيل الفروق

- **الشرط:** acknowledged seq retained; next session resumes (REQ-OFF-006)
- **المخرجات:** الحدث EVT-SYN-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-SYNC-SESSION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC07-Q-SYN-DELTA — جلب: Server → device: my task changes, package updates, purge list, conflict notices, wipe/stop instruction

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | device + user of the session | `GET /api/v1/field/sync-sessions/{session_id}/delta` | POL-SYN-DELTA |

**القصة:** بصفتي **device + user of the session**، أريد **جلب Server → device: my task changes, package updates, purge list, conflict notices, wipe/stop instruction**، لكي يتحقق المتطلب: Where the mobile field application is used, the system shall allow recording observations with location, time and photos, and updating the status of assigned tasks, without connectivity for at least 72 hours

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Server → device: my task changes, package updates, purge list, conflict notices, wipe/stop instruction؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** device + user of the session؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SYN-DELTA` · `AGG-SYNC-SESSION` · متطلبات: REQ-OFF-001
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-SYN-DELTA returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SYN-DELTA with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SYN-DELTA is denied
  Given the policy denies the caller
  When the caller sends QRY-SYN-DELTA
  Then the response has the same shape as for a missing item (not-found shape)
```

### استعلامات عابرة للـAggregates

#### US-BC07-Q-AI-USAGE — جلب: GPU-hours, requests, cost indicators per tenant and operation

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | Administrator, finance | `GET /api/v1/ai/usage` | POL-AI-USAGE |

**القصة:** بصفتي **Administrator, finance**، أريد **جلب GPU-hours, requests, cost indicators per tenant and operation**، لكي يتحقق المتطلب: The system shall process every AI request through identity, policy, authorized retrieval, context package, model, output, grounding and confidence, and shall record each step

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** GPU-hours, requests, cost indicators per tenant and operation؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Administrator, finance؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AI-USAGE` · عابر للـAggregates · متطلبات: REQ-AI-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-AI-USAGE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-AI-USAGE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-AI-USAGE is denied
  Given the policy denies the caller
  When the caller sends QRY-AI-USAGE
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC07-Q-GRAPH-NEIGHBORHOOD — جلب: Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges cut

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/discovery/graph/entities/{entity_id}/neighborhood` | POL-GRAPH-NEIGHBORHOOD |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges cut**، لكي يتحقق المتطلب: The system shall represent relationships as objects with type, source, target, validity period, evidence, provenance, confidence and classification

- **المدخلات:** `cursor`, `limit`, `depth`, `valid_at`, `known_at`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges cut؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user; per-node and per-edge authorization؛ النطاق المسموح: PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-GRAPH-NEIGHBORHOOD` · عابر للـAggregates · متطلبات: REQ-INF-027
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-GRAPH-NEIGHBORHOOD returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-GRAPH-NEIGHBORHOOD with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-GRAPH-NEIGHBORHOOD is denied
  Given the policy denies the caller
  When the caller sends QRY-GRAPH-NEIGHBORHOOD
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC07-Q-GRAPH-PATHS — جلب: Paths between two entities, ≤ 4 hops, only through visible nodes and edges

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `POST /api/v1/discovery/graph/paths` | POL-GRAPH-PATHS |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Paths between two entities, ≤ 4 hops, only through visible nodes and edges**، لكي يتحقق المتطلب: The system shall represent relationships as objects with type, source, target, validity period, evidence, provenance, confidence and classification

- **المدخلات:** `from`!, `to`!, `max_hops`, `relationship_types`, `valid_at`, `known_at`, `max_paths` (معاملات الرابط وحقول جسم الطلب؛ `!` = إلزامي)؛ مع ترويسة `X-Purpose`
- **المخرجات:** Paths between two entities, ≤ 4 hops, only through visible nodes and edges
- **الصلاحية:** any user; per-node and per-edge authorization؛ النطاق المسموح: PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`, `known_at`
- **الربط:** `QRY-GRAPH-PATHS` · عابر للـAggregates · متطلبات: REQ-INF-027
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-GRAPH-PATHS computes its result only over what the caller may see
  Given data inside and outside the caller's allowed_scope
  When the caller sends QRY-GRAPH-PATHS
  Then the result neither includes nor reveals data outside allowed_scope

Scenario: QRY-GRAPH-PATHS is denied
  Given the policy denies the caller
  When the caller sends QRY-GRAPH-PATHS
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC07-Q-SRCH-QUERY — جلب: Unified search: text + types + polygon/bbox + time window + filters + facets; cursor paging; results and facets over visible facts only

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `POST /api/v1/discovery/search-queries` | POL-SRCH-QUERY |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Unified search: text + types + polygon/bbox + time window + filters + facets; cursor paging; results and facets over visible facts only**، لكي يتحقق المتطلب: The system shall provide unified search across entities, observations, documents, assessments, plans and tasks, with text, spatial and temporal filters

- **المدخلات:** `text`, `types`!, `geo`, `time`, `valid_at`, `filters`, `facets`, `sort`, `cursor`, `limit` (معاملات الرابط وحقول جسم الطلب؛ `!` = إلزامي)؛ مع ترويسة `X-Purpose`
- **المخرجات:** Unified search: text + types + polygon/bbox + time window + filters + facets; cursor paging; results and facets over visible facts only؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user; allowed_scope pre-filter + authoritative re-check؛ النطاق المسموح: PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `valid_at`
- **الربط:** `QRY-SRCH-QUERY` · عابر للـAggregates · متطلبات: REQ-SRC-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SRCH-QUERY returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SRCH-QUERY with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SRCH-QUERY is denied
  Given the policy denies the caller
  When the caller sends QRY-SRCH-QUERY
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC07-Q-SRCH-SUGGEST — جلب: Autocomplete from visible facts only

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user; same filter | `GET /api/v1/discovery/suggestions` | POL-SRCH-SUGGEST |

**القصة:** بصفتي **any user; same filter**، أريد **جلب Autocomplete from visible facts only**، لكي يتحقق المتطلب: The system shall match Arabic text regardless of hamza forms, alef maqsura, taa marbuta, diacritics and tatweel, and shall match names across Arabic and Latin transliterations

- **المدخلات:** `cursor`, `limit`, `q`!؛ مع ترويسة `X-Purpose`
- **المخرجات:** Autocomplete from visible facts only؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user; same filter؛ النطاق المسموح: PDP allowed_scope → pre-filter on doc and fact labels; LabelCheck re-check on page؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SRCH-SUGGEST` · عابر للـAggregates · متطلبات: REQ-SRC-003
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SRCH-SUGGEST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SRCH-SUGGEST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SRCH-SUGGEST is denied
  Given the policy denies the caller
  When the caller sends QRY-SRCH-SUGGEST
  Then the response has the same shape as for a missing item (not-found shape)
```

<!-- END GENERATED: build_analysis_design.py -->
