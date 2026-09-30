---
id: THREAT-MODEL-SLC04
type: threat-model
title: Threat Model — SLC-04 (STRIDE)
wave: W5
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Threat Model — SLC-04 (STRIDE)

## threats

_7 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S04-01 | ER decision | Tampering | deliberate false merge to bury or blend information | L | H | human decision + SoD; reversible split; decision_basis_level; audit; cluster size gate | L |
| THR-S04-02 | ER queue | Info Disclosure | cases reveal existence of hidden entities | M | H | case visible only if both entities visible; comparison shows visible claims only | L |
| THR-S04-03 | Conflict | Info Disclosure | conflict existence reveals a hidden claim | M | H | INV-CNF-04: visible only with ≥ 2 visible incompatible members | L |
| THR-S04-04 | Cluster | Info Disclosure | identity-cluster endpoint lists hidden members | M | H | invisible members omitted; counts over visible members | L |
| THR-S04-05 | Ruleset | Tampering | weakened ruleset floods queue or hides duplicates | L | M | activation needs evaluation ≥ targets + approver ≠ author | L |
| THR-S04-06 | Resolution | Repudiation | analyst denies having resolved a conflict | L | M | bitemporal resolution record with decided_by; audit | L |
| THR-S04-07 | AI proposals (R2) | Tampering | prompt-injected document induces false match proposals | M | M | AI proposes only (AIL1); human decision; proposer recorded | L |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S04-01
  component: ER decision
  stride: Tampering
  threat: deliberate false merge to bury or blend information
  likelihood: L
  impact: H
  controls: human decision + SoD; reversible split; decision_basis_level; audit; cluster size gate
  residual_risk: L
- id: THR-S04-02
  component: ER queue
  stride: Info Disclosure
  threat: cases reveal existence of hidden entities
  likelihood: M
  impact: H
  controls: case visible only if both entities visible; comparison shows visible claims only
  residual_risk: L
- id: THR-S04-03
  component: Conflict
  stride: Info Disclosure
  threat: conflict existence reveals a hidden claim
  likelihood: M
  impact: H
  controls: 'INV-CNF-04: visible only with ≥ 2 visible incompatible members'
  residual_risk: L
- id: THR-S04-04
  component: Cluster
  stride: Info Disclosure
  threat: identity-cluster endpoint lists hidden members
  likelihood: M
  impact: H
  controls: invisible members omitted; counts over visible members
  residual_risk: L
- id: THR-S04-05
  component: Ruleset
  stride: Tampering
  threat: weakened ruleset floods queue or hides duplicates
  likelihood: L
  impact: M
  controls: activation needs evaluation ≥ targets + approver ≠ author
  residual_risk: L
- id: THR-S04-06
  component: Resolution
  stride: Repudiation
  threat: analyst denies having resolved a conflict
  likelihood: L
  impact: M
  controls: bitemporal resolution record with decided_by; audit
  residual_risk: L
- id: THR-S04-07
  component: AI proposals (R2)
  stride: Tampering
  threat: prompt-injected document induces false match proposals
  likelihood: M
  impact: M
  controls: AI proposes only (AIL1); human decision; proposer recorded
  residual_risk: L
```

</details>
