---
id: FMEA-SLC12
type: fmea
title: Failure Mode Analysis — SLC-12
wave: W5
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Failure Mode Analysis — SLC-12

## failure_modes

_3 items_

### FM-S12-P1

- **component:** Product generator
- **failure:** fails
- **cause:** binding error / timeout
- **effect:** GENERATION_FAILED
- **detection:** job status
- **severity:** M
- **likelihood:** M
- **prevention:** sample generation at template activation
- **mitigation_recovery:** regenerate
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** —

### FM-S12-P2

- **component:** Cold archive
- **failure:** slow retrieval
- **cause:** offline media
- **effect:** retrieval ≤ 24 h
- **detection:** staging queue
- **severity:** L
- **likelihood:** M
- **prevention:** warm tier for recent/high-use
- **mitigation_recovery:** staged job
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** —

### FM-S12-P3

- **component:** Fixity
- **failure:** mismatch
- **cause:** bit rot / tampering
- **effect:** INTEGRITY_FAILED
- **detection:** integrity job
- **severity:** H
- **likelihood:** L
- **prevention:** WORM + replica
- **mitigation_recovery:** repair from replica
- **data_loss:** none if replica ok
- **user_impact:** none
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S12-P1
  component: Product generator
  failure: fails
  cause: binding error / timeout
  effect: GENERATION_FAILED
  detection: job status
  severity: M
  likelihood: M
  prevention: sample generation at template activation
  mitigation_recovery: regenerate
  data_loss: none
  user_impact: delay
  dependency_impact: —
- id: FM-S12-P2
  component: Cold archive
  failure: slow retrieval
  cause: offline media
  effect: retrieval ≤ 24 h
  detection: staging queue
  severity: L
  likelihood: M
  prevention: warm tier for recent/high-use
  mitigation_recovery: staged job
  data_loss: none
  user_impact: delay
  dependency_impact: —
- id: FM-S12-P3
  component: Fixity
  failure: mismatch
  cause: bit rot / tampering
  effect: INTEGRITY_FAILED
  detection: integrity job
  severity: H
  likelihood: L
  prevention: WORM + replica
  mitigation_recovery: repair from replica
  data_loss: none if replica ok
  user_impact: none
  dependency_impact: —
```

</details>
