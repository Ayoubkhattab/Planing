---
id: QRY-CAT-BC02-SLC02
type: query-catalog
title: Queries — BC02 (SLC-02)
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC02 (SLC-02)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-ENT-RESOLVED | `GET /api/v1/information/entities/{entity_id}` | Resolved view per predicate at valid_at/known_at (value, CORROBORATED/DISPUTED candidates, confidence); resolves through the identity cluster and returns canonical_urn + requested_urn (SLC-04) | any user; claims label-filtered (INV-ENT-02) | REQ-INF-023 |
| QRY-ENT-CLAIMS | `GET /api/v1/information/entities/{entity_id}/claims` | Claim history (predicate, valid_at, known_at, include_closed) | any user; label-filtered | REQ-INF-022 |
| QRY-ENT-LIST | `GET /api/v1/information/entities` | Entities by type, bbox/polygon of current location, valid_at | any user; allowed_scope pre-filter | REQ-INF-020 |
| QRY-ENT-POSITIONS | `GET /api/v1/information/entities/{entity_id}/positions` | Position history in [from,to) as known_at | any user; label-filtered; geometry generalized by obligation | REQ-INF-030 |
| QRY-RWE-GET | `GET /api/v1/information/events/{event_id}` | Resolved real-world event | any user; label-filtered | REQ-INF-020 |
| QRY-REL-LIST | `GET /api/v1/information/entities/{entity_id}/relationships` | Relationships valid_at/known_at, both directions | any user; hidden relationships and endpoints omitted | REQ-INF-027 |
| QRY-CLM-GET | `GET /api/v1/information/claims/{claim_id}` | Claim with sources (per protection), evidence links, supersession chain | any user; label-filtered | REQ-INF-021 |
| QRY-OBS-LIST | `GET /api/v1/information/observations` | Observations by bbox, time window (mandatory, ≤ 31 days), source, state | any user; allowed_scope pre-filter | REQ-INF-002 |
| QRY-OBS-GET | `GET /api/v1/information/observations/{observation_id}` | Observation with measurements and attachment refs | any user; label-filtered | REQ-INF-002 |
| QRY-SRC-GET | `GET /api/v1/information/sources/{source_id}` | Source; identity only with source-protection permission | Analyst and above; protection policy | REQ-INF-001 |
| QRY-EVD-GET | `GET /api/v1/information/evidence/{evidence_id}` | Evidence metadata and custody chain | any user; label-filtered | REQ-INF-004 |
| QRY-ATT-DOWNLOAD | `POST /api/v1/information/attachments/{attachment_id}/download-grants` | Short-lived signed download target (≤ 5 min); audited | authorized on the owning evidence/observation | REQ-INF-004 |
| QRY-LIN-TRACE | `GET /api/v1/information/lineage/{object_urn}` | Upstream/downstream lineage, depth ≤ 10; hidden nodes cut per policy | any user; per-node authorization | REQ-INF-035 |
| QRY-EXT-RESOLVE | `GET /api/v1/information/external-ids/{system}/{external_id}` | Object URN mapped at time t (not-found shape if hidden) | adapter service accounts; Analyst | REQ-INF-036 |
| QRY-IMP-GET | `GET /api/v1/information/import-batches/{batch_id}` | Batch status, counts, quarantine records (paged) | adapter owner; Administrator | REQ-INF-006 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
