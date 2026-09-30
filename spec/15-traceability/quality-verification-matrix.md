---
id: QUALITY-MATRIX
type: traceability-matrix
title: 'Quality Verification Matrix — every QAS → verification method and timing (V5 #104)'
wave: W9
status: GENERATED
notes: فحص W9 وجد 19 سيناريو جودة بلا مرجع تحقق صريح؛ هذا الجدول يغطي كل السيناريوهات الـ 74.
---

# Quality Verification Matrix — every QAS → verification method and timing (V5 #104)

> فحص W9 وجد 19 سيناريو جودة بلا مرجع تحقق صريح؛ هذا الجدول يغطي كل السيناريوهات الـ 74.

## scenarios

_91 items_

| qas | quality | measure | verification | when | workload |
|---|---|---|---|---|---|
| QAS-PERF-001 | performance | p95 ≤ 300 ms; p99 ≤ 1 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01 |
| QAS-PERF-002 | performance | single object p95 ≤ 300 ms; list page p95 ≤ 1 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01 |
| QAS-PERF-003 | performance | p95 ≤ 1 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-02 |
| QAS-PERF-004 | performance | index lag p95 ≤ 30 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-02 |
| QAS-PERF-005 | performance | end-to-end p95 ≤ 5 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-06 |
| QAS-PERF-006 | performance | p95 ≤ 10 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-06 |
| QAS-PERF-007 | performance | tile p95 ≤ 500 ms | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-03 |
| QAS-PERF-008 | performance | p95 ≤ 30 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-02 |
| QAS-SCAL-001 | scalability | 0 architectural or schema changes needed | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01 |
| QAS-SCAL-002 | scalability | 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PERF-005 ≤ 5 min after | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-06 |
| QAS-SCAL-003 | scalability | automated; ≤ 1 hour; no code or schema change | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | — |
| QAS-SCAL-004 | scalability | QAS-PERF-002 holds for queries with a time window ≤ 30 days | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01 |
| QAS-SCAL-005 | scalability | other tenants stay within QAS-PERF-001 | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | — |
| QAS-AVL-001 | availability | ≥ 99.9 % monthly | availability SLO monitoring over pilot + chaos tests | pilot (monthly) | — |
| QAS-AVL-002 | availability | ≥ 99.5 % monthly | availability SLO monitoring over pilot + chaos tests | pilot (monthly) | — |
| QAS-AVL-003 | availability | ≥ 99 % monthly | availability SLO monitoring over pilot + chaos tests | pilot (monthly) | — |
| QAS-REC-001 | recoverability | RPO ≤ 5 min; RTO ≤ 1 h | DR drill: restore within RPO/RTO per tier (DR-CONTINUITY §2) | pre-G8, quarterly | — |
| QAS-REC-002 | recoverability | RPO ≤ 15 min; RTO ≤ 4 h | DR drill: restore within RPO/RTO per tier (DR-CONTINUITY §2) | pre-G8, quarterly | — |
| QAS-REC-003 | recoverability | RPO ≤ 24 h; RTO ≤ 24 h | DR drill: restore within RPO/RTO per tier (DR-CONTINUITY §2) | pre-G8, quarterly | — |
| QAS-REL-001 | reliability | 0 lost events; 0 duplicates with effect | fault-injection / chaos test (FMEA scenarios) | CI nightly + pre-G7 | WL-06 |
| QAS-REL-002 | resilience | critical tier unaffected; index rebuilt without data loss | fault-injection / chaos test (FMEA scenarios) | CI nightly + pre-G7 | WL-02 |
| QAS-REL-003 | integrity | 0 silent overwrites | fault-injection / chaos test (FMEA scenarios) | CI nightly + pre-G7 | WL-01 |
| QAS-SEC-001 | security | 0 leaks in tenant-isolation suite | security acceptance + inference suite + penetration test | CI + pre-G8 | — |
| QAS-SEC-002 | security | 0 leakage in inference suite (counts, facets, ordering, timing, errors) | security acceptance + inference suite + penetration test | CI + pre-G8 | WL-02 |
| QAS-SEC-003 | security | effective on next request in every path, independent of index lag | security acceptance + inference suite + penetration test | CI + pre-G8 | — |
| QAS-SEC-004 | security | 0 cross-scope cache hits | security acceptance + inference suite + penetration test | CI + pre-G8 | WL-03 |
| QAS-SEC-005 | security | 100 % fail-closed | security acceptance + inference suite + penetration test | CI + pre-G8 | — |
| QAS-SEC-006 | security | detected by next integrity check (≤ 24 h) | security acceptance + inference suite + penetration test | CI + pre-G8 | — |
| QAS-SEC-007 | security | 0 readable records without authentication; wipe on next connection | security acceptance + inference suite + penetration test | CI + pre-G8 | WL-12 |
| QAS-PRV-001 | privacy | operational & projections ≤ 24 h; backups unrecoverable immediately via key destruction | erasure drill incl. backup restore gate (FIT-19) | pre-G8, quarterly | — |
| QAS-OFF-001 | offline | 1,000 queued commands synced ≤ 10 min; 0 silent overwrites; 0 duplicates | field sync tests with interruption injection + device tests | CI + field pilot | WL-12 |
| QAS-DQ-001 | data quality | 100 % of invalid records quarantined; 0 published | ingestion acceptance (quarantine) | CI | WL-15 |
| QAS-TMP-001 | correctness | 100 % agreement with temporal oracle corpus | temporal oracle suite (500 cases) | CI | WL-04 |
| QAS-AUD-001 | auditability | 100 % of commands audited with all fields | audit completeness check in e2e suite | CI | — |
| QAS-TRC-001 | traceability | 100 % of decisions and T1 derived objects traceable to sources | lineage / basis e2e tests | CI | — |
| QAS-TRC-002 | reproducibility | 100 % | lineage / basis e2e tests | CI | WL-11 |
| QAS-USA-001 | usability | median ≤ 60 s in usability test with 10 field users | usability test with 10 field users; Arabic name recall test set | pilot | WL-12 |
| QAS-USA-002 | usability | recall ≥ 95 % on the Arabic name test set | usability test with 10 field users; Arabic name recall test set | pilot | WL-02 |
| QAS-ACC-001 | accessibility | WCAG 2.2 level AA conformance (AR and EN) | WCAG 2.2 AA audit (automated + manual) | pre-G8 | — |
| QAS-EVO-001 | evolvability | previous major version supported ≥ 6 months after successor | contract compatibility check (FIT-14) | CI | — |
| QAS-OPS-001 | operability | offline bundle only; rollback ≤ 1 h | air-gapped install/upgrade/rollback rehearsal | pre-G8 | — |
| QAS-OBS-001 | observability | 100 % of requests traceable end to end | trace completeness sampling | pilot | — |
| QAS-COST-001 | cost | computed from telemetry with no manual input | monthly per-tenant cost report from OpenCost | pilot | — |
| QAS-PERF-009 | performance | p95 ≤ 5 ms with embedded evaluator; ≤ 20 ms remote | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01 |
| QAS-PERF-010 | performance | p95 ≤ 20 ms (cache hit p95 ≤ 2 ms) | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01 |
| QAS-PERF-011 | performance | audit record in BC08 store ≤ 5 s p95; anchor ≤ 5 min | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01 |
| QAS-SEC-008 | security | next request from any session denied; SCIM-to-effect ≤ 5 min (REQ-FND-005) | security acceptance + inference suite + penetration test | CI + pre-G8 | WL-01 |
| QAS-PERF-012 | performance | batch commit p95 ≤ 1 s; 0 duplicates on retry | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01/06 |
| QAS-PERF-013 | performance | p95 ≤ 300 ms end-to-end | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01/06 |
| QAS-PERF-014 | performance | p95 ≤ 2 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01/06 |
| QAS-SEC-009 | security | 0 identity attributes disclosed in any response, export or lineage | security acceptance + inference suite + penetration test | CI + pre-G8 | WL-01/06 |
| QAS-SEC-010 | security | hidden claims affect neither status, counts, completeness nor timing (inference suite) | security acceptance + inference suite + penetration test | CI + pre-G8 | WL-01/06 |
| QAS-ER-001 | accuracy | ≥ 95 % of true matches proposed | ruleset evaluation on labelled set; latency test | CI + pilot | WL-08 |
| QAS-ER-002 | usability | ≥ 60 % of proposals are true matches | ruleset evaluation on labelled set; latency test | CI + pilot | WL-08 |
| QAS-ER-003 | performance | candidates visible p95 ≤ 60 s | ruleset evaluation on labelled set; latency test | CI + pilot | WL-08 |
| QAS-CNF-001 | performance | conflict opened p95 ≤ 30 s | latency test | CI + pilot | WL-08 |
| QAS-PERF-015 | performance | ≤ 20 % overhead vs unclustered; p95 ≤ 300 ms | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-08 |
| QAS-PERF-016 | performance | p95 ≤ 500 ms | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01 |
| QAS-OPS-002 | timeliness | escalation event ≤ 60 s after due | air-gapped install/upgrade/rollback rehearsal | pre-G8 | WL-01 |
| QAS-PERF-017 | performance | p95 ≤ 500 ms including BC05 call | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01 |
| QAS-SEC-011 | security | 0 disclosures of hidden objects, hidden facts, hidden nodes/edges | security acceptance + inference suite + penetration test | CI + pre-G8 | WL-02 |
| QAS-PERF-018 | performance | p95 ≤ 1 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-02 |
| QAS-REL-004 | recoverability | ≤ 24 h to READY with no loss of query service (old version stays ACTIVE) | fault-injection / chaos test (FMEA scenarios) | CI nightly + pre-G7 | WL-02 |
| QAS-PERF-019 | performance | p95 ≤ 1 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-06 |
| QAS-SEC-012 | security | receives no alert, notification, push or count change | security acceptance + inference suite + penetration test | CI + pre-G8 | WL-06 |
| QAS-OPS-003 | operability | in-app inbox current; polling fallback ≤ 60 s | air-gapped install/upgrade/rollback rehearsal | pre-G8 | WL-06 |
| QAS-PERF-020 | fairness | no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-11 |
| QAS-SEC-013 | security | run reads only data visible to U; results labelled ≥ max input label | security acceptance + inference suite + penetration test | CI + pre-G8 | WL-11 |
| QAS-PERF-021 | performance | task synchronization completes ≤ 60 s; idempotent on retry | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot | WL-01 |
| QAS-TRC-003 | traceability | authority chain, pinned citations and claims as known at decision time returned; 100 % of decisions | lineage / basis e2e tests | CI | WL-01 |
| QAS-OFF-002 | security | packages revoked and purged on next contact; commands evaluated under current authorization | field sync tests with interruption injection + device tests | CI + field pilot | WL-12 |
| QAS-OFF-003 | scalability | all sessions complete ≤ 30 min; oldest-offline devices first; no data loss | field sync tests with interruption injection + device tests | CI + field pilot | WL-12 |
| QAS-PRV-002 | privacy | destroyed keys unusable before any service reads data (restore gate) | erasure drill incl. backup restore gate (FIT-19) | pre-G8, quarterly | WL-14 |
| QAS-GOV-001 | compliance | candidates computed ≤ 1 h; 0 held records destroyed | disposition run test at design volume | pre-G8 | WL-14 |
| QAS-AI-001 | AI quality | ≥ 95 % of cited items actually support the statement | AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111 | pre-G7-R2 + per model promotion (recalibrate after R1 pilot) | R2 |
| QAS-AI-002 | AI quality | ≤ 2 % unsupported statements; ≥ 95 % correct 'Insufficient Evidence' | AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111 | pre-G7-R2 + per model promotion (recalibrate after R1 pilot) | R2 |
| QAS-AI-003 | performance | first token ≤ 3 s, full answer p95 ≤ 20 s on local models | AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111 | pre-G7-R2 + per model promotion (recalibrate after R1 pilot) | R2 |
| QAS-AI-004 | security | 0 unauthorized retrievals, 0 tool abuse, 0 cross-tenant leakage | AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111 | pre-G7-R2 + per model promotion (recalibrate after R1 pilot) | R2 |
| QAS-AI-005 | cost | GPU-hours and cost per request reported per tenant | AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111 | pre-G7-R2 + per model promotion (recalibrate after R1 pilot) | R2 |
| QAS-RES-001 | integrity | 0 over-commitment; deterministic priority order | concurrency and availability tests | CI + pilot (recalibrate after R1 pilot) | R2 |
| QAS-RES-002 | performance | p95 ≤ 1 s | concurrency and availability tests | CI + pilot (recalibrate after R1 pilot) | R2 |
| QAS-PRD-001 | performance | ≤ 2 min (async job) | product generation + inference suite on products | CI (recalibrate after R1 pilot) | R2 |
| QAS-PRD-002 | security | 0 content above the product label (inference suite on products) | product generation + inference suite on products | CI (recalibrate after R1 pilot) | R2 |
| QAS-ARC-001 | performance | ≤ 1 min for warm, ≤ 24 h for cold/offline media | archive retrieval, reconstruction oracle, integrity verification | CI + yearly (recalibrate after R1 pilot) | R2 |
| QAS-ARC-002 | correctness | 100 % agreement with oracle; every element labelled | archive retrieval, reconstruction oracle, integrity verification | CI + yearly (recalibrate after R1 pilot) | R2 |
| QAS-ARC-003 | integrity | 0 unreported corruption; repair from replica | archive retrieval, reconstruction oracle, integrity verification | CI + yearly (recalibrate after R1 pilot) | R2 |
| QAS-KNW-001 | usability | relevant published lessons suggested in ≥ 80 % of cases in pilot | pilot usability measurement | pilot (recalibrate after R1 pilot) | R2 |
| QAS-COL-001 | traceability | 100 % of fulfilment links traceable to validated observations | lineage e2e tests | CI (recalibrate after R1 pilot) | R2 |
| QAS-INT-001 | reliability | no data loss; backlog processed ≤ 1 h after recovery | adapter outage/backlog test | pre-G8-R2 (recalibrate after R1 pilot) | R2 |
| QAS-RCM-001 | performance | response dispatched within the severity's SLA | incident dispatch latency test (TST-INCIDENT-SM + load harness) | CI + pilot (recalibrate after R1 and R2 pilot — RSK-028) | R3 |
| QAS-RCM-002 | governance | 100 % of treated risks have ≥ 1 treatment action or an explicit accept decision | TST-SLC17-INVARIANTS + registry audit query | CI (recalibrate after R1 and R2 pilot — RSK-028) | R3 |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
scenarios:
- qas: QAS-PERF-001
  quality: performance
  measure: p95 ≤ 300 ms; p99 ≤ 1 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01
