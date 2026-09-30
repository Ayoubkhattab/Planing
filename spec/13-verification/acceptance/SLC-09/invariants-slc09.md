---
id: TST-SLC09-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-09 availability, reservations, allocation contention, pre-emption, readiness
wave: W6
slice: SLC-09
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-004, REQ-RES-005, REQ-RES-006, REQ-RES-007, REQ-RES-008, REQ-RES-009, REQ-RES-010, REQ-RES-011, REQ-RES-012, REQ-RES-013, REQ-RES-014, QAS-RES-001, QAS-RES-002]}
---

# Acceptance — Assets & Resources

```gherkin
Feature: Asset availability                                                       # REQ-RES-003/004/014

  Scenario: Expired certification blocks assignment at read time
    Given crane C requires certification LIFT-A valid until 12:00
    When C is assigned for a window starting 12:30
    Then the command is rejected with ASSET_NOT_AVAILABLE and reason CERTIFICATION_EXPIRED

  Scenario: Maintenance window blocks availability
    Given a PLANNED maintenance order for C on [08:00, 16:00)
    When availability for C on [10:00, 11:00) is queried
    Then C is unavailable with reason MAINTENANCE

  Scenario: Overlapping reservations rejected
    Given C is HELD for [09:00, 12:00)
    When another planner holds C for [11:00, 13:00)
    Then the command is rejected with ASSET_RESERVED

  Scenario: Unconfirmed hold expires
    Given a HELD reservation not confirmed for 24 h
    Then it is EXPIRED and C becomes available for that window

  Scenario: Hidden blocker is not revealed                                         # THR-S09-03
    Given C is assigned to a SECRET task and planner P is cleared CONFIDENTIAL
    Then P sees C as unavailable without the task reference

Feature: Custody                                                                    # REQ-RES-002

  Scenario: Only the holder transfers custody
    Given C's custody holder is H1
    When user H2 transfers custody to H3
    Then the command is rejected with CUSTODY_INVALID

Feature: Asset location as claims                                                    # REQ-RES-005

  Scenario: Past location is retrievable
    Given C moved from depot A (valid until 1 May) to site B
    Then resolve(C.linked_entity, location, valid_at = 30 April) = depot A

Feature: Allocation checks and contention                                           # REQ-RES-007/008, QAS-RES-001

  Scenario: Each failed check has its own reason
    Given a pool in region R and a target task in region S
    When an allocation is requested
    Then it is REJECTED with GEOGRAPHY_MISMATCH

  Scenario: No over-commitment under concurrency
    Given pool P has capacity 100 units for the window
    When 100 concurrent requests of 5 units with random priorities arrive
    Then exactly 20 are COMMITTED, total committed = 100
    And within each ordering window committed requests have priority ≥ every rejected request of that window

  Scenario: Approval hold
    Given tenant policy requires approval for allocations above 50 units
    When a planner requests 60 units
    Then the allocation is PENDING_APPROVAL with capacity provisionally held
    When the requester approves it
    Then the command is rejected with SEGREGATION_OF_DUTIES

Feature: Pre-emption                                                                 # REQ-RES-009

  Scenario: No automatic pre-emption
    Given capacity fully committed at priority 2
    When a priority-5 allocation is requested
    Then it is REJECTED with CAPACITY_UNAVAILABLE and lists the lower-priority allocations holding capacity

  Scenario: Authorized pre-emption
    Given decision D of type resource-preemption by the pool-scope authority
    When allocation A (priority 2) is pre-empted referencing D
    Then A is PREEMPTED, its task owner is notified, and capacity becomes available

Feature: Consumption and release                                                     # REQ-RES-010/011

  Scenario: Over-consumption flagged
    Given allocation of 10 units
    When 12 units are recorded
    Then an over-consumption flag is raised for review

  Scenario: Task completion releases unused capacity
    Given allocation of 10 units for task T with 6 consumed
    When T becomes COMPLETED
    Then the allocation is RELEASED and 4 units return to the ledger for the remaining hours

Feature: Readiness                                                                   # REQ-RES-013

  Scenario: Training recency matters
    Given role R requires training SAFETY within P12M
    And person X completed SAFETY 14 months ago
    Then readiness(X, R, now) is REQUIRES_TRAINING with gap SAFETY

Feature: DEBT-001 migration                                                           # REQ-RES-012

  Scenario: Legacy notes kept when not matched
    Given plan version notes "crane from depot A"
    When migration proposes asset C and the planner rejects it
    Then the note stays as legacy_note and appears in the migration report
```
