---
id: AD-05-US-BC01
type: user-stories
title: "قصص المستخدم — BC01"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
generator: 17-system-study/_build/build_analysis_design.py
---

# قصص المستخدم — BC01 Foundation — الأساس

مولَّد بالكامل من المصادر بواسطة `17-system-study/_build/build_analysis_design.py`؛ لا يُحرَّر يدويًا. القالب والتصنيف وتعريف ضوابط النوع والفئة في [00-guide.md](00-guide.md).

<!-- BEGIN GENERATED: build_analysis_design.py -->

## ملخص BC01

| نوع العملية | عدد القصص |
|---|---|
| إنشاء | 11 |
| تعديل | 14 |
| جلب | 10 |
| حذف / إنهاء | 11 |
| سير عمل | 26 |
| نظام | 5 |
| نظام (SYS) | 7 |
| **المجموع** | **84** |

### AGG-AUTHORITY-GRANT — منح السلطة (Authority Grant (incl. delegation))

`03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md` · SLC-01 · الحالات: PENDING_APPROVAL, ACTIVE, SUSPENDED → EXPIRED, REVOKED, REJECTED

#### US-BC01-AUT-APPROVE-GRANT — اعتماد منح السلطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | holder of permission authority.grant in scope \| Executive in scope \| holder of parent grant | `POST /api/v1/foundation/authority-grants/{id}/actions/approve-grant` | POL-AUT-APPROVE-GRANT |

**القصة:** بصفتي **holder of permission authority.grant in scope \| Executive in scope \| holder of parent grant**، أريد **اعتماد منح السلطة**، لكي يتحقق غرض منح السلطة: حق تقرير نوع قرار ضمن نطاق وحدود وفترة

- **الشروط المسبقة:** الحالة الحالية ∈ {PENDING_APPROVAL}؛ approver is Executive in scope; approver ≠ requester
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-AUT-GRANTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: approver ≠ requester؛ الالتزامات: audit; mfa
- **الربط:** `CMD-AUT-APPROVE-GRANT` · `AGG-AUTHORITY-GRANT` · متطلبات: REQ-FND-007, REQ-FND-008, REQ-FND-009 · حالات استخدام: UC-032, UC-035, UC-082, UC-083
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AUT-APPROVE-GRANT succeeds
  Given AGG-AUTHORITY-GRANT in state PENDING_APPROVAL and every guard holds
  When holder of permission authority.grant in scope | Executive in scope | holder of parent grant sends CMD-AUT-APPROVE-GRANT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-AUT-GRANTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AUT-APPROVE-GRANT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHORITY_GRANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, EXPIRED, REJECTED, REVOKED, SUSPENDED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AUT-APPROVE-GRANT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ requester |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-AUT-DELEGATE — تفويض منح السلطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate) | `POST /api/v1/foundation/authority-grants/{id}/actions/delegate` | POL-AUT-DELEGATE |

**القصة:** بصفتي **holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)**، أريد **تفويض منح السلطة**، لكي يتحقق غرض منح السلطة: حق تقرير نوع قرار ضمن نطاق وحدود وفترة

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ parent grant effective and delegable; scope ⊆ parent; limits ≤ parent; period ⊆ parent; depth ≤ 2; delegate ≠ delegator
- **المدخلات:** `delegate`!: urn, `decision_types`!: array, `org_scope`!: urn, `include_descendants`!: boolean, `limits`: object, `valid_from`!: date-time, `valid_to`!: date-time, `delegable`!: boolean — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-AUT-DELEGATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: delegate ≠ delegator؛ الالتزامات: audit
- **الربط:** `CMD-AUT-DELEGATE` · `AGG-AUTHORITY-GRANT` · متطلبات: REQ-FND-007, REQ-FND-008, REQ-FND-009 · حالات استخدام: UC-032, UC-035, UC-082, UC-083
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AUT-DELEGATE succeeds
  Given AGG-AUTHORITY-GRANT in state ∅ and every guard holds
  When holder of permission authority.grant in scope | Executive in scope sends CMD-AUT-DELEGATE with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-AUT-DELEGATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AUT-DELEGATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHORITY_EXCEEDS_DELEGATOR | 422 | لم يتحقق الشرط: parent grant effective and delegable; scope ⊆ parent; limits ≤ parent; period ⊆ parent; depth ≤ 2; delegate ≠ delegator |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AUT-DELEGATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: delegate, decision_types, org_scope, include_descendants, valid_from, valid_to, delegable |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-AUT-GRANT — منح منح السلطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate) | `POST /api/v1/foundation/authority-grants` | POL-AUT-GRANT |

**القصة:** بصفتي **holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)**، أريد **منح منح السلطة**، لكي يتحقق غرض منح السلطة: حق تقرير نوع قرار ضمن نطاق وحدود وفترة

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ actor has authority.grant permission; decision type exists; scope unit ACTIVE
- **المدخلات:** `holder`!: urn, `decision_types`!: array, `org_scope`!: urn, `include_descendants`!: boolean, `limits`: object, `valid_from`!: date-time, `valid_to`: date-time, `delegable`!: boolean — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← PENDING_APPROVAL؛ الحدث EVT-AUT-GRANT-REQUESTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AUT-GRANT` · `AGG-AUTHORITY-GRANT` · متطلبات: REQ-FND-007, REQ-FND-008, REQ-FND-009 · حالات استخدام: UC-032, UC-035, UC-082, UC-083
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AUT-GRANT succeeds
  Given AGG-AUTHORITY-GRANT in state ∅ and every guard holds
  When holder of permission authority.grant in scope | Executive in scope sends CMD-AUT-GRANT with a valid payload, a new Idempotency-Key
  Then the state becomes PENDING_APPROVAL
  And EVT-AUT-GRANT-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AUT-GRANT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AUT-GRANT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PERMISSION_DENIED | 403→404 | لم يتحقق الشرط: actor has authority.grant permission; decision type exists; scope unit ACTIVE |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: holder, decision_types, org_scope, include_descendants, valid_from, delegable |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-AUT-REJECT-GRANT — رفض منح السلطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate) | `POST /api/v1/foundation/authority-grants/{id}/actions/reject-grant` | POL-AUT-REJECT-GRANT |

**القصة:** بصفتي **holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)**، أريد **رفض منح السلطة**، لكي يتحقق غرض منح السلطة: حق تقرير نوع قرار ضمن نطاق وحدود وفترة

- **الشروط المسبقة:** الحالة الحالية ∈ {PENDING_APPROVAL}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-AUT-GRANT-REJECTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AUT-REJECT-GRANT` · `AGG-AUTHORITY-GRANT` · متطلبات: REQ-FND-007, REQ-FND-008, REQ-FND-009 · حالات استخدام: UC-032, UC-035, UC-082, UC-083
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AUT-REJECT-GRANT succeeds
  Given AGG-AUTHORITY-GRANT in state PENDING_APPROVAL and every guard holds
  When holder of permission authority.grant in scope | Executive in scope sends CMD-AUT-REJECT-GRANT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-AUT-GRANT-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AUT-REJECT-GRANT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHORITY_GRANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, EXPIRED, REJECTED, REVOKED, SUSPENDED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AUT-REJECT-GRANT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-AUT-RESUME — استئناف منح السلطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate) | `POST /api/v1/foundation/authority-grants/{id}/actions/resume` | POL-AUT-RESUME |

**القصة:** بصفتي **holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)**، أريد **استئناف منح السلطة**، لكي يتحقق غرض منح السلطة: حق تقرير نوع قرار ضمن نطاق وحدود وفترة

- **الشروط المسبقة:** الحالة الحالية ∈ {SUSPENDED}؛ period not ended
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-AUT-RESUMED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AUT-RESUME` · `AGG-AUTHORITY-GRANT` · متطلبات: REQ-FND-007, REQ-FND-008, REQ-FND-009 · حالات استخدام: UC-032, UC-035, UC-082, UC-083
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AUT-RESUME succeeds
  Given AGG-AUTHORITY-GRANT in state SUSPENDED and every guard holds
  When holder of permission authority.grant in scope | Executive in scope sends CMD-AUT-RESUME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-AUT-RESUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AUT-RESUME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHORITY_GRANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, EXPIRED, PENDING_APPROVAL, REJECTED, REVOKED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AUT-RESUME لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | GRANT_EXPIRED | 422 | لم يتحقق الشرط: period not ended |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-AUT-REVOKE — سحب منح السلطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate) | `POST /api/v1/foundation/authority-grants/{id}/actions/revoke` | POL-AUT-REVOKE |

**القصة:** بصفتي **holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)**، أريد **سحب منح السلطة**، لكي يتحقق غرض منح السلطة: حق تقرير نوع قرار ضمن نطاق وحدود وفترة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, PENDING_APPROVAL, SUSPENDED}؛ granter, delegator or Executive in scope; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REVOKED؛ الحدث EVT-AUT-REVOKED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AUT-REVOKE` · `AGG-AUTHORITY-GRANT` · متطلبات: REQ-FND-007, REQ-FND-008, REQ-FND-009 · حالات استخدام: UC-032, UC-035, UC-082, UC-083
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AUT-REVOKE succeeds
  Given AGG-AUTHORITY-GRANT in state ACTIVE or PENDING_APPROVAL or SUSPENDED and every guard holds
  When holder of permission authority.grant in scope | Executive in scope sends CMD-AUT-REVOKE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REVOKED
  And EVT-AUT-REVOKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AUT-REVOKE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHORITY_GRANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, REJECTED, REVOKED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AUT-REVOKE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-AUT-SUSPEND — تعليق منح السلطة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate) | `POST /api/v1/foundation/authority-grants/{id}/actions/suspend` | POL-AUT-SUSPEND |

**القصة:** بصفتي **holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)**، أريد **تعليق منح السلطة**، لكي يتحقق غرض منح السلطة: حق تقرير نوع قرار ضمن نطاق وحدود وفترة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← SUSPENDED؛ الحدث EVT-AUT-SUSPENDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AUT-SUSPEND` · `AGG-AUTHORITY-GRANT` · متطلبات: REQ-FND-007, REQ-FND-008, REQ-FND-009 · حالات استخدام: UC-032, UC-035, UC-082, UC-083
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AUT-SUSPEND succeeds
  Given AGG-AUTHORITY-GRANT in state ACTIVE and every guard holds
  When holder of permission authority.grant in scope | Executive in scope sends CMD-AUT-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUSPENDED
  And EVT-AUT-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AUT-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHORITY_GRANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, PENDING_APPROVAL, REJECTED, REVOKED, SUSPENDED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AUT-SUSPEND لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-S-AUTHORITY-GRANT-01 — تلقائي: valid_to reached (منح السلطة)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | ACTIVE, SUSPENDED | EXPIRED |

**القصة:** بصفتي **النظام**، عند «valid_to reached»، أريد نقل **منح السلطة** إلى EXPIRED، لكي يتحقق غرض منح السلطة: حق تقرير نوع قرار ضمن نطاق وحدود وفترة

- **الشرط:** system scheduler
- **المخرجات:** الحدث EVT-AUT-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-AUTHORITY-GRANT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC01-Q-AUT-CHECK — جلب: AuthorityCheck(actor, decision_type, scope, at, amount?)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | internal services (workload identity) or self | `POST /api/v1/foundation/authority-checks` | POL-AUT-CHECK |

**القصة:** بصفتي **internal services (workload identity) or self**، أريد **جلب AuthorityCheck(actor, decision_type, scope, at, amount?)**، لكي يتحقق المتطلب: The system shall provide an authority check returning whether an actor holds authority for a given decision type, scope and point in time, including through delegation

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** AuthorityCheck(actor, decision_type, scope, at, amount?)
- **الصلاحية:** internal services (workload identity) or self؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AUT-CHECK` · `AGG-AUTHORITY-GRANT` · متطلبات: REQ-FND-009
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-AUT-CHECK returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-AUT-CHECK
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-AUT-CHECK is denied
  Given the policy denies the caller
  When the caller sends QRY-AUT-CHECK
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC01-Q-AUT-LIST — جلب: Grants by holder / scope / effective at t

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | Executive or Administrator in scope, or holder | `GET /api/v1/foundation/authority-grants` | POL-AUT-LIST |

