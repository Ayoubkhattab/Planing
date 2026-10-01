---
id: POLICIES-SLC09
type: policy-decision-tables
title: Policy Decision Tables — SLC-09
wave: W6
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Policy Decision Tables — SLC-09

## command_policies

_39 items_

### POL-AST-REGISTER

- **command:** CMD-AST-REGISTER
- **subject:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-UPDATE-CONDITION

- **command:** CMD-AST-UPDATE-CONDITION
- **subject:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-MARK-UNSERVICEABLE

- **command:** CMD-AST-MARK-UNSERVICEABLE
- **subject:** Resource Manager (mark unserviceable)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-START-MAINTENANCE

- **command:** CMD-AST-START-MAINTENANCE
- **subject:** Resource Manager (start maintenance)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-RETURN-TO-SERVICE

- **command:** CMD-AST-RETURN-TO-SERVICE
- **subject:** Resource Manager (return to service)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-FAIL-MAINTENANCE

- **command:** CMD-AST-FAIL-MAINTENANCE
- **subject:** Resource Manager (fail maintenance)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-TRANSFER-CUSTODY

- **command:** CMD-AST-TRANSFER-CUSTODY
- **subject:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-SET-CERTIFICATION

- **command:** CMD-AST-SET-CERTIFICATION
- **subject:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-REPORT-LOST

- **command:** CMD-AST-REPORT-LOST
- **subject:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-RECOVER

- **command:** CMD-AST-RECOVER
- **subject:** Resource Manager (recover)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-DISPOSE

- **command:** CMD-AST-DISPOSE
- **subject:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** asset-disposal authority
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-AST-RECLASSIFY

- **command:** CMD-AST-RECLASSIFY
- **subject:** Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security Officer (reclassify)
- **resource:** AGG-ASSET
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MNT-PLAN

- **command:** CMD-MNT-PLAN
- **subject:** Resource Manager / technician
- **resource:** AGG-MAINTENANCE-ORDER
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MNT-RESCHEDULE

- **command:** CMD-MNT-RESCHEDULE
- **subject:** Resource Manager / technician
- **resource:** AGG-MAINTENANCE-ORDER
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MNT-START

- **command:** CMD-MNT-START
- **subject:** Resource Manager / technician
- **resource:** AGG-MAINTENANCE-ORDER
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MNT-COMPLETE

- **command:** CMD-MNT-COMPLETE
- **subject:** Resource Manager / technician
- **resource:** AGG-MAINTENANCE-ORDER
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-MNT-CANCEL

- **command:** CMD-MNT-CANCEL
- **subject:** Resource Manager / technician
- **resource:** AGG-MAINTENANCE-ORDER
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RSV-HOLD

- **command:** CMD-RSV-HOLD
- **subject:** Planner / Resource Manager
- **resource:** AGG-ASSET-RESERVATION
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RSV-CONFIRM

- **command:** CMD-RSV-CONFIRM
- **subject:** Planner / Resource Manager
- **resource:** AGG-ASSET-RESERVATION
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RSV-RELEASE

- **command:** CMD-RSV-RELEASE
- **subject:** Planner / Resource Manager
- **resource:** AGG-ASSET-RESERVATION
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RSV-CANCEL

- **command:** CMD-RSV-CANCEL
- **subject:** Planner / Resource Manager
- **resource:** AGG-ASSET-RESERVATION
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-ASG-ASSIGN

- **command:** CMD-ASG-ASSIGN
- **subject:** Resource Manager / Planner
- **resource:** AGG-ASSET-ASSIGNMENT
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-ASG-RETURN

- **command:** CMD-ASG-RETURN
- **subject:** Resource Manager / Planner
- **resource:** AGG-ASSET-ASSIGNMENT
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-ASG-CANCEL

- **command:** CMD-ASG-CANCEL
- **subject:** Resource Manager / Planner
- **resource:** AGG-ASSET-ASSIGNMENT
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RPL-CREATE

- **command:** CMD-RPL-CREATE
- **subject:** Resource Manager
- **resource:** AGG-RESOURCE-POOL
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RPL-ADJUST-CAPACITY

- **command:** CMD-RPL-ADJUST-CAPACITY
- **subject:** Resource Manager
- **resource:** AGG-RESOURCE-POOL
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RPL-SUSPEND

- **command:** CMD-RPL-SUSPEND
- **subject:** Resource Manager
- **resource:** AGG-RESOURCE-POOL
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RPL-RESUME

- **command:** CMD-RPL-RESUME
- **subject:** Resource Manager
- **resource:** AGG-RESOURCE-POOL
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RPL-CLOSE

- **command:** CMD-RPL-CLOSE
- **subject:** Resource Manager
- **resource:** AGG-RESOURCE-POOL
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-ALC-REQUEST

