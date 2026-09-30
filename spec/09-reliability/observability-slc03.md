---
id: OBS-SLC03
type: observability
title: Observability — SLC-03
wave: W5
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Observability — SLC-03

## signals

_6 items_

| metric | type | alert |
|---|---|---|
| task.commands_total{command,outcome} | counter | rejection spike |
| task.overdue_total{unit} | gauge | trend |
| scheduler.lag_s | histogram | p95 > 60 s |
| eligibility.denied_total{reason} | counter | report |
| task.sod_rejections_total | counter | any spike → review |
| task.my_tasks_latency_ms | histogram | p95 > 500 ms |

## business_telemetry

- on-time completion rate (OUT-05)
- tasks linked to plan vs ad-hoc (REQ-OPS-010)
- rework rate
- mean time in each state

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: task.commands_total{command,outcome}
  type: counter
  alert: rejection spike
- metric: task.overdue_total{unit}
  type: gauge
  alert: trend
- metric: scheduler.lag_s
  type: histogram
  alert: p95 > 60 s
- metric: eligibility.denied_total{reason}
  type: counter
  alert: report
- metric: task.sod_rejections_total
  type: counter
  alert: any spike → review
- metric: task.my_tasks_latency_ms
  type: histogram
  alert: p95 > 500 ms
business_telemetry:
- on-time completion rate (OUT-05)
- tasks linked to plan vs ad-hoc (REQ-OPS-010)
- rework rate
- mean time in each state
```

</details>
