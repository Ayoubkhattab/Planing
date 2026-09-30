---
id: OPENAPI-BC04-SLC08
type: api-contract
title: Operations API (BC04) — SLC-08
wave: W6
slice: SLC-08
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

# Operations API (BC04) — SLC-08

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_33 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/operations/decision-requests` | CMD-DRQ-CREATE |
| GET | `/api/v1/operations/decision-requests` | QRY-DRQ-LIST |
| POST | `/api/v1/operations/decision-requests/{id}/actions/add-option` | CMD-DRQ-ADD-OPTION |
| POST | `/api/v1/operations/decision-requests/{id}/actions/cite` | CMD-DRQ-CITE |
| POST | `/api/v1/operations/decision-requests/{id}/actions/open` | CMD-DRQ-OPEN |
| POST | `/api/v1/operations/decision-requests/{id}/actions/withdraw` | CMD-DRQ-WITHDRAW |
| POST | `/api/v1/operations/decisions` | CMD-DEC-RECORD |
| POST | `/api/v1/operations/decisions/{id}/actions/annul` | CMD-DEC-ANNUL |
| POST | `/api/v1/operations/plans` | CMD-PLN-CREATE |
| POST | `/api/v1/operations/plans/{id}/actions/suspend` | CMD-PLN-SUSPEND |
| POST | `/api/v1/operations/plans/{id}/actions/resume` | CMD-PLN-RESUME |
| POST | `/api/v1/operations/plans/{id}/actions/complete` | CMD-PLN-COMPLETE |
| POST | `/api/v1/operations/plans/{id}/actions/close` | CMD-PLN-CLOSE |
| POST | `/api/v1/operations/plans/{id}/actions/cancel` | CMD-PLN-CANCEL |
| POST | `/api/v1/operations/plans/{id}/actions/reclassify` | CMD-PLN-RECLASSIFY |
| POST | `/api/v1/operations/plan-versions` | CMD-PLV-DRAFT |
| POST | `/api/v1/operations/plan-versions/{id}/actions/edit` | CMD-PLV-EDIT |
| POST | `/api/v1/operations/plan-versions/{id}/actions/submit` | CMD-PLV-SUBMIT |
| POST | `/api/v1/operations/plan-versions/{id}/actions/return` | CMD-PLV-RETURN |
| POST | `/api/v1/operations/plan-versions/{id}/actions/approve` | CMD-PLV-APPROVE |
| POST | `/api/v1/operations/plan-versions/{id}/actions/reject` | CMD-PLV-REJECT |
| POST | `/api/v1/operations/plan-versions/{id}/actions/amend-minor` | CMD-PLV-AMEND-MINOR |
| POST | `/api/v1/operations/plan-versions/{id}/actions/discard` | CMD-PLV-DISCARD |
| POST | `/api/v1/operations/outcome-trackers/{id}/actions/record` | CMD-OUT-RECORD |
| POST | `/api/v1/operations/outcome-trackers/{id}/actions/correct` | CMD-OUT-CORRECT |
| GET | `/api/v1/operations/decision-requests/{request_id}` | QRY-DRQ-GET |
| GET | `/api/v1/operations/decisions/{decision_id}` | QRY-DEC-GET |
| GET | `/api/v1/operations/decisions/{decision_id}/basis` | QRY-DEC-BASIS |
| GET | `/api/v1/operations/plans/{plan_id}` | QRY-PLN-GET |
| GET | `/api/v1/operations/plans/{plan_id}/versions` | QRY-PLV-LIST |
| GET | `/api/v1/operations/plans/{plan_id}/versions/{version}/diff` | QRY-PLV-DIFF |
| GET | `/api/v1/operations/plans/{plan_id}/progress` | QRY-PLN-PROGRESS |
| GET | `/api/v1/operations/plans/{plan_id}/outcomes/{outcome_id}/measurements` | QRY-OUT-SERIES |

```yaml
openapi: 3.1.0
info:
  title: Operations API (BC04) — SLC-08
  version: 1.0.0
  description: Generated from SLC-08 domain specification. Do not edit by hand.
servers:
- url: https://{cell}.platform.local
  variables:
    cell:
      default: cell-1
