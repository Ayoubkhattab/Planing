---
id: OPENAPI-BC04-SLC17
type: api-contract
title: Operations API (BC04) — SLC-17
wave: W6
slice: SLC-17
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

# Operations API (BC04) — SLC-17

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_20 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/operations/risks` | CMD-RIS-IDENTIFY |
| GET | `/api/v1/operations/risks` | QRY-RIS-REGISTER |
| POST | `/api/v1/operations/risks/{id}/actions/assess` | CMD-RIS-ASSESS |
| POST | `/api/v1/operations/risks/{id}/actions/plan-treatment` | CMD-RIS-PLAN-TREATMENT |
| POST | `/api/v1/operations/risks/{id}/actions/reassess` | CMD-RIS-REASSESS |
| POST | `/api/v1/operations/risks/{id}/actions/close` | CMD-RIS-CLOSE |
| POST | `/api/v1/operations/incidents` | CMD-INC-REPORT |
| GET | `/api/v1/operations/incidents` | QRY-INC-LIST |
| POST | `/api/v1/operations/incidents/{id}/actions/assess` | CMD-INC-ASSESS |
| POST | `/api/v1/operations/incidents/{id}/actions/dispatch-response` | CMD-INC-DISPATCH-RESPONSE |
| POST | `/api/v1/operations/incidents/{id}/actions/contain` | CMD-INC-CONTAIN |
| POST | `/api/v1/operations/incidents/{id}/actions/resolve` | CMD-INC-RESOLVE |
| POST | `/api/v1/operations/incidents/{id}/actions/close` | CMD-INC-CLOSE |
| POST | `/api/v1/operations/incidents/{id}/actions/cancel` | CMD-INC-CANCEL |
| POST | `/api/v1/operations/incidents/{id}/actions/escalate` | CMD-INC-ESCALATE |
| POST | `/api/v1/operations/incidents/{id}/actions/de-escalate` | CMD-INC-DE-ESCALATE |
| POST | `/api/v1/operations/incidents/{id}/actions/activate-contingency` | CMD-INC-ACTIVATE-CONTINGENCY |
| GET | `/api/v1/operations/risks/{risk_id}` | QRY-RIS-GET |
| GET | `/api/v1/operations/incidents/{incident_id}` | QRY-INC-GET |
| GET | `/api/v1/operations/incidents/{incident_id}/recovery-status` | QRY-INC-RECOVERY-STATUS |

```yaml
openapi: 3.1.0
info:
  title: Operations API (BC04) — SLC-17
  version: 1.0.0
  description: Generated from SLC-17 domain specification. Do not edit by hand.
servers:
- url: https://{cell}.platform.local
  variables:
    cell:
      default: cell-1
