---
id: FMEA-SLC01
type: fmea
title: Failure Mode Analysis — SLC-01
wave: W5
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Failure Mode Analysis — SLC-01

## failure_modes

_9 items_

### FM-S01-01

- **component:** IdP
- **failure:** unavailable
- **cause:** network/IdP outage
- **effect:** no new sign-ins; existing sessions continue ≤ 15 min
- **detection:** sign-in error rate
- **severity:** H
- **likelihood:** M
- **prevention:** multi-node IdP (tenant side); clear error UX
- **mitigation_recovery:** sessions continue; field offline unaffected
- **data_loss:** none
- **user_impact:** new logins blocked
- **dependency_impact:** all contexts after token expiry

### FM-S01-02

- **component:** BC01 directory
- **failure:** unavailable
- **cause:** DB/node failure
- **effect:** SecurityContext cannot be rebuilt
- **detection:** health + error rate
- **severity:** H
- **likelihood:** L
- **prevention:** replicated store, critical tier
- **mitigation_recovery:** cached contexts ≤ 60 s, then fail-closed
- **data_loss:** none
- **user_impact:** requests denied after 60 s
- **dependency_impact:** all

### FM-S01-03

- **component:** PDP evaluator
- **failure:** bundle stale / crash
- **cause:** distribution failure
- **effect:** decisions on old policy or none
- **detection:** bundle age metric
- **severity:** H
- **likelihood:** L
- **prevention:** embedded evaluators; signed bundles; max bundle age 5 min then DENY
- **mitigation_recovery:** restart; redistribute
- **data_loss:** none
- **user_impact:** possible denials
- **dependency_impact:** all

### FM-S01-04

- **component:** Security-version store
- **failure:** unavailable
- **cause:** KV failure
- **effect:** cannot verify freshness
- **detection:** health
- **severity:** H
- **likelihood:** L
- **prevention:** replicated KV per cell
- **mitigation_recovery:** fail-closed for writes & above-threshold reads; cached contexts ≤ 60 s for low-level reads
- **data_loss:** none
- **user_impact:** partial denials
- **dependency_impact:** all

### FM-S01-05

- **component:** Security-version stream
- **failure:** lagging
- **cause:** broker backlog
- **effect:** revocation delayed
- **detection:** stream lag metric
- **severity:** H
- **likelihood:** M
- **prevention:** high-priority dedicated channel; lag alert > 2 s
- **mitigation_recovery:** auto-catch-up; PEP falls back to direct KV read
- **data_loss:** none
- **user_impact:** revocation delay
- **dependency_impact:** all

### FM-S01-06

- **component:** Audit store (BC08)
- **failure:** unavailable
- **cause:** failure
- **effect:** audit not persisted centrally
- **detection:** shipper backlog
- **severity:** M
- **likelihood:** L
- **prevention:** local audit outbox buffering
- **mitigation_recovery:** ship on recovery; block writes if backlog > 24 h / 80 % (AUDIT_UNAVAILABLE)
- **data_loss:** none
- **user_impact:** writes blocked only in extreme case
- **dependency_impact:** all

### FM-S01-07

- **component:** Provisioning saga
- **failure:** step fails
- **cause:** dependency failure
- **effect:** tenant stuck
- **detection:** saga timeout
- **severity:** M
- **likelihood:** M
- **prevention:** idempotent steps + compensation
- **mitigation_recovery:** PROVISIONING_FAILED then retry
- **data_loss:** none
- **user_impact:** tenant not usable
- **dependency_impact:** none

### FM-S01-08

- **component:** KMS / HSM
- **failure:** unavailable
- **cause:** failure
- **effect:** cannot unwrap tenant keys
- **detection:** health
- **severity:** H
- **likelihood:** L
- **prevention:** HA KMS, critical tier; key cache with TTL ≤ 10 min in memory
- **mitigation_recovery:** serve from cache; then fail
- **data_loss:** none
- **user_impact:** reads/writes fail after TTL
- **dependency_impact:** all

### FM-S01-09

