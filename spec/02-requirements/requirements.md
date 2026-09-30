---
id: REQ-BASELINE
type: requirements
title: Requirements Baseline — R1 (baselined) + R2 (W2-R2)
wave: W2
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
notes: EARS; كل متطلب له معيار قبول وطريقة تحقق. المتطلبات الفنية التفصيلية (العقود) في W6.
---

# Requirements Baseline — R1 (baselined) + R2 (W2-R2)

> EARS; كل متطلب له معيار قبول وطريقة تحقق. المتطلبات الفنية التفصيلية (العقود) في W6.

## business_requirements

_8 items_

### BRQ-001 — Unified Information

- **statement:** The organization shall have one authorized point of access to its geospatial, documentary and operational information.
- **outcomes:** OUT-01, OUT-02
- **acceptance_criteria:** ≥ 90 % of in-scope sources integrated and searchable (OUT-01)
- **verification_method:** measurement at pilot + test
- **status:** APPROVED_DELEGATED

### BRQ-002 — Contextual Understanding

- **statement:** The organization shall be able to see any situation in its place, time and relationships.
- **outcomes:** OUT-02
- **acceptance_criteria:** Situation picture build time reduced ≥ 50 % vs pilot baseline
- **verification_method:** measurement at pilot + test
- **status:** APPROVED_DELEGATED

### BRQ-003 — Decision Support

- **statement:** Decisions shall be supported by assessments and evidence and taken by the competent authority.
- **outcomes:** OUT-03, OUT-04
- **acceptance_criteria:** 100 % of decisions linked to assessment/evidence and authority
- **verification_method:** measurement at pilot + test
- **status:** APPROVED_DELEGATED

### BRQ-004 — Operational Execution

- **statement:** Decisions shall be executed through approved plans and tracked tasks.
- **outcomes:** OUT-05
- **acceptance_criteria:** 100 % of tasks linked to a plan or justified ad-hoc owner
- **verification_method:** measurement at pilot + test
- **status:** APPROVED_DELEGATED

### BRQ-005 — Institutional Learning

- **statement:** Experience from execution shall be captured and reusable.
- **outcomes:** OUT-06
- **acceptance_criteria:** ≥ 1 after-action review per closed major operation (R2 full)
- **verification_method:** measurement at pilot + test
- **status:** APPROVED_DELEGATED

### BRQ-006 — Traceability

- **statement:** Any important result shall be traceable to its sources, inputs and actors.
- **outcomes:** OUT-03, OUT-04
- **acceptance_criteria:** 100 % of T1 derived objects and decisions traceable
- **verification_method:** measurement at pilot + test
- **status:** APPROVED_DELEGATED

### BRQ-007 — Governance

- **statement:** Access, classification, retention and privacy shall be enforced by policy and auditable.
- **outcomes:** OUT-04
- **acceptance_criteria:** 0 leaks in isolation and inference suites; 100 % audit coverage
- **verification_method:** measurement at pilot + test
- **status:** APPROVED_DELEGATED

### BRQ-008 — Integration

- **statement:** External systems shall connect through explicit, versioned contracts without becoming automatic sources of truth.
- **outcomes:** OUT-01
- **acceptance_criteria:** All R1 integrations via registered adapters with lineage
- **verification_method:** measurement at pilot + test
- **status:** APPROVED_DELEGATED

## system_requirements

_181 items_

### REQ-FND-001

- **capability:** CAP-01.01
- **pattern:** ubiquitous
- **statement:** The system shall isolate each tenant's data, policies, configuration, projections, files, events and audit records from every other tenant.
- **acceptance_criteria:** No command, query, search, map, export, event subscription or AI context returns or reveals data of another tenant in the tenant-isolation test suite.
- **source:** W1 Q6; PRJ§6
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-080
- **quality:** QAS-SEC-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-002

- **capability:** CAP-01.01
- **pattern:** ubiquitous
- **statement:** The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational units of unlimited depth.
- **acceptance_criteria:** A tenant with 2 organizations and 5 unit levels can be created; every query is scoped to the caller's tenant.
- **source:** W1 Q32; PRJ§7.1
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-081
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-003

- **capability:** CAP-01.01
- **pattern:** event-driven
- **statement:** When a tenant is provisioned, the system shall create its isolation boundary, classification scheme, default roles, quotas and audit stream before any user of that tenant can sign in.
- **acceptance_criteria:** Provisioning is atomic: an injected failure at any step leaves no tenant usable by end users.
- **source:** W1 Q6; SR-07
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-080
- **quality:** QAS-SCAL-003
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-004

- **capability:** CAP-01.01
- **pattern:** optional-feature
- **statement:** Where a tenant is designated dedicated or sovereign, the system shall run that tenant in its own cell with no data store shared with other tenants.
- **acceptance_criteria:** A dedicated-cell tenant is deployed from the same release artifacts and shares no database, object store, index or event stream with other cells.
- **source:** W1 Q6; SR-09
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-080
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-005

- **capability:** CAP-01.02
- **pattern:** ubiquitous
- **statement:** The system shall authenticate human users only through a configured external identity provider using OIDC or SAML, and shall support account provisioning through SCIM.
- **acceptance_criteria:** Sign-in succeeds via OIDC and via SAML test IdPs; SCIM create/disable propagates within 5 minutes.
- **source:** W1 Q24, Q25
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-084
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-006

- **capability:** CAP-01.02
- **pattern:** ubiquitous
- **statement:** The system shall maintain Person, Identity, User and Service Account as separate records with explicit links.
- **acceptance_criteria:** A person with two identities and one user account, and a service account with no person, are represented without duplication.
- **source:** PRJ§56
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-084
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-007

- **capability:** CAP-01.03
- **pattern:** ubiquitous
- **statement:** The system shall record authority as a grant stating decision type, organizational scope, limits and validity period, held by a role or a person.
- **acceptance_criteria:** An authority grant with scope, monetary/volume limit and expiry can be created, queried and expires automatically.
- **source:** W1 Q31; PRJ§7.1
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-082
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-008

- **capability:** CAP-01.03
- **pattern:** event-driven
- **statement:** When an authority holder delegates authority, the system shall record delegator, delegate, scope, limits and validity period, and shall reject any delegation exceeding the delegator's own authority.
- **acceptance_criteria:** Delegation beyond delegator scope or limits is rejected with AUTHORITY_EXCEEDS_DELEGATOR; valid delegation is effective only within its period.
- **source:** PRJ§7.1
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-083
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-009

- **capability:** CAP-01.03
- **pattern:** ubiquitous
- **statement:** The system shall provide an authority check returning whether an actor holds authority for a given decision type, scope and point in time, including through delegation.
- **acceptance_criteria:** Authority check results match an oracle table of 50 grant/delegation/time combinations.
- **source:** W1 Q31; CR-32
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-032, UC-035
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-010

- **capability:** CAP-01.04
- **pattern:** ubiquitous
- **statement:** The system shall evaluate authorization before retrieving data for every command, query, search, map request, export, event subscription and AI retrieval.
- **acceptance_criteria:** Architecture fitness test finds no retrieval path that executes before a policy decision; penetration tests find no bypass.
- **source:** PRJ§5; BRL-008, BRL-010
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-SEC-002
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-011

- **capability:** CAP-01.04
- **pattern:** ubiquitous
- **statement:** The system shall base authorization decisions on subject, action, resource, purpose, context, classification, compartments and jurisdiction.
- **acceptance_criteria:** Policy test matrix covers each attribute; changing any single attribute changes the decision where the policy says it should.
- **source:** PRJ§66; CR-24
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-086
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-012

- **capability:** CAP-01.04
- **pattern:** ubiquitous
- **statement:** The system shall return a policy decision of ALLOW, DENY, CONDITIONAL, REDACT, AGGREGATE or REQUIRE_APPROVAL, with any obligations, and shall enforce the obligations.
- **acceptance_criteria:** Each decision type is produced by a test policy and its enforcement is observable in the response or workflow.
- **source:** PRJ§66
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-086
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-013

- **capability:** CAP-01.04
- **pattern:** unwanted-behaviour
- **statement:** If the policy decision point is unavailable or returns an error, then the system shall deny the request.
- **acceptance_criteria:** With the policy engine stopped, 100% of protected requests are denied and logged.
- **source:** V6 SL-28
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-SEC-005
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-014

- **capability:** CAP-01.04
- **pattern:** ubiquitous
- **statement:** The system shall treat View, Edit, Export, Share, Approve, Delete, Retain and Archive as separately grantable permissions.
- **acceptance_criteria:** A role granted Archive but not Delete cannot delete; each permission is independently testable.
- **source:** CR-39
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-086
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-015

- **capability:** CAP-13.02
- **pattern:** ubiquitous
- **statement:** The system shall write an audit record for every state-changing command and for every read of data classified at or above the tenant's audit threshold, containing actor, action, resource, purpose, policy decision, time and correlation id.
- **acceptance_criteria:** 100% of commands in the end-to-end suite produce exactly one audit record with all fields populated.
- **source:** BRL-015; PRJ§4
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-087
- **quality:** QAS-AUD-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-016 — The system shall keep audit records append-only and tamper-evident.

- **capability:** CAP-13.02
- **pattern:** ubiquitous
- **statement:** The system shall keep audit records append-only and tamper-evident.
- **acceptance_criteria:** Modifying or deleting any audit record in storage is detected by the integrity verification job.
- **source:** PRJ§3.4
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-087
- **quality:** QAS-SEC-006
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-017

- **capability:** CAP-13.01
- **pattern:** event-driven
- **statement:** When a security exception is requested, the system shall require approval by two distinct authorized persons and shall revoke the exception automatically at its expiry.
- **acceptance_criteria:** Approval by one person, or by the requester, does not activate the exception; the exception stops applying at expiry.
- **source:** W1 Q19
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-088
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-FND-018

- **capability:** CAP-14.03
- **pattern:** ubiquitous
- **statement:** The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs.
- **acceptance_criteria:** A tenant exceeding its request quota receives RATE_LIMITED while other tenants' latency stays within QAS-PERF-001.
- **source:** SR-07
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-105
- **quality:** QAS-SCAL-005
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-GOV-001

- **capability:** CAP-13.01
- **pattern:** ubiquitous
- **statement:** The system shall support a per-tenant classification scheme with ordered levels, an unlimited number of compartments and release caveats.
- **acceptance_criteria:** A scheme with 5 levels, 20 compartments and 3 caveats can be configured and enforced.
- **source:** W1 Q16
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-085
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-GOV-002 — The system shall require a classification on every object of importance tier T1 or T2.

- **capability:** CAP-13.01
- **pattern:** ubiquitous
- **statement:** The system shall require a classification on every object of importance tier T1 or T2.
- **acceptance_criteria:** Creating a T1/T2 object without classification is rejected with CLASSIFICATION_REQUIRED.
- **source:** W1 Q12, Q16
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-GOV-003

- **capability:** CAP-13.01
- **pattern:** ubiquitous
- **statement:** The system shall permit read access to an object only if the subject's clearance is at least the object's level and the subject holds every compartment of the object.
- **acceptance_criteria:** Access matrix of 5 levels × compartment combinations matches the oracle with 0 deviations.
- **source:** W1 Q16
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-089 (added by correction CR-64 — see corrections.md)
- **quality:** QAS-SEC-002
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-GOV-004

- **capability:** CAP-13.01
- **pattern:** event-driven
- **statement:** When the classification of an object is changed, the system shall require the authority defined by tenant policy, record the change as a new version, and stop returning the object to newly unauthorized subjects from the moment of the change in all access paths including projections.
- **acceptance_criteria:** After a downgrade of a user's access, the next search, map, export and API call does not return the object, regardless of index lag.
- **source:** W1 Q16; ADR-P06
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-085 (scheme/object side), UC-089 (user clearance side — added by correction CR-64)
- **quality:** QAS-SEC-003
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-GOV-005

- **capability:** CAP-13.04
- **pattern:** ubiquitous
- **statement:** The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data outside it unless a tenant policy explicitly permits the transfer.
- **acceptance_criteria:** Egress monitoring during the full test suite shows no data leaving the configured jurisdiction boundary.
- **source:** W1 Q17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-GOV-006 — The system shall apply a retention schedule to every record class.

- **capability:** CAP-11.02
- **pattern:** ubiquitous
- **statement:** The system shall apply a retention schedule to every record class.
- **acceptance_criteria:** Every record class in the reference data has a retention rule; records past retention are flagged for disposition.
- **source:** W1 Q18
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-103
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-GOV-007

- **capability:** CAP-11.02
- **pattern:** event-driven
- **statement:** When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modification until the hold is released.
- **acceptance_criteria:** Disposition and erasure jobs skip held records; attempts are logged.
- **source:** W1 Q18
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-103
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-GOV-008

- **capability:** CAP-13.03
- **pattern:** event-driven
- **statement:** When the personal data of a data subject must be erased, the system shall make it unrecoverable in operational stores, projections, backups and archives while retaining non-personal audit facts.
- **acceptance_criteria:** After erasure, the subject's personal data cannot be recovered from any store or restored backup; audit facts remain.
- **source:** W1 Q18; ADR-P08
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-103
- **quality:** QAS-PRV-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-GOV-009

- **capability:** CAP-13.01
- **pattern:** ubiquitous
- **statement:** The system shall version, audit and time-stamp every policy and configuration change and apply each change from its effective time.
- **acceptance_criteria:** A policy with a future effective time does not apply before it and applies after it; history is queryable.
- **source:** V5§81
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-086
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-001

- **capability:** CAP-02.02
- **pattern:** ubiquitous
- **statement:** The system shall register each source with type, owner, classification and a reliability rating, and keep the history of reliability changes.
- **acceptance_criteria:** Changing a source's reliability creates a new version; previous ratings remain queryable by time.
- **source:** PRJ§7.5
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-004, UC-095
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-002

- **capability:** CAP-02.03
- **pattern:** event-driven
- **statement:** When an observation is recorded, the system shall store its observation time, its event time where known, its record time, its location with CRS and positional accuracy, its source, its observer and its attachments.
- **acceptance_criteria:** Recorded observations contain all listed fields; record time is assigned by the server, not the client.
- **source:** PRJ§3.5, §22; V6 SL-11, SL-12
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-005
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-003

- **capability:** CAP-02.03
- **pattern:** ubiquitous
- **statement:** The system shall store attachments (documents, images, video, raster) in object storage and reference them by content hash.
- **acceptance_criteria:** No attachment larger than 1 MB is stored in the operational database; references resolve by hash.
- **source:** SR-05
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-005, UC-006
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-004

- **capability:** CAP-02.03
- **pattern:** event-driven
- **statement:** When an attachment is stored or retrieved, the system shall compute or verify its content hash.
- **acceptance_criteria:** A corrupted stored object is detected at retrieval and reported as INTEGRITY_ERROR.
- **source:** PRJ§3.6
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-006
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-005

- **capability:** CAP-02.04
- **pattern:** ubiquitous
- **statement:** The system shall ingest external data only through registered adapters or bulk import jobs that record source, batch, transformation and lineage.
- **acceptance_criteria:** Every ingested record has a lineage record pointing to adapter, batch and transformation version.
- **source:** W1 Q14, Q24
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-094
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-006

- **capability:** CAP-02.04
- **pattern:** unwanted-behaviour
- **statement:** If an ingested record fails validation, then the system shall quarantine it with the failure reason and shall not publish it.
- **acceptance_criteria:** Invalid records appear in quarantine with reason codes and never in queries or projections.
- **source:** V5§43
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-094
- **quality:** QAS-DQ-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-007 — When an ingestion batch is re-submitted, the system shall not create duplicate records.

- **capability:** CAP-02.04
- **pattern:** event-driven
- **statement:** When an ingestion batch is re-submitted, the system shall not create duplicate records.
- **acceptance_criteria:** Submitting the same batch twice yields the same record count as once.
- **source:** PRJ§16 idempotency
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-094
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-008

- **capability:** CAP-02.04
- **pattern:** ubiquitous
- **statement:** The system shall import geospatial data via OGC API Features/Maps/Tiles, WMS/WFS, GeoJSON, GeoPackage, GeoTIFF/COG and KML.
- **acceptance_criteria:** A reference dataset in each format imports with geometry and attributes preserved.
- **source:** W1 Q25
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-094
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-009

- **capability:** CAP-02.04
- **pattern:** ubiquitous
- **statement:** The system shall ingest weather data through an adapter and register the provider as a source.
- **acceptance_criteria:** Weather records carry source and observation time and appear as a map layer.
- **source:** W1 Q24
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-094
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-020

- **capability:** CAP-03.01
- **pattern:** ubiquitous
- **statement:** The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct object types.
- **acceptance_criteria:** Each type has its own identity, lifecycle and schema in the contracts.
- **source:** PRJ§57
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-001, UC-002, UC-003
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-021

- **capability:** CAP-03.02
- **pattern:** ubiquitous
- **statement:** The system shall represent each attribute value of an importance-tier T1 object as a claim linked to its sources, evidence and confidence.
- **acceptance_criteria:** Every T1 attribute value in the test corpus resolves to at least one claim with source and confidence.
- **source:** W1 Q12; ADR-P03; BRL-001
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-006
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-022

- **capability:** CAP-03.04
- **pattern:** ubiquitous
- **statement:** The system shall record a valid-time interval and a record-time interval for every T1 claim.
- **acceptance_criteria:** Each T1 claim has valid_from/valid_to and recorded_from/recorded_to; open intervals are explicit.
- **source:** W1 Q13; ADR-P01
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-023

- **capability:** CAP-03.04
- **pattern:** event-driven
- **statement:** When a query specifies a valid time T, a record time K, or both, the system shall return the state valid at T as known at K, using the current time for any time not specified.
- **acceptance_criteria:** Results on the temporal test corpus match the oracle for all (T, K) pairs.
- **source:** W1 Q13
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-096
- **quality:** QAS-TMP-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-024

- **capability:** CAP-03.02
- **pattern:** ubiquitous
- **statement:** The system shall never overwrite a T1 claim; a correction shall close the record-time interval of the previous claim and create a new claim.
- **acceptance_criteria:** After a correction, the old claim remains retrievable as known before the correction time.
- **source:** BRL-002; PRJ§3.4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-025

- **capability:** CAP-03.06
- **pattern:** event-driven
- **statement:** When two claims about the same subject and attribute overlap in valid time with incompatible values, the system shall open a conflict case and retain both claims.
- **acceptance_criteria:** Conflicting claims create exactly one open conflict case; no claim is removed.
- **source:** PRJ§24; BRL-002
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-008
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-026

- **capability:** CAP-03.07
- **pattern:** ubiquitous
- **statement:** The system shall expose confidence as separate dimensions: source reliability, information confidence, data quality, verification status, freshness, completeness and uncertainty.
- **acceptance_criteria:** APIs return all seven dimensions; no single mandatory aggregate score exists.
- **source:** PRJ§3.8; V5§55; CR-03
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-027

- **capability:** CAP-03.01
- **pattern:** ubiquitous
- **statement:** The system shall represent relationships as objects with type, source, target, validity period, evidence, provenance, confidence and classification.
- **acceptance_criteria:** A relationship can be classified higher than its endpoints and is hidden accordingly.
- **source:** PRJ§3.3
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-003
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-028

- **capability:** CAP-03.03
- **pattern:** ubiquitous
- **statement:** The system shall require every geometry to carry a CRS and a positional accuracy, and shall reject invalid geometries.
- **acceptance_criteria:** Geometries without CRS, without accuracy, or failing validity checks are rejected with GEOMETRY_INVALID.
- **source:** V6 SL-12
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-DQ-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-029

- **capability:** CAP-03.03
- **pattern:** ubiquitous
- **statement:** The system shall store each geometry in the canonical CRS WGS 84 (EPSG:4326) and shall keep the original CRS and coordinates.
- **acceptance_criteria:** Round-trip transformation of the reference set returns original coordinates within the stated accuracy.
- **source:** W2 delegated decision (ADR-P16)
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-030 — The system shall keep the position history of located entities over time.

