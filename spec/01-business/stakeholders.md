---
id: STK
type: stakeholder-model
title: Stakeholder Model (loaded — incomplete)
wave: W1
tier: T0
owner_role: Orchestrator
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
consumers: []
notes: المستند يعرف مجموعات عامة؛ Decision Rights وRACI وPower/Interest مطلوبة في W1
---

# Stakeholder Model (loaded — incomplete)

> المستند يعرف مجموعات عامة؛ Decision Rights وRACI وPower/Interest مطلوبة في W1

## stakeholder_groups

_5 items_

| id | en | ar | epistemic | decision_rights |
|---|---|---|---|---|
| SH-01 | Leadership | القيادة | DOC:PRJ§36 | UNKNOWN |
| SH-02 | Operational Users | المستخدمون التشغيليون | DOC:PRJ§36 | UNKNOWN |
| SH-03 | Information / Analysis Users | مستخدمو المعلومات والتحليل | DOC:PRJ§36 | UNKNOWN |
| SH-04 | Governance | الحوكمة | DOC:PRJ§36 | UNKNOWN |
| SH-05 | Platform Teams | فرق المنصة | DOC:PRJ§36 | UNKNOWN |

## actors

_15 items_

| id | name | group | epistemic |
|---|---|---|---|
| ACT-01 | Executive | SH-01 | DOC:PRJ§45 (group mapping INF) |
| ACT-02 | Manager | SH-01 | DOC:PRJ§45 (group mapping INF) |
| ACT-03 | Planner | SH-02 | DOC:PRJ§45 (group mapping INF) |
| ACT-04 | Analyst | SH-03 | DOC:PRJ§45 (group mapping INF) |
| ACT-05 | Operator | SH-02 | DOC:PRJ§45 (group mapping INF) |
| ACT-06 | Field User | SH-02 | DOC:PRJ§45 (group mapping INF) |
| ACT-07 | Resource Manager | SH-02 | DOC:PRJ§45 (group mapping INF) |
| ACT-08 | Logistics User | SH-02 | DOC:PRJ§45 (group mapping INF) |
| ACT-09 | Risk Manager | SH-02 | DOC:PRJ§45 (group mapping INF) |
| ACT-10 | Training Manager | SH-02 | DOC:PRJ§45 (group mapping INF) |
| ACT-11 | Knowledge Manager | SH-03 | DOC:PRJ§45 (group mapping INF) |
| ACT-12 | Archivist | SH-04 | DOC:PRJ§45 (group mapping INF) |
| ACT-13 | Security Officer | SH-04 | DOC:PRJ§45 (group mapping INF) |
| ACT-14 | Auditor | SH-04 | DOC:PRJ§45 (group mapping INF) |
| ACT-15 | Administrator | SH-05 | DOC:PRJ§45 (group mapping INF) |

## external_systems

- ERP
- HRIS
- GIS
- DMS
- Identity Provider
- Sensors
- Weather
- External APIs

## internal_system_actors

- AI
- Workflow
- Policy
- Event Bus
- Scheduler
- Search
- Notification

## decision_rights

_7 items_

| decision | responsible | accountable | consulted | informed |
|---|---|---|---|---|
| Business Decision (DOM-10) | Manager / Executive حسب Authority | صاحب السلطة المسجل في BC01 | Analyst | Planner |
| Plan approval & baseline | Planner | Manager (≠ المُعد — فصل المهام) | Resource Manager | Operator |
| Task approval | Reviewer | Manager (≠ المنفذ) | — | Planner |
| Assessment publication | Analyst | Analysis lead / Manager | Knowledge Manager | Executive |
| Security exception | Security Officer | موافقة شخصين | Auditor | Administrator |
| Classification change | Originator | Security Officer | — | Auditor |
| Retention / Legal hold | Archivist | Legal / Compliance authority | Security Officer | Auditor |

**authority_model:** قابلة للتهيئة لكل مؤسسة؛ مملوكة لـ BC01 (Q31)

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
stakeholder_groups:
- id: SH-01
  en: Leadership
  ar: القيادة
  epistemic: DOC:PRJ§36
  decision_rights: UNKNOWN
- id: SH-02
  en: Operational Users
  ar: المستخدمون التشغيليون
  epistemic: DOC:PRJ§36
  decision_rights: UNKNOWN
- id: SH-03
  en: Information / Analysis Users
  ar: مستخدمو المعلومات والتحليل
  epistemic: DOC:PRJ§36
  decision_rights: UNKNOWN
- id: SH-04
  en: Governance
  ar: الحوكمة
  epistemic: DOC:PRJ§36
  decision_rights: UNKNOWN
- id: SH-05
  en: Platform Teams
  ar: فرق المنصة
  epistemic: DOC:PRJ§36
  decision_rights: UNKNOWN
actors:
- id: ACT-01
  name: Executive
  group: SH-01
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-02
  name: Manager
  group: SH-01
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-03
  name: Planner
  group: SH-02
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-04
  name: Analyst
  group: SH-03
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-05
  name: Operator
  group: SH-02
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-06
  name: Field User
  group: SH-02
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-07
  name: Resource Manager
  group: SH-02
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-08
  name: Logistics User
  group: SH-02
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-09
  name: Risk Manager
  group: SH-02
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-10
  name: Training Manager
  group: SH-02
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-11
  name: Knowledge Manager
  group: SH-03
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-12
  name: Archivist
  group: SH-04
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-13
  name: Security Officer
  group: SH-04
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-14
  name: Auditor
  group: SH-04
  epistemic: DOC:PRJ§45 (group mapping INF)
- id: ACT-15
  name: Administrator
  group: SH-05
  epistemic: DOC:PRJ§45 (group mapping INF)
external_systems:
- ERP
- HRIS
- GIS
- DMS
- Identity Provider
- Sensors
- Weather
- External APIs
internal_system_actors:
- AI
- Workflow
- Policy
- Event Bus
- Scheduler
- Search
- Notification
decision_rights:
- decision: Business Decision (DOM-10)
  responsible: Manager / Executive حسب Authority
  accountable: صاحب السلطة المسجل في BC01
  consulted: Analyst
  informed: Planner
- decision: Plan approval & baseline
  responsible: Planner
  accountable: Manager (≠ المُعد — فصل المهام)
  consulted: Resource Manager
  informed: Operator
- decision: Task approval
  responsible: Reviewer
  accountable: Manager (≠ المنفذ)
  consulted: null
  informed: Planner
- decision: Assessment publication
  responsible: Analyst
  accountable: Analysis lead / Manager
  consulted: Knowledge Manager
  informed: Executive
- decision: Security exception
  responsible: Security Officer
  accountable: موافقة شخصين
  consulted: Auditor
  informed: Administrator
- decision: Classification change
  responsible: Originator
  accountable: Security Officer
  consulted: null
  informed: Auditor
- decision: Retention / Legal hold
  responsible: Archivist
  accountable: Legal / Compliance authority
  consulted: Security Officer
  informed: Auditor
authority_model: قابلة للتهيئة لكل مؤسسة؛ مملوكة لـ BC01 (Q31)
```

</details>
