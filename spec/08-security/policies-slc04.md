---
id: POLICIES-SLC04
type: policy-decision-tables
title: Policy Decision Tables — SLC-04
wave: W6
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: PB-01..PB-11 تنطبق.
---

# Policy Decision Tables — SLC-04

> PB-01..PB-11 تنطبق.

## command_policies

_19 items_

| id | command | subject | resource | context_conditions | segregation_of_duties | decision | otherwise | obligations |
|---|---|---|---|---|---|---|---|---|
| POL-CNF-RAISE | CMD-CNF-RAISE | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | AGG-CONFLICT | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-CNF-ASSIGN | CMD-CNF-ASSIGN | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | AGG-CONFLICT | tenant match; assignee cleared for every member claim | — | ALLOW | DENY (not-found shape) | audit |
| POL-CNF-START-REVIEW | CMD-CNF-START-REVIEW | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | AGG-CONFLICT | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-CNF-RESOLVE | CMD-CNF-RESOLVE | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | AGG-CONFLICT | tenant match; cleared for every member claim label | reviewer ≠ asserter of preferred claim | ALLOW | DENY (not-found shape) | audit |
| POL-CNF-ACCEPT | CMD-CNF-ACCEPT | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | AGG-CONFLICT | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-CNF-REOPEN | CMD-CNF-REOPEN | Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign) | AGG-CONFLICT | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-ER-PROPOSE | CMD-ER-PROPOSE | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | AGG-ER-CASE | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-ER-START-REVIEW | CMD-ER-START-REVIEW | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | AGG-ER-CASE | tenant match; cleared for both entity labels | — | ALLOW | DENY (not-found shape) | audit |
| POL-ER-DECIDE-MATCH | CMD-ER-DECIDE-MATCH | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | AGG-ER-CASE | tenant match; cleared for both entity labels | reviewer ≠ human proposer; second reviewer if cluster > 50 | ALLOW | DENY (not-found shape) | audit |
| POL-ER-DECIDE-NOT-MATCH | CMD-ER-DECIDE-NOT-MATCH | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | AGG-ER-CASE | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-ER-PARK | CMD-ER-PARK | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | AGG-ER-CASE | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-ER-RESUME | CMD-ER-RESUME | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | AGG-ER-CASE | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-ER-REQUEST-SPLIT | CMD-ER-REQUEST-SPLIT | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | AGG-ER-CASE | tenant match; cleared for both entity labels | — | ALLOW | DENY (not-found shape) | audit |
| POL-ER-CONFIRM-MATCH | CMD-ER-CONFIRM-MATCH | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | AGG-ER-CASE | tenant match; object visible | reviewer ≠ split requester | ALLOW | DENY (not-found shape) | audit |
| POL-ER-SPLIT | CMD-ER-SPLIT | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | AGG-ER-CASE | tenant match; object visible | reviewer ≠ split requester | ALLOW | DENY (not-found shape) | audit |
| POL-ER-WITHDRAW | CMD-ER-WITHDRAW | Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters) | AGG-ER-CASE | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-MRS-DRAFT | CMD-MRS-DRAFT | Analyst lead (draft, edit) · Administrator ≠ author (activate) | AGG-MATCH-RULESET | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-MRS-EDIT | CMD-MRS-EDIT | Analyst lead (draft, edit) · Administrator ≠ author (activate) | AGG-MATCH-RULESET | tenant match; object visible | — | ALLOW | DENY (not-found shape) | audit |
| POL-MRS-ACTIVATE | CMD-MRS-ACTIVATE | Analyst lead (draft, edit) · Administrator ≠ author (activate) | AGG-MATCH-RULESET | tenant match; object visible | approver ≠ author | ALLOW | DENY (not-found shape) | audit |

## query_policies

