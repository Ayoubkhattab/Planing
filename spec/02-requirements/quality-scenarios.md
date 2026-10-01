---
id: QAS-CAT
type: quality-scenarios
title: Quality Attribute Scenarios — R1
wave: W2
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: priority = importance/difficulty. كل الأرقام أهداف تصميم مفوّضة.
---

# Quality Attribute Scenarios — R1

> priority = importance/difficulty. كل الأرقام أهداف تصميم مفوّضة.

## scenarios

_95 items_

### QAS-PERF-001

- **quality:** performance
- **source:** user
- **stimulus:** submits a state-changing command
- **environment:** design envelope load (5,000 concurrent users)
- **artifact:** command API
- **response:** command validated, authorized, committed and acknowledged
- **response_measure:** p95 ≤ 300 ms; p99 ≤ 1 s
- **workload:** WL-01
- **priority:** H/M
- **origin:** W2 delegated target
- **refines:** BRQ-004

### QAS-PERF-002

- **quality:** performance
- **source:** user
- **stimulus:** reads a single object or a list page
- **environment:** design envelope load
- **artifact:** query API
- **response:** authorized result returned
- **response_measure:** single object p95 ≤ 300 ms; list page p95 ≤ 1 s
- **workload:** WL-01
- **priority:** H/M
- **origin:** W2 delegated target
- **refines:** BRQ-001, BRQ-004

### QAS-PERF-003

- **quality:** performance
- **source:** user
- **stimulus:** runs a combined text + spatial + temporal search
- **environment:** design envelope load
- **artifact:** search
- **response:** authorized results returned
- **response_measure:** p95 ≤ 1 s
- **workload:** WL-02
- **priority:** H/H
- **origin:** W1 Q23
- **refines:** BRQ-001

### QAS-PERF-004

- **quality:** performance
- **source:** system
- **stimulus:** an object is created or changed
- **environment:** sustained design event rate
- **artifact:** search projection
- **response:** change visible in search
- **response_measure:** index lag p95 ≤ 30 s
- **workload:** WL-02
- **priority:** M/M
- **origin:** W1 Q23
- **refines:** BRQ-001

### QAS-PERF-005

- **quality:** performance
- **source:** sensor / adapter
- **stimulus:** reports a value that meets a critical alert rule
- **environment:** 5,000 events/s sustained
- **artifact:** ingestion → alerting → notification
- **response:** authorized subscribers notified
- **response_measure:** end-to-end p95 ≤ 5 s
- **workload:** WL-06
- **priority:** H/H
- **origin:** W1 Q23
- **refines:** BRQ-002

### QAS-PERF-006

- **quality:** performance
- **source:** system
- **stimulus:** a situation member changes
- **environment:** design envelope load
- **artifact:** situation view
- **response:** open views reflect the change
- **response_measure:** p95 ≤ 10 s
- **workload:** WL-06
- **priority:** H/M
- **origin:** W1 Q23
- **refines:** BRQ-002

### QAS-PERF-007

- **quality:** performance
- **source:** user
- **stimulus:** pans or zooms the operational map
- **environment:** design envelope load
- **artifact:** map / tile service
- **response:** authorized tiles rendered
- **response_measure:** tile p95 ≤ 500 ms
- **workload:** WL-03
- **priority:** M/H
- **origin:** W2 delegated target
- **refines:** BRQ-002

### QAS-PERF-008

- **quality:** performance
- **source:** field user
- **stimulus:** records an observation (online)
- **environment:** normal
- **artifact:** observation → search
- **response:** observation searchable
- **response_measure:** p95 ≤ 30 s
- **workload:** WL-02
- **priority:** M/M
- **origin:** OUT-01
- **refines:** BRQ-001

### QAS-SCAL-001

- **quality:** scalability
- **source:** load test
- **stimulus:** load rises from pilot (100 concurrent) to 10× (1,000) and then to design (5,000)
- **environment:** normal
- **artifact:** whole platform
- **response:** performance targets hold with horizontal scaling only
- **response_measure:** 0 architectural or schema changes needed
- **workload:** WL-01
- **priority:** H/H
- **origin:** W1 Q7
- **refines:** BRQ-001, BRQ-004

### QAS-SCAL-002

- **quality:** scalability
- **source:** sources
- **stimulus:** event burst of 50,000/s for 60 s
- **environment:** design load
- **artifact:** ingestion pipeline
- **response:** backpressure applied, no data lost
- **response_measure:** 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PERF-005 ≤ 5 min after
- **workload:** WL-06
- **priority:** H/H
- **origin:** W1 Q11
- **refines:** BRQ-001, BRQ-004

### QAS-SCAL-003

- **quality:** scalability
- **source:** operator
- **stimulus:** provisions a new tenant
- **environment:** up to 100 tenants
- **artifact:** provisioning
- **response:** tenant usable
- **response_measure:** automated; ≤ 1 hour; no code or schema change
- **workload:** —
- **priority:** M/M
- **origin:** W1 Q6
- **refines:** BRQ-001, BRQ-004

### QAS-SCAL-004

- **quality:** scalability
- **source:** time
- **stimulus:** observations grow to 1e9
- **environment:** design data volume
- **artifact:** observation store
- **response:** time-bounded queries keep targets
- **response_measure:** QAS-PERF-002 holds for queries with a time window ≤ 30 days
- **workload:** WL-01
- **priority:** M/H
- **origin:** W1 Q11
- **refines:** BRQ-001, BRQ-004

### QAS-SCAL-005

- **quality:** scalability
- **source:** noisy tenant
- **stimulus:** exceeds its quota by 10×
- **environment:** shared cell
- **artifact:** quota / rate limiter
- **response:** other tenants unaffected
- **response_measure:** other tenants stay within QAS-PERF-001
- **workload:** —
- **priority:** H/M
- **origin:** SR-07
- **refines:** BRQ-001, BRQ-004

### QAS-AVL-001

- **quality:** availability
- **source:** any
- **stimulus:** normal operation over a month
- **environment:** production
- **artifact:** critical tier capabilities
- **response:** service available
- **response_measure:** ≥ 99.9 % monthly
- **workload:** —
- **priority:** H/H
- **origin:** W1 Q21
- **refines:** BRQ-002, BRQ-004

### QAS-AVL-002

- **quality:** availability
- **source:** any
- **stimulus:** normal operation over a month
- **environment:** production
- **artifact:** important tier capabilities
- **response:** service available
- **response_measure:** ≥ 99.5 % monthly
- **workload:** —
- **priority:** M/M
- **origin:** W1 Q21
- **refines:** BRQ-002, BRQ-004

### QAS-AVL-003

- **quality:** availability
- **source:** any
- **stimulus:** normal operation over a month
- **environment:** production
- **artifact:** standard tier capabilities
- **response:** service available
- **response_measure:** ≥ 99 % monthly
- **workload:** —
- **priority:** L/L
- **origin:** W1 Q21
- **refines:** BRQ-002, BRQ-004

### QAS-REC-001

- **quality:** recoverability
- **source:** disaster
- **stimulus:** primary site lost
- **environment:** production
- **artifact:** critical tier
- **response:** restored
- **response_measure:** RPO ≤ 5 min; RTO ≤ 1 h
- **workload:** —
- **priority:** H/H
- **origin:** W1 Q21
- **refines:** BRQ-002, BRQ-004

### QAS-REC-002

- **quality:** recoverability
- **source:** disaster
- **stimulus:** primary site lost
- **environment:** production
- **artifact:** important tier
- **response:** restored
- **response_measure:** RPO ≤ 15 min; RTO ≤ 4 h
- **workload:** —
- **priority:** M/M
- **origin:** W1 Q21
- **refines:** BRQ-002, BRQ-004

### QAS-REC-003

- **quality:** recoverability
- **source:** disaster
- **stimulus:** primary site lost
- **environment:** production
- **artifact:** standard tier
- **response:** restored
- **response_measure:** RPO ≤ 24 h; RTO ≤ 24 h
- **workload:** —
- **priority:** L/L
- **origin:** W1 Q21
- **refines:** BRQ-002, BRQ-004

### QAS-REL-001

- **quality:** reliability
- **source:** infrastructure
- **stimulus:** event bus unavailable for 30 min
- **environment:** normal load
- **artifact:** outbox publisher
- **response:** commands keep succeeding; events published after recovery
- **response_measure:** 0 lost events; 0 duplicates with effect
- **workload:** WL-06
- **priority:** H/M
- **origin:** PRJ§106
- **refines:** BRQ-006, BRQ-007

### QAS-REL-002

- **quality:** resilience
- **source:** infrastructure
- **stimulus:** search projection unavailable
- **environment:** normal load
- **artifact:** platform
- **response:** commands, direct reads and maps keep working; search shows degraded state
- **response_measure:** critical tier unaffected; index rebuilt without data loss
- **workload:** WL-02
- **priority:** M/M
- **origin:** PRJ§107
- **refines:** BRQ-006, BRQ-007

### QAS-REL-003

