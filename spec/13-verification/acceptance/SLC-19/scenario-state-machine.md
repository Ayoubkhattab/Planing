---
id: TST-SCENARIO-SM
type: acceptance-spec
title: Acceptance — Scenario state machine
wave: W6
slice: SLC-19
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
generated_from: AGG-SCENARIO
traces:
  verifies:
  - SL-05
  - AGG-SCENARIO
  - REQ-TRX-001
  - REQ-TRX-002
---

# Acceptance — Scenario

مولّدة من مصفوفة AGG-SCENARIO: 4 انتقالات مسموحة، 8 رفضاً.

```gherkin
Feature: Scenario lifecycle (AGG-SCENARIO)

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
      | Scenario | DRAFT | CMD-SCN-EDIT | DRAFT | EVT-SCN-EDITED | 2 |
      | Scenario | DRAFT | CMD-SCN-ACTIVATE | ACTIVE | EVT-SCN-ACTIVATED | 2 |
      | Scenario | ACTIVE | CMD-SCN-EDIT | ACTIVE | EVT-SCN-EDITED | 3 |
      | Scenario | ACTIVE | CMD-SCN-RETIRE | RETIRED | EVT-SCN-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Scenario | CMD-SCN-DEFINE | DRAFT | EVT-SCN-DEFINED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Scenario | DRAFT | CMD-SCN-DEFINE | SCENARIO_INVALID_STATE_TRANSITION |
      | Scenario | DRAFT | CMD-SCN-RETIRE | SCENARIO_INVALID_STATE_TRANSITION |
      | Scenario | ACTIVE | CMD-SCN-DEFINE | SCENARIO_INVALID_STATE_TRANSITION |
      | Scenario | ACTIVE | CMD-SCN-ACTIVATE | SCENARIO_INVALID_STATE_TRANSITION |
      | Scenario | RETIRED | CMD-SCN-DEFINE | SCENARIO_INVALID_STATE_TRANSITION |
      | Scenario | RETIRED | CMD-SCN-EDIT | SCENARIO_INVALID_STATE_TRANSITION |
      | Scenario | RETIRED | CMD-SCN-ACTIVATE | SCENARIO_INVALID_STATE_TRANSITION |
      | Scenario | RETIRED | CMD-SCN-RETIRE | SCENARIO_INVALID_STATE_TRANSITION |

  Scenario: Activation requires a different approver from the author
    Given a Scenario in state DRAFT authored by user U1
    When user U1 sends CMD-SCN-ACTIVATE
    Then the command is rejected with SEGREGATION_OF_DUTIES
    And the state remains DRAFT
```