- **capability:** CAP-03.03
- **pattern:** ubiquitous
- **statement:** The system shall keep the position history of located entities over time.
- **acceptance_criteria:** The location of an entity at any past valid time is retrievable.
- **source:** V5§53
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-096
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-031

- **capability:** CAP-03.01
- **pattern:** ubiquitous
- **statement:** The system shall store names in their original form and in normalized and transliterated forms for Arabic and English.
- **acceptance_criteria:** Each name has original, normalized and at least one transliterated form; the original is never modified.
- **source:** W1 Q15; ADR-P15
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-USA-002
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-032

- **capability:** CAP-03.05
- **pattern:** event-driven
- **statement:** When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, method, features, score and evidence, and shall not merge entities without a recorded decision.
- **acceptance_criteria:** No merge occurs in the test corpus without a decision record naming the reviewer.
- **source:** PRJ§13
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-007
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-033

- **capability:** CAP-03.05
- **pattern:** event-driven
- **statement:** When entities are matched, the system shall record a same-as link with the decision, reviewer and time, keep all original identifiers valid, and resolve any member identifier to the identity cluster's canonical identifier while reporting the requested identifier.
- **acceptance_criteria:** Requests by any member URN return the resolved entity with canonical_urn and requested_urn; no identifier is rewritten or deleted.
- **source:** PRJ§13; ADR-P13
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-007
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED
- **change_log:** W3: aligned with ER-MODEL (merge = link, no id rewrite)

### REQ-INF-034

- **capability:** CAP-03.05
- **pattern:** event-driven
- **statement:** When a match is reversed, the system shall close the same-as link so that each original entity again resolves to exactly its own claims.
- **acceptance_criteria:** After split, each original entity resolves to exactly the claims whose subject_ref is its own URN; the link remains queryable as known before the split.
- **source:** CR-15
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-104
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED
- **change_log:** W3: aligned with ER-MODEL (split = close link)

### REQ-INF-035

- **capability:** CAP-03.07
- **pattern:** ubiquitous
- **statement:** The system shall record lineage for every derived object: inputs and their versions, the transformation and its version, the actor and the execution time.
- **acceptance_criteria:** 100% of derived objects in the end-to-end suite have a complete lineage record.
- **source:** PRJ§23
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-TRC-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-036

- **capability:** CAP-03.01
- **pattern:** ubiquitous
- **statement:** The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type>:<id>, and shall map external identifiers per source system.
- **acceptance_criteria:** Every object exposes both identifiers; an external identifier maps to exactly one object per system at a given time.
- **source:** ADR-P13; PRJ§12
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-INF-037 — If a T1 object is submitted without a source reference, then the system shall reject it.

- **capability:** CAP-03.07
- **pattern:** unwanted-behaviour
- **statement:** If a T1 object is submitted without a source reference, then the system shall reject it.
- **acceptance_criteria:** Creation without source is rejected with SOURCE_REQUIRED.
- **source:** BRL-001
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-ANL-001

- **capability:** CAP-04.01
- **pattern:** ubiquitous
- **statement:** The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumptions and evidence references.
- **acceptance_criteria:** An analysis case cannot move beyond DRAFT without a question and scope.
- **source:** PRJ§58
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-010, UC-011, UC-012
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-ANL-002

- **capability:** CAP-04.02
- **pattern:** event-driven
- **statement:** When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and version, layers, filters, time and spatial extent, assumptions, steps, results, analyst and execution time.
- **acceptance_criteria:** Every run record contains all listed fields.
- **source:** PRJ§3.7
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-013
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-ANL-003

- **capability:** CAP-04.02
- **pattern:** event-driven
- **statement:** When a recorded analysis run is re-executed with the same recorded inputs, the system shall produce the same results or report which inputs differ.
- **acceptance_criteria:** Re-execution of 100% of deterministic runs in the test set yields identical results.
- **source:** PRJ§3.7; OUT-03
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-013
- **quality:** QAS-TRC-002
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-ANL-004

- **capability:** CAP-04.02
- **pattern:** ubiquitous
- **statement:** The system shall execute long-running analysis runs as asynchronous jobs with status, progress, cancellation and retry.
- **acceptance_criteria:** A run exceeding 10 seconds returns a job reference immediately; status is pollable and subscribable.
- **source:** PRJ§72; SR-06
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-013
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-ANL-005

- **capability:** CAP-04.03
- **pattern:** ubiquitous
- **statement:** The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, methodology, limitations, reviewer and version.
- **acceptance_criteria:** An assessment cannot be published with any of these fields missing.
- **source:** PRJ§59
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-015, UC-014
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-ANL-006

- **capability:** CAP-04.03
- **pattern:** event-driven
- **statement:** When an assessment is published, the system shall make that version immutable; later changes shall create a new version.
- **acceptance_criteria:** Edit attempts on a published version are rejected; a new version links to its predecessor.
- **source:** PRJ§59
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-015
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-ANL-007 — The system shall allow comparison of alternative scenarios within an analysis case.

- **capability:** CAP-04.01
- **pattern:** ubiquitous
- **statement:** The system shall allow comparison of alternative scenarios within an analysis case.
- **acceptance_criteria:** Two scenarios with different assumptions display side by side with their differing inputs and results.
- **source:** PRJ§46 UC-016
- **priority:** should
- **verification_method:** test
- **use_cases:** UC-016
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-ANL-008

- **capability:** CAP-04.03
- **pattern:** unwanted-behaviour
- **statement:** If an assessment references evidence the reader is not authorized to view, then the system shall withhold that evidence according to policy and shall indicate the omission only where the policy permits.
- **acceptance_criteria:** Readers without access never receive the evidence content or identifiers; omission markers follow the policy setting.
- **source:** BRL-010; A21
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-SEC-002
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SIT-001

- **capability:** CAP-05.01
- **pattern:** ubiquitous
- **statement:** The system shall define each situation by geographic extent, time window, inclusion criteria, owner and classification.
- **acceptance_criteria:** A situation cannot be activated without extent, window and criteria.
- **source:** ADR-P07; PRJ§60
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-020
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SIT-002

- **capability:** CAP-05.02
- **pattern:** event-driven
- **statement:** When an object matching a situation's criteria is created or changed, the system shall update the situation membership and record a situation change.
- **acceptance_criteria:** Membership changes appear in the situation change log with cause and time.
- **source:** PRJ§60
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-021, UC-022
- **quality:** QAS-PERF-006
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SIT-003

- **capability:** CAP-05.03
- **pattern:** ubiquitous
- **statement:** The system shall present each situation as a map-based common operational picture of its entities, events, risks, tasks, resources, assessments and alerts.
- **acceptance_criteria:** All member types render on the map and in lists, filtered by the viewer's authorization.
- **source:** PRJ§60
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-024, UC-098
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SIT-004

- **capability:** CAP-05.02
- **pattern:** event-driven
- **statement:** When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users.
- **acceptance_criteria:** Alert raised and delivered within QAS-PERF-005 under design load.
- **source:** PRJ§7.9
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-023
- **quality:** QAS-PERF-005
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SIT-005

- **capability:** CAP-05.02
- **pattern:** ubiquitous
- **statement:** The system shall manage alerts through the states RAISED, ACKNOWLEDGED, RESOLVED and DISMISSED, requiring a reason for dismissal, and shall audit every transition.
- **acceptance_criteria:** Dismissal without reason is rejected; every transition has an audit record.
- **source:** PRJ§7.9
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-023
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SIT-006

- **capability:** CAP-05.02
- **pattern:** unwanted-behaviour
- **statement:** If a user is not authorized for the object that triggered an alert, then the system shall not reveal that object or its existence in the alert shown to that user.
- **acceptance_criteria:** Alert payloads received by unauthorized subscribers contain no identifier, location or attribute of the object.
- **source:** BRL-010; A21
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-SEC-002
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SIT-007

- **capability:** CAP-05.03
- **pattern:** ubiquitous
- **statement:** The system shall serve map layers filtered by the requesting user's authorization and shall not share cached map tiles across different authorization scopes.
- **acceptance_criteria:** Two users with different compartments requesting the same tile receive different content; cache keys include the authorization scope.
- **source:** ADR-P06; ADR-P12
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-098
- **quality:** QAS-SEC-004, QAS-PERF-007
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-DEC-001

- **capability:** CAP-06.01
- **pattern:** ubiquitous
- **statement:** The system shall record each decision request with its question, options, assessment references, deadline and required authority type.
- **acceptance_criteria:** A decision request without options or required authority type cannot be submitted.
- **source:** PRJ§61
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-030, UC-031
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-DEC-002

- **capability:** CAP-06.02
- **pattern:** event-driven
- **statement:** When a decision is recorded, the system shall verify through the authority check that the decider holds the required authority at the decision time, and shall reject the decision otherwise.
- **acceptance_criteria:** Decisions by actors without valid authority are rejected with AUTHORITY_REQUIRED.
- **source:** BRL-003; REQ-FND-009
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-032
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-DEC-003

- **capability:** CAP-06.02
- **pattern:** ubiquitous
- **statement:** The system shall record for each decision the selected option, rationale, authority, approval, effective time and links to the assessments and evidence considered.
- **acceptance_criteria:** 100% of recorded decisions link to at least one assessment or evidence object.
- **source:** PRJ§61; OUT-04
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-032
- **quality:** QAS-TRC-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-DEC-004

- **capability:** CAP-06.02
- **pattern:** ubiquitous
- **statement:** The system shall make a recorded decision immutable; a change shall be recorded as a new decision that supersedes it.
- **acceptance_criteria:** Edit attempts are rejected; supersession links are navigable both ways.
- **source:** PRJ§3.4
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-032
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-001

- **capability:** CAP-07.01
- **pattern:** ubiquitous
- **statement:** The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities, milestones, resources, schedule, dependencies and metrics.
- **acceptance_criteria:** Plan schema contains all listed parts; a plan cannot be submitted without objectives and outcomes.
- **source:** PRJ§62
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-033
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-002 — The system shall link every approved plan to the decisions or objectives it implements.

- **capability:** CAP-07.01
- **pattern:** ubiquitous
- **statement:** The system shall link every approved plan to the decisions or objectives it implements.
- **acceptance_criteria:** Approval of a plan without such a link is rejected.
- **source:** OUT-05
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-033, UC-035
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-003

- **capability:** CAP-07.02
- **pattern:** event-driven
- **statement:** When a plan is approved, the system shall create an immutable baseline of that plan version.
- **acceptance_criteria:** Baseline content cannot be modified; it remains retrievable after later versions.
- **source:** BRL-004
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-035, UC-036
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-004

- **capability:** CAP-07.02
- **pattern:** event-driven
- **statement:** When a major change is made to a baselined plan, the system shall create a new plan version that requires approval before it becomes effective.
- **acceptance_criteria:** Major changes (as defined in BRL-005) create a new version; minor changes do not.
- **source:** BRL-005
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-034, UC-036
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-005

- **capability:** CAP-07.02
- **pattern:** unwanted-behaviour
- **statement:** If the approver of a plan is also its author, then the system shall reject the approval unless tenant policy explicitly permits it.
- **acceptance_criteria:** Self-approval rejected with SEGREGATION_OF_DUTIES under default policy.
- **source:** W1 Q8
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-035
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-006

- **capability:** CAP-07.03
- **pattern:** ubiquitous
- **statement:** The system shall manage task state according to state machine SM-TASK and reject any transition not defined in it.
- **acceptance_criteria:** Every state × command pair not in SM-TASK is rejected with TASK_INVALID_STATE_TRANSITION.
- **source:** PRJ§55; V6§13.5
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-040, UC-042, UC-043, UC-044, UC-045
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-007

- **capability:** CAP-07.03
- **pattern:** event-driven
- **statement:** When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares required competencies, qualifications or authorizations.
- **acceptance_criteria:** Assignment to a NOT_ELIGIBLE person is rejected; CONDITIONALLY_ELIGIBLE requires the stated condition.
- **source:** BRL-007
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-041, UC-102
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-008

- **capability:** CAP-07.03
- **pattern:** unwanted-behaviour
- **statement:** If a task's completion criteria are not all met, then the system shall reject its completion.
- **acceptance_criteria:** Completion with any unmet criterion is rejected with TASK_CRITERIA_NOT_MET.
- **source:** BRL-006
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-045
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-009

- **capability:** CAP-07.03
- **pattern:** unwanted-behaviour
- **statement:** If the approver of a task result is also its assignee, then the system shall reject the approval unless tenant policy explicitly permits it.
- **acceptance_criteria:** Self-approval rejected with SEGREGATION_OF_DUTIES under default policy.
- **source:** W1 Q8; OQ-030
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-044
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-010

- **capability:** CAP-07.03
- **pattern:** ubiquitous
- **statement:** The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reason.
- **acceptance_criteria:** No task exists without either a plan link or an ad-hoc reason and owner.
- **source:** OUT-05
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-040
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-011

- **capability:** CAP-07.03
- **pattern:** ubiquitous
- **statement:** The system shall require an idempotency key and the expected version on every state-changing command, and shall reject commands whose expected version is stale.
- **acceptance_criteria:** Duplicate command returns the original result; stale version returns VERSION_CONFLICT with no state change.
- **source:** PRJ§16, §104
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-REL-003
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-012

- **capability:** CAP-07.03
- **pattern:** event-driven
- **statement:** When a task is escalated, the system shall notify the next authority level and keep the task state unchanged.
- **acceptance_criteria:** Escalation produces a TaskEscalated event and a notification; state is unchanged.
- **source:** PRJ§55
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-046
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-013 — The system shall record measurements of plan outcomes over time against their targets.

- **capability:** CAP-07.05
- **pattern:** ubiquitous
- **statement:** The system shall record measurements of plan outcomes over time against their targets.
- **acceptance_criteria:** Outcome measurements are time-series linked to the plan outcome and its metric.
- **source:** PRJ§62; OUT-05
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-101
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OPS-014

- **capability:** CAP-07.04
- **pattern:** ubiquitous
- **statement:** The system shall allow each tenant to configure review and approval steps for plans and tasks within the limits of the state machines.
- **acceptance_criteria:** A tenant can add a second review step without changing code; configurations are versioned.
- **source:** PRJ§7.13
- **priority:** should
- **verification_method:** test
- **use_cases:** UC-034, UC-044
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-RDY-001

- **capability:** CAP-08.04
- **pattern:** ubiquitous
- **statement:** The system shall record each person's competencies, qualifications and certifications with their validity periods.
- **acceptance_criteria:** Expired certifications are reported as expired at any query time after expiry.
- **source:** PRJ§64
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-102
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-RDY-002

- **capability:** CAP-08.04
- **pattern:** event-driven
- **statement:** When eligibility is checked for a person, role or task at a given time, the system shall return ELIGIBLE, CONDITIONALLY_ELIGIBLE, NOT_ELIGIBLE, EXPIRED, REQUIRES_SUPERVISION, REQUIRES_TRAINING, REQUIRES_CERTIFICATION or UNKNOWN, with reasons.
- **acceptance_criteria:** Eligibility results match an oracle table of 40 cases.
- **source:** PRJ§64
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-102
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-COM-001

- **capability:** CAP-10.01
- **pattern:** event-driven
- **statement:** When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authorized recipients according to their preferences.
- **acceptance_criteria:** Recipients receive in-app notification; mobile push is delivered when the device is reachable.
- **source:** PRJ§7.11
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-099
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-COM-002

- **capability:** CAP-10.01
- **pattern:** ubiquitous
- **statement:** The system shall not include classified content in mobile push payloads and shall limit notification content to the recipient's authorization.
- **acceptance_criteria:** Push payloads contain only a reference and a non-sensitive title; content is fetched after authorization.
- **source:** A21
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-099
- **quality:** QAS-SEC-002
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OFF-001

- **capability:** CAP-02.03
- **pattern:** optional-feature
- **statement:** Where the mobile field application is used, the system shall allow recording observations with location, time and photos, and updating the status of assigned tasks, without connectivity for at least 72 hours.
- **acceptance_criteria:** A device offline for 72 hours records 500 observations and 100 task updates and synchronizes them all.
- **source:** W1 Q9
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-090
- **quality:** QAS-OFF-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OFF-002

- **capability:** CAP-02.03
- **pattern:** ubiquitous
- **statement:** The system shall let field users preload authorized area-of-interest data, which shall respect the user's authorization at download time and expire according to tenant policy.
- **acceptance_criteria:** Preloaded data excludes unauthorized objects; expired data becomes unreadable on the device.
- **source:** W1 Q9
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-090
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OFF-003

- **capability:** CAP-02.03
- **pattern:** event-driven
- **statement:** When a device reconnects, the system shall receive the device's recorded commands in their original order with device times, and shall assign record time on receipt.
- **acceptance_criteria:** Device time is stored as observation time; record time equals server receipt time.
- **source:** ADR-P09; ADR-P01
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-091
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OFF-004

- **capability:** CAP-02.03
- **pattern:** unwanted-behaviour
- **statement:** If a synchronized command conflicts with the current server state, then the system shall route it to conflict review and shall not apply last-write-wins to T1 or T2 data.
- **acceptance_criteria:** 0 silent overwrites in the concurrent-edit sync test; all conflicts appear for review.
- **source:** PRJ§110; ADR-P09
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-092
- **quality:** QAS-OFF-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OFF-005

- **capability:** CAP-02.03
- **pattern:** ubiquitous
- **statement:** The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device.
- **acceptance_criteria:** Device data is unreadable without user authentication; remote wipe completes on next connection.
- **source:** W1 Q9
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-093
- **quality:** QAS-SEC-007
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-OFF-006

- **capability:** CAP-02.03
- **pattern:** event-driven
- **statement:** When a synchronization is interrupted, the system shall resume it without duplicating commands.
- **acceptance_criteria:** Interrupting sync at random points 100 times produces no duplicates.
- **source:** Idempotency
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-091
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SRC-001

- **capability:** CAP-03.01
- **pattern:** ubiquitous
- **statement:** The system shall provide unified search across entities, observations, documents, assessments, plans and tasks, with text, spatial and temporal filters.
- **acceptance_criteria:** A single query can combine text, a polygon and a time window across all listed types.
- **source:** PRJ§21
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-097
- **quality:** QAS-PERF-003
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SRC-002

- **capability:** CAP-03.01
- **pattern:** ubiquitous
- **statement:** The system shall not reveal the existence of unauthorized objects through search results, counts, facets, suggestions, ordering, errors or response timing.
- **acceptance_criteria:** Inference test suite detects 0 leakage.
- **source:** BRL-010; A21
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-097
- **quality:** QAS-SEC-002
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SRC-003

- **capability:** CAP-03.01
- **pattern:** ubiquitous
- **statement:** The system shall match Arabic text regardless of hamza forms, alef maqsura, taa marbuta, diacritics and tatweel, and shall match names across Arabic and Latin transliterations.
- **acceptance_criteria:** Arabic search test set reaches the recall target in QAS-USA-002.
- **source:** W1 Q15; ADR-P15
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-097
- **quality:** QAS-USA-002
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-SRC-004

- **capability:** CAP-03.01
- **pattern:** ubiquitous
- **statement:** The system shall be able to rebuild every search and graph projection from the source of truth without data loss.
- **acceptance_criteria:** Dropping and rebuilding the index yields identical query results on the reference set.
- **source:** PRJ§21; V5 A07
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-REL-002
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-001

- **capability:** CAP-14.02
- **pattern:** ubiquitous
- **statement:** The system shall install, upgrade and operate in an air-gapped environment with no dependency on external network services.
- **acceptance_criteria:** Full install and upgrade succeed from an offline bundle in an isolated network.
- **source:** W1 Q20
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-OPS-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-002

- **capability:** CAP-14.03
- **pattern:** ubiquitous
- **statement:** The system shall use the same release artifacts for shared, dedicated and sovereign deployments.
- **acceptance_criteria:** The three deployment modes pass the same acceptance suite from one release.
- **source:** W1 Q6
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-003

