---
id: FMEA-SLC03
type: fmea
title: Failure Mode Analysis — SLC-03
wave: W5
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Failure Mode Analysis — SLC-03

## failure_modes

_4 items_

### FM-S03-01

- **component:** Scheduler
- **failure:** down
- **cause:** failure
- **effect:** escalations/expiry/close late
- **detection:** heartbeat
- **severity:** M
- **likelihood:** L
- **prevention:** leased buckets; multiple workers
- **mitigation_recovery:** catch-up on restart; overdue computed at read
- **data_loss:** none
- **user_impact:** late notifications
- **dependency_impact:** —

### FM-S03-02

- **component:** Eligibility service (BC05)
- **failure:** unavailable
- **cause:** failure
- **effect:** assignment rejected
- **detection:** error rate
- **severity:** M
- **likelihood:** L
- **prevention:** HA; cache ≤ 5 min
- **mitigation_recovery:** retry; fail-closed
- **data_loss:** none
- **user_impact:** cannot assign temporarily
- **dependency_impact:** —

### FM-S03-03

- **component:** Notification (SLC-06)
- **failure:** down
- **cause:** failure
- **effect:** assignees not informed
- **detection:** queue lag
- **severity:** M
- **likelihood:** M
- **prevention:** outbox; retry
- **mitigation_recovery:** deliver on recovery; my-tasks list authoritative
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** —

### FM-S03-04

- **component:** Offline replay storm
- **failure:** overload
- **cause:** many devices reconnect
- **effect:** command backlog
- **detection:** queue depth
- **severity:** M
- **likelihood:** M
- **prevention:** per-device rate, batching
- **mitigation_recovery:** backpressure
- **data_loss:** none
- **user_impact:** sync delay
- **dependency_impact:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S03-01
  component: Scheduler
  failure: down
  cause: failure
  effect: escalations/expiry/close late
  detection: heartbeat
  severity: M
  likelihood: L
  prevention: leased buckets; multiple workers
  mitigation_recovery: catch-up on restart; overdue computed at read
  data_loss: none
  user_impact: late notifications
  dependency_impact: —
- id: FM-S03-02
  component: Eligibility service (BC05)
  failure: unavailable
  cause: failure
  effect: assignment rejected
  detection: error rate
  severity: M
  likelihood: L
  prevention: HA; cache ≤ 5 min
  mitigation_recovery: retry; fail-closed
  data_loss: none
  user_impact: cannot assign temporarily
  dependency_impact: —
- id: FM-S03-03
  component: Notification (SLC-06)
  failure: down
  cause: failure
  effect: assignees not informed
  detection: queue lag
  severity: M
  likelihood: M
  prevention: outbox; retry
  mitigation_recovery: deliver on recovery; my-tasks list authoritative
  data_loss: none
  user_impact: delay
  dependency_impact: —
- id: FM-S03-04
  component: Offline replay storm
  failure: overload
  cause: many devices reconnect
  effect: command backlog
  detection: queue depth
  severity: M
  likelihood: M
  prevention: per-device rate, batching
  mitigation_recovery: backpressure
  data_loss: none
  user_impact: sync delay
  dependency_impact: —
```

</details>
