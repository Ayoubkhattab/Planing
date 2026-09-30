---
id: OBS-SLC12
type: observability
title: Observability — SLC-12
wave: W5
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Observability — SLC-12

## signals

_5 items_

| metric | type | alert |
|---|---|---|
| products.generation_s | histogram | p95 > 120 s |
| distribution.exclusions_total | counter | report |
| archive.fixity_failures_total | counter | any = P1 |
| archive.retrieval_s{tier} | histogram | warm p95 > 60 s |
| knowledge.reuse_total | counter | business (OUT-06) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: products.generation_s
  type: histogram
  alert: p95 > 120 s
- metric: distribution.exclusions_total
  type: counter
  alert: report
- metric: archive.fixity_failures_total
  type: counter
  alert: any = P1
- metric: archive.retrieval_s{tier}
  type: histogram
  alert: warm p95 > 60 s
- metric: knowledge.reuse_total
  type: counter
  alert: business (OUT-06)
```

</details>
