---
id: TST-PROJECTION-VERSION-SM
type: acceptance-spec
title: Acceptance — Projection Version state machine
wave: W6
slice: SLC-05
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-PROJECTION-VERSION
traces:
  verifies:
  - SL-05
  - AGG-PROJECTION-VERSION
  - REQ-SRC-004
---

# Acceptance — Projection Version

مولّدة من مصفوفة AGG-PROJECTION-VERSION: 5 انتقالاً مسموحاً، 19 رفضاً.

```gherkin
Feature: Projection Version lifecycle (AGG-PROJECTION-VERSION)

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
      | Projection Version | BUILDING | CMD-PRJ-CANCEL-BUILD | FAILED | EVT-PRJ-FAILED | 3 |
      | Projection Version | READY | CMD-PRJ-PROMOTE | ACTIVE | EVT-PRJ-PROMOTED | 3 |
      | Projection Version | READY | CMD-PRJ-RETIRE | RETIRED | EVT-PRJ-RETIRED | 3 |
      | Projection Version | ACTIVE | CMD-PRJ-RETIRE | RETIRED | EVT-PRJ-RETIRED | 3 |
      | Projection Version | DEGRADED | CMD-PRJ-RETIRE | RETIRED | EVT-PRJ-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Projection Version | CMD-PRJ-CREATE-VERSION | BUILDING | EVT-PRJ-BUILD-STARTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Projection Version | BUILDING | CMD-PRJ-CREATE-VERSION | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | BUILDING | CMD-PRJ-PROMOTE | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | BUILDING | CMD-PRJ-RETIRE | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | READY | CMD-PRJ-CREATE-VERSION | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | READY | CMD-PRJ-CANCEL-BUILD | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | ACTIVE | CMD-PRJ-CREATE-VERSION | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | ACTIVE | CMD-PRJ-PROMOTE | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | ACTIVE | CMD-PRJ-CANCEL-BUILD | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | DEGRADED | CMD-PRJ-CREATE-VERSION | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | DEGRADED | CMD-PRJ-PROMOTE | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | DEGRADED | CMD-PRJ-CANCEL-BUILD | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | FAILED | CMD-PRJ-CREATE-VERSION | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | FAILED | CMD-PRJ-PROMOTE | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | FAILED | CMD-PRJ-RETIRE | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | FAILED | CMD-PRJ-CANCEL-BUILD | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | RETIRED | CMD-PRJ-CREATE-VERSION | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | RETIRED | CMD-PRJ-PROMOTE | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | RETIRED | CMD-PRJ-RETIRE | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
      | Projection Version | RETIRED | CMD-PRJ-CANCEL-BUILD | PROJECTION_VERSION_INVALID_STATE_TRANSITION |
```
