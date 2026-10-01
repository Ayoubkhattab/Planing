---
id: CMD-CAT-BC03-SLC07
type: command-catalog
title: Commands — BC03 (SLC-07)
wave: W4
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC03 (SLC-07)

_32 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-ACS-CREATE | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-CREATE | `title!:LocalizedName owner!:urn label!:Label` | EVT-ACS-CREATED | AUTHZ_DENIED, CASE_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-DEFINE | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/define` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-DEFINE | `question!:LocalizedName extent:object window!:Interval` | EVT-ACS-DEFINED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CASE_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-OPEN | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/open` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-OPEN | `—` | EVT-ACS-OPENED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CASE_NOT_DEFINED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-ADD-HYPOTHESIS | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/add-hypothesis` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-ADD-HYPOTHESIS | `statement!:LocalizedName` | EVT-ACS-HYPOTHESIS-ADDED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CASE_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-UPDATE-HYPOTHESIS | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/update-hypothesis` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-UPDATE-HYPOTHESIS | `hypothesis_id!:string status!:enum(PROPOSED,SUPPORTED,WEAKENED,REJECTED,UNRESOLVED) rationale!:string findings:array` | EVT-ACS-HYPOTHESIS-UPDATED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-ADD-ASSUMPTION | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/add-assumption` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-ADD-ASSUMPTION | `statement!:LocalizedName criticality!:enum(high,medium,low)` | EVT-ACS-ASSUMPTION-ADDED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CASE_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-RETIRE-ASSUMPTION | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/retire-assumption` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-RETIRE-ASSUMPTION | `assumption_id!:string reason!:string` | EVT-ACS-ASSUMPTION-RETIRED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-SELECT-EVIDENCE | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/select-evidence` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-SELECT-EVIDENCE | `items!:array note:string` | EVT-ACS-EVIDENCE-SELECTED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, EVIDENCE_ABOVE_CASE_LABEL, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-DESELECT-EVIDENCE | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/deselect-evidence` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-DESELECT-EVIDENCE | `selection_id!:string reason!:string` | EVT-ACS-EVIDENCE-DESELECTED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-DEFINE-SCENARIO | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/define-scenario` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-DEFINE-SCENARIO | `name!:string assumptions!:array parameter_overrides:object` | EVT-ACS-SCENARIO-DEFINED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CASE_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-CLOSE | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/close` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-CLOSE | `reason!:string` | EVT-ACS-CLOSED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RUNS_IN_PROGRESS, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-REOPEN | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/reopen` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-REOPEN | `reason!:string` | EVT-ACS-REOPENED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-CANCEL | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/cancel` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-CANCEL | `reason!:string` | EVT-ACS-CANCELLED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CASE_HAS_PUBLISHED_ASSESSMENT, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ACS-RECLASSIFY | AGG-ANALYSIS-CASE | `POST /api/v1/intelligence/analysis-cases/{id}/actions/reclassify` | لا | Analyst (owner) · Security Officer (reclassify) | POL-ACS-RECLASSIFY | `label!:Label reason!:string` | EVT-ACS-RECLASSIFIED | ANALYSIS_CASE_INVALID_STATE_TRANSITION, AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AMT-REGISTER | AGG-ANALYSIS-METHOD | `POST /api/v1/intelligence/analysis-methods` | لا | Analysis lead (register) · second lead or Administrator (activate) | POL-AMT-REGISTER | `code!:string version!:string parameter_schema!:object image_digest!:string deterministic!:boolean description!:LocalizedName` | EVT-AMT-REGISTERED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, METHOD_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AMT-ACTIVATE | AGG-ANALYSIS-METHOD | `POST /api/v1/intelligence/analysis-methods/{id}/actions/activate` | لا | Analysis lead (register) · second lead or Administrator (activate) | POL-AMT-ACTIVATE | `validation_report!:urn` | EVT-AMT-ACTIVATED | ANALYSIS_METHOD_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AMT-DEPRECATE | AGG-ANALYSIS-METHOD | `POST /api/v1/intelligence/analysis-methods/{id}/actions/deprecate` | لا | Analysis lead | POL-AMT-DEPRECATE | `reason!:string` | EVT-AMT-DEPRECATED | ANALYSIS_METHOD_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AMT-RETIRE | AGG-ANALYSIS-METHOD | `POST /api/v1/intelligence/analysis-methods/{id}/actions/retire` | لا | Analysis lead | POL-AMT-RETIRE | `reason!:string` | EVT-AMT-RETIRED | ANALYSIS_METHOD_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, METHOD_BACKS_PUBLISHED_WORK, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RUN-SUBMIT | AGG-ANALYSIS-RUN | `POST /api/v1/intelligence/analysis-runs` | لا | Analyst (submit, reproduce, cancel) | POL-RUN-SUBMIT | `case!:urn method!:urn parameters!:object inputs!:array scenario:string assumptions:array seed:integer label!:Label` | EVT-RUN-QUEUED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RUN_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RUN-REPRODUCE | AGG-ANALYSIS-RUN | `POST /api/v1/intelligence/analysis-runs/{id}/actions/reproduce` | لا | Analyst (submit, reproduce, cancel) | POL-RUN-REPRODUCE | `source_run!:urn` | EVT-RUN-QUEUED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REPRODUCTION_NOT_ALLOWED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RUN-CANCEL | AGG-ANALYSIS-RUN | `POST /api/v1/intelligence/analysis-runs/{id}/actions/cancel` | لا | Analyst (submit, reproduce, cancel) | POL-RUN-CANCEL | `reason!:string` | EVT-RUN-CANCELLED | ANALYSIS_RUN_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-FND-RECORD | AGG-FINDING | `POST /api/v1/intelligence/findings` | لا | Analyst (record, edit, withdraw) · peer Analyst (accept) | POL-FND-RECORD | `case!:urn statement!:LocalizedName sources!:array uncertainty!:object label!:Label` | EVT-FND-RECORDED | AUTHZ_DENIED, FINDING_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-FND-EDIT | AGG-FINDING | `POST /api/v1/intelligence/findings/{id}/actions/edit` | لا | Analyst (record, edit, withdraw) · peer Analyst (accept) | POL-FND-EDIT | `statement:LocalizedName sources:array uncertainty:object` | EVT-FND-EDITED | AUTHZ_DENIED, FINDING_INVALID, FINDING_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-FND-ACCEPT | AGG-FINDING | `POST /api/v1/intelligence/findings/{id}/actions/accept` | لا | Analyst (record, edit, withdraw) · peer Analyst (accept) | POL-FND-ACCEPT | `note:string` | EVT-FND-ACCEPTED | AUTHZ_DENIED, FINDING_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-FND-WITHDRAW | AGG-FINDING | `POST /api/v1/intelligence/findings/{id}/actions/withdraw` | لا | Analyst (record, edit, withdraw) · peer Analyst (accept) | POL-FND-WITHDRAW | `reason!:string` | EVT-FND-WITHDRAWN | AUTHZ_DENIED, FINDING_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ASM-DRAFT | AGG-ASSESSMENT | `POST /api/v1/intelligence/assessments` | لا | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-DRAFT | `case!:urn assessment:urn title!:LocalizedName label!:Label` | EVT-ASM-DRAFTED | AUTHZ_DENIED, DRAFT_EXISTS, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ASM-EDIT | AGG-ASSESSMENT | `POST /api/v1/intelligence/assessments/{id}/actions/edit` | لا | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-EDIT | `key_judgments!:array citations!:array assumptions!:array uncertainty!:object confidence!:enum(low,moderate,high) methodology!:LocalizedName limitations!:LocalizedName` | EVT-ASM-EDITED | ASSESSMENT_INVALID, ASSESSMENT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ASM-SUBMIT | AGG-ASSESSMENT | `POST /api/v1/intelligence/assessments/{id}/actions/submit` | لا | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-SUBMIT | `—` | EVT-ASM-SUBMITTED | ASSESSMENT_INCOMPLETE, ASSESSMENT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ASM-RETURN | AGG-ASSESSMENT | `POST /api/v1/intelligence/assessments/{id}/actions/return` | لا | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-RETURN | `reason!:string` | EVT-ASM-RETURNED | ASSESSMENT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ASM-PUBLISH | AGG-ASSESSMENT | `POST /api/v1/intelligence/assessments/{id}/actions/publish` | لا | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-PUBLISH | `note:string` | EVT-ASM-PUBLISHED | ASSESSMENT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ASM-WITHDRAW | AGG-ASSESSMENT | `POST /api/v1/intelligence/assessments/{id}/actions/withdraw` | لا | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-WITHDRAW | `reason!:string` | EVT-ASM-WITHDRAWN | ASSESSMENT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ASM-DISCARD | AGG-ASSESSMENT | `POST /api/v1/intelligence/assessments/{id}/actions/discard` | لا | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | POL-ASM-DISCARD | `reason!:string` | EVT-ASM-DISCARDED | ASSESSMENT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-ACS-CREATE
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: title; owner; label
    event: EVT-ACS-CREATED
  errors:
  - AUTHZ_DENIED
  - CASE_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/intelligence/analysis-cases
  internal: false
  policy: POL-ACS-CREATE
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: title!:LocalizedName owner!:urn label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ACS-DEFINE
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - DRAFT
    - OPEN
    to: '='
    guard: question text; spatial extent (optional polygon); time window; new version
    event: EVT-ACS-DEFINED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CASE_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/define
  internal: false
  policy: POL-ACS-DEFINE
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: question!:LocalizedName extent:object window!:Interval
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-OPEN
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - DRAFT
    to: OPEN
    guard: question and scope present (REQ-ANL-001)
    event: EVT-ACS-OPENED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CASE_NOT_DEFINED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/open
  internal: false
  policy: POL-ACS-OPEN
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-ADD-HYPOTHESIS
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - OPEN
    to: '='
    guard: statement; hypotheses per case ≤ 20
    event: EVT-ACS-HYPOTHESIS-ADDED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CASE_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/add-hypothesis
  internal: false
  policy: POL-ACS-ADD-HYPOTHESIS
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: statement!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-UPDATE-HYPOTHESIS
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - OPEN
    to: '='
    guard: status ∈ {PROPOSED, SUPPORTED, WEAKENED, REJECTED, UNRESOLVED}; rationale;
      supporting findings refs
    event: EVT-ACS-HYPOTHESIS-UPDATED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/update-hypothesis
  internal: false
  policy: POL-ACS-UPDATE-HYPOTHESIS
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: hypothesis_id!:string status!:enum(PROPOSED,SUPPORTED,WEAKENED,REJECTED,UNRESOLVED)
    rationale!:string findings:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-ADD-ASSUMPTION
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - OPEN
    to: '='
    guard: statement; criticality (high/medium/low)
    event: EVT-ACS-ASSUMPTION-ADDED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CASE_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/add-assumption
  internal: false
  policy: POL-ACS-ADD-ASSUMPTION
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: statement!:LocalizedName criticality!:enum(high,medium,low)
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-RETIRE-ASSUMPTION
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - OPEN
    to: '='
    guard: reason; runs using it are flagged
    event: EVT-ACS-ASSUMPTION-RETIRED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/retire-assumption
  internal: false
  policy: POL-ACS-RETIRE-ASSUMPTION
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: assumption_id!:string reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-SELECT-EVIDENCE
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - OPEN
    to: '='
    guard: items visible to actor; each pinned with known_at = now; item label ≤ case
      label
    event: EVT-ACS-EVIDENCE-SELECTED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - EVIDENCE_ABOVE_CASE_LABEL
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/select-evidence
  internal: false
  policy: POL-ACS-SELECT-EVIDENCE
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: items!:array note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-DESELECT-EVIDENCE
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - OPEN
    to: '='
    guard: reason; selection record closed, not deleted
    event: EVT-ACS-EVIDENCE-DESELECTED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/deselect-evidence
  internal: false
  policy: POL-ACS-DESELECT-EVIDENCE
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: selection_id!:string reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-DEFINE-SCENARIO
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - OPEN
    to: '='
    guard: name; assumption set; parameter overrides (REQ-ANL-007)
    event: EVT-ACS-SCENARIO-DEFINED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CASE_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/define-scenario
  internal: false
  policy: POL-ACS-DEFINE-SCENARIO
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: name!:string assumptions!:array parameter_overrides:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-CLOSE
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - OPEN
    to: CLOSED
    guard: reason; no QUEUED or RUNNING runs
    event: EVT-ACS-CLOSED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RUNS_IN_PROGRESS
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/close
  internal: false
  policy: POL-ACS-CLOSE
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-REOPEN
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - CLOSED
    to: OPEN
    guard: reason
    event: EVT-ACS-REOPENED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/reopen
  internal: false
  policy: POL-ACS-REOPEN
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-CANCEL
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - DRAFT
    - OPEN
    to: CANCELLED
    guard: reason; no PUBLISHED assessment references the case
    event: EVT-ACS-CANCELLED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CASE_HAS_PUBLISHED_ASSESSMENT
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/cancel
  internal: false
  policy: POL-ACS-CANCEL
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ACS-RECLASSIFY
  aggregate: AGG-ANALYSIS-CASE
  bc: BC03
  transitions:
  - from:
    - DRAFT
    - OPEN
    - CLOSED
    to: '='
    guard: new label ≥ max label of selected evidence; authority per policy
    event: EVT-ACS-RECLASSIFIED
  errors:
  - ANALYSIS_CASE_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-cases/{id}/actions/reclassify
  internal: false
  policy: POL-ACS-RECLASSIFY
  actors: Analyst (owner) · Security Officer (reclassify)
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AMT-REGISTER
  aggregate: AGG-ANALYSIS-METHOD
  bc: BC03
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: code + version unique; parameter JSON schema; execution image digest from
      internal registry; deterministic flag
    event: EVT-AMT-REGISTERED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - METHOD_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/intelligence/analysis-methods
  internal: false
  policy: POL-AMT-REGISTER
  actors: Analysis lead (register) · second lead or Administrator (activate)
  payload: code!:string version!:string parameter_schema!:object image_digest!:string
    deterministic!:boolean description!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-AMT-ACTIVATE
  aggregate: AGG-ANALYSIS-METHOD
  bc: BC03
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: validation suite passed; approver ≠ author
    event: EVT-AMT-ACTIVATED
  errors:
  - ANALYSIS_METHOD_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-methods/{id}/actions/activate
  internal: false
  policy: POL-AMT-ACTIVATE
  actors: Analysis lead (register) · second lead or Administrator (activate)
  payload: validation_report!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AMT-DEPRECATE
  aggregate: AGG-ANALYSIS-METHOD
  bc: BC03
  transitions:
  - from:
    - ACTIVE
    to: DEPRECATED
    guard: reason; no new runs; reproduction still allowed
    event: EVT-AMT-DEPRECATED
  errors:
  - ANALYSIS_METHOD_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-methods/{id}/actions/deprecate
  internal: false
  policy: POL-AMT-DEPRECATE
  actors: Analysis lead
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AMT-RETIRE
  aggregate: AGG-ANALYSIS-METHOD
  bc: BC03
  transitions:
  - from:
    - DEPRECATED
    to: RETIRED
    guard: no run of this version backs a PUBLISHED or SUPERSEDED assessment (reproducibility
      preserved)
    event: EVT-AMT-RETIRED
  errors:
  - ANALYSIS_METHOD_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - METHOD_BACKS_PUBLISHED_WORK
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-methods/{id}/actions/retire
  internal: false
  policy: POL-AMT-RETIRE
  actors: Analysis lead
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RUN-SUBMIT
  aggregate: AGG-ANALYSIS-RUN
  bc: BC03
  transitions:
  - from:
    - ∅
    to: QUEUED
    guard: case OPEN; method ACTIVE; parameters valid against schema; inputs pinned
      (dataset refs with known_at = submission time, filters, layers, extent, time
      window, assumptions); run label ≥ max input label; tenant job quota
    event: EVT-RUN-QUEUED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RUN_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/intelligence/analysis-runs
  internal: false
  policy: POL-RUN-SUBMIT
  actors: Analyst (submit, reproduce, cancel)
  payload: case!:urn method!:urn parameters!:object inputs!:array scenario:string
    assumptions:array seed:integer label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-RUN-REPRODUCE
  aggregate: AGG-ANALYSIS-RUN
  bc: BC03
  transitions:
  - from:
    - ∅
    to: QUEUED
    guard: source run SUCCEEDED; reproducer cleared for source run label; method version
      ACTIVE or DEPRECATED; copies inputs/parameters/seed exactly
    event: EVT-RUN-QUEUED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REPRODUCTION_NOT_ALLOWED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/intelligence/analysis-runs/{id}/actions/reproduce
  internal: false
  policy: POL-RUN-REPRODUCE
  actors: Analyst (submit, reproduce, cancel)
  payload: source_run!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-RUN-CANCEL
  aggregate: AGG-ANALYSIS-RUN
  bc: BC03
  transitions:
  - from:
    - QUEUED
    - RUNNING
    to: CANCELLED
    guard: submitter or case owner; reason
    event: EVT-RUN-CANCELLED
  errors:
  - ANALYSIS_RUN_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/analysis-runs/{id}/actions/cancel
  internal: false
  policy: POL-RUN-CANCEL
  actors: Analyst (submit, reproduce, cancel)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-FND-RECORD
  aggregate: AGG-FINDING
  bc: BC03
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: statement; ≥ 1 source among SUCCEEDED runs of the case or selected evidence;
      uncertainty; label ≥ sources
    event: EVT-FND-RECORDED
  errors:
  - AUTHZ_DENIED
  - FINDING_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/intelligence/findings
  internal: false
  policy: POL-FND-RECORD
  actors: Analyst (record, edit, withdraw) · peer Analyst (accept)
  payload: case!:urn statement!:LocalizedName sources!:array uncertainty!:object label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-FND-EDIT
  aggregate: AGG-FINDING
  bc: BC03
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: same rules; new version
    event: EVT-FND-EDITED
  errors:
  - AUTHZ_DENIED
  - FINDING_INVALID
  - FINDING_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/findings/{id}/actions/edit
  internal: false
  policy: POL-FND-EDIT
  actors: Analyst (record, edit, withdraw) · peer Analyst (accept)
  payload: statement:LocalizedName sources:array uncertainty:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-FND-ACCEPT
  aggregate: AGG-FINDING
  bc: BC03
  transitions:
  - from:
    - DRAFT
    to: ACCEPTED
    guard: reviewer ≠ author (peer review)
    event: EVT-FND-ACCEPTED
  errors:
  - AUTHZ_DENIED
  - FINDING_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/findings/{id}/actions/accept
  internal: false
  policy: POL-FND-ACCEPT
  actors: Analyst (record, edit, withdraw) · peer Analyst (accept)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-FND-WITHDRAW
  aggregate: AGG-FINDING
  bc: BC03
  transitions:
  - from:
    - DRAFT
    - ACCEPTED
    to: WITHDRAWN
    guard: reason; assessments citing it are flagged for review
    event: EVT-FND-WITHDRAWN
  errors:
  - AUTHZ_DENIED
  - FINDING_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/findings/{id}/actions/withdraw
  internal: false
  policy: POL-FND-WITHDRAW
  actors: Analyst (record, edit, withdraw) · peer Analyst (accept)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ASM-DRAFT
  aggregate: AGG-ASSESSMENT
  bc: BC03
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: case exists; either new assessment or revision of a PUBLISHED version (copies
      content); at most one DRAFT/IN_REVIEW per assessment
    event: EVT-ASM-DRAFTED
  errors:
  - AUTHZ_DENIED
  - DRAFT_EXISTS
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/intelligence/assessments
  internal: false
  policy: POL-ASM-DRAFT
  actors: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return,
    publish, withdraw)
  payload: case!:urn assessment:urn title!:LocalizedName label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ASM-EDIT
  aggregate: AGG-ASSESSMENT
  bc: BC03
  transitions:
  - from:
    - DRAFT
    to: '='
    guard: key judgments use RD-ESTIMATIVE-PROBABILITY terms and analytic confidence
      (low/moderate/high)
    event: EVT-ASM-EDITED
  errors:
  - ASSESSMENT_INVALID
  - ASSESSMENT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/assessments/{id}/actions/edit
  internal: false
  policy: POL-ASM-EDIT
  actors: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return,
    publish, withdraw)
  payload: key_judgments!:array citations!:array assumptions!:array uncertainty!:object
    confidence!:enum(low,moderate,high) methodology!:LocalizedName limitations!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ASM-SUBMIT
  aggregate: AGG-ASSESSMENT
  bc: BC03
  transitions:
  - from:
    - DRAFT
    to: IN_REVIEW
    guard: findings ≥ 1 (ACCEPTED), evidence, assumptions, uncertainty, confidence,
      methodology, limitations all present (REQ-ANL-005)
    event: EVT-ASM-SUBMITTED
  errors:
  - ASSESSMENT_INCOMPLETE
  - ASSESSMENT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/assessments/{id}/actions/submit
  internal: false
  policy: POL-ASM-SUBMIT
  actors: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return,
    publish, withdraw)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ASM-RETURN
  aggregate: AGG-ASSESSMENT
  bc: BC03
  transitions:
  - from:
    - IN_REVIEW
    to: DRAFT
    guard: reviewer; reason
    event: EVT-ASM-RETURNED
  errors:
  - ASSESSMENT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/assessments/{id}/actions/return
  internal: false
  policy: POL-ASM-RETURN
  actors: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return,
    publish, withdraw)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ASM-PUBLISH
  aggregate: AGG-ASSESSMENT
  bc: BC03
  transitions:
  - from:
    - IN_REVIEW
    to: PUBLISHED
    guard: reviewer ≠ author; label ≥ max(findings, evidence); previous PUBLISHED
      version → SUPERSEDED in the same transaction
    event: EVT-ASM-PUBLISHED
  errors:
  - ASSESSMENT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/assessments/{id}/actions/publish
  internal: false
  policy: POL-ASM-PUBLISH
  actors: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return,
    publish, withdraw)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ASM-WITHDRAW
  aggregate: AGG-ASSESSMENT
  bc: BC03
  transitions:
  - from:
    - PUBLISHED
    to: WITHDRAWN
    guard: reason; decisions and products referencing it are notified
    event: EVT-ASM-WITHDRAWN
  errors:
  - ASSESSMENT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/assessments/{id}/actions/withdraw
  internal: false
  policy: POL-ASM-WITHDRAW
  actors: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return,
    publish, withdraw)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ASM-DISCARD
  aggregate: AGG-ASSESSMENT
  bc: BC03
  transitions:
  - from:
    - DRAFT
    to: DISCARDED
    guard: author; reason
    event: EVT-ASM-DISCARDED
  errors:
  - ASSESSMENT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/intelligence/assessments/{id}/actions/discard
  internal: false
  policy: POL-ASM-DISCARD
  actors: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return,
    publish, withdraw)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
