---
id: OBS-SLC11
type: observability
title: Observability — SLC-11
wave: W5
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Observability — SLC-11

## signals

_7 items_

| metric | type | alert |
|---|---|---|
| sync.session_duration_s | histogram | p95 > 600 s |
| sync.queue_depth | gauge | storm alert |
| sync.conflict_ratio | gauge | > 5 % of commands |
| sync.clock_offset_s | histogram | \|offset\| > 300 s share > 2 % |
| devices.lost_total | counter | security review |
| packages.revoked_total | counter | trend |
| sync.signature_failures_total | counter | any = security incident |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: sync.session_duration_s
  type: histogram
  alert: p95 > 600 s
- metric: sync.queue_depth
  type: gauge
  alert: storm alert
- metric: sync.conflict_ratio
  type: gauge
  alert: '> 5 % of commands'
- metric: sync.clock_offset_s
  type: histogram
  alert: '|offset| > 300 s share > 2 %'
- metric: devices.lost_total
  type: counter
  alert: security review
- metric: packages.revoked_total
  type: counter
  alert: trend
- metric: sync.signature_failures_total
  type: counter
  alert: any = security incident
```

</details>
