---
id: POLICIES-SLC01
type: policy-decision-tables
title: Policy Decision Tables — SLC-01
wave: W6
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: 'الجدول يُولَّد من كتالوج الأوامر: لكل أمر سياسة واحدة (SL-02). السياسات الأساسية للمنصة PB-* تُطبق قبلها ولا يتجاوزها
  المستأجر (INV-POL-02).'
---

# Policy Decision Tables — SLC-01

> الجدول يُولَّد من كتالوج الأوامر: لكل أمر سياسة واحدة (SL-02). السياسات الأساسية للمنصة PB-* تُطبق قبلها ولا يتجاوزها المستأجر (INV-POL-02).

## platform_baseline

_7 items_

| id | rule | overridable |
|---|---|---|
| PB-01 | tenant(subject) = tenant(resource) else DENY (not-found shape) | no |
| PB-02 | classification rule (classification-scheme §2) | no |
| PB-03 | PDP unavailable → DENY | no |
| PB-04 | every state-changing command and above-threshold read → audit obligation | no |
| PB-05 | subject cannot act on own clearance, role assignments or authority approvals | no |
| PB-06 | segregation of duties for plan/task approval (REQ-OPS-005/009) | tenant may disable with documented policy |
| PB-07 | MFA required for security administration commands | no |

## command_policies

_71 items_

### POL-TEN-PROVISION

- **command:** CMD-TEN-PROVISION
- **subject:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** yes

### POL-TEN-COMPLETE-PROVISIONING

- **command:** CMD-TEN-COMPLETE-PROVISIONING
- **subject:** workload identity: scheduler / provisioning saga
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** yes

### POL-TEN-FAIL-PROVISIONING

- **command:** CMD-TEN-FAIL-PROVISIONING
- **subject:** workload identity: scheduler / provisioning saga
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** yes

### POL-TEN-RETRY-PROVISIONING

- **command:** CMD-TEN-RETRY-PROVISIONING
- **subject:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** yes

### POL-TEN-SUSPEND

- **command:** CMD-TEN-SUSPEND
- **subject:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** yes

### POL-TEN-REACTIVATE

- **command:** CMD-TEN-REACTIVATE
- **subject:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** yes

### POL-TEN-START-CELL-MIGRATION

- **command:** CMD-TEN-START-CELL-MIGRATION
- **subject:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** yes

### POL-TEN-COMPLETE-CELL-MIGRATION

- **command:** CMD-TEN-COMPLETE-CELL-MIGRATION
- **subject:** workload identity: scheduler / provisioning saga
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** yes

### POL-TEN-START-DECOMMISSION

- **command:** CMD-TEN-START-DECOMMISSION
- **subject:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** two distinct platform operators
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa
- **platform_baseline:** yes

### POL-TEN-COMPLETE-DECOMMISSION

- **command:** CMD-TEN-COMPLETE-DECOMMISSION
- **subject:** workload identity: scheduler / provisioning saga
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** yes

### POL-TEN-UPDATE-QUOTAS

- **command:** CMD-TEN-UPDATE-QUOTAS
- **subject:** Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
- **resource:** AGG-TENANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** yes

### POL-ORG-CREATE

- **command:** CMD-ORG-CREATE
- **subject:** Administrator with org scope ⊇ target
- **resource:** AGG-ORGANIZATION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ORG-RENAME

- **command:** CMD-ORG-RENAME
- **subject:** Administrator with org scope ⊇ target
- **resource:** AGG-ORGANIZATION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ORG-ADD-UNIT

- **command:** CMD-ORG-ADD-UNIT
- **subject:** Administrator with org scope ⊇ target
- **resource:** AGG-ORGANIZATION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ORG-RENAME-UNIT

- **command:** CMD-ORG-RENAME-UNIT
- **subject:** Administrator with org scope ⊇ target
- **resource:** AGG-ORGANIZATION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ORG-MOVE-UNIT

