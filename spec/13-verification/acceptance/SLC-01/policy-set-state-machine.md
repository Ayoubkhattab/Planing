---
id: TST-POLICY-SET-SM
type: acceptance-spec
title: Acceptance — Policy Set Version state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-POLICY-SET
traces:
  verifies:
  - SL-05
  - AGG-POLICY-SET
  - REQ-FND-011
  - REQ-FND-012
  - REQ-GOV-009
---

# Acceptance — Policy Set Version

مولّدة من مصفوفة AGG-POLICY-SET: 4 انتقالاً مسموحاً، 26 رفضاً، 2 انتقالاً نظامياً (SYS).

```gherkin
Feature: Policy Set Version lifecycle (AGG-POLICY-SET)

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
      | Policy Set Version | DRAFT | CMD-POL-EDIT | DRAFT | EVT-POL-EDITED | 3 |
      | Policy Set Version | DRAFT | CMD-POL-SUBMIT | IN_REVIEW | EVT-POL-SUBMITTED | 3 |
      | Policy Set Version | IN_REVIEW | CMD-POL-APPROVE | APPROVED | EVT-POL-APPROVED | 3 |
      | Policy Set Version | IN_REVIEW | CMD-POL-REJECT | REJECTED | EVT-POL-REJECTED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Policy Set Version | CMD-POL-DRAFT | DRAFT | EVT-POL-DRAFTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Policy Set Version | DRAFT | CMD-POL-DRAFT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | DRAFT | CMD-POL-APPROVE | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | DRAFT | CMD-POL-REJECT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | IN_REVIEW | CMD-POL-DRAFT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | IN_REVIEW | CMD-POL-EDIT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | IN_REVIEW | CMD-POL-SUBMIT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | APPROVED | CMD-POL-DRAFT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | APPROVED | CMD-POL-EDIT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | APPROVED | CMD-POL-SUBMIT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | APPROVED | CMD-POL-APPROVE | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | APPROVED | CMD-POL-REJECT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | ACTIVE | CMD-POL-DRAFT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | ACTIVE | CMD-POL-EDIT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | ACTIVE | CMD-POL-SUBMIT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | ACTIVE | CMD-POL-APPROVE | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | ACTIVE | CMD-POL-REJECT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | SUPERSEDED | CMD-POL-DRAFT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | SUPERSEDED | CMD-POL-EDIT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | SUPERSEDED | CMD-POL-SUBMIT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | SUPERSEDED | CMD-POL-APPROVE | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | SUPERSEDED | CMD-POL-REJECT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | REJECTED | CMD-POL-DRAFT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | REJECTED | CMD-POL-EDIT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | REJECTED | CMD-POL-SUBMIT | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | REJECTED | CMD-POL-APPROVE | POLICY_SET_INVALID_STATE_TRANSITION |
      | Policy Set Version | REJECTED | CMD-POL-REJECT | POLICY_SET_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Policy Set Version | APPROVED | effective_from reached | ACTIVE | EVT-POL-ACTIVATED |
      | Policy Set Version | ACTIVE | successor activated | SUPERSEDED | EVT-POL-SUPERSEDED |
```
