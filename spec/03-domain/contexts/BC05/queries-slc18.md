---
id: QRY-CAT-BC05-SLC18
type: query-catalog
title: Queries — BC05 (SLC-18)
wave: W4
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
---


# Queries — BC05 (SLC-18)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-LGR-GET | `GET /api/v1/readiness/logistics-requests/{request_id}` | Logistics request with linked allocation and shipment refs | label rule; allowed_scope | REQ-LOG-010 |
| QRY-LGR-LIST | `GET /api/v1/readiness/logistics-requests` | Logistics requests filtered by item, destination, state, priority | allowed_scope | REQ-LOG-010 |
| QRY-SHP-GET | `GET /api/v1/readiness/shipments/{shipment_id}` | Shipment with current state and delivered/damaged/lost quantity | allowed_scope | REQ-LOG-011 |
| QRY-SHP-LIST | `GET /api/v1/readiness/shipments` | Shipments filtered by logistics request, carrier, state, window | allowed_scope | REQ-LOG-011 |
| QRY-SHP-TRACKING | `GET /api/v1/readiness/shipments/{shipment_id}/checkpoints` | Full checkpoint history of a shipment, in order | allowed_scope | REQ-LOG-012 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
