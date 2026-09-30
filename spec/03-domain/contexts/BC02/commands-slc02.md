---
id: CMD-CAT-BC02-SLC02
type: command-catalog
title: Commands — BC02 (SLC-02)
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC02 (SLC-02)

_51 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-SRC-REGISTER | AGG-SOURCE | `POST /api/v1/information/sources` | لا | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-REGISTER | `type!:string name!:LocalizedName owner_org!:urn reliability!:enum(A,B,C,D,E,F) valid_from!:date-time protection_level:integer label!:Label` | EVT-SRC-REGISTERED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SOURCE_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SRC-RATE-RELIABILITY | AGG-SOURCE | `POST /api/v1/information/sources/{id}/actions/rate-reliability` | لا | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-RATE-RELIABILITY | `reliability!:enum(A,B,C,D,E,F) valid_from!:date-time rationale!:string` | EVT-SRC-RELIABILITY-RATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RATING_INVALID, SOURCE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SRC-UPDATE-PROFILE | AGG-SOURCE | `POST /api/v1/information/sources/{id}/actions/update-profile` | لا | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-UPDATE-PROFILE | `name:LocalizedName contact:object` | EVT-SRC-PROFILE-UPDATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SOURCE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SRC-SET-PROTECTION | AGG-SOURCE | `POST /api/v1/information/sources/{id}/actions/set-protection` | لا | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-SET-PROTECTION | `protection_level!:integer second_approver:urn` | EVT-SRC-PROTECTION-CHANGED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, SOURCE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SRC-RECLASSIFY | AGG-SOURCE | `POST /api/v1/information/sources/{id}/actions/reclassify` | لا | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-RECLASSIFY | `label!:Label reason!:string` | EVT-SRC-RECLASSIFIED | AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, IDEMPOTENCY_KEY_REUSED, SOURCE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SRC-SUSPEND | AGG-SOURCE | `POST /api/v1/information/sources/{id}/actions/suspend` | لا | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-SUSPEND | `reason!:string` | EVT-SRC-SUSPENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SOURCE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SRC-REINSTATE | AGG-SOURCE | `POST /api/v1/information/sources/{id}/actions/reinstate` | لا | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-REINSTATE | `—` | EVT-SRC-REINSTATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SOURCE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SRC-RETIRE | AGG-SOURCE | `POST /api/v1/information/sources/{id}/actions/retire` | لا | Analyst (register, rate, profile) · Security Officer (protection, reclassify) | POL-SRC-RETIRE | `reason!:string` | EVT-SRC-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SOURCE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-OBS-RECORD | AGG-OBSERVATION | `POST /api/v1/information/observations` | لا | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-RECORD | `client_id:string source!:urn observer!:urn observed_at!:date-time event_time:FuzzyInterval location!:SpatialEnvelope method!:string measurements:array narrative:LocalizedName attachments:array label!:Label field_session:urn device:urn` | EVT-OBS-RECORDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OBSERVATION_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-OBS-AMEND | AGG-OBSERVATION | `POST /api/v1/information/observations/{id}/actions/amend` | لا | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-AMEND | `changes!:object reason!:string` | EVT-OBS-AMENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OBSERVATION_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-OBS-ATTACH-EVIDENCE | AGG-OBSERVATION | `POST /api/v1/information/observations/{id}/actions/attach-evidence` | لا | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-ATTACH-EVIDENCE | `evidence!:urn` | EVT-OBS-EVIDENCE-ATTACHED | AUTHZ_DENIED, EVIDENCE_INVALID, IDEMPOTENCY_KEY_REUSED, OBSERVATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-OBS-RECLASSIFY | AGG-OBSERVATION | `POST /api/v1/information/observations/{id}/actions/reclassify` | لا | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-RECLASSIFY | `label!:Label reason!:string` | EVT-OBS-RECLASSIFIED | AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, IDEMPOTENCY_KEY_REUSED, OBSERVATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-OBS-VALIDATE | AGG-OBSERVATION | `POST /api/v1/information/observations/{id}/actions/validate` | لا | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-VALIDATE | `note:string` | EVT-OBS-VALIDATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OBSERVATION_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-OBS-REJECT | AGG-OBSERVATION | `POST /api/v1/information/observations/{id}/actions/reject` | لا | Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject) | POL-OBS-REJECT | `reason!:string` | EVT-OBS-REJECTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OBSERVATION_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ENT-REGISTER | AGG-ENTITY | `POST /api/v1/information/entities` | لا | Analyst · adapter service account | POL-ENT-REGISTER | `entity_type!:string label!:Label initial_claims:array external_ids:array` | EVT-ENT-REGISTERED | AUTHZ_DENIED, ENTITY_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ENT-CHANGE-TYPE | AGG-ENTITY | `POST /api/v1/information/entities/{id}/actions/change-type` | لا | Analyst · adapter service account | POL-ENT-CHANGE-TYPE | `entity_type!:string reason!:string` | EVT-ENT-TYPE-CHANGED | AUTHZ_DENIED, ENTITY_INVALID_STATE_TRANSITION, ENTITY_TYPE_INCOMPATIBLE, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ENT-RECLASSIFY | AGG-ENTITY | `POST /api/v1/information/entities/{id}/actions/reclassify` | لا | Analyst · adapter service account | POL-ENT-RECLASSIFY | `label!:Label reason!:string` | EVT-ENT-RECLASSIFIED | AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, ENTITY_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ENT-RETIRE | AGG-ENTITY | `POST /api/v1/information/entities/{id}/actions/retire` | لا | Analyst · adapter service account | POL-ENT-RETIRE | `reason!:string` | EVT-ENT-RETIRED | AUTHZ_DENIED, ENTITY_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ENT-REINSTATE | AGG-ENTITY | `POST /api/v1/information/entities/{id}/actions/reinstate` | لا | Analyst · adapter service account | POL-ENT-REINSTATE | `reason!:string` | EVT-ENT-REINSTATED | AUTHZ_DENIED, ENTITY_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RWE-REGISTER | AGG-REALWORLD-EVENT | `POST /api/v1/information/events` | لا | Analyst · adapter service account | POL-RWE-REGISTER | `event_type!:string label!:Label initial_claims!:array` | EVT-RWE-REGISTERED | AUTHZ_DENIED, EVENT_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RWE-CHANGE-TYPE | AGG-REALWORLD-EVENT | `POST /api/v1/information/events/{id}/actions/change-type` | لا | Analyst · adapter service account | POL-RWE-CHANGE-TYPE | `event_type!:string reason!:string` | EVT-RWE-TYPE-CHANGED | AUTHZ_DENIED, EVENT_TYPE_INCOMPATIBLE, IDEMPOTENCY_KEY_REUSED, REALWORLD_EVENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RWE-RECLASSIFY | AGG-REALWORLD-EVENT | `POST /api/v1/information/events/{id}/actions/reclassify` | لا | Analyst · adapter service account | POL-RWE-RECLASSIFY | `label!:Label reason!:string` | EVT-RWE-RECLASSIFIED | AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, IDEMPOTENCY_KEY_REUSED, REALWORLD_EVENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RWE-RETIRE | AGG-REALWORLD-EVENT | `POST /api/v1/information/events/{id}/actions/retire` | لا | Analyst · adapter service account | POL-RWE-RETIRE | `reason!:string` | EVT-RWE-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REALWORLD_EVENT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RWE-REINSTATE | AGG-REALWORLD-EVENT | `POST /api/v1/information/events/{id}/actions/reinstate` | لا | Analyst · adapter service account | POL-RWE-REINSTATE | `reason!:string` | EVT-RWE-REINSTATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REALWORLD_EVENT_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-REL-REGISTER | AGG-RELATIONSHIP | `POST /api/v1/information/relationships` | لا | Analyst · adapter service account | POL-REL-REGISTER | `relationship_type!:string source_ref!:urn target_ref!:urn valid!:Interval source_refs!:array label!:Label` | EVT-REL-REGISTERED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, RELATIONSHIP_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-REL-RECLASSIFY | AGG-RELATIONSHIP | `POST /api/v1/information/relationships/{id}/actions/reclassify` | لا | Analyst · adapter service account | POL-REL-RECLASSIFY | `label!:Label reason!:string` | EVT-REL-RECLASSIFIED | AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, IDEMPOTENCY_KEY_REUSED, RELATIONSHIP_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-REL-RETIRE | AGG-RELATIONSHIP | `POST /api/v1/information/relationships/{id}/actions/retire` | لا | Analyst · adapter service account | POL-REL-RETIRE | `reason!:string` | EVT-REL-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, RELATIONSHIP_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-REL-REINSTATE | AGG-RELATIONSHIP | `POST /api/v1/information/relationships/{id}/actions/reinstate` | لا | Analyst · adapter service account | POL-REL-REINSTATE | `reason!:string` | EVT-REL-REINSTATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, RELATIONSHIP_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLM-ASSERT | AGG-CLAIM | `POST /api/v1/information/claims` | لا | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-ASSERT | `subject!:urn predicate!:string value!:ClaimValue valid!:Interval source_refs!:array derived_from:array confidence!:Confidence label!:Label` | EVT-CLM-ASSERTED | AUTHZ_DENIED, CLAIM_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLM-CORRECT | AGG-CLAIM | `POST /api/v1/information/claims/{id}/actions/correct` | لا | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-CORRECT | `value!:ClaimValue valid:Interval source_refs!:array confidence!:Confidence reason!:string` | EVT-CLM-CORRECTED | AUTHZ_DENIED, CLAIM_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLM-RECORD-CHANGE | AGG-CLAIM | `POST /api/v1/information/claims/{id}/actions/record-change` | لا | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-RECORD-CHANGE | `t_change!:date-time new_value!:ClaimValue source_refs!:array confidence!:Confidence` | EVT-CLM-CHANGED | AUTHZ_DENIED, CHANGE_TIME_INVALID, CLAIM_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLM-RETRACT | AGG-CLAIM | `POST /api/v1/information/claims/{id}/actions/retract` | لا | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-RETRACT | `reason!:string` | EVT-CLM-RETRACTED | AUTHZ_DENIED, CLAIM_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLM-ASSESS | AGG-CLAIM | `POST /api/v1/information/claims/{id}/actions/assess` | لا | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-ASSESS | `information_confidence:enum(1,2,3,4,5,6) verification_status:enum(UNVERIFIED,PARTIALLY_VERIFIED,VERIFIED,DISPUTED,REFUTED) rationale!:string` | EVT-CLM-ASSESSED | ASSESSMENT_INVALID, AUTHZ_DENIED, CLAIM_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLM-RECLASSIFY | AGG-CLAIM | `POST /api/v1/information/claims/{id}/actions/reclassify` | لا | Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract) | POL-CLM-RECLASSIFY | `label!:Label reason!:string` | EVT-CLM-RECLASSIFIED | AUTHZ_DENIED, CLAIM_INVALID_STATE_TRANSITION, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVD-REGISTER | AGG-EVIDENCE | `POST /api/v1/information/evidence` | لا | Analyst · Field User (register) · custodian role (custody) | POL-EVD-REGISTER | `client_id:string evidence_type!:string attachment:urn observation_ref:urn locator:object source!:urn collected_at!:date-time label!:Label` | EVT-EVD-REGISTERED | AUTHZ_DENIED, EVIDENCE_INVALID, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVD-UPDATE-LOCATOR | AGG-EVIDENCE | `POST /api/v1/information/evidence/{id}/actions/update-locator` | لا | Analyst · Field User (register) · custodian role (custody) | POL-EVD-UPDATE-LOCATOR | `locator!:object` | EVT-EVD-LOCATOR-UPDATED | AUTHZ_DENIED, EVIDENCE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, LOCATOR_INVALID, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVD-SEAL | AGG-EVIDENCE | `POST /api/v1/information/evidence/{id}/actions/seal` | لا | Analyst · Field User (register) · custodian role (custody) | POL-EVD-SEAL | `—` | EVT-EVD-SEALED | AUTHZ_DENIED, EVIDENCE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVD-TRANSFER-CUSTODY | AGG-EVIDENCE | `POST /api/v1/information/evidence/{id}/actions/transfer-custody` | لا | Analyst · Field User (register) · custodian role (custody) | POL-EVD-TRANSFER-CUSTODY | `new_holder!:urn action!:string` | EVT-EVD-CUSTODY-TRANSFERRED | AUTHZ_DENIED, CUSTODY_INVALID, EVIDENCE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVD-RECLASSIFY | AGG-EVIDENCE | `POST /api/v1/information/evidence/{id}/actions/reclassify` | لا | Analyst · Field User (register) · custodian role (custody) | POL-EVD-RECLASSIFY | `label!:Label reason!:string` | EVT-EVD-RECLASSIFIED | AUTHZ_DENIED, CLASSIFICATION_CHANGE_NOT_AUTHORIZED, EVIDENCE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVD-WITHDRAW | AGG-EVIDENCE | `POST /api/v1/information/evidence/{id}/actions/withdraw` | لا | Analyst · Field User (register) · custodian role (custody) | POL-EVD-WITHDRAW | `reason!:string` | EVT-EVD-WITHDRAWN | AUTHZ_DENIED, EVIDENCE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVL-LINK | AGG-EVIDENCE-LINK | `POST /api/v1/information/evidence-links` | لا | Analyst | POL-EVL-LINK | `evidence!:urn claim!:urn stance!:enum(SUPPORTS,REFUTES,CONTEXT) note:string` | EVT-EVL-LINKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LINK_DUPLICATE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EVL-UNLINK | AGG-EVIDENCE-LINK | `POST /api/v1/information/evidence-links/{id}/actions/unlink` | لا | Analyst | POL-EVL-UNLINK | `reason!:string` | EVT-EVL-UNLINKED | AUTHZ_DENIED, EVIDENCE_LINK_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ATT-INITIATE-UPLOAD | AGG-ATTACHMENT | `POST /api/v1/information/attachments` | لا | user with write permission on the target object | POL-ATT-INITIATE-UPLOAD | `client_id:string sha256!:string size_bytes!:integer mime_type!:string file_name:string label!:Label` | EVT-ATT-UPLOAD-INITIATED | ATTACHMENT_REJECTED, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ATT-COMPLETE-UPLOAD | AGG-ATTACHMENT | `POST /api/v1/information/attachments/{id}/actions/complete-upload` | لا | user with write permission on the target object | POL-ATT-COMPLETE-UPLOAD | `—` | EVT-ATT-UPLOADED | ATTACHMENT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, HASH_MISMATCH, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ATT-ERASE | AGG-ATTACHMENT | `POST /api/v1/information/attachments/{id}/actions/erase` | لا | user with write permission on the target object | POL-ATT-ERASE | `erasure_order_ref!:string` | EVT-ATT-ERASED | ATTACHMENT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LEGAL_HOLD_ACTIVE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-IMP-SUBMIT | AGG-IMPORT-BATCH | `POST /api/v1/information/import-batches` | لا | adapter service account · Administrator | POL-IMP-SUBMIT | `adapter!:urn batch_key!:string content_sha256!:string format!:string payload_attachment!:urn` | EVT-IMP-RECEIVED | AUTHZ_DENIED, BATCH_KEY_REUSED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-IMP-REPROCESS-QUARANTINE | AGG-IMPORT-BATCH | `POST /api/v1/information/import-batches/{id}/actions/reprocess-quarantine` | لا | adapter service account · Administrator | POL-IMP-REPROCESS-QUARANTINE | `mapping_version:string corrections:array` | EVT-IMP-REPROCESSING | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, IMPORT_BATCH_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-IMP-ACCEPT-QUARANTINE | AGG-IMPORT-BATCH | `POST /api/v1/information/import-batches/{id}/actions/accept-quarantine` | لا | adapter service account · Administrator | POL-IMP-ACCEPT-QUARANTINE | `reason!:string` | EVT-IMP-QUARANTINE-ACCEPTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, IMPORT_BATCH_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-IMP-CANCEL | AGG-IMPORT-BATCH | `POST /api/v1/information/import-batches/{id}/actions/cancel` | لا | adapter service account · Administrator | POL-IMP-CANCEL | `reason!:string` | EVT-IMP-CANCELLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, IMPORT_BATCH_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EXT-MAP | AGG-EXTERNAL-ID | `POST /api/v1/information/external-ids` | لا | adapter service account · Analyst | POL-EXT-MAP | `system!:string external_id!:string object!:urn valid_from!:date-time` | EVT-EXT-MAPPED | AUTHZ_DENIED, EXTERNAL_ID_TAKEN, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-EXT-END | AGG-EXTERNAL-ID | `POST /api/v1/information/external-ids/{id}/actions/end` | لا | adapter service account · Analyst | POL-EXT-END | `valid_to!:date-time reason!:string` | EVT-EXT-ENDED | AUTHZ_DENIED, EXTERNAL_ID_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-SRC-REGISTER
  aggregate: AGG-SOURCE
  bc: BC02
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: type in RD-SOURCE-TYPES; initial reliability A–F; person-type sources get
      protection_level ≥ 1 and label ≥ tenant default + 1 rank
    event: EVT-SRC-REGISTERED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SOURCE_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/sources
  internal: false
  policy: POL-SRC-REGISTER
  actors: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  payload: type!:string name!:LocalizedName owner_org!:urn reliability!:enum(A,B,C,D,E,F)
    valid_from!:date-time protection_level:integer label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-SRC-RATE-RELIABILITY
  aggregate: AGG-SOURCE
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: '='
    guard: rating ∈ A–F; valid_from given; creates bitemporal reliability claim
    event: EVT-SRC-RELIABILITY-RATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RATING_INVALID
  - SOURCE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/sources/{id}/actions/rate-reliability
  internal: false
  policy: POL-SRC-RATE-RELIABILITY
  actors: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  payload: reliability!:enum(A,B,C,D,E,F) valid_from!:date-time rationale!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SRC-UPDATE-PROFILE
  aggregate: AGG-SOURCE
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: '='
    guard: —
    event: EVT-SRC-PROFILE-UPDATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SOURCE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/sources/{id}/actions/update-profile
  internal: false
  policy: POL-SRC-UPDATE-PROFILE
  actors: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  payload: name:LocalizedName contact:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SRC-SET-PROTECTION
  aggregate: AGG-SOURCE
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: '='
    guard: Security Officer; decreasing protection requires a second Security Officer
    event: EVT-SRC-PROTECTION-CHANGED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - SOURCE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/sources/{id}/actions/set-protection
  internal: false
  policy: POL-SRC-SET-PROTECTION
  actors: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  payload: protection_level!:integer second_approver:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SRC-RECLASSIFY
  aggregate: AGG-SOURCE
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: '='
    guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
    event: EVT-SRC-RECLASSIFIED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - IDEMPOTENCY_KEY_REUSED
  - SOURCE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/sources/{id}/actions/reclassify
  internal: false
  policy: POL-SRC-RECLASSIFY
  actors: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SRC-SUSPEND
  aggregate: AGG-SOURCE
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    to: SUSPENDED
    guard: reason
    event: EVT-SRC-SUSPENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SOURCE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/sources/{id}/actions/suspend
  internal: false
  policy: POL-SRC-SUSPEND
  actors: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SRC-REINSTATE
  aggregate: AGG-SOURCE
  bc: BC02
  transitions:
  - from:
    - SUSPENDED
    to: ACTIVE
    guard: —
    event: EVT-SRC-REINSTATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SOURCE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/sources/{id}/actions/reinstate
  internal: false
  policy: POL-SRC-REINSTATE
  actors: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SRC-RETIRE
  aggregate: AGG-SOURCE
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: RETIRED
    guard: reason; history retained
    event: EVT-SRC-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SOURCE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/sources/{id}/actions/retire
  internal: false
  policy: POL-SRC-RETIRE
  actors: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-OBS-RECORD
  aggregate: AGG-OBSERVATION
  bc: BC02
  transitions:
  - from:
    - ∅
    to: RECORDED
    guard: source ACTIVE; location with CRS + accuracy + valid geometry; UCUM units;
      observed_at ≤ server time + 5 min; recorded_from by server
    event: EVT-OBS-RECORDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OBSERVATION_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/observations
  internal: false
  policy: POL-OBS-RECORD
  actors: Field User / Operator / Analyst / adapter service account (record) · Analyst
    (validate, reject)
  payload: client_id:string source!:urn observer!:urn observed_at!:date-time event_time:FuzzyInterval
    location!:SpatialEnvelope method!:string measurements:array narrative:LocalizedName
    attachments:array label!:Label field_session:urn device:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-OBS-AMEND
  aggregate: AGG-OBSERVATION
  bc: BC02
  transitions:
  - from:
    - RECORDED
    to: '='
    guard: actor = observer or Analyst; new version; reason
    event: EVT-OBS-AMENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OBSERVATION_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/observations/{id}/actions/amend
  internal: false
  policy: POL-OBS-AMEND
  actors: Field User / Operator / Analyst / adapter service account (record) · Analyst
    (validate, reject)
  payload: changes!:object reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-OBS-ATTACH-EVIDENCE
  aggregate: AGG-OBSERVATION
  bc: BC02
  transitions:
  - from:
    - RECORDED
    to: '='
    guard: evidence REGISTERED or SEALED
    event: EVT-OBS-EVIDENCE-ATTACHED
  errors:
  - AUTHZ_DENIED
  - EVIDENCE_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - OBSERVATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/observations/{id}/actions/attach-evidence
  internal: false
  policy: POL-OBS-ATTACH-EVIDENCE
  actors: Field User / Operator / Analyst / adapter service account (record) · Analyst
    (validate, reject)
  payload: evidence!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-OBS-RECLASSIFY
  aggregate: AGG-OBSERVATION
  bc: BC02
  transitions:
  - from:
    - RECORDED
    - VALIDATED
    - REJECTED
    to: '='
    guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
    event: EVT-OBS-RECLASSIFIED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - IDEMPOTENCY_KEY_REUSED
  - OBSERVATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/observations/{id}/actions/reclassify
  internal: false
  policy: POL-OBS-RECLASSIFY
  actors: Field User / Operator / Analyst / adapter service account (record) · Analyst
    (validate, reject)
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-OBS-VALIDATE
  aggregate: AGG-OBSERVATION
  bc: BC02
  transitions:
  - from:
    - RECORDED
    to: VALIDATED
    guard: Analyst ≠ observer, or system auto-validation for sensor sources rated
      A/B under tenant policy
    event: EVT-OBS-VALIDATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OBSERVATION_INVALID_STATE_TRANSITION
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/observations/{id}/actions/validate
  internal: false
  policy: POL-OBS-VALIDATE
  actors: Field User / Operator / Analyst / adapter service account (record) · Analyst
    (validate, reject)
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-OBS-REJECT
  aggregate: AGG-OBSERVATION
  bc: BC02
  transitions:
  - from:
    - RECORDED
    to: REJECTED
    guard: reason
    event: EVT-OBS-REJECTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OBSERVATION_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/observations/{id}/actions/reject
  internal: false
  policy: POL-OBS-REJECT
  actors: Field User / Operator / Analyst / adapter service account (record) · Analyst
    (validate, reject)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ENT-REGISTER
  aggregate: AGG-ENTITY
  bc: BC02
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: type in RD-ENTITY-TYPES; each initial claim valid as CMD-CLM-ASSERT; Entity
      + initial Claims created in one unit of work
    event: EVT-ENT-REGISTERED
  errors:
  - AUTHZ_DENIED
  - ENTITY_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/entities
  internal: false
  policy: POL-ENT-REGISTER
  actors: Analyst · adapter service account
  payload: entity_type!:string label!:Label initial_claims:array external_ids:array
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ENT-CHANGE-TYPE
  aggregate: AGG-ENTITY
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: compatible type per RD-ENTITY-TYPES; new version; reason
    event: EVT-ENT-TYPE-CHANGED
  errors:
  - AUTHZ_DENIED
  - ENTITY_INVALID_STATE_TRANSITION
  - ENTITY_TYPE_INCOMPATIBLE
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/entities/{id}/actions/change-type
  internal: false
  policy: POL-ENT-CHANGE-TYPE
  actors: Analyst · adapter service account
  payload: entity_type!:string reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ENT-RECLASSIFY
  aggregate: AGG-ENTITY
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    - RETIRED
    to: '='
    guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
    event: EVT-ENT-RECLASSIFIED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - ENTITY_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/entities/{id}/actions/reclassify
  internal: false
  policy: POL-ENT-RECLASSIFY
  actors: Analyst · adapter service account
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ENT-RETIRE
  aggregate: AGG-ENTITY
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    to: RETIRED
    guard: reason (created in error / no longer tracked); claims untouched
    event: EVT-ENT-RETIRED
  errors:
  - AUTHZ_DENIED
  - ENTITY_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/entities/{id}/actions/retire
  internal: false
  policy: POL-ENT-RETIRE
  actors: Analyst · adapter service account
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ENT-REINSTATE
  aggregate: AGG-ENTITY
  bc: BC02
  transitions:
  - from:
    - RETIRED
    to: ACTIVE
    guard: reason
    event: EVT-ENT-REINSTATED
  errors:
  - AUTHZ_DENIED
  - ENTITY_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/entities/{id}/actions/reinstate
  internal: false
  policy: POL-ENT-REINSTATE
  actors: Analyst · adapter service account
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RWE-REGISTER
  aggregate: AGG-REALWORLD-EVENT
  bc: BC02
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: type in RD-EVENT-TYPES; initial claims include event_time (fuzzy) and location
    event: EVT-RWE-REGISTERED
  errors:
  - AUTHZ_DENIED
  - EVENT_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/events
  internal: false
  policy: POL-RWE-REGISTER
  actors: Analyst · adapter service account
  payload: event_type!:string label!:Label initial_claims!:array
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-RWE-CHANGE-TYPE
  aggregate: AGG-REALWORLD-EVENT
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: compatible type; reason
    event: EVT-RWE-TYPE-CHANGED
  errors:
  - AUTHZ_DENIED
  - EVENT_TYPE_INCOMPATIBLE
  - IDEMPOTENCY_KEY_REUSED
  - REALWORLD_EVENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/events/{id}/actions/change-type
  internal: false
  policy: POL-RWE-CHANGE-TYPE
  actors: Analyst · adapter service account
  payload: event_type!:string reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RWE-RECLASSIFY
  aggregate: AGG-REALWORLD-EVENT
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    - RETIRED
    to: '='
    guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
    event: EVT-RWE-RECLASSIFIED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - IDEMPOTENCY_KEY_REUSED
  - REALWORLD_EVENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/events/{id}/actions/reclassify
  internal: false
  policy: POL-RWE-RECLASSIFY
  actors: Analyst · adapter service account
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RWE-RETIRE
  aggregate: AGG-REALWORLD-EVENT
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    to: RETIRED
    guard: reason
    event: EVT-RWE-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REALWORLD_EVENT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/events/{id}/actions/retire
  internal: false
  policy: POL-RWE-RETIRE
  actors: Analyst · adapter service account
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RWE-REINSTATE
  aggregate: AGG-REALWORLD-EVENT
  bc: BC02
  transitions:
  - from:
    - RETIRED
    to: ACTIVE
    guard: reason
    event: EVT-RWE-REINSTATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REALWORLD_EVENT_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/events/{id}/actions/reinstate
  internal: false
  policy: POL-RWE-REINSTATE
  actors: Analyst · adapter service account
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-REL-REGISTER
  aggregate: AGG-RELATIONSHIP
  bc: BC02
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: type in RD-RELATIONSHIP-TYPES; endpoint types allowed; creates identity
      + existence claim (valid interval, sources ≥ 1)
    event: EVT-REL-REGISTERED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - RELATIONSHIP_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/relationships
  internal: false
  policy: POL-REL-REGISTER
  actors: Analyst · adapter service account
  payload: relationship_type!:string source_ref!:urn target_ref!:urn valid!:Interval
    source_refs!:array label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-REL-RECLASSIFY
  aggregate: AGG-RELATIONSHIP
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    - RETIRED
    to: '='
    guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
    event: EVT-REL-RECLASSIFIED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - IDEMPOTENCY_KEY_REUSED
  - RELATIONSHIP_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/relationships/{id}/actions/reclassify
  internal: false
  policy: POL-REL-RECLASSIFY
  actors: Analyst · adapter service account
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-REL-RETIRE
  aggregate: AGG-RELATIONSHIP
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    to: RETIRED
    guard: created in error only; ending in reality = CMD-CLM-RECORD-CHANGE on the
      existence claim
    event: EVT-REL-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - RELATIONSHIP_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/relationships/{id}/actions/retire
  internal: false
  policy: POL-REL-RETIRE
  actors: Analyst · adapter service account
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-REL-REINSTATE
  aggregate: AGG-RELATIONSHIP
  bc: BC02
  transitions:
  - from:
    - RETIRED
    to: ACTIVE
    guard: reason
    event: EVT-REL-REINSTATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - RELATIONSHIP_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/relationships/{id}/actions/reinstate
  internal: false
  policy: POL-REL-REINSTATE
  actors: Analyst · adapter service account
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLM-ASSERT
  aggregate: AGG-CLAIM
  bc: BC02
  transitions:
  - from:
    - ∅
    to: CURRENT
    guard: subject exists; predicate in RD-PREDICATES; value matches predicate type/unit/cardinality;
      ≥ 1 source, all ACTIVE; valid_from < valid_to; geometry rules; confidence dims
      valid
    event: EVT-CLM-ASSERTED
  errors:
  - AUTHZ_DENIED
  - CLAIM_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/claims
  internal: false
  policy: POL-CLM-ASSERT
  actors: Analyst · adapter service account · analysis-run identity (assert) · Analyst
    or verification re-evaluator system identity (assess) · Analyst (correct, change,
    retract)
  payload: subject!:urn predicate!:string value!:ClaimValue valid!:Interval source_refs!:array
    derived_from:array confidence!:Confidence label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CLM-CORRECT
  aggregate: AGG-CLAIM
  bc: BC02
  transitions:
  - from:
    - CURRENT
    to: CLOSED
    guard: closes recorded_to = now and asserts the replacement (same subject/predicate)
      in the same transaction; reason
    event: EVT-CLM-CORRECTED
  errors:
  - AUTHZ_DENIED
  - CLAIM_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/claims/{id}/actions/correct
  internal: false
  policy: POL-CLM-CORRECT
  actors: Analyst · adapter service account · analysis-run identity (assert) · Analyst
    or verification re-evaluator system identity (assess) · Analyst (correct, change,
    retract)
  payload: value!:ClaimValue valid:Interval source_refs!:array confidence!:Confidence
    reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLM-RECORD-CHANGE
  aggregate: AGG-CLAIM
  bc: BC02
  transitions:
  - from:
    - CURRENT
    to: CLOSED
    guard: 't_change ∈ (valid_from, valid_to): closes record, re-records old value
      with valid_to = t_change, asserts new value from t_change'
    event: EVT-CLM-CHANGED
  errors:
  - AUTHZ_DENIED
  - CHANGE_TIME_INVALID
  - CLAIM_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/claims/{id}/actions/record-change
  internal: false
  policy: POL-CLM-RECORD-CHANGE
  actors: Analyst · adapter service account · analysis-run identity (assert) · Analyst
    or verification re-evaluator system identity (assess) · Analyst (correct, change,
    retract)
  payload: t_change!:date-time new_value!:ClaimValue source_refs!:array confidence!:Confidence
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLM-RETRACT
  aggregate: AGG-CLAIM
  bc: BC02
  transitions:
  - from:
    - CURRENT
    to: CLOSED
    guard: reason; no replacement
    event: EVT-CLM-RETRACTED
  errors:
  - AUTHZ_DENIED
  - CLAIM_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/claims/{id}/actions/retract
  internal: false
  policy: POL-CLM-RETRACT
  actors: Analyst · adapter service account · analysis-run identity (assert) · Analyst
    or verification re-evaluator system identity (assess) · Analyst (correct, change,
    retract)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLM-ASSESS
  aggregate: AGG-CLAIM
  bc: BC02
  transitions:
  - from:
    - CURRENT
    to: '='
    guard: updates information_confidence / verification_status only (T2 versioned
      assessment); value and times untouched
    event: EVT-CLM-ASSESSED
  errors:
  - ASSESSMENT_INVALID
  - AUTHZ_DENIED
  - CLAIM_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/claims/{id}/actions/assess
  internal: false
  policy: POL-CLM-ASSESS
  actors: Analyst · adapter service account · analysis-run identity (assert) · Analyst
    or verification re-evaluator system identity (assess) · Analyst (correct, change,
    retract)
  payload: information_confidence:enum(1,2,3,4,5,6) verification_status:enum(UNVERIFIED,PARTIALLY_VERIFIED,VERIFIED,DISPUTED,REFUTED)
    rationale!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLM-RECLASSIFY
  aggregate: AGG-CLAIM
  bc: BC02
  transitions:
  - from:
    - CURRENT
    - CLOSED
    to: '='
    guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
    event: EVT-CLM-RECLASSIFIED
  errors:
  - AUTHZ_DENIED
  - CLAIM_INVALID_STATE_TRANSITION
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/claims/{id}/actions/reclassify
  internal: false
  policy: POL-CLM-RECLASSIFY
  actors: Analyst · adapter service account · analysis-run identity (assert) · Analyst
    or verification re-evaluator system identity (assess) · Analyst (correct, change,
    retract)
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EVD-REGISTER
  aggregate: AGG-EVIDENCE
  bc: BC02
  transitions:
  - from:
    - ∅
    to: REGISTERED
    guard: attachment STORED or observation_ref; type in RD-EVIDENCE-TYPES; source
      ACTIVE
    event: EVT-EVD-REGISTERED
  errors:
  - AUTHZ_DENIED
  - EVIDENCE_INVALID
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/evidence
  internal: false
  policy: POL-EVD-REGISTER
  actors: Analyst · Field User (register) · custodian role (custody)
  payload: client_id:string evidence_type!:string attachment:urn observation_ref:urn
    locator:object source!:urn collected_at!:date-time label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-EVD-UPDATE-LOCATOR
  aggregate: AGG-EVIDENCE
  bc: BC02
  transitions:
  - from:
    - REGISTERED
    to: '='
    guard: locator within attachment bounds
    event: EVT-EVD-LOCATOR-UPDATED
  errors:
  - AUTHZ_DENIED
  - EVIDENCE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - LOCATOR_INVALID
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/evidence/{id}/actions/update-locator
  internal: false
  policy: POL-EVD-UPDATE-LOCATOR
  actors: Analyst · Field User (register) · custodian role (custody)
  payload: locator!:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EVD-SEAL
  aggregate: AGG-EVIDENCE
  bc: BC02
  transitions:
  - from:
    - REGISTERED
    to: SEALED
    guard: integrity hash over metadata + attachment hash
    event: EVT-EVD-SEALED
  errors:
  - AUTHZ_DENIED
  - EVIDENCE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/evidence/{id}/actions/seal
  internal: false
  policy: POL-EVD-SEAL
  actors: Analyst · Field User (register) · custodian role (custody)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EVD-TRANSFER-CUSTODY
  aggregate: AGG-EVIDENCE
  bc: BC02
  transitions:
  - from:
    - REGISTERED
    - SEALED
    to: '='
    guard: actor is current holder or custodian role; new holder named
    event: EVT-EVD-CUSTODY-TRANSFERRED
  errors:
  - AUTHZ_DENIED
  - CUSTODY_INVALID
  - EVIDENCE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/evidence/{id}/actions/transfer-custody
  internal: false
  policy: POL-EVD-TRANSFER-CUSTODY
  actors: Analyst · Field User (register) · custodian role (custody)
  payload: new_holder!:urn action!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EVD-RECLASSIFY
  aggregate: AGG-EVIDENCE
  bc: BC02
  transitions:
  - from:
    - REGISTERED
    - SEALED
    - WITHDRAWN
    to: '='
    guard: authority per tenant policy (REQ-GOV-004); new version; bumps object security_version
    event: EVT-EVD-RECLASSIFIED
  errors:
  - AUTHZ_DENIED
  - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
  - EVIDENCE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/evidence/{id}/actions/reclassify
  internal: false
  policy: POL-EVD-RECLASSIFY
  actors: Analyst · Field User (register) · custodian role (custody)
  payload: label!:Label reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EVD-WITHDRAW
  aggregate: AGG-EVIDENCE
  bc: BC02
  transitions:
  - from:
    - REGISTERED
    - SEALED
    to: WITHDRAWN
    guard: reason (e.g. forged); links kept and flagged; dependent verification re-evaluated
    event: EVT-EVD-WITHDRAWN
  errors:
  - AUTHZ_DENIED
  - EVIDENCE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/evidence/{id}/actions/withdraw
  internal: false
  policy: POL-EVD-WITHDRAW
  actors: Analyst · Field User (register) · custodian role (custody)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EVL-LINK
  aggregate: AGG-EVIDENCE-LINK
  bc: BC02
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: evidence not WITHDRAWN; claim exists; stance ∈ {SUPPORTS, REFUTES, CONTEXT};
      no ACTIVE duplicate (evidence, claim, stance)
    event: EVT-EVL-LINKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LINK_DUPLICATE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/evidence-links
  internal: false
  policy: POL-EVL-LINK
  actors: Analyst
  payload: evidence!:urn claim!:urn stance!:enum(SUPPORTS,REFUTES,CONTEXT) note:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-EVL-UNLINK
  aggregate: AGG-EVIDENCE-LINK
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    to: REMOVED
    guard: reason; recorded_to closed
    event: EVT-EVL-UNLINKED
  errors:
  - AUTHZ_DENIED
  - EVIDENCE_LINK_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/evidence-links/{id}/actions/unlink
  internal: false
  policy: POL-EVL-UNLINK
  actors: Analyst
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ATT-INITIATE-UPLOAD
  aggregate: AGG-ATTACHMENT
  bc: BC02
  transitions:
  - from:
    - ∅
    to: PENDING
    guard: size ≤ tenant limit; mime allowed; returns direct upload target (≤ 5 min);
      same sha256 already STORED in tenant → returns existing
    event: EVT-ATT-UPLOAD-INITIATED
  errors:
  - ATTACHMENT_REJECTED
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/attachments
  internal: false
  policy: POL-ATT-INITIATE-UPLOAD
  actors: user with write permission on the target object
  payload: client_id:string sha256!:string size_bytes!:integer mime_type!:string file_name:string
    label!:Label
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ATT-COMPLETE-UPLOAD
  aggregate: AGG-ATTACHMENT
  bc: BC02
  transitions:
  - from:
    - PENDING
    to: SCANNING
    guard: stored bytes hash = declared sha256; size matches
    event: EVT-ATT-UPLOADED
  errors:
  - ATTACHMENT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - HASH_MISMATCH
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/attachments/{id}/actions/complete-upload
  internal: false
  policy: POL-ATT-COMPLETE-UPLOAD
  actors: user with write permission on the target object
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ATT-ERASE
  aggregate: AGG-ATTACHMENT
  bc: BC02
  transitions:
  - from:
    - STORED
    to: ERASED
    guard: erasure order or disposition; no legal hold; key destroyed (ADR-P08)
    event: EVT-ATT-ERASED
  errors:
  - ATTACHMENT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LEGAL_HOLD_ACTIVE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/attachments/{id}/actions/erase
  internal: false
  policy: POL-ATT-ERASE
  actors: user with write permission on the target object
  payload: erasure_order_ref!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-IMP-SUBMIT
  aggregate: AGG-IMPORT-BATCH
  bc: BC02
  transitions:
  - from:
    - ∅
    to: RECEIVED
    guard: 'adapter ACTIVE (or authorized manual import); batch_key unique per adapter:
      same key + same content hash returns the existing batch; different hash → rejected'
    event: EVT-IMP-RECEIVED
  errors:
  - AUTHZ_DENIED
  - BATCH_KEY_REUSED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/import-batches
  internal: false
  policy: POL-IMP-SUBMIT
  actors: adapter service account · Administrator
  payload: adapter!:urn batch_key!:string content_sha256!:string format!:string payload_attachment!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-IMP-REPROCESS-QUARANTINE
  aggregate: AGG-IMPORT-BATCH
  bc: BC02
  transitions:
  - from:
    - COMPLETED_WITH_QUARANTINE
    to: PROCESSING
    guard: new mapping version or corrected records
    event: EVT-IMP-REPROCESSING
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - IMPORT_BATCH_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/import-batches/{id}/actions/reprocess-quarantine
  internal: false
  policy: POL-IMP-REPROCESS-QUARANTINE
  actors: adapter service account · Administrator
  payload: mapping_version:string corrections:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-IMP-ACCEPT-QUARANTINE
  aggregate: AGG-IMPORT-BATCH
  bc: BC02
  transitions:
  - from:
    - COMPLETED_WITH_QUARANTINE
    to: COMPLETED
    guard: reason; quarantined records dropped, record kept
    event: EVT-IMP-QUARANTINE-ACCEPTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - IMPORT_BATCH_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/import-batches/{id}/actions/accept-quarantine
  internal: false
  policy: POL-IMP-ACCEPT-QUARANTINE
  actors: adapter service account · Administrator
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-IMP-CANCEL
  aggregate: AGG-IMPORT-BATCH
  bc: BC02
  transitions:
  - from:
    - RECEIVED
    to: CANCELLED
    guard: reason
    event: EVT-IMP-CANCELLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - IMPORT_BATCH_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/import-batches/{id}/actions/cancel
  internal: false
  policy: POL-IMP-CANCEL
  actors: adapter service account · Administrator
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-EXT-MAP
  aggregate: AGG-EXTERNAL-ID
  bc: BC02
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: (system, external_id) has no ACTIVE mapping; target exists
    event: EVT-EXT-MAPPED
  errors:
  - AUTHZ_DENIED
  - EXTERNAL_ID_TAKEN
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/information/external-ids
  internal: false
  policy: POL-EXT-MAP
  actors: adapter service account · Analyst
  payload: system!:string external_id!:string object!:urn valid_from!:date-time
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-EXT-END
  aggregate: AGG-EXTERNAL-ID
  bc: BC02
  transitions:
  - from:
    - ACTIVE
    to: ENDED
    guard: reason; valid_to set
    event: EVT-EXT-ENDED
  errors:
  - AUTHZ_DENIED
  - EXTERNAL_ID_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/information/external-ids/{id}/actions/end
  internal: false
  policy: POL-EXT-END
  actors: adapter service account · Analyst
  payload: valid_to!:date-time reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
