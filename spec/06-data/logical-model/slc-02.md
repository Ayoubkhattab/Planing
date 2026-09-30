---
id: LDM-SLC02
type: logical-data-model
title: Logical Data Model — SLC-02
wave: W6
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P01, ADR-P02, ADR-P03, ADR-P04, ADR-P13, ADR-P15, ADR-P16], library: LIB-CLAIMS-KERNEL}
---

# Logical Data Model — SLC-02 (schema `information`, BC02; `integration`, BC07)

القواعد العامة من LDM-SLC01 تنطبق (tenant_id أولاً، history، outbox، audit_outbox، inbox، idempotency_keys).

## BC02 — information

| الجدول | المفتاح / التقسيم | أعمدة أساسية | قيود وفهارس |
|---|---|---|---|
| sources | (tenant_id, source_id) | type, name(json), owner_org, protection_level, label(json), state, version | — |
| source_reliability | (tenant_id, source_id, valid_from, recorded_from) | rating A–F, valid_to, recorded_to, rationale, rated_by | bitemporal; no overlapping current records |
| observations | (tenant_id, observed_month, observation_id) · **partition by (tenant, month)** | source_id, observer, observed_at, event_time(json), recorded_from, geom(4326), crs_original, coords_original, accuracy_m, method, measurements(json), narrative(json), label, state, version, data_quality(json) | spatial index per partition; index (tenant, observed_at); list queries require time window ≤ 31 d |
| observation_attachments | (tenant_id, observation_id, attachment_id) | — | — |
| entities | (tenant_id, entity_id) | urn, entity_type, label, state, version | — |
| realworld_events | (tenant_id, event_id) | urn, event_type, label, state, version | — |
| relationships | (tenant_id, relationship_id) | urn, type, source_urn, target_urn, label, state, version, existence_claim_id | index (tenant, source_urn), (tenant, target_urn) |
| claims | (tenant_id, subject_hash_bucket, claim_id) · **partition by (tenant, hash(subject))** | subject_urn, predicate, value(json), value_norm (typed + normalized), unit_canonical, valid_from, valid_to, recorded_from, recorded_to, supersedes, sources[], label, security_version, derived_from[] | index (tenant, subject_urn, predicate, valid_from, valid_to, recorded_from, recorded_to); `recorded_*` writable only by kernel (FIT-05) |
| claims_current | (tenant_id, subject_urn, predicate, claim_id) | value_norm, valid_from, valid_to, label | maintained in the same transaction; = claims where recorded_to is null (P-26) |
| claim_assessments | (tenant_id, claim_id, version) | information_confidence, verification_status, rationale, assessed_by, recorded_at | versioned T2 |
| name_forms | (tenant_id, claim_id, form) | lang, original, normalized, translit_scheme, phonetic_key, normalization_version | index (tenant, normalized), (tenant, phonetic_key) |
| evidence | (tenant_id, evidence_id) | type, attachment_id?, observation_ref?, locator(json), source_id, collected_at, seal_hash, label, state, version | — |
| evidence_custody | (tenant_id, evidence_id, seq) | holder, from, to, action | gapless seq |
| evidence_links | (tenant_id, link_id) | evidence_id, claim_id, stance, recorded_from, recorded_to, label, state | partial unique (evidence, claim, stance) where state = ACTIVE |
| attachments | (tenant_id, attachment_id) | sha256, size, mime, object_key, key_ref, label, state, version | partial unique (tenant, sha256) where state non-terminal |
| import_batches | (tenant_id, batch_id) | adapter_id, batch_key, content_sha256, mapping_version, counts(json), state, lease_owner, lease_until, version | UNIQUE (tenant, adapter_id, batch_key) |
| quarantine_records | (tenant_id, batch_id, seq) | raw(json, encrypted), reason_codes[] | excluded from all queries/projections |
| external_ids | (tenant_id, mapping_id) | system, external_id, object_urn, valid_from, valid_to, state | exclusion: no overlapping ACTIVE validity for (tenant, system, external_id) |
| lineage_records | (tenant_id, lineage_id) | activity_type, activity_ref, inputs(json with versions/known_at), outputs(json), transformation{code,version}, agent, started_at, ended_at | append-only; index on inputs/outputs URNs |

## BC07 — integration
| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| adapters | (tenant_id, adapter_id) | name, source_urn, service_account_urn, state, version | one source per adapter |
| adapter_mappings | (tenant_id, adapter_id, mapping_version) | spec(json), tests(json), author, approved_by | immutable |

## أحجام تقديرية (INF، نطاق التصميم)
| الجدول | الحجم |
|---|---|
| observations | 1e9 صف؛ تقسيم شهري؛ تقادم hot/warm/cold بعد 3/12 شهراً (SR-08) |
| claims | 1e8 صف |
| claims_current | ~ 0.6 × claims |
| lineage_records | ~ عدد الكائنات المشتقة (≤ 1.2e8) |
