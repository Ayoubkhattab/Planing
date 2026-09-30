---
id: BRL
type: business-rules
title: Business Rules Catalog (BRL) — corrected
wave: W2
tier: T0
owner_role: Orchestrator
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
consumers: []
---

# Business Rules Catalog (BRL) — corrected

## rules

_15 items_

### BRL-001

- **legacy_id:** BR01
- **statement:** Every T1 information item shall be traceable to at least one source and, where available, evidence. (T1 as defined in ADR-P03 / W1 Q12)
- **epistemic:** DOC:PRJ§40
- **quality_finding:** Ambiguous: 'important' undefined → RESOLVED (W2)
- **related:** CR-10
- **original_statement:** Important information traceable to source/evidence.
- **enforced_by:** REQ-INF-021, REQ-INF-037

### BRL-002

- **legacy_id:** BR02
- **statement:** A T1 claim shall never be overwritten or deleted to resolve a conflict; conflicts are resolved through a conflict case.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** Ambiguous: 'important' undefined → RESOLVED (W2)
- **related:** CR-10
- **original_statement:** No silent overwrite for important conflicts.
- **enforced_by:** REQ-INF-024, REQ-INF-025

### BRL-003

- **legacy_id:** BR03
- **statement:** A business decision shall be recorded only if the decider holds, at decision time, an authority grant (directly or by delegation) for that decision type and scope, as held in BC01.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** Ambiguous: 'appropriate authority' undefined; Authority duplicated across D01/D10 → RESOLVED (W2)
- **related:** CR-32
- **original_statement:** Decision linked to appropriate authority.
- **enforced_by:** REQ-DEC-002

### BRL-004 — Approved Plan has Baseline.

- **legacy_id:** BR04
- **statement:** Approved Plan has Baseline.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** none found at W0 (INF)
- **related:** —
- **enforced_by:** REQ-OPS-003

### BRL-005

- **legacy_id:** BR05
- **statement:** A change to a baselined plan's objectives, outcomes, phases, milestone dates or resource commitments is a major change and creates a new plan version; changes to descriptions, notes or attachments are minor.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** Ambiguous: 'major change' undefined → RESOLVED (W2)
- **related:** OQ-010
- **original_statement:** Major Plan change creates new Plan Version.
- **enforced_by:** REQ-OPS-004

### BRL-006 — Task completes only when completion requirements met.

- **legacy_id:** BR06
- **statement:** Task completes only when completion requirements met.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** none found at W0 (INF)
- **related:** —
- **enforced_by:** REQ-OPS-008

### BRL-007

- **legacy_id:** BR07
- **statement:** A task assignment requires eligibility when the task type declares required competencies, qualifications or authorizations; an asset assignment requires the asset's valid certification and custody authorization (R2).
- **epistemic:** DOC:PRJ§40
- **quality_finding:** Ambiguous: 'may require' — which assignments, under which condition? → RESOLVED (W2)
- **related:** OQ-011
- **original_statement:** Assignment may require Eligibility / Qualification / Authorization.
- **enforced_by:** REQ-OPS-007

### BRL-008 — AI never bypasses Authorization.

- **legacy_id:** BR08
- **statement:** AI never bypasses Authorization.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** none found at W0 (INF)
- **related:** —
- **enforced_by:** REQ-FND-010

### BRL-009

- **legacy_id:** BR09
- **statement:** Every AI result used as input to a decision, assessment or product shall be traceable to its context package, model, model version and inputs.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** Ambiguous: 'important' undefined → RESOLVED (W2)
- **related:** CR-10
- **original_statement:** Important AI result traceable to Context / Model / Inputs.
- **enforced_by:** —

### BRL-010 — Search cannot expose unauthorized data existence.

- **legacy_id:** BR10
- **statement:** Search cannot expose unauthorized data existence.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** none found at W0 (INF)
- **related:** —
- **enforced_by:** REQ-FND-010, REQ-ANL-008, REQ-SIT-006, REQ-SRC-002

### BRL-011 — Archive ≠ Backup.

- **legacy_id:** BR11
- **statement:** Archive ≠ Backup.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** none found at W0 (INF)
- **related:** —
- **enforced_by:** —

### BRL-012 — Historical Reconstruction distinguishes recorded / reconstructed / inferred.

- **legacy_id:** BR12
- **statement:** Historical Reconstruction distinguishes recorded / reconstructed / inferred.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** none found at W0 (INF)
- **related:** CR-25
- **enforced_by:** —

### BRL-013 — External systems are not automatically Source of Truth.

- **legacy_id:** BR13
- **statement:** External systems are not automatically Source of Truth.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** none found at W0 (INF)
- **related:** —
- **enforced_by:** —

### BRL-014 — Each Domain owns its state.

- **legacy_id:** BR14
- **statement:** Each Domain owns its state.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** none found at W0 (INF)
- **related:** —
- **enforced_by:** —

### BRL-015

