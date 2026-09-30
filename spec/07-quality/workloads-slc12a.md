---
id: WL-SLC12A
type: workload-catalog
title: Workloads & Added Quality Scenarios — SLC-12a
wave: W5
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Workloads & Added Quality Scenarios — SLC-12a

## workloads

_3 items_

| id | name | derivation | basis | target |
|---|---|---|---|---|
| WL-14a | Disposition planning | buckets = classes × months × tenants ≈ 20 × 120 × 100 = 240,000 buckets (design) | INF | QAS-GOV-001 |
| WL-14b | Subject keys | platform persons ≤ 5 M + person entities ≤ 1e7 | INF | key store scale (W8) |
| WL-14c | Erasure requests | low (≤ 100/day) | INF | ≤ 24 h completion |

## added_quality_scenarios

_2 items_

| id | quality | stimulus | environment | response_measure | refines |
|---|---|---|---|---|---|
| QAS-PRV-002 | privacy | restore of a key-store backup older than a key destruction | DR drill | destroyed keys unusable before any service reads data (restore gate) | BRQ-007 |
| QAS-GOV-001 | compliance | daily disposition evaluation | design volume | candidates computed ≤ 1 h; 0 held records destroyed | BRQ-007 |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-14a
  name: Disposition planning
  derivation: buckets = classes × months × tenants ≈ 20 × 120 × 100 = 240,000 buckets (design)
  basis: INF
  target: QAS-GOV-001
- id: WL-14b
  name: Subject keys
  derivation: platform persons ≤ 5 M + person entities ≤ 1e7
  basis: INF
  target: key store scale (W8)
- id: WL-14c
  name: Erasure requests
  derivation: low (≤ 100/day)
  basis: INF
  target: ≤ 24 h completion
added_quality_scenarios:
- id: QAS-PRV-002
  quality: privacy
  stimulus: restore of a key-store backup older than a key destruction
  environment: DR drill
  response_measure: destroyed keys unusable before any service reads data (restore gate)
  refines:
  - BRQ-007
- id: QAS-GOV-001
  quality: compliance
  stimulus: daily disposition evaluation
  environment: design volume
  response_measure: candidates computed ≤ 1 h; 0 held records destroyed
  refines:
  - BRQ-007
```

</details>
