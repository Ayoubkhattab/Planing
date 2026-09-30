---
id: OBS-SLC14
type: observability
title: Observability — SLC-14
wave: W5
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Observability — SLC-14

## signals

_3 items_

| metric | type | alert |
|---|---|---|
| collection.match_lag_s | histogram | p95 > 30 s |
| collection.requirements_open{priority} | gauge | business |
| collection.expired_total | counter | trend |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: collection.match_lag_s
  type: histogram
  alert: p95 > 30 s
- metric: collection.requirements_open{priority}
  type: gauge
  alert: business
- metric: collection.expired_total
  type: counter
  alert: trend
```

</details>
