---
id: FMEA-SLC04
type: fmea
title: Failure Mode Analysis — SLC-04
wave: W5
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Failure Mode Analysis — SLC-04

## failure_modes

_4 items_

### FM-S04-01

- **component:** Conflict detector
- **failure:** lagging / down
- **cause:** worker failure
- **effect:** conflicts open late; resolved views still show DISPUTED (computed by LIB)
- **detection:** queue lag
- **severity:** M
- **likelihood:** M
- **prevention:** stateless workers; idempotent
- **mitigation_recovery:** catch-up; no data loss
- **data_loss:** none
- **user_impact:** review delay
- **dependency_impact:** —

### FM-S04-02

- **component:** Candidate generator
- **failure:** down
- **cause:** failure
- **effect:** no new proposals
- **detection:** lag metric
- **severity:** L
- **likelihood:** M
- **prevention:** stateless; incremental
- **mitigation_recovery:** catch-up
- **data_loss:** none
- **user_impact:** duplicates stay unmerged longer
- **dependency_impact:** —

### FM-S04-03

- **component:** Cluster table
- **failure:** inconsistent with links
- **cause:** bug
- **effect:** wrong resolved identity
- **detection:** nightly recompute from links (as-known-at)
- **severity:** H
- **likelihood:** L
- **prevention:** same-transaction maintenance; P-44
- **mitigation_recovery:** rebuild from same_as_links
- **data_loss:** none
- **user_impact:** wrong merges shown until rebuild
- **dependency_impact:** projections

### FM-S04-04

- **component:** Mass mis-merge
- **failure:** bad decisions
- **cause:** human error / bad ruleset
- **effect:** many wrong clusters
- **detection:** cluster-size and split-rate alerts
- **severity:** H
- **likelihood:** L
- **prevention:** size gate; SoD
- **mitigation_recovery:** bulk split tooling by case list (audited)
- **data_loss:** none
- **user_impact:** temporary wrong views
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S04-01
  component: Conflict detector
  failure: lagging / down
  cause: worker failure
  effect: conflicts open late; resolved views still show DISPUTED (computed by LIB)
  detection: queue lag
  severity: M
  likelihood: M
  prevention: stateless workers; idempotent
  mitigation_recovery: catch-up; no data loss
  data_loss: none
  user_impact: review delay
  dependency_impact: —
- id: FM-S04-02
  component: Candidate generator
  failure: down
  cause: failure
  effect: no new proposals
  detection: lag metric
  severity: L
  likelihood: M
  prevention: stateless; incremental
  mitigation_recovery: catch-up
  data_loss: none
  user_impact: duplicates stay unmerged longer
  dependency_impact: —
- id: FM-S04-03
  component: Cluster table
  failure: inconsistent with links
  cause: bug
  effect: wrong resolved identity
  detection: nightly recompute from links (as-known-at)
  severity: H
  likelihood: L
  prevention: same-transaction maintenance; P-44
  mitigation_recovery: rebuild from same_as_links
  data_loss: none
  user_impact: wrong merges shown until rebuild
  dependency_impact: projections
- id: FM-S04-04
  component: Mass mis-merge
  failure: bad decisions
  cause: human error / bad ruleset
  effect: many wrong clusters
  detection: cluster-size and split-rate alerts
  severity: H
  likelihood: L
  prevention: size gate; SoD
  mitigation_recovery: bulk split tooling by case list (audited)
  data_loss: none
  user_impact: temporary wrong views
  dependency_impact: —
```

</details>
