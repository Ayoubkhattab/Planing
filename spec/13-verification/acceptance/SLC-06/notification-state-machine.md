---
id: TST-NOTIFICATION-SM
type: acceptance-spec
title: Acceptance — Notification state machine
wave: W6
slice: SLC-06
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-NOTIFICATION
traces:
  verifies:
  - SL-05
  - AGG-NOTIFICATION
  - REQ-COM-001
  - REQ-COM-002
---

# Acceptance — Notification

مولّدة من مصفوفة AGG-NOTIFICATION: 1 انتقالاً مسموحاً، 5 رفضاً.

```gherkin
Feature: Notification lifecycle (AGG-NOTIFICATION)

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
      | Notification | SENT | CMD-NTF-MARK-READ | READ | EVT-NTF-READ | 3 |

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
      | Notification | QUEUED | CMD-NTF-MARK-READ | NOTIFICATION_INVALID_STATE_TRANSITION |
      | Notification | READ | CMD-NTF-MARK-READ | NOTIFICATION_INVALID_STATE_TRANSITION |
      | Notification | FAILED | CMD-NTF-MARK-READ | NOTIFICATION_INVALID_STATE_TRANSITION |
      | Notification | WITHHELD | CMD-NTF-MARK-READ | NOTIFICATION_INVALID_STATE_TRANSITION |
      | Notification | EXPIRED | CMD-NTF-MARK-READ | NOTIFICATION_INVALID_STATE_TRANSITION |
```
