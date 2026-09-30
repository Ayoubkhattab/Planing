---
id: FMEA-SLC10
type: fmea
title: Failure Mode Analysis — SLC-10
wave: W5
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Failure Mode Analysis — SLC-10

## failure_modes

_4 items_

### FM-S10-01

- **component:** Inference server
- **failure:** unavailable
- **cause:** GPU/node failure
- **effect:** AI features unavailable
- **detection:** health
- **severity:** M
- **likelihood:** M
- **prevention:** replicas per cell
- **mitigation_recovery:** platform works without AI (AI is assistive)
- **data_loss:** none
- **user_impact:** no AI assistance
- **dependency_impact:** —

### FM-S10-02

- **component:** Verifier model
- **failure:** unavailable
- **cause:** failure
- **effect:** cannot check grounding
- **detection:** health
- **severity:** M
- **likelihood:** L
- **prevention:** HA
- **mitigation_recovery:** fail-closed: requests end INSUFFICIENT_EVIDENCE
- **data_loss:** none
- **user_impact:** no answers
- **dependency_impact:** —

### FM-S10-03

- **component:** Vector projection
- **failure:** lag
- **cause:** embedding backlog
- **effect:** recent facts not retrievable
- **detection:** lag metric
- **severity:** L
- **likelihood:** M
- **prevention:** scaled embedding workers
- **mitigation_recovery:** answers may be insufficient; search still works
- **data_loss:** none
- **user_impact:** stale context
- **dependency_impact:** —

### FM-S10-04

- **component:** Model drift
- **failure:** quality drop
- **cause:** data shift
- **effect:** more hallucinations
- **detection:** weekly evaluation sample
- **severity:** H
- **likelihood:** M
- **prevention:** drift monitoring
- **mitigation_recovery:** rollback via CMD-MDL-REINSTATE
- **data_loss:** none
- **user_impact:** lower quality
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S10-01
  component: Inference server
  failure: unavailable
  cause: GPU/node failure
  effect: AI features unavailable
  detection: health
  severity: M
  likelihood: M
  prevention: replicas per cell
  mitigation_recovery: platform works without AI (AI is assistive)
  data_loss: none
  user_impact: no AI assistance
  dependency_impact: —
- id: FM-S10-02
  component: Verifier model
  failure: unavailable
  cause: failure
  effect: cannot check grounding
  detection: health
  severity: M
  likelihood: L
  prevention: HA
  mitigation_recovery: 'fail-closed: requests end INSUFFICIENT_EVIDENCE'
  data_loss: none
  user_impact: no answers
  dependency_impact: —
- id: FM-S10-03
  component: Vector projection
  failure: lag
  cause: embedding backlog
  effect: recent facts not retrievable
  detection: lag metric
  severity: L
  likelihood: M
  prevention: scaled embedding workers
  mitigation_recovery: answers may be insufficient; search still works
  data_loss: none
  user_impact: stale context
  dependency_impact: —
- id: FM-S10-04
  component: Model drift
  failure: quality drop
  cause: data shift
  effect: more hallucinations
  detection: weekly evaluation sample
  severity: H
  likelihood: M
  prevention: drift monitoring
  mitigation_recovery: rollback via CMD-MDL-REINSTATE
  data_loss: none
  user_impact: lower quality
  dependency_impact: —
```

</details>
