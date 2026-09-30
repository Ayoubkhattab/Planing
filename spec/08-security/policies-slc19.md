---
id: POLICIES-SLC19
type: policy-decision-tables
title: Policy Decision Tables — SLC-19
wave: W6
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
recalibrate_after_pilot: true
---

# Policy Decision Tables — SLC-19

## command_policies

_15 items_

### POL-SCN-DEFINE

- **command:** CMD-SCN-DEFINE
- **subject:** Training Manager
- **resource:** AGG-SCENARIO
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SCN-EDIT

- **command:** CMD-SCN-EDIT
- **subject:** Training Manager
- **resource:** AGG-SCENARIO
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SCN-ACTIVATE

- **command:** CMD-SCN-ACTIVATE
- **subject:** Exercise Director
- **resource:** AGG-SCENARIO
- **context_conditions:** tenant match; approver ≠ author (INV-SCN via segregation of duties)
- **segregation_of_duties:** approver ≠ author
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SCN-RETIRE

- **command:** CMD-SCN-RETIRE
- **subject:** Exercise Director
- **resource:** AGG-SCENARIO
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-EXR-PLAN

- **command:** CMD-EXR-PLAN
- **subject:** Exercise Director / Training Manager
- **resource:** AGG-EXERCISE
- **context_conditions:** tenant match; scenario ACTIVE and visible to actor
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-EXR-SCHEDULE

- **command:** CMD-EXR-SCHEDULE
- **subject:** Exercise Director / Training Manager
- **resource:** AGG-EXERCISE
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-EXR-START

- **command:** CMD-EXR-START
- **subject:** Exercise Director / Training Manager
- **resource:** AGG-EXERCISE
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-EXR-CANCEL

- **command:** CMD-EXR-CANCEL
- **subject:** Exercise Director / Training Manager
- **resource:** AGG-EXERCISE
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SIM-START

- **command:** CMD-SIM-START
- **subject:** system (workload identity)
- **resource:** AGG-SIMULATION
- **context_conditions:** tenant match; invoked only within CMD-EXR-START's unit of work
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SIM-DELIVER-INJECT

- **command:** CMD-SIM-DELIVER-INJECT
- **subject:** Exercise Controller
- **resource:** AGG-SIMULATION
- **context_conditions:** tenant match; inject_ref belongs to the linked scenario
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SIM-RECORD-EVALUATION

- **command:** CMD-SIM-RECORD-EVALUATION
- **subject:** Evaluator
- **resource:** AGG-SIMULATION
- **context_conditions:** tenant match; evaluator ≠ participant (INV-SIM-03)
- **segregation_of_duties:** evaluator ≠ participant
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SIM-PAUSE

- **command:** CMD-SIM-PAUSE
- **subject:** Exercise Controller
- **resource:** AGG-SIMULATION
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SIM-RESUME

- **command:** CMD-SIM-RESUME
- **subject:** Exercise Controller
- **resource:** AGG-SIMULATION
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SIM-COMPLETE

- **command:** CMD-SIM-COMPLETE
- **subject:** Exercise Controller
- **resource:** AGG-SIMULATION
- **context_conditions:** tenant match; every participant evaluated (INV-SIM-02)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SIM-ABORT

- **command:** CMD-SIM-ABORT
- **subject:** Exercise Controller
- **resource:** AGG-SIMULATION
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

## query_policies

_7 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-SCN-GET | QRY-SCN-GET | allowed_scope | DENY (not-found shape) |
| POL-SCN-LIST | QRY-SCN-LIST | allowed_scope | DENY (not-found shape) |
| POL-EXR-GET | QRY-EXR-GET | allowed_scope | DENY (not-found shape) |
| POL-EXR-LIST | QRY-EXR-LIST | allowed_scope | DENY (not-found shape) |
| POL-SIM-GET | QRY-SIM-GET | allowed_scope | DENY (not-found shape) |
| POL-SIM-LIST | QRY-SIM-LIST | allowed_scope | DENY (not-found shape) |
| POL-SIM-TIMELINE | QRY-SIM-TIMELINE | allowed_scope | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-SCN-DEFINE
  command: CMD-SCN-DEFINE
  subject: Training Manager
  resource: AGG-SCENARIO
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SCN-EDIT
  command: CMD-SCN-EDIT
  subject: Training Manager
  resource: AGG-SCENARIO
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SCN-ACTIVATE
  command: CMD-SCN-ACTIVATE
  subject: Exercise Director
  resource: AGG-SCENARIO
  context_conditions: tenant match; approver ≠ author (INV-SCN via segregation of duties)
  segregation_of_duties: approver ≠ author
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SCN-RETIRE
  command: CMD-SCN-RETIRE
  subject: Exercise Director
  resource: AGG-SCENARIO
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-EXR-PLAN
  command: CMD-EXR-PLAN
  subject: Exercise Director / Training Manager
  resource: AGG-EXERCISE
  context_conditions: tenant match; scenario ACTIVE and visible to actor
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-EXR-SCHEDULE
  command: CMD-EXR-SCHEDULE
  subject: Exercise Director / Training Manager
  resource: AGG-EXERCISE
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-EXR-START
  command: CMD-EXR-START
  subject: Exercise Director / Training Manager
  resource: AGG-EXERCISE
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-EXR-CANCEL
  command: CMD-EXR-CANCEL
  subject: Exercise Director / Training Manager
  resource: AGG-EXERCISE
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SIM-START
  command: CMD-SIM-START
  subject: system (workload identity)
  resource: AGG-SIMULATION
  context_conditions: tenant match; invoked only within CMD-EXR-START's unit of work
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SIM-DELIVER-INJECT
  command: CMD-SIM-DELIVER-INJECT
  subject: Exercise Controller
  resource: AGG-SIMULATION
  context_conditions: tenant match; inject_ref belongs to the linked scenario
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SIM-RECORD-EVALUATION
  command: CMD-SIM-RECORD-EVALUATION
  subject: Evaluator
  resource: AGG-SIMULATION
  context_conditions: tenant match; evaluator ≠ participant (INV-SIM-03)
  segregation_of_duties: evaluator ≠ participant
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SIM-PAUSE
  command: CMD-SIM-PAUSE
  subject: Exercise Controller
  resource: AGG-SIMULATION
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SIM-RESUME
  command: CMD-SIM-RESUME
  subject: Exercise Controller
  resource: AGG-SIMULATION
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SIM-COMPLETE
  command: CMD-SIM-COMPLETE
  subject: Exercise Controller
  resource: AGG-SIMULATION
  context_conditions: tenant match; every participant evaluated (INV-SIM-02)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SIM-ABORT
  command: CMD-SIM-ABORT
  subject: Exercise Controller
  resource: AGG-SIMULATION
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-SCN-GET
  query: QRY-SCN-GET
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-SCN-LIST
  query: QRY-SCN-LIST
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-EXR-GET
  query: QRY-EXR-GET
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-EXR-LIST
  query: QRY-EXR-LIST
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-SIM-GET
  query: QRY-SIM-GET
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-SIM-LIST
  query: QRY-SIM-LIST
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-SIM-TIMELINE
  query: QRY-SIM-TIMELINE
  subject: allowed_scope
  otherwise: DENY (not-found shape)
```

</details>
