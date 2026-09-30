---
id: LDM-SLC12
type: logical-data-model
title: Logical Data Model — SLC-12
wave: W6
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-12 (schema `knowledge`, BC06)

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| product_templates | (tenant_id, template_id, version) | code, kind, sections(json), state | — |
| products | (tenant_id, product_id, version) | template_id, template_version, parameters(json), audience(json), label, state, generated_known_at, artifacts(json: format, sha256, object_key), citations(json pinned), author, reviewer | APPROVED immutable; one APPROVED per product_id |
| product_exclusions | (tenant_id, product_id, version, seq) | object_urn, reason | internal audit only; never rendered |
| distributions | (tenant_id, distribution_id) | product_id, version, formats[], state, distributor | — |
| deliveries | (tenant_id, distribution_id, recipient) | watermark_id, format, delivered_at, status (delivered/excluded) | — |
| knowledge_objects | (tenant_id, knowledge_id, version) | type, title(json), statements(json), relationships(json), source?, label, state, author, reviewer, reuse_count | one PUBLISHED per knowledge_id |
| knowledge_relations_index | (tenant_id, kind, ref, knowledge_id) | — | for suggestions |
| archive_packages | (tenant_id, package_id) | record_class, bucket, bag_manifest(json), representations(json), label, state, tier (warm/cold), last_fixity_at | — |
| archive_preservation_events | (tenant_id, package_id, seq) | event (ingest, fixity, migration, repair, transfer), outcome, at, agent | append-only |
| archive_access | (tenant_id, package_id, seq) | actor, purpose, at | append-only (REQ-ARC-003) |
| reconstructions | (tenant_id, reconstruction_id) | scope(json), valid_at, known_at, purpose, requester, state, report_ref | — |
