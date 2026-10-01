---
id: OPENAPI-BC08-SLC01
type: api-contract
title: Governance API (BC08) — SLC-01
wave: W6
slice: SLC-01
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

# Governance API (BC08) — SLC-01

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_19 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/governance/classification-schemes` | CMD-CLS-DRAFT |
| POST | `/api/v1/governance/classification-schemes/{id}/actions/edit` | CMD-CLS-EDIT |
| POST | `/api/v1/governance/classification-schemes/{id}/actions/activate` | CMD-CLS-ACTIVATE |
| POST | `/api/v1/governance/classification-schemes/{id}/actions/discard` | CMD-CLS-DISCARD |
| POST | `/api/v1/governance/policy-sets` | CMD-POL-DRAFT |
| POST | `/api/v1/governance/policy-sets/{id}/actions/edit` | CMD-POL-EDIT |
| POST | `/api/v1/governance/policy-sets/{id}/actions/submit` | CMD-POL-SUBMIT |
| POST | `/api/v1/governance/policy-sets/{id}/actions/approve` | CMD-POL-APPROVE |
| POST | `/api/v1/governance/policy-sets/{id}/actions/reject` | CMD-POL-REJECT |
| POST | `/api/v1/governance/security-exceptions` | CMD-EXC-REQUEST |
| GET | `/api/v1/governance/security-exceptions` | QRY-EXC-LIST |
| POST | `/api/v1/governance/security-exceptions/{id}/actions/approve` | CMD-EXC-APPROVE |
| POST | `/api/v1/governance/security-exceptions/{id}/actions/reject` | CMD-EXC-REJECT |
| POST | `/api/v1/governance/security-exceptions/{id}/actions/revoke` | CMD-EXC-REVOKE |
| GET | `/api/v1/governance/classification-scheme` | QRY-CLS-ACTIVE |
| GET | `/api/v1/governance/policy-sets/{version_id}` | QRY-POL-GET |
| POST | `/api/v1/governance/policy-decisions` | QRY-PDP-DECIDE |
| GET | `/api/v1/governance/audit-records` | QRY-AUD-SEARCH |
| POST | `/api/v1/governance/audit-integrity-checks` | QRY-AUD-VERIFY |

```yaml
openapi: 3.1.0
info:
  title: Governance API (BC08) — SLC-01
  version: 1.0.0
  description: Generated from SLC-01 domain specification. Do not edit by hand.
servers:
- url: https://{cell}.platform.local
  variables:
    cell:
      default: cell-1
