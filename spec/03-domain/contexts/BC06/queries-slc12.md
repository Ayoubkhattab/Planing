---
id: QRY-CAT-BC06-SLC12
type: query-catalog
title: Queries — BC06 (SLC-12)
wave: W4
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC06 (SLC-12)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-PRD-GET | `GET /api/v1/knowledge/products/{product_id}` | Product version with rendered artifacts (download grants) and pinned citations | audience + label rule | REQ-PRD-003 |
| QRY-PRD-LIST | `GET /api/v1/knowledge/products` | Products by kind, state, situation/case, date | allowed_scope | REQ-PRD-001 |
| QRY-DST-LOG | `GET /api/v1/knowledge/products/{product_id}/distributions` | Distribution and delivery log with watermark ids | distributor, Security Officer, Auditor | REQ-PRD-004 |
| QRY-KNO-SEARCH | `GET /api/v1/knowledge/knowledge-objects` | Published knowledge by type, text, relationships | any user; label rule | REQ-KNW-001 |
| QRY-KNO-SUGGEST | `POST /api/v1/knowledge/knowledge-suggestions` | Published knowledge relevant to a task type / plan / area (by relationships) | planner; label rule | REQ-KNW-003 |
| QRY-ARC-SEARCH | `GET /api/v1/knowledge/archive-packages` | Archive catalogue (metadata only) by class, period, org | Archivist; label rule | REQ-ARC-003 |
| QRY-ARC-RETRIEVE | `POST /api/v1/knowledge/archive-packages/{package_id}/retrievals` | Retrieve package content (warm: signed grant; cold: staged job) — access logged | authorized by package label and purpose | REQ-ARC-003 |
| QRY-REC-REPORT | `GET /api/v1/knowledge/reconstructions/{reconstruction_id}/report` | Labelled reconstruction report | requester, Auditor | REQ-ARC-004 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
