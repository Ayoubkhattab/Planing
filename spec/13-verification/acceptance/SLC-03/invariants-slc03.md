---
id: TST-SLC03-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-03 task rules, eligibility, scheduling and offline contract
wave: W6
slice: SLC-03
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-OPS-014, REQ-RDY-001, REQ-RDY-002, REQ-OFF-001, QAS-OPS-002, QAS-PERF-016]}
---

# Acceptance — Task Rules

```gherkin
Feature: Completion semantics (OQ-031, BRL-006)

  Scenario: Automatic completion when all criteria are machine-checkable
    Given a task whose criteria are "result_item ≥ 1" and "evidence_count ≥ 2", both satisfied
    When the reviewer approves it
    Then the task is COMPLETED immediately with one TaskApproved and one TaskCompleted event

  Scenario: Attestation criteria require an explicit completion
    Given an APPROVED task with an unconfirmed attestation criterion
    Then the task stays APPROVED
    When an authorized actor completes it with the attestation
    Then the task is COMPLETED

  Scenario: Completion blocked by unmet criteria
    Given an APPROVED task with "evidence_count ≥ 2" and 1 evidence
    When CMD-TASK-COMPLETE is sent
    Then it is rejected with TASK_CRITERIA_NOT_MET

  Scenario: Auto-close after the follow-up window
    Given a COMPLETED task with no open follow-ups for 7 days
    Then the task is CLOSED by the scheduler

  Scenario: Open follow-ups prevent closing
    Given a COMPLETED task with an open follow-up task
    When CMD-TASK-CLOSE is sent
    Then it is rejected with OPEN_FOLLOW_UPS

Feature: Deadlines (OQ-032, REQ-OPS-012)

  Scenario: Default is escalation, not expiry
    Given an IN_PROGRESS task of a type with expires_on_due = false
    When due_at passes
    Then within 60 s a TaskEscalated event is emitted and the state stays IN_PROGRESS

  Scenario: Expiry only when declared by the task type
    Given an ASSIGNED task of a type with expires_on_due = true
    When due_at passes
    Then the task is EXPIRED

Feature: Rejection is final (OQ-033)

  Scenario: Rework after rejection is a new task
    Given an UNDER_REVIEW task T1
    When the reviewer rejects it with create_follow_up = true
    Then T1 is REJECTED and a new DRAFT task T2 exists with follow_up_of = T1

Feature: Suspension is a flag (INV-TASK-06)

  Scenario: Suspended task keeps its state and rejects work
    Given an IN_PROGRESS task that is suspended
    When the assignee submits it
    Then the command is rejected with TASK_SUSPENDED
    When the task is unsuspended
    Then the state is IN_PROGRESS and submission is accepted

Feature: Assignment guards

  Scenario: Ineligible assignee                                                  # REQ-OPS-007
    Given a task type requiring certification "HAZMAT" level 2
    And person P has competency HAZMAT without certification
    When P is assigned
    Then the command is rejected with ASSIGNEE_NOT_ELIGIBLE and reason REQUIRES_CERTIFICATION

  Scenario: Supervision makes assignment conditional
    Given the type allows supervision and P has level 1 of the required level 2
    When P is assigned with supervisor S who is ELIGIBLE
    Then the task is ASSIGNED with eligibility snapshot CONDITIONALLY_ELIGIBLE

  Scenario: Eligibility is evaluated at the assignment time
    Given P's certification expires at 12:00
    When P is assigned at 12:01
    Then the command is rejected with reason EXPIRED even if the expiry transition has not run

  Scenario: Clearance below task label
    Given a CONFIDENTIAL task and user U cleared INTERNAL
    When U is assigned
    Then the command is rejected

  Scenario: Eligibility service unavailable
    Given BC05 is unreachable and no cached result exists
    When a Planner assigns the task
    Then the command is rejected with ELIGIBILITY_UNAVAILABLE

Feature: Segregation of duties (REQ-OPS-009)

  Scenario: Assignee cannot approve own task
    Given a SUBMITTED task assigned to A
    When A starts the review
    Then the command is rejected with SEGREGATION_OF_DUTIES

Feature: Plan link (REQ-OPS-010)

  Scenario: Task without plan requires ad-hoc reason and owner
    When a task is created without plan_ref and without ad_hoc_reason
    Then the command is rejected with TASK_INVALID

Feature: Dependencies

  Scenario: Start waits for predecessors
    Given T2 depends on T1 which is IN_PROGRESS
    When the assignee starts T2
    Then the command is rejected with DEPENDENCIES_NOT_MET

  Scenario: Dependency cycle is rejected
    Given T2 depends on T1
    When T1 is edited to depend on T2
    Then the command is rejected with TASK_INVALID

Feature: Offline contract (REQ-OFF-001, ADR-P09)

  Scenario: Offline-capable commands replay in order
    Given a device recorded ACCEPT, START, ADD-RESULT-ITEM, SUBMIT offline with base versions 3, 4, 5, 6
    When it reconnects and the task is still at version 3
    Then all four commands apply and the task is SUBMITTED at version 7

  Scenario: Stale offline command becomes a sync conflict
    Given a device recorded SUBMIT with base_version 5
    And the task was reassigned online (now version 6)
    When the device replays SUBMIT
    Then the command is not applied and a CF-05 sync conflict is opened for review

  Scenario: Approval is not offline-capable
    Then the OpenAPI operation CMD-TASK-APPROVE has x-offline-capable = false
```
