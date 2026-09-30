---
id: TST-SYNC-CONFLICT-SM
type: acceptance-spec
title: Acceptance — Sync Conflict state machine
wave: W6
slice: SLC-11
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-SYNC-CONFLICT
traces:
  verifies:
  - SL-05
  - AGG-SYNC-CONFLICT
  - REQ-OFF-004
---

# Acceptance — Sync Conflict

مولّدة من مصفوفة AGG-SYNC-CONFLICT: 4 انتقالاً مسموحاً، 12 رفضاً.

```gherkin
Feature: Sync Conflict lifecycle (AGG-SYNC-CONFLICT)

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
      | Sync Conflict | OPEN | CMD-SCF-ASSIGN | OPEN | EVT-SCF-ASSIGNED | 3 |
      | Sync Conflict | OPEN | CMD-SCF-REAPPLY | RESOLVED_APPLIED | EVT-SCF-REAPPLIED | 3 |
      | Sync Conflict | OPEN | CMD-SCF-DISCARD | RESOLVED_DISCARDED | EVT-SCF-DISCARDED | 3 |
      | Sync Conflict | OPEN | CMD-SCF-RESOLVE-MANUALLY | RESOLVED_MANUAL | EVT-SCF-RESOLVED-MANUALLY | 3 |

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
      | Sync Conflict | RESOLVED_APPLIED | CMD-SCF-ASSIGN | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_APPLIED | CMD-SCF-REAPPLY | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_APPLIED | CMD-SCF-DISCARD | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_APPLIED | CMD-SCF-RESOLVE-MANUALLY | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_DISCARDED | CMD-SCF-ASSIGN | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_DISCARDED | CMD-SCF-REAPPLY | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_DISCARDED | CMD-SCF-DISCARD | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_DISCARDED | CMD-SCF-RESOLVE-MANUALLY | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_MANUAL | CMD-SCF-ASSIGN | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_MANUAL | CMD-SCF-REAPPLY | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_MANUAL | CMD-SCF-DISCARD | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
      | Sync Conflict | RESOLVED_MANUAL | CMD-SCF-RESOLVE-MANUALLY | SYNC_CONFLICT_INVALID_STATE_TRANSITION |
```
