---
id: TST-USER-SM
type: acceptance-spec
title: Acceptance — User Account state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-USER
traces:
  verifies:
  - SL-05
  - AGG-USER
  - REQ-FND-005
  - REQ-FND-006
---

# Acceptance — User Account

مولّدة من مصفوفة AGG-USER: 20 انتقالاً مسموحاً، 30 رفضاً.

```gherkin
Feature: User Account lifecycle (AGG-USER)

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
      | User Account | PENDING | CMD-USR-LINK-IDENTITY | PENDING | EVT-USR-IDENTITY-LINKED | 3 |
      | User Account | PENDING | CMD-USR-UNLINK-IDENTITY | PENDING | EVT-USR-IDENTITY-UNLINKED | 3 |
      | User Account | PENDING | CMD-USR-LINK-PERSON | PENDING | EVT-USR-PERSON-LINKED | 3 |
      | User Account | PENDING | CMD-USR-RECORD-FIRST-SIGN-IN | ACTIVE | EVT-USR-ACTIVATED | 3 |
      | User Account | PENDING | CMD-USR-DISABLE | DISABLED | EVT-USR-DISABLED | 3 |
      | User Account | ACTIVE | CMD-USR-LINK-IDENTITY | ACTIVE | EVT-USR-IDENTITY-LINKED | 3 |
      | User Account | ACTIVE | CMD-USR-UNLINK-IDENTITY | ACTIVE | EVT-USR-IDENTITY-UNLINKED | 3 |
      | User Account | ACTIVE | CMD-USR-LINK-PERSON | ACTIVE | EVT-USR-PERSON-LINKED | 3 |
      | User Account | ACTIVE | CMD-USR-LOCK | LOCKED | EVT-USR-LOCKED | 3 |
      | User Account | ACTIVE | CMD-USR-DISABLE | DISABLED | EVT-USR-DISABLED | 3 |
      | User Account | LOCKED | CMD-USR-LINK-IDENTITY | LOCKED | EVT-USR-IDENTITY-LINKED | 3 |
      | User Account | LOCKED | CMD-USR-UNLINK-IDENTITY | LOCKED | EVT-USR-IDENTITY-UNLINKED | 3 |
      | User Account | LOCKED | CMD-USR-LINK-PERSON | LOCKED | EVT-USR-PERSON-LINKED | 3 |
      | User Account | LOCKED | CMD-USR-UNLOCK | ACTIVE | EVT-USR-UNLOCKED | 3 |
      | User Account | LOCKED | CMD-USR-DISABLE | DISABLED | EVT-USR-DISABLED | 3 |
      | User Account | DISABLED | CMD-USR-LINK-IDENTITY | DISABLED | EVT-USR-IDENTITY-LINKED | 3 |
      | User Account | DISABLED | CMD-USR-UNLINK-IDENTITY | DISABLED | EVT-USR-IDENTITY-UNLINKED | 3 |
      | User Account | DISABLED | CMD-USR-LINK-PERSON | DISABLED | EVT-USR-PERSON-LINKED | 3 |
      | User Account | DISABLED | CMD-USR-ENABLE | ACTIVE | EVT-USR-ENABLED | 3 |
      | User Account | DISABLED | CMD-USR-CLOSE | CLOSED | EVT-USR-CLOSED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | User Account | CMD-USR-PROVISION | PENDING | EVT-USR-PROVISIONED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | User Account | PENDING | CMD-USR-PROVISION | USER_INVALID_STATE_TRANSITION |
      | User Account | PENDING | CMD-USR-LOCK | USER_INVALID_STATE_TRANSITION |
      | User Account | PENDING | CMD-USR-UNLOCK | USER_INVALID_STATE_TRANSITION |
      | User Account | PENDING | CMD-USR-ENABLE | USER_INVALID_STATE_TRANSITION |
      | User Account | PENDING | CMD-USR-CLOSE | USER_INVALID_STATE_TRANSITION |
      | User Account | ACTIVE | CMD-USR-PROVISION | USER_INVALID_STATE_TRANSITION |
      | User Account | ACTIVE | CMD-USR-RECORD-FIRST-SIGN-IN | USER_INVALID_STATE_TRANSITION |
      | User Account | ACTIVE | CMD-USR-UNLOCK | USER_INVALID_STATE_TRANSITION |
      | User Account | ACTIVE | CMD-USR-ENABLE | USER_INVALID_STATE_TRANSITION |
      | User Account | ACTIVE | CMD-USR-CLOSE | USER_INVALID_STATE_TRANSITION |
      | User Account | LOCKED | CMD-USR-PROVISION | USER_INVALID_STATE_TRANSITION |
      | User Account | LOCKED | CMD-USR-RECORD-FIRST-SIGN-IN | USER_INVALID_STATE_TRANSITION |
      | User Account | LOCKED | CMD-USR-LOCK | USER_INVALID_STATE_TRANSITION |
      | User Account | LOCKED | CMD-USR-ENABLE | USER_INVALID_STATE_TRANSITION |
      | User Account | LOCKED | CMD-USR-CLOSE | USER_INVALID_STATE_TRANSITION |
      | User Account | DISABLED | CMD-USR-PROVISION | USER_INVALID_STATE_TRANSITION |
      | User Account | DISABLED | CMD-USR-RECORD-FIRST-SIGN-IN | USER_INVALID_STATE_TRANSITION |
      | User Account | DISABLED | CMD-USR-LOCK | USER_INVALID_STATE_TRANSITION |
      | User Account | DISABLED | CMD-USR-UNLOCK | USER_INVALID_STATE_TRANSITION |
      | User Account | DISABLED | CMD-USR-DISABLE | USER_INVALID_STATE_TRANSITION |
      | User Account | CLOSED | CMD-USR-PROVISION | USER_INVALID_STATE_TRANSITION |
      | User Account | CLOSED | CMD-USR-LINK-IDENTITY | USER_INVALID_STATE_TRANSITION |
      | User Account | CLOSED | CMD-USR-UNLINK-IDENTITY | USER_INVALID_STATE_TRANSITION |
      | User Account | CLOSED | CMD-USR-LINK-PERSON | USER_INVALID_STATE_TRANSITION |
      | User Account | CLOSED | CMD-USR-RECORD-FIRST-SIGN-IN | USER_INVALID_STATE_TRANSITION |
      | User Account | CLOSED | CMD-USR-LOCK | USER_INVALID_STATE_TRANSITION |
      | User Account | CLOSED | CMD-USR-UNLOCK | USER_INVALID_STATE_TRANSITION |
      | User Account | CLOSED | CMD-USR-DISABLE | USER_INVALID_STATE_TRANSITION |
      | User Account | CLOSED | CMD-USR-ENABLE | USER_INVALID_STATE_TRANSITION |
      | User Account | CLOSED | CMD-USR-CLOSE | USER_INVALID_STATE_TRANSITION |
```