- **command:** CMD-ORG-MOVE-UNIT
- **subject:** Administrator with org scope ⊇ target
- **resource:** AGG-ORGANIZATION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ORG-DEACTIVATE-UNIT

- **command:** CMD-ORG-DEACTIVATE-UNIT
- **subject:** Administrator with org scope ⊇ target
- **resource:** AGG-ORGANIZATION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ORG-DEACTIVATE

- **command:** CMD-ORG-DEACTIVATE
- **subject:** Administrator with org scope ⊇ target
- **resource:** AGG-ORGANIZATION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ORG-REACTIVATE

- **command:** CMD-ORG-REACTIVATE
- **subject:** Administrator with org scope ⊇ target
- **resource:** AGG-ORGANIZATION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-PER-REGISTER

- **command:** CMD-PER-REGISTER
- **subject:** Administrator with org scope ⊇ person's unit
- **resource:** AGG-PERSON
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-PER-UPDATE-DETAILS

- **command:** CMD-PER-UPDATE-DETAILS
- **subject:** Administrator with org scope ⊇ person's unit
- **resource:** AGG-PERSON
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-PER-DEACTIVATE

- **command:** CMD-PER-DEACTIVATE
- **subject:** Administrator with org scope ⊇ person's unit
- **resource:** AGG-PERSON
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-PER-REACTIVATE

- **command:** CMD-PER-REACTIVATE
- **subject:** Administrator with org scope ⊇ person's unit
- **resource:** AGG-PERSON
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-PER-ERASE

- **command:** CMD-PER-ERASE
- **subject:** Administrator with org scope ⊇ person's unit
- **resource:** AGG-PERSON
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa; legal-hold check
- **platform_baseline:** no

### POL-USR-PROVISION

- **command:** CMD-USR-PROVISION
- **subject:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)
- **resource:** AGG-USER
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-USR-LINK-IDENTITY

- **command:** CMD-USR-LINK-IDENTITY
- **subject:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)
- **resource:** AGG-USER
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-USR-UNLINK-IDENTITY

- **command:** CMD-USR-UNLINK-IDENTITY
- **subject:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)
- **resource:** AGG-USER
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-USR-LINK-PERSON

- **command:** CMD-USR-LINK-PERSON
- **subject:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)
- **resource:** AGG-USER
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-USR-RECORD-FIRST-SIGN-IN

- **command:** CMD-USR-RECORD-FIRST-SIGN-IN
- **subject:** workload identity: scheduler / provisioning saga
- **resource:** AGG-USER
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-USR-LOCK

- **command:** CMD-USR-LOCK
- **subject:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)
- **resource:** AGG-USER
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-USR-UNLOCK

- **command:** CMD-USR-UNLOCK
- **subject:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)
- **resource:** AGG-USER
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-USR-DISABLE

- **command:** CMD-USR-DISABLE
- **subject:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)
- **resource:** AGG-USER
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-USR-ENABLE

- **command:** CMD-USR-ENABLE
- **subject:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)
- **resource:** AGG-USER
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-USR-CLOSE

- **command:** CMD-USR-CLOSE
- **subject:** Administrator with scope ⊇ user's units \| SCIM service account (provision/disable/enable) \| Security Officer (lock/unlock)
- **resource:** AGG-USER
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-SVC-CREATE

- **command:** CMD-SVC-CREATE
- **subject:** Administrator
- **resource:** AGG-SERVICE-ACCOUNT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-SVC-ROTATE-CREDENTIAL

- **command:** CMD-SVC-ROTATE-CREDENTIAL
- **subject:** Administrator
- **resource:** AGG-SERVICE-ACCOUNT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-SVC-DISABLE

- **command:** CMD-SVC-DISABLE
- **subject:** Administrator
- **resource:** AGG-SERVICE-ACCOUNT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-SVC-ENABLE

- **command:** CMD-SVC-ENABLE
- **subject:** Administrator
- **resource:** AGG-SERVICE-ACCOUNT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-SVC-CLOSE

