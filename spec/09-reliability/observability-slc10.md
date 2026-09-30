---
id: OBS-SLC10
type: observability
title: Observability — SLC-10
wave: W5
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Observability — SLC-10

## signals

_6 items_

| metric | type | alert |
|---|---|---|
| ai.first_token_s | histogram | p95 > 3 s |
| ai.insufficient_evidence_ratio{operation} | gauge | sudden change |
| ai.ungrounded_statements_dropped | counter | trend |
| ai.guard_blocks_total{kind} | counter | injection spike = security review |
| ai.results_rejected_ratio{operation} | gauge | > 30 % → model review |
| ai.gpu_hours{tenant} | counter | quota |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: ai.first_token_s
  type: histogram
  alert: p95 > 3 s
- metric: ai.insufficient_evidence_ratio{operation}
  type: gauge
  alert: sudden change
- metric: ai.ungrounded_statements_dropped
  type: counter
  alert: trend
- metric: ai.guard_blocks_total{kind}
  type: counter
  alert: injection spike = security review
- metric: ai.results_rejected_ratio{operation}
  type: gauge
  alert: '> 30 % → model review'
- metric: ai.gpu_hours{tenant}
  type: counter
  alert: quota
```

</details>
