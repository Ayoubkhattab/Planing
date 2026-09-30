---
id: OPENAPI-BC07-SLC10
type: api-contract
title: AI API (BC07) — SLC-10
wave: W6
slice: SLC-10
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

# AI API (BC07) — SLC-10

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_34 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/ai/requests` | CMD-AIR-SUBMIT |
| POST | `/api/v1/ai/requests/{id}/actions/cancel` | CMD-AIR-CANCEL |
| POST | `/api/v1/ai/results/{id}/actions/start-review` | CMD-AIRS-START-REVIEW |
| POST | `/api/v1/ai/results/{id}/actions/accept` | CMD-AIRS-ACCEPT |
| POST | `/api/v1/ai/results/{id}/actions/accept-partially` | CMD-AIRS-ACCEPT-PARTIALLY |
| POST | `/api/v1/ai/results/{id}/actions/reject` | CMD-AIRS-REJECT |
| POST | `/api/v1/ai/models` | CMD-MDL-REGISTER |
| GET | `/api/v1/ai/models` | QRY-MDL-LIST |
| POST | `/api/v1/ai/models/{id}/actions/start-evaluation` | CMD-MDL-START-EVALUATION |
| POST | `/api/v1/ai/models/{id}/actions/approve` | CMD-MDL-APPROVE |
| POST | `/api/v1/ai/models/{id}/actions/fail-evaluation` | CMD-MDL-FAIL-EVALUATION |
| POST | `/api/v1/ai/models/{id}/actions/stage` | CMD-MDL-STAGE |
| POST | `/api/v1/ai/models/{id}/actions/promote` | CMD-MDL-PROMOTE |
| POST | `/api/v1/ai/models/{id}/actions/deprecate` | CMD-MDL-DEPRECATE |
| POST | `/api/v1/ai/models/{id}/actions/reinstate` | CMD-MDL-REINSTATE |
| POST | `/api/v1/ai/models/{id}/actions/retire` | CMD-MDL-RETIRE |
| POST | `/api/v1/ai/routings` | CMD-RTG-DRAFT |
| POST | `/api/v1/ai/routings/{id}/actions/edit` | CMD-RTG-EDIT |
| POST | `/api/v1/ai/routings/{id}/actions/activate` | CMD-RTG-ACTIVATE |
| POST | `/api/v1/ai/routings/{id}/actions/discard` | CMD-RTG-DISCARD |
| POST | `/api/v1/ai/tools` | CMD-TOL-REGISTER |
| GET | `/api/v1/ai/tools` | QRY-TOL-LIST |
| POST | `/api/v1/ai/tools/{id}/actions/activate` | CMD-TOL-ACTIVATE |
| POST | `/api/v1/ai/tools/{id}/actions/disable` | CMD-TOL-DISABLE |
| POST | `/api/v1/ai/tools/{id}/actions/enable` | CMD-TOL-ENABLE |
| POST | `/api/v1/ai/tools/{id}/actions/retire` | CMD-TOL-RETIRE |
| POST | `/api/v1/ai/evaluation-suites` | CMD-EVS-DRAFT |
| POST | `/api/v1/ai/evaluation-suites/{id}/actions/edit` | CMD-EVS-EDIT |
| POST | `/api/v1/ai/evaluation-suites/{id}/actions/activate` | CMD-EVS-ACTIVATE |
| GET | `/api/v1/ai/requests/{request_id}` | QRY-AIR-GET |
| GET | `/api/v1/ai/requests/{request_id}/context` | QRY-AIR-CONTEXT |
| GET | `/api/v1/ai/results` | QRY-AIRS-QUEUE |
| GET | `/api/v1/ai/routing` | QRY-RTG-ACTIVE |
| GET | `/api/v1/ai/usage` | QRY-AI-USAGE |

```yaml
openapi: 3.1.0
info:
  title: AI API (BC07) — SLC-10
  version: 1.0.0
  description: Generated from SLC-10 domain specification. Do not edit by hand.
servers:
- url: https://{cell}.platform.local
  variables:
    cell:
      default: cell-1
