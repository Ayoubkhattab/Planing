---
id: TST-CORRELATION-PROPOSAL-SM
type: acceptance-spec
title: Acceptance — Correlation Proposal state machine
wave: W6
slice: SLC-15
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-CORRELATION-PROPOSAL
traces:
  verifies:
  - SL-05
  - AGG-CORRELATION-PROPOSAL
  - REQ-FUS-001
  - REQ-FUS-002
---

# Acceptance — Correlation Proposal

مولّدة من مصفوفة AGG-CORRELATION-PROPOSAL: 4 انتقالاً مسموحاً، 16 رفضاً.

```gherkin
Feature: Correlation Proposal lifecycle (AGG-CORRELATION-PROPOSAL)

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
      | Correlation Proposal | PROPOSED | CMD-CRP-START-REVIEW | UNDER_REVIEW | EVT-CRP-REVIEW-STARTED | 3 |
      | Correlation Proposal | PROPOSED | CMD-CRP-REJECT | REJECTED | EVT-CRP-REJECTED | 3 |
      | Correlation Proposal | UNDER_REVIEW | CMD-CRP-ACCEPT | ACCEPTED | EVT-CRP-ACCEPTED | 3 |
      | Correlation Proposal | UNDER_REVIEW | CMD-CRP-REJECT | REJECTED | EVT-CRP-REJECTED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Correlation Proposal | CMD-CRP-PROPOSE | PROPOSED | EVT-CRP-PROPOSED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Correlation Proposal | PROPOSED | CMD-CRP-PROPOSE | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | PROPOSED | CMD-CRP-ACCEPT | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | UNDER_REVIEW | CMD-CRP-PROPOSE | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | UNDER_REVIEW | CMD-CRP-START-REVIEW | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | ACCEPTED | CMD-CRP-PROPOSE | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | ACCEPTED | CMD-CRP-START-REVIEW | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | ACCEPTED | CMD-CRP-ACCEPT | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | ACCEPTED | CMD-CRP-REJECT | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | REJECTED | CMD-CRP-PROPOSE | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | REJECTED | CMD-CRP-START-REVIEW | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | REJECTED | CMD-CRP-ACCEPT | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | REJECTED | CMD-CRP-REJECT | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | EXPIRED | CMD-CRP-PROPOSE | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | EXPIRED | CMD-CRP-START-REVIEW | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | EXPIRED | CMD-CRP-ACCEPT | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
      | Correlation Proposal | EXPIRED | CMD-CRP-REJECT | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION |
```
