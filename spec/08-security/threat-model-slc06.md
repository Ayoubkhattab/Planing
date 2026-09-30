---
id: THREAT-MODEL-SLC06
type: threat-model
title: Threat Model — SLC-06 (STRIDE)
wave: W5
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Threat Model — SLC-06 (STRIDE)

## threats

_7 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S06-01 | Alert fan-out | Info Disclosure | uncleared subscriber learns that something happened | M | H | INV-ALR-02: no delivery at all to uncleared recipients | L |
| THR-S06-02 | Push payload | Info Disclosure | lock-screen shows sensitive content | H | H | reference + safe template only (INV-NTF-02) | L |
| THR-S06-03 | Tiles | Info Disclosure | cached tile served across scopes | M | H | scope-hash cache keys; private cache headers | L |
| THR-S06-04 | COP counts | Info Disclosure | member counts include hidden members | M | H | counts over visible members only | L |
| THR-S06-05 | Alert rules | Tampering | rule silently changed to suppress alerts | L | H | ACTIVE rules immutable; disable/edit/enable audited; dry-run | L |
| THR-S06-06 | Alert storm | DoS | flood of alerts hides critical ones | M | M | dedupe; severity priority queue; per-rule rate limit | L |
| THR-S06-07 | Subscription | Elevation | subscription used to receive data after revocation | M | H | delivery re-check; auto-end on visibility loss | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S06-01
  component: Alert fan-out
  stride: Info Disclosure
  threat: uncleared subscriber learns that something happened
  likelihood: M
  impact: H
  controls: 'INV-ALR-02: no delivery at all to uncleared recipients'
  residual_risk: L
- id: THR-S06-02
  component: Push payload
  stride: Info Disclosure
  threat: lock-screen shows sensitive content
  likelihood: H
  impact: H
  controls: reference + safe template only (INV-NTF-02)
  residual_risk: L
- id: THR-S06-03
  component: Tiles
  stride: Info Disclosure
  threat: cached tile served across scopes
  likelihood: M
  impact: H
  controls: scope-hash cache keys; private cache headers
  residual_risk: L
- id: THR-S06-04
  component: COP counts
  stride: Info Disclosure
  threat: member counts include hidden members
  likelihood: M
  impact: H
  controls: counts over visible members only
  residual_risk: L
- id: THR-S06-05
  component: Alert rules
  stride: Tampering
  threat: rule silently changed to suppress alerts
  likelihood: L
  impact: H
  controls: ACTIVE rules immutable; disable/edit/enable audited; dry-run
  residual_risk: L
- id: THR-S06-06
  component: Alert storm
  stride: DoS
  threat: flood of alerts hides critical ones
  likelihood: M
  impact: M
  controls: dedupe; severity priority queue; per-rule rate limit
  residual_risk: L
- id: THR-S06-07
  component: Subscription
  stride: Elevation
  threat: subscription used to receive data after revocation
  likelihood: M
  impact: H
  controls: delivery re-check; auto-end on visibility loss
  residual_risk: L
```

</details>
