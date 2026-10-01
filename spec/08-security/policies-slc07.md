---
id: POLICIES-SLC07
type: policy-decision-tables
title: Policy Decision Tables — SLC-07
wave: W6
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Policy Decision Tables — SLC-07

## command_policies

_32 items_

| id | command | subject | resource | context_conditions | segregation_of_duties | decision | otherwise | obligations |
|---|---|---|---|---|---|---|---|---|
| POL-ACS-CREATE | CMD-ACS-CREATE | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-DEFINE | CMD-ACS-DEFINE | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-OPEN | CMD-ACS-OPEN | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-ADD-HYPOTHESIS | CMD-ACS-ADD-HYPOTHESIS | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-UPDATE-HYPOTHESIS | CMD-ACS-UPDATE-HYPOTHESIS | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-ADD-ASSUMPTION | CMD-ACS-ADD-ASSUMPTION | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-RETIRE-ASSUMPTION | CMD-ACS-RETIRE-ASSUMPTION | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-SELECT-EVIDENCE | CMD-ACS-SELECT-EVIDENCE | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-DESELECT-EVIDENCE | CMD-ACS-DESELECT-EVIDENCE | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-DEFINE-SCENARIO | CMD-ACS-DEFINE-SCENARIO | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-CLOSE | CMD-ACS-CLOSE | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-REOPEN | CMD-ACS-REOPEN | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-CANCEL | CMD-ACS-CANCEL | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ACS-RECLASSIFY | CMD-ACS-RECLASSIFY | Analyst (owner) · Security Officer (reclassify) | AGG-ANALYSIS-CASE | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-AMT-REGISTER | CMD-AMT-REGISTER | Analysis lead (register) · second lead or Administrator (activate) | AGG-ANALYSIS-METHOD | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-AMT-ACTIVATE | CMD-AMT-ACTIVATE | Analysis lead (register) · second lead or Administrator (activate) | AGG-ANALYSIS-METHOD | tenant match; case visible; label rules | approver ≠ author | ALLOW | DENY (not-found shape) | audit |
| POL-AMT-DEPRECATE | CMD-AMT-DEPRECATE | Analysis lead (deprecate) | AGG-ANALYSIS-METHOD | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-AMT-RETIRE | CMD-AMT-RETIRE | Analysis lead (retire) | AGG-ANALYSIS-METHOD | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-RUN-SUBMIT | CMD-RUN-SUBMIT | Analyst (submit, reproduce, cancel) | AGG-ANALYSIS-RUN | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-RUN-REPRODUCE | CMD-RUN-REPRODUCE | Analyst (submit, reproduce, cancel) | AGG-ANALYSIS-RUN | tenant match; case visible; label rules | reproducer cleared for source run label | ALLOW | DENY (not-found shape) | audit |
| POL-RUN-CANCEL | CMD-RUN-CANCEL | Analyst (submit, reproduce, cancel) | AGG-ANALYSIS-RUN | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-FND-RECORD | CMD-FND-RECORD | Analyst (record, edit, withdraw) · peer Analyst (accept) | AGG-FINDING | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-FND-EDIT | CMD-FND-EDIT | Analyst (record, edit, withdraw) · peer Analyst (accept) | AGG-FINDING | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-FND-ACCEPT | CMD-FND-ACCEPT | Analyst (record, edit, withdraw) · peer Analyst (accept) | AGG-FINDING | tenant match; case visible; label rules | reviewer ≠ author | ALLOW | DENY (not-found shape) | audit |
| POL-FND-WITHDRAW | CMD-FND-WITHDRAW | Analyst (record, edit, withdraw) · peer Analyst (accept) | AGG-FINDING | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ASM-DRAFT | CMD-ASM-DRAFT | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | AGG-ASSESSMENT | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ASM-EDIT | CMD-ASM-EDIT | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | AGG-ASSESSMENT | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ASM-SUBMIT | CMD-ASM-SUBMIT | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | AGG-ASSESSMENT | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ASM-RETURN | CMD-ASM-RETURN | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | AGG-ASSESSMENT | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ASM-PUBLISH | CMD-ASM-PUBLISH | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | AGG-ASSESSMENT | tenant match; case visible; label rules | reviewer ≠ author | ALLOW | DENY (not-found shape) | audit |
| POL-ASM-WITHDRAW | CMD-ASM-WITHDRAW | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | AGG-ASSESSMENT | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |
| POL-ASM-DISCARD | CMD-ASM-DISCARD | Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw) | AGG-ASSESSMENT | tenant match; case visible; label rules | — | ALLOW | DENY (not-found shape) | audit |

## query_policies

