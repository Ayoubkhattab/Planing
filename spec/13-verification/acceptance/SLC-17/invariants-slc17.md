---
id: TST-SLC17-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-17 risk lifecycle, incident escalation, contingency activation
wave: W6
slice: SLC-17
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
traces: {verifies: [REQ-RCM-002, REQ-RCM-003, REQ-RCM-004, REQ-RCM-005, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013, QAS-RCM-001, QAS-RCM-002]}
---

# Acceptance — Risk & Contingency

```gherkin
Feature: Risk lifecycle                                                          # REQ-RCM-002/003/004/005

  Scenario: Risk score is always computed
    Given a risk assessed with likelihood 4 and impact 3
    Then risk_score reads 12
    When the actor attempts to submit risk_score directly in the assessment payload
    Then the submitted value is ignored and risk_score is still computed as likelihood × impact

  Scenario: Segregation of duties on assessment
    Given tenant policy requires segregation of duties for risk assessment
    And analyst A identified risk K
    When A attempts to assess K
    Then the command is rejected with SEGREGATION_OF_DUTIES
    When a different analyst B assesses K
    Then the assessment succeeds

  Scenario: Treatment requires an action unless accepted
    Given risk K is ASSESSED
    When the actor plans treatment with strategy "reduce" and zero treatment_task_refs
    Then the command is rejected with TREATMENT_INVALID
    When the actor plans treatment with strategy "accept" and an authorized approver
    Then the command succeeds with zero treatment actions

  Scenario: Closing a risk always needs a rationale, and cannot be undone
    When the actor closes risk K without a rationale
    Then the command is rejected with RATIONALE_REQUIRED
    When the actor closes K with rationale "retired"
    Then K is CLOSED
    And no command exists to reopen K — a new Risk must be identified instead

Feature: Incident severity and contingency                                       # REQ-RCM-009/011/012

  Scenario: Severity only increases via escalate
    Given incident I is ASSESSED at severity MAJOR
    When the commander sends CMD-INC-ESCALATE with new_severity MAJOR
    Then the command is rejected with SEVERITY_MUST_INCREASE
    When the commander sends CMD-INC-ESCALATE with new_severity CRISIS
    Then I's severity becomes CRISIS

  Scenario: De-escalation is a distinct, authorized, single-step action
    Given incident I is at severity CRISIS
    When an actor without de-escalation authority sends CMD-INC-DE-ESCALATE with new_severity MINOR
    Then the command is rejected
    When an authorized commander sends CMD-INC-DE-ESCALATE with new_severity EMERGENCY and a reason
    Then I's severity becomes EMERGENCY (one level down, not MINOR)

  Scenario: Contingency activation is never automatic
    Given incident I is escalated from MAJOR to CRISIS
    Then no Plan is created or activated as a result
    When the commander separately sends CMD-INC-ACTIVATE-CONTINGENCY with an authorized plan_template_ref
    Then a Plan is created with plan_kind CONTINGENCY and triggered_by = I

  Scenario: Linking a materialized risk never changes the risk
    Given risk K is TREATED
    When incident I is reported with risk_ref = K
    Then K's state, version and label are unchanged
    When I is later closed with rationale on K separately set to "materialized" and incident_ref = I
    Then K's own closure is a separate command the risk owner issued, not a side effect of I's lifecycle

Feature: Response tasks and closure gate                                         # REQ-RCM-010/013

  Scenario: Response tasks reuse SLC-03 directly
    Given incident I is ASSESSED
    When the commander creates a task with incident_ref = I and no plan_ref
    Then the task is created (CR-61) and appears among I's response_task_refs after dispatch

  Scenario: Cannot close while response is open
    Given incident I is CONTAINED with one response task still IN_PROGRESS
    When the commander attempts CMD-INC-RESOLVE
    Then the command is rejected with RESPONSE_TASKS_OPEN
    When that task reaches a terminal state
    Then CMD-INC-RESOLVE succeeds
```
