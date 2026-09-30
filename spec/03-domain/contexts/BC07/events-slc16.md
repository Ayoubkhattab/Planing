---
id: EVT-CAT-BC07-SLC16
type: event-catalog
title: Domain Events — BC07 (SLC-16)
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC07 (SLC-16)

_15 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-CON-REGISTERED | AGG-INTEGRATION-CONNECTION | CMD-CON-REGISTER | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting | tenant_id + aggregate.id |
| EVT-CON-TEST-STARTED | AGG-INTEGRATION-CONNECTION | CMD-CON-TEST | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting | tenant_id + aggregate.id |
| EVT-CON-ACTIVATED | AGG-INTEGRATION-CONNECTION | CMD-CON-ACTIVATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting | tenant_id + aggregate.id |
| EVT-CON-TEST-FAILED | AGG-INTEGRATION-CONNECTION | CMD-CON-FAIL-TEST | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting | tenant_id + aggregate.id |
| EVT-CON-DEGRADED | AGG-INTEGRATION-CONNECTION | SYS:health checks failing 5 min | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting | tenant_id + aggregate.id |
| EVT-CON-RECOVERED | AGG-INTEGRATION-CONNECTION | SYS:health restored | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting | tenant_id + aggregate.id |
| EVT-CON-SUSPENDED | AGG-INTEGRATION-CONNECTION | CMD-CON-SUSPEND | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting | tenant_id + aggregate.id |
| EVT-CON-RESUMED | AGG-INTEGRATION-CONNECTION | CMD-CON-RESUME | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting | tenant_id + aggregate.id |
| EVT-CON-RETIRED | AGG-INTEGRATION-CONNECTION | CMD-CON-RETIRE | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting | tenant_id + aggregate.id |
| EVT-SNS-REGISTERED | AGG-SENSOR-STREAM | CMD-SNS-REGISTER | — | Ingestion workers (SLC-02 batches); Operations alerting | tenant_id + aggregate.id |
| EVT-SNS-QUALITY-RULES-SET | AGG-SENSOR-STREAM | CMD-SNS-SET-QUALITY-RULES | — | Ingestion workers (SLC-02 batches); Operations alerting | tenant_id + aggregate.id |
| EVT-SNS-ACTIVATED | AGG-SENSOR-STREAM | CMD-SNS-ACTIVATE | — | Ingestion workers (SLC-02 batches); Operations alerting | tenant_id + aggregate.id |
| EVT-SNS-PAUSED | AGG-SENSOR-STREAM | CMD-SNS-PAUSE | — | Ingestion workers (SLC-02 batches); Operations alerting | tenant_id + aggregate.id |
| EVT-SNS-STALE | AGG-SENSOR-STREAM | SYS:no data beyond stale-after | — | Ingestion workers (SLC-02 batches); Operations alerting | tenant_id + aggregate.id |
| EVT-SNS-RETIRED | AGG-SENSOR-STREAM | CMD-SNS-RETIRE | — | Ingestion workers (SLC-02 batches); Operations alerting | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
