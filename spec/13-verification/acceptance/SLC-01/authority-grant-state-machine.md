---
id: TST-AUTHORITY-GRANT-SM
type: acceptance-spec
title: Acceptance — Authority Grant (incl. delegation) state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-AUTHORITY-GRANT
traces:
  verifies:
  - SL-05
  - AGG-AUTHORITY-GRANT
  - REQ-FND-007
  - REQ-FND-008
  - REQ-FND-009
---

# Acceptance — Authority Grant (incl. delegation)

مولّدة من مصفوفة AGG-AUTHORITY-GRANT: 7 انتقالاً مسموحاً، 35 رفضاً، 2 انتقالاً نظامياً (SYS).

```gherkin
Feature: Authority Grant (incl. delegation) lifecycle (AGG-AUTHORITY-GRANT)

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
      | Authority Grant (incl. delegation) | PENDING_APPROVAL | CMD-AUT-APPROVE-GRANT | ACTIVE | EVT-AUT-GRANTED | 3 |
      | Authority Grant (incl. delegation) | PENDING_APPROVAL | CMD-AUT-REJECT-GRANT | REJECTED | EVT-AUT-GRANT-REJECTED | 3 |
      | Authority Grant (incl. delegation) | PENDING_APPROVAL | CMD-AUT-REVOKE | REVOKED | EVT-AUT-REVOKED | 3 |
      | Authority Grant (incl. delegation) | ACTIVE | CMD-AUT-SUSPEND | SUSPENDED | EVT-AUT-SUSPENDED | 3 |
      | Authority Grant (incl. delegation) | ACTIVE | CMD-AUT-REVOKE | REVOKED | EVT-AUT-REVOKED | 3 |
      | Authority Grant (incl. delegation) | SUSPENDED | CMD-AUT-RESUME | ACTIVE | EVT-AUT-RESUMED | 3 |
      | Authority Grant (incl. delegation) | SUSPENDED | CMD-AUT-REVOKE | REVOKED | EVT-AUT-REVOKED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Authority Grant (incl. delegation) | CMD-AUT-GRANT | PENDING_APPROVAL | EVT-AUT-GRANT-REQUESTED |
      | Authority Grant (incl. delegation) | CMD-AUT-DELEGATE | ACTIVE | EVT-AUT-DELEGATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Authority Grant (incl. delegation) | PENDING_APPROVAL | CMD-AUT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | PENDING_APPROVAL | CMD-AUT-DELEGATE | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | PENDING_APPROVAL | CMD-AUT-SUSPEND | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | PENDING_APPROVAL | CMD-AUT-RESUME | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | ACTIVE | CMD-AUT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | ACTIVE | CMD-AUT-APPROVE-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | ACTIVE | CMD-AUT-REJECT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | ACTIVE | CMD-AUT-DELEGATE | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | ACTIVE | CMD-AUT-RESUME | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | SUSPENDED | CMD-AUT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | SUSPENDED | CMD-AUT-APPROVE-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | SUSPENDED | CMD-AUT-REJECT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | SUSPENDED | CMD-AUT-DELEGATE | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | SUSPENDED | CMD-AUT-SUSPEND | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | EXPIRED | CMD-AUT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | EXPIRED | CMD-AUT-APPROVE-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | EXPIRED | CMD-AUT-REJECT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | EXPIRED | CMD-AUT-DELEGATE | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | EXPIRED | CMD-AUT-SUSPEND | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | EXPIRED | CMD-AUT-RESUME | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | EXPIRED | CMD-AUT-REVOKE | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REVOKED | CMD-AUT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REVOKED | CMD-AUT-APPROVE-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REVOKED | CMD-AUT-REJECT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REVOKED | CMD-AUT-DELEGATE | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REVOKED | CMD-AUT-SUSPEND | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REVOKED | CMD-AUT-RESUME | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REVOKED | CMD-AUT-REVOKE | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REJECTED | CMD-AUT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REJECTED | CMD-AUT-APPROVE-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REJECTED | CMD-AUT-REJECT-GRANT | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REJECTED | CMD-AUT-DELEGATE | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REJECTED | CMD-AUT-SUSPEND | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REJECTED | CMD-AUT-RESUME | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |
      | Authority Grant (incl. delegation) | REJECTED | CMD-AUT-REVOKE | AUTHORITY_GRANT_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Authority Grant (incl. delegation) | ACTIVE | valid_to reached | EXPIRED | EVT-AUT-EXPIRED |
      | Authority Grant (incl. delegation) | SUSPENDED | valid_to reached | EXPIRED | EVT-AUT-EXPIRED |
```
