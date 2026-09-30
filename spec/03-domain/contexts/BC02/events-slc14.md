---
id: EVT-CAT-BC02-SLC14
type: event-catalog
title: Domain Events — BC02 (SLC-14)
wave: W4
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC02 (SLC-14)

_16 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-CRQ-DRAFTED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-DRAFT | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) | tenant_id + aggregate.id |
| EVT-CRQ-EDITED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-EDIT | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) | tenant_id + aggregate.id |
| EVT-CRQ-SUBMITTED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-SUBMIT | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) | tenant_id + aggregate.id |
| EVT-CRQ-APPROVED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-APPROVE | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) | tenant_id + aggregate.id |
| EVT-CRQ-REJECTED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-REJECT | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) | tenant_id + aggregate.id |
| EVT-CRQ-AMENDED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-AMEND | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) | tenant_id + aggregate.id |
| EVT-CRQ-FULFILMENT-UPDATED | AGG-COLLECTION-REQUIREMENT | SYS:validated observation matched | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) | tenant_id + aggregate.id |
| EVT-CRQ-SATISFIED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-MARK-SATISFIED | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) | tenant_id + aggregate.id |
| EVT-CRQ-EXPIRED | AGG-COLLECTION-REQUIREMENT | SYS:due passed | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) | tenant_id + aggregate.id |
| EVT-CRQ-CANCELLED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-CANCEL | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) | tenant_id + aggregate.id |
| EVT-CPL-CREATED | AGG-COLLECTION-PLAN | CMD-CPL-CREATE | — | Task creation (SLC-03); Notification (units) | tenant_id + aggregate.id |
| EVT-CPL-ACTIVITY-ADDED | AGG-COLLECTION-PLAN | CMD-CPL-ADD-ACTIVITY | — | Task creation (SLC-03); Notification (units) | tenant_id + aggregate.id |
| EVT-CPL-ACTIVITY-REMOVED | AGG-COLLECTION-PLAN | CMD-CPL-REMOVE-ACTIVITY | — | Task creation (SLC-03); Notification (units) | tenant_id + aggregate.id |
| EVT-CPL-ACTIVATED | AGG-COLLECTION-PLAN | CMD-CPL-ACTIVATE | — | Task creation (SLC-03); Notification (units) | tenant_id + aggregate.id |
| EVT-CPL-COMPLETED | AGG-COLLECTION-PLAN | SYS:all activity tasks terminal, CMD-CPL-COMPLETE | — | Task creation (SLC-03); Notification (units) | tenant_id + aggregate.id |
| EVT-CPL-CANCELLED | AGG-COLLECTION-PLAN | CMD-CPL-CANCEL | — | Task creation (SLC-03); Notification (units) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
