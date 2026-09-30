---
id: OWNERSHIP
type: ownership-model
title: Domain Ownership Model
wave: W3
tier: T0
owner_role: Orchestrator
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
consumers: []
notes: كل كائن عمل له مالك واحد (SL-01 = 0). المالك وحده يغير حالة الكائن؛ الآخرون يقرؤون عبر عقد.
---

# Domain Ownership Model

> كل كائن عمل له مالك واحد (SL-01 = 0). المالك وحده يغير حالة الكائن؛ الآخرون يقرؤون عبر عقد.

## ownership

_48 items_

| business_object | name | documented_owner | epistemic | inferred_candidate | domains | refs | owner | note |
|---|---|---|---|---|---|---|---|---|
| BO-ORGANIZATION | Organization | BC01 | DOCUMENTED | — | DOM-01 | PRJ§9 | BC01 | — |
| BO-IDENTITY | Identity | BC01 | DOCUMENTED | — | DOM-02 | PRJ§9 | BC01 | — |
| BO-ENTITY | Entity | BC02 | DOCUMENTED | — | DOM-03 | PRJ§9 | BC02 | — |
| BO-GEOMETRY | Geometry | Geospatial / Information | DECIDED (W3) | BC02 | DOM-04 | PRJ§9, CR-01 | BC02 | value object inside BC02 objects (CR-01) |
| BO-OBSERVATION | Observation | BC02 | DOCUMENTED | — | DOM-06 | PRJ§9 | BC02 | — |
| BO-ANALYSIS-CASE | AnalysisCase | BC03 | DOCUMENTED | — | DOM-08 | PRJ§9 | BC03 | — |
| BO-ASSESSMENT | Assessment | BC03 | DOCUMENTED | — | DOM-08 | PRJ§9, CR-36 | BC03 | — |
| BO-SITUATION | Situation | BC03 | DOCUMENTED | — | DOM-09 | PRJ§9, CR-05 | BC03 | — |
| BO-DECISION | Decision | BC04 | DOCUMENTED | — | DOM-10 | PRJ§9 | BC04 | — |
| BO-PLAN | Plan | BC04 | DOCUMENTED | — | DOM-12 | PRJ§9 | BC04 | — |
| BO-TASK | Task | BC04 | DOCUMENTED | — | DOM-13 | PRJ§9 | BC04 | — |
| BO-ASSET | Asset | BC05 | DOCUMENTED | — | DOM-14 | PRJ§9 | BC05 | — |
| BO-RESOURCE | Resource | BC05 | DOCUMENTED | — | DOM-15 | PRJ§9 | BC05 | — |
| BO-LOGISTICS | Logistics (aggregate term) | BC05 | DOCUMENTED | — | DOM-16 | PRJ§9, OQ-012 | BC05 | — |
| BO-KNOWLEDGE-OBJECT | Knowledge | BC06 | DOCUMENTED | — | DOM-21 | PRJ§9 | BC06 | — |
| BO-ARCHIVE-RECORD | Archive | BC06 | DOCUMENTED | — | DOM-22 | PRJ§9 | BC06 | — |
| BO-AI-REQUEST | AI (aggregate term) | BC07 | DOCUMENTED | — | DOM-23 | PRJ§9 | BC07 | — |
| BO-POLICY | Policy | BC08 | DOCUMENTED | — | DOM-25 | PRJ§9, CR-33 | BC08 | — |
| BO-EVENT | Event (domain-level record) | — | DECIDED (W3) | BC02 | DOM-03 | CR-02 | BC02 | RealWorldEvent (CR-44) |
| BO-RELATIONSHIP | Relationship | — | DECIDED (W3) | BC02 | DOM-03 | CR-02 | BC02 | — |
| BO-CLAIM | Claim | — | DECIDED (W3) | BC02 | DOM-03 | CR-02 | BC02 | — |
| BO-EVIDENCE | Evidence | — | DECIDED (W3) | BC02 | DOM-03, DOM-06 | CR-02, CR-31 | BC02 | DOM-03 owns; DOM-06 uses by reference (CR-31) |
| BO-SOURCE | Source | — | DECIDED (W3) | BC02 | DOM-05 | CR-02 | BC02 | — |
| BO-CONFLICT | Conflict | — | DECIDED (W3) | BC02 | DOM-03 | CR-02 | BC02 | — |
| BO-ER-CASE | EntityResolutionCase | — | DECIDED (W3) | BC03 or BC02 | DOM-07 | CR-02, OQ-013 | BC02 | identity changes stay with identity owner; BC03 proposes (OQ-013) |
| BO-COLLECTION-REQUIREMENT | Collection Requirement | — | DECIDED (W3) | BC02 | DOM-05 | CR-02, CR-34 | BC02 | R2 |
| BO-ALERT | Alert | — | DECIDED (W3) | BC03 | DOM-09 | CR-02 | BC03 | part of Situation aggregate family |
| BO-AUTHORITY | Authority | — | DECIDED (W1 Q31) | BC01 or BC04 | DOM-01, DOM-10 | CR-32 | BC01 | BC04 consumes via Authority Check query |
| BO-DELEGATION | Delegation | — | DECIDED (W3) | BC01 | DOM-01 | CR-02 | BC01 | — |
| BO-COMMUNICATION | Communication / Message | — | DECIDED (W3) | BC04 | DOM-11 | CR-02 | BC04 | delivery mechanics are platform infrastructure; content/record owned by BC04 |
| BO-RISK | Risk | — | DECIDED (W3) | BC04 | DOM-17 | CR-02 | BC04 | R3 |
| BO-INCIDENT | Incident | — | DECIDED (W3) | BC04 | DOM-17 | CR-02 | BC04 | R3; candidate for separate deployment unit (failure isolation) |
| BO-COMPETENCY | Competency / Qualification | — | DECIDED (W3) | BC05 | DOM-18 | CR-02 | BC05 | — |
| BO-ELIGIBILITY | Eligibility | — | DECIDED (W3) | BC05 | DOM-18 | CR-02, OQ-011 | BC05 | derived result, computed by BC05; not stored as truth |
| BO-EXERCISE | Exercise | — | DECIDED (W3) | BC05 | DOM-19 | CR-02 | BC05 | R3 |
| BO-PRODUCT | Report / Operational Product | — | DECIDED (W3) | BC06 | DOM-20 | CR-02 | BC06 | R2 |
| BO-TENANT | Tenant / Workspace | — | DECIDED (W1 Q6,Q32) | BC01 | — | CR-41 | BC01 | Tenant > Organization; domain assignment DOM-01 pending W3 |
| BO-CLASSIFICATION | Security Classification | — | DECIDED (W3) | BC08 | DOM-25 | CR-02 | BC08 | scheme per tenant; labels on objects owned by each object's owner |
| BO-AUDIT-RECORD | Audit Record | — | DECIDED (W3) | BC08 | DOM-25 | CR-02 | BC08 | append-only; written by every context through audit contract |
| BO-SAMEAS | SameAsLink | — | DECIDED (W3) | — | DOM-03 | ER-MODEL | BC02 | — |
| BO-LINEAGE | LineageRecord | — | DECIDED (W3) | — | DOM-03 | PROVENANCE-LINEAGE | BC02 | — |
| BO-SITUATION-ALERT-RULE | Alert Rule | — | DECIDED (W3) | — | DOM-09 | ADR-P07 | BC03 | — |
| BO-DECISION-REQUEST | Decision Request | — | DECIDED (W3) | — | DOM-10 | REQ-DEC-001 | BC04 | — |
| BO-PLAN-OUTCOME | PlanOutcome / measurement | — | DECIDED (W3) | — | DOM-12 | CR-37, REQ-OPS-013 | BC04 | — |
| BO-SECURITY-EXCEPTION | Security Exception | — | DECIDED (W3) | — | DOM-25 | REQ-FND-017 | BC08 | — |
| BO-RETENTION-SCHEDULE | Retention Schedule / Legal Hold | — | DECIDED (W3) | — | DOM-25, DOM-22 | REQ-GOV-006, REQ-GOV-007 | BC08 | — |
| BO-QUOTA | Tenant Quota | — | DECIDED (W3) | — | DOM-01 | REQ-FND-018 | BC01 | — |
| BO-DEVICE | Field Device registration | — | DECIDED (W3) | — | DOM-02 | REQ-OFF-005 | BC01 | — |

