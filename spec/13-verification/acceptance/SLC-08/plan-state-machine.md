---
id: TST-PLAN-SM
type: acceptance-spec
title: Acceptance — Plan (identity) state machine
wave: W6
slice: SLC-08
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-PLAN
traces:
  verifies:
  - SL-05
  - AGG-PLAN
  - REQ-OPS-001
  - REQ-OPS-002
  - REQ-OPS-003
---

# Acceptance — Plan (identity)

مولّدة من مصفوفة AGG-PLAN: 10 انتقالاً مسموحاً، 32 رفضاً، 3 انتقالاً نظامياً (SYS).

```gherkin
Feature: Plan (identity) lifecycle (AGG-PLAN)

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
      | Plan (identity) | DRAFT | CMD-PLN-CANCEL | CANCELLED | EVT-PLN-CANCELLED | 3 |
      | Plan (identity) | DRAFT | CMD-PLN-RECLASSIFY | DRAFT | EVT-PLN-RECLASSIFIED | 3 |
      | Plan (identity) | ACTIVE | CMD-PLN-SUSPEND | SUSPENDED | EVT-PLN-SUSPENDED | 3 |
      | Plan (identity) | ACTIVE | CMD-PLN-COMPLETE | COMPLETED | EVT-PLN-COMPLETED | 3 |
      | Plan (identity) | ACTIVE | CMD-PLN-CANCEL | CANCELLED | EVT-PLN-CANCELLED | 3 |
      | Plan (identity) | ACTIVE | CMD-PLN-RECLASSIFY | ACTIVE | EVT-PLN-RECLASSIFIED | 3 |
      | Plan (identity) | SUSPENDED | CMD-PLN-RESUME | ACTIVE | EVT-PLN-RESUMED | 3 |
      | Plan (identity) | SUSPENDED | CMD-PLN-CANCEL | CANCELLED | EVT-PLN-CANCELLED | 3 |
      | Plan (identity) | SUSPENDED | CMD-PLN-RECLASSIFY | SUSPENDED | EVT-PLN-RECLASSIFIED | 3 |
      | Plan (identity) | COMPLETED | CMD-PLN-CLOSE | CLOSED | EVT-PLN-CLOSED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Plan (identity) | CMD-PLN-CREATE | DRAFT | EVT-PLN-CREATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Plan (identity) | DRAFT | CMD-PLN-CREATE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | DRAFT | CMD-PLN-SUSPEND | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | DRAFT | CMD-PLN-RESUME | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | DRAFT | CMD-PLN-COMPLETE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | DRAFT | CMD-PLN-CLOSE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | ACTIVE | CMD-PLN-CREATE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | ACTIVE | CMD-PLN-RESUME | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | ACTIVE | CMD-PLN-CLOSE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | SUSPENDED | CMD-PLN-CREATE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | SUSPENDED | CMD-PLN-SUSPEND | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | SUSPENDED | CMD-PLN-COMPLETE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | SUSPENDED | CMD-PLN-CLOSE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | COMPLETED | CMD-PLN-CREATE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | COMPLETED | CMD-PLN-SUSPEND | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | COMPLETED | CMD-PLN-RESUME | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | COMPLETED | CMD-PLN-COMPLETE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | COMPLETED | CMD-PLN-CANCEL | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | COMPLETED | CMD-PLN-RECLASSIFY | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CLOSED | CMD-PLN-CREATE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CLOSED | CMD-PLN-SUSPEND | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CLOSED | CMD-PLN-RESUME | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CLOSED | CMD-PLN-COMPLETE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CLOSED | CMD-PLN-CLOSE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CLOSED | CMD-PLN-CANCEL | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CLOSED | CMD-PLN-RECLASSIFY | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CANCELLED | CMD-PLN-CREATE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CANCELLED | CMD-PLN-SUSPEND | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CANCELLED | CMD-PLN-RESUME | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CANCELLED | CMD-PLN-COMPLETE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CANCELLED | CMD-PLN-CLOSE | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CANCELLED | CMD-PLN-CANCEL | PLAN_INVALID_STATE_TRANSITION |
      | Plan (identity) | CANCELLED | CMD-PLN-RECLASSIFY | PLAN_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Plan (identity) | DRAFT | first version baselined | ACTIVE | EVT-PLN-ACTIVATED |
      | Plan (identity) | ACTIVE | implemented decision annulled or superseded | ACTIVE | EVT-PLN-REVIEW-FLAGGED |
      | Plan (identity) | SUSPENDED | implemented decision annulled or superseded | SUSPENDED | EVT-PLN-REVIEW-FLAGGED |
```
