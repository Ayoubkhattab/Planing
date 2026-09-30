---
id: TST-SOURCE-SM
type: acceptance-spec
title: Acceptance — Source state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-SOURCE
traces:
  verifies:
  - SL-05
  - AGG-SOURCE
  - REQ-INF-001
---

# Acceptance — Source

مولّدة من مصفوفة AGG-SOURCE: 12 انتقالاً مسموحاً، 12 رفضاً.

```gherkin
Feature: Source lifecycle (AGG-SOURCE)

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
      | Source | ACTIVE | CMD-SRC-RATE-RELIABILITY | ACTIVE | EVT-SRC-RELIABILITY-RATED | 3 |
      | Source | ACTIVE | CMD-SRC-UPDATE-PROFILE | ACTIVE | EVT-SRC-PROFILE-UPDATED | 3 |
      | Source | ACTIVE | CMD-SRC-SET-PROTECTION | ACTIVE | EVT-SRC-PROTECTION-CHANGED | 3 |
      | Source | ACTIVE | CMD-SRC-RECLASSIFY | ACTIVE | EVT-SRC-RECLASSIFIED | 3 |
      | Source | ACTIVE | CMD-SRC-SUSPEND | SUSPENDED | EVT-SRC-SUSPENDED | 3 |
      | Source | ACTIVE | CMD-SRC-RETIRE | RETIRED | EVT-SRC-RETIRED | 3 |
      | Source | SUSPENDED | CMD-SRC-RATE-RELIABILITY | SUSPENDED | EVT-SRC-RELIABILITY-RATED | 3 |
      | Source | SUSPENDED | CMD-SRC-UPDATE-PROFILE | SUSPENDED | EVT-SRC-PROFILE-UPDATED | 3 |
      | Source | SUSPENDED | CMD-SRC-SET-PROTECTION | SUSPENDED | EVT-SRC-PROTECTION-CHANGED | 3 |
      | Source | SUSPENDED | CMD-SRC-RECLASSIFY | SUSPENDED | EVT-SRC-RECLASSIFIED | 3 |
      | Source | SUSPENDED | CMD-SRC-REINSTATE | ACTIVE | EVT-SRC-REINSTATED | 3 |
      | Source | SUSPENDED | CMD-SRC-RETIRE | RETIRED | EVT-SRC-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Source | CMD-SRC-REGISTER | ACTIVE | EVT-SRC-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Source | ACTIVE | CMD-SRC-REGISTER | SOURCE_INVALID_STATE_TRANSITION |
      | Source | ACTIVE | CMD-SRC-REINSTATE | SOURCE_INVALID_STATE_TRANSITION |
      | Source | SUSPENDED | CMD-SRC-REGISTER | SOURCE_INVALID_STATE_TRANSITION |
      | Source | SUSPENDED | CMD-SRC-SUSPEND | SOURCE_INVALID_STATE_TRANSITION |
      | Source | RETIRED | CMD-SRC-REGISTER | SOURCE_INVALID_STATE_TRANSITION |
      | Source | RETIRED | CMD-SRC-RATE-RELIABILITY | SOURCE_INVALID_STATE_TRANSITION |
      | Source | RETIRED | CMD-SRC-UPDATE-PROFILE | SOURCE_INVALID_STATE_TRANSITION |
      | Source | RETIRED | CMD-SRC-SET-PROTECTION | SOURCE_INVALID_STATE_TRANSITION |
      | Source | RETIRED | CMD-SRC-RECLASSIFY | SOURCE_INVALID_STATE_TRANSITION |
      | Source | RETIRED | CMD-SRC-SUSPEND | SOURCE_INVALID_STATE_TRANSITION |
      | Source | RETIRED | CMD-SRC-REINSTATE | SOURCE_INVALID_STATE_TRANSITION |
      | Source | RETIRED | CMD-SRC-RETIRE | SOURCE_INVALID_STATE_TRANSITION |
```
