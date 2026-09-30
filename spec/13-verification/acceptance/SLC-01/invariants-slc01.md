---
id: TST-SLC01-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-01 guards, invariants and security scenarios
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-FND-001, REQ-FND-010, REQ-FND-016, REQ-FND-003, REQ-FND-008, REQ-FND-009, REQ-FND-013, REQ-FND-015, REQ-FND-017, REQ-GOV-003, REQ-GOV-004, QAS-SEC-001, QAS-SEC-003, QAS-SEC-005, QAS-SEC-008]}
---

# Acceptance — Guards, Invariants & Security

```gherkin
Feature: Tenant isolation and provisioning

  Scenario: Cross-tenant access is indistinguishable from absence            # REQ-FND-001, PB-01
    Given user U1 of tenant A and user U2 of tenant B exists
    When U1 requests GET /api/v1/foundation/users/{U2.id}
    Then the response is 404 NOT_FOUND with the same body shape as a non-existent id
    And the response time distribution does not differ from a non-existent id (inference suite)

  Scenario: Provisioning is atomic                                            # REQ-FND-003, INV-TEN-01
    Given a tenant provisioning where step "audit stream" fails
    When compensation completes
    Then the tenant state is PROVISIONING_FAILED
    And no user of that tenant can obtain a SecurityContext

  Scenario: Dedicated cell is enforced                                        # INV-TEN-03
    When a platform operator provisions a tenant with sovereign = true and cell_mode = shared
    Then the command is rejected with VALIDATION_FAILED

Feature: Organization tree

  Scenario: No cycles                                                         # INV-ORG-01
    Given units A > B > C in one organization
    When an Administrator moves A under C
    Then the command is rejected with ORG_UNIT_CYCLE

  Scenario: Moving a unit changes scopes immediately                         # THR-S01-12
    Given user U has role Manager scoped to unit B with descendants
    And unit C is moved from under B to under D
    When U requests data scoped to C on the next request
    Then access is evaluated with the new tree and denied

Feature: Authority and delegation

  Scenario: Delegation cannot exceed the delegator                             # INV-AUT-01, REQ-FND-008
    Given grant G1 to M for decision type "operational-plan" in unit B with limit 100
    When M delegates to D with limit 150
    Then the command is rejected with AUTHORITY_EXCEEDS_DELEGATOR

  Scenario: Delegation depth is limited                                        # INV-AUT-02
    Given G1 → G2 (depth 1) → G3 (depth 2), all delegable
    When the holder of G3 delegates further
    Then the command is rejected with AUTHORITY_EXCEEDS_DELEGATOR

  Scenario: Revoking a parent makes delegations ineffective without writing to them   # INV-AUT-03
    Given G1 delegated as G2 to D
    When G1 is revoked at time t
    Then AuthorityCheck(D, type, scope, at = t + 1s) returns authorized = false with reason "parent grant not effective"
    And G2 state is still ACTIVE
    And AuthorityCheck(D, type, scope, at = t - 1s) returns authorized = true

  Scenario: Root grant needs a different Executive                             # INV-AUT-04
    Given a PENDING_APPROVAL grant requested by E1
    When E1 approves it
    Then the command is rejected with SEGREGATION_OF_DUTIES

Feature: Roles and assignments

  Scenario: No self-assignment                                                 # INV-RAS-01, PB-05
    When Administrator A assigns any role to A
    Then the command is rejected with SEGREGATION_OF_DUTIES

  Scenario: Incompatible roles                                                 # INV-RAS-02
    Given user U has an ACTIVE Administrator assignment
    When an Administrator assigns Auditor to U
    Then the command is rejected with SOD_ROLE_CONFLICT

  Scenario: System roles are locked                                            # INV-ROL-01
    When an Administrator changes permissions of system role "Analyst"
    Then the command is rejected with SYSTEM_ROLE_LOCKED

Feature: Clearance and classification

  Scenario: Read requires level and all compartments                           # REQ-GOV-003
    Given object O labeled CONFIDENTIAL with compartments [X, Y]
    And user U cleared SECRET with compartments [X]
    When U requests O
    Then the response is 404 NOT_FOUND

  Scenario: Top-rank clearance needs two officers                              # INV-CLR-03
    Given S1 requested a SECRET clearance for U
    When S1 approves it
    Then the command is rejected with SEGREGATION_OF_DUTIES

  Scenario: Revocation is effective on the next request                        # REQ-GOV-004, QAS-SEC-003
    Given user U has an open session and a cached SecurityContext (age 10 s)
    When U's clearance is revoked
    And U sends any request 1 second later
    Then the PEP detects a newer security_version and rebuilds the context
    And the request is evaluated without the revoked clearance

  Scenario: SCIM disable ends all sessions                                     # QAS-SEC-008
    When the IdP disables U through SCIM
    Then within 5 minutes U's next request from any session is denied

  Scenario: Scheme codes cannot be removed                                      # INV-CLS-03
    Given an ACTIVE scheme with compartment "X" used by objects
    When a Security Officer drafts a new version without "X"
    Then the command is rejected with SCHEME_INVALID
    And deprecating "X" is accepted

Feature: Policy and exceptions

  Scenario: Tenant policy cannot weaken the baseline                            # INV-POL-02
    Given a draft tenant policy that ALLOWs cross-tenant read
    When it is submitted
    Then the command is rejected with POLICY_TESTS_FAILED

  Scenario: Policy engine failure denies                                        # REQ-FND-013, QAS-SEC-005
    Given the policy bundle is older than 5 minutes and no evaluator can refresh it
    When any state-changing command is sent
    Then it is rejected and logged with POLICY_ENGINE_UNAVAILABLE

  Scenario: Exception needs two distinct approvers                              # INV-EXC-01, REQ-FND-017
    Given exception X requested by R
    When A1 approves and then A1 approves again
    Then the second approval is rejected with SEGREGATION_OF_DUTIES
    When A2 approves
    Then X is ACTIVE until ends_at and EXPIRED after it

  Scenario: Baseline rules cannot be excepted                                   # INV-EXC-02
    When a user requests an exception for rule PB-01
    Then the command is rejected with EXCEPTION_NOT_ALLOWED

Feature: Audit

  Scenario: Every command is audited atomically                                 # FIT-04, QAS-AUD-001
    Given a fault is injected after the state row is written and before commit
    Then neither the state change nor the audit record nor the outbox event persists

  Scenario: Audit tampering is detected                                         # QAS-SEC-006
    Given an audit record in shard 3 is modified in storage
    When the integrity check runs
    Then the check reports FAIL for tenant/shard 3 at that seq

  Scenario: Writes stop when audit cannot be guaranteed                          # audit-architecture rule 3
    Given the audit store has been unavailable and the local backlog exceeds the limit
    When any state-changing command is sent
    Then it is rejected with AUDIT_UNAVAILABLE (HTTP 503)
```
