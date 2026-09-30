---
id: THREAT-MODEL-SLC03
type: threat-model
title: Threat Model — SLC-03 (STRIDE)
wave: W5
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Threat Model — SLC-03 (STRIDE)

## threats

_6 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S03-01 | Approval | Elevation | assignee approves own work | M | H | PB-06 / INV-TASK-07; audit | L |
| THR-S03-02 | Criteria | Tampering | criteria weakened after assignment | M | M | INV-TASK-09 frozen from ASSIGNED | L |
| THR-S03-03 | Assignment | Info Disclosure | task assigned to a user not cleared for its label | M | H | assign guard: clearance ≥ label; reclassify guard | L |
| THR-S03-04 | Eligibility | Elevation | assignment bypasses eligibility when BC05 is down | M | M | fail-closed ELIGIBILITY_UNAVAILABLE | L |
| THR-S03-05 | Offline replay | Tampering | forged or replayed offline commands | M | M | base_version + client_command_id + device signature (SLC-11) | L |
| THR-S03-06 | Task list | Info Disclosure | list counts reveal hidden tasks | M | M | allowed_scope pre-filter (ADR-P06) | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S03-01
  component: Approval
  stride: Elevation
  threat: assignee approves own work
  likelihood: M
  impact: H
  controls: PB-06 / INV-TASK-07; audit
  residual_risk: L
- id: THR-S03-02
  component: Criteria
  stride: Tampering
  threat: criteria weakened after assignment
  likelihood: M
  impact: M
  controls: INV-TASK-09 frozen from ASSIGNED
  residual_risk: L
- id: THR-S03-03
  component: Assignment
  stride: Info Disclosure
  threat: task assigned to a user not cleared for its label
  likelihood: M
  impact: H
  controls: 'assign guard: clearance ≥ label; reclassify guard'
  residual_risk: L
- id: THR-S03-04
  component: Eligibility
  stride: Elevation
  threat: assignment bypasses eligibility when BC05 is down
  likelihood: M
  impact: M
  controls: fail-closed ELIGIBILITY_UNAVAILABLE
  residual_risk: L
- id: THR-S03-05
  component: Offline replay
  stride: Tampering
  threat: forged or replayed offline commands
  likelihood: M
  impact: M
  controls: base_version + client_command_id + device signature (SLC-11)
  residual_risk: L
- id: THR-S03-06
  component: Task list
  stride: Info Disclosure
  threat: list counts reveal hidden tasks
  likelihood: M
  impact: M
  controls: allowed_scope pre-filter (ADR-P06)
  residual_risk: L
```

</details>