- **command:** CMD-SVC-CLOSE
- **subject:** Administrator
- **resource:** AGG-SERVICE-ACCOUNT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ROL-DEFINE

- **command:** CMD-ROL-DEFINE
- **subject:** Administrator (tenant-wide)
- **resource:** AGG-ROLE
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ROL-SET-PERMISSIONS

- **command:** CMD-ROL-SET-PERMISSIONS
- **subject:** Administrator (tenant-wide)
- **resource:** AGG-ROLE
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ROL-ACTIVATE

- **command:** CMD-ROL-ACTIVATE
- **subject:** Administrator (tenant-wide)
- **resource:** AGG-ROLE
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-ROL-RETIRE

- **command:** CMD-ROL-RETIRE
- **subject:** Administrator (tenant-wide)
- **resource:** AGG-ROLE
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-RAS-ASSIGN

- **command:** CMD-RAS-ASSIGN
- **subject:** Administrator with scope ⊇ assignment scope
- **resource:** AGG-ROLE-ASSIGNMENT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** assigner ≠ user; SoD role pairs
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-RAS-REVOKE

- **command:** CMD-RAS-REVOKE
- **subject:** Administrator with scope ⊇ assignment scope
- **resource:** AGG-ROLE-ASSIGNMENT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-AUT-GRANT

- **command:** CMD-AUT-GRANT
- **subject:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)
- **resource:** AGG-AUTHORITY-GRANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-AUT-APPROVE-GRANT

- **command:** CMD-AUT-APPROVE-GRANT
- **subject:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)
- **resource:** AGG-AUTHORITY-GRANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** approver ≠ requester
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa
- **platform_baseline:** no

### POL-AUT-REJECT-GRANT

- **command:** CMD-AUT-REJECT-GRANT
- **subject:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)
- **resource:** AGG-AUTHORITY-GRANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-AUT-DELEGATE

- **command:** CMD-AUT-DELEGATE
- **subject:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)
- **resource:** AGG-AUTHORITY-GRANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** delegate ≠ delegator
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-AUT-SUSPEND

- **command:** CMD-AUT-SUSPEND
- **subject:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)
- **resource:** AGG-AUTHORITY-GRANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-AUT-RESUME

- **command:** CMD-AUT-RESUME
- **subject:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)
- **resource:** AGG-AUTHORITY-GRANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-AUT-REVOKE

- **command:** CMD-AUT-REVOKE
- **subject:** holder of permission authority.grant in scope \| Executive in scope (approve) \| holder of parent grant (delegate)
- **resource:** AGG-AUTHORITY-GRANT
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-CLR-GRANT

- **command:** CMD-CLR-GRANT
- **subject:** Security Officer
- **resource:** AGG-CLEARANCE
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** requester ≠ subject
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa
- **platform_baseline:** no

### POL-CLR-APPROVE

- **command:** CMD-CLR-APPROVE
- **subject:** Security Officer
- **resource:** AGG-CLEARANCE
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** approver ≠ requester ≠ subject (top rank)
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa
- **platform_baseline:** no

### POL-CLR-MODIFY

- **command:** CMD-CLR-MODIFY
- **subject:** Security Officer
- **resource:** AGG-CLEARANCE
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-CLR-SUSPEND

- **command:** CMD-CLR-SUSPEND
- **subject:** Security Officer
- **resource:** AGG-CLEARANCE
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-CLR-REINSTATE

- **command:** CMD-CLR-REINSTATE
- **subject:** Security Officer
- **resource:** AGG-CLEARANCE
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-CLR-REVOKE

- **command:** CMD-CLR-REVOKE
- **subject:** Security Officer
- **resource:** AGG-CLEARANCE
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-CLS-DRAFT

- **command:** CMD-CLS-DRAFT
- **subject:** Security Officer
- **resource:** AGG-CLASSIFICATION-SCHEME
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-CLS-EDIT

