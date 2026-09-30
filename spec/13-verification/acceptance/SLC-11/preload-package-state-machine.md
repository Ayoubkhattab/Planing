---
id: TST-PRELOAD-PACKAGE-SM
type: acceptance-spec
title: Acceptance — Preload Package state machine
wave: W6
slice: SLC-11
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-PRELOAD-PACKAGE
traces:
  verifies:
  - SL-05
  - AGG-PRELOAD-PACKAGE
  - REQ-OFF-002
  - REQ-OFF-005
---

# Acceptance — Preload Package

مولّدة من مصفوفة AGG-PRELOAD-PACKAGE: 5 انتقالاً مسموحاً، 13 رفضاً.

```gherkin
Feature: Preload Package lifecycle (AGG-PRELOAD-PACKAGE)

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
      | Preload Package | REQUESTED | CMD-PKG-REVOKE | REVOKED | EVT-PKG-REVOKED | 3 |
      | Preload Package | BUILDING | CMD-PKG-REVOKE | REVOKED | EVT-PKG-REVOKED | 3 |
      | Preload Package | READY | CMD-PKG-CONFIRM-DOWNLOAD | DOWNLOADED | EVT-PKG-DOWNLOADED | 3 |
      | Preload Package | READY | CMD-PKG-REVOKE | REVOKED | EVT-PKG-REVOKED | 3 |
      | Preload Package | DOWNLOADED | CMD-PKG-REVOKE | REVOKED | EVT-PKG-REVOKED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Preload Package | CMD-PKG-REQUEST | REQUESTED | EVT-PKG-REQUESTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Preload Package | REQUESTED | CMD-PKG-REQUEST | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | REQUESTED | CMD-PKG-CONFIRM-DOWNLOAD | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | BUILDING | CMD-PKG-REQUEST | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | BUILDING | CMD-PKG-CONFIRM-DOWNLOAD | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | READY | CMD-PKG-REQUEST | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | DOWNLOADED | CMD-PKG-REQUEST | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | DOWNLOADED | CMD-PKG-CONFIRM-DOWNLOAD | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | EXPIRED | CMD-PKG-REQUEST | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | EXPIRED | CMD-PKG-CONFIRM-DOWNLOAD | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | EXPIRED | CMD-PKG-REVOKE | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | REVOKED | CMD-PKG-REQUEST | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | REVOKED | CMD-PKG-CONFIRM-DOWNLOAD | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
      | Preload Package | REVOKED | CMD-PKG-REVOKE | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
```
