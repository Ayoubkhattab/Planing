---
id: TST-ERASURE-REQUEST-SM
type: acceptance-spec
title: Acceptance — Erasure Request state machine
wave: W6
slice: SLC-12a
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ERASURE-REQUEST
traces:
  verifies:
  - SL-05
  - AGG-ERASURE-REQUEST
  - REQ-GOV-008
---

# Acceptance — Erasure Request

مولّدة من مصفوفة AGG-ERASURE-REQUEST: 2 انتقالاً مسموحاً، 19 رفضاً، 5 انتقالاً نظامياً (SYS).

```gherkin
Feature: Erasure Request lifecycle (AGG-ERASURE-REQUEST)

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
      | Erasure Request | SCOPED | CMD-ERS-APPROVE | APPROVED | EVT-ERS-APPROVED | 3 |
      | Erasure Request | SCOPED | CMD-ERS-REJECT | REJECTED | EVT-ERS-REJECTED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Erasure Request | CMD-ERS-REGISTER | RECEIVED | EVT-ERS-RECEIVED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Erasure Request | RECEIVED | CMD-ERS-REGISTER | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | RECEIVED | CMD-ERS-APPROVE | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | RECEIVED | CMD-ERS-REJECT | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | SCOPED | CMD-ERS-REGISTER | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | APPROVED | CMD-ERS-REGISTER | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | APPROVED | CMD-ERS-APPROVE | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | APPROVED | CMD-ERS-REJECT | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | BLOCKED_BY_HOLD | CMD-ERS-REGISTER | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | BLOCKED_BY_HOLD | CMD-ERS-APPROVE | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | BLOCKED_BY_HOLD | CMD-ERS-REJECT | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | EXECUTING | CMD-ERS-REGISTER | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | EXECUTING | CMD-ERS-APPROVE | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | EXECUTING | CMD-ERS-REJECT | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | COMPLETED | CMD-ERS-REGISTER | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | COMPLETED | CMD-ERS-APPROVE | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | COMPLETED | CMD-ERS-REJECT | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | REJECTED | CMD-ERS-REGISTER | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | REJECTED | CMD-ERS-APPROVE | ERASURE_REQUEST_INVALID_STATE_TRANSITION |
      | Erasure Request | REJECTED | CMD-ERS-REJECT | ERASURE_REQUEST_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Erasure Request | RECEIVED | subject scope resolved | SCOPED | EVT-ERS-SCOPED |
      | Erasure Request | APPROVED | hold matches subject | BLOCKED_BY_HOLD | EVT-ERS-BLOCKED |
      | Erasure Request | APPROVED | execution started | EXECUTING | EVT-ERS-EXECUTING |
      | Erasure Request | BLOCKED_BY_HOLD | hold released | APPROVED | EVT-ERS-UNBLOCKED |
      | Erasure Request | EXECUTING | all contexts confirmed | COMPLETED | EVT-ERS-COMPLETED |
```
