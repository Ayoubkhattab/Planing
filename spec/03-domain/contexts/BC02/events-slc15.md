---
id: EVT-CAT-BC02-SLC15
type: event-catalog
title: Domain Events — BC02 (SLC-15)
wave: W4
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC02 (SLC-15)

_9 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-CRP-PROPOSED | AGG-CORRELATION-PROPOSAL | SYS:correlation rule score ≥ threshold, CMD-CRP-PROPOSE | — | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback | tenant_id + aggregate.id |
| EVT-CRP-REVIEW-STARTED | AGG-CORRELATION-PROPOSAL | CMD-CRP-START-REVIEW | — | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback | tenant_id + aggregate.id |
| EVT-CRP-ACCEPTED | AGG-CORRELATION-PROPOSAL | CMD-CRP-ACCEPT | — | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback | tenant_id + aggregate.id |
| EVT-CRP-REJECTED | AGG-CORRELATION-PROPOSAL | CMD-CRP-REJECT | — | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback | tenant_id + aggregate.id |
| EVT-CRP-EXPIRED | AGG-CORRELATION-PROPOSAL | SYS:not reviewed within 30 days | — | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback | tenant_id + aggregate.id |
| EVT-CRR-DEFINED | AGG-CORRELATION-RULE | CMD-CRR-DEFINE | — | Correlation engine | tenant_id + aggregate.id |
| EVT-CRR-EDITED | AGG-CORRELATION-RULE | CMD-CRR-EDIT | — | Correlation engine | tenant_id + aggregate.id |
| EVT-CRR-ACTIVATED | AGG-CORRELATION-RULE | CMD-CRR-ACTIVATE | — | Correlation engine | tenant_id + aggregate.id |
| EVT-CRR-RETIRED | AGG-CORRELATION-RULE | CMD-CRR-RETIRE | — | Correlation engine | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
