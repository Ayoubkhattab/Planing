---
id: THREAT-MODEL-SLC19
type: threat-model
title: Threat Model — SLC-19
wave: W5
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
recalibrate_after_pilot: true
---

# Threat Model — SLC-19

## threats

_5 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S19-01 | Scenario ↔ Exercise freeze (INV-EXR-01) | Tampering | a scenario edited after an exercise was planned against it retroactively changes what the exercise is understood to have tested | L | M | scenario_ref is frozen on AGG-EXERCISE at CMD-EXR-PLAN time; editing an ACTIVE scenario always creates a new version rather than mutating the version already referenced by planned exercises | L |
| THR-S19-02 | Exercise ↔ Simulation outcome delegation (mirrors CR-62/SLC-18) | Elevation | an exercise forced into COMPLETED without a simulation ever actually running, hiding that no training occurred | L | H | no human command sets COMPLETED or ABORTED; only SYS: transitions driven by the linked Simulation's own EVT-SIM-COMPLETED/EVT-SIM-ABORTED (INV-EXR-02) — visible in the full state × command matrix (SL-05), which has no human-triggered cell for either terminal state | L |
| THR-S19-03 | Evaluation recording | Repudiation | a participant records their own evaluation as MET to fabricate a passing result | M | H | evaluator ≠ participant is a hard guard (INV-SIM-03), enforced by the policy decision point before the command is accepted, rejected with SEGREGATION_OF_DUTIES | L |
| THR-S19-04 | Simulation completion vs. evaluation coverage | Repudiation | a simulation marked COMPLETED while some participants were never evaluated, silently certifying attendance without assessment | M | M | INV-SIM-02 requires at least one recorded evaluation per participant before COMPLETED; CMD-SIM-COMPLETE's guard fails with EVALUATION_MISSING otherwise — no state hides an unevaluated participant | L |
| THR-S19-05 | Inject delivery timeline | Tampering | an inject delivery record inserted out of order or backdated to fabricate a different exercise timeline than what actually happened | L | M | inject deliveries are append-only and strictly increasing in time (INV-SIM-01), mirroring AGG-SHIPMENT's checkpoint pattern; no edit or delete command exists | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S19-01
  component: Scenario ↔ Exercise freeze (INV-EXR-01)
  stride: Tampering
  threat: a scenario edited after an exercise was planned against it retroactively changes what the exercise is understood to have tested
  likelihood: L
  impact: M
  controls: scenario_ref is frozen on AGG-EXERCISE at CMD-EXR-PLAN time; editing an ACTIVE scenario always creates a new version rather than mutating the version already referenced by planned exercises
  residual_risk: L
- id: THR-S19-02
  component: Exercise ↔ Simulation outcome delegation (mirrors CR-62/SLC-18)
  stride: Elevation
  threat: an exercise forced into COMPLETED without a simulation ever actually running, hiding that no training occurred
  likelihood: L
  impact: H
  controls: 'no human command sets COMPLETED or ABORTED; only SYS: transitions driven by the linked Simulation''s own EVT-SIM-COMPLETED/EVT-SIM-ABORTED (INV-EXR-02) — visible in the full state × command matrix (SL-05), which has no human-triggered cell for either terminal state'
  residual_risk: L
- id: THR-S19-03
  component: Evaluation recording
  stride: Repudiation
  threat: a participant records their own evaluation as MET to fabricate a passing result
  likelihood: M
  impact: H
  controls: evaluator ≠ participant is a hard guard (INV-SIM-03), enforced by the policy decision point before the command is accepted, rejected with SEGREGATION_OF_DUTIES
  residual_risk: L
- id: THR-S19-04
  component: Simulation completion vs. evaluation coverage
  stride: Repudiation
  threat: a simulation marked COMPLETED while some participants were never evaluated, silently certifying attendance without assessment
  likelihood: M
  impact: M
  controls: INV-SIM-02 requires at least one recorded evaluation per participant before COMPLETED; CMD-SIM-COMPLETE's guard fails with EVALUATION_MISSING otherwise — no state hides an unevaluated participant
  residual_risk: L
- id: THR-S19-05
  component: Inject delivery timeline
  stride: Tampering
  threat: an inject delivery record inserted out of order or backdated to fabricate a different exercise timeline than what actually happened
  likelihood: L
  impact: M
  controls: inject deliveries are append-only and strictly increasing in time (INV-SIM-01), mirroring AGG-SHIPMENT's checkpoint pattern; no edit or delete command exists
  residual_risk: L
```

</details>
