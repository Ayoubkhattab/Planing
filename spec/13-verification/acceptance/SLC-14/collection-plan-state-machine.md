---
id: TST-COLLECTION-PLAN-SM
type: acceptance-spec
title: Acceptance — Collection Plan state machine
wave: W6
slice: SLC-14
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-COLLECTION-PLAN
traces:
  verifies:
  - SL-05
  - AGG-COLLECTION-PLAN
  - REQ-COL-002
---

# Acceptance — Collection Plan

مولّدة من مصفوفة AGG-COLLECTION-PLAN: 7 انتقالاً مسموحاً، 17 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: Collection Plan lifecycle (AGG-COLLECTION-PLAN)

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
      | Collection Plan | DRAFT | CMD-CPL-ADD-ACTIVITY | DRAFT | EVT-CPL-ACTIVITY-ADDED | 3 |
      | Collection Plan | DRAFT | CMD-CPL-REMOVE-ACTIVITY | DRAFT | EVT-CPL-ACTIVITY-REMOVED | 3 |
      | Collection Plan | DRAFT | CMD-CPL-ACTIVATE | ACTIVE | EVT-CPL-ACTIVATED | 3 |
      | Collection Plan | DRAFT | CMD-CPL-CANCEL | CANCELLED | EVT-CPL-CANCELLED | 3 |
      | Collection Plan | ACTIVE | CMD-CPL-ADD-ACTIVITY | ACTIVE | EVT-CPL-ACTIVITY-ADDED | 3 |
      | Collection Plan | ACTIVE | CMD-CPL-COMPLETE | COMPLETED | EVT-CPL-COMPLETED | 3 |
      | Collection Plan | ACTIVE | CMD-CPL-CANCEL | CANCELLED | EVT-CPL-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Collection Plan | CMD-CPL-CREATE | DRAFT | EVT-CPL-CREATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Collection Plan | DRAFT | CMD-CPL-CREATE | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | DRAFT | CMD-CPL-COMPLETE | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | ACTIVE | CMD-CPL-CREATE | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | ACTIVE | CMD-CPL-REMOVE-ACTIVITY | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | ACTIVE | CMD-CPL-ACTIVATE | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | COMPLETED | CMD-CPL-CREATE | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | COMPLETED | CMD-CPL-ADD-ACTIVITY | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | COMPLETED | CMD-CPL-REMOVE-ACTIVITY | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | COMPLETED | CMD-CPL-ACTIVATE | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | COMPLETED | CMD-CPL-COMPLETE | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | COMPLETED | CMD-CPL-CANCEL | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | CANCELLED | CMD-CPL-CREATE | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | CANCELLED | CMD-CPL-ADD-ACTIVITY | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | CANCELLED | CMD-CPL-REMOVE-ACTIVITY | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | CANCELLED | CMD-CPL-ACTIVATE | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | CANCELLED | CMD-CPL-COMPLETE | COLLECTION_PLAN_INVALID_STATE_TRANSITION |
      | Collection Plan | CANCELLED | CMD-CPL-CANCEL | COLLECTION_PLAN_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Collection Plan | ACTIVE | all activity tasks terminal | COMPLETED | EVT-CPL-COMPLETED |
```