- **command:** CMD-CLS-EDIT
- **subject:** Security Officer
- **resource:** AGG-CLASSIFICATION-SCHEME
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-CLS-ACTIVATE

- **command:** CMD-CLS-ACTIVATE
- **subject:** Security Officer
- **resource:** AGG-CLASSIFICATION-SCHEME
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** approver ≠ drafter
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa
- **platform_baseline:** no

### POL-CLS-DISCARD

- **command:** CMD-CLS-DISCARD
- **subject:** Security Officer
- **resource:** AGG-CLASSIFICATION-SCHEME
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-POL-DRAFT

- **command:** CMD-POL-DRAFT
- **subject:** Security Officer
- **resource:** AGG-POLICY-SET
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-POL-EDIT

- **command:** CMD-POL-EDIT
- **subject:** Security Officer
- **resource:** AGG-POLICY-SET
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-POL-SUBMIT

- **command:** CMD-POL-SUBMIT
- **subject:** Security Officer
- **resource:** AGG-POLICY-SET
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-POL-APPROVE

- **command:** CMD-POL-APPROVE
- **subject:** Security Officer
- **resource:** AGG-POLICY-SET
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** approver ≠ author
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa
- **platform_baseline:** no

### POL-POL-REJECT

- **command:** CMD-POL-REJECT
- **subject:** Security Officer
- **resource:** AGG-POLICY-SET
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-EXC-REQUEST

- **command:** CMD-EXC-REQUEST
- **subject:** authenticated user (request) \| Security Officer (approve/reject/revoke)
- **resource:** AGG-SECURITY-EXCEPTION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-EXC-APPROVE

- **command:** CMD-EXC-APPROVE
- **subject:** authenticated user (request) \| Security Officer (approve/reject/revoke)
- **resource:** AGG-SECURITY-EXCEPTION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** approver ∉ {requester, first approver}
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit; mfa
- **platform_baseline:** no

### POL-EXC-REJECT

- **command:** CMD-EXC-REJECT
- **subject:** authenticated user (request) \| Security Officer (approve/reject/revoke)
- **resource:** AGG-SECURITY-EXCEPTION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

### POL-EXC-REVOKE

- **command:** CMD-EXC-REVOKE
- **subject:** authenticated user (request) \| Security Officer (approve/reject/revoke)
- **resource:** AGG-SECURITY-EXCEPTION
- **context_conditions:** tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY
- **obligations:** audit
- **platform_baseline:** no

## query_policies

_14 items_

| id | query | subject | allowed_scope | otherwise |
|---|---|---|---|---|
| POL-TEN-GET | QRY-TEN-GET | platform operator or tenant Administrator of that tenant | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-ORG-TREE | QRY-ORG-TREE | any user of tenant (view org structure) | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-USR-LIST | QRY-USR-LIST | Administrator in scope | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-USR-GET | QRY-USR-GET | Administrator in scope or self | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-SEC-CONTEXT | QRY-SEC-CONTEXT | self | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-AUT-CHECK | QRY-AUT-CHECK | internal services (workload identity) or self | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-AUT-LIST | QRY-AUT-LIST | Executive or Administrator in scope, or holder | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-CLR-GET | QRY-CLR-GET | Security Officer or self | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-CLS-ACTIVE | QRY-CLS-ACTIVE | any user of tenant | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-POL-GET | QRY-POL-GET | Security Officer, Auditor | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-PDP-DECIDE | QRY-PDP-DECIDE | internal PEPs only (workload identity) | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-AUD-SEARCH | QRY-AUD-SEARCH | Auditor, Security Officer (itself audited) | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-AUD-VERIFY | QRY-AUD-VERIFY | Auditor | org scope of subject roles ∩ classification rule | DENY (not-found shape) |
| POL-EXC-LIST | QRY-EXC-LIST | Security Officer, Auditor | org scope of subject roles ∩ classification rule | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
platform_baseline:
- id: PB-01
  rule: tenant(subject) = tenant(resource) else DENY (not-found shape)
  overridable: false
