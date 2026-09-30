---
id: TST-SECURITY-EXCEPTION-SM
type: acceptance-spec
title: Acceptance — Security Exception state machine
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-SECURITY-EXCEPTION
traces:
  verifies:
  - SL-05
  - AGG-SECURITY-EXCEPTION
  - REQ-FND-017
---

# Acceptance — Security Exception

مولّدة من مصفوفة AGG-SECURITY-EXCEPTION: 5 انتقالاً مسموحاً، 19 رفضاً.

```gherkin
Feature: Security Exception lifecycle (AGG-SECURITY-EXCEPTION)

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
      | Security Exception | REQUESTED | CMD-EXC-APPROVE | FIRST_APPROVED | EVT-EXC-FIRST-APPROVED | 3 |
      | Security Exception | REQUESTED | CMD-EXC-REJECT | REJECTED | EVT-EXC-REJECTED | 3 |
      | Security Exception | FIRST_APPROVED | CMD-EXC-APPROVE | ACTIVE | EVT-EXC-ACTIVATED | 3 |
      | Security Exception | FIRST_APPROVED | CMD-EXC-REJECT | REJECTED | EVT-EXC-REJECTED | 3 |
      | Security Exception | ACTIVE | CMD-EXC-REVOKE | REVOKED | EVT-EXC-REVOKED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Security Exception | CMD-EXC-REQUEST | REQUESTED | EVT-EXC-REQUESTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Security Exception | REQUESTED | CMD-EXC-REQUEST | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | REQUESTED | CMD-EXC-REVOKE | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | FIRST_APPROVED | CMD-EXC-REQUEST | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | FIRST_APPROVED | CMD-EXC-REVOKE | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | ACTIVE | CMD-EXC-REQUEST | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | ACTIVE | CMD-EXC-APPROVE | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | ACTIVE | CMD-EXC-REJECT | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | REJECTED | CMD-EXC-REQUEST | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | REJECTED | CMD-EXC-APPROVE | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | REJECTED | CMD-EXC-REJECT | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | REJECTED | CMD-EXC-REVOKE | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | EXPIRED | CMD-EXC-REQUEST | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | EXPIRED | CMD-EXC-APPROVE | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | EXPIRED | CMD-EXC-REJECT | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | EXPIRED | CMD-EXC-REVOKE | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | REVOKED | CMD-EXC-REQUEST | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | REVOKED | CMD-EXC-APPROVE | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | REVOKED | CMD-EXC-REJECT | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
      | Security Exception | REVOKED | CMD-EXC-REVOKE | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
```
