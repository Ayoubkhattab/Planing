---
id: WL-SLC09
type: workload-catalog
title: Workloads — SLC-09 (recalibrate after R1 pilot)
wave: W5
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Workloads — SLC-09 (recalibrate after R1 pilot)

## workloads

_3 items_

| id | name | derivation | target |
|---|---|---|---|
| WL-01p | Availability queries | planning screens ≈ 20/s; 1,000 assets × 30 days | QAS-RES-002 |
| WL-01q | Allocation requests | ≈ ≤ 5/s; bursts at plan baseline (≤ 500) | QAS-RES-001; ordering window 250 ms |
| WL-01r | Readiness checks | ≈ 10/s | p95 ≤ 500 ms |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-01p
  name: Availability queries
  derivation: planning screens ≈ 20/s; 1,000 assets × 30 days
  target: QAS-RES-002
- id: WL-01q
  name: Allocation requests
  derivation: ≈ ≤ 5/s; bursts at plan baseline (≤ 500)
  target: QAS-RES-001; ordering window 250 ms
- id: WL-01r
  name: Readiness checks
  derivation: ≈ 10/s
  target: p95 ≤ 500 ms
```

</details>
