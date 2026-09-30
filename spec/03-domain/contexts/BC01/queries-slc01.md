---
id: QRY-CAT-BC01-SLC01
type: query-catalog
title: Queries — BC01 (SLC-01)
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC01 (SLC-01)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-TEN-GET | `GET /api/v1/foundation/tenants/{tenant_id}` | Tenant state, cell, quotas | platform operator or tenant Administrator of that tenant | REQ-FND-001 |
| QRY-ORG-TREE | `GET /api/v1/foundation/organizations/{org_id}/units` | Unit tree (cursor pagination on flattened order) | any user of tenant (view org structure) | REQ-FND-002 |
| QRY-USR-LIST | `GET /api/v1/foundation/users` | Users filtered by state, unit, role | Administrator in scope | REQ-FND-006 |
| QRY-USR-GET | `GET /api/v1/foundation/users/{user_id}` | User with identities (no secrets) | Administrator in scope or self | REQ-FND-006 |
| QRY-SEC-CONTEXT | `GET /api/v1/foundation/me/security-context` | Caller's resolved SecurityContext | self | REQ-FND-010 |
| QRY-AUT-CHECK | `POST /api/v1/foundation/authority-checks` | AuthorityCheck(actor, decision_type, scope, at, amount?) | internal services (workload identity) or self | REQ-FND-009 |
| QRY-AUT-LIST | `GET /api/v1/foundation/authority-grants` | Grants by holder / scope / effective at t | Executive or Administrator in scope, or holder | REQ-FND-007 |
| QRY-CLR-GET | `GET /api/v1/foundation/users/{user_id}/clearance` | Current clearance (level/compartments) | Security Officer or self | REQ-GOV-003 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
