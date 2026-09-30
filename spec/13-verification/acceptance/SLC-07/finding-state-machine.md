---
id: TST-FINDING-SM
type: acceptance-spec
title: Acceptance — Finding state machine
wave: W6
slice: SLC-07
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-FINDING
traces:
  verifies:
  - SL-05
  - AGG-FINDING
  - REQ-ANL-005
  - REQ-INF-035
---

# Acceptance — Finding

مولّدة من مصفوفة AGG-FINDING: 4 انتقالاً مسموحاً، 8 رفضاً.

```gherkin
Feature: Finding lifecycle (AGG-FINDING)

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
      | Finding | DRAFT | CMD-FND-EDIT | DRAFT | EVT-FND-EDITED | 3 |
      | Finding | DRAFT | CMD-FND-ACCEPT | ACCEPTED | EVT-FND-ACCEPTED | 3 |
      | Finding | DRAFT | CMD-FND-WITHDRAW | WITHDRAWN | EVT-FND-WITHDRAWN | 3 |
      | Finding | ACCEPTED | CMD-FND-WITHDRAW | WITHDRAWN | EVT-FND-WITHDRAWN | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Finding | CMD-FND-RECORD | DRAFT | EVT-FND-RECORDED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Finding | DRAFT | CMD-FND-RECORD | FINDING_INVALID_STATE_TRANSITION |
      | Finding | ACCEPTED | CMD-FND-RECORD | FINDING_INVALID_STATE_TRANSITION |
      | Finding | ACCEPTED | CMD-FND-EDIT | FINDING_INVALID_STATE_TRANSITION |
      | Finding | ACCEPTED | CMD-FND-ACCEPT | FINDING_INVALID_STATE_TRANSITION |
      | Finding | WITHDRAWN | CMD-FND-RECORD | FINDING_INVALID_STATE_TRANSITION |
      | Finding | WITHDRAWN | CMD-FND-EDIT | FINDING_INVALID_STATE_TRANSITION |
      | Finding | WITHDRAWN | CMD-FND-ACCEPT | FINDING_INVALID_STATE_TRANSITION |
      | Finding | WITHDRAWN | CMD-FND-WITHDRAW | FINDING_INVALID_STATE_TRANSITION |
```
