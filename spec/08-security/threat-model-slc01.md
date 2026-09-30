---
id: THREAT-MODEL-SLC01
type: threat-model
title: Threat Model — SLC-01 (STRIDE)
wave: W5
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Threat Model — SLC-01 (STRIDE)

## threats

_12 items_

### THR-S01-01

- **component:** SCIM endpoint
- **stride:** Spoofing/Elevation
- **threat:** SCIM client provisions users with admin roles
- **likelihood:** M
- **impact:** H
- **controls:** SCIM service account can only create PENDING users and link identities; roles never via SCIM (only via CMD-RAS-ASSIGN)
- **residual_risk:** L

### THR-S01-02

- **component:** Role assignment
- **stride:** Elevation
- **threat:** Administrator assigns self a higher role or out-of-scope role
- **likelihood:** M
- **impact:** H
- **controls:** INV-RAS-01 (no self, scope-bound); PB-05; audit
- **residual_risk:** L

### THR-S01-03

- **component:** Delegation
- **stride:** Elevation
- **threat:** Delegation chain amplifies authority
- **likelihood:** L
- **impact:** H
- **controls:** INV-AUT-01/02; effective check evaluates chain at time t
- **residual_risk:** L

### THR-S01-04

- **component:** Clearance
- **stride:** Elevation
- **threat:** Security Officer grants own or colluding clearance
- **likelihood:** L
- **impact:** H
- **controls:** INV-CLR-02/03 two distinct officers for top rank; MFA; audit review
- **residual_risk:** M

### THR-S01-05

- **component:** Policy set
- **stride:** Tampering
- **threat:** Tenant weakens platform baseline via policy
- **likelihood:** M
- **impact:** H
- **controls:** INV-POL-02 restrict-only; PB-* non-overridable; policy tests
- **residual_risk:** L

### THR-S01-06

- **component:** Security exception
- **stride:** Elevation
- **threat:** Long-lived or chained exceptions
- **likelihood:** M
- **impact:** M
- **controls:** 30-day max; two approvers; baseline exempt; exception report to Auditor
- **residual_risk:** L

### THR-S01-07

- **component:** SecurityContext
- **stride:** Spoofing
- **threat:** Forged or replayed internal context
- **likelihood:** L
- **impact:** H
- **controls:** JWS, ≤ 60 s, mTLS, security_version check
- **residual_risk:** L

### THR-S01-08

- **component:** Tenant provisioning
- **stride:** Tampering
- **threat:** Namespace squatting / takeover
- **likelihood:** L
- **impact:** M
- **controls:** platform operator only; namespace immutable; two-person decommission
- **residual_risk:** L

### THR-S01-09

- **component:** Audit outbox
- **stride:** Repudiation
- **threat:** Application deletes audit before shipping
- **likelihood:** L
- **impact:** H
- **controls:** insert-only grants; shipping counters reconciliation; ≤ 5 s window
- **residual_risk:** L

### THR-S01-10

- **component:** Revocation
- **stride:** Info Disclosure
- **threat:** Disabled user keeps access via cached decisions
- **likelihood:** M
- **impact:** H
- **controls:** security_version checked per request (PL-SECURITY-CONTEXT §2)
- **residual_risk:** L

### THR-S01-11

- **component:** Service account
- **stride:** Spoofing
- **threat:** Leaked long-lived credential
- **likelihood:** M
- **impact:** H
- **controls:** ≤ 90 days; public-key credentials; owner accountability; rotation
- **residual_risk:** M

### THR-S01-12

- **component:** Org tree
- **stride:** Tampering
- **threat:** Moving a unit to widen an admin's scope
- **likelihood:** M
- **impact:** M
- **controls:** MoveUnit increments security_version of affected subjects; requires Administrator of both old and new parent scopes
- **residual_risk:** L

## accepted_residual_risks

- THR-S01-04 (M): collusion of two Security Officers — accepted; mitigated by periodic Auditor review
- THR-S01-11 (M): credential leak window ≤ 90 days — accepted; anomaly detection in W8 observability

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S01-01
  component: SCIM endpoint
  stride: Spoofing/Elevation
  threat: SCIM client provisions users with admin roles
  likelihood: M
  impact: H
  controls: SCIM service account can only create PENDING users and link identities; roles never via SCIM (only via CMD-RAS-ASSIGN)
  residual_risk: L
- id: THR-S01-02
  component: Role assignment
  stride: Elevation
  threat: Administrator assigns self a higher role or out-of-scope role
  likelihood: M
  impact: H
  controls: INV-RAS-01 (no self, scope-bound); PB-05; audit
  residual_risk: L
- id: THR-S01-03
  component: Delegation
  stride: Elevation
  threat: Delegation chain amplifies authority
  likelihood: L
  impact: H
  controls: INV-AUT-01/02; effective check evaluates chain at time t
  residual_risk: L
- id: THR-S01-04
  component: Clearance
  stride: Elevation
  threat: Security Officer grants own or colluding clearance
  likelihood: L
  impact: H
  controls: INV-CLR-02/03 two distinct officers for top rank; MFA; audit review
  residual_risk: M
- id: THR-S01-05
  component: Policy set
  stride: Tampering
  threat: Tenant weakens platform baseline via policy
  likelihood: M
  impact: H
  controls: INV-POL-02 restrict-only; PB-* non-overridable; policy tests
  residual_risk: L
- id: THR-S01-06
  component: Security exception
  stride: Elevation
  threat: Long-lived or chained exceptions
  likelihood: M
  impact: M
  controls: 30-day max; two approvers; baseline exempt; exception report to Auditor
  residual_risk: L
- id: THR-S01-07
  component: SecurityContext
  stride: Spoofing
  threat: Forged or replayed internal context
  likelihood: L
  impact: H
  controls: JWS, ≤ 60 s, mTLS, security_version check
  residual_risk: L
- id: THR-S01-08
  component: Tenant provisioning
  stride: Tampering
  threat: Namespace squatting / takeover
  likelihood: L
  impact: M
  controls: platform operator only; namespace immutable; two-person decommission
  residual_risk: L
- id: THR-S01-09
  component: Audit outbox
  stride: Repudiation
  threat: Application deletes audit before shipping
  likelihood: L
  impact: H
  controls: insert-only grants; shipping counters reconciliation; ≤ 5 s window
  residual_risk: L
- id: THR-S01-10
  component: Revocation
  stride: Info Disclosure
  threat: Disabled user keeps access via cached decisions
  likelihood: M
  impact: H
  controls: security_version checked per request (PL-SECURITY-CONTEXT §2)
  residual_risk: L
- id: THR-S01-11
  component: Service account
  stride: Spoofing
  threat: Leaked long-lived credential
  likelihood: M
  impact: H
  controls: ≤ 90 days; public-key credentials; owner accountability; rotation
  residual_risk: M
- id: THR-S01-12
  component: Org tree
  stride: Tampering
  threat: Moving a unit to widen an admin's scope
  likelihood: M
  impact: M
  controls: MoveUnit increments security_version of affected subjects; requires Administrator of both old and new parent scopes
  residual_risk: L
accepted_residual_risks:
- 'THR-S01-04 (M): collusion of two Security Officers — accepted; mitigated by periodic Auditor review'
- 'THR-S01-11 (M): credential leak window ≤ 90 days — accepted; anomaly detection in W8 observability'
```

</details>
