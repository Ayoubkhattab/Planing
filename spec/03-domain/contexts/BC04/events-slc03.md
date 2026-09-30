---
id: EVT-CAT-BC04-SLC03
type: event-catalog
title: Domain Events — BC04 (SLC-03)
wave: W4
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC04 (SLC-03)

_30 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-TASK-CREATED | AGG-TASK | CMD-TASK-CREATE | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-EDITED | AGG-TASK | CMD-TASK-EDIT | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-READIED | AGG-TASK | CMD-TASK-MARK-READY | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-ASSIGNED | AGG-TASK | CMD-TASK-ASSIGN | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-REASSIGNED | AGG-TASK | CMD-TASK-REASSIGN | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-ACCEPTED | AGG-TASK | CMD-TASK-ACCEPT | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-DECLINED | AGG-TASK | CMD-TASK-DECLINE | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-STARTED | AGG-TASK | CMD-TASK-START | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-BLOCKED | AGG-TASK | CMD-TASK-BLOCK | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-RESUMED | AGG-TASK | CMD-TASK-RESUME | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-RESULT-ITEM-ADDED | AGG-TASK | CMD-TASK-ADD-RESULT-ITEM | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-SUBMITTED | AGG-TASK | CMD-TASK-SUBMIT | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-REVIEW-STARTED | AGG-TASK | CMD-TASK-START-REVIEW | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-RETURNED-FOR-REWORK | AGG-TASK | CMD-TASK-RETURN | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-APPROVED | AGG-TASK | CMD-TASK-APPROVE | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-REJECTED | AGG-TASK | CMD-TASK-REJECT | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-COMPLETED | AGG-TASK | SYS:all completion criteria satisfied, CMD-TASK-COMPLETE | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-CLOSED | AGG-TASK | CMD-TASK-CLOSE, SYS:follow-up window (7 d) elapsed without open follow-ups | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-CANCELLED | AGG-TASK | CMD-TASK-CANCEL | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-EXPIRED | AGG-TASK | SYS:due passed and task type expires_on_due | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-SUPERSEDED | AGG-TASK | SYS:plan version baselined without this task | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-ESCALATED | AGG-TASK | CMD-TASK-ESCALATE, SYS:due passed (escalation policy) | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-DUE-CHANGED | AGG-TASK | CMD-TASK-SET-DUE | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-SUSPENDED | AGG-TASK | CMD-TASK-SUSPEND | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-UNSUSPENDED | AGG-TASK | CMD-TASK-UNSUSPEND | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TASK-RECLASSIFIED | AGG-TASK | CMD-TASK-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) | tenant_id + aggregate.id |
| EVT-TTY-DEFINED | AGG-TASK-TYPE | CMD-TTY-DEFINE | — | Task command handler cache | tenant_id + aggregate.id |
| EVT-TTY-EDITED | AGG-TASK-TYPE | CMD-TTY-EDIT | — | Task command handler cache | tenant_id + aggregate.id |
| EVT-TTY-ACTIVATED | AGG-TASK-TYPE | CMD-TTY-ACTIVATE | — | Task command handler cache | tenant_id + aggregate.id |
| EVT-TTY-RETIRED | AGG-TASK-TYPE | CMD-TTY-RETIRE | — | Task command handler cache | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