**logistics_family:** OQ-012 closed: Logistics is a family — Inventory, Shipment, Movement, Supply, LogisticsRequest — each a separate BO owned by BC05 (R3 detail).

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
ownership:
- business_object: BO-ORGANIZATION
  name: Organization
  documented_owner: BC01
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-01
  refs:
  - PRJ§9
  owner: BC01
- business_object: BO-IDENTITY
  name: Identity
  documented_owner: BC01
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-02
  refs:
  - PRJ§9
  owner: BC01
- business_object: BO-ENTITY
  name: Entity
  documented_owner: BC02
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-03
  refs:
  - PRJ§9
  owner: BC02
- business_object: BO-GEOMETRY
  name: Geometry
  documented_owner: Geospatial / Information
  epistemic: DECIDED (W3)
  inferred_candidate: BC02
  domains:
  - DOM-04
  refs:
  - PRJ§9
  - CR-01
  owner: BC02
  note: value object inside BC02 objects (CR-01)
- business_object: BO-OBSERVATION
  name: Observation
  documented_owner: BC02
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-06
  refs:
  - PRJ§9
  owner: BC02
- business_object: BO-ANALYSIS-CASE
  name: AnalysisCase
  documented_owner: BC03
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-08
  refs:
  - PRJ§9
  owner: BC03