security:
- bearer: []
paths:
  /api/v1/operations/decision-requests:
    post:
      operationId: CMD-DRQ-CREATE
      summary: CMD-DRQ-CREATE
      x-aggregate: AGG-DECISION-REQUEST
      x-policy: POL-DRQ-CREATE
      x-events:
      - EVT-DRQ-CREATED
      x-error-codes:
      - AUTHZ_DENIED
      - DECISION_REQUEST_INVALID
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
              $ref: '#/components/schemas/DrqCreateCommand'
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
      operationId: QRY-DRQ-LIST
      summary: My pending requests (as authority holder), by deadline
      x-authorized: allowed_scope
      x-requirement: REQ-DEC-001
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
  /api/v1/operations/decision-requests/{id}/actions/add-option:
    post:
      operationId: CMD-DRQ-ADD-OPTION
      summary: CMD-DRQ-ADD-OPTION
      x-aggregate: AGG-DECISION-REQUEST
      x-policy: POL-DRQ-ADD-OPTION
      x-events:
      - EVT-DRQ-OPTION-ADDED
      x-error-codes:
      - AUTHZ_DENIED
      - DECISION_REQUEST_INVALID
      - DECISION_REQUEST_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/DrqAddOptionCommand'
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
  /api/v1/operations/decision-requests/{id}/actions/cite:
    post:
      operationId: CMD-DRQ-CITE
      summary: CMD-DRQ-CITE
      x-aggregate: AGG-DECISION-REQUEST
      x-policy: POL-DRQ-CITE
      x-events:
      - EVT-DRQ-CITED
      x-error-codes:
      - AUTHZ_DENIED
      - CITATION_ABOVE_LABEL
      - DECISION_REQUEST_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/DrqCiteCommand'
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
  /api/v1/operations/decision-requests/{id}/actions/open:
    post:
      operationId: CMD-DRQ-OPEN
      summary: CMD-DRQ-OPEN
      x-aggregate: AGG-DECISION-REQUEST
      x-policy: POL-DRQ-OPEN
      x-events:
      - EVT-DRQ-OPENED
      x-error-codes:
      - AUTHZ_DENIED
      - DECISION_REQUEST_INCOMPLETE
      - DECISION_REQUEST_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/DrqOpenCommand'
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
  /api/v1/operations/decision-requests/{id}/actions/withdraw:
    post:
      operationId: CMD-DRQ-WITHDRAW
      summary: CMD-DRQ-WITHDRAW
      x-aggregate: AGG-DECISION-REQUEST
      x-policy: POL-DRQ-WITHDRAW
      x-events:
      - EVT-DRQ-WITHDRAWN
      x-error-codes:
      - AUTHZ_DENIED
      - DECISION_REQUEST_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/DrqWithdrawCommand'
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
  /api/v1/operations/decisions:
    post:
      operationId: CMD-DEC-RECORD
      summary: CMD-DEC-RECORD
      x-aggregate: AGG-DECISION
      x-policy: POL-DEC-RECORD
      x-events:
      - EVT-DEC-RECORDED
      x-error-codes:
      - AUTHORITY_REQUIRED
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
              $ref: '#/components/schemas/DecRecordCommand'
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
  /api/v1/operations/decisions/{id}/actions/annul:
    post:
      operationId: CMD-DEC-ANNUL
      summary: CMD-DEC-ANNUL
      x-aggregate: AGG-DECISION
      x-policy: POL-DEC-ANNUL
      x-events:
      - EVT-DEC-ANNULLED
      x-error-codes:
      - AUTHORITY_REQUIRED
      - AUTHZ_DENIED
      - DECISION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/DecAnnulCommand'
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
  /api/v1/operations/plans:
    post:
      operationId: CMD-PLN-CREATE
      summary: CMD-PLN-CREATE
      x-aggregate: AGG-PLAN
      x-policy: POL-PLN-CREATE
      x-events:
      - EVT-PLN-CREATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_INVALID
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
              $ref: '#/components/schemas/PlnCreateCommand'
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
  /api/v1/operations/plans/{id}/actions/suspend:
    post:
      operationId: CMD-PLN-SUSPEND
      summary: CMD-PLN-SUSPEND
      x-aggregate: AGG-PLAN
      x-policy: POL-PLN-SUSPEND
      x-events:
      - EVT-PLN-SUSPENDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlnSuspendCommand'
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
  /api/v1/operations/plans/{id}/actions/resume:
    post:
      operationId: CMD-PLN-RESUME
      summary: CMD-PLN-RESUME
      x-aggregate: AGG-PLAN
      x-policy: POL-PLN-RESUME
      x-events:
      - EVT-PLN-RESUMED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlnResumeCommand'
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
  /api/v1/operations/plans/{id}/actions/complete:
    post:
      operationId: CMD-PLN-COMPLETE
      summary: CMD-PLN-COMPLETE
      x-aggregate: AGG-PLAN
      x-policy: POL-PLN-COMPLETE
      x-events:
      - EVT-PLN-COMPLETED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_INVALID_STATE_TRANSITION
      - PLAN_NOT_COMPLETABLE
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
              $ref: '#/components/schemas/PlnCompleteCommand'
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
  /api/v1/operations/plans/{id}/actions/close:
    post:
      operationId: CMD-PLN-CLOSE
      summary: CMD-PLN-CLOSE
      x-aggregate: AGG-PLAN
      x-policy: POL-PLN-CLOSE
      x-events:
      - EVT-PLN-CLOSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlnCloseCommand'
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
  /api/v1/operations/plans/{id}/actions/cancel:
    post:
      operationId: CMD-PLN-CANCEL
      summary: CMD-PLN-CANCEL
      x-aggregate: AGG-PLAN
      x-policy: POL-PLN-CANCEL
      x-events:
      - EVT-PLN-CANCELLED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlnCancelCommand'
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
  /api/v1/operations/plans/{id}/actions/reclassify:
    post:
      operationId: CMD-PLN-RECLASSIFY
      summary: CMD-PLN-RECLASSIFY
      x-aggregate: AGG-PLAN
      x-policy: POL-PLN-RECLASSIFY
      x-events:
      - EVT-PLN-RECLASSIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlnReclassifyCommand'
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
  /api/v1/operations/plan-versions:
    post:
      operationId: CMD-PLV-DRAFT
      summary: CMD-PLV-DRAFT
      x-aggregate: AGG-PLAN-VERSION
      x-policy: POL-PLV-DRAFT
      x-events:
      - EVT-PLV-DRAFTED
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
              $ref: '#/components/schemas/PlvDraftCommand'
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
  /api/v1/operations/plan-versions/{id}/actions/edit:
    post:
      operationId: CMD-PLV-EDIT
      summary: CMD-PLV-EDIT
      x-aggregate: AGG-PLAN-VERSION
      x-policy: POL-PLV-EDIT
      x-events:
      - EVT-PLV-EDITED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_VERSION_INVALID
      - PLAN_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlvEditCommand'
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
  /api/v1/operations/plan-versions/{id}/actions/submit:
    post:
      operationId: CMD-PLV-SUBMIT
      summary: CMD-PLV-SUBMIT
      x-aggregate: AGG-PLAN-VERSION
      x-policy: POL-PLV-SUBMIT
      x-events:
      - EVT-PLV-SUBMITTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_VERSION_INCOMPLETE
      - PLAN_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlvSubmitCommand'
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
  /api/v1/operations/plan-versions/{id}/actions/return:
    post:
      operationId: CMD-PLV-RETURN
      summary: CMD-PLV-RETURN
      x-aggregate: AGG-PLAN-VERSION
      x-policy: POL-PLV-RETURN
      x-events:
      - EVT-PLV-RETURNED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlvReturnCommand'
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
  /api/v1/operations/plan-versions/{id}/actions/approve:
    post:
      operationId: CMD-PLV-APPROVE
      summary: CMD-PLV-APPROVE
      x-aggregate: AGG-PLAN-VERSION
      x-policy: POL-PLV-APPROVE
      x-events:
      - EVT-PLV-BASELINED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlvApproveCommand'
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
  /api/v1/operations/plan-versions/{id}/actions/reject:
    post:
      operationId: CMD-PLV-REJECT
      summary: CMD-PLV-REJECT
      x-aggregate: AGG-PLAN-VERSION
      x-policy: POL-PLV-REJECT
      x-events:
      - EVT-PLV-REJECTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlvRejectCommand'
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
  /api/v1/operations/plan-versions/{id}/actions/amend-minor:
    post:
      operationId: CMD-PLV-AMEND-MINOR
      summary: CMD-PLV-AMEND-MINOR
      x-aggregate: AGG-PLAN-VERSION
      x-policy: POL-PLV-AMEND-MINOR
      x-events:
      - EVT-PLV-MINOR-AMENDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - MAJOR_CHANGE_REQUIRES_VERSION
      - PLAN_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlvAmendMinorCommand'
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
  /api/v1/operations/plan-versions/{id}/actions/discard:
    post:
      operationId: CMD-PLV-DISCARD
      summary: CMD-PLV-DISCARD
      x-aggregate: AGG-PLAN-VERSION
      x-policy: POL-PLV-DISCARD
      x-events:
      - EVT-PLV-DISCARDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PLAN_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PlvDiscardCommand'
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
  /api/v1/operations/outcome-trackers/{id}/actions/record:
    post:
      operationId: CMD-OUT-RECORD
      summary: CMD-OUT-RECORD
      x-aggregate: AGG-OUTCOME-TRACKER
      x-policy: POL-OUT-RECORD
      x-events:
      - EVT-OUT-MEASURED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - MEASUREMENT_INVALID
      - OUTCOME_TRACKER_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/OutRecordCommand'
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
  /api/v1/operations/outcome-trackers/{id}/actions/correct:
    post:
      operationId: CMD-OUT-CORRECT
      summary: CMD-OUT-CORRECT
      x-aggregate: AGG-OUTCOME-TRACKER
      x-policy: POL-OUT-CORRECT
      x-events:
      - EVT-OUT-MEASUREMENT-CORRECTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - OUTCOME_TRACKER_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/OutCorrectCommand'
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
  /api/v1/operations/decision-requests/{request_id}:
    get:
      operationId: QRY-DRQ-GET
      summary: Request with options and pinned citations (withheld per policy)
      x-authorized: label rule; required-authority holders in scope
      x-requirement: REQ-DEC-001
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
  /api/v1/operations/decisions/{decision_id}:
    get:
      operationId: QRY-DEC-GET
      summary: Decision with authority snapshot, citations (pinned) and supersession
        chain
      x-authorized: label rule
      x-requirement: REQ-DEC-003
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: decision_id
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
  /api/v1/operations/decisions/{decision_id}/basis:
    get:
      operationId: QRY-DEC-BASIS
      summary: 'What was known at decision time: cited assessments (pinned versions)
        and their key claims resolved known_at = decision.recorded_at'
      x-authorized: label rule; Auditor
      x-requirement: REQ-DEC-003
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: decision_id
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
  /api/v1/operations/plans/{plan_id}:
    get:
      operationId: QRY-PLN-GET
      summary: Plan with current baseline, draft (if any), implemented decisions
      x-authorized: label rule
      x-requirement: REQ-OPS-001
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: plan_id
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
  /api/v1/operations/plans/{plan_id}/versions:
    get:
      operationId: QRY-PLV-LIST
      summary: Versions with states and times
      x-authorized: label rule
      x-requirement: REQ-OPS-003
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: plan_id
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
  /api/v1/operations/plans/{plan_id}/versions/{version}/diff:
    get:
      operationId: QRY-PLV-DIFF
      summary: Diff vs baseline with major/minor classification and task synchronization
        preview
      x-authorized: label rule
      x-requirement: REQ-OPS-004
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: plan_id
        in: path
        required: true
        schema:
          type: string
      - name: version
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
  /api/v1/operations/plans/{plan_id}/progress:
    get:
      operationId: QRY-PLN-PROGRESS
      summary: Tasks by activity and state, milestones, outcome progress vs targets
      x-authorized: label rule; visible tasks only
      x-requirement: REQ-OPS-013
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: plan_id
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
  /api/v1/operations/plans/{plan_id}/outcomes/{outcome_id}/measurements:
    get:
      operationId: QRY-OUT-SERIES
      summary: Measurement series as known_at
      x-authorized: label rule
      x-requirement: REQ-OPS-013
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: plan_id
        in: path
        required: true
        schema:
          type: string
      - name: outcome_id
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
    DrqCreateCommand:
      type: object
      properties:
        question:
          $ref: '#/components/schemas/LocalizedName'
        decision_type:
          type: string
        scope:
          $ref: '#/components/schemas/Urn'
        deadline:
          type: string
          format: date-time
        context_refs:
          type: array
          items:
            type: string
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - question
      - decision_type
      - scope
      - deadline
      - label
    DrqAddOptionCommand:
      type: object
      properties:
        text:
          $ref: '#/components/schemas/LocalizedName'
        expected_impact:
          $ref: '#/components/schemas/LocalizedName'
      additionalProperties: false
      required:
      - text
    DrqCiteCommand:
      type: object
      properties:
        citations:
          type: array
          items:
            $ref: '#/components/schemas/Citation'
      additionalProperties: false
      required:
      - citations
    DrqOpenCommand:
      type: object
      properties: {}
      additionalProperties: false
    DrqWithdrawCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    DecRecordCommand:
      type: object
      properties:
        request:
          $ref: '#/components/schemas/Urn'
        selected_option:
          type: string
        rationale:
          $ref: '#/components/schemas/LocalizedName'
        effective_from:
          type: string
          format: date-time
        citations:
          type: array
          items:
            $ref: '#/components/schemas/Citation'
        supersedes:
          $ref: '#/components/schemas/Urn'
        ad_hoc_reason:
          type: string
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - selected_option
      - rationale
      - effective_from
      - label
    DecAnnulCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PlnCreateCommand:
      type: object
      properties:
        title:
          $ref: '#/components/schemas/LocalizedName'
        owner:
          $ref: '#/components/schemas/Urn'
        org_scope:
          $ref: '#/components/schemas/Urn'
        implements:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/Urn'
        plan_kind:
          type: string
          enum:
          - OPERATIONS
          - CONTINGENCY
        triggered_by:
          $ref: '#/components/schemas/Urn'
        window:
          $ref: '#/components/schemas/Interval'
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - title
      - owner
      - org_scope
      - plan_kind
      - window
      - label
    PlnSuspendCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PlnResumeCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PlnCompleteCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
    PlnCloseCommand:
      type: object
      properties:
        after_action_notes:
          $ref: '#/components/schemas/LocalizedName'
      additionalProperties: false
    PlnCancelCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PlnReclassifyCommand:
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
    PlvDraftCommand:
      type: object
      properties:
        plan:
          $ref: '#/components/schemas/Urn'
        based_on:
          type: integer
      additionalProperties: false
      required:
      - plan
    PlvEditCommand:
      type: object
      properties:
        objectives:
          type: array
          items:
            $ref: '#/components/schemas/Objective'
        outcomes:
          type: array
          items:
            $ref: '#/components/schemas/PlanOutcome'
        constraints:
          type: array
          items:
            type: string
        assumptions:
          type: array
          items:
            type: string
        phases:
          type: array
          items:
            $ref: '#/components/schemas/Phase'
        activities:
          type: array
          items:
            $ref: '#/components/schemas/Activity'
        milestones:
          type: array
          items:
            $ref: '#/components/schemas/Milestone'
        dependencies:
          type: array
          items:
            $ref: '#/components/schemas/PlanDependency'
        resource_notes:
          type: array
          items:
            type: string
      additionalProperties: false
      required:
      - objectives
      - outcomes
      - phases
      - activities
    PlvSubmitCommand:
      type: object
      properties: {}
      additionalProperties: false
    PlvReturnCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PlvApproveCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
    PlvRejectCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PlvAmendMinorCommand:
      type: object
      properties:
        annotations:
          type: array
          items:
            type: string
      additionalProperties: false
      required:
      - annotations
    PlvDiscardCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    OutRecordCommand:
      type: object
      properties:
        value:
          type: number
        unit:
          type: string
        measured_at:
          type: string
          format: date-time
        source:
          type: string
          enum:
          - manual
          - task_result
          - observation
        source_ref:
          $ref: '#/components/schemas/Urn'
        note:
          type: string
      additionalProperties: false
      required:
      - value
      - unit
      - measured_at
      - source
    OutCorrectCommand:
      type: object
      properties:
        measurement_id:
          type: string
        value:
          type: number
        unit:
          type: string
        reason:
          type: string
      additionalProperties: false
      required:
      - measurement_id
      - value
      - unit
      - reason
    Citation:
      type: object
      required:
      - ref
      - version
      properties:
        ref:
          $ref: '#/components/schemas/Urn'
        version:
          type: integer
        kind:
          enum:
          - assessment
          - finding
          - evidence
          - claim
    Objective:
      type: object
      required:
      - id
      - statement
      properties:
        id:
          type: string
        statement:
          $ref: '#/components/schemas/LocalizedName'
    PlanOutcome:
      type: object
      required:
      - id
      - metric
      - unit
      - target
      - due
      properties:
        id:
          type: string
        metric:
          type: string
        unit:
          type: string
        target:
          type: number
        direction:
          enum:
          - increase
          - decrease
          - reach
        due:
          type: string
          format: date-time
        objective_ref:
          type: string
    Phase:
      type: object
      required:
      - id
      - name
      - window
      properties:
        id:
          type: string
        name:
          $ref: '#/components/schemas/LocalizedName'
        window:
          $ref: '#/components/schemas/Interval'
    Activity:
      type: object
      required:
      - id
      - phase_id
      - name
      - task_generating
      properties:
        id:
          type: string
        phase_id:
          type: string
        name:
          $ref: '#/components/schemas/LocalizedName'
        task_generating:
          type: boolean
        task_type:
          $ref: '#/components/schemas/Urn'
        org_scope:
          $ref: '#/components/schemas/Urn'
        window:
          $ref: '#/components/schemas/Interval'
        completion_criteria:
          type: array
          items:
            type: object
        resource_note:
          type: string
    Milestone:
      type: object
      required:
      - id
      - name
      - date
      properties:
        id:
          type: string
        name:
          $ref: '#/components/schemas/LocalizedName'
        date:
          type: string
          format: date-time
        activity_refs:
          type: array
          items:
            type: string
    PlanDependency:
      type: object
      required:
      - from
      - to
      properties:
        from:
          type: string
        to:
          type: string
        kind:
          enum:
          - finish_to_start
          - start_to_start
```
