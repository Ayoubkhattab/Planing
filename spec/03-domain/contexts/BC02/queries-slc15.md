---
id: QRY-CAT-BC02-SLC15
type: query-catalog
title: Queries — BC02 (SLC-15)
wave: W4
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC02 (SLC-15)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-CRP-QUEUE | `GET /api/v1/information/correlation-proposals` | Proposals by kind, state, area, score (inputs all visible to caller) | Analyst | REQ-FUS-001 |
| QRY-CRP-GET | `GET /api/v1/information/correlation-proposals/{proposal_id}` | Proposal with inputs, sources, reliabilities, score breakdown | reviewer cleared for all inputs | REQ-FUS-002 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
