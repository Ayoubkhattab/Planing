---
id: EVT-CAT-BC02-SLC04
type: event-catalog
title: Domain Events — BC02 (SLC-04)
wave: W4
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC02 (SLC-04)

_23 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-CNF-DETECTED | AGG-CONFLICT | SYS:conflict rule matched | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) | tenant_id + aggregate.id |
| EVT-CNF-RAISED | AGG-CONFLICT | CMD-CNF-RAISE | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) | tenant_id + aggregate.id |
| EVT-CNF-CLAIM-ADDED | AGG-CONFLICT | SYS:incompatible claim joined | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) | tenant_id + aggregate.id |
| EVT-CNF-ASSIGNED | AGG-CONFLICT | CMD-CNF-ASSIGN | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) | tenant_id + aggregate.id |
| EVT-CNF-REVIEW-STARTED | AGG-CONFLICT | CMD-CNF-START-REVIEW | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) | tenant_id + aggregate.id |
| EVT-CNF-RESOLVED | AGG-CONFLICT | CMD-CNF-RESOLVE | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) | tenant_id + aggregate.id |
| EVT-CNF-ACCEPTED | AGG-CONFLICT | CMD-CNF-ACCEPT | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) | tenant_id + aggregate.id |
| EVT-CNF-REOPENED | AGG-CONFLICT | CMD-CNF-REOPEN | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) | tenant_id + aggregate.id |
| EVT-CNF-SUPERSEDED | AGG-CONFLICT | SYS:member set no longer conflicting | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) | tenant_id + aggregate.id |
| EVT-ER-PROPOSED | AGG-ER-CASE | SYS:candidate generator score ≥ propose threshold, CMD-ER-PROPOSE | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) | tenant_id + aggregate.id |
| EVT-ER-REVIEW-STARTED | AGG-ER-CASE | CMD-ER-START-REVIEW | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) | tenant_id + aggregate.id |
| EVT-ER-MATCHED | AGG-ER-CASE | CMD-ER-DECIDE-MATCH | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) | tenant_id + aggregate.id |
| EVT-ER-NOT-MATCHED | AGG-ER-CASE | CMD-ER-DECIDE-NOT-MATCH, CMD-ER-DECIDE-NOT-MATCH | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) | tenant_id + aggregate.id |
| EVT-ER-PARKED | AGG-ER-CASE | CMD-ER-PARK | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) | tenant_id + aggregate.id |
| EVT-ER-RESUMED | AGG-ER-CASE | CMD-ER-RESUME | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) | tenant_id + aggregate.id |
| EVT-ER-SPLIT-REQUESTED | AGG-ER-CASE | CMD-ER-REQUEST-SPLIT | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) | tenant_id + aggregate.id |
| EVT-ER-MATCH-CONFIRMED | AGG-ER-CASE | CMD-ER-CONFIRM-MATCH | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) | tenant_id + aggregate.id |
| EVT-ER-SPLIT | AGG-ER-CASE | CMD-ER-SPLIT | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) | tenant_id + aggregate.id |
| EVT-ER-WITHDRAWN | AGG-ER-CASE | CMD-ER-WITHDRAW | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) | tenant_id + aggregate.id |
| EVT-MRS-DRAFTED | AGG-MATCH-RULESET | CMD-MRS-DRAFT | — | Candidate generator (reloads ruleset) | tenant_id + aggregate.id |
| EVT-MRS-EDITED | AGG-MATCH-RULESET | CMD-MRS-EDIT | — | Candidate generator (reloads ruleset) | tenant_id + aggregate.id |
| EVT-MRS-ACTIVATED | AGG-MATCH-RULESET | CMD-MRS-ACTIVATE | — | Candidate generator (reloads ruleset) | tenant_id + aggregate.id |
| EVT-MRS-SUPERSEDED | AGG-MATCH-RULESET | SYS:successor activated | — | Candidate generator (reloads ruleset) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