- **command:** CMD-ALC-REQUEST
- **subject:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
- **resource:** AGG-ALLOCATION
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-ALC-APPROVE

- **command:** CMD-ALC-APPROVE
- **subject:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
- **resource:** AGG-ALLOCATION
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** approver ≠ requester
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-ALC-REJECT

- **command:** CMD-ALC-REJECT
- **subject:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
- **resource:** AGG-ALLOCATION
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-ALC-RECORD-CONSUMPTION

- **command:** CMD-ALC-RECORD-CONSUMPTION
- **subject:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
- **resource:** AGG-ALLOCATION
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-ALC-PREEMPT

- **command:** CMD-ALC-PREEMPT
- **subject:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
- **resource:** AGG-ALLOCATION
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** decision by pool-scope authority
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-ALC-RELEASE

- **command:** CMD-ALC-RELEASE
- **subject:** Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
- **resource:** AGG-ALLOCATION
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RRQ-DEFINE

- **command:** CMD-RRQ-DEFINE
- **subject:** Training Manager / Administrator
- **resource:** AGG-ROLE-REQUIREMENT
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RRQ-EDIT

- **command:** CMD-RRQ-EDIT
- **subject:** Training Manager / Administrator
- **resource:** AGG-ROLE-REQUIREMENT
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RRQ-ACTIVATE

- **command:** CMD-RRQ-ACTIVATE
- **subject:** Training Manager / Administrator
- **resource:** AGG-ROLE-REQUIREMENT
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** approver ≠ author
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

### POL-RRQ-RETIRE

- **command:** CMD-RRQ-RETIRE
- **subject:** Training Manager / Administrator
- **resource:** AGG-ROLE-REQUIREMENT
- **context_conditions:** tenant match; object visible; owner/pool scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit

## query_policies

_6 items_

