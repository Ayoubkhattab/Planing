---
id: OBS-SLC02
type: observability
title: Observability — SLC-02
wave: W5
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Observability — SLC-02

## signals

_10 items_

| metric | type | alert |
|---|---|---|
| ingest.obs_per_s{tenant} | counter | < 10 % of baseline 10 min (source silence) |
| ingest.queue_depth | gauge | > 60 s of work |
| ingest.batch_commit_ms | histogram | p95 > 1 s |
| import.quarantine_ratio{adapter} | gauge | > 5 % per batch |
| claims.current_reconciliation_diff | gauge | any > 0 = P1 |
| resolve.latency_ms{mode} | histogram | current p95 > 300 ms; as-of > 500 ms |
| attachments.scanning_age_s | gauge | > 600 s |
| attachments.quarantined_total | counter | any → security review |
| obs.clock_skew_flagged_ratio | gauge | > 2 % per device |
| lineage.trace_ms | histogram | p95 > 2 s |

## business_telemetry

- observations per source type
- claims per predicate
- DISPUTED ratio per predicate
- quarantine reasons per adapter

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: ingest.obs_per_s{tenant}
  type: counter
  alert: < 10 % of baseline 10 min (source silence)
- metric: ingest.queue_depth
  type: gauge
  alert: '> 60 s of work'
- metric: ingest.batch_commit_ms
  type: histogram
  alert: p95 > 1 s
- metric: import.quarantine_ratio{adapter}
  type: gauge
  alert: '> 5 % per batch'
- metric: claims.current_reconciliation_diff
  type: gauge
  alert: any > 0 = P1
- metric: resolve.latency_ms{mode}
  type: histogram
  alert: current p95 > 300 ms; as-of > 500 ms
- metric: attachments.scanning_age_s
  type: gauge
  alert: '> 600 s'
- metric: attachments.quarantined_total
  type: counter
  alert: any → security review
- metric: obs.clock_skew_flagged_ratio
  type: gauge
  alert: '> 2 % per device'
- metric: lineage.trace_ms
  type: histogram
  alert: p95 > 2 s
business_telemetry:
- observations per source type
- claims per predicate
- DISPUTED ratio per predicate
- quarantine reasons per adapter
```

</details>
