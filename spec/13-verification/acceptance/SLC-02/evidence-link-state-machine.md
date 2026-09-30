---
id: TST-EVIDENCE-LINK-SM
type: acceptance-spec
title: Acceptance — Evidence Link state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-EVIDENCE-LINK
traces:
  verifies:
  - SL-05
  - AGG-EVIDENCE-LINK
  - REQ-INF-021
---

# Acceptance — Evidence Link

مولّدة من مصفوفة AGG-EVIDENCE-LINK: 1 انتقالاً مسموحاً، 3 رفضاً.

```gherkin
Feature: Evidence Link lifecycle (AGG-EVIDENCE-LINK)

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
      | Evidence Link | ACTIVE | CMD-EVL-UNLINK | REMOVED | EVT-EVL-UNLINKED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Evidence Link | CMD-EVL-LINK | ACTIVE | EVT-EVL-LINKED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Evidence Link | ACTIVE | CMD-EVL-LINK | EVIDENCE_LINK_INVALID_STATE_TRANSITION |
      | Evidence Link | REMOVED | CMD-EVL-LINK | EVIDENCE_LINK_INVALID_STATE_TRANSITION |
      | Evidence Link | REMOVED | CMD-EVL-UNLINK | EVIDENCE_LINK_INVALID_STATE_TRANSITION |
```
