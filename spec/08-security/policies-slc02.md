---
id: POLICIES-SLC02
type: policy-decision-tables
title: Policy Decision Tables — SLC-02
wave: W6
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: 'PB-01..PB-07 من SLC-01 تنطبق. أُضيف التزام جديد: generalize (LIB-CLAIMS-KERNEL §5).'
---

# Policy Decision Tables — SLC-02

> PB-01..PB-07 من SLC-01 تنطبق. أُضيف التزام جديد: generalize (LIB-CLAIMS-KERNEL §5).

## added_platform_baseline

_4 items_

| id | rule | overridable |
|---|---|---|
| PB-08 | source identity attributes require permission source.identity.view; otherwise REDACT(identity fields) | no |
| PB-09 | write of a claim/observation with label above the writer's clearance is rejected | no |
| PB-10 | tenant may define generalize(min_accuracy_m) for location reads by level/role/purpose | configurable |
| PB-11 | lineage traversal stops at invisible nodes; the cut is shown only if policy allows existence disclosure | configurable |

## command_policies

_57 items_

### POL-SRC-REGISTER

- **command:** CMD-SRC-REGISTER
- **subject:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)
- **resource:** AGG-SOURCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-SRC-RATE-RELIABILITY

- **command:** CMD-SRC-RATE-RELIABILITY
- **subject:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)
- **resource:** AGG-SOURCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-SRC-UPDATE-PROFILE

- **command:** CMD-SRC-UPDATE-PROFILE
- **subject:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)
- **resource:** AGG-SOURCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-SRC-SET-PROTECTION

- **command:** CMD-SRC-SET-PROTECTION
- **subject:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)
- **resource:** AGG-SOURCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** decrease needs second Security Officer
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit; mfa

### POL-SRC-RECLASSIFY

- **command:** CMD-SRC-RECLASSIFY
- **subject:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)
- **resource:** AGG-SOURCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-SRC-SUSPEND

- **command:** CMD-SRC-SUSPEND
- **subject:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)
- **resource:** AGG-SOURCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-SRC-REINSTATE

- **command:** CMD-SRC-REINSTATE
- **subject:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)
- **resource:** AGG-SOURCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-SRC-RETIRE

- **command:** CMD-SRC-RETIRE
- **subject:** Analyst (register, rate, profile) · Security Officer (protection, reclassify)
- **resource:** AGG-SOURCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-OBS-RECORD

- **command:** CMD-OBS-RECORD
- **subject:** Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
- **resource:** AGG-OBSERVATION
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-OBS-AMEND

- **command:** CMD-OBS-AMEND
- **subject:** Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
- **resource:** AGG-OBSERVATION
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-OBS-ATTACH-EVIDENCE

- **command:** CMD-OBS-ATTACH-EVIDENCE
- **subject:** Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
- **resource:** AGG-OBSERVATION
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-OBS-RECLASSIFY

- **command:** CMD-OBS-RECLASSIFY
- **subject:** Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
- **resource:** AGG-OBSERVATION
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-OBS-VALIDATE

- **command:** CMD-OBS-VALIDATE
- **subject:** Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
- **resource:** AGG-OBSERVATION
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** validator ≠ observer (unless system auto-validation policy)
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-OBS-REJECT

- **command:** CMD-OBS-REJECT
- **subject:** Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
- **resource:** AGG-OBSERVATION
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ENT-REGISTER

- **command:** CMD-ENT-REGISTER
- **subject:** Analyst · adapter service account
- **resource:** AGG-ENTITY
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ENT-CHANGE-TYPE

- **command:** CMD-ENT-CHANGE-TYPE
- **subject:** Analyst · adapter service account
- **resource:** AGG-ENTITY
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ENT-RECLASSIFY

- **command:** CMD-ENT-RECLASSIFY
- **subject:** Analyst · adapter service account
- **resource:** AGG-ENTITY
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ENT-RETIRE

- **command:** CMD-ENT-RETIRE
- **subject:** Analyst · adapter service account
- **resource:** AGG-ENTITY
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ENT-REINSTATE

- **command:** CMD-ENT-REINSTATE
- **subject:** Analyst · adapter service account
- **resource:** AGG-ENTITY
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-RWE-REGISTER

