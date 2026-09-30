---
id: DOMAINS
type: domain-model
title: Domains (26) and Bounded Context assignment
wave: W3
tier: T0
owner_role: Orchestrator
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
consumers: []
---

# Domains (26) and Bounded Context assignment

## bounded_contexts

_8 items_

| id | name | domains | epistemic | boundary_test |
|---|---|---|---|---|
| BC01 | Foundation | DOM-01, DOM-02 | DOC:PRJ§8 | DONE W3 — see bc-boundary-test.md |
| BC02 | Information | DOM-03, DOM-04, DOM-05, DOM-06 | DOC:PRJ§8 | DONE W3 — see bc-boundary-test.md |
| BC03 | Intelligence & Analysis | DOM-07, DOM-08, DOM-09 | DOC:PRJ§8 | DONE W3 — see bc-boundary-test.md |
| BC04 | Operations | DOM-10, DOM-11, DOM-12, DOM-13, DOM-17 | DOC:PRJ§8 | DONE W3 — see bc-boundary-test.md |
| BC05 | Resources & Readiness | DOM-14, DOM-15, DOM-16, DOM-18, DOM-19 | DOC:PRJ§8 | DONE W3 — see bc-boundary-test.md |
| BC06 | Knowledge & Products | DOM-20, DOM-21, DOM-22 | DOC:PRJ§8 | DONE W3 — see bc-boundary-test.md |
| BC07 | Platform Intelligence | DOM-23, DOM-24 | DOC:PRJ§8 | DONE W3 — see bc-boundary-test.md |
| BC08 | Governance & Runtime | DOM-25, DOM-26 | DOC:PRJ§8 | DONE W3 — see bc-boundary-test.md |

## domains

_26 items_