- **quality:** integrity
- **source:** two users
- **stimulus:** update the same object from the same version
- **environment:** concurrent
- **artifact:** any aggregate
- **response:** second update rejected
- **response_measure:** 0 silent overwrites
- **workload:** WL-01
- **priority:** H/L
- **origin:** PRJ§104
- **refines:** BRQ-006, BRQ-007

### QAS-SEC-001

- **quality:** security
- **source:** authenticated user of tenant A
- **stimulus:** attempts to access tenant B data by any path
- **environment:** normal
- **artifact:** all access paths
- **response:** access denied and audited
- **response_measure:** 0 leaks in tenant-isolation suite
- **workload:** —
- **priority:** H/H
- **origin:** W1 Q6
- **refines:** BRQ-007

### QAS-SEC-002

- **quality:** security
- **source:** authenticated user without clearance
- **stimulus:** searches, lists, maps or receives alerts touching objects above clearance
- **environment:** normal
- **artifact:** search, lists, maps, alerts, notifications
- **response:** no disclosure of content or existence
- **response_measure:** 0 leakage in inference suite (counts, facets, ordering, timing, errors)
- **workload:** WL-02
- **priority:** H/H
- **origin:** BRL-010; A21
- **refines:** BRQ-007

### QAS-SEC-003

- **quality:** security
- **source:** security officer
- **stimulus:** removes a user's compartment
- **environment:** normal
- **artifact:** all access paths
- **response:** object no longer returned to that user
- **response_measure:** effective on next request in every path, independent of index lag
- **workload:** —
- **priority:** H/H
- **origin:** W1 Q16
- **refines:** BRQ-007

### QAS-SEC-004

- **quality:** security
- **source:** two users with different compartments
- **stimulus:** request the same map tile
- **environment:** normal
- **artifact:** tile cache
- **response:** each receives only authorized content
- **response_measure:** 0 cross-scope cache hits
- **workload:** WL-03
- **priority:** H/M
- **origin:** ADR-P06
- **refines:** BRQ-007

### QAS-SEC-005

- **quality:** security
- **source:** fault
- **stimulus:** policy engine unavailable
- **environment:** normal
- **artifact:** authorization
- **response:** requests denied
- **response_measure:** 100 % fail-closed
- **workload:** —
- **priority:** H/L
- **origin:** SL-28
- **refines:** BRQ-007

### QAS-SEC-006

- **quality:** security
- **source:** insider
- **stimulus:** modifies an audit record in storage
- **environment:** production
- **artifact:** audit store
- **response:** tampering detected
- **response_measure:** detected by next integrity check (≤ 24 h)
- **workload:** —
- **priority:** H/M
- **origin:** PRJ§3.4
- **refines:** BRQ-007

### QAS-SEC-007

- **quality:** security
- **source:** thief
- **stimulus:** obtains a field device
- **environment:** device powered off or locked
- **artifact:** mobile app storage
- **response:** data unreadable
- **response_measure:** 0 readable records without authentication; wipe on next connection
- **workload:** WL-12
- **priority:** H/M
- **origin:** W1 Q9
- **refines:** BRQ-007

### QAS-PRV-001

- **quality:** privacy
- **source:** data protection officer
- **stimulus:** orders erasure of a data subject
- **environment:** production
- **artifact:** all stores and backups
- **response:** personal data unrecoverable, audit facts kept
- **response_measure:** operational & projections ≤ 24 h; backups unrecoverable immediately via key destruction
- **workload:** —
- **priority:** H/H
- **origin:** W1 Q18
- **refines:** BRQ-007

### QAS-OFF-001

- **quality:** offline
- **source:** field user
- **stimulus:** works 72 h offline then reconnects on a 1 Mbps link
- **environment:** field
- **artifact:** sync
- **response:** all changes synchronized; conflicts routed to review
- **response_measure:** 1,000 queued commands synced ≤ 10 min; 0 silent overwrites; 0 duplicates
- **workload:** WL-12
- **priority:** H/H
- **origin:** W1 Q9
- **refines:** BRQ-001

### QAS-DQ-001

- **quality:** data quality
- **source:** adapter
- **stimulus:** submits records with invalid geometry or missing CRS
- **environment:** normal
- **artifact:** ingestion
- **response:** records quarantined with reason
- **response_measure:** 100 % of invalid records quarantined; 0 published
- **workload:** WL-15
- **priority:** H/L
- **origin:** REQ-INF-006
- **refines:** BRQ-008

### QAS-TMP-001

- **quality:** correctness
- **source:** analyst
- **stimulus:** asks for state as of valid time T known at record time K
- **environment:** normal
- **artifact:** temporal query
- **response:** correct historical state
- **response_measure:** 100 % agreement with temporal oracle corpus
- **workload:** WL-04
- **priority:** H/H
- **origin:** W1 Q13
- **refines:** BRQ-006

### QAS-AUD-001

- **quality:** auditability
- **source:** any actor
- **stimulus:** executes a state-changing command
- **environment:** normal
- **artifact:** audit
- **response:** audit record written
- **response_measure:** 100 % of commands audited with all fields
- **workload:** —
- **priority:** H/L
- **origin:** BRL-015
- **refines:** BRQ-007

### QAS-TRC-001

- **quality:** traceability
- **source:** auditor
- **stimulus:** follows a decision back to its sources
- **environment:** normal
- **artifact:** lineage / provenance
- **response:** complete path returned
- **response_measure:** 100 % of decisions and T1 derived objects traceable to sources
- **workload:** —
- **priority:** H/M
- **origin:** OUT-03, OUT-04
- **refines:** BRQ-006

### QAS-TRC-002

- **quality:** reproducibility
- **source:** analyst
- **stimulus:** re-executes a recorded deterministic analysis run
- **environment:** normal
- **artifact:** analysis
- **response:** identical results
- **response_measure:** 100 %
- **workload:** WL-11
- **priority:** M/M
- **origin:** OUT-03
- **refines:** BRQ-006

### QAS-USA-001

- **quality:** usability
- **source:** field user
- **stimulus:** records an observation with one photo on the mobile app
- **environment:** field, one hand
- **artifact:** mobile app
- **response:** observation saved
- **response_measure:** median ≤ 60 s in usability test with 10 field users
- **workload:** WL-12
- **priority:** M/M
- **origin:** W2 delegated target
- **refines:** BRQ-001

### QAS-USA-002

- **quality:** usability
- **source:** analyst
- **stimulus:** searches a name with Arabic spelling variants or Latin transliteration
- **environment:** normal
- **artifact:** search
- **response:** same entity found
- **response_measure:** recall ≥ 95 % on the Arabic name test set
- **workload:** WL-02
- **priority:** H/H
- **origin:** W1 Q15
- **refines:** BRQ-001

### QAS-ACC-001

- **quality:** accessibility
- **source:** user with assistive technology
- **stimulus:** uses R1 web screens
- **environment:** normal
- **artifact:** web UI
- **response:** tasks completable
- **response_measure:** WCAG 2.2 level AA conformance (AR and EN)
- **workload:** —
- **priority:** M/M
- **origin:** W2 delegated decision (closes UNK-016)
- **refines:** BRQ-001

### QAS-EVO-001

- **quality:** evolvability
- **source:** developer
- **stimulus:** changes an API or event contract
- **environment:** CI
- **artifact:** contracts
- **response:** breaking change blocked unless new major version
- **response_measure:** previous major version supported ≥ 6 months after successor
- **workload:** —
- **priority:** M/L
- **origin:** PRJ§97
- **refines:** BRQ-008

### QAS-OPS-001

- **quality:** operability
- **source:** operator
- **stimulus:** installs or upgrades in an air-gapped site
- **environment:** no internet
- **artifact:** platform
- **response:** install / upgrade completes; rollback possible
- **response_measure:** offline bundle only; rollback ≤ 1 h
- **workload:** —
- **priority:** H/M
- **origin:** W1 Q20
- **refines:** BRQ-007

### QAS-OBS-001

- **quality:** observability
- **source:** operator
- **stimulus:** investigates a failed request
- **environment:** production
- **artifact:** all components
- **response:** full trace found by correlation id
- **response_measure:** 100 % of requests traceable end to end
- **workload:** —
- **priority:** M/M
- **origin:** PRJ§26
- **refines:** BRQ-007

### QAS-COST-001

- **quality:** cost
- **source:** finance
- **stimulus:** requests monthly cost per tenant
- **environment:** production
- **artifact:** telemetry
- **response:** report produced
- **response_measure:** computed from telemetry with no manual input
- **workload:** —
- **priority:** M/M
- **origin:** W1 Q29
- **refines:** BRQ-007

### QAS-PERF-009

- **quality:** performance
- **source:** system
- **stimulus:** PEP requests a policy decision
- **environment:** 10,000 decisions/s
- **artifact:** SLC-01
- **response:** as measured
- **response_measure:** p95 ≤ 5 ms with embedded evaluator; ≤ 20 ms remote
- **workload:** WL-01
- **priority:** H/M
- **origin:** SLC-01 W5 delegated
- **refines:** BRQ-007

### QAS-PERF-010