- **capability:** CAP-14.01
- **pattern:** ubiquitous
- **statement:** The system shall emit metrics, logs and traces carrying a correlation id across every component, plus business telemetry for the outcome measures.
- **acceptance_criteria:** Any request can be traced end to end by its correlation id.
- **source:** PRJ§26; V5§39
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-OBS-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-004

- **capability:** CAP-14.02
- **pattern:** ubiquitous
- **statement:** The system shall assign every capability to one of the service tiers defined in QAS-AVL-001..003 (critical, important, standard) and meet that tier's availability, RPO and RTO.
- **acceptance_criteria:** Tier assignment exists for 100% of R1 capabilities; DR drills meet tier targets.
- **source:** W1 Q21
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-AVL-001, QAS-AVL-002, QAS-AVL-003, QAS-REC-001, QAS-REC-002, QAS-REC-003
- **release:** R1
- **status:** APPROVED_DELEGATED
- **note:** 'important' here is the defined name of a service tier (W1 Q21), not an ambiguous qualifier.

### REQ-PLT-005

- **capability:** CAP-14.02
- **pattern:** ubiquitous
- **statement:** The system shall run heavy operations (raster processing, bulk import, analysis runs, reconstruction, report generation) as asynchronous jobs with status, retry and cancellation.
- **acceptance_criteria:** No synchronous API call performs a listed heavy operation.
- **source:** SR-06; PRJ§72
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-006

- **capability:** CAP-14.02
- **pattern:** ubiquitous
- **statement:** The system shall publish domain events through a transactional outbox and shall process received events idempotently through an inbox.
- **acceptance_criteria:** State change and event are committed atomically; duplicated deliveries have no second effect.
- **source:** PRJ§33–34
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-REL-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-007

- **capability:** CAP-14.02
- **pattern:** ubiquitous
- **statement:** The system shall version every API and event contract and shall introduce breaking changes only as a new major version that coexists with the previous one.
- **acceptance_criteria:** Contract tests fail the build on any unversioned breaking change.
- **source:** PRJ§20, §97
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-EVO-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-008 — The system shall use cursor-based pagination for every list API.

- **capability:** CAP-14.02
- **pattern:** ubiquitous
- **statement:** The system shall use cursor-based pagination for every list API.
- **acceptance_criteria:** No list endpoint accepts offset pagination.
- **source:** SR-12
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-009

- **capability:** CAP-14.02
- **pattern:** ubiquitous
- **statement:** The system shall return errors in the standard error model with code, message, details, correlation id, retryable flag and policy reason where applicable.
- **acceptance_criteria:** All error responses in the API suite conform to the schema.
- **source:** PRJ§19
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-010

- **capability:** CAP-14.01
- **pattern:** ubiquitous
- **statement:** The system shall provide its user interfaces in Arabic and English with right-to-left and left-to-right layouts, and optional Hijri date display.
- **acceptance_criteria:** All R1 screens pass bilingual and RTL review.
- **source:** W1 Q15
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-ACC-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-011 — The system shall provide a responsive web application and a mobile field application.

- **capability:** CAP-14.01
- **pattern:** ubiquitous
- **statement:** The system shall provide a responsive web application and a mobile field application.
- **acceptance_criteria:** R1 web screens work from 360 px to desktop width; field functions run on the mobile app.
- **source:** W1 Q10
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-012

- **capability:** CAP-14.02
- **pattern:** ubiquitous
- **statement:** The system shall back up all stores according to their service tier and shall verify restores automatically.
- **acceptance_criteria:** Scheduled restore tests succeed and meet the tier RTO.
- **source:** PRJ§114
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-REC-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-PLT-013 — The system shall compute resource consumption and cost per tenant from telemetry.

- **capability:** CAP-14.03
- **pattern:** ubiquitous
- **statement:** The system shall compute resource consumption and cost per tenant from telemetry.
- **acceptance_criteria:** A monthly per-tenant cost report is produced from telemetry alone.
- **source:** W1 Q29
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-COST-001
- **release:** R1
- **status:** APPROVED_DELEGATED

### REQ-RES-001

- **capability:** CAP-08.01
- **pattern:** ubiquitous
- **statement:** The system shall register each asset with type, ownership, custody holder, status, condition, location, capabilities, certifications and maintenance schedule.
- **acceptance_criteria:** An asset can be registered with all listed attributes; status and condition are versioned.
- **source:** PRJ§63 Asset; DOM-14
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-050
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-002

- **capability:** CAP-08.01
- **pattern:** event-driven
- **statement:** When custody of an asset is transferred, the system shall record the previous holder, the new holder, the time and the authorization, keeping a gapless custody chain.
- **acceptance_criteria:** Custody history is complete; a transfer by a non-holder without authority is rejected.
- **source:** DOM-14 Custody
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-053
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-003

- **capability:** CAP-08.01
- **pattern:** event-driven
- **statement:** When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavailable for new assignments from that moment.
- **acceptance_criteria:** Assignment of an expired or unserviceable asset is rejected with the reason.
- **source:** PRJ§63 Certification/Condition; BRL-007
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-051, UC-053
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-004

- **capability:** CAP-08.01
- **pattern:** ubiquitous
- **statement:** The system shall schedule and record maintenance for assets, and shall mark an asset under maintenance as unavailable for the maintenance window.
- **acceptance_criteria:** Availability queries exclude maintenance windows.
- **source:** DOM-14 Maintenance
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-051
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-005

- **capability:** CAP-08.01
- **pattern:** ubiquitous
- **statement:** The system shall keep asset location as bitemporal claims so that the location of an asset at any past time is retrievable.
- **acceptance_criteria:** Asset position history is available through the claims kernel.
- **source:** ADR-P01; REQ-INF-030
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-050
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-006

- **capability:** CAP-08.02
- **pattern:** ubiquitous
- **statement:** The system shall manage resource pools with type, quantity, unit, capacity and availability over time.
- **acceptance_criteria:** A pool's available quantity at time t equals capacity minus commitments valid at t.
- **source:** PRJ§63 Resource; DOM-15
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-054
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-007

- **capability:** CAP-08.02
- **pattern:** event-driven
- **statement:** When a resource allocation is requested, the system shall verify authorization, type, availability, capacity, time window, geography, priority, existing commitments and policy before committing it.
- **acceptance_criteria:** Each failing check returns its own reason code; a successful allocation creates a commitment.
- **source:** PRJ§63 Allocation Domain Service
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-054
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-008

- **capability:** CAP-08.02
- **pattern:** unwanted-behaviour
- **statement:** If two allocation requests compete for the same capacity, then the system shall commit at most the available capacity and shall resolve the contention by priority, then by request time.
- **acceptance_criteria:** No over-commitment under concurrent requests; losers receive CAPACITY_UNAVAILABLE with the competing priority.
- **source:** DOM-15 Capacity
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-054
- **quality:** QAS-RES-001
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-009

- **capability:** CAP-08.02
- **pattern:** event-driven
- **statement:** When a higher-priority allocation needs capacity already committed at lower priority, the system shall require an authorized pre-emption decision and notify the affected owners.
- **acceptance_criteria:** Pre-emption without authority is rejected; affected tasks are notified.
- **source:** DOM-15 Priority; BRL-003
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-054
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-010

- **capability:** CAP-08.02
- **pattern:** ubiquitous
- **statement:** The system shall record resource consumption against allocations with quantity, unit and time.
- **acceptance_criteria:** Consumption above the allocation is flagged for review.
- **source:** DOM-15 Consumption
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-055
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-011

- **capability:** CAP-08.02
- **pattern:** event-driven
- **statement:** When a task linked to an allocation reaches a terminal state, the system shall release the unused allocation.
- **acceptance_criteria:** Released quantity becomes available immediately.
- **source:** SLC-03 events; DEBT-001
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-054
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-012

- **capability:** CAP-08.02
- **pattern:** ubiquitous
- **statement:** The system shall link resources and assets to tasks as structured references, replacing the text-only resource notes of R1.
- **acceptance_criteria:** R1 resource notes are migrated to references or kept as notes with a migration report.
- **source:** DEBT-001
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-053, UC-054
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-013

- **capability:** CAP-08.04
- **pattern:** ubiquitous
- **statement:** The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications, certifications, recent training, experience and authorization.
- **acceptance_criteria:** Readiness results match an oracle table of 60 cases.
- **source:** PRJ§64
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-102
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-001

- **capability:** CAP-12.01
- **pattern:** ubiquitous
- **statement:** The system shall process every AI request through identity, policy, authorized retrieval, context package, model, output, grounding and confidence, and shall record each step.
- **acceptance_criteria:** Every AI result has a request, context package, model version and lineage record.
- **source:** PRJ§25–28
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-070, UC-071, UC-072
- **quality:** QAS-AI-003
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-002

- **capability:** CAP-12.01
- **pattern:** ubiquitous
- **statement:** The system shall build context packages only from data retrieved with the requesting user's authorization, including vector retrieval.
- **acceptance_criteria:** AI inference suite: 0 retrieved items outside the user's authorization.
- **source:** BRL-008; ADR-P06
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-071
- **quality:** QAS-AI-004
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-003

- **capability:** CAP-12.01
- **pattern:** unwanted-behaviour
- **statement:** If the retrieved evidence is insufficient to answer, then the system shall return 'Insufficient Evidence' instead of generating an answer.
- **acceptance_criteria:** On the insufficient-evidence test set, ≥ 95 % of responses are 'Insufficient Evidence'.
- **source:** PRJ§112
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-072
- **quality:** QAS-AI-002
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-004

- **capability:** CAP-12.01
- **pattern:** ubiquitous
- **statement:** The system shall attach to every AI statement the citations (claim, evidence, source, context reference) that support it.
- **acceptance_criteria:** Citation accuracy on the evaluation set meets QAS-AI-001.
- **source:** PRJ§112
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-072
- **quality:** QAS-AI-001
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-005

- **capability:** CAP-12.02
- **pattern:** ubiquitous
- **statement:** The system shall label every AI-generated draft as AI output and shall prevent its publication without human review.
- **acceptance_criteria:** Publishing an unreviewed AI draft is rejected.
- **source:** AI-OP-02/03; BRL-009
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-073, UC-074
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-006

- **capability:** CAP-12.03
- **pattern:** event-driven
- **statement:** When AI extracts entities, locations or dates from a document, the system shall create proposed claims whose source is the document and whose agent is the model, pending human acceptance.
- **acceptance_criteria:** Extracted claims are not ASSERTED until accepted; lineage names the model version.
- **source:** AI-OP-04
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-072, UC-073
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-007

- **capability:** CAP-12.03
- **pattern:** ubiquitous
- **statement:** The system shall translate between Arabic and English on request without replacing the original text.
- **acceptance_criteria:** Original text is always retained; translations are linked and labelled as machine translation.
- **source:** AI-OP-05; W1 Q26
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-072
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-008

- **capability:** CAP-12.01
- **pattern:** ubiquitous
- **statement:** The system shall enforce the AI autonomy matrix, allowing at most AIL3 in R2 and forbidding AIL5.
- **acceptance_criteria:** Any AI operation above its matrix level is rejected; forbidden operations are unreachable.
- **source:** 10-ai/autonomy-matrix; HAP-06
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-074
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-009

- **capability:** CAP-12.04
- **pattern:** ubiquitous
- **statement:** The system shall manage models through the lifecycle REGISTERED, EVALUATING, APPROVED, STAGED, PRODUCTION, MONITORED, DEPRECATED, RETIRED.
- **acceptance_criteria:** A model not in PRODUCTION cannot serve production requests.
- **source:** PRJ§30
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-010

- **capability:** CAP-12.04
- **pattern:** event-driven
- **statement:** When a model version is proposed for production, the system shall require evaluation results for groundedness, citation accuracy, hallucination rate, latency and cost, and human approval.
- **acceptance_criteria:** Promotion without an approved evaluation report is rejected.
- **source:** PRJ§31
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** QAS-AI-001, QAS-AI-002
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-011

- **capability:** CAP-12.01
- **pattern:** ubiquitous
- **statement:** The system shall run all models on local infrastructure by default and shall use external models only where a tenant policy allows it and only for unclassified data.
- **acceptance_criteria:** Egress to external model endpoints occurs only under an active tenant policy and only with unclassified context.
- **source:** W1 Q20, Q28
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-012

- **capability:** CAP-12.01
- **pattern:** unwanted-behaviour
- **statement:** If content retrieved into a context package contains instructions, then the system shall treat it as data and shall not let it change tools, permissions or recipients.
- **acceptance_criteria:** Indirect prompt-injection test suite: 0 successful tool or permission changes.
- **source:** PRJ§111; THR-013
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-071
- **quality:** QAS-AI-004
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-013

- **capability:** CAP-12.01
- **pattern:** ubiquitous
- **statement:** The system shall register every tool available to AI runs, with the permission it requires and its autonomy level.
- **acceptance_criteria:** An AI run cannot call an unregistered tool.
- **source:** DOM-23 AI Tool Registry
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-AI-014

- **capability:** CAP-12.01
- **pattern:** ubiquitous
- **statement:** The system shall maintain a vector projection of authorized content with the same security labels and pre-filtering as search.
- **acceptance_criteria:** Vector retrieval satisfies the non-inference properties P-51..P-53.
- **source:** ADR-P06; CR-11
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-071
- **quality:** QAS-AI-004
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-PRD-001

- **capability:** CAP-10.02
- **pattern:** ubiquitous
- **statement:** The system shall produce reports, briefings, map products and analytical products from versioned templates with sections, data, evidence, citations, maps and charts.
- **acceptance_criteria:** A product can be generated from a template and every data element traces to its source version.
- **source:** PRJ§65 Product; DOM-20
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-110
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-PRD-002

- **capability:** CAP-10.02
- **pattern:** ubiquitous
- **statement:** The system shall set a product's label to at least the highest label of its content and shall render only content visible to the product's approved audience.
- **acceptance_criteria:** A product never contains content above its label.
- **source:** ADR-P06; LABEL-DERIVATION
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-110
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-PRD-003

- **capability:** CAP-10.02
- **pattern:** event-driven
- **statement:** When a product is approved, the system shall freeze its content as an immutable version with its citations pinned.
- **acceptance_criteria:** Edits after approval create a new version.
- **source:** PRJ§65 Review/Approval
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-111
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-PRD-004

- **capability:** CAP-10.02
- **pattern:** event-driven
- **statement:** When a product is distributed, the system shall deliver it only to recipients authorized for its label and shall record each distribution.
- **acceptance_criteria:** Distribution to an unauthorized recipient is rejected; distribution log complete.
- **source:** PRJ§65 Distribution
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-112
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-PRD-005

- **capability:** CAP-10.02
- **pattern:** ubiquitous
- **statement:** The system shall export approved products as PDF and as documents with a watermark identifying the recipient.
- **acceptance_criteria:** Exported files carry recipient watermark and product version.
- **source:** POL-EXPORT-BULK; THR (leakage)
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-112
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-KNW-001

- **capability:** CAP-11.01
- **pattern:** ubiquitous
- **statement:** The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims with evidence, relationships, versions, review, approval and publication.
- **acceptance_criteria:** A knowledge object cannot be published without review and approval.
- **source:** PRJ§65 KnowledgeObject; DOM-21
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-060, UC-061, UC-062
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-KNW-002

- **capability:** CAP-11.01
- **pattern:** event-driven
- **statement:** When a task, plan, incident, or exercise simulation is closed or completed, the system shall allow capturing lessons linked to it and to its evidence.
- **acceptance_criteria:** Lessons link to the closed or completed object and its evidence (task, plan, incident, or a completed exercise simulation — CR-63).
- **source:** VS06; OUT-06
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-060
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-KNW-003

- **capability:** CAP-11.01
- **pattern:** event-driven
- **statement:** When a published knowledge object is relevant to a new plan or task type, the system shall suggest it to the planner.
- **acceptance_criteria:** Suggestions are based on declared relationships; reuse is recorded (OUT-06).
- **source:** VS06 Reuse
- **priority:** should
- **verification_method:** test
- **use_cases:** UC-062
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-ARC-001

- **capability:** CAP-11.03
- **pattern:** ubiquitous
- **statement:** The system shall transfer records reaching the ARCHIVE disposition action into archive packages containing content, metadata, provenance, integrity hashes and access history.
- **acceptance_criteria:** Archive packages validate against the package schema and their hashes.
- **source:** PRJ§65 ArchiveRecord; SLC-12a
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-063
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-ARC-002

- **capability:** CAP-11.03
- **pattern:** ubiquitous
- **statement:** The system shall preserve archive packages in preservation formats and verify their integrity periodically.
- **acceptance_criteria:** Integrity verification runs on all packages at least yearly with 0 unreported failures.
- **source:** PRJ§65 Preservation/Integrity
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-063
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-ARC-003

- **capability:** CAP-11.03
- **pattern:** event-driven
- **statement:** When an authorized user requests a historical record, the system shall retrieve it within the archive retrieval target and audit the access.
- **acceptance_criteria:** Retrieval meets QAS-ARC-001; access history updated.
- **source:** DOM-22 Historical Retrieval
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-064
- **quality:** QAS-ARC-001
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-ARC-004

- **capability:** CAP-11.03
- **pattern:** event-driven
- **statement:** When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the state from versions, events, valid time, effective time and provenance, labelling each element RECORDED, RECONSTRUCTED, INFERRED or UNKNOWN.
- **acceptance_criteria:** Reconstruction of the reference scenarios matches the oracle; every element is labelled.
- **source:** PRJ§103; CR-25
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-065
- **quality:** QAS-ARC-002
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-COL-001

- **capability:** CAP-02.01
- **pattern:** ubiquitous
- **statement:** The system shall record information needs as collection requirements with question, area, time window, priority, requester and due date.
- **acceptance_criteria:** A collection requirement cannot be approved without area, window and priority.
- **source:** DOM-05; BP01–BP02
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-120
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-COL-002

- **capability:** CAP-02.01
- **pattern:** event-driven
- **statement:** When a collection requirement is approved, the system shall allow planning collection activities with methods, sources and assigned field tasks.
- **acceptance_criteria:** Collection activities create tasks through SLC-03 and link back to the requirement.
- **source:** BP03–BP04
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-121
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-COL-003

- **capability:** CAP-02.01
- **pattern:** event-driven
- **statement:** When observations answering a collection requirement are validated, the system shall update the requirement's fulfilment status.
- **acceptance_criteria:** Fulfilment shows answered, partially answered or open with linked observations.
- **source:** VS01
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-122
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-CRD-001

- **capability:** CAP-06.03
- **pattern:** ubiquitous
- **statement:** The system shall manage coordination cases linking decisions, plans and organizations that must act together, with participants, responsibilities and status.
- **acceptance_criteria:** Each participant sees only the parts of the case they are authorized for.
- **source:** DOM-10 Coordination Case
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-130
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-CRD-002

- **capability:** CAP-06.03
- **pattern:** event-driven
- **statement:** When a coordination action requires another organization's authority, the system shall route it for that authority's decision and record the outcome.
- **acceptance_criteria:** Cross-organization actions are not executed without the other authority's recorded decision.
- **source:** BRL-003
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-131
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-FUS-001

- **capability:** CAP-04.04
- **pattern:** ubiquitous
- **statement:** The system shall correlate observations and claims across sources in space and time into correlation proposals with method, score and evidence.
- **acceptance_criteria:** Correlation proposals never change claims; acceptance creates relationships or ER cases.
- **source:** DOM-07 Correlation/Fusion
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-132
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-FUS-002

- **capability:** CAP-04.04
- **pattern:** ubiquitous
- **statement:** The system shall record for each fused result the contributing sources and their reliabilities.
- **acceptance_criteria:** Fused results trace to every contributing source (lineage).
- **source:** PRJ§23
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-132
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-INT-001