- **legacy_id:** BR15
- **statement:** Every state-changing command, and every read of data at or above the tenant audit threshold, shall be audited.
- **epistemic:** DOC:PRJ§40
- **quality_finding:** Ambiguous: 'important' undefined → RESOLVED (W2)
- **related:** CR-10
- **original_statement:** Important operations are auditable.
- **enforced_by:** REQ-FND-015

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
rules:
- id: BRL-001
  legacy_id: BR01
  statement: Every T1 information item shall be traceable to at least one source and, where available, evidence. (T1 as defined
    in ADR-P03 / W1 Q12)
  epistemic: DOC:PRJ§40
  quality_finding: 'Ambiguous: ''important'' undefined → RESOLVED (W2)'
  related:
  - CR-10
  original_statement: Important information traceable to source/evidence.
  enforced_by:
  - REQ-INF-021
  - REQ-INF-037
- id: BRL-002
  legacy_id: BR02
  statement: A T1 claim shall never be overwritten or deleted to resolve a conflict; conflicts are resolved through a conflict
    case.
  epistemic: DOC:PRJ§40
  quality_finding: 'Ambiguous: ''important'' undefined → RESOLVED (W2)'
  related:
  - CR-10
  original_statement: No silent overwrite for important conflicts.
  enforced_by:
  - REQ-INF-024
  - REQ-INF-025
- id: BRL-003
  legacy_id: BR03
  statement: A business decision shall be recorded only if the decider holds, at decision time, an authority grant (directly
    or by delegation) for that decision type and scope, as held in BC01.
  epistemic: DOC:PRJ§40
  quality_finding: 'Ambiguous: ''appropriate authority'' undefined; Authority duplicated across D01/D10 → RESOLVED (W2)'
  related:
  - CR-32
  original_statement: Decision linked to appropriate authority.
  enforced_by:
  - REQ-DEC-002
- id: BRL-004
  legacy_id: BR04
  statement: Approved Plan has Baseline.
  epistemic: DOC:PRJ§40
  quality_finding: none found at W0 (INF)
  related: []
  enforced_by:
  - REQ-OPS-003
- id: BRL-005
  legacy_id: BR05
  statement: A change to a baselined plan's objectives, outcomes, phases, milestone dates or resource commitments is a major
    change and creates a new plan version; changes to descriptions, notes or attachments are minor.
  epistemic: DOC:PRJ§40
  quality_finding: 'Ambiguous: ''major change'' undefined → RESOLVED (W2)'
  related:
  - OQ-010
  original_statement: Major Plan change creates new Plan Version.
  enforced_by:
  - REQ-OPS-004
- id: BRL-006
  legacy_id: BR06
  statement: Task completes only when completion requirements met.
  epistemic: DOC:PRJ§40
  quality_finding: none found at W0 (INF)
  related: []
  enforced_by:
  - REQ-OPS-008
- id: BRL-007
  legacy_id: BR07
  statement: A task assignment requires eligibility when the task type declares required competencies, qualifications or authorizations;
    an asset assignment requires the asset's valid certification and custody authorization (R2).
  epistemic: DOC:PRJ§40
  quality_finding: 'Ambiguous: ''may require'' — which assignments, under which condition? → RESOLVED (W2)'
  related:
  - OQ-011
  original_statement: Assignment may require Eligibility / Qualification / Authorization.
  enforced_by:
  - REQ-OPS-007
- id: BRL-008
  legacy_id: BR08
  statement: AI never bypasses Authorization.
  epistemic: DOC:PRJ§40
  quality_finding: none found at W0 (INF)
  related: []
  enforced_by:
  - REQ-FND-010
- id: BRL-009
  legacy_id: BR09
  statement: Every AI result used as input to a decision, assessment or product shall be traceable to its context package,
    model, model version and inputs.
  epistemic: DOC:PRJ§40
  quality_finding: 'Ambiguous: ''important'' undefined → RESOLVED (W2)'
  related:
  - CR-10
  original_statement: Important AI result traceable to Context / Model / Inputs.
  enforced_by: []
- id: BRL-010
  legacy_id: BR10
  statement: Search cannot expose unauthorized data existence.
  epistemic: DOC:PRJ§40
  quality_finding: none found at W0 (INF)
  related: []
  enforced_by:
  - REQ-FND-010
  - REQ-ANL-008
  - REQ-SIT-006
  - REQ-SRC-002
- id: BRL-011
  legacy_id: BR11
  statement: Archive ≠ Backup.
  epistemic: DOC:PRJ§40
  quality_finding: none found at W0 (INF)
  related: []
  enforced_by: []
- id: BRL-012
  legacy_id: BR12
  statement: Historical Reconstruction distinguishes recorded / reconstructed / inferred.
  epistemic: DOC:PRJ§40
  quality_finding: none found at W0 (INF)
  related:
  - CR-25
  enforced_by: []
- id: BRL-013
  legacy_id: BR13
  statement: External systems are not automatically Source of Truth.
  epistemic: DOC:PRJ§40
  quality_finding: none found at W0 (INF)
  related: []
  enforced_by: []
- id: BRL-014
  legacy_id: BR14
  statement: Each Domain owns its state.
  epistemic: DOC:PRJ§40
  quality_finding: none found at W0 (INF)
  related: []
  enforced_by: []
- id: BRL-015
  legacy_id: BR15
  statement: Every state-changing command, and every read of data at or above the tenant audit threshold, shall be audited.
  epistemic: DOC:PRJ§40
  quality_finding: 'Ambiguous: ''important'' undefined → RESOLVED (W2)'
  related:
  - CR-10
  original_statement: Important operations are auditable.
  enforced_by:
  - REQ-FND-015
```

</details>