- qas: QAS-PERF-002
  quality: performance
  measure: single object p95 ≤ 300 ms; list page p95 ≤ 1 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01
- qas: QAS-PERF-003
  quality: performance
  measure: p95 ≤ 1 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-02
- qas: QAS-PERF-004
  quality: performance
  measure: index lag p95 ≤ 30 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-02
- qas: QAS-PERF-005
  quality: performance
  measure: end-to-end p95 ≤ 5 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-06
- qas: QAS-PERF-006
  quality: performance
  measure: p95 ≤ 10 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-06
- qas: QAS-PERF-007
  quality: performance
  measure: tile p95 ≤ 500 ms
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-03
- qas: QAS-PERF-008
  quality: performance
  measure: p95 ≤ 30 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-02
- qas: QAS-SCAL-001
  quality: scalability
  measure: 0 architectural or schema changes needed
  verification: scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01
- qas: QAS-SCAL-002
  quality: scalability
  measure: 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PERF-005 ≤ 5 min after
  verification: scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-06
- qas: QAS-SCAL-003
  quality: scalability
  measure: automated; ≤ 1 hour; no code or schema change
  verification: scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: —
- qas: QAS-SCAL-004
  quality: scalability
  measure: QAS-PERF-002 holds for queries with a time window ≤ 30 days
  verification: scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01
