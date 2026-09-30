---
id: TST-SLC02-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-02 temporal, claims, security and ingestion scenarios
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-INF-001, REQ-INF-002, REQ-INF-003, REQ-INF-004, REQ-INF-005, REQ-INF-006, REQ-INF-007, REQ-INF-008, REQ-INF-009, REQ-INF-020, REQ-INF-021, REQ-INF-022, REQ-INF-023, REQ-INF-024, REQ-INF-026, REQ-INF-027, REQ-INF-028, REQ-INF-029, REQ-INF-030, REQ-INF-031, REQ-INF-035, REQ-INF-036, REQ-INF-037, QAS-TMP-001, QAS-SEC-009, QAS-SEC-010, QAS-DQ-001]}
---

# Acceptance — Temporal, Claims, Security & Ingestion

```gherkin
Feature: Bitemporal claims                                                     # REQ-INF-022..024, TEMPORAL-MODEL §5

  Background:
    Given asset X and source S rated B

  Scenario: Correction versus as-known-at
    Given on 2026-03-01 claim C1 "location of X = A" valid from 2026-03-01 is asserted
    And on 2026-03-10 C1 is corrected to "B" valid from 2026-03-01
    Then resolve(X, location, valid_at = 2026-03-05, known_at = 2026-03-05) = A
    And resolve(X, location, valid_at = 2026-03-05, known_at = now) = B
    And C1 has recorded_to = 2026-03-10 and remains retrievable

  Scenario: Change in reality keeps both periods true
    Given claim "status of X = operational" valid from 2026-01-01
    When a change to "damaged" is recorded at t_change = 2026-04-01
    Then resolve(valid_at = 2026-03-31) = operational
    And resolve(valid_at = 2026-04-01) = damaged
    And no value known before the change is altered

  Scenario: Half-open interval boundary
    Given claim valid [2026-01-01T00:00:00Z, 2026-02-01T00:00:00Z)
    Then resolve(valid_at = 2026-02-01T00:00:00Z) is EMPTY
    And resolve(valid_at = 2026-01-31T23:59:59.999999Z) returns the value

  Scenario: Record time is never client-supplied
    When a client sends CMD-CLM-ASSERT containing recorded_from
    Then the command is rejected with VALIDATION_FAILED

  Scenario: No automatic winner
    Given claims "name = مستودع الشمال" (source A) and "name = مستودع الساحل" (source F) valid now
    Then the resolved name status is DISPUTED with both values
    And no value is chosen by confidence

  Scenario: Arabic variants corroborate
    Given claims "name = أحمد" and "name = احمد" from two sources
    Then the resolved name status is CORROBORATED                               # language-model N3

  Scenario: Units are normalized before comparison
    Given claims "length = 1.2 km" and "length = 1200 m"
    Then the resolved length status is CORROBORATED

Feature: Visibility-first resolution                                            # INV-ENT-02, QAS-SEC-010

  Scenario: Hidden claim does not create a dispute
    Given claim C1 "owner = O1" labelled INTERNAL and claim C2 "owner = O2" labelled SECRET
    And user U cleared CONFIDENTIAL
    When U reads the entity
    Then owner status is SINGLE with value O1
    And completeness, claim counts and response timing are indistinguishable from an entity without C2

  Scenario: Protected source identity                                            # QAS-SEC-009, PB-08
    Given source S of type person with protection level 2
    And user U without permission source.identity.view
    When U reads a claim citing S
    Then the response contains S's type and reliability only
    And lineage and exports from U contain no identity attribute of S

  Scenario: Location generalization                                             # PB-10
    Given tenant policy generalize(1000 m) for role Operator on level CONFIDENTIAL
    When an Operator reads positions of X
    Then each geometry is a 1 km grid-cell centre, accuracy_m ≥ 1000 and flagged GENERALIZED
    And repeated reads return the same cell

Feature: Observations and geometry                                              # REQ-INF-002, REQ-INF-028, REQ-INF-029

  Scenario: Geometry without accuracy is rejected
    When an observation is recorded with geometry but no accuracy_m
    Then the command is rejected with OBSERVATION_INVALID

  Scenario: Original CRS is preserved
    When an observation arrives in EPSG:32638
    Then geometry is stored in EPSG:4326 and crs_original = EPSG:32638 with the original coordinates

  Scenario: Validation segregation
    Given observation O recorded by user F
    When F validates O
    Then the command is rejected with SEGREGATION_OF_DUTIES

  Scenario: Clock skew is flagged, not trusted
    Given a device clock 20 minutes ahead
    When it syncs an observation
    Then recorded_from = server receipt time
    And data_quality contains DEVICE_CLOCK_SUSPECT

  Scenario: Batch ingestion is idempotent                                       # QAS-PERF-012
    Given a batch of 1,000 observations each with an item idempotency key
    When the same batch is sent twice
    Then exactly 1,000 observations exist

Feature: Evidence and attachments                                               # REQ-INF-003, REQ-INF-004

  Scenario: Content-addressed dedupe
    Given attachment with sha256 H is STORED in tenant T
    When another upload with sha256 H is initiated in tenant T
    Then the existing attachment is returned and no upload target is issued

  Scenario: Hash mismatch
    When the uploaded bytes do not match the declared sha256
    Then CMD-ATT-COMPLETE-UPLOAD is rejected with HASH_MISMATCH

  Scenario: Integrity on retrieval
    Given a STORED object whose bytes were altered in storage
    When a download grant is used
    Then the platform reports INTEGRITY_ERROR and audits the event

  Scenario: Withdrawn evidence re-evaluates verification
    Given claim C VERIFIED only by evidence E
    When E is withdrawn
    Then C's verification_status is recomputed to UNVERIFIED
    And E and its links remain retrievable

Feature: Ingestion                                                               # REQ-INF-005..009

  Scenario: Same batch key and content returns the same batch
    When adapter A submits batch_key K with content hash H twice
    Then one batch exists and the second call returns it

  Scenario: Same batch key with different content is rejected
    When adapter A submits batch_key K with content hash H2 ≠ H
    Then the command is rejected with BATCH_KEY_REUSED

  Scenario: Invalid records are quarantined, never published                     # QAS-DQ-001
    Given a batch with 3 records without CRS
    When processing finishes
    Then the batch is COMPLETED_WITH_QUARANTINE with 3 quarantine records
    And none of the 3 appears in any query

  Scenario: External systems are not truth                                        # BRL-013
    When an imported record sets "status = closed" for entity X
    Then a claim is asserted citing the adapter's source
    And any existing contradicting claim remains, producing DISPUTED if incompatible

  Scenario: External id is unique at a time                                     # INV-EXT-01
    Given (ERP, 123) is ACTIVE for X
    When (ERP, 123) is mapped to Y
    Then the command is rejected with EXTERNAL_ID_TAKEN

Feature: Lineage                                                                 # REQ-INF-035

  Scenario: Derived claim traces to observation and source
    Given claim C derived from observation O recorded from source S
    When lineage of C is traced upstream
    Then the path C → O → S is returned with versions and times

  Scenario: Invisible nodes cut the path
    Given O is labelled above the reader's clearance
    Then the upstream trace of C stops at C without revealing O (default policy)
```
