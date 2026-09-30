---
id: TST-INTEGRATION-CONNECTION-SM
type: acceptance-spec
title: Acceptance — Integration Connection state machine
wave: W6
slice: SLC-16
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-INTEGRATION-CONNECTION
traces:
  verifies:
  - SL-05
  - AGG-INTEGRATION-CONNECTION
  - REQ-INT-001
---

# Acceptance — Integration Connection

مولّدة من مصفوفة AGG-INTEGRATION-CONNECTION: 8 انتقالاً مسموحاً، 34 رفضاً.

```gherkin
Feature: Integration Connection lifecycle (AGG-INTEGRATION-CONNECTION)

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
      | Integration Connection | DRAFT | CMD-CON-TEST | TESTING | EVT-CON-TEST-STARTED | 3 |
      | Integration Connection | DRAFT | CMD-CON-RETIRE | RETIRED | EVT-CON-RETIRED | 3 |
      | Integration Connection | TESTING | CMD-CON-ACTIVATE | ACTIVE | EVT-CON-ACTIVATED | 3 |
      | Integration Connection | TESTING | CMD-CON-FAIL-TEST | DRAFT | EVT-CON-TEST-FAILED | 3 |
      | Integration Connection | ACTIVE | CMD-CON-SUSPEND | SUSPENDED | EVT-CON-SUSPENDED | 3 |
      | Integration Connection | DEGRADED | CMD-CON-SUSPEND | SUSPENDED | EVT-CON-SUSPENDED | 3 |
      | Integration Connection | SUSPENDED | CMD-CON-RESUME | ACTIVE | EVT-CON-RESUMED | 3 |
      | Integration Connection | SUSPENDED | CMD-CON-RETIRE | RETIRED | EVT-CON-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Integration Connection | CMD-CON-REGISTER | DRAFT | EVT-CON-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Integration Connection | DRAFT | CMD-CON-REGISTER | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | DRAFT | CMD-CON-ACTIVATE | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | DRAFT | CMD-CON-FAIL-TEST | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | DRAFT | CMD-CON-SUSPEND | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | DRAFT | CMD-CON-RESUME | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | TESTING | CMD-CON-REGISTER | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | TESTING | CMD-CON-TEST | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | TESTING | CMD-CON-SUSPEND | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | TESTING | CMD-CON-RESUME | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | TESTING | CMD-CON-RETIRE | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | ACTIVE | CMD-CON-REGISTER | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | ACTIVE | CMD-CON-TEST | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | ACTIVE | CMD-CON-ACTIVATE | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | ACTIVE | CMD-CON-FAIL-TEST | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | ACTIVE | CMD-CON-RESUME | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | ACTIVE | CMD-CON-RETIRE | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | DEGRADED | CMD-CON-REGISTER | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | DEGRADED | CMD-CON-TEST | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | DEGRADED | CMD-CON-ACTIVATE | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | DEGRADED | CMD-CON-FAIL-TEST | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | DEGRADED | CMD-CON-RESUME | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | DEGRADED | CMD-CON-RETIRE | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | SUSPENDED | CMD-CON-REGISTER | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | SUSPENDED | CMD-CON-TEST | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | SUSPENDED | CMD-CON-ACTIVATE | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | SUSPENDED | CMD-CON-FAIL-TEST | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | SUSPENDED | CMD-CON-SUSPEND | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | RETIRED | CMD-CON-REGISTER | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | RETIRED | CMD-CON-TEST | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | RETIRED | CMD-CON-ACTIVATE | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | RETIRED | CMD-CON-FAIL-TEST | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | RETIRED | CMD-CON-SUSPEND | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | RETIRED | CMD-CON-RESUME | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
      | Integration Connection | RETIRED | CMD-CON-RETIRE | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
```
