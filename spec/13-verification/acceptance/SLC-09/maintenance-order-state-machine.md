---
id: TST-MAINTENANCE-ORDER-SM
type: acceptance-spec
title: Acceptance — Maintenance Order state machine
wave: W6
slice: SLC-09
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-MAINTENANCE-ORDER
traces:
  verifies:
  - SL-05
  - AGG-MAINTENANCE-ORDER
  - REQ-RES-004
---

# Acceptance — Maintenance Order

مولّدة من مصفوفة AGG-MAINTENANCE-ORDER: 4 انتقالاً مسموحاً، 16 رفضاً.

```gherkin
Feature: Maintenance Order lifecycle (AGG-MAINTENANCE-ORDER)

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
      | Maintenance Order | PLANNED | CMD-MNT-RESCHEDULE | PLANNED | EVT-MNT-RESCHEDULED | 3 |
      | Maintenance Order | PLANNED | CMD-MNT-START | IN_PROGRESS | EVT-MNT-STARTED | 3 |
      | Maintenance Order | PLANNED | CMD-MNT-CANCEL | CANCELLED | EVT-MNT-CANCELLED | 3 |
      | Maintenance Order | IN_PROGRESS | CMD-MNT-COMPLETE | COMPLETED | EVT-MNT-COMPLETED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Maintenance Order | CMD-MNT-PLAN | PLANNED | EVT-MNT-PLANNED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Maintenance Order | PLANNED | CMD-MNT-PLAN | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | PLANNED | CMD-MNT-COMPLETE | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | IN_PROGRESS | CMD-MNT-PLAN | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | IN_PROGRESS | CMD-MNT-RESCHEDULE | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | IN_PROGRESS | CMD-MNT-START | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | IN_PROGRESS | CMD-MNT-CANCEL | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | COMPLETED | CMD-MNT-PLAN | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | COMPLETED | CMD-MNT-RESCHEDULE | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | COMPLETED | CMD-MNT-START | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | COMPLETED | CMD-MNT-COMPLETE | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | COMPLETED | CMD-MNT-CANCEL | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | CANCELLED | CMD-MNT-PLAN | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | CANCELLED | CMD-MNT-RESCHEDULE | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | CANCELLED | CMD-MNT-START | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | CANCELLED | CMD-MNT-COMPLETE | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
      | Maintenance Order | CANCELLED | CMD-MNT-CANCEL | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |
```
