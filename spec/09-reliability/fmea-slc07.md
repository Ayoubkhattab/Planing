---
id: FMEA-SLC07
type: fmea
title: Failure Mode Analysis — SLC-07
wave: W5
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Failure Mode Analysis — SLC-07

## failure_modes

_4 items_

### FM-S07-01

- **component:** Compute worker
- **failure:** crash mid-run
- **cause:** failure
- **effect:** run stuck RUNNING
- **detection:** lease expiry
- **severity:** M
- **likelihood:** M
- **prevention:** leases; idempotent restart from inputs
- **mitigation_recovery:** re-run automatically once, then FAILED
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** —

### FM-S07-02

- **component:** Image registry
- **failure:** unavailable
- **cause:** failure
- **effect:** runs cannot start
- **detection:** health
- **severity:** M
- **likelihood:** L
- **prevention:** replicated internal registry; local image cache
- **mitigation_recovery:** queue waits
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** —

### FM-S07-03

- **component:** Source data
- **failure:** changed after submission
- **cause:** normal operation
- **effect:** n/a — inputs pinned by known_at
- **detection:** —
- **severity:** L
- **likelihood:** H
- **prevention:** bitemporal pins
- **mitigation_recovery:** none needed
- **data_loss:** none
- **user_impact:** none
- **dependency_impact:** —

### FM-S07-04

- **component:** Long runs
- **failure:** exceed timeout
- **cause:** heavy data
- **effect:** FAILED
- **detection:** timeout
- **severity:** M
- **likelihood:** M
- **prevention:** tile-wise processing; method-level timeout
- **mitigation_recovery:** resubmit with narrower scope
- **data_loss:** none
- **user_impact:** rework
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S07-01
  component: Compute worker
  failure: crash mid-run
  cause: failure
  effect: run stuck RUNNING
  detection: lease expiry
  severity: M
  likelihood: M
  prevention: leases; idempotent restart from inputs
  mitigation_recovery: re-run automatically once, then FAILED
  data_loss: none
  user_impact: delay
  dependency_impact: —
- id: FM-S07-02
  component: Image registry
  failure: unavailable
  cause: failure
  effect: runs cannot start
  detection: health
  severity: M
  likelihood: L
  prevention: replicated internal registry; local image cache
  mitigation_recovery: queue waits
  data_loss: none
  user_impact: delay
  dependency_impact: —
- id: FM-S07-03
  component: Source data
  failure: changed after submission
  cause: normal operation
  effect: n/a — inputs pinned by known_at
  detection: —
  severity: L
  likelihood: H
  prevention: bitemporal pins
  mitigation_recovery: none needed
  data_loss: none
  user_impact: none
  dependency_impact: —
- id: FM-S07-04
  component: Long runs
  failure: exceed timeout
  cause: heavy data
  effect: FAILED
  detection: timeout
  severity: M
  likelihood: M
  prevention: tile-wise processing; method-level timeout
  mitigation_recovery: resubmit with narrower scope
  data_loss: none
  user_impact: rework
  dependency_impact: —
```

</details>
