---
id: SYS-STUDY-INVENTORY
type: inventory
title: Phase 1 — Global File Inventory (all spec/ markdown files)
wave: PostW9-SystemStudy
status: DRAFT
generated_by: Claude (Dynamic Engineering System Reconstruction, Phase 1)
generated_at: '2026-09-29'
notes: >
  Extracted mechanically from YAML front-matter of every .md file under spec/.
  No file content beyond front-matter was read for this pass. This is the base
  layer for Phase 2 (Entity Index) and all later Reverse Discovery passes.
---

# Phase 1 — Global File Inventory

مصدر الحقيقة: 705 ملف `.md` تحت `spec/`. هذا الفهرس آلي بالكامل (لا قراءة تحليلية)، ويغطي كل ملف بحقول الـfront-matter الخاصة به.

## 1. إحصاءات عامة

- **إجمالي الملفات:** 705
- **ملفات بلا `id`/front-matter صالح:** 2 (`spec/README.md`, `spec/11-integration/README.md` — ملفات فهرسة عادية، متوقّع)

## 2. التوزيع حسب المجلد الرئيسي (recursive)

| المجلد | عدد الملفات | الملاحظة |
|---|---|---|
| 00-governance | 28 | حوكمة: ADRs, registers, elicitation |
| 01-business | 9 | capabilities, business-rules, stakeholders... |
| 02-requirements | 3 | requirements, use-cases, quality-scenarios |
| 03-domain | 194 | **الأكبر** — BC01..BC08 (aggregates+commands+events+queries) |
| 04-information | 13 | |
| 05-contracts | 66 | OpenAPI/AsyncAPI/errors لكل شريحة |
| 06-data | 19 | logical-model |
| 07-quality | 23 | workloads, quality scenarios |
| 08-security | 47 | policies, threat-model, classification |
| 09-reliability | 41 | FMEA, degradation, observability |
| 10-ai | 1 | |
| 11-integration | 1 | |
| 12-solution | 8 | architecture |
| 13-verification | 131 | **ثاني الأكبر** — acceptance specs لكل aggregate |
| 14-slices | 39 | readiness لكل شريحة |
| 15-traceability | 23 | RTM لكل شريحة |
| 16-reports | 58 | session reports, consistency checks |

## 3. التوزيع حسب Bounded Context (من مجلد 03-domain/contexts)

| BC | عدد الملفات | من حقل bounded_context (front-matter) |
|---|---|---|
| BC01 | 21 | 11 |
| BC02 | 35 | 18 |
| BC03 | 20 | 9 |
| BC04 | 30 | 12 |
| BC05 | 29 | 13 |
| BC06 | 10 | 6 |
| BC07 | 32 | 13 |
| BC08 | 13 | 7 |

**ملاحظة [Explicit]:** عمود "من حقل bounded_context" أقل من عدد ملفات المجلد لكل BC لأن هذا الحقل موجود فقط في ملفات `aggregates/*.md`، بينما commands/events/queries-slc*.md لا تحمل الحقل صراحة (BC مُستدل من المسار فقط) — **هذه فجوة توثيقية صغيرة تُسجَّل [Missing]، وليست خطأ استخراج.**

## 4. التوزيع حسب نوع المستند (type:) — أعلى 15

| type | العدد |
|---|---|
| acceptance-spec | 108 |
| aggregate | 89 |
| api-contract | 28 |
| session-report | 27 |
| query-catalog | 27 |
| event-catalog | 27 |
| command-catalog | 27 |
| traceability-matrix | 23 |
| architecture-review | 22 |
| workload-catalog | 20 |
| threat-model | 20 |
| slice-readiness | 19 |
| property-spec | 19 |
| policy-decision-tables | 19 |
| observability | 19 |
| logical-data-model | 19 |
| fmea | 19 |
| event-contract | 19 |
| error-catalog | 19 |
| component-specification | 19 |
| ... +45 نوعًا آخر (1-16 ملفًا لكل نوع) | — انظر الجدول الكامل أدناه |

**89 aggregate هو الرقم الأهم عمليًا** — هذا يعني وجود ~89 "ميزة" على مستوى Aggregate عبر 8 BCs، مقارنة بالميزتين اللتين درسناهما بعمق (Authority Grant, Clearance). إذا استغرقت كل ميزة نفس عمق Reverse Discovery، فهذا يعني نطاقًا يعادل ~44 ضعف ما أنجزناه حتى الآن.

## 5. التوزيع حسب الحالة (status)

| status | العدد |
|---|---|
| APPROVED_DELEGATED | 574 |
| DRAFT | 52 |
| (فارغ) | 29 |
| GENERATED | 23 |
| FINAL (delegated) | 7 |
| DESIGN_COMPLETE — G6 HELD (متغيرات متعددة، RSK-027/028) | 9 |
| RATIFIED | 2 |
| أخرى (PROPOSED/OPEN/BASELINED/...) | 9 |

**ملاحظة مهمة [Explicit]:** 9 ملفات بحالة `DESIGN_COMPLETE — G6 HELD` — أي أنها **مصممة لكن معلّقة رسميًا** بانتظار مراجعة تجريبية (R1/R2 pilot review) أو معرفة أنظمة المستأجر (UNK-021). هذه ملفات **لا يجب اعتبارها "جاهزة نهائيًا"** عند بناء الدراسة النهائية — يجب تمييزها بوضوح.

## 6. الفهرس الكامل (705 صف)

