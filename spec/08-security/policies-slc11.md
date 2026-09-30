---
id: POLICIES-SLC11
type: policy-decision-tables
title: Policy Decision Tables — SLC-11
wave: W6
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Policy Decision Tables — SLC-11

## command_policies

_16 items_

### POL-DEV-ENROLL

- **command:** CMD-DEV-ENROLL
- **subject:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)
- **resource:** AGG-DEVICE
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-DEV-CONFIRM

- **command:** CMD-DEV-CONFIRM
- **subject:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)
- **resource:** AGG-DEVICE
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa

### POL-DEV-ROTATE-KEY

- **command:** CMD-DEV-ROTATE-KEY
- **subject:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)
- **resource:** AGG-DEVICE
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-DEV-SUSPEND

- **command:** CMD-DEV-SUSPEND
- **subject:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)
- **resource:** AGG-DEVICE
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-DEV-REINSTATE

- **command:** CMD-DEV-REINSTATE
- **subject:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)
- **resource:** AGG-DEVICE
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-DEV-REPORT-LOST

- **command:** CMD-DEV-REPORT-LOST
- **subject:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)
- **resource:** AGG-DEVICE
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-DEV-RETIRE

- **command:** CMD-DEV-RETIRE
- **subject:** user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer (lost, retire override)
- **resource:** AGG-DEVICE
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa

### POL-PKG-REQUEST

- **command:** CMD-PKG-REQUEST
- **subject:** field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)
- **resource:** AGG-PRELOAD-PACKAGE
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-PKG-CONFIRM-DOWNLOAD

- **command:** CMD-PKG-CONFIRM-DOWNLOAD
- **subject:** field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)
- **resource:** AGG-PRELOAD-PACKAGE
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-PKG-REVOKE

- **command:** CMD-PKG-REVOKE
- **subject:** field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)
- **resource:** AGG-PRELOAD-PACKAGE
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SYN-OPEN

- **command:** CMD-SYN-OPEN
- **subject:** field device + user (open, upload)
- **resource:** AGG-SYNC-SESSION
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SYN-UPLOAD-BATCH

- **command:** CMD-SYN-UPLOAD-BATCH
- **subject:** field device + user (open, upload)
- **resource:** AGG-SYNC-SESSION
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SCF-ASSIGN

- **command:** CMD-SCF-ASSIGN
- **subject:** reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)
- **resource:** AGG-SYNC-CONFLICT
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SCF-REAPPLY

- **command:** CMD-SCF-REAPPLY
- **subject:** reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)
- **resource:** AGG-SYNC-CONFLICT
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SCF-DISCARD

- **command:** CMD-SCF-DISCARD
- **subject:** reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)
- **resource:** AGG-SYNC-CONFLICT
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-SCF-RESOLVE-MANUALLY

- **command:** CMD-SCF-RESOLVE-MANUALLY
- **subject:** reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)
- **resource:** AGG-SYNC-CONFLICT
- **context_conditions:** tenant match; device ACTIVE where applicable; device signature for SYN
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

## query_policies

_5 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-DEV-LIST | QRY-DEV-LIST | self; Administrator in scope | DENY |
| POL-PKG-GET | QRY-PKG-GET | package owner device + user | DENY |
| POL-SYN-DELTA | QRY-SYN-DELTA | device + user of the session | DENY |
| POL-SCF-LIST | QRY-SCF-LIST | reviewers authorized on targets | DENY |
| POL-SCF-GET | QRY-SCF-GET | reviewer authorized on target | DENY |

## offline_rules

- tenant offline max level (default INTERNAL) caps preload packages (POL-OFFLINE-PRELOAD)
- offline commands executed with the user's delegated SecurityContext at sync time — a user who lost a permission while offline has the command rejected (conflict)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-DEV-ENROLL
  command: CMD-DEV-ENROLL
  subject: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer
    (lost, retire override)
  resource: AGG-DEVICE
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-DEV-CONFIRM
  command: CMD-DEV-CONFIRM
  subject: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer
    (lost, retire override)
  resource: AGG-DEVICE
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-DEV-ROTATE-KEY
  command: CMD-DEV-ROTATE-KEY
  subject: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer
    (lost, retire override)
  resource: AGG-DEVICE
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-DEV-SUSPEND
  command: CMD-DEV-SUSPEND
  subject: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer
    (lost, retire override)
  resource: AGG-DEVICE
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-DEV-REINSTATE
  command: CMD-DEV-REINSTATE
  subject: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer
    (lost, retire override)
  resource: AGG-DEVICE
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-DEV-REPORT-LOST
  command: CMD-DEV-REPORT-LOST
  subject: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer
    (lost, retire override)
  resource: AGG-DEVICE
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-DEV-RETIRE
  command: CMD-DEV-RETIRE
  subject: user (enroll, report lost) · Administrator / MDM policy (confirm, suspend, reinstate, retire) · Security Officer
    (lost, retire override)
  resource: AGG-DEVICE
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
- id: POL-PKG-REQUEST
  command: CMD-PKG-REQUEST
  subject: field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)
  resource: AGG-PRELOAD-PACKAGE
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PKG-CONFIRM-DOWNLOAD
  command: CMD-PKG-CONFIRM-DOWNLOAD
  subject: field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)
  resource: AGG-PRELOAD-PACKAGE
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-PKG-REVOKE
  command: CMD-PKG-REVOKE
  subject: field user (request, confirm download, revoke) · Administrator / Security Officer (revoke)
  resource: AGG-PRELOAD-PACKAGE
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SYN-OPEN
  command: CMD-SYN-OPEN
  subject: field device + user (open, upload)
  resource: AGG-SYNC-SESSION
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SYN-UPLOAD-BATCH
  command: CMD-SYN-UPLOAD-BATCH
  subject: field device + user (open, upload)
  resource: AGG-SYNC-SESSION
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SCF-ASSIGN
  command: CMD-SCF-ASSIGN
  subject: 'reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)'
  resource: AGG-SYNC-CONFLICT
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SCF-REAPPLY
  command: CMD-SCF-REAPPLY
  subject: 'reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)'
  resource: AGG-SYNC-CONFLICT
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SCF-DISCARD
  command: CMD-SCF-DISCARD
  subject: 'reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)'
  resource: AGG-SYNC-CONFLICT
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-SCF-RESOLVE-MANUALLY
  command: CMD-SCF-RESOLVE-MANUALLY
  subject: 'reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve)'
  resource: AGG-SYNC-CONFLICT
  context_conditions: tenant match; device ACTIVE where applicable; device signature for SYN
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-DEV-LIST
  query: QRY-DEV-LIST
  subject: self; Administrator in scope
  otherwise: DENY
- id: POL-PKG-GET
  query: QRY-PKG-GET
  subject: package owner device + user
  otherwise: DENY
- id: POL-SYN-DELTA
  query: QRY-SYN-DELTA
  subject: device + user of the session
  otherwise: DENY
- id: POL-SCF-LIST
  query: QRY-SCF-LIST
  subject: reviewers authorized on targets
  otherwise: DENY
- id: POL-SCF-GET
  query: QRY-SCF-GET
  subject: reviewer authorized on target
  otherwise: DENY
offline_rules:
- tenant offline max level (default INTERNAL) caps preload packages (POL-OFFLINE-PRELOAD)
- offline commands executed with the user's delegated SecurityContext at sync time — a user who lost a permission while offline
  has the command rejected (conflict)
```

</details>
