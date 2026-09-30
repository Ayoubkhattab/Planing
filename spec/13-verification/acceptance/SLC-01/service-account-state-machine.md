---
id: TST-SERVICE-ACCOUNT-SM
type: acceptance-spec
title: Acceptance — Service Account state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-SERVICE-ACCOUNT
traces:
  verifies:
  - SL-05
  - AGG-SERVICE-ACCOUNT
  - REQ-FND-006
---

# Acceptance — Service Account

مولّدة من مصفوفة AGG-SERVICE-ACCOUNT: 4 انتقالاً مسموحاً، 11 رفضاً.

```gherkin
Feature: Service Account lifecycle (AGG-SERVICE-ACCOUNT)

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
      | Service Account | ACTIVE | CMD-SVC-ROTATE-CREDENTIAL | ACTIVE | EVT-SVC-CREDENTIAL-ROTATED | 3 |
      | Service Account | ACTIVE | CMD-SVC-DISABLE | DISABLED | EVT-SVC-DISABLED | 3 |
      | Service Account | DISABLED | CMD-SVC-ENABLE | ACTIVE | EVT-SVC-ENABLED | 3 |
      | Service Account | DISABLED | CMD-SVC-CLOSE | CLOSED | EVT-SVC-CLOSED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Service Account | CMD-SVC-CREATE | ACTIVE | EVT-SVC-CREATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Service Account | ACTIVE | CMD-SVC-CREATE | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
      | Service Account | ACTIVE | CMD-SVC-ENABLE | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
      | Service Account | ACTIVE | CMD-SVC-CLOSE | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
      | Service Account | DISABLED | CMD-SVC-CREATE | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
      | Service Account | DISABLED | CMD-SVC-ROTATE-CREDENTIAL | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
      | Service Account | DISABLED | CMD-SVC-DISABLE | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
      | Service Account | CLOSED | CMD-SVC-CREATE | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
      | Service Account | CLOSED | CMD-SVC-ROTATE-CREDENTIAL | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
      | Service Account | CLOSED | CMD-SVC-DISABLE | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
      | Service Account | CLOSED | CMD-SVC-ENABLE | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
      | Service Account | CLOSED | CMD-SVC-CLOSE | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
```
