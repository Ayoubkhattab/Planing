---
id: TST-EVAL-SUITE-SM
type: acceptance-spec
title: Acceptance — Evaluation Suite state machine
wave: W6
slice: SLC-10
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-EVAL-SUITE
traces:
  verifies:
  - SL-05
  - AGG-EVAL-SUITE
  - REQ-AI-010
---

# Acceptance — Evaluation Suite

مولّدة من مصفوفة AGG-EVAL-SUITE: 2 انتقالاً مسموحاً، 7 رفضاً.

```gherkin
Feature: Evaluation Suite lifecycle (AGG-EVAL-SUITE)

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
      | Evaluation Suite | DRAFT | CMD-EVS-EDIT | DRAFT | EVT-EVS-EDITED | 3 |
      | Evaluation Suite | DRAFT | CMD-EVS-ACTIVATE | ACTIVE | EVT-EVS-ACTIVATED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Evaluation Suite | CMD-EVS-DRAFT | DRAFT | EVT-EVS-DRAFTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Evaluation Suite | DRAFT | CMD-EVS-DRAFT | EVAL_SUITE_INVALID_STATE_TRANSITION |
      | Evaluation Suite | ACTIVE | CMD-EVS-DRAFT | EVAL_SUITE_INVALID_STATE_TRANSITION |
      | Evaluation Suite | ACTIVE | CMD-EVS-EDIT | EVAL_SUITE_INVALID_STATE_TRANSITION |
      | Evaluation Suite | ACTIVE | CMD-EVS-ACTIVATE | EVAL_SUITE_INVALID_STATE_TRANSITION |
      | Evaluation Suite | SUPERSEDED | CMD-EVS-DRAFT | EVAL_SUITE_INVALID_STATE_TRANSITION |
      | Evaluation Suite | SUPERSEDED | CMD-EVS-EDIT | EVAL_SUITE_INVALID_STATE_TRANSITION |
      | Evaluation Suite | SUPERSEDED | CMD-EVS-ACTIVATE | EVAL_SUITE_INVALID_STATE_TRANSITION |
```
