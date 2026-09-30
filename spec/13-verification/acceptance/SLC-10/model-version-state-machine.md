---
id: TST-MODEL-VERSION-SM
type: acceptance-spec
title: Acceptance — Model Version state machine
wave: W6
slice: SLC-10
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-MODEL-VERSION
traces:
  verifies:
  - SL-05
  - AGG-MODEL-VERSION
  - REQ-AI-009
  - REQ-AI-010
---

# Acceptance — Model Version

مولّدة من مصفوفة AGG-MODEL-VERSION: 10 انتقالاً مسموحاً، 62 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: Model Version lifecycle (AGG-MODEL-VERSION)

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
      | Model Version | REGISTERED | CMD-MDL-START-EVALUATION | EVALUATING | EVT-MDL-EVALUATION-STARTED | 3 |
      | Model Version | EVALUATING | CMD-MDL-APPROVE | APPROVED | EVT-MDL-APPROVED | 3 |
      | Model Version | EVALUATING | CMD-MDL-FAIL-EVALUATION | EVALUATION_FAILED | EVT-MDL-EVALUATION-FAILED | 3 |
      | Model Version | APPROVED | CMD-MDL-STAGE | STAGED | EVT-MDL-STAGED | 3 |
      | Model Version | APPROVED | CMD-MDL-DEPRECATE | DEPRECATED | EVT-MDL-DEPRECATED | 3 |
      | Model Version | STAGED | CMD-MDL-PROMOTE | PRODUCTION | EVT-MDL-PROMOTED | 3 |
      | Model Version | STAGED | CMD-MDL-DEPRECATE | DEPRECATED | EVT-MDL-DEPRECATED | 3 |
      | Model Version | PRODUCTION | CMD-MDL-DEPRECATE | DEPRECATED | EVT-MDL-DEPRECATED | 3 |
      | Model Version | DEPRECATED | CMD-MDL-REINSTATE | PRODUCTION | EVT-MDL-REINSTATED | 3 |
      | Model Version | DEPRECATED | CMD-MDL-RETIRE | RETIRED | EVT-MDL-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Model Version | CMD-MDL-REGISTER | REGISTERED | EVT-MDL-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Model Version | REGISTERED | CMD-MDL-REGISTER | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | REGISTERED | CMD-MDL-APPROVE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | REGISTERED | CMD-MDL-FAIL-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | REGISTERED | CMD-MDL-STAGE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | REGISTERED | CMD-MDL-PROMOTE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | REGISTERED | CMD-MDL-DEPRECATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | REGISTERED | CMD-MDL-REINSTATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | REGISTERED | CMD-MDL-RETIRE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATING | CMD-MDL-REGISTER | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATING | CMD-MDL-START-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATING | CMD-MDL-STAGE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATING | CMD-MDL-PROMOTE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATING | CMD-MDL-DEPRECATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATING | CMD-MDL-REINSTATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATING | CMD-MDL-RETIRE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATION_FAILED | CMD-MDL-REGISTER | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATION_FAILED | CMD-MDL-START-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATION_FAILED | CMD-MDL-APPROVE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATION_FAILED | CMD-MDL-FAIL-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATION_FAILED | CMD-MDL-STAGE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATION_FAILED | CMD-MDL-PROMOTE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATION_FAILED | CMD-MDL-DEPRECATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATION_FAILED | CMD-MDL-REINSTATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | EVALUATION_FAILED | CMD-MDL-RETIRE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | APPROVED | CMD-MDL-REGISTER | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | APPROVED | CMD-MDL-START-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | APPROVED | CMD-MDL-APPROVE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | APPROVED | CMD-MDL-FAIL-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | APPROVED | CMD-MDL-PROMOTE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | APPROVED | CMD-MDL-REINSTATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | APPROVED | CMD-MDL-RETIRE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | STAGED | CMD-MDL-REGISTER | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | STAGED | CMD-MDL-START-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | STAGED | CMD-MDL-APPROVE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | STAGED | CMD-MDL-FAIL-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | STAGED | CMD-MDL-STAGE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | STAGED | CMD-MDL-REINSTATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | STAGED | CMD-MDL-RETIRE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | PRODUCTION | CMD-MDL-REGISTER | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | PRODUCTION | CMD-MDL-START-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | PRODUCTION | CMD-MDL-APPROVE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | PRODUCTION | CMD-MDL-FAIL-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | PRODUCTION | CMD-MDL-STAGE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | PRODUCTION | CMD-MDL-PROMOTE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | PRODUCTION | CMD-MDL-REINSTATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | PRODUCTION | CMD-MDL-RETIRE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | DEPRECATED | CMD-MDL-REGISTER | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | DEPRECATED | CMD-MDL-START-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | DEPRECATED | CMD-MDL-APPROVE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | DEPRECATED | CMD-MDL-FAIL-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | DEPRECATED | CMD-MDL-STAGE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | DEPRECATED | CMD-MDL-PROMOTE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | DEPRECATED | CMD-MDL-DEPRECATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | RETIRED | CMD-MDL-REGISTER | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | RETIRED | CMD-MDL-START-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | RETIRED | CMD-MDL-APPROVE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | RETIRED | CMD-MDL-FAIL-EVALUATION | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | RETIRED | CMD-MDL-STAGE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | RETIRED | CMD-MDL-PROMOTE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | RETIRED | CMD-MDL-DEPRECATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | RETIRED | CMD-MDL-REINSTATE | MODEL_VERSION_INVALID_STATE_TRANSITION |
      | Model Version | RETIRED | CMD-MDL-RETIRE | MODEL_VERSION_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Model Version | PRODUCTION | monitoring drift detected | PRODUCTION | EVT-MDL-DRIFT-DETECTED |
```
