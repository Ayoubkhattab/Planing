---
id: EVT-CAT-BC02-SLC02
type: event-catalog
title: Domain Events — BC02 (SLC-02)
wave: W4
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC02 (SLC-02)

_58 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-SRC-REGISTERED | AGG-SOURCE | CMD-SRC-REGISTER | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-SRC-RELIABILITY-RATED | AGG-SOURCE | CMD-SRC-RATE-RELIABILITY | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-SRC-PROFILE-UPDATED | AGG-SOURCE | CMD-SRC-UPDATE-PROFILE | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-SRC-PROTECTION-CHANGED | AGG-SOURCE | CMD-SRC-SET-PROTECTION | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-SRC-RECLASSIFIED | AGG-SOURCE | CMD-SRC-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-SRC-SUSPENDED | AGG-SOURCE | CMD-SRC-SUSPEND | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-SRC-REINSTATED | AGG-SOURCE | CMD-SRC-REINSTATE | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-SRC-RETIRED | AGG-SOURCE | CMD-SRC-RETIRE | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-OBS-RECORDED | AGG-OBSERVATION | CMD-OBS-RECORD | — | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-OBS-AMENDED | AGG-OBSERVATION | CMD-OBS-AMEND | — | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-OBS-EVIDENCE-ATTACHED | AGG-OBSERVATION | CMD-OBS-ATTACH-EVIDENCE | — | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-OBS-RECLASSIFIED | AGG-OBSERVATION | CMD-OBS-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-OBS-VALIDATED | AGG-OBSERVATION | CMD-OBS-VALIDATE | — | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-OBS-REJECTED | AGG-OBSERVATION | CMD-OBS-REJECT | — | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-ENT-REGISTERED | AGG-ENTITY | CMD-ENT-REGISTER | — | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-ENT-TYPE-CHANGED | AGG-ENTITY | CMD-ENT-CHANGE-TYPE | — | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-ENT-RECLASSIFIED | AGG-ENTITY | CMD-ENT-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; ER candidate generator (SLC-04); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-ENT-RETIRED | AGG-ENTITY | CMD-ENT-RETIRE | — | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-ENT-REINSTATED | AGG-ENTITY | CMD-ENT-REINSTATE | — | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-RWE-REGISTERED | AGG-REALWORLD-EVENT | CMD-RWE-REGISTER | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-RWE-TYPE-CHANGED | AGG-REALWORLD-EVENT | CMD-RWE-CHANGE-TYPE | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-RWE-RECLASSIFIED | AGG-REALWORLD-EVENT | CMD-RWE-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-RWE-RETIRED | AGG-REALWORLD-EVENT | CMD-RWE-RETIRE | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-RWE-REINSTATED | AGG-REALWORLD-EVENT | CMD-RWE-REINSTATE | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-REL-REGISTERED | AGG-RELATIONSHIP | CMD-REL-REGISTER | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-REL-RECLASSIFIED | AGG-RELATIONSHIP | CMD-REL-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-REL-RETIRED | AGG-RELATIONSHIP | CMD-REL-RETIRE | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-REL-REINSTATED | AGG-RELATIONSHIP | CMD-REL-REINSTATE | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-CLM-ASSERTED | AGG-CLAIM | CMD-CLM-ASSERT | — | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-CLM-CORRECTED | AGG-CLAIM | CMD-CLM-CORRECT | — | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-CLM-CHANGED | AGG-CLAIM | CMD-CLM-RECORD-CHANGE | — | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-CLM-RETRACTED | AGG-CLAIM | CMD-CLM-RETRACT | — | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-CLM-ASSESSED | AGG-CLAIM | CMD-CLM-ASSESS | — | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-CLM-RECLASSIFIED | AGG-CLAIM | CMD-CLM-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-EVD-REGISTERED | AGG-EVIDENCE | CMD-EVD-REGISTER | — | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EVD-LOCATOR-UPDATED | AGG-EVIDENCE | CMD-EVD-UPDATE-LOCATOR | — | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EVD-SEALED | AGG-EVIDENCE | CMD-EVD-SEAL | — | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EVD-CUSTODY-TRANSFERRED | AGG-EVIDENCE | CMD-EVD-TRANSFER-CUSTODY | — | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EVD-RECLASSIFIED | AGG-EVIDENCE | CMD-EVD-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EVD-WITHDRAWN | AGG-EVIDENCE | CMD-EVD-WITHDRAW | — | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EVL-LINKED | AGG-EVIDENCE-LINK | CMD-EVL-LINK | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-EVL-UNLINKED | AGG-EVIDENCE-LINK | CMD-EVL-UNLINK | — | Search/Graph projections (SLC-05) | tenant_id + aggregate.id |
| EVT-ATT-UPLOAD-INITIATED | AGG-ATTACHMENT | CMD-ATT-INITIATE-UPLOAD | — | Content scanner; Evidence registrar | tenant_id + aggregate.id |
| EVT-ATT-UPLOADED | AGG-ATTACHMENT | CMD-ATT-COMPLETE-UPLOAD | — | Content scanner; Evidence registrar | tenant_id + aggregate.id |
| EVT-ATT-STORED | AGG-ATTACHMENT | SYS:scan passed | — | Content scanner; Evidence registrar | tenant_id + aggregate.id |
| EVT-ATT-QUARANTINED | AGG-ATTACHMENT | SYS:scan failed | — | Content scanner; Evidence registrar | tenant_id + aggregate.id |
| EVT-ATT-EXPIRED | AGG-ATTACHMENT | SYS:upload window 24 h elapsed | — | Content scanner; Evidence registrar | tenant_id + aggregate.id |
| EVT-ATT-ERASED | AGG-ATTACHMENT | CMD-ATT-ERASE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Content scanner; Evidence registrar | tenant_id + aggregate.id |
| EVT-IMP-RECEIVED | AGG-IMPORT-BATCH | CMD-IMP-SUBMIT | — | Import worker; Adapter owner notification | tenant_id + aggregate.id |
| EVT-IMP-PROCESSING-STARTED | AGG-IMPORT-BATCH | SYS:processing started | — | Import worker; Adapter owner notification | tenant_id + aggregate.id |
| EVT-IMP-COMPLETED | AGG-IMPORT-BATCH | SYS:all records applied | — | Import worker; Adapter owner notification | tenant_id + aggregate.id |
| EVT-IMP-COMPLETED-WITH-QUARANTINE | AGG-IMPORT-BATCH | SYS:finished with invalid records | — | Import worker; Adapter owner notification | tenant_id + aggregate.id |
| EVT-IMP-FAILED | AGG-IMPORT-BATCH | SYS:unrecoverable error | — | Import worker; Adapter owner notification | tenant_id + aggregate.id |
| EVT-IMP-REPROCESSING | AGG-IMPORT-BATCH | CMD-IMP-REPROCESS-QUARANTINE | — | Import worker; Adapter owner notification | tenant_id + aggregate.id |
| EVT-IMP-QUARANTINE-ACCEPTED | AGG-IMPORT-BATCH | CMD-IMP-ACCEPT-QUARANTINE | — | Import worker; Adapter owner notification | tenant_id + aggregate.id |
| EVT-IMP-CANCELLED | AGG-IMPORT-BATCH | CMD-IMP-CANCEL | — | Import worker; Adapter owner notification | tenant_id + aggregate.id |
| EVT-EXT-MAPPED | AGG-EXTERNAL-ID | CMD-EXT-MAP | — | Import worker cache | tenant_id + aggregate.id |
| EVT-EXT-ENDED | AGG-EXTERNAL-ID | CMD-EXT-END | — | Import worker cache | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
