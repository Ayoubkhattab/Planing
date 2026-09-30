---
id: EVT-CAT-BC06-SLC12
type: event-catalog
title: Domain Events — BC06 (SLC-12)
wave: W4
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC06 (SLC-12)

_42 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-PTM-DEFINED | AGG-PRODUCT-TEMPLATE | CMD-PTM-DEFINE | — | Product generator | tenant_id + aggregate.id |
| EVT-PTM-EDITED | AGG-PRODUCT-TEMPLATE | CMD-PTM-EDIT | — | Product generator | tenant_id + aggregate.id |
| EVT-PTM-ACTIVATED | AGG-PRODUCT-TEMPLATE | CMD-PTM-ACTIVATE | — | Product generator | tenant_id + aggregate.id |
| EVT-PTM-RETIRED | AGG-PRODUCT-TEMPLATE | CMD-PTM-RETIRE | — | Product generator | tenant_id + aggregate.id |
| EVT-PRD-CREATED | AGG-PRODUCT | CMD-PRD-CREATE | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-PRD-GENERATION-STARTED | AGG-PRODUCT | CMD-PRD-GENERATE | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-PRD-GENERATED | AGG-PRODUCT | SYS:generation succeeded | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-PRD-GENERATION-FAILED | AGG-PRODUCT | SYS:generation failed | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-PRD-NARRATIVE-EDITED | AGG-PRODUCT | CMD-PRD-EDIT-NARRATIVE | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-PRD-SUBMITTED | AGG-PRODUCT | CMD-PRD-SUBMIT | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-PRD-RETURNED | AGG-PRODUCT | CMD-PRD-RETURN | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-PRD-APPROVED | AGG-PRODUCT | CMD-PRD-APPROVE | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-PRD-SUPERSEDED | AGG-PRODUCT | SYS:newer version approved | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-PRD-WITHDRAWN | AGG-PRODUCT | CMD-PRD-WITHDRAW | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-PRD-DISCARDED | AGG-PRODUCT | CMD-PRD-DISCARD | — | Distribution; Search projection (SLC-05); Notification (reviewers) | tenant_id + aggregate.id |
| EVT-DST-STARTED | AGG-DISTRIBUTION | CMD-DST-DISTRIBUTE | — | Notification (recipients); Audit | tenant_id + aggregate.id |
| EVT-DST-COMPLETED | AGG-DISTRIBUTION | SYS:all recipients authorized and delivered | — | Notification (recipients); Audit | tenant_id + aggregate.id |
| EVT-DST-COMPLETED-WITH-EXCLUSIONS | AGG-DISTRIBUTION | SYS:some recipients not authorized | — | Notification (recipients); Audit | tenant_id + aggregate.id |
| EVT-DST-CANCELLED | AGG-DISTRIBUTION | CMD-DST-CANCEL | — | Notification (recipients); Audit | tenant_id + aggregate.id |
| EVT-KNO-DRAFTED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-DRAFT | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) | tenant_id + aggregate.id |
| EVT-KNO-EDITED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-EDIT | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) | tenant_id + aggregate.id |
| EVT-KNO-SUBMITTED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-SUBMIT | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) | tenant_id + aggregate.id |
| EVT-KNO-RETURNED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-RETURN | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) | tenant_id + aggregate.id |
| EVT-KNO-PUBLISHED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-PUBLISH | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) | tenant_id + aggregate.id |
| EVT-KNO-REJECTED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-REJECT | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) | tenant_id + aggregate.id |
| EVT-KNO-REUSED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-RECORD-REUSE | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) | tenant_id + aggregate.id |
| EVT-KNO-SUPERSEDED | AGG-KNOWLEDGE-OBJECT | SYS:newer version published | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) | tenant_id + aggregate.id |
| EVT-KNO-RETIRED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-RETIRE | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) | tenant_id + aggregate.id |
| EVT-KNO-DISCARDED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-DISCARD | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) | tenant_id + aggregate.id |
| EVT-ARC-INGEST-STARTED | AGG-ARCHIVE-PACKAGE | SYS:disposition action ARCHIVE for a bucket or record set, CMD-ARC-RETRY-INGEST | — | Archive catalogue; Disposition (SLC-12a); Audit | tenant_id + aggregate.id |
| EVT-ARC-ARCHIVED | AGG-ARCHIVE-PACKAGE | SYS:package validated | — | Archive catalogue; Disposition (SLC-12a); Audit | tenant_id + aggregate.id |
| EVT-ARC-INGEST-FAILED | AGG-ARCHIVE-PACKAGE | SYS:validation failed | — | Archive catalogue; Disposition (SLC-12a); Audit | tenant_id + aggregate.id |
| EVT-ARC-INTEGRITY-FAILED | AGG-ARCHIVE-PACKAGE | SYS:integrity check failed | — | Archive catalogue; Disposition (SLC-12a); Audit | tenant_id + aggregate.id |
| EVT-ARC-REPAIRED | AGG-ARCHIVE-PACKAGE | CMD-ARC-REPAIR | — | Archive catalogue; Disposition (SLC-12a); Audit | tenant_id + aggregate.id |
| EVT-ARC-FORMAT-MIGRATED | AGG-ARCHIVE-PACKAGE | CMD-ARC-MIGRATE-FORMAT | — | Archive catalogue; Disposition (SLC-12a); Audit | tenant_id + aggregate.id |
| EVT-ARC-TRANSFERRED | AGG-ARCHIVE-PACKAGE | CMD-ARC-TRANSFER | — | Archive catalogue; Disposition (SLC-12a); Audit | tenant_id + aggregate.id |
| EVT-ARC-DISPOSED | AGG-ARCHIVE-PACKAGE | SYS:disposition DESTROY executed for the package bucket | — | Archive catalogue; Disposition (SLC-12a); Audit | tenant_id + aggregate.id |
| EVT-REC-REQUESTED | AGG-RECONSTRUCTION | CMD-REC-REQUEST | — | Requester notification; Audit | tenant_id + aggregate.id |
| EVT-REC-STARTED | AGG-RECONSTRUCTION | SYS:worker started | — | Requester notification; Audit | tenant_id + aggregate.id |
| EVT-REC-COMPLETED | AGG-RECONSTRUCTION | SYS:completed | — | Requester notification; Audit | tenant_id + aggregate.id |
| EVT-REC-FAILED | AGG-RECONSTRUCTION | SYS:failed | — | Requester notification; Audit | tenant_id + aggregate.id |
| EVT-REC-CANCELLED | AGG-RECONSTRUCTION | CMD-REC-CANCEL | — | Requester notification; Audit | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
