---
id: TST-SLC08-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-08 authority, decision basis, baselines, change classification, task sync, outcomes
wave: W6
slice: SLC-08
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-DEC-001, REQ-DEC-002, REQ-DEC-003, REQ-DEC-004, REQ-OPS-001, REQ-OPS-002, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-013, REQ-OPS-014, QAS-TRC-003, QAS-PERF-021]}
---

# Acceptance — Decision → Plan → Tasks

```gherkin
Feature: Authority                                                               # REQ-DEC-002, BRL-003

  Scenario: Decision without authority is rejected
    Given manager M has no grant for decision type "resource-reallocation" in unit U
    When M records a decision of that type in U
    Then the command is rejected with AUTHORITY_REQUIRED

  Scenario: Delegated authority works while the parent is effective
    Given E granted "resource-reallocation" in U and delegated it to M
    When M records a decision
    Then the decision is RECORDED with an authority snapshot showing the chain E → M

  Scenario: Authority snapshot survives later revocation
    Given decision D recorded by M under delegation from E
    When E's grant is revoked later
    Then D remains RECORDED and QRY-DEC-BASIS shows the authority valid at D.recorded_at

Feature: Decision basis                                                          # REQ-DEC-003, QAS-TRC-003

  Scenario: What was known at decision time
    Given D cites assessment A version 2 whose key claim was later corrected
    When an auditor requests D's basis
    Then the basis shows A version 2 and the claim value as known at D.recorded_at
    And a separate "current" view shows the corrected value

  Scenario: Decisions require citations
    When a decision is recorded ad-hoc without any citation
    Then the command is rejected with VALIDATION_FAILED

  Scenario: Decisions are immutable                                              # REQ-DEC-004
    Given a RECORDED decision
    When a new decision supersedes it
    Then the old decision is SUPERSEDED and unchanged, and both link to each other

Feature: Plans and baselines                                                      # REQ-OPS-001..005, BRL-004

  Scenario: Plan must implement a decision or objective
    When a plan is created with an empty implements list
    Then the command is rejected with PLAN_INVALID

  Scenario: Approval creates the baseline and activates the plan
    Given version 1 IN_REVIEW authored by P
    When approver A (≠ P, with plan-approval authority) approves it
    Then version 1 is BASELINED and the plan is ACTIVE

  Scenario: Author cannot approve own version
    When P approves version 1
    Then the command is rejected with SEGREGATION_OF_DUTIES

  Scenario: Only one baseline at a time
    Given version 1 BASELINED and version 2 IN_REVIEW
    When version 2 is approved
    Then version 2 is BASELINED and version 1 is SUPERSEDED in the same transaction

  Scenario: Major change requires a new version                                    # BRL-005, REQ-OPS-004
    Given a BASELINED version
    When a planner tries a minor amendment that moves a milestone date
    Then the command is rejected with MAJOR_CHANGE_REQUIRES_VERSION

  Scenario: Minor amendment is allowed
    When a planner amends only an activity description on the baseline
    Then an annotation is recorded and the baseline content is unchanged

  Scenario: Diff classifies changes before approval
    Given a draft that changes one outcome target and one note
    Then QRY-PLV-DIFF classifies the version as major and lists both changes

Feature: Task synchronization                                                      # SPEC-PLAN §3, QAS-PERF-021

  Scenario: New activity creates tasks
    Given version 2 adds task-generating activity A7
    When version 2 is baselined
    Then within 60 s a READY task linked to A7 and plan@v2 exists

  Scenario: Removed activity supersedes open tasks
    Given A3 has an IN_PROGRESS task and version 2 removes A3
    When version 2 is baselined
    Then the task becomes SUPERSEDED

  Scenario: Changed criteria on an assigned task
    Given A4's task is ASSIGNED and version 2 changes A4's completion criteria
    When version 2 is baselined
    Then the old task is SUPERSEDED and a new task with the new criteria is created

  Scenario: Synchronization is idempotent
    When the synchronization for (plan, v1 → v2) runs twice
    Then the second run changes nothing

Feature: Outcomes                                                                   # REQ-OPS-013

  Scenario: Progress as known at a time
    Given measurements 40 (recorded day 10) corrected to 45 (recorded day 12) for target 100
    Then progress known at day 11 is 40 % and known now is 45 %

  Scenario: Plan completion requires measured outcomes
    Given all tasks terminal but outcome O has no measurement
    When the plan is completed
    Then the command is rejected with PLAN_NOT_COMPLETABLE
```
