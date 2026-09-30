---
id: EVT-CAT-BC03-SLC06
type: event-catalog
title: Domain Events — BC03 (SLC-06)
wave: W4
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC03 (SLC-06)

_19 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-SIT-CREATED | AGG-SITUATION | CMD-SIT-CREATE | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIT-DEFINITION-CHANGED | AGG-SITUATION | CMD-SIT-EDIT-DEFINITION | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIT-ACTIVATED | AGG-SITUATION | CMD-SIT-ACTIVATE | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIT-PAUSED | AGG-SITUATION | CMD-SIT-PAUSE | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIT-RESUMED | AGG-SITUATION | CMD-SIT-RESUME | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIT-CLOSED | AGG-SITUATION | CMD-SIT-CLOSE | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIT-RECLASSIFIED | AGG-SITUATION | CMD-SIT-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ARL-DEFINED | AGG-ALERT-RULE | CMD-ARL-DEFINE | — | Alert evaluator (reload rules) | tenant_id + aggregate.id |
| EVT-ARL-EDITED | AGG-ALERT-RULE | CMD-ARL-EDIT | — | Alert evaluator (reload rules) | tenant_id + aggregate.id |
| EVT-ARL-ACTIVATED | AGG-ALERT-RULE | CMD-ARL-ACTIVATE | — | Alert evaluator (reload rules) | tenant_id + aggregate.id |
| EVT-ARL-DISABLED | AGG-ALERT-RULE | CMD-ARL-DISABLE | — | Alert evaluator (reload rules) | tenant_id + aggregate.id |
| EVT-ARL-ENABLED | AGG-ALERT-RULE | CMD-ARL-ENABLE | — | Alert evaluator (reload rules) | tenant_id + aggregate.id |
| EVT-ARL-RETIRED | AGG-ALERT-RULE | CMD-ARL-RETIRE | — | Alert evaluator (reload rules) | tenant_id + aggregate.id |
| EVT-ALR-RAISED | AGG-ALERT | SYS:rule condition met | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler | tenant_id + aggregate.id |
| EVT-ALR-REPEATED | AGG-ALERT | SYS:condition met again within dedupe window | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler | tenant_id + aggregate.id |
| EVT-ALR-ACKNOWLEDGED | AGG-ALERT | CMD-ALR-ACKNOWLEDGE | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler | tenant_id + aggregate.id |
| EVT-ALR-ESCALATED | AGG-ALERT | SYS:unacknowledged beyond escalation delay | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler | tenant_id + aggregate.id |
| EVT-ALR-RESOLVED | AGG-ALERT | CMD-ALR-RESOLVE, SYS:condition cleared and rule auto_resolve | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler | tenant_id + aggregate.id |
| EVT-ALR-DISMISSED | AGG-ALERT | CMD-ALR-DISMISS | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
