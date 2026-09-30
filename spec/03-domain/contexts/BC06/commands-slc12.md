---
id: CMD-CAT-BC06-SLC12
type: command-catalog
title: Commands — BC06 (SLC-12)
wave: W4
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC06 (SLC-12)

_29 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-PTM-DEFINE | AGG-PRODUCT-TEMPLATE | `POST /api/v1/knowledge/product-templates` | لا | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | POL-PTM-DEFINE | `code!:string kind!:enum(report,briefing,map_product,analytical_product) name!:LocalizedName` | EVT-PTM-DEFINED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TEMPLATE_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PTM-EDIT | AGG-PRODUCT-TEMPLATE | `POST /api/v1/knowledge/product-templates/{id}/actions/edit` | لا | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | POL-PTM-EDIT | `sections!:array` | EVT-PTM-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION, TEMPLATE_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PTM-ACTIVATE | AGG-PRODUCT-TEMPLATE | `POST /api/v1/knowledge/product-templates/{id}/actions/activate` | لا | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | POL-PTM-ACTIVATE | `sample_ref!:urn` | EVT-PTM-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PTM-RETIRE | AGG-PRODUCT-TEMPLATE | `POST /api/v1/knowledge/product-templates/{id}/actions/retire` | لا | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | POL-PTM-RETIRE | `reason!:string` | EVT-PTM-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRD-CREATE | AGG-PRODUCT | `POST /api/v1/knowledge/products` | لا | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-CREATE | `template!:urn parameters!:object audience!:array title!:LocalizedName revises:urn label!:Label` | EVT-PRD-CREATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRD-GENERATE | AGG-PRODUCT | `POST /api/v1/knowledge/products/{id}/actions/generate` | لا | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-GENERATE | `—` | EVT-PRD-GENERATION-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRD-EDIT-NARRATIVE | AGG-PRODUCT | `POST /api/v1/knowledge/products/{id}/actions/edit-narrative` | لا | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-EDIT-NARRATIVE | `section_id!:string text!:LocalizedName` | EVT-PRD-NARRATIVE-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_INVALID_STATE_TRANSITION, SECTION_NOT_EDITABLE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRD-SUBMIT | AGG-PRODUCT | `POST /api/v1/knowledge/products/{id}/actions/submit` | لا | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-SUBMIT | `—` | EVT-PRD-SUBMITTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_INCOMPLETE, PRODUCT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRD-RETURN | AGG-PRODUCT | `POST /api/v1/knowledge/products/{id}/actions/return` | لا | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-RETURN | `reason!:string` | EVT-PRD-RETURNED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRD-APPROVE | AGG-PRODUCT | `POST /api/v1/knowledge/products/{id}/actions/approve` | لا | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-APPROVE | `note:string` | EVT-PRD-APPROVED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRD-WITHDRAW | AGG-PRODUCT | `POST /api/v1/knowledge/products/{id}/actions/withdraw` | لا | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-WITHDRAW | `reason!:string` | EVT-PRD-WITHDRAWN | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PRD-DISCARD | AGG-PRODUCT | `POST /api/v1/knowledge/products/{id}/actions/discard` | لا | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | POL-PRD-DISCARD | `reason!:string` | EVT-PRD-DISCARDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DST-DISTRIBUTE | AGG-DISTRIBUTION | `POST /api/v1/knowledge/distributions` | لا | Manager / product owner | POL-DST-DISTRIBUTE | `product!:urn recipients!:array formats!:array message:string` | EVT-DST-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRODUCT_NOT_APPROVED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-DST-CANCEL | AGG-DISTRIBUTION | `POST /api/v1/knowledge/distributions/{id}/actions/cancel` | لا | Manager / product owner | POL-DST-CANCEL | `reason!:string` | EVT-DST-CANCELLED | AUTHZ_DENIED, DISTRIBUTION_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-KNO-DRAFT | AGG-KNOWLEDGE-OBJECT | `POST /api/v1/knowledge/knowledge-objects` | لا | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-DRAFT | `knowledge_type!:enum(procedure,lesson,best_practice,policy_knowledge) title!:LocalizedName source:urn revises:urn label!:Label` | EVT-KNO-DRAFTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, KNOWLEDGE_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-KNO-EDIT | AGG-KNOWLEDGE-OBJECT | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/edit` | لا | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-EDIT | `statements!:array relationships:array` | EVT-KNO-EDITED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, KNOWLEDGE_INVALID, KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-KNO-SUBMIT | AGG-KNOWLEDGE-OBJECT | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/submit` | لا | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-SUBMIT | `—` | EVT-KNO-SUBMITTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, KNOWLEDGE_INCOMPLETE, KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-KNO-RETURN | AGG-KNOWLEDGE-OBJECT | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/return` | لا | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-RETURN | `reason!:string` | EVT-KNO-RETURNED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-KNO-PUBLISH | AGG-KNOWLEDGE-OBJECT | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/publish` | لا | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-PUBLISH | `note:string` | EVT-KNO-PUBLISHED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-KNO-REJECT | AGG-KNOWLEDGE-OBJECT | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/reject` | لا | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-REJECT | `reason!:string` | EVT-KNO-REJECTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-KNO-RECORD-REUSE | AGG-KNOWLEDGE-OBJECT | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/record-reuse` | لا | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-RECORD-REUSE | `target!:urn` | EVT-KNO-REUSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, TARGET_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-KNO-RETIRE | AGG-KNOWLEDGE-OBJECT | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/retire` | لا | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-RETIRE | `reason!:string` | EVT-KNO-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-KNO-DISCARD | AGG-KNOWLEDGE-OBJECT | `POST /api/v1/knowledge/knowledge-objects/{id}/actions/discard` | لا | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | POL-KNO-DISCARD | `reason!:string` | EVT-KNO-DISCARDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ARC-RETRY-INGEST | AGG-ARCHIVE-PACKAGE | `POST /api/v1/knowledge/archive-packages/{id}/actions/retry-ingest` | لا | Archivist (retry, repair, migrate) · transfer authority (transfer) | POL-ARC-RETRY-INGEST | `note!:string` | EVT-ARC-INGEST-STARTED | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ARC-REPAIR | AGG-ARCHIVE-PACKAGE | `POST /api/v1/knowledge/archive-packages/{id}/actions/repair` | لا | Archivist (retry, repair, migrate) · transfer authority (transfer) | POL-ARC-REPAIR | `replica_ref!:string` | EVT-ARC-REPAIRED | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, FIXITY_MISMATCH, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ARC-MIGRATE-FORMAT | AGG-ARCHIVE-PACKAGE | `POST /api/v1/knowledge/archive-packages/{id}/actions/migrate-format` | لا | Archivist (retry, repair, migrate) · transfer authority (transfer) | POL-ARC-MIGRATE-FORMAT | `target_format!:string reason!:string` | EVT-ARC-FORMAT-MIGRATED | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, FORMAT_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ARC-TRANSFER | AGG-ARCHIVE-PACKAGE | `POST /api/v1/knowledge/archive-packages/{id}/actions/transfer` | لا | Archivist (retry, repair, migrate) · transfer authority (transfer) | POL-ARC-TRANSFER | `decision!:urn receiving_archive!:string receipt!:string` | EVT-ARC-TRANSFERRED | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION, AUTHORITY_REQUIRED, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-REC-REQUEST | AGG-RECONSTRUCTION | `POST /api/v1/knowledge/reconstructions` | لا | Auditor / Legal / Analyst (request, cancel) | POL-REC-REQUEST | `scope!:object valid_at!:date-time known_at!:date-time purpose!:enum(audit,legal,lessons,analysis)` | EVT-REC-REQUESTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RECONSTRUCTION_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-REC-CANCEL | AGG-RECONSTRUCTION | `POST /api/v1/knowledge/reconstructions/{id}/actions/cancel` | لا | Auditor / Legal / Analyst (request, cancel) | POL-REC-CANCEL | `reason!:string` | EVT-REC-CANCELLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, RECONSTRUCTION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-PTM-DEFINE
  aggregate: AGG-PRODUCT-TEMPLATE
  bc: BC06
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: code unique; product kind ∈ {report, briefing, map_product, analytical_product}
    event: EVT-PTM-DEFINED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TEMPLATE_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/knowledge/product-templates
  internal: false
  policy: POL-PTM-DEFINE
  actors: Knowledge Manager / Analysis lead (define, edit) · second approver (activate)
  payload: code!:string kind!:enum(report,briefing,map_product,analytical_product)
    name!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-PTM-EDIT
  aggregate: AGG-PRODUCT-TEMPLATE
  bc: BC06
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    to: '='
    guard: sections valid (text, map, chart, table, key_judgments, citations); every
      data binding is a declared platform query with typed parameters; ACTIVE → new
      version
    event: EVT-PTM-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION
  - TEMPLATE_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/product-templates/{id}/actions/edit
  internal: false
  policy: POL-PTM-EDIT
  actors: Knowledge Manager / Analysis lead (define, edit) · second approver (activate)
  payload: sections!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PTM-ACTIVATE
  aggregate: AGG-PRODUCT-TEMPLATE
  bc: BC06
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: sample generation succeeded; approver ≠ author
    event: EVT-PTM-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/product-templates/{id}/actions/activate
  internal: false
  policy: POL-PTM-ACTIVATE
  actors: Knowledge Manager / Analysis lead (define, edit) · second approver (activate)
  payload: sample_ref!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PTM-RETIRE
  aggregate: AGG-PRODUCT-TEMPLATE
  bc: BC06
  transitions:
  - from:
    - ACTIVE
    to: RETIRED
    guard: reason; existing products keep their pinned version
    event: EVT-PTM-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/product-templates/{id}/actions/retire
  internal: false
  policy: POL-PTM-RETIRE
  actors: Knowledge Manager / Analysis lead (define, edit) · second approver (activate)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PRD-CREATE
  aggregate: AGG-PRODUCT
  bc: BC06
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: template ACTIVE (version pinned); parameters valid; audience (org units/roles);
      target label ≥ labels of scope objects referenced in parameters; optional revises
      = APPROVED version
    event: EVT-PRD-CREATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/knowledge/products
  internal: false
  policy: POL-PRD-CREATE
  actors: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return,
    approve) · Manager (withdraw)
  payload: template!:urn parameters!:object audience!:array title!:LocalizedName revises:urn
    label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-PRD-GENERATE
  aggregate: AGG-PRODUCT
  bc: BC06
  transitions:
  - from:
    - DRAFT
    - GENERATED
    - GENERATION_FAILED
    to: GENERATING
    guard: author; async job with the author's authority
    event: EVT-PRD-GENERATION-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/products/{id}/actions/generate
  internal: false
  policy: POL-PRD-GENERATE
  actors: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return,
    approve) · Manager (withdraw)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PRD-EDIT-NARRATIVE
  aggregate: AGG-PRODUCT
  bc: BC06
  transitions:
  - from:
    - GENERATED
    to: '='
    guard: only narrative sections; data sections change only by regeneration
    event: EVT-PRD-NARRATIVE-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_INVALID_STATE_TRANSITION
  - SECTION_NOT_EDITABLE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/products/{id}/actions/edit-narrative
  internal: false
  policy: POL-PRD-EDIT-NARRATIVE
  actors: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return,
    approve) · Manager (withdraw)
  payload: section_id!:string text!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PRD-SUBMIT
  aggregate: AGG-PRODUCT
  bc: BC06
  transitions:
  - from:
    - GENERATED
    to: IN_REVIEW
    guard: all required sections present; AI-drafted sections reviewed (REQ-AI-005)
    event: EVT-PRD-SUBMITTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_INCOMPLETE
  - PRODUCT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/products/{id}/actions/submit
  internal: false
  policy: POL-PRD-SUBMIT
  actors: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return,
    approve) · Manager (withdraw)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PRD-RETURN
  aggregate: AGG-PRODUCT
  bc: BC06
  transitions:
  - from:
    - IN_REVIEW
    to: GENERATED
    guard: reviewer; reason
    event: EVT-PRD-RETURNED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/products/{id}/actions/return
  internal: false
  policy: POL-PRD-RETURN
  actors: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return,
    approve) · Manager (withdraw)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PRD-APPROVE
  aggregate: AGG-PRODUCT
  bc: BC06
  transitions:
  - from:
    - IN_REVIEW
    to: APPROVED
    guard: reviewer ≠ author; content frozen with pinned citations; previous APPROVED
      version of the same product → SUPERSEDED
    event: EVT-PRD-APPROVED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/products/{id}/actions/approve
  internal: false
  policy: POL-PRD-APPROVE
  actors: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return,
    approve) · Manager (withdraw)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PRD-WITHDRAW
  aggregate: AGG-PRODUCT
  bc: BC06
  transitions:
  - from:
    - APPROVED
    to: WITHDRAWN
    guard: reason; recipients notified
    event: EVT-PRD-WITHDRAWN
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/products/{id}/actions/withdraw
  internal: false
  policy: POL-PRD-WITHDRAW
  actors: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return,
    approve) · Manager (withdraw)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PRD-DISCARD
  aggregate: AGG-PRODUCT
  bc: BC06
  transitions:
  - from:
    - DRAFT
    - GENERATED
    - GENERATION_FAILED
    to: DISCARDED
    guard: author; reason
    event: EVT-PRD-DISCARDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/products/{id}/actions/discard
  internal: false
  policy: POL-PRD-DISCARD
  actors: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return,
    approve) · Manager (withdraw)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-DST-DISTRIBUTE
  aggregate: AGG-DISTRIBUTION
  bc: BC06
  transitions:
  - from:
    - ∅
    to: PREPARING
    guard: product APPROVED; recipients (users, org units); formats ⊆ {pdf, docx,
      in_app}; distributor authorized
    event: EVT-DST-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRODUCT_NOT_APPROVED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/knowledge/distributions
  internal: false
  policy: POL-DST-DISTRIBUTE
  actors: Manager / product owner
  payload: product!:urn recipients!:array formats!:array message:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-DST-CANCEL
  aggregate: AGG-DISTRIBUTION
  bc: BC06
  transitions:
  - from:
    - PREPARING
    to: CANCELLED
    guard: distributor; reason
    event: EVT-DST-CANCELLED
  errors:
  - AUTHZ_DENIED
  - DISTRIBUTION_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/distributions/{id}/actions/cancel
  internal: false
  policy: POL-DST-CANCEL
  actors: Manager / product owner
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-KNO-DRAFT
  aggregate: AGG-KNOWLEDGE-OBJECT
  bc: BC06
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: type ∈ {procedure, lesson, best_practice, policy_knowledge}; lessons reference
      a terminal source (task, plan, incident, or a completed exercise simulation
      — CR-63) and its evidence (REQ-KNW-002); label ≥ source label
    event: EVT-KNO-DRAFTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - KNOWLEDGE_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/knowledge/knowledge-objects
  internal: false
  policy: POL-KNO-DRAFT
  actors: any user (draft lessons) · Knowledge Manager (review, publish, retire) ·
    planner (record reuse)
  payload: knowledge_type!:enum(procedure,lesson,best_practice,policy_knowledge) title!:LocalizedName
    source:urn revises:urn label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-KNO-EDIT
  aggregate: AGG-KNOWLEDGE-OBJECT
  bc: BC06
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: statements with evidence links; relationships to task types, plan types,
      entity types, areas
    event: EVT-KNO-EDITED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - KNOWLEDGE_INVALID
  - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/knowledge-objects/{id}/actions/edit
  internal: false
  policy: POL-KNO-EDIT
  actors: any user (draft lessons) · Knowledge Manager (review, publish, retire) ·
    planner (record reuse)
  payload: statements!:array relationships:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-KNO-SUBMIT
  aggregate: AGG-KNOWLEDGE-OBJECT
  bc: BC06
  transitions:
  - from:
    - DRAFT
    to: IN_REVIEW
    guard: '≥ 1 statement; lessons: ≥ 1 evidence link'
    event: EVT-KNO-SUBMITTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - KNOWLEDGE_INCOMPLETE
  - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/knowledge-objects/{id}/actions/submit
  internal: false
  policy: POL-KNO-SUBMIT
  actors: any user (draft lessons) · Knowledge Manager (review, publish, retire) ·
    planner (record reuse)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-KNO-RETURN
  aggregate: AGG-KNOWLEDGE-OBJECT
  bc: BC06
  transitions:
  - from:
    - IN_REVIEW
    to: DRAFT
    guard: reviewer; reason
    event: EVT-KNO-RETURNED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/knowledge-objects/{id}/actions/return
  internal: false
  policy: POL-KNO-RETURN
  actors: any user (draft lessons) · Knowledge Manager (review, publish, retire) ·
    planner (record reuse)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-KNO-PUBLISH
  aggregate: AGG-KNOWLEDGE-OBJECT
  bc: BC06
  transitions:
  - from:
    - IN_REVIEW
    to: PUBLISHED
    guard: reviewer ≠ author; procedures and policy knowledge require the owning authority
      (Knowledge Manager + domain authority); previous PUBLISHED → SUPERSEDED
    event: EVT-KNO-PUBLISHED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/knowledge-objects/{id}/actions/publish
  internal: false
  policy: POL-KNO-PUBLISH
  actors: any user (draft lessons) · Knowledge Manager (review, publish, retire) ·
    planner (record reuse)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-KNO-REJECT
  aggregate: AGG-KNOWLEDGE-OBJECT
  bc: BC06
  transitions:
  - from:
    - IN_REVIEW
    to: REJECTED
    guard: reason
    event: EVT-KNO-REJECTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/knowledge-objects/{id}/actions/reject
  internal: false
  policy: POL-KNO-REJECT
  actors: any user (draft lessons) · Knowledge Manager (review, publish, retire) ·
    planner (record reuse)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-KNO-RECORD-REUSE
  aggregate: AGG-KNOWLEDGE-OBJECT
  bc: BC06
  transitions:
  - from:
    - PUBLISHED
    to: '='
    guard: target plan/task/product visible; reuse counted (OUT-06)
    event: EVT-KNO-REUSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
  - TARGET_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/knowledge-objects/{id}/actions/record-reuse
  internal: false
  policy: POL-KNO-RECORD-REUSE
  actors: any user (draft lessons) · Knowledge Manager (review, publish, retire) ·
    planner (record reuse)
  payload: target!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-KNO-RETIRE
  aggregate: AGG-KNOWLEDGE-OBJECT
  bc: BC06
  transitions:
  - from:
    - PUBLISHED
    to: RETIRED
    guard: reason (obsolete, wrong)
    event: EVT-KNO-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/knowledge-objects/{id}/actions/retire
  internal: false
  policy: POL-KNO-RETIRE
  actors: any user (draft lessons) · Knowledge Manager (review, publish, retire) ·
    planner (record reuse)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-KNO-DISCARD
  aggregate: AGG-KNOWLEDGE-OBJECT
  bc: BC06
  transitions:
  - from:
    - DRAFT
    to: DISCARDED
    guard: author; reason
    event: EVT-KNO-DISCARDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/knowledge-objects/{id}/actions/discard
  internal: false
  policy: POL-KNO-DISCARD
  actors: any user (draft lessons) · Knowledge Manager (review, publish, retire) ·
    planner (record reuse)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ARC-RETRY-INGEST
  aggregate: AGG-ARCHIVE-PACKAGE
  bc: BC06
  transitions:
  - from:
    - INGEST_FAILED
    to: INGESTING
    guard: archivist; corrective note
    event: EVT-ARC-INGEST-STARTED
  errors:
  - ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/archive-packages/{id}/actions/retry-ingest
  internal: false
  policy: POL-ARC-RETRY-INGEST
  actors: Archivist (retry, repair, migrate) · transfer authority (transfer)
  payload: note!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ARC-REPAIR
  aggregate: AGG-ARCHIVE-PACKAGE
  bc: BC06
  transitions:
  - from:
    - INTEGRITY_FAILED
    to: ARCHIVED
    guard: restored from replica; fixity re-verified
    event: EVT-ARC-REPAIRED
  errors:
  - ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - FIXITY_MISMATCH
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/archive-packages/{id}/actions/repair
  internal: false
  policy: POL-ARC-REPAIR
  actors: Archivist (retry, repair, migrate) · transfer authority (transfer)
  payload: replica_ref!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ARC-MIGRATE-FORMAT
  aggregate: AGG-ARCHIVE-PACKAGE
  bc: BC06
  transitions:
  - from:
    - ARCHIVED
    to: '='
    guard: new preservation representation added; originals kept; preservation event
      recorded
    event: EVT-ARC-FORMAT-MIGRATED
  errors:
  - ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - FORMAT_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/archive-packages/{id}/actions/migrate-format
  internal: false
  policy: POL-ARC-MIGRATE-FORMAT
  actors: Archivist (retry, repair, migrate) · transfer authority (transfer)
  payload: target_format!:string reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ARC-TRANSFER
  aggregate: AGG-ARCHIVE-PACKAGE
  bc: BC06
  transitions:
  - from:
    - ARCHIVED
    to: TRANSFERRED
    guard: transfer authority decision; receipt from the receiving archive
    event: EVT-ARC-TRANSFERRED
  errors:
  - ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION
  - AUTHORITY_REQUIRED
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/archive-packages/{id}/actions/transfer
  internal: false
  policy: POL-ARC-TRANSFER
  actors: Archivist (retry, repair, migrate) · transfer authority (transfer)
  payload: decision!:urn receiving_archive!:string receipt!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-REC-REQUEST
  aggregate: AGG-RECONSTRUCTION
  bc: BC06
  transitions:
  - from:
    - ∅
    to: REQUESTED
    guard: scope (objects, situation, plan, decision basis); valid_at T; known_at
      K ≤ now; purpose (audit, legal, lessons); requester authorized
    event: EVT-REC-REQUESTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RECONSTRUCTION_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/knowledge/reconstructions
  internal: false
  policy: POL-REC-REQUEST
  actors: Auditor / Legal / Analyst (request, cancel)
  payload: scope!:object valid_at!:date-time known_at!:date-time purpose!:enum(audit,legal,lessons,analysis)
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-REC-CANCEL
  aggregate: AGG-RECONSTRUCTION
  bc: BC06
  transitions:
  - from:
    - REQUESTED
    - RUNNING
    to: CANCELLED
    guard: requester; reason
    event: EVT-REC-CANCELLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - RECONSTRUCTION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/knowledge/reconstructions/{id}/actions/cancel
  internal: false
  policy: POL-REC-CANCEL
  actors: Auditor / Legal / Analyst (request, cancel)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
