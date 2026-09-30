---
id: OBS-SLC05
type: observability
title: Observability — SLC-05
wave: W5
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Observability — SLC-05

## signals

_7 items_

| metric | type | alert |
|---|---|---|
| projection.lag_s{kind} | histogram | p95 > 30 s; DEGRADED > 5 min |
| search.latency_ms | histogram | p95 > 1 s |
| labelcheck.drop_ratio | gauge | > 1 % (indicates stale index or revocations) |
| labelcheck.latency_ms{owner} | histogram | p95 > 20 ms |
| reconciliation.mismatch_ratio | gauge | > 0.01 % |
| graph.latency_ms{op} | histogram | p95 > 1 s |
| inference_suite.failures | counter | any = P0 |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: projection.lag_s{kind}
  type: histogram
  alert: p95 > 30 s; DEGRADED > 5 min
- metric: search.latency_ms
  type: histogram
  alert: p95 > 1 s
- metric: labelcheck.drop_ratio
  type: gauge
  alert: '> 1 % (indicates stale index or revocations)'
- metric: labelcheck.latency_ms{owner}
  type: histogram
  alert: p95 > 20 ms
- metric: reconciliation.mismatch_ratio
  type: gauge
  alert: '> 0.01 %'
- metric: graph.latency_ms{op}
  type: histogram
  alert: p95 > 1 s
- metric: inference_suite.failures
  type: counter
  alert: any = P0
```

</details>
