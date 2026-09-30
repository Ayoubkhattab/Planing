---
id: FMEA-SLC08
type: fmea
title: Failure Mode Analysis — SLC-08
wave: W5
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Failure Mode Analysis — SLC-08

## failure_modes

_3 items_

### FM-S08-01

- **component:** Task synchronizer
- **failure:** fails mid-run
- **cause:** error
- **effect:** partial task set
- **detection:** run status vs expected diff
- **severity:** M
- **likelihood:** L
- **prevention:** idempotent run id; resumable
- **mitigation_recovery:** re-run completes remaining items
- **data_loss:** none
- **user_impact:** temporary mismatch shown in progress
- **dependency_impact:** SLC-03

### FM-S08-02

- **component:** Authority check (BC01)
- **failure:** unavailable
- **cause:** outage
- **effect:** decisions and approvals rejected
- **detection:** error rate
- **severity:** M
- **likelihood:** L
- **prevention:** HA BC01
- **mitigation_recovery:** retry; fail-closed
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** —

### FM-S08-03

- **component:** Outcome source
- **failure:** late measurement
- **cause:** task result delayed
- **effect:** progress lag
- **detection:** freshness
- **severity:** L
- **likelihood:** M
- **prevention:** —
- **mitigation_recovery:** progress shows as-of time
- **data_loss:** none
- **user_impact:** stale progress
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S08-01
  component: Task synchronizer
  failure: fails mid-run
  cause: error
  effect: partial task set
  detection: run status vs expected diff
  severity: M
  likelihood: L
  prevention: idempotent run id; resumable
  mitigation_recovery: re-run completes remaining items
  data_loss: none
  user_impact: temporary mismatch shown in progress
  dependency_impact: SLC-03
- id: FM-S08-02
  component: Authority check (BC01)
  failure: unavailable
  cause: outage
  effect: decisions and approvals rejected
  detection: error rate
  severity: M
  likelihood: L
  prevention: HA BC01
  mitigation_recovery: retry; fail-closed
  data_loss: none
  user_impact: delay
  dependency_impact: —
- id: FM-S08-03
  component: Outcome source
  failure: late measurement
  cause: task result delayed
  effect: progress lag
  detection: freshness
  severity: L
  likelihood: M
  prevention: —
  mitigation_recovery: progress shows as-of time
  data_loss: none
  user_impact: stale progress
  dependency_impact: —
```

</details>
