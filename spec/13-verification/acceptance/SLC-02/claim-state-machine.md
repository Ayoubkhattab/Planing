---
id: TST-CLAIM-SM
type: acceptance-spec
title: Acceptance — Claim state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-CLAIM
traces:
  verifies:
  - SL-05
  - AGG-CLAIM
  - REQ-INF-021
  - REQ-INF-022
  - REQ-INF-024
  - REQ-INF-026
  - REQ-INF-037
---

# Acceptance — Claim

مولّدة من مصفوفة AGG-CLAIM: 6 انتقالاً مسموحاً، 6 رفضاً.

```gherkin
Feature: Claim lifecycle (AGG-CLAIM)

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
      | Claim | CURRENT | CMD-CLM-CORRECT | CLOSED | EVT-CLM-CORRECTED | 3 |
      | Claim | CURRENT | CMD-CLM-RECORD-CHANGE | CLOSED | EVT-CLM-CHANGED | 3 |
      | Claim | CURRENT | CMD-CLM-RETRACT | CLOSED | EVT-CLM-RETRACTED | 3 |
      | Claim | CURRENT | CMD-CLM-ASSESS | CURRENT | EVT-CLM-ASSESSED | 3 |
      | Claim | CURRENT | CMD-CLM-RECLASSIFY | CURRENT | EVT-CLM-RECLASSIFIED | 3 |
      | Claim | CLOSED | CMD-CLM-RECLASSIFY | CLOSED | EVT-CLM-RECLASSIFIED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Claim | CMD-CLM-ASSERT | CURRENT | EVT-CLM-ASSERTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Claim | CURRENT | CMD-CLM-ASSERT | CLAIM_INVALID_STATE_TRANSITION |
      | Claim | CLOSED | CMD-CLM-ASSERT | CLAIM_INVALID_STATE_TRANSITION |
      | Claim | CLOSED | CMD-CLM-CORRECT | CLAIM_INVALID_STATE_TRANSITION |
      | Claim | CLOSED | CMD-CLM-RECORD-CHANGE | CLAIM_INVALID_STATE_TRANSITION |
      | Claim | CLOSED | CMD-CLM-RETRACT | CLAIM_INVALID_STATE_TRANSITION |
      | Claim | CLOSED | CMD-CLM-ASSESS | CLAIM_INVALID_STATE_TRANSITION |
```
