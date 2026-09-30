---
id: WORKLOADS
type: workload-catalog
title: Workload Catalog (initial from W1)
wave: W1
tier: T0/T1
status: DRAFT
approved_by: null
approved_at: null
---

# Workload Catalog (initial from W1)

## workloads

_12 items_

| id | name | load | latency | consistency | source | detail | quality_scenarios |
|---|---|---|---|---|---|---|---|
| WL-01 | Transactional | 5,000 concurrent (design) | p95 ≤ 300ms للأوامر (target) | strong within aggregate | W1 delegated targets | W2/W5 | QAS-PERF-001, QAS-PERF-002, QAS-SCAL-001, QAS-SCAL-004, QAS-REL-003 |
| WL-02 | Search | 5,000 concurrent | p95 ≤ 1s; index lag ≤ 30s | eventual | W1 delegated targets | W2/W5 | QAS-PERF-003, QAS-PERF-004, QAS-PERF-008, QAS-REL-002, QAS-SEC-002, QAS-USA-002 |
| WL-03 | Spatial | مرتبط بـ WL-01 | TBD W5 | strong for writes | W1 delegated targets | W2/W5 | QAS-PERF-007, QAS-SEC-004 |
| WL-04 | Temporal / As-Of | منخفض التكرار، عالي الكلفة | async job للاستعلامات الكبيرة | snapshot | W1 delegated targets | W2/W5 | QAS-TMP-001 |
| WL-06 | Event Streaming / Ingestion | 5,000/s sustained; 50,000/s burst | alerts p95 ≤ 5s end-to-end | at-least-once + idempotent | W1 delegated targets | W2/W5 | QAS-PERF-005, QAS-PERF-006, QAS-SCAL-002, QAS-REL-001 |
| WL-08 | Graph | TBD | TBD W5 | eventual | W1 delegated targets | W2/W5 | — |
| WL-09/10 | AI Retrieval / Inference | R2 | TBD W5 | n/a | W1 delegated targets | W2/W5 | — |
| WL-12 | Offline Sync | 72h–7d offline | sync on reconnect; conflicts to Conflict Engine | eventual + conflict review | W1 delegated targets | W2/W5 | QAS-SEC-007, QAS-OFF-001, QAS-USA-001 |
| WL-05 | Document | R1: store + metadata; OCR/extraction R2 | upload p95 ≤ 2 s per 10 MB (target) | n/a | W2 | W5 | — |
| WL-11 | Batch Processing | analysis runs, raster jobs, bulk import | job start ≤ 30 s; throughput TBD W5 | n/a | W2 | W5 | QAS-TRC-002 |
| WL-15 | Import / Ingestion | adapters + bulk import | QAS-DQ-001; idempotent | exactly-once effect | W2 | W5 | QAS-DQ-001 |
| WL-16 | Export | policy-controlled exports | async for > 10,000 records | snapshot | W2 | W5 | — |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-01
  name: Transactional
  load: 5,000 concurrent (design)
  latency: p95 ≤ 300ms للأوامر (target)
  consistency: strong within aggregate
  source: W1 delegated targets
  detail: W2/W5
  quality_scenarios:
  - QAS-PERF-001
  - QAS-PERF-002
  - QAS-SCAL-001
  - QAS-SCAL-004
  - QAS-REL-003
- id: WL-02
  name: Search
  load: 5,000 concurrent
  latency: p95 ≤ 1s; index lag ≤ 30s
  consistency: eventual
  source: W1 delegated targets
  detail: W2/W5
  quality_scenarios:
  - QAS-PERF-003
  - QAS-PERF-004
  - QAS-PERF-008
  - QAS-REL-002
  - QAS-SEC-002
  - QAS-USA-002
- id: WL-03
  name: Spatial
  load: مرتبط بـ WL-01
  latency: TBD W5
  consistency: strong for writes
  source: W1 delegated targets
  detail: W2/W5
  quality_scenarios:
  - QAS-PERF-007
  - QAS-SEC-004
- id: WL-04
  name: Temporal / As-Of
  load: منخفض التكرار، عالي الكلفة
  latency: async job للاستعلامات الكبيرة
  consistency: snapshot
  source: W1 delegated targets
  detail: W2/W5
  quality_scenarios:
  - QAS-TMP-001
- id: WL-06
  name: Event Streaming / Ingestion
  load: 5,000/s sustained; 50,000/s burst
  latency: alerts p95 ≤ 5s end-to-end
  consistency: at-least-once + idempotent
  source: W1 delegated targets
  detail: W2/W5
  quality_scenarios:
  - QAS-PERF-005
  - QAS-PERF-006
  - QAS-SCAL-002
  - QAS-REL-001
- id: WL-08
  name: Graph
  load: TBD
  latency: TBD W5
  consistency: eventual
  source: W1 delegated targets
  detail: W2/W5
  quality_scenarios: []
- id: WL-09/10
  name: AI Retrieval / Inference
  load: R2
  latency: TBD W5
  consistency: n/a
  source: W1 delegated targets
  detail: W2/W5
  quality_scenarios: []
- id: WL-12
  name: Offline Sync
  load: 72h–7d offline
  latency: sync on reconnect; conflicts to Conflict Engine
  consistency: eventual + conflict review
  source: W1 delegated targets
  detail: W2/W5
  quality_scenarios:
  - QAS-SEC-007
  - QAS-OFF-001
  - QAS-USA-001
- id: WL-05
  name: Document
  load: 'R1: store + metadata; OCR/extraction R2'
  latency: upload p95 ≤ 2 s per 10 MB (target)
  consistency: n/a
  source: W2
  detail: W5
  quality_scenarios: []
- id: WL-11
  name: Batch Processing
  load: analysis runs, raster jobs, bulk import
  latency: job start ≤ 30 s; throughput TBD W5
  consistency: n/a
  source: W2
  detail: W5
  quality_scenarios:
  - QAS-TRC-002
- id: WL-15
  name: Import / Ingestion
  load: adapters + bulk import
  latency: QAS-DQ-001; idempotent
  consistency: exactly-once effect
  source: W2
  detail: W5
  quality_scenarios:
  - QAS-DQ-001
- id: WL-16
  name: Export
  load: policy-controlled exports
  latency: async for > 10,000 records
  consistency: snapshot
  source: W2
  detail: W5
  quality_scenarios: []
```

</details>
