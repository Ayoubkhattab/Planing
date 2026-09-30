---
id: EVT-CAT-BC04-SLC06
type: event-catalog
title: Domain Events — BC04 (SLC-06)
wave: W4
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC04 (SLC-06)

_11 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-SUB-SUBSCRIBED | AGG-SUBSCRIPTION | CMD-SUB-SUBSCRIBE | — | Notification fan-out index | tenant_id + aggregate.id |
| EVT-SUB-CHANNELS-UPDATED | AGG-SUBSCRIPTION | CMD-SUB-UPDATE-CHANNELS | — | Notification fan-out index | tenant_id + aggregate.id |
| EVT-SUB-PAUSED | AGG-SUBSCRIPTION | CMD-SUB-PAUSE | — | Notification fan-out index | tenant_id + aggregate.id |
| EVT-SUB-RESUMED | AGG-SUBSCRIPTION | CMD-SUB-RESUME | — | Notification fan-out index | tenant_id + aggregate.id |
| EVT-SUB-ENDED | AGG-SUBSCRIPTION | CMD-SUB-UNSUBSCRIBE, SYS:subscriber lost visibility of target | — | Notification fan-out index | tenant_id + aggregate.id |
| EVT-NTF-QUEUED | AGG-NOTIFICATION | SYS:notifiable event for recipient | — | Push gateway; In-app inbox | tenant_id + aggregate.id |
| EVT-NTF-SENT | AGG-NOTIFICATION | SYS:delivered to channel | — | Push gateway; In-app inbox | tenant_id + aggregate.id |
| EVT-NTF-WITHHELD | AGG-NOTIFICATION | SYS:recipient no longer authorized at delivery | — | Push gateway; In-app inbox | tenant_id + aggregate.id |
| EVT-NTF-FAILED | AGG-NOTIFICATION | SYS:delivery failed after retries | — | Push gateway; In-app inbox | tenant_id + aggregate.id |
| EVT-NTF-READ | AGG-NOTIFICATION | CMD-NTF-MARK-READ | — | Push gateway; In-app inbox | tenant_id + aggregate.id |
| EVT-NTF-EXPIRED | AGG-NOTIFICATION | SYS:TTL (30 d) elapsed | — | Push gateway; In-app inbox | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
