---
id: IMPORTANCE-TIERS
type: importance-tiers
title: Importance Tier Model (ADR-P03)
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: المستوى يُحدد لكل سمة. هذا الجدول يحدد الافتراضي لكل كائن؛ الاستثناءات تُعلن في مواصفة الكائن (W4).
---

# Importance Tier Model (ADR-P03)

> المستوى يُحدد لكل سمة. هذا الجدول يحدد الافتراضي لكل كائن؛ الاستثناءات تُعلن في مواصفة الكائن (W4).

## tier_rules

_4 items_

| tier | name | storage | source | evidence | confidence | conflict_detection | versioning | audit |
|---|---|---|---|---|---|---|---|---|
| T1 | Evidential | claims (bitemporal) | required | optional | 7 dims | yes | via record time | all commands |
| T2 | Governed | immutable versions | when derived | links optional | no | no (concurrency conflict only) | yes | all commands |
| T3 | Operational | current value | no | no | no | no | optimistic version only | all changes |
| T4 | Ephemeral | current value | no | no | no | no | no | no |

## default_assignment

_20 items_

| object | tier |
|---|---|
| Entity attributes (name, type-specific attributes, location) | T1 |
| RealWorldEvent attributes | T1 |
| Relationship existence & attributes | T1 |
| Observation | T1 (immutable after VALIDATED) |
| Source reliability | T1 |
| Evidence metadata | T1 |
| SameAsLink, Conflict resolution | T2 |
| Finding, Assessment | T1 content / T2 lifecycle (published versions immutable) |
| AI result used in decision/assessment/product | T1 |
| Decision, Decision Request | T2 |
| Plan, Plan Version, Baseline | T2 |
| Task (state, assignment, result) | T2 |
| Authority grant, Delegation | T2 |
| Policy, Classification scheme, Retention schedule | T2 |
| Asset / Resource status (R2) | T2 |
| Competency, Qualification, Certification | T2 |
| Alert lifecycle | T2 |
| Situation definition | T2 |
| Tenant / org configuration, quotas, notification preferences | T3 |
| UI state, drafts not submitted | T4 |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
tier_rules:
- tier: T1
  name: Evidential
  storage: claims (bitemporal)
  source: required
  evidence: optional
  confidence: 7 dims
  conflict_detection: 'yes'
  versioning: via record time
  audit: all commands
- tier: T2
  name: Governed
  storage: immutable versions
  source: when derived
  evidence: links optional
  confidence: 'no'
  conflict_detection: no (concurrency conflict only)
  versioning: 'yes'
  audit: all commands
- tier: T3
  name: Operational
  storage: current value
  source: 'no'
  evidence: 'no'
  confidence: 'no'
  conflict_detection: 'no'
  versioning: optimistic version only
  audit: all changes
- tier: T4
  name: Ephemeral
  storage: current value
  source: 'no'
  evidence: 'no'
  confidence: 'no'
  conflict_detection: 'no'
  versioning: 'no'
  audit: 'no'
default_assignment:
- object: Entity attributes (name, type-specific attributes, location)
  tier: T1
- object: RealWorldEvent attributes
  tier: T1
- object: Relationship existence & attributes
  tier: T1
- object: Observation
  tier: T1 (immutable after VALIDATED)
- object: Source reliability
  tier: T1
- object: Evidence metadata
  tier: T1
- object: SameAsLink, Conflict resolution
  tier: T2
- object: Finding, Assessment
  tier: T1 content / T2 lifecycle (published versions immutable)
- object: AI result used in decision/assessment/product
  tier: T1
- object: Decision, Decision Request
  tier: T2
- object: Plan, Plan Version, Baseline
  tier: T2
- object: Task (state, assignment, result)
  tier: T2
- object: Authority grant, Delegation
  tier: T2
- object: Policy, Classification scheme, Retention schedule
  tier: T2
- object: Asset / Resource status (R2)
  tier: T2
- object: Competency, Qualification, Certification
  tier: T2
- object: Alert lifecycle
  tier: T2
- object: Situation definition
  tier: T2
- object: Tenant / org configuration, quotas, notification preferences
  tier: T3
- object: UI state, drafts not submitted
  tier: T4
```

</details>
