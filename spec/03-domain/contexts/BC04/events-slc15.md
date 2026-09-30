---
id: EVT-CAT-BC04-SLC15
type: event-catalog
title: Domain Events — BC04 (SLC-15)
wave: W4
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC04 (SLC-15)

_10 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-CRD-OPENED | AGG-COORDINATION-CASE | CMD-CRD-OPEN | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-CRD-PARTICIPANT-ADDED | AGG-COORDINATION-CASE | CMD-CRD-ADD-PARTICIPANT | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-CRD-PARTICIPANT-REMOVED | AGG-COORDINATION-CASE | CMD-CRD-REMOVE-PARTICIPANT | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-CRD-ACTIVATED | AGG-COORDINATION-CASE | CMD-CRD-ACTIVATE | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-CRD-RESPONSIBILITY-ASSIGNED | AGG-COORDINATION-CASE | CMD-CRD-ASSIGN-RESPONSIBILITY | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-CRD-RESPONSIBILITY-UPDATED | AGG-COORDINATION-CASE | CMD-CRD-UPDATE-RESPONSIBILITY | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-CRD-DECISION-REQUESTED | AGG-COORDINATION-CASE | CMD-CRD-REQUEST-DECISION | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-CRD-DECISION-RECORDED | AGG-COORDINATION-CASE | SYS:linked decision recorded | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-CRD-CLOSED | AGG-COORDINATION-CASE | CMD-CRD-CLOSE | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-CRD-CANCELLED | AGG-COORDINATION-CASE | CMD-CRD-CANCEL | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