**القصة:** بصفتي **Executive or Administrator in scope, or holder**، أريد **جلب Grants by holder / scope / effective at t**، لكي يتحقق المتطلب: The system shall record authority as a grant stating decision type, organizational scope, limits and validity period, held by a role or a person

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Grants by holder / scope / effective at t؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Executive or Administrator in scope, or holder؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AUT-LIST` · `AGG-AUTHORITY-GRANT` · متطلبات: REQ-FND-007
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-AUT-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-AUT-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-AUT-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-AUT-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-CLEARANCE — التصريح الأمني (Clearance)

`03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md` · SLC-01 · الحالات: PENDING_APPROVAL, ACTIVE, SUSPENDED → EXPIRED, REVOKED

#### US-BC01-CLR-APPROVE — اعتماد التصريح الأمني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Security Officer | `POST /api/v1/foundation/clearances/{id}/actions/approve` | POL-CLR-APPROVE |

**القصة:** بصفتي **Security Officer**، أريد **اعتماد التصريح الأمني**، لكي يتحقق غرض التصريح الأمني: مستوى التصريح والأقسام لمستخدم

- **الشروط المسبقة:** الحالة الحالية ∈ {PENDING_APPROVAL}؛ second Security Officer ≠ requester when level is top rank; else requester may self-confirm
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-CLR-GRANTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: approver ≠ requester ≠ subject (top rank)؛ الالتزامات: audit; mfa
- **الربط:** `CMD-CLR-APPROVE` · `AGG-CLEARANCE` · متطلبات: REQ-GOV-003, REQ-GOV-004 · حالات استخدام: UC-085, UC-089
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLR-APPROVE succeeds
  Given AGG-CLEARANCE in state PENDING_APPROVAL and every guard holds
  When Security Officer sends CMD-CLR-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-CLR-GRANTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLR-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLR-APPROVE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLEARANCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, EXPIRED, REVOKED, SUSPENDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ requester ≠ subject (top rank) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-CLR-GRANT — منح التصريح الأمني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | Security Officer | `POST /api/v1/foundation/clearances` | POL-CLR-GRANT |

**القصة:** بصفتي **Security Officer**، أريد **منح التصريح الأمني**، لكي يتحقق غرض التصريح الأمني: مستوى التصريح والأقسام لمستخدم

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ Security Officer; level and compartments exist in ACTIVE scheme; subject has no other non-terminal clearance
- **المدخلات:** `user`!: urn, `level`!: string, `compartments`!: array, `caveat_attributes`: object, `valid_to`: date-time — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← PENDING_APPROVAL؛ الحدث EVT-CLR-REQUESTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: requester ≠ subject؛ الالتزامات: audit; mfa
- **الربط:** `CMD-CLR-GRANT` · `AGG-CLEARANCE` · متطلبات: REQ-GOV-003, REQ-GOV-004 · حالات استخدام: UC-085, UC-089
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLR-GRANT succeeds
  Given AGG-CLEARANCE in state ∅ and every guard holds
  When Security Officer sends CMD-CLR-GRANT with a valid payload, a new Idempotency-Key
  Then the state becomes PENDING_APPROVAL
  And EVT-CLR-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLR-GRANT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLR-GRANT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLEARANCE_EXISTS | 422 | لم يتحقق الشرط: Security Officer; level and compartments exist in ACTIVE scheme; subject has no other non-terminal clearance |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: user, level, compartments |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-CLR-MODIFY — تعديل التصريح الأمني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | حوكمة وأمن | Security Officer | `POST /api/v1/foundation/clearances/{id}/actions/modify` | POL-CLR-MODIFY |

**القصة:** بصفتي **Security Officer**، أريد **تعديل التصريح الأمني**، لكي يتحقق غرض التصريح الأمني: مستوى التصريح والأقسام لمستخدم

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ same rules as grant; creates new version
- **المدخلات:** `level`!: string, `compartments`!: array, `caveat_attributes`: object — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-CLR-MODIFIED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLR-MODIFY` · `AGG-CLEARANCE` · متطلبات: REQ-GOV-003, REQ-GOV-004 · حالات استخدام: UC-085, UC-089
- **ضوابط النوع والفئة:** C-UPD، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLR-MODIFY succeeds
  Given AGG-CLEARANCE in state ACTIVE and every guard holds
  When Security Officer sends CMD-CLR-MODIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-CLR-MODIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLR-MODIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLR-MODIFY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLEARANCE_INVALID | 422 | لم يتحقق الشرط: same rules as grant; creates new version |
    | CLEARANCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, PENDING_APPROVAL, REVOKED, SUSPENDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: level, compartments |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-CLR-REINSTATE — إعادة التصريح الأمني إلى السريان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Security Officer | `POST /api/v1/foundation/clearances/{id}/actions/reinstate` | POL-CLR-REINSTATE |

**القصة:** بصفتي **Security Officer**، أريد **إعادة التصريح الأمني إلى السريان**، لكي يتحقق غرض التصريح الأمني: مستوى التصريح والأقسام لمستخدم

- **الشروط المسبقة:** الحالة الحالية ∈ {SUSPENDED}؛ period not ended
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-CLR-REINSTATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLR-REINSTATE` · `AGG-CLEARANCE` · متطلبات: REQ-GOV-003, REQ-GOV-004 · حالات استخدام: UC-085, UC-089
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLR-REINSTATE succeeds
  Given AGG-CLEARANCE in state SUSPENDED and every guard holds
  When Security Officer sends CMD-CLR-REINSTATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-CLR-REINSTATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLR-REINSTATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLR-REINSTATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLEARANCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, EXPIRED, PENDING_APPROVAL, REVOKED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-CLR-REVOKE — سحب التصريح الأمني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Security Officer | `POST /api/v1/foundation/clearances/{id}/actions/revoke` | POL-CLR-REVOKE |

**القصة:** بصفتي **Security Officer**، أريد **سحب التصريح الأمني**، لكي يتحقق غرض التصريح الأمني: مستوى التصريح والأقسام لمستخدم

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, PENDING_APPROVAL, SUSPENDED}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REVOKED؛ الحدث EVT-CLR-REVOKED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLR-REVOKE` · `AGG-CLEARANCE` · متطلبات: REQ-GOV-003, REQ-GOV-004 · حالات استخدام: UC-085, UC-089
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLR-REVOKE succeeds
  Given AGG-CLEARANCE in state ACTIVE or PENDING_APPROVAL or SUSPENDED and every guard holds
  When Security Officer sends CMD-CLR-REVOKE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REVOKED
  And EVT-CLR-REVOKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLR-REVOKE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLR-REVOKE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLEARANCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, REVOKED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-CLR-SUSPEND — تعليق التصريح الأمني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Security Officer | `POST /api/v1/foundation/clearances/{id}/actions/suspend` | POL-CLR-SUSPEND |

**القصة:** بصفتي **Security Officer**، أريد **تعليق التصريح الأمني**، لكي يتحقق غرض التصريح الأمني: مستوى التصريح والأقسام لمستخدم

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← SUSPENDED؛ الحدث EVT-CLR-SUSPENDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Security Officer؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-CLR-SUSPEND` · `AGG-CLEARANCE` · متطلبات: REQ-GOV-003, REQ-GOV-004 · حالات استخدام: UC-085, UC-089
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-CLR-SUSPEND succeeds
  Given AGG-CLEARANCE in state ACTIVE and every guard holds
  When Security Officer sends CMD-CLR-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUSPENDED
  And EVT-CLR-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-CLR-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-CLR-SUSPEND لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CLEARANCE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, PENDING_APPROVAL, REVOKED, SUSPENDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-S-CLEARANCE-01 — تلقائي: valid_to reached (التصريح الأمني)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | ACTIVE, SUSPENDED | EXPIRED |

**القصة:** بصفتي **النظام**، عند «valid_to reached»، أريد نقل **التصريح الأمني** إلى EXPIRED، لكي يتحقق غرض التصريح الأمني: مستوى التصريح والأقسام لمستخدم

- **الشرط:** system
- **المخرجات:** الحدث EVT-CLR-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-CLEARANCE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC01-Q-CLR-GET — جلب: Current clearance (level/compartments)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | حوكمة وأمن | Security Officer or self | `GET /api/v1/foundation/users/{user_id}/clearance` | POL-CLR-GET |

**القصة:** بصفتي **Security Officer or self**، أريد **جلب Current clearance (level/compartments)**، لكي يتحقق المتطلب: The system shall permit read access to an object only if the subject's clearance is at least the object's level and the subject holds every compartment of the object

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Current clearance (level/compartments)؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Security Officer or self؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-CLR-GET` · `AGG-CLEARANCE` · متطلبات: REQ-GOV-003
- **ضوابط النوع والفئة:** C-READ، K-GOV

```gherkin
Scenario: QRY-CLR-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-CLR-GET with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-CLR-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-CLR-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-DEVICE — الجهاز الميداني (Field Device)

`03-domain/contexts/BC01/aggregates/AGG-DEVICE.md` · SLC-11 · الحالات: PENDING_ENROLLMENT, ACTIVE, SUSPENDED, LOST → WIPED, RETIRED

#### US-BC01-DEV-CONFIRM — تأكيد الجهاز الميداني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | Administrator / MDM policy | `POST /api/v1/foundation/devices/{id}/actions/confirm` | POL-DEV-CONFIRM |

**القصة:** بصفتي **Administrator / MDM policy**، أريد **تأكيد الجهاز الميداني**، لكي يتحقق غرض الجهاز الميداني: جهاز ميداني مسجل ومربوط بمستخدم ومفتاح

- **الشروط المسبقة:** الحالة الحالية ∈ {PENDING_ENROLLMENT}؛ hardware attestation valid (or MDM compliance); Administrator or MDM policy
- **المدخلات:** `attestation`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-DEV-ACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-DEV-CONFIRM` · `AGG-DEVICE` · متطلبات: REQ-OFF-005 · حالات استخدام: UC-093
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DEV-CONFIRM succeeds
  Given AGG-DEVICE in state PENDING_ENROLLMENT and every guard holds
  When Administrator / MDM policy sends CMD-DEV-CONFIRM with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-DEV-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DEV-CONFIRM is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ATTESTATION_FAILED | 422 | لم يتحقق الشرط: hardware attestation valid (or MDM compliance); Administrator or MDM policy |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DEV-CONFIRM لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DEVICE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, LOST, RETIRED, SUSPENDED, WIPED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: attestation |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-DEV-ENROLL — تسجيل الجهاز الميداني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | تكامل | user | `POST /api/v1/foundation/devices` | POL-DEV-ENROLL |

