---
id: EVT-CAT-BC05-SLC09
type: event-catalog
title: Domain Events — BC05 (SLC-09)
wave: W4
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC05 (SLC-09)

_40 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-AST-REGISTERED | AGG-ASSET | CMD-AST-REGISTER | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-AST-CONDITION-UPDATED | AGG-ASSET | CMD-AST-UPDATE-CONDITION | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-AST-UNSERVICEABLE | AGG-ASSET | CMD-AST-MARK-UNSERVICEABLE, CMD-AST-FAIL-MAINTENANCE | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-AST-MAINTENANCE-STARTED | AGG-ASSET | CMD-AST-START-MAINTENANCE | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-AST-RETURNED-TO-SERVICE | AGG-ASSET | CMD-AST-RETURN-TO-SERVICE | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-AST-CUSTODY-TRANSFERRED | AGG-ASSET | CMD-AST-TRANSFER-CUSTODY | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-AST-CERTIFICATION-SET | AGG-ASSET | CMD-AST-SET-CERTIFICATION | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-AST-REPORTED-LOST | AGG-ASSET | CMD-AST-REPORT-LOST | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-AST-RECOVERED | AGG-ASSET | CMD-AST-RECOVER | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-AST-DISPOSED | AGG-ASSET | CMD-AST-DISPOSE | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-AST-RECLASSIFIED | AGG-ASSET | CMD-AST-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) | tenant_id + aggregate.id |
| EVT-MNT-PLANNED | AGG-MAINTENANCE-ORDER | CMD-MNT-PLAN | — | Asset (start/return via policy); Availability view | tenant_id + aggregate.id |
| EVT-MNT-RESCHEDULED | AGG-MAINTENANCE-ORDER | CMD-MNT-RESCHEDULE | — | Asset (start/return via policy); Availability view | tenant_id + aggregate.id |
| EVT-MNT-STARTED | AGG-MAINTENANCE-ORDER | CMD-MNT-START | — | Asset (start/return via policy); Availability view | tenant_id + aggregate.id |
| EVT-MNT-COMPLETED | AGG-MAINTENANCE-ORDER | CMD-MNT-COMPLETE | — | Asset (start/return via policy); Availability view | tenant_id + aggregate.id |
| EVT-MNT-CANCELLED | AGG-MAINTENANCE-ORDER | CMD-MNT-CANCEL | — | Asset (start/return via policy); Availability view | tenant_id + aggregate.id |
| EVT-RSV-HELD | AGG-ASSET-RESERVATION | CMD-RSV-HOLD | — | Availability view | tenant_id + aggregate.id |
| EVT-RSV-CONFIRMED | AGG-ASSET-RESERVATION | CMD-RSV-CONFIRM | — | Availability view | tenant_id + aggregate.id |
| EVT-RSV-EXPIRED | AGG-ASSET-RESERVATION | SYS:hold expiry (24 h) reached | — | Availability view | tenant_id + aggregate.id |
| EVT-RSV-RELEASED | AGG-ASSET-RESERVATION | CMD-RSV-RELEASE, SYS:linked task or plan terminal | — | Availability view | tenant_id + aggregate.id |
| EVT-RSV-CANCELLED | AGG-ASSET-RESERVATION | CMD-RSV-CANCEL | — | Availability view | tenant_id + aggregate.id |
| EVT-ASG-ASSIGNED | AGG-ASSET-ASSIGNMENT | CMD-ASG-ASSIGN | — | Availability view; Task (SLC-03) | tenant_id + aggregate.id |
| EVT-ASG-RETURNED | AGG-ASSET-ASSIGNMENT | CMD-ASG-RETURN, SYS:linked task terminal | — | Availability view; Task (SLC-03) | tenant_id + aggregate.id |
| EVT-ASG-CANCELLED | AGG-ASSET-ASSIGNMENT | CMD-ASG-CANCEL | — | Availability view; Task (SLC-03) | tenant_id + aggregate.id |
| EVT-RPL-CREATED | AGG-RESOURCE-POOL | CMD-RPL-CREATE | — | Capacity ledger | tenant_id + aggregate.id |
| EVT-RPL-CAPACITY-ADJUSTED | AGG-RESOURCE-POOL | CMD-RPL-ADJUST-CAPACITY | — | Capacity ledger | tenant_id + aggregate.id |
| EVT-RPL-SUSPENDED | AGG-RESOURCE-POOL | CMD-RPL-SUSPEND | — | Capacity ledger | tenant_id + aggregate.id |
| EVT-RPL-RESUMED | AGG-RESOURCE-POOL | CMD-RPL-RESUME | — | Capacity ledger | tenant_id + aggregate.id |
| EVT-RPL-CLOSED | AGG-RESOURCE-POOL | CMD-RPL-CLOSE | — | Capacity ledger | tenant_id + aggregate.id |
| EVT-ALC-REQUESTED | AGG-ALLOCATION | CMD-ALC-REQUEST | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) | tenant_id + aggregate.id |
| EVT-ALC-COMMITTED | AGG-ALLOCATION | SYS:all checks passed, CMD-ALC-APPROVE | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) | tenant_id + aggregate.id |
| EVT-ALC-APPROVAL-REQUIRED | AGG-ALLOCATION | SYS:checks passed, policy requires approval | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) | tenant_id + aggregate.id |
| EVT-ALC-REJECTED | AGG-ALLOCATION | SYS:a check failed, CMD-ALC-REJECT, SYS:provisional hold (1 h) elapsed | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) | tenant_id + aggregate.id |
| EVT-ALC-CONSUMED | AGG-ALLOCATION | CMD-ALC-RECORD-CONSUMPTION | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) | tenant_id + aggregate.id |
| EVT-ALC-PREEMPTED | AGG-ALLOCATION | CMD-ALC-PREEMPT | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) | tenant_id + aggregate.id |
| EVT-ALC-RELEASED | AGG-ALLOCATION | CMD-ALC-RELEASE, SYS:linked task terminal | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) | tenant_id + aggregate.id |
| EVT-RRQ-DEFINED | AGG-ROLE-REQUIREMENT | CMD-RRQ-DEFINE | — | Readiness evaluator; Eligibility cache | tenant_id + aggregate.id |
| EVT-RRQ-EDITED | AGG-ROLE-REQUIREMENT | CMD-RRQ-EDIT | — | Readiness evaluator; Eligibility cache | tenant_id + aggregate.id |
| EVT-RRQ-ACTIVATED | AGG-ROLE-REQUIREMENT | CMD-RRQ-ACTIVATE | — | Readiness evaluator; Eligibility cache | tenant_id + aggregate.id |
| EVT-RRQ-RETIRED | AGG-ROLE-REQUIREMENT | CMD-RRQ-RETIRE | — | Readiness evaluator; Eligibility cache | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
