---
id: TST-ANALYSIS-RUN-SM
type: acceptance-spec
title: Acceptance — Analysis Run state machine
wave: W6
slice: SLC-07
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ANALYSIS-RUN
traces:
  verifies:
  - SL-05
  - AGG-ANALYSIS-RUN
  - REQ-ANL-002
  - REQ-ANL-003
  - REQ-ANL-004
  - REQ-INF-035
---

# Acceptance — Analysis Run

مولّدة من مصفوفة AGG-ANALYSIS-RUN: 2 انتقالاً مسموحاً، 13 رفضاً.

```gherkin
Feature: Analysis Run lifecycle (AGG-ANALYSIS-RUN)

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
      | Analysis Run | QUEUED | CMD-RUN-CANCEL | CANCELLED | EVT-RUN-CANCELLED | 3 |
      | Analysis Run | RUNNING | CMD-RUN-CANCEL | CANCELLED | EVT-RUN-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Analysis Run | CMD-RUN-SUBMIT | QUEUED | EVT-RUN-QUEUED |
      | Analysis Run | CMD-RUN-REPRODUCE | QUEUED | EVT-RUN-QUEUED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Analysis Run | QUEUED | CMD-RUN-SUBMIT | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | QUEUED | CMD-RUN-REPRODUCE | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | RUNNING | CMD-RUN-SUBMIT | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | RUNNING | CMD-RUN-REPRODUCE | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | SUCCEEDED | CMD-RUN-SUBMIT | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | SUCCEEDED | CMD-RUN-REPRODUCE | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | SUCCEEDED | CMD-RUN-CANCEL | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | FAILED | CMD-RUN-SUBMIT | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | FAILED | CMD-RUN-REPRODUCE | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | FAILED | CMD-RUN-CANCEL | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | CANCELLED | CMD-RUN-SUBMIT | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | CANCELLED | CMD-RUN-REPRODUCE | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
      | Analysis Run | CANCELLED | CMD-RUN-CANCEL | ANALYSIS_RUN_INVALID_STATE_TRANSITION |
```
