---
id: TST-ORGANIZATION-SM
type: acceptance-spec
title: Acceptance — Organization (with unit tree) state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ORGANIZATION
traces:
  verifies:
  - SL-05
  - AGG-ORGANIZATION
  - REQ-FND-002
---

# Acceptance — Organization (with unit tree)

مولّدة من مصفوفة AGG-ORGANIZATION: 7 انتقالاً مسموحاً، 9 رفضاً.

```gherkin
Feature: Organization (with unit tree) lifecycle (AGG-ORGANIZATION)

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
      | Organization (with unit tree) | ACTIVE | CMD-ORG-RENAME | ACTIVE | EVT-ORG-RENAMED | 3 |
      | Organization (with unit tree) | ACTIVE | CMD-ORG-ADD-UNIT | ACTIVE | EVT-ORG-UNIT-ADDED | 3 |
      | Organization (with unit tree) | ACTIVE | CMD-ORG-RENAME-UNIT | ACTIVE | EVT-ORG-UNIT-RENAMED | 3 |
      | Organization (with unit tree) | ACTIVE | CMD-ORG-MOVE-UNIT | ACTIVE | EVT-ORG-UNIT-MOVED | 3 |
      | Organization (with unit tree) | ACTIVE | CMD-ORG-DEACTIVATE-UNIT | ACTIVE | EVT-ORG-UNIT-DEACTIVATED | 3 |
      | Organization (with unit tree) | ACTIVE | CMD-ORG-DEACTIVATE | INACTIVE | EVT-ORG-DEACTIVATED | 3 |
      | Organization (with unit tree) | INACTIVE | CMD-ORG-REACTIVATE | ACTIVE | EVT-ORG-REACTIVATED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Organization (with unit tree) | CMD-ORG-CREATE | ACTIVE | EVT-ORG-CREATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Organization (with unit tree) | ACTIVE | CMD-ORG-CREATE | ORGANIZATION_INVALID_STATE_TRANSITION |
      | Organization (with unit tree) | ACTIVE | CMD-ORG-REACTIVATE | ORGANIZATION_INVALID_STATE_TRANSITION |
      | Organization (with unit tree) | INACTIVE | CMD-ORG-CREATE | ORGANIZATION_INVALID_STATE_TRANSITION |
      | Organization (with unit tree) | INACTIVE | CMD-ORG-RENAME | ORGANIZATION_INVALID_STATE_TRANSITION |
      | Organization (with unit tree) | INACTIVE | CMD-ORG-ADD-UNIT | ORGANIZATION_INVALID_STATE_TRANSITION |
      | Organization (with unit tree) | INACTIVE | CMD-ORG-RENAME-UNIT | ORGANIZATION_INVALID_STATE_TRANSITION |
      | Organization (with unit tree) | INACTIVE | CMD-ORG-MOVE-UNIT | ORGANIZATION_INVALID_STATE_TRANSITION |
      | Organization (with unit tree) | INACTIVE | CMD-ORG-DEACTIVATE-UNIT | ORGANIZATION_INVALID_STATE_TRANSITION |
      | Organization (with unit tree) | INACTIVE | CMD-ORG-DEACTIVATE | ORGANIZATION_INVALID_STATE_TRANSITION |
```
