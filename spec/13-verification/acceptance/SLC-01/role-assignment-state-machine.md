---
id: TST-ROLE-ASSIGNMENT-SM
type: acceptance-spec
title: Acceptance — Role Assignment state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ROLE-ASSIGNMENT
traces:
  verifies:
  - SL-05
  - AGG-ROLE-ASSIGNMENT
  - REQ-FND-011
  - REQ-OPS-005
  - REQ-OPS-009
---

# Acceptance — Role Assignment

مولّدة من مصفوفة AGG-ROLE-ASSIGNMENT: 1 انتقالاً مسموحاً، 5 رفضاً.

```gherkin
Feature: Role Assignment lifecycle (AGG-ROLE-ASSIGNMENT)

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
      | Role Assignment | ACTIVE | CMD-RAS-REVOKE | REVOKED | EVT-RAS-REVOKED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Role Assignment | CMD-RAS-ASSIGN | ACTIVE | EVT-RAS-ASSIGNED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Role Assignment | ACTIVE | CMD-RAS-ASSIGN | ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION |
      | Role Assignment | EXPIRED | CMD-RAS-ASSIGN | ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION |
      | Role Assignment | EXPIRED | CMD-RAS-REVOKE | ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION |
      | Role Assignment | REVOKED | CMD-RAS-ASSIGN | ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION |
      | Role Assignment | REVOKED | CMD-RAS-REVOKE | ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION |
```