- id: PB-02
  rule: classification rule (classification-scheme §2)
  overridable: false
- id: PB-03
  rule: PDP unavailable → DENY
  overridable: false
- id: PB-04
  rule: every state-changing command and above-threshold read → audit obligation
  overridable: false
- id: PB-05
  rule: subject cannot act on own clearance, role assignments or authority approvals
  overridable: false
- id: PB-06
  rule: segregation of duties for plan/task approval (REQ-OPS-005/009)
  overridable: tenant may disable with documented policy
- id: PB-07
  rule: MFA required for security administration commands
  overridable: false
command_policies:
- id: POL-TEN-PROVISION
  command: CMD-TEN-PROVISION
  subject: Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: true
- id: POL-TEN-COMPLETE-PROVISIONING
  command: CMD-TEN-COMPLETE-PROVISIONING
  subject: 'workload identity: scheduler / provisioning saga'
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: true
- id: POL-TEN-FAIL-PROVISIONING
  command: CMD-TEN-FAIL-PROVISIONING
  subject: 'workload identity: scheduler / provisioning saga'
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: true
- id: POL-TEN-RETRY-PROVISIONING
  command: CMD-TEN-RETRY-PROVISIONING
  subject: Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: true
- id: POL-TEN-SUSPEND
  command: CMD-TEN-SUSPEND
  subject: Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: true
- id: POL-TEN-REACTIVATE
  command: CMD-TEN-REACTIVATE
  subject: Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: true
- id: POL-TEN-START-CELL-MIGRATION
  command: CMD-TEN-START-CELL-MIGRATION
  subject: Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: true
- id: POL-TEN-COMPLETE-CELL-MIGRATION
  command: CMD-TEN-COMPLETE-CELL-MIGRATION
  subject: 'workload identity: scheduler / provisioning saga'
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: true
- id: POL-TEN-START-DECOMMISSION
  command: CMD-TEN-START-DECOMMISSION
  subject: Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: two distinct platform operators
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
  platform_baseline: true
- id: POL-TEN-COMPLETE-DECOMMISSION
  command: CMD-TEN-COMPLETE-DECOMMISSION
  subject: 'workload identity: scheduler / provisioning saga'
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: true
- id: POL-TEN-UPDATE-QUOTAS
  command: CMD-TEN-UPDATE-QUOTAS
  subject: Platform Operator (platform tenant) ; Tenant Administrator for quotas view only
  resource: AGG-TENANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: true
- id: POL-ORG-CREATE
  command: CMD-ORG-CREATE
  subject: Administrator with org scope ⊇ target
  resource: AGG-ORGANIZATION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ORG-RENAME
  command: CMD-ORG-RENAME
  subject: Administrator with org scope ⊇ target
  resource: AGG-ORGANIZATION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ORG-ADD-UNIT
  command: CMD-ORG-ADD-UNIT
  subject: Administrator with org scope ⊇ target
  resource: AGG-ORGANIZATION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ORG-RENAME-UNIT
  command: CMD-ORG-RENAME-UNIT
  subject: Administrator with org scope ⊇ target
  resource: AGG-ORGANIZATION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ORG-MOVE-UNIT
  command: CMD-ORG-MOVE-UNIT
  subject: Administrator with org scope ⊇ target
  resource: AGG-ORGANIZATION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ORG-DEACTIVATE-UNIT
  command: CMD-ORG-DEACTIVATE-UNIT
  subject: Administrator with org scope ⊇ target
  resource: AGG-ORGANIZATION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ORG-DEACTIVATE
  command: CMD-ORG-DEACTIVATE
  subject: Administrator with org scope ⊇ target
  resource: AGG-ORGANIZATION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ORG-REACTIVATE
  command: CMD-ORG-REACTIVATE
  subject: Administrator with org scope ⊇ target
  resource: AGG-ORGANIZATION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-PER-REGISTER
  command: CMD-PER-REGISTER
  subject: Administrator with org scope ⊇ person's unit
  resource: AGG-PERSON
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-PER-UPDATE-DETAILS
  command: CMD-PER-UPDATE-DETAILS
  subject: Administrator with org scope ⊇ person's unit
  resource: AGG-PERSON
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-PER-DEACTIVATE
  command: CMD-PER-DEACTIVATE
  subject: Administrator with org scope ⊇ person's unit
  resource: AGG-PERSON
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-PER-REACTIVATE
  command: CMD-PER-REACTIVATE
  subject: Administrator with org scope ⊇ person's unit
  resource: AGG-PERSON
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-PER-ERASE
  command: CMD-PER-ERASE
  subject: Administrator with org scope ⊇ person's unit
  resource: AGG-PERSON
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa; legal-hold check
  platform_baseline: false
