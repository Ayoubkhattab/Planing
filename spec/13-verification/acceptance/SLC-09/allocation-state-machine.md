---
id: TST-ALLOCATION-SM
type: acceptance-spec
title: Acceptance — Resource Allocation state machine
wave: W6
slice: SLC-09
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ALLOCATION
traces:
  verifies:
  - SL-05
  - AGG-ALLOCATION
  - REQ-RES-007
  - REQ-RES-008
  - REQ-RES-009
  - REQ-RES-010
  - REQ-RES-011
  - REQ-RES-012
---

# Acceptance — Resource Allocation

مولّدة من مصفوفة AGG-ALLOCATION: 5 انتقالاً مسموحاً، 31 رفضاً، 5 انتقالاً نظامياً (SYS).

```gherkin
Feature: Resource Allocation lifecycle (AGG-ALLOCATION)

  Background:
    Given an ACTIVE tenant, baseline policies, and an authorized actor
    And every guard of the command is satisfied

  Scenario Outline: allowed transition
    Given a <aggregate> in state <from> at version <v>
    When the actor sends <command> with a new Idempotency-Key and If-Match <v>
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And one audit record is written in the same transaction

    Examples:
      | aggregate | from | command | to | event | v |
      | Resource Allocation | PENDING_APPROVAL | CMD-ALC-APPROVE | COMMITTED | EVT-ALC-COMMITTED | 3 |
      | Resource Allocation | PENDING_APPROVAL | CMD-ALC-REJECT | REJECTED | EVT-ALC-REJECTED | 3 |
      | Resource Allocation | COMMITTED | CMD-ALC-RECORD-CONSUMPTION | COMMITTED | EVT-ALC-CONSUMED | 3 |
      | Resource Allocation | COMMITTED | CMD-ALC-PREEMPT | PREEMPTED | EVT-ALC-PREEMPTED | 3 |
      | Resource Allocation | COMMITTED | CMD-ALC-RELEASE | RELEASED | EVT-ALC-RELEASED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Resource Allocation | CMD-ALC-REQUEST | REQUESTED | EVT-ALC-REQUESTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Resource Allocation | REQUESTED | CMD-ALC-REQUEST | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REQUESTED | CMD-ALC-APPROVE | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REQUESTED | CMD-ALC-REJECT | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REQUESTED | CMD-ALC-RECORD-CONSUMPTION | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REQUESTED | CMD-ALC-PREEMPT | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REQUESTED | CMD-ALC-RELEASE | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | PENDING_APPROVAL | CMD-ALC-REQUEST | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | PENDING_APPROVAL | CMD-ALC-RECORD-CONSUMPTION | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | PENDING_APPROVAL | CMD-ALC-PREEMPT | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | PENDING_APPROVAL | CMD-ALC-RELEASE | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | COMMITTED | CMD-ALC-REQUEST | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | COMMITTED | CMD-ALC-APPROVE | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | COMMITTED | CMD-ALC-REJECT | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REJECTED | CMD-ALC-REQUEST | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REJECTED | CMD-ALC-APPROVE | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REJECTED | CMD-ALC-REJECT | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REJECTED | CMD-ALC-RECORD-CONSUMPTION | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REJECTED | CMD-ALC-PREEMPT | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | REJECTED | CMD-ALC-RELEASE | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | PREEMPTED | CMD-ALC-REQUEST | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | PREEMPTED | CMD-ALC-APPROVE | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | PREEMPTED | CMD-ALC-REJECT | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | PREEMPTED | CMD-ALC-RECORD-CONSUMPTION | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | PREEMPTED | CMD-ALC-PREEMPT | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | PREEMPTED | CMD-ALC-RELEASE | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | RELEASED | CMD-ALC-REQUEST | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | RELEASED | CMD-ALC-APPROVE | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | RELEASED | CMD-ALC-REJECT | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | RELEASED | CMD-ALC-RECORD-CONSUMPTION | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | RELEASED | CMD-ALC-PREEMPT | ALLOCATION_INVALID_STATE_TRANSITION |
      | Resource Allocation | RELEASED | CMD-ALC-RELEASE | ALLOCATION_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Resource Allocation | REQUESTED | all checks passed | COMMITTED | EVT-ALC-COMMITTED |
      | Resource Allocation | REQUESTED | checks passed, policy requires approval | PENDING_APPROVAL | EVT-ALC-APPROVAL-REQUIRED |
      | Resource Allocation | REQUESTED | a check failed | REJECTED | EVT-ALC-REJECTED |
      | Resource Allocation | PENDING_APPROVAL | provisional hold (1 h) elapsed | REJECTED | EVT-ALC-REJECTED |
      | Resource Allocation | COMMITTED | linked task terminal | RELEASED | EVT-ALC-RELEASED |
```
