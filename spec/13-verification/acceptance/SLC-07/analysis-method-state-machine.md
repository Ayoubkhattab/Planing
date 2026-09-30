---
id: TST-ANALYSIS-METHOD-SM
type: acceptance-spec
title: Acceptance — Analysis Method Version state machine
wave: W6
slice: SLC-07
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ANALYSIS-METHOD
traces:
  verifies:
  - SL-05
  - AGG-ANALYSIS-METHOD
  - REQ-ANL-002
  - REQ-ANL-003
---

# Acceptance — Analysis Method Version

مولّدة من مصفوفة AGG-ANALYSIS-METHOD: 3 انتقالاً مسموحاً، 13 رفضاً.

```gherkin
Feature: Analysis Method Version lifecycle (AGG-ANALYSIS-METHOD)

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
      | Analysis Method Version | DRAFT | CMD-AMT-ACTIVATE | ACTIVE | EVT-AMT-ACTIVATED | 3 |
      | Analysis Method Version | ACTIVE | CMD-AMT-DEPRECATE | DEPRECATED | EVT-AMT-DEPRECATED | 3 |
      | Analysis Method Version | DEPRECATED | CMD-AMT-RETIRE | RETIRED | EVT-AMT-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Analysis Method Version | CMD-AMT-REGISTER | DRAFT | EVT-AMT-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Analysis Method Version | DRAFT | CMD-AMT-REGISTER | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | DRAFT | CMD-AMT-DEPRECATE | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | DRAFT | CMD-AMT-RETIRE | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | ACTIVE | CMD-AMT-REGISTER | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | ACTIVE | CMD-AMT-ACTIVATE | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | ACTIVE | CMD-AMT-RETIRE | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | DEPRECATED | CMD-AMT-REGISTER | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | DEPRECATED | CMD-AMT-ACTIVATE | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | DEPRECATED | CMD-AMT-DEPRECATE | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | RETIRED | CMD-AMT-REGISTER | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | RETIRED | CMD-AMT-ACTIVATE | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | RETIRED | CMD-AMT-DEPRECATE | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
      | Analysis Method Version | RETIRED | CMD-AMT-RETIRE | ANALYSIS_METHOD_INVALID_STATE_TRANSITION |
```