- **capability:** CAP-02.04
- **pattern:** ubiquitous
- **statement:** The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims, persons and documents without making external systems sources of truth.
- **acceptance_criteria:** Each integration has an ACTIVE adapter, mapping tests and lineage; conflicting values create conflicts, not overwrites.
- **source:** W1 Q24; BRL-013
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-094
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-INT-002

- **capability:** CAP-02.04
- **pattern:** ubiquitous
- **statement:** The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a.
- **acceptance_criteria:** Sensor ingestion meets QAS-PERF-012.
- **source:** W1 Q11
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-094
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-INT-003

- **capability:** CAP-10.01
- **pattern:** optional-feature
- **statement:** Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2).
- **acceptance_criteria:** Alerts export and import as valid CAP 1.2 messages.
- **source:** W1 Q25
- **priority:** should
- **verification_method:** test
- **use_cases:** UC-023
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-INT-004

- **capability:** CAP-01.02
- **pattern:** event-driven
- **statement:** When HRIS reports a change of role or organization for a person, the system shall propose the corresponding role-assignment change for administrator approval.
- **acceptance_criteria:** No role changes are applied automatically from HRIS.
- **source:** SLC-01 THR-S01-01
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-084
- **quality:** —
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RES-014

- **capability:** CAP-08.01
- **pattern:** event-driven
- **statement:** When an asset is reserved for a time window, the system shall reject any other reservation or assignment of that asset overlapping the window.
- **acceptance_criteria:** Overlapping reservations are rejected with ASSET_RESERVED and the holder reference.
- **source:** DOM-14; UC-052
- **priority:** must
- **verification_method:** test
- **use_cases:** UC-052
- **quality:** QAS-RES-001
- **release:** R2
- **status:** APPROVED_DELEGATED

### REQ-RCM-001

- **capability:** CAP-09.01
- **pattern:** ubiquitous
- **statement:** The system shall allow an authorized actor to identify a risk with a hazard category, description, and at least one scope reference (asset, area, organization or plan).
- **acceptance_criteria:** A risk can be created with all listed attributes; category_ref resolves against the tenant's hazard category catalog (RD-HAZARD-CATEGORIES).
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-002

- **capability:** CAP-09.01
- **pattern:** ubiquitous
- **statement:** The system shall require a likelihood and an impact rating (1-5) to assess a risk, and shall compute the risk score itself rather than accept it as input.
- **acceptance_criteria:** risk_score is always likelihood x impact; a request that supplies risk_score directly is rejected or ignored.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-003

- **capability:** CAP-09.01
- **pattern:** constraint
- **statement:** Where tenant policy requires segregation of duties, the system shall reject a risk assessment or reassessment performed by the same actor who identified the risk.
- **acceptance_criteria:** Assessment by the identifying actor is rejected with SEGREGATION_OF_DUTIES when the policy is enabled.
- **source:** DOM-17; mirrors INV-TASK-07
- **priority:** should
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-004

- **capability:** CAP-09.01
- **pattern:** constraint
- **statement:** The system shall require at least one treatment action for a risk moving to treated status, unless the chosen strategy is 'accept' with an authorized approver recorded.
- **acceptance_criteria:** Planning treatment with strategy other than accept and zero treatment actions is rejected with TREATMENT_INVALID.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-005

- **capability:** CAP-09.01
- **pattern:** constraint
- **statement:** The system shall require an explicit rationale to close a risk, and shall provide no command to reopen a closed risk.
- **acceptance_criteria:** Close without rationale is rejected with RATIONALE_REQUIRED; no reopen operation exists in the API.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-006

- **capability:** CAP-09.02
- **pattern:** ubiquitous
- **statement:** The system shall allow any authorized actor to report an incident with a hazard category, description, at least one scope reference, and a default severity of MINOR.
- **acceptance_criteria:** An incident can be reported with all listed attributes; severity defaults to MINOR when not stated.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-007

- **capability:** CAP-09.02
- **pattern:** ubiquitous
- **statement:** The system shall require an authorized assessor to set an incident's severity to one of MINOR, MAJOR, EMERGENCY or CRISIS before a response can be dispatched.
- **acceptance_criteria:** Dispatching a response before assessment is rejected with the aggregate's invalid-state-transition error.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-008

- **capability:** CAP-09.02
- **pattern:** ubiquitous
- **statement:** The system shall require a commander and at least one linked response task before an incident moves to responding status.
- **acceptance_criteria:** Dispatch without a commander or without at least one response_task_ref is rejected with RESPONSE_REQUIRED.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-009

- **capability:** CAP-09.02
- **pattern:** event-driven
- **statement:** When an incident's severity is escalated, the system shall accept only a value higher than the current severity, and shall change severity downward only through a distinct, separately-authorized de-escalation command.
- **acceptance_criteria:** An escalate command with a severity not higher than current is rejected with SEVERITY_MUST_INCREASE; severity never decreases except via CMD-INC-DE-ESCALATE.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-010

- **capability:** CAP-09.02
- **pattern:** constraint
- **statement:** The system shall reject closing an incident while any of its linked response tasks is not in a terminal state.
- **acceptance_criteria:** Close is rejected with RESPONSE_TASKS_OPEN while a linked task remains non-terminal.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-011

- **capability:** CAP-09.03
- **pattern:** constraint
- **statement:** The system shall never activate a contingency plan automatically as a side effect of a severity escalation; activation shall always be a distinct, separately-authorized command.
- **acceptance_criteria:** Escalating an incident's severity alone never creates or links a Plan; only CMD-INC-ACTIVATE-CONTINGENCY does, and it requires its own authorization.
- **source:** DOM-17; anti-pattern lesson from SLC-09 (Silent Pre-emption)
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-012

- **capability:** CAP-09.02
- **pattern:** constraint
- **statement:** When an incident references a risk as materialized, the system shall not change that risk's state automatically; the risk owner acts on it through a separate command.
- **acceptance_criteria:** Creating, escalating or closing an incident with a risk_ref never changes the referenced risk's state or version.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-013

- **capability:** CAP-09.02
- **pattern:** ubiquitous
- **statement:** The system shall allow a response task to be created directly under an incident (incident_ref) without requiring a plan.
- **acceptance_criteria:** CMD-TASK-CREATE with incident_ref and without plan_ref or ad_hoc_reason succeeds (CR-61).
- **source:** DOM-17; CR-61
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-014

- **capability:** CAP-09.01
- **pattern:** ubiquitous
- **statement:** The system shall let an authorized actor list and filter the risk register by category, scope and score, restricted to the caller's visible scope.
- **acceptance_criteria:** Risks outside the caller's allowed_scope never appear in the list or count.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-015

- **capability:** CAP-09.02
- **pattern:** ubiquitous
- **statement:** The system shall let an authorized actor list and filter incidents by category, severity, status and scope, restricted to the caller's visible scope.
- **acceptance_criteria:** Incidents outside the caller's allowed_scope never appear in the list or count.
- **source:** DOM-17
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-RCM-016

- **capability:** CAP-09.03
- **pattern:** ubiquitous
- **statement:** The system shall compute an incident's recovery status from its linked contingency plan's task completion against the incident's start time, as an estimate, without a separate recovery state machine.
- **acceptance_criteria:** Recovery status is a read query over existing Plan/Task data (SLC-08/SLC-03); no new aggregate stores recovery state (R3-Q2, R3-Q4 reuse decisions).
- **source:** DOM-17; R3-Q2; R3-Q4
- **priority:** should
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-001

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall allow an authorized actor to request a quantity of a logistics item to a destination, and shall issue a matching resource allocation request against the item's pool in the same unit of work.
- **acceptance_criteria:** Creating a logistics request always creates exactly one linked allocation (target = the request, CR-62); no logistics request exists without one.
- **source:** DOM-16
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-002

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall track logistics item inventory as a Resource Pool (SLC-09) rather than a separate stock model, and shall commit a logistics request's quantity through the existing allocation checks and capacity ledger, unchanged.
- **acceptance_criteria:** No logistics-specific capacity table or reservation engine exists; SPEC-ALLOCATION §1/§2 apply to logistics requests exactly as to any other allocation (R3-Q3).
- **source:** DOM-16; R3-Q3
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-003

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** A logistics request's approval routing shall exactly follow its linked allocation's approval outcome; no separate approval step exists at the request level.
- **acceptance_criteria:** A logistics request reaches APPROVED, PENDING_APPROVAL or REJECTED only as a system-driven consequence of the linked allocation's own EVT-ALC-COMMITTED / -APPROVAL-REQUIRED / -REJECTED events, never through a request-level approval command.
- **source:** DOM-16
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-004

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall allow dispatch of an approved logistics request only while its linked allocation remains COMMITTED, creating a Shipment for a quantity not exceeding the request.
- **acceptance_criteria:** CMD-LGR-DISPATCH is rejected with ALLOCATION_NOT_COMMITTED if the linked allocation is no longer COMMITTED; the created Shipment's planned_quantity never exceeds the requested quantity.
- **source:** DOM-16
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-005

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall record a shipment's movement as an append-only, chronologically ordered checkpoint history.
- **acceptance_criteria:** CMD-SHP-RECORD-CHECKPOINT is rejected with CHECKPOINT_INVALID if the new checkpoint's time is not strictly after the previous one; no command edits or removes an existing checkpoint.
- **source:** DOM-16
- **priority:** should
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-006

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall record the quantity actually delivered at receipt, distinct from the quantity planned, and shall never mark a logistics request fulfilled when the delivered quantity is less than requested.
- **acceptance_criteria:** delivered_quantity is a required field on CMD-SHP-DELIVER; the linked logistics request reaches FULFILLED only when delivered_quantity equals the requested quantity, otherwise PARTIALLY_FULFILLED.
- **source:** DOM-16
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-007

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall allow reporting a shipment as damaged or lost in transit, recording the reason and, for damage, the affected quantity.
- **acceptance_criteria:** CMD-SHP-REPORT-DAMAGE requires a reason and a damaged_quantity not exceeding the planned quantity; CMD-SHP-REPORT-LOST requires a reason.
- **source:** DOM-16
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-008

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall record consumption on a logistics request's linked allocation only from a confirmed shipment outcome (delivered, damaged, or lost), never speculatively at dispatch.
- **acceptance_criteria:** No CMD-ALC-RECORD-CONSUMPTION is issued for a logistics-linked allocation before the linked Shipment reaches DELIVERED, DAMAGED or LOST.
- **source:** DOM-16
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-009

- **capability:** CAP-08.03
- **pattern:** constraint
- **statement:** The system shall allow cancelling a logistics request before dispatch, releasing its linked allocation, and shall allow cancelling a shipment only before departure.
- **acceptance_criteria:** CMD-LGR-CANCEL is accepted from REQUESTED, PENDING_APPROVAL or APPROVED only; CMD-SHP-CANCEL is accepted from PLANNED only, rejected once IN_TRANSIT.
- **source:** DOM-16
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-010

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall let an authorized actor list and filter logistics requests by item, destination, state and priority, restricted to the caller's visible scope.
- **acceptance_criteria:** Logistics requests outside the caller's allowed_scope never appear in the list or count.
- **source:** DOM-16
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-011

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall let an authorized actor list and filter shipments by logistics request, carrier, state and window, restricted to the caller's visible scope.
- **acceptance_criteria:** Shipments outside the caller's allowed_scope never appear in the list or count.
- **source:** DOM-16
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-012

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall provide the full, ordered checkpoint history of a shipment to an authorized actor.
- **acceptance_criteria:** QRY-SHP-TRACKING returns every recorded checkpoint for a shipment in chronological order.
- **source:** DOM-16
- **priority:** should
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-013

- **capability:** CAP-08.03
- **pattern:** ubiquitous
- **statement:** The system shall resolve a logistics item's identity against a per-tenant reference catalog (RD-LOGISTICS-ITEM-TYPES) rather than a fixed list, consistent with the existing resource-type/asset-type pattern.
- **acceptance_criteria:** No logistics item type is hard-coded in the domain model; item_pool resolves to a resource_type value from the tenant's catalog.
- **source:** DOM-16; R2-Q1
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-LOG-014

