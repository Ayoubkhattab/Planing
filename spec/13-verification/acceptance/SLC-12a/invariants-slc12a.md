---
id: TST-SLC12A-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-12a retention, holds, disposition, erasure, restore gate
wave: W6
slice: SLC-12a
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-GOV-006, REQ-GOV-007, REQ-GOV-008, QAS-PRV-001, QAS-PRV-002, QAS-GOV-001]}
---

# Acceptance — Retention & Erasure

```gherkin
Feature: Retention schedule                                                      # REQ-GOV-006

  Scenario: Schedule must cover every record class
    Given RD-RECORD-CLASSES has 20 classes and a draft covers 19
    When it is activated
    Then the command is rejected with SCHEDULE_INCOMPLETE

  Scenario: Drafter cannot activate
    When the drafter activates the schedule
    Then the command is rejected with SEGREGATION_OF_DUTIES

  Scenario: Shortening is not retroactive by default                             # INV-RTS-02
    Given class "observation-routine" changes from P5Y to P3Y without retroactive marking
    Then records triggered before activation keep P5Y

Feature: Legal hold                                                              # REQ-GOV-007

  Scenario: Held records survive disposition
    Given bucket (observation-routine, 2019-03) is past retention
    And 12 observations in it are covered by hold H
    When the disposition run executes
    Then the bucket key is destroyed
    And the 12 held observations remain readable (re-wrapped under H's key)
    And the certificate lists 12 held items excluded

  Scenario: Hold blocks erasure and person erasure                                # INV-ERS-02
    Given subject S is covered by hold H
    When an approved erasure request for S reaches execution
    Then it is BLOCKED_BY_HOLD until H is released

  Scenario: Hold blocks destructive commands in other contexts
    Given attachment A is covered by hold H
    When CMD-ATT-ERASE is sent for A
    Then it is rejected with LEGAL_HOLD_ACTIVE

  Scenario: Hold does not block versioned changes                                  # INV-LHD-02
    Given task T is covered by hold H
    When T is edited (new version)
    Then the edit succeeds and T's history is preserved

  Scenario: Release needs two authorities
    When the requester of a release approves it
    Then the command is rejected with SEGREGATION_OF_DUTIES

Feature: Disposition                                                                # QAS-GOV-001

  Scenario: Two-person approval and re-check
    Given a PLANNED run submitted by archivist A
    When A approves it
    Then the command is rejected with SEGREGATION_OF_DUTIES
    When legal officer L approves it and a new hold appeared since planning
    Then the new hold's items are excluded at approval

  Scenario: Destroyed bucket unreadable everywhere
    Given bucket B was destroyed
    Then no store, projection, archive or restored backup can decrypt records of B
    And a tombstone records class, bucket, count and run

Feature: Erasure                                                                    # REQ-GOV-008, QAS-PRV-001

  Scenario: Personal data unreadable, audit facts kept
    Given person P with personal attributes and 40 audit records
    When an approved erasure executes
    Then P's personal attributes are unreadable in all stores within 24 h (confirmations from BC01 and BC02)
    And the 40 audit records remain with a pseudonymous subject reference

  Scenario: Registrar cannot approve
    When the registrar approves the erasure
    Then the command is rejected with SEGREGATION_OF_DUTIES

Feature: Restore gate                                                                # QAS-PRV-002, CR-51

  Scenario: Old key-store backup does not revive destroyed keys
    Given subject key K was destroyed on day 10
    When the key store is restored from a day-5 backup
    Then the restore gate replays the destruction log before services start
    And K is unusable
```
