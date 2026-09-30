---
id: TST-CAP-MESSAGE-SM
type: acceptance-spec
title: Acceptance — CAP Message (outbound) state machine
wave: W6
slice: SLC-16
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-CAP-MESSAGE
traces:
  verifies:
  - SL-05
  - AGG-CAP-MESSAGE
  - REQ-INT-003
---

# Acceptance — CAP Message (outbound)

مولّدة من مصفوفة AGG-CAP-MESSAGE: 4 انتقالاً مسموحاً، 12 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: CAP Message (outbound) lifecycle (AGG-CAP-MESSAGE)

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
      | CAP Message (outbound) | PREPARED | CMD-CAP-RELEASE | SENT | EVT-CAP-SENT | 3 |
      | CAP Message (outbound) | PREPARED | CMD-CAP-CANCEL | CANCELLED | EVT-CAP-CANCELLED | 3 |
      | CAP Message (outbound) | FAILED | CMD-CAP-RETRY | PREPARED | EVT-CAP-RETRY | 3 |
      | CAP Message (outbound) | FAILED | CMD-CAP-CANCEL | CANCELLED | EVT-CAP-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | CAP Message (outbound) | CMD-CAP-PREPARE | PREPARED | EVT-CAP-PREPARED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | CAP Message (outbound) | PREPARED | CMD-CAP-PREPARE | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | PREPARED | CMD-CAP-RETRY | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | SENT | CMD-CAP-PREPARE | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | SENT | CMD-CAP-RELEASE | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | SENT | CMD-CAP-RETRY | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | SENT | CMD-CAP-CANCEL | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | FAILED | CMD-CAP-PREPARE | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | FAILED | CMD-CAP-RELEASE | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | CANCELLED | CMD-CAP-PREPARE | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | CANCELLED | CMD-CAP-RELEASE | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | CANCELLED | CMD-CAP-RETRY | CAP_MESSAGE_INVALID_STATE_TRANSITION |
      | CAP Message (outbound) | CANCELLED | CMD-CAP-CANCEL | CAP_MESSAGE_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | CAP Message (outbound) | PREPARED | delivery failed after retries | FAILED | EVT-CAP-FAILED |
```
