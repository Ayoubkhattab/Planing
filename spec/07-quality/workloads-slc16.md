---
id: WL-SLC16
type: workload-catalog
title: Workloads — SLC-16
wave: W5
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Workloads — SLC-16

## workloads

_3 items_

| id | name | derivation | target |
|---|---|---|---|
| WL-06e | Sensor streams | up to WL-06a (5,000 readings/s sustained per cell) | QAS-PERF-012 |
| WL-05b | ERP/HRIS/DMS batches | nightly + intraday deltas; ≤ 1e6 records/day per tenant | QAS-INT-001 |
| WL-13c | CAP outbound | ≤ alerts marked releasable; low | release ≤ 2 min after decision |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-06e
  name: Sensor streams
  derivation: up to WL-06a (5,000 readings/s sustained per cell)
  target: QAS-PERF-012
- id: WL-05b
  name: ERP/HRIS/DMS batches
  derivation: nightly + intraday deltas; ≤ 1e6 records/day per tenant
  target: QAS-INT-001
- id: WL-13c
  name: CAP outbound
  derivation: ≤ alerts marked releasable; low
  target: release ≤ 2 min after decision
```

</details>
