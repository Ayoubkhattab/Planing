---
id: OPENAPI-BC03-SLC06
type: api-contract
title: Intelligence API (BC03) — SLC-06
wave: W6
slice: SLC-06
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

# Intelligence API (BC03) — SLC-06

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_23 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/intelligence/situations` | CMD-SIT-CREATE |
| GET | `/api/v1/intelligence/situations` | QRY-SIT-LIST |
| POST | `/api/v1/intelligence/situations/{id}/actions/edit-definition` | CMD-SIT-EDIT-DEFINITION |
| POST | `/api/v1/intelligence/situations/{id}/actions/activate` | CMD-SIT-ACTIVATE |
| POST | `/api/v1/intelligence/situations/{id}/actions/pause` | CMD-SIT-PAUSE |
| POST | `/api/v1/intelligence/situations/{id}/actions/resume` | CMD-SIT-RESUME |
| POST | `/api/v1/intelligence/situations/{id}/actions/close` | CMD-SIT-CLOSE |
| POST | `/api/v1/intelligence/situations/{id}/actions/reclassify` | CMD-SIT-RECLASSIFY |
| POST | `/api/v1/intelligence/alert-rules` | CMD-ARL-DEFINE |
| POST | `/api/v1/intelligence/alert-rules/{id}/actions/edit` | CMD-ARL-EDIT |
| POST | `/api/v1/intelligence/alert-rules/{id}/actions/activate` | CMD-ARL-ACTIVATE |
| POST | `/api/v1/intelligence/alert-rules/{id}/actions/disable` | CMD-ARL-DISABLE |
| POST | `/api/v1/intelligence/alert-rules/{id}/actions/enable` | CMD-ARL-ENABLE |
| POST | `/api/v1/intelligence/alert-rules/{id}/actions/retire` | CMD-ARL-RETIRE |
| POST | `/api/v1/intelligence/alerts/{id}/actions/acknowledge` | CMD-ALR-ACKNOWLEDGE |
| POST | `/api/v1/intelligence/alerts/{id}/actions/resolve` | CMD-ALR-RESOLVE |
| POST | `/api/v1/intelligence/alerts/{id}/actions/dismiss` | CMD-ALR-DISMISS |
| GET | `/api/v1/intelligence/situations/{situation_id}` | QRY-SIT-GET |
| GET | `/api/v1/intelligence/situations/{situation_id}/picture` | QRY-SIT-COP |
| GET | `/api/v1/intelligence/situations/{situation_id}/changes` | QRY-SIT-CHANGES |
| GET | `/api/v1/intelligence/situations/{situation_id}/tiles/{layer}/{z}/{x}/{y}` | QRY-SIT-TILE |
| GET | `/api/v1/intelligence/base-maps/{layer}/{z}/{x}/{y}` | QRY-BASE-TILE |
| GET | `/api/v1/intelligence/alerts` | QRY-ALR-LIST |

```yaml
openapi: 3.1.0
info:
  title: Intelligence API (BC03) — SLC-06
  version: 1.0.0
  description: Generated from SLC-06 domain specification. Do not edit by hand.
servers:
- url: https://{cell}.platform.local
  variables:
    cell:
      default: cell-1
