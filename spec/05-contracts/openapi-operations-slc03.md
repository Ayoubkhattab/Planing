---
id: OPENAPI-BC04-SLC03
type: api-contract
title: Operations API (BC04) — SLC-03
wave: W6
slice: SLC-03
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

# Operations API (BC04) — SLC-03

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_32 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/operations/tasks` | CMD-TASK-CREATE |
| GET | `/api/v1/operations/tasks` | QRY-TASK-LIST |
| POST | `/api/v1/operations/tasks/{id}/actions/edit` | CMD-TASK-EDIT |
| POST | `/api/v1/operations/tasks/{id}/actions/mark-ready` | CMD-TASK-MARK-READY |
| POST | `/api/v1/operations/tasks/{id}/actions/assign` | CMD-TASK-ASSIGN |
| POST | `/api/v1/operations/tasks/{id}/actions/reassign` | CMD-TASK-REASSIGN |
| POST | `/api/v1/operations/tasks/{id}/actions/accept` | CMD-TASK-ACCEPT |
| POST | `/api/v1/operations/tasks/{id}/actions/decline` | CMD-TASK-DECLINE |
| POST | `/api/v1/operations/tasks/{id}/actions/start` | CMD-TASK-START |
| POST | `/api/v1/operations/tasks/{id}/actions/block` | CMD-TASK-BLOCK |
| POST | `/api/v1/operations/tasks/{id}/actions/resume` | CMD-TASK-RESUME |
| POST | `/api/v1/operations/tasks/{id}/actions/add-result-item` | CMD-TASK-ADD-RESULT-ITEM |
| POST | `/api/v1/operations/tasks/{id}/actions/submit` | CMD-TASK-SUBMIT |
| POST | `/api/v1/operations/tasks/{id}/actions/start-review` | CMD-TASK-START-REVIEW |
| POST | `/api/v1/operations/tasks/{id}/actions/return` | CMD-TASK-RETURN |
| POST | `/api/v1/operations/tasks/{id}/actions/approve` | CMD-TASK-APPROVE |
| POST | `/api/v1/operations/tasks/{id}/actions/reject` | CMD-TASK-REJECT |
| POST | `/api/v1/operations/tasks/{id}/actions/complete` | CMD-TASK-COMPLETE |
| POST | `/api/v1/operations/tasks/{id}/actions/close` | CMD-TASK-CLOSE |
| POST | `/api/v1/operations/tasks/{id}/actions/cancel` | CMD-TASK-CANCEL |
| POST | `/api/v1/operations/tasks/{id}/actions/escalate` | CMD-TASK-ESCALATE |
| POST | `/api/v1/operations/tasks/{id}/actions/set-due` | CMD-TASK-SET-DUE |
| POST | `/api/v1/operations/tasks/{id}/actions/suspend` | CMD-TASK-SUSPEND |
| POST | `/api/v1/operations/tasks/{id}/actions/unsuspend` | CMD-TASK-UNSUSPEND |
| POST | `/api/v1/operations/tasks/{id}/actions/reclassify` | CMD-TASK-RECLASSIFY |
| POST | `/api/v1/operations/task-types` | CMD-TTY-DEFINE |
| POST | `/api/v1/operations/task-types/{id}/actions/edit` | CMD-TTY-EDIT |
| POST | `/api/v1/operations/task-types/{id}/actions/activate` | CMD-TTY-ACTIVATE |
| POST | `/api/v1/operations/task-types/{id}/actions/retire` | CMD-TTY-RETIRE |
| GET | `/api/v1/operations/tasks/{task_id}` | QRY-TASK-GET |
| GET | `/api/v1/operations/tasks/{task_id}/history` | QRY-TASK-HISTORY |
| GET | `/api/v1/operations/task-types/{task_type_id}` | QRY-TTY-GET |

```yaml
openapi: 3.1.0
info:
  title: Operations API (BC04) — SLC-03
  version: 1.0.0
  description: Generated from SLC-03 domain specification. Do not edit by hand.
servers:
- url: https://{cell}.platform.local
  variables:
    cell:
      default: cell-1
