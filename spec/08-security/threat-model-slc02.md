---
id: THREAT-MODEL-SLC02
type: threat-model
title: Threat Model — SLC-02 (STRIDE)
wave: W5
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Threat Model — SLC-02 (STRIDE)

## threats

_10 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S02-01 | Adapter / import | Tampering | poisoned external data asserted as facts | M | H | claims cite adapter source with reliability; quarantine; no automatic truth (BRL-013); anomaly review | M |
| THR-S02-02 | Source | Info Disclosure | identity of protected human source revealed via claims, lineage, exports or search | M | H | PB-08; source label ≥ default+1; lineage cut (PB-11); QAS-SEC-009 | L |
| THR-S02-03 | Claims | Info Disclosure | hidden claims inferred from DISPUTED status, counts or completeness | M | H | LIB §3 visibility-first filtering; QAS-SEC-010 | L |
| THR-S02-04 | Attachments | Tampering | malicious file (malware, polyglot, parser exploit) | M | H | offline scanner + format validation; QUARANTINED state; rendering in sandboxed viewer | M |
| THR-S02-05 | Attachments | Info Disclosure | signed download URL shared or replayed | M | M | ≤ 5 min lifetime; bound to subject + tenant; each grant audited | L |
| THR-S02-06 | Evidence | Tampering | evidence altered after sealing | L | H | content hash + seal hash; custody chain; verification on retrieval (REQ-INF-004) | L |
| THR-S02-07 | Observation | Spoofing | fabricated observation with forged device time | M | M | server record time; clock-skew flag; source reliability; validation SoD | M |
| THR-S02-08 | Location | Info Disclosure | precise positions exposed to lower clearance | M | H | generalize obligation (PB-10) | L |
| THR-S02-09 | External-id resolve | Info Disclosure | probing external ids to learn existence | M | M | not-found shape; rate limit per subject; audit | L |
| THR-S02-10 | Import | DoS | oversized or pathological batch | M | M | size limits; streaming parser; per-tenant job quotas | L |

## accepted_residual_risks

- THR-S02-01 (M): external data can be wrong — by design it is a claim with source reliability, never automatic truth
- THR-S02-04 (M): zero-day file exploits — mitigated by sandboxed rendering
- THR-S02-07 (M): a trusted observer can lie — mitigated by validation SoD and corroboration

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S02-01
  component: Adapter / import
  stride: Tampering
  threat: poisoned external data asserted as facts
  likelihood: M
  impact: H
  controls: claims cite adapter source with reliability; quarantine; no automatic truth (BRL-013); anomaly review
  residual_risk: M
- id: THR-S02-02
  component: Source
  stride: Info Disclosure
  threat: identity of protected human source revealed via claims, lineage, exports or search
  likelihood: M
  impact: H
  controls: PB-08; source label ≥ default+1; lineage cut (PB-11); QAS-SEC-009
  residual_risk: L
- id: THR-S02-03
  component: Claims
  stride: Info Disclosure
  threat: hidden claims inferred from DISPUTED status, counts or completeness
  likelihood: M
  impact: H
  controls: LIB §3 visibility-first filtering; QAS-SEC-010
  residual_risk: L
- id: THR-S02-04
  component: Attachments
  stride: Tampering
  threat: malicious file (malware, polyglot, parser exploit)
  likelihood: M
  impact: H
  controls: offline scanner + format validation; QUARANTINED state; rendering in sandboxed viewer
  residual_risk: M
- id: THR-S02-05
  component: Attachments
  stride: Info Disclosure
  threat: signed download URL shared or replayed
  likelihood: M
  impact: M
  controls: ≤ 5 min lifetime; bound to subject + tenant; each grant audited
  residual_risk: L
- id: THR-S02-06
  component: Evidence
  stride: Tampering
  threat: evidence altered after sealing
  likelihood: L
  impact: H
  controls: content hash + seal hash; custody chain; verification on retrieval (REQ-INF-004)
  residual_risk: L
- id: THR-S02-07
  component: Observation
  stride: Spoofing
  threat: fabricated observation with forged device time
  likelihood: M
  impact: M
  controls: server record time; clock-skew flag; source reliability; validation SoD
  residual_risk: M
- id: THR-S02-08
  component: Location
  stride: Info Disclosure
  threat: precise positions exposed to lower clearance
  likelihood: M
  impact: H
  controls: generalize obligation (PB-10)
  residual_risk: L
- id: THR-S02-09
  component: External-id resolve
  stride: Info Disclosure
  threat: probing external ids to learn existence
  likelihood: M
  impact: M
  controls: not-found shape; rate limit per subject; audit
  residual_risk: L
- id: THR-S02-10
  component: Import
  stride: DoS
  threat: oversized or pathological batch
  likelihood: M
  impact: M
  controls: size limits; streaming parser; per-tenant job quotas
  residual_risk: L
accepted_residual_risks:
- 'THR-S02-01 (M): external data can be wrong — by design it is a claim with source reliability, never automatic truth'
- 'THR-S02-04 (M): zero-day file exploits — mitigated by sandboxed rendering'
- 'THR-S02-07 (M): a trusted observer can lie — mitigated by validation SoD and corroboration'
```

</details>
