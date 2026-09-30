---
id: AD-05-US-BC04
type: user-stories
title: "قصص المستخدم — BC04"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
generator: 17-system-study/_build/build_analysis_design.py
---

# قصص المستخدم — BC04 Operations — التخطيط والتنفيذ

مولَّد بالكامل من المصادر بواسطة `17-system-study/_build/build_analysis_design.py`؛ لا يُحرَّر يدويًا. القالب والتصنيف وتعريف ضوابط النوع والفئة في [00-guide.md](00-guide.md).

<!-- BEGIN GENERATED: build_analysis_design.py -->

## ملخص BC04

| نوع العملية | عدد القصص |
|---|---|
| إنشاء | 10 |
| تعديل | 24 |
| جلب | 21 |
| حذف / إنهاء | 17 |
| سير عمل | 31 |
| نظام (SYS) | 23 |
| **المجموع** | **126** |

### AGG-COORDINATION-CASE — حالة التنسيق (Coordination Case)

`03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md` · SLC-15 · الحالات: OPEN, ACTIVE → CLOSED, CANCELLED

#### US-BC04-CRD-ACTIVATE — تفعيل حالة التنسيق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | lead organization Manager | `POST /api/v1/operations/coordination-cases/{id}/actions/activate` | POL-CRD-ACTIVATE |

**القصة:** بصفتي **lead organization Manager**، أريد **تفعيل حالة التنسيق**، لكي يتحقق غرض حالة التنسيق: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة

- **الشروط المسبقة:** الحالة الحالية ∈ {OPEN}؛ ≥ 2 participants
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-CRD-ACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)؛ الشروط: tenant match; participant scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRD-ACTIVATE` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001, REQ-CRD-002 · حالات استخدام: UC-130, UC-131
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRD-ACTIVATE succeeds
  Given AGG-COORDINATION-CASE in state OPEN and every guard holds
  When lead organization Manager sends CMD-CRD-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-CRD-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRD-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRD-ACTIVATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | COORDINATION_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CANCELLED, CLOSED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PARTICIPANTS_REQUIRED | 422 | لم يتحقق الشرط: ≥ 2 participants |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-CRD-ADD-PARTICIPANT — إضافة مشارك إلى حالة التنسيق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | lead organization Manager | `POST /api/v1/operations/coordination-cases/{id}/actions/add-participant` | POL-CRD-ADD-PARTICIPANT |

**القصة:** بصفتي **lead organization Manager**، أريد **إضافة مشارك إلى حالة التنسيق**، لكي يتحقق غرض حالة التنسيق: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, OPEN}؛ org unit in the same tenant; participant role; access scope (sections); participant's members cleared for case label
- **المدخلات:** `org_unit`!: urn, `role`!: string, `access_scope`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CRD-PARTICIPANT-ADDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)؛ الشروط: tenant match; participant scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRD-ADD-PARTICIPANT` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001, REQ-CRD-002 · حالات استخدام: UC-130, UC-131
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRD-ADD-PARTICIPANT succeeds
  Given AGG-COORDINATION-CASE in state ACTIVE or OPEN and every guard holds
  When lead organization Manager sends CMD-CRD-ADD-PARTICIPANT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-CRD-PARTICIPANT-ADDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRD-ADD-PARTICIPANT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRD-ADD-PARTICIPANT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | COORDINATION_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PARTICIPANT_INVALID | 422 | لم يتحقق الشرط: org unit in the same tenant; participant role; access scope (sections); participant's members cleared for case label |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: org_unit, role, access_scope |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-CRD-ASSIGN-RESPONSIBILITY — إسناد مسؤولية ضمن حالة التنسيق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | lead organization Manager | `POST /api/v1/operations/coordination-cases/{id}/actions/assign-responsibility` | POL-CRD-ASSIGN-RESPONSIBILITY |

**القصة:** بصفتي **lead organization Manager**، أريد **إسناد مسؤولية ضمن حالة التنسيق**، لكي يتحقق غرض حالة التنسيق: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ participant exists; item, due; flag requires_authority (decision type) when the action needs that organization's authority
- **المدخلات:** `participant`!: urn, `item`!: LocalizedName, `due`!: date-time, `requires_authority`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CRD-RESPONSIBILITY-ASSIGNED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)؛ الشروط: tenant match; participant scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRD-ASSIGN-RESPONSIBILITY` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001, REQ-CRD-002 · حالات استخدام: UC-130, UC-131
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRD-ASSIGN-RESPONSIBILITY succeeds
  Given AGG-COORDINATION-CASE in state ACTIVE and every guard holds
  When lead organization Manager sends CMD-CRD-ASSIGN-RESPONSIBILITY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-CRD-RESPONSIBILITY-ASSIGNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRD-ASSIGN-RESPONSIBILITY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRD-ASSIGN-RESPONSIBILITY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | COORDINATION_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, OPEN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RESPONSIBILITY_INVALID | 422 | لم يتحقق الشرط: participant exists; item, due; flag requires_authority (decision type) when the action needs that organization's authority |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: participant, item, due |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-CRD-CANCEL — إلغاء حالة التنسيق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | lead organization Manager | `POST /api/v1/operations/coordination-cases/{id}/actions/cancel` | POL-CRD-CANCEL |

**القصة:** بصفتي **lead organization Manager**، أريد **إلغاء حالة التنسيق**، لكي يتحقق غرض حالة التنسيق: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, OPEN}؛ lead; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-CRD-CANCELLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)؛ الشروط: tenant match; participant scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRD-CANCEL` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001, REQ-CRD-002 · حالات استخدام: UC-130, UC-131
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRD-CANCEL succeeds
  Given AGG-COORDINATION-CASE in state ACTIVE or OPEN and every guard holds
  When lead organization Manager sends CMD-CRD-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-CRD-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRD-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRD-CANCEL لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | COORDINATION_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-CRD-CLOSE — إغلاق حالة التنسيق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | lead organization Manager | `POST /api/v1/operations/coordination-cases/{id}/actions/close` | POL-CRD-CLOSE |

**القصة:** بصفتي **lead organization Manager**، أريد **إغلاق حالة التنسيق**، لكي يتحقق غرض حالة التنسيق: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ all responsibilities done or waived; closing note
- **المدخلات:** `note`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-CRD-CLOSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)؛ الشروط: tenant match; participant scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRD-CLOSE` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001, REQ-CRD-002 · حالات استخدام: UC-130, UC-131
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRD-CLOSE succeeds
  Given AGG-COORDINATION-CASE in state ACTIVE and every guard holds
  When lead organization Manager sends CMD-CRD-CLOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-CRD-CLOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRD-CLOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRD-CLOSE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | COORDINATION_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, OPEN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OPEN_RESPONSIBILITIES | 422 | لم يتحقق الشرط: all responsibilities done or waived; closing note |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: note |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-CRD-OPEN — فتح حالة التنسيق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | lead organization Manager | `POST /api/v1/operations/coordination-cases` | POL-CRD-OPEN |

**القصة:** بصفتي **lead organization Manager**، أريد **فتح حالة التنسيق**، لكي يتحقق غرض حالة التنسيق: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ title; purpose; lead organization; linked decisions/plans/situations visible to the opener; label
- **المدخلات:** `title`!: LocalizedName, `purpose`!: LocalizedName, `lead_org`!: urn, `links`: array, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← OPEN؛ الحدث EVT-CRD-OPENED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)؛ الشروط: tenant match; participant scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRD-OPEN` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001, REQ-CRD-002 · حالات استخدام: UC-130, UC-131
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRD-OPEN succeeds
  Given AGG-COORDINATION-CASE in state ∅ and every guard holds
  When lead organization Manager sends CMD-CRD-OPEN with a valid payload, a new Idempotency-Key
  Then the state becomes OPEN
  And EVT-CRD-OPENED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRD-OPEN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRD-OPEN لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | COORDINATION_INVALID | 422 | لم يتحقق الشرط: title; purpose; lead organization; linked decisions/plans/situations visible to the opener; label |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: title, purpose, lead_org, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-CRD-REMOVE-PARTICIPANT — إزالة مشارك من حالة التنسيق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | lead organization Manager | `POST /api/v1/operations/coordination-cases/{id}/actions/remove-participant` | POL-CRD-REMOVE-PARTICIPANT |

**القصة:** بصفتي **lead organization Manager**، أريد **إزالة مشارك من حالة التنسيق**، لكي يتحقق غرض حالة التنسيق: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, OPEN}؛ not the lead; no open responsibilities
- **المدخلات:** `org_unit`!: urn, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CRD-PARTICIPANT-REMOVED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)؛ الشروط: tenant match; participant scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRD-REMOVE-PARTICIPANT` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001, REQ-CRD-002 · حالات استخدام: UC-130, UC-131
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRD-REMOVE-PARTICIPANT succeeds
  Given AGG-COORDINATION-CASE in state ACTIVE or OPEN and every guard holds
  When lead organization Manager sends CMD-CRD-REMOVE-PARTICIPANT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-CRD-PARTICIPANT-REMOVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRD-REMOVE-PARTICIPANT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRD-REMOVE-PARTICIPANT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | COORDINATION_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PARTICIPANT_HAS_RESPONSIBILITIES | 422 | لم يتحقق الشرط: not the lead; no open responsibilities |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: org_unit, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-CRD-REQUEST-DECISION — طلب قرار ضمن حالة التنسيق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | participant members | `POST /api/v1/operations/coordination-cases/{id}/actions/request-decision` | POL-CRD-REQUEST-DECISION |

**القصة:** بصفتي **participant members**، أريد **طلب قرار ضمن حالة التنسيق**، لكي يتحقق غرض حالة التنسيق: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ responsibility requires authority; creates a Decision Request (SLC-08) in the participant's scope with the required decision type
- **المدخلات:** `responsibility_id`!: string, `question`!: LocalizedName, `options`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CRD-DECISION-REQUESTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)؛ الشروط: tenant match; participant scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRD-REQUEST-DECISION` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001, REQ-CRD-002 · حالات استخدام: UC-130, UC-131
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRD-REQUEST-DECISION succeeds
  Given AGG-COORDINATION-CASE in state ACTIVE and every guard holds
  When participant members sends CMD-CRD-REQUEST-DECISION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-CRD-DECISION-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRD-REQUEST-DECISION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRD-REQUEST-DECISION لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | COORDINATION_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, OPEN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RESPONSIBILITY_INVALID | 422 | لم يتحقق الشرط: responsibility requires authority; creates a Decision Request (SLC-08) in the participant's scope with the required decision type |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: responsibility_id, question, options |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-CRD-UPDATE-RESPONSIBILITY — تحديث مسؤولية ضمن حالة التنسيق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | participant members | `POST /api/v1/operations/coordination-cases/{id}/actions/update-responsibility` | POL-CRD-UPDATE-RESPONSIBILITY |

