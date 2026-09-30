---
id: EVT-CAT-BC01-SLC11
type: event-catalog
title: Domain Events — BC01 (SLC-11)
wave: W4
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC01 (SLC-11)

_8 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-DEV-ENROLL-REQUESTED | AGG-DEVICE | CMD-DEV-ENROLL | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service | tenant_id + aggregate.id |
| EVT-DEV-ACTIVATED | AGG-DEVICE | CMD-DEV-CONFIRM | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service | tenant_id + aggregate.id |
| EVT-DEV-KEY-ROTATED | AGG-DEVICE | CMD-DEV-ROTATE-KEY | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service | tenant_id + aggregate.id |
| EVT-DEV-SUSPENDED | AGG-DEVICE | CMD-DEV-SUSPEND | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service | tenant_id + aggregate.id |
| EVT-DEV-REINSTATED | AGG-DEVICE | CMD-DEV-REINSTATE | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service | tenant_id + aggregate.id |
| EVT-DEV-REPORTED-LOST | AGG-DEVICE | CMD-DEV-REPORT-LOST | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service | tenant_id + aggregate.id |
| EVT-DEV-WIPED | AGG-DEVICE | SYS:wipe confirmed by device | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service | tenant_id + aggregate.id |
| EVT-DEV-RETIRED | AGG-DEVICE | CMD-DEV-RETIRE | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
