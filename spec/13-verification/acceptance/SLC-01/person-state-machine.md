---
id: TST-PERSON-SM
type: acceptance-spec
title: Acceptance — Person state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-PERSON
traces:
  verifies:
  - SL-05
  - AGG-PERSON
  - REQ-FND-006
  - REQ-GOV-008
---

# Acceptance — Person

مولّدة من مصفوفة AGG-PERSON: 4 انتقالاً مسموحاً، 11 رفضاً.

```gherkin
Feature: Person lifecycle (AGG-PERSON)

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
      | Person | ACTIVE | CMD-PER-UPDATE-DETAILS | ACTIVE | EVT-PER-DETAILS-UPDATED | 3 |
      | Person | ACTIVE | CMD-PER-DEACTIVATE | INACTIVE | EVT-PER-DEACTIVATED | 3 |
      | Person | INACTIVE | CMD-PER-REACTIVATE | ACTIVE | EVT-PER-REACTIVATED | 3 |
      | Person | INACTIVE | CMD-PER-ERASE | ERASED | EVT-PER-ERASED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Person | CMD-PER-REGISTER | ACTIVE | EVT-PER-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Person | ACTIVE | CMD-PER-REGISTER | PERSON_INVALID_STATE_TRANSITION |
      | Person | ACTIVE | CMD-PER-REACTIVATE | PERSON_INVALID_STATE_TRANSITION |
      | Person | ACTIVE | CMD-PER-ERASE | PERSON_INVALID_STATE_TRANSITION |
      | Person | INACTIVE | CMD-PER-REGISTER | PERSON_INVALID_STATE_TRANSITION |
      | Person | INACTIVE | CMD-PER-UPDATE-DETAILS | PERSON_INVALID_STATE_TRANSITION |
      | Person | INACTIVE | CMD-PER-DEACTIVATE | PERSON_INVALID_STATE_TRANSITION |
      | Person | ERASED | CMD-PER-REGISTER | PERSON_INVALID_STATE_TRANSITION |
      | Person | ERASED | CMD-PER-UPDATE-DETAILS | PERSON_INVALID_STATE_TRANSITION |
      | Person | ERASED | CMD-PER-DEACTIVATE | PERSON_INVALID_STATE_TRANSITION |
      | Person | ERASED | CMD-PER-REACTIVATE | PERSON_INVALID_STATE_TRANSITION |
      | Person | ERASED | CMD-PER-ERASE | PERSON_INVALID_STATE_TRANSITION |
```
