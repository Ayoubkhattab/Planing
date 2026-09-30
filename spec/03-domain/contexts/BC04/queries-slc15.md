---
id: QRY-CAT-BC04-SLC15
type: query-catalog
title: Queries — BC04 (SLC-15)
wave: W4
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC04 (SLC-15)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-CRD-GET | `GET /api/v1/operations/coordination-cases/{case_id}` | Case filtered to the caller's participant scope | participants (scope-limited); lead | REQ-CRD-001 |
| QRY-CRD-LIST | `GET /api/v1/operations/coordination-cases` | Cases where the caller's unit participates | allowed_scope | REQ-CRD-001 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