**القصة:** بصفتي **user**، أريد **تسجيل الجهاز الميداني**، لكي يتحقق غرض الجهاز الميداني: جهاز ميداني مسجل ومربوط بمستخدم ومفتاح

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ user ACTIVE; device public key; platform; MDM reference; ≤ 3 active devices per user
- **المدخلات:** `user`!: urn, `public_key`!: string, `platform`!: enum(android, `mdm_ref`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← PENDING_ENROLLMENT؛ الحدث EVT-DEV-ENROLL-REQUESTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DEV-ENROLL` · `AGG-DEVICE` · متطلبات: REQ-OFF-005 · حالات استخدام: UC-093
- **ضوابط النوع والفئة:** C-CRE، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DEV-ENROLL succeeds
  Given AGG-DEVICE in state ∅ and every guard holds
  When user sends CMD-DEV-ENROLL with a valid payload, a new Idempotency-Key
  Then the state becomes PENDING_ENROLLMENT
  And EVT-DEV-ENROLL-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DEV-ENROLL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DEV-ENROLL لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DEVICE_LIMIT_REACHED | 422 | لم يتحقق الشرط: user ACTIVE; device public key; platform; MDM reference; ≤ 3 active devices per user |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: user, public_key, platform |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-DEV-REINSTATE — إعادة الجهاز الميداني إلى السريان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | Administrator / MDM policy | `POST /api/v1/foundation/devices/{id}/actions/reinstate` | POL-DEV-REINSTATE |

**القصة:** بصفتي **Administrator / MDM policy**، أريد **إعادة الجهاز الميداني إلى السريان**، لكي يتحقق غرض الجهاز الميداني: جهاز ميداني مسجل ومربوط بمستخدم ومفتاح

- **الشروط المسبقة:** الحالة الحالية ∈ {SUSPENDED}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-DEV-REINSTATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DEV-REINSTATE` · `AGG-DEVICE` · متطلبات: REQ-OFF-005 · حالات استخدام: UC-093
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DEV-REINSTATE succeeds
  Given AGG-DEVICE in state SUSPENDED and every guard holds
  When Administrator / MDM policy sends CMD-DEV-REINSTATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-DEV-REINSTATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DEV-REINSTATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DEV-REINSTATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DEVICE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, LOST, PENDING_ENROLLMENT, RETIRED, WIPED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-DEV-REPORT-LOST — الإبلاغ عن فقد الجهاز الميداني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | user | `POST /api/v1/foundation/devices/{id}/actions/report-lost` | POL-DEV-REPORT-LOST |

**القصة:** بصفتي **user**، أريد **الإبلاغ عن فقد الجهاز الميداني**، لكي يتحقق غرض الجهاز الميداني: جهاز ميداني مسجل ومربوط بمستخدم ومفتاح

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, SUSPENDED}؛ user or Security Officer; key revoked immediately; wipe instruction queued; queued commands from the device after the lost time require review
- **المدخلات:** `lost_at`!: date-time, `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← LOST؛ الحدث EVT-DEV-REPORTED-LOST؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DEV-REPORT-LOST` · `AGG-DEVICE` · متطلبات: REQ-OFF-005 · حالات استخدام: UC-093
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DEV-REPORT-LOST succeeds
  Given AGG-DEVICE in state ACTIVE or SUSPENDED and every guard holds
  When user sends CMD-DEV-REPORT-LOST with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes LOST
  And EVT-DEV-REPORTED-LOST is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DEV-REPORT-LOST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DEV-REPORT-LOST لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DEVICE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: LOST, PENDING_ENROLLMENT, RETIRED, WIPED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: lost_at |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-DEV-RETIRE — إحالة الجهاز الميداني إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | Administrator / MDM policy | `POST /api/v1/foundation/devices/{id}/actions/retire` | POL-DEV-RETIRE |

**القصة:** بصفتي **Administrator / MDM policy**، أريد **إحالة الجهاز الميداني إلى التقاعد**، لكي يتحقق غرض الجهاز الميداني: جهاز ميداني مسجل ومربوط بمستخدم ومفتاح

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, SUSPENDED}؛ device synced and wiped (confirmation) or Security Officer override
- **المدخلات:** `reason`!: string, `override`: boolean — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-DEV-RETIRED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit; mfa
- **الربط:** `CMD-DEV-RETIRE` · `AGG-DEVICE` · متطلبات: REQ-OFF-005 · حالات استخدام: UC-093
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DEV-RETIRE succeeds
  Given AGG-DEVICE in state ACTIVE or SUSPENDED and every guard holds
  When Administrator / MDM policy sends CMD-DEV-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-DEV-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DEV-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DEV-RETIRE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DEVICE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: LOST, PENDING_ENROLLMENT, RETIRED, WIPED |
    | DEVICE_NOT_WIPED | 422 | لم يتحقق الشرط: device synced and wiped (confirmation) or Security Officer override |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-DEV-ROTATE-KEY — تدوير مفتاح الجهاز الميداني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | تكامل | user · Administrator / MDM policy · Security Officer | `POST /api/v1/foundation/devices/{id}/actions/rotate-key` | POL-DEV-ROTATE-KEY |

**القصة:** بصفتي **user · Administrator / MDM policy · Security Officer**، أريد **تدوير مفتاح الجهاز الميداني**، لكي يتحقق غرض الجهاز الميداني: جهاز ميداني مسجل ومربوط بمستخدم ومفتاح

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ signed by current key; new public key
- **المدخلات:** `new_public_key`!: string, `signature`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-DEV-KEY-ROTATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DEV-ROTATE-KEY` · `AGG-DEVICE` · متطلبات: REQ-OFF-005 · حالات استخدام: UC-093
- **ضوابط النوع والفئة:** C-UPD، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DEV-ROTATE-KEY succeeds
  Given AGG-DEVICE in state ACTIVE and every guard holds
  When user · Administrator / MDM policy · Security Officer sends CMD-DEV-ROTATE-KEY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-DEV-KEY-ROTATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DEV-ROTATE-KEY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DEV-ROTATE-KEY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DEVICE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: LOST, PENDING_ENROLLMENT, RETIRED, SUSPENDED, WIPED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SIGNATURE_INVALID | 422 | لم يتحقق الشرط: signed by current key; new public key |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: new_public_key, signature |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-DEV-SUSPEND — تعليق الجهاز الميداني

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | تكامل | Administrator / MDM policy | `POST /api/v1/foundation/devices/{id}/actions/suspend` | POL-DEV-SUSPEND |

**القصة:** بصفتي **Administrator / MDM policy**، أريد **تعليق الجهاز الميداني**، لكي يتحقق غرض الجهاز الميداني: جهاز ميداني مسجل ومربوط بمستخدم ومفتاح

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ reason; sync rejected while suspended
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← SUSPENDED؛ الحدث EVT-DEV-SUSPENDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)؛ الشروط: tenant match; device ACTIVE where applicable; device signature for SYN؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-DEV-SUSPEND` · `AGG-DEVICE` · متطلبات: REQ-OFF-005 · حالات استخدام: UC-093
- **ضوابط النوع والفئة:** C-WF، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-DEV-SUSPEND succeeds
  Given AGG-DEVICE in state ACTIVE and every guard holds
  When Administrator / MDM policy sends CMD-DEV-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUSPENDED
  And EVT-DEV-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-DEV-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-DEV-SUSPEND لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | DEVICE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: LOST, PENDING_ENROLLMENT, RETIRED, SUSPENDED, WIPED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-S-DEVICE-01 — تلقائي: wipe confirmed by device (الجهاز الميداني)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | LOST | WIPED |

**القصة:** بصفتي **النظام**، عند «wipe confirmed by device»، أريد نقل **الجهاز الميداني** إلى WIPED، لكي يتحقق غرض الجهاز الميداني: جهاز ميداني مسجل ومربوط بمستخدم ومفتاح

- **الشرط:** device acknowledges wipe on next contact
- **المخرجات:** الحدث EVT-DEV-WIPED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-DEVICE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC01-Q-DEV-LIST — جلب: Devices of a user (self) or in scope (Administrator)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | self; Administrator in scope | `GET /api/v1/foundation/devices` | POL-DEV-LIST |

**القصة:** بصفتي **self; Administrator in scope**، أريد **جلب Devices of a user (self) or in scope (Administrator)**، لكي يتحقق المتطلب: The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Devices of a user (self) or in scope (Administrator)؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** self; Administrator in scope؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-DEV-LIST` · `AGG-DEVICE` · متطلبات: REQ-OFF-005
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-DEV-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-DEV-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-DEV-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-DEV-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-HR-SYNC-PROPOSAL — مقترح مزامنة الموارد البشرية (HR Sync Proposal)

`03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md` · SLC-16 · الحالات: PROPOSED → APPROVED, REJECTED, SUPERSEDED, EXPIRED

#### US-BC01-HRS-APPROVE — اعتماد مقترح مزامنة الموارد البشرية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | Administrator in scope | `POST /api/v1/foundation/hr-sync-proposals/{id}/actions/approve` | POL-HRS-APPROVE |

**القصة:** بصفتي **Administrator in scope**، أريد **اعتماد مقترح مزامنة الموارد البشرية**، لكي يتحقق غرض مقترح مزامنة الموارد البشرية: تغيير دور أو وحدة من HRIS يُقترح على المسؤول ولا يُطبق آلياً

- **الشروط المسبقة:** الحالة الحالية ∈ {PROPOSED}؛ Administrator in scope of the affected units; applies CMD-RAS-ASSIGN / CMD-RAS-REVOKE and, for leave, CMD-USR-DISABLE — each through its own guards
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← APPROVED؛ الحدث EVT-HRS-APPROVED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator in scope؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-HRS-APPROVE` · `AGG-HR-SYNC-PROPOSAL` · متطلبات: REQ-INT-004 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-HRS-APPROVE succeeds
  Given AGG-HR-SYNC-PROPOSAL in state PROPOSED and every guard holds
  When Administrator in scope sends CMD-HRS-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes APPROVED
  And EVT-HRS-APPROVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-HRS-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-HRS-APPROVE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, EXPIRED, REJECTED, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OWNER_REJECTED | 422 | لم يتحقق الشرط: Administrator in scope of the affected units; applies CMD-RAS-ASSIGN / CMD-RAS-REVOKE and, for leave, CMD-USR-DISABLE — each through its own guards |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-HRS-REJECT — رفض مقترح مزامنة الموارد البشرية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | تكامل | Administrator in scope | `POST /api/v1/foundation/hr-sync-proposals/{id}/actions/reject` | POL-HRS-REJECT |

**القصة:** بصفتي **Administrator in scope**، أريد **رفض مقترح مزامنة الموارد البشرية**، لكي يتحقق غرض مقترح مزامنة الموارد البشرية: تغيير دور أو وحدة من HRIS يُقترح على المسؤول ولا يُطبق آلياً

- **الشروط المسبقة:** الحالة الحالية ∈ {PROPOSED}؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-HRS-REJECTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator in scope؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-HRS-REJECT` · `AGG-HR-SYNC-PROPOSAL` · متطلبات: REQ-INT-004 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-DEL، K-INT (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-HRS-REJECT succeeds
  Given AGG-HR-SYNC-PROPOSAL in state PROPOSED and every guard holds
  When Administrator in scope sends CMD-HRS-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-HRS-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-HRS-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-HRS-REJECT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: APPROVED, EXPIRED, REJECTED, SUPERSEDED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-S-HR-SYNC-PROPOSAL-01 — تلقائي: HRIS change received (مقترح مزامنة الموارد البشرية)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ∅ | PROPOSED |

**القصة:** بصفتي **النظام**، عند «HRIS change received»، أريد نقل **مقترح مزامنة الموارد البشرية** إلى PROPOSED، لكي يتحقق غرض مقترح مزامنة الموارد البشرية: تغيير دور أو وحدة من HRIS يُقترح على المسؤول ولا يُطبق آلياً

- **الشرط:** person matched to a platform Person by HR identifier; change ∈ {join, leave, move_unit, change_position}; mapped to proposed role-assignment changes by tenant mapping table
- **المخرجات:** الحدث EVT-HRS-PROPOSED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-HR-SYNC-PROPOSAL` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC01-S-HR-SYNC-PROPOSAL-02 — تلقائي: newer HR change for the same person (مقترح مزامنة الموارد البشرية)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | PROPOSED | SUPERSEDED |

**القصة:** بصفتي **النظام**، عند «newer HR change for the same person»، أريد نقل **مقترح مزامنة الموارد البشرية** إلى SUPERSEDED، لكي يتحقق غرض مقترح مزامنة الموارد البشرية: تغيير دور أو وحدة من HRIS يُقترح على المسؤول ولا يُطبق آلياً