- business_object: BO-ASSESSMENT
  name: Assessment
  documented_owner: BC03
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-08
  refs:
  - PRJ§9
  - CR-36
  owner: BC03
- business_object: BO-SITUATION
  name: Situation
  documented_owner: BC03
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-09
  refs:
  - PRJ§9
  - CR-05
  owner: BC03
- business_object: BO-DECISION
  name: Decision
  documented_owner: BC04
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-10
  refs:
  - PRJ§9
  owner: BC04
- business_object: BO-PLAN
  name: Plan
  documented_owner: BC04
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-12
  refs:
  - PRJ§9
  owner: BC04
- business_object: BO-TASK
  name: Task
  documented_owner: BC04
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-13
  refs:
  - PRJ§9
  owner: BC04
- business_object: BO-ASSET
  name: Asset
  documented_owner: BC05
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-14
  refs:
  - PRJ§9
  owner: BC05
- business_object: BO-RESOURCE
  name: Resource
  documented_owner: BC05
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-15
  refs:
  - PRJ§9
  owner: BC05
- business_object: BO-LOGISTICS
  name: Logistics (aggregate term)
  documented_owner: BC05
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-16
  refs:
  - PRJ§9
  - OQ-012
  owner: BC05
- business_object: BO-KNOWLEDGE-OBJECT
  name: Knowledge
  documented_owner: BC06
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-21
  refs:
  - PRJ§9
  owner: BC06
- business_object: BO-ARCHIVE-RECORD
  name: Archive
  documented_owner: BC06
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-22
  refs:
  - PRJ§9
  owner: BC06
- business_object: BO-AI-REQUEST
  name: AI (aggregate term)
  documented_owner: BC07
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-23
  refs:
  - PRJ§9
  owner: BC07
- business_object: BO-POLICY
  name: Policy
  documented_owner: BC08
  epistemic: DOCUMENTED
  inferred_candidate: null
  domains:
  - DOM-25
  refs:
  - PRJ§9
  - CR-33
  owner: BC08
- business_object: BO-EVENT
  name: Event (domain-level record)
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC02
  domains:
  - DOM-03
  refs:
  - CR-02
  owner: BC02
  note: RealWorldEvent (CR-44)
- business_object: BO-RELATIONSHIP
  name: Relationship
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC02
  domains:
  - DOM-03
  refs:
  - CR-02
  owner: BC02
- business_object: BO-CLAIM
  name: Claim
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC02
  domains:
  - DOM-03
  refs:
  - CR-02
  owner: BC02
- business_object: BO-EVIDENCE
  name: Evidence
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC02
  domains:
  - DOM-03
  - DOM-06
  refs:
  - CR-02
  - CR-31
  owner: BC02
  note: DOM-03 owns; DOM-06 uses by reference (CR-31)
- business_object: BO-SOURCE
  name: Source
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC02
  domains:
  - DOM-05
  refs:
  - CR-02
  owner: BC02
- business_object: BO-CONFLICT
  name: Conflict
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC02
  domains:
  - DOM-03
  refs:
  - CR-02
  owner: BC02
- business_object: BO-ER-CASE
  name: EntityResolutionCase
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC03 or BC02
  domains:
  - DOM-07
  refs:
  - CR-02
  - OQ-013
  owner: BC02
  note: identity changes stay with identity owner; BC03 proposes (OQ-013)
- business_object: BO-COLLECTION-REQUIREMENT
  name: Collection Requirement
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC02
  domains:
  - DOM-05
  refs:
  - CR-02
  - CR-34
  owner: BC02
  note: R2
- business_object: BO-ALERT
  name: Alert
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC03
  domains:
  - DOM-09
  refs:
  - CR-02
  owner: BC03
  note: part of Situation aggregate family
