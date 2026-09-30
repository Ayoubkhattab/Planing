---
id: FMEA-SLC19
type: fmea
title: Failure Mode Analysis — SLC-19
wave: W5
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
recalibrate_after_pilot: true
---

# Failure Mode Analysis — SLC-19

## failure_modes

_2 items_

### FM-S19-01

- **component:** Exercise ↔ Simulation linkage, abort path
- **failure:** a simulation aborts (safety stop, participant unavailability) leaving its exercise ABORTED, but the readiness gap that motivated the exercise remains uncovered with no automatic re-scheduling
- **cause:** CMD-EXR-CANCEL is not accepted once IN_PROGRESS (mirrors SLC-18's Shipment cancel-only-before-departure pattern), and no automatic retry exists once a simulation aborts
- **effect:** an aborted exercise requires an explicit new CMD-EXR-PLAN; if unnoticed, the underlying training or certification gap persists silently
- **detection:** exercise abort rate per scenario/role; SLC-09's own role-requirement readiness reports (read-only) keep showing the gap until it is closed
- **severity:** M
- **likelihood:** L
- **prevention:** none by design — an intentional simplification (A17), mirroring SLC-18's decision not to auto-resend a partial delivery
- **mitigation_recovery:** the Training Manager reviews ABORTED exercises and re-plans explicitly with a new CMD-EXR-PLAN
- **data_loss:** none
- **user_impact:** a training/readiness gap that persists until someone re-plans, never silently marked resolved
- **dependency_impact:** SLC-09 (Role Requirement readiness, read-only)

### FM-S19-02

- **component:** Evaluation ↔ Qualification Record reuse (evidence:urn)
- **failure:** a completed simulation's evaluation is cited as evidence on a Qualification Record, but the simulation is later found to have run against the wrong scenario version for the competency being certified
- **cause:** AGG-QUALIFICATION-RECORD's `evidence:urn` is a generic, untyped reference by design (no schema change — `03-domain/contexts/BC05/training-exercise-spec.md` §1); it does not itself validate that the cited Simulation's scenario matches the competency claimed
- **effect:** a qualification record could cite evidence that, on closer inspection, does not actually demonstrate the claimed competency
- **detection:** manual review during qualification renewal or audit; the Simulation's own scenario_ref and evaluation history remain fully inspectable (append-only, never overwritten)
- **severity:** M
- **likelihood:** L
- **prevention:** the Qualification Record's own approving actor (Resource Manager / Training Manager, SLC-03) is expected to check cited evidence before recording; no automated cross-aggregate validation was added, consistent with keeping `evidence:urn` generic across all its existing uses (tasks, plans, incidents, and now simulations)
- **mitigation_recovery:** `CMD-QUAL-REVOKE` remains available on SLC-03's own aggregate if a qualification is later found improperly evidenced
- **data_loss:** none
- **user_impact:** possible delayed detection of an improperly evidenced qualification, mitigated by full evidence traceability
- **dependency_impact:** SLC-03 (Qualification Record, unmodified)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S19-01
  component: Exercise ↔ Simulation linkage, abort path
  failure: a simulation aborts (safety stop, participant unavailability) leaving its exercise ABORTED, but the readiness gap that motivated the exercise remains uncovered with no automatic re-scheduling
  cause: CMD-EXR-CANCEL is not accepted once IN_PROGRESS (mirrors SLC-18's Shipment cancel-only-before-departure pattern), and no automatic retry exists once a simulation aborts
  effect: an aborted exercise requires an explicit new CMD-EXR-PLAN; if unnoticed, the underlying training or certification gap persists silently
  detection: exercise abort rate per scenario/role; SLC-09's own role-requirement readiness reports (read-only) keep showing the gap until it is closed
  severity: M
  likelihood: L
  prevention: none by design — an intentional simplification (A17), mirroring SLC-18's decision not to auto-resend a partial delivery
  mitigation_recovery: the Training Manager reviews ABORTED exercises and re-plans explicitly with a new CMD-EXR-PLAN
  data_loss: none
  user_impact: a training/readiness gap that persists until someone re-plans, never silently marked resolved
  dependency_impact: SLC-09 (Role Requirement readiness, read-only)
- id: FM-S19-02
  component: Evaluation ↔ Qualification Record reuse (evidence:urn)
  failure: a completed simulation's evaluation is cited as evidence on a Qualification Record, but the simulation is later found to have run against the wrong scenario version for the competency being certified
  cause: AGG-QUALIFICATION-RECORD's evidence:urn is a generic, untyped reference by design (no schema change); it does not itself validate that the cited Simulation's scenario matches the competency claimed
  effect: a qualification record could cite evidence that, on closer inspection, does not actually demonstrate the claimed competency
  detection: manual review during qualification renewal or audit; the Simulation's own scenario_ref and evaluation history remain fully inspectable (append-only, never overwritten)
  severity: M
  likelihood: L
  prevention: the Qualification Record's own approving actor (Resource Manager / Training Manager, SLC-03) is expected to check cited evidence before recording; no automated cross-aggregate validation was added, consistent with keeping evidence:urn generic across all its existing uses
  mitigation_recovery: CMD-QUAL-REVOKE remains available on SLC-03's own aggregate if a qualification is later found improperly evidenced
  data_loss: none
  user_impact: possible delayed detection of an improperly evidenced qualification, mitigated by full evidence traceability
  dependency_impact: SLC-03 (Qualification Record, unmodified)
```

</details>