- **quality:** performance
- **source:** system
- **stimulus:** gateway resolves SecurityContext
- **environment:** 7,500 req/s peak
- **artifact:** SLC-01
- **response:** as measured
- **response_measure:** p95 ≤ 20 ms (cache hit p95 ≤ 2 ms)
- **workload:** WL-01
- **priority:** H/M
- **origin:** SLC-01 W5 delegated
- **refines:** BRQ-007

### QAS-PERF-011

- **quality:** performance
- **source:** system
- **stimulus:** a command commits
- **environment:** normal
- **artifact:** SLC-01
- **response:** as measured
- **response_measure:** audit record in BC08 store ≤ 5 s p95; anchor ≤ 5 min
- **workload:** WL-01
- **priority:** H/M
- **origin:** SLC-01 W5 delegated
- **refines:** BRQ-007

### QAS-SEC-008

- **quality:** security
- **source:** system
- **stimulus:** user disabled via SCIM
- **environment:** normal
- **artifact:** SLC-01
- **response:** as measured
- **response_measure:** next request from any session denied; SCIM-to-effect ≤ 5 min (REQ-FND-005)
- **workload:** WL-01
- **priority:** H/M
- **origin:** SLC-01 W5 delegated
- **refines:** BRQ-007

### QAS-PERF-012

- **quality:** performance
- **source:** user/system
- **stimulus:** batch of 1,000 observations
- **environment:** 5,000 obs/s sustained per cell
- **artifact:** SLC-02
- **response:** as measured
- **response_measure:** batch commit p95 ≤ 1 s; 0 duplicates on retry
- **workload:** WL-01/06
- **priority:** H/M
- **origin:** SLC-02 W5 delegated
- **refines:** BRQ-001

### QAS-PERF-013

- **quality:** performance
- **source:** user/system
- **stimulus:** resolved entity read (current)
- **environment:** 750 reads/s; 1e8 claims
- **artifact:** SLC-02
- **response:** as measured
- **response_measure:** p95 ≤ 300 ms end-to-end
- **workload:** WL-01/06
- **priority:** H/M
- **origin:** SLC-02 W5 delegated
- **refines:** BRQ-002

### QAS-PERF-014

- **quality:** performance
- **source:** user/system
- **stimulus:** lineage trace depth 5
- **environment:** normal
- **artifact:** SLC-02
- **response:** as measured
- **response_measure:** p95 ≤ 2 s
- **workload:** WL-01/06
- **priority:** H/M
- **origin:** SLC-02 W5 delegated
- **refines:** BRQ-006

### QAS-SEC-009

- **quality:** security
- **source:** user/system
- **stimulus:** user without source-protection permission reads claims of a protected human source
- **environment:** normal
- **artifact:** SLC-02
- **response:** as measured
- **response_measure:** 0 identity attributes disclosed in any response, export or lineage
- **workload:** WL-01/06
- **priority:** H/M
- **origin:** SLC-02 W5 delegated
- **refines:** BRQ-007

### QAS-SEC-010

- **quality:** security
- **source:** user/system
- **stimulus:** user sees an entity but not some of its claims
- **environment:** normal
- **artifact:** SLC-02
- **response:** as measured
- **response_measure:** hidden claims affect neither status, counts, completeness nor timing (inference suite)
- **workload:** WL-01/06
- **priority:** H/M
- **origin:** SLC-02 W5 delegated
- **refines:** BRQ-007

### QAS-ER-001

- **quality:** accuracy
- **source:** system/analyst
- **stimulus:** candidate recall on labelled AR/EN test set
- **environment:** ruleset evaluation
- **artifact:** SLC-04
- **response:** as measured
- **response_measure:** ≥ 95 % of true matches proposed
- **workload:** WL-08
- **priority:** H/M
- **origin:** SLC-04 W5 delegated
- **refines:** BRQ-001

### QAS-ER-002

- **quality:** usability
- **source:** system/analyst
- **stimulus:** precision of proposals in review queue
- **environment:** ruleset evaluation
- **artifact:** SLC-04
- **response:** as measured
- **response_measure:** ≥ 60 % of proposals are true matches
- **workload:** WL-08
- **priority:** H/M
- **origin:** SLC-04 W5 delegated
- **refines:** BRQ-001

### QAS-ER-003

- **quality:** performance
- **source:** system/analyst
- **stimulus:** new entity registered
- **environment:** normal load
- **artifact:** SLC-04
- **response:** as measured
- **response_measure:** candidates visible p95 ≤ 60 s
- **workload:** WL-08
- **priority:** H/M
- **origin:** SLC-04 W5 delegated
- **refines:** BRQ-001

### QAS-CNF-001

- **quality:** performance
- **source:** system/analyst
- **stimulus:** incompatible claim committed
- **environment:** normal load
- **artifact:** SLC-04
- **response:** as measured
- **response_measure:** conflict opened p95 ≤ 30 s
- **workload:** WL-08
- **priority:** H/M
- **origin:** SLC-04 W5 delegated
- **refines:** BRQ-006

### QAS-PERF-015

- **quality:** performance
- **source:** system/analyst
- **stimulus:** resolved read of clustered entity
- **environment:** 750 reads/s
- **artifact:** SLC-04
- **response:** as measured
- **response_measure:** ≤ 20 % overhead vs unclustered; p95 ≤ 300 ms
- **workload:** WL-08
- **priority:** H/M
- **origin:** SLC-04 W5 delegated
- **refines:** BRQ-002

### QAS-PERF-016

- **quality:** performance
- **source:** user/system
- **stimulus:** field user opens 'my tasks'
- **environment:** design load
- **artifact:** SLC-03
- **response:** as measured
- **response_measure:** p95 ≤ 500 ms
- **workload:** WL-01
- **priority:** H/M
- **origin:** SLC-03 W5 delegated
- **refines:** BRQ-004

### QAS-OPS-002

- **quality:** timeliness
- **source:** user/system
- **stimulus:** task reaches due_at
- **environment:** normal
- **artifact:** SLC-03
- **response:** as measured
- **response_measure:** escalation event ≤ 60 s after due
- **workload:** WL-01
- **priority:** H/M
- **origin:** SLC-03 W5 delegated
- **refines:** BRQ-004

### QAS-PERF-017

- **quality:** performance
- **source:** user/system
- **stimulus:** assignment with eligibility check
- **environment:** normal
- **artifact:** SLC-03
- **response:** as measured
- **response_measure:** p95 ≤ 500 ms including BC05 call
- **workload:** WL-01
- **priority:** H/M
- **origin:** SLC-03 W5 delegated
- **refines:** BRQ-004

### QAS-SEC-011

- **quality:** security
- **source:** user/operator
- **stimulus:** inference test suite on search, suggestions, facets, graph and paths
- **environment:** normal
- **artifact:** SLC-05
- **response:** as measured
- **response_measure:** 0 disclosures of hidden objects, hidden facts, hidden nodes/edges
- **workload:** WL-02
- **priority:** H/H
- **origin:** SLC-05 W5 delegated
- **refines:** BRQ-007

### QAS-PERF-018

- **quality:** performance
- **source:** user/operator
- **stimulus:** graph neighborhood depth 2
- **environment:** design load, dense nodes
- **artifact:** SLC-05
- **response:** as measured
- **response_measure:** p95 ≤ 1 s
- **workload:** WL-02
- **priority:** H/H
- **origin:** SLC-05 W5 delegated
- **refines:** BRQ-002

### QAS-REL-004

- **quality:** recoverability
- **source:** user/operator
- **stimulus:** full projection rebuild
- **environment:** design volume
- **artifact:** SLC-05
- **response:** as measured
- **response_measure:** ≤ 24 h to READY with no loss of query service (old version stays ACTIVE)
- **workload:** WL-02
- **priority:** H/H
- **origin:** SLC-05 W5 delegated
- **refines:** BRQ-006

### QAS-PERF-019

- **quality:** performance
- **source:** user/system
- **stimulus:** situation picture read (≤ 2,000 visible members)
- **environment:** design load
- **artifact:** SLC-06
- **response:** as measured
- **response_measure:** p95 ≤ 1 s
- **workload:** WL-06
- **priority:** H/M
- **origin:** SLC-06 W5 delegated
- **refines:** BRQ-002

### QAS-SEC-012

- **quality:** security
- **source:** user/system
- **stimulus:** user not cleared for an alert's label
- **environment:** normal
- **artifact:** SLC-06
- **response:** as measured
- **response_measure:** receives no alert, notification, push or count change
- **workload:** WL-06
- **priority:** H/M
- **origin:** SLC-06 W5 delegated
- **refines:** BRQ-007

### QAS-OPS-003

- **quality:** operability
- **source:** user/system
- **stimulus:** push gateway unavailable (air-gapped)
- **environment:** field network
- **artifact:** SLC-06
- **response:** as measured
- **response_measure:** in-app inbox current; polling fallback ≤ 60 s
- **workload:** WL-06
- **priority:** H/M
- **origin:** SLC-06 W5 delegated
- **refines:** BRQ-004

### QAS-PERF-020

