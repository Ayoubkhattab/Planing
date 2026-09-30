---
id: TST-DECISION-REQUEST-SM
type: acceptance-spec
title: Acceptance — Decision Request state machine
wave: W6
slice: SLC-08
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-DECISION-REQUEST
traces:
  verifies:
  - SL-05
  - AGG-DECISION-REQUEST
  - REQ-DEC-001
---

# Acceptance — Decision Request

مولّدة من مصفوفة AGG-DECISION-REQUEST: 7 انتقالاً مسموحاً، 13 رفضاً، 2 انتقالاً نظامياً (SYS).

```gherkin
Feature: Decision Request lifecycle (AGG-DECISION-REQUEST)

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
      | Decision Request | DRAFT | CMD-DRQ-ADD-OPTION | DRAFT | EVT-DRQ-OPTION-ADDED | 3 |
      | Decision Request | DRAFT | CMD-DRQ-CITE | DRAFT | EVT-DRQ-CITED | 3 |
      | Decision Request | DRAFT | CMD-DRQ-OPEN | OPEN | EVT-DRQ-OPENED | 3 |
      | Decision Request | DRAFT | CMD-DRQ-WITHDRAW | WITHDRAWN | EVT-DRQ-WITHDRAWN | 3 |
      | Decision Request | OPEN | CMD-DRQ-ADD-OPTION | OPEN | EVT-DRQ-OPTION-ADDED | 3 |
      | Decision Request | OPEN | CMD-DRQ-CITE | OPEN | EVT-DRQ-CITED | 3 |
      | Decision Request | OPEN | CMD-DRQ-WITHDRAW | WITHDRAWN | EVT-DRQ-WITHDRAWN | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Decision Request | CMD-DRQ-CREATE | DRAFT | EVT-DRQ-CREATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Decision Request | DRAFT | CMD-DRQ-CREATE | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | OPEN | CMD-DRQ-CREATE | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | OPEN | CMD-DRQ-OPEN | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | DECIDED | CMD-DRQ-CREATE | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | DECIDED | CMD-DRQ-ADD-OPTION | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | DECIDED | CMD-DRQ-CITE | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | DECIDED | CMD-DRQ-OPEN | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | DECIDED | CMD-DRQ-WITHDRAW | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | WITHDRAWN | CMD-DRQ-CREATE | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | WITHDRAWN | CMD-DRQ-ADD-OPTION | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | WITHDRAWN | CMD-DRQ-CITE | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | WITHDRAWN | CMD-DRQ-OPEN | DECISION_REQUEST_INVALID_STATE_TRANSITION |
      | Decision Request | WITHDRAWN | CMD-DRQ-WITHDRAW | DECISION_REQUEST_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Decision Request | OPEN | deadline passed | OPEN | EVT-DRQ-ESCALATED |
      | Decision Request | OPEN | decision recorded for this request | DECIDED | EVT-DRQ-DECIDED |
```
