---
id: TST-SIMULATION-SM
type: acceptance-spec
title: Acceptance — Simulation state machine
wave: W6
slice: SLC-19
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
generated_from: AGG-SIMULATION
traces:
  verifies:
  - SL-05
  - AGG-SIMULATION
  - REQ-TRX-008
  - REQ-TRX-009
  - REQ-TRX-010
  - REQ-TRX-011
---

# Acceptance — Simulation

مولّدة من مصفوفة AGG-SIMULATION: 10 انتقالات مسموحة، 19 رفضاً.

```gherkin
Feature: Simulation lifecycle (AGG-SIMULATION)

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
      | Simulation | IN_PROGRESS | CMD-SIM-DELIVER-INJECT | IN_PROGRESS | EVT-SIM-INJECT-DELIVERED | 2 |
      | Simulation | IN_PROGRESS | CMD-SIM-RECORD-EVALUATION | IN_PROGRESS | EVT-SIM-EVALUATION-RECORDED | 2 |
      | Simulation | IN_PROGRESS | CMD-SIM-PAUSE | PAUSED | EVT-SIM-PAUSED | 2 |
      | Simulation | IN_PROGRESS | CMD-SIM-COMPLETE | COMPLETED | EVT-SIM-COMPLETED | 3 |
      | Simulation | IN_PROGRESS | CMD-SIM-ABORT | ABORTED | EVT-SIM-ABORTED | 2 |
      | Simulation | PAUSED | CMD-SIM-RECORD-EVALUATION | PAUSED | EVT-SIM-EVALUATION-RECORDED | 3 |
      | Simulation | PAUSED | CMD-SIM-RESUME | IN_PROGRESS | EVT-SIM-RESUMED | 3 |
      | Simulation | PAUSED | CMD-SIM-COMPLETE | COMPLETED | EVT-SIM-COMPLETED | 3 |
      | Simulation | PAUSED | CMD-SIM-ABORT | ABORTED | EVT-SIM-ABORTED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Simulation | CMD-SIM-START | IN_PROGRESS | EVT-SIM-STARTED |

  Scenario: Completion fails while any exercise participant is unevaluated
    Given a Simulation M for an Exercise with participants P1 and P2
    And only P1 has a recorded evaluation
    When the actor sends CMD-SIM-COMPLETE
    Then the command is rejected with EVALUATION_MISSING
    And the state remains IN_PROGRESS

  Scenario: Completion succeeds once every participant has a recorded evaluation
    Given a Simulation M for an Exercise with participants P1 and P2
    And both P1 and P2 have a recorded evaluation
    When the actor sends CMD-SIM-COMPLETE
    Then the state becomes COMPLETED

  Scenario: An evaluator can never evaluate themself
    Given a Simulation M IN_PROGRESS with participant P1
    When P1 sends CMD-SIM-RECORD-EVALUATION for participant P1
    Then the command is rejected with SEGREGATION_OF_DUTIES
    And no evaluation is recorded

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Simulation | IN_PROGRESS | CMD-SIM-START | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | PAUSED | CMD-SIM-START | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | COMPLETED | CMD-SIM-START | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | ABORTED | CMD-SIM-START | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | PAUSED | CMD-SIM-DELIVER-INJECT | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | COMPLETED | CMD-SIM-DELIVER-INJECT | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | ABORTED | CMD-SIM-DELIVER-INJECT | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | COMPLETED | CMD-SIM-RECORD-EVALUATION | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | ABORTED | CMD-SIM-RECORD-EVALUATION | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | PAUSED | CMD-SIM-PAUSE | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | COMPLETED | CMD-SIM-PAUSE | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | ABORTED | CMD-SIM-PAUSE | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | IN_PROGRESS | CMD-SIM-RESUME | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | COMPLETED | CMD-SIM-RESUME | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | ABORTED | CMD-SIM-RESUME | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | COMPLETED | CMD-SIM-COMPLETE | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | ABORTED | CMD-SIM-COMPLETE | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | COMPLETED | CMD-SIM-ABORT | SIMULATION_INVALID_STATE_TRANSITION |
      | Simulation | ABORTED | CMD-SIM-ABORT | SIMULATION_INVALID_STATE_TRANSITION |
```