- id: POL-USR-PROVISION
  command: CMD-USR-PROVISION
  subject: Administrator with scope ⊇ user's units | SCIM service account (provision/disable/enable) | Security Officer (lock/unlock)
  resource: AGG-USER
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-USR-LINK-IDENTITY
  command: CMD-USR-LINK-IDENTITY
  subject: Administrator with scope ⊇ user's units | SCIM service account (provision/disable/enable) | Security Officer (lock/unlock)
  resource: AGG-USER
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-USR-UNLINK-IDENTITY
  command: CMD-USR-UNLINK-IDENTITY
  subject: Administrator with scope ⊇ user's units | SCIM service account (provision/disable/enable) | Security Officer (lock/unlock)
  resource: AGG-USER
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-USR-LINK-PERSON
  command: CMD-USR-LINK-PERSON
  subject: Administrator with scope ⊇ user's units | SCIM service account (provision/disable/enable) | Security Officer (lock/unlock)
  resource: AGG-USER
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-USR-RECORD-FIRST-SIGN-IN
  command: CMD-USR-RECORD-FIRST-SIGN-IN
  subject: 'workload identity: scheduler / provisioning saga'
  resource: AGG-USER
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-USR-LOCK
  command: CMD-USR-LOCK
  subject: Administrator with scope ⊇ user's units | SCIM service account (provision/disable/enable) | Security Officer (lock/unlock)
  resource: AGG-USER
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-USR-UNLOCK
  command: CMD-USR-UNLOCK
  subject: Administrator with scope ⊇ user's units | SCIM service account (provision/disable/enable) | Security Officer (lock/unlock)
  resource: AGG-USER
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-USR-DISABLE
  command: CMD-USR-DISABLE
  subject: Administrator with scope ⊇ user's units | SCIM service account (provision/disable/enable) | Security Officer (lock/unlock)
  resource: AGG-USER
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-USR-ENABLE
  command: CMD-USR-ENABLE
  subject: Administrator with scope ⊇ user's units | SCIM service account (provision/disable/enable) | Security Officer (lock/unlock)
  resource: AGG-USER
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-USR-CLOSE
  command: CMD-USR-CLOSE
  subject: Administrator with scope ⊇ user's units | SCIM service account (provision/disable/enable) | Security Officer (lock/unlock)
  resource: AGG-USER
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-SVC-CREATE
  command: CMD-SVC-CREATE
  subject: Administrator
  resource: AGG-SERVICE-ACCOUNT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-SVC-ROTATE-CREDENTIAL
  command: CMD-SVC-ROTATE-CREDENTIAL
  subject: Administrator
  resource: AGG-SERVICE-ACCOUNT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-SVC-DISABLE
  command: CMD-SVC-DISABLE
  subject: Administrator
  resource: AGG-SERVICE-ACCOUNT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-SVC-ENABLE
  command: CMD-SVC-ENABLE
  subject: Administrator
  resource: AGG-SERVICE-ACCOUNT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-SVC-CLOSE
  command: CMD-SVC-CLOSE
  subject: Administrator
  resource: AGG-SERVICE-ACCOUNT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ROL-DEFINE
  command: CMD-ROL-DEFINE
  subject: Administrator (tenant-wide)
  resource: AGG-ROLE
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ROL-SET-PERMISSIONS
  command: CMD-ROL-SET-PERMISSIONS
  subject: Administrator (tenant-wide)
  resource: AGG-ROLE
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ROL-ACTIVATE
  command: CMD-ROL-ACTIVATE
  subject: Administrator (tenant-wide)
  resource: AGG-ROLE
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-ROL-RETIRE
  command: CMD-ROL-RETIRE
  subject: Administrator (tenant-wide)
  resource: AGG-ROLE
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-RAS-ASSIGN
  command: CMD-RAS-ASSIGN
  subject: Administrator with scope ⊇ assignment scope
  resource: AGG-ROLE-ASSIGNMENT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: assigner ≠ user; SoD role pairs
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-RAS-REVOKE
  command: CMD-RAS-REVOKE
  subject: Administrator with scope ⊇ assignment scope
  resource: AGG-ROLE-ASSIGNMENT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-AUT-GRANT
  command: CMD-AUT-GRANT
  subject: holder of permission authority.grant in scope | Executive in scope (approve) | holder of parent grant (delegate)
  resource: AGG-AUTHORITY-GRANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-AUT-APPROVE-GRANT
  command: CMD-AUT-APPROVE-GRANT
  subject: holder of permission authority.grant in scope | Executive in scope (approve) | holder of parent grant (delegate)
  resource: AGG-AUTHORITY-GRANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: approver ≠ requester
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
  platform_baseline: false
