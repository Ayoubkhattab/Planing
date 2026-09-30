---
id: TST-RESOURCE-POOL-SM
type: acceptance-spec
title: Acceptance — Resource Pool state machine
wave: W6
slice: SLC-09
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-RESOURCE-POOL
traces:
  verifies:
  - SL-05
  - AGG-RESOURCE-POOL
  - REQ-RES-006
---

# Acceptance — Resource Pool

مولّدة من مصفوفة AGG-RESOURCE-POOL: 6 انتقالاً مسموحاً، 9 رفضاً.

```gherkin
Feature: Resource Pool lifecycle (AGG-RESOURCE-POOL)

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
      | Resource Pool | ACTIVE | CMD-RPL-ADJUST-CAPACITY | ACTIVE | EVT-RPL-CAPACITY-ADJUSTED | 3 |
      | Resource Pool | ACTIVE | CMD-RPL-SUSPEND | SUSPENDED | EVT-RPL-SUSPENDED | 3 |
      | Resource Pool | ACTIVE | CMD-RPL-CLOSE | CLOSED | EVT-RPL-CLOSED | 3 |
      | Resource Pool | SUSPENDED | CMD-RPL-ADJUST-CAPACITY | SUSPENDED | EVT-RPL-CAPACITY-ADJUSTED | 3 |
      | Resource Pool | SUSPENDED | CMD-RPL-RESUME | ACTIVE | EVT-RPL-RESUMED | 3 |
      | Resource Pool | SUSPENDED | CMD-RPL-CLOSE | CLOSED | EVT-RPL-CLOSED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Resource Pool | CMD-RPL-CREATE | ACTIVE | EVT-RPL-CREATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Resource Pool | ACTIVE | CMD-RPL-CREATE | RESOURCE_POOL_INVALID_STATE_TRANSITION |
      | Resource Pool | ACTIVE | CMD-RPL-RESUME | RESOURCE_POOL_INVALID_STATE_TRANSITION |
      | Resource Pool | SUSPENDED | CMD-RPL-CREATE | RESOURCE_POOL_INVALID_STATE_TRANSITION |
      | Resource Pool | SUSPENDED | CMD-RPL-SUSPEND | RESOURCE_POOL_INVALID_STATE_TRANSITION |
      | Resource Pool | CLOSED | CMD-RPL-CREATE | RESOURCE_POOL_INVALID_STATE_TRANSITION |
      | Resource Pool | CLOSED | CMD-RPL-ADJUST-CAPACITY | RESOURCE_POOL_INVALID_STATE_TRANSITION |
      | Resource Pool | CLOSED | CMD-RPL-SUSPEND | RESOURCE_POOL_INVALID_STATE_TRANSITION |
      | Resource Pool | CLOSED | CMD-RPL-RESUME | RESOURCE_POOL_INVALID_STATE_TRANSITION |
      | Resource Pool | CLOSED | CMD-RPL-CLOSE | RESOURCE_POOL_INVALID_STATE_TRANSITION |
```