- qas: QAS-SCAL-005
  quality: scalability
  measure: other tenants stay within QAS-PERF-001
  verification: scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: —
- qas: QAS-AVL-001
  quality: availability
  measure: ≥ 99.9 % monthly
  verification: availability SLO monitoring over pilot + chaos tests
  when: pilot (monthly)
  workload: —
- qas: QAS-AVL-002
  quality: availability
  measure: ≥ 99.5 % monthly
  verification: availability SLO monitoring over pilot + chaos tests
  when: pilot (monthly)
  workload: —
- qas: QAS-AVL-003
  quality: availability
  measure: ≥ 99 % monthly
  verification: availability SLO monitoring over pilot + chaos tests
  when: pilot (monthly)
  workload: —
- qas: QAS-REC-001
  quality: recoverability
  measure: RPO ≤ 5 min; RTO ≤ 1 h
  verification: 'DR drill: restore within RPO/RTO per tier (DR-CONTINUITY §2)'
  when: pre-G8, quarterly
  workload: —
- qas: QAS-REC-002
  quality: recoverability
  measure: RPO ≤ 15 min; RTO ≤ 4 h
  verification: 'DR drill: restore within RPO/RTO per tier (DR-CONTINUITY §2)'
  when: pre-G8, quarterly
  workload: —
