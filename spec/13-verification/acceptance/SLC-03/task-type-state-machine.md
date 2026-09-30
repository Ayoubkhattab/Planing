---
id: TST-TASK-TYPE-SM
type: acceptance-spec
title: Acceptance — Task Type state machine
wave: W6
slice: SLC-03
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-TASK-TYPE
traces:
  verifies:
  - SL-05
  - AGG-TASK-TYPE
  - REQ-OPS-007
  - REQ-OPS-014
---

# Acceptance — Task Type

مولّدة من مصفوفة AGG-TASK-TYPE: 4 انتقالاً مسموحاً، 8 رفضاً.

```gherkin
Feature: Task Type lifecycle (AGG-TASK-TYPE)

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
      | Task Type | DRAFT | CMD-TTY-EDIT | DRAFT | EVT-TTY-EDITED | 3 |
      | Task Type | DRAFT | CMD-TTY-ACTIVATE | ACTIVE | EVT-TTY-ACTIVATED | 3 |
      | Task Type | ACTIVE | CMD-TTY-EDIT | ACTIVE | EVT-TTY-EDITED | 3 |
      | Task Type | ACTIVE | CMD-TTY-RETIRE | RETIRED | EVT-TTY-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Task Type | CMD-TTY-DEFINE | DRAFT | EVT-TTY-DEFINED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Task Type | DRAFT | CMD-TTY-DEFINE | TASK_TYPE_INVALID_STATE_TRANSITION |
      | Task Type | DRAFT | CMD-TTY-RETIRE | TASK_TYPE_INVALID_STATE_TRANSITION |
      | Task Type | ACTIVE | CMD-TTY-DEFINE | TASK_TYPE_INVALID_STATE_TRANSITION |
      | Task Type | ACTIVE | CMD-TTY-ACTIVATE | TASK_TYPE_INVALID_STATE_TRANSITION |
      | Task Type | RETIRED | CMD-TTY-DEFINE | TASK_TYPE_INVALID_STATE_TRANSITION |
      | Task Type | RETIRED | CMD-TTY-EDIT | TASK_TYPE_INVALID_STATE_TRANSITION |
      | Task Type | RETIRED | CMD-TTY-ACTIVATE | TASK_TYPE_INVALID_STATE_TRANSITION |
      | Task Type | RETIRED | CMD-TTY-RETIRE | TASK_TYPE_INVALID_STATE_TRANSITION |
```
