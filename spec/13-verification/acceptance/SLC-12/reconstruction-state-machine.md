---
id: TST-RECONSTRUCTION-SM
type: acceptance-spec
title: Acceptance — Historical Reconstruction state machine
wave: W6
slice: SLC-12
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-RECONSTRUCTION
traces:
  verifies:
  - SL-05
  - AGG-RECONSTRUCTION
  - REQ-ARC-004
---

# Acceptance — Historical Reconstruction

مولّدة من مصفوفة AGG-RECONSTRUCTION: 2 انتقالاً مسموحاً، 8 رفضاً.

```gherkin
Feature: Historical Reconstruction lifecycle (AGG-RECONSTRUCTION)

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
      | Historical Reconstruction | REQUESTED | CMD-REC-CANCEL | CANCELLED | EVT-REC-CANCELLED | 3 |
      | Historical Reconstruction | RUNNING | CMD-REC-CANCEL | CANCELLED | EVT-REC-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Historical Reconstruction | CMD-REC-REQUEST | REQUESTED | EVT-REC-REQUESTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Historical Reconstruction | REQUESTED | CMD-REC-REQUEST | RECONSTRUCTION_INVALID_STATE_TRANSITION |
      | Historical Reconstruction | RUNNING | CMD-REC-REQUEST | RECONSTRUCTION_INVALID_STATE_TRANSITION |
      | Historical Reconstruction | COMPLETED | CMD-REC-REQUEST | RECONSTRUCTION_INVALID_STATE_TRANSITION |
      | Historical Reconstruction | COMPLETED | CMD-REC-CANCEL | RECONSTRUCTION_INVALID_STATE_TRANSITION |
      | Historical Reconstruction | FAILED | CMD-REC-REQUEST | RECONSTRUCTION_INVALID_STATE_TRANSITION |
      | Historical Reconstruction | FAILED | CMD-REC-CANCEL | RECONSTRUCTION_INVALID_STATE_TRANSITION |
      | Historical Reconstruction | CANCELLED | CMD-REC-REQUEST | RECONSTRUCTION_INVALID_STATE_TRANSITION |
      | Historical Reconstruction | CANCELLED | CMD-REC-CANCEL | RECONSTRUCTION_INVALID_STATE_TRANSITION |
```
