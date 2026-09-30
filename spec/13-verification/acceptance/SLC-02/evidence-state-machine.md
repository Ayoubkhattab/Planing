---
id: TST-EVIDENCE-SM
type: acceptance-spec
title: Acceptance — Evidence state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-EVIDENCE
traces:
  verifies:
  - SL-05
  - AGG-EVIDENCE
  - REQ-INF-003
  - REQ-INF-004
---

# Acceptance — Evidence

مولّدة من مصفوفة AGG-EVIDENCE: 9 انتقالاً مسموحاً، 9 رفضاً.

```gherkin
Feature: Evidence lifecycle (AGG-EVIDENCE)

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
      | Evidence | REGISTERED | CMD-EVD-UPDATE-LOCATOR | REGISTERED | EVT-EVD-LOCATOR-UPDATED | 3 |
      | Evidence | REGISTERED | CMD-EVD-SEAL | SEALED | EVT-EVD-SEALED | 3 |
      | Evidence | REGISTERED | CMD-EVD-TRANSFER-CUSTODY | REGISTERED | EVT-EVD-CUSTODY-TRANSFERRED | 3 |
      | Evidence | REGISTERED | CMD-EVD-RECLASSIFY | REGISTERED | EVT-EVD-RECLASSIFIED | 3 |
      | Evidence | REGISTERED | CMD-EVD-WITHDRAW | WITHDRAWN | EVT-EVD-WITHDRAWN | 3 |
      | Evidence | SEALED | CMD-EVD-TRANSFER-CUSTODY | SEALED | EVT-EVD-CUSTODY-TRANSFERRED | 3 |
      | Evidence | SEALED | CMD-EVD-RECLASSIFY | SEALED | EVT-EVD-RECLASSIFIED | 3 |
      | Evidence | SEALED | CMD-EVD-WITHDRAW | WITHDRAWN | EVT-EVD-WITHDRAWN | 3 |
      | Evidence | WITHDRAWN | CMD-EVD-RECLASSIFY | WITHDRAWN | EVT-EVD-RECLASSIFIED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Evidence | CMD-EVD-REGISTER | REGISTERED | EVT-EVD-REGISTERED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Evidence | REGISTERED | CMD-EVD-REGISTER | EVIDENCE_INVALID_STATE_TRANSITION |
      | Evidence | SEALED | CMD-EVD-REGISTER | EVIDENCE_INVALID_STATE_TRANSITION |
      | Evidence | SEALED | CMD-EVD-UPDATE-LOCATOR | EVIDENCE_INVALID_STATE_TRANSITION |
      | Evidence | SEALED | CMD-EVD-SEAL | EVIDENCE_INVALID_STATE_TRANSITION |
      | Evidence | WITHDRAWN | CMD-EVD-REGISTER | EVIDENCE_INVALID_STATE_TRANSITION |
      | Evidence | WITHDRAWN | CMD-EVD-UPDATE-LOCATOR | EVIDENCE_INVALID_STATE_TRANSITION |
      | Evidence | WITHDRAWN | CMD-EVD-SEAL | EVIDENCE_INVALID_STATE_TRANSITION |
      | Evidence | WITHDRAWN | CMD-EVD-TRANSFER-CUSTODY | EVIDENCE_INVALID_STATE_TRANSITION |
      | Evidence | WITHDRAWN | CMD-EVD-WITHDRAW | EVIDENCE_INVALID_STATE_TRANSITION |
```