- id: POL-AUT-REJECT-GRANT
  command: CMD-AUT-REJECT-GRANT
  subject: holder of permission authority.grant in scope | Executive in scope (approve) | holder of parent grant (delegate)
  resource: AGG-AUTHORITY-GRANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-AUT-DELEGATE
  command: CMD-AUT-DELEGATE
  subject: holder of permission authority.grant in scope | Executive in scope (approve) | holder of parent grant (delegate)
  resource: AGG-AUTHORITY-GRANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: delegate ≠ delegator
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-AUT-SUSPEND
  command: CMD-AUT-SUSPEND
  subject: holder of permission authority.grant in scope | Executive in scope (approve) | holder of parent grant (delegate)
  resource: AGG-AUTHORITY-GRANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-AUT-RESUME
  command: CMD-AUT-RESUME
  subject: holder of permission authority.grant in scope | Executive in scope (approve) | holder of parent grant (delegate)
  resource: AGG-AUTHORITY-GRANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-AUT-REVOKE
  command: CMD-AUT-REVOKE
  subject: holder of permission authority.grant in scope | Executive in scope (approve) | holder of parent grant (delegate)
  resource: AGG-AUTHORITY-GRANT
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-CLR-GRANT
  command: CMD-CLR-GRANT
  subject: Security Officer
  resource: AGG-CLEARANCE
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: requester ≠ subject
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
  platform_baseline: false
- id: POL-CLR-APPROVE
  command: CMD-CLR-APPROVE
  subject: Security Officer
  resource: AGG-CLEARANCE
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: approver ≠ requester ≠ subject (top rank)
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
  platform_baseline: false
- id: POL-CLR-MODIFY
  command: CMD-CLR-MODIFY
  subject: Security Officer
  resource: AGG-CLEARANCE
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-CLR-SUSPEND
  command: CMD-CLR-SUSPEND
  subject: Security Officer
  resource: AGG-CLEARANCE
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-CLR-REINSTATE
  command: CMD-CLR-REINSTATE
  subject: Security Officer
  resource: AGG-CLEARANCE
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-CLR-REVOKE
  command: CMD-CLR-REVOKE
  subject: Security Officer
  resource: AGG-CLEARANCE
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-CLS-DRAFT
  command: CMD-CLS-DRAFT
  subject: Security Officer
  resource: AGG-CLASSIFICATION-SCHEME
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-CLS-EDIT
  command: CMD-CLS-EDIT
  subject: Security Officer
  resource: AGG-CLASSIFICATION-SCHEME
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-CLS-ACTIVATE
  command: CMD-CLS-ACTIVATE
  subject: Security Officer
  resource: AGG-CLASSIFICATION-SCHEME
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: approver ≠ drafter
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
  platform_baseline: false
