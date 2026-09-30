---
id: LDM-SLC12A
type: logical-data-model
title: Logical Data Model — SLC-12a
wave: W6
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-12a (schema `governance`, BC08; key store per cell)

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| retention_schedules | (tenant_id, schedule_version) | rules(json), state, drafted_by, approved_by, effective_from, retroactive_classes[] | one ACTIVE per tenant |
| legal_holds | (tenant_id, hold_id) | name, legal_reference, scope(json), state, placed_by, release_requested_by?, released_by? | — |
| hold_index | (tenant_id, kind, key) | hold_id | fast HoldCheck (class, urn, subject, org, range) |
| disposition_runs | (tenant_id, run_id) | schedule_version, candidates(json summary), exceptions(json), certificate(json), state, submitted_by, approved_by | — |
| tombstones | (tenant_id, record_class, bucket) | run_id, count, destroyed_at | non-personal facts only |
| erasure_requests | (tenant_id, request_id) | legal_basis, subject_refs (pseudonymous), scope_counts(json), confirmations(json), state, registered_by, approved_by | no personal data stored |
| key_store.deks (per cell) | (tenant_id, key_id) | kind (class_bucket / subject / hold), scope ref, wrapped_key, created_at, destroyed_at? | wrapped by tenant KEK |
| key_store.destruction_log (per cell) | (seq) | tenant_id, key_id, destroyed_at, run/request ref, prev_hash, hash | append-only; replicated; replayed by restore gate |
