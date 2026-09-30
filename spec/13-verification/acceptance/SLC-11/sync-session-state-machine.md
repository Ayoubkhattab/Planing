---
id: TST-SYNC-SESSION-SM
type: acceptance-spec
title: Acceptance — Sync Session state machine
wave: W6
slice: SLC-11
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-SYNC-SESSION
traces:
  verifies:
  - SL-05
  - AGG-SYNC-SESSION
  - REQ-OFF-001
  - REQ-OFF-003
  - REQ-OFF-004
  - REQ-OFF-006
---

# Acceptance — Sync Session

مولّدة من مصفوفة AGG-SYNC-SESSION: 2 انتقالاً مسموحاً، 10 رفضاً.

```gherkin
Feature: Sync Session lifecycle (AGG-SYNC-SESSION)

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
      | Sync Session | OPEN | CMD-SYN-UPLOAD-BATCH | APPLYING | EVT-SYN-BATCH-RECEIVED | 3 |
      | Sync Session | APPLYING | CMD-SYN-UPLOAD-BATCH | APPLYING | EVT-SYN-BATCH-RECEIVED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Sync Session | CMD-SYN-OPEN | OPEN | EVT-SYN-OPENED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Sync Session | OPEN | CMD-SYN-OPEN | SYNC_SESSION_INVALID_STATE_TRANSITION |
      | Sync Session | APPLYING | CMD-SYN-OPEN | SYNC_SESSION_INVALID_STATE_TRANSITION |
      | Sync Session | COMPLETED | CMD-SYN-OPEN | SYNC_SESSION_INVALID_STATE_TRANSITION |
      | Sync Session | COMPLETED | CMD-SYN-UPLOAD-BATCH | SYNC_SESSION_INVALID_STATE_TRANSITION |
      | Sync Session | COMPLETED_WITH_CONFLICTS | CMD-SYN-OPEN | SYNC_SESSION_INVALID_STATE_TRANSITION |
      | Sync Session | COMPLETED_WITH_CONFLICTS | CMD-SYN-UPLOAD-BATCH | SYNC_SESSION_INVALID_STATE_TRANSITION |
      | Sync Session | FAILED | CMD-SYN-OPEN | SYNC_SESSION_INVALID_STATE_TRANSITION |
      | Sync Session | FAILED | CMD-SYN-UPLOAD-BATCH | SYNC_SESSION_INVALID_STATE_TRANSITION |
      | Sync Session | REJECTED | CMD-SYN-OPEN | SYNC_SESSION_INVALID_STATE_TRANSITION |
      | Sync Session | REJECTED | CMD-SYN-UPLOAD-BATCH | SYNC_SESSION_INVALID_STATE_TRANSITION |
```
