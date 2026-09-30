---
id: TST-KNOWLEDGE-OBJECT-SM
type: acceptance-spec
title: Acceptance — Knowledge Object Version state machine
wave: W6
slice: SLC-12
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-KNOWLEDGE-OBJECT
traces:
  verifies:
  - SL-05
  - AGG-KNOWLEDGE-OBJECT
  - REQ-KNW-001
  - REQ-KNW-002
  - REQ-KNW-003
---

# Acceptance — Knowledge Object Version

مولّدة من مصفوفة AGG-KNOWLEDGE-OBJECT: 8 انتقالاً مسموحاً، 55 رفضاً.

```gherkin
Feature: Knowledge Object Version lifecycle (AGG-KNOWLEDGE-OBJECT)

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
      | Knowledge Object Version | DRAFT | CMD-KNO-EDIT | DRAFT | EVT-KNO-EDITED | 3 |
      | Knowledge Object Version | DRAFT | CMD-KNO-SUBMIT | IN_REVIEW | EVT-KNO-SUBMITTED | 3 |
      | Knowledge Object Version | DRAFT | CMD-KNO-DISCARD | DISCARDED | EVT-KNO-DISCARDED | 3 |
      | Knowledge Object Version | IN_REVIEW | CMD-KNO-RETURN | DRAFT | EVT-KNO-RETURNED | 3 |
      | Knowledge Object Version | IN_REVIEW | CMD-KNO-PUBLISH | PUBLISHED | EVT-KNO-PUBLISHED | 3 |
      | Knowledge Object Version | IN_REVIEW | CMD-KNO-REJECT | REJECTED | EVT-KNO-REJECTED | 3 |
      | Knowledge Object Version | PUBLISHED | CMD-KNO-RECORD-REUSE | PUBLISHED | EVT-KNO-REUSED | 3 |
      | Knowledge Object Version | PUBLISHED | CMD-KNO-RETIRE | RETIRED | EVT-KNO-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Knowledge Object Version | CMD-KNO-DRAFT | DRAFT | EVT-KNO-DRAFTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Knowledge Object Version | DRAFT | CMD-KNO-DRAFT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DRAFT | CMD-KNO-RETURN | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DRAFT | CMD-KNO-PUBLISH | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DRAFT | CMD-KNO-REJECT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DRAFT | CMD-KNO-RECORD-REUSE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DRAFT | CMD-KNO-RETIRE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | IN_REVIEW | CMD-KNO-DRAFT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | IN_REVIEW | CMD-KNO-EDIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | IN_REVIEW | CMD-KNO-SUBMIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | IN_REVIEW | CMD-KNO-RECORD-REUSE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | IN_REVIEW | CMD-KNO-RETIRE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | IN_REVIEW | CMD-KNO-DISCARD | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | PUBLISHED | CMD-KNO-DRAFT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | PUBLISHED | CMD-KNO-EDIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | PUBLISHED | CMD-KNO-SUBMIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | PUBLISHED | CMD-KNO-RETURN | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | PUBLISHED | CMD-KNO-PUBLISH | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | PUBLISHED | CMD-KNO-REJECT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | PUBLISHED | CMD-KNO-DISCARD | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | REJECTED | CMD-KNO-DRAFT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | REJECTED | CMD-KNO-EDIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | REJECTED | CMD-KNO-SUBMIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | REJECTED | CMD-KNO-RETURN | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | REJECTED | CMD-KNO-PUBLISH | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | REJECTED | CMD-KNO-REJECT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | REJECTED | CMD-KNO-RECORD-REUSE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | REJECTED | CMD-KNO-RETIRE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | REJECTED | CMD-KNO-DISCARD | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | SUPERSEDED | CMD-KNO-DRAFT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | SUPERSEDED | CMD-KNO-EDIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | SUPERSEDED | CMD-KNO-SUBMIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | SUPERSEDED | CMD-KNO-RETURN | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | SUPERSEDED | CMD-KNO-PUBLISH | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | SUPERSEDED | CMD-KNO-REJECT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | SUPERSEDED | CMD-KNO-RECORD-REUSE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | SUPERSEDED | CMD-KNO-RETIRE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | SUPERSEDED | CMD-KNO-DISCARD | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | RETIRED | CMD-KNO-DRAFT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | RETIRED | CMD-KNO-EDIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | RETIRED | CMD-KNO-SUBMIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | RETIRED | CMD-KNO-RETURN | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | RETIRED | CMD-KNO-PUBLISH | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | RETIRED | CMD-KNO-REJECT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | RETIRED | CMD-KNO-RECORD-REUSE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | RETIRED | CMD-KNO-RETIRE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | RETIRED | CMD-KNO-DISCARD | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DISCARDED | CMD-KNO-DRAFT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DISCARDED | CMD-KNO-EDIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DISCARDED | CMD-KNO-SUBMIT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DISCARDED | CMD-KNO-RETURN | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DISCARDED | CMD-KNO-PUBLISH | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DISCARDED | CMD-KNO-REJECT | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DISCARDED | CMD-KNO-RECORD-REUSE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DISCARDED | CMD-KNO-RETIRE | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
      | Knowledge Object Version | DISCARDED | CMD-KNO-DISCARD | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
```
