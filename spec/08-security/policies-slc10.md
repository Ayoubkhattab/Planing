---
id: POLICIES-SLC10
type: policy-decision-tables
title: Policy Decision Tables — SLC-10
wave: W6
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Policy Decision Tables — SLC-10

## command_policies

_27 items_

### POL-AIR-SUBMIT

- **command:** CMD-AIR-SUBMIT
- **subject:** any authorized user (submit, cancel)
- **resource:** AGG-AI-REQUEST
- **context_conditions:** tenant match; operation allowed by routing and matrix
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AIR-CANCEL

- **command:** CMD-AIR-CANCEL
- **subject:** any authorized user (submit, cancel)
- **resource:** AGG-AI-REQUEST
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AIRS-START-REVIEW

- **command:** CMD-AIRS-START-REVIEW
- **subject:** reviewer authorized on the target (review, accept, reject)
- **resource:** AGG-AI-RESULT
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AIRS-ACCEPT

- **command:** CMD-AIRS-ACCEPT
- **subject:** reviewer authorized on the target (review, accept, reject)
- **resource:** AGG-AI-RESULT
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AIRS-ACCEPT-PARTIALLY

- **command:** CMD-AIRS-ACCEPT-PARTIALLY
- **subject:** reviewer authorized on the target (review, accept, reject)
- **resource:** AGG-AI-RESULT
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AIRS-REJECT

- **command:** CMD-AIRS-REJECT
- **subject:** reviewer authorized on the target (review, accept, reject)
- **resource:** AGG-AI-RESULT
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MDL-REGISTER

- **command:** CMD-MDL-REGISTER
- **subject:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
- **resource:** AGG-MODEL-VERSION
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MDL-START-EVALUATION

- **command:** CMD-MDL-START-EVALUATION
- **subject:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
- **resource:** AGG-MODEL-VERSION
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MDL-APPROVE

- **command:** CMD-MDL-APPROVE
- **subject:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
- **resource:** AGG-MODEL-VERSION
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** approver ≠ registrar
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MDL-FAIL-EVALUATION

- **command:** CMD-MDL-FAIL-EVALUATION
- **subject:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
- **resource:** AGG-MODEL-VERSION
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MDL-STAGE

- **command:** CMD-MDL-STAGE
- **subject:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
- **resource:** AGG-MODEL-VERSION
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MDL-PROMOTE

- **command:** CMD-MDL-PROMOTE
- **subject:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
- **resource:** AGG-MODEL-VERSION
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** approver ≠ stager
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MDL-DEPRECATE

- **command:** CMD-MDL-DEPRECATE
- **subject:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
- **resource:** AGG-MODEL-VERSION
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MDL-REINSTATE

- **command:** CMD-MDL-REINSTATE
- **subject:** AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
- **resource:** AGG-MODEL-VERSION
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MDL-RETIRE

- **command:** CMD-MDL-RETIRE
- **subject:** AI governance authority (retire)
- **resource:** AGG-MODEL-VERSION
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RTG-DRAFT

- **command:** CMD-RTG-DRAFT
- **subject:** AI governance authority (draft, edit) · second authority (activate)
- **resource:** AGG-AI-ROUTING
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RTG-EDIT

- **command:** CMD-RTG-EDIT
- **subject:** AI governance authority (draft, edit) · second authority (activate)
- **resource:** AGG-AI-ROUTING
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RTG-ACTIVATE

- **command:** CMD-RTG-ACTIVATE
- **subject:** AI governance authority (draft, edit) · second authority (activate)
- **resource:** AGG-AI-ROUTING
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** approver ≠ author
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RTG-DISCARD

- **command:** CMD-RTG-DISCARD
- **subject:** AI governance authority (draft, edit) · second authority (activate)
- **resource:** AGG-AI-ROUTING
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-TOL-REGISTER

- **command:** CMD-TOL-REGISTER
- **subject:** AI platform engineer (register) · Security Officer (activate, disable)
- **resource:** AGG-AI-TOOL
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-TOL-ACTIVATE

- **command:** CMD-TOL-ACTIVATE
- **subject:** AI platform engineer (register) · Security Officer (activate, disable)
- **resource:** AGG-AI-TOOL
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** Security Officer
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-TOL-DISABLE

- **command:** CMD-TOL-DISABLE
- **subject:** AI platform engineer (register) · Security Officer (activate, disable)
- **resource:** AGG-AI-TOOL
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-TOL-ENABLE

