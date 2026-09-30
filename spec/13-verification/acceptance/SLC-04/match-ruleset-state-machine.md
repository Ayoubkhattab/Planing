---
id: TST-MATCH-RULESET-SM
type: acceptance-spec
title: Acceptance — Match Ruleset state machine
wave: W6
slice: SLC-04
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-MATCH-RULESET
traces:
  verifies:
  - SL-05
  - AGG-MATCH-RULESET
  - REQ-INF-032
  - REQ-SRC-003
---

# Acceptance — Match Ruleset

مولّدة من مصفوفة AGG-MATCH-RULESET: 2 انتقالاً مسموحاً، 7 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: Match Ruleset lifecycle (AGG-MATCH-RULESET)

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
      | Match Ruleset | DRAFT | CMD-MRS-EDIT | DRAFT | EVT-MRS-EDITED | 3 |
      | Match Ruleset | DRAFT | CMD-MRS-ACTIVATE | ACTIVE | EVT-MRS-ACTIVATED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Match Ruleset | CMD-MRS-DRAFT | DRAFT | EVT-MRS-DRAFTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Match Ruleset | DRAFT | CMD-MRS-DRAFT | MATCH_RULESET_INVALID_STATE_TRANSITION |
      | Match Ruleset | ACTIVE | CMD-MRS-DRAFT | MATCH_RULESET_INVALID_STATE_TRANSITION |
      | Match Ruleset | ACTIVE | CMD-MRS-EDIT | MATCH_RULESET_INVALID_STATE_TRANSITION |
      | Match Ruleset | ACTIVE | CMD-MRS-ACTIVATE | MATCH_RULESET_INVALID_STATE_TRANSITION |
      | Match Ruleset | SUPERSEDED | CMD-MRS-DRAFT | MATCH_RULESET_INVALID_STATE_TRANSITION |
      | Match Ruleset | SUPERSEDED | CMD-MRS-EDIT | MATCH_RULESET_INVALID_STATE_TRANSITION |
      | Match Ruleset | SUPERSEDED | CMD-MRS-ACTIVATE | MATCH_RULESET_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Match Ruleset | ACTIVE | successor activated | SUPERSEDED | EVT-MRS-SUPERSEDED |
```
