---
id: TST-AI-RESULT-SM
type: acceptance-spec
title: Acceptance — AI Result (reviewable) state machine
wave: W6
slice: SLC-10
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-AI-RESULT
traces:
  verifies:
  - SL-05
  - AGG-AI-RESULT
  - REQ-AI-005
  - REQ-AI-006
  - REQ-AI-008
---

# Acceptance — AI Result (reviewable)

مولّدة من مصفوفة AGG-AI-RESULT: 5 انتقالاً مسموحاً، 15 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: AI Result (reviewable) lifecycle (AGG-AI-RESULT)

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
      | AI Result (reviewable) | PROPOSED | CMD-AIRS-START-REVIEW | UNDER_REVIEW | EVT-AIRS-REVIEW-STARTED | 3 |
      | AI Result (reviewable) | PROPOSED | CMD-AIRS-REJECT | REJECTED | EVT-AIRS-REJECTED | 3 |
      | AI Result (reviewable) | UNDER_REVIEW | CMD-AIRS-ACCEPT | ACCEPTED | EVT-AIRS-ACCEPTED | 3 |
      | AI Result (reviewable) | UNDER_REVIEW | CMD-AIRS-ACCEPT-PARTIALLY | PARTIALLY_ACCEPTED | EVT-AIRS-PARTIALLY-ACCEPTED | 3 |
      | AI Result (reviewable) | UNDER_REVIEW | CMD-AIRS-REJECT | REJECTED | EVT-AIRS-REJECTED | 3 |

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
      | AI Result (reviewable) | PROPOSED | CMD-AIRS-ACCEPT | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | PROPOSED | CMD-AIRS-ACCEPT-PARTIALLY | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | UNDER_REVIEW | CMD-AIRS-START-REVIEW | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | ACCEPTED | CMD-AIRS-START-REVIEW | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | ACCEPTED | CMD-AIRS-ACCEPT | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | ACCEPTED | CMD-AIRS-ACCEPT-PARTIALLY | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | ACCEPTED | CMD-AIRS-REJECT | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | PARTIALLY_ACCEPTED | CMD-AIRS-START-REVIEW | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | PARTIALLY_ACCEPTED | CMD-AIRS-ACCEPT | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | PARTIALLY_ACCEPTED | CMD-AIRS-ACCEPT-PARTIALLY | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | PARTIALLY_ACCEPTED | CMD-AIRS-REJECT | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | REJECTED | CMD-AIRS-START-REVIEW | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | REJECTED | CMD-AIRS-ACCEPT | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | REJECTED | CMD-AIRS-ACCEPT-PARTIALLY | AI_RESULT_INVALID_STATE_TRANSITION |
      | AI Result (reviewable) | REJECTED | CMD-AIRS-REJECT | AI_RESULT_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | AI Result (reviewable) | ∅ | request COMPLETED for a reviewable operation | PROPOSED | EVT-AIRS-PROPOSED |
```
