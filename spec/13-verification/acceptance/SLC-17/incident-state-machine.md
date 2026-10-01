---
id: TST-INCIDENT-SM
type: acceptance-spec
title: Acceptance — Incident state machine
wave: W6
slice: SLC-17
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
generated_from: AGG-INCIDENT
traces:
  verifies:
  - SL-05
  - AGG-INCIDENT
  - REQ-RCM-006
  - REQ-RCM-007
  - REQ-RCM-008
  - REQ-RCM-009
  - REQ-RCM-010
  - REQ-RCM-011
  - REQ-RCM-012
  - REQ-RCM-013
---

# Acceptance — Incident

مولّدة من مصفوفة AGG-INCIDENT: 21 انتقالاً مسموحاً، 49 رفضاً، 2 انتقالاً نظامياً (SYS).

```gherkin
Feature: Incident lifecycle (AGG-INCIDENT)

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
      | Incident | REPORTED | CMD-INC-ASSESS | ASSESSED | EVT-INC-ASSESSED | 3 |
      | Incident | REPORTED | CMD-INC-CANCEL | CANCELLED | EVT-INC-CANCELLED | 3 |
      | Incident | REPORTED | CMD-INC-ESCALATE | REPORTED | EVT-INC-ESCALATED | 3 |
      | Incident | REPORTED | CMD-INC-DE-ESCALATE | REPORTED | EVT-INC-DE-ESCALATED | 3 |
      | Incident | REPORTED | CMD-INC-ACTIVATE-CONTINGENCY | REPORTED | EVT-INC-CONTINGENCY-ACTIVATED | 3 |
      | Incident | ASSESSED | CMD-INC-DISPATCH-RESPONSE | RESPONDING | EVT-INC-RESPONSE-DISPATCHED | 3 |
      | Incident | ASSESSED | CMD-INC-ESCALATE | ASSESSED | EVT-INC-ESCALATED | 3 |
      | Incident | ASSESSED | CMD-INC-DE-ESCALATE | ASSESSED | EVT-INC-DE-ESCALATED | 3 |
      | Incident | ASSESSED | CMD-INC-ACTIVATE-CONTINGENCY | ASSESSED | EVT-INC-CONTINGENCY-ACTIVATED | 3 |
      | Incident | RESPONDING | CMD-INC-CONTAIN | CONTAINED | EVT-INC-CONTAINED | 3 |
      | Incident | RESPONDING | CMD-INC-ESCALATE | RESPONDING | EVT-INC-ESCALATED | 3 |
      | Incident | RESPONDING | CMD-INC-DE-ESCALATE | RESPONDING | EVT-INC-DE-ESCALATED | 3 |
      | Incident | RESPONDING | CMD-INC-ACTIVATE-CONTINGENCY | RESPONDING | EVT-INC-CONTINGENCY-ACTIVATED | 3 |
      | Incident | CONTAINED | CMD-INC-RESOLVE | RESOLVED | EVT-INC-RESOLVED | 3 |
      | Incident | CONTAINED | CMD-INC-ESCALATE | CONTAINED | EVT-INC-ESCALATED | 3 |
      | Incident | CONTAINED | CMD-INC-DE-ESCALATE | CONTAINED | EVT-INC-DE-ESCALATED | 3 |
      | Incident | CONTAINED | CMD-INC-ACTIVATE-CONTINGENCY | CONTAINED | EVT-INC-CONTINGENCY-ACTIVATED | 3 |
      | Incident | RESOLVED | CMD-INC-CLOSE | CLOSED | EVT-INC-CLOSED | 3 |
      | Incident | RESOLVED | CMD-INC-ESCALATE | RESOLVED | EVT-INC-ESCALATED | 3 |
      | Incident | RESOLVED | CMD-INC-DE-ESCALATE | RESOLVED | EVT-INC-DE-ESCALATED | 3 |
      | Incident | RESOLVED | CMD-INC-ACTIVATE-CONTINGENCY | RESOLVED | EVT-INC-CONTINGENCY-ACTIVATED | 3 |

  Scenario Outline: creation
    When the actor sends <command> with a valid payload
    Then a new <aggregate> exists in state <to> at version 1
    And exactly one <event> is written to the outbox

    Examples:
      | aggregate | command | to | event |
      | Incident | CMD-INC-REPORT | REPORTED | EVT-INC-REPORTED |

  Scenario Outline: rejected transition
    Given a <aggregate> in state <state>
    When the actor sends <command>
    Then the command is rejected with <error> and HTTP 409
    And the state and version are unchanged
    And no event is written

    Examples:
      | aggregate | state | command | error |
      | Incident | REPORTED | CMD-INC-REPORT | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | REPORTED | CMD-INC-DISPATCH-RESPONSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | REPORTED | CMD-INC-CONTAIN | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | REPORTED | CMD-INC-RESOLVE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | REPORTED | CMD-INC-CLOSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | ASSESSED | CMD-INC-REPORT | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | ASSESSED | CMD-INC-ASSESS | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | ASSESSED | CMD-INC-CONTAIN | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | ASSESSED | CMD-INC-RESOLVE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | ASSESSED | CMD-INC-CLOSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | ASSESSED | CMD-INC-CANCEL | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESPONDING | CMD-INC-REPORT | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESPONDING | CMD-INC-ASSESS | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESPONDING | CMD-INC-DISPATCH-RESPONSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESPONDING | CMD-INC-RESOLVE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESPONDING | CMD-INC-CLOSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESPONDING | CMD-INC-CANCEL | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CONTAINED | CMD-INC-REPORT | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CONTAINED | CMD-INC-ASSESS | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CONTAINED | CMD-INC-DISPATCH-RESPONSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CONTAINED | CMD-INC-CONTAIN | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CONTAINED | CMD-INC-CLOSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CONTAINED | CMD-INC-CANCEL | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESOLVED | CMD-INC-REPORT | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESOLVED | CMD-INC-ASSESS | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESOLVED | CMD-INC-DISPATCH-RESPONSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESOLVED | CMD-INC-CONTAIN | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESOLVED | CMD-INC-RESOLVE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | RESOLVED | CMD-INC-CANCEL | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CLOSED | CMD-INC-REPORT | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CLOSED | CMD-INC-ASSESS | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CLOSED | CMD-INC-DISPATCH-RESPONSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CLOSED | CMD-INC-CONTAIN | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CLOSED | CMD-INC-RESOLVE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CLOSED | CMD-INC-CLOSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CLOSED | CMD-INC-CANCEL | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CLOSED | CMD-INC-ESCALATE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CLOSED | CMD-INC-DE-ESCALATE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CLOSED | CMD-INC-ACTIVATE-CONTINGENCY | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CANCELLED | CMD-INC-REPORT | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CANCELLED | CMD-INC-ASSESS | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CANCELLED | CMD-INC-DISPATCH-RESPONSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CANCELLED | CMD-INC-CONTAIN | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CANCELLED | CMD-INC-RESOLVE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CANCELLED | CMD-INC-CLOSE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CANCELLED | CMD-INC-CANCEL | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CANCELLED | CMD-INC-ESCALATE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CANCELLED | CMD-INC-DE-ESCALATE | INCIDENT_INVALID_STATE_TRANSITION |
      | Incident | CANCELLED | CMD-INC-ACTIVATE-CONTINGENCY | INCIDENT_INVALID_STATE_TRANSITION |

  Scenario Outline: system-triggered transition
    Given a <aggregate> in state <from>
    When the system trigger <trigger> occurs under a workload identity
    Then the state becomes <to>
    And exactly one <event> is written to the outbox
    And the aggregate invariants hold exactly as for actor commands

    Examples:
      | aggregate | from | trigger | to | event |
      | Incident | REPORTED | response SLA elapsed without dispatch | REPORTED | EVT-INC-SLA-BREACHED |
      | Incident | ASSESSED | response SLA elapsed without dispatch | ASSESSED | EVT-INC-SLA-BREACHED |
```
