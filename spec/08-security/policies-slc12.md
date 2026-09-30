---
id: POLICIES-SLC12
type: policy-decision-tables
title: Policy Decision Tables — SLC-12
wave: W6
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Policy Decision Tables — SLC-12

## command_policies

_29 items_

| id | command | subject | resource | context_conditions | segregation_of_duties | decision | otherwise | obligations |
|---|---|---|---|---|---|---|---|---|
| POL-PTM-DEFINE | CMD-PTM-DEFINE | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | AGG-PRODUCT-TEMPLATE | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-PTM-EDIT | CMD-PTM-EDIT | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | AGG-PRODUCT-TEMPLATE | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-PTM-ACTIVATE | CMD-PTM-ACTIVATE | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | AGG-PRODUCT-TEMPLATE | tenant match; object visible | approver ≠ author | ALLOW | DENY | audit |
| POL-PTM-RETIRE | CMD-PTM-RETIRE | Knowledge Manager / Analysis lead (define, edit) · second approver (activate) | AGG-PRODUCT-TEMPLATE | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-PRD-CREATE | CMD-PRD-CREATE | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | AGG-PRODUCT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-PRD-GENERATE | CMD-PRD-GENERATE | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | AGG-PRODUCT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-PRD-EDIT-NARRATIVE | CMD-PRD-EDIT-NARRATIVE | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | AGG-PRODUCT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-PRD-SUBMIT | CMD-PRD-SUBMIT | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | AGG-PRODUCT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-PRD-RETURN | CMD-PRD-RETURN | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | AGG-PRODUCT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-PRD-APPROVE | CMD-PRD-APPROVE | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | AGG-PRODUCT | tenant match; object visible | reviewer ≠ author | ALLOW | DENY | audit |
| POL-PRD-WITHDRAW | CMD-PRD-WITHDRAW | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | AGG-PRODUCT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-PRD-DISCARD | CMD-PRD-DISCARD | Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw) | AGG-PRODUCT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-DST-DISTRIBUTE | CMD-DST-DISTRIBUTE | Manager / product owner | AGG-DISTRIBUTION | tenant match; object visible | — | ALLOW | DENY | audit; watermark |
| POL-DST-CANCEL | CMD-DST-CANCEL | Manager / product owner | AGG-DISTRIBUTION | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-KNO-DRAFT | CMD-KNO-DRAFT | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | AGG-KNOWLEDGE-OBJECT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-KNO-EDIT | CMD-KNO-EDIT | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | AGG-KNOWLEDGE-OBJECT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-KNO-SUBMIT | CMD-KNO-SUBMIT | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | AGG-KNOWLEDGE-OBJECT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-KNO-RETURN | CMD-KNO-RETURN | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | AGG-KNOWLEDGE-OBJECT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-KNO-PUBLISH | CMD-KNO-PUBLISH | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | AGG-KNOWLEDGE-OBJECT | tenant match; object visible | reviewer ≠ author; domain authority for procedures/policy knowledge | ALLOW | DENY | audit |
| POL-KNO-REJECT | CMD-KNO-REJECT | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | AGG-KNOWLEDGE-OBJECT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-KNO-RECORD-REUSE | CMD-KNO-RECORD-REUSE | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | AGG-KNOWLEDGE-OBJECT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-KNO-RETIRE | CMD-KNO-RETIRE | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | AGG-KNOWLEDGE-OBJECT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-KNO-DISCARD | CMD-KNO-DISCARD | any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse) | AGG-KNOWLEDGE-OBJECT | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-ARC-RETRY-INGEST | CMD-ARC-RETRY-INGEST | Archivist (retry, repair, migrate) · transfer authority (transfer) | AGG-ARCHIVE-PACKAGE | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-ARC-REPAIR | CMD-ARC-REPAIR | Archivist (retry, repair, migrate) · transfer authority (transfer) | AGG-ARCHIVE-PACKAGE | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-ARC-MIGRATE-FORMAT | CMD-ARC-MIGRATE-FORMAT | Archivist (retry, repair, migrate) · transfer authority (transfer) | AGG-ARCHIVE-PACKAGE | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-ARC-TRANSFER | CMD-ARC-TRANSFER | Archivist (retry, repair, migrate) · transfer authority (transfer) | AGG-ARCHIVE-PACKAGE | tenant match; object visible | transfer authority decision | ALLOW | DENY | audit |
| POL-REC-REQUEST | CMD-REC-REQUEST | Auditor / Legal / Analyst (request, cancel) | AGG-RECONSTRUCTION | tenant match; object visible | — | ALLOW | DENY | audit |
| POL-REC-CANCEL | CMD-REC-CANCEL | Auditor / Legal / Analyst (request, cancel) | AGG-RECONSTRUCTION | tenant match; object visible | — | ALLOW | DENY | audit |

