---
id: QRY-CAT-BC05-SLC09
type: query-catalog
title: Queries — BC05 (SLC-09)
wave: W4
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC05 (SLC-09)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-AST-GET | `GET /api/v1/readiness/assets/{asset_id}` | Asset with status, condition, certifications, custody chain, linked entity | label rule | REQ-RES-001 |
| QRY-AST-AVAILABILITY | `POST /api/v1/readiness/asset-availability-queries` | Assets of type/capability available in a window (and optional bbox), with blocking reasons for others visible to caller | allowed_scope | REQ-RES-003 |
| QRY-MNT-SCHEDULE | `GET /api/v1/readiness/maintenance-orders` | Maintenance orders by asset, window, state | asset owner scope | REQ-RES-004 |
| QRY-POL-TIMELINE | `GET /api/v1/readiness/resource-pools/{pool_id}/timeline` | Capacity, committed and available quantity per hour in a window | pool scope | REQ-RES-006 |
| QRY-ALC-LIST | `GET /api/v1/readiness/allocations` | Allocations by pool, task, plan, state | scope | REQ-RES-007 |
| QRY-READINESS | `POST /api/v1/readiness/readiness-checks` | Readiness of a person or unit for a role at time t, with gaps | Manager / Training Manager in scope; self | REQ-RES-013 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
