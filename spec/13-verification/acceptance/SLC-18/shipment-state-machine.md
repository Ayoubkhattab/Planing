---
id: TST-SHIPMENT-SM
type: acceptance-spec
title: Acceptance — Shipment state machine
wave: W6
slice: SLC-18
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
generated_from: AGG-SHIPMENT
traces:
  verifies:
  - SL-05
  - AGG-SHIPMENT
  - REQ-LOG-004
  - REQ-LOG-005
  - REQ-LOG-006
  - REQ-LOG-007
  - REQ-LOG-009
---

# Acceptance — Shipment

مولّدة من مصفوفة AGG-SHIPMENT: 6 انتقالاً مسموحاً، 8 رفضاً.

```gherkin
Feature: Shipment lifecycle (AGG-SHIPMENT)

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
      | Shipment | PLANNED | CMD-SHP-DEPART | IN_TRANSIT | EVT-SHP-DEPARTED | 3 |
      | Shipment | PLANNED | CMD-SHP-CANCEL | CANCELLED | EVT-SHP-CANCELLED | 3 |
      | Shipment | IN_TRANSIT | CMD-SHP-RECORD-CHECKPOINT | IN_TRANSIT | EVT-SHP-CHECKPOINT-RECORDED | 3 |
      | Shipment | IN_TRANSIT | CMD-SHP-DELIVER | DELIVERED | EVT-SHP-DELIVERED | 3 |
      | Shipment | IN_TRANSIT | CMD-SHP-REPORT-DAMAGE | DAMAGED | EVT-SHP-DAMAGED | 3 |
      | Shipment | IN_TRANSIT | CMD-SHP-REPORT-LOST | LOST | EVT-SHP-LOST | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Shipment | CMD-SHP-PLAN | PLANNED | EVT-SHP-PLANNED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Shipment | PLANNED | CMD-SHP-PLAN | SHIPMENT_INVALID_STATE_TRANSITION |
      | Shipment | PLANNED | CMD-SHP-RECORD-CHECKPOINT | SHIPMENT_INVALID_STATE_TRANSITION |
      | Shipment | PLANNED | CMD-SHP-DELIVER | SHIPMENT_INVALID_STATE_TRANSITION |
      | Shipment | PLANNED | CMD-SHP-REPORT-DAMAGE | SHIPMENT_INVALID_STATE_TRANSITION |
      | Shipment | PLANNED | CMD-SHP-REPORT-LOST | SHIPMENT_INVALID_STATE_TRANSITION |
      | Shipment | IN_TRANSIT | CMD-SHP-PLAN | SHIPMENT_INVALID_STATE_TRANSITION |
      | Shipment | IN_TRANSIT | CMD-SHP-DEPART | SHIPMENT_INVALID_STATE_TRANSITION |
      | Shipment | IN_TRANSIT | CMD-SHP-CANCEL | SHIPMENT_INVALID_STATE_TRANSITION |
```
