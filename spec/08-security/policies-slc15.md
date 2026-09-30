---
id: POLICIES-SLC15
type: policy-decision-tables
title: Policy Decision Tables — SLC-15
wave: W6
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Policy Decision Tables — SLC-15

## command_policies

_17 items_

### POL-CRD-OPEN

- **command:** CMD-CRD-OPEN
- **subject:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)
- **resource:** AGG-COORDINATION-CASE
- **context_conditions:** tenant match; participant scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRD-ADD-PARTICIPANT

- **command:** CMD-CRD-ADD-PARTICIPANT
- **subject:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)
- **resource:** AGG-COORDINATION-CASE
- **context_conditions:** tenant match; participant scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRD-REMOVE-PARTICIPANT

- **command:** CMD-CRD-REMOVE-PARTICIPANT
- **subject:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)
- **resource:** AGG-COORDINATION-CASE
- **context_conditions:** tenant match; participant scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRD-ACTIVATE

- **command:** CMD-CRD-ACTIVATE
- **subject:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)
- **resource:** AGG-COORDINATION-CASE
- **context_conditions:** tenant match; participant scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRD-ASSIGN-RESPONSIBILITY

- **command:** CMD-CRD-ASSIGN-RESPONSIBILITY
- **subject:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)
- **resource:** AGG-COORDINATION-CASE
- **context_conditions:** tenant match; participant scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRD-UPDATE-RESPONSIBILITY

- **command:** CMD-CRD-UPDATE-RESPONSIBILITY
- **subject:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)
- **resource:** AGG-COORDINATION-CASE
- **context_conditions:** tenant match; participant scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRD-REQUEST-DECISION

- **command:** CMD-CRD-REQUEST-DECISION
- **subject:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)
- **resource:** AGG-COORDINATION-CASE
- **context_conditions:** tenant match; participant scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRD-CLOSE

- **command:** CMD-CRD-CLOSE
- **subject:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)
- **resource:** AGG-COORDINATION-CASE
- **context_conditions:** tenant match; participant scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRD-CANCEL

- **command:** CMD-CRD-CANCEL
- **subject:** lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update, request decision)
- **resource:** AGG-COORDINATION-CASE
- **context_conditions:** tenant match; participant scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRP-PROPOSE

- **command:** CMD-CRP-PROPOSE
- **subject:** Analyst (propose, review, accept, reject)
- **resource:** AGG-CORRELATION-PROPOSAL
- **context_conditions:** tenant match; inputs visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRP-START-REVIEW

- **command:** CMD-CRP-START-REVIEW
- **subject:** Analyst (propose, review, accept, reject)
- **resource:** AGG-CORRELATION-PROPOSAL
- **context_conditions:** tenant match; inputs visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRP-ACCEPT

- **command:** CMD-CRP-ACCEPT
- **subject:** Analyst (propose, review, accept, reject)
- **resource:** AGG-CORRELATION-PROPOSAL
- **context_conditions:** tenant match; inputs visible
- **segregation_of_duties:** reviewer cleared for all inputs
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRP-REJECT

- **command:** CMD-CRP-REJECT
- **subject:** Analyst (propose, review, accept, reject)
- **resource:** AGG-CORRELATION-PROPOSAL
- **context_conditions:** tenant match; inputs visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRR-DEFINE

- **command:** CMD-CRR-DEFINE
- **subject:** Analyst lead (define, edit) · second approver (activate)
- **resource:** AGG-CORRELATION-RULE
- **context_conditions:** tenant match; inputs visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRR-EDIT

- **command:** CMD-CRR-EDIT
- **subject:** Analyst lead (define, edit) · second approver (activate)
- **resource:** AGG-CORRELATION-RULE
- **context_conditions:** tenant match; inputs visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRR-ACTIVATE

- **command:** CMD-CRR-ACTIVATE
- **subject:** Analyst lead (define, edit) · second approver (activate)
- **resource:** AGG-CORRELATION-RULE
- **context_conditions:** tenant match; inputs visible
- **segregation_of_duties:** approver ≠ author
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CRR-RETIRE

- **command:** CMD-CRR-RETIRE
- **subject:** Analyst lead (define, edit) · second approver (activate)
- **resource:** AGG-CORRELATION-RULE
- **context_conditions:** tenant match; inputs visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

## query_policies

