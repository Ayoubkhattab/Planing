---
id: TST-ASSET-ASSIGNMENT-SM
type: acceptance-spec
title: Acceptance — Asset Assignment state machine
wave: W6
slice: SLC-09
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ASSET-ASSIGNMENT
traces:
  verifies:
  - SL-05
  - AGG-ASSET-ASSIGNMENT
  - REQ-RES-003
  - REQ-RES-012
---

# Acceptance — Asset Assignment

مولّدة من مصفوفة AGG-ASSET-ASSIGNMENT: 2 انتقالاً مسموحاً، 7 رفضاً.

```gherkin
Feature: Asset Assignment lifecycle (AGG-ASSET-ASSIGNMENT)

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
      | Asset Assignment | ACTIVE | CMD-ASG-RETURN | RETURNED | EVT-ASG-RETURNED | 3 |
      | Asset Assignment | ACTIVE | CMD-ASG-CANCEL | CANCELLED | EVT-ASG-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Asset Assignment | CMD-ASG-ASSIGN | ACTIVE | EVT-ASG-ASSIGNED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Asset Assignment | ACTIVE | CMD-ASG-ASSIGN | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION |
      | Asset Assignment | RETURNED | CMD-ASG-ASSIGN | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION |
      | Asset Assignment | RETURNED | CMD-ASG-RETURN | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION |
      | Asset Assignment | RETURNED | CMD-ASG-CANCEL | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION |
      | Asset Assignment | CANCELLED | CMD-ASG-ASSIGN | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION |
      | Asset Assignment | CANCELLED | CMD-ASG-RETURN | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION |
      | Asset Assignment | CANCELLED | CMD-ASG-CANCEL | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION |
```
