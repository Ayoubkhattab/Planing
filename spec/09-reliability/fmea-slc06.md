---
id: FMEA-SLC06
type: fmea
title: Failure Mode Analysis — SLC-06
wave: W5
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Failure Mode Analysis — SLC-06

## failure_modes

_5 items_

### FM-S06-01

- **component:** Alert evaluator
- **failure:** lag
- **cause:** burst
- **effect:** late critical alerts
- **detection:** stream lag
- **severity:** H
- **likelihood:** M
- **prevention:** priority queue; scaled workers
- **mitigation_recovery:** catch-up; lag alert
- **data_loss:** none
- **user_impact:** late alerts
- **dependency_impact:** —

### FM-S06-02

- **component:** Membership evaluator
- **failure:** down
- **cause:** failure
- **effect:** COP stale
- **detection:** lag
- **severity:** M
- **likelihood:** L
- **prevention:** stateless partitions
- **mitigation_recovery:** re-evaluate from checkpoint
- **data_loss:** none
- **user_impact:** stale picture
- **dependency_impact:** tiles

### FM-S06-03

- **component:** Push gateway
- **failure:** down
- **cause:** network / relay
- **effect:** no push
- **detection:** delivery failures
- **severity:** M
- **likelihood:** M
- **prevention:** in-app inbox; polling
- **mitigation_recovery:** retries; FAILED after 5
- **data_loss:** none
- **user_impact:** delayed awareness
- **dependency_impact:** —

### FM-S06-04

- **component:** Tile renderer
- **failure:** overload
- **cause:** many distinct scopes
- **effect:** slow maps
- **detection:** latency
- **severity:** M
- **likelihood:** M
- **prevention:** clustering, element cap, scope-keyed cache
- **mitigation_recovery:** degrade to lower zoom
- **data_loss:** none
- **user_impact:** slow map
- **dependency_impact:** —

### FM-S06-05

- **component:** Scheduler
- **failure:** down
- **cause:** failure
- **effect:** escalations/TTL late
- **detection:** heartbeat
- **severity:** M
- **likelihood:** L
- **prevention:** leased buckets
- **mitigation_recovery:** catch-up
- **data_loss:** none
- **user_impact:** late escalation
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S06-01
  component: Alert evaluator
  failure: lag
  cause: burst
  effect: late critical alerts
  detection: stream lag
  severity: H
  likelihood: M
  prevention: priority queue; scaled workers
  mitigation_recovery: catch-up; lag alert
  data_loss: none
  user_impact: late alerts
  dependency_impact: —
- id: FM-S06-02
  component: Membership evaluator
  failure: down
  cause: failure
  effect: COP stale
  detection: lag
  severity: M
  likelihood: L
  prevention: stateless partitions
  mitigation_recovery: re-evaluate from checkpoint
  data_loss: none
  user_impact: stale picture
  dependency_impact: tiles
- id: FM-S06-03
  component: Push gateway
  failure: down
  cause: network / relay
  effect: no push
  detection: delivery failures
  severity: M
  likelihood: M
  prevention: in-app inbox; polling
  mitigation_recovery: retries; FAILED after 5
  data_loss: none
  user_impact: delayed awareness
  dependency_impact: —
- id: FM-S06-04
  component: Tile renderer
  failure: overload
  cause: many distinct scopes
  effect: slow maps
  detection: latency
  severity: M
  likelihood: M
  prevention: clustering, element cap, scope-keyed cache
  mitigation_recovery: degrade to lower zoom
  data_loss: none
  user_impact: slow map
  dependency_impact: —
- id: FM-S06-05
  component: Scheduler
  failure: down
  cause: failure
  effect: escalations/TTL late
  detection: heartbeat
  severity: M
  likelihood: L
  prevention: leased buckets
  mitigation_recovery: catch-up
  data_loss: none
  user_impact: late escalation
  dependency_impact: —
```

</details>
