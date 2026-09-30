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

_26 items_ (6 categories added by CR-68 — cited as mandatory guards in BC04/BC05 but previously undefined; CONFLICT-03)

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
| RD-HAZARD-CATEGORIES | Hazard categories for Risk and Incident (category_ref). Platform seed [Explicit, risk-contingency-spec §1]: natural, technical, security, health, environmental, other; the tenant's actual catalog is loaded at tenant setup (CR-68) | BC04 | tenant | tenant-defined | yes | yes |
| RD-ASSET-TYPES | Asset types (CMD-AST-REGISTER). Platform seed [Explicit, R2-Q1]: vehicles, equipment, facilities, consumable materials; actual types defined per tenant (CR-68) | BC05 | tenant | tenant-defined | yes | yes |
| RD-RESOURCE-TYPES | Resource pool types (CMD-RPL-CREATE), each with a UCUM unit. Platform seed [Explicit, R2-Q1]: vehicles, equipment, facilities, consumable materials; actual types defined per tenant (CR-68) | BC05 | tenant | tenant-defined | yes | yes |
| RD-LOGISTICS-ITEM-TYPES | Logistics item types, used as resource_type of the pool behind a logistics request [Explicit, logistics-spec §1]: open catalog, e.g. fuel, food, medical equipment, spare parts; items are resource types held in SLC-09 pools, no separate stock model (R3-Q3) (CR-68) | BC05 | tenant | tenant-defined | yes | yes |
| RD-CONDITION-GRADES | Asset condition grades (CMD-AST-UPDATE-CONDITION); every grade carries a serviceable flag [Derived from AGG-ASSET guards: unserviceable grades require CMD-AST-MARK-UNSERVICEABLE, return to service requires a serviceable condition]; seed values to be confirmed by tenant workshop (CR-68) | BC05 | tenant | tenant-defined | yes | yes |
| RD-EXERCISE-TYPES | Exercise types for training scenarios (exercise_type_ref in CMD-SCN-DEFINE); distinct from exercise purpose (drill, certification, assessment in CMD-EXR-PLAN). Examples [Inferred]: tabletop, drill, functional, full-scale; to be confirmed by tenant workshop (CR-68) | BC05 | tenant | tenant-defined | yes | yes |

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
- id: RD-HAZARD-CATEGORIES
  content: 'Hazard categories for Risk and Incident (category_ref). Platform seed [Explicit, risk-contingency-spec §1]: natural,
    technical, security, health, environmental, other; the tenant''s actual catalog is loaded at tenant setup (CR-68)'
  owner: BC04
  scope: tenant
  tenant_rule: tenant-defined
  versioned: true
  effective_time: true
- id: RD-ASSET-TYPES
  content: 'Asset types (CMD-AST-REGISTER). Platform seed [Explicit, R2-Q1]: vehicles, equipment, facilities, consumable materials;
    actual types defined per tenant (CR-68)'
  owner: BC05
  scope: tenant
  tenant_rule: tenant-defined
  versioned: true
  effective_time: true
- id: RD-RESOURCE-TYPES
  content: 'Resource pool types (CMD-RPL-CREATE), each with a UCUM unit. Platform seed [Explicit, R2-Q1]: vehicles, equipment,
    facilities, consumable materials; actual types defined per tenant (CR-68)'
  owner: BC05
  scope: tenant
  tenant_rule: tenant-defined
  versioned: true
  effective_time: true
- id: RD-LOGISTICS-ITEM-TYPES
  content: 'Logistics item types, used as resource_type of the pool behind a logistics request [Explicit, logistics-spec §1]:
    open catalog, e.g. fuel, food, medical equipment, spare parts; items are resource types held in SLC-09 pools, no separate
    stock model (R3-Q3) (CR-68)'
  owner: BC05
  scope: tenant
  tenant_rule: tenant-defined
  versioned: true
  effective_time: true
- id: RD-CONDITION-GRADES
  content: 'Asset condition grades (CMD-AST-UPDATE-CONDITION); every grade carries a serviceable flag [Derived from AGG-ASSET
    guards: unserviceable grades require CMD-AST-MARK-UNSERVICEABLE, return to service requires a serviceable condition];
    seed values to be confirmed by tenant workshop (CR-68)'
  owner: BC05
  scope: tenant
  tenant_rule: tenant-defined
  versioned: true
  effective_time: true
- id: RD-EXERCISE-TYPES
  content: 'Exercise types for training scenarios (exercise_type_ref in CMD-SCN-DEFINE); distinct from exercise purpose (drill,
    certification, assessment in CMD-EXR-PLAN). Examples [Inferred]: tabletop, drill, functional, full-scale; to be confirmed
    by tenant workshop (CR-68)'
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
