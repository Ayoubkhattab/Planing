---
id: THREAT-MODEL-SLC17
type: threat-model
title: Threat Model — SLC-17
wave: W5
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
recalibrate_after_pilot: true
---

# Threat Model — SLC-17

## threats

_5 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S17-01 | Incident severity | Tampering | severity silently lowered to hide a crisis from oversight | L | H | severity only decreases via a distinct, separately-authorized CMD-INC-DE-ESCALATE (INV-INC-01) | L |
| THR-S17-02 | Contingency activation | Elevation | a plan activated automatically as a side effect of escalation, bypassing authorization | M | H | activation is always an explicit command (INV-INC-03); mirrors the SLC-09 Silent Pre-emption lesson | L |
| THR-S17-03 | Risk register | Repudiation | a risk closed without rationale, later disputed as never having been treated | M | M | CLOSED requires an explicit rationale; no reopen command (INV-RIS-04) | L |
| THR-S17-04 | Risk / Incident linkage | Info Disclosure | linking an incident to a risk leaks the risk's scope to an actor not cleared for it | M | H | linkage does not change either aggregate's label; each still enforces its own label independently (INV-RIS-05, INV-INC-04) | L |
| THR-S17-05 | Response tasks | Elevation | a task created with incident_ref bypasses the review/segregation-of-duties checks that plan-linked tasks get | L | M | CMD-TASK-CREATE's guards (assignee eligibility, SoD on approval) apply identically regardless of plan_ref/incident_ref/ad_hoc_reason (CR-61 changes only the creation link, not downstream guards) | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S17-01
  component: Incident severity
  stride: Tampering
  threat: severity silently lowered to hide a crisis from oversight
  likelihood: L
  impact: H
  controls: severity only decreases via a distinct, separately-authorized CMD-INC-DE-ESCALATE (INV-INC-01)
  residual_risk: L
- id: THR-S17-02
  component: Contingency activation
  stride: Elevation
  threat: a plan activated automatically as a side effect of escalation, bypassing authorization
  likelihood: M
  impact: H
  controls: activation is always an explicit command (INV-INC-03); mirrors the SLC-09 Silent Pre-emption lesson
  residual_risk: L
- id: THR-S17-03
  component: Risk register
  stride: Repudiation
  threat: a risk closed without rationale, later disputed as never having been treated
  likelihood: M
  impact: M
  controls: CLOSED requires an explicit rationale; no reopen command (INV-RIS-04)
  residual_risk: L
- id: THR-S17-04
  component: Risk / Incident linkage
  stride: Info Disclosure
  threat: linking an incident to a risk leaks the risk's scope to an actor not cleared for it
  likelihood: M
  impact: H
  controls: linkage does not change either aggregate's label; each still enforces its own label independently (INV-RIS-05, INV-INC-04)
  residual_risk: L
- id: THR-S17-05
  component: Response tasks
  stride: Elevation
  threat: a task created with incident_ref bypasses the review/segregation-of-duties checks that plan-linked tasks get
  likelihood: L
  impact: M
  controls: CMD-TASK-CREATE's guards (assignee eligibility, SoD on approval) apply identically regardless of plan_ref/incident_ref/ad_hoc_reason (CR-61 changes only the creation link, not downstream guards)
  residual_risk: L
```

</details>
