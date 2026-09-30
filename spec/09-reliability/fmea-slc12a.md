---
id: FMEA-SLC12A
type: fmea
title: Failure Mode Analysis — SLC-12a
wave: W5
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Failure Mode Analysis — SLC-12a

## failure_modes

_3 items_

### FM-S12-01

- **component:** Key destruction
- **failure:** partial
- **cause:** KMS failure mid-run
- **effect:** bucket partly processed
- **detection:** run exceptions
- **severity:** H
- **likelihood:** L
- **prevention:** idempotent per bucket; re-wrap before destroy
- **mitigation_recovery:** retry next run
- **data_loss:** none (keys either destroyed or intact)
- **user_impact:** none
- **dependency_impact:** —

### FM-S12-02

- **component:** HoldCheck
- **failure:** unavailable
- **cause:** BC08 outage
- **effect:** disposition/erasure cannot proceed
- **detection:** health
- **severity:** M
- **likelihood:** L
- **prevention:** fail-closed
- **mitigation_recovery:** wait
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** owners' erase commands

### FM-S12-03

- **component:** Owner confirmation
- **failure:** missing
- **cause:** context outage
- **effect:** erasure stays EXECUTING
- **detection:** age > 24 h
- **severity:** M
- **likelihood:** L
- **prevention:** retries
- **mitigation_recovery:** escalate to Legal
- **data_loss:** none
- **user_impact:** compliance delay
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S12-01
  component: Key destruction
  failure: partial
  cause: KMS failure mid-run
  effect: bucket partly processed
  detection: run exceptions
  severity: H
  likelihood: L
  prevention: idempotent per bucket; re-wrap before destroy
  mitigation_recovery: retry next run
  data_loss: none (keys either destroyed or intact)
  user_impact: none
  dependency_impact: —
- id: FM-S12-02
  component: HoldCheck
  failure: unavailable
  cause: BC08 outage
  effect: disposition/erasure cannot proceed
  detection: health
  severity: M
  likelihood: L
  prevention: fail-closed
  mitigation_recovery: wait
  data_loss: none
  user_impact: delay
  dependency_impact: owners' erase commands
- id: FM-S12-03
  component: Owner confirmation
  failure: missing
  cause: context outage
  effect: erasure stays EXECUTING
  detection: age > 24 h
  severity: M
  likelihood: L
  prevention: retries
  mitigation_recovery: escalate to Legal
  data_loss: none
  user_impact: compliance delay
  dependency_impact: —
```

</details>