## query_policies

_8 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-PRD-GET | QRY-PRD-GET | audience + label rule | DENY (not-found shape) |
| POL-PRD-LIST | QRY-PRD-LIST | allowed_scope | DENY (not-found shape) |
| POL-DST-LOG | QRY-DST-LOG | distributor, Security Officer, Auditor | DENY (not-found shape) |
| POL-KNO-SEARCH | QRY-KNO-SEARCH | any user; label rule | DENY (not-found shape) |
| POL-KNO-SUGGEST | QRY-KNO-SUGGEST | planner; label rule | DENY (not-found shape) |
| POL-ARC-SEARCH | QRY-ARC-SEARCH | Archivist; label rule | DENY (not-found shape) |
| POL-ARC-RETRIEVE | QRY-ARC-RETRIEVE | authorized by package label and purpose | DENY (not-found shape) |
| POL-REC-REPORT | QRY-REC-REPORT | requester, Auditor | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-PTM-DEFINE
  command: CMD-PTM-DEFINE
  subject: Knowledge Manager / Analysis lead (define, edit) · second approver (activate)
  resource: AGG-PRODUCT-TEMPLATE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PTM-EDIT
  command: CMD-PTM-EDIT
  subject: Knowledge Manager / Analysis lead (define, edit) · second approver (activate)
  resource: AGG-PRODUCT-TEMPLATE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PTM-ACTIVATE
  command: CMD-PTM-ACTIVATE
  subject: Knowledge Manager / Analysis lead (define, edit) · second approver (activate)
  resource: AGG-PRODUCT-TEMPLATE
  context_conditions: tenant match; object visible
  segregation_of_duties: approver ≠ author
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PTM-RETIRE
  command: CMD-PTM-RETIRE
  subject: Knowledge Manager / Analysis lead (define, edit) · second approver (activate)
  resource: AGG-PRODUCT-TEMPLATE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PRD-CREATE
  command: CMD-PRD-CREATE
  subject: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)
  resource: AGG-PRODUCT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PRD-GENERATE
  command: CMD-PRD-GENERATE
  subject: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)
  resource: AGG-PRODUCT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PRD-EDIT-NARRATIVE
  command: CMD-PRD-EDIT-NARRATIVE
  subject: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)
  resource: AGG-PRODUCT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PRD-SUBMIT
  command: CMD-PRD-SUBMIT
  subject: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)
  resource: AGG-PRODUCT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PRD-RETURN
  command: CMD-PRD-RETURN
  subject: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)
  resource: AGG-PRODUCT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PRD-APPROVE
  command: CMD-PRD-APPROVE
  subject: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)
  resource: AGG-PRODUCT
  context_conditions: tenant match; object visible
  segregation_of_duties: reviewer ≠ author
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PRD-WITHDRAW
  command: CMD-PRD-WITHDRAW
  subject: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)
  resource: AGG-PRODUCT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PRD-DISCARD
  command: CMD-PRD-DISCARD
  subject: Analyst / Planner (create, generate, edit, submit, discard) · reviewer (return, approve) · Manager (withdraw)
  resource: AGG-PRODUCT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-DST-DISTRIBUTE
  command: CMD-DST-DISTRIBUTE
  subject: Manager / product owner
  resource: AGG-DISTRIBUTION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; watermark
