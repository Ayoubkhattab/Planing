---
id: TST-SLC15-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-15 coordination scoping, decision-gated actions, correlation and fusion
wave: W6
slice: SLC-15
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-CRD-001, REQ-CRD-002, REQ-FUS-001, REQ-FUS-002]}
---

# Acceptance — Coordination & Fusion

```gherkin
Feature: Coordination                                                             # REQ-CRD-001/002

  Scenario: Participants see only their scope
    Given case K with participants Civil Defence (scope: briefing, own_responsibilities) and Health (scope: briefing, all_responsibilities)
    When a Civil Defence member reads K
    Then only the briefing and Civil Defence responsibilities are returned

  Scenario: Authority-gated responsibility
    Given responsibility R for Health requires decision type "hospital-diversion"
    When a Health member marks R done before any decision
    Then the command is rejected with DECISION_PENDING
    When the case requests the decision and Health's authority records it
    Then R shows the decision outcome and can be marked done

  Scenario: Cannot close with open responsibilities
    When the lead closes K while a responsibility is in progress
    Then the command is rejected with OPEN_RESPONSIBILITIES

Feature: Correlation and fusion                                                   # REQ-FUS-001/002

  Scenario: Same event from two independent sources
    Given a field report of a fire at 10:05 (accuracy 50 m) and a sensor alarm at 10:07 (accuracy 20 m) 60 m apart
    Then a same_event proposal is created with score breakdown and rule version
    When a reviewer accepts it
    Then a Real-World Event exists with derived location weighted toward the sensor, event time 10:05–10:07, and claims citing both observations with each source's reliability

  Scenario: Same source does not corroborate itself
    Given two reports from the same source
    Then no same_event proposal requiring 2 distinct sources is created

  Scenario: Proposals never change data
    Given a PROPOSED correlation
    Then no claim, observation or entity changed

  Scenario: Hidden inputs restrict review
    Given a proposal with a SECRET input and analyst A cleared CONFIDENTIAL
    Then the proposal is not in A's queue

  Scenario: Fused value conflicting with an existing claim opens a conflict
    Given an existing claim of event time 09:00 for the same event
    When fusion derives 10:05–10:07
    Then a conflict is opened (SLC-04) and no value is overwritten
```