- **الشرط:** system
- **المخرجات:** الحدث EVT-HRS-SUPERSEDED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-HR-SYNC-PROPOSAL` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC01-S-HR-SYNC-PROPOSAL-03 — تلقائي: 14 days without decision (مقترح مزامنة الموارد البشرية)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي | النظام بهوية عبء عمل | PROPOSED | EXPIRED |

**القصة:** بصفتي **النظام**، عند «14 days without decision»، أريد نقل **مقترح مزامنة الموارد البشرية** إلى EXPIRED، لكي يتحقق غرض مقترح مزامنة الموارد البشرية: تغيير دور أو وحدة من HRIS يُقترح على المسؤول ولا يُطبق آلياً

- **الشرط:** scheduler; escalated to Security Officer for leave events
- **المخرجات:** الحدث EVT-HRS-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-HR-SYNC-PROPOSAL` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC01-Q-HRS-QUEUE — جلب: Pending HR proposals by unit and change kind (leave first)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | تكامل | Administrator in scope, Security Officer | `GET /api/v1/foundation/hr-sync-proposals` | POL-HRS-QUEUE |

**القصة:** بصفتي **Administrator in scope, Security Officer**، أريد **جلب Pending HR proposals by unit and change kind (leave first)**، لكي يتحقق المتطلب: When HRIS reports a change of role or organization for a person, the system shall propose the corresponding role-assignment change for administrator approval

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Pending HR proposals by unit and change kind (leave first)؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Administrator in scope, Security Officer؛ النطاق المسموح: —؛ عند الرفض: DENY
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-HRS-QUEUE` · `AGG-HR-SYNC-PROPOSAL` · متطلبات: REQ-INT-004
- **ضوابط النوع والفئة:** C-READ، K-INT

```gherkin
Scenario: QRY-HRS-QUEUE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-HRS-QUEUE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-HRS-QUEUE is denied
  Given the policy denies the caller
  When the caller sends QRY-HRS-QUEUE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-ORGANIZATION — المؤسسة (Organization (with unit tree))

`03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md` · SLC-01 · الحالات: ACTIVE, INACTIVE → —

#### US-BC01-ORG-ADD-UNIT — إضافة وحدة تنظيمية إلى المؤسسة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Administrator with org scope ⊇ target | `POST /api/v1/foundation/organizations/{id}/actions/add-unit` | POL-ORG-ADD-UNIT |

**القصة:** بصفتي **Administrator with org scope ⊇ target**، أريد **إضافة وحدة تنظيمية إلى المؤسسة**، لكي يتحقق غرض المؤسسة: مؤسسة داخل مستأجر مع شجرة وحداتها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ parent unit ACTIVE; sibling name unique
- **المدخلات:** `parent_unit`!: urn, `name`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ORG-UNIT-ADDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ target؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ORG-ADD-UNIT` · `AGG-ORGANIZATION` · متطلبات: REQ-FND-002 · حالات استخدام: UC-081
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ORG-ADD-UNIT succeeds
  Given AGG-ORGANIZATION in state ACTIVE and every guard holds
  When Administrator with org scope ⊇ target sends CMD-ORG-ADD-UNIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-ORG-UNIT-ADDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ORG-ADD-UNIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ORG-ADD-UNIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ORGANIZATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: INACTIVE |
    | ORG_UNIT_INVALID_PARENT | 422 | لم يتحقق الشرط: parent unit ACTIVE; sibling name unique |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: parent_unit, name |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-ORG-CREATE — إنشاء المؤسسة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Administrator with org scope ⊇ target | `POST /api/v1/foundation/organizations` | POL-ORG-CREATE |

**القصة:** بصفتي **Administrator with org scope ⊇ target**، أريد **إنشاء المؤسسة**، لكي يتحقق غرض المؤسسة: مؤسسة داخل مستأجر مع شجرة وحداتها

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ tenant ACTIVE; name unique in tenant; creates root unit
- **المدخلات:** `name`!: LocalizedName, `root_unit_name`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-ORG-CREATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ target؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ORG-CREATE` · `AGG-ORGANIZATION` · متطلبات: REQ-FND-002 · حالات استخدام: UC-081
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ORG-CREATE succeeds
  Given AGG-ORGANIZATION in state ∅ and every guard holds
  When Administrator with org scope ⊇ target sends CMD-ORG-CREATE with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-ORG-CREATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ORG-CREATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ORG-CREATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ORG_NAME_TAKEN | 422 | لم يتحقق الشرط: tenant ACTIVE; name unique in tenant; creates root unit |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: name, root_unit_name |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-ORG-DEACTIVATE — إيقاف تفعيل المؤسسة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Administrator with org scope ⊇ target | `POST /api/v1/foundation/organizations/{id}/actions/deactivate` | POL-ORG-DEACTIVATE |

**القصة:** بصفتي **Administrator with org scope ⊇ target**، أريد **إيقاف تفعيل المؤسسة**، لكي يتحقق غرض المؤسسة: مؤسسة داخل مستأجر مع شجرة وحداتها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ all non-root units inactive; no active assignments
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← INACTIVE؛ الحدث EVT-ORG-DEACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ target؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ORG-DEACTIVATE` · `AGG-ORGANIZATION` · متطلبات: REQ-FND-002 · حالات استخدام: UC-081
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ORG-DEACTIVATE succeeds
  Given AGG-ORGANIZATION in state ACTIVE and every guard holds
  When Administrator with org scope ⊇ target sends CMD-ORG-DEACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes INACTIVE
  And EVT-ORG-DEACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ORG-DEACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ORG-DEACTIVATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ORGANIZATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: INACTIVE |
    | ORG_IN_USE | 422 | لم يتحقق الشرط: all non-root units inactive; no active assignments |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-ORG-DEACTIVATE-UNIT — إيقاف وحدة تنظيمية في المؤسسة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Administrator with org scope ⊇ target | `POST /api/v1/foundation/organizations/{id}/actions/deactivate-unit` | POL-ORG-DEACTIVATE-UNIT |

**القصة:** بصفتي **Administrator with org scope ⊇ target**، أريد **إيقاف وحدة تنظيمية في المؤسسة**، لكي يتحقق غرض المؤسسة: مؤسسة داخل مستأجر مع شجرة وحداتها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ no active children; no active role assignments, grants or clearances scoped only to it (BC01 query)
- **المدخلات:** `unit`!: urn, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ORG-UNIT-DEACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ target؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ORG-DEACTIVATE-UNIT` · `AGG-ORGANIZATION` · متطلبات: REQ-FND-002 · حالات استخدام: UC-081
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ORG-DEACTIVATE-UNIT succeeds
  Given AGG-ORGANIZATION in state ACTIVE and every guard holds
  When Administrator with org scope ⊇ target sends CMD-ORG-DEACTIVATE-UNIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-ORG-UNIT-DEACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ORG-DEACTIVATE-UNIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ORG-DEACTIVATE-UNIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ORGANIZATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: INACTIVE |
    | ORG_UNIT_IN_USE | 422 | لم يتحقق الشرط: no active children; no active role assignments, grants or clearances scoped only to it (BC01 query) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: unit, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-ORG-MOVE-UNIT — نقل وحدة تنظيمية في المؤسسة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Administrator with org scope ⊇ target | `POST /api/v1/foundation/organizations/{id}/actions/move-unit` | POL-ORG-MOVE-UNIT |

**القصة:** بصفتي **Administrator with org scope ⊇ target**، أريد **نقل وحدة تنظيمية في المؤسسة**، لكي يتحقق غرض المؤسسة: مؤسسة داخل مستأجر مع شجرة وحداتها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ new parent ACTIVE, same org, not a descendant (no cycle); root cannot move
- **المدخلات:** `unit`!: urn, `new_parent`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ORG-UNIT-MOVED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ target؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ORG-MOVE-UNIT` · `AGG-ORGANIZATION` · متطلبات: REQ-FND-002 · حالات استخدام: UC-081
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ORG-MOVE-UNIT succeeds
  Given AGG-ORGANIZATION in state ACTIVE and every guard holds
  When Administrator with org scope ⊇ target sends CMD-ORG-MOVE-UNIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-ORG-UNIT-MOVED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ORG-MOVE-UNIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ORG-MOVE-UNIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ORGANIZATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: INACTIVE |
    | ORG_UNIT_CYCLE | 422 | لم يتحقق الشرط: new parent ACTIVE, same org, not a descendant (no cycle); root cannot move |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: unit, new_parent |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-ORG-REACTIVATE — إعادة تفعيل المؤسسة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Administrator with org scope ⊇ target | `POST /api/v1/foundation/organizations/{id}/actions/reactivate` | POL-ORG-REACTIVATE |

**القصة:** بصفتي **Administrator with org scope ⊇ target**، أريد **إعادة تفعيل المؤسسة**، لكي يتحقق غرض المؤسسة: مؤسسة داخل مستأجر مع شجرة وحداتها

- **الشروط المسبقة:** الحالة الحالية ∈ {INACTIVE}؛ tenant ACTIVE
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-ORG-REACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ target؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ORG-REACTIVATE` · `AGG-ORGANIZATION` · متطلبات: REQ-FND-002 · حالات استخدام: UC-081
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ORG-REACTIVATE succeeds
  Given AGG-ORGANIZATION in state INACTIVE and every guard holds
  When Administrator with org scope ⊇ target sends CMD-ORG-REACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-ORG-REACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ORG-REACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ORG-REACTIVATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ORGANIZATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-ORG-RENAME — إعادة تسمية المؤسسة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Administrator with org scope ⊇ target | `POST /api/v1/foundation/organizations/{id}/actions/rename` | POL-ORG-RENAME |

**القصة:** بصفتي **Administrator with org scope ⊇ target**، أريد **إعادة تسمية المؤسسة**، لكي يتحقق غرض المؤسسة: مؤسسة داخل مستأجر مع شجرة وحداتها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ name unique in tenant
- **المدخلات:** `name`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ORG-RENAMED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ target؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ORG-RENAME` · `AGG-ORGANIZATION` · متطلبات: REQ-FND-002 · حالات استخدام: UC-081
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ORG-RENAME succeeds
  Given AGG-ORGANIZATION in state ACTIVE and every guard holds
  When Administrator with org scope ⊇ target sends CMD-ORG-RENAME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-ORG-RENAMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ORG-RENAME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ORG-RENAME لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ORGANIZATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: INACTIVE |
    | ORG_NAME_TAKEN | 422 | لم يتحقق الشرط: name unique in tenant |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: name |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-ORG-RENAME-UNIT — إعادة تسمية وحدة تنظيمية في المؤسسة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Administrator with org scope ⊇ target | `POST /api/v1/foundation/organizations/{id}/actions/rename-unit` | POL-ORG-RENAME-UNIT |

**القصة:** بصفتي **Administrator with org scope ⊇ target**، أريد **إعادة تسمية وحدة تنظيمية في المؤسسة**، لكي يتحقق غرض المؤسسة: مؤسسة داخل مستأجر مع شجرة وحداتها

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ sibling name unique
- **المدخلات:** `unit`!: urn, `name`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ORG-UNIT-RENAMED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ target؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ORG-RENAME-UNIT` · `AGG-ORGANIZATION` · متطلبات: REQ-FND-002 · حالات استخدام: UC-081
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ORG-RENAME-UNIT succeeds
  Given AGG-ORGANIZATION in state ACTIVE and every guard holds
  When Administrator with org scope ⊇ target sends CMD-ORG-RENAME-UNIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-ORG-UNIT-RENAMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ORG-RENAME-UNIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ORG-RENAME-UNIT لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ORGANIZATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: INACTIVE |
    | ORG_UNIT_NAME_TAKEN | 422 | لم يتحقق الشرط: sibling name unique |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: unit, name |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-Q-ORG-TREE — جلب: Unit tree (cursor pagination on flattened order)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | any user of tenant (view org structure) | `GET /api/v1/foundation/organizations/{org_id}/units` | POL-ORG-TREE |

