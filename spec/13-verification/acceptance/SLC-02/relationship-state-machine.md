---
id: TST-RELATIONSHIP-SM
type: acceptance-spec
title: Acceptance — Relationship (identity) state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-RELATIONSHIP
traces:
  verifies:
  - SL-05
  - AGG-RELATIONSHIP
  - REQ-INF-027
---

# Acceptance — Relationship (identity)

مولّدة من مصفوفة AGG-RELATIONSHIP: 4 انتقالاً مسموحاً، 4 رفضاً.

```gherkin
Feature: Relationship (identity) lifecycle (AGG-RELATIONSHIP)

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
      | Relationship (identity) | ACTIVE | CMD-REL-RECLASSIFY | ACTIVE | EVT-REL-RECLASSIFIED | 3 |
      | Relationship (identity) | ACTIVE | CMD-REL-RETIRE | RETIRED | EVT-REL-RETIRED | 3 |
      | Relationship (identity) | RETIRED | CMD-REL-RECLASSIFY | RETIRED | EVT-REL-RECLASSIFIED | 3 |
      | Relationship (identity) | RETIRED | CMD-REL-REINSTATE | ACTIVE | EVT-REL-REINSTATED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Relationship (identity) | CMD-REL-REGISTER | ACTIVE | EVT-REL-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Relationship (identity) | ACTIVE | CMD-REL-REGISTER | RELATIONSHIP_INVALID_STATE_TRANSITION |
      | Relationship (identity) | ACTIVE | CMD-REL-REINSTATE | RELATIONSHIP_INVALID_STATE_TRANSITION |
      | Relationship (identity) | RETIRED | CMD-REL-REGISTER | RELATIONSHIP_INVALID_STATE_TRANSITION |
      | Relationship (identity) | RETIRED | CMD-REL-RETIRE | RELATIONSHIP_INVALID_STATE_TRANSITION |
```