_4 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-CRD-GET | QRY-CRD-GET | participants (scope-limited); lead | DENY (not-found shape) |
| POL-CRD-LIST | QRY-CRD-LIST | allowed_scope | DENY (not-found shape) |
| POL-CRP-QUEUE | QRY-CRP-QUEUE | Analyst | DENY (not-found shape) |
| POL-CRP-GET | QRY-CRP-GET | reviewer cleared for all inputs | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-CRD-OPEN
  command: CMD-CRD-OPEN
  subject: lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update,
    request decision)
  resource: AGG-COORDINATION-CASE
  context_conditions: tenant match; participant scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRD-ADD-PARTICIPANT
  command: CMD-CRD-ADD-PARTICIPANT
  subject: lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update,
    request decision)
  resource: AGG-COORDINATION-CASE
  context_conditions: tenant match; participant scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRD-REMOVE-PARTICIPANT
  command: CMD-CRD-REMOVE-PARTICIPANT
  subject: lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update,
    request decision)
  resource: AGG-COORDINATION-CASE
  context_conditions: tenant match; participant scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRD-ACTIVATE
  command: CMD-CRD-ACTIVATE
  subject: lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update,
    request decision)
  resource: AGG-COORDINATION-CASE
  context_conditions: tenant match; participant scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRD-ASSIGN-RESPONSIBILITY
  command: CMD-CRD-ASSIGN-RESPONSIBILITY
  subject: lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update,
    request decision)
  resource: AGG-COORDINATION-CASE
  context_conditions: tenant match; participant scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRD-UPDATE-RESPONSIBILITY
  command: CMD-CRD-UPDATE-RESPONSIBILITY
  subject: lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update,
    request decision)
  resource: AGG-COORDINATION-CASE
  context_conditions: tenant match; participant scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRD-REQUEST-DECISION
  command: CMD-CRD-REQUEST-DECISION
  subject: lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update,
    request decision)
  resource: AGG-COORDINATION-CASE
  context_conditions: tenant match; participant scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRD-CLOSE
  command: CMD-CRD-CLOSE
  subject: lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update,
    request decision)
  resource: AGG-COORDINATION-CASE
  context_conditions: tenant match; participant scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRD-CANCEL
  command: CMD-CRD-CANCEL
  subject: lead organization Manager (open, participants, activate, assign, close, cancel) · participant members (update,
    request decision)
  resource: AGG-COORDINATION-CASE
  context_conditions: tenant match; participant scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRP-PROPOSE
  command: CMD-CRP-PROPOSE
  subject: Analyst (propose, review, accept, reject)
  resource: AGG-CORRELATION-PROPOSAL
  context_conditions: tenant match; inputs visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRP-START-REVIEW
  command: CMD-CRP-START-REVIEW
  subject: Analyst (propose, review, accept, reject)
  resource: AGG-CORRELATION-PROPOSAL
  context_conditions: tenant match; inputs visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRP-ACCEPT
  command: CMD-CRP-ACCEPT
  subject: Analyst (propose, review, accept, reject)
  resource: AGG-CORRELATION-PROPOSAL
  context_conditions: tenant match; inputs visible
  segregation_of_duties: reviewer cleared for all inputs
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRP-REJECT
  command: CMD-CRP-REJECT
  subject: Analyst (propose, review, accept, reject)
  resource: AGG-CORRELATION-PROPOSAL
  context_conditions: tenant match; inputs visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRR-DEFINE
  command: CMD-CRR-DEFINE
  subject: Analyst lead (define, edit) · second approver (activate)
  resource: AGG-CORRELATION-RULE
  context_conditions: tenant match; inputs visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRR-EDIT
  command: CMD-CRR-EDIT
  subject: Analyst lead (define, edit) · second approver (activate)
  resource: AGG-CORRELATION-RULE
  context_conditions: tenant match; inputs visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRR-ACTIVATE
  command: CMD-CRR-ACTIVATE
  subject: Analyst lead (define, edit) · second approver (activate)
  resource: AGG-CORRELATION-RULE
  context_conditions: tenant match; inputs visible
  segregation_of_duties: approver ≠ author
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRR-RETIRE
  command: CMD-CRR-RETIRE
  subject: Analyst lead (define, edit) · second approver (activate)
  resource: AGG-CORRELATION-RULE
  context_conditions: tenant match; inputs visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-CRD-GET
  query: QRY-CRD-GET
  subject: participants (scope-limited); lead
  otherwise: DENY (not-found shape)
- id: POL-CRD-LIST
  query: QRY-CRD-LIST
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-CRP-QUEUE
  query: QRY-CRP-QUEUE
  subject: Analyst
  otherwise: DENY (not-found shape)
- id: POL-CRP-GET
  query: QRY-CRP-GET
  subject: reviewer cleared for all inputs
  otherwise: DENY (not-found shape)
```

</details>
