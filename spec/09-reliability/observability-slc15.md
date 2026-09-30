---
id: OBS-SLC15
type: observability
title: Observability — SLC-15
wave: W5
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Observability — SLC-15

## signals

_3 items_

| metric | type | alert |
|---|---|---|
| correlation.proposals_total{kind} | counter | trend |
| correlation.acceptance_ratio{rule} | gauge | < 50 % → rule review |
| coordination.overdue_responsibilities | gauge | business |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: correlation.proposals_total{kind}
  type: counter
  alert: trend
- metric: correlation.acceptance_ratio{rule}
  type: gauge
  alert: < 50 % → rule review
- metric: coordination.overdue_responsibilities
  type: gauge
  alert: business
```

</details>
