---
id: FMEA-SLC18
type: fmea
title: Failure Mode Analysis — SLC-18
wave: W5
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
recalibrate_after_pilot: true
---

# Failure Mode Analysis — SLC-18

## failure_modes

_2 items_

### FM-S18-01

- **component:** Shared capacity ledger (SLC-09 dependency)
- **failure:** allocation contention spikes when logistics requests and task/plan allocations compete for the same resource pools during a surge
- **cause:** SLC-18 adds a new, unmeasured source of demand onto the same AGG-RESOURCE-POOL/AGG-ALLOCATION infrastructure that SLC-09 itself sized only from unmeasured estimates (R2-Q design values, RSK-027/028)
- **effect:** legitimate task/plan allocations may see a higher PENDING_APPROVAL or rejection rate during a logistics surge, since both share the same priority/time ordering window per pool (SPEC-ALLOCATION §2)
- **detection:** allocation rejection/pending rate per pool, segmented by target type (task/activity vs. logistics-request)
- **severity:** M
- **likelihood:** M
- **prevention:** no dedicated pools are required at design time, but a tenant may configure separate pools per item type; the ordering rule itself is shared, not duplicated or weakened
- **mitigation_recovery:** the same priority and pre-emption levers SLC-09 already exposes (CMD-ALC-PREEMPT, pool capacity adjustment) apply directly — no new mechanism to build for logistics specifically
- **data_loss:** none
- **user_impact:** possible unexpected contention on shared pools until sizing is tuned after Pilot R2
- **dependency_impact:** SLC-09 (Resource Pool, Allocation)

### FM-S18-02

- **component:** Logistics Request ↔ Shipment ↔ Allocation three-way link
- **failure:** a shipment departs referencing a logistics request whose allocation was just released by a concurrent cancellation
- **cause:** the request's cancel path (CMD-LGR-CANCEL) and the shipment's plan/depart path (CMD-SHP-PLAN/CMD-SHP-DEPART) are separate aggregates, coordinated only through each one's own optimistic version — no shared lock across the three
- **effect:** without a re-check, a shipment could depart against capacity that was already returned to the ledger
- **detection:** CMD-SHP-PLAN and CMD-SHP-DEPART's guards re-verify the linked allocation is still COMMITTED at that instant (INV-SHP-03), not only once at shipment creation
- **severity:** M
- **likelihood:** L
- **prevention:** the guard re-check at plan and depart time, rather than a one-time check at creation, closes the race deterministically — a cancelled request's released allocation makes the guard fail with ALLOCATION_NOT_COMMITTED
- **mitigation_recovery:** the operator retries CMD-SHP-PLAN against a fresh, still-committed allocation, or a new logistics request is issued
- **data_loss:** none
- **user_impact:** a rejected shipment command, never a silent inconsistency between the two aggregates
- **dependency_impact:** SLC-09 (Allocation)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S18-01
  component: Shared capacity ledger (SLC-09 dependency)
  failure: allocation contention spikes when logistics requests and task/plan allocations compete for the same resource pools during a surge
  cause: SLC-18 adds a new, unmeasured source of demand onto the same AGG-RESOURCE-POOL/AGG-ALLOCATION infrastructure that SLC-09 itself sized only from unmeasured estimates (R2-Q design values, RSK-027/028)
  effect: legitimate task/plan allocations may see a higher PENDING_APPROVAL or rejection rate during a logistics surge, since both share the same priority/time ordering window per pool (SPEC-ALLOCATION §2)
  detection: allocation rejection/pending rate per pool, segmented by target type (task/activity vs. logistics-request)
  severity: M
  likelihood: M
  prevention: no dedicated pools are required at design time, but a tenant may configure separate pools per item type; the ordering rule itself is shared, not duplicated or weakened
  mitigation_recovery: the same priority and pre-emption levers SLC-09 already exposes (CMD-ALC-PREEMPT, pool capacity adjustment) apply directly — no new mechanism to build for logistics specifically
  data_loss: none
  user_impact: possible unexpected contention on shared pools until sizing is tuned after Pilot R2
  dependency_impact: SLC-09 (Resource Pool, Allocation)
- id: FM-S18-02
  component: Logistics Request ↔ Shipment ↔ Allocation three-way link
  failure: a shipment departs referencing a logistics request whose allocation was just released by a concurrent cancellation
  cause: the request's cancel path (CMD-LGR-CANCEL) and the shipment's plan/depart path (CMD-SHP-PLAN/CMD-SHP-DEPART) are separate aggregates, coordinated only through each one's own optimistic version — no shared lock across the three
  effect: without a re-check, a shipment could depart against capacity that was already returned to the ledger
  detection: CMD-SHP-PLAN and CMD-SHP-DEPART's guards re-verify the linked allocation is still COMMITTED at that instant (INV-SHP-03), not only once at shipment creation
  severity: M
  likelihood: L
  prevention: the guard re-check at plan and depart time, rather than a one-time check at creation, closes the race deterministically — a cancelled request's released allocation makes the guard fail with ALLOCATION_NOT_COMMITTED
  mitigation_recovery: the operator retries CMD-SHP-PLAN against a fresh, still-committed allocation, or a new logistics request is issued
  data_loss: none
  user_impact: a rejected shipment command, never a silent inconsistency between the two aggregates
  dependency_impact: SLC-09 (Allocation)
```

</details>
