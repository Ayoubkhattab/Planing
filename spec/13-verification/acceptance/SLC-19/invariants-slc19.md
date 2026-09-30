---
id: TST-SLC19-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-19 scenario freeze / exercise-simulation delegation / evidence reuse
wave: W6
slice: SLC-19
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
traces: {verifies: [REQ-TRX-002, REQ-TRX-003, REQ-TRX-005, REQ-TRX-006, REQ-TRX-010, REQ-TRX-012, REQ-TRX-013, QAS-TRX-001, QAS-TRX-002]}
---

# Acceptance — Scenario freeze / Exercise-Simulation delegation / evidence reuse

```gherkin
Feature: Scenario versioning never disturbs an already-planned exercise            # REQ-TRX-002/003

  Scenario: Editing an ACTIVE scenario creates a new version while a planned exercise keeps its frozen reference
    Given a Scenario S is ACTIVE at version 3
    And an Exercise E was planned against S, freezing scenario_version_frozen = 3
    When the scenario author sends CMD-SCN-EDIT
    Then S becomes version 4, still ACTIVE
    And E's scenario_version_frozen remains 3, unchanged

  Scenario: An exercise cannot be planned against a DRAFT or RETIRED scenario
    Given a Scenario S is in state DRAFT
    When the actor sends CMD-EXR-PLAN referencing S
    Then the command is rejected with EXERCISE_INVALID
    Given a different Scenario S2 is in state RETIRED
    When the actor sends CMD-EXR-PLAN referencing S2
    Then the command is rejected with EXERCISE_INVALID

Feature: Starting an exercise always creates exactly one linked simulation           # REQ-TRX-005

  Scenario: CMD-EXR-START creates a Simulation in the same unit of work
    When the actor sends CMD-EXR-START for a SCHEDULED Exercise E referencing frozen Scenario S
    Then E becomes IN_PROGRESS
    And exactly one Simulation M exists with exercise_ref = E and scenario_ref = S, in state IN_PROGRESS
    And M was created in the same transaction as E's transition

  Scenario: An exercise cannot start before it is scheduled
    Given an Exercise E is in state PLANNED
    When the actor sends CMD-EXR-START
    Then the command is rejected with EXERCISE_INVALID_STATE_TRANSITION
    And no Simulation is created

Feature: An exercise's terminal outcome always mirrors its linked simulation's outcome  # REQ-TRX-006

  Scenario: A completed simulation resolves its exercise to COMPLETED
    Given Exercise E is IN_PROGRESS with linked Simulation M, both open
    When M reaches COMPLETED (every participant evaluated)
    Then E becomes COMPLETED as a system-driven consequence, with no exercise-level completion command involved

  Scenario: An aborted simulation resolves its exercise to ABORTED, never silently
    Given a different Exercise E2 is IN_PROGRESS with linked Simulation M2
    When M2 is aborted with a reason
    Then E2 becomes ABORTED as a system-driven consequence
    And no CMD-EXR-CANCEL or any human command changed E2's state

Feature: A simulation never completes with an unevaluated participant                # REQ-TRX-010

  Scenario: Completion fails while a participant has zero evaluations
    Given a Simulation M for an Exercise with participants P1 and P2
    And only P1 has a recorded evaluation
    When the actor sends CMD-SIM-COMPLETE
    Then the command is rejected with EVALUATION_MISSING
    And M remains IN_PROGRESS

  Scenario: Completion succeeds once every participant has at least one evaluation
    Given the same Simulation M
    When an evaluation for P2 is recorded (evaluator ≠ P2)
    And the actor sends CMD-SIM-COMPLETE
    Then M becomes COMPLETED

Feature: Cross-slice reuse changes nothing in the aggregates it reuses               # REQ-TRX-012/013

  Scenario: A completed simulation cited as qualification evidence requires no SLC-03 schema change
    Given a Simulation M reached COMPLETED with a MET evaluation for person X on competency C
    When a Training Manager sends CMD-QUAL-RECORD for person X, code C, with evidence = M's urn
    Then the Qualification Record is created in state ACTIVE
    And AGG-QUALIFICATION-RECORD's payload schema and guard remain byte-identical to the pre-SLC-19 baseline (evidence:urn was already generic)

  Scenario: A completed simulation drafted as an After Action Review resolves through the existing lesson path (CR-63)
    Given a Simulation M reached COMPLETED
    When a Training Manager sends CMD-KNO-DRAFT with knowledge_type = lesson and source = M's urn
    Then the Knowledge Object is created in state DRAFT
    And CMD-KNO-DRAFT's payload schema (source:urn) remains unchanged — only the guard text and REQ-KNW-002 were broadened (CR-63)
```