_9 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-ACS-GET | QRY-ACS-GET | case label rule; selections filtered | DENY (not-found shape) |
| POL-ACS-LIST | QRY-ACS-LIST | allowed_scope | DENY (not-found shape) |
| POL-RUN-GET | QRY-RUN-GET | run label rule | DENY (not-found shape) |
| POL-RUN-ARTIFACT | QRY-RUN-ARTIFACT | run label rule; audited | DENY (not-found shape) |
| POL-SCN-COMPARE | QRY-SCN-COMPARE | case label rule | DENY (not-found shape) |
| POL-FND-LIST | QRY-FND-LIST | label rule | DENY (not-found shape) |
| POL-ASM-GET | QRY-ASM-GET | label rule; REDACT obligation for uncleared citations | DENY (not-found shape) |
| POL-ASM-VERSIONS | QRY-ASM-VERSIONS | label rule | DENY (not-found shape) |
| POL-AMT-LIST | QRY-AMT-LIST | any analyst | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-ACS-CREATE
  command: CMD-ACS-CREATE
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-DEFINE
  command: CMD-ACS-DEFINE
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-OPEN
  command: CMD-ACS-OPEN
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-ADD-HYPOTHESIS
  command: CMD-ACS-ADD-HYPOTHESIS
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-UPDATE-HYPOTHESIS
  command: CMD-ACS-UPDATE-HYPOTHESIS
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-ADD-ASSUMPTION
  command: CMD-ACS-ADD-ASSUMPTION
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-RETIRE-ASSUMPTION
  command: CMD-ACS-RETIRE-ASSUMPTION
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-SELECT-EVIDENCE
  command: CMD-ACS-SELECT-EVIDENCE
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-DESELECT-EVIDENCE
  command: CMD-ACS-DESELECT-EVIDENCE
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-DEFINE-SCENARIO
  command: CMD-ACS-DEFINE-SCENARIO
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-CLOSE
  command: CMD-ACS-CLOSE
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-REOPEN
  command: CMD-ACS-REOPEN
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-CANCEL
  command: CMD-ACS-CANCEL
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ACS-RECLASSIFY
  command: CMD-ACS-RECLASSIFY
  subject: Analyst (owner) · Security Officer (reclassify)
  resource: AGG-ANALYSIS-CASE
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-AMT-REGISTER
  command: CMD-AMT-REGISTER
  subject: Analysis lead (register) · second lead or Administrator (activate)
  resource: AGG-ANALYSIS-METHOD
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-AMT-ACTIVATE
  command: CMD-AMT-ACTIVATE
  subject: Analysis lead (register) · second lead or Administrator (activate)
  resource: AGG-ANALYSIS-METHOD
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: approver ≠ author
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-AMT-DEPRECATE
  command: CMD-AMT-DEPRECATE
  subject: Analysis lead (deprecate)
  resource: AGG-ANALYSIS-METHOD
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-AMT-RETIRE
  command: CMD-AMT-RETIRE
  subject: Analysis lead (retire)
  resource: AGG-ANALYSIS-METHOD
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-RUN-SUBMIT
  command: CMD-RUN-SUBMIT
  subject: Analyst (submit, reproduce, cancel)
  resource: AGG-ANALYSIS-RUN
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-RUN-REPRODUCE
  command: CMD-RUN-REPRODUCE
  subject: Analyst (submit, reproduce, cancel)
  resource: AGG-ANALYSIS-RUN
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: reproducer cleared for source run label
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-RUN-CANCEL
  command: CMD-RUN-CANCEL
  subject: Analyst (submit, reproduce, cancel)
  resource: AGG-ANALYSIS-RUN
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-FND-RECORD
  command: CMD-FND-RECORD
  subject: Analyst (record, edit, withdraw) · peer Analyst (accept)
  resource: AGG-FINDING
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-FND-EDIT
  command: CMD-FND-EDIT
  subject: Analyst (record, edit, withdraw) · peer Analyst (accept)
  resource: AGG-FINDING
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-FND-ACCEPT
  command: CMD-FND-ACCEPT
  subject: Analyst (record, edit, withdraw) · peer Analyst (accept)
  resource: AGG-FINDING
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: reviewer ≠ author
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-FND-WITHDRAW
  command: CMD-FND-WITHDRAW
  subject: Analyst (record, edit, withdraw) · peer Analyst (accept)
  resource: AGG-FINDING
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ASM-DRAFT
  command: CMD-ASM-DRAFT
  subject: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)
  resource: AGG-ASSESSMENT
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ASM-EDIT
  command: CMD-ASM-EDIT
  subject: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)
  resource: AGG-ASSESSMENT
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ASM-SUBMIT
  command: CMD-ASM-SUBMIT
  subject: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)
  resource: AGG-ASSESSMENT
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ASM-RETURN
  command: CMD-ASM-RETURN
  subject: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)
  resource: AGG-ASSESSMENT
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ASM-PUBLISH
  command: CMD-ASM-PUBLISH
  subject: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)
  resource: AGG-ASSESSMENT
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: reviewer ≠ author
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ASM-WITHDRAW
  command: CMD-ASM-WITHDRAW
  subject: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)
  resource: AGG-ASSESSMENT
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ASM-DISCARD
  command: CMD-ASM-DISCARD
  subject: Analyst (draft, edit, submit, discard) · reviewer / Analysis lead (return, publish, withdraw)
  resource: AGG-ASSESSMENT
  context_conditions: tenant match; case visible; label rules
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
query_policies:
- id: POL-ACS-GET
  query: QRY-ACS-GET
  subject: case label rule; selections filtered
  otherwise: DENY (not-found shape)
- id: POL-ACS-LIST
  query: QRY-ACS-LIST
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-RUN-GET
  query: QRY-RUN-GET
  subject: run label rule
  otherwise: DENY (not-found shape)
- id: POL-RUN-ARTIFACT
  query: QRY-RUN-ARTIFACT
  subject: run label rule; audited
  otherwise: DENY (not-found shape)
- id: POL-SCN-COMPARE
  query: QRY-SCN-COMPARE
  subject: case label rule
  otherwise: DENY (not-found shape)
- id: POL-FND-LIST
  query: QRY-FND-LIST
  subject: label rule
  otherwise: DENY (not-found shape)
- id: POL-ASM-GET
  query: QRY-ASM-GET
  subject: label rule; REDACT obligation for uncleared citations
  otherwise: DENY (not-found shape)
- id: POL-ASM-VERSIONS
  query: QRY-ASM-VERSIONS
  subject: label rule
  otherwise: DENY (not-found shape)
- id: POL-AMT-LIST
  query: QRY-AMT-LIST
  subject: any analyst
  otherwise: DENY (not-found shape)
```

</details>
