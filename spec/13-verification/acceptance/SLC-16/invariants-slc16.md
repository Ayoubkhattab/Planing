---
id: TST-SLC16-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-16 enterprise integrations
wave: W6
slice: SLC-16
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-INT-001, REQ-INT-002, REQ-INT-003, REQ-INT-004, QAS-INT-001]}
---

# Acceptance — Enterprise Integrations

```gherkin
Feature: Connections and sources of truth                                         # REQ-INT-001

  Scenario: Activation needs a second person's allow-list approval
    When the requester of connection C approves its allow-list entry
    Then the command is rejected with SEGREGATION_OF_DUTIES

  Scenario: No writes to enterprise systems in R2
    When an outbound connection of kind erp is registered
    Then the command is rejected with CONNECTION_INVALID

  Scenario: ERP value conflicting with a field observation
    Given a field claim "warehouse W capacity = 200 t" and ERP reports 350 t
    When the ERP batch is applied
    Then a claim citing the ERP source is asserted and a conflict is opened; nothing is overwritten

  Scenario: Outage without loss                                                   # QAS-INT-001
    Given the ERP connection is unreachable for 4 hours
    When it recovers
    Then all records since the last watermark are processed within 1 hour with no duplicates

Feature: Sensors                                                                  # REQ-INT-002

  Scenario: Readings become observations in batches
    Given an ACTIVE stream at 2,000 readings/s
    Then observations are recorded in batches of ≤ 1,000 with per-item idempotency and observed_at = sensor time

  Scenario: Quality violations annotate, never drop
    When a reading exceeds the configured max
    Then the observation is recorded with a data_quality issue OUT_OF_RANGE

Feature: HR synchronization                                                       # REQ-INT-004

  Scenario: HR move produces a proposal, not an access change
    Given HRIS reports person P moved from unit A to unit B
    Then a PROPOSED change (revoke A roles, assign B roles) exists and P's access is unchanged
    When an administrator of A and B approves it
    Then the role assignments change through CMD-RAS-* with their guards (e.g. SoD)

  Scenario: Leave is escalated
    Given a leave proposal pending 14 days
    Then it EXPIRES and a Security Officer is notified
    And account disablement through SCIM, when received, still applies immediately

Feature: CAP                                                                       # REQ-INT-003

  Scenario: Release requires a second person
    Given a prepared CAP message for alert A
    When the preparer releases it
    Then the command is rejected with SEGREGATION_OF_DUTIES

  Scenario: Classified alerts cannot be exported
    Given tenant external release level INTERNAL and alert A labelled CONFIDENTIAL
    When a CAP message is prepared for A
    Then the command is rejected with RELEASE_NOT_ALLOWED

  Scenario: Valid CAP only
    When a message is released
    Then the payload validates against CAP 1.2 and contains only template fields
```
