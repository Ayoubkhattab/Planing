---
id: TST-LEGAL-HOLD-SM
type: acceptance-spec
title: Acceptance — Legal Hold state machine
wave: W6
slice: SLC-12a
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-LEGAL-HOLD
traces:
  verifies:
  - SL-05
  - AGG-LEGAL-HOLD
  - REQ-GOV-007
---

# Acceptance — Legal Hold

مولّدة من مصفوفة AGG-LEGAL-HOLD: 4 انتقالاً مسموحاً، 11 رفضاً.

```gherkin
Feature: Legal Hold lifecycle (AGG-LEGAL-HOLD)

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
      | Legal Hold | ACTIVE | CMD-LHD-EXTEND | ACTIVE | EVT-LHD-EXTENDED | 3 |
      | Legal Hold | ACTIVE | CMD-LHD-REQUEST-RELEASE | RELEASE_REQUESTED | EVT-LHD-RELEASE-REQUESTED | 3 |
      | Legal Hold | RELEASE_REQUESTED | CMD-LHD-APPROVE-RELEASE | RELEASED | EVT-LHD-RELEASED | 3 |
      | Legal Hold | RELEASE_REQUESTED | CMD-LHD-CANCEL-RELEASE | ACTIVE | EVT-LHD-RELEASE-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Legal Hold | CMD-LHD-PLACE | ACTIVE | EVT-LHD-PLACED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Legal Hold | ACTIVE | CMD-LHD-PLACE | LEGAL_HOLD_INVALID_STATE_TRANSITION |
      | Legal Hold | ACTIVE | CMD-LHD-APPROVE-RELEASE | LEGAL_HOLD_INVALID_STATE_TRANSITION |
      | Legal Hold | ACTIVE | CMD-LHD-CANCEL-RELEASE | LEGAL_HOLD_INVALID_STATE_TRANSITION |
      | Legal Hold | RELEASE_REQUESTED | CMD-LHD-PLACE | LEGAL_HOLD_INVALID_STATE_TRANSITION |
      | Legal Hold | RELEASE_REQUESTED | CMD-LHD-EXTEND | LEGAL_HOLD_INVALID_STATE_TRANSITION |
      | Legal Hold | RELEASE_REQUESTED | CMD-LHD-REQUEST-RELEASE | LEGAL_HOLD_INVALID_STATE_TRANSITION |
      | Legal Hold | RELEASED | CMD-LHD-PLACE | LEGAL_HOLD_INVALID_STATE_TRANSITION |
      | Legal Hold | RELEASED | CMD-LHD-EXTEND | LEGAL_HOLD_INVALID_STATE_TRANSITION |
      | Legal Hold | RELEASED | CMD-LHD-REQUEST-RELEASE | LEGAL_HOLD_INVALID_STATE_TRANSITION |
      | Legal Hold | RELEASED | CMD-LHD-APPROVE-RELEASE | LEGAL_HOLD_INVALID_STATE_TRANSITION |
      | Legal Hold | RELEASED | CMD-LHD-CANCEL-RELEASE | LEGAL_HOLD_INVALID_STATE_TRANSITION |
```
