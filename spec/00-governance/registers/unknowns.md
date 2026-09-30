---
id: REG-UNK
type: register
title: Unknown Register
wave: W0
tier: T3
owner_role: Orchestrator
status: DRAFT
approved_by: null
approved_at: null
consumers:
- gate-reports
- W1 elicitation
---

# Unknown Register

## unknowns

_22 items_

### UNK-001

- **question:** ما المؤسسة والقطاع والمهمة الأساسية؟
- **decisions_blocked:** scope, slice order, classification
- **priority:** critical
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q1
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-002

- **question:** ما الإطار التنظيمي والقانوني ومتطلبات إقامة البيانات؟
- **decisions_blocked:** ADR-P04, ADR-P08, retention, hosting
- **priority:** critical
- **target_wave:** W1
- **status:** partially_closed_non_blocking_for_design
- **owner:** Sponsor / Orchestrator
- **answer:** Q17,Q18 — design for strictest case; actual jurisdiction still unknown; blocks G8 not design
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-003

- **question:** بيئة التشغيل: سحابة، محلي، معزول، أم مزيج؟
- **decisions_blocked:** ADR-P05, AI hosting, cost
- **priority:** critical
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q20
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-004

- **question:** عدد المؤسسات والوحدات والمستخدمين والمناطق؟
- **decisions_blocked:** ADR-P04, capacity
- **priority:** critical
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q6,Q7
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-005

- **question:** أحجام البيانات ومعدلات الحساسات والصور؟
- **decisions_blocked:** WL-06, WL-11, storage
- **priority:** high
- **target_wave:** W2
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q11
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-006

- **question:** مستويات التصنيف والـ Compartments وNeed-to-Know؟
- **decisions_blocked:** authorization model
- **priority:** critical
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q16 (framework)
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-007

- **question:** ما المعلومات التي تحتاج أثراً كاملاً للأدلة؟
- **decisions_blocked:** ADR-P01, ADR-P03
- **priority:** critical
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q12,Q13
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-008

- **question:** التوفر وRPO/RTO لكل قدرة حرجة؟
- **decisions_blocked:** reliability, DR, cost
- **priority:** high
- **target_wave:** W2
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q21
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-009

- **question:** متطلبات العمل الميداني دون اتصال؟
- **decisions_blocked:** ADR-P09, SLC-11
- **priority:** high
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q9
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-010

- **question:** الأنظمة الخارجية الفعلية وعقودها؟
- **decisions_blocked:** integration, ADR-P12
- **priority:** high
- **target_wave:** W2
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q24,Q25 (framework)
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-011

- **question:** اللغات وقواعد الأسماء والتقويم؟
- **decisions_blocked:** ADR-P15
- **priority:** high
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q15
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-012

- **question:** الميزانية والفريق والجدول؟
- **decisions_blocked:** release scope, ADR-P05
- **priority:** critical
- **target_wave:** W1
- **status:** partially_closed_non_blocking_for_design
- **owner:** Sponsor / Orchestrator
- **answer:** Q29,Q30 — cost-proportional architecture; actual budget unknown; non-blocking
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-013

- **question:** من يحدد استقلالية AI لكل عملية؟
- **decisions_blocked:** AI Autonomy Matrix
- **priority:** high
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q26–Q28
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-014

- **question:** البيانات القديمة المطلوب ترحيلها؟
- **decisions_blocked:** migration
- **priority:** medium
- **target_wave:** W2
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q14
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-015

- **question:** درجة الآنية للمواقف والتنبيهات؟
- **decisions_blocked:** WL-01, WL-06, ADR-P07
- **priority:** high
- **target_wave:** W2
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q23
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-016

- **question:** متطلبات إمكانية الوصول الملزمة؟
- **decisions_blocked:** accessibility
- **priority:** medium
- **target_wave:** W2
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** WCAG 2.2 AA (QAS-ACC-001)
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-017

- **question:** قواعد فصل المهام؟
- **decisions_blocked:** SM-TASK, policies
- **priority:** medium
- **target_wave:** W4
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q8
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-018

- **question:** هل Tenant = Organization، أم مستوى أعلى يضم عدة مؤسسات؟ (W0)
- **decisions_blocked:** ADR-P04, BO-TENANT
- **priority:** high
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q6,Q32
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-019

- **question:** من يملك قرار 'Authority' — الهيكل التنظيمي أم التنسيق التشغيلي؟ (W0)
- **decisions_blocked:** CR-32, BRL-003
- **priority:** high
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q31
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-020

- **question:** هل الواجهات الثلاث (ويب، سطح مكتب، جوال) مطلوبة في الإصدار الأول؟ (W0)
- **decisions_blocked:** ASM-003, HAP-02
- **priority:** medium
- **target_wave:** W1
- **status:** closed_by_delegated_decision
- **owner:** Sponsor / Orchestrator
- **answer:** see W1-answers.md Q10
- **answered_by:** Claude (acting decision owner, delegated by project owner)
- **answered_at:** 2026-09-24

### UNK-021

- **question:** أنظمة ERP/HRIS/DMS/CMMS الفعلية لكل مستأجر وواجهاتها
- **decisions_blocked:** SLC-16 adapters (not the framework)
- **priority:** medium
- **target_wave:** tenant onboarding
- **status:** open
- **owner:** Tenant onboarding
- **answer:** —
- **answered_by:** —
- **answered_at:** —

### UNK-022

