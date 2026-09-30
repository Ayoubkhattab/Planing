---
id: QRY-CAT-BC04-SLC03
type: query-catalog
title: Queries — BC04 (SLC-03)
wave: W4
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC04 (SLC-03)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-TASK-GET | `GET /api/v1/operations/tasks/{task_id}` | Task with criteria status, result, eligibility snapshot, dependencies | assignee, reviewer, Planner/Manager in scope; label rule | REQ-OPS-006 |
| QRY-TASK-LIST | `GET /api/v1/operations/tasks` | Tasks by assignee (me), plan, state, due_before, unit | allowed_scope pre-filter | REQ-OPS-006 |
| QRY-TASK-HISTORY | `GET /api/v1/operations/tasks/{task_id}/history` | State history; state as of t (RECONSTRUCTED) | same as QRY-TASK-GET | REQ-OPS-006 |
| QRY-TTY-GET | `GET /api/v1/operations/task-types/{task_type_id}` | Task type version | any user of tenant | REQ-OPS-014 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
