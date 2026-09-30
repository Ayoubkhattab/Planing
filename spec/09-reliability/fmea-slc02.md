---
id: FMEA-SLC02
type: fmea
title: Failure Mode Analysis — SLC-02
wave: W5
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Failure Mode Analysis — SLC-02

## failure_modes

_8 items_

### FM-S02-01

- **component:** Object storage
- **failure:** unavailable
- **cause:** outage
- **effect:** uploads fail; evidence download fails
- **detection:** health
- **severity:** H
- **likelihood:** L
- **prevention:** replicated object store
- **mitigation_recovery:** claims/observations text continue; attachments marked temporarily unavailable
- **data_loss:** none
- **user_impact:** no files
- **dependency_impact:** evidence views

### FM-S02-02

- **component:** Content scanner
- **failure:** down
- **cause:** failure
- **effect:** attachments stuck in SCANNING
- **detection:** queue age
- **severity:** M
- **likelihood:** M
- **prevention:** scanner pool; alert on age > 10 min
- **mitigation_recovery:** auto-resume; not usable until STORED
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** evidence registration

### FM-S02-03

- **component:** Current table
- **failure:** diverges from history
- **cause:** bug / partial repair
- **effect:** wrong current reads
- **detection:** nightly reconciliation job (history → current)
- **severity:** H
- **likelihood:** L
- **prevention:** same-transaction maintenance; FIT-05
- **mitigation_recovery:** rebuild current from history
- **data_loss:** none
- **user_impact:** wrong values until rebuild
- **dependency_impact:** projections

### FM-S02-04

- **component:** Import worker
- **failure:** crash mid-batch
- **cause:** failure
- **effect:** batch PROCESSING stalls
- **detection:** lease expiry
- **severity:** M
- **likelihood:** M
- **prevention:** leases + idempotent per-record apply
- **mitigation_recovery:** another worker resumes
- **data_loss:** none
- **user_impact:** delay
- **dependency_impact:** adapters

### FM-S02-05

- **component:** Ingestion burst
- **failure:** overload
- **cause:** 50,000/s burst
- **effect:** queue growth
- **detection:** queue depth
- **severity:** H
- **likelihood:** M
- **prevention:** backpressure; per-tenant quotas
- **mitigation_recovery:** drain after burst ≤ 5 min (QAS-SCAL-002)
- **data_loss:** none
- **user_impact:** alert delay
- **dependency_impact:** situations

### FM-S02-06

- **component:** Device clock
- **failure:** wrong
- **cause:** bad device time
- **effect:** wrong observed_at
- **detection:** skew check at sync
- **severity:** M
- **likelihood:** M
- **prevention:** server record time; skew flag
- **mitigation_recovery:** analyst correction via amend (before validation)
- **data_loss:** none
- **user_impact:** misplaced in time
- **dependency_impact:** temporal queries

### FM-S02-07

- **component:** Hot ClaimKey
- **failure:** contention
- **cause:** many writers on one subject/predicate
- **effect:** commit retries
- **detection:** conflict rate metric
- **severity:** M
- **likelihood:** L
- **prevention:** predicate sampling interval; batching
- **mitigation_recovery:** retry with backoff
- **data_loss:** none
- **user_impact:** latency
- **dependency_impact:** —

### FM-S02-08

- **component:** KMS (attachments)
- **failure:** unavailable
- **cause:** failure
- **effect:** cannot sign or decrypt
- **detection:** health
- **severity:** H
- **likelihood:** L
- **prevention:** HA KMS
- **mitigation_recovery:** cached data keys ≤ 10 min
- **data_loss:** none
- **user_impact:** downloads fail after TTL
- **dependency_impact:** evidence

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S02-01
  component: Object storage
  failure: unavailable
  cause: outage
  effect: uploads fail; evidence download fails
  detection: health
  severity: H
  likelihood: L
  prevention: replicated object store
  mitigation_recovery: claims/observations text continue; attachments marked temporarily unavailable
  data_loss: none
  user_impact: no files
  dependency_impact: evidence views
- id: FM-S02-02
  component: Content scanner
  failure: down
  cause: failure
  effect: attachments stuck in SCANNING
  detection: queue age
  severity: M
  likelihood: M
  prevention: scanner pool; alert on age > 10 min
  mitigation_recovery: auto-resume; not usable until STORED
  data_loss: none
  user_impact: delay
  dependency_impact: evidence registration
- id: FM-S02-03
  component: Current table
  failure: diverges from history
  cause: bug / partial repair
  effect: wrong current reads
  detection: nightly reconciliation job (history → current)
  severity: H
  likelihood: L
  prevention: same-transaction maintenance; FIT-05
  mitigation_recovery: rebuild current from history
  data_loss: none
  user_impact: wrong values until rebuild
  dependency_impact: projections
- id: FM-S02-04
  component: Import worker
  failure: crash mid-batch
  cause: failure
  effect: batch PROCESSING stalls
  detection: lease expiry
  severity: M
  likelihood: M
  prevention: leases + idempotent per-record apply
  mitigation_recovery: another worker resumes
  data_loss: none
  user_impact: delay
  dependency_impact: adapters
- id: FM-S02-05
  component: Ingestion burst
  failure: overload
  cause: 50,000/s burst
  effect: queue growth
  detection: queue depth
  severity: H
  likelihood: M
  prevention: backpressure; per-tenant quotas
  mitigation_recovery: drain after burst ≤ 5 min (QAS-SCAL-002)
  data_loss: none
  user_impact: alert delay
  dependency_impact: situations
- id: FM-S02-06
  component: Device clock
  failure: wrong
  cause: bad device time
  effect: wrong observed_at
  detection: skew check at sync
  severity: M
  likelihood: M
  prevention: server record time; skew flag
  mitigation_recovery: analyst correction via amend (before validation)
  data_loss: none
  user_impact: misplaced in time
  dependency_impact: temporal queries
- id: FM-S02-07
  component: Hot ClaimKey
  failure: contention
  cause: many writers on one subject/predicate
  effect: commit retries
  detection: conflict rate metric
  severity: M
  likelihood: L
  prevention: predicate sampling interval; batching
  mitigation_recovery: retry with backoff
  data_loss: none
  user_impact: latency
  dependency_impact: —
- id: FM-S02-08
  component: KMS (attachments)
  failure: unavailable
  cause: failure
  effect: cannot sign or decrypt
  detection: health
  severity: H
  likelihood: L
  prevention: HA KMS
  mitigation_recovery: cached data keys ≤ 10 min
  data_loss: none
  user_impact: downloads fail after TTL
  dependency_impact: evidence
```

</details>