- **command:** CMD-RWE-REGISTER
- **subject:** Analyst · adapter service account
- **resource:** AGG-REALWORLD-EVENT
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-RWE-CHANGE-TYPE

- **command:** CMD-RWE-CHANGE-TYPE
- **subject:** Analyst · adapter service account
- **resource:** AGG-REALWORLD-EVENT
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-RWE-RECLASSIFY

- **command:** CMD-RWE-RECLASSIFY
- **subject:** Analyst · adapter service account
- **resource:** AGG-REALWORLD-EVENT
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-RWE-RETIRE

- **command:** CMD-RWE-RETIRE
- **subject:** Analyst · adapter service account
- **resource:** AGG-REALWORLD-EVENT
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-RWE-REINSTATE

- **command:** CMD-RWE-REINSTATE
- **subject:** Analyst · adapter service account
- **resource:** AGG-REALWORLD-EVENT
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-REL-REGISTER

- **command:** CMD-REL-REGISTER
- **subject:** Analyst · adapter service account
- **resource:** AGG-RELATIONSHIP
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-REL-RECLASSIFY

- **command:** CMD-REL-RECLASSIFY
- **subject:** Analyst · adapter service account
- **resource:** AGG-RELATIONSHIP
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-REL-RETIRE

- **command:** CMD-REL-RETIRE
- **subject:** Analyst · adapter service account
- **resource:** AGG-RELATIONSHIP
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-REL-REINSTATE

- **command:** CMD-REL-REINSTATE
- **subject:** Analyst · adapter service account
- **resource:** AGG-RELATIONSHIP
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-CLM-ASSERT

- **command:** CMD-CLM-ASSERT
- **subject:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)
- **resource:** AGG-CLAIM
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-CLM-CORRECT

- **command:** CMD-CLM-CORRECT
- **subject:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)
- **resource:** AGG-CLAIM
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-CLM-RECORD-CHANGE

- **command:** CMD-CLM-RECORD-CHANGE
- **subject:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)
- **resource:** AGG-CLAIM
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-CLM-RETRACT

- **command:** CMD-CLM-RETRACT
- **subject:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)
- **resource:** AGG-CLAIM
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-CLM-ASSESS

- **command:** CMD-CLM-ASSESS
- **subject:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)
- **resource:** AGG-CLAIM
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-CLM-RECLASSIFY

- **command:** CMD-CLM-RECLASSIFY
- **subject:** Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system identity (assess) · Analyst (correct, change, retract)
- **resource:** AGG-CLAIM
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-EVD-REGISTER

- **command:** CMD-EVD-REGISTER
- **subject:** Analyst · Field User (register) · custodian role (custody)
- **resource:** AGG-EVIDENCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-EVD-UPDATE-LOCATOR

- **command:** CMD-EVD-UPDATE-LOCATOR
- **subject:** Analyst · Field User (register) · custodian role (custody)
- **resource:** AGG-EVIDENCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-EVD-SEAL

- **command:** CMD-EVD-SEAL
- **subject:** Analyst · Field User (register) · custodian role (custody)
- **resource:** AGG-EVIDENCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-EVD-TRANSFER-CUSTODY

- **command:** CMD-EVD-TRANSFER-CUSTODY
- **subject:** Analyst · Field User (register) · custodian role (custody)
- **resource:** AGG-EVIDENCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-EVD-RECLASSIFY

- **command:** CMD-EVD-RECLASSIFY
- **subject:** Analyst · Field User (register) · custodian role (custody)
- **resource:** AGG-EVIDENCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-EVD-WITHDRAW

- **command:** CMD-EVD-WITHDRAW
- **subject:** Analyst · Field User (register) · custodian role (custody)
- **resource:** AGG-EVIDENCE
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit; notify owners of dependent claims

### POL-EVL-LINK

- **command:** CMD-EVL-LINK
- **subject:** Analyst
- **resource:** AGG-EVIDENCE-LINK
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-EVL-UNLINK

- **command:** CMD-EVL-UNLINK
- **subject:** Analyst
- **resource:** AGG-EVIDENCE-LINK
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ATT-INITIATE-UPLOAD

- **command:** CMD-ATT-INITIATE-UPLOAD
- **subject:** user with write permission on the target object
- **resource:** AGG-ATTACHMENT
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ATT-COMPLETE-UPLOAD

