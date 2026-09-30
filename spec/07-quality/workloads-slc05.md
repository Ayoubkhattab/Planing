---
id: WL-SLC05
type: workload-catalog
title: Workloads & Added Quality Scenarios — SLC-05
wave: W5
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Workloads & Added Quality Scenarios — SLC-05

## workloads

_4 items_

| id | name | derivation | basis | target |
|---|---|---|---|---|
| WL-02a | Search queries | ≈ 20 % of 2,500 req/s ≈ 500/s peak | INF | QAS-PERF-003 |
| WL-02b | Index updates | ≈ claim + observation + task events ≈ 5,600/s peak (observations dominate) | INF | QAS-PERF-004 |
| WL-02c | LabelCheck calls | 1 batched call per owning context per page ≈ 500–1,000/s | INF | p95 ≤ 20 ms |
| WL-08e | Graph queries | ≈ 20/s | INF | QAS-PERF-018 |

## added_quality_scenarios

_3 items_

| id | quality | stimulus | environment | response_measure | refines |
|---|---|---|---|---|---|
| QAS-SEC-011 | security | inference test suite on search, suggestions, facets, graph and paths | normal | 0 disclosures of hidden objects, hidden facts, hidden nodes/edges | BRQ-007 |
| QAS-PERF-018 | performance | graph neighborhood depth 2 | design load, dense nodes | p95 ≤ 1 s | BRQ-002 |
| QAS-REL-004 | recoverability | full projection rebuild | design volume | ≤ 24 h to READY with no loss of query service (old version stays ACTIVE) | BRQ-006 |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-02a
  name: Search queries
  derivation: ≈ 20 % of 2,500 req/s ≈ 500/s peak
  basis: INF
  target: QAS-PERF-003
- id: WL-02b
  name: Index updates
  derivation: ≈ claim + observation + task events ≈ 5,600/s peak (observations dominate)
  basis: INF
  target: QAS-PERF-004
- id: WL-02c
  name: LabelCheck calls
  derivation: 1 batched call per owning context per page ≈ 500–1,000/s
  basis: INF
  target: p95 ≤ 20 ms
- id: WL-08e
  name: Graph queries
  derivation: ≈ 20/s
  basis: INF
  target: QAS-PERF-018
added_quality_scenarios:
- id: QAS-SEC-011
  quality: security
  stimulus: inference test suite on search, suggestions, facets, graph and paths
  environment: normal
  response_measure: 0 disclosures of hidden objects, hidden facts, hidden nodes/edges
  refines:
  - BRQ-007
- id: QAS-PERF-018
  quality: performance
  stimulus: graph neighborhood depth 2
  environment: design load, dense nodes
  response_measure: p95 ≤ 1 s
  refines:
  - BRQ-002
- id: QAS-REL-004
  quality: recoverability
  stimulus: full projection rebuild
  environment: design volume
  response_measure: ≤ 24 h to READY with no loss of query service (old version stays ACTIVE)
  refines:
  - BRQ-006
```

</details>
