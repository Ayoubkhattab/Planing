---
id: POLICIES-SLC06
type: policy-decision-tables
title: Policy Decision Tables — SLC-06
wave: W6
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Policy Decision Tables — SLC-06

## command_policies

_22 items_

| id | command | subject | resource | context_conditions | decision | otherwise | obligations |
|---|---|---|---|---|---|---|---|
| POL-SIT-CREATE | CMD-SIT-CREATE | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | AGG-SITUATION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SIT-EDIT-DEFINITION | CMD-SIT-EDIT-DEFINITION | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | AGG-SITUATION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SIT-ACTIVATE | CMD-SIT-ACTIVATE | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | AGG-SITUATION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SIT-PAUSE | CMD-SIT-PAUSE | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | AGG-SITUATION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SIT-RESUME | CMD-SIT-RESUME | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | AGG-SITUATION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SIT-CLOSE | CMD-SIT-CLOSE | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | AGG-SITUATION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SIT-RECLASSIFY | CMD-SIT-RECLASSIFY | Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify) | AGG-SITUATION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-ARL-DEFINE | CMD-ARL-DEFINE | Analyst lead / Manager | AGG-ALERT-RULE | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-ARL-EDIT | CMD-ARL-EDIT | Analyst lead / Manager | AGG-ALERT-RULE | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-ARL-ACTIVATE | CMD-ARL-ACTIVATE | Analyst lead / Manager | AGG-ALERT-RULE | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-ARL-DISABLE | CMD-ARL-DISABLE | Analyst lead / Manager | AGG-ALERT-RULE | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-ARL-ENABLE | CMD-ARL-ENABLE | Analyst lead / Manager | AGG-ALERT-RULE | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-ARL-RETIRE | CMD-ARL-RETIRE | Analyst lead / Manager | AGG-ALERT-RULE | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-ALR-ACKNOWLEDGE | CMD-ALR-ACKNOWLEDGE | recipient | AGG-ALERT | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-ALR-RESOLVE | CMD-ALR-RESOLVE | recipient | AGG-ALERT | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-ALR-DISMISS | CMD-ALR-DISMISS | recipient | AGG-ALERT | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SUB-SUBSCRIBE | CMD-SUB-SUBSCRIBE | any user (self) · Administrator (end) | AGG-SUBSCRIPTION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SUB-UPDATE-CHANNELS | CMD-SUB-UPDATE-CHANNELS | any user (self) · Administrator (end) | AGG-SUBSCRIPTION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SUB-PAUSE | CMD-SUB-PAUSE | any user (self) · Administrator (end) | AGG-SUBSCRIPTION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SUB-RESUME | CMD-SUB-RESUME | any user (self) · Administrator (end) | AGG-SUBSCRIPTION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-SUB-UNSUBSCRIBE | CMD-SUB-UNSUBSCRIBE | any user (self) · Administrator (end) | AGG-SUBSCRIPTION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |
| POL-NTF-MARK-READ | CMD-NTF-MARK-READ | recipient | AGG-NOTIFICATION | tenant match; target visible to subject | ALLOW | DENY (not-found shape) | audit |

## query_policies

