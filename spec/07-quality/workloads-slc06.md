---
id: WL-SLC06
type: workload-catalog
title: Workloads & Added Quality Scenarios — SLC-06
wave: W5
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Workloads & Added Quality Scenarios — SLC-06

## workloads

_4 items_

| id | name | derivation | basis | target |
|---|---|---|---|---|
| WL-06b | Membership evaluation | ≈ all location/observation events ≈ 5,500/s peak × situations intersecting (spatial index keeps it ≈ 1–3) | INF | QAS-PERF-006 |
| WL-06c | Alert evaluation | critical rules on ingestion stream ≈ 5,000/s | INF | QAS-PERF-005 |
| WL-03b | Tiles | map panning ≈ 20 tiles per view change; ≈ 2,000 tiles/s peak; hit rate depends on distinct scope hashes | INF | QAS-PERF-007 |
| WL-13a | Notifications | alerts × recipients ≈ 200/s; bursts 10,000 within 1 min | INF | REQ-COM-001 |

## added_quality_scenarios

_3 items_

| id | quality | stimulus | environment | response_measure | refines |
|---|---|---|---|---|---|
| QAS-PERF-019 | performance | situation picture read (≤ 2,000 visible members) | design load | p95 ≤ 1 s | BRQ-002 |
| QAS-SEC-012 | security | user not cleared for an alert's label | normal | receives no alert, notification, push or count change | BRQ-007 |
| QAS-OPS-003 | operability | push gateway unavailable (air-gapped) | field network | in-app inbox current; polling fallback ≤ 60 s | BRQ-004 |

## scalability_design

- evaluators partitioned by (tenant, geohash4 of object location)
- active situation extents in in-memory spatial index per partition, reloaded on EVT-SIT-*
- tile cache keyed by scope hash; distinct scopes per tenant expected < 50 (roles × levels)
- notification fan-out via subscription index; push per channel with backpressure

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-06b
  name: Membership evaluation
  derivation: ≈ all location/observation events ≈ 5,500/s peak × situations intersecting (spatial index keeps it ≈ 1–3)
  basis: INF
  target: QAS-PERF-006
- id: WL-06c
  name: Alert evaluation
  derivation: critical rules on ingestion stream ≈ 5,000/s
  basis: INF
  target: QAS-PERF-005
- id: WL-03b
  name: Tiles
  derivation: map panning ≈ 20 tiles per view change; ≈ 2,000 tiles/s peak; hit rate depends on distinct scope hashes
  basis: INF
  target: QAS-PERF-007
- id: WL-13a
  name: Notifications
  derivation: alerts × recipients ≈ 200/s; bursts 10,000 within 1 min
  basis: INF
  target: REQ-COM-001
added_quality_scenarios:
- id: QAS-PERF-019
  quality: performance
  stimulus: situation picture read (≤ 2,000 visible members)
  environment: design load
  response_measure: p95 ≤ 1 s
  refines:
  - BRQ-002
- id: QAS-SEC-012
  quality: security
  stimulus: user not cleared for an alert's label
  environment: normal
  response_measure: receives no alert, notification, push or count change
  refines:
  - BRQ-007
- id: QAS-OPS-003
  quality: operability
  stimulus: push gateway unavailable (air-gapped)
  environment: field network
  response_measure: in-app inbox current; polling fallback ≤ 60 s
  refines:
  - BRQ-004
scalability_design:
- evaluators partitioned by (tenant, geohash4 of object location)
- active situation extents in in-memory spatial index per partition, reloaded on EVT-SIT-*
- tile cache keyed by scope hash; distinct scopes per tenant expected < 50 (roles × levels)
- notification fan-out via subscription index; push per channel with backpressure
```

</details>
