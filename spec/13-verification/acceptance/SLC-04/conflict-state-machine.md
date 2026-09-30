---
id: TST-CONFLICT-SM
type: acceptance-spec
title: Acceptance — Conflict state machine
wave: W6
slice: SLC-04
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-CONFLICT
traces:
  verifies:
  - SL-05
  - AGG-CONFLICT
  - REQ-INF-025
  - REQ-INF-024
---

# Acceptance — Conflict

مولّدة من مصفوفة AGG-CONFLICT: 7 انتقالاً مسموحاً، 23 رفضاً، 7 انتقالاً نظامياً (SYS).

```gherkin
Feature: Conflict lifecycle (AGG-CONFLICT)

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
      | Conflict | OPEN | CMD-CNF-ASSIGN | OPEN | EVT-CNF-ASSIGNED | 3 |
      | Conflict | OPEN | CMD-CNF-START-REVIEW | UNDER_REVIEW | EVT-CNF-REVIEW-STARTED | 3 |
      | Conflict | UNDER_REVIEW | CMD-CNF-ASSIGN | UNDER_REVIEW | EVT-CNF-ASSIGNED | 3 |
      | Conflict | UNDER_REVIEW | CMD-CNF-RESOLVE | RESOLVED | EVT-CNF-RESOLVED | 3 |
      | Conflict | UNDER_REVIEW | CMD-CNF-ACCEPT | ACCEPTED_AS_CONFLICT | EVT-CNF-ACCEPTED | 3 |
      | Conflict | RESOLVED | CMD-CNF-REOPEN | UNDER_REVIEW | EVT-CNF-REOPENED | 3 |
      | Conflict | ACCEPTED_AS_CONFLICT | CMD-CNF-REOPEN | UNDER_REVIEW | EVT-CNF-REOPENED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Conflict | CMD-CNF-RAISE | OPEN | EVT-CNF-RAISED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Conflict | OPEN | CMD-CNF-RAISE | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | OPEN | CMD-CNF-RESOLVE | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | OPEN | CMD-CNF-ACCEPT | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | OPEN | CMD-CNF-REOPEN | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | UNDER_REVIEW | CMD-CNF-RAISE | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | UNDER_REVIEW | CMD-CNF-START-REVIEW | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | UNDER_REVIEW | CMD-CNF-REOPEN | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | RESOLVED | CMD-CNF-RAISE | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | RESOLVED | CMD-CNF-ASSIGN | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | RESOLVED | CMD-CNF-START-REVIEW | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | RESOLVED | CMD-CNF-RESOLVE | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | RESOLVED | CMD-CNF-ACCEPT | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | ACCEPTED_AS_CONFLICT | CMD-CNF-RAISE | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | ACCEPTED_AS_CONFLICT | CMD-CNF-ASSIGN | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | ACCEPTED_AS_CONFLICT | CMD-CNF-START-REVIEW | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | ACCEPTED_AS_CONFLICT | CMD-CNF-RESOLVE | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | ACCEPTED_AS_CONFLICT | CMD-CNF-ACCEPT | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | SUPERSEDED | CMD-CNF-RAISE | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | SUPERSEDED | CMD-CNF-ASSIGN | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | SUPERSEDED | CMD-CNF-START-REVIEW | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | SUPERSEDED | CMD-CNF-RESOLVE | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | SUPERSEDED | CMD-CNF-ACCEPT | CONFLICT_INVALID_STATE_TRANSITION |
      | Conflict | SUPERSEDED | CMD-CNF-REOPEN | CONFLICT_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Conflict | ∅ | conflict rule matched | OPEN | EVT-CNF-DETECTED |
      | Conflict | OPEN | incompatible claim joined | OPEN | EVT-CNF-CLAIM-ADDED |
      | Conflict | OPEN | member set no longer conflicting | SUPERSEDED | EVT-CNF-SUPERSEDED |
      | Conflict | UNDER_REVIEW | incompatible claim joined | UNDER_REVIEW | EVT-CNF-CLAIM-ADDED |
      | Conflict | UNDER_REVIEW | member set no longer conflicting | SUPERSEDED | EVT-CNF-SUPERSEDED |
      | Conflict | RESOLVED | member set no longer conflicting | SUPERSEDED | EVT-CNF-SUPERSEDED |
      | Conflict | ACCEPTED_AS_CONFLICT | member set no longer conflicting | SUPERSEDED | EVT-CNF-SUPERSEDED |
```