- **question:** "الاتصالات الموسعة" (extended communications) المذكورة في `EVOLUTION-ROADMAP.md` §R3 لم تُفكَّك بعد إلى قدرة/نطاق فرعي بمعرِّف (لا CAP ولا DOM مخصص، خلافاً لبقية بنود R3)؛ ما هي القنوات والأنظمة المقصودة فعلاً؟
- **decisions_blocked:** R3 slice scoping for this item specifically (does not block SLC-17/18/19 scoping in `release-3-scope.md`)
- **priority:** low
- **target_wave:** W1/W2-R3 (next pass, once named)
- **status:** open
- **owner:** Orchestrator
- **answer:** —
- **answered_by:** —
- **answered_at:** —

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
unknowns:
- id: UNK-001
  question: ما المؤسسة والقطاع والمهمة الأساسية؟
  decisions_blocked:
  - scope
  - slice order
  - classification
  priority: critical
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q1
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-002
  question: ما الإطار التنظيمي والقانوني ومتطلبات إقامة البيانات؟
  decisions_blocked:
  - ADR-P04
  - ADR-P08
  - retention
  - hosting
  priority: critical
  target_wave: W1
  status: partially_closed_non_blocking_for_design
  owner: Sponsor / Orchestrator
  answer: Q17,Q18 — design for strictest case; actual jurisdiction still unknown; blocks G8 not design
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-003
  question: 'بيئة التشغيل: سحابة، محلي، معزول، أم مزيج؟'
  decisions_blocked:
  - ADR-P05
  - AI hosting
  - cost
  priority: critical
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q20
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-004
  question: عدد المؤسسات والوحدات والمستخدمين والمناطق؟
  decisions_blocked:
  - ADR-P04
  - capacity
  priority: critical
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q6,Q7
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-005
  question: أحجام البيانات ومعدلات الحساسات والصور؟
  decisions_blocked:
  - WL-06
  - WL-11
  - storage
  priority: high
  target_wave: W2
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q11
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-006
  question: مستويات التصنيف والـ Compartments وNeed-to-Know؟
  decisions_blocked:
  - authorization model
  priority: critical
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q16 (framework)
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-007
  question: ما المعلومات التي تحتاج أثراً كاملاً للأدلة؟
  decisions_blocked:
  - ADR-P01
  - ADR-P03
  priority: critical
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q12,Q13
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-008
  question: التوفر وRPO/RTO لكل قدرة حرجة؟
  decisions_blocked:
  - reliability
  - DR
  - cost
  priority: high
  target_wave: W2
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q21
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-009
  question: متطلبات العمل الميداني دون اتصال؟
  decisions_blocked:
  - ADR-P09
  - SLC-11
  priority: high
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q9
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-010
  question: الأنظمة الخارجية الفعلية وعقودها؟
  decisions_blocked:
  - integration
  - ADR-P12
  priority: high
  target_wave: W2
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q24,Q25 (framework)
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-011
  question: اللغات وقواعد الأسماء والتقويم؟
  decisions_blocked:
  - ADR-P15
  priority: high
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q15
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-012
  question: الميزانية والفريق والجدول؟
  decisions_blocked:
  - release scope
  - ADR-P05
  priority: critical
  target_wave: W1
  status: partially_closed_non_blocking_for_design
  owner: Sponsor / Orchestrator
  answer: Q29,Q30 — cost-proportional architecture; actual budget unknown; non-blocking
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-013
  question: من يحدد استقلالية AI لكل عملية؟
  decisions_blocked:
  - AI Autonomy Matrix
  priority: high
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q26–Q28
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-014
  question: البيانات القديمة المطلوب ترحيلها؟
  decisions_blocked:
  - migration
  priority: medium
  target_wave: W2
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q14
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-015
  question: درجة الآنية للمواقف والتنبيهات؟
  decisions_blocked:
  - WL-01
  - WL-06
  - ADR-P07
  priority: high
  target_wave: W2
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q23
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-016
  question: متطلبات إمكانية الوصول الملزمة؟
  decisions_blocked:
  - accessibility
  priority: medium
  target_wave: W2
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: WCAG 2.2 AA (QAS-ACC-001)
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-017
  question: قواعد فصل المهام؟
  decisions_blocked:
  - SM-TASK
  - policies
  priority: medium
  target_wave: W4
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q8
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-018
  question: هل Tenant = Organization، أم مستوى أعلى يضم عدة مؤسسات؟ (W0)
  decisions_blocked:
  - ADR-P04
  - BO-TENANT
  priority: high
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q6,Q32
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-019
  question: من يملك قرار 'Authority' — الهيكل التنظيمي أم التنسيق التشغيلي؟ (W0)
  decisions_blocked:
  - CR-32
  - BRL-003
  priority: high
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q31
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-020
  question: هل الواجهات الثلاث (ويب، سطح مكتب، جوال) مطلوبة في الإصدار الأول؟ (W0)
  decisions_blocked:
  - ASM-003
  - HAP-02
  priority: medium
  target_wave: W1
  status: closed_by_delegated_decision
  owner: Sponsor / Orchestrator
  answer: see W1-answers.md Q10
  answered_by: Claude (acting decision owner, delegated by project owner)
  answered_at: '2026-09-24'
- id: UNK-021
  question: أنظمة ERP/HRIS/DMS/CMMS الفعلية لكل مستأجر وواجهاتها
  decisions_blocked:
  - SLC-16 adapters (not the framework)
  priority: medium
  target_wave: tenant onboarding
  status: open
  owner: Tenant onboarding
  answer: null
  answered_by: null
  answered_at: null
- id: UNK-022
  question: '"الاتصالات الموسعة" (extended communications) المذكورة في EVOLUTION-ROADMAP.md
    §R3 لم تُفكَّك بعد إلى قدرة/نطاق فرعي بمعرِّف'
  decisions_blocked:
  - R3 slice scoping for this item specifically
  priority: low
  target_wave: W1/W2-R3 (next pass, once named)
  status: open
  owner: Orchestrator
  answer: null
  answered_by: null
  answered_at: null
```

</details>