- **command:** CMD-TOL-ENABLE
- **subject:** Security Officer (enable)
- **resource:** AGG-AI-TOOL
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-TOL-RETIRE

- **command:** CMD-TOL-RETIRE
- **subject:** Security Officer (retire)
- **resource:** AGG-AI-TOOL
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-EVS-DRAFT

- **command:** CMD-EVS-DRAFT
- **subject:** AI governance (draft, edit) · second authority (activate)
- **resource:** AGG-EVAL-SUITE
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-EVS-EDIT

- **command:** CMD-EVS-EDIT
- **subject:** AI governance (draft, edit) · second authority (activate)
- **resource:** AGG-EVAL-SUITE
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-EVS-ACTIVATE

- **command:** CMD-EVS-ACTIVATE
- **subject:** AI governance (draft, edit) · second authority (activate)
- **resource:** AGG-EVAL-SUITE
- **context_conditions:** tenant match; object visible
- **segregation_of_duties:** approver ≠ author
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

## query_policies

_7 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-AIR-GET | QRY-AIR-GET | requester; Auditor (metadata) | DENY (not-found shape) |
| POL-AIR-CONTEXT | QRY-AIR-CONTEXT | requester if cleared; Auditor | DENY (not-found shape) |
| POL-AIRS-QUEUE | QRY-AIRS-QUEUE | reviewers authorized on targets | DENY (not-found shape) |
| POL-MDL-LIST | QRY-MDL-LIST | AI governance, Auditor | DENY (not-found shape) |
| POL-RTG-ACTIVE | QRY-RTG-ACTIVE | AI governance, Security Officer | DENY (not-found shape) |
| POL-TOL-LIST | QRY-TOL-LIST | AI governance, Security Officer | DENY (not-found shape) |
| POL-AI-USAGE | QRY-AI-USAGE | Administrator, finance | DENY (not-found shape) |

## ai_policy_baseline

_3 items_

