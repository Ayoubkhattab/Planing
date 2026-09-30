---
id: WL-SLC11
type: workload-catalog
title: Workloads & Added Quality Scenarios — SLC-11
wave: W5
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Workloads & Added Quality Scenarios — SLC-11

## workloads

_3 items_

| id | name | derivation | basis | target |
|---|---|---|---|---|
| WL-12a | Sync sessions | design: 5,000 field devices; reconnect storms at shift start | INF | QAS-OFF-001, QAS-OFF-003 |
| WL-12b | Preload builds | ≈ 1 package per device per day; ≤ 200 MB each | INF | build ≤ 10 min |
| WL-12c | Attachment uploads after reconnect | photos ≈ 3 MB × 50 per device per day | INF | resumable direct upload |

## added_quality_scenarios

_2 items_

| id | quality | stimulus | environment | response_measure | refines |
|---|---|---|---|---|---|
| QAS-OFF-002 | security | user's clearance reduced while device offline | reconnect | packages revoked and purged on next contact; commands evaluated under current authorization | BRQ-007 |
| QAS-OFF-003 | scalability | 5,000 devices reconnect within 10 min | morning shift start | all sessions complete ≤ 30 min; oldest-offline devices first; no data loss | BRQ-001 |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-12a
  name: Sync sessions
  derivation: 'design: 5,000 field devices; reconnect storms at shift start'
  basis: INF
  target: QAS-OFF-001, QAS-OFF-003
- id: WL-12b
  name: Preload builds
  derivation: ≈ 1 package per device per day; ≤ 200 MB each
  basis: INF
  target: build ≤ 10 min
- id: WL-12c
  name: Attachment uploads after reconnect
  derivation: photos ≈ 3 MB × 50 per device per day
  basis: INF
  target: resumable direct upload
added_quality_scenarios:
- id: QAS-OFF-002
  quality: security
  stimulus: user's clearance reduced while device offline
  environment: reconnect
  response_measure: packages revoked and purged on next contact; commands evaluated under current authorization
  refines:
  - BRQ-007
- id: QAS-OFF-003
  quality: scalability
  stimulus: 5,000 devices reconnect within 10 min
  environment: morning shift start
  response_measure: all sessions complete ≤ 30 min; oldest-offline devices first; no data loss
  refines:
  - BRQ-001
```

</details>
