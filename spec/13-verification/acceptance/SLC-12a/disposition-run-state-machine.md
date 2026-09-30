---
id: TST-DISPOSITION-RUN-SM
type: acceptance-spec
title: Acceptance — Disposition Run state machine
wave: W6
slice: SLC-12a
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-DISPOSITION-RUN
traces:
  verifies:
  - SL-05
  - AGG-DISPOSITION-RUN
  - REQ-GOV-006
  - REQ-GOV-007
---

# Acceptance — Disposition Run

مولّدة من مصفوفة AGG-DISPOSITION-RUN: 5 انتقالاً مسموحاً، 16 رفضاً.

```gherkin
Feature: Disposition Run lifecycle (AGG-DISPOSITION-RUN)

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
      | Disposition Run | PLANNED | CMD-DSP-SUBMIT | AWAITING_APPROVAL | EVT-DSP-SUBMITTED | 3 |
      | Disposition Run | PLANNED | CMD-DSP-CANCEL | CANCELLED | EVT-DSP-CANCELLED | 3 |
      | Disposition Run | AWAITING_APPROVAL | CMD-DSP-APPROVE | APPROVED | EVT-DSP-APPROVED | 3 |
      | Disposition Run | AWAITING_APPROVAL | CMD-DSP-CANCEL | CANCELLED | EVT-DSP-CANCELLED | 3 |
      | Disposition Run | APPROVED | CMD-DSP-CANCEL | CANCELLED | EVT-DSP-CANCELLED | 3 |

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
      | Disposition Run | PLANNED | CMD-DSP-APPROVE | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | AWAITING_APPROVAL | CMD-DSP-SUBMIT | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | APPROVED | CMD-DSP-SUBMIT | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | APPROVED | CMD-DSP-APPROVE | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | EXECUTING | CMD-DSP-SUBMIT | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | EXECUTING | CMD-DSP-APPROVE | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | EXECUTING | CMD-DSP-CANCEL | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | COMPLETED | CMD-DSP-SUBMIT | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | COMPLETED | CMD-DSP-APPROVE | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | COMPLETED | CMD-DSP-CANCEL | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | COMPLETED_WITH_EXCEPTIONS | CMD-DSP-SUBMIT | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | COMPLETED_WITH_EXCEPTIONS | CMD-DSP-APPROVE | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | COMPLETED_WITH_EXCEPTIONS | CMD-DSP-CANCEL | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | CANCELLED | CMD-DSP-SUBMIT | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | CANCELLED | CMD-DSP-APPROVE | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
      | Disposition Run | CANCELLED | CMD-DSP-CANCEL | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
```
