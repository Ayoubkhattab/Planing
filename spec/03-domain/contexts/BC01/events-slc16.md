---
id: EVT-CAT-BC01-SLC16
type: event-catalog
title: Domain Events — BC01 (SLC-16)
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC01 (SLC-16)

_5 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-HRS-PROPOSED | AGG-HR-SYNC-PROPOSAL | SYS:HRIS change received | — | Role assignments / users (BC01); Security Officer notification (leave) | tenant_id + aggregate.id |
| EVT-HRS-APPROVED | AGG-HR-SYNC-PROPOSAL | CMD-HRS-APPROVE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Role assignments / users (BC01); Security Officer notification (leave) | tenant_id + aggregate.id |
| EVT-HRS-REJECTED | AGG-HR-SYNC-PROPOSAL | CMD-HRS-REJECT | — | Role assignments / users (BC01); Security Officer notification (leave) | tenant_id + aggregate.id |
| EVT-HRS-SUPERSEDED | AGG-HR-SYNC-PROPOSAL | SYS:newer HR change for the same person | — | Role assignments / users (BC01); Security Officer notification (leave) | tenant_id + aggregate.id |
| EVT-HRS-EXPIRED | AGG-HR-SYNC-PROPOSAL | SYS:14 days without decision | — | Role assignments / users (BC01); Security Officer notification (leave) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
