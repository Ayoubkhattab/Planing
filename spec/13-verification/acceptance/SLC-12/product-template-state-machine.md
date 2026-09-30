---
id: TST-PRODUCT-TEMPLATE-SM
type: acceptance-spec
title: Acceptance — Product Template state machine
wave: W6
slice: SLC-12
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-PRODUCT-TEMPLATE
traces:
  verifies:
  - SL-05
  - AGG-PRODUCT-TEMPLATE
  - REQ-PRD-001
---

# Acceptance — Product Template

مولّدة من مصفوفة AGG-PRODUCT-TEMPLATE: 4 انتقالاً مسموحاً، 8 رفضاً.

```gherkin
Feature: Product Template lifecycle (AGG-PRODUCT-TEMPLATE)

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
      | Product Template | DRAFT | CMD-PTM-EDIT | DRAFT | EVT-PTM-EDITED | 3 |
      | Product Template | DRAFT | CMD-PTM-ACTIVATE | ACTIVE | EVT-PTM-ACTIVATED | 3 |
      | Product Template | ACTIVE | CMD-PTM-EDIT | ACTIVE | EVT-PTM-EDITED | 3 |
      | Product Template | ACTIVE | CMD-PTM-RETIRE | RETIRED | EVT-PTM-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Product Template | CMD-PTM-DEFINE | DRAFT | EVT-PTM-DEFINED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Product Template | DRAFT | CMD-PTM-DEFINE | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION |
      | Product Template | DRAFT | CMD-PTM-RETIRE | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION |
      | Product Template | ACTIVE | CMD-PTM-DEFINE | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION |
      | Product Template | ACTIVE | CMD-PTM-ACTIVATE | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION |
      | Product Template | RETIRED | CMD-PTM-DEFINE | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION |
      | Product Template | RETIRED | CMD-PTM-EDIT | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION |
      | Product Template | RETIRED | CMD-PTM-ACTIVATE | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION |
      | Product Template | RETIRED | CMD-PTM-RETIRE | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION |
```
