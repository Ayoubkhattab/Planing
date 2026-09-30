---
id: TST-REALWORLD-EVENT-SM
type: acceptance-spec
title: Acceptance — Real-World Event (identity) state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-REALWORLD-EVENT
traces:
  verifies:
  - SL-05
  - AGG-REALWORLD-EVENT
  - REQ-INF-020
---

# Acceptance — Real-World Event (identity)

مولّدة من مصفوفة AGG-REALWORLD-EVENT: 5 انتقالاً مسموحاً، 5 رفضاً.

```gherkin
Feature: Real-World Event (identity) lifecycle (AGG-REALWORLD-EVENT)

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
      | Real-World Event (identity) | ACTIVE | CMD-RWE-CHANGE-TYPE | ACTIVE | EVT-RWE-TYPE-CHANGED | 3 |
      | Real-World Event (identity) | ACTIVE | CMD-RWE-RECLASSIFY | ACTIVE | EVT-RWE-RECLASSIFIED | 3 |
      | Real-World Event (identity) | ACTIVE | CMD-RWE-RETIRE | RETIRED | EVT-RWE-RETIRED | 3 |
      | Real-World Event (identity) | RETIRED | CMD-RWE-RECLASSIFY | RETIRED | EVT-RWE-RECLASSIFIED | 3 |
      | Real-World Event (identity) | RETIRED | CMD-RWE-REINSTATE | ACTIVE | EVT-RWE-REINSTATED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Real-World Event (identity) | CMD-RWE-REGISTER | ACTIVE | EVT-RWE-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Real-World Event (identity) | ACTIVE | CMD-RWE-REGISTER | REALWORLD_EVENT_INVALID_STATE_TRANSITION |
      | Real-World Event (identity) | ACTIVE | CMD-RWE-REINSTATE | REALWORLD_EVENT_INVALID_STATE_TRANSITION |
      | Real-World Event (identity) | RETIRED | CMD-RWE-REGISTER | REALWORLD_EVENT_INVALID_STATE_TRANSITION |
      | Real-World Event (identity) | RETIRED | CMD-RWE-CHANGE-TYPE | REALWORLD_EVENT_INVALID_STATE_TRANSITION |
      | Real-World Event (identity) | RETIRED | CMD-RWE-RETIRE | REALWORLD_EVENT_INVALID_STATE_TRANSITION |
```
