---
id: FMEA-SLC09
type: fmea
title: Failure Mode Analysis — SLC-09
wave: W5
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Failure Mode Analysis — SLC-09

## failure_modes

_3 items_

### FM-S09-01

- **component:** Capacity ledger
- **failure:** drift from allocations
- **cause:** bug
- **effect:** over/under availability
- **detection:** nightly reconciliation (Σ committed = ledger)
- **severity:** H
- **likelihood:** L
- **prevention:** single writer path; FIT
- **mitigation_recovery:** rebuild ledger from allocations
- **data_loss:** none
- **user_impact:** wrong availability
- **dependency_impact:** plans

### FM-S09-02

- **component:** Availability view
- **failure:** stale
- **cause:** event lag
- **effect:** planner sees wrong availability
- **detection:** lag metric
- **severity:** M
- **likelihood:** M
- **prevention:** commands re-check source
- **mitigation_recovery:** refresh
- **data_loss:** none
- **user_impact:** rejected reservation
- **dependency_impact:** —

### FM-S09-03

- **component:** Ordering window worker
- **failure:** down
- **cause:** failure
- **effect:** allocations stuck REQUESTED
- **detection:** queue age
- **severity:** M
- **likelihood:** L
- **prevention:** HA workers; lease
- **mitigation_recovery:** resume
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S09-01
  component: Capacity ledger
  failure: drift from allocations
  cause: bug
  effect: over/under availability
  detection: nightly reconciliation (Σ committed = ledger)
  severity: H
  likelihood: L
  prevention: single writer path; FIT
  mitigation_recovery: rebuild ledger from allocations
  data_loss: none
  user_impact: wrong availability
  dependency_impact: plans
- id: FM-S09-02
  component: Availability view
  failure: stale
  cause: event lag
  effect: planner sees wrong availability
  detection: lag metric
  severity: M
  likelihood: M
  prevention: commands re-check source
  mitigation_recovery: refresh
  data_loss: none
  user_impact: rejected reservation
  dependency_impact: —
- id: FM-S09-03
  component: Ordering window worker
  failure: down
  cause: failure
  effect: allocations stuck REQUESTED
  detection: queue age
  severity: M
  likelihood: L
  prevention: HA workers; lease
  mitigation_recovery: resume
  data_loss: none
  user_impact: delay
  dependency_impact: —
```

</details>
