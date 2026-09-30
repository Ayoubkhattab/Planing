---
id: EVT-CAT-BC04-SLC08
type: event-catalog
title: Domain Events — BC04 (SLC-08)
wave: W4
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC04 (SLC-08)

_33 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-DRQ-CREATED | AGG-DECISION-REQUEST | CMD-DRQ-CREATE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-DRQ-OPTION-ADDED | AGG-DECISION-REQUEST | CMD-DRQ-ADD-OPTION | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-DRQ-CITED | AGG-DECISION-REQUEST | CMD-DRQ-CITE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-DRQ-OPENED | AGG-DECISION-REQUEST | CMD-DRQ-OPEN | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-DRQ-ESCALATED | AGG-DECISION-REQUEST | SYS:deadline passed | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-DRQ-DECIDED | AGG-DECISION-REQUEST | SYS:decision recorded for this request | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-DRQ-WITHDRAWN | AGG-DECISION-REQUEST | CMD-DRQ-WITHDRAW | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-DEC-RECORDED | AGG-DECISION | CMD-DEC-RECORD | — | Decision request (DECIDED); Plans implementing it (review flag on supersede/annul); Search projection (SLC-05); Audit reports | tenant_id + aggregate.id |
| EVT-DEC-SUPERSEDED | AGG-DECISION | SYS:superseding decision recorded | — | Decision request (DECIDED); Plans implementing it (review flag on supersede/annul); Search projection (SLC-05); Audit reports | tenant_id + aggregate.id |
| EVT-DEC-ANNULLED | AGG-DECISION | CMD-DEC-ANNUL | — | Decision request (DECIDED); Plans implementing it (review flag on supersede/annul); Search projection (SLC-05); Audit reports | tenant_id + aggregate.id |
| EVT-PLN-CREATED | AGG-PLAN | CMD-PLN-CREATE | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) | tenant_id + aggregate.id |
| EVT-PLN-ACTIVATED | AGG-PLAN | SYS:first version baselined | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) | tenant_id + aggregate.id |
| EVT-PLN-SUSPENDED | AGG-PLAN | CMD-PLN-SUSPEND | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) | tenant_id + aggregate.id |
| EVT-PLN-RESUMED | AGG-PLAN | CMD-PLN-RESUME | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) | tenant_id + aggregate.id |
| EVT-PLN-COMPLETED | AGG-PLAN | CMD-PLN-COMPLETE | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) | tenant_id + aggregate.id |
| EVT-PLN-CLOSED | AGG-PLAN | CMD-PLN-CLOSE | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) | tenant_id + aggregate.id |
| EVT-PLN-CANCELLED | AGG-PLAN | CMD-PLN-CANCEL | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) | tenant_id + aggregate.id |
| EVT-PLN-RECLASSIFIED | AGG-PLAN | CMD-PLN-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) | tenant_id + aggregate.id |
| EVT-PLN-REVIEW-FLAGGED | AGG-PLAN | SYS:implemented decision annulled or superseded | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) | tenant_id + aggregate.id |
| EVT-PLV-DRAFTED | AGG-PLAN-VERSION | CMD-PLV-DRAFT | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-PLV-EDITED | AGG-PLAN-VERSION | CMD-PLV-EDIT | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-PLV-SUBMITTED | AGG-PLAN-VERSION | CMD-PLV-SUBMIT | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-PLV-RETURNED | AGG-PLAN-VERSION | CMD-PLV-RETURN | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-PLV-BASELINED | AGG-PLAN-VERSION | CMD-PLV-APPROVE | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-PLV-REJECTED | AGG-PLAN-VERSION | CMD-PLV-REJECT | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-PLV-MINOR-AMENDED | AGG-PLAN-VERSION | CMD-PLV-AMEND-MINOR | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-PLV-SUPERSEDED | AGG-PLAN-VERSION | SYS:newer version baselined | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-PLV-DISCARDED | AGG-PLAN-VERSION | CMD-PLV-DISCARD | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-OUT-TRACKER-CREATED | AGG-OUTCOME-TRACKER | SYS:outcome baselined | — | Plan progress view; Business telemetry (OUT-05) | tenant_id + aggregate.id |
| EVT-OUT-TARGET-CHANGED | AGG-OUTCOME-TRACKER | SYS:target changed by new baseline | — | Plan progress view; Business telemetry (OUT-05) | tenant_id + aggregate.id |
| EVT-OUT-MEASURED | AGG-OUTCOME-TRACKER | CMD-OUT-RECORD | — | Plan progress view; Business telemetry (OUT-05) | tenant_id + aggregate.id |
| EVT-OUT-MEASUREMENT-CORRECTED | AGG-OUTCOME-TRACKER | CMD-OUT-CORRECT | — | Plan progress view; Business telemetry (OUT-05) | tenant_id + aggregate.id |
| EVT-OUT-TRACKER-CLOSED | AGG-OUTCOME-TRACKER | SYS:plan closed or cancelled | — | Plan progress view; Business telemetry (OUT-05) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
