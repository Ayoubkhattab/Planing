---
id: LDM-SLC14
type: logical-data-model
title: Logical Data Model — SLC-14
wave: W6
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-14 (schema `information`, BC02)

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| collection_requirements | (tenant_id, requirement_id, version) | question(json), area(geom 4326), window tstzrange, priority, due, eeis(json), requester, approver?, label, state | spatial index on area for APPROVED |
| fulfilment_links | (tenant_id, requirement_id, eei_id, observation_id) | derived_claim?, matched_at, lineage_ref | observation VALIDATED |
| collection_plans | (tenant_id, plan_id) | requirements[], title(json), label, state, version | — |
| collection_activities | (tenant_id, plan_id, activity_id) | method, sources[], area, window, unit, task_type, eei_refs[], task_ref? | area ⊆ requirement areas (checked in aggregate) |
