---
id: QRY-CAT-BC07-SLC10
type: query-catalog
title: Queries — BC07 (SLC-10)
wave: W4
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC07 (SLC-10)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-AIR-GET | `GET /api/v1/ai/requests/{request_id}` | Request with answer, statements and citations (visible only), status | requester; Auditor (metadata) | REQ-AI-001 |
| QRY-AIR-CONTEXT | `GET /api/v1/ai/requests/{request_id}/context` | Context package items (URN, version, label) — for audit and review | requester if cleared; Auditor | REQ-AI-002 |
| QRY-AIRS-QUEUE | `GET /api/v1/ai/results` | Reviewable AI results by state, operation, target | reviewers authorized on targets | REQ-AI-005 |
| QRY-MDL-LIST | `GET /api/v1/ai/models` | Model versions with state, evaluation summary, hosting | AI governance, Auditor | REQ-AI-009 |
| QRY-RTG-ACTIVE | `GET /api/v1/ai/routing` | Active routing for the tenant | AI governance, Security Officer | REQ-AI-008 |
| QRY-TOL-LIST | `GET /api/v1/ai/tools` | Tool registry | AI governance, Security Officer | REQ-AI-013 |
| QRY-AI-USAGE | `GET /api/v1/ai/usage` | GPU-hours, requests, cost indicators per tenant and operation | Administrator, finance | REQ-AI-001 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
