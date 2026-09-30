---
id: POLICIES-SLC03
type: policy-decision-tables
title: Policy Decision Tables — SLC-03
wave: W6
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: PB-01..PB-11 تنطبق.
---

# Policy Decision Tables — SLC-03

> PB-01..PB-11 تنطبق.

## command_policies

_33 items_

| id | command | subject | resource | context_conditions | segregation_of_duties | decision | otherwise | obligations |
|---|---|---|---|---|---|---|---|---|
| POL-TASK-CREATE | CMD-TASK-CREATE | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-EDIT | CMD-TASK-EDIT | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-MARK-READY | CMD-TASK-MARK-READY | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-ASSIGN | CMD-TASK-ASSIGN | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | AGG-TASK | tenant match; task visible; org scope | assignee clearance ≥ task label | ALLOW | DENY | audit |
| POL-TASK-REASSIGN | CMD-TASK-REASSIGN | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | AGG-TASK | tenant match; task visible; org scope | assignee clearance ≥ task label | ALLOW | DENY | audit |
| POL-TASK-ACCEPT | CMD-TASK-ACCEPT | assignee | AGG-TASK | tenant match; task visible; org scope; offline allowed | — | ALLOW | DENY | audit |
| POL-TASK-DECLINE | CMD-TASK-DECLINE | assignee | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-START | CMD-TASK-START | assignee | AGG-TASK | tenant match; task visible; org scope; offline allowed | — | ALLOW | DENY | audit |
| POL-TASK-BLOCK | CMD-TASK-BLOCK | assignee | AGG-TASK | tenant match; task visible; org scope; offline allowed | — | ALLOW | DENY | audit |
| POL-TASK-RESUME | CMD-TASK-RESUME | assignee | AGG-TASK | tenant match; task visible; org scope; offline allowed | — | ALLOW | DENY | audit |
| POL-TASK-ADD-RESULT-ITEM | CMD-TASK-ADD-RESULT-ITEM | assignee | AGG-TASK | tenant match; task visible; org scope; offline allowed | — | ALLOW | DENY | audit |
| POL-TASK-SUBMIT | CMD-TASK-SUBMIT | assignee | AGG-TASK | tenant match; task visible; org scope; offline allowed | — | ALLOW | DENY | audit |
| POL-TASK-START-REVIEW | CMD-TASK-START-REVIEW | reviewer role in scope | AGG-TASK | tenant match; task visible; org scope | reviewer ≠ assignee | ALLOW | DENY | audit |
| POL-TASK-RETURN | CMD-TASK-RETURN | reviewer | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-APPROVE | CMD-TASK-APPROVE | reviewer | AGG-TASK | tenant match; task visible; org scope | reviewer ≠ assignee (PB-06) | ALLOW | DENY | audit |
| POL-TASK-REJECT | CMD-TASK-REJECT | reviewer | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-COMPLETE | CMD-TASK-COMPLETE | reviewer or attestation role | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-CLOSE | CMD-TASK-CLOSE | owner / Planner | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-CANCEL | CMD-TASK-CANCEL | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-ESCALATE | CMD-TASK-ESCALATE | assignee, owner, Planner | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-SET-DUE | CMD-TASK-SET-DUE | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-SUSPEND | CMD-TASK-SUSPEND | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-UNSUSPEND | CMD-TASK-UNSUSPEND | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TASK-RECLASSIFY | CMD-TASK-RECLASSIFY | Planner/Manager in scope (create, edit, assign, set due, cancel, suspend) | AGG-TASK | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TTY-DEFINE | CMD-TTY-DEFINE | Administrator / Planner lead | AGG-TASK-TYPE | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TTY-EDIT | CMD-TTY-EDIT | Administrator / Planner lead | AGG-TASK-TYPE | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TTY-ACTIVATE | CMD-TTY-ACTIVATE | Administrator / Planner lead | AGG-TASK-TYPE | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-TTY-RETIRE | CMD-TTY-RETIRE | Administrator / Planner lead | AGG-TASK-TYPE | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-QUAL-RECORD | CMD-QUAL-RECORD | Resource Manager / Training Manager | AGG-QUALIFICATION-RECORD | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-QUAL-RENEW | CMD-QUAL-RENEW | Resource Manager / Training Manager | AGG-QUALIFICATION-RECORD | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-QUAL-SUSPEND | CMD-QUAL-SUSPEND | Resource Manager / Training Manager | AGG-QUALIFICATION-RECORD | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-QUAL-REINSTATE | CMD-QUAL-REINSTATE | Resource Manager / Training Manager | AGG-QUALIFICATION-RECORD | tenant match; task visible; org scope | — | ALLOW | DENY | audit |
| POL-QUAL-REVOKE | CMD-QUAL-REVOKE | Resource Manager / Training Manager | AGG-QUALIFICATION-RECORD | tenant match; task visible; org scope | — | ALLOW | DENY | audit |

## query_policies