- qas: QAS-REC-003
  quality: recoverability
  measure: RPO ≤ 24 h; RTO ≤ 24 h
  verification: 'DR drill: restore within RPO/RTO per tier (DR-CONTINUITY §2)'
  when: pre-G8, quarterly
  workload: —
- qas: QAS-REL-001
  quality: reliability
  measure: 0 lost events; 0 duplicates with effect
  verification: fault-injection / chaos test (FMEA scenarios)
  when: CI nightly + pre-G7
  workload: WL-06
- qas: QAS-REL-002
  quality: resilience
  measure: critical tier unaffected; index rebuilt without data loss
  verification: fault-injection / chaos test (FMEA scenarios)
  when: CI nightly + pre-G7
  workload: WL-02
- qas: QAS-REL-003
  quality: integrity
  measure: 0 silent overwrites
  verification: fault-injection / chaos test (FMEA scenarios)
  when: CI nightly + pre-G7
  workload: WL-01
- qas: QAS-SEC-001
  quality: security
  measure: 0 leaks in tenant-isolation suite
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: —
- qas: QAS-SEC-002
  quality: security
  measure: 0 leakage in inference suite (counts, facets, ordering, timing, errors)
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: WL-02
- qas: QAS-SEC-003
  quality: security
  measure: effective on next request in every path, independent of index lag
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: —
- qas: QAS-SEC-004
  quality: security
  measure: 0 cross-scope cache hits
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: WL-03
- qas: QAS-SEC-005
  quality: security
  measure: 100 % fail-closed
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: —
- qas: QAS-SEC-006
  quality: security
  measure: detected by next integrity check (≤ 24 h)
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: —
- qas: QAS-SEC-007
  quality: security
  measure: 0 readable records without authentication; wipe on next connection
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: WL-12
- qas: QAS-PRV-001
  quality: privacy
  measure: operational & projections ≤ 24 h; backups unrecoverable immediately via key destruction
  verification: erasure drill incl. backup restore gate (FIT-19)
  when: pre-G8, quarterly
  workload: —
