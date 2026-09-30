---
id: THREAT-MODEL-SLC12A
type: threat-model
title: Threat Model — SLC-12a (STRIDE)
wave: W5
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Threat Model — SLC-12a (STRIDE)

## threats

_5 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S12-01 | Disposition | Tampering | premature destruction of evidence to hide it | L | H | two-person approval; HoldCheck twice; certificate; audit | L |
| THR-S12-02 | Legal hold | Elevation | hold released by one person | L | H | two Legal authorities (INV-LHD-04) | L |
| THR-S12-03 | Key store backup | Info Disclosure | old backup revives destroyed data | M | H | restore gate + key-store backup retention ≤ 35 d (CR-51) | L |
| THR-S12-04 | Erasure | Repudiation | erasure claimed but plaintext copies remain | M | M | per-context confirmation ≤ 24 h; projection rebuild; verification sample | L |
| THR-S12-05 | Schedule | Tampering | retention silently shortened | L | H | immutable versions; Legal approval; retroactivity explicit | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S12-01
  component: Disposition
  stride: Tampering
  threat: premature destruction of evidence to hide it
  likelihood: L
  impact: H
  controls: two-person approval; HoldCheck twice; certificate; audit
  residual_risk: L
- id: THR-S12-02
  component: Legal hold
  stride: Elevation
  threat: hold released by one person
  likelihood: L
  impact: H
  controls: two Legal authorities (INV-LHD-04)
  residual_risk: L
- id: THR-S12-03
  component: Key store backup
  stride: Info Disclosure
  threat: old backup revives destroyed data
  likelihood: M
  impact: H
  controls: restore gate + key-store backup retention ≤ 35 d (CR-51)
  residual_risk: L
- id: THR-S12-04
  component: Erasure
  stride: Repudiation
  threat: erasure claimed but plaintext copies remain
  likelihood: M
  impact: M
  controls: per-context confirmation ≤ 24 h; projection rebuild; verification sample
  residual_risk: L
- id: THR-S12-05
  component: Schedule
  stride: Tampering
  threat: retention silently shortened
  likelihood: L
  impact: H
  controls: immutable versions; Legal approval; retroactivity explicit
  residual_risk: L
```

</details>
