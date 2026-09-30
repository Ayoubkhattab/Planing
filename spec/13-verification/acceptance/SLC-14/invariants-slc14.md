---
id: TST-SLC14-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-14 collection requirements, matching, viewer-scoped fulfilment, tasking
wave: W6
slice: SLC-14
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-COL-001, REQ-COL-002, REQ-COL-003, QAS-COL-001]}
---

# Acceptance — Collection

```gherkin
Feature: Requirements                                                            # REQ-COL-001

  Scenario: Requirement needs area, window, priority and EEIs
    When a draft without EEIs is submitted
    Then the command is rejected with REQUIREMENT_INCOMPLETE

  Scenario: Requester cannot approve
    When the requester approves the requirement
    Then the command is rejected with SEGREGATION_OF_DUTIES

Feature: Planning and tasking                                                     # REQ-COL-002

  Scenario: Activation creates field tasks
    Given a collection plan with 3 activities for an APPROVED requirement
    When the plan is activated
    Then 3 tasks exist with plan_ref = the collection plan and the activities' task types

  Scenario: Activity outside the requirement area is rejected
    When an activity with an area outside all requirement areas is added
    Then the command is rejected with ACTIVITY_INVALID

Feature: Matching and fulfilment                                                   # REQ-COL-003, QAS-COL-001

  Scenario: Validated observation answers an EEI
    Given requirement R with EEI e1 (method: visual, entity type: bridge) and e2 (quantity: water_level)
    When an observation of a bridge inside R's area and window is validated
    Then a fulfilment link (R, e1, observation) exists with lineage within 30 s
    And R's fulfilment is PARTIAL

  Scenario: Unvalidated observations never count
    When a RECORDED (not validated) observation matches e2
    Then no link is created

  Scenario: Fulfilment is scoped to the viewer
    Given e2 is answered only by a SECRET observation and requester Q is cleared CONFIDENTIAL
    Then Q sees R as PARTIAL (e1 only) and no indication that e2 has an answer
    And a collection manager cleared SECRET sees R as ANSWERED

  Scenario: Expiry by date only
    Given R is ANSWERED for the manager but PARTIAL for Q
    When the due date passes without CMD-CRQ-MARK-SATISFIED
    Then R is EXPIRED regardless of fulfilment
```
