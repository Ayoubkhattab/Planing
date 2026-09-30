---
id: THREAT-MODEL-SLC07
type: threat-model
title: Threat Model — SLC-07 (STRIDE)
wave: W5
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Threat Model — SLC-07 (STRIDE)

## threats

_6 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S07-01 | Run execution | Elevation | run reads data beyond submitter's clearance using worker privileges | M | H | runs execute with delegated SecurityContext of submitter; PEP on every read | L |
| THR-S07-02 | Method image | Tampering | malicious or altered analysis image | L | H | digest-pinned images from internal registry; activation SoD; signature verification | L |
| THR-S07-03 | Reproduction | Info Disclosure | reproduction report reveals inputs hidden from reproducer | M | M | reproducer must be cleared for source run label | L |
| THR-S07-04 | Assessment | Tampering | published assessment silently edited | L | H | immutability; new versions only; decisions pin versions | L |
| THR-S07-05 | Citations | Info Disclosure | citation list reveals existence of compartmented evidence | M | M | withhold citations for uncleared readers; no markers by default | L |
| THR-S07-06 | Compute | DoS | one tenant exhausts compute | M | M | per-tenant quotas; fair scheduling; timeouts | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S07-01
  component: Run execution
  stride: Elevation
  threat: run reads data beyond submitter's clearance using worker privileges
  likelihood: M
  impact: H
  controls: runs execute with delegated SecurityContext of submitter; PEP on every read
  residual_risk: L
- id: THR-S07-02
  component: Method image
  stride: Tampering
  threat: malicious or altered analysis image
  likelihood: L
  impact: H
  controls: digest-pinned images from internal registry; activation SoD; signature verification
  residual_risk: L
- id: THR-S07-03
  component: Reproduction
  stride: Info Disclosure
  threat: reproduction report reveals inputs hidden from reproducer
  likelihood: M
  impact: M
  controls: reproducer must be cleared for source run label
  residual_risk: L
- id: THR-S07-04
  component: Assessment
  stride: Tampering
  threat: published assessment silently edited
  likelihood: L
  impact: H
  controls: immutability; new versions only; decisions pin versions
  residual_risk: L
- id: THR-S07-05
  component: Citations
  stride: Info Disclosure
  threat: citation list reveals existence of compartmented evidence
  likelihood: M
  impact: M
  controls: withhold citations for uncleared readers; no markers by default
  residual_risk: L
- id: THR-S07-06
  component: Compute
  stride: DoS
  threat: one tenant exhausts compute
  likelihood: M
  impact: M
  controls: per-tenant quotas; fair scheduling; timeouts
  residual_risk: L
```

</details>