**القصة:** بصفتي **any user of tenant (view org structure)**، أريد **جلب Unit tree (cursor pagination on flattened order)**، لكي يتحقق المتطلب: The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational units of unlimited depth

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Unit tree (cursor pagination on flattened order)؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** any user of tenant (view org structure)؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ORG-TREE` · `AGG-ORGANIZATION` · متطلبات: REQ-FND-002
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-ORG-TREE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ORG-TREE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ORG-TREE is denied
  Given the policy denies the caller
  When the caller sends QRY-ORG-TREE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-PERSON — الشخص (Person)

`03-domain/contexts/BC01/aggregates/AGG-PERSON.md` · SLC-01 · الحالات: ACTIVE, INACTIVE → ERASED

#### US-BC01-PER-DEACTIVATE — إيقاف تفعيل الشخص

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Administrator with org scope ⊇ person's unit | `POST /api/v1/foundation/persons/{id}/actions/deactivate` | POL-PER-DEACTIVATE |

**القصة:** بصفتي **Administrator with org scope ⊇ person's unit**، أريد **إيقاف تفعيل الشخص**، لكي يتحقق غرض الشخص: سجل الشخص في المنصة (ليس كيان معلومات من نوع شخص)

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ لا شروط إضافية
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← INACTIVE؛ الحدث EVT-PER-DEACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ person's unit؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PER-DEACTIVATE` · `AGG-PERSON` · متطلبات: REQ-FND-006, REQ-GOV-008 · حالات استخدام: UC-084, UC-103
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PER-DEACTIVATE succeeds
  Given AGG-PERSON in state ACTIVE and every guard holds
  When Administrator with org scope ⊇ person's unit sends CMD-PER-DEACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes INACTIVE
  And EVT-PER-DEACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PER-DEACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PER-DEACTIVATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PERSON_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ERASED, INACTIVE |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-PER-ERASE — محو الشخص

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Administrator with org scope ⊇ person's unit | `POST /api/v1/foundation/persons/{id}/actions/erase` | POL-PER-ERASE |

**القصة:** بصفتي **Administrator with org scope ⊇ person's unit**، أريد **محو الشخص**، لكي يتحقق غرض الشخص: سجل الشخص في المنصة (ليس كيان معلومات من نوع شخص)

- **الشروط المسبقة:** الحالة الحالية ∈ {INACTIVE}؛ erasure order recorded; no legal hold; destroys subject key (ADR-P08)
- **المدخلات:** `erasure_order_ref`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ERASED؛ الحدث EVT-PER-ERASED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ person's unit؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit; mfa; legal-hold check
- **الربط:** `CMD-PER-ERASE` · `AGG-PERSON` · متطلبات: REQ-FND-006, REQ-GOV-008 · حالات استخدام: UC-084, UC-103
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PER-ERASE succeeds
  Given AGG-PERSON in state INACTIVE and every guard holds
  When Administrator with org scope ⊇ person's unit sends CMD-PER-ERASE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ERASED
  And EVT-PER-ERASED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PER-ERASE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PER-ERASE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LEGAL_HOLD_ACTIVE | 422 | لم يتحقق الشرط: erasure order recorded; no legal hold; destroys subject key (ADR-P08) |
    | PERSON_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, ERASED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: erasure_order_ref |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-PER-REACTIVATE — إعادة تفعيل الشخص

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Administrator with org scope ⊇ person's unit | `POST /api/v1/foundation/persons/{id}/actions/reactivate` | POL-PER-REACTIVATE |

**القصة:** بصفتي **Administrator with org scope ⊇ person's unit**، أريد **إعادة تفعيل الشخص**، لكي يتحقق غرض الشخص: سجل الشخص في المنصة (ليس كيان معلومات من نوع شخص)

- **الشروط المسبقة:** الحالة الحالية ∈ {INACTIVE}؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-PER-REACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ person's unit؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PER-REACTIVATE` · `AGG-PERSON` · متطلبات: REQ-FND-006, REQ-GOV-008 · حالات استخدام: UC-084, UC-103
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PER-REACTIVATE succeeds
  Given AGG-PERSON in state INACTIVE and every guard holds
  When Administrator with org scope ⊇ person's unit sends CMD-PER-REACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-PER-REACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PER-REACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PER-REACTIVATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PERSON_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, ERASED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-PER-REGISTER — تسجيل الشخص

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Administrator with org scope ⊇ person's unit | `POST /api/v1/foundation/persons` | POL-PER-REGISTER |

**القصة:** بصفتي **Administrator with org scope ⊇ person's unit**، أريد **تسجيل الشخص**، لكي يتحقق غرض الشخص: سجل الشخص في المنصة (ليس كيان معلومات من نوع شخص)

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ names per language-model; no duplicate HR id
- **المدخلات:** `names`!: array, `hr_id`: string, `contact`: object — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-PER-REGISTERED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ person's unit؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PER-REGISTER` · `AGG-PERSON` · متطلبات: REQ-FND-006, REQ-GOV-008 · حالات استخدام: UC-084, UC-103
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PER-REGISTER succeeds
  Given AGG-PERSON in state ∅ and every guard holds
  When Administrator with org scope ⊇ person's unit sends CMD-PER-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-PER-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PER-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PER-REGISTER لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PERSON_DUPLICATE | 422 | لم يتحقق الشرط: names per language-model; no duplicate HR id |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: names |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-PER-UPDATE-DETAILS — تحديث بيانات الشخص

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Administrator with org scope ⊇ person's unit | `POST /api/v1/foundation/persons/{id}/actions/update-details` | POL-PER-UPDATE-DETAILS |

**القصة:** بصفتي **Administrator with org scope ⊇ person's unit**، أريد **تحديث بيانات الشخص**، لكي يتحقق غرض الشخص: سجل الشخص في المنصة (ليس كيان معلومات من نوع شخص)

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ لا شروط إضافية
- **المدخلات:** `names`: array, `contact`: object — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-PER-DETAILS-UPDATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with org scope ⊇ person's unit؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-PER-UPDATE-DETAILS` · `AGG-PERSON` · متطلبات: REQ-FND-006, REQ-GOV-008 · حالات استخدام: UC-084, UC-103
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-PER-UPDATE-DETAILS succeeds
  Given AGG-PERSON in state ACTIVE and every guard holds
  When Administrator with org scope ⊇ person's unit sends CMD-PER-UPDATE-DETAILS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-PER-DETAILS-UPDATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-PER-UPDATE-DETAILS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-PER-UPDATE-DETAILS لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PERSON_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ERASED, INACTIVE |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

### AGG-ROLE — الدور (Role)

`03-domain/contexts/BC01/aggregates/AGG-ROLE.md` · SLC-01 · الحالات: DRAFT, ACTIVE → RETIRED

#### US-BC01-ROL-ACTIVATE — تفعيل الدور

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Administrator (tenant-wide) | `POST /api/v1/foundation/roles/{id}/actions/activate` | POL-ROL-ACTIVATE |

**القصة:** بصفتي **Administrator (tenant-wide)**، أريد **تفعيل الدور**، لكي يتحقق غرض الدور: تعريف دور = مجموعة صلاحيات (action × resource type)

- **الشروط المسبقة:** الحالة الحالية ∈ {DRAFT}؛ ≥ 1 permission
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-ROL-ACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator (tenant-wide)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ROL-ACTIVATE` · `AGG-ROLE` · متطلبات: REQ-FND-014 · حالات استخدام: UC-086
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ROL-ACTIVATE succeeds
  Given AGG-ROLE in state DRAFT and every guard holds
  When Administrator sends CMD-ROL-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-ROL-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ROL-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ROL-ACTIVATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ROLE_EMPTY | 422 | لم يتحقق الشرط: ≥ 1 permission |
    | ROLE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-ROL-DEFINE — تعريف الدور

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | Administrator (tenant-wide) | `POST /api/v1/foundation/roles` | POL-ROL-DEFINE |

**القصة:** بصفتي **Administrator (tenant-wide)**، أريد **تعريف الدور**، لكي يتحقق غرض الدور: تعريف دور = مجموعة صلاحيات (action × resource type)

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ code unique in tenant
- **المدخلات:** `code`!: string, `name`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-ROL-DEFINED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator (tenant-wide)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ROL-DEFINE` · `AGG-ROLE` · متطلبات: REQ-FND-014 · حالات استخدام: UC-086
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ROL-DEFINE succeeds
  Given AGG-ROLE in state ∅ and every guard holds
  When Administrator sends CMD-ROL-DEFINE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-ROL-DEFINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ROL-DEFINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ROL-DEFINE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ROLE_CODE_TAKEN | 422 | لم يتحقق الشرط: code unique in tenant |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: code, name |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-ROL-RETIRE — إحالة الدور إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Administrator (tenant-wide) | `POST /api/v1/foundation/roles/{id}/actions/retire` | POL-ROL-RETIRE |

**القصة:** بصفتي **Administrator (tenant-wide)**، أريد **إحالة الدور إلى التقاعد**، لكي يتحقق غرض الدور: تعريف دور = مجموعة صلاحيات (action × resource type)

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ not a system role; no active assignments
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-ROL-RETIRED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator (tenant-wide)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ROL-RETIRE` · `AGG-ROLE` · متطلبات: REQ-FND-014 · حالات استخدام: UC-086
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ROL-RETIRE succeeds
  Given AGG-ROLE in state ACTIVE and every guard holds
  When Administrator sends CMD-ROL-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-ROL-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ROL-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ROL-RETIRE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ROLE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DRAFT, RETIRED |
    | ROLE_IN_USE | 422 | لم يتحقق الشرط: not a system role; no active assignments |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-ROL-SET-PERMISSIONS — تحديد صلاحيات الدور

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | حوكمة وأمن | Administrator (tenant-wide) | `POST /api/v1/foundation/roles/{id}/actions/set-permissions` | POL-ROL-SET-PERMISSIONS |

**القصة:** بصفتي **Administrator (tenant-wide)**، أريد **تحديد صلاحيات الدور**، لكي يتحقق غرض الدور: تعريف دور = مجموعة صلاحيات (action × resource type)

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, DRAFT}؛ permissions exist in catalog; system roles are locked; ACTIVE → new version
- **المدخلات:** `permissions`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ROL-PERMISSIONS-CHANGED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator (tenant-wide)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ROL-SET-PERMISSIONS` · `AGG-ROLE` · متطلبات: REQ-FND-014 · حالات استخدام: UC-086
- **ضوابط النوع والفئة:** C-UPD، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ROL-SET-PERMISSIONS succeeds
  Given AGG-ROLE in state ACTIVE or DRAFT and every guard holds
  When Administrator sends CMD-ROL-SET-PERMISSIONS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-ROL-PERMISSIONS-CHANGED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ROL-SET-PERMISSIONS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ROL-SET-PERMISSIONS لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ROLE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | SYSTEM_ROLE_LOCKED | 422 | لم يتحقق الشرط: permissions exist in catalog; system roles are locked; ACTIVE → new version |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: permissions |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

### AGG-ROLE-ASSIGNMENT — إسناد الدور (Role Assignment)

`03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md` · SLC-01 · الحالات: ACTIVE → EXPIRED, REVOKED

#### US-BC01-RAS-ASSIGN — إسناد إسناد الدور

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | Administrator with scope ⊇ assignment scope | `POST /api/v1/foundation/role-assignments` | POL-RAS-ASSIGN |

**القصة:** بصفتي **Administrator with scope ⊇ assignment scope**، أريد **إسناد إسناد الدور**، لكي يتحقق غرض إسناد الدور: إسناد دور لمستخدم ضمن نطاق وحدة تنظيمية لفترة

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ role ACTIVE; user not CLOSED; scope unit ACTIVE; assigner administers the scope; no SoD-incompatible active role
- **المدخلات:** `user`!: urn, `role`!: urn, `org_scope`!: urn, `include_descendants`!: boolean, `valid_from`!: date-time, `valid_to`: date-time — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-RAS-ASSIGNED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ assignment scope؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: assigner ≠ user; SoD role pairs؛ الالتزامات: audit
- **الربط:** `CMD-RAS-ASSIGN` · `AGG-ROLE-ASSIGNMENT` · متطلبات: REQ-FND-011, REQ-OPS-005, REQ-OPS-009 · حالات استخدام: UC-035, UC-044, UC-086
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RAS-ASSIGN succeeds
  Given AGG-ROLE-ASSIGNMENT in state ∅ and every guard holds
  When Administrator with scope ⊇ assignment scope sends CMD-RAS-ASSIGN with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-RAS-ASSIGNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RAS-ASSIGN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RAS-ASSIGN لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SOD_ROLE_CONFLICT | 422 | لم يتحقق الشرط: role ACTIVE; user not CLOSED; scope unit ACTIVE; assigner administers the scope; no SoD-incompatible active role |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: user, role, org_scope, include_descendants, valid_from |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-RAS-REVOKE — سحب إسناد الدور

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Administrator with scope ⊇ assignment scope | `POST /api/v1/foundation/role-assignments/{id}/actions/revoke` | POL-RAS-REVOKE |

