---
id: TST-CLASSIFICATION-SCHEME-SM
type: acceptance-spec
title: Acceptance — Classification Scheme Version state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-CLASSIFICATION-SCHEME
traces:
  verifies:
  - SL-05
  - AGG-CLASSIFICATION-SCHEME
  - REQ-GOV-001
  - REQ-GOV-004
  - REQ-GOV-009
---

# Acceptance — Classification Scheme Version

مولّدة من مصفوفة AGG-CLASSIFICATION-SCHEME: 3 انتقالاً مسموحاً، 13 رفضاً، 1 انتقالاً نظامياً (SYS).

```gherkin
Feature: Classification Scheme Version lifecycle (AGG-CLASSIFICATION-SCHEME)

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
      | Classification Scheme Version | DRAFT | CMD-CLS-EDIT | DRAFT | EVT-CLS-EDITED | 3 |
      | Classification Scheme Version | DRAFT | CMD-CLS-ACTIVATE | ACTIVE | EVT-CLS-ACTIVATED | 3 |
      | Classification Scheme Version | DRAFT | CMD-CLS-DISCARD | DISCARDED | EVT-CLS-DISCARDED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Classification Scheme Version | CMD-CLS-DRAFT | DRAFT | EVT-CLS-DRAFTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Classification Scheme Version | DRAFT | CMD-CLS-DRAFT | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | ACTIVE | CMD-CLS-DRAFT | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | ACTIVE | CMD-CLS-EDIT | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | ACTIVE | CMD-CLS-ACTIVATE | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | ACTIVE | CMD-CLS-DISCARD | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | SUPERSEDED | CMD-CLS-DRAFT | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | SUPERSEDED | CMD-CLS-EDIT | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | SUPERSEDED | CMD-CLS-ACTIVATE | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | SUPERSEDED | CMD-CLS-DISCARD | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | DISCARDED | CMD-CLS-DRAFT | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | DISCARDED | CMD-CLS-EDIT | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | DISCARDED | CMD-CLS-ACTIVATE | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
      | Classification Scheme Version | DISCARDED | CMD-CLS-DISCARD | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Classification Scheme Version | ACTIVE | successor activated | SUPERSEDED | EVT-CLS-SUPERSEDED |
```
