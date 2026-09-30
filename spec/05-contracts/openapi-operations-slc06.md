---
id: OPENAPI-BC04-SLC06
type: api-contract
title: Operations API (BC04) — SLC-06
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

# Operations API (BC04) — SLC-06

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_7 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/operations/subscriptions` | CMD-SUB-SUBSCRIBE |
| POST | `/api/v1/operations/subscriptions/{id}/actions/update-channels` | CMD-SUB-UPDATE-CHANNELS |
| POST | `/api/v1/operations/subscriptions/{id}/actions/pause` | CMD-SUB-PAUSE |
| POST | `/api/v1/operations/subscriptions/{id}/actions/resume` | CMD-SUB-RESUME |
| POST | `/api/v1/operations/subscriptions/{id}/actions/unsubscribe` | CMD-SUB-UNSUBSCRIBE |
| POST | `/api/v1/operations/notifications/{id}/actions/mark-read` | CMD-NTF-MARK-READ |
| GET | `/api/v1/operations/notifications` | QRY-NTF-INBOX |

```yaml
openapi: 3.1.0
info:
  title: Operations API (BC04) — SLC-06
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
  /api/v1/operations/subscriptions:
    post:
      operationId: CMD-SUB-SUBSCRIBE
      summary: CMD-SUB-SUBSCRIBE
      x-aggregate: AGG-SUBSCRIPTION
      x-policy: POL-SUB-SUBSCRIBE
      x-events:
      - EVT-SUB-SUBSCRIBED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SUBSCRIPTION_EXISTS
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
              $ref: '#/components/schemas/SubSubscribeCommand'
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
  /api/v1/operations/subscriptions/{id}/actions/update-channels:
    post:
      operationId: CMD-SUB-UPDATE-CHANNELS
      summary: CMD-SUB-UPDATE-CHANNELS
      x-aggregate: AGG-SUBSCRIPTION
      x-policy: POL-SUB-UPDATE-CHANNELS
      x-events:
      - EVT-SUB-CHANNELS-UPDATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SUBSCRIPTION_INVALID
      - SUBSCRIPTION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SubUpdateChannelsCommand'
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
  /api/v1/operations/subscriptions/{id}/actions/pause:
    post:
      operationId: CMD-SUB-PAUSE
      summary: CMD-SUB-PAUSE
      x-aggregate: AGG-SUBSCRIPTION
      x-policy: POL-SUB-PAUSE
      x-events:
      - EVT-SUB-PAUSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SUBSCRIPTION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SubPauseCommand'
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
  /api/v1/operations/subscriptions/{id}/actions/resume:
    post:
      operationId: CMD-SUB-RESUME
      summary: CMD-SUB-RESUME
      x-aggregate: AGG-SUBSCRIPTION
      x-policy: POL-SUB-RESUME
      x-events:
      - EVT-SUB-RESUMED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SUBSCRIPTION_INVALID_STATE_TRANSITION
      - TARGET_NOT_VISIBLE
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
              $ref: '#/components/schemas/SubResumeCommand'
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
  /api/v1/operations/subscriptions/{id}/actions/unsubscribe:
    post:
      operationId: CMD-SUB-UNSUBSCRIBE
      summary: CMD-SUB-UNSUBSCRIBE
      x-aggregate: AGG-SUBSCRIPTION
      x-policy: POL-SUB-UNSUBSCRIBE
      x-events:
      - EVT-SUB-ENDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SUBSCRIPTION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SubUnsubscribeCommand'
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
  /api/v1/operations/notifications/{id}/actions/mark-read:
    post:
      operationId: CMD-NTF-MARK-READ
      summary: CMD-NTF-MARK-READ
      x-aggregate: AGG-NOTIFICATION
      x-policy: POL-NTF-MARK-READ
      x-events:
      - EVT-NTF-READ
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - NOTIFICATION_INVALID_STATE_TRANSITION
      - NOT_RECIPIENT
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
              $ref: '#/components/schemas/NtfMarkReadCommand'
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
  /api/v1/operations/notifications:
    get:
      operationId: QRY-NTF-INBOX
      summary: My notifications (references + templates)
      x-authorized: recipient
      x-requirement: REQ-COM-001
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
    SubSubscribeCommand:
      type: object
      properties:
        target:
          $ref: '#/components/schemas/Urn'
        channels:
          type: array
          items:
            type: string
        quiet_hours:
          type: object
      additionalProperties: false
      required:
      - target
      - channels
    SubUpdateChannelsCommand:
      type: object
      properties:
        channels:
          type: array
          items:
            type: string
        quiet_hours:
          type: object
      additionalProperties: false
      required:
      - channels
    SubPauseCommand:
      type: object
      properties: {}
      additionalProperties: false
    SubResumeCommand:
      type: object
      properties: {}
      additionalProperties: false
    SubUnsubscribeCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
    NtfMarkReadCommand:
      type: object
      properties: {}
      additionalProperties: false
```
