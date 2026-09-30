---
id: OBS-SLC18
type: observability
title: Observability — SLC-18
wave: W5
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
recalibrate_after_pilot: true
---

# Observability — SLC-18

## signals

_4 items_

| metric | type | alert |
|---|---|---|
| logistics_request.open_by_state{state} | gauge | business |
| logistics_request.fulfillment_ratio | gauge | below target → supply chain review (recalibrate after Pilot R2) |
| shipment.transit_duration_s | histogram | p95 > target (recalibrate after Pilot R1/R2) |
| shipment.partial_delivery_ratio | gauge | sustained increase → logistics review (an operations signal, not a defect signal — INV-SHP-02 already guarantees the ratio is never hidden) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: logistics_request.open_by_state{state}
  type: gauge
  alert: business
- metric: logistics_request.fulfillment_ratio
  type: gauge
  alert: below target → supply chain review (recalibrate after Pilot R2)
- metric: shipment.transit_duration_s
  type: histogram
  alert: p95 > target (recalibrate after Pilot R1/R2)
- metric: shipment.partial_delivery_ratio
  type: gauge
  alert: sustained increase → logistics review (an operations signal, not a defect signal — INV-SHP-02 already guarantees the ratio is never hidden)
```

</details>
