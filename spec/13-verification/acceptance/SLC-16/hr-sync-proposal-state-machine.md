---
id: TST-HR-SYNC-PROPOSAL-SM
type: acceptance-spec
title: Acceptance — HR Sync Proposal state machine
wave: W6
slice: SLC-16
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-HR-SYNC-PROPOSAL
traces:
  verifies:
  - SL-05
  - AGG-HR-SYNC-PROPOSAL
  - REQ-INT-004
---

# Acceptance — HR Sync Proposal

مولّدة من مصفوفة AGG-HR-SYNC-PROPOSAL: 2 انتقالاً مسموحاً، 8 رفضاً.

```gherkin
Feature: HR Sync Proposal lifecycle (AGG-HR-SYNC-PROPOSAL)

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
      | HR Sync Proposal | PROPOSED | CMD-HRS-APPROVE | APPROVED | EVT-HRS-APPROVED | 3 |
      | HR Sync Proposal | PROPOSED | CMD-HRS-REJECT | REJECTED | EVT-HRS-REJECTED | 3 |

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
      | HR Sync Proposal | APPROVED | CMD-HRS-APPROVE | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
      | HR Sync Proposal | APPROVED | CMD-HRS-REJECT | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
      | HR Sync Proposal | REJECTED | CMD-HRS-APPROVE | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
      | HR Sync Proposal | REJECTED | CMD-HRS-REJECT | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
      | HR Sync Proposal | SUPERSEDED | CMD-HRS-APPROVE | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
      | HR Sync Proposal | SUPERSEDED | CMD-HRS-REJECT | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
      | HR Sync Proposal | EXPIRED | CMD-HRS-APPROVE | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
      | HR Sync Proposal | EXPIRED | CMD-HRS-REJECT | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION |
```
