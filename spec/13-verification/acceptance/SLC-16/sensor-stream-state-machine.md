---
id: TST-SENSOR-STREAM-SM
type: acceptance-spec
title: Acceptance — Sensor Stream state machine
wave: W6
slice: SLC-16
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-SENSOR-STREAM
traces:
  verifies:
  - SL-05
  - AGG-SENSOR-STREAM
  - REQ-INT-002
---

# Acceptance — Sensor Stream

مولّدة من مصفوفة AGG-SENSOR-STREAM: 8 انتقالاً مسموحاً، 12 رفضاً.

```gherkin
Feature: Sensor Stream lifecycle (AGG-SENSOR-STREAM)

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
      | Sensor Stream | DRAFT | CMD-SNS-SET-QUALITY-RULES | DRAFT | EVT-SNS-QUALITY-RULES-SET | 3 |
      | Sensor Stream | DRAFT | CMD-SNS-ACTIVATE | ACTIVE | EVT-SNS-ACTIVATED | 3 |
      | Sensor Stream | DRAFT | CMD-SNS-RETIRE | RETIRED | EVT-SNS-RETIRED | 3 |
      | Sensor Stream | ACTIVE | CMD-SNS-SET-QUALITY-RULES | ACTIVE | EVT-SNS-QUALITY-RULES-SET | 3 |
      | Sensor Stream | ACTIVE | CMD-SNS-PAUSE | PAUSED | EVT-SNS-PAUSED | 3 |
      | Sensor Stream | PAUSED | CMD-SNS-SET-QUALITY-RULES | PAUSED | EVT-SNS-QUALITY-RULES-SET | 3 |
      | Sensor Stream | PAUSED | CMD-SNS-ACTIVATE | ACTIVE | EVT-SNS-ACTIVATED | 3 |
      | Sensor Stream | PAUSED | CMD-SNS-RETIRE | RETIRED | EVT-SNS-RETIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Sensor Stream | CMD-SNS-REGISTER | DRAFT | EVT-SNS-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Sensor Stream | DRAFT | CMD-SNS-REGISTER | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | DRAFT | CMD-SNS-PAUSE | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | ACTIVE | CMD-SNS-REGISTER | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | ACTIVE | CMD-SNS-ACTIVATE | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | ACTIVE | CMD-SNS-RETIRE | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | PAUSED | CMD-SNS-REGISTER | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | PAUSED | CMD-SNS-PAUSE | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | RETIRED | CMD-SNS-REGISTER | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | RETIRED | CMD-SNS-SET-QUALITY-RULES | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | RETIRED | CMD-SNS-ACTIVATE | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | RETIRED | CMD-SNS-PAUSE | SENSOR_STREAM_INVALID_STATE_TRANSITION |
      | Sensor Stream | RETIRED | CMD-SNS-RETIRE | SENSOR_STREAM_INVALID_STATE_TRANSITION |
```
