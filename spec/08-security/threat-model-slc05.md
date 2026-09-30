---
id: THREAT-MODEL-SLC05
type: threat-model
title: Threat Model — SLC-05 (STRIDE)
wave: W5
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Threat Model — SLC-05 (STRIDE)

## threats

_8 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S05-01 | Search facts | Info Disclosure | finding a visible entity by the value of a hidden claim | H | H | fact-level filtering (SPEC-DISCOVERY §3.1) | L |
| THR-S05-02 | Counts/facets | Info Disclosure | inferring hidden objects from totals or facet buckets | H | H | computed on pre-filtered set only | L |
| THR-S05-03 | Ranking | Info Disclosure | hidden facts boosting rank reveal them | M | M | scoring on visible facts only | L |
| THR-S05-04 | Graph paths | Info Disclosure | path existence through hidden node reveals connection | M | H | traversal on visible graph only | L |
| THR-S05-05 | Stale index | Info Disclosure | revoked access still served from lagging index | H | H | LabelCheck re-check + subject security_version (CR-47) | L |
| THR-S05-06 | Cursor | Tampering | cursor reused by another user or scope | M | M | cursor bound to scope fingerprint | L |
| THR-S05-07 | Discovery service | Elevation | projection bypass: direct index access | L | H | index reachable only from discovery workload identity (TB-04) | L |
| THR-S05-08 | Timing | Info Disclosure | response time correlates with hidden matches | L | M | pre-filter; re-check only on returned page; residual accepted | M |

## accepted_residual_risks

- THR-S05-08 (M): residual timing channel from index-internal filter cost — accepted; monitored in inference suite

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S05-01
  component: Search facts
  stride: Info Disclosure
  threat: finding a visible entity by the value of a hidden claim
  likelihood: H
  impact: H
  controls: fact-level filtering (SPEC-DISCOVERY §3.1)
  residual_risk: L
- id: THR-S05-02
  component: Counts/facets
  stride: Info Disclosure
  threat: inferring hidden objects from totals or facet buckets
  likelihood: H
  impact: H
  controls: computed on pre-filtered set only
  residual_risk: L
- id: THR-S05-03
  component: Ranking
  stride: Info Disclosure
  threat: hidden facts boosting rank reveal them
  likelihood: M
  impact: M
  controls: scoring on visible facts only
  residual_risk: L
- id: THR-S05-04
  component: Graph paths
  stride: Info Disclosure
  threat: path existence through hidden node reveals connection
  likelihood: M
  impact: H
  controls: traversal on visible graph only
  residual_risk: L
- id: THR-S05-05
  component: Stale index
  stride: Info Disclosure
  threat: revoked access still served from lagging index
  likelihood: H
  impact: H
  controls: LabelCheck re-check + subject security_version (CR-47)
  residual_risk: L
- id: THR-S05-06
  component: Cursor
  stride: Tampering
  threat: cursor reused by another user or scope
  likelihood: M
  impact: M
  controls: cursor bound to scope fingerprint
  residual_risk: L
- id: THR-S05-07
  component: Discovery service
  stride: Elevation
  threat: 'projection bypass: direct index access'
  likelihood: L
  impact: H
  controls: index reachable only from discovery workload identity (TB-04)
  residual_risk: L
- id: THR-S05-08
  component: Timing
  stride: Info Disclosure
  threat: response time correlates with hidden matches
  likelihood: L
  impact: M
  controls: pre-filter; re-check only on returned page; residual accepted
  residual_risk: M
accepted_residual_risks:
- 'THR-S05-08 (M): residual timing channel from index-internal filter cost — accepted; monitored in inference suite'
```

</details>
