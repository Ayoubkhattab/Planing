---
id: TST-CLEARANCE-SM
type: acceptance-spec
title: Acceptance — Clearance state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-CLEARANCE
traces:
  verifies:
  - SL-05
  - AGG-CLEARANCE
  - REQ-GOV-003
  - REQ-GOV-004
---

# Acceptance — Clearance

مولّدة من مصفوفة AGG-CLEARANCE: 7 انتقالاً مسموحاً، 23 رفضاً، 2 انتقالاً نظامياً (SYS).

```gherkin
Feature: Clearance lifecycle (AGG-CLEARANCE)

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
      | Clearance | PENDING_APPROVAL | CMD-CLR-APPROVE | ACTIVE | EVT-CLR-GRANTED | 3 |
      | Clearance | PENDING_APPROVAL | CMD-CLR-REVOKE | REVOKED | EVT-CLR-REVOKED | 3 |
      | Clearance | ACTIVE | CMD-CLR-MODIFY | ACTIVE | EVT-CLR-MODIFIED | 3 |
      | Clearance | ACTIVE | CMD-CLR-SUSPEND | SUSPENDED | EVT-CLR-SUSPENDED | 3 |
      | Clearance | ACTIVE | CMD-CLR-REVOKE | REVOKED | EVT-CLR-REVOKED | 3 |
      | Clearance | SUSPENDED | CMD-CLR-REINSTATE | ACTIVE | EVT-CLR-REINSTATED | 3 |
      | Clearance | SUSPENDED | CMD-CLR-REVOKE | REVOKED | EVT-CLR-REVOKED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Clearance | CMD-CLR-GRANT | PENDING_APPROVAL | EVT-CLR-REQUESTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Clearance | PENDING_APPROVAL | CMD-CLR-GRANT | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | PENDING_APPROVAL | CMD-CLR-MODIFY | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | PENDING_APPROVAL | CMD-CLR-SUSPEND | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | PENDING_APPROVAL | CMD-CLR-REINSTATE | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | ACTIVE | CMD-CLR-GRANT | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | ACTIVE | CMD-CLR-APPROVE | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | ACTIVE | CMD-CLR-REINSTATE | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | SUSPENDED | CMD-CLR-GRANT | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | SUSPENDED | CMD-CLR-APPROVE | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | SUSPENDED | CMD-CLR-MODIFY | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | SUSPENDED | CMD-CLR-SUSPEND | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | EXPIRED | CMD-CLR-GRANT | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | EXPIRED | CMD-CLR-APPROVE | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | EXPIRED | CMD-CLR-MODIFY | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | EXPIRED | CMD-CLR-SUSPEND | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | EXPIRED | CMD-CLR-REINSTATE | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | EXPIRED | CMD-CLR-REVOKE | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | REVOKED | CMD-CLR-GRANT | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | REVOKED | CMD-CLR-APPROVE | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | REVOKED | CMD-CLR-MODIFY | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | REVOKED | CMD-CLR-SUSPEND | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | REVOKED | CMD-CLR-REINSTATE | CLEARANCE_INVALID_STATE_TRANSITION |
      | Clearance | REVOKED | CMD-CLR-REVOKE | CLEARANCE_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Clearance | ACTIVE | valid_to reached | EXPIRED | EVT-CLR-EXPIRED |
      | Clearance | SUSPENDED | valid_to reached | EXPIRED | EVT-CLR-EXPIRED |
```
