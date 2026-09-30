---
id: OBS-SLC09
type: observability
title: Observability — SLC-09
wave: W5
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Observability — SLC-09

## signals

_5 items_

| metric | type | alert |
|---|---|---|
| allocation.rejections_total{reason} | counter | capacity rejection spike |
| ledger.reconciliation_diff | gauge | any > 0 = P1 |
| availability.view_lag_s | histogram | p95 > 30 s |
| assets.unserviceable_ratio{type} | gauge | report |
| certifications.expiring_30d | gauge | report |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: allocation.rejections_total{reason}
  type: counter
  alert: capacity rejection spike
- metric: ledger.reconciliation_diff
  type: gauge
  alert: any > 0 = P1
- metric: availability.view_lag_s
  type: histogram
  alert: p95 > 30 s
- metric: assets.unserviceable_ratio{type}
  type: gauge
  alert: report
- metric: certifications.expiring_30d
  type: gauge
  alert: report
```

</details>
