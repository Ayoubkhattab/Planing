---
id: CMD-CAT-BC01-SLC01
type: command-catalog
title: Commands — BC01 (SLC-01)
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC01 (SLC-01)

_58 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-TEN-PROVISION | AGG-TENANT | `POST /api/v1/foundation/tenants` | لا | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-PROVISION | `namespace!:string display_name!:string cell_mode!:enum(shared,dedicated) sovereign!:boolean top_level_enabled!:boolean jurisdiction!:string quotas!:TenantQuotas` | EVT-TEN-PROVISIONING-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TENANT_NAMESPACE_TAKEN, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TEN-COMPLETE-PROVISIONING | AGG-TENANT | `POST /api/v1/foundation/tenants/{id}/actions/complete-provisioning` | نعم | system (workload identity) | POL-TEN-COMPLETE-PROVISIONING | `steps!:array` | EVT-TEN-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TENANT_INVALID_STATE_TRANSITION, TENANT_PROVISIONING_INCOMPLETE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TEN-FAIL-PROVISIONING | AGG-TENANT | `POST /api/v1/foundation/tenants/{id}/actions/fail-provisioning` | نعم | system (workload identity) | POL-TEN-FAIL-PROVISIONING | `failed_step!:string reason!:string` | EVT-TEN-PROVISIONING-FAILED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TENANT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TEN-RETRY-PROVISIONING | AGG-TENANT | `POST /api/v1/foundation/tenants/{id}/actions/retry-provisioning` | لا | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-RETRY-PROVISIONING | `—` | EVT-TEN-PROVISIONING-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TENANT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TEN-SUSPEND | AGG-TENANT | `POST /api/v1/foundation/tenants/{id}/actions/suspend` | لا | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-SUSPEND | `reason!:string` | EVT-TEN-SUSPENDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, TENANT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TEN-REACTIVATE | AGG-TENANT | `POST /api/v1/foundation/tenants/{id}/actions/reactivate` | لا | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-REACTIVATE | `—` | EVT-TEN-REACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TENANT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TEN-START-CELL-MIGRATION | AGG-TENANT | `POST /api/v1/foundation/tenants/{id}/actions/start-cell-migration` | لا | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-START-CELL-MIGRATION | `target_cell!:string` | EVT-TEN-MIGRATION-STARTED | AUTHZ_DENIED, CELL_UNAVAILABLE, IDEMPOTENCY_KEY_REUSED, TENANT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TEN-COMPLETE-CELL-MIGRATION | AGG-TENANT | `POST /api/v1/foundation/tenants/{id}/actions/complete-cell-migration` | نعم | system (workload identity) | POL-TEN-COMPLETE-CELL-MIGRATION | `reconciliation_report!:string` | EVT-TEN-MIGRATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MIGRATION_NOT_RECONCILED, TENANT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TEN-START-DECOMMISSION | AGG-TENANT | `POST /api/v1/foundation/tenants/{id}/actions/start-decommission` | لا | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-START-DECOMMISSION | `reason!:string second_approver!:urn` | EVT-TEN-DECOMMISSION-STARTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LEGAL_HOLD_ACTIVE, SEGREGATION_OF_DUTIES, TENANT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TEN-COMPLETE-DECOMMISSION | AGG-TENANT | `POST /api/v1/foundation/tenants/{id}/actions/complete-decommission` | نعم | system (workload identity) | POL-TEN-COMPLETE-DECOMMISSION | `—` | EVT-TEN-DECOMMISSIONED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TENANT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-TEN-UPDATE-QUOTAS | AGG-TENANT | `POST /api/v1/foundation/tenants/{id}/actions/update-quotas` | لا | Platform Operator (provision, migrate, decommission) / Tenant Administrator (quotas view) | POL-TEN-UPDATE-QUOTAS | `quotas!:TenantQuotas` | EVT-TEN-QUOTAS-UPDATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, QUOTA_EXCEEDS_CAPACITY, TENANT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ORG-CREATE | AGG-ORGANIZATION | `POST /api/v1/foundation/organizations` | لا | Administrator (in scope) | POL-ORG-CREATE | `name!:LocalizedName root_unit_name!:LocalizedName` | EVT-ORG-CREATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ORG_NAME_TAKEN, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ORG-RENAME | AGG-ORGANIZATION | `POST /api/v1/foundation/organizations/{id}/actions/rename` | لا | Administrator (in scope) | POL-ORG-RENAME | `name!:LocalizedName` | EVT-ORG-RENAMED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ORGANIZATION_INVALID_STATE_TRANSITION, ORG_NAME_TAKEN, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ORG-ADD-UNIT | AGG-ORGANIZATION | `POST /api/v1/foundation/organizations/{id}/actions/add-unit` | لا | Administrator (in scope) | POL-ORG-ADD-UNIT | `parent_unit!:urn name!:LocalizedName` | EVT-ORG-UNIT-ADDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ORGANIZATION_INVALID_STATE_TRANSITION, ORG_UNIT_INVALID_PARENT, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ORG-RENAME-UNIT | AGG-ORGANIZATION | `POST /api/v1/foundation/organizations/{id}/actions/rename-unit` | لا | Administrator (in scope) | POL-ORG-RENAME-UNIT | `unit!:urn name!:LocalizedName` | EVT-ORG-UNIT-RENAMED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ORGANIZATION_INVALID_STATE_TRANSITION, ORG_UNIT_NAME_TAKEN, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ORG-MOVE-UNIT | AGG-ORGANIZATION | `POST /api/v1/foundation/organizations/{id}/actions/move-unit` | لا | Administrator (in scope) | POL-ORG-MOVE-UNIT | `unit!:urn new_parent!:urn` | EVT-ORG-UNIT-MOVED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ORGANIZATION_INVALID_STATE_TRANSITION, ORG_UNIT_CYCLE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ORG-DEACTIVATE-UNIT | AGG-ORGANIZATION | `POST /api/v1/foundation/organizations/{id}/actions/deactivate-unit` | لا | Administrator (in scope) | POL-ORG-DEACTIVATE-UNIT | `unit!:urn reason!:string` | EVT-ORG-UNIT-DEACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ORGANIZATION_INVALID_STATE_TRANSITION, ORG_UNIT_IN_USE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ORG-DEACTIVATE | AGG-ORGANIZATION | `POST /api/v1/foundation/organizations/{id}/actions/deactivate` | لا | Administrator (in scope) | POL-ORG-DEACTIVATE | `reason!:string` | EVT-ORG-DEACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ORGANIZATION_INVALID_STATE_TRANSITION, ORG_IN_USE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ORG-REACTIVATE | AGG-ORGANIZATION | `POST /api/v1/foundation/organizations/{id}/actions/reactivate` | لا | Administrator (in scope) | POL-ORG-REACTIVATE | `—` | EVT-ORG-REACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ORGANIZATION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PER-REGISTER | AGG-PERSON | `POST /api/v1/foundation/persons` | لا | Administrator (in scope) | POL-PER-REGISTER | `names!:array hr_id:string contact:object` | EVT-PER-REGISTERED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PERSON_DUPLICATE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PER-UPDATE-DETAILS | AGG-PERSON | `POST /api/v1/foundation/persons/{id}/actions/update-details` | لا | Administrator (in scope) | POL-PER-UPDATE-DETAILS | `names:array contact:object` | EVT-PER-DETAILS-UPDATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PERSON_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PER-DEACTIVATE | AGG-PERSON | `POST /api/v1/foundation/persons/{id}/actions/deactivate` | لا | Administrator (in scope) | POL-PER-DEACTIVATE | `reason!:string` | EVT-PER-DEACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PERSON_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PER-REACTIVATE | AGG-PERSON | `POST /api/v1/foundation/persons/{id}/actions/reactivate` | لا | Administrator (in scope) | POL-PER-REACTIVATE | `—` | EVT-PER-REACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PERSON_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PER-ERASE | AGG-PERSON | `POST /api/v1/foundation/persons/{id}/actions/erase` | لا | Administrator (in scope) | POL-PER-ERASE | `erasure_order_ref!:string` | EVT-PER-ERASED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LEGAL_HOLD_ACTIVE, PERSON_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-USR-PROVISION | AGG-USER | `POST /api/v1/foundation/users` | لا | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-PROVISION | `username!:string person:urn source!:enum(scim,admin)` | EVT-USR-PROVISIONED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, TENANT_NOT_ACTIVE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-USR-LINK-IDENTITY | AGG-USER | `POST /api/v1/foundation/users/{id}/actions/link-identity` | لا | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-LINK-IDENTITY | `issuer!:string subject!:string` | EVT-USR-IDENTITY-LINKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, IDENTITY_ALREADY_LINKED, USER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-USR-UNLINK-IDENTITY | AGG-USER | `POST /api/v1/foundation/users/{id}/actions/unlink-identity` | لا | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-UNLINK-IDENTITY | `issuer!:string subject!:string` | EVT-USR-IDENTITY-UNLINKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LAST_IDENTITY, USER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-USR-LINK-PERSON | AGG-USER | `POST /api/v1/foundation/users/{id}/actions/link-person` | لا | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-LINK-PERSON | `person!:urn` | EVT-USR-PERSON-LINKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PERSON_ALREADY_LINKED, USER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-USR-RECORD-FIRST-SIGN-IN | AGG-USER | `POST /api/v1/foundation/users/{id}/actions/record-first-sign-in` | نعم | system (workload identity) | POL-USR-RECORD-FIRST-SIGN-IN | `issuer!:string subject!:string` | EVT-USR-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, USER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-USR-LOCK | AGG-USER | `POST /api/v1/foundation/users/{id}/actions/lock` | لا | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-LOCK | `reason!:string` | EVT-USR-LOCKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, USER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-USR-UNLOCK | AGG-USER | `POST /api/v1/foundation/users/{id}/actions/unlock` | لا | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-UNLOCK | `reason!:string` | EVT-USR-UNLOCKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, USER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-USR-DISABLE | AGG-USER | `POST /api/v1/foundation/users/{id}/actions/disable` | لا | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-DISABLE | `reason:string` | EVT-USR-DISABLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, USER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-USR-ENABLE | AGG-USER | `POST /api/v1/foundation/users/{id}/actions/enable` | لا | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-ENABLE | `—` | EVT-USR-ENABLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, LAST_IDENTITY, USER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-USR-CLOSE | AGG-USER | `POST /api/v1/foundation/users/{id}/actions/close` | لا | Administrator in scope / SCIM service account / Security Officer (lock) | POL-USR-CLOSE | `reason!:string` | EVT-USR-CLOSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, USER_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SVC-CREATE | AGG-SERVICE-ACCOUNT | `POST /api/v1/foundation/service-accounts` | لا | Administrator | POL-SVC-CREATE | `name!:string owner!:urn purpose!:string` | EVT-SVC-CREATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OWNER_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SVC-ROTATE-CREDENTIAL | AGG-SERVICE-ACCOUNT | `POST /api/v1/foundation/service-accounts/{id}/actions/rotate-credential` | لا | Administrator | POL-SVC-ROTATE-CREDENTIAL | `public_key!:string expires_at!:date-time` | EVT-SVC-CREDENTIAL-ROTATED | AUTHZ_DENIED, CREDENTIAL_LIFETIME_EXCEEDED, IDEMPOTENCY_KEY_REUSED, SERVICE_ACCOUNT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SVC-DISABLE | AGG-SERVICE-ACCOUNT | `POST /api/v1/foundation/service-accounts/{id}/actions/disable` | لا | Administrator | POL-SVC-DISABLE | `reason:string` | EVT-SVC-DISABLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SERVICE_ACCOUNT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SVC-ENABLE | AGG-SERVICE-ACCOUNT | `POST /api/v1/foundation/service-accounts/{id}/actions/enable` | لا | Administrator | POL-SVC-ENABLE | `—` | EVT-SVC-ENABLED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OWNER_REQUIRED, SERVICE_ACCOUNT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SVC-CLOSE | AGG-SERVICE-ACCOUNT | `POST /api/v1/foundation/service-accounts/{id}/actions/close` | لا | Administrator | POL-SVC-CLOSE | `—` | EVT-SVC-CLOSED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SERVICE_ACCOUNT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ROL-DEFINE | AGG-ROLE | `POST /api/v1/foundation/roles` | لا | Administrator | POL-ROL-DEFINE | `code!:string name!:LocalizedName` | EVT-ROL-DEFINED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ROLE_CODE_TAKEN, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ROL-SET-PERMISSIONS | AGG-ROLE | `POST /api/v1/foundation/roles/{id}/actions/set-permissions` | لا | Administrator | POL-ROL-SET-PERMISSIONS | `permissions!:array` | EVT-ROL-PERMISSIONS-CHANGED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ROLE_INVALID_STATE_TRANSITION, SYSTEM_ROLE_LOCKED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ROL-ACTIVATE | AGG-ROLE | `POST /api/v1/foundation/roles/{id}/actions/activate` | لا | Administrator | POL-ROL-ACTIVATE | `—` | EVT-ROL-ACTIVATED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ROLE_EMPTY, ROLE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-ROL-RETIRE | AGG-ROLE | `POST /api/v1/foundation/roles/{id}/actions/retire` | لا | Administrator | POL-ROL-RETIRE | `reason!:string` | EVT-ROL-RETIRED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, ROLE_INVALID_STATE_TRANSITION, ROLE_IN_USE, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RAS-ASSIGN | AGG-ROLE-ASSIGNMENT | `POST /api/v1/foundation/role-assignments` | لا | Administrator (in scope, not self) | POL-RAS-ASSIGN | `user!:urn role!:urn org_scope!:urn include_descendants!:boolean valid_from!:date-time valid_to:date-time` | EVT-RAS-ASSIGNED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, SOD_ROLE_CONFLICT, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-RAS-REVOKE | AGG-ROLE-ASSIGNMENT | `POST /api/v1/foundation/role-assignments/{id}/actions/revoke` | لا | Administrator (in scope, not self) | POL-RAS-REVOKE | `reason!:string` | EVT-RAS-REVOKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AUT-GRANT | AGG-AUTHORITY-GRANT | `POST /api/v1/foundation/authority-grants` | لا | holder of authority.grant; Executive approves | POL-AUT-GRANT | `holder!:urn decision_types!:array org_scope!:urn include_descendants!:boolean limits:object valid_from!:date-time valid_to:date-time delegable!:boolean` | EVT-AUT-GRANT-REQUESTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PERMISSION_DENIED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AUT-APPROVE-GRANT | AGG-AUTHORITY-GRANT | `POST /api/v1/foundation/authority-grants/{id}/actions/approve-grant` | لا | holder of authority.grant; Executive approves | POL-AUT-APPROVE-GRANT | `—` | EVT-AUT-GRANTED | AUTHORITY_GRANT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AUT-REJECT-GRANT | AGG-AUTHORITY-GRANT | `POST /api/v1/foundation/authority-grants/{id}/actions/reject-grant` | لا | holder of authority.grant; Executive approves | POL-AUT-REJECT-GRANT | `reason!:string` | EVT-AUT-GRANT-REJECTED | AUTHORITY_GRANT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AUT-DELEGATE | AGG-AUTHORITY-GRANT | `POST /api/v1/foundation/authority-grants/{id}/actions/delegate` | لا | holder of authority.grant; Executive approves | POL-AUT-DELEGATE | `delegate!:urn decision_types!:array org_scope!:urn include_descendants!:boolean limits:object valid_from!:date-time valid_to!:date-time delegable!:boolean` | EVT-AUT-DELEGATED | AUTHORITY_EXCEEDS_DELEGATOR, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AUT-SUSPEND | AGG-AUTHORITY-GRANT | `POST /api/v1/foundation/authority-grants/{id}/actions/suspend` | لا | holder of authority.grant; Executive approves | POL-AUT-SUSPEND | `reason!:string` | EVT-AUT-SUSPENDED | AUTHORITY_GRANT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AUT-RESUME | AGG-AUTHORITY-GRANT | `POST /api/v1/foundation/authority-grants/{id}/actions/resume` | لا | holder of authority.grant; Executive approves | POL-AUT-RESUME | `—` | EVT-AUT-RESUMED | AUTHORITY_GRANT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, GRANT_EXPIRED, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-AUT-REVOKE | AGG-AUTHORITY-GRANT | `POST /api/v1/foundation/authority-grants/{id}/actions/revoke` | لا | holder of authority.grant; Executive approves | POL-AUT-REVOKE | `reason!:string` | EVT-AUT-REVOKED | AUTHORITY_GRANT_INVALID_STATE_TRANSITION, AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLR-GRANT | AGG-CLEARANCE | `POST /api/v1/foundation/clearances` | لا | Security Officer | POL-CLR-GRANT | `user!:urn level!:string compartments!:array caveat_attributes:object valid_to:date-time` | EVT-CLR-REQUESTED | AUTHZ_DENIED, CLEARANCE_EXISTS, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLR-APPROVE | AGG-CLEARANCE | `POST /api/v1/foundation/clearances/{id}/actions/approve` | لا | Security Officer | POL-CLR-APPROVE | `—` | EVT-CLR-GRANTED | AUTHZ_DENIED, CLEARANCE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, SEGREGATION_OF_DUTIES, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLR-MODIFY | AGG-CLEARANCE | `POST /api/v1/foundation/clearances/{id}/actions/modify` | لا | Security Officer | POL-CLR-MODIFY | `level!:string compartments!:array caveat_attributes:object` | EVT-CLR-MODIFIED | AUTHZ_DENIED, CLEARANCE_INVALID, CLEARANCE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLR-SUSPEND | AGG-CLEARANCE | `POST /api/v1/foundation/clearances/{id}/actions/suspend` | لا | Security Officer | POL-CLR-SUSPEND | `reason!:string` | EVT-CLR-SUSPENDED | AUTHZ_DENIED, CLEARANCE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLR-REINSTATE | AGG-CLEARANCE | `POST /api/v1/foundation/clearances/{id}/actions/reinstate` | لا | Security Officer | POL-CLR-REINSTATE | `—` | EVT-CLR-REINSTATED | AUTHZ_DENIED, CLEARANCE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-CLR-REVOKE | AGG-CLEARANCE | `POST /api/v1/foundation/clearances/{id}/actions/revoke` | لا | Security Officer | POL-CLR-REVOKE | `reason!:string` | EVT-CLR-REVOKED | AUTHZ_DENIED, CLEARANCE_INVALID_STATE_TRANSITION, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-TEN-PROVISION
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - ∅
    to: PROVISIONING
    guard: namespace unique; cell_mode valid for tenant profile (INV-TEN-03)
    event: EVT-TEN-PROVISIONING-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TENANT_NAMESPACE_TAKEN
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/tenants
  internal: false
  policy: POL-TEN-PROVISION
  actors: Platform Operator (provision, migrate, decommission) / Tenant Administrator
    (quotas view)
  payload: namespace!:string display_name!:string cell_mode!:enum(shared,dedicated)
    sovereign!:boolean top_level_enabled!:boolean jurisdiction!:string quotas!:TenantQuotas
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-TEN-COMPLETE-PROVISIONING
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - PROVISIONING
    to: ACTIVE
    guard: system; all provisioning steps confirmed (isolation, keys, scheme, roles,
      quotas, audit stream)
    event: EVT-TEN-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TENANT_INVALID_STATE_TRANSITION
  - TENANT_PROVISIONING_INCOMPLETE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/tenants/{id}/actions/complete-provisioning
  internal: true
  policy: POL-TEN-COMPLETE-PROVISIONING
  actors: system (workload identity)
  payload: steps!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TEN-FAIL-PROVISIONING
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - PROVISIONING
    to: PROVISIONING_FAILED
    guard: system; compensation completed
    event: EVT-TEN-PROVISIONING-FAILED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TENANT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/tenants/{id}/actions/fail-provisioning
  internal: true
  policy: POL-TEN-FAIL-PROVISIONING
  actors: system (workload identity)
  payload: failed_step!:string reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TEN-RETRY-PROVISIONING
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - PROVISIONING_FAILED
    to: PROVISIONING
    guard: actor = platform operator
    event: EVT-TEN-PROVISIONING-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TENANT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/tenants/{id}/actions/retry-provisioning
  internal: false
  policy: POL-TEN-RETRY-PROVISIONING
  actors: Platform Operator (provision, migrate, decommission) / Tenant Administrator
    (quotas view)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TEN-SUSPEND
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: SUSPENDED
    guard: reason provided
    event: EVT-TEN-SUSPENDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - TENANT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/tenants/{id}/actions/suspend
  internal: false
  policy: POL-TEN-SUSPEND
  actors: Platform Operator (provision, migrate, decommission) / Tenant Administrator
    (quotas view)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TEN-REACTIVATE
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - SUSPENDED
    to: ACTIVE
    guard: —
    event: EVT-TEN-REACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TENANT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/tenants/{id}/actions/reactivate
  internal: false
  policy: POL-TEN-REACTIVATE
  actors: Platform Operator (provision, migrate, decommission) / Tenant Administrator
    (quotas view)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TEN-START-CELL-MIGRATION
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: MIGRATING
    guard: target cell exists and has capacity
    event: EVT-TEN-MIGRATION-STARTED
  errors:
  - AUTHZ_DENIED
  - CELL_UNAVAILABLE
  - IDEMPOTENCY_KEY_REUSED
  - TENANT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/tenants/{id}/actions/start-cell-migration
  internal: false
  policy: POL-TEN-START-CELL-MIGRATION
  actors: Platform Operator (provision, migrate, decommission) / Tenant Administrator
    (quotas view)
  payload: target_cell!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TEN-COMPLETE-CELL-MIGRATION
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - MIGRATING
    to: ACTIVE
    guard: system; export/import reconciled
    event: EVT-TEN-MIGRATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MIGRATION_NOT_RECONCILED
  - TENANT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/tenants/{id}/actions/complete-cell-migration
  internal: true
  policy: POL-TEN-COMPLETE-CELL-MIGRATION
  actors: system (workload identity)
  payload: reconciliation_report!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TEN-START-DECOMMISSION
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: DECOMMISSIONING
    guard: no active legal hold (BC08 query); two-person approval
    event: EVT-TEN-DECOMMISSION-STARTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LEGAL_HOLD_ACTIVE
  - SEGREGATION_OF_DUTIES
  - TENANT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/tenants/{id}/actions/start-decommission
  internal: false
  policy: POL-TEN-START-DECOMMISSION
  actors: Platform Operator (provision, migrate, decommission) / Tenant Administrator
    (quotas view)
  payload: reason!:string second_approver!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TEN-COMPLETE-DECOMMISSION
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - DECOMMISSIONING
    to: DECOMMISSIONED
    guard: system; keys destroyed, stores removed
    event: EVT-TEN-DECOMMISSIONED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TENANT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/tenants/{id}/actions/complete-decommission
  internal: true
  policy: POL-TEN-COMPLETE-DECOMMISSION
  actors: system (workload identity)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-TEN-UPDATE-QUOTAS
  aggregate: AGG-TENANT
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    - SUSPENDED
    to: '='
    guard: quotas ≤ cell capacity
    event: EVT-TEN-QUOTAS-UPDATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - QUOTA_EXCEEDS_CAPACITY
  - TENANT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/tenants/{id}/actions/update-quotas
  internal: false
  policy: POL-TEN-UPDATE-QUOTAS
  actors: Platform Operator (provision, migrate, decommission) / Tenant Administrator
    (quotas view)
  payload: quotas!:TenantQuotas
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ORG-CREATE
  aggregate: AGG-ORGANIZATION
  bc: BC01
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: tenant ACTIVE; name unique in tenant; creates root unit
    event: EVT-ORG-CREATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ORG_NAME_TAKEN
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/organizations
  internal: false
  policy: POL-ORG-CREATE
  actors: Administrator (in scope)
  payload: name!:LocalizedName root_unit_name!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ORG-RENAME
  aggregate: AGG-ORGANIZATION
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: name unique in tenant
    event: EVT-ORG-RENAMED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ORGANIZATION_INVALID_STATE_TRANSITION
  - ORG_NAME_TAKEN
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/organizations/{id}/actions/rename
  internal: false
  policy: POL-ORG-RENAME
  actors: Administrator (in scope)
  payload: name!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ORG-ADD-UNIT
  aggregate: AGG-ORGANIZATION
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: parent unit ACTIVE; sibling name unique
    event: EVT-ORG-UNIT-ADDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ORGANIZATION_INVALID_STATE_TRANSITION
  - ORG_UNIT_INVALID_PARENT
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/organizations/{id}/actions/add-unit
  internal: false
  policy: POL-ORG-ADD-UNIT
  actors: Administrator (in scope)
  payload: parent_unit!:urn name!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ORG-RENAME-UNIT
  aggregate: AGG-ORGANIZATION
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: sibling name unique
    event: EVT-ORG-UNIT-RENAMED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ORGANIZATION_INVALID_STATE_TRANSITION
  - ORG_UNIT_NAME_TAKEN
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/organizations/{id}/actions/rename-unit
  internal: false
  policy: POL-ORG-RENAME-UNIT
  actors: Administrator (in scope)
  payload: unit!:urn name!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ORG-MOVE-UNIT
  aggregate: AGG-ORGANIZATION
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: new parent ACTIVE, same org, not a descendant (no cycle); root cannot move
    event: EVT-ORG-UNIT-MOVED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ORGANIZATION_INVALID_STATE_TRANSITION
  - ORG_UNIT_CYCLE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/organizations/{id}/actions/move-unit
  internal: false
  policy: POL-ORG-MOVE-UNIT
  actors: Administrator (in scope)
  payload: unit!:urn new_parent!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ORG-DEACTIVATE-UNIT
  aggregate: AGG-ORGANIZATION
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: no active children; no active role assignments, grants or clearances scoped
      only to it (BC01 query)
    event: EVT-ORG-UNIT-DEACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ORGANIZATION_INVALID_STATE_TRANSITION
  - ORG_UNIT_IN_USE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/organizations/{id}/actions/deactivate-unit
  internal: false
  policy: POL-ORG-DEACTIVATE-UNIT
  actors: Administrator (in scope)
  payload: unit!:urn reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ORG-DEACTIVATE
  aggregate: AGG-ORGANIZATION
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: INACTIVE
    guard: all non-root units inactive; no active assignments
    event: EVT-ORG-DEACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ORGANIZATION_INVALID_STATE_TRANSITION
  - ORG_IN_USE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/organizations/{id}/actions/deactivate
  internal: false
  policy: POL-ORG-DEACTIVATE
  actors: Administrator (in scope)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ORG-REACTIVATE
  aggregate: AGG-ORGANIZATION
  bc: BC01
  transitions:
  - from:
    - INACTIVE
    to: ACTIVE
    guard: tenant ACTIVE
    event: EVT-ORG-REACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ORGANIZATION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/organizations/{id}/actions/reactivate
  internal: false
  policy: POL-ORG-REACTIVATE
  actors: Administrator (in scope)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PER-REGISTER
  aggregate: AGG-PERSON
  bc: BC01
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: names per language-model; no duplicate HR id
    event: EVT-PER-REGISTERED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PERSON_DUPLICATE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/persons
  internal: false
  policy: POL-PER-REGISTER
  actors: Administrator (in scope)
  payload: names!:array hr_id:string contact:object
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-PER-UPDATE-DETAILS
  aggregate: AGG-PERSON
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: —
    event: EVT-PER-DETAILS-UPDATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PERSON_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/persons/{id}/actions/update-details
  internal: false
  policy: POL-PER-UPDATE-DETAILS
  actors: Administrator (in scope)
  payload: names:array contact:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PER-DEACTIVATE
  aggregate: AGG-PERSON
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: INACTIVE
    guard: —
    event: EVT-PER-DEACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PERSON_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/persons/{id}/actions/deactivate
  internal: false
  policy: POL-PER-DEACTIVATE
  actors: Administrator (in scope)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PER-REACTIVATE
  aggregate: AGG-PERSON
  bc: BC01
  transitions:
  - from:
    - INACTIVE
    to: ACTIVE
    guard: —
    event: EVT-PER-REACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PERSON_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/persons/{id}/actions/reactivate
  internal: false
  policy: POL-PER-REACTIVATE
  actors: Administrator (in scope)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PER-ERASE
  aggregate: AGG-PERSON
  bc: BC01
  transitions:
  - from:
    - INACTIVE
    to: ERASED
    guard: erasure order recorded; no legal hold; destroys subject key (ADR-P08)
    event: EVT-PER-ERASED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LEGAL_HOLD_ACTIVE
  - PERSON_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/persons/{id}/actions/erase
  internal: false
  policy: POL-PER-ERASE
  actors: Administrator (in scope)
  payload: erasure_order_ref!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-USR-PROVISION
  aggregate: AGG-USER
  bc: BC01
  transitions:
  - from:
    - ∅
    to: PENDING
    guard: tenant ACTIVE; via SCIM or admin
    event: EVT-USR-PROVISIONED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - TENANT_NOT_ACTIVE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/users
  internal: false
  policy: POL-USR-PROVISION
  actors: Administrator in scope / SCIM service account / Security Officer (lock)
  payload: username!:string person:urn source!:enum(scim,admin)
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-USR-LINK-IDENTITY
  aggregate: AGG-USER
  bc: BC01
  transitions:
  - from: &id001
    - PENDING
    - ACTIVE
    - LOCKED
    - DISABLED
    to: '='
    guard: (issuer, subject) unique in tenant; issuer is a configured IdP
    event: EVT-USR-IDENTITY-LINKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - IDENTITY_ALREADY_LINKED
  - USER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/users/{id}/actions/link-identity
  internal: false
  policy: POL-USR-LINK-IDENTITY
  actors: Administrator in scope / SCIM service account / Security Officer (lock)
  payload: issuer!:string subject!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-USR-UNLINK-IDENTITY
  aggregate: AGG-USER
  bc: BC01
  transitions:
  - from: *id001
    to: '='
    guard: if ACTIVE, at least one identity remains
    event: EVT-USR-IDENTITY-UNLINKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LAST_IDENTITY
  - USER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/users/{id}/actions/unlink-identity
  internal: false
  policy: POL-USR-UNLINK-IDENTITY
  actors: Administrator in scope / SCIM service account / Security Officer (lock)
  payload: issuer!:string subject!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-USR-LINK-PERSON
  aggregate: AGG-USER
  bc: BC01
  transitions:
  - from: *id001
    to: '='
    guard: person ACTIVE, not linked to another user
    event: EVT-USR-PERSON-LINKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PERSON_ALREADY_LINKED
  - USER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/users/{id}/actions/link-person
  internal: false
  policy: POL-USR-LINK-PERSON
  actors: Administrator in scope / SCIM service account / Security Officer (lock)
  payload: person!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-USR-RECORD-FIRST-SIGN-IN
  aggregate: AGG-USER
  bc: BC01
  transitions:
  - from:
    - PENDING
    to: ACTIVE
    guard: system; ≥ 1 identity; tenant ACTIVE
    event: EVT-USR-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - USER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/users/{id}/actions/record-first-sign-in
  internal: true
  policy: POL-USR-RECORD-FIRST-SIGN-IN
  actors: system (workload identity)
  payload: issuer!:string subject!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-USR-LOCK
  aggregate: AGG-USER
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: LOCKED
    guard: security officer or system anomaly rule; reason
    event: EVT-USR-LOCKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - USER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/users/{id}/actions/lock
  internal: false
  policy: POL-USR-LOCK
  actors: Administrator in scope / SCIM service account / Security Officer (lock)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-USR-UNLOCK
  aggregate: AGG-USER
  bc: BC01
  transitions:
  - from:
    - LOCKED
    to: ACTIVE
    guard: security officer
    event: EVT-USR-UNLOCKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - USER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/users/{id}/actions/unlock
  internal: false
  policy: POL-USR-UNLOCK
  actors: Administrator in scope / SCIM service account / Security Officer (lock)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-USR-DISABLE
  aggregate: AGG-USER
  bc: BC01
  transitions:
  - from:
    - PENDING
    - ACTIVE
    - LOCKED
    to: DISABLED
    guard: SCIM deactivate or administrator
    event: EVT-USR-DISABLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - USER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/users/{id}/actions/disable
  internal: false
  policy: POL-USR-DISABLE
  actors: Administrator in scope / SCIM service account / Security Officer (lock)
  payload: reason:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-USR-ENABLE
  aggregate: AGG-USER
  bc: BC01
  transitions:
  - from:
    - DISABLED
    to: ACTIVE
    guard: ≥ 1 identity; tenant ACTIVE
    event: EVT-USR-ENABLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - LAST_IDENTITY
  - USER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/users/{id}/actions/enable
  internal: false
  policy: POL-USR-ENABLE
  actors: Administrator in scope / SCIM service account / Security Officer (lock)
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-USR-CLOSE
  aggregate: AGG-USER
  bc: BC01
  transitions:
  - from:
    - DISABLED
    to: CLOSED
    guard: administrator; audit history retained
    event: EVT-USR-CLOSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - USER_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/users/{id}/actions/close
  internal: false
  policy: POL-USR-CLOSE
  actors: Administrator in scope / SCIM service account / Security Officer (lock)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SVC-CREATE
  aggregate: AGG-SERVICE-ACCOUNT
  bc: BC01
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: owner user ACTIVE; purpose stated
    event: EVT-SVC-CREATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OWNER_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/service-accounts
  internal: false
  policy: POL-SVC-CREATE
  actors: Administrator
  payload: name!:string owner!:urn purpose!:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-SVC-ROTATE-CREDENTIAL
  aggregate: AGG-SERVICE-ACCOUNT
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: new credential expiry ≤ 90 days
    event: EVT-SVC-CREDENTIAL-ROTATED
  errors:
  - AUTHZ_DENIED
  - CREDENTIAL_LIFETIME_EXCEEDED
  - IDEMPOTENCY_KEY_REUSED
  - SERVICE_ACCOUNT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/service-accounts/{id}/actions/rotate-credential
  internal: false
  policy: POL-SVC-ROTATE-CREDENTIAL
  actors: Administrator
  payload: public_key!:string expires_at!:date-time
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SVC-DISABLE
  aggregate: AGG-SERVICE-ACCOUNT
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: DISABLED
    guard: —
    event: EVT-SVC-DISABLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SERVICE_ACCOUNT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/service-accounts/{id}/actions/disable
  internal: false
  policy: POL-SVC-DISABLE
  actors: Administrator
  payload: reason:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SVC-ENABLE
  aggregate: AGG-SERVICE-ACCOUNT
  bc: BC01
  transitions:
  - from:
    - DISABLED
    to: ACTIVE
    guard: owner still ACTIVE
    event: EVT-SVC-ENABLED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OWNER_REQUIRED
  - SERVICE_ACCOUNT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/service-accounts/{id}/actions/enable
  internal: false
  policy: POL-SVC-ENABLE
  actors: Administrator
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SVC-CLOSE
  aggregate: AGG-SERVICE-ACCOUNT
  bc: BC01
  transitions:
  - from:
    - DISABLED
    to: CLOSED
    guard: —
    event: EVT-SVC-CLOSED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SERVICE_ACCOUNT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/service-accounts/{id}/actions/close
  internal: false
  policy: POL-SVC-CLOSE
  actors: Administrator
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ROL-DEFINE
  aggregate: AGG-ROLE
  bc: BC01
  transitions:
  - from:
    - ∅
    to: DRAFT
    guard: code unique in tenant
    event: EVT-ROL-DEFINED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ROLE_CODE_TAKEN
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/roles
  internal: false
  policy: POL-ROL-DEFINE
  actors: Administrator
  payload: code!:string name!:LocalizedName
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-ROL-SET-PERMISSIONS
  aggregate: AGG-ROLE
  bc: BC01
  transitions:
  - from:
    - DRAFT
    - ACTIVE
    to: '='
    guard: permissions exist in catalog; system roles are locked; ACTIVE → new version
    event: EVT-ROL-PERMISSIONS-CHANGED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ROLE_INVALID_STATE_TRANSITION
  - SYSTEM_ROLE_LOCKED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/roles/{id}/actions/set-permissions
  internal: false
  policy: POL-ROL-SET-PERMISSIONS
  actors: Administrator
  payload: permissions!:array
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ROL-ACTIVATE
  aggregate: AGG-ROLE
  bc: BC01
  transitions:
  - from:
    - DRAFT
    to: ACTIVE
    guard: ≥ 1 permission
    event: EVT-ROL-ACTIVATED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ROLE_EMPTY
  - ROLE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/roles/{id}/actions/activate
  internal: false
  policy: POL-ROL-ACTIVATE
  actors: Administrator
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-ROL-RETIRE
  aggregate: AGG-ROLE
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: RETIRED
    guard: not a system role; no active assignments
    event: EVT-ROL-RETIRED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - ROLE_INVALID_STATE_TRANSITION
  - ROLE_IN_USE
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/roles/{id}/actions/retire
  internal: false
  policy: POL-ROL-RETIRE
  actors: Administrator
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-RAS-ASSIGN
  aggregate: AGG-ROLE-ASSIGNMENT
  bc: BC01
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: role ACTIVE; user not CLOSED; scope unit ACTIVE; assigner administers the
      scope; no SoD-incompatible active role
    event: EVT-RAS-ASSIGNED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - SOD_ROLE_CONFLICT
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/role-assignments
  internal: false
  policy: POL-RAS-ASSIGN
  actors: Administrator (in scope, not self)
  payload: user!:urn role!:urn org_scope!:urn include_descendants!:boolean valid_from!:date-time
    valid_to:date-time
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-RAS-REVOKE
  aggregate: AGG-ROLE-ASSIGNMENT
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: REVOKED
    guard: assigner administers the scope; reason
    event: EVT-RAS-REVOKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/role-assignments/{id}/actions/revoke
  internal: false
  policy: POL-RAS-REVOKE
  actors: Administrator (in scope, not self)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AUT-GRANT
  aggregate: AGG-AUTHORITY-GRANT
  bc: BC01
  transitions:
  - from:
    - ∅
    to: PENDING_APPROVAL
    guard: actor has authority.grant permission; decision type exists; scope unit
      ACTIVE
    event: EVT-AUT-GRANT-REQUESTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PERMISSION_DENIED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/authority-grants
  internal: false
  policy: POL-AUT-GRANT
  actors: holder of authority.grant; Executive approves
  payload: holder!:urn decision_types!:array org_scope!:urn include_descendants!:boolean
    limits:object valid_from!:date-time valid_to:date-time delegable!:boolean
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-AUT-APPROVE-GRANT
  aggregate: AGG-AUTHORITY-GRANT
  bc: BC01
  transitions:
  - from:
    - PENDING_APPROVAL
    to: ACTIVE
    guard: approver is Executive in scope; approver ≠ requester
    event: EVT-AUT-GRANTED
  errors:
  - AUTHORITY_GRANT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/authority-grants/{id}/actions/approve-grant
  internal: false
  policy: POL-AUT-APPROVE-GRANT
  actors: holder of authority.grant; Executive approves
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AUT-REJECT-GRANT
  aggregate: AGG-AUTHORITY-GRANT
  bc: BC01
  transitions:
  - from:
    - PENDING_APPROVAL
    to: REJECTED
    guard: reason
    event: EVT-AUT-GRANT-REJECTED
  errors:
  - AUTHORITY_GRANT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/authority-grants/{id}/actions/reject-grant
  internal: false
  policy: POL-AUT-REJECT-GRANT
  actors: holder of authority.grant; Executive approves
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AUT-DELEGATE
  aggregate: AGG-AUTHORITY-GRANT
  bc: BC01
  transitions:
  - from:
    - ∅
    to: ACTIVE
    guard: parent grant effective and delegable; scope ⊆ parent; limits ≤ parent;
      period ⊆ parent; depth ≤ 2; delegate ≠ delegator
    event: EVT-AUT-DELEGATED
  errors:
  - AUTHORITY_EXCEEDS_DELEGATOR
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/authority-grants/{id}/actions/delegate
  internal: false
  policy: POL-AUT-DELEGATE
  actors: holder of authority.grant; Executive approves
  payload: delegate!:urn decision_types!:array org_scope!:urn include_descendants!:boolean
    limits:object valid_from!:date-time valid_to!:date-time delegable!:boolean
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-AUT-SUSPEND
  aggregate: AGG-AUTHORITY-GRANT
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: SUSPENDED
    guard: reason
    event: EVT-AUT-SUSPENDED
  errors:
  - AUTHORITY_GRANT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/authority-grants/{id}/actions/suspend
  internal: false
  policy: POL-AUT-SUSPEND
  actors: holder of authority.grant; Executive approves
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AUT-RESUME
  aggregate: AGG-AUTHORITY-GRANT
  bc: BC01
  transitions:
  - from:
    - SUSPENDED
    to: ACTIVE
    guard: period not ended
    event: EVT-AUT-RESUMED
  errors:
  - AUTHORITY_GRANT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - GRANT_EXPIRED
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/authority-grants/{id}/actions/resume
  internal: false
  policy: POL-AUT-RESUME
  actors: holder of authority.grant; Executive approves
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-AUT-REVOKE
  aggregate: AGG-AUTHORITY-GRANT
  bc: BC01
  transitions:
  - from:
    - PENDING_APPROVAL
    - ACTIVE
    - SUSPENDED
    to: REVOKED
    guard: granter, delegator or Executive in scope; reason
    event: EVT-AUT-REVOKED
  errors:
  - AUTHORITY_GRANT_INVALID_STATE_TRANSITION
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/authority-grants/{id}/actions/revoke
  internal: false
  policy: POL-AUT-REVOKE
  actors: holder of authority.grant; Executive approves
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLR-GRANT
  aggregate: AGG-CLEARANCE
  bc: BC01
  transitions:
  - from:
    - ∅
    to: PENDING_APPROVAL
    guard: Security Officer; level and compartments exist in ACTIVE scheme; subject
      has no other non-terminal clearance
    event: EVT-CLR-REQUESTED
  errors:
  - AUTHZ_DENIED
  - CLEARANCE_EXISTS
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/foundation/clearances
  internal: false
  policy: POL-CLR-GRANT
  actors: Security Officer
  payload: user!:urn level!:string compartments!:array caveat_attributes:object valid_to:date-time
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-CLR-APPROVE
  aggregate: AGG-CLEARANCE
  bc: BC01
  transitions:
  - from:
    - PENDING_APPROVAL
    to: ACTIVE
    guard: second Security Officer ≠ requester when level is top rank; else requester
      may self-confirm
    event: EVT-CLR-GRANTED
  errors:
  - AUTHZ_DENIED
  - CLEARANCE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - SEGREGATION_OF_DUTIES
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/clearances/{id}/actions/approve
  internal: false
  policy: POL-CLR-APPROVE
  actors: Security Officer
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLR-MODIFY
  aggregate: AGG-CLEARANCE
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: '='
    guard: same rules as grant; creates new version
    event: EVT-CLR-MODIFIED
  errors:
  - AUTHZ_DENIED
  - CLEARANCE_INVALID
  - CLEARANCE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/clearances/{id}/actions/modify
  internal: false
  policy: POL-CLR-MODIFY
  actors: Security Officer
  payload: level!:string compartments!:array caveat_attributes:object
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLR-SUSPEND
  aggregate: AGG-CLEARANCE
  bc: BC01
  transitions:
  - from:
    - ACTIVE
    to: SUSPENDED
    guard: reason
    event: EVT-CLR-SUSPENDED
  errors:
  - AUTHZ_DENIED
  - CLEARANCE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/clearances/{id}/actions/suspend
  internal: false
  policy: POL-CLR-SUSPEND
  actors: Security Officer
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLR-REINSTATE
  aggregate: AGG-CLEARANCE
  bc: BC01
  transitions:
  - from:
    - SUSPENDED
    to: ACTIVE
    guard: period not ended
    event: EVT-CLR-REINSTATED
  errors:
  - AUTHZ_DENIED
  - CLEARANCE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/clearances/{id}/actions/reinstate
  internal: false
  policy: POL-CLR-REINSTATE
  actors: Security Officer
  payload: ''
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-CLR-REVOKE
  aggregate: AGG-CLEARANCE
  bc: BC01
  transitions:
  - from:
    - PENDING_APPROVAL
    - ACTIVE
    - SUSPENDED
    to: REVOKED
    guard: reason
    event: EVT-CLR-REVOKED
  errors:
  - AUTHZ_DENIED
  - CLEARANCE_INVALID_STATE_TRANSITION
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/foundation/clearances/{id}/actions/revoke
  internal: false
  policy: POL-CLR-REVOKE
  actors: Security Officer
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
