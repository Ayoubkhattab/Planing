---
id: FMEA-SLC16
type: fmea
title: Failure Mode Analysis — SLC-16
wave: W5
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Failure Mode Analysis — SLC-16

## failure_modes

_2 items_

### FM-S16-01

- **component:** External system
- **failure:** outage
- **cause:** remote
- **effect:** no new data
- **detection:** health checks
- **severity:** M
- **likelihood:** M
- **prevention:** cursor/watermark
- **mitigation_recovery:** replay backlog ≤ 1 h after 4 h outage
- **data_loss:** none
- **user_impact:** stale external data
- **dependency_impact:** —

### FM-S16-02

- **component:** CAP endpoint
- **failure:** unreachable
- **cause:** network
- **effect:** FAILED messages
- **detection:** delivery errors
- **severity:** M
- **likelihood:** L
- **prevention:** retries
- **mitigation_recovery:** operator retry
- **data_loss:** none
- **user_impact:** external partners not informed
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S16-01
  component: External system
  failure: outage
  cause: remote
  effect: no new data
  detection: health checks
  severity: M
  likelihood: M
  prevention: cursor/watermark
  mitigation_recovery: replay backlog ≤ 1 h after 4 h outage
  data_loss: none
  user_impact: stale external data
  dependency_impact: —
- id: FM-S16-02
  component: CAP endpoint
  failure: unreachable
  cause: network
  effect: FAILED messages
  detection: delivery errors
  severity: M
  likelihood: L
  prevention: retries
  mitigation_recovery: operator retry
  data_loss: none
  user_impact: external partners not informed
  dependency_impact: —
```

</details>
