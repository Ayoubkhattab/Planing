---
id: OPENAPI-BC07-SLC05
type: api-contract
title: Discovery API (BC07) — SLC-05
wave: W6
slice: SLC-05
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

# Discovery API (BC07) — SLC-05

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_10 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/discovery/projection-versions` | CMD-PRJ-CREATE-VERSION |
| GET | `/api/v1/discovery/projection-versions` | QRY-PRJ-STATUS |
| POST | `/api/v1/discovery/projection-versions/{id}/actions/promote` | CMD-PRJ-PROMOTE |
| POST | `/api/v1/discovery/projection-versions/{id}/actions/retire` | CMD-PRJ-RETIRE |
| POST | `/api/v1/discovery/projection-versions/{id}/actions/cancel-build` | CMD-PRJ-CANCEL-BUILD |
| POST | `/api/v1/discovery/search-queries` | QRY-SRCH-QUERY |
| GET | `/api/v1/discovery/suggestions` | QRY-SRCH-SUGGEST |
| GET | `/api/v1/discovery/graph/entities/{entity_id}/neighborhood` | QRY-GRAPH-NEIGHBORHOOD |
| POST | `/api/v1/discovery/graph/paths` | QRY-GRAPH-PATHS |
| POST | `/api/v1/{context}/label-checks` | QRY-LABEL-CHECK |

```yaml
openapi: 3.1.0
info:
  title: Discovery API (BC07) — SLC-05
  version: 1.0.0
  description: Generated from SLC-05 domain specification. Do not edit by hand.
servers:
- url: https://{cell}.platform.local
  variables:
    cell:
      default: cell-1
