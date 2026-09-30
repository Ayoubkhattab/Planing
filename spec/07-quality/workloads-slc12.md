---
id: WL-SLC12
type: workload-catalog
title: Workloads — SLC-12 (recalibrate after R1 pilot)
wave: W5
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Workloads — SLC-12 (recalibrate after R1 pilot)

## workloads

_4 items_

| id | name | derivation | target |
|---|---|---|---|
| WL-13b | Product generation | ≈ 50–200 products/day per tenant; bursts at shift briefings | QAS-PRD-001 |
| WL-14d | Archive ingest | driven by disposition runs (daily); size = bucket volume | ingest ≤ 24 h per run |
| WL-14e | Archive retrieval | low (≤ 100/day) | QAS-ARC-001 |
| WL-04b | Reconstructions | low (≤ 20/day), heavy | async; ≤ 1 h for a plan-sized scope |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-13b
  name: Product generation
  derivation: ≈ 50–200 products/day per tenant; bursts at shift briefings
  target: QAS-PRD-001
- id: WL-14d
  name: Archive ingest
  derivation: driven by disposition runs (daily); size = bucket volume
  target: ingest ≤ 24 h per run
- id: WL-14e
  name: Archive retrieval
  derivation: low (≤ 100/day)
  target: QAS-ARC-001
- id: WL-04b
  name: Reconstructions
  derivation: low (≤ 20/day), heavy
  target: async; ≤ 1 h for a plan-sized scope
```

</details>
