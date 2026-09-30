---
id: TST-AI-TOOL-SM
type: acceptance-spec
title: Acceptance — AI Tool state machine
wave: W6
slice: SLC-10
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-AI-TOOL
traces:
  verifies:
  - SL-05
  - AGG-AI-TOOL
  - REQ-AI-013
  - REQ-AI-012
---

# Acceptance — AI Tool

مولّدة من مصفوفة AGG-AI-TOOL: 6 انتقالاً مسموحاً، 14 رفضاً.

```gherkin
Feature: AI Tool lifecycle (AGG-AI-TOOL)

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
      | AI Tool | DRAFT | CMD-TOL-ACTIVATE | ACTIVE | EVT-TOL-ACTIVATED | 3 |
      | AI Tool | DRAFT | CMD-TOL-RETIRE | RETIRED | EVT-TOL-RETIRED | 3 |
      | AI Tool | ACTIVE | CMD-TOL-DISABLE | DISABLED | EVT-TOL-DISABLED | 3 |
      | AI Tool | ACTIVE | CMD-TOL-RETIRE | RETIRED | EVT-TOL-RETIRED | 3 |
      | AI Tool | DISABLED | CMD-TOL-ENABLE | ACTIVE | EVT-TOL-ENABLED | 3 |
      | AI Tool | DISABLED | CMD-TOL-RETIRE | RETIRED | EVT-TOL-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | AI Tool | CMD-TOL-REGISTER | DRAFT | EVT-TOL-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | AI Tool | DRAFT | CMD-TOL-REGISTER | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | DRAFT | CMD-TOL-DISABLE | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | DRAFT | CMD-TOL-ENABLE | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | ACTIVE | CMD-TOL-REGISTER | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | ACTIVE | CMD-TOL-ACTIVATE | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | ACTIVE | CMD-TOL-ENABLE | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | DISABLED | CMD-TOL-REGISTER | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | DISABLED | CMD-TOL-ACTIVATE | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | DISABLED | CMD-TOL-DISABLE | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | RETIRED | CMD-TOL-REGISTER | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | RETIRED | CMD-TOL-ACTIVATE | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | RETIRED | CMD-TOL-DISABLE | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | RETIRED | CMD-TOL-ENABLE | AI_TOOL_INVALID_STATE_TRANSITION |
      | AI Tool | RETIRED | CMD-TOL-RETIRE | AI_TOOL_INVALID_STATE_TRANSITION |
```
