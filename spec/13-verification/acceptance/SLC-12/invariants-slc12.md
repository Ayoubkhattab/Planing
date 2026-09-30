---
id: TST-SLC12-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-12 products, distribution, knowledge, archive, reconstruction
wave: W6
slice: SLC-12
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-PRD-001, REQ-PRD-002, REQ-PRD-003, REQ-PRD-004, REQ-PRD-005, REQ-KNW-001, REQ-KNW-002, REQ-KNW-003, REQ-ARC-001, REQ-ARC-002, REQ-ARC-003, REQ-ARC-004, QAS-PRD-001, QAS-PRD-002, QAS-KNW-001, QAS-ARC-001, QAS-ARC-002, QAS-ARC-003]}
---

# Acceptance — Products, Knowledge & Archive

```gherkin
Feature: Products                                                                  # REQ-PRD-001..003

  Scenario: Content above the product label is excluded silently
    Given a CONFIDENTIAL briefing whose situation has 12 members, 2 of them SECRET
    When the briefing is generated
    Then it shows 10 members, all counts say 10, and no text or marker indicates exclusions
    And the exclusion of 2 members is recorded only in the internal audit table

  Scenario: Generated data is pinned
    Given a product generated at K
    When a claim it shows is corrected after K
    Then the product still shows the value known at K, with the claim pinned at that version

  Scenario: Data sections cannot be hand-edited
    When the author edits a data-bound table section
    Then the command is rejected with SECTION_NOT_EDITABLE

  Scenario: Approval freezes and supersedes
    Given version 1 APPROVED and version 2 IN_REVIEW
    When version 2 is approved by a reviewer other than the author
    Then version 1 is SUPERSEDED and version 2 is immutable

  Scenario: Unreviewed AI section blocks submission
    Given a GENERATED product with an AI-drafted section not yet reviewed
    When it is submitted
    Then the command is rejected with PRODUCT_INCOMPLETE

Feature: Distribution                                                             # REQ-PRD-004/005

  Scenario: Unauthorized recipients are excluded
    Given a CONFIDENTIAL product distributed to U1 (CONFIDENTIAL) and U2 (INTERNAL)
    Then U1 receives a watermarked copy and U2 receives nothing
    And the distribution is COMPLETED_WITH_EXCLUSIONS listing U2 to the distributor

  Scenario: Each copy is traceable
    Given copies delivered to U1 and U3
    Then each PDF carries a distinct visible and invisible watermark id mapped to its recipient

Feature: Knowledge                                                                 # REQ-KNW-001..003

  Scenario: Lesson from closed work
    Given task T is CLOSED with evidence E
    When a user drafts a lesson with source T and links E
    Then the draft is accepted
    And a lesson with source an IN_PROGRESS task is rejected with KNOWLEDGE_INVALID

  Scenario: Author cannot publish own knowledge
    When the author publishes
    Then the command is rejected with SEGREGATION_OF_DUTIES

  Scenario: Suggestions by relationship
    Given a published lesson related to task type "road-clearance"
    When a planner creates an activity with task type "road-clearance"
    Then the lesson is suggested and, when used, its reuse count increases

  Scenario: Policy knowledge does not change authorization
    Given policy knowledge describing an access rule
    Then the PDP decision for that rule is unchanged by publishing or retiring it

Feature: Archive                                                                   # REQ-ARC-001..003

  Scenario: Package validity and preservation formats
    Given a disposition run with action ARCHIVE for class "operations-records" 2020-01
    Then an archive package exists as a valid BagIt bag with SHA-256 manifests
    And each document has its original and a PDF/A-2b representation

  Scenario: Fixity failure is repaired from replica
    Given a file in package X is altered in storage
    When the integrity check runs
    Then X becomes INTEGRITY_FAILED and after repair from replica it is ARCHIVED with a repair event

  Scenario: Retrieval is logged and timely
    When an authorized archivist retrieves a warm package
    Then content is available within 1 minute and the access history has a new entry

Feature: Reconstruction                                                             # REQ-ARC-004, QAS-ARC-002

  Scenario: Labelled reconstruction of a decision's context
    Given decision D recorded at K and plan P baselined before K
    When a reconstruction of (P, D basis) at T = K, known_at K is requested
    Then every element is labelled: claims RECORDED, plan version RECORDED, task states RECONSTRUCTED, positions between observations INFERRED (rule id), destroyed buckets UNKNOWN
    And repeating the request yields an identical report

  Scenario: Hidden elements are absent
    Given part of the scope is above the requester's clearance
    Then those elements are absent from the report without markers
```
