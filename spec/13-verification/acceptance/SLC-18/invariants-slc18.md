---
id: TST-SLC18-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-18 logistics request / allocation / shipment linkage
wave: W6
slice: SLC-18
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
traces: {verifies: [REQ-LOG-001, REQ-LOG-002, REQ-LOG-003, REQ-LOG-004, REQ-LOG-006, REQ-LOG-008, REQ-LOG-009, QAS-LOG-001, QAS-LOG-002]}
---

# Acceptance — Logistics Request / Allocation / Shipment linkage

```gherkin
Feature: Creating a logistics request always links an allocation                 # REQ-LOG-001/002/003

  Scenario: Request creation issues a linked allocation in the same unit of work
    When the actor sends CMD-LGR-REQUEST for item_pool P, quantity 100, needed_by T
    Then a Logistics Request L exists in state REQUESTED
    And exactly one Allocation A exists with target = L, in state REQUESTED
    And A was created in the same transaction as L

  Scenario: Approval routing exactly mirrors the linked allocation
    Given logistics request L with linked allocation A, both REQUESTED
    When A's checks all pass and it becomes COMMITTED (EVT-ALC-COMMITTED)
    Then L becomes APPROVED as a system-driven consequence, with no request-level approval command involved
    Given a different logistics request L2 whose linked allocation A2 requires approval
    When A2 becomes PENDING_APPROVAL (EVT-ALC-APPROVAL-REQUIRED)
    Then L2 becomes PENDING_APPROVAL
    When A2 is later rejected (EVT-ALC-REJECTED)
    Then L2 becomes REJECTED

Feature: Dispatch never outruns the capacity ledger                              # REQ-LOG-004, INV-SHP-02/03

  Scenario: Dispatch fails once the linked allocation is no longer committed
    Given logistics request L is APPROVED with linked allocation A COMMITTED
    And A is separately released (CMD-ALC-RELEASE) before dispatch
    When the actor sends CMD-LGR-DISPATCH for L
    Then the command is rejected with ALLOCATION_NOT_COMMITTED
    And no Shipment is created

  Scenario: Successful dispatch bounds the shipment to the requested quantity
    Given logistics request L is APPROVED for quantity 100 with linked allocation A COMMITTED
    When the actor sends CMD-LGR-DISPATCH with ship_quantity 100
    Then L becomes IN_TRANSIT
    And a Shipment S is created with planned_quantity 100, referencing L and A
    And CMD-SHP-PLAN's guard confirms A is still COMMITTED for at least 100 at that instant (INV-SHP-03)

Feature: Delivery outcome decides fulfillment, never a default                    # REQ-LOG-006/008, INV-LGR-03/05

  Scenario: Full delivery fulfills the request and records consumption
    Given shipment S for logistics request L, planned_quantity 100, IN_TRANSIT
    When the receiving party sends CMD-SHP-DELIVER with delivered_quantity 100
    Then S becomes DELIVERED
    And L becomes FULFILLED
    And CMD-ALC-RECORD-CONSUMPTION is recorded on L's linked allocation for quantity 100

  Scenario: A shortfall, damage, or loss never fulfills the request
    Given shipment S for logistics request L, planned_quantity 100, IN_TRANSIT
    When the receiving party sends CMD-SHP-DELIVER with delivered_quantity 60
    Then S becomes DELIVERED with delivered_quantity 60 recorded, not silently rounded to 100
    And L becomes PARTIALLY_FULFILLED, never FULFILLED
    Given a different shipment S2 for logistics request L2, IN_TRANSIT
    When the carrier reports CMD-SHP-REPORT-LOST
    Then S2 becomes LOST
    And L2 becomes PARTIALLY_FULFILLED with consumption recorded for the quantity actually delivered before the loss (possibly zero)

  Scenario: Consumption is never recorded before the shipment resolves
    Given shipment S for logistics request L, PLANNED
    Then no CMD-ALC-RECORD-CONSUMPTION exists yet for L's linked allocation
    When S departs (CMD-SHP-DEPART) and is IN_TRANSIT
    Then consumption is still not recorded
    When S finally reaches DELIVERED, DAMAGED or LOST
    Then consumption is recorded exactly once, only then

Feature: Cancellation always releases what it reserved                           # REQ-LOG-009, INV-LGR-04, INV-SHP-04

  Scenario: Cancelling a request before dispatch releases its allocation
    Given logistics request L is APPROVED with linked allocation A COMMITTED
    When the actor sends CMD-LGR-CANCEL with a reason
    Then L becomes CANCELLED
    And A is released (CMD-ALC-RELEASE), never left dangling COMMITTED

  Scenario: A shipment cannot be cancelled once in transit
    Given shipment S is PLANNED
    When the actor sends CMD-SHP-CANCEL with a reason
    Then S becomes CANCELLED
    Given shipment S2 is IN_TRANSIT
    When the actor sends CMD-SHP-CANCEL
    Then the command is rejected with SHIPMENT_INVALID_STATE_TRANSITION
    And S2 must instead resolve to DELIVERED, DAMAGED or LOST
```
