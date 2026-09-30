---
id: TST-ADAPTER-SM
type: acceptance-spec
title: Acceptance — Adapter state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ADAPTER
traces:
  verifies:
  - SL-05
  - AGG-ADAPTER
  - REQ-INF-005
  - REQ-INF-008
  - REQ-INF-009
---

# Acceptance — Adapter

مولّدة من مصفوفة AGG-ADAPTER: 8 انتقالاً مسموحاً، 16 رفضاً.

```gherkin
Feature: Adapter lifecycle (AGG-ADAPTER)

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
      | Adapter | DRAFT | CMD-ADP-UPDATE-MAPPING | DRAFT | EVT-ADP-MAPPING-UPDATED | 3 |
      | Adapter | DRAFT | CMD-ADP-ACTIVATE | ACTIVE | EVT-ADP-ACTIVATED | 3 |
      | Adapter | DRAFT | CMD-ADP-RETIRE | RETIRED | EVT-ADP-RETIRED | 3 |
      | Adapter | ACTIVE | CMD-ADP-UPDATE-MAPPING | ACTIVE | EVT-ADP-MAPPING-UPDATED | 3 |
      | Adapter | ACTIVE | CMD-ADP-SUSPEND | SUSPENDED | EVT-ADP-SUSPENDED | 3 |
      | Adapter | ACTIVE | CMD-ADP-RETIRE | RETIRED | EVT-ADP-RETIRED | 3 |
      | Adapter | SUSPENDED | CMD-ADP-RESUME | ACTIVE | EVT-ADP-RESUMED | 3 |
      | Adapter | SUSPENDED | CMD-ADP-RETIRE | RETIRED | EVT-ADP-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Adapter | CMD-ADP-REGISTER | DRAFT | EVT-ADP-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Adapter | DRAFT | CMD-ADP-REGISTER | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | DRAFT | CMD-ADP-SUSPEND | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | DRAFT | CMD-ADP-RESUME | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | ACTIVE | CMD-ADP-REGISTER | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | ACTIVE | CMD-ADP-ACTIVATE | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | ACTIVE | CMD-ADP-RESUME | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | SUSPENDED | CMD-ADP-REGISTER | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | SUSPENDED | CMD-ADP-UPDATE-MAPPING | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | SUSPENDED | CMD-ADP-ACTIVATE | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | SUSPENDED | CMD-ADP-SUSPEND | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | RETIRED | CMD-ADP-REGISTER | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | RETIRED | CMD-ADP-UPDATE-MAPPING | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | RETIRED | CMD-ADP-ACTIVATE | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | RETIRED | CMD-ADP-SUSPEND | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | RETIRED | CMD-ADP-RESUME | ADAPTER_INVALID_STATE_TRANSITION |
      | Adapter | RETIRED | CMD-ADP-RETIRE | ADAPTER_INVALID_STATE_TRANSITION |
```