- **command:** CMD-ATT-COMPLETE-UPLOAD
- **subject:** user with write permission on the target object
- **resource:** AGG-ATTACHMENT
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ATT-ERASE

- **command:** CMD-ATT-ERASE
- **subject:** user with write permission on the target object
- **resource:** AGG-ATTACHMENT
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit; mfa; legal-hold check

### POL-IMP-SUBMIT

- **command:** CMD-IMP-SUBMIT
- **subject:** adapter service account · Administrator
- **resource:** AGG-IMPORT-BATCH
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-IMP-REPROCESS-QUARANTINE

- **command:** CMD-IMP-REPROCESS-QUARANTINE
- **subject:** adapter service account · Administrator
- **resource:** AGG-IMPORT-BATCH
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-IMP-ACCEPT-QUARANTINE

- **command:** CMD-IMP-ACCEPT-QUARANTINE
- **subject:** adapter service account · Administrator
- **resource:** AGG-IMPORT-BATCH
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-IMP-CANCEL

- **command:** CMD-IMP-CANCEL
- **subject:** adapter service account · Administrator
- **resource:** AGG-IMPORT-BATCH
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-EXT-MAP

- **command:** CMD-EXT-MAP
- **subject:** adapter service account · Analyst
- **resource:** AGG-EXTERNAL-ID
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-EXT-END

- **command:** CMD-EXT-END
- **subject:** adapter service account · Analyst
- **resource:** AGG-EXTERNAL-ID
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ADP-REGISTER

- **command:** CMD-ADP-REGISTER
- **subject:** Administrator (register, update) · second Administrator (activate)
- **resource:** AGG-ADAPTER
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ADP-UPDATE-MAPPING

- **command:** CMD-ADP-UPDATE-MAPPING
- **subject:** Administrator (register, update) · second Administrator (activate)
- **resource:** AGG-ADAPTER
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ADP-ACTIVATE

- **command:** CMD-ADP-ACTIVATE
- **subject:** Administrator (register, update) · second Administrator (activate)
- **resource:** AGG-ADAPTER
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** approver ≠ author
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ADP-SUSPEND

- **command:** CMD-ADP-SUSPEND
- **subject:** Administrator (register, update) · second Administrator (activate)
- **resource:** AGG-ADAPTER
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ADP-RESUME

- **command:** CMD-ADP-RESUME
- **subject:** Administrator (register, update) · second Administrator (activate)
- **resource:** AGG-ADAPTER
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

### POL-ADP-RETIRE

- **command:** CMD-ADP-RETIRE
- **subject:** Administrator (register, update) · second Administrator (activate)
- **resource:** AGG-ADAPTER
- **context_conditions:** tenant match; object visible to subject (label ≤ clearance); write permission in org scope
- **segregation_of_duties:** —
- **decision:** ALLOW
- **otherwise:** DENY (not-found shape if object invisible)
- **obligations:** audit

## query_policies

_16 items_

| id | query | subject | allowed_scope | otherwise |
|---|---|---|---|---|
| POL-ENT-RESOLVED | QRY-ENT-RESOLVED | any user; claims label-filtered (INV-ENT-02) | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-ENT-CLAIMS | QRY-ENT-CLAIMS | any user; label-filtered | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-ENT-LIST | QRY-ENT-LIST | any user; allowed_scope pre-filter | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-ENT-POSITIONS | QRY-ENT-POSITIONS | any user; label-filtered; geometry generalized by obligation | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-RWE-GET | QRY-RWE-GET | any user; label-filtered | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-REL-LIST | QRY-REL-LIST | any user; hidden relationships and endpoints omitted | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-CLM-GET | QRY-CLM-GET | any user; label-filtered | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-OBS-LIST | QRY-OBS-LIST | any user; allowed_scope pre-filter | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-OBS-GET | QRY-OBS-GET | any user; label-filtered | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-SRC-GET | QRY-SRC-GET | Analyst and above; protection policy | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-EVD-GET | QRY-EVD-GET | any user; label-filtered | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-ATT-DOWNLOAD | QRY-ATT-DOWNLOAD | authorized on the owning evidence/observation | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-LIN-TRACE | QRY-LIN-TRACE | any user; per-node authorization | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-EXT-RESOLVE | QRY-EXT-RESOLVE | adapter service accounts; Analyst | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-IMP-GET | QRY-IMP-GET | adapter owner; Administrator | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |
| POL-ADP-GET | QRY-ADP-GET | Administrator | org scope ∩ classification rule; claims filtered by label | DENY (not-found shape) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
added_platform_baseline:
- id: PB-08
  rule: source identity attributes require permission source.identity.view; otherwise REDACT(identity fields)
  overridable: false