| id | name | group | bounded_context | elements | epistemic | note |
|---|---|---|---|---|---|---|
| DOM-01 | Organization & Command | Foundation | BC01 | Organization, Organizational Unit, Team, Role, Responsibility, Authority, Delegation, Tenant, Workspace, Quota | DOC:PRJ§7 | Tenant/Workspace added (CR-41) |
| DOM-02 | Identity & Access | Foundation | BC01 | Identity, User, Service Account, Authentication, Authorization, Access Policy, Device | DOC:PRJ§7 | — |
| DOM-03 | Information Fabric | Foundation | BC02 | Entity, Event, Relationship, Claim, Evidence, Provenance, Version, Metadata, SameAsLink, Conflict, EntityResolutionCase | DOC:PRJ§7 | ER decision objects owned here (OQ-013) |
| DOM-04 | Geospatial | Geospatial & Information Collection | BC02 | Location, Geometry, CRS, Spatial Representation, Spatial Analysis | DOC:PRJ§7 | — |
| DOM-05 | Sources & Collection | Geospatial & Information Collection | BC02 | Source, Collection Requirement, Collection Method, Collection Activity | DOC:PRJ§7 | — |
| DOM-06 | Observation & Field | Geospatial & Information Collection | BC02 | Observation, Field Session, Measurement, Evidence (reference to DOM-03), Offline Capture | DOC:PRJ§7 | — |
| DOM-07 | Intelligence | Geospatial & Information Collection | BC03 | Information Processing, Entity Resolution proposals, Correlation, Fusion, Intelligence Product | DOC:PRJ§7 | — |
| DOM-08 | Analysis & Assessment | Analysis & Operations | BC03 | Analysis Case, Analytical Question, Hypothesis, Assumption, Analysis Run, Finding, Assessment, Uncertainty | DOC:PRJ§7 | — |
| DOM-09 | Situation Management | Analysis & Operations | BC03 | Situation, Situation Member, Situation Change, Alert, Current Context | DOC:PRJ§7 | — |
| DOM-10 | Command & Coordination | Analysis & Operations | BC04 | Decision, Decision Request, Coordination Case, Authority check (consumes BC01), Approval | DOC:PRJ§7 | — |
| DOM-11 | Communications | Analysis & Operations | BC04 | Communication, Message, Channel, Notification, Distribution | DOC:PRJ§7 | — |
| DOM-12 | Planning | Planning & Execution | BC04 | Objective, Outcome, Plan, Plan Version, Phase, Activity, Milestone, Baseline | DOC:PRJ§7 | — |
| DOM-13 | Tasks & Workflow | Planning & Execution | BC04 | Task, Assignment, Requirement, Dependency, Workflow, Result, Exception | DOC:PRJ§7 | — |
| DOM-14 | Assets | Planning & Execution | BC05 | Asset, Capability, Ownership, Custody, Status, Condition, Maintenance | DOC:PRJ§7 | — |
| DOM-15 | Resources | Planning & Execution | BC05 | Resource, Pool, Capacity, Availability, Allocation, Consumption | DOC:PRJ§7 | — |
| DOM-16 | Logistics | Planning & Execution | BC05 | Inventory, Shipment, Movement, Supply, Storage, Logistics Request | DOC:PRJ§7 | — |
| DOM-17 | Risk & Emergency | Analysis & Operations | BC04 | Risk, Hazard, Incident, Emergency, Crisis, Response, Recovery, Continuity | DOC:PRJ§7 | regrouped to match BC04 (CR-42) |
| DOM-18 | Training & Competency | Risk, Training & Knowledge | BC05 | Competency, Training, Qualification, Certification, Readiness, Eligibility | DOC:PRJ§7 | — |
| DOM-19 | Exercises & Simulation | Risk, Training & Knowledge | BC05 | Exercise, Scenario, Simulation, Evaluation, After Action Review | DOC:PRJ§7 | — |
| DOM-20 | Reports & Operational Products | Risk, Training & Knowledge | BC06 | Report, Dashboard, Map Product, Briefing, Analytical Product | DOC:PRJ§7 | — |
| DOM-21 | Knowledge Management | Risk, Training & Knowledge | BC06 | Knowledge Object, Procedure, Policy Knowledge, Lesson, Best Practice, Semantic Relationships | DOC:PRJ§7 | — |
| DOM-22 | Archive & Institutional Memory | Risk, Training & Knowledge | BC06 | Archive Record, Retention, Legal Hold, Preservation, Historical Retrieval, Historical Reconstruction | DOC:PRJ§7 | — |
| DOM-23 | AI | Platform Intelligence & Infrastructure | BC07 | AI Request, AI Run, Context Package, AI Result, AI Review, AI Evaluation, AI Tool Registry | DOC:PRJ§7 | — |
| DOM-24 | Integration & Event Bus | Platform Intelligence & Infrastructure | BC07 | API, Event Bus, Integration, Adapter, CDC, Synchronization, Webhook | DOC:PRJ§7 | — |
| DOM-25 | Security & Governance | Platform Intelligence & Infrastructure | BC08 | Policy, Security Classification, Privacy, Compliance, Audit, Governance, Sovereignty | DOC:PRJ§7 | — |
| DOM-26 | Observability & Infrastructure | Platform Intelligence & Infrastructure | BC08 | Logging, Metrics, Tracing, Monitoring, Reliability, DR, Infrastructure, Platform Operations | DOC:PRJ§7 | — |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
bounded_contexts:
- id: BC01
  name: Foundation
  domains:
  - DOM-01
  - DOM-02
  epistemic: DOC:PRJ§8
  boundary_test: DONE W3 — see bc-boundary-test.md
- id: BC02
  name: Information
  domains:
  - DOM-03
  - DOM-04
  - DOM-05
  - DOM-06
  epistemic: DOC:PRJ§8
  boundary_test: DONE W3 — see bc-boundary-test.md
- id: BC03
  name: Intelligence & Analysis
  domains:
  - DOM-07
  - DOM-08
  - DOM-09
  epistemic: DOC:PRJ§8
  boundary_test: DONE W3 — see bc-boundary-test.md
- id: BC04
  name: Operations
  domains:
  - DOM-10
  - DOM-11
  - DOM-12
  - DOM-13
  - DOM-17
  epistemic: DOC:PRJ§8
  boundary_test: DONE W3 — see bc-boundary-test.md
- id: BC05
  name: Resources & Readiness
  domains:
  - DOM-14
  - DOM-15
  - DOM-16
  - DOM-18
  - DOM-19
  epistemic: DOC:PRJ§8
  boundary_test: DONE W3 — see bc-boundary-test.md
