---
id: THREAT-MODEL-SLC18
type: threat-model
title: Threat Model — SLC-18
wave: W5
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
recalibrate_after_pilot: true
---

# Threat Model — SLC-18

## threats

_5 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S18-01 | Logistics Request ↔ Allocation linkage (CR-62) | Tampering | a logistics request forced into APPROVED directly, bypassing the linked allocation's own commitment check | L | H | no human command sets APPROVED; only SYS: transitions driven by SLC-09's own EVT-ALC-COMMITTED (INV-LGR-01); commitment still runs the unchanged SPEC-ALLOCATION §1 checks and capacity-ledger constraint | L |
| THR-S18-02 | Delivery quantity | Repudiation | a shipment marked delivered in full when the quantity actually received was short, hiding a loss | M | M | delivered_quantity is a required, explicit field on CMD-SHP-DELIVER; INV-SHP-02/INV-LGR-03 force PARTIALLY_FULFILLED whenever less than requested arrives — no state hides a shortfall | L |
| THR-S18-03 | Dispatch vs. capacity ledger | Elevation | a shipment dispatched for a quantity never actually reserved, bypassing SLC-09's contention and pre-emption rules | M | H | INV-SHP-03 requires the linked allocation still COMMITTED for at least the shipped quantity at departure; CMD-SHP-PLAN's guard checks the same ledger SLC-09 already enforces — no second, weaker capacity check exists | L |
| THR-S18-04 | Movement checkpoints | Tampering | a checkpoint inserted out of order or edited, obscuring where or when a shipment actually was | L | M | checkpoints are append-only and must be strictly after the previous one (INV-SHP-01), mirroring AGG-ASSET's gapless custody chain; no edit or delete command exists | L |
| THR-S18-05 | Cancellation mid-transit | Repudiation | a shipment cancelled while IN_TRANSIT to make an in-flight loss disappear without a DAMAGED/LOST record | L | M | CMD-SHP-CANCEL is only accepted from PLANNED (INV-SHP-04); once IN_TRANSIT the only terminal outcomes are DELIVERED, DAMAGED or LOST, each with its own guard and event | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S18-01
  component: Logistics Request ↔ Allocation linkage (CR-62)
  stride: Tampering
  threat: a logistics request forced into APPROVED directly, bypassing the linked allocation's own commitment check
  likelihood: L
  impact: H
  controls: no human command sets APPROVED; only SYS: transitions driven by SLC-09's own EVT-ALC-COMMITTED (INV-LGR-01); commitment still runs the unchanged SPEC-ALLOCATION §1 checks and capacity-ledger constraint
  residual_risk: L
- id: THR-S18-02
  component: Delivery quantity
  stride: Repudiation
  threat: a shipment marked delivered in full when the quantity actually received was short, hiding a loss
  likelihood: M
  impact: M
  controls: delivered_quantity is a required, explicit field on CMD-SHP-DELIVER; INV-SHP-02/INV-LGR-03 force PARTIALLY_FULFILLED whenever less than requested arrives — no state hides a shortfall
  residual_risk: L
- id: THR-S18-03
  component: Dispatch vs. capacity ledger
  stride: Elevation
  threat: a shipment dispatched for a quantity never actually reserved, bypassing SLC-09's contention and pre-emption rules
  likelihood: M
  impact: H
  controls: INV-SHP-03 requires the linked allocation still COMMITTED for at least the shipped quantity at departure; CMD-SHP-PLAN's guard checks the same ledger SLC-09 already enforces — no second, weaker capacity check exists
  residual_risk: L
- id: THR-S18-04
  component: Movement checkpoints
  stride: Tampering
  threat: a checkpoint inserted out of order or edited, obscuring where or when a shipment actually was
  likelihood: L
  impact: M
  controls: checkpoints are append-only and must be strictly after the previous one (INV-SHP-01), mirroring AGG-ASSET's gapless custody chain; no edit or delete command exists
  residual_risk: L
- id: THR-S18-05
  component: Cancellation mid-transit
  stride: Repudiation
  threat: a shipment cancelled while IN_TRANSIT to make an in-flight loss disappear without a DAMAGED/LOST record
  likelihood: L
  impact: M
  controls: CMD-SHP-CANCEL is only accepted from PLANNED (INV-SHP-04); once IN_TRANSIT the only terminal outcomes are DELIVERED, DAMAGED or LOST, each with its own guard and event
  residual_risk: L
```

</details>
