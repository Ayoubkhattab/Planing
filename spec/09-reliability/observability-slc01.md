---
id: OBS-SLC01
type: observability
title: Observability — SLC-01
wave: W5
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Observability — SLC-01

## signals

_12 items_

| metric | type | alert |
|---|---|---|
| authz.decisions_total{decision} | counter | spike in DENY > 5× baseline for a tenant (5 min) |
| pdp.latency_ms | histogram | p95 > 5 ms (embedded) 10 min |
| pdp.bundle_age_s | gauge | > 120 s |
| secctx.resolve_latency_ms | histogram | p95 > 20 ms |
| secversion.stream_lag_s | gauge | > 2 s |
| audit.ship_lag_s | gauge | > 5 s p95; page at > 60 s |
| audit.local_backlog | gauge | > 1 h equivalent |
| audit.chain_verification | status | any FAIL = P0 incident |
| signin.failures_total{reason} | counter | brute-force pattern per user/IP |
| tenant.provisioning_duration_s | histogram | > 3,600 s (QAS-SCAL-003) |
| scim.sync_to_effect_s | histogram | > 300 s (QAS-SEC-008) |
| exceptions.active | gauge | report to Auditor weekly |

**tracing:** كل طلب يحمل correlation_id من البوابة؛ spans: gateway.resolve_context → pep.decide → command.handle → db.commit (state+history+outbox+audit_outbox)

## business_telemetry

- active users per tenant
- role assignments per unit
- grants and delegations effective
- clearances by level (counts only, AGGREGATE ≥ 5)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: authz.decisions_total{decision}
  type: counter
  alert: spike in DENY > 5× baseline for a tenant (5 min)
- metric: pdp.latency_ms
  type: histogram
  alert: p95 > 5 ms (embedded) 10 min
- metric: pdp.bundle_age_s
  type: gauge
  alert: '> 120 s'
- metric: secctx.resolve_latency_ms
  type: histogram
  alert: p95 > 20 ms
- metric: secversion.stream_lag_s
  type: gauge
  alert: '> 2 s'
- metric: audit.ship_lag_s
  type: gauge
  alert: '> 5 s p95; page at > 60 s'
- metric: audit.local_backlog
  type: gauge
  alert: '> 1 h equivalent'
- metric: audit.chain_verification
  type: status
  alert: any FAIL = P0 incident
- metric: signin.failures_total{reason}
  type: counter
  alert: brute-force pattern per user/IP
- metric: tenant.provisioning_duration_s
  type: histogram
  alert: '> 3,600 s (QAS-SCAL-003)'
- metric: scim.sync_to_effect_s
  type: histogram
  alert: '> 300 s (QAS-SEC-008)'
- metric: exceptions.active
  type: gauge
  alert: report to Auditor weekly
tracing: 'كل طلب يحمل correlation_id من البوابة؛ spans: gateway.resolve_context → pep.decide → command.handle → db.commit
  (state+history+outbox+audit_outbox)'
business_telemetry:
- active users per tenant
- role assignments per unit
- grants and delegations effective
- clearances by level (counts only, AGGREGATE ≥ 5)
```

</details>
