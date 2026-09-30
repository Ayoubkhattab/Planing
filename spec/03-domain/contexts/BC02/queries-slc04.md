---
id: QRY-CAT-BC02-SLC04
type: query-catalog
title: Queries — BC02 (SLC-04)
wave: W4
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC02 (SLC-04)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-CNF-LIST | `GET /api/v1/information/conflicts` | Conflicts by subject, predicate, state, assignee | Analyst; only conflicts with ≥ 2 visible member claims | REQ-INF-025 |
| QRY-CNF-GET | `GET /api/v1/information/conflicts/{conflict_id}` | Conflict with visible members, evidence, resolution history (as known_at) | Analyst; visibility rule INV-CNF-04 | REQ-INF-025 |
| QRY-ER-QUEUE | `GET /api/v1/information/er-cases` | Review queue by state, entity type, score, ruleset | Analyst; cases where both entities are visible | REQ-INF-032 |
| QRY-ER-GET | `GET /api/v1/information/er-cases/{case_id}` | Case with side-by-side feature comparison (visible claims only) | Analyst; both entities visible | REQ-INF-032 |
| QRY-CLUSTER-GET | `GET /api/v1/information/entities/{entity_id}/identity-cluster` | Cluster members, canonical URN, links, as known_at | Analyst; invisible members omitted | REQ-INF-033 |
| QRY-MRS-GET | `GET /api/v1/information/match-rulesets/{ruleset_id}` | Ruleset with evaluation report | Analyst lead, Administrator | REQ-INF-032 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
