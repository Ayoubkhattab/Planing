---
id: TST-AI-ROUTING-SM
type: acceptance-spec
title: Acceptance — AI Routing Configuration state machine
wave: W6
slice: SLC-10
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-AI-ROUTING
traces:
  verifies:
  - SL-05
  - AGG-AI-ROUTING
  - REQ-AI-008
  - REQ-AI-011
---

# Acceptance — AI Routing Configuration

مولّدة من مصفوفة AGG-AI-ROUTING: 3 انتقالاً مسموحاً، 13 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: AI Routing Configuration lifecycle (AGG-AI-ROUTING)

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
      | AI Routing Configuration | DRAFT | CMD-RTG-EDIT | DRAFT | EVT-RTG-EDITED | 3 |
      | AI Routing Configuration | DRAFT | CMD-RTG-ACTIVATE | ACTIVE | EVT-RTG-ACTIVATED | 3 |
      | AI Routing Configuration | DRAFT | CMD-RTG-DISCARD | DISCARDED | EVT-RTG-DISCARDED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | AI Routing Configuration | CMD-RTG-DRAFT | DRAFT | EVT-RTG-DRAFTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | AI Routing Configuration | DRAFT | CMD-RTG-DRAFT | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | ACTIVE | CMD-RTG-DRAFT | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | ACTIVE | CMD-RTG-EDIT | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | ACTIVE | CMD-RTG-ACTIVATE | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | ACTIVE | CMD-RTG-DISCARD | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | SUPERSEDED | CMD-RTG-DRAFT | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | SUPERSEDED | CMD-RTG-EDIT | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | SUPERSEDED | CMD-RTG-ACTIVATE | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | SUPERSEDED | CMD-RTG-DISCARD | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | DISCARDED | CMD-RTG-DRAFT | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | DISCARDED | CMD-RTG-EDIT | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | DISCARDED | CMD-RTG-ACTIVATE | AI_ROUTING_INVALID_STATE_TRANSITION |
      | AI Routing Configuration | DISCARDED | CMD-RTG-DISCARD | AI_ROUTING_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | AI Routing Configuration | ACTIVE | successor activated | SUPERSEDED | EVT-RTG-SUPERSEDED |
```
