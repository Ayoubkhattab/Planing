---
id: TST-ENTITY-SM
type: acceptance-spec
title: Acceptance — Entity (identity) state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ENTITY
traces:
  verifies:
  - SL-05
  - AGG-ENTITY
  - REQ-INF-020
  - REQ-INF-021
  - REQ-INF-036
---

# Acceptance — Entity (identity)

مولّدة من مصفوفة AGG-ENTITY: 5 انتقالاً مسموحاً، 5 رفضاً.

```gherkin
Feature: Entity (identity) lifecycle (AGG-ENTITY)

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
      | Entity (identity) | ACTIVE | CMD-ENT-CHANGE-TYPE | ACTIVE | EVT-ENT-TYPE-CHANGED | 3 |
      | Entity (identity) | ACTIVE | CMD-ENT-RECLASSIFY | ACTIVE | EVT-ENT-RECLASSIFIED | 3 |
      | Entity (identity) | ACTIVE | CMD-ENT-RETIRE | RETIRED | EVT-ENT-RETIRED | 3 |
      | Entity (identity) | RETIRED | CMD-ENT-RECLASSIFY | RETIRED | EVT-ENT-RECLASSIFIED | 3 |
      | Entity (identity) | RETIRED | CMD-ENT-REINSTATE | ACTIVE | EVT-ENT-REINSTATED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Entity (identity) | CMD-ENT-REGISTER | ACTIVE | EVT-ENT-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Entity (identity) | ACTIVE | CMD-ENT-REGISTER | ENTITY_INVALID_STATE_TRANSITION |
      | Entity (identity) | ACTIVE | CMD-ENT-REINSTATE | ENTITY_INVALID_STATE_TRANSITION |
      | Entity (identity) | RETIRED | CMD-ENT-REGISTER | ENTITY_INVALID_STATE_TRANSITION |
      | Entity (identity) | RETIRED | CMD-ENT-CHANGE-TYPE | ENTITY_INVALID_STATE_TRANSITION |
      | Entity (identity) | RETIRED | CMD-ENT-RETIRE | ENTITY_INVALID_STATE_TRANSITION |
```
