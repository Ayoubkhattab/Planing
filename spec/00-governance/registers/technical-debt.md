---
id: REG-DEBT
type: register
title: Technical Debt Register
wave: W0
tier: T3
owner_role: Orchestrator
status: DRAFT
approved_by: null
approved_at: null
consumers: []
notes: لا يوجد كود بعد؛ الدين المعماري المعروف مسجل كتصحيحات في corrections.md
---

# Technical Debt Register

> لا يوجد كود بعد؛ الدين المعماري المعروف مسجل كتصحيحات في corrections.md

## technical_debt

_2 items_

### DEBT-001

- **description:** R1: الموارد مرتبطة بالمهام نصاً فقط (SLC-09 في R2)
- **cause:** نطاق R1
- **impact:** لا تحقق من السعة/التوفر في R1
- **severity:** M
- **workaround:** حقل نصي + رابط اختياري
- **remediation:** SLC-09 designed: structured references + migration of legacy notes (SPEC-ALLOCATION §6)
- **owner:** BC05
- **due:** R2
- **related_decisions:** HAP-02
- **status:** remediation designed (R2)

### DEBT-002

- **description:** SLC-19 (Training, Competency & Exercises) domain, contract and acceptance files were authored outside the spec tooling: column order, YAML quoting, hand-written notes and narrative SYS scenarios differ from what slice_gen/slice_contracts/acc_gen produce
- **cause:** R3 slice designed after the W9 tooling baseline; files written directly
- **impact:** Regenerating SLC-19 from slc19_data would drop the hand-written notes and narrative scenarios; the V5 round trip excludes 13 SLC-19 files
- **severity:** L
- **workaround:** Treat SLC-19 files as documents until reconciled; V1-V4 and V6 still verify them
- **remediation:** Move SLC-19 notes into slc19_data, then regenerate and compare scenario coverage before replacing files
- **owner:** BC05
- **due:** before SLC-19 G6 (after R1/R2 pilot reviews, RSK-028)
- **related_decisions:** CR-71
- **status:** open

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
technical_debt:
- id: DEBT-001
  description: 'R1: الموارد مرتبطة بالمهام نصاً فقط (SLC-09 في R2)'
  cause: نطاق R1
  impact: لا تحقق من السعة/التوفر في R1
  severity: M
  workaround: حقل نصي + رابط اختياري
  remediation: 'SLC-09 designed: structured references + migration of legacy notes (SPEC-ALLOCATION §6)'
  owner: BC05
  due: R2
  related_decisions:
  - HAP-02
  status: remediation designed (R2)
- id: DEBT-002
  description: 'SLC-19 (Training, Competency & Exercises) domain, contract and acceptance files were authored outside the
    spec tooling: column order, YAML quoting, hand-written notes and narrative SYS scenarios differ from what slice_gen/slice_contracts/acc_gen
    produce'
  cause: R3 slice designed after the W9 tooling baseline; files written directly
  impact: Regenerating SLC-19 from slc19_data would drop the hand-written notes and narrative scenarios; the V5 round trip
    excludes 13 SLC-19 files
  severity: L
  workaround: Treat SLC-19 files as documents until reconciled; V1-V4 and V6 still verify them
  remediation: Move SLC-19 notes into slc19_data, then regenerate and compare scenario coverage before replacing files
  owner: BC05
  due: before SLC-19 G6 (after R1/R2 pilot reviews, RSK-028)
  related_decisions: CR-71
  status: open
```

</details>
