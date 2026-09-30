---
id: QRY-CAT-BC02-SLC14
type: query-catalog
title: Queries — BC02 (SLC-14)
wave: W4
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC02 (SLC-14)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-CRQ-GET | `GET /api/v1/information/collection-requirements/{requirement_id}` | Requirement with EEIs and fulfilment computed over observations visible to the caller | requester, collection managers; label rule | REQ-COL-003 |
| QRY-CRQ-BOARD | `GET /api/v1/information/collection-requirements` | Requirements by area (bbox/polygon), state, priority, due | allowed_scope | REQ-COL-001 |
| QRY-CPL-GET | `GET /api/v1/information/collection-plans/{plan_id}` | Plan with activities and linked tasks | planner scope | REQ-COL-002 |
| QRY-CRQ-EVIDENCE | `GET /api/v1/information/collection-requirements/{requirement_id}/fulfilment` | Fulfilment links per EEI (visible observations only) with lineage | requester, collection managers | REQ-COL-003 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
