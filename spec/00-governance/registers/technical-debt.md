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

_1 items_

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
```

</details>