_6 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-TASK-GET | QRY-TASK-GET | assignee, reviewer, Planner/Manager in scope; label rule | DENY (not-found shape) |
| POL-TASK-LIST | QRY-TASK-LIST | allowed_scope pre-filter | DENY (not-found shape) |
| POL-TASK-HISTORY | QRY-TASK-HISTORY | same as QRY-TASK-GET | DENY (not-found shape) |
| POL-TTY-GET | QRY-TTY-GET | any user of tenant | DENY (not-found shape) |
| POL-QUAL-LIST | QRY-QUAL-LIST | Manager/Resource Manager in scope; self | DENY (not-found shape) |
| POL-ELIG-CHECK | QRY-ELIG-CHECK | Planner/Manager in scope; internal BC04 (workload identity) | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-TASK-CREATE
  command: CMD-TASK-CREATE
  subject: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-EDIT
  command: CMD-TASK-EDIT
  subject: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-MARK-READY
  command: CMD-TASK-MARK-READY
  subject: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-ASSIGN
  command: CMD-TASK-ASSIGN
  subject: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: assignee clearance ≥ task label
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-REASSIGN
  command: CMD-TASK-REASSIGN
  subject: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: assignee clearance ≥ task label
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-ACCEPT
  command: CMD-TASK-ACCEPT
  subject: assignee
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope; offline allowed
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-DECLINE
  command: CMD-TASK-DECLINE
  subject: assignee
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-START
  command: CMD-TASK-START
  subject: assignee
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope; offline allowed
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-BLOCK
  command: CMD-TASK-BLOCK
  subject: assignee
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope; offline allowed
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-RESUME
  command: CMD-TASK-RESUME
  subject: assignee
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope; offline allowed
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-ADD-RESULT-ITEM
  command: CMD-TASK-ADD-RESULT-ITEM
  subject: assignee
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope; offline allowed
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-SUBMIT
  command: CMD-TASK-SUBMIT
  subject: assignee
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope; offline allowed
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-START-REVIEW
  command: CMD-TASK-START-REVIEW
  subject: reviewer role in scope
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: reviewer ≠ assignee
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-RETURN
  command: CMD-TASK-RETURN
  subject: reviewer
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-APPROVE
  command: CMD-TASK-APPROVE
  subject: reviewer
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: reviewer ≠ assignee (PB-06)
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-REJECT
  command: CMD-TASK-REJECT
  subject: reviewer
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-COMPLETE
  command: CMD-TASK-COMPLETE
  subject: reviewer or attestation role
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-CLOSE
  command: CMD-TASK-CLOSE
  subject: owner / Planner
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-CANCEL
  command: CMD-TASK-CANCEL
  subject: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-ESCALATE
  command: CMD-TASK-ESCALATE
  subject: assignee, owner, Planner
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-SET-DUE
  command: CMD-TASK-SET-DUE
  subject: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-SUSPEND
  command: CMD-TASK-SUSPEND
  subject: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-UNSUSPEND
  command: CMD-TASK-UNSUSPEND
  subject: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TASK-RECLASSIFY
  command: CMD-TASK-RECLASSIFY
  subject: Planner/Manager in scope (create, edit, assign, set due, cancel, suspend)
  resource: AGG-TASK
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TTY-DEFINE
  command: CMD-TTY-DEFINE
  subject: Administrator / Planner lead
  resource: AGG-TASK-TYPE
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TTY-EDIT
  command: CMD-TTY-EDIT
  subject: Administrator / Planner lead
  resource: AGG-TASK-TYPE
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TTY-ACTIVATE
  command: CMD-TTY-ACTIVATE
  subject: Administrator / Planner lead
  resource: AGG-TASK-TYPE
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-TTY-RETIRE
  command: CMD-TTY-RETIRE
  subject: Administrator / Planner lead
  resource: AGG-TASK-TYPE
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-QUAL-RECORD
  command: CMD-QUAL-RECORD
  subject: Resource Manager / Training Manager
  resource: AGG-QUALIFICATION-RECORD
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-QUAL-RENEW
  command: CMD-QUAL-RENEW
  subject: Resource Manager / Training Manager
  resource: AGG-QUALIFICATION-RECORD
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-QUAL-SUSPEND
  command: CMD-QUAL-SUSPEND
  subject: Resource Manager / Training Manager
  resource: AGG-QUALIFICATION-RECORD
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-QUAL-REINSTATE
  command: CMD-QUAL-REINSTATE
  subject: Resource Manager / Training Manager
  resource: AGG-QUALIFICATION-RECORD
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-QUAL-REVOKE
  command: CMD-QUAL-REVOKE
  subject: Resource Manager / Training Manager
  resource: AGG-QUALIFICATION-RECORD
  context_conditions: tenant match; task visible; org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-TASK-GET
  query: QRY-TASK-GET
  subject: assignee, reviewer, Planner/Manager in scope; label rule
  otherwise: DENY (not-found shape)
- id: POL-TASK-LIST
  query: QRY-TASK-LIST
  subject: allowed_scope pre-filter
  otherwise: DENY (not-found shape)
- id: POL-TASK-HISTORY
  query: QRY-TASK-HISTORY
  subject: same as QRY-TASK-GET
  otherwise: DENY (not-found shape)
- id: POL-TTY-GET
  query: QRY-TTY-GET
  subject: any user of tenant
  otherwise: DENY (not-found shape)
- id: POL-QUAL-LIST
  query: QRY-QUAL-LIST
  subject: Manager/Resource Manager in scope; self
  otherwise: DENY (not-found shape)
- id: POL-ELIG-CHECK
  query: QRY-ELIG-CHECK
  subject: Planner/Manager in scope; internal BC04 (workload identity)
  otherwise: DENY (not-found shape)
```

</details>
