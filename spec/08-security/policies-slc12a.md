---
id: POLICIES-SLC12A
type: policy-decision-tables
title: Policy Decision Tables — SLC-12a
wave: W6
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Policy Decision Tables — SLC-12a

## command_policies

_15 items_

| id | command | subject | resource | context_conditions | segregation_of_duties | decision | otherwise | obligations |
|---|---|---|---|---|---|---|---|---|
| POL-RTS-DRAFT | CMD-RTS-DRAFT | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | AGG-RETENTION-SCHEDULE | tenant match | — | ALLOW | DENY | audit; mfa |
| POL-RTS-EDIT | CMD-RTS-EDIT | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | AGG-RETENTION-SCHEDULE | tenant match | — | ALLOW | DENY | audit; mfa |
| POL-RTS-ACTIVATE | CMD-RTS-ACTIVATE | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | AGG-RETENTION-SCHEDULE | tenant match | approver ≠ drafter | ALLOW | DENY | audit; mfa |
| POL-RTS-DISCARD | CMD-RTS-DISCARD | Archivist (draft, edit, discard) · Legal/Compliance authority (activate) | AGG-RETENTION-SCHEDULE | tenant match | — | ALLOW | DENY | audit; mfa |
| POL-LHD-PLACE | CMD-LHD-PLACE | Legal/Compliance authority (place, extend, request/approve/cancel release) | AGG-LEGAL-HOLD | tenant match | — | ALLOW | DENY | audit; mfa |
| POL-LHD-EXTEND | CMD-LHD-EXTEND | Legal/Compliance authority (place, extend, request/approve/cancel release) | AGG-LEGAL-HOLD | tenant match | — | ALLOW | DENY | audit; mfa |
| POL-LHD-REQUEST-RELEASE | CMD-LHD-REQUEST-RELEASE | Legal/Compliance authority (place, extend, request/approve/cancel release) | AGG-LEGAL-HOLD | tenant match | — | ALLOW | DENY | audit; mfa |
| POL-LHD-APPROVE-RELEASE | CMD-LHD-APPROVE-RELEASE | Legal/Compliance authority (place, extend, request/approve/cancel release) | AGG-LEGAL-HOLD | tenant match | approver ≠ requester | ALLOW | DENY | audit; mfa |
| POL-LHD-CANCEL-RELEASE | CMD-LHD-CANCEL-RELEASE | Legal/Compliance authority (place, extend, request/approve/cancel release) | AGG-LEGAL-HOLD | tenant match | — | ALLOW | DENY | audit; mfa |
| POL-DSP-SUBMIT | CMD-DSP-SUBMIT | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve) | AGG-DISPOSITION-RUN | tenant match | — | ALLOW | DENY | audit; mfa |
| POL-DSP-APPROVE | CMD-DSP-APPROVE | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve) | AGG-DISPOSITION-RUN | tenant match | approver ≠ submitter | ALLOW | DENY | audit; mfa |
| POL-DSP-CANCEL | CMD-DSP-CANCEL | Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve) | AGG-DISPOSITION-RUN | tenant match | — | ALLOW | DENY | audit; mfa |
| POL-ERS-REGISTER | CMD-ERS-REGISTER | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject) | AGG-ERASURE-REQUEST | tenant match | — | ALLOW | DENY | audit; mfa |
| POL-ERS-APPROVE | CMD-ERS-APPROVE | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject) | AGG-ERASURE-REQUEST | tenant match | approver ≠ registrar | ALLOW | DENY | audit; mfa |
| POL-ERS-REJECT | CMD-ERS-REJECT | Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject) | AGG-ERASURE-REQUEST | tenant match | — | ALLOW | DENY | audit; mfa |

## query_policies

