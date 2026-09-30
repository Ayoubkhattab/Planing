---
id: POLICIES-SLC16
type: policy-decision-tables
title: Policy Decision Tables — SLC-16
wave: W6
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Policy Decision Tables — SLC-16

## command_policies

_18 items_

### POL-CON-REGISTER

- **command:** CMD-CON-REGISTER
- **subject:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)
- **resource:** AGG-INTEGRATION-CONNECTION
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CON-TEST

- **command:** CMD-CON-TEST
- **subject:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)
- **resource:** AGG-INTEGRATION-CONNECTION
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CON-ACTIVATE

- **command:** CMD-CON-ACTIVATE
- **subject:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)
- **resource:** AGG-INTEGRATION-CONNECTION
- **context_conditions:** tenant match
- **segregation_of_duties:** Security Officer ≠ requester
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa

### POL-CON-FAIL-TEST

- **command:** CMD-CON-FAIL-TEST
- **subject:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)
- **resource:** AGG-INTEGRATION-CONNECTION
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CON-SUSPEND

- **command:** CMD-CON-SUSPEND
- **subject:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)
- **resource:** AGG-INTEGRATION-CONNECTION
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CON-RESUME

- **command:** CMD-CON-RESUME
- **subject:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)
- **resource:** AGG-INTEGRATION-CONNECTION
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CON-RETIRE

- **command:** CMD-CON-RETIRE
- **subject:** integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume, retire)
- **resource:** AGG-INTEGRATION-CONNECTION
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SNS-REGISTER

- **command:** CMD-SNS-REGISTER
- **subject:** integration engineer
- **resource:** AGG-SENSOR-STREAM
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SNS-SET-QUALITY-RULES

- **command:** CMD-SNS-SET-QUALITY-RULES
- **subject:** integration engineer
- **resource:** AGG-SENSOR-STREAM
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SNS-ACTIVATE

- **command:** CMD-SNS-ACTIVATE
- **subject:** integration engineer
- **resource:** AGG-SENSOR-STREAM
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SNS-PAUSE

- **command:** CMD-SNS-PAUSE
- **subject:** integration engineer
- **resource:** AGG-SENSOR-STREAM
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SNS-RETIRE

- **command:** CMD-SNS-RETIRE
- **subject:** integration engineer
- **resource:** AGG-SENSOR-STREAM
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-HRS-APPROVE

- **command:** CMD-HRS-APPROVE
- **subject:** Administrator in scope
- **resource:** AGG-HR-SYNC-PROPOSAL
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-HRS-REJECT

- **command:** CMD-HRS-REJECT
- **subject:** Administrator in scope
- **resource:** AGG-HR-SYNC-PROPOSAL
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CAP-PREPARE

- **command:** CMD-CAP-PREPARE
- **subject:** alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)
- **resource:** AGG-CAP-MESSAGE
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CAP-RELEASE

- **command:** CMD-CAP-RELEASE
- **subject:** alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)
- **resource:** AGG-CAP-MESSAGE
- **context_conditions:** tenant match
- **segregation_of_duties:** release authority ≠ preparer
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa

### POL-CAP-RETRY

- **command:** CMD-CAP-RETRY
- **subject:** alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)
- **resource:** AGG-CAP-MESSAGE
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-CAP-CANCEL

- **command:** CMD-CAP-CANCEL
- **subject:** alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)
- **resource:** AGG-CAP-MESSAGE
- **context_conditions:** tenant match
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

## query_policies

_4 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-CON-LIST | QRY-CON-LIST | integration engineers, Security Officer | DENY |
| POL-SNS-LIST | QRY-SNS-LIST | integration engineers, Analyst | DENY |
| POL-HRS-QUEUE | QRY-HRS-QUEUE | Administrator in scope, Security Officer | DENY |
| POL-CAP-LIST | QRY-CAP-LIST | release authority, Auditor | DENY |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-CON-REGISTER
  command: CMD-CON-REGISTER
  subject: integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume,
    retire)
  resource: AGG-INTEGRATION-CONNECTION
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CON-TEST
  command: CMD-CON-TEST
  subject: integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume,
    retire)
  resource: AGG-INTEGRATION-CONNECTION
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CON-ACTIVATE
  command: CMD-CON-ACTIVATE
  subject: integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume,
    retire)
  resource: AGG-INTEGRATION-CONNECTION
  context_conditions: tenant match
  segregation_of_duties: Security Officer ≠ requester
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-CON-FAIL-TEST
  command: CMD-CON-FAIL-TEST
  subject: integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume,
    retire)
  resource: AGG-INTEGRATION-CONNECTION
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CON-SUSPEND
  command: CMD-CON-SUSPEND
  subject: integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume,
    retire)
  resource: AGG-INTEGRATION-CONNECTION
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CON-RESUME
  command: CMD-CON-RESUME
  subject: integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume,
    retire)
  resource: AGG-INTEGRATION-CONNECTION
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CON-RETIRE
  command: CMD-CON-RETIRE
  subject: integration engineer (register, test) · Security Officer ≠ requester (activate) · Administrator (suspend, resume,
    retire)
  resource: AGG-INTEGRATION-CONNECTION
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SNS-REGISTER
  command: CMD-SNS-REGISTER
  subject: integration engineer
  resource: AGG-SENSOR-STREAM
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SNS-SET-QUALITY-RULES
  command: CMD-SNS-SET-QUALITY-RULES
  subject: integration engineer
  resource: AGG-SENSOR-STREAM
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SNS-ACTIVATE
  command: CMD-SNS-ACTIVATE
  subject: integration engineer
  resource: AGG-SENSOR-STREAM
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SNS-PAUSE
  command: CMD-SNS-PAUSE
  subject: integration engineer
  resource: AGG-SENSOR-STREAM
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SNS-RETIRE
  command: CMD-SNS-RETIRE
  subject: integration engineer
  resource: AGG-SENSOR-STREAM
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-HRS-APPROVE
  command: CMD-HRS-APPROVE
  subject: Administrator in scope
  resource: AGG-HR-SYNC-PROPOSAL
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-HRS-REJECT
  command: CMD-HRS-REJECT
  subject: Administrator in scope
  resource: AGG-HR-SYNC-PROPOSAL
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CAP-PREPARE
  command: CMD-CAP-PREPARE
  subject: alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)
  resource: AGG-CAP-MESSAGE
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CAP-RELEASE
  command: CMD-CAP-RELEASE
  subject: alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)
  resource: AGG-CAP-MESSAGE
  context_conditions: tenant match
  segregation_of_duties: release authority ≠ preparer
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-CAP-RETRY
  command: CMD-CAP-RETRY
  subject: alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)
  resource: AGG-CAP-MESSAGE
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CAP-CANCEL
  command: CMD-CAP-CANCEL
  subject: alert recipient / duty officer (prepare) · release authority (release) · operator (retry, cancel)
  resource: AGG-CAP-MESSAGE
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-CON-LIST
  query: QRY-CON-LIST
  subject: integration engineers, Security Officer
  otherwise: DENY
- id: POL-SNS-LIST
  query: QRY-SNS-LIST
  subject: integration engineers, Analyst
  otherwise: DENY
- id: POL-HRS-QUEUE
  query: QRY-HRS-QUEUE
  subject: Administrator in scope, Security Officer
  otherwise: DENY
- id: POL-CAP-LIST
  query: QRY-CAP-LIST
  subject: release authority, Auditor
  otherwise: DENY
```

</details>
