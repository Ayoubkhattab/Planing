---
id: THREAT-MODEL-SLC15
type: threat-model
title: Threat Model — SLC-15
wave: W5
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Threat Model — SLC-15

## threats

_4 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S15-01 | Coordination | Info Disclosure | participant sees another organization's sensitive parts | M | H | per-participant access scope + label rule (INV-CRD-02) | L |
| THR-S15-02 | Coordination | Elevation | action executed without the owning organization's authority | M | H | INV-CRD-03 decision-gated responsibilities | L |
| THR-S15-03 | Fusion | Tampering | one source counted twice to fake corroboration | M | M | independence via lineage (INV-CRP-04) | L |
| THR-S15-04 | Correlation queue | Info Disclosure | proposal reveals hidden inputs | M | H | proposal visible only to reviewers cleared for all inputs | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S15-01
  component: Coordination
  stride: Info Disclosure
  threat: participant sees another organization's sensitive parts
  likelihood: M
  impact: H
  controls: per-participant access scope + label rule (INV-CRD-02)
  residual_risk: L
- id: THR-S15-02
  component: Coordination
  stride: Elevation
  threat: action executed without the owning organization's authority
  likelihood: M
  impact: H
  controls: INV-CRD-03 decision-gated responsibilities
  residual_risk: L
- id: THR-S15-03
  component: Fusion
  stride: Tampering
  threat: one source counted twice to fake corroboration
  likelihood: M
  impact: M
  controls: independence via lineage (INV-CRP-04)
  residual_risk: L
- id: THR-S15-04
  component: Correlation queue
  stride: Info Disclosure
  threat: proposal reveals hidden inputs
  likelihood: M
  impact: H
  controls: proposal visible only to reviewers cleared for all inputs
  residual_risk: L
```

</details>
