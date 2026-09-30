---
id: TST-OUTCOME-TRACKER-SM
type: acceptance-spec
title: Acceptance — Outcome Tracker state machine
wave: W6
slice: SLC-08
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-OUTCOME-TRACKER
traces:
  verifies:
  - SL-05
  - AGG-OUTCOME-TRACKER
  - REQ-OPS-013
---

# Acceptance — Outcome Tracker

مولّدة من مصفوفة AGG-OUTCOME-TRACKER: 2 انتقالاً مسموحاً، 2 رفضاً، 3 انتقالاً نظامياً (SYS).

```gherkin
Feature: Outcome Tracker lifecycle (AGG-OUTCOME-TRACKER)

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
      | Outcome Tracker | ACTIVE | CMD-OUT-RECORD | ACTIVE | EVT-OUT-MEASURED | 3 |
      | Outcome Tracker | ACTIVE | CMD-OUT-CORRECT | ACTIVE | EVT-OUT-MEASUREMENT-CORRECTED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Outcome Tracker | CLOSED | CMD-OUT-RECORD | OUTCOME_TRACKER_INVALID_STATE_TRANSITION |
      | Outcome Tracker | CLOSED | CMD-OUT-CORRECT | OUTCOME_TRACKER_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Outcome Tracker | ∅ | outcome baselined | ACTIVE | EVT-OUT-TRACKER-CREATED |
      | Outcome Tracker | ACTIVE | target changed by new baseline | ACTIVE | EVT-OUT-TARGET-CHANGED |
      | Outcome Tracker | ACTIVE | plan closed or cancelled | CLOSED | EVT-OUT-TRACKER-CLOSED |
```
