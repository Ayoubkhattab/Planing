---
id: TST-DISTRIBUTION-SM
type: acceptance-spec
title: Acceptance — Distribution state machine
wave: W6
slice: SLC-12
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-DISTRIBUTION
traces:
  verifies:
  - SL-05
  - AGG-DISTRIBUTION
  - REQ-PRD-004
  - REQ-PRD-005
---

# Acceptance — Distribution

مولّدة من مصفوفة AGG-DISTRIBUTION: 1 انتقالاً مسموحاً، 7 رفضاً.

```gherkin
Feature: Distribution lifecycle (AGG-DISTRIBUTION)

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
      | Distribution | PREPARING | CMD-DST-CANCEL | CANCELLED | EVT-DST-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Distribution | CMD-DST-DISTRIBUTE | PREPARING | EVT-DST-STARTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Distribution | PREPARING | CMD-DST-DISTRIBUTE | DISTRIBUTION_INVALID_STATE_TRANSITION |
      | Distribution | COMPLETED | CMD-DST-DISTRIBUTE | DISTRIBUTION_INVALID_STATE_TRANSITION |
      | Distribution | COMPLETED | CMD-DST-CANCEL | DISTRIBUTION_INVALID_STATE_TRANSITION |
      | Distribution | COMPLETED_WITH_EXCLUSIONS | CMD-DST-DISTRIBUTE | DISTRIBUTION_INVALID_STATE_TRANSITION |
      | Distribution | COMPLETED_WITH_EXCLUSIONS | CMD-DST-CANCEL | DISTRIBUTION_INVALID_STATE_TRANSITION |
      | Distribution | CANCELLED | CMD-DST-DISTRIBUTE | DISTRIBUTION_INVALID_STATE_TRANSITION |
      | Distribution | CANCELLED | CMD-DST-CANCEL | DISTRIBUTION_INVALID_STATE_TRANSITION |
```
