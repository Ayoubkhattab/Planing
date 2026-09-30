---
id: TST-ASSESSMENT-SM
type: acceptance-spec
title: Acceptance — Assessment Version state machine
wave: W6
slice: SLC-07
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ASSESSMENT
traces:
  verifies:
  - SL-05
  - AGG-ASSESSMENT
  - REQ-ANL-005
  - REQ-ANL-006
  - REQ-ANL-008
---

# Acceptance — Assessment Version

مولّدة من مصفوفة AGG-ASSESSMENT: 6 انتقالاً مسموحاً، 36 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: Assessment Version lifecycle (AGG-ASSESSMENT)

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
      | Assessment Version | DRAFT | CMD-ASM-EDIT | DRAFT | EVT-ASM-EDITED | 3 |
      | Assessment Version | DRAFT | CMD-ASM-SUBMIT | IN_REVIEW | EVT-ASM-SUBMITTED | 3 |
      | Assessment Version | DRAFT | CMD-ASM-DISCARD | DISCARDED | EVT-ASM-DISCARDED | 3 |
      | Assessment Version | IN_REVIEW | CMD-ASM-RETURN | DRAFT | EVT-ASM-RETURNED | 3 |
      | Assessment Version | IN_REVIEW | CMD-ASM-PUBLISH | PUBLISHED | EVT-ASM-PUBLISHED | 3 |
      | Assessment Version | PUBLISHED | CMD-ASM-WITHDRAW | WITHDRAWN | EVT-ASM-WITHDRAWN | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Assessment Version | CMD-ASM-DRAFT | DRAFT | EVT-ASM-DRAFTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Assessment Version | DRAFT | CMD-ASM-DRAFT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | DRAFT | CMD-ASM-RETURN | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | DRAFT | CMD-ASM-PUBLISH | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | DRAFT | CMD-ASM-WITHDRAW | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | IN_REVIEW | CMD-ASM-DRAFT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | IN_REVIEW | CMD-ASM-EDIT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | IN_REVIEW | CMD-ASM-SUBMIT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | IN_REVIEW | CMD-ASM-WITHDRAW | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | IN_REVIEW | CMD-ASM-DISCARD | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | PUBLISHED | CMD-ASM-DRAFT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | PUBLISHED | CMD-ASM-EDIT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | PUBLISHED | CMD-ASM-SUBMIT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | PUBLISHED | CMD-ASM-RETURN | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | PUBLISHED | CMD-ASM-PUBLISH | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | PUBLISHED | CMD-ASM-DISCARD | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | SUPERSEDED | CMD-ASM-DRAFT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | SUPERSEDED | CMD-ASM-EDIT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | SUPERSEDED | CMD-ASM-SUBMIT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | SUPERSEDED | CMD-ASM-RETURN | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | SUPERSEDED | CMD-ASM-PUBLISH | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | SUPERSEDED | CMD-ASM-WITHDRAW | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | SUPERSEDED | CMD-ASM-DISCARD | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | WITHDRAWN | CMD-ASM-DRAFT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | WITHDRAWN | CMD-ASM-EDIT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | WITHDRAWN | CMD-ASM-SUBMIT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | WITHDRAWN | CMD-ASM-RETURN | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | WITHDRAWN | CMD-ASM-PUBLISH | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | WITHDRAWN | CMD-ASM-WITHDRAW | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | WITHDRAWN | CMD-ASM-DISCARD | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | DISCARDED | CMD-ASM-DRAFT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | DISCARDED | CMD-ASM-EDIT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | DISCARDED | CMD-ASM-SUBMIT | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | DISCARDED | CMD-ASM-RETURN | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | DISCARDED | CMD-ASM-PUBLISH | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | DISCARDED | CMD-ASM-WITHDRAW | ASSESSMENT_INVALID_STATE_TRANSITION |
      | Assessment Version | DISCARDED | CMD-ASM-DISCARD | ASSESSMENT_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Assessment Version | PUBLISHED | newer version published | SUPERSEDED | EVT-ASM-SUPERSEDED |
```
