---
id: AD-03-REQUIREMENTS-ANALYSIS
type: requirements-analysis
title: "تحليل المتطلبات — الوظيفية وسيناريوهات الجودة والأولويات"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 3)"
sources: [02-requirements/requirements.md, 02-requirements/quality-scenarios.md, 01-business/capabilities.md, 01-business/outcomes.md, 15-traceability/quality-verification-matrix.md, 15-traceability/trace-*.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# تحليل المتطلبات

المتطلبات الوظيفية (210) وسيناريوهات الجودة (95) مرتبة حسب القدرة والخاصية، مع ما يحققها في التصميم وفجوات التغطية. نص كل متطلب في `02-requirements/requirements.md` هو المرجع، والجداول هنا تختصره.

## 1. طريقة القراءة

| العمود | المعنى |
|---|---|
| النمط | نمط صياغة EARS في المصدر: ubiquitous (دائم)، event-driven (عند حدث)، unwanted-behaviour (سلوك غير مرغوب)، constraint (قيد)، optional-feature (ميزة اختيارية) |
| الأولوية | MoSCoW في المصدر: must / should |
| الـAggregates | من `traces.satisfies` في ملفات الـAggregates — التحقيق في المجال؛ «— (§3.4)» = يتحقق بغير Aggregate |
| QAS | سيناريو الجودة المرتبط بالمتطلب في المصدر |
| يتحقق عبر (§3.4) | عناصر التصميم من ملفات التتبع لمتطلبات لا يحققها Aggregate (مكتبات مشتركة، استعلامات، قيود منصة) |

## 2. ملاحظات التحليل

1. **الأولوية.** 198 من 210 متطلبًا `must`؛ الـ12 `should` موزعة على CAP-08 (6) وCAP-09 (2) وCAP-04 وCAP-07 وCAP-10 وCAP-11 (واحد لكل منها). التمييز الفعلي بين المتطلبات هو **الإصدار** (R1: 114، R2: 51، R3: 45) وترتيب السنة الأولى للنتائج (OUT-02 ثم OUT-04 ثم OUT-05 — `01-business/system-definition.md` §3).
2. **القدرة الأكبر** CAP-08 (الموارد والجاهزية، 45 متطلبًا) وأغلبها R3؛ R1 يتركز في CAP-01..07 وCAP-13..14.
3. **التحقق.** كل المتطلبات طريقة تحققها `test`؛ الاختبار المقابل في ملفات القبول (`13-verification/acceptance/`) ودوال اللياقة وملفات التتبع.
4. **متطلبات بلا Aggregate** ليست بالضرورة فجوة: قيود المنصة (CAP-14) والأمن تتحقق بالبنية ودوال اللياقة، والمتطلبات القرائية تتحقق باستعلامات. §3.4 يسرد لكل منها ما يحققه.
5. **سيناريوهات الجودة** مصدر محركات المعمارية. §3.5 يسرد سيناريوهات الأولوية `H/H` (أهمية/صعوبة)؛ أما ترتيب المحركات في `10-architecture-overview.md` فمن شجرة المنفعة في `16-reports/ARCHITECTURE-REVIEW-R1.md`، ويشمل سيناريوهات بأولوية أدنى (مثل QAS-EVO-001).

## 3. الكتالوج والتحليل

<!-- BEGIN GENERATED: build_analysis_design.py -->

### 3.1 المتطلبات الوظيفية حسب القدرة

| القدرة | الاسم | المتطلبات | R1 | R2 | R3 | must | should | بلا Aggregate | بلا حالة استخدام |
|---|---|---|---|---|---|---|---|---|---|
| CAP-01 | إدارة المؤسسة والوصول | 15 | 14 | 1 | 0 | 15 | 0 | 2 | 2 |
| CAP-02 | جمع المعلومات | 20 | 15 | 5 | 0 | 20 | 0 | 0 | 0 |
| CAP-03 | إدارة المعلومات | 22 | 22 | 0 | 0 | 22 | 0 | 6 | 9 |
| CAP-04 | التحليل والتقييم | 10 | 8 | 2 | 0 | 9 | 1 | 0 | 1 |
| CAP-05 | الوعي بالموقف | 7 | 7 | 0 | 0 | 7 | 0 | 1 | 1 |
| CAP-06 | إدارة القرار | 6 | 4 | 2 | 0 | 6 | 0 | 0 | 0 |
| CAP-07 | التخطيط والتنفيذ | 14 | 14 | 0 | 0 | 13 | 1 | 0 | 1 |
| CAP-08 | الموارد والجاهزية | 45 | 2 | 14 | 29 | 39 | 6 | 7 | 0 |
| CAP-09 | المخاطر والطوارئ | 16 | 0 | 0 | 16 | 14 | 2 | 3 | 0 |
| CAP-10 | الاتصال والمنتجات | 8 | 2 | 6 | 0 | 7 | 1 | 0 | 0 |
| CAP-11 | المعرفة والذاكرة المؤسسية | 9 | 2 | 7 | 0 | 8 | 1 | 0 | 0 |
| CAP-12 | المساعدة بالذكاء الاصطناعي | 14 | 0 | 14 | 0 | 14 | 0 | 1 | 0 |
| CAP-13 | الحوكمة والأمن والامتثال | 10 | 10 | 0 | 0 | 10 | 0 | 4 | 2 |
| CAP-14 | تشغيل المنصة | 14 | 14 | 0 | 0 | 14 | 0 | 13 | 13 |
| **المجموع** | | **210** | 114 | 51 | 45 | 198 | 12 | 37 | 29 |

**أنماط الصياغة (EARS):** ubiquitous: 131، event-driven: 49، constraint: 15، unwanted-behaviour: 12، optional-feature: 3. **طريقة التحقق:** test: 210.

### 3.2 من النتائج إلى القدرات إلى المتطلبات

حقل `contributing_requirements` في النتائج ما زال TBD (CR-30)، فالربط هنا مشتق عبر حقل `outcomes` في كل قدرة **[Derived]**. القدرة الواحدة قد تخدم أكثر من نتيجة، فالأعداد متداخلة ولا يساوي مجموعها 210؛ وقدرات بلا نتيجة: CAP-14 (14 متطلبًا).

| النتيجة | الاسم | أولوية السنة الأولى | القدرات | المتطلبات عبرها |
|---|---|---|---|---|
| OUT-01 | وضوح المعلومات (Information Visibility) | secondary | CAP-02, CAP-03, CAP-12 | 56 |
| OUT-02 | الفهم السياقي (Contextual Understanding) | 1 | CAP-03, CAP-05, CAP-09 | 45 |
| OUT-03 | الفهم التحليلي (Analytical Understanding) | secondary | CAP-04, CAP-12 | 24 |
| OUT-04 | دعم القرار (Decision Support) | 2 | CAP-01, CAP-06, CAP-10, CAP-13 | 39 |
| OUT-05 | التنفيذ المنسق (Coordinated Execution) | 3 | CAP-07, CAP-08, CAP-09 | 75 |
| OUT-06 | التعلم المؤسسي (Institutional Learning) | secondary | CAP-11 | 9 |

### 3.3 المتطلبات حسب القدرة

#### CAP-01 — إدارة المؤسسة والوصول

القدرات الفرعية: CAP-01.01 إدارة المستأجرين والمؤسسات (R1)، CAP-01.02 الهوية والمصادقة والاتحاد (R1)، CAP-01.03 السلطة والتفويض (R1)، CAP-01.04 سياسات الوصول (R1)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-FND-001 | The system shall isolate each tenant's data, policies, configuration, projections, files, events and audit records from every other tenant. | ubiquitous | must | R1 | UC-080 | AGG-TENANT | QAS-SEC-001 |
| REQ-FND-002 | The system shall allow a tenant to contain one or more organizations, each with a hierarchy of organizational units of unlimited depth. | ubiquitous | must | R1 | UC-081 | AGG-ORGANIZATION | — |
| REQ-FND-003 | When a tenant is provisioned, the system shall create its isolation boundary, classification scheme, default roles, quotas and audit stream before any user of… | event-driven | must | R1 | UC-080 | AGG-TENANT | QAS-SCAL-003 |
| REQ-FND-004 | Where a tenant is designated dedicated or sovereign, the system shall run that tenant in its own cell with no data store shared with other tenants. | optional-feature | must | R1 | UC-080 | AGG-TENANT | — |
| REQ-FND-005 | The system shall authenticate human users only through a configured external identity provider using OIDC or SAML, and shall support account provisioning throu… | ubiquitous | must | R1 | UC-084 | AGG-USER | — |
| REQ-FND-006 | The system shall maintain Person, Identity, User and Service Account as separate records with explicit links. | ubiquitous | must | R1 | UC-084 | AGG-PERSON, AGG-SERVICE-ACCOUNT, AGG-USER | — |
| REQ-FND-007 | The system shall record authority as a grant stating decision type, organizational scope, limits and validity period, held by a role or a person. | ubiquitous | must | R1 | UC-082 | AGG-AUTHORITY-GRANT | — |
| REQ-FND-008 | When an authority holder delegates authority, the system shall record delegator, delegate, scope, limits and validity period, and shall reject any delegation e… | event-driven | must | R1 | UC-083 | AGG-AUTHORITY-GRANT | — |
| REQ-FND-009 | The system shall provide an authority check returning whether an actor holds authority for a given decision type, scope and point in time, including through de… | ubiquitous | must | R1 | UC-032, UC-035 | AGG-AUTHORITY-GRANT | — |
| REQ-FND-010 | The system shall evaluate authorization before retrieving data for every command, query, search, map request, export, event subscription and AI retrieval. | ubiquitous | must | R1 | **—** | — (§3.4) | QAS-SEC-002 |
| REQ-FND-011 | The system shall base authorization decisions on subject, action, resource, purpose, context, classification, compartments and jurisdiction. | ubiquitous | must | R1 | UC-086 | AGG-ROLE-ASSIGNMENT, AGG-POLICY-SET | — |
| REQ-FND-012 | The system shall return a policy decision of ALLOW, DENY, CONDITIONAL, REDACT, AGGREGATE or REQUIRE_APPROVAL, with any obligations, and shall enforce the oblig… | ubiquitous | must | R1 | UC-086 | AGG-POLICY-SET | — |
| REQ-FND-013 | If the policy decision point is unavailable or returns an error, then the system shall deny the request. | unwanted-behaviour | must | R1 | **—** | — (§3.4) | QAS-SEC-005 |
| REQ-FND-014 | The system shall treat View, Edit, Export, Share, Approve, Delete, Retain and Archive as separately grantable permissions. | ubiquitous | must | R1 | UC-086 | AGG-ROLE | — |
| REQ-INT-004 | When HRIS reports a change of role or organization for a person, the system shall propose the corresponding role-assignment change for administrator approval. | event-driven | must | R2 | UC-084 | AGG-HR-SYNC-PROPOSAL | — |

#### CAP-02 — جمع المعلومات

القدرات الفرعية: CAP-02.01 الحاجة المعلوماتية وتخطيط الجمع (R2)، CAP-02.02 إدارة المصادر (R1)، CAP-02.03 تسجيل الملاحظات (بما فيها دون اتصال) (R1)، CAP-02.04 الاستيعاب والتكامل (R1)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-COL-001 | The system shall record information needs as collection requirements with question, area, time window, priority, requester and due date. | ubiquitous | must | R2 | UC-120 | AGG-COLLECTION-REQUIREMENT | — |
| REQ-COL-002 | When a collection requirement is approved, the system shall allow planning collection activities with methods, sources and assigned field tasks. | event-driven | must | R2 | UC-121 | AGG-COLLECTION-PLAN | — |
| REQ-COL-003 | When observations answering a collection requirement are validated, the system shall update the requirement's fulfilment status. | event-driven | must | R2 | UC-122 | AGG-COLLECTION-REQUIREMENT | — |
| REQ-INF-001 | The system shall register each source with type, owner, classification and a reliability rating, and keep the history of reliability changes. | ubiquitous | must | R1 | UC-004, UC-095 | AGG-SOURCE | — |
| REQ-INF-002 | When an observation is recorded, the system shall store its observation time, its event time where known, its record time, its location with CRS and positional… | event-driven | must | R1 | UC-005 | AGG-OBSERVATION | — |
| REQ-INF-003 | The system shall store attachments (documents, images, video, raster) in object storage and reference them by content hash. | ubiquitous | must | R1 | UC-005, UC-006 | AGG-ATTACHMENT, AGG-EVIDENCE | — |
| REQ-INF-004 | When an attachment is stored or retrieved, the system shall compute or verify its content hash. | event-driven | must | R1 | UC-006 | AGG-ATTACHMENT, AGG-EVIDENCE | — |
| REQ-INF-005 | The system shall ingest external data only through registered adapters or bulk import jobs that record source, batch, transformation and lineage. | ubiquitous | must | R1 | UC-094 | AGG-IMPORT-BATCH, AGG-ADAPTER | — |
| REQ-INF-006 | If an ingested record fails validation, then the system shall quarantine it with the failure reason and shall not publish it. | unwanted-behaviour | must | R1 | UC-094 | AGG-IMPORT-BATCH | QAS-DQ-001 |
| REQ-INF-007 | When an ingestion batch is re-submitted, the system shall not create duplicate records. | event-driven | must | R1 | UC-094 | AGG-IMPORT-BATCH | — |
| REQ-INF-008 | The system shall import geospatial data via OGC API Features/Maps/Tiles, WMS/WFS, GeoJSON, GeoPackage, GeoTIFF/COG and KML. | ubiquitous | must | R1 | UC-094 | AGG-IMPORT-BATCH, AGG-ADAPTER | — |
| REQ-INF-009 | The system shall ingest weather data through an adapter and register the provider as a source. | ubiquitous | must | R1 | UC-094 | AGG-IMPORT-BATCH, AGG-ADAPTER | — |
| REQ-INT-001 | The system shall integrate ERP, HRIS and DMS through registered adapters that map external records to claims, persons and documents without making external sys… | ubiquitous | must | R2 | UC-094 | AGG-INTEGRATION-CONNECTION | — |
| REQ-INT-002 | The system shall ingest sensor streams through adapters into observations at the design rates of WL-06a. | ubiquitous | must | R2 | UC-094 | AGG-SENSOR-STREAM | — |
| REQ-OFF-001 | Where the mobile field application is used, the system shall allow recording observations with location, time and photos, and updating the status of assigned t… | optional-feature | must | R1 | UC-090 | AGG-TASK, AGG-SYNC-SESSION | QAS-OFF-001 |
| REQ-OFF-002 | The system shall let field users preload authorized area-of-interest data, which shall respect the user's authorization at download time and expire according t… | ubiquitous | must | R1 | UC-090 | AGG-PRELOAD-PACKAGE | — |
| REQ-OFF-003 | When a device reconnects, the system shall receive the device's recorded commands in their original order with device times, and shall assign record time on re… | event-driven | must | R1 | UC-091 | AGG-SYNC-SESSION | — |
| REQ-OFF-004 | If a synchronized command conflicts with the current server state, then the system shall route it to conflict review and shall not apply last-write-wins to T1… | unwanted-behaviour | must | R1 | UC-092 | AGG-SYNC-CONFLICT, AGG-SYNC-SESSION | QAS-OFF-001 |
| REQ-OFF-005 | The system shall encrypt all data stored on field devices and shall support remote wipe of a lost device. | ubiquitous | must | R1 | UC-093 | AGG-DEVICE, AGG-PRELOAD-PACKAGE | QAS-SEC-007 |
| REQ-OFF-006 | When a synchronization is interrupted, the system shall resume it without duplicating commands. | event-driven | must | R1 | UC-091 | AGG-SYNC-SESSION | — |

#### CAP-03 — إدارة المعلومات

القدرات الفرعية: CAP-03.01 الكيانات والعلاقات (R1)، CAP-03.02 الادعاءات والأدلة (R1)، CAP-03.03 المعلومات الجغرافية (R1)، CAP-03.04 الزمن والتاريخ (R1)، CAP-03.05 مطابقة الكيانات (R1)، CAP-03.06 إدارة التعارض (R1)، CAP-03.07 المنشأ والثقة (R1)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-INF-020 | The system shall represent Entity, Event, Relationship, Claim, Evidence, Source and Observation as distinct object types. | ubiquitous | must | R1 | UC-001, UC-002, UC-003 | AGG-ENTITY, AGG-REALWORLD-EVENT | — |
| REQ-INF-021 | The system shall represent each attribute value of an importance-tier T1 object as a claim linked to its sources, evidence and confidence. | ubiquitous | must | R1 | UC-006 | AGG-CLAIM, AGG-ENTITY, AGG-EVIDENCE-LINK | — |
| REQ-INF-022 | The system shall record a valid-time interval and a record-time interval for every T1 claim. | ubiquitous | must | R1 | **—** | AGG-CLAIM | — |
| REQ-INF-023 | When a query specifies a valid time T, a record time K, or both, the system shall return the state valid at T as known at K, using the current time for any tim… | event-driven | must | R1 | UC-096 | — (§3.4) | QAS-TMP-001 |
| REQ-INF-024 | The system shall never overwrite a T1 claim; a correction shall close the record-time interval of the previous claim and create a new claim. | ubiquitous | must | R1 | **—** | AGG-CLAIM, AGG-CONFLICT | — |
| REQ-INF-025 | When two claims about the same subject and attribute overlap in valid time with incompatible values, the system shall open a conflict case and retain both clai… | event-driven | must | R1 | UC-008 | AGG-CONFLICT | — |
| REQ-INF-026 | The system shall expose confidence as separate dimensions: source reliability, information confidence, data quality, verification status, freshness, completene… | ubiquitous | must | R1 | **—** | AGG-CLAIM | — |
| REQ-INF-027 | The system shall represent relationships as objects with type, source, target, validity period, evidence, provenance, confidence and classification. | ubiquitous | must | R1 | UC-003 | AGG-RELATIONSHIP | — |
| REQ-INF-028 | The system shall require every geometry to carry a CRS and a positional accuracy, and shall reject invalid geometries. | ubiquitous | must | R1 | **—** | AGG-OBSERVATION | QAS-DQ-001 |
| REQ-INF-029 | The system shall store each geometry in the canonical CRS WGS 84 (EPSG:4326) and shall keep the original CRS and coordinates. | ubiquitous | must | R1 | **—** | — (§3.4) | — |
| REQ-INF-030 | The system shall keep the position history of located entities over time. | ubiquitous | must | R1 | UC-096 | — (§3.4) | — |
| REQ-INF-031 | The system shall store names in their original form and in normalized and transliterated forms for Arabic and English. | ubiquitous | must | R1 | **—** | — (§3.4) | QAS-USA-002 |
| REQ-INF-032 | When an entity-resolution candidate is detected, the system shall create a resolution case with candidates, method, features, score and evidence, and shall not… | event-driven | must | R1 | UC-007 | AGG-ER-CASE, AGG-MATCH-RULESET | — |
| REQ-INF-033 | When entities are matched, the system shall record a same-as link with the decision, reviewer and time, keep all original identifiers valid, and resolve any me… | event-driven | must | R1 | UC-007 | AGG-ER-CASE | — |
| REQ-INF-034 | When a match is reversed, the system shall close the same-as link so that each original entity again resolves to exactly its own claims. | event-driven | must | R1 | UC-104 | AGG-ER-CASE | — |
| REQ-INF-035 | The system shall record lineage for every derived object: inputs and their versions, the transformation and its version, the actor and the execution time. | ubiquitous | must | R1 | **—** | AGG-ANALYSIS-RUN, AGG-FINDING | QAS-TRC-001 |
| REQ-INF-036 | The system shall identify every object by an internal ULID and a global URN of the form urn:<namespace>:<type>:<id>, and shall map external identifiers per sou… | ubiquitous | must | R1 | **—** | AGG-ENTITY, AGG-EXTERNAL-ID | — |
| REQ-INF-037 | If a T1 object is submitted without a source reference, then the system shall reject it. | unwanted-behaviour | must | R1 | **—** | AGG-CLAIM | — |
| REQ-SRC-001 | The system shall provide unified search across entities, observations, documents, assessments, plans and tasks, with text, spatial and temporal filters. | ubiquitous | must | R1 | UC-097 | — (§3.4) | QAS-PERF-003 |
| REQ-SRC-002 | The system shall not reveal the existence of unauthorized objects through search results, counts, facets, suggestions, ordering, errors or response timing. | ubiquitous | must | R1 | UC-097 | — (§3.4) | QAS-SEC-002 |
| REQ-SRC-003 | The system shall match Arabic text regardless of hamza forms, alef maqsura, taa marbuta, diacritics and tatweel, and shall match names across Arabic and Latin… | ubiquitous | must | R1 | UC-097 | AGG-MATCH-RULESET | QAS-USA-002 |
| REQ-SRC-004 | The system shall be able to rebuild every search and graph projection from the source of truth without data loss. | ubiquitous | must | R1 | UC-078 | AGG-PROJECTION-VERSION | QAS-REL-002 |

#### CAP-04 — التحليل والتقييم

القدرات الفرعية: CAP-04.01 حالات التحليل (R1)، CAP-04.02 التنفيذ وإعادة الإنتاج (R1)، CAP-04.03 إنتاج التقييم (R1)، CAP-04.04 الدمج والربط (R2)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-ANL-001 | The system shall record for each analysis case its question, spatial and temporal scope, hypotheses, assumptions and evidence references. | ubiquitous | must | R1 | UC-010, UC-011, UC-012 | AGG-ANALYSIS-CASE | — |
| REQ-ANL-002 | When an analysis run is executed, the system shall record the dataset versions, parameters, algorithm and version, layers, filters, time and spatial extent, as… | event-driven | must | R1 | UC-013 | AGG-ANALYSIS-METHOD, AGG-ANALYSIS-RUN | — |
| REQ-ANL-003 | When a recorded analysis run is re-executed with the same recorded inputs, the system shall produce the same results or report which inputs differ. | event-driven | must | R1 | UC-013 | AGG-ANALYSIS-METHOD, AGG-ANALYSIS-RUN | QAS-TRC-002 |
| REQ-ANL-004 | The system shall execute long-running analysis runs as asynchronous jobs with status, progress, cancellation and retry. | ubiquitous | must | R1 | UC-013 | AGG-ANALYSIS-RUN | — |
| REQ-ANL-005 | The system shall record for each assessment its findings, evidence, assumptions, uncertainty, confidence, methodology, limitations, reviewer and version. | ubiquitous | must | R1 | UC-015, UC-014 | AGG-ASSESSMENT, AGG-FINDING | — |
| REQ-ANL-006 | When an assessment is published, the system shall make that version immutable; later changes shall create a new version. | event-driven | must | R1 | UC-015 | AGG-ASSESSMENT | — |
| REQ-ANL-007 | The system shall allow comparison of alternative scenarios within an analysis case. | ubiquitous | should | R1 | UC-016 | AGG-ANALYSIS-CASE | — |
| REQ-ANL-008 | If an assessment references evidence the reader is not authorized to view, then the system shall withhold that evidence according to policy and shall indicate… | unwanted-behaviour | must | R1 | **—** | AGG-ASSESSMENT | QAS-SEC-002 |
| REQ-FUS-001 | The system shall correlate observations and claims across sources in space and time into correlation proposals with method, score and evidence. | ubiquitous | must | R2 | UC-132 | AGG-CORRELATION-PROPOSAL, AGG-CORRELATION-RULE | — |
| REQ-FUS-002 | The system shall record for each fused result the contributing sources and their reliabilities. | ubiquitous | must | R2 | UC-132 | AGG-CORRELATION-PROPOSAL | — |

#### CAP-05 — الوعي بالموقف

القدرات الفرعية: CAP-05.01 تعريف الموقف (R1)، CAP-05.02 المراقبة والتنبيه (R1)، CAP-05.03 صورة العمليات المشتركة (الخرائط) (R1)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-SIT-001 | The system shall define each situation by geographic extent, time window, inclusion criteria, owner and classification. | ubiquitous | must | R1 | UC-020 | AGG-SITUATION | — |
| REQ-SIT-002 | When an object matching a situation's criteria is created or changed, the system shall update the situation membership and record a situation change. | event-driven | must | R1 | UC-021, UC-022 | AGG-SITUATION | QAS-PERF-006 |
| REQ-SIT-003 | The system shall present each situation as a map-based common operational picture of its entities, events, risks, tasks, resources, assessments and alerts. | ubiquitous | must | R1 | UC-024, UC-098 | AGG-SITUATION | — |
| REQ-SIT-004 | When an alert rule condition is met, the system shall raise an alert and notify subscribed authorized users. | event-driven | must | R1 | UC-023 | AGG-ALERT-RULE, AGG-ALERT | QAS-PERF-005 |
| REQ-SIT-005 | The system shall manage alerts through the states RAISED, ACKNOWLEDGED, RESOLVED and DISMISSED, requiring a reason for dismissal, and shall audit every transit… | ubiquitous | must | R1 | UC-023 | AGG-ALERT | — |
| REQ-SIT-006 | If a user is not authorized for the object that triggered an alert, then the system shall not reveal that object or its existence in the alert shown to that us… | unwanted-behaviour | must | R1 | **—** | AGG-ALERT | QAS-SEC-002 |
| REQ-SIT-007 | The system shall serve map layers filtered by the requesting user's authorization and shall not share cached map tiles across different authorization scopes. | ubiquitous | must | R1 | UC-098 | — (§3.4) | QAS-SEC-004, QAS-PERF-007 |

#### CAP-06 — إدارة القرار

القدرات الفرعية: CAP-06.01 طلبات القرار والخيارات (R1)، CAP-06.02 تسجيل القرار والتحقق من السلطة (R1)، CAP-06.03 التنسيق (R2)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-CRD-001 | The system shall manage coordination cases linking decisions, plans and organizations that must act together, with participants, responsibilities and status. | ubiquitous | must | R2 | UC-130 | AGG-COORDINATION-CASE | — |
| REQ-CRD-002 | When a coordination action requires another organization's authority, the system shall route it for that authority's decision and record the outcome. | event-driven | must | R2 | UC-131 | AGG-COORDINATION-CASE | — |
| REQ-DEC-001 | The system shall record each decision request with its question, options, assessment references, deadline and required authority type. | ubiquitous | must | R1 | UC-030, UC-031 | AGG-DECISION-REQUEST | — |
| REQ-DEC-002 | When a decision is recorded, the system shall verify through the authority check that the decider holds the required authority at the decision time, and shall… | event-driven | must | R1 | UC-032 | AGG-DECISION | — |
| REQ-DEC-003 | The system shall record for each decision the selected option, rationale, authority, approval, effective time and links to the assessments and evidence conside… | ubiquitous | must | R1 | UC-032 | AGG-DECISION | QAS-TRC-001 |
| REQ-DEC-004 | The system shall make a recorded decision immutable; a change shall be recorded as a new decision that supersedes it. | ubiquitous | must | R1 | UC-032 | AGG-DECISION | — |

#### CAP-07 — التخطيط والتنفيذ

القدرات الفرعية: CAP-07.01 الأهداف والتخطيط (R1)، CAP-07.02 إصدارات الخطة وخط الأساس (R1)، CAP-07.03 إدارة المهام (R1)، CAP-07.04 سير العمل (R1)، CAP-07.05 قياس النتائج (R1)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-OPS-001 | The system shall record for each plan its objectives, outcomes, constraints, assumptions, phases, activities, milestones, resources, schedule, dependencies and… | ubiquitous | must | R1 | UC-033 | AGG-PLAN-VERSION, AGG-PLAN | — |
| REQ-OPS-002 | The system shall link every approved plan to the decisions or objectives it implements. | ubiquitous | must | R1 | UC-033, UC-035 | AGG-PLAN | — |
| REQ-OPS-003 | When a plan is approved, the system shall create an immutable baseline of that plan version. | event-driven | must | R1 | UC-035, UC-036 | AGG-PLAN-VERSION, AGG-PLAN | — |
| REQ-OPS-004 | When a major change is made to a baselined plan, the system shall create a new plan version that requires approval before it becomes effective. | event-driven | must | R1 | UC-034, UC-036 | AGG-PLAN-VERSION | — |
| REQ-OPS-005 | If the approver of a plan is also its author, then the system shall reject the approval unless tenant policy explicitly permits it. | unwanted-behaviour | must | R1 | UC-035 | AGG-ROLE-ASSIGNMENT, AGG-PLAN-VERSION | — |
| REQ-OPS-006 | The system shall manage task state according to state machine SM-TASK and reject any transition not defined in it. | ubiquitous | must | R1 | UC-040, UC-042, UC-043, UC-044, UC-045 | AGG-TASK | — |
| REQ-OPS-007 | When a task is assigned, the system shall verify the assignee's eligibility wherever the task type declares required competencies, qualifications or authorizat… | event-driven | must | R1 | UC-041, UC-102 | AGG-TASK-TYPE, AGG-TASK | — |
| REQ-OPS-008 | If a task's completion criteria are not all met, then the system shall reject its completion. | unwanted-behaviour | must | R1 | UC-045 | AGG-TASK | — |
| REQ-OPS-009 | If the approver of a task result is also its assignee, then the system shall reject the approval unless tenant policy explicitly permits it. | unwanted-behaviour | must | R1 | UC-044 | AGG-ROLE-ASSIGNMENT, AGG-TASK | — |
| REQ-OPS-010 | The system shall link every task to a plan, or record it as an ad-hoc task with an accountable owner and reason. | ubiquitous | must | R1 | UC-040 | AGG-TASK | — |
| REQ-OPS-011 | The system shall require an idempotency key and the expected version on every state-changing command, and shall reject commands whose expected version is stale. | ubiquitous | must | R1 | **—** | AGG-TASK | QAS-REL-003 |
| REQ-OPS-012 | When a task is escalated, the system shall notify the next authority level and keep the task state unchanged. | event-driven | must | R1 | UC-046 | AGG-TASK | — |
| REQ-OPS-013 | The system shall record measurements of plan outcomes over time against their targets. | ubiquitous | must | R1 | UC-101 | AGG-OUTCOME-TRACKER | — |
| REQ-OPS-014 | The system shall allow each tenant to configure review and approval steps for plans and tasks within the limits of the state machines. | ubiquitous | should | R1 | UC-034, UC-044 | AGG-PLAN-VERSION, AGG-TASK-TYPE | — |

#### CAP-08 — الموارد والجاهزية

القدرات الفرعية: CAP-08.01 إدارة الأصول (R2)، CAP-08.02 تخصيص الموارد (R2)، CAP-08.03 الإمداد (R3)، CAP-08.04 الكفاءة والأهلية (R1 (الأهلية فقط))، CAP-08.05 التدريب والتمارين (R3)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-LOG-001 | The system shall allow an authorized actor to request a quantity of a logistics item to a destination, and shall issue a matching resource allocation request a… | ubiquitous | must | R3 | UC-150 | AGG-LOGISTICS-REQUEST | — |
| REQ-LOG-002 | The system shall track logistics item inventory as a Resource Pool (SLC-09) rather than a separate stock model, and shall commit a logistics request's quantity… | ubiquitous | must | R3 | UC-150 | AGG-LOGISTICS-REQUEST | — |
| REQ-LOG-003 | A logistics request's approval routing shall exactly follow its linked allocation's approval outcome; no separate approval step exists at the request level. | ubiquitous | must | R3 | UC-150 | AGG-LOGISTICS-REQUEST | — |
| REQ-LOG-004 | The system shall allow dispatch of an approved logistics request only while its linked allocation remains COMMITTED, creating a Shipment for a quantity not exc… | ubiquitous | must | R3 | UC-151 | AGG-SHIPMENT | — |
| REQ-LOG-005 | The system shall record a shipment's movement as an append-only, chronologically ordered checkpoint history. | ubiquitous | should | R3 | UC-151 | AGG-SHIPMENT | — |
| REQ-LOG-006 | The system shall record the quantity actually delivered at receipt, distinct from the quantity planned, and shall never mark a logistics request fulfilled when… | ubiquitous | must | R3 | UC-152 | AGG-SHIPMENT | — |
| REQ-LOG-007 | The system shall allow reporting a shipment as damaged or lost in transit, recording the reason and, for damage, the affected quantity. | ubiquitous | must | R3 | UC-152 | AGG-SHIPMENT | — |
| REQ-LOG-008 | The system shall record consumption on a logistics request's linked allocation only from a confirmed shipment outcome (delivered, damaged, or lost), never spec… | ubiquitous | must | R3 | UC-152 | AGG-LOGISTICS-REQUEST | — |
| REQ-LOG-009 | The system shall allow cancelling a logistics request before dispatch, releasing its linked allocation, and shall allow cancelling a shipment only before depar… | constraint | must | R3 | UC-152 | AGG-LOGISTICS-REQUEST, AGG-SHIPMENT | — |
| REQ-LOG-010 | The system shall let an authorized actor list and filter logistics requests by item, destination, state and priority, restricted to the caller's visible scope. | ubiquitous | must | R3 | UC-150 | — (§3.4) | — |
| REQ-LOG-011 | The system shall let an authorized actor list and filter shipments by logistics request, carrier, state and window, restricted to the caller's visible scope. | ubiquitous | must | R3 | UC-151 | — (§3.4) | — |
| REQ-LOG-012 | The system shall provide the full, ordered checkpoint history of a shipment to an authorized actor. | ubiquitous | should | R3 | UC-151 | — (§3.4) | — |
| REQ-LOG-013 | The system shall resolve a logistics item's identity against a per-tenant reference catalog (RD-LOGISTICS-ITEM-TYPES) rather than a fixed list, consistent with… | ubiquitous | must | R3 | UC-150 | AGG-LOGISTICS-REQUEST | — |
| REQ-LOG-014 | Contention among logistics requests for the same pool shall be resolved exactly as SLC-09 resolves allocation contention (priority then request time within the… | constraint | must | R3 | UC-150 | AGG-LOGISTICS-REQUEST | — |
| REQ-RDY-001 | The system shall record each person's competencies, qualifications and certifications with their validity periods. | ubiquitous | must | R1 | UC-102 | AGG-QUALIFICATION-RECORD | — |
| REQ-RDY-002 | When eligibility is checked for a person, role or task at a given time, the system shall return ELIGIBLE, CONDITIONALLY_ELIGIBLE, NOT_ELIGIBLE, EXPIRED, REQUIR… | event-driven | must | R1 | UC-102 | AGG-QUALIFICATION-RECORD | — |
| REQ-RES-001 | The system shall register each asset with type, ownership, custody holder, status, condition, location, capabilities, certifications and maintenance schedule. | ubiquitous | must | R2 | UC-050 | AGG-ASSET | — |
| REQ-RES-002 | When custody of an asset is transferred, the system shall record the previous holder, the new holder, the time and the authorization, keeping a gapless custody… | event-driven | must | R2 | UC-053 | AGG-ASSET | — |
| REQ-RES-003 | When an asset's certification expires or its condition becomes unserviceable, the system shall make it unavailable for new assignments from that moment. | event-driven | must | R2 | UC-051, UC-053 | AGG-ASSET-ASSIGNMENT, AGG-ASSET | — |
| REQ-RES-004 | The system shall schedule and record maintenance for assets, and shall mark an asset under maintenance as unavailable for the maintenance window. | ubiquitous | must | R2 | UC-051 | AGG-MAINTENANCE-ORDER | — |
| REQ-RES-005 | The system shall keep asset location as bitemporal claims so that the location of an asset at any past time is retrievable. | ubiquitous | must | R2 | UC-050 | AGG-ASSET | — |
| REQ-RES-006 | The system shall manage resource pools with type, quantity, unit, capacity and availability over time. | ubiquitous | must | R2 | UC-054 | AGG-RESOURCE-POOL | — |
| REQ-RES-007 | When a resource allocation is requested, the system shall verify authorization, type, availability, capacity, time window, geography, priority, existing commit… | event-driven | must | R2 | UC-054 | AGG-ALLOCATION | — |
| REQ-RES-008 | If two allocation requests compete for the same capacity, then the system shall commit at most the available capacity and shall resolve the contention by prior… | unwanted-behaviour | must | R2 | UC-054 | AGG-ALLOCATION | QAS-RES-001 |
| REQ-RES-009 | When a higher-priority allocation needs capacity already committed at lower priority, the system shall require an authorized pre-emption decision and notify th… | event-driven | must | R2 | UC-054 | AGG-ALLOCATION | — |
| REQ-RES-010 | The system shall record resource consumption against allocations with quantity, unit and time. | ubiquitous | must | R2 | UC-055 | AGG-ALLOCATION | — |
| REQ-RES-011 | When a task linked to an allocation reaches a terminal state, the system shall release the unused allocation. | event-driven | must | R2 | UC-054 | AGG-ALLOCATION | — |
| REQ-RES-012 | The system shall link resources and assets to tasks as structured references, replacing the text-only resource notes of R1. | ubiquitous | must | R2 | UC-053, UC-054 | AGG-ALLOCATION, AGG-ASSET-ASSIGNMENT | — |
| REQ-RES-013 | The system shall evaluate readiness of a person or unit from role requirements, competencies, qualifications, certifications, recent training, experience and a… | ubiquitous | must | R2 | UC-102 | AGG-ROLE-REQUIREMENT | — |
| REQ-RES-014 | When an asset is reserved for a time window, the system shall reject any other reservation or assignment of that asset overlapping the window. | event-driven | must | R2 | UC-052 | AGG-ASSET-RESERVATION | QAS-RES-001 |
| REQ-TRX-001 | The system shall allow defining a training scenario with a situation narrative, target competencies and an ordered set of injects, under a versioned DRAFT → AC… | ubiquitous | must | R3 | UC-160 | AGG-SCENARIO | — |
| REQ-TRX-002 | Editing an ACTIVE scenario shall create a new version; an exercise already planned against a prior version shall keep its frozen reference unaffected. | constraint | must | R3 | UC-160 | AGG-SCENARIO | — |
| REQ-TRX-003 | An exercise shall be planned only against a scenario that is ACTIVE at that instant; the scenario reference shall be frozen for the life of the exercise. | constraint | must | R3 | UC-161 | AGG-EXERCISE | — |
| REQ-TRX-004 | An exercise shall be scheduled with a valid time window, a location and confirmed participants before it can start. | ubiquitous | must | R3 | UC-161 | AGG-EXERCISE | — |
| REQ-TRX-005 | Starting a scheduled exercise shall create exactly one linked simulation run, in the same unit of work. | event-driven | must | R3 | UC-162 | AGG-EXERCISE | — |
| REQ-TRX-006 | An exercise's terminal outcome (COMPLETED or ABORTED) shall be driven exclusively by its linked simulation's own outcome; no direct human command shall set eit… | constraint | must | R3 | UC-162 | AGG-EXERCISE | — |
| REQ-TRX-007 | An exercise shall be cancellable with a reason before it starts, and never once it is in progress. | constraint | must | R3 | UC-161 | AGG-EXERCISE | — |
| REQ-TRX-008 | A simulation run shall record inject deliveries as an append-only, strictly time-ordered log. | constraint | must | R3 | UC-162 | AGG-SIMULATION | — |
| REQ-TRX-009 | A simulation run shall record a per-participant, per-competency evaluation, always by an evaluator distinct from the participant being evaluated. | constraint | must | R3 | UC-162 | AGG-SIMULATION | — |
| REQ-TRX-010 | A simulation run shall reach COMPLETED only when every participant listed on its linked exercise has at least one recorded evaluation. | constraint | must | R3 | UC-162 | AGG-SIMULATION | — |
| REQ-TRX-011 | A simulation run shall be pausable and resumable, or abortable with a reason, without losing any previously recorded inject-delivery or evaluation history. | ubiquitous | should | R3 | UC-162 | AGG-SIMULATION | — |
| REQ-TRX-012 | A person's qualification record shall be able to cite a completed simulation run as evidence, using the existing, unmodified Qualification Record evidence refe… | ubiquitous | should | R3 | UC-163 | — (§3.4) | — |
| REQ-TRX-013 | A completed simulation run shall be usable as the terminal source of an After Action Review, captured as a lesson-type Knowledge Object in BC06. | event-driven | should | R3 | UC-163 | — (§3.4) | — |
| REQ-TRX-014 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted to the caller's visible scope. | ubiquitous | must | R3 | UC-161 | — (§3.4) | — |
| REQ-TRX-015 | The system shall provide the full, ordered timeline of inject deliveries and evaluations for a simulation run to an authorized actor. | ubiquitous | should | R3 | UC-162 | — (§3.4) | — |

#### CAP-09 — المخاطر والطوارئ

القدرات الفرعية: CAP-09.01 إدارة المخاطر (R3)، CAP-09.02 الحوادث والاستجابة (R3)، CAP-09.03 الاستمرارية والتعافي (R3)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-RCM-001 | The system shall allow an authorized actor to identify a risk with a hazard category, description, and at least one scope reference (asset, area, organization… | ubiquitous | must | R3 | UC-140 | AGG-RISK | — |
| REQ-RCM-002 | The system shall require a likelihood and an impact rating (1-5) to assess a risk, and shall compute the risk score itself rather than accept it as input. | ubiquitous | must | R3 | UC-140 | AGG-RISK | — |
| REQ-RCM-003 | Where tenant policy requires segregation of duties, the system shall reject a risk assessment or reassessment performed by the same actor who identified the ri… | constraint | should | R3 | UC-140 | AGG-RISK | — |
| REQ-RCM-004 | The system shall require at least one treatment action for a risk moving to treated status, unless the chosen strategy is 'accept' with an authorized approver… | constraint | must | R3 | UC-141 | AGG-RISK | — |
| REQ-RCM-005 | The system shall require an explicit rationale to close a risk, and shall provide no command to reopen a closed risk. | constraint | must | R3 | UC-141 | AGG-RISK | — |
| REQ-RCM-006 | The system shall allow any authorized actor to report an incident with a hazard category, description, at least one scope reference, and a default severity of… | ubiquitous | must | R3 | UC-142 | AGG-INCIDENT | — |
| REQ-RCM-007 | The system shall require an authorized assessor to set an incident's severity to one of MINOR, MAJOR, EMERGENCY or CRISIS before a response can be dispatched. | ubiquitous | must | R3 | UC-142 | AGG-INCIDENT | — |
| REQ-RCM-008 | The system shall require a commander and at least one linked response task before an incident moves to responding status. | ubiquitous | must | R3 | UC-143 | AGG-INCIDENT | — |
| REQ-RCM-009 | When an incident's severity is escalated, the system shall accept only a value higher than the current severity, and shall change severity downward only throug… | event-driven | must | R3 | UC-143 | AGG-INCIDENT | — |
| REQ-RCM-010 | The system shall reject closing an incident while any of its linked response tasks is not in a terminal state. | constraint | must | R3 | UC-143 | AGG-INCIDENT | — |
| REQ-RCM-011 | The system shall never activate a contingency plan automatically as a side effect of a severity escalation; activation shall always be a distinct, separately-a… | constraint | must | R3 | UC-144 | AGG-INCIDENT | — |
| REQ-RCM-012 | When an incident references a risk as materialized, the system shall not change that risk's state automatically; the risk owner acts on it through a separate c… | constraint | must | R3 | UC-143 | AGG-INCIDENT | — |
| REQ-RCM-013 | The system shall allow a response task to be created directly under an incident (incident_ref) without requiring a plan. | ubiquitous | must | R3 | UC-143 | AGG-INCIDENT | — |
| REQ-RCM-014 | The system shall let an authorized actor list and filter the risk register by category, scope and score, restricted to the caller's visible scope. | ubiquitous | must | R3 | UC-140 | — (§3.4) | — |
| REQ-RCM-015 | The system shall let an authorized actor list and filter incidents by category, severity, status and scope, restricted to the caller's visible scope. | ubiquitous | must | R3 | UC-142 | — (§3.4) | — |
| REQ-RCM-016 | The system shall compute an incident's recovery status from its linked contingency plan's task completion against the incident's start time, as an estimate, wi… | ubiquitous | should | R3 | UC-144 | — (§3.4) | — |

#### CAP-10 — الاتصال والمنتجات

القدرات الفرعية: CAP-10.01 الإشعارات والتوزيع (R1 (إشعارات))، CAP-10.02 التقارير والإحاطات ومنتجات الخرائط (R2)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-COM-001 | When a notifiable event occurs, the system shall deliver a notification in-app and by mobile push to authorized recipients according to their preferences. | event-driven | must | R1 | UC-099 | AGG-NOTIFICATION, AGG-SUBSCRIPTION | — |
| REQ-COM-002 | The system shall not include classified content in mobile push payloads and shall limit notification content to the recipient's authorization. | ubiquitous | must | R1 | UC-099 | AGG-NOTIFICATION | QAS-SEC-002 |
| REQ-INT-003 | Where a tenant enables it, the system shall exchange alerts using the Common Alerting Protocol (CAP 1.2). | optional-feature | should | R2 | UC-023 | AGG-CAP-MESSAGE | — |
| REQ-PRD-001 | The system shall produce reports, briefings, map products and analytical products from versioned templates with sections, data, evidence, citations, maps and c… | ubiquitous | must | R2 | UC-110 | AGG-PRODUCT-TEMPLATE, AGG-PRODUCT | — |
| REQ-PRD-002 | The system shall set a product's label to at least the highest label of its content and shall render only content visible to the product's approved audience. | ubiquitous | must | R2 | UC-110 | AGG-PRODUCT | — |
| REQ-PRD-003 | When a product is approved, the system shall freeze its content as an immutable version with its citations pinned. | event-driven | must | R2 | UC-111 | AGG-PRODUCT | — |
| REQ-PRD-004 | When a product is distributed, the system shall deliver it only to recipients authorized for its label and shall record each distribution. | event-driven | must | R2 | UC-112 | AGG-DISTRIBUTION | — |
| REQ-PRD-005 | The system shall export approved products as PDF and as documents with a watermark identifying the recipient. | ubiquitous | must | R2 | UC-112 | AGG-DISTRIBUTION | — |

#### CAP-11 — المعرفة والذاكرة المؤسسية

القدرات الفرعية: CAP-11.01 الدروس والمعرفة (R2)، CAP-11.02 السجلات والاحتفاظ (R1 (الاحتفاظ والتجميد))، CAP-11.03 الأرشيف وإعادة البناء التاريخي (R2)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-ARC-001 | The system shall transfer records reaching the ARCHIVE disposition action into archive packages containing content, metadata, provenance, integrity hashes and… | ubiquitous | must | R2 | UC-063 | AGG-ARCHIVE-PACKAGE | — |
| REQ-ARC-002 | The system shall preserve archive packages in preservation formats and verify their integrity periodically. | ubiquitous | must | R2 | UC-063 | AGG-ARCHIVE-PACKAGE | — |
| REQ-ARC-003 | When an authorized user requests a historical record, the system shall retrieve it within the archive retrieval target and audit the access. | event-driven | must | R2 | UC-064 | AGG-ARCHIVE-PACKAGE | QAS-ARC-001 |
| REQ-ARC-004 | When a historical reconstruction as of time T known at time K is requested, the system shall rebuild the state from versions, events, valid time, effective tim… | event-driven | must | R2 | UC-065 | AGG-RECONSTRUCTION | QAS-ARC-002 |
| REQ-GOV-006 | The system shall apply a retention schedule to every record class. | ubiquitous | must | R1 | UC-103 | AGG-DISPOSITION-RUN, AGG-RETENTION-SCHEDULE | — |
| REQ-GOV-007 | When a legal hold is placed on a set of records, the system shall prevent their disposition, erasure or modification until the hold is released. | event-driven | must | R1 | UC-103 | AGG-DISPOSITION-RUN, AGG-LEGAL-HOLD | — |
| REQ-KNW-001 | The system shall manage knowledge objects (procedures, lessons, best practices, policy knowledge) as claims with evidence, relationships, versions, review, app… | ubiquitous | must | R2 | UC-060, UC-061, UC-062 | AGG-KNOWLEDGE-OBJECT | — |
| REQ-KNW-002 | When a task, plan, incident, or exercise simulation is closed or completed, the system shall allow capturing lessons linked to it and to its evidence. | event-driven | must | R2 | UC-060 | AGG-KNOWLEDGE-OBJECT | — |
| REQ-KNW-003 | When a published knowledge object is relevant to a new plan or task type, the system shall suggest it to the planner. | event-driven | should | R2 | UC-062 | AGG-KNOWLEDGE-OBJECT | — |

#### CAP-12 — المساعدة بالذكاء الاصطناعي

القدرات الفرعية: CAP-12.01 الاسترجاع والإجابة المؤرّضة (R2)، CAP-12.02 الصياغة والتلخيص (R2)، CAP-12.03 الاستخراج والترجمة (R2)، CAP-12.04 تقييم AI وحوكمته (R2)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-AI-001 | The system shall process every AI request through identity, policy, authorized retrieval, context package, model, output, grounding and confidence, and shall r… | ubiquitous | must | R2 | UC-070, UC-071, UC-072 | AGG-AI-REQUEST | QAS-AI-003 |
| REQ-AI-002 | The system shall build context packages only from data retrieved with the requesting user's authorization, including vector retrieval. | ubiquitous | must | R2 | UC-071 | AGG-AI-REQUEST | QAS-AI-004 |
| REQ-AI-003 | If the retrieved evidence is insufficient to answer, then the system shall return 'Insufficient Evidence' instead of generating an answer. | unwanted-behaviour | must | R2 | UC-072 | AGG-AI-REQUEST | QAS-AI-002 |
| REQ-AI-004 | The system shall attach to every AI statement the citations (claim, evidence, source, context reference) that support it. | ubiquitous | must | R2 | UC-072 | AGG-AI-REQUEST | QAS-AI-001 |
| REQ-AI-005 | The system shall label every AI-generated draft as AI output and shall prevent its publication without human review. | ubiquitous | must | R2 | UC-073, UC-074 | AGG-AI-RESULT | — |
| REQ-AI-006 | When AI extracts entities, locations or dates from a document, the system shall create proposed claims whose source is the document and whose agent is the mode… | event-driven | must | R2 | UC-072, UC-073 | AGG-AI-RESULT | — |
| REQ-AI-007 | The system shall translate between Arabic and English on request without replacing the original text. | ubiquitous | must | R2 | UC-072 | AGG-AI-REQUEST | — |
| REQ-AI-008 | The system shall enforce the AI autonomy matrix, allowing at most AIL3 in R2 and forbidding AIL5. | ubiquitous | must | R2 | UC-074 | AGG-AI-REQUEST, AGG-AI-RESULT, AGG-AI-ROUTING | — |
| REQ-AI-009 | The system shall manage models through the lifecycle REGISTERED, EVALUATING, APPROVED, STAGED, PRODUCTION, MONITORED, DEPRECATED, RETIRED. | ubiquitous | must | R2 | UC-075 | AGG-MODEL-VERSION | — |
| REQ-AI-010 | When a model version is proposed for production, the system shall require evaluation results for groundedness, citation accuracy, hallucination rate, latency a… | event-driven | must | R2 | UC-075, UC-076 | AGG-EVAL-SUITE, AGG-MODEL-VERSION | QAS-AI-001, QAS-AI-002 |
| REQ-AI-011 | The system shall run all models on local infrastructure by default and shall use external models only where a tenant policy allows it and only for unclassified… | ubiquitous | must | R2 | UC-077 | AGG-AI-REQUEST, AGG-AI-ROUTING | — |
| REQ-AI-012 | If content retrieved into a context package contains instructions, then the system shall treat it as data and shall not let it change tools, permissions or rec… | unwanted-behaviour | must | R2 | UC-071 | AGG-AI-REQUEST, AGG-AI-TOOL | QAS-AI-004 |
| REQ-AI-013 | The system shall register every tool available to AI runs, with the permission it requires and its autonomy level. | ubiquitous | must | R2 | UC-077 | AGG-AI-TOOL | — |
| REQ-AI-014 | The system shall maintain a vector projection of authorized content with the same security labels and pre-filtering as search. | ubiquitous | must | R2 | UC-071 | — (§3.4) | QAS-AI-004 |

#### CAP-13 — الحوكمة والأمن والامتثال

القدرات الفرعية: CAP-13.01 التصنيف والسياسات (R1)، CAP-13.02 التدقيق (R1)، CAP-13.03 الخصوصية والاحتفاظ (R1)، CAP-13.04 السيادة وإقامة البيانات (R1)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-FND-015 | The system shall write an audit record for every state-changing command and for every read of data classified at or above the tenant's audit threshold, contain… | ubiquitous | must | R1 | UC-087 | — (§3.4) | QAS-AUD-001 |
| REQ-FND-016 | The system shall keep audit records append-only and tamper-evident. | ubiquitous | must | R1 | UC-087 | — (§3.4) | QAS-SEC-006 |
| REQ-FND-017 | When a security exception is requested, the system shall require approval by two distinct authorized persons and shall revoke the exception automatically at it… | event-driven | must | R1 | UC-088 | AGG-SECURITY-EXCEPTION | — |
| REQ-GOV-001 | The system shall support a per-tenant classification scheme with ordered levels, an unlimited number of compartments and release caveats. | ubiquitous | must | R1 | UC-085 | AGG-CLASSIFICATION-SCHEME | — |
| REQ-GOV-002 | The system shall require a classification on every object of importance tier T1 or T2. | ubiquitous | must | R1 | **—** | — (§3.4) | — |
| REQ-GOV-003 | The system shall permit read access to an object only if the subject's clearance is at least the object's level and the subject holds every compartment of the… | ubiquitous | must | R1 | UC-089 | AGG-CLEARANCE | QAS-SEC-002 |
| REQ-GOV-004 | When the classification of an object is changed, the system shall require the authority defined by tenant policy, record the change as a new version, and stop… | event-driven | must | R1 | UC-085, UC-089 | AGG-CLEARANCE, AGG-CLASSIFICATION-SCHEME | QAS-SEC-003 |
| REQ-GOV-005 | The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data outside it unless a tenant policy explicitly perm… | ubiquitous | must | R1 | **—** | — (§3.4) | — |
| REQ-GOV-008 | When the personal data of a data subject must be erased, the system shall make it unrecoverable in operational stores, projections, backups and archives while… | event-driven | must | R1 | UC-103 | AGG-PERSON, AGG-ATTACHMENT, AGG-ERASURE-REQUEST | QAS-PRV-001 |
| REQ-GOV-009 | The system shall version, audit and time-stamp every policy and configuration change and apply each change from its effective time. | ubiquitous | must | R1 | UC-086 | AGG-CLASSIFICATION-SCHEME, AGG-POLICY-SET | — |

#### CAP-14 — تشغيل المنصة

القدرات الفرعية: CAP-14.01 المراقبة (R1)، CAP-14.02 الاعتمادية والتعافي (R1)، CAP-14.03 تهيئة المستأجرين والحصص (R1)

| المتطلب | النص | النمط | الأولوية | الإصدار | حالات الاستخدام | الـAggregates | QAS |
|---|---|---|---|---|---|---|---|
| REQ-FND-018 | The system shall enforce per-tenant quotas and rate limits for requests, storage, events and jobs. | ubiquitous | must | R1 | UC-105 | AGG-TENANT | QAS-SCAL-005 |
| REQ-PLT-001 | The system shall install, upgrade and operate in an air-gapped environment with no dependency on external network services. | ubiquitous | must | R1 | **—** | — (§3.4) | QAS-OPS-001 |
| REQ-PLT-002 | The system shall use the same release artifacts for shared, dedicated and sovereign deployments. | ubiquitous | must | R1 | **—** | — (§3.4) | — |
| REQ-PLT-003 | The system shall emit metrics, logs and traces carrying a correlation id across every component, plus business telemetry for the outcome measures. | ubiquitous | must | R1 | **—** | — (§3.4) | QAS-OBS-001 |
| REQ-PLT-004 | The system shall assign every capability to one of the service tiers defined in QAS-AVL-001..003 (critical, important, standard) and meet that tier's availabil… | ubiquitous | must | R1 | **—** | — (§3.4) | QAS-AVL-001, QAS-AVL-002, QAS-AVL-003, QAS-REC-001, QAS-REC-002, QAS-REC-003 |
| REQ-PLT-005 | The system shall run heavy operations (raster processing, bulk import, analysis runs, reconstruction, report generation) as asynchronous jobs with status, retr… | ubiquitous | must | R1 | **—** | — (§3.4) | — |
| REQ-PLT-006 | The system shall publish domain events through a transactional outbox and shall process received events idempotently through an inbox. | ubiquitous | must | R1 | **—** | — (§3.4) | QAS-REL-001 |
| REQ-PLT-007 | The system shall version every API and event contract and shall introduce breaking changes only as a new major version that coexists with the previous one. | ubiquitous | must | R1 | **—** | — (§3.4) | QAS-EVO-001 |
| REQ-PLT-008 | The system shall use cursor-based pagination for every list API. | ubiquitous | must | R1 | **—** | — (§3.4) | — |
| REQ-PLT-009 | The system shall return errors in the standard error model with code, message, details, correlation id, retryable flag and policy reason where applicable. | ubiquitous | must | R1 | **—** | — (§3.4) | — |
| REQ-PLT-010 | The system shall provide its user interfaces in Arabic and English with right-to-left and left-to-right layouts, and optional Hijri date display. | ubiquitous | must | R1 | **—** | — (§3.4) | QAS-ACC-001 |
| REQ-PLT-011 | The system shall provide a responsive web application and a mobile field application. | ubiquitous | must | R1 | **—** | — (§3.4) | — |
| REQ-PLT-012 | The system shall back up all stores according to their service tier and shall verify restores automatically. | ubiquitous | must | R1 | **—** | — (§3.4) | QAS-REC-001 |
| REQ-PLT-013 | The system shall compute resource consumption and cost per tenant from telemetry. | ubiquitous | must | R1 | **—** | — (§3.4) | QAS-COST-001 |

### 3.4 فجوات التغطية

**متطلبات لا يحققها أي Aggregate (37).** أغلبها قيود منصة أو أمن أو مكتبات مشتركة تتحقق بالبنية لا بـAggregate. العمود الأخير يسرد عناصر التصميم التي تحققها من ملفات التتبع `15-traceability/trace-*.md` (العمود `design_elements`)، والاستعلامات التي تذكرها، ودوال اللياقة التي تستند إليها؛ المتطلب بلا أي منها فجوة **[Needs Review]**.

| المتطلب | النمط | الإصدار | النص | يتحقق عبر |
|---|---|---|---|---|
| REQ-AI-014 | ubiquitous | R2 | The system shall maintain a vector projection of authorized content with the same security labels and pre-fil… | SPEC-AI |
| REQ-FND-010 | ubiquitous | R1 | The system shall evaluate authorization before retrieving data for every command, query, search, map request,… | FIT-03, QRY-PDP-DECIDE, QRY-SEC-CONTEXT, SPEC-DISCOVERY |
| REQ-FND-013 | unwanted-behaviour | R1 | If the policy decision point is unavailable or returns an error, then the system shall deny the request. | FIT-16, PB-*/audit-architecture |
| REQ-FND-015 | ubiquitous | R1 | The system shall write an audit record for every state-changing command and for every read of data classified… | PB-*/audit-architecture, QRY-AUD-SEARCH |
| REQ-FND-016 | ubiquitous | R1 | The system shall keep audit records append-only and tamper-evident. | PB-*/audit-architecture, QRY-AUD-VERIFY |
| REQ-GOV-002 | ubiquitous | R1 | The system shall require a classification on every object of importance tier T1 or T2. | LABEL-DERIVATION (54 aggregates) + SL-29 |
| REQ-GOV-005 | ubiquitous | R1 | The system shall keep all data of a deployment within its configured jurisdiction and shall not transfer data… | CELL-ARCHITECTURE §3 (default-deny egress, allow-listed egress gateway); egress monitoring test in PERF/security suite |
| REQ-INF-023 | event-driven | R1 | When a query specifies a valid time T, a record time K, or both, the system shall return the state valid at T… | LIB-CLAIMS-KERNEL, QRY-ENT-RESOLVED |
| REQ-INF-029 | ubiquitous | R1 | The system shall store each geometry in the canonical CRS WGS 84 (EPSG:4326) and shall keep the original CRS… | LIB-CLAIMS-KERNEL |
| REQ-INF-030 | ubiquitous | R1 | The system shall keep the position history of located entities over time. | LIB-CLAIMS-KERNEL, QRY-ENT-POSITIONS |
| REQ-INF-031 | ubiquitous | R1 | The system shall store names in their original form and in normalized and transliterated forms for Arabic and… | LDM name_forms, LIB-CLAIMS-KERNEL |
| REQ-LOG-010 | ubiquitous | R3 | The system shall let an authorized actor list and filter logistics requests by item, destination, state and p… | QRY-LGR-GET, QRY-LGR-LIST |
| REQ-LOG-011 | ubiquitous | R3 | The system shall let an authorized actor list and filter shipments by logistics request, carrier, state and w… | QRY-SHP-GET, QRY-SHP-LIST |
| REQ-LOG-012 | ubiquitous | R3 | The system shall provide the full, ordered checkpoint history of a shipment to an authorized actor. | QRY-SHP-TRACKING |
| REQ-PLT-001 | ubiquitous | R1 | The system shall install, upgrade and operate in an air-gapped environment with no dependency on external net… | FIT-12 (no external network at runtime/build) |
| REQ-PLT-002 | ubiquitous | R1 | The system shall use the same release artifacts for shared, dedicated and sovereign deployments. | RELEASE-CONFIG-MIGRATION §1 (one Zarf bundle; profiles as values; acceptance on 3 profiles) |
| REQ-PLT-003 | ubiquitous | R1 | The system shall emit metrics, logs and traces carrying a correlation id across every component, plus busines… | observability-slc* (8 slices) + correlation id in every contract (X-Correlation-Id) |
| REQ-PLT-004 | ubiquitous | R1 | The system shall assign every capability to one of the service tiers defined in QAS-AVL-001..003 (critical, i… | DR-CONTINUITY §1–2 (tier per DU; DR drills) |
| REQ-PLT-005 | ubiquitous | R1 | The system shall run heavy operations (raster processing, bulk import, analysis runs, reconstruction, report… | async jobs specified: analysis runs, imports, builds, disposition, sync |
| REQ-PLT-006 | ubiquitous | R1 | The system shall publish domain events through a transactional outbox and shall process received events idemp… | outbox/inbox in every LDM + AsyncAPI per slice; FIT-04 |
| REQ-PLT-007 | ubiquitous | R1 | The system shall version every API and event contract and shall introduce breaking changes only as a new majo… | FIT-14, OpenAPI 3.1 / AsyncAPI 3 versioned per slice; FIT-14 |
| REQ-PLT-008 | ubiquitous | R1 | The system shall use cursor-based pagination for every list API. | cursor parameters in all generated list operations; FIT-13 |
| REQ-PLT-009 | ubiquitous | R1 | The system shall return errors in the standard error model with code, message, details, correlation id, retry… | ApiError schema in every generated OpenAPI |
| REQ-PLT-010 | ubiquitous | R1 | The system shall provide its user interfaces in Arabic and English with right-to-left and left-to-right layou… | UI-ARCHITECTURE (i18n ICU, RTL, Hijri display) |
| REQ-PLT-011 | ubiquitous | R1 | The system shall provide a responsive web application and a mobile field application. | UI-ARCHITECTURE (web 360 px+, React Native field app) |
| REQ-PLT-012 | ubiquitous | R1 | The system shall back up all stores according to their service tier and shall verify restores automatically. | DR-CONTINUITY §2 (backups per store, automated restore tests, restore gate) |
| REQ-PLT-013 | ubiquitous | R1 | The system shall compute resource consumption and cost per tenant from telemetry. | COST-MODEL + OpenCost (TD-14) |
| REQ-RCM-014 | ubiquitous | R3 | The system shall let an authorized actor list and filter the risk register by category, scope and score, rest… | QRY-RIS-GET, QRY-RIS-REGISTER |
| REQ-RCM-015 | ubiquitous | R3 | The system shall let an authorized actor list and filter incidents by category, severity, status and scope, r… | QRY-INC-GET, QRY-INC-LIST |
| REQ-RCM-016 | ubiquitous | R3 | The system shall compute an incident's recovery status from its linked contingency plan's task completion aga… | QRY-INC-RECOVERY-STATUS, SPEC-RISK-CONTINGENCY |
| REQ-SIT-007 | ubiquitous | R1 | The system shall serve map layers filtered by the requesting user's authorization and shall not share cached… | QRY-BASE-TILE, QRY-SIT-TILE, SPEC-SITUATION |
| REQ-SRC-001 | ubiquitous | R1 | The system shall provide unified search across entities, observations, documents, assessments, plans and task… | QRY-SRCH-QUERY, SPEC-DISCOVERY |
| REQ-SRC-002 | ubiquitous | R1 | The system shall not reveal the existence of unauthorized objects through search results, counts, facets, sug… | SPEC-DISCOVERY |
| REQ-TRX-012 | ubiquitous | R3 | A person's qualification record shall be able to cite a completed simulation run as evidence, using the exist… | AGG-QUALIFICATION-RECORD (SLC-03, unmodified), SPEC-TRAINING-EXERCISE |
| REQ-TRX-013 | event-driven | R3 | A completed simulation run shall be usable as the terminal source of an After Action Review, captured as a le… | AGG-KNOWLEDGE-OBJECT (SLC-12, CR-63), SPEC-TRAINING-EXERCISE |
| REQ-TRX-014 | ubiquitous | R3 | The system shall let an authorized actor list and filter scenarios, exercises and simulation runs, restricted… | QRY-EXR-GET, QRY-EXR-LIST, QRY-SCN-GET, QRY-SCN-LIST, QRY-SIM-GET, QRY-SIM-LIST |
| REQ-TRX-015 | ubiquitous | R3 | The system shall provide the full, ordered timeline of inject deliveries and evaluations for a simulation run… | QRY-SIM-TIMELINE |

**تعارض بين تتبع المتطلب في الـAggregates (`traces.satisfies`) وفي ملفات التتبع (12)** **[Needs Review]** — مسجل في `00-index.md` §6:

| المتطلب | الـAggregates (satisfies) | الـAggregates (trace-*.md) |
|---|---|---|
| REQ-GOV-004 | AGG-CLASSIFICATION-SCHEME, AGG-CLEARANCE | AGG-CLEARANCE |
| REQ-LOG-002 | AGG-LOGISTICS-REQUEST | AGG-ALLOCATION, AGG-LOGISTICS-REQUEST, AGG-RESOURCE-POOL |
| REQ-LOG-004 | AGG-SHIPMENT | AGG-LOGISTICS-REQUEST, AGG-SHIPMENT |
| REQ-LOG-006 | AGG-SHIPMENT | AGG-LOGISTICS-REQUEST, AGG-SHIPMENT |
| REQ-LOG-008 | AGG-LOGISTICS-REQUEST | AGG-ALLOCATION, AGG-LOGISTICS-REQUEST, AGG-SHIPMENT |
| REQ-LOG-014 | AGG-LOGISTICS-REQUEST | AGG-ALLOCATION |
| REQ-RCM-012 | AGG-INCIDENT | AGG-INCIDENT, AGG-RISK |
| REQ-RCM-013 | AGG-INCIDENT | AGG-INCIDENT, AGG-TASK |
| REQ-TRX-002 | AGG-SCENARIO | AGG-EXERCISE, AGG-SCENARIO |
| REQ-TRX-005 | AGG-EXERCISE | AGG-EXERCISE, AGG-SIMULATION |
| REQ-TRX-012 | — | AGG-QUALIFICATION-RECORD |
| REQ-TRX-013 | — | AGG-KNOWLEDGE-OBJECT |

**متطلبات بلا حالة استخدام (29):** مسرودة بعلامة **—** في §3.3؛ أغلبها في CAP-14 (تشغيل المنصة) وCAP-03.

### 3.5 سيناريوهات الجودة

95 سيناريو في `02-requirements/quality-scenarios.md`؛ مصفوفة التحقق `15-traceability/quality-verification-matrix.md` تغطي 95 منها. غير المغطاة: لا شيء.

| الخاصية | العدد | السيناريوهات |
|---|---|---|
| performance | 29 | QAS-AI-003, QAS-ARC-001, QAS-CNF-001, QAS-ER-003, QAS-LOG-002, QAS-PERF-001, QAS-PERF-002, QAS-PERF-003, QAS-PERF-004, QAS-PERF-005, QAS-PERF-006, QAS-PERF-007, QAS-PERF-008, QAS-PERF-009, QAS-PERF-010, QAS-PERF-011, QAS-PERF-012, QAS-PERF-013, QAS-PERF-014, QAS-PERF-015, QAS-PERF-016, QAS-PERF-017, QAS-PERF-018, QAS-PERF-019, QAS-PERF-021, QAS-PRD-001, QAS-RCM-001, QAS-RES-002, QAS-TRX-002 |
| security | 16 | QAS-AI-004, QAS-OFF-002, QAS-PRD-002, QAS-SEC-001, QAS-SEC-002, QAS-SEC-003, QAS-SEC-004, QAS-SEC-005, QAS-SEC-006, QAS-SEC-007, QAS-SEC-008, QAS-SEC-009, QAS-SEC-010, QAS-SEC-011, QAS-SEC-012, QAS-SEC-013 |
| scalability | 6 | QAS-OFF-003, QAS-SCAL-001, QAS-SCAL-002, QAS-SCAL-003, QAS-SCAL-004, QAS-SCAL-005 |
| integrity | 5 | QAS-ARC-003, QAS-LOG-001, QAS-REL-003, QAS-RES-001, QAS-TRX-001 |
| recoverability | 4 | QAS-REC-001, QAS-REC-002, QAS-REC-003, QAS-REL-004 |
| usability | 4 | QAS-ER-002, QAS-KNW-001, QAS-USA-001, QAS-USA-002 |
| availability | 3 | QAS-AVL-001, QAS-AVL-002, QAS-AVL-003 |
| traceability | 3 | QAS-COL-001, QAS-TRC-001, QAS-TRC-003 |
| AI quality | 2 | QAS-AI-001, QAS-AI-002 |
| correctness | 2 | QAS-ARC-002, QAS-TMP-001 |
| cost | 2 | QAS-AI-005, QAS-COST-001 |
| operability | 2 | QAS-OPS-001, QAS-OPS-003 |
| privacy | 2 | QAS-PRV-001, QAS-PRV-002 |
| reliability | 2 | QAS-INT-001, QAS-REL-001 |
| accessibility | 1 | QAS-ACC-001 |
| accuracy | 1 | QAS-ER-001 |
| auditability | 1 | QAS-AUD-001 |
| compliance | 1 | QAS-GOV-001 |
| data quality | 1 | QAS-DQ-001 |
| evolvability | 1 | QAS-EVO-001 |
| fairness | 1 | QAS-PERF-020 |
| governance | 1 | QAS-RCM-002 |
| observability | 1 | QAS-OBS-001 |
| offline | 1 | QAS-OFF-001 |
| reproducibility | 1 | QAS-TRC-002 |
| resilience | 1 | QAS-REL-002 |
| timeliness | 1 | QAS-OPS-002 |

#### محركات المعمارية (الأولوية H/H)

| السيناريو | الخاصية | المحفِّز | المقياس | التحقق |
|---|---|---|---|---|
| QAS-AVL-001 | availability | normal operation over a month | ≥ 99.9 % monthly | availability SLO monitoring over pilot + chaos tests |
| QAS-GOV-001 | compliance | daily disposition evaluation | candidates computed ≤ 1 h; 0 held records destroyed | disposition run test at design volume |
| QAS-OFF-001 | offline | works 72 h offline then reconnects on a 1 Mbps link | 1,000 queued commands synced ≤ 10 min; 0 silent overwrites; 0 duplicates | field sync tests with interruption injection + device tests |
| QAS-OFF-002 | security | user's clearance reduced while device offline | packages revoked and purged on next contact; commands evaluated under current authorization | field sync tests with interruption injection + device tests |
| QAS-OFF-003 | scalability | 5,000 devices reconnect within 10 min | all sessions complete ≤ 30 min; oldest-offline devices first; no data loss | field sync tests with interruption injection + device tests |
| QAS-PERF-003 | performance | runs a combined text + spatial + temporal search | p95 ≤ 1 s | load test (PERF-TEST-STRATEGY §3) |
| QAS-PERF-005 | performance | reports a value that meets a critical alert rule | end-to-end p95 ≤ 5 s | load test (PERF-TEST-STRATEGY §3) |
| QAS-PERF-018 | performance | graph neighborhood depth 2 | p95 ≤ 1 s | load test (PERF-TEST-STRATEGY §3) |
| QAS-PRV-001 | privacy | orders erasure of a data subject | operational & projections ≤ 24 h; backups unrecoverable immediately via key destruction | erasure drill incl. backup restore gate (FIT-19) |
| QAS-PRV-002 | privacy | restore of a key-store backup older than a key destruction | destroyed keys unusable before any service reads data (restore gate) | erasure drill incl. backup restore gate (FIT-19) |
| QAS-REC-001 | recoverability | primary site lost | RPO ≤ 5 min; RTO ≤ 1 h | DR drill: restore within RPO/RTO per tier (DR-CONTINUITY §2) |
| QAS-REL-004 | recoverability | full projection rebuild | ≤ 24 h to READY with no loss of query service (old version stays ACTIVE) | fault-injection / chaos test (FMEA scenarios) |
| QAS-SCAL-001 | scalability | load rises from pilot (100 concurrent) to 10× (1,000) and then to design (5,000) | 0 architectural or schema changes needed | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) |
| QAS-SCAL-002 | scalability | event burst of 50,000/s for 60 s | 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PERF-005 ≤ 5 min after | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) |
| QAS-SEC-001 | security | attempts to access tenant B data by any path | 0 leaks in tenant-isolation suite | security acceptance + inference suite + penetration test |
| QAS-SEC-002 | security | searches, lists, maps or receives alerts touching objects above clearance | 0 leakage in inference suite (counts, facets, ordering, timing, errors) | security acceptance + inference suite + penetration test |
| QAS-SEC-003 | security | removes a user's compartment | effective on next request in every path, independent of index lag | security acceptance + inference suite + penetration test |
| QAS-SEC-011 | security | inference test suite on search, suggestions, facets, graph and paths | 0 disclosures of hidden objects, hidden facts, hidden nodes/edges | security acceptance + inference suite + penetration test |
| QAS-TMP-001 | correctness | asks for state as of valid time T known at record time K | 100 % agreement with temporal oracle corpus | temporal oracle suite (500 cases) |
| QAS-USA-002 | usability | searches a name with Arabic spelling variants or Latin transliteration | recall ≥ 95 % on the Arabic name test set | usability test with 10 field users; Arabic name recall test set |

#### الكتالوج الكامل

| السيناريو | الخاصية | الأولوية | المحفِّز | المقياس | الحمل | التحقق | متى |
|---|---|---|---|---|---|---|---|
| QAS-ACC-001 | accessibility | M/M | uses R1 web screens | WCAG 2.2 level AA conformance (AR and EN) | — | WCAG 2.2 AA audit (automated + manual) | pre-G8 |
| QAS-AI-001 | AI quality | H/M | evaluation set of 500 questions | ≥ 95 % of cited items actually support the statement | R2 | AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111 | pre-G7-R2 + per model promotion (recalibrate after R1 pilot) |
| QAS-AI-002 | AI quality | H/M | insufficient-evidence and hallucination sets | ≤ 2 % unsupported statements; ≥ 95 % correct 'Insufficient Evidence' | R2 | AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111 | pre-G7-R2 + per model promotion (recalibrate after R1 pilot) |
| QAS-AI-003 | performance | H/M | grounded Q&A request | first token ≤ 3 s, full answer p95 ≤ 20 s on local models | R2 | AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111 | pre-G7-R2 + per model promotion (recalibrate after R1 pilot) |
| QAS-AI-004 | security | H/M | prompt-injection, exfiltration and unauthorized-retrieval suites | 0 unauthorized retrievals, 0 tool abuse, 0 cross-tenant leakage | R2 | AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111 | pre-G7-R2 + per model promotion (recalibrate after R1 pilot) |
| QAS-AI-005 | cost | H/M | AI usage per tenant | GPU-hours and cost per request reported per tenant | R2 | AI evaluation suite (groundedness, citation accuracy, hallucination, injection, exfiltration) — PRJ§31, §111 | pre-G7-R2 + per model promotion (recalibrate after R1 pilot) |
| QAS-ARC-001 | performance | H/M | retrieve an archived record | ≤ 1 min for warm, ≤ 24 h for cold/offline media | R2 | archive retrieval, reconstruction oracle, integrity verification | CI + yearly (recalibrate after R1 pilot) |
| QAS-ARC-002 | correctness | H/M | historical reconstruction scenarios | 100 % agreement with oracle; every element labelled | R2 | archive retrieval, reconstruction oracle, integrity verification | CI + yearly (recalibrate after R1 pilot) |
| QAS-ARC-003 | integrity | H/M | yearly archive integrity verification | 0 unreported corruption; repair from replica | R2 | archive retrieval, reconstruction oracle, integrity verification | CI + yearly (recalibrate after R1 pilot) |
| QAS-AUD-001 | auditability | H/L | executes a state-changing command | 100 % of commands audited with all fields | — | audit completeness check in e2e suite | CI |
| QAS-AVL-001 | availability | H/H | normal operation over a month | ≥ 99.9 % monthly | — | availability SLO monitoring over pilot + chaos tests | pilot (monthly) |
| QAS-AVL-002 | availability | M/M | normal operation over a month | ≥ 99.5 % monthly | — | availability SLO monitoring over pilot + chaos tests | pilot (monthly) |
| QAS-AVL-003 | availability | L/L | normal operation over a month | ≥ 99 % monthly | — | availability SLO monitoring over pilot + chaos tests | pilot (monthly) |
| QAS-CNF-001 | performance | H/M | incompatible claim committed | conflict opened p95 ≤ 30 s | WL-08 | latency test | CI + pilot |
| QAS-COL-001 | traceability | H/M | collection requirement fulfilment | 100 % of fulfilment links traceable to validated observations | R2 | lineage e2e tests | CI (recalibrate after R1 pilot) |
| QAS-COST-001 | cost | M/M | requests monthly cost per tenant | computed from telemetry with no manual input | — | monthly per-tenant cost report from OpenCost | pilot |
| QAS-DQ-001 | data quality | H/L | submits records with invalid geometry or missing CRS | 100 % of invalid records quarantined; 0 published | WL-15 | ingestion acceptance (quarantine) | CI |
| QAS-ER-001 | accuracy | H/M | candidate recall on labelled AR/EN test set | ≥ 95 % of true matches proposed | WL-08 | ruleset evaluation on labelled set; latency test | CI + pilot |
| QAS-ER-002 | usability | H/M | precision of proposals in review queue | ≥ 60 % of proposals are true matches | WL-08 | ruleset evaluation on labelled set; latency test | CI + pilot |
| QAS-ER-003 | performance | H/M | new entity registered | candidates visible p95 ≤ 60 s | WL-08 | ruleset evaluation on labelled set; latency test | CI + pilot |
| QAS-EVO-001 | evolvability | M/L | changes an API or event contract | previous major version supported ≥ 6 months after successor | — | contract compatibility check (FIT-14) | CI |
| QAS-GOV-001 | compliance | H/H | daily disposition evaluation | candidates computed ≤ 1 h; 0 held records destroyed | WL-14 | disposition run test at design volume | pre-G8 |
| QAS-INT-001 | reliability | H/M | ERP adapter outage 4 h | no data loss; backlog processed ≤ 1 h after recovery | R2 | adapter outage/backlog test | pre-G8-R2 (recalibrate after R1 pilot) |
| QAS-KNW-001 | usability | H/M | planner creates a plan for a known task type | relevant published lessons suggested in ≥ 80 % of cases in pilot | R2 | pilot usability measurement | pilot (recalibrate after R1 pilot) |
| QAS-LOG-001 | integrity | H/M | concurrent logistics requests and task/plan allocations on the same resource pool | 0 over-commitment across combined demand; deterministic priority order (shared mechanism with QAS-RES-001) | R3 | TST-SLC18-INVARIANTS + shared capacity-ledger concurrency tests (QAS-RES-001) | CI + pilot (recalibrate after R1 and R2 pilot — RSK-028) |
| QAS-LOG-002 | performance | H/M | shipment dispatched to its destination | transit duration within target (tagged: recalibrate after Pilot R1 and R2 — RSK-028) | R3 | TST-SHIPMENT-SM + transit-time measurement in pilot | pilot (recalibrate after R1 and R2 pilot — RSK-028) |
| QAS-OBS-001 | observability | M/M | investigates a failed request | 100 % of requests traceable end to end | — | trace completeness sampling | pilot |
| QAS-OFF-001 | offline | H/H | works 72 h offline then reconnects on a 1 Mbps link | 1,000 queued commands synced ≤ 10 min; 0 silent overwrites; 0 duplicates | WL-12 | field sync tests with interruption injection + device tests | CI + field pilot |
| QAS-OFF-002 | security | H/H | user's clearance reduced while device offline | packages revoked and purged on next contact; commands evaluated under current authorization | WL-12 | field sync tests with interruption injection + device tests | CI + field pilot |
| QAS-OFF-003 | scalability | H/H | 5,000 devices reconnect within 10 min | all sessions complete ≤ 30 min; oldest-offline devices first; no data loss | WL-12 | field sync tests with interruption injection + device tests | CI + field pilot |
| QAS-OPS-001 | operability | H/M | installs or upgrades in an air-gapped site | offline bundle only; rollback ≤ 1 h | — | air-gapped install/upgrade/rollback rehearsal | pre-G8 |
| QAS-OPS-002 | timeliness | H/M | task reaches due_at | escalation event ≤ 60 s after due | WL-01 | task timer escalation acceptance (TST-SLC03-INVARIANTS) + scheduler latency measurement | CI + pre-G8 |
| QAS-OPS-003 | operability | H/M | push gateway unavailable (air-gapped) | in-app inbox current; polling fallback ≤ 60 s | WL-06 | notification delivery with push gateway down (TST-SLC06-INVARIANTS) | CI + pre-G8 |
| QAS-PERF-001 | performance | H/M | submits a state-changing command | p95 ≤ 300 ms; p99 ≤ 1 s | WL-01 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-002 | performance | H/M | reads a single object or a list page | single object p95 ≤ 300 ms; list page p95 ≤ 1 s | WL-01 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-003 | performance | H/H | runs a combined text + spatial + temporal search | p95 ≤ 1 s | WL-02 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-004 | performance | M/M | an object is created or changed | index lag p95 ≤ 30 s | WL-02 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-005 | performance | H/H | reports a value that meets a critical alert rule | end-to-end p95 ≤ 5 s | WL-06 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-006 | performance | H/M | a situation member changes | p95 ≤ 10 s | WL-06 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-007 | performance | M/H | pans or zooms the operational map | tile p95 ≤ 500 ms | WL-03 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-008 | performance | M/M | records an observation (online) | p95 ≤ 30 s | WL-02 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-009 | performance | H/M | PEP requests a policy decision | p95 ≤ 5 ms with embedded evaluator; ≤ 20 ms remote | WL-01 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-010 | performance | H/M | gateway resolves SecurityContext | p95 ≤ 20 ms (cache hit p95 ≤ 2 ms) | WL-01 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-011 | performance | H/M | a command commits | audit record in BC08 store ≤ 5 s p95; anchor ≤ 5 min | WL-01 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-012 | performance | H/M | batch of 1,000 observations | batch commit p95 ≤ 1 s; 0 duplicates on retry | WL-01/06 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-013 | performance | H/M | resolved entity read (current) | p95 ≤ 300 ms end-to-end | WL-01/06 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-014 | performance | H/M | lineage trace depth 5 | p95 ≤ 2 s | WL-01/06 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-015 | performance | H/M | resolved read of clustered entity | ≤ 20 % overhead vs unclustered; p95 ≤ 300 ms | WL-08 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-016 | performance | H/M | field user opens 'my tasks' | p95 ≤ 500 ms | WL-01 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-017 | performance | H/M | assignment with eligibility check | p95 ≤ 500 ms including BC05 call | WL-01 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-018 | performance | H/H | graph neighborhood depth 2 | p95 ≤ 1 s | WL-02 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-019 | performance | H/M | situation picture read (≤ 2,000 visible members) | p95 ≤ 1 s | WL-06 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-020 | fairness | H/M | tenant submits 100 runs | no tenant exceeds its concurrent-job quota; other tenants' start latency ≤ 30 s | WL-11 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PERF-021 | performance | H/M | plan version baselined with 500 task-generating activities | task synchronization completes ≤ 60 s; idempotent on retry | WL-01 | load test (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-PRD-001 | performance | H/M | generate a 30-page product with 10 maps | ≤ 2 min (async job) | R2 | product generation + inference suite on products | CI (recalibrate after R1 pilot) |
| QAS-PRD-002 | security | H/M | product rendered for an audience | 0 content above the product label (inference suite on products) | R2 | product generation + inference suite on products | CI (recalibrate after R1 pilot) |
| QAS-PRV-001 | privacy | H/H | orders erasure of a data subject | operational & projections ≤ 24 h; backups unrecoverable immediately via key destruction | — | erasure drill incl. backup restore gate (FIT-19) | pre-G8, quarterly |
| QAS-PRV-002 | privacy | H/H | restore of a key-store backup older than a key destruction | destroyed keys unusable before any service reads data (restore gate) | WL-14 | erasure drill incl. backup restore gate (FIT-19) | pre-G8, quarterly |
| QAS-RCM-001 | performance | H/M | CRISIS-severity incident assessed | response dispatched within the severity's SLA (tagged: recalibrate after Pilot R1 and R2 — RSK-028) | R3 | incident dispatch latency test (TST-INCIDENT-SM + load harness) | CI + pilot (recalibrate after R1 and R2 pilot — RSK-028) |
| QAS-RCM-002 | governance | H/M | risk moved to treated status | 100 % of treated risks have ≥ 1 treatment action or an explicit, authorized accept decision | R3 | TST-SLC17-INVARIANTS + registry audit query | CI (recalibrate after R1 and R2 pilot — RSK-028) |
| QAS-REC-001 | recoverability | H/H | primary site lost | RPO ≤ 5 min; RTO ≤ 1 h | — | DR drill: restore within RPO/RTO per tier (DR-CONTINUITY §2) | pre-G8, quarterly |
| QAS-REC-002 | recoverability | M/M | primary site lost | RPO ≤ 15 min; RTO ≤ 4 h | — | DR drill: restore within RPO/RTO per tier (DR-CONTINUITY §2) | pre-G8, quarterly |
| QAS-REC-003 | recoverability | L/L | primary site lost | RPO ≤ 24 h; RTO ≤ 24 h | — | DR drill: restore within RPO/RTO per tier (DR-CONTINUITY §2) | pre-G8, quarterly |
| QAS-REL-001 | reliability | H/M | event bus unavailable for 30 min | 0 lost events; 0 duplicates with effect | WL-06 | fault-injection / chaos test (FMEA scenarios) | CI nightly + pre-G7 |
| QAS-REL-002 | resilience | M/M | search projection unavailable | critical tier unaffected; index rebuilt without data loss | WL-02 | fault-injection / chaos test (FMEA scenarios) | CI nightly + pre-G7 |
| QAS-REL-003 | integrity | H/L | update the same object from the same version | 0 silent overwrites | WL-01 | fault-injection / chaos test (FMEA scenarios) | CI nightly + pre-G7 |
| QAS-REL-004 | recoverability | H/H | full projection rebuild | ≤ 24 h to READY with no loss of query service (old version stays ACTIVE) | WL-02 | fault-injection / chaos test (FMEA scenarios) | CI nightly + pre-G7 |
| QAS-RES-001 | integrity | H/M | 100 concurrent allocation requests on one pool | 0 over-commitment; deterministic priority order | R2 | concurrency and availability tests | CI + pilot (recalibrate after R1 pilot) |
| QAS-RES-002 | performance | H/M | availability query for 1,000 assets over 30 days | p95 ≤ 1 s | R2 | concurrency and availability tests | CI + pilot (recalibrate after R1 pilot) |
| QAS-SCAL-001 | scalability | H/H | load rises from pilot (100 concurrent) to 10× (1,000) and then to design (5,000) | 0 architectural or schema changes needed | WL-01 | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-SCAL-002 | scalability | H/H | event burst of 50,000/s for 60 s | 0 lost events; critical alert p95 ≤ 30 s during burst; back within QAS-PERF-005 ≤ 5 min after | WL-06 | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-SCAL-003 | scalability | M/M | provisions a new tenant | automated; ≤ 1 hour; no code or schema change | — | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-SCAL-004 | scalability | M/H | observations grow to 1e9 | QAS-PERF-002 holds for queries with a time window ≤ 30 days | WL-01 | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-SCAL-005 | scalability | H/M | exceeds its quota by 10× | other tenants stay within QAS-PERF-001 | — | scalability / burst / noisy-tenant tests (PERF-TEST-STRATEGY §3) | pre-G7 + pilot |
| QAS-SEC-001 | security | H/H | attempts to access tenant B data by any path | 0 leaks in tenant-isolation suite | — | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-002 | security | H/H | searches, lists, maps or receives alerts touching objects above clearance | 0 leakage in inference suite (counts, facets, ordering, timing, errors) | WL-02 | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-003 | security | H/H | removes a user's compartment | effective on next request in every path, independent of index lag | — | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-004 | security | H/M | request the same map tile | 0 cross-scope cache hits | WL-03 | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-005 | security | H/L | policy engine unavailable | 100 % fail-closed | — | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-006 | security | H/M | modifies an audit record in storage | detected by next integrity check (≤ 24 h) | — | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-007 | security | H/M | obtains a field device | 0 readable records without authentication; wipe on next connection | WL-12 | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-008 | security | H/M | user disabled via SCIM | next request from any session denied; SCIM-to-effect ≤ 5 min (REQ-FND-005) | WL-01 | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-009 | security | H/M | user without source-protection permission reads claims of a protected human source | 0 identity attributes disclosed in any response, export or lineage | WL-01/06 | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-010 | security | H/M | user sees an entity but not some of its claims | hidden claims affect neither status, counts, completeness nor timing (inference suite) | WL-01/06 | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-011 | security | H/H | inference test suite on search, suggestions, facets, graph and paths | 0 disclosures of hidden objects, hidden facts, hidden nodes/edges | WL-02 | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-012 | security | H/M | user not cleared for an alert's label | receives no alert, notification, push or count change | WL-06 | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-SEC-013 | security | H/M | run submitted by user U | run reads only data visible to U; results labelled ≥ max input label | WL-11 | security acceptance + inference suite + penetration test | CI + pre-G8 |
| QAS-TMP-001 | correctness | H/H | asks for state as of valid time T known at record time K | 100 % agreement with temporal oracle corpus | WL-04 | temporal oracle suite (500 cases) | CI |
| QAS-TRC-001 | traceability | H/M | follows a decision back to its sources | 100 % of decisions and T1 derived objects traceable to sources | — | lineage / basis e2e tests | CI |
| QAS-TRC-002 | reproducibility | M/M | re-executes a recorded deterministic analysis run | 100 % | WL-11 | lineage / basis e2e tests | CI |
| QAS-TRC-003 | traceability | H/M | auditor asks for a decision's basis | authority chain, pinned citations and claims as known at decision time returned; 100 % of decisions | WL-01 | lineage / basis e2e tests | CI |
| QAS-TRX-001 | integrity | H/M | a simulation run nears completion (CMD-SIM-COMPLETE sent) with at least one exercise part… | 0 simulations reach COMPLETED with a participant lacking at least one recorded evaluation (INV-SIM-02) | R3 | TST-SLC19-INVARIANTS + TST-SIMULATION-SM | CI |
| QAS-TRX-002 | performance | H/M | an inject delivered during a live simulation run | 'inject delivery recorded within target latency (tagged: recalibrate after Pilot R1 and R2 — RSK-028)' | R3 | TST-SIMULATION-SM + load harness | CI + pilot (recalibrate after R1 and R2 pilot — RSK-028) |
| QAS-USA-001 | usability | M/M | records an observation with one photo on the mobile app | median ≤ 60 s in usability test with 10 field users | WL-12 | usability test with 10 field users; Arabic name recall test set | pilot |
| QAS-USA-002 | usability | H/H | searches a name with Arabic spelling variants or Latin transliteration | recall ≥ 95 % on the Arabic name test set | WL-02 | usability test with 10 field users; Arabic name recall test set | pilot |

<!-- END GENERATED: build_analysis_design.py -->
