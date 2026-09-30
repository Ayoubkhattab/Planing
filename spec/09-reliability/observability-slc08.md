---
id: OBS-SLC08
type: observability
title: Observability — SLC-08
wave: W5
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Observability — SLC-08

## signals

_6 items_

| metric | type | alert |
|---|---|---|
| decisions.recorded_total{type} | counter | business |
| decisions.authority_denied_total | counter | spike review |
| plans.sync_duration_s | histogram | p95 > 60 s |
| plans.sync_mismatch | gauge | > 0 after 5 min |
| plans.major_changes_per_plan | gauge | report |
| outcomes.on_track_ratio | gauge | business (OUT-05) |

## business_telemetry

- decisions with ≥ 1 citation (OUT-04 = 100 %)
- decision cycle time (request open → decided)
- tasks linked to plan (REQ-OPS-010)
- outcome progress vs target

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: decisions.recorded_total{type}
  type: counter
  alert: business
- metric: decisions.authority_denied_total
  type: counter
  alert: spike review
- metric: plans.sync_duration_s
  type: histogram
  alert: p95 > 60 s
- metric: plans.sync_mismatch
  type: gauge
  alert: '> 0 after 5 min'
- metric: plans.major_changes_per_plan
  type: gauge
  alert: report
- metric: outcomes.on_track_ratio
  type: gauge
  alert: business (OUT-05)
business_telemetry:
- decisions with ≥ 1 citation (OUT-04 = 100 %)
- decision cycle time (request open → decided)
- tasks linked to plan (REQ-OPS-010)
- outcome progress vs target
```

</details>