- **component:** Scheduler
- **failure:** missed expiry
- **cause:** scheduler down
- **effect:** grants/clearances not expired on time
- **detection:** scheduler heartbeat
- **severity:** M
- **likelihood:** L
- **prevention:** effective checks also evaluate validity period at read time (expiry is enforced even if SYS transition late)
- **mitigation_recovery:** catch-up run
- **data_loss:** none
- **user_impact:** none (read-time enforcement)
- **dependency_impact:** none

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
failure_modes:
- id: FM-S01-01
  component: IdP
  failure: unavailable
  cause: network/IdP outage
  effect: no new sign-ins; existing sessions continue ≤ 15 min
  detection: sign-in error rate
  severity: H
  likelihood: M
  prevention: multi-node IdP (tenant side); clear error UX
  mitigation_recovery: sessions continue; field offline unaffected
  data_loss: none
  user_impact: new logins blocked
  dependency_impact: all contexts after token expiry
- id: FM-S01-02
  component: BC01 directory
  failure: unavailable
  cause: DB/node failure
  effect: SecurityContext cannot be rebuilt
  detection: health + error rate
  severity: H
  likelihood: L
  prevention: replicated store, critical tier
  mitigation_recovery: cached contexts ≤ 60 s, then fail-closed
  data_loss: none
  user_impact: requests denied after 60 s
  dependency_impact: all
- id: FM-S01-03
  component: PDP evaluator
  failure: bundle stale / crash
  cause: distribution failure
  effect: decisions on old policy or none
  detection: bundle age metric
  severity: H
  likelihood: L
  prevention: embedded evaluators; signed bundles; max bundle age 5 min then DENY
  mitigation_recovery: restart; redistribute
  data_loss: none
  user_impact: possible denials
  dependency_impact: all
- id: FM-S01-04
  component: Security-version store
  failure: unavailable
  cause: KV failure
  effect: cannot verify freshness
  detection: health
  severity: H
  likelihood: L
  prevention: replicated KV per cell
  mitigation_recovery: fail-closed for writes & above-threshold reads; cached contexts ≤ 60 s for low-level reads
  data_loss: none
  user_impact: partial denials
  dependency_impact: all
- id: FM-S01-05
  component: Security-version stream
  failure: lagging
  cause: broker backlog
  effect: revocation delayed
  detection: stream lag metric
  severity: H
  likelihood: M
  prevention: high-priority dedicated channel; lag alert > 2 s
  mitigation_recovery: auto-catch-up; PEP falls back to direct KV read
  data_loss: none
  user_impact: revocation delay
  dependency_impact: all
- id: FM-S01-06
  component: Audit store (BC08)
  failure: unavailable
  cause: failure
  effect: audit not persisted centrally
  detection: shipper backlog
  severity: M
  likelihood: L
  prevention: local audit outbox buffering
  mitigation_recovery: ship on recovery; block writes if backlog > 24 h / 80 % (AUDIT_UNAVAILABLE)
  data_loss: none
  user_impact: writes blocked only in extreme case
  dependency_impact: all
- id: FM-S01-07
  component: Provisioning saga
  failure: step fails
  cause: dependency failure
  effect: tenant stuck
  detection: saga timeout
  severity: M
  likelihood: M
  prevention: idempotent steps + compensation
  mitigation_recovery: PROVISIONING_FAILED then retry
  data_loss: none
  user_impact: tenant not usable
  dependency_impact: none
- id: FM-S01-08
  component: KMS / HSM
  failure: unavailable
  cause: failure
  effect: cannot unwrap tenant keys
  detection: health
  severity: H
  likelihood: L
  prevention: HA KMS, critical tier; key cache with TTL ≤ 10 min in memory
  mitigation_recovery: serve from cache; then fail
  data_loss: none
  user_impact: reads/writes fail after TTL
  dependency_impact: all
- id: FM-S01-09
  component: Scheduler
  failure: missed expiry
  cause: scheduler down
  effect: grants/clearances not expired on time
  detection: scheduler heartbeat
  severity: M
  likelihood: L
  prevention: effective checks also evaluate validity period at read time (expiry is enforced even if SYS transition late)
  mitigation_recovery: catch-up run
  data_loss: none
  user_impact: none (read-time enforcement)
  dependency_impact: none
```

</details>