**القصة:** بصفتي **participant members**، أريد **تحديث مسؤولية ضمن حالة التنسيق**، لكي يتحقق غرض حالة التنسيق: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ actor belongs to the responsible participant; status ∈ {in_progress, done, waived with reason}; items requiring authority cannot be done before the decision is recorded
- **المدخلات:** `responsibility_id`!: string, `status`!: enum(in_progress, `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CRD-RESPONSIBILITY-UPDATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)؛ الشروط: tenant match; participant scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CRD-UPDATE-RESPONSIBILITY` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001, REQ-CRD-002 · حالات استخدام: UC-130, UC-131
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CRD-UPDATE-RESPONSIBILITY succeeds
  Given AGG-COORDINATION-CASE in state ACTIVE and every guard holds
  When participant members sends CMD-CRD-UPDATE-RESPONSIBILITY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-CRD-RESPONSIBILITY-UPDATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CRD-UPDATE-RESPONSIBILITY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CRD-UPDATE-RESPONSIBILITY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | COORDINATION_CASE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, OPEN |
    | DECISION_PENDING | 422 | لم يتحقق الشرط: actor belongs to the responsible participant; status ∈ {in_progress, done, waived with reason}; items requiring authority cannot be done before the decision is recorded |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: responsibility_id, status |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-COORDINATION-CASE-01 — تلقائي: linked decision recorded (حالة التنسيق)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ACTIVE | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «linked decision recorded»، أريد تحديث **حالة التنسيق** دون تغيير حالته، لكي يتحقق غرض حالة التنسيق: تنسيق بين وحدات/مؤسسات داخل المستأجر حول قرارات وخطط ومواقف مشتركة

- **الشرط:** decision references the request created by the case; outcome stored on the responsibility
- **المخرجات:** الحدث EVT-CRD-DECISION-RECORDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-COORDINATION-CASE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-Q-CRD-GET — جلب: Case filtered to the caller's participant scope

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | participants (scope-limited); lead | `GET /api/v1/operations/coordination-cases/{case_id}` | POL-CRD-GET |

**القصة:** بصفتي **participants (scope-limited); lead**، أريد **جلب Case filtered to the caller's participant scope**، لكي يتحقق المتطلب: The system shall manage coordination cases linking decisions, plans and organizations that must act together, with participants, responsibilities and status

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Case filtered to the caller's participant scope
- **الصلاحية:** participants (scope-limited); lead؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CRD-GET` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-CRD-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CRD-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CRD-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-CRD-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC04-Q-CRD-LIST — جلب: Cases where the caller's unit participates

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | allowed_scope | `GET /api/v1/operations/coordination-cases` | POL-CRD-LIST |

**القصة:** بصفتي **allowed_scope**، أريد **جلب Cases where the caller's unit participates**، لكي يتحقق المتطلب: The system shall manage coordination cases linking decisions, plans and organizations that must act together, with participants, responsibilities and status

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Cases where the caller's unit participates؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CRD-LIST` · `AGG-COORDINATION-CASE` · متطلبات: REQ-CRD-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-CRD-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CRD-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CRD-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-CRD-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-DECISION — القرار (Decision)

`03-domain/contexts/BC04/aggregates/AGG-DECISION.md` · SLC-08 · الحالات: RECORDED → SUPERSEDED, ANNULLED

#### US-BC04-DEC-ANNUL — إبطال القرار

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | higher authority | `POST /api/v1/operations/decisions/{id}/actions/annul` | POL-DEC-ANNUL |

**القصة:** بصفتي **higher authority**، أريد **إبطال القرار**، لكي يتحقق غرض القرار: قرار مسجل بسلطة مختصة وخيار ومبرر وسريان؛ غير قابل للتعديل

- **الشروط المسبقة:** الحالة الحالية ∈ {RECORDED}؛ recorded in error; actor holds authority for the same decision type at a higher scope; reason; plans implementing it are flagged
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ANNULLED؛ الحدث EVT-DEC-ANNULLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** authority holder (record) · higher authority (annul)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: authority at higher scope؛ الالتزامات: audit; mfa
- **الربط:** `CMD-DEC-ANNUL` · `AGG-DECISION` · متطلبات: REQ-DEC-002, REQ-DEC-003, REQ-DEC-004 · حالات استخدام: UC-032
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DEC-ANNUL succeeds
  Given AGG-DECISION in state RECORDED and every guard holds
  When higher authority sends CMD-DEC-ANNUL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ANNULLED
  And EVT-DEC-ANNULLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DEC-ANNUL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHORITY_REQUIRED | 422 | لم يتحقق الشرط: recorded in error; actor holds authority for the same decision type at a higher scope; reason; plans implementing it are flagged |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DEC-ANNUL لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DECISION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ANNULLED, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-DEC-RECORD — تسجيل القرار

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | authority holder | `POST /api/v1/operations/decisions` | POL-DEC-RECORD |

**القصة:** بصفتي **authority holder**، أريد **تسجيل القرار**، لكي يتحقق غرض القرار: قرار مسجل بسلطة مختصة وخيار ومبرر وسريان؛ غير قابل للتعديل

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ AuthorityCheck(decider, decision type, scope, now) = authorized — grant chain stored as authority snapshot (BRL-003, REQ-DEC-002); request OPEN (or ad-hoc with rationale and ≥ 1 citation); selected option ∈ request options; rationale; effective_from ≥ now − 1 h; supersedes (optional) is RECORDED and same scope
- **المدخلات:** `request`: urn, `selected_option`!: string, `rationale`!: LocalizedName, `effective_from`!: date-time, `citations`: array, `supersedes`: urn, `ad_hoc_reason`: string, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← RECORDED؛ الحدث EVT-DEC-RECORDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** authority holder (record) · higher authority (annul)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: AuthorityCheck (BRL-003)؛ الالتزامات: audit; mfa
- **الربط:** `CMD-DEC-RECORD` · `AGG-DECISION` · متطلبات: REQ-DEC-002, REQ-DEC-003, REQ-DEC-004 · حالات استخدام: UC-032
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DEC-RECORD succeeds
  Given AGG-DECISION in state ∅ and every guard holds
  When authority holder sends CMD-DEC-RECORD with a valid payload, a new Idempotency-Key
  Then the state becomes RECORDED
  And EVT-DEC-RECORDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DEC-RECORD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHORITY_REQUIRED | 422 | لم يتحقق الشرط: AuthorityCheck(decider, decision type, scope, now) = authorized — grant chain stored as authority snapshot (BRL-003, REQ-DEC-002); request OPEN (or ad-hoc with rationale and ≥ 1 citation); selected option ∈ request options; rationale; effective_from ≥ now − 1 h; supersedes (optional) is RECORDED and same scope |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DEC-RECORD لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: selected_option, rationale, effective_from, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-DECISION-01 — تلقائي: superseding decision recorded (القرار)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | RECORDED | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «superseding decision recorded»، أريد نقل **القرار** إلى SUPERSEDED، لكي يتحقق غرض القرار: قرار مسجل بسلطة مختصة وخيار ومبرر وسريان؛ غير قابل للتعديل

- **الشرط:** new decision references this one in supersedes
- **المخرجات:** الحدث EVT-DEC-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-DECISION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-Q-DEC-BASIS — جلب: What was known at decision time: cited assessments (pinned versions) and their key claims resolved known_at = decision.recorded_at

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | label rule; Auditor | `GET /api/v1/operations/decisions/{decision_id}/basis` | POL-DEC-BASIS |

**القصة:** بصفتي **label rule; Auditor**، أريد **جلب What was known at decision time: cited assessments (pinned versions) and their key claims resolved known_at = decision.recorded_at**، لكي يتحقق المتطلب: The system shall record for each decision the selected option, rationale, authority, approval, effective time and links to the assessments and evidence considered

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** What was known at decision time: cited assessments (pinned versions) and their key claims resolved known_at = decision.recorded_at؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** label rule; Auditor؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-DEC-BASIS` · `AGG-DECISION` · متطلبات: REQ-DEC-003
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-DEC-BASIS returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-DEC-BASIS with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-DEC-BASIS is denied
  Given the policy denies the caller
  When the caller sends QRY-DEC-BASIS
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC04-Q-DEC-GET — جلب: Decision with authority snapshot, citations (pinned) and supersession chain

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | label rule | `GET /api/v1/operations/decisions/{decision_id}` | POL-DEC-GET |

**القصة:** بصفتي **label rule**، أريد **جلب Decision with authority snapshot, citations (pinned) and supersession chain**، لكي يتحقق المتطلب: The system shall record for each decision the selected option, rationale, authority, approval, effective time and links to the assessments and evidence considered

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Decision with authority snapshot, citations (pinned) and supersession chain
- **الصلاحية:** label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-DEC-GET` · `AGG-DECISION` · متطلبات: REQ-DEC-003
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-DEC-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-DEC-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-DEC-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-DEC-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-DECISION-REQUEST — طلب القرار (Decision Request)

`03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md` · SLC-08 · الحالات: DRAFT, OPEN → DECIDED, WITHDRAWN

#### US-BC04-DRQ-ADD-OPTION — إضافة خيار إلى طلب القرار

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst / Planner / Manager | `POST /api/v1/operations/decision-requests/{id}/actions/add-option` | POL-DRQ-ADD-OPTION |

**القصة:** بصفتي **Analyst / Planner / Manager**، أريد **إضافة خيار إلى طلب القرار**، لكي يتحقق غرض طلب القرار: طلب قرار بسؤال وخيارات وتقييمات مستشهد بها وسلطة مطلوبة

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT, OPEN}؛ option text; expected impact; options ≤ 10
- **المدخلات:** `text`!: LocalizedName, `expected_impact`: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-DRQ-OPTION-ADDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Analyst / Planner / Manager (create, add, cite, open, withdraw)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DRQ-ADD-OPTION` · `AGG-DECISION-REQUEST` · متطلبات: REQ-DEC-001 · حالات استخدام: UC-030, UC-031
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DRQ-ADD-OPTION succeeds
  Given AGG-DECISION-REQUEST in state DRAFT or OPEN and every guard holds
  When Analyst / Planner / Manager sends CMD-DRQ-ADD-OPTION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-DRQ-OPTION-ADDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DRQ-ADD-OPTION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DRQ-ADD-OPTION لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DECISION_REQUEST_INVALID | 422 | لم يتحقق الشرط: option text; expected impact; options ≤ 10 |
    | DECISION_REQUEST_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DECIDED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: text |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-DRQ-CITE — الاستشهاد في طلب القرار

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Analyst / Planner / Manager | `POST /api/v1/operations/decision-requests/{id}/actions/cite` | POL-DRQ-CITE |

**القصة:** بصفتي **Analyst / Planner / Manager**، أريد **الاستشهاد في طلب القرار**، لكي يتحقق غرض طلب القرار: طلب قرار بسؤال وخيارات وتقييمات مستشهد بها وسلطة مطلوبة

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT, OPEN}؛ assessment or evidence visible; pinned URN + version; cited label ≤ request label
- **المدخلات:** `citations`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-DRQ-CITED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Analyst / Planner / Manager (create, add, cite, open, withdraw)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DRQ-CITE` · `AGG-DECISION-REQUEST` · متطلبات: REQ-DEC-001 · حالات استخدام: UC-030, UC-031
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DRQ-CITE succeeds
  Given AGG-DECISION-REQUEST in state DRAFT or OPEN and every guard holds
  When Analyst / Planner / Manager sends CMD-DRQ-CITE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-DRQ-CITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DRQ-CITE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DRQ-CITE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CITATION_ABOVE_LABEL | 422 | لم يتحقق الشرط: assessment or evidence visible; pinned URN + version; cited label ≤ request label |
    | DECISION_REQUEST_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DECIDED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: citations |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-DRQ-CREATE — إنشاء طلب القرار

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Analyst / Planner / Manager | `POST /api/v1/operations/decision-requests` | POL-DRQ-CREATE |

**القصة:** بصفتي **Analyst / Planner / Manager**، أريد **إنشاء طلب القرار**، لكي يتحقق غرض طلب القرار: طلب قرار بسؤال وخيارات وتقييمات مستشهد بها وسلطة مطلوبة

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ question; required decision type (RD-DECISION-TYPES); scope unit; deadline; label
- **المدخلات:** `question`!: LocalizedName, `decision_type`!: string, `scope`!: urn, `deadline`!: date-time, `context_refs`: array, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-DRQ-CREATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Analyst / Planner / Manager (create, add, cite, open, withdraw)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DRQ-CREATE` · `AGG-DECISION-REQUEST` · متطلبات: REQ-DEC-001 · حالات استخدام: UC-030, UC-031
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DRQ-CREATE succeeds
  Given AGG-DECISION-REQUEST in state ∅ and every guard holds
  When Analyst / Planner / Manager sends CMD-DRQ-CREATE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-DRQ-CREATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DRQ-CREATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DRQ-CREATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DECISION_REQUEST_INVALID | 422 | لم يتحقق الشرط: question; required decision type (RD-DECISION-TYPES); scope unit; deadline; label |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: question, decision_type, scope, deadline, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-DRQ-OPEN — فتح طلب القرار

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Analyst / Planner / Manager | `POST /api/v1/operations/decision-requests/{id}/actions/open` | POL-DRQ-OPEN |

**القصة:** بصفتي **Analyst / Planner / Manager**، أريد **فتح طلب القرار**، لكي يتحقق غرض طلب القرار: طلب قرار بسؤال وخيارات وتقييمات مستشهد بها وسلطة مطلوبة

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ ≥ 2 options (one may be 'no action'); ≥ 1 citation (REQ-DEC-001, OUT-04)
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← OPEN؛ الحدث EVT-DRQ-OPENED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Analyst / Planner / Manager (create, add, cite, open, withdraw)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DRQ-OPEN` · `AGG-DECISION-REQUEST` · متطلبات: REQ-DEC-001 · حالات استخدام: UC-030, UC-031
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DRQ-OPEN succeeds
  Given AGG-DECISION-REQUEST in state DRAFT and every guard holds
  When Analyst / Planner / Manager sends CMD-DRQ-OPEN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes OPEN
  And EVT-DRQ-OPENED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DRQ-OPEN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DRQ-OPEN لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DECISION_REQUEST_INCOMPLETE | 422 | لم يتحقق الشرط: ≥ 2 options (one may be 'no action'); ≥ 1 citation (REQ-DEC-001, OUT-04) |
    | DECISION_REQUEST_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DECIDED, OPEN, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-DRQ-WITHDRAW — سحب طلب القرار

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Analyst / Planner / Manager | `POST /api/v1/operations/decision-requests/{id}/actions/withdraw` | POL-DRQ-WITHDRAW |

**القصة:** بصفتي **Analyst / Planner / Manager**، أريد **سحب طلب القرار**، لكي يتحقق غرض طلب القرار: طلب قرار بسؤال وخيارات وتقييمات مستشهد بها وسلطة مطلوبة

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT, OPEN}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← WITHDRAWN؛ الحدث EVT-DRQ-WITHDRAWN؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Analyst / Planner / Manager (create, add, cite, open, withdraw)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DRQ-WITHDRAW` · `AGG-DECISION-REQUEST` · متطلبات: REQ-DEC-001 · حالات استخدام: UC-030, UC-031
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DRQ-WITHDRAW succeeds
  Given AGG-DECISION-REQUEST in state DRAFT or OPEN and every guard holds
  When Analyst / Planner / Manager sends CMD-DRQ-WITHDRAW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes WITHDRAWN
  And EVT-DRQ-WITHDRAWN is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DRQ-WITHDRAW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DRQ-WITHDRAW لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DECISION_REQUEST_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DECIDED, WITHDRAWN |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-DECISION-REQUEST-01 — تلقائي: deadline passed (طلب القرار)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | OPEN | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «deadline passed»، أريد تحديث **طلب القرار** دون تغيير حالته، لكي يتحقق غرض طلب القرار: طلب قرار بسؤال وخيارات وتقييمات مستشهد بها وسلطة مطلوبة

- **الشرط:** escalates to holders of the required authority in scope
- **المخرجات:** الحدث EVT-DRQ-ESCALATED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-DECISION-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-DECISION-REQUEST-02 — تلقائي: decision recorded for this request (طلب القرار)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | OPEN | DECIDED |

**القصة:** بصفتي **النظام**، عند «decision recorded for this request»، أريد نقل **طلب القرار** إلى DECIDED، لكي يتحقق غرض طلب القرار: طلب قرار بسؤال وخيارات وتقييمات مستشهد بها وسلطة مطلوبة

- **الشرط:** EVT-DEC-RECORDED references the request
- **المخرجات:** الحدث EVT-DRQ-DECIDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-DECISION-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-Q-DRQ-GET — جلب: Request with options and pinned citations (withheld per policy)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | label rule; required-authority holders in scope | `GET /api/v1/operations/decision-requests/{request_id}` | POL-DRQ-GET |

**القصة:** بصفتي **label rule; required-authority holders in scope**، أريد **جلب Request with options and pinned citations (withheld per policy)**، لكي يتحقق المتطلب: The system shall record each decision request with its question, options, assessment references, deadline and required authority type

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Request with options and pinned citations (withheld per policy)
- **الصلاحية:** label rule; required-authority holders in scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-DRQ-GET` · `AGG-DECISION-REQUEST` · متطلبات: REQ-DEC-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-DRQ-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-DRQ-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-DRQ-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-DRQ-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC04-Q-DRQ-LIST — جلب: My pending requests (as authority holder), by deadline

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | allowed_scope | `GET /api/v1/operations/decision-requests` | POL-DRQ-LIST |

**القصة:** بصفتي **allowed_scope**، أريد **جلب My pending requests (as authority holder), by deadline**، لكي يتحقق المتطلب: The system shall record each decision request with its question, options, assessment references, deadline and required authority type

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** My pending requests (as authority holder), by deadline؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-DRQ-LIST` · `AGG-DECISION-REQUEST` · متطلبات: REQ-DEC-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-DRQ-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-DRQ-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-DRQ-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-DRQ-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-INCIDENT — الحادثة (Incident)

`03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md` · SLC-17 · الحالات: REPORTED, ASSESSED, RESPONDING, CONTAINED, RESOLVED → CLOSED, CANCELLED

#### US-BC04-INC-ACTIVATE-CONTINGENCY — تفعيل خطة الاستمرارية لـالحادثة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | قائد الحادثة بسلطة صريحة لتفعيل الاستمرارية | `POST /api/v1/operations/incidents/{id}/actions/activate-contingency` | POL-INC-ACTIVATE-CONTINGENCY |

**القصة:** بصفتي **قائد الحادثة بسلطة صريحة لتفعيل الاستمرارية**، أريد **تفعيل خطة الاستمرارية لـالحادثة**، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشروط المسبقة:** الحالة الحالية ∈ {ASSESSED, CONTAINED, REPORTED, RESOLVED, RESPONDING}؛ سلطة؛ ينشئ/يربط Plan (SLC-08، plan_kind=CONTINGENCY، triggered_by=هذه الحادثة — CR-60)؛ أمر صريح دائماً، ليس أثراً تلقائياً للتصعيد (INV-INC-03)
- **المدخلات:** `plan_template_ref`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-INC-CONTINGENCY-ACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** قائد الحادثة بسلطة صريحة لتفعيل الاستمرارية؛ الشروط: tenant match; أمر صريح دائماً (INV-INC-03)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-INC-ACTIVATE-CONTINGENCY` · `AGG-INCIDENT` · متطلبات: REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 · حالات استخدام: UC-142, UC-143, UC-144
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-INC-ACTIVATE-CONTINGENCY succeeds
  Given AGG-INCIDENT in state ASSESSED or CONTAINED or REPORTED or RESOLVED or RESPONDING and every guard holds
  When قائد الحادثة بسلطة صريحة لتفعيل الاستمرارية sends CMD-INC-ACTIVATE-CONTINGENCY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-INC-CONTINGENCY-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-INC-ACTIVATE-CONTINGENCY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-INC-ACTIVATE-CONTINGENCY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INCIDENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: حالات لا يسمح منها الأمر |
    | PLAN_LINK_INVALID | 422 | لم يتحقق الشرط: سلطة؛ ينشئ/يربط Plan (SLC-08، plan_kind=CONTINGENCY، triggered_by=هذه الحادثة — CR-60)؛ أمر صريح دائماً، ليس أثراً تلقائياً للتصعيد (INV-INC-03) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: plan_template_ref |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-INC-ASSESS — تقييم الحادثة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | مقيّم الحادثة | `POST /api/v1/operations/incidents/{id}/actions/assess` | POL-INC-ASSESS |