- id: PB-09
  rule: write of a claim/observation with label above the writer's clearance is rejected
  overridable: false
- id: PB-10
  rule: tenant may define generalize(min_accuracy_m) for location reads by level/role/purpose
  overridable: configurable
- id: PB-11
  rule: lineage traversal stops at invisible nodes; the cut is shown only if policy allows existence disclosure
  overridable: configurable
command_policies:
- id: POL-SRC-REGISTER
  command: CMD-SRC-REGISTER
  subject: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  resource: AGG-SOURCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-SRC-RATE-RELIABILITY
  command: CMD-SRC-RATE-RELIABILITY
  subject: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  resource: AGG-SOURCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-SRC-UPDATE-PROFILE
  command: CMD-SRC-UPDATE-PROFILE
  subject: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  resource: AGG-SOURCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-SRC-SET-PROTECTION
  command: CMD-SRC-SET-PROTECTION
  subject: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  resource: AGG-SOURCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: decrease needs second Security Officer
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit; mfa
- id: POL-SRC-RECLASSIFY
  command: CMD-SRC-RECLASSIFY
  subject: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  resource: AGG-SOURCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-SRC-SUSPEND
  command: CMD-SRC-SUSPEND
  subject: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  resource: AGG-SOURCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-SRC-REINSTATE
  command: CMD-SRC-REINSTATE
  subject: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  resource: AGG-SOURCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-SRC-RETIRE
  command: CMD-SRC-RETIRE
  subject: Analyst (register, rate, profile) · Security Officer (protection, reclassify)
  resource: AGG-SOURCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-OBS-RECORD
  command: CMD-OBS-RECORD
  subject: Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
  resource: AGG-OBSERVATION
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-OBS-AMEND
  command: CMD-OBS-AMEND
  subject: Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
  resource: AGG-OBSERVATION
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-OBS-ATTACH-EVIDENCE
  command: CMD-OBS-ATTACH-EVIDENCE
  subject: Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
  resource: AGG-OBSERVATION
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-OBS-RECLASSIFY
  command: CMD-OBS-RECLASSIFY
  subject: Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
  resource: AGG-OBSERVATION
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-OBS-VALIDATE
  command: CMD-OBS-VALIDATE
  subject: Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
  resource: AGG-OBSERVATION
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: validator ≠ observer (unless system auto-validation policy)
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-OBS-REJECT
  command: CMD-OBS-REJECT
  subject: Field User / Operator / Analyst / adapter service account (record) · Analyst (validate, reject)
  resource: AGG-OBSERVATION
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ENT-REGISTER
  command: CMD-ENT-REGISTER
  subject: Analyst · adapter service account
  resource: AGG-ENTITY
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ENT-CHANGE-TYPE
  command: CMD-ENT-CHANGE-TYPE
  subject: Analyst · adapter service account
  resource: AGG-ENTITY
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ENT-RECLASSIFY
  command: CMD-ENT-RECLASSIFY
  subject: Analyst · adapter service account
  resource: AGG-ENTITY
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ENT-RETIRE
  command: CMD-ENT-RETIRE
  subject: Analyst · adapter service account
  resource: AGG-ENTITY
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ENT-REINSTATE
  command: CMD-ENT-REINSTATE
  subject: Analyst · adapter service account
  resource: AGG-ENTITY
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-RWE-REGISTER
  command: CMD-RWE-REGISTER
  subject: Analyst · adapter service account
  resource: AGG-REALWORLD-EVENT
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-RWE-CHANGE-TYPE
  command: CMD-RWE-CHANGE-TYPE
  subject: Analyst · adapter service account
  resource: AGG-REALWORLD-EVENT
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-RWE-RECLASSIFY
  command: CMD-RWE-RECLASSIFY
  subject: Analyst · adapter service account
  resource: AGG-REALWORLD-EVENT
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-RWE-RETIRE
  command: CMD-RWE-RETIRE
  subject: Analyst · adapter service account
  resource: AGG-REALWORLD-EVENT
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-RWE-REINSTATE
  command: CMD-RWE-REINSTATE
  subject: Analyst · adapter service account
  resource: AGG-REALWORLD-EVENT
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-REL-REGISTER
  command: CMD-REL-REGISTER
  subject: Analyst · adapter service account
  resource: AGG-RELATIONSHIP
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-REL-RECLASSIFY
  command: CMD-REL-RECLASSIFY
  subject: Analyst · adapter service account
  resource: AGG-RELATIONSHIP
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-REL-RETIRE
  command: CMD-REL-RETIRE
  subject: Analyst · adapter service account
  resource: AGG-RELATIONSHIP
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-REL-REINSTATE
  command: CMD-REL-REINSTATE
  subject: Analyst · adapter service account
  resource: AGG-RELATIONSHIP
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-CLM-ASSERT
  command: CMD-CLM-ASSERT
  subject: Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system
    identity (assess) · Analyst (correct, change, retract)
  resource: AGG-CLAIM
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-CLM-CORRECT
  command: CMD-CLM-CORRECT
  subject: Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system
    identity (assess) · Analyst (correct, change, retract)
  resource: AGG-CLAIM
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-CLM-RECORD-CHANGE
  command: CMD-CLM-RECORD-CHANGE
  subject: Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system
    identity (assess) · Analyst (correct, change, retract)
  resource: AGG-CLAIM
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-CLM-RETRACT
  command: CMD-CLM-RETRACT
  subject: Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system
    identity (assess) · Analyst (correct, change, retract)
  resource: AGG-CLAIM
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-CLM-ASSESS
  command: CMD-CLM-ASSESS
  subject: Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system
    identity (assess) · Analyst (correct, change, retract)
  resource: AGG-CLAIM
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-CLM-RECLASSIFY
  command: CMD-CLM-RECLASSIFY
  subject: Analyst · adapter service account · analysis-run identity (assert) · Analyst or verification re-evaluator system
    identity (assess) · Analyst (correct, change, retract)
  resource: AGG-CLAIM
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-EVD-REGISTER
  command: CMD-EVD-REGISTER
  subject: Analyst · Field User (register) · custodian role (custody)
  resource: AGG-EVIDENCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-EVD-UPDATE-LOCATOR
  command: CMD-EVD-UPDATE-LOCATOR
  subject: Analyst · Field User (register) · custodian role (custody)
  resource: AGG-EVIDENCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-EVD-SEAL
  command: CMD-EVD-SEAL
  subject: Analyst · Field User (register) · custodian role (custody)
  resource: AGG-EVIDENCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-EVD-TRANSFER-CUSTODY
  command: CMD-EVD-TRANSFER-CUSTODY
  subject: Analyst · Field User (register) · custodian role (custody)
  resource: AGG-EVIDENCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-EVD-RECLASSIFY
  command: CMD-EVD-RECLASSIFY
  subject: Analyst · Field User (register) · custodian role (custody)
  resource: AGG-EVIDENCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-EVD-WITHDRAW
  command: CMD-EVD-WITHDRAW
  subject: Analyst · Field User (register) · custodian role (custody)
  resource: AGG-EVIDENCE
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit; notify owners of dependent claims
- id: POL-EVL-LINK
  command: CMD-EVL-LINK
  subject: Analyst
  resource: AGG-EVIDENCE-LINK
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-EVL-UNLINK
  command: CMD-EVL-UNLINK
  subject: Analyst
  resource: AGG-EVIDENCE-LINK
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ATT-INITIATE-UPLOAD
  command: CMD-ATT-INITIATE-UPLOAD
  subject: user with write permission on the target object
  resource: AGG-ATTACHMENT
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ATT-COMPLETE-UPLOAD
  command: CMD-ATT-COMPLETE-UPLOAD
  subject: user with write permission on the target object
  resource: AGG-ATTACHMENT
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ATT-ERASE
  command: CMD-ATT-ERASE
  subject: user with write permission on the target object
  resource: AGG-ATTACHMENT
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit; mfa; legal-hold check
- id: POL-IMP-SUBMIT
  command: CMD-IMP-SUBMIT
  subject: adapter service account · Administrator
  resource: AGG-IMPORT-BATCH
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-IMP-REPROCESS-QUARANTINE
  command: CMD-IMP-REPROCESS-QUARANTINE
  subject: adapter service account · Administrator
  resource: AGG-IMPORT-BATCH
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-IMP-ACCEPT-QUARANTINE
  command: CMD-IMP-ACCEPT-QUARANTINE
  subject: adapter service account · Administrator
  resource: AGG-IMPORT-BATCH
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-IMP-CANCEL
  command: CMD-IMP-CANCEL
  subject: adapter service account · Administrator
  resource: AGG-IMPORT-BATCH
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-EXT-MAP
  command: CMD-EXT-MAP
  subject: adapter service account · Analyst
  resource: AGG-EXTERNAL-ID
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-EXT-END
  command: CMD-EXT-END
  subject: adapter service account · Analyst
  resource: AGG-EXTERNAL-ID
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ADP-REGISTER
  command: CMD-ADP-REGISTER
  subject: Administrator (register, update) · second Administrator (activate)
  resource: AGG-ADAPTER
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ADP-UPDATE-MAPPING
  command: CMD-ADP-UPDATE-MAPPING
  subject: Administrator (register, update) · second Administrator (activate)
  resource: AGG-ADAPTER
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ADP-ACTIVATE
  command: CMD-ADP-ACTIVATE
  subject: Administrator (register, update) · second Administrator (activate)
  resource: AGG-ADAPTER
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: approver ≠ author
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ADP-SUSPEND
  command: CMD-ADP-SUSPEND
  subject: Administrator (register, update) · second Administrator (activate)
  resource: AGG-ADAPTER
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ADP-RESUME
  command: CMD-ADP-RESUME
  subject: Administrator (register, update) · second Administrator (activate)
  resource: AGG-ADAPTER
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
- id: POL-ADP-RETIRE
  command: CMD-ADP-RETIRE
  subject: Administrator (register, update) · second Administrator (activate)
  resource: AGG-ADAPTER
  context_conditions: tenant match; object visible to subject (label ≤ clearance); write permission in org scope
  segregation_of_duties: —
  decision: ALLOW
  otherwise: DENY (not-found shape if object invisible)
  obligations: audit
