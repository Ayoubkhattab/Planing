---
id: TST-EXTERNAL-ID-SM
type: acceptance-spec
title: Acceptance — External Identifier Mapping state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-EXTERNAL-ID
traces:
  verifies:
  - SL-05
  - AGG-EXTERNAL-ID
  - REQ-INF-036
---

# Acceptance — External Identifier Mapping

مولّدة من مصفوفة AGG-EXTERNAL-ID: 1 انتقالاً مسموحاً، 3 رفضاً.

```gherkin
Feature: External Identifier Mapping lifecycle (AGG-EXTERNAL-ID)

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
      | External Identifier Mapping | ACTIVE | CMD-EXT-END | ENDED | EVT-EXT-ENDED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | External Identifier Mapping | CMD-EXT-MAP | ACTIVE | EVT-EXT-MAPPED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | External Identifier Mapping | ACTIVE | CMD-EXT-MAP | EXTERNAL_ID_INVALID_STATE_TRANSITION |
      | External Identifier Mapping | ENDED | CMD-EXT-MAP | EXTERNAL_ID_INVALID_STATE_TRANSITION |
      | External Identifier Mapping | ENDED | CMD-EXT-END | EXTERNAL_ID_INVALID_STATE_TRANSITION |
```