| id | query | subject | otherwise |
|---|---|---|---|
| POL-AST-GET | QRY-AST-GET | label rule | DENY (not-found shape) |
| POL-AST-AVAILABILITY | QRY-AST-AVAILABILITY | allowed_scope | DENY (not-found shape) |
| POL-MNT-SCHEDULE | QRY-MNT-SCHEDULE | asset owner scope | DENY (not-found shape) |
| POL-POL-TIMELINE | QRY-POL-TIMELINE | pool scope | DENY (not-found shape) |
| POL-ALC-LIST | QRY-ALC-LIST | scope | DENY (not-found shape) |
| POL-READINESS | QRY-READINESS | Manager / Training Manager in scope; self | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
command_policies:
- id: POL-AST-REGISTER
  command: CMD-AST-REGISTER
  subject: Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security
    Officer (reclassify)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-UPDATE-CONDITION
  command: CMD-AST-UPDATE-CONDITION
  subject: Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security
    Officer (reclassify)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-MARK-UNSERVICEABLE
  command: CMD-AST-MARK-UNSERVICEABLE
  subject: Resource Manager (mark unserviceable)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-START-MAINTENANCE
  command: CMD-AST-START-MAINTENANCE
  subject: Resource Manager (start maintenance)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-RETURN-TO-SERVICE
  command: CMD-AST-RETURN-TO-SERVICE
  subject: Resource Manager (return to service)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-FAIL-MAINTENANCE
  command: CMD-AST-FAIL-MAINTENANCE
  subject: Resource Manager (fail maintenance)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-TRANSFER-CUSTODY
  command: CMD-AST-TRANSFER-CUSTODY
  subject: Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security
    Officer (reclassify)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-SET-CERTIFICATION
  command: CMD-AST-SET-CERTIFICATION
  subject: Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security
    Officer (reclassify)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-REPORT-LOST
  command: CMD-AST-REPORT-LOST
  subject: Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security
    Officer (reclassify)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-RECOVER
  command: CMD-AST-RECOVER
  subject: Resource Manager (recover)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-DISPOSE
  command: CMD-AST-DISPOSE
  subject: Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security
    Officer (reclassify)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: asset-disposal authority
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-AST-RECLASSIFY
  command: CMD-AST-RECLASSIFY
  subject: Resource Manager (register, condition, custody, certification, lost) · disposal authority (dispose) · Security
    Officer (reclassify)
  resource: AGG-ASSET
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MNT-PLAN
  command: CMD-MNT-PLAN
  subject: Resource Manager / technician
  resource: AGG-MAINTENANCE-ORDER
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MNT-RESCHEDULE
  command: CMD-MNT-RESCHEDULE
  subject: Resource Manager / technician
  resource: AGG-MAINTENANCE-ORDER
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MNT-START
  command: CMD-MNT-START
  subject: Resource Manager / technician
  resource: AGG-MAINTENANCE-ORDER
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MNT-COMPLETE
  command: CMD-MNT-COMPLETE
  subject: Resource Manager / technician
  resource: AGG-MAINTENANCE-ORDER
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-MNT-CANCEL
  command: CMD-MNT-CANCEL
  subject: Resource Manager / technician
  resource: AGG-MAINTENANCE-ORDER
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RSV-HOLD
  command: CMD-RSV-HOLD
  subject: Planner / Resource Manager
  resource: AGG-ASSET-RESERVATION
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RSV-CONFIRM
  command: CMD-RSV-CONFIRM
  subject: Planner / Resource Manager
  resource: AGG-ASSET-RESERVATION
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RSV-RELEASE
  command: CMD-RSV-RELEASE
  subject: Planner / Resource Manager
  resource: AGG-ASSET-RESERVATION
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RSV-CANCEL
  command: CMD-RSV-CANCEL
  subject: Planner / Resource Manager
  resource: AGG-ASSET-RESERVATION
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ASG-ASSIGN
  command: CMD-ASG-ASSIGN
  subject: Resource Manager / Planner
  resource: AGG-ASSET-ASSIGNMENT
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ASG-RETURN
  command: CMD-ASG-RETURN
  subject: Resource Manager / Planner
  resource: AGG-ASSET-ASSIGNMENT
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ASG-CANCEL
  command: CMD-ASG-CANCEL
  subject: Resource Manager / Planner
  resource: AGG-ASSET-ASSIGNMENT
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RPL-CREATE
  command: CMD-RPL-CREATE
  subject: Resource Manager
  resource: AGG-RESOURCE-POOL
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RPL-ADJUST-CAPACITY
  command: CMD-RPL-ADJUST-CAPACITY
  subject: Resource Manager
  resource: AGG-RESOURCE-POOL
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RPL-SUSPEND
  command: CMD-RPL-SUSPEND
  subject: Resource Manager
  resource: AGG-RESOURCE-POOL
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RPL-RESUME
  command: CMD-RPL-RESUME
  subject: Resource Manager
  resource: AGG-RESOURCE-POOL
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RPL-CLOSE
  command: CMD-RPL-CLOSE
  subject: Resource Manager
  resource: AGG-RESOURCE-POOL
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ALC-REQUEST
  command: CMD-ALC-REQUEST
  subject: Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
  resource: AGG-ALLOCATION
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ALC-APPROVE
  command: CMD-ALC-APPROVE
  subject: Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
  resource: AGG-ALLOCATION
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: approver ≠ requester
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ALC-REJECT
  command: CMD-ALC-REJECT
  subject: Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
  resource: AGG-ALLOCATION
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ALC-RECORD-CONSUMPTION
  command: CMD-ALC-RECORD-CONSUMPTION
  subject: Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
  resource: AGG-ALLOCATION
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ALC-PREEMPT
  command: CMD-ALC-PREEMPT
  subject: Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
  resource: AGG-ALLOCATION
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: decision by pool-scope authority
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-ALC-RELEASE
  command: CMD-ALC-RELEASE
  subject: Planner (request, release) · allocation authority (approve, reject, pre-empt) · task assignee (consumption)
  resource: AGG-ALLOCATION
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RRQ-DEFINE
  command: CMD-RRQ-DEFINE
  subject: Training Manager / Administrator
  resource: AGG-ROLE-REQUIREMENT
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RRQ-EDIT
  command: CMD-RRQ-EDIT
  subject: Training Manager / Administrator
  resource: AGG-ROLE-REQUIREMENT
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RRQ-ACTIVATE
  command: CMD-RRQ-ACTIVATE
  subject: Training Manager / Administrator
  resource: AGG-ROLE-REQUIREMENT
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: approver ≠ author
  decision: ALLOW
  otherwise: DENY
  obligations: audit
- id: POL-RRQ-RETIRE
  command: CMD-RRQ-RETIRE
  subject: Training Manager / Administrator
  resource: AGG-ROLE-REQUIREMENT
  context_conditions: tenant match; object visible; owner/pool scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
query_policies:
- id: POL-AST-GET
  query: QRY-AST-GET
  subject: label rule
  otherwise: DENY (not-found shape)
- id: POL-AST-AVAILABILITY
  query: QRY-AST-AVAILABILITY
  subject: allowed_scope
  otherwise: DENY (not-found shape)
- id: POL-MNT-SCHEDULE
  query: QRY-MNT-SCHEDULE
  subject: asset owner scope
  otherwise: DENY (not-found shape)
- id: POL-POL-TIMELINE
  query: QRY-POL-TIMELINE
  subject: pool scope
  otherwise: DENY (not-found shape)
- id: POL-ALC-LIST
  query: QRY-ALC-LIST
  subject: scope
  otherwise: DENY (not-found shape)
- id: POL-READINESS
  query: QRY-READINESS
  subject: Manager / Training Manager in scope; self
  otherwise: DENY (not-found shape)
```

</details>
