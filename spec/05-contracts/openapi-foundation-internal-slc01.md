---
id: OPENAPI-BC01-INTERNAL
type: api-contract
title: Foundation Internal API — system commands (SLC-01)
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

# Foundation Internal API — system commands (SLC-01)

أوامر داخلية بهوية عبء عمل فقط.

_5 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/foundation/tenants/{id}/actions/complete-provisioning` | CMD-TEN-COMPLETE-PROVISIONING |
| POST | `/api/v1/foundation/tenants/{id}/actions/fail-provisioning` | CMD-TEN-FAIL-PROVISIONING |
| POST | `/api/v1/foundation/tenants/{id}/actions/complete-cell-migration` | CMD-TEN-COMPLETE-CELL-MIGRATION |
| POST | `/api/v1/foundation/tenants/{id}/actions/complete-decommission` | CMD-TEN-COMPLETE-DECOMMISSION |
| POST | `/api/v1/foundation/users/{id}/actions/record-first-sign-in` | CMD-USR-RECORD-FIRST-SIGN-IN |

```yaml
openapi: 3.1.0
info:
  title: Foundation Internal API (system commands)
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
  /api/v1/foundation/tenants/{id}/actions/complete-provisioning:
    post:
      operationId: CMD-TEN-COMPLETE-PROVISIONING
      summary: CMD-TEN-COMPLETE-PROVISIONING
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-COMPLETE-PROVISIONING
      x-events:
      - EVT-TEN-ACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TENANT_INVALID_STATE_TRANSITION
      - TENANT_PROVISIONING_INCOMPLETE
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
              $ref: '#/components/schemas/TenCompleteProvisioningCommand'
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
  /api/v1/foundation/tenants/{id}/actions/fail-provisioning:
    post:
      operationId: CMD-TEN-FAIL-PROVISIONING
      summary: CMD-TEN-FAIL-PROVISIONING
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-FAIL-PROVISIONING
      x-events:
      - EVT-TEN-PROVISIONING-FAILED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TENANT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/TenFailProvisioningCommand'
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
  /api/v1/foundation/tenants/{id}/actions/complete-cell-migration:
    post:
      operationId: CMD-TEN-COMPLETE-CELL-MIGRATION
      summary: CMD-TEN-COMPLETE-CELL-MIGRATION
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-COMPLETE-CELL-MIGRATION
      x-events:
      - EVT-TEN-MIGRATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - MIGRATION_NOT_RECONCILED
      - TENANT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/TenCompleteCellMigrationCommand'
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
  /api/v1/foundation/tenants/{id}/actions/complete-decommission:
    post:
      operationId: CMD-TEN-COMPLETE-DECOMMISSION
      summary: CMD-TEN-COMPLETE-DECOMMISSION
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-COMPLETE-DECOMMISSION
      x-events:
      - EVT-TEN-DECOMMISSIONED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TENANT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/TenCompleteDecommissionCommand'
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
  /api/v1/foundation/users/{id}/actions/record-first-sign-in:
    post:
      operationId: CMD-USR-RECORD-FIRST-SIGN-IN
      summary: CMD-USR-RECORD-FIRST-SIGN-IN
      x-aggregate: AGG-USER
      x-policy: POL-USR-RECORD-FIRST-SIGN-IN
      x-events:
      - EVT-USR-ACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - USER_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/UsrRecordFirstSignInCommand'
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
    TenCompleteProvisioningCommand:
      type: object
      properties:
        steps:
          type: array
          items:
            type: string
      additionalProperties: false
      required:
      - steps
    TenFailProvisioningCommand:
      type: object
      properties:
        failed_step:
          type: string
        reason:
          type: string
      additionalProperties: false
      required:
      - failed_step
      - reason
    TenCompleteCellMigrationCommand:
      type: object
      properties:
        reconciliation_report:
          type: string
      additionalProperties: false
      required:
      - reconciliation_report
    TenCompleteDecommissionCommand:
      type: object
      properties: {}
      additionalProperties: false
    UsrRecordFirstSignInCommand:
      type: object
      properties:
        issuer:
          type: string
        subject:
          type: string
      additionalProperties: false
      required:
      - issuer
      - subject
```
