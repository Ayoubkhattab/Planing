---
id: OPENAPI-BC06-SLC12
type: api-contract
title: Knowledge API (BC06) — SLC-12
wave: W6
slice: SLC-12
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

# Knowledge API (BC06) — SLC-12

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_37 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/knowledge/product-templates` | CMD-PTM-DEFINE |
| POST | `/api/v1/knowledge/product-templates/{id}/actions/edit` | CMD-PTM-EDIT |
| POST | `/api/v1/knowledge/product-templates/{id}/actions/activate` | CMD-PTM-ACTIVATE |
| POST | `/api/v1/knowledge/product-templates/{id}/actions/retire` | CMD-PTM-RETIRE |
| POST | `/api/v1/knowledge/products` | CMD-PRD-CREATE |
| GET | `/api/v1/knowledge/products` | QRY-PRD-LIST |
| POST | `/api/v1/knowledge/products/{id}/actions/generate` | CMD-PRD-GENERATE |
| POST | `/api/v1/knowledge/products/{id}/actions/edit-narrative` | CMD-PRD-EDIT-NARRATIVE |
| POST | `/api/v1/knowledge/products/{id}/actions/submit` | CMD-PRD-SUBMIT |
| POST | `/api/v1/knowledge/products/{id}/actions/return` | CMD-PRD-RETURN |
| POST | `/api/v1/knowledge/products/{id}/actions/approve` | CMD-PRD-APPROVE |
| POST | `/api/v1/knowledge/products/{id}/actions/withdraw` | CMD-PRD-WITHDRAW |
| POST | `/api/v1/knowledge/products/{id}/actions/discard` | CMD-PRD-DISCARD |
| POST | `/api/v1/knowledge/distributions` | CMD-DST-DISTRIBUTE |
| POST | `/api/v1/knowledge/distributions/{id}/actions/cancel` | CMD-DST-CANCEL |
| POST | `/api/v1/knowledge/knowledge-objects` | CMD-KNO-DRAFT |
| GET | `/api/v1/knowledge/knowledge-objects` | QRY-KNO-SEARCH |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/edit` | CMD-KNO-EDIT |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/submit` | CMD-KNO-SUBMIT |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/return` | CMD-KNO-RETURN |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/publish` | CMD-KNO-PUBLISH |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/reject` | CMD-KNO-REJECT |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/record-reuse` | CMD-KNO-RECORD-REUSE |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/retire` | CMD-KNO-RETIRE |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/discard` | CMD-KNO-DISCARD |
| POST | `/api/v1/knowledge/archive-packages/{id}/actions/retry-ingest` | CMD-ARC-RETRY-INGEST |
| POST | `/api/v1/knowledge/archive-packages/{id}/actions/repair` | CMD-ARC-REPAIR |
| POST | `/api/v1/knowledge/archive-packages/{id}/actions/migrate-format` | CMD-ARC-MIGRATE-FORMAT |
| POST | `/api/v1/knowledge/archive-packages/{id}/actions/transfer` | CMD-ARC-TRANSFER |
| POST | `/api/v1/knowledge/reconstructions` | CMD-REC-REQUEST |
| POST | `/api/v1/knowledge/reconstructions/{id}/actions/cancel` | CMD-REC-CANCEL |
| GET | `/api/v1/knowledge/products/{product_id}` | QRY-PRD-GET |
| GET | `/api/v1/knowledge/products/{product_id}/distributions` | QRY-DST-LOG |
| POST | `/api/v1/knowledge/knowledge-suggestions` | QRY-KNO-SUGGEST |
| GET | `/api/v1/knowledge/archive-packages` | QRY-ARC-SEARCH |
| POST | `/api/v1/knowledge/archive-packages/{package_id}/retrievals` | QRY-ARC-RETRIEVE |
| GET | `/api/v1/knowledge/reconstructions/{reconstruction_id}/report` | QRY-REC-REPORT |

```yaml
openapi: 3.1.0
info:
  title: Knowledge API (BC06) — SLC-12
  version: 1.0.0
  description: Generated from SLC-12 domain specification. Do not edit by hand.
