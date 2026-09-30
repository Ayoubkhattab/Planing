---
id: OBS-SLC17
type: observability
title: Observability — SLC-17
wave: W5
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
recalibrate_after_pilot: true
---

# Observability — SLC-17

## signals

_4 items_

| metric | type | alert |
|---|---|---|
| incident.open_by_severity{severity} | gauge | business |
| incident.response_dispatch_latency_s | histogram | p95 > SLA (recalibrate after Pilot R1/R2) |
| incident.sla_breached_total | counter | any increment → page commander (CRISIS/EMERGENCY only) |
| risk.treated_without_action_ratio | gauge | > 0 → governance review (should always be 0 by INV-RIS-03) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: incident.open_by_severity{severity}
  type: gauge
  alert: business
- metric: incident.response_dispatch_latency_s
  type: histogram
  alert: p95 > SLA (recalibrate after Pilot R1/R2)
- metric: incident.sla_breached_total
  type: counter
  alert: any increment → page commander (CRISIS/EMERGENCY only)
- metric: risk.treated_without_action_ratio
  type: gauge
  alert: '> 0 → governance review (should always be 0 by INV-RIS-03)'
```

</details>
