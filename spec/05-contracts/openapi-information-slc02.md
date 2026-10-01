---
id: OPENAPI-BC02-SLC02
type: api-contract
title: Information API (BC02) — SLC-02
wave: W6
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: OpenAPI 3.1 (validated)
traces:
  decided_by:
  - CR-40
  - REQ-PLT-007
  - REQ-PLT-008
  - REQ-PLT-009
---

# Information API (BC02) — SLC-02

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_66 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/information/sources` | CMD-SRC-REGISTER |
| POST | `/api/v1/information/sources/{id}/actions/rate-reliability` | CMD-SRC-RATE-RELIABILITY |
| POST | `/api/v1/information/sources/{id}/actions/update-profile` | CMD-SRC-UPDATE-PROFILE |
| POST | `/api/v1/information/sources/{id}/actions/set-protection` | CMD-SRC-SET-PROTECTION |
| POST | `/api/v1/information/sources/{id}/actions/reclassify` | CMD-SRC-RECLASSIFY |
| POST | `/api/v1/information/sources/{id}/actions/suspend` | CMD-SRC-SUSPEND |
| POST | `/api/v1/information/sources/{id}/actions/reinstate` | CMD-SRC-REINSTATE |
| POST | `/api/v1/information/sources/{id}/actions/retire` | CMD-SRC-RETIRE |
| POST | `/api/v1/information/observations` | CMD-OBS-RECORD |
| GET | `/api/v1/information/observations` | QRY-OBS-LIST |
| POST | `/api/v1/information/observations/{id}/actions/amend` | CMD-OBS-AMEND |
| POST | `/api/v1/information/observations/{id}/actions/attach-evidence` | CMD-OBS-ATTACH-EVIDENCE |
| POST | `/api/v1/information/observations/{id}/actions/reclassify` | CMD-OBS-RECLASSIFY |
| POST | `/api/v1/information/observations/{id}/actions/validate` | CMD-OBS-VALIDATE |
| POST | `/api/v1/information/observations/{id}/actions/reject` | CMD-OBS-REJECT |
| POST | `/api/v1/information/entities` | CMD-ENT-REGISTER |
| GET | `/api/v1/information/entities` | QRY-ENT-LIST |
| POST | `/api/v1/information/entities/{id}/actions/change-type` | CMD-ENT-CHANGE-TYPE |
| POST | `/api/v1/information/entities/{id}/actions/reclassify` | CMD-ENT-RECLASSIFY |
| POST | `/api/v1/information/entities/{id}/actions/retire` | CMD-ENT-RETIRE |
| POST | `/api/v1/information/entities/{id}/actions/reinstate` | CMD-ENT-REINSTATE |
| POST | `/api/v1/information/events` | CMD-RWE-REGISTER |
| POST | `/api/v1/information/events/{id}/actions/change-type` | CMD-RWE-CHANGE-TYPE |
| POST | `/api/v1/information/events/{id}/actions/reclassify` | CMD-RWE-RECLASSIFY |
| POST | `/api/v1/information/events/{id}/actions/retire` | CMD-RWE-RETIRE |
| POST | `/api/v1/information/events/{id}/actions/reinstate` | CMD-RWE-REINSTATE |
| POST | `/api/v1/information/relationships` | CMD-REL-REGISTER |
| POST | `/api/v1/information/relationships/{id}/actions/reclassify` | CMD-REL-RECLASSIFY |
| POST | `/api/v1/information/relationships/{id}/actions/retire` | CMD-REL-RETIRE |
| POST | `/api/v1/information/relationships/{id}/actions/reinstate` | CMD-REL-REINSTATE |
| POST | `/api/v1/information/claims` | CMD-CLM-ASSERT |
| POST | `/api/v1/information/claims/{id}/actions/correct` | CMD-CLM-CORRECT |
| POST | `/api/v1/information/claims/{id}/actions/record-change` | CMD-CLM-RECORD-CHANGE |
| POST | `/api/v1/information/claims/{id}/actions/retract` | CMD-CLM-RETRACT |
| POST | `/api/v1/information/claims/{id}/actions/assess` | CMD-CLM-ASSESS |
| POST | `/api/v1/information/claims/{id}/actions/reclassify` | CMD-CLM-RECLASSIFY |
| POST | `/api/v1/information/evidence` | CMD-EVD-REGISTER |
| POST | `/api/v1/information/evidence/{id}/actions/update-locator` | CMD-EVD-UPDATE-LOCATOR |
| POST | `/api/v1/information/evidence/{id}/actions/seal` | CMD-EVD-SEAL |
| POST | `/api/v1/information/evidence/{id}/actions/transfer-custody` | CMD-EVD-TRANSFER-CUSTODY |
| POST | `/api/v1/information/evidence/{id}/actions/reclassify` | CMD-EVD-RECLASSIFY |
| POST | `/api/v1/information/evidence/{id}/actions/withdraw` | CMD-EVD-WITHDRAW |
| POST | `/api/v1/information/evidence-links` | CMD-EVL-LINK |
| POST | `/api/v1/information/evidence-links/{id}/actions/unlink` | CMD-EVL-UNLINK |
| POST | `/api/v1/information/attachments` | CMD-ATT-INITIATE-UPLOAD |
| POST | `/api/v1/information/attachments/{id}/actions/complete-upload` | CMD-ATT-COMPLETE-UPLOAD |
| POST | `/api/v1/information/attachments/{id}/actions/erase` | CMD-ATT-ERASE |
| POST | `/api/v1/information/import-batches` | CMD-IMP-SUBMIT |
| POST | `/api/v1/information/import-batches/{id}/actions/reprocess-quarantine` | CMD-IMP-REPROCESS-QUARANTINE |
| POST | `/api/v1/information/import-batches/{id}/actions/accept-quarantine` | CMD-IMP-ACCEPT-QUARANTINE |
| POST | `/api/v1/information/import-batches/{id}/actions/cancel` | CMD-IMP-CANCEL |
| POST | `/api/v1/information/external-ids` | CMD-EXT-MAP |
| POST | `/api/v1/information/external-ids/{id}/actions/end` | CMD-EXT-END |
| GET | `/api/v1/information/entities/{entity_id}` | QRY-ENT-RESOLVED |
| GET | `/api/v1/information/entities/{entity_id}/claims` | QRY-ENT-CLAIMS |
| GET | `/api/v1/information/entities/{entity_id}/positions` | QRY-ENT-POSITIONS |
| GET | `/api/v1/information/events/{event_id}` | QRY-RWE-GET |
| GET | `/api/v1/information/entities/{entity_id}/relationships` | QRY-REL-LIST |
| GET | `/api/v1/information/claims/{claim_id}` | QRY-CLM-GET |
| GET | `/api/v1/information/observations/{observation_id}` | QRY-OBS-GET |
| GET | `/api/v1/information/sources/{source_id}` | QRY-SRC-GET |
| GET | `/api/v1/information/evidence/{evidence_id}` | QRY-EVD-GET |
| POST | `/api/v1/information/attachments/{attachment_id}/download-grants` | QRY-ATT-DOWNLOAD |
| GET | `/api/v1/information/lineage/{object_urn}` | QRY-LIN-TRACE |
| GET | `/api/v1/information/external-ids/{system}/{external_id}` | QRY-EXT-RESOLVE |
| GET | `/api/v1/information/import-batches/{batch_id}` | QRY-IMP-GET |

```yaml
openapi: 3.1.0
info:
  title: Information API (BC02) — SLC-02
  version: 1.0.0
  description: Generated from SLC-02 domain specification. Do not edit by hand.
