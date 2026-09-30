---
id: TST-ARCHIVE-PACKAGE-SM
type: acceptance-spec
title: Acceptance — Archive Package (AIP) state machine
wave: W6
slice: SLC-12
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ARCHIVE-PACKAGE
traces:
  verifies:
  - SL-05
  - AGG-ARCHIVE-PACKAGE
  - REQ-ARC-001
  - REQ-ARC-002
  - REQ-ARC-003
---

# Acceptance — Archive Package (AIP)

مولّدة من مصفوفة AGG-ARCHIVE-PACKAGE: 4 انتقالاً مسموحاً، 20 رفضاً، 6 انتقالاً نظامياً (SYS).

```gherkin
Feature: Archive Package (AIP) lifecycle (AGG-ARCHIVE-PACKAGE)

  Background:
    Given an ACTIVE tenant, baseline policies, and an authorized actor
    And every guard of the command is satisfied

  Scenario Outline: allowed transition
    Given a <aggregate> in state <from> at version <v>
    When the actor sends <command> with a new Idempotency-Key and If-Match <v>
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And one audit record is written in the same transaction

    Examples:
      | aggregate | from | command | to | event | v |
      | Archive Package (AIP) | INGEST_FAILED | CMD-ARC-RETRY-INGEST | INGESTING | EVT-ARC-INGEST-STARTED | 3 |
      | Archive Package (AIP) | ARCHIVED | CMD-ARC-MIGRATE-FORMAT | ARCHIVED | EVT-ARC-FORMAT-MIGRATED | 3 |
      | Archive Package (AIP) | ARCHIVED | CMD-ARC-TRANSFER | TRANSFERRED | EVT-ARC-TRANSFERRED | 3 |
      | Archive Package (AIP) | INTEGRITY_FAILED | CMD-ARC-REPAIR | ARCHIVED | EVT-ARC-REPAIRED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Archive Package (AIP) | INGESTING | CMD-ARC-RETRY-INGEST | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | INGESTING | CMD-ARC-REPAIR | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | INGESTING | CMD-ARC-MIGRATE-FORMAT | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | INGESTING | CMD-ARC-TRANSFER | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | INGEST_FAILED | CMD-ARC-REPAIR | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | INGEST_FAILED | CMD-ARC-MIGRATE-FORMAT | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | INGEST_FAILED | CMD-ARC-TRANSFER | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | ARCHIVED | CMD-ARC-RETRY-INGEST | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | ARCHIVED | CMD-ARC-REPAIR | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | INTEGRITY_FAILED | CMD-ARC-RETRY-INGEST | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | INTEGRITY_FAILED | CMD-ARC-MIGRATE-FORMAT | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | INTEGRITY_FAILED | CMD-ARC-TRANSFER | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | TRANSFERRED | CMD-ARC-RETRY-INGEST | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | TRANSFERRED | CMD-ARC-REPAIR | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | TRANSFERRED | CMD-ARC-MIGRATE-FORMAT | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | TRANSFERRED | CMD-ARC-TRANSFER | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | DISPOSED | CMD-ARC-RETRY-INGEST | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | DISPOSED | CMD-ARC-REPAIR | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | DISPOSED | CMD-ARC-MIGRATE-FORMAT | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |
      | Archive Package (AIP) | DISPOSED | CMD-ARC-TRANSFER | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Archive Package (AIP) | ∅ | disposition action ARCHIVE for a bucket or record set | INGESTING | EVT-ARC-INGEST-STARTED |
      | Archive Package (AIP) | INGESTING | package validated | ARCHIVED | EVT-ARC-ARCHIVED |
      | Archive Package (AIP) | INGESTING | validation failed | INGEST_FAILED | EVT-ARC-INGEST-FAILED |
      | Archive Package (AIP) | ARCHIVED | integrity check failed | INTEGRITY_FAILED | EVT-ARC-INTEGRITY-FAILED |
      | Archive Package (AIP) | ARCHIVED | disposition DESTROY executed for the package bucket | DISPOSED | EVT-ARC-DISPOSED |
      | Archive Package (AIP) | INTEGRITY_FAILED | disposition DESTROY executed for the package bucket | DISPOSED | EVT-ARC-DISPOSED |
```