security:
- bearer: []
paths:
  /api/v1/operations/risks:
    post:
      operationId: CMD-RIS-IDENTIFY
      summary: CMD-RIS-IDENTIFY
      x-aggregate: AGG-RISK
      x-policy: POL-RIS-IDENTIFY
      x-events:
      - EVT-RIS-IDENTIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - RISK_INVALID
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
              $ref: '#/components/schemas/RisIdentifyCommand'
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
      operationId: QRY-RIS-REGISTER
      summary: سجل المخاطر مصفّى بالفئة/النطاق/الدرجة
      x-authorized: allowed_scope
      x-requirement: REQ-RCM-014
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
  /api/v1/operations/risks/{id}/actions/assess:
    post:
      operationId: CMD-RIS-ASSESS
      summary: CMD-RIS-ASSESS
      x-aggregate: AGG-RISK
      x-policy: POL-RIS-ASSESS
      x-events:
      - EVT-RIS-ASSESSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - RISK_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/RisAssessCommand'
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
  /api/v1/operations/risks/{id}/actions/plan-treatment:
    post:
      operationId: CMD-RIS-PLAN-TREATMENT
      summary: CMD-RIS-PLAN-TREATMENT
      x-aggregate: AGG-RISK
      x-policy: POL-RIS-PLAN-TREATMENT
      x-events:
      - EVT-RIS-TREATMENT-PLANNED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - RISK_INVALID_STATE_TRANSITION
      - TREATMENT_INVALID
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
              $ref: '#/components/schemas/RisPlanTreatmentCommand'
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
  /api/v1/operations/risks/{id}/actions/reassess:
    post:
      operationId: CMD-RIS-REASSESS
      summary: CMD-RIS-REASSESS
      x-aggregate: AGG-RISK
      x-policy: POL-RIS-REASSESS
      x-events:
      - EVT-RIS-REASSESSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - RISK_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/RisReassessCommand'
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
  /api/v1/operations/risks/{id}/actions/close:
    post:
      operationId: CMD-RIS-CLOSE
      summary: CMD-RIS-CLOSE
      x-aggregate: AGG-RISK
      x-policy: POL-RIS-CLOSE
      x-events:
      - EVT-RIS-CLOSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - RATIONALE_REQUIRED
      - RISK_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/RisCloseCommand'
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
  /api/v1/operations/incidents:
    post:
      operationId: CMD-INC-REPORT
      summary: CMD-INC-REPORT
      x-aggregate: AGG-INCIDENT
      x-policy: POL-INC-REPORT
      x-events:
      - EVT-INC-REPORTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - INCIDENT_INVALID
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
              $ref: '#/components/schemas/IncReportCommand'
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
      operationId: QRY-INC-LIST
      summary: حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق
      x-authorized: allowed_scope
      x-requirement: REQ-RCM-015
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
  /api/v1/operations/incidents/{id}/actions/assess:
    post:
      operationId: CMD-INC-ASSESS
      summary: CMD-INC-ASSESS
      x-aggregate: AGG-INCIDENT
      x-policy: POL-INC-ASSESS
      x-events:
      - EVT-INC-ASSESSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - INCIDENT_INVALID
      - INCIDENT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/IncAssessCommand'
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
  /api/v1/operations/incidents/{id}/actions/dispatch-response:
    post:
      operationId: CMD-INC-DISPATCH-RESPONSE
      summary: CMD-INC-DISPATCH-RESPONSE
      x-aggregate: AGG-INCIDENT
      x-policy: POL-INC-DISPATCH-RESPONSE
      x-events:
      - EVT-INC-RESPONSE-DISPATCHED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - INCIDENT_INVALID_STATE_TRANSITION
      - RESPONSE_REQUIRED
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
              $ref: '#/components/schemas/IncDispatchResponseCommand'
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
  /api/v1/operations/incidents/{id}/actions/contain:
    post:
      operationId: CMD-INC-CONTAIN
      summary: CMD-INC-CONTAIN
      x-aggregate: AGG-INCIDENT
      x-policy: POL-INC-CONTAIN
      x-events:
      - EVT-INC-CONTAINED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - INCIDENT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/IncContainCommand'
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
  /api/v1/operations/incidents/{id}/actions/resolve:
    post:
      operationId: CMD-INC-RESOLVE
      summary: CMD-INC-RESOLVE
      x-aggregate: AGG-INCIDENT
      x-policy: POL-INC-RESOLVE
      x-events:
      - EVT-INC-RESOLVED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - INCIDENT_INVALID_STATE_TRANSITION
      - RESPONSE_TASKS_OPEN
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
              $ref: '#/components/schemas/IncResolveCommand'
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
  /api/v1/operations/incidents/{id}/actions/close:
    post:
      operationId: CMD-INC-CLOSE
      summary: CMD-INC-CLOSE
      x-aggregate: AGG-INCIDENT
      x-policy: POL-INC-CLOSE
      x-events:
      - EVT-INC-CLOSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - INCIDENT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/IncCloseCommand'
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
  /api/v1/operations/incidents/{id}/actions/cancel:
    post:
      operationId: CMD-INC-CANCEL
      summary: CMD-INC-CANCEL
      x-aggregate: AGG-INCIDENT
      x-policy: POL-INC-CANCEL
      x-events:
      - EVT-INC-CANCELLED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - INCIDENT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/IncCancelCommand'
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
  /api/v1/operations/incidents/{id}/actions/escalate:
    post:
      operationId: CMD-INC-ESCALATE
      summary: CMD-INC-ESCALATE
      x-aggregate: AGG-INCIDENT
      x-policy: POL-INC-ESCALATE
      x-events:
      - EVT-INC-ESCALATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - INCIDENT_INVALID_STATE_TRANSITION
      - SEVERITY_MUST_INCREASE
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
              $ref: '#/components/schemas/IncEscalateCommand'
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
  /api/v1/operations/incidents/{id}/actions/de-escalate:
    post:
      operationId: CMD-INC-DE-ESCALATE
      summary: CMD-INC-DE-ESCALATE
      x-aggregate: AGG-INCIDENT
      x-policy: POL-INC-DE-ESCALATE
      x-events:
      - EVT-INC-DE-ESCALATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - INCIDENT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/IncDeEscalateCommand'
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
  /api/v1/operations/incidents/{id}/actions/activate-contingency:
    post:
      operationId: CMD-INC-ACTIVATE-CONTINGENCY
      summary: CMD-INC-ACTIVATE-CONTINGENCY
      x-aggregate: AGG-INCIDENT
      x-policy: POL-INC-ACTIVATE-CONTINGENCY
      x-events:
      - EVT-INC-CONTINGENCY-ACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - INCIDENT_INVALID_STATE_TRANSITION
      - PLAN_LINK_INVALID
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
              $ref: '#/components/schemas/IncActivateContingencyCommand'
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
  /api/v1/operations/risks/{risk_id}:
    get:
      operationId: QRY-RIS-GET
      summary: Risk بنطاقه المرئي للطالب
      x-authorized: مالك النطاق؛ مدير المخاطر
      x-requirement: REQ-RCM-014
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: risk_id
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
  /api/v1/operations/incidents/{incident_id}:
    get:
      operationId: QRY-INC-GET
      summary: Incident بنطاقه المرئي للطالب
      x-authorized: allowed_scope
      x-requirement: REQ-RCM-015
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: incident_id
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
  /api/v1/operations/incidents/{incident_id}/recovery-status:
    get:
      operationId: QRY-INC-RECOVERY-STATUS
      summary: تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء
        الحادثة (RTO/RPO تقديرية)
      x-authorized: القائد؛ مالك الاستمرارية
      x-requirement: REQ-RCM-016
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: incident_id
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
    RisIdentifyCommand:
      type: object
      properties:
        category_ref:
          $ref: '#/components/schemas/Urn'
        description:
          $ref: '#/components/schemas/LocalizedName'
        scope_refs:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - category_ref
      - description
      - scope_refs
      - label
    RisAssessCommand:
      type: object
      properties:
        likelihood:
          type: integer
        impact:
          type: integer
      additionalProperties: false
      required:
      - likelihood
      - impact
    RisPlanTreatmentCommand:
      type: object
      properties:
        treatment_strategy:
          type: string
          enum:
          - avoid
          - reduce
          - transfer
          - accept
        treatment_task_refs:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
        approver:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - treatment_strategy
      - approver
    RisReassessCommand:
      type: object
      properties:
        likelihood:
          type: integer
        impact:
          type: integer
        reason:
          type: string
      additionalProperties: false
      required:
      - likelihood
      - impact
      - reason
    RisCloseCommand:
      type: object
      properties:
        rationale:
          type: string
          enum:
          - retired
          - accepted_permanently
          - materialized
        incident_ref:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - rationale
    IncReportCommand:
      type: object
      properties:
        category_ref:
          $ref: '#/components/schemas/Urn'
        description:
          $ref: '#/components/schemas/LocalizedName'
        scope_refs:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
        risk_ref:
          $ref: '#/components/schemas/Urn'
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - category_ref
      - description
      - scope_refs
      - label
    IncAssessCommand:
      type: object
      properties:
        severity:
          type: string
          enum:
          - MINOR
          - MAJOR
          - EMERGENCY
          - CRISIS
        affected_scope_refs:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - severity
      - affected_scope_refs
    IncDispatchResponseCommand:
      type: object
      properties:
        commander:
          $ref: '#/components/schemas/Urn'
        response_task_refs:
          type: array
          items:
            $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - commander
      - response_task_refs
    IncContainCommand:
      type: object
      properties:
        containment_note:
          type: string
      additionalProperties: false
      required:
      - containment_note
    IncResolveCommand:
      type: object
      properties:
        resolution_note:
          type: string
      additionalProperties: false
      required:
      - resolution_note
    IncCloseCommand:
      type: object
      properties:
        closing_note:
          type: string
        after_action_ref:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - closing_note
    IncCancelCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    IncEscalateCommand:
      type: object
      properties:
        reason:
          type: string
        new_severity:
          type: string
          enum:
          - MINOR
          - MAJOR
          - EMERGENCY
          - CRISIS
      additionalProperties: false
      required:
      - reason
      - new_severity
    IncDeEscalateCommand:
      type: object
      properties:
        reason:
          type: string
        new_severity:
          type: string
          enum:
          - MINOR
          - MAJOR
          - EMERGENCY
          - CRISIS
      additionalProperties: false
      required:
      - reason
      - new_severity
    IncActivateContingencyCommand:
      type: object
      properties:
        plan_template_ref:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - plan_template_ref
```