**القصة:** بصفتي **Administrator with scope ⊇ assignment scope**، أريد **سحب إسناد الدور**، لكي يتحقق غرض إسناد الدور: إسناد دور لمستخدم ضمن نطاق وحدة تنظيمية لفترة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ assigner administers the scope; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← REVOKED؛ الحدث EVT-RAS-REVOKED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ assignment scope؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RAS-REVOKE` · `AGG-ROLE-ASSIGNMENT` · متطلبات: REQ-FND-011, REQ-OPS-005, REQ-OPS-009 · حالات استخدام: UC-035, UC-044, UC-086
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RAS-REVOKE succeeds
  Given AGG-ROLE-ASSIGNMENT in state ACTIVE and every guard holds
  When Administrator with scope ⊇ assignment scope sends CMD-RAS-REVOKE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REVOKED
  And EVT-RAS-REVOKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RAS-REVOKE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RAS-REVOKE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, REVOKED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-S-ROLE-ASSIGNMENT-01 — تلقائي: valid_to reached (إسناد الدور)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | ACTIVE | EXPIRED |

**القصة:** بصفتي **النظام**، عند «valid_to reached»، أريد نقل **إسناد الدور** إلى EXPIRED، لكي يتحقق غرض إسناد الدور: إسناد دور لمستخدم ضمن نطاق وحدة تنظيمية لفترة

- **الشرط:** system scheduler
- **المخرجات:** الحدث EVT-RAS-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ROLE-ASSIGNMENT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

### AGG-SERVICE-ACCOUNT — حساب الخدمة (Service Account)

`03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md` · SLC-01 · الحالات: ACTIVE, DISABLED → CLOSED

#### US-BC01-SVC-CLOSE — إغلاق حساب الخدمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | حوكمة وأمن | Administrator | `POST /api/v1/foundation/service-accounts/{id}/actions/close` | POL-SVC-CLOSE |

**القصة:** بصفتي **Administrator**، أريد **إغلاق حساب الخدمة**، لكي يتحقق غرض حساب الخدمة: هوية لنظام أو محول، ليست لشخص

- **الشروط المسبقة:** الحالة الحالية ∈ {DISABLED}؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-SVC-CLOSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SVC-CLOSE` · `AGG-SERVICE-ACCOUNT` · متطلبات: REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-DEL، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SVC-CLOSE succeeds
  Given AGG-SERVICE-ACCOUNT in state DISABLED and every guard holds
  When Administrator sends CMD-SVC-CLOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-SVC-CLOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SVC-CLOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SVC-CLOSE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-SVC-CREATE — إنشاء حساب الخدمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | حوكمة وأمن | Administrator | `POST /api/v1/foundation/service-accounts` | POL-SVC-CREATE |

**القصة:** بصفتي **Administrator**، أريد **إنشاء حساب الخدمة**، لكي يتحقق غرض حساب الخدمة: هوية لنظام أو محول، ليست لشخص

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ owner user ACTIVE; purpose stated
- **المدخلات:** `name`!: string, `owner`!: urn, `purpose`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-SVC-CREATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SVC-CREATE` · `AGG-SERVICE-ACCOUNT` · متطلبات: REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-CRE، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SVC-CREATE succeeds
  Given AGG-SERVICE-ACCOUNT in state ∅ and every guard holds
  When Administrator sends CMD-SVC-CREATE with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-SVC-CREATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SVC-CREATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SVC-CREATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OWNER_REQUIRED | 422 | لم يتحقق الشرط: owner user ACTIVE; purpose stated |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: name, owner, purpose |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-SVC-DISABLE — تعطيل حساب الخدمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Administrator | `POST /api/v1/foundation/service-accounts/{id}/actions/disable` | POL-SVC-DISABLE |

**القصة:** بصفتي **Administrator**، أريد **تعطيل حساب الخدمة**، لكي يتحقق غرض حساب الخدمة: هوية لنظام أو محول، ليست لشخص

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ لا شروط إضافية
- **المدخلات:** `reason`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DISABLED؛ الحدث EVT-SVC-DISABLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SVC-DISABLE` · `AGG-SERVICE-ACCOUNT` · متطلبات: REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SVC-DISABLE succeeds
  Given AGG-SERVICE-ACCOUNT in state ACTIVE and every guard holds
  When Administrator sends CMD-SVC-DISABLE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISABLED
  And EVT-SVC-DISABLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SVC-DISABLE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SVC-DISABLE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED, DISABLED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-SVC-ENABLE — تمكين حساب الخدمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | حوكمة وأمن | Administrator | `POST /api/v1/foundation/service-accounts/{id}/actions/enable` | POL-SVC-ENABLE |

**القصة:** بصفتي **Administrator**، أريد **تمكين حساب الخدمة**، لكي يتحقق غرض حساب الخدمة: هوية لنظام أو محول، ليست لشخص