_6 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-CNF-LIST | QRY-CNF-LIST | Analyst; only conflicts with ≥ 2 visible member claims | DENY (not-found shape) |
| POL-CNF-GET | QRY-CNF-GET | Analyst; visibility rule INV-CNF-04 | DENY (not-found shape) |
| POL-ER-QUEUE | QRY-ER-QUEUE | Analyst; cases where both entities are visible | DENY (not-found shape) |
| POL-ER-GET | QRY-ER-GET | Analyst; both entities visible | DENY (not-found shape) |
| POL-CLUSTER-GET | QRY-CLUSTER-GET | Analyst; invisible members omitted | DENY (not-found shape) |
| POL-MRS-GET | QRY-MRS-GET | Analyst lead, Administrator | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-CNF-RAISE
  command: CMD-CNF-RAISE
  subject: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  resource: AGG-CONFLICT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-CNF-ASSIGN
  command: CMD-CNF-ASSIGN
  subject: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  resource: AGG-CONFLICT
  context_conditions: tenant match; assignee cleared for every member claim
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-CNF-START-REVIEW
  command: CMD-CNF-START-REVIEW
  subject: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  resource: AGG-CONFLICT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-CNF-RESOLVE
  command: CMD-CNF-RESOLVE
  subject: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  resource: AGG-CONFLICT
  context_conditions: tenant match; cleared for every member claim label
  segregation_of_duties: reviewer ≠ asserter of preferred claim
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-CNF-ACCEPT
  command: CMD-CNF-ACCEPT
  subject: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  resource: AGG-CONFLICT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-CNF-REOPEN
  command: CMD-CNF-REOPEN
  subject: Analyst (raise, review, resolve, accept, reopen) · Analyst lead (assign)
  resource: AGG-CONFLICT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ER-PROPOSE
  command: CMD-ER-PROPOSE
  subject: Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)
  resource: AGG-ER-CASE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ER-START-REVIEW
  command: CMD-ER-START-REVIEW
  subject: Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)
  resource: AGG-ER-CASE
  context_conditions: tenant match; cleared for both entity labels
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ER-DECIDE-MATCH
  command: CMD-ER-DECIDE-MATCH
  subject: Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)
  resource: AGG-ER-CASE
  context_conditions: tenant match; cleared for both entity labels
  segregation_of_duties: reviewer ≠ human proposer; second reviewer if cluster > 50
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ER-DECIDE-NOT-MATCH
  command: CMD-ER-DECIDE-NOT-MATCH
  subject: Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)
  resource: AGG-ER-CASE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ER-PARK
  command: CMD-ER-PARK
  subject: Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)
  resource: AGG-ER-CASE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ER-RESUME
  command: CMD-ER-RESUME
  subject: Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)
  resource: AGG-ER-CASE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ER-REQUEST-SPLIT
  command: CMD-ER-REQUEST-SPLIT
  subject: Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)
  resource: AGG-ER-CASE
  context_conditions: tenant match; cleared for both entity labels
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ER-CONFIRM-MATCH
  command: CMD-ER-CONFIRM-MATCH
  subject: Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)
  resource: AGG-ER-CASE
  context_conditions: tenant match; object visible
  segregation_of_duties: reviewer ≠ split requester
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ER-SPLIT
  command: CMD-ER-SPLIT
  subject: Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)
  resource: AGG-ER-CASE
  context_conditions: tenant match; object visible
  segregation_of_duties: reviewer ≠ split requester
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ER-WITHDRAW
  command: CMD-ER-WITHDRAW
  subject: Analyst (propose, review, decide, request split) · second Analyst (confirm/split, large clusters)
  resource: AGG-ER-CASE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-MRS-DRAFT
  command: CMD-MRS-DRAFT
  subject: Analyst lead (draft, edit) · Administrator ≠ author (activate)
  resource: AGG-MATCH-RULESET
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-MRS-EDIT
  command: CMD-MRS-EDIT
  subject: Analyst lead (draft, edit) · Administrator ≠ author (activate)
  resource: AGG-MATCH-RULESET
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-MRS-ACTIVATE
  command: CMD-MRS-ACTIVATE
  subject: Analyst lead (draft, edit) · Administrator ≠ author (activate)
  resource: AGG-MATCH-RULESET
  context_conditions: tenant match; object visible
  segregation_of_duties: approver ≠ author
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
query_policies:
- id: POL-CNF-LIST
  query: QRY-CNF-LIST
  subject: Analyst; only conflicts with ≥ 2 visible member claims
  otherwise: DENY (not-found shape)
- id: POL-CNF-GET
  query: QRY-CNF-GET
  subject: Analyst; visibility rule INV-CNF-04
  otherwise: DENY (not-found shape)
- id: POL-ER-QUEUE
  query: QRY-ER-QUEUE
  subject: Analyst; cases where both entities are visible
  otherwise: DENY (not-found shape)
- id: POL-ER-GET
  query: QRY-ER-GET
  subject: Analyst; both entities visible
  otherwise: DENY (not-found shape)
- id: POL-CLUSTER-GET
  query: QRY-CLUSTER-GET
  subject: Analyst; invisible members omitted
  otherwise: DENY (not-found shape)
- id: POL-MRS-GET
  query: QRY-MRS-GET
  subject: Analyst lead, Administrator
  otherwise: DENY (not-found shape)
```

</details>