- id: BC06
  name: Knowledge & Products
  domains:
  - DOM-20
  - DOM-21
  - DOM-22
  epistemic: DOC:PRJ§8
  boundary_test: DONE W3 — see bc-boundary-test.md
- id: BC07
  name: Platform Intelligence
  domains:
  - DOM-23
  - DOM-24
  epistemic: DOC:PRJ§8
  boundary_test: DONE W3 — see bc-boundary-test.md
- id: BC08
  name: Governance & Runtime
  domains:
  - DOM-25
  - DOM-26
  epistemic: DOC:PRJ§8
  boundary_test: DONE W3 — see bc-boundary-test.md
domains:
- id: DOM-01
  name: Organization & Command
  group: Foundation
  bounded_context: BC01
  elements:
  - Organization
  - Organizational Unit
  - Team
  - Role
  - Responsibility
  - Authority
  - Delegation
  - Tenant
  - Workspace
  - Quota
  epistemic: DOC:PRJ§7
  note: Tenant/Workspace added (CR-41)
- id: DOM-02
  name: Identity & Access
  group: Foundation
  bounded_context: BC01
  elements:
  - Identity
  - User
  - Service Account
  - Authentication
  - Authorization
  - Access Policy
  - Device
  epistemic: DOC:PRJ§7
- id: DOM-03
  name: Information Fabric
  group: Foundation
  bounded_context: BC02
  elements:
  - Entity
  - Event
  - Relationship
  - Claim
  - Evidence
  - Provenance
  - Version
  - Metadata
  - SameAsLink
  - Conflict
  - EntityResolutionCase
  epistemic: DOC:PRJ§7
  note: ER decision objects owned here (OQ-013)
- id: DOM-04
  name: Geospatial
  group: Geospatial & Information Collection
  bounded_context: BC02
  elements:
  - Location
  - Geometry
  - CRS
  - Spatial Representation
  - Spatial Analysis
  epistemic: DOC:PRJ§7
- id: DOM-05
  name: Sources & Collection
  group: Geospatial & Information Collection
  bounded_context: BC02
  elements:
  - Source
  - Collection Requirement
  - Collection Method
  - Collection Activity
  epistemic: DOC:PRJ§7
- id: DOM-06
  name: Observation & Field
  group: Geospatial & Information Collection
  bounded_context: BC02
  elements:
  - Observation
  - Field Session
  - Measurement
  - Evidence (reference to DOM-03)
  - Offline Capture
  epistemic: DOC:PRJ§7
- id: DOM-07
  name: Intelligence
  group: Geospatial & Information Collection
  bounded_context: BC03
  elements:
  - Information Processing
  - Entity Resolution proposals
  - Correlation
  - Fusion
  - Intelligence Product
  epistemic: DOC:PRJ§7
- id: DOM-08
  name: Analysis & Assessment
  group: Analysis & Operations
  bounded_context: BC03
  elements:
  - Analysis Case
  - Analytical Question
  - Hypothesis
  - Assumption
  - Analysis Run
  - Finding
  - Assessment
  - Uncertainty
  epistemic: DOC:PRJ§7
- id: DOM-09
  name: Situation Management
  group: Analysis & Operations
  bounded_context: BC03
  elements:
  - Situation
  - Situation Member
  - Situation Change
  - Alert
  - Current Context
  epistemic: DOC:PRJ§7
- id: DOM-10
  name: Command & Coordination
  group: Analysis & Operations
  bounded_context: BC04
  elements:
  - Decision
  - Decision Request
  - Coordination Case
  - Authority check (consumes BC01)
  - Approval
  epistemic: DOC:PRJ§7
- id: DOM-11
  name: Communications
  group: Analysis & Operations
  bounded_context: BC04
  elements:
  - Communication
  - Message
  - Channel
  - Notification
  - Distribution
  epistemic: DOC:PRJ§7
- id: DOM-12
  name: Planning
  group: Planning & Execution
  bounded_context: BC04
  elements:
  - Objective
  - Outcome
  - Plan
  - Plan Version
  - Phase
  - Activity
  - Milestone
  - Baseline
  epistemic: DOC:PRJ§7
