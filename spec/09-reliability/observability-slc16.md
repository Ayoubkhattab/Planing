---
id: OBS-SLC16
type: observability
title: Observability — SLC-16
wave: W5
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Observability — SLC-16

## signals

_5 items_

| metric | type | alert |
|---|---|---|
| integration.backlog_age_s{connection} | gauge | > 1 h |
| sensors.stale_streams | gauge | any |
| sensors.quality_violations{stream} | counter | trend |
| hr.proposals_pending{kind} | gauge | leave > 24 h |
| cap.failed_total | counter | any |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: integration.backlog_age_s{connection}
  type: gauge
  alert: '> 1 h'
- metric: sensors.stale_streams
  type: gauge
  alert: any
- metric: sensors.quality_violations{stream}
  type: counter
  alert: trend
- metric: hr.proposals_pending{kind}
  type: gauge
  alert: leave > 24 h
- metric: cap.failed_total
  type: counter
  alert: any
```

</details>
