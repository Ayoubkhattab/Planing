---
id: EVT-CAT-BC07-SLC02
type: event-catalog
title: Domain Events — BC07 (SLC-02)
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC07 (SLC-02)

_6 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-ADP-REGISTERED | AGG-ADAPTER | CMD-ADP-REGISTER | — | Import worker | tenant_id + aggregate.id |
| EVT-ADP-MAPPING-UPDATED | AGG-ADAPTER | CMD-ADP-UPDATE-MAPPING | — | Import worker | tenant_id + aggregate.id |
| EVT-ADP-ACTIVATED | AGG-ADAPTER | CMD-ADP-ACTIVATE | — | Import worker | tenant_id + aggregate.id |
| EVT-ADP-SUSPENDED | AGG-ADAPTER | CMD-ADP-SUSPEND | — | Import worker | tenant_id + aggregate.id |
| EVT-ADP-RESUMED | AGG-ADAPTER | CMD-ADP-RESUME | — | Import worker | tenant_id + aggregate.id |
| EVT-ADP-RETIRED | AGG-ADAPTER | CMD-ADP-RETIRE | — | Import worker | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
