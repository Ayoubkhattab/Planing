---
id: OBS-SLC07
type: observability
title: Observability — SLC-07
wave: W5
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Observability — SLC-07

## signals

_6 items_

| metric | type | alert |
|---|---|---|
| runs.queue_wait_s{tenant} | histogram | p95 > 30 s |
| runs.duration_s{method} | histogram | trend |
| runs.failed_ratio{method} | gauge | > 5 % |
| reproductions.different_ratio{method} | gauge | any for deterministic methods = P1 |
| assessments.published_total | counter | business |
| compute.utilization{tenant} | gauge | quota saturation |

## business_telemetry

- share of assessments with full lineage (OUT-03 target 100 %)
- reproducibility rate (OUT-03 target 100 % deterministic)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: runs.queue_wait_s{tenant}
  type: histogram
  alert: p95 > 30 s
- metric: runs.duration_s{method}
  type: histogram
  alert: trend
- metric: runs.failed_ratio{method}
  type: gauge
  alert: '> 5 %'
- metric: reproductions.different_ratio{method}
  type: gauge
  alert: any for deterministic methods = P1
- metric: assessments.published_total
  type: counter
  alert: business
- metric: compute.utilization{tenant}
  type: gauge
  alert: quota saturation
business_telemetry:
- share of assessments with full lineage (OUT-03 target 100 %)
- reproducibility rate (OUT-03 target 100 % deterministic)
```

</details>
