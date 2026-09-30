---
id: THREAT-MODEL-SLC08
type: threat-model
title: Threat Model — SLC-08 (STRIDE)
wave: W5
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Threat Model — SLC-08 (STRIDE)

## threats

_6 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S08-01 | Decision | Elevation | decision recorded without competent authority | M | H | AuthorityCheck at record time, fail-closed; snapshot stored | L |
| THR-S08-02 | Decision | Repudiation | decider denies the basis | L | H | pinned citations; basis query; MFA; audit | L |
| THR-S08-03 | Plan version | Tampering | baseline changed after approval | L | H | immutability; minor amendments as annotations only | L |
| THR-S08-04 | Plan approval | Elevation | author approves own plan | M | H | SoD + authority check | L |
| THR-S08-05 | Decision request | Info Disclosure | citations above request label exposed | M | M | CITATION_ABOVE_LABEL guard; withheld per reader | L |
| THR-S08-06 | Task sync | Tampering | sync creates tasks outside plan scope | L | M | sync identity limited to plan's org scope; activities' scopes ⊆ plan scope | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S08-01
  component: Decision
  stride: Elevation
  threat: decision recorded without competent authority
  likelihood: M
  impact: H
  controls: AuthorityCheck at record time, fail-closed; snapshot stored
  residual_risk: L
- id: THR-S08-02
  component: Decision
  stride: Repudiation
  threat: decider denies the basis
  likelihood: L
  impact: H
  controls: pinned citations; basis query; MFA; audit
  residual_risk: L
- id: THR-S08-03
  component: Plan version
  stride: Tampering
  threat: baseline changed after approval
  likelihood: L
  impact: H
  controls: immutability; minor amendments as annotations only
  residual_risk: L
- id: THR-S08-04
  component: Plan approval
  stride: Elevation
  threat: author approves own plan
  likelihood: M
  impact: H
  controls: SoD + authority check
  residual_risk: L
- id: THR-S08-05
  component: Decision request
  stride: Info Disclosure
  threat: citations above request label exposed
  likelihood: M
  impact: M
  controls: CITATION_ABOVE_LABEL guard; withheld per reader
  residual_risk: L
- id: THR-S08-06
  component: Task sync
  stride: Tampering
  threat: sync creates tasks outside plan scope
  likelihood: L
  impact: M
  controls: sync identity limited to plan's org scope; activities' scopes ⊆ plan scope
  residual_risk: L
```

</details>
