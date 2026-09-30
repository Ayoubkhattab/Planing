---
id: WL-SLC03
type: workload-catalog
title: Workloads & Added Quality Scenarios — SLC-03
wave: W5
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Workloads & Added Quality Scenarios — SLC-03

## workloads

_3 items_

| id | name | derivation | basis | target |
|---|---|---|---|---|
| WL-01i | Task commands | ≈ 100/s peak; offline replay bursts ≤ 1,000 commands per device reconnect | INF | QAS-PERF-001 |
| WL-01j | My-tasks reads | ≈ 300/s peak | INF | QAS-PERF-016 |
| WL-01k | Scheduler timers | ≤ 1e6 active tasks × 2 timers | INF | QAS-OPS-002 |

## added_quality_scenarios

_3 items_

| id | quality | stimulus | environment | response_measure | refines |
|---|---|---|---|---|---|
| QAS-PERF-016 | performance | field user opens 'my tasks' | design load | p95 ≤ 500 ms | BRQ-004 |
| QAS-OPS-002 | timeliness | task reaches due_at | normal | escalation event ≤ 60 s after due | BRQ-004 |
| QAS-PERF-017 | performance | assignment with eligibility check | normal | p95 ≤ 500 ms including BC05 call | BRQ-004 |

## scalability_design

- index (tenant, assignee, state, due_at) for my-tasks
- timers stored as due buckets (minute granularity), partitioned by tenant; scheduler workers claim buckets with leases
- eligibility results cached ≤ 5 min keyed by (person, task_type version, qualification security version)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-01i
  name: Task commands
  derivation: ≈ 100/s peak; offline replay bursts ≤ 1,000 commands per device reconnect
  basis: INF
  target: QAS-PERF-001
- id: WL-01j
  name: My-tasks reads
  derivation: ≈ 300/s peak
  basis: INF
  target: QAS-PERF-016
- id: WL-01k
  name: Scheduler timers
  derivation: ≤ 1e6 active tasks × 2 timers
  basis: INF
  target: QAS-OPS-002
added_quality_scenarios:
- id: QAS-PERF-016
  quality: performance
  stimulus: field user opens 'my tasks'
  environment: design load
  response_measure: p95 ≤ 500 ms
  refines:
  - BRQ-004
- id: QAS-OPS-002
  quality: timeliness
  stimulus: task reaches due_at
  environment: normal
  response_measure: escalation event ≤ 60 s after due
  refines:
  - BRQ-004
- id: QAS-PERF-017
  quality: performance
  stimulus: assignment with eligibility check
  environment: normal
  response_measure: p95 ≤ 500 ms including BC05 call
  refines:
  - BRQ-004
scalability_design:
- index (tenant, assignee, state, due_at) for my-tasks
- timers stored as due buckets (minute granularity), partitioned by tenant; scheduler workers claim buckets with leases
- eligibility results cached ≤ 5 min keyed by (person, task_type version, qualification security version)
```

</details>
