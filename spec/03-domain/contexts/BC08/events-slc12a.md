---
id: EVT-CAT-BC08-SLC12A
type: event-catalog
title: Domain Events — BC08 (SLC-12a)
wave: W4
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC08 (SLC-12a)

_25 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-RTS-DRAFTED | AGG-RETENTION-SCHEDULE | CMD-RTS-DRAFT | — | Disposition planner; Key-bucket policy (class period sizing) | tenant_id + aggregate.id |
| EVT-RTS-EDITED | AGG-RETENTION-SCHEDULE | CMD-RTS-EDIT | — | Disposition planner; Key-bucket policy (class period sizing) | tenant_id + aggregate.id |
| EVT-RTS-ACTIVATED | AGG-RETENTION-SCHEDULE | CMD-RTS-ACTIVATE | — | Disposition planner; Key-bucket policy (class period sizing) | tenant_id + aggregate.id |
| EVT-RTS-DISCARDED | AGG-RETENTION-SCHEDULE | CMD-RTS-DISCARD | — | Disposition planner; Key-bucket policy (class period sizing) | tenant_id + aggregate.id |
| EVT-RTS-SUPERSEDED | AGG-RETENTION-SCHEDULE | SYS:successor activated | — | Disposition planner; Key-bucket policy (class period sizing) | tenant_id + aggregate.id |
| EVT-LHD-PLACED | AGG-LEGAL-HOLD | CMD-LHD-PLACE | — | HoldCheck cache (all owners); Disposition planner; Erasure executor | tenant_id + aggregate.id |
| EVT-LHD-EXTENDED | AGG-LEGAL-HOLD | CMD-LHD-EXTEND | — | HoldCheck cache (all owners); Disposition planner; Erasure executor | tenant_id + aggregate.id |
| EVT-LHD-RELEASE-REQUESTED | AGG-LEGAL-HOLD | CMD-LHD-REQUEST-RELEASE | — | HoldCheck cache (all owners); Disposition planner; Erasure executor | tenant_id + aggregate.id |
| EVT-LHD-RELEASED | AGG-LEGAL-HOLD | CMD-LHD-APPROVE-RELEASE | — | HoldCheck cache (all owners); Disposition planner; Erasure executor | tenant_id + aggregate.id |
| EVT-LHD-RELEASE-CANCELLED | AGG-LEGAL-HOLD | CMD-LHD-CANCEL-RELEASE | — | HoldCheck cache (all owners); Disposition planner; Erasure executor | tenant_id + aggregate.id |
| EVT-DSP-PLANNED | AGG-DISPOSITION-RUN | SYS:scheduled evaluation (daily) | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit | tenant_id + aggregate.id |
| EVT-DSP-SUBMITTED | AGG-DISPOSITION-RUN | CMD-DSP-SUBMIT | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit | tenant_id + aggregate.id |
| EVT-DSP-APPROVED | AGG-DISPOSITION-RUN | CMD-DSP-APPROVE | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit | tenant_id + aggregate.id |
| EVT-DSP-EXECUTING | AGG-DISPOSITION-RUN | SYS:execution started | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit | tenant_id + aggregate.id |
| EVT-DSP-COMPLETED | AGG-DISPOSITION-RUN | SYS:all buckets processed | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit | tenant_id + aggregate.id |
| EVT-DSP-COMPLETED-WITH-EXCEPTIONS | AGG-DISPOSITION-RUN | SYS:some buckets failed | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit | tenant_id + aggregate.id |
| EVT-DSP-CANCELLED | AGG-DISPOSITION-RUN | CMD-DSP-CANCEL | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit | tenant_id + aggregate.id |
| EVT-ERS-RECEIVED | AGG-ERASURE-REQUEST | CMD-ERS-REGISTER | — | Key manager (subject key destruction); BC01 / BC02 (scope + confirmation); Projections (purge) | tenant_id + aggregate.id |
| EVT-ERS-SCOPED | AGG-ERASURE-REQUEST | SYS:subject scope resolved | — | Key manager (subject key destruction); BC01 / BC02 (scope + confirmation); Projections (purge) | tenant_id + aggregate.id |
| EVT-ERS-APPROVED | AGG-ERASURE-REQUEST | CMD-ERS-APPROVE | — | Key manager (subject key destruction); BC01 / BC02 (scope + confirmation); Projections (purge) | tenant_id + aggregate.id |
| EVT-ERS-REJECTED | AGG-ERASURE-REQUEST | CMD-ERS-REJECT | — | Key manager (subject key destruction); BC01 / BC02 (scope + confirmation); Projections (purge) | tenant_id + aggregate.id |
| EVT-ERS-BLOCKED | AGG-ERASURE-REQUEST | SYS:hold matches subject | — | Key manager (subject key destruction); BC01 / BC02 (scope + confirmation); Projections (purge) | tenant_id + aggregate.id |
| EVT-ERS-UNBLOCKED | AGG-ERASURE-REQUEST | SYS:hold released | — | Key manager (subject key destruction); BC01 / BC02 (scope + confirmation); Projections (purge) | tenant_id + aggregate.id |
| EVT-ERS-EXECUTING | AGG-ERASURE-REQUEST | SYS:execution started | — | Key manager (subject key destruction); BC01 / BC02 (scope + confirmation); Projections (purge) | tenant_id + aggregate.id |
| EVT-ERS-COMPLETED | AGG-ERASURE-REQUEST | SYS:all contexts confirmed | — | Key manager (subject key destruction); BC01 / BC02 (scope + confirmation); Projections (purge) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
