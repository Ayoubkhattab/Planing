---
id: TST-ALERT-RULE-SM
type: acceptance-spec
title: Acceptance — Alert Rule state machine
wave: W6
slice: SLC-06
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ALERT-RULE
traces:
  verifies:
  - SL-05
  - AGG-ALERT-RULE
  - REQ-SIT-004
---

# Acceptance — Alert Rule

مولّدة من مصفوفة AGG-ALERT-RULE: 8 انتقالاً مسموحاً، 16 رفضاً.

```gherkin
Feature: Alert Rule lifecycle (AGG-ALERT-RULE)

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
      | Alert Rule | DRAFT | CMD-ARL-EDIT | DRAFT | EVT-ARL-EDITED | 3 |
      | Alert Rule | DRAFT | CMD-ARL-ACTIVATE | ACTIVE | EVT-ARL-ACTIVATED | 3 |
      | Alert Rule | DRAFT | CMD-ARL-RETIRE | RETIRED | EVT-ARL-RETIRED | 3 |
      | Alert Rule | ACTIVE | CMD-ARL-DISABLE | DISABLED | EVT-ARL-DISABLED | 3 |
      | Alert Rule | ACTIVE | CMD-ARL-RETIRE | RETIRED | EVT-ARL-RETIRED | 3 |
      | Alert Rule | DISABLED | CMD-ARL-EDIT | DISABLED | EVT-ARL-EDITED | 3 |
      | Alert Rule | DISABLED | CMD-ARL-ENABLE | ACTIVE | EVT-ARL-ENABLED | 3 |
      | Alert Rule | DISABLED | CMD-ARL-RETIRE | RETIRED | EVT-ARL-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Alert Rule | CMD-ARL-DEFINE | DRAFT | EVT-ARL-DEFINED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Alert Rule | DRAFT | CMD-ARL-DEFINE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | DRAFT | CMD-ARL-DISABLE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | DRAFT | CMD-ARL-ENABLE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | ACTIVE | CMD-ARL-DEFINE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | ACTIVE | CMD-ARL-EDIT | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | ACTIVE | CMD-ARL-ACTIVATE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | ACTIVE | CMD-ARL-ENABLE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | DISABLED | CMD-ARL-DEFINE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | DISABLED | CMD-ARL-ACTIVATE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | DISABLED | CMD-ARL-DISABLE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | RETIRED | CMD-ARL-DEFINE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | RETIRED | CMD-ARL-EDIT | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | RETIRED | CMD-ARL-ACTIVATE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | RETIRED | CMD-ARL-DISABLE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | RETIRED | CMD-ARL-ENABLE | ALERT_RULE_INVALID_STATE_TRANSITION |
      | Alert Rule | RETIRED | CMD-ARL-RETIRE | ALERT_RULE_INVALID_STATE_TRANSITION |
```
