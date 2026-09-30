---
id: TST-RISK-SM
type: acceptance-spec
title: Acceptance — Risk state machine
wave: W6
slice: SLC-17
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-RISK
traces:
  verifies:
  - SL-05
  - AGG-RISK
  - REQ-RCM-001
  - REQ-RCM-002
  - REQ-RCM-003
  - REQ-RCM-004
  - REQ-RCM-005
---

# Acceptance — Risk

مولّدة من مصفوفة AGG-RISK: 7 انتقالاً مسموحاً، 13 رفضاً.

```gherkin
Feature: Risk lifecycle (AGG-RISK)

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
      | Risk | IDENTIFIED | CMD-RIS-ASSESS | ASSESSED | EVT-RIS-ASSESSED | 3 |
      | Risk | IDENTIFIED | CMD-RIS-CLOSE | CLOSED | EVT-RIS-CLOSED | 3 |
      | Risk | ASSESSED | CMD-RIS-PLAN-TREATMENT | TREATED | EVT-RIS-TREATMENT-PLANNED | 3 |
      | Risk | ASSESSED | CMD-RIS-REASSESS | ASSESSED | EVT-RIS-REASSESSED | 3 |
      | Risk | ASSESSED | CMD-RIS-CLOSE | CLOSED | EVT-RIS-CLOSED | 3 |
      | Risk | TREATED | CMD-RIS-REASSESS | ASSESSED | EVT-RIS-REASSESSED | 3 |
      | Risk | TREATED | CMD-RIS-CLOSE | CLOSED | EVT-RIS-CLOSED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Risk | CMD-RIS-IDENTIFY | IDENTIFIED | EVT-RIS-IDENTIFIED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Risk | IDENTIFIED | CMD-RIS-IDENTIFY | RISK_INVALID_STATE_TRANSITION |
      | Risk | IDENTIFIED | CMD-RIS-PLAN-TREATMENT | RISK_INVALID_STATE_TRANSITION |
      | Risk | IDENTIFIED | CMD-RIS-REASSESS | RISK_INVALID_STATE_TRANSITION |
      | Risk | ASSESSED | CMD-RIS-IDENTIFY | RISK_INVALID_STATE_TRANSITION |
      | Risk | ASSESSED | CMD-RIS-ASSESS | RISK_INVALID_STATE_TRANSITION |
      | Risk | TREATED | CMD-RIS-IDENTIFY | RISK_INVALID_STATE_TRANSITION |
      | Risk | TREATED | CMD-RIS-ASSESS | RISK_INVALID_STATE_TRANSITION |
      | Risk | TREATED | CMD-RIS-PLAN-TREATMENT | RISK_INVALID_STATE_TRANSITION |
      | Risk | CLOSED | CMD-RIS-IDENTIFY | RISK_INVALID_STATE_TRANSITION |
      | Risk | CLOSED | CMD-RIS-ASSESS | RISK_INVALID_STATE_TRANSITION |
      | Risk | CLOSED | CMD-RIS-PLAN-TREATMENT | RISK_INVALID_STATE_TRANSITION |
      | Risk | CLOSED | CMD-RIS-REASSESS | RISK_INVALID_STATE_TRANSITION |
      | Risk | CLOSED | CMD-RIS-CLOSE | RISK_INVALID_STATE_TRANSITION |
```
