---
id: SYS-STUDY-ENTITY-INDEX
type: entity-index
title: Phase 2 -- Canonical Entity Index
status: DRAFT
generated_by: Claude (Dynamic Engineering System Reconstruction, Phase 2)
generated_at: '2026-09-29'
---

# Phase 2 -- Canonical Entity Index

**3999 معرّفًا (Entity ID) مكتشفًا آليًا** عبر 705 ملف، بستة أنماط اكتشاف: front-matter (`id:`, `state_machine:`)، عناوين `### ID`، عناصر قوائم غامقة بصيغتين (`- **ID**` و`- **ID وصف...**`)، وأول عمود في جداول الكتالوجات بصيغتين (خلية تحتوي المعرّف فقط، أو المعرّف متبوعًا بنص وصفي). لكل معرّف: أين عُرِّف (`defined_in`) وعدد الملفات الأخرى المستشهدة به (`ext_ref_count`) — وهذا العمود الأخير هو نفسه **Raw Relationship Graph** الذي تشير إليه `02-relationship-index.md`؛ لم أكرره في ملف منفصل لتفادي مصدرين للحقيقة لنفس البيانات. القيود المعروفة وأنواع الضجيج (Noise) موثّقة في `03-data-quality.md`.

## 1. Family Summary

| Family | Count | Orphans (0 external ref) |
|---|---|---|
| POL | 616 | 137 |
| EVT | 612 | 27 |
| CMD | 504 | 27 |
| INV | 302 | 0 |
| REQ | 213 | 3 |
| QRY | 160 | 27 |
| THR | 134 | 120 |
| TST | 108 | 0 |
| QAS | 96 | 3 |
| AGG | 89 | 0 |
| SM | 89 | 87 |
| UC | 86 |  |
| CAP | 69 |  |
| FM | 69 | 61 |
| CR | 64 | 7 |
| BO | 49 | 44 |
| WL | 38 | 27 |
| SL | 29 | 6 |
| OPENAPI | 28 | 27 |
| RSK | 28 | 5 |
| SESSION | 27 | 26 |
| DOM | 26 | 0 |
| UNK | 22 | 0 |
| SLC | 22 |  |
| TRACE | 20 | 19 |
| THREAT | 20 | 20 |
| SPEC | 20 |  |
| RD | 20 | 6 |
| FIT | 19 | 2 |
| OBS | 19 | 19 |
| LDM | 19 | 17 |
| FMEA | 19 | 19 |
| ASYNCAPI | 19 | 19 |
| POLICIES | 19 | 18 |
| TD | 19 | 5 |
| PROP | 19 | 18 |
| ATAM | 19 | 19 |
| ERRORS | 19 | 19 |
| GATE | 16 | 16 |
| ADR | 16 | 0 |
| DU | 16 | 0 |
| ACT | 15 | 15 |
| BRL | 15 |  |
| AI | 15 | 9 |
| PB | 14 | 5 |
| SR | 13 | 3 |
| DEP | 13 | 10 |
| HAP | 11 | 0 |
| TB | 10 | 0 |
| ASM | 10 | 6 |
| OQ | 9 | 0 |
| REG | 8 | 8 |
| BRQ | 8 | 0 |
| PRV | 7 | 7 |
| OUT | 6 | 0 |
| SH | 5 | 5 |
| CF | 5 | 3 |
| RTM | 2 |  |
| ANTI | 2 | 2 |
| ARCH | 2 | 2 |
| VALUE | 1 |  |
| SPATIAL | 1 |  |
| SLICE | 1 |  |
| AUDIT | 1 |  |
| OBJECT | 1 |  |
| UI | 1 | 0 |
| BC | 1 | 0 |
| TECH | 1 | 0 |
| TRUST | 1 |  |
| TEMPORAL | 1 | 0 |
| AUTHZ | 1 |  |
| CELL | 1 | 0 |
| ER | 1 | 0 |
| PL | 1 | 0 |
| PRIVACY | 1 |  |
| DR | 1 | 0 |
| PERF | 1 | 0 |
| META | 1 | 0 |
| LIB | 1 | 0 |
| FITNESS | 1 |  |
| LABEL | 1 | 0 |
| DEBT | 1 | 0 |
| LANGUAGE | 1 | 0 |
| CONFLICT | 1 | 0 |
| CLAIM | 1 |  |
| SCALE | 1 |  |
| CONTEXT | 1 |  |
| QUALITY | 1 | 0 |
| DATA | 1 |  |
| RELEASE | 1 | 0 |
| COST | 1 | 0 |

## 2. Full Index (grouped by family)


### Family: ACT

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| ACT-01 | 01-business/stakeholders.md | 0 |  |
| ACT-02 | 01-business/stakeholders.md | 0 |  |
| ACT-03 | 01-business/stakeholders.md | 0 |  |
| ACT-04 | 01-business/stakeholders.md | 0 |  |
| ACT-05 | 01-business/stakeholders.md | 0 |  |
| ACT-06 | 01-business/stakeholders.md | 0 |  |
| ACT-07 | 01-business/stakeholders.md | 0 |  |
| ACT-08 | 01-business/stakeholders.md | 0 |  |
| ACT-09 | 01-business/stakeholders.md | 0 |  |
| ACT-10 | 01-business/stakeholders.md | 0 |  |
| ACT-11 | 01-business/stakeholders.md | 0 |  |
| ACT-12 | 01-business/stakeholders.md | 0 |  |
| ACT-13 | 01-business/stakeholders.md | 0 |  |
| ACT-14 | 01-business/stakeholders.md | 0 |  |
| ACT-15 | 01-business/stakeholders.md | 0 |  |

### Family: ADR

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| ADR-P01 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P01.md | 110 | 00-governance/glossary.md; 00-governance/decisions/ADR-P02.md; 00-governance/elicitation/W1-answers.md; 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governanc ...(truncated) |
| ADR-P02 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P02.md | 101 | 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 03-d ...(truncated) |
| ADR-P03 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P03.md | 104 | 00-governance/elicitation/W1-answers.md; 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/risks.md; 00-governance/registers/unknowns.md; 01-b ...(truncated) |
| ADR-P04 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P04.md | 16 | 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/unknowns.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 04-information/object-envelop ...(truncated) |
| ADR-P05 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P05.md | 31 | README.md; 00-governance/decisions/ADR-P11.md; 00-governance/registers/assumptions.md; 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/risks ...(truncated) |
| ADR-P06 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P06.md | 124 | 00-governance/glossary.md; 00-governance/decisions/ADR-P12.md; 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/risks.md; 02-requirements/qua ...(truncated) |
| ADR-P07 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P07.md | 10 | 00-governance/glossary.md; 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/unknowns.md; 02-requirements/requirements.md; 03-domain/context-m ...(truncated) |
| ADR-P08 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P08.md | 20 | 00-governance/elicitation/W1-answers.md; 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/risks.md; 00-governance/registers/unknowns.md; 02-r ...(truncated) |
| ADR-P09 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P09.md | 13 | 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/risks.md; 00-governance/registers/unknowns.md; 02-requirements/requirements.md; 03-domain/co ...(truncated) |
| ADR-P10 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P10.md | 3 | 00-governance/glossary.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 16-reports/SESSION-W0.md |
| ADR-P11 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P11.md | 4 | 00-governance/registers/human-approvals.md; 03-domain/context-map.md; 08-security/authorization-model.md; 12-solution/technology-decisions.md |
| ADR-P12 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P12.md | 9 | 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/unknowns.md; 02-requirements/requirements.md; 03-domain/contexts/BC03/situation-alerting-spe ...(truncated) |
| ADR-P13 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P13.md | 99 | 00-governance/registers/human-approvals.md; 02-requirements/requirements.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 03-domain/c ...(truncated) |
| ADR-P14 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P14.md | 3 | 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 04-information/reference-data.md |
| ADR-P15 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P15.md | 9 | 00-governance/elicitation/W1-answers.md; 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/risks.md; 00-governance/registers/unknowns.md; 02-r ...(truncated) |
| ADR-P16 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/decisions/ADR-P16.md | 9 | 00-governance/registers/human-approvals.md; 02-requirements/requirements.md; 03-domain/contexts/BC07/discovery-architecture.md; 04-information/business-objects-kernel.md; 04-information/object-envelop ...(truncated) |

### Family: AGG

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| AGG-ADAPTER | 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 8 | 03-domain/contexts/BC07/commands-slc02.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 03-domain/contexts/BC07/events-slc02.md; 05-contracts/openapi-integration-slc02.md; 08-security/polic ...(truncated) |
| AGG-AI-REQUEST | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md;08-security/label-derivation-rules.md;14-slices/SLC-10/readiness.md | 7 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/events-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/acceptance/SLC-10/ai-request-state- ...(truncated) |
| AGG-AI-RESULT | 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md;08-security/label-derivation-rules.md;14-slices/SLC-10/readiness.md | 7 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/events-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/acceptance/SLC-10/ai-result-state-m ...(truncated) |
| AGG-AI-ROUTING | 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md;08-security/label-derivation-rules.md;14-slices/SLC-10/readiness.md | 9 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/events-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/acceptance/SLC-10/ai-routing-state- ...(truncated) |
| AGG-AI-TOOL | 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md;08-security/label-derivation-rules.md;14-slices/SLC-10/readiness.md | 7 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/events-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/acceptance/SLC-10/ai-tool-state-mac ...(truncated) |
| AGG-ALERT | 03-domain/contexts/BC03/aggregates/AGG-ALERT.md;08-security/label-derivation-rules.md;14-slices/SLC-06/readiness.md | 8 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies ...(truncated) |
| AGG-ALERT-RULE | 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md;08-security/label-derivation-rules.md;14-slices/SLC-06/readiness.md | 7 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/events-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-verification/acceptance/SLC-06/alert-r ...(truncated) |
| AGG-ALLOCATION | 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md;08-security/label-derivation-rules.md;14-slices/SLC-09/readiness.md | 17 | 00-governance/registers/corrections.md; 01-business/release-3-scope.md; 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/logistics-spec.md; 0 ...(truncated) |
| AGG-ANALYSIS-CASE | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md;08-security/label-derivation-rules.md;14-slices/SLC-07/readiness.md | 7 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/events-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/acceptance/SLC-07/analysi ...(truncated) |
| AGG-ANALYSIS-METHOD | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md;08-security/label-derivation-rules.md;14-slices/SLC-07/readiness.md | 7 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/events-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/acceptance/SLC-07/analysi ...(truncated) |
| AGG-ANALYSIS-RUN | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md;08-security/label-derivation-rules.md;14-slices/SLC-07/readiness.md | 7 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/events-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/acceptance/SLC-07/analysi ...(truncated) |
| AGG-ARCHIVE-PACKAGE | 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md;08-security/label-derivation-rules.md;14-slices/SLC-12/readiness.md | 7 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/events-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/acceptance/SLC-12/archive-pa ...(truncated) |
| AGG-ASSESSMENT | 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md;08-security/label-derivation-rules.md;14-slices/SLC-07/readiness.md | 7 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/events-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/acceptance/SLC-07/assessm ...(truncated) |
| AGG-ASSET | 03-domain/contexts/BC05/aggregates/AGG-ASSET.md;08-security/label-derivation-rules.md;14-slices/SLC-09/readiness.md | 9 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/logistics-spec.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 0 ...(truncated) |
| AGG-ASSET-ASSIGNMENT | 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md;08-security/label-derivation-rules.md;14-slices/SLC-09/readiness.md | 7 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/events-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verification/acceptance/SLC-09/asset-assi ...(truncated) |
| AGG-ASSET-RESERVATION | 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md;08-security/label-derivation-rules.md;14-slices/SLC-09/readiness.md | 7 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/events-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verification/acceptance/SLC-09/asset-rese ...(truncated) |
| AGG-ATTACHMENT | 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 8 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 12-solution/w8-inputs.md; 13-verification/ ...(truncated) |
| AGG-AUTHORITY-GRANT | 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 9 | 00-governance/registers/corrections.md; 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/events-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13- ...(truncated) |
| AGG-CAP-MESSAGE | 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md;08-security/label-derivation-rules.md;14-slices/SLC-16/readiness.md | 8 | 03-domain/contexts/BC03/commands-slc16.md; 03-domain/contexts/BC03/events-slc16.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 05-contracts/openapi-intelligence-slc16.md; 08-security/poli ...(truncated) |
| AGG-CLAIM | 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/acceptance/SLC-02/claim-st ...(truncated) |
| AGG-CLASSIFICATION-SCHEME | 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 8 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/events-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/classific ...(truncated) |
| AGG-CLEARANCE | 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 8 | 00-governance/registers/corrections.md; 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/events-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13- ...(truncated) |
| AGG-COLLECTION-PLAN | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md;08-security/label-derivation-rules.md;14-slices/SLC-14/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/events-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14.md; 13-verification/acceptance/SLC-14/collecti ...(truncated) |
| AGG-COLLECTION-REQUIREMENT | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md;08-security/label-derivation-rules.md;14-slices/SLC-14/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/events-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14.md; 13-verification/acceptance/SLC-14/collecti ...(truncated) |
| AGG-CONFLICT | 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md;08-security/label-derivation-rules.md;14-slices/SLC-04/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/events-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-verification/acceptance/SLC-04/conflict ...(truncated) |
| AGG-COORDINATION-CASE | 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md;08-security/label-derivation-rules.md;14-slices/SLC-15/readiness.md | 7 | 03-domain/contexts/BC04/commands-slc15.md; 03-domain/contexts/BC04/events-slc15.md; 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15.md; 13-verification/acceptance/SLC-15/coordinat ...(truncated) |
| AGG-CORRELATION-PROPOSAL | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md;08-security/label-derivation-rules.md;14-slices/SLC-15/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/events-slc15.md; 05-contracts/openapi-information-slc15.md; 08-security/policies-slc15.md; 13-verification/acceptance/SLC-15/correlat ...(truncated) |
| AGG-CORRELATION-RULE | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md;08-security/label-derivation-rules.md;14-slices/SLC-15/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/events-slc15.md; 05-contracts/openapi-information-slc15.md; 08-security/policies-slc15.md; 13-verification/acceptance/SLC-15/correlat ...(truncated) |
| AGG-DECISION | 03-domain/contexts/BC04/aggregates/AGG-DECISION.md;08-security/label-derivation-rules.md;14-slices/SLC-08/readiness.md | 7 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/events-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/acceptance/SLC-08/decision- ...(truncated) |
| AGG-DECISION-REQUEST | 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md;08-security/label-derivation-rules.md;14-slices/SLC-08/readiness.md | 7 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/events-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/acceptance/SLC-08/decision- ...(truncated) |
| AGG-DEVICE | 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md;08-security/label-derivation-rules.md;14-slices/SLC-11/readiness.md | 7 | 03-domain/contexts/BC01/commands-slc11.md; 03-domain/contexts/BC01/events-slc11.md; 05-contracts/openapi-foundation-slc11.md; 08-security/policies-slc11.md; 13-verification/acceptance/SLC-11/device-st ...(truncated) |
| AGG-DISPOSITION-RUN | 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md;08-security/label-derivation-rules.md;14-slices/SLC-12a/readiness.md | 7 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/events-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md; 13-verification/acceptance/SLC-12a/disp ...(truncated) |
| AGG-DISTRIBUTION | 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md;08-security/label-derivation-rules.md;14-slices/SLC-12/readiness.md | 7 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/events-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/acceptance/SLC-12/distributi ...(truncated) |
| AGG-ENTITY | 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/acceptance/SLC-02/entity-s ...(truncated) |
| AGG-ERASURE-REQUEST | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md;08-security/label-derivation-rules.md;14-slices/SLC-12a/readiness.md | 7 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/events-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md; 13-verification/acceptance/SLC-12a/eras ...(truncated) |
| AGG-ER-CASE | 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md;08-security/label-derivation-rules.md;14-slices/SLC-04/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/events-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-verification/acceptance/SLC-04/er-case- ...(truncated) |
| AGG-EVAL-SUITE | 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md;08-security/label-derivation-rules.md;14-slices/SLC-10/readiness.md | 8 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc1 ...(truncated) |
| AGG-EVIDENCE | 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/acceptance/SLC-02/evidence ...(truncated) |
| AGG-EVIDENCE-LINK | 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/acceptance/SLC-02/evidence ...(truncated) |
| AGG-EXERCISE | 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md;14-slices/SLC-19/readiness.md | 10 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/training-exercise-spec.md; 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc ...(truncated) |
| AGG-EXTERNAL-ID | 03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 8 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/openapi-information-slc02.md; 08-security/polic ...(truncated) |
| AGG-FINDING | 03-domain/contexts/BC03/aggregates/AGG-FINDING.md;08-security/label-derivation-rules.md;14-slices/SLC-07/readiness.md | 7 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/events-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/acceptance/SLC-07/finding ...(truncated) |
| AGG-HR-SYNC-PROPOSAL | 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md;08-security/label-derivation-rules.md;14-slices/SLC-16/readiness.md | 8 | 03-domain/contexts/BC01/commands-slc16.md; 03-domain/contexts/BC01/events-slc16.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 05-contracts/openapi-foundation-slc16.md; 08-security/polici ...(truncated) |
| AGG-IMPORT-BATCH | 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/acceptance/SLC-02/import-b ...(truncated) |
| AGG-INCIDENT | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md;08-security/label-derivation-rules.md;14-slices/SLC-17/readiness.md | 9 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC05/logistics-spec.md; 05-contracts/openapi-op ...(truncated) |
| AGG-INTEGRATION-CONNECTION | 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md;08-security/label-derivation-rules.md;14-slices/SLC-16/readiness.md | 7 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/events-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies-slc16.md; 13-verification/acceptance/SLC-16/integrat ...(truncated) |
| AGG-KNOWLEDGE-OBJECT | 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md;08-security/label-derivation-rules.md;14-slices/SLC-12/readiness.md | 13 | 00-governance/registers/corrections.md; 02-requirements/requirements.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/events-sl ...(truncated) |
| AGG-LEGAL-HOLD | 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md;08-security/label-derivation-rules.md;14-slices/SLC-12a/readiness.md | 7 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/events-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md; 13-verification/acceptance/SLC-12a/lega ...(truncated) |
| AGG-LOGISTICS-REQUEST | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md;14-slices/SLC-18/readiness.md | 10 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/training-exercise-spec.md; 05-contracts/openapi-r ...(truncated) |
| AGG-MAINTENANCE-ORDER | 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md;08-security/label-derivation-rules.md;14-slices/SLC-09/readiness.md | 8 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policie ...(truncated) |
| AGG-MATCH-RULESET | 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md;08-security/label-derivation-rules.md;14-slices/SLC-04/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/events-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-verification/acceptance/SLC-04/match-ru ...(truncated) |
| AGG-MODEL-VERSION | 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md;08-security/label-derivation-rules.md;14-slices/SLC-10/readiness.md | 8 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/events-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 12-solution/technology-decisions.md; 13-verificatio ...(truncated) |
| AGG-NOTIFICATION | 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md;08-security/label-derivation-rules.md;14-slices/SLC-06/readiness.md | 7 | 03-domain/contexts/BC04/commands-slc06.md; 03-domain/contexts/BC04/events-slc06.md; 05-contracts/openapi-operations-slc06.md; 08-security/policies-slc06.md; 13-verification/acceptance/SLC-06/notificat ...(truncated) |
| AGG-OBSERVATION | 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/acceptance/SLC-02/observat ...(truncated) |
| AGG-ORGANIZATION | 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 8 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/events-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/organizat ...(truncated) |
| AGG-OUTCOME-TRACKER | 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md;08-security/label-derivation-rules.md;14-slices/SLC-08/readiness.md | 7 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/events-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/acceptance/SLC-08/outcome-t ...(truncated) |
| AGG-PERSON | 03-domain/contexts/BC01/aggregates/AGG-PERSON.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 7 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/events-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/person-st ...(truncated) |
| AGG-PLAN | 03-domain/contexts/BC04/aggregates/AGG-PLAN.md;08-security/label-derivation-rules.md;14-slices/SLC-08/readiness.md | 13 | 00-governance/registers/corrections.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC05/tr ...(truncated) |
| AGG-PLAN-VERSION | 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md;08-security/label-derivation-rules.md;14-slices/SLC-08/readiness.md | 7 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/events-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/acceptance/SLC-08/plan-vers ...(truncated) |
| AGG-POLICY-SET | 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 8 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/events-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/policy-se ...(truncated) |
| AGG-PRELOAD-PACKAGE | 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md;08-security/label-derivation-rules.md;14-slices/SLC-11/readiness.md | 8 | 00-governance/glossary.md; 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/events-slc11.md; 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-verification/accep ...(truncated) |
| AGG-PRODUCT | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md;08-security/label-derivation-rules.md;14-slices/SLC-12/readiness.md | 7 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/events-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/acceptance/SLC-12/product-st ...(truncated) |
| AGG-PRODUCT-TEMPLATE | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md;08-security/label-derivation-rules.md;14-slices/SLC-12/readiness.md | 7 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/events-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/acceptance/SLC-12/product-te ...(truncated) |
| AGG-PROJECTION-VERSION | 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md;08-security/label-derivation-rules.md | 13 | 00-governance/registers/corrections.md; 03-domain/contexts/BC07/commands-slc05.md; 03-domain/contexts/BC07/discovery-architecture.md; 03-domain/contexts/BC07/events-slc05.md; 03-domain/contexts/BC07/g ...(truncated) |
| AGG-QUALIFICATION-RECORD | 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md;08-security/label-derivation-rules.md;14-slices/SLC-03/readiness.md | 15 | 01-business/release-3-scope.md; 02-requirements/requirements.md; 03-domain/contexts/BC05/commands-slc03.md; 03-domain/contexts/BC05/events-slc03.md; 03-domain/contexts/BC05/training-exercise-spec.md;  ...(truncated) |
| AGG-REALWORLD-EVENT | 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/acceptance/SLC-02/realworl ...(truncated) |
| AGG-RECONSTRUCTION | 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md;08-security/label-derivation-rules.md;14-slices/SLC-12/readiness.md | 7 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/events-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/acceptance/SLC-12/reconstruc ...(truncated) |
| AGG-RELATIONSHIP | 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/acceptance/SLC-02/relation ...(truncated) |
| AGG-RESOURCE-POOL | 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md;08-security/label-derivation-rules.md;14-slices/SLC-09/readiness.md | 17 | 01-business/release-3-scope.md; 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/logistics-spec.md ...(truncated) |
| AGG-RETENTION-SCHEDULE | 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md;08-security/label-derivation-rules.md;14-slices/SLC-12a/readiness.md | 7 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/events-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md; 13-verification/acceptance/SLC-12a/rete ...(truncated) |
| AGG-RISK | 03-domain/contexts/BC04/aggregates/AGG-RISK.md;08-security/label-derivation-rules.md;14-slices/SLC-17/readiness.md | 7 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/events-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-verification/acceptance/SLC-17/risk-stat ...(truncated) |
| AGG-ROLE | 03-domain/contexts/BC01/aggregates/AGG-ROLE.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 7 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/events-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/role-stat ...(truncated) |
| AGG-ROLE-ASSIGNMENT | 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 7 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/events-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/role-assi ...(truncated) |
| AGG-ROLE-REQUIREMENT | 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md;08-security/label-derivation-rules.md;14-slices/SLC-09/readiness.md | 11 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 05-contracts/ ...(truncated) |
| AGG-SCENARIO | 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md;14-slices/SLC-19/readiness.md | 7 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/events-slc19.md; 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-verification/acceptance/SLC-19/scenario-s ...(truncated) |
| AGG-SECURITY-EXCEPTION | 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 7 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/events-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/security- ...(truncated) |
| AGG-SENSOR-STREAM | 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md;08-security/label-derivation-rules.md;14-slices/SLC-16/readiness.md | 8 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 03-domain/contexts/BC07/events-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/polic ...(truncated) |
| AGG-SERVICE-ACCOUNT | 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 7 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/events-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/service-a ...(truncated) |
| AGG-SHIPMENT | 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md;14-slices/SLC-18/readiness.md | 11 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC0 ...(truncated) |
| AGG-SIMULATION | 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md;14-slices/SLC-19/readiness.md | 9 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/training-exercise-spec.md; 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc ...(truncated) |
| AGG-SITUATION | 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md;08-security/label-derivation-rules.md;14-slices/SLC-06/readiness.md | 7 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/events-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-verification/acceptance/SLC-06/situati ...(truncated) |
| AGG-SOURCE | 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md;08-security/label-derivation-rules.md;14-slices/SLC-02/readiness.md | 7 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/events-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/acceptance/SLC-02/source-s ...(truncated) |
| AGG-SUBSCRIPTION | 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md;08-security/label-derivation-rules.md;14-slices/SLC-06/readiness.md | 7 | 03-domain/contexts/BC04/commands-slc06.md; 03-domain/contexts/BC04/events-slc06.md; 05-contracts/openapi-operations-slc06.md; 08-security/policies-slc06.md; 13-verification/acceptance/SLC-06/subscript ...(truncated) |
| AGG-SYNC-CONFLICT | 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md;08-security/label-derivation-rules.md;14-slices/SLC-11/readiness.md | 12 | 00-governance/glossary.md; 00-governance/registers/corrections.md; 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/events-slc11.md; 03-domain/contexts/BC07/field-sync-protocol.md; 0 ...(truncated) |
| AGG-SYNC-SESSION | 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md;08-security/label-derivation-rules.md;14-slices/SLC-11/readiness.md | 7 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/events-slc11.md; 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-verification/acceptance/SLC-11/sync-session-s ...(truncated) |
| AGG-TASK | 03-domain/contexts/BC04/aggregates/AGG-TASK.md;08-security/label-derivation-rules.md;14-slices/SLC-03/readiness.md | 12 | 00-governance/registers/corrections.md; 00-governance/registers/open-questions.md; 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/risk-cont ...(truncated) |
| AGG-TASK-TYPE | 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md;08-security/label-derivation-rules.md;14-slices/SLC-03/readiness.md | 7 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/events-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verification/acceptance/SLC-03/task-type ...(truncated) |
| AGG-TENANT | 03-domain/contexts/BC01/aggregates/AGG-TENANT.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 9 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/events-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-sl ...(truncated) |
| AGG-USER | 03-domain/contexts/BC01/aggregates/AGG-USER.md;08-security/label-derivation-rules.md;14-slices/SLC-01/readiness.md | 8 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/events-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-sl ...(truncated) |

### Family: AI

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| AI-AUTONOMY-MATRIX | 10-ai/autonomy-matrix.md | 1 | 03-domain/contexts/BC07/grounded-ai-spec.md |
| AI-OP-01 | 10-ai/autonomy-matrix.md | 0 |  |
| AI-OP-02 | 10-ai/autonomy-matrix.md | 1 | 02-requirements/requirements.md |
| AI-OP-03 | 10-ai/autonomy-matrix.md | 2 | 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 13-verification/tooling/slice-sources.md |
| AI-OP-04 | 10-ai/autonomy-matrix.md | 3 | 02-requirements/requirements.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 13-verification/tooling/slice-sources.md |
| AI-OP-05 | 10-ai/autonomy-matrix.md | 3 | 02-requirements/requirements.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 13-verification/tooling/slice-sources.md |
| AI-OP-06 | 10-ai/autonomy-matrix.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 13-verification/tooling/slice-sources.md |
| AI-OP-07 | 10-ai/autonomy-matrix.md | 0 |  |
| AI-OP-08 | 10-ai/autonomy-matrix.md | 0 |  |
| AI-OP-F1 | 10-ai/autonomy-matrix.md | 0 |  |
| AI-OP-F2 | 10-ai/autonomy-matrix.md | 0 |  |
| AI-OP-F3 | 10-ai/autonomy-matrix.md | 0 |  |
| AI-OP-F4 | 10-ai/autonomy-matrix.md | 0 |  |
| AI-OP-F5 | 10-ai/autonomy-matrix.md | 0 |  |
| AI-OP-F6 | 10-ai/autonomy-matrix.md | 0 |  |

### Family: ANTI

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| ANTI-PATTERN-R1 | 16-reports/ANTI-PATTERN-REPORT-R1.md | 0 |  |
| ANTI-PATTERN-R2 | 16-reports/ANTI-PATTERN-REPORT-R2.md | 0 |  |

### Family: ARCH

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| ARCH-REVIEW-R1 | 16-reports/ARCHITECTURE-REVIEW-R1.md | 0 |  |
| ARCH-REVIEW-R2 | 16-reports/ARCHITECTURE-REVIEW-R2.md | 0 |  |

### Family: ASM

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| ASM-001 | 00-governance/registers/assumptions.md | 0 |  |
| ASM-002 | 00-governance/registers/assumptions.md | 0 |  |
| ASM-003 | 00-governance/registers/assumptions.md | 1 | 00-governance/registers/unknowns.md |
| ASM-004 | 00-governance/registers/assumptions.md | 0 |  |
| ASM-005 | 00-governance/registers/assumptions.md | 0 |  |
| ASM-006 | 00-governance/registers/assumptions.md | 0 |  |
| ASM-007 | 00-governance/registers/assumptions.md | 0 |  |
| ASM-008 | 00-governance/registers/assumptions.md | 3 | 00-governance/decisions/ADR-P02.md; 00-governance/elicitation/W1-answers.md; 12-solution/technology-decisions.md |
| ASM-009 | 00-governance/registers/assumptions.md | 1 | 00-governance/elicitation/W1-answers.md |
| ASM-010 | 00-governance/registers/assumptions.md | 5 | 00-governance/registers/risks.md; 07-quality/workloads-slc01.md; 12-solution/cell-architecture.md; 16-reports/EVOLUTION-ROADMAP.md; 16-reports/SESSION-W1.md |

### Family: ASYNCAPI

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| ASYNCAPI-SLC01 | 05-contracts/asyncapi-slc01.md | 0 |  |
| ASYNCAPI-SLC02 | 05-contracts/asyncapi-slc02.md | 0 |  |
| ASYNCAPI-SLC03 | 05-contracts/asyncapi-slc03.md | 0 |  |
| ASYNCAPI-SLC04 | 05-contracts/asyncapi-slc04.md | 0 |  |
| ASYNCAPI-SLC05 | 05-contracts/asyncapi-slc05.md | 0 |  |
| ASYNCAPI-SLC06 | 05-contracts/asyncapi-slc06.md | 0 |  |
| ASYNCAPI-SLC07 | 05-contracts/asyncapi-slc07.md | 0 |  |
| ASYNCAPI-SLC08 | 05-contracts/asyncapi-slc08.md | 0 |  |
| ASYNCAPI-SLC09 | 05-contracts/asyncapi-slc09.md | 0 |  |
| ASYNCAPI-SLC10 | 05-contracts/asyncapi-slc10.md | 0 |  |
| ASYNCAPI-SLC11 | 05-contracts/asyncapi-slc11.md | 0 |  |
| ASYNCAPI-SLC12 | 05-contracts/asyncapi-slc12.md | 0 |  |
| ASYNCAPI-SLC12A | 05-contracts/asyncapi-slc12a.md | 0 |  |
| ASYNCAPI-SLC14 | 05-contracts/asyncapi-slc14.md | 0 |  |
| ASYNCAPI-SLC15 | 05-contracts/asyncapi-slc15.md | 0 |  |
| ASYNCAPI-SLC16 | 05-contracts/asyncapi-slc16.md | 0 |  |
| ASYNCAPI-SLC17 | 05-contracts/asyncapi-slc17.md | 0 |  |
| ASYNCAPI-SLC18 | 05-contracts/asyncapi-slc18.md | 0 |  |
| ASYNCAPI-SLC19 | 05-contracts/asyncapi-slc19.md | 0 |  |

### Family: ATAM

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| ATAM-SLC01 | 14-slices/SLC-01/atam-lite.md | 0 |  |
| ATAM-SLC02 | 14-slices/SLC-02/atam-lite.md | 0 |  |
| ATAM-SLC03 | 14-slices/SLC-03/atam-lite.md | 0 |  |
| ATAM-SLC04 | 14-slices/SLC-04/atam-lite.md | 0 |  |
| ATAM-SLC05 | 14-slices/SLC-05/atam-lite.md | 0 |  |
| ATAM-SLC06 | 14-slices/SLC-06/atam-lite.md | 0 |  |
| ATAM-SLC07 | 14-slices/SLC-07/atam-lite.md | 0 |  |
| ATAM-SLC08 | 14-slices/SLC-08/atam-lite.md | 0 |  |
| ATAM-SLC09 | 14-slices/SLC-09/atam-lite.md | 0 |  |
| ATAM-SLC10 | 14-slices/SLC-10/atam-lite.md | 0 |  |
| ATAM-SLC11 | 14-slices/SLC-11/atam-lite.md | 0 |  |
| ATAM-SLC12 | 14-slices/SLC-12/atam-lite.md | 0 |  |
| ATAM-SLC12A | 14-slices/SLC-12a/atam-lite.md | 0 |  |
| ATAM-SLC14 | 14-slices/SLC-14/atam-lite.md | 0 |  |
| ATAM-SLC15 | 14-slices/SLC-15/atam-lite.md | 0 |  |
| ATAM-SLC16 | 14-slices/SLC-16/atam-lite.md | 0 |  |
| ATAM-SLC17 | 14-slices/SLC-17/atam-lite.md | 0 |  |
| ATAM-SLC18 | 14-slices/SLC-18/atam-lite.md | 0 |  |
| ATAM-SLC19 | 14-slices/SLC-19/atam-lite.md | 0 |  |

### Family: AUDIT

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| AUDIT-ARCHITECTURE | 08-security/audit-architecture.md | 0 |  |

### Family: AUTHZ

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| AUTHZ-MODEL | 08-security/authorization-model.md | 0 |  |

### Family: BC

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| BC-BOUNDARY-TEST | 03-domain/bc-boundary-test.md | 1 | 12-solution/deployment-units.md |

### Family: BO

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| BO-AI-REQUEST | 03-domain/ownership.md | 0 |  |
| BO-ALERT | 03-domain/ownership.md | 0 |  |
| BO-ANALYSIS-CASE | 03-domain/ownership.md | 0 |  |
| BO-ARCHIVE-RECORD | 03-domain/ownership.md | 0 |  |
| BO-ASSESSMENT | 03-domain/ownership.md | 0 |  |
| BO-ASSET | 03-domain/ownership.md | 0 |  |
| BO-AUDIT-RECORD | 03-domain/ownership.md | 0 |  |
| BO-AUTHORITY | 03-domain/ownership.md | 0 |  |
| BO-CATALOG-KERNEL | 04-information/business-objects-kernel.md | 0 |  |
| BO-CLAIM | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-CLASSIFICATION | 03-domain/ownership.md | 0 |  |
| BO-COLLECTION-REQUIREMENT | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-COMMUNICATION | 03-domain/ownership.md | 0 |  |
| BO-COMPETENCY | 03-domain/ownership.md | 0 |  |
| BO-CONFLICT | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-DECISION | 03-domain/ownership.md | 0 |  |
| BO-DECISION-REQUEST | 03-domain/ownership.md | 0 |  |
| BO-DELEGATION | 03-domain/ownership.md | 0 |  |
| BO-DEVICE | 03-domain/ownership.md | 1 | 14-slices/SLC-01/readiness.md |
| BO-ELIGIBILITY | 03-domain/ownership.md | 1 | 00-governance/registers/open-questions.md |
| BO-ENTITY | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-ER-CASE | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-EVENT | 03-domain/ownership.md;04-information/business-objects-kernel.md | 1 | 04-information/meta-model.md |
| BO-EVIDENCE | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-EXERCISE | 03-domain/ownership.md | 0 |  |
| BO-GEOMETRY | 03-domain/ownership.md | 0 |  |
| BO-IDENTITY | 03-domain/ownership.md | 0 |  |
| BO-INCIDENT | 03-domain/ownership.md | 0 |  |
| BO-KNOWLEDGE-OBJECT | 03-domain/ownership.md | 0 |  |
| BO-LINEAGE | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-LOGISTICS | 03-domain/ownership.md | 0 |  |
| BO-OBSERVATION | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-ORGANIZATION | 03-domain/ownership.md | 0 |  |
| BO-PLAN | 03-domain/ownership.md | 0 |  |
| BO-PLAN-OUTCOME | 03-domain/ownership.md | 1 | 00-governance/registers/corrections.md |
| BO-POLICY | 03-domain/ownership.md | 0 |  |
| BO-PRODUCT | 03-domain/ownership.md | 0 |  |
| BO-QUOTA | 03-domain/ownership.md | 0 |  |
| BO-RELATIONSHIP | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-RESOURCE | 03-domain/ownership.md | 0 |  |
| BO-RETENTION-SCHEDULE | 03-domain/ownership.md | 0 |  |
| BO-RISK | 03-domain/ownership.md | 0 |  |
| BO-SAMEAS | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-SECURITY-EXCEPTION | 03-domain/ownership.md | 0 |  |
| BO-SITUATION | 03-domain/ownership.md | 0 |  |
| BO-SITUATION-ALERT-RULE | 03-domain/ownership.md | 0 |  |
| BO-SOURCE | 03-domain/ownership.md;04-information/business-objects-kernel.md | 0 |  |
| BO-TASK | 03-domain/ownership.md | 0 |  |
| BO-TENANT | 03-domain/ownership.md | 1 | 00-governance/registers/unknowns.md |

### Family: BRL

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| BRL-001 | 01-business/business-rules.md | 3 | 00-governance/decisions/ADR-P03.md; 02-requirements/requirements.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| BRL-002 | 01-business/business-rules.md | 3 | 02-requirements/requirements.md; 04-information/conflict-model.md; 13-verification/acceptance/SLC-04/invariants-slc04.md |
| BRL-003 | 01-business/business-rules.md;16-reports/REQUIREMENTS-QUALITY-REPORT.md | 11 | 00-governance/registers/corrections.md; 00-governance/registers/unknowns.md; 02-requirements/requirements.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/decision-plan-spec.md;  ...(truncated) |
| BRL-004 | 01-business/business-rules.md | 6 | 00-governance/glossary.md; 02-requirements/requirements.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 13-verification/acceptance/SLC-08/inv ...(truncated) |
| BRL-005 | 01-business/business-rules.md;16-reports/REQUIREMENTS-QUALITY-REPORT.md | 8 | 00-governance/registers/open-questions.md; 02-requirements/requirements.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/aggregates ...(truncated) |
| BRL-006 | 01-business/business-rules.md | 6 | 02-requirements/requirements.md; 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 13-verification/acceptance/ ...(truncated) |
| BRL-007 | 01-business/business-rules.md;16-reports/REQUIREMENTS-QUALITY-REPORT.md | 5 | 00-governance/registers/open-questions.md; 02-requirements/requirements.md; 03-domain/contexts/BC05/eligibility-rules.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md; 13-verification/to ...(truncated) |
| BRL-008 | 01-business/business-rules.md | 3 | 02-requirements/requirements.md; 10-ai/autonomy-matrix.md; 16-reports/CONSISTENCY-CHECK-W3.md |
| BRL-009 | 01-business/business-rules.md | 5 | 02-requirements/requirements.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 04-information/provenance-lineage.md; 10-ai/autonomy-matrix.md; 13-verification/tooling/slice-sources.md |
| BRL-010 | 01-business/business-rules.md | 2 | 02-requirements/quality-scenarios.md; 02-requirements/requirements.md |
| BRL-011 | 01-business/business-rules.md | 3 | 00-governance/glossary.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 13-verification/tooling/slice-sources.md |
| BRL-012 | 01-business/business-rules.md | 0 |  |
| BRL-013 | 01-business/business-rules.md | 8 | 02-requirements/requirements.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONN ...(truncated) |
| BRL-014 | 01-business/business-rules.md | 2 | 03-domain/context-map.md; 13-verification/fitness-functions.md |
| BRL-015 | 01-business/business-rules.md | 2 | 02-requirements/quality-scenarios.md; 02-requirements/requirements.md |

### Family: BRQ

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| BRQ-001 | 02-requirements/requirements.md | 6 | 02-requirements/quality-scenarios.md; 07-quality/workloads-slc02.md; 07-quality/workloads-slc04.md; 07-quality/workloads-slc11.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |
| BRQ-002 | 02-requirements/requirements.md | 6 | 02-requirements/quality-scenarios.md; 07-quality/workloads-slc02.md; 07-quality/workloads-slc04.md; 07-quality/workloads-slc05.md; 07-quality/workloads-slc06.md; 15-traceability/rtm-r1.md |
| BRQ-003 | 02-requirements/requirements.md | 5 | 02-requirements/quality-scenarios.md; 07-quality/workloads-slc07.md; 07-quality/workloads-slc08.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |
| BRQ-004 | 02-requirements/requirements.md | 6 | 02-requirements/quality-scenarios.md; 07-quality/workloads-slc03.md; 07-quality/workloads-slc06.md; 07-quality/workloads-slc08.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |
| BRQ-005 | 02-requirements/requirements.md | 3 | 02-requirements/quality-scenarios.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |
| BRQ-006 | 02-requirements/requirements.md | 6 | 02-requirements/quality-scenarios.md; 07-quality/workloads-slc02.md; 07-quality/workloads-slc04.md; 07-quality/workloads-slc05.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |
| BRQ-007 | 02-requirements/requirements.md | 10 | 02-requirements/quality-scenarios.md; 07-quality/workloads-slc01.md; 07-quality/workloads-slc02.md; 07-quality/workloads-slc05.md; 07-quality/workloads-slc06.md; 07-quality/workloads-slc07.md; 07-qual ...(truncated) |
| BRQ-008 | 02-requirements/requirements.md | 3 | 02-requirements/quality-scenarios.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |

### Family: CAP

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| CAP-01 | 01-business/capabilities.md | 2 | 16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-01.01 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-01.02 | 01-business/capabilities.md | 4 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |
| CAP-01.03 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-01.04 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-02 | 01-business/capabilities.md | 2 | 16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-02.01 | 01-business/capabilities.md;16-reports/EVOLUTION-ROADMAP.md | 8 | 01-business/release-2-scope.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 13-verification/tooling/slice-sources.md; 14-slices/slices.md; 15-traceability/rtm-r2.md; 16-reports/CONS ...(truncated) |
| CAP-02.02 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-02.03 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-02.04 | 01-business/capabilities.md | 4 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |
| CAP-03 | 01-business/capabilities.md | 1 | 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-03.01 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-03.02 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-03.03 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-03.04 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-03.05 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-03.06 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-03.07 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-04 | 01-business/capabilities.md | 2 | 16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-04.01 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-04.02 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-04.03 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-04.04 | 01-business/capabilities.md | 8 | 01-business/release-2-scope.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 13-verification/tooling/slice-sources.md; 14-slices/slices.md; 15-traceability/rtm-r2.md; 16-reports/CONS ...(truncated) |
| CAP-05 | 01-business/capabilities.md | 1 | 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-05.01 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-05.02 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-05.03 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-06 | 01-business/capabilities.md | 2 | 16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-06.01 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-06.02 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-06.03 | 01-business/capabilities.md | 8 | 01-business/release-2-scope.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 13-verification/tooling/slice-sources.md; 14-slices/slices.md; 15-traceability/rtm-r2.md; 16-reports/CONS ...(truncated) |
| CAP-07 | 01-business/capabilities.md | 1 | 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-07.01 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-07.02 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-07.03 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-07.04 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-07.05 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-08 | 01-business/capabilities.md | 2 | 16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-08.01 | 01-business/capabilities.md | 5 | 01-business/release-2-scope.md; 02-requirements/requirements.md; 15-traceability/rtm-r2.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/ENGINEERING-BASELINE-R2.md |
| CAP-08.02 | 01-business/capabilities.md | 3 | 01-business/release-2-scope.md; 02-requirements/requirements.md; 15-traceability/rtm-r2.md |
| CAP-08.03 | 01-business/capabilities.md;01-business/release-3-scope.md | 5 | 02-requirements/requirements.md; 03-domain/contexts/BC05/logistics-spec.md; 13-verification/tooling/slice-sources.md; 14-slices/slices.md; 16-reports/SESSION-W4-W7-SLC17.md |
| CAP-08.04 | 01-business/capabilities.md | 5 | 01-business/release-2-scope.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |
| CAP-08.05 | 01-business/capabilities.md;01-business/release-3-scope.md | 4 | 02-requirements/requirements.md; 13-verification/tooling/slice-sources.md; 14-slices/slices.md; 16-reports/SESSION-W4-W7-SLC18.md |
| CAP-09 | 01-business/capabilities.md | 1 | 01-business/release-3-scope.md |
| CAP-09.01 | 01-business/capabilities.md;01-business/release-3-scope.md | 2 | 02-requirements/requirements.md; 13-verification/tooling/slice-sources.md |
| CAP-09.02 | 01-business/capabilities.md;01-business/release-3-scope.md | 1 | 02-requirements/requirements.md |
| CAP-09.03 | 01-business/capabilities.md;01-business/release-3-scope.md | 1 | 02-requirements/requirements.md |
| CAP-10 | 01-business/capabilities.md | 2 | 16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-10.01 | 01-business/capabilities.md | 4 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |
| CAP-10.02 | 01-business/capabilities.md | 6 | 01-business/release-2-scope.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r2.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/ENGINEERING-BASELINE-R2.md |
| CAP-11 | 01-business/capabilities.md | 2 | 16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-11.01 | 01-business/capabilities.md | 5 | 01-business/release-2-scope.md; 02-requirements/requirements.md; 15-traceability/rtm-r2.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/ENGINEERING-BASELINE-R2.md |
| CAP-11.02 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-11.03 | 01-business/capabilities.md | 3 | 01-business/release-2-scope.md; 02-requirements/requirements.md; 15-traceability/rtm-r2.md |
| CAP-12 | 01-business/capabilities.md | 1 | 16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md |
| CAP-12.01 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r2.md |
| CAP-12.02 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r2.md |
| CAP-12.03 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r2.md |
| CAP-12.04 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r2.md |
| CAP-13 | 01-business/capabilities.md | 1 | 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-13.01 | 01-business/capabilities.md | 4 | 00-governance/registers/corrections.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-13.02 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-13.03 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-13.04 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-14 | 01-business/capabilities.md | 1 | 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| CAP-14.01 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-14.02 | 01-business/capabilities.md | 2 | 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| CAP-14.03 | 01-business/capabilities.md | 3 | 02-requirements/requirements.md; 02-requirements/use-cases.md; 15-traceability/rtm-r1.md |
| CAP-MAP | 01-business/capabilities.md | 0 |  |

### Family: CELL

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| CELL-ARCHITECTURE | 12-solution/cell-architecture.md | 5 | 00-governance/glossary.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 07-quality/performance-test-strategy.md; 15-traceability/trace-platform.md; 16-reports/ARCHITECTURE-REVIEW-R1.md |

### Family: CF

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| CF-01 | 03-domain/contexts/BC02/conflict-detection-engine.md;04-information/conflict-model.md | 2 | 13-verification/acceptance/SLC-11/invariants-slc11.md; 16-reports/SLC-00-WALKTHROUGH.md |
| CF-02 | 03-domain/contexts/BC02/conflict-detection-engine.md;04-information/conflict-model.md | 0 |  |
| CF-03 | 03-domain/contexts/BC02/conflict-detection-engine.md;04-information/conflict-model.md | 0 |  |
| CF-04 | 03-domain/contexts/BC02/conflict-detection-engine.md;04-information/conflict-model.md | 0 |  |
| CF-05 | 03-domain/contexts/BC02/conflict-detection-engine.md;04-information/conflict-model.md | 8 | 00-governance/registers/corrections.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC07/field-sync-protocol.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 13-ver ...(truncated) |

### Family: CLAIM

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| CLAIM-EVIDENCE-MODEL | 04-information/claim-evidence-model.md | 0 |  |

### Family: CMD

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| CMD-ACS-ADD-ASSUMPTION | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-ADD-HYPOTHESIS | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-CANCEL | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-CLOSE | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-CREATE | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-DEFINE | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-DEFINE-SCENARIO | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-DESELECT-EVIDENCE | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-OPEN | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-RECLASSIFY | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-REOPEN | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-RETIRE-ASSUMPTION | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-SELECT-EVIDENCE | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ACS-UPDATE-HYPOTHESIS | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.m ...(truncated) |
| CMD-ADP-ACTIVATE | 03-domain/contexts/BC07/commands-slc02.md | 7 | 03-domain/contexts/BC07/events-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-integration-slc02.md; 08-security/policies-slc02.md; 13-v ...(truncated) |
| CMD-ADP-REGISTER | 03-domain/contexts/BC07/commands-slc02.md | 7 | 03-domain/contexts/BC07/events-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-integration-slc02.md; 08-security/policies-slc02.md; 13-v ...(truncated) |
| CMD-ADP-RESUME | 03-domain/contexts/BC07/commands-slc02.md | 7 | 03-domain/contexts/BC07/events-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-integration-slc02.md; 08-security/policies-slc02.md; 13-v ...(truncated) |
| CMD-ADP-RETIRE | 03-domain/contexts/BC07/commands-slc02.md | 7 | 03-domain/contexts/BC07/events-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-integration-slc02.md; 08-security/policies-slc02.md; 13-v ...(truncated) |
| CMD-ADP-SUSPEND | 03-domain/contexts/BC07/commands-slc02.md | 7 | 03-domain/contexts/BC07/events-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-integration-slc02.md; 08-security/policies-slc02.md; 13-v ...(truncated) |
| CMD-ADP-UPDATE-MAPPING | 03-domain/contexts/BC07/commands-slc02.md | 7 | 03-domain/contexts/BC07/events-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-integration-slc02.md; 08-security/policies-slc02.md; 13-v ...(truncated) |
| CMD-AIR-CANCEL | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verific ...(truncated) |
| CMD-AIRS-ACCEPT | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verifica ...(truncated) |
| CMD-AIRS-ACCEPT-PARTIALLY | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verifica ...(truncated) |
| CMD-AIRS-REJECT | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verifica ...(truncated) |
| CMD-AIRS-START-REVIEW | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verifica ...(truncated) |
| CMD-AIR-SUBMIT | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verific ...(truncated) |
| CMD-ALC-APPROVE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13- ...(truncated) |
| CMD-ALC-PREEMPT | 03-domain/contexts/BC05/commands-slc09.md | 9 | 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 05-contracts/errors-slc09.md; 05-contracts/openapi- ...(truncated) |
| CMD-ALC-RECORD-CONSUMPTION | 03-domain/contexts/BC05/commands-slc09.md | 11 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contract ...(truncated) |
| CMD-ALC-REJECT | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13- ...(truncated) |
| CMD-ALC-RELEASE | 03-domain/contexts/BC05/commands-slc09.md | 10 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 0 ...(truncated) |
| CMD-ALC-REQUEST | 03-domain/contexts/BC05/commands-slc09.md | 14 | 00-governance/registers/corrections.md; 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/training- ...(truncated) |
| CMD-ALR-ACKNOWLEDGE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-ve ...(truncated) |
| CMD-ALR-DISMISS | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-ve ...(truncated) |
| CMD-ALR-RESOLVE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-ve ...(truncated) |
| CMD-AMT-ACTIVATE | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07 ...(truncated) |
| CMD-AMT-DEPRECATE | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07 ...(truncated) |
| CMD-AMT-REGISTER | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07 ...(truncated) |
| CMD-AMT-RETIRE | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07 ...(truncated) |
| CMD-ARC-MIGRATE-FORMAT | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md ...(truncated) |
| CMD-ARC-REPAIR | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md ...(truncated) |
| CMD-ARC-RETRY-INGEST | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md ...(truncated) |
| CMD-ARC-TRANSFER | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md ...(truncated) |
| CMD-ARL-ACTIVATE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-ARL-DEFINE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-ARL-DISABLE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-ARL-EDIT | 03-domain/contexts/BC03/commands-slc06.md | 8 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-ARL-ENABLE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-ARL-RETIRE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-ASG-ASSIGN | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.m ...(truncated) |
| CMD-ASG-CANCEL | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.m ...(truncated) |
| CMD-ASG-RETURN | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.m ...(truncated) |
| CMD-ASM-DISCARD | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md;  ...(truncated) |
| CMD-ASM-DRAFT | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md;  ...(truncated) |
| CMD-ASM-EDIT | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md;  ...(truncated) |
| CMD-ASM-PUBLISH | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md;  ...(truncated) |
| CMD-ASM-RETURN | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md;  ...(truncated) |
| CMD-ASM-SUBMIT | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md;  ...(truncated) |
| CMD-ASM-WITHDRAW | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md;  ...(truncated) |
| CMD-AST-DISPOSE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-FAIL-MAINTENANCE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-MARK-UNSERVICEABLE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-RECLASSIFY | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-RECOVER | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-REGISTER | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-REPORT-LOST | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-RETURN-TO-SERVICE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-SET-CERTIFICATION | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-START-MAINTENANCE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-TRANSFER-CUSTODY | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-AST-UPDATE-CONDITION | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verif ...(truncated) |
| CMD-ATT-COMPLETE-UPLOAD | 03-domain/contexts/BC02/commands-slc02.md | 9 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-information-slc02 ...(truncated) |
| CMD-ATT-ERASE | 03-domain/contexts/BC02/commands-slc02.md | 8 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 1 ...(truncated) |
| CMD-ATT-INITIATE-UPLOAD | 03-domain/contexts/BC02/commands-slc02.md | 8 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-information-slc02 ...(truncated) |
| CMD-AUT-APPROVE-GRANT | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-AUT-DELEGATE | 03-domain/contexts/BC01/commands-slc01.md | 8 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-AUT-GRANT | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-AUT-REJECT-GRANT | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-AUT-RESUME | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-AUT-REVOKE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-AUT-SUSPEND | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-CAP-CANCEL | 03-domain/contexts/BC03/commands-slc16.md | 7 | 03-domain/contexts/BC03/events-slc16.md; 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-intelligence-slc16.md; 08-security/policies-slc16.md; ...(truncated) |
| CMD-CAP-PREPARE | 03-domain/contexts/BC03/commands-slc16.md | 7 | 03-domain/contexts/BC03/events-slc16.md; 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-intelligence-slc16.md; 08-security/policies-slc16.md; ...(truncated) |
| CMD-CAP-RELEASE | 03-domain/contexts/BC03/commands-slc16.md | 7 | 03-domain/contexts/BC03/events-slc16.md; 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-intelligence-slc16.md; 08-security/policies-slc16.md; ...(truncated) |
| CMD-CAP-RETRY | 03-domain/contexts/BC03/commands-slc16.md | 7 | 03-domain/contexts/BC03/events-slc16.md; 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-intelligence-slc16.md; 08-security/policies-slc16.md; ...(truncated) |
| CMD-CAT-BC01-SLC01 | 03-domain/contexts/BC01/commands-slc01.md | 0 |  |
| CMD-CAT-BC01-SLC11 | 03-domain/contexts/BC01/commands-slc11.md | 0 |  |
| CMD-CAT-BC01-SLC16 | 03-domain/contexts/BC01/commands-slc16.md | 0 |  |
| CMD-CAT-BC02-SLC02 | 03-domain/contexts/BC02/commands-slc02.md | 0 |  |
| CMD-CAT-BC02-SLC04 | 03-domain/contexts/BC02/commands-slc04.md | 0 |  |
| CMD-CAT-BC02-SLC14 | 03-domain/contexts/BC02/commands-slc14.md | 0 |  |
| CMD-CAT-BC02-SLC15 | 03-domain/contexts/BC02/commands-slc15.md | 0 |  |
| CMD-CAT-BC03-SLC06 | 03-domain/contexts/BC03/commands-slc06.md | 0 |  |
| CMD-CAT-BC03-SLC07 | 03-domain/contexts/BC03/commands-slc07.md | 0 |  |
| CMD-CAT-BC03-SLC16 | 03-domain/contexts/BC03/commands-slc16.md | 0 |  |
| CMD-CAT-BC04-SLC03 | 03-domain/contexts/BC04/commands-slc03.md | 0 |  |
| CMD-CAT-BC04-SLC06 | 03-domain/contexts/BC04/commands-slc06.md | 0 |  |
| CMD-CAT-BC04-SLC08 | 03-domain/contexts/BC04/commands-slc08.md | 0 |  |
| CMD-CAT-BC04-SLC15 | 03-domain/contexts/BC04/commands-slc15.md | 0 |  |
| CMD-CAT-BC04-SLC17 | 03-domain/contexts/BC04/commands-slc17.md | 0 |  |
| CMD-CAT-BC05-SLC03 | 03-domain/contexts/BC05/commands-slc03.md | 0 |  |
| CMD-CAT-BC05-SLC09 | 03-domain/contexts/BC05/commands-slc09.md | 0 |  |
| CMD-CAT-BC05-SLC18 | 03-domain/contexts/BC05/commands-slc18.md | 0 |  |
| CMD-CAT-BC05-SLC19 | 03-domain/contexts/BC05/commands-slc19.md | 0 |  |
| CMD-CAT-BC06-SLC12 | 03-domain/contexts/BC06/commands-slc12.md | 0 |  |
| CMD-CAT-BC07-SLC02 | 03-domain/contexts/BC07/commands-slc02.md | 0 |  |
| CMD-CAT-BC07-SLC05 | 03-domain/contexts/BC07/commands-slc05.md | 0 |  |
| CMD-CAT-BC07-SLC10 | 03-domain/contexts/BC07/commands-slc10.md | 0 |  |
| CMD-CAT-BC07-SLC11 | 03-domain/contexts/BC07/commands-slc11.md | 0 |  |
| CMD-CAT-BC07-SLC16 | 03-domain/contexts/BC07/commands-slc16.md | 0 |  |
| CMD-CAT-BC08-SLC01 | 03-domain/contexts/BC08/commands-slc01.md | 0 |  |
| CMD-CAT-BC08-SLC12A | 03-domain/contexts/BC08/commands-slc12a.md | 0 |  |
| CMD-CLM-ASSERT | 03-domain/contexts/BC02/commands-slc02.md | 11 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 03-domain/contexts/BC07/commands-slc10.md; 03-domain/context ...(truncated) |
| CMD-CLM-ASSESS | 03-domain/contexts/BC02/commands-slc02.md | 8 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 05-contracts/asyncapi-slc02.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-se ...(truncated) |
| CMD-CLM-CORRECT | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ver ...(truncated) |
| CMD-CLM-RECLASSIFY | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ver ...(truncated) |
| CMD-CLM-RECORD-CHANGE | 03-domain/contexts/BC02/commands-slc02.md | 8 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-inf ...(truncated) |
| CMD-CLM-RETRACT | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ver ...(truncated) |
| CMD-CLR-APPROVE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13- ...(truncated) |
| CMD-CLR-GRANT | 03-domain/contexts/BC01/commands-slc01.md | 8 | 00-governance/registers/corrections.md; 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc0 ...(truncated) |
| CMD-CLR-MODIFY | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13- ...(truncated) |
| CMD-CLR-REINSTATE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13- ...(truncated) |
| CMD-CLR-REVOKE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13- ...(truncated) |
| CMD-CLR-SUSPEND | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13- ...(truncated) |
| CMD-CLS-ACTIVATE | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-s ...(truncated) |
| CMD-CLS-DISCARD | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-s ...(truncated) |
| CMD-CLS-DRAFT | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-s ...(truncated) |
| CMD-CLS-EDIT | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-s ...(truncated) |
| CMD-CNF-ACCEPT | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13- ...(truncated) |
| CMD-CNF-ASSIGN | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13- ...(truncated) |
| CMD-CNF-RAISE | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13- ...(truncated) |
| CMD-CNF-REOPEN | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13- ...(truncated) |
| CMD-CNF-RESOLVE | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13- ...(truncated) |
| CMD-CNF-START-REVIEW | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13- ...(truncated) |
| CMD-CON-ACTIVATE | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies ...(truncated) |
| CMD-CON-FAIL-TEST | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies ...(truncated) |
| CMD-CON-REGISTER | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies ...(truncated) |
| CMD-CON-RESUME | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies ...(truncated) |
| CMD-CON-RETIRE | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies ...(truncated) |
| CMD-CON-SUSPEND | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies ...(truncated) |
| CMD-CON-TEST | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies ...(truncated) |
| CMD-CPL-ACTIVATE | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14. ...(truncated) |
| CMD-CPL-ADD-ACTIVITY | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14. ...(truncated) |
| CMD-CPL-CANCEL | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14. ...(truncated) |
| CMD-CPL-COMPLETE | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14. ...(truncated) |
| CMD-CPL-CREATE | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14. ...(truncated) |
| CMD-CPL-REMOVE-ACTIVITY | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14. ...(truncated) |
| CMD-CRD-ACTIVATE | 03-domain/contexts/BC04/commands-slc15.md | 7 | 03-domain/contexts/BC04/events-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRD-ADD-PARTICIPANT | 03-domain/contexts/BC04/commands-slc15.md | 7 | 03-domain/contexts/BC04/events-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRD-ASSIGN-RESPONSIBILITY | 03-domain/contexts/BC04/commands-slc15.md | 7 | 03-domain/contexts/BC04/events-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRD-CANCEL | 03-domain/contexts/BC04/commands-slc15.md | 7 | 03-domain/contexts/BC04/events-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRD-CLOSE | 03-domain/contexts/BC04/commands-slc15.md | 7 | 03-domain/contexts/BC04/events-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRD-OPEN | 03-domain/contexts/BC04/commands-slc15.md | 7 | 03-domain/contexts/BC04/events-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRD-REMOVE-PARTICIPANT | 03-domain/contexts/BC04/commands-slc15.md | 7 | 03-domain/contexts/BC04/events-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRD-REQUEST-DECISION | 03-domain/contexts/BC04/commands-slc15.md | 7 | 03-domain/contexts/BC04/events-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRD-UPDATE-RESPONSIBILITY | 03-domain/contexts/BC04/commands-slc15.md | 7 | 03-domain/contexts/BC04/events-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRP-ACCEPT | 03-domain/contexts/BC02/commands-slc15.md | 7 | 03-domain/contexts/BC02/events-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-information-slc15.md; 08-security/policies-s ...(truncated) |
| CMD-CRP-PROPOSE | 03-domain/contexts/BC02/commands-slc15.md | 7 | 03-domain/contexts/BC02/events-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-information-slc15.md; 08-security/policies-s ...(truncated) |
| CMD-CRP-REJECT | 03-domain/contexts/BC02/commands-slc15.md | 7 | 03-domain/contexts/BC02/events-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-information-slc15.md; 08-security/policies-s ...(truncated) |
| CMD-CRP-START-REVIEW | 03-domain/contexts/BC02/commands-slc15.md | 7 | 03-domain/contexts/BC02/events-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-information-slc15.md; 08-security/policies-s ...(truncated) |
| CMD-CRQ-AMEND | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies ...(truncated) |
| CMD-CRQ-APPROVE | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies ...(truncated) |
| CMD-CRQ-CANCEL | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies ...(truncated) |
| CMD-CRQ-DRAFT | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies ...(truncated) |
| CMD-CRQ-EDIT | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies ...(truncated) |
| CMD-CRQ-MARK-SATISFIED | 03-domain/contexts/BC02/commands-slc14.md | 8 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies ...(truncated) |
| CMD-CRQ-REJECT | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies ...(truncated) |
| CMD-CRQ-SUBMIT | 03-domain/contexts/BC02/commands-slc14.md | 7 | 03-domain/contexts/BC02/events-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/errors-slc14.md; 05-contracts/openapi-information-slc14.md; 08-security/policies ...(truncated) |
| CMD-CRR-ACTIVATE | 03-domain/contexts/BC02/commands-slc15.md | 7 | 03-domain/contexts/BC02/events-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-information-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRR-DEFINE | 03-domain/contexts/BC02/commands-slc15.md | 7 | 03-domain/contexts/BC02/events-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-information-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRR-EDIT | 03-domain/contexts/BC02/commands-slc15.md | 7 | 03-domain/contexts/BC02/events-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-information-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-CRR-RETIRE | 03-domain/contexts/BC02/commands-slc15.md | 7 | 03-domain/contexts/BC02/events-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md; 05-contracts/errors-slc15.md; 05-contracts/openapi-information-slc15.md; 08-security/policies-slc15 ...(truncated) |
| CMD-DEC-ANNUL | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-v ...(truncated) |
| CMD-DEC-RECORD | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-v ...(truncated) |
| CMD-DEV-CONFIRM | 03-domain/contexts/BC01/commands-slc11.md | 7 | 03-domain/contexts/BC01/events-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-foundation-slc11.md; 08-security/policies-slc11.md; 13-ver ...(truncated) |
| CMD-DEV-ENROLL | 03-domain/contexts/BC01/commands-slc11.md | 7 | 03-domain/contexts/BC01/events-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-foundation-slc11.md; 08-security/policies-slc11.md; 13-ver ...(truncated) |
| CMD-DEV-REINSTATE | 03-domain/contexts/BC01/commands-slc11.md | 7 | 03-domain/contexts/BC01/events-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-foundation-slc11.md; 08-security/policies-slc11.md; 13-ver ...(truncated) |
| CMD-DEV-REPORT-LOST | 03-domain/contexts/BC01/commands-slc11.md | 7 | 03-domain/contexts/BC01/events-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-foundation-slc11.md; 08-security/policies-slc11.md; 13-ver ...(truncated) |
| CMD-DEV-RETIRE | 03-domain/contexts/BC01/commands-slc11.md | 7 | 03-domain/contexts/BC01/events-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-foundation-slc11.md; 08-security/policies-slc11.md; 13-ver ...(truncated) |
| CMD-DEV-ROTATE-KEY | 03-domain/contexts/BC01/commands-slc11.md | 7 | 03-domain/contexts/BC01/events-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-foundation-slc11.md; 08-security/policies-slc11.md; 13-ver ...(truncated) |
| CMD-DEV-SUSPEND | 03-domain/contexts/BC01/commands-slc11.md | 7 | 03-domain/contexts/BC01/events-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-foundation-slc11.md; 08-security/policies-slc11.md; 13-ver ...(truncated) |
| CMD-DRQ-ADD-OPTION | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08. ...(truncated) |
| CMD-DRQ-CITE | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08. ...(truncated) |
| CMD-DRQ-CREATE | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08. ...(truncated) |
| CMD-DRQ-OPEN | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08. ...(truncated) |
| CMD-DRQ-WITHDRAW | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08. ...(truncated) |
| CMD-DSP-APPROVE | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc1 ...(truncated) |
| CMD-DSP-CANCEL | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc1 ...(truncated) |
| CMD-DSP-SUBMIT | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc1 ...(truncated) |
| CMD-DST-CANCEL | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 1 ...(truncated) |
| CMD-DST-DISTRIBUTE | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 1 ...(truncated) |
| CMD-ENT-CHANGE-TYPE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-ENT-RECLASSIFY | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-ENT-REGISTER | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-ENT-REINSTATE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-ENT-RETIRE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-ER-CONFIRM-MATCH | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-v ...(truncated) |
| CMD-ER-DECIDE-MATCH | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-v ...(truncated) |
| CMD-ER-DECIDE-NOT-MATCH | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-v ...(truncated) |
| CMD-ER-PARK | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-v ...(truncated) |
| CMD-ER-PROPOSE | 03-domain/contexts/BC02/commands-slc04.md | 9 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 05-contracts ...(truncated) |
| CMD-ER-REQUEST-SPLIT | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-v ...(truncated) |
| CMD-ER-RESUME | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-v ...(truncated) |
| CMD-ERS-APPROVE | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc1 ...(truncated) |
| CMD-ER-SPLIT | 03-domain/contexts/BC02/commands-slc04.md | 8 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-v ...(truncated) |
| CMD-ERS-REGISTER | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc1 ...(truncated) |
| CMD-ERS-REJECT | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc1 ...(truncated) |
| CMD-ER-START-REVIEW | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-v ...(truncated) |
| CMD-ER-WITHDRAW | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-v ...(truncated) |
| CMD-EVD-RECLASSIFY | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13- ...(truncated) |
| CMD-EVD-REGISTER | 03-domain/contexts/BC02/commands-slc02.md | 8 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-information-slc02.m ...(truncated) |
| CMD-EVD-SEAL | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13- ...(truncated) |
| CMD-EVD-TRANSFER-CUSTODY | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13- ...(truncated) |
| CMD-EVD-UPDATE-LOCATOR | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13- ...(truncated) |
| CMD-EVD-WITHDRAW | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13- ...(truncated) |
| CMD-EVL-LINK | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md ...(truncated) |
| CMD-EVL-UNLINK | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md ...(truncated) |
| CMD-EVS-ACTIVATE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verific ...(truncated) |
| CMD-EVS-DRAFT | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verific ...(truncated) |
| CMD-EVS-EDIT | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verific ...(truncated) |
| CMD-EXC-APPROVE | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc0 ...(truncated) |
| CMD-EXC-REJECT | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc0 ...(truncated) |
| CMD-EXC-REQUEST | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc0 ...(truncated) |
| CMD-EXC-REVOKE | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc0 ...(truncated) |
| CMD-EXR-CANCEL | 03-domain/contexts/BC05/commands-slc19.md | 10 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 05-contracts/errors-slc19.md; 05-contracts/openapi-readiness-slc19.md; 08- ...(truncated) |
| CMD-EXR-PLAN | 03-domain/contexts/BC05/commands-slc19.md | 15 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 05-contracts/errors-slc ...(truncated) |
| CMD-EXR-SCHEDULE | 03-domain/contexts/BC05/commands-slc19.md | 7 | 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 05-contracts/errors-slc19.md; 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-ve ...(truncated) |
| CMD-EXR-START | 03-domain/contexts/BC05/commands-slc19.md | 11 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 03-domain/contexts/BC05 ...(truncated) |
| CMD-EXT-END | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md;  ...(truncated) |
| CMD-EXT-MAP | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md;  ...(truncated) |
| CMD-FND-ACCEPT | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-FINDING.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13- ...(truncated) |
| CMD-FND-EDIT | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-FINDING.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13- ...(truncated) |
| CMD-FND-RECORD | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-FINDING.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13- ...(truncated) |
| CMD-FND-WITHDRAW | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-FINDING.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13- ...(truncated) |
| CMD-HRS-APPROVE | 03-domain/contexts/BC01/commands-slc16.md | 7 | 03-domain/contexts/BC01/events-slc16.md; 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-foundation-slc16.md; 08-security/policies-slc16. ...(truncated) |
| CMD-HRS-REJECT | 03-domain/contexts/BC01/commands-slc16.md | 7 | 03-domain/contexts/BC01/events-slc16.md; 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-foundation-slc16.md; 08-security/policies-slc16. ...(truncated) |
| CMD-IMP-ACCEPT-QUARANTINE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; ...(truncated) |
| CMD-IMP-CANCEL | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; ...(truncated) |
| CMD-IMP-REPROCESS-QUARANTINE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; ...(truncated) |
| CMD-IMP-SUBMIT | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; ...(truncated) |
| CMD-INC-ACTIVATE-CONTINGENCY | 03-domain/contexts/BC04/commands-slc17.md | 12 | 02-requirements/requirements.md; 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/errors-slc1 ...(truncated) |
| CMD-INC-ASSESS | 03-domain/contexts/BC04/commands-slc17.md | 7 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-v ...(truncated) |
| CMD-INC-CANCEL | 03-domain/contexts/BC04/commands-slc17.md | 7 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-v ...(truncated) |
| CMD-INC-CLOSE | 03-domain/contexts/BC04/commands-slc17.md | 8 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 09-r ...(truncated) |
| CMD-INC-CONTAIN | 03-domain/contexts/BC04/commands-slc17.md | 7 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-v ...(truncated) |
| CMD-INC-DE-ESCALATE | 03-domain/contexts/BC04/commands-slc17.md | 12 | 02-requirements/requirements.md; 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/errors-slc1 ...(truncated) |
| CMD-INC-DISPATCH-RESPONSE | 03-domain/contexts/BC04/commands-slc17.md | 7 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-v ...(truncated) |
| CMD-INC-ESCALATE | 03-domain/contexts/BC04/commands-slc17.md | 9 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operat ...(truncated) |
| CMD-INC-REPORT | 03-domain/contexts/BC04/commands-slc17.md | 7 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-v ...(truncated) |
| CMD-INC-RESOLVE | 03-domain/contexts/BC04/commands-slc17.md | 8 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-v ...(truncated) |
| CMD-KNO-DISCARD | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.m ...(truncated) |
| CMD-KNO-DRAFT | 03-domain/contexts/BC06/commands-slc12.md | 11 | 00-governance/registers/corrections.md; 02-requirements/requirements.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/ ...(truncated) |
| CMD-KNO-EDIT | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.m ...(truncated) |
| CMD-KNO-PUBLISH | 03-domain/contexts/BC06/commands-slc12.md | 8 | 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/errors-slc12.md; 05-contracts/op ...(truncated) |
| CMD-KNO-RECORD-REUSE | 03-domain/contexts/BC06/commands-slc12.md | 8 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/errors-slc12.md; 05-contra ...(truncated) |
| CMD-KNO-REJECT | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.m ...(truncated) |
| CMD-KNO-RETIRE | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.m ...(truncated) |
| CMD-KNO-RETURN | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.m ...(truncated) |
| CMD-KNO-SUBMIT | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.m ...(truncated) |
| CMD-LGR-CANCEL | 03-domain/contexts/BC05/commands-slc18.md | 10 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/errors-slc18.md; 05-contracts/openapi-readiness-slc1 ...(truncated) |
| CMD-LGR-DISPATCH | 03-domain/contexts/BC05/commands-slc18.md | 9 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/errors-slc18.md; 05-contracts/openapi-readiness-slc1 ...(truncated) |
| CMD-LGR-REQUEST | 03-domain/contexts/BC05/commands-slc18.md | 9 | 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/errors-slc18.md; 05-contracts/openapi-read ...(truncated) |
| CMD-LHD-APPROVE-RELEASE | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md ...(truncated) |
| CMD-LHD-CANCEL-RELEASE | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md ...(truncated) |
| CMD-LHD-EXTEND | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md ...(truncated) |
| CMD-LHD-PLACE | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md ...(truncated) |
| CMD-LHD-REQUEST-RELEASE | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md ...(truncated) |
| CMD-MDL-APPROVE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-veri ...(truncated) |
| CMD-MDL-DEPRECATE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-veri ...(truncated) |
| CMD-MDL-FAIL-EVALUATION | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-veri ...(truncated) |
| CMD-MDL-PROMOTE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-veri ...(truncated) |
| CMD-MDL-REGISTER | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-veri ...(truncated) |
| CMD-MDL-REINSTATE | 03-domain/contexts/BC07/commands-slc10.md | 8 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 09-reli ...(truncated) |
| CMD-MDL-RETIRE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-veri ...(truncated) |
| CMD-MDL-STAGE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-veri ...(truncated) |
| CMD-MDL-START-EVALUATION | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-veri ...(truncated) |
| CMD-MNT-CANCEL | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09. ...(truncated) |
| CMD-MNT-COMPLETE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09. ...(truncated) |
| CMD-MNT-PLAN | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09. ...(truncated) |
| CMD-MNT-RESCHEDULE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09. ...(truncated) |
| CMD-MNT-START | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09. ...(truncated) |
| CMD-MRS-ACTIVATE | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md ...(truncated) |
| CMD-MRS-DRAFT | 03-domain/contexts/BC02/commands-slc04.md | 6 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-verification/acceptance/S ...(truncated) |
| CMD-MRS-EDIT | 03-domain/contexts/BC02/commands-slc04.md | 7 | 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md; 05-contracts/errors-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md ...(truncated) |
| CMD-NTF-MARK-READ | 03-domain/contexts/BC04/commands-slc06.md | 7 | 03-domain/contexts/BC04/events-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-operations-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-OBS-AMEND | 03-domain/contexts/BC02/commands-slc02.md | 8 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-information-slc0 ...(truncated) |
| CMD-OBS-ATTACH-EVIDENCE | 03-domain/contexts/BC02/commands-slc02.md | 8 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-information-slc0 ...(truncated) |
| CMD-OBS-RECLASSIFY | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md;  ...(truncated) |
| CMD-OBS-RECORD | 03-domain/contexts/BC02/commands-slc02.md | 10 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-c ...(truncated) |
| CMD-OBS-REJECT | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md;  ...(truncated) |
| CMD-OBS-VALIDATE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md;  ...(truncated) |
| CMD-ORG-ADD-UNIT | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md;  ...(truncated) |
| CMD-ORG-CREATE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md;  ...(truncated) |
| CMD-ORG-DEACTIVATE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md;  ...(truncated) |
| CMD-ORG-DEACTIVATE-UNIT | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md;  ...(truncated) |
| CMD-ORG-MOVE-UNIT | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md;  ...(truncated) |
| CMD-ORG-REACTIVATE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md;  ...(truncated) |
| CMD-ORG-RENAME | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md;  ...(truncated) |
| CMD-ORG-RENAME-UNIT | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md;  ...(truncated) |
| CMD-OUT-CORRECT | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.m ...(truncated) |
| CMD-OUT-RECORD | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.m ...(truncated) |
| CMD-PER-DEACTIVATE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-ver ...(truncated) |
| CMD-PER-ERASE | 03-domain/contexts/BC01/commands-slc01.md | 10 | 00-governance/RATIFICATION-PACKAGE.md; 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md ...(truncated) |
| CMD-PER-REACTIVATE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-ver ...(truncated) |
| CMD-PER-REGISTER | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-ver ...(truncated) |
| CMD-PER-UPDATE-DETAILS | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-ver ...(truncated) |
| CMD-PKG-CONFIRM-DOWNLOAD | 03-domain/contexts/BC07/commands-slc11.md | 7 | 03-domain/contexts/BC07/events-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13 ...(truncated) |
| CMD-PKG-REQUEST | 03-domain/contexts/BC07/commands-slc11.md | 7 | 03-domain/contexts/BC07/events-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13 ...(truncated) |
| CMD-PKG-REVOKE | 03-domain/contexts/BC07/commands-slc11.md | 7 | 03-domain/contexts/BC07/events-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13 ...(truncated) |
| CMD-PLN-CANCEL | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verif ...(truncated) |
| CMD-PLN-CLOSE | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verif ...(truncated) |
| CMD-PLN-COMPLETE | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verif ...(truncated) |
| CMD-PLN-CREATE | 03-domain/contexts/BC04/commands-slc08.md | 9 | 00-governance/registers/corrections.md; 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; ...(truncated) |
| CMD-PLN-RECLASSIFY | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verif ...(truncated) |
| CMD-PLN-RESUME | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verif ...(truncated) |
| CMD-PLN-SUSPEND | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verif ...(truncated) |
| CMD-PLV-AMEND-MINOR | 03-domain/contexts/BC04/commands-slc08.md | 8 | 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-opera ...(truncated) |
| CMD-PLV-APPROVE | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md;  ...(truncated) |
| CMD-PLV-DISCARD | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md;  ...(truncated) |
| CMD-PLV-DRAFT | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md;  ...(truncated) |
| CMD-PLV-EDIT | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md;  ...(truncated) |
| CMD-PLV-REJECT | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md;  ...(truncated) |
| CMD-PLV-RETURN | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md;  ...(truncated) |
| CMD-PLV-SUBMIT | 03-domain/contexts/BC04/commands-slc08.md | 7 | 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/errors-slc08.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md;  ...(truncated) |
| CMD-POL-APPROVE | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13 ...(truncated) |
| CMD-POL-DRAFT | 03-domain/contexts/BC08/commands-slc01.md | 6 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| CMD-POL-EDIT | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13 ...(truncated) |
| CMD-POL-REJECT | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13 ...(truncated) |
| CMD-POL-SUBMIT | 03-domain/contexts/BC08/commands-slc01.md | 7 | 03-domain/contexts/BC08/events-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13 ...(truncated) |
| CMD-PRD-APPROVE | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-ver ...(truncated) |
| CMD-PRD-CREATE | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-ver ...(truncated) |
| CMD-PRD-DISCARD | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-ver ...(truncated) |
| CMD-PRD-EDIT-NARRATIVE | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-ver ...(truncated) |
| CMD-PRD-GENERATE | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-ver ...(truncated) |
| CMD-PRD-RETURN | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-ver ...(truncated) |
| CMD-PRD-SUBMIT | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-ver ...(truncated) |
| CMD-PRD-WITHDRAW | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-ver ...(truncated) |
| CMD-PRJ-CANCEL-BUILD | 03-domain/contexts/BC07/commands-slc05.md | 7 | 03-domain/contexts/BC07/events-slc05.md; 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/errors-slc05.md; 05-contracts/openapi-discovery-slc05.md; 08-security/policies-slc05 ...(truncated) |
| CMD-PRJ-CREATE-VERSION | 03-domain/contexts/BC07/commands-slc05.md | 7 | 03-domain/contexts/BC07/events-slc05.md; 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/errors-slc05.md; 05-contracts/openapi-discovery-slc05.md; 08-security/policies-slc05 ...(truncated) |
| CMD-PRJ-PROMOTE | 03-domain/contexts/BC07/commands-slc05.md | 7 | 03-domain/contexts/BC07/events-slc05.md; 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/errors-slc05.md; 05-contracts/openapi-discovery-slc05.md; 08-security/policies-slc05 ...(truncated) |
| CMD-PRJ-RETIRE | 03-domain/contexts/BC07/commands-slc05.md | 7 | 03-domain/contexts/BC07/events-slc05.md; 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/errors-slc05.md; 05-contracts/openapi-discovery-slc05.md; 08-security/policies-slc05 ...(truncated) |
| CMD-PTM-ACTIVATE | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.m ...(truncated) |
| CMD-PTM-DEFINE | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.m ...(truncated) |
| CMD-PTM-EDIT | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.m ...(truncated) |
| CMD-PTM-RETIRE | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.m ...(truncated) |
| CMD-QUAL-RECORD | 03-domain/contexts/BC05/commands-slc03.md | 11 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc03.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contract ...(truncated) |
| CMD-QUAL-REINSTATE | 03-domain/contexts/BC05/commands-slc03.md | 7 | 03-domain/contexts/BC05/events-slc03.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-readiness-slc03.md; 08-security/policies-slc ...(truncated) |
| CMD-QUAL-RENEW | 03-domain/contexts/BC05/commands-slc03.md | 9 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc03.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contract ...(truncated) |
| CMD-QUAL-REVOKE | 03-domain/contexts/BC05/commands-slc03.md | 8 | 03-domain/contexts/BC05/events-slc03.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-readiness-slc03.md; 08-security/policies-slc ...(truncated) |
| CMD-QUAL-SUSPEND | 03-domain/contexts/BC05/commands-slc03.md | 7 | 03-domain/contexts/BC05/events-slc03.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-readiness-slc03.md; 08-security/policies-slc ...(truncated) |
| CMD-RAS-ASSIGN | 03-domain/contexts/BC01/commands-slc01.md | 10 | 03-domain/contexts/BC01/commands-slc16.md; 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.m ...(truncated) |
| CMD-RAS-REVOKE | 03-domain/contexts/BC01/commands-slc01.md | 9 | 03-domain/contexts/BC01/commands-slc16.md; 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.m ...(truncated) |
| CMD-REC-CANCEL | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; ...(truncated) |
| CMD-REC-REQUEST | 03-domain/contexts/BC06/commands-slc12.md | 7 | 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md; 05-contracts/errors-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; ...(truncated) |
| CMD-REL-RECLASSIFY | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; ...(truncated) |
| CMD-REL-REGISTER | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; ...(truncated) |
| CMD-REL-REINSTATE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; ...(truncated) |
| CMD-REL-RETIRE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; ...(truncated) |
| CMD-RIS-ASSESS | 03-domain/contexts/BC04/commands-slc17.md | 7 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-verif ...(truncated) |
| CMD-RIS-CLOSE | 03-domain/contexts/BC04/commands-slc17.md | 7 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-verif ...(truncated) |
| CMD-RIS-IDENTIFY | 03-domain/contexts/BC04/commands-slc17.md | 7 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-verif ...(truncated) |
| CMD-RIS-PLAN-TREATMENT | 03-domain/contexts/BC04/commands-slc17.md | 7 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-verif ...(truncated) |
| CMD-RIS-REASSESS | 03-domain/contexts/BC04/commands-slc17.md | 7 | 03-domain/contexts/BC04/events-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/errors-slc17.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-verif ...(truncated) |
| CMD-ROL-ACTIVATE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-ROL-DEFINE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-ROL-RETIRE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-ROL-SET-PERMISSIONS | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-RPL-ADJUST-CAPACITY | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md;  ...(truncated) |
| CMD-RPL-CLOSE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md;  ...(truncated) |
| CMD-RPL-CREATE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md;  ...(truncated) |
| CMD-RPL-RESUME | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md;  ...(truncated) |
| CMD-RPL-SUSPEND | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md;  ...(truncated) |
| CMD-RRQ-ACTIVATE | 03-domain/contexts/BC05/commands-slc09.md | 8 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/errors-slc09.md; 05-contracts/op ...(truncated) |
| CMD-RRQ-DEFINE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.m ...(truncated) |
| CMD-RRQ-EDIT | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.m ...(truncated) |
| CMD-RRQ-RETIRE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.m ...(truncated) |
| CMD-RSV-CANCEL | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09. ...(truncated) |
| CMD-RSV-CONFIRM | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09. ...(truncated) |
| CMD-RSV-HOLD | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09. ...(truncated) |
| CMD-RSV-RELEASE | 03-domain/contexts/BC05/commands-slc09.md | 7 | 03-domain/contexts/BC05/events-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 05-contracts/errors-slc09.md; 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09. ...(truncated) |
| CMD-RTG-ACTIVATE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verific ...(truncated) |
| CMD-RTG-DISCARD | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verific ...(truncated) |
| CMD-RTG-DRAFT | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verific ...(truncated) |
| CMD-RTG-EDIT | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verific ...(truncated) |
| CMD-RTS-ACTIVATE | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-s ...(truncated) |
| CMD-RTS-DISCARD | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-s ...(truncated) |
| CMD-RTS-DRAFT | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-s ...(truncated) |
| CMD-RTS-EDIT | 03-domain/contexts/BC08/commands-slc12a.md | 7 | 03-domain/contexts/BC08/events-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md; 05-contracts/errors-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 08-security/policies-s ...(truncated) |
| CMD-RUN-CANCEL | 03-domain/contexts/BC03/commands-slc07.md | 7 | 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md ...(truncated) |
| CMD-RUN-REPRODUCE | 03-domain/contexts/BC03/commands-slc07.md | 8 | 00-governance/registers/corrections.md; 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence ...(truncated) |
| CMD-RUN-SUBMIT | 03-domain/contexts/BC03/commands-slc07.md | 10 | 00-governance/registers/corrections.md; 03-domain/contexts/BC03/events-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md; 05-contracts/errors-slc07.md; 05-contracts/openapi-intelligence ...(truncated) |
| CMD-RWE-CHANGE-TYPE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02. ...(truncated) |
| CMD-RWE-RECLASSIFY | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02. ...(truncated) |
| CMD-RWE-REGISTER | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02. ...(truncated) |
| CMD-RWE-REINSTATE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02. ...(truncated) |
| CMD-RWE-RETIRE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02. ...(truncated) |
| CMD-SCF-ASSIGN | 03-domain/contexts/BC07/commands-slc11.md | 7 | 03-domain/contexts/BC07/events-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-v ...(truncated) |
| CMD-SCF-DISCARD | 03-domain/contexts/BC07/commands-slc11.md | 7 | 03-domain/contexts/BC07/events-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-v ...(truncated) |
| CMD-SCF-REAPPLY | 03-domain/contexts/BC07/commands-slc11.md | 7 | 03-domain/contexts/BC07/events-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-v ...(truncated) |
| CMD-SCF-RESOLVE-MANUALLY | 03-domain/contexts/BC07/commands-slc11.md | 7 | 03-domain/contexts/BC07/events-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-v ...(truncated) |
| CMD-SCN-ACTIVATE | 03-domain/contexts/BC05/commands-slc19.md | 8 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 05-contracts/errors-slc19.md; 05-contracts/openapi-readiness-slc19.md; 08- ...(truncated) |
| CMD-SCN-DEFINE | 03-domain/contexts/BC05/commands-slc19.md | 7 | 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 05-contracts/errors-slc19.md; 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-ve ...(truncated) |
| CMD-SCN-EDIT | 03-domain/contexts/BC05/commands-slc19.md | 9 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 05-contracts/errors-slc19.md; 05-contracts/openapi-readiness-slc19.md; 08- ...(truncated) |
| CMD-SCN-RETIRE | 03-domain/contexts/BC05/commands-slc19.md | 7 | 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 05-contracts/errors-slc19.md; 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-ve ...(truncated) |
| CMD-SHP-CANCEL | 03-domain/contexts/BC05/commands-slc18.md | 10 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/errors-slc18.md; 05-contracts/openapi-readiness-slc18.md; 08- ...(truncated) |
| CMD-SHP-DELIVER | 03-domain/contexts/BC05/commands-slc18.md | 13 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/errors-slc18.md; 0 ...(truncated) |
| CMD-SHP-DEPART | 03-domain/contexts/BC05/commands-slc18.md | 10 | 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/errors-slc18.md; 05-contracts/openapi-readiness-slc18.md; 08-security/policies-slc18.md; 09-re ...(truncated) |
| CMD-SHP-PLAN | 03-domain/contexts/BC05/commands-slc18.md | 12 | 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/errors-slc18.md; 05-contracts/openapi-readiness-slc18.md; 06-data/logical-model/slc-18.md; 08- ...(truncated) |
| CMD-SHP-RECORD-CHECKPOINT | 03-domain/contexts/BC05/commands-slc18.md | 9 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/errors-slc18.md; 0 ...(truncated) |
| CMD-SHP-REPORT-DAMAGE | 03-domain/contexts/BC05/commands-slc18.md | 9 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/errors-slc18.md; 05-contracts/openapi-readiness-slc18.md; 08- ...(truncated) |
| CMD-SHP-REPORT-LOST | 03-domain/contexts/BC05/commands-slc18.md | 10 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/errors-slc18.md; 05-contracts/openapi-readiness-slc18.md; 08- ...(truncated) |
| CMD-SIM-ABORT | 03-domain/contexts/BC05/commands-slc19.md | 9 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/errors-s ...(truncated) |
| CMD-SIM-COMPLETE | 03-domain/contexts/BC05/commands-slc19.md | 12 | 02-requirements/quality-scenarios.md; 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/errors-slc19.md; 05-c ...(truncated) |
| CMD-SIM-DELIVER-INJECT | 03-domain/contexts/BC05/commands-slc19.md | 8 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/errors-slc19.md; 05-contracts/openapi-readiness-slc19.md; 0 ...(truncated) |
| CMD-SIM-PAUSE | 03-domain/contexts/BC05/commands-slc19.md | 8 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/errors-slc19.md; 05-contracts/openapi-readiness-slc19.md; 0 ...(truncated) |
| CMD-SIM-RECORD-EVALUATION | 03-domain/contexts/BC05/commands-slc19.md | 8 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/errors-slc19.md; 05-contracts/openapi-readiness-slc19.md; 0 ...(truncated) |
| CMD-SIM-RESUME | 03-domain/contexts/BC05/commands-slc19.md | 8 | 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/errors-slc19.md; 05-contracts/openapi-readiness-slc19.md; 0 ...(truncated) |
| CMD-SIM-START | 03-domain/contexts/BC05/commands-slc19.md | 9 | 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05 ...(truncated) |
| CMD-SIT-ACTIVATE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 1 ...(truncated) |
| CMD-SIT-CLOSE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 1 ...(truncated) |
| CMD-SIT-CREATE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 1 ...(truncated) |
| CMD-SIT-EDIT-DEFINITION | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 1 ...(truncated) |
| CMD-SIT-PAUSE | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 1 ...(truncated) |
| CMD-SIT-RECLASSIFY | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 1 ...(truncated) |
| CMD-SIT-RESUME | 03-domain/contexts/BC03/commands-slc06.md | 7 | 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 1 ...(truncated) |
| CMD-SNS-ACTIVATE | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies-slc16.md ...(truncated) |
| CMD-SNS-PAUSE | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies-slc16.md ...(truncated) |
| CMD-SNS-REGISTER | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies-slc16.md ...(truncated) |
| CMD-SNS-RETIRE | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies-slc16.md ...(truncated) |
| CMD-SNS-SET-QUALITY-RULES | 03-domain/contexts/BC07/commands-slc16.md | 7 | 03-domain/contexts/BC07/events-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/errors-slc16.md; 05-contracts/openapi-integration-slc16.md; 08-security/policies-slc16.md ...(truncated) |
| CMD-SRC-RATE-RELIABILITY | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-SRC-RECLASSIFY | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-SRC-REGISTER | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-SRC-REINSTATE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-SRC-RETIRE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-SRC-SET-PROTECTION | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-SRC-SUSPEND | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-SRC-UPDATE-PROFILE | 03-domain/contexts/BC02/commands-slc02.md | 7 | 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/errors-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-ve ...(truncated) |
| CMD-SUB-PAUSE | 03-domain/contexts/BC04/commands-slc06.md | 7 | 03-domain/contexts/BC04/events-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-operations-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-SUB-RESUME | 03-domain/contexts/BC04/commands-slc06.md | 7 | 03-domain/contexts/BC04/events-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-operations-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-SUB-SUBSCRIBE | 03-domain/contexts/BC04/commands-slc06.md | 7 | 03-domain/contexts/BC04/events-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-operations-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-SUB-UNSUBSCRIBE | 03-domain/contexts/BC04/commands-slc06.md | 7 | 03-domain/contexts/BC04/events-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-operations-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-SUB-UPDATE-CHANNELS | 03-domain/contexts/BC04/commands-slc06.md | 7 | 03-domain/contexts/BC04/events-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md; 05-contracts/errors-slc06.md; 05-contracts/openapi-operations-slc06.md; 08-security/policies-slc06.md;  ...(truncated) |
| CMD-SVC-CLOSE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-SVC-CREATE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-SVC-DISABLE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-SVC-ENABLE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-SVC-ROTATE-CREDENTIAL | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-SYN-OPEN | 03-domain/contexts/BC07/commands-slc11.md | 8 | 03-domain/contexts/BC07/events-slc11.md; 03-domain/contexts/BC07/field-sync-protocol.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-fiel ...(truncated) |
| CMD-SYN-UPLOAD-BATCH | 03-domain/contexts/BC07/commands-slc11.md | 7 | 03-domain/contexts/BC07/events-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md; 05-contracts/errors-slc11.md; 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-ve ...(truncated) |
| CMD-TASK-ACCEPT | 03-domain/contexts/BC04/commands-slc03.md | 8 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-operations-slc03.md; 08 ...(truncated) |
| CMD-TASK-ADD-RESULT-ITEM | 03-domain/contexts/BC04/commands-slc03.md | 8 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-operations-slc03.md; 08 ...(truncated) |
| CMD-TASK-APPROVE | 03-domain/contexts/BC04/commands-slc03.md | 8 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-ASSIGN | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-BLOCK | 03-domain/contexts/BC04/commands-slc03.md | 8 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-operations-slc03.md; 08 ...(truncated) |
| CMD-TASK-CANCEL | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-CLOSE | 03-domain/contexts/BC04/commands-slc03.md | 8 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-COMPLETE | 03-domain/contexts/BC04/commands-slc03.md | 8 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-CREATE | 03-domain/contexts/BC04/commands-slc03.md | 11 | 00-governance/registers/corrections.md; 02-requirements/requirements.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG- ...(truncated) |
| CMD-TASK-DECLINE | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-EDIT | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-ESCALATE | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-MARK-READY | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-REASSIGN | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-RECLASSIFY | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-REJECT | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-RESUME | 03-domain/contexts/BC04/commands-slc03.md | 8 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-operations-slc03.md; 08 ...(truncated) |
| CMD-TASK-RETURN | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-SET-DUE | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-s ...(truncated) |
| CMD-TASK-START | 03-domain/contexts/BC04/commands-slc03.md | 8 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-operations-slc03.md; 08 ...(truncated) |
| CMD-TASK-START-REVIEW | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TASK-SUBMIT | 03-domain/contexts/BC04/commands-slc03.md | 8 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-operations-slc03.md; 08 ...(truncated) |
| CMD-TASK-SUSPEND | 03-domain/contexts/BC04/commands-slc03.md | 6 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verification/acceptance/SLC-03/task ...(truncated) |
| CMD-TASK-UNSUSPEND | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verif ...(truncated) |
| CMD-TEN-COMPLETE-CELL-MIGRATION | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-TEN-COMPLETE-DECOMMISSION | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-TEN-COMPLETE-PROVISIONING | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-TEN-FAIL-PROVISIONING | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 08-security/policies-slc01.m ...(truncated) |
| CMD-TEN-PROVISION | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-ver ...(truncated) |
| CMD-TEN-REACTIVATE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-ver ...(truncated) |
| CMD-TEN-RETRY-PROVISIONING | 03-domain/contexts/BC01/commands-slc01.md | 6 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/te ...(truncated) |
| CMD-TEN-START-CELL-MIGRATION | 03-domain/contexts/BC01/commands-slc01.md | 8 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 12-sol ...(truncated) |
| CMD-TEN-START-DECOMMISSION | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-ver ...(truncated) |
| CMD-TEN-SUSPEND | 03-domain/contexts/BC01/commands-slc01.md | 6 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/te ...(truncated) |
| CMD-TEN-UPDATE-QUOTAS | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-ver ...(truncated) |
| CMD-TOL-ACTIVATE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verificati ...(truncated) |
| CMD-TOL-DISABLE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verificati ...(truncated) |
| CMD-TOL-ENABLE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verificati ...(truncated) |
| CMD-TOL-REGISTER | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verificati ...(truncated) |
| CMD-TOL-RETIRE | 03-domain/contexts/BC07/commands-slc10.md | 7 | 03-domain/contexts/BC07/events-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/errors-slc10.md; 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verificati ...(truncated) |
| CMD-TTY-ACTIVATE | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13- ...(truncated) |
| CMD-TTY-DEFINE | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13- ...(truncated) |
| CMD-TTY-EDIT | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13- ...(truncated) |
| CMD-TTY-RETIRE | 03-domain/contexts/BC04/commands-slc03.md | 7 | 03-domain/contexts/BC04/events-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 05-contracts/errors-slc03.md; 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13- ...(truncated) |
| CMD-USR-CLOSE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-USR-DISABLE | 03-domain/contexts/BC01/commands-slc01.md | 10 | 03-domain/contexts/BC01/commands-slc16.md; 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contr ...(truncated) |
| CMD-USR-ENABLE | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-USR-LINK-IDENTITY | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-USR-LINK-PERSON | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-USR-LOCK | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-USR-PROVISION | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-USR-RECORD-FIRST-SIGN-IN | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 08-security/policies-slc01.md; ...(truncated) |
| CMD-USR-UNLINK-IDENTITY | 03-domain/contexts/BC01/commands-slc01.md | 7 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/errors-slc01.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verif ...(truncated) |
| CMD-USR-UNLOCK | 03-domain/contexts/BC01/commands-slc01.md | 6 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/acceptance/SLC-01/user ...(truncated) |

### Family: CONFLICT

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| CONFLICT-MODEL | 04-information/conflict-model.md | 2 | 00-governance/registers/corrections.md; 03-domain/contexts/BC02/conflict-detection-engine.md |

### Family: CONTEXT

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| CONTEXT-MAP | 03-domain/context-map.md | 0 |  |

### Family: COST

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| COST-MODEL | 07-quality/cost-model.md | 2 | 00-governance/decisions/ADR-P05.md; 15-traceability/trace-platform.md |

### Family: CR

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| CR-01 | 00-governance/registers/corrections.md | 2 | 03-domain/ownership.md; 04-information/spatial-model.md |
| CR-02 | 00-governance/registers/corrections.md | 3 | 00-governance/registers/open-questions.md; 03-domain/ownership.md; 04-information/meta-model.md |
| CR-03 | 00-governance/registers/corrections.md | 4 | 00-governance/glossary.md; 02-requirements/requirements.md; 04-information/confidence-model.md; 04-information/object-envelope.md |
| CR-04 | 00-governance/registers/corrections.md | 2 | 00-governance/decisions/ADR-P01.md; 04-information/object-envelope.md |
| CR-05 | 00-governance/registers/corrections.md | 2 | 00-governance/decisions/ADR-P07.md; 03-domain/ownership.md |
| CR-06 | 00-governance/registers/corrections.md;16-reports/CONSISTENCY-REPORT-R1.md;16-reports/SESSION-W9.md | 1 | 03-domain/contexts/BC04/task-lifecycle-rules.md |
| CR-07 | 00-governance/registers/corrections.md | 0 |  |
| CR-08 | 00-governance/registers/corrections.md | 0 |  |
| CR-09 | 00-governance/registers/corrections.md | 2 | 01-business/value-streams.md; 02-requirements/use-cases.md |
| CR-10 | 00-governance/registers/corrections.md | 2 | 00-governance/decisions/ADR-P03.md; 01-business/business-rules.md |
| CR-11 | 00-governance/registers/corrections.md | 2 | 00-governance/decisions/ADR-P06.md; 02-requirements/requirements.md |
| CR-12 | 00-governance/registers/corrections.md | 3 | 00-governance/decisions/ADR-P12.md; 00-governance/decisions/ADR-P16.md; 04-information/spatial-model.md |
| CR-13 | 00-governance/registers/corrections.md | 1 | 00-governance/decisions/ADR-P09.md |
| CR-14 | 00-governance/registers/corrections.md | 1 | 00-governance/decisions/ADR-P04.md |
| CR-15 | 00-governance/registers/corrections.md | 2 | 02-requirements/requirements.md; 04-information/entity-resolution.md |
| CR-16 | 00-governance/registers/corrections.md | 2 | 00-governance/decisions/ADR-P02.md; 06-data/logical-model/slc-03.md |
| CR-17 | 00-governance/registers/corrections.md | 1 | 00-governance/decisions/ADR-P06.md |
| CR-18 | 00-governance/registers/corrections.md | 2 | 00-governance/decisions/ADR-P15.md; 04-information/language-model.md |
| CR-19 | 00-governance/registers/corrections.md | 1 | 00-governance/decisions/ADR-P14.md |
| CR-20 | 00-governance/registers/corrections.md | 0 |  |
| CR-21 | 00-governance/registers/corrections.md | 5 | 00-governance/decisions/ADR-P05.md; 12-solution/technology-decisions.md; 16-reports/ANTI-PATTERN-REPORT-R1.md; 16-reports/SESSION-W8.md; 16-reports/gate-reports/GATE-STATUS-W0.md |
| CR-22 | 00-governance/registers/corrections.md | 1 | 16-reports/gate-reports/GATE-STATUS-W0.md |
| CR-23 | 00-governance/registers/corrections.md | 0 |  |
| CR-24 | 00-governance/registers/corrections.md | 1 | 02-requirements/requirements.md |
| CR-25 | 00-governance/registers/corrections.md | 6 | 00-governance/decisions/ADR-P01.md; 01-business/business-rules.md; 02-requirements/requirements.md; 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md; 04-information/temporal-model.md; 13-verif ...(truncated) |
| CR-26 | 00-governance/registers/corrections.md | 0 |  |
| CR-27 | 00-governance/registers/corrections.md | 2 | 04-information/meta-model.md; 04-information/object-envelope.md |
| CR-28 | 00-governance/registers/corrections.md | 0 |  |
| CR-29 | 00-governance/registers/corrections.md | 11 | 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/aggregates/AGG ...(truncated) |
| CR-30 | 00-governance/registers/corrections.md | 1 | 01-business/outcomes.md |
| CR-31 | 00-governance/registers/corrections.md | 4 | 00-governance/glossary.md; 03-domain/bc-boundary-test.md; 03-domain/ownership.md; 04-information/claim-evidence-model.md |
| CR-32 | 00-governance/registers/corrections.md | 8 | 00-governance/glossary.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 00-governance/registers/unknowns.md; 01-business/business-rules.md; 02-requirements/requi ...(truncated) |
| CR-33 | 00-governance/registers/corrections.md | 5 | 00-governance/glossary.md; 00-governance/decisions/ADR-P11.md; 03-domain/ownership.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 13-verification/tooling/slice-sources.md |
| CR-34 | 00-governance/registers/corrections.md | 2 | 00-governance/glossary.md; 03-domain/ownership.md |
| CR-35 | 00-governance/registers/corrections.md | 1 | 00-governance/glossary.md |
| CR-36 | 00-governance/registers/corrections.md | 2 | 00-governance/glossary.md; 03-domain/ownership.md |
| CR-37 | 00-governance/registers/corrections.md | 2 | 00-governance/glossary.md; 03-domain/ownership.md |
| CR-38 | 00-governance/registers/corrections.md | 1 | 00-governance/glossary.md |
| CR-39 | 00-governance/registers/corrections.md | 2 | 00-governance/decisions/ADR-P08.md; 02-requirements/requirements.md |
| CR-40 | 00-governance/registers/corrections.md | 28 | 05-contracts/openapi-ai-slc10.md; 05-contracts/openapi-discovery-slc05.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-foundation-internal-slc01.md; 05-contracts/openapi-foundation-slc01 ...(truncated) |
| CR-41 | 00-governance/registers/corrections.md | 6 | 00-governance/glossary.md; 00-governance/decisions/ADR-P04.md; 03-domain/bc-boundary-test.md; 03-domain/domains.md; 03-domain/ownership.md; 16-reports/CONSISTENCY-CHECK-W3.md |
| CR-42 | 00-governance/registers/corrections.md | 4 | 01-business/release-3-scope.md; 03-domain/bc-boundary-test.md; 03-domain/domains.md; 16-reports/CONSISTENCY-CHECK-W3.md |
| CR-43 | 00-governance/registers/corrections.md | 1 | 00-governance/glossary.md |
| CR-44 | 00-governance/registers/corrections.md | 4 | 00-governance/glossary.md; 03-domain/ownership.md; 04-information/meta-model.md; 16-reports/SESSION-W3.md |
| CR-45 | 00-governance/registers/corrections.md | 3 | 07-quality/workloads-slc01.md; 08-security/audit-architecture.md; 16-reports/SESSION-W4-W7-SLC01.md |
| CR-46 | 00-governance/registers/corrections.md | 6 | 00-governance/RATIFICATION-PACKAGE.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 13-verification/tooling/slice-sources.md; 14-slices/SLC-03/readi ...(truncated) |
| CR-47 | 00-governance/registers/corrections.md | 10 | 00-governance/glossary.md; 00-governance/RATIFICATION-PACKAGE.md; 00-governance/decisions/ADR-P06.md; 03-domain/contexts/BC07/discovery-architecture.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 08 ...(truncated) |
| CR-48 | 00-governance/registers/corrections.md | 2 | 16-reports/METHODOLOGY-RETROSPECTIVE.md; 16-reports/SESSION-W4-W7-SLC08.md |
| CR-49 | 00-governance/registers/corrections.md | 6 | 03-domain/contexts/BC07/field-sync-protocol.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 04-information/conflict-model.md; 13-verification/acceptance/SLC-11/invariants-slc11.md; 13-ver ...(truncated) |
| CR-50 | 00-governance/registers/corrections.md | 5 | 03-domain/contexts/BC07/field-sync-protocol.md; 13-verification/acceptance/SLC-11/invariants-slc11.md; 14-slices/SLC-11/readiness.md; 16-reports/ENGINEERING-BASELINE-R1.md; 16-reports/SESSION-W4-W7-SL ...(truncated) |
| CR-51 | 00-governance/registers/corrections.md | 11 | 00-governance/glossary.md; 00-governance/decisions/ADR-P08.md; 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 08-security/key-hie ...(truncated) |
| CR-52 | 00-governance/registers/corrections.md | 1 | 16-reports/SESSION-W4-W7-SLC12a.md |
| CR-53 | 00-governance/registers/corrections.md | 1 | 16-reports/SESSION-W4-W7-SLC12a.md |
| CR-54 | 00-governance/registers/corrections.md | 2 | 09-reliability/dr-and-continuity.md; 16-reports/SESSION-W8.md |
| CR-55 | 00-governance/registers/corrections.md;16-reports/CONSISTENCY-REPORT-R1.md;16-reports/SESSION-W9.md | 3 | 14-slices/SLC-07/readiness.md; 16-reports/ENGINEERING-BASELINE-R1.md; 16-reports/METHODOLOGY-RETROSPECTIVE.md |
| CR-56 | 00-governance/registers/corrections.md;16-reports/CONSISTENCY-REPORT-R1.md;16-reports/SESSION-W9.md | 0 |  |
| CR-57 | 00-governance/registers/corrections.md;16-reports/CONSISTENCY-REPORT-R1.md;16-reports/SESSION-W9.md | 1 | 16-reports/METHODOLOGY-RETROSPECTIVE.md |
| CR-58 | 00-governance/registers/corrections.md | 7 | 03-domain/contexts/BC07/grounded-ai-spec.md; 12-solution/deployment-units.md; 14-slices/SLC-10/readiness.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/ENGINEERING-BASELINE-R2.md; 16-reports/SESS ...(truncated) |
| CR-59 | 00-governance/registers/corrections.md | 11 | 03-domain/contexts/BC02/collection-spec.md; 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 03-domain/contexts/BC04/commands-slc03.md; 03-domain/c ...(truncated) |
| CR-60 | 00-governance/registers/corrections.md | 12 | README.md; 01-business/release-3-scope.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC ...(truncated) |
| CR-61 | 00-governance/registers/corrections.md | 14 | README.md; 01-business/release-3-scope.md; 02-requirements/requirements.md; 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/risk-contingen ...(truncated) |
| CR-62 | 00-governance/registers/corrections.md | 20 | README.md; 01-business/release-3-scope.md; 02-requirements/requirements.md; 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/logistics-spec ...(truncated) |
| CR-63 | 00-governance/registers/corrections.md | 16 | README.md; 01-business/release-3-scope.md; 02-requirements/requirements.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC06/commands ...(truncated) |
| CR-64 | 00-governance/registers/corrections.md | 2 | 02-requirements/requirements.md; 02-requirements/use-cases.md |

### Family: DATA

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| DATA-PROTECTION | 08-security/data-protection.md | 0 |  |

### Family: DEBT

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| DEBT-001 | 00-governance/registers/technical-debt.md;14-slices/SLC-09/readiness.md | 12 | 02-requirements/requirements.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 06-data/logical-model/slc-09.md; 13-verification/acceptan ...(truncated) |

### Family: DEP

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| DEP-EXT-001 | 00-governance/registers/dependencies.md | 0 |  |
| DEP-EXT-002 | 00-governance/registers/dependencies.md | 0 |  |
| DEP-EXT-003 | 00-governance/registers/dependencies.md | 0 |  |
| DEP-EXT-004 | 00-governance/registers/dependencies.md | 0 |  |
| DEP-EXT-005 | 00-governance/registers/dependencies.md | 0 |  |
| DEP-EXT-006 | 00-governance/registers/dependencies.md | 0 |  |
| DEP-EXT-007 | 00-governance/registers/dependencies.md | 0 |  |
| DEP-EXT-008 | 00-governance/registers/dependencies.md | 0 |  |
| DEP-HUM-001 | 00-governance/registers/dependencies.md | 0 |  |
| DEP-HUM-002 | 00-governance/registers/dependencies.md | 1 | 16-reports/IMPLEMENTATION-READINESS-R1.md |
| DEP-HUM-003 | 00-governance/registers/dependencies.md | 2 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md |
| DEP-HUM-004 | 00-governance/registers/dependencies.md | 6 | 00-governance/RATIFICATION-PACKAGE.md; 00-governance/decisions/ADR-P05.md; 00-governance/registers/human-approvals.md; 12-solution/technology-decisions.md; 16-reports/IMPLEMENTATION-READINESS-R1.md; 1 ...(truncated) |
| DEP-ORG-001 | 00-governance/registers/dependencies.md | 0 |  |

### Family: DOM

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| DOM-01 | 03-domain/domains.md | 6 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 02-requirements/use-cases.md; 03-domain/bc-boundary-test.md; 03-domain/ownership.md; 16-reports/SESSION-W0.md |
| DOM-02 | 03-domain/domains.md | 4 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 02-requirements/use-cases.md; 03-domain/ownership.md |
| DOM-03 | 03-domain/domains.md | 7 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 03-domain/bc-boundary-test.md; 03-domain/ownership.md; 04-information/business-objects-kernel.md; 04-information/claim-evidence-mod ...(truncated) |
| DOM-04 | 03-domain/domains.md | 2 | 01-business/capabilities.md; 03-domain/ownership.md |
| DOM-05 | 03-domain/domains.md | 6 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 03-domain/ownership.md; 04-information/business-objects-kernel.md |
| DOM-06 | 03-domain/domains.md | 5 | 01-business/capabilities.md; 03-domain/ownership.md; 04-information/business-objects-kernel.md; 04-information/claim-evidence-model.md; 16-reports/SESSION-W0.md |
| DOM-07 | 03-domain/domains.md | 5 | 01-business/capabilities.md; 02-requirements/requirements.md; 03-domain/ownership.md; 04-information/business-objects-kernel.md; 04-information/entity-resolution.md |
| DOM-08 | 03-domain/domains.md | 3 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 03-domain/ownership.md |
| DOM-09 | 03-domain/domains.md | 2 | 01-business/capabilities.md; 03-domain/ownership.md |
| DOM-10 | 03-domain/domains.md | 6 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 01-business/stakeholders.md; 02-requirements/requirements.md; 03-domain/ownership.md; 16-reports/SESSION-W0.md |
| DOM-11 | 03-domain/domains.md | 3 | 01-business/capabilities.md; 02-requirements/use-cases.md; 03-domain/ownership.md |
| DOM-12 | 03-domain/domains.md | 3 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 03-domain/ownership.md |
| DOM-13 | 03-domain/domains.md | 3 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 03-domain/ownership.md |
| DOM-14 | 03-domain/domains.md | 3 | 01-business/capabilities.md; 02-requirements/requirements.md; 03-domain/ownership.md |
| DOM-15 | 03-domain/domains.md | 3 | 01-business/capabilities.md; 02-requirements/requirements.md; 03-domain/ownership.md |
| DOM-16 | 03-domain/domains.md | 14 | 00-governance/elicitation/W1-answers.md; 01-business/capabilities.md; 01-business/release-3-scope.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 03-domain/ownership.md; 03-domain/c ...(truncated) |
| DOM-17 | 03-domain/domains.md | 17 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 01-business/release-3-scope.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 03-domain/bc-boundary-test.md; 03-do ...(truncated) |
| DOM-18 | 03-domain/domains.md | 12 | 00-governance/elicitation/W1-answers.md; 01-business/capabilities.md; 01-business/release-3-scope.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 03-domain/ownership.md; 03-domain/c ...(truncated) |
| DOM-19 | 03-domain/domains.md | 9 | 00-governance/elicitation/W1-answers.md; 00-governance/registers/corrections.md; 01-business/capabilities.md; 01-business/release-3-scope.md; 02-requirements/requirements.md; 02-requirements/use-cases ...(truncated) |
| DOM-20 | 03-domain/domains.md | 4 | 01-business/capabilities.md; 02-requirements/requirements.md; 02-requirements/use-cases.md; 03-domain/ownership.md |
| DOM-21 | 03-domain/domains.md | 4 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 02-requirements/requirements.md; 03-domain/ownership.md |
| DOM-22 | 03-domain/domains.md | 3 | 01-business/capabilities.md; 02-requirements/requirements.md; 03-domain/ownership.md |
| DOM-23 | 03-domain/domains.md | 4 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 02-requirements/requirements.md; 03-domain/ownership.md |
| DOM-24 | 03-domain/domains.md | 1 | 01-business/capabilities.md |
| DOM-25 | 03-domain/domains.md | 4 | 00-governance/registers/corrections.md; 01-business/capabilities.md; 02-requirements/use-cases.md; 03-domain/ownership.md |
| DOM-26 | 03-domain/domains.md | 1 | 01-business/capabilities.md |

### Family: DR

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| DR-CONTINUITY | 09-reliability/dr-and-continuity.md | 4 | 00-governance/registers/corrections.md; 15-traceability/quality-verification-matrix.md; 15-traceability/trace-platform.md; 16-reports/IMPLEMENTATION-READINESS-R1.md |

### Family: DU

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| DU-01 | 12-solution/deployment-units.md | 2 | 09-reliability/dr-and-continuity.md; 12-solution/c4-containers.md |
| DU-02 | 12-solution/deployment-units.md | 1 | 12-solution/c4-containers.md |
| DU-03 | 12-solution/deployment-units.md | 1 | 12-solution/c4-containers.md |
| DU-04 | 12-solution/deployment-units.md | 1 | 12-solution/c4-containers.md |
| DU-05 | 12-solution/deployment-units.md | 1 | 12-solution/c4-containers.md |
| DU-06 | 12-solution/deployment-units.md | 2 | 09-reliability/dr-and-continuity.md; 12-solution/c4-containers.md |
| DU-07 | 12-solution/deployment-units.md | 1 | 12-solution/c4-containers.md |
| DU-08 | 12-solution/deployment-units.md | 6 | 01-business/release-3-scope.md; 12-solution/c4-containers.md; 16-reports/ANTI-PATTERN-REPORT-R1.md; 16-reports/ARCHITECTURE-REVIEW-R2.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/SESSION-R2-BAS ...(truncated) |
| DU-09 | 12-solution/deployment-units.md | 1 | 12-solution/c4-containers.md |
| DU-10 | 12-solution/deployment-units.md | 1 | 12-solution/c4-containers.md |
| DU-11 | 12-solution/deployment-units.md | 2 | 09-reliability/dr-and-continuity.md; 12-solution/c4-containers.md |
| DU-12 | 12-solution/deployment-units.md | 3 | 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 12-solution/c4-containers.md; 12-solution/ui-architecture.md |
| DU-13 | 12-solution/deployment-units.md | 1 | 12-solution/c4-containers.md |
| DU-14 | 12-solution/deployment-units.md | 4 | 16-reports/ARCHITECTURE-REVIEW-R2.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/ENGINEERING-BASELINE-R2.md; 16-reports/SESSION-R2-BASELINE.md |
| DU-15 | 12-solution/deployment-units.md | 4 | 16-reports/ARCHITECTURE-REVIEW-R2.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/ENGINEERING-BASELINE-R2.md; 16-reports/SESSION-R2-BASELINE.md |
| DU-16 | 12-solution/deployment-units.md | 3 | 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/ENGINEERING-BASELINE-R2.md; 16-reports/SESSION-R2-BASELINE.md |

### Family: ER

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| ER-MODEL | 04-information/entity-resolution.md | 9 | 00-governance/glossary.md; 02-requirements/requirements.md; 03-domain/ownership.md; 03-domain/contexts/BC02/candidate-generation.md; 03-domain/contexts/BC02/claims-temporal-kernel.md; 03-domain/contex ...(truncated) |

### Family: ERRORS

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| ERRORS-SLC01 | 05-contracts/errors-slc01.md | 0 |  |
| ERRORS-SLC02 | 05-contracts/errors-slc02.md | 0 |  |
| ERRORS-SLC03 | 05-contracts/errors-slc03.md | 0 |  |
| ERRORS-SLC04 | 05-contracts/errors-slc04.md | 0 |  |
| ERRORS-SLC05 | 05-contracts/errors-slc05.md | 0 |  |
| ERRORS-SLC06 | 05-contracts/errors-slc06.md | 0 |  |
| ERRORS-SLC07 | 05-contracts/errors-slc07.md | 0 |  |
| ERRORS-SLC08 | 05-contracts/errors-slc08.md | 0 |  |
| ERRORS-SLC09 | 05-contracts/errors-slc09.md | 0 |  |
| ERRORS-SLC10 | 05-contracts/errors-slc10.md | 0 |  |
| ERRORS-SLC11 | 05-contracts/errors-slc11.md | 0 |  |
| ERRORS-SLC12 | 05-contracts/errors-slc12.md | 0 |  |
| ERRORS-SLC12A | 05-contracts/errors-slc12a.md | 0 |  |
| ERRORS-SLC14 | 05-contracts/errors-slc14.md | 0 |  |
| ERRORS-SLC15 | 05-contracts/errors-slc15.md | 0 |  |
| ERRORS-SLC16 | 05-contracts/errors-slc16.md | 0 |  |
| ERRORS-SLC17 | 05-contracts/errors-slc17.md | 0 |  |
| ERRORS-SLC18 | 05-contracts/errors-slc18.md | 0 |  |
| ERRORS-SLC19 | 05-contracts/errors-slc19.md | 0 |  |

### Family: EVT

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| EVT-ACS-ASSUMPTION-ADDED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-ASSUMPTION-RETIRED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-CANCELLED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-CLOSED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-CREATED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-DEFINED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-EVIDENCE-DESELECTED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-EVIDENCE-SELECTED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-HYPOTHESIS-ADDED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-HYPOTHESIS-UPDATED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-OPENED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-RECLASSIFIED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-REOPENED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ACS-SCENARIO-DEFINED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptan ...(truncated) |
| EVT-ADP-ACTIVATED | 03-domain/contexts/BC07/events-slc02.md | 6 | 03-domain/contexts/BC07/commands-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-integration-slc02.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ADP-MAPPING-UPDATED | 03-domain/contexts/BC07/events-slc02.md | 6 | 03-domain/contexts/BC07/commands-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-integration-slc02.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ADP-REGISTERED | 03-domain/contexts/BC07/events-slc02.md | 6 | 03-domain/contexts/BC07/commands-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-integration-slc02.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ADP-RESUMED | 03-domain/contexts/BC07/events-slc02.md | 6 | 03-domain/contexts/BC07/commands-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-integration-slc02.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ADP-RETIRED | 03-domain/contexts/BC07/events-slc02.md | 6 | 03-domain/contexts/BC07/commands-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-integration-slc02.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ADP-SUSPENDED | 03-domain/contexts/BC07/events-slc02.md | 6 | 03-domain/contexts/BC07/commands-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-integration-slc02.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-AIR-CANCELLED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai- ...(truncated) |
| EVT-AIR-COMPLETED | 03-domain/contexts/BC07/events-slc10.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 05-contracts/asyncapi-slc10.md; 13-verification/tooling/slice-sources.md |
| EVT-AIR-CONTEXT-SEALED | 03-domain/contexts/BC07/events-slc10.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 05-contracts/asyncapi-slc10.md; 13-verification/tooling/slice-sources.md |
| EVT-AIR-FAILED | 03-domain/contexts/BC07/events-slc10.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 05-contracts/asyncapi-slc10.md; 13-verification/tooling/slice-sources.md |
| EVT-AIR-INSUFFICIENT-EVIDENCE | 03-domain/contexts/BC07/events-slc10.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 05-contracts/asyncapi-slc10.md; 13-verification/tooling/slice-sources.md |
| EVT-AIR-RECEIVED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai- ...(truncated) |
| EVT-AIR-REFUSED | 03-domain/contexts/BC07/events-slc10.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 05-contracts/asyncapi-slc10.md; 13-verification/tooling/slice-sources.md |
| EVT-AIR-RETRIEVING | 03-domain/contexts/BC07/events-slc10.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 05-contracts/asyncapi-slc10.md; 13-verification/tooling/slice-sources.md |
| EVT-AIRS-ACCEPTED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai-r ...(truncated) |
| EVT-AIRS-PARTIALLY-ACCEPTED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai-r ...(truncated) |
| EVT-AIRS-PROPOSED | 03-domain/contexts/BC07/events-slc10.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 05-contracts/asyncapi-slc10.md; 13-verification/tooling/slice-sources.md |
| EVT-AIRS-REJECTED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai-r ...(truncated) |
| EVT-AIRS-REVIEW-STARTED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai-r ...(truncated) |
| EVT-ALC-APPROVAL-REQUIRED | 03-domain/contexts/BC05/events-slc09.md | 5 | 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/asyncapi-slc09.md; 13-verification/acceptance/SLC-18/invariants-slc18.md ...(truncated) |
| EVT-ALC-COMMITTED | 03-domain/contexts/BC05/events-slc09.md | 12 | 02-requirements/requirements.md; 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 03-domain/contexts/BC05/agg ...(truncated) |
| EVT-ALC-CONSUMED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-ALC-PREEMPTED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-ALC-REJECTED | 03-domain/contexts/BC05/events-slc09.md | 8 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/asyncapi-slc09.md; 05-contrac ...(truncated) |
| EVT-ALC-RELEASED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-ALC-REQUESTED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-ALR-ACKNOWLEDGED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-ALR-DISMISSED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-ALR-ESCALATED | 03-domain/contexts/BC03/events-slc06.md | 3 | 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 05-contracts/asyncapi-slc06.md; 13-verification/tooling/slice-sources.md |
| EVT-ALR-RAISED | 03-domain/contexts/BC03/events-slc06.md | 3 | 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 05-contracts/asyncapi-slc06.md; 13-verification/tooling/slice-sources.md |
| EVT-ALR-REPEATED | 03-domain/contexts/BC03/events-slc06.md | 3 | 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 05-contracts/asyncapi-slc06.md; 13-verification/tooling/slice-sources.md |
| EVT-ALR-RESOLVED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-AMT-ACTIVATED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/accept ...(truncated) |
| EVT-AMT-DEPRECATED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/accept ...(truncated) |
| EVT-AMT-REGISTERED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/accept ...(truncated) |
| EVT-AMT-RETIRED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/accept ...(truncated) |
| EVT-ARC-ARCHIVED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-ARC-DISPOSED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-ARC-FORMAT-MIGRATED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptanc ...(truncated) |
| EVT-ARC-INGEST-FAILED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-ARC-INGEST-STARTED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptanc ...(truncated) |
| EVT-ARC-INTEGRITY-FAILED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-ARC-REPAIRED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptanc ...(truncated) |
| EVT-ARC-TRANSFERRED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptanc ...(truncated) |
| EVT-ARL-ACTIVATED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ARL-DEFINED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ARL-DISABLED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ARL-EDITED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ARL-ENABLED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ARL-RETIRED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ASG-ASSIGNED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptan ...(truncated) |
| EVT-ASG-CANCELLED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptan ...(truncated) |
| EVT-ASG-RETURNED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptan ...(truncated) |
| EVT-ASM-DISCARDED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ASM-DRAFTED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ASM-EDITED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ASM-PUBLISHED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ASM-RETURNED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ASM-SUBMITTED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ASM-SUPERSEDED | 03-domain/contexts/BC03/events-slc07.md | 3 | 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/asyncapi-slc07.md; 13-verification/tooling/slice-sources.md |
| EVT-ASM-WITHDRAWN | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/ ...(truncated) |
| EVT-AST-CERTIFICATION-SET | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-AST-CONDITION-UPDATED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-AST-CUSTODY-TRANSFERRED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-AST-DISPOSED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-AST-MAINTENANCE-STARTED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-AST-RECLASSIFIED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-AST-RECOVERED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-AST-REGISTERED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-AST-REPORTED-LOST | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-AST-RETURNED-TO-SERVICE | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-AST-UNSERVICEABLE | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/a ...(truncated) |
| EVT-ATT-ERASED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/S ...(truncated) |
| EVT-ATT-EXPIRED | 03-domain/contexts/BC02/events-slc02.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 05-contracts/asyncapi-slc02.md; 13-verification/tooling/slice-sources.md |
| EVT-ATT-QUARANTINED | 03-domain/contexts/BC02/events-slc02.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 05-contracts/asyncapi-slc02.md; 13-verification/tooling/slice-sources.md |
| EVT-ATT-STORED | 03-domain/contexts/BC02/events-slc02.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 05-contracts/asyncapi-slc02.md; 13-verification/tooling/slice-sources.md |
| EVT-ATT-UPLOADED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/S ...(truncated) |
| EVT-ATT-UPLOAD-INITIATED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/S ...(truncated) |
| EVT-AUT-DELEGATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-AUT-EXPIRED | 03-domain/contexts/BC01/events-slc01.md | 3 | 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/asyncapi-slc01.md; 13-verification/tooling/slice-sources.md |
| EVT-AUT-GRANTED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-AUT-GRANT-REJECTED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-AUT-GRANT-REQUESTED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-AUT-RESUMED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-AUT-REVOKED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-AUT-SUSPENDED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-CAP-CANCELLED | 03-domain/contexts/BC03/events-slc16.md | 6 | 03-domain/contexts/BC03/commands-slc16.md; 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-intelligence-slc16.md; 13-verification/acceptance ...(truncated) |
| EVT-CAP-FAILED | 03-domain/contexts/BC03/events-slc16.md | 3 | 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md; 05-contracts/asyncapi-slc16.md; 13-verification/tooling/slice-sources.md |
| EVT-CAP-PREPARED | 03-domain/contexts/BC03/events-slc16.md | 6 | 03-domain/contexts/BC03/commands-slc16.md; 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-intelligence-slc16.md; 13-verification/acceptance ...(truncated) |
| EVT-CAP-RETRY | 03-domain/contexts/BC03/events-slc16.md | 6 | 03-domain/contexts/BC03/commands-slc16.md; 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-intelligence-slc16.md; 13-verification/acceptance ...(truncated) |
| EVT-CAP-SENT | 03-domain/contexts/BC03/events-slc16.md | 6 | 03-domain/contexts/BC03/commands-slc16.md; 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-intelligence-slc16.md; 13-verification/acceptance ...(truncated) |
| EVT-CAT-BC01-SLC01 | 03-domain/contexts/BC01/events-slc01.md | 0 |  |
| EVT-CAT-BC01-SLC11 | 03-domain/contexts/BC01/events-slc11.md | 0 |  |
| EVT-CAT-BC01-SLC16 | 03-domain/contexts/BC01/events-slc16.md | 0 |  |
| EVT-CAT-BC02-SLC02 | 03-domain/contexts/BC02/events-slc02.md | 0 |  |
| EVT-CAT-BC02-SLC04 | 03-domain/contexts/BC02/events-slc04.md | 0 |  |
| EVT-CAT-BC02-SLC14 | 03-domain/contexts/BC02/events-slc14.md | 0 |  |
| EVT-CAT-BC02-SLC15 | 03-domain/contexts/BC02/events-slc15.md | 0 |  |
| EVT-CAT-BC03-SLC06 | 03-domain/contexts/BC03/events-slc06.md | 0 |  |
| EVT-CAT-BC03-SLC07 | 03-domain/contexts/BC03/events-slc07.md | 0 |  |
| EVT-CAT-BC03-SLC16 | 03-domain/contexts/BC03/events-slc16.md | 0 |  |
| EVT-CAT-BC04-SLC03 | 03-domain/contexts/BC04/events-slc03.md | 0 |  |
| EVT-CAT-BC04-SLC06 | 03-domain/contexts/BC04/events-slc06.md | 0 |  |
| EVT-CAT-BC04-SLC08 | 03-domain/contexts/BC04/events-slc08.md | 0 |  |
| EVT-CAT-BC04-SLC15 | 03-domain/contexts/BC04/events-slc15.md | 0 |  |
| EVT-CAT-BC04-SLC17 | 03-domain/contexts/BC04/events-slc17.md | 0 |  |
| EVT-CAT-BC05-SLC03 | 03-domain/contexts/BC05/events-slc03.md | 0 |  |
| EVT-CAT-BC05-SLC09 | 03-domain/contexts/BC05/events-slc09.md | 0 |  |
| EVT-CAT-BC05-SLC18 | 03-domain/contexts/BC05/events-slc18.md | 0 |  |
| EVT-CAT-BC05-SLC19 | 03-domain/contexts/BC05/events-slc19.md | 0 |  |
| EVT-CAT-BC06-SLC12 | 03-domain/contexts/BC06/events-slc12.md | 0 |  |
| EVT-CAT-BC07-SLC02 | 03-domain/contexts/BC07/events-slc02.md | 0 |  |
| EVT-CAT-BC07-SLC05 | 03-domain/contexts/BC07/events-slc05.md | 0 |  |
| EVT-CAT-BC07-SLC10 | 03-domain/contexts/BC07/events-slc10.md | 0 |  |
| EVT-CAT-BC07-SLC11 | 03-domain/contexts/BC07/events-slc11.md | 0 |  |
| EVT-CAT-BC07-SLC16 | 03-domain/contexts/BC07/events-slc16.md | 0 |  |
| EVT-CAT-BC08-SLC01 | 03-domain/contexts/BC08/events-slc01.md | 0 |  |
| EVT-CAT-BC08-SLC12A | 03-domain/contexts/BC08/events-slc12a.md | 0 |  |
| EVT-CLM-ASSERTED | 03-domain/contexts/BC02/events-slc02.md | 8 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/conflict-detection-engine.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05 ...(truncated) |
| EVT-CLM-ASSESSED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-02 ...(truncated) |
| EVT-CLM-CHANGED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-02 ...(truncated) |
| EVT-CLM-CORRECTED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-02 ...(truncated) |
| EVT-CLM-RECLASSIFIED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-02 ...(truncated) |
| EVT-CLM-RETRACTED | 03-domain/contexts/BC02/conflict-detection-engine.md;03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-02 ...(truncated) |
| EVT-CLR-EXPIRED | 03-domain/contexts/BC01/events-slc01.md | 3 | 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/asyncapi-slc01.md; 13-verification/tooling/slice-sources.md |
| EVT-CLR-GRANTED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CLR-MODIFIED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CLR-REINSTATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CLR-REQUESTED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CLR-REVOKED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CLR-SUSPENDED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CLS-ACTIVATED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/ac ...(truncated) |
| EVT-CLS-DISCARDED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/ac ...(truncated) |
| EVT-CLS-DRAFTED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/ac ...(truncated) |
| EVT-CLS-EDITED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/ac ...(truncated) |
| EVT-CLS-SUPERSEDED | 03-domain/contexts/BC08/events-slc01.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 05-contracts/asyncapi-slc01.md; 13-verification/tooling/slice-sources.md |
| EVT-CNF-ACCEPTED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CNF-ASSIGNED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CNF-CLAIM-ADDED | 03-domain/contexts/BC02/events-slc04.md | 4 | 03-domain/contexts/BC02/conflict-detection-engine.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/asyncapi-slc04.md; 13-verification/tooling/slice-sources.md |
| EVT-CNF-DETECTED | 03-domain/contexts/BC02/events-slc04.md | 4 | 03-domain/contexts/BC02/conflict-detection-engine.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/asyncapi-slc04.md; 13-verification/tooling/slice-sources.md |
| EVT-CNF-RAISED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CNF-REOPENED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CNF-RESOLVED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CNF-REVIEW-STARTED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-CNF-SUPERSEDED | 03-domain/contexts/BC02/events-slc04.md | 4 | 03-domain/contexts/BC02/conflict-detection-engine.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 05-contracts/asyncapi-slc04.md; 13-verification/tooling/slice-sources.md |
| EVT-CON-ACTIVATED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/ ...(truncated) |
| EVT-CON-DEGRADED | 03-domain/contexts/BC07/events-slc16.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/asyncapi-slc16.md; 13-verification/tooling/slice-sources.md |
| EVT-CON-RECOVERED | 03-domain/contexts/BC07/events-slc16.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/asyncapi-slc16.md; 13-verification/tooling/slice-sources.md |
| EVT-CON-REGISTERED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/ ...(truncated) |
| EVT-CON-RESUMED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/ ...(truncated) |
| EVT-CON-RETIRED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/ ...(truncated) |
| EVT-CON-SUSPENDED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/ ...(truncated) |
| EVT-CON-TEST-FAILED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/ ...(truncated) |
| EVT-CON-TEST-STARTED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/ ...(truncated) |
| EVT-CPL-ACTIVATED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/accepta ...(truncated) |
| EVT-CPL-ACTIVITY-ADDED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/accepta ...(truncated) |
| EVT-CPL-ACTIVITY-REMOVED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/accepta ...(truncated) |
| EVT-CPL-CANCELLED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/accepta ...(truncated) |
| EVT-CPL-COMPLETED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/accepta ...(truncated) |
| EVT-CPL-CREATED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/accepta ...(truncated) |
| EVT-CRD-ACTIVATED | 03-domain/contexts/BC04/events-slc15.md | 6 | 03-domain/contexts/BC04/commands-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-operations-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRD-CANCELLED | 03-domain/contexts/BC04/events-slc15.md | 6 | 03-domain/contexts/BC04/commands-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-operations-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRD-CLOSED | 03-domain/contexts/BC04/events-slc15.md | 6 | 03-domain/contexts/BC04/commands-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-operations-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRD-DECISION-RECORDED | 03-domain/contexts/BC04/events-slc15.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/asyncapi-slc15.md; 13-verification/tooling/slice-sources.md |
| EVT-CRD-DECISION-REQUESTED | 03-domain/contexts/BC04/events-slc15.md | 6 | 03-domain/contexts/BC04/commands-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-operations-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRD-OPENED | 03-domain/contexts/BC04/events-slc15.md | 6 | 03-domain/contexts/BC04/commands-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-operations-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRD-PARTICIPANT-ADDED | 03-domain/contexts/BC04/events-slc15.md | 6 | 03-domain/contexts/BC04/commands-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-operations-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRD-PARTICIPANT-REMOVED | 03-domain/contexts/BC04/events-slc15.md | 6 | 03-domain/contexts/BC04/commands-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-operations-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRD-RESPONSIBILITY-ASSIGNED | 03-domain/contexts/BC04/events-slc15.md | 6 | 03-domain/contexts/BC04/commands-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-operations-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRD-RESPONSIBILITY-UPDATED | 03-domain/contexts/BC04/events-slc15.md | 6 | 03-domain/contexts/BC04/commands-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-operations-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRP-ACCEPTED | 03-domain/contexts/BC02/events-slc15.md | 6 | 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-information-slc15.md; 13-verification/ac ...(truncated) |
| EVT-CRP-EXPIRED | 03-domain/contexts/BC02/events-slc15.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 05-contracts/asyncapi-slc15.md; 13-verification/tooling/slice-sources.md |
| EVT-CRP-PROPOSED | 03-domain/contexts/BC02/events-slc15.md | 6 | 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-information-slc15.md; 13-verification/ac ...(truncated) |
| EVT-CRP-REJECTED | 03-domain/contexts/BC02/events-slc15.md | 6 | 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-information-slc15.md; 13-verification/ac ...(truncated) |
| EVT-CRP-REVIEW-STARTED | 03-domain/contexts/BC02/events-slc15.md | 6 | 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-information-slc15.md; 13-verification/ac ...(truncated) |
| EVT-CRQ-AMENDED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/ ...(truncated) |
| EVT-CRQ-APPROVED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/ ...(truncated) |
| EVT-CRQ-CANCELLED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/ ...(truncated) |
| EVT-CRQ-DRAFTED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/ ...(truncated) |
| EVT-CRQ-EDITED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/ ...(truncated) |
| EVT-CRQ-EXPIRED | 03-domain/contexts/BC02/events-slc14.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/asyncapi-slc14.md; 13-verification/tooling/slice-sources.md |
| EVT-CRQ-FULFILMENT-UPDATED | 03-domain/contexts/BC02/events-slc14.md | 4 | 03-domain/contexts/BC02/collection-spec.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/asyncapi-slc14.md; 13-verification/tooling/slice-sources.md |
| EVT-CRQ-REJECTED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/ ...(truncated) |
| EVT-CRQ-SATISFIED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/ ...(truncated) |
| EVT-CRQ-SUBMITTED | 03-domain/contexts/BC02/events-slc14.md | 6 | 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 05-contracts/asyncapi-slc14.md; 05-contracts/openapi-information-slc14.md; 13-verification/ ...(truncated) |
| EVT-CRR-ACTIVATED | 03-domain/contexts/BC02/events-slc15.md | 6 | 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-information-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRR-DEFINED | 03-domain/contexts/BC02/events-slc15.md | 6 | 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-information-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRR-EDITED | 03-domain/contexts/BC02/events-slc15.md | 6 | 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-information-slc15.md; 13-verification/accept ...(truncated) |
| EVT-CRR-RETIRED | 03-domain/contexts/BC02/events-slc15.md | 6 | 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md; 05-contracts/asyncapi-slc15.md; 05-contracts/openapi-information-slc15.md; 13-verification/accept ...(truncated) |
| EVT-DEC-ANNULLED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-DEC-RECORDED | 03-domain/contexts/BC04/events-slc08.md | 7 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION.md; 05-contracts/asyncapi-slc08.md; 05-contracts/ ...(truncated) |
| EVT-DEC-SUPERSEDED | 03-domain/contexts/BC04/events-slc08.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-DECISION.md; 05-contracts/asyncapi-slc08.md; 13-verification/tooling/slice-sources.md |
| EVT-DEV-ACTIVATED | 03-domain/contexts/BC01/events-slc11.md | 6 | 03-domain/contexts/BC01/commands-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-foundation-slc11.md; 13-verification/acceptance/SLC-11 ...(truncated) |
| EVT-DEV-ENROLL-REQUESTED | 03-domain/contexts/BC01/events-slc11.md | 6 | 03-domain/contexts/BC01/commands-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-foundation-slc11.md; 13-verification/acceptance/SLC-11 ...(truncated) |
| EVT-DEV-KEY-ROTATED | 03-domain/contexts/BC01/events-slc11.md | 6 | 03-domain/contexts/BC01/commands-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-foundation-slc11.md; 13-verification/acceptance/SLC-11 ...(truncated) |
| EVT-DEV-REINSTATED | 03-domain/contexts/BC01/events-slc11.md | 6 | 03-domain/contexts/BC01/commands-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-foundation-slc11.md; 13-verification/acceptance/SLC-11 ...(truncated) |
| EVT-DEV-REPORTED-LOST | 03-domain/contexts/BC01/events-slc11.md | 6 | 03-domain/contexts/BC01/commands-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-foundation-slc11.md; 13-verification/acceptance/SLC-11 ...(truncated) |
| EVT-DEV-RETIRED | 03-domain/contexts/BC01/events-slc11.md | 6 | 03-domain/contexts/BC01/commands-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-foundation-slc11.md; 13-verification/acceptance/SLC-11 ...(truncated) |
| EVT-DEV-SUSPENDED | 03-domain/contexts/BC01/events-slc11.md | 6 | 03-domain/contexts/BC01/commands-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-foundation-slc11.md; 13-verification/acceptance/SLC-11 ...(truncated) |
| EVT-DEV-WIPED | 03-domain/contexts/BC01/events-slc11.md | 3 | 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 05-contracts/asyncapi-slc11.md; 13-verification/tooling/slice-sources.md |
| EVT-DRQ-CITED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/accepta ...(truncated) |
| EVT-DRQ-CREATED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/accepta ...(truncated) |
| EVT-DRQ-DECIDED | 03-domain/contexts/BC04/events-slc08.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/asyncapi-slc08.md; 13-verification/tooling/slice-sources.md |
| EVT-DRQ-ESCALATED | 03-domain/contexts/BC04/events-slc08.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/asyncapi-slc08.md; 13-verification/tooling/slice-sources.md |
| EVT-DRQ-OPENED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/accepta ...(truncated) |
| EVT-DRQ-OPTION-ADDED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/accepta ...(truncated) |
| EVT-DRQ-WITHDRAWN | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/accepta ...(truncated) |
| EVT-DSP-APPROVED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/accep ...(truncated) |
| EVT-DSP-CANCELLED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/accep ...(truncated) |
| EVT-DSP-COMPLETED | 03-domain/contexts/BC08/events-slc12a.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 05-contracts/asyncapi-slc12a.md; 13-verification/tooling/slice-sources.md |
| EVT-DSP-COMPLETED-WITH-EXCEPTIONS | 03-domain/contexts/BC08/events-slc12a.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 05-contracts/asyncapi-slc12a.md; 13-verification/tooling/slice-sources.md |
| EVT-DSP-EXECUTING | 03-domain/contexts/BC08/events-slc12a.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 05-contracts/asyncapi-slc12a.md; 13-verification/tooling/slice-sources.md |
| EVT-DSP-PLANNED | 03-domain/contexts/BC08/events-slc12a.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 05-contracts/asyncapi-slc12a.md; 13-verification/tooling/slice-sources.md |
| EVT-DSP-SUBMITTED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/accep ...(truncated) |
| EVT-DST-CANCELLED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance/S ...(truncated) |
| EVT-DST-COMPLETED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-DST-COMPLETED-WITH-EXCLUSIONS | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-DST-STARTED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance/S ...(truncated) |
| EVT-ENT-RECLASSIFIED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-ENT-REGISTERED | 03-domain/contexts/BC02/events-slc02.md | 7 | 03-domain/contexts/BC02/candidate-generation.md; 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-infor ...(truncated) |
| EVT-ENT-REINSTATED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-ENT-RETIRED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-ENT-TYPE-CHANGED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-ER-MATCH-CONFIRMED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ER-MATCHED | 03-domain/contexts/BC02/events-slc04.md | 7 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/conflict-detection-engine.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi ...(truncated) |
| EVT-ER-NOT-MATCHED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ER-PARKED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ER-PROPOSED | 03-domain/contexts/BC02/events-slc04.md | 7 | 03-domain/contexts/BC02/candidate-generation.md; 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-info ...(truncated) |
| EVT-ER-RESUMED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ER-REVIEW-STARTED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ERS-APPROVED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/accep ...(truncated) |
| EVT-ERS-BLOCKED | 03-domain/contexts/BC08/events-slc12a.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/asyncapi-slc12a.md; 13-verification/tooling/slice-sources.md |
| EVT-ERS-COMPLETED | 03-domain/contexts/BC08/events-slc12a.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/asyncapi-slc12a.md; 13-verification/tooling/slice-sources.md |
| EVT-ERS-EXECUTING | 03-domain/contexts/BC08/events-slc12a.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/asyncapi-slc12a.md; 13-verification/tooling/slice-sources.md |
| EVT-ER-SPLIT | 03-domain/contexts/BC02/conflict-detection-engine.md;03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ER-SPLIT-REQUESTED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-ERS-RECEIVED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/accep ...(truncated) |
| EVT-ERS-REJECTED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/accep ...(truncated) |
| EVT-ERS-SCOPED | 03-domain/contexts/BC08/events-slc12a.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/asyncapi-slc12a.md; 13-verification/tooling/slice-sources.md |
| EVT-ERS-UNBLOCKED | 03-domain/contexts/BC08/events-slc12a.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 05-contracts/asyncapi-slc12a.md; 13-verification/tooling/slice-sources.md |
| EVT-ER-WITHDRAWN | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-EVD-CUSTODY-TRANSFERRED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-EVD-LOCATOR-UPDATED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-EVD-RECLASSIFIED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-EVD-REGISTERED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-EVD-SEALED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-EVD-WITHDRAWN | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-EVL-LINKED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptanc ...(truncated) |
| EVT-EVL-UNLINKED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptanc ...(truncated) |
| EVT-EVS-ACTIVATED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/eva ...(truncated) |
| EVT-EVS-DRAFTED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/eva ...(truncated) |
| EVT-EVS-EDITED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/eva ...(truncated) |
| EVT-EVS-SUPERSEDED | 03-domain/contexts/BC07/events-slc10.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md; 05-contracts/asyncapi-slc10.md; 13-verification/tooling/slice-sources.md |
| EVT-EXC-ACTIVATED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/accep ...(truncated) |
| EVT-EXC-EXPIRED | 03-domain/contexts/BC08/events-slc01.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/asyncapi-slc01.md; 13-verification/tooling/slice-sources.md |
| EVT-EXC-FIRST-APPROVED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/accep ...(truncated) |
| EVT-EXC-REJECTED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/accep ...(truncated) |
| EVT-EXC-REQUESTED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/accep ...(truncated) |
| EVT-EXC-REVOKED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/accep ...(truncated) |
| EVT-EXR-ABORTED | 03-domain/contexts/BC05/events-slc19.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 05-contracts/asyncapi-slc19.md; 13-verification/tooling/slice-sources.md |
| EVT-EXR-CANCELLED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-EXR-COMPLETED | 03-domain/contexts/BC05/events-slc19.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 05-contracts/asyncapi-slc19.md; 13-verification/tooling/slice-sources.md |
| EVT-EXR-PLANNED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-EXR-SCHEDULED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-EXR-STARTED | 03-domain/contexts/BC05/events-slc19.md | 8 | 02-requirements/requirements.md; 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; ...(truncated) |
| EVT-EXT-ENDED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/ ...(truncated) |
| EVT-EXT-MAPPED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/ ...(truncated) |
| EVT-FND-ACCEPTED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-FINDING.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-FND-EDITED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-FINDING.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-FND-RECORDED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-FINDING.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-FND-WITHDRAWN | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-FINDING.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-HRS-APPROVED | 03-domain/contexts/BC01/events-slc16.md | 6 | 03-domain/contexts/BC01/commands-slc16.md; 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-foundation-slc16.md; 13-verification/accepta ...(truncated) |
| EVT-HRS-EXPIRED | 03-domain/contexts/BC01/events-slc16.md | 3 | 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 05-contracts/asyncapi-slc16.md; 13-verification/tooling/slice-sources.md |
| EVT-HRS-PROPOSED | 03-domain/contexts/BC01/events-slc16.md | 3 | 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 05-contracts/asyncapi-slc16.md; 13-verification/tooling/slice-sources.md |
| EVT-HRS-REJECTED | 03-domain/contexts/BC01/events-slc16.md | 6 | 03-domain/contexts/BC01/commands-slc16.md; 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-foundation-slc16.md; 13-verification/accepta ...(truncated) |
| EVT-HRS-SUPERSEDED | 03-domain/contexts/BC01/events-slc16.md | 3 | 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 05-contracts/asyncapi-slc16.md; 13-verification/tooling/slice-sources.md |
| EVT-IMP-CANCELLED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance ...(truncated) |
| EVT-IMP-COMPLETED | 03-domain/contexts/BC02/events-slc02.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/asyncapi-slc02.md; 13-verification/tooling/slice-sources.md |
| EVT-IMP-COMPLETED-WITH-QUARANTINE | 03-domain/contexts/BC02/events-slc02.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/asyncapi-slc02.md; 13-verification/tooling/slice-sources.md |
| EVT-IMP-FAILED | 03-domain/contexts/BC02/events-slc02.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/asyncapi-slc02.md; 13-verification/tooling/slice-sources.md |
| EVT-IMP-PROCESSING-STARTED | 03-domain/contexts/BC02/events-slc02.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/asyncapi-slc02.md; 13-verification/tooling/slice-sources.md |
| EVT-IMP-QUARANTINE-ACCEPTED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance ...(truncated) |
| EVT-IMP-RECEIVED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance ...(truncated) |
| EVT-IMP-REPROCESSING | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance ...(truncated) |
| EVT-INC-ASSESSED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-INC-CANCELLED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-INC-CLOSED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-INC-CONTAINED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-INC-CONTINGENCY-ACTIVATED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-INC-DE-ESCALATED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-INC-ESCALATED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-INC-REPORTED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-INC-RESOLVED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-INC-RESPONSE-DISPATCHED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-INC-SLA-BREACHED | 03-domain/contexts/BC04/events-slc17.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 05-contracts/asyncapi-slc17.md; 13-verification/tooling/slice-sources.md |
| EVT-KNO-DISCARDED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-KNO-DRAFTED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-KNO-EDITED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-KNO-PUBLISHED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-KNO-REJECTED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-KNO-RETIRED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-KNO-RETURNED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-KNO-REUSED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-KNO-SUBMITTED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-KNO-SUPERSEDED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-LGR-APPROVED | 03-domain/contexts/BC05/events-slc18.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/asyncapi-slc18.md; 13-verification/tooling/slice-sources.md |
| EVT-LGR-CANCELLED | 03-domain/contexts/BC05/events-slc18.md | 6 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/asyncapi-slc18.md; 05-contracts/openapi-readiness-slc18.md; 13-verification/accepta ...(truncated) |
| EVT-LGR-DISPATCHED | 03-domain/contexts/BC05/events-slc18.md | 6 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/asyncapi-slc18.md; 05-contracts/openapi-readiness-slc18.md; 13-verification/accepta ...(truncated) |
| EVT-LGR-FULFILLED | 03-domain/contexts/BC05/events-slc18.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/asyncapi-slc18.md; 13-verification/tooling/slice-sources.md |
| EVT-LGR-PARTIALLY-FULFILLED | 03-domain/contexts/BC05/events-slc18.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/asyncapi-slc18.md; 13-verification/tooling/slice-sources.md |
| EVT-LGR-PENDING-APPROVAL | 03-domain/contexts/BC05/events-slc18.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/asyncapi-slc18.md; 13-verification/tooling/slice-sources.md |
| EVT-LGR-REJECTED | 03-domain/contexts/BC05/events-slc18.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/asyncapi-slc18.md; 13-verification/tooling/slice-sources.md |
| EVT-LGR-REQUESTED | 03-domain/contexts/BC05/events-slc18.md | 6 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 05-contracts/asyncapi-slc18.md; 05-contracts/openapi-readiness-slc18.md; 13-verification/accepta ...(truncated) |
| EVT-LHD-EXTENDED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/acceptance ...(truncated) |
| EVT-LHD-PLACED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/acceptance ...(truncated) |
| EVT-LHD-RELEASE-CANCELLED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/acceptance ...(truncated) |
| EVT-LHD-RELEASED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/acceptance ...(truncated) |
| EVT-LHD-RELEASE-REQUESTED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/acceptance ...(truncated) |
| EVT-MDL-APPROVED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ ...(truncated) |
| EVT-MDL-DEPRECATED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ ...(truncated) |
| EVT-MDL-DRIFT-DETECTED | 03-domain/contexts/BC07/events-slc10.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/asyncapi-slc10.md; 13-verification/tooling/slice-sources.md |
| EVT-MDL-EVALUATION-FAILED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ ...(truncated) |
| EVT-MDL-EVALUATION-STARTED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ ...(truncated) |
| EVT-MDL-PROMOTED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ ...(truncated) |
| EVT-MDL-REGISTERED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ ...(truncated) |
| EVT-MDL-REINSTATED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ ...(truncated) |
| EVT-MDL-RETIRED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ ...(truncated) |
| EVT-MDL-STAGED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ ...(truncated) |
| EVT-MNT-CANCELLED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/accepta ...(truncated) |
| EVT-MNT-COMPLETED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/accepta ...(truncated) |
| EVT-MNT-PLANNED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/accepta ...(truncated) |
| EVT-MNT-RESCHEDULED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/accepta ...(truncated) |
| EVT-MNT-STARTED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/accepta ...(truncated) |
| EVT-MRS-ACTIVATED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptanc ...(truncated) |
| EVT-MRS-DRAFTED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptanc ...(truncated) |
| EVT-MRS-EDITED | 03-domain/contexts/BC02/events-slc04.md | 6 | 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md; 05-contracts/asyncapi-slc04.md; 05-contracts/openapi-information-slc04.md; 13-verification/acceptanc ...(truncated) |
| EVT-MRS-SUPERSEDED | 03-domain/contexts/BC02/events-slc04.md | 3 | 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md; 05-contracts/asyncapi-slc04.md; 13-verification/tooling/slice-sources.md |
| EVT-NTF-EXPIRED | 03-domain/contexts/BC04/events-slc06.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md; 05-contracts/asyncapi-slc06.md; 13-verification/tooling/slice-sources.md |
| EVT-NTF-FAILED | 03-domain/contexts/BC04/events-slc06.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md; 05-contracts/asyncapi-slc06.md; 13-verification/tooling/slice-sources.md |
| EVT-NTF-QUEUED | 03-domain/contexts/BC04/events-slc06.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md; 05-contracts/asyncapi-slc06.md; 13-verification/tooling/slice-sources.md |
| EVT-NTF-READ | 03-domain/contexts/BC04/events-slc06.md | 6 | 03-domain/contexts/BC04/commands-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-operations-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-NTF-SENT | 03-domain/contexts/BC04/events-slc06.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md; 05-contracts/asyncapi-slc06.md; 13-verification/tooling/slice-sources.md |
| EVT-NTF-WITHHELD | 03-domain/contexts/BC04/events-slc06.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md; 05-contracts/asyncapi-slc06.md; 13-verification/tooling/slice-sources.md |
| EVT-OBS-AMENDED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/ ...(truncated) |
| EVT-OBS-EVIDENCE-ATTACHED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/ ...(truncated) |
| EVT-OBS-RECLASSIFIED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/ ...(truncated) |
| EVT-OBS-RECORDED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/ ...(truncated) |
| EVT-OBS-REJECTED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/ ...(truncated) |
| EVT-OBS-VALIDATED | 03-domain/contexts/BC02/events-slc02.md | 7 | 03-domain/contexts/BC02/collection-spec.md; 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-infor ...(truncated) |
| EVT-ORG-CREATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ORG-DEACTIVATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ORG-REACTIVATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ORG-RENAMED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ORG-UNIT-ADDED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ORG-UNIT-DEACTIVATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ORG-UNIT-MOVED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/ ...(truncated) |
| EVT-ORG-UNIT-RENAMED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/ ...(truncated) |
| EVT-OUT-MEASURED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptan ...(truncated) |
| EVT-OUT-MEASUREMENT-CORRECTED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptan ...(truncated) |
| EVT-OUT-TARGET-CHANGED | 03-domain/contexts/BC04/events-slc08.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md; 05-contracts/asyncapi-slc08.md; 13-verification/tooling/slice-sources.md |
| EVT-OUT-TRACKER-CLOSED | 03-domain/contexts/BC04/events-slc08.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md; 05-contracts/asyncapi-slc08.md; 13-verification/tooling/slice-sources.md |
| EVT-OUT-TRACKER-CREATED | 03-domain/contexts/BC04/events-slc08.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md; 05-contracts/asyncapi-slc08.md; 13-verification/tooling/slice-sources.md |
| EVT-PER-DEACTIVATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-PER-DETAILS-UPDATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-PER-ERASED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-PER-REACTIVATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-PER-REGISTERED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-PKG-BUILDING | 03-domain/contexts/BC07/events-slc11.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 05-contracts/asyncapi-slc11.md; 13-verification/tooling/slice-sources.md |
| EVT-PKG-DOWNLOADED | 03-domain/contexts/BC07/events-slc11.md | 6 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-field-slc11.md; 13-verification/acceptance/SL ...(truncated) |
| EVT-PKG-EXPIRED | 03-domain/contexts/BC07/events-slc11.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 05-contracts/asyncapi-slc11.md; 13-verification/tooling/slice-sources.md |
| EVT-PKG-READY | 03-domain/contexts/BC07/events-slc11.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 05-contracts/asyncapi-slc11.md; 13-verification/tooling/slice-sources.md |
| EVT-PKG-REQUESTED | 03-domain/contexts/BC07/events-slc11.md | 6 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-field-slc11.md; 13-verification/acceptance/SL ...(truncated) |
| EVT-PKG-REVOKED | 03-domain/contexts/BC07/events-slc11.md | 6 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-field-slc11.md; 13-verification/acceptance/SL ...(truncated) |
| EVT-PLN-ACTIVATED | 03-domain/contexts/BC04/events-slc08.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/asyncapi-slc08.md; 13-verification/tooling/slice-sources.md |
| EVT-PLN-CANCELLED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/SLC-08/p ...(truncated) |
| EVT-PLN-CLOSED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/SLC-08/p ...(truncated) |
| EVT-PLN-COMPLETED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/SLC-08/p ...(truncated) |
| EVT-PLN-CREATED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/SLC-08/p ...(truncated) |
| EVT-PLN-RECLASSIFIED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/SLC-08/p ...(truncated) |
| EVT-PLN-RESUMED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/SLC-08/p ...(truncated) |
| EVT-PLN-REVIEW-FLAGGED | 03-domain/contexts/BC04/events-slc08.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/asyncapi-slc08.md; 13-verification/tooling/slice-sources.md |
| EVT-PLN-SUSPENDED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/SLC-08/p ...(truncated) |
| EVT-PLV-BASELINED | 03-domain/contexts/BC04/events-slc08.md | 8 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 05-con ...(truncated) |
| EVT-PLV-DISCARDED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/ ...(truncated) |
| EVT-PLV-DRAFTED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/ ...(truncated) |
| EVT-PLV-EDITED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/ ...(truncated) |
| EVT-PLV-MINOR-AMENDED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/ ...(truncated) |
| EVT-PLV-REJECTED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/ ...(truncated) |
| EVT-PLV-RETURNED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/ ...(truncated) |
| EVT-PLV-SUBMITTED | 03-domain/contexts/BC04/events-slc08.md | 6 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/asyncapi-slc08.md; 05-contracts/openapi-operations-slc08.md; 13-verification/acceptance/ ...(truncated) |
| EVT-PLV-SUPERSEDED | 03-domain/contexts/BC04/events-slc08.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 05-contracts/asyncapi-slc08.md; 13-verification/tooling/slice-sources.md |
| EVT-POL-ACTIVATED | 03-domain/contexts/BC08/events-slc01.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/asyncapi-slc01.md; 13-verification/tooling/slice-sources.md |
| EVT-POL-APPROVED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/acceptance/SL ...(truncated) |
| EVT-POL-DRAFTED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/acceptance/SL ...(truncated) |
| EVT-POL-EDITED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/acceptance/SL ...(truncated) |
| EVT-POL-REJECTED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/acceptance/SL ...(truncated) |
| EVT-POL-SUBMITTED | 03-domain/contexts/BC08/events-slc01.md | 6 | 03-domain/contexts/BC08/commands-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-governance-slc01.md; 13-verification/acceptance/SL ...(truncated) |
| EVT-POL-SUPERSEDED | 03-domain/contexts/BC08/events-slc01.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 05-contracts/asyncapi-slc01.md; 13-verification/tooling/slice-sources.md |
| EVT-PRD-APPROVED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance/SLC-12 ...(truncated) |
| EVT-PRD-CREATED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance/SLC-12 ...(truncated) |
| EVT-PRD-DISCARDED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance/SLC-12 ...(truncated) |
| EVT-PRD-GENERATED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-PRD-GENERATION-FAILED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-PRD-GENERATION-STARTED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance/SLC-12 ...(truncated) |
| EVT-PRD-NARRATIVE-EDITED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance/SLC-12 ...(truncated) |
| EVT-PRD-RETURNED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance/SLC-12 ...(truncated) |
| EVT-PRD-SUBMITTED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance/SLC-12 ...(truncated) |
| EVT-PRD-SUPERSEDED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-PRD-WITHDRAWN | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance/SLC-12 ...(truncated) |
| EVT-PRJ-BUILD-STARTED | 03-domain/contexts/BC07/events-slc05.md | 6 | 03-domain/contexts/BC07/commands-slc05.md; 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/asyncapi-slc05.md; 05-contracts/openapi-discovery-slc05.md; 13-verification/accept ...(truncated) |
| EVT-PRJ-DEGRADED | 03-domain/contexts/BC07/events-slc05.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/asyncapi-slc05.md; 13-verification/tooling/slice-sources.md |
| EVT-PRJ-FAILED | 03-domain/contexts/BC07/events-slc05.md | 6 | 03-domain/contexts/BC07/commands-slc05.md; 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/asyncapi-slc05.md; 05-contracts/openapi-discovery-slc05.md; 13-verification/accept ...(truncated) |
| EVT-PRJ-PROMOTED | 03-domain/contexts/BC07/events-slc05.md | 6 | 03-domain/contexts/BC07/commands-slc05.md; 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/asyncapi-slc05.md; 05-contracts/openapi-discovery-slc05.md; 13-verification/accept ...(truncated) |
| EVT-PRJ-READY | 03-domain/contexts/BC07/events-slc05.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/asyncapi-slc05.md; 13-verification/tooling/slice-sources.md |
| EVT-PRJ-RECOVERED | 03-domain/contexts/BC07/events-slc05.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/asyncapi-slc05.md; 13-verification/tooling/slice-sources.md |
| EVT-PRJ-RETIRED | 03-domain/contexts/BC07/events-slc05.md | 6 | 03-domain/contexts/BC07/commands-slc05.md; 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/asyncapi-slc05.md; 05-contracts/openapi-discovery-slc05.md; 13-verification/accept ...(truncated) |
| EVT-PTM-ACTIVATED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-PTM-DEFINED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-PTM-EDITED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-PTM-RETIRED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptan ...(truncated) |
| EVT-QUAL-EXPIRED | 03-domain/contexts/BC05/events-slc03.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/asyncapi-slc03.md; 13-verification/tooling/slice-sources.md |
| EVT-QUAL-RECORDED | 03-domain/contexts/BC05/events-slc03.md | 6 | 03-domain/contexts/BC05/commands-slc03.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-readiness-slc03.md; 13-verification/acce ...(truncated) |
| EVT-QUAL-REINSTATED | 03-domain/contexts/BC05/events-slc03.md | 6 | 03-domain/contexts/BC05/commands-slc03.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-readiness-slc03.md; 13-verification/acce ...(truncated) |
| EVT-QUAL-RENEWED | 03-domain/contexts/BC05/events-slc03.md | 6 | 03-domain/contexts/BC05/commands-slc03.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-readiness-slc03.md; 13-verification/acce ...(truncated) |
| EVT-QUAL-REVOKED | 03-domain/contexts/BC05/events-slc03.md | 6 | 03-domain/contexts/BC05/commands-slc03.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-readiness-slc03.md; 13-verification/acce ...(truncated) |
| EVT-QUAL-SUSPENDED | 03-domain/contexts/BC05/events-slc03.md | 6 | 03-domain/contexts/BC05/commands-slc03.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-readiness-slc03.md; 13-verification/acce ...(truncated) |
| EVT-RAS-ASSIGNED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-RAS-EXPIRED | 03-domain/contexts/BC01/events-slc01.md | 3 | 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md; 05-contracts/asyncapi-slc01.md; 13-verification/tooling/slice-sources.md |
| EVT-RAS-REVOKED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-REC-CANCELLED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance ...(truncated) |
| EVT-REC-COMPLETED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-REC-FAILED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-REC-REQUESTED | 03-domain/contexts/BC06/events-slc12.md | 6 | 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md; 05-contracts/asyncapi-slc12.md; 05-contracts/openapi-knowledge-slc12.md; 13-verification/acceptance ...(truncated) |
| EVT-REC-STARTED | 03-domain/contexts/BC06/events-slc12.md | 3 | 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md; 05-contracts/asyncapi-slc12.md; 13-verification/tooling/slice-sources.md |
| EVT-REL-RECLASSIFIED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance ...(truncated) |
| EVT-REL-REGISTERED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance ...(truncated) |
| EVT-REL-REINSTATED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance ...(truncated) |
| EVT-REL-RETIRED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance ...(truncated) |
| EVT-RIS-ASSESSED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC-17/r ...(truncated) |
| EVT-RIS-CLOSED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC-17/r ...(truncated) |
| EVT-RIS-IDENTIFIED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC-17/r ...(truncated) |
| EVT-RIS-MATERIALIZATION-LINKED | 03-domain/contexts/BC04/events-slc17.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/asyncapi-slc17.md; 13-verification/tooling/slice-sources.md |
| EVT-RIS-REASSESSED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC-17/r ...(truncated) |
| EVT-RIS-TREATMENT-PLANNED | 03-domain/contexts/BC04/events-slc17.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 05-contracts/asyncapi-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/acceptance/SLC-17/r ...(truncated) |
| EVT-ROL-ACTIVATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/r ...(truncated) |
| EVT-ROL-DEFINED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/r ...(truncated) |
| EVT-ROL-PERMISSIONS-CHANGED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/r ...(truncated) |
| EVT-ROL-RETIRED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/r ...(truncated) |
| EVT-RPL-CAPACITY-ADJUSTED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/ ...(truncated) |
| EVT-RPL-CLOSED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/ ...(truncated) |
| EVT-RPL-CREATED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/ ...(truncated) |
| EVT-RPL-RESUMED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/ ...(truncated) |
| EVT-RPL-SUSPENDED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/ ...(truncated) |
| EVT-RRQ-ACTIVATED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptan ...(truncated) |
| EVT-RRQ-DEFINED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptan ...(truncated) |
| EVT-RRQ-EDITED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptan ...(truncated) |
| EVT-RRQ-RETIRED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptan ...(truncated) |
| EVT-RSV-CANCELLED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/accepta ...(truncated) |
| EVT-RSV-CONFIRMED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/accepta ...(truncated) |
| EVT-RSV-EXPIRED | 03-domain/contexts/BC05/events-slc09.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 05-contracts/asyncapi-slc09.md; 13-verification/tooling/slice-sources.md |
| EVT-RSV-HELD | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/accepta ...(truncated) |
| EVT-RSV-RELEASED | 03-domain/contexts/BC05/events-slc09.md | 6 | 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 05-contracts/asyncapi-slc09.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/accepta ...(truncated) |
| EVT-RTG-ACTIVATED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai- ...(truncated) |
| EVT-RTG-DISCARDED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai- ...(truncated) |
| EVT-RTG-DRAFTED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai- ...(truncated) |
| EVT-RTG-EDITED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai- ...(truncated) |
| EVT-RTG-SUPERSEDED | 03-domain/contexts/BC07/events-slc10.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md; 05-contracts/asyncapi-slc10.md; 13-verification/tooling/slice-sources.md |
| EVT-RTS-ACTIVATED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/ac ...(truncated) |
| EVT-RTS-DISCARDED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/ac ...(truncated) |
| EVT-RTS-DRAFTED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/ac ...(truncated) |
| EVT-RTS-EDITED | 03-domain/contexts/BC08/events-slc12a.md | 6 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md; 05-contracts/asyncapi-slc12a.md; 05-contracts/openapi-governance-slc12a.md; 13-verification/ac ...(truncated) |
| EVT-RTS-SUPERSEDED | 03-domain/contexts/BC08/events-slc12a.md | 3 | 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md; 05-contracts/asyncapi-slc12a.md; 13-verification/tooling/slice-sources.md |
| EVT-RUN-CANCELLED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptanc ...(truncated) |
| EVT-RUN-FAILED | 03-domain/contexts/BC03/events-slc07.md | 3 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md; 05-contracts/asyncapi-slc07.md; 13-verification/tooling/slice-sources.md |
| EVT-RUN-QUEUED | 03-domain/contexts/BC03/events-slc07.md | 6 | 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md; 05-contracts/asyncapi-slc07.md; 05-contracts/openapi-intelligence-slc07.md; 13-verification/acceptanc ...(truncated) |
| EVT-RUN-STARTED | 03-domain/contexts/BC03/events-slc07.md | 3 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md; 05-contracts/asyncapi-slc07.md; 13-verification/tooling/slice-sources.md |
| EVT-RUN-SUCCEEDED | 03-domain/contexts/BC03/events-slc07.md | 3 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md; 05-contracts/asyncapi-slc07.md; 13-verification/tooling/slice-sources.md |
| EVT-RWE-RECLASSIFIED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/accepta ...(truncated) |
| EVT-RWE-REGISTERED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/accepta ...(truncated) |
| EVT-RWE-REINSTATED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/accepta ...(truncated) |
| EVT-RWE-RETIRED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/accepta ...(truncated) |
| EVT-RWE-TYPE-CHANGED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/accepta ...(truncated) |
| EVT-SCF-ASSIGNED | 03-domain/contexts/BC07/events-slc11.md | 6 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-field-slc11.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-SCF-DISCARDED | 03-domain/contexts/BC07/events-slc11.md | 6 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-field-slc11.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-SCF-OPENED | 03-domain/contexts/BC07/events-slc11.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 05-contracts/asyncapi-slc11.md; 13-verification/tooling/slice-sources.md |
| EVT-SCF-REAPPLIED | 03-domain/contexts/BC07/events-slc11.md | 6 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-field-slc11.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-SCF-RESOLVED-MANUALLY | 03-domain/contexts/BC07/events-slc11.md | 6 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-field-slc11.md; 13-verification/acceptance/SLC- ...(truncated) |
| EVT-SCN-ACTIVATED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-SCN-DEFINED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-SCN-EDITED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-SCN-RETIRED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-SEC-VERSION-INCREMENTED | 03-domain/contexts/BC01/events-slc01.md | 24 | 03-domain/contexts/BC01/events-slc11.md; 03-domain/contexts/BC01/events-slc16.md; 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC03/events-slc06.md; 03-domain/contexts/BC03/events-slc07 ...(truncated) |
| EVT-SHP-CANCELLED | 03-domain/contexts/BC05/events-slc18.md | 6 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/asyncapi-slc18.md; 05-contracts/openapi-readiness-slc18.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-SHP-CHECKPOINT-RECORDED | 03-domain/contexts/BC05/events-slc18.md | 6 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/asyncapi-slc18.md; 05-contracts/openapi-readiness-slc18.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-SHP-DAMAGED | 03-domain/contexts/BC05/events-slc18.md | 7 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/asyncapi-slc18.md; 05-contracts ...(truncated) |
| EVT-SHP-DELIVERED | 03-domain/contexts/BC05/events-slc18.md | 7 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/asyncapi-slc18.md; 05-contracts ...(truncated) |
| EVT-SHP-DEPARTED | 03-domain/contexts/BC05/events-slc18.md | 6 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/asyncapi-slc18.md; 05-contracts/openapi-readiness-slc18.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-SHP-LOST | 03-domain/contexts/BC05/events-slc18.md | 7 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/asyncapi-slc18.md; 05-contracts ...(truncated) |
| EVT-SHP-PLANNED | 03-domain/contexts/BC05/events-slc18.md | 6 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 05-contracts/asyncapi-slc18.md; 05-contracts/openapi-readiness-slc18.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-SIM-ABORTED | 03-domain/contexts/BC05/events-slc19.md | 10 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openap ...(truncated) |
| EVT-SIM-COMPLETED | 03-domain/contexts/BC05/events-slc19.md | 11 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md;  ...(truncated) |
| EVT-SIM-EVALUATION-RECORDED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-SIM-INJECT-DELIVERED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-SIM-PAUSED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-SIM-RESUMED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-SIM-STARTED | 03-domain/contexts/BC05/events-slc19.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 05-contracts/asyncapi-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-SIT-ACTIVATED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/S ...(truncated) |
| EVT-SIT-CLOSED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/S ...(truncated) |
| EVT-SIT-CREATED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/S ...(truncated) |
| EVT-SIT-DEFINITION-CHANGED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/S ...(truncated) |
| EVT-SIT-PAUSED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/S ...(truncated) |
| EVT-SIT-RECLASSIFIED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/S ...(truncated) |
| EVT-SIT-RESUMED | 03-domain/contexts/BC03/events-slc06.md | 6 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-intelligence-slc06.md; 13-verification/acceptance/S ...(truncated) |
| EVT-SNS-ACTIVATED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/acceptanc ...(truncated) |
| EVT-SNS-PAUSED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/acceptanc ...(truncated) |
| EVT-SNS-QUALITY-RULES-SET | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/acceptanc ...(truncated) |
| EVT-SNS-REGISTERED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/acceptanc ...(truncated) |
| EVT-SNS-RETIRED | 03-domain/contexts/BC07/events-slc16.md | 6 | 03-domain/contexts/BC07/commands-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/asyncapi-slc16.md; 05-contracts/openapi-integration-slc16.md; 13-verification/acceptanc ...(truncated) |
| EVT-SNS-STALE | 03-domain/contexts/BC07/events-slc16.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/asyncapi-slc16.md; 13-verification/tooling/slice-sources.md |
| EVT-SRC-PROFILE-UPDATED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-SRC-PROTECTION-CHANGED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-SRC-RECLASSIFIED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-SRC-REGISTERED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-SRC-REINSTATED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-SRC-RELIABILITY-RATED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-SRC-RETIRED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-SRC-SUSPENDED | 03-domain/contexts/BC02/events-slc02.md | 6 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 05-contracts/asyncapi-slc02.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| EVT-SUB-CHANNELS-UPDATED | 03-domain/contexts/BC04/events-slc06.md | 6 | 03-domain/contexts/BC04/commands-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-operations-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-SUB-ENDED | 03-domain/contexts/BC04/events-slc06.md | 6 | 03-domain/contexts/BC04/commands-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-operations-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-SUB-PAUSED | 03-domain/contexts/BC04/events-slc06.md | 6 | 03-domain/contexts/BC04/commands-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-operations-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-SUB-RESUMED | 03-domain/contexts/BC04/events-slc06.md | 6 | 03-domain/contexts/BC04/commands-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-operations-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-SUB-SUBSCRIBED | 03-domain/contexts/BC04/events-slc06.md | 6 | 03-domain/contexts/BC04/commands-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md; 05-contracts/asyncapi-slc06.md; 05-contracts/openapi-operations-slc06.md; 13-verification/acceptance/ ...(truncated) |
| EVT-SVC-CLOSED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-SVC-CREATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-SVC-CREDENTIAL-ROTATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-SVC-DISABLED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-SVC-ENABLED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-SYN-BATCH-RECEIVED | 03-domain/contexts/BC07/events-slc11.md | 6 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-field-slc11.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-SYN-COMPLETED | 03-domain/contexts/BC07/events-slc11.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md; 05-contracts/asyncapi-slc11.md; 13-verification/tooling/slice-sources.md |
| EVT-SYN-COMPLETED-WITH-CONFLICTS | 03-domain/contexts/BC07/events-slc11.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md; 05-contracts/asyncapi-slc11.md; 13-verification/tooling/slice-sources.md |
| EVT-SYN-FAILED | 03-domain/contexts/BC07/events-slc11.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md; 05-contracts/asyncapi-slc11.md; 13-verification/tooling/slice-sources.md |
| EVT-SYN-OPENED | 03-domain/contexts/BC07/events-slc11.md | 6 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md; 05-contracts/asyncapi-slc11.md; 05-contracts/openapi-field-slc11.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| EVT-SYN-REJECTED | 03-domain/contexts/BC07/events-slc11.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md; 05-contracts/asyncapi-slc11.md; 13-verification/tooling/slice-sources.md |
| EVT-TASK-ACCEPTED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-APPROVED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-ASSIGNED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-BLOCKED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-CANCELLED | 03-domain/contexts/BC04/events-slc03.md | 7 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operati ...(truncated) |
| EVT-TASK-CLOSED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-COMPLETED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-CREATED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-DECLINED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-DUE-CHANGED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-EDITED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-ESCALATED | 03-domain/contexts/BC04/events-slc03.md | 8 | 03-domain/contexts/BC03/situation-alerting-spec.md; 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contr ...(truncated) |
| EVT-TASK-EXPIRED | 03-domain/contexts/BC04/events-slc03.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 13-verification/tooling/slice-sources.md |
| EVT-TASK-READIED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-REASSIGNED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-RECLASSIFIED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-REJECTED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-RESULT-ITEM-ADDED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-RESUMED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-RETURNED-FOR-REWORK | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-REVIEW-STARTED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-STARTED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-SUBMITTED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-SUPERSEDED | 03-domain/contexts/BC04/events-slc03.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 13-verification/tooling/slice-sources.md |
| EVT-TASK-SUSPENDED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TASK-UNSUSPENDED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC-03/t ...(truncated) |
| EVT-TEN-ACTIVATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-TEN-DECOMMISSIONED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-TEN-DECOMMISSION-STARTED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-TEN-MIGRATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-TEN-MIGRATION-STARTED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-TEN-PROVISIONING-FAILED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 13-verification/acceptan ...(truncated) |
| EVT-TEN-PROVISIONING-STARTED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-TEN-QUOTAS-UPDATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-TEN-REACTIVATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-TEN-SUSPENDED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01 ...(truncated) |
| EVT-TOL-ACTIVATED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai-too ...(truncated) |
| EVT-TOL-DISABLED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai-too ...(truncated) |
| EVT-TOL-ENABLED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai-too ...(truncated) |
| EVT-TOL-REGISTERED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai-too ...(truncated) |
| EVT-TOL-RETIRED | 03-domain/contexts/BC07/events-slc10.md | 6 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/asyncapi-slc10.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai-too ...(truncated) |
| EVT-TTY-ACTIVATED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-TTY-DEFINED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-TTY-EDITED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-TTY-RETIRED | 03-domain/contexts/BC04/events-slc03.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 05-contracts/asyncapi-slc03.md; 05-contracts/openapi-operations-slc03.md; 13-verification/acceptance/SLC ...(truncated) |
| EVT-USR-ACTIVATED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md; 13-verification/acceptance ...(truncated) |
| EVT-USR-CLOSED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/u ...(truncated) |
| EVT-USR-DISABLED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/u ...(truncated) |
| EVT-USR-ENABLED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/u ...(truncated) |
| EVT-USR-IDENTITY-LINKED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/u ...(truncated) |
| EVT-USR-IDENTITY-UNLINKED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/u ...(truncated) |
| EVT-USR-LOCKED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/u ...(truncated) |
| EVT-USR-PERSON-LINKED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/u ...(truncated) |
| EVT-USR-PROVISIONED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/u ...(truncated) |
| EVT-USR-UNLOCKED | 03-domain/contexts/BC01/events-slc01.md | 6 | 03-domain/contexts/BC01/commands-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 05-contracts/asyncapi-slc01.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/u ...(truncated) |

### Family: FIT

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| FIT-01 | 13-verification/fitness-functions.md | 7 | 00-governance/registers/corrections.md; 03-domain/context-map.md; 06-data/logical-model/slc-01.md; 08-security/audit-architecture.md; 08-security/trust-boundaries.md; 12-solution/c4-containers.md; 16- ...(truncated) |
| FIT-02 | 13-verification/fitness-functions.md | 3 | 00-governance/decisions/ADR-P04.md; 06-data/logical-model/slc-01.md; 08-security/threat-model.md |
| FIT-03 | 13-verification/fitness-functions.md | 1 | 00-governance/decisions/ADR-P06.md |
| FIT-04 | 13-verification/fitness-functions.md | 95 | 00-governance/decisions/ADR-P02.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 03 ...(truncated) |
| FIT-05 | 13-verification/fitness-functions.md | 3 | 00-governance/decisions/ADR-P01.md; 06-data/logical-model/slc-02.md; 09-reliability/fmea-slc02.md |
| FIT-06 | 13-verification/fitness-functions.md | 1 | 00-governance/decisions/ADR-P03.md |
| FIT-07 | 13-verification/fitness-functions.md | 1 | 00-governance/decisions/ADR-P13.md |
| FIT-08 | 13-verification/fitness-functions.md | 1 | 00-governance/decisions/ADR-P16.md |
| FIT-09 | 13-verification/fitness-functions.md | 3 | 06-data/logical-model/slc-01.md; 16-reports/ANTI-PATTERN-REPORT-R1.md; 16-reports/CONSISTENCY-CHECK-W3.md |
| FIT-10 | 13-verification/fitness-functions.md | 1 | 03-domain/contexts/BC02/claims-temporal-kernel.md |
| FIT-11 | 13-verification/fitness-functions.md | 3 | 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 13-verification/tooling/slice-sources.md; 16-reports/ANTI-PATTERN-REPORT-R1.md |
| FIT-12 | 13-verification/fitness-functions.md | 7 | 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 12-solution/c4-context.md; 12-solution/technology-decisions.md; 13-verification/tooling/sli ...(truncated) |
| FIT-13 | 13-verification/fitness-functions.md | 1 | 15-traceability/trace-platform.md |
| FIT-14 | 13-verification/fitness-functions.md | 2 | 15-traceability/quality-verification-matrix.md; 15-traceability/trace-platform.md |
| FIT-15 | 13-verification/fitness-functions.md | 0 |  |
| FIT-16 | 13-verification/fitness-functions.md | 2 | 14-slices/SLC-01/readiness.md; 16-reports/CONSISTENCY-CHECK-W3.md |
| FIT-17 | 13-verification/fitness-functions.md | 0 |  |
| FIT-18 | 13-verification/fitness-functions.md | 1 | 00-governance/decisions/ADR-P05.md |
| FIT-19 | 13-verification/fitness-functions.md | 9 | 00-governance/registers/corrections.md; 00-governance/registers/risks.md; 08-security/key-hierarchy-and-disposition.md; 09-reliability/dr-and-continuity.md; 15-traceability/quality-verification-matrix ...(truncated) |

### Family: FITNESS

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| FITNESS-FUNCTIONS | 13-verification/fitness-functions.md | 0 |  |

### Family: FM

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| FM-S01-01 | 09-reliability/fmea-slc01.md | 0 |  |
| FM-S01-02 | 09-reliability/fmea-slc01.md | 0 |  |
| FM-S01-03 | 09-reliability/fmea-slc01.md | 1 | 15-traceability/trace-slc01.md |
| FM-S01-04 | 09-reliability/fmea-slc01.md | 0 |  |
| FM-S01-05 | 09-reliability/fmea-slc01.md | 0 |  |
| FM-S01-06 | 09-reliability/fmea-slc01.md | 0 |  |
| FM-S01-07 | 09-reliability/fmea-slc01.md | 0 |  |
| FM-S01-08 | 09-reliability/fmea-slc01.md | 2 | 08-security/key-hierarchy-and-disposition.md; 12-solution/technology-decisions.md |
| FM-S01-09 | 09-reliability/fmea-slc01.md | 0 |  |
| FM-S02-01 | 09-reliability/fmea-slc02.md | 0 |  |
| FM-S02-02 | 09-reliability/fmea-slc02.md | 0 |  |
| FM-S02-03 | 09-reliability/fmea-slc02.md | 0 |  |
| FM-S02-04 | 09-reliability/fmea-slc02.md | 0 |  |
| FM-S02-05 | 09-reliability/fmea-slc02.md | 0 |  |
| FM-S02-06 | 09-reliability/fmea-slc02.md | 0 |  |
| FM-S02-07 | 09-reliability/fmea-slc02.md | 0 |  |
| FM-S02-08 | 09-reliability/fmea-slc02.md | 0 |  |
| FM-S03-01 | 09-reliability/fmea-slc03.md | 1 | 03-domain/contexts/BC04/task-lifecycle-rules.md |
| FM-S03-02 | 09-reliability/fmea-slc03.md | 0 |  |
| FM-S03-03 | 09-reliability/fmea-slc03.md | 0 |  |
| FM-S03-04 | 09-reliability/fmea-slc03.md | 1 | 03-domain/contexts/BC07/field-sync-protocol.md |
| FM-S04-01 | 09-reliability/fmea-slc04.md | 0 |  |
| FM-S04-02 | 09-reliability/fmea-slc04.md | 0 |  |
| FM-S04-03 | 09-reliability/fmea-slc04.md | 0 |  |
| FM-S04-04 | 09-reliability/fmea-slc04.md | 0 |  |
| FM-S05-01 | 09-reliability/fmea-slc05.md | 0 |  |
| FM-S05-02 | 09-reliability/fmea-slc05.md | 0 |  |
| FM-S05-03 | 09-reliability/fmea-slc05.md | 0 |  |
| FM-S05-04 | 09-reliability/fmea-slc05.md | 0 |  |
| FM-S05-05 | 09-reliability/fmea-slc05.md | 0 |  |
| FM-S06-01 | 09-reliability/fmea-slc06.md | 0 |  |
| FM-S06-02 | 09-reliability/fmea-slc06.md | 0 |  |
| FM-S06-03 | 09-reliability/fmea-slc06.md | 0 |  |
| FM-S06-04 | 09-reliability/fmea-slc06.md | 0 |  |
| FM-S06-05 | 09-reliability/fmea-slc06.md | 0 |  |
| FM-S07-01 | 09-reliability/fmea-slc07.md | 0 |  |
| FM-S07-02 | 09-reliability/fmea-slc07.md | 0 |  |
| FM-S07-03 | 09-reliability/fmea-slc07.md | 0 |  |
| FM-S07-04 | 09-reliability/fmea-slc07.md | 0 |  |
| FM-S08-01 | 09-reliability/fmea-slc08.md | 0 |  |
| FM-S08-02 | 09-reliability/fmea-slc08.md | 0 |  |
| FM-S08-03 | 09-reliability/fmea-slc08.md | 0 |  |
| FM-S09-01 | 09-reliability/fmea-slc09.md | 0 |  |
| FM-S09-02 | 09-reliability/fmea-slc09.md | 0 |  |
| FM-S09-03 | 09-reliability/fmea-slc09.md | 0 |  |
| FM-S10-01 | 09-reliability/fmea-slc10.md | 0 |  |
| FM-S10-02 | 09-reliability/fmea-slc10.md | 0 |  |
| FM-S10-03 | 09-reliability/fmea-slc10.md | 0 |  |
| FM-S10-04 | 09-reliability/fmea-slc10.md | 0 |  |
| FM-S11-01 | 09-reliability/fmea-slc11.md | 0 |  |
| FM-S11-02 | 09-reliability/fmea-slc11.md | 0 |  |
| FM-S11-03 | 09-reliability/fmea-slc11.md | 0 |  |
| FM-S11-04 | 09-reliability/fmea-slc11.md | 0 |  |
| FM-S12-01 | 09-reliability/fmea-slc12a.md | 0 |  |
| FM-S12-02 | 09-reliability/fmea-slc12a.md | 0 |  |
| FM-S12-03 | 09-reliability/fmea-slc12a.md | 0 |  |
| FM-S12-P1 | 09-reliability/fmea-slc12.md | 0 |  |
| FM-S12-P2 | 09-reliability/fmea-slc12.md | 0 |  |
| FM-S12-P3 | 09-reliability/fmea-slc12.md | 0 |  |
| FM-S14-01 | 09-reliability/fmea-slc14.md | 0 |  |
| FM-S15-01 | 09-reliability/fmea-slc15.md | 0 |  |
| FM-S16-01 | 09-reliability/fmea-slc16.md | 0 |  |
| FM-S16-02 | 09-reliability/fmea-slc16.md | 0 |  |
| FM-S17-01 | 09-reliability/fmea-slc17.md | 0 |  |
| FM-S17-02 | 09-reliability/fmea-slc17.md | 3 | 03-domain/contexts/BC04/risk-contingency-spec.md; 14-slices/SLC-17/atam-lite.md; 16-reports/SESSION-W4-W7-SLC17.md |
| FM-S18-01 | 09-reliability/fmea-slc18.md | 2 | 14-slices/SLC-18/readiness.md; 16-reports/SESSION-W4-W7-SLC18.md |
| FM-S18-02 | 09-reliability/fmea-slc18.md | 1 | 16-reports/SESSION-W4-W7-SLC18.md |
| FM-S19-01 | 09-reliability/fmea-slc19.md | 1 | 16-reports/SESSION-W4-W7-SLC19.md |
| FM-S19-02 | 09-reliability/fmea-slc19.md | 0 |  |

### Family: FMEA

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| FMEA-SLC01 | 09-reliability/fmea-slc01.md | 0 |  |
| FMEA-SLC02 | 09-reliability/fmea-slc02.md | 0 |  |
| FMEA-SLC03 | 09-reliability/fmea-slc03.md | 0 |  |
| FMEA-SLC04 | 09-reliability/fmea-slc04.md | 0 |  |
| FMEA-SLC05 | 09-reliability/fmea-slc05.md | 0 |  |
| FMEA-SLC06 | 09-reliability/fmea-slc06.md | 0 |  |
| FMEA-SLC07 | 09-reliability/fmea-slc07.md | 0 |  |
| FMEA-SLC08 | 09-reliability/fmea-slc08.md | 0 |  |
| FMEA-SLC09 | 09-reliability/fmea-slc09.md | 0 |  |
| FMEA-SLC10 | 09-reliability/fmea-slc10.md | 0 |  |
| FMEA-SLC11 | 09-reliability/fmea-slc11.md | 0 |  |
| FMEA-SLC12 | 09-reliability/fmea-slc12.md | 0 |  |
| FMEA-SLC12A | 09-reliability/fmea-slc12a.md | 0 |  |
| FMEA-SLC14 | 09-reliability/fmea-slc14.md | 0 |  |
| FMEA-SLC15 | 09-reliability/fmea-slc15.md | 0 |  |
| FMEA-SLC16 | 09-reliability/fmea-slc16.md | 0 |  |
| FMEA-SLC17 | 09-reliability/fmea-slc17.md | 0 |  |
| FMEA-SLC18 | 09-reliability/fmea-slc18.md | 0 |  |
| FMEA-SLC19 | 09-reliability/fmea-slc19.md | 0 |  |

### Family: GATE

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| GATE-FINAL-R1 | 16-reports/gate-reports/GATE-STATUS-FINAL-R1.md | 0 |  |
| GATE-SLC01 | 16-reports/gate-reports/GATE-STATUS-SLC01.md | 0 |  |
| GATE-SLC02 | 16-reports/gate-reports/GATE-STATUS-SLC02.md | 0 |  |
| GATE-SLC03 | 16-reports/gate-reports/GATE-STATUS-SLC03.md | 0 |  |
| GATE-SLC04 | 16-reports/gate-reports/GATE-STATUS-SLC04.md | 0 |  |
| GATE-SLC05 | 16-reports/gate-reports/GATE-STATUS-SLC05.md | 0 |  |
| GATE-SLC06 | 16-reports/gate-reports/GATE-STATUS-SLC06.md | 0 |  |
| GATE-SLC07 | 16-reports/gate-reports/GATE-STATUS-SLC07.md | 0 |  |
| GATE-SLC08 | 16-reports/gate-reports/GATE-STATUS-SLC08.md | 0 |  |
| GATE-SLC11 | 16-reports/gate-reports/GATE-STATUS-SLC11.md | 0 |  |
| GATE-SLC12A | 16-reports/gate-reports/GATE-STATUS-SLC12a.md | 0 |  |
| GATE-W0 | 16-reports/gate-reports/GATE-STATUS-W0.md | 0 |  |
| GATE-W1 | 16-reports/gate-reports/GATE-STATUS-W1.md | 0 |  |
| GATE-W2 | 16-reports/gate-reports/GATE-STATUS-W2.md | 0 |  |
| GATE-W3 | 16-reports/gate-reports/GATE-STATUS-W3.md | 0 |  |
| GATE-W8 | 16-reports/gate-reports/GATE-STATUS-W8.md | 0 |  |

### Family: HAP

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| HAP-01 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 7 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 01-business/system-definition.md; 16-reports/SESSION-W0.md; 16-reports/gate-reports/GATE-STATUS-FINAL-R1.md; 16-repo ...(truncated) |
| HAP-02 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 11 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 00-governance/registers/assumptions.md; 00-governance/registers/risks.md; 00-governance/registers/technical-debt.md; ...(truncated) |
| HAP-03 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 2 | 00-governance/decisions/ADR-P08.md; 00-governance/registers/dependencies.md |
| HAP-04 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 9 | 00-governance/decisions/ADR-P01.md; 00-governance/decisions/ADR-P02.md; 00-governance/decisions/ADR-P03.md; 00-governance/decisions/ADR-P07.md; 00-governance/decisions/ADR-P09.md; 00-governance/decisi ...(truncated) |
| HAP-05 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 5 | 00-governance/decisions/ADR-P04.md; 00-governance/decisions/ADR-P06.md; 00-governance/decisions/ADR-P11.md; 00-governance/decisions/ADR-P12.md; 00-governance/registers/dependencies.md |
| HAP-06 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 4 | 00-governance/decisions/ADR-P10.md; 00-governance/elicitation/W1-answers.md; 02-requirements/requirements.md; 10-ai/autonomy-matrix.md |
| HAP-07 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 1 | 00-governance/elicitation/W1-answers.md |
| HAP-08 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 1 | 00-governance/decisions/ADR-P05.md |
| HAP-09 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 19 | 14-slices/SLC-01/readiness.md; 14-slices/SLC-02/readiness.md; 14-slices/SLC-03/readiness.md; 14-slices/SLC-04/readiness.md; 14-slices/SLC-05/readiness.md; 14-slices/SLC-06/readiness.md; 14-slices/SLC- ...(truncated) |
| HAP-10 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 1 | 16-reports/IMPLEMENTATION-READINESS-R1.md |
| HAP-11 | 00-governance/RATIFICATION-PACKAGE.md;00-governance/registers/human-approvals.md | 4 | README.md; 16-reports/IMPLEMENTATION-READINESS-R1.md; 16-reports/SESSION-W2.md; 16-reports/SESSION-W3.md |

### Family: INV

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| INV-ACS-01 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md | 2 | 13-verification/acceptance/SLC-07/invariants-slc07.md; 13-verification/tooling/slice-sources.md |
| INV-ACS-02 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md | 2 | 13-verification/acceptance/SLC-07/invariants-slc07.md; 13-verification/tooling/slice-sources.md |
| INV-ACS-03 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ACS-04 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ADP-01 | 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ADP-02 | 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ADP-03 | 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AIR-01 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AIR-02 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AIR-03 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AIR-04 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AIR-05 | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AIRS-01 | 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md | 2 | 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 13-verification/tooling/slice-sources.md |
| INV-AIRS-02 | 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AIRS-03 | 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ALC-01 | 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ALC-02 | 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md | 2 | 03-domain/contexts/BC05/allocation-readiness-spec.md; 13-verification/tooling/slice-sources.md |
| INV-ALC-03 | 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ALC-04 | 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ALR-01 | 03-domain/contexts/BC03/aggregates/AGG-ALERT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ALR-02 | 03-domain/contexts/BC03/aggregates/AGG-ALERT.md | 6 | 03-domain/contexts/BC03/situation-alerting-spec.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 08-security/label-derivation-rules.md; 08-security/threat-model-slc06.md; 13-verification/acce ...(truncated) |
| INV-ALR-03 | 03-domain/contexts/BC03/aggregates/AGG-ALERT.md | 2 | 03-domain/contexts/BC03/situation-alerting-spec.md; 13-verification/tooling/slice-sources.md |
| INV-AMT-01 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AMT-02 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ARC-01 | 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ARC-02 | 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ARC-03 | 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ARC-04 | 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ARL-01 | 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md | 2 | 13-verification/acceptance/SLC-06/invariants-slc06.md; 13-verification/tooling/slice-sources.md |
| INV-ARL-02 | 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ARL-03 | 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ASG-01 | 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ASG-02 | 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ASM-01 | 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ASM-02 | 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ASM-03 | 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 13-verification/acceptance/SLC-07/invariants-slc07.md; 13-verification/tooling/slice-sources.md |
| INV-ASM-04 | 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AST-01 | 03-domain/contexts/BC05/aggregates/AGG-ASSET.md | 5 | 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 03-domain/contexts/BC05/aggregates/AGG-MAI ...(truncated) |
| INV-AST-02 | 03-domain/contexts/BC05/aggregates/AGG-ASSET.md | 4 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 13-verification/tooling/slice-sources.md |
| INV-AST-03 | 03-domain/contexts/BC05/aggregates/AGG-ASSET.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AST-04 | 03-domain/contexts/BC05/aggregates/AGG-ASSET.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ATT-01 | 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ATT-02 | 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ATT-03 | 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ATT-04 | 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-AUT-01 | 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md | 3 | 08-security/threat-model-slc01.md; 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-AUT-02 | 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-AUT-03 | 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md | 3 | 00-governance/glossary.md; 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-AUT-04 | 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-CAP-01 | 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CAP-02 | 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CAP-03 | 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CLM-01 | 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md | 2 | 13-verification/tooling/slice-sources.md; 16-reports/ARCHITECTURE-REVIEW-R1.md |
| INV-CLM-02 | 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md | 2 | 03-domain/contexts/BC02/claims-temporal-kernel.md; 13-verification/tooling/slice-sources.md |
| INV-CLM-03 | 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CLM-04 | 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CLM-05 | 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CLR-01 | 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CLR-02 | 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md | 2 | 08-security/threat-model-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-CLR-03 | 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-CLR-04 | 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CLS-01 | 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CLS-02 | 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CLS-03 | 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-CLS-04 | 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md | 2 | 00-governance/registers/corrections.md; 13-verification/tooling/slice-sources.md |
| INV-CNF-01 | 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CNF-02 | 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CNF-03 | 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CNF-04 | 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md | 8 | 03-domain/contexts/BC02/conflict-detection-engine.md; 03-domain/contexts/BC02/queries-slc04.md; 05-contracts/openapi-information-slc04.md; 08-security/label-derivation-rules.md; 08-security/policies-s ...(truncated) |
| INV-CNF-05 | 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CON-01 | 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CON-02 | 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 13-verification/tooling/slice-sources.md |
| INV-CON-03 | 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CPL-01 | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CPL-02 | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CRD-01 | 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CRD-02 | 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md | 3 | 00-governance/glossary.md; 08-security/threat-model-slc15.md; 13-verification/tooling/slice-sources.md |
| INV-CRD-03 | 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md | 3 | 03-domain/contexts/BC02/correlation-fusion-spec.md; 08-security/threat-model-slc15.md; 13-verification/tooling/slice-sources.md |
| INV-CRD-04 | 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CRP-01 | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CRP-02 | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CRP-03 | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CRP-04 | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md | 4 | 00-governance/glossary.md; 03-domain/contexts/BC02/correlation-fusion-spec.md; 08-security/threat-model-slc15.md; 13-verification/tooling/slice-sources.md |
| INV-CRQ-01 | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md | 2 | 08-security/threat-model-slc14.md; 13-verification/tooling/slice-sources.md |
| INV-CRQ-02 | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CRQ-03 | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CRQ-04 | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CRR-01 | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-CRR-02 | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DEC-01 | 03-domain/contexts/BC04/aggregates/AGG-DECISION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DEC-02 | 03-domain/contexts/BC04/aggregates/AGG-DECISION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DEC-03 | 03-domain/contexts/BC04/aggregates/AGG-DECISION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DEC-04 | 03-domain/contexts/BC04/aggregates/AGG-DECISION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DEV-01 | 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DEV-02 | 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DEV-03 | 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DEV-04 | 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DRQ-01 | 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DRQ-02 | 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DRQ-03 | 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DSP-01 | 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DSP-02 | 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md | 2 | 08-security/key-hierarchy-and-disposition.md; 13-verification/tooling/slice-sources.md |
| INV-DSP-03 | 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DSP-04 | 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DST-01 | 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DST-02 | 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-DST-03 | 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ENT-01 | 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ENT-02 | 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md | 6 | 03-domain/contexts/BC02/claims-temporal-kernel.md; 03-domain/contexts/BC02/queries-slc02.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/acceptance/SLC-02 ...(truncated) |
| INV-ENT-03 | 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ER-01 | 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md | 2 | 13-verification/acceptance/SLC-04/invariants-slc04.md; 13-verification/tooling/slice-sources.md |
| INV-ER-02 | 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ER-03 | 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md | 2 | 13-verification/acceptance/SLC-04/invariants-slc04.md; 13-verification/tooling/slice-sources.md |
| INV-ER-04 | 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md | 3 | 03-domain/contexts/BC02/candidate-generation.md; 13-verification/acceptance/SLC-04/invariants-slc04.md; 13-verification/tooling/slice-sources.md |
| INV-ER-05 | 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md | 2 | 13-verification/acceptance/SLC-04/invariants-slc04.md; 13-verification/tooling/slice-sources.md |
| INV-ER-06 | 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md | 2 | 00-governance/glossary.md; 13-verification/tooling/slice-sources.md |
| INV-ERS-01 | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ERS-02 | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md | 2 | 13-verification/acceptance/SLC-12a/invariants-slc12a.md; 13-verification/tooling/slice-sources.md |
| INV-ERS-03 | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md | 2 | 08-security/key-hierarchy-and-disposition.md; 13-verification/tooling/slice-sources.md |
| INV-ERS-04 | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-EVD-01 | 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-EVD-02 | 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-EVD-03 | 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-EVL-01 | 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-EVL-02 | 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md | 2 | 08-security/label-derivation-rules.md; 13-verification/tooling/slice-sources.md |
| INV-EVS-01 | 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-EVS-02 | 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-EXC-01 | 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-EXC-02 | 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-EXC-03 | 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-EXR-01 | 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md | 6 | 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 06-data/logical-model/slc-19.md; 08-security/threat-mo ...(truncated) |
| INV-EXR-02 | 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md | 5 | 03-domain/contexts/BC05/training-exercise-spec.md; 08-security/threat-model-slc19.md; 13-verification/tooling/slice-sources.md; 14-slices/SLC-19/readiness.md; 16-reports/SESSION-W4-W7-SLC19.md |
| INV-EXT-01 | 03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md | 2 | 13-verification/acceptance/SLC-02/invariants-slc02.md; 13-verification/tooling/slice-sources.md |
| INV-EXT-02 | 03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-FND-01 | 03-domain/contexts/BC03/aggregates/AGG-FINDING.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-FND-02 | 03-domain/contexts/BC03/aggregates/AGG-FINDING.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-HRS-01 | 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md | 2 | 08-security/threat-model-slc16.md; 13-verification/tooling/slice-sources.md |
| INV-HRS-02 | 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-HRS-03 | 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-IMP-01 | 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-IMP-02 | 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-IMP-03 | 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-IMP-04 | 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-INC-01 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md | 5 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 08-security/policies-slc17.md; 08-security/threat-model-slc17.md; 13-verification/tooling/slice-sources.md |
| INV-INC-02 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md | 4 | 03-domain/contexts/BC04/commands-slc17.md; 08-security/policies-slc17.md; 09-reliability/fmea-slc17.md; 13-verification/tooling/slice-sources.md |
| INV-INC-03 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md | 6 | 03-domain/contexts/BC04/commands-slc17.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 08-security/policies-slc17.md; 08-security/threat-model-slc17.md; 13-verification/tooling/slice-sources.md; ...(truncated) |
| INV-INC-04 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md | 3 | 03-domain/contexts/BC04/risk-contingency-spec.md; 08-security/threat-model-slc17.md; 13-verification/tooling/slice-sources.md |
| INV-INC-05 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-KNO-01 | 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-KNO-02 | 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-KNO-03 | 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-LGR-01 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md | 3 | 06-data/logical-model/slc-18.md; 08-security/threat-model-slc18.md; 13-verification/tooling/slice-sources.md |
| INV-LGR-02 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md | 2 | 08-security/policies-slc18.md; 13-verification/tooling/slice-sources.md |
| INV-LGR-03 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md | 4 | 03-domain/contexts/BC05/logistics-spec.md; 08-security/threat-model-slc18.md; 13-verification/acceptance/SLC-18/invariants-slc18.md; 13-verification/tooling/slice-sources.md |
| INV-LGR-04 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md | 2 | 13-verification/acceptance/SLC-18/invariants-slc18.md; 13-verification/tooling/slice-sources.md |
| INV-LGR-05 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md | 4 | 03-domain/contexts/BC05/logistics-spec.md; 13-verification/tooling/slice-sources.md; 14-slices/SLC-18/readiness.md; 16-reports/SESSION-W4-W7-SLC18.md |
| INV-LHD-01 | 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-LHD-02 | 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md | 2 | 13-verification/acceptance/SLC-12a/invariants-slc12a.md; 13-verification/tooling/slice-sources.md |
| INV-LHD-03 | 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-LHD-04 | 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md | 2 | 08-security/threat-model-slc12a.md; 13-verification/tooling/slice-sources.md |
| INV-MDL-01 | 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-MDL-02 | 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-MDL-03 | 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-MNT-01 | 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-MNT-02 | 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-MRS-01 | 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-MRS-02 | 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-MRS-03 | 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md | 2 | 03-domain/contexts/BC02/candidate-generation.md; 13-verification/tooling/slice-sources.md |
| INV-NTF-01 | 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-NTF-02 | 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md | 3 | 03-domain/contexts/BC03/situation-alerting-spec.md; 08-security/threat-model-slc06.md; 13-verification/tooling/slice-sources.md |
| INV-NTF-03 | 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-OBS-01 | 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-OBS-02 | 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-OBS-03 | 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-OBS-04 | 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md | 2 | 03-domain/contexts/BC07/field-sync-protocol.md; 13-verification/tooling/slice-sources.md |
| INV-ORG-01 | 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-ORG-02 | 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ORG-03 | 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ORG-04 | 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-OUT-01 | 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-OUT-02 | 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PER-01 | 03-domain/contexts/BC01/aggregates/AGG-PERSON.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PER-02 | 03-domain/contexts/BC01/aggregates/AGG-PERSON.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PKG-01 | 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PKG-02 | 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PKG-03 | 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PLN-01 | 03-domain/contexts/BC04/aggregates/AGG-PLAN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PLN-02 | 03-domain/contexts/BC04/aggregates/AGG-PLAN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PLN-03 | 03-domain/contexts/BC04/aggregates/AGG-PLAN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PLN-04 | 03-domain/contexts/BC04/aggregates/AGG-PLAN.md | 3 | 00-governance/registers/corrections.md; 06-data/logical-model/slc-17.md; 13-verification/tooling/slice-sources.md |
| INV-PLV-01 | 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PLV-02 | 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PLV-03 | 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md | 2 | 03-domain/contexts/BC04/decision-plan-spec.md; 13-verification/tooling/slice-sources.md |
| INV-PLV-04 | 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md | 2 | 03-domain/contexts/BC04/decision-plan-spec.md; 13-verification/tooling/slice-sources.md |
| INV-PLV-05 | 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-POL-01 | 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-POL-02 | 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md | 4 | 08-security/policies-slc01.md; 08-security/threat-model-slc01.md; 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-POL-03 | 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-POL-04 | 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PRD-01 | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PRD-02 | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PRD-03 | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PRD-04 | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PRJ-01 | 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md | 3 | 03-domain/contexts/BC07/discovery-architecture.md; 06-data/logical-model/slc-05.md; 13-verification/tooling/slice-sources.md |
| INV-PRJ-02 | 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PRJ-03 | 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PRJ-04 | 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md | 2 | 03-domain/contexts/BC07/discovery-architecture.md; 13-verification/tooling/slice-sources.md |
| INV-PTM-01 | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-PTM-02 | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-QUAL-01 | 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-QUAL-02 | 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RAS-01 | 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md | 3 | 08-security/threat-model-slc01.md; 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-RAS-02 | 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-RAS-03 | 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-REC-01 | 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-REC-02 | 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-REC-03 | 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md | 2 | 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 13-verification/tooling/slice-sources.md |
| INV-REL-01 | 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-REL-02 | 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RIS-01 | 03-domain/contexts/BC04/aggregates/AGG-RISK.md | 3 | 03-domain/contexts/BC04/commands-slc17.md; 08-security/policies-slc17.md; 13-verification/tooling/slice-sources.md |
| INV-RIS-02 | 03-domain/contexts/BC04/aggregates/AGG-RISK.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 13-verification/tooling/slice-sources.md |
| INV-RIS-03 | 03-domain/contexts/BC04/aggregates/AGG-RISK.md | 3 | 03-domain/contexts/BC04/commands-slc17.md; 09-reliability/observability-slc17.md; 13-verification/tooling/slice-sources.md |
| INV-RIS-04 | 03-domain/contexts/BC04/aggregates/AGG-RISK.md | 3 | 03-domain/contexts/BC04/commands-slc17.md; 08-security/threat-model-slc17.md; 13-verification/tooling/slice-sources.md |
| INV-RIS-05 | 03-domain/contexts/BC04/aggregates/AGG-RISK.md | 4 | 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 08-security/threat-model-slc17.md; 13-verification/tooling/slice-sources.md |
| INV-ROL-01 | 03-domain/contexts/BC01/aggregates/AGG-ROLE.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-ROL-02 | 03-domain/contexts/BC01/aggregates/AGG-ROLE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-ROL-03 | 03-domain/contexts/BC01/aggregates/AGG-ROLE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RPL-01 | 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RPL-02 | 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md | 3 | 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/logistics-spec.md; 13-verification/tooling/slice-sources.md |
| INV-RRQ-01 | 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RRQ-02 | 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RSV-01 | 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RSV-02 | 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RTG-01 | 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RTG-02 | 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RTG-03 | 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RTS-01 | 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RTS-02 | 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md | 2 | 13-verification/acceptance/SLC-12a/invariants-slc12a.md; 13-verification/tooling/slice-sources.md |
| INV-RTS-03 | 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RUN-01 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RUN-02 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md | 3 | 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 08-security/label-derivation-rules.md; 13-verification/tooling/slice-sources.md |
| INV-RUN-03 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RUN-04 | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RWE-01 | 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-RWE-02 | 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SCF-01 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SCF-02 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md | 2 | 03-domain/contexts/BC07/field-sync-protocol.md; 13-verification/tooling/slice-sources.md |
| INV-SCF-03 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md | 3 | 03-domain/contexts/BC07/field-sync-protocol.md; 08-security/threat-model-slc11.md; 13-verification/tooling/slice-sources.md |
| INV-SCN-01 | 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md | 4 | 02-requirements/requirements.md; 03-domain/contexts/BC05/commands-slc19.md; 06-data/logical-model/slc-19.md; 13-verification/tooling/slice-sources.md |
| INV-SCN-02 | 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SHP-01 | 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md | 5 | 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 06-data/logical-model/slc-18.md; 08-security/policies-slc18.md; 08-security/threat-model-slc18.md; 13-verification/tooling/slice-sources.md |
| INV-SHP-02 | 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md | 7 | 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/logistics-spec.md; 08-security/policies-slc18.md; 08-security/threat-model-slc18.md; 09-reliability/observability-slc18.md; 13-verifi ...(truncated) |
| INV-SHP-03 | 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md | 6 | 06-data/logical-model/slc-18.md; 08-security/threat-model-slc18.md; 09-reliability/fmea-slc18.md; 13-verification/acceptance/SLC-18/invariants-slc18.md; 13-verification/tooling/slice-sources.md; 16-re ...(truncated) |
| INV-SHP-04 | 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md | 4 | 08-security/policies-slc18.md; 08-security/threat-model-slc18.md; 13-verification/acceptance/SLC-18/invariants-slc18.md; 13-verification/tooling/slice-sources.md |
| INV-SIM-01 | 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md | 5 | 02-requirements/requirements.md; 03-domain/contexts/BC05/commands-slc19.md; 06-data/logical-model/slc-19.md; 08-security/threat-model-slc19.md; 13-verification/tooling/slice-sources.md |
| INV-SIM-02 | 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md | 9 | 02-requirements/quality-scenarios.md; 02-requirements/requirements.md; 03-domain/contexts/BC05/commands-slc19.md; 06-data/logical-model/slc-19.md; 08-security/policies-slc19.md; 08-security/threat-mod ...(truncated) |
| INV-SIM-03 | 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md | 6 | 02-requirements/requirements.md; 03-domain/contexts/BC05/commands-slc19.md; 06-data/logical-model/slc-19.md; 08-security/policies-slc19.md; 08-security/threat-model-slc19.md; 13-verification/tooling/s ...(truncated) |
| INV-SIT-01 | 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SIT-02 | 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md | 2 | 03-domain/contexts/BC03/situation-alerting-spec.md; 13-verification/tooling/slice-sources.md |
| INV-SIT-03 | 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md | 3 | 03-domain/contexts/BC03/situation-alerting-spec.md; 13-verification/acceptance/SLC-06/invariants-slc06.md; 13-verification/tooling/slice-sources.md |
| INV-SIT-04 | 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SNS-01 | 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SNS-02 | 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SNS-03 | 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SRC-01 | 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SRC-02 | 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SRC-03 | 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SRC-04 | 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SUB-01 | 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SUB-02 | 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md | 2 | 13-verification/acceptance/SLC-06/invariants-slc06.md; 13-verification/tooling/slice-sources.md |
| INV-SVC-01 | 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SVC-02 | 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SVC-03 | 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SYN-01 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SYN-02 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SYN-03 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-SYN-04 | 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TASK-01 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TASK-02 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TASK-03 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TASK-04 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TASK-05 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TASK-06 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md | 7 | 00-governance/glossary.md; 00-governance/registers/corrections.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-PL ...(truncated) |
| INV-TASK-07 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md | 4 | 02-requirements/requirements.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 08-security/threat-model-slc03.md; 13-verification/tooling/slice-sources.md |
| INV-TASK-08 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md | 2 | 03-domain/contexts/BC04/task-lifecycle-rules.md; 13-verification/tooling/slice-sources.md |
| INV-TASK-09 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md | 4 | 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 08-security/threat-model-slc03.md; 13-verification/tooling/slice-sources.md |
| INV-TEN-01 | 03-domain/contexts/BC01/aggregates/AGG-TENANT.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-TEN-02 | 03-domain/contexts/BC01/aggregates/AGG-TENANT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TEN-03 | 03-domain/contexts/BC01/aggregates/AGG-TENANT.md | 3 | 03-domain/contexts/BC01/commands-slc01.md; 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| INV-TEN-04 | 03-domain/contexts/BC01/aggregates/AGG-TENANT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TEN-05 | 03-domain/contexts/BC01/aggregates/AGG-TENANT.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TOL-01 | 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md | 2 | 08-security/threat-model-slc10.md; 13-verification/tooling/slice-sources.md |
| INV-TOL-02 | 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TOL-03 | 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TTY-01 | 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TTY-02 | 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-TTY-03 | 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-USR-01 | 03-domain/contexts/BC01/aggregates/AGG-USER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-USR-02 | 03-domain/contexts/BC01/aggregates/AGG-USER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-USR-03 | 03-domain/contexts/BC01/aggregates/AGG-USER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-USR-04 | 03-domain/contexts/BC01/aggregates/AGG-USER.md | 1 | 13-verification/tooling/slice-sources.md |
| INV-USR-05 | 03-domain/contexts/BC01/aggregates/AGG-USER.md | 1 | 13-verification/tooling/slice-sources.md |

### Family: LABEL

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| LABEL-DERIVATION | 08-security/label-derivation-rules.md | 5 | 00-governance/glossary.md; 00-governance/registers/corrections.md; 02-requirements/requirements.md; 13-verification/spec-lint-rules.md; 15-traceability/trace-platform.md |

### Family: LANGUAGE

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| LANGUAGE-MODEL | 04-information/language-model.md | 1 | 03-domain/contexts/BC02/candidate-generation.md |

### Family: LDM

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| LDM-SLC01 | 06-data/logical-model/slc-01.md | 2 | 06-data/logical-model/slc-02.md; 06-data/logical-model/slc-03.md |
| LDM-SLC02 | 06-data/logical-model/slc-02.md | 2 | 12-solution/technology-decisions.md; 12-solution/w8-inputs.md |
| LDM-SLC03 | 06-data/logical-model/slc-03.md | 0 |  |
| LDM-SLC04 | 06-data/logical-model/slc-04.md | 0 |  |
| LDM-SLC05 | 06-data/logical-model/slc-05.md | 0 |  |
| LDM-SLC06 | 06-data/logical-model/slc-06.md | 0 |  |
| LDM-SLC07 | 06-data/logical-model/slc-07.md | 0 |  |
| LDM-SLC08 | 06-data/logical-model/slc-08.md | 0 |  |
| LDM-SLC09 | 06-data/logical-model/slc-09.md | 0 |  |
| LDM-SLC10 | 06-data/logical-model/slc-10.md | 0 |  |
| LDM-SLC11 | 06-data/logical-model/slc-11.md | 0 |  |
| LDM-SLC12 | 06-data/logical-model/slc-12.md | 0 |  |
| LDM-SLC12A | 06-data/logical-model/slc-12a.md | 0 |  |
| LDM-SLC14 | 06-data/logical-model/slc-14.md | 0 |  |
| LDM-SLC15 | 06-data/logical-model/slc-15.md | 0 |  |
| LDM-SLC16 | 06-data/logical-model/slc-16.md | 0 |  |
| LDM-SLC17 | 06-data/logical-model/slc-17.md | 0 |  |
| LDM-SLC18 | 06-data/logical-model/slc-18.md | 0 |  |
| LDM-SLC19 | 06-data/logical-model/slc-19.md | 0 |  |

### Family: LIB

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| LIB-CLAIMS-KERNEL | 03-domain/contexts/BC02/claims-temporal-kernel.md | 13 | 00-governance/glossary.md; 00-governance/RATIFICATION-PACKAGE.md; 03-domain/contexts/BC02/conflict-detection-engine.md; 03-domain/contexts/BC02/correlation-fusion-spec.md; 03-domain/contexts/BC06/prod ...(truncated) |

### Family: META

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| META-MODEL | 04-information/meta-model.md | 2 | 00-governance/glossary.md; 03-domain/contexts/BC02/claims-temporal-kernel.md |

### Family: OBJECT

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| OBJECT-ENVELOPE | 04-information/object-envelope.md | 0 |  |

### Family: OBS

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| OBS-SLC01 | 09-reliability/observability-slc01.md | 0 |  |
| OBS-SLC02 | 09-reliability/observability-slc02.md | 0 |  |
| OBS-SLC03 | 09-reliability/observability-slc03.md | 0 |  |
| OBS-SLC04 | 09-reliability/observability-slc04.md | 0 |  |
| OBS-SLC05 | 09-reliability/observability-slc05.md | 0 |  |
| OBS-SLC06 | 09-reliability/observability-slc06.md | 0 |  |
| OBS-SLC07 | 09-reliability/observability-slc07.md | 0 |  |
| OBS-SLC08 | 09-reliability/observability-slc08.md | 0 |  |
| OBS-SLC09 | 09-reliability/observability-slc09.md | 0 |  |
| OBS-SLC10 | 09-reliability/observability-slc10.md | 0 |  |
| OBS-SLC11 | 09-reliability/observability-slc11.md | 0 |  |
| OBS-SLC12 | 09-reliability/observability-slc12.md | 0 |  |
| OBS-SLC12A | 09-reliability/observability-slc12a.md | 0 |  |
| OBS-SLC14 | 09-reliability/observability-slc14.md | 0 |  |
| OBS-SLC15 | 09-reliability/observability-slc15.md | 0 |  |
| OBS-SLC16 | 09-reliability/observability-slc16.md | 0 |  |
| OBS-SLC17 | 09-reliability/observability-slc17.md | 0 |  |
| OBS-SLC18 | 09-reliability/observability-slc18.md | 0 |  |
| OBS-SLC19 | 09-reliability/observability-slc19.md | 0 |  |

### Family: OPENAPI

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| OPENAPI-BC01-INTERNAL | 05-contracts/openapi-foundation-internal-slc01.md | 1 | 13-verification/tooling/spec-tooling.md |
| OPENAPI-BC01-SLC01 | 05-contracts/openapi-foundation-slc01.md | 0 |  |
| OPENAPI-BC01-SLC11 | 05-contracts/openapi-foundation-slc11.md | 0 |  |
| OPENAPI-BC01-SLC16 | 05-contracts/openapi-foundation-slc16.md | 0 |  |
| OPENAPI-BC02-SLC02 | 05-contracts/openapi-information-slc02.md | 0 |  |
| OPENAPI-BC02-SLC04 | 05-contracts/openapi-information-slc04.md | 0 |  |
| OPENAPI-BC02-SLC14 | 05-contracts/openapi-information-slc14.md | 0 |  |
| OPENAPI-BC02-SLC15 | 05-contracts/openapi-information-slc15.md | 0 |  |
| OPENAPI-BC03-SLC06 | 05-contracts/openapi-intelligence-slc06.md | 0 |  |
| OPENAPI-BC03-SLC07 | 05-contracts/openapi-intelligence-slc07.md | 0 |  |
| OPENAPI-BC03-SLC16 | 05-contracts/openapi-intelligence-slc16.md | 0 |  |
| OPENAPI-BC04-SLC03 | 05-contracts/openapi-operations-slc03.md | 0 |  |
| OPENAPI-BC04-SLC06 | 05-contracts/openapi-operations-slc06.md | 0 |  |
| OPENAPI-BC04-SLC08 | 05-contracts/openapi-operations-slc08.md | 0 |  |
| OPENAPI-BC04-SLC15 | 05-contracts/openapi-operations-slc15.md | 0 |  |
| OPENAPI-BC04-SLC17 | 05-contracts/openapi-operations-slc17.md | 0 |  |
| OPENAPI-BC05-SLC03 | 05-contracts/openapi-readiness-slc03.md | 0 |  |
| OPENAPI-BC05-SLC09 | 05-contracts/openapi-readiness-slc09.md | 0 |  |
| OPENAPI-BC05-SLC18 | 05-contracts/openapi-readiness-slc18.md | 0 |  |
| OPENAPI-BC05-SLC19 | 05-contracts/openapi-readiness-slc19.md | 0 |  |
| OPENAPI-BC06-SLC12 | 05-contracts/openapi-knowledge-slc12.md | 0 |  |
| OPENAPI-BC07-SLC02 | 05-contracts/openapi-integration-slc02.md | 0 |  |
| OPENAPI-BC07-SLC05 | 05-contracts/openapi-discovery-slc05.md | 0 |  |
| OPENAPI-BC07-SLC10 | 05-contracts/openapi-ai-slc10.md | 0 |  |
| OPENAPI-BC07-SLC11 | 05-contracts/openapi-field-slc11.md | 0 |  |
| OPENAPI-BC07-SLC16 | 05-contracts/openapi-integration-slc16.md | 0 |  |
| OPENAPI-BC08-SLC01 | 05-contracts/openapi-governance-slc01.md | 0 |  |
| OPENAPI-BC08-SLC12A | 05-contracts/openapi-governance-slc12a.md | 0 |  |

### Family: OQ

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| OQ-001 | 00-governance/registers/open-questions.md | 3 | 00-governance/registers/corrections.md; 02-requirements/use-cases.md; 16-reports/SESSION-W0.md |
| OQ-010 | 00-governance/registers/open-questions.md | 1 | 01-business/business-rules.md |
| OQ-011 | 00-governance/registers/open-questions.md | 2 | 01-business/business-rules.md; 03-domain/ownership.md |
| OQ-012 | 00-governance/registers/open-questions.md | 1 | 03-domain/ownership.md |
| OQ-013 | 00-governance/registers/open-questions.md | 4 | 03-domain/bc-boundary-test.md; 03-domain/domains.md; 03-domain/ownership.md; 04-information/entity-resolution.md |
| OQ-030 | 00-governance/registers/open-questions.md | 1 | 02-requirements/requirements.md |
| OQ-031 | 00-governance/registers/open-questions.md | 3 | 03-domain/contexts/BC04/task-lifecycle-rules.md; 13-verification/acceptance/SLC-03/invariants-slc03.md; 16-reports/SESSION-W4-W7-SLC03.md |
| OQ-032 | 00-governance/registers/open-questions.md | 5 | 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 13-verification/acceptance/SLC-03/invariants-slc03.md; 13-verification/tooling/slice-sources.md; 16-rep ...(truncated) |
| OQ-033 | 00-governance/registers/open-questions.md | 6 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 13-verification/acceptance/SLC-03/invariants-slc03.md; 13-ve ...(truncated) |

### Family: OUT

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| OUT-01 | 01-business/outcomes.md | 5 | 01-business/capabilities.md; 02-requirements/quality-scenarios.md; 02-requirements/requirements.md; 15-traceability/rtm-r1.md; 15-traceability/rtm-r2.md |
| OUT-02 | 01-business/outcomes.md | 5 | 00-governance/elicitation/W1-answers.md; 01-business/capabilities.md; 01-business/system-definition.md; 02-requirements/requirements.md; 15-traceability/rtm-r1.md |
| OUT-03 | 01-business/outcomes.md | 7 | 01-business/capabilities.md; 02-requirements/quality-scenarios.md; 02-requirements/requirements.md; 09-reliability/observability-slc07.md; 14-slices/SLC-08/atam-lite.md; 15-traceability/rtm-r1.md; 15- ...(truncated) |
| OUT-04 | 01-business/outcomes.md | 14 | 00-governance/elicitation/W1-answers.md; 01-business/capabilities.md; 01-business/system-definition.md; 02-requirements/quality-scenarios.md; 02-requirements/requirements.md; 03-domain/contexts/BC04/c ...(truncated) |
| OUT-05 | 01-business/outcomes.md | 11 | 00-governance/elicitation/W1-answers.md; 01-business/capabilities.md; 01-business/system-definition.md; 02-requirements/requirements.md; 03-domain/contexts/BC04/events-slc08.md; 05-contracts/asyncapi- ...(truncated) |
| OUT-06 | 01-business/outcomes.md | 13 | 01-business/capabilities.md; 01-business/release-3-scope.md; 02-requirements/requirements.md; 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/events-slc12.md; 03-domain/contexts/BC0 ...(truncated) |

### Family: PB

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| PB-01 | 08-security/policies-slc01.md | 2 | 13-verification/acceptance/SLC-01/invariants-slc01.md; 15-traceability/trace-slc01.md |
| PB-02 | 08-security/policies-slc01.md | 0 |  |
| PB-03 | 08-security/policies-slc01.md | 2 | 14-slices/SLC-01/readiness.md; 15-traceability/trace-slc01.md |
| PB-04 | 08-security/policies-slc01.md | 0 |  |
| PB-05 | 08-security/policies-slc01.md | 2 | 08-security/threat-model-slc01.md; 13-verification/acceptance/SLC-01/invariants-slc01.md |
| PB-06 | 08-security/policies-slc01.md | 2 | 08-security/policies-slc03.md; 08-security/threat-model-slc03.md |
| PB-07 | 08-security/policies-slc01.md | 0 |  |
| PB-08 | 08-security/policies-slc02.md | 2 | 08-security/threat-model-slc02.md; 13-verification/acceptance/SLC-02/invariants-slc02.md |
| PB-09 | 08-security/policies-slc02.md | 0 |  |
| PB-10 | 08-security/policies-slc02.md | 2 | 08-security/threat-model-slc02.md; 13-verification/acceptance/SLC-02/invariants-slc02.md |
| PB-11 | 08-security/policies-slc02.md | 1 | 08-security/threat-model-slc02.md |
| PB-12 | 08-security/policies-slc10.md | 1 | 08-security/threat-model-slc10.md |
| PB-13 | 08-security/policies-slc10.md | 1 | 08-security/threat-model-slc10.md |
| PB-14 | 08-security/policies-slc10.md | 0 |  |

### Family: PERF

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| PERF-TEST-STRATEGY | 07-quality/performance-test-strategy.md | 5 | 00-governance/decisions/ADR-P05.md; 12-solution/cell-architecture.md; 15-traceability/quality-verification-matrix.md; 16-reports/ARCHITECTURE-REVIEW-R1.md; 16-reports/IMPLEMENTATION-READINESS-R1.md |

### Family: PL

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| PL-SECURITY-CONTEXT | 03-domain/contexts/BC01/security-context.md | 6 | 00-governance/glossary.md; 05-contracts/openapi-foundation-slc01.md; 08-security/threat-model-slc01.md; 13-verification/tooling/spec-tooling.md; 15-traceability/trace-slc01.md; 16-reports/ARCHITECTURE ...(truncated) |

### Family: POL

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| POL-ACS-ADD-ASSUMPTION | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-ADD-HYPOTHESIS | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-CANCEL | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-CLOSE | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-CREATE | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-DEFINE | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-DEFINE-SCENARIO | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-DESELECT-EVIDENCE | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-GET | 08-security/policies-slc07.md | 0 |  |
| POL-ACS-LIST | 08-security/policies-slc07.md | 0 |  |
| POL-ACS-OPEN | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-RECLASSIFY | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-REOPEN | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-RETIRE-ASSUMPTION | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-SELECT-EVIDENCE | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ACS-UPDATE-HYPOTHESIS | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ADP-ACTIVATE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC07/commands-slc02.md; 05-contracts/openapi-integration-slc02.md |
| POL-ADP-GET | 08-security/policies-slc02.md | 0 |  |
| POL-ADP-REGISTER | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC07/commands-slc02.md; 05-contracts/openapi-integration-slc02.md |
| POL-ADP-RESUME | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC07/commands-slc02.md; 05-contracts/openapi-integration-slc02.md |
| POL-ADP-RETIRE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC07/commands-slc02.md; 05-contracts/openapi-integration-slc02.md |
| POL-ADP-SUSPEND | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC07/commands-slc02.md; 05-contracts/openapi-integration-slc02.md |
| POL-ADP-UPDATE-MAPPING | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC07/commands-slc02.md; 05-contracts/openapi-integration-slc02.md |
| POL-AGG-STATS | 08-security/authorization-model.md | 0 |  |
| POL-AIR-CANCEL | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-AIR-CONTEXT | 08-security/policies-slc10.md | 0 |  |
| POL-AIR-GET | 08-security/policies-slc10.md | 0 |  |
| POL-AIRS-ACCEPT | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-AIRS-ACCEPT-PARTIALLY | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-AIRS-QUEUE | 08-security/policies-slc10.md | 0 |  |
| POL-AIRS-REJECT | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-AIRS-START-REVIEW | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-AIR-SUBMIT | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-AI-USAGE | 08-security/policies-slc10.md | 0 |  |
| POL-ALC-APPROVE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-ALC-LIST | 08-security/policies-slc09.md | 0 |  |
| POL-ALC-PREEMPT | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-ALC-RECORD-CONSUMPTION | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-ALC-REJECT | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-ALC-RELEASE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-ALC-REQUEST | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-ALR-ACKNOWLEDGE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-ALR-DISMISS | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-ALR-LIST | 08-security/policies-slc06.md | 0 |  |
| POL-ALR-RESOLVE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-AMT-ACTIVATE | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-AMT-DEPRECATE | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-AMT-LIST | 08-security/policies-slc07.md | 0 |  |
| POL-AMT-REGISTER | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-AMT-RETIRE | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ARC-MIGRATE-FORMAT | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-ARC-REPAIR | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-ARC-RETRIEVE | 08-security/policies-slc12.md | 0 |  |
| POL-ARC-RETRY-INGEST | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-ARC-SEARCH | 08-security/policies-slc12.md | 0 |  |
| POL-ARC-TRANSFER | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-ARL-ACTIVATE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-ARL-DEFINE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-ARL-DISABLE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-ARL-EDIT | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-ARL-ENABLE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-ARL-RETIRE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-ASG-ASSIGN | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-ASG-CANCEL | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-ASG-RETURN | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-ASM-DISCARD | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ASM-DRAFT | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ASM-EDIT | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ASM-GET | 08-security/policies-slc07.md | 0 |  |
| POL-ASM-PUBLISH | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ASM-RETURN | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ASM-SUBMIT | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-ASM-VERSIONS | 08-security/policies-slc07.md | 0 |  |
| POL-ASM-WITHDRAW | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-AST-AVAILABILITY | 08-security/policies-slc09.md | 0 |  |
| POL-AST-DISPOSE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-FAIL-MAINTENANCE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-GET | 08-security/policies-slc09.md | 0 |  |
| POL-AST-MARK-UNSERVICEABLE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-RECLASSIFY | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-RECOVER | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-REGISTER | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-REPORT-LOST | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-RETURN-TO-SERVICE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-SET-CERTIFICATION | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-START-MAINTENANCE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-TRANSFER-CUSTODY | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-AST-UPDATE-CONDITION | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-ATT-COMPLETE-UPLOAD | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-ATT-DOWNLOAD | 08-security/policies-slc02.md | 0 |  |
| POL-ATT-ERASE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-ATT-INITIATE-UPLOAD | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-AUD-SEARCH | 08-security/policies-slc01.md | 0 |  |
| POL-AUD-VERIFY | 08-security/policies-slc01.md | 0 |  |
| POL-AUT-APPROVE-GRANT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-AUT-CHECK | 08-security/policies-slc01.md | 0 |  |
| POL-AUT-DELEGATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-AUT-GRANT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-AUT-LIST | 08-security/policies-slc01.md | 0 |  |
| POL-AUT-REJECT-GRANT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-AUT-RESUME | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-AUT-REVOKE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-AUT-SUSPEND | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-BASE-TILE | 08-security/policies-slc06.md | 0 |  |
| POL-CAP-CANCEL | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC03/commands-slc16.md; 05-contracts/openapi-intelligence-slc16.md |
| POL-CAP-LIST | 08-security/policies-slc16.md | 0 |  |
| POL-CAP-PREPARE | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC03/commands-slc16.md; 05-contracts/openapi-intelligence-slc16.md |
| POL-CAP-RELEASE | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC03/commands-slc16.md; 05-contracts/openapi-intelligence-slc16.md |
| POL-CAP-RETRY | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC03/commands-slc16.md; 05-contracts/openapi-intelligence-slc16.md |
| POL-CLM-ASSERT | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-CLM-ASSESS | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-CLM-CORRECT | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-CLM-GET | 08-security/policies-slc02.md | 0 |  |
| POL-CLM-RECLASSIFY | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-CLM-RECORD-CHANGE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-CLM-RETRACT | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-CLR-APPROVE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-CLR-GET | 08-security/policies-slc01.md | 0 |  |
| POL-CLR-GRANT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-CLR-MODIFY | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-CLR-REINSTATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-CLR-REVOKE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-CLR-SUSPEND | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-CLS-ACTIVATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-CLS-ACTIVE | 08-security/policies-slc01.md | 0 |  |
| POL-CLS-DISCARD | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-CLS-DRAFT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-CLS-EDIT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-CLUSTER-GET | 08-security/policies-slc04.md | 0 |  |
| POL-CNF-ACCEPT | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-CNF-ASSIGN | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-CNF-GET | 08-security/policies-slc04.md | 0 |  |
| POL-CNF-LIST | 08-security/policies-slc04.md | 0 |  |
| POL-CNF-RAISE | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-CNF-REOPEN | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-CNF-RESOLVE | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-CNF-START-REVIEW | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-CON-ACTIVATE | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-CON-FAIL-TEST | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-CON-LIST | 08-security/policies-slc16.md | 0 |  |
| POL-CON-REGISTER | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-CON-RESUME | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-CON-RETIRE | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-CON-SUSPEND | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-CON-TEST | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-CPL-ACTIVATE | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CPL-ADD-ACTIVITY | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CPL-CANCEL | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CPL-COMPLETE | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CPL-CREATE | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CPL-GET | 08-security/policies-slc14.md | 0 |  |
| POL-CPL-REMOVE-ACTIVITY | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CRD-ACTIVATE | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC04/commands-slc15.md; 05-contracts/openapi-operations-slc15.md |
| POL-CRD-ADD-PARTICIPANT | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC04/commands-slc15.md; 05-contracts/openapi-operations-slc15.md |
| POL-CRD-ASSIGN-RESPONSIBILITY | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC04/commands-slc15.md; 05-contracts/openapi-operations-slc15.md |
| POL-CRD-CANCEL | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC04/commands-slc15.md; 05-contracts/openapi-operations-slc15.md |
| POL-CRD-CLOSE | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC04/commands-slc15.md; 05-contracts/openapi-operations-slc15.md |
| POL-CRD-GET | 08-security/policies-slc15.md | 0 |  |
| POL-CRD-LIST | 08-security/policies-slc15.md | 0 |  |
| POL-CRD-OPEN | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC04/commands-slc15.md; 05-contracts/openapi-operations-slc15.md |
| POL-CRD-REMOVE-PARTICIPANT | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC04/commands-slc15.md; 05-contracts/openapi-operations-slc15.md |
| POL-CRD-REQUEST-DECISION | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC04/commands-slc15.md; 05-contracts/openapi-operations-slc15.md |
| POL-CRD-UPDATE-RESPONSIBILITY | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC04/commands-slc15.md; 05-contracts/openapi-operations-slc15.md |
| POL-CRP-ACCEPT | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC02/commands-slc15.md; 05-contracts/openapi-information-slc15.md |
| POL-CRP-GET | 08-security/policies-slc15.md | 0 |  |
| POL-CRP-PROPOSE | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC02/commands-slc15.md; 05-contracts/openapi-information-slc15.md |
| POL-CRP-QUEUE | 08-security/policies-slc15.md | 0 |  |
| POL-CRP-REJECT | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC02/commands-slc15.md; 05-contracts/openapi-information-slc15.md |
| POL-CRP-START-REVIEW | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC02/commands-slc15.md; 05-contracts/openapi-information-slc15.md |
| POL-CRQ-AMEND | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CRQ-APPROVE | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CRQ-BOARD | 08-security/policies-slc14.md | 0 |  |
| POL-CRQ-CANCEL | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CRQ-DRAFT | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CRQ-EDIT | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CRQ-EVIDENCE | 08-security/policies-slc14.md | 0 |  |
| POL-CRQ-GET | 08-security/policies-slc14.md | 0 |  |
| POL-CRQ-MARK-SATISFIED | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CRQ-REJECT | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CRQ-SUBMIT | 08-security/policies-slc14.md | 2 | 03-domain/contexts/BC02/commands-slc14.md; 05-contracts/openapi-information-slc14.md |
| POL-CRR-ACTIVATE | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC02/commands-slc15.md; 05-contracts/openapi-information-slc15.md |
| POL-CRR-DEFINE | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC02/commands-slc15.md; 05-contracts/openapi-information-slc15.md |
| POL-CRR-EDIT | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC02/commands-slc15.md; 05-contracts/openapi-information-slc15.md |
| POL-CRR-RETIRE | 08-security/policies-slc15.md | 2 | 03-domain/contexts/BC02/commands-slc15.md; 05-contracts/openapi-information-slc15.md |
| POL-DEC-ANNUL | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-DEC-BASIS | 08-security/policies-slc08.md | 0 |  |
| POL-DEC-GET | 08-security/policies-slc08.md | 0 |  |
| POL-DEC-RECORD | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-DEV-CONFIRM | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC01/commands-slc11.md; 05-contracts/openapi-foundation-slc11.md |
| POL-DEV-ENROLL | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC01/commands-slc11.md; 05-contracts/openapi-foundation-slc11.md |
| POL-DEV-LIST | 08-security/policies-slc11.md | 0 |  |
| POL-DEV-REINSTATE | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC01/commands-slc11.md; 05-contracts/openapi-foundation-slc11.md |
| POL-DEV-REPORT-LOST | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC01/commands-slc11.md; 05-contracts/openapi-foundation-slc11.md |
| POL-DEV-RETIRE | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC01/commands-slc11.md; 05-contracts/openapi-foundation-slc11.md |
| POL-DEV-ROTATE-KEY | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC01/commands-slc11.md; 05-contracts/openapi-foundation-slc11.md |
| POL-DEV-SUSPEND | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC01/commands-slc11.md; 05-contracts/openapi-foundation-slc11.md |
| POL-DRQ-ADD-OPTION | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-DRQ-CITE | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-DRQ-CREATE | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-DRQ-GET | 08-security/policies-slc08.md | 0 |  |
| POL-DRQ-LIST | 08-security/policies-slc08.md | 0 |  |
| POL-DRQ-OPEN | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-DRQ-WITHDRAW | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-DSP-APPROVE | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-DSP-CANCEL | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-DSP-GET | 08-security/policies-slc12a.md | 0 |  |
| POL-DSP-SUBMIT | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-DST-CANCEL | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-DST-DISTRIBUTE | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-DST-LOG | 08-security/policies-slc12.md | 0 |  |
| POL-ELIG-CHECK | 08-security/policies-slc03.md | 0 |  |
| POL-ENT-CHANGE-TYPE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-ENT-CLAIMS | 08-security/policies-slc02.md | 0 |  |
| POL-ENT-LIST | 08-security/policies-slc02.md | 0 |  |
| POL-ENT-POSITIONS | 08-security/policies-slc02.md | 0 |  |
| POL-ENT-RECLASSIFY | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-ENT-REGISTER | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-ENT-REINSTATE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-ENT-RESOLVED | 08-security/policies-slc02.md | 0 |  |
| POL-ENT-RETIRE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-ER-CONFIRM-MATCH | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-ER-DECIDE-MATCH | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-ER-DECIDE-NOT-MATCH | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-ER-GET | 08-security/policies-slc04.md | 0 |  |
| POL-ER-PARK | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-ER-PROPOSE | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-ER-QUEUE | 08-security/policies-slc04.md | 0 |  |
| POL-ER-REQUEST-SPLIT | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-ER-RESUME | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-ERS-APPROVE | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-ERS-GET | 08-security/policies-slc12a.md | 0 |  |
| POL-ER-SPLIT | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-ERS-REGISTER | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-ERS-REJECT | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-ER-START-REVIEW | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-ER-WITHDRAW | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-EVD-GET | 08-security/policies-slc02.md | 0 |  |
| POL-EVD-RECLASSIFY | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-EVD-REGISTER | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-EVD-SEAL | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-EVD-TRANSFER-CUSTODY | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-EVD-UPDATE-LOCATOR | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-EVD-WITHDRAW | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-EVL-LINK | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-EVL-UNLINK | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-EVS-ACTIVATE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-EVS-DRAFT | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-EVS-EDIT | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-EXC-APPROVE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-EXC-LIST | 08-security/policies-slc01.md | 0 |  |
| POL-EXC-REJECT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-EXC-REQUEST | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-EXC-REVOKE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-EXPORT-BULK | 08-security/authorization-model.md | 1 | 02-requirements/requirements.md |
| POL-EXR-CANCEL | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-EXR-GET | 08-security/policies-slc19.md | 0 |  |
| POL-EXR-LIST | 08-security/policies-slc19.md | 0 |  |
| POL-EXR-PLAN | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-EXR-SCHEDULE | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-EXR-START | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-EXT-END | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-EXT-MAP | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-EXT-RESOLVE | 08-security/policies-slc02.md | 0 |  |
| POL-FND-ACCEPT | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-FND-EDIT | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-FND-LIST | 08-security/policies-slc07.md | 0 |  |
| POL-FND-RECORD | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-FND-WITHDRAW | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-GRAPH-NEIGHBORHOOD | 08-security/policies-slc05.md | 0 |  |
| POL-GRAPH-PATHS | 08-security/policies-slc05.md | 0 |  |
| POL-HRS-APPROVE | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC01/commands-slc16.md; 05-contracts/openapi-foundation-slc16.md |
| POL-HRS-QUEUE | 08-security/policies-slc16.md | 0 |  |
| POL-HRS-REJECT | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC01/commands-slc16.md; 05-contracts/openapi-foundation-slc16.md |
| POL-IMP-ACCEPT-QUARANTINE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-IMP-CANCEL | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-IMP-GET | 08-security/policies-slc02.md | 0 |  |
| POL-IMP-REPROCESS-QUARANTINE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-IMP-SUBMIT | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-INC-ACTIVATE-CONTINGENCY | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-INC-ASSESS | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-INC-CANCEL | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-INC-CLOSE | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-INC-CONTAIN | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-INC-DE-ESCALATE | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-INC-DISPATCH-RESPONSE | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-INC-ESCALATE | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-INC-GET | 08-security/policies-slc17.md | 0 |  |
| POL-INC-LIST | 08-security/policies-slc17.md | 0 |  |
| POL-INC-RECOVERY-STATUS | 08-security/policies-slc17.md | 0 |  |
| POL-INC-REPORT | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-INC-RESOLVE | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-KNO-DISCARD | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-KNO-DRAFT | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-KNO-EDIT | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-KNO-PUBLISH | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-KNO-RECORD-REUSE | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-KNO-REJECT | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-KNO-RETIRE | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-KNO-RETURN | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-KNO-SEARCH | 08-security/policies-slc12.md | 0 |  |
| POL-KNO-SUBMIT | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-KNO-SUGGEST | 08-security/policies-slc12.md | 0 |  |
| POL-LABEL-CHECK | 08-security/policies-slc05.md | 0 |  |
| POL-LGR-CANCEL | 08-security/policies-slc18.md | 2 | 03-domain/contexts/BC05/commands-slc18.md; 05-contracts/openapi-readiness-slc18.md |
| POL-LGR-DISPATCH | 08-security/policies-slc18.md | 2 | 03-domain/contexts/BC05/commands-slc18.md; 05-contracts/openapi-readiness-slc18.md |
| POL-LGR-GET | 08-security/policies-slc18.md | 0 |  |
| POL-LGR-LIST | 08-security/policies-slc18.md | 0 |  |
| POL-LGR-REQUEST | 08-security/policies-slc18.md | 2 | 03-domain/contexts/BC05/commands-slc18.md; 05-contracts/openapi-readiness-slc18.md |
| POL-LHD-APPROVE-RELEASE | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-LHD-CANCEL-RELEASE | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-LHD-CHECK | 08-security/policies-slc12a.md | 0 |  |
| POL-LHD-EXTEND | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-LHD-LIST | 08-security/policies-slc12a.md | 0 |  |
| POL-LHD-PLACE | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-LHD-REQUEST-RELEASE | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-LIN-TRACE | 08-security/policies-slc02.md | 0 |  |
| POL-MDL-APPROVE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-MDL-DEPRECATE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-MDL-FAIL-EVALUATION | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-MDL-LIST | 08-security/policies-slc10.md | 0 |  |
| POL-MDL-PROMOTE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-MDL-REGISTER | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-MDL-REINSTATE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-MDL-RETIRE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-MDL-STAGE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-MDL-START-EVALUATION | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-MNT-CANCEL | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-MNT-COMPLETE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-MNT-PLAN | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-MNT-RESCHEDULE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-MNT-SCHEDULE | 08-security/policies-slc09.md | 0 |  |
| POL-MNT-START | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-MRS-ACTIVATE | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-MRS-DRAFT | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-MRS-EDIT | 08-security/policies-slc04.md | 2 | 03-domain/contexts/BC02/commands-slc04.md; 05-contracts/openapi-information-slc04.md |
| POL-MRS-GET | 08-security/policies-slc04.md | 0 |  |
| POL-NTF-INBOX | 08-security/policies-slc06.md | 0 |  |
| POL-NTF-MARK-READ | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC04/commands-slc06.md; 05-contracts/openapi-operations-slc06.md |
| POL-OBS-AMEND | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-OBS-ATTACH-EVIDENCE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-OBS-GET | 08-security/policies-slc02.md | 0 |  |
| POL-OBS-LIST | 08-security/policies-slc02.md | 0 |  |
| POL-OBS-RECLASSIFY | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-OBS-RECORD | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-OBS-REJECT | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-OBS-VALIDATE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-OFFLINE-PRELOAD | 08-security/authorization-model.md | 4 | 03-domain/contexts/BC07/commands-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 08-security/policies-slc11.md; 13-verification/tooling/slice-sources.md |
| POL-ORG-ADD-UNIT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ORG-CREATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ORG-DEACTIVATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ORG-DEACTIVATE-UNIT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ORG-MOVE-UNIT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ORG-REACTIVATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ORG-RENAME | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ORG-RENAME-UNIT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ORG-TREE | 08-security/policies-slc01.md | 0 |  |
| POL-OUT-CORRECT | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-OUT-RECORD | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-OUT-SERIES | 08-security/policies-slc08.md | 0 |  |
| POL-PDP-DECIDE | 08-security/policies-slc01.md | 0 |  |
| POL-PER-DEACTIVATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-PER-ERASE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-PER-REACTIVATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-PER-REGISTER | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-PERSONAL-DATA | 08-security/authorization-model.md | 0 |  |
| POL-PER-UPDATE-DETAILS | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-PKG-CONFIRM-DOWNLOAD | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC07/commands-slc11.md; 05-contracts/openapi-field-slc11.md |
| POL-PKG-GET | 08-security/policies-slc11.md | 0 |  |
| POL-PKG-REQUEST | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC07/commands-slc11.md; 05-contracts/openapi-field-slc11.md |
| POL-PKG-REVOKE | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC07/commands-slc11.md; 05-contracts/openapi-field-slc11.md |
| POL-PLN-CANCEL | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLN-CLOSE | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLN-COMPLETE | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLN-CREATE | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLN-GET | 08-security/policies-slc08.md | 0 |  |
| POL-PLN-PROGRESS | 08-security/policies-slc08.md | 0 |  |
| POL-PLN-RECLASSIFY | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLN-RESUME | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLN-SUSPEND | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLV-AMEND-MINOR | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLV-APPROVE | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLV-DIFF | 08-security/policies-slc08.md | 0 |  |
| POL-PLV-DISCARD | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLV-DRAFT | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLV-EDIT | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLV-LIST | 08-security/policies-slc08.md | 0 |  |
| POL-PLV-REJECT | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLV-RETURN | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-PLV-SUBMIT | 08-security/policies-slc08.md | 2 | 03-domain/contexts/BC04/commands-slc08.md; 05-contracts/openapi-operations-slc08.md |
| POL-POL-APPROVE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-POL-DRAFT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-POL-EDIT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-POL-GET | 08-security/policies-slc01.md | 0 |  |
| POL-POL-REJECT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-POL-SUBMIT | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC08/commands-slc01.md; 05-contracts/openapi-governance-slc01.md |
| POL-POL-TIMELINE | 08-security/policies-slc09.md | 0 |  |
| POL-PRD-APPROVE | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PRD-CREATE | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PRD-DISCARD | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PRD-EDIT-NARRATIVE | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PRD-GENERATE | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PRD-GET | 08-security/policies-slc12.md | 0 |  |
| POL-PRD-LIST | 08-security/policies-slc12.md | 0 |  |
| POL-PRD-RETURN | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PRD-SUBMIT | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PRD-WITHDRAW | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PRJ-CANCEL-BUILD | 08-security/policies-slc05.md | 2 | 03-domain/contexts/BC07/commands-slc05.md; 05-contracts/openapi-discovery-slc05.md |
| POL-PRJ-CREATE-VERSION | 08-security/policies-slc05.md | 2 | 03-domain/contexts/BC07/commands-slc05.md; 05-contracts/openapi-discovery-slc05.md |
| POL-PRJ-PROMOTE | 08-security/policies-slc05.md | 2 | 03-domain/contexts/BC07/commands-slc05.md; 05-contracts/openapi-discovery-slc05.md |
| POL-PRJ-RETIRE | 08-security/policies-slc05.md | 2 | 03-domain/contexts/BC07/commands-slc05.md; 05-contracts/openapi-discovery-slc05.md |
| POL-PRJ-STATUS | 08-security/policies-slc05.md | 0 |  |
| POL-PTM-ACTIVATE | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PTM-DEFINE | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PTM-EDIT | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-PTM-RETIRE | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-QUAL-LIST | 08-security/policies-slc03.md | 0 |  |
| POL-QUAL-RECORD | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC05/commands-slc03.md; 05-contracts/openapi-readiness-slc03.md |
| POL-QUAL-REINSTATE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC05/commands-slc03.md; 05-contracts/openapi-readiness-slc03.md |
| POL-QUAL-RENEW | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC05/commands-slc03.md; 05-contracts/openapi-readiness-slc03.md |
| POL-QUAL-REVOKE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC05/commands-slc03.md; 05-contracts/openapi-readiness-slc03.md |
| POL-QUAL-SUSPEND | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC05/commands-slc03.md; 05-contracts/openapi-readiness-slc03.md |
| POL-RAS-ASSIGN | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-RAS-REVOKE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-READINESS | 08-security/policies-slc09.md | 0 |  |
| POL-REC-CANCEL | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-REC-REPORT | 08-security/policies-slc12.md | 0 |  |
| POL-REC-REQUEST | 08-security/policies-slc12.md | 2 | 03-domain/contexts/BC06/commands-slc12.md; 05-contracts/openapi-knowledge-slc12.md |
| POL-REL-LIST | 08-security/policies-slc02.md | 0 |  |
| POL-REL-RECLASSIFY | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-REL-REGISTER | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-REL-REINSTATE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-REL-RETIRE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-RIS-ASSESS | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-RIS-CLOSE | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-RIS-GET | 08-security/policies-slc17.md | 0 |  |
| POL-RIS-IDENTIFY | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-RIS-PLAN-TREATMENT | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-RIS-REASSESS | 08-security/policies-slc17.md | 2 | 03-domain/contexts/BC04/commands-slc17.md; 05-contracts/openapi-operations-slc17.md |
| POL-RIS-REGISTER | 08-security/policies-slc17.md | 0 |  |
| POL-ROL-ACTIVATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ROL-DEFINE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ROL-RETIRE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-ROL-SET-PERMISSIONS | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-RPL-ADJUST-CAPACITY | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RPL-CLOSE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RPL-CREATE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RPL-RESUME | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RPL-SUSPEND | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RRQ-ACTIVATE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RRQ-DEFINE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RRQ-EDIT | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RRQ-RETIRE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RSV-CANCEL | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RSV-CONFIRM | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RSV-HOLD | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RSV-RELEASE | 08-security/policies-slc09.md | 2 | 03-domain/contexts/BC05/commands-slc09.md; 05-contracts/openapi-readiness-slc09.md |
| POL-RTG-ACTIVATE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-RTG-ACTIVE | 08-security/policies-slc10.md | 0 |  |
| POL-RTG-DISCARD | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-RTG-DRAFT | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-RTG-EDIT | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-RTS-ACTIVATE | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-RTS-ACTIVE | 08-security/policies-slc12a.md | 0 |  |
| POL-RTS-DISCARD | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-RTS-DRAFT | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-RTS-EDIT | 08-security/policies-slc12a.md | 2 | 03-domain/contexts/BC08/commands-slc12a.md; 05-contracts/openapi-governance-slc12a.md |
| POL-RUN-ARTIFACT | 08-security/policies-slc07.md | 0 |  |
| POL-RUN-CANCEL | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-RUN-GET | 08-security/policies-slc07.md | 0 |  |
| POL-RUN-REPRODUCE | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-RUN-SUBMIT | 08-security/policies-slc07.md | 2 | 03-domain/contexts/BC03/commands-slc07.md; 05-contracts/openapi-intelligence-slc07.md |
| POL-RWE-CHANGE-TYPE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-RWE-GET | 08-security/policies-slc02.md | 0 |  |
| POL-RWE-RECLASSIFY | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-RWE-REGISTER | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-RWE-REINSTATE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-RWE-RETIRE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-SCF-ASSIGN | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC07/commands-slc11.md; 05-contracts/openapi-field-slc11.md |
| POL-SCF-DISCARD | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC07/commands-slc11.md; 05-contracts/openapi-field-slc11.md |
| POL-SCF-GET | 08-security/policies-slc11.md | 0 |  |
| POL-SCF-LIST | 08-security/policies-slc11.md | 0 |  |
| POL-SCF-REAPPLY | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC07/commands-slc11.md; 05-contracts/openapi-field-slc11.md |
| POL-SCF-RESOLVE-MANUALLY | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC07/commands-slc11.md; 05-contracts/openapi-field-slc11.md |
| POL-SCN-ACTIVATE | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SCN-COMPARE | 08-security/policies-slc07.md | 0 |  |
| POL-SCN-DEFINE | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SCN-EDIT | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SCN-GET | 08-security/policies-slc19.md | 0 |  |
| POL-SCN-LIST | 08-security/policies-slc19.md | 0 |  |
| POL-SCN-RETIRE | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SEC-CONTEXT | 08-security/policies-slc01.md | 0 |  |
| POL-SHP-CANCEL | 08-security/policies-slc18.md | 2 | 03-domain/contexts/BC05/commands-slc18.md; 05-contracts/openapi-readiness-slc18.md |
| POL-SHP-DELIVER | 08-security/policies-slc18.md | 2 | 03-domain/contexts/BC05/commands-slc18.md; 05-contracts/openapi-readiness-slc18.md |
| POL-SHP-DEPART | 08-security/policies-slc18.md | 2 | 03-domain/contexts/BC05/commands-slc18.md; 05-contracts/openapi-readiness-slc18.md |
| POL-SHP-GET | 08-security/policies-slc18.md | 0 |  |
| POL-SHP-LIST | 08-security/policies-slc18.md | 0 |  |
| POL-SHP-PLAN | 08-security/policies-slc18.md | 2 | 03-domain/contexts/BC05/commands-slc18.md; 05-contracts/openapi-readiness-slc18.md |
| POL-SHP-RECORD-CHECKPOINT | 08-security/policies-slc18.md | 2 | 03-domain/contexts/BC05/commands-slc18.md; 05-contracts/openapi-readiness-slc18.md |
| POL-SHP-REPORT-DAMAGE | 08-security/policies-slc18.md | 2 | 03-domain/contexts/BC05/commands-slc18.md; 05-contracts/openapi-readiness-slc18.md |
| POL-SHP-REPORT-LOST | 08-security/policies-slc18.md | 2 | 03-domain/contexts/BC05/commands-slc18.md; 05-contracts/openapi-readiness-slc18.md |
| POL-SHP-TRACKING | 08-security/policies-slc18.md | 0 |  |
| POL-SIM-ABORT | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SIM-COMPLETE | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SIM-DELIVER-INJECT | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SIM-GET | 08-security/policies-slc19.md | 0 |  |
| POL-SIM-LIST | 08-security/policies-slc19.md | 0 |  |
| POL-SIM-PAUSE | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SIM-RECORD-EVALUATION | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SIM-RESUME | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SIM-START | 08-security/policies-slc19.md | 2 | 03-domain/contexts/BC05/commands-slc19.md; 05-contracts/openapi-readiness-slc19.md |
| POL-SIM-TIMELINE | 08-security/policies-slc19.md | 0 |  |
| POL-SIT-ACTIVATE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-SIT-CHANGES | 08-security/policies-slc06.md | 0 |  |
| POL-SIT-CLOSE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-SIT-COP | 08-security/policies-slc06.md | 0 |  |
| POL-SIT-CREATE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-SIT-EDIT-DEFINITION | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-SIT-GET | 08-security/policies-slc06.md | 0 |  |
| POL-SIT-LIST | 08-security/policies-slc06.md | 0 |  |
| POL-SIT-PAUSE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-SIT-RECLASSIFY | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-SIT-RESUME | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC03/commands-slc06.md; 05-contracts/openapi-intelligence-slc06.md |
| POL-SIT-TILE | 08-security/policies-slc06.md | 0 |  |
| POL-SNS-ACTIVATE | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-SNS-LIST | 08-security/policies-slc16.md | 0 |  |
| POL-SNS-PAUSE | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-SNS-REGISTER | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-SNS-RETIRE | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-SNS-SET-QUALITY-RULES | 08-security/policies-slc16.md | 2 | 03-domain/contexts/BC07/commands-slc16.md; 05-contracts/openapi-integration-slc16.md |
| POL-SRC-GET | 08-security/policies-slc02.md | 0 |  |
| POL-SRCH-QUERY | 08-security/policies-slc05.md | 0 |  |
| POL-SRCH-SUGGEST | 08-security/policies-slc05.md | 0 |  |
| POL-SRC-RATE-RELIABILITY | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-SRC-RECLASSIFY | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-SRC-REGISTER | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-SRC-REINSTATE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-SRC-RETIRE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-SRC-SET-PROTECTION | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-SRC-SUSPEND | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-SRC-UPDATE-PROFILE | 08-security/policies-slc02.md | 2 | 03-domain/contexts/BC02/commands-slc02.md; 05-contracts/openapi-information-slc02.md |
| POL-SUB-PAUSE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC04/commands-slc06.md; 05-contracts/openapi-operations-slc06.md |
| POL-SUB-RESUME | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC04/commands-slc06.md; 05-contracts/openapi-operations-slc06.md |
| POL-SUB-SUBSCRIBE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC04/commands-slc06.md; 05-contracts/openapi-operations-slc06.md |
| POL-SUB-UNSUBSCRIBE | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC04/commands-slc06.md; 05-contracts/openapi-operations-slc06.md |
| POL-SUB-UPDATE-CHANNELS | 08-security/policies-slc06.md | 2 | 03-domain/contexts/BC04/commands-slc06.md; 05-contracts/openapi-operations-slc06.md |
| POL-SVC-CLOSE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-SVC-CREATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-SVC-DISABLE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-SVC-ENABLE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-SVC-ROTATE-CREDENTIAL | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-SYN-DELTA | 08-security/policies-slc11.md | 0 |  |
| POL-SYN-OPEN | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC07/commands-slc11.md; 05-contracts/openapi-field-slc11.md |
| POL-SYN-UPLOAD-BATCH | 08-security/policies-slc11.md | 2 | 03-domain/contexts/BC07/commands-slc11.md; 05-contracts/openapi-field-slc11.md |
| POL-TASK-ACCEPT | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-ADD-RESULT-ITEM | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-APPROVE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-APPROVE-SOD | 08-security/authorization-model.md | 0 |  |
| POL-TASK-ASSIGN | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-BLOCK | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-CANCEL | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-CLOSE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-COMPLETE | 08-security/authorization-model.md;08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-CREATE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-DECLINE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-EDIT | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-ESCALATE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-GET | 08-security/policies-slc03.md | 0 |  |
| POL-TASK-HISTORY | 08-security/policies-slc03.md | 0 |  |
| POL-TASK-LIST | 08-security/policies-slc03.md | 0 |  |
| POL-TASK-MARK-READY | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-REASSIGN | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-RECLASSIFY | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-REJECT | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-RESUME | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-RETURN | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-SET-DUE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-START | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-START-REVIEW | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-SUBMIT | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-SUSPEND | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TASK-UNSUSPEND | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TEN-COMPLETE-CELL-MIGRATION | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md |
| POL-TEN-COMPLETE-DECOMMISSION | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md |
| POL-TEN-COMPLETE-PROVISIONING | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md |
| POL-TEN-FAIL-PROVISIONING | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md |
| POL-TEN-GET | 08-security/policies-slc01.md | 0 |  |
| POL-TEN-PROVISION | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-TEN-REACTIVATE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-TEN-RETRY-PROVISIONING | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-TEN-START-CELL-MIGRATION | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-TEN-START-DECOMMISSION | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-TEN-SUSPEND | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-TEN-UPDATE-QUOTAS | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-TOL-ACTIVATE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-TOL-DISABLE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-TOL-ENABLE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-TOL-LIST | 08-security/policies-slc10.md | 0 |  |
| POL-TOL-REGISTER | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-TOL-RETIRE | 08-security/policies-slc10.md | 2 | 03-domain/contexts/BC07/commands-slc10.md; 05-contracts/openapi-ai-slc10.md |
| POL-TTY-ACTIVATE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TTY-DEFINE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TTY-EDIT | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-TTY-GET | 08-security/policies-slc03.md | 0 |  |
| POL-TTY-RETIRE | 08-security/policies-slc03.md | 2 | 03-domain/contexts/BC04/commands-slc03.md; 05-contracts/openapi-operations-slc03.md |
| POL-USR-CLOSE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-USR-DISABLE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-USR-ENABLE | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-USR-GET | 08-security/policies-slc01.md | 0 |  |
| POL-USR-LINK-IDENTITY | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-USR-LINK-PERSON | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-USR-LIST | 08-security/policies-slc01.md | 0 |  |
| POL-USR-LOCK | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-USR-PROVISION | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-USR-RECORD-FIRST-SIGN-IN | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-internal-slc01.md |
| POL-USR-UNLINK-IDENTITY | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |
| POL-USR-UNLOCK | 08-security/policies-slc01.md | 2 | 03-domain/contexts/BC01/commands-slc01.md; 05-contracts/openapi-foundation-slc01.md |

### Family: POLICIES

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| POLICIES-SLC01 | 08-security/policies-slc01.md | 1 | 00-governance/glossary.md |
| POLICIES-SLC02 | 08-security/policies-slc02.md | 0 |  |
| POLICIES-SLC03 | 08-security/policies-slc03.md | 0 |  |
| POLICIES-SLC04 | 08-security/policies-slc04.md | 0 |  |
| POLICIES-SLC05 | 08-security/policies-slc05.md | 0 |  |
| POLICIES-SLC06 | 08-security/policies-slc06.md | 0 |  |
| POLICIES-SLC07 | 08-security/policies-slc07.md | 0 |  |
| POLICIES-SLC08 | 08-security/policies-slc08.md | 0 |  |
| POLICIES-SLC09 | 08-security/policies-slc09.md | 0 |  |
| POLICIES-SLC10 | 08-security/policies-slc10.md | 0 |  |
| POLICIES-SLC11 | 08-security/policies-slc11.md | 0 |  |
| POLICIES-SLC12 | 08-security/policies-slc12.md | 0 |  |
| POLICIES-SLC12A | 08-security/policies-slc12a.md | 0 |  |
| POLICIES-SLC14 | 08-security/policies-slc14.md | 0 |  |
| POLICIES-SLC15 | 08-security/policies-slc15.md | 0 |  |
| POLICIES-SLC16 | 08-security/policies-slc16.md | 0 |  |
| POLICIES-SLC17 | 08-security/policies-slc17.md | 0 |  |
| POLICIES-SLC18 | 08-security/policies-slc18.md | 0 |  |
| POLICIES-SLC19 | 08-security/policies-slc19.md | 0 |  |

### Family: PRIVACY

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| PRIVACY-THREATS | 08-security/privacy-threats.md | 0 |  |

### Family: PROP

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| PROP-SLC01 | 13-verification/invariant-properties-slc01.md | 0 |  |
| PROP-SLC02 | 13-verification/invariant-properties-slc02.md | 0 |  |
| PROP-SLC03 | 13-verification/invariant-properties-slc03.md | 0 |  |
| PROP-SLC04 | 13-verification/invariant-properties-slc04.md | 0 |  |
| PROP-SLC05 | 13-verification/invariant-properties-slc05.md | 1 | 00-governance/glossary.md |
| PROP-SLC06 | 13-verification/invariant-properties-slc06.md | 0 |  |
| PROP-SLC07 | 13-verification/invariant-properties-slc07.md | 0 |  |
| PROP-SLC08 | 13-verification/invariant-properties-slc08.md | 0 |  |
| PROP-SLC09 | 13-verification/invariant-properties-slc09.md | 0 |  |
| PROP-SLC10 | 13-verification/invariant-properties-slc10.md | 0 |  |
| PROP-SLC11 | 13-verification/invariant-properties-slc11.md | 0 |  |
| PROP-SLC12 | 13-verification/invariant-properties-slc12.md | 0 |  |
| PROP-SLC12A | 13-verification/invariant-properties-slc12a.md | 0 |  |
| PROP-SLC14 | 13-verification/invariant-properties-slc14.md | 0 |  |
| PROP-SLC15 | 13-verification/invariant-properties-slc15.md | 0 |  |
| PROP-SLC16 | 13-verification/invariant-properties-slc16.md | 0 |  |
| PROP-SLC17 | 13-verification/invariant-properties-slc17.md | 0 |  |
| PROP-SLC18 | 13-verification/invariant-properties-slc18.md | 0 |  |
| PROP-SLC19 | 13-verification/invariant-properties-slc19.md | 0 |  |

### Family: PRV

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| PRV-01 | 08-security/privacy-threats.md | 0 |  |
| PRV-02 | 08-security/privacy-threats.md | 0 |  |
| PRV-03 | 08-security/privacy-threats.md | 0 |  |
| PRV-04 | 08-security/privacy-threats.md | 0 |  |
| PRV-05 | 08-security/privacy-threats.md | 0 |  |
| PRV-06 | 08-security/privacy-threats.md | 0 |  |
| PRV-07 | 08-security/privacy-threats.md | 0 |  |

### Family: QAS

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| QAS-ACC-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 00-governance/registers/unknowns.md; 02-requirements/requirements.md; 12-solution/ui-architecture.md |
| QAS-AI-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 5 | 01-business/release-2-scope.md; 02-requirements/requirements.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 13-verification/acceptance/SLC-10/invariants-slc10.md; 16-reports/ARCHITECTURE-REVIEW-R2.m ...(truncated) |
| QAS-AI-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 02-requirements/requirements.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 13-verification/acceptance/SLC-10/invariants-slc10.md |
| QAS-AI-003 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 5 | 02-requirements/requirements.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 07-quality/workloads-slc10.md; 12-solution/technology-decisions.md; 13-verification/acceptance/SLC-10/invariants-slc10.md |
| QAS-AI-004 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 02-requirements/requirements.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 13-verification/acceptance/SLC-10/invariants-slc10.md |
| QAS-AI-005 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 03-domain/contexts/BC07/grounded-ai-spec.md; 13-verification/acceptance/SLC-10/invariants-slc10.md |
| QAS-ARC-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 4 | 02-requirements/requirements.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 07-quality/workloads-slc12.md; 13-verification/acceptance/SLC-12/invariants-slc12.md |
| QAS-ARC-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 02-requirements/requirements.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 13-verification/acceptance/SLC-12/invariants-slc12.md |
| QAS-ARC-003 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 13-verification/acceptance/SLC-12/invariants-slc12.md |
| QAS-AUD-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md;15-traceability/trace-slc01.md | 3 | 02-requirements/requirements.md; 08-security/audit-architecture.md; 13-verification/acceptance/SLC-01/invariants-slc01.md |
| QAS-AVL-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 02-requirements/requirements.md; 09-reliability/dr-and-continuity.md |
| QAS-AVL-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 02-requirements/requirements.md; 09-reliability/dr-and-continuity.md |
| QAS-AVL-003 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 02-requirements/requirements.md; 09-reliability/dr-and-continuity.md |
| QAS-CAT | 02-requirements/quality-scenarios.md | 0 |  |
| QAS-CNF-001 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc04.md;15-traceability/quality-verification-matrix.md | 2 | 03-domain/contexts/BC02/conflict-detection-engine.md; 13-verification/acceptance/SLC-04/invariants-slc04.md |
| QAS-COL-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 4 | 03-domain/contexts/BC02/collection-spec.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 13-verification/acceptance/SLC-14/invariants-slc14.md; 13-verification/tooling/slice-sourc ...(truncated) |
| QAS-COST-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 02-requirements/requirements.md; 07-quality/cost-model.md |
| QAS-DQ-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 02-requirements/requirements.md; 07-quality/workloads.md; 13-verification/acceptance/SLC-02/invariants-slc02.md |
| QAS-ER-001 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc04.md;15-traceability/quality-verification-matrix.md | 6 | 03-domain/contexts/BC02/candidate-generation.md; 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md; 13-verification/acceptance/SLC-04/invariants-slc04. ...(truncated) |
| QAS-ER-002 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc04.md;15-traceability/quality-verification-matrix.md | 5 | 03-domain/contexts/BC02/candidate-generation.md; 03-domain/contexts/BC02/commands-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md; 13-verification/acceptance/SLC-04/invariants-slc04. ...(truncated) |
| QAS-ER-003 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc04.md;15-traceability/quality-verification-matrix.md | 1 | 03-domain/contexts/BC02/candidate-generation.md |
| QAS-EVO-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 02-requirements/requirements.md; 12-solution/release-configuration-migration.md; 16-reports/ENGINEERING-BASELINE-R1.md |
| QAS-GOV-001 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc12a.md;15-traceability/quality-verification-matrix.md | 1 | 13-verification/acceptance/SLC-12a/invariants-slc12a.md |
| QAS-INT-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 5 | 03-domain/contexts/BC07/enterprise-integration-spec.md; 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md; 07-quality/workloads-slc16.md; 13-verification/acceptance/SLC-16/invariants-sl ...(truncated) |
| QAS-KNW-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 13-verification/acceptance/SLC-12/invariants-slc12.md |
| QAS-LOG-001 | 02-requirements/quality-scenarios.md | 1 | 13-verification/acceptance/SLC-18/invariants-slc18.md |
| QAS-LOG-002 | 02-requirements/quality-scenarios.md | 1 | 13-verification/acceptance/SLC-18/invariants-slc18.md |
| QAS-OBS-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 4 | 02-requirements/requirements.md; 12-solution/technology-decisions.md; 15-traceability/rtm-r1.md; 15-traceability/trace-platform.md |
| QAS-OFF-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 6 | 00-governance/decisions/ADR-P09.md; 02-requirements/requirements.md; 03-domain/contexts/BC07/field-sync-protocol.md; 07-quality/workloads-slc11.md; 07-quality/workloads.md; 13-verification/acceptance/ ...(truncated) |
| QAS-OFF-002 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc11.md;15-traceability/quality-verification-matrix.md | 1 | 13-verification/acceptance/SLC-11/invariants-slc11.md |
| QAS-OFF-003 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc11.md;15-traceability/quality-verification-matrix.md | 3 | 07-quality/performance-test-strategy.md; 12-solution/deployment-units.md; 13-verification/acceptance/SLC-11/invariants-slc11.md |
| QAS-OPS-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 02-requirements/requirements.md; 12-solution/release-configuration-migration.md; 12-solution/technology-decisions.md |
| QAS-OPS-002 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc03.md;15-traceability/quality-verification-matrix.md | 2 | 03-domain/contexts/BC04/task-lifecycle-rules.md; 13-verification/acceptance/SLC-03/invariants-slc03.md |
| QAS-OPS-003 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc06.md;15-traceability/quality-verification-matrix.md | 1 | 13-verification/acceptance/SLC-06/invariants-slc06.md |
| QAS-PERF-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 11 | 00-governance/registers/risks.md; 02-requirements/requirements.md; 03-domain/contexts/BC02/claims-temporal-kernel.md; 07-quality/performance-test-strategy.md; 07-quality/workloads-slc01.md; 07-quality ...(truncated) |
| QAS-PERF-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 6 | 04-information/temporal-model.md; 07-quality/performance-test-strategy.md; 07-quality/workloads-slc02.md; 07-quality/workloads-slc07.md; 07-quality/workloads-slc08.md; 07-quality/workloads.md |
| QAS-PERF-003 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 7 | 02-requirements/requirements.md; 03-domain/contexts/BC07/discovery-architecture.md; 07-quality/performance-test-strategy.md; 07-quality/workloads-slc05.md; 07-quality/workloads.md; 12-solution/technol ...(truncated) |
| QAS-PERF-004 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 4 | 03-domain/contexts/BC07/discovery-architecture.md; 07-quality/workloads-slc05.md; 07-quality/workloads.md; 13-verification/acceptance/SLC-05/invariants-slc05.md |
| QAS-PERF-005 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 6 | 02-requirements/requirements.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 07-quality/performance-test-strategy.md; 07-quality/workloads-slc06.md; 07-quality/workloads.md; 13-verification/ac ...(truncated) |
| QAS-PERF-006 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 7 | 00-governance/decisions/ADR-P07.md; 02-requirements/requirements.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 07-quality/workloads-slc06.md; 07-quality/workloads.md; 13-verification/accepta ...(truncated) |
| QAS-PERF-007 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 7 | 00-governance/decisions/ADR-P12.md; 02-requirements/requirements.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 07-quality/performance-test-strategy.md; 07-quality/workloads-slc06.md; 07-qual ...(truncated) |
| QAS-PERF-008 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 1 | 07-quality/workloads.md |
| QAS-PERF-009 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc01.md;15-traceability/quality-verification-matrix.md;15-traceability/trace-slc01.md | 4 | 07-quality/performance-test-strategy.md; 12-solution/technology-decisions.md; 12-solution/w8-inputs.md; 14-slices/SLC-01/atam-lite.md |
| QAS-PERF-010 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc01.md;15-traceability/quality-verification-matrix.md;15-traceability/trace-slc01.md | 1 | 03-domain/contexts/BC01/security-context.md |
| QAS-PERF-011 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc01.md;15-traceability/quality-verification-matrix.md;15-traceability/trace-slc01.md | 1 | 08-security/audit-architecture.md |
| QAS-PERF-012 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc02.md;15-traceability/quality-verification-matrix.md | 8 | 02-requirements/requirements.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 07-quality/performance-test-strategy.md; 07-quality/work ...(truncated) |
| QAS-PERF-013 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc02.md;15-traceability/quality-verification-matrix.md | 3 | 03-domain/contexts/BC02/claims-temporal-kernel.md; 07-quality/performance-test-strategy.md; 14-slices/SLC-02/atam-lite.md |
| QAS-PERF-014 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc02.md;15-traceability/quality-verification-matrix.md | 0 |  |
| QAS-PERF-015 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc04.md;15-traceability/quality-verification-matrix.md | 3 | 03-domain/contexts/BC02/claims-temporal-kernel.md; 13-verification/acceptance/SLC-04/invariants-slc04.md; 14-slices/SLC-04/atam-lite.md |
| QAS-PERF-016 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc03.md;15-traceability/quality-verification-matrix.md | 1 | 13-verification/acceptance/SLC-03/invariants-slc03.md |
| QAS-PERF-017 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc03.md;15-traceability/quality-verification-matrix.md | 0 |  |
| QAS-PERF-018 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc05.md;15-traceability/quality-verification-matrix.md | 3 | 03-domain/contexts/BC07/discovery-architecture.md; 12-solution/technology-decisions.md; 12-solution/w8-inputs.md |
| QAS-PERF-019 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc06.md;15-traceability/quality-verification-matrix.md | 1 | 07-quality/performance-test-strategy.md |
| QAS-PERF-020 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc07.md;15-traceability/quality-verification-matrix.md | 2 | 12-solution/technology-decisions.md; 13-verification/acceptance/SLC-07/invariants-slc07.md |
| QAS-PERF-021 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc08.md;15-traceability/quality-verification-matrix.md | 1 | 13-verification/acceptance/SLC-08/invariants-slc08.md |
| QAS-PRD-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 07-quality/workloads-slc12.md; 13-verification/acceptance/SLC-12/invariants-slc12.md |
| QAS-PRD-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 08-security/threat-model-slc12.md; 13-verification/acceptance/SLC-12/invariants-slc12.md |
| QAS-PRV-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 6 | 00-governance/decisions/ADR-P08.md; 02-requirements/requirements.md; 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md; 08-security/key-hierarchy-and-disposition.md; 13-verification/acceptance ...(truncated) |
| QAS-PRV-002 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc12a.md;15-traceability/quality-verification-matrix.md | 3 | 09-reliability/dr-and-continuity.md; 13-verification/fitness-functions.md; 13-verification/acceptance/SLC-12a/invariants-slc12a.md |
| QAS-RCM-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 07-quality/workloads-slc17.md; 13-verification/acceptance/SLC-17/invariants-slc17.md |
| QAS-RCM-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 1 | 13-verification/acceptance/SLC-17/invariants-slc17.md |
| QAS-REC-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 02-requirements/requirements.md; 09-reliability/dr-and-continuity.md |
| QAS-REC-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 02-requirements/requirements.md; 09-reliability/dr-and-continuity.md |
| QAS-REC-003 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 02-requirements/requirements.md; 09-reliability/dr-and-continuity.md |
| QAS-REL-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 00-governance/decisions/ADR-P02.md; 02-requirements/requirements.md; 07-quality/workloads.md |
| QAS-REL-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 4 | 02-requirements/requirements.md; 03-domain/contexts/BC07/discovery-architecture.md; 07-quality/workloads.md; 13-verification/acceptance/SLC-05/invariants-slc05.md |
| QAS-REL-003 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 02-requirements/requirements.md; 07-quality/workloads.md |
| QAS-REL-004 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc05.md;15-traceability/quality-verification-matrix.md | 3 | 03-domain/contexts/BC07/discovery-architecture.md; 09-reliability/dr-and-continuity.md; 13-verification/acceptance/SLC-05/invariants-slc05.md |
| QAS-RES-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 5 | 02-requirements/requirements.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 06-data/logical-model/slc-09.md; 07-quality/workloads-slc09.md; 13-verification/acceptance/SLC-09/invariants-slc0 ...(truncated) |
| QAS-RES-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 03-domain/contexts/BC05/allocation-readiness-spec.md; 07-quality/workloads-slc09.md; 13-verification/acceptance/SLC-09/invariants-slc09.md |
| QAS-SCAL-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 5 | 07-quality/performance-test-strategy.md; 07-quality/workloads.md; 12-solution/cell-architecture.md; 16-reports/ARCHITECTURE-REVIEW-R1.md; 16-reports/SESSION-W2.md |
| QAS-SCAL-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 7 | 03-domain/contexts/BC03/situation-alerting-spec.md; 07-quality/performance-test-strategy.md; 07-quality/workloads-slc02.md; 07-quality/workloads.md; 08-security/threat-model.md; 09-reliability/fmea-sl ...(truncated) |
| QAS-SCAL-003 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md;15-traceability/trace-slc01.md | 4 | 00-governance/decisions/ADR-P04.md; 02-requirements/requirements.md; 09-reliability/observability-slc01.md; 12-solution/cell-architecture.md |
| QAS-SCAL-004 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 1 | 07-quality/workloads.md |
| QAS-SCAL-005 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 2 | 02-requirements/requirements.md; 07-quality/performance-test-strategy.md |
| QAS-SEC-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md;15-traceability/trace-slc01.md | 4 | 00-governance/decisions/ADR-P04.md; 02-requirements/requirements.md; 13-verification/acceptance/SLC-01/invariants-slc01.md; 14-slices/SLC-01/atam-lite.md |
| QAS-SEC-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 8 | 00-governance/decisions/ADR-P06.md; 02-requirements/requirements.md; 03-domain/contexts/BC07/discovery-architecture.md; 07-quality/performance-test-strategy.md; 07-quality/workloads.md; 08-security/th ...(truncated) |
| QAS-SEC-003 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md;15-traceability/trace-slc01.md | 12 | 00-governance/decisions/ADR-P06.md; 02-requirements/requirements.md; 03-domain/contexts/BC01/security-context.md; 03-domain/contexts/BC07/discovery-architecture.md; 08-security/authorization-model.md; ...(truncated) |
| QAS-SEC-004 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 6 | 00-governance/decisions/ADR-P06.md; 00-governance/decisions/ADR-P12.md; 02-requirements/requirements.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 07-quality/workloads.md; 13-verification/ac ...(truncated) |
| QAS-SEC-005 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md;15-traceability/trace-slc01.md | 3 | 00-governance/decisions/ADR-P11.md; 02-requirements/requirements.md; 13-verification/acceptance/SLC-01/invariants-slc01.md |
| QAS-SEC-006 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md;15-traceability/trace-slc01.md | 4 | 02-requirements/requirements.md; 08-security/audit-architecture.md; 08-security/threat-model.md; 13-verification/acceptance/SLC-01/invariants-slc01.md |
| QAS-SEC-007 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 4 | 02-requirements/requirements.md; 03-domain/contexts/BC07/field-sync-protocol.md; 07-quality/workloads.md; 13-verification/acceptance/SLC-11/invariants-slc11.md |
| QAS-SEC-008 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc01.md;15-traceability/quality-verification-matrix.md;15-traceability/trace-slc01.md | 4 | 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 09-reliability/observability-slc01.md; 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/tooling/slice-sources.md |
| QAS-SEC-009 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc02.md;15-traceability/quality-verification-matrix.md | 2 | 08-security/threat-model-slc02.md; 13-verification/acceptance/SLC-02/invariants-slc02.md |
| QAS-SEC-010 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc02.md;15-traceability/quality-verification-matrix.md | 4 | 08-security/threat-model-slc02.md; 13-verification/acceptance/SLC-02/invariants-slc02.md; 14-slices/SLC-02/atam-lite.md; 16-reports/SESSION-W4-W7-SLC02.md |
| QAS-SEC-011 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc05.md;15-traceability/quality-verification-matrix.md | 2 | 03-domain/contexts/BC07/discovery-architecture.md; 13-verification/acceptance/SLC-05/invariants-slc05.md |
| QAS-SEC-012 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc06.md;15-traceability/quality-verification-matrix.md | 1 | 13-verification/acceptance/SLC-06/invariants-slc06.md |
| QAS-SEC-013 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc07.md;15-traceability/quality-verification-matrix.md | 1 | 13-verification/acceptance/SLC-07/invariants-slc07.md |
| QAS-TMP-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 7 | 00-governance/decisions/ADR-P01.md; 02-requirements/requirements.md; 03-domain/contexts/BC02/claims-temporal-kernel.md; 04-information/temporal-model.md; 07-quality/workloads.md; 13-verification/accep ...(truncated) |
| QAS-TRC-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 5 | 02-requirements/requirements.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 04-information/provenance-lineage.md; 13-verification/acceptance/SLC-07/invariants-slc07.md; 14-slices/SLC-02 ...(truncated) |
| QAS-TRC-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 5 | 02-requirements/requirements.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 04-information/provenance-lineage.md; 07-quality/workloads.md; 13-verification/acceptance/SLC-07/invariants-s ...(truncated) |
| QAS-TRC-003 | 02-requirements/quality-scenarios.md;07-quality/workloads-slc08.md;15-traceability/quality-verification-matrix.md | 1 | 13-verification/acceptance/SLC-08/invariants-slc08.md |
| QAS-TRX-001 | 02-requirements/quality-scenarios.md | 1 | 13-verification/acceptance/SLC-19/invariants-slc19.md |
| QAS-TRX-002 | 02-requirements/quality-scenarios.md | 1 | 13-verification/acceptance/SLC-19/invariants-slc19.md |
| QAS-USA-001 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 3 | 00-governance/registers/risks.md; 07-quality/workloads.md; 12-solution/ui-architecture.md |
| QAS-USA-002 | 02-requirements/quality-scenarios.md;15-traceability/quality-verification-matrix.md | 6 | 00-governance/decisions/ADR-P15.md; 02-requirements/requirements.md; 03-domain/contexts/BC07/discovery-architecture.md; 04-information/language-model.md; 07-quality/workloads.md; 13-verification/accep ...(truncated) |

### Family: QRY

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| QRY-ACS-GET | 03-domain/contexts/BC03/queries-slc07.md | 4 | 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc07.md |
| QRY-ACS-LIST | 03-domain/contexts/BC03/queries-slc07.md | 4 | 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc07.md |
| QRY-ADP-GET | 03-domain/contexts/BC07/queries-slc02.md | 4 | 05-contracts/openapi-integration-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-AIR-CONTEXT | 03-domain/contexts/BC07/queries-slc10.md | 4 | 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc10.md |
| QRY-AIR-GET | 03-domain/contexts/BC07/queries-slc10.md | 4 | 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc10.md |
| QRY-AIRS-QUEUE | 03-domain/contexts/BC07/queries-slc10.md | 4 | 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc10.md |
| QRY-AI-USAGE | 03-domain/contexts/BC07/queries-slc10.md | 4 | 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc10.md |
| QRY-ALC-LIST | 03-domain/contexts/BC05/queries-slc09.md | 4 | 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc09.md |
| QRY-ALR-LIST | 03-domain/contexts/BC03/queries-slc06.md | 4 | 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc06.md |
| QRY-AMT-LIST | 03-domain/contexts/BC03/queries-slc07.md | 4 | 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc07.md |
| QRY-ARC-RETRIEVE | 03-domain/contexts/BC06/queries-slc12.md | 4 | 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12.md |
| QRY-ARC-SEARCH | 03-domain/contexts/BC06/queries-slc12.md | 4 | 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12.md |
| QRY-ASM-GET | 03-domain/contexts/BC03/queries-slc07.md | 4 | 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc07.md |
| QRY-ASM-VERSIONS | 03-domain/contexts/BC03/queries-slc07.md | 4 | 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc07.md |
| QRY-AST-AVAILABILITY | 03-domain/contexts/BC05/queries-slc09.md | 4 | 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc09.md |
| QRY-AST-GET | 03-domain/contexts/BC05/queries-slc09.md | 4 | 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc09.md |
| QRY-ATT-DOWNLOAD | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-AUD-SEARCH | 03-domain/contexts/BC08/queries-slc01.md | 4 | 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc01.md |
| QRY-AUD-VERIFY | 03-domain/contexts/BC08/queries-slc01.md | 5 | 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 13-verification/tooling/spec-tooling.md; 15-traceability/trace-slc01.md |
| QRY-AUT-CHECK | 03-domain/contexts/BC01/queries-slc01.md | 6 | 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 13-verification/tooling/sp ...(truncated) |
| QRY-AUT-LIST | 03-domain/contexts/BC01/queries-slc01.md | 4 | 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc01.md |
| QRY-BASE-TILE | 03-domain/contexts/BC03/queries-slc06.md | 4 | 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc06.md |
| QRY-CAP-LIST | 03-domain/contexts/BC03/queries-slc16.md | 4 | 05-contracts/openapi-intelligence-slc16.md; 08-security/policies-slc16.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc16.md |
| QRY-CAT-BC01-SLC01 | 03-domain/contexts/BC01/queries-slc01.md | 0 |  |
| QRY-CAT-BC01-SLC11 | 03-domain/contexts/BC01/queries-slc11.md | 0 |  |
| QRY-CAT-BC01-SLC16 | 03-domain/contexts/BC01/queries-slc16.md | 0 |  |
| QRY-CAT-BC02-SLC02 | 03-domain/contexts/BC02/queries-slc02.md | 0 |  |
| QRY-CAT-BC02-SLC04 | 03-domain/contexts/BC02/queries-slc04.md | 0 |  |
| QRY-CAT-BC02-SLC14 | 03-domain/contexts/BC02/queries-slc14.md | 0 |  |
| QRY-CAT-BC02-SLC15 | 03-domain/contexts/BC02/queries-slc15.md | 0 |  |
| QRY-CAT-BC03-SLC06 | 03-domain/contexts/BC03/queries-slc06.md | 0 |  |
| QRY-CAT-BC03-SLC07 | 03-domain/contexts/BC03/queries-slc07.md | 0 |  |
| QRY-CAT-BC03-SLC16 | 03-domain/contexts/BC03/queries-slc16.md | 0 |  |
| QRY-CAT-BC04-SLC03 | 03-domain/contexts/BC04/queries-slc03.md | 0 |  |
| QRY-CAT-BC04-SLC06 | 03-domain/contexts/BC04/queries-slc06.md | 0 |  |
| QRY-CAT-BC04-SLC08 | 03-domain/contexts/BC04/queries-slc08.md | 0 |  |
| QRY-CAT-BC04-SLC15 | 03-domain/contexts/BC04/queries-slc15.md | 0 |  |
| QRY-CAT-BC04-SLC17 | 03-domain/contexts/BC04/queries-slc17.md | 0 |  |
| QRY-CAT-BC05-SLC03 | 03-domain/contexts/BC05/queries-slc03.md | 0 |  |
| QRY-CAT-BC05-SLC09 | 03-domain/contexts/BC05/queries-slc09.md | 0 |  |
| QRY-CAT-BC05-SLC18 | 03-domain/contexts/BC05/queries-slc18.md | 0 |  |
| QRY-CAT-BC05-SLC19 | 03-domain/contexts/BC05/queries-slc19.md | 0 |  |
| QRY-CAT-BC06-SLC12 | 03-domain/contexts/BC06/queries-slc12.md | 0 |  |
| QRY-CAT-BC07-SLC02 | 03-domain/contexts/BC07/queries-slc02.md | 0 |  |
| QRY-CAT-BC07-SLC05 | 03-domain/contexts/BC07/queries-slc05.md | 0 |  |
| QRY-CAT-BC07-SLC10 | 03-domain/contexts/BC07/queries-slc10.md | 0 |  |
| QRY-CAT-BC07-SLC11 | 03-domain/contexts/BC07/queries-slc11.md | 0 |  |
| QRY-CAT-BC07-SLC16 | 03-domain/contexts/BC07/queries-slc16.md | 0 |  |
| QRY-CAT-BC08-SLC01 | 03-domain/contexts/BC08/queries-slc01.md | 0 |  |
| QRY-CAT-BC08-SLC12A | 03-domain/contexts/BC08/queries-slc12a.md | 0 |  |
| QRY-CLM-GET | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-CLR-GET | 03-domain/contexts/BC01/queries-slc01.md | 4 | 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc01.md |
| QRY-CLS-ACTIVE | 03-domain/contexts/BC08/queries-slc01.md | 4 | 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc01.md |
| QRY-CLUSTER-GET | 03-domain/contexts/BC02/queries-slc04.md | 4 | 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc04.md |
| QRY-CNF-GET | 03-domain/contexts/BC02/queries-slc04.md | 4 | 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc04.md |
| QRY-CNF-LIST | 03-domain/contexts/BC02/queries-slc04.md | 5 | 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-verification/acceptance/SLC-04/invariants-slc04.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc04.m ...(truncated) |
| QRY-CON-LIST | 03-domain/contexts/BC07/queries-slc16.md | 4 | 05-contracts/openapi-integration-slc16.md; 08-security/policies-slc16.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc16.md |
| QRY-CPL-GET | 03-domain/contexts/BC02/queries-slc14.md | 4 | 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc14.md |
| QRY-CRD-GET | 03-domain/contexts/BC04/queries-slc15.md | 4 | 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc15.md |
| QRY-CRD-LIST | 03-domain/contexts/BC04/queries-slc15.md | 4 | 05-contracts/openapi-operations-slc15.md; 08-security/policies-slc15.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc15.md |
| QRY-CRP-GET | 03-domain/contexts/BC02/queries-slc15.md | 4 | 05-contracts/openapi-information-slc15.md; 08-security/policies-slc15.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc15.md |
| QRY-CRP-QUEUE | 03-domain/contexts/BC02/queries-slc15.md | 4 | 05-contracts/openapi-information-slc15.md; 08-security/policies-slc15.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc15.md |
| QRY-CRQ-BOARD | 03-domain/contexts/BC02/queries-slc14.md | 4 | 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc14.md |
| QRY-CRQ-EVIDENCE | 03-domain/contexts/BC02/queries-slc14.md | 4 | 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc14.md |
| QRY-CRQ-GET | 03-domain/contexts/BC02/queries-slc14.md | 4 | 05-contracts/openapi-information-slc14.md; 08-security/policies-slc14.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc14.md |
| QRY-DEC-BASIS | 03-domain/contexts/BC04/queries-slc08.md | 6 | 03-domain/contexts/BC04/decision-plan-spec.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/acceptance/SLC-08/invariants-slc08.md; 13-verification/tooling/s ...(truncated) |
| QRY-DEC-GET | 03-domain/contexts/BC04/queries-slc08.md | 4 | 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc08.md |
| QRY-DEV-LIST | 03-domain/contexts/BC01/queries-slc11.md | 4 | 05-contracts/openapi-foundation-slc11.md; 08-security/policies-slc11.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc11.md |
| QRY-DRQ-GET | 03-domain/contexts/BC04/queries-slc08.md | 4 | 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc08.md |
| QRY-DRQ-LIST | 03-domain/contexts/BC04/queries-slc08.md | 4 | 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc08.md |
| QRY-DSP-GET | 03-domain/contexts/BC08/queries-slc12a.md | 4 | 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12a.md |
| QRY-DST-LOG | 03-domain/contexts/BC06/queries-slc12.md | 4 | 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12.md |
| QRY-ELIG-CHECK | 03-domain/contexts/BC05/queries-slc03.md | 4 | 05-contracts/openapi-readiness-slc03.md; 08-security/policies-slc03.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc03.md |
| QRY-ENT-CLAIMS | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-ENT-LIST | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-ENT-POSITIONS | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-ENT-RESOLVED | 03-domain/contexts/BC02/queries-slc02.md | 7 | 00-governance/RATIFICATION-PACKAGE.md; 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 14-slices/SLC-04/readiness.md; 15-traceabilit ...(truncated) |
| QRY-ER-GET | 03-domain/contexts/BC02/queries-slc04.md | 4 | 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc04.md |
| QRY-ER-QUEUE | 03-domain/contexts/BC02/queries-slc04.md | 4 | 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc04.md |
| QRY-ERS-GET | 03-domain/contexts/BC08/queries-slc12a.md | 4 | 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12a.md |
| QRY-EVD-GET | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-EXC-LIST | 03-domain/contexts/BC08/queries-slc01.md | 4 | 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc01.md |
| QRY-EXR-GET | 03-domain/contexts/BC05/queries-slc19.md | 4 | 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc19.md |
| QRY-EXR-LIST | 03-domain/contexts/BC05/queries-slc19.md | 4 | 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc19.md |
| QRY-EXT-RESOLVE | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-FND-LIST | 03-domain/contexts/BC03/queries-slc07.md | 4 | 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc07.md |
| QRY-GRAPH-NEIGHBORHOOD | 03-domain/contexts/BC07/queries-slc05.md | 4 | 05-contracts/openapi-discovery-slc05.md; 08-security/policies-slc05.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc05.md |
| QRY-GRAPH-PATHS | 03-domain/contexts/BC07/queries-slc05.md | 4 | 05-contracts/openapi-discovery-slc05.md; 08-security/policies-slc05.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc05.md |
| QRY-HRS-QUEUE | 03-domain/contexts/BC01/queries-slc16.md | 4 | 05-contracts/openapi-foundation-slc16.md; 08-security/policies-slc16.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc16.md |
| QRY-IMP-GET | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-INC-GET | 03-domain/contexts/BC04/queries-slc17.md | 4 | 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc17.md |
| QRY-INC-LIST | 03-domain/contexts/BC04/queries-slc17.md | 4 | 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc17.md |
| QRY-INC-RECOVERY-STATUS | 03-domain/contexts/BC04/queries-slc17.md | 6 | 03-domain/contexts/BC04/risk-contingency-spec.md; 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 09-reliability/fmea-slc17.md; 13-verification/tooling/slice-sources.md; 15-tr ...(truncated) |
| QRY-KNO-SEARCH | 03-domain/contexts/BC06/queries-slc12.md | 4 | 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12.md |
| QRY-KNO-SUGGEST | 03-domain/contexts/BC06/queries-slc12.md | 4 | 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12.md |
| QRY-LGR-GET | 03-domain/contexts/BC05/queries-slc18.md | 4 | 05-contracts/openapi-readiness-slc18.md; 08-security/policies-slc18.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc18.md |
| QRY-LGR-LIST | 03-domain/contexts/BC05/queries-slc18.md | 4 | 05-contracts/openapi-readiness-slc18.md; 08-security/policies-slc18.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc18.md |
| QRY-LHD-CHECK | 03-domain/contexts/BC08/queries-slc12a.md | 4 | 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12a.md |
| QRY-LHD-LIST | 03-domain/contexts/BC08/queries-slc12a.md | 4 | 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12a.md |
| QRY-LIN-TRACE | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-MDL-LIST | 03-domain/contexts/BC07/queries-slc10.md | 4 | 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc10.md |
| QRY-MNT-SCHEDULE | 03-domain/contexts/BC05/queries-slc09.md | 4 | 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc09.md |
| QRY-MRS-GET | 03-domain/contexts/BC02/queries-slc04.md | 4 | 05-contracts/openapi-information-slc04.md; 08-security/policies-slc04.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc04.md |
| QRY-NTF-INBOX | 03-domain/contexts/BC04/queries-slc06.md | 4 | 05-contracts/openapi-operations-slc06.md; 08-security/policies-slc06.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc06.md |
| QRY-OBS-GET | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-OBS-LIST | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-ORG-TREE | 03-domain/contexts/BC01/queries-slc01.md | 4 | 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc01.md |
| QRY-OUT-SERIES | 03-domain/contexts/BC04/queries-slc08.md | 4 | 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc08.md |
| QRY-PDP-DECIDE | 03-domain/contexts/BC08/queries-slc01.md | 5 | 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 13-verification/tooling/spec-tooling.md; 15-traceability/trace-slc01.md |
| QRY-PKG-GET | 03-domain/contexts/BC07/queries-slc11.md | 4 | 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc11.md |
| QRY-PLN-GET | 03-domain/contexts/BC04/queries-slc08.md | 4 | 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc08.md |
| QRY-PLN-PROGRESS | 03-domain/contexts/BC04/queries-slc08.md | 4 | 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc08.md |
| QRY-PLV-DIFF | 03-domain/contexts/BC04/queries-slc08.md | 6 | 03-domain/contexts/BC04/decision-plan-spec.md; 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/acceptance/SLC-08/invariants-slc08.md; 13-verification/tooling/s ...(truncated) |
| QRY-PLV-LIST | 03-domain/contexts/BC04/queries-slc08.md | 4 | 05-contracts/openapi-operations-slc08.md; 08-security/policies-slc08.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc08.md |
| QRY-POL-GET | 03-domain/contexts/BC08/queries-slc01.md | 4 | 05-contracts/openapi-governance-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc01.md |
| QRY-POL-TIMELINE | 03-domain/contexts/BC05/queries-slc09.md | 4 | 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc09.md |
| QRY-PRD-GET | 03-domain/contexts/BC06/queries-slc12.md | 4 | 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12.md |
| QRY-PRD-LIST | 03-domain/contexts/BC06/queries-slc12.md | 4 | 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12.md |
| QRY-PRJ-STATUS | 03-domain/contexts/BC07/queries-slc05.md | 4 | 05-contracts/openapi-discovery-slc05.md; 08-security/policies-slc05.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc05.md |
| QRY-QUAL-LIST | 03-domain/contexts/BC05/queries-slc03.md | 4 | 05-contracts/openapi-readiness-slc03.md; 08-security/policies-slc03.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc03.md |
| QRY-READINESS | 03-domain/contexts/BC05/queries-slc09.md | 4 | 05-contracts/openapi-readiness-slc09.md; 08-security/policies-slc09.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc09.md |
| QRY-REC-REPORT | 03-domain/contexts/BC06/queries-slc12.md | 4 | 05-contracts/openapi-knowledge-slc12.md; 08-security/policies-slc12.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12.md |
| QRY-REL-LIST | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-RIS-GET | 03-domain/contexts/BC04/queries-slc17.md | 4 | 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc17.md |
| QRY-RIS-REGISTER | 03-domain/contexts/BC04/queries-slc17.md | 4 | 05-contracts/openapi-operations-slc17.md; 08-security/policies-slc17.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc17.md |
| QRY-RTG-ACTIVE | 03-domain/contexts/BC07/queries-slc10.md | 4 | 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc10.md |
| QRY-RTS-ACTIVE | 03-domain/contexts/BC08/queries-slc12a.md | 4 | 05-contracts/openapi-governance-slc12a.md; 08-security/policies-slc12a.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc12a.md |
| QRY-RUN-ARTIFACT | 03-domain/contexts/BC03/queries-slc07.md | 4 | 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc07.md |
| QRY-RUN-GET | 03-domain/contexts/BC03/queries-slc07.md | 4 | 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc07.md |
| QRY-RWE-GET | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-SCF-GET | 03-domain/contexts/BC07/queries-slc11.md | 4 | 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc11.md |
| QRY-SCF-LIST | 03-domain/contexts/BC07/queries-slc11.md | 4 | 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc11.md |
| QRY-SCN-COMPARE | 03-domain/contexts/BC03/queries-slc07.md | 4 | 05-contracts/openapi-intelligence-slc07.md; 08-security/policies-slc07.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc07.md |
| QRY-SCN-GET | 03-domain/contexts/BC05/queries-slc19.md | 4 | 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc19.md |
| QRY-SCN-LIST | 03-domain/contexts/BC05/queries-slc19.md | 4 | 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc19.md |
| QRY-SEC-CONTEXT | 03-domain/contexts/BC01/queries-slc01.md | 5 | 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 13-verification/tooling/spec-tooling.md; 15-traceability/trace-slc01.md |
| QRY-SHP-GET | 03-domain/contexts/BC05/queries-slc18.md | 4 | 05-contracts/openapi-readiness-slc18.md; 08-security/policies-slc18.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc18.md |
| QRY-SHP-LIST | 03-domain/contexts/BC05/queries-slc18.md | 4 | 05-contracts/openapi-readiness-slc18.md; 08-security/policies-slc18.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc18.md |
| QRY-SHP-TRACKING | 03-domain/contexts/BC05/queries-slc18.md | 5 | 02-requirements/requirements.md; 05-contracts/openapi-readiness-slc18.md; 08-security/policies-slc18.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc18.md |
| QRY-SIM-GET | 03-domain/contexts/BC05/queries-slc19.md | 4 | 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc19.md |
| QRY-SIM-LIST | 03-domain/contexts/BC05/queries-slc19.md | 4 | 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc19.md |
| QRY-SIM-TIMELINE | 03-domain/contexts/BC05/queries-slc19.md | 5 | 02-requirements/requirements.md; 05-contracts/openapi-readiness-slc19.md; 08-security/policies-slc19.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc19.md |
| QRY-SIT-CHANGES | 03-domain/contexts/BC03/queries-slc06.md | 5 | 05-contracts/openapi-intelligence-slc06.md; 06-data/logical-model/slc-06.md; 08-security/policies-slc06.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc06.md |
| QRY-SIT-COP | 03-domain/contexts/BC03/queries-slc06.md | 4 | 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc06.md |
| QRY-SIT-GET | 03-domain/contexts/BC03/queries-slc06.md | 4 | 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc06.md |
| QRY-SIT-LIST | 03-domain/contexts/BC03/queries-slc06.md | 4 | 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc06.md |
| QRY-SIT-TILE | 03-domain/contexts/BC03/queries-slc06.md | 4 | 05-contracts/openapi-intelligence-slc06.md; 08-security/policies-slc06.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc06.md |
| QRY-SNS-LIST | 03-domain/contexts/BC07/queries-slc16.md | 4 | 05-contracts/openapi-integration-slc16.md; 08-security/policies-slc16.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc16.md |
| QRY-SRC-GET | 03-domain/contexts/BC02/queries-slc02.md | 4 | 05-contracts/openapi-information-slc02.md; 08-security/policies-slc02.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc02.md |
| QRY-SRCH-QUERY | 03-domain/contexts/BC07/queries-slc05.md | 4 | 05-contracts/openapi-discovery-slc05.md; 08-security/policies-slc05.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc05.md |
| QRY-SRCH-SUGGEST | 03-domain/contexts/BC07/queries-slc05.md | 4 | 05-contracts/openapi-discovery-slc05.md; 08-security/policies-slc05.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc05.md |
| QRY-SYN-DELTA | 03-domain/contexts/BC07/queries-slc11.md | 4 | 05-contracts/openapi-field-slc11.md; 08-security/policies-slc11.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc11.md |
| QRY-TASK-GET | 03-domain/contexts/BC04/queries-slc03.md | 4 | 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc03.md |
| QRY-TASK-HISTORY | 03-domain/contexts/BC04/queries-slc03.md | 5 | 05-contracts/openapi-operations-slc03.md; 06-data/logical-model/slc-03.md; 08-security/policies-slc03.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc03.md |
| QRY-TASK-LIST | 03-domain/contexts/BC04/queries-slc03.md | 4 | 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc03.md |
| QRY-TEN-GET | 03-domain/contexts/BC01/queries-slc01.md | 4 | 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc01.md |
| QRY-TOL-LIST | 03-domain/contexts/BC07/queries-slc10.md | 4 | 05-contracts/openapi-ai-slc10.md; 08-security/policies-slc10.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc10.md |
| QRY-TTY-GET | 03-domain/contexts/BC04/queries-slc03.md | 4 | 05-contracts/openapi-operations-slc03.md; 08-security/policies-slc03.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc03.md |
| QRY-USR-GET | 03-domain/contexts/BC01/queries-slc01.md | 4 | 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc01.md |
| QRY-USR-LIST | 03-domain/contexts/BC01/queries-slc01.md | 4 | 05-contracts/openapi-foundation-slc01.md; 08-security/policies-slc01.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc01.md |

### Family: QUALITY

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| QUALITY-MATRIX | 15-traceability/quality-verification-matrix.md | 1 | 16-reports/IMPLEMENTATION-READINESS-R1.md |

### Family: RD

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| RD-ALERT-RULE-TYPES | 04-information/reference-data.md | 3 | 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 13-verification/tooling/slice-sources.md |
| RD-CLASSIFICATION | 04-information/reference-data.md | 0 |  |
| RD-COMPETENCIES | 04-information/reference-data.md | 10 | 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 03-domain/contexts/BC05/commands-slc03.md; 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts ...(truncated) |
| RD-CONFLICT-RULES | 04-information/reference-data.md | 2 | 03-domain/contexts/BC02/conflict-detection-engine.md; 04-information/conflict-model.md |
| RD-CRS | 04-information/reference-data.md | 0 |  |
| RD-DECISION-TYPES | 04-information/reference-data.md | 3 | 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md; 13-verification/tooling/slice-sources.md |
| RD-ENTITY-TYPES | 04-information/reference-data.md | 3 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 13-verification/tooling/slice-sources.md |
| RD-ESTIMATIVE-PROBABILITY | 04-information/reference-data.md | 5 | 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 04-information/confidence-model.md; 13-verifi ...(truncated) |
| RD-EVENT-TYPES | 04-information/reference-data.md | 3 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 13-verification/tooling/slice-sources.md |
| RD-EVIDENCE-TYPES | 04-information/reference-data.md | 3 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 13-verification/tooling/slice-sources.md |
| RD-INFO-CREDIBILITY | 04-information/reference-data.md | 0 |  |
| RD-LANGUAGES | 04-information/reference-data.md | 0 |  |
| RD-OBJECT-TYPES | 04-information/reference-data.md | 1 | 04-information/object-envelope.md |
| RD-PREDICATES | 04-information/reference-data.md | 6 | 03-domain/contexts/BC02/claims-temporal-kernel.md; 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 04-information/claim-evidence-model.md; 07-quality/worklo ...(truncated) |
| RD-RECORD-CLASSES | 04-information/reference-data.md | 4 | 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md; 13-verification/acceptance/SLC-12a/invariants-slc12a.md; 13-verification/tooling/slice-sources ...(truncated) |
| RD-RELATIONSHIP-TYPES | 04-information/reference-data.md | 3 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 13-verification/tooling/slice-sources.md |
| RD-SOURCE-RELIABILITY | 04-information/reference-data.md | 1 | 04-information/claim-evidence-model.md |
| RD-SOURCE-TYPES | 04-information/reference-data.md | 3 | 03-domain/contexts/BC02/commands-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 13-verification/tooling/slice-sources.md |
| RD-TASK-TYPES | 04-information/reference-data.md | 0 |  |
| RD-UNITS | 04-information/reference-data.md | 0 |  |

### Family: REG

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| REG-ASM | 00-governance/registers/assumptions.md | 0 |  |
| REG-CR | 00-governance/registers/corrections.md | 0 |  |
| REG-DEBT | 00-governance/registers/technical-debt.md | 0 |  |
| REG-DEP | 00-governance/registers/dependencies.md | 0 |  |
| REG-HAP | 00-governance/registers/human-approvals.md | 0 |  |
| REG-OQ | 00-governance/registers/open-questions.md | 0 |  |
| REG-RSK | 00-governance/registers/risks.md | 0 |  |
| REG-UNK | 00-governance/registers/unknowns.md | 0 |  |

### Family: RELEASE

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| RELEASE-CONFIG-MIGRATION | 12-solution/release-configuration-migration.md | 2 | 15-traceability/trace-platform.md; 16-reports/IMPLEMENTATION-READINESS-R1.md |

### Family: REQ

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| REQ-AI-001 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 9 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 03-domain/contexts/BC07/queries-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQ ...(truncated) |
| REQ-AI-002 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 9 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 03-domain/contexts/BC07/queries-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQ ...(truncated) |
| REQ-AI-003 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 7 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 13-verification/acceptance/SLC-10 ...(truncated) |
| REQ-AI-004 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 7 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 13-verification/acceptance/SLC-10 ...(truncated) |
| REQ-AI-005 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 10 | 02-requirements/use-cases.md; 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 03-domain/contexts/BC07/queries ...(truncated) |
| REQ-AI-006 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md; 13-verification/acceptance/SLC-10/ai-result-state-machine.md; 13-verific ...(truncated) |
| REQ-AI-007 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 13-verification/acceptance/SLC-10/ai-request-state-machine.md; 13-verif ...(truncated) |
| REQ-AI-008 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 12 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 03-domain/contexts/BC07/queries-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 03-domain/contexts/BC07/aggre ...(truncated) |
| REQ-AI-009 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 6 | 03-domain/contexts/BC07/queries-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/invariants-slc10.md; 13-verificat ...(truncated) |
| REQ-AI-010 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 7 | 03-domain/contexts/BC07/commands-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md; 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md; 13-verification/acceptance/SLC-10/eval-suite-s ...(truncated) |
| REQ-AI-011 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 7 | 03-domain/contexts/BC07/grounded-ai-spec.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md; 13-verification/acceptance/SLC-10/ai-request-st ...(truncated) |
| REQ-AI-012 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 13-verification/acce ...(truncated) |
| REQ-AI-013 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 7 | 03-domain/contexts/BC07/queries-slc10.md; 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md; 05-contracts/openapi-ai-slc10.md; 13-verification/acceptance/SLC-10/ai-tool-state-machine.md; 13-verificati ...(truncated) |
| REQ-AI-014 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc10.md | 3 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 13-verification/acceptance/SLC-10/invariants-slc10.md |
| REQ-ANL-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc07.md | 9 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/queries-slc07.md; 03-domain/contexts/BC03/agg ...(truncated) |
| REQ-ANL-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc07.md | 11 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/queries-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md; 03-domain/c ...(truncated) |
| REQ-ANL-003 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc07.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.m ...(truncated) |
| REQ-ANL-004 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc07.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md; 13-verification/acceptance/SLC-07/analysis-run-state-mac ...(truncated) |
| REQ-ANL-005 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc07.md | 12 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/queries-slc07.md; 03-domain/contexts/BC03/agg ...(truncated) |
| REQ-ANL-006 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc07.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/queries-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/ope ...(truncated) |
| REQ-ANL-007 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc07.md | 9 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/commands-slc07.md; 03-domain/contexts/BC03/queries-slc07.md; 03-domain/contexts/BC03/agg ...(truncated) |
| REQ-ANL-008 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc07.md | 8 | 01-business/business-rules.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/queries-slc07.md; 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md; 05-contracts/op ...(truncated) |
| REQ-ARC-001 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 13-verification/acceptance/SLC-12/archive-package-s ...(truncated) |
| REQ-ARC-002 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 7 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md; 13-verificati ...(truncated) |
| REQ-ARC-003 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 10 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/queries-slc12.md; 03-domain/contexts/BC06/aggreg ...(truncated) |
| REQ-ARC-004 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 9 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/queries-slc12.md; 03-domain/contexts/BC06/aggreg ...(truncated) |
| REQ-BASELINE | 02-requirements/requirements.md | 0 |  |
| REQ-COL-001 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc14.md | 9 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/collection-spec.md; 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/queries-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-CO ...(truncated) |
| REQ-COL-002 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc14.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/collection-spec.md; 03-domain/contexts/BC02/queries-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md; 05-contracts/openapi-info ...(truncated) |
| REQ-COL-003 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc14.md | 9 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC02/collection-spec.md; 03-domain/contexts/BC02/queries-slc14.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECT ...(truncated) |
| REQ-COM-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc06.md | 11 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 03-domain/contexts/BC04/queries-slc06.md; 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md; 03-domain/contexts/B ...(truncated) |
| REQ-COM-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc06.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md; 13-verification/acceptance/SLC-06/invariants-slc06.md; 13-veri ...(truncated) |
| REQ-CRD-001 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc15.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/correlation-fusion-spec.md; 03-domain/contexts/BC04/queries-slc15.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 05-contracts/op ...(truncated) |
| REQ-CRD-002 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc15.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/correlation-fusion-spec.md; 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md; 13-verification/acceptance/SLC-15/coordination-case-state ...(truncated) |
| REQ-DEC-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc08.md | 10 | 02-requirements/use-cases.md; 03-domain/ownership.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/queries-slc08.md; 03-domain/cont ...(truncated) |
| REQ-DEC-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc08.md | 8 | 01-business/business-rules.md; 02-requirements/use-cases.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION.m ...(truncated) |
| REQ-DEC-003 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc08.md | 10 | 02-requirements/use-cases.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/queries-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION.md; 04-information/provenance-lin ...(truncated) |
| REQ-DEC-004 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc08.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/aggregates/AGG-DECISION.md; 13-verification/acceptance/SLC-08/decision-state-machine.md; 13-verific ...(truncated) |
| REQ-FND-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 7 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/queries-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC-01/in ...(truncated) |
| REQ-FND-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/queries-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/SLC ...(truncated) |
| REQ-FND-003 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 5 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 13-verification/acceptance/SLC-01/invariants-slc01.md; 13-verification/acceptance/SLC-01/tenant-state-machine.md; 13-ver ...(truncated) |
| REQ-FND-004 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 5 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 12-solution/cell-architecture.md; 13-verification/acceptance/SLC-01/tenant-state-machine.md; 13-verification/tooling/sli ...(truncated) |
| REQ-FND-005 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 8 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC01/aggregates/AGG-USER.md; 07-quality/workloads-slc01.md; 12-solution/technology-decisions.md; 13-verification/ ...(truncated) |
| REQ-FND-006 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 10 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/queries-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md; 03-domain/contexts/ ...(truncated) |
| REQ-FND-007 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/queries-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/ ...(truncated) |
| REQ-FND-008 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 5 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 13-verification/acceptance/SLC-01/authority-grant-state-machine.md; 13-verification/acceptance/SLC-01/invariant ...(truncated) |
| REQ-FND-009 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 7 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/queries-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 05-contracts/openapi-foundation-slc01.md; 13-verification/acceptance/ ...(truncated) |
| REQ-FND-010 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md;15-traceability/trace-slc05.md | 12 | 01-business/business-rules.md; 03-domain/contexts/BC01/queries-slc01.md; 03-domain/contexts/BC01/security-context.md; 03-domain/contexts/BC07/discovery-architecture.md; 03-domain/contexts/BC08/queries ...(truncated) |
| REQ-FND-011 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 9 | 00-governance/registers/corrections.md; 02-requirements/use-cases.md; 03-domain/contexts/BC01/security-context.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md; 03-domain/contexts/BC08/ag ...(truncated) |
| REQ-FND-012 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 5 | 02-requirements/use-cases.md; 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md; 08-security/authorization-model.md; 13-verification/acceptance/SLC-01/policy-set-state-machine.md; 13-verification/t ...(truncated) |
| REQ-FND-013 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 4 | 08-security/authorization-model.md; 13-verification/fitness-functions.md; 13-verification/acceptance/SLC-01/invariants-slc01.md; 16-reports/CONSISTENCY-CHECK-W3.md |
| REQ-FND-014 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 6 | 00-governance/registers/corrections.md; 02-requirements/use-cases.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE.md; 08-security/authorization-model.md; 13-verification/acceptance/SLC-01/role-state-m ...(truncated) |
| REQ-FND-015 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 8 | 01-business/business-rules.md; 02-requirements/use-cases.md; 03-domain/contexts/BC08/queries-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/audit-architecture.md; 08-security/classifi ...(truncated) |
| REQ-FND-016 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC08/queries-slc01.md; 05-contracts/openapi-governance-slc01.md; 08-security/audit-architecture.md; 13-verification/acceptance/SLC-01/invariants-slc01. ...(truncated) |
| REQ-FND-017 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 8 | 02-requirements/use-cases.md; 03-domain/ownership.md; 03-domain/contexts/BC08/queries-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md; 05-contracts/openapi-governance-slc01.md;  ...(truncated) |
| REQ-FND-018 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 5 | 02-requirements/use-cases.md; 03-domain/ownership.md; 03-domain/contexts/BC01/aggregates/AGG-TENANT.md; 13-verification/acceptance/SLC-01/tenant-state-machine.md; 13-verification/tooling/slice-sources ...(truncated) |
| REQ-FUS-001 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc15.md | 10 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/correlation-fusion-spec.md; 03-domain/contexts/BC02/queries-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 03-domain/co ...(truncated) |
| REQ-FUS-002 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc15.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/correlation-fusion-spec.md; 03-domain/contexts/BC02/queries-slc15.md; 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md; 05-contracts ...(truncated) |
| REQ-GOV-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 8 | 00-governance/registers/corrections.md; 02-requirements/use-cases.md; 03-domain/contexts/BC08/queries-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 05-contracts/openapi-go ...(truncated) |
| REQ-GOV-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 6 | 00-governance/registers/corrections.md; 08-security/classification-scheme.md; 08-security/label-derivation-rules.md; 15-traceability/trace-platform.md; 16-reports/CONSISTENCY-CHECK-W3.md; 16-reports/S ...(truncated) |
| REQ-GOV-003 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 9 | 00-governance/registers/corrections.md; 02-requirements/use-cases.md; 03-domain/contexts/BC01/queries-slc01.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 05-contracts/openapi-foundation-slc ...(truncated) |
| REQ-GOV-004 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md;15-traceability/trace-slc05.md | 22 | 00-governance/decisions/ADR-P06.md; 00-governance/registers/corrections.md; 02-requirements/use-cases.md; 03-domain/contexts/BC01/security-context.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE. ...(truncated) |
| REQ-GOV-005 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 3 | 08-security/data-protection.md; 12-solution/cell-architecture.md; 15-traceability/trace-platform.md |
| REQ-GOV-006 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc12a.md | 13 | 02-requirements/use-cases.md; 03-domain/ownership.md; 03-domain/contexts/BC08/commands-slc12a.md; 03-domain/contexts/BC08/queries-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md;  ...(truncated) |
| REQ-GOV-007 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc12a.md | 11 | 02-requirements/use-cases.md; 03-domain/ownership.md; 03-domain/contexts/BC08/queries-slc12a.md; 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md; 03-domain/contexts/BC08/aggregates/AGG-LEGAL ...(truncated) |
| REQ-GOV-008 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md;15-traceability/trace-slc02.md;15-traceability/trace-slc12a.md | 14 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/aggregates/AGG-PERSON.md; 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 03-domain/contexts/BC08/queries-slc12a.md; 03-domain/contexts/BC08 ...(truncated) |
| REQ-GOV-009 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md | 10 | 00-governance/registers/corrections.md; 02-requirements/use-cases.md; 03-domain/contexts/BC08/queries-slc01.md; 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md; 03-domain/contexts/BC08 ...(truncated) |
| REQ-INF-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md; 04-information/claim-evidence-model.md; 05-contracts/openapi-information-slc02 ...(truncated) |
| REQ-INF-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 04-information/claim-evidence-model.md; 05-contracts/openapi-information- ...(truncated) |
| REQ-INF-003 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 9 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 04-information/claim-evidence-model.md; 13-verification/acceptan ...(truncated) |
| REQ-INF-004 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 11 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md; 05-contracts/openapi-i ...(truncated) |
| REQ-INF-005 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 11 | 02-requirements/use-cases.md; 03-domain/context-map.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 03-domain/contexts/BC07/queries-slc02.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER ...(truncated) |
| REQ-INF-006 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 9 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 04-information/spatial-model.md; 0 ...(truncated) |
| REQ-INF-007 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 5 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 13-verification/acceptance/SLC-02/import-batch-state-machine.md; 13-verification/acceptance/SLC-02/invariants-slc0 ...(truncated) |
| REQ-INF-008 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 9 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 04-information/spatial-model.md; 12-solution/technology-decisio ...(truncated) |
| REQ-INF-009 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 7 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md; 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md; 13-verification/acceptance/SLC-02/adapter-state-machine.md; 13- ...(truncated) |
| REQ-INF-020 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 9 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md; 05-contracts/openap ...(truncated) |
| REQ-INF-021 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 14 | 01-business/business-rules.md; 02-requirements/use-cases.md; 03-domain/contexts/BC02/claims-temporal-kernel.md; 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.m ...(truncated) |
| REQ-INF-022 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 8 | 03-domain/contexts/BC02/claims-temporal-kernel.md; 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 04-information/temporal-model.md; 05-contracts/openapi-inf ...(truncated) |
| REQ-INF-023 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/claims-temporal-kernel.md; 03-domain/contexts/BC02/queries-slc02.md; 04-information/temporal-model.md; 05-contracts/openapi-information-slc02.md;  ...(truncated) |
| REQ-INF-024 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md;15-traceability/trace-slc04.md | 12 | 01-business/business-rules.md; 03-domain/contexts/BC02/claims-temporal-kernel.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md; 04-information/cl ...(truncated) |
| REQ-INF-025 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md;15-traceability/trace-slc04.md | 10 | 01-business/business-rules.md; 02-requirements/use-cases.md; 03-domain/contexts/BC02/conflict-detection-engine.md; 03-domain/contexts/BC02/queries-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-CONF ...(truncated) |
| REQ-INF-026 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 6 | 03-domain/contexts/BC02/claims-temporal-kernel.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 04-information/confidence-model.md; 13-verification/acceptance/SLC-02/claim-state-machine.md; 13-ver ...(truncated) |
| REQ-INF-027 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md;15-traceability/trace-slc05.md | 12 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md; 03-domain/contexts/BC07/discovery-architecture.md; 03-domain/contexts/BC ...(truncated) |
| REQ-INF-028 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 5 | 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md; 04-information/spatial-model.md; 13-verification/acceptance/SLC-02/invariants-slc02.md; 13-verification/acceptance/SLC-02/observation-state-machi ...(truncated) |
| REQ-INF-029 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 3 | 00-governance/decisions/ADR-P16.md; 04-information/spatial-model.md; 13-verification/acceptance/SLC-02/invariants-slc02.md |
| REQ-INF-030 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/queries-slc02.md; 04-information/spatial-model.md; 05-contracts/openapi-information-slc02.md; 13-verification/acceptance/SLC-02/invariants-slc02.m ...(truncated) |
| REQ-INF-031 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 2 | 04-information/language-model.md; 13-verification/acceptance/SLC-02/invariants-slc02.md |
| REQ-INF-032 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md;15-traceability/trace-slc04.md | 11 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/candidate-generation.md; 03-domain/contexts/BC02/queries-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 03-domain/contexts/BC02/aggr ...(truncated) |
| REQ-INF-033 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md;15-traceability/trace-slc04.md;16-reports/CONSISTENCY-CHECK-W3.md | 9 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/queries-slc04.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 04-information/entity-resolution.md; 05-contracts/openapi-information-slc04.m ...(truncated) |
| REQ-INF-034 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md;15-traceability/trace-slc04.md;16-reports/CONSISTENCY-CHECK-W3.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md; 04-information/entity-resolution.md; 13-verification/acceptance/SLC-04/er-case-state-machine.md; 13-verification/accept ...(truncated) |
| REQ-INF-035 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md;15-traceability/trace-slc07.md | 11 | 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md; 03-domain/contexts/BC03/aggregates/AGG-FINDI ...(truncated) |
| REQ-INF-036 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 8 | 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md; 03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md; 05-contracts/openapi-information-slc02.md; 13-verific ...(truncated) |
| REQ-INF-037 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc02.md | 6 | 01-business/business-rules.md; 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md; 04-information/claim-evidence-model.md; 13-verification/acceptance/SLC-02/claim-state-machine.md; 13-verification/accept ...(truncated) |
| REQ-INT-001 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc16.md | 9 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 03-domain/contexts/BC07/queries-slc16.md; 03-domain/contexts/BC07/aggregates ...(truncated) |
| REQ-INT-002 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc16.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 03-domain/contexts/BC07/queries-slc16.md; 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md; 05-contracts/op ...(truncated) |
| REQ-INT-003 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc16.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/queries-slc16.md; 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 05-contracts/open ...(truncated) |
| REQ-INT-004 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc16.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/queries-slc16.md; 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 05-contracts ...(truncated) |
| REQ-KNW-001 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/queries-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md; 05-contr ...(truncated) |
| REQ-KNW-002 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 12 | 00-governance/registers/corrections.md; 02-requirements/use-cases.md; 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC06/commands-slc12.md; 03-domain/contexts/BC06/products-kno ...(truncated) |
| REQ-KNW-003 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 9 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/queries-slc12.md; 03-domain/contexts/BC06/aggreg ...(truncated) |
| REQ-LOG-001 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 5 | 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 13-verification/acceptance/SLC-18/invariants-slc18.md; 13-verification/acceptance/SLC-18/logisti ...(truncated) |
| REQ-LOG-002 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 6 | 02-requirements/quality-scenarios.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 13-verification/acceptance/SLC-18/invariants-slc18.md; 13- ...(truncated) |
| REQ-LOG-003 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 5 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 13-verification/acceptance/SLC-18/invariants-slc18.md; 13-verification/acceptance/SLC-18/logistics-request-state-machine.md; 13-verificatio ...(truncated) |
| REQ-LOG-004 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 5 | 02-requirements/quality-scenarios.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 13-verification/acceptance/SLC-18/invariants-slc18.md; 13-verification/acceptance/SLC-18/shipment-state-machin ...(truncated) |
| REQ-LOG-005 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 13-verification/acceptance/SLC-18/shipment-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-LOG-006 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 4 | 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 13-verification/acceptance/SLC-18/invariants-slc18.md; 13-verification/acceptance/SLC-18/shipment-state-machine.md; 13-verification/tooling/slice-so ...(truncated) |
| REQ-LOG-007 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 13-verification/acceptance/SLC-18/shipment-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-LOG-008 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 5 | 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 13-verification/acceptance/SLC-18/invariants-slc18.md; 13-verification/acceptance/SLC-18/logisti ...(truncated) |
| REQ-LOG-009 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 6 | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md; 13-verification/acceptance/SLC-18/invariants-slc18.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| REQ-LOG-010 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 3 | 03-domain/contexts/BC05/queries-slc18.md; 05-contracts/openapi-readiness-slc18.md; 13-verification/tooling/slice-sources.md |
| REQ-LOG-011 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 3 | 03-domain/contexts/BC05/queries-slc18.md; 05-contracts/openapi-readiness-slc18.md; 13-verification/tooling/slice-sources.md |
| REQ-LOG-012 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 3 | 03-domain/contexts/BC05/queries-slc18.md; 05-contracts/openapi-readiness-slc18.md; 13-verification/tooling/slice-sources.md |
| REQ-LOG-013 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 4 | 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 13-verification/acceptance/SLC-18/logistics-request-state-machine.md; 13-verification/tooling/sl ...(truncated) |
| REQ-LOG-014 | 02-requirements/requirements.md;15-traceability/trace-slc18.md | 4 | 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md; 13-verification/acceptance/SLC-18/logistics-request-state-machine.md; 13-verification/tooling/sl ...(truncated) |
| REQ-OFF-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc03.md;15-traceability/trace-slc11.md | 12 | 02-requirements/use-cases.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 03-domain/contexts/BC07/field-sync-protocol.md; 03-domain/contexts/BC07/q ...(truncated) |
| REQ-OFF-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc11.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/field-sync-protocol.md; 03-domain/contexts/BC07/queries-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md; 05-contracts/openapi- ...(truncated) |
| REQ-OFF-003 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc11.md | 7 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/field-sync-protocol.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md; 04-information/temporal-model.md; 13-verification/acceptance/SLC-1 ...(truncated) |
| REQ-OFF-004 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc11.md | 12 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/field-sync-protocol.md; 03-domain/contexts/BC07/queries-slc11.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md; 03-domain/contexts/BC07 ...(truncated) |
| REQ-OFF-005 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc11.md | 12 | 02-requirements/use-cases.md; 03-domain/ownership.md; 03-domain/contexts/BC01/queries-slc11.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 03-domain/contexts/BC07/field-sync-protocol.md; 03-dom ...(truncated) |
| REQ-OFF-006 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc11.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/field-sync-protocol.md; 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md; 13-verification/acceptance/SLC-11/invariants-slc11.md; 13-verifica ...(truncated) |
| REQ-OPS-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc08.md | 11 | 02-requirements/use-cases.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/queries-slc08.md; 03-domain/contexts/BC04/aggregates/AGG ...(truncated) |
| REQ-OPS-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc08.md | 7 | 02-requirements/use-cases.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN.md; 13-verification/acceptance/SLC-0 ...(truncated) |
| REQ-OPS-003 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc08.md | 11 | 01-business/business-rules.md; 02-requirements/use-cases.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/queries-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSIO ...(truncated) |
| REQ-OPS-004 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc08.md | 9 | 01-business/business-rules.md; 02-requirements/use-cases.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/queries-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSIO ...(truncated) |
| REQ-OPS-005 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md;15-traceability/trace-slc08.md | 12 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC ...(truncated) |
| REQ-OPS-006 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc03.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC04/queries-slc03.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 05-contracts/openapi-operations ...(truncated) |
| REQ-OPS-007 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc03.md | 10 | 01-business/business-rules.md; 02-requirements/use-cases.md; 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 03-domain/contexts/BC04/aggregates/AGG-TASK ...(truncated) |
| REQ-OPS-008 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc03.md | 7 | 01-business/business-rules.md; 02-requirements/use-cases.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 13-verification/acceptance/SLC-03/invarian ...(truncated) |
| REQ-OPS-009 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc01.md;15-traceability/trace-slc03.md | 9 | 02-requirements/use-cases.md; 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md; 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 08-security/authoriz ...(truncated) |
| REQ-OPS-010 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc03.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 09-reliability/observability-slc03.md; 09-reliability/observability-slc08.md; 1 ...(truncated) |
| REQ-OPS-011 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc03.md | 4 | 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 13-verification/acceptance/SLC-03/invariants-slc03.md; 13-verification/acceptance/SLC-03/task-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-OPS-012 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc03.md | 7 | 02-requirements/use-cases.md; 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/task-lifecycle-rules.md; 03-domain/contexts/BC04/aggregates/AGG-TASK.md; 13-verification/acceptance/SLC ...(truncated) |
| REQ-OPS-013 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc08.md | 9 | 02-requirements/use-cases.md; 03-domain/ownership.md; 03-domain/contexts/BC04/decision-plan-spec.md; 03-domain/contexts/BC04/queries-slc08.md; 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md ...(truncated) |
| REQ-OPS-014 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc03.md;15-traceability/trace-slc08.md | 10 | 02-requirements/use-cases.md; 03-domain/contexts/BC04/queries-slc03.md; 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md; 05-contracts/openap ...(truncated) |
| REQ-PLT-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 4 | 12-solution/release-configuration-migration.md; 12-solution/technology-decisions.md; 13-verification/fitness-functions.md; 15-traceability/trace-platform.md |
| REQ-PLT-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 3 | 12-solution/cell-architecture.md; 12-solution/release-configuration-migration.md; 15-traceability/trace-platform.md |
| REQ-PLT-003 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 1 | 15-traceability/trace-platform.md |
| REQ-PLT-004 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 3 | 09-reliability/dr-and-continuity.md; 15-traceability/trace-platform.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| REQ-PLT-005 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 2 | 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 15-traceability/trace-platform.md |
| REQ-PLT-006 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 29 | 03-domain/contexts/BC01/events-slc01.md; 03-domain/contexts/BC01/events-slc11.md; 03-domain/contexts/BC01/events-slc16.md; 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/events-slc04 ...(truncated) |
| REQ-PLT-007 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 32 | 05-contracts/openapi-ai-slc10.md; 05-contracts/openapi-discovery-slc05.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-foundation-internal-slc01.md; 05-contracts/openapi-foundation-slc01 ...(truncated) |
| REQ-PLT-008 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 30 | 05-contracts/openapi-ai-slc10.md; 05-contracts/openapi-discovery-slc05.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-foundation-internal-slc01.md; 05-contracts/openapi-foundation-slc01 ...(truncated) |
| REQ-PLT-009 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 30 | 05-contracts/openapi-ai-slc10.md; 05-contracts/openapi-discovery-slc05.md; 05-contracts/openapi-field-slc11.md; 05-contracts/openapi-foundation-internal-slc01.md; 05-contracts/openapi-foundation-slc01 ...(truncated) |
| REQ-PLT-010 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 4 | 04-information/language-model.md; 12-solution/technology-decisions.md; 12-solution/ui-architecture.md; 15-traceability/trace-platform.md |
| REQ-PLT-011 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 2 | 12-solution/ui-architecture.md; 15-traceability/trace-platform.md |
| REQ-PLT-012 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 2 | 09-reliability/dr-and-continuity.md; 15-traceability/trace-platform.md |
| REQ-PLT-013 | 02-requirements/requirements.md;15-traceability/rtm-r1.md | 3 | 07-quality/cost-model.md; 12-solution/technology-decisions.md; 15-traceability/trace-platform.md |
| REQ-PRD-001 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 11 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/queries-slc12.md; 03-domain/contexts/BC06/aggreg ...(truncated) |
| REQ-PRD-002 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 7 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 13-verification/accep ...(truncated) |
| REQ-PRD-003 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/queries-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md; 05-contracts/open ...(truncated) |
| REQ-PRD-004 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/queries-slc12.md; 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md; 05-contracts ...(truncated) |
| REQ-PRD-005 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc12.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC06/products-knowledge-archive-spec.md; 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md; 13-verification/acceptance/SLC-12/distribution-state-m ...(truncated) |
| REQ-QUALITY-R2 | 16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md | 0 |  |
| REQ-QUALITY-REPORT | 16-reports/REQUIREMENTS-QUALITY-REPORT.md | 0 |  |
| REQ-RCM-001 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 4 | 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 13-verification/acceptance/SLC-17/risk-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-RCM-002 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 4 | 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 13-verification/acceptance/SLC-17/invariants-slc17.md; 13-verification/acceptance/SLC-17/risk-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-RCM-003 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 4 | 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 13-verification/acceptance/SLC-17/invariants-slc17.md; 13-verification/acceptance/SLC-17/risk-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-RCM-004 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 5 | 02-requirements/quality-scenarios.md; 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 13-verification/acceptance/SLC-17/invariants-slc17.md; 13-verification/acceptance/SLC-17/risk-state-machine.md; 13 ...(truncated) |
| REQ-RCM-005 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 4 | 03-domain/contexts/BC04/aggregates/AGG-RISK.md; 13-verification/acceptance/SLC-17/invariants-slc17.md; 13-verification/acceptance/SLC-17/risk-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-RCM-006 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 13-verification/acceptance/SLC-17/incident-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-RCM-007 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 13-verification/acceptance/SLC-17/incident-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-RCM-008 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 3 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 13-verification/acceptance/SLC-17/incident-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-RCM-009 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 6 | 02-requirements/quality-scenarios.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 13-verification/acceptance/SLC-17/incident-state-machine.md; ...(truncated) |
| REQ-RCM-010 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 4 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 13-verification/acceptance/SLC-17/incident-state-machine.md; 13-verification/acceptance/SLC-17/invariants-slc17.md; 13-verification/tooling/slice-so ...(truncated) |
| REQ-RCM-011 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 5 | 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 13-verification/acceptance/SLC-17/incident-state-machine.md; 13-verification/acceptance/SLC-17/inv ...(truncated) |
| REQ-RCM-012 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 4 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 13-verification/acceptance/SLC-17/incident-state-machine.md; 13-verification/acceptance/SLC-17/invariants-slc17.md; 13-verification/tooling/slice-so ...(truncated) |
| REQ-RCM-013 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 4 | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 13-verification/acceptance/SLC-17/incident-state-machine.md; 13-verification/acceptance/SLC-17/invariants-slc17.md; 13-verification/tooling/slice-so ...(truncated) |
| REQ-RCM-014 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 3 | 03-domain/contexts/BC04/queries-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/tooling/slice-sources.md |
| REQ-RCM-015 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 3 | 03-domain/contexts/BC04/queries-slc17.md; 05-contracts/openapi-operations-slc17.md; 13-verification/tooling/slice-sources.md |
| REQ-RCM-016 | 02-requirements/requirements.md;15-traceability/trace-slc17.md | 4 | 03-domain/contexts/BC04/queries-slc17.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 05-contracts/openapi-operations-slc17.md; 13-verification/tooling/slice-sources.md |
| REQ-RDY-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc03.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/eligibility-rules.md; 03-domain/contexts/BC05/queries-slc03.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/opena ...(truncated) |
| REQ-RDY-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc03.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/eligibility-rules.md; 03-domain/contexts/BC05/queries-slc03.md; 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md; 05-contracts/opena ...(truncated) |
| REQ-RES-001 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 7 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/queries-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 05-contracts/openapi-readiness-slc09.md; 13-verification/acceptance/SLC-09/asse ...(truncated) |
| REQ-RES-002 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 5 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 13-verification/acceptance/SLC-09/asset-state-machine.md; 13-verification/acceptance/SLC-09/invariants-slc09.md; 13-verif ...(truncated) |
| REQ-RES-003 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 10 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/queries-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md; 03-domain/cont ...(truncated) |
| REQ-RES-004 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/queries-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md; 05-contracts/ ...(truncated) |
| REQ-RES-005 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 5 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET.md; 13-verification/acceptance/SLC-09/asset-state-machine.md; 13-verification/acceptance/SLC-09/invariants-slc09.md; 13-verif ...(truncated) |
| REQ-RES-006 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 9 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/queries-slc09.md; 03-domain/contexts/BC05/aggregates/A ...(truncated) |
| REQ-RES-007 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/queries-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 05-contracts/openapi ...(truncated) |
| REQ-RES-008 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 7 | 02-requirements/quality-scenarios.md; 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 13-verification/acceptan ...(truncated) |
| REQ-RES-009 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 8 | 00-governance/glossary.md; 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCAT ...(truncated) |
| REQ-RES-010 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 7 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 13-verification/acc ...(truncated) |
| REQ-RES-011 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 13-verification/acceptance/SLC-09/allocation-state-machine.md; ...(truncated) |
| REQ-RES-012 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md; 13 ...(truncated) |
| REQ-RES-013 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/queries-slc09.md; 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md; 05-contracts/o ...(truncated) |
| REQ-RES-014 | 02-requirements/requirements.md;15-traceability/rtm-r2.md;15-traceability/trace-slc09.md | 7 | 02-requirements/use-cases.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md; 13-verification/acceptance/SLC-09/asset-reservation-sta ...(truncated) |
| REQ-SIT-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc06.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/queries-slc06.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/openapi-in ...(truncated) |
| REQ-SIT-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc06.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/queries-slc06.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/openapi-in ...(truncated) |
| REQ-SIT-003 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc06.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/queries-slc06.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 05-contracts/openapi-in ...(truncated) |
| REQ-SIT-004 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc06.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 13-verification ...(truncated) |
| REQ-SIT-005 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc06.md | 9 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/queries-slc06.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 03-domain/contexts/BC03/aggregate ...(truncated) |
| REQ-SIT-006 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc06.md | 7 | 01-business/business-rules.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 03-domain/contexts/BC03/aggregates/AGG-ALERT.md; 13-verification/acceptance/SLC-06/alert-state-machine.md; 13-verific ...(truncated) |
| REQ-SIT-007 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc06.md | 8 | 02-requirements/use-cases.md; 03-domain/contexts/BC03/queries-slc06.md; 03-domain/contexts/BC03/situation-alerting-spec.md; 04-information/spatial-model.md; 05-contracts/openapi-intelligence-slc06.md; ...(truncated) |
| REQ-SRC-001 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc05.md | 6 | 02-requirements/use-cases.md; 03-domain/contexts/BC07/discovery-architecture.md; 03-domain/contexts/BC07/queries-slc05.md; 05-contracts/openapi-discovery-slc05.md; 13-verification/acceptance/SLC-05/in ...(truncated) |
| REQ-SRC-002 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc05.md | 4 | 01-business/business-rules.md; 02-requirements/use-cases.md; 03-domain/contexts/BC07/discovery-architecture.md; 13-verification/acceptance/SLC-05/invariants-slc05.md |
| REQ-SRC-003 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc04.md;15-traceability/trace-slc05.md | 11 | 02-requirements/use-cases.md; 03-domain/contexts/BC02/candidate-generation.md; 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md; 03-domain/contexts/BC07/discovery-architecture.md; 03-domain/con ...(truncated) |
| REQ-SRC-004 | 02-requirements/requirements.md;15-traceability/rtm-r1.md;15-traceability/trace-slc05.md | 8 | 03-domain/contexts/BC07/discovery-architecture.md; 03-domain/contexts/BC07/queries-slc05.md; 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md; 05-contracts/openapi-discovery-slc05.md; 13-v ...(truncated) |
| REQ-TRX-001 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 4 | 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 13-verification/acceptance/SLC-19/scenario-state-machine.md; 13-verification/tooling/slice-source ...(truncated) |
| REQ-TRX-002 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 4 | 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md; 13-verification/acceptance/SLC-19/invariants-slc19.md; 13-verification/acceptance/SLC-19/scenario-state-machine.md; 13-verification/tooling/slice-so ...(truncated) |
| REQ-TRX-003 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 5 | 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 13-verification/acceptance/SLC-19/exercise-state-machine.md; 13-verification/acceptance/SLC-19/in ...(truncated) |
| REQ-TRX-004 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 13-verification/acceptance/SLC-19/exercise-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-TRX-005 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 5 | 03-domain/contexts/BC05/training-exercise-spec.md; 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 13-verification/acceptance/SLC-19/exercise-state-machine.md; 13-verification/acceptance/SLC-19/in ...(truncated) |
| REQ-TRX-006 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 4 | 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 13-verification/acceptance/SLC-19/exercise-state-machine.md; 13-verification/acceptance/SLC-19/invariants-slc19.md; 13-verification/tooling/slice-so ...(truncated) |
| REQ-TRX-007 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md; 13-verification/acceptance/SLC-19/exercise-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-TRX-008 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 4 | 02-requirements/quality-scenarios.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 13-verification/acceptance/SLC-19/simulation-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-TRX-009 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 13-verification/acceptance/SLC-19/simulation-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-TRX-010 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 5 | 02-requirements/quality-scenarios.md; 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 13-verification/acceptance/SLC-19/invariants-slc19.md; 13-verification/acceptance/SLC-19/simulation-state-ma ...(truncated) |
| REQ-TRX-011 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 3 | 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md; 13-verification/acceptance/SLC-19/simulation-state-machine.md; 13-verification/tooling/slice-sources.md |
| REQ-TRX-012 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 2 | 03-domain/contexts/BC05/training-exercise-spec.md; 13-verification/acceptance/SLC-19/invariants-slc19.md |
| REQ-TRX-013 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 2 | 03-domain/contexts/BC05/training-exercise-spec.md; 13-verification/acceptance/SLC-19/invariants-slc19.md |
| REQ-TRX-014 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 3 | 03-domain/contexts/BC05/queries-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/tooling/slice-sources.md |
| REQ-TRX-015 | 02-requirements/requirements.md;15-traceability/trace-slc19.md | 3 | 03-domain/contexts/BC05/queries-slc19.md; 05-contracts/openapi-readiness-slc19.md; 13-verification/tooling/slice-sources.md |

### Family: RSK

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| RSK-001 | 00-governance/registers/risks.md | 2 | 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md |
| RSK-002 | 00-governance/registers/risks.md | 2 | 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md |
| RSK-003 | 00-governance/registers/risks.md | 2 | 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md |
| RSK-004 | 00-governance/registers/risks.md | 0 |  |
| RSK-005 | 00-governance/registers/risks.md | 1 | 16-reports/ARCHITECTURE-REVIEW-R1.md |
| RSK-006 | 00-governance/registers/risks.md | 2 | 16-reports/ARCHITECTURE-REVIEW-R1.md; 16-reports/ARCHITECTURE-REVIEW-R2.md |
| RSK-007 | 00-governance/registers/risks.md | 2 | 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md |
| RSK-008 | 00-governance/registers/risks.md | 2 | 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md |
| RSK-009 | 00-governance/registers/risks.md | 1 | 16-reports/EVOLUTION-ROADMAP.md |
| RSK-010 | 00-governance/registers/risks.md | 2 | 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md |
| RSK-011 | 00-governance/registers/risks.md | 0 |  |
| RSK-012 | 00-governance/registers/risks.md | 0 |  |
| RSK-013 | 00-governance/registers/risks.md | 3 | 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/SESSION-W1.md |
| RSK-014 | 00-governance/registers/risks.md | 0 |  |
| RSK-015 | 00-governance/registers/risks.md | 2 | 14-slices/SLC-10/atam-lite.md; 16-reports/ARCHITECTURE-REVIEW-R2.md |
| RSK-016 | 00-governance/registers/risks.md | 0 |  |
| RSK-017 | 00-governance/registers/risks.md | 3 | 04-information/entity-resolution.md; 14-slices/SLC-04/atam-lite.md; 16-reports/SESSION-W3.md |
| RSK-018 | 00-governance/registers/risks.md;14-slices/SLC-01/atam-lite.md | 4 | 16-reports/ARCHITECTURE-REVIEW-R1.md; 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/SESSION-W3.md |
| RSK-019 | 00-governance/registers/risks.md | 6 | 03-domain/contexts/BC02/claims-temporal-kernel.md; 14-slices/SLC-02/atam-lite.md; 16-reports/ARCHITECTURE-REVIEW-R1.md; 16-reports/SESSION-W3.md; 16-reports/SESSION-W4-W7-SLC01.md; 16-reports/SESSION- ...(truncated) |
| RSK-020 | 00-governance/registers/risks.md | 4 | 14-slices/SLC-02/atam-lite.md; 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/SESSION-W4-W7-SLC02.md |
| RSK-021 | 00-governance/registers/risks.md | 6 | 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md; 13-verification/tooling/slice-sources.md; 14-slices/SLC-04/atam-lite.md; 16-reports/ARCHITECTURE-REVIEW-R1.md; 16-reports/ARCHITECTURE-REVIEW-R2.m ...(truncated) |
| RSK-022 | 00-governance/registers/risks.md | 3 | 12-solution/technology-decisions.md; 14-slices/SLC-05/atam-lite.md; 16-reports/SESSION-W4-W7-SLC05.md |
| RSK-023 | 00-governance/registers/risks.md | 3 | 12-solution/w8-inputs.md; 14-slices/SLC-06/atam-lite.md; 16-reports/SESSION-W4-W7-SLC06.md |
| RSK-024 | 00-governance/registers/risks.md | 2 | 14-slices/SLC-07/atam-lite.md; 16-reports/SESSION-W4-W7-SLC07.md |
| RSK-025 | 00-governance/registers/risks.md | 5 | 14-slices/SLC-12a/atam-lite.md; 16-reports/ARCHITECTURE-REVIEW-R1.md; 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/SESSION-W4-W7-SLC12a.md |
| RSK-026 | 00-governance/registers/risks.md | 7 | 00-governance/RATIFICATION-PACKAGE.md; 00-governance/registers/assumptions.md; 16-reports/ARCHITECTURE-REVIEW-R1.md; 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-report ...(truncated) |
| RSK-027 | 00-governance/registers/risks.md | 28 | README.md; 01-business/release-2-scope.md; 01-business/release-3-scope.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC07/grou ...(truncated) |
| RSK-028 | 00-governance/registers/risks.md | 22 | README.md; 01-business/release-3-scope.md; 02-requirements/quality-scenarios.md; 03-domain/contexts/BC04/risk-contingency-spec.md; 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md; 03-domain/context ...(truncated) |

### Family: RTM

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| RTM-R1 | 15-traceability/rtm-r1.md | 2 | 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/IMPLEMENTATION-READINESS-R1.md |
| RTM-R2 | 15-traceability/rtm-r2.md | 0 |  |

### Family: SCALE

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| SCALE-ENVELOPE | 07-quality/scale-envelope.md | 0 |  |

### Family: SESSION

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| SESSION-R2-BASELINE | 16-reports/SESSION-R2-BASELINE.md | 0 |  |
| SESSION-SLC01 | 16-reports/SESSION-W4-W7-SLC01.md | 0 |  |
| SESSION-SLC02 | 16-reports/SESSION-W4-W7-SLC02.md | 0 |  |
| SESSION-SLC03 | 16-reports/SESSION-W4-W7-SLC03.md | 0 |  |
| SESSION-SLC04 | 16-reports/SESSION-W4-W7-SLC04.md | 0 |  |
| SESSION-SLC05 | 16-reports/SESSION-W4-W7-SLC05.md | 0 |  |
| SESSION-SLC06 | 16-reports/SESSION-W4-W7-SLC06.md | 0 |  |
| SESSION-SLC07 | 16-reports/SESSION-W4-W7-SLC07.md | 0 |  |
| SESSION-SLC08 | 16-reports/SESSION-W4-W7-SLC08.md | 0 |  |
| SESSION-SLC09 | 16-reports/SESSION-W4-W7-SLC09.md | 0 |  |
| SESSION-SLC10 | 16-reports/SESSION-W4-W7-SLC10.md | 0 |  |
| SESSION-SLC11 | 16-reports/SESSION-W4-W7-SLC11.md | 0 |  |
| SESSION-SLC12 | 16-reports/SESSION-W4-W7-SLC12.md | 0 |  |
| SESSION-SLC12A | 16-reports/SESSION-W4-W7-SLC12a.md | 0 |  |
| SESSION-SLC14 | 16-reports/SESSION-W4-W7-SLC14.md | 0 |  |
| SESSION-SLC15 | 16-reports/SESSION-W4-W7-SLC15.md | 0 |  |
| SESSION-SLC16 | 16-reports/SESSION-W4-W7-SLC16.md | 0 |  |
| SESSION-SLC17 | 16-reports/SESSION-W4-W7-SLC17.md | 0 |  |
| SESSION-SLC18 | 16-reports/SESSION-W4-W7-SLC18.md | 0 |  |
| SESSION-SLC19 | 16-reports/SESSION-W4-W7-SLC19.md | 0 |  |
| SESSION-W0 | 16-reports/SESSION-W0.md | 0 |  |
| SESSION-W1 | 16-reports/SESSION-W1.md | 0 |  |
| SESSION-W2 | 16-reports/SESSION-W2.md | 1 | 00-governance/RATIFICATION-PACKAGE.md |
| SESSION-W2-R2 | 16-reports/SESSION-W2-R2.md | 0 |  |
| SESSION-W3 | 16-reports/SESSION-W3.md | 0 |  |
| SESSION-W8 | 16-reports/SESSION-W8.md | 0 |  |
| SESSION-W9 | 16-reports/SESSION-W9.md | 0 |  |

### Family: SH

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| SH-01 | 01-business/stakeholders.md | 0 |  |
| SH-02 | 01-business/stakeholders.md | 0 |  |
| SH-03 | 01-business/stakeholders.md | 0 |  |
| SH-04 | 01-business/stakeholders.md | 0 |  |
| SH-05 | 01-business/stakeholders.md | 0 |  |

### Family: SL

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| SL-01 | 13-verification/spec-lint-rules.md;16-reports/SESSION-W0.md;16-reports/SESSION-W1.md;16-reports/SESSION-W2.md;16-reports/SESSION-W3.md | 6 | 03-domain/ownership.md; 13-verification/tooling/spec-tooling.md; 14-slices/SLC-01/readiness.md; 16-reports/CONSISTENCY-CHECK-W3.md; 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/gate-reports/GATE-ST ...(truncated) |
| SL-02 | 13-verification/spec-lint-rules.md | 4 | 08-security/policies-slc01.md; 13-verification/tooling/spec-tooling.md; 14-slices/SLC-01/readiness.md; 14-slices/SLC-02/readiness.md |
| SL-03 | 13-verification/spec-lint-rules.md | 4 | 13-verification/tooling/spec-tooling.md; 14-slices/SLC-01/readiness.md; 14-slices/SLC-02/readiness.md; 16-reports/CONSISTENCY-REPORT-R1.md |
| SL-04 | 13-verification/spec-lint-rules.md | 3 | 13-verification/tooling/spec-tooling.md; 14-slices/SLC-01/readiness.md; 14-slices/SLC-02/readiness.md |
| SL-05 | 13-verification/spec-lint-rules.md | 185 | 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 03-domain/contexts/BC01/aggregates/AGG ...(truncated) |
| SL-06 | 13-verification/spec-lint-rules.md;14-slices/SLC-02/readiness.md | 92 | 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md; 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md; 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 03-domain/contexts/BC01/aggregates/AGG ...(truncated) |
| SL-07 | 13-verification/spec-lint-rules.md;14-slices/SLC-02/readiness.md | 2 | 13-verification/tooling/spec-tooling.md; 14-slices/SLC-01/readiness.md |
| SL-08 | 13-verification/spec-lint-rules.md | 1 | 14-slices/SLC-01/readiness.md |
| SL-09 | 13-verification/spec-lint-rules.md;14-slices/SLC-02/readiness.md | 29 | 03-domain/contexts/BC01/queries-slc01.md; 03-domain/contexts/BC01/queries-slc11.md; 03-domain/contexts/BC01/queries-slc16.md; 03-domain/contexts/BC02/queries-slc02.md; 03-domain/contexts/BC02/queries- ...(truncated) |
| SL-10 | 13-verification/spec-lint-rules.md | 3 | 00-governance/decisions/ADR-P03.md; 13-verification/fitness-functions.md; 14-slices/SLC-02/readiness.md |
| SL-11 | 13-verification/spec-lint-rules.md | 6 | 02-requirements/requirements.md; 04-information/temporal-model.md; 13-verification/fitness-functions.md; 14-slices/SLC-02/readiness.md; 16-reports/ANTI-PATTERN-REPORT-R1.md; 16-reports/CONSISTENCY-CHE ...(truncated) |
| SL-12 | 13-verification/spec-lint-rules.md | 3 | 02-requirements/requirements.md; 13-verification/fitness-functions.md; 14-slices/SLC-02/readiness.md |
| SL-13 | 13-verification/spec-lint-rules.md | 0 |  |
| SL-14 | 13-verification/spec-lint-rules.md | 0 |  |
| SL-15 | 13-verification/spec-lint-rules.md;16-reports/SESSION-W0.md;16-reports/SESSION-W1.md;16-reports/SESSION-W2.md | 3 | 13-verification/tooling/spec-tooling.md; 16-reports/SESSION-W3.md; 16-reports/gate-reports/GATE-STATUS-W0.md |
| SL-16 | 13-verification/spec-lint-rules.md;16-reports/SESSION-W2.md | 1 | 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| SL-17 | 13-verification/spec-lint-rules.md | 1 | 14-slices/SLC-01/readiness.md |
| SL-18 | 13-verification/spec-lint-rules.md | 1 | 14-slices/SLC-01/readiness.md |
| SL-19 | 13-verification/spec-lint-rules.md;16-reports/SESSION-W0.md;16-reports/SESSION-W1.md | 2 | 13-verification/tooling/spec-tooling.md; 16-reports/SESSION-W3.md |
| SL-20 | 13-verification/spec-lint-rules.md;16-reports/SESSION-W0.md;16-reports/SESSION-W1.md;16-reports/SESSION-W2.md;16-reports/SESSION-W3.md | 4 | 13-verification/tooling/spec-tooling.md; 14-slices/SLC-01/readiness.md; 16-reports/CONSISTENCY-CHECK-W3.md; 16-reports/CONSISTENCY-REPORT-R1.md |
| SL-21 | 13-verification/spec-lint-rules.md | 0 |  |
| SL-22 | 13-verification/spec-lint-rules.md | 1 | 14-slices/SLC-01/readiness.md |
| SL-23 | 13-verification/spec-lint-rules.md | 0 |  |
| SL-24 | 13-verification/spec-lint-rules.md | 7 | 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md; 13-verification/fitness-functions.md; 13-verification/tooling/slice-sources.md; 13-verification/tooling/spec-tooling.md; 14-slices/SLC-01/readin ...(truncated) |
| SL-25 | 13-verification/spec-lint-rules.md | 0 |  |
| SL-26 | 13-verification/spec-lint-rules.md | 2 | 00-governance/glossary.md; 00-governance/registers/risks.md |
| SL-27 | 13-verification/spec-lint-rules.md | 0 |  |
| SL-28 | 13-verification/spec-lint-rules.md;14-slices/SLC-01/readiness.md | 2 | 02-requirements/quality-scenarios.md; 02-requirements/requirements.md |
| SL-29 | 13-verification/spec-lint-rules.md | 5 | 00-governance/registers/corrections.md; 08-security/label-derivation-rules.md; 15-traceability/trace-platform.md; 16-reports/CONSISTENCY-REPORT-R1.md; 16-reports/SESSION-W4-W7-SLC12a.md |

### Family: SLC

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| SLC-00 | 14-slices/slices.md | 3 | 16-reports/SESSION-W3.md; 16-reports/SLC-00-WALKTHROUGH.md; 16-reports/gate-reports/GATE-STATUS-W3.md |
| SLC-00-WALKTHROUGH | 16-reports/SLC-00-WALKTHROUGH.md | 0 |  |
| SLC-01 | 00-governance/RATIFICATION-PACKAGE.md;12-solution/w8-inputs.md;14-slices/slices.md;14-slices/SLC-03/readiness.md;16-reports/SESSION-W4-W7-SLC12a.md | 79 | 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 01-business/system-definition.md; 02-requirements/quality-scenarios.md; 02-requirements/requirements.md; 03-domain/c ...(truncated) |
| SLC-01..04 | 14-slices/SLC-05/readiness.md | 3 | 03-domain/contexts/BC07/discovery-architecture.md; 16-reports/SESSION-W4-W7-SLC03.md; 16-reports/gate-reports/GATE-STATUS-SLC05.md |
| SLC-02 | 00-governance/RATIFICATION-PACKAGE.md;12-solution/w8-inputs.md;14-slices/slices.md;16-reports/SESSION-W4-W7-SLC12a.md | 83 | 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/risks.md; 02-requirements/quality-scenarios.md; 03-domain/contexts/BC02/claims-temporal-kern ...(truncated) |
| SLC-03 | 00-governance/RATIFICATION-PACKAGE.md;12-solution/w8-inputs.md;14-slices/slices.md;16-reports/SESSION-W4-W7-SLC12a.md | 92 | README.md; 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 01-business/release-3-scope.md; 02-requirements/quality-scenarios.md; 02-requirements/requirements.md; 03 ...(truncated) |
| SLC-04 | 00-governance/RATIFICATION-PACKAGE.md;12-solution/w8-inputs.md;14-slices/slices.md;16-reports/SESSION-W4-W7-SLC12a.md | 57 | 00-governance/registers/human-approvals.md; 00-governance/registers/open-questions.md; 02-requirements/quality-scenarios.md; 03-domain/contexts/BC02/candidate-generation.md; 03-domain/contexts/BC02/cl ...(truncated) |
| SLC-05 | 00-governance/RATIFICATION-PACKAGE.md;12-solution/w8-inputs.md;14-slices/slices.md;16-reports/SESSION-W4-W7-SLC12a.md | 71 | 00-governance/decisions/ADR-P06.md; 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 02-requirements/quality-scenarios.md; 03-domain/contexts/BC02/claims-temporal-ke ...(truncated) |
| SLC-06 | 00-governance/RATIFICATION-PACKAGE.md;12-solution/w8-inputs.md;14-slices/slices.md;16-reports/SESSION-W4-W7-SLC12a.md | 55 | 00-governance/registers/human-approvals.md; 02-requirements/quality-scenarios.md; 03-domain/contexts/BC02/events-slc02.md; 03-domain/contexts/BC02/events-slc04.md; 03-domain/contexts/BC03/commands-slc ...(truncated) |
| SLC-07 | 00-governance/RATIFICATION-PACKAGE.md;12-solution/w8-inputs.md;14-slices/slices.md;16-reports/SESSION-W4-W7-SLC12a.md | 42 | 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 02-requirements/quality-scenarios.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/B ...(truncated) |
| SLC-08 | 00-governance/RATIFICATION-PACKAGE.md;14-slices/slices.md;16-reports/SESSION-W4-W7-SLC12a.md | 69 | 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 01-business/release-3-scope.md; 01-business/system-definition.md; 02-requirements/quality-scenarios.md; 02-requireme ...(truncated) |
| SLC-09 | 14-slices/slices.md;16-reports/EVOLUTION-ROADMAP.md | 81 | README.md; 00-governance/registers/corrections.md; 00-governance/registers/technical-debt.md; 01-business/release-2-scope.md; 01-business/release-3-scope.md; 01-business/system-definition.md; 02-requi ...(truncated) |
| SLC-10 | 14-slices/slices.md;16-reports/EVOLUTION-ROADMAP.md | 49 | 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/risks.md; 01-business/release-2-scope.md; 01-business/system-definition.md; 03-domain/contex ...(truncated) |
| SLC-11 | 00-governance/RATIFICATION-PACKAGE.md;12-solution/w8-inputs.md;14-slices/slices.md;16-reports/SESSION-W4-W7-SLC12a.md | 59 | 00-governance/decisions/ADR-P09.md; 00-governance/registers/corrections.md; 00-governance/registers/human-approvals.md; 00-governance/registers/unknowns.md; 01-business/system-definition.md; 02-requir ...(truncated) |
| SLC-12 | 00-governance/RATIFICATION-PACKAGE.md;14-slices/slices.md;16-reports/EVOLUTION-ROADMAP.md | 61 | 00-governance/registers/corrections.md; 01-business/release-2-scope.md; 01-business/release-3-scope.md; 01-business/system-definition.md; 02-requirements/use-cases.md; 03-domain/contexts/BC02/correlat ...(truncated) |
| SLC-13 | 14-slices/slices.md | 2 | 01-business/system-definition.md; 02-requirements/use-cases.md |
| SLC-14 | 14-slices/slices.md | 32 | 00-governance/registers/corrections.md; 01-business/release-2-scope.md; 03-domain/contexts/BC02/collection-spec.md; 03-domain/contexts/BC02/commands-slc14.md; 03-domain/contexts/BC02/events-slc14.md;  ...(truncated) |
| SLC-15 | 14-slices/slices.md | 40 | 01-business/release-2-scope.md; 03-domain/contexts/BC02/commands-slc15.md; 03-domain/contexts/BC02/correlation-fusion-spec.md; 03-domain/contexts/BC02/events-slc15.md; 03-domain/contexts/BC02/queries- ...(truncated) |
| SLC-16 | 14-slices/slices.md | 48 | 00-governance/registers/unknowns.md; 01-business/release-2-scope.md; 03-domain/contexts/BC01/commands-slc16.md; 03-domain/contexts/BC01/events-slc16.md; 03-domain/contexts/BC01/queries-slc16.md; 03-do ...(truncated) |
| SLC-17 | 14-slices/slices.md | 41 | README.md; 00-governance/registers/corrections.md; 00-governance/registers/unknowns.md; 01-business/release-3-scope.md; 03-domain/contexts/BC04/commands-slc03.md; 03-domain/contexts/BC04/commands-slc0 ...(truncated) |
| SLC-18 | 14-slices/slices.md | 38 | README.md; 00-governance/registers/corrections.md; 01-business/release-3-scope.md; 03-domain/contexts/BC05/commands-slc09.md; 03-domain/contexts/BC05/commands-slc18.md; 03-domain/contexts/BC05/events- ...(truncated) |
| SLC-19 | 14-slices/slices.md | 30 | README.md; 00-governance/registers/corrections.md; 01-business/release-3-scope.md; 03-domain/contexts/BC05/commands-slc19.md; 03-domain/contexts/BC05/events-slc19.md; 03-domain/contexts/BC05/queries-s ...(truncated) |

### Family: SLICE

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| SLICE-SOURCES | 13-verification/tooling/slice-sources.md | 0 |  |

### Family: SM

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| SM-ADAPTER | 03-domain/contexts/BC07/aggregates/AGG-ADAPTER.md | 0 |  |
| SM-AI-REQUEST | 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md | 0 |  |
| SM-AI-RESULT | 03-domain/contexts/BC07/aggregates/AGG-AI-RESULT.md | 0 |  |
| SM-AI-ROUTING | 03-domain/contexts/BC07/aggregates/AGG-AI-ROUTING.md | 0 |  |
| SM-AI-TOOL | 03-domain/contexts/BC07/aggregates/AGG-AI-TOOL.md | 0 |  |
| SM-ALERT | 03-domain/contexts/BC03/aggregates/AGG-ALERT.md | 0 |  |
| SM-ALERT-RULE | 03-domain/contexts/BC03/aggregates/AGG-ALERT-RULE.md | 0 |  |
| SM-ALLOCATION | 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md | 0 |  |
| SM-ANALYSIS-CASE | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md | 0 |  |
| SM-ANALYSIS-METHOD | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-METHOD.md | 0 |  |
| SM-ANALYSIS-RUN | 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-RUN.md | 0 |  |
| SM-ARCHIVE-PACKAGE | 03-domain/contexts/BC06/aggregates/AGG-ARCHIVE-PACKAGE.md | 0 |  |
| SM-ASSESSMENT | 03-domain/contexts/BC03/aggregates/AGG-ASSESSMENT.md | 0 |  |
| SM-ASSET | 03-domain/contexts/BC05/aggregates/AGG-ASSET.md | 0 |  |
| SM-ASSET-ASSIGNMENT | 03-domain/contexts/BC05/aggregates/AGG-ASSET-ASSIGNMENT.md | 0 |  |
| SM-ASSET-RESERVATION | 03-domain/contexts/BC05/aggregates/AGG-ASSET-RESERVATION.md | 0 |  |
| SM-ATTACHMENT | 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md | 0 |  |
| SM-AUTHORITY-GRANT | 03-domain/contexts/BC01/aggregates/AGG-AUTHORITY-GRANT.md | 0 |  |
| SM-CAP-MESSAGE | 03-domain/contexts/BC03/aggregates/AGG-CAP-MESSAGE.md | 0 |  |
| SM-CLAIM | 03-domain/contexts/BC02/aggregates/AGG-CLAIM.md | 0 |  |
| SM-CLASSIFICATION-SCHEME | 03-domain/contexts/BC08/aggregates/AGG-CLASSIFICATION-SCHEME.md | 0 |  |
| SM-CLEARANCE | 03-domain/contexts/BC01/aggregates/AGG-CLEARANCE.md | 0 |  |
| SM-COLLECTION-PLAN | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-PLAN.md | 0 |  |
| SM-COLLECTION-REQUIREMENT | 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md | 0 |  |
| SM-CONFLICT | 03-domain/contexts/BC02/aggregates/AGG-CONFLICT.md | 0 |  |
| SM-COORDINATION-CASE | 03-domain/contexts/BC04/aggregates/AGG-COORDINATION-CASE.md | 0 |  |
| SM-CORRELATION-PROPOSAL | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-PROPOSAL.md | 0 |  |
| SM-CORRELATION-RULE | 03-domain/contexts/BC02/aggregates/AGG-CORRELATION-RULE.md | 0 |  |
| SM-DECISION | 03-domain/contexts/BC04/aggregates/AGG-DECISION.md | 0 |  |
| SM-DECISION-REQUEST | 03-domain/contexts/BC04/aggregates/AGG-DECISION-REQUEST.md | 0 |  |
| SM-DEVICE | 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md | 0 |  |
| SM-DISPOSITION-RUN | 03-domain/contexts/BC08/aggregates/AGG-DISPOSITION-RUN.md | 0 |  |
| SM-DISTRIBUTION | 03-domain/contexts/BC06/aggregates/AGG-DISTRIBUTION.md | 0 |  |
| SM-ENTITY | 03-domain/contexts/BC02/aggregates/AGG-ENTITY.md | 0 |  |
| SM-ERASURE-REQUEST | 03-domain/contexts/BC08/aggregates/AGG-ERASURE-REQUEST.md | 0 |  |
| SM-ER-CASE | 03-domain/contexts/BC02/aggregates/AGG-ER-CASE.md | 0 |  |
| SM-EVAL-SUITE | 03-domain/contexts/BC07/aggregates/AGG-EVAL-SUITE.md | 0 |  |
| SM-EVIDENCE | 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE.md | 0 |  |
| SM-EVIDENCE-LINK | 03-domain/contexts/BC02/aggregates/AGG-EVIDENCE-LINK.md | 0 |  |
| SM-EXERCISE | 03-domain/contexts/BC05/aggregates/AGG-EXERCISE.md | 0 |  |
| SM-EXTERNAL-ID | 03-domain/contexts/BC02/aggregates/AGG-EXTERNAL-ID.md | 0 |  |
| SM-FINDING | 03-domain/contexts/BC03/aggregates/AGG-FINDING.md | 0 |  |
| SM-HR-SYNC-PROPOSAL | 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md | 0 |  |
| SM-IMPORT-BATCH | 03-domain/contexts/BC02/aggregates/AGG-IMPORT-BATCH.md | 0 |  |
| SM-INCIDENT | 03-domain/contexts/BC04/aggregates/AGG-INCIDENT.md | 0 |  |
| SM-INTEGRATION-CONNECTION | 03-domain/contexts/BC07/aggregates/AGG-INTEGRATION-CONNECTION.md | 0 |  |
| SM-KNOWLEDGE-OBJECT | 03-domain/contexts/BC06/aggregates/AGG-KNOWLEDGE-OBJECT.md | 0 |  |
| SM-LEGAL-HOLD | 03-domain/contexts/BC08/aggregates/AGG-LEGAL-HOLD.md | 0 |  |
| SM-LOGISTICS-REQUEST | 03-domain/contexts/BC05/aggregates/AGG-LOGISTICS-REQUEST.md | 0 |  |
| SM-MAINTENANCE-ORDER | 03-domain/contexts/BC05/aggregates/AGG-MAINTENANCE-ORDER.md | 0 |  |
| SM-MATCH-RULESET | 03-domain/contexts/BC02/aggregates/AGG-MATCH-RULESET.md | 0 |  |
| SM-MODEL-VERSION | 03-domain/contexts/BC07/aggregates/AGG-MODEL-VERSION.md | 0 |  |
| SM-NOTIFICATION | 03-domain/contexts/BC04/aggregates/AGG-NOTIFICATION.md | 0 |  |
| SM-OBSERVATION | 03-domain/contexts/BC02/aggregates/AGG-OBSERVATION.md | 0 |  |
| SM-ORGANIZATION | 03-domain/contexts/BC01/aggregates/AGG-ORGANIZATION.md | 0 |  |
| SM-OUTCOME-TRACKER | 03-domain/contexts/BC04/aggregates/AGG-OUTCOME-TRACKER.md | 0 |  |
| SM-PERSON | 03-domain/contexts/BC01/aggregates/AGG-PERSON.md | 0 |  |
| SM-PLAN | 03-domain/contexts/BC04/aggregates/AGG-PLAN.md | 1 | 00-governance/registers/open-questions.md |
| SM-PLAN-VERSION | 03-domain/contexts/BC04/aggregates/AGG-PLAN-VERSION.md | 0 |  |
| SM-POLICY-SET | 03-domain/contexts/BC08/aggregates/AGG-POLICY-SET.md | 0 |  |
| SM-PRELOAD-PACKAGE | 03-domain/contexts/BC07/aggregates/AGG-PRELOAD-PACKAGE.md | 0 |  |
| SM-PRODUCT | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT.md | 0 |  |
| SM-PRODUCT-TEMPLATE | 03-domain/contexts/BC06/aggregates/AGG-PRODUCT-TEMPLATE.md | 0 |  |
| SM-PROJECTION-VERSION | 03-domain/contexts/BC07/aggregates/AGG-PROJECTION-VERSION.md | 0 |  |
| SM-QUALIFICATION-RECORD | 03-domain/contexts/BC05/aggregates/AGG-QUALIFICATION-RECORD.md | 0 |  |
| SM-REALWORLD-EVENT | 03-domain/contexts/BC02/aggregates/AGG-REALWORLD-EVENT.md | 0 |  |
| SM-RECONSTRUCTION | 03-domain/contexts/BC06/aggregates/AGG-RECONSTRUCTION.md | 0 |  |
| SM-RELATIONSHIP | 03-domain/contexts/BC02/aggregates/AGG-RELATIONSHIP.md | 0 |  |
| SM-RESOURCE-POOL | 03-domain/contexts/BC05/aggregates/AGG-RESOURCE-POOL.md | 0 |  |
| SM-RETENTION-SCHEDULE | 03-domain/contexts/BC08/aggregates/AGG-RETENTION-SCHEDULE.md | 0 |  |
| SM-RISK | 03-domain/contexts/BC04/aggregates/AGG-RISK.md | 0 |  |
| SM-ROLE | 03-domain/contexts/BC01/aggregates/AGG-ROLE.md | 0 |  |
| SM-ROLE-ASSIGNMENT | 03-domain/contexts/BC01/aggregates/AGG-ROLE-ASSIGNMENT.md | 0 |  |
| SM-ROLE-REQUIREMENT | 03-domain/contexts/BC05/aggregates/AGG-ROLE-REQUIREMENT.md | 0 |  |
| SM-SCENARIO | 03-domain/contexts/BC05/aggregates/AGG-SCENARIO.md | 0 |  |
| SM-SECURITY-EXCEPTION | 03-domain/contexts/BC08/aggregates/AGG-SECURITY-EXCEPTION.md | 0 |  |
| SM-SENSOR-STREAM | 03-domain/contexts/BC07/aggregates/AGG-SENSOR-STREAM.md | 0 |  |
| SM-SERVICE-ACCOUNT | 03-domain/contexts/BC01/aggregates/AGG-SERVICE-ACCOUNT.md | 0 |  |
| SM-SHIPMENT | 03-domain/contexts/BC05/aggregates/AGG-SHIPMENT.md | 0 |  |
| SM-SIMULATION | 03-domain/contexts/BC05/aggregates/AGG-SIMULATION.md | 0 |  |
| SM-SITUATION | 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md | 0 |  |
| SM-SOURCE | 03-domain/contexts/BC02/aggregates/AGG-SOURCE.md | 0 |  |
| SM-SUBSCRIPTION | 03-domain/contexts/BC04/aggregates/AGG-SUBSCRIPTION.md | 0 |  |
| SM-SYNC-CONFLICT | 03-domain/contexts/BC07/aggregates/AGG-SYNC-CONFLICT.md | 0 |  |
| SM-SYNC-SESSION | 03-domain/contexts/BC07/aggregates/AGG-SYNC-SESSION.md | 0 |  |
| SM-TASK | 03-domain/contexts/BC04/aggregates/AGG-TASK.md | 4 | 00-governance/registers/open-questions.md; 00-governance/registers/unknowns.md; 02-requirements/requirements.md; 03-domain/contexts/BC04/decision-plan-spec.md |
| SM-TASK-TYPE | 03-domain/contexts/BC04/aggregates/AGG-TASK-TYPE.md | 0 |  |
| SM-TENANT | 03-domain/contexts/BC01/aggregates/AGG-TENANT.md | 0 |  |
| SM-USER | 03-domain/contexts/BC01/aggregates/AGG-USER.md | 0 |  |

### Family: SPATIAL

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| SPATIAL-MODEL | 04-information/spatial-model.md | 0 |  |

### Family: SPEC

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| SPEC-AI | 03-domain/contexts/BC07/grounded-ai-spec.md | 7 | 00-governance/glossary.md; 03-domain/contexts/BC07/aggregates/AGG-AI-REQUEST.md; 12-solution/technology-decisions.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc10.md; 16-repor ...(truncated) |
| SPEC-ALLOCATION | 03-domain/contexts/BC05/allocation-readiness-spec.md | 12 | 00-governance/glossary.md; 00-governance/registers/technical-debt.md; 02-requirements/requirements.md; 03-domain/contexts/BC05/logistics-spec.md; 03-domain/contexts/BC05/aggregates/AGG-ALLOCATION.md;  ...(truncated) |
| SPEC-ANALYSIS | 03-domain/contexts/BC03/analysis-reproducibility-spec.md | 5 | 00-governance/glossary.md; 12-solution/technology-decisions.md; 12-solution/w8-inputs.md; 15-traceability/trace-slc07.md; 16-reports/ARCHITECTURE-REVIEW-R1.md |
| SPEC-COLLECTION | 03-domain/contexts/BC02/collection-spec.md | 4 | 00-governance/glossary.md; 03-domain/contexts/BC02/aggregates/AGG-COLLECTION-REQUIREMENT.md; 13-verification/tooling/slice-sources.md; 15-traceability/trace-slc14.md |
| SPEC-CONFLICT-DETECTION | 03-domain/contexts/BC02/conflict-detection-engine.md | 1 | 15-traceability/trace-slc04.md |
| SPEC-DISCOVERY | 03-domain/contexts/BC07/discovery-architecture.md | 13 | 00-governance/glossary.md; 00-governance/decisions/ADR-P05.md; 00-governance/decisions/ADR-P06.md; 00-governance/registers/corrections.md; 00-governance/registers/risks.md; 03-domain/contexts/BC07/gro ...(truncated) |
| SPEC-ELIGIBILITY | 03-domain/contexts/BC05/eligibility-rules.md | 3 | 00-governance/glossary.md; 03-domain/contexts/BC05/allocation-readiness-spec.md; 15-traceability/trace-slc03.md |
| SPEC-ER-CANDIDATES | 03-domain/contexts/BC02/candidate-generation.md | 2 | 00-governance/glossary.md; 15-traceability/trace-slc04.md |
| SPEC-FIELD-SYNC | 03-domain/contexts/BC07/field-sync-protocol.md | 6 | 00-governance/glossary.md; 00-governance/registers/corrections.md; 04-information/conflict-model.md; 12-solution/technology-decisions.md; 12-solution/w8-inputs.md; 15-traceability/trace-slc11.md |
| SPEC-FUSION | 03-domain/contexts/BC02/correlation-fusion-spec.md | 1 | 15-traceability/trace-slc15.md |
| SPEC-INTEGRATION | 03-domain/contexts/BC07/enterprise-integration-spec.md | 2 | 00-governance/glossary.md; 15-traceability/trace-slc16.md |
| SPEC-KEYS-DISPOSITION | 08-security/key-hierarchy-and-disposition.md | 5 | 00-governance/glossary.md; 00-governance/registers/corrections.md; 12-solution/technology-decisions.md; 12-solution/w8-inputs.md; 15-traceability/trace-slc12a.md |
| SPEC-LOGISTICS | 03-domain/contexts/BC05/logistics-spec.md | 2 | 14-slices/SLC-18/atam-lite.md; 15-traceability/trace-slc18.md |
| SPEC-PKA | 03-domain/contexts/BC06/products-knowledge-archive-spec.md | 3 | 00-governance/glossary.md; 03-domain/contexts/BC07/grounded-ai-spec.md; 15-traceability/trace-slc12.md |
| SPEC-PLAN | 03-domain/contexts/BC04/decision-plan-spec.md | 12 | 00-governance/glossary.md; 00-governance/RATIFICATION-PACKAGE.md; 01-business/release-3-scope.md; 03-domain/contexts/BC04/commands-slc08.md; 03-domain/contexts/BC04/events-slc08.md; 03-domain/contexts ...(truncated) |
| SPEC-RISK-CONTINGENCY | 03-domain/contexts/BC04/risk-contingency-spec.md | 2 | 03-domain/contexts/BC05/logistics-spec.md; 15-traceability/trace-slc17.md |
| SPEC-SITUATION | 03-domain/contexts/BC03/situation-alerting-spec.md | 7 | 00-governance/glossary.md; 03-domain/contexts/BC03/commands-slc06.md; 03-domain/contexts/BC03/aggregates/AGG-SITUATION.md; 12-solution/technology-decisions.md; 12-solution/w8-inputs.md; 13-verificatio ...(truncated) |
| SPEC-TASK-RULES | 03-domain/contexts/BC04/task-lifecycle-rules.md | 4 | 00-governance/registers/corrections.md; 00-governance/registers/open-questions.md; 14-slices/SLC-03/readiness.md; 15-traceability/trace-slc03.md |
| SPEC-TOOLING | 13-verification/tooling/spec-tooling.md | 0 |  |
| SPEC-TRAINING-EXERCISE | 03-domain/contexts/BC05/training-exercise-spec.md | 1 | 15-traceability/trace-slc19.md |

### Family: SR

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| SR-00 | 01-business/system-definition.md | 6 | 00-governance/registers/risks.md; 03-domain/contexts/BC07/discovery-architecture.md; 07-quality/scale-envelope.md; 08-security/audit-architecture.md; 08-security/key-hierarchy-and-disposition.md; 16-r ...(truncated) |
| SR-01 | 07-quality/scale-envelope.md | 1 | 12-solution/technology-decisions.md |
| SR-02 | 07-quality/scale-envelope.md | 2 | 06-data/logical-model/slc-01.md; 13-verification/fitness-functions.md |
| SR-03 | 07-quality/scale-envelope.md | 0 |  |
| SR-04 | 07-quality/scale-envelope.md | 0 |  |
| SR-05 | 07-quality/scale-envelope.md | 5 | 02-requirements/requirements.md; 03-domain/contexts/BC02/aggregates/AGG-ATTACHMENT.md; 07-quality/workloads-slc07.md; 12-solution/technology-decisions.md; 13-verification/tooling/slice-sources.md |
| SR-06 | 07-quality/scale-envelope.md | 1 | 02-requirements/requirements.md |
| SR-07 | 07-quality/scale-envelope.md | 2 | 02-requirements/quality-scenarios.md; 02-requirements/requirements.md |
| SR-08 | 07-quality/scale-envelope.md | 4 | 00-governance/decisions/ADR-P01.md; 04-information/temporal-model.md; 06-data/logical-model/slc-02.md; 07-quality/cost-model.md |
| SR-09 | 07-quality/scale-envelope.md | 3 | 00-governance/glossary.md; 00-governance/decisions/ADR-P04.md; 02-requirements/requirements.md |
| SR-10 | 07-quality/scale-envelope.md | 8 | 00-governance/decisions/ADR-P05.md; 00-governance/registers/risks.md; 03-domain/bc-boundary-test.md; 03-domain/contexts/BC07/discovery-architecture.md; 07-quality/cost-model.md; 12-solution/technology ...(truncated) |
| SR-11 | 07-quality/scale-envelope.md | 0 |  |
| SR-12 | 07-quality/scale-envelope.md | 2 | 02-requirements/requirements.md; 13-verification/fitness-functions.md |

### Family: TB

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| TB-01 | 08-security/trust-boundaries.md | 2 | 08-security/threat-model.md; 12-solution/deployment-units.md |
| TB-02 | 08-security/trust-boundaries.md | 2 | 03-domain/contexts/BC01/security-context.md; 08-security/threat-model.md |
| TB-03 | 08-security/trust-boundaries.md | 1 | 08-security/threat-model.md |
| TB-04 | 08-security/trust-boundaries.md | 2 | 08-security/threat-model-slc05.md; 08-security/threat-model.md |
| TB-05 | 08-security/trust-boundaries.md | 2 | 08-security/threat-model.md; 12-solution/cell-architecture.md |
| TB-06 | 08-security/trust-boundaries.md | 4 | 08-security/threat-model.md; 12-solution/deployment-units.md; 16-reports/ARCHITECTURE-REVIEW-R2.md; 16-reports/CONSISTENCY-REPORT-R2.md |
| TB-07 | 08-security/trust-boundaries.md | 1 | 08-security/threat-model.md |
| TB-08 | 08-security/trust-boundaries.md | 2 | 03-domain/bc-boundary-test.md; 08-security/threat-model.md |
| TB-09 | 08-security/trust-boundaries.md | 1 | 08-security/threat-model.md |
| TB-10 | 08-security/trust-boundaries.md | 1 | 08-security/threat-model.md |

### Family: TD

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| TD-01 | 12-solution/technology-decisions.md | 3 | 00-governance/registers/assumptions.md; 16-reports/ANTI-PATTERN-REPORT-R1.md; 16-reports/EVOLUTION-ROADMAP.md |
| TD-02 | 12-solution/technology-decisions.md | 3 | 00-governance/registers/risks.md; 14-slices/slices.md; 16-reports/gate-reports/GATE-STATUS-W8.md |
| TD-03 | 12-solution/technology-decisions.md | 3 | 00-governance/registers/assumptions.md; 07-quality/cost-model.md; 16-reports/EVOLUTION-ROADMAP.md |
| TD-04 | 12-solution/technology-decisions.md | 2 | 00-governance/registers/assumptions.md; 16-reports/EVOLUTION-ROADMAP.md |
| TD-05 | 12-solution/technology-decisions.md | 1 | 16-reports/ANTI-PATTERN-REPORT-R1.md |
| TD-06 | 12-solution/technology-decisions.md | 0 |  |
| TD-07 | 12-solution/technology-decisions.md | 0 |  |
| TD-08 | 12-solution/technology-decisions.md | 2 | 12-solution/c4-containers.md; 16-reports/IMPLEMENTATION-READINESS-R1.md |
| TD-09 | 12-solution/technology-decisions.md | 0 |  |
| TD-10 | 12-solution/technology-decisions.md | 1 | 11-integration/README.md |
| TD-11 | 12-solution/technology-decisions.md | 0 |  |
| TD-12 | 12-solution/technology-decisions.md | 1 | 03-domain/contexts/BC07/grounded-ai-spec.md |
| TD-13 | 12-solution/technology-decisions.md | 0 |  |
| TD-14 | 12-solution/technology-decisions.md | 2 | 07-quality/performance-test-strategy.md; 15-traceability/trace-platform.md |
| TD-15 | 12-solution/technology-decisions.md | 1 | 16-reports/EVOLUTION-ROADMAP.md |
| TD-16 | 12-solution/technology-decisions.md | 2 | 00-governance/registers/risks.md; 12-solution/ui-architecture.md |
| TD-17 | 12-solution/technology-decisions.md | 1 | 12-solution/release-configuration-migration.md |
| TD-18 | 12-solution/technology-decisions.md | 5 | 03-domain/contexts/BC07/grounded-ai-spec.md; 12-solution/deployment-units.md; 16-reports/CONSISTENCY-REPORT-R2.md; 16-reports/ENGINEERING-BASELINE-R2.md; 16-reports/SESSION-W4-W7-SLC10.md |
| TD-19 | 12-solution/technology-decisions.md | 4 | 03-domain/contexts/BC07/grounded-ai-spec.md; 16-reports/ARCHITECTURE-REVIEW-R2.md; 16-reports/ENGINEERING-BASELINE-R2.md; 16-reports/SESSION-W4-W7-SLC10.md |

### Family: TECH

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| TECH-DECISIONS | 12-solution/technology-decisions.md | 5 | 00-governance/glossary.md; 00-governance/decisions/ADR-P05.md; 00-governance/registers/corrections.md; 16-reports/ANTI-PATTERN-REPORT-R1.md; 16-reports/gate-reports/GATE-STATUS-FINAL-R1.md |

### Family: TEMPORAL

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| TEMPORAL-MODEL | 04-information/temporal-model.md | 6 | 03-domain/contexts/BC02/claims-temporal-kernel.md; 03-domain/contexts/BC03/analysis-reproducibility-spec.md; 03-domain/contexts/BC03/aggregates/AGG-ANALYSIS-CASE.md; 03-domain/contexts/BC04/decision-p ...(truncated) |

### Family: THR

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| THR-001 | 08-security/threat-model.md | 0 |  |
| THR-002 | 08-security/threat-model.md | 0 |  |
| THR-003 | 08-security/threat-model.md | 0 |  |
| THR-004 | 08-security/threat-model.md | 0 |  |
| THR-005 | 08-security/threat-model.md | 0 |  |
| THR-006 | 08-security/threat-model.md | 0 |  |
| THR-007 | 08-security/threat-model.md | 0 |  |
| THR-008 | 08-security/threat-model.md | 0 |  |
| THR-009 | 08-security/threat-model.md | 0 |  |
| THR-010 | 08-security/threat-model.md | 0 |  |
| THR-011 | 08-security/threat-model.md | 0 |  |
| THR-012 | 08-security/threat-model.md | 2 | 03-domain/contexts/BC01/aggregates/AGG-DEVICE.md; 13-verification/tooling/slice-sources.md |
| THR-013 | 08-security/threat-model.md | 1 | 02-requirements/requirements.md |
| THR-014 | 08-security/threat-model.md | 0 |  |
| THR-015 | 08-security/threat-model.md | 0 |  |
| THR-016 | 08-security/threat-model.md | 0 |  |
| THR-017 | 08-security/threat-model.md | 0 |  |
| THR-018 | 08-security/threat-model.md | 0 |  |
| THR-019 | 08-security/threat-model.md | 1 | 12-solution/technology-decisions.md |
| THR-020 | 08-security/threat-model.md | 0 |  |
| THR-S01-01 | 08-security/threat-model-slc01.md | 3 | 02-requirements/requirements.md; 03-domain/contexts/BC01/aggregates/AGG-HR-SYNC-PROPOSAL.md; 13-verification/tooling/slice-sources.md |
| THR-S01-02 | 08-security/threat-model-slc01.md | 0 |  |
| THR-S01-03 | 08-security/threat-model-slc01.md | 0 |  |
| THR-S01-04 | 08-security/threat-model-slc01.md | 1 | 14-slices/SLC-01/atam-lite.md |
| THR-S01-05 | 08-security/threat-model-slc01.md | 0 |  |
| THR-S01-06 | 08-security/threat-model-slc01.md | 0 |  |
| THR-S01-07 | 08-security/threat-model-slc01.md | 0 |  |
| THR-S01-08 | 08-security/threat-model-slc01.md | 0 |  |
| THR-S01-09 | 08-security/threat-model-slc01.md | 0 |  |
| THR-S01-10 | 08-security/threat-model-slc01.md | 0 |  |
| THR-S01-11 | 08-security/threat-model-slc01.md | 1 | 14-slices/SLC-01/atam-lite.md |
| THR-S01-12 | 08-security/threat-model-slc01.md | 1 | 13-verification/acceptance/SLC-01/invariants-slc01.md |
| THR-S02-01 | 08-security/threat-model-slc02.md | 0 |  |
| THR-S02-02 | 08-security/threat-model-slc02.md | 0 |  |
| THR-S02-03 | 08-security/threat-model-slc02.md | 0 |  |
| THR-S02-04 | 08-security/threat-model-slc02.md | 0 |  |
| THR-S02-05 | 08-security/threat-model-slc02.md | 0 |  |
| THR-S02-06 | 08-security/threat-model-slc02.md | 0 |  |
| THR-S02-07 | 08-security/threat-model-slc02.md | 0 |  |
| THR-S02-08 | 08-security/threat-model-slc02.md | 0 |  |
| THR-S02-09 | 08-security/threat-model-slc02.md | 0 |  |
| THR-S02-10 | 08-security/threat-model-slc02.md | 0 |  |
| THR-S03-01 | 08-security/threat-model-slc03.md | 0 |  |
| THR-S03-02 | 08-security/threat-model-slc03.md | 0 |  |
| THR-S03-03 | 08-security/threat-model-slc03.md | 0 |  |
| THR-S03-04 | 08-security/threat-model-slc03.md | 0 |  |
| THR-S03-05 | 08-security/threat-model-slc03.md | 0 |  |
| THR-S03-06 | 08-security/threat-model-slc03.md | 0 |  |
| THR-S04-01 | 08-security/threat-model-slc04.md | 0 |  |
| THR-S04-02 | 08-security/threat-model-slc04.md | 0 |  |
| THR-S04-03 | 08-security/threat-model-slc04.md | 0 |  |
| THR-S04-04 | 08-security/threat-model-slc04.md | 0 |  |
| THR-S04-05 | 08-security/threat-model-slc04.md | 0 |  |
| THR-S04-06 | 08-security/threat-model-slc04.md | 0 |  |
| THR-S04-07 | 08-security/threat-model-slc04.md | 0 |  |
| THR-S05-01 | 08-security/threat-model-slc05.md | 1 | 03-domain/contexts/BC07/discovery-architecture.md |
| THR-S05-02 | 08-security/threat-model-slc05.md | 0 |  |
| THR-S05-03 | 08-security/threat-model-slc05.md | 0 |  |
| THR-S05-04 | 08-security/threat-model-slc05.md | 1 | 13-verification/acceptance/SLC-05/invariants-slc05.md |
| THR-S05-05 | 08-security/threat-model-slc05.md | 0 |  |
| THR-S05-06 | 08-security/threat-model-slc05.md | 0 |  |
| THR-S05-07 | 08-security/threat-model-slc05.md | 0 |  |
| THR-S05-08 | 08-security/threat-model-slc05.md | 1 | 14-slices/SLC-05/atam-lite.md |
| THR-S06-01 | 08-security/threat-model-slc06.md | 0 |  |
| THR-S06-02 | 08-security/threat-model-slc06.md | 0 |  |
| THR-S06-03 | 08-security/threat-model-slc06.md | 0 |  |
| THR-S06-04 | 08-security/threat-model-slc06.md | 0 |  |
| THR-S06-05 | 08-security/threat-model-slc06.md | 0 |  |
| THR-S06-06 | 08-security/threat-model-slc06.md | 0 |  |
| THR-S06-07 | 08-security/threat-model-slc06.md | 0 |  |
| THR-S07-01 | 08-security/threat-model-slc07.md | 0 |  |
| THR-S07-02 | 08-security/threat-model-slc07.md | 0 |  |
| THR-S07-03 | 08-security/threat-model-slc07.md | 0 |  |
| THR-S07-04 | 08-security/threat-model-slc07.md | 0 |  |
| THR-S07-05 | 08-security/threat-model-slc07.md | 0 |  |
| THR-S07-06 | 08-security/threat-model-slc07.md | 0 |  |
| THR-S08-01 | 08-security/threat-model-slc08.md | 0 |  |
| THR-S08-02 | 08-security/threat-model-slc08.md | 0 |  |
| THR-S08-03 | 08-security/threat-model-slc08.md | 0 |  |
| THR-S08-04 | 08-security/threat-model-slc08.md | 0 |  |
| THR-S08-05 | 08-security/threat-model-slc08.md | 0 |  |
| THR-S08-06 | 08-security/threat-model-slc08.md | 0 |  |
| THR-S09-01 | 08-security/threat-model-slc09.md | 0 |  |
| THR-S09-02 | 08-security/threat-model-slc09.md | 0 |  |
| THR-S09-03 | 08-security/threat-model-slc09.md | 1 | 13-verification/acceptance/SLC-09/invariants-slc09.md |
| THR-S09-04 | 08-security/threat-model-slc09.md | 0 |  |
| THR-S10-01 | 08-security/threat-model-slc10.md | 0 |  |
| THR-S10-02 | 08-security/threat-model-slc10.md | 0 |  |
| THR-S10-03 | 08-security/threat-model-slc10.md | 0 |  |
| THR-S10-04 | 08-security/threat-model-slc10.md | 1 | 14-slices/SLC-10/atam-lite.md |
| THR-S10-05 | 08-security/threat-model-slc10.md | 0 |  |
| THR-S10-06 | 08-security/threat-model-slc10.md | 0 |  |
| THR-S11-01 | 08-security/threat-model-slc11.md | 0 |  |
| THR-S11-02 | 08-security/threat-model-slc11.md | 0 |  |
| THR-S11-03 | 08-security/threat-model-slc11.md | 0 |  |
| THR-S11-04 | 08-security/threat-model-slc11.md | 0 |  |
| THR-S11-05 | 08-security/threat-model-slc11.md | 0 |  |
| THR-S11-06 | 08-security/threat-model-slc11.md | 0 |  |
| THR-S12-01 | 08-security/threat-model-slc12a.md | 0 |  |
| THR-S12-02 | 08-security/threat-model-slc12a.md | 0 |  |
| THR-S12-03 | 08-security/threat-model-slc12a.md | 0 |  |
| THR-S12-04 | 08-security/threat-model-slc12a.md | 0 |  |
| THR-S12-05 | 08-security/threat-model-slc12a.md | 0 |  |
| THR-S12-P1 | 08-security/threat-model-slc12.md | 0 |  |
| THR-S12-P2 | 08-security/threat-model-slc12.md | 1 | 14-slices/SLC-12/atam-lite.md |
| THR-S12-P3 | 08-security/threat-model-slc12.md | 0 |  |
| THR-S12-P4 | 08-security/threat-model-slc12.md | 0 |  |
| THR-S12-P5 | 08-security/threat-model-slc12.md | 0 |  |
| THR-S14-01 | 08-security/threat-model-slc14.md | 0 |  |
| THR-S14-02 | 08-security/threat-model-slc14.md | 0 |  |
| THR-S15-01 | 08-security/threat-model-slc15.md | 0 |  |
| THR-S15-02 | 08-security/threat-model-slc15.md | 0 |  |
| THR-S15-03 | 08-security/threat-model-slc15.md | 0 |  |
| THR-S15-04 | 08-security/threat-model-slc15.md | 0 |  |
| THR-S16-01 | 08-security/threat-model-slc16.md | 0 |  |
| THR-S16-02 | 08-security/threat-model-slc16.md | 0 |  |
| THR-S16-03 | 08-security/threat-model-slc16.md | 0 |  |
| THR-S16-04 | 08-security/threat-model-slc16.md | 0 |  |
| THR-S16-05 | 08-security/threat-model-slc16.md | 1 | 14-slices/SLC-16/atam-lite.md |
| THR-S17-01 | 08-security/threat-model-slc17.md | 0 |  |
| THR-S17-02 | 08-security/threat-model-slc17.md | 0 |  |
| THR-S17-03 | 08-security/threat-model-slc17.md | 0 |  |
| THR-S17-04 | 08-security/threat-model-slc17.md | 0 |  |
| THR-S17-05 | 08-security/threat-model-slc17.md | 0 |  |
| THR-S18-01 | 08-security/threat-model-slc18.md | 0 |  |
| THR-S18-02 | 08-security/threat-model-slc18.md | 0 |  |
| THR-S18-03 | 08-security/threat-model-slc18.md | 0 |  |
| THR-S18-04 | 08-security/threat-model-slc18.md | 0 |  |
| THR-S18-05 | 08-security/threat-model-slc18.md | 0 |  |
| THR-S19-01 | 08-security/threat-model-slc19.md | 0 |  |
| THR-S19-02 | 08-security/threat-model-slc19.md | 0 |  |
| THR-S19-03 | 08-security/threat-model-slc19.md | 0 |  |
| THR-S19-04 | 08-security/threat-model-slc19.md | 0 |  |
| THR-S19-05 | 08-security/threat-model-slc19.md | 0 |  |

### Family: THREAT

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| THREAT-MODEL | 08-security/threat-model.md | 0 |  |
| THREAT-MODEL-SLC01 | 08-security/threat-model-slc01.md | 0 |  |
| THREAT-MODEL-SLC02 | 08-security/threat-model-slc02.md | 0 |  |
| THREAT-MODEL-SLC03 | 08-security/threat-model-slc03.md | 0 |  |
| THREAT-MODEL-SLC04 | 08-security/threat-model-slc04.md | 0 |  |
| THREAT-MODEL-SLC05 | 08-security/threat-model-slc05.md | 0 |  |
| THREAT-MODEL-SLC06 | 08-security/threat-model-slc06.md | 0 |  |
| THREAT-MODEL-SLC07 | 08-security/threat-model-slc07.md | 0 |  |
| THREAT-MODEL-SLC08 | 08-security/threat-model-slc08.md | 0 |  |
| THREAT-MODEL-SLC09 | 08-security/threat-model-slc09.md | 0 |  |
| THREAT-MODEL-SLC10 | 08-security/threat-model-slc10.md | 0 |  |
| THREAT-MODEL-SLC11 | 08-security/threat-model-slc11.md | 0 |  |
| THREAT-MODEL-SLC12 | 08-security/threat-model-slc12.md | 0 |  |
| THREAT-MODEL-SLC12A | 08-security/threat-model-slc12a.md | 0 |  |
| THREAT-MODEL-SLC14 | 08-security/threat-model-slc14.md | 0 |  |
| THREAT-MODEL-SLC15 | 08-security/threat-model-slc15.md | 0 |  |
| THREAT-MODEL-SLC16 | 08-security/threat-model-slc16.md | 0 |  |
| THREAT-MODEL-SLC17 | 08-security/threat-model-slc17.md | 0 |  |
| THREAT-MODEL-SLC18 | 08-security/threat-model-slc18.md | 0 |  |
| THREAT-MODEL-SLC19 | 08-security/threat-model-slc19.md | 0 |  |

### Family: TRACE

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| TRACE-PLATFORM | 12-solution/w8-inputs.md;15-traceability/trace-platform.md | 1 | 00-governance/registers/corrections.md |
| TRACE-SLC01 | 15-traceability/trace-slc01.md | 0 |  |
| TRACE-SLC02 | 15-traceability/trace-slc02.md | 0 |  |
| TRACE-SLC03 | 15-traceability/trace-slc03.md | 0 |  |
| TRACE-SLC04 | 15-traceability/trace-slc04.md | 0 |  |
| TRACE-SLC05 | 15-traceability/trace-slc05.md | 0 |  |
| TRACE-SLC06 | 15-traceability/trace-slc06.md | 0 |  |
| TRACE-SLC07 | 15-traceability/trace-slc07.md | 0 |  |
| TRACE-SLC08 | 15-traceability/trace-slc08.md | 0 |  |
| TRACE-SLC09 | 15-traceability/trace-slc09.md | 0 |  |
| TRACE-SLC10 | 15-traceability/trace-slc10.md | 0 |  |
| TRACE-SLC11 | 15-traceability/trace-slc11.md | 0 |  |
| TRACE-SLC12 | 15-traceability/trace-slc12.md | 0 |  |
| TRACE-SLC12A | 15-traceability/trace-slc12a.md | 0 |  |
| TRACE-SLC14 | 15-traceability/trace-slc14.md | 0 |  |
| TRACE-SLC15 | 15-traceability/trace-slc15.md | 0 |  |
| TRACE-SLC16 | 15-traceability/trace-slc16.md | 0 |  |
| TRACE-SLC17 | 15-traceability/trace-slc17.md | 0 |  |
| TRACE-SLC18 | 15-traceability/trace-slc18.md | 0 |  |
| TRACE-SLC19 | 15-traceability/trace-slc19.md | 0 |  |

### Family: TRUST

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| TRUST-BOUNDARIES | 08-security/trust-boundaries.md | 0 |  |

### Family: TST

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| TST-ADAPTER-SM | 13-verification/acceptance/SLC-02/adapter-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-AI-REQUEST-SM | 13-verification/acceptance/SLC-10/ai-request-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc10.md |
| TST-AI-RESULT-SM | 13-verification/acceptance/SLC-10/ai-result-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc10.md |
| TST-AI-ROUTING-SM | 13-verification/acceptance/SLC-10/ai-routing-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc10.md |
| TST-AI-TOOL-SM | 13-verification/acceptance/SLC-10/ai-tool-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc10.md |
| TST-ALERT-RULE-SM | 13-verification/acceptance/SLC-06/alert-rule-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc06.md |
| TST-ALERT-SM | 13-verification/acceptance/SLC-06/alert-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc06.md |
| TST-ALLOCATION-SM | 13-verification/acceptance/SLC-09/allocation-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc09.md |
| TST-ANALYSIS-CASE-SM | 13-verification/acceptance/SLC-07/analysis-case-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc07.md |
| TST-ANALYSIS-METHOD-SM | 13-verification/acceptance/SLC-07/analysis-method-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc07.md |
| TST-ANALYSIS-RUN-SM | 13-verification/acceptance/SLC-07/analysis-run-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc07.md |
| TST-ARCHIVE-PACKAGE-SM | 13-verification/acceptance/SLC-12/archive-package-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc12.md |
| TST-ASSESSMENT-SM | 13-verification/acceptance/SLC-07/assessment-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc07.md |
| TST-ASSET-ASSIGNMENT-SM | 13-verification/acceptance/SLC-09/asset-assignment-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc09.md |
| TST-ASSET-RESERVATION-SM | 13-verification/acceptance/SLC-09/asset-reservation-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc09.md |
| TST-ASSET-SM | 13-verification/acceptance/SLC-09/asset-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc09.md |
| TST-ATTACHMENT-SM | 13-verification/acceptance/SLC-02/attachment-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-AUTHORITY-GRANT-SM | 13-verification/acceptance/SLC-01/authority-grant-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-CAP-MESSAGE-SM | 13-verification/acceptance/SLC-16/cap-message-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc16.md |
| TST-CLAIM-SM | 13-verification/acceptance/SLC-02/claim-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-CLASSIFICATION-SCHEME-SM | 13-verification/acceptance/SLC-01/classification-scheme-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-CLEARANCE-SM | 13-verification/acceptance/SLC-01/clearance-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-COLLECTION-PLAN-SM | 13-verification/acceptance/SLC-14/collection-plan-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc14.md |
| TST-COLLECTION-REQUIREMENT-SM | 13-verification/acceptance/SLC-14/collection-requirement-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc14.md |
| TST-CONFLICT-SM | 13-verification/acceptance/SLC-04/conflict-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc04.md |
| TST-COORDINATION-CASE-SM | 13-verification/acceptance/SLC-15/coordination-case-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc15.md |
| TST-CORRELATION-PROPOSAL-SM | 13-verification/acceptance/SLC-15/correlation-proposal-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc15.md |
| TST-CORRELATION-RULE-SM | 13-verification/acceptance/SLC-15/correlation-rule-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc15.md |
| TST-DECISION-REQUEST-SM | 13-verification/acceptance/SLC-08/decision-request-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc08.md |
| TST-DECISION-SM | 13-verification/acceptance/SLC-08/decision-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc08.md |
| TST-DEVICE-SM | 13-verification/acceptance/SLC-11/device-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc11.md |
| TST-DISPOSITION-RUN-SM | 13-verification/acceptance/SLC-12a/disposition-run-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc12a.md |
| TST-DISTRIBUTION-SM | 13-verification/acceptance/SLC-12/distribution-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc12.md |
| TST-ENTITY-SM | 13-verification/acceptance/SLC-02/entity-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-ERASURE-REQUEST-SM | 13-verification/acceptance/SLC-12a/erasure-request-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc12a.md |
| TST-ER-CASE-SM | 13-verification/acceptance/SLC-04/er-case-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc04.md |
| TST-EVAL-SUITE-SM | 13-verification/acceptance/SLC-10/eval-suite-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc10.md |
| TST-EVIDENCE-LINK-SM | 13-verification/acceptance/SLC-02/evidence-link-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-EVIDENCE-SM | 13-verification/acceptance/SLC-02/evidence-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-EXERCISE-SM | 13-verification/acceptance/SLC-19/exercise-state-machine.md | 1 | 15-traceability/trace-slc19.md |
| TST-EXTERNAL-ID-SM | 13-verification/acceptance/SLC-02/external-id-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-FINDING-SM | 13-verification/acceptance/SLC-07/finding-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc07.md |
| TST-HR-SYNC-PROPOSAL-SM | 13-verification/acceptance/SLC-16/hr-sync-proposal-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc16.md |
| TST-IMPORT-BATCH-SM | 13-verification/acceptance/SLC-02/import-batch-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-INCIDENT-SM | 13-verification/acceptance/SLC-17/incident-state-machine.md | 2 | 15-traceability/quality-verification-matrix.md; 15-traceability/trace-slc17.md |
| TST-INTEGRATION-CONNECTION-SM | 13-verification/acceptance/SLC-16/integration-connection-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc16.md |
| TST-KNOWLEDGE-OBJECT-SM | 13-verification/acceptance/SLC-12/knowledge-object-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc12.md |
| TST-LEGAL-HOLD-SM | 13-verification/acceptance/SLC-12a/legal-hold-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc12a.md |
| TST-LOGISTICS-REQUEST-SM | 13-verification/acceptance/SLC-18/logistics-request-state-machine.md | 1 | 15-traceability/trace-slc18.md |
| TST-MAINTENANCE-ORDER-SM | 13-verification/acceptance/SLC-09/maintenance-order-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc09.md |
| TST-MATCH-RULESET-SM | 13-verification/acceptance/SLC-04/match-ruleset-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc04.md |
| TST-MODEL-VERSION-SM | 13-verification/acceptance/SLC-10/model-version-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc10.md |
| TST-NOTIFICATION-SM | 13-verification/acceptance/SLC-06/notification-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc06.md |
| TST-OBSERVATION-SM | 13-verification/acceptance/SLC-02/observation-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-ORGANIZATION-SM | 13-verification/acceptance/SLC-01/organization-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-OUTCOME-TRACKER-SM | 13-verification/acceptance/SLC-08/outcome-tracker-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc08.md |
| TST-PERSON-SM | 13-verification/acceptance/SLC-01/person-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-PLAN-SM | 13-verification/acceptance/SLC-08/plan-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc08.md |
| TST-PLAN-VERSION-SM | 13-verification/acceptance/SLC-08/plan-version-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc08.md |
| TST-POLICY-SET-SM | 13-verification/acceptance/SLC-01/policy-set-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-PRELOAD-PACKAGE-SM | 13-verification/acceptance/SLC-11/preload-package-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc11.md |
| TST-PRODUCT-SM | 13-verification/acceptance/SLC-12/product-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc12.md |
| TST-PRODUCT-TEMPLATE-SM | 13-verification/acceptance/SLC-12/product-template-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc12.md |
| TST-PROJECTION-VERSION-SM | 13-verification/acceptance/SLC-05/projection-version-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc05.md |
| TST-QUALIFICATION-RECORD-SM | 13-verification/acceptance/SLC-03/qualification-record-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc03.md |
| TST-REALWORLD-EVENT-SM | 13-verification/acceptance/SLC-02/realworld-event-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-RECONSTRUCTION-SM | 13-verification/acceptance/SLC-12/reconstruction-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc12.md |
| TST-RELATIONSHIP-SM | 13-verification/acceptance/SLC-02/relationship-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-RESOURCE-POOL-SM | 13-verification/acceptance/SLC-09/resource-pool-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc09.md |
| TST-RETENTION-SCHEDULE-SM | 13-verification/acceptance/SLC-12a/retention-schedule-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc12a.md |
| TST-RISK-SM | 13-verification/acceptance/SLC-17/risk-state-machine.md | 1 | 15-traceability/trace-slc17.md |
| TST-ROLE-ASSIGNMENT-SM | 13-verification/acceptance/SLC-01/role-assignment-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-ROLE-REQUIREMENT-SM | 13-verification/acceptance/SLC-09/role-requirement-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc09.md |
| TST-ROLE-SM | 13-verification/acceptance/SLC-01/role-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-SCENARIO-SM | 13-verification/acceptance/SLC-19/scenario-state-machine.md | 1 | 15-traceability/trace-slc19.md |
| TST-SECURITY-EXCEPTION-SM | 13-verification/acceptance/SLC-01/security-exception-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-SENSOR-STREAM-SM | 13-verification/acceptance/SLC-16/sensor-stream-state-machine.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc16.md |
| TST-SERVICE-ACCOUNT-SM | 13-verification/acceptance/SLC-01/service-account-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-SHIPMENT-SM | 13-verification/acceptance/SLC-18/shipment-state-machine.md | 1 | 15-traceability/trace-slc18.md |
| TST-SIMULATION-SM | 13-verification/acceptance/SLC-19/simulation-state-machine.md | 1 | 15-traceability/trace-slc19.md |
| TST-SITUATION-SM | 13-verification/acceptance/SLC-06/situation-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc06.md |
| TST-SLC01-INVARIANTS | 13-verification/acceptance/SLC-01/invariants-slc01.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-SLC02-INVARIANTS | 13-verification/acceptance/SLC-02/invariants-slc02.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-SLC03-INVARIANTS | 13-verification/acceptance/SLC-03/invariants-slc03.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc03.md |
| TST-SLC04-INVARIANTS | 13-verification/acceptance/SLC-04/invariants-slc04.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc04.md |
| TST-SLC05-INVARIANTS | 13-verification/acceptance/SLC-05/invariants-slc05.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc05.md |
| TST-SLC06-INVARIANTS | 13-verification/acceptance/SLC-06/invariants-slc06.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc06.md |
| TST-SLC07-INVARIANTS | 13-verification/acceptance/SLC-07/invariants-slc07.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc07.md |
| TST-SLC08-INVARIANTS | 13-verification/acceptance/SLC-08/invariants-slc08.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc08.md |
| TST-SLC09-INVARIANTS | 13-verification/acceptance/SLC-09/invariants-slc09.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc09.md |
| TST-SLC10-INVARIANTS | 13-verification/acceptance/SLC-10/invariants-slc10.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc10.md |
| TST-SLC11-INVARIANTS | 13-verification/acceptance/SLC-11/invariants-slc11.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc11.md |
| TST-SLC12A-INVARIANTS | 13-verification/acceptance/SLC-12a/invariants-slc12a.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc12a.md |
| TST-SLC12-INVARIANTS | 13-verification/acceptance/SLC-12/invariants-slc12.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc12.md |
| TST-SLC14-INVARIANTS | 13-verification/acceptance/SLC-14/invariants-slc14.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc14.md |
| TST-SLC15-INVARIANTS | 13-verification/acceptance/SLC-15/invariants-slc15.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc15.md |
| TST-SLC16-INVARIANTS | 13-verification/acceptance/SLC-16/invariants-slc16.md | 2 | 15-traceability/rtm-r2.md; 15-traceability/trace-slc16.md |
| TST-SLC17-INVARIANTS | 13-verification/acceptance/SLC-17/invariants-slc17.md | 2 | 15-traceability/quality-verification-matrix.md; 15-traceability/trace-slc17.md |
| TST-SLC18-INVARIANTS | 13-verification/acceptance/SLC-18/invariants-slc18.md | 1 | 15-traceability/trace-slc18.md |
| TST-SLC19-INVARIANTS | 13-verification/acceptance/SLC-19/invariants-slc19.md | 1 | 15-traceability/trace-slc19.md |
| TST-SOURCE-SM | 13-verification/acceptance/SLC-02/source-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc02.md |
| TST-SUBSCRIPTION-SM | 13-verification/acceptance/SLC-06/subscription-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc06.md |
| TST-SYNC-CONFLICT-SM | 13-verification/acceptance/SLC-11/sync-conflict-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc11.md |
| TST-SYNC-SESSION-SM | 13-verification/acceptance/SLC-11/sync-session-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc11.md |
| TST-TASK-SM | 13-verification/acceptance/SLC-03/task-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc03.md |
| TST-TASK-TYPE-SM | 13-verification/acceptance/SLC-03/task-type-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc03.md |
| TST-TENANT-SM | 13-verification/acceptance/SLC-01/tenant-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |
| TST-USER-SM | 13-verification/acceptance/SLC-01/user-state-machine.md | 2 | 15-traceability/rtm-r1.md; 15-traceability/trace-slc01.md |

### Family: UC

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| UC-001 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-002 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-003 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-004 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-005 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-006 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-007 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-008 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-010 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-011 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-012 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-013 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-014 | 02-requirements/use-cases.md | 2 | 02-requirements/requirements.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| UC-015 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-016 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-020 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-021 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-022 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-023 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-024 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-030 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-031 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-032 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-033 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-034 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-035 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-036 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-040 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-041 | 02-requirements/use-cases.md | 3 | 00-governance/glossary.md; 00-governance/registers/corrections.md; 02-requirements/requirements.md |
| UC-042 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-043 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-044 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-045 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-046 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-050 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-051 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-052 | 02-requirements/use-cases.md | 2 | 02-requirements/requirements.md; 16-reports/REQUIREMENTS-QUALITY-REPORT-R2.md |
| UC-053 | 02-requirements/use-cases.md | 3 | 00-governance/glossary.md; 00-governance/registers/corrections.md; 02-requirements/requirements.md |
| UC-054 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-055 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-060 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-061 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-062 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-063 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-064 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-065 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-070 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-071 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-072 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-073 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-074 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-080 | 02-requirements/use-cases.md | 2 | 00-governance/registers/open-questions.md; 02-requirements/requirements.md |
| UC-081 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-082 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-083 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-084 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-085 | 02-requirements/use-cases.md | 2 | 00-governance/registers/corrections.md; 02-requirements/requirements.md |
| UC-086 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-087 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-088 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-089 | 02-requirements/use-cases.md | 2 | 00-governance/registers/corrections.md; 02-requirements/requirements.md |
| UC-090 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-091 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-092 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-093 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-094 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-095 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-096 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-097 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-098 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-099 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-101 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-102 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-103 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-104 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-105 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-110 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-111 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-112 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-120 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-121 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-122 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-130 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-131 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-132 | 02-requirements/use-cases.md | 1 | 02-requirements/requirements.md |
| UC-CAT | 02-requirements/use-cases.md | 0 |  |

### Family: UI

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| UI-ARCHITECTURE | 12-solution/ui-architecture.md | 1 | 15-traceability/trace-platform.md |

### Family: UNK

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| UNK-001 | 00-governance/registers/unknowns.md | 3 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 16-reports/gate-reports/GATE-STATUS-W0.md |
| UNK-002 | 00-governance/registers/unknowns.md;01-business/system-definition.md | 20 | README.md; 00-governance/RATIFICATION-PACKAGE.md; 00-governance/decisions/ADR-P04.md; 00-governance/decisions/ADR-P08.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-question ...(truncated) |
| UNK-003 | 00-governance/registers/unknowns.md | 3 | 00-governance/decisions/ADR-P05.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md |
| UNK-004 | 00-governance/registers/unknowns.md | 4 | 00-governance/decisions/ADR-P04.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 00-governance/registers/assumptions.md |
| UNK-005 | 00-governance/registers/unknowns.md | 2 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md |
| UNK-006 | 00-governance/registers/unknowns.md | 4 | 00-governance/decisions/ADR-P04.md; 00-governance/decisions/ADR-P06.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md |
| UNK-007 | 00-governance/registers/unknowns.md | 6 | 00-governance/decisions/ADR-P01.md; 00-governance/decisions/ADR-P03.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 16-reports/SESSION-W0.md; 16-reports/gate-re ...(truncated) |
| UNK-008 | 00-governance/registers/unknowns.md | 2 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md |
| UNK-009 | 00-governance/registers/unknowns.md | 3 | 00-governance/decisions/ADR-P09.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md |
| UNK-010 | 00-governance/registers/unknowns.md | 6 | 00-governance/decisions/ADR-P12.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 00-governance/registers/dependencies.md; 01-business/release-2-scope.md; 16-repo ...(truncated) |
| UNK-011 | 00-governance/registers/unknowns.md | 4 | 00-governance/decisions/ADR-P15.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 00-governance/registers/assumptions.md |
| UNK-012 | 00-governance/registers/unknowns.md;01-business/system-definition.md | 25 | 00-governance/RATIFICATION-PACKAGE.md; 00-governance/decisions/ADR-P05.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 00-governance/registers/assumptions.md; 0 ...(truncated) |
| UNK-013 | 00-governance/registers/unknowns.md | 2 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md |
| UNK-014 | 00-governance/registers/unknowns.md | 3 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 12-solution/release-configuration-migration.md |
| UNK-015 | 00-governance/registers/unknowns.md | 3 | 00-governance/decisions/ADR-P01.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md |
| UNK-016 | 00-governance/registers/unknowns.md | 4 | 02-requirements/quality-scenarios.md; 16-reports/SESSION-W1.md; 16-reports/SESSION-W2.md; 16-reports/gate-reports/GATE-STATUS-W1.md |
| UNK-017 | 00-governance/registers/unknowns.md | 2 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md |
| UNK-018 | 00-governance/registers/unknowns.md | 6 | 00-governance/glossary.md; 00-governance/decisions/ADR-P04.md; 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 00-governance/registers/assumptions.md; 16-reports/ga ...(truncated) |
| UNK-019 | 00-governance/registers/unknowns.md | 3 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 16-reports/gate-reports/GATE-STATUS-W0.md |
| UNK-020 | 00-governance/registers/unknowns.md | 3 | 00-governance/elicitation/W1-answers.md; 00-governance/elicitation/W1-questions.md; 00-governance/registers/assumptions.md |
| UNK-021 | 00-governance/registers/unknowns.md | 10 | 01-business/release-2-scope.md; 03-domain/contexts/BC07/enterprise-integration-spec.md; 14-slices/slices.md; 14-slices/SLC-16/readiness.md; 16-reports/ARCHITECTURE-REVIEW-R2.md; 16-reports/CONSISTENCY ...(truncated) |
| UNK-022 | 00-governance/registers/unknowns.md | 3 | README.md; 01-business/release-3-scope.md; 16-reports/EVOLUTION-ROADMAP.md |

### Family: VALUE

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| VALUE-STREAMS | 01-business/value-streams.md | 0 |  |

### Family: WL

| id | defined_in | ext_ref_count | ext_files |
|---|---|---|---|
| WL-01 | 07-quality/workloads-slc01.md;07-quality/workloads-slc02.md;07-quality/workloads-slc03.md;07-quality/workloads-slc07.md;07-quality/workloads-slc08.md;07-quality/workloads-slc09.md;07-quality/workloads-slc15.md;07-quality/workloads.md | 9 | 00-governance/registers/assumptions.md; 00-governance/registers/unknowns.md; 02-requirements/quality-scenarios.md; 07-quality/performance-test-strategy.md; 07-quality/workloads-slc17.md; 07-quality/wo ...(truncated) |
| WL-02 | 07-quality/workloads-slc05.md;07-quality/workloads.md | 3 | 00-governance/decisions/ADR-P05.md; 02-requirements/quality-scenarios.md; 15-traceability/quality-verification-matrix.md |
| WL-03 | 07-quality/workloads-slc02.md;07-quality/workloads-slc06.md;07-quality/workloads.md | 5 | 00-governance/decisions/ADR-P12.md; 00-governance/registers/assumptions.md; 02-requirements/quality-scenarios.md; 15-traceability/quality-verification-matrix.md; 16-reports/REQUIREMENTS-QUALITY-REPORT ...(truncated) |
| WL-04 | 07-quality/workloads-slc02.md;07-quality/workloads-slc12.md;07-quality/workloads.md | 3 | 00-governance/decisions/ADR-P02.md; 02-requirements/quality-scenarios.md; 15-traceability/quality-verification-matrix.md |
| WL-05 | 07-quality/workloads-slc02.md;07-quality/workloads-slc16.md;07-quality/workloads.md | 0 |  |
| WL-06 | 07-quality/workloads-slc02.md;07-quality/workloads-slc06.md;07-quality/workloads-slc14.md;07-quality/workloads-slc16.md;07-quality/workloads.md | 7 | 00-governance/decisions/ADR-P05.md; 00-governance/decisions/ADR-P07.md; 00-governance/registers/assumptions.md; 00-governance/registers/unknowns.md; 02-requirements/quality-scenarios.md; 03-domain/bc- ...(truncated) |
| WL-07 | 07-quality/workloads-slc15.md | 0 |  |
| WL-08 | 07-quality/workloads-slc04.md;07-quality/workloads-slc05.md;07-quality/workloads.md | 5 | 00-governance/decisions/ADR-P05.md; 00-governance/registers/assumptions.md; 02-requirements/quality-scenarios.md; 15-traceability/quality-verification-matrix.md; 16-reports/REQUIREMENTS-QUALITY-REPORT ...(truncated) |
| WL-09 | 07-quality/workloads-slc10.md;07-quality/workloads.md | 1 | 07-quality/workloads-slc18.md |
| WL-10 | 07-quality/workloads-slc10.md | 0 |  |
| WL-11 | 07-quality/workloads-slc02.md;07-quality/workloads-slc07.md;07-quality/workloads.md | 4 | 00-governance/registers/unknowns.md; 02-requirements/quality-scenarios.md; 15-traceability/quality-verification-matrix.md; 16-reports/REQUIREMENTS-QUALITY-REPORT.md |
| WL-12 | 07-quality/workloads-slc11.md;07-quality/workloads.md | 2 | 02-requirements/quality-scenarios.md; 15-traceability/quality-verification-matrix.md |
| WL-13 | 07-quality/workloads-slc06.md;07-quality/workloads-slc12.md;07-quality/workloads-slc16.md | 0 |  |
| WL-14 | 07-quality/workloads-slc12.md;07-quality/workloads-slc12a.md | 2 | 02-requirements/quality-scenarios.md; 15-traceability/quality-verification-matrix.md |
| WL-15 | 07-quality/workloads.md | 2 | 02-requirements/quality-scenarios.md; 15-traceability/quality-verification-matrix.md |
| WL-16 | 07-quality/workloads.md | 0 |  |
| WL-17 | 07-quality/workloads-slc17.md | 0 |  |
| WL-18 | 07-quality/workloads-slc18.md | 0 |  |
| WL-19 | 07-quality/workloads-slc19.md | 0 |  |
| WL-SLC01 | 07-quality/workloads-slc01.md | 0 |  |
| WL-SLC02 | 07-quality/workloads-slc02.md | 0 |  |
| WL-SLC03 | 07-quality/workloads-slc03.md | 0 |  |
| WL-SLC04 | 07-quality/workloads-slc04.md | 0 |  |
| WL-SLC05 | 07-quality/workloads-slc05.md | 0 |  |
| WL-SLC06 | 07-quality/workloads-slc06.md | 0 |  |
| WL-SLC07 | 07-quality/workloads-slc07.md | 0 |  |
| WL-SLC08 | 07-quality/workloads-slc08.md | 0 |  |
| WL-SLC09 | 07-quality/workloads-slc09.md | 0 |  |
| WL-SLC10 | 07-quality/workloads-slc10.md | 0 |  |
| WL-SLC11 | 07-quality/workloads-slc11.md | 0 |  |
| WL-SLC12 | 07-quality/workloads-slc12.md | 0 |  |
| WL-SLC12A | 07-quality/workloads-slc12a.md | 0 |  |
| WL-SLC14 | 07-quality/workloads-slc14.md | 0 |  |
| WL-SLC15 | 07-quality/workloads-slc15.md | 0 |  |
| WL-SLC16 | 07-quality/workloads-slc16.md | 0 |  |
| WL-SLC17 | 07-quality/workloads-slc17.md | 0 |  |
| WL-SLC18 | 07-quality/workloads-slc18.md | 0 |  |
| WL-SLC19 | 07-quality/workloads-slc19.md | 0 |  |
