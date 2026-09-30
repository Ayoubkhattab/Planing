---
id: QRY-CAT-BC05-SLC19
type: query-catalog
title: Queries — BC05 (SLC-19)
wave: W4
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
---


# Queries — BC05 (SLC-19)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-SCN-GET | `GET /api/v1/readiness/scenarios/{scenario_id}` | Scenario with injects and target competencies | allowed_scope | REQ-TRX-014 |
| QRY-SCN-LIST | `GET /api/v1/readiness/scenarios` | Scenarios filtered by exercise type, state | allowed_scope | REQ-TRX-014 |
| QRY-EXR-GET | `GET /api/v1/readiness/exercises/{exercise_id}` | Exercise with frozen scenario reference, participants, current state | allowed_scope | REQ-TRX-014 |
| QRY-EXR-LIST | `GET /api/v1/readiness/exercises` | Exercises filtered by scenario, state, window | allowed_scope | REQ-TRX-014 |
| QRY-SIM-GET | `GET /api/v1/readiness/simulations/{simulation_id}` | Simulation with current state and evaluation summary | allowed_scope | REQ-TRX-014 |
| QRY-SIM-LIST | `GET /api/v1/readiness/simulations` | Simulations filtered by exercise, state, window | allowed_scope | REQ-TRX-014 |
| QRY-SIM-TIMELINE | `GET /api/v1/readiness/simulations/{simulation_id}/timeline` | Full, ordered timeline of inject deliveries and evaluations for a simulation | allowed_scope | REQ-TRX-015 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