- **quality:** fairness
- **source:** analyst
- **stimulus:** tenant submits 100 runs
- **environment:** shared compute pool
- **artifact:** SLC-07
- **response:** as measured
- **response_measure:** no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s
- **workload:** WL-11
- **priority:** H/M
- **origin:** SLC-07 W5 delegated
- **refines:** BRQ-003

### QAS-SEC-013

- **quality:** security
- **source:** analyst
- **stimulus:** run submitted by user U
- **environment:** normal
- **artifact:** SLC-07
- **response:** as measured
- **response_measure:** run reads only data visible to U; results labelled ≥ max input label
- **workload:** WL-11
- **priority:** H/M
- **origin:** SLC-07 W5 delegated
- **refines:** BRQ-007

### QAS-PERF-021

- **quality:** performance
- **source:** planner/auditor
- **stimulus:** plan version baselined with 500 task-generating activities
- **environment:** normal
- **artifact:** SLC-08
- **response:** as measured
- **response_measure:** task synchronization completes ≤ 60 s; idempotent on retry
- **workload:** WL-01
- **priority:** H/M
- **origin:** SLC-08 W5 delegated
- **refines:** BRQ-004

### QAS-TRC-003

- **quality:** traceability
- **source:** planner/auditor
- **stimulus:** auditor asks for a decision's basis
- **environment:** normal
- **artifact:** SLC-08
- **response:** as measured
- **response_measure:** authority chain, pinned citations and claims as known at decision time returned; 100 % of decisions
- **workload:** WL-01
- **priority:** H/M
- **origin:** SLC-08 W5 delegated
- **refines:** BRQ-003

### QAS-OFF-002

- **quality:** security
- **source:** field
- **stimulus:** user's clearance reduced while device offline
- **environment:** reconnect
- **artifact:** SLC-11
- **response:** as measured
- **response_measure:** packages revoked and purged on next contact; commands evaluated under current authorization
- **workload:** WL-12
- **priority:** H/H
- **origin:** SLC-11 W5 delegated
- **refines:** BRQ-007

### QAS-OFF-003

- **quality:** scalability
- **source:** field
- **stimulus:** 5,000 devices reconnect within 10 min
- **environment:** morning shift start
- **artifact:** SLC-11
- **response:** as measured
- **response_measure:** all sessions complete ≤ 30 min; oldest-offline devices first; no data loss
- **workload:** WL-12
- **priority:** H/H
- **origin:** SLC-11 W5 delegated
- **refines:** BRQ-001

### QAS-PRV-002

- **quality:** privacy
- **source:** operator/legal
- **stimulus:** restore of a key-store backup older than a key destruction
- **environment:** DR drill
- **artifact:** SLC-12a
- **response:** as measured
- **response_measure:** destroyed keys unusable before any service reads data (restore gate)
- **workload:** WL-14
- **priority:** H/H
- **origin:** SLC-12a W5 delegated
- **refines:** BRQ-007

### QAS-GOV-001

- **quality:** compliance
- **source:** operator/legal
- **stimulus:** daily disposition evaluation
- **environment:** design volume
- **artifact:** SLC-12a
- **response:** as measured
- **response_measure:** candidates computed ≤ 1 h; 0 held records destroyed
- **workload:** WL-14
- **priority:** H/H
- **origin:** SLC-12a W5 delegated
- **refines:** BRQ-007

### QAS-AI-001

- **quality:** AI quality
- **source:** user/system
- **stimulus:** evaluation set of 500 questions
- **environment:** citation accuracy
- **artifact:** R2
- **response:** as measured
- **response_measure:** ≥ 95 % of cited items actually support the statement
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-003
- **release:** R2
- **requirement:** REQ-AI-004

### QAS-AI-002

- **quality:** AI quality
- **source:** user/system
- **stimulus:** insufficient-evidence and hallucination sets
- **environment:** hallucination rate
- **artifact:** R2
- **response:** as measured
- **response_measure:** ≤ 2 % unsupported statements; ≥ 95 % correct 'Insufficient Evidence'
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-003
- **release:** R2
- **requirement:** REQ-AI-003

### QAS-AI-003

- **quality:** performance
- **source:** user/system
- **stimulus:** grounded Q&A request
- **environment:** design load (50 concurrent AI requests per cell)
- **artifact:** R2
- **response:** as measured
- **response_measure:** first token ≤ 3 s, full answer p95 ≤ 20 s on local models
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-003
- **release:** R2
- **requirement:** REQ-AI-001

### QAS-AI-004

- **quality:** security
- **source:** user/system
- **stimulus:** prompt-injection, exfiltration and unauthorized-retrieval suites
- **environment:** normal
- **artifact:** R2
- **response:** as measured
- **response_measure:** 0 unauthorized retrievals, 0 tool abuse, 0 cross-tenant leakage
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-003
- **release:** R2
- **requirement:** REQ-AI-002

### QAS-AI-005

- **quality:** cost
- **source:** user/system
- **stimulus:** AI usage per tenant
- **environment:** monthly
- **artifact:** R2
- **response:** as measured
- **response_measure:** GPU-hours and cost per request reported per tenant
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-003
- **release:** R2
- **requirement:** REQ-AI-001

### QAS-RES-001

- **quality:** integrity
- **source:** user/system
- **stimulus:** 100 concurrent allocation requests on one pool
- **environment:** normal
- **artifact:** R2
- **response:** as measured
- **response_measure:** 0 over-commitment; deterministic priority order
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-004
- **release:** R2
- **requirement:** REQ-RES-008

### QAS-RES-002

- **quality:** performance
- **source:** user/system
- **stimulus:** availability query for 1,000 assets over 30 days
- **environment:** normal
- **artifact:** R2
- **response:** as measured
- **response_measure:** p95 ≤ 1 s
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-004
- **release:** R2
- **requirement:** REQ-RES-006

### QAS-PRD-001

- **quality:** performance
- **source:** user/system
- **stimulus:** generate a 30-page product with 10 maps
- **environment:** normal
- **artifact:** R2
- **response:** as measured
- **response_measure:** ≤ 2 min (async job)
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-001
- **release:** R2
- **requirement:** REQ-PRD-001

### QAS-PRD-002

- **quality:** security
- **source:** user/system
- **stimulus:** product rendered for an audience
- **environment:** normal
- **artifact:** R2
- **response:** as measured
- **response_measure:** 0 content above the product label (inference suite on products)
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-001
- **release:** R2
- **requirement:** REQ-PRD-002

### QAS-ARC-001

- **quality:** performance
- **source:** user/system
- **stimulus:** retrieve an archived record
- **environment:** archive tier
- **artifact:** R2
- **response:** as measured
- **response_measure:** ≤ 1 min for warm, ≤ 24 h for cold/offline media
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-005
- **release:** R2
- **requirement:** REQ-ARC-003

### QAS-ARC-002

- **quality:** correctness
- **source:** user/system
- **stimulus:** historical reconstruction scenarios
- **environment:** normal
- **artifact:** R2
- **response:** as measured
- **response_measure:** 100 % agreement with oracle; every element labelled
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-005
- **release:** R2
- **requirement:** REQ-ARC-004

### QAS-ARC-003

- **quality:** integrity
- **source:** user/system
- **stimulus:** yearly archive integrity verification
- **environment:** archive
- **artifact:** R2
- **response:** as measured
- **response_measure:** 0 unreported corruption; repair from replica
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-005
- **release:** R2
- **requirement:** REQ-ARC-002

### QAS-KNW-001

- **quality:** usability
- **source:** user/system
- **stimulus:** planner creates a plan for a known task type
- **environment:** normal
- **artifact:** R2
- **response:** as measured
- **response_measure:** relevant published lessons suggested in ≥ 80 % of cases in pilot
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-005
- **release:** R2
- **requirement:** REQ-KNW-003

### QAS-COL-001

- **quality:** traceability
- **source:** user/system
- **stimulus:** collection requirement fulfilment
- **environment:** normal
- **artifact:** R2
- **response:** as measured
- **response_measure:** 100 % of fulfilment links traceable to validated observations
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-001
- **release:** R2
- **requirement:** REQ-COL-003

### QAS-INT-001

- **quality:** reliability
- **source:** user/system
- **stimulus:** ERP adapter outage 4 h
- **environment:** normal
- **artifact:** R2
- **response:** as measured
- **response_measure:** no data loss; backlog processed ≤ 1 h after recovery
- **workload:** R2
- **priority:** H/M
- **origin:** W2-R2 delegated
- **refines:** BRQ-001
- **release:** R2
- **requirement:** REQ-INT-001

### QAS-RCM-001

- **quality:** performance
- **source:** user/system
- **stimulus:** CRISIS-severity incident assessed
- **environment:** normal
- **artifact:** R3
- **response:** as measured
- **response_measure:** response dispatched within the severity's SLA (tagged: recalibrate after Pilot R1 and R2 — RSK-028)
- **workload:** R3
- **priority:** H/M
- **origin:** W1/W2-R3 delegated
- **refines:** BRQ-004
- **release:** R3
- **requirement:** REQ-RCM-009

### QAS-RCM-002

