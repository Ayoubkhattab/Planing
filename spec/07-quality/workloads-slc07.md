---
id: WL-SLC07
type: workload-catalog
title: Workloads & Added Quality Scenarios — SLC-07
wave: W5
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Workloads & Added Quality Scenarios — SLC-07

## workloads

_3 items_

| id | name | derivation | basis | target |
|---|---|---|---|---|
| WL-11b | Analysis runs | ≈ 1–5 runs/s submitted; duration seconds to hours; concurrent jobs per tenant by quota | INF | start ≤ 30 s; QAS-PERF-020 |
| WL-11c | Run artifacts | ≈ 10–500 MB per raster-heavy run; stored as COG / Parquet-like tables in object storage | INF | direct transfer (SR-05) |
| WL-01l | Assessment reads | ≈ 50/s | INF | QAS-PERF-002 |

## added_quality_scenarios

_2 items_

| id | quality | stimulus | environment | response_measure | refines |
|---|---|---|---|---|---|
| QAS-PERF-020 | fairness | tenant submits 100 runs | shared compute pool | no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s | BRQ-003 |
| QAS-SEC-013 | security | run submitted by user U | normal | run reads only data visible to U; results labelled ≥ max input label | BRQ-007 |

## scalability_design

- compute workers stateless; horizontal scale; per-tenant queues with weighted fair scheduling
- inputs streamed by partition (time/space) — no full-dataset loads into memory for raster methods (tile-wise processing)
- artifacts content-addressed; identical re-runs dedupe storage

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-11b
  name: Analysis runs
  derivation: ≈ 1–5 runs/s submitted; duration seconds to hours; concurrent jobs per tenant by quota
  basis: INF
  target: start ≤ 30 s; QAS-PERF-020
- id: WL-11c
  name: Run artifacts
  derivation: ≈ 10–500 MB per raster-heavy run; stored as COG / Parquet-like tables in object storage
  basis: INF
  target: direct transfer (SR-05)
- id: WL-01l
  name: Assessment reads
  derivation: ≈ 50/s
  basis: INF
  target: QAS-PERF-002
added_quality_scenarios:
- id: QAS-PERF-020
  quality: fairness
  stimulus: tenant submits 100 runs
  environment: shared compute pool
  response_measure: no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s
  refines:
  - BRQ-003
- id: QAS-SEC-013
  quality: security
  stimulus: run submitted by user U
  environment: normal
  response_measure: run reads only data visible to U; results labelled ≥ max input label
  refines:
  - BRQ-007
scalability_design:
- compute workers stateless; horizontal scale; per-tenant queues with weighted fair scheduling
- inputs streamed by partition (time/space) — no full-dataset loads into memory for raster methods (tile-wise processing)
- artifacts content-addressed; identical re-runs dedupe storage
```

</details>