security:
- bearer: []
paths:
  /api/v1/ai/requests:
    post:
      operationId: CMD-AIR-SUBMIT
      summary: CMD-AIR-SUBMIT
      x-aggregate: AGG-AI-REQUEST
      x-policy: POL-AIR-SUBMIT
      x-events:
      - EVT-AIR-RECEIVED
      x-error-codes:
      - AI_OPERATION_NOT_ALLOWED
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
              $ref: '#/components/schemas/AirSubmitCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/requests/{id}/actions/cancel:
    post:
      operationId: CMD-AIR-CANCEL
      summary: CMD-AIR-CANCEL
      x-aggregate: AGG-AI-REQUEST
      x-policy: POL-AIR-CANCEL
      x-events:
      - EVT-AIR-CANCELLED
      x-error-codes:
      - AI_REQUEST_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/AirCancelCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/results/{id}/actions/start-review:
    post:
      operationId: CMD-AIRS-START-REVIEW
      summary: CMD-AIRS-START-REVIEW
      x-aggregate: AGG-AI-RESULT
      x-policy: POL-AIRS-START-REVIEW
      x-events:
      - EVT-AIRS-REVIEW-STARTED
      x-error-codes:
      - AI_RESULT_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REVIEWER_NOT_CLEARED
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
              $ref: '#/components/schemas/AirsStartReviewCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/results/{id}/actions/accept:
    post:
      operationId: CMD-AIRS-ACCEPT
      summary: CMD-AIRS-ACCEPT
      x-aggregate: AGG-AI-RESULT
      x-policy: POL-AIRS-ACCEPT
      x-events:
      - EVT-AIRS-ACCEPTED
      x-error-codes:
      - AI_RESULT_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - OWNER_REJECTED
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
              $ref: '#/components/schemas/AirsAcceptCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/results/{id}/actions/accept-partially:
    post:
      operationId: CMD-AIRS-ACCEPT-PARTIALLY
      summary: CMD-AIRS-ACCEPT-PARTIALLY
      x-aggregate: AGG-AI-RESULT
      x-policy: POL-AIRS-ACCEPT-PARTIALLY
      x-events:
      - EVT-AIRS-PARTIALLY-ACCEPTED
      x-error-codes:
      - AI_RESULT_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - OWNER_REJECTED
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
              $ref: '#/components/schemas/AirsAcceptPartiallyCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/results/{id}/actions/reject:
    post:
      operationId: CMD-AIRS-REJECT
      summary: CMD-AIRS-REJECT
      x-aggregate: AGG-AI-RESULT
      x-policy: POL-AIRS-REJECT
      x-events:
      - EVT-AIRS-REJECTED
      x-error-codes:
      - AI_RESULT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/AirsRejectCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/models:
    post:
      operationId: CMD-MDL-REGISTER
      summary: CMD-MDL-REGISTER
      x-aggregate: AGG-MODEL-VERSION
      x-policy: POL-MDL-REGISTER
      x-events:
      - EVT-MDL-REGISTERED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - MODEL_INVALID
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
              $ref: '#/components/schemas/MdlRegisterCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
    get:
      operationId: QRY-MDL-LIST
      summary: Model versions with state, evaluation summary, hosting
      x-authorized: AI governance, Auditor
      x-requirement: REQ-AI-009
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
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/models/{id}/actions/start-evaluation:
    post:
      operationId: CMD-MDL-START-EVALUATION
      summary: CMD-MDL-START-EVALUATION
      x-aggregate: AGG-MODEL-VERSION
      x-policy: POL-MDL-START-EVALUATION
      x-events:
      - EVT-MDL-EVALUATION-STARTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - MODEL_VERSION_INVALID_STATE_TRANSITION
      - SUITE_NOT_ACTIVE
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
              $ref: '#/components/schemas/MdlStartEvaluationCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/models/{id}/actions/approve:
    post:
      operationId: CMD-MDL-APPROVE
      summary: CMD-MDL-APPROVE
      x-aggregate: AGG-MODEL-VERSION
      x-policy: POL-MDL-APPROVE
      x-events:
      - EVT-MDL-APPROVED
      x-error-codes:
      - AUTHZ_DENIED
      - EVALUATION_BELOW_THRESHOLD
      - IDEMPOTENCY_KEY_REUSED
      - MODEL_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/MdlApproveCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/models/{id}/actions/fail-evaluation:
    post:
      operationId: CMD-MDL-FAIL-EVALUATION
      summary: CMD-MDL-FAIL-EVALUATION
      x-aggregate: AGG-MODEL-VERSION
      x-policy: POL-MDL-FAIL-EVALUATION
      x-events:
      - EVT-MDL-EVALUATION-FAILED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - MODEL_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/MdlFailEvaluationCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/models/{id}/actions/stage:
    post:
      operationId: CMD-MDL-STAGE
      summary: CMD-MDL-STAGE
      x-aggregate: AGG-MODEL-VERSION
      x-policy: POL-MDL-STAGE
      x-events:
      - EVT-MDL-STAGED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - MODEL_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/MdlStageCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/models/{id}/actions/promote:
    post:
      operationId: CMD-MDL-PROMOTE
      summary: CMD-MDL-PROMOTE
      x-aggregate: AGG-MODEL-VERSION
      x-policy: POL-MDL-PROMOTE
      x-events:
      - EVT-MDL-PROMOTED
      x-error-codes:
      - AUTHZ_DENIED
      - CANARY_BELOW_THRESHOLD
      - IDEMPOTENCY_KEY_REUSED
      - MODEL_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/MdlPromoteCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/models/{id}/actions/deprecate:
    post:
      operationId: CMD-MDL-DEPRECATE
      summary: CMD-MDL-DEPRECATE
      x-aggregate: AGG-MODEL-VERSION
      x-policy: POL-MDL-DEPRECATE
      x-events:
      - EVT-MDL-DEPRECATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - MODEL_IN_ACTIVE_ROUTE
      - MODEL_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/MdlDeprecateCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/models/{id}/actions/reinstate:
    post:
      operationId: CMD-MDL-REINSTATE
      summary: CMD-MDL-REINSTATE
      x-aggregate: AGG-MODEL-VERSION
      x-policy: POL-MDL-REINSTATE
      x-events:
      - EVT-MDL-REINSTATED
      x-error-codes:
      - AUTHZ_DENIED
      - EVALUATION_TOO_OLD
      - IDEMPOTENCY_KEY_REUSED
      - MODEL_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/MdlReinstateCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/models/{id}/actions/retire:
    post:
      operationId: CMD-MDL-RETIRE
      summary: CMD-MDL-RETIRE
      x-aggregate: AGG-MODEL-VERSION
      x-policy: POL-MDL-RETIRE
      x-events:
      - EVT-MDL-RETIRED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - MODEL_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/MdlRetireCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/routings:
    post:
      operationId: CMD-RTG-DRAFT
      summary: CMD-RTG-DRAFT
      x-aggregate: AGG-AI-ROUTING
      x-policy: POL-RTG-DRAFT
      x-events:
      - EVT-RTG-DRAFTED
      x-error-codes:
      - AUTHZ_DENIED
      - DRAFT_EXISTS
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
              $ref: '#/components/schemas/RtgDraftCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/routings/{id}/actions/edit:
    post:
      operationId: CMD-RTG-EDIT
      summary: CMD-RTG-EDIT
      x-aggregate: AGG-AI-ROUTING
      x-policy: POL-RTG-EDIT
      x-events:
      - EVT-RTG-EDITED
      x-error-codes:
      - AI_ROUTING_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ROUTING_INVALID
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
              $ref: '#/components/schemas/RtgEditCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/routings/{id}/actions/activate:
    post:
      operationId: CMD-RTG-ACTIVATE
      summary: CMD-RTG-ACTIVATE
      x-aggregate: AGG-AI-ROUTING
      x-policy: POL-RTG-ACTIVATE
      x-events:
      - EVT-RTG-ACTIVATED
      x-error-codes:
      - AI_ROUTING_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
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
              $ref: '#/components/schemas/RtgActivateCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/routings/{id}/actions/discard:
    post:
      operationId: CMD-RTG-DISCARD
      summary: CMD-RTG-DISCARD
      x-aggregate: AGG-AI-ROUTING
      x-policy: POL-RTG-DISCARD
      x-events:
      - EVT-RTG-DISCARDED
      x-error-codes:
      - AI_ROUTING_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/RtgDiscardCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/tools:
    post:
      operationId: CMD-TOL-REGISTER
      summary: CMD-TOL-REGISTER
      x-aggregate: AGG-AI-TOOL
      x-policy: POL-TOL-REGISTER
      x-events:
      - EVT-TOL-REGISTERED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TOOL_INVALID
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
              $ref: '#/components/schemas/TolRegisterCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
    get:
      operationId: QRY-TOL-LIST
      summary: Tool registry
      x-authorized: AI governance, Security Officer
      x-requirement: REQ-AI-013
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
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/tools/{id}/actions/activate:
    post:
      operationId: CMD-TOL-ACTIVATE
      summary: CMD-TOL-ACTIVATE
      x-aggregate: AGG-AI-TOOL
      x-policy: POL-TOL-ACTIVATE
      x-events:
      - EVT-TOL-ACTIVATED
      x-error-codes:
      - AI_TOOL_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SECURITY_REVIEW_REQUIRED
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
              $ref: '#/components/schemas/TolActivateCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/tools/{id}/actions/disable:
    post:
      operationId: CMD-TOL-DISABLE
      summary: CMD-TOL-DISABLE
      x-aggregate: AGG-AI-TOOL
      x-policy: POL-TOL-DISABLE
      x-events:
      - EVT-TOL-DISABLED
      x-error-codes:
      - AI_TOOL_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/TolDisableCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/tools/{id}/actions/enable:
    post:
      operationId: CMD-TOL-ENABLE
      summary: CMD-TOL-ENABLE
      x-aggregate: AGG-AI-TOOL
      x-policy: POL-TOL-ENABLE
      x-events:
      - EVT-TOL-ENABLED
      x-error-codes:
      - AI_TOOL_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/TolEnableCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/tools/{id}/actions/retire:
    post:
      operationId: CMD-TOL-RETIRE
      summary: CMD-TOL-RETIRE
      x-aggregate: AGG-AI-TOOL
      x-policy: POL-TOL-RETIRE
      x-events:
      - EVT-TOL-RETIRED
      x-error-codes:
      - AI_TOOL_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/TolRetireCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/evaluation-suites:
    post:
      operationId: CMD-EVS-DRAFT
      summary: CMD-EVS-DRAFT
      x-aggregate: AGG-EVAL-SUITE
      x-policy: POL-EVS-DRAFT
      x-events:
      - EVT-EVS-DRAFTED
      x-error-codes:
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
              $ref: '#/components/schemas/EvsDraftCommand'
      responses:
        '201':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/evaluation-suites/{id}/actions/edit:
    post:
      operationId: CMD-EVS-EDIT
      summary: CMD-EVS-EDIT
      x-aggregate: AGG-EVAL-SUITE
      x-policy: POL-EVS-EDIT
      x-events:
      - EVT-EVS-EDITED
      x-error-codes:
      - AUTHZ_DENIED
      - EVAL_SUITE_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - SUITE_INVALID
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
              $ref: '#/components/schemas/EvsEditCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/evaluation-suites/{id}/actions/activate:
    post:
      operationId: CMD-EVS-ACTIVATE
      summary: CMD-EVS-ACTIVATE
      x-aggregate: AGG-EVAL-SUITE
      x-policy: POL-EVS-ACTIVATE
      x-events:
      - EVT-EVS-ACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - EVAL_SUITE_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
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
              $ref: '#/components/schemas/EvsActivateCommand'
      responses:
        '202':
          description: accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceRef'
        '400':
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/requests/{request_id}:
    get:
      operationId: QRY-AIR-GET
      summary: Request with answer, statements and citations (visible only), status
      x-authorized: requester; Auditor (metadata)
      x-requirement: REQ-AI-001
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: request_id
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
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/requests/{request_id}/context:
    get:
      operationId: QRY-AIR-CONTEXT
      summary: Context package items (URN, version, label) — for audit and review
      x-authorized: requester if cleared; Auditor
      x-requirement: REQ-AI-002
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: request_id
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
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/results:
    get:
      operationId: QRY-AIRS-QUEUE
      summary: Reviewable AI results by state, operation, target
      x-authorized: reviewers authorized on targets
      x-requirement: REQ-AI-005
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
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/routing:
    get:
      operationId: QRY-RTG-ACTIVE
      summary: Active routing for the tenant
      x-authorized: AI governance, Security Officer
      x-requirement: REQ-AI-008
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
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
  /api/v1/ai/usage:
    get:
      operationId: QRY-AI-USAGE
      summary: GPU-hours, requests, cost indicators per tenant and operation
      x-authorized: Administrator, finance
      x-requirement: REQ-AI-001
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
          description: VALIDATION_FAILED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '404':
          description: NOT_FOUND (also returned for forbidden resources — ADR-P06
            §5)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '409':
          description: state transition or version conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '422':
          description: guard failed / idempotency key reused
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '429':
          description: RATE_LIMITED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
        '503':
          description: AUDIT_UNAVAILABLE / dependency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
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
    AirSubmitCommand:
      type: object
      properties:
        operation:
          type: string
        input:
          $ref: '#/components/schemas/LocalizedName'
        scope:
          type: object
        purpose:
          type: string
        target:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - operation
      - input
      - purpose
    AirCancelCommand:
      type: object
      properties: {}
      additionalProperties: false
    AirsStartReviewCommand:
      type: object
      properties: {}
      additionalProperties: false
    AirsAcceptCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
    AirsAcceptPartiallyCommand:
      type: object
      properties:
        accepted_items:
          type: array
          items:
            type: string
        rejected_items:
          type: array
          items:
            type: string
      additionalProperties: false
      required:
      - accepted_items
      - rejected_items
    AirsRejectCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    MdlRegisterCommand:
      type: object
      properties:
        family:
          type: string
        version:
          type: string
        weights_digest:
          type: string
        licence:
          type: string
        languages:
          type: array
          items:
            type: string
        context_tokens:
          type: integer
        hosting:
          type: string
          enum:
          - local
          - external_allowed
        roles:
          type: array
          items:
            type: string
      additionalProperties: false
      required:
      - family
      - version
      - weights_digest
      - licence
      - languages
      - context_tokens
      - hosting
      - roles
    MdlStartEvaluationCommand:
      type: object
      properties:
        suite:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - suite
    MdlApproveCommand:
      type: object
      properties:
        report:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - report
    MdlFailEvaluationCommand:
      type: object
      properties:
        report:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - report
    MdlStageCommand:
      type: object
      properties:
        canary_share:
          type: number
          minimum: 0
          maximum: 0.1
        operations:
          type: array
          items:
            type: string
      additionalProperties: false
      required:
      - canary_share
      - operations
    MdlPromoteCommand:
      type: object
      properties:
        canary_report:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - canary_report
    MdlDeprecateCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    MdlReinstateCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    MdlRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    RtgDraftCommand:
      type: object
      properties:
        based_on:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
    RtgEditCommand:
      type: object
      properties:
        routes:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/Route'
      additionalProperties: false
      required:
      - routes
    RtgActivateCommand:
      type: object
      properties: {}
      additionalProperties: false
    RtgDiscardCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TolRegisterCommand:
      type: object
      properties:
        name:
          type: string
        description:
          $ref: '#/components/schemas/LocalizedName'
        input_schema:
          type: object
        binding:
          type: string
        effect:
          type: string
          enum:
          - read
          - propose
        permission:
          type: string
        max_ail:
          type: integer
          minimum: 0
          maximum: 3
      additionalProperties: false
      required:
      - name
      - description
      - input_schema
      - binding
      - effect
      - permission
      - max_ail
    TolActivateCommand:
      type: object
      properties:
        review_ref:
          type: string
      additionalProperties: false
      required:
      - review_ref
    TolDisableCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TolEnableCommand:
      type: object
      properties: {}
      additionalProperties: false
    TolRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    EvsDraftCommand:
      type: object
      properties:
        based_on:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
    EvsEditCommand:
      type: object
      properties:
        sets:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/EvalSet'
      additionalProperties: false
      required:
      - sets
    EvsActivateCommand:
      type: object
      properties: {}
      additionalProperties: false
    Route:
      type: object
      required:
      - operation
      - model
      - prompt_template
      - max_ail
      properties:
        operation:
          type: string
          description: AI-OP-* from autonomy matrix
        model:
          $ref: '#/components/schemas/Urn'
        prompt_template:
          type: string
        allowed_tools:
          type: array
          items:
            type: string
        max_ail:
          type: integer
          minimum: 0
          maximum: 4
        external_allowed:
          type: boolean
          default: false
    EvalSet:
      type: object
      required:
      - kind
      - items_ref
      properties:
        kind:
          enum:
          - groundedness
          - citation
          - insufficient_evidence
          - prompt_injection
          - exfiltration
          - cross_tenant
          - language
        items_ref:
          $ref: '#/components/schemas/Urn'
        size:
          type: integer
          minimum: 1
```