- **quality:** governance
- **source:** user/system
- **stimulus:** risk moved to treated status
- **environment:** normal
- **artifact:** R3
- **response:** as measured
- **response_measure:** 100 % of treated risks have ≥ 1 treatment action or an explicit, authorized accept decision
- **workload:** R3
- **priority:** H/M
- **origin:** W1/W2-R3 delegated
- **refines:** BRQ-003
- **release:** R3
- **requirement:** REQ-RCM-004

### QAS-LOG-001

- **quality:** integrity
- **source:** user/system
- **stimulus:** concurrent logistics requests and task/plan allocations on the same resource pool
- **environment:** normal
- **artifact:** R3
- **response:** as measured
- **response_measure:** 0 over-commitment across combined demand; deterministic priority order (shared mechanism with QAS-RES-001)
- **workload:** R3
- **priority:** H/M
- **origin:** W1/W2-R3 delegated
- **refines:** BRQ-004
- **release:** R3
- **requirement:** REQ-LOG-002

### QAS-LOG-002

- **quality:** performance
- **source:** user/system
- **stimulus:** shipment dispatched to its destination
- **environment:** normal
- **artifact:** R3
- **response:** as measured
- **response_measure:** transit duration within target (tagged: recalibrate after Pilot R1 and R2 — RSK-028)
- **workload:** R3
- **priority:** H/M
- **origin:** W1/W2-R3 delegated
- **refines:** BRQ-004
- **release:** R3
- **requirement:** REQ-LOG-004

### QAS-TRX-001

- **quality:** integrity
- **source:** user/system
- **stimulus:** a simulation run nears completion (CMD-SIM-COMPLETE sent) with at least one exercise participant still unevaluated
- **environment:** normal
- **artifact:** R3
- **response:** as measured
- **response_measure:** 0 simulations reach COMPLETED with a participant lacking at least one recorded evaluation (INV-SIM-02)
- **workload:** R3
- **priority:** H/M
- **origin:** W1/W2-R3 delegated
- **refines:** BRQ-005
- **release:** R3
- **requirement:** REQ-TRX-010

### QAS-TRX-002

- **quality:** performance
- **source:** user/system
- **stimulus:** an inject delivered during a live simulation run
- **environment:** normal
- **artifact:** R3
- **response:** as measured
- **response_measure:** 'inject delivery recorded within target latency (tagged: recalibrate after Pilot R1 and R2 — RSK-028)'
- **workload:** R3
- **priority:** H/M
- **origin:** W1/W2-R3 delegated
- **refines:** BRQ-004
- **release:** R3
- **requirement:** REQ-TRX-008

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
scenarios:
- id: QAS-PERF-001
  quality: performance
  source: user
  stimulus: submits a state-changing command
  environment: design envelope load (5,000 concurrent users)
  artifact: command API
  response: command validated, authorized, committed and acknowledged
  response_measure: p95 ≤ 300 ms; p99 ≤ 1 s
  workload: WL-01
  priority: H/M
  origin: W2 delegated target
  refines:
  - BRQ-004
- id: QAS-PERF-002
  quality: performance
  source: user
  stimulus: reads a single object or a list page
  environment: design envelope load
  artifact: query API
  response: authorized result returned
  response_measure: single object p95 ≤ 300 ms; list page p95 ≤ 1 s
  workload: WL-01
  priority: H/M
  origin: W2 delegated target
  refines:
  - BRQ-001
  - BRQ-004
- id: QAS-PERF-003
  quality: performance
  source: user
  stimulus: runs a combined text + spatial + temporal search
  environment: design envelope load
  artifact: search
  response: authorized results returned
  response_measure: p95 ≤ 1 s
  workload: WL-02
  priority: H/H
  origin: W1 Q23
  refines:
  - BRQ-001
- id: QAS-PERF-004
  quality: performance
  source: system
  stimulus: an object is created or changed
  environment: sustained design event rate
  artifact: search projection
  response: change visible in search
  response_measure: index lag p95 ≤ 30 s
  workload: WL-02
  priority: M/M
  origin: W1 Q23
  refines:
  - BRQ-001
- id: QAS-PERF-005
  quality: performance
  source: sensor / adapter
  stimulus: reports a value that meets a critical alert rule
  environment: 5,000 events/s sustained
  artifact: ingestion → alerting → notification
  response: authorized subscribers notified
  response_measure: end-to-end p95 ≤ 5 s
  workload: WL-06
  priority: H/H
  origin: W1 Q23
  refines:
  - BRQ-002
- id: QAS-PERF-006
  quality: performance
  source: system
  stimulus: a situation member changes
  environment: design envelope load
  artifact: situation view
  response: open views reflect the change
  response_measure: p95 ≤ 10 s
  workload: WL-06
  priority: H/M
  origin: W1 Q23
  refines:
  - BRQ-002
- id: QAS-PERF-007
  quality: performance
  source: user
  stimulus: pans or zooms the operational map
  environment: design envelope load
  artifact: map / tile service
  response: authorized tiles rendered
  response_measure: tile p95 ≤ 500 ms
  workload: WL-03
  priority: M/H
  origin: W2 delegated target
  refines:
  - BRQ-002
- id: QAS-PERF-008
  quality: performance
  source: field user
  stimulus: records an observation (online)
  environment: normal
  artifact: observation → search
  response: observation searchable
  response_measure: p95 ≤ 30 s
  workload: WL-02
  priority: M/M
  origin: OUT-01
  refines:
  - BRQ-001
- id: QAS-SCAL-001
  quality: scalability
  source: load test
  stimulus: load rises from pilot (100 concurrent) to 10× (1,000) and then to design (5,000)
  environment: normal
  artifact: whole platform
  response: performance targets hold with horizontal scaling only
  response_measure: 0 architectural or schema changes needed
  workload: WL-01
  priority: H/H
  origin: W1 Q7
  refines: &id001
  - BRQ-001
  - BRQ-004
- id: QAS-SCAL-002
  quality: scalability
  source: sources
  stimulus: event burst of 50,000/s for 60 s
  environment: design load
  artifact: ingestion pipeline
  response: backpressure applied, no data lost
  response_measure: 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PERF-005 ≤ 5 min after
  workload: WL-06
  priority: H/H
  origin: W1 Q11
  refines: *id001
- id: QAS-SCAL-003
  quality: scalability
  source: operator
  stimulus: provisions a new tenant
  environment: up to 100 tenants
  artifact: provisioning
  response: tenant usable
  response_measure: automated; ≤ 1 hour; no code or schema change
  workload: —
  priority: M/M
  origin: W1 Q6
  refines: *id001
- id: QAS-SCAL-004
  quality: scalability
  source: time
  stimulus: observations grow to 1e9
  environment: design data volume
  artifact: observation store
  response: time-bounded queries keep targets
  response_measure: QAS-PERF-002 holds for queries with a time window ≤ 30 days
  workload: WL-01
  priority: M/H
  origin: W1 Q11
  refines: *id001
- id: QAS-SCAL-005
  quality: scalability
  source: noisy tenant
  stimulus: exceeds its quota by 10×
  environment: shared cell
  artifact: quota / rate limiter
  response: other tenants unaffected
  response_measure: other tenants stay within QAS-PERF-001
  workload: —
  priority: H/M
  origin: SR-07
  refines: *id001
- id: QAS-AVL-001
  quality: availability
  source: any
  stimulus: normal operation over a month
  environment: production
  artifact: critical tier capabilities
  response: service available
  response_measure: ≥ 99.9 % monthly
  workload: —
  priority: H/H
  origin: W1 Q21
  refines: &id002
  - BRQ-002
  - BRQ-004
- id: QAS-AVL-002
  quality: availability
  source: any
  stimulus: normal operation over a month
  environment: production
  artifact: important tier capabilities
  response: service available
  response_measure: ≥ 99.5 % monthly
  workload: —
  priority: M/M
  origin: W1 Q21
  refines: *id002
- id: QAS-AVL-003
  quality: availability
  source: any
  stimulus: normal operation over a month
  environment: production
  artifact: standard tier capabilities
  response: service available
  response_measure: ≥ 99 % monthly
  workload: —
  priority: L/L
  origin: W1 Q21
  refines: *id002
- id: QAS-REC-001
  quality: recoverability
  source: disaster
  stimulus: primary site lost
  environment: production
  artifact: critical tier
  response: restored
  response_measure: RPO ≤ 5 min; RTO ≤ 1 h
  workload: —
  priority: H/H
  origin: W1 Q21
  refines: &id003
  - BRQ-002
  - BRQ-004
- id: QAS-REC-002
  quality: recoverability
  source: disaster
  stimulus: primary site lost
  environment: production
  artifact: important tier
  response: restored
  response_measure: RPO ≤ 15 min; RTO ≤ 4 h
  workload: —
  priority: M/M
  origin: W1 Q21
  refines: *id003
- id: QAS-REC-003
  quality: recoverability
  source: disaster
  stimulus: primary site lost
  environment: production
  artifact: standard tier
  response: restored
  response_measure: RPO ≤ 24 h; RTO ≤ 24 h
  workload: —
  priority: L/L
  origin: W1 Q21
  refines: *id003