| id | rule | overridable |
|---|---|---|
| PB-12 | AI requests execute and retrieve with the requesting user's authorization only | no |
| PB-13 | classified context never sent to external models | no |
| PB-14 | AIL5 forbidden; R2 maximum AIL3 | no |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-AIR-SUBMIT
  command: CMD-AIR-SUBMIT
  subject: any authorized user (submit, cancel)
  resource: AGG-AI-REQUEST
  context_conditions: tenant match; operation allowed by routing and matrix
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AIR-CANCEL
  command: CMD-AIR-CANCEL
  subject: any authorized user (submit, cancel)
  resource: AGG-AI-REQUEST
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AIRS-START-REVIEW
  command: CMD-AIRS-START-REVIEW
  subject: reviewer authorized on the target (review, accept, reject)
  resource: AGG-AI-RESULT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AIRS-ACCEPT
  command: CMD-AIRS-ACCEPT
  subject: reviewer authorized on the target (review, accept, reject)
  resource: AGG-AI-RESULT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AIRS-ACCEPT-PARTIALLY
  command: CMD-AIRS-ACCEPT-PARTIALLY
  subject: reviewer authorized on the target (review, accept, reject)
  resource: AGG-AI-RESULT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AIRS-REJECT
  command: CMD-AIRS-REJECT
  subject: reviewer authorized on the target (review, accept, reject)
  resource: AGG-AI-RESULT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MDL-REGISTER
  command: CMD-MDL-REGISTER
  subject: AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
  resource: AGG-MODEL-VERSION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MDL-START-EVALUATION
  command: CMD-MDL-START-EVALUATION
  subject: AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
  resource: AGG-MODEL-VERSION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MDL-APPROVE
  command: CMD-MDL-APPROVE
  subject: AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
  resource: AGG-MODEL-VERSION
  context_conditions: tenant match; object visible
  segregation_of_duties: approver ≠ registrar
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MDL-FAIL-EVALUATION
  command: CMD-MDL-FAIL-EVALUATION
  subject: AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
  resource: AGG-MODEL-VERSION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MDL-STAGE
  command: CMD-MDL-STAGE
  subject: AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
  resource: AGG-MODEL-VERSION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MDL-PROMOTE
  command: CMD-MDL-PROMOTE
  subject: AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
  resource: AGG-MODEL-VERSION
  context_conditions: tenant match; object visible
  segregation_of_duties: approver ≠ stager
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MDL-DEPRECATE
  command: CMD-MDL-DEPRECATE
  subject: AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
  resource: AGG-MODEL-VERSION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MDL-REINSTATE
  command: CMD-MDL-REINSTATE
  subject: AI platform engineer (register, evaluate, stage, deprecate) · AI governance authority (approve, promote, reinstate)
  resource: AGG-MODEL-VERSION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MDL-RETIRE
  command: CMD-MDL-RETIRE
  subject: AI governance authority (retire)
  resource: AGG-MODEL-VERSION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RTG-DRAFT
  command: CMD-RTG-DRAFT
  subject: AI governance authority (draft, edit) · second authority (activate)
  resource: AGG-AI-ROUTING
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RTG-EDIT
  command: CMD-RTG-EDIT
  subject: AI governance authority (draft, edit) · second authority (activate)
  resource: AGG-AI-ROUTING
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RTG-ACTIVATE
  command: CMD-RTG-ACTIVATE
  subject: AI governance authority (draft, edit) · second authority (activate)
  resource: AGG-AI-ROUTING
  context_conditions: tenant match; object visible
  segregation_of_duties: approver ≠ author
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RTG-DISCARD
  command: CMD-RTG-DISCARD
  subject: AI governance authority (draft, edit) · second authority (activate)
  resource: AGG-AI-ROUTING
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TOL-REGISTER
  command: CMD-TOL-REGISTER
  subject: AI platform engineer (register) · Security Officer (activate, disable)
  resource: AGG-AI-TOOL
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TOL-ACTIVATE
  command: CMD-TOL-ACTIVATE
  subject: AI platform engineer (register) · Security Officer (activate, disable)
  resource: AGG-AI-TOOL
  context_conditions: tenant match; object visible
  segregation_of_duties: Security Officer
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TOL-DISABLE
  command: CMD-TOL-DISABLE
  subject: AI platform engineer (register) · Security Officer (activate, disable)
  resource: AGG-AI-TOOL
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TOL-ENABLE
  command: CMD-TOL-ENABLE
  subject: Security Officer (enable)
  resource: AGG-AI-TOOL
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TOL-RETIRE
  command: CMD-TOL-RETIRE
  subject: Security Officer (retire)
  resource: AGG-AI-TOOL
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-EVS-DRAFT
  command: CMD-EVS-DRAFT
  subject: AI governance (draft, edit) · second authority (activate)
  resource: AGG-EVAL-SUITE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-EVS-EDIT
  command: CMD-EVS-EDIT
  subject: AI governance (draft, edit) · second authority (activate)
  resource: AGG-EVAL-SUITE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-EVS-ACTIVATE
  command: CMD-EVS-ACTIVATE
  subject: AI governance (draft, edit) · second authority (activate)
  resource: AGG-EVAL-SUITE
  context_conditions: tenant match; object visible
  segregation_of_duties: approver ≠ author
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-AIR-GET
  query: QRY-AIR-GET
  subject: requester; Auditor (metadata)
  otherwise: DENY (not-found shape)
- id: POL-AIR-CONTEXT
  query: QRY-AIR-CONTEXT
  subject: requester if cleared; Auditor
  otherwise: DENY (not-found shape)
- id: POL-AIRS-QUEUE
  query: QRY-AIRS-QUEUE
  subject: reviewers authorized on targets
  otherwise: DENY (not-found shape)
- id: POL-MDL-LIST
  query: QRY-MDL-LIST
  subject: AI governance, Auditor
  otherwise: DENY (not-found shape)
- id: POL-RTG-ACTIVE
  query: QRY-RTG-ACTIVE
  subject: AI governance, Security Officer
  otherwise: DENY (not-found shape)
- id: POL-TOL-LIST
  query: QRY-TOL-LIST
  subject: AI governance, Security Officer
  otherwise: DENY (not-found shape)
- id: POL-AI-USAGE
  query: QRY-AI-USAGE
  subject: Administrator, finance
  otherwise: DENY (not-found shape)
ai_policy_baseline:
- id: PB-12
  rule: AI requests execute and retrieve with the requesting user's authorization only
  overridable: false
- id: PB-13
  rule: classified context never sent to external models
  overridable: false
- id: PB-14
  rule: AIL5 forbidden; R2 maximum AIL3
  overridable: false
```

</details>