_5 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-RTS-ACTIVE | QRY-RTS-ACTIVE | Archivist, Legal, Auditor | DENY |
| POL-LHD-LIST | QRY-LHD-LIST | Legal, Archivist, Auditor | DENY |
| POL-LHD-CHECK | QRY-LHD-CHECK | owner contexts (workload identity); Archivist | DENY |
| POL-DSP-GET | QRY-DSP-GET | Archivist, Legal, Auditor | DENY |
| POL-ERS-GET | QRY-ERS-GET | Legal, Auditor | DENY |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-RTS-DRAFT
  command: CMD-RTS-DRAFT
  subject: Archivist (draft, edit, discard) · Legal/Compliance authority (activate)
  resource: AGG-RETENTION-SCHEDULE
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-RTS-EDIT
  command: CMD-RTS-EDIT
  subject: Archivist (draft, edit, discard) · Legal/Compliance authority (activate)
  resource: AGG-RETENTION-SCHEDULE
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-RTS-ACTIVATE
  command: CMD-RTS-ACTIVATE
  subject: Archivist (draft, edit, discard) · Legal/Compliance authority (activate)
  resource: AGG-RETENTION-SCHEDULE
  context_conditions: tenant match
  segregation_of_duties: approver ≠ drafter
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-RTS-DISCARD
  command: CMD-RTS-DISCARD
  subject: Archivist (draft, edit, discard) · Legal/Compliance authority (activate)
  resource: AGG-RETENTION-SCHEDULE
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-LHD-PLACE
  command: CMD-LHD-PLACE
  subject: Legal/Compliance authority (place, extend, request/approve/cancel release)
  resource: AGG-LEGAL-HOLD
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-LHD-EXTEND
  command: CMD-LHD-EXTEND
  subject: Legal/Compliance authority (place, extend, request/approve/cancel release)
  resource: AGG-LEGAL-HOLD
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-LHD-REQUEST-RELEASE
  command: CMD-LHD-REQUEST-RELEASE
  subject: Legal/Compliance authority (place, extend, request/approve/cancel release)
  resource: AGG-LEGAL-HOLD
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-LHD-APPROVE-RELEASE
  command: CMD-LHD-APPROVE-RELEASE
  subject: Legal/Compliance authority (place, extend, request/approve/cancel release)
  resource: AGG-LEGAL-HOLD
  context_conditions: tenant match
  segregation_of_duties: approver ≠ requester
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-LHD-CANCEL-RELEASE
  command: CMD-LHD-CANCEL-RELEASE
  subject: Legal/Compliance authority (place, extend, request/approve/cancel release)
  resource: AGG-LEGAL-HOLD
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-DSP-SUBMIT
  command: CMD-DSP-SUBMIT
  subject: Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)
  resource: AGG-DISPOSITION-RUN
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-DSP-APPROVE
  command: CMD-DSP-APPROVE
  subject: Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)
  resource: AGG-DISPOSITION-RUN
  context_conditions: tenant match
  segregation_of_duties: approver ≠ submitter
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-DSP-CANCEL
  command: CMD-DSP-CANCEL
  subject: Archivist (submit, cancel) · Records/Legal authority ≠ submitter (approve)
  resource: AGG-DISPOSITION-RUN
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-ERS-REGISTER
  command: CMD-ERS-REGISTER
  subject: Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject)
  resource: AGG-ERASURE-REQUEST
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-ERS-APPROVE
  command: CMD-ERS-APPROVE
  subject: Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject)
  resource: AGG-ERASURE-REQUEST
  context_conditions: tenant match
  segregation_of_duties: approver ≠ registrar
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-ERS-REJECT
  command: CMD-ERS-REJECT
  subject: Privacy officer / Legal (register) · Legal authority ≠ registrar (approve, reject)
  resource: AGG-ERASURE-REQUEST
  context_conditions: tenant match
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
query_policies:
- id: POL-RTS-ACTIVE
  query: QRY-RTS-ACTIVE
  subject: Archivist, Legal, Auditor
  otherwise: DENY
- id: POL-LHD-LIST
  query: QRY-LHD-LIST
  subject: Legal, Archivist, Auditor
  otherwise: DENY
- id: POL-LHD-CHECK
  query: QRY-LHD-CHECK
  subject: owner contexts (workload identity); Archivist
  otherwise: DENY
- id: POL-DSP-GET
  query: QRY-DSP-GET
  subject: Archivist, Legal, Auditor
  otherwise: DENY
- id: POL-ERS-GET
  query: QRY-ERS-GET
  subject: Legal, Auditor
  otherwise: DENY
```

</details>
