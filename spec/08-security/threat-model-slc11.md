---
id: THREAT-MODEL-SLC11
type: threat-model
title: Threat Model — SLC-11 (STRIDE)
wave: W5
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Threat Model — SLC-11 (STRIDE)

## threats

_6 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S11-01 | Device | Info Disclosure | stolen device reveals preloaded data | M | H | local encryption; unlock required; package expiry; wipe on contact; level cap | L |
| THR-S11-02 | Sync | Spoofing | forged commands injected as a device | L | H | per-command device signatures + hash chain; device key revocation | L |
| THR-S11-03 | Sync | Repudiation | field user denies an offline action | L | M | signed envelopes stored with conflicts and audit | L |
| THR-S11-04 | Lost device | Tampering | commands created after theft are applied | M | H | INV-SCF-03: post-lost commands always go to review | L |
| THR-S11-05 | Clock | Tampering | device clock manipulated to backdate observations | M | M | server record time; offset measured; skew flag | M |
| THR-S11-06 | Preload | Elevation | package built above the user's current authorization | L | H | build-time filtering; revocation on security_version change | L |

## accepted_residual_risks

- THR-S11-05 (M): a trusted field user can still misreport event time; mitigated by skew flag, validation SoD and corroboration

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S11-01
  component: Device
  stride: Info Disclosure
  threat: stolen device reveals preloaded data
  likelihood: M
  impact: H
  controls: local encryption; unlock required; package expiry; wipe on contact; level cap
  residual_risk: L
- id: THR-S11-02
  component: Sync
  stride: Spoofing
  threat: forged commands injected as a device
  likelihood: L
  impact: H
  controls: per-command device signatures + hash chain; device key revocation
  residual_risk: L
- id: THR-S11-03
  component: Sync
  stride: Repudiation
  threat: field user denies an offline action
  likelihood: L
  impact: M
  controls: signed envelopes stored with conflicts and audit
  residual_risk: L
- id: THR-S11-04
  component: Lost device
  stride: Tampering
  threat: commands created after theft are applied
  likelihood: M
  impact: H
  controls: 'INV-SCF-03: post-lost commands always go to review'
  residual_risk: L
- id: THR-S11-05
  component: Clock
  stride: Tampering
  threat: device clock manipulated to backdate observations
  likelihood: M
  impact: M
  controls: server record time; offset measured; skew flag
  residual_risk: M
- id: THR-S11-06
  component: Preload
  stride: Elevation
  threat: package built above the user's current authorization
  likelihood: L
  impact: H
  controls: build-time filtering; revocation on security_version change
  residual_risk: L
accepted_residual_risks:
- 'THR-S11-05 (M): a trusted field user can still misreport event time; mitigated by skew flag, validation SoD and corroboration'
```

</details>
