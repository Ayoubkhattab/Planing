---
id: TST-QUALIFICATION-RECORD-SM
type: acceptance-spec
title: Acceptance — Qualification Record state machine
wave: W6
slice: SLC-03
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-QUALIFICATION-RECORD
traces:
  verifies:
  - SL-05
  - AGG-QUALIFICATION-RECORD
  - REQ-RDY-001
  - REQ-RDY-002
---

# Acceptance — Qualification Record

مولّدة من مصفوفة AGG-QUALIFICATION-RECORD: 5 انتقالاً مسموحاً، 15 رفضاً، 2 انتقالاً نظامياً (SYS).

```gherkin
Feature: Qualification Record lifecycle (AGG-QUALIFICATION-RECORD)

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
      | Qualification Record | ACTIVE | CMD-QUAL-RENEW | ACTIVE | EVT-QUAL-RENEWED | 3 |
      | Qualification Record | ACTIVE | CMD-QUAL-SUSPEND | SUSPENDED | EVT-QUAL-SUSPENDED | 3 |
      | Qualification Record | ACTIVE | CMD-QUAL-REVOKE | REVOKED | EVT-QUAL-REVOKED | 3 |
      | Qualification Record | SUSPENDED | CMD-QUAL-REINSTATE | ACTIVE | EVT-QUAL-REINSTATED | 3 |
      | Qualification Record | SUSPENDED | CMD-QUAL-REVOKE | REVOKED | EVT-QUAL-REVOKED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Qualification Record | CMD-QUAL-RECORD | ACTIVE | EVT-QUAL-RECORDED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Qualification Record | ACTIVE | CMD-QUAL-RECORD | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | ACTIVE | CMD-QUAL-REINSTATE | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | SUSPENDED | CMD-QUAL-RECORD | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | SUSPENDED | CMD-QUAL-RENEW | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | SUSPENDED | CMD-QUAL-SUSPEND | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | EXPIRED | CMD-QUAL-RECORD | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | EXPIRED | CMD-QUAL-RENEW | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | EXPIRED | CMD-QUAL-SUSPEND | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | EXPIRED | CMD-QUAL-REINSTATE | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | EXPIRED | CMD-QUAL-REVOKE | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | REVOKED | CMD-QUAL-RECORD | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | REVOKED | CMD-QUAL-RENEW | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | REVOKED | CMD-QUAL-SUSPEND | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | REVOKED | CMD-QUAL-REINSTATE | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
      | Qualification Record | REVOKED | CMD-QUAL-REVOKE | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Qualification Record | ACTIVE | valid_to reached | EXPIRED | EVT-QUAL-EXPIRED |
      | Qualification Record | SUSPENDED | valid_to reached | EXPIRED | EVT-QUAL-EXPIRED |
```
