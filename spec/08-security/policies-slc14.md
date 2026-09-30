---
id: POLICIES-SLC14
type: policy-decision-tables
title: Policy Decision Tables — SLC-14
wave: W6
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Policy Decision Tables — SLC-14

## command_policies

_14 items_

| id | command | subject | resource | context_conditions | segregation_of_duties | decision | otherwise | obligations |
|---|---|---|---|---|---|---|---|---|
| POL-CRQ-DRAFT | CMD-CRQ-DRAFT | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | AGG-COLLECTION-REQUIREMENT | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CRQ-EDIT | CMD-CRQ-EDIT | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | AGG-COLLECTION-REQUIREMENT | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CRQ-SUBMIT | CMD-CRQ-SUBMIT | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | AGG-COLLECTION-REQUIREMENT | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CRQ-APPROVE | CMD-CRQ-APPROVE | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | AGG-COLLECTION-REQUIREMENT | tenant match; area within scope | approver ≠ requester | ALLOW | DENY | audit |
| POL-CRQ-REJECT | CMD-CRQ-REJECT | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | AGG-COLLECTION-REQUIREMENT | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CRQ-AMEND | CMD-CRQ-AMEND | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | AGG-COLLECTION-REQUIREMENT | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CRQ-MARK-SATISFIED | CMD-CRQ-MARK-SATISFIED | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | AGG-COLLECTION-REQUIREMENT | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CRQ-CANCEL | CMD-CRQ-CANCEL | Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend) | AGG-COLLECTION-REQUIREMENT | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CPL-CREATE | CMD-CPL-CREATE | collection planner | AGG-COLLECTION-PLAN | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CPL-ADD-ACTIVITY | CMD-CPL-ADD-ACTIVITY | collection planner | AGG-COLLECTION-PLAN | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CPL-REMOVE-ACTIVITY | CMD-CPL-REMOVE-ACTIVITY | collection planner | AGG-COLLECTION-PLAN | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CPL-ACTIVATE | CMD-CPL-ACTIVATE | collection planner | AGG-COLLECTION-PLAN | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CPL-COMPLETE | CMD-CPL-COMPLETE | collection planner | AGG-COLLECTION-PLAN | tenant match; area within scope | — | ALLOW | DENY | audit |
| POL-CPL-CANCEL | CMD-CPL-CANCEL | collection planner | AGG-COLLECTION-PLAN | tenant match; area within scope | — | ALLOW | DENY | audit |

## query_policies

_4 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-CRQ-GET | QRY-CRQ-GET | requester, collection managers; label rule | DENY (not-found shape) |
| POL-CRQ-BOARD | QRY-CRQ-BOARD | allowed_scope | DENY (not-found shape) |
| POL-CPL-GET | QRY-CPL-GET | planner scope | DENY (not-found shape) |
| POL-CRQ-EVIDENCE | QRY-CRQ-EVIDENCE | requester, collection managers | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-CRQ-DRAFT
  command: CMD-CRQ-DRAFT
  subject: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)
  resource: AGG-COLLECTION-REQUIREMENT
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRQ-EDIT
  command: CMD-CRQ-EDIT
  subject: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)
  resource: AGG-COLLECTION-REQUIREMENT
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRQ-SUBMIT
  command: CMD-CRQ-SUBMIT
  subject: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)
  resource: AGG-COLLECTION-REQUIREMENT
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRQ-APPROVE
  command: CMD-CRQ-APPROVE
  subject: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)
  resource: AGG-COLLECTION-REQUIREMENT
  context_conditions: tenant match; area within scope
  segregation_of_duties: approver ≠ requester
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRQ-REJECT
  command: CMD-CRQ-REJECT
  subject: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)
  resource: AGG-COLLECTION-REQUIREMENT
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRQ-AMEND
  command: CMD-CRQ-AMEND
  subject: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)
  resource: AGG-COLLECTION-REQUIREMENT
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRQ-MARK-SATISFIED
  command: CMD-CRQ-MARK-SATISFIED
  subject: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)
  resource: AGG-COLLECTION-REQUIREMENT
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CRQ-CANCEL
  command: CMD-CRQ-CANCEL
  subject: Analyst / any requester (draft, edit, submit, satisfy, cancel) · collection manager (approve, reject, amend)
  resource: AGG-COLLECTION-REQUIREMENT
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CPL-CREATE
  command: CMD-CPL-CREATE
  subject: collection planner
  resource: AGG-COLLECTION-PLAN
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CPL-ADD-ACTIVITY
  command: CMD-CPL-ADD-ACTIVITY
  subject: collection planner
  resource: AGG-COLLECTION-PLAN
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CPL-REMOVE-ACTIVITY
  command: CMD-CPL-REMOVE-ACTIVITY
  subject: collection planner
  resource: AGG-COLLECTION-PLAN
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CPL-ACTIVATE
  command: CMD-CPL-ACTIVATE
  subject: collection planner
  resource: AGG-COLLECTION-PLAN
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CPL-COMPLETE
  command: CMD-CPL-COMPLETE
  subject: collection planner
  resource: AGG-COLLECTION-PLAN
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-CPL-CANCEL
  command: CMD-CPL-CANCEL
  subject: collection planner
  resource: AGG-COLLECTION-PLAN
  context_conditions: tenant match; area within scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-CRQ-GET
  query: QRY-CRQ-GET
  subject: requester, collection managers; label rule
  otherwise: DENY (not-found shape)
- id: POL-CRQ-BOARD
  query: QRY-CRQ-BOARD
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-CPL-GET
  query: QRY-CPL-GET
  subject: planner scope
  otherwise: DENY (not-found shape)
- id: POL-CRQ-EVIDENCE
  query: QRY-CRQ-EVIDENCE
  subject: requester, collection managers
  otherwise: DENY (not-found shape)
```

</details>
