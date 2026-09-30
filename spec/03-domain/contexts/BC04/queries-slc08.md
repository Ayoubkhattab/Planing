---
id: QRY-CAT-BC04-SLC08
type: query-catalog
title: Queries — BC04 (SLC-08)
wave: W4
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC04 (SLC-08)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-DRQ-GET | `GET /api/v1/operations/decision-requests/{request_id}` | Request with options and pinned citations (withheld per policy) | label rule; required-authority holders in scope | REQ-DEC-001 |
| QRY-DRQ-LIST | `GET /api/v1/operations/decision-requests` | My pending requests (as authority holder), by deadline | allowed_scope | REQ-DEC-001 |
| QRY-DEC-GET | `GET /api/v1/operations/decisions/{decision_id}` | Decision with authority snapshot, citations (pinned) and supersession chain | label rule | REQ-DEC-003 |
| QRY-DEC-BASIS | `GET /api/v1/operations/decisions/{decision_id}/basis` | What was known at decision time: cited assessments (pinned versions) and their key claims resolved known_at = decision.recorded_at | label rule; Auditor | REQ-DEC-003 |
| QRY-PLN-GET | `GET /api/v1/operations/plans/{plan_id}` | Plan with current baseline, draft (if any), implemented decisions | label rule | REQ-OPS-001 |
| QRY-PLV-LIST | `GET /api/v1/operations/plans/{plan_id}/versions` | Versions with states and times | label rule | REQ-OPS-003 |
| QRY-PLV-DIFF | `GET /api/v1/operations/plans/{plan_id}/versions/{version}/diff` | Diff vs baseline with major/minor classification and task synchronization preview | label rule | REQ-OPS-004 |
| QRY-PLN-PROGRESS | `GET /api/v1/operations/plans/{plan_id}/progress` | Tasks by activity and state, milestones, outcome progress vs targets | label rule; visible tasks only | REQ-OPS-013 |
| QRY-OUT-SERIES | `GET /api/v1/operations/plans/{plan_id}/outcomes/{outcome_id}/measurements` | Measurement series as known_at | label rule | REQ-OPS-013 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