- id: QAS-REL-001
  quality: reliability
  source: infrastructure
  stimulus: event bus unavailable for 30 min
  environment: normal load
  artifact: outbox publisher
  response: commands keep succeeding; events published after recovery
  response_measure: 0 lost events; 0 duplicates with effect
  workload: WL-06
  priority: H/M
  origin: PRJ§106
  refines: &id004
  - BRQ-006
  - BRQ-007
- id: QAS-REL-002
  quality: resilience
  source: infrastructure
  stimulus: search projection unavailable
  environment: normal load
  artifact: platform
  response: commands, direct reads and maps keep working; search shows degraded state
  response_measure: critical tier unaffected; index rebuilt without data loss
  workload: WL-02
  priority: M/M
  origin: PRJ§107
  refines: *id004
- id: QAS-REL-003
  quality: integrity
  source: two users
  stimulus: update the same object from the same version
  environment: concurrent
  artifact: any aggregate
  response: second update rejected
  response_measure: 0 silent overwrites
  workload: WL-01
  priority: H/L
  origin: PRJ§104
  refines: *id004
- id: QAS-SEC-001
  quality: security
  source: authenticated user of tenant A
  stimulus: attempts to access tenant B data by any path
  environment: normal
  artifact: all access paths
  response: access denied and audited
  response_measure: 0 leaks in tenant-isolation suite
  workload: —
  priority: H/H
  origin: W1 Q6
  refines: &id005
  - BRQ-007
- id: QAS-SEC-002
  quality: security
  source: authenticated user without clearance
  stimulus: searches, lists, maps or receives alerts touching objects above clearance
  environment: normal
  artifact: search, lists, maps, alerts, notifications
  response: no disclosure of content or existence
  response_measure: 0 leakage in inference suite (counts, facets, ordering, timing, errors)
  workload: WL-02
  priority: H/H
  origin: BRL-010; A21
  refines: *id005
- id: QAS-SEC-003
  quality: security
  source: security officer
  stimulus: removes a user's compartment
  environment: normal
  artifact: all access paths
  response: object no longer returned to that user
  response_measure: effective on next request in every path, independent of index lag
  workload: —
  priority: H/H
  origin: W1 Q16
  refines: *id005
- id: QAS-SEC-004
  quality: security
  source: two users with different compartments
  stimulus: request the same map tile
  environment: normal
  artifact: tile cache
  response: each receives only authorized content
  response_measure: 0 cross-scope cache hits
  workload: WL-03
  priority: H/M
  origin: ADR-P06
  refines: *id005
- id: QAS-SEC-005
  quality: security
  source: fault
  stimulus: policy engine unavailable
  environment: normal
  artifact: authorization
  response: requests denied
  response_measure: 100 % fail-closed
  workload: —
  priority: H/L
  origin: SL-28
  refines: *id005
- id: QAS-SEC-006
  quality: security
  source: insider
  stimulus: modifies an audit record in storage
  environment: production
  artifact: audit store
  response: tampering detected
  response_measure: detected by next integrity check (≤ 24 h)
  workload: —
  priority: H/M
  origin: PRJ§3.4
  refines: *id005
- id: QAS-SEC-007
  quality: security
  source: thief
  stimulus: obtains a field device
  environment: device powered off or locked
  artifact: mobile app storage
  response: data unreadable
  response_measure: 0 readable records without authentication; wipe on next connection
  workload: WL-12
  priority: H/M
  origin: W1 Q9
  refines: *id005
- id: QAS-PRV-001
  quality: privacy
  source: data protection officer
  stimulus: orders erasure of a data subject
  environment: production
  artifact: all stores and backups
  response: personal data unrecoverable, audit facts kept
  response_measure: operational & projections ≤ 24 h; backups unrecoverable immediately via key destruction
  workload: —
  priority: H/H
  origin: W1 Q18
  refines:
  - BRQ-007
- id: QAS-OFF-001
  quality: offline
  source: field user
  stimulus: works 72 h offline then reconnects on a 1 Mbps link
  environment: field
  artifact: sync
  response: all changes synchronized; conflicts routed to review
  response_measure: 1,000 queued commands synced ≤ 10 min; 0 silent overwrites; 0 duplicates
  workload: WL-12
  priority: H/H
  origin: W1 Q9
  refines:
  - BRQ-001
- id: QAS-DQ-001
  quality: data quality
  source: adapter
  stimulus: submits records with invalid geometry or missing CRS
  environment: normal
  artifact: ingestion
  response: records quarantined with reason
  response_measure: 100 % of invalid records quarantined; 0 published
  workload: WL-15
  priority: H/L
  origin: REQ-INF-006
  refines:
  - BRQ-008
- id: QAS-TMP-001
  quality: correctness
  source: analyst
  stimulus: asks for state as of valid time T known at record time K
  environment: normal
  artifact: temporal query
  response: correct historical state
  response_measure: 100 % agreement with temporal oracle corpus
  workload: WL-04
  priority: H/H
  origin: W1 Q13
  refines:
  - BRQ-006
- id: QAS-AUD-001
  quality: auditability
  source: any actor
  stimulus: executes a state-changing command
  environment: normal
  artifact: audit
  response: audit record written
  response_measure: 100 % of commands audited with all fields
  workload: —
  priority: H/L
  origin: BRL-015
  refines:
  - BRQ-007
- id: QAS-TRC-001
  quality: traceability
  source: auditor
  stimulus: follows a decision back to its sources
  environment: normal
  artifact: lineage / provenance
  response: complete path returned
  response_measure: 100 % of decisions and T1 derived objects traceable to sources
  workload: —
  priority: H/M
  origin: OUT-03, OUT-04
  refines: &id006
  - BRQ-006
- id: QAS-TRC-002
  quality: reproducibility
  source: analyst
  stimulus: re-executes a recorded deterministic analysis run
  environment: normal
  artifact: analysis
  response: identical results
  response_measure: 100 %
  workload: WL-11
  priority: M/M
  origin: OUT-03
  refines: *id006
- id: QAS-USA-001
  quality: usability
  source: field user
  stimulus: records an observation with one photo on the mobile app
  environment: field, one hand
  artifact: mobile app
  response: observation saved
  response_measure: median ≤ 60 s in usability test with 10 field users
  workload: WL-12
  priority: M/M
  origin: W2 delegated target
  refines: &id007
  - BRQ-001
- id: QAS-USA-002
  quality: usability
  source: analyst
  stimulus: searches a name with Arabic spelling variants or Latin transliteration
  environment: normal
  artifact: search
  response: same entity found
  response_measure: recall ≥ 95 % on the Arabic name test set
  workload: WL-02
  priority: H/H
  origin: W1 Q15
  refines: *id007
- id: QAS-ACC-001
  quality: accessibility
  source: user with assistive technology
  stimulus: uses R1 web screens
  environment: normal
  artifact: web UI
  response: tasks completable
  response_measure: WCAG 2.2 level AA conformance (AR and EN)
  workload: —
  priority: M/M
  origin: W2 delegated decision (closes UNK-016)
  refines:
  - BRQ-001
- id: QAS-EVO-001
  quality: evolvability
  source: developer
  stimulus: changes an API or event contract
  environment: CI
  artifact: contracts
  response: breaking change blocked unless new major version
  response_measure: previous major version supported ≥ 6 months after successor
  workload: —
  priority: M/L
  origin: PRJ§97
  refines:
  - BRQ-008
- id: QAS-OPS-001
  quality: operability
  source: operator
  stimulus: installs or upgrades in an air-gapped site
  environment: no internet
  artifact: platform
  response: install / upgrade completes; rollback possible
  response_measure: offline bundle only; rollback ≤ 1 h
  workload: —
  priority: H/M
  origin: W1 Q20
  refines:
  - BRQ-007
- id: QAS-OBS-001
  quality: observability
  source: operator
  stimulus: investigates a failed request
  environment: production
  artifact: all components
  response: full trace found by correlation id
  response_measure: 100 % of requests traceable end to end
  workload: —
  priority: M/M
  origin: PRJ§26
  refines:
  - BRQ-007
- id: QAS-COST-001
  quality: cost
  source: finance
  stimulus: requests monthly cost per tenant
  environment: production
  artifact: telemetry
  response: report produced
  response_measure: computed from telemetry with no manual input
  workload: —
  priority: M/M
  origin: W1 Q29
  refines:
  - BRQ-007
- id: QAS-PERF-009
  quality: performance
  source: system
  stimulus: PEP requests a policy decision
  environment: 10,000 decisions/s
  artifact: SLC-01
  response: as measured
  response_measure: p95 ≤ 5 ms with embedded evaluator; ≤ 20 ms remote
  workload: WL-01
  priority: H/M
  origin: SLC-01 W5 delegated
  refines:
  - BRQ-007
- id: QAS-PERF-010
  quality: performance
  source: system
  stimulus: gateway resolves SecurityContext
  environment: 7,500 req/s peak
  artifact: SLC-01
  response: as measured
  response_measure: p95 ≤ 20 ms (cache hit p95 ≤ 2 ms)
  workload: WL-01
  priority: H/M
  origin: SLC-01 W5 delegated
  refines:
  - BRQ-007
