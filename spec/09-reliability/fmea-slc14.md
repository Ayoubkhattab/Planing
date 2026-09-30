---
id: FMEA-SLC14
type: fmea
title: Failure Mode Analysis — SLC-14
wave: W5
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Failure Mode Analysis — SLC-14

## failure_modes

_1 items_

### FM-S14-01

- **component:** Matching engine
- **failure:** lag
- **cause:** backlog
- **effect:** fulfilment late
- **detection:** lag metric
- **severity:** L
- **likelihood:** M
- **prevention:** stateless partitioned workers
- **mitigation_recovery:** catch-up from events
- **data_loss:** none
- **user_impact:** stale status
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S14-01
  component: Matching engine
  failure: lag
  cause: backlog
  effect: fulfilment late
  detection: lag metric
  severity: L
  likelihood: M
  prevention: stateless partitioned workers
  mitigation_recovery: catch-up from events
  data_loss: none
  user_impact: stale status
  dependency_impact: —
```

</details>
