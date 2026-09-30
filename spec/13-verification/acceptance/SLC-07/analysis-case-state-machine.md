---
id: TST-ANALYSIS-CASE-SM
type: acceptance-spec
title: Acceptance — Analysis Case state machine
wave: W6
slice: SLC-07
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ANALYSIS-CASE
traces:
  verifies:
  - SL-05
  - AGG-ANALYSIS-CASE
  - REQ-ANL-001
  - REQ-ANL-007
---

# Acceptance — Analysis Case

مولّدة من مصفوفة AGG-ANALYSIS-CASE: 17 انتقالاً مسموحاً، 39 رفضاً.

```gherkin
Feature: Analysis Case lifecycle (AGG-ANALYSIS-CASE)

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
      | Analysis Case | DRAFT | CMD-ACS-DEFINE | DRAFT | EVT-ACS-DEFINED | 3 |
      | Analysis Case | DRAFT | CMD-ACS-OPEN | OPEN | EVT-ACS-OPENED | 3 |
      | Analysis Case | DRAFT | CMD-ACS-CANCEL | CANCELLED | EVT-ACS-CANCELLED | 3 |
      | Analysis Case | DRAFT | CMD-ACS-RECLASSIFY | DRAFT | EVT-ACS-RECLASSIFIED | 3 |
      | Analysis Case | OPEN | CMD-ACS-DEFINE | OPEN | EVT-ACS-DEFINED | 3 |
      | Analysis Case | OPEN | CMD-ACS-ADD-HYPOTHESIS | OPEN | EVT-ACS-HYPOTHESIS-ADDED | 3 |
      | Analysis Case | OPEN | CMD-ACS-UPDATE-HYPOTHESIS | OPEN | EVT-ACS-HYPOTHESIS-UPDATED | 3 |
      | Analysis Case | OPEN | CMD-ACS-ADD-ASSUMPTION | OPEN | EVT-ACS-ASSUMPTION-ADDED | 3 |
      | Analysis Case | OPEN | CMD-ACS-RETIRE-ASSUMPTION | OPEN | EVT-ACS-ASSUMPTION-RETIRED | 3 |
      | Analysis Case | OPEN | CMD-ACS-SELECT-EVIDENCE | OPEN | EVT-ACS-EVIDENCE-SELECTED | 3 |
      | Analysis Case | OPEN | CMD-ACS-DESELECT-EVIDENCE | OPEN | EVT-ACS-EVIDENCE-DESELECTED | 3 |
      | Analysis Case | OPEN | CMD-ACS-DEFINE-SCENARIO | OPEN | EVT-ACS-SCENARIO-DEFINED | 3 |
      | Analysis Case | OPEN | CMD-ACS-CLOSE | CLOSED | EVT-ACS-CLOSED | 3 |
      | Analysis Case | OPEN | CMD-ACS-CANCEL | CANCELLED | EVT-ACS-CANCELLED | 3 |
      | Analysis Case | OPEN | CMD-ACS-RECLASSIFY | OPEN | EVT-ACS-RECLASSIFIED | 3 |
      | Analysis Case | CLOSED | CMD-ACS-REOPEN | OPEN | EVT-ACS-REOPENED | 3 |
      | Analysis Case | CLOSED | CMD-ACS-RECLASSIFY | CLOSED | EVT-ACS-RECLASSIFIED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Analysis Case | CMD-ACS-CREATE | DRAFT | EVT-ACS-CREATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Analysis Case | DRAFT | CMD-ACS-CREATE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | DRAFT | CMD-ACS-ADD-HYPOTHESIS | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | DRAFT | CMD-ACS-UPDATE-HYPOTHESIS | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | DRAFT | CMD-ACS-ADD-ASSUMPTION | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | DRAFT | CMD-ACS-RETIRE-ASSUMPTION | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | DRAFT | CMD-ACS-SELECT-EVIDENCE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | DRAFT | CMD-ACS-DESELECT-EVIDENCE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | DRAFT | CMD-ACS-DEFINE-SCENARIO | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | DRAFT | CMD-ACS-CLOSE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | DRAFT | CMD-ACS-REOPEN | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | OPEN | CMD-ACS-CREATE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | OPEN | CMD-ACS-OPEN | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | OPEN | CMD-ACS-REOPEN | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-CREATE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-DEFINE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-OPEN | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-ADD-HYPOTHESIS | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-UPDATE-HYPOTHESIS | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-ADD-ASSUMPTION | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-RETIRE-ASSUMPTION | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-SELECT-EVIDENCE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-DESELECT-EVIDENCE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-DEFINE-SCENARIO | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-CLOSE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CLOSED | CMD-ACS-CANCEL | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-CREATE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-DEFINE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-OPEN | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-ADD-HYPOTHESIS | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-UPDATE-HYPOTHESIS | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-ADD-ASSUMPTION | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-RETIRE-ASSUMPTION | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-SELECT-EVIDENCE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-DESELECT-EVIDENCE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-DEFINE-SCENARIO | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-CLOSE | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-REOPEN | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-CANCEL | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
      | Analysis Case | CANCELLED | CMD-ACS-RECLASSIFY | ANALYSIS_CASE_INVALID_STATE_TRANSITION |
```
