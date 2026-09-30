---
id: FMEA-SLC15
type: fmea
title: Failure Mode Analysis — SLC-15
wave: W5
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Failure Mode Analysis — SLC-15

## failure_modes

_1 items_

### FM-S15-01

- **component:** Correlation engine
- **failure:** lag / down
- **cause:** burst
- **effect:** late proposals
- **detection:** lag metric
- **severity:** L
- **likelihood:** M
- **prevention:** partitioned by geohash4
- **mitigation_recovery:** catch-up
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S15-01
  component: Correlation engine
  failure: lag / down
  cause: burst
  effect: late proposals
  detection: lag metric
  severity: L
  likelihood: M
  prevention: partitioned by geohash4
  mitigation_recovery: catch-up
  data_loss: none
  user_impact: delay
  dependency_impact: —
```

</details>
