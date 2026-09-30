---
id: EVT-CAT-BC03-SLC16
type: event-catalog
title: Domain Events — BC03 (SLC-16)
wave: W4
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC03 (SLC-16)

_5 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-CAP-PREPARED | AGG-CAP-MESSAGE | CMD-CAP-PREPARE | — | CAP gateway; Audit | tenant_id + aggregate.id |
| EVT-CAP-SENT | AGG-CAP-MESSAGE | CMD-CAP-RELEASE | — | CAP gateway; Audit | tenant_id + aggregate.id |
| EVT-CAP-FAILED | AGG-CAP-MESSAGE | SYS:delivery failed after retries | — | CAP gateway; Audit | tenant_id + aggregate.id |
| EVT-CAP-RETRY | AGG-CAP-MESSAGE | CMD-CAP-RETRY | — | CAP gateway; Audit | tenant_id + aggregate.id |
| EVT-CAP-CANCELLED | AGG-CAP-MESSAGE | CMD-CAP-CANCEL | — | CAP gateway; Audit | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
