---
id: LDM-SLC04
type: logical-data-model
title: Logical Data Model — SLC-04
wave: W6
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-04 (schema `information`)

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| conflicts | (tenant_id, conflict_id) | cluster_id, predicate, window_from, window_to, detected_by, label, state, version | partial unique (tenant, cluster_id, predicate, window) where state non-terminal — enforced by engine + exclusion on window overlap |
| conflict_members | (tenant_id, conflict_id, claim_id) | joined_at | — |
| conflict_resolutions | (tenant_id, conflict_id, recorded_from) | kind (RESOLVED/ACCEPTED), preferred_claim_id?, rationale, decided_by, recorded_to | bitemporal; one current per conflict |
| er_cases | (tenant_id, case_id) | left_entity, right_entity, score, ruleset_version, feature_comparison(json), proposer, agent?, decision_basis_level, state, version | partial unique (tenant, pair) where state non-terminal |
| same_as_links | (tenant_id, link_id) | left_entity, right_entity, kind (MATCH/NOT_A_MATCH), case_id, recorded_from, recorded_to, decided_by | index (tenant, left), (tenant, right) |
| identity_clusters | (tenant_id, entity_id, recorded_from) | cluster_id, canonical_entity, recorded_to | one current row per entity; recomputed in decision transaction |
| match_rulesets | (tenant_id, ruleset_id) | entity_type, version, blocking_keys(json), features(json), thresholds(json), evaluation(json), state, author, approver | one ACTIVE per (tenant, entity_type) |
| blocking_index | (tenant_id, entity_type, key_kind, key_value, entity_id) | computed_at, ruleset_version | rebuilt on ruleset activation |
