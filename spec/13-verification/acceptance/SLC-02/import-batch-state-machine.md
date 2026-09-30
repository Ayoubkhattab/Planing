---
id: TST-IMPORT-BATCH-SM
type: acceptance-spec
title: Acceptance — Import Batch state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-IMPORT-BATCH
traces:
  verifies:
  - SL-05
  - AGG-IMPORT-BATCH
  - REQ-INF-005
  - REQ-INF-006
  - REQ-INF-007
  - REQ-INF-008
  - REQ-INF-009
---

# Acceptance — Import Batch

مولّدة من مصفوفة AGG-IMPORT-BATCH: 3 انتقالاً مسموحاً، 21 رفضاً، 4 انتقالاً نظامياً (SYS).

```gherkin
Feature: Import Batch lifecycle (AGG-IMPORT-BATCH)

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
      | Import Batch | RECEIVED | CMD-IMP-CANCEL | CANCELLED | EVT-IMP-CANCELLED | 3 |
      | Import Batch | COMPLETED_WITH_QUARANTINE | CMD-IMP-REPROCESS-QUARANTINE | PROCESSING | EVT-IMP-REPROCESSING | 3 |
      | Import Batch | COMPLETED_WITH_QUARANTINE | CMD-IMP-ACCEPT-QUARANTINE | COMPLETED | EVT-IMP-QUARANTINE-ACCEPTED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Import Batch | CMD-IMP-SUBMIT | RECEIVED | EVT-IMP-RECEIVED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Import Batch | RECEIVED | CMD-IMP-SUBMIT | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | RECEIVED | CMD-IMP-REPROCESS-QUARANTINE | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | RECEIVED | CMD-IMP-ACCEPT-QUARANTINE | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | PROCESSING | CMD-IMP-SUBMIT | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | PROCESSING | CMD-IMP-REPROCESS-QUARANTINE | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | PROCESSING | CMD-IMP-ACCEPT-QUARANTINE | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | PROCESSING | CMD-IMP-CANCEL | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | COMPLETED | CMD-IMP-SUBMIT | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | COMPLETED | CMD-IMP-REPROCESS-QUARANTINE | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | COMPLETED | CMD-IMP-ACCEPT-QUARANTINE | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | COMPLETED | CMD-IMP-CANCEL | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | COMPLETED_WITH_QUARANTINE | CMD-IMP-SUBMIT | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | COMPLETED_WITH_QUARANTINE | CMD-IMP-CANCEL | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | FAILED | CMD-IMP-SUBMIT | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | FAILED | CMD-IMP-REPROCESS-QUARANTINE | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | FAILED | CMD-IMP-ACCEPT-QUARANTINE | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | FAILED | CMD-IMP-CANCEL | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | CANCELLED | CMD-IMP-SUBMIT | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | CANCELLED | CMD-IMP-REPROCESS-QUARANTINE | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | CANCELLED | CMD-IMP-ACCEPT-QUARANTINE | IMPORT_BATCH_INVALID_STATE_TRANSITION |
      | Import Batch | CANCELLED | CMD-IMP-CANCEL | IMPORT_BATCH_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Import Batch | RECEIVED | processing started | PROCESSING | EVT-IMP-PROCESSING-STARTED |
      | Import Batch | PROCESSING | all records applied | COMPLETED | EVT-IMP-COMPLETED |
      | Import Batch | PROCESSING | finished with invalid records | COMPLETED_WITH_QUARANTINE | EVT-IMP-COMPLETED-WITH-QUARANTINE |
      | Import Batch | PROCESSING | unrecoverable error | FAILED | EVT-IMP-FAILED |
```
