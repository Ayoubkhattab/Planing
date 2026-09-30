---
id: TST-ASSET-RESERVATION-SM
type: acceptance-spec
title: Acceptance — Asset Reservation state machine
wave: W6
slice: SLC-09
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ASSET-RESERVATION
traces:
  verifies:
  - SL-05
  - AGG-ASSET-RESERVATION
  - REQ-RES-014
---

# Acceptance — Asset Reservation

مولّدة من مصفوفة AGG-ASSET-RESERVATION: 4 انتقالاً مسموحاً، 16 رفضاً، 2 انتقالاً نظامياً (SYS).

```gherkin
Feature: Asset Reservation lifecycle (AGG-ASSET-RESERVATION)

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
      | Asset Reservation | HELD | CMD-RSV-CONFIRM | CONFIRMED | EVT-RSV-CONFIRMED | 3 |
      | Asset Reservation | HELD | CMD-RSV-CANCEL | CANCELLED | EVT-RSV-CANCELLED | 3 |
      | Asset Reservation | CONFIRMED | CMD-RSV-RELEASE | RELEASED | EVT-RSV-RELEASED | 3 |
      | Asset Reservation | CONFIRMED | CMD-RSV-CANCEL | CANCELLED | EVT-RSV-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Asset Reservation | CMD-RSV-HOLD | HELD | EVT-RSV-HELD |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Asset Reservation | HELD | CMD-RSV-HOLD | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | HELD | CMD-RSV-RELEASE | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | CONFIRMED | CMD-RSV-HOLD | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | CONFIRMED | CMD-RSV-CONFIRM | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | RELEASED | CMD-RSV-HOLD | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | RELEASED | CMD-RSV-CONFIRM | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | RELEASED | CMD-RSV-RELEASE | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | RELEASED | CMD-RSV-CANCEL | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | EXPIRED | CMD-RSV-HOLD | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | EXPIRED | CMD-RSV-CONFIRM | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | EXPIRED | CMD-RSV-RELEASE | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | EXPIRED | CMD-RSV-CANCEL | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | CANCELLED | CMD-RSV-HOLD | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | CANCELLED | CMD-RSV-CONFIRM | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | CANCELLED | CMD-RSV-RELEASE | ASSET_RESERVATION_INVALID_STATE_TRANSITION |
      | Asset Reservation | CANCELLED | CMD-RSV-CANCEL | ASSET_RESERVATION_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Asset Reservation | HELD | hold expiry (24 h) reached | EXPIRED | EVT-RSV-EXPIRED |
      | Asset Reservation | CONFIRMED | linked task or plan terminal | RELEASED | EVT-RSV-RELEASED |
```