security:
- bearer: []
paths:
  /api/v1/governance/classification-schemes:
    post:
      operationId: CMD-CLS-DRAFT
      summary: CMD-CLS-DRAFT
      x-aggregate: AGG-CLASSIFICATION-SCHEME
      x-policy: POL-CLS-DRAFT
      x-events:
      - EVT-CLS-DRAFTED
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
              $ref: '#/components/schemas/ClsDraftCommand'
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
  /api/v1/governance/classification-schemes/{id}/actions/edit:
    post:
      operationId: CMD-CLS-EDIT
      summary: CMD-CLS-EDIT
      x-aggregate: AGG-CLASSIFICATION-SCHEME
      x-policy: POL-CLS-EDIT
      x-events:
      - EVT-CLS-EDITED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - SCHEME_INVALID
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
              $ref: '#/components/schemas/ClsEditCommand'
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
  /api/v1/governance/classification-schemes/{id}/actions/activate:
    post:
      operationId: CMD-CLS-ACTIVATE
      summary: CMD-CLS-ACTIVATE
      x-aggregate: AGG-CLASSIFICATION-SCHEME
      x-policy: POL-CLS-ACTIVATE
      x-events:
      - EVT-CLS-ACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION
      - IDEMPOTENCY_KEY_REUSED
      - SCHEME_INVALID
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
              $ref: '#/components/schemas/ClsActivateCommand'
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
  /api/v1/governance/classification-schemes/{id}/actions/discard:
    post:
      operationId: CMD-CLS-DISCARD
      summary: CMD-CLS-DISCARD
      x-aggregate: AGG-CLASSIFICATION-SCHEME
      x-policy: POL-CLS-DISCARD
      x-events:
      - EVT-CLS-DISCARDED
      x-error-codes:
      - AUTHZ_DENIED
      - CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/ClsDiscardCommand'
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
  /api/v1/governance/policy-sets:
    post:
      operationId: CMD-POL-DRAFT
      summary: CMD-POL-DRAFT
      x-aggregate: AGG-POLICY-SET
      x-policy: POL-POL-DRAFT
      x-events:
      - EVT-POL-DRAFTED
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
              $ref: '#/components/schemas/PolDraftCommand'
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
  /api/v1/governance/policy-sets/{id}/actions/edit:
    post:
      operationId: CMD-POL-EDIT
      summary: CMD-POL-EDIT
      x-aggregate: AGG-POLICY-SET
      x-policy: POL-POL-EDIT
      x-events:
      - EVT-POL-EDITED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - POLICY_INVALID
      - POLICY_SET_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PolEditCommand'
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
  /api/v1/governance/policy-sets/{id}/actions/submit:
    post:
      operationId: CMD-POL-SUBMIT
      summary: CMD-POL-SUBMIT
      x-aggregate: AGG-POLICY-SET
      x-policy: POL-POL-SUBMIT
      x-events:
      - EVT-POL-SUBMITTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - POLICY_SET_INVALID_STATE_TRANSITION
      - POLICY_TESTS_FAILED
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
              $ref: '#/components/schemas/PolSubmitCommand'
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
  /api/v1/governance/policy-sets/{id}/actions/approve:
    post:
      operationId: CMD-POL-APPROVE
      summary: CMD-POL-APPROVE
      x-aggregate: AGG-POLICY-SET
      x-policy: POL-POL-APPROVE
      x-events:
      - EVT-POL-APPROVED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - POLICY_SET_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PolApproveCommand'
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
  /api/v1/governance/policy-sets/{id}/actions/reject:
    post:
      operationId: CMD-POL-REJECT
      summary: CMD-POL-REJECT
      x-aggregate: AGG-POLICY-SET
      x-policy: POL-POL-REJECT
      x-events:
      - EVT-POL-REJECTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - POLICY_SET_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PolRejectCommand'
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
  /api/v1/governance/security-exceptions:
    post:
      operationId: CMD-EXC-REQUEST
      summary: CMD-EXC-REQUEST
      x-aggregate: AGG-SECURITY-EXCEPTION
      x-policy: POL-EXC-REQUEST
      x-events:
      - EVT-EXC-REQUESTED
      x-error-codes:
      - AUTHZ_DENIED
      - EXCEPTION_NOT_ALLOWED
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
              $ref: '#/components/schemas/ExcRequestCommand'
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
      operationId: QRY-EXC-LIST
      summary: Exceptions by state
      x-authorized: Security Officer, Auditor
      x-requirement: REQ-FND-017
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
  /api/v1/governance/security-exceptions/{id}/actions/approve:
    post:
      operationId: CMD-EXC-APPROVE
      summary: CMD-EXC-APPROVE
      x-aggregate: AGG-SECURITY-EXCEPTION
      x-policy: POL-EXC-APPROVE
      x-events:
      - EVT-EXC-ACTIVATED
      - EVT-EXC-FIRST-APPROVED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SECURITY_EXCEPTION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/ExcApproveCommand'
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
  /api/v1/governance/security-exceptions/{id}/actions/reject:
    post:
      operationId: CMD-EXC-REJECT
      summary: CMD-EXC-REJECT
      x-aggregate: AGG-SECURITY-EXCEPTION
      x-policy: POL-EXC-REJECT
      x-events:
      - EVT-EXC-REJECTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - SECURITY_EXCEPTION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/ExcRejectCommand'
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
  /api/v1/governance/security-exceptions/{id}/actions/revoke:
    post:
      operationId: CMD-EXC-REVOKE
      summary: CMD-EXC-REVOKE
      x-aggregate: AGG-SECURITY-EXCEPTION
      x-policy: POL-EXC-REVOKE
      x-events:
      - EVT-EXC-REVOKED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - SECURITY_EXCEPTION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/ExcRevokeCommand'
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
  /api/v1/governance/classification-scheme:
    get:
      operationId: QRY-CLS-ACTIVE
      summary: Active scheme (labels only)
      x-authorized: any user of tenant
      x-requirement: REQ-GOV-001
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
  /api/v1/governance/policy-sets/{version_id}:
    get:
      operationId: QRY-POL-GET
      summary: Policy set version with tables and tests
      x-authorized: Security Officer, Auditor
      x-requirement: REQ-GOV-009
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: version_id
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
  /api/v1/governance/policy-decisions:
    post:
      operationId: QRY-PDP-DECIDE
      summary: DecisionRequest → DecisionResponse (authorization-model §2)
      x-authorized: internal PEPs only (workload identity)
      x-requirement: REQ-FND-010
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DecisionResponse'
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
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DecisionRequest'
  /api/v1/governance/audit-records:
    get:
      operationId: QRY-AUD-SEARCH
      summary: Audit records by actor, resource, time, correlation id
      x-authorized: Auditor, Security Officer (itself audited)
      x-requirement: REQ-FND-015
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
  /api/v1/governance/audit-integrity-checks:
    post:
      operationId: QRY-AUD-VERIFY
      summary: Start integrity verification job; returns job ref
      x-authorized: Auditor
      x-requirement: REQ-FND-016
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      responses:
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
        '202':
          description: ok
          content:
            application/json:
              schema:
                type: object
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
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
    ClsDraftCommand:
      type: object
      properties:
        based_on:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
    ClsEditCommand:
      type: object
      properties:
        levels:
          type: array
          items:
            $ref: '#/components/schemas/Level'
        compartments:
          type: array
          items:
            type: string
        caveats:
          type: array
          items:
            $ref: '#/components/schemas/Caveat'
        audit_threshold:
          type: string
        default_level:
          type: string
      additionalProperties: false
      required:
      - levels
      - compartments
      - caveats
      - audit_threshold
      - default_level
    ClsActivateCommand:
      type: object
      properties:
        effective_from:
          type: string
          format: date-time
      additionalProperties: false
      required:
      - effective_from
    ClsDiscardCommand:
      type: object
      properties: {}
      additionalProperties: false
    PolDraftCommand:
      type: object
      properties:
        based_on:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
    PolEditCommand:
      type: object
      properties:
        decision_tables:
          type: array
          items:
            type: object
        tests:
          type: array
          items:
            type: object
      additionalProperties: false
      required:
      - decision_tables
      - tests
    PolSubmitCommand:
      type: object
      properties:
        effective_from:
          type: string
          format: date-time
      additionalProperties: false
      required:
      - effective_from
    PolApproveCommand:
      type: object
      properties: {}
      additionalProperties: false
    PolRejectCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ExcRequestCommand:
      type: object
      properties:
        policy_rule:
          type: string
        subject_scope:
          type: object
        justification:
          type: string
        starts_at:
          type: string
          format: date-time
        ends_at:
          type: string
          format: date-time
      additionalProperties: false
      required:
      - policy_rule
      - subject_scope
      - justification
      - starts_at
      - ends_at
    ExcApproveCommand:
      type: object
      properties:
        note:
          type: string
      additionalProperties: false
    ExcRejectCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ExcRevokeCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
```