security:
- bearer: []
paths:
  /api/v1/intelligence/situations:
    post:
      operationId: CMD-SIT-CREATE
      summary: CMD-SIT-CREATE
      x-aggregate: AGG-SITUATION
      x-policy: POL-SIT-CREATE
      x-events:
      - EVT-SIT-CREATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SITUATION_INVALID
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
              $ref: '#/components/schemas/SitCreateCommand'
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
      operationId: QRY-SIT-LIST
      summary: Situations by state, owner, extent intersecting bbox
      x-authorized: any user; situation label rule
      x-requirement: REQ-SIT-001
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
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
  /api/v1/intelligence/situations/{id}/actions/edit-definition:
    post:
      operationId: CMD-SIT-EDIT-DEFINITION
      summary: CMD-SIT-EDIT-DEFINITION
      x-aggregate: AGG-SITUATION
      x-policy: POL-SIT-EDIT-DEFINITION
      x-events:
      - EVT-SIT-DEFINITION-CHANGED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SITUATION_INVALID
      - SITUATION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SitEditDefinitionCommand'
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
  /api/v1/intelligence/situations/{id}/actions/activate:
    post:
      operationId: CMD-SIT-ACTIVATE
      summary: CMD-SIT-ACTIVATE
      x-aggregate: AGG-SITUATION
      x-policy: POL-SIT-ACTIVATE
      x-events:
      - EVT-SIT-ACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - QUOTA_EXCEEDED
      - SITUATION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SitActivateCommand'
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
  /api/v1/intelligence/situations/{id}/actions/pause:
    post:
      operationId: CMD-SIT-PAUSE
      summary: CMD-SIT-PAUSE
      x-aggregate: AGG-SITUATION
      x-policy: POL-SIT-PAUSE
      x-events:
      - EVT-SIT-PAUSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - SITUATION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SitPauseCommand'
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
  /api/v1/intelligence/situations/{id}/actions/resume:
    post:
      operationId: CMD-SIT-RESUME
      summary: CMD-SIT-RESUME
      x-aggregate: AGG-SITUATION
      x-policy: POL-SIT-RESUME
      x-events:
      - EVT-SIT-RESUMED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SITUATION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SitResumeCommand'
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
  /api/v1/intelligence/situations/{id}/actions/close:
    post:
      operationId: CMD-SIT-CLOSE
      summary: CMD-SIT-CLOSE
      x-aggregate: AGG-SITUATION
      x-policy: POL-SIT-CLOSE
      x-events:
      - EVT-SIT-CLOSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - SITUATION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SitCloseCommand'
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
  /api/v1/intelligence/situations/{id}/actions/reclassify:
    post:
      operationId: CMD-SIT-RECLASSIFY
      summary: CMD-SIT-RECLASSIFY
      x-aggregate: AGG-SITUATION
      x-policy: POL-SIT-RECLASSIFY
      x-events:
      - EVT-SIT-RECLASSIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
      - IDEMPOTENCY_KEY_REUSED
      - SITUATION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SitReclassifyCommand'
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
  /api/v1/intelligence/alert-rules:
    post:
      operationId: CMD-ARL-DEFINE
      summary: CMD-ARL-DEFINE
      x-aggregate: AGG-ALERT-RULE
      x-policy: POL-ARL-DEFINE
      x-events:
      - EVT-ARL-DEFINED
      x-error-codes:
      - ALERT_RULE_INVALID
      - AUTHZ_DENIED
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
              $ref: '#/components/schemas/ArlDefineCommand'
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
  /api/v1/intelligence/alert-rules/{id}/actions/edit:
    post:
      operationId: CMD-ARL-EDIT
      summary: CMD-ARL-EDIT
      x-aggregate: AGG-ALERT-RULE
      x-policy: POL-ARL-EDIT
      x-events:
      - EVT-ARL-EDITED
      x-error-codes:
      - ALERT_RULE_INVALID
      - ALERT_RULE_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
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
              $ref: '#/components/schemas/ArlEditCommand'
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
  /api/v1/intelligence/alert-rules/{id}/actions/activate:
    post:
      operationId: CMD-ARL-ACTIVATE
      summary: CMD-ARL-ACTIVATE
      x-aggregate: AGG-ALERT-RULE
      x-policy: POL-ARL-ACTIVATE
      x-events:
      - EVT-ARL-ACTIVATED
      x-error-codes:
      - ALERT_RULE_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - DRY_RUN_REQUIRED
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
              $ref: '#/components/schemas/ArlActivateCommand'
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
  /api/v1/intelligence/alert-rules/{id}/actions/disable:
    post:
      operationId: CMD-ARL-DISABLE
      summary: CMD-ARL-DISABLE
      x-aggregate: AGG-ALERT-RULE
      x-policy: POL-ARL-DISABLE
      x-events:
      - EVT-ARL-DISABLED
      x-error-codes:
      - ALERT_RULE_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
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
              $ref: '#/components/schemas/ArlDisableCommand'
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
  /api/v1/intelligence/alert-rules/{id}/actions/enable:
    post:
      operationId: CMD-ARL-ENABLE
      summary: CMD-ARL-ENABLE
      x-aggregate: AGG-ALERT-RULE
      x-policy: POL-ARL-ENABLE
      x-events:
      - EVT-ARL-ENABLED
      x-error-codes:
      - ALERT_RULE_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
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
              $ref: '#/components/schemas/ArlEnableCommand'
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
  /api/v1/intelligence/alert-rules/{id}/actions/retire:
    post:
      operationId: CMD-ARL-RETIRE
      summary: CMD-ARL-RETIRE
      x-aggregate: AGG-ALERT-RULE
      x-policy: POL-ARL-RETIRE
      x-events:
      - EVT-ARL-RETIRED
      x-error-codes:
      - ALERT_RULE_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
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
              $ref: '#/components/schemas/ArlRetireCommand'
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
  /api/v1/intelligence/alerts/{id}/actions/acknowledge:
    post:
      operationId: CMD-ALR-ACKNOWLEDGE
      summary: CMD-ALR-ACKNOWLEDGE
      x-aggregate: AGG-ALERT
      x-policy: POL-ALR-ACKNOWLEDGE
      x-events:
      - EVT-ALR-ACKNOWLEDGED
      x-error-codes:
      - ALERT_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - NOT_A_RECIPIENT
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
              $ref: '#/components/schemas/AlrAcknowledgeCommand'
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
  /api/v1/intelligence/alerts/{id}/actions/resolve:
    post:
      operationId: CMD-ALR-RESOLVE
      summary: CMD-ALR-RESOLVE
      x-aggregate: AGG-ALERT
      x-policy: POL-ALR-RESOLVE
      x-events:
      - EVT-ALR-RESOLVED
      x-error-codes:
      - ALERT_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - NOT_A_RECIPIENT
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
              $ref: '#/components/schemas/AlrResolveCommand'
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
  /api/v1/intelligence/alerts/{id}/actions/dismiss:
    post:
      operationId: CMD-ALR-DISMISS
      summary: CMD-ALR-DISMISS
      x-aggregate: AGG-ALERT
      x-policy: POL-ALR-DISMISS
      x-events:
      - EVT-ALR-DISMISSED
      x-error-codes:
      - ALERT_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
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
              $ref: '#/components/schemas/AlrDismissCommand'
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
  /api/v1/intelligence/situations/{situation_id}:
    get:
      operationId: QRY-SIT-GET
      summary: Definition (version at valid_at), counts of visible members by type
      x-authorized: cleared for situation label
      x-requirement: REQ-SIT-001
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: situation_id
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
        '422':
          $ref: '#/components/responses/Unprocessable'
        '429':
          $ref: '#/components/responses/RateLimited'
        '503':
          $ref: '#/components/responses/Unavailable'
  /api/v1/intelligence/situations/{situation_id}/picture:
    get:
      operationId: QRY-SIT-COP
      summary: 'Common operational picture: visible members (entities, events, observations,
        tasks, assessments, alerts) with resolved, possibly generalized geometry'
      x-authorized: cleared for situation; per-member filtering
      x-requirement: REQ-SIT-003
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: situation_id
        in: path
        required: true
        schema:
          type: string
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
  /api/v1/intelligence/situations/{situation_id}/changes:
    get:
      operationId: QRY-SIT-CHANGES
      summary: Membership change log (visible members only) since cursor/time
      x-authorized: cleared for situation; per-member filtering
      x-requirement: REQ-SIT-002
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: situation_id
        in: path
        required: true
        schema:
          type: string
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
  /api/v1/intelligence/situations/{situation_id}/tiles/{layer}/{z}/{x}/{y}:
    get:
      operationId: QRY-SIT-TILE
      summary: Vector tile of operational layer for the caller's security scope
      x-authorized: cleared for situation; scope-keyed cache (ADR-P06 §6)
      x-requirement: REQ-SIT-007
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: situation_id
        in: path
        required: true
        schema:
          type: string
      - name: layer
        in: path
        required: true
        schema:
          type: string
      - name: z
        in: path
        required: true
        schema:
          type: string
      - name: x
        in: path
        required: true
        schema:
          type: string
      - name: y
        in: path
        required: true
        schema:
          type: string
      responses:
        '200': &id001
          description: vector tile for the caller's security scope
          headers:
            Cache-Control:
              schema:
                type: string
              description: private, max-age <= 60; shared caches keyed by scope hash
                only
            ETag:
              schema:
                type: string
              description: hash(tile, layer, scope_hash, data_version)
          content:
            application/vnd.mapbox-vector-tile:
              schema:
                type: string
                format: binary
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
  /api/v1/intelligence/base-maps/{layer}/{z}/{x}/{y}:
    get:
      operationId: QRY-BASE-TILE
      summary: Base-map tile (layers marked unclassified only; shared cache)
      x-authorized: any user of tenant
      x-requirement: REQ-SIT-007
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: layer
        in: path
        required: true
        schema:
          type: string
      - name: z
        in: path
        required: true
        schema:
          type: string
      - name: x
        in: path
        required: true
        schema:
          type: string
      - name: y
        in: path
        required: true
        schema:
          type: string
      responses:
        '200': *id001
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
  /api/v1/intelligence/alerts:
    get:
      operationId: QRY-ALR-LIST
      summary: My alerts by state, severity, situation
      x-authorized: recipient; label rule
      x-requirement: REQ-SIT-005
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
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
      headers: &id002
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
      headers: *id002
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
    SitCreateCommand:
      type: object
      properties:
        name:
          $ref: '#/components/schemas/LocalizedName'
        extent:
          $ref: '#/components/schemas/SituationExtent'
        window:
          $ref: '#/components/schemas/Interval'
        criteria:
          $ref: '#/components/schemas/SituationCriteria'
        owner:
          $ref: '#/components/schemas/Urn'
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - name
      - extent
      - window
      - criteria
      - owner
      - label
    SitEditDefinitionCommand:
      type: object
      properties:
        extent:
          $ref: '#/components/schemas/SituationExtent'
        window:
          $ref: '#/components/schemas/Interval'
        criteria:
          $ref: '#/components/schemas/SituationCriteria'
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    SitActivateCommand:
      type: object
      properties: {}
      additionalProperties: false
    SitPauseCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    SitResumeCommand:
      type: object
      properties: {}
      additionalProperties: false
    SitCloseCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    SitReclassifyCommand:
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
    ArlDefineCommand:
      type: object
      properties:
        situation:
          $ref: '#/components/schemas/Urn'
        scope:
          type: string
          enum:
          - situation
          - tenant
        kind:
          type: string
        parameters:
          $ref: '#/components/schemas/AlertCondition'
        severity:
          type: string
          enum:
          - info
          - warning
          - critical
        dedupe_window:
          type: string
        escalation:
          type: object
        auto_resolve:
          type: boolean
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - scope
      - kind
      - parameters
      - severity
      - dedupe_window
      - auto_resolve
      - label
    ArlEditCommand:
      type: object
      properties:
        parameters:
          $ref: '#/components/schemas/AlertCondition'
        severity:
          type: string
          enum:
          - info
          - warning
          - critical
        dedupe_window:
          type: string
        escalation:
          type: object
      additionalProperties: false
      required:
      - parameters
    ArlActivateCommand:
      type: object
      properties:
        dry_run_ref:
          type: string
      additionalProperties: false
      required:
      - dry_run_ref
    ArlDisableCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ArlEnableCommand:
      type: object
      properties: {}
      additionalProperties: false
    ArlRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    AlrAcknowledgeCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
    AlrResolveCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
      required:
      - note
    AlrDismissCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    SituationCriteria:
      type: object
      additionalProperties: false
      required:
      - object_types
      properties:
        object_types:
          type: array
          minItems: 1
          items:
            enum:
            - entity
            - realworld_event
            - observation
            - task
            - assessment
            - alert
        entity_types:
          type: array
          items:
            type: string
        event_types:
          type: array
          items:
            type: string
        predicate_filters:
          type: array
          items:
            type: object
            required:
            - predicate
            - op
            properties:
              predicate:
                type: string
              op:
                enum:
                - eq
                - in
                - gte
                - lte
                - exists
                - changed
              value: {}
        observation_methods:
          type: array
          items:
            type: string
        min_source_reliability:
          enum:
          - A
          - B
          - C
          - D
          - E
          - F
        include_disputed:
          type: boolean
          default: true
        include_unvalidated_observations:
          type: boolean
          default: false
    SituationExtent:
      type: object
      oneOf:
      - required:
        - polygon
        properties:
          polygon:
            type: object
      - required:
        - buffer_around
        - radius_m
        properties:
          buffer_around:
            $ref: '#/components/schemas/Urn'
          radius_m:
            type: number
            minimum: 1
            maximum: 500000
    AlertCondition:
      type: object
      required:
      - kind
      properties:
        kind:
          enum:
          - measurement_threshold
          - enters_extent
          - leaves_extent
          - new_observation_in_extent
          - claim_changed
          - conflict_opened
          - task_overdue_in_situation
        quantity:
          type: string
        op:
          enum:
          - gt
          - gte
          - lt
          - lte
        threshold:
          type: number
        unit:
          type: string
        entity_types:
          type: array
          items:
            type: string
        predicate:
          type: string
        observation_methods:
          type: array
          items:
            type: string
```
