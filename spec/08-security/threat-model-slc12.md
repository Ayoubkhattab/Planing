---
id: THREAT-MODEL-SLC12
type: threat-model
title: Threat Model — SLC-12
wave: W5
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Threat Model — SLC-12

## threats

_5 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S12-P1 | Product | Info Disclosure | product includes content above its label or reveals exclusions | M | H | label filter on every binding; no exclusion counts (QAS-PRD-002) | L |
| THR-S12-P2 | Distribution | Info Disclosure | leaked copy cannot be traced | M | H | per-recipient visible + invisible watermark | M |
| THR-S12-P3 | Template | Tampering | template binding reads data outside the author's authority | L | H | bindings only to declared queries executed as the author | L |
| THR-S12-P4 | Archive | Tampering | silent corruption or alteration of archived records | L | H | fixity at ingest/retrieval/yearly; WORM; replica repair | L |
| THR-S12-P5 | Reconstruction | Info Disclosure | reconstruction reveals hidden elements | M | H | runs with requester authority; hidden elements absent | L |

## accepted_residual_risks

- THR-S12-P2 (M): watermarks deter and trace but cannot prevent photographing a screen

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S12-P1
  component: Product
  stride: Info Disclosure
  threat: product includes content above its label or reveals exclusions
  likelihood: M
  impact: H
  controls: label filter on every binding; no exclusion counts (QAS-PRD-002)
  residual_risk: L
- id: THR-S12-P2
  component: Distribution
  stride: Info Disclosure
  threat: leaked copy cannot be traced
  likelihood: M
  impact: H
  controls: per-recipient visible + invisible watermark
  residual_risk: M
- id: THR-S12-P3
  component: Template
  stride: Tampering
  threat: template binding reads data outside the author's authority
  likelihood: L
  impact: H
  controls: bindings only to declared queries executed as the author
  residual_risk: L
- id: THR-S12-P4
  component: Archive
  stride: Tampering
  threat: silent corruption or alteration of archived records
  likelihood: L
  impact: H
  controls: fixity at ingest/retrieval/yearly; WORM; replica repair
  residual_risk: L
- id: THR-S12-P5
  component: Reconstruction
  stride: Info Disclosure
  threat: reconstruction reveals hidden elements
  likelihood: M
  impact: H
  controls: runs with requester authority; hidden elements absent
  residual_risk: L
accepted_residual_risks:
- 'THR-S12-P2 (M): watermarks deter and trace but cannot prevent photographing a screen'
```

</details>
