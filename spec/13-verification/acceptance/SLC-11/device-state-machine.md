---
id: TST-DEVICE-SM
type: acceptance-spec
title: Acceptance — Field Device state machine
wave: W6
slice: SLC-11
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-DEVICE
traces:
  verifies:
  - SL-05
  - AGG-DEVICE
  - REQ-OFF-005
---

# Acceptance — Field Device

مولّدة من مصفوفة AGG-DEVICE: 8 انتقالاً مسموحاً، 34 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: Field Device lifecycle (AGG-DEVICE)

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
      | Field Device | PENDING_ENROLLMENT | CMD-DEV-CONFIRM | ACTIVE | EVT-DEV-ACTIVATED | 3 |
      | Field Device | ACTIVE | CMD-DEV-ROTATE-KEY | ACTIVE | EVT-DEV-KEY-ROTATED | 3 |
      | Field Device | ACTIVE | CMD-DEV-SUSPEND | SUSPENDED | EVT-DEV-SUSPENDED | 3 |
      | Field Device | ACTIVE | CMD-DEV-REPORT-LOST | LOST | EVT-DEV-REPORTED-LOST | 3 |
      | Field Device | ACTIVE | CMD-DEV-RETIRE | RETIRED | EVT-DEV-RETIRED | 3 |
      | Field Device | SUSPENDED | CMD-DEV-REINSTATE | ACTIVE | EVT-DEV-REINSTATED | 3 |
      | Field Device | SUSPENDED | CMD-DEV-REPORT-LOST | LOST | EVT-DEV-REPORTED-LOST | 3 |
      | Field Device | SUSPENDED | CMD-DEV-RETIRE | RETIRED | EVT-DEV-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Field Device | CMD-DEV-ENROLL | PENDING_ENROLLMENT | EVT-DEV-ENROLL-REQUESTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Field Device | PENDING_ENROLLMENT | CMD-DEV-ENROLL | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | PENDING_ENROLLMENT | CMD-DEV-ROTATE-KEY | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | PENDING_ENROLLMENT | CMD-DEV-SUSPEND | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | PENDING_ENROLLMENT | CMD-DEV-REINSTATE | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | PENDING_ENROLLMENT | CMD-DEV-REPORT-LOST | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | PENDING_ENROLLMENT | CMD-DEV-RETIRE | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | ACTIVE | CMD-DEV-ENROLL | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | ACTIVE | CMD-DEV-CONFIRM | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | ACTIVE | CMD-DEV-REINSTATE | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | SUSPENDED | CMD-DEV-ENROLL | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | SUSPENDED | CMD-DEV-CONFIRM | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | SUSPENDED | CMD-DEV-ROTATE-KEY | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | SUSPENDED | CMD-DEV-SUSPEND | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | LOST | CMD-DEV-ENROLL | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | LOST | CMD-DEV-CONFIRM | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | LOST | CMD-DEV-ROTATE-KEY | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | LOST | CMD-DEV-SUSPEND | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | LOST | CMD-DEV-REINSTATE | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | LOST | CMD-DEV-REPORT-LOST | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | LOST | CMD-DEV-RETIRE | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | WIPED | CMD-DEV-ENROLL | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | WIPED | CMD-DEV-CONFIRM | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | WIPED | CMD-DEV-ROTATE-KEY | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | WIPED | CMD-DEV-SUSPEND | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | WIPED | CMD-DEV-REINSTATE | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | WIPED | CMD-DEV-REPORT-LOST | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | WIPED | CMD-DEV-RETIRE | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | RETIRED | CMD-DEV-ENROLL | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | RETIRED | CMD-DEV-CONFIRM | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | RETIRED | CMD-DEV-ROTATE-KEY | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | RETIRED | CMD-DEV-SUSPEND | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | RETIRED | CMD-DEV-REINSTATE | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | RETIRED | CMD-DEV-REPORT-LOST | DEVICE_INVALID_STATE_TRANSITION |
      | Field Device | RETIRED | CMD-DEV-RETIRE | DEVICE_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Field Device | LOST | wipe confirmed by device | WIPED | EVT-DEV-WIPED |
```
