---
id: TST-SLC05-INVARIANTS
type: acceptance-spec
title: Acceptance — SLC-05 inference safety, revocation, Arabic search, graph, rebuild
wave: W6
slice: SLC-05
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {verifies: [REQ-SRC-001, REQ-SRC-002, REQ-SRC-003, REQ-SRC-004, REQ-FND-010, REQ-GOV-004, REQ-INF-027, QAS-SEC-002, QAS-SEC-003, QAS-SEC-011, QAS-USA-002, QAS-REL-002, QAS-REL-004, QAS-PERF-003, QAS-PERF-004]}
---

# Acceptance — Discovery

```gherkin
Feature: Inference-safe search                                                  # REQ-SRC-002, QAS-SEC-011

  Background:
    Given user U cleared CONFIDENTIAL without compartment "K"
    And entity E (INTERNAL) with claims: name "مصنع الشرق" (INTERNAL) and alias "مشروع النجم" (SECRET)
    And entity H (SECRET)

  Scenario: Hidden claim value does not find a visible entity
    When U searches "مشروع النجم"
    Then no hit is returned
    And visible_total is "0" and facets are empty

  Scenario: Visible claim value finds the entity without leaking the hidden alias
    When U searches "مصنع الشرق"
    Then E is returned and its snippet contains no text from the SECRET alias

  Scenario: Counts and facets ignore hidden objects
    Given 10 visible warehouses and 3 hidden warehouses in region R
    When U searches type=entity, facet=entity_type, geo=R
    Then visible_total is "10" and the warehouse bucket count is 10

  Scenario: Suggestions ignore hidden facts
    When U types "مشر"
    Then "مشروع النجم" is not suggested

  Scenario: Ranking ignores hidden facts
    Given E1 and E2 are identical in visible facts and E2 has an extra hidden matching fact
    When U searches the shared term
    Then E1 and E2 have equal scores

  Scenario: Cursor bound to scope
    Given a cursor issued to U
    When user V (different scope) uses it
    Then the request is rejected as VALIDATION_FAILED

Feature: Revocation beats index lag                                              # REQ-GOV-004, QAS-SEC-003

  Scenario: Reclassified object disappears on the next request
    Given E is visible to U and indexed
    When E is reclassified to SECRET at t
    And U searches at t + 1 s, before the index is updated
    Then E is not returned (LabelCheck re-check)

  Scenario: Revoked subject loses results immediately
    Given U's compartment "K" is revoked at t
    When U searches at t + 1 s
    Then no object labelled with "K" is returned

  Scenario: Owner unavailable fails closed
    Given BC04 LabelCheck is unavailable
    When U searches tasks and entities
    Then no task hits are returned
    And completeness is "partial_service_unavailable" regardless of whether tasks matched

Feature: Arabic and transliteration                                              # REQ-SRC-003, QAS-USA-002

  Scenario Outline: Spelling variants match
    Given entity with name <stored>
    When U searches <query>
    Then the entity is returned

    Examples:
      | stored              | query            |
      | أحمد إبراهيم        | احمد ابراهيم     |
      | مستشفى الأمل        | مستشفي الامل     |
      | عبدالرحمن           | عبد الرحمن       |
      | محمد                | Mohammed         |
      | الرياض              | Riyadh           |
      | ٢٠٢٦                | 2026             |

Feature: Graph visibility                                                        # REQ-INF-027, THR-S05-04

  Scenario: Hidden node cuts the path
    Given relationships A–B (INTERNAL) and B–C (INTERNAL) and B is SECRET
    When U asks for paths from A to C
    Then no path is returned

  Scenario: Hidden edge is not traversed
    Given A–C relationship labelled SECRET and A, C INTERNAL
    When U asks for the neighborhood of A at depth 1
    Then C is not included

  Scenario: Truncation reflects visible fan-out only
    Given node D with 450 visible and 200 hidden neighbours
    When U asks for the neighbourhood of D
    Then truncated is false and 450 neighbours are returned

  Scenario: Temporal graph
    Given relationship A–B valid [2025-01-01, 2026-01-01)
    Then the neighbourhood of A at valid_at 2026-03-01 excludes B

Feature: Projection lifecycle                                                   # REQ-SRC-004, QAS-REL-004

  Scenario: Rebuild equals source
    Given a new projection version built from owners' exports
    When it reaches READY
    Then the verification sample of 10,000 documents equals the source
    And the reference query set returns identical results on old and new versions

  Scenario: Queries keep working during rebuild
    While a version is BUILDING
    Then search is served by the ACTIVE version

  Scenario: Degraded projection is signalled
    Given projection lag exceeds 5 minutes
    Then the version becomes DEGRADED
    And responses carry completeness "partial_service_unavailable"
```
