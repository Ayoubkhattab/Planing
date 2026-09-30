---
id: TST-CORRELATION-RULE-SM
type: acceptance-spec
title: Acceptance — Correlation Rule state machine
wave: W6
slice: SLC-15
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-CORRELATION-RULE
traces:
  verifies:
  - SL-05
  - AGG-CORRELATION-RULE
  - REQ-FUS-001
---

# Acceptance — Correlation Rule

مولّدة من مصفوفة AGG-CORRELATION-RULE: 4 انتقالاً مسموحاً، 8 رفضاً.

```gherkin
Feature: Correlation Rule lifecycle (AGG-CORRELATION-RULE)

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
      | Correlation Rule | DRAFT | CMD-CRR-EDIT | DRAFT | EVT-CRR-EDITED | 3 |
      | Correlation Rule | DRAFT | CMD-CRR-ACTIVATE | ACTIVE | EVT-CRR-ACTIVATED | 3 |
      | Correlation Rule | ACTIVE | CMD-CRR-EDIT | ACTIVE | EVT-CRR-EDITED | 3 |
      | Correlation Rule | ACTIVE | CMD-CRR-RETIRE | RETIRED | EVT-CRR-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Correlation Rule | CMD-CRR-DEFINE | DRAFT | EVT-CRR-DEFINED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Correlation Rule | DRAFT | CMD-CRR-DEFINE | CORRELATION_RULE_INVALID_STATE_TRANSITION |
      | Correlation Rule | DRAFT | CMD-CRR-RETIRE | CORRELATION_RULE_INVALID_STATE_TRANSITION |
      | Correlation Rule | ACTIVE | CMD-CRR-DEFINE | CORRELATION_RULE_INVALID_STATE_TRANSITION |
      | Correlation Rule | ACTIVE | CMD-CRR-ACTIVATE | CORRELATION_RULE_INVALID_STATE_TRANSITION |
      | Correlation Rule | RETIRED | CMD-CRR-DEFINE | CORRELATION_RULE_INVALID_STATE_TRANSITION |
      | Correlation Rule | RETIRED | CMD-CRR-EDIT | CORRELATION_RULE_INVALID_STATE_TRANSITION |
      | Correlation Rule | RETIRED | CMD-CRR-ACTIVATE | CORRELATION_RULE_INVALID_STATE_TRANSITION |
      | Correlation Rule | RETIRED | CMD-CRR-RETIRE | CORRELATION_RULE_INVALID_STATE_TRANSITION |
```
