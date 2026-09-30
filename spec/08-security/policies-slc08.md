---
id: POLICIES-SLC08
type: policy-decision-tables
title: Policy Decision Tables — SLC-08
wave: W6
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Policy Decision Tables — SLC-08

## command_policies

_24 items_

### POL-DRQ-CREATE

- **command:** CMD-DRQ-CREATE
- **subject:** Analyst / Planner / Manager (create, add, cite, open, withdraw)
- **resource:** AGG-DECISION-REQUEST
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-DRQ-ADD-OPTION

- **command:** CMD-DRQ-ADD-OPTION
- **subject:** Analyst / Planner / Manager (create, add, cite, open, withdraw)
- **resource:** AGG-DECISION-REQUEST
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-DRQ-CITE

- **command:** CMD-DRQ-CITE
- **subject:** Analyst / Planner / Manager (create, add, cite, open, withdraw)
- **resource:** AGG-DECISION-REQUEST
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-DRQ-OPEN

- **command:** CMD-DRQ-OPEN
- **subject:** Analyst / Planner / Manager (create, add, cite, open, withdraw)
- **resource:** AGG-DECISION-REQUEST
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-DRQ-WITHDRAW

- **command:** CMD-DRQ-WITHDRAW
- **subject:** Analyst / Planner / Manager (create, add, cite, open, withdraw)
- **resource:** AGG-DECISION-REQUEST
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-DEC-RECORD

- **command:** CMD-DEC-RECORD
- **subject:** authority holder (record) · higher authority (annul)
- **resource:** AGG-DECISION
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** AuthorityCheck (BRL-003)
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit; mfa

### POL-DEC-ANNUL

- **command:** CMD-DEC-ANNUL
- **subject:** authority holder (record) · higher authority (annul)
- **resource:** AGG-DECISION
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** authority at higher scope
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit; mfa

### POL-PLN-CREATE

- **command:** CMD-PLN-CREATE
- **subject:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
- **resource:** AGG-PLAN
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLN-SUSPEND

- **command:** CMD-PLN-SUSPEND
- **subject:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
- **resource:** AGG-PLAN
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLN-RESUME

- **command:** CMD-PLN-RESUME
- **subject:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
- **resource:** AGG-PLAN
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLN-COMPLETE

- **command:** CMD-PLN-COMPLETE
- **subject:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
- **resource:** AGG-PLAN
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLN-CLOSE

- **command:** CMD-PLN-CLOSE
- **subject:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
- **resource:** AGG-PLAN
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLN-CANCEL

- **command:** CMD-PLN-CANCEL
- **subject:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
- **resource:** AGG-PLAN
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLN-RECLASSIFY

- **command:** CMD-PLN-RECLASSIFY
- **subject:** Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
- **resource:** AGG-PLAN
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLV-DRAFT

- **command:** CMD-PLV-DRAFT
- **subject:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)
- **resource:** AGG-PLAN-VERSION
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLV-EDIT

- **command:** CMD-PLV-EDIT
- **subject:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)
- **resource:** AGG-PLAN-VERSION
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLV-SUBMIT

- **command:** CMD-PLV-SUBMIT
- **subject:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)
- **resource:** AGG-PLAN-VERSION
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLV-RETURN

- **command:** CMD-PLV-RETURN
- **subject:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)
- **resource:** AGG-PLAN-VERSION
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLV-APPROVE

- **command:** CMD-PLV-APPROVE
- **subject:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)
- **resource:** AGG-PLAN-VERSION
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** approver ≠ author (REQ-OPS-005); AuthorityCheck plan-approval
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit; mfa

### POL-PLV-REJECT

- **command:** CMD-PLV-REJECT
- **subject:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)
- **resource:** AGG-PLAN-VERSION
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLV-AMEND-MINOR

- **command:** CMD-PLV-AMEND-MINOR
- **subject:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)
- **resource:** AGG-PLAN-VERSION
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-PLV-DISCARD

- **command:** CMD-PLV-DISCARD
- **subject:** Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve, return, reject)
- **resource:** AGG-PLAN-VERSION
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-OUT-RECORD

- **command:** CMD-OUT-RECORD
- **subject:** Planner / owner (record, correct)
- **resource:** AGG-OUTCOME-TRACKER
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

### POL-OUT-CORRECT

- **command:** CMD-OUT-CORRECT
- **subject:** Planner / owner (record, correct)
- **resource:** AGG-OUTCOME-TRACKER
- **context_conditions:** tenant match; object visible; org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape)
- **obligations:** audit

## query_policies

