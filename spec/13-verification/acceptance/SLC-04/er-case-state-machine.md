---
id: TST-ER-CASE-SM
type: acceptance-spec
title: Acceptance — Entity Resolution Case state machine
wave: W6
slice: SLC-04
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ER-CASE
traces:
  verifies:
  - SL-05
  - AGG-ER-CASE
  - REQ-INF-032
  - REQ-INF-033
  - REQ-INF-034
---

# Acceptance — Entity Resolution Case

مولّدة من مصفوفة AGG-ER-CASE: 12 انتقالاً مسموحاً، 68 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: Entity Resolution Case lifecycle (AGG-ER-CASE)

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
      | Entity Resolution Case | CANDIDATE | CMD-ER-START-REVIEW | UNDER_REVIEW | EVT-ER-REVIEW-STARTED | 3 |
      | Entity Resolution Case | CANDIDATE | CMD-ER-WITHDRAW | WITHDRAWN | EVT-ER-WITHDRAWN | 3 |
      | Entity Resolution Case | UNDER_REVIEW | CMD-ER-DECIDE-MATCH | MATCHED | EVT-ER-MATCHED | 3 |
      | Entity Resolution Case | UNDER_REVIEW | CMD-ER-DECIDE-NOT-MATCH | NOT_A_MATCH | EVT-ER-NOT-MATCHED | 3 |
      | Entity Resolution Case | UNDER_REVIEW | CMD-ER-PARK | POSSIBLE_DUPLICATE | EVT-ER-PARKED | 3 |
      | Entity Resolution Case | UNDER_REVIEW | CMD-ER-WITHDRAW | WITHDRAWN | EVT-ER-WITHDRAWN | 3 |
      | Entity Resolution Case | MATCHED | CMD-ER-REQUEST-SPLIT | SPLIT_REQUIRED | EVT-ER-SPLIT-REQUESTED | 3 |
      | Entity Resolution Case | POSSIBLE_DUPLICATE | CMD-ER-DECIDE-NOT-MATCH | NOT_A_MATCH | EVT-ER-NOT-MATCHED | 3 |
      | Entity Resolution Case | POSSIBLE_DUPLICATE | CMD-ER-RESUME | UNDER_REVIEW | EVT-ER-RESUMED | 3 |
      | Entity Resolution Case | POSSIBLE_DUPLICATE | CMD-ER-WITHDRAW | WITHDRAWN | EVT-ER-WITHDRAWN | 3 |
      | Entity Resolution Case | SPLIT_REQUIRED | CMD-ER-CONFIRM-MATCH | MATCHED | EVT-ER-MATCH-CONFIRMED | 3 |
      | Entity Resolution Case | SPLIT_REQUIRED | CMD-ER-SPLIT | SPLIT | EVT-ER-SPLIT | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Entity Resolution Case | CMD-ER-PROPOSE | CANDIDATE | EVT-ER-PROPOSED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Entity Resolution Case | CANDIDATE | CMD-ER-PROPOSE | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | CANDIDATE | CMD-ER-DECIDE-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | CANDIDATE | CMD-ER-DECIDE-NOT-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | CANDIDATE | CMD-ER-PARK | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | CANDIDATE | CMD-ER-RESUME | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | CANDIDATE | CMD-ER-REQUEST-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | CANDIDATE | CMD-ER-CONFIRM-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | CANDIDATE | CMD-ER-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | UNDER_REVIEW | CMD-ER-PROPOSE | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | UNDER_REVIEW | CMD-ER-START-REVIEW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | UNDER_REVIEW | CMD-ER-RESUME | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | UNDER_REVIEW | CMD-ER-REQUEST-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | UNDER_REVIEW | CMD-ER-CONFIRM-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | UNDER_REVIEW | CMD-ER-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | MATCHED | CMD-ER-PROPOSE | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | MATCHED | CMD-ER-START-REVIEW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | MATCHED | CMD-ER-DECIDE-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | MATCHED | CMD-ER-DECIDE-NOT-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | MATCHED | CMD-ER-PARK | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | MATCHED | CMD-ER-RESUME | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | MATCHED | CMD-ER-CONFIRM-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | MATCHED | CMD-ER-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | MATCHED | CMD-ER-WITHDRAW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | POSSIBLE_DUPLICATE | CMD-ER-PROPOSE | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | POSSIBLE_DUPLICATE | CMD-ER-START-REVIEW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | POSSIBLE_DUPLICATE | CMD-ER-DECIDE-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | POSSIBLE_DUPLICATE | CMD-ER-PARK | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | POSSIBLE_DUPLICATE | CMD-ER-REQUEST-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | POSSIBLE_DUPLICATE | CMD-ER-CONFIRM-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | POSSIBLE_DUPLICATE | CMD-ER-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT_REQUIRED | CMD-ER-PROPOSE | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT_REQUIRED | CMD-ER-START-REVIEW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT_REQUIRED | CMD-ER-DECIDE-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT_REQUIRED | CMD-ER-DECIDE-NOT-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT_REQUIRED | CMD-ER-PARK | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT_REQUIRED | CMD-ER-RESUME | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT_REQUIRED | CMD-ER-REQUEST-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT_REQUIRED | CMD-ER-WITHDRAW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | NOT_A_MATCH | CMD-ER-PROPOSE | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | NOT_A_MATCH | CMD-ER-START-REVIEW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | NOT_A_MATCH | CMD-ER-DECIDE-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | NOT_A_MATCH | CMD-ER-DECIDE-NOT-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | NOT_A_MATCH | CMD-ER-PARK | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | NOT_A_MATCH | CMD-ER-RESUME | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | NOT_A_MATCH | CMD-ER-REQUEST-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | NOT_A_MATCH | CMD-ER-CONFIRM-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | NOT_A_MATCH | CMD-ER-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | NOT_A_MATCH | CMD-ER-WITHDRAW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT | CMD-ER-PROPOSE | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT | CMD-ER-START-REVIEW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT | CMD-ER-DECIDE-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT | CMD-ER-DECIDE-NOT-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT | CMD-ER-PARK | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT | CMD-ER-RESUME | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT | CMD-ER-REQUEST-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT | CMD-ER-CONFIRM-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT | CMD-ER-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | SPLIT | CMD-ER-WITHDRAW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | WITHDRAWN | CMD-ER-PROPOSE | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | WITHDRAWN | CMD-ER-START-REVIEW | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | WITHDRAWN | CMD-ER-DECIDE-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | WITHDRAWN | CMD-ER-DECIDE-NOT-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | WITHDRAWN | CMD-ER-PARK | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | WITHDRAWN | CMD-ER-RESUME | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | WITHDRAWN | CMD-ER-REQUEST-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | WITHDRAWN | CMD-ER-CONFIRM-MATCH | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | WITHDRAWN | CMD-ER-SPLIT | ER_CASE_INVALID_STATE_TRANSITION |
      | Entity Resolution Case | WITHDRAWN | CMD-ER-WITHDRAW | ER_CASE_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Entity Resolution Case | ∅ | candidate generator score ≥ propose threshold | CANDIDATE | EVT-ER-PROPOSED |
```