- **الشروط المسبقة:** الحالة الحالية ∈ {DISABLED}؛ owner still ACTIVE
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-SVC-ENABLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SVC-ENABLE` · `AGG-SERVICE-ACCOUNT` · متطلبات: REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-WF، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SVC-ENABLE succeeds
  Given AGG-SERVICE-ACCOUNT in state DISABLED and every guard holds
  When Administrator sends CMD-SVC-ENABLE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-SVC-ENABLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SVC-ENABLE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SVC-ENABLE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | OWNER_REQUIRED | 422 | لم يتحقق الشرط: owner still ACTIVE |
    | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-SVC-ROTATE-CREDENTIAL — تدوير بيانات اعتماد حساب الخدمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | حوكمة وأمن | Administrator | `POST /api/v1/foundation/service-accounts/{id}/actions/rotate-credential` | POL-SVC-ROTATE-CREDENTIAL |

**القصة:** بصفتي **Administrator**، أريد **تدوير بيانات اعتماد حساب الخدمة**، لكي يتحقق غرض حساب الخدمة: هوية لنظام أو محول، ليست لشخص

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ new credential expiry ≤ 90 days
- **المدخلات:** `public_key`!: string, `expires_at`!: date-time — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SVC-CREDENTIAL-ROTATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SVC-ROTATE-CREDENTIAL` · `AGG-SERVICE-ACCOUNT` · متطلبات: REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-UPD، K-GOV (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SVC-ROTATE-CREDENTIAL succeeds
  Given AGG-SERVICE-ACCOUNT in state ACTIVE and every guard holds
  When Administrator sends CMD-SVC-ROTATE-CREDENTIAL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-SVC-CREDENTIAL-ROTATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SVC-ROTATE-CREDENTIAL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SVC-ROTATE-CREDENTIAL لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CREDENTIAL_LIFETIME_EXCEEDED | 422 | لم يتحقق الشرط: new credential expiry ≤ 90 days |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED, DISABLED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: public_key, expires_at |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

### AGG-TENANT — المستأجر (Tenant)

`03-domain/contexts/BC01/aggregates/AGG-TENANT.md` · SLC-01 · الحالات: PROVISIONING, PROVISIONING_FAILED, ACTIVE, SUSPENDED, MIGRATING, DECOMMISSIONING → DECOMMISSIONED

#### US-BC01-TEN-COMPLETE-CELL-MIGRATION — إكمال ترحيل المستأجر إلى خلية أخرى

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| نظام | أساسية | workload identity: scheduler / provisioning saga | `POST /api/v1/foundation/tenants/{id}/actions/complete-cell-migration` | POL-TEN-COMPLETE-CELL-MIGRATION |

**القصة:** بصفتي **workload identity: scheduler / provisioning saga**، أريد **إكمال ترحيل المستأجر إلى خلية أخرى**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {MIGRATING}؛ system; export/import reconciled
- **المدخلات:** `reconciliation_report`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-TEN-MIGRATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** workload identity: scheduler / provisioning saga؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TEN-COMPLETE-CELL-MIGRATION` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-SYS، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-COMPLETE-CELL-MIGRATION succeeds
  Given AGG-TENANT in state MIGRATING and every guard holds
  When workload identity: scheduler / provisioning saga sends CMD-TEN-COMPLETE-CELL-MIGRATION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-TEN-MIGRATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-COMPLETE-CELL-MIGRATION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-COMPLETE-CELL-MIGRATION لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MIGRATION_NOT_RECONCILED | 422 | لم يتحقق الشرط: system; export/import reconciled |
    | TENANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DECOMMISSIONED, DECOMMISSIONING, PROVISIONING, PROVISIONING_FAILED, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reconciliation_report |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-TEN-COMPLETE-DECOMMISSION — إكمال إخراج المستأجر من الخدمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| نظام | أساسية | workload identity: scheduler / provisioning saga | `POST /api/v1/foundation/tenants/{id}/actions/complete-decommission` | POL-TEN-COMPLETE-DECOMMISSION |

**القصة:** بصفتي **workload identity: scheduler / provisioning saga**، أريد **إكمال إخراج المستأجر من الخدمة**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {DECOMMISSIONING}؛ system; keys destroyed, stores removed
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DECOMMISSIONED؛ الحدث EVT-TEN-DECOMMISSIONED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** workload identity: scheduler / provisioning saga؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TEN-COMPLETE-DECOMMISSION` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-SYS، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-COMPLETE-DECOMMISSION succeeds
  Given AGG-TENANT in state DECOMMISSIONING and every guard holds
  When workload identity: scheduler / provisioning saga sends CMD-TEN-COMPLETE-DECOMMISSION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DECOMMISSIONED
  And EVT-TEN-DECOMMISSIONED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-COMPLETE-DECOMMISSION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-COMPLETE-DECOMMISSION لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TENANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DECOMMISSIONED, MIGRATING, PROVISIONING, PROVISIONING_FAILED, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-TEN-COMPLETE-PROVISIONING — إكمال تهيئة المستأجر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| نظام | أساسية | workload identity: scheduler / provisioning saga | `POST /api/v1/foundation/tenants/{id}/actions/complete-provisioning` | POL-TEN-COMPLETE-PROVISIONING |

**القصة:** بصفتي **workload identity: scheduler / provisioning saga**، أريد **إكمال تهيئة المستأجر**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {PROVISIONING}؛ system; all provisioning steps confirmed (isolation, keys, scheme, roles, quotas, audit stream)
- **المدخلات:** `steps`!: array — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-TEN-ACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** workload identity: scheduler / provisioning saga؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TEN-COMPLETE-PROVISIONING` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-SYS، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-COMPLETE-PROVISIONING succeeds
  Given AGG-TENANT in state PROVISIONING and every guard holds
  When workload identity: scheduler / provisioning saga sends CMD-TEN-COMPLETE-PROVISIONING with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-TEN-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-COMPLETE-PROVISIONING is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-COMPLETE-PROVISIONING لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TENANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DECOMMISSIONED, DECOMMISSIONING, MIGRATING, PROVISIONING_FAILED, SUSPENDED |
    | TENANT_PROVISIONING_INCOMPLETE | 422 | لم يتحقق الشرط: system; all provisioning steps confirmed (isolation, keys, scheme, roles, quotas, audit stream) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: steps |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-TEN-FAIL-PROVISIONING — تسجيل فشل تهيئة المستأجر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| نظام | أساسية | workload identity: scheduler / provisioning saga | `POST /api/v1/foundation/tenants/{id}/actions/fail-provisioning` | POL-TEN-FAIL-PROVISIONING |

**القصة:** بصفتي **workload identity: scheduler / provisioning saga**، أريد **تسجيل فشل تهيئة المستأجر**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {PROVISIONING}؛ system; compensation completed
- **المدخلات:** `failed_step`!: string, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← PROVISIONING_FAILED؛ الحدث EVT-TEN-PROVISIONING-FAILED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** workload identity: scheduler / provisioning saga؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TEN-FAIL-PROVISIONING` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-SYS، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-FAIL-PROVISIONING succeeds
  Given AGG-TENANT in state PROVISIONING and every guard holds
  When workload identity: scheduler / provisioning saga sends CMD-TEN-FAIL-PROVISIONING with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PROVISIONING_FAILED
  And EVT-TEN-PROVISIONING-FAILED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-FAIL-PROVISIONING is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-FAIL-PROVISIONING لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TENANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DECOMMISSIONED, DECOMMISSIONING, MIGRATING, PROVISIONING_FAILED, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: failed_step, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-TEN-PROVISION — تهيئة المستأجر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only | `POST /api/v1/foundation/tenants` | POL-TEN-PROVISION |

**القصة:** بصفتي **Platform Operator (platform tenant) ; Tenant Administrator for quotas view only**، أريد **تهيئة المستأجر**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ namespace unique; cell_mode valid for tenant profile (INV-TEN-03)
- **المدخلات:** `namespace`!: string, `display_name`!: string, `cell_mode`!: enum(shared, `sovereign`!: boolean, `top_level_enabled`!: boolean, `jurisdiction`!: string, `quotas`!: TenantQuotas — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← PROVISIONING؛ الحدث EVT-TEN-PROVISIONING-STARTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TEN-PROVISION` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-PROVISION succeeds
  Given AGG-TENANT in state ∅ and every guard holds
  When Platform Operator sends CMD-TEN-PROVISION with a valid payload, a new Idempotency-Key
  Then the state becomes PROVISIONING
  And EVT-TEN-PROVISIONING-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-PROVISION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-PROVISION لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TENANT_NAMESPACE_TAKEN | 422 | لم يتحقق الشرط: namespace unique; cell_mode valid for tenant profile (INV-TEN-03) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: namespace, display_name, cell_mode, sovereign, top_level_enabled, jurisdiction, quotas |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-TEN-REACTIVATE — إعادة تفعيل المستأجر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only | `POST /api/v1/foundation/tenants/{id}/actions/reactivate` | POL-TEN-REACTIVATE |

**القصة:** بصفتي **Platform Operator (platform tenant) ; Tenant Administrator for quotas view only**، أريد **إعادة تفعيل المستأجر**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {SUSPENDED}؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-TEN-REACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TEN-REACTIVATE` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-REACTIVATE succeeds
  Given AGG-TENANT in state SUSPENDED and every guard holds
  When Platform Operator sends CMD-TEN-REACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-TEN-REACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-REACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-REACTIVATE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TENANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DECOMMISSIONED, DECOMMISSIONING, MIGRATING, PROVISIONING, PROVISIONING_FAILED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-TEN-RETRY-PROVISIONING — إعادة محاولة تهيئة المستأجر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only | `POST /api/v1/foundation/tenants/{id}/actions/retry-provisioning` | POL-TEN-RETRY-PROVISIONING |

**القصة:** بصفتي **Platform Operator (platform tenant) ; Tenant Administrator for quotas view only**، أريد **إعادة محاولة تهيئة المستأجر**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {PROVISIONING_FAILED}؛ actor = platform operator
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← PROVISIONING؛ الحدث EVT-TEN-PROVISIONING-STARTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TEN-RETRY-PROVISIONING` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-RETRY-PROVISIONING succeeds
  Given AGG-TENANT in state PROVISIONING_FAILED and every guard holds
  When Platform Operator sends CMD-TEN-RETRY-PROVISIONING with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PROVISIONING
  And EVT-TEN-PROVISIONING-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-RETRY-PROVISIONING is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-RETRY-PROVISIONING لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TENANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, DECOMMISSIONED, DECOMMISSIONING, MIGRATING, PROVISIONING, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-TEN-START-CELL-MIGRATION — بدء ترحيل المستأجر إلى خلية أخرى

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only | `POST /api/v1/foundation/tenants/{id}/actions/start-cell-migration` | POL-TEN-START-CELL-MIGRATION |

**القصة:** بصفتي **Platform Operator (platform tenant) ; Tenant Administrator for quotas view only**، أريد **بدء ترحيل المستأجر إلى خلية أخرى**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ target cell exists and has capacity
- **المدخلات:** `target_cell`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← MIGRATING؛ الحدث EVT-TEN-MIGRATION-STARTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TEN-START-CELL-MIGRATION` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-START-CELL-MIGRATION succeeds
  Given AGG-TENANT in state ACTIVE and every guard holds
  When Platform Operator sends CMD-TEN-START-CELL-MIGRATION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes MIGRATING
  And EVT-TEN-MIGRATION-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-START-CELL-MIGRATION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-START-CELL-MIGRATION لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | CELL_UNAVAILABLE | 422 | لم يتحقق الشرط: target cell exists and has capacity |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TENANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DECOMMISSIONED, DECOMMISSIONING, MIGRATING, PROVISIONING, PROVISIONING_FAILED, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: target_cell |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-TEN-START-DECOMMISSION — بدء إخراج المستأجر من الخدمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only | `POST /api/v1/foundation/tenants/{id}/actions/start-decommission` | POL-TEN-START-DECOMMISSION |

**القصة:** بصفتي **Platform Operator (platform tenant) ; Tenant Administrator for quotas view only**، أريد **بدء إخراج المستأجر من الخدمة**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, SUSPENDED}؛ no active legal hold (BC08 query); two-person approval
- **المدخلات:** `reason`!: string, `second_approver`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DECOMMISSIONING؛ الحدث EVT-TEN-DECOMMISSION-STARTED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: two distinct platform operators؛ الالتزامات: audit; mfa
- **الربط:** `CMD-TEN-START-DECOMMISSION` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-START-DECOMMISSION succeeds
  Given AGG-TENANT in state ACTIVE or SUSPENDED and every guard holds
  When Platform Operator sends CMD-TEN-START-DECOMMISSION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DECOMMISSIONING
  And EVT-TEN-DECOMMISSION-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-START-DECOMMISSION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-START-DECOMMISSION لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LEGAL_HOLD_ACTIVE | 422 | لم يتحقق الشرط: no active legal hold (BC08 query); two-person approval |
    | TENANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DECOMMISSIONED, DECOMMISSIONING, MIGRATING, PROVISIONING, PROVISIONING_FAILED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason, second_approver |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-TEN-SUSPEND — تعليق المستأجر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only | `POST /api/v1/foundation/tenants/{id}/actions/suspend` | POL-TEN-SUSPEND |

**القصة:** بصفتي **Platform Operator (platform tenant) ; Tenant Administrator for quotas view only**، أريد **تعليق المستأجر**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ reason provided
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← SUSPENDED؛ الحدث EVT-TEN-SUSPENDED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TEN-SUSPEND` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-SUSPEND succeeds
  Given AGG-TENANT in state ACTIVE and every guard holds
  When Platform Operator sends CMD-TEN-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUSPENDED
  And EVT-TEN-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-SUSPEND لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | TENANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DECOMMISSIONED, DECOMMISSIONING, MIGRATING, PROVISIONING, PROVISIONING_FAILED, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-TEN-UPDATE-QUOTAS — تحديث حصص المستأجر

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Platform Operator (platform tenant) ; Tenant Administrator for quotas view only | `POST /api/v1/foundation/tenants/{id}/actions/update-quotas` | POL-TEN-UPDATE-QUOTAS |

**القصة:** بصفتي **Platform Operator (platform tenant) ; Tenant Administrator for quotas view only**، أريد **تحديث حصص المستأجر**، لكي يتحقق غرض المستأجر: وحدة العزل العليا؛ تُربط بخلية واحدة

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, SUSPENDED}؛ quotas ≤ cell capacity
- **المدخلات:** `quotas`!: TenantQuotas — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-TEN-QUOTAS-UPDATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-TEN-UPDATE-QUOTAS` · `AGG-TENANT` · متطلبات: REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 · حالات استخدام: UC-080, UC-105
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-TEN-UPDATE-QUOTAS succeeds
  Given AGG-TENANT in state ACTIVE or SUSPENDED and every guard holds
  When Platform Operator sends CMD-TEN-UPDATE-QUOTAS with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-TEN-QUOTAS-UPDATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-TEN-UPDATE-QUOTAS is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-TEN-UPDATE-QUOTAS لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | QUOTA_EXCEEDS_CAPACITY | 422 | لم يتحقق الشرط: quotas ≤ cell capacity |
    | TENANT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DECOMMISSIONED, DECOMMISSIONING, MIGRATING, PROVISIONING, PROVISIONING_FAILED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: quotas |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-Q-TEN-GET — جلب: Tenant state, cell, quotas

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | platform operator or tenant Administrator of that tenant | `GET /api/v1/foundation/tenants/{tenant_id}` | POL-TEN-GET |

**القصة:** بصفتي **platform operator or tenant Administrator of that tenant**، أريد **جلب Tenant state, cell, quotas**، لكي يتحقق المتطلب: The system shall isolate each tenant's data, policies, configuration, projections, files, events and audit records from every other tenant

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Tenant state, cell, quotas
- **الصلاحية:** platform operator or tenant Administrator of that tenant؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-TEN-GET` · `AGG-TENANT` · متطلبات: REQ-FND-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-TEN-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-TEN-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-TEN-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-TEN-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-USER — حساب المستخدم (User Account)

`03-domain/contexts/BC01/aggregates/AGG-USER.md` · SLC-01 · الحالات: PENDING, ACTIVE, LOCKED, DISABLED → CLOSED

#### US-BC01-USR-CLOSE — إغلاق حساب المستخدم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock) | `POST /api/v1/foundation/users/{id}/actions/close` | POL-USR-CLOSE |

**القصة:** بصفتي **Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)**، أريد **إغلاق حساب المستخدم**، لكي يتحقق غرض حساب المستخدم: حساب دخول مرتبط بهويات خارجية

- **الشروط المسبقة:** الحالة الحالية ∈ {DISABLED}؛ administrator; audit history retained
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-USR-CLOSED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-USR-CLOSE` · `AGG-USER` · متطلبات: REQ-FND-005, REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-USR-CLOSE succeeds
  Given AGG-USER in state DISABLED and every guard holds
  When Administrator with scope ⊇ user's units | SCIM service account sends CMD-USR-CLOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-USR-CLOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-USR-CLOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-USR-CLOSE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | USER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CLOSED, LOCKED, PENDING |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-USR-DISABLE — تعطيل حساب المستخدم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Administrator with scope ⊇ user's units \| SCIM service account \| Security Officer | `POST /api/v1/foundation/users/{id}/actions/disable` | POL-USR-DISABLE |

**القصة:** بصفتي **Administrator with scope ⊇ user's units \| SCIM service account \| Security Officer**، أريد **تعطيل حساب المستخدم**، لكي يتحقق غرض حساب المستخدم: حساب دخول مرتبط بهويات خارجية

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, LOCKED, PENDING}؛ SCIM deactivate or administrator
- **المدخلات:** `reason`: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← DISABLED؛ الحدث EVT-USR-DISABLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-USR-DISABLE` · `AGG-USER` · متطلبات: REQ-FND-005, REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-USR-DISABLE succeeds
  Given AGG-USER in state ACTIVE or LOCKED or PENDING and every guard holds
  When Administrator with scope ⊇ user's units | SCIM service account | Security Officer sends CMD-USR-DISABLE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISABLED
  And EVT-USR-DISABLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-USR-DISABLE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-USR-DISABLE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | USER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED, DISABLED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-USR-ENABLE — تمكين حساب المستخدم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Administrator with scope ⊇ user's units \| SCIM service account \| Security Officer | `POST /api/v1/foundation/users/{id}/actions/enable` | POL-USR-ENABLE |

**القصة:** بصفتي **Administrator with scope ⊇ user's units \| SCIM service account \| Security Officer**، أريد **تمكين حساب المستخدم**، لكي يتحقق غرض حساب المستخدم: حساب دخول مرتبط بهويات خارجية

- **الشروط المسبقة:** الحالة الحالية ∈ {DISABLED}؛ ≥ 1 identity; tenant ACTIVE
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-USR-ENABLED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-USR-ENABLE` · `AGG-USER` · متطلبات: REQ-FND-005, REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-USR-ENABLE succeeds
  Given AGG-USER in state DISABLED and every guard holds
  When Administrator with scope ⊇ user's units | SCIM service account | Security Officer sends CMD-USR-ENABLE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-USR-ENABLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-USR-ENABLE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-USR-ENABLE لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LAST_IDENTITY | 422 | لم يتحقق الشرط: ≥ 1 identity; tenant ACTIVE |
    | USER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CLOSED, LOCKED, PENDING |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-USR-LINK-IDENTITY — ربط هوية خارجية بـحساب المستخدم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock) | `POST /api/v1/foundation/users/{id}/actions/link-identity` | POL-USR-LINK-IDENTITY |

