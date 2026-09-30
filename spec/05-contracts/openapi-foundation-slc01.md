---
id: OPENAPI-BC01-SLC01
type: api-contract
title: Foundation API (BC01) — SLC-01
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

# Foundation API (BC01) — SLC-01

المسارات `/api/v1/{context}/{resource}`؛ الأوامر `POST …/actions/{action}` مع `Idempotency-Key` و`If-Match`؛ الاستعلامات تقبل `valid_at` و`known_at` حيث تنطبق؛ القوائم بمؤشر؛ الأخطاء بنموذج ApiError.

_61 operations · validated with openapi-spec-validator_

| Method | Path | Operation |
|---|---|---|
| POST | `/api/v1/foundation/tenants` | CMD-TEN-PROVISION |
| POST | `/api/v1/foundation/tenants/{id}/actions/retry-provisioning` | CMD-TEN-RETRY-PROVISIONING |
| POST | `/api/v1/foundation/tenants/{id}/actions/suspend` | CMD-TEN-SUSPEND |
| POST | `/api/v1/foundation/tenants/{id}/actions/reactivate` | CMD-TEN-REACTIVATE |
| POST | `/api/v1/foundation/tenants/{id}/actions/start-cell-migration` | CMD-TEN-START-CELL-MIGRATION |
| POST | `/api/v1/foundation/tenants/{id}/actions/start-decommission` | CMD-TEN-START-DECOMMISSION |
| POST | `/api/v1/foundation/tenants/{id}/actions/update-quotas` | CMD-TEN-UPDATE-QUOTAS |
| POST | `/api/v1/foundation/organizations` | CMD-ORG-CREATE |
| POST | `/api/v1/foundation/organizations/{id}/actions/rename` | CMD-ORG-RENAME |
| POST | `/api/v1/foundation/organizations/{id}/actions/add-unit` | CMD-ORG-ADD-UNIT |
| POST | `/api/v1/foundation/organizations/{id}/actions/rename-unit` | CMD-ORG-RENAME-UNIT |
| POST | `/api/v1/foundation/organizations/{id}/actions/move-unit` | CMD-ORG-MOVE-UNIT |
| POST | `/api/v1/foundation/organizations/{id}/actions/deactivate-unit` | CMD-ORG-DEACTIVATE-UNIT |
| POST | `/api/v1/foundation/organizations/{id}/actions/deactivate` | CMD-ORG-DEACTIVATE |
| POST | `/api/v1/foundation/organizations/{id}/actions/reactivate` | CMD-ORG-REACTIVATE |
| POST | `/api/v1/foundation/persons` | CMD-PER-REGISTER |
| POST | `/api/v1/foundation/persons/{id}/actions/update-details` | CMD-PER-UPDATE-DETAILS |
| POST | `/api/v1/foundation/persons/{id}/actions/deactivate` | CMD-PER-DEACTIVATE |
| POST | `/api/v1/foundation/persons/{id}/actions/reactivate` | CMD-PER-REACTIVATE |
| POST | `/api/v1/foundation/persons/{id}/actions/erase` | CMD-PER-ERASE |
| POST | `/api/v1/foundation/users` | CMD-USR-PROVISION |
| GET | `/api/v1/foundation/users` | QRY-USR-LIST |
| POST | `/api/v1/foundation/users/{id}/actions/link-identity` | CMD-USR-LINK-IDENTITY |
| POST | `/api/v1/foundation/users/{id}/actions/unlink-identity` | CMD-USR-UNLINK-IDENTITY |
| POST | `/api/v1/foundation/users/{id}/actions/link-person` | CMD-USR-LINK-PERSON |
| POST | `/api/v1/foundation/users/{id}/actions/lock` | CMD-USR-LOCK |
| POST | `/api/v1/foundation/users/{id}/actions/unlock` | CMD-USR-UNLOCK |
| POST | `/api/v1/foundation/users/{id}/actions/disable` | CMD-USR-DISABLE |
| POST | `/api/v1/foundation/users/{id}/actions/enable` | CMD-USR-ENABLE |
| POST | `/api/v1/foundation/users/{id}/actions/close` | CMD-USR-CLOSE |
| POST | `/api/v1/foundation/service-accounts` | CMD-SVC-CREATE |
| POST | `/api/v1/foundation/service-accounts/{id}/actions/rotate-credential` | CMD-SVC-ROTATE-CREDENTIAL |
| POST | `/api/v1/foundation/service-accounts/{id}/actions/disable` | CMD-SVC-DISABLE |
| POST | `/api/v1/foundation/service-accounts/{id}/actions/enable` | CMD-SVC-ENABLE |
| POST | `/api/v1/foundation/service-accounts/{id}/actions/close` | CMD-SVC-CLOSE |
| POST | `/api/v1/foundation/roles` | CMD-ROL-DEFINE |
| POST | `/api/v1/foundation/roles/{id}/actions/set-permissions` | CMD-ROL-SET-PERMISSIONS |
| POST | `/api/v1/foundation/roles/{id}/actions/activate` | CMD-ROL-ACTIVATE |
| POST | `/api/v1/foundation/roles/{id}/actions/retire` | CMD-ROL-RETIRE |
| POST | `/api/v1/foundation/role-assignments` | CMD-RAS-ASSIGN |
| POST | `/api/v1/foundation/role-assignments/{id}/actions/revoke` | CMD-RAS-REVOKE |
| POST | `/api/v1/foundation/authority-grants` | CMD-AUT-GRANT |
| GET | `/api/v1/foundation/authority-grants` | QRY-AUT-LIST |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/approve-grant` | CMD-AUT-APPROVE-GRANT |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/reject-grant` | CMD-AUT-REJECT-GRANT |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/delegate` | CMD-AUT-DELEGATE |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/suspend` | CMD-AUT-SUSPEND |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/resume` | CMD-AUT-RESUME |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/revoke` | CMD-AUT-REVOKE |
| POST | `/api/v1/foundation/clearances` | CMD-CLR-GRANT |
| POST | `/api/v1/foundation/clearances/{id}/actions/approve` | CMD-CLR-APPROVE |
| POST | `/api/v1/foundation/clearances/{id}/actions/modify` | CMD-CLR-MODIFY |
| POST | `/api/v1/foundation/clearances/{id}/actions/suspend` | CMD-CLR-SUSPEND |
| POST | `/api/v1/foundation/clearances/{id}/actions/reinstate` | CMD-CLR-REINSTATE |
| POST | `/api/v1/foundation/clearances/{id}/actions/revoke` | CMD-CLR-REVOKE |
| GET | `/api/v1/foundation/tenants/{tenant_id}` | QRY-TEN-GET |
| GET | `/api/v1/foundation/organizations/{org_id}/units` | QRY-ORG-TREE |
| GET | `/api/v1/foundation/users/{user_id}` | QRY-USR-GET |
| GET | `/api/v1/foundation/me/security-context` | QRY-SEC-CONTEXT |
| POST | `/api/v1/foundation/authority-checks` | QRY-AUT-CHECK |
| GET | `/api/v1/foundation/users/{user_id}/clearance` | QRY-CLR-GET |

