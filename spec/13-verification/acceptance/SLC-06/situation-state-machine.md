---
id: TST-SITUATION-SM
type: acceptance-spec
title: Acceptance — Situation state machine
wave: W6
slice: SLC-06
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-SITUATION
traces:
  verifies:
  - SL-05
  - AGG-SITUATION
  - REQ-SIT-001
  - REQ-SIT-002
  - REQ-SIT-003
---

# Acceptance — Situation

مولّدة من مصفوفة AGG-SITUATION: 12 انتقالاً مسموحاً، 16 رفضاً.

```gherkin
Feature: Situation lifecycle (AGG-SITUATION)

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
      | Situation | DRAFT | CMD-SIT-EDIT-DEFINITION | DRAFT | EVT-SIT-DEFINITION-CHANGED | 3 |
      | Situation | DRAFT | CMD-SIT-ACTIVATE | ACTIVE | EVT-SIT-ACTIVATED | 3 |
      | Situation | DRAFT | CMD-SIT-CLOSE | CLOSED | EVT-SIT-CLOSED | 3 |
      | Situation | DRAFT | CMD-SIT-RECLASSIFY | DRAFT | EVT-SIT-RECLASSIFIED | 3 |
      | Situation | ACTIVE | CMD-SIT-EDIT-DEFINITION | ACTIVE | EVT-SIT-DEFINITION-CHANGED | 3 |
      | Situation | ACTIVE | CMD-SIT-PAUSE | PAUSED | EVT-SIT-PAUSED | 3 |
      | Situation | ACTIVE | CMD-SIT-CLOSE | CLOSED | EVT-SIT-CLOSED | 3 |
      | Situation | ACTIVE | CMD-SIT-RECLASSIFY | ACTIVE | EVT-SIT-RECLASSIFIED | 3 |
      | Situation | PAUSED | CMD-SIT-EDIT-DEFINITION | PAUSED | EVT-SIT-DEFINITION-CHANGED | 3 |
      | Situation | PAUSED | CMD-SIT-RESUME | ACTIVE | EVT-SIT-RESUMED | 3 |
      | Situation | PAUSED | CMD-SIT-CLOSE | CLOSED | EVT-SIT-CLOSED | 3 |
      | Situation | PAUSED | CMD-SIT-RECLASSIFY | PAUSED | EVT-SIT-RECLASSIFIED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Situation | CMD-SIT-CREATE | DRAFT | EVT-SIT-CREATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Situation | DRAFT | CMD-SIT-CREATE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | DRAFT | CMD-SIT-PAUSE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | DRAFT | CMD-SIT-RESUME | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | ACTIVE | CMD-SIT-CREATE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | ACTIVE | CMD-SIT-ACTIVATE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | ACTIVE | CMD-SIT-RESUME | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | PAUSED | CMD-SIT-CREATE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | PAUSED | CMD-SIT-ACTIVATE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | PAUSED | CMD-SIT-PAUSE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | CLOSED | CMD-SIT-CREATE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | CLOSED | CMD-SIT-EDIT-DEFINITION | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | CLOSED | CMD-SIT-ACTIVATE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | CLOSED | CMD-SIT-PAUSE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | CLOSED | CMD-SIT-RESUME | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | CLOSED | CMD-SIT-CLOSE | SITUATION_INVALID_STATE_TRANSITION |
      | Situation | CLOSED | CMD-SIT-RECLASSIFY | SITUATION_INVALID_STATE_TRANSITION |
```
