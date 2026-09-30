---
id: WL-SLC02
type: workload-catalog
title: Workloads & Added Quality Scenarios — SLC-02
wave: W5
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: اشتقاقات تقديرية (INF) تُعاد معايرتها في Pilot.
---

# Workloads & Added Quality Scenarios — SLC-02

> اشتقاقات تقديرية (INF) تُعاد معايرتها في Pilot.

## workloads

_7 items_

| id | name | derivation | basis | target |
|---|---|---|---|---|
| WL-06a | Observation ingestion (sensors + field + adapters) | design 5,000 obs/s sustained, 50,000/s burst 60 s (W1 Q11) | W1 targets | QAS-PERF-012, QAS-SCAL-002 |
| WL-01g | Claim assertions | ~10 % of observations yield derived claims after summarization + analyst/adapters ≈ 500/s sustained | INF | QAS-PERF-001 |
| WL-01h | Resolved entity reads | dominant read: ~30 % of 2,500 req/s ≈ 750/s | INF | QAS-PERF-013 |
| WL-04a | As-of / as-known-at reads | low frequency (audit, analysis) ≈ 5–20/s | INF | LIB §6 p95 ≤ 500 ms |
| WL-03a | Spatial list queries (bbox + time) | map panning ≈ 20 % of reads ≈ 500/s | INF | QAS-PERF-002 list ≤ 1 s |
| WL-05a | Attachments | design: 50 uploads/s avg, PB-class total; bytes bypass app tier | INF | object storage throughput; app tier only signs |
| WL-11a | Lineage traversal | ≈ 5/s, depth ≤ 10 | INF | QAS-PERF-014 |

## added_quality_scenarios

_5 items_

| id | quality | stimulus | environment | response_measure | refines |
|---|---|---|---|---|---|
| QAS-PERF-012 | performance | batch of 1,000 observations | 5,000 obs/s sustained per cell | batch commit p95 ≤ 1 s; 0 duplicates on retry | BRQ-001 |
| QAS-PERF-013 | performance | resolved entity read (current) | 750 reads/s; 1e8 claims | p95 ≤ 300 ms end-to-end | BRQ-002 |
| QAS-PERF-014 | performance | lineage trace depth 5 | normal | p95 ≤ 2 s | BRQ-006 |
| QAS-SEC-009 | security | user without source-protection permission reads claims of a protected human source | normal | 0 identity attributes disclosed in any response, export or lineage | BRQ-007 |
| QAS-SEC-010 | security | user sees an entity but not some of its claims | normal | hidden claims affect neither status, counts, completeness nor timing (inference suite) | BRQ-007 |

## scalability_design

- Observations: partition by (tenant, month) + spatial index per partition; mandatory time window on list queries (≤ 31 days)
- Claims: partition by (tenant, hash(subject)); current table keyed by ClaimKey; full history indexed on (key, valid, record)
- Batch ingestion: ≤ 1,000 items per command, per-item idempotency; ingestion workers stateless and horizontally scaled; backpressure via queue depth
- Position summarization: high-rate observations stay observations; a derived location claim per entity at most once per predicate sampling interval (RD-PREDICATES)
- Attachments: direct upload/download with signed targets; app tier signs only
- Hot subjects (many writers on one ClaimKey): current-row update is the only contention point; acceptable, bounded by predicate sampling

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-06a
  name: Observation ingestion (sensors + field + adapters)
  derivation: design 5,000 obs/s sustained, 50,000/s burst 60 s (W1 Q11)
  basis: W1 targets
  target: QAS-PERF-012, QAS-SCAL-002
- id: WL-01g
  name: Claim assertions
  derivation: ~10 % of observations yield derived claims after summarization + analyst/adapters ≈ 500/s sustained
  basis: INF
  target: QAS-PERF-001
- id: WL-01h
  name: Resolved entity reads
  derivation: 'dominant read: ~30 % of 2,500 req/s ≈ 750/s'
  basis: INF
  target: QAS-PERF-013
- id: WL-04a
  name: As-of / as-known-at reads
  derivation: low frequency (audit, analysis) ≈ 5–20/s
  basis: INF
  target: LIB §6 p95 ≤ 500 ms
- id: WL-03a
  name: Spatial list queries (bbox + time)
  derivation: map panning ≈ 20 % of reads ≈ 500/s
  basis: INF
  target: QAS-PERF-002 list ≤ 1 s
- id: WL-05a
  name: Attachments
  derivation: 'design: 50 uploads/s avg, PB-class total; bytes bypass app tier'
  basis: INF
  target: object storage throughput; app tier only signs
- id: WL-11a
  name: Lineage traversal
  derivation: ≈ 5/s, depth ≤ 10
  basis: INF
  target: QAS-PERF-014
added_quality_scenarios:
- id: QAS-PERF-012
  quality: performance
  stimulus: batch of 1,000 observations
  environment: 5,000 obs/s sustained per cell
  response_measure: batch commit p95 ≤ 1 s; 0 duplicates on retry
  refines:
  - BRQ-001
- id: QAS-PERF-013
  quality: performance
  stimulus: resolved entity read (current)
  environment: 750 reads/s; 1e8 claims
  response_measure: p95 ≤ 300 ms end-to-end
  refines:
  - BRQ-002
- id: QAS-PERF-014
  quality: performance
  stimulus: lineage trace depth 5
  environment: normal
  response_measure: p95 ≤ 2 s
  refines:
  - BRQ-006
- id: QAS-SEC-009
  quality: security
  stimulus: user without source-protection permission reads claims of a protected human source
  environment: normal
  response_measure: 0 identity attributes disclosed in any response, export or lineage
  refines:
  - BRQ-007
- id: QAS-SEC-010
  quality: security
  stimulus: user sees an entity but not some of its claims
  environment: normal
  response_measure: hidden claims affect neither status, counts, completeness nor timing (inference suite)
  refines:
  - BRQ-007
scalability_design:
- 'Observations: partition by (tenant, month) + spatial index per partition; mandatory time window on list queries (≤ 31 days)'
- 'Claims: partition by (tenant, hash(subject)); current table keyed by ClaimKey; full history indexed on (key, valid, record)'
- 'Batch ingestion: ≤ 1,000 items per command, per-item idempotency; ingestion workers stateless and horizontally scaled;
  backpressure via queue depth'
- 'Position summarization: high-rate observations stay observations; a derived location claim per entity at most once per
  predicate sampling interval (RD-PREDICATES)'
- 'Attachments: direct upload/download with signed targets; app tier signs only'
- 'Hot subjects (many writers on one ClaimKey): current-row update is the only contention point; acceptable, bounded by predicate
  sampling'
```

</details>
