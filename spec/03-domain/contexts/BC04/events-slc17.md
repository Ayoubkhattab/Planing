---
id: EVT-CAT-BC04-SLC17
type: event-catalog
title: Domain Events — BC04 (SLC-17)
wave: W4
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC04 (SLC-17)

_17 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-RIS-IDENTIFIED | AGG-RISK | CMD-RIS-IDENTIFY | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) | tenant_id + aggregate.id |
| EVT-RIS-ASSESSED | AGG-RISK | CMD-RIS-ASSESS | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) | tenant_id + aggregate.id |
| EVT-RIS-TREATMENT-PLANNED | AGG-RISK | CMD-RIS-PLAN-TREATMENT | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) | tenant_id + aggregate.id |
| EVT-RIS-REASSESSED | AGG-RISK | CMD-RIS-REASSESS | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) | tenant_id + aggregate.id |
| EVT-RIS-CLOSED | AGG-RISK | CMD-RIS-CLOSE | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) | tenant_id + aggregate.id |
| EVT-RIS-MATERIALIZATION-LINKED | AGG-RISK | SYS:incident references this risk as risk_ref | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) | tenant_id + aggregate.id |
| EVT-INC-REPORTED | AGG-INCIDENT | CMD-INC-REPORT | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |
| EVT-INC-ASSESSED | AGG-INCIDENT | CMD-INC-ASSESS | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |
| EVT-INC-RESPONSE-DISPATCHED | AGG-INCIDENT | CMD-INC-DISPATCH-RESPONSE | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |
| EVT-INC-CONTAINED | AGG-INCIDENT | CMD-INC-CONTAIN | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |
| EVT-INC-RESOLVED | AGG-INCIDENT | CMD-INC-RESOLVE | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |
| EVT-INC-CLOSED | AGG-INCIDENT | CMD-INC-CLOSE | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |
| EVT-INC-CANCELLED | AGG-INCIDENT | CMD-INC-CANCEL | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |
| EVT-INC-ESCALATED | AGG-INCIDENT | CMD-INC-ESCALATE | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |
| EVT-INC-DE-ESCALATED | AGG-INCIDENT | CMD-INC-DE-ESCALATE | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |
| EVT-INC-CONTINGENCY-ACTIVATED | AGG-INCIDENT | CMD-INC-ACTIVATE-CONTINGENCY | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |
| EVT-INC-SLA-BREACHED | AGG-INCIDENT | SYS:response SLA elapsed without dispatch | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
