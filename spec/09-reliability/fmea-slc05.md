---
id: FMEA-SLC05
type: fmea
title: Failure Mode Analysis — SLC-05
wave: W5
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Failure Mode Analysis — SLC-05

## failure_modes

_5 items_

### FM-S05-01

- **component:** Projection pipeline
- **failure:** lag
- **cause:** burst or consumer failure
- **effect:** stale results
- **detection:** lag metric
- **severity:** M
- **likelihood:** M
- **prevention:** scaled consumers; backpressure
- **mitigation_recovery:** DEGRADED state; catch-up
- **data_loss:** none
- **user_impact:** stale search
- **dependency_impact:** —

### FM-S05-02

- **component:** Search engine
- **failure:** unavailable
- **cause:** failure
- **effect:** search 503
- **detection:** health
- **severity:** M
- **likelihood:** L
- **prevention:** replicas
- **mitigation_recovery:** owners' direct reads continue
- **data_loss:** none
- **user_impact:** no search
- **dependency_impact:** —

### FM-S05-03

- **component:** LabelCheck owner
- **failure:** unavailable
- **cause:** owner outage
- **effect:** results of that owner dropped
- **detection:** health
- **severity:** M
- **likelihood:** L
- **prevention:** HA owners
- **mitigation_recovery:** partial results flagged by health
- **data_loss:** none
- **user_impact:** incomplete results
- **dependency_impact:** —

### FM-S05-04

- **component:** Rebuild
- **failure:** fails
- **cause:** bug or data
- **effect:** BUILDING → FAILED
- **detection:** build status
- **severity:** L
- **likelihood:** M
- **prevention:** verification sample before promote
- **mitigation_recovery:** old ACTIVE keeps serving
- **data_loss:** none
- **user_impact:** none
- **dependency_impact:** —

### FM-S05-05

- **component:** Divergence
- **failure:** projection ≠ source
- **cause:** missed event
- **effect:** wrong/missing hits
- **detection:** nightly sampled reconciliation
- **severity:** M
- **likelihood:** L
- **prevention:** inbox + ordered partitions
- **mitigation_recovery:** targeted re-index or rebuild
- **data_loss:** none
- **user_impact:** missing hits
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S05-01
  component: Projection pipeline
  failure: lag
  cause: burst or consumer failure
  effect: stale results
  detection: lag metric
  severity: M
  likelihood: M
  prevention: scaled consumers; backpressure
  mitigation_recovery: DEGRADED state; catch-up
  data_loss: none
  user_impact: stale search
  dependency_impact: —
- id: FM-S05-02
  component: Search engine
  failure: unavailable
  cause: failure
  effect: search 503
  detection: health
  severity: M
  likelihood: L
  prevention: replicas
  mitigation_recovery: owners' direct reads continue
  data_loss: none
  user_impact: no search
  dependency_impact: —
- id: FM-S05-03
  component: LabelCheck owner
  failure: unavailable
  cause: owner outage
  effect: results of that owner dropped
  detection: health
  severity: M
  likelihood: L
  prevention: HA owners
  mitigation_recovery: partial results flagged by health
  data_loss: none
  user_impact: incomplete results
  dependency_impact: —
- id: FM-S05-04
  component: Rebuild
  failure: fails
  cause: bug or data
  effect: BUILDING → FAILED
  detection: build status
  severity: L
  likelihood: M
  prevention: verification sample before promote
  mitigation_recovery: old ACTIVE keeps serving
  data_loss: none
  user_impact: none
  dependency_impact: —
- id: FM-S05-05
  component: Divergence
  failure: projection ≠ source
  cause: missed event
  effect: wrong/missing hits
  detection: nightly sampled reconciliation
  severity: M
  likelihood: L
  prevention: inbox + ordered partitions
  mitigation_recovery: targeted re-index or rebuild
  data_loss: none
  user_impact: missing hits
  dependency_impact: —
```

</details>