- id: POL-DST-CANCEL
  command: CMD-DST-CANCEL
  subject: Manager / product owner
  resource: AGG-DISTRIBUTION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-KNO-DRAFT
  command: CMD-KNO-DRAFT
  subject: any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)
  resource: AGG-KNOWLEDGE-OBJECT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-KNO-EDIT
  command: CMD-KNO-EDIT
  subject: any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)
  resource: AGG-KNOWLEDGE-OBJECT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-KNO-SUBMIT
  command: CMD-KNO-SUBMIT
  subject: any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)
  resource: AGG-KNOWLEDGE-OBJECT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-KNO-RETURN
  command: CMD-KNO-RETURN
  subject: any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)
  resource: AGG-KNOWLEDGE-OBJECT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-KNO-PUBLISH
  command: CMD-KNO-PUBLISH
  subject: any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)
  resource: AGG-KNOWLEDGE-OBJECT
  context_conditions: tenant match; object visible
  segregation_of_duties: reviewer ≠ author; domain authority for procedures/policy knowledge
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-KNO-REJECT
  command: CMD-KNO-REJECT
  subject: any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)
  resource: AGG-KNOWLEDGE-OBJECT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-KNO-RECORD-REUSE
  command: CMD-KNO-RECORD-REUSE
  subject: any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)
  resource: AGG-KNOWLEDGE-OBJECT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-KNO-RETIRE
  command: CMD-KNO-RETIRE
  subject: any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)
  resource: AGG-KNOWLEDGE-OBJECT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-KNO-DISCARD
  command: CMD-KNO-DISCARD
  subject: any user (draft lessons) · Knowledge Manager (review, publish, retire) · planner (record reuse)
  resource: AGG-KNOWLEDGE-OBJECT
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ARC-RETRY-INGEST
  command: CMD-ARC-RETRY-INGEST
  subject: Archivist (retry, repair, migrate) · transfer authority (transfer)
  resource: AGG-ARCHIVE-PACKAGE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ARC-REPAIR
  command: CMD-ARC-REPAIR
  subject: Archivist (retry, repair, migrate) · transfer authority (transfer)
  resource: AGG-ARCHIVE-PACKAGE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ARC-MIGRATE-FORMAT
  command: CMD-ARC-MIGRATE-FORMAT
  subject: Archivist (retry, repair, migrate) · transfer authority (transfer)
  resource: AGG-ARCHIVE-PACKAGE
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ARC-TRANSFER
  command: CMD-ARC-TRANSFER
  subject: Archivist (retry, repair, migrate) · transfer authority (transfer)
  resource: AGG-ARCHIVE-PACKAGE
  context_conditions: tenant match; object visible
  segregation_of_duties: transfer authority decision
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-REC-REQUEST
  command: CMD-REC-REQUEST
  subject: Auditor / Legal / Analyst (request, cancel)
  resource: AGG-RECONSTRUCTION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-REC-CANCEL
  command: CMD-REC-CANCEL
  subject: Auditor / Legal / Analyst (request, cancel)
  resource: AGG-RECONSTRUCTION
  context_conditions: tenant match; object visible
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-PRD-GET
  query: QRY-PRD-GET
  subject: audience + label rule
  otherwise: DENY (not-found shape)
- id: POL-PRD-LIST
  query: QRY-PRD-LIST
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-DST-LOG
  query: QRY-DST-LOG
  subject: distributor, Security Officer, Auditor
  otherwise: DENY (not-found shape)
- id: POL-KNO-SEARCH
  query: QRY-KNO-SEARCH
  subject: any user; label rule
  otherwise: DENY (not-found shape)
- id: POL-KNO-SUGGEST
  query: QRY-KNO-SUGGEST
  subject: planner; label rule
  otherwise: DENY (not-found shape)
- id: POL-ARC-SEARCH
  query: QRY-ARC-SEARCH
  subject: Archivist; label rule
  otherwise: DENY (not-found shape)
- id: POL-ARC-RETRIEVE
  query: QRY-ARC-RETRIEVE
  subject: authorized by package label and purpose
  otherwise: DENY (not-found shape)
- id: POL-REC-REPORT
  query: QRY-REC-REPORT
  subject: requester, Auditor
  otherwise: DENY (not-found shape)
```

</details>