- qas: QAS-OFF-001
  quality: offline
  measure: 1,000 queued commands synced ≤ 10 min; 0 silent overwrites; 0 duplicates
  verification: field sync tests with interruption injection + device tests
  when: CI + field pilot
  workload: WL-12
- qas: QAS-DQ-001
  quality: data quality
  measure: 100 % of invalid records quarantined; 0 published
  verification: ingestion acceptance (quarantine)
  when: CI
  workload: WL-15
- qas: QAS-TMP-001
  quality: correctness
  measure: 100 % agreement with temporal oracle corpus
  verification: temporal oracle suite (500 cases)
  when: CI
  workload: WL-04
- qas: QAS-AUD-001
  quality: auditability
  measure: 100 % of commands audited with all fields
  verification: audit completeness check in e2e suite
  when: CI
  workload: —
- qas: QAS-TRC-001
  quality: traceability
  measure: 100 % of decisions and T1 derived objects traceable to sources
  verification: lineage / basis e2e tests
  when: CI
  workload: —
- qas: QAS-TRC-002
  quality: reproducibility
  measure: 100 %
  verification: lineage / basis e2e tests
  when: CI
  workload: WL-11
- qas: QAS-USA-001
  quality: usability
  measure: median ≤ 60 s in usability test with 10 field users
  verification: usability test with 10 field users; Arabic name recall test set
  when: pilot
  workload: WL-12
- qas: QAS-USA-002
  quality: usability
  measure: recall ≥ 95 % on the Arabic name test set
  verification: usability test with 10 field users; Arabic name recall test set
  when: pilot
  workload: WL-02
- qas: QAS-ACC-001
  quality: accessibility
  measure: WCAG 2.2 level AA conformance (AR and EN)
  verification: WCAG 2.2 AA audit (automated + manual)
  when: pre-G8
  workload: —
- qas: QAS-EVO-001
  quality: evolvability
  measure: previous major version supported ≥ 6 months after successor
  verification: contract compatibility check (FIT-14)
  when: CI
  workload: —
- qas: QAS-OPS-001
  quality: operability
  measure: offline bundle only; rollback ≤ 1 h
  verification: air-gapped install/upgrade/rollback rehearsal
  when: pre-G8
  workload: —