query_policies:
- id: POL-ENT-RESOLVED
  query: QRY-ENT-RESOLVED
  subject: any user; claims label-filtered (INV-ENT-02)
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-ENT-CLAIMS
  query: QRY-ENT-CLAIMS
  subject: any user; label-filtered
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-ENT-LIST
  query: QRY-ENT-LIST
  subject: any user; allowed_scope pre-filter
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-ENT-POSITIONS
  query: QRY-ENT-POSITIONS
  subject: any user; label-filtered; geometry generalized by obligation
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-RWE-GET
  query: QRY-RWE-GET
  subject: any user; label-filtered
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-REL-LIST
  query: QRY-REL-LIST
  subject: any user; hidden relationships and endpoints omitted
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-CLM-GET
  query: QRY-CLM-GET
  subject: any user; label-filtered
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-OBS-LIST
  query: QRY-OBS-LIST
  subject: any user; allowed_scope pre-filter
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-OBS-GET
  query: QRY-OBS-GET
  subject: any user; label-filtered
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-SRC-GET
  query: QRY-SRC-GET
  subject: Analyst and above; protection policy
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-EVD-GET
  query: QRY-EVD-GET
  subject: any user; label-filtered
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-ATT-DOWNLOAD
  query: QRY-ATT-DOWNLOAD
  subject: authorized on the owning evidence/observation
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-LIN-TRACE
  query: QRY-LIN-TRACE
  subject: any user; per-node authorization
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-EXT-RESOLVE
  query: QRY-EXT-RESOLVE
  subject: adapter service accounts; Analyst
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-IMP-GET
  query: QRY-IMP-GET
  subject: adapter owner; Administrator
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
- id: POL-ADP-GET
  query: QRY-ADP-GET
  subject: Administrator
  allowed_scope: org scope ∩ classification rule; claims filtered by label
  otherwise: DENY (not-found shape)
```

</details>
