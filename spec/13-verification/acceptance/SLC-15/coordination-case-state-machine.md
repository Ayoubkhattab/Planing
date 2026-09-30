---
id: TST-COORDINATION-CASE-SM
type: acceptance-spec
title: Acceptance — Coordination Case state machine
wave: W6
slice: SLC-15
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-COORDINATION-CASE
traces:
  verifies:
  - SL-05
  - AGG-COORDINATION-CASE
  - REQ-CRD-001
  - REQ-CRD-002
---

# Acceptance — Coordination Case

مولّدة من مصفوفة AGG-COORDINATION-CASE: 11 انتقالاً مسموحاً، 25 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: Coordination Case lifecycle (AGG-COORDINATION-CASE)

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
      | Coordination Case | OPEN | CMD-CRD-ADD-PARTICIPANT | OPEN | EVT-CRD-PARTICIPANT-ADDED | 3 |
      | Coordination Case | OPEN | CMD-CRD-REMOVE-PARTICIPANT | OPEN | EVT-CRD-PARTICIPANT-REMOVED | 3 |
      | Coordination Case | OPEN | CMD-CRD-ACTIVATE | ACTIVE | EVT-CRD-ACTIVATED | 3 |
      | Coordination Case | OPEN | CMD-CRD-CANCEL | CANCELLED | EVT-CRD-CANCELLED | 3 |
      | Coordination Case | ACTIVE | CMD-CRD-ADD-PARTICIPANT | ACTIVE | EVT-CRD-PARTICIPANT-ADDED | 3 |
      | Coordination Case | ACTIVE | CMD-CRD-REMOVE-PARTICIPANT | ACTIVE | EVT-CRD-PARTICIPANT-REMOVED | 3 |
      | Coordination Case | ACTIVE | CMD-CRD-ASSIGN-RESPONSIBILITY | ACTIVE | EVT-CRD-RESPONSIBILITY-ASSIGNED | 3 |
      | Coordination Case | ACTIVE | CMD-CRD-UPDATE-RESPONSIBILITY | ACTIVE | EVT-CRD-RESPONSIBILITY-UPDATED | 3 |
      | Coordination Case | ACTIVE | CMD-CRD-REQUEST-DECISION | ACTIVE | EVT-CRD-DECISION-REQUESTED | 3 |
      | Coordination Case | ACTIVE | CMD-CRD-CLOSE | CLOSED | EVT-CRD-CLOSED | 3 |
      | Coordination Case | ACTIVE | CMD-CRD-CANCEL | CANCELLED | EVT-CRD-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Coordination Case | CMD-CRD-OPEN | OPEN | EVT-CRD-OPENED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Coordination Case | OPEN | CMD-CRD-OPEN | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | OPEN | CMD-CRD-ASSIGN-RESPONSIBILITY | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | OPEN | CMD-CRD-UPDATE-RESPONSIBILITY | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | OPEN | CMD-CRD-REQUEST-DECISION | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | OPEN | CMD-CRD-CLOSE | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | ACTIVE | CMD-CRD-OPEN | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | ACTIVE | CMD-CRD-ACTIVATE | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CLOSED | CMD-CRD-OPEN | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CLOSED | CMD-CRD-ADD-PARTICIPANT | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CLOSED | CMD-CRD-REMOVE-PARTICIPANT | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CLOSED | CMD-CRD-ACTIVATE | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CLOSED | CMD-CRD-ASSIGN-RESPONSIBILITY | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CLOSED | CMD-CRD-UPDATE-RESPONSIBILITY | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CLOSED | CMD-CRD-REQUEST-DECISION | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CLOSED | CMD-CRD-CLOSE | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CLOSED | CMD-CRD-CANCEL | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CANCELLED | CMD-CRD-OPEN | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CANCELLED | CMD-CRD-ADD-PARTICIPANT | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CANCELLED | CMD-CRD-REMOVE-PARTICIPANT | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CANCELLED | CMD-CRD-ACTIVATE | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CANCELLED | CMD-CRD-ASSIGN-RESPONSIBILITY | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CANCELLED | CMD-CRD-UPDATE-RESPONSIBILITY | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CANCELLED | CMD-CRD-REQUEST-DECISION | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CANCELLED | CMD-CRD-CLOSE | COORDINATION_CASE_INVALID_STATE_TRANSITION |
      | Coordination Case | CANCELLED | CMD-CRD-CANCEL | COORDINATION_CASE_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Coordination Case | ACTIVE | linked decision recorded | ACTIVE | EVT-CRD-DECISION-RECORDED |
```
