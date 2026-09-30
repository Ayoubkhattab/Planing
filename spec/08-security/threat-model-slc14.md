---
id: THREAT-MODEL-SLC14
type: threat-model
title: Threat Model — SLC-14
wave: W5
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Threat Model — SLC-14

## threats

_2 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S14-01 | Fulfilment | Info Disclosure | fulfilment status reveals classified collection answering a lower-labelled requirement | M | H | viewer-scoped fulfilment (INV-CRQ-01); expiry by date only | L |
| THR-S14-02 | Requirement | Info Disclosure | requirement text itself reveals an intelligence interest | M | M | requirement label set by requester; tasks inherit ≥ label; field users see task-level text only | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S14-01
  component: Fulfilment
  stride: Info Disclosure
  threat: fulfilment status reveals classified collection answering a lower-labelled requirement
  likelihood: M
  impact: H
  controls: viewer-scoped fulfilment (INV-CRQ-01); expiry by date only
  residual_risk: L
- id: THR-S14-02
  component: Requirement
  stride: Info Disclosure
  threat: requirement text itself reveals an intelligence interest
  likelihood: M
  impact: M
  controls: requirement label set by requester; tasks inherit ≥ label; field users see task-level text only
  residual_risk: L
```

</details>
