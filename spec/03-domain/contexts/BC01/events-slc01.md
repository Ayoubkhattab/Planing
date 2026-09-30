---
id: EVT-CAT-BC01-SLC01
type: event-catalog
title: Domain Events — BC01 (SLC-01)
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC01 (SLC-01)

_61 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-TEN-PROVISIONING-STARTED | AGG-TENANT | CMD-TEN-PROVISION, CMD-TEN-RETRY-PROVISIONING | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller | tenant_id + aggregate.id |
| EVT-TEN-ACTIVATED | AGG-TENANT | CMD-TEN-COMPLETE-PROVISIONING | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller | tenant_id + aggregate.id |
| EVT-TEN-PROVISIONING-FAILED | AGG-TENANT | CMD-TEN-FAIL-PROVISIONING | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller | tenant_id + aggregate.id |
| EVT-TEN-SUSPENDED | AGG-TENANT | CMD-TEN-SUSPEND | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Provisioning saga / cell controller | tenant_id + aggregate.id |
| EVT-TEN-REACTIVATED | AGG-TENANT | CMD-TEN-REACTIVATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Provisioning saga / cell controller | tenant_id + aggregate.id |
| EVT-TEN-MIGRATION-STARTED | AGG-TENANT | CMD-TEN-START-CELL-MIGRATION | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller | tenant_id + aggregate.id |
| EVT-TEN-MIGRATED | AGG-TENANT | CMD-TEN-COMPLETE-CELL-MIGRATION | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller | tenant_id + aggregate.id |
| EVT-TEN-DECOMMISSION-STARTED | AGG-TENANT | CMD-TEN-START-DECOMMISSION | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller | tenant_id + aggregate.id |
| EVT-TEN-DECOMMISSIONED | AGG-TENANT | CMD-TEN-COMPLETE-DECOMMISSION | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller | tenant_id + aggregate.id |
| EVT-TEN-QUOTAS-UPDATED | AGG-TENANT | CMD-TEN-UPDATE-QUOTAS | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller | tenant_id + aggregate.id |
| EVT-ORG-CREATED | AGG-ORGANIZATION | CMD-ORG-CREATE | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models | tenant_id + aggregate.id |
| EVT-ORG-RENAMED | AGG-ORGANIZATION | CMD-ORG-RENAME | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models | tenant_id + aggregate.id |
| EVT-ORG-UNIT-ADDED | AGG-ORGANIZATION | CMD-ORG-ADD-UNIT | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models | tenant_id + aggregate.id |
| EVT-ORG-UNIT-RENAMED | AGG-ORGANIZATION | CMD-ORG-RENAME-UNIT | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models | tenant_id + aggregate.id |
| EVT-ORG-UNIT-MOVED | AGG-ORGANIZATION | CMD-ORG-MOVE-UNIT | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); All contexts' org-scope read models | tenant_id + aggregate.id |
| EVT-ORG-UNIT-DEACTIVATED | AGG-ORGANIZATION | CMD-ORG-DEACTIVATE-UNIT | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); All contexts' org-scope read models | tenant_id + aggregate.id |
| EVT-ORG-DEACTIVATED | AGG-ORGANIZATION | CMD-ORG-DEACTIVATE | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models | tenant_id + aggregate.id |
| EVT-ORG-REACTIVATED | AGG-ORGANIZATION | CMD-ORG-REACTIVATE | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models | tenant_id + aggregate.id |
| EVT-PER-REGISTERED | AGG-PERSON | CMD-PER-REGISTER | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-PER-DETAILS-UPDATED | AGG-PERSON | CMD-PER-UPDATE-DETAILS | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-PER-DEACTIVATED | AGG-PERSON | CMD-PER-DEACTIVATE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-PER-REACTIVATED | AGG-PERSON | CMD-PER-REACTIVATE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-PER-ERASED | AGG-PERSON | CMD-PER-ERASE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-USR-PROVISIONED | AGG-USER | CMD-USR-PROVISION | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-USR-IDENTITY-LINKED | AGG-USER | CMD-USR-LINK-IDENTITY | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-USR-IDENTITY-UNLINKED | AGG-USER | CMD-USR-UNLINK-IDENTITY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-USR-PERSON-LINKED | AGG-USER | CMD-USR-LINK-PERSON | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-USR-ACTIVATED | AGG-USER | CMD-USR-RECORD-FIRST-SIGN-IN | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-USR-LOCKED | AGG-USER | CMD-USR-LOCK | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-USR-UNLOCKED | AGG-USER | CMD-USR-UNLOCK | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-USR-DISABLED | AGG-USER | CMD-USR-DISABLE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-USR-ENABLED | AGG-USER | CMD-USR-ENABLE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-USR-CLOSED | AGG-USER | CMD-USR-CLOSE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-SVC-CREATED | AGG-SERVICE-ACCOUNT | CMD-SVC-CREATE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-SVC-CREDENTIAL-ROTATED | AGG-SERVICE-ACCOUNT | CMD-SVC-ROTATE-CREDENTIAL | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-SVC-DISABLED | AGG-SERVICE-ACCOUNT | CMD-SVC-DISABLE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-SVC-ENABLED | AGG-SERVICE-ACCOUNT | CMD-SVC-ENABLE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-SVC-CLOSED | AGG-SERVICE-ACCOUNT | CMD-SVC-CLOSE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-ROL-DEFINED | AGG-ROLE | CMD-ROL-DEFINE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-ROL-PERMISSIONS-CHANGED | AGG-ROLE | CMD-ROL-SET-PERMISSIONS | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-ROL-ACTIVATED | AGG-ROLE | CMD-ROL-ACTIVATE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-ROL-RETIRED | AGG-ROLE | CMD-ROL-RETIRE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-RAS-ASSIGNED | AGG-ROLE-ASSIGNMENT | CMD-RAS-ASSIGN | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-RAS-REVOKED | AGG-ROLE-ASSIGNMENT | CMD-RAS-REVOKE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-RAS-EXPIRED | AGG-ROLE-ASSIGNMENT | SYS:valid_to reached | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-AUT-GRANT-REQUESTED | AGG-AUTHORITY-GRANT | CMD-AUT-GRANT | — | Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) | tenant_id + aggregate.id |
| EVT-AUT-GRANTED | AGG-AUTHORITY-GRANT | CMD-AUT-APPROVE-GRANT | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) | tenant_id + aggregate.id |
| EVT-AUT-GRANT-REJECTED | AGG-AUTHORITY-GRANT | CMD-AUT-REJECT-GRANT | — | Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) | tenant_id + aggregate.id |
| EVT-AUT-DELEGATED | AGG-AUTHORITY-GRANT | CMD-AUT-DELEGATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) | tenant_id + aggregate.id |
| EVT-AUT-SUSPENDED | AGG-AUTHORITY-GRANT | CMD-AUT-SUSPEND | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) | tenant_id + aggregate.id |
| EVT-AUT-RESUMED | AGG-AUTHORITY-GRANT | CMD-AUT-RESUME | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) | tenant_id + aggregate.id |
| EVT-AUT-REVOKED | AGG-AUTHORITY-GRANT | CMD-AUT-REVOKE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) | tenant_id + aggregate.id |
| EVT-AUT-EXPIRED | AGG-AUTHORITY-GRANT | SYS:valid_to reached | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) | tenant_id + aggregate.id |
| EVT-CLR-REQUESTED | AGG-CLEARANCE | CMD-CLR-GRANT | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-CLR-GRANTED | AGG-CLEARANCE | CMD-CLR-APPROVE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-CLR-MODIFIED | AGG-CLEARANCE | CMD-CLR-MODIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-CLR-SUSPENDED | AGG-CLEARANCE | CMD-CLR-SUSPEND | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-CLR-REINSTATED | AGG-CLEARANCE | CMD-CLR-REINSTATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-CLR-REVOKED | AGG-CLEARANCE | CMD-CLR-REVOKE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-CLR-EXPIRED | AGG-CLEARANCE | SYS:valid_to reached | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-SEC-VERSION-INCREMENTED | (derived) SecurityVersion | security-version service on any security-affecting event | نعم | All PEPs; Projection security-version tables; SecurityContext cache | tenant_id + subject_urn |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