**القصة:** بصفتي **مقيّم الحادثة**، أريد **تقييم الحادثة**، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشروط المسبقة:** الحالة الحالية ∈ {REPORTED}؛ severity ∈ {MINOR,MAJOR,EMERGENCY,CRISIS}؛ affected_scope_refs؛ مقيّم مخوَّل
- **المدخلات:** `severity`!: enum(MINOR, `affected_scope_refs`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ASSESSED؛ الحدث EVT-INC-ASSESSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** مقيّم الحادثة؛ الشروط: tenant match; affected_scope_refs visible to actor؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-INC-ASSESS` · `AGG-INCIDENT` · متطلبات: REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 · حالات استخدام: UC-142, UC-143, UC-144
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-INC-ASSESS succeeds
  Given AGG-INCIDENT in state REPORTED and every guard holds
  When مقيّم الحادثة sends CMD-INC-ASSESS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ASSESSED
  And EVT-INC-ASSESSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-INC-ASSESS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-INC-ASSESS لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INCIDENT_INVALID | 422 | لم يتحقق الشرط: severity ∈ {MINOR,MAJOR,EMERGENCY,CRISIS}؛ affected_scope_refs؛ مقيّم مخوَّل |
    | INCIDENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ASSESSED, CONTAINED, RESOLVED, RESPONDING |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: severity, affected_scope_refs |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-INC-CANCEL — إلغاء الحادثة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) | `POST /api/v1/operations/incidents/{id}/actions/cancel` | POL-INC-CANCEL |

**القصة:** بصفتي **أي مُبلِّغ مخوَّل (تبليغ، إلغاء)**، أريد **إلغاء الحادثة**، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشروط المسبقة:** الحالة الحالية ∈ {REPORTED}؛ سبب (إنذار كاذب)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-INC-CANCELLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** أي مُبلِّغ مخوَّل (تبليغ، إلغاء)؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-INC-CANCEL` · `AGG-INCIDENT` · متطلبات: REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 · حالات استخدام: UC-142, UC-143, UC-144
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-INC-CANCEL succeeds
  Given AGG-INCIDENT in state REPORTED and every guard holds
  When أي مُبلِّغ مخوَّل sends CMD-INC-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-INC-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-INC-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-INC-CANCEL لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INCIDENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ASSESSED, CONTAINED, RESOLVED, RESPONDING |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-INC-CLOSE — إغلاق الحادثة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | قائد الحادثة | `POST /api/v1/operations/incidents/{id}/actions/close` | POL-INC-CLOSE |

**القصة:** بصفتي **قائد الحادثة**، أريد **إغلاق الحادثة**، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشروط المسبقة:** الحالة الحالية ∈ {RESOLVED}؛ ملاحظة إغلاق؛ after_action_ref اختياري (كائن معرفة، SLC-12 — R3-Q5)
- **المدخلات:** `closing_note`!: string, `after_action_ref`: urn — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-INC-CLOSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** قائد الحادثة؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-INC-CLOSE` · `AGG-INCIDENT` · متطلبات: REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 · حالات استخدام: UC-142, UC-143, UC-144
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-INC-CLOSE succeeds
  Given AGG-INCIDENT in state RESOLVED and every guard holds
  When قائد الحادثة sends CMD-INC-CLOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-INC-CLOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-INC-CLOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-INC-CLOSE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INCIDENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ASSESSED, CONTAINED, REPORTED, RESPONDING |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: closing_note |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-INC-CONTAIN — احتواء الحادثة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | قائد الحادثة | `POST /api/v1/operations/incidents/{id}/actions/contain` | POL-INC-CONTAIN |

**القصة:** بصفتي **قائد الحادثة**، أريد **احتواء الحادثة**، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشروط المسبقة:** الحالة الحالية ∈ {RESPONDING}؛ القائد يؤكد الاحتواء؛ ملاحظة احتواء
- **المدخلات:** `containment_note`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CONTAINED؛ الحدث EVT-INC-CONTAINED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** قائد الحادثة؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-INC-CONTAIN` · `AGG-INCIDENT` · متطلبات: REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 · حالات استخدام: UC-142, UC-143, UC-144
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-INC-CONTAIN succeeds
  Given AGG-INCIDENT in state RESPONDING and every guard holds
  When قائد الحادثة sends CMD-INC-CONTAIN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CONTAINED
  And EVT-INC-CONTAINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-INC-CONTAIN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-INC-CONTAIN لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INCIDENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ASSESSED, CONTAINED, REPORTED, RESOLVED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: containment_note |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-INC-DE-ESCALATE — خفض خطورة الحادثة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | قائد الحادثة بسلطة صريحة | `POST /api/v1/operations/incidents/{id}/actions/de-escalate` | POL-INC-DE-ESCALATE |

**القصة:** بصفتي **قائد الحادثة بسلطة صريحة**، أريد **خفض خطورة الحادثة**، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشروط المسبقة:** الحالة الحالية ∈ {ASSESSED, CONTAINED, REPORTED, RESOLVED, RESPONDING}؛ سلطة؛ سبب؛ new_severity أدنى بمستوى واحد كحد أقصى (INV-INC-01)
- **المدخلات:** `reason`!: string, `new_severity`!: enum(MINOR — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-INC-DE-ESCALATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** قائد الحادثة بسلطة صريحة؛ الشروط: tenant match; new_severity أدنى بمستوى واحد كحد أقصى (INV-INC-01)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-INC-DE-ESCALATE` · `AGG-INCIDENT` · متطلبات: REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 · حالات استخدام: UC-142, UC-143, UC-144
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-INC-DE-ESCALATE succeeds
  Given AGG-INCIDENT in state ASSESSED or CONTAINED or REPORTED or RESOLVED or RESPONDING and every guard holds
  When قائد الحادثة بسلطة صريحة sends CMD-INC-DE-ESCALATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-INC-DE-ESCALATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-INC-DE-ESCALATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-INC-DE-ESCALATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INCIDENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: حالات لا يسمح منها الأمر |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason, new_severity |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-INC-DISPATCH-RESPONSE — توجيه الاستجابة لـالحادثة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | قائد الحادثة | `POST /api/v1/operations/incidents/{id}/actions/dispatch-response` | POL-INC-DISPATCH-RESPONSE |

**القصة:** بصفتي **قائد الحادثة**، أريد **توجيه الاستجابة لـالحادثة**، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشروط المسبقة:** الحالة الحالية ∈ {ASSESSED}؛ commander؛ ≥ 1 response_task_ref (مهام SLC-03 مرتبطة عبر incident_ref — CR-61)
- **المدخلات:** `commander`!: urn, `response_task_refs`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← RESPONDING؛ الحدث EVT-INC-RESPONSE-DISPATCHED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** قائد الحادثة؛ الشروط: tenant match; commander authorized in scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-INC-DISPATCH-RESPONSE` · `AGG-INCIDENT` · متطلبات: REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 · حالات استخدام: UC-142, UC-143, UC-144
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-INC-DISPATCH-RESPONSE succeeds
  Given AGG-INCIDENT in state ASSESSED and every guard holds
  When قائد الحادثة sends CMD-INC-DISPATCH-RESPONSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RESPONDING
  And EVT-INC-RESPONSE-DISPATCHED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-INC-DISPATCH-RESPONSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-INC-DISPATCH-RESPONSE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INCIDENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CONTAINED, REPORTED, RESOLVED, RESPONDING |
    | RESPONSE_REQUIRED | 422 | لم يتحقق الشرط: commander؛ ≥ 1 response_task_ref (مهام SLC-03 مرتبطة عبر incident_ref — CR-61) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: commander, response_task_refs |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-INC-ESCALATE — تصعيد الحادثة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | قائد الحادثة | `POST /api/v1/operations/incidents/{id}/actions/escalate` | POL-INC-ESCALATE |

**القصة:** بصفتي **قائد الحادثة**، أريد **تصعيد الحادثة**، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشروط المسبقة:** الحالة الحالية ∈ {ASSESSED, CONTAINED, REPORTED, RESOLVED, RESPONDING}؛ سبب؛ new_severity أعلى من الحالية فقط (INV-INC-01)؛ إشعار المستوى الأعلى
- **المدخلات:** `reason`!: string, `new_severity`!: enum(MINOR — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-INC-ESCALATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** قائد الحادثة؛ الشروط: tenant match; new_severity أعلى فقط (INV-INC-01)؛ فصل المهام: —؛ الالتزامات: audit; notify next authority level
- **الربط:** `CMD-INC-ESCALATE` · `AGG-INCIDENT` · متطلبات: REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 · حالات استخدام: UC-142, UC-143, UC-144
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-INC-ESCALATE succeeds
  Given AGG-INCIDENT in state ASSESSED or CONTAINED or REPORTED or RESOLVED or RESPONDING and every guard holds
  When قائد الحادثة sends CMD-INC-ESCALATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-INC-ESCALATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-INC-ESCALATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-INC-ESCALATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INCIDENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: حالات لا يسمح منها الأمر |
    | SEVERITY_MUST_INCREASE | 422 | لم يتحقق الشرط: سبب؛ new_severity أعلى من الحالية فقط (INV-INC-01)؛ إشعار المستوى الأعلى |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason, new_severity |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-INC-REPORT — الإبلاغ عن الحادثة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | أي مُبلِّغ مخوَّل (تبليغ، إلغاء) | `POST /api/v1/operations/incidents` | POL-INC-REPORT |

**القصة:** بصفتي **أي مُبلِّغ مخوَّل (تبليغ، إلغاء)**، أريد **الإبلاغ عن الحادثة**، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ category_ref (RD-HAZARD-CATEGORIES)؛ description؛ scope_refs ≥ 1؛ risk_ref اختياري (خطر تحقَّق)؛ severity ابتدائية MINOR؛ label ≥ تصنيف النطاق
- **المدخلات:** `category_ref`!: urn, `description`!: LocalizedName, `scope_refs`!: array, `risk_ref`: urn, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REPORTED؛ الحدث EVT-INC-REPORTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** أي مُبلِّغ مخوَّل (تبليغ، إلغاء)؛ الشروط: tenant match; scope_refs visible to actor؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-INC-REPORT` · `AGG-INCIDENT` · متطلبات: REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 · حالات استخدام: UC-142, UC-143, UC-144
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-INC-REPORT succeeds
  Given AGG-INCIDENT in state ∅ and every guard holds
  When أي مُبلِّغ مخوَّل sends CMD-INC-REPORT with a valid payload, a new Idempotency-Key
  Then the state becomes REPORTED
  And EVT-INC-REPORTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-INC-REPORT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-INC-REPORT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INCIDENT_INVALID | 422 | لم يتحقق الشرط: category_ref (RD-HAZARD-CATEGORIES)؛ description؛ scope_refs ≥ 1؛ risk_ref اختياري (خطر تحقَّق)؛ severity ابتدائية MINOR؛ label ≥ تصنيف النطاق |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: category_ref, description, scope_refs, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-INC-RESOLVE — حل الحادثة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | قائد الحادثة | `POST /api/v1/operations/incidents/{id}/actions/resolve` | POL-INC-RESOLVE |

**القصة:** بصفتي **قائد الحادثة**، أريد **حل الحادثة**، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشروط المسبقة:** الحالة الحالية ∈ {CONTAINED}؛ كل مهام الاستجابة في حالة نهائية (INV-INC-02)؛ ملاحظة حل
- **المدخلات:** `resolution_note`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← RESOLVED؛ الحدث EVT-INC-RESOLVED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** قائد الحادثة؛ الشروط: tenant match; كل مهام الاستجابة نهائية (INV-INC-02)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-INC-RESOLVE` · `AGG-INCIDENT` · متطلبات: REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 · حالات استخدام: UC-142, UC-143, UC-144
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-INC-RESOLVE succeeds
  Given AGG-INCIDENT in state CONTAINED and every guard holds
  When قائد الحادثة sends CMD-INC-RESOLVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RESOLVED
  And EVT-INC-RESOLVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-INC-RESOLVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-INC-RESOLVE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INCIDENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ASSESSED, REPORTED, RESOLVED, RESPONDING |
    | RESPONSE_TASKS_OPEN | 422 | لم يتحقق الشرط: كل مهام الاستجابة في حالة نهائية (INV-INC-02)؛ ملاحظة حل |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: resolution_note |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-INCIDENT-01 — تلقائي: response SLA elapsed without dispatch (الحادثة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | REPORTED, ASSESSED | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «response SLA elapsed without dispatch»، أريد تحديث **الحادثة** دون تغيير حالته، لكي يتحقق غرض الحادثة: تتبّع حادثة فعلية من التبليغ حتى الإغلاق، بما فيها تصعيدها لطارئ/أزمة والاستجابة والتعافي

- **الشرط:** المجدول؛ SLA حسب severity، موسوم 'تُعاد معايرته بعد Pilot R1/R2' (RSK-028)
- **المخرجات:** الحدث EVT-INC-SLA-BREACHED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-INCIDENT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-Q-INC-GET — جلب: Incident بنطاقه المرئي للطالب

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | allowed_scope | `GET /api/v1/operations/incidents/{incident_id}` | POL-INC-GET |

**القصة:** بصفتي **allowed_scope**، أريد **جلب Incident بنطاقه المرئي للطالب**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter incidents by category, severity, status and scope, restricted to the caller's visible scope

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Incident بنطاقه المرئي للطالب
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-INC-GET` · `AGG-INCIDENT` · متطلبات: REQ-RCM-015
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-INC-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-INC-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-INC-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-INC-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC04-Q-INC-LIST — جلب: حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | allowed_scope | `GET /api/v1/operations/incidents` | POL-INC-LIST |

**القصة:** بصفتي **allowed_scope**، أريد **جلب حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter incidents by category, severity, status and scope, restricted to the caller's visible scope

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-INC-LIST` · `AGG-INCIDENT` · متطلبات: REQ-RCM-015
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-INC-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-INC-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-INC-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-INC-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC04-Q-INC-RECOVERY-STATUS — جلب: تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء الحادثة (RTO/RPO تقديرية)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | القائد؛ مالك الاستمرارية | `GET /api/v1/operations/incidents/{incident_id}/recovery-status` | POL-INC-RECOVERY-STATUS |

**القصة:** بصفتي **القائد؛ مالك الاستمرارية**، أريد **جلب تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء الحادثة (RTO/RPO تقديرية)**، لكي يتحقق المتطلب: The system shall compute an incident's recovery status from its linked contingency plan's task completion against the incident's start time, as an estimate, without a separate recovery state machine

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء الحادثة (RTO/RPO تقديرية)؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** القائد؛ مالك الاستمرارية؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-INC-RECOVERY-STATUS` · `AGG-INCIDENT` · متطلبات: REQ-RCM-016
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-INC-RECOVERY-STATUS returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-INC-RECOVERY-STATUS with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-INC-RECOVERY-STATUS is denied
  Given the policy denies the caller
  When the caller sends QRY-INC-RECOVERY-STATUS
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-NOTIFICATION — الإشعار (Notification)

`03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md` · SLC-06 · الحالات: QUEUED, SENT → READ, FAILED, WITHHELD, EXPIRED

#### US-BC04-NTF-MARK-READ — تعليم الإشعار كمقروء

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | recipient | `POST /api/v1/operations/notifications/{id}/actions/mark-read` | POL-NTF-MARK-READ |

**القصة:** بصفتي **recipient**، أريد **تعليم الإشعار كمقروء**، لكي يتحقق غرض الإشعار: رسالة لمستلم واحد؛ الحمولة مرجع فقط

- **الشروط المسبقة:** الحالة الحالية ∈ {SENT}؛ actor = recipient; content fetched through normal authorized query
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← READ؛ الحدث EVT-NTF-READ؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** recipient؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-NTF-MARK-READ` · `AGG-NOTIFICATION` · متطلبات: REQ-COM-001, REQ-COM-002 · حالات استخدام: UC-099
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-NTF-MARK-READ succeeds
  Given AGG-NOTIFICATION in state SENT and every guard holds
  When recipient sends CMD-NTF-MARK-READ with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes READ
  And EVT-NTF-READ is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-NTF-MARK-READ is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-NTF-MARK-READ لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | NOTIFICATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, FAILED, QUEUED, READ, WITHHELD |
    | NOT_RECIPIENT | 422 | لم يتحقق الشرط: actor = recipient; content fetched through normal authorized query |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-NOTIFICATION-01 — تلقائي: notifiable event for recipient (الإشعار)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ∅ | QUEUED |

**القصة:** بصفتي **النظام**، عند «notifiable event for recipient»، أريد نقل **الإشعار** إلى QUEUED، لكي يتحقق غرض الإشعار: رسالة لمستلم واحد؛ الحمولة مرجع فقط

- **الشرط:** recipient ACTIVE; recipient authorized for the referenced object at enqueue time
- **المخرجات:** الحدث EVT-NTF-QUEUED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-NOTIFICATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-NOTIFICATION-02 — تلقائي: delivered to channel (الإشعار)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | QUEUED | SENT |

**القصة:** بصفتي **النظام**، عند «delivered to channel»، أريد نقل **الإشعار** إلى SENT، لكي يتحقق غرض الإشعار: رسالة لمستلم واحد؛ الحمولة مرجع فقط

- **الشرط:** re-check authorization at delivery (security_version); push payload = reference + classification-safe title template
- **المخرجات:** الحدث EVT-NTF-SENT؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-NOTIFICATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-NOTIFICATION-03 — تلقائي: recipient no longer authorized at delivery (الإشعار)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | QUEUED | WITHHELD |

**القصة:** بصفتي **النظام**، عند «recipient no longer authorized at delivery»، أريد نقل **الإشعار** إلى WITHHELD، لكي يتحقق غرض الإشعار: رسالة لمستلم واحد؛ الحمولة مرجع فقط

- **الشرط:** re-check failed
- **المخرجات:** الحدث EVT-NTF-WITHHELD؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-NOTIFICATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-NOTIFICATION-04 — تلقائي: delivery failed after retries (الإشعار)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | QUEUED | FAILED |

**القصة:** بصفتي **النظام**، عند «delivery failed after retries»، أريد نقل **الإشعار** إلى FAILED، لكي يتحقق غرض الإشعار: رسالة لمستلم واحد؛ الحمولة مرجع فقط

- **الشرط:** 5 attempts with exponential backoff; in-app copy remains
- **المخرجات:** الحدث EVT-NTF-FAILED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-NOTIFICATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-NOTIFICATION-05 — تلقائي: TTL (30 d) elapsed (الإشعار)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | QUEUED, SENT | EXPIRED |

**القصة:** بصفتي **النظام**، عند «TTL (30 d) elapsed»، أريد نقل **الإشعار** إلى EXPIRED، لكي يتحقق غرض الإشعار: رسالة لمستلم واحد؛ الحمولة مرجع فقط

- **الشرط:** scheduler
- **المخرجات:** الحدث EVT-NTF-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-NOTIFICATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-Q-NTF-INBOX — جلب: My notifications (references + templates)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | recipient | `GET /api/v1/operations/notifications` | POL-NTF-INBOX |

**القصة:** بصفتي **recipient**، أريد **جلب My notifications (references + templates)**، لكي يتحقق المتطلب: When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authorized recipients according to their preferences

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** My notifications (references + templates)؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** recipient؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-NTF-INBOX` · `AGG-NOTIFICATION` · متطلبات: REQ-COM-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-NTF-INBOX returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-NTF-INBOX with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-NTF-INBOX is denied
  Given the policy denies the caller
  When the caller sends QRY-NTF-INBOX
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-OUTCOME-TRACKER — متتبّع النتائج (Outcome Tracker)

`03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md` · SLC-08 · الحالات: ACTIVE → CLOSED

#### US-BC04-OUT-CORRECT — تصحيح متتبّع النتائج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Planner / owner | `POST /api/v1/operations/outcome-trackers/{id}/actions/correct` | POL-OUT-CORRECT |

**القصة:** بصفتي **Planner / owner**، أريد **تصحيح متتبّع النتائج**، لكي يتحقق غرض متتبّع النتائج: سلسلة قياسات لنتيجة خطة مقابل هدفها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ corrects a measurement: previous record closed (recorded_to), corrected record added — no overwrite
- **المدخلات:** `measurement_id`!: string, `value`!: number, `unit`!: string, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-OUT-MEASUREMENT-CORRECTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner / owner (record, correct)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-OUT-CORRECT` · `AGG-OUTCOME-TRACKER` · متطلبات: REQ-OPS-013 · حالات استخدام: UC-101
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-OUT-CORRECT succeeds
  Given AGG-OUTCOME-TRACKER in state ACTIVE and every guard holds
  When Planner / owner sends CMD-OUT-CORRECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-OUT-MEASUREMENT-CORRECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-OUT-CORRECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-OUT-CORRECT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OUTCOME_TRACKER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: measurement_id, value, unit, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-OUT-RECORD — تسجيل متتبّع النتائج

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Planner / owner | `POST /api/v1/operations/outcome-trackers/{id}/actions/record` | POL-OUT-RECORD |

**القصة:** بصفتي **Planner / owner**، أريد **تسجيل متتبّع النتائج**، لكي يتحقق غرض متتبّع النتائج: سلسلة قياسات لنتيجة خطة مقابل هدفها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ value with unit convertible to metric unit (UCUM); measured_at; source = manual \| task result \| observation ref
- **المدخلات:** `value`!: number, `unit`!: string, `measured_at`!: date-time, `source`!: enum(manual, `source_ref`: urn, `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-OUT-MEASURED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner / owner (record, correct)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-OUT-RECORD` · `AGG-OUTCOME-TRACKER` · متطلبات: REQ-OPS-013 · حالات استخدام: UC-101
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-OUT-RECORD succeeds
  Given AGG-OUTCOME-TRACKER in state ACTIVE and every guard holds
  When Planner / owner sends CMD-OUT-RECORD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-OUT-MEASURED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-OUT-RECORD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-OUT-RECORD لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MEASUREMENT_INVALID | 422 | لم يتحقق الشرط: value with unit convertible to metric unit (UCUM); measured_at; source = manual \| task result \| observation ref |
    | OUTCOME_TRACKER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: value, unit, measured_at, source |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-OUTCOME-TRACKER-01 — تلقائي: outcome baselined (متتبّع النتائج)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ∅ | ACTIVE |

**القصة:** بصفتي **النظام**، عند «outcome baselined»، أريد نقل **متتبّع النتائج** إلى ACTIVE، لكي يتحقق غرض متتبّع النتائج: سلسلة قياسات لنتيجة خطة مقابل هدفها

- **الشرط:** one tracker per (plan, outcome id); target copied from baseline
- **المخرجات:** الحدث EVT-OUT-TRACKER-CREATED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-OUTCOME-TRACKER` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-OUTCOME-TRACKER-02 — تلقائي: target changed by new baseline (متتبّع النتائج)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | ACTIVE | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «target changed by new baseline»، أريد تحديث **متتبّع النتائج** دون تغيير حالته، لكي يتحقق غرض متتبّع النتائج: سلسلة قياسات لنتيجة خطة مقابل هدفها

- **الشرط:** target history appended (valid time = baseline time)
- **المخرجات:** الحدث EVT-OUT-TARGET-CHANGED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-OUTCOME-TRACKER` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-OUTCOME-TRACKER-03 — تلقائي: plan closed or cancelled (متتبّع النتائج)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ACTIVE | CLOSED |

**القصة:** بصفتي **النظام**، عند «plan closed or cancelled»، أريد نقل **متتبّع النتائج** إلى CLOSED، لكي يتحقق غرض متتبّع النتائج: سلسلة قياسات لنتيجة خطة مقابل هدفها

- **الشرط:** system
- **المخرجات:** الحدث EVT-OUT-TRACKER-CLOSED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-OUTCOME-TRACKER` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-Q-OUT-SERIES — جلب: Measurement series as known_at

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | label rule | `GET /api/v1/operations/plans/{plan_id}/outcomes/{outcome_id}/measurements` | POL-OUT-SERIES |

**القصة:** بصفتي **label rule**، أريد **جلب Measurement series as known_at**، لكي يتحقق المتطلب: The system shall record measurements of plan outcomes over time against their targets

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Measurement series as known_at؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-OUT-SERIES` · `AGG-OUTCOME-TRACKER` · متطلبات: REQ-OPS-013
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-OUT-SERIES returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-OUT-SERIES with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-OUT-SERIES is denied
  Given the policy denies the caller
  When the caller sends QRY-OUT-SERIES
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-PLAN — الخطة (Plan (identity))

`03-domain/contexts/BC04/aggregates/AGG-PLAN.md` · SLC-08 · الحالات: DRAFT, ACTIVE, SUSPENDED, COMPLETED → CLOSED, CANCELLED

#### US-BC04-PLN-CANCEL — إلغاء الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | authority | `POST /api/v1/operations/plans/{id}/actions/cancel` | POL-PLN-CANCEL |

**القصة:** بصفتي **authority**، أريد **إلغاء الخطة**، لكي يتحقق غرض الخطة: هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, DRAFT, SUSPENDED}؛ authority; reason; open tasks cancelled
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-PLN-CANCELLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLN-CANCEL` · `AGG-PLAN` · متطلبات: REQ-OPS-001, REQ-OPS-002, REQ-OPS-003 · حالات استخدام: UC-033, UC-035, UC-036
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLN-CANCEL succeeds
  Given AGG-PLAN in state ACTIVE or DRAFT or SUSPENDED and every guard holds
  When authority sends CMD-PLN-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-PLN-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLN-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLN-CANCEL لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, COMPLETED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLN-CLOSE — إغلاق الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Planner / owner | `POST /api/v1/operations/plans/{id}/actions/close` | POL-PLN-CLOSE |

**القصة:** بصفتي **Planner / owner**، أريد **إغلاق الخطة**، لكي يتحقق غرض الخطة: هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها

- **الشروط المسبقة:** الحالة الحالية ∈ {COMPLETED}؛ after-action notes (optional in R1); outcome trackers closed
- **المدخلات:** `after_action_notes`: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-PLN-CLOSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLN-CLOSE` · `AGG-PLAN` · متطلبات: REQ-OPS-001, REQ-OPS-002, REQ-OPS-003 · حالات استخدام: UC-033, UC-035, UC-036
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLN-CLOSE succeeds
  Given AGG-PLAN in state COMPLETED and every guard holds
  When Planner / owner sends CMD-PLN-CLOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-PLN-CLOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLN-CLOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLN-CLOSE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CANCELLED, CLOSED, DRAFT, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLN-COMPLETE — إكمال الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Planner / owner | `POST /api/v1/operations/plans/{id}/actions/complete` | POL-PLN-COMPLETE |

**القصة:** بصفتي **Planner / owner**، أريد **إكمال الخطة**، لكي يتحقق غرض الخطة: هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ all plan tasks terminal; every outcome has ≥ 1 measurement
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← COMPLETED؛ الحدث EVT-PLN-COMPLETED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLN-COMPLETE` · `AGG-PLAN` · متطلبات: REQ-OPS-001, REQ-OPS-002, REQ-OPS-003 · حالات استخدام: UC-033, UC-035, UC-036
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLN-COMPLETE succeeds
  Given AGG-PLAN in state ACTIVE and every guard holds
  When Planner / owner sends CMD-PLN-COMPLETE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes COMPLETED
  And EVT-PLN-COMPLETED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLN-COMPLETE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLN-COMPLETE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, COMPLETED, DRAFT, SUSPENDED |
    | PLAN_NOT_COMPLETABLE | 422 | لم يتحقق الشرط: all plan tasks terminal; every outcome has ≥ 1 measurement |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLN-CREATE — إنشاء الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Planner / owner | `POST /api/v1/operations/plans` | POL-PLN-CREATE |

**القصة:** بصفتي **Planner / owner**، أريد **إنشاء الخطة**، لكي يتحقق غرض الخطة: هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ title; owner; org scope; implements ≥ 1 decision (RECORDED) or objective (REQ-OPS-002), or for plan_kind=CONTINGENCY a risk_ref or incident_ref trigger (CR-60, SLC-17); label ≥ implemented decisions or triggering scope's label
- **المدخلات:** `title`!: LocalizedName, `owner`!: urn, `org_scope`!: urn, `implements`: array, `plan_kind`!: enum(OPERATIONS, `triggered_by`: urn, `window`!: Interval, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-PLN-CREATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLN-CREATE` · `AGG-PLAN` · متطلبات: REQ-OPS-001, REQ-OPS-002, REQ-OPS-003 · حالات استخدام: UC-033, UC-035, UC-036
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLN-CREATE succeeds
  Given AGG-PLAN in state ∅ and every guard holds
  When Planner / owner sends CMD-PLN-CREATE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-PLN-CREATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLN-CREATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLN-CREATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_INVALID | 422 | لم يتحقق الشرط: title; owner; org scope; implements ≥ 1 decision (RECORDED) or objective (REQ-OPS-002), or for plan_kind=CONTINGENCY a risk_ref or incident_ref trigger (CR-60, SLC-17); label ≥ implemented decisions or triggering scope's label |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: title, owner, org_scope, plan_kind, window, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLN-RECLASSIFY — إعادة تصنيف الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Security Officer | `POST /api/v1/operations/plans/{id}/actions/reclassify` | POL-PLN-RECLASSIFY |

**القصة:** بصفتي **Security Officer**، أريد **إعادة تصنيف الخطة**، لكي يتحقق غرض الخطة: هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, DRAFT, SUSPENDED}؛ authority; new label ≥ implemented decisions; assignees without clearance → reassignment required
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-PLN-RECLASSIFIED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLN-RECLASSIFY` · `AGG-PLAN` · متطلبات: REQ-OPS-001, REQ-OPS-002, REQ-OPS-003 · حالات استخدام: UC-033, UC-035, UC-036
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLN-RECLASSIFY succeeds
  Given AGG-PLAN in state ACTIVE or DRAFT or SUSPENDED and every guard holds
  When Security Officer sends CMD-PLN-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-PLN-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLN-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLN-RECLASSIFY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority; new label ≥ implemented decisions; assignees without clearance → reassignment required |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, COMPLETED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLN-RESUME — استئناف الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Planner / owner | `POST /api/v1/operations/plans/{id}/actions/resume` | POL-PLN-RESUME |

**القصة:** بصفتي **Planner / owner**، أريد **استئناف الخطة**، لكي يتحقق غرض الخطة: هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها

- **الشروط المسبقة:** الحالة الحالية ∈ {SUSPENDED}؛ reason; tasks unsuspended
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-PLN-RESUMED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLN-RESUME` · `AGG-PLAN` · متطلبات: REQ-OPS-001, REQ-OPS-002, REQ-OPS-003 · حالات استخدام: UC-033, UC-035, UC-036
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLN-RESUME succeeds
  Given AGG-PLAN in state SUSPENDED and every guard holds
  When Planner / owner sends CMD-PLN-RESUME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-PLN-RESUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLN-RESUME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLN-RESUME لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CANCELLED, CLOSED, COMPLETED, DRAFT |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLN-SUSPEND — تعليق الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Planner / owner | `POST /api/v1/operations/plans/{id}/actions/suspend` | POL-PLN-SUSPEND |

**القصة:** بصفتي **Planner / owner**، أريد **تعليق الخطة**، لكي يتحقق غرض الخطة: هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ reason; open tasks suspended (flag, INV-TASK-06)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← SUSPENDED؛ الحدث EVT-PLN-SUSPENDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLN-SUSPEND` · `AGG-PLAN` · متطلبات: REQ-OPS-001, REQ-OPS-002, REQ-OPS-003 · حالات استخدام: UC-033, UC-035, UC-036
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLN-SUSPEND succeeds
  Given AGG-PLAN in state ACTIVE and every guard holds
  When Planner / owner sends CMD-PLN-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUSPENDED
  And EVT-PLN-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLN-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLN-SUSPEND لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, COMPLETED, DRAFT, SUSPENDED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-PLAN-01 — تلقائي: first version baselined (الخطة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | DRAFT | ACTIVE |

**القصة:** بصفتي **النظام**، عند «first version baselined»، أريد نقل **الخطة** إلى ACTIVE، لكي يتحقق غرض الخطة: هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها

- **الشرط:** EVT-PLV-BASELINED for this plan
- **المخرجات:** الحدث EVT-PLN-ACTIVATED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PLAN` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-PLAN-02 — تلقائي: implemented decision annulled or superseded (الخطة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | ACTIVE, SUSPENDED | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «implemented decision annulled or superseded»، أريد تحديث **الخطة** دون تغيير حالته، لكي يتحقق غرض الخطة: هوية الخطة ودورة حياتها؛ المحتوى في إصداراتها

- **الشرط:** plan flagged for review (no automatic change)
- **المخرجات:** الحدث EVT-PLN-REVIEW-FLAGGED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PLAN` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-Q-PLN-GET — جلب: Plan with current baseline, draft (if any), implemented decisions

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | label rule | `GET /api/v1/operations/plans/{plan_id}` | POL-PLN-GET |

**القصة:** بصفتي **label rule**، أريد **جلب Plan with current baseline, draft (if any), implemented decisions**، لكي يتحقق المتطلب: The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities, milestones, resources, schedule, dependencies and metrics

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Plan with current baseline, draft (if any), implemented decisions
- **الصلاحية:** label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-PLN-GET` · `AGG-PLAN` · متطلبات: REQ-OPS-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-PLN-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-PLN-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-PLN-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-PLN-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC04-Q-PLN-PROGRESS — جلب: Tasks by activity and state, milestones, outcome progress vs targets

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | label rule; visible tasks only | `GET /api/v1/operations/plans/{plan_id}/progress` | POL-PLN-PROGRESS |

**القصة:** بصفتي **label rule; visible tasks only**، أريد **جلب Tasks by activity and state, milestones, outcome progress vs targets**، لكي يتحقق المتطلب: The system shall record measurements of plan outcomes over time against their targets

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Tasks by activity and state, milestones, outcome progress vs targets؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** label rule; visible tasks only؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-PLN-PROGRESS` · `AGG-PLAN` · متطلبات: REQ-OPS-013
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-PLN-PROGRESS returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-PLN-PROGRESS with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-PLN-PROGRESS is denied
  Given the policy denies the caller
  When the caller sends QRY-PLN-PROGRESS
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-PLAN-VERSION — إصدار الخطة (Plan Version)

`03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md` · SLC-08 · الحالات: DRAFT, IN_REVIEW, BASELINED → SUPERSEDED, REJECTED, DISCARDED

#### US-BC04-PLV-AMEND-MINOR — تعديل طفيف على إصدار الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Planner | `POST /api/v1/operations/plan-versions/{id}/actions/amend-minor` | POL-PLV-AMEND-MINOR |

**القصة:** بصفتي **Planner**، أريد **تعديل طفيف على إصدار الخطة**، لكي يتحقق غرض إصدار الخطة: محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس

- **الشروط المسبقة:** الحالة الحالية ∈ {BASELINED}؛ only minor fields (descriptions, notes, attachments) per BRL-005; recorded as annotation, baseline content unchanged
- **المدخلات:** `annotations`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-PLV-MINOR-AMENDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLV-AMEND-MINOR` · `AGG-PLAN-VERSION` · متطلبات: REQ-OPS-001, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-014 · حالات استخدام: UC-033, UC-034, UC-035, UC-036, UC-044
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLV-AMEND-MINOR succeeds
  Given AGG-PLAN-VERSION in state BASELINED and every guard holds
  When Planner sends CMD-PLV-AMEND-MINOR with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-PLV-MINOR-AMENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLV-AMEND-MINOR is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLV-AMEND-MINOR لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MAJOR_CHANGE_REQUIRES_VERSION | 422 | لم يتحقق الشرط: only minor fields (descriptions, notes, attachments) per BRL-005; recorded as annotation, baseline content unchanged |
    | PLAN_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISCARDED, DRAFT, IN_REVIEW, REJECTED, SUPERSEDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: annotations |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLV-APPROVE — اعتماد إصدار الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | approver with plan-approval authority ≠ author | `POST /api/v1/operations/plan-versions/{id}/actions/approve` | POL-PLV-APPROVE |

**القصة:** بصفتي **approver with plan-approval authority ≠ author**، أريد **اعتماد إصدار الخطة**، لكي يتحقق غرض إصدار الخطة: محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس

- **الشروط المسبقة:** الحالة الحالية ∈ {IN_REVIEW}؛ approver ≠ author (REQ-OPS-005); AuthorityCheck(approver, plan-approval type, scope); previous BASELINED → SUPERSEDED in the same transaction; task synchronization started (SPEC-PLAN §3)
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← BASELINED؛ الحدث EVT-PLV-BASELINED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: approver ≠ author (REQ-OPS-005); AuthorityCheck plan-approval؛ الالتزامات: audit; mfa
- **الربط:** `CMD-PLV-APPROVE` · `AGG-PLAN-VERSION` · متطلبات: REQ-OPS-001, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-014 · حالات استخدام: UC-033, UC-034, UC-035, UC-036, UC-044
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLV-APPROVE succeeds
  Given AGG-PLAN-VERSION in state IN_REVIEW and every guard holds
  When approver with plan-approval authority ≠ author sends CMD-PLV-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes BASELINED
  And EVT-PLV-BASELINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLV-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLV-APPROVE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: BASELINED, DISCARDED, DRAFT, REJECTED, SUPERSEDED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author (REQ-OPS-005); AuthorityCheck plan-approval |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLV-DISCARD — تجاهل مسودة إصدار الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Planner | `POST /api/v1/operations/plan-versions/{id}/actions/discard` | POL-PLV-DISCARD |

**القصة:** بصفتي **Planner**، أريد **تجاهل مسودة إصدار الخطة**، لكي يتحقق غرض إصدار الخطة: محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ author; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DISCARDED؛ الحدث EVT-PLV-DISCARDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLV-DISCARD` · `AGG-PLAN-VERSION` · متطلبات: REQ-OPS-001, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-014 · حالات استخدام: UC-033, UC-034, UC-035, UC-036, UC-044
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLV-DISCARD succeeds
  Given AGG-PLAN-VERSION in state DRAFT and every guard holds
  When Planner sends CMD-PLV-DISCARD with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISCARDED
  And EVT-PLV-DISCARDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLV-DISCARD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLV-DISCARD لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: BASELINED, DISCARDED, IN_REVIEW, REJECTED, SUPERSEDED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLV-DRAFT — إعداد مسودة إصدار الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Planner | `POST /api/v1/operations/plan-versions` | POL-PLV-DRAFT |

**القصة:** بصفتي **Planner**، أريد **إعداد مسودة إصدار الخطة**، لكي يتحقق غرض إصدار الخطة: محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ plan not CLOSED/CANCELLED; new or revision copying the BASELINED version (activity ids preserved); ≤ 1 DRAFT/IN_REVIEW per plan
- **المدخلات:** `plan`!: urn, `based_on`: integer — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-PLV-DRAFTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLV-DRAFT` · `AGG-PLAN-VERSION` · متطلبات: REQ-OPS-001, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-014 · حالات استخدام: UC-033, UC-034, UC-035, UC-036, UC-044
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLV-DRAFT succeeds
  Given AGG-PLAN-VERSION in state ∅ and every guard holds
  When Planner sends CMD-PLV-DRAFT with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-PLV-DRAFTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLV-DRAFT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLV-DRAFT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DRAFT_EXISTS | 422 | لم يتحقق الشرط: plan not CLOSED/CANCELLED; new or revision copying the BASELINED version (activity ids preserved); ≤ 1 DRAFT/IN_REVIEW per plan |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: plan |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLV-EDIT — تعديل إصدار الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Planner | `POST /api/v1/operations/plan-versions/{id}/actions/edit` | POL-PLV-EDIT |

**القصة:** بصفتي **Planner**، أريد **تعديل إصدار الخطة**، لكي يتحقق غرض إصدار الخطة: محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ objectives, outcomes (metric, unit, target, due), phases, activities (stable ids, task_generating flag, task type), milestones, schedule within plan window, acyclic dependencies
- **المدخلات:** `objectives`!: array, `outcomes`!: array, `constraints`: array, `assumptions`: array, `phases`!: array, `activities`!: array, `milestones`: array, `dependencies`: array, `resource_notes`: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-PLV-EDITED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLV-EDIT` · `AGG-PLAN-VERSION` · متطلبات: REQ-OPS-001, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-014 · حالات استخدام: UC-033, UC-034, UC-035, UC-036, UC-044
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLV-EDIT succeeds
  Given AGG-PLAN-VERSION in state DRAFT and every guard holds
  When Planner sends CMD-PLV-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-PLV-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLV-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLV-EDIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_VERSION_INVALID | 422 | لم يتحقق الشرط: objectives, outcomes (metric, unit, target, due), phases, activities (stable ids, task_generating flag, task type), milestones, schedule within plan window, acyclic dependencies |
    | PLAN_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: BASELINED, DISCARDED, IN_REVIEW, REJECTED, SUPERSEDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: objectives, outcomes, phases, activities |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLV-REJECT — رفض إصدار الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | approver with plan-approval authority ≠ author | `POST /api/v1/operations/plan-versions/{id}/actions/reject` | POL-PLV-REJECT |

**القصة:** بصفتي **approver with plan-approval authority ≠ author**، أريد **رفض إصدار الخطة**، لكي يتحقق غرض إصدار الخطة: محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس

- **الشروط المسبقة:** الحالة الحالية ∈ {IN_REVIEW}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-PLV-REJECTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLV-REJECT` · `AGG-PLAN-VERSION` · متطلبات: REQ-OPS-001, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-014 · حالات استخدام: UC-033, UC-034, UC-035, UC-036, UC-044
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLV-REJECT succeeds
  Given AGG-PLAN-VERSION in state IN_REVIEW and every guard holds
  When approver with plan-approval authority ≠ author sends CMD-PLV-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-PLV-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLV-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLV-REJECT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: BASELINED, DISCARDED, DRAFT, REJECTED, SUPERSEDED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLV-RETURN — إعادة إصدار الخطة للمراجعة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | approver with plan-approval authority ≠ author | `POST /api/v1/operations/plan-versions/{id}/actions/return` | POL-PLV-RETURN |

**القصة:** بصفتي **approver with plan-approval authority ≠ author**، أريد **إعادة إصدار الخطة للمراجعة**، لكي يتحقق غرض إصدار الخطة: محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس

- **الشروط المسبقة:** الحالة الحالية ∈ {IN_REVIEW}؛ reviewer; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-PLV-RETURNED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLV-RETURN` · `AGG-PLAN-VERSION` · متطلبات: REQ-OPS-001, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-014 · حالات استخدام: UC-033, UC-034, UC-035, UC-036, UC-044
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLV-RETURN succeeds
  Given AGG-PLAN-VERSION in state IN_REVIEW and every guard holds
  When approver with plan-approval authority ≠ author sends CMD-PLV-RETURN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DRAFT
  And EVT-PLV-RETURNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLV-RETURN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLV-RETURN لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: BASELINED, DISCARDED, DRAFT, REJECTED, SUPERSEDED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-PLV-SUBMIT — تقديم إصدار الخطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Planner | `POST /api/v1/operations/plan-versions/{id}/actions/submit` | POL-PLV-SUBMIT |

**القصة:** بصفتي **Planner**، أريد **تقديم إصدار الخطة**، لكي يتحقق غرض إصدار الخطة: محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ complete per REQ-OPS-001; change classification computed vs current baseline (major/minor, BRL-005)
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← IN_REVIEW؛ الحدث EVT-PLV-SUBMITTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)؛ الشروط: tenant match; object visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PLV-SUBMIT` · `AGG-PLAN-VERSION` · متطلبات: REQ-OPS-001, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-014 · حالات استخدام: UC-033, UC-034, UC-035, UC-036, UC-044
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PLV-SUBMIT succeeds
  Given AGG-PLAN-VERSION in state DRAFT and every guard holds
  When Planner sends CMD-PLV-SUBMIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_REVIEW
  And EVT-PLV-SUBMITTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PLV-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PLV-SUBMIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PLAN_VERSION_INCOMPLETE | 422 | لم يتحقق الشرط: complete per REQ-OPS-001; change classification computed vs current baseline (major/minor, BRL-005) |
    | PLAN_VERSION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: BASELINED, DISCARDED, IN_REVIEW, REJECTED, SUPERSEDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-PLAN-VERSION-01 — تلقائي: newer version baselined (إصدار الخطة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | BASELINED | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «newer version baselined»، أريد نقل **إصدار الخطة** إلى SUPERSEDED، لكي يتحقق غرض إصدار الخطة: محتوى الخطة: أهداف، نتائج، قيود، افتراضات، مراحل، أنشطة، معالم، جدول، اعتماديات، مقاييس

- **الشرط:** system
- **المخرجات:** الحدث EVT-PLV-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-PLAN-VERSION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-Q-PLV-DIFF — جلب: Diff vs baseline with major/minor classification and task synchronization preview

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | label rule | `GET /api/v1/operations/plans/{plan_id}/versions/{version}/diff` | POL-PLV-DIFF |

**القصة:** بصفتي **label rule**، أريد **جلب Diff vs baseline with major/minor classification and task synchronization preview**، لكي يتحقق المتطلب: When a major change is made to a baselined plan, the system shall create a new plan version that requires approval before it becomes effective

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Diff vs baseline with major/minor classification and task synchronization preview؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-PLV-DIFF` · `AGG-PLAN-VERSION` · متطلبات: REQ-OPS-004
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-PLV-DIFF returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-PLV-DIFF with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-PLV-DIFF is denied
  Given the policy denies the caller
  When the caller sends QRY-PLV-DIFF
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC04-Q-PLV-LIST — جلب: Versions with states and times

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | label rule | `GET /api/v1/operations/plans/{plan_id}/versions` | POL-PLV-LIST |

**القصة:** بصفتي **label rule**، أريد **جلب Versions with states and times**، لكي يتحقق المتطلب: When a plan is approved, the system shall create an immutable baseline of that plan version

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Versions with states and times؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-PLV-LIST` · `AGG-PLAN-VERSION` · متطلبات: REQ-OPS-003
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-PLV-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-PLV-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-PLV-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-PLV-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-RISK — الخطر (Risk)

`03-domain/contexts/BC04/aggregates/AGG-RISK.md` · SLC-17 · الحالات: IDENTIFIED, ASSESSED, TREATED → CLOSED

#### US-BC04-RIS-ASSESS — تقييم الخطر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | مقيّم (تقييم، إعادة تقييم) | `POST /api/v1/operations/risks/{id}/actions/assess` | POL-RIS-ASSESS |

**القصة:** بصفتي **مقيّم (تقييم، إعادة تقييم)**، أريد **تقييم الخطر**، لكي يتحقق غرض الخطر: تسجيل وتقييم ومعالجة مخاطر محتملة قبل وقوعها (استباقي، لا حادثة فعلية)

- **الشروط المسبقة:** الحالة الحالية ∈ {IDENTIFIED}؛ likelihood ∈ 1..5؛ impact ∈ 1..5؛ risk_score محسوب لا يُدخَل مباشرة (INV-RIS-02)؛ المقيّم ≠ المحدِّد عند سياسة فصل الواجبات (INV-RIS-01)
- **المدخلات:** `likelihood`!: integer, `impact`!: integer — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ASSESSED؛ الحدث EVT-RIS-ASSESSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** مقيّم (تقييم، إعادة تقييم)؛ الشروط: tenant match; scope_refs visible to actor؛ فصل المهام: assessor ≠ identifier when tenant policy requires it (INV-RIS-01)؛ الالتزامات: audit
- **الربط:** `CMD-RIS-ASSESS` · `AGG-RISK` · متطلبات: REQ-RCM-001, REQ-RCM-002, REQ-RCM-003, REQ-RCM-004, REQ-RCM-005 · حالات استخدام: UC-140, UC-141
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RIS-ASSESS succeeds
  Given AGG-RISK in state IDENTIFIED and every guard holds
  When مقيّم sends CMD-RIS-ASSESS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ASSESSED
  And EVT-RIS-ASSESSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RIS-ASSESS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RIS-ASSESS لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RISK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ASSESSED, CLOSED, TREATED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: assessor ≠ identifier when tenant policy requires it (INV-RIS-01) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: likelihood, impact |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-RIS-CLOSE — إغلاق الخطر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | مدير المخاطر | `POST /api/v1/operations/risks/{id}/actions/close` | POL-RIS-CLOSE |

**القصة:** بصفتي **مدير المخاطر**، أريد **إغلاق الخطر**، لكي يتحقق غرض الخطر: تسجيل وتقييم ومعالجة مخاطر محتملة قبل وقوعها (استباقي، لا حادثة فعلية)

- **الشروط المسبقة:** الحالة الحالية ∈ {ASSESSED, IDENTIFIED, TREATED}؛ rationale ∈ {retired,accepted_permanently,materialized}؛ إن كان materialized فـ incident_ref إلزامي (INV-RIS-04)؛ لا أمر لإعادة الفتح — الخطر المُعاد تحديده خطر جديد
- **المدخلات:** `rationale`!: enum(retired, `incident_ref`: urn — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-RIS-CLOSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** مدير المخاطر؛ الشروط: tenant match; scope_refs visible to actor؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RIS-CLOSE` · `AGG-RISK` · متطلبات: REQ-RCM-001, REQ-RCM-002, REQ-RCM-003, REQ-RCM-004, REQ-RCM-005 · حالات استخدام: UC-140, UC-141
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RIS-CLOSE succeeds
  Given AGG-RISK in state ASSESSED or IDENTIFIED or TREATED and every guard holds
  When مدير المخاطر sends CMD-RIS-CLOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-RIS-CLOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RIS-CLOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RIS-CLOSE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RATIONALE_REQUIRED | 422 | لم يتحقق الشرط: rationale ∈ {retired,accepted_permanently,materialized}؛ إن كان materialized فـ incident_ref إلزامي (INV-RIS-04)؛ لا أمر لإعادة الفتح — الخطر المُعاد تحديده خطر جديد |
    | RISK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: rationale |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-RIS-IDENTIFY — تحديد الخطر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | محدِّد الخطر · مقيّم · موافق المعالجة · مدير المخاطر | `POST /api/v1/operations/risks` | POL-RIS-IDENTIFY |

**القصة:** بصفتي **محدِّد الخطر · مقيّم · موافق المعالجة · مدير المخاطر**، أريد **تحديد الخطر**، لكي يتحقق غرض الخطر: تسجيل وتقييم ومعالجة مخاطر محتملة قبل وقوعها (استباقي، لا حادثة فعلية)

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ category_ref (RD-HAZARD-CATEGORIES، مرجع لكل مستأجر — نمط R2-Q1)؛ description؛ scope_refs ≥ 1 (أصل/منطقة/منظمة/خطة)؛ label ≥ تصنيف النطاق
- **المدخلات:** `category_ref`!: urn, `description`!: LocalizedName, `scope_refs`!: array, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← IDENTIFIED؛ الحدث EVT-RIS-IDENTIFIED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** محدِّد الخطر (تحديد) · مقيّم (تقييم، إعادة تقييم) · موافق المعالجة (تخطيط المعالجة) · مدير المخاطر (إغلاق)؛ الشروط: tenant match; scope_refs visible to actor؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RIS-IDENTIFY` · `AGG-RISK` · متطلبات: REQ-RCM-001, REQ-RCM-002, REQ-RCM-003, REQ-RCM-004, REQ-RCM-005 · حالات استخدام: UC-140, UC-141
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RIS-IDENTIFY succeeds
  Given AGG-RISK in state ∅ and every guard holds
  When محدِّد الخطر · مقيّم · موافق المعالجة · مدير المخاطر sends CMD-RIS-IDENTIFY with a valid payload, a new Idempotency-Key
  Then the state becomes IDENTIFIED
  And EVT-RIS-IDENTIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RIS-IDENTIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RIS-IDENTIFY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RISK_INVALID | 422 | لم يتحقق الشرط: category_ref (RD-HAZARD-CATEGORIES، مرجع لكل مستأجر — نمط R2-Q1)؛ description؛ scope_refs ≥ 1 (أصل/منطقة/منظمة/خطة)؛ label ≥ تصنيف النطاق |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: category_ref, description, scope_refs, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-RIS-PLAN-TREATMENT — تخطيط معالجة الخطر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | موافق المعالجة مخوَّل | `POST /api/v1/operations/risks/{id}/actions/plan-treatment` | POL-RIS-PLAN-TREATMENT |

**القصة:** بصفتي **موافق المعالجة مخوَّل**، أريد **تخطيط معالجة الخطر**، لكي يتحقق غرض الخطر: تسجيل وتقييم ومعالجة مخاطر محتملة قبل وقوعها (استباقي، لا حادثة فعلية)

- **الشروط المسبقة:** الحالة الحالية ∈ {ASSESSED}؛ treatment_strategy ∈ {avoid,reduce,transfer,accept}؛ ≥ 1 إجراء معالجة إلا عند accept (INV-RIS-03)؛ موافق مخوَّل
- **المدخلات:** `treatment_strategy`!: enum(avoid, `treatment_task_refs`: array, `approver`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← TREATED؛ الحدث EVT-RIS-TREATMENT-PLANNED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** موافق المعالجة مخوَّل؛ الشروط: tenant match; scope_refs visible to actor؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RIS-PLAN-TREATMENT` · `AGG-RISK` · متطلبات: REQ-RCM-001, REQ-RCM-002, REQ-RCM-003, REQ-RCM-004, REQ-RCM-005 · حالات استخدام: UC-140, UC-141
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RIS-PLAN-TREATMENT succeeds
  Given AGG-RISK in state ASSESSED and every guard holds
  When موافق المعالجة مخوَّل sends CMD-RIS-PLAN-TREATMENT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes TREATED
  And EVT-RIS-TREATMENT-PLANNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RIS-PLAN-TREATMENT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RIS-PLAN-TREATMENT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RISK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED, IDENTIFIED, TREATED |
    | TREATMENT_INVALID | 422 | لم يتحقق الشرط: treatment_strategy ∈ {avoid,reduce,transfer,accept}؛ ≥ 1 إجراء معالجة إلا عند accept (INV-RIS-03)؛ موافق مخوَّل |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: treatment_strategy, approver |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-RIS-REASSESS — إعادة تقييم الخطر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | مقيّم (تقييم، إعادة تقييم) | `POST /api/v1/operations/risks/{id}/actions/reassess` | POL-RIS-REASSESS |

**القصة:** بصفتي **مقيّم (تقييم، إعادة تقييم)**، أريد **إعادة تقييم الخطر**، لكي يتحقق غرض الخطر: تسجيل وتقييم ومعالجة مخاطر محتملة قبل وقوعها (استباقي، لا حادثة فعلية)

- **الشروط المسبقة:** الحالة الحالية ∈ {ASSESSED, TREATED}؛ likelihood/impact جديدان؛ سبب؛ المقيّم ≠ المحدِّد عند سياسة فصل الواجبات
- **المدخلات:** `likelihood`!: integer, `impact`!: integer, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ASSESSED؛ الحدث EVT-RIS-REASSESSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** مقيّم (تقييم، إعادة تقييم)؛ الشروط: tenant match; scope_refs visible to actor؛ فصل المهام: assessor ≠ identifier when tenant policy requires it (INV-RIS-01)؛ الالتزامات: audit
- **الربط:** `CMD-RIS-REASSESS` · `AGG-RISK` · متطلبات: REQ-RCM-001, REQ-RCM-002, REQ-RCM-003, REQ-RCM-004, REQ-RCM-005 · حالات استخدام: UC-140, UC-141
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RIS-REASSESS succeeds
  Given AGG-RISK in state ASSESSED or TREATED and every guard holds
  When مقيّم sends CMD-RIS-REASSESS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ASSESSED
  And EVT-RIS-REASSESSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RIS-REASSESS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RIS-REASSESS لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RISK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED, IDENTIFIED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: assessor ≠ identifier when tenant policy requires it (INV-RIS-01) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: likelihood, impact, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-RISK-01 — تلقائي: incident references this risk as risk_ref (الخطر)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | IDENTIFIED, ASSESSED, TREATED | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «incident references this risk as risk_ref»، أريد تحديث **الخطر** دون تغيير حالته، لكي يتحقق غرض الخطر: تسجيل وتقييم ومعالجة مخاطر محتملة قبل وقوعها (استباقي، لا حادثة فعلية)

- **الشرط:** رابط تلقائي عند تسجيل حادثة تحقَّق منها هذا الخطر؛ لا يغيّر حالة الخطر تلقائياً أبداً (INV-RIS-05)
- **المخرجات:** الحدث EVT-RIS-MATERIALIZATION-LINKED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-RISK` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-Q-RIS-GET — جلب: Risk بنطاقه المرئي للطالب

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مالك النطاق؛ مدير المخاطر | `GET /api/v1/operations/risks/{risk_id}` | POL-RIS-GET |

**القصة:** بصفتي **مالك النطاق؛ مدير المخاطر**، أريد **جلب Risk بنطاقه المرئي للطالب**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter the risk register by category, scope and score, restricted to the caller's visible scope

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Risk بنطاقه المرئي للطالب
- **الصلاحية:** مالك النطاق؛ مدير المخاطر؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-RIS-GET` · `AGG-RISK` · متطلبات: REQ-RCM-014
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-RIS-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-RIS-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-RIS-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-RIS-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC04-Q-RIS-REGISTER — جلب: سجل المخاطر مصفّى بالفئة/النطاق/الدرجة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | allowed_scope | `GET /api/v1/operations/risks` | POL-RIS-REGISTER |

**القصة:** بصفتي **allowed_scope**، أريد **جلب سجل المخاطر مصفّى بالفئة/النطاق/الدرجة**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter the risk register by category, scope and score, restricted to the caller's visible scope

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** سجل المخاطر مصفّى بالفئة/النطاق/الدرجة؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-RIS-REGISTER` · `AGG-RISK` · متطلبات: REQ-RCM-014
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-RIS-REGISTER returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-RIS-REGISTER with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-RIS-REGISTER is denied
  Given the policy denies the caller
  When the caller sends QRY-RIS-REGISTER
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-SUBSCRIPTION — الاشتراك (Subscription)

`03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md` · SLC-06 · الحالات: ACTIVE, PAUSED → ENDED

#### US-BC04-SUB-PAUSE — إيقاف الاشتراك مؤقتًا

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | any user · Administrator | `POST /api/v1/operations/subscriptions/{id}/actions/pause` | POL-SUB-PAUSE |

**القصة:** بصفتي **any user · Administrator**، أريد **إيقاف الاشتراك مؤقتًا**، لكي يتحقق غرض الاشتراك: اشتراك مستخدم في تنبيهات موقف أو قاعدة، بقنوات مفضلة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← PAUSED؛ الحدث EVT-SUB-PAUSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** any user (self) · Administrator (end)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SUB-PAUSE` · `AGG-SUBSCRIPTION` · متطلبات: REQ-COM-001 · حالات استخدام: UC-099
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SUB-PAUSE succeeds
  Given AGG-SUBSCRIPTION in state ACTIVE and every guard holds
  When any user · Administrator sends CMD-SUB-PAUSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PAUSED
  And EVT-SUB-PAUSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SUB-PAUSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SUB-PAUSE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SUBSCRIPTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ENDED, PAUSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-SUB-RESUME — استئناف الاشتراك

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | any user · Administrator | `POST /api/v1/operations/subscriptions/{id}/actions/resume` | POL-SUB-RESUME |

**القصة:** بصفتي **any user · Administrator**، أريد **استئناف الاشتراك**، لكي يتحقق غرض الاشتراك: اشتراك مستخدم في تنبيهات موقف أو قاعدة، بقنوات مفضلة

- **الشروط المسبقة:** الحالة الحالية ∈ {PAUSED}؛ target still visible
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-SUB-RESUMED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** any user (self) · Administrator (end)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SUB-RESUME` · `AGG-SUBSCRIPTION` · متطلبات: REQ-COM-001 · حالات استخدام: UC-099
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SUB-RESUME succeeds
  Given AGG-SUBSCRIPTION in state PAUSED and every guard holds
  When any user · Administrator sends CMD-SUB-RESUME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-SUB-RESUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SUB-RESUME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SUB-RESUME لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SUBSCRIPTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, ENDED |
    | TARGET_NOT_VISIBLE | 422 | لم يتحقق الشرط: target still visible |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-SUB-SUBSCRIBE — إنشاء الاشتراك

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | any user · Administrator | `POST /api/v1/operations/subscriptions` | POL-SUB-SUBSCRIBE |

**القصة:** بصفتي **any user · Administrator**، أريد **إنشاء الاشتراك**، لكي يتحقق غرض الاشتراك: اشتراك مستخدم في تنبيهات موقف أو قاعدة، بقنوات مفضلة

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ target (situation \| alert rule) visible to subscriber; channels ⊆ {in_app, push}; one ACTIVE per (user, target)
- **المدخلات:** `target`!: urn, `channels`!: array, `quiet_hours`: object — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-SUB-SUBSCRIBED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** any user (self) · Administrator (end)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SUB-SUBSCRIBE` · `AGG-SUBSCRIPTION` · متطلبات: REQ-COM-001 · حالات استخدام: UC-099
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SUB-SUBSCRIBE succeeds
  Given AGG-SUBSCRIPTION in state ∅ and every guard holds
  When any user · Administrator sends CMD-SUB-SUBSCRIBE with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-SUB-SUBSCRIBED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SUB-SUBSCRIBE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SUB-SUBSCRIBE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SUBSCRIPTION_EXISTS | 422 | لم يتحقق الشرط: target (situation \| alert rule) visible to subscriber; channels ⊆ {in_app, push}; one ACTIVE per (user, target) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: target, channels |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-SUB-UNSUBSCRIBE — إلغاء الاشتراك

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | any user · Administrator | `POST /api/v1/operations/subscriptions/{id}/actions/unsubscribe` | POL-SUB-UNSUBSCRIBE |

**القصة:** بصفتي **any user · Administrator**، أريد **إلغاء الاشتراك**، لكي يتحقق غرض الاشتراك: اشتراك مستخدم في تنبيهات موقف أو قاعدة، بقنوات مفضلة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, PAUSED}؛ actor = subscriber or Administrator
- **المدخلات:** `reason`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ENDED؛ الحدث EVT-SUB-ENDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** any user (self) · Administrator (end)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SUB-UNSUBSCRIBE` · `AGG-SUBSCRIPTION` · متطلبات: REQ-COM-001 · حالات استخدام: UC-099
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SUB-UNSUBSCRIBE succeeds
  Given AGG-SUBSCRIPTION in state ACTIVE or PAUSED and every guard holds
  When any user · Administrator sends CMD-SUB-UNSUBSCRIBE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ENDED
  And EVT-SUB-ENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SUB-UNSUBSCRIBE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SUB-UNSUBSCRIBE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SUBSCRIPTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-SUB-UPDATE-CHANNELS — تحديث قنوات الاشتراك

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | any user · Administrator | `POST /api/v1/operations/subscriptions/{id}/actions/update-channels` | POL-SUB-UPDATE-CHANNELS |

**القصة:** بصفتي **any user · Administrator**، أريد **تحديث قنوات الاشتراك**، لكي يتحقق غرض الاشتراك: اشتراك مستخدم في تنبيهات موقف أو قاعدة، بقنوات مفضلة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, PAUSED}؛ channels valid; quiet hours valid (critical severity bypasses quiet hours)
- **المدخلات:** `channels`!: array, `quiet_hours`: object — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SUB-CHANNELS-UPDATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** any user (self) · Administrator (end)؛ الشروط: tenant match; target visible to subject؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SUB-UPDATE-CHANNELS` · `AGG-SUBSCRIPTION` · متطلبات: REQ-COM-001 · حالات استخدام: UC-099
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SUB-UPDATE-CHANNELS succeeds
  Given AGG-SUBSCRIPTION in state ACTIVE or PAUSED and every guard holds
  When any user · Administrator sends CMD-SUB-UPDATE-CHANNELS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-SUB-CHANNELS-UPDATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SUB-UPDATE-CHANNELS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SUB-UPDATE-CHANNELS لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SUBSCRIPTION_INVALID | 422 | لم يتحقق الشرط: channels valid; quiet hours valid (critical severity bypasses quiet hours) |
    | SUBSCRIPTION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: channels |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-SUBSCRIPTION-01 — تلقائي: subscriber lost visibility of target (الاشتراك)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | ACTIVE, PAUSED | ENDED |

**القصة:** بصفتي **النظام**، عند «subscriber lost visibility of target»، أريد نقل **الاشتراك** إلى ENDED، لكي يتحقق غرض الاشتراك: اشتراك مستخدم في تنبيهات موقف أو قاعدة، بقنوات مفضلة

- **الشرط:** security-version change or reclassification
- **المخرجات:** الحدث EVT-SUB-ENDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-SUBSCRIPTION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

### AGG-TASK — المهمة (Task)

`03-domain/contexts/BC04/aggregates/AGG-TASK.md` · SLC-03 · الحالات: DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED, SUBMITTED, UNDER_REVIEW, APPROVED, COMPLETED → CLOSED, CANCELLED, REJECTED, EXPIRED, SUPERSEDED

#### US-BC04-TASK-ACCEPT — قبول المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | assignee | `POST /api/v1/operations/tasks/{id}/actions/accept` | POL-TASK-ACCEPT |

**القصة:** بصفتي **assignee**، أريد **قبول المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {ASSIGNED}؛ actor = assignee
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACCEPTED؛ الحدث EVT-TASK-ACCEPTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** assignee؛ الشروط: tenant match; task visible; org scope; offline allowed؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-ACCEPT` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-ACCEPT succeeds
  Given AGG-TASK in state ASSIGNED and every guard holds
  When assignee sends CMD-TASK-ACCEPT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACCEPTED
  And EVT-TASK-ACCEPTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-ACCEPT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-ACCEPT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | NOT_ASSIGNEE | 422 | لم يتحقق الشرط: actor = assignee |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, IN_PROGRESS, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-ADD-RESULT-ITEM — إضافة بند نتيجة إلى المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | assignee | `POST /api/v1/operations/tasks/{id}/actions/add-result-item` | POL-TASK-ADD-RESULT-ITEM |

**القصة:** بصفتي **assignee**، أريد **إضافة بند نتيجة إلى المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {BLOCKED, IN_PROGRESS}؛ actor = assignee; item = note \| evidence URN \| observation URN \| measurement
- **المدخلات:** `kind`!: enum(note, `ref`: urn, `note`: LocalizedName, `measurement`: object — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-TASK-RESULT-ITEM-ADDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** assignee؛ الشروط: tenant match; task visible; org scope; offline allowed؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-ADD-RESULT-ITEM` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-ADD-RESULT-ITEM succeeds
  Given AGG-TASK in state BLOCKED or IN_PROGRESS and every guard holds
  When assignee sends CMD-TASK-ADD-RESULT-ITEM with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-TASK-RESULT-ITEM-ADDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-ADD-RESULT-ITEM is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-ADD-RESULT-ITEM لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RESULT_ITEM_INVALID | 422 | لم يتحقق الشرط: actor = assignee; item = note \| evidence URN \| observation URN \| measurement |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: kind |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-APPROVE — اعتماد المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | reviewer | `POST /api/v1/operations/tasks/{id}/actions/approve` | POL-TASK-APPROVE |

**القصة:** بصفتي **reviewer**، أريد **اعتماد المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {UNDER_REVIEW}؛ reviewer ≠ assignee unless tenant policy disables SoD (REQ-OPS-009)
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← APPROVED؛ الحدث EVT-TASK-APPROVED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** reviewer؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: reviewer ≠ assignee (PB-06)؛ الالتزامات: audit
- **الربط:** `CMD-TASK-APPROVE` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-APPROVE succeeds
  Given AGG-TASK in state UNDER_REVIEW and every guard holds
  When reviewer sends CMD-TASK-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes APPROVED
  And EVT-TASK-APPROVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-APPROVE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: reviewer ≠ assignee (PB-06) |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, IN_PROGRESS, READY, REJECTED, SUBMITTED, SUPERSEDED |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-ASSIGN — إسناد المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Planner/Manager in scope | `POST /api/v1/operations/tasks/{id}/actions/assign` | POL-TASK-ASSIGN |

**القصة:** بصفتي **Planner/Manager in scope**، أريد **إسناد المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {READY}؛ assignee ACTIVE user; assignee clearance ≥ task label; EligibilityCheck(assignee, task type, now) ∈ {ELIGIBLE, CONDITIONALLY_ELIGIBLE with condition met} (REQ-OPS-007); actor authorized in scope
- **المدخلات:** `assignee`!: urn, `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ASSIGNED؛ الحدث EVT-TASK-ASSIGNED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: assignee clearance ≥ task label؛ الالتزامات: audit
- **الربط:** `CMD-TASK-ASSIGN` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-ASSIGN succeeds
  Given AGG-TASK in state READY and every guard holds
  When Planner/Manager in scope sends CMD-TASK-ASSIGN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ASSIGNED
  And EVT-TASK-ASSIGNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-ASSIGN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSIGNEE_NOT_ELIGIBLE | 422 | لم يتحقق الشرط: assignee ACTIVE user; assignee clearance ≥ task label; EligibilityCheck(assignee, task type, now) ∈ {ELIGIBLE, CONDITIONALLY_ELIGIBLE with condition met} (REQ-OPS-007); actor authorized in scope |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-ASSIGN لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, IN_PROGRESS, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: assignee |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-BLOCK — تعليق المهمة كمحجوب

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | assignee | `POST /api/v1/operations/tasks/{id}/actions/block` | POL-TASK-BLOCK |

**القصة:** بصفتي **assignee**، أريد **تعليق المهمة كمحجوب**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {IN_PROGRESS}؛ actor = assignee; blocking reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← BLOCKED؛ الحدث EVT-TASK-BLOCKED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** assignee؛ الشروط: tenant match; task visible; org scope; offline allowed؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-BLOCK` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-BLOCK succeeds
  Given AGG-TASK in state IN_PROGRESS and every guard holds
  When assignee sends CMD-TASK-BLOCK with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes BLOCKED
  And EVT-TASK-BLOCKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-BLOCK is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-BLOCK لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-CANCEL — إلغاء المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Planner/Manager in scope | `POST /api/v1/operations/tasks/{id}/actions/cancel` | POL-TASK-CANCEL |

**القصة:** بصفتي **Planner/Manager in scope**، أريد **إلغاء المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {ACCEPTED, APPROVED, ASSIGNED, BLOCKED, DRAFT, IN_PROGRESS, READY, SUBMITTED, UNDER_REVIEW}؛ actor has cancel authority in scope; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-TASK-CANCELLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-CANCEL` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-CANCEL succeeds
  Given AGG-TASK in state ACCEPTED or APPROVED or ASSIGNED or BLOCKED or DRAFT or IN_PROGRESS or READY or SUBMITTED or UNDER_REVIEW and every guard holds
  When Planner/Manager in scope sends CMD-TASK-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-TASK-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-CANCEL لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, COMPLETED, EXPIRED, REJECTED, SUPERSEDED |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-CLOSE — إغلاق المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | owner / Planner | `POST /api/v1/operations/tasks/{id}/actions/close` | POL-TASK-CLOSE |

**القصة:** بصفتي **owner / Planner**، أريد **إغلاق المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {COMPLETED}؛ no open follow-up tasks
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-TASK-CLOSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** owner / Planner؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-CLOSE` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-CLOSE succeeds
  Given AGG-TASK in state COMPLETED and every guard holds
  When owner / Planner sends CMD-TASK-CLOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-TASK-CLOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-CLOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-CLOSE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OPEN_FOLLOW_UPS | 422 | لم يتحقق الشرط: no open follow-up tasks |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, DRAFT, EXPIRED, IN_PROGRESS, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-COMPLETE — إكمال المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | reviewer or attestation role | `POST /api/v1/operations/tasks/{id}/actions/complete` | POL-TASK-COMPLETE |

**القصة:** بصفتي **reviewer or attestation role**، أريد **إكمال المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {APPROVED}؛ attestation-type criteria confirmed by an authorized actor; all criteria satisfied (BRL-006)
- **المدخلات:** `attestations`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← COMPLETED؛ الحدث EVT-TASK-COMPLETED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** reviewer or attestation role؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-COMPLETE` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-COMPLETE succeeds
  Given AGG-TASK in state APPROVED and every guard holds
  When reviewer or attestation role sends CMD-TASK-COMPLETE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes COMPLETED
  And EVT-TASK-COMPLETED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-COMPLETE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-COMPLETE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_CRITERIA_NOT_MET | 422 | لم يتحقق الشرط: attestation-type criteria confirmed by an authorized actor; all criteria satisfied (BRL-006) |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, IN_PROGRESS, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: attestations |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-CREATE — إنشاء المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Planner/Manager in scope | `POST /api/v1/operations/tasks` | POL-TASK-CREATE |

**القصة:** بصفتي **Planner/Manager in scope**، أريد **إنشاء المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ task type ACTIVE (version pinned); plan_ref (operations, collection or contingency plan — CR-59, CR-61) or incident_ref (direct response task under an Incident, SLC-17 — CR-61), or ad_hoc_reason + accountable owner (REQ-OPS-010); label ≤ creator clearance
- **المدخلات:** `task_type`!: urn, `title`!: LocalizedName, `description`: LocalizedName, `plan_ref`: urn, `incident_ref`: urn, `ad_hoc_reason`: string, `owner`!: urn, `org_scope`!: urn, `due_at`: date-time, `dependencies`: array, `follow_up_of`: urn, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-TASK-CREATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-CREATE` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-CREATE succeeds
  Given AGG-TASK in state ∅ and every guard holds
  When Planner/Manager in scope sends CMD-TASK-CREATE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-TASK-CREATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-CREATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-CREATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_INVALID | 422 | لم يتحقق الشرط: task type ACTIVE (version pinned); plan_ref (operations, collection or contingency plan — CR-59, CR-61) or incident_ref (direct response task under an Incident, SLC-17 — CR-61), or ad_hoc_reason + accountable owner (REQ-OPS-010); label ≤ creator clearance |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: task_type, title, owner, org_scope, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-DECLINE — رفض قبول المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | assignee | `POST /api/v1/operations/tasks/{id}/actions/decline` | POL-TASK-DECLINE |

**القصة:** بصفتي **assignee**، أريد **رفض قبول المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {ASSIGNED}؛ actor = assignee; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← READY؛ الحدث EVT-TASK-DECLINED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** assignee؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-DECLINE` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-DECLINE succeeds
  Given AGG-TASK in state ASSIGNED and every guard holds
  When assignee sends CMD-TASK-DECLINE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes READY
  And EVT-TASK-DECLINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-DECLINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-DECLINE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, IN_PROGRESS, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-EDIT — تعديل المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Planner/Manager in scope | `POST /api/v1/operations/tasks/{id}/actions/edit` | POL-TASK-EDIT |

**القصة:** بصفتي **Planner/Manager in scope**، أريد **تعديل المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT, READY}؛ creator or Planner; completion criteria editable only in DRAFT/READY; new version
- **المدخلات:** `title`: LocalizedName, `description`: LocalizedName, `criteria`: array, `dependencies`: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-TASK-EDITED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-EDIT` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-EDIT succeeds
  Given AGG-TASK in state DRAFT or READY and every guard holds
  When Planner/Manager in scope sends CMD-TASK-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-TASK-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-EDIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_INVALID | 422 | لم يتحقق الشرط: creator or Planner; completion criteria editable only in DRAFT/READY; new version |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, EXPIRED, IN_PROGRESS, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-ESCALATE — تصعيد المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | assignee, owner, Planner | `POST /api/v1/operations/tasks/{id}/actions/escalate` | POL-TASK-ESCALATE |

**القصة:** بصفتي **assignee, owner, Planner**، أريد **تصعيد المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {ACCEPTED, APPROVED, ASSIGNED, BLOCKED, COMPLETED, DRAFT, IN_PROGRESS, READY, SUBMITTED, UNDER_REVIEW}؛ reason; notifies next authority level (REQ-OPS-012)
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-TASK-ESCALATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** assignee, owner, Planner؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-ESCALATE` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-ESCALATE succeeds
  Given AGG-TASK in state ACCEPTED or APPROVED or ASSIGNED or BLOCKED or COMPLETED or DRAFT or IN_PROGRESS or READY or SUBMITTED or UNDER_REVIEW and every guard holds
  When assignee, owner, Planner sends CMD-TASK-ESCALATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-TASK-ESCALATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-ESCALATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-ESCALATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, EXPIRED, REJECTED, SUPERSEDED |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-MARK-READY — تعليم المهمة كجاهز

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | `POST /api/v1/operations/tasks/{id}/actions/mark-ready` | POL-TASK-MARK-READY |

**القصة:** بصفتي **Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)**، أريد **تعليم المهمة كجاهز**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ title, ≥ 1 completion criterion, owner; dependencies reference existing tasks without cycle
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← READY؛ الحدث EVT-TASK-READIED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-MARK-READY` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-MARK-READY succeeds
  Given AGG-TASK in state DRAFT and every guard holds
  When Planner/Manager in scope sends CMD-TASK-MARK-READY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes READY
  And EVT-TASK-READIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-MARK-READY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-MARK-READY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, EXPIRED, IN_PROGRESS, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_NOT_READY | 422 | لم يتحقق الشرط: title, ≥ 1 completion criterion, owner; dependencies reference existing tasks without cycle |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-REASSIGN — إعادة إسناد المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | `POST /api/v1/operations/tasks/{id}/actions/reassign` | POL-TASK-REASSIGN |

**القصة:** بصفتي **Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)**، أريد **إعادة إسناد المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {ACCEPTED, ASSIGNED, BLOCKED, IN_PROGRESS}؛ same checks as assign for the new assignee; reason; previous assignee notified
- **المدخلات:** `assignee`!: urn, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ASSIGNED؛ الحدث EVT-TASK-REASSIGNED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: assignee clearance ≥ task label؛ الالتزامات: audit
- **الربط:** `CMD-TASK-REASSIGN` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-REASSIGN succeeds
  Given AGG-TASK in state ACCEPTED or ASSIGNED or BLOCKED or IN_PROGRESS and every guard holds
  When Planner/Manager in scope sends CMD-TASK-REASSIGN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ASSIGNED
  And EVT-TASK-REASSIGNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-REASSIGN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSIGNEE_NOT_ELIGIBLE | 422 | لم يتحقق الشرط: same checks as assign for the new assignee; reason; previous assignee notified |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-REASSIGN لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: assignee, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-RECLASSIFY — إعادة تصنيف المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | `POST /api/v1/operations/tasks/{id}/actions/reclassify` | POL-TASK-RECLASSIFY |

**القصة:** بصفتي **Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)**، أريد **إعادة تصنيف المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {ACCEPTED, APPROVED, ASSIGNED, BLOCKED, COMPLETED, DRAFT, IN_PROGRESS, READY, SUBMITTED, UNDER_REVIEW}؛ authority per tenant policy; assignee clearance ≥ new label, else reassignment required first
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-TASK-RECLASSIFIED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-RECLASSIFY` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-RECLASSIFY succeeds
  Given AGG-TASK in state ACCEPTED or APPROVED or ASSIGNED or BLOCKED or COMPLETED or DRAFT or IN_PROGRESS or READY or SUBMITTED or UNDER_REVIEW and every guard holds
  When Planner/Manager in scope sends CMD-TASK-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-TASK-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-RECLASSIFY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per tenant policy; assignee clearance ≥ new label, else reassignment required first |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, EXPIRED, REJECTED, SUPERSEDED |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-REJECT — رفض المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | reviewer | `POST /api/v1/operations/tasks/{id}/actions/reject` | POL-TASK-REJECT |

**القصة:** بصفتي **reviewer**، أريد **رفض المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {UNDER_REVIEW}؛ reviewer; reason; follow-up task may be created linked by follow_up_of (OQ-033)
- **المدخلات:** `reason`!: string, `create_follow_up`!: boolean — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-TASK-REJECTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** reviewer؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-REJECT` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-REJECT succeeds
  Given AGG-TASK in state UNDER_REVIEW and every guard holds
  When reviewer sends CMD-TASK-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-TASK-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-REJECT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, IN_PROGRESS, READY, REJECTED, SUBMITTED, SUPERSEDED |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason, create_follow_up |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-RESUME — استئناف المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | assignee | `POST /api/v1/operations/tasks/{id}/actions/resume` | POL-TASK-RESUME |

**القصة:** بصفتي **assignee**، أريد **استئناف المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {BLOCKED}؛ actor = assignee; resolution note
- **المدخلات:** `note`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← IN_PROGRESS؛ الحدث EVT-TASK-RESUMED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** assignee؛ الشروط: tenant match; task visible; org scope; offline allowed؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-RESUME` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-RESUME succeeds
  Given AGG-TASK in state BLOCKED and every guard holds
  When assignee sends CMD-TASK-RESUME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_PROGRESS
  And EVT-TASK-RESUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-RESUME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-RESUME لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, IN_PROGRESS, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: note |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-RETURN — إعادة المهمة للمراجعة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | reviewer | `POST /api/v1/operations/tasks/{id}/actions/return` | POL-TASK-RETURN |

**القصة:** بصفتي **reviewer**، أريد **إعادة المهمة للمراجعة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {UNDER_REVIEW}؛ reviewer; rework reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← IN_PROGRESS؛ الحدث EVT-TASK-RETURNED-FOR-REWORK؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** reviewer؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-RETURN` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-RETURN succeeds
  Given AGG-TASK in state UNDER_REVIEW and every guard holds
  When reviewer sends CMD-TASK-RETURN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_PROGRESS
  And EVT-TASK-RETURNED-FOR-REWORK is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-RETURN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-RETURN لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, IN_PROGRESS, READY, REJECTED, SUBMITTED, SUPERSEDED |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-SET-DUE — تحديد موعد استحقاق المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Planner/Manager in scope | `POST /api/v1/operations/tasks/{id}/actions/set-due` | POL-TASK-SET-DUE |

**القصة:** بصفتي **Planner/Manager in scope**، أريد **تحديد موعد استحقاق المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {ACCEPTED, ASSIGNED, BLOCKED, DRAFT, IN_PROGRESS, READY}؛ Planner or owner; reason
- **المدخلات:** `due_at`!: date-time, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-TASK-DUE-CHANGED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-SET-DUE` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-SET-DUE succeeds
  Given AGG-TASK in state ACCEPTED or ASSIGNED or BLOCKED or DRAFT or IN_PROGRESS or READY and every guard holds
  When Planner/Manager in scope sends CMD-TASK-SET-DUE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-TASK-DUE-CHANGED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-SET-DUE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-SET-DUE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, CANCELLED, CLOSED, COMPLETED, EXPIRED, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: due_at, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-START — بدء المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | assignee | `POST /api/v1/operations/tasks/{id}/actions/start` | POL-TASK-START |

**القصة:** بصفتي **assignee**، أريد **بدء المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {ACCEPTED}؛ actor = assignee; all predecessor tasks COMPLETED or CLOSED
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← IN_PROGRESS؛ الحدث EVT-TASK-STARTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** assignee؛ الشروط: tenant match; task visible; org scope; offline allowed؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-START` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-START succeeds
  Given AGG-TASK in state ACCEPTED and every guard holds
  When assignee sends CMD-TASK-START with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_PROGRESS
  And EVT-TASK-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-START is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-START لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DEPENDENCIES_NOT_MET | 422 | لم يتحقق الشرط: actor = assignee; all predecessor tasks COMPLETED or CLOSED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, IN_PROGRESS, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-START-REVIEW — بدء مراجعة المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | reviewer role in scope | `POST /api/v1/operations/tasks/{id}/actions/start-review` | POL-TASK-START-REVIEW |

**القصة:** بصفتي **reviewer role in scope**، أريد **بدء مراجعة المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {SUBMITTED}؛ actor has review permission in scope; actor ≠ assignee
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← UNDER_REVIEW؛ الحدث EVT-TASK-REVIEW-STARTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** reviewer role in scope؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: reviewer ≠ assignee؛ الالتزامات: audit
- **الربط:** `CMD-TASK-START-REVIEW` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-START-REVIEW succeeds
  Given AGG-TASK in state SUBMITTED and every guard holds
  When reviewer role in scope sends CMD-TASK-START-REVIEW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNDER_REVIEW
  And EVT-TASK-REVIEW-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-START-REVIEW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-START-REVIEW لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: reviewer ≠ assignee |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, IN_PROGRESS, READY, REJECTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-SUBMIT — تقديم المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | assignee | `POST /api/v1/operations/tasks/{id}/actions/submit` | POL-TASK-SUBMIT |

**القصة:** بصفتي **assignee**، أريد **تقديم المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {IN_PROGRESS}؛ actor = assignee; result has ≥ 1 item
- **المدخلات:** `summary`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← SUBMITTED؛ الحدث EVT-TASK-SUBMITTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** assignee؛ الشروط: tenant match; task visible; org scope; offline allowed؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-SUBMIT` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-SUBMIT succeeds
  Given AGG-TASK in state IN_PROGRESS and every guard holds
  When assignee sends CMD-TASK-SUBMIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUBMITTED
  And EVT-TASK-SUBMITTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-SUBMIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-SUBMIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RESULT_REQUIRED | 422 | لم يتحقق الشرط: actor = assignee; result has ≥ 1 item |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACCEPTED, APPROVED, ASSIGNED, BLOCKED, CANCELLED, CLOSED, COMPLETED, DRAFT, EXPIRED, READY, REJECTED, SUBMITTED, SUPERSEDED, UNDER_REVIEW |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: summary |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-SUSPEND — تعليق المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Planner/Manager in scope | `POST /api/v1/operations/tasks/{id}/actions/suspend` | POL-TASK-SUSPEND |

**القصة:** بصفتي **Planner/Manager in scope**، أريد **تعليق المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {ACCEPTED, APPROVED, ASSIGNED, BLOCKED, COMPLETED, DRAFT, IN_PROGRESS, READY, SUBMITTED, UNDER_REVIEW}؛ suspend authority; reason; sets suspended = true
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-TASK-SUSPENDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-SUSPEND` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-SUSPEND succeeds
  Given AGG-TASK in state ACCEPTED or APPROVED or ASSIGNED or BLOCKED or COMPLETED or DRAFT or IN_PROGRESS or READY or SUBMITTED or UNDER_REVIEW and every guard holds
  When Planner/Manager in scope sends CMD-TASK-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-TASK-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-SUSPEND لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, EXPIRED, REJECTED, SUPERSEDED |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TASK-UNSUSPEND — رفع تعليق المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | `POST /api/v1/operations/tasks/{id}/actions/unsuspend` | POL-TASK-UNSUSPEND |

**القصة:** بصفتي **Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)**، أريد **رفع تعليق المهمة**، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشروط المسبقة:** الحالة الحالية ∈ {ACCEPTED, APPROVED, ASSIGNED, BLOCKED, COMPLETED, DRAFT, IN_PROGRESS, READY, SUBMITTED, UNDER_REVIEW}؛ suspend authority; suspended = true
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-TASK-UNSUSPENDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TASK-UNSUSPEND` · `AGG-TASK` · متطلبات: REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OFF-001 · حالات استخدام: UC-040, UC-041, UC-042, UC-043, UC-044, UC-045, UC-046, UC-090, UC-102
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TASK-UNSUSPEND succeeds
  Given AGG-TASK in state ACCEPTED or APPROVED or ASSIGNED or BLOCKED or COMPLETED or DRAFT or IN_PROGRESS or READY or SUBMITTED or UNDER_REVIEW and every guard holds
  When Planner/Manager in scope sends CMD-TASK-UNSUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-TASK-UNSUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TASK-UNSUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TASK-UNSUSPEND لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | NOT_SUSPENDED | 422 | لم يتحقق الشرط: suspend authority; suspended = true |
    | TASK_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CLOSED, EXPIRED, REJECTED, SUPERSEDED |
    | TASK_SUSPENDED | 422 | انظر شرط الانتقال وكتالوج الأخطاء |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-S-TASK-01 — تلقائي: all completion criteria satisfied (المهمة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | APPROVED | COMPLETED |

**القصة:** بصفتي **النظام**، عند «all completion criteria satisfied»، أريد نقل **المهمة** إلى COMPLETED، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشرط:** system-checkable criteria evaluated at approval and whenever result evidence changes (BRL-006)
- **المخرجات:** الحدث EVT-TASK-COMPLETED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-TASK` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-TASK-02 — تلقائي: follow-up window (7 d) elapsed without open follow-ups (المهمة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | COMPLETED | CLOSED |

**القصة:** بصفتي **النظام**، عند «follow-up window (7 d) elapsed without open follow-ups»، أريد نقل **المهمة** إلى CLOSED، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشرط:** scheduler
- **المخرجات:** الحدث EVT-TASK-CLOSED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-TASK` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-TASK-03 — تلقائي: due passed and task type expires_on_due (المهمة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED, SUBMITTED, UNDER_REVIEW | EXPIRED |

**القصة:** بصفتي **النظام**، عند «due passed and task type expires_on_due»، أريد نقل **المهمة** إلى EXPIRED، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشرط:** scheduler; only when the task type declares expires_on_due = true (OQ-032)
- **المخرجات:** الحدث EVT-TASK-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-TASK` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-TASK-04 — تلقائي: plan version baselined without this task (المهمة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED, SUBMITTED, UNDER_REVIEW, APPROVED | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «plan version baselined without this task»، أريد نقل **المهمة** إلى SUPERSEDED، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشرط:** SLC-08 trigger
- **المخرجات:** الحدث EVT-TASK-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-TASK` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-S-TASK-05 — تلقائي: due passed (escalation policy) (المهمة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED, SUBMITTED, UNDER_REVIEW, APPROVED, COMPLETED | (بلا تغيير) |

**القصة:** بصفتي **النظام**، عند «due passed (escalation policy)»، أريد تحديث **المهمة** دون تغيير حالته، لكي يتحقق غرض المهمة: وحدة عمل قابلة للإسناد والتنفيذ والمراجعة والقياس

- **الشرط:** scheduler; at due and at due + grace from task type
- **المخرجات:** الحدث EVT-TASK-ESCALATED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-TASK` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC04-Q-TASK-GET — جلب: Task with criteria status, result, eligibility snapshot, dependencies

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | assignee, reviewer, Planner/Manager in scope; label rule | `GET /api/v1/operations/tasks/{task_id}` | POL-TASK-GET |

**القصة:** بصفتي **assignee, reviewer, Planner/Manager in scope; label rule**، أريد **جلب Task with criteria status, result, eligibility snapshot, dependencies**، لكي يتحقق المتطلب: The system shall manage task state according to state machine SM-TASK and reject any transition not defined in it

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Task with criteria status, result, eligibility snapshot, dependencies
- **الصلاحية:** assignee, reviewer, Planner/Manager in scope; label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-TASK-GET` · `AGG-TASK` · متطلبات: REQ-OPS-006
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-TASK-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-TASK-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-TASK-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-TASK-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC04-Q-TASK-HISTORY — جلب: State history; state as of t (RECONSTRUCTED)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | same as QRY-TASK-GET | `GET /api/v1/operations/tasks/{task_id}/history` | POL-TASK-HISTORY |

**القصة:** بصفتي **same as QRY-TASK-GET**، أريد **جلب State history; state as of t (RECONSTRUCTED)**، لكي يتحقق المتطلب: The system shall manage task state according to state machine SM-TASK and reject any transition not defined in it

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** State history; state as of t (RECONSTRUCTED)؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** same as QRY-TASK-GET؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-TASK-HISTORY` · `AGG-TASK` · متطلبات: REQ-OPS-006
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-TASK-HISTORY returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-TASK-HISTORY with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-TASK-HISTORY is denied
  Given the policy denies the caller
  When the caller sends QRY-TASK-HISTORY
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC04-Q-TASK-LIST — جلب: Tasks by assignee (me), plan, state, due_before, unit

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | allowed_scope pre-filter | `GET /api/v1/operations/tasks` | POL-TASK-LIST |

**القصة:** بصفتي **allowed_scope pre-filter**، أريد **جلب Tasks by assignee (me), plan, state, due_before, unit**، لكي يتحقق المتطلب: The system shall manage task state according to state machine SM-TASK and reject any transition not defined in it

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Tasks by assignee (me), plan, state, due_before, unit؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope pre-filter؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-TASK-LIST` · `AGG-TASK` · متطلبات: REQ-OPS-006
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-TASK-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-TASK-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-TASK-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-TASK-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-TASK-TYPE — نوع المهمة (Task Type)

`03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md` · SLC-03 · الحالات: DRAFT, ACTIVE → RETIRED

#### US-BC04-TTY-ACTIVATE — تفعيل نوع المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Administrator / Planner lead | `POST /api/v1/operations/task-types/{id}/actions/activate` | POL-TTY-ACTIVATE |

**القصة:** بصفتي **Administrator / Planner lead**، أريد **تفعيل نوع المهمة**، لكي يتحقق غرض نوع المهمة: قالب نوع مهمة: متطلبات الأهلية، معايير الإكمال، التصعيد، الانتهاء

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ ≥ 1 completion criterion template
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-TTY-ACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator / Planner lead؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TTY-ACTIVATE` · `AGG-TASK-TYPE` · متطلبات: REQ-OPS-007, REQ-OPS-014 · حالات استخدام: UC-034, UC-041, UC-044, UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TTY-ACTIVATE succeeds
  Given AGG-TASK-TYPE in state DRAFT and every guard holds
  When Administrator / Planner lead sends CMD-TTY-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-TTY-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TTY-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TTY-ACTIVATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_TYPE_INVALID | 422 | لم يتحقق الشرط: ≥ 1 completion criterion template |
    | TASK_TYPE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TTY-DEFINE — تعريف نوع المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Administrator / Planner lead | `POST /api/v1/operations/task-types` | POL-TTY-DEFINE |

**القصة:** بصفتي **Administrator / Planner lead**، أريد **تعريف نوع المهمة**، لكي يتحقق غرض نوع المهمة: قالب نوع مهمة: متطلبات الأهلية، معايير الإكمال، التصعيد، الانتهاء

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ code unique in tenant
- **المدخلات:** `code`!: string, `name`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-TTY-DEFINED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator / Planner lead؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TTY-DEFINE` · `AGG-TASK-TYPE` · متطلبات: REQ-OPS-007, REQ-OPS-014 · حالات استخدام: UC-034, UC-041, UC-044, UC-102
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TTY-DEFINE succeeds
  Given AGG-TASK-TYPE in state ∅ and every guard holds
  When Administrator / Planner lead sends CMD-TTY-DEFINE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-TTY-DEFINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TTY-DEFINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TTY-DEFINE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_TYPE_CODE_TAKEN | 422 | لم يتحقق الشرط: code unique in tenant |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: code, name |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TTY-EDIT — تعديل نوع المهمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Administrator / Planner lead | `POST /api/v1/operations/task-types/{id}/actions/edit` | POL-TTY-EDIT |

**القصة:** بصفتي **Administrator / Planner lead**، أريد **تعديل نوع المهمة**، لكي يتحقق غرض نوع المهمة: قالب نوع مهمة: متطلبات الأهلية، معايير الإكمال، التصعيد، الانتهاء

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, DRAFT}؛ required qualifications exist in RD-COMPETENCIES; criteria templates valid; ACTIVE → new version (existing tasks keep their pinned version)
- **المدخلات:** `qualification_requirements`!: array, `criteria_templates`!: array, `escalation`!: object, `expires_on_due`!: boolean, `review_steps`: integer — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-TTY-EDITED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator / Planner lead؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TTY-EDIT` · `AGG-TASK-TYPE` · متطلبات: REQ-OPS-007, REQ-OPS-014 · حالات استخدام: UC-034, UC-041, UC-044, UC-102
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TTY-EDIT succeeds
  Given AGG-TASK-TYPE in state ACTIVE or DRAFT and every guard holds
  When Administrator / Planner lead sends CMD-TTY-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-TTY-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TTY-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TTY-EDIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TASK_TYPE_INVALID | 422 | لم يتحقق الشرط: required qualifications exist in RD-COMPETENCIES; criteria templates valid; ACTIVE → new version (existing tasks keep their pinned version) |
    | TASK_TYPE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: qualification_requirements, criteria_templates, escalation, expires_on_due |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-TTY-RETIRE — إحالة نوع المهمة إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Administrator / Planner lead | `POST /api/v1/operations/task-types/{id}/actions/retire` | POL-TTY-RETIRE |

**القصة:** بصفتي **Administrator / Planner lead**، أريد **إحالة نوع المهمة إلى التقاعد**، لكي يتحقق غرض نوع المهمة: قالب نوع مهمة: متطلبات الأهلية، معايير الإكمال، التصعيد، الانتهاء

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ reason; existing tasks unaffected
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-TTY-RETIRED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator / Planner lead؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TTY-RETIRE` · `AGG-TASK-TYPE` · متطلبات: REQ-OPS-007, REQ-OPS-014 · حالات استخدام: UC-034, UC-041, UC-044, UC-102
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TTY-RETIRE succeeds
  Given AGG-TASK-TYPE in state ACTIVE and every guard holds
  When Administrator / Planner lead sends CMD-TTY-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-TTY-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TTY-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TTY-RETIRE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TASK_TYPE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DRAFT, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC04-Q-TTY-GET — جلب: Task type version

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user of tenant | `GET /api/v1/operations/task-types/{task_type_id}` | POL-TTY-GET |

**القصة:** بصفتي **any user of tenant**، أريد **جلب Task type version**، لكي يتحقق المتطلب: The system shall allow each tenant to configure review and approval steps for plans and tasks within the limits of the state machines

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Task type version
- **الصلاحية:** any user of tenant؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-TTY-GET` · `AGG-TASK-TYPE` · متطلبات: REQ-OPS-014
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-TTY-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-TTY-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-TTY-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-TTY-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

<!-- END GENERATED: build_analysis_design.py -->