_8 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-SIT-LIST | QRY-SIT-LIST | any user; situation label rule | DENY (not-found shape) |
| POL-SIT-GET | QRY-SIT-GET | cleared for situation label | DENY (not-found shape) |
| POL-SIT-COP | QRY-SIT-COP | cleared for situation; per-member filtering | DENY (not-found shape) |
| POL-SIT-CHANGES | QRY-SIT-CHANGES | cleared for situation; per-member filtering | DENY (not-found shape) |
| POL-SIT-TILE | QRY-SIT-TILE | cleared for situation; scope-keyed cache (ADR-P06 §6) | DENY (not-found shape) |
| POL-BASE-TILE | QRY-BASE-TILE | any user of tenant | DENY (not-found shape) |
| POL-ALR-LIST | QRY-ALR-LIST | recipient; label rule | DENY (not-found shape) |
| POL-NTF-INBOX | QRY-NTF-INBOX | recipient | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-SIT-CREATE
  command: CMD-SIT-CREATE
  subject: Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)
  resource: AGG-SITUATION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SIT-EDIT-DEFINITION
  command: CMD-SIT-EDIT-DEFINITION
  subject: Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)
  resource: AGG-SITUATION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SIT-ACTIVATE
  command: CMD-SIT-ACTIVATE
  subject: Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)
  resource: AGG-SITUATION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SIT-PAUSE
  command: CMD-SIT-PAUSE
  subject: Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)
  resource: AGG-SITUATION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SIT-RESUME
  command: CMD-SIT-RESUME
  subject: Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)
  resource: AGG-SITUATION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SIT-CLOSE
  command: CMD-SIT-CLOSE
  subject: Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)
  resource: AGG-SITUATION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SIT-RECLASSIFY
  command: CMD-SIT-RECLASSIFY
  subject: Analyst / Manager (create, edit, activate, pause, close) · Security Officer (reclassify)
  resource: AGG-SITUATION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ARL-DEFINE
  command: CMD-ARL-DEFINE
  subject: Analyst lead / Manager
  resource: AGG-ALERT-RULE
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ARL-EDIT
  command: CMD-ARL-EDIT
  subject: Analyst lead / Manager
  resource: AGG-ALERT-RULE
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ARL-ACTIVATE
  command: CMD-ARL-ACTIVATE
  subject: Analyst lead / Manager
  resource: AGG-ALERT-RULE
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ARL-DISABLE
  command: CMD-ARL-DISABLE
  subject: Analyst lead / Manager
  resource: AGG-ALERT-RULE
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ARL-ENABLE
  command: CMD-ARL-ENABLE
  subject: Analyst lead / Manager
  resource: AGG-ALERT-RULE
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ARL-RETIRE
  command: CMD-ARL-RETIRE
  subject: Analyst lead / Manager
  resource: AGG-ALERT-RULE
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ALR-ACKNOWLEDGE
  command: CMD-ALR-ACKNOWLEDGE
  subject: recipient
  resource: AGG-ALERT
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ALR-RESOLVE
  command: CMD-ALR-RESOLVE
  subject: recipient
  resource: AGG-ALERT
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-ALR-DISMISS
  command: CMD-ALR-DISMISS
  subject: recipient
  resource: AGG-ALERT
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SUB-SUBSCRIBE
  command: CMD-SUB-SUBSCRIBE
  subject: any user (self) · Administrator (end)
  resource: AGG-SUBSCRIPTION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SUB-UPDATE-CHANNELS
  command: CMD-SUB-UPDATE-CHANNELS
  subject: any user (self) · Administrator (end)
  resource: AGG-SUBSCRIPTION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SUB-PAUSE
  command: CMD-SUB-PAUSE
  subject: any user (self) · Administrator (end)
  resource: AGG-SUBSCRIPTION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SUB-RESUME
  command: CMD-SUB-RESUME
  subject: any user (self) · Administrator (end)
  resource: AGG-SUBSCRIPTION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-SUB-UNSUBSCRIBE
  command: CMD-SUB-UNSUBSCRIBE
  subject: any user (self) · Administrator (end)
  resource: AGG-SUBSCRIPTION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
- id: POL-NTF-MARK-READ
  command: CMD-NTF-MARK-READ
  subject: recipient
  resource: AGG-NOTIFICATION
  context_conditions: tenant match; target visible to subject
  decision: ALLOW
  otherwise: DENY (not-found shape)
  obligations: audit
query_policies:
- id: POL-SIT-LIST
  query: QRY-SIT-LIST
  subject: any user; situation label rule
  otherwise: DENY (not-found shape)
- id: POL-SIT-GET
  query: QRY-SIT-GET
  subject: cleared for situation label
  otherwise: DENY (not-found shape)
- id: POL-SIT-COP
  query: QRY-SIT-COP
  subject: cleared for situation; per-member filtering
  otherwise: DENY (not-found shape)
- id: POL-SIT-CHANGES
  query: QRY-SIT-CHANGES
  subject: cleared for situation; per-member filtering
  otherwise: DENY (not-found shape)
- id: POL-SIT-TILE
  query: QRY-SIT-TILE
  subject: cleared for situation; scope-keyed cache (ADR-P06 §6)
  otherwise: DENY (not-found shape)
- id: POL-BASE-TILE
  query: QRY-BASE-TILE
  subject: any user of tenant
  otherwise: DENY (not-found shape)
- id: POL-ALR-LIST
  query: QRY-ALR-LIST
  subject: recipient; label rule
  otherwise: DENY (not-found shape)
- id: POL-NTF-INBOX
  query: QRY-NTF-INBOX
  subject: recipient
  otherwise: DENY (not-found shape)
```

</details>
