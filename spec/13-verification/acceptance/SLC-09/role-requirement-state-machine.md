---
id: TST-ROLE-REQUIREMENT-SM
type: acceptance-spec
title: Acceptance — Role Requirement state machine
wave: W6
slice: SLC-09
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ROLE-REQUIREMENT
traces:
  verifies:
  - SL-05
  - AGG-ROLE-REQUIREMENT
  - REQ-RES-013
---

# Acceptance — Role Requirement

مولّدة من مصفوفة AGG-ROLE-REQUIREMENT: 4 انتقالاً مسموحاً، 8 رفضاً.

```gherkin
Feature: Role Requirement lifecycle (AGG-ROLE-REQUIREMENT)

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
      | Role Requirement | DRAFT | CMD-RRQ-EDIT | DRAFT | EVT-RRQ-EDITED | 3 |
      | Role Requirement | DRAFT | CMD-RRQ-ACTIVATE | ACTIVE | EVT-RRQ-ACTIVATED | 3 |
      | Role Requirement | ACTIVE | CMD-RRQ-EDIT | ACTIVE | EVT-RRQ-EDITED | 3 |
      | Role Requirement | ACTIVE | CMD-RRQ-RETIRE | RETIRED | EVT-RRQ-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Role Requirement | CMD-RRQ-DEFINE | DRAFT | EVT-RRQ-DEFINED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Role Requirement | DRAFT | CMD-RRQ-DEFINE | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Role Requirement | DRAFT | CMD-RRQ-RETIRE | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Role Requirement | ACTIVE | CMD-RRQ-DEFINE | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Role Requirement | ACTIVE | CMD-RRQ-ACTIVATE | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Role Requirement | RETIRED | CMD-RRQ-DEFINE | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Role Requirement | RETIRED | CMD-RRQ-EDIT | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Role Requirement | RETIRED | CMD-RRQ-ACTIVATE | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Role Requirement | RETIRED | CMD-RRQ-RETIRE | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |
```
