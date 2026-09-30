---
id: QRY-CAT-BC07-SLC05
type: query-catalog
title: Queries — BC07 (SLC-05)
wave: W4
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC07 (SLC-05)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-SRCH-QUERY | `POST /api/v1/discovery/search-queries` | Unified search: text + types + polygon/bbox + time window + filters + facets; cursor paging; results and facets over visible facts only | any user; allowed_scope pre-filter + authoritative re-check | REQ-SRC-001 |
| QRY-SRCH-SUGGEST | `GET /api/v1/discovery/suggestions` | Autocomplete from visible facts only | any user; same filter | REQ-SRC-003 |
| QRY-GRAPH-NEIGHBORHOOD | `GET /api/v1/discovery/graph/entities/{entity_id}/neighborhood` | Nodes/edges within depth ≤ 3, valid_at/known_at; hidden nodes and edges cut | any user; per-node and per-edge authorization | REQ-INF-027 |
| QRY-GRAPH-PATHS | `POST /api/v1/discovery/graph/paths` | Paths between two entities, ≤ 4 hops, only through visible nodes and edges | any user; per-node and per-edge authorization | REQ-INF-027 |
| QRY-PRJ-STATUS | `GET /api/v1/discovery/projection-versions` | Projection versions, lag, state | platform operator | REQ-SRC-004 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
