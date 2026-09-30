---
id: TST-SUBSCRIPTION-SM
type: acceptance-spec
title: Acceptance — Subscription state machine
wave: W6
slice: SLC-06
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-SUBSCRIPTION
traces:
  verifies:
  - SL-05
  - AGG-SUBSCRIPTION
  - REQ-COM-001
---

# Acceptance — Subscription

مولّدة من مصفوفة AGG-SUBSCRIPTION: 6 انتقالاً مسموحاً، 9 رفضاً، 2 انتقالاً نظامياً (SYS).

```gherkin
Feature: Subscription lifecycle (AGG-SUBSCRIPTION)

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
      | Subscription | ACTIVE | CMD-SUB-UPDATE-CHANNELS | ACTIVE | EVT-SUB-CHANNELS-UPDATED | 3 |
      | Subscription | ACTIVE | CMD-SUB-PAUSE | PAUSED | EVT-SUB-PAUSED | 3 |
      | Subscription | ACTIVE | CMD-SUB-UNSUBSCRIBE | ENDED | EVT-SUB-ENDED | 3 |
      | Subscription | PAUSED | CMD-SUB-UPDATE-CHANNELS | PAUSED | EVT-SUB-CHANNELS-UPDATED | 3 |
      | Subscription | PAUSED | CMD-SUB-RESUME | ACTIVE | EVT-SUB-RESUMED | 3 |
      | Subscription | PAUSED | CMD-SUB-UNSUBSCRIBE | ENDED | EVT-SUB-ENDED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Subscription | CMD-SUB-SUBSCRIBE | ACTIVE | EVT-SUB-SUBSCRIBED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Subscription | ACTIVE | CMD-SUB-SUBSCRIBE | SUBSCRIPTION_INVALID_STATE_TRANSITION |
      | Subscription | ACTIVE | CMD-SUB-RESUME | SUBSCRIPTION_INVALID_STATE_TRANSITION |
      | Subscription | PAUSED | CMD-SUB-SUBSCRIBE | SUBSCRIPTION_INVALID_STATE_TRANSITION |
      | Subscription | PAUSED | CMD-SUB-PAUSE | SUBSCRIPTION_INVALID_STATE_TRANSITION |
      | Subscription | ENDED | CMD-SUB-SUBSCRIBE | SUBSCRIPTION_INVALID_STATE_TRANSITION |
      | Subscription | ENDED | CMD-SUB-UPDATE-CHANNELS | SUBSCRIPTION_INVALID_STATE_TRANSITION |
      | Subscription | ENDED | CMD-SUB-PAUSE | SUBSCRIPTION_INVALID_STATE_TRANSITION |
      | Subscription | ENDED | CMD-SUB-RESUME | SUBSCRIPTION_INVALID_STATE_TRANSITION |
      | Subscription | ENDED | CMD-SUB-UNSUBSCRIBE | SUBSCRIPTION_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Subscription | ACTIVE | subscriber lost visibility of target | ENDED | EVT-SUB-ENDED |
      | Subscription | PAUSED | subscriber lost visibility of target | ENDED | EVT-SUB-ENDED |
```
