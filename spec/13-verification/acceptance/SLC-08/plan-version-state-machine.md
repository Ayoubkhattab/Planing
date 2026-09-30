---
id: TST-PLAN-VERSION-SM
type: acceptance-spec
title: Acceptance — Plan Version state machine
wave: W6
slice: SLC-08
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-PLAN-VERSION
traces:
  verifies:
  - SL-05
  - AGG-PLAN-VERSION
  - REQ-OPS-001
  - REQ-OPS-003
  - REQ-OPS-004
  - REQ-OPS-005
  - REQ-OPS-014
---

# Acceptance — Plan Version

مولّدة من مصفوفة AGG-PLAN-VERSION: 7 انتقالاً مسموحاً، 41 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: Plan Version lifecycle (AGG-PLAN-VERSION)

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
      | Plan Version | DRAFT | CMD-PLV-EDIT | DRAFT | EVT-PLV-EDITED | 3 |
      | Plan Version | DRAFT | CMD-PLV-SUBMIT | IN_REVIEW | EVT-PLV-SUBMITTED | 3 |
      | Plan Version | DRAFT | CMD-PLV-DISCARD | DISCARDED | EVT-PLV-DISCARDED | 3 |
      | Plan Version | IN_REVIEW | CMD-PLV-RETURN | DRAFT | EVT-PLV-RETURNED | 3 |
      | Plan Version | IN_REVIEW | CMD-PLV-APPROVE | BASELINED | EVT-PLV-BASELINED | 3 |
      | Plan Version | IN_REVIEW | CMD-PLV-REJECT | REJECTED | EVT-PLV-REJECTED | 3 |
      | Plan Version | BASELINED | CMD-PLV-AMEND-MINOR | BASELINED | EVT-PLV-MINOR-AMENDED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Plan Version | CMD-PLV-DRAFT | DRAFT | EVT-PLV-DRAFTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Plan Version | DRAFT | CMD-PLV-DRAFT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DRAFT | CMD-PLV-RETURN | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DRAFT | CMD-PLV-APPROVE | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DRAFT | CMD-PLV-REJECT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DRAFT | CMD-PLV-AMEND-MINOR | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | IN_REVIEW | CMD-PLV-DRAFT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | IN_REVIEW | CMD-PLV-EDIT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | IN_REVIEW | CMD-PLV-SUBMIT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | IN_REVIEW | CMD-PLV-AMEND-MINOR | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | IN_REVIEW | CMD-PLV-DISCARD | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | BASELINED | CMD-PLV-DRAFT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | BASELINED | CMD-PLV-EDIT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | BASELINED | CMD-PLV-SUBMIT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | BASELINED | CMD-PLV-RETURN | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | BASELINED | CMD-PLV-APPROVE | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | BASELINED | CMD-PLV-REJECT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | BASELINED | CMD-PLV-DISCARD | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | SUPERSEDED | CMD-PLV-DRAFT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | SUPERSEDED | CMD-PLV-EDIT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | SUPERSEDED | CMD-PLV-SUBMIT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | SUPERSEDED | CMD-PLV-RETURN | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | SUPERSEDED | CMD-PLV-APPROVE | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | SUPERSEDED | CMD-PLV-REJECT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | SUPERSEDED | CMD-PLV-AMEND-MINOR | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | SUPERSEDED | CMD-PLV-DISCARD | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | REJECTED | CMD-PLV-DRAFT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | REJECTED | CMD-PLV-EDIT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | REJECTED | CMD-PLV-SUBMIT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | REJECTED | CMD-PLV-RETURN | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | REJECTED | CMD-PLV-APPROVE | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | REJECTED | CMD-PLV-REJECT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | REJECTED | CMD-PLV-AMEND-MINOR | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | REJECTED | CMD-PLV-DISCARD | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DISCARDED | CMD-PLV-DRAFT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DISCARDED | CMD-PLV-EDIT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DISCARDED | CMD-PLV-SUBMIT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DISCARDED | CMD-PLV-RETURN | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DISCARDED | CMD-PLV-APPROVE | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DISCARDED | CMD-PLV-REJECT | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DISCARDED | CMD-PLV-AMEND-MINOR | PLAN_VERSION_INVALID_STATE_TRANSITION |
      | Plan Version | DISCARDED | CMD-PLV-DISCARD | PLAN_VERSION_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Plan Version | BASELINED | newer version baselined | SUPERSEDED | EVT-PLV-SUPERSEDED |
```