security:
- bearer: []
paths:
  /api/v1/discovery/projection-versions:
    post:
      operationId: CMD-PRJ-CREATE-VERSION
      summary: CMD-PRJ-CREATE-VERSION
      x-aggregate: AGG-PROJECTION-VERSION
      x-policy: POL-PRJ-CREATE-VERSION
      x-events:
      - EVT-PRJ-BUILD-STARTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PROJECTION_BUILD_IN_PROGRESS
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
              $ref: '#/components/schemas/PrjCreateVersionCommand'
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
      operationId: QRY-PRJ-STATUS
      summary: Projection versions, lag, state
      x-authorized: platform operator
      x-requirement: REQ-SRC-004
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
  /api/v1/discovery/projection-versions/{id}/actions/promote:
    post:
      operationId: CMD-PRJ-PROMOTE
      summary: CMD-PRJ-PROMOTE
      x-aggregate: AGG-PROJECTION-VERSION
      x-policy: POL-PRJ-PROMOTE
      x-events:
      - EVT-PRJ-PROMOTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PROJECTION_NOT_VERIFIED
      - PROJECTION_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PrjPromoteCommand'
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
  /api/v1/discovery/projection-versions/{id}/actions/retire:
    post:
      operationId: CMD-PRJ-RETIRE
      summary: CMD-PRJ-RETIRE
      x-aggregate: AGG-PROJECTION-VERSION
      x-policy: POL-PRJ-RETIRE
      x-events:
      - EVT-PRJ-RETIRED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - LAST_ACTIVE_PROJECTION
      - PROJECTION_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PrjRetireCommand'
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
  /api/v1/discovery/projection-versions/{id}/actions/cancel-build:
    post:
      operationId: CMD-PRJ-CANCEL-BUILD
      summary: CMD-PRJ-CANCEL-BUILD
      x-aggregate: AGG-PROJECTION-VERSION
      x-policy: POL-PRJ-CANCEL-BUILD
      x-events:
      - EVT-PRJ-FAILED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PROJECTION_VERSION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PrjCancelBuildCommand'
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
  /api/v1/discovery/search-queries:
    post:
      operationId: QRY-SRCH-QUERY
      summary: 'Unified search: text + types + polygon/bbox + time window + filters
        + facets; cursor paging; results and facets over visible facts only'
      x-authorized: any user; allowed_scope pre-filter + authoritative re-check
      x-requirement: REQ-SRC-001
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SearchResponse'
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
              $ref: '#/components/schemas/SearchRequest'
  /api/v1/discovery/suggestions:
    get:
      operationId: QRY-SRCH-SUGGEST
      summary: Autocomplete from visible facts only
      x-authorized: any user; same filter
      x-requirement: REQ-SRC-003
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - $ref: '#/components/parameters/Cursor'
      - $ref: '#/components/parameters/Limit'
      - name: q
        in: query
        required: true
        schema:
          type: string
          minLength: 2
          maxLength: 100
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                type: object
                properties:
                  suggestions:
                    type: array
                    maxItems: 10
                    items:
                      type: string
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
  /api/v1/discovery/graph/entities/{entity_id}/neighborhood:
    get:
      operationId: QRY-GRAPH-NEIGHBORHOOD
      summary: Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges
        cut
      x-authorized: any user; per-node and per-edge authorization
      x-requirement: REQ-INF-027
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: entity_id
        in: path
        required: true
        schema:
          type: string
      - $ref: '#/components/parameters/Cursor'
      - $ref: '#/components/parameters/Limit'
      - name: depth
        in: query
        required: false
        schema:
          type: integer
          minimum: 1
          maximum: 3
          default: 1
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
                $ref: '#/components/schemas/GraphResponse'
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
  /api/v1/discovery/graph/paths:
    post:
      operationId: QRY-GRAPH-PATHS
      summary: Paths between two entities, ≤ 4 hops, only through visible nodes and
        edges
      x-authorized: any user; per-node and per-edge authorization
      x-requirement: REQ-INF-027
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PathResponse'
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
              $ref: '#/components/schemas/PathRequest'
  /api/v1/{context}/label-checks:
    post:
      operationId: QRY-LABEL-CHECK
      summary: LabelCheck OHS contract implemented by each owning context; discovery
        workload identity only
      parameters:
      - name: context
        in: path
        required: true
        schema:
          type: string
      - $ref: '#/components/parameters/X-Correlation-Id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LabelCheckRequest'
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LabelCheckResponse'
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
    PrjCreateVersionCommand:
      type: object
      properties:
        kind:
          type: string
          enum:
          - search
          - graph
          - vector
        tenant_group:
          type: string
        schema_version:
          type: integer
        normalization_version:
          type: integer
        reason:
          type: string
      additionalProperties: false
      required:
      - kind
      - tenant_group
      - schema_version
      - normalization_version
      - reason
    PrjPromoteCommand:
      type: object
      properties: {}
      additionalProperties: false
    PrjRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PrjCancelBuildCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    GeoFilter:
      type: object
      properties:
        bbox:
          type: array
          items:
            type: number
          minItems: 4
          maxItems: 4
        polygon:
          type: object
    SearchRequest:
      type: object
      required:
      - types
      additionalProperties: false
      properties:
        text:
          type: string
          maxLength: 500
        types:
          type: array
          minItems: 1
          items:
            enum:
            - entity
            - observation
            - realworld_event
            - document
            - assessment
            - plan
            - task
        geo:
          $ref: '#/components/schemas/GeoFilter'
        time:
          $ref: '#/components/schemas/Interval'
        valid_at:
          type: string
          format: date-time
        filters:
          type: array
          items:
            type: object
            required:
            - field
            - op
            - value
            properties:
              field:
                type: string
              op:
                enum:
                - eq
                - in
                - range
                - exists
              value: {}
        facets:
          type: array
          maxItems: 10
          items:
            type: string
        sort:
          enum:
          - relevance
          - time_desc
          - time_asc
          - distance
        cursor:
          type:
          - string
          - 'null'
        limit:
          type: integer
          minimum: 1
          maximum: 100
          default: 20
    SearchHit:
      type: object
      required:
      - urn
      - type
      - title
      properties:
        urn:
          $ref: '#/components/schemas/Urn'
        canonical_urn:
          $ref: '#/components/schemas/Urn'
        type:
          type: string
        title:
          type: string
        snippet:
          type: string
        location:
          type:
          - object
          - 'null'
        time:
          type:
          - object
          - 'null'
        score:
          type: number
    Facet:
      type: object
      required:
      - field
      - buckets
      properties:
        field:
          type: string
        buckets:
          type: array
          items:
            type: object
            required:
            - value
            - count
            properties:
              value:
                type: string
              count:
                type: integer
                minimum: 1
    SearchResponse:
      type: object
      required:
      - hits
      - facets
      - next_cursor
      - completeness
      properties:
        hits:
          type: array
          items:
            $ref: '#/components/schemas/SearchHit'
        facets:
          type: array
          items:
            $ref: '#/components/schemas/Facet'
        visible_total:
          type: string
        next_cursor:
          type:
          - string
          - 'null'
        completeness:
          enum:
          - complete
          - partial_service_unavailable
    GraphNode:
      type: object
      required:
      - urn
      - type
      - label_text
      properties:
        urn:
          $ref: '#/components/schemas/Urn'
        type:
          type: string
        label_text:
          type: string
        depth:
          type: integer
    GraphEdge:
      type: object
      required:
      - urn
      - type
      - source
      - target
      properties:
        urn:
          $ref: '#/components/schemas/Urn'
        type:
          type: string
        source:
          $ref: '#/components/schemas/Urn'
        target:
          $ref: '#/components/schemas/Urn'
        valid:
          $ref: '#/components/schemas/Interval'
    GraphResponse:
      type: object
      required:
      - nodes
      - edges
      - truncated
      properties:
        nodes:
          type: array
          items:
            $ref: '#/components/schemas/GraphNode'
        edges:
          type: array
          items:
            $ref: '#/components/schemas/GraphEdge'
        truncated:
          type: boolean
    PathRequest:
      type: object
      required:
      - from
      - to
      additionalProperties: false
      properties:
        from:
          $ref: '#/components/schemas/Urn'
        to:
          $ref: '#/components/schemas/Urn'
        max_hops:
          type: integer
          minimum: 1
          maximum: 4
          default: 3
        relationship_types:
          type: array
          items:
            type: string
        valid_at:
          type: string
          format: date-time
        known_at:
          type: string
          format: date-time
        max_paths:
          type: integer
          minimum: 1
          maximum: 20
          default: 5
    PathResponse:
      type: object
      required:
      - paths
      properties:
        paths:
          type: array
          items:
            type: object
            properties:
              nodes:
                type: array
                items:
                  $ref: '#/components/schemas/Urn'
              edges:
                type: array
                items:
                  $ref: '#/components/schemas/Urn'
    LabelCheckRequest:
      type: object
      required:
      - urns
      properties:
        urns:
          type: array
          maxItems: 100
          items:
            $ref: '#/components/schemas/Urn'
        subject_security_version:
          type: integer
    LabelCheckResponse:
      type: object
      required:
      - results
      properties:
        results:
          type: array
          items:
            type: object
            required:
            - urn
            - visible
            properties:
              urn:
                $ref: '#/components/schemas/Urn'
              visible:
                type: boolean
              security_version:
                type: integer
```