security:
- bearer: []
paths:
  /api/v1/operations/tasks:
    post:
      operationId: CMD-TASK-CREATE
      summary: CMD-TASK-CREATE
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-CREATE
      x-events:
      - EVT-TASK-CREATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TASK_INVALID
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskCreateCommand'
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
      operationId: QRY-TASK-LIST
      summary: Tasks by assignee (me), plan, state, due_before, unit
      x-authorized: allowed_scope pre-filter
      x-requirement: REQ-OPS-006
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
  /api/v1/operations/tasks/{id}/actions/edit:
    post:
      operationId: CMD-TASK-EDIT
      summary: CMD-TASK-EDIT
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-EDIT
      x-events:
      - EVT-TASK-EDITED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TASK_INVALID
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskEditCommand'
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
  /api/v1/operations/tasks/{id}/actions/mark-ready:
    post:
      operationId: CMD-TASK-MARK-READY
      summary: CMD-TASK-MARK-READY
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-MARK-READY
      x-events:
      - EVT-TASK-READIED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_NOT_READY
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskMarkReadyCommand'
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
  /api/v1/operations/tasks/{id}/actions/assign:
    post:
      operationId: CMD-TASK-ASSIGN
      summary: CMD-TASK-ASSIGN
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-ASSIGN
      x-events:
      - EVT-TASK-ASSIGNED
      x-error-codes:
      - ASSIGNEE_NOT_ELIGIBLE
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskAssignCommand'
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
  /api/v1/operations/tasks/{id}/actions/reassign:
    post:
      operationId: CMD-TASK-REASSIGN
      summary: CMD-TASK-REASSIGN
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-REASSIGN
      x-events:
      - EVT-TASK-REASSIGNED
      x-error-codes:
      - ASSIGNEE_NOT_ELIGIBLE
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskReassignCommand'
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
  /api/v1/operations/tasks/{id}/actions/accept:
    post:
      operationId: CMD-TASK-ACCEPT
      summary: CMD-TASK-ACCEPT
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-ACCEPT
      x-events:
      - EVT-TASK-ACCEPTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - NOT_ASSIGNEE
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskAcceptCommand'
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
  /api/v1/operations/tasks/{id}/actions/decline:
    post:
      operationId: CMD-TASK-DECLINE
      summary: CMD-TASK-DECLINE
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-DECLINE
      x-events:
      - EVT-TASK-DECLINED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskDeclineCommand'
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
  /api/v1/operations/tasks/{id}/actions/start:
    post:
      operationId: CMD-TASK-START
      summary: CMD-TASK-START
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-START
      x-events:
      - EVT-TASK-STARTED
      x-error-codes:
      - AUTHZ_DENIED
      - DEPENDENCIES_NOT_MET
      - IDEMPOTENCY_KEY_REUSED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskStartCommand'
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
  /api/v1/operations/tasks/{id}/actions/block:
    post:
      operationId: CMD-TASK-BLOCK
      summary: CMD-TASK-BLOCK
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-BLOCK
      x-events:
      - EVT-TASK-BLOCKED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskBlockCommand'
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
  /api/v1/operations/tasks/{id}/actions/resume:
    post:
      operationId: CMD-TASK-RESUME
      summary: CMD-TASK-RESUME
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-RESUME
      x-events:
      - EVT-TASK-RESUMED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskResumeCommand'
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
  /api/v1/operations/tasks/{id}/actions/add-result-item:
    post:
      operationId: CMD-TASK-ADD-RESULT-ITEM
      summary: CMD-TASK-ADD-RESULT-ITEM
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-ADD-RESULT-ITEM
      x-events:
      - EVT-TASK-RESULT-ITEM-ADDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - RESULT_ITEM_INVALID
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskAddResultItemCommand'
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
  /api/v1/operations/tasks/{id}/actions/submit:
    post:
      operationId: CMD-TASK-SUBMIT
      summary: CMD-TASK-SUBMIT
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-SUBMIT
      x-events:
      - EVT-TASK-SUBMITTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - RESULT_REQUIRED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskSubmitCommand'
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
  /api/v1/operations/tasks/{id}/actions/start-review:
    post:
      operationId: CMD-TASK-START-REVIEW
      summary: CMD-TASK-START-REVIEW
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-START-REVIEW
      x-events:
      - EVT-TASK-REVIEW-STARTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SEGREGATION_OF_DUTIES
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskStartReviewCommand'
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
  /api/v1/operations/tasks/{id}/actions/return:
    post:
      operationId: CMD-TASK-RETURN
      summary: CMD-TASK-RETURN
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-RETURN
      x-events:
      - EVT-TASK-RETURNED-FOR-REWORK
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskReturnCommand'
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
  /api/v1/operations/tasks/{id}/actions/approve:
    post:
      operationId: CMD-TASK-APPROVE
      summary: CMD-TASK-APPROVE
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-APPROVE
      x-events:
      - EVT-TASK-APPROVED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SEGREGATION_OF_DUTIES
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskApproveCommand'
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
  /api/v1/operations/tasks/{id}/actions/reject:
    post:
      operationId: CMD-TASK-REJECT
      summary: CMD-TASK-REJECT
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-REJECT
      x-events:
      - EVT-TASK-REJECTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskRejectCommand'
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
  /api/v1/operations/tasks/{id}/actions/complete:
    post:
      operationId: CMD-TASK-COMPLETE
      summary: CMD-TASK-COMPLETE
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-COMPLETE
      x-events:
      - EVT-TASK-COMPLETED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TASK_CRITERIA_NOT_MET
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskCompleteCommand'
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
  /api/v1/operations/tasks/{id}/actions/close:
    post:
      operationId: CMD-TASK-CLOSE
      summary: CMD-TASK-CLOSE
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-CLOSE
      x-events:
      - EVT-TASK-CLOSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - OPEN_FOLLOW_UPS
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskCloseCommand'
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
  /api/v1/operations/tasks/{id}/actions/cancel:
    post:
      operationId: CMD-TASK-CANCEL
      summary: CMD-TASK-CANCEL
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-CANCEL
      x-events:
      - EVT-TASK-CANCELLED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskCancelCommand'
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
  /api/v1/operations/tasks/{id}/actions/escalate:
    post:
      operationId: CMD-TASK-ESCALATE
      summary: CMD-TASK-ESCALATE
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-ESCALATE
      x-events:
      - EVT-TASK-ESCALATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskEscalateCommand'
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
  /api/v1/operations/tasks/{id}/actions/set-due:
    post:
      operationId: CMD-TASK-SET-DUE
      summary: CMD-TASK-SET-DUE
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-SET-DUE
      x-events:
      - EVT-TASK-DUE-CHANGED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskSetDueCommand'
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
  /api/v1/operations/tasks/{id}/actions/suspend:
    post:
      operationId: CMD-TASK-SUSPEND
      summary: CMD-TASK-SUSPEND
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-SUSPEND
      x-events:
      - EVT-TASK-SUSPENDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskSuspendCommand'
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
  /api/v1/operations/tasks/{id}/actions/unsuspend:
    post:
      operationId: CMD-TASK-UNSUSPEND
      summary: CMD-TASK-UNSUSPEND
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-UNSUSPEND
      x-events:
      - EVT-TASK-UNSUSPENDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - NOT_SUSPENDED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskUnsuspendCommand'
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
  /api/v1/operations/tasks/{id}/actions/reclassify:
    post:
      operationId: CMD-TASK-RECLASSIFY
      summary: CMD-TASK-RECLASSIFY
      x-aggregate: AGG-TASK
      x-policy: POL-TASK-RECLASSIFY
      x-events:
      - EVT-TASK-RECLASSIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_CHANGE_NOT_AUTHORIZED
      - IDEMPOTENCY_KEY_REUSED
      - TASK_INVALID_STATE_TRANSITION
      - TASK_SUSPENDED
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
              $ref: '#/components/schemas/TaskReclassifyCommand'
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
  /api/v1/operations/task-types:
    post:
      operationId: CMD-TTY-DEFINE
      summary: CMD-TTY-DEFINE
      x-aggregate: AGG-TASK-TYPE
      x-policy: POL-TTY-DEFINE
      x-events:
      - EVT-TTY-DEFINED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TASK_TYPE_CODE_TAKEN
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
              $ref: '#/components/schemas/TtyDefineCommand'
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
  /api/v1/operations/task-types/{id}/actions/edit:
    post:
      operationId: CMD-TTY-EDIT
      summary: CMD-TTY-EDIT
      x-aggregate: AGG-TASK-TYPE
      x-policy: POL-TTY-EDIT
      x-events:
      - EVT-TTY-EDITED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TASK_TYPE_INVALID
      - TASK_TYPE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/TtyEditCommand'
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
  /api/v1/operations/task-types/{id}/actions/activate:
    post:
      operationId: CMD-TTY-ACTIVATE
      summary: CMD-TTY-ACTIVATE
      x-aggregate: AGG-TASK-TYPE
      x-policy: POL-TTY-ACTIVATE
      x-events:
      - EVT-TTY-ACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TASK_TYPE_INVALID
      - TASK_TYPE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/TtyActivateCommand'
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
  /api/v1/operations/task-types/{id}/actions/retire:
    post:
      operationId: CMD-TTY-RETIRE
      summary: CMD-TTY-RETIRE
      x-aggregate: AGG-TASK-TYPE
      x-policy: POL-TTY-RETIRE
      x-events:
      - EVT-TTY-RETIRED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - TASK_TYPE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/TtyRetireCommand'
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
  /api/v1/operations/tasks/{task_id}:
    get:
      operationId: QRY-TASK-GET
      summary: Task with criteria status, result, eligibility snapshot, dependencies
      x-authorized: assignee, reviewer, Planner/Manager in scope; label rule
      x-requirement: REQ-OPS-006
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: task_id
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
  /api/v1/operations/tasks/{task_id}/history:
    get:
      operationId: QRY-TASK-HISTORY
      summary: State history; state as of t (RECONSTRUCTED)
      x-authorized: same as QRY-TASK-GET
      x-requirement: REQ-OPS-006
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: task_id
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
  /api/v1/operations/task-types/{task_type_id}:
    get:
      operationId: QRY-TTY-GET
      summary: Task type version
      x-authorized: any user of tenant
      x-requirement: REQ-OPS-014
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: task_type_id
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
    TaskCreateCommand:
      type: object
      properties:
        task_type:
          $ref: '#/components/schemas/Urn'
        title:
          $ref: '#/components/schemas/LocalizedName'
        description:
          $ref: '#/components/schemas/LocalizedName'
        plan_ref:
          $ref: '#/components/schemas/Urn'
        incident_ref:
          $ref: '#/components/schemas/Urn'
        ad_hoc_reason:
          type: string
        owner:
          $ref: '#/components/schemas/Urn'
        org_scope:
          $ref: '#/components/schemas/Urn'
        due_at:
          type: string
          format: date-time
        dependencies:
          type: array
          items:
            type: string
        follow_up_of:
          $ref: '#/components/schemas/Urn'
        label:
          $ref: '#/components/schemas/Label'
      additionalProperties: false
      required:
      - task_type
      - title
      - owner
      - org_scope
      - label
    TaskEditCommand:
      type: object
      properties:
        title:
          $ref: '#/components/schemas/LocalizedName'
        description:
          $ref: '#/components/schemas/LocalizedName'
        criteria:
          type: array
          items:
            type: string
        dependencies:
          type: array
          items:
            type: string
      additionalProperties: false
    TaskMarkReadyCommand:
      type: object
      properties: {}
      additionalProperties: false
    TaskAssignCommand:
      type: object
      properties:
        assignee:
          $ref: '#/components/schemas/Urn'
        note:
          type: string
      additionalProperties: false
      required:
      - assignee
    TaskReassignCommand:
      type: object
      properties:
        assignee:
          $ref: '#/components/schemas/Urn'
        reason:
          type: string
      additionalProperties: false
      required:
      - assignee
      - reason
    TaskAcceptCommand:
      type: object
      properties: {}
      additionalProperties: false
    TaskDeclineCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TaskStartCommand:
      type: object
      properties: {}
      additionalProperties: false
    TaskBlockCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TaskResumeCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
      required:
      - note
    TaskAddResultItemCommand:
      type: object
      properties:
        kind:
          type: string
          enum:
          - note
          - evidence
          - observation
          - measurement
        ref:
          $ref: '#/components/schemas/Urn'
        note:
          $ref: '#/components/schemas/LocalizedName'
        measurement:
          type: object
      additionalProperties: false
      required:
      - kind
    TaskSubmitCommand:
      type: object
      properties:
        summary:
          $ref: '#/components/schemas/LocalizedName'
      additionalProperties: false
      required:
      - summary
    TaskStartReviewCommand:
      type: object
      properties: {}
      additionalProperties: false
    TaskReturnCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TaskApproveCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
    TaskRejectCommand:
      type: object
      properties:
        reason:
          type: string
        create_follow_up:
          type: boolean
      additionalProperties: false
      required:
      - reason
      - create_follow_up
    TaskCompleteCommand:
      type: object
      properties:
        attestations:
          type: array
          items:
            type: string
      additionalProperties: false
      required:
      - attestations
    TaskCloseCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
    TaskCancelCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TaskEscalateCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TaskSetDueCommand:
      type: object
      properties:
        due_at:
          type: string
          format: date-time
        reason:
          type: string
      additionalProperties: false
      required:
      - due_at
      - reason
    TaskSuspendCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TaskUnsuspendCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TaskReclassifyCommand:
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
    TtyDefineCommand:
      type: object
      properties:
        code:
          type: string
        name:
          $ref: '#/components/schemas/LocalizedName'
      additionalProperties: false
      required:
      - code
      - name
    TtyEditCommand:
      type: object
      properties:
        qualification_requirements:
          type: array
          items:
            type: string
        criteria_templates:
          type: array
          items:
            type: string
        escalation:
          type: object
        expires_on_due:
          type: boolean
        review_steps:
          type: integer
      additionalProperties: false
      required:
      - qualification_requirements
      - criteria_templates
      - escalation
      - expires_on_due
    TtyActivateCommand:
      type: object
      properties: {}
      additionalProperties: false
    TtyRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
```
