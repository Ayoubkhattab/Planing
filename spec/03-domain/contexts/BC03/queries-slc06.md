---
id: QRY-CAT-BC03-SLC06
type: query-catalog
title: Queries — BC03 (SLC-06)
wave: W4
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC03 (SLC-06)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-SIT-LIST | `GET /api/v1/intelligence/situations` | Situations by state, owner, extent intersecting bbox | any user; situation label rule | REQ-SIT-001 |
| QRY-SIT-GET | `GET /api/v1/intelligence/situations/{situation_id}` | Definition (version at valid_at), counts of visible members by type | cleared for situation label | REQ-SIT-001 |
| QRY-SIT-COP | `GET /api/v1/intelligence/situations/{situation_id}/picture` | Common operational picture: visible members (entities, events, observations, tasks, assessments, alerts) with resolved, possibly generalized geometry | cleared for situation; per-member filtering | REQ-SIT-003 |
| QRY-SIT-CHANGES | `GET /api/v1/intelligence/situations/{situation_id}/changes` | Membership change log (visible members only) since cursor/time | cleared for situation; per-member filtering | REQ-SIT-002 |
| QRY-SIT-TILE | `GET /api/v1/intelligence/situations/{situation_id}/tiles/{layer}/{z}/{x}/{y}` | Vector tile of operational layer for the caller's security scope | cleared for situation; scope-keyed cache (ADR-P06 §6) | REQ-SIT-007 |
| QRY-BASE-TILE | `GET /api/v1/intelligence/base-maps/{layer}/{z}/{x}/{y}` | Base-map tile (layers marked unclassified only; shared cache) | any user of tenant | REQ-SIT-007 |
| QRY-ALR-LIST | `GET /api/v1/intelligence/alerts` | My alerts by state, severity, situation | recipient; label rule | REQ-SIT-005 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
