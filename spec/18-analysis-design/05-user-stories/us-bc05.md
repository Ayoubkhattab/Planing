---
id: AD-05-US-BC05
type: user-stories
title: "قصص المستخدم — BC05"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
generator: 17-system-study/_build/build_analysis_design.py
---

# قصص المستخدم — BC05 Readiness — الموارد والجاهزية

مولَّد بالكامل من المصادر بواسطة `17-system-study/_build/build_analysis_design.py`؛ لا يُحرَّر يدويًا. القالب والتصنيف وتعريف ضوابط النوع والفئة في [00-guide.md](00-guide.md).

<!-- BEGIN GENERATED: build_analysis_design.py -->

## ملخص BC05

| نوع العملية | عدد القصص |
|---|---|
| إنشاء | 12 |
| تعديل | 13 |
| جلب | 20 |
| حذف / إنهاء | 22 |
| سير عمل | 21 |
| نظام | 1 |
| نظام (SYS) | 18 |
| **المجموع** | **107** |

### AGG-ALLOCATION — تخصيص الموارد (Resource Allocation)

`03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md` · SLC-09 · الحالات: REQUESTED, PENDING_APPROVAL, COMMITTED → REJECTED, PREEMPTED, RELEASED

#### US-BC05-ALC-APPROVE — اعتماد تخصيص الموارد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | allocation authority | `POST /api/v1/readiness/allocations/{id}/actions/approve` | POL-ALC-APPROVE |

**القصة:** بصفتي **allocation authority**، أريد **اعتماد تخصيص الموارد**، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشروط المسبقة:** الحالة الحالية: PENDING_APPROVAL؛ approver with allocation authority ≠ requester; capacity still available
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← COMMITTED؛ الحدث EVT-ALC-COMMITTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: approver ≠ requester؛ الالتزامات: audit
- **الربط:** `CMD-ALC-APPROVE` · `AGG-ALLOCATION` · متطلبات: REQ-RES-007, REQ-RES-008, REQ-RES-009, REQ-RES-010, REQ-RES-011, REQ-RES-012 · حالات استخدام: UC-053, UC-054, UC-055
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ALC-APPROVE succeeds
  Given AGG-ALLOCATION in state PENDING_APPROVAL and every guard holds
  When allocation authority sends CMD-ALC-APPROVE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes COMMITTED
  And EVT-ALC-COMMITTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ALC-APPROVE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALLOCATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: COMMITTED, PREEMPTED, REJECTED, RELEASED, REQUESTED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ALC-APPROVE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CAPACITY_UNAVAILABLE | 422 | لم يتحقق الشرط: capacity still available |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-ALC-PREEMPT — استباق تخصيص الموارد بأولوية أعلى

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | allocation authority | `POST /api/v1/readiness/allocations/{id}/actions/preempt` | POL-ALC-PREEMPT |

**القصة:** بصفتي **allocation authority**، أريد **استباق تخصيص الموارد بأولوية أعلى**، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشروط المسبقة:** الحالة الحالية: COMMITTED؛ pre-emption decision (BC04 Decision) by an authority for the pool scope; higher-priority allocation reference; owners notified (REQ-RES-009)
- **المدخلات:** `decision`!: urn, `preempting_allocation`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PREEMPTED؛ الحدث EVT-ALC-PREEMPTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: decision by pool-scope authority؛ الالتزامات: audit
- **الربط:** `CMD-ALC-PREEMPT` · `AGG-ALLOCATION` · متطلبات: REQ-RES-007, REQ-RES-008, REQ-RES-009, REQ-RES-010, REQ-RES-011, REQ-RES-012 · حالات استخدام: UC-053, UC-054, UC-055
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ALC-PREEMPT succeeds
  Given AGG-ALLOCATION in state COMMITTED and every guard holds
  When allocation authority sends CMD-ALC-PREEMPT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PREEMPTED
  And EVT-ALC-PREEMPTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ALC-PREEMPT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALLOCATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: PENDING_APPROVAL, PREEMPTED, REJECTED, RELEASED, REQUESTED |
    | AUTHORITY_REQUIRED | 422 | لم يتحقق الشرط: pre-emption decision (BC04 Decision) by an authority for the pool scope |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ALC-PREEMPT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: decision, preempting_allocation |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-ALC-RECORD-CONSUMPTION — تسجيل استهلاك تخصيص الموارد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | task assignee | `POST /api/v1/readiness/allocations/{id}/actions/record-consumption` | POL-ALC-RECORD-CONSUMPTION |

**القصة:** بصفتي **task assignee**، أريد **تسجيل استهلاك تخصيص الموارد**، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشروط المسبقة:** الحالة الحالية: COMMITTED؛ quantity in pool unit; time; consumption beyond commitment flagged (REQ-RES-010)
- **المدخلات:** `quantity`!: number, `at`!: date-time, `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-ALC-CONSUMED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ALC-RECORD-CONSUMPTION` · `AGG-ALLOCATION` · متطلبات: REQ-RES-007, REQ-RES-008, REQ-RES-009, REQ-RES-010, REQ-RES-011, REQ-RES-012 · حالات استخدام: UC-053, UC-054, UC-055
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ALC-RECORD-CONSUMPTION succeeds
  Given AGG-ALLOCATION in state COMMITTED and every guard holds
  When task assignee sends CMD-ALC-RECORD-CONSUMPTION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-ALC-CONSUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ALC-RECORD-CONSUMPTION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALLOCATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: PENDING_APPROVAL, PREEMPTED, REJECTED, RELEASED, REQUESTED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ALC-RECORD-CONSUMPTION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONSUMPTION_INVALID | 422 | لم يتحقق الشرط: consumption beyond commitment flagged (REQ-RES-010) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: quantity, at |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-ALC-REJECT — رفض تخصيص الموارد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | allocation authority | `POST /api/v1/readiness/allocations/{id}/actions/reject` | POL-ALC-REJECT |

**القصة:** بصفتي **allocation authority**، أريد **رفض تخصيص الموارد**، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشروط المسبقة:** الحالة الحالية: PENDING_APPROVAL؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← REJECTED؛ الحدث EVT-ALC-REJECTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ALC-REJECT` · `AGG-ALLOCATION` · متطلبات: REQ-RES-007, REQ-RES-008, REQ-RES-009, REQ-RES-010, REQ-RES-011, REQ-RES-012 · حالات استخدام: UC-053, UC-054, UC-055
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ALC-REJECT succeeds
  Given AGG-ALLOCATION in state PENDING_APPROVAL and every guard holds
  When allocation authority sends CMD-ALC-REJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REJECTED
  And EVT-ALC-REJECTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ALC-REJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALLOCATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: COMMITTED, PREEMPTED, REJECTED, RELEASED, REQUESTED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ALC-REJECT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-ALC-RELEASE — تحرير تخصيص الموارد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Planner | `POST /api/v1/readiness/allocations/{id}/actions/release` | POL-ALC-RELEASE |

**القصة:** بصفتي **Planner**، أريد **تحرير تخصيص الموارد**، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشروط المسبقة:** الحالة الحالية: COMMITTED؛ requester or task owner; unused quantity returned to the ledger
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RELEASED؛ الحدث EVT-ALC-RELEASED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ALC-RELEASE` · `AGG-ALLOCATION` · متطلبات: REQ-RES-007, REQ-RES-008, REQ-RES-009, REQ-RES-010, REQ-RES-011, REQ-RES-012 · حالات استخدام: UC-053, UC-054, UC-055
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ALC-RELEASE succeeds
  Given AGG-ALLOCATION in state COMMITTED and every guard holds
  When Planner sends CMD-ALC-RELEASE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RELEASED
  And EVT-ALC-RELEASED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ALC-RELEASE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALLOCATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: PENDING_APPROVAL, PREEMPTED, REJECTED, RELEASED, REQUESTED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ALC-RELEASE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-ALC-REQUEST — طلب تخصيص الموارد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Planner | `POST /api/v1/readiness/allocations` | POL-ALC-REQUEST |

**القصة:** بصفتي **Planner**، أريد **طلب تخصيص الموارد**، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشروط المسبقة:** الحالة الحالية: ∅؛ pool ACTIVE; quantity > 0 in pool unit; window; priority 1–5; target task/activity/logistics-request (CR-62, SLC-18); requester
- **المدخلات:** `pool`!: urn, `quantity`!: number, `window`!: Interval, `priority`!: integer, `target`!: urn, `justification`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← REQUESTED؛ الحدث EVT-ALC-REQUESTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ALC-REQUEST` · `AGG-ALLOCATION` · متطلبات: REQ-RES-007, REQ-RES-008, REQ-RES-009, REQ-RES-010, REQ-RES-011, REQ-RES-012 · حالات استخدام: UC-053, UC-054, UC-055
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ALC-REQUEST succeeds
  Given AGG-ALLOCATION does not exist yet and every guard holds
  When Planner sends CMD-ALC-REQUEST with a valid payload, a new Idempotency-Key
  Then the state becomes REQUESTED
  And EVT-ALC-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ALC-REQUEST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALLOCATION_INVALID | 422 | لم يتحقق الشرط: pool ACTIVE; quantity > 0 in pool unit; window; priority 1–5; target task/activity/logistics-request (CR-62, SLC-18); requester |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ALC-REQUEST ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: pool, quantity, window, priority, target |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-S-ALLOCATION-01 — تلقائي: all checks passed (تخصيص الموارد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | REQUESTED | COMMITTED |

**القصة:** بصفتي **النظام**، عند «all checks passed»، أريد نقل **تخصيص الموارد** إلى COMMITTED، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشرط:** SPEC-ALLOCATION §1 checks + capacity ledger reserve in priority order (§2)
- **المخرجات:** الحدث EVT-ALC-COMMITTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ALLOCATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-ALLOCATION-02 — تلقائي: checks passed, policy requires approval (تخصيص الموارد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | REQUESTED | PENDING_APPROVAL |

**القصة:** بصفتي **النظام**، عند «checks passed, policy requires approval»، أريد نقل **تخصيص الموارد** إلى PENDING_APPROVAL، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشرط:** PDP obligation REQUIRE_APPROVAL; capacity provisionally held ≤ 1 h
- **المخرجات:** الحدث EVT-ALC-APPROVAL-REQUIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ALLOCATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-ALLOCATION-03 — تلقائي: a check failed (تخصيص الموارد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | شرطي بعد أمر | النظام بهوية عبء عمل | REQUESTED | REJECTED |

**القصة:** بصفتي **النظام**، عند «a check failed»، أريد نقل **تخصيص الموارد** إلى REJECTED، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشرط:** reason codes per failed check
- **المخرجات:** الحدث EVT-ALC-REJECTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ALLOCATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-ALLOCATION-04 — تلقائي: provisional hold (1 h) elapsed (تخصيص الموارد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | PENDING_APPROVAL | REJECTED |

**القصة:** بصفتي **النظام**، عند «provisional hold (1 h) elapsed»، أريد نقل **تخصيص الموارد** إلى REJECTED، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشرط:** capacity released
- **المخرجات:** الحدث EVT-ALC-REJECTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ALLOCATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-ALLOCATION-05 — تلقائي: linked task terminal (تخصيص الموارد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | COMMITTED | RELEASED |

**القصة:** بصفتي **النظام**، عند «linked task terminal»، أريد نقل **تخصيص الموارد** إلى RELEASED، لكي يتحقق غرض تخصيص الموارد: التزام كمية من مجمع لمهمة أو نشاط في نافذة زمنية

- **الشرط:** SLC-03 events (REQ-RES-011)
- **المخرجات:** الحدث EVT-ALC-RELEASED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ALLOCATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-Q-ALC-LIST — جلب: Allocations by pool, task, plan, state

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/allocations` | POL-ALC-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Allocations by pool, task, plan, state**، لكي يتحقق المتطلب: When a resource allocation is requested, the system shall verify authorization, type, availability, capacity, time window, geography, priority, existing commitments and policy before committing it

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Allocations by pool, task, plan, state؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ALC-LIST` · `AGG-ALLOCATION` · متطلبات: REQ-RES-007
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-ALC-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-ALC-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-ALC-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-ALC-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-ASSET — الأصل (Asset)

`03-domain/contexts/BC05/aggregates/AGG-ASSET.md` · SLC-09 · الحالات: IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE, LOST → DISPOSED

#### US-BC05-AST-DISPOSE — التخلص من الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | disposal authority | `POST /api/v1/readiness/assets/{id}/actions/dispose` | POL-AST-DISPOSE |

**القصة:** بصفتي **disposal authority**، أريد **التخلص من الأصل**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: UNSERVICEABLE, LOST؛ disposal authority (decision type asset-disposal); no active reservation or assignment; no legal hold
- **المدخلات:** `decision`!: urn, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DISPOSED؛ الحدث EVT-AST-DISPOSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: asset-disposal authority؛ الالتزامات: audit
- **الربط:** `CMD-AST-DISPOSE` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-DISPOSE succeeds
  Given AGG-ASSET in state UNSERVICEABLE or LOST and every guard holds
  When disposal authority sends CMD-AST-DISPOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DISPOSED
  And EVT-AST-DISPOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-DISPOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, IN_SERVICE, UNDER_MAINTENANCE |
    | AUTHORITY_REQUIRED | 422 | لم يتحقق الشرط: disposal authority (decision type asset-disposal) |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-DISPOSE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: decision, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-FAIL-MAINTENANCE — تسجيل فشل صيانة الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager · disposal authority · Security Officer **[Needs Review]** | `POST /api/v1/readiness/assets/{id}/actions/fail-maintenance` | POL-AST-FAIL-MAINTENANCE |

**القصة:** بصفتي **Resource Manager · disposal authority · Security Officer**، أريد **تسجيل فشل صيانة الأصل**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: UNDER_MAINTENANCE؛ maintenance order COMPLETED with outcome failed; reason
- **المدخلات:** `maintenance_order`!: urn, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← UNSERVICEABLE؛ الحدث EVT-AST-UNSERVICEABLE؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-FAIL-MAINTENANCE` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-FAIL-MAINTENANCE succeeds
  Given AGG-ASSET in state UNDER_MAINTENANCE and every guard holds
  When an authorized actor (Resource Manager or disposal authority or Security Officer) sends CMD-AST-FAIL-MAINTENANCE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNSERVICEABLE
  And EVT-AST-UNSERVICEABLE is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-FAIL-MAINTENANCE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, IN_SERVICE, LOST, UNSERVICEABLE |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-FAIL-MAINTENANCE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: maintenance_order, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-MARK-UNSERVICEABLE — تعليم الأصل كغير صالح للخدمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager · disposal authority · Security Officer **[Needs Review]** | `POST /api/v1/readiness/assets/{id}/actions/mark-unserviceable` | POL-AST-MARK-UNSERVICEABLE |