- qas: QAS-OBS-001
  quality: observability
  measure: 100 % of requests traceable end to end
  verification: trace completeness sampling
  when: pilot
  workload: —
- qas: QAS-COST-001
  quality: cost
  measure: computed from telemetry with no manual input
  verification: monthly per-tenant cost report from OpenCost
  when: pilot
  workload: —
- qas: QAS-PERF-009
  quality: performance
  measure: p95 ≤ 5 ms with embedded evaluator; ≤ 20 ms remote
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01
- qas: QAS-PERF-010
  quality: performance
  measure: p95 ≤ 20 ms (cache hit p95 ≤ 2 ms)
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01
- qas: QAS-PERF-011
  quality: performance
  measure: audit record in BC08 store ≤ 5 s p95; anchor ≤ 5 min
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01
- qas: QAS-SEC-008
  quality: security
  measure: next request from any session denied; SCIM-to-effect ≤ 5 min (REQ-FND-005)
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: WL-01
- qas: QAS-PERF-012
  quality: performance
  measure: batch commit p95 ≤ 1 s; 0 duplicates on retry
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01/06
- qas: QAS-PERF-013
  quality: performance
  measure: p95 ≤ 300 ms end-to-end
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01/06
- qas: QAS-PERF-014
  quality: performance
  measure: p95 ≤ 2 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01/06
- qas: QAS-SEC-009
  quality: security
  measure: 0 identity attributes disclosed in any response, export or lineage
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: WL-01/06
- qas: QAS-SEC-010
  quality: security
  measure: hidden claims affect neither status, counts, completeness nor timing (inference suite)
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: WL-01/06
- qas: QAS-ER-001
  quality: accuracy
  measure: ≥ 95 % of true matches proposed
  verification: ruleset evaluation on labelled set; latency test
  when: CI + pilot
  workload: WL-08
- qas: QAS-ER-002
  quality: usability
  measure: ≥ 60 % of proposals are true matches
  verification: ruleset evaluation on labelled set; latency test
  when: CI + pilot
  workload: WL-08
- qas: QAS-ER-003
  quality: performance
  measure: candidates visible p95 ≤ 60 s
  verification: ruleset evaluation on labelled set; latency test
  when: CI + pilot
  workload: WL-08
- qas: QAS-CNF-001
  quality: performance
  measure: conflict opened p95 ≤ 30 s
  verification: latency test
  when: CI + pilot
  workload: WL-08
- qas: QAS-PERF-015
  quality: performance
  measure: ≤ 20 % overhead vs unclustered; p95 ≤ 300 ms
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-08
- qas: QAS-PERF-016
  quality: performance
  measure: p95 ≤ 500 ms
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01
- qas: QAS-OPS-002
  quality: timeliness
  measure: escalation event ≤ 60 s after due
  verification: air-gapped install/upgrade/rollback rehearsal
  when: pre-G8
  workload: WL-01
- qas: QAS-PERF-017
  quality: performance
  measure: p95 ≤ 500 ms including BC05 call
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01
- qas: QAS-SEC-011
  quality: security
  measure: 0 disclosures of hidden objects, hidden facts, hidden nodes/edges
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: WL-02
- qas: QAS-PERF-018
  quality: performance
  measure: p95 ≤ 1 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-02
- qas: QAS-REL-004
  quality: recoverability
  measure: ≤ 24 h to READY with no loss of query service (old version stays ACTIVE)
  verification: fault-injection / chaos test (FMEA scenarios)
  when: CI nightly + pre-G7
  workload: WL-02
- qas: QAS-PERF-019
  quality: performance
  measure: p95 ≤ 1 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-06
- qas: QAS-SEC-012
  quality: security
  measure: receives no alert, notification, push or count change
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: WL-06
- qas: QAS-OPS-003
  quality: operability
  measure: in-app inbox current; polling fallback ≤ 60 s
  verification: air-gapped install/upgrade/rollback rehearsal
  when: pre-G8
  workload: WL-06
- qas: QAS-PERF-020
  quality: fairness
  measure: no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-11
- qas: QAS-SEC-013
  quality: security
  measure: run reads only data visible to U; results labelled ≥ max input label
  verification: security acceptance + inference suite + penetration test
  when: CI + pre-G8
  workload: WL-11
- qas: QAS-PERF-021
  quality: performance
  measure: task synchronization completes ≤ 60 s; idempotent on retry
  verification: load test (PERF-TEST-STRATEGY §3)
  when: pre-G7 + pilot
  workload: WL-01
