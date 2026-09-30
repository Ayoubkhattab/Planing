---
id: THREAT-MODEL-SLC16
type: threat-model
title: Threat Model — SLC-16
wave: W5
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Threat Model — SLC-16

## threats

_5 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S16-01 | Outbound | Info Disclosure | classified content leaves via an integration | M | H | only CAP outbound in R2; release level cap; template-only content; two-person release | L |
| THR-S16-02 | HRIS | Elevation | forged HR change grants access | M | H | proposals only, admin approval, owner guards (INV-HRS-01) | L |
| THR-S16-03 | DMS | Info Disclosure | unmapped DMS classification ingested too low | M | H | unmapped → highest default level until review | L |
| THR-S16-04 | Connections | Tampering | new egress path opened silently | L | H | allow-list entry per connection approved by a second person; monitoring (GOV-005) | L |
| THR-S16-05 | Sensors | Tampering | spoofed sensor readings | M | M | gateway authentication; source reliability; quality rules; corroboration (SLC-15) | M |

## accepted_residual_risks

- THR-S16-05 (M): a compromised sensor gateway can inject plausible readings; mitigated by reliability and corroboration

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S16-01
  component: Outbound
  stride: Info Disclosure
  threat: classified content leaves via an integration
  likelihood: M
  impact: H
  controls: only CAP outbound in R2; release level cap; template-only content; two-person release
  residual_risk: L
- id: THR-S16-02
  component: HRIS
  stride: Elevation
  threat: forged HR change grants access
  likelihood: M
  impact: H
  controls: proposals only, admin approval, owner guards (INV-HRS-01)
  residual_risk: L
- id: THR-S16-03
  component: DMS
  stride: Info Disclosure
  threat: unmapped DMS classification ingested too low
  likelihood: M
  impact: H
  controls: unmapped → highest default level until review
  residual_risk: L
- id: THR-S16-04
  component: Connections
  stride: Tampering
  threat: new egress path opened silently
  likelihood: L
  impact: H
  controls: allow-list entry per connection approved by a second person; monitoring (GOV-005)
  residual_risk: L
- id: THR-S16-05
  component: Sensors
  stride: Tampering
  threat: spoofed sensor readings
  likelihood: M
  impact: M
  controls: gateway authentication; source reliability; quality rules; corroboration (SLC-15)
  residual_risk: M
accepted_residual_risks:
- 'THR-S16-05 (M): a compromised sensor gateway can inject plausible readings; mitigated by reliability and corroboration'
```

</details>