- id: DOM-13
  name: Tasks & Workflow
  group: Planning & Execution
  bounded_context: BC04
  elements:
  - Task
  - Assignment
  - Requirement
  - Dependency
  - Workflow
  - Result
  - Exception
  epistemic: DOC:PRJ§7
- id: DOM-14
  name: Assets
  group: Planning & Execution
  bounded_context: BC05
  elements:
  - Asset
  - Capability
  - Ownership
  - Custody
  - Status
  - Condition
  - Maintenance
  epistemic: DOC:PRJ§7
- id: DOM-15
  name: Resources
  group: Planning & Execution
  bounded_context: BC05
  elements:
  - Resource
  - Pool
  - Capacity
  - Availability
  - Allocation
  - Consumption
  epistemic: DOC:PRJ§7
- id: DOM-16
  name: Logistics
  group: Planning & Execution
  bounded_context: BC05
  elements:
  - Inventory
  - Shipment
  - Movement
  - Supply
  - Storage
  - Logistics Request
  epistemic: DOC:PRJ§7
- id: DOM-17
  name: Risk & Emergency
  group: Analysis & Operations
  bounded_context: BC04
  elements:
  - Risk
  - Hazard
  - Incident
  - Emergency
  - Crisis
  - Response
  - Recovery
  - Continuity
  epistemic: DOC:PRJ§7
  note: regrouped to match BC04 (CR-42)
- id: DOM-18
  name: Training & Competency
  group: Risk, Training & Knowledge
  bounded_context: BC05
  elements:
  - Competency
  - Training
  - Qualification
  - Certification
  - Readiness
  - Eligibility
  epistemic: DOC:PRJ§7
- id: DOM-19
  name: Exercises & Simulation
  group: Risk, Training & Knowledge
  bounded_context: BC05
  elements:
  - Exercise
  - Scenario
  - Simulation
  - Evaluation
  - After Action Review
  epistemic: DOC:PRJ§7
- id: DOM-20
  name: Reports & Operational Products
  group: Risk, Training & Knowledge
  bounded_context: BC06
  elements:
  - Report
  - Dashboard
  - Map Product
  - Briefing
  - Analytical Product
  epistemic: DOC:PRJ§7
- id: DOM-21
  name: Knowledge Management
  group: Risk, Training & Knowledge
  bounded_context: BC06
  elements:
  - Knowledge Object
  - Procedure
  - Policy Knowledge
  - Lesson
  - Best Practice
  - Semantic Relationships
  epistemic: DOC:PRJ§7
- id: DOM-22
  name: Archive & Institutional Memory
  group: Risk, Training & Knowledge
  bounded_context: BC06
  elements:
  - Archive Record
  - Retention
  - Legal Hold
  - Preservation
  - Historical Retrieval
  - Historical Reconstruction
  epistemic: DOC:PRJ§7
- id: DOM-23
  name: AI
  group: Platform Intelligence & Infrastructure
  bounded_context: BC07
  elements:
  - AI Request
  - AI Run
  - Context Package
  - AI Result
  - AI Review
  - AI Evaluation
  - AI Tool Registry
  epistemic: DOC:PRJ§7
- id: DOM-24
  name: Integration & Event Bus
  group: Platform Intelligence & Infrastructure
  bounded_context: BC07
  elements:
  - API
  - Event Bus
  - Integration
  - Adapter
  - CDC
  - Synchronization
  - Webhook
  epistemic: DOC:PRJ§7
- id: DOM-25
  name: Security & Governance
  group: Platform Intelligence & Infrastructure
  bounded_context: BC08
  elements:
  - Policy
  - Security Classification
  - Privacy
  - Compliance
  - Audit
  - Governance
  - Sovereignty
  epistemic: DOC:PRJ§7
- id: DOM-26
  name: Observability & Infrastructure
  group: Platform Intelligence & Infrastructure
  bounded_context: BC08
  elements:
  - Logging
  - Metrics
  - Tracing
  - Monitoring
  - Reliability
  - DR
  - Infrastructure
  - Platform Operations
  epistemic: DOC:PRJ§7
```

</details>
