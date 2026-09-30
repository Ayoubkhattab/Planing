---
id: QRY-CAT-BC07-SLC16
type: query-catalog
title: Queries — BC07 (SLC-16)
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC07 (SLC-16)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-CON-LIST | `GET /api/v1/integration/connections` | Connections with state, health, allow-list entry | integration engineers, Security Officer | REQ-INT-001 |
| QRY-SNS-LIST | `GET /api/v1/integration/sensor-streams` | Streams with rate, staleness, quality violation counts | integration engineers, Analyst | REQ-INT-002 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
