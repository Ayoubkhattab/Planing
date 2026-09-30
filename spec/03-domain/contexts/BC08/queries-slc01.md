---
id: QRY-CAT-BC08-SLC01
type: query-catalog
title: Queries — BC08 (SLC-01)
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC08 (SLC-01)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-CLS-ACTIVE | `GET /api/v1/governance/classification-scheme` | Active scheme (labels only) | any user of tenant | REQ-GOV-001 |
| QRY-POL-GET | `GET /api/v1/governance/policy-sets/{version_id}` | Policy set version with tables and tests | Security Officer, Auditor | REQ-GOV-009 |
| QRY-PDP-DECIDE | `POST /api/v1/governance/policy-decisions` | DecisionRequest → DecisionResponse (authorization-model §2) | internal PEPs only (workload identity) | REQ-FND-010 |
| QRY-AUD-SEARCH | `GET /api/v1/governance/audit-records` | Audit records by actor, resource, time, correlation id | Auditor, Security Officer (itself audited) | REQ-FND-015 |
| QRY-AUD-VERIFY | `POST /api/v1/governance/audit-integrity-checks` | Start integrity verification job; returns job ref | Auditor | REQ-FND-016 |
| QRY-EXC-LIST | `GET /api/v1/governance/security-exceptions` | Exceptions by state | Security Officer, Auditor | REQ-FND-017 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
