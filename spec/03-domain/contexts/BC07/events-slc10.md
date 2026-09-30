---
id: EVT-CAT-BC07-SLC10
type: event-catalog
title: Domain Events — BC07 (SLC-10)
wave: W4
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC07 (SLC-10)

_37 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-AIR-RECEIVED | AGG-AI-REQUEST | CMD-AIR-SUBMIT | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) | tenant_id + aggregate.id |
| EVT-AIR-REFUSED | AGG-AI-REQUEST | SYS:policy denied | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) | tenant_id + aggregate.id |
| EVT-AIR-RETRIEVING | AGG-AI-REQUEST | SYS:retrieval started | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) | tenant_id + aggregate.id |
| EVT-AIR-CONTEXT-SEALED | AGG-AI-REQUEST | SYS:context package sealed | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) | tenant_id + aggregate.id |
| EVT-AIR-INSUFFICIENT-EVIDENCE | AGG-AI-REQUEST | SYS:no sufficient evidence retrieved, SYS:output not grounded | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) | tenant_id + aggregate.id |
| EVT-AIR-COMPLETED | AGG-AI-REQUEST | SYS:output grounded | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) | tenant_id + aggregate.id |
| EVT-AIR-FAILED | AGG-AI-REQUEST | SYS:error or timeout | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) | tenant_id + aggregate.id |
| EVT-AIR-CANCELLED | AGG-AI-REQUEST | CMD-AIR-CANCEL | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) | tenant_id + aggregate.id |
| EVT-AIRS-PROPOSED | AGG-AI-RESULT | SYS:request COMPLETED for a reviewable operation | — | Owner contexts (effects on acceptance); Evaluation feedback store | tenant_id + aggregate.id |
| EVT-AIRS-REVIEW-STARTED | AGG-AI-RESULT | CMD-AIRS-START-REVIEW | — | Owner contexts (effects on acceptance); Evaluation feedback store | tenant_id + aggregate.id |
| EVT-AIRS-ACCEPTED | AGG-AI-RESULT | CMD-AIRS-ACCEPT | — | Owner contexts (effects on acceptance); Evaluation feedback store | tenant_id + aggregate.id |
| EVT-AIRS-PARTIALLY-ACCEPTED | AGG-AI-RESULT | CMD-AIRS-ACCEPT-PARTIALLY | — | Owner contexts (effects on acceptance); Evaluation feedback store | tenant_id + aggregate.id |
| EVT-AIRS-REJECTED | AGG-AI-RESULT | CMD-AIRS-REJECT | — | Owner contexts (effects on acceptance); Evaluation feedback store | tenant_id + aggregate.id |
| EVT-MDL-REGISTERED | AGG-MODEL-VERSION | CMD-MDL-REGISTER | — | Inference servers (load/unload); Routing validation | tenant_id + aggregate.id |
| EVT-MDL-EVALUATION-STARTED | AGG-MODEL-VERSION | CMD-MDL-START-EVALUATION | — | Inference servers (load/unload); Routing validation | tenant_id + aggregate.id |
| EVT-MDL-APPROVED | AGG-MODEL-VERSION | CMD-MDL-APPROVE | — | Inference servers (load/unload); Routing validation | tenant_id + aggregate.id |
| EVT-MDL-EVALUATION-FAILED | AGG-MODEL-VERSION | CMD-MDL-FAIL-EVALUATION | — | Inference servers (load/unload); Routing validation | tenant_id + aggregate.id |
| EVT-MDL-STAGED | AGG-MODEL-VERSION | CMD-MDL-STAGE | — | Inference servers (load/unload); Routing validation | tenant_id + aggregate.id |
| EVT-MDL-PROMOTED | AGG-MODEL-VERSION | CMD-MDL-PROMOTE | — | Inference servers (load/unload); Routing validation | tenant_id + aggregate.id |
| EVT-MDL-DRIFT-DETECTED | AGG-MODEL-VERSION | SYS:monitoring drift detected | — | Inference servers (load/unload); Routing validation | tenant_id + aggregate.id |
| EVT-MDL-DEPRECATED | AGG-MODEL-VERSION | CMD-MDL-DEPRECATE | — | Inference servers (load/unload); Routing validation | tenant_id + aggregate.id |
| EVT-MDL-REINSTATED | AGG-MODEL-VERSION | CMD-MDL-REINSTATE | — | Inference servers (load/unload); Routing validation | tenant_id + aggregate.id |
| EVT-MDL-RETIRED | AGG-MODEL-VERSION | CMD-MDL-RETIRE | — | Inference servers (load/unload); Routing validation | tenant_id + aggregate.id |
| EVT-RTG-DRAFTED | AGG-AI-ROUTING | CMD-RTG-DRAFT | — | Model router; PEP cache | tenant_id + aggregate.id |
| EVT-RTG-EDITED | AGG-AI-ROUTING | CMD-RTG-EDIT | — | Model router; PEP cache | tenant_id + aggregate.id |
| EVT-RTG-ACTIVATED | AGG-AI-ROUTING | CMD-RTG-ACTIVATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Model router; PEP cache | tenant_id + aggregate.id |
| EVT-RTG-DISCARDED | AGG-AI-ROUTING | CMD-RTG-DISCARD | — | Model router; PEP cache | tenant_id + aggregate.id |
| EVT-RTG-SUPERSEDED | AGG-AI-ROUTING | SYS:successor activated | — | Model router; PEP cache | tenant_id + aggregate.id |
| EVT-TOL-REGISTERED | AGG-AI-TOOL | CMD-TOL-REGISTER | — | Tool gateway | tenant_id + aggregate.id |
| EVT-TOL-ACTIVATED | AGG-AI-TOOL | CMD-TOL-ACTIVATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Tool gateway | tenant_id + aggregate.id |
| EVT-TOL-DISABLED | AGG-AI-TOOL | CMD-TOL-DISABLE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Tool gateway | tenant_id + aggregate.id |
| EVT-TOL-ENABLED | AGG-AI-TOOL | CMD-TOL-ENABLE | — | Tool gateway | tenant_id + aggregate.id |
| EVT-TOL-RETIRED | AGG-AI-TOOL | CMD-TOL-RETIRE | — | Tool gateway | tenant_id + aggregate.id |
| EVT-EVS-DRAFTED | AGG-EVAL-SUITE | CMD-EVS-DRAFT | — | Evaluation runner | tenant_id + aggregate.id |
| EVT-EVS-EDITED | AGG-EVAL-SUITE | CMD-EVS-EDIT | — | Evaluation runner | tenant_id + aggregate.id |
| EVT-EVS-ACTIVATED | AGG-EVAL-SUITE | CMD-EVS-ACTIVATE | — | Evaluation runner | tenant_id + aggregate.id |
| EVT-EVS-SUPERSEDED | AGG-EVAL-SUITE | SYS:successor activated | — | Evaluation runner | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