- qas: QAS-TRC-003
  quality: traceability
  measure: authority chain, pinned citations and claims as known at decision time returned; 100 % of decisions
  verification: lineage / basis e2e tests
  when: CI
  workload: WL-01
- qas: QAS-OFF-002
  quality: security
  measure: packages revoked and purged on next contact; commands evaluated under current authorization
  verification: field sync tests with interruption injection + device tests
  when: CI + field pilot
  workload: WL-12
- qas: QAS-OFF-003
  quality: scalability
  measure: all sessions complete ≤ 30 min; oldest-offline devices first; no data loss
  verification: field sync tests with interruption injection + device tests
  when: CI + field pilot
  workload: WL-12
- qas: QAS-PRV-002
  quality: privacy
  measure: destroyed keys unusable before any service reads data (restore gate)
  verification: erasure drill incl. backup restore gate (FIT-19)
  when: pre-G8, quarterly
  workload: WL-14
- qas: QAS-GOV-001
  quality: compliance
  measure: candidates computed ≤ 1 h; 0 held records destroyed
  verification: disposition run test at design volume
  when: pre-G8
  workload: WL-14
- qas: QAS-AI-001
  quality: AI quality
  measure: ≥ 95 % of cited items actually support the statement
  verification: AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111
  when: pre-G7-R2 + per model promotion (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-AI-002
  quality: AI quality
  measure: ≤ 2 % unsupported statements; ≥ 95 % correct 'Insufficient Evidence'
  verification: AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111
  when: pre-G7-R2 + per model promotion (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-AI-003
  quality: performance
  measure: first token ≤ 3 s, full answer p95 ≤ 20 s on local models
  verification: AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111
  when: pre-G7-R2 + per model promotion (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-AI-004
  quality: security
  measure: 0 unauthorized retrievals, 0 tool abuse, 0 cross-tenant leakage
  verification: AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111
  when: pre-G7-R2 + per model promotion (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-AI-005
  quality: cost
  measure: GPU-hours and cost per request reported per tenant
  verification: AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111
  when: pre-G7-R2 + per model promotion (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-RES-001
  quality: integrity
  measure: 0 over-commitment; deterministic priority order
  verification: concurrency and availability tests
  when: CI + pilot (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-RES-002
  quality: performance
  measure: p95 ≤ 1 s
  verification: concurrency and availability tests
  when: CI + pilot (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-PRD-001
  quality: performance
  measure: ≤ 2 min (async job)
  verification: product generation + inference suite on products
  when: CI (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-PRD-002
  quality: security
  measure: 0 content above the product label (inference suite on products)
  verification: product generation + inference suite on products
  when: CI (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-ARC-001
  quality: performance
  measure: ≤ 1 min for warm, ≤ 24 h for cold/offline media
  verification: archive retrieval, reconstruction oracle, integrity verification
  when: CI + yearly (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-ARC-002
  quality: correctness
  measure: 100 % agreement with oracle; every element labelled
  verification: archive retrieval, reconstruction oracle, integrity verification
  when: CI + yearly (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-ARC-003
  quality: integrity
  measure: 0 unreported corruption; repair from replica
  verification: archive retrieval, reconstruction oracle, integrity verification
  when: CI + yearly (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-KNW-001
  quality: usability
  measure: relevant published lessons suggested in ≥ 80 % of cases in pilot
  verification: pilot usability measurement
  when: pilot (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-COL-001
  quality: traceability
  measure: 100 % of fulfilment links traceable to validated observations
  verification: lineage e2e tests
  when: CI (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-INT-001
  quality: reliability
  measure: no data loss; backlog processed ≤ 1 h after recovery
  verification: adapter outage/backlog test
  when: pre-G8-R2 (recalibrate after R1 pilot)
  workload: R2
- qas: QAS-RCM-001
  quality: performance
  measure: response dispatched within the severity's SLA
  verification: incident dispatch latency test (TST-INCIDENT-SM + load harness)
  when: CI + pilot (recalibrate after R1 and R2 pilot — RSK-028)
  workload: R3
- qas: QAS-RCM-002
  quality: governance
  measure: 100 % of treated risks have ≥ 1 treatment action or an explicit accept decision
  verification: TST-SLC17-INVARIANTS + registry audit query
  when: CI (recalibrate after R1 and R2 pilot — RSK-028)
  workload: R3
```

</details>
