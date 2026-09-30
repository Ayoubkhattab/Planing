---
id: WL-SLC01
type: workload-catalog
title: Workloads & Added Quality Scenarios — SLC-01
wave: W5
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: الاشتقاقات تقديرية (INF) من نطاق التصميم؛ تُعاد معايرتها في Pilot (ASM-010).
---

# Workloads & Added Quality Scenarios — SLC-01

> الاشتقاقات تقديرية (INF) من نطاق التصميم؛ تُعاد معايرتها في Pilot (ASM-010).

## workloads

_6 items_

| id | name | derivation | basis | target |
|---|---|---|---|---|
| WL-01a | SecurityContext resolution | 5,000 concurrent × ~0.5 req/s = 2,500 req/s sustained; peak 3× = 7,500 req/s | INF from W1 envelope; recalibrate at pilot | QAS-PERF-010 |
| WL-01b | Policy decisions | ~1.3 decisions per request + list scopes → ≈ 10,000 decisions/s at peak | INF | QAS-PERF-009 |
| WL-01c | Security-version checks | 1 per request → 7,500 lookups/s peak | INF | key-value p99 ≤ 2 ms |
| WL-01d | Audit records | commands + above-threshold reads ≈ 2,000 records/s peak, ~200/s average | INF | QAS-PERF-011; storage ≈ avg_rate × 86,400 × ~1 KB ≈ 17 GB/day at 200/s before compression |
| WL-01e | Authority checks | only on decisions/approvals ≈ 10–50/s | INF | p95 ≤ 50 ms |
| WL-01f | Admin commands (users, roles, grants) | low: ≤ 20/s; bursts during SCIM sync ≤ 500/s | INF | QAS-PERF-001 |

## added_quality_scenarios

_4 items_

| id | quality | stimulus | environment | response_measure | refines |
|---|---|---|---|---|---|
| QAS-PERF-009 | performance | PEP requests a policy decision | 10,000 decisions/s | p95 ≤ 5 ms with embedded evaluator; ≤ 20 ms remote | BRQ-007 |
| QAS-PERF-010 | performance | gateway resolves SecurityContext | 7,500 req/s peak | p95 ≤ 20 ms (cache hit p95 ≤ 2 ms) | BRQ-007 |
| QAS-PERF-011 | performance | a command commits | normal | audit record in BC08 store ≤ 5 s p95; anchor ≤ 5 min | BRQ-007 |
| QAS-SEC-008 | security | user disabled via SCIM | normal | next request from any session denied; SCIM-to-effect ≤ 5 min (REQ-FND-005) | BRQ-007 |

## scalability_design

- PDP: مقيّم مضمّن في كل تطبيق (sidecar/library) يستقبل حزمة سياسات موقعة؛ لا نداء شبكة لكل قرار
- SecurityContext: cache لكل بوابة بمفتاح (subject, security_version)
- Security-version store: key-value مكرر لكل خلية، يُحدَّث من قناة EVT-SEC-VERSION-INCREMENTED
- Audit: سلاسل مجزأة 16 shard لكل مستأجر (CR-45)
- كل ما سبق stateless أو مقسم بالمستأجر → توسع أفقي

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-01a
  name: SecurityContext resolution
  derivation: 5,000 concurrent × ~0.5 req/s = 2,500 req/s sustained; peak 3× = 7,500 req/s
  basis: INF from W1 envelope; recalibrate at pilot
  target: QAS-PERF-010
- id: WL-01b
  name: Policy decisions
  derivation: ~1.3 decisions per request + list scopes → ≈ 10,000 decisions/s at peak
  basis: INF
  target: QAS-PERF-009
- id: WL-01c
  name: Security-version checks
  derivation: 1 per request → 7,500 lookups/s peak
  basis: INF
  target: key-value p99 ≤ 2 ms
- id: WL-01d
  name: Audit records
  derivation: commands + above-threshold reads ≈ 2,000 records/s peak, ~200/s average
  basis: INF
  target: QAS-PERF-011; storage ≈ avg_rate × 86,400 × ~1 KB ≈ 17 GB/day at 200/s before compression
- id: WL-01e
  name: Authority checks
  derivation: only on decisions/approvals ≈ 10–50/s
  basis: INF
  target: p95 ≤ 50 ms
- id: WL-01f
  name: Admin commands (users, roles, grants)
  derivation: 'low: ≤ 20/s; bursts during SCIM sync ≤ 500/s'
  basis: INF
  target: QAS-PERF-001
added_quality_scenarios:
- id: QAS-PERF-009
  quality: performance
  stimulus: PEP requests a policy decision
  environment: 10,000 decisions/s
  response_measure: p95 ≤ 5 ms with embedded evaluator; ≤ 20 ms remote
  refines:
  - BRQ-007
- id: QAS-PERF-010
  quality: performance
  stimulus: gateway resolves SecurityContext
  environment: 7,500 req/s peak
  response_measure: p95 ≤ 20 ms (cache hit p95 ≤ 2 ms)
  refines:
  - BRQ-007
- id: QAS-PERF-011
  quality: performance
  stimulus: a command commits
  environment: normal
  response_measure: audit record in BC08 store ≤ 5 s p95; anchor ≤ 5 min
  refines:
  - BRQ-007
- id: QAS-SEC-008
  quality: security
  stimulus: user disabled via SCIM
  environment: normal
  response_measure: next request from any session denied; SCIM-to-effect ≤ 5 min (REQ-FND-005)
  refines:
  - BRQ-007
scalability_design:
- 'PDP: مقيّم مضمّن في كل تطبيق (sidecar/library) يستقبل حزمة سياسات موقعة؛ لا نداء شبكة لكل قرار'
- 'SecurityContext: cache لكل بوابة بمفتاح (subject, security_version)'
- 'Security-version store: key-value مكرر لكل خلية، يُحدَّث من قناة EVT-SEC-VERSION-INCREMENTED'
- 'Audit: سلاسل مجزأة 16 shard لكل مستأجر (CR-45)'
- كل ما سبق stateless أو مقسم بالمستأجر → توسع أفقي
```

</details>
