---
id: TST-LOGISTICS-REQUEST-SM
type: acceptance-spec
title: Acceptance — Logistics Request state machine
wave: W6
slice: SLC-18
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
generated_from: AGG-LOGISTICS-REQUEST
traces:
  verifies:
  - SL-05
  - AGG-LOGISTICS-REQUEST
  - REQ-LOG-001
  - REQ-LOG-002
  - REQ-LOG-003
  - REQ-LOG-008
  - REQ-LOG-009
  - REQ-LOG-013
  - REQ-LOG-014
---

# Acceptance — Logistics Request

مولّدة من مصفوفة AGG-LOGISTICS-REQUEST: 4 انتقالاً مسموحاً، 8 رفضاً.

```gherkin
Feature: Logistics Request lifecycle (AGG-LOGISTICS-REQUEST)

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
      | Logistics Request | REQUESTED | CMD-LGR-CANCEL | CANCELLED | EVT-LGR-CANCELLED | 3 |
      | Logistics Request | PENDING_APPROVAL | CMD-LGR-CANCEL | CANCELLED | EVT-LGR-CANCELLED | 3 |
      | Logistics Request | APPROVED | CMD-LGR-DISPATCH | IN_TRANSIT | EVT-LGR-DISPATCHED | 3 |
      | Logistics Request | APPROVED | CMD-LGR-CANCEL | CANCELLED | EVT-LGR-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Logistics Request | CMD-LGR-REQUEST | REQUESTED | EVT-LGR-REQUESTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Logistics Request | REQUESTED | CMD-LGR-REQUEST | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
      | Logistics Request | REQUESTED | CMD-LGR-DISPATCH | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
      | Logistics Request | PENDING_APPROVAL | CMD-LGR-REQUEST | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
      | Logistics Request | PENDING_APPROVAL | CMD-LGR-DISPATCH | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
      | Logistics Request | APPROVED | CMD-LGR-REQUEST | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
      | Logistics Request | IN_TRANSIT | CMD-LGR-REQUEST | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
      | Logistics Request | IN_TRANSIT | CMD-LGR-DISPATCH | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
      | Logistics Request | IN_TRANSIT | CMD-LGR-CANCEL | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
```