- id: POL-CLS-DISCARD
  command: CMD-CLS-DISCARD
  subject: Security Officer
  resource: AGG-CLASSIFICATION-SCHEME
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-POL-DRAFT
  command: CMD-POL-DRAFT
  subject: Security Officer
  resource: AGG-POLICY-SET
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-POL-EDIT
  command: CMD-POL-EDIT
  subject: Security Officer
  resource: AGG-POLICY-SET
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-POL-SUBMIT
  command: CMD-POL-SUBMIT
  subject: Security Officer
  resource: AGG-POLICY-SET
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-POL-APPROVE
  command: CMD-POL-APPROVE
  subject: Security Officer
  resource: AGG-POLICY-SET
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: approver ≠ author
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
  platform_baseline: false
- id: POL-POL-REJECT
  command: CMD-POL-REJECT
  subject: Security Officer
  resource: AGG-POLICY-SET
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-EXC-REQUEST
  command: CMD-EXC-REQUEST
  subject: authenticated user (request) | Security Officer (approve/reject/revoke)
  resource: AGG-SECURITY-EXCEPTION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-EXC-APPROVE
  command: CMD-EXC-APPROVE
  subject: authenticated user (request) | Security Officer (approve/reject/revoke)
  resource: AGG-SECURITY-EXCEPTION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: approver ∉ {requester, first approver}
  decision: ALLOW
  otherwise: DENY
  obligations: audit; mfa
  platform_baseline: false
- id: POL-EXC-REJECT
  command: CMD-EXC-REJECT
  subject: authenticated user (request) | Security Officer (approve/reject/revoke)
  resource: AGG-SECURITY-EXCEPTION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
- id: POL-EXC-REVOKE
  command: CMD-EXC-REVOKE
  subject: authenticated user (request) | Security Officer (approve/reject/revoke)
  resource: AGG-SECURITY-EXCEPTION
  context_conditions: tenant match; subject ACTIVE; tenant ACTIVE (except TEN operations by platform)
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY
  obligations: audit
  platform_baseline: false
query_policies:
- id: POL-TEN-GET
  query: QRY-TEN-GET
  subject: platform operator or tenant Administrator of that tenant
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-ORG-TREE
  query: QRY-ORG-TREE
  subject: any user of tenant (view org structure)
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-USR-LIST
  query: QRY-USR-LIST
  subject: Administrator in scope
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-USR-GET
  query: QRY-USR-GET
  subject: Administrator in scope or self
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-SEC-CONTEXT
  query: QRY-SEC-CONTEXT
  subject: self
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-AUT-CHECK
  query: QRY-AUT-CHECK
  subject: internal services (workload identity) or self
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-AUT-LIST
  query: QRY-AUT-LIST
  subject: Executive or Administrator in scope, or holder
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-CLR-GET
  query: QRY-CLR-GET
  subject: Security Officer or self
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-CLS-ACTIVE
  query: QRY-CLS-ACTIVE
  subject: any user of tenant
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-POL-GET
  query: QRY-POL-GET
  subject: Security Officer, Auditor
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-PDP-DECIDE
  query: QRY-PDP-DECIDE
  subject: internal PEPs only (workload identity)
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-AUD-SEARCH
  query: QRY-AUD-SEARCH
  subject: Auditor, Security Officer (itself audited)
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-AUD-VERIFY
  query: QRY-AUD-VERIFY
  subject: Auditor
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
- id: POL-EXC-LIST
  query: QRY-EXC-LIST
  subject: Security Officer, Auditor
  allowed_scope: org scope of subject roles ∩ classification rule
  otherwise: DENY (not-found shape)
```

</details>
