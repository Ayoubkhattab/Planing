---
id: WL-SLC15
type: workload-catalog
title: Workloads — SLC-15
wave: W5
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Workloads — SLC-15

## workloads

_2 items_

| id | name | derivation | target |
|---|---|---|---|
| WL-07a | Correlation candidates | per validated observation / position claim ≈ ≤ 500/s; bounded by 9 spatial × 3 time buckets | proposal ≤ 60 s after input |
| WL-01s | Coordination commands | low (≤ 1/s) | QAS-PERF-001 |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-07a
  name: Correlation candidates
  derivation: per validated observation / position claim ≈ ≤ 500/s; bounded by 9 spatial × 3 time buckets
  target: proposal ≤ 60 s after input
- id: WL-01s
  name: Coordination commands
  derivation: low (≤ 1/s)
  target: QAS-PERF-001
```

</details>
