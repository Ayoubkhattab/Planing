---
id: EVT-CAT-BC07-SLC05
type: event-catalog
title: Domain Events — BC07 (SLC-05)
wave: W4
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC07 (SLC-05)

_7 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-PRJ-BUILD-STARTED | AGG-PROJECTION-VERSION | CMD-PRJ-CREATE-VERSION | — | Query router (alias switch); Operations alerting | tenant_id + aggregate.id |
| EVT-PRJ-READY | AGG-PROJECTION-VERSION | SYS:full rebuild reached live checkpoint | — | Query router (alias switch); Operations alerting | tenant_id + aggregate.id |
| EVT-PRJ-FAILED | AGG-PROJECTION-VERSION | SYS:build failed, CMD-PRJ-CANCEL-BUILD | — | Query router (alias switch); Operations alerting | tenant_id + aggregate.id |
| EVT-PRJ-PROMOTED | AGG-PROJECTION-VERSION | CMD-PRJ-PROMOTE | — | Query router (alias switch); Operations alerting | tenant_id + aggregate.id |
| EVT-PRJ-DEGRADED | AGG-PROJECTION-VERSION | SYS:lag above threshold | — | Query router (alias switch); Operations alerting | tenant_id + aggregate.id |
| EVT-PRJ-RECOVERED | AGG-PROJECTION-VERSION | SYS:lag back within target | — | Query router (alias switch); Operations alerting | tenant_id + aggregate.id |
| EVT-PRJ-RETIRED | AGG-PROJECTION-VERSION | CMD-PRJ-RETIRE | — | Query router (alias switch); Operations alerting | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
