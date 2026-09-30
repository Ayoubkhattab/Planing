---
id: LDM-SLC09
type: logical-data-model
title: Logical Data Model — SLC-09
wave: W6
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-09 (schema `readiness`, BC05)

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| assets | (tenant_id, asset_id) | asset_type, name(json), owner_org, custody_holder, linked_entity_urn, state, condition_grade, capabilities(json), label, version | — |
| asset_certifications | (tenant_id, asset_id, code, valid_from) | issuer, valid_to, evidence? | history kept |
| asset_custody | (tenant_id, asset_id, seq) | holder, from, to, actor, reason | gapless seq |
| maintenance_orders | (tenant_id, order_id) | asset_id, kind, window tstzrange, state, outcome?, technician | EXCLUDE (asset_id WITH =, window WITH &&) WHERE state IN (PLANNED, IN_PROGRESS) |
| asset_reservations | (tenant_id, reservation_id) | asset_id, window tstzrange, purpose, link?, state, hold_expires_at | EXCLUDE (asset_id =, window &&) WHERE state IN (HELD, CONFIRMED) |
| asset_assignments | (tenant_id, assignment_id) | asset_id, task?, unit?, window, state, condition_report? | EXCLUDE (asset_id =, window &&) WHERE state = ACTIVE |
| resource_pools | (tenant_id, pool_id) | resource_type, unit, org_scope, state, label, version | — |
| pool_capacity_series | (tenant_id, pool_id, valid_from, recorded_from) | capacity, valid_to, recorded_to, reason | bitemporal |
| capacity_ledger | (tenant_id, pool_id, hour) | capacity, committed | CHECK(committed ≤ capacity); writable only by allocation role |
| allocations | (tenant_id, allocation_id) | pool_id, quantity, window, priority, target, requester, state, reasons(json), approver?, preempted_by? | — |
| allocation_consumption | (tenant_id, allocation_id, seq) | quantity, at | over-consumption flag |
| role_requirements | (tenant_id, role_id, version) | requirements(json), state | one ACTIVE per role |
| legacy_resource_notes_migration | (tenant_id, source_urn, note_seq) | note, proposed_ref?, decision, decided_by | DEBT-001 migration report |

قيود EXCLUDE (btree_gist) تفرض عدم التداخل في قاعدة البيانات نفسها — حماية ثانية بعد ثوابت الـ Aggregates (QAS-RES-001).