- id: QAS-PERF-011
  quality: performance
  source: system
  stimulus: a command commits
  environment: normal
  artifact: SLC-01
  response: as measured
  response_measure: audit record in BC08 store ≤ 5 s p95; anchor ≤ 5 min
  workload: WL-01
  priority: H/M
  origin: SLC-01 W5 delegated
  refines:
  - BRQ-007
- id: QAS-SEC-008
  quality: security
  source: system
  stimulus: user disabled via SCIM
  environment: normal
  artifact: SLC-01
  response: as measured
  response_measure: next request from any session denied; SCIM-to-effect ≤ 5 min (REQ-FND-005)
  workload: WL-01
  priority: H/M
  origin: SLC-01 W5 delegated
  refines:
  - BRQ-007
- id: QAS-PERF-012
  quality: performance
  source: user/system
  stimulus: batch of 1,000 observations
  environment: 5,000 obs/s sustained per cell
  artifact: SLC-02
  response: as measured
  response_measure: batch commit p95 ≤ 1 s; 0 duplicates on retry
  workload: WL-01/06
  priority: H/M
  origin: SLC-02 W5 delegated
  refines:
  - BRQ-001
- id: QAS-PERF-013
  quality: performance
  source: user/system
  stimulus: resolved entity read (current)
  environment: 750 reads/s; 1e8 claims
  artifact: SLC-02
  response: as measured
  response_measure: p95 ≤ 300 ms end-to-end
  workload: WL-01/06
  priority: H/M
  origin: SLC-02 W5 delegated
  refines:
  - BRQ-002
- id: QAS-PERF-014
  quality: performance
  source: user/system
  stimulus: lineage trace depth 5
  environment: normal
  artifact: SLC-02
  response: as measured
  response_measure: p95 ≤ 2 s
  workload: WL-01/06
  priority: H/M
  origin: SLC-02 W5 delegated
  refines:
  - BRQ-006
- id: QAS-SEC-009
  quality: security
  source: user/system
  stimulus: user without source-protection permission reads claims of a protected human source
  environment: normal
  artifact: SLC-02
  response: as measured
  response_measure: 0 identity attributes disclosed in any response, export or lineage
  workload: WL-01/06
  priority: H/M
  origin: SLC-02 W5 delegated
  refines:
  - BRQ-007
- id: QAS-SEC-010
  quality: security
  source: user/system
  stimulus: user sees an entity but not some of its claims
  environment: normal
  artifact: SLC-02
  response: as measured
  response_measure: hidden claims affect neither status, counts, completeness nor timing (inference suite)
  workload: WL-01/06
  priority: H/M
  origin: SLC-02 W5 delegated
  refines:
  - BRQ-007
- id: QAS-ER-001
  quality: accuracy
  source: system/analyst
  stimulus: candidate recall on labelled AR/EN test set
  environment: ruleset evaluation
  artifact: SLC-04
  response: as measured
  response_measure: ≥ 95 % of true matches proposed
  workload: WL-08
  priority: H/M
  origin: SLC-04 W5 delegated
  refines:
  - BRQ-001
- id: QAS-ER-002
  quality: usability
  source: system/analyst
  stimulus: precision of proposals in review queue
  environment: ruleset evaluation
  artifact: SLC-04
  response: as measured
  response_measure: ≥ 60 % of proposals are true matches
  workload: WL-08
  priority: H/M
  origin: SLC-04 W5 delegated
  refines:
  - BRQ-001
- id: QAS-ER-003
  quality: performance
  source: system/analyst
  stimulus: new entity registered
  environment: normal load
  artifact: SLC-04
  response: as measured
  response_measure: candidates visible p95 ≤ 60 s
  workload: WL-08
  priority: H/M
  origin: SLC-04 W5 delegated
  refines:
  - BRQ-001
- id: QAS-CNF-001
  quality: performance
  source: system/analyst
  stimulus: incompatible claim committed
  environment: normal load
  artifact: SLC-04
  response: as measured
  response_measure: conflict opened p95 ≤ 30 s
  workload: WL-08
  priority: H/M
  origin: SLC-04 W5 delegated
  refines:
  - BRQ-006
- id: QAS-PERF-015
  quality: performance
  source: system/analyst
  stimulus: resolved read of clustered entity
  environment: 750 reads/s
  artifact: SLC-04
  response: as measured
  response_measure: ≤ 20 % overhead vs unclustered; p95 ≤ 300 ms
  workload: WL-08
  priority: H/M
  origin: SLC-04 W5 delegated
  refines:
  - BRQ-002
- id: QAS-PERF-016
  quality: performance
  source: user/system
  stimulus: field user opens 'my tasks'
  environment: design load
  artifact: SLC-03
  response: as measured
  response_measure: p95 ≤ 500 ms
  workload: WL-01
  priority: H/M
  origin: SLC-03 W5 delegated
  refines:
  - BRQ-004
- id: QAS-OPS-002
  quality: timeliness
  source: user/system
  stimulus: task reaches due_at
  environment: normal
  artifact: SLC-03
  response: as measured
  response_measure: escalation event ≤ 60 s after due
  workload: WL-01
  priority: H/M
  origin: SLC-03 W5 delegated
  refines:
  - BRQ-004
- id: QAS-PERF-017
  quality: performance
  source: user/system
  stimulus: assignment with eligibility check
  environment: normal
  artifact: SLC-03
  response: as measured
  response_measure: p95 ≤ 500 ms including BC05 call
  workload: WL-01
  priority: H/M
  origin: SLC-03 W5 delegated
  refines:
  - BRQ-004
- id: QAS-SEC-011
  quality: security
  source: user/operator
  stimulus: inference test suite on search, suggestions, facets, graph and paths
  environment: normal
  artifact: SLC-05
  response: as measured
  response_measure: 0 disclosures of hidden objects, hidden facts, hidden nodes/edges
  workload: WL-02
  priority: H/H
  origin: SLC-05 W5 delegated
  refines:
  - BRQ-007
- id: QAS-PERF-018
  quality: performance
  source: user/operator
  stimulus: graph neighborhood depth 2
  environment: design load, dense nodes
  artifact: SLC-05
  response: as measured
  response_measure: p95 ≤ 1 s
  workload: WL-02
  priority: H/H
  origin: SLC-05 W5 delegated
  refines:
  - BRQ-002
- id: QAS-REL-004
  quality: recoverability
  source: user/operator
  stimulus: full projection rebuild
  environment: design volume
  artifact: SLC-05
  response: as measured
  response_measure: ≤ 24 h to READY with no loss of query service (old version stays ACTIVE)
  workload: WL-02
  priority: H/H
  origin: SLC-05 W5 delegated
  refines:
  - BRQ-006
- id: QAS-PERF-019
  quality: performance
  source: user/system
  stimulus: situation picture read (≤ 2,000 visible members)
  environment: design load
  artifact: SLC-06
  response: as measured
  response_measure: p95 ≤ 1 s
  workload: WL-06
  priority: H/M
  origin: SLC-06 W5 delegated
  refines:
  - BRQ-002
- id: QAS-SEC-012
  quality: security
  source: user/system
  stimulus: user not cleared for an alert's label
  environment: normal
  artifact: SLC-06
  response: as measured
  response_measure: receives no alert, notification, push or count change
  workload: WL-06
  priority: H/M
  origin: SLC-06 W5 delegated
  refines:
  - BRQ-007
- id: QAS-OPS-003
  quality: operability
  source: user/system
  stimulus: push gateway unavailable (air-gapped)
  environment: field network
  artifact: SLC-06
  response: as measured
  response_measure: in-app inbox current; polling fallback ≤ 60 s
  workload: WL-06
  priority: H/M
  origin: SLC-06 W5 delegated
  refines:
  - BRQ-004
- id: QAS-PERF-020
  quality: fairness
  source: analyst
  stimulus: tenant submits 100 runs
  environment: shared compute pool
  artifact: SLC-07
  response: as measured
  response_measure: no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s
  workload: WL-11
  priority: H/M
  origin: SLC-07 W5 delegated
  refines:
  - BRQ-003
- id: QAS-SEC-013
  quality: security
  source: analyst
  stimulus: run submitted by user U
  environment: normal
  artifact: SLC-07
  response: as measured
  response_measure: run reads only data visible to U; results labelled ≥ max input label
  workload: WL-11
  priority: H/M
  origin: SLC-07 W5 delegated
  refines:
  - BRQ-007
- id: QAS-PERF-021
  quality: performance
  source: planner/auditor
  stimulus: plan version baselined with 500 task-generating activities
  environment: normal
  artifact: SLC-08
  response: as measured
  response_measure: task synchronization completes ≤ 60 s; idempotent on retry
  workload: WL-01
  priority: H/M
  origin: SLC-08 W5 delegated
  refines:
  - BRQ-004
- id: QAS-TRC-003
  quality: traceability
  source: planner/auditor
  stimulus: auditor asks for a decision's basis
  environment: normal
  artifact: SLC-08
  response: as measured
  response_measure: authority chain, pinned citations and claims as known at decision time returned; 100 % of decisions
  workload: WL-01
  priority: H/M
  origin: SLC-08 W5 delegated
  refines:
  - BRQ-003