**القصة:** بصفتي **Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)**، أريد **ربط هوية خارجية بـحساب المستخدم**، لكي يتحقق غرض حساب المستخدم: حساب دخول مرتبط بهويات خارجية

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, DISABLED, LOCKED, PENDING}؛ (issuer, subject) unique in tenant; issuer is a configured IdP
- **المدخلات:** `issuer`!: string, `subject`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-USR-IDENTITY-LINKED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-USR-LINK-IDENTITY` · `AGG-USER` · متطلبات: REQ-FND-005, REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-USR-LINK-IDENTITY succeeds
  Given AGG-USER in state ACTIVE or DISABLED or LOCKED or PENDING and every guard holds
  When Administrator with scope ⊇ user's units | SCIM service account sends CMD-USR-LINK-IDENTITY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-USR-IDENTITY-LINKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-USR-LINK-IDENTITY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-USR-LINK-IDENTITY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | IDENTITY_ALREADY_LINKED | 422 | لم يتحقق الشرط: (issuer, subject) unique in tenant; issuer is a configured IdP |
    | USER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: issuer, subject |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-USR-LINK-PERSON — ربط شخص بـحساب المستخدم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock) | `POST /api/v1/foundation/users/{id}/actions/link-person` | POL-USR-LINK-PERSON |

**القصة:** بصفتي **Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)**، أريد **ربط شخص بـحساب المستخدم**، لكي يتحقق غرض حساب المستخدم: حساب دخول مرتبط بهويات خارجية

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, DISABLED, LOCKED, PENDING}؛ person ACTIVE, not linked to another user
- **المدخلات:** `person`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-USR-PERSON-LINKED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-USR-LINK-PERSON` · `AGG-USER` · متطلبات: REQ-FND-005, REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-USR-LINK-PERSON succeeds
  Given AGG-USER in state ACTIVE or DISABLED or LOCKED or PENDING and every guard holds
  When Administrator with scope ⊇ user's units | SCIM service account sends CMD-USR-LINK-PERSON with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-USR-PERSON-LINKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-USR-LINK-PERSON is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-USR-LINK-PERSON لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | PERSON_ALREADY_LINKED | 422 | لم يتحقق الشرط: person ACTIVE, not linked to another user |
    | USER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: person |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-USR-LOCK — قفل حساب المستخدم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock) | `POST /api/v1/foundation/users/{id}/actions/lock` | POL-USR-LOCK |

**القصة:** بصفتي **Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)**، أريد **قفل حساب المستخدم**، لكي يتحقق غرض حساب المستخدم: حساب دخول مرتبط بهويات خارجية

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE}؛ security officer or system anomaly rule; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← LOCKED؛ الحدث EVT-USR-LOCKED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-USR-LOCK` · `AGG-USER` · متطلبات: REQ-FND-005, REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-USR-LOCK succeeds
  Given AGG-USER in state ACTIVE and every guard holds
  When Administrator with scope ⊇ user's units | SCIM service account sends CMD-USR-LOCK with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes LOCKED
  And EVT-USR-LOCKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-USR-LOCK is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-USR-LOCK لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | USER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED, DISABLED, LOCKED, PENDING |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-USR-PROVISION — تهيئة حساب المستخدم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Administrator with scope ⊇ user's units \| SCIM service account \| Security Officer | `POST /api/v1/foundation/users` | POL-USR-PROVISION |

**القصة:** بصفتي **Administrator with scope ⊇ user's units \| SCIM service account \| Security Officer**، أريد **تهيئة حساب المستخدم**، لكي يتحقق غرض حساب المستخدم: حساب دخول مرتبط بهويات خارجية

- **الشروط المسبقة:** الحالة الحالية ∈ {∅}؛ tenant ACTIVE; via SCIM or admin
- **المدخلات:** `username`!: string, `person`: urn, `source`!: enum(scim — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← PENDING؛ الحدث EVT-USR-PROVISIONED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-USR-PROVISION` · `AGG-USER` · متطلبات: REQ-FND-005, REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-USR-PROVISION succeeds
  Given AGG-USER in state ∅ and every guard holds
  When Administrator with scope ⊇ user's units | SCIM service account | Security Officer sends CMD-USR-PROVISION with a valid payload, a new Idempotency-Key
  Then the state becomes PENDING
  And EVT-USR-PROVISIONED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-USR-PROVISION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-USR-PROVISION لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | TENANT_NOT_ACTIVE | 422 | لم يتحقق الشرط: tenant ACTIVE; via SCIM or admin |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: username, source |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-USR-RECORD-FIRST-SIGN-IN — تسجيل أول دخول لـحساب المستخدم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| نظام | أساسية | workload identity: scheduler / provisioning saga | `POST /api/v1/foundation/users/{id}/actions/record-first-sign-in` | POL-USR-RECORD-FIRST-SIGN-IN |

**القصة:** بصفتي **workload identity: scheduler / provisioning saga**، أريد **تسجيل أول دخول لـحساب المستخدم**، لكي يتحقق غرض حساب المستخدم: حساب دخول مرتبط بهويات خارجية

- **الشروط المسبقة:** الحالة الحالية ∈ {PENDING}؛ system; ≥ 1 identity; tenant ACTIVE
- **المدخلات:** `issuer`!: string, `subject`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-USR-ACTIVATED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** workload identity: scheduler / provisioning saga؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-USR-RECORD-FIRST-SIGN-IN` · `AGG-USER` · متطلبات: REQ-FND-005, REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-SYS، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-USR-RECORD-FIRST-SIGN-IN succeeds
  Given AGG-USER in state PENDING and every guard holds
  When workload identity: scheduler / provisioning saga sends CMD-USR-RECORD-FIRST-SIGN-IN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-USR-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-USR-RECORD-FIRST-SIGN-IN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-USR-RECORD-FIRST-SIGN-IN لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | USER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CLOSED, DISABLED, LOCKED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: issuer, subject |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-USR-UNLINK-IDENTITY — فك ربط هوية خارجية عن حساب المستخدم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock) | `POST /api/v1/foundation/users/{id}/actions/unlink-identity` | POL-USR-UNLINK-IDENTITY |

**القصة:** بصفتي **Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)**، أريد **فك ربط هوية خارجية عن حساب المستخدم**، لكي يتحقق غرض حساب المستخدم: حساب دخول مرتبط بهويات خارجية

- **الشروط المسبقة:** الحالة الحالية ∈ {ACTIVE, DISABLED, LOCKED, PENDING}؛ if ACTIVE, at least one identity remains
- **المدخلات:** `issuer`!: string, `subject`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-USR-IDENTITY-UNLINKED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-USR-UNLINK-IDENTITY` · `AGG-USER` · متطلبات: REQ-FND-005, REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-USR-UNLINK-IDENTITY succeeds
  Given AGG-USER in state ACTIVE or DISABLED or LOCKED or PENDING and every guard holds
  When Administrator with scope ⊇ user's units | SCIM service account sends CMD-USR-UNLINK-IDENTITY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes unchanged
  And EVT-USR-IDENTITY-UNLINKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-USR-UNLINK-IDENTITY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-USR-UNLINK-IDENTITY لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LAST_IDENTITY | 422 | لم يتحقق الشرط: if ACTIVE, at least one identity remains |
    | USER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: issuer, subject |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-USR-UNLOCK — فتح قفل حساب المستخدم

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock) | `POST /api/v1/foundation/users/{id}/actions/unlock` | POL-USR-UNLOCK |

**القصة:** بصفتي **Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)**، أريد **فتح قفل حساب المستخدم**، لكي يتحقق غرض حساب المستخدم: حساب دخول مرتبط بهويات خارجية

- **الشروط المسبقة:** الحالة الحالية ∈ {LOCKED}؛ security officer
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` دائمًا و`If-Match` لغير الإنشاء
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-USR-UNLOCKED؛ الاستجابة `ResourceRef` (id، version)
- **الصلاحية:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)؛ الشروط: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-USR-UNLOCK` · `AGG-USER` · متطلبات: REQ-FND-005, REQ-FND-006 · حالات استخدام: UC-084
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-USR-UNLOCK succeeds
  Given AGG-USER in state LOCKED and every guard holds
  When Administrator with scope ⊇ user's units | SCIM service account sends CMD-USR-UNLOCK with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-USR-UNLOCKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-USR-UNLOCK is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-USR-UNLOCK لا تمنح المستدعي الإذن؛ يُعاد شكل not-found إن كان المورد غير مرئي له |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | USER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CLOSED, DISABLED, PENDING |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل) |
```

#### US-BC01-Q-USR-GET — جلب: User with identities (no secrets)

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | Administrator in scope or self | `GET /api/v1/foundation/users/{user_id}` | POL-USR-GET |

**القصة:** بصفتي **Administrator in scope or self**، أريد **جلب User with identities (no secrets)**، لكي يتحقق المتطلب: The system shall maintain Person, Identity, User and Service Account as separate records with explicit links

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** User with identities (no secrets)
- **الصلاحية:** Administrator in scope or self؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-USR-GET` · `AGG-USER` · متطلبات: REQ-FND-006
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-USR-GET returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-USR-GET
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-USR-GET is denied
  Given the policy denies the caller
  When the caller sends QRY-USR-GET
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC01-Q-USR-LIST — جلب: Users filtered by state, unit, role

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | Administrator in scope | `GET /api/v1/foundation/users` | POL-USR-LIST |

**القصة:** بصفتي **Administrator in scope**، أريد **جلب Users filtered by state, unit, role**، لكي يتحقق المتطلب: The system shall maintain Person, Identity, User and Service Account as separate records with explicit links

- **المدخلات:** `cursor`, `limit`
- **المخرجات:** Users filtered by state, unit, role؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Administrator in scope؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-USR-LIST` · `AGG-USER` · متطلبات: REQ-FND-006
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-USR-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-USR-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-USR-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-USR-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### استعلامات عابرة للـAggregates

#### US-BC01-Q-SEC-CONTEXT — جلب: Caller's resolved SecurityContext

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | self | `GET /api/v1/foundation/me/security-context` | POL-SEC-CONTEXT |

**القصة:** بصفتي **self**، أريد **جلب Caller's resolved SecurityContext**، لكي يتحقق المتطلب: The system shall evaluate authorization before retrieving data for every command, query, search, map request, export, event subscription and AI retrieval

- **المدخلات:** معاملات المسار فقط
- **المخرجات:** Caller's resolved SecurityContext
- **الصلاحية:** self؛ النطاق المسموح: org scope of subject roles ∩ classification rule؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SEC-CONTEXT` · عابر للـAggregates · متطلبات: REQ-FND-010
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SEC-CONTEXT returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SEC-CONTEXT
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SEC-CONTEXT is denied
  Given the policy denies the caller
  When the caller sends QRY-SEC-CONTEXT
  Then the response has the same shape as for a missing item (not-found shape)
```

<!-- END GENERATED: build_analysis_design.py -->
