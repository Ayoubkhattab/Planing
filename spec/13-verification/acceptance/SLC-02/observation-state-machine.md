---
id: TST-OBSERVATION-SM
type: acceptance-spec
title: Acceptance — Observation state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-OBSERVATION
traces:
  verifies:
  - SL-05
  - AGG-OBSERVATION
  - REQ-INF-002
  - REQ-INF-028
---

# Acceptance — Observation

مولّدة من مصفوفة AGG-OBSERVATION: 7 انتقالاً مسموحاً، 11 رفضاً.

```gherkin
Feature: Observation lifecycle (AGG-OBSERVATION)

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
      | Observation | RECORDED | CMD-OBS-AMEND | RECORDED | EVT-OBS-AMENDED | 3 |
      | Observation | RECORDED | CMD-OBS-ATTACH-EVIDENCE | RECORDED | EVT-OBS-EVIDENCE-ATTACHED | 3 |
      | Observation | RECORDED | CMD-OBS-RECLASSIFY | RECORDED | EVT-OBS-RECLASSIFIED | 3 |
      | Observation | RECORDED | CMD-OBS-VALIDATE | VALIDATED | EVT-OBS-VALIDATED | 3 |
      | Observation | RECORDED | CMD-OBS-REJECT | REJECTED | EVT-OBS-REJECTED | 3 |
      | Observation | VALIDATED | CMD-OBS-RECLASSIFY | VALIDATED | EVT-OBS-RECLASSIFIED | 3 |
      | Observation | REJECTED | CMD-OBS-RECLASSIFY | REJECTED | EVT-OBS-RECLASSIFIED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Observation | CMD-OBS-RECORD | RECORDED | EVT-OBS-RECORDED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Observation | RECORDED | CMD-OBS-RECORD | OBSERVATION_INVALID_STATE_TRANSITION |
      | Observation | VALIDATED | CMD-OBS-RECORD | OBSERVATION_INVALID_STATE_TRANSITION |
      | Observation | VALIDATED | CMD-OBS-AMEND | OBSERVATION_INVALID_STATE_TRANSITION |
      | Observation | VALIDATED | CMD-OBS-ATTACH-EVIDENCE | OBSERVATION_INVALID_STATE_TRANSITION |
      | Observation | VALIDATED | CMD-OBS-VALIDATE | OBSERVATION_INVALID_STATE_TRANSITION |
      | Observation | VALIDATED | CMD-OBS-REJECT | OBSERVATION_INVALID_STATE_TRANSITION |
      | Observation | REJECTED | CMD-OBS-RECORD | OBSERVATION_INVALID_STATE_TRANSITION |
      | Observation | REJECTED | CMD-OBS-AMEND | OBSERVATION_INVALID_STATE_TRANSITION |
      | Observation | REJECTED | CMD-OBS-ATTACH-EVIDENCE | OBSERVATION_INVALID_STATE_TRANSITION |
      | Observation | REJECTED | CMD-OBS-VALIDATE | OBSERVATION_INVALID_STATE_TRANSITION |
      | Observation | REJECTED | CMD-OBS-REJECT | OBSERVATION_INVALID_STATE_TRANSITION |
```
