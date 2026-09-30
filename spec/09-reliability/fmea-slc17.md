---
id: FMEA-SLC17
type: fmea
title: Failure Mode Analysis — SLC-17
wave: W5
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
recalibrate_after_pilot: true
---

# Failure Mode Analysis — SLC-17

## failure_modes

_2 items_

### FM-S17-01

- **component:** Incident response SLA scheduler
- **failure:** scheduler down or delayed
- **cause:** platform-wide scheduler outage (shared with SLC-03/SLC-08 due-date mechanisms)
- **effect:** SYS:response SLA elapsed without dispatch not raised on time; late dispatch goes undetected
- **detection:** scheduler heartbeat metric; incident age gauge
- **severity:** H
- **likelihood:** L
- **prevention:** scheduler is a platform-shared, already-redundant component (no SLC-17-specific new dependency)
- **mitigation_recovery:** manual dispatch remains available at all times; SLA breach is a detection aid, not a blocking gate
- **data_loss:** none
- **user_impact:** delayed escalation notice, not delayed response capability
- **dependency_impact:** shared with SLC-03, SLC-08

### FM-S17-02

- **component:** Contingency plan linkage (AGG-PLAN, CR-60)
- **failure:** an Incident is closed while a linked CONTINGENCY plan is still ACTIVE
- **cause:** commander closes the incident without checking the plan's own lifecycle (Plan and Incident are separate aggregates, no automatic coupling — R3-Q2)
- **effect:** recovery work under the plan continues after the triggering incident is marked closed, which can read as recovery being "done" when it is not
- **detection:** QRY-INC-RECOVERY-STATUS surfaces the linked plan's open tasks regardless of the incident's own state
- **severity:** M
- **likelihood:** M
- **prevention:** CMD-INC-CLOSE's guard only requires linked response tasks terminal (INV-INC-02); it deliberately does not require the contingency plan closed, since recovery may legitimately outlast incident closure
- **mitigation_recovery:** operational runbook should check recovery status before treating an incident's closure as "fully resolved" — documented in `12-06 (Recovery)` query response_measure, not enforced by a guard (a design trade-off, not a defect)
- **data_loss:** none
- **user_impact:** possible false sense of completion if the runbook step is skipped
- **dependency_impact:** SLC-08 (Plan)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S17-01
  component: Incident response SLA scheduler
  failure: scheduler down or delayed
  cause: platform-wide scheduler outage (shared with SLC-03/SLC-08 due-date mechanisms)
  effect: SYS:response SLA elapsed without dispatch not raised on time; late dispatch goes undetected
  detection: scheduler heartbeat metric; incident age gauge
  severity: H
  likelihood: L
  prevention: scheduler is a platform-shared, already-redundant component (no SLC-17-specific new dependency)
  mitigation_recovery: manual dispatch remains available at all times; SLA breach is a detection aid, not a blocking gate
  data_loss: none
  user_impact: delayed escalation notice, not delayed response capability
  dependency_impact: shared with SLC-03, SLC-08
- id: FM-S17-02
  component: Contingency plan linkage (AGG-PLAN, CR-60)
  failure: an Incident is closed while a linked CONTINGENCY plan is still ACTIVE
  cause: commander closes the incident without checking the plan's own lifecycle (Plan and Incident are separate aggregates, no automatic coupling — R3-Q2)
  effect: recovery work under the plan continues after the triggering incident is marked closed, which can read as recovery being "done" when it is not
  detection: QRY-INC-RECOVERY-STATUS surfaces the linked plan's open tasks regardless of the incident's own state
  severity: M
  likelihood: M
  prevention: CMD-INC-CLOSE's guard only requires linked response tasks terminal (INV-INC-02); it deliberately does not require the contingency plan closed, since recovery may legitimately outlast incident closure
  mitigation_recovery: operational runbook should check recovery status before treating an incident's closure as fully resolved — a design trade-off, not a defect
  data_loss: none
  user_impact: possible false sense of completion if the runbook step is skipped
  dependency_impact: SLC-08 (Plan)
```

</details>
