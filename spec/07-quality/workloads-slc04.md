---
id: WL-SLC04
type: workload-catalog
title: Workloads & Added Quality Scenarios — SLC-04
wave: W5
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Workloads & Added Quality Scenarios — SLC-04

## workloads

_4 items_

| id | name | derivation | basis | target |
|---|---|---|---|---|
| WL-08a | Candidate generation | ≈ entity registrations + name/location claim changes ≈ 50/s; ≤ 10 candidates each | INF | QAS-ER-003 |
| WL-08b | Conflict detection | = claim writes ≈ 500/s; per-key evaluation | INF | QAS-CNF-001 |
| WL-08c | Cluster maintenance | match/split decisions ≈ ≤ 5/s; components ≤ 50 | INF | within decision transaction |
| WL-08d | Full re-blocking | on ruleset activation: all entities of a type (≤ 1e7) in batches | INF | completes ≤ 24 h, low priority |

## added_quality_scenarios

_5 items_

| id | quality | stimulus | environment | response_measure | refines |
|---|---|---|---|---|---|
| QAS-ER-001 | accuracy | candidate recall on labelled AR/EN test set | ruleset evaluation | ≥ 95 % of true matches proposed | BRQ-001 |
| QAS-ER-002 | usability | precision of proposals in review queue | ruleset evaluation | ≥ 60 % of proposals are true matches | BRQ-001 |
| QAS-ER-003 | performance | new entity registered | normal load | candidates visible p95 ≤ 60 s | BRQ-001 |
| QAS-CNF-001 | performance | incompatible claim committed | normal load | conflict opened p95 ≤ 30 s | BRQ-006 |
| QAS-PERF-015 | performance | resolved read of clustered entity | 750 reads/s | ≤ 20 % overhead vs unclustered; p95 ≤ 300 ms | BRQ-002 |

## scalability_design

- blocking index table (tenant, entity_type, key) → entity; bounded fan-out (top 10)
- detection partitioned by (tenant, cluster, predicate)
- clusters materialized; recomputation bounded by component size (≤ 50)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-08a
  name: Candidate generation
  derivation: ≈ entity registrations + name/location claim changes ≈ 50/s; ≤ 10 candidates each
  basis: INF
  target: QAS-ER-003
- id: WL-08b
  name: Conflict detection
  derivation: = claim writes ≈ 500/s; per-key evaluation
  basis: INF
  target: QAS-CNF-001
- id: WL-08c
  name: Cluster maintenance
  derivation: match/split decisions ≈ ≤ 5/s; components ≤ 50
  basis: INF
  target: within decision transaction
- id: WL-08d
  name: Full re-blocking
  derivation: 'on ruleset activation: all entities of a type (≤ 1e7) in batches'
  basis: INF
  target: completes ≤ 24 h, low priority
added_quality_scenarios:
- id: QAS-ER-001
  quality: accuracy
  stimulus: candidate recall on labelled AR/EN test set
  environment: ruleset evaluation
  response_measure: ≥ 95 % of true matches proposed
  refines:
  - BRQ-001
- id: QAS-ER-002
  quality: usability
  stimulus: precision of proposals in review queue
  environment: ruleset evaluation
  response_measure: ≥ 60 % of proposals are true matches
  refines:
  - BRQ-001
- id: QAS-ER-003
  quality: performance
  stimulus: new entity registered
  environment: normal load
  response_measure: candidates visible p95 ≤ 60 s
  refines:
  - BRQ-001
- id: QAS-CNF-001
  quality: performance
  stimulus: incompatible claim committed
  environment: normal load
  response_measure: conflict opened p95 ≤ 30 s
  refines:
  - BRQ-006
- id: QAS-PERF-015
  quality: performance
  stimulus: resolved read of clustered entity
  environment: 750 reads/s
  response_measure: ≤ 20 % overhead vs unclustered; p95 ≤ 300 ms
  refines:
  - BRQ-002
scalability_design:
- blocking index table (tenant, entity_type, key) → entity; bounded fan-out (top 10)
- detection partitioned by (tenant, cluster, predicate)
- clusters materialized; recomputation bounded by component size (≤ 50)
```

</details>