_9 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-DRQ-GET | QRY-DRQ-GET | label rule; required-authority holders in scope | DENY (not-found shape) |
| POL-DRQ-LIST | QRY-DRQ-LIST | allowed_scope | DENY (not-found shape) |
| POL-DEC-GET | QRY-DEC-GET | label rule | DENY (not-found shape) |
| POL-DEC-BASIS | QRY-DEC-BASIS | label rule; Auditor | DENY (not-found shape) |
| POL-PLN-GET | QRY-PLN-GET | label rule | DENY (not-found shape) |
| POL-PLV-LIST | QRY-PLV-LIST | label rule | DENY (not-found shape) |
| POL-PLV-DIFF | QRY-PLV-DIFF | label rule | DENY (not-found shape) |
| POL-PLN-PROGRESS | QRY-PLN-PROGRESS | label rule; visible tasks only | DENY (not-found shape) |
| POL-OUT-SERIES | QRY-OUT-SERIES | label rule | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-DRQ-CREATE
  command: CMD-DRQ-CREATE
  subject: Analyst / Planner / Manager (create, add, cite, open, withdraw)
  resource: AGG-DECISION-REQUEST
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-DRQ-ADD-OPTION
  command: CMD-DRQ-ADD-OPTION
  subject: Analyst / Planner / Manager (create, add, cite, open, withdraw)
  resource: AGG-DECISION-REQUEST
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-DRQ-CITE
  command: CMD-DRQ-CITE
  subject: Analyst / Planner / Manager (create, add, cite, open, withdraw)
  resource: AGG-DECISION-REQUEST
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-DRQ-OPEN
  command: CMD-DRQ-OPEN
  subject: Analyst / Planner / Manager (create, add, cite, open, withdraw)
  resource: AGG-DECISION-REQUEST
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-DRQ-WITHDRAW
  command: CMD-DRQ-WITHDRAW
  subject: Analyst / Planner / Manager (create, add, cite, open, withdraw)
  resource: AGG-DECISION-REQUEST
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-DEC-RECORD
  command: CMD-DEC-RECORD
  subject: authority holder (record) · higher authority (annul)
  resource: AGG-DECISION
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: AuthorityCheck (BRL-003)
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit; mfa
- id: POL-DEC-ANNUL
  command: CMD-DEC-ANNUL
  subject: authority holder (record) · higher authority (annul)
  resource: AGG-DECISION
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: authority at higher scope
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit; mfa
- id: POL-PLN-CREATE
  command: CMD-PLN-CREATE
  subject: Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
  resource: AGG-PLAN
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLN-SUSPEND
  command: CMD-PLN-SUSPEND
  subject: Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
  resource: AGG-PLAN
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLN-RESUME
  command: CMD-PLN-RESUME
  subject: Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
  resource: AGG-PLAN
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLN-COMPLETE
  command: CMD-PLN-COMPLETE
  subject: Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
  resource: AGG-PLAN
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLN-CLOSE
  command: CMD-PLN-CLOSE
  subject: Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
  resource: AGG-PLAN
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLN-CANCEL
  command: CMD-PLN-CANCEL
  subject: Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
  resource: AGG-PLAN
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLN-RECLASSIFY
  command: CMD-PLN-RECLASSIFY
  subject: Planner / owner (create, suspend, resume, complete, close) · authority (cancel) · Security Officer (reclassify)
  resource: AGG-PLAN
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLV-DRAFT
  command: CMD-PLV-DRAFT
  subject: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve,
    return, reject)
  resource: AGG-PLAN-VERSION
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLV-EDIT
  command: CMD-PLV-EDIT
  subject: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve,
    return, reject)
  resource: AGG-PLAN-VERSION
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLV-SUBMIT
  command: CMD-PLV-SUBMIT
  subject: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve,
    return, reject)
  resource: AGG-PLAN-VERSION
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLV-RETURN
  command: CMD-PLV-RETURN
  subject: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve,
    return, reject)
  resource: AGG-PLAN-VERSION
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLV-APPROVE
  command: CMD-PLV-APPROVE
  subject: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve,
    return, reject)
  resource: AGG-PLAN-VERSION
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: approver ≠ author (REQ-OPS-005); AuthorityCheck plan-approval
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit; mfa
- id: POL-PLV-REJECT
  command: CMD-PLV-REJECT
  subject: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve,
    return, reject)
  resource: AGG-PLAN-VERSION
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLV-AMEND-MINOR
  command: CMD-PLV-AMEND-MINOR
  subject: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve,
    return, reject)
  resource: AGG-PLAN-VERSION
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-PLV-DISCARD
  command: CMD-PLV-DISCARD
  subject: Planner (draft, edit, submit, discard, minor amend) · approver with plan-approval authority ≠ author (approve,
    return, reject)
  resource: AGG-PLAN-VERSION
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-OUT-RECORD
  command: CMD-OUT-RECORD
  subject: Planner / owner (record, correct)
  resource: AGG-OUTCOME-TRACKER
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-OUT-CORRECT
  command: CMD-OUT-CORRECT
  subject: Planner / owner (record, correct)
  resource: AGG-OUTCOME-TRACKER
  context_conditions: tenant match; object visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
query_policies:
- id: POL-DRQ-GET
  query: QRY-DRQ-GET
  subject: label rule; required-authority holders in scope
  otherwise: DENY (not-found shape)
- id: POL-DRQ-LIST
  query: QRY-DRQ-LIST
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-DEC-GET
  query: QRY-DEC-GET
  subject: label rule
  otherwise: DENY (not-found shape)
- id: POL-DEC-BASIS
  query: QRY-DEC-BASIS
  subject: label rule; Auditor
  otherwise: DENY (not-found shape)
- id: POL-PLN-GET
  query: QRY-PLN-GET
  subject: label rule
  otherwise: DENY (not-found shape)
- id: POL-PLV-LIST
  query: QRY-PLV-LIST
  subject: label rule
  otherwise: DENY (not-found shape)
- id: POL-PLV-DIFF
  query: QRY-PLV-DIFF
  subject: label rule
  otherwise: DENY (not-found shape)
- id: POL-PLN-PROGRESS
  query: QRY-PLN-PROGRESS
  subject: label rule; visible tasks only
  otherwise: DENY (not-found shape)
- id: POL-OUT-SERIES
  query: QRY-OUT-SERIES
  subject: label rule
  otherwise: DENY (not-found shape)
```

</details>
