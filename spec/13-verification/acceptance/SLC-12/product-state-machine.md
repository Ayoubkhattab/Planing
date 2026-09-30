---
id: TST-PRODUCT-SM
type: acceptance-spec
title: Acceptance — Product Version state machine
wave: W6
slice: SLC-12
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-PRODUCT
traces:
  verifies:
  - SL-05
  - AGG-PRODUCT
  - REQ-PRD-001
  - REQ-PRD-002
  - REQ-PRD-003
---

# Acceptance — Product Version

مولّدة من مصفوفة AGG-PRODUCT: 11 انتقالاً مسموحاً، 61 رفضاً.

```gherkin
Feature: Product Version lifecycle (AGG-PRODUCT)

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
      | Product Version | DRAFT | CMD-PRD-GENERATE | GENERATING | EVT-PRD-GENERATION-STARTED | 3 |
      | Product Version | DRAFT | CMD-PRD-DISCARD | DISCARDED | EVT-PRD-DISCARDED | 3 |
      | Product Version | GENERATED | CMD-PRD-GENERATE | GENERATING | EVT-PRD-GENERATION-STARTED | 3 |
      | Product Version | GENERATED | CMD-PRD-EDIT-NARRATIVE | GENERATED | EVT-PRD-NARRATIVE-EDITED | 3 |
      | Product Version | GENERATED | CMD-PRD-SUBMIT | IN_REVIEW | EVT-PRD-SUBMITTED | 3 |
      | Product Version | GENERATED | CMD-PRD-DISCARD | DISCARDED | EVT-PRD-DISCARDED | 3 |
      | Product Version | GENERATION_FAILED | CMD-PRD-GENERATE | GENERATING | EVT-PRD-GENERATION-STARTED | 3 |
      | Product Version | GENERATION_FAILED | CMD-PRD-DISCARD | DISCARDED | EVT-PRD-DISCARDED | 3 |
      | Product Version | IN_REVIEW | CMD-PRD-RETURN | GENERATED | EVT-PRD-RETURNED | 3 |
      | Product Version | IN_REVIEW | CMD-PRD-APPROVE | APPROVED | EVT-PRD-APPROVED | 3 |
      | Product Version | APPROVED | CMD-PRD-WITHDRAW | WITHDRAWN | EVT-PRD-WITHDRAWN | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Product Version | CMD-PRD-CREATE | DRAFT | EVT-PRD-CREATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Product Version | DRAFT | CMD-PRD-CREATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DRAFT | CMD-PRD-EDIT-NARRATIVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DRAFT | CMD-PRD-SUBMIT | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DRAFT | CMD-PRD-RETURN | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DRAFT | CMD-PRD-APPROVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DRAFT | CMD-PRD-WITHDRAW | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATING | CMD-PRD-CREATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATING | CMD-PRD-GENERATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATING | CMD-PRD-EDIT-NARRATIVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATING | CMD-PRD-SUBMIT | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATING | CMD-PRD-RETURN | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATING | CMD-PRD-APPROVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATING | CMD-PRD-WITHDRAW | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATING | CMD-PRD-DISCARD | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATED | CMD-PRD-CREATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATED | CMD-PRD-RETURN | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATED | CMD-PRD-APPROVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATED | CMD-PRD-WITHDRAW | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATION_FAILED | CMD-PRD-CREATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATION_FAILED | CMD-PRD-EDIT-NARRATIVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATION_FAILED | CMD-PRD-SUBMIT | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATION_FAILED | CMD-PRD-RETURN | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATION_FAILED | CMD-PRD-APPROVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | GENERATION_FAILED | CMD-PRD-WITHDRAW | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | IN_REVIEW | CMD-PRD-CREATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | IN_REVIEW | CMD-PRD-GENERATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | IN_REVIEW | CMD-PRD-EDIT-NARRATIVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | IN_REVIEW | CMD-PRD-SUBMIT | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | IN_REVIEW | CMD-PRD-WITHDRAW | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | IN_REVIEW | CMD-PRD-DISCARD | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | APPROVED | CMD-PRD-CREATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | APPROVED | CMD-PRD-GENERATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | APPROVED | CMD-PRD-EDIT-NARRATIVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | APPROVED | CMD-PRD-SUBMIT | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | APPROVED | CMD-PRD-RETURN | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | APPROVED | CMD-PRD-APPROVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | APPROVED | CMD-PRD-DISCARD | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | SUPERSEDED | CMD-PRD-CREATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | SUPERSEDED | CMD-PRD-GENERATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | SUPERSEDED | CMD-PRD-EDIT-NARRATIVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | SUPERSEDED | CMD-PRD-SUBMIT | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | SUPERSEDED | CMD-PRD-RETURN | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | SUPERSEDED | CMD-PRD-APPROVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | SUPERSEDED | CMD-PRD-WITHDRAW | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | SUPERSEDED | CMD-PRD-DISCARD | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | WITHDRAWN | CMD-PRD-CREATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | WITHDRAWN | CMD-PRD-GENERATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | WITHDRAWN | CMD-PRD-EDIT-NARRATIVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | WITHDRAWN | CMD-PRD-SUBMIT | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | WITHDRAWN | CMD-PRD-RETURN | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | WITHDRAWN | CMD-PRD-APPROVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | WITHDRAWN | CMD-PRD-WITHDRAW | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | WITHDRAWN | CMD-PRD-DISCARD | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DISCARDED | CMD-PRD-CREATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DISCARDED | CMD-PRD-GENERATE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DISCARDED | CMD-PRD-EDIT-NARRATIVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DISCARDED | CMD-PRD-SUBMIT | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DISCARDED | CMD-PRD-RETURN | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DISCARDED | CMD-PRD-APPROVE | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DISCARDED | CMD-PRD-WITHDRAW | PRODUCT_INVALID_STATE_TRANSITION |
      | Product Version | DISCARDED | CMD-PRD-DISCARD | PRODUCT_INVALID_STATE_TRANSITION |
```
