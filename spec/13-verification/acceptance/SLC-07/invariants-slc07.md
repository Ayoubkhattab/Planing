---
id: TST-SLC07-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-07 reproducibility, execution security, assessment rules
wave: W6
slice: SLC-07
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-ANL-001, REQ-ANL-002, REQ-ANL-003, REQ-ANL-004, REQ-ANL-005, REQ-ANL-006, REQ-ANL-007, REQ-ANL-008, REQ-INF-035, QAS-TRC-001, QAS-TRC-002, QAS-SEC-013, QAS-PERF-020]}
---

# Acceptance — Analytical Work

```gherkin
Feature: Reproducibility                                                          # REQ-ANL-003, QAS-TRC-002

  Scenario: Re-execution after data changed gives the same result
    Given run R1 (deterministic method M v1.2) SUCCEEDED on inputs pinned at K1
    And the underlying claims were corrected after K1
    When an analyst reproduces R1
    Then the new run reads data as known at K1
    And the reproduction report is REPRODUCED with identical result hashes

  Scenario: Different environment is reported, not hidden
    Given method M v1.2 image was rebuilt with a different digest (new method version v1.3)
    When R1 is reproduced
    Then the reproduction uses v1.2's recorded digest
    And if v1.2 were unavailable the command would be rejected, not silently switched

  Scenario: Reproducer must be cleared for the source run
    Given R1 labelled SECRET and analyst A cleared CONFIDENTIAL
    When A reproduces R1
    Then the command is rejected with REPRODUCTION_NOT_ALLOWED

  Scenario: Method backing published work cannot be retired
    Given a PUBLISHED assessment citing a finding from a run of M v1.2
    When an administrator retires M v1.2
    Then the command is rejected with METHOD_BACKS_PUBLISHED_WORK

Feature: Execution security                                                       # QAS-SEC-013

  Scenario: Run sees only the submitter's data
    Given dataset D has 100 visible and 20 SECRET observations for analyst A (CONFIDENTIAL)
    When A runs a count over D
    Then the run result is 100 and the run label is ≤ CONFIDENTIAL

  Scenario: Long run is asynchronous                                              # REQ-ANL-004
    When a run is submitted
    Then the API returns 201 with the run reference in ≤ 1 s and state QUEUED

  Scenario: Fair scheduling                                                        # QAS-PERF-020
    Given tenant T1 submits 100 runs and its quota is 5 concurrent
    Then at most 5 of T1's runs are RUNNING and T2's new run starts within 30 s

Feature: Case rules                                                                # REQ-ANL-001

  Scenario: Case cannot open without question and scope
    When a DRAFT case without a time window is opened
    Then the command is rejected with CASE_NOT_DEFINED

  Scenario: Evidence above the case label is refused                              # INV-ACS-02
    Given a CONFIDENTIAL case
    When a SECRET observation is selected
    Then the command is rejected with EVIDENCE_ABOVE_CASE_LABEL

  Scenario: Selections are pinned in time                                         # INV-ACS-01
    When an analyst selects claim C at time K
    Then the selection stores known_at = K and later corrections of C do not change what the case shows as selected

Feature: Findings and assessments                                                  # REQ-ANL-005, REQ-ANL-006

  Scenario: Incomplete assessment cannot be submitted
    Given a draft without limitations
    When it is submitted
    Then the command is rejected with ASSESSMENT_INCOMPLETE

  Scenario: Author cannot publish own assessment
    When the author publishes
    Then the command is rejected with SEGREGATION_OF_DUTIES

  Scenario: Publishing a revision supersedes the previous version atomically
    Given version 1 PUBLISHED and version 2 IN_REVIEW
    When version 2 is published
    Then version 1 is SUPERSEDED and version 2 is PUBLISHED in the same transaction

  Scenario: Decisions keep the version they relied on                              # INV-ASM-03
    Given decision D cites assessment A version 1
    When version 2 is published
    Then D still resolves its citation to version 1

  Scenario: Key judgments require estimative language
    When a key judgment is saved without a probability term
    Then the command is rejected with ASSESSMENT_INVALID

  Scenario: Withheld citations for compartmented readers                           # REQ-ANL-008
    Given assessment A cites evidence E in compartment K
    And reader R is cleared for A's level but not K
    Then R sees A without E's identifier or content and no marker of omission (default policy)

Feature: Scenarios                                                                  # REQ-ANL-007

  Scenario: Compare scenarios
    Given two scenarios with different assumption sets and one SUCCEEDED run each
    Then the comparison shows both results side by side with the differing assumptions and inputs

Feature: Lineage                                                                    # REQ-INF-035, QAS-TRC-001

  Scenario: Assessment traces to sources
    Given a PUBLISHED assessment
    When lineage is traced upstream
    Then every key judgment reaches findings, runs (with method version and image digest) and source observations/claims with known_at
```