- business_object: BO-AUTHORITY
  name: Authority
  documented_owner: null
  epistemic: DECIDED (W1 Q31)
  inferred_candidate: BC01 or BC04
  domains:
  - DOM-01
  - DOM-10
  refs:
  - CR-32
  owner: BC01
  note: BC04 consumes via Authority Check query
- business_object: BO-DELEGATION
  name: Delegation
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC01
  domains:
  - DOM-01
  refs:
  - CR-02
  owner: BC01
- business_object: BO-COMMUNICATION
  name: Communication / Message
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC04
  domains:
  - DOM-11
  refs:
  - CR-02
  owner: BC04
  note: delivery mechanics are platform infrastructure; content/record owned by BC04
- business_object: BO-RISK
  name: Risk
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC04
  domains:
  - DOM-17
  refs:
  - CR-02
  owner: BC04
  note: R3
- business_object: BO-INCIDENT
  name: Incident
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC04
  domains:
  - DOM-17
  refs:
  - CR-02
  owner: BC04
  note: R3; candidate for separate deployment unit (failure isolation)
- business_object: BO-COMPETENCY
  name: Competency / Qualification
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC05
  domains:
  - DOM-18
  refs:
  - CR-02
  owner: BC05
- business_object: BO-ELIGIBILITY
  name: Eligibility
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC05
  domains:
  - DOM-18
  refs:
  - CR-02
  - OQ-011
  owner: BC05
  note: derived result, computed by BC05; not stored as truth
- business_object: BO-EXERCISE
  name: Exercise
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC05
  domains:
  - DOM-19
  refs:
  - CR-02
  owner: BC05
  note: R3
- business_object: BO-PRODUCT
  name: Report / Operational Product
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC06
  domains:
  - DOM-20
  refs:
  - CR-02
  owner: BC06
  note: R2
- business_object: BO-TENANT
  name: Tenant / Workspace
  documented_owner: null
  epistemic: DECIDED (W1 Q6,Q32)
  inferred_candidate: BC01
  domains: []
  refs:
  - CR-41
  owner: BC01
  note: Tenant > Organization; domain assignment DOM-01 pending W3
- business_object: BO-CLASSIFICATION
  name: Security Classification
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC08
  domains:
  - DOM-25
  refs:
  - CR-02
  owner: BC08
  note: scheme per tenant; labels on objects owned by each object's owner
- business_object: BO-AUDIT-RECORD
  name: Audit Record
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: BC08
  domains:
  - DOM-25
  refs:
  - CR-02
  owner: BC08
  note: append-only; written by every context through audit contract
- business_object: BO-SAMEAS
  name: SameAsLink
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: null
  domains:
  - DOM-03
  refs:
  - ER-MODEL
  owner: BC02
- business_object: BO-LINEAGE
  name: LineageRecord
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: null
  domains:
  - DOM-03
  refs:
  - PROVENANCE-LINEAGE
  owner: BC02
- business_object: BO-SITUATION-ALERT-RULE
  name: Alert Rule
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: null
  domains:
  - DOM-09
  refs:
  - ADR-P07
  owner: BC03
- business_object: BO-DECISION-REQUEST
  name: Decision Request
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: null
  domains:
  - DOM-10
  refs:
  - REQ-DEC-001
  owner: BC04
- business_object: BO-PLAN-OUTCOME
  name: PlanOutcome / measurement
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: null
  domains:
  - DOM-12
  refs:
  - CR-37
  - REQ-OPS-013
  owner: BC04
- business_object: BO-SECURITY-EXCEPTION
  name: Security Exception
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: null
  domains:
  - DOM-25
  refs:
  - REQ-FND-017
  owner: BC08
- business_object: BO-RETENTION-SCHEDULE
  name: Retention Schedule / Legal Hold
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: null
  domains:
  - DOM-25
  - DOM-22
  refs:
  - REQ-GOV-006
  - REQ-GOV-007
  owner: BC08
- business_object: BO-QUOTA
  name: Tenant Quota
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: null
  domains:
  - DOM-01
  refs:
  - REQ-FND-018
  owner: BC01
- business_object: BO-DEVICE
  name: Field Device registration
  documented_owner: null
  epistemic: DECIDED (W3)
  inferred_candidate: null
  domains:
  - DOM-02
  refs:
  - REQ-OFF-005
  owner: BC01
logistics_family: 'OQ-012 closed: Logistics is a family — Inventory, Shipment, Movement, Supply, LogisticsRequest — each a
  separate BO owned by BC05 (R3 detail).'
```

</details>