**القصة:** بصفتي **Resource Manager · disposal authority · Security Officer**، أريد **تعليم الأصل كغير صالح للخدمة**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: IN_SERVICE؛ reason; active assignments are notified; future reservations flagged
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← UNSERVICEABLE؛ الحدث EVT-AST-UNSERVICEABLE؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-MARK-UNSERVICEABLE` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-MARK-UNSERVICEABLE succeeds
  Given AGG-ASSET in state IN_SERVICE and every guard holds
  When an authorized actor (Resource Manager or disposal authority or Security Officer) sends CMD-AST-MARK-UNSERVICEABLE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNSERVICEABLE
  And EVT-AST-UNSERVICEABLE is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-MARK-UNSERVICEABLE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, LOST, UNDER_MAINTENANCE, UNSERVICEABLE |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-MARK-UNSERVICEABLE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-RECLASSIFY — إعادة تصنيف الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Security Officer | `POST /api/v1/readiness/assets/{id}/actions/reclassify` | POL-AST-RECLASSIFY |

**القصة:** بصفتي **Security Officer**، أريد **إعادة تصنيف الأصل**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE, LOST؛ authority per policy
- **المدخلات:** `label`!: Label, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-AST-RECLASSIFIED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-RECLASSIFY` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-RECLASSIFY succeeds
  Given AGG-ASSET in state IN_SERVICE or UNSERVICEABLE or UNDER_MAINTENANCE or LOST and every guard holds
  When Security Officer sends CMD-AST-RECLASSIFY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-AST-RECLASSIFIED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-RECLASSIFY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-RECLASSIFY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CLASSIFICATION_CHANGE_NOT_AUTHORIZED | 422 | لم يتحقق الشرط: authority per policy |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: label, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-RECOVER — استعادة الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager · disposal authority · Security Officer **[Needs Review]** | `POST /api/v1/readiness/assets/{id}/actions/recover` | POL-AST-RECOVER |

**القصة:** بصفتي **Resource Manager · disposal authority · Security Officer**، أريد **استعادة الأصل**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: LOST؛ found; inspection required before service
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← UNSERVICEABLE؛ الحدث EVT-AST-RECOVERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-RECOVER` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-RECOVER succeeds
  Given AGG-ASSET in state LOST and every guard holds
  When an authorized actor (Resource Manager or disposal authority or Security Officer) sends CMD-AST-RECOVER with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNSERVICEABLE
  And EVT-AST-RECOVERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-RECOVER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, IN_SERVICE, UNDER_MAINTENANCE, UNSERVICEABLE |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-RECOVER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-REGISTER — تسجيل الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Resource Manager | `POST /api/v1/readiness/assets` | POL-AST-REGISTER |

**القصة:** بصفتي **Resource Manager**، أريد **تسجيل الأصل**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ type in RD-ASSET-TYPES; owner org; custody holder ACTIVE; linked information entity (entity_type asset-ref) created or referenced in BC02; capabilities; label
- **المدخلات:** `asset_type`!: string, `name`!: LocalizedName, `owner_org`!: urn, `custody_holder`!: urn, `linked_entity`: urn, `capabilities`!: array, `serial`: string, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← IN_SERVICE؛ الحدث EVT-AST-REGISTERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-REGISTER` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-REGISTER succeeds
  Given AGG-ASSET does not exist yet and every guard holds
  When Resource Manager sends CMD-AST-REGISTER with a valid payload, a new Idempotency-Key
  Then the state becomes IN_SERVICE
  And EVT-AST-REGISTERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-REGISTER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID | 422 | لم يتحقق الشرط: type in RD-ASSET-TYPES; linked information entity (entity_type asset-ref) created or referenced in BC02 |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-REGISTER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: asset_type, name, owner_org, custody_holder, capabilities, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-REPORT-LOST — الإبلاغ عن فقد الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager | `POST /api/v1/readiness/assets/{id}/actions/report-lost` | POL-AST-REPORT-LOST |

**القصة:** بصفتي **Resource Manager**، أريد **الإبلاغ عن فقد الأصل**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: IN_SERVICE, UNSERVICEABLE؛ reason; active assignments ended; reservations cancelled
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← LOST؛ الحدث EVT-AST-REPORTED-LOST؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-REPORT-LOST` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-REPORT-LOST succeeds
  Given AGG-ASSET in state IN_SERVICE or UNSERVICEABLE and every guard holds
  When Resource Manager sends CMD-AST-REPORT-LOST with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes LOST
  And EVT-AST-REPORTED-LOST is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-REPORT-LOST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, LOST, UNDER_MAINTENANCE |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-REPORT-LOST ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-RETURN-TO-SERVICE — إعادة الأصل إلى الخدمة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager · disposal authority · Security Officer **[Needs Review]** | `POST /api/v1/readiness/assets/{id}/actions/return-to-service` | POL-AST-RETURN-TO-SERVICE |

**القصة:** بصفتي **Resource Manager · disposal authority · Security Officer**، أريد **إعادة الأصل إلى الخدمة**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: UNDER_MAINTENANCE؛ maintenance order COMPLETED; condition serviceable; required certifications valid
- **المدخلات:** `maintenance_order`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← IN_SERVICE؛ الحدث EVT-AST-RETURNED-TO-SERVICE؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-RETURN-TO-SERVICE` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-RETURN-TO-SERVICE succeeds
  Given AGG-ASSET in state UNDER_MAINTENANCE and every guard holds
  When an authorized actor (Resource Manager or disposal authority or Security Officer) sends CMD-AST-RETURN-TO-SERVICE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_SERVICE
  And EVT-AST-RETURNED-TO-SERVICE is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-RETURN-TO-SERVICE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, IN_SERVICE, LOST, UNSERVICEABLE |
    | ASSET_NOT_SERVICEABLE | 422 | لم يتحقق الشرط: condition serviceable |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-RETURN-TO-SERVICE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: maintenance_order |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-SET-CERTIFICATION — تحديد شهادة الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Resource Manager | `POST /api/v1/readiness/assets/{id}/actions/set-certification` | POL-AST-SET-CERTIFICATION |

**القصة:** بصفتي **Resource Manager**، أريد **تحديد شهادة الأصل**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE؛ certification code, issuer, valid_from/to; evidence
- **المدخلات:** `code`!: string, `issuer`!: string, `valid_from`!: date-time, `valid_to`!: date-time, `evidence`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-AST-CERTIFICATION-SET؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-SET-CERTIFICATION` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-SET-CERTIFICATION succeeds
  Given AGG-ASSET in state IN_SERVICE or UNSERVICEABLE or UNDER_MAINTENANCE and every guard holds
  When Resource Manager sends CMD-AST-SET-CERTIFICATION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-AST-CERTIFICATION-SET is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-SET-CERTIFICATION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, LOST |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-SET-CERTIFICATION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CERTIFICATION_INVALID | 422 | لم يتحقق الشرط: certification code, issuer, valid_from/to |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: code, issuer, valid_from, valid_to |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-START-MAINTENANCE — بدء صيانة الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager · disposal authority · Security Officer **[Needs Review]** | `POST /api/v1/readiness/assets/{id}/actions/start-maintenance` | POL-AST-START-MAINTENANCE |

**القصة:** بصفتي **Resource Manager · disposal authority · Security Officer**، أريد **بدء صيانة الأصل**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: IN_SERVICE, UNSERVICEABLE؛ maintenance order IN_PROGRESS for this asset
- **المدخلات:** `maintenance_order`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← UNDER_MAINTENANCE؛ الحدث EVT-AST-MAINTENANCE-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-START-MAINTENANCE` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-START-MAINTENANCE succeeds
  Given AGG-ASSET in state IN_SERVICE or UNSERVICEABLE and every guard holds
  When an authorized actor (Resource Manager or disposal authority or Security Officer) sends CMD-AST-START-MAINTENANCE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes UNDER_MAINTENANCE
  And EVT-AST-MAINTENANCE-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-START-MAINTENANCE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, LOST, UNDER_MAINTENANCE |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-START-MAINTENANCE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MAINTENANCE_ORDER_REQUIRED | 422 | لم يتحقق الشرط: maintenance order IN_PROGRESS for this asset |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: maintenance_order |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-TRANSFER-CUSTODY — نقل عهدة الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Resource Manager | `POST /api/v1/readiness/assets/{id}/actions/transfer-custody` | POL-AST-TRANSFER-CUSTODY |

**القصة:** بصفتي **Resource Manager**، أريد **نقل عهدة الأصل**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE؛ actor is current holder or custodian authority; new holder ACTIVE in scope; gapless chain
- **المدخلات:** `new_holder`!: urn, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-AST-CUSTODY-TRANSFERRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-TRANSFER-CUSTODY` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-TRANSFER-CUSTODY succeeds
  Given AGG-ASSET in state IN_SERVICE or UNSERVICEABLE or UNDER_MAINTENANCE and every guard holds
  When Resource Manager sends CMD-AST-TRANSFER-CUSTODY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-AST-CUSTODY-TRANSFERRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-TRANSFER-CUSTODY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, LOST |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-TRANSFER-CUSTODY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CUSTODY_INVALID | 422 | لم يتحقق الشرط: actor is current holder or custodian authority |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: new_holder, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-AST-UPDATE-CONDITION — تحديث حالة الأصل الفنية

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Resource Manager | `POST /api/v1/readiness/assets/{id}/actions/update-condition` | POL-AST-UPDATE-CONDITION |

**القصة:** بصفتي **Resource Manager**، أريد **تحديث حالة الأصل الفنية**، لكي يتحقق غرض الأصل: أصل مادي بملكية وحيازة وحالة وقدرات وشهادات وصيانة

- **الشروط المسبقة:** الحالة الحالية: IN_SERVICE, UNSERVICEABLE, UNDER_MAINTENANCE؛ condition grade in RD-CONDITION-GRADES; inspector; unserviceable grades require CMD-AST-MARK-UNSERVICEABLE
- **المدخلات:** `grade`!: string, `inspector`!: urn, `notes`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-AST-CONDITION-UPDATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-AST-UPDATE-CONDITION` · `AGG-ASSET` · متطلبات: REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 · حالات استخدام: UC-050, UC-051, UC-053
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-AST-UPDATE-CONDITION succeeds
  Given AGG-ASSET in state IN_SERVICE or UNSERVICEABLE or UNDER_MAINTENANCE and every guard holds
  When Resource Manager sends CMD-AST-UPDATE-CONDITION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-AST-CONDITION-UPDATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-AST-UPDATE-CONDITION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DISPOSED, LOST |
    | AUTHZ_DENIED | 403→404 | السياسة POL-AST-UPDATE-CONDITION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONDITION_INVALID | 422 | لم يتحقق الشرط: condition grade in RD-CONDITION-GRADES |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: grade, inspector |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-Q-AST-AVAILABILITY — جلب: Assets of type/capability available in a window (and optional bbox), with blocking reasons for others visible to caller

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `POST /api/v1/readiness/asset-availability-queries` | POL-AST-AVAILABILITY |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Assets of type/capability available in a window (and optional bbox), with blocking reasons for others visible to caller**، لكي يتحقق المتطلب: When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavailable for new assignments from that moment

- **المدخلات:** `asset_types`, `capabilities`, `window`!, `bbox` (معاملات الرابط وحقول جسم الطلب؛ `!` = إلزامي)؛ مع ترويسة `X-Purpose`
- **المخرجات:** Assets of type/capability available in a window (and optional bbox), with blocking reasons for others visible to caller
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AST-AVAILABILITY` · `AGG-ASSET` · متطلبات: REQ-RES-003
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-AST-AVAILABILITY computes its result only over what the caller may see
  Given data inside and outside the caller's allowed_scope
  When the caller sends QRY-AST-AVAILABILITY
  Then the result neither includes nor reveals data outside allowed_scope

Scenario: QRY-AST-AVAILABILITY is denied
  Given the policy denies the caller
  When the caller sends QRY-AST-AVAILABILITY
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC05-Q-AST-GET — جلب: Asset with status, condition, certifications, custody chain, linked entity

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/assets/{asset_id}` | POL-AST-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Asset with status, condition, certifications, custody chain, linked entity**، لكي يتحقق المتطلب: The system shall register each asset with type, ownership, custody holder, status, condition, location, capabilities, certifications and maintenance schedule

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Asset with status, condition, certifications, custody chain, linked entity
- **الصلاحية:** label rule؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-AST-GET` · `AGG-ASSET` · متطلبات: REQ-RES-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-AST-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-AST-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-AST-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-AST-GET
  Then the response is 404 with the same shape as for a missing item
```

### AGG-ASSET-ASSIGNMENT — إسناد الأصل (Asset Assignment)

`03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md` · SLC-09 · الحالات: ACTIVE → RETURNED, CANCELLED

#### US-BC05-ASG-ASSIGN — تسجيل إسناد الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Resource Manager / Planner | `POST /api/v1/readiness/asset-assignments` | POL-ASG-ASSIGN |

