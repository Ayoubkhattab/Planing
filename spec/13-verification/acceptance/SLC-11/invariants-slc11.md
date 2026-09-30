---
id: TST-SLC11-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-11 offline capture, sync protocol, conflicts, device security
wave: W6
slice: SLC-11
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-OFF-001, REQ-OFF-002, REQ-OFF-003, REQ-OFF-004, REQ-OFF-005, REQ-OFF-006, QAS-OFF-001, QAS-OFF-002, QAS-OFF-003, QAS-SEC-007]}
---

# Acceptance — Offline & Sync

```gherkin
Feature: Offline capture                                                           # REQ-OFF-001

  Scenario: 72 hours offline
    Given a device offline for 72 hours
    When the user records 500 observations with photos and 100 task updates
    Then all are queued with seq, client_command_id, device_time and signatures

  Scenario: Capture continues after the offline limit, reading stops
    Given the device has been offline for 73 hours
    Then new observations can still be recorded
    And preloaded data can no longer be opened

Feature: Sync protocol                                                              # REQ-OFF-003, REQ-OFF-006, QAS-OFF-001

  Scenario: Full sync on a slow link
    Given 1,000 queued commands after 72 h offline
    When the device syncs on a 1 Mbps link
    Then all commands are processed within 10 minutes
    And observations have recorded_from = server receipt and observed_at = device time corrected by the measured offset

  Scenario: Interrupted sync resumes without duplicates
    Given a sync interrupted after seq 430 was acknowledged
    When the device reconnects
    Then the new session resumes at seq 431
    And no observation or task update is applied twice

  Scenario: Sequence gap is refused
    When a batch starts at seq 435 while acked_seq is 430
    Then the batch is rejected with SEQUENCE_GAP

  Scenario: Tampered queue detected
    Given an envelope whose prev_hash does not match
    Then the batch is rejected and a security event is logged

  Scenario: Client-generated ids are idempotent                                     # CR-50
    Given observation with client_id X was applied
    When the same envelope is delivered again
    Then exactly one observation with id X exists

Feature: Conflicts                                                                  # REQ-OFF-004

  Scenario: Stale task submission becomes a sync conflict
    Given the device queued SUBMIT for task T with base_version 5
    And T was reassigned online (version 6)
    When the device syncs
    Then SUBMIT is not applied and a sync conflict is OPEN with the original envelope and T's current state
    And the field user receives a conflict notice in the delta

  Scenario: Reapply still respects the owner's guards
    Given the conflict above
    When the reviewer reapplies it
    Then the command is rejected by BC04 (T is ASSIGNED to someone else) and the conflict stays OPEN with the owner's reason

  Scenario: Append-only commands never conflict on version
    Given the device queued 20 new observations
    Then all 20 are applied regardless of other changes

  Scenario: Observations disagreeing with existing claims go to the claims conflict engine, not sync conflicts   # CR-49
    Given a synced observation derives a claim incompatible with a current claim
    Then a Conflict (BC02, CF-01) is opened and no sync conflict is created

Feature: Device security                                                             # REQ-OFF-005, QAS-SEC-007

  Scenario: Lost device is wiped and its later commands reviewed
    Given device D reported lost at 10:00
    When D connects later with commands dated after 10:00
    Then the session is REJECTED with a WIPE instruction
    And no command from D is applied

  Scenario: Data unreadable without unlock
    Given a locked device
    Then preloaded data and queued attachments cannot be read from storage

  Scenario: Preload respects the offline level
    Given tenant offline max level INTERNAL
    When a user requests a package including CONFIDENTIAL objects
    Then the package excludes them (or the request is rejected with PRELOAD_NOT_ALLOWED if the requested level is above INTERNAL)

  Scenario: Permission lost while offline                                            # QAS-OFF-002
    Given user U lost compartment K while offline
    When U's device syncs
    Then packages containing K objects are revoked and purged
    And U's queued commands on K objects are rejected into sync conflicts

Feature: Reconnect storm                                                             # QAS-OFF-003

  Scenario: Shift start
    Given 5,000 devices reconnect within 10 minutes
    Then all sessions complete within 30 minutes with no data loss, oldest-offline first
```
