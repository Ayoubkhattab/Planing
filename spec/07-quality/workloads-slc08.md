---
id: WL-SLC08
type: workload-catalog
title: Workloads & Added Quality Scenarios — SLC-08
wave: W5
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Workloads & Added Quality Scenarios — SLC-08

## workloads

_3 items_

| id | name | derivation | basis | target |
|---|---|---|---|---|
| WL-01m | Decisions & plan commands | low volume ≈ ≤ 10/s | INF | QAS-PERF-001 |
| WL-01n | Task synchronization bursts | ≤ 500 tasks per baseline | INF | QAS-PERF-021 |
| WL-01o | Progress reads | ≈ 50/s | INF | QAS-PERF-002 |

## added_quality_scenarios

_2 items_

| id | quality | stimulus | environment | response_measure | refines |
|---|---|---|---|---|---|
| QAS-PERF-021 | performance | plan version baselined with 500 task-generating activities | normal | task synchronization completes ≤ 60 s; idempotent on retry | BRQ-004 |
| QAS-TRC-003 | traceability | auditor asks for a decision's basis | normal | authority chain, pinned citations and claims as known at decision time returned; 100 % of decisions | BRQ-003 |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-01m
  name: Decisions & plan commands
  derivation: low volume ≈ ≤ 10/s
  basis: INF
  target: QAS-PERF-001
- id: WL-01n
  name: Task synchronization bursts
  derivation: ≤ 500 tasks per baseline
  basis: INF
  target: QAS-PERF-021
- id: WL-01o
  name: Progress reads
  derivation: ≈ 50/s
  basis: INF
  target: QAS-PERF-002
added_quality_scenarios:
- id: QAS-PERF-021
  quality: performance
  stimulus: plan version baselined with 500 task-generating activities
  environment: normal
  response_measure: task synchronization completes ≤ 60 s; idempotent on retry
  refines:
  - BRQ-004
- id: QAS-TRC-003
  quality: traceability
  stimulus: auditor asks for a decision's basis
  environment: normal
  response_measure: authority chain, pinned citations and claims as known at decision time returned; 100 % of decisions
  refines:
  - BRQ-003
```

</details>
