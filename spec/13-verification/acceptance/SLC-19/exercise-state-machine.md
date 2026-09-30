---
id: TST-EXERCISE-SM
type: acceptance-spec
title: Acceptance — Exercise state machine
wave: W6
slice: SLC-19
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
generated_from: AGG-EXERCISE
traces:
  verifies:
  - SL-05
  - AGG-EXERCISE
  - REQ-TRX-003
  - REQ-TRX-004
  - REQ-TRX-005
  - REQ-TRX-006
  - REQ-TRX-007
---

# Acceptance — Exercise

مولّدة من مصفوفة AGG-EXERCISE: 7 انتقالات مسموحة (5 بشرية بما فيها الإنشاء + 2 نظامية)، 20 رفضاً على مستوى الأوامر البشرية الأربعة (لا تُختبر انتقالات `SYS:` كـ"أمر يرسله الفاعل" — لا مسار HTTP لها أصلاً).

```gherkin
Feature: Exercise lifecycle (AGG-EXERCISE)

  Background:
    Given an ACTIVE tenant, baseline policies, and an authorized actor
    And every guard of the command is satisfied

  Scenario Outline: allowed transition
    Given an <aggregate> in state <from> at version <v>
    When the actor sends <command> with a new Idempotency-Key and If-Match <v>
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And one audit record is written in the same transaction

    Examples:
      | aggregate | from | command | to | event | v |
      | Exercise | PLANNED | CMD-EXR-SCHEDULE | SCHEDULED | EVT-EXR-SCHEDULED | 2 |
      | Exercise | SCHEDULED | CMD-EXR-START | IN_PROGRESS | EVT-EXR-STARTED | 3 |
      | Exercise | PLANNED | CMD-EXR-CANCEL | CANCELLED | EVT-EXR-CANCELLED | 2 |
      | Exercise | SCHEDULED | CMD-EXR-CANCEL | CANCELLED | EVT-EXR-CANCELLED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Exercise | CMD-EXR-PLAN | PLANNED | EVT-EXR-PLANNED |

  Scenario: Starting an exercise creates exactly one linked simulation in the same unit of work
    Given an Exercise E in state SCHEDULED, referencing a frozen ACTIVE scenario S
    When the actor sends CMD-EXR-START
    Then E becomes IN_PROGRESS
    And exactly one Simulation exists with exercise_ref = E and scenario_ref = S
    And the Simulation was created in the same transaction as E's transition

  Scenario: An exercise's terminal outcome is driven exclusively by its linked simulation
    Given an Exercise E is IN_PROGRESS with linked Simulation M
    When M reaches COMPLETED (EVT-SIM-COMPLETED)
    Then E becomes COMPLETED as a system-driven consequence, with no exercise-level completion command involved
    Given a different Exercise E2 is IN_PROGRESS with linked Simulation M2
    When M2 is aborted (EVT-SIM-ABORTED)
    Then E2 becomes ABORTED as a system-driven consequence

  Scenario Outline: rejected transition
    Given an <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Exercise | PLANNED | CMD-EXR-PLAN | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | SCHEDULED | CMD-EXR-PLAN | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | IN_PROGRESS | CMD-EXR-PLAN | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | COMPLETED | CMD-EXR-PLAN | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | ABORTED | CMD-EXR-PLAN | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | CANCELLED | CMD-EXR-PLAN | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | SCHEDULED | CMD-EXR-SCHEDULE | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | IN_PROGRESS | CMD-EXR-SCHEDULE | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | COMPLETED | CMD-EXR-SCHEDULE | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | ABORTED | CMD-EXR-SCHEDULE | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | CANCELLED | CMD-EXR-SCHEDULE | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | PLANNED | CMD-EXR-START | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | IN_PROGRESS | CMD-EXR-START | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | COMPLETED | CMD-EXR-START | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | ABORTED | CMD-EXR-START | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | CANCELLED | CMD-EXR-START | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | IN_PROGRESS | CMD-EXR-CANCEL | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | COMPLETED | CMD-EXR-CANCEL | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | ABORTED | CMD-EXR-CANCEL | EXERCISE_INVALID_STATE_TRANSITION |
      | Exercise | CANCELLED | CMD-EXR-CANCEL | EXERCISE_INVALID_STATE_TRANSITION |
```
