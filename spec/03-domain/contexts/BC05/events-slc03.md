---
id: EVT-CAT-BC05-SLC03
type: event-catalog
title: Domain Events — BC05 (SLC-03)
wave: W4
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC05 (SLC-03)

_6 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-QUAL-RECORDED | AGG-QUALIFICATION-RECORD | CMD-QUAL-RECORD | — | Eligibility cache invalidation; Task assignment re-check report | tenant_id + aggregate.id |
| EVT-QUAL-RENEWED | AGG-QUALIFICATION-RECORD | CMD-QUAL-RENEW | — | Eligibility cache invalidation; Task assignment re-check report | tenant_id + aggregate.id |
| EVT-QUAL-SUSPENDED | AGG-QUALIFICATION-RECORD | CMD-QUAL-SUSPEND | — | Eligibility cache invalidation; Task assignment re-check report | tenant_id + aggregate.id |
| EVT-QUAL-REINSTATED | AGG-QUALIFICATION-RECORD | CMD-QUAL-REINSTATE | — | Eligibility cache invalidation; Task assignment re-check report | tenant_id + aggregate.id |
| EVT-QUAL-REVOKED | AGG-QUALIFICATION-RECORD | CMD-QUAL-REVOKE | — | Eligibility cache invalidation; Task assignment re-check report | tenant_id + aggregate.id |
| EVT-QUAL-EXPIRED | AGG-QUALIFICATION-RECORD | SYS:valid_to reached | — | Eligibility cache invalidation; Task assignment re-check report | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
