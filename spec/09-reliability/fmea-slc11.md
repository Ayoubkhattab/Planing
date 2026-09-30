---
id: FMEA-SLC11
type: fmea
title: Failure Mode Analysis — SLC-11
wave: W5
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Failure Mode Analysis — SLC-11

## failure_modes

_4 items_

### FM-S11-01

- **component:** Sync gateway
- **failure:** overload
- **cause:** reconnect storm
- **effect:** slow sync
- **detection:** queue depth
- **severity:** M
- **likelihood:** M
- **prevention:** stateless scale-out; per-device rate; oldest-first
- **mitigation_recovery:** queue drains ≤ 30 min
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** —

### FM-S11-02

- **component:** Transport
- **failure:** drops mid-batch
- **cause:** field network
- **effect:** session FAILED
- **detection:** session state
- **severity:** M
- **likelihood:** H
- **prevention:** acked seq; idempotent ids
- **mitigation_recovery:** resume next session
- **data_loss:** none
- **user_impact:** none
- **dependency_impact:** —

### FM-S11-03

- **component:** Owner context
- **failure:** unavailable during sync
- **cause:** outage
- **effect:** commands cannot apply
- **detection:** owner health
- **severity:** M
- **likelihood:** L
- **prevention:** retry with backoff inside session
- **mitigation_recovery:** session FAILED, resume later
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** owners

### FM-S11-04

- **component:** Device storage
- **failure:** corrupted
- **cause:** hardware
- **effect:** queued commands lost
- **detection:** hash chain break at handshake
- **severity:** H
- **likelihood:** L
- **prevention:** hash chain; periodic encrypted backup to server when online
- **mitigation_recovery:** report + data recovery from partial chain
- **data_loss:** possible (device only)
- **user_impact:** lost captures
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S11-01
  component: Sync gateway
  failure: overload
  cause: reconnect storm
  effect: slow sync
  detection: queue depth
  severity: M
  likelihood: M
  prevention: stateless scale-out; per-device rate; oldest-first
  mitigation_recovery: queue drains ≤ 30 min
  data_loss: none
  user_impact: delay
  dependency_impact: —
- id: FM-S11-02
  component: Transport
  failure: drops mid-batch
  cause: field network
  effect: session FAILED
  detection: session state
  severity: M
  likelihood: H
  prevention: acked seq; idempotent ids
  mitigation_recovery: resume next session
  data_loss: none
  user_impact: none
  dependency_impact: —
- id: FM-S11-03
  component: Owner context
  failure: unavailable during sync
  cause: outage
  effect: commands cannot apply
  detection: owner health
  severity: M
  likelihood: L
  prevention: retry with backoff inside session
  mitigation_recovery: session FAILED, resume later
  data_loss: none
  user_impact: delay
  dependency_impact: owners
- id: FM-S11-04
  component: Device storage
  failure: corrupted
  cause: hardware
  effect: queued commands lost
  detection: hash chain break at handshake
  severity: H
  likelihood: L
  prevention: hash chain; periodic encrypted backup to server when online
  mitigation_recovery: report + data recovery from partial chain
  data_loss: possible (device only)
  user_impact: lost captures
  dependency_impact: —
```

</details>