- id: QAS-OFF-002
  quality: security
  source: field
  stimulus: user's clearance reduced while device offline
  environment: reconnect
  artifact: SLC-11
  response: as measured
  response_measure: packages revoked and purged on next contact; commands evaluated under current authorization
  workload: WL-12
  priority: H/H
  origin: SLC-11 W5 delegated
  refines:
  - BRQ-007
- id: QAS-OFF-003
  quality: scalability
  source: field
  stimulus: 5,000 devices reconnect within 10 min
  environment: morning shift start
  artifact: SLC-11
  response: as measured
  response_measure: all sessions complete ≤ 30 min; oldest-offline devices first; no data loss
  workload: WL-12
  priority: H/H
  origin: SLC-11 W5 delegated
  refines:
  - BRQ-001
- id: QAS-PRV-002
  quality: privacy
  source: operator/legal
  stimulus: restore of a key-store backup older than a key destruction
  environment: DR drill
  artifact: SLC-12a
  response: as measured
  response_measure: destroyed keys unusable before any service reads data (restore gate)
  workload: WL-14
  priority: H/H
  origin: SLC-12a W5 delegated
  refines:
  - BRQ-007
- id: QAS-GOV-001
  quality: compliance
  source: operator/legal
  stimulus: daily disposition evaluation
  environment: design volume
  artifact: SLC-12a
  response: as measured
  response_measure: candidates computed ≤ 1 h; 0 held records destroyed
  workload: WL-14
  priority: H/H
  origin: SLC-12a W5 delegated
  refines:
  - BRQ-007
- id: QAS-AI-001
  quality: AI quality
  source: user/system
  stimulus: evaluation set of 500 questions
  environment: citation accuracy
  artifact: R2
  response: as measured
  response_measure: ≥ 95 % of cited items actually support the statement
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-003
  release: R2
  requirement: REQ-AI-004
- id: QAS-AI-002
  quality: AI quality
  source: user/system
  stimulus: insufficient-evidence and hallucination sets
  environment: hallucination rate
  artifact: R2
  response: as measured
  response_measure: ≤ 2 % unsupported statements; ≥ 95 % correct 'Insufficient Evidence'
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-003
  release: R2
  requirement: REQ-AI-003
- id: QAS-AI-003
  quality: performance
  source: user/system
  stimulus: grounded Q&A request
  environment: design load (50 concurrent AI requests per cell)
  artifact: R2
  response: as measured
  response_measure: first token ≤ 3 s, full answer p95 ≤ 20 s on local models
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-003
  release: R2
  requirement: REQ-AI-001
- id: QAS-AI-004
  quality: security
  source: user/system
  stimulus: prompt-injection, exfiltration and unauthorized-retrieval suites
  environment: normal
  artifact: R2
  response: as measured
  response_measure: 0 unauthorized retrievals, 0 tool abuse, 0 cross-tenant leakage
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-003
  release: R2
  requirement: REQ-AI-002
- id: QAS-AI-005
  quality: cost
  source: user/system
  stimulus: AI usage per tenant
  environment: monthly
  artifact: R2
  response: as measured
  response_measure: GPU-hours and cost per request reported per tenant
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-003
  release: R2
  requirement: REQ-AI-001
- id: QAS-RES-001
  quality: integrity
  source: user/system
  stimulus: 100 concurrent allocation requests on one pool
  environment: normal
  artifact: R2
  response: as measured
  response_measure: 0 over-commitment; deterministic priority order
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-004
  release: R2
  requirement: REQ-RES-008
- id: QAS-RES-002
  quality: performance
  source: user/system
  stimulus: availability query for 1,000 assets over 30 days
  environment: normal
  artifact: R2
  response: as measured
  response_measure: p95 ≤ 1 s
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-004
  release: R2
  requirement: REQ-RES-006
- id: QAS-PRD-001
  quality: performance
  source: user/system
  stimulus: generate a 30-page product with 10 maps
  environment: normal
  artifact: R2
  response: as measured
  response_measure: ≤ 2 min (async job)
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-001
  release: R2
  requirement: REQ-PRD-001
- id: QAS-PRD-002
  quality: security
  source: user/system
  stimulus: product rendered for an audience
  environment: normal
  artifact: R2
  response: as measured
  response_measure: 0 content above the product label (inference suite on products)
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-001
  release: R2
  requirement: REQ-PRD-002
- id: QAS-ARC-001
  quality: performance
  source: user/system
  stimulus: retrieve an archived record
  environment: archive tier
  artifact: R2
  response: as measured
  response_measure: ≤ 1 min for warm, ≤ 24 h for cold/offline media
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-005
  release: R2
  requirement: REQ-ARC-003
- id: QAS-ARC-002
  quality: correctness
  source: user/system
  stimulus: historical reconstruction scenarios
  environment: normal
  artifact: R2
  response: as measured
  response_measure: 100 % agreement with oracle; every element labelled
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-005
  release: R2
  requirement: REQ-ARC-004
- id: QAS-ARC-003
  quality: integrity
  source: user/system
  stimulus: yearly archive integrity verification
  environment: archive
  artifact: R2
  response: as measured
  response_measure: 0 unreported corruption; repair from replica
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-005
  release: R2
  requirement: REQ-ARC-002
- id: QAS-KNW-001
  quality: usability
  source: user/system
  stimulus: planner creates a plan for a known task type
  environment: normal
  artifact: R2
  response: as measured
  response_measure: relevant published lessons suggested in ≥ 80 % of cases in pilot
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-005
  release: R2
  requirement: REQ-KNW-003
- id: QAS-COL-001
  quality: traceability
  source: user/system
  stimulus: collection requirement fulfilment
  environment: normal
  artifact: R2
  response: as measured
  response_measure: 100 % of fulfilment links traceable to validated observations
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-001
  release: R2
  requirement: REQ-COL-003
- id: QAS-INT-001
  quality: reliability
  source: user/system
  stimulus: ERP adapter outage 4 h
  environment: normal
  artifact: R2
  response: as measured
  response_measure: no data loss; backlog processed ≤ 1 h after recovery
  workload: R2
  priority: H/M
  origin: W2-R2 delegated
  refines:
  - BRQ-001
  release: R2
  requirement: REQ-INT-001
- id: QAS-RCM-001
  quality: performance
  source: user/system
  stimulus: CRISIS-severity incident assessed
  environment: normal
  artifact: R3
  response: as measured
  response_measure: 'response dispatched within the severity''s SLA (tagged: recalibrate after Pilot R1 and R2 — RSK-028)'
  workload: R3
  priority: H/M
  origin: W1/W2-R3 delegated
  refines:
  - BRQ-004
  release: R3
  requirement: REQ-RCM-009
- id: QAS-RCM-002
  quality: governance
  source: user/system
  stimulus: risk moved to treated status
  environment: normal
  artifact: R3
  response: as measured
  response_measure: 100 % of treated risks have ≥ 1 treatment action or an explicit, authorized accept decision
  workload: R3
  priority: H/M
  origin: W1/W2-R3 delegated
  refines:
  - BRQ-003
  release: R3
  requirement: REQ-RCM-004
- id: QAS-LOG-001
  quality: integrity
  source: user/system
  stimulus: concurrent logistics requests and task/plan allocations on the same resource pool
  environment: normal
  artifact: R3
  response: as measured
  response_measure: 0 over-commitment across combined demand; deterministic priority order (shared mechanism with QAS-RES-001)
  workload: R3
  priority: H/M
  origin: W1/W2-R3 delegated
  refines:
  - BRQ-004
  release: R3
  requirement: REQ-LOG-002
- id: QAS-LOG-002
  quality: performance
  source: user/system
  stimulus: shipment dispatched to its destination
  environment: normal
  artifact: R3
  response: as measured
  response_measure: 'transit duration within target (tagged: recalibrate after Pilot R1 and R2 — RSK-028)'
  workload: R3
  priority: H/M
  origin: W1/W2-R3 delegated
  refines:
  - BRQ-004
  release: R3
  requirement: REQ-LOG-004
- id: QAS-TRX-001
  quality: integrity
  source: user/system
  stimulus: a simulation run nears completion (CMD-SIM-COMPLETE sent) with at least one exercise participant still unevaluated
  environment: normal
  artifact: R3
  response: as measured
  response_measure: 0 simulations reach COMPLETED with a participant lacking at least one recorded evaluation (INV-SIM-02)
  workload: R3
  priority: H/M
  origin: W1/W2-R3 delegated
  refines:
  - BRQ-005
  release: R3
  requirement: REQ-TRX-010
- id: QAS-TRX-002
  quality: performance
  source: user/system
  stimulus: an inject delivered during a live simulation run
  environment: normal
  artifact: R3
  response: as measured
  response_measure: 'inject delivery recorded within target latency (tagged: recalibrate after Pilot R1 and R2 — RSK-028)'
  workload: R3
  priority: H/M
  origin: W1/W2-R3 delegated
  refines:
  - BRQ-004
  release: R3
  requirement: REQ-TRX-008
```

</details>
