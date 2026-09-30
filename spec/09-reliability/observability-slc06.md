---
id: OBS-SLC06
type: observability
title: Observability — SLC-06
wave: W5
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Observability — SLC-06

## signals

_7 items_

| metric | type | alert |
|---|---|---|
| alert.e2e_latency_s{severity} | histogram | critical p95 > 5 s |
| membership.lag_s | histogram | p95 > 10 s |
| tiles.latency_ms | histogram | p95 > 500 ms |
| tiles.cache_hit_ratio{scope} | gauge | < 50 % sustained |
| notifications.withheld_total | counter | trend (revocations) |
| notifications.failed_total{channel} | counter | > 1 % |
| alerts.storm_rate{rule} | gauge | > rate limit |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: alert.e2e_latency_s{severity}
  type: histogram
  alert: critical p95 > 5 s
- metric: membership.lag_s
  type: histogram
  alert: p95 > 10 s
- metric: tiles.latency_ms
  type: histogram
  alert: p95 > 500 ms
- metric: tiles.cache_hit_ratio{scope}
  type: gauge
  alert: < 50 % sustained
- metric: notifications.withheld_total
  type: counter
  alert: trend (revocations)
- metric: notifications.failed_total{channel}
  type: counter
  alert: '> 1 %'
- metric: alerts.storm_rate{rule}
  type: gauge
  alert: '> rate limit'
```

</details>