**القصة:** بصفتي **Resource Manager / Planner**، أريد **تسجيل إسناد الأصل**، لكي يتحقق غرض إسناد الأصل: استخدام فعلي لأصل في مهمة أو وحدة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ asset available (or covered by the caller's CONFIRMED reservation); asset certifications satisfy the task type's asset requirements; custody authorization; assignee cleared for asset label
- **المدخلات:** `asset`!: urn, `task`: urn, `unit`: urn, `window`!: Interval, `reservation`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-ASG-ASSIGNED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / Planner؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ASG-ASSIGN` · `AGG-ASSET-ASSIGNMENT` · متطلبات: REQ-RES-003, REQ-RES-012 · حالات استخدام: UC-051, UC-053, UC-054
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ASG-ASSIGN succeeds
  Given AGG-ASSET-ASSIGNMENT does not exist yet and every guard holds
  When Resource Manager / Planner sends CMD-ASG-ASSIGN with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-ASG-ASSIGNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ASG-ASSIGN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_NOT_AVAILABLE | 422 | لم يتحقق الشرط: asset available (or covered by the caller's CONFIRMED reservation); asset certifications satisfy the task type's asset requirements; assignee cleared for asset label |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ASG-ASSIGN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: asset, window |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-ASG-CANCEL — إلغاء إسناد الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Resource Manager / Planner | `POST /api/v1/readiness/asset-assignments/{id}/actions/cancel` | POL-ASG-CANCEL |

**القصة:** بصفتي **Resource Manager / Planner**، أريد **إلغاء إسناد الأصل**، لكي يتحقق غرض إسناد الأصل: استخدام فعلي لأصل في مهمة أو وحدة

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ assigned in error; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-ASG-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / Planner؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ASG-CANCEL` · `AGG-ASSET-ASSIGNMENT` · متطلبات: REQ-RES-003, REQ-RES-012 · حالات استخدام: UC-051, UC-053, UC-054
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ASG-CANCEL succeeds
  Given AGG-ASSET-ASSIGNMENT in state ACTIVE and every guard holds
  When Resource Manager / Planner sends CMD-ASG-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-ASG-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ASG-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, RETURNED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ASG-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-ASG-RETURN — إرجاع الأصل وإنهاء إسناد الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Resource Manager / Planner | `POST /api/v1/readiness/asset-assignments/{id}/actions/return` | POL-ASG-RETURN |

**القصة:** بصفتي **Resource Manager / Planner**، أريد **إرجاع الأصل وإنهاء إسناد الأصل**، لكي يتحقق غرض إسناد الأصل: استخدام فعلي لأصل في مهمة أو وحدة

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ condition report; asset condition updated accordingly
- **المدخلات:** `condition_report`!: object — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETURNED؛ الحدث EVT-ASG-RETURNED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / Planner؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-ASG-RETURN` · `AGG-ASSET-ASSIGNMENT` · متطلبات: REQ-RES-003, REQ-RES-012 · حالات استخدام: UC-051, UC-053, UC-054
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-ASG-RETURN succeeds
  Given AGG-ASSET-ASSIGNMENT in state ACTIVE and every guard holds
  When Resource Manager / Planner sends CMD-ASG-RETURN with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETURNED
  And EVT-ASG-RETURNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-ASG-RETURN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, RETURNED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-ASG-RETURN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CONDITION_REPORT_REQUIRED | 422 | لم يتحقق الشرط: condition report; asset condition updated accordingly |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: condition_report |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-S-ASSET-ASSIGNMENT-01 — تلقائي: linked task terminal (إسناد الأصل)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | ACTIVE | RETURNED |

**القصة:** بصفتي **النظام**، عند «linked task terminal»، أريد نقل **إسناد الأصل** إلى RETURNED، لكي يتحقق غرض إسناد الأصل: استخدام فعلي لأصل في مهمة أو وحدة

- **الشرط:** condition report requested from last holder (follow-up task)
- **المخرجات:** الحدث EVT-ASG-RETURNED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ASSET-ASSIGNMENT` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

### AGG-ASSET-RESERVATION — حجز الأصل (Asset Reservation)

`03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md` · SLC-09 · الحالات: HELD, CONFIRMED → RELEASED, EXPIRED, CANCELLED

#### US-BC05-RSV-CANCEL — إلغاء حجز الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Planner / Resource Manager | `POST /api/v1/readiness/asset-reservations/{id}/actions/cancel` | POL-RSV-CANCEL |

**القصة:** بصفتي **Planner / Resource Manager**، أريد **إلغاء حجز الأصل**، لكي يتحقق غرض حجز الأصل: حجز أصل لنافذة زمنية قبل الاستخدام

- **الشروط المسبقة:** الحالة الحالية: HELD, CONFIRMED؛ requester or asset owner; reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-RSV-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Planner / Resource Manager؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RSV-CANCEL` · `AGG-ASSET-RESERVATION` · متطلبات: REQ-RES-014 · حالات استخدام: UC-052
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RSV-CANCEL succeeds
  Given AGG-ASSET-RESERVATION in state HELD or CONFIRMED and every guard holds
  When Planner / Resource Manager sends CMD-RSV-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-RSV-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RSV-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_RESERVATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, EXPIRED, RELEASED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RSV-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-RSV-CONFIRM — تأكيد حجز الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Planner / Resource Manager | `POST /api/v1/readiness/asset-reservations/{id}/actions/confirm` | POL-RSV-CONFIRM |

**القصة:** بصفتي **Planner / Resource Manager**، أريد **تأكيد حجز الأصل**، لكي يتحقق غرض حجز الأصل: حجز أصل لنافذة زمنية قبل الاستخدام

- **الشروط المسبقة:** الحالة الحالية: HELD؛ linked to a task or plan activity
- **المدخلات:** `link`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CONFIRMED؛ الحدث EVT-RSV-CONFIRMED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Planner / Resource Manager؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RSV-CONFIRM` · `AGG-ASSET-RESERVATION` · متطلبات: REQ-RES-014 · حالات استخدام: UC-052
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RSV-CONFIRM succeeds
  Given AGG-ASSET-RESERVATION in state HELD and every guard holds
  When Planner / Resource Manager sends CMD-RSV-CONFIRM with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CONFIRMED
  And EVT-RSV-CONFIRMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RSV-CONFIRM is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_RESERVATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, CONFIRMED, EXPIRED, RELEASED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RSV-CONFIRM ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LINK_REQUIRED | 422 | لم يتحقق الشرط: linked to a task or plan activity |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: link |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-RSV-HOLD — إنشاء حجز الأصل مبدئيًا

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Planner / Resource Manager | `POST /api/v1/readiness/asset-reservations` | POL-RSV-HOLD |

**القصة:** بصفتي **Planner / Resource Manager**، أريد **إنشاء حجز الأصل مبدئيًا**، لكي يتحقق غرض حجز الأصل: حجز أصل لنافذة زمنية قبل الاستخدام

- **الشروط المسبقة:** الحالة الحالية: ∅؛ asset available for the window (INV-AST-01); purpose; requester authorized in asset owner scope
- **المدخلات:** `asset`!: urn, `window`!: Interval, `purpose`!: string, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← HELD؛ الحدث EVT-RSV-HELD؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Planner / Resource Manager؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RSV-HOLD` · `AGG-ASSET-RESERVATION` · متطلبات: REQ-RES-014 · حالات استخدام: UC-052
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RSV-HOLD succeeds
  Given AGG-ASSET-RESERVATION does not exist yet and every guard holds
  When Planner / Resource Manager sends CMD-RSV-HOLD with a valid payload, a new Idempotency-Key
  Then the state becomes HELD
  And EVT-RSV-HELD is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RSV-HOLD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_RESERVED | 422 | لم يتحقق الشرط: asset available for the window (INV-AST-01); requester authorized in asset owner scope |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RSV-HOLD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: asset, window, purpose, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-RSV-RELEASE — تحرير حجز الأصل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Planner / Resource Manager | `POST /api/v1/readiness/asset-reservations/{id}/actions/release` | POL-RSV-RELEASE |

**القصة:** بصفتي **Planner / Resource Manager**، أريد **تحرير حجز الأصل**، لكي يتحقق غرض حجز الأصل: حجز أصل لنافذة زمنية قبل الاستخدام

- **الشروط المسبقة:** الحالة الحالية: CONFIRMED؛ requester or linked task terminal
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RELEASED؛ الحدث EVT-RSV-RELEASED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Planner / Resource Manager؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RSV-RELEASE` · `AGG-ASSET-RESERVATION` · متطلبات: REQ-RES-014 · حالات استخدام: UC-052
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RSV-RELEASE succeeds
  Given AGG-ASSET-RESERVATION in state CONFIRMED and every guard holds
  When Planner / Resource Manager sends CMD-RSV-RELEASE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RELEASED
  And EVT-RSV-RELEASED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RSV-RELEASE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ASSET_RESERVATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, EXPIRED, HELD, RELEASED |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RSV-RELEASE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-S-ASSET-RESERVATION-01 — تلقائي: hold expiry (24 h) reached (حجز الأصل)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | HELD | EXPIRED |

**القصة:** بصفتي **النظام**، عند «hold expiry (24 h) reached»، أريد نقل **حجز الأصل** إلى EXPIRED، لكي يتحقق غرض حجز الأصل: حجز أصل لنافذة زمنية قبل الاستخدام

- **الشرط:** scheduler
- **المخرجات:** الحدث EVT-RSV-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ASSET-RESERVATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-ASSET-RESERVATION-02 — تلقائي: linked task or plan terminal (حجز الأصل)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | CONFIRMED | RELEASED |

**القصة:** بصفتي **النظام**، عند «linked task or plan terminal»، أريد نقل **حجز الأصل** إلى RELEASED، لكي يتحقق غرض حجز الأصل: حجز أصل لنافذة زمنية قبل الاستخدام

- **الشرط:** SLC-03/SLC-08 events
- **المخرجات:** الحدث EVT-RSV-RELEASED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-ASSET-RESERVATION` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

### AGG-EXERCISE — التمرين (Exercise)

`03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md` · SLC-19 · الحالات: PLANNED, SCHEDULED, IN_PROGRESS → COMPLETED, ABORTED, CANCELLED

#### US-BC05-EXR-CANCEL — إلغاء التمرين

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Exercise Director / Training Manager | `POST /api/v1/readiness/exercises/{id}/actions/cancel` | POL-EXR-CANCEL |

**القصة:** بصفتي **Exercise Director / Training Manager**، أريد **إلغاء التمرين**، لكي يتحقق غرض التمرين: حدث تدريبي/جاهزية مجدوَل ينفّذ سيناريو محدَّداً لمجموعة مشاركين

- **الشروط المسبقة:** الحالة الحالية: PLANNED, SCHEDULED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-EXR-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Director / Training Manager؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EXR-CANCEL` · `AGG-EXERCISE` · متطلبات: REQ-TRX-003, REQ-TRX-004, REQ-TRX-005, REQ-TRX-006, REQ-TRX-007 · حالات استخدام: UC-161, UC-162
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EXR-CANCEL succeeds
  Given AGG-EXERCISE in state PLANNED or SCHEDULED and every guard holds
  When Exercise Director / Training Manager sends CMD-EXR-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-EXR-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EXR-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EXR-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EXERCISE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ABORTED, CANCELLED, COMPLETED, IN_PROGRESS |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-EXR-PLAN — تخطيط التمرين

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Exercise Director / Training Manager | `POST /api/v1/readiness/exercises` | POL-EXR-PLAN |

**القصة:** بصفتي **Exercise Director / Training Manager**، أريد **تخطيط التمرين**، لكي يتحقق غرض التمرين: حدث تدريبي/جاهزية مجدوَل ينفّذ سيناريو محدَّداً لمجموعة مشاركين

- **الشروط المسبقة:** الحالة الحالية: ∅؛ scenario ACTIVE at this instant, frozen thereafter (INV-EXR-01); objectives; participants; purpose; role_ref optional (readiness comparison reuses SLC-09's AGG-ROLE-REQUIREMENT read-only, no new eligibility mechanism)
- **المدخلات:** `scenario`!: urn, `objectives`!: string, `participants`!: array, `purpose`!: enum(drill,certification,assessment), `role_ref`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← PLANNED؛ الحدث EVT-EXR-PLANNED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Director / Training Manager؛ الشروط: tenant match; scenario ACTIVE and visible to actor؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EXR-PLAN` · `AGG-EXERCISE` · متطلبات: REQ-TRX-003, REQ-TRX-004, REQ-TRX-005, REQ-TRX-006, REQ-TRX-007 · حالات استخدام: UC-161, UC-162
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EXR-PLAN succeeds
  Given AGG-EXERCISE does not exist yet and every guard holds
  When Exercise Director / Training Manager sends CMD-EXR-PLAN with a valid payload, a new Idempotency-Key
  Then the state becomes PLANNED
  And EVT-EXR-PLANNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EXR-PLAN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EXR-PLAN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EXERCISE_INVALID | 422 | لم يتحقق الشرط: scenario ACTIVE at this instant, frozen thereafter (INV-EXR-01); objectives; participants; purpose; role_ref optional (readiness comparison reuses SLC-09's AGG-ROLE-REQUIREMENT read-only, no new eligibility mechanism) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: scenario, objectives, participants, purpose |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-EXR-SCHEDULE — جدولة التمرين

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Exercise Director / Training Manager | `POST /api/v1/readiness/exercises/{id}/actions/schedule` | POL-EXR-SCHEDULE |

**القصة:** بصفتي **Exercise Director / Training Manager**، أريد **جدولة التمرين**، لكي يتحقق غرض التمرين: حدث تدريبي/جاهزية مجدوَل ينفّذ سيناريو محدَّداً لمجموعة مشاركين

- **الشروط المسبقة:** الحالة الحالية: PLANNED؛ window.from < window.to; location; participants confirmed
- **المدخلات:** `window`!: Interval, `location`!: LocalizedName, `participants`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SCHEDULED؛ الحدث EVT-EXR-SCHEDULED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Director / Training Manager؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EXR-SCHEDULE` · `AGG-EXERCISE` · متطلبات: REQ-TRX-003, REQ-TRX-004, REQ-TRX-005, REQ-TRX-006, REQ-TRX-007 · حالات استخدام: UC-161, UC-162
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EXR-SCHEDULE succeeds
  Given AGG-EXERCISE in state PLANNED and every guard holds
  When Exercise Director / Training Manager sends CMD-EXR-SCHEDULE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SCHEDULED
  And EVT-EXR-SCHEDULED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EXR-SCHEDULE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EXR-SCHEDULE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EXERCISE_INVALID | 422 | لم يتحقق الشرط: window.from < window.to; location; participants confirmed |
    | EXERCISE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ABORTED, CANCELLED, COMPLETED, IN_PROGRESS, SCHEDULED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: window, location, participants |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-EXR-START — بدء التمرين

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Exercise Director / Training Manager | `POST /api/v1/readiness/exercises/{id}/actions/start` | POL-EXR-START |

**القصة:** بصفتي **Exercise Director / Training Manager**، أريد **بدء التمرين**، لكي يتحقق غرض التمرين: حدث تدريبي/جاهزية مجدوَل ينفّذ سيناريو محدَّداً لمجموعة مشاركين

- **الشروط المسبقة:** الحالة الحالية: SCHEDULED؛ scheduled window reached (or authorized override); system creates a linked Simulation in the same unit of work (CMD-SIM-START, exercise_ref = this, scenario_ref = the frozen scenario — mirrors the linked-creation pattern of CR-62)
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← IN_PROGRESS؛ الحدث EVT-EXR-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Director / Training Manager؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-EXR-START` · `AGG-EXERCISE` · متطلبات: REQ-TRX-003, REQ-TRX-004, REQ-TRX-005, REQ-TRX-006, REQ-TRX-007 · حالات استخدام: UC-161, UC-162
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-EXR-START succeeds
  Given AGG-EXERCISE in state SCHEDULED and every guard holds
  When Exercise Director / Training Manager sends CMD-EXR-START with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_PROGRESS
  And EVT-EXR-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-EXR-START is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-EXR-START ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EXERCISE_INVALID | 422 | لم يتحقق الشرط: system creates a linked Simulation in the same unit of work (CMD-SIM-START, exercise_ref = this, scenario_ref = the frozen scenario — mirrors the linked-creation pattern of CR-62) |
    | EXERCISE_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ABORTED, CANCELLED, COMPLETED, IN_PROGRESS, PLANNED |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-S-EXERCISE-01 — تلقائي: linked simulation completed (التمرين)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | IN_PROGRESS | COMPLETED |

**القصة:** بصفتي **النظام**، عند «linked simulation completed»، أريد نقل **التمرين** إلى COMPLETED، لكي يتحقق غرض التمرين: حدث تدريبي/جاهزية مجدوَل ينفّذ سيناريو محدَّداً لمجموعة مشاركين

- **الشرط:** system; driven exclusively by the linked Simulation's own EVT-SIM-COMPLETED (INV-EXR-02)
- **المخرجات:** الحدث EVT-EXR-COMPLETED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-EXERCISE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-EXERCISE-02 — تلقائي: linked simulation aborted (التمرين)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | IN_PROGRESS | ABORTED |

**القصة:** بصفتي **النظام**، عند «linked simulation aborted»، أريد نقل **التمرين** إلى ABORTED، لكي يتحقق غرض التمرين: حدث تدريبي/جاهزية مجدوَل ينفّذ سيناريو محدَّداً لمجموعة مشاركين

- **الشرط:** system; driven exclusively by the linked Simulation's own EVT-SIM-ABORTED (INV-EXR-02)
- **المخرجات:** الحدث EVT-EXR-ABORTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-EXERCISE` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-Q-EXR-GET — جلب: Exercise with frozen scenario reference, participants, current state

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/exercises/{exercise_id}` | POL-EXR-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Exercise with frozen scenario reference, participants, current state**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted to the caller's visible scope

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Exercise with frozen scenario reference, participants, current state
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-EXR-GET` · `AGG-EXERCISE` · متطلبات: REQ-TRX-014
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-EXR-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-EXR-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-EXR-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-EXR-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC05-Q-EXR-LIST — جلب: Exercises filtered by scenario, state, window

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/exercises` | POL-EXR-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Exercises filtered by scenario, state, window**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted to the caller's visible scope

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Exercises filtered by scenario, state, window؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-EXR-LIST` · `AGG-EXERCISE` · متطلبات: REQ-TRX-014
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-EXR-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-EXR-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-EXR-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-EXR-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-LOGISTICS-REQUEST — طلب الإمداد (Logistics Request)

`03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md` · SLC-18 · الحالات: REQUESTED, PENDING_APPROVAL, APPROVED, IN_TRANSIT → FULFILLED, PARTIALLY_FULFILLED, REJECTED, CANCELLED

#### US-BC05-LGR-CANCEL — إلغاء طلب الإمداد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | requester · logistics authority | `POST /api/v1/readiness/logistics-requests/{id}/actions/cancel` | POL-LGR-CANCEL |

**القصة:** بصفتي **requester · logistics authority**، أريد **إلغاء طلب الإمداد**، لكي يتحقق غرض طلب الإمداد: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه

- **الشروط المسبقة:** الحالة الحالية: REQUESTED, PENDING_APPROVAL, APPROVED؛ requester or logistics authority; reason; releases the linked allocation if COMMITTED (CMD-ALC-RELEASE), or leaves a PENDING_APPROVAL allocation to its own provisional-hold expiry
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-LGR-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** requester · logistics authority؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-LGR-CANCEL` · `AGG-LOGISTICS-REQUEST` · متطلبات: REQ-LOG-001, REQ-LOG-002, REQ-LOG-003, REQ-LOG-008, REQ-LOG-009, REQ-LOG-013, REQ-LOG-014 · حالات استخدام: UC-150, UC-152
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-LGR-CANCEL succeeds
  Given AGG-LOGISTICS-REQUEST in state REQUESTED or PENDING_APPROVAL or APPROVED and every guard holds
  When an authorized actor (requester or logistics authority) sends CMD-LGR-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-LGR-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-LGR-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-LGR-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: IN_TRANSIT, FULFILLED, PARTIALLY_FULFILLED, REJECTED, CANCELLED — الحالات النهائية FULFILLED, PARTIALLY_FULFILLED, REJECTED, CANCELLED بلا صف في المصفوفة، وأُضيفت لأن الحالة النهائية لا تقبل أوامر **[Derived]** |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-LGR-DISPATCH — إرسال طلب الإمداد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | dispatcher | `POST /api/v1/readiness/logistics-requests/{id}/actions/dispatch` | POL-LGR-DISPATCH |

**القصة:** بصفتي **dispatcher**، أريد **إرسال طلب الإمداد**، لكي يتحقق غرض طلب الإمداد: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه

- **الشروط المسبقة:** الحالة الحالية: APPROVED؛ dispatcher; linked allocation still COMMITTED; creates a Shipment (AGG-SHIPMENT) referencing this request and the allocation; ship_quantity ≤ requested quantity
- **المدخلات:** `carrier`!: string, `ship_quantity`!: number — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← IN_TRANSIT؛ الحدث EVT-LGR-DISPATCHED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** dispatcher؛ الشروط: tenant match; linked allocation COMMITTED (INV-LGR-02)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-LGR-DISPATCH` · `AGG-LOGISTICS-REQUEST` · متطلبات: REQ-LOG-001, REQ-LOG-002, REQ-LOG-003, REQ-LOG-008, REQ-LOG-009, REQ-LOG-013, REQ-LOG-014 · حالات استخدام: UC-150, UC-152
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-LGR-DISPATCH succeeds
  Given AGG-LOGISTICS-REQUEST in state APPROVED and every guard holds
  When dispatcher sends CMD-LGR-DISPATCH with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_TRANSIT
  And EVT-LGR-DISPATCHED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-LGR-DISPATCH is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | ALLOCATION_NOT_COMMITTED | 422 | لم يتحقق الشرط: linked allocation still COMMITTED; creates a Shipment (AGG-SHIPMENT) referencing this request and the allocation |
    | AUTHZ_DENIED | 403→404 | السياسة POL-LGR-DISPATCH ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: IN_TRANSIT, PENDING_APPROVAL, REQUESTED, FULFILLED, PARTIALLY_FULFILLED, REJECTED, CANCELLED — الحالات النهائية FULFILLED, PARTIALLY_FULFILLED, REJECTED, CANCELLED بلا صف في المصفوفة، وأُضيفت لأن الحالة النهائية لا تقبل أوامر **[Derived]** |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: carrier, ship_quantity |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-LGR-REQUEST — تقديم طلب الإمداد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Logistics Officer / Planner | `POST /api/v1/readiness/logistics-requests` | POL-LGR-REQUEST |

**القصة:** بصفتي **Logistics Officer / Planner**، أريد **تقديم طلب الإمداد**، لكي يتحقق غرض طلب الإمداد: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه

- **الشروط المسبقة:** الحالة الحالية: ∅؛ item pool ACTIVE (AGG-RESOURCE-POOL, resource_type in RD-LOGISTICS-ITEM-TYPES); quantity > 0 in pool unit; destination; needed_by; priority 1–5; requester; justification; system issues a linked allocation request in the same unit of work (CMD-ALC-REQUEST, target = this request — CR-62)
- **المدخلات:** `item_pool`!: urn, `quantity`!: number, `destination`!: LocalizedName, `needed_by`!: date-time, `priority`!: integer, `justification`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← REQUESTED؛ الحدث EVT-LGR-REQUESTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Logistics Officer / Planner؛ الشروط: tenant match; item_pool visible to actor؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-LGR-REQUEST` · `AGG-LOGISTICS-REQUEST` · متطلبات: REQ-LOG-001, REQ-LOG-002, REQ-LOG-003, REQ-LOG-008, REQ-LOG-009, REQ-LOG-013, REQ-LOG-014 · حالات استخدام: UC-150, UC-152
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-LGR-REQUEST succeeds
  Given AGG-LOGISTICS-REQUEST does not exist yet and every guard holds
  When Logistics Officer / Planner sends CMD-LGR-REQUEST with a valid payload, a new Idempotency-Key
  Then the state becomes REQUESTED
  And EVT-LGR-REQUESTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-LGR-REQUEST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-LGR-REQUEST ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | LOGISTICS_REQUEST_INVALID | 422 | لم يتحقق الشرط: item pool ACTIVE (AGG-RESOURCE-POOL, resource_type in RD-LOGISTICS-ITEM-TYPES); requester; system issues a linked allocation request in the same unit of work (CMD-ALC-REQUEST, target = this request — CR-62) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: item_pool, quantity, destination, needed_by, priority |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-S-LOGISTICS-REQUEST-01 — تلقائي: linked allocation committed (طلب الإمداد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | REQUESTED | APPROVED |

**القصة:** بصفتي **النظام**، عند «linked allocation committed»، أريد نقل **طلب الإمداد** إلى APPROVED، لكي يتحقق غرض طلب الإمداد: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه

- **الشرط:** SLC-09 EVT-ALC-COMMITTED for the linked allocation
- **المخرجات:** الحدث EVT-LGR-APPROVED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-LOGISTICS-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-LOGISTICS-REQUEST-02 — تلقائي: linked allocation requires approval (طلب الإمداد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | REQUESTED | PENDING_APPROVAL |

**القصة:** بصفتي **النظام**، عند «linked allocation requires approval»، أريد نقل **طلب الإمداد** إلى PENDING_APPROVAL، لكي يتحقق غرض طلب الإمداد: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه

- **الشرط:** SLC-09 EVT-ALC-APPROVAL-REQUIRED for the linked allocation
- **المخرجات:** الحدث EVT-LGR-PENDING-APPROVAL؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-LOGISTICS-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-LOGISTICS-REQUEST-03 — تلقائي: linked allocation rejected (طلب الإمداد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | REQUESTED | REJECTED |

**القصة:** بصفتي **النظام**، عند «linked allocation rejected»، أريد نقل **طلب الإمداد** إلى REJECTED، لكي يتحقق غرض طلب الإمداد: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه

- **الشرط:** SLC-09 EVT-ALC-REJECTED for the linked allocation; reason codes carried over
- **المخرجات:** الحدث EVT-LGR-REJECTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-LOGISTICS-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-LOGISTICS-REQUEST-04 — تلقائي: linked allocation committed (طلب الإمداد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | PENDING_APPROVAL | APPROVED |

**القصة:** بصفتي **النظام**، عند «linked allocation committed»، أريد نقل **طلب الإمداد** إلى APPROVED، لكي يتحقق غرض طلب الإمداد: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه

- **الشرط:** SLC-09 EVT-ALC-COMMITTED for the linked allocation
- **المخرجات:** الحدث EVT-LGR-APPROVED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-LOGISTICS-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-LOGISTICS-REQUEST-05 — تلقائي: linked allocation rejected (طلب الإمداد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | PENDING_APPROVAL | REJECTED |

**القصة:** بصفتي **النظام**، عند «linked allocation rejected»، أريد نقل **طلب الإمداد** إلى REJECTED، لكي يتحقق غرض طلب الإمداد: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه

- **الشرط:** SLC-09 EVT-ALC-REJECTED for the linked allocation (approval denied or provisional hold elapsed)
- **المخرجات:** الحدث EVT-LGR-REJECTED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-LOGISTICS-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-LOGISTICS-REQUEST-06 — تلقائي: linked shipment delivered in full (طلب الإمداد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | IN_TRANSIT | FULFILLED |

**القصة:** بصفتي **النظام**، عند «linked shipment delivered in full»، أريد نقل **طلب الإمداد** إلى FULFILLED، لكي يتحقق غرض طلب الإمداد: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه

- **الشرط:** SLC-18 EVT-SHP-DELIVERED with delivered_quantity = requested quantity; records consumption on the linked allocation (CMD-ALC-RECORD-CONSUMPTION)
- **المخرجات:** الحدث EVT-LGR-FULFILLED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-LOGISTICS-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-S-LOGISTICS-REQUEST-07 — تلقائي: linked shipment resolved short (طلب الإمداد)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | مدفوع بحدث | النظام بهوية عبء عمل | IN_TRANSIT | PARTIALLY_FULFILLED |

**القصة:** بصفتي **النظام**، عند «linked shipment resolved short»، أريد نقل **طلب الإمداد** إلى PARTIALLY_FULFILLED، لكي يتحقق غرض طلب الإمداد: طلب كمية من صنف إمداد لوجهة؛ يقود إلى تخصيص من دفتر سعة المخزون (SLC-09) وشحنة تُنفّذه

- **الشرط:** SLC-18 EVT-SHP-DELIVERED with delivered_quantity < requested quantity, or EVT-SHP-DAMAGED / EVT-SHP-LOST; records consumption for the quantity actually delivered before the incident (possibly zero)
- **المخرجات:** الحدث EVT-LGR-PARTIALLY-FULFILLED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-LOGISTICS-REQUEST` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-Q-LGR-GET — جلب: Logistics request with linked allocation and shipment refs

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/logistics-requests/{request_id}` | POL-LGR-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Logistics request with linked allocation and shipment refs**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter logistics requests by item, destination, state and priority, restricted to the caller's visible scope

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Logistics request with linked allocation and shipment refs
- **الصلاحية:** allowed_scope; requester؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-LGR-GET` · `AGG-LOGISTICS-REQUEST` · متطلبات: REQ-LOG-010
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-LGR-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-LGR-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-LGR-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-LGR-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC05-Q-LGR-LIST — جلب: Logistics requests filtered by item, destination, state, priority

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/logistics-requests` | POL-LGR-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Logistics requests filtered by item, destination, state, priority**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter logistics requests by item, destination, state and priority, restricted to the caller's visible scope

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Logistics requests filtered by item, destination, state, priority؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-LGR-LIST` · `AGG-LOGISTICS-REQUEST` · متطلبات: REQ-LOG-010
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-LGR-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-LGR-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-LGR-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-LGR-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-MAINTENANCE-ORDER — أمر الصيانة (Maintenance Order)

`03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md` · SLC-09 · الحالات: PLANNED, IN_PROGRESS → COMPLETED, CANCELLED

#### US-BC05-MNT-CANCEL — إلغاء أمر الصيانة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Resource Manager / technician | `POST /api/v1/readiness/maintenance-orders/{id}/actions/cancel` | POL-MNT-CANCEL |

**القصة:** بصفتي **Resource Manager / technician**، أريد **إلغاء أمر الصيانة**، لكي يتحقق غرض أمر الصيانة: أمر صيانة مجدول أو تصحيحي بنافذة زمنية تحجب التوفر

- **الشروط المسبقة:** الحالة الحالية: PLANNED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-MNT-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / technician؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MNT-CANCEL` · `AGG-MAINTENANCE-ORDER` · متطلبات: REQ-RES-004 · حالات استخدام: UC-051
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MNT-CANCEL succeeds
  Given AGG-MAINTENANCE-ORDER in state PLANNED and every guard holds
  When Resource Manager / technician sends CMD-MNT-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-MNT-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MNT-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MNT-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, IN_PROGRESS |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-MNT-COMPLETE — إكمال أمر الصيانة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Resource Manager / technician | `POST /api/v1/readiness/maintenance-orders/{id}/actions/complete` | POL-MNT-COMPLETE |

**القصة:** بصفتي **Resource Manager / technician**، أريد **إكمال أمر الصيانة**، لكي يتحقق غرض أمر الصيانة: أمر صيانة مجدول أو تصحيحي بنافذة زمنية تحجب التوفر

- **الشروط المسبقة:** الحالة الحالية: IN_PROGRESS؛ outcome ∈ {serviceable, failed}; work performed; parts consumed (optional allocation refs)
- **المدخلات:** `outcome`!: enum(serviceable,failed), `work`!: LocalizedName, `parts`: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← COMPLETED؛ الحدث EVT-MNT-COMPLETED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / technician؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MNT-COMPLETE` · `AGG-MAINTENANCE-ORDER` · متطلبات: REQ-RES-004 · حالات استخدام: UC-051
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MNT-COMPLETE succeeds
  Given AGG-MAINTENANCE-ORDER in state IN_PROGRESS and every guard holds
  When Resource Manager / technician sends CMD-MNT-COMPLETE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes COMPLETED
  And EVT-MNT-COMPLETED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MNT-COMPLETE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MNT-COMPLETE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, PLANNED |
    | OUTCOME_REQUIRED | 422 | لم يتحقق الشرط: outcome ∈ {serviceable, failed} |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: outcome, work |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-MNT-PLAN — تخطيط أمر الصيانة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Resource Manager / technician | `POST /api/v1/readiness/maintenance-orders` | POL-MNT-PLAN |

**القصة:** بصفتي **Resource Manager / technician**، أريد **تخطيط أمر الصيانة**، لكي يتحقق غرض أمر الصيانة: أمر صيانة مجدول أو تصحيحي بنافذة زمنية تحجب التوفر

- **الشروط المسبقة:** الحالة الحالية: ∅؛ asset not DISPOSED; kind ∈ {scheduled, corrective}; window; no overlap with another non-terminal order of the asset
- **المدخلات:** `asset`!: urn, `kind`!: enum(scheduled,corrective), `window`!: Interval, `description`!: LocalizedName — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← PLANNED؛ الحدث EVT-MNT-PLANNED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / technician؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MNT-PLAN` · `AGG-MAINTENANCE-ORDER` · متطلبات: REQ-RES-004 · حالات استخدام: UC-051
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MNT-PLAN succeeds
  Given AGG-MAINTENANCE-ORDER does not exist yet and every guard holds
  When Resource Manager / technician sends CMD-MNT-PLAN with a valid payload, a new Idempotency-Key
  Then the state becomes PLANNED
  And EVT-MNT-PLANNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MNT-PLAN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MNT-PLAN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MAINTENANCE_OVERLAP | 422 | لم يتحقق الشرط: no overlap with another non-terminal order of the asset |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: asset, kind, window, description |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-MNT-RESCHEDULE — إعادة جدولة أمر الصيانة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Resource Manager / technician | `POST /api/v1/readiness/maintenance-orders/{id}/actions/reschedule` | POL-MNT-RESCHEDULE |

**القصة:** بصفتي **Resource Manager / technician**، أريد **إعادة جدولة أمر الصيانة**، لكي يتحقق غرض أمر الصيانة: أمر صيانة مجدول أو تصحيحي بنافذة زمنية تحجب التوفر

- **الشروط المسبقة:** الحالة الحالية: PLANNED؛ new window without overlap; affected reservations flagged
- **المدخلات:** `window`!: Interval, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-MNT-RESCHEDULED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / technician؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MNT-RESCHEDULE` · `AGG-MAINTENANCE-ORDER` · متطلبات: REQ-RES-004 · حالات استخدام: UC-051
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MNT-RESCHEDULE succeeds
  Given AGG-MAINTENANCE-ORDER in state PLANNED and every guard holds
  When Resource Manager / technician sends CMD-MNT-RESCHEDULE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-MNT-RESCHEDULED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MNT-RESCHEDULE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MNT-RESCHEDULE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, IN_PROGRESS |
    | MAINTENANCE_OVERLAP | 422 | لم يتحقق الشرط: new window without overlap |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: window, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-MNT-START — بدء أمر الصيانة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager / technician | `POST /api/v1/readiness/maintenance-orders/{id}/actions/start` | POL-MNT-START |

**القصة:** بصفتي **Resource Manager / technician**، أريد **بدء أمر الصيانة**، لكي يتحقق غرض أمر الصيانة: أمر صيانة مجدول أو تصحيحي بنافذة زمنية تحجب التوفر

- **الشروط المسبقة:** الحالة الحالية: PLANNED؛ technician; asset moves to UNDER_MAINTENANCE via its own command (policy)
- **المدخلات:** `technician`!: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← IN_PROGRESS؛ الحدث EVT-MNT-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / technician؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-MNT-START` · `AGG-MAINTENANCE-ORDER` · متطلبات: REQ-RES-004 · حالات استخدام: UC-051
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-MNT-START succeeds
  Given AGG-MAINTENANCE-ORDER in state PLANNED and every guard holds
  When Resource Manager / technician sends CMD-MNT-START with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_PROGRESS
  And EVT-MNT-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-MNT-START is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-MNT-START ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CANCELLED, COMPLETED, IN_PROGRESS |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: technician |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-Q-MNT-SCHEDULE — جلب: Maintenance orders by asset, window, state

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | asset owner scope | `GET /api/v1/readiness/maintenance-orders` | POL-MNT-SCHEDULE |

**القصة:** بصفتي **asset owner scope**، أريد **جلب Maintenance orders by asset, window, state**، لكي يتحقق المتطلب: The system shall schedule and record maintenance for assets, and shall mark an asset under maintenance as unavailable for the maintenance window

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Maintenance orders by asset, window, state؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** asset owner scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-MNT-SCHEDULE` · `AGG-MAINTENANCE-ORDER` · متطلبات: REQ-RES-004
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-MNT-SCHEDULE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-MNT-SCHEDULE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-MNT-SCHEDULE is denied
  Given the policy denies the caller
  When the caller sends QRY-MNT-SCHEDULE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-QUALIFICATION-RECORD — سجل التأهيل (Qualification Record)

`03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md` · SLC-03 · الحالات: ACTIVE, SUSPENDED → EXPIRED, REVOKED

#### US-BC05-QUAL-RECORD — تسجيل سجل التأهيل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Resource Manager / Training Manager | `POST /api/v1/readiness/qualification-records` | POL-QUAL-RECORD |

**القصة:** بصفتي **Resource Manager / Training Manager**، أريد **تسجيل سجل التأهيل**، لكي يتحقق غرض سجل التأهيل: كفاءة أو تأهيل أو شهادة لشخص بفترة صلاحية

- **الشروط المسبقة:** الحالة الحالية: ∅؛ person ACTIVE; code in RD-COMPETENCIES; level valid; valid_from < valid_to; issuer; evidence ref optional
- **المدخلات:** `person`!: urn, `kind`!: enum(competency,qualification,certification), `code`!: string, `level`!: integer, `valid_from`!: date-time, `valid_to`!: date-time, `issuer`!: string, `evidence`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-QUAL-RECORDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / Training Manager؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-QUAL-RECORD` · `AGG-QUALIFICATION-RECORD` · متطلبات: REQ-RDY-001, REQ-RDY-002 · حالات استخدام: UC-102
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-QUAL-RECORD succeeds
  Given AGG-QUALIFICATION-RECORD does not exist yet and every guard holds
  When Resource Manager / Training Manager sends CMD-QUAL-RECORD with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-QUAL-RECORDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-QUAL-RECORD is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-QUAL-RECORD ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | QUALIFICATION_INVALID | 422 | لم يتحقق الشرط: person ACTIVE; code in RD-COMPETENCIES; level valid; valid_from < valid_to; issuer; evidence ref optional |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: person, kind, code, level, valid_from, valid_to, issuer |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-QUAL-REINSTATE — إعادة سجل التأهيل إلى السريان

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager / Training Manager | `POST /api/v1/readiness/qualification-records/{id}/actions/reinstate` | POL-QUAL-REINSTATE |

**القصة:** بصفتي **Resource Manager / Training Manager**، أريد **إعادة سجل التأهيل إلى السريان**، لكي يتحقق غرض سجل التأهيل: كفاءة أو تأهيل أو شهادة لشخص بفترة صلاحية

- **الشروط المسبقة:** الحالة الحالية: SUSPENDED؛ validity not ended
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-QUAL-REINSTATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / Training Manager؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-QUAL-REINSTATE` · `AGG-QUALIFICATION-RECORD` · متطلبات: REQ-RDY-001, REQ-RDY-002 · حالات استخدام: UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-QUAL-REINSTATE succeeds
  Given AGG-QUALIFICATION-RECORD in state SUSPENDED and every guard holds
  When Resource Manager / Training Manager sends CMD-QUAL-REINSTATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-QUAL-REINSTATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-QUAL-REINSTATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-QUAL-REINSTATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | QUALIFICATION_EXPIRED | 422 | لم يتحقق الشرط: validity not ended |
    | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, EXPIRED, REVOKED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-QUAL-RENEW — تجديد سجل التأهيل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Resource Manager / Training Manager | `POST /api/v1/readiness/qualification-records/{id}/actions/renew` | POL-QUAL-RENEW |

**القصة:** بصفتي **Resource Manager / Training Manager**، أريد **تجديد سجل التأهيل**، لكي يتحقق غرض سجل التأهيل: كفاءة أو تأهيل أو شهادة لشخص بفترة صلاحية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ new valid_to > old; evidence; new version
- **المدخلات:** `valid_to`!: date-time, `evidence`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-QUAL-RENEWED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / Training Manager؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-QUAL-RENEW` · `AGG-QUALIFICATION-RECORD` · متطلبات: REQ-RDY-001, REQ-RDY-002 · حالات استخدام: UC-102
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-QUAL-RENEW succeeds
  Given AGG-QUALIFICATION-RECORD in state ACTIVE and every guard holds
  When Resource Manager / Training Manager sends CMD-QUAL-RENEW with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-QUAL-RENEWED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-QUAL-RENEW is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-QUAL-RENEW ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | QUALIFICATION_INVALID | 422 | لم يتحقق الشرط: new valid_to > old; evidence; new version |
    | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, REVOKED, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: valid_to |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-QUAL-REVOKE — سحب سجل التأهيل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Resource Manager / Training Manager | `POST /api/v1/readiness/qualification-records/{id}/actions/revoke` | POL-QUAL-REVOKE |

**القصة:** بصفتي **Resource Manager / Training Manager**، أريد **سحب سجل التأهيل**، لكي يتحقق غرض سجل التأهيل: كفاءة أو تأهيل أو شهادة لشخص بفترة صلاحية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, SUSPENDED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← REVOKED؛ الحدث EVT-QUAL-REVOKED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / Training Manager؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-QUAL-REVOKE` · `AGG-QUALIFICATION-RECORD` · متطلبات: REQ-RDY-001, REQ-RDY-002 · حالات استخدام: UC-102
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-QUAL-REVOKE succeeds
  Given AGG-QUALIFICATION-RECORD in state ACTIVE or SUSPENDED and every guard holds
  When Resource Manager / Training Manager sends CMD-QUAL-REVOKE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes REVOKED
  And EVT-QUAL-REVOKED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-QUAL-REVOKE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-QUAL-REVOKE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, REVOKED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-QUAL-SUSPEND — تعليق سجل التأهيل

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager / Training Manager | `POST /api/v1/readiness/qualification-records/{id}/actions/suspend` | POL-QUAL-SUSPEND |

**القصة:** بصفتي **Resource Manager / Training Manager**، أريد **تعليق سجل التأهيل**، لكي يتحقق غرض سجل التأهيل: كفاءة أو تأهيل أو شهادة لشخص بفترة صلاحية

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SUSPENDED؛ الحدث EVT-QUAL-SUSPENDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager / Training Manager؛ الشروط: tenant match; task visible; org scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-QUAL-SUSPEND` · `AGG-QUALIFICATION-RECORD` · متطلبات: REQ-RDY-001, REQ-RDY-002 · حالات استخدام: UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-QUAL-SUSPEND succeeds
  Given AGG-QUALIFICATION-RECORD in state ACTIVE and every guard holds
  When Resource Manager / Training Manager sends CMD-QUAL-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUSPENDED
  And EVT-QUAL-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-QUAL-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-QUAL-SUSPEND ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: EXPIRED, REVOKED, SUSPENDED |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-S-QUALIFICATION-RECORD-01 — تلقائي: valid_to reached (سجل التأهيل)

| النوع | نوع المحفِّز (تقدير آلي) | الفاعل | من | إلى |
|---|---|---|---|---|
| نظام | زمني | النظام بهوية عبء عمل | ACTIVE, SUSPENDED | EXPIRED |

**القصة:** بصفتي **النظام**، عند «valid_to reached»، أريد نقل **سجل التأهيل** إلى EXPIRED، لكي يتحقق غرض سجل التأهيل: كفاءة أو تأهيل أو شهادة لشخص بفترة صلاحية

- **الشرط:** scheduler (eligibility also checks validity at read time)
- **المخرجات:** الحدث EVT-QUAL-EXPIRED؛ سجل تدقيق بهوية النظام
- **الربط:** `AGG-QUALIFICATION-RECORD` · سيناريو القبول: «system-triggered transition» في ملف قبول الـAggregate (CR-72)
- **ضوابط النوع:** C-SYS

#### US-BC05-Q-QUAL-LIST — جلب: Qualification records as of t

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | Manager/Resource Manager in scope; self | `GET /api/v1/readiness/persons/{person_id}/qualifications` | POL-QUAL-LIST |

**القصة:** بصفتي **Manager/Resource Manager in scope; self**، أريد **جلب Qualification records as of t**، لكي يتحقق المتطلب: The system shall record each person's competencies, qualifications and certifications with their validity periods

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Qualification records as of t؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** Manager/Resource Manager in scope; self؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-QUAL-LIST` · `AGG-QUALIFICATION-RECORD` · متطلبات: REQ-RDY-001
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-QUAL-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-QUAL-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-QUAL-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-QUAL-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-RESOURCE-POOL — مجمع الموارد (Resource Pool)

`03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md` · SLC-09 · الحالات: ACTIVE, SUSPENDED → CLOSED

#### US-BC05-RPL-ADJUST-CAPACITY — تعديل سعة مجمع الموارد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Resource Manager | `POST /api/v1/readiness/resource-pools/{id}/actions/adjust-capacity` | POL-RPL-ADJUST-CAPACITY |

**القصة:** بصفتي **Resource Manager**، أريد **تعديل سعة مجمع الموارد**، لكي يتحقق غرض مجمع الموارد: مجمع موارد قابلة للعد أو القياس بسعة متغيرة زمنياً

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, SUSPENDED؛ new capacity with valid_from; reason; a reduction below committed quantity requires pre-emption decisions first
- **المدخلات:** `capacity`!: number, `valid_from`!: date-time, `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-RPL-CAPACITY-ADJUSTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RPL-ADJUST-CAPACITY` · `AGG-RESOURCE-POOL` · متطلبات: REQ-RES-006 · حالات استخدام: UC-054
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RPL-ADJUST-CAPACITY succeeds
  Given AGG-RESOURCE-POOL in state ACTIVE or SUSPENDED and every guard holds
  When Resource Manager sends CMD-RPL-ADJUST-CAPACITY with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-RPL-CAPACITY-ADJUSTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RPL-ADJUST-CAPACITY is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RPL-ADJUST-CAPACITY ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CAPACITY_BELOW_COMMITMENTS | 422 | لم يتحقق الشرط: new capacity with valid_from; a reduction below committed quantity requires pre-emption decisions first |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RESOURCE_POOL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: capacity, valid_from, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-RPL-CLOSE — إغلاق مجمع الموارد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Resource Manager | `POST /api/v1/readiness/resource-pools/{id}/actions/close` | POL-RPL-CLOSE |

**القصة:** بصفتي **Resource Manager**، أريد **إغلاق مجمع الموارد**، لكي يتحقق غرض مجمع الموارد: مجمع موارد قابلة للعد أو القياس بسعة متغيرة زمنياً

- **الشروط المسبقة:** الحالة الحالية: ACTIVE, SUSPENDED؛ no COMMITTED or PENDING allocations
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CLOSED؛ الحدث EVT-RPL-CLOSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RPL-CLOSE` · `AGG-RESOURCE-POOL` · متطلبات: REQ-RES-006 · حالات استخدام: UC-054
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RPL-CLOSE succeeds
  Given AGG-RESOURCE-POOL in state ACTIVE or SUSPENDED and every guard holds
  When Resource Manager sends CMD-RPL-CLOSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CLOSED
  And EVT-RPL-CLOSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RPL-CLOSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RPL-CLOSE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | POOL_HAS_COMMITMENTS | 422 | لم يتحقق الشرط: no COMMITTED or PENDING allocations |
    | RESOURCE_POOL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-RPL-CREATE — إنشاء مجمع الموارد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Resource Manager | `POST /api/v1/readiness/resource-pools` | POL-RPL-CREATE |

**القصة:** بصفتي **Resource Manager**، أريد **إنشاء مجمع الموارد**، لكي يتحقق غرض مجمع الموارد: مجمع موارد قابلة للعد أو القياس بسعة متغيرة زمنياً

- **الشروط المسبقة:** الحالة الحالية: ∅؛ type in RD-RESOURCE-TYPES; unit (UCUM); org scope; initial capacity; label
- **المدخلات:** `resource_type`!: string, `name`!: LocalizedName, `unit`!: string, `org_scope`!: urn, `capacity`!: number, `label`!: Label — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-RPL-CREATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RPL-CREATE` · `AGG-RESOURCE-POOL` · متطلبات: REQ-RES-006 · حالات استخدام: UC-054
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RPL-CREATE succeeds
  Given AGG-RESOURCE-POOL does not exist yet and every guard holds
  When Resource Manager sends CMD-RPL-CREATE with a valid payload, a new Idempotency-Key
  Then the state becomes ACTIVE
  And EVT-RPL-CREATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RPL-CREATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RPL-CREATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | POOL_INVALID | 422 | لم يتحقق الشرط: type in RD-RESOURCE-TYPES; unit (UCUM); org scope; initial capacity; label |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: resource_type, name, unit, org_scope, capacity, label |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-RPL-RESUME — استئناف مجمع الموارد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager | `POST /api/v1/readiness/resource-pools/{id}/actions/resume` | POL-RPL-RESUME |

**القصة:** بصفتي **Resource Manager**، أريد **استئناف مجمع الموارد**، لكي يتحقق غرض مجمع الموارد: مجمع موارد قابلة للعد أو القياس بسعة متغيرة زمنياً

- **الشروط المسبقة:** الحالة الحالية: SUSPENDED؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-RPL-RESUMED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RPL-RESUME` · `AGG-RESOURCE-POOL` · متطلبات: REQ-RES-006 · حالات استخدام: UC-054
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RPL-RESUME succeeds
  Given AGG-RESOURCE-POOL in state SUSPENDED and every guard holds
  When Resource Manager sends CMD-RPL-RESUME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-RPL-RESUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RPL-RESUME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RPL-RESUME ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | RESOURCE_POOL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, CLOSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-RPL-SUSPEND — تعليق مجمع الموارد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Resource Manager | `POST /api/v1/readiness/resource-pools/{id}/actions/suspend` | POL-RPL-SUSPEND |

**القصة:** بصفتي **Resource Manager**، أريد **تعليق مجمع الموارد**، لكي يتحقق غرض مجمع الموارد: مجمع موارد قابلة للعد أو القياس بسعة متغيرة زمنياً

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason; no new allocations
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← SUSPENDED؛ الحدث EVT-RPL-SUSPENDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Resource Manager؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RPL-SUSPEND` · `AGG-RESOURCE-POOL` · متطلبات: REQ-RES-006 · حالات استخدام: UC-054
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RPL-SUSPEND succeeds
  Given AGG-RESOURCE-POOL in state ACTIVE and every guard holds
  When Resource Manager sends CMD-RPL-SUSPEND with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes SUSPENDED
  And EVT-RPL-SUSPENDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RPL-SUSPEND is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RPL-SUSPEND ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | RESOURCE_POOL_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: CLOSED, SUSPENDED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-Q-POL-TIMELINE — جلب: Capacity, committed and available quantity per hour in a window

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/resource-pools/{pool_id}/timeline` | POL-POL-TIMELINE |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Capacity, committed and available quantity per hour in a window**، لكي يتحقق المتطلب: The system shall manage resource pools with type, quantity, unit, capacity and availability over time

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Capacity, committed and available quantity per hour in a window؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** pool scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-POL-TIMELINE` · `AGG-RESOURCE-POOL` · متطلبات: REQ-RES-006
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-POL-TIMELINE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-POL-TIMELINE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-POL-TIMELINE is denied
  Given the policy denies the caller
  When the caller sends QRY-POL-TIMELINE
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-ROLE-REQUIREMENT — متطلبات الدور (Role Requirement)

`03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md` · SLC-09 · الحالات: DRAFT, ACTIVE → RETIRED

#### US-BC05-RRQ-ACTIVATE — تفعيل متطلبات الدور

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Training Manager / Administrator | `POST /api/v1/readiness/role-requirements/{id}/actions/activate` | POL-RRQ-ACTIVATE |

**القصة:** بصفتي **Training Manager / Administrator**، أريد **تفعيل متطلبات الدور**، لكي يتحقق غرض متطلبات الدور: متطلبات جاهزية دور: كفاءات، مؤهلات، شهادات، تدريب حديث، خبرة

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ approver ≠ author
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-RRQ-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Training Manager / Administrator؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: approver ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-RRQ-ACTIVATE` · `AGG-ROLE-REQUIREMENT` · متطلبات: REQ-RES-013 · حالات استخدام: UC-102
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RRQ-ACTIVATE succeeds
  Given AGG-ROLE-REQUIREMENT in state DRAFT and every guard holds
  When Training Manager / Administrator sends CMD-RRQ-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-RRQ-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RRQ-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RRQ-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-RRQ-DEFINE — تعريف متطلبات الدور

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Training Manager / Administrator | `POST /api/v1/readiness/role-requirements` | POL-RRQ-DEFINE |

**القصة:** بصفتي **Training Manager / Administrator**، أريد **تعريف متطلبات الدور**، لكي يتحقق غرض متطلبات الدور: متطلبات جاهزية دور: كفاءات، مؤهلات، شهادات، تدريب حديث، خبرة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ role exists (BC01); requirements reference RD-COMPETENCIES
- **المدخلات:** `role`!: urn, `requirements`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-RRQ-DEFINED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Training Manager / Administrator؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RRQ-DEFINE` · `AGG-ROLE-REQUIREMENT` · متطلبات: REQ-RES-013 · حالات استخدام: UC-102
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RRQ-DEFINE succeeds
  Given AGG-ROLE-REQUIREMENT does not exist yet and every guard holds
  When Training Manager / Administrator sends CMD-RRQ-DEFINE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-RRQ-DEFINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RRQ-DEFINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RRQ-DEFINE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ROLE_REQUIREMENT_INVALID | 422 | لم يتحقق الشرط: role exists (BC01); requirements reference RD-COMPETENCIES |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: role, requirements |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-RRQ-EDIT — تعديل متطلبات الدور

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Training Manager / Administrator | `POST /api/v1/readiness/role-requirements/{id}/actions/edit` | POL-RRQ-EDIT |

**القصة:** بصفتي **Training Manager / Administrator**، أريد **تعديل متطلبات الدور**، لكي يتحقق غرض متطلبات الدور: متطلبات جاهزية دور: كفاءات، مؤهلات، شهادات، تدريب حديث، خبرة

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE؛ requirements valid; ACTIVE → new version
- **المدخلات:** `requirements`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-RRQ-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Training Manager / Administrator؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RRQ-EDIT` · `AGG-ROLE-REQUIREMENT` · متطلبات: REQ-RES-013 · حالات استخدام: UC-102
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RRQ-EDIT succeeds
  Given AGG-ROLE-REQUIREMENT in state DRAFT or ACTIVE and every guard holds
  When Training Manager / Administrator sends CMD-RRQ-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-RRQ-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RRQ-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RRQ-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | ROLE_REQUIREMENT_INVALID | 422 | لم يتحقق الشرط: requirements valid |
    | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: requirements |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-RRQ-RETIRE — إحالة متطلبات الدور إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Training Manager / Administrator | `POST /api/v1/readiness/role-requirements/{id}/actions/retire` | POL-RRQ-RETIRE |

**القصة:** بصفتي **Training Manager / Administrator**، أريد **إحالة متطلبات الدور إلى التقاعد**، لكي يتحقق غرض متطلبات الدور: متطلبات جاهزية دور: كفاءات، مؤهلات، شهادات، تدريب حديث، خبرة

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-RRQ-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Training Manager / Administrator؛ الشروط: tenant match; object visible; owner/pool scope؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-RRQ-RETIRE` · `AGG-ROLE-REQUIREMENT` · متطلبات: REQ-RES-013 · حالات استخدام: UC-102
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-RRQ-RETIRE succeeds
  Given AGG-ROLE-REQUIREMENT in state ACTIVE and every guard holds
  When Training Manager / Administrator sends CMD-RRQ-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-RRQ-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-RRQ-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-RRQ-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DRAFT, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

### AGG-SCENARIO — سيناريو التدريب (Scenario)

`03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md` · SLC-19 · الحالات: DRAFT, ACTIVE → RETIRED

#### US-BC05-SCN-ACTIVATE — تفعيل سيناريو التدريب

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Exercise Director | `POST /api/v1/readiness/scenarios/{id}/actions/activate` | POL-SCN-ACTIVATE |

**القصة:** بصفتي **Exercise Director**، أريد **تفعيل سيناريو التدريب**، لكي يتحقق غرض سيناريو التدريب: تعريف قابل لإعادة الاستخدام لتمرين تدريبي: موقف، أهداف، كفاءات مستهدفة، وحقن مرتبة زمنياً

- **الشروط المسبقة:** الحالة الحالية: DRAFT؛ approver ≠ author
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ACTIVE؛ الحدث EVT-SCN-ACTIVATED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Director؛ الشروط: tenant match; approver ≠ author (INV-SCN via segregation of duties)؛ فصل المهام: approver ≠ author؛ الالتزامات: audit
- **الربط:** `CMD-SCN-ACTIVATE` · `AGG-SCENARIO` · متطلبات: REQ-TRX-001, REQ-TRX-002 · حالات استخدام: UC-160
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SCN-ACTIVATE succeeds
  Given AGG-SCENARIO in state DRAFT and every guard holds
  When Exercise Director sends CMD-SCN-ACTIVATE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ACTIVE
  And EVT-SCN-ACTIVATED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SCN-ACTIVATE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SCN-ACTIVATE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SCENARIO_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ACTIVE, RETIRED |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: approver ≠ author |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SCN-DEFINE — تعريف سيناريو التدريب

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | Training Manager | `POST /api/v1/readiness/scenarios` | POL-SCN-DEFINE |

**القصة:** بصفتي **Training Manager**، أريد **تعريف سيناريو التدريب**، لكي يتحقق غرض سيناريو التدريب: تعريف قابل لإعادة الاستخدام لتمرين تدريبي: موقف، أهداف، كفاءات مستهدفة، وحقن مرتبة زمنياً

- **الشروط المسبقة:** الحالة الحالية: ∅؛ title; exercise_type_ref in RD-EXERCISE-TYPES; situation; target_competencies ⊆ RD-COMPETENCIES; injects ordered by strictly increasing offset (INV-SCN-01)
- **المدخلات:** `title`!: LocalizedName, `exercise_type_ref`!: urn, `situation`!: string, `target_competencies`!: array, `injects`!: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← DRAFT؛ الحدث EVT-SCN-DEFINED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Training Manager؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SCN-DEFINE` · `AGG-SCENARIO` · متطلبات: REQ-TRX-001, REQ-TRX-002 · حالات استخدام: UC-160
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SCN-DEFINE succeeds
  Given AGG-SCENARIO does not exist yet and every guard holds
  When Training Manager sends CMD-SCN-DEFINE with a valid payload, a new Idempotency-Key
  Then the state becomes DRAFT
  And EVT-SCN-DEFINED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SCN-DEFINE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SCN-DEFINE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SCENARIO_INVALID | 422 | لم يتحقق الشرط: title; exercise_type_ref in RD-EXERCISE-TYPES; situation; target_competencies ⊆ RD-COMPETENCIES; injects ordered by strictly increasing offset (INV-SCN-01) |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: title, exercise_type_ref, situation, target_competencies, injects |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SCN-EDIT — تعديل سيناريو التدريب

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Training Manager | `POST /api/v1/readiness/scenarios/{id}/actions/edit` | POL-SCN-EDIT |

**القصة:** بصفتي **Training Manager**، أريد **تعديل سيناريو التدريب**، لكي يتحقق غرض سيناريو التدريب: تعريف قابل لإعادة الاستخدام لتمرين تدريبي: موقف، أهداف، كفاءات مستهدفة، وحقن مرتبة زمنياً

- **الشروط المسبقة:** الحالة الحالية: DRAFT, ACTIVE؛ same validations as DEFINE; editing an ACTIVE scenario creates a new version — exercises already planned against the prior version keep their frozen reference (INV-EXR-01)
- **المدخلات:** `title`: LocalizedName, `situation`: string, `target_competencies`: array, `injects`: array — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SCN-EDITED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Training Manager؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SCN-EDIT` · `AGG-SCENARIO` · متطلبات: REQ-TRX-001, REQ-TRX-002 · حالات استخدام: UC-160
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SCN-EDIT succeeds
  Given AGG-SCENARIO in state DRAFT or ACTIVE and every guard holds
  When Training Manager sends CMD-SCN-EDIT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SCN-EDITED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SCN-EDIT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SCN-EDIT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SCENARIO_INVALID | 422 | لم يتحقق الشرط: editing an ACTIVE scenario creates a new version — exercises already planned against the prior version keep their frozen reference (INV-EXR-01) |
    | SCENARIO_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SCN-RETIRE — إحالة سيناريو التدريب إلى التقاعد

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Exercise Director | `POST /api/v1/readiness/scenarios/{id}/actions/retire` | POL-SCN-RETIRE |

**القصة:** بصفتي **Exercise Director**، أريد **إحالة سيناريو التدريب إلى التقاعد**، لكي يتحقق غرض سيناريو التدريب: تعريف قابل لإعادة الاستخدام لتمرين تدريبي: موقف، أهداف، كفاءات مستهدفة، وحقن مرتبة زمنياً

- **الشروط المسبقة:** الحالة الحالية: ACTIVE؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← RETIRED؛ الحدث EVT-SCN-RETIRED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Director؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SCN-RETIRE` · `AGG-SCENARIO` · متطلبات: REQ-TRX-001, REQ-TRX-002 · حالات استخدام: UC-160
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SCN-RETIRE succeeds
  Given AGG-SCENARIO in state ACTIVE and every guard holds
  When Exercise Director sends CMD-SCN-RETIRE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes RETIRED
  And EVT-SCN-RETIRED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SCN-RETIRE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SCN-RETIRE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SCENARIO_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: DRAFT, RETIRED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-Q-SCN-GET — جلب: Scenario with injects and target competencies

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/scenarios/{scenario_id}` | POL-SCN-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Scenario with injects and target competencies**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted to the caller's visible scope

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Scenario with injects and target competencies
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SCN-GET` · `AGG-SCENARIO` · متطلبات: REQ-TRX-014
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SCN-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-SCN-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-SCN-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-SCN-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC05-Q-SCN-LIST — جلب: Scenarios filtered by exercise type, state

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/scenarios` | POL-SCN-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Scenarios filtered by exercise type, state**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted to the caller's visible scope

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Scenarios filtered by exercise type, state؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SCN-LIST` · `AGG-SCENARIO` · متطلبات: REQ-TRX-014
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SCN-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SCN-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SCN-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-SCN-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-SHIPMENT — الشحنة (Shipment)

`03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md` · SLC-18 · الحالات: PLANNED, IN_TRANSIT → DELIVERED, DAMAGED, LOST, CANCELLED

#### US-BC05-SHP-CANCEL — إلغاء الشحنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | dispatcher | `POST /api/v1/readiness/shipments/{id}/actions/cancel` | POL-SHP-CANCEL |

**القصة:** بصفتي **dispatcher**، أريد **إلغاء الشحنة**، لكي يتحقق غرض الشحنة: نقل كمية من صنف إمداد من موقع تخزين إلى وجهة تلبيةً لطلب إمداد، بتتبع نقاط حركة

- **الشروط المسبقة:** الحالة الحالية: PLANNED؛ reason; only before departure
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← CANCELLED؛ الحدث EVT-SHP-CANCELLED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** dispatcher؛ الشروط: tenant match; only before departure (INV-SHP-04)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SHP-CANCEL` · `AGG-SHIPMENT` · متطلبات: REQ-LOG-004, REQ-LOG-005, REQ-LOG-006, REQ-LOG-007, REQ-LOG-009 · حالات استخدام: UC-151, UC-152
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SHP-CANCEL succeeds
  Given AGG-SHIPMENT in state PLANNED and every guard holds
  When dispatcher sends CMD-SHP-CANCEL with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes CANCELLED
  And EVT-SHP-CANCELLED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SHP-CANCEL is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SHP-CANCEL ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SHIPMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: IN_TRANSIT, DELIVERED, DAMAGED, LOST, CANCELLED — الحالات النهائية DELIVERED, DAMAGED, LOST, CANCELLED بلا صف في المصفوفة، وأُضيفت لأن الحالة النهائية لا تقبل أوامر **[Derived]** |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SHP-DELIVER — تسليم الشحنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | receiving party | `POST /api/v1/readiness/shipments/{id}/actions/deliver` | POL-SHP-DELIVER |

**القصة:** بصفتي **receiving party**، أريد **تسليم الشحنة**، لكي يتحقق غرض الشحنة: نقل كمية من صنف إمداد من موقع تخزين إلى وجهة تلبيةً لطلب إمداد، بتتبع نقاط حركة

- **الشروط المسبقة:** الحالة الحالية: IN_TRANSIT؛ receiving party confirms; delivered_quantity ≤ planned quantity; a shortfall is recorded, never hidden (INV-SHP-02)
- **المدخلات:** `delivered_quantity`!: number, `received_by`!: urn, `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DELIVERED؛ الحدث EVT-SHP-DELIVERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** receiving party؛ الشروط: tenant match; delivered_quantity ≤ planned quantity (INV-SHP-02)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SHP-DELIVER` · `AGG-SHIPMENT` · متطلبات: REQ-LOG-004, REQ-LOG-005, REQ-LOG-006, REQ-LOG-007, REQ-LOG-009 · حالات استخدام: UC-151, UC-152
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SHP-DELIVER succeeds
  Given AGG-SHIPMENT in state IN_TRANSIT and every guard holds
  When receiving party sends CMD-SHP-DELIVER with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DELIVERED
  And EVT-SHP-DELIVERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SHP-DELIVER is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SHP-DELIVER ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | DELIVERY_INVALID | 422 | لم يتحقق الشرط: delivered_quantity ≤ planned quantity |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SHIPMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: PLANNED, DELIVERED, DAMAGED, LOST, CANCELLED — الحالات النهائية DELIVERED, DAMAGED, LOST, CANCELLED بلا صف في المصفوفة، وأُضيفت لأن الحالة النهائية لا تقبل أوامر **[Derived]** |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: delivered_quantity, received_by |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SHP-DEPART — بدء نقل الشحنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | carrier operator · dispatcher | `POST /api/v1/readiness/shipments/{id}/actions/depart` | POL-SHP-DEPART |

**القصة:** بصفتي **carrier operator · dispatcher**، أريد **بدء نقل الشحنة**، لكي يتحقق غرض الشحنة: نقل كمية من صنف إمداد من موقع تخزين إلى وجهة تلبيةً لطلب إمداد، بتتبع نقاط حركة

- **الشروط المسبقة:** الحالة الحالية: PLANNED؛ carrier confirmed; departure checkpoint recorded
- **المدخلات:** `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← IN_TRANSIT؛ الحدث EVT-SHP-DEPARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** carrier operator · dispatcher؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SHP-DEPART` · `AGG-SHIPMENT` · متطلبات: REQ-LOG-004, REQ-LOG-005, REQ-LOG-006, REQ-LOG-007, REQ-LOG-009 · حالات استخدام: UC-151, UC-152
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SHP-DEPART succeeds
  Given AGG-SHIPMENT in state PLANNED and every guard holds
  When an authorized actor (carrier operator or dispatcher) sends CMD-SHP-DEPART with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_TRANSIT
  And EVT-SHP-DEPARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SHP-DEPART is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SHP-DEPART ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | DEPARTURE_INVALID | 422 | لم يتحقق الشرط: departure checkpoint recorded |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SHIPMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: IN_TRANSIT, DELIVERED, DAMAGED, LOST, CANCELLED — الحالات النهائية DELIVERED, DAMAGED, LOST, CANCELLED بلا صف في المصفوفة، وأُضيفت لأن الحالة النهائية لا تقبل أوامر **[Derived]** |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SHP-PLAN — تخطيط الشحنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| إنشاء | أساسية | dispatcher | `POST /api/v1/readiness/shipments` | POL-SHP-PLAN |

**القصة:** بصفتي **dispatcher**، أريد **تخطيط الشحنة**، لكي يتحقق غرض الشحنة: نقل كمية من صنف إمداد من موقع تخزين إلى وجهة تلبيةً لطلب إمداد، بتتبع نقاط حركة

- **الشروط المسبقة:** الحالة الحالية: ∅؛ logistics_request APPROVED; origin pool with sufficient COMMITTED allocation quantity for the linked request; destination; carrier; planned_quantity ≤ the linked allocation's committed quantity
- **المدخلات:** `logistics_request`!: urn, `origin_pool`!: urn, `destination`!: LocalizedName, `carrier`!: string, `planned_quantity`!: number — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← PLANNED؛ الحدث EVT-SHP-PLANNED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** dispatcher؛ الشروط: tenant match; origin pool scope visible to actor; linked logistics request APPROVED؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SHP-PLAN` · `AGG-SHIPMENT` · متطلبات: REQ-LOG-004, REQ-LOG-005, REQ-LOG-006, REQ-LOG-007, REQ-LOG-009 · حالات استخدام: UC-151, UC-152
- **ضوابط النوع والفئة:** C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SHP-PLAN succeeds
  Given AGG-SHIPMENT does not exist yet and every guard holds
  When dispatcher sends CMD-SHP-PLAN with a valid payload, a new Idempotency-Key
  Then the state becomes PLANNED
  And EVT-SHP-PLANNED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SHP-PLAN is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SHP-PLAN ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SHIPMENT_INVALID | 422 | لم يتحقق الشرط: logistics_request APPROVED; origin pool with sufficient COMMITTED allocation quantity for the linked request; destination; carrier; planned_quantity ≤ the linked allocation's committed quantity |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: logistics_request, origin_pool, destination, carrier, planned_quantity |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SHP-RECORD-CHECKPOINT — تسجيل نقطة عبور لـالشحنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | carrier operator · dispatcher | `POST /api/v1/readiness/shipments/{id}/actions/record-checkpoint` | POL-SHP-RECORD-CHECKPOINT |

**القصة:** بصفتي **carrier operator · dispatcher**، أريد **تسجيل نقطة عبور لـالشحنة**، لكي يتحقق غرض الشحنة: نقل كمية من صنف إمداد من موقع تخزين إلى وجهة تلبيةً لطلب إمداد، بتتبع نقاط حركة

- **الشروط المسبقة:** الحالة الحالية: IN_TRANSIT؛ checkpoint strictly after the previous checkpoint in time (append-only, gapless — mirrors INV-AST-02); location; at; note
- **المدخلات:** `location`!: LocalizedName, `at`!: date-time, `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SHP-CHECKPOINT-RECORDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** carrier operator · dispatcher؛ الشروط: tenant match; checkpoint strictly after the previous one (INV-SHP-01)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SHP-RECORD-CHECKPOINT` · `AGG-SHIPMENT` · متطلبات: REQ-LOG-004, REQ-LOG-005, REQ-LOG-006, REQ-LOG-007, REQ-LOG-009 · حالات استخدام: UC-151, UC-152
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SHP-RECORD-CHECKPOINT succeeds
  Given AGG-SHIPMENT in state IN_TRANSIT and every guard holds
  When an authorized actor (carrier operator or dispatcher) sends CMD-SHP-RECORD-CHECKPOINT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SHP-CHECKPOINT-RECORDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SHP-RECORD-CHECKPOINT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SHP-RECORD-CHECKPOINT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | CHECKPOINT_INVALID | 422 | لم يتحقق الشرط: checkpoint strictly after the previous checkpoint in time (append-only, gapless — mirrors INV-AST-02) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SHIPMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: PLANNED, DELIVERED, DAMAGED, LOST, CANCELLED — الحالات النهائية DELIVERED, DAMAGED, LOST, CANCELLED بلا صف في المصفوفة، وأُضيفت لأن الحالة النهائية لا تقبل أوامر **[Derived]** |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: location, at |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SHP-REPORT-DAMAGE — الإبلاغ عن تلف الشحنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | carrier operator · dispatcher | `POST /api/v1/readiness/shipments/{id}/actions/report-damage` | POL-SHP-REPORT-DAMAGE |

**القصة:** بصفتي **carrier operator · dispatcher**، أريد **الإبلاغ عن تلف الشحنة**، لكي يتحقق غرض الشحنة: نقل كمية من صنف إمداد من موقع تخزين إلى وجهة تلبيةً لطلب إمداد، بتتبع نقاط حركة

- **الشروط المسبقة:** الحالة الحالية: IN_TRANSIT؛ reason; damaged_quantity ≤ planned quantity; evidence
- **المدخلات:** `damaged_quantity`!: number, `reason`!: string, `evidence`: urn — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← DAMAGED؛ الحدث EVT-SHP-DAMAGED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** carrier operator · dispatcher؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SHP-REPORT-DAMAGE` · `AGG-SHIPMENT` · متطلبات: REQ-LOG-004, REQ-LOG-005, REQ-LOG-006, REQ-LOG-007, REQ-LOG-009 · حالات استخدام: UC-151, UC-152
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SHP-REPORT-DAMAGE succeeds
  Given AGG-SHIPMENT in state IN_TRANSIT and every guard holds
  When an authorized actor (carrier operator or dispatcher) sends CMD-SHP-REPORT-DAMAGE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes DAMAGED
  And EVT-SHP-DAMAGED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SHP-REPORT-DAMAGE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SHP-REPORT-DAMAGE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SHIPMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: PLANNED, DELIVERED, DAMAGED, LOST, CANCELLED — الحالات النهائية DELIVERED, DAMAGED, LOST, CANCELLED بلا صف في المصفوفة، وأُضيفت لأن الحالة النهائية لا تقبل أوامر **[Derived]** |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: damaged_quantity, reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SHP-REPORT-LOST — الإبلاغ عن فقد الشحنة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | carrier operator · dispatcher | `POST /api/v1/readiness/shipments/{id}/actions/report-lost` | POL-SHP-REPORT-LOST |

**القصة:** بصفتي **carrier operator · dispatcher**، أريد **الإبلاغ عن فقد الشحنة**، لكي يتحقق غرض الشحنة: نقل كمية من صنف إمداد من موقع تخزين إلى وجهة تلبيةً لطلب إمداد، بتتبع نقاط حركة

- **الشروط المسبقة:** الحالة الحالية: IN_TRANSIT؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← LOST؛ الحدث EVT-SHP-LOST؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** carrier operator · dispatcher؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SHP-REPORT-LOST` · `AGG-SHIPMENT` · متطلبات: REQ-LOG-004, REQ-LOG-005, REQ-LOG-006, REQ-LOG-007, REQ-LOG-009 · حالات استخدام: UC-151, UC-152
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SHP-REPORT-LOST succeeds
  Given AGG-SHIPMENT in state IN_TRANSIT and every guard holds
  When an authorized actor (carrier operator or dispatcher) sends CMD-SHP-REPORT-LOST with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes LOST
  And EVT-SHP-LOST is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SHP-REPORT-LOST is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SHP-REPORT-LOST ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SHIPMENT_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: PLANNED, DELIVERED, DAMAGED, LOST, CANCELLED — الحالات النهائية DELIVERED, DAMAGED, LOST, CANCELLED بلا صف في المصفوفة، وأُضيفت لأن الحالة النهائية لا تقبل أوامر **[Derived]** |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-Q-SHP-GET — جلب: Shipment with current state and delivered/damaged/lost quantity

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/shipments/{shipment_id}` | POL-SHP-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Shipment with current state and delivered/damaged/lost quantity**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter shipments by logistics request, carrier, state and window, restricted to the caller's visible scope

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Shipment with current state and delivered/damaged/lost quantity
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SHP-GET` · `AGG-SHIPMENT` · متطلبات: REQ-LOG-011
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SHP-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-SHP-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-SHP-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-SHP-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC05-Q-SHP-LIST — جلب: Shipments filtered by logistics request, carrier, state, window

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/shipments` | POL-SHP-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Shipments filtered by logistics request, carrier, state, window**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter shipments by logistics request, carrier, state and window, restricted to the caller's visible scope

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Shipments filtered by logistics request, carrier, state, window؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SHP-LIST` · `AGG-SHIPMENT` · متطلبات: REQ-LOG-011
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SHP-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SHP-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SHP-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-SHP-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC05-Q-SHP-TRACKING — جلب: Full checkpoint history of a shipment, in order

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/shipments/{shipment_id}/checkpoints` | POL-SHP-TRACKING |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Full checkpoint history of a shipment, in order**، لكي يتحقق المتطلب: The system shall provide the full, ordered checkpoint history of a shipment to an authorized actor

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Full checkpoint history of a shipment, in order؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SHP-TRACKING` · `AGG-SHIPMENT` · متطلبات: REQ-LOG-012
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SHP-TRACKING returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SHP-TRACKING with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SHP-TRACKING is denied
  Given the policy denies the caller
  When the caller sends QRY-SHP-TRACKING
  Then the response has the same shape as for a missing item (not-found shape)
```

### AGG-SIMULATION — تشغيل المحاكاة (Simulation)

`03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md` · SLC-19 · الحالات: IN_PROGRESS, PAUSED → COMPLETED, ABORTED

#### US-BC05-SIM-ABORT — إيقاف تشغيل المحاكاة نهائيًا مع السبب

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Exercise Controller | `POST /api/v1/readiness/simulations/{id}/actions/abort` | POL-SIM-ABORT |

**القصة:** بصفتي **Exercise Controller**، أريد **إيقاف تشغيل المحاكاة نهائيًا مع السبب**، لكي يتحقق غرض تشغيل المحاكاة: تنفيذ فعلي واحد لتمرين: تسليم الحقن، تسجيل التقييمات، والانتهاء إلى نتيجة نهائية

- **الشروط المسبقة:** الحالة الحالية: IN_PROGRESS, PAUSED؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← ABORTED؛ الحدث EVT-SIM-ABORTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Controller؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIM-ABORT` · `AGG-SIMULATION` · متطلبات: REQ-TRX-008, REQ-TRX-009, REQ-TRX-010, REQ-TRX-011 · حالات استخدام: UC-162
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIM-ABORT succeeds
  Given AGG-SIMULATION in state IN_PROGRESS or PAUSED and every guard holds
  When Exercise Controller sends CMD-SIM-ABORT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes ABORTED
  And EVT-SIM-ABORTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIM-ABORT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIM-ABORT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SIMULATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ABORTED, COMPLETED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SIM-COMPLETE — إكمال تشغيل المحاكاة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| حذف / إنهاء | أساسية | Exercise Controller | `POST /api/v1/readiness/simulations/{id}/actions/complete` | POL-SIM-COMPLETE |

**القصة:** بصفتي **Exercise Controller**، أريد **إكمال تشغيل المحاكاة**، لكي يتحقق غرض تشغيل المحاكاة: تنفيذ فعلي واحد لتمرين: تسليم الحقن، تسجيل التقييمات، والانتهاء إلى نتيجة نهائية

- **الشروط المسبقة:** الحالة الحالية: IN_PROGRESS, PAUSED؛ every participant on the linked exercise has ≥ 1 recorded evaluation (INV-SIM-02)
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← COMPLETED؛ الحدث EVT-SIM-COMPLETED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Controller؛ الشروط: tenant match; every participant evaluated (INV-SIM-02)؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIM-COMPLETE` · `AGG-SIMULATION` · متطلبات: REQ-TRX-008, REQ-TRX-009, REQ-TRX-010, REQ-TRX-011 · حالات استخدام: UC-162
- **ضوابط النوع والفئة:** C-DEL، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIM-COMPLETE succeeds
  Given AGG-SIMULATION in state IN_PROGRESS or PAUSED and every guard holds
  When Exercise Controller sends CMD-SIM-COMPLETE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes COMPLETED
  And EVT-SIM-COMPLETED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIM-COMPLETE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIM-COMPLETE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | EVALUATION_MISSING | 422 | لم يتحقق الشرط: every participant on the linked exercise has ≥ 1 recorded evaluation (INV-SIM-02) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SIMULATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ABORTED, COMPLETED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SIM-DELIVER-INJECT — تسليم حقنة سيناريو ضمن تشغيل المحاكاة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Exercise Controller | `POST /api/v1/readiness/simulations/{id}/actions/deliver-inject` | POL-SIM-DELIVER-INJECT |

**القصة:** بصفتي **Exercise Controller**، أريد **تسليم حقنة سيناريو ضمن تشغيل المحاكاة**، لكي يتحقق غرض تشغيل المحاكاة: تنفيذ فعلي واحد لتمرين: تسليم الحقن، تسجيل التقييمات، والانتهاء إلى نتيجة نهائية

- **الشروط المسبقة:** الحالة الحالية: IN_PROGRESS؛ inject_ref belongs to the linked scenario; delivered_at strictly after the previous delivery (INV-SIM-01)
- **المدخلات:** `inject_ref`!: urn, `delivered_at`!: date-time, `note`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SIM-INJECT-DELIVERED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Controller؛ الشروط: tenant match; inject_ref belongs to the linked scenario؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIM-DELIVER-INJECT` · `AGG-SIMULATION` · متطلبات: REQ-TRX-008, REQ-TRX-009, REQ-TRX-010, REQ-TRX-011 · حالات استخدام: UC-162
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIM-DELIVER-INJECT succeeds
  Given AGG-SIMULATION in state IN_PROGRESS and every guard holds
  When Exercise Controller sends CMD-SIM-DELIVER-INJECT with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SIM-INJECT-DELIVERED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIM-DELIVER-INJECT is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIM-DELIVER-INJECT ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | INJECT_INVALID | 422 | لم يتحقق الشرط: inject_ref belongs to the linked scenario |
    | SIMULATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ABORTED, COMPLETED, PAUSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: inject_ref, delivered_at |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SIM-PAUSE — إيقاف تشغيل المحاكاة مؤقتًا

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Exercise Controller | `POST /api/v1/readiness/simulations/{id}/actions/pause` | POL-SIM-PAUSE |

**القصة:** بصفتي **Exercise Controller**، أريد **إيقاف تشغيل المحاكاة مؤقتًا**، لكي يتحقق غرض تشغيل المحاكاة: تنفيذ فعلي واحد لتمرين: تسليم الحقن، تسجيل التقييمات، والانتهاء إلى نتيجة نهائية

- **الشروط المسبقة:** الحالة الحالية: IN_PROGRESS؛ reason
- **المدخلات:** `reason`!: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← PAUSED؛ الحدث EVT-SIM-PAUSED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Controller؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIM-PAUSE` · `AGG-SIMULATION` · متطلبات: REQ-TRX-008, REQ-TRX-009, REQ-TRX-010, REQ-TRX-011 · حالات استخدام: UC-162
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIM-PAUSE succeeds
  Given AGG-SIMULATION in state IN_PROGRESS and every guard holds
  When Exercise Controller sends CMD-SIM-PAUSE with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes PAUSED
  And EVT-SIM-PAUSED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIM-PAUSE is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIM-PAUSE ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | REASON_REQUIRED | 422 | لم يُذكر السبب |
    | SIMULATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ABORTED, COMPLETED, PAUSED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: reason |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SIM-RECORD-EVALUATION — تسجيل تقييم ضمن تشغيل المحاكاة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| تعديل | أساسية | Evaluator | `POST /api/v1/readiness/simulations/{id}/actions/record-evaluation` | POL-SIM-RECORD-EVALUATION |

**القصة:** بصفتي **Evaluator**، أريد **تسجيل تقييم ضمن تشغيل المحاكاة**، لكي يتحقق غرض تشغيل المحاكاة: تنفيذ فعلي واحد لتمرين: تسليم الحقن، تسجيل التقييمات، والانتهاء إلى نتيجة نهائية

- **الشروط المسبقة:** الحالة الحالية: IN_PROGRESS, PAUSED؛ participant_ref is one of the linked exercise's participants; competency_code in RD-COMPETENCIES; result ∈ {MET, PARTIAL, NOT_MET}; evaluator ≠ participant (INV-SIM-03)
- **المدخلات:** `participant`!: urn, `competency_code`!: string, `result`!: enum(MET,PARTIAL,NOT_MET), `notes`: string — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← (بلا تغيير)؛ الحدث EVT-SIM-EVALUATION-RECORDED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Evaluator؛ الشروط: tenant match; evaluator ≠ participant (INV-SIM-03)؛ فصل المهام: evaluator ≠ participant؛ الالتزامات: audit
- **الربط:** `CMD-SIM-RECORD-EVALUATION` · `AGG-SIMULATION` · متطلبات: REQ-TRX-008, REQ-TRX-009, REQ-TRX-010, REQ-TRX-011 · حالات استخدام: UC-162
- **ضوابط النوع والفئة:** C-UPD، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIM-RECORD-EVALUATION succeeds
  Given AGG-SIMULATION in state IN_PROGRESS or PAUSED and every guard holds
  When Evaluator sends CMD-SIM-RECORD-EVALUATION with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state is unchanged and the version increases by one
  And EVT-SIM-EVALUATION-RECORDED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIM-RECORD-EVALUATION is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIM-RECORD-EVALUATION ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SEGREGATION_OF_DUTIES | 422 | فصل المهام: evaluator ≠ participant |
    | SIMULATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ABORTED, COMPLETED |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: participant, competency_code, result |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SIM-RESUME — استئناف تشغيل المحاكاة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| سير عمل | أساسية | Exercise Controller | `POST /api/v1/readiness/simulations/{id}/actions/resume` | POL-SIM-RESUME |

**القصة:** بصفتي **Exercise Controller**، أريد **استئناف تشغيل المحاكاة**، لكي يتحقق غرض تشغيل المحاكاة: تنفيذ فعلي واحد لتمرين: تسليم الحقن، تسجيل التقييمات، والانتهاء إلى نتيجة نهائية

- **الشروط المسبقة:** الحالة الحالية: PAUSED؛ لا شروط إضافية
- **المدخلات:** لا حمولة — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose` و`If-Match`
- **المخرجات:** الحالة ← IN_PROGRESS؛ الحدث EVT-SIM-RESUMED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** Exercise Controller؛ الشروط: tenant match؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIM-RESUME` · `AGG-SIMULATION` · متطلبات: REQ-TRX-008, REQ-TRX-009, REQ-TRX-010, REQ-TRX-011 · حالات استخدام: UC-162
- **ضوابط النوع والفئة:** C-WF، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIM-RESUME succeeds
  Given AGG-SIMULATION in state PAUSED and every guard holds
  When Exercise Controller sends CMD-SIM-RESUME with a valid payload, a new Idempotency-Key and a matching If-Match
  Then the state becomes IN_PROGRESS
  And EVT-SIM-RESUMED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIM-RESUME is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIM-RESUME ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SIMULATION_INVALID_STATE_TRANSITION | 409 | الحالة الحالية واحدة من: ABORTED, COMPLETED, IN_PROGRESS |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-SIM-START — بدء تشغيل المحاكاة

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| نظام | أساسية | system | `POST /api/v1/readiness/simulations` | POL-SIM-START |

**القصة:** بصفتي **system**، أريد **بدء تشغيل المحاكاة**، لكي يتحقق غرض تشغيل المحاكاة: تنفيذ فعلي واحد لتمرين: تسليم الحقن، تسجيل التقييمات، والانتهاء إلى نتيجة نهائية

- **الشروط المسبقة:** الحالة الحالية: ∅؛ system-issued in the same unit of work as CMD-EXR-START; exercise_ref SCHEDULED transitioning to IN_PROGRESS; scenario_ref = the exercise's frozen scenario; started_at
- **المدخلات:** `exercise`!: urn, `scenario`!: urn, `started_at`!: date-time — `!` = إلزامي؛ مع `Idempotency-Key` و`X-Purpose`
- **المخرجات:** الحالة ← IN_PROGRESS؛ الحدث EVT-SIM-STARTED؛ الاستجابة `ResourceRef` (urn، id، version، state)
- **الصلاحية:** system (workload identity)؛ الشروط: tenant match; invoked only within CMD-EXR-START's unit of work؛ فصل المهام: —؛ الالتزامات: audit
- **الربط:** `CMD-SIM-START` · `AGG-SIMULATION` · متطلبات: REQ-TRX-008, REQ-TRX-009, REQ-TRX-010, REQ-TRX-011 · حالات استخدام: UC-162
- **ضوابط النوع والفئة:** C-SYS، C-CRE، K-CORE (التعريف في [00-guide.md](00-guide.md))

```gherkin
Scenario: CMD-SIM-START succeeds
  Given AGG-SIMULATION does not exist yet and every guard holds
  When system sends CMD-SIM-START with a valid payload, a new Idempotency-Key
  Then the state becomes IN_PROGRESS
  And EVT-SIM-STARTED is written to the outbox with one audit record in the same transaction

Scenario Outline: CMD-SIM-START is rejected
  When the command is sent while <condition>
  Then it is rejected with <code> (HTTP <http>) and nothing changes

  Examples:
    | code | http | condition |
    | AUTHZ_DENIED | 403→404 | السياسة POL-SIM-START ترفض: يُعاد 404 بنفس شكل المورد غير الموجود، و403 فقط إن كان المورد مرئيًا له دون الإذن بالإجراء (`errors-*.md`) |
    | IDEMPOTENCY_KEY_REUSED | 422 | نفس Idempotency-Key مع حمولة مختلفة |
    | SIMULATION_INVALID | 422 | لم يتحقق الشرط: system-issued in the same unit of work as CMD-EXR-START; exercise_ref SCHEDULED transitioning to IN_PROGRESS; scenario_ref = the exercise's frozen scenario; started_at |
    | VALIDATION_FAILED | 400 | حقل إلزامي مفقود أو غير صالح: exercise, scenario, started_at |
    | VERSION_CONFLICT | 409 | قيمة If-Match لا تطابق الإصدار الحالي (يُفحص بعد التخويل الكامل؛ يُعاد بعد تحميل المورد) |
```

#### US-BC05-Q-SIM-GET — جلب: Simulation with current state and evaluation summary

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/simulations/{simulation_id}` | POL-SIM-GET |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Simulation with current state and evaluation summary**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted to the caller's visible scope

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** Simulation with current state and evaluation summary
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SIM-GET` · `AGG-SIMULATION` · متطلبات: REQ-TRX-014
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SIM-GET returns a visible item
  Given the item exists and the policy allows the caller
  When the caller sends QRY-SIM-GET
  Then the item is returned after the result re-check (security_version, LabelCheck)

Scenario: QRY-SIM-GET hides an item the caller may not see
  Given the item exists but the policy denies the caller
  When the caller sends QRY-SIM-GET
  Then the response is 404 with the same shape as for a missing item
```

#### US-BC05-Q-SIM-LIST — جلب: Simulations filtered by exercise, state, window

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/simulations` | POL-SIM-LIST |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Simulations filtered by exercise, state, window**، لكي يتحقق المتطلب: The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted to the caller's visible scope

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Simulations filtered by exercise, state, window؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SIM-LIST` · `AGG-SIMULATION` · متطلبات: REQ-TRX-014
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SIM-LIST returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SIM-LIST with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SIM-LIST is denied
  Given the policy denies the caller
  When the caller sends QRY-SIM-LIST
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC05-Q-SIM-TIMELINE — جلب: Full, ordered timeline of inject deliveries and evaluations for a simulation

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | مستخدم مخوَّل (ضمن allowed_scope) | `GET /api/v1/readiness/simulations/{simulation_id}/timeline` | POL-SIM-TIMELINE |

**القصة:** بصفتي **مستخدم مخوَّل (ضمن allowed_scope)**، أريد **جلب Full, ordered timeline of inject deliveries and evaluations for a simulation**، لكي يتحقق المتطلب: The system shall provide the full, ordered timeline of inject deliveries and evaluations for a simulation run to an authorized actor

- **المدخلات:** `cursor`, `limit`؛ مع ترويسة `X-Purpose`
- **المخرجات:** Full, ordered timeline of inject deliveries and evaluations for a simulation؛ صفحة بمؤشر (لا offset — FIT-13)
- **الصلاحية:** allowed_scope؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-SIM-TIMELINE` · `AGG-SIMULATION` · متطلبات: REQ-TRX-015
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-SIM-TIMELINE returns only what the caller may see
  Given items inside and outside the caller's allowed_scope
  When the caller sends QRY-SIM-TIMELINE with a cursor
  Then only items inside allowed_scope are returned, each re-checked (security_version, LabelCheck)
  And no count, facet or suggestion reveals a hidden item

Scenario: QRY-SIM-TIMELINE is denied
  Given the policy denies the caller
  When the caller sends QRY-SIM-TIMELINE
  Then the response has the same shape as for a missing item (not-found shape)
```

### استعلامات عابرة للـAggregates

#### US-BC05-Q-ELIG-CHECK — جلب: EligibilityCheck(person, task_type version, at) → status + reasons

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | Planner/Manager in scope; internal BC04 (workload identity) | `POST /api/v1/readiness/eligibility-checks` | POL-ELIG-CHECK |

**القصة:** بصفتي **Planner/Manager in scope; internal BC04 (workload identity)**، أريد **جلب EligibilityCheck(person, task_type version, at) → status + reasons**، لكي يتحقق المتطلب: When eligibility is checked for a person, role or task at a given time, the system shall return ELIGIBLE, CONDITIONALLY_ELIGIBLE, NOT_ELIGIBLE, EXPIRED, REQUIRES_SUPERVISION, REQUIRES_TRAINING, REQUIRES_CERTIFICATION or UNKNOWN, with reasons

- **المدخلات:** معاملات المسار فقط؛ مع ترويسة `X-Purpose`
- **المخرجات:** EligibilityCheck(person, task_type version, at) → status + reasons
- **الصلاحية:** Planner/Manager in scope; internal BC04 (workload identity)؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** الحالة الحالية
- **الربط:** `QRY-ELIG-CHECK` · عابر للـAggregates · متطلبات: REQ-RDY-002
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-ELIG-CHECK computes its result only over what the caller may see
  Given data inside and outside the caller's allowed_scope
  When the caller sends QRY-ELIG-CHECK
  Then the result neither includes nor reveals data outside allowed_scope

Scenario: QRY-ELIG-CHECK is denied
  Given the policy denies the caller
  When the caller sends QRY-ELIG-CHECK
  Then the response has the same shape as for a missing item (not-found shape)
```

#### US-BC05-Q-READINESS — جلب: Readiness of a person or unit for a role at time t, with gaps

| النوع | الفئة | الفاعل | الواجهة | السياسة |
|---|---|---|---|---|
| جلب | أساسية | Manager / Training Manager in scope; self | `POST /api/v1/readiness/readiness-checks` | POL-READINESS |

**القصة:** بصفتي **Manager / Training Manager in scope; self**، أريد **جلب Readiness of a person or unit for a role at time t, with gaps**، لكي يتحقق المتطلب: The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications, certifications, recent training, experience and authorization

- **المدخلات:** `subject`!, `role`!, `at`! (معاملات الرابط وحقول جسم الطلب؛ `!` = إلزامي)؛ مع ترويسة `X-Purpose`
- **المخرجات:** Readiness of a person or unit for a role at time t, with gaps
- **الصلاحية:** Manager / Training Manager in scope; self؛ النطاق المسموح: —؛ عند الرفض: DENY (not-found shape)
- **الزمن:** استعلام بأثر رجعي عبر `at`
- **الربط:** `QRY-READINESS` · عابر للـAggregates · متطلبات: REQ-RES-013
- **ضوابط النوع والفئة:** C-READ، K-CORE

```gherkin
Scenario: QRY-READINESS computes its result only over what the caller may see
  Given data inside and outside the caller's allowed_scope
  When the caller sends QRY-READINESS
  Then the result neither includes nor reveals data outside allowed_scope

Scenario: QRY-READINESS is denied
  Given the policy denies the caller
  When the caller sends QRY-READINESS
  Then the response has the same shape as for a missing item (not-found shape)
```

<!-- END GENERATED: build_analysis_design.py -->
