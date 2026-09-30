---
id: TST-SLC06-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-06 membership, alerts, COP, tiles, notifications
wave: W6
slice: SLC-06
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-SIT-001, REQ-SIT-002, REQ-SIT-003, REQ-SIT-004, REQ-SIT-005, REQ-SIT-006, REQ-SIT-007, REQ-COM-001, REQ-COM-002, QAS-PERF-005, QAS-PERF-006, QAS-PERF-007, QAS-SEC-004, QAS-SEC-012, QAS-OPS-003]}
---

# Acceptance — Situation, Alerts & Notifications

```gherkin
Feature: Membership                                                              # REQ-SIT-002, INV-SIT-03

  Scenario: Object entering the extent joins the situation
    Given ACTIVE situation S "Eastern floods" with extent P and criteria object_types = [entity], entity_types = [road]
    When road R's location claim moves inside P
    Then within 10 s R is a member of S with cause = the claim event
    And a "joined" change is recorded

  Scenario: Unvalidated observations excluded by default
    Given S includes observations
    When an observation inside P is RECORDED but not VALIDATED
    Then it is not a member until validated

  Scenario: Membership history is reproducible
    Given S's definition changed at t from extent P to P2
    Then membership at t − 1 s is evaluated with P and membership after t with P2

  Scenario: Buffer extent follows its anchor
    Given S with extent = buffer 5 km around convoy C
    When C moves 20 km
    Then members are re-evaluated around C's new location

Feature: Alerts                                                                  # REQ-SIT-004..006

  Scenario: Critical threshold alert end-to-end
    Given ACTIVE rule "water level > 3 m" (critical) on S with subscriber U cleared for its label
    When a sensor observation of 3.4 m inside P is ingested
    Then U receives an in-app notification within 5 s (p95)

  Scenario: Dedupe within window
    Given the same sensor reports 3.5 m and 3.6 m within the dedupe window
    Then one alert exists with occurrences = 3

  Scenario: Uncleared subscriber receives nothing                                  # INV-ALR-02, QAS-SEC-012
    Given the triggering observation is labelled SECRET and subscriber V is cleared CONFIDENTIAL
    When the alert is raised
    Then V receives no notification, no push, and V's alert list and counts are unchanged

  Scenario: Dismissal requires a reason                                           # REQ-SIT-005
    When a recipient dismisses an alert without reason
    Then the command is rejected with REASON_REQUIRED

  Scenario: Active rules cannot be edited silently                                # INV-ARL-01
    When an analyst edits an ACTIVE rule
    Then the command is rejected (state ACTIVE does not accept CMD-ARL-EDIT)

  Scenario: Paused situation suppresses its rules
    Given S is PAUSED
    When the threshold is exceeded
    Then no alert is raised

Feature: COP and tiles                                                           # REQ-SIT-003, REQ-SIT-007

  Scenario: Per-member filtering in the picture
    Given S has 12 members of which 2 are SECRET
    When U (CONFIDENTIAL) reads the picture
    Then 10 members are returned and all counts show 10

  Scenario: Tiles never shared across scopes                                      # QAS-SEC-004
    Given U (CONFIDENTIAL) and W (SECRET) request the same tile
    Then the responses differ and have different ETags
    And no cache entry keyed by W's scope is served to U

  Scenario: Revocation changes the tile on the next request
    Given U has a cached tile containing member M
    When M is reclassified above U's clearance
    Then U's next request for that tile does not contain M

  Scenario: Generalized geometry in tiles
    Given tenant policy generalize(1000 m) for Operators
    Then an Operator's tile places members at deterministic 1 km cell centres

Feature: Notifications                                                           # REQ-COM-001, REQ-COM-002

  Scenario: Push payload contains a reference only
    When a push is delivered for alert A
    Then the payload contains A's URN and a template title, and no names, places or values

  Scenario: Revoked recipient is withheld at delivery
    Given a queued notification for U
    When U's clearance is revoked before delivery
    Then the notification becomes WITHHELD

  Scenario: Opening after revocation shows not-found
    Given U received a notification and later lost access
    When U opens it
    Then the referenced object returns not-found

  Scenario: Air-gapped fallback                                                    # QAS-OPS-003
    Given the push relay is unavailable
    Then the mobile app shows new notifications through polling within 60 s

  Scenario: Subscription ends when target becomes invisible                        # INV-SUB-02
    Given U subscribes to S
    When S is reclassified above U's clearance
    Then U's subscription is ENDED
```