servers:
- url: https://{cell}.platform.local
  variables:
    cell:
      default: cell-1
security:
- bearer: []
paths:
  /api/v1/knowledge/product-templates:
    post:
      operationId: CMD-PTM-DEFINE
      summary: CMD-PTM-DEFINE
      x-aggregate: AGG-PRODUCT-TEMPLATE
      x-policy: POL-PTM-DEFINE
      x-events:
      - EVT-PTM-DEFINED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TEMPLATE_INVALID
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
              $ref: '#/components/schemas/PtmDefineCommand'
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
  /api/v1/knowledge/product-templates/{id}/actions/edit:
    post:
      operationId: CMD-PTM-EDIT
      summary: CMD-PTM-EDIT
      x-aggregate: AGG-PRODUCT-TEMPLATE
      x-policy: POL-PTM-EDIT
      x-events:
      - EVT-PTM-EDITED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION
      - TEMPLATE_INVALID
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
              $ref: '#/components/schemas/PtmEditCommand'
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
  /api/v1/knowledge/product-templates/{id}/actions/activate:
    post:
      operationId: CMD-PTM-ACTIVATE
      summary: CMD-PTM-ACTIVATE
      x-aggregate: AGG-PRODUCT-TEMPLATE
      x-policy: POL-PTM-ACTIVATE
      x-events:
      - EVT-PTM-ACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PtmActivateCommand'
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
  /api/v1/knowledge/product-templates/{id}/actions/retire:
    post:
      operationId: CMD-PTM-RETIRE
      summary: CMD-PTM-RETIRE
      x-aggregate: AGG-PRODUCT-TEMPLATE
      x-policy: POL-PTM-RETIRE
      x-events:
      - EVT-PTM-RETIRED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PtmRetireCommand'
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
  /api/v1/knowledge/products:
    post:
      operationId: CMD-PRD-CREATE
      summary: CMD-PRD-CREATE
      x-aggregate: AGG-PRODUCT
      x-policy: POL-PRD-CREATE
      x-events:
      - EVT-PRD-CREATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_INVALID
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
              $ref: '#/components/schemas/PrdCreateCommand'
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
      operationId: QRY-PRD-LIST
      summary: Products by kind, state, situation/case, date
      x-authorized: allowed_scope
      x-requirement: REQ-PRD-001
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
  /api/v1/knowledge/products/{id}/actions/generate:
    post:
      operationId: CMD-PRD-GENERATE
      summary: CMD-PRD-GENERATE
      x-aggregate: AGG-PRODUCT
      x-policy: POL-PRD-GENERATE
      x-events:
      - EVT-PRD-GENERATION-STARTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PrdGenerateCommand'
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
  /api/v1/knowledge/products/{id}/actions/edit-narrative:
    post:
      operationId: CMD-PRD-EDIT-NARRATIVE
      summary: CMD-PRD-EDIT-NARRATIVE
      x-aggregate: AGG-PRODUCT
      x-policy: POL-PRD-EDIT-NARRATIVE
      x-events:
      - EVT-PRD-NARRATIVE-EDITED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_INVALID_STATE_TRANSITION
      - SECTION_NOT_EDITABLE
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
              $ref: '#/components/schemas/PrdEditNarrativeCommand'
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
  /api/v1/knowledge/products/{id}/actions/submit:
    post:
      operationId: CMD-PRD-SUBMIT
      summary: CMD-PRD-SUBMIT
      x-aggregate: AGG-PRODUCT
      x-policy: POL-PRD-SUBMIT
      x-events:
      - EVT-PRD-SUBMITTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_INCOMPLETE
      - PRODUCT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PrdSubmitCommand'
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
  /api/v1/knowledge/products/{id}/actions/return:
    post:
      operationId: CMD-PRD-RETURN
      summary: CMD-PRD-RETURN
      x-aggregate: AGG-PRODUCT
      x-policy: POL-PRD-RETURN
      x-events:
      - EVT-PRD-RETURNED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PrdReturnCommand'
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
  /api/v1/knowledge/products/{id}/actions/approve:
    post:
      operationId: CMD-PRD-APPROVE
      summary: CMD-PRD-APPROVE
      x-aggregate: AGG-PRODUCT
      x-policy: POL-PRD-APPROVE
      x-events:
      - EVT-PRD-APPROVED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PrdApproveCommand'
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
  /api/v1/knowledge/products/{id}/actions/withdraw:
    post:
      operationId: CMD-PRD-WITHDRAW
      summary: CMD-PRD-WITHDRAW
      x-aggregate: AGG-PRODUCT
      x-policy: POL-PRD-WITHDRAW
      x-events:
      - EVT-PRD-WITHDRAWN
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PrdWithdrawCommand'
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
  /api/v1/knowledge/products/{id}/actions/discard:
    post:
      operationId: CMD-PRD-DISCARD
      summary: CMD-PRD-DISCARD
      x-aggregate: AGG-PRODUCT
      x-policy: POL-PRD-DISCARD
      x-events:
      - EVT-PRD-DISCARDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PrdDiscardCommand'
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
  /api/v1/knowledge/distributions:
    post:
      operationId: CMD-DST-DISTRIBUTE
      summary: CMD-DST-DISTRIBUTE
      x-aggregate: AGG-DISTRIBUTION
      x-policy: POL-DST-DISTRIBUTE
      x-events:
      - EVT-DST-STARTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PRODUCT_NOT_APPROVED
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
              $ref: '#/components/schemas/DstDistributeCommand'
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
  /api/v1/knowledge/distributions/{id}/actions/cancel:
    post:
      operationId: CMD-DST-CANCEL
      summary: CMD-DST-CANCEL
      x-aggregate: AGG-DISTRIBUTION
      x-policy: POL-DST-CANCEL
      x-events:
      - EVT-DST-CANCELLED
      x-error-codes:
      - AUTHZ_DENIED
      - DISTRIBUTION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/DstCancelCommand'
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
  /api/v1/knowledge/knowledge-objects:
    post:
      operationId: CMD-KNO-DRAFT
      summary: CMD-KNO-DRAFT
      x-aggregate: AGG-KNOWLEDGE-OBJECT
      x-policy: POL-KNO-DRAFT
      x-events:
      - EVT-KNO-DRAFTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - KNOWLEDGE_INVALID
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
              $ref: '#/components/schemas/KnoDraftCommand'
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
      operationId: QRY-KNO-SEARCH
      summary: Published knowledge by type, text, relationships
      x-authorized: any user; label rule
      x-requirement: REQ-KNW-001
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
  /api/v1/knowledge/knowledge-objects/{id}/actions/edit:
    post:
      operationId: CMD-KNO-EDIT
      summary: CMD-KNO-EDIT
      x-aggregate: AGG-KNOWLEDGE-OBJECT
      x-policy: POL-KNO-EDIT
      x-events:
      - EVT-KNO-EDITED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - KNOWLEDGE_INVALID
      - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/KnoEditCommand'
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
  /api/v1/knowledge/knowledge-objects/{id}/actions/submit:
    post:
      operationId: CMD-KNO-SUBMIT
      summary: CMD-KNO-SUBMIT
      x-aggregate: AGG-KNOWLEDGE-OBJECT
      x-policy: POL-KNO-SUBMIT
      x-events:
      - EVT-KNO-SUBMITTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - KNOWLEDGE_INCOMPLETE
      - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/KnoSubmitCommand'
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
  /api/v1/knowledge/knowledge-objects/{id}/actions/return:
    post:
      operationId: CMD-KNO-RETURN
      summary: CMD-KNO-RETURN
      x-aggregate: AGG-KNOWLEDGE-OBJECT
      x-policy: POL-KNO-RETURN
      x-events:
      - EVT-KNO-RETURNED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/KnoReturnCommand'
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
  /api/v1/knowledge/knowledge-objects/{id}/actions/publish:
    post:
      operationId: CMD-KNO-PUBLISH
      summary: CMD-KNO-PUBLISH
      x-aggregate: AGG-KNOWLEDGE-OBJECT
      x-policy: POL-KNO-PUBLISH
      x-events:
      - EVT-KNO-PUBLISHED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/KnoPublishCommand'
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
  /api/v1/knowledge/knowledge-objects/{id}/actions/reject:
    post:
      operationId: CMD-KNO-REJECT
      summary: CMD-KNO-REJECT
      x-aggregate: AGG-KNOWLEDGE-OBJECT
      x-policy: POL-KNO-REJECT
      x-events:
      - EVT-KNO-REJECTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/KnoRejectCommand'
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
  /api/v1/knowledge/knowledge-objects/{id}/actions/record-reuse:
    post:
      operationId: CMD-KNO-RECORD-REUSE
      summary: CMD-KNO-RECORD-REUSE
      x-aggregate: AGG-KNOWLEDGE-OBJECT
      x-policy: POL-KNO-RECORD-REUSE
      x-events:
      - EVT-KNO-REUSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
      - TARGET_INVALID
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
              $ref: '#/components/schemas/KnoRecordReuseCommand'
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
  /api/v1/knowledge/knowledge-objects/{id}/actions/retire:
    post:
      operationId: CMD-KNO-RETIRE
      summary: CMD-KNO-RETIRE
      x-aggregate: AGG-KNOWLEDGE-OBJECT
      x-policy: POL-KNO-RETIRE
      x-events:
      - EVT-KNO-RETIRED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/KnoRetireCommand'
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
  /api/v1/knowledge/knowledge-objects/{id}/actions/discard:
    post:
      operationId: CMD-KNO-DISCARD
      summary: CMD-KNO-DISCARD
      x-aggregate: AGG-KNOWLEDGE-OBJECT
      x-policy: POL-KNO-DISCARD
      x-events:
      - EVT-KNO-DISCARDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/KnoDiscardCommand'
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
  /api/v1/knowledge/archive-packages/{id}/actions/retry-ingest:
    post:
      operationId: CMD-ARC-RETRY-INGEST
      summary: CMD-ARC-RETRY-INGEST
      x-aggregate: AGG-ARCHIVE-PACKAGE
      x-policy: POL-ARC-RETRY-INGEST
      x-events:
      - EVT-ARC-INGEST-STARTED
      x-error-codes:
      - ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/ArcRetryIngestCommand'
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
  /api/v1/knowledge/archive-packages/{id}/actions/repair:
    post:
      operationId: CMD-ARC-REPAIR
      summary: CMD-ARC-REPAIR
      x-aggregate: AGG-ARCHIVE-PACKAGE
      x-policy: POL-ARC-REPAIR
      x-events:
      - EVT-ARC-REPAIRED
      x-error-codes:
      - ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - FIXITY_MISMATCH
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
              $ref: '#/components/schemas/ArcRepairCommand'
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
  /api/v1/knowledge/archive-packages/{id}/actions/migrate-format:
    post:
      operationId: CMD-ARC-MIGRATE-FORMAT
      summary: CMD-ARC-MIGRATE-FORMAT
      x-aggregate: AGG-ARCHIVE-PACKAGE
      x-policy: POL-ARC-MIGRATE-FORMAT
      x-events:
      - EVT-ARC-FORMAT-MIGRATED
      x-error-codes:
      - ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - FORMAT_INVALID
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
              $ref: '#/components/schemas/ArcMigrateFormatCommand'
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
  /api/v1/knowledge/archive-packages/{id}/actions/transfer:
    post:
      operationId: CMD-ARC-TRANSFER
      summary: CMD-ARC-TRANSFER
      x-aggregate: AGG-ARCHIVE-PACKAGE
      x-policy: POL-ARC-TRANSFER
      x-events:
      - EVT-ARC-TRANSFERRED
      x-error-codes:
      - ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION
      - AUTHORITY_REQUIRED
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
              $ref: '#/components/schemas/ArcTransferCommand'
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
  /api/v1/knowledge/reconstructions:
    post:
      operationId: CMD-REC-REQUEST
      summary: CMD-REC-REQUEST
      x-aggregate: AGG-RECONSTRUCTION
      x-policy: POL-REC-REQUEST
      x-events:
      - EVT-REC-REQUESTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - RECONSTRUCTION_INVALID
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
              $ref: '#/components/schemas/RecRequestCommand'
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
  /api/v1/knowledge/reconstructions/{id}/actions/cancel:
    post:
      operationId: CMD-REC-CANCEL
      summary: CMD-REC-CANCEL
      x-aggregate: AGG-RECONSTRUCTION
      x-policy: POL-REC-CANCEL
      x-events:
      - EVT-REC-CANCELLED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - RECONSTRUCTION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/RecCancelCommand'
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
  /api/v1/knowledge/products/{product_id}:
    get:
      operationId: QRY-PRD-GET
      summary: Product version with rendered artifacts (download grants) and pinned
        citations
      x-authorized: audience + label rule
      x-requirement: REQ-PRD-003
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: product_id
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
  /api/v1/knowledge/products/{product_id}/distributions:
    get:
      operationId: QRY-DST-LOG
      summary: Distribution and delivery log with watermark ids
      x-authorized: distributor, Security Officer, Auditor
      x-requirement: REQ-PRD-004
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: product_id
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
  /api/v1/knowledge/knowledge-suggestions:
    post:
      operationId: QRY-KNO-SUGGEST
      summary: Published knowledge relevant to a task type / plan / area (by relationships)
      x-authorized: planner; label rule
      x-requirement: REQ-KNW-003
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
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
  /api/v1/knowledge/archive-packages:
    get:
      operationId: QRY-ARC-SEARCH
      summary: Archive catalogue (metadata only) by class, period, org
      x-authorized: Archivist; label rule
      x-requirement: REQ-ARC-003
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
  /api/v1/knowledge/archive-packages/{package_id}/retrievals:
    post:
      operationId: QRY-ARC-RETRIEVE
      summary: 'Retrieve package content (warm: signed grant; cold: staged job) —
        access logged'
      x-authorized: authorized by package label and purpose
      x-requirement: REQ-ARC-003
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: package_id
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
  /api/v1/knowledge/reconstructions/{reconstruction_id}/report:
    get:
      operationId: QRY-REC-REPORT
      summary: Labelled reconstruction report
      x-authorized: requester, Auditor
      x-requirement: REQ-ARC-004
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: reconstruction_id
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
        (challenge carries the required authentication strength as OIDC acr_values;
        retry with the same Idempotency-Key — ADR-P19)
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    Forbidden:
      description: AUTHZ_DENIED for a visible resource or a denied create / APPROVAL_REQUIRED
        with details.approver (ADR-P19)
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
      description: AUDIT_UNAVAILABLE (not retryable, no Retry-After) / POLICY_ENGINE_UNAVAILABLE
        / DEPENDENCY_UNAVAILABLE / context-specific dependency codes such as ELIGIBILITY_UNAVAILABLE
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
          properties:
            approver:
              type: string
              description: approver role (APPROVAL_REQUIRED, ADR-P19)
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
    PtmDefineCommand:
      type: object
      properties:
        code:
          type: string
        kind:
          type: string
          enum:
          - report
          - briefing
          - map_product
          - analytical_product
        name:
          $ref: '#/components/schemas/LocalizedName'
      additionalProperties: false
      required:
      - code
      - kind
      - name
    PtmEditCommand:
      type: object
      properties:
        sections:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/TemplateSection'
      additionalProperties: false
      required:
      - sections
    PtmActivateCommand:
      type: object
      properties:
        sample_ref:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - sample_ref
    PtmRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PrdCreateCommand:
      type: object
      properties:
        template:
          $ref: '#/components/schemas/Urn'
        parameters:
          type: object
        audience:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/Recipient'
        title:
          $ref: '#/components/schemas/LocalizedName'
        revises:
          $ref: '#/components/schemas/Urn'
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - template
      - parameters
      - audience
      - title
      - label
    PrdGenerateCommand:
      type: object
      properties: {}
      additionalProperties: false
    PrdEditNarrativeCommand:
      type: object
      properties:
        section_id:
          type: string
        text:
          $ref: '#/components/schemas/LocalizedName'
      additionalProperties: false
      required:
      - section_id
      - text
    PrdSubmitCommand:
      type: object
      properties: {}
      additionalProperties: false
    PrdReturnCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PrdApproveCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
    PrdWithdrawCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PrdDiscardCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    DstDistributeCommand:
      type: object
      properties:
        product:
          $ref: '#/components/schemas/Urn'
        recipients:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/Recipient'
        formats:
          type: array
          minItems: 1
          items:
            enum:
            - pdf
            - docx
            - in_app
        message:
          type: string
      additionalProperties: false
      required:
      - product
      - recipients
      - formats
    DstCancelCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    KnoDraftCommand:
      type: object
      properties:
        knowledge_type:
          type: string
          enum:
          - procedure
          - lesson
          - best_practice
          - policy_knowledge
        title:
          $ref: '#/components/schemas/LocalizedName'
        source:
          $ref: '#/components/schemas/Urn'
        revises:
          $ref: '#/components/schemas/Urn'
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - knowledge_type
      - title
      - label
    KnoEditCommand:
      type: object
      properties:
        statements:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/KnowledgeStatement'
        relationships:
          type: array
          items:
            $ref: '#/components/schemas/KnowledgeRelationship'
      additionalProperties: false
      required:
      - statements
    KnoSubmitCommand:
      type: object
      properties: {}
      additionalProperties: false
    KnoReturnCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    KnoPublishCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
    KnoRejectCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    KnoRecordReuseCommand:
      type: object
      properties:
        target:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - target
    KnoRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    KnoDiscardCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ArcRetryIngestCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
      required:
      - note
    ArcRepairCommand:
      type: object
      properties:
        replica_ref:
          type: string
      additionalProperties: false
      required:
      - replica_ref
    ArcMigrateFormatCommand:
      type: object
      properties:
        target_format:
          type: string
        reason:
          type: string
      additionalProperties: false
      required:
      - target_format
      - reason
    ArcTransferCommand:
      type: object
      properties:
        decision:
          $ref: '#/components/schemas/Urn'
        receiving_archive:
          type: string
        receipt:
          type: string
      additionalProperties: false
      required:
      - decision
      - receiving_archive
      - receipt
    RecRequestCommand:
      type: object
      properties:
        scope:
          $ref: '#/components/schemas/ReconstructionScope'
        valid_at:
          type: string
          format: date-time
        known_at:
          type: string
          format: date-time
        purpose:
          type: string
          enum:
          - audit
          - legal
          - lessons
          - analysis
      additionalProperties: false
      required:
      - scope
      - valid_at
      - known_at
      - purpose
    RecCancelCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TemplateSection:
      type: object
      required:
      - id
      - kind
      properties:
        id:
          type: string
        kind:
          enum:
          - text
          - map
          - chart
          - table
          - key_judgments
          - citations
        editable:
          type: boolean
        binding:
          type: object
          properties:
            query:
              type: string
              description: declared platform query id
            parameters:
              type: object
    Recipient:
      type: object
      required:
      - kind
      - ref
      properties:
        kind:
          enum:
          - user
          - org_unit
        ref:
          $ref: '#/components/schemas/Urn'
    KnowledgeStatement:
      type: object
      required:
      - text
      properties:
        text:
          $ref: '#/components/schemas/LocalizedName'
        evidence:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
        claims:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
    KnowledgeRelationship:
      type: object
      required:
      - kind
      - ref
      properties:
        kind:
          enum:
          - task_type
          - plan_type
          - entity_type
          - area
          - knowledge
        ref:
          type: string
    ReconstructionScope:
      type: object
      properties:
        objects:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
        situation:
          $ref: '#/components/schemas/Urn'
        plan:
          $ref: '#/components/schemas/Urn'
        decision_basis:
          $ref: '#/components/schemas/Urn'
```
