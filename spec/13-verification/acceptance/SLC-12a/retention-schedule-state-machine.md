---
id: TST-RETENTION-SCHEDULE-SM
type: acceptance-spec
title: Acceptance — Retention Schedule Version state machine
wave: W6
slice: SLC-12a
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-RETENTION-SCHEDULE
traces:
  verifies:
  - SL-05
  - AGG-RETENTION-SCHEDULE
  - REQ-GOV-006
---

# Acceptance — Retention Schedule Version

مولّدة من مصفوفة AGG-RETENTION-SCHEDULE: 3 انتقالاً مسموحاً، 13 رفضاً.

```gherkin
Feature: Retention Schedule Version lifecycle (AGG-RETENTION-SCHEDULE)

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
      | Retention Schedule Version | DRAFT | CMD-RTS-EDIT | DRAFT | EVT-RTS-EDITED | 3 |
      | Retention Schedule Version | DRAFT | CMD-RTS-ACTIVATE | ACTIVE | EVT-RTS-ACTIVATED | 3 |
      | Retention Schedule Version | DRAFT | CMD-RTS-DISCARD | DISCARDED | EVT-RTS-DISCARDED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Retention Schedule Version | CMD-RTS-DRAFT | DRAFT | EVT-RTS-DRAFTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Retention Schedule Version | DRAFT | CMD-RTS-DRAFT | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | ACTIVE | CMD-RTS-DRAFT | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | ACTIVE | CMD-RTS-EDIT | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | ACTIVE | CMD-RTS-ACTIVATE | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | ACTIVE | CMD-RTS-DISCARD | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | SUPERSEDED | CMD-RTS-DRAFT | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | SUPERSEDED | CMD-RTS-EDIT | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | SUPERSEDED | CMD-RTS-ACTIVATE | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | SUPERSEDED | CMD-RTS-DISCARD | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | DISCARDED | CMD-RTS-DRAFT | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | DISCARDED | CMD-RTS-EDIT | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | DISCARDED | CMD-RTS-ACTIVATE | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
      | Retention Schedule Version | DISCARDED | CMD-RTS-DISCARD | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
```
