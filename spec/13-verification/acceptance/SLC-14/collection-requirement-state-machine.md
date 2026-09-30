---
id: TST-COLLECTION-REQUIREMENT-SM
type: acceptance-spec
title: Acceptance — Collection Requirement state machine
wave: W6
slice: SLC-14
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-COLLECTION-REQUIREMENT
traces:
  verifies:
  - SL-05
  - AGG-COLLECTION-REQUIREMENT
  - REQ-COL-001
  - REQ-COL-003
---

# Acceptance — Collection Requirement

مولّدة من مصفوفة AGG-COLLECTION-REQUIREMENT: 9 انتقالاً مسموحاً، 47 رفضاً، 2 انتقالاً نظامياً (SYS).

```gherkin
Feature: Collection Requirement lifecycle (AGG-COLLECTION-REQUIREMENT)

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
      | Collection Requirement | DRAFT | CMD-CRQ-EDIT | DRAFT | EVT-CRQ-EDITED | 3 |
      | Collection Requirement | DRAFT | CMD-CRQ-SUBMIT | SUBMITTED | EVT-CRQ-SUBMITTED | 3 |
      | Collection Requirement | DRAFT | CMD-CRQ-CANCEL | CANCELLED | EVT-CRQ-CANCELLED | 3 |
      | Collection Requirement | SUBMITTED | CMD-CRQ-APPROVE | APPROVED | EVT-CRQ-APPROVED | 3 |
      | Collection Requirement | SUBMITTED | CMD-CRQ-REJECT | REJECTED | EVT-CRQ-REJECTED | 3 |
      | Collection Requirement | SUBMITTED | CMD-CRQ-CANCEL | CANCELLED | EVT-CRQ-CANCELLED | 3 |
      | Collection Requirement | APPROVED | CMD-CRQ-AMEND | APPROVED | EVT-CRQ-AMENDED | 3 |
      | Collection Requirement | APPROVED | CMD-CRQ-MARK-SATISFIED | SATISFIED | EVT-CRQ-SATISFIED | 3 |
      | Collection Requirement | APPROVED | CMD-CRQ-CANCEL | CANCELLED | EVT-CRQ-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Collection Requirement | CMD-CRQ-DRAFT | DRAFT | EVT-CRQ-DRAFTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Collection Requirement | DRAFT | CMD-CRQ-DRAFT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | DRAFT | CMD-CRQ-APPROVE | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | DRAFT | CMD-CRQ-REJECT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | DRAFT | CMD-CRQ-AMEND | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | DRAFT | CMD-CRQ-MARK-SATISFIED | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SUBMITTED | CMD-CRQ-DRAFT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SUBMITTED | CMD-CRQ-EDIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SUBMITTED | CMD-CRQ-SUBMIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SUBMITTED | CMD-CRQ-AMEND | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SUBMITTED | CMD-CRQ-MARK-SATISFIED | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | APPROVED | CMD-CRQ-DRAFT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | APPROVED | CMD-CRQ-EDIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | APPROVED | CMD-CRQ-SUBMIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | APPROVED | CMD-CRQ-APPROVE | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | APPROVED | CMD-CRQ-REJECT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | REJECTED | CMD-CRQ-DRAFT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | REJECTED | CMD-CRQ-EDIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | REJECTED | CMD-CRQ-SUBMIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | REJECTED | CMD-CRQ-APPROVE | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | REJECTED | CMD-CRQ-REJECT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | REJECTED | CMD-CRQ-AMEND | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | REJECTED | CMD-CRQ-MARK-SATISFIED | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | REJECTED | CMD-CRQ-CANCEL | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SATISFIED | CMD-CRQ-DRAFT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SATISFIED | CMD-CRQ-EDIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SATISFIED | CMD-CRQ-SUBMIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SATISFIED | CMD-CRQ-APPROVE | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SATISFIED | CMD-CRQ-REJECT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SATISFIED | CMD-CRQ-AMEND | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SATISFIED | CMD-CRQ-MARK-SATISFIED | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | SATISFIED | CMD-CRQ-CANCEL | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | EXPIRED | CMD-CRQ-DRAFT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | EXPIRED | CMD-CRQ-EDIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | EXPIRED | CMD-CRQ-SUBMIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | EXPIRED | CMD-CRQ-APPROVE | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | EXPIRED | CMD-CRQ-REJECT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | EXPIRED | CMD-CRQ-AMEND | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | EXPIRED | CMD-CRQ-MARK-SATISFIED | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | EXPIRED | CMD-CRQ-CANCEL | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | CANCELLED | CMD-CRQ-DRAFT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | CANCELLED | CMD-CRQ-EDIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | CANCELLED | CMD-CRQ-SUBMIT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | CANCELLED | CMD-CRQ-APPROVE | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | CANCELLED | CMD-CRQ-REJECT | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | CANCELLED | CMD-CRQ-AMEND | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | CANCELLED | CMD-CRQ-MARK-SATISFIED | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |
      | Collection Requirement | CANCELLED | CMD-CRQ-CANCEL | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Collection Requirement | APPROVED | validated observation matched | APPROVED | EVT-CRQ-FULFILMENT-UPDATED |
      | Collection Requirement | APPROVED | due passed | EXPIRED | EVT-CRQ-EXPIRED |
```
