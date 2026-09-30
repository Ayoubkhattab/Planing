---
id: THREAT-MODEL-SLC10
type: threat-model
title: Threat Model — SLC-10 (STRIDE + OWASP LLM)
wave: W5
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Threat Model — SLC-10 (STRIDE + OWASP LLM)

## threats

_6 items_

| id | component | stride | threat | likelihood | impact | controls | residual_risk |
|---|---|---|---|---|---|---|---|
| THR-S10-01 | Context retrieval | Info Disclosure | model sees data the user may not | M | H | retrieval as user; pre-filter + LabelCheck; PB-12 | L |
| THR-S10-02 | Retrieved content | Elevation | indirect prompt injection triggers tools or widens scope | H | H | content as data; operation tool allow-list; argument validation; no write tools (INV-TOL-01) | L |
| THR-S10-03 | Output | Info Disclosure | exfiltration via links or external calls | M | H | no network egress from runtime; link stripping; PB-13 | L |
| THR-S10-04 | Output | Tampering | hallucinated statements presented as facts | H | H | grounding verifier; insufficient-evidence path; citations; human review for effects | M |
| THR-S10-05 | Model supply chain | Tampering | poisoned or altered weights | L | H | digest-pinned weights from internal registry; licence and evaluation gates | L |
| THR-S10-06 | Tenancy | Info Disclosure | cross-tenant leakage via caches or fine-tuning | L | H | no cross-user caches; no training on tenant data in R2 | L |

## accepted_residual_risks

- THR-S10-04 (M): grounding reduces but cannot eliminate wrong statements; effects always need human acceptance (AIL ≤ 3)

## not_in_R2

- no fine-tuning on tenant data
- no autonomous tool execution
- no external model for classified data

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
threats:
- id: THR-S10-01
  component: Context retrieval
  stride: Info Disclosure
  threat: model sees data the user may not
  likelihood: M
  impact: H
  controls: retrieval as user; pre-filter + LabelCheck; PB-12
  residual_risk: L
- id: THR-S10-02
  component: Retrieved content
  stride: Elevation
  threat: indirect prompt injection triggers tools or widens scope
  likelihood: H
  impact: H
  controls: content as data; operation tool allow-list; argument validation; no write tools (INV-TOL-01)
  residual_risk: L
- id: THR-S10-03
  component: Output
  stride: Info Disclosure
  threat: exfiltration via links or external calls
  likelihood: M
  impact: H
  controls: no network egress from runtime; link stripping; PB-13
  residual_risk: L
- id: THR-S10-04
  component: Output
  stride: Tampering
  threat: hallucinated statements presented as facts
  likelihood: H
  impact: H
  controls: grounding verifier; insufficient-evidence path; citations; human review for effects
  residual_risk: M
- id: THR-S10-05
  component: Model supply chain
  stride: Tampering
  threat: poisoned or altered weights
  likelihood: L
  impact: H
  controls: digest-pinned weights from internal registry; licence and evaluation gates
  residual_risk: L
- id: THR-S10-06
  component: Tenancy
  stride: Info Disclosure
  threat: cross-tenant leakage via caches or fine-tuning
  likelihood: L
  impact: H
  controls: no cross-user caches; no training on tenant data in R2
  residual_risk: L
accepted_residual_risks:
- 'THR-S10-04 (M): grounding reduces but cannot eliminate wrong statements; effects always need human acceptance (AIL ≤ 3)'
not_in_R2:
- no fine-tuning on tenant data
- no autonomous tool execution
- no external model for classified data
```

</details>
