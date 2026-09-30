---
id: OBS-SLC12A
type: observability
title: Observability — SLC-12a
wave: W5
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Observability — SLC-12a

## signals

_5 items_

| metric | type | alert |
|---|---|---|
| disposition.buckets_destroyed_total | counter | report |
| disposition.held_items_rewrapped_total | counter | report |
| erasure.age_h | gauge | > 24 h |
| restore_gate.replayed_keys | counter | each restore |
| keystore.backup_age_days_max | gauge | > 35 d |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
signals:
- metric: disposition.buckets_destroyed_total
  type: counter
  alert: report
- metric: disposition.held_items_rewrapped_total
  type: counter
  alert: report
- metric: erasure.age_h
  type: gauge
  alert: '> 24 h'
- metric: restore_gate.replayed_keys
  type: counter
  alert: each restore
- metric: keystore.backup_age_days_max
  type: gauge
  alert: '> 35 d'
```

</details>
