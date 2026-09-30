---
id: TST-SLC04-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-04 conflicts, merge/split and visibility
wave: W6
slice: SLC-04
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-INF-025, REQ-INF-032, REQ-INF-033, REQ-INF-034, REQ-INF-024, REQ-SRC-003, QAS-ER-001, QAS-ER-002, QAS-CNF-001, QAS-PERF-015]}
---

# Acceptance — Conflicts, Merge/Split & Visibility

```gherkin
Feature: Conflict detection and resolution                                      # REQ-INF-025, BRL-002

  Scenario: Incompatible claims open one conflict
    Given claims C1 "capacity = 200 t" and C2 "capacity = 350 t" on warehouse W with overlapping validity
    When C2 is committed
    Then exactly one conflict on (W, capacity) is OPEN with members C1, C2 within 30 s
    And C1 and C2 are unchanged

  Scenario: A third claim joins the existing conflict
    Given an OPEN conflict K on (W, capacity)
    When claim C3 "capacity = 500 t" with overlapping validity is committed
    Then C3 is added to K and no new conflict is opened

  Scenario: Resolution is known-at, not retroactive
    Given conflict K resolved on 2026-05-10 preferring C1
    Then resolve(W, capacity, valid_at = now, known_at = 2026-05-09) is DISPUTED
    And resolve(W, capacity, valid_at = now, known_at = now) is SINGLE with C1

  Scenario: Retracting a member supersedes the conflict
    Given conflict K with members C1, C2
    When C2 is retracted
    Then K is SUPERSEDED and W's capacity resolves SINGLE

  Scenario: Reviewer cannot prefer own claim
    Given C1 asserted by analyst A
    When A resolves K preferring C1
    Then the command is rejected with SEGREGATION_OF_DUTIES

  Scenario: Conflict invisible when only one side is visible                     # INV-CNF-04
    Given C1 labelled INTERNAL and C2 labelled SECRET in conflict K
    And user U cleared CONFIDENTIAL
    Then QRY-CNF-LIST for U does not include K
    And W's capacity resolves SINGLE for U

Feature: Merge without rewriting                                                # REQ-INF-033, INV-ER-01

  Scenario: Matched entities resolve as one
    Given entity E1 with claim "name = مستودع الشمال" and E2 with claim "phone = 555"
    When a case E1–E2 is decided MATCHED
    Then resolve(E2) returns canonical_urn = min(E1, E2) and requested_urn = E2
    And the result contains both name and phone
    And every claim keeps its original subject_urn

  Scenario: A merge can reveal a conflict
    Given E1 "status = open" and E2 "status = closed" valid now
    When E1–E2 is decided MATCHED
    Then a conflict on (cluster, status) is opened

  Scenario: Identity as known at a time
    Given E1–E2 MATCHED on 2026-06-01
    Then cluster(E2, known_at = 2026-05-31) = {E2}
    And cluster(E2, known_at = now) = {E1, E2}

  Scenario: NOT_A_MATCH blocks transitive merges                                  # INV-ER-03
    Given E1–E3 decided NOT_A_MATCH and E1–E2 MATCHED
    When E2–E3 is decided MATCHED
    Then the command is rejected with MATCH_CONTRADICTS_NOT_A_MATCH

  Scenario: Large clusters need a second reviewer                                 # INV-ER-05
    Given a cluster with 50 members
    When a reviewer decides a match adding one more member without second_reviewer
    Then the command is rejected

  Scenario: No automatic merge                                                    # INV-ER-04
    Given the candidate generator scores a pair at 0.99
    Then a CANDIDATE case exists and no MATCH link exists until a human decision

Feature: Split restores exactly                                                   # REQ-INF-034

  Scenario: Split returns each entity to its own claims
    Given E1–E2 MATCHED and 5 claims later asserted on E1 and 3 on E2
    When a split is requested by A and executed by B
    Then resolve(E1) contains exactly E1's claims and resolve(E2) exactly E2's
    And the conflict opened by the merge becomes SUPERSEDED
    And cluster(E2, known_at = before split) still includes E1

  Scenario: The requester cannot execute the split
    When the split requester executes CMD-ER-SPLIT
    Then the command is rejected with SEGREGATION_OF_DUTIES

Feature: Visibility in resolution work                                           # THR-S04-02..04

  Scenario: Case invisible if one entity is hidden
    Given E2 labelled SECRET and user U cleared CONFIDENTIAL
    Then no case involving E2 appears in U's queue

  Scenario: Cluster endpoint omits hidden members
    Given cluster {E1, E2, E3} where E3 is hidden from U
    Then U's identity-cluster response lists E1, E2 only, with no count or marker of E3

  Scenario: Decision basis is recorded
    Given reviewer R cleared CONFIDENTIAL decides E1–E2 MATCHED
    Then the case records decision_basis_level = CONFIDENTIAL

Feature: Candidate generation quality                                            # QAS-ER-001, QAS-ER-002, REQ-SRC-003

  Scenario: Ruleset below target cannot be activated
    Given a draft ruleset whose evaluation recall is 91 %
    When it is activated
    Then the command is rejected with RULESET_BELOW_TARGET

  Scenario Outline: Arabic name variants are proposed
    Given entity A named <a> and entity B named <b> in the same geohash cell
    Then a CANDIDATE case A–B is proposed

    Examples:
      | a                      | b                       |
      | محمد بن عبدالله الأحمد | محمد عبد الله احمد      |
      | Mohammed Al-Ahmad      | محمد الأحمد             |
      | أبو خالد               | Abu Khaled              |
```
