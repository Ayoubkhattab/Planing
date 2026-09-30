---
id: TST-AI-REQUEST-SM
type: acceptance-spec
title: Acceptance — AI Request state machine
wave: W6
slice: SLC-10
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-AI-REQUEST
traces:
  verifies:
  - SL-05
  - AGG-AI-REQUEST
  - REQ-AI-001
  - REQ-AI-002
  - REQ-AI-003
  - REQ-AI-004
  - REQ-AI-007
  - REQ-AI-008
  - REQ-AI-011
  - REQ-AI-012
---

# Acceptance — AI Request

مولّدة من مصفوفة AGG-AI-REQUEST: 3 انتقالاً مسموحاً، 13 رفضاً، 8 انتقالاً نظامياً (SYS).

```gherkin
Feature: AI Request lifecycle (AGG-AI-REQUEST)

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
      | AI Request | RECEIVED | CMD-AIR-CANCEL | CANCELLED | EVT-AIR-CANCELLED | 3 |
      | AI Request | RETRIEVING | CMD-AIR-CANCEL | CANCELLED | EVT-AIR-CANCELLED | 3 |
      | AI Request | GENERATING | CMD-AIR-CANCEL | CANCELLED | EVT-AIR-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | AI Request | CMD-AIR-SUBMIT | RECEIVED | EVT-AIR-RECEIVED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | AI Request | RECEIVED | CMD-AIR-SUBMIT | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | RETRIEVING | CMD-AIR-SUBMIT | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | GENERATING | CMD-AIR-SUBMIT | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | COMPLETED | CMD-AIR-SUBMIT | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | COMPLETED | CMD-AIR-CANCEL | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | INSUFFICIENT_EVIDENCE | CMD-AIR-SUBMIT | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | INSUFFICIENT_EVIDENCE | CMD-AIR-CANCEL | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | REFUSED | CMD-AIR-SUBMIT | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | REFUSED | CMD-AIR-CANCEL | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | FAILED | CMD-AIR-SUBMIT | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | FAILED | CMD-AIR-CANCEL | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | CANCELLED | CMD-AIR-SUBMIT | AI_REQUEST_INVALID_STATE_TRANSITION |
      | AI Request | CANCELLED | CMD-AIR-CANCEL | AI_REQUEST_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | AI Request | RECEIVED | policy denied | REFUSED | EVT-AIR-REFUSED |
      | AI Request | RECEIVED | retrieval started | RETRIEVING | EVT-AIR-RETRIEVING |
      | AI Request | RETRIEVING | context package sealed | GENERATING | EVT-AIR-CONTEXT-SEALED |
      | AI Request | RETRIEVING | no sufficient evidence retrieved | INSUFFICIENT_EVIDENCE | EVT-AIR-INSUFFICIENT-EVIDENCE |
      | AI Request | RETRIEVING | error or timeout | FAILED | EVT-AIR-FAILED |
      | AI Request | GENERATING | output grounded | COMPLETED | EVT-AIR-COMPLETED |
      | AI Request | GENERATING | output not grounded | INSUFFICIENT_EVIDENCE | EVT-AIR-INSUFFICIENT-EVIDENCE |
      | AI Request | GENERATING | error or timeout | FAILED | EVT-AIR-FAILED |
```