```yaml
openapi: 3.1.0
info:
  title: Foundation API (BC01) — SLC-01
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
  /api/v1/foundation/tenants:
    post:
      operationId: CMD-TEN-PROVISION
      summary: CMD-TEN-PROVISION
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-PROVISION
      x-events:
      - EVT-TEN-PROVISIONING-STARTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TENANT_NAMESPACE_TAKEN
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
              $ref: '#/components/schemas/TenProvisionCommand'
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
  /api/v1/foundation/tenants/{id}/actions/retry-provisioning:
    post:
      operationId: CMD-TEN-RETRY-PROVISIONING
      summary: CMD-TEN-RETRY-PROVISIONING
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-RETRY-PROVISIONING
      x-events:
      - EVT-TEN-PROVISIONING-STARTED
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
              $ref: '#/components/schemas/TenRetryProvisioningCommand'
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
  /api/v1/foundation/tenants/{id}/actions/suspend:
    post:
      operationId: CMD-TEN-SUSPEND
      summary: CMD-TEN-SUSPEND
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-SUSPEND
      x-events:
      - EVT-TEN-SUSPENDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
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
              $ref: '#/components/schemas/TenSuspendCommand'
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
  /api/v1/foundation/tenants/{id}/actions/reactivate:
    post:
      operationId: CMD-TEN-REACTIVATE
      summary: CMD-TEN-REACTIVATE
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-REACTIVATE
      x-events:
      - EVT-TEN-REACTIVATED
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
              $ref: '#/components/schemas/TenReactivateCommand'
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
  /api/v1/foundation/tenants/{id}/actions/start-cell-migration:
    post:
      operationId: CMD-TEN-START-CELL-MIGRATION
      summary: CMD-TEN-START-CELL-MIGRATION
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-START-CELL-MIGRATION
      x-events:
      - EVT-TEN-MIGRATION-STARTED
      x-error-codes:
      - AUTHZ_DENIED
      - CELL_UNAVAILABLE
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
              $ref: '#/components/schemas/TenStartCellMigrationCommand'
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
  /api/v1/foundation/tenants/{id}/actions/start-decommission:
    post:
      operationId: CMD-TEN-START-DECOMMISSION
      summary: CMD-TEN-START-DECOMMISSION
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-START-DECOMMISSION
      x-events:
      - EVT-TEN-DECOMMISSION-STARTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - LEGAL_HOLD_ACTIVE
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
              $ref: '#/components/schemas/TenStartDecommissionCommand'
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
  /api/v1/foundation/tenants/{id}/actions/update-quotas:
    post:
      operationId: CMD-TEN-UPDATE-QUOTAS
      summary: CMD-TEN-UPDATE-QUOTAS
      x-aggregate: AGG-TENANT
      x-policy: POL-TEN-UPDATE-QUOTAS
      x-events:
      - EVT-TEN-QUOTAS-UPDATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - QUOTA_EXCEEDS_CAPACITY
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
              $ref: '#/components/schemas/TenUpdateQuotasCommand'
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
  /api/v1/foundation/organizations:
    post:
      operationId: CMD-ORG-CREATE
      summary: CMD-ORG-CREATE
      x-aggregate: AGG-ORGANIZATION
      x-policy: POL-ORG-CREATE
      x-events:
      - EVT-ORG-CREATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ORG_NAME_TAKEN
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
              $ref: '#/components/schemas/OrgCreateCommand'
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
  /api/v1/foundation/organizations/{id}/actions/rename:
    post:
      operationId: CMD-ORG-RENAME
      summary: CMD-ORG-RENAME
      x-aggregate: AGG-ORGANIZATION
      x-policy: POL-ORG-RENAME
      x-events:
      - EVT-ORG-RENAMED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ORGANIZATION_INVALID_STATE_TRANSITION
      - ORG_NAME_TAKEN
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
              $ref: '#/components/schemas/OrgRenameCommand'
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
  /api/v1/foundation/organizations/{id}/actions/add-unit:
    post:
      operationId: CMD-ORG-ADD-UNIT
      summary: CMD-ORG-ADD-UNIT
      x-aggregate: AGG-ORGANIZATION
      x-policy: POL-ORG-ADD-UNIT
      x-events:
      - EVT-ORG-UNIT-ADDED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ORGANIZATION_INVALID_STATE_TRANSITION
      - ORG_UNIT_INVALID_PARENT
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
              $ref: '#/components/schemas/OrgAddUnitCommand'
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
  /api/v1/foundation/organizations/{id}/actions/rename-unit:
    post:
      operationId: CMD-ORG-RENAME-UNIT
      summary: CMD-ORG-RENAME-UNIT
      x-aggregate: AGG-ORGANIZATION
      x-policy: POL-ORG-RENAME-UNIT
      x-events:
      - EVT-ORG-UNIT-RENAMED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ORGANIZATION_INVALID_STATE_TRANSITION
      - ORG_UNIT_NAME_TAKEN
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
              $ref: '#/components/schemas/OrgRenameUnitCommand'
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
  /api/v1/foundation/organizations/{id}/actions/move-unit:
    post:
      operationId: CMD-ORG-MOVE-UNIT
      summary: CMD-ORG-MOVE-UNIT
      x-aggregate: AGG-ORGANIZATION
      x-policy: POL-ORG-MOVE-UNIT
      x-events:
      - EVT-ORG-UNIT-MOVED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ORGANIZATION_INVALID_STATE_TRANSITION
      - ORG_UNIT_CYCLE
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
              $ref: '#/components/schemas/OrgMoveUnitCommand'
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
  /api/v1/foundation/organizations/{id}/actions/deactivate-unit:
    post:
      operationId: CMD-ORG-DEACTIVATE-UNIT
      summary: CMD-ORG-DEACTIVATE-UNIT
      x-aggregate: AGG-ORGANIZATION
      x-policy: POL-ORG-DEACTIVATE-UNIT
      x-events:
      - EVT-ORG-UNIT-DEACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ORGANIZATION_INVALID_STATE_TRANSITION
      - ORG_UNIT_IN_USE
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
              $ref: '#/components/schemas/OrgDeactivateUnitCommand'
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
  /api/v1/foundation/organizations/{id}/actions/deactivate:
    post:
      operationId: CMD-ORG-DEACTIVATE
      summary: CMD-ORG-DEACTIVATE
      x-aggregate: AGG-ORGANIZATION
      x-policy: POL-ORG-DEACTIVATE
      x-events:
      - EVT-ORG-DEACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ORGANIZATION_INVALID_STATE_TRANSITION
      - ORG_IN_USE
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
              $ref: '#/components/schemas/OrgDeactivateCommand'
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
  /api/v1/foundation/organizations/{id}/actions/reactivate:
    post:
      operationId: CMD-ORG-REACTIVATE
      summary: CMD-ORG-REACTIVATE
      x-aggregate: AGG-ORGANIZATION
      x-policy: POL-ORG-REACTIVATE
      x-events:
      - EVT-ORG-REACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ORGANIZATION_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/OrgReactivateCommand'
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
  /api/v1/foundation/persons:
    post:
      operationId: CMD-PER-REGISTER
      summary: CMD-PER-REGISTER
      x-aggregate: AGG-PERSON
      x-policy: POL-PER-REGISTER
      x-events:
      - EVT-PER-REGISTERED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PERSON_DUPLICATE
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
              $ref: '#/components/schemas/PerRegisterCommand'
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
  /api/v1/foundation/persons/{id}/actions/update-details:
    post:
      operationId: CMD-PER-UPDATE-DETAILS
      summary: CMD-PER-UPDATE-DETAILS
      x-aggregate: AGG-PERSON
      x-policy: POL-PER-UPDATE-DETAILS
      x-events:
      - EVT-PER-DETAILS-UPDATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PERSON_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PerUpdateDetailsCommand'
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
  /api/v1/foundation/persons/{id}/actions/deactivate:
    post:
      operationId: CMD-PER-DEACTIVATE
      summary: CMD-PER-DEACTIVATE
      x-aggregate: AGG-PERSON
      x-policy: POL-PER-DEACTIVATE
      x-events:
      - EVT-PER-DEACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PERSON_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PerDeactivateCommand'
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
  /api/v1/foundation/persons/{id}/actions/reactivate:
    post:
      operationId: CMD-PER-REACTIVATE
      summary: CMD-PER-REACTIVATE
      x-aggregate: AGG-PERSON
      x-policy: POL-PER-REACTIVATE
      x-events:
      - EVT-PER-REACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PERSON_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PerReactivateCommand'
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
  /api/v1/foundation/persons/{id}/actions/erase:
    post:
      operationId: CMD-PER-ERASE
      summary: CMD-PER-ERASE
      x-aggregate: AGG-PERSON
      x-policy: POL-PER-ERASE
      x-events:
      - EVT-PER-ERASED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - LEGAL_HOLD_ACTIVE
      - PERSON_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/PerEraseCommand'
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
  /api/v1/foundation/users:
    post:
      operationId: CMD-USR-PROVISION
      summary: CMD-USR-PROVISION
      x-aggregate: AGG-USER
      x-policy: POL-USR-PROVISION
      x-events:
      - EVT-USR-PROVISIONED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - TENANT_NOT_ACTIVE
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
              $ref: '#/components/schemas/UsrProvisionCommand'
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
      operationId: QRY-USR-LIST
      summary: Users filtered by state, unit, role
      x-authorized: Administrator in scope
      x-requirement: REQ-FND-006
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
  /api/v1/foundation/users/{id}/actions/link-identity:
    post:
      operationId: CMD-USR-LINK-IDENTITY
      summary: CMD-USR-LINK-IDENTITY
      x-aggregate: AGG-USER
      x-policy: POL-USR-LINK-IDENTITY
      x-events:
      - EVT-USR-IDENTITY-LINKED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - IDENTITY_ALREADY_LINKED
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
              $ref: '#/components/schemas/UsrLinkIdentityCommand'
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
  /api/v1/foundation/users/{id}/actions/unlink-identity:
    post:
      operationId: CMD-USR-UNLINK-IDENTITY
      summary: CMD-USR-UNLINK-IDENTITY
      x-aggregate: AGG-USER
      x-policy: POL-USR-UNLINK-IDENTITY
      x-events:
      - EVT-USR-IDENTITY-UNLINKED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - LAST_IDENTITY
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
              $ref: '#/components/schemas/UsrUnlinkIdentityCommand'
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
  /api/v1/foundation/users/{id}/actions/link-person:
    post:
      operationId: CMD-USR-LINK-PERSON
      summary: CMD-USR-LINK-PERSON
      x-aggregate: AGG-USER
      x-policy: POL-USR-LINK-PERSON
      x-events:
      - EVT-USR-PERSON-LINKED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PERSON_ALREADY_LINKED
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
              $ref: '#/components/schemas/UsrLinkPersonCommand'
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
  /api/v1/foundation/users/{id}/actions/lock:
    post:
      operationId: CMD-USR-LOCK
      summary: CMD-USR-LOCK
      x-aggregate: AGG-USER
      x-policy: POL-USR-LOCK
      x-events:
      - EVT-USR-LOCKED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
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
              $ref: '#/components/schemas/UsrLockCommand'
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
  /api/v1/foundation/users/{id}/actions/unlock:
    post:
      operationId: CMD-USR-UNLOCK
      summary: CMD-USR-UNLOCK
      x-aggregate: AGG-USER
      x-policy: POL-USR-UNLOCK
      x-events:
      - EVT-USR-UNLOCKED
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
              $ref: '#/components/schemas/UsrUnlockCommand'
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
  /api/v1/foundation/users/{id}/actions/disable:
    post:
      operationId: CMD-USR-DISABLE
      summary: CMD-USR-DISABLE
      x-aggregate: AGG-USER
      x-policy: POL-USR-DISABLE
      x-events:
      - EVT-USR-DISABLED
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
              $ref: '#/components/schemas/UsrDisableCommand'
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
  /api/v1/foundation/users/{id}/actions/enable:
    post:
      operationId: CMD-USR-ENABLE
      summary: CMD-USR-ENABLE
      x-aggregate: AGG-USER
      x-policy: POL-USR-ENABLE
      x-events:
      - EVT-USR-ENABLED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - LAST_IDENTITY
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
              $ref: '#/components/schemas/UsrEnableCommand'
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
  /api/v1/foundation/users/{id}/actions/close:
    post:
      operationId: CMD-USR-CLOSE
      summary: CMD-USR-CLOSE
      x-aggregate: AGG-USER
      x-policy: POL-USR-CLOSE
      x-events:
      - EVT-USR-CLOSED
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
              $ref: '#/components/schemas/UsrCloseCommand'
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
  /api/v1/foundation/service-accounts:
    post:
      operationId: CMD-SVC-CREATE
      summary: CMD-SVC-CREATE
      x-aggregate: AGG-SERVICE-ACCOUNT
      x-policy: POL-SVC-CREATE
      x-events:
      - EVT-SVC-CREATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - OWNER_REQUIRED
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
              $ref: '#/components/schemas/SvcCreateCommand'
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
  /api/v1/foundation/service-accounts/{id}/actions/rotate-credential:
    post:
      operationId: CMD-SVC-ROTATE-CREDENTIAL
      summary: CMD-SVC-ROTATE-CREDENTIAL
      x-aggregate: AGG-SERVICE-ACCOUNT
      x-policy: POL-SVC-ROTATE-CREDENTIAL
      x-events:
      - EVT-SVC-CREDENTIAL-ROTATED
      x-error-codes:
      - AUTHZ_DENIED
      - CREDENTIAL_LIFETIME_EXCEEDED
      - IDEMPOTENCY_KEY_REUSED
      - SERVICE_ACCOUNT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SvcRotateCredentialCommand'
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
  /api/v1/foundation/service-accounts/{id}/actions/disable:
    post:
      operationId: CMD-SVC-DISABLE
      summary: CMD-SVC-DISABLE
      x-aggregate: AGG-SERVICE-ACCOUNT
      x-policy: POL-SVC-DISABLE
      x-events:
      - EVT-SVC-DISABLED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SERVICE_ACCOUNT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SvcDisableCommand'
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
  /api/v1/foundation/service-accounts/{id}/actions/enable:
    post:
      operationId: CMD-SVC-ENABLE
      summary: CMD-SVC-ENABLE
      x-aggregate: AGG-SERVICE-ACCOUNT
      x-policy: POL-SVC-ENABLE
      x-events:
      - EVT-SVC-ENABLED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - OWNER_REQUIRED
      - SERVICE_ACCOUNT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SvcEnableCommand'
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
  /api/v1/foundation/service-accounts/{id}/actions/close:
    post:
      operationId: CMD-SVC-CLOSE
      summary: CMD-SVC-CLOSE
      x-aggregate: AGG-SERVICE-ACCOUNT
      x-policy: POL-SVC-CLOSE
      x-events:
      - EVT-SVC-CLOSED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SERVICE_ACCOUNT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/SvcCloseCommand'
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
  /api/v1/foundation/roles:
    post:
      operationId: CMD-ROL-DEFINE
      summary: CMD-ROL-DEFINE
      x-aggregate: AGG-ROLE
      x-policy: POL-ROL-DEFINE
      x-events:
      - EVT-ROL-DEFINED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ROLE_CODE_TAKEN
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
              $ref: '#/components/schemas/RolDefineCommand'
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
  /api/v1/foundation/roles/{id}/actions/set-permissions:
    post:
      operationId: CMD-ROL-SET-PERMISSIONS
      summary: CMD-ROL-SET-PERMISSIONS
      x-aggregate: AGG-ROLE
      x-policy: POL-ROL-SET-PERMISSIONS
      x-events:
      - EVT-ROL-PERMISSIONS-CHANGED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ROLE_INVALID_STATE_TRANSITION
      - SYSTEM_ROLE_LOCKED
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
              $ref: '#/components/schemas/RolSetPermissionsCommand'
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
  /api/v1/foundation/roles/{id}/actions/activate:
    post:
      operationId: CMD-ROL-ACTIVATE
      summary: CMD-ROL-ACTIVATE
      x-aggregate: AGG-ROLE
      x-policy: POL-ROL-ACTIVATE
      x-events:
      - EVT-ROL-ACTIVATED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ROLE_EMPTY
      - ROLE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/RolActivateCommand'
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
  /api/v1/foundation/roles/{id}/actions/retire:
    post:
      operationId: CMD-ROL-RETIRE
      summary: CMD-ROL-RETIRE
      x-aggregate: AGG-ROLE
      x-policy: POL-ROL-RETIRE
      x-events:
      - EVT-ROL-RETIRED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - ROLE_INVALID_STATE_TRANSITION
      - ROLE_IN_USE
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
              $ref: '#/components/schemas/RolRetireCommand'
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
  /api/v1/foundation/role-assignments:
    post:
      operationId: CMD-RAS-ASSIGN
      summary: CMD-RAS-ASSIGN
      x-aggregate: AGG-ROLE-ASSIGNMENT
      x-policy: POL-RAS-ASSIGN
      x-events:
      - EVT-RAS-ASSIGNED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - SOD_ROLE_CONFLICT
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
              $ref: '#/components/schemas/RasAssignCommand'
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
  /api/v1/foundation/role-assignments/{id}/actions/revoke:
    post:
      operationId: CMD-RAS-REVOKE
      summary: CMD-RAS-REVOKE
      x-aggregate: AGG-ROLE-ASSIGNMENT
      x-policy: POL-RAS-REVOKE
      x-events:
      - EVT-RAS-REVOKED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - REASON_REQUIRED
      - ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/RasRevokeCommand'
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
  /api/v1/foundation/authority-grants:
    post:
      operationId: CMD-AUT-GRANT
      summary: CMD-AUT-GRANT
      x-aggregate: AGG-AUTHORITY-GRANT
      x-policy: POL-AUT-GRANT
      x-events:
      - EVT-AUT-GRANT-REQUESTED
      x-error-codes:
      - AUTHZ_DENIED
      - IDEMPOTENCY_KEY_REUSED
      - PERMISSION_DENIED
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
              $ref: '#/components/schemas/AutGrantCommand'
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
      operationId: QRY-AUT-LIST
      summary: Grants by holder / scope / effective at t
      x-authorized: Executive or Administrator in scope, or holder
      x-requirement: REQ-FND-007
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
  /api/v1/foundation/authority-grants/{id}/actions/approve-grant:
    post:
      operationId: CMD-AUT-APPROVE-GRANT
      summary: CMD-AUT-APPROVE-GRANT
      x-aggregate: AGG-AUTHORITY-GRANT
      x-policy: POL-AUT-APPROVE-GRANT
      x-events:
      - EVT-AUT-GRANTED
      x-error-codes:
      - AUTHORITY_GRANT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/AutApproveGrantCommand'
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
  /api/v1/foundation/authority-grants/{id}/actions/reject-grant:
    post:
      operationId: CMD-AUT-REJECT-GRANT
      summary: CMD-AUT-REJECT-GRANT
      x-aggregate: AGG-AUTHORITY-GRANT
      x-policy: POL-AUT-REJECT-GRANT
      x-events:
      - EVT-AUT-GRANT-REJECTED
      x-error-codes:
      - AUTHORITY_GRANT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/AutRejectGrantCommand'
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
  /api/v1/foundation/authority-grants/{id}/actions/delegate:
    post:
      operationId: CMD-AUT-DELEGATE
      summary: CMD-AUT-DELEGATE
      x-aggregate: AGG-AUTHORITY-GRANT
      x-policy: POL-AUT-DELEGATE
      x-events:
      - EVT-AUT-DELEGATED
      x-error-codes:
      - AUTHORITY_EXCEEDS_DELEGATOR
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AutDelegateCommand'
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
  /api/v1/foundation/authority-grants/{id}/actions/suspend:
    post:
      operationId: CMD-AUT-SUSPEND
      summary: CMD-AUT-SUSPEND
      x-aggregate: AGG-AUTHORITY-GRANT
      x-policy: POL-AUT-SUSPEND
      x-events:
      - EVT-AUT-SUSPENDED
      x-error-codes:
      - AUTHORITY_GRANT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/AutSuspendCommand'
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
  /api/v1/foundation/authority-grants/{id}/actions/resume:
    post:
      operationId: CMD-AUT-RESUME
      summary: CMD-AUT-RESUME
      x-aggregate: AGG-AUTHORITY-GRANT
      x-policy: POL-AUT-RESUME
      x-events:
      - EVT-AUT-RESUMED
      x-error-codes:
      - AUTHORITY_GRANT_INVALID_STATE_TRANSITION
      - AUTHZ_DENIED
      - GRANT_EXPIRED
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
              $ref: '#/components/schemas/AutResumeCommand'
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
  /api/v1/foundation/authority-grants/{id}/actions/revoke:
    post:
      operationId: CMD-AUT-REVOKE
      summary: CMD-AUT-REVOKE
      x-aggregate: AGG-AUTHORITY-GRANT
      x-policy: POL-AUT-REVOKE
      x-events:
      - EVT-AUT-REVOKED
      x-error-codes:
      - AUTHORITY_GRANT_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/AutRevokeCommand'
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
  /api/v1/foundation/clearances:
    post:
      operationId: CMD-CLR-GRANT
      summary: CMD-CLR-GRANT
      x-aggregate: AGG-CLEARANCE
      x-policy: POL-CLR-GRANT
      x-events:
      - EVT-CLR-REQUESTED
      x-error-codes:
      - AUTHZ_DENIED
      - CLEARANCE_EXISTS
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
              $ref: '#/components/schemas/ClrGrantCommand'
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
  /api/v1/foundation/clearances/{id}/actions/approve:
    post:
      operationId: CMD-CLR-APPROVE
      summary: CMD-CLR-APPROVE
      x-aggregate: AGG-CLEARANCE
      x-policy: POL-CLR-APPROVE
      x-events:
      - EVT-CLR-GRANTED
      x-error-codes:
      - AUTHZ_DENIED
      - CLEARANCE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/ClrApproveCommand'
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
  /api/v1/foundation/clearances/{id}/actions/modify:
    post:
      operationId: CMD-CLR-MODIFY
      summary: CMD-CLR-MODIFY
      x-aggregate: AGG-CLEARANCE
      x-policy: POL-CLR-MODIFY
      x-events:
      - EVT-CLR-MODIFIED
      x-error-codes:
      - AUTHZ_DENIED
      - CLEARANCE_INVALID
      - CLEARANCE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/ClrModifyCommand'
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
  /api/v1/foundation/clearances/{id}/actions/suspend:
    post:
      operationId: CMD-CLR-SUSPEND
      summary: CMD-CLR-SUSPEND
      x-aggregate: AGG-CLEARANCE
      x-policy: POL-CLR-SUSPEND
      x-events:
      - EVT-CLR-SUSPENDED
      x-error-codes:
      - AUTHZ_DENIED
      - CLEARANCE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/ClrSuspendCommand'
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
  /api/v1/foundation/clearances/{id}/actions/reinstate:
    post:
      operationId: CMD-CLR-REINSTATE
      summary: CMD-CLR-REINSTATE
      x-aggregate: AGG-CLEARANCE
      x-policy: POL-CLR-REINSTATE
      x-events:
      - EVT-CLR-REINSTATED
      x-error-codes:
      - AUTHZ_DENIED
      - CLEARANCE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/ClrReinstateCommand'
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
  /api/v1/foundation/clearances/{id}/actions/revoke:
    post:
      operationId: CMD-CLR-REVOKE
      summary: CMD-CLR-REVOKE
      x-aggregate: AGG-CLEARANCE
      x-policy: POL-CLR-REVOKE
      x-events:
      - EVT-CLR-REVOKED
      x-error-codes:
      - AUTHZ_DENIED
      - CLEARANCE_INVALID_STATE_TRANSITION
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
              $ref: '#/components/schemas/ClrRevokeCommand'
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
  /api/v1/foundation/tenants/{tenant_id}:
    get:
      operationId: QRY-TEN-GET
      summary: Tenant state, cell, quotas
      x-authorized: platform operator or tenant Administrator of that tenant
      x-requirement: REQ-FND-001
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: tenant_id
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
  /api/v1/foundation/organizations/{org_id}/units:
    get:
      operationId: QRY-ORG-TREE
      summary: Unit tree (cursor pagination on flattened order)
      x-authorized: any user of tenant (view org structure)
      x-requirement: REQ-FND-002
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: org_id
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
  /api/v1/foundation/users/{user_id}:
    get:
      operationId: QRY-USR-GET
      summary: User with identities (no secrets)
      x-authorized: Administrator in scope or self
      x-requirement: REQ-FND-006
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: user_id
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
  /api/v1/foundation/me/security-context:
    get:
      operationId: QRY-SEC-CONTEXT
      summary: Caller's resolved SecurityContext
      x-authorized: self
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
                type: object
                description: PL-SECURITY-CONTEXT
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
  /api/v1/foundation/authority-checks:
    post:
      operationId: QRY-AUT-CHECK
      summary: AuthorityCheck(actor, decision_type, scope, at, amount?)
      x-authorized: internal services (workload identity) or self
      x-requirement: REQ-FND-009
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuthorityCheckResponse'
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AuthorityCheckRequest'
  /api/v1/foundation/users/{user_id}/clearance:
    get:
      operationId: QRY-CLR-GET
      summary: Current clearance (level/compartments)
      x-authorized: Security Officer or self
      x-requirement: REQ-GOV-003
      parameters:
      - $ref: '#/components/parameters/X-Purpose'
      - $ref: '#/components/parameters/X-Correlation-Id'
      - name: user_id
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
    TenProvisionCommand:
      type: object
      properties:
        namespace:
          type: string
        display_name:
          type: string
        cell_mode:
          type: string
          enum:
          - shared
          - dedicated
        sovereign:
          type: boolean
        top_level_enabled:
          type: boolean
        jurisdiction:
          type: string
        quotas:
          $ref: '#/components/schemas/TenantQuotas'
      additionalProperties: false
      required:
      - namespace
      - display_name
      - cell_mode
      - sovereign
      - top_level_enabled
      - jurisdiction
      - quotas
    TenRetryProvisioningCommand:
      type: object
      properties: {}
      additionalProperties: false
    TenSuspendCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    TenReactivateCommand:
      type: object
      properties: {}
      additionalProperties: false
    TenStartCellMigrationCommand:
      type: object
      properties:
        target_cell:
          type: string
      additionalProperties: false
      required:
      - target_cell
    TenStartDecommissionCommand:
      type: object
      properties:
        reason:
          type: string
        second_approver:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - reason
      - second_approver
    TenUpdateQuotasCommand:
      type: object
      properties:
        quotas:
          $ref: '#/components/schemas/TenantQuotas'
      additionalProperties: false
      required:
      - quotas
    OrgCreateCommand:
      type: object
      properties:
        name:
          $ref: '#/components/schemas/LocalizedName'
        root_unit_name:
          $ref: '#/components/schemas/LocalizedName'
      additionalProperties: false
      required:
      - name
      - root_unit_name
    OrgRenameCommand:
      type: object
      properties:
        name:
          $ref: '#/components/schemas/LocalizedName'
      additionalProperties: false
      required:
      - name
    OrgAddUnitCommand:
      type: object
      properties:
        parent_unit:
          $ref: '#/components/schemas/Urn'
        name:
          $ref: '#/components/schemas/LocalizedName'
      additionalProperties: false
      required:
      - parent_unit
      - name
    OrgRenameUnitCommand:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/Urn'
        name:
          $ref: '#/components/schemas/LocalizedName'
      additionalProperties: false
      required:
      - unit
      - name
    OrgMoveUnitCommand:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/Urn'
        new_parent:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - unit
      - new_parent
    OrgDeactivateUnitCommand:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/Urn'
        reason:
          type: string
      additionalProperties: false
      required:
      - unit
      - reason
    OrgDeactivateCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    OrgReactivateCommand:
      type: object
      properties: {}
      additionalProperties: false
    PerRegisterCommand:
      type: object
      properties:
        names:
          type: array
          items: &id001
            $ref: '#/components/schemas/LocalizedName'
        hr_id:
          type: string
        contact:
          type: object
      additionalProperties: false
      required:
      - names
    PerUpdateDetailsCommand:
      type: object
      properties:
        names:
          type: array
          items: *id001
        contact:
          type: object
      additionalProperties: false
    PerDeactivateCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    PerReactivateCommand:
      type: object
      properties: {}
      additionalProperties: false
    PerEraseCommand:
      type: object
      properties:
        erasure_order_ref:
          type: string
      additionalProperties: false
      required:
      - erasure_order_ref
    UsrProvisionCommand:
      type: object
      properties:
        username:
          type: string
        person:
          $ref: '#/components/schemas/Urn'
        source:
          type: string
          enum:
          - scim
          - admin
      additionalProperties: false
      required:
      - username
      - source
    UsrLinkIdentityCommand:
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
    UsrUnlinkIdentityCommand:
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
    UsrLinkPersonCommand:
      type: object
      properties:
        person:
          $ref: '#/components/schemas/Urn'
      additionalProperties: false
      required:
      - person
    UsrLockCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    UsrUnlockCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    UsrDisableCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
    UsrEnableCommand:
      type: object
      properties: {}
      additionalProperties: false
    UsrCloseCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    SvcCreateCommand:
      type: object
      properties:
        name:
          type: string
        owner:
          $ref: '#/components/schemas/Urn'
        purpose:
          type: string
      additionalProperties: false
      required:
      - name
      - owner
      - purpose
    SvcRotateCredentialCommand:
      type: object
      properties:
        public_key:
          type: string
        expires_at:
          type: string
          format: date-time
      additionalProperties: false
      required:
      - public_key
      - expires_at
    SvcDisableCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
    SvcEnableCommand:
      type: object
      properties: {}
      additionalProperties: false
    SvcCloseCommand:
      type: object
      properties: {}
      additionalProperties: false
    RolDefineCommand:
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
    RolSetPermissionsCommand:
      type: object
      properties:
        permissions:
          type: array
          items:
            $ref: '#/components/schemas/Permission'
      additionalProperties: false
      required:
      - permissions
    RolActivateCommand:
      type: object
      properties: {}
      additionalProperties: false
    RolRetireCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    RasAssignCommand:
      type: object
      properties:
        user:
          $ref: '#/components/schemas/Urn'
        role:
          $ref: '#/components/schemas/Urn'
        org_scope:
          $ref: '#/components/schemas/Urn'
        include_descendants:
          type: boolean
        valid_from:
          type: string
          format: date-time
        valid_to:
          type: string
          format: date-time
      additionalProperties: false
      required:
      - user
      - role
      - org_scope
      - include_descendants
      - valid_from
    RasRevokeCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    AutGrantCommand:
      type: object
      properties:
        holder:
          $ref: '#/components/schemas/Urn'
        decision_types:
          type: array
          items:
            type: string
        org_scope:
          $ref: '#/components/schemas/Urn'
        include_descendants:
          type: boolean
        limits:
          type: object
        valid_from:
          type: string
          format: date-time
        valid_to:
          type: string
          format: date-time
        delegable:
          type: boolean
      additionalProperties: false
      required:
      - holder
      - decision_types
      - org_scope
      - include_descendants
      - valid_from
      - delegable
    AutApproveGrantCommand:
      type: object
      properties: {}
      additionalProperties: false
    AutRejectGrantCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    AutDelegateCommand:
      type: object
      properties:
        delegate:
          $ref: '#/components/schemas/Urn'
        decision_types:
          type: array
          items:
            type: string
        org_scope:
          $ref: '#/components/schemas/Urn'
        include_descendants:
          type: boolean
        limits:
          type: object
        valid_from:
          type: string
          format: date-time
        valid_to:
          type: string
          format: date-time
        delegable:
          type: boolean
      additionalProperties: false
      required:
      - delegate
      - decision_types
      - org_scope
      - include_descendants
      - valid_from
      - valid_to
      - delegable
    AutSuspendCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    AutResumeCommand:
      type: object
      properties: {}
      additionalProperties: false
    AutRevokeCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ClrGrantCommand:
      type: object
      properties:
        user:
          $ref: '#/components/schemas/Urn'
        level:
          type: string
        compartments:
          type: array
          items:
            type: string
        caveat_attributes:
          type: object
        valid_to:
          type: string
          format: date-time
      additionalProperties: false
      required:
      - user
      - level
      - compartments
    ClrApproveCommand:
      type: object
      properties: {}
      additionalProperties: false
    ClrModifyCommand:
      type: object
      properties:
        level:
          type: string
        compartments:
          type: array
          items:
            type: string
        caveat_attributes:
          type: object
      additionalProperties: false
      required:
      - level
      - compartments
    ClrSuspendCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
    ClrReinstateCommand:
      type: object
      properties: {}
      additionalProperties: false
    ClrRevokeCommand:
      type: object
      properties:
        reason:
          type: string
      additionalProperties: false
      required:
      - reason
```
