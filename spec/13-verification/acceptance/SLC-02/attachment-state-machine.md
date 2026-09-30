---
id: TST-ATTACHMENT-SM
type: acceptance-spec
title: Acceptance — Attachment state machine
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-ATTACHMENT
traces:
  verifies:
  - SL-05
  - AGG-ATTACHMENT
  - REQ-INF-003
  - REQ-INF-004
  - REQ-GOV-008
---

# Acceptance — Attachment

مولّدة من مصفوفة AGG-ATTACHMENT: 2 انتقالاً مسموحاً، 16 رفضاً.

```gherkin
Feature: Attachment lifecycle (AGG-ATTACHMENT)

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
      | Attachment | PENDING | CMD-ATT-COMPLETE-UPLOAD | SCANNING | EVT-ATT-UPLOADED | 3 |
      | Attachment | STORED | CMD-ATT-ERASE | ERASED | EVT-ATT-ERASED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Attachment | CMD-ATT-INITIATE-UPLOAD | PENDING | EVT-ATT-UPLOAD-INITIATED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Attachment | PENDING | CMD-ATT-INITIATE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | PENDING | CMD-ATT-ERASE | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | SCANNING | CMD-ATT-INITIATE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | SCANNING | CMD-ATT-COMPLETE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | SCANNING | CMD-ATT-ERASE | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | STORED | CMD-ATT-INITIATE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | STORED | CMD-ATT-COMPLETE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | QUARANTINED | CMD-ATT-INITIATE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | QUARANTINED | CMD-ATT-COMPLETE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | QUARANTINED | CMD-ATT-ERASE | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | EXPIRED | CMD-ATT-INITIATE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | EXPIRED | CMD-ATT-COMPLETE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | EXPIRED | CMD-ATT-ERASE | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | ERASED | CMD-ATT-INITIATE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | ERASED | CMD-ATT-COMPLETE-UPLOAD | ATTACHMENT_INVALID_STATE_TRANSITION |
      | Attachment | ERASED | CMD-ATT-ERASE | ATTACHMENT_INVALID_STATE_TRANSITION |
```