- **capability:** CAP-08.03
- **pattern:** constraint
- **statement:** Contention among logistics requests for the same pool shall be resolved exactly as SLC-09 resolves allocation contention (priority then request time within the pool's ordering window); no separate logistics-specific ordering rule shall be introduced.
- **acceptance_criteria:** No logistics-specific contention or ordering logic exists outside SPEC-ALLOCATION §2.
- **source:** DOM-16; R3-Q3
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-001

- **capability:** CAP-08.05
- **pattern:** ubiquitous
- **statement:** The system shall allow defining a training scenario with a situation narrative, target competencies and an ordered set of injects, under a versioned DRAFT → ACTIVE → RETIRED lifecycle with segregation of duties on activation.
- **acceptance_criteria:** CMD-SCN-ACTIVATE is rejected with SEGREGATION_OF_DUTIES when the approver equals the author; injects are rejected unless strictly ordered by offset (INV-SCN-01).
- **source:** DOM-19; R3-Q4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-002

- **capability:** CAP-08.05
- **pattern:** constraint
- **statement:** Editing an ACTIVE scenario shall create a new version; an exercise already planned against a prior version shall keep its frozen reference unaffected.
- **acceptance_criteria:** After CMD-SCN-EDIT on an ACTIVE scenario, an exercise planned earlier still reports its original scenario_version_frozen.
- **source:** DOM-19; R3-Q4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-003

- **capability:** CAP-08.05
- **pattern:** constraint
- **statement:** An exercise shall be planned only against a scenario that is ACTIVE at that instant; the scenario reference shall be frozen for the life of the exercise.
- **acceptance_criteria:** CMD-EXR-PLAN referencing a DRAFT or RETIRED scenario is rejected with EXERCISE_INVALID.
- **source:** DOM-19; R3-Q4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-004

- **capability:** CAP-08.05
- **pattern:** ubiquitous
- **statement:** An exercise shall be scheduled with a valid time window, a location and confirmed participants before it can start.
- **acceptance_criteria:** CMD-EXR-START is rejected unless the exercise is SCHEDULED with window.from < window.to.
- **source:** DOM-19; R3-Q4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-005

- **capability:** CAP-08.05
- **pattern:** event-driven
- **statement:** Starting a scheduled exercise shall create exactly one linked simulation run, in the same unit of work.
- **acceptance_criteria:** After CMD-EXR-START, exactly one Simulation exists referencing the exercise and its frozen scenario, created in the same transaction as EVT-EXR-STARTED.
- **source:** DOM-19; R3-Q4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-006

- **capability:** CAP-08.05
- **pattern:** constraint
- **statement:** An exercise's terminal outcome (COMPLETED or ABORTED) shall be driven exclusively by its linked simulation's own outcome; no direct human command shall set either state.
- **acceptance_criteria:** No command exists whose guard transitions an Exercise directly to COMPLETED or ABORTED; both are reachable only via the SYS: rows of the state × command matrix.
- **source:** DOM-19; R3-Q4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-007

- **capability:** CAP-08.05
- **pattern:** constraint
- **statement:** An exercise shall be cancellable with a reason before it starts, and never once it is in progress.
- **acceptance_criteria:** CMD-EXR-CANCEL succeeds from PLANNED or SCHEDULED only; rejected with EXERCISE_INVALID_STATE_TRANSITION from IN_PROGRESS.
- **source:** DOM-19; R3-Q4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-008

- **capability:** CAP-08.05
- **pattern:** constraint
- **statement:** A simulation run shall record inject deliveries as an append-only, strictly time-ordered log.
- **acceptance_criteria:** CMD-SIM-DELIVER-INJECT is rejected with INJECT_INVALID unless delivered_at is strictly after the previous delivery for that simulation (INV-SIM-01); no edit or delete command exists for a delivered inject.
- **source:** DOM-19; R3-Q4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-009

- **capability:** CAP-08.05
- **pattern:** constraint
- **statement:** A simulation run shall record a per-participant, per-competency evaluation, always by an evaluator distinct from the participant being evaluated.
- **acceptance_criteria:** CMD-SIM-RECORD-EVALUATION is rejected with SEGREGATION_OF_DUTIES when evaluator equals participant (INV-SIM-03).
- **source:** DOM-19; R3-Q4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-010

- **capability:** CAP-08.05
- **pattern:** constraint
- **statement:** A simulation run shall reach COMPLETED only when every participant listed on its linked exercise has at least one recorded evaluation.
- **acceptance_criteria:** CMD-SIM-COMPLETE is rejected with EVALUATION_MISSING while any exercise participant has zero recorded evaluations (INV-SIM-02).
- **source:** DOM-19; R3-Q4
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-011

- **capability:** CAP-08.05
- **pattern:** ubiquitous
- **statement:** A simulation run shall be pausable and resumable, or abortable with a reason, without losing any previously recorded inject-delivery or evaluation history.
- **acceptance_criteria:** CMD-SIM-PAUSE/CMD-SIM-RESUME/CMD-SIM-ABORT never remove or alter a prior InjectDelivery or Evaluation record.
- **source:** DOM-19; R3-Q4
- **priority:** should
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-012

- **capability:** CAP-08.05
- **pattern:** ubiquitous
- **statement:** A person's qualification record shall be able to cite a completed simulation run as evidence, using the existing, unmodified Qualification Record evidence reference — no schema change to SLC-03.
- **acceptance_criteria:** CMD-QUAL-RECORD/CMD-QUAL-RENEW accept a completed simulation's URN in their existing evidence:urn field without any change to AGG-QUALIFICATION-RECORD's guard or payload schema.
- **source:** DOM-18; R3-Q4
- **priority:** should
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-013

- **capability:** CAP-08.05
- **pattern:** event-driven
- **statement:** A completed simulation run shall be usable as the terminal source of an After Action Review, captured as a lesson-type Knowledge Object in BC06.
- **acceptance_criteria:** CMD-KNO-DRAFT with knowledge_type=lesson accepts a completed Simulation's URN as source (CR-63), with no payload schema change to AGG-KNOWLEDGE-OBJECT.
- **source:** DOM-19; R3-Q5; CR-63
- **priority:** should
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-014

- **capability:** CAP-08.05
- **pattern:** ubiquitous
- **statement:** The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted to the caller's visible scope.
- **acceptance_criteria:** Scenarios, exercises and simulations outside the caller's allowed_scope never appear in a list or count.
- **source:** DOM-18; DOM-19
- **priority:** must
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

### REQ-TRX-015

- **capability:** CAP-08.05
- **pattern:** ubiquitous
- **statement:** The system shall provide the full, ordered timeline of inject deliveries and evaluations for a simulation run to an authorized actor.
- **acceptance_criteria:** QRY-SIM-TIMELINE returns every recorded inject delivery and evaluation for a simulation in chronological order.
- **source:** DOM-19
- **priority:** should
- **verification_method:** test
- **use_cases:** —
- **quality:** —
- **release:** R3
- **status:** APPROVED_DELEGATED

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
business_requirements:
- id: BRQ-001
  title: Unified Information
  statement: The organization shall have one authorized point of access to its geospatial, documentary and operational information.
  outcomes:
  - OUT-01
  - OUT-02
  acceptance_criteria: ≥ 90 % of in-scope sources integrated and searchable (OUT-01)
  verification_method: measurement at pilot + test
  status: APPROVED_DELEGATED
- id: BRQ-002
  title: Contextual Understanding
  statement: The organization shall be able to see any situation in its place, time and relationships.
  outcomes:
  - OUT-02
  acceptance_criteria: Situation picture build time reduced ≥ 50 % vs pilot baseline
  verification_method: measurement at pilot + test
  status: APPROVED_DELEGATED
- id: BRQ-003
  title: Decision Support
  statement: Decisions shall be supported by assessments and evidence and taken by the competent authority.
  outcomes:
  - OUT-03
  - OUT-04
  acceptance_criteria: 100 % of decisions linked to assessment/evidence and authority
  verification_method: measurement at pilot + test
  status: APPROVED_DELEGATED
- id: BRQ-004
  title: Operational Execution
  statement: Decisions shall be executed through approved plans and tracked tasks.
  outcomes:
  - OUT-05
  acceptance_criteria: 100 % of tasks linked to a plan or justified ad-hoc owner
  verification_method: measurement at pilot + test
  status: APPROVED_DELEGATED
- id: BRQ-005
  title: Institutional Learning
  statement: Experience from execution shall be captured and reusable.
  outcomes:
  - OUT-06
  acceptance_criteria: ≥ 1 after-action review per closed major operation (R2 full)
  verification_method: measurement at pilot + test
  status: APPROVED_DELEGATED
- id: BRQ-006
  title: Traceability
  statement: Any important result shall be traceable to its sources, inputs and actors.
  outcomes:
  - OUT-03
  - OUT-04
  acceptance_criteria: 100 % of T1 derived objects and decisions traceable
  verification_method: measurement at pilot + test
  status: APPROVED_DELEGATED
- id: BRQ-007
  title: Governance
  statement: Access, classification, retention and privacy shall be enforced by policy and auditable.
  outcomes:
  - OUT-04
  acceptance_criteria: 0 leaks in isolation and inference suites; 100 % audit coverage
  verification_method: measurement at pilot + test
  status: APPROVED_DELEGATED
- id: BRQ-008
  title: Integration
  statement: External systems shall connect through explicit, versioned contracts without becoming automatic sources of truth.
  outcomes:
  - OUT-01
  acceptance_criteria: All R1 integrations via registered adapters with lineage
  verification_method: measurement at pilot + test
  status: APPROVED_DELEGATED
system_requirements:
- id: REQ-FND-001
  capability: CAP-01.01
  pattern: ubiquitous
  statement: The system shall isolate each tenant's data, policies, configuration, projections, files, events and audit records
    from every other tenant.
  acceptance_criteria: No command, query, search, map, export, event subscription or AI context returns or reveals data of
    another tenant in the tenant-isolation test suite.
  source: W1 Q6; PRJ§6
  priority: must
  verification_method: test
  use_cases:
  - UC-080
  quality:
  - QAS-SEC-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-002
  capability: CAP-01.01
  pattern: ubiquitous
  statement: The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational
    units of unlimited depth.
  acceptance_criteria: A tenant with 2 organizations and 5 unit levels can be created; every query is scoped to the caller's
    tenant.
  source: W1 Q32; PRJ§7.1
  priority: must
  verification_method: test
  use_cases:
  - UC-081
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-003
  capability: CAP-01.01
  pattern: event-driven
  statement: When a tenant is provisioned, the system shall create its isolation boundary, classification scheme, default
    roles, quotas and audit stream before any user of that tenant can sign in.
  acceptance_criteria: 'Provisioning is atomic: an injected failure at any step leaves no tenant usable by end users.'
  source: W1 Q6; SR-07
  priority: must
  verification_method: test
  use_cases:
  - UC-080
  quality:
  - QAS-SCAL-003
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-004
  capability: CAP-01.01
  pattern: optional-feature
  statement: Where a tenant is designated dedicated or sovereign, the system shall run that tenant in its own cell with no
    data store shared with other tenants.
  acceptance_criteria: A dedicated-cell tenant is deployed from the same release artifacts and shares no database, object
    store, index or event stream with other cells.
  source: W1 Q6; SR-09
  priority: must
  verification_method: test
  use_cases:
  - UC-080
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-005
  capability: CAP-01.02
  pattern: ubiquitous
  statement: The system shall authenticate human users only through a configured external identity provider using OIDC or
    SAML, and shall support account provisioning through SCIM.
  acceptance_criteria: Sign-in succeeds via OIDC and via SAML test IdPs; SCIM create/disable propagates within 5 minutes.
  source: W1 Q24, Q25
  priority: must
  verification_method: test
  use_cases:
  - UC-084
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-006
  capability: CAP-01.02
  pattern: ubiquitous
  statement: The system shall maintain Person, Identity, User and Service Account as separate records with explicit links.
  acceptance_criteria: A person with two identities and one user account, and a service account with no person, are represented
    without duplication.
  source: PRJ§56
  priority: must
  verification_method: test
  use_cases:
  - UC-084
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-007
  capability: CAP-01.03
  pattern: ubiquitous
  statement: The system shall record authority as a grant stating decision type, organizational scope, limits and validity
    period, held by a role or a person.
  acceptance_criteria: An authority grant with scope, monetary/volume limit and expiry can be created, queried and expires
    automatically.
  source: W1 Q31; PRJ§7.1
  priority: must
  verification_method: test
  use_cases:
  - UC-082
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-008
  capability: CAP-01.03
  pattern: event-driven
  statement: When an authority holder delegates authority, the system shall record delegator, delegate, scope, limits and
    validity period, and shall reject any delegation exceeding the delegator's own authority.
  acceptance_criteria: Delegation beyond delegator scope or limits is rejected with AUTHORITY_EXCEEDS_DELEGATOR; valid delegation
    is effective only within its period.
  source: PRJ§7.1
  priority: must
  verification_method: test
  use_cases:
  - UC-083
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-009
  capability: CAP-01.03
  pattern: ubiquitous
  statement: The system shall provide an authority check returning whether an actor holds authority for a given decision type,
    scope and point in time, including through delegation.
  acceptance_criteria: Authority check results match an oracle table of 50 grant/delegation/time combinations.
  source: W1 Q31; CR-32
  priority: must
  verification_method: test
  use_cases:
  - UC-032
  - UC-035
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-010
  capability: CAP-01.04
  pattern: ubiquitous
  statement: The system shall evaluate authorization before retrieving data for every command, query, search, map request,
    export, event subscription and AI retrieval.
  acceptance_criteria: Architecture fitness test finds no retrieval path that executes before a policy decision; penetration
    tests find no bypass.
  source: PRJ§5; BRL-008, BRL-010
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-SEC-002
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-011
  capability: CAP-01.04
  pattern: ubiquitous
  statement: The system shall base authorization decisions on subject, action, resource, purpose, context, classification,
    compartments and jurisdiction.
  acceptance_criteria: Policy test matrix covers each attribute; changing any single attribute changes the decision where
    the policy says it should.
  source: PRJ§66; CR-24
  priority: must
  verification_method: test
  use_cases:
  - UC-086
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-012
  capability: CAP-01.04
  pattern: ubiquitous
  statement: The system shall return a policy decision of ALLOW, DENY, CONDITIONAL, REDACT, AGGREGATE or REQUIRE_APPROVAL,
    with any obligations, and shall enforce the obligations.
  acceptance_criteria: Each decision type is produced by a test policy and its enforcement is observable in the response or
    workflow.
  source: PRJ§66
  priority: must
  verification_method: test
  use_cases:
  - UC-086
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-013
  capability: CAP-01.04
  pattern: unwanted-behaviour
  statement: If the policy decision point is unavailable or returns an error, then the system shall deny the request.
  acceptance_criteria: With the policy engine stopped, 100% of protected requests are denied and logged.
  source: V6 SL-28
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-SEC-005
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-014
  capability: CAP-01.04
  pattern: ubiquitous
  statement: The system shall treat View, Edit, Export, Share, Approve, Delete, Retain and Archive as separately grantable
    permissions.
  acceptance_criteria: A role granted Archive but not Delete cannot delete; each permission is independently testable.
  source: CR-39
  priority: must
  verification_method: test
  use_cases:
  - UC-086
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-015
  capability: CAP-13.02
  pattern: ubiquitous
  statement: The system shall write an audit record for every state-changing command and for every read of data classified
    at or above the tenant's audit threshold, containing actor, action, resource, purpose, policy decision, time and correlation
    id.
  acceptance_criteria: 100% of commands in the end-to-end suite produce exactly one audit record with all fields populated.
  source: BRL-015; PRJ§4
  priority: must
  verification_method: test
  use_cases:
  - UC-087
  quality:
  - QAS-AUD-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-016
  capability: CAP-13.02
  pattern: ubiquitous
  statement: The system shall keep audit records append-only and tamper-evident.
  acceptance_criteria: Modifying or deleting any audit record in storage is detected by the integrity verification job.
  source: PRJ§3.4
  priority: must
  verification_method: test
  use_cases:
  - UC-087
  quality:
  - QAS-SEC-006
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-017
  capability: CAP-13.01
  pattern: event-driven
  statement: When a security exception is requested, the system shall require approval by two distinct authorized persons
    and shall revoke the exception automatically at its expiry.
  acceptance_criteria: Approval by one person, or by the requester, does not activate the exception; the exception stops applying
    at expiry.
  source: W1 Q19
  priority: must
  verification_method: test
  use_cases:
  - UC-088
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-FND-018
  capability: CAP-14.03
  pattern: ubiquitous
  statement: The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs.
  acceptance_criteria: A tenant exceeding its request quota receives RATE_LIMITED while other tenants' latency stays within
    QAS-PERF-001.
  source: SR-07
  priority: must
  verification_method: test
  use_cases:
  - UC-105
  quality:
  - QAS-SCAL-005
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-GOV-001
  capability: CAP-13.01
  pattern: ubiquitous
  statement: The system shall support a per-tenant classification scheme with ordered levels, an unlimited number of compartments
    and release caveats.
  acceptance_criteria: A scheme with 5 levels, 20 compartments and 3 caveats can be configured and enforced.
  source: W1 Q16
  priority: must
  verification_method: test
  use_cases:
  - UC-085
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-GOV-002
  capability: CAP-13.01
  pattern: ubiquitous
  statement: The system shall require a classification on every object of importance tier T1 or T2.
  acceptance_criteria: Creating a T1/T2 object without classification is rejected with CLASSIFICATION_REQUIRED.
  source: W1 Q12, Q16
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-GOV-003
  capability: CAP-13.01
  pattern: ubiquitous
  statement: The system shall permit read access to an object only if the subject's clearance is at least the object's level
    and the subject holds every compartment of the object.
  acceptance_criteria: Access matrix of 5 levels × compartment combinations matches the oracle with 0 deviations.
  source: W1 Q16
  priority: must
  verification_method: test
  use_cases:
  - UC-089
  quality:
  - QAS-SEC-002
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-GOV-004
  capability: CAP-13.01
  pattern: event-driven
  statement: When the classification of an object is changed, the system shall require the authority defined by tenant policy,
    record the change as a new version, and stop returning the object to newly unauthorized subjects from the moment of the
    change in all access paths including projections.
  acceptance_criteria: After a downgrade of a user's access, the next search, map, export and API call does not return the
    object, regardless of index lag.
  source: W1 Q16; ADR-P06
  priority: must
  verification_method: test
  use_cases:
  - UC-085
  - UC-089
  quality:
  - QAS-SEC-003
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-GOV-005
  capability: CAP-13.04
  pattern: ubiquitous
  statement: The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data
    outside it unless a tenant policy explicitly permits the transfer.
  acceptance_criteria: Egress monitoring during the full test suite shows no data leaving the configured jurisdiction boundary.
  source: W1 Q17
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-GOV-006
  capability: CAP-11.02
  pattern: ubiquitous
  statement: The system shall apply a retention schedule to every record class.
  acceptance_criteria: Every record class in the reference data has a retention rule; records past retention are flagged for
    disposition.
  source: W1 Q18
  priority: must
  verification_method: test
  use_cases:
  - UC-103
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-GOV-007
  capability: CAP-11.02
  pattern: event-driven
  statement: When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modification
    until the hold is released.
  acceptance_criteria: Disposition and erasure jobs skip held records; attempts are logged.
  source: W1 Q18
  priority: must
  verification_method: test
  use_cases:
  - UC-103
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-GOV-008
  capability: CAP-13.03
  pattern: event-driven
  statement: When the personal data of a data subject must be erased, the system shall make it unrecoverable in operational
    stores, projections, backups and archives while retaining non-personal audit facts.
  acceptance_criteria: After erasure, the subject's personal data cannot be recovered from any store or restored backup; audit
    facts remain.
  source: W1 Q18; ADR-P08
  priority: must
  verification_method: test
  use_cases:
  - UC-103
  quality:
  - QAS-PRV-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-GOV-009
  capability: CAP-13.01
  pattern: ubiquitous
  statement: The system shall version, audit and time-stamp every policy and configuration change and apply each change from
    its effective time.
  acceptance_criteria: A policy with a future effective time does not apply before it and applies after it; history is queryable.
  source: V5§81
  priority: must
  verification_method: test
  use_cases:
  - UC-086
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-001
  capability: CAP-02.02
  pattern: ubiquitous
  statement: The system shall register each source with type, owner, classification and a reliability rating, and keep the
    history of reliability changes.
  acceptance_criteria: Changing a source's reliability creates a new version; previous ratings remain queryable by time.
  source: PRJ§7.5
  priority: must
  verification_method: test
  use_cases:
  - UC-004
  - UC-095
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-002
  capability: CAP-02.03
  pattern: event-driven
  statement: When an observation is recorded, the system shall store its observation time, its event time where known, its
    record time, its location with CRS and positional accuracy, its source, its observer and its attachments.
  acceptance_criteria: Recorded observations contain all listed fields; record time is assigned by the server, not the client.
  source: PRJ§3.5, §22; V6 SL-11, SL-12
  priority: must
  verification_method: test
  use_cases:
  - UC-005
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-003
  capability: CAP-02.03
  pattern: ubiquitous
  statement: The system shall store attachments (documents, images, video, raster) in object storage and reference them by
    content hash.
  acceptance_criteria: No attachment larger than 1 MB is stored in the operational database; references resolve by hash.
  source: SR-05
  priority: must
  verification_method: test
  use_cases:
  - UC-005
  - UC-006
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-004
  capability: CAP-02.03
  pattern: event-driven
  statement: When an attachment is stored or retrieved, the system shall compute or verify its content hash.
  acceptance_criteria: A corrupted stored object is detected at retrieval and reported as INTEGRITY_ERROR.
  source: PRJ§3.6
  priority: must
  verification_method: test
  use_cases:
  - UC-006
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-005
  capability: CAP-02.04
  pattern: ubiquitous
  statement: The system shall ingest external data only through registered adapters or bulk import jobs that record source,
    batch, transformation and lineage.
  acceptance_criteria: Every ingested record has a lineage record pointing to adapter, batch and transformation version.
  source: W1 Q14, Q24
  priority: must
  verification_method: test
  use_cases:
  - UC-094
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-006
  capability: CAP-02.04
  pattern: unwanted-behaviour
  statement: If an ingested record fails validation, then the system shall quarantine it with the failure reason and shall
    not publish it.
  acceptance_criteria: Invalid records appear in quarantine with reason codes and never in queries or projections.
  source: V5§43
  priority: must
  verification_method: test
  use_cases:
  - UC-094
  quality:
  - QAS-DQ-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-007
  capability: CAP-02.04
  pattern: event-driven
  statement: When an ingestion batch is re-submitted, the system shall not create duplicate records.
  acceptance_criteria: Submitting the same batch twice yields the same record count as once.
  source: PRJ§16 idempotency
  priority: must
  verification_method: test
  use_cases:
  - UC-094
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-008
  capability: CAP-02.04
  pattern: ubiquitous
  statement: The system shall import geospatial data via OGC API Features/Maps/Tiles, WMS/WFS, GeoJSON, GeoPackage, GeoTIFF/COG
    and KML.
  acceptance_criteria: A reference dataset in each format imports with geometry and attributes preserved.
  source: W1 Q25
  priority: must
  verification_method: test
  use_cases:
  - UC-094
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-009
  capability: CAP-02.04
  pattern: ubiquitous
  statement: The system shall ingest weather data through an adapter and register the provider as a source.
  acceptance_criteria: Weather records carry source and observation time and appear as a map layer.
  source: W1 Q24
  priority: must
  verification_method: test
  use_cases:
  - UC-094
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-020
  capability: CAP-03.01
  pattern: ubiquitous
  statement: The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct object
    types.
  acceptance_criteria: Each type has its own identity, lifecycle and schema in the contracts.
  source: PRJ§57
  priority: must
  verification_method: test
  use_cases:
  - UC-001
  - UC-002
  - UC-003
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-021
  capability: CAP-03.02
  pattern: ubiquitous
  statement: The system shall represent each attribute value of an importance-tier T1 object as a claim linked to its sources,
    evidence and confidence.
  acceptance_criteria: Every T1 attribute value in the test corpus resolves to at least one claim with source and confidence.
  source: W1 Q12; ADR-P03; BRL-001
  priority: must
  verification_method: test
  use_cases:
  - UC-006
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-022
  capability: CAP-03.04
  pattern: ubiquitous
  statement: The system shall record a valid-time interval and a record-time interval for every T1 claim.
  acceptance_criteria: Each T1 claim has valid_from/valid_to and recorded_from/recorded_to; open intervals are explicit.
  source: W1 Q13; ADR-P01
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-023
  capability: CAP-03.04
  pattern: event-driven
  statement: When a query specifies a valid time T, a record time K, or both, the system shall return the state valid at T
    as known at K, using the current time for any time not specified.
  acceptance_criteria: Results on the temporal test corpus match the oracle for all (T, K) pairs.
  source: W1 Q13
  priority: must
  verification_method: test
  use_cases:
  - UC-096
  quality:
  - QAS-TMP-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-024
  capability: CAP-03.02
  pattern: ubiquitous
  statement: The system shall never overwrite a T1 claim; a correction shall close the record-time interval of the previous
    claim and create a new claim.
  acceptance_criteria: After a correction, the old claim remains retrievable as known before the correction time.
  source: BRL-002; PRJ§3.4
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-025
  capability: CAP-03.06
  pattern: event-driven
  statement: When two claims about the same subject and attribute overlap in valid time with incompatible values, the system
    shall open a conflict case and retain both claims.
  acceptance_criteria: Conflicting claims create exactly one open conflict case; no claim is removed.
  source: PRJ§24; BRL-002
  priority: must
  verification_method: test
  use_cases:
  - UC-008
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-026
  capability: CAP-03.07
  pattern: ubiquitous
  statement: 'The system shall expose confidence as separate dimensions: source reliability, information confidence, data
    quality, verification status, freshness, completeness and uncertainty.'
  acceptance_criteria: APIs return all seven dimensions; no single mandatory aggregate score exists.
  source: PRJ§3.8; V5§55; CR-03
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-027
  capability: CAP-03.01
  pattern: ubiquitous
  statement: The system shall represent relationships as objects with type, source, target, validity period, evidence, provenance,
    confidence and classification.
  acceptance_criteria: A relationship can be classified higher than its endpoints and is hidden accordingly.
  source: PRJ§3.3
  priority: must
  verification_method: test
  use_cases:
  - UC-003
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-028
  capability: CAP-03.03
  pattern: ubiquitous
  statement: The system shall require every geometry to carry a CRS and a positional accuracy, and shall reject invalid geometries.
  acceptance_criteria: Geometries without CRS, without accuracy, or failing validity checks are rejected with GEOMETRY_INVALID.
  source: V6 SL-12
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-DQ-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-029
  capability: CAP-03.03
  pattern: ubiquitous
  statement: The system shall store each geometry in the canonical CRS WGS 84 (EPSG:4326) and shall keep the original CRS
    and coordinates.
  acceptance_criteria: Round-trip transformation of the reference set returns original coordinates within the stated accuracy.
  source: W2 delegated decision (ADR-P16)
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-030
  capability: CAP-03.03
  pattern: ubiquitous
  statement: The system shall keep the position history of located entities over time.
  acceptance_criteria: The location of an entity at any past valid time is retrievable.
  source: V5§53
  priority: must
  verification_method: test
  use_cases:
  - UC-096
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-031
  capability: CAP-03.01
  pattern: ubiquitous
  statement: The system shall store names in their original form and in normalized and transliterated forms for Arabic and
    English.
  acceptance_criteria: Each name has original, normalized and at least one transliterated form; the original is never modified.
  source: W1 Q15; ADR-P15
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-USA-002
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-032
  capability: CAP-03.05
  pattern: event-driven
  statement: When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, method,
    features, score and evidence, and shall not merge entities without a recorded decision.
  acceptance_criteria: No merge occurs in the test corpus without a decision record naming the reviewer.
  source: PRJ§13
  priority: must
  verification_method: test
  use_cases:
  - UC-007
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-033
  capability: CAP-03.05
  pattern: event-driven
  statement: When entities are matched, the system shall record a same-as link with the decision, reviewer and time, keep
    all original identifiers valid, and resolve any member identifier to the identity cluster's canonical identifier while
    reporting the requested identifier.
  acceptance_criteria: Requests by any member URN return the resolved entity with canonical_urn and requested_urn; no identifier
    is rewritten or deleted.
  source: PRJ§13; ADR-P13
  priority: must
  verification_method: test
  use_cases:
  - UC-007
  quality: []
  release: R1
  status: APPROVED_DELEGATED
  change_log:
  - 'W3: aligned with ER-MODEL (merge = link, no id rewrite)'
- id: REQ-INF-034
  capability: CAP-03.05
  pattern: event-driven
  statement: When a match is reversed, the system shall close the same-as link so that each original entity again resolves
    to exactly its own claims.
  acceptance_criteria: After split, each original entity resolves to exactly the claims whose subject_ref is its own URN;
    the link remains queryable as known before the split.
  source: CR-15
  priority: must
  verification_method: test
  use_cases:
  - UC-104
  quality: []
  release: R1
  status: APPROVED_DELEGATED
  change_log:
  - 'W3: aligned with ER-MODEL (split = close link)'
- id: REQ-INF-035
  capability: CAP-03.07
  pattern: ubiquitous
  statement: 'The system shall record lineage for every derived object: inputs and their versions, the transformation and
    its version, the actor and the execution time.'
  acceptance_criteria: 100% of derived objects in the end-to-end suite have a complete lineage record.
  source: PRJ§23
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-TRC-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-036
  capability: CAP-03.01
  pattern: ubiquitous
  statement: The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type>:<id>,
    and shall map external identifiers per source system.
  acceptance_criteria: Every object exposes both identifiers; an external identifier maps to exactly one object per system
    at a given time.
  source: ADR-P13; PRJ§12
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-INF-037
  capability: CAP-03.07
  pattern: unwanted-behaviour
  statement: If a T1 object is submitted without a source reference, then the system shall reject it.
  acceptance_criteria: Creation without source is rejected with SOURCE_REQUIRED.
  source: BRL-001
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-ANL-001
  capability: CAP-04.01
  pattern: ubiquitous
  statement: The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumptions
    and evidence references.
  acceptance_criteria: An analysis case cannot move beyond DRAFT without a question and scope.
  source: PRJ§58
  priority: must
  verification_method: test
  use_cases:
  - UC-010
  - UC-011
  - UC-012
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-ANL-002
  capability: CAP-04.02
  pattern: event-driven
  statement: When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and version,
    layers, filters, time and spatial extent, assumptions, steps, results, analyst and execution time.
  acceptance_criteria: Every run record contains all listed fields.
  source: PRJ§3.7
  priority: must
  verification_method: test
  use_cases:
  - UC-013
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-ANL-003
  capability: CAP-04.02
  pattern: event-driven
  statement: When a recorded analysis run is re-executed with the same recorded inputs, the system shall produce the same
    results or report which inputs differ.
  acceptance_criteria: Re-execution of 100% of deterministic runs in the test set yields identical results.
  source: PRJ§3.7; OUT-03
  priority: must
  verification_method: test
  use_cases:
  - UC-013
  quality:
  - QAS-TRC-002
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-ANL-004
  capability: CAP-04.02
  pattern: ubiquitous
  statement: The system shall execute long-running analysis runs as asynchronous jobs with status, progress, cancellation
    and retry.
  acceptance_criteria: A run exceeding 10 seconds returns a job reference immediately; status is pollable and subscribable.
  source: PRJ§72; SR-06
  priority: must
  verification_method: test
  use_cases:
  - UC-013
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-ANL-005
  capability: CAP-04.03
  pattern: ubiquitous
  statement: The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, methodology,
    limitations, reviewer and version.
  acceptance_criteria: An assessment cannot be published with any of these fields missing.
  source: PRJ§59
  priority: must
  verification_method: test
  use_cases:
  - UC-015
  - UC-014
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-ANL-006
  capability: CAP-04.03
  pattern: event-driven
  statement: When an assessment is published, the system shall make that version immutable; later changes shall create a new
    version.
  acceptance_criteria: Edit attempts on a published version are rejected; a new version links to its predecessor.
  source: PRJ§59
  priority: must
  verification_method: test
  use_cases:
  - UC-015
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-ANL-007
  capability: CAP-04.01
  pattern: ubiquitous
  statement: The system shall allow comparison of alternative scenarios within an analysis case.
  acceptance_criteria: Two scenarios with different assumptions display side by side with their differing inputs and results.
  source: PRJ§46 UC-016
  priority: should
  verification_method: test
  use_cases:
  - UC-016
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-ANL-008
  capability: CAP-04.03
  pattern: unwanted-behaviour
  statement: If an assessment references evidence the reader is not authorized to view, then the system shall withhold that
    evidence according to policy and shall indicate the omission only where the policy permits.
  acceptance_criteria: Readers without access never receive the evidence content or identifiers; omission markers follow the
    policy setting.
  source: BRL-010; A21
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-SEC-002
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SIT-001
  capability: CAP-05.01
  pattern: ubiquitous
  statement: The system shall define each situation by geographic extent, time window, inclusion criteria, owner and classification.
  acceptance_criteria: A situation cannot be activated without extent, window and criteria.
  source: ADR-P07; PRJ§60
  priority: must
  verification_method: test
  use_cases:
  - UC-020
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SIT-002
  capability: CAP-05.02
  pattern: event-driven
  statement: When an object matching a situation's criteria is created or changed, the system shall update the situation membership
    and record a situation change.
  acceptance_criteria: Membership changes appear in the situation change log with cause and time.
  source: PRJ§60
  priority: must
  verification_method: test
  use_cases:
  - UC-021
  - UC-022
  quality:
  - QAS-PERF-006
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SIT-003
  capability: CAP-05.03
  pattern: ubiquitous
  statement: The system shall present each situation as a map-based common operational picture of its entities, events, risks,
    tasks, resources, assessments and alerts.
  acceptance_criteria: All member types render on the map and in lists, filtered by the viewer's authorization.
  source: PRJ§60
  priority: must
  verification_method: test
  use_cases:
  - UC-024
  - UC-098
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SIT-004
  capability: CAP-05.02
  pattern: event-driven
  statement: When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users.
  acceptance_criteria: Alert raised and delivered within QAS-PERF-005 under design load.
  source: PRJ§7.9
  priority: must
  verification_method: test
  use_cases:
  - UC-023
  quality:
  - QAS-PERF-005
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SIT-005
  capability: CAP-05.02
  pattern: ubiquitous
  statement: The system shall manage alerts through the states RAISED, ACKNOWLEDGED, RESOLVED and DISMISSED, requiring a reason
    for dismissal, and shall audit every transition.
  acceptance_criteria: Dismissal without reason is rejected; every transition has an audit record.
  source: PRJ§7.9
  priority: must
  verification_method: test
  use_cases:
  - UC-023
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SIT-006
  capability: CAP-05.02
  pattern: unwanted-behaviour
  statement: If a user is not authorized for the object that triggered an alert, then the system shall not reveal that object
    or its existence in the alert shown to that user.
  acceptance_criteria: Alert payloads received by unauthorized subscribers contain no identifier, location or attribute of
    the object.
  source: BRL-010; A21
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-SEC-002
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SIT-007
  capability: CAP-05.03
  pattern: ubiquitous
  statement: The system shall serve map layers filtered by the requesting user's authorization and shall not share cached
    map tiles across different authorization scopes.
  acceptance_criteria: Two users with different compartments requesting the same tile receive different content; cache keys
    include the authorization scope.
  source: ADR-P06; ADR-P12
  priority: must
  verification_method: test
  use_cases:
  - UC-098
  quality:
  - QAS-SEC-004
  - QAS-PERF-007
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-DEC-001
  capability: CAP-06.01
  pattern: ubiquitous
  statement: The system shall record each decision request with its question, options, assessment references, deadline and
    required authority type.
  acceptance_criteria: A decision request without options or required authority type cannot be submitted.
  source: PRJ§61
  priority: must
  verification_method: test
  use_cases:
  - UC-030
  - UC-031
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-DEC-002
  capability: CAP-06.02
  pattern: event-driven
  statement: When a decision is recorded, the system shall verify through the authority check that the decider holds the required
    authority at the decision time, and shall reject the decision otherwise.
  acceptance_criteria: Decisions by actors without valid authority are rejected with AUTHORITY_REQUIRED.
  source: BRL-003; REQ-FND-009
  priority: must
  verification_method: test
  use_cases:
  - UC-032
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-DEC-003
  capability: CAP-06.02
  pattern: ubiquitous
  statement: The system shall record for each decision the selected option, rationale, authority, approval, effective time
    and links to the assessments and evidence considered.
  acceptance_criteria: 100% of recorded decisions link to at least one assessment or evidence object.
  source: PRJ§61; OUT-04
  priority: must
  verification_method: test
  use_cases:
  - UC-032
  quality:
  - QAS-TRC-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-DEC-004
  capability: CAP-06.02
  pattern: ubiquitous
  statement: The system shall make a recorded decision immutable; a change shall be recorded as a new decision that supersedes
    it.
  acceptance_criteria: Edit attempts are rejected; supersession links are navigable both ways.
  source: PRJ§3.4
  priority: must
  verification_method: test
  use_cases:
  - UC-032
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-001
  capability: CAP-07.01
  pattern: ubiquitous
  statement: The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities,
    milestones, resources, schedule, dependencies and metrics.
  acceptance_criteria: Plan schema contains all listed parts; a plan cannot be submitted without objectives and outcomes.
  source: PRJ§62
  priority: must
  verification_method: test
  use_cases:
  - UC-033
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-002
  capability: CAP-07.01
  pattern: ubiquitous
  statement: The system shall link every approved plan to the decisions or objectives it implements.
  acceptance_criteria: Approval of a plan without such a link is rejected.
  source: OUT-05
  priority: must
  verification_method: test
  use_cases:
  - UC-033
  - UC-035
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-003
  capability: CAP-07.02
  pattern: event-driven
  statement: When a plan is approved, the system shall create an immutable baseline of that plan version.
  acceptance_criteria: Baseline content cannot be modified; it remains retrievable after later versions.
  source: BRL-004
  priority: must
  verification_method: test
  use_cases:
  - UC-035
  - UC-036
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-004
  capability: CAP-07.02
  pattern: event-driven
  statement: When a major change is made to a baselined plan, the system shall create a new plan version that requires approval
    before it becomes effective.
  acceptance_criteria: Major changes (as defined in BRL-005) create a new version; minor changes do not.
  source: BRL-005
  priority: must
  verification_method: test
  use_cases:
  - UC-034
  - UC-036
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-005
  capability: CAP-07.02
  pattern: unwanted-behaviour
  statement: If the approver of a plan is also its author, then the system shall reject the approval unless tenant policy
    explicitly permits it.
  acceptance_criteria: Self-approval rejected with SEGREGATION_OF_DUTIES under default policy.
  source: W1 Q8
  priority: must
  verification_method: test
  use_cases:
  - UC-035
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-006
  capability: CAP-07.03
  pattern: ubiquitous
  statement: The system shall manage task state according to state machine SM-TASK and reject any transition not defined in
    it.
  acceptance_criteria: Every state × command pair not in SM-TASK is rejected with TASK_INVALID_STATE_TRANSITION.
  source: PRJ§55; V6§13.5
  priority: must
  verification_method: test
  use_cases:
  - UC-040
  - UC-042
  - UC-043
  - UC-044
  - UC-045
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-007
  capability: CAP-07.03
  pattern: event-driven
  statement: When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares required
    competencies, qualifications or authorizations.
  acceptance_criteria: Assignment to a NOT_ELIGIBLE person is rejected; CONDITIONALLY_ELIGIBLE requires the stated condition.
  source: BRL-007
  priority: must
  verification_method: test
  use_cases:
  - UC-041
  - UC-102
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-008
  capability: CAP-07.03
  pattern: unwanted-behaviour
  statement: If a task's completion criteria are not all met, then the system shall reject its completion.
  acceptance_criteria: Completion with any unmet criterion is rejected with TASK_CRITERIA_NOT_MET.
  source: BRL-006
  priority: must
  verification_method: test
  use_cases:
  - UC-045
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-009
  capability: CAP-07.03
  pattern: unwanted-behaviour
  statement: If the approver of a task result is also its assignee, then the system shall reject the approval unless tenant
    policy explicitly permits it.
  acceptance_criteria: Self-approval rejected with SEGREGATION_OF_DUTIES under default policy.
  source: W1 Q8; OQ-030
  priority: must
  verification_method: test
  use_cases:
  - UC-044
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-010
  capability: CAP-07.03
  pattern: ubiquitous
  statement: The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reason.
  acceptance_criteria: No task exists without either a plan link or an ad-hoc reason and owner.
  source: OUT-05
  priority: must
  verification_method: test
  use_cases:
  - UC-040
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-011
  capability: CAP-07.03
  pattern: ubiquitous
  statement: The system shall require an idempotency key and the expected version on every state-changing command, and shall
    reject commands whose expected version is stale.
  acceptance_criteria: Duplicate command returns the original result; stale version returns VERSION_CONFLICT with no state
    change.
  source: PRJ§16, §104
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-REL-003
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-012
  capability: CAP-07.03
  pattern: event-driven
  statement: When a task is escalated, the system shall notify the next authority level and keep the task state unchanged.
  acceptance_criteria: Escalation produces a TaskEscalated event and a notification; state is unchanged.
  source: PRJ§55
  priority: must
  verification_method: test
  use_cases:
  - UC-046
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-013
  capability: CAP-07.05
  pattern: ubiquitous
  statement: The system shall record measurements of plan outcomes over time against their targets.
  acceptance_criteria: Outcome measurements are time-series linked to the plan outcome and its metric.
  source: PRJ§62; OUT-05
  priority: must
  verification_method: test
  use_cases:
  - UC-101
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OPS-014
  capability: CAP-07.04
  pattern: ubiquitous
  statement: The system shall allow each tenant to configure review and approval steps for plans and tasks within the limits
    of the state machines.
  acceptance_criteria: A tenant can add a second review step without changing code; configurations are versioned.
  source: PRJ§7.13
  priority: should
  verification_method: test
  use_cases:
  - UC-034
  - UC-044
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-RDY-001
  capability: CAP-08.04
  pattern: ubiquitous
  statement: The system shall record each person's competencies, qualifications and certifications with their validity periods.
  acceptance_criteria: Expired certifications are reported as expired at any query time after expiry.
  source: PRJ§64
  priority: must
  verification_method: test
  use_cases:
  - UC-102
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-RDY-002
  capability: CAP-08.04
  pattern: event-driven
  statement: When eligibility is checked for a person, role or task at a given time, the system shall return ELIGIBLE, CONDITIONALLY_ELIGIBLE,
    NOT_ELIGIBLE, EXPIRED, REQUIRES_SUPERVISION, REQUIRES_TRAINING, REQUIRES_CERTIFICATION or UNKNOWN, with reasons.
  acceptance_criteria: Eligibility results match an oracle table of 40 cases.
  source: PRJ§64
  priority: must
  verification_method: test
  use_cases:
  - UC-102
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-COM-001
  capability: CAP-10.01
  pattern: event-driven
  statement: When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authorized
    recipients according to their preferences.
  acceptance_criteria: Recipients receive in-app notification; mobile push is delivered when the device is reachable.
  source: PRJ§7.11
  priority: must
  verification_method: test
  use_cases:
  - UC-099
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-COM-002
  capability: CAP-10.01
  pattern: ubiquitous
  statement: The system shall not include classified content in mobile push payloads and shall limit notification content
    to the recipient's authorization.
  acceptance_criteria: Push payloads contain only a reference and a non-sensitive title; content is fetched after authorization.
  source: A21
  priority: must
  verification_method: test
  use_cases:
  - UC-099
  quality:
  - QAS-SEC-002
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OFF-001
  capability: CAP-02.03
  pattern: optional-feature
  statement: Where the mobile field application is used, the system shall allow recording observations with location, time
    and photos, and updating the status of assigned tasks, without connectivity for at least 72 hours.
  acceptance_criteria: A device offline for 72 hours records 500 observations and 100 task updates and synchronizes them all.
  source: W1 Q9
  priority: must
  verification_method: test
  use_cases:
  - UC-090
  quality:
  - QAS-OFF-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OFF-002
  capability: CAP-02.03
  pattern: ubiquitous
  statement: The system shall let field users preload authorized area-of-interest data, which shall respect the user's authorization
    at download time and expire according to tenant policy.
  acceptance_criteria: Preloaded data excludes unauthorized objects; expired data becomes unreadable on the device.
  source: W1 Q9
  priority: must
  verification_method: test
  use_cases:
  - UC-090
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OFF-003
  capability: CAP-02.03
  pattern: event-driven
  statement: When a device reconnects, the system shall receive the device's recorded commands in their original order with
    device times, and shall assign record time on receipt.
  acceptance_criteria: Device time is stored as observation time; record time equals server receipt time.
  source: ADR-P09; ADR-P01
  priority: must
  verification_method: test
  use_cases:
  - UC-091
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OFF-004
  capability: CAP-02.03
  pattern: unwanted-behaviour
  statement: If a synchronized command conflicts with the current server state, then the system shall route it to conflict
    review and shall not apply last-write-wins to T1 or T2 data.
  acceptance_criteria: 0 silent overwrites in the concurrent-edit sync test; all conflicts appear for review.
  source: PRJ§110; ADR-P09
  priority: must
  verification_method: test
  use_cases:
  - UC-092
  quality:
  - QAS-OFF-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OFF-005
  capability: CAP-02.03
  pattern: ubiquitous
  statement: The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device.
  acceptance_criteria: Device data is unreadable without user authentication; remote wipe completes on next connection.
  source: W1 Q9
  priority: must
  verification_method: test
  use_cases:
  - UC-093
  quality:
  - QAS-SEC-007
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-OFF-006
  capability: CAP-02.03
  pattern: event-driven
  statement: When a synchronization is interrupted, the system shall resume it without duplicating commands.
  acceptance_criteria: Interrupting sync at random points 100 times produces no duplicates.
  source: Idempotency
  priority: must
  verification_method: test
  use_cases:
  - UC-091
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SRC-001
  capability: CAP-03.01
  pattern: ubiquitous
  statement: The system shall provide unified search across entities, observations, documents, assessments, plans and tasks,
    with text, spatial and temporal filters.
  acceptance_criteria: A single query can combine text, a polygon and a time window across all listed types.
  source: PRJ§21
  priority: must
  verification_method: test
  use_cases:
  - UC-097
  quality:
  - QAS-PERF-003
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SRC-002
  capability: CAP-03.01
  pattern: ubiquitous
  statement: The system shall not reveal the existence of unauthorized objects through search results, counts, facets, suggestions,
    ordering, errors or response timing.
  acceptance_criteria: Inference test suite detects 0 leakage.
  source: BRL-010; A21
  priority: must
  verification_method: test
  use_cases:
  - UC-097
  quality:
  - QAS-SEC-002
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SRC-003
  capability: CAP-03.01
  pattern: ubiquitous
  statement: The system shall match Arabic text regardless of hamza forms, alef maqsura, taa marbuta, diacritics and tatweel,
    and shall match names across Arabic and Latin transliterations.
  acceptance_criteria: Arabic search test set reaches the recall target in QAS-USA-002.
  source: W1 Q15; ADR-P15
  priority: must
  verification_method: test
  use_cases:
  - UC-097
  quality:
  - QAS-USA-002
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-SRC-004
  capability: CAP-03.01
  pattern: ubiquitous
  statement: The system shall be able to rebuild every search and graph projection from the source of truth without data loss.
  acceptance_criteria: Dropping and rebuilding the index yields identical query results on the reference set.
  source: PRJ§21; V5 A07
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-REL-002
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-001
  capability: CAP-14.02
  pattern: ubiquitous
  statement: The system shall install, upgrade and operate in an air-gapped environment with no dependency on external network
    services.
  acceptance_criteria: Full install and upgrade succeed from an offline bundle in an isolated network.
  source: W1 Q20
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-OPS-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-002
  capability: CAP-14.03
  pattern: ubiquitous
  statement: The system shall use the same release artifacts for shared, dedicated and sovereign deployments.
  acceptance_criteria: The three deployment modes pass the same acceptance suite from one release.
  source: W1 Q6
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-003
  capability: CAP-14.01
  pattern: ubiquitous
  statement: The system shall emit metrics, logs and traces carrying a correlation id across every component, plus business
    telemetry for the outcome measures.
  acceptance_criteria: Any request can be traced end to end by its correlation id.
  source: PRJ§26; V5§39
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-OBS-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-004
  capability: CAP-14.02
  pattern: ubiquitous
  statement: The system shall assign every capability to one of the service tiers defined in QAS-AVL-001..003 (critical, important,
    standard) and meet that tier's availability, RPO and RTO.
  acceptance_criteria: Tier assignment exists for 100% of R1 capabilities; DR drills meet tier targets.
  source: W1 Q21
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-AVL-001
  - QAS-AVL-002
  - QAS-AVL-003
  - QAS-REC-001
  - QAS-REC-002
  - QAS-REC-003
  release: R1
  status: APPROVED_DELEGATED
  note: '''important'' here is the defined name of a service tier (W1 Q21), not an ambiguous qualifier.'
- id: REQ-PLT-005
  capability: CAP-14.02
  pattern: ubiquitous
  statement: The system shall run heavy operations (raster processing, bulk import, analysis runs, reconstruction, report
    generation) as asynchronous jobs with status, retry and cancellation.
  acceptance_criteria: No synchronous API call performs a listed heavy operation.
  source: SR-06; PRJ§72
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-006
  capability: CAP-14.02
  pattern: ubiquitous
  statement: The system shall publish domain events through a transactional outbox and shall process received events idempotently
    through an inbox.
  acceptance_criteria: State change and event are committed atomically; duplicated deliveries have no second effect.
  source: PRJ§33–34
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-REL-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-007
  capability: CAP-14.02
  pattern: ubiquitous
  statement: The system shall version every API and event contract and shall introduce breaking changes only as a new major
    version that coexists with the previous one.
  acceptance_criteria: Contract tests fail the build on any unversioned breaking change.
  source: PRJ§20, §97
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-EVO-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-008
  capability: CAP-14.02
  pattern: ubiquitous
  statement: The system shall use cursor-based pagination for every list API.
  acceptance_criteria: No list endpoint accepts offset pagination.
  source: SR-12
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-009
  capability: CAP-14.02
  pattern: ubiquitous
  statement: The system shall return errors in the standard error model with code, message, details, correlation id, retryable
    flag and policy reason where applicable.
  acceptance_criteria: All error responses in the API suite conform to the schema.
  source: PRJ§19
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-010
  capability: CAP-14.01
  pattern: ubiquitous
  statement: The system shall provide its user interfaces in Arabic and English with right-to-left and left-to-right layouts,
    and optional Hijri date display.
  acceptance_criteria: All R1 screens pass bilingual and RTL review.
  source: W1 Q15
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-ACC-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-011
  capability: CAP-14.01
  pattern: ubiquitous
  statement: The system shall provide a responsive web application and a mobile field application.
  acceptance_criteria: R1 web screens work from 360 px to desktop width; field functions run on the mobile app.
  source: W1 Q10
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-012
  capability: CAP-14.02
  pattern: ubiquitous
  statement: The system shall back up all stores according to their service tier and shall verify restores automatically.
  acceptance_criteria: Scheduled restore tests succeed and meet the tier RTO.
  source: PRJ§114
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-REC-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-PLT-013
  capability: CAP-14.03
  pattern: ubiquitous
  statement: The system shall compute resource consumption and cost per tenant from telemetry.
  acceptance_criteria: A monthly per-tenant cost report is produced from telemetry alone.
  source: W1 Q29
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-COST-001
  release: R1
  status: APPROVED_DELEGATED
- id: REQ-RES-001
  capability: CAP-08.01
  pattern: ubiquitous
  statement: The system shall register each asset with type, ownership, custody holder, status, condition, location, capabilities,
    certifications and maintenance schedule.
  acceptance_criteria: An asset can be registered with all listed attributes; status and condition are versioned.
  source: PRJ§63 Asset; DOM-14
  priority: must
  verification_method: test
  use_cases:
  - UC-050
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-002
  capability: CAP-08.01
  pattern: event-driven
  statement: When custody of an asset is transferred, the system shall record the previous holder, the new holder, the time
    and the authorization, keeping a gapless custody chain.
  acceptance_criteria: Custody history is complete; a transfer by a non-holder without authority is rejected.
  source: DOM-14 Custody
  priority: must
  verification_method: test
  use_cases:
  - UC-053
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-003
  capability: CAP-08.01
  pattern: event-driven
  statement: When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavailable
    for new assignments from that moment.
  acceptance_criteria: Assignment of an expired or unserviceable asset is rejected with the reason.
  source: PRJ§63 Certification/Condition; BRL-007
  priority: must
  verification_method: test
  use_cases:
  - UC-051
  - UC-053
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-004
  capability: CAP-08.01
  pattern: ubiquitous
  statement: The system shall schedule and record maintenance for assets, and shall mark an asset under maintenance as unavailable
    for the maintenance window.
  acceptance_criteria: Availability queries exclude maintenance windows.
  source: DOM-14 Maintenance
  priority: must
  verification_method: test
  use_cases:
  - UC-051
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-005
  capability: CAP-08.01
  pattern: ubiquitous
  statement: The system shall keep asset location as bitemporal claims so that the location of an asset at any past time is
    retrievable.
  acceptance_criteria: Asset position history is available through the claims kernel.
  source: ADR-P01; REQ-INF-030
  priority: must
  verification_method: test
  use_cases:
  - UC-050
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-006
  capability: CAP-08.02
  pattern: ubiquitous
  statement: The system shall manage resource pools with type, quantity, unit, capacity and availability over time.
  acceptance_criteria: A pool's available quantity at time t equals capacity minus commitments valid at t.
  source: PRJ§63 Resource; DOM-15
  priority: must
  verification_method: test
  use_cases:
  - UC-054
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-007
  capability: CAP-08.02
  pattern: event-driven
  statement: When a resource allocation is requested, the system shall verify authorization, type, availability, capacity,
    time window, geography, priority, existing commitments and policy before committing it.
  acceptance_criteria: Each failing check returns its own reason code; a successful allocation creates a commitment.
  source: PRJ§63 Allocation Domain Service
  priority: must
  verification_method: test
  use_cases:
  - UC-054
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-008
  capability: CAP-08.02
  pattern: unwanted-behaviour
  statement: If two allocation requests compete for the same capacity, then the system shall commit at most the available
    capacity and shall resolve the contention by priority, then by request time.
  acceptance_criteria: No over-commitment under concurrent requests; losers receive CAPACITY_UNAVAILABLE with the competing
    priority.
  source: DOM-15 Capacity
  priority: must
  verification_method: test
  use_cases:
  - UC-054
  quality:
  - QAS-RES-001
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-009
  capability: CAP-08.02
  pattern: event-driven
  statement: When a higher-priority allocation needs capacity already committed at lower priority, the system shall require
    an authorized pre-emption decision and notify the affected owners.
  acceptance_criteria: Pre-emption without authority is rejected; affected tasks are notified.
  source: DOM-15 Priority; BRL-003
  priority: must
  verification_method: test
  use_cases:
  - UC-054
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-010
  capability: CAP-08.02
  pattern: ubiquitous
  statement: The system shall record resource consumption against allocations with quantity, unit and time.
  acceptance_criteria: Consumption above the allocation is flagged for review.
  source: DOM-15 Consumption
  priority: must
  verification_method: test
  use_cases:
  - UC-055
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-011
  capability: CAP-08.02
  pattern: event-driven
  statement: When a task linked to an allocation reaches a terminal state, the system shall release the unused allocation.
  acceptance_criteria: Released quantity becomes available immediately.
  source: SLC-03 events; DEBT-001
  priority: must
  verification_method: test
  use_cases:
  - UC-054
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-012
  capability: CAP-08.02
  pattern: ubiquitous
  statement: The system shall link resources and assets to tasks as structured references, replacing the text-only resource
    notes of R1.
  acceptance_criteria: R1 resource notes are migrated to references or kept as notes with a migration report.
  source: DEBT-001
  priority: must
  verification_method: test
  use_cases:
  - UC-053
  - UC-054
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-013
  capability: CAP-08.04
  pattern: ubiquitous
  statement: The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications,
    certifications, recent training, experience and authorization.
  acceptance_criteria: Readiness results match an oracle table of 60 cases.
  source: PRJ§64
  priority: must
  verification_method: test
  use_cases:
  - UC-102
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-001
  capability: CAP-12.01
  pattern: ubiquitous
  statement: The system shall process every AI request through identity, policy, authorized retrieval, context package, model,
    output, grounding and confidence, and shall record each step.
  acceptance_criteria: Every AI result has a request, context package, model version and lineage record.
  source: PRJ§25–28
  priority: must
  verification_method: test
  use_cases:
  - UC-070
  - UC-071
  - UC-072
  quality:
  - QAS-AI-003
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-002
  capability: CAP-12.01
  pattern: ubiquitous
  statement: The system shall build context packages only from data retrieved with the requesting user's authorization, including
    vector retrieval.
  acceptance_criteria: 'AI inference suite: 0 retrieved items outside the user''s authorization.'
  source: BRL-008; ADR-P06
  priority: must
  verification_method: test
  use_cases:
  - UC-071
  quality:
  - QAS-AI-004
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-003
  capability: CAP-12.01
  pattern: unwanted-behaviour
  statement: If the retrieved evidence is insufficient to answer, then the system shall return 'Insufficient Evidence' instead
    of generating an answer.
  acceptance_criteria: On the insufficient-evidence test set, ≥ 95 % of responses are 'Insufficient Evidence'.
  source: PRJ§112
  priority: must
  verification_method: test
  use_cases:
  - UC-072
  quality:
  - QAS-AI-002
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-004
  capability: CAP-12.01
  pattern: ubiquitous
  statement: The system shall attach to every AI statement the citations (claim, evidence, source, context reference) that
    support it.
  acceptance_criteria: Citation accuracy on the evaluation set meets QAS-AI-001.
  source: PRJ§112
  priority: must
  verification_method: test
  use_cases:
  - UC-072
  quality:
  - QAS-AI-001
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-005
  capability: CAP-12.02
  pattern: ubiquitous
  statement: The system shall label every AI-generated draft as AI output and shall prevent its publication without human
    review.
  acceptance_criteria: Publishing an unreviewed AI draft is rejected.
  source: AI-OP-02/03; BRL-009
  priority: must
  verification_method: test
  use_cases:
  - UC-073
  - UC-074
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-006
  capability: CAP-12.03
  pattern: event-driven
  statement: When AI extracts entities, locations or dates from a document, the system shall create proposed claims whose
    source is the document and whose agent is the model, pending human acceptance.
  acceptance_criteria: Extracted claims are not ASSERTED until accepted; lineage names the model version.
  source: AI-OP-04
  priority: must
  verification_method: test
  use_cases:
  - UC-072
  - UC-073
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-007
  capability: CAP-12.03
  pattern: ubiquitous
  statement: The system shall translate between Arabic and English on request without replacing the original text.
  acceptance_criteria: Original text is always retained; translations are linked and labelled as machine translation.
  source: AI-OP-05; W1 Q26
  priority: must
  verification_method: test
  use_cases:
  - UC-072
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-008
  capability: CAP-12.01
  pattern: ubiquitous
  statement: The system shall enforce the AI autonomy matrix, allowing at most AIL3 in R2 and forbidding AIL5.
  acceptance_criteria: Any AI operation above its matrix level is rejected; forbidden operations are unreachable.
  source: 10-ai/autonomy-matrix; HAP-06
  priority: must
  verification_method: test
  use_cases:
  - UC-074
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-009
  capability: CAP-12.04
  pattern: ubiquitous
  statement: The system shall manage models through the lifecycle REGISTERED, EVALUATING, APPROVED, STAGED, PRODUCTION, MONITORED,
    DEPRECATED, RETIRED.
  acceptance_criteria: A model not in PRODUCTION cannot serve production requests.
  source: PRJ§30
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-010
  capability: CAP-12.04
  pattern: event-driven
  statement: When a model version is proposed for production, the system shall require evaluation results for groundedness,
    citation accuracy, hallucination rate, latency and cost, and human approval.
  acceptance_criteria: Promotion without an approved evaluation report is rejected.
  source: PRJ§31
  priority: must
  verification_method: test
  use_cases: []
  quality:
  - QAS-AI-001
  - QAS-AI-002
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-011
  capability: CAP-12.01
  pattern: ubiquitous
  statement: The system shall run all models on local infrastructure by default and shall use external models only where a
    tenant policy allows it and only for unclassified data.
  acceptance_criteria: Egress to external model endpoints occurs only under an active tenant policy and only with unclassified
    context.
  source: W1 Q20, Q28
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-012
  capability: CAP-12.01
  pattern: unwanted-behaviour
  statement: If content retrieved into a context package contains instructions, then the system shall treat it as data and
    shall not let it change tools, permissions or recipients.
  acceptance_criteria: 'Indirect prompt-injection test suite: 0 successful tool or permission changes.'
  source: PRJ§111; THR-013
  priority: must
  verification_method: test
  use_cases:
  - UC-071
  quality:
  - QAS-AI-004
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-013
  capability: CAP-12.01
  pattern: ubiquitous
  statement: The system shall register every tool available to AI runs, with the permission it requires and its autonomy level.
  acceptance_criteria: An AI run cannot call an unregistered tool.
  source: DOM-23 AI Tool Registry
  priority: must
  verification_method: test
  use_cases: []
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-AI-014
  capability: CAP-12.01
  pattern: ubiquitous
  statement: The system shall maintain a vector projection of authorized content with the same security labels and pre-filtering
    as search.
  acceptance_criteria: Vector retrieval satisfies the non-inference properties P-51..P-53.
  source: ADR-P06; CR-11
  priority: must
  verification_method: test
  use_cases:
  - UC-071
  quality:
  - QAS-AI-004
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-PRD-001
  capability: CAP-10.02
  pattern: ubiquitous
  statement: The system shall produce reports, briefings, map products and analytical products from versioned templates with
    sections, data, evidence, citations, maps and charts.
  acceptance_criteria: A product can be generated from a template and every data element traces to its source version.
  source: PRJ§65 Product; DOM-20
  priority: must
  verification_method: test
  use_cases:
  - UC-110
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-PRD-002
  capability: CAP-10.02
  pattern: ubiquitous
  statement: The system shall set a product's label to at least the highest label of its content and shall render only content
    visible to the product's approved audience.
  acceptance_criteria: A product never contains content above its label.
  source: ADR-P06; LABEL-DERIVATION
  priority: must
  verification_method: test
  use_cases:
  - UC-110
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-PRD-003
  capability: CAP-10.02
  pattern: event-driven
  statement: When a product is approved, the system shall freeze its content as an immutable version with its citations pinned.
  acceptance_criteria: Edits after approval create a new version.
  source: PRJ§65 Review/Approval
  priority: must
  verification_method: test
  use_cases:
  - UC-111
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-PRD-004
  capability: CAP-10.02
  pattern: event-driven
  statement: When a product is distributed, the system shall deliver it only to recipients authorized for its label and shall
    record each distribution.
  acceptance_criteria: Distribution to an unauthorized recipient is rejected; distribution log complete.
  source: PRJ§65 Distribution
  priority: must
  verification_method: test
  use_cases:
  - UC-112
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-PRD-005
  capability: CAP-10.02
  pattern: ubiquitous
  statement: The system shall export approved products as PDF and as documents with a watermark identifying the recipient.
  acceptance_criteria: Exported files carry recipient watermark and product version.
  source: POL-EXPORT-BULK; THR (leakage)
  priority: must
  verification_method: test
  use_cases:
  - UC-112
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-KNW-001
  capability: CAP-11.01
  pattern: ubiquitous
  statement: The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims with
    evidence, relationships, versions, review, approval and publication.
  acceptance_criteria: A knowledge object cannot be published without review and approval.
  source: PRJ§65 KnowledgeObject; DOM-21
  priority: must
  verification_method: test
  use_cases:
  - UC-060
  - UC-061
  - UC-062
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-KNW-002
  capability: CAP-11.01
  pattern: event-driven
  statement: When a task, plan, incident, or exercise simulation is closed or completed, the system shall allow capturing lessons linked to it and to its evidence.
  acceptance_criteria: Lessons link to the closed or completed object and its evidence (task, plan, incident, or a completed exercise simulation — CR-63).
  source: VS06; OUT-06
  priority: must
  verification_method: test
  use_cases:
  - UC-060
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-KNW-003
  capability: CAP-11.01
  pattern: event-driven
  statement: When a published knowledge object is relevant to a new plan or task type, the system shall suggest it to the
    planner.
  acceptance_criteria: Suggestions are based on declared relationships; reuse is recorded (OUT-06).
  source: VS06 Reuse
  priority: should
  verification_method: test
  use_cases:
  - UC-062
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-ARC-001
  capability: CAP-11.03
  pattern: ubiquitous
  statement: The system shall transfer records reaching the ARCHIVE disposition action into archive packages containing content,
    metadata, provenance, integrity hashes and access history.
  acceptance_criteria: Archive packages validate against the package schema and their hashes.
  source: PRJ§65 ArchiveRecord; SLC-12a
  priority: must
  verification_method: test
  use_cases:
  - UC-063
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-ARC-002
  capability: CAP-11.03
  pattern: ubiquitous
  statement: The system shall preserve archive packages in preservation formats and verify their integrity periodically.
  acceptance_criteria: Integrity verification runs on all packages at least yearly with 0 unreported failures.
  source: PRJ§65 Preservation/Integrity
  priority: must
  verification_method: test
  use_cases:
  - UC-063
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-ARC-003
  capability: CAP-11.03
  pattern: event-driven
  statement: When an authorized user requests a historical record, the system shall retrieve it within the archive retrieval
    target and audit the access.
  acceptance_criteria: Retrieval meets QAS-ARC-001; access history updated.
  source: DOM-22 Historical Retrieval
  priority: must
  verification_method: test
  use_cases:
  - UC-064
  quality:
  - QAS-ARC-001
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-ARC-004
  capability: CAP-11.03
  pattern: event-driven
  statement: When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the state
    from versions, events, valid time, effective time and provenance, labelling each element RECORDED, RECONSTRUCTED, INFERRED
    or UNKNOWN.
  acceptance_criteria: Reconstruction of the reference scenarios matches the oracle; every element is labelled.
  source: PRJ§103; CR-25
  priority: must
  verification_method: test
  use_cases:
  - UC-065
  quality:
  - QAS-ARC-002
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-COL-001
  capability: CAP-02.01
  pattern: ubiquitous
  statement: The system shall record information needs as collection requirements with question, area, time window, priority,
    requester and due date.
  acceptance_criteria: A collection requirement cannot be approved without area, window and priority.
  source: DOM-05; BP01–BP02
  priority: must
  verification_method: test
  use_cases:
  - UC-120
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-COL-002
  capability: CAP-02.01
  pattern: event-driven
  statement: When a collection requirement is approved, the system shall allow planning collection activities with methods,
    sources and assigned field tasks.
  acceptance_criteria: Collection activities create tasks through SLC-03 and link back to the requirement.
  source: BP03–BP04
  priority: must
  verification_method: test
  use_cases:
  - UC-121
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-COL-003
  capability: CAP-02.01
  pattern: event-driven
  statement: When observations answering a collection requirement are validated, the system shall update the requirement's
    fulfilment status.
  acceptance_criteria: Fulfilment shows answered, partially answered or open with linked observations.
  source: VS01
  priority: must
  verification_method: test
  use_cases:
  - UC-122
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-CRD-001
  capability: CAP-06.03
  pattern: ubiquitous
  statement: The system shall manage coordination cases linking decisions, plans and organizations that must act together,
    with participants, responsibilities and status.
  acceptance_criteria: Each participant sees only the parts of the case they are authorized for.
  source: DOM-10 Coordination Case
  priority: must
  verification_method: test
  use_cases:
  - UC-130
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-CRD-002
  capability: CAP-06.03
  pattern: event-driven
  statement: When a coordination action requires another organization's authority, the system shall route it for that authority's
    decision and record the outcome.
  acceptance_criteria: Cross-organization actions are not executed without the other authority's recorded decision.
  source: BRL-003
  priority: must
  verification_method: test
  use_cases:
  - UC-131
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-FUS-001
  capability: CAP-04.04
  pattern: ubiquitous
  statement: The system shall correlate observations and claims across sources in space and time into correlation proposals
    with method, score and evidence.
  acceptance_criteria: Correlation proposals never change claims; acceptance creates relationships or ER cases.
  source: DOM-07 Correlation/Fusion
  priority: must
  verification_method: test
  use_cases:
  - UC-132
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-FUS-002
  capability: CAP-04.04
  pattern: ubiquitous
  statement: The system shall record for each fused result the contributing sources and their reliabilities.
  acceptance_criteria: Fused results trace to every contributing source (lineage).
  source: PRJ§23
  priority: must
  verification_method: test
  use_cases:
  - UC-132
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-INT-001
  capability: CAP-02.04
  pattern: ubiquitous
  statement: The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims,
    persons and documents without making external systems sources of truth.
  acceptance_criteria: Each integration has an ACTIVE adapter, mapping tests and lineage; conflicting values create conflicts,
    not overwrites.
  source: W1 Q24; BRL-013
  priority: must
  verification_method: test
  use_cases:
  - UC-094
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-INT-002
  capability: CAP-02.04
  pattern: ubiquitous
  statement: The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a.
  acceptance_criteria: Sensor ingestion meets QAS-PERF-012.
  source: W1 Q11
  priority: must
  verification_method: test
  use_cases:
  - UC-094
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-INT-003
  capability: CAP-10.01
  pattern: optional-feature
  statement: Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2).
  acceptance_criteria: Alerts export and import as valid CAP 1.2 messages.
  source: W1 Q25
  priority: should
  verification_method: test
  use_cases:
  - UC-023
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-INT-004
  capability: CAP-01.02
  pattern: event-driven
  statement: When HRIS reports a change of role or organization for a person, the system shall propose the corresponding role-assignment
    change for administrator approval.
  acceptance_criteria: No role changes are applied automatically from HRIS.
  source: SLC-01 THR-S01-01
  priority: must
  verification_method: test
  use_cases:
  - UC-084
  quality: []
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RES-014
  capability: CAP-08.01
  pattern: event-driven
  statement: When an asset is reserved for a time window, the system shall reject any other reservation or assignment of that
    asset overlapping the window.
  acceptance_criteria: Overlapping reservations are rejected with ASSET_RESERVED and the holder reference.
  source: DOM-14; UC-052
  priority: must
  verification_method: test
  use_cases:
  - UC-052
  quality:
  - QAS-RES-001
  release: R2
  status: APPROVED_DELEGATED
- id: REQ-RCM-001
  capability: CAP-09.01
  pattern: ubiquitous
  statement: The system shall allow an authorized actor to identify a risk with a hazard category, description, and at least one scope reference (asset, area, organization or plan).
  acceptance_criteria: A risk can be created with all listed attributes; category_ref resolves against the tenant's hazard category catalog (RD-HAZARD-CATEGORIES).
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-002
  capability: CAP-09.01
  pattern: ubiquitous
  statement: The system shall require a likelihood and an impact rating (1-5) to assess a risk, and shall compute the risk score itself rather than accept it as input.
  acceptance_criteria: risk_score is always likelihood x impact; a request that supplies risk_score directly is rejected or ignored.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-003
  capability: CAP-09.01
  pattern: constraint
  statement: Where tenant policy requires segregation of duties, the system shall reject a risk assessment or reassessment performed by the same actor who identified the risk.
  acceptance_criteria: Assessment by the identifying actor is rejected with SEGREGATION_OF_DUTIES when the policy is enabled.
  source: DOM-17; mirrors INV-TASK-07
  priority: should
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-004
  capability: CAP-09.01
  pattern: constraint
  statement: The system shall require at least one treatment action for a risk moving to treated status, unless the chosen strategy is 'accept' with an authorized approver recorded.
  acceptance_criteria: Planning treatment with strategy other than accept and zero treatment actions is rejected with TREATMENT_INVALID.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-005
  capability: CAP-09.01
  pattern: constraint
  statement: The system shall require an explicit rationale to close a risk, and shall provide no command to reopen a closed risk.
  acceptance_criteria: Close without rationale is rejected with RATIONALE_REQUIRED; no reopen operation exists in the API.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-006
  capability: CAP-09.02
  pattern: ubiquitous
  statement: The system shall allow any authorized actor to report an incident with a hazard category, description, at least one scope reference, and a default severity of MINOR.
  acceptance_criteria: An incident can be reported with all listed attributes; severity defaults to MINOR when not stated.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-007
  capability: CAP-09.02
  pattern: ubiquitous
  statement: The system shall require an authorized assessor to set an incident's severity to one of MINOR, MAJOR, EMERGENCY or CRISIS before a response can be dispatched.
  acceptance_criteria: Dispatching a response before assessment is rejected with the aggregate's invalid-state-transition error.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-008
  capability: CAP-09.02
  pattern: ubiquitous
  statement: The system shall require a commander and at least one linked response task before an incident moves to responding status.
  acceptance_criteria: Dispatch without a commander or without at least one response_task_ref is rejected with RESPONSE_REQUIRED.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-009
  capability: CAP-09.02
  pattern: event-driven
  statement: When an incident's severity is escalated, the system shall accept only a value higher than the current severity, and shall change severity downward only through a distinct, separately-authorized de-escalation command.
  acceptance_criteria: An escalate command with a severity not higher than current is rejected with SEVERITY_MUST_INCREASE; severity never decreases except via CMD-INC-DE-ESCALATE.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-010
  capability: CAP-09.02
  pattern: constraint
  statement: The system shall reject closing an incident while any of its linked response tasks is not in a terminal state.
  acceptance_criteria: Close is rejected with RESPONSE_TASKS_OPEN while a linked task remains non-terminal.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-011
  capability: CAP-09.03
  pattern: constraint
  statement: The system shall never activate a contingency plan automatically as a side effect of a severity escalation; activation shall always be a distinct, separately-authorized command.
  acceptance_criteria: Escalating an incident's severity alone never creates or links a Plan; only CMD-INC-ACTIVATE-CONTINGENCY does, and it requires its own authorization.
  source: DOM-17; anti-pattern lesson from SLC-09 (Silent Pre-emption)
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-012
  capability: CAP-09.02
  pattern: constraint
  statement: When an incident references a risk as materialized, the system shall not change that risk's state automatically; the risk owner acts on it through a separate command.
  acceptance_criteria: Creating, escalating or closing an incident with a risk_ref never changes the referenced risk's state or version.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-013
  capability: CAP-09.02
  pattern: ubiquitous
  statement: The system shall allow a response task to be created directly under an incident (incident_ref) without requiring a plan.
  acceptance_criteria: CMD-TASK-CREATE with incident_ref and without plan_ref or ad_hoc_reason succeeds (CR-61).
  source: DOM-17; CR-61
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-014
  capability: CAP-09.01
  pattern: ubiquitous
  statement: The system shall let an authorized actor list and filter the risk register by category, scope and score, restricted to the caller's visible scope.
  acceptance_criteria: Risks outside the caller's allowed_scope never appear in the list or count.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-015
  capability: CAP-09.02
  pattern: ubiquitous
  statement: The system shall let an authorized actor list and filter incidents by category, severity, status and scope, restricted to the caller's visible scope.
  acceptance_criteria: Incidents outside the caller's allowed_scope never appear in the list or count.
  source: DOM-17
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-RCM-016
  capability: CAP-09.03
  pattern: ubiquitous
  statement: The system shall compute an incident's recovery status from its linked contingency plan's task completion against the incident's start time, as an estimate, without a separate recovery state machine.
  acceptance_criteria: Recovery status is a read query over existing Plan/Task data (SLC-08/SLC-03); no new aggregate stores recovery state (R3-Q2, R3-Q4 reuse decisions).
  source: DOM-17; R3-Q2; R3-Q4
  priority: should
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-001
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall allow an authorized actor to request a quantity of a logistics item to a destination, and shall issue a matching resource allocation request against the item's pool in the same unit of work.
  acceptance_criteria: Creating a logistics request always creates exactly one linked allocation (target = the request, CR-62); no logistics request exists without one.
  source: DOM-16
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-002
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall track logistics item inventory as a Resource Pool (SLC-09) rather than a separate stock model, and shall commit a logistics request's quantity through the existing allocation checks and capacity ledger, unchanged.
  acceptance_criteria: No logistics-specific capacity table or reservation engine exists; SPEC-ALLOCATION §1/§2 apply to logistics requests exactly as to any other allocation (R3-Q3).
  source: DOM-16; R3-Q3
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-003
  capability: CAP-08.03
  pattern: ubiquitous
  statement: A logistics request's approval routing shall exactly follow its linked allocation's approval outcome; no separate approval step exists at the request level.
  acceptance_criteria: A logistics request reaches APPROVED, PENDING_APPROVAL or REJECTED only as a system-driven consequence of the linked allocation's own EVT-ALC-COMMITTED / -APPROVAL-REQUIRED / -REJECTED events, never through a request-level approval command.
  source: DOM-16
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-004
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall allow dispatch of an approved logistics request only while its linked allocation remains COMMITTED, creating a Shipment for a quantity not exceeding the request.
  acceptance_criteria: CMD-LGR-DISPATCH is rejected with ALLOCATION_NOT_COMMITTED if the linked allocation is no longer COMMITTED; the created Shipment's planned_quantity never exceeds the requested quantity.
  source: DOM-16
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-005
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall record a shipment's movement as an append-only, chronologically ordered checkpoint history.
  acceptance_criteria: CMD-SHP-RECORD-CHECKPOINT is rejected with CHECKPOINT_INVALID if the new checkpoint's time is not strictly after the previous one; no command edits or removes an existing checkpoint.
  source: DOM-16
  priority: should
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-006
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall record the quantity actually delivered at receipt, distinct from the quantity planned, and shall never mark a logistics request fulfilled when the delivered quantity is less than requested.
  acceptance_criteria: delivered_quantity is a required field on CMD-SHP-DELIVER; the linked logistics request reaches FULFILLED only when delivered_quantity equals the requested quantity, otherwise PARTIALLY_FULFILLED.
  source: DOM-16
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-007
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall allow reporting a shipment as damaged or lost in transit, recording the reason and, for damage, the affected quantity.
  acceptance_criteria: CMD-SHP-REPORT-DAMAGE requires a reason and a damaged_quantity not exceeding the planned quantity; CMD-SHP-REPORT-LOST requires a reason.
  source: DOM-16
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-008
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall record consumption on a logistics request's linked allocation only from a confirmed shipment outcome (delivered, damaged, or lost), never speculatively at dispatch.
  acceptance_criteria: No CMD-ALC-RECORD-CONSUMPTION is issued for a logistics-linked allocation before the linked Shipment reaches DELIVERED, DAMAGED or LOST.
  source: DOM-16
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-009
  capability: CAP-08.03
  pattern: constraint
  statement: The system shall allow cancelling a logistics request before dispatch, releasing its linked allocation, and shall allow cancelling a shipment only before departure.
  acceptance_criteria: CMD-LGR-CANCEL is accepted from REQUESTED, PENDING_APPROVAL or APPROVED only; CMD-SHP-CANCEL is accepted from PLANNED only, rejected once IN_TRANSIT.
  source: DOM-16
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-010
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall let an authorized actor list and filter logistics requests by item, destination, state and priority, restricted to the caller's visible scope.
  acceptance_criteria: Logistics requests outside the caller's allowed_scope never appear in the list or count.
  source: DOM-16
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-011
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall let an authorized actor list and filter shipments by logistics request, carrier, state and window, restricted to the caller's visible scope.
  acceptance_criteria: Shipments outside the caller's allowed_scope never appear in the list or count.
  source: DOM-16
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-012
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall provide the full, ordered checkpoint history of a shipment to an authorized actor.
  acceptance_criteria: QRY-SHP-TRACKING returns every recorded checkpoint for a shipment in chronological order.
  source: DOM-16
  priority: should
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-013
  capability: CAP-08.03
  pattern: ubiquitous
  statement: The system shall resolve a logistics item's identity against a per-tenant reference catalog (RD-LOGISTICS-ITEM-TYPES) rather than a fixed list, consistent with the existing resource-type/asset-type pattern.
  acceptance_criteria: No logistics item type is hard-coded in the domain model; item_pool resolves to a resource_type value from the tenant's catalog.
  source: DOM-16; R2-Q1
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-LOG-014
  capability: CAP-08.03
  pattern: constraint
  statement: Contention among logistics requests for the same pool shall be resolved exactly as SLC-09 resolves allocation contention (priority then request time within the pool's ordering window); no separate logistics-specific ordering rule shall be introduced.
  acceptance_criteria: No logistics-specific contention or ordering logic exists outside SPEC-ALLOCATION §2.
  source: DOM-16; R3-Q3
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-001
  capability: CAP-08.05
  pattern: ubiquitous
  statement: The system shall allow defining a training scenario with a situation narrative, target competencies and an ordered set of injects, under a versioned DRAFT → ACTIVE → RETIRED lifecycle with segregation of duties on activation.
  acceptance_criteria: CMD-SCN-ACTIVATE is rejected with SEGREGATION_OF_DUTIES when the approver equals the author; injects are rejected unless strictly ordered by offset (INV-SCN-01).
  source: DOM-19; R3-Q4
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-002
  capability: CAP-08.05
  pattern: constraint
  statement: Editing an ACTIVE scenario shall create a new version; an exercise already planned against a prior version shall keep its frozen reference unaffected.
  acceptance_criteria: After CMD-SCN-EDIT on an ACTIVE scenario, an exercise planned earlier still reports its original scenario_version_frozen.
  source: DOM-19; R3-Q4
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-003
  capability: CAP-08.05
  pattern: constraint
  statement: An exercise shall be planned only against a scenario that is ACTIVE at that instant; the scenario reference shall be frozen for the life of the exercise.
  acceptance_criteria: CMD-EXR-PLAN referencing a DRAFT or RETIRED scenario is rejected with EXERCISE_INVALID.
  source: DOM-19; R3-Q4
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-004
  capability: CAP-08.05
  pattern: ubiquitous
  statement: An exercise shall be scheduled with a valid time window, a location and confirmed participants before it can start.
  acceptance_criteria: CMD-EXR-START is rejected unless the exercise is SCHEDULED with window.from < window.to.
  source: DOM-19; R3-Q4
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-005
  capability: CAP-08.05
  pattern: event-driven
  statement: Starting a scheduled exercise shall create exactly one linked simulation run, in the same unit of work.
  acceptance_criteria: After CMD-EXR-START, exactly one Simulation exists referencing the exercise and its frozen scenario, created in the same transaction as EVT-EXR-STARTED.
  source: DOM-19; R3-Q4
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-006
  capability: CAP-08.05
  pattern: constraint
  statement: An exercise's terminal outcome (COMPLETED or ABORTED) shall be driven exclusively by its linked simulation's own outcome; no direct human command shall set either state.
  acceptance_criteria: No command exists whose guard transitions an Exercise directly to COMPLETED or ABORTED; both are reachable only via the SYS: rows of the state × command matrix.
  source: DOM-19; R3-Q4
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-007
  capability: CAP-08.05
  pattern: constraint
  statement: An exercise shall be cancellable with a reason before it starts, and never once it is in progress.
  acceptance_criteria: CMD-EXR-CANCEL succeeds from PLANNED or SCHEDULED only; rejected with EXERCISE_INVALID_STATE_TRANSITION from IN_PROGRESS.
  source: DOM-19; R3-Q4
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-008
  capability: CAP-08.05
  pattern: constraint
  statement: A simulation run shall record inject deliveries as an append-only, strictly time-ordered log.
  acceptance_criteria: CMD-SIM-DELIVER-INJECT is rejected with INJECT_INVALID unless delivered_at is strictly after the previous delivery for that simulation (INV-SIM-01); no edit or delete command exists for a delivered inject.
  source: DOM-19; R3-Q4
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-009
  capability: CAP-08.05
  pattern: constraint
  statement: A simulation run shall record a per-participant, per-competency evaluation, always by an evaluator distinct from the participant being evaluated.
  acceptance_criteria: CMD-SIM-RECORD-EVALUATION is rejected with SEGREGATION_OF_DUTIES when evaluator equals participant (INV-SIM-03).
  source: DOM-19; R3-Q4
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-010
  capability: CAP-08.05
  pattern: constraint
  statement: A simulation run shall reach COMPLETED only when every participant listed on its linked exercise has at least one recorded evaluation.
  acceptance_criteria: CMD-SIM-COMPLETE is rejected with EVALUATION_MISSING while any exercise participant has zero recorded evaluations (INV-SIM-02).
  source: DOM-19; R3-Q4
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-011
  capability: CAP-08.05
  pattern: ubiquitous
  statement: A simulation run shall be pausable and resumable, or abortable with a reason, without losing any previously recorded inject-delivery or evaluation history.
  acceptance_criteria: CMD-SIM-PAUSE/CMD-SIM-RESUME/CMD-SIM-ABORT never remove or alter a prior InjectDelivery or Evaluation record.
  source: DOM-19; R3-Q4
  priority: should
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-012
  capability: CAP-08.05
  pattern: ubiquitous
  statement: A person's qualification record shall be able to cite a completed simulation run as evidence, using the existing, unmodified Qualification Record evidence reference — no schema change to SLC-03.
  acceptance_criteria: CMD-QUAL-RECORD/CMD-QUAL-RENEW accept a completed simulation's URN in their existing evidence:urn field without any change to AGG-QUALIFICATION-RECORD's guard or payload schema.
  source: DOM-18; R3-Q4
  priority: should
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-013
  capability: CAP-08.05
  pattern: event-driven
  statement: A completed simulation run shall be usable as the terminal source of an After Action Review, captured as a lesson-type Knowledge Object in BC06.
  acceptance_criteria: CMD-KNO-DRAFT with knowledge_type=lesson accepts a completed Simulation's URN as source (CR-63), with no payload schema change to AGG-KNOWLEDGE-OBJECT.
  source: DOM-19; R3-Q5; CR-63
  priority: should
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-014
  capability: CAP-08.05
  pattern: ubiquitous
  statement: The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted to the caller's visible scope.
  acceptance_criteria: Scenarios, exercises and simulations outside the caller's allowed_scope never appear in a list or count.
  source: DOM-18; DOM-19
  priority: must
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
- id: REQ-TRX-015
  capability: CAP-08.05
  pattern: ubiquitous
  statement: The system shall provide the full, ordered timeline of inject deliveries and evaluations for a simulation run to an authorized actor.
  acceptance_criteria: QRY-SIM-TIMELINE returns every recorded inject delivery and evaluation for a simulation in chronological order.
  source: DOM-19
  priority: should
  verification_method: test
  use_cases: —
  quality: —
  release: R3
  status: APPROVED_DELEGATED
```

</details>
