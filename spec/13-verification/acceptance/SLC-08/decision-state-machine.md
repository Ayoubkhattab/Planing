---
id: TST-DECISION-SM
type: acceptance-spec
title: Acceptance — Decision state machine
wave: W6
slice: SLC-08
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-DECISION
traces:
  verifies:
  - SL-05
  - AGG-DECISION
  - REQ-DEC-002
  - REQ-DEC-003
  - REQ-DEC-004
---

# Acceptance — Decision

مولّدة من مصفوفة AGG-DECISION: 1 انتقالاً مسموحاً، 5 رفضاً.

```gherkin
Feature: Decision lifecycle (AGG-DECISION)

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
      | Decision | RECORDED | CMD-DEC-ANNUL | ANNULLED | EVT-DEC-ANNULLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Decision | CMD-DEC-RECORD | RECORDED | EVT-DEC-RECORDED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Decision | RECORDED | CMD-DEC-RECORD | DECISION_INVALID_STATE_TRANSITION |
      | Decision | SUPERSEDED | CMD-DEC-RECORD | DECISION_INVALID_STATE_TRANSITION |
      | Decision | SUPERSEDED | CMD-DEC-ANNUL | DECISION_INVALID_STATE_TRANSITION |
      | Decision | ANNULLED | CMD-DEC-RECORD | DECISION_INVALID_STATE_TRANSITION |
      | Decision | ANNULLED | CMD-DEC-ANNUL | DECISION_INVALID_STATE_TRANSITION |
```