servers:
- url: https://{cell}.platform.local
  variables:
    cell:
      default: cell-1
security:
- bearer: []
paths:
  /api/v1/information/sources:
    post:
      operationId: CMD-SRC-REGISTER
      summary: CMD-SRC-REGISTER
      x-aggregate: AGG-SOURCE
      x-policy: POL-SRC-REGISTER
      x-events:
      - EVT-SRC-REGISTERED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SOURCE_INVALID
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SrcRegisterCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/sources/{id}/actions/rate-reliability:
    post:
      operationId: CMD-SRC-RATE-RELIABILITY
      summary: CMD-SRC-RATE-RELIABILITY
      x-aggregate: AGG-SOURCE
      x-policy: POL-SRC-RATE-RELIABILITY
      x-events:
      - EVT-SRC-RELIABILITY-RATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - RATING_INVALID
      - SOURCE_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SrcRateReliabilityCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/sources/{id}/actions/update-profile:
    post:
      operationId: CMD-SRC-UPDATE-PROFILE
      summary: CMD-SRC-UPDATE-PROFILE
      x-aggregate: AGG-SOURCE
      x-policy: POL-SRC-UPDATE-PROFILE
      x-events:
      - EVT-SRC-PROFILE-UPDATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SOURCE_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SrcUpdateProfileCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/sources/{id}/actions/set-protection:
    post:
      operationId: CMD-SRC-SET-PROTECTION
      summary: CMD-SRC-SET-PROTECTION
      x-aggregate: AGG-SOURCE
      x-policy: POL-SRC-SET-PROTECTION
      x-events:
      - EVT-SRC-PROTECTION-CHANGED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SEGREGATION_OF_DUTIES
      - SOURCE_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SrcSetProtectionCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/sources/{id}/actions/reclassify:
    post:
      operationId: CMD-SRC-RECLASSIFY
      summary: CMD-SRC-RECLASSIFY
      x-aggregate: AGG-SOURCE
      x-policy: POL-SRC-RECLASSIFY
      x-events:
      - EVT-SRC-RECLASSIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
      - IDEMPOTENCY_KEY_REUSED
      - SOURCE_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SrcReclassifyCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/sources/{id}/actions/suspend:
    post:
      operationId: CMD-SRC-SUSPEND
      summary: CMD-SRC-SUSPEND
      x-aggregate: AGG-SOURCE
      x-policy: POL-SRC-SUSPEND
      x-events:
      - EVT-SRC-SUSPENDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - SOURCE_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SrcSuspendCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/sources/{id}/actions/reinstate:
    post:
      operationId: CMD-SRC-REINSTATE
      summary: CMD-SRC-REINSTATE
      x-aggregate: AGG-SOURCE
      x-policy: POL-SRC-REINSTATE
      x-events:
      - EVT-SRC-REINSTATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SOURCE_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SrcReinstateCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/sources/{id}/actions/retire:
    post:
      operationId: CMD-SRC-RETIRE
      summary: CMD-SRC-RETIRE
      x-aggregate: AGG-SOURCE
      x-policy: POL-SRC-RETIRE
      x-events:
      - EVT-SRC-RETIRED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - SOURCE_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SrcRetireCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/observations:
    post:
      operationId: CMD-OBS-RECORD
      summary: CMD-OBS-RECORD
      x-aggregate: AGG-OBSERVATION
      x-policy: POL-OBS-RECORD
      x-events:
      - EVT-OBS-RECORDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - OBSERVATION_INVALID
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: true
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObsRecordCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
    get:
      operationId: QRY-OBS-LIST
      summary: Observations by bbox, time window (mandatory, ≤ 31 days), source, state
      x-authorized: any user; allowed_scope pre-filter
      x-requirement: REQ-INF-002
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - $ref: '#/components/parameters/Cursor'
      - $ref: '#/components/parameters/Limit'
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Page'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/observations/{id}/actions/amend:
    post:
      operationId: CMD-OBS-AMEND
      summary: CMD-OBS-AMEND
      x-aggregate: AGG-OBSERVATION
      x-policy: POL-OBS-AMEND
      x-events:
      - EVT-OBS-AMENDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - OBSERVATION_INVALID_STATE_TRANSITION
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: true
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObsAmendCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/observations/{id}/actions/attach-evidence:
    post:
      operationId: CMD-OBS-ATTACH-EVIDENCE
      summary: CMD-OBS-ATTACH-EVIDENCE
      x-aggregate: AGG-OBSERVATION
      x-policy: POL-OBS-ATTACH-EVIDENCE
      x-events:
      - EVT-OBS-EVIDENCE-ATTACHED
      x-error-codes:
      - AUTHZ_DENIED
      - EVIDENCE_INVALID
      - IDEMPOTENCY_KEY_REUSED
      - OBSERVATION_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: true
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObsAttachEvidenceCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/observations/{id}/actions/reclassify:
    post:
      operationId: CMD-OBS-RECLASSIFY
      summary: CMD-OBS-RECLASSIFY
      x-aggregate: AGG-OBSERVATION
      x-policy: POL-OBS-RECLASSIFY
      x-events:
      - EVT-OBS-RECLASSIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
      - IDEMPOTENCY_KEY_REUSED
      - OBSERVATION_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObsReclassifyCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/observations/{id}/actions/validate:
    post:
      operationId: CMD-OBS-VALIDATE
      summary: CMD-OBS-VALIDATE
      x-aggregate: AGG-OBSERVATION
      x-policy: POL-OBS-VALIDATE
      x-events:
      - EVT-OBS-VALIDATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - OBSERVATION_INVALID_STATE_TRANSITION
      - SEGREGATION_OF_DUTIES
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObsValidateCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/observations/{id}/actions/reject:
    post:
      operationId: CMD-OBS-REJECT
      summary: CMD-OBS-REJECT
      x-aggregate: AGG-OBSERVATION
      x-policy: POL-OBS-REJECT
      x-events:
      - EVT-OBS-REJECTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - OBSERVATION_INVALID_STATE_TRANSITION
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObsRejectCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/entities:
    post:
      operationId: CMD-ENT-REGISTER
      summary: CMD-ENT-REGISTER
      x-aggregate: AGG-ENTITY
      x-policy: POL-ENT-REGISTER
      x-events:
      - EVT-ENT-REGISTERED
      x-error-codes:
      - AUTHZ_DENIED
      - ENTITY_INVALID
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EntRegisterCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
    get:
      operationId: QRY-ENT-LIST
      summary: Entities by type, bbox/polygon of current location, valid_at
      x-authorized: any user; allowed_scope pre-filter
      x-requirement: REQ-INF-020
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - $ref: '#/components/parameters/Cursor'
      - $ref: '#/components/parameters/Limit'
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Page'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/entities/{id}/actions/change-type:
    post:
      operationId: CMD-ENT-CHANGE-TYPE
      summary: CMD-ENT-CHANGE-TYPE
      x-aggregate: AGG-ENTITY
      x-policy: POL-ENT-CHANGE-TYPE
      x-events:
      - EVT-ENT-TYPE-CHANGED
      x-error-codes:
      - AUTHZ_DENIED
      - ENTITY_INVALID_STATE_TRANSITION
      - ENTITY_TYPE_INCOMPATIBLE
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EntChangeTypeCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/entities/{id}/actions/reclassify:
    post:
      operationId: CMD-ENT-RECLASSIFY
      summary: CMD-ENT-RECLASSIFY
      x-aggregate: AGG-ENTITY
      x-policy: POL-ENT-RECLASSIFY
      x-events:
      - EVT-ENT-RECLASSIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
      - ENTITY_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EntReclassifyCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/entities/{id}/actions/retire:
    post:
      operationId: CMD-ENT-RETIRE
      summary: CMD-ENT-RETIRE
      x-aggregate: AGG-ENTITY
      x-policy: POL-ENT-RETIRE
      x-events:
      - EVT-ENT-RETIRED
      x-error-codes:
      - AUTHZ_DENIED
      - ENTITY_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EntRetireCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/entities/{id}/actions/reinstate:
    post:
      operationId: CMD-ENT-REINSTATE
      summary: CMD-ENT-REINSTATE
      x-aggregate: AGG-ENTITY
      x-policy: POL-ENT-REINSTATE
      x-events:
      - EVT-ENT-REINSTATED
      x-error-codes:
      - AUTHZ_DENIED
      - ENTITY_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EntReinstateCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/events:
    post:
      operationId: CMD-RWE-REGISTER
      summary: CMD-RWE-REGISTER
      x-aggregate: AGG-REALWORLD-EVENT
      x-policy: POL-RWE-REGISTER
      x-events:
      - EVT-RWE-REGISTERED
      x-error-codes:
      - AUTHZ_DENIED
      - EVENT_INVALID
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RweRegisterCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/events/{id}/actions/change-type:
    post:
      operationId: CMD-RWE-CHANGE-TYPE
      summary: CMD-RWE-CHANGE-TYPE
      x-aggregate: AGG-REALWORLD-EVENT
      x-policy: POL-RWE-CHANGE-TYPE
      x-events:
      - EVT-RWE-TYPE-CHANGED
      x-error-codes:
      - AUTHZ_DENIED
      - EVENT_TYPE_INCOMPATIBLE
      - IDEMPOTENCY_KEY_REUSED
      - REALWORLD_EVENT_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RweChangeTypeCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/events/{id}/actions/reclassify:
    post:
      operationId: CMD-RWE-RECLASSIFY
      summary: CMD-RWE-RECLASSIFY
      x-aggregate: AGG-REALWORLD-EVENT
      x-policy: POL-RWE-RECLASSIFY
      x-events:
      - EVT-RWE-RECLASSIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
      - IDEMPOTENCY_KEY_REUSED
      - REALWORLD_EVENT_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RweReclassifyCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/events/{id}/actions/retire:
    post:
      operationId: CMD-RWE-RETIRE
      summary: CMD-RWE-RETIRE
      x-aggregate: AGG-REALWORLD-EVENT
      x-policy: POL-RWE-RETIRE
      x-events:
      - EVT-RWE-RETIRED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REALWORLD_EVENT_INVALID_STATE_TRANSITION
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RweRetireCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/events/{id}/actions/reinstate:
    post:
      operationId: CMD-RWE-REINSTATE
      summary: CMD-RWE-REINSTATE
      x-aggregate: AGG-REALWORLD-EVENT
      x-policy: POL-RWE-REINSTATE
      x-events:
      - EVT-RWE-REINSTATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REALWORLD_EVENT_INVALID_STATE_TRANSITION
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RweReinstateCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/relationships:
    post:
      operationId: CMD-REL-REGISTER
      summary: CMD-REL-REGISTER
      x-aggregate: AGG-RELATIONSHIP
      x-policy: POL-REL-REGISTER
      x-events:
      - EVT-REL-REGISTERED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - RELATIONSHIP_INVALID
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RelRegisterCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/relationships/{id}/actions/reclassify:
    post:
      operationId: CMD-REL-RECLASSIFY
      summary: CMD-REL-RECLASSIFY
      x-aggregate: AGG-RELATIONSHIP
      x-policy: POL-REL-RECLASSIFY
      x-events:
      - EVT-REL-RECLASSIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
      - IDEMPOTENCY_KEY_REUSED
      - RELATIONSHIP_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RelReclassifyCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/relationships/{id}/actions/retire:
    post:
      operationId: CMD-REL-RETIRE
      summary: CMD-REL-RETIRE
      x-aggregate: AGG-RELATIONSHIP
      x-policy: POL-REL-RETIRE
      x-events:
      - EVT-REL-RETIRED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - RELATIONSHIP_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RelRetireCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/relationships/{id}/actions/reinstate:
    post:
      operationId: CMD-REL-REINSTATE
      summary: CMD-REL-REINSTATE
      x-aggregate: AGG-RELATIONSHIP
      x-policy: POL-REL-REINSTATE
      x-events:
      - EVT-REL-REINSTATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - RELATIONSHIP_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RelReinstateCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/claims:
    post:
      operationId: CMD-CLM-ASSERT
      summary: CMD-CLM-ASSERT
      x-aggregate: AGG-CLAIM
      x-policy: POL-CLM-ASSERT
      x-events:
      - EVT-CLM-ASSERTED
      x-error-codes:
      - AUTHZ_DENIED
      - CLAIM_INVALID
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ClmAssertCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/claims/{id}/actions/correct:
    post:
      operationId: CMD-CLM-CORRECT
      summary: CMD-CLM-CORRECT
      x-aggregate: AGG-CLAIM
      x-policy: POL-CLM-CORRECT
      x-events:
      - EVT-CLM-CORRECTED
      x-error-codes:
      - AUTHZ_DENIED
      - CLAIM_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ClmCorrectCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/claims/{id}/actions/record-change:
    post:
      operationId: CMD-CLM-RECORD-CHANGE
      summary: CMD-CLM-RECORD-CHANGE
      x-aggregate: AGG-CLAIM
      x-policy: POL-CLM-RECORD-CHANGE
      x-events:
      - EVT-CLM-CHANGED
      x-error-codes:
      - AUTHZ_DENIED
      - CHANGE_TIME_INVALID
      - CLAIM_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ClmRecordChangeCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/claims/{id}/actions/retract:
    post:
      operationId: CMD-CLM-RETRACT
      summary: CMD-CLM-RETRACT
      x-aggregate: AGG-CLAIM
      x-policy: POL-CLM-RETRACT
      x-events:
      - EVT-CLM-RETRACTED
      x-error-codes:
      - AUTHZ_DENIED
      - CLAIM_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ClmRetractCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/claims/{id}/actions/assess:
    post:
      operationId: CMD-CLM-ASSESS
      summary: CMD-CLM-ASSESS
      x-aggregate: AGG-CLAIM
      x-policy: POL-CLM-ASSESS
      x-events:
      - EVT-CLM-ASSESSED
      x-error-codes:
      - ASSESSMENT_INVALID
      - AUTHZ_DENIED
      - CLAIM_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ClmAssessCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/claims/{id}/actions/reclassify:
    post:
      operationId: CMD-CLM-RECLASSIFY
      summary: CMD-CLM-RECLASSIFY
      x-aggregate: AGG-CLAIM
      x-policy: POL-CLM-RECLASSIFY
      x-events:
      - EVT-CLM-RECLASSIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLAIM_INVALID_STATE_TRANSITION
      - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ClmReclassifyCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/evidence:
    post:
      operationId: CMD-EVD-REGISTER
      summary: CMD-EVD-REGISTER
      x-aggregate: AGG-EVIDENCE
      x-policy: POL-EVD-REGISTER
      x-events:
      - EVT-EVD-REGISTERED
      x-error-codes:
      - AUTHZ_DENIED
      - EVIDENCE_INVALID
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: true
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvdRegisterCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/evidence/{id}/actions/update-locator:
    post:
      operationId: CMD-EVD-UPDATE-LOCATOR
      summary: CMD-EVD-UPDATE-LOCATOR
      x-aggregate: AGG-EVIDENCE
      x-policy: POL-EVD-UPDATE-LOCATOR
      x-events:
      - EVT-EVD-LOCATOR-UPDATED
      x-error-codes:
      - AUTHZ_DENIED
      - EVIDENCE_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - LOCATOR_INVALID
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvdUpdateLocatorCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/evidence/{id}/actions/seal:
    post:
      operationId: CMD-EVD-SEAL
      summary: CMD-EVD-SEAL
      x-aggregate: AGG-EVIDENCE
      x-policy: POL-EVD-SEAL
      x-events:
      - EVT-EVD-SEALED
      x-error-codes:
      - AUTHZ_DENIED
      - EVIDENCE_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvdSealCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/evidence/{id}/actions/transfer-custody:
    post:
      operationId: CMD-EVD-TRANSFER-CUSTODY
      summary: CMD-EVD-TRANSFER-CUSTODY
      x-aggregate: AGG-EVIDENCE
      x-policy: POL-EVD-TRANSFER-CUSTODY
      x-events:
      - EVT-EVD-CUSTODY-TRANSFERRED
      x-error-codes:
      - AUTHZ_DENIED
      - CUSTODY_INVALID
      - EVIDENCE_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvdTransferCustodyCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/evidence/{id}/actions/reclassify:
    post:
      operationId: CMD-EVD-RECLASSIFY
      summary: CMD-EVD-RECLASSIFY
      x-aggregate: AGG-EVIDENCE
      x-policy: POL-EVD-RECLASSIFY
      x-events:
      - EVT-EVD-RECLASSIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
      - EVIDENCE_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvdReclassifyCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/evidence/{id}/actions/withdraw:
    post:
      operationId: CMD-EVD-WITHDRAW
      summary: CMD-EVD-WITHDRAW
      x-aggregate: AGG-EVIDENCE
      x-policy: POL-EVD-WITHDRAW
      x-events:
      - EVT-EVD-WITHDRAWN
      x-error-codes:
      - AUTHZ_DENIED
      - EVIDENCE_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvdWithdrawCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/evidence-links:
    post:
      operationId: CMD-EVL-LINK
      summary: CMD-EVL-LINK
      x-aggregate: AGG-EVIDENCE-LINK
      x-policy: POL-EVL-LINK
      x-events:
      - EVT-EVL-LINKED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - LINK_DUPLICATE
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvlLinkCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/evidence-links/{id}/actions/unlink:
    post:
      operationId: CMD-EVL-UNLINK
      summary: CMD-EVL-UNLINK
      x-aggregate: AGG-EVIDENCE-LINK
      x-policy: POL-EVL-UNLINK
      x-events:
      - EVT-EVL-UNLINKED
      x-error-codes:
      - AUTHZ_DENIED
      - EVIDENCE_LINK_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvlUnlinkCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/attachments:
    post:
      operationId: CMD-ATT-INITIATE-UPLOAD
      summary: CMD-ATT-INITIATE-UPLOAD
      x-aggregate: AGG-ATTACHMENT
      x-policy: POL-ATT-INITIATE-UPLOAD
      x-events:
      - EVT-ATT-UPLOAD-INITIATED
      x-error-codes:
      - ATTACHMENT_REJECTED
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: true
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AttInitiateUploadCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/attachments/{id}/actions/complete-upload:
    post:
      operationId: CMD-ATT-COMPLETE-UPLOAD
      summary: CMD-ATT-COMPLETE-UPLOAD
      x-aggregate: AGG-ATTACHMENT
      x-policy: POL-ATT-COMPLETE-UPLOAD
      x-events:
      - EVT-ATT-UPLOADED
      x-error-codes:
      - ATTACHMENT_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - HASH_MISMATCH
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: true
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AttCompleteUploadCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/attachments/{id}/actions/erase:
    post:
      operationId: CMD-ATT-ERASE
      summary: CMD-ATT-ERASE
      x-aggregate: AGG-ATTACHMENT
      x-policy: POL-ATT-ERASE
      x-events:
      - EVT-ATT-ERASED
      x-error-codes:
      - ATTACHMENT_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - LEGAL_HOLD_ACTIVE
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AttEraseCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/import-batches:
    post:
      operationId: CMD-IMP-SUBMIT
      summary: CMD-IMP-SUBMIT
      x-aggregate: AGG-IMPORT-BATCH
      x-policy: POL-IMP-SUBMIT
      x-events:
      - EVT-IMP-RECEIVED
      x-error-codes:
      - AUTHZ_DENIED
      - BATCH_KEY_REUSED
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ImpSubmitCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/import-batches/{id}/actions/reprocess-quarantine:
    post:
      operationId: CMD-IMP-REPROCESS-QUARANTINE
      summary: CMD-IMP-REPROCESS-QUARANTINE
      x-aggregate: AGG-IMPORT-BATCH
      x-policy: POL-IMP-REPROCESS-QUARANTINE
      x-events:
      - EVT-IMP-REPROCESSING
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - IMPORT_BATCH_INVALID_STATE_TRANSITION
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ImpReprocessQuarantineCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/import-batches/{id}/actions/accept-quarantine:
    post:
      operationId: CMD-IMP-ACCEPT-QUARANTINE
      summary: CMD-IMP-ACCEPT-QUARANTINE
      x-aggregate: AGG-IMPORT-BATCH
      x-policy: POL-IMP-ACCEPT-QUARANTINE
      x-events:
      - EVT-IMP-QUARANTINE-ACCEPTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - IMPORT_BATCH_INVALID_STATE_TRANSITION
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ImpAcceptQuarantineCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/import-batches/{id}/actions/cancel:
    post:
      operationId: CMD-IMP-CANCEL
      summary: CMD-IMP-CANCEL
      x-aggregate: AGG-IMPORT-BATCH
      x-policy: POL-IMP-CANCEL
      x-events:
      - EVT-IMP-CANCELLED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - IMPORT_BATCH_INVALID_STATE_TRANSITION
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ImpCancelCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/external-ids:
    post:
      operationId: CMD-EXT-MAP
      summary: CMD-EXT-MAP
      x-aggregate: AGG-EXTERNAL-ID
      x-policy: POL-EXT-MAP
      x-events:
      - EVT-EXT-MAPPED
      x-error-codes:
      - AUTHZ_DENIED
      - EXTERNAL_ID_TAKEN
      - IDEMPOTENCY_KEY_REUSED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ExtMapCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/external-ids/{id}/actions/end:
    post:
      operationId: CMD-EXT-END
      summary: CMD-EXT-END
      x-aggregate: AGG-EXTERNAL-ID
      x-policy: POL-EXT-END
      x-events:
      - EVT-EXT-ENDED
      x-error-codes:
      - AUTHZ_DENIED
      - EXTERNAL_ID_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - VALIDATION_FAILED
      - VERSION_CONFLICT
      x-offline-capable: false
      parameters:
      - $ref: '#/components/parameters/Id'
      - $ref: '#/components/parameters/Idempotency-Key'
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/If-Match'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ExtEndCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/entities/{entity_id}:
    get:
      operationId: QRY-ENT-RESOLVED
      summary: Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED
        candidates, confidence); resolves through the identity cluster and returns
        canonical_urn + requested_urn (SLC-04)
      x-authorized: any user; claims label-filtered (INV-ENT-02)
      x-requirement: REQ-INF-023
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: entity_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/entities/{entity_id}/claims:
    get:
      operationId: QRY-ENT-CLAIMS
      summary: Claim history (predicate, valid_at, known_at, include_closed)
      x-authorized: any user; label-filtered
      x-requirement: REQ-INF-022
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: entity_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - $ref: '#/components/parameters/Cursor'
      - $ref: '#/components/parameters/Limit'
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Page'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/entities/{entity_id}/positions:
    get:
      operationId: QRY-ENT-POSITIONS
      summary: Position history in [from,to) as known_at
      x-authorized: any user; label-filtered; geometry generalized by obligation
      x-requirement: REQ-INF-030
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: entity_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - $ref: '#/components/parameters/Cursor'
      - $ref: '#/components/parameters/Limit'
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Page'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/events/{event_id}:
    get:
      operationId: QRY-RWE-GET
      summary: Resolved real-world event
      x-authorized: any user; label-filtered
      x-requirement: REQ-INF-020
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: event_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/entities/{entity_id}/relationships:
    get:
      operationId: QRY-REL-LIST
      summary: Relationships valid_at/known_at, both directions
      x-authorized: any user; hidden relationships and endpoints omitted
      x-requirement: REQ-INF-027
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: entity_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - $ref: '#/components/parameters/Cursor'
      - $ref: '#/components/parameters/Limit'
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Page'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/claims/{claim_id}:
    get:
      operationId: QRY-CLM-GET
      summary: Claim with sources (per protection), evidence links, supersession chain
      x-authorized: any user; label-filtered
      x-requirement: REQ-INF-021
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: claim_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/observations/{observation_id}:
    get:
      operationId: QRY-OBS-GET
      summary: Observation with measurements and attachment refs
      x-authorized: any user; label-filtered
      x-requirement: REQ-INF-002
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: observation_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/sources/{source_id}:
    get:
      operationId: QRY-SRC-GET
      summary: Source; identity only with source-protection permission
      x-authorized: Analyst and above; protection policy
      x-requirement: REQ-INF-001
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: source_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/evidence/{evidence_id}:
    get:
      operationId: QRY-EVD-GET
      summary: Evidence metadata and custody chain
      x-authorized: any user; label-filtered
      x-requirement: REQ-INF-004
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: evidence_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/attachments/{attachment_id}/download-grants:
    post:
      operationId: QRY-ATT-DOWNLOAD
      summary: Short-lived signed download target (≤ 5 min); audited
      x-authorized: authorized on the owning evidence/observation
      x-requirement: REQ-INF-004
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: attachment_id
        in: path
        required: true
        schema:
          type: string
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedMediaType'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
  /api/v1/information/lineage/{object_urn}:
    get:
      operationId: QRY-LIN-TRACE
      summary: Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy
      x-authorized: any user; per-node authorization
      x-requirement: REQ-INF-035
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: object_urn
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/external-ids/{system}/{external_id}:
    get:
      operationId: QRY-EXT-RESOLVE
      summary: Object URN mapped at time t (not-found shape if hidden)
      x-authorized: adapter service accounts; Analyst
      x-requirement: REQ-INF-036
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: system
        in: path
        required: true
        schema:
          type: string
      - name: external_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/information/import-batches/{batch_id}:
    get:
      operationId: QRY-IMP-GET
      summary: Batch status, counts, quarantine records (paged)
      x-authorized: adapter owner; Administrator
      x-requirement: REQ-INF-006
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: batch_id
        in: path
        required: true
        schema:
          type: string
      - name: valid_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      - name: known_at
        in: query
        required: false
        schema:
          type: string
          format: date-time
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
components:
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
  parameters:
    Idempotency-Key:
      name: Idempotency-Key
      in: header
      required: true
      schema:
        type: string
        maxLength: 128
    If-Match:
      name: If-Match
      in: header
      required: true
      description: expected aggregate version
      schema:
        type: string
    X-Purpose:
      name: X-Purpose
      in: header
      required: true
      schema:
        type: string
    X-Correlation-Id:
      name: X-Correlation-Id
      in: header
      required: true
      schema:
        type: string
    Cursor:
      name: cursor
      in: query
      required: false
      schema:
        type: string
    Limit:
      name: limit
      in: query
      required: false
      schema:
        type: integer
        minimum: 1
        maximum: 200
        default: 50
    Id:
      name: id
      in: path
      required: true
      schema:
        type: string
  responses:
    BadRequest:
      description: VALIDATION_FAILED
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    Unauthorized:
      description: UNAUTHENTICATED (missing or expired token) / MFA_STEP_UP_REQUIRED
        (step-up challenge, retry with the same Idempotency-Key — ADR-P19)
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    Forbidden:
      description: AUTHZ_DENIED for a visible resource or a denied create / APPROVAL_REQUIRED
        (ADR-P19)
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    NotFound:
      description: NOT_FOUND (also returned for resources the caller may not see —
        ADR-P06 §5 as amended by ADR-P19)
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    Conflict:
      description: state transition or version conflict
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    PayloadTooLarge:
      description: PAYLOAD_TOO_LARGE
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    UnsupportedMediaType:
      description: UNSUPPORTED_MEDIA_TYPE
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    Unprocessable:
      description: guard failed / segregation of duties / idempotency key reused
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    RateLimited:
      description: RATE_LIMITED
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
      headers: &id001
        Retry-After:
          description: seconds to wait before retrying; sent when the error is retryable
            (CR-78)
          schema:
            type: integer
            minimum: 0
    Unavailable:
      description: AUDIT_UNAVAILABLE / POLICY_ENGINE_UNAVAILABLE / DEPENDENCY_UNAVAILABLE
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
      headers: *id001
  schemas:
    Urn:
      type: string
      pattern: ^urn:[a-z0-9-]+:[a-z0-9-]+:[0-9A-HJKMNP-TV-Z]{26}$
    LocalizedName:
      type: object
      required:
      - original
      - lang
      properties:
        original:
          type: string
        lang:
          type: string
        normalized:
          type: string
          readOnly: true
        transliterations:
          type: array
          items:
            type: object
            properties:
              scheme:
                type: string
              value:
                type: string
    TenantQuotas:
      type: object
      required:
      - requests_per_s
      - storage_gb
      - events_per_s
      - concurrent_jobs
      properties:
        requests_per_s:
          type: integer
          minimum: 0
        storage_gb:
          type: integer
          minimum: 0
        events_per_s:
          type: integer
          minimum: 0
        concurrent_jobs:
          type: integer
          minimum: 0
    Permission:
      type: object
      required:
      - action
      - resource_type
      properties:
        action:
          type: string
        resource_type:
          type: string
    Level:
      type: object
      required:
      - code
      - rank
      properties:
        code:
          type: string
        rank:
          type: integer
        label_ar:
          type: string
        label_en:
          type: string
        requires_dedicated_cell:
          type: boolean
        deprecated:
          type: boolean
    Caveat:
      type: object
      required:
      - code
      properties:
        code:
          type: string
        releasable_to:
          type: array
          items:
            type: string
        not_releasable_to:
          type: array
          items:
            type: string
    ResourceRef:
      type: object
      required:
      - urn
      - id
      - version
      - state
      properties:
        urn:
          $ref: '#/components/schemas/Urn'
        id:
          type: string
        version:
          type: integer
        state:
          type: string
    ApiError:
      type: object
      required:
      - code
      - message
      - correlation_id
      - retryable
      properties:
        code:
          type: string
        message:
          type: string
        details:
          type: object
        correlation_id:
          type: string
        trace_id:
          type: string
        retryable:
          type: boolean
        policy:
          type: object
          properties:
            decision:
              type: string
            reason_code:
              type: string
    Page:
      type: object
      required:
      - items
      properties:
        items:
          type: array
          items:
            type: object
        next_cursor:
          type:
          - string
          - 'null'
    AuthorityCheckRequest:
      type: object
      required:
      - actor
      - decision_type
      - scope
      - at
      properties:
        actor:
          $ref: '#/components/schemas/Urn'
        decision_type:
          type: string
        scope:
          $ref: '#/components/schemas/Urn'
        at:
          type: string
          format: date-time
        amount:
          type: number
    AuthorityCheckResponse:
      type: object
      required:
      - authorized
      - reason
      properties:
        authorized:
          type: boolean
        grant_chain:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
        reason:
          type: string
    DecisionRequest:
      type: object
      required:
      - subject
      - action
      - resource
      - purpose
      - context
      properties:
        subject:
          type: object
        action:
          type: string
        resource:
          type: object
        purpose:
          type: string
        context:
          type: object
    DecisionResponse:
      type: object
      required:
      - decision
      - reason_code
      - policy_version
      properties:
        decision:
          enum:
          - ALLOW
          - DENY
          - CONDITIONAL
          - REDACT
          - AGGREGATE
          - REQUIRE_APPROVAL
        obligations:
          type: array
          items:
            type: object
        allowed_scope:
          type:
          - object
          - 'null'
        reason_code:
          type: string
        policy_version:
          type: string
    Label:
      type: object
      required:
      - level
      properties:
        level:
          type: string
        compartments:
          type: array
          items:
            type: string
        caveats:
          type: array
          items:
            type: string
    Interval:
      type: object
      required:
      - from
      properties:
        from:
          type: string
          format: date-time
        to:
          type:
          - string
          - 'null'
          format: date-time
    FuzzyInterval:
      type: object
      required:
      - precision
      properties:
        start:
          type:
          - string
          - 'null'
          format: date-time
        end:
          type:
          - string
          - 'null'
          format: date-time
        precision:
          enum:
          - instant
          - second
          - minute
          - hour
          - day
          - month
          - year
          - decade
          - unknown
        uncertainty_before:
          type:
          - string
          - 'null'
        uncertainty_after:
          type:
          - string
          - 'null'
    SpatialEnvelope:
      type: object
      required:
      - geometry
      - crs_original
      - accuracy_m
      properties:
        geometry:
          type: object
          description: GeoJSON
        crs_original:
          type: string
          pattern: ^EPSG:[0-9]+$
        coordinates_original:
          type: object
        accuracy_m:
          type: number
          minimum: 0
        accuracy_basis:
          enum:
          - measured
          - reported
          - estimated
          - unknown
    ClaimValue:
      type: object
      required:
      - kind
      properties:
        kind:
          enum:
          - string
          - number
          - date
          - fuzzy_interval
          - geometry
          - enum
          - ref
        string:
          $ref: '#/components/schemas/LocalizedName'
        number:
          type: number
        unit:
          type: string
          description: UCUM
        date:
          type: string
          format: date-time
        fuzzy_interval:
          $ref: '#/components/schemas/FuzzyInterval'
        geometry:
          $ref: '#/components/schemas/SpatialEnvelope'
        enum:
          type: string
        ref:
          $ref: '#/components/schemas/Urn'
    Confidence:
      type: object
      required:
      - information_confidence
      properties:
        information_confidence:
          enum:
          - 1
          - 2
          - 3
          - 4
          - 5
          - 6
        verification_status:
          enum:
          - UNVERIFIED
          - PARTIALLY_VERIFIED
          - VERIFIED
          - DISPUTED
          - REFUTED
        uncertainty:
          type: object
      description: source_reliability, data_quality, freshness, completeness are computed
        by the platform (confidence-model)
    ClaimInput:
      type: object
      required:
      - predicate
      - value
      - valid
      - source_refs
      - confidence
      properties:
        predicate:
          type: string
        value:
          $ref: '#/components/schemas/ClaimValue'
        valid:
          $ref: '#/components/schemas/Interval'
        source_refs:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/Urn'
        confidence:
          $ref: '#/components/schemas/Confidence'
        label:
          $ref: '#/components/schemas/Label'
    Measurement:
      type: object
      required:
      - quantity
      - value
      - unit
      properties:
        quantity:
          type: string
        value:
          type: number
        unit:
          type: string
        uncertainty:
          type: number
    TemporalParams:
      type: object
      description: valid_at, known_at query parameters (ISO 8601; default now)
    SrcRegisterCommand:
      type: object
      properties:
        type:
          type: string
        name:
          $ref: '#/components/schemas/LocalizedName'
        owner_org:
          $ref: '#/components/schemas/Urn'
        reliability:
          type: string
          enum:
          - A
          - B
          - C
          - D
          - E
          - F
        valid_from:
          type: string
          format: date-time
        protection_level:
          type: integer
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - type
      - name
      - owner_org
      - reliability
      - valid_from
      - label
    SrcRateReliabilityCommand:
      type: object
      properties:
        reliability:
          type: string
          enum:
          - A
          - B
          - C
          - D
          - E
          - F
        valid_from:
          type: string
          format: date-time
        rationale:
          type: string
      additionalProperties: false
      required:
      - reliability
      - valid_from
      - rationale
    SrcUpdateProfileCommand:
      type: object
      properties:
        name:
          $ref: '#/components/schemas/LocalizedName'
        contact:
          type: object
      additionalProperties: false
    SrcSetProtectionCommand:
      type: object
      properties:
        protection_level:
          type: integer
        second_approver:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - protection_level
    SrcReclassifyCommand:
      type: object
      properties:
        label:
          $ref: '#/components/schemas/Label'
        reason:
          type: string
      additionalProperties: false
      required:
      - label
      - reason
    SrcSuspendCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    SrcReinstateCommand:
      type: object
      properties: {}
      additionalProperties: false
    SrcRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ObsRecordCommand:
      type: object
      properties:
        client_id:
          type: string
        source:
          $ref: '#/components/schemas/Urn'
        observer:
          $ref: '#/components/schemas/Urn'
        observed_at:
          type: string
          format: date-time
        event_time:
          $ref: '#/components/schemas/FuzzyInterval'
        location:
          $ref: '#/components/schemas/SpatialEnvelope'
        method:
          type: string
        measurements:
          type: array
          items:
            $ref: '#/components/schemas/Measurement'
        narrative:
          $ref: '#/components/schemas/LocalizedName'
        attachments:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
        label:
          $ref: '#/components/schemas/Label'
        field_session:
          $ref: '#/components/schemas/Urn'
        device:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - source
      - observer
      - observed_at
      - location
      - method
      - label
    ObsAmendCommand:
      type: object
      properties:
        changes:
          type: object
        reason:
          type: string
      additionalProperties: false
      required:
      - changes
      - reason
    ObsAttachEvidenceCommand:
      type: object
      properties:
        evidence:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - evidence
    ObsReclassifyCommand:
      type: object
      properties:
        label:
          $ref: '#/components/schemas/Label'
        reason:
          type: string
      additionalProperties: false
      required:
      - label
      - reason
    ObsValidateCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
    ObsRejectCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    EntRegisterCommand:
      type: object
      properties:
        entity_type:
          type: string
        label:
          $ref: '#/components/schemas/Label'
        initial_claims:
          type: array
          items: &id002
            $ref: '#/components/schemas/ClaimInput'
        external_ids:
          type: array
          items:
            type: object
      additionalProperties: false
      required:
      - entity_type
      - label
    EntChangeTypeCommand:
      type: object
      properties:
        entity_type:
          type: string
        reason:
          type: string
      additionalProperties: false
      required:
      - entity_type
      - reason
    EntReclassifyCommand:
      type: object
      properties:
        label:
          $ref: '#/components/schemas/Label'
        reason:
          type: string
      additionalProperties: false
      required:
      - label
      - reason
    EntRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    EntReinstateCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    RweRegisterCommand:
      type: object
      properties:
        event_type:
          type: string
        label:
          $ref: '#/components/schemas/Label'
        initial_claims:
          type: array
          items: *id002
      additionalProperties: false
      required:
      - event_type
      - label
      - initial_claims
    RweChangeTypeCommand:
      type: object
      properties:
        event_type:
          type: string
        reason:
          type: string
      additionalProperties: false
      required:
      - event_type
      - reason
    RweReclassifyCommand:
      type: object
      properties:
        label:
          $ref: '#/components/schemas/Label'
        reason:
          type: string
      additionalProperties: false
      required:
      - label
      - reason
    RweRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    RweReinstateCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    RelRegisterCommand:
      type: object
      properties:
        relationship_type:
          type: string
        source_ref:
          $ref: '#/components/schemas/Urn'
        target_ref:
          $ref: '#/components/schemas/Urn'
        valid:
          $ref: '#/components/schemas/Interval'
        source_refs:
          type: array
          items: &id003
            $ref: '#/components/schemas/Urn'
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - relationship_type
      - source_ref
      - target_ref
      - valid
      - source_refs
      - label
    RelReclassifyCommand:
      type: object
      properties:
        label:
          $ref: '#/components/schemas/Label'
        reason:
          type: string
      additionalProperties: false
      required:
      - label
      - reason
    RelRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    RelReinstateCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ClmAssertCommand:
      type: object
      properties:
        subject:
          $ref: '#/components/schemas/Urn'
        predicate:
          type: string
        value:
          $ref: '#/components/schemas/ClaimValue'
        valid:
          $ref: '#/components/schemas/Interval'
        source_refs:
          type: array
          items: *id003
        derived_from:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
        confidence:
          $ref: '#/components/schemas/Confidence'
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - subject
      - predicate
      - value
      - valid
      - source_refs
      - confidence
      - label
    ClmCorrectCommand:
      type: object
      properties:
        value:
          $ref: '#/components/schemas/ClaimValue'
        valid:
          $ref: '#/components/schemas/Interval'
        source_refs:
          type: array
          items: *id003
        confidence:
          $ref: '#/components/schemas/Confidence'
        reason:
          type: string
      additionalProperties: false
      required:
      - value
      - source_refs
      - confidence
      - reason
    ClmRecordChangeCommand:
      type: object
      properties:
        t_change:
          type: string
          format: date-time
        new_value:
          $ref: '#/components/schemas/ClaimValue'
        source_refs:
          type: array
          items: *id003
        confidence:
          $ref: '#/components/schemas/Confidence'
      additionalProperties: false
      required:
      - t_change
      - new_value
      - source_refs
      - confidence
    ClmRetractCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ClmAssessCommand:
      type: object
      properties:
        information_confidence:
          type: string
          enum:
          - '1'
          - '2'
          - '3'
          - '4'
          - '5'
          - '6'
        verification_status:
          type: string
          enum:
          - UNVERIFIED
          - PARTIALLY_VERIFIED
          - VERIFIED
          - DISPUTED
          - REFUTED
        rationale:
          type: string
      additionalProperties: false
      required:
      - rationale
    ClmReclassifyCommand:
      type: object
      properties:
        label:
          $ref: '#/components/schemas/Label'
        reason:
          type: string
      additionalProperties: false
      required:
      - label
      - reason
    EvdRegisterCommand:
      type: object
      properties:
        client_id:
          type: string
        evidence_type:
          type: string
        attachment:
          $ref: '#/components/schemas/Urn'
        observation_ref:
          $ref: '#/components/schemas/Urn'
        locator:
          type: object
        source:
          $ref: '#/components/schemas/Urn'
        collected_at:
          type: string
          format: date-time
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - evidence_type
      - source
      - collected_at
      - label
    EvdUpdateLocatorCommand:
      type: object
      properties:
        locator:
          type: object
      additionalProperties: false
      required:
      - locator
    EvdSealCommand:
      type: object
      properties: {}
      additionalProperties: false
    EvdTransferCustodyCommand:
      type: object
      properties:
        new_holder:
          $ref: '#/components/schemas/Urn'
        action:
          type: string
      additionalProperties: false
      required:
      - new_holder
      - action
    EvdReclassifyCommand:
      type: object
      properties:
        label:
          $ref: '#/components/schemas/Label'
        reason:
          type: string
      additionalProperties: false
      required:
      - label
      - reason
    EvdWithdrawCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    EvlLinkCommand:
      type: object
      properties:
        evidence:
          $ref: '#/components/schemas/Urn'
        claim:
          $ref: '#/components/schemas/Urn'
        stance:
          type: string
          enum:
          - SUPPORTS
          - REFUTES
          - CONTEXT
        note:
          type: string
      additionalProperties: false
      required:
      - evidence
      - claim
      - stance
    EvlUnlinkCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    AttInitiateUploadCommand:
      type: object
      properties:
        client_id:
          type: string
        sha256:
          type: string
        size_bytes:
          type: integer
        mime_type:
          type: string
        file_name:
          type: string
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - sha256
      - size_bytes
      - mime_type
      - label
    AttCompleteUploadCommand:
      type: object
      properties: {}
      additionalProperties: false
    AttEraseCommand:
      type: object
      properties:
        erasure_order_ref:
          type: string
      additionalProperties: false
      required:
      - erasure_order_ref
    ImpSubmitCommand:
      type: object
      properties:
        adapter:
          $ref: '#/components/schemas/Urn'
        batch_key:
          type: string
        content_sha256:
          type: string
        format:
          type: string
        payload_attachment:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - adapter
      - batch_key
      - content_sha256
      - format
      - payload_attachment
    ImpReprocessQuarantineCommand:
      type: object
      properties:
        mapping_version:
          type: string
        corrections:
          type: array
          items:
            type: object
      additionalProperties: false
    ImpAcceptQuarantineCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ImpCancelCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ExtMapCommand:
      type: object
      properties:
        system:
          type: string
        external_id:
          type: string
        object:
          $ref: '#/components/schemas/Urn'
        valid_from:
          type: string
          format: date-time
      additionalProperties: false
      required:
      - system
      - external_id
      - object
      - valid_from
    ExtEndCommand:
      type: object
      properties:
        valid_to:
          type: string
          format: date-time
        reason:
          type: string
      additionalProperties: false
      required:
      - valid_to
      - reason
```
