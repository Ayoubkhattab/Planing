---
id: EVT-CAT-BC03-SLC07
type: event-catalog
title: Domain Events — BC03 (SLC-07)
wave: W4
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC03 (SLC-07)

_35 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-ACS-CREATED | AGG-ANALYSIS-CASE | CMD-ACS-CREATE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-DEFINED | AGG-ANALYSIS-CASE | CMD-ACS-DEFINE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-OPENED | AGG-ANALYSIS-CASE | CMD-ACS-OPEN | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-HYPOTHESIS-ADDED | AGG-ANALYSIS-CASE | CMD-ACS-ADD-HYPOTHESIS | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-HYPOTHESIS-UPDATED | AGG-ANALYSIS-CASE | CMD-ACS-UPDATE-HYPOTHESIS | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-ASSUMPTION-ADDED | AGG-ANALYSIS-CASE | CMD-ACS-ADD-ASSUMPTION | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-ASSUMPTION-RETIRED | AGG-ANALYSIS-CASE | CMD-ACS-RETIRE-ASSUMPTION | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-EVIDENCE-SELECTED | AGG-ANALYSIS-CASE | CMD-ACS-SELECT-EVIDENCE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-EVIDENCE-DESELECTED | AGG-ANALYSIS-CASE | CMD-ACS-DESELECT-EVIDENCE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-SCENARIO-DEFINED | AGG-ANALYSIS-CASE | CMD-ACS-DEFINE-SCENARIO | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-CLOSED | AGG-ANALYSIS-CASE | CMD-ACS-CLOSE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-REOPENED | AGG-ANALYSIS-CASE | CMD-ACS-REOPEN | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-CANCELLED | AGG-ANALYSIS-CASE | CMD-ACS-CANCEL | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ACS-RECLASSIFIED | AGG-ANALYSIS-CASE | CMD-ACS-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-AMT-REGISTERED | AGG-ANALYSIS-METHOD | CMD-AMT-REGISTER | — | Job scheduler (image allow-list) | tenant_id + aggregate.id |
| EVT-AMT-ACTIVATED | AGG-ANALYSIS-METHOD | CMD-AMT-ACTIVATE | — | Job scheduler (image allow-list) | tenant_id + aggregate.id |
| EVT-AMT-DEPRECATED | AGG-ANALYSIS-METHOD | CMD-AMT-DEPRECATE | — | Job scheduler (image allow-list) | tenant_id + aggregate.id |
| EVT-AMT-RETIRED | AGG-ANALYSIS-METHOD | CMD-AMT-RETIRE | — | Job scheduler (image allow-list) | tenant_id + aggregate.id |
| EVT-RUN-QUEUED | AGG-ANALYSIS-RUN | CMD-RUN-SUBMIT, CMD-RUN-REPRODUCE | — | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification | tenant_id + aggregate.id |
| EVT-RUN-STARTED | AGG-ANALYSIS-RUN | SYS:worker lease acquired | — | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification | tenant_id + aggregate.id |
| EVT-RUN-SUCCEEDED | AGG-ANALYSIS-RUN | SYS:completed | — | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification | tenant_id + aggregate.id |
| EVT-RUN-FAILED | AGG-ANALYSIS-RUN | SYS:error or timeout | — | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification | tenant_id + aggregate.id |
| EVT-RUN-CANCELLED | AGG-ANALYSIS-RUN | CMD-RUN-CANCEL | — | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification | tenant_id + aggregate.id |
| EVT-FND-RECORDED | AGG-FINDING | CMD-FND-RECORD | — | Assessment review flags | tenant_id + aggregate.id |
| EVT-FND-EDITED | AGG-FINDING | CMD-FND-EDIT | — | Assessment review flags | tenant_id + aggregate.id |
| EVT-FND-ACCEPTED | AGG-FINDING | CMD-FND-ACCEPT | — | Assessment review flags | tenant_id + aggregate.id |
| EVT-FND-WITHDRAWN | AGG-FINDING | CMD-FND-WITHDRAW | — | Assessment review flags | tenant_id + aggregate.id |
| EVT-ASM-DRAFTED | AGG-ASSESSMENT | CMD-ASM-DRAFT | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) | tenant_id + aggregate.id |
| EVT-ASM-EDITED | AGG-ASSESSMENT | CMD-ASM-EDIT | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) | tenant_id + aggregate.id |
| EVT-ASM-SUBMITTED | AGG-ASSESSMENT | CMD-ASM-SUBMIT | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) | tenant_id + aggregate.id |
| EVT-ASM-RETURNED | AGG-ASSESSMENT | CMD-ASM-RETURN | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) | tenant_id + aggregate.id |
| EVT-ASM-PUBLISHED | AGG-ASSESSMENT | CMD-ASM-PUBLISH | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) | tenant_id + aggregate.id |
| EVT-ASM-SUPERSEDED | AGG-ASSESSMENT | SYS:newer version published | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) | tenant_id + aggregate.id |
| EVT-ASM-WITHDRAWN | AGG-ASSESSMENT | CMD-ASM-WITHDRAW | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) | tenant_id + aggregate.id |
| EVT-ASM-DISCARDED | AGG-ASSESSMENT | CMD-ASM-DISCARD | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
