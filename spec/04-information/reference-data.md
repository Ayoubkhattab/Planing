---
id: REFERENCE-DATA
type: reference-data
title: Reference Data Catalog (ADR-P14)
wave: W3
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: 'كل قائمة: مالك، إصدار، زمن سريان. locked = لا تعديل؛ extend = المستأجر يضيف ولا يعدل؛ configure = معاملات قابلة للضبط؛
  tenant-defined = يعرّفها المستأجر.'
---

# Reference Data Catalog (ADR-P14)

> كل قائمة: مالك، إصدار، زمن سريان. locked = لا تعديل؛ extend = المستأجر يضيف ولا يعدل؛ configure = معاملات قابلة للضبط؛ tenant-defined = يعرّفها المستأجر.

## code_lists

_20 items_

| id | content | owner | scope | tenant_rule | versioned | effective_time |
|---|---|---|---|---|---|---|
| RD-OBJECT-TYPES | Object types | BC02 | platform | extend | yes | yes |
| RD-ENTITY-TYPES | Entity types (person, organization, facility, location, asset-ref, document, vehicle…) | BC02 | platform | extend | yes | yes |
| RD-EVENT-TYPES | Real-world event types | BC02 | platform | extend | yes | yes |
| RD-PREDICATES | Predicates: value type, cardinality, unit family, tolerance, freshness threshold, default tier | BC02 | platform | extend | yes | yes |
| RD-RELATIONSHIP-TYPES | Relationship types with allowed source/target types and inverse | BC02 | platform | extend | yes | yes |
| RD-SOURCE-TYPES | Source types | BC02 | platform | extend | yes | yes |
| RD-SOURCE-RELIABILITY | Admiralty reliability A–F | BC02 | platform | locked | yes | yes |
| RD-INFO-CREDIBILITY | Admiralty credibility 1–6 | BC02 | platform | locked | yes | yes |
| RD-EVIDENCE-TYPES | Evidence types | BC02 | platform | extend | yes | yes |
| RD-CONFLICT-RULES | Conflict detection rules CF-01..05 + parameters | BC02 | platform | configure | yes | yes |
| RD-ESTIMATIVE-PROBABILITY | Estimative probability terms with numeric ranges | BC03 | platform | locked | yes | yes |
| RD-UNITS | Units of measure (UCUM) | BC02 | external standard | locked | yes | yes |
| RD-CRS | Coordinate reference systems (EPSG) | BC02 | external standard | locked | yes | yes |
| RD-LANGUAGES | Languages (BCP 47) | BC08 | external standard | locked | yes | yes |
| RD-CLASSIFICATION | Classification levels, compartments, caveats | BC08 | tenant | tenant-defined | yes | yes |
| RD-RECORD-CLASSES | Record classes and retention periods | BC08 | tenant | tenant-defined | yes | yes |
| RD-DECISION-TYPES | Decision types (for authority grants) | BC01 | tenant | tenant-defined | yes | yes |
| RD-TASK-TYPES | Task types with required competencies and completion criteria templates | BC04 | tenant | tenant-defined | yes | yes |
| RD-ALERT-RULE-TYPES | Alert rule types | BC03 | platform | extend | yes | yes |
| RD-COMPETENCIES | Competencies, qualifications, certifications | BC05 | tenant | tenant-defined | yes | yes |

## rules

- البيانات التاريخية تحتفظ بإصدار القائمة الذي سُجلت به
- حذف رمز = إيقاف (deprecated) مع زمن سريان، لا حذف فعلي
- تغيير معنى رمز ممنوع؛ يُنشأ رمز جديد

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
code_lists:
- id: RD-OBJECT-TYPES
  content: Object types
  owner: BC02
  scope: platform
  tenant_rule: extend
  versioned: true
  effective_time: true
- id: RD-ENTITY-TYPES
  content: Entity types (person, organization, facility, location, asset-ref, document, vehicle…)
  owner: BC02
  scope: platform
  tenant_rule: extend
  versioned: true
  effective_time: true
- id: RD-EVENT-TYPES
  content: Real-world event types
  owner: BC02
  scope: platform
  tenant_rule: extend
  versioned: true
  effective_time: true
- id: RD-PREDICATES
  content: 'Predicates: value type, cardinality, unit family, tolerance, freshness threshold, default tier'
  owner: BC02
  scope: platform
  tenant_rule: extend
  versioned: true
  effective_time: true
- id: RD-RELATIONSHIP-TYPES
  content: Relationship types with allowed source/target types and inverse
  owner: BC02
  scope: platform
  tenant_rule: extend
  versioned: true
  effective_time: true
- id: RD-SOURCE-TYPES
  content: Source types
  owner: BC02
  scope: platform
  tenant_rule: extend
  versioned: true
  effective_time: true
- id: RD-SOURCE-RELIABILITY
  content: Admiralty reliability A–F
  owner: BC02
  scope: platform
  tenant_rule: locked
  versioned: true
  effective_time: true
- id: RD-INFO-CREDIBILITY
  content: Admiralty credibility 1–6
  owner: BC02
  scope: platform
  tenant_rule: locked
  versioned: true
  effective_time: true
- id: RD-EVIDENCE-TYPES
  content: Evidence types
  owner: BC02
  scope: platform
  tenant_rule: extend
  versioned: true
  effective_time: true
- id: RD-CONFLICT-RULES
  content: Conflict detection rules CF-01..05 + parameters
  owner: BC02
  scope: platform
  tenant_rule: configure
  versioned: true
  effective_time: true
- id: RD-ESTIMATIVE-PROBABILITY
  content: Estimative probability terms with numeric ranges
  owner: BC03
  scope: platform
  tenant_rule: locked
  versioned: true
  effective_time: true
- id: RD-UNITS
  content: Units of measure (UCUM)
  owner: BC02
  scope: external standard
  tenant_rule: locked
  versioned: true
  effective_time: true
- id: RD-CRS
  content: Coordinate reference systems (EPSG)
  owner: BC02
  scope: external standard
  tenant_rule: locked
  versioned: true
  effective_time: true
- id: RD-LANGUAGES
  content: Languages (BCP 47)
  owner: BC08
  scope: external standard
  tenant_rule: locked
  versioned: true
  effective_time: true
- id: RD-CLASSIFICATION
  content: Classification levels, compartments, caveats
  owner: BC08
  scope: tenant
  tenant_rule: tenant-defined
  versioned: true
  effective_time: true
- id: RD-RECORD-CLASSES
  content: Record classes and retention periods
  owner: BC08
  scope: tenant
  tenant_rule: tenant-defined
  versioned: true
  effective_time: true
- id: RD-DECISION-TYPES
  content: Decision types (for authority grants)
  owner: BC01
  scope: tenant
  tenant_rule: tenant-defined
  versioned: true
  effective_time: true
- id: RD-TASK-TYPES
  content: Task types with required competencies and completion criteria templates
  owner: BC04
  scope: tenant
  tenant_rule: tenant-defined
  versioned: true
  effective_time: true
- id: RD-ALERT-RULE-TYPES
  content: Alert rule types
  owner: BC03
  scope: platform
  tenant_rule: extend
  versioned: true
  effective_time: true
- id: RD-COMPETENCIES
  content: Competencies, qualifications, certifications
  owner: BC05
  scope: tenant
  tenant_rule: tenant-defined
  versioned: true
  effective_time: true
rules:
- البيانات التاريخية تحتفظ بإصدار القائمة الذي سُجلت به
- حذف رمز = إيقاف (deprecated) مع زمن سريان، لا حذف فعلي
- تغيير معنى رمز ممنوع؛ يُنشأ رمز جديد
```

</details>
