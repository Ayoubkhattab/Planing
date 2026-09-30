---
id: LDM-SLC18
type: logical-data-model
title: Logical Data Model — SLC-18
wave: W6
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
---

# Logical Data Model — SLC-18

| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| logistics_requests (readiness) | (tenant_id, request_id) | item_pool_ref, quantity, destination(json), needed_by, priority, requester, justification, allocation_ref, shipment_ref?, delivered_quantity?, label, state, version | exactly one allocation_ref, created in the same unit of work as the row (INV-LGR-01) |
| shipments (readiness) | (tenant_id, shipment_id) | logistics_request_ref, origin_pool_ref, destination(json), carrier, planned_quantity, delivered_quantity?, damaged_quantity?, label, state, version | planned_quantity ≤ linked allocation's committed quantity at CMD-SHP-PLAN time (INV-SHP-03) |
| shipment_checkpoints | (tenant_id, shipment_id, recorded_at) | location(json), note, actor | append-only; recorded_at strictly increasing per shipment (INV-SHP-01) |
| resource_pools (readiness, unchanged — SLC-09) | (tenant_id, pool_id) | ...existing SLC-09 columns... | resource_type may now be a logistics item type (RD-LOGISTICS-ITEM-TYPES); no schema change |
| allocations (readiness, extended guard only — CR-62) | (tenant_id, allocation_id) | ...existing SLC-09 columns..., target_ref | target_ref may now reference a logistics_requests row in addition to a task/activity; column type (urn) unchanged |