| path | id | type | title | wave | tier | status | bounded_context |
|---|---|---|---|---|---|---|---|
| spec/00-governance/RATIFICATION-PACKAGE.md | RATIFICATION-PACKAGE | decision-register | Ratification Package — all delegated decisions awaiting the project owner | W9 |  | RATIFIED |  |
| spec/00-governance/decisions/ADR-P01.md | ADR-P01 | adr | Temporal Model | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P02.md | ADR-P02 | adr | Persistence Style | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P03.md | ADR-P03 | adr | Importance Tiers | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P04.md | ADR-P04 | adr | Tenant Isolation | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P05.md | ADR-P05 | adr | Initial Technology Footprint | W8 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P06.md | ADR-P06 | adr | Security Inside Projections | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P07.md | ADR-P07 | adr | Nature of Situation | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P08.md | ADR-P08 | adr | Erasure vs Immutability | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P09.md | ADR-P09 | adr | Field Synchronization | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P10.md | ADR-P10 | adr | Autonomy Level Naming (AIL vs DAL) | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P11.md | ADR-P11 | adr | Policy Engine & Representation | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P12.md | ADR-P12 | adr | Map Serving & Tile Security | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P13.md | ADR-P13 | adr | Identifiers | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P14.md | ADR-P14 | adr | Reference Data Governance | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P15.md | ADR-P15 | adr | Language & Entity Matching | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/decisions/ADR-P16.md | ADR-P16 | adr | Canonical CRS | W3 |  | APPROVED_DELEGATED |  |
| spec/00-governance/elicitation/W1-answers.md | W1-ELICITATION | elicitation-form |  | W1-a |  | ANSWERED (DELEGATED DECISIONS) |  |
| spec/00-governance/elicitation/W1-questions.md | W1-ELICITATION | elicitation-form |  | W1-a |  | OPEN |  |
| spec/00-governance/glossary.md | GLOSSARY | glossary | Glossary (AR/EN) — binding | W0 | T0 | DRAFT |  |
| spec/00-governance/registers/assumptions.md | REG-ASM | register | Assumption Register | W0 | T3 | DRAFT |  |
| spec/00-governance/registers/corrections.md | REG-CR | register | Baseline Corrections Register | W0 | T3 | DRAFT |  |
| spec/00-governance/registers/dependencies.md | REG-DEP | register | Dependency Register | W0 | T3 | DRAFT |  |
| spec/00-governance/registers/human-approvals.md | REG-HAP | register | Human Approval Register | W0 | T3 | DRAFT |  |
| spec/00-governance/registers/open-questions.md | REG-OQ | register | Open Questions | W0 | T3 | DRAFT |  |
| spec/00-governance/registers/risks.md | REG-RSK | register | Risk Register | W0 | T3 | DRAFT |  |
| spec/00-governance/registers/technical-debt.md | REG-DEBT | register | Technical Debt Register | W0 | T3 | DRAFT |  |
| spec/00-governance/registers/unknowns.md | REG-UNK | register | Unknown Register | W0 | T3 | DRAFT |  |
| spec/01-business/business-rules.md | BRL | business-rules | Business Rules Catalog (BRL) — corrected | W2 | T0 | APPROVED_DELEGATED |  |
| spec/01-business/capabilities.md | CAP-MAP | capability-map | Capability Map (L1/L2) | W1 | T0 | APPROVED_DELEGATED |  |
| spec/01-business/outcomes.md | OUTCOMES | outcomes | Business Outcomes | W1 | T0 | APPROVED_DELEGATED |  |
| spec/01-business/processes.md | PROCESSES | processes | Business Processes (catalog) | W0 | T0 | DRAFT |  |
| spec/01-business/release-2-scope.md | R2-SCOPE | release-scope | Release 2 — Scope, Slices and Delegated Decisions (W1/W2-R2) | W1/W2-R2 |  | APPROVED_DELEGATED |  |
| spec/01-business/release-3-scope.md | R3-SCOPE | release-scope | Release 3 — Scope, Slices and Delegated Decisions (W1/W2-R3) | W1/W2-R3 |  | APPROVED_DELEGATED (scope §§1-2/4-5 as of 2026-09-27; all three R3 slices DESIGN COMPLETE as of 2026-09-29 — see §2) |  |
| spec/01-business/stakeholders.md | STK | stakeholder-model | Stakeholder Model (loaded — incomplete) | W1 | T0 | APPROVED_DELEGATED |  |
| spec/01-business/system-definition.md | SYSDEF | system-definition |  | W1 |  | APPROVED_DELEGATED |  |
| spec/01-business/value-streams.md | VALUE-STREAMS | value-streams | Value Streams | W0 | T0 | DRAFT |  |
| spec/02-requirements/quality-scenarios.md | QAS-CAT | quality-scenarios | Quality Attribute Scenarios — R1 | W2 | T0 | APPROVED_DELEGATED |  |
| spec/02-requirements/requirements.md | REQ-BASELINE | requirements | Requirements Baseline — R1 (baselined) + R2 (W2-R2) | W2 | T0 | APPROVED_DELEGATED |  |
| spec/02-requirements/use-cases.md | UC-CAT | use-case-catalog | Use Case Catalog | W2 | T0 | APPROVED_DELEGATED |  |
| spec/03-domain/bc-boundary-test.md | BC-BOUNDARY-TEST | architecture-review | Bounded Context Boundary Test (V5§9 — 10 criteria) | W3 | T0 | APPROVED_DELEGATED |  |
| spec/03-domain/context-map.md | CONTEXT-MAP | context-map | Bounded Context Map | W3 | T0 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md | AGG-AUTHORITY-GRANT | aggregate | Authority Grant (incl. delegation) | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md | AGG-CLEARANCE | aggregate | Clearance | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/aggregates/AGG-DEVICE.md | AGG-DEVICE | aggregate | Field Device | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md | AGG-HR-SYNC-PROPOSAL | aggregate | HR Sync Proposal | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md | AGG-ORGANIZATION | aggregate | Organization (with unit tree) | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/aggregates/AGG-PERSON.md | AGG-PERSON | aggregate | Person | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md | AGG-ROLE-ASSIGNMENT | aggregate | Role Assignment | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/aggregates/AGG-ROLE.md | AGG-ROLE | aggregate | Role | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md | AGG-SERVICE-ACCOUNT | aggregate | Service Account | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/aggregates/AGG-TENANT.md | AGG-TENANT | aggregate | Tenant | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/aggregates/AGG-USER.md | AGG-USER | aggregate | User Account | W4 | T1 | APPROVED_DELEGATED | BC01 |
| spec/03-domain/contexts/BC01/commands-slc01.md | CMD-CAT-BC01-SLC01 | command-catalog | Commands — BC01 (SLC-01) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC01/commands-slc11.md | CMD-CAT-BC01-SLC11 | command-catalog | Commands — BC01 (SLC-11) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC01/commands-slc16.md | CMD-CAT-BC01-SLC16 | command-catalog | Commands — BC01 (SLC-16) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC01/events-slc01.md | EVT-CAT-BC01-SLC01 | event-catalog | Domain Events — BC01 (SLC-01) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC01/events-slc11.md | EVT-CAT-BC01-SLC11 | event-catalog | Domain Events — BC01 (SLC-11) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC01/events-slc16.md | EVT-CAT-BC01-SLC16 | event-catalog | Domain Events — BC01 (SLC-16) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC01/queries-slc01.md | QRY-CAT-BC01-SLC01 | query-catalog | Queries — BC01 (SLC-01) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC01/queries-slc11.md | QRY-CAT-BC01-SLC11 | query-catalog | Queries — BC01 (SLC-11) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC01/queries-slc16.md | QRY-CAT-BC01-SLC16 | query-catalog | Queries — BC01 (SLC-16) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC01/security-context.md | PL-SECURITY-CONTEXT | published-language | SecurityContext (Published Language of BC01) | W4 | T0 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md | AGG-ATTACHMENT | aggregate | Attachment | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-CLAIM.md | AGG-CLAIM | aggregate | Claim | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md | AGG-COLLECTION-PLAN | aggregate | Collection Plan | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md | AGG-COLLECTION-REQUIREMENT | aggregate | Collection Requirement | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md | AGG-CONFLICT | aggregate | Conflict | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md | AGG-CORRELATION-PROPOSAL | aggregate | Correlation Proposal | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md | AGG-CORRELATION-RULE | aggregate | Correlation Rule | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-ENTITY.md | AGG-ENTITY | aggregate | Entity (identity) | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md | AGG-ER-CASE | aggregate | Entity Resolution Case | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md | AGG-EVIDENCE-LINK | aggregate | Evidence Link | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md | AGG-EVIDENCE | aggregate | Evidence | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md | AGG-EXTERNAL-ID | aggregate | External Identifier Mapping | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md | AGG-IMPORT-BATCH | aggregate | Import Batch | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md | AGG-MATCH-RULESET | aggregate | Match Ruleset | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md | AGG-OBSERVATION | aggregate | Observation | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md | AGG-REALWORLD-EVENT | aggregate | Real-World Event (identity) | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md | AGG-RELATIONSHIP | aggregate | Relationship (identity) | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/aggregates/AGG-SOURCE.md | AGG-SOURCE | aggregate | Source | W4 | T1 | APPROVED_DELEGATED | BC02 |
| spec/03-domain/contexts/BC02/candidate-generation.md | SPEC-ER-CANDIDATES | component-specification | Entity Resolution Candidate Generation | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/claims-temporal-kernel.md | LIB-CLAIMS-KERNEL | library-specification | Claims & Temporal Kernel — shared library specification | W4 | T0 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/collection-spec.md | SPEC-COLLECTION | component-specification | Collection Requirements — EEIs, Matching Engine, Viewer-Scoped Fulfilment, Tasking | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/commands-slc02.md | CMD-CAT-BC02-SLC02 | command-catalog | Commands — BC02 (SLC-02) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/commands-slc04.md | CMD-CAT-BC02-SLC04 | command-catalog | Commands — BC02 (SLC-04) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/commands-slc14.md | CMD-CAT-BC02-SLC14 | command-catalog | Commands — BC02 (SLC-14) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/commands-slc15.md | CMD-CAT-BC02-SLC15 | command-catalog | Commands — BC02 (SLC-15) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/conflict-detection-engine.md | SPEC-CONFLICT-DETECTION | component-specification | Conflict Detection Engine | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/correlation-fusion-spec.md | SPEC-FUSION | component-specification | Coordination Scoping, Correlation Engine and Fusion Rules | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/events-slc02.md | EVT-CAT-BC02-SLC02 | event-catalog | Domain Events — BC02 (SLC-02) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/events-slc04.md | EVT-CAT-BC02-SLC04 | event-catalog | Domain Events — BC02 (SLC-04) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/events-slc14.md | EVT-CAT-BC02-SLC14 | event-catalog | Domain Events — BC02 (SLC-14) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/events-slc15.md | EVT-CAT-BC02-SLC15 | event-catalog | Domain Events — BC02 (SLC-15) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/queries-slc02.md | QRY-CAT-BC02-SLC02 | query-catalog | Queries — BC02 (SLC-02) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/queries-slc04.md | QRY-CAT-BC02-SLC04 | query-catalog | Queries — BC02 (SLC-04) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/queries-slc14.md | QRY-CAT-BC02-SLC14 | query-catalog | Queries — BC02 (SLC-14) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC02/queries-slc15.md | QRY-CAT-BC02-SLC15 | query-catalog | Queries — BC02 (SLC-15) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md | AGG-ALERT-RULE | aggregate | Alert Rule | W4 | T1 | APPROVED_DELEGATED | BC03 |
| spec/03-domain/contexts/BC03/aggregates/AGG-ALERT.md | AGG-ALERT | aggregate | Alert | W4 | T1 | APPROVED_DELEGATED | BC03 |
| spec/03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md | AGG-ANALYSIS-CASE | aggregate | Analysis Case | W4 | T1 | APPROVED_DELEGATED | BC03 |
| spec/03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md | AGG-ANALYSIS-METHOD | aggregate | Analysis Method Version | W4 | T1 | APPROVED_DELEGATED | BC03 |
| spec/03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md | AGG-ANALYSIS-RUN | aggregate | Analysis Run | W4 | T1 | APPROVED_DELEGATED | BC03 |
| spec/03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md | AGG-ASSESSMENT | aggregate | Assessment Version | W4 | T1 | APPROVED_DELEGATED | BC03 |
| spec/03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md | AGG-CAP-MESSAGE | aggregate | CAP Message (outbound) | W4 | T1 | APPROVED_DELEGATED | BC03 |
| spec/03-domain/contexts/BC03/aggregates/AGG-FINDING.md | AGG-FINDING | aggregate | Finding | W4 | T1 | APPROVED_DELEGATED | BC03 |
| spec/03-domain/contexts/BC03/aggregates/AGG-SITUATION.md | AGG-SITUATION | aggregate | Situation | W4 | T1 | APPROVED_DELEGATED | BC03 |
| spec/03-domain/contexts/BC03/analysis-reproducibility-spec.md | SPEC-ANALYSIS | component-specification | Analytical Work — Reproducibility, Execution, Estimative Language, Citations | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/commands-slc06.md | CMD-CAT-BC03-SLC06 | command-catalog | Commands — BC03 (SLC-06) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/commands-slc07.md | CMD-CAT-BC03-SLC07 | command-catalog | Commands — BC03 (SLC-07) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/commands-slc16.md | CMD-CAT-BC03-SLC16 | command-catalog | Commands — BC03 (SLC-16) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/events-slc06.md | EVT-CAT-BC03-SLC06 | event-catalog | Domain Events — BC03 (SLC-06) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/events-slc07.md | EVT-CAT-BC03-SLC07 | event-catalog | Domain Events — BC03 (SLC-07) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/events-slc16.md | EVT-CAT-BC03-SLC16 | event-catalog | Domain Events — BC03 (SLC-16) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/queries-slc06.md | QRY-CAT-BC03-SLC06 | query-catalog | Queries — BC03 (SLC-06) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/queries-slc07.md | QRY-CAT-BC03-SLC07 | query-catalog | Queries — BC03 (SLC-07) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/queries-slc16.md | QRY-CAT-BC03-SLC16 | query-catalog | Queries — BC03 (SLC-16) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC03/situation-alerting-spec.md | SPEC-SITUATION | component-specification | Situation Membership, Alert Evaluation, COP & Secured Tiles, Notification Delivery | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md | AGG-COORDINATION-CASE | aggregate | Coordination Case | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md | AGG-DECISION-REQUEST | aggregate | Decision Request | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-DECISION.md | AGG-DECISION | aggregate | Decision | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md | AGG-INCIDENT | aggregate | Incident | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md | AGG-NOTIFICATION | aggregate | Notification | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md | AGG-OUTCOME-TRACKER | aggregate | Outcome Tracker | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md | AGG-PLAN-VERSION | aggregate | Plan Version | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-PLAN.md | AGG-PLAN | aggregate | Plan (identity) | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-RISK.md | AGG-RISK | aggregate | Risk | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md | AGG-SUBSCRIPTION | aggregate | Subscription | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md | AGG-TASK-TYPE | aggregate | Task Type | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/aggregates/AGG-TASK.md | AGG-TASK | aggregate | Task | W4 | T1 | APPROVED_DELEGATED | BC04 |
| spec/03-domain/contexts/BC04/commands-slc03.md | CMD-CAT-BC04-SLC03 | command-catalog | Commands — BC04 (SLC-03) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/commands-slc06.md | CMD-CAT-BC04-SLC06 | command-catalog | Commands — BC04 (SLC-06) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/commands-slc08.md | CMD-CAT-BC04-SLC08 | command-catalog | Commands — BC04 (SLC-08) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/commands-slc15.md | CMD-CAT-BC04-SLC15 | command-catalog | Commands — BC04 (SLC-15) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/commands-slc17.md | CMD-CAT-BC04-SLC17 | command-catalog | Commands — BC04 (SLC-17) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/decision-plan-spec.md | SPEC-PLAN | component-specification | Decision Basis, Change Classification, Task Synchronization, Outcome Progress | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/events-slc03.md | EVT-CAT-BC04-SLC03 | event-catalog | Domain Events — BC04 (SLC-03) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/events-slc06.md | EVT-CAT-BC04-SLC06 | event-catalog | Domain Events — BC04 (SLC-06) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/events-slc08.md | EVT-CAT-BC04-SLC08 | event-catalog | Domain Events — BC04 (SLC-08) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/events-slc15.md | EVT-CAT-BC04-SLC15 | event-catalog | Domain Events — BC04 (SLC-15) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/events-slc17.md | EVT-CAT-BC04-SLC17 | event-catalog | Domain Events — BC04 (SLC-17) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/queries-slc03.md | QRY-CAT-BC04-SLC03 | query-catalog | Queries — BC04 (SLC-03) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/queries-slc06.md | QRY-CAT-BC04-SLC06 | query-catalog | Queries — BC04 (SLC-06) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/queries-slc08.md | QRY-CAT-BC04-SLC08 | query-catalog | Queries — BC04 (SLC-08) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/queries-slc15.md | QRY-CAT-BC04-SLC15 | query-catalog | Queries — BC04 (SLC-15) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/queries-slc17.md | QRY-CAT-BC04-SLC17 | query-catalog | Queries — BC04 (SLC-17) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/risk-contingency-spec.md | SPEC-RISK-CONTINGENCY | component-specification | Risk & Contingency Rules — hazard catalog, severity, reuse of Plan/Task | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC04/task-lifecycle-rules.md | SPEC-TASK-RULES | component-specification | Task Lifecycle Rules — decisions, criteria evaluation, scheduling, offline | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md | AGG-ALLOCATION | aggregate | Resource Allocation | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md | AGG-ASSET-ASSIGNMENT | aggregate | Asset Assignment | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md | AGG-ASSET-RESERVATION | aggregate | Asset Reservation | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-ASSET.md | AGG-ASSET | aggregate | Asset | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md | AGG-EXERCISE | aggregate | Exercise | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md | AGG-LOGISTICS-REQUEST | aggregate | Logistics Request | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md | AGG-MAINTENANCE-ORDER | aggregate | Maintenance Order | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md | AGG-QUALIFICATION-RECORD | aggregate | Qualification Record | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md | AGG-RESOURCE-POOL | aggregate | Resource Pool | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md | AGG-ROLE-REQUIREMENT | aggregate | Role Requirement | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md | AGG-SCENARIO | aggregate | Scenario | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md | AGG-SHIPMENT | aggregate | Shipment | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md | AGG-SIMULATION | aggregate | Simulation | W4 | T1 | APPROVED_DELEGATED | BC05 |
| spec/03-domain/contexts/BC05/allocation-readiness-spec.md | SPEC-ALLOCATION | component-specification | Allocation Checks, Capacity Ledger, Contention, Pre-emption, Availability & Readiness | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/commands-slc03.md | CMD-CAT-BC05-SLC03 | command-catalog | Commands — BC05 (SLC-03) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/commands-slc09.md | CMD-CAT-BC05-SLC09 | command-catalog | Commands — BC05 (SLC-09) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/commands-slc18.md | CMD-CAT-BC05-SLC18 | command-catalog | Commands — BC05 (SLC-18) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/commands-slc19.md | CMD-CAT-BC05-SLC19 | command-catalog | Commands — BC05 (SLC-19) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/eligibility-rules.md | SPEC-ELIGIBILITY | component-specification | Eligibility Evaluation (R1) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/events-slc03.md | EVT-CAT-BC05-SLC03 | event-catalog | Domain Events — BC05 (SLC-03) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/events-slc09.md | EVT-CAT-BC05-SLC09 | event-catalog | Domain Events — BC05 (SLC-09) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/events-slc18.md | EVT-CAT-BC05-SLC18 | event-catalog | Domain Events — BC05 (SLC-18) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/events-slc19.md | EVT-CAT-BC05-SLC19 | event-catalog | Domain Events — BC05 (SLC-19) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/logistics-spec.md | SPEC-LOGISTICS | component-specification | Logistics & Supply Rules — item catalog, reuse of Resource Pool/Allocation, movement | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/queries-slc03.md | QRY-CAT-BC05-SLC03 | query-catalog | Queries — BC05 (SLC-03) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/queries-slc09.md | QRY-CAT-BC05-SLC09 | query-catalog | Queries — BC05 (SLC-09) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/queries-slc18.md | QRY-CAT-BC05-SLC18 | query-catalog | Queries — BC05 (SLC-18) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/queries-slc19.md | QRY-CAT-BC05-SLC19 | query-catalog | Queries — BC05 (SLC-19) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC05/training-exercise-spec.md | SPEC-TRAINING-EXERCISE | component-specification | Training, Competency & Exercises Rules — reuse of Qualification Record/Role Requirement, Scenario/Exercise/Simulation, After Action Review | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md | AGG-ARCHIVE-PACKAGE | aggregate | Archive Package (AIP) | W4 | T1 | APPROVED_DELEGATED | BC06 |
| spec/03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md | AGG-DISTRIBUTION | aggregate | Distribution | W4 | T1 | APPROVED_DELEGATED | BC06 |
| spec/03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md | AGG-KNOWLEDGE-OBJECT | aggregate | Knowledge Object Version | W4 | T1 | APPROVED_DELEGATED | BC06 |
| spec/03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md | AGG-PRODUCT-TEMPLATE | aggregate | Product Template | W4 | T1 | APPROVED_DELEGATED | BC06 |
| spec/03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md | AGG-PRODUCT | aggregate | Product Version | W4 | T1 | APPROVED_DELEGATED | BC06 |
| spec/03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md | AGG-RECONSTRUCTION | aggregate | Historical Reconstruction | W4 | T1 | APPROVED_DELEGATED | BC06 |
| spec/03-domain/contexts/BC06/commands-slc12.md | CMD-CAT-BC06-SLC12 | command-catalog | Commands — BC06 (SLC-12) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC06/events-slc12.md | EVT-CAT-BC06-SLC12 | event-catalog | Domain Events — BC06 (SLC-12) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC06/products-knowledge-archive-spec.md | SPEC-PKA | component-specification | Product Generation, Distribution, Knowledge Suggestion, Archive Packages, Historical Reconstruction | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC06/queries-slc12.md | QRY-CAT-BC06-SLC12 | query-catalog | Queries — BC06 (SLC-12) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md | AGG-ADAPTER | aggregate | Adapter | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md | AGG-AI-REQUEST | aggregate | AI Request | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md | AGG-AI-RESULT | aggregate | AI Result (reviewable) | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md | AGG-AI-ROUTING | aggregate | AI Routing Configuration | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md | AGG-AI-TOOL | aggregate | AI Tool | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md | AGG-EVAL-SUITE | aggregate | Evaluation Suite | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md | AGG-INTEGRATION-CONNECTION | aggregate | Integration Connection | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md | AGG-MODEL-VERSION | aggregate | Model Version | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md | AGG-PRELOAD-PACKAGE | aggregate | Preload Package | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md | AGG-PROJECTION-VERSION | aggregate | Projection Version | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md | AGG-SENSOR-STREAM | aggregate | Sensor Stream | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md | AGG-SYNC-CONFLICT | aggregate | Sync Conflict | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md | AGG-SYNC-SESSION | aggregate | Sync Session | W4 | T1 | APPROVED_DELEGATED | BC07 |
| spec/03-domain/contexts/BC07/commands-slc02.md | CMD-CAT-BC07-SLC02 | command-catalog | Commands — BC07 (SLC-02) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/commands-slc05.md | CMD-CAT-BC07-SLC05 | command-catalog | Commands — BC07 (SLC-05) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/commands-slc10.md | CMD-CAT-BC07-SLC10 | command-catalog | Commands — BC07 (SLC-10) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/commands-slc11.md | CMD-CAT-BC07-SLC11 | command-catalog | Commands — BC07 (SLC-11) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/commands-slc16.md | CMD-CAT-BC07-SLC16 | command-catalog | Commands — BC07 (SLC-16) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/discovery-architecture.md | SPEC-DISCOVERY | component-specification | Discovery — Secured Search & Graph Projections | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/enterprise-integration-spec.md | SPEC-INTEGRATION | component-specification | Enterprise Integrations — patterns per system kind, sensors, HR proposals, CAP release | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/events-slc02.md | EVT-CAT-BC07-SLC02 | event-catalog | Domain Events — BC07 (SLC-02) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/events-slc05.md | EVT-CAT-BC07-SLC05 | event-catalog | Domain Events — BC07 (SLC-05) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/events-slc10.md | EVT-CAT-BC07-SLC10 | event-catalog | Domain Events — BC07 (SLC-10) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/events-slc11.md | EVT-CAT-BC07-SLC11 | event-catalog | Domain Events — BC07 (SLC-11) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/events-slc16.md | EVT-CAT-BC07-SLC16 | event-catalog | Domain Events — BC07 (SLC-16) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/field-sync-protocol.md | SPEC-FIELD-SYNC | component-specification | Field Synchronization Protocol (ADR-P09) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/grounded-ai-spec.md | SPEC-AI | component-specification | Grounded AI — pipeline, authorized retrieval, context packages, grounding, guards, serving | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/queries-slc02.md | QRY-CAT-BC07-SLC02 | query-catalog | Queries — BC07 (SLC-02) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/queries-slc05.md | QRY-CAT-BC07-SLC05 | query-catalog | Queries — BC07 (SLC-05) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/queries-slc10.md | QRY-CAT-BC07-SLC10 | query-catalog | Queries — BC07 (SLC-10) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/queries-slc11.md | QRY-CAT-BC07-SLC11 | query-catalog | Queries — BC07 (SLC-11) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC07/queries-slc16.md | QRY-CAT-BC07-SLC16 | query-catalog | Queries — BC07 (SLC-16) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md | AGG-CLASSIFICATION-SCHEME | aggregate | Classification Scheme Version | W4 | T1 | APPROVED_DELEGATED | BC08 |
| spec/03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md | AGG-DISPOSITION-RUN | aggregate | Disposition Run | W4 | T1 | APPROVED_DELEGATED | BC08 |
| spec/03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md | AGG-ERASURE-REQUEST | aggregate | Erasure Request | W4 | T1 | APPROVED_DELEGATED | BC08 |
| spec/03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md | AGG-LEGAL-HOLD | aggregate | Legal Hold | W4 | T1 | APPROVED_DELEGATED | BC08 |
| spec/03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md | AGG-POLICY-SET | aggregate | Policy Set Version | W4 | T1 | APPROVED_DELEGATED | BC08 |
| spec/03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md | AGG-RETENTION-SCHEDULE | aggregate | Retention Schedule Version | W4 | T1 | APPROVED_DELEGATED | BC08 |
| spec/03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md | AGG-SECURITY-EXCEPTION | aggregate | Security Exception | W4 | T1 | APPROVED_DELEGATED | BC08 |
| spec/03-domain/contexts/BC08/commands-slc01.md | CMD-CAT-BC08-SLC01 | command-catalog | Commands — BC08 (SLC-01) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC08/commands-slc12a.md | CMD-CAT-BC08-SLC12A | command-catalog | Commands — BC08 (SLC-12a) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC08/events-slc01.md | EVT-CAT-BC08-SLC01 | event-catalog | Domain Events — BC08 (SLC-01) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC08/events-slc12a.md | EVT-CAT-BC08-SLC12A | event-catalog | Domain Events — BC08 (SLC-12a) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC08/queries-slc01.md | QRY-CAT-BC08-SLC01 | query-catalog | Queries — BC08 (SLC-01) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/contexts/BC08/queries-slc12a.md | QRY-CAT-BC08-SLC12A | query-catalog | Queries — BC08 (SLC-12a) | W4 | T1 | APPROVED_DELEGATED |  |
| spec/03-domain/domains.md | DOMAINS | domain-model | Domains (26) and Bounded Context assignment | W3 | T0 | APPROVED_DELEGATED |  |
| spec/03-domain/ownership.md | OWNERSHIP | ownership-model | Domain Ownership Model | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/business-objects-kernel.md | BO-CATALOG-KERNEL | business-object-catalog | Business Object Catalog — Information Kernel (BC02) | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/claim-evidence-model.md | CLAIM-EVIDENCE-MODEL | information-model | Claim, Evidence, Source & Observation Model | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/confidence-model.md | CONFIDENCE-MODEL | information-model | Confidence Model (7 dimensions) | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/conflict-model.md | CONFLICT-MODEL | information-model | Conflict Model | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/entity-resolution.md | ER-MODEL | information-model | Entity Resolution (merge / split without id rewrite) | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/importance-tiers.md | IMPORTANCE-TIERS | importance-tiers | Importance Tier Model (ADR-P03) | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/language-model.md | LANGUAGE-MODEL | information-model | Language, Names & Transliteration Model | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/meta-model.md | META-MODEL | information-model | Canonical Meta-Model | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/object-envelope.md | OBJECT-ENVELOPE | schema | Object Envelope v1 (corrected) | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/provenance-lineage.md | PROVENANCE-LINEAGE | architecture | Provenance & Lineage | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/reference-data.md | REFERENCE-DATA | reference-data | Reference Data Catalog (ADR-P14) | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/spatial-model.md | SPATIAL-MODEL | architecture | Spatial Architecture | W3 | T0 | APPROVED_DELEGATED |  |
| spec/04-information/temporal-model.md | TEMPORAL-MODEL | architecture | Temporal Architecture | W3 | T0 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc01.md | ASYNCAPI-SLC01 | event-contract | AsyncAPI — SLC-01 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc02.md | ASYNCAPI-SLC02 | event-contract | AsyncAPI — SLC-02 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc03.md | ASYNCAPI-SLC03 | event-contract | AsyncAPI — SLC-03 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc04.md | ASYNCAPI-SLC04 | event-contract | AsyncAPI — SLC-04 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc05.md | ASYNCAPI-SLC05 | event-contract | AsyncAPI — SLC-05 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc06.md | ASYNCAPI-SLC06 | event-contract | AsyncAPI — SLC-06 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc07.md | ASYNCAPI-SLC07 | event-contract | AsyncAPI — SLC-07 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc08.md | ASYNCAPI-SLC08 | event-contract | AsyncAPI — SLC-08 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc09.md | ASYNCAPI-SLC09 | event-contract | AsyncAPI — SLC-09 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc10.md | ASYNCAPI-SLC10 | event-contract | AsyncAPI — SLC-10 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc11.md | ASYNCAPI-SLC11 | event-contract | AsyncAPI — SLC-11 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc12.md | ASYNCAPI-SLC12 | event-contract | AsyncAPI — SLC-12 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc12a.md | ASYNCAPI-SLC12A | event-contract | AsyncAPI — SLC-12a Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc14.md | ASYNCAPI-SLC14 | event-contract | AsyncAPI — SLC-14 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc15.md | ASYNCAPI-SLC15 | event-contract | AsyncAPI — SLC-15 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc16.md | ASYNCAPI-SLC16 | event-contract | AsyncAPI — SLC-16 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc17.md | ASYNCAPI-SLC17 | event-contract | AsyncAPI — SLC-17 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc18.md | ASYNCAPI-SLC18 | event-contract | AsyncAPI — SLC-18 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/asyncapi-slc19.md | ASYNCAPI-SLC19 | event-contract | AsyncAPI — SLC-19 Domain Events | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc01.md | ERRORS-SLC01 | error-catalog | Error Catalog — SLC-01 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc02.md | ERRORS-SLC02 | error-catalog | Error Catalog — SLC-02 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc03.md | ERRORS-SLC03 | error-catalog | Error Catalog — SLC-03 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc04.md | ERRORS-SLC04 | error-catalog | Error Catalog — SLC-04 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc05.md | ERRORS-SLC05 | error-catalog | Error Catalog — SLC-05 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc06.md | ERRORS-SLC06 | error-catalog | Error Catalog — SLC-06 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc07.md | ERRORS-SLC07 | error-catalog | Error Catalog — SLC-07 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc08.md | ERRORS-SLC08 | error-catalog | Error Catalog — SLC-08 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc09.md | ERRORS-SLC09 | error-catalog | Error Catalog — SLC-09 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc10.md | ERRORS-SLC10 | error-catalog | Error Catalog — SLC-10 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc11.md | ERRORS-SLC11 | error-catalog | Error Catalog — SLC-11 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc12.md | ERRORS-SLC12 | error-catalog | Error Catalog — SLC-12 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc12a.md | ERRORS-SLC12A | error-catalog | Error Catalog — SLC-12a | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc14.md | ERRORS-SLC14 | error-catalog | Error Catalog — SLC-14 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc15.md | ERRORS-SLC15 | error-catalog | Error Catalog — SLC-15 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc16.md | ERRORS-SLC16 | error-catalog | Error Catalog — SLC-16 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc17.md | ERRORS-SLC17 | error-catalog | Error Catalog — SLC-17 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc18.md | ERRORS-SLC18 | error-catalog | Error Catalog — SLC-18 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/errors-slc19.md | ERRORS-SLC19 | error-catalog | Error Catalog — SLC-19 | W6 |  | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-ai-slc10.md | OPENAPI-BC07-SLC10 | api-contract | AI API (BC07) — SLC-10 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-discovery-slc05.md | OPENAPI-BC07-SLC05 | api-contract | Discovery API (BC07) — SLC-05 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-field-slc11.md | OPENAPI-BC07-SLC11 | api-contract | Field API (BC07) — SLC-11 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-foundation-internal-slc01.md | OPENAPI-BC01-INTERNAL | api-contract | Foundation Internal API — system commands (SLC-01) | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-foundation-slc01.md | OPENAPI-BC01-SLC01 | api-contract | Foundation API (BC01) — SLC-01 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-foundation-slc11.md | OPENAPI-BC01-SLC11 | api-contract | Foundation API (BC01) — SLC-11 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-foundation-slc16.md | OPENAPI-BC01-SLC16 | api-contract | Foundation API (BC01) — SLC-16 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-governance-slc01.md | OPENAPI-BC08-SLC01 | api-contract | Governance API (BC08) — SLC-01 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-governance-slc12a.md | OPENAPI-BC08-SLC12A | api-contract | Governance API (BC08) — SLC-12a | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-information-slc02.md | OPENAPI-BC02-SLC02 | api-contract | Information API (BC02) — SLC-02 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-information-slc04.md | OPENAPI-BC02-SLC04 | api-contract | Information API (BC02) — SLC-04 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-information-slc14.md | OPENAPI-BC02-SLC14 | api-contract | Information API (BC02) — SLC-14 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-information-slc15.md | OPENAPI-BC02-SLC15 | api-contract | Information API (BC02) — SLC-15 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-integration-slc02.md | OPENAPI-BC07-SLC02 | api-contract | Integration API (BC07) — SLC-02 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-integration-slc16.md | OPENAPI-BC07-SLC16 | api-contract | Integration API (BC07) — SLC-16 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-intelligence-slc06.md | OPENAPI-BC03-SLC06 | api-contract | Intelligence API (BC03) — SLC-06 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-intelligence-slc07.md | OPENAPI-BC03-SLC07 | api-contract | Intelligence API (BC03) — SLC-07 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-intelligence-slc16.md | OPENAPI-BC03-SLC16 | api-contract | Intelligence API (BC03) — SLC-16 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-knowledge-slc12.md | OPENAPI-BC06-SLC12 | api-contract | Knowledge API (BC06) — SLC-12 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-operations-slc03.md | OPENAPI-BC04-SLC03 | api-contract | Operations API (BC04) — SLC-03 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-operations-slc06.md | OPENAPI-BC04-SLC06 | api-contract | Operations API (BC04) — SLC-06 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-operations-slc08.md | OPENAPI-BC04-SLC08 | api-contract | Operations API (BC04) — SLC-08 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-operations-slc15.md | OPENAPI-BC04-SLC15 | api-contract | Operations API (BC04) — SLC-15 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-operations-slc17.md | OPENAPI-BC04-SLC17 | api-contract | Operations API (BC04) — SLC-17 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-readiness-slc03.md | OPENAPI-BC05-SLC03 | api-contract | Readiness API (BC05) — SLC-03 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-readiness-slc09.md | OPENAPI-BC05-SLC09 | api-contract | Readiness API (BC05) — SLC-09 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-readiness-slc18.md | OPENAPI-BC05-SLC18 | api-contract | Readiness API (BC05) — SLC-18 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/05-contracts/openapi-readiness-slc19.md | OPENAPI-BC05-SLC19 | api-contract | Readiness API (BC05) — SLC-19 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-01.md | LDM-SLC01 | logical-data-model | Logical Data Model — SLC-01 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-02.md | LDM-SLC02 | logical-data-model | Logical Data Model — SLC-02 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-03.md | LDM-SLC03 | logical-data-model | Logical Data Model — SLC-03 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-04.md | LDM-SLC04 | logical-data-model | Logical Data Model — SLC-04 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-05.md | LDM-SLC05 | logical-data-model | Logical Data Model — SLC-05 (projection documents) | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-06.md | LDM-SLC06 | logical-data-model | Logical Data Model — SLC-06 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-07.md | LDM-SLC07 | logical-data-model | Logical Data Model — SLC-07 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-08.md | LDM-SLC08 | logical-data-model | Logical Data Model — SLC-08 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-09.md | LDM-SLC09 | logical-data-model | Logical Data Model — SLC-09 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-10.md | LDM-SLC10 | logical-data-model | Logical Data Model — SLC-10 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-11.md | LDM-SLC11 | logical-data-model | Logical Data Model — SLC-11 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-12.md | LDM-SLC12 | logical-data-model | Logical Data Model — SLC-12 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-12a.md | LDM-SLC12A | logical-data-model | Logical Data Model — SLC-12a | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-14.md | LDM-SLC14 | logical-data-model | Logical Data Model — SLC-14 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-15.md | LDM-SLC15 | logical-data-model | Logical Data Model — SLC-15 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-16.md | LDM-SLC16 | logical-data-model | Logical Data Model — SLC-16 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-17.md | LDM-SLC17 | logical-data-model | Logical Data Model — SLC-17 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-18.md | LDM-SLC18 | logical-data-model | Logical Data Model — SLC-18 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/06-data/logical-model/slc-19.md | LDM-SLC19 | logical-data-model | Logical Data Model — SLC-19 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/cost-model.md | COST-MODEL | cost-model | Cost Model (unit economics) | W8 | T0/T2 | APPROVED_DELEGATED |  |
| spec/07-quality/performance-test-strategy.md | PERF-TEST-STRATEGY | verification-strategy | Performance, Capacity & Scalability Test Strategy | W8 | T2 | APPROVED_DELEGATED |  |
| spec/07-quality/scale-envelope.md | SCALE-ENVELOPE | quality | Design Scale Envelope & Scale-Ready Principles | W1 | T0 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc01.md | WL-SLC01 | workload-catalog | Workloads & Added Quality Scenarios — SLC-01 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc02.md | WL-SLC02 | workload-catalog | Workloads & Added Quality Scenarios — SLC-02 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc03.md | WL-SLC03 | workload-catalog | Workloads & Added Quality Scenarios — SLC-03 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc04.md | WL-SLC04 | workload-catalog | Workloads & Added Quality Scenarios — SLC-04 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc05.md | WL-SLC05 | workload-catalog | Workloads & Added Quality Scenarios — SLC-05 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc06.md | WL-SLC06 | workload-catalog | Workloads & Added Quality Scenarios — SLC-06 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc07.md | WL-SLC07 | workload-catalog | Workloads & Added Quality Scenarios — SLC-07 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc08.md | WL-SLC08 | workload-catalog | Workloads & Added Quality Scenarios — SLC-08 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc09.md | WL-SLC09 | workload-catalog | Workloads — SLC-09 (recalibrate after R1 pilot) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc10.md | WL-SLC10 | workload-catalog | Workloads — SLC-10 (recalibrate after R1 pilot) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc11.md | WL-SLC11 | workload-catalog | Workloads & Added Quality Scenarios — SLC-11 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc12.md | WL-SLC12 | workload-catalog | Workloads — SLC-12 (recalibrate after R1 pilot) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc12a.md | WL-SLC12A | workload-catalog | Workloads & Added Quality Scenarios — SLC-12a | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc14.md | WL-SLC14 | workload-catalog | Workloads — SLC-14 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc15.md | WL-SLC15 | workload-catalog | Workloads — SLC-15 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc16.md | WL-SLC16 | workload-catalog | Workloads — SLC-16 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc17.md | WL-SLC17 | workload-catalog | Workloads — SLC-17 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc18.md | WL-SLC18 | workload-catalog | Workloads — SLC-18 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads-slc19.md | WL-SLC19 | workload-catalog | Workloads — SLC-19 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/07-quality/workloads.md | WORKLOADS | workload-catalog | Workload Catalog (initial from W1) | W1 | T0/T1 | DRAFT |  |
| spec/08-security/audit-architecture.md | AUDIT-ARCHITECTURE | architecture | Audit Architecture (revised in SLC-01) | W3→W4 | T0 | APPROVED_DELEGATED |  |
| spec/08-security/authorization-model.md | AUTHZ-MODEL | security-model | Authorization Model | W3 | T0 | APPROVED_DELEGATED |  |
| spec/08-security/classification-scheme.md | CLASSIFICATION-SCHEME | security-model | Classification Scheme Model | W3 | T0 | APPROVED_DELEGATED |  |
| spec/08-security/data-protection.md | DATA-PROTECTION | security-model | Data Protection Model | W3 | T0 | APPROVED_DELEGATED |  |
| spec/08-security/key-hierarchy-and-disposition.md | SPEC-KEYS-DISPOSITION | component-specification | Key Hierarchy, Crypto-Shredding, Restore Gate, Disposition & Erasure Execution | W4 | T0 | APPROVED_DELEGATED |  |
| spec/08-security/label-derivation-rules.md | LABEL-DERIVATION | security-model | Label Derivation Rules — every aggregate (REQ-GOV-002 clarified) | W7 (SLC-12a consolidation) | T0 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc01.md | POLICIES-SLC01 | policy-decision-tables | Policy Decision Tables — SLC-01 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc02.md | POLICIES-SLC02 | policy-decision-tables | Policy Decision Tables — SLC-02 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc03.md | POLICIES-SLC03 | policy-decision-tables | Policy Decision Tables — SLC-03 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc04.md | POLICIES-SLC04 | policy-decision-tables | Policy Decision Tables — SLC-04 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc05.md | POLICIES-SLC05 | policy-decision-tables | Policy Decision Tables — SLC-05 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc06.md | POLICIES-SLC06 | policy-decision-tables | Policy Decision Tables — SLC-06 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc07.md | POLICIES-SLC07 | policy-decision-tables | Policy Decision Tables — SLC-07 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc08.md | POLICIES-SLC08 | policy-decision-tables | Policy Decision Tables — SLC-08 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc09.md | POLICIES-SLC09 | policy-decision-tables | Policy Decision Tables — SLC-09 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc10.md | POLICIES-SLC10 | policy-decision-tables | Policy Decision Tables — SLC-10 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc11.md | POLICIES-SLC11 | policy-decision-tables | Policy Decision Tables — SLC-11 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc12.md | POLICIES-SLC12 | policy-decision-tables | Policy Decision Tables — SLC-12 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc12a.md | POLICIES-SLC12A | policy-decision-tables | Policy Decision Tables — SLC-12a | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc14.md | POLICIES-SLC14 | policy-decision-tables | Policy Decision Tables — SLC-14 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc15.md | POLICIES-SLC15 | policy-decision-tables | Policy Decision Tables — SLC-15 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc16.md | POLICIES-SLC16 | policy-decision-tables | Policy Decision Tables — SLC-16 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc17.md | POLICIES-SLC17 | policy-decision-tables | Policy Decision Tables — SLC-17 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc18.md | POLICIES-SLC18 | policy-decision-tables | Policy Decision Tables — SLC-18 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/policies-slc19.md | POLICIES-SLC19 | policy-decision-tables | Policy Decision Tables — SLC-19 | W6 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/privacy-threats.md | PRIVACY-THREATS | privacy-threat-model | Privacy Threat Model (LINDDUN) | W3 | T0 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc01.md | THREAT-MODEL-SLC01 | threat-model | Threat Model — SLC-01 (STRIDE) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc02.md | THREAT-MODEL-SLC02 | threat-model | Threat Model — SLC-02 (STRIDE) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc03.md | THREAT-MODEL-SLC03 | threat-model | Threat Model — SLC-03 (STRIDE) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc04.md | THREAT-MODEL-SLC04 | threat-model | Threat Model — SLC-04 (STRIDE) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc05.md | THREAT-MODEL-SLC05 | threat-model | Threat Model — SLC-05 (STRIDE) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc06.md | THREAT-MODEL-SLC06 | threat-model | Threat Model — SLC-06 (STRIDE) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc07.md | THREAT-MODEL-SLC07 | threat-model | Threat Model — SLC-07 (STRIDE) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc08.md | THREAT-MODEL-SLC08 | threat-model | Threat Model — SLC-08 (STRIDE) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc09.md | THREAT-MODEL-SLC09 | threat-model | Threat Model — SLC-09 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc10.md | THREAT-MODEL-SLC10 | threat-model | Threat Model — SLC-10 (STRIDE + OWASP LLM) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc11.md | THREAT-MODEL-SLC11 | threat-model | Threat Model — SLC-11 (STRIDE) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc12.md | THREAT-MODEL-SLC12 | threat-model | Threat Model — SLC-12 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc12a.md | THREAT-MODEL-SLC12A | threat-model | Threat Model — SLC-12a (STRIDE) | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc14.md | THREAT-MODEL-SLC14 | threat-model | Threat Model — SLC-14 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc15.md | THREAT-MODEL-SLC15 | threat-model | Threat Model — SLC-15 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc16.md | THREAT-MODEL-SLC16 | threat-model | Threat Model — SLC-16 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc17.md | THREAT-MODEL-SLC17 | threat-model | Threat Model — SLC-17 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc18.md | THREAT-MODEL-SLC18 | threat-model | Threat Model — SLC-18 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model-slc19.md | THREAT-MODEL-SLC19 | threat-model | Threat Model — SLC-19 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/08-security/threat-model.md | THREAT-MODEL | threat-model | Threat Model — Kernel (STRIDE per trust boundary) | W3 | T0 | APPROVED_DELEGATED |  |
| spec/08-security/trust-boundaries.md | TRUST-BOUNDARIES | security-model | Trust Boundary Model | W3 | T0 | APPROVED_DELEGATED |  |
| spec/09-reliability/degradation-slc01.md | DEGRADATION-SLC01 | degradation-matrix | Degradation Matrix — SLC-01 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/degradation-slc02.md | DEGRADATION-SLC02 | degradation-matrix | Degradation Matrix — SLC-02 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/dr-and-continuity.md | DR-CONTINUITY | architecture | Disaster Recovery, Backups & Business Continuity | W8 | T2 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc01.md | FMEA-SLC01 | fmea | Failure Mode Analysis — SLC-01 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc02.md | FMEA-SLC02 | fmea | Failure Mode Analysis — SLC-02 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc03.md | FMEA-SLC03 | fmea | Failure Mode Analysis — SLC-03 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc04.md | FMEA-SLC04 | fmea | Failure Mode Analysis — SLC-04 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc05.md | FMEA-SLC05 | fmea | Failure Mode Analysis — SLC-05 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc06.md | FMEA-SLC06 | fmea | Failure Mode Analysis — SLC-06 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc07.md | FMEA-SLC07 | fmea | Failure Mode Analysis — SLC-07 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc08.md | FMEA-SLC08 | fmea | Failure Mode Analysis — SLC-08 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc09.md | FMEA-SLC09 | fmea | Failure Mode Analysis — SLC-09 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc10.md | FMEA-SLC10 | fmea | Failure Mode Analysis — SLC-10 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc11.md | FMEA-SLC11 | fmea | Failure Mode Analysis — SLC-11 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc12.md | FMEA-SLC12 | fmea | Failure Mode Analysis — SLC-12 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc12a.md | FMEA-SLC12A | fmea | Failure Mode Analysis — SLC-12a | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc14.md | FMEA-SLC14 | fmea | Failure Mode Analysis — SLC-14 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc15.md | FMEA-SLC15 | fmea | Failure Mode Analysis — SLC-15 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc16.md | FMEA-SLC16 | fmea | Failure Mode Analysis — SLC-16 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc17.md | FMEA-SLC17 | fmea | Failure Mode Analysis — SLC-17 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc18.md | FMEA-SLC18 | fmea | Failure Mode Analysis — SLC-18 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/fmea-slc19.md | FMEA-SLC19 | fmea | Failure Mode Analysis — SLC-19 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc01.md | OBS-SLC01 | observability | Observability — SLC-01 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc02.md | OBS-SLC02 | observability | Observability — SLC-02 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc03.md | OBS-SLC03 | observability | Observability — SLC-03 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc04.md | OBS-SLC04 | observability | Observability — SLC-04 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc05.md | OBS-SLC05 | observability | Observability — SLC-05 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc06.md | OBS-SLC06 | observability | Observability — SLC-06 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc07.md | OBS-SLC07 | observability | Observability — SLC-07 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc08.md | OBS-SLC08 | observability | Observability — SLC-08 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc09.md | OBS-SLC09 | observability | Observability — SLC-09 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc10.md | OBS-SLC10 | observability | Observability — SLC-10 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc11.md | OBS-SLC11 | observability | Observability — SLC-11 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc12.md | OBS-SLC12 | observability | Observability — SLC-12 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc12a.md | OBS-SLC12A | observability | Observability — SLC-12a | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc14.md | OBS-SLC14 | observability | Observability — SLC-14 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc15.md | OBS-SLC15 | observability | Observability — SLC-15 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc16.md | OBS-SLC16 | observability | Observability — SLC-16 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc17.md | OBS-SLC17 | observability | Observability — SLC-17 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc18.md | OBS-SLC18 | observability | Observability — SLC-18 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/09-reliability/observability-slc19.md | OBS-SLC19 | observability | Observability — SLC-19 | W5 | T1 | APPROVED_DELEGATED |  |
| spec/10-ai/autonomy-matrix.md | AI-AUTONOMY-MATRIX | autonomy-matrix | AI Autonomy Matrix (AIL) — HAP-06 | W3 | T0 | APPROVED_DELEGATED |  |
| spec/11-integration/README.md |  |  |  |  |  |  |  |
| spec/12-solution/c4-containers.md | C4-CONTAINERS | architecture-view | C4 — Containers (one cell) | W8 | T0 | APPROVED_DELEGATED |  |
| spec/12-solution/c4-context.md | C4-CONTEXT | architecture-view | C4 — System Context | W8 | T0 | APPROVED_DELEGATED |  |
| spec/12-solution/cell-architecture.md | CELL-ARCHITECTURE | architecture | Cell Architecture, Profiles and Capacity Sizing | W8 | T0 | APPROVED_DELEGATED |  |
| spec/12-solution/deployment-units.md | DEPLOYMENT-UNITS | architecture | Deployment Units (V5§97 criteria) | W8 (extended R2 baseline consolidation) | T0 | APPROVED_DELEGATED |  |
| spec/12-solution/release-configuration-migration.md | RELEASE-CONFIG-MIGRATION | architecture | Release, Configuration & Migration | W8 | T2 | APPROVED_DELEGATED |  |
| spec/12-solution/technology-decisions.md | TECH-DECISIONS | technology-decisions | Technology Decisions (W8) — from workload and capability evidence | W8 | T0 | APPROVED_DELEGATED |  |
| spec/12-solution/ui-architecture.md | UI-ARCHITECTURE | architecture | Client Architecture (web + mobile, bilingual, RTL) | W8 | T1 | APPROVED_DELEGATED |  |
| spec/12-solution/w8-inputs.md | W8-INPUTS | decision-input-register | Inputs Collected for W8 (Solution & Technology Decisions) | W4–W7 → W8 |  | DRAFT |  |
| spec/13-verification/acceptance/SLC-01/authority-grant-state-machine.md | TST-AUTHORITY-GRANT-SM | acceptance-spec | Acceptance — Authority Grant (incl. delegation) state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/classification-scheme-state-machine.md | TST-CLASSIFICATION-SCHEME-SM | acceptance-spec | Acceptance — Classification Scheme Version state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/clearance-state-machine.md | TST-CLEARANCE-SM | acceptance-spec | Acceptance — Clearance state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/invariants-slc01.md | TST-SLC01-INVARIANTS | acceptance-spec | Acceptance — SLC-01 guards, invariants and security scenarios | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/organization-state-machine.md | TST-ORGANIZATION-SM | acceptance-spec | Acceptance — Organization (with unit tree) state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/person-state-machine.md | TST-PERSON-SM | acceptance-spec | Acceptance — Person state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/policy-set-state-machine.md | TST-POLICY-SET-SM | acceptance-spec | Acceptance — Policy Set Version state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/role-assignment-state-machine.md | TST-ROLE-ASSIGNMENT-SM | acceptance-spec | Acceptance — Role Assignment state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/role-state-machine.md | TST-ROLE-SM | acceptance-spec | Acceptance — Role state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/security-exception-state-machine.md | TST-SECURITY-EXCEPTION-SM | acceptance-spec | Acceptance — Security Exception state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/service-account-state-machine.md | TST-SERVICE-ACCOUNT-SM | acceptance-spec | Acceptance — Service Account state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/tenant-state-machine.md | TST-TENANT-SM | acceptance-spec | Acceptance — Tenant state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-01/user-state-machine.md | TST-USER-SM | acceptance-spec | Acceptance — User Account state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/adapter-state-machine.md | TST-ADAPTER-SM | acceptance-spec | Acceptance — Adapter state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/attachment-state-machine.md | TST-ATTACHMENT-SM | acceptance-spec | Acceptance — Attachment state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/claim-state-machine.md | TST-CLAIM-SM | acceptance-spec | Acceptance — Claim state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/entity-state-machine.md | TST-ENTITY-SM | acceptance-spec | Acceptance — Entity (identity) state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/evidence-link-state-machine.md | TST-EVIDENCE-LINK-SM | acceptance-spec | Acceptance — Evidence Link state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/evidence-state-machine.md | TST-EVIDENCE-SM | acceptance-spec | Acceptance — Evidence state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/external-id-state-machine.md | TST-EXTERNAL-ID-SM | acceptance-spec | Acceptance — External Identifier Mapping state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/import-batch-state-machine.md | TST-IMPORT-BATCH-SM | acceptance-spec | Acceptance — Import Batch state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/invariants-slc02.md | TST-SLC02-INVARIANTS | acceptance-spec | Acceptance — SLC-02 temporal, claims, security and ingestion scenarios | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/observation-state-machine.md | TST-OBSERVATION-SM | acceptance-spec | Acceptance — Observation state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/realworld-event-state-machine.md | TST-REALWORLD-EVENT-SM | acceptance-spec | Acceptance — Real-World Event (identity) state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/relationship-state-machine.md | TST-RELATIONSHIP-SM | acceptance-spec | Acceptance — Relationship (identity) state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-02/source-state-machine.md | TST-SOURCE-SM | acceptance-spec | Acceptance — Source state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-03/invariants-slc03.md | TST-SLC03-INVARIANTS | acceptance-spec | Acceptance — SLC-03 task rules, eligibility, scheduling and offline contract | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-03/qualification-record-state-machine.md | TST-QUALIFICATION-RECORD-SM | acceptance-spec | Acceptance — Qualification Record state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-03/task-state-machine.md | TST-TASK-SM | acceptance-spec | Acceptance — Task state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-03/task-type-state-machine.md | TST-TASK-TYPE-SM | acceptance-spec | Acceptance — Task Type state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-04/conflict-state-machine.md | TST-CONFLICT-SM | acceptance-spec | Acceptance — Conflict state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-04/er-case-state-machine.md | TST-ER-CASE-SM | acceptance-spec | Acceptance — Entity Resolution Case state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-04/invariants-slc04.md | TST-SLC04-INVARIANTS | acceptance-spec | Acceptance — SLC-04 conflicts, merge/split and visibility | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-04/match-ruleset-state-machine.md | TST-MATCH-RULESET-SM | acceptance-spec | Acceptance — Match Ruleset state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-05/invariants-slc05.md | TST-SLC05-INVARIANTS | acceptance-spec | Acceptance — SLC-05 inference safety, revocation, Arabic search, graph, rebuild | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-05/projection-version-state-machine.md | TST-PROJECTION-VERSION-SM | acceptance-spec | Acceptance — Projection Version state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-06/alert-rule-state-machine.md | TST-ALERT-RULE-SM | acceptance-spec | Acceptance — Alert Rule state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-06/alert-state-machine.md | TST-ALERT-SM | acceptance-spec | Acceptance — Alert state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-06/invariants-slc06.md | TST-SLC06-INVARIANTS | acceptance-spec | Acceptance — SLC-06 membership, alerts, COP, tiles, notifications | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-06/notification-state-machine.md | TST-NOTIFICATION-SM | acceptance-spec | Acceptance — Notification state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-06/situation-state-machine.md | TST-SITUATION-SM | acceptance-spec | Acceptance — Situation state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-06/subscription-state-machine.md | TST-SUBSCRIPTION-SM | acceptance-spec | Acceptance — Subscription state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-07/analysis-case-state-machine.md | TST-ANALYSIS-CASE-SM | acceptance-spec | Acceptance — Analysis Case state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-07/analysis-method-state-machine.md | TST-ANALYSIS-METHOD-SM | acceptance-spec | Acceptance — Analysis Method Version state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-07/analysis-run-state-machine.md | TST-ANALYSIS-RUN-SM | acceptance-spec | Acceptance — Analysis Run state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-07/assessment-state-machine.md | TST-ASSESSMENT-SM | acceptance-spec | Acceptance — Assessment Version state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-07/finding-state-machine.md | TST-FINDING-SM | acceptance-spec | Acceptance — Finding state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-07/invariants-slc07.md | TST-SLC07-INVARIANTS | acceptance-spec | Acceptance — SLC-07 reproducibility, execution security, assessment rules | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-08/decision-request-state-machine.md | TST-DECISION-REQUEST-SM | acceptance-spec | Acceptance — Decision Request state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-08/decision-state-machine.md | TST-DECISION-SM | acceptance-spec | Acceptance — Decision state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-08/invariants-slc08.md | TST-SLC08-INVARIANTS | acceptance-spec | Acceptance — SLC-08 authority, decision basis, baselines, change classification, task sync, outcomes | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-08/outcome-tracker-state-machine.md | TST-OUTCOME-TRACKER-SM | acceptance-spec | Acceptance — Outcome Tracker state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-08/plan-state-machine.md | TST-PLAN-SM | acceptance-spec | Acceptance — Plan (identity) state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-08/plan-version-state-machine.md | TST-PLAN-VERSION-SM | acceptance-spec | Acceptance — Plan Version state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-09/allocation-state-machine.md | TST-ALLOCATION-SM | acceptance-spec | Acceptance — Resource Allocation state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-09/asset-assignment-state-machine.md | TST-ASSET-ASSIGNMENT-SM | acceptance-spec | Acceptance — Asset Assignment state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-09/asset-reservation-state-machine.md | TST-ASSET-RESERVATION-SM | acceptance-spec | Acceptance — Asset Reservation state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-09/asset-state-machine.md | TST-ASSET-SM | acceptance-spec | Acceptance — Asset state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-09/invariants-slc09.md | TST-SLC09-INVARIANTS | acceptance-spec | Acceptance — SLC-09 availability, reservations, allocation contention, pre-emption, readiness | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-09/maintenance-order-state-machine.md | TST-MAINTENANCE-ORDER-SM | acceptance-spec | Acceptance — Maintenance Order state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-09/resource-pool-state-machine.md | TST-RESOURCE-POOL-SM | acceptance-spec | Acceptance — Resource Pool state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-09/role-requirement-state-machine.md | TST-ROLE-REQUIREMENT-SM | acceptance-spec | Acceptance — Role Requirement state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-10/ai-request-state-machine.md | TST-AI-REQUEST-SM | acceptance-spec | Acceptance — AI Request state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-10/ai-result-state-machine.md | TST-AI-RESULT-SM | acceptance-spec | Acceptance — AI Result (reviewable) state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-10/ai-routing-state-machine.md | TST-AI-ROUTING-SM | acceptance-spec | Acceptance — AI Routing Configuration state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-10/ai-tool-state-machine.md | TST-AI-TOOL-SM | acceptance-spec | Acceptance — AI Tool state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-10/eval-suite-state-machine.md | TST-EVAL-SUITE-SM | acceptance-spec | Acceptance — Evaluation Suite state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-10/invariants-slc10.md | TST-SLC10-INVARIANTS | acceptance-spec | Acceptance — SLC-10 grounded AI, authorization, injection, review, model lifecycle | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-10/model-version-state-machine.md | TST-MODEL-VERSION-SM | acceptance-spec | Acceptance — Model Version state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-11/device-state-machine.md | TST-DEVICE-SM | acceptance-spec | Acceptance — Field Device state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-11/invariants-slc11.md | TST-SLC11-INVARIANTS | acceptance-spec | Acceptance — SLC-11 offline capture, sync protocol, conflicts, device security | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-11/preload-package-state-machine.md | TST-PRELOAD-PACKAGE-SM | acceptance-spec | Acceptance — Preload Package state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-11/sync-conflict-state-machine.md | TST-SYNC-CONFLICT-SM | acceptance-spec | Acceptance — Sync Conflict state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-11/sync-session-state-machine.md | TST-SYNC-SESSION-SM | acceptance-spec | Acceptance — Sync Session state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12/archive-package-state-machine.md | TST-ARCHIVE-PACKAGE-SM | acceptance-spec | Acceptance — Archive Package (AIP) state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12/distribution-state-machine.md | TST-DISTRIBUTION-SM | acceptance-spec | Acceptance — Distribution state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12/invariants-slc12.md | TST-SLC12-INVARIANTS | acceptance-spec | Acceptance — SLC-12 products, distribution, knowledge, archive, reconstruction | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12/knowledge-object-state-machine.md | TST-KNOWLEDGE-OBJECT-SM | acceptance-spec | Acceptance — Knowledge Object Version state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12/product-state-machine.md | TST-PRODUCT-SM | acceptance-spec | Acceptance — Product Version state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12/product-template-state-machine.md | TST-PRODUCT-TEMPLATE-SM | acceptance-spec | Acceptance — Product Template state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12/reconstruction-state-machine.md | TST-RECONSTRUCTION-SM | acceptance-spec | Acceptance — Historical Reconstruction state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12a/disposition-run-state-machine.md | TST-DISPOSITION-RUN-SM | acceptance-spec | Acceptance — Disposition Run state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12a/erasure-request-state-machine.md | TST-ERASURE-REQUEST-SM | acceptance-spec | Acceptance — Erasure Request state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12a/invariants-slc12a.md | TST-SLC12A-INVARIANTS | acceptance-spec | Acceptance — SLC-12a retention, holds, disposition, erasure, restore gate | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12a/legal-hold-state-machine.md | TST-LEGAL-HOLD-SM | acceptance-spec | Acceptance — Legal Hold state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-12a/retention-schedule-state-machine.md | TST-RETENTION-SCHEDULE-SM | acceptance-spec | Acceptance — Retention Schedule Version state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-14/collection-plan-state-machine.md | TST-COLLECTION-PLAN-SM | acceptance-spec | Acceptance — Collection Plan state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-14/collection-requirement-state-machine.md | TST-COLLECTION-REQUIREMENT-SM | acceptance-spec | Acceptance — Collection Requirement state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-14/invariants-slc14.md | TST-SLC14-INVARIANTS | acceptance-spec | Acceptance — SLC-14 collection requirements, matching, viewer-scoped fulfilment, tasking | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-15/coordination-case-state-machine.md | TST-COORDINATION-CASE-SM | acceptance-spec | Acceptance — Coordination Case state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-15/correlation-proposal-state-machine.md | TST-CORRELATION-PROPOSAL-SM | acceptance-spec | Acceptance — Correlation Proposal state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-15/correlation-rule-state-machine.md | TST-CORRELATION-RULE-SM | acceptance-spec | Acceptance — Correlation Rule state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-15/invariants-slc15.md | TST-SLC15-INVARIANTS | acceptance-spec | Acceptance — SLC-15 coordination scoping, decision-gated actions, correlation and fusion | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-16/cap-message-state-machine.md | TST-CAP-MESSAGE-SM | acceptance-spec | Acceptance — CAP Message (outbound) state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-16/hr-sync-proposal-state-machine.md | TST-HR-SYNC-PROPOSAL-SM | acceptance-spec | Acceptance — HR Sync Proposal state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-16/integration-connection-state-machine.md | TST-INTEGRATION-CONNECTION-SM | acceptance-spec | Acceptance — Integration Connection state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-16/invariants-slc16.md | TST-SLC16-INVARIANTS | acceptance-spec | Acceptance — SLC-16 enterprise integrations | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-16/sensor-stream-state-machine.md | TST-SENSOR-STREAM-SM | acceptance-spec | Acceptance — Sensor Stream state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-17/incident-state-machine.md | TST-INCIDENT-SM | acceptance-spec | Acceptance — Incident state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-17/invariants-slc17.md | TST-SLC17-INVARIANTS | acceptance-spec | Acceptance — SLC-17 risk lifecycle, incident escalation, contingency activation | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-17/risk-state-machine.md | TST-RISK-SM | acceptance-spec | Acceptance — Risk state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-18/invariants-slc18.md | TST-SLC18-INVARIANTS | acceptance-spec | Acceptance — SLC-18 logistics request / allocation / shipment linkage | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-18/logistics-request-state-machine.md | TST-LOGISTICS-REQUEST-SM | acceptance-spec | Acceptance — Logistics Request state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-18/shipment-state-machine.md | TST-SHIPMENT-SM | acceptance-spec | Acceptance — Shipment state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-19/exercise-state-machine.md | TST-EXERCISE-SM | acceptance-spec | Acceptance — Exercise state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-19/invariants-slc19.md | TST-SLC19-INVARIANTS | acceptance-spec | Acceptance — SLC-19 scenario freeze / exercise-simulation delegation / evidence reuse | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-19/scenario-state-machine.md | TST-SCENARIO-SM | acceptance-spec | Acceptance — Scenario state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/acceptance/SLC-19/simulation-state-machine.md | TST-SIMULATION-SM | acceptance-spec | Acceptance — Simulation state machine | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/fitness-functions.md | FITNESS-FUNCTIONS | fitness-model | Architecture Fitness Functions | W3 | T0 | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc01.md | PROP-SLC01 | property-spec | Property-Based Invariant Specifications — SLC-01 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc02.md | PROP-SLC02 | property-spec | Property-Based Invariant Specifications — SLC-02 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc03.md | PROP-SLC03 | property-spec | Property-Based Invariant Specifications — SLC-03 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc04.md | PROP-SLC04 | property-spec | Property-Based Invariant Specifications — SLC-04 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc05.md | PROP-SLC05 | property-spec | Property-Based Invariant Specifications — SLC-05 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc06.md | PROP-SLC06 | property-spec | Property-Based Invariant Specifications — SLC-06 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc07.md | PROP-SLC07 | property-spec | Property-Based Invariant Specifications — SLC-07 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc08.md | PROP-SLC08 | property-spec | Property-Based Invariant Specifications — SLC-08 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc09.md | PROP-SLC09 | property-spec | Property-Based Invariant Specifications — SLC-09 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc10.md | PROP-SLC10 | property-spec | Property-Based Invariant Specifications — SLC-10 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc11.md | PROP-SLC11 | property-spec | Property-Based Invariant Specifications — SLC-11 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc12.md | PROP-SLC12 | property-spec | Property-Based Invariant Specifications — SLC-12 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc12a.md | PROP-SLC12A | property-spec | Property-Based Invariant Specifications — SLC-12a | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc14.md | PROP-SLC14 | property-spec | Property-Based Invariant Specifications — SLC-14 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc15.md | PROP-SLC15 | property-spec | Property-Based Invariant Specifications — SLC-15 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc16.md | PROP-SLC16 | property-spec | Property-Based Invariant Specifications — SLC-16 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc17.md | PROP-SLC17 | property-spec | Property-Based Invariant Specifications — SLC-17 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc18.md | PROP-SLC18 | property-spec | Property-Based Invariant Specifications — SLC-18 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/invariant-properties-slc19.md | PROP-SLC19 | property-spec | Property-Based Invariant Specifications — SLC-19 | W6 |  | APPROVED_DELEGATED |  |
| spec/13-verification/spec-lint-rules.md | LINT | spec-lint-rules | Spec Lint Rules | W0 | T0 | DRAFT |  |
| spec/13-verification/tooling/slice-sources.md | SLICE-SOURCES | specification-source | Slice source data (authoritative input to the generators) | W9 + R2 + R3 |  | BASELINED (R1) / DESIGN (R2) / DESIGN, G6 held per RSK-028 (R3) |  |
| spec/13-verification/tooling/spec-tooling.md | SPEC-TOOLING | specification-tooling | Specification tooling (generators and checkers) | W9 |  | BASELINED |  |
| spec/14-slices/SLC-01/atam-lite.md | ATAM-SLC01 | architecture-review | ATAM-lite Review — SLC-01 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-01/readiness.md | G6-SLC-01 | slice-readiness | Slice Readiness — SLC-01 (G6-SLC) | W7 |  | APPROVED_DELEGATED |  |
| spec/14-slices/SLC-02/atam-lite.md | ATAM-SLC02 | architecture-review | ATAM-lite Review — SLC-02 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-02/readiness.md | G6-SLC-02 | slice-readiness | Slice Readiness — SLC-02 Information Kernel (G6-SLC) | W7 |  | APPROVED_DELEGATED |  |
| spec/14-slices/SLC-03/atam-lite.md | ATAM-SLC03 | architecture-review | ATAM-lite Review — SLC-03 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-03/readiness.md | G6-SLC-03 | slice-readiness | Slice Readiness — SLC-03 Task Lifecycle (G6-SLC) | W7 |  | APPROVED_DELEGATED |  |
| spec/14-slices/SLC-04/atam-lite.md | ATAM-SLC04 | architecture-review | ATAM-lite Review — SLC-04 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-04/readiness.md | G6-SLC-04 | slice-readiness | Slice Readiness — SLC-04 Conflict & Entity Resolution (G6-SLC) | W7 |  | APPROVED_DELEGATED |  |
| spec/14-slices/SLC-05/atam-lite.md | ATAM-SLC05 | architecture-review | ATAM-lite Review — SLC-05 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-05/readiness.md | G6-SLC-05 | slice-readiness | Slice Readiness — SLC-05 Secured Search & Graph (G6-SLC) | W7 |  | APPROVED_DELEGATED |  |
| spec/14-slices/SLC-06/atam-lite.md | ATAM-SLC06 | architecture-review | ATAM-lite Review — SLC-06 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-06/readiness.md | G6-SLC-06 | slice-readiness | Slice Readiness — SLC-06 Situation, Alerts & Notifications (G6-SLC) | W7 |  | APPROVED_DELEGATED |  |
| spec/14-slices/SLC-07/atam-lite.md | ATAM-SLC07 | architecture-review | ATAM-lite Review — SLC-07 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-07/readiness.md | G6-SLC-07 | slice-readiness | Slice Readiness — SLC-07 Analysis → Assessment (G6-SLC) | W7 |  | APPROVED_DELEGATED |  |
| spec/14-slices/SLC-08/atam-lite.md | ATAM-SLC08 | architecture-review | ATAM-lite Review — SLC-08 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-08/readiness.md | G6-SLC-08 | slice-readiness | Slice Readiness — SLC-08 Decision → Plan → Baseline → Tasks (G6-SLC) | W7 |  | APPROVED_DELEGATED |  |
| spec/14-slices/SLC-09/atam-lite.md | ATAM-SLC09 | architecture-review | ATAM-lite Review — SLC-09 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-09/readiness.md | G6-SLC-09 | slice-readiness | Slice Readiness — SLC-09 Assets & Resources (R2) | W7 |  | DESIGN_COMPLETE — G6 HELD until R1 pilot review (RSK-027) |  |
| spec/14-slices/SLC-10/atam-lite.md | ATAM-SLC10 | architecture-review | ATAM-lite Review — SLC-10 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-10/readiness.md | G6-SLC-10 | slice-readiness | Slice Readiness — SLC-10 Grounded AI (R2) | W7 |  | DESIGN_COMPLETE — G6 HELD until R1 pilot review (RSK-027) and first model evaluation |  |
| spec/14-slices/SLC-11/atam-lite.md | ATAM-SLC11 | architecture-review | ATAM-lite Review — SLC-11 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-11/readiness.md | G6-SLC-11 | slice-readiness | Slice Readiness — SLC-11 Offline Field Capture & Sync (G6-SLC) | W7 |  | APPROVED_DELEGATED |  |
| spec/14-slices/SLC-12/atam-lite.md | ATAM-SLC12 | architecture-review | ATAM-lite Review — SLC-12 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-12/readiness.md | G6-SLC-12 | slice-readiness | Slice Readiness — SLC-12 Products, Knowledge, Archive & Reconstruction (R2) | W7 |  | DESIGN_COMPLETE — G6 HELD until R1 pilot review (RSK-027) |  |
| spec/14-slices/SLC-12a/atam-lite.md | ATAM-SLC12A | architecture-review | ATAM-lite Review — SLC-12a | W7 |  | DRAFT |  |
| spec/14-slices/SLC-12a/readiness.md | G6-SLC-12a | slice-readiness | Slice Readiness — SLC-12a Retention, Legal Hold, Disposition, Erasure (G6-SLC) | W7 |  | APPROVED_DELEGATED |  |
| spec/14-slices/SLC-14/atam-lite.md | ATAM-SLC14 | architecture-review | ATAM-lite Review — SLC-14 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-14/readiness.md | G6-SLC-14 | slice-readiness | Slice Readiness — SLC-14 Collection Requirements & Planning (R2) | W7 |  | DESIGN_COMPLETE — G6 HELD until R1 pilot review (RSK-027) |  |
| spec/14-slices/SLC-15/atam-lite.md | ATAM-SLC15 | architecture-review | ATAM-lite Review — SLC-15 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-15/readiness.md | G6-SLC-15 | slice-readiness | Slice Readiness — SLC-15 Coordination & Correlation/Fusion (R2) | W7 |  | DESIGN_COMPLETE — G6 HELD until R1 pilot review (RSK-027) |  |
| spec/14-slices/SLC-16/atam-lite.md | ATAM-SLC16 | architecture-review | ATAM-lite Review — SLC-16 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-16/readiness.md | G6-SLC-16 | slice-readiness | Slice Readiness — SLC-16 Enterprise Integrations (R2) | W7 |  | DESIGN_COMPLETE — G6 HELD until R1 pilot review (RSK-027) and tenant systems known (UNK-021) |  |
| spec/14-slices/SLC-17/atam-lite.md | ATAM-SLC17 | architecture-review | ATAM-lite Review — SLC-17 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-17/readiness.md | G6-SLC-17 | slice-readiness | Slice Readiness — SLC-17 Risk & Contingency (R3) | W7 |  | DESIGN_COMPLETE — G6 HELD until R1 pilot review AND R2 pilot review (RSK-028, stricter than RSK-027) |  |
| spec/14-slices/SLC-18/atam-lite.md | ATAM-SLC18 | architecture-review | ATAM-lite Review — SLC-18 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-18/readiness.md | G6-SLC-18 | slice-readiness | Slice Readiness — SLC-18 Logistics & Supply (R3) | W7 |  | DESIGN_COMPLETE — G6 HELD until R1 pilot review AND R2 pilot review (RSK-028) |  |
| spec/14-slices/SLC-19/atam-lite.md | ATAM-SLC19 | architecture-review | ATAM-lite Review — SLC-19 | W7 |  | DRAFT |  |
| spec/14-slices/SLC-19/readiness.md | G6-SLC-19 | slice-readiness | Slice Readiness — SLC-19 Training, Competency & Exercises (R3) | W7 |  | DESIGN_COMPLETE — G6 HELD until R1 pilot review AND R2 pilot review (RSK-028) |  |
| spec/14-slices/slices.md | SLICES | slices | Slice Plan | W1 | T0 | APPROVED_DELEGATED |  |
| spec/15-traceability/quality-verification-matrix.md | QUALITY-MATRIX | traceability-matrix | Quality Verification Matrix — every QAS → verification method and timing (V5 #104) | W9 |  | GENERATED |  |
| spec/15-traceability/rtm-r1.md | RTM-R1 | traceability-matrix | Requirements Traceability Matrix — R1 (OUT → BRQ → REQ → slice → verification), generated | W9 |  | GENERATED |  |
| spec/15-traceability/rtm-r2.md | RTM-R2 | traceability-matrix | Requirements Traceability Matrix — R2 (OUT → BRQ → REQ → slice → verification), generated | R2 baseline consolidation |  | GENERATED |  |
| spec/15-traceability/trace-platform.md | TRACE-PLATFORM | traceability-matrix | Traceability — cross-cutting platform requirements (not owned by a domain slice) | W7 → W8 |  | GENERATED |  |
| spec/15-traceability/trace-slc01.md | TRACE-SLC01 | traceability-matrix | Traceability — SLC-01 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc02.md | TRACE-SLC02 | traceability-matrix | Traceability — SLC-02 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc03.md | TRACE-SLC03 | traceability-matrix | Traceability — SLC-03 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc04.md | TRACE-SLC04 | traceability-matrix | Traceability — SLC-04 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc05.md | TRACE-SLC05 | traceability-matrix | Traceability — SLC-05 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc06.md | TRACE-SLC06 | traceability-matrix | Traceability — SLC-06 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc07.md | TRACE-SLC07 | traceability-matrix | Traceability — SLC-07 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc08.md | TRACE-SLC08 | traceability-matrix | Traceability — SLC-08 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc09.md | TRACE-SLC09 | traceability-matrix | Traceability — SLC-09 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc10.md | TRACE-SLC10 | traceability-matrix | Traceability — SLC-10 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc11.md | TRACE-SLC11 | traceability-matrix | Traceability — SLC-11 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc12.md | TRACE-SLC12 | traceability-matrix | Traceability — SLC-12 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc12a.md | TRACE-SLC12A | traceability-matrix | Traceability — SLC-12a (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc14.md | TRACE-SLC14 | traceability-matrix | Traceability — SLC-14 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc15.md | TRACE-SLC15 | traceability-matrix | Traceability — SLC-15 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc16.md | TRACE-SLC16 | traceability-matrix | Traceability — SLC-16 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc17.md | TRACE-SLC17 | traceability-matrix | Traceability — SLC-17 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc18.md | TRACE-SLC18 | traceability-matrix | Traceability — SLC-18 (generated) | W7 |  | GENERATED |  |
| spec/15-traceability/trace-slc19.md | TRACE-SLC19 | traceability-matrix | Traceability — SLC-19 (generated) | W7 |  | GENERATED |  |
| spec/16-reports/ANTI-PATTERN-REPORT-R1.md | ANTI-PATTERN-R1 | anti-pattern-report |  | W9 |  | FINAL (delegated) |  |
| spec/16-reports/ANTI-PATTERN-REPORT-R2.md | ANTI-PATTERN-R2 | anti-pattern-report |  | R2 baseline consolidation |  | FINAL (delegated) |  |
| spec/16-reports/ARCHITECTURE-REVIEW-R1.md | ARCH-REVIEW-R1 | architecture-review | ATAM-lite Architecture Review — Release 1 (whole system) | W9 |  | FINAL (delegated) |  |
| spec/16-reports/ARCHITECTURE-REVIEW-R2.md | ARCH-REVIEW-R2 | architecture-review | ATAM-lite Architecture Review — Release 2 (six new slices) | R2 baseline consolidation |  | FINAL (delegated) |  |
| spec/16-reports/CONSISTENCY-CHECK-W3.md | CONSISTENCY-W3 | consistency-report |  | W3 |  | DRAFT |  |
| spec/16-reports/CONSISTENCY-REPORT-R1.md | CONSISTENCY-R1 | consistency-report |  | W9 |  | FINAL (delegated) |  |
| spec/16-reports/CONSISTENCY-REPORT-R2.md | CONSISTENCY-R2 | consistency-report |  | R2 baseline consolidation |  | FINAL (delegated) |  |
| spec/16-reports/ENGINEERING-BASELINE-R1.md | ENGINEERING-BASELINE-R1 | engineering-baseline | Engineering Baseline — Release 1 | W9 |  | BASELINED (delegated) — pending owner ratification at G6 |  |
| spec/16-reports/ENGINEERING-BASELINE-R2.md | ENGINEERING-BASELINE-R2 | engineering-baseline | Engineering Baseline — Release 2 (design) | R2 baseline consolidation |  | BASELINED (delegated) — DESIGN baseline only; G6 held per slice until R1 pilot review (RSK-027) |  |
| spec/16-reports/EVOLUTION-ROADMAP.md | EVOLUTION-ROADMAP | roadmap | Evolution Roadmap — R2, R3 and watched triggers | W9 |  | PROPOSED (delegated) |  |
| spec/16-reports/IMPLEMENTATION-READINESS-R1.md | IMPLEMENTATION-READINESS-R1 | implementation-readiness | Implementation Readiness — Release 1 (G6 verdict) | W9 |  | RATIFIED |  |
| spec/16-reports/METHODOLOGY-RETROSPECTIVE.md | METHODOLOGY-RETRO | retrospective | Methodology Retrospective — lessons for V6.1 | W9 |  | PROPOSED |  |
| spec/16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md | REQ-QUALITY-R2 | requirements-quality-report |  | W2-R2 |  | DRAFT |  |
| spec/16-reports/REQUIREMENTS-QUALITY-REPORT.md | REQ-QUALITY-REPORT | requirements-quality-report |  | W2 |  | DRAFT |  |
| spec/16-reports/SESSION-R2-BASELINE.md | SESSION-R2-BASELINE | session-report |  | R2 baseline consolidation (W9-style) |  |  |  |
| spec/16-reports/SESSION-W0.md | SESSION-W0 | session-report |  | W0 |  |  |  |
| spec/16-reports/SESSION-W1.md | SESSION-W1 | session-report |  | W1 (a + b) |  |  |  |
| spec/16-reports/SESSION-W2-R2.md | SESSION-W2-R2 | session-report |  | W1/W2 for Release 2 |  |  |  |
| spec/16-reports/SESSION-W2.md | SESSION-W2 | session-report |  | W2 |  |  |  |
| spec/16-reports/SESSION-W3.md | SESSION-W3 | session-report |  | W3 |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC01.md | SESSION-SLC01 | session-report |  | W4–W7 (SLC-01) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC02.md | SESSION-SLC02 | session-report |  | W4–W7 (SLC-02) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC03.md | SESSION-SLC03 | session-report |  | W4–W7 (SLC-03) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC04.md | SESSION-SLC04 | session-report |  | W4–W7 (SLC-04) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC05.md | SESSION-SLC05 | session-report |  | W4–W7 (SLC-05) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC06.md | SESSION-SLC06 | session-report |  | W4–W7 (SLC-06) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC07.md | SESSION-SLC07 | session-report |  | W4–W7 (SLC-07) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC08.md | SESSION-SLC08 | session-report |  | W4–W7 (SLC-08) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC09.md | SESSION-SLC09 | session-report |  | W4–W7 (SLC-09, Release 2) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC10.md | SESSION-SLC10 | session-report |  | W4–W7 (SLC-10, Release 2) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC11.md | SESSION-SLC11 | session-report |  | W4–W7 (SLC-11) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC12.md | SESSION-SLC12 | session-report |  | W4–W7 (SLC-12, Release 2) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC12a.md | SESSION-SLC12A | session-report |  | W4–W7 (SLC-12a) + R1 slice consolidation |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC14.md | SESSION-SLC14 | session-report |  | W4–W7 (SLC-14, Release 2) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC15.md | SESSION-SLC15 | session-report |  | W4–W7 (SLC-15, Release 2) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC16.md | SESSION-SLC16 | session-report |  | W4–W7 (SLC-16, Release 2) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC17.md | SESSION-SLC17 | session-report |  | W4–W7 (SLC-17, Release 3) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC18.md | SESSION-SLC18 | session-report |  | W4–W7 (SLC-18, Release 3) |  |  |  |
| spec/16-reports/SESSION-W4-W7-SLC19.md | SESSION-SLC19 | session-report |  | W4–W7 (SLC-19, Release 3) |  |  |  |
| spec/16-reports/SESSION-W8.md | SESSION-W8 | session-report |  | W8 — Solution & Technology Decisions |  |  |  |
| spec/16-reports/SESSION-W9.md | SESSION-W9 | session-report |  | W9 — Baseline Consolidation |  |  |  |
| spec/16-reports/SLC-00-WALKTHROUGH.md | SLC-00-WALKTHROUGH | conceptual-validation | SLC-00 Conceptual End-to-End Walkthrough (end of W3) | W3 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-FINAL-R1.md | GATE-FINAL-R1 | gate-report |  | W9 |  | FINAL (delegated) |  |
| spec/16-reports/gate-reports/GATE-STATUS-SLC01.md | GATE-SLC01 | gate-report |  | W7 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-SLC02.md | GATE-SLC02 | gate-report |  | W7 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-SLC03.md | GATE-SLC03 | gate-report |  | W7 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-SLC04.md | GATE-SLC04 | gate-report |  | W7 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-SLC05.md | GATE-SLC05 | gate-report |  | W7 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-SLC06.md | GATE-SLC06 | gate-report |  | W7 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-SLC07.md | GATE-SLC07 | gate-report |  | W7 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-SLC08.md | GATE-SLC08 | gate-report |  | W7 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-SLC11.md | GATE-SLC11 | gate-report |  | W7 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-SLC12a.md | GATE-SLC12A | gate-report |  | W7 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-W0.md | GATE-W0 | gate-report |  | W0 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-W1.md | GATE-W1 | gate-report |  | W1 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-W2.md | GATE-W2 | gate-report |  | W2 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-W3.md | GATE-W3 | gate-report |  | W3 |  | DRAFT |  |
| spec/16-reports/gate-reports/GATE-STATUS-W8.md | GATE-W8 | gate-report |  | W8 |  | DRAFT |  |
| spec/README.md |  |  |  |  |  |  |  |
