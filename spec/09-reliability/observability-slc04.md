---
id: OBS-SLC04
type: observability
title: Observability — SLC-04
wave: W5
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Observability — SLC-04

## signals

_7 items_

| metric | type | alert |
|---|---|---|
| cnf.detect_lag_s | histogram | p95 > 30 s |
| cnf.open_total{predicate} | gauge | trend alert |
| er.candidate_lag_s | histogram | p95 > 60 s |
| er.queue_size{entity_type} | gauge | > 5,000 pending |
| er.split_rate | gauge | > 5 % of matches in 30 d → ruleset review |
| er.cluster_size_max | gauge | > 50 |
| cluster.reconciliation_diff | gauge | any > 0 = P1 |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: cnf.detect_lag_s
  type: histogram
  alert: p95 > 30 s
- metric: cnf.open_total{predicate}
  type: gauge
  alert: trend alert
- metric: er.candidate_lag_s
  type: histogram
  alert: p95 > 60 s
- metric: er.queue_size{entity_type}
  type: gauge
  alert: '> 5,000 pending'
- metric: er.split_rate
  type: gauge
  alert: '> 5 % of matches in 30 d → ruleset review'
- metric: er.cluster_size_max
  type: gauge
  alert: '> 50'
- metric: cluster.reconciliation_diff
  type: gauge
  alert: any > 0 = P1
```

</details>
