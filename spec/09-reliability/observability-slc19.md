---
id: OBS-SLC19
type: observability
title: Observability — SLC-19
wave: W5
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
recalibrate_after_pilot: true
---

# Observability — SLC-19

## signals

_4 items_

| metric | type | alert |
|---|---|---|
| exercise.open_by_state{state} | gauge | business |
| exercise.abort_ratio | gauge | sustained increase → training program review (recalibrate after Pilot R1) |
| simulation.unevaluated_participant_count | gauge | > 0 while IN_PROGRESS past scheduled end → evaluator follow-up (operations signal — INV-SIM-02 already guarantees COMPLETED never hides this) |
| simulation.inject_delivery_latency_s | histogram | p95 > target (recalibrate after Pilot R1/R2) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: exercise.open_by_state{state}
  type: gauge
  alert: business
- metric: exercise.abort_ratio
  type: gauge
  alert: sustained increase → training program review (recalibrate after Pilot R1)
- metric: simulation.unevaluated_participant_count
  type: gauge
  alert: '> 0 while IN_PROGRESS past scheduled end → evaluator follow-up (operations signal — INV-SIM-02 already guarantees COMPLETED never hides this)'
- metric: simulation.inject_delivery_latency_s
  type: histogram
  alert: p95 > target (recalibrate after Pilot R1/R2)
```

</details>
