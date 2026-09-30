---
id: TST-ALERT-SM
type: acceptance-spec
title: Acceptance — Alert state machine
wave: W6
slice: SLC-06
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ALERT
traces:
  verifies:
  - SL-05
  - AGG-ALERT
  - REQ-SIT-004
  - REQ-SIT-005
  - REQ-SIT-006
---

# Acceptance — Alert

مولّدة من مصفوفة AGG-ALERT: 5 انتقالاً مسموحاً، 7 رفضاً.

```gherkin
Feature: Alert lifecycle (AGG-ALERT)

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
      | Alert | RAISED | CMD-ALR-ACKNOWLEDGE | ACKNOWLEDGED | EVT-ALR-ACKNOWLEDGED | 3 |
      | Alert | RAISED | CMD-ALR-RESOLVE | RESOLVED | EVT-ALR-RESOLVED | 3 |
      | Alert | RAISED | CMD-ALR-DISMISS | DISMISSED | EVT-ALR-DISMISSED | 3 |
      | Alert | ACKNOWLEDGED | CMD-ALR-RESOLVE | RESOLVED | EVT-ALR-RESOLVED | 3 |
      | Alert | ACKNOWLEDGED | CMD-ALR-DISMISS | DISMISSED | EVT-ALR-DISMISSED | 3 |

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
      | Alert | ACKNOWLEDGED | CMD-ALR-ACKNOWLEDGE | ALERT_INVALID_STATE_TRANSITION |
      | Alert | RESOLVED | CMD-ALR-ACKNOWLEDGE | ALERT_INVALID_STATE_TRANSITION |
      | Alert | RESOLVED | CMD-ALR-RESOLVE | ALERT_INVALID_STATE_TRANSITION |
      | Alert | RESOLVED | CMD-ALR-DISMISS | ALERT_INVALID_STATE_TRANSITION |
      | Alert | DISMISSED | CMD-ALR-ACKNOWLEDGE | ALERT_INVALID_STATE_TRANSITION |
      | Alert | DISMISSED | CMD-ALR-RESOLVE | ALERT_INVALID_STATE_TRANSITION |
      | Alert | DISMISSED | CMD-ALR-DISMISS | ALERT_INVALID_STATE_TRANSITION |
```
