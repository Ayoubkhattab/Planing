---
id: TST-ROLE-SM
type: acceptance-spec
title: Acceptance — Role state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ROLE
traces:
  verifies:
  - SL-05
  - AGG-ROLE
  - REQ-FND-014
---

# Acceptance — Role

مولّدة من مصفوفة AGG-ROLE: 4 انتقالاً مسموحاً، 8 رفضاً.

```gherkin
Feature: Role lifecycle (AGG-ROLE)

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
      | Role | DRAFT | CMD-ROL-SET-PERMISSIONS | DRAFT | EVT-ROL-PERMISSIONS-CHANGED | 3 |
      | Role | DRAFT | CMD-ROL-ACTIVATE | ACTIVE | EVT-ROL-ACTIVATED | 3 |
      | Role | ACTIVE | CMD-ROL-SET-PERMISSIONS | ACTIVE | EVT-ROL-PERMISSIONS-CHANGED | 3 |
      | Role | ACTIVE | CMD-ROL-RETIRE | RETIRED | EVT-ROL-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Role | CMD-ROL-DEFINE | DRAFT | EVT-ROL-DEFINED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Role | DRAFT | CMD-ROL-DEFINE | ROLE_INVALID_STATE_TRANSITION |
      | Role | DRAFT | CMD-ROL-RETIRE | ROLE_INVALID_STATE_TRANSITION |
      | Role | ACTIVE | CMD-ROL-DEFINE | ROLE_INVALID_STATE_TRANSITION |
      | Role | ACTIVE | CMD-ROL-ACTIVATE | ROLE_INVALID_STATE_TRANSITION |
      | Role | RETIRED | CMD-ROL-DEFINE | ROLE_INVALID_STATE_TRANSITION |
      | Role | RETIRED | CMD-ROL-SET-PERMISSIONS | ROLE_INVALID_STATE_TRANSITION |
      | Role | RETIRED | CMD-ROL-ACTIVATE | ROLE_INVALID_STATE_TRANSITION |
      | Role | RETIRED | CMD-ROL-RETIRE | ROLE_INVALID_STATE_TRANSITION |
```
