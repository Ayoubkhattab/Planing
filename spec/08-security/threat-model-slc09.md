---
id: THREAT-MODEL-SLC09
type: threat-model
title: Threat Model — SLC-09
wave: W5
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Threat Model — SLC-09

## threats

_4 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S09-01 | Allocation | Elevation | self-approval or pre-emption without authority | M | H | SoD; decision-backed pre-emption | L |
| THR-S09-02 | Asset custody | Repudiation | holder denies receiving an asset | L | M | gapless custody chain with actor and time; condition reports | L |
| THR-S09-03 | Availability | Info Disclosure | availability reveals hidden tasks holding assets | M | M | blocking reasons shown only if the blocking object is visible; otherwise 'unavailable' | L |
| THR-S09-04 | Capacity ledger | Tampering | direct ledger edits bypass commitments | L | H | ledger writable only by allocation handlers (DB role); reconciliation job | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S09-01
  component: Allocation
  stride: Elevation
  threat: self-approval or pre-emption without authority
  likelihood: M
  impact: H
  controls: SoD; decision-backed pre-emption
  residual_risk: L
- id: THR-S09-02
  component: Asset custody
  stride: Repudiation
  threat: holder denies receiving an asset
  likelihood: L
  impact: M
  controls: gapless custody chain with actor and time; condition reports
  residual_risk: L
- id: THR-S09-03
  component: Availability
  stride: Info Disclosure
  threat: availability reveals hidden tasks holding assets
  likelihood: M
  impact: M
  controls: blocking reasons shown only if the blocking object is visible; otherwise 'unavailable'
  residual_risk: L
- id: THR-S09-04
  component: Capacity ledger
  stride: Tampering
  threat: direct ledger edits bypass commitments
  likelihood: L
  impact: H
  controls: ledger writable only by allocation handlers (DB role); reconciliation job
  residual_risk: L
```

</details>
