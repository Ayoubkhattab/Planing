---
id: AD-25-TRACEABILITY-MATRIX
type: traceability-matrix
title: "مصفوفة التتبع — من المتطلب إلى الاختبار"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 5)"
sources: [02-requirements/requirements.md, 02-requirements/use-cases.md, 03-domain/contexts/BC*/aggregates/AGG-*.md, 05-contracts/openapi-*.md, 06-data/logical-model/slc-*.md, 13-verification/acceptance/SLC-*/*.md, 13-verification/invariant-properties-*.md, 15-traceability/*.md, 12-solution/deployment-units.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# مصفوفة التتبع

تربط كل متطلب بما يحققه ويتحقق منه، عبر سلسلة واحدة:

```mermaid
flowchart LR
  REQ["متطلب REQ-*"] --> UC["حالة استخدام UC-*"]
  REQ --> AGG["Aggregate AGG-* (traces.satisfies، design_elements)"]
  REQ --> QRY["استعلام QRY-* (عمود المتطلب، design_elements)"]
  AGG --> US["قصة مستخدم US-*"]
  QRY --> US
  AGG --> API["عملية API (CMD-* / QRY-*)"]
  QRY --> API
  AGG --> TAB["جدول schema.table"]
  AGG --> DU["وحدة نشر DU-*"]
  AGG --> CODE["مكان الكود contexts/…/domain/…"]
  REQ --> TST["اختبار قبول TST-* (traces.verifies)"]
```

## 1. كيف تُبنى

| الحلقة | المصدر | القاعدة |
|---|---|---|
| متطلب ← حالة استخدام | حقل `use_cases` في `02-requirements/requirements.md` | كما في المصدر |
| متطلب ← Aggregate | `traces.satisfies` في كل `AGG-*.md`، وما يسميه `design_elements` في `15-traceability/trace-slc*.md` | الحلقة المركزية في التصميم؛ الفرق بين المصدرين مسرود في §4.1 (S-22) |
| متطلب ← استعلام | عمود «المتطلب» في كتالوجات الاستعلامات (`queries-*.md`)، و`design_elements` | متطلبات العرض والتقارير يحققها استعلام لا Aggregate |
| ← قصة، عملية API | القصص المولَّدة في `05-user-stories/`؛ `x-aggregate` للأوامر والـAggregate صاحب المورد للاستعلامات (`14-api-design.md`) | كل قصص وعمليات العنصر المرتبط |
| Aggregate ← جدول | الجدول الرئيسي في `06-data/logical-model/` (`16-database-schema.md`) | جدول رئيسي واحد لكل Aggregate |
| Aggregate ← وحدة نشر | `12-components.md` §2 | Aggregate واحد لا يُقسَّم بين وحدتين |
| Aggregate ← مكان الكود | قاعدة `13-project-structure.md` §5 داخل حزمة السياق (`11-hexagonal-reference.md` §7) | هذا هو التحويل العكسي من المستودع إلى المواصفة |
| متطلب ← اختبار | `traces.verifies` في مواصفات القبول | مواصفات آلة الحالة ترث متطلبات الـAggregate؛ مواصفات الثوابت تسمي المتطلبات بنفسها |

المصفوفة مولَّدة من المصادر في كل تشغيل، فلا تُعدَّل يدويًا (V6 القاعدة 65). ملفات التتبع المعتمدة في `15-traceability/` تبقى مرجع المصدر، وهذه المصفوفة تجمعها مع التصميم والاختبار في مكان واحد.

## 2. القراءة

- **متطلب يحققه استعلام فقط** (عرض، بحث، تقارير) له قصة جلب وعملية API، ولا Aggregate خاص به.
- **متطلب بلا Aggregate ولا استعلام** متطلب منصة أو جودة (CAP-14 وأمثاله) يتحقق في `platform/` وبـFitness functions والقياس، أو بمكتبة أو مواصفة مسماة (`LIB-CLAIMS-KERNEL`، `SPEC-DISCOVERY`).
- **متطلب بلا مواصفة قبول تسميه** له طريقة تحقق أخرى في ملفات التتبع (فحص العقود، خطة W9). شرط G6 «كل متطلب يصل إلى TST» يتحقق إذن لكل المتطلبات عدا هذه، وهي مسرودة في §4.1.

## 3. استعمالها في التنفيذ

- عند تغيير متطلب: الصف في §4.2 يسمّي الـAggregates والاستعلامات والقصص والعمليات والجداول والوحدات والاختبارات المتأثرة.
- عند تغيير Aggregate: الصف في §4.3 يسمّي المتطلبات التي يمسها التغيير ومكان كوده.
- كل commit يذكر القصة (US-*) أو المتطلب (REQ-*) الذي ينفذه (`27-engineering-standards.md` §4)، فيُتتبع من هنا.

## 4. المصفوفة المولَّدة

<!-- BEGIN GENERATED: build_analysis_design.py -->

### 4.1 التغطية

| الحلقة | R1 | R2 | R3 | المجموع |
|---|---|---|---|---|
| المتطلبات | 114 | 51 | 45 | 210 |
| ← حالة استخدام | 85 | 51 | 45 | 181 |
| ← عنصر تصميم (Aggregate أو استعلام) | 95 | 50 | 45 | 190 |
| ← قصة مستخدم | 95 | 50 | 45 | 190 |
| ← عملية API | 95 | 50 | 45 | 190 |
| ← جدول | 90 | 50 | 45 | 185 |
| ← وحدة نشر | 91 | 50 | 45 | 186 |
| ← اختبار قبول يسمّي المتطلب | 99 | 51 | 37 | 187 |

**عنصر التصميم:** `traces.satisfies` في الـAggregates، وعمود «المتطلب» في كتالوجات الاستعلامات، وما يسميه عمود `design_elements` في `15-traceability/trace-slc*.md` من Aggregates واستعلامات.

- **يحققه استعلام فقط (15):** REQ-FND-010, REQ-FND-015, REQ-FND-016, REQ-INF-023, REQ-INF-030, REQ-LOG-010, REQ-LOG-011, REQ-LOG-012, REQ-RCM-014, REQ-RCM-015, REQ-RCM-016, REQ-SIT-007, REQ-SRC-001, REQ-TRX-014, REQ-TRX-015.
- **Aggregate يسميه ملف التتبع ولا يذكر المتطلب في `traces.satisfies` (11):** REQ-LOG-002, REQ-LOG-004, REQ-LOG-006, REQ-LOG-008, REQ-LOG-014, REQ-RCM-012, REQ-RCM-013, REQ-TRX-002, REQ-TRX-005, REQ-TRX-012, REQ-TRX-013 (S-22).
- **بلا Aggregate ولا استعلام (20):** REQ-AI-014 (SPEC-AI), REQ-FND-013, REQ-GOV-002, REQ-GOV-005, REQ-INF-029 (LIB-CLAIMS-KERNEL), REQ-INF-031 (LIB-CLAIMS-KERNEL), REQ-PLT-001, REQ-PLT-002, REQ-PLT-003, REQ-PLT-004, REQ-PLT-005, REQ-PLT-006, REQ-PLT-007, REQ-PLT-008, REQ-PLT-009, REQ-PLT-010, REQ-PLT-011, REQ-PLT-012, REQ-PLT-013, REQ-SRC-002 (SPEC-DISCOVERY) — متطلبات منصة وجودة تتحقق في `platform/` وبـFitness functions والقياس، أو بمكتبة/مواصفة مسماة بين القوسين (`24-testing-strategy.md` §4).

**بلا مواصفة قبول تسميه (23)** — وطريقة تحققها في ملفات التتبع المعتمدة (`15-traceability/`):

| المتطلب | الإصدار | التحقق في المصدر |
|---|---|---|
| REQ-GOV-002 | R1 | contract lint: creation commands of explicit-label aggregates require label |
| REQ-GOV-005 | R1 | egress monitoring test in W9 verification plan |
| REQ-LOG-010 | R3 | contract lint (OpenAPI operationId presence, allowed_scope enforcement) |
| REQ-LOG-011 | R3 | contract lint (OpenAPI operationId presence, allowed_scope enforcement) |
| REQ-LOG-012 | R3 | contract lint (OpenAPI operationId presence) |
| REQ-PLT-001 | R1 | isolated-network CI stage |
| REQ-PLT-002 | R1 | same-release acceptance across shared/dedicated/sovereign modes |
| REQ-PLT-003 | R1 | QAS-OBS-001 trace test |
| REQ-PLT-004 | R1 | DR drills per tier (W9 plan) |
| REQ-PLT-005 | R1 | API lint: no synchronous heavy operations (operations list) |
| REQ-PLT-006 | R1 | fault-injection test at commit |
| REQ-PLT-007 | R1 | contract compatibility check |
| REQ-PLT-008 | R1 | OpenAPI lint |
| REQ-PLT-009 | R1 | OpenAPI lint |
| REQ-PLT-010 | R1 | bilingual/RTL UI review (W9) |
| REQ-PLT-011 | R1 | UI acceptance (W9) |
| REQ-PLT-012 | R1 | scheduled restore tests (W9 plan) |
| REQ-PLT-013 | R1 | monthly per-tenant cost report (W9) |
| REQ-RCM-014 | R3 | contract lint (OpenAPI operationId presence, allowed_scope enforcement) |
| REQ-RCM-015 | R3 | contract lint (OpenAPI operationId presence, allowed_scope enforcement) |
| REQ-RCM-016 | R3 | contract lint (OpenAPI operationId presence) |
| REQ-TRX-014 | R3 | contract lint (OpenAPI operationId presence, allowed_scope enforcement) |
| REQ-TRX-015 | R3 | contract lint (OpenAPI operationId presence) |

**بلا أي تحقق مسمّى (0):** لا شيء.

الاختبارات: 108 مواصفة قبول في `13-verification/acceptance/` و19 ملف خصائص ثوابت (`invariant-properties-*.md`). مواصفة آلة الحالة (`TST-<AGG>-SM`) ترث متطلبات الـAggregate من `traces.satisfies`، فالدليل المستقل على المستوى المتطلب هو مواصفات الثوابت `TST-SLCnn-INVARIANTS`.

### 4.2 لكل متطلب

القصص والعمليات بالعدد، وهي كل قصص وعمليات عناصر التصميم المرتبطة (الـAggregate كله لا الجزء الذي يخص المتطلب وحده)؛ تفاصيلها في `05-user-stories/` و`14-api-design.md`.

#### CAP-01

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-FND-001 | R1 | UC-080 | TENANT | QRY-TEN-GET | 12 | 12 | `foundation.tenants` | DU-02 | TST-SLC01-INVARIANTS, TST-TENANT-SM |
| REQ-FND-002 | R1 | UC-081 | ORGANIZATION | QRY-ORG-TREE | 9 | 9 | `foundation.organizations` | DU-02 | TST-ORGANIZATION-SM |
| REQ-FND-003 | R1 | UC-080 | TENANT | — | 12 | 12 | `foundation.tenants` | DU-02 | TST-SLC01-INVARIANTS, TST-TENANT-SM |
| REQ-FND-004 | R1 | UC-080 | TENANT | — | 12 | 12 | `foundation.tenants` | DU-02 | TST-TENANT-SM |
| REQ-FND-005 | R1 | UC-084 | USER | — | 13 | 13 | `foundation.users` | DU-02 | TST-USER-SM |
| REQ-FND-006 | R1 | UC-084 | PERSON, SERVICE-ACCOUNT, USER | QRY-USR-GET, QRY-USR-LIST | 23 | 23 | `foundation.persons`, `foundation.service_accounts`, `foundation.users` | DU-02 | TST-PERSON-SM, TST-SERVICE-ACCOUNT-SM, TST-USER-SM |
| REQ-FND-007 | R1 | UC-082 | AUTHORITY-GRANT | QRY-AUT-LIST | 10 | 9 | `foundation.authority_grants` | DU-02 | TST-AUTHORITY-GRANT-SM |
| REQ-FND-008 | R1 | UC-083 | AUTHORITY-GRANT | — | 10 | 9 | `foundation.authority_grants` | DU-02 | TST-AUTHORITY-GRANT-SM, TST-SLC01-INVARIANTS |
| REQ-FND-009 | R1 | UC-032, UC-035 | AUTHORITY-GRANT | QRY-AUT-CHECK | 10 | 9 | `foundation.authority_grants` | DU-02 | TST-AUTHORITY-GRANT-SM, TST-SLC01-INVARIANTS |
| REQ-FND-010 | R1 | — | — | QRY-PDP-DECIDE, QRY-SEC-CONTEXT | 2 | 2 | — | — | TST-SLC01-INVARIANTS, TST-SLC05-INVARIANTS |
| REQ-FND-011 | R1 | UC-086 | POLICY-SET, ROLE-ASSIGNMENT | — | 11 | 8 | `foundation.role_assignments`, `governance.policy_sets` | DU-02, DU-03 | TST-POLICY-SET-SM, TST-ROLE-ASSIGNMENT-SM |
| REQ-FND-012 | R1 | UC-086 | POLICY-SET | — | 8 | 6 | `governance.policy_sets` | DU-03 | TST-POLICY-SET-SM |
| REQ-FND-013 | R1 | — | — | — | — | — | — | — | TST-SLC01-INVARIANTS |
| REQ-FND-014 | R1 | UC-086 | ROLE | — | 4 | 4 | `foundation.roles` | DU-02 | TST-ROLE-SM |
| REQ-INT-004 | R2 | UC-084 | HR-SYNC-PROPOSAL | QRY-HRS-QUEUE | 6 | 3 | `foundation.hr_sync_proposals` | DU-02 | TST-HR-SYNC-PROPOSAL-SM, TST-SLC16-INVARIANTS |

#### CAP-02

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-COL-001 | R2 | UC-120 | COLLECTION-REQUIREMENT | QRY-CRQ-BOARD | 13 | 11 | `information.collection_requirements` | DU-04 | TST-COLLECTION-REQUIREMENT-SM, TST-SLC14-INVARIANTS |
| REQ-COL-002 | R2 | UC-121 | COLLECTION-PLAN | QRY-CPL-GET | 8 | 7 | `information.collection_plans` | DU-04 | TST-COLLECTION-PLAN-SM, TST-SLC14-INVARIANTS |
| REQ-COL-003 | R2 | UC-122 | COLLECTION-REQUIREMENT | QRY-CRQ-EVIDENCE, QRY-CRQ-GET | 13 | 11 | `information.collection_requirements` | DU-04 | TST-COLLECTION-REQUIREMENT-SM, TST-SLC14-INVARIANTS |
| REQ-INF-001 | R1 | UC-004, UC-095 | SOURCE | QRY-SRC-GET | 9 | 9 | `information.sources` | DU-04 | TST-SLC02-INVARIANTS, TST-SOURCE-SM |
| REQ-INF-002 | R1 | UC-005 | OBSERVATION | QRY-OBS-GET, QRY-OBS-LIST | 8 | 8 | `information.observations` | DU-05 | TST-OBSERVATION-SM, TST-SLC02-INVARIANTS |
| REQ-INF-003 | R1 | UC-005, UC-006 | ATTACHMENT, EVIDENCE | — | 14 | 11 | `information.attachments`, `information.evidence` | DU-04, DU-05 | TST-ATTACHMENT-SM, TST-EVIDENCE-SM, TST-SLC02-INVARIANTS |
| REQ-INF-004 | R1 | UC-006 | ATTACHMENT, EVIDENCE | QRY-ATT-DOWNLOAD, QRY-EVD-GET | 14 | 11 | `information.attachments`, `information.evidence` | DU-04, DU-05 | TST-ATTACHMENT-SM, TST-EVIDENCE-SM, TST-SLC02-INVARIANTS |
| REQ-INF-005 | R1 | UC-094 | ADAPTER, IMPORT-BATCH | QRY-ADP-GET | 16 | 12 | `information.import_batches`, `integration.adapters` | DU-05, DU-11 | TST-ADAPTER-SM, TST-IMPORT-BATCH-SM, TST-SLC02-INVARIANTS |
| REQ-INF-006 | R1 | UC-094 | IMPORT-BATCH | QRY-IMP-GET | 9 | 5 | `information.import_batches` | DU-05 | TST-IMPORT-BATCH-SM, TST-SLC02-INVARIANTS |
| REQ-INF-007 | R1 | UC-094 | IMPORT-BATCH | — | 9 | 5 | `information.import_batches` | DU-05 | TST-IMPORT-BATCH-SM, TST-SLC02-INVARIANTS |
| REQ-INF-008 | R1 | UC-094 | ADAPTER, IMPORT-BATCH | — | 16 | 12 | `information.import_batches`, `integration.adapters` | DU-05, DU-11 | TST-ADAPTER-SM, TST-IMPORT-BATCH-SM, TST-SLC02-INVARIANTS |
| REQ-INF-009 | R1 | UC-094 | ADAPTER, IMPORT-BATCH | — | 16 | 12 | `information.import_batches`, `integration.adapters` | DU-05, DU-11 | TST-ADAPTER-SM, TST-IMPORT-BATCH-SM, TST-SLC02-INVARIANTS |
| REQ-INT-001 | R2 | UC-094 | INTEGRATION-CONNECTION | QRY-CON-LIST | 10 | 8 | `integration.integration_connections` | DU-11 | TST-INTEGRATION-CONNECTION-SM, TST-SLC16-INVARIANTS |
| REQ-INT-002 | R2 | UC-094 | SENSOR-STREAM | QRY-SNS-LIST | 7 | 6 | `integration.sensor_streams` | DU-11 | TST-SENSOR-STREAM-SM, TST-SLC16-INVARIANTS |
| REQ-OFF-001 | R1 | UC-090 | SYNC-SESSION, TASK | QRY-SYN-DELTA | 39 | 30 | `field.sync_sessions`, `operations.tasks` | DU-08, DU-10 | TST-SLC03-INVARIANTS, TST-SLC11-INVARIANTS, TST-SYNC-SESSION-SM, TST-TASK-SM |
| REQ-OFF-002 | R1 | UC-090 | PRELOAD-PACKAGE | QRY-PKG-GET | 8 | 4 | `field.preload_packages` | DU-10 | TST-PRELOAD-PACKAGE-SM, TST-SLC11-INVARIANTS |
| REQ-OFF-003 | R1 | UC-091 | SYNC-SESSION | — | 7 | 3 | `field.sync_sessions` | DU-10 | TST-SLC11-INVARIANTS, TST-SYNC-SESSION-SM |
| REQ-OFF-004 | R1 | UC-092 | SYNC-CONFLICT, SYNC-SESSION | QRY-SCF-GET, QRY-SCF-LIST | 14 | 9 | `field.sync_conflicts`, `field.sync_sessions` | DU-10 | TST-SLC11-INVARIANTS, TST-SYNC-CONFLICT-SM, TST-SYNC-SESSION-SM |
| REQ-OFF-005 | R1 | UC-093 | DEVICE, PRELOAD-PACKAGE | QRY-DEV-LIST | 17 | 12 | `field.preload_packages`, `foundation.devices` | DU-02, DU-10 | TST-DEVICE-SM, TST-PRELOAD-PACKAGE-SM, TST-SLC11-INVARIANTS |
| REQ-OFF-006 | R1 | UC-091 | SYNC-SESSION | — | 7 | 3 | `field.sync_sessions` | DU-10 | TST-SLC11-INVARIANTS, TST-SYNC-SESSION-SM |

#### CAP-03

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-INF-020 | R1 | UC-001, UC-002, UC-003 | ENTITY, REALWORLD-EVENT | QRY-ENT-LIST, QRY-RWE-GET | 17 | 17 | `information.entities`, `information.realworld_events` | DU-04 | TST-ENTITY-SM, TST-REALWORLD-EVENT-SM, TST-SLC02-INVARIANTS |
| REQ-INF-021 | R1 | UC-006 | CLAIM, ENTITY, EVIDENCE-LINK | QRY-CLM-GET | 20 | 20 | `information.claims`, `information.entities`, `information.evidence_links` | DU-04 | TST-CLAIM-SM, TST-ENTITY-SM, TST-EVIDENCE-LINK-SM, TST-SLC02-INVARIANTS |
| REQ-INF-022 | R1 | — | CLAIM | QRY-ENT-CLAIMS | 8 | 8 | `information.claims`, `information.entities` | DU-04 | TST-CLAIM-SM, TST-SLC02-INVARIANTS |
| REQ-INF-023 | R1 | UC-096 | — | QRY-ENT-RESOLVED | 1 | 1 | `information.entities` | DU-04 | TST-SLC02-INVARIANTS |
| REQ-INF-024 | R1 | — | CLAIM, CONFLICT | — | 18 | 15 | `information.claims`, `information.conflicts` | DU-04 | TST-CLAIM-SM, TST-CONFLICT-SM, TST-SLC02-INVARIANTS, TST-SLC04-INVARIANTS |
| REQ-INF-025 | R1 | UC-008 | CONFLICT | QRY-CNF-GET, QRY-CNF-LIST | 11 | 8 | `information.conflicts` | DU-04 | TST-CONFLICT-SM, TST-SLC04-INVARIANTS |
| REQ-INF-026 | R1 | — | CLAIM | — | 7 | 7 | `information.claims` | DU-04 | TST-CLAIM-SM, TST-SLC02-INVARIANTS |
| REQ-INF-027 | R1 | UC-003 | RELATIONSHIP | QRY-GRAPH-NEIGHBORHOOD, QRY-GRAPH-PATHS, QRY-REL-LIST | 7 | 7 | `information.entities`, `information.relationships` | DU-04 | TST-RELATIONSHIP-SM, TST-SLC02-INVARIANTS, TST-SLC05-INVARIANTS |
| REQ-INF-028 | R1 | — | OBSERVATION | — | 8 | 8 | `information.observations` | DU-05 | TST-OBSERVATION-SM, TST-SLC02-INVARIANTS |
| REQ-INF-029 | R1 | — | — | — | — | — | — | — | TST-SLC02-INVARIANTS |
| REQ-INF-030 | R1 | UC-096 | — | QRY-ENT-POSITIONS | 1 | 1 | `information.entities` | DU-04 | TST-SLC02-INVARIANTS |
| REQ-INF-031 | R1 | — | — | — | — | — | — | — | TST-SLC02-INVARIANTS |
| REQ-INF-032 | R1 | UC-007 | ER-CASE, MATCH-RULESET | QRY-ER-GET, QRY-ER-QUEUE, QRY-MRS-GET | 18 | 16 | `information.er_cases`, `information.match_rulesets` | DU-04 | TST-ER-CASE-SM, TST-MATCH-RULESET-SM, TST-SLC04-INVARIANTS |
| REQ-INF-033 | R1 | UC-007 | ER-CASE | QRY-CLUSTER-GET | 14 | 13 | `information.entities`, `information.er_cases` | DU-04 | TST-ER-CASE-SM, TST-SLC04-INVARIANTS |
| REQ-INF-034 | R1 | UC-104 | ER-CASE | — | 13 | 12 | `information.er_cases` | DU-04 | TST-ER-CASE-SM, TST-SLC04-INVARIANTS |
| REQ-INF-035 | R1 | — | ANALYSIS-RUN, FINDING | QRY-LIN-TRACE | 13 | 10 | `intelligence.analysis_runs`, `intelligence.findings` | DU-06 | TST-ANALYSIS-RUN-SM, TST-FINDING-SM, TST-SLC02-INVARIANTS, TST-SLC07-INVARIANTS |
| REQ-INF-036 | R1 | — | ENTITY, EXTERNAL-ID | QRY-EXT-RESOLVE | 14 | 14 | `information.entities`, `information.external_ids` | DU-04 | TST-ENTITY-SM, TST-EXTERNAL-ID-SM, TST-SLC02-INVARIANTS |
| REQ-INF-037 | R1 | — | CLAIM | — | 7 | 7 | `information.claims` | DU-04 | TST-CLAIM-SM, TST-SLC02-INVARIANTS |
| REQ-SRC-001 | R1 | UC-097 | — | QRY-SRCH-QUERY | 1 | 1 | — | — | TST-SLC05-INVARIANTS |
| REQ-SRC-002 | R1 | UC-097 | — | — | — | — | — | — | TST-SLC05-INVARIANTS |
| REQ-SRC-003 | R1 | UC-097 | MATCH-RULESET | QRY-SRCH-SUGGEST | 6 | 5 | `information.match_rulesets` | DU-04 | TST-MATCH-RULESET-SM, TST-SLC04-INVARIANTS, TST-SLC05-INVARIANTS |
| REQ-SRC-004 | R1 | UC-078 | PROJECTION-VERSION | QRY-PRJ-STATUS | 9 | 5 | — | DU-09 | TST-PROJECTION-VERSION-SM, TST-SLC05-INVARIANTS |

#### CAP-04

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-ANL-001 | R1 | UC-010, UC-011, UC-012 | ANALYSIS-CASE | QRY-ACS-GET, QRY-ACS-LIST | 18 | 18 | `intelligence.analysis_cases` | DU-06 | TST-ANALYSIS-CASE-SM, TST-SLC07-INVARIANTS |
| REQ-ANL-002 | R1 | UC-013 | ANALYSIS-METHOD, ANALYSIS-RUN | QRY-AMT-LIST, QRY-RUN-ARTIFACT, QRY-RUN-GET | 13 | 10 | `intelligence.analysis_methods`, `intelligence.analysis_runs` | DU-06 | TST-ANALYSIS-METHOD-SM, TST-ANALYSIS-RUN-SM, TST-SLC07-INVARIANTS |
| REQ-ANL-003 | R1 | UC-013 | ANALYSIS-METHOD, ANALYSIS-RUN | — | 13 | 10 | `intelligence.analysis_methods`, `intelligence.analysis_runs` | DU-06 | TST-ANALYSIS-METHOD-SM, TST-ANALYSIS-RUN-SM, TST-SLC07-INVARIANTS |
| REQ-ANL-004 | R1 | UC-013 | ANALYSIS-RUN | — | 8 | 5 | `intelligence.analysis_runs` | DU-06 | TST-ANALYSIS-RUN-SM, TST-SLC07-INVARIANTS |
| REQ-ANL-005 | R1 | UC-015, UC-014 | ASSESSMENT, FINDING | QRY-FND-LIST | 15 | 14 | `intelligence.analysis_cases`, `intelligence.assessment_versions`, `intelligence.findings` | DU-06 | TST-ASSESSMENT-SM, TST-FINDING-SM, TST-SLC07-INVARIANTS |
| REQ-ANL-006 | R1 | UC-015 | ASSESSMENT | QRY-ASM-VERSIONS | 10 | 9 | `intelligence.assessment_versions` | DU-06 | TST-ASSESSMENT-SM, TST-SLC07-INVARIANTS |
| REQ-ANL-007 | R1 | UC-016 | ANALYSIS-CASE | QRY-SCN-COMPARE | 18 | 18 | `intelligence.analysis_cases` | DU-06 | TST-ANALYSIS-CASE-SM, TST-SLC07-INVARIANTS |
| REQ-ANL-008 | R1 | — | ASSESSMENT | QRY-ASM-GET | 10 | 9 | `intelligence.assessment_versions` | DU-06 | TST-ASSESSMENT-SM, TST-SLC07-INVARIANTS |
| REQ-FUS-001 | R2 | UC-132 | CORRELATION-PROPOSAL, CORRELATION-RULE | QRY-CRP-QUEUE | 12 | 10 | `information.correlation_proposals`, `information.correlation_rules` | DU-04 | TST-CORRELATION-PROPOSAL-SM, TST-CORRELATION-RULE-SM, TST-SLC15-INVARIANTS |
| REQ-FUS-002 | R2 | UC-132 | CORRELATION-PROPOSAL | QRY-CRP-GET | 8 | 6 | `information.correlation_proposals` | DU-04 | TST-CORRELATION-PROPOSAL-SM, TST-SLC15-INVARIANTS |

#### CAP-05

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-SIT-001 | R1 | UC-020 | SITUATION | QRY-SIT-GET, QRY-SIT-LIST | 12 | 12 | `intelligence.situations` | DU-06 | TST-SITUATION-SM, TST-SLC06-INVARIANTS |
| REQ-SIT-002 | R1 | UC-021, UC-022 | SITUATION | QRY-SIT-CHANGES | 12 | 12 | `intelligence.situations` | DU-06 | TST-SITUATION-SM, TST-SLC06-INVARIANTS |
| REQ-SIT-003 | R1 | UC-024, UC-098 | SITUATION | QRY-SIT-COP | 12 | 12 | `intelligence.situations` | DU-06 | TST-SITUATION-SM, TST-SLC06-INVARIANTS |
| REQ-SIT-004 | R1 | UC-023 | ALERT, ALERT-RULE | — | 14 | 10 | `intelligence.alert_rules`, `intelligence.alerts` | DU-06 | TST-ALERT-RULE-SM, TST-ALERT-SM, TST-SLC06-INVARIANTS |
| REQ-SIT-005 | R1 | UC-023 | ALERT | QRY-ALR-LIST | 8 | 4 | `intelligence.alerts` | DU-06 | TST-ALERT-SM, TST-SLC06-INVARIANTS |
| REQ-SIT-006 | R1 | — | ALERT | — | 8 | 4 | `intelligence.alerts` | DU-06 | TST-ALERT-SM, TST-SLC06-INVARIANTS |
| REQ-SIT-007 | R1 | UC-098 | — | QRY-BASE-TILE, QRY-SIT-TILE | 2 | 2 | `intelligence.situations` | DU-06 | TST-SLC06-INVARIANTS |

#### CAP-06

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-CRD-001 | R2 | UC-130 | COORDINATION-CASE | QRY-CRD-GET, QRY-CRD-LIST | 12 | 11 | `operations.coordination_cases` | DU-08 | TST-COORDINATION-CASE-SM, TST-SLC15-INVARIANTS |
| REQ-CRD-002 | R2 | UC-131 | COORDINATION-CASE | — | 12 | 11 | `operations.coordination_cases` | DU-08 | TST-COORDINATION-CASE-SM, TST-SLC15-INVARIANTS |
| REQ-DEC-001 | R1 | UC-030, UC-031 | DECISION-REQUEST | QRY-DRQ-GET, QRY-DRQ-LIST | 9 | 7 | `operations.decision_requests` | DU-08 | TST-DECISION-REQUEST-SM, TST-SLC08-INVARIANTS |
| REQ-DEC-002 | R1 | UC-032 | DECISION | — | 5 | 4 | `operations.decisions` | DU-08 | TST-DECISION-SM, TST-SLC08-INVARIANTS |
| REQ-DEC-003 | R1 | UC-032 | DECISION | QRY-DEC-BASIS, QRY-DEC-GET | 5 | 4 | `operations.decisions` | DU-08 | TST-DECISION-SM, TST-SLC08-INVARIANTS |
| REQ-DEC-004 | R1 | UC-032 | DECISION | — | 5 | 4 | `operations.decisions` | DU-08 | TST-DECISION-SM, TST-SLC08-INVARIANTS |

#### CAP-07

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-OPS-001 | R1 | UC-033 | PLAN, PLAN-VERSION | QRY-PLN-GET | 23 | 20 | `operations.plan_versions`, `operations.plans` | DU-08 | TST-PLAN-SM, TST-PLAN-VERSION-SM, TST-SLC08-INVARIANTS |
| REQ-OPS-002 | R1 | UC-033, UC-035 | PLAN | — | 14 | 12 | `operations.plans` | DU-08 | TST-PLAN-SM, TST-SLC08-INVARIANTS |
| REQ-OPS-003 | R1 | UC-035, UC-036 | PLAN, PLAN-VERSION | QRY-PLV-LIST | 23 | 20 | `operations.plan_versions`, `operations.plans` | DU-08 | TST-PLAN-SM, TST-PLAN-VERSION-SM, TST-SLC08-INVARIANTS |
| REQ-OPS-004 | R1 | UC-034, UC-036 | PLAN-VERSION | QRY-PLV-DIFF | 10 | 9 | `operations.plan_versions`, `operations.plans` | DU-08 | TST-PLAN-VERSION-SM, TST-SLC08-INVARIANTS |
| REQ-OPS-005 | R1 | UC-035 | PLAN-VERSION, ROLE-ASSIGNMENT | — | 12 | 10 | `foundation.role_assignments`, `operations.plan_versions` | DU-02, DU-08 | TST-PLAN-VERSION-SM, TST-ROLE-ASSIGNMENT-SM, TST-SLC08-INVARIANTS |
| REQ-OPS-006 | R1 | UC-040, UC-042, UC-043, UC-044, UC-045 | TASK | QRY-TASK-GET, QRY-TASK-HISTORY, QRY-TASK-LIST | 32 | 27 | `operations.tasks` | DU-08 | TST-SLC03-INVARIANTS, TST-TASK-SM |
| REQ-OPS-007 | R1 | UC-041, UC-102 | TASK, TASK-TYPE | — | 37 | 32 | `operations.task_types`, `operations.tasks` | DU-08 | TST-SLC03-INVARIANTS, TST-TASK-SM, TST-TASK-TYPE-SM |
| REQ-OPS-008 | R1 | UC-045 | TASK | — | 32 | 27 | `operations.tasks` | DU-08 | TST-SLC03-INVARIANTS, TST-TASK-SM |
| REQ-OPS-009 | R1 | UC-044 | ROLE-ASSIGNMENT, TASK | — | 35 | 29 | `foundation.role_assignments`, `operations.tasks` | DU-02, DU-08 | TST-ROLE-ASSIGNMENT-SM, TST-SLC03-INVARIANTS, TST-TASK-SM |
| REQ-OPS-010 | R1 | UC-040 | TASK | — | 32 | 27 | `operations.tasks` | DU-08 | TST-SLC03-INVARIANTS, TST-TASK-SM |
| REQ-OPS-011 | R1 | — | TASK | — | 32 | 27 | `operations.tasks` | DU-08 | TST-SLC03-INVARIANTS, TST-TASK-SM |
| REQ-OPS-012 | R1 | UC-046 | TASK | — | 32 | 27 | `operations.tasks` | DU-08 | TST-SLC03-INVARIANTS, TST-TASK-SM |
| REQ-OPS-013 | R1 | UC-101 | OUTCOME-TRACKER | QRY-OUT-SERIES, QRY-PLN-PROGRESS | 7 | 4 | `operations.outcome_trackers`, `operations.plans` | DU-08 | TST-OUTCOME-TRACKER-SM, TST-SLC08-INVARIANTS |
| REQ-OPS-014 | R1 | UC-034, UC-044 | PLAN-VERSION, TASK-TYPE | QRY-TTY-GET | 14 | 13 | `operations.plan_versions`, `operations.task_types` | DU-08 | TST-PLAN-VERSION-SM, TST-SLC03-INVARIANTS, TST-SLC08-INVARIANTS, TST-TASK-TYPE-SM |

#### CAP-08

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-LOG-001 | R3 | UC-150 | LOGISTICS-REQUEST | — | 12 | 5 | `readiness.logistics_requests` | DU-14 | TST-LOGISTICS-REQUEST-SM, TST-SLC18-INVARIANTS |
| REQ-LOG-002 | R3 | UC-150 | ALLOCATION, LOGISTICS-REQUEST, RESOURCE-POOL | — | 30 | 18 | `readiness.allocations`, `readiness.logistics_requests`, `readiness.resource_pools` | DU-14 | TST-LOGISTICS-REQUEST-SM, TST-SLC18-INVARIANTS |
| REQ-LOG-003 | R3 | UC-150 | LOGISTICS-REQUEST | — | 12 | 5 | `readiness.logistics_requests` | DU-14 | TST-LOGISTICS-REQUEST-SM, TST-SLC18-INVARIANTS |
| REQ-LOG-004 | R3 | UC-151 | LOGISTICS-REQUEST, SHIPMENT | — | 22 | 15 | `readiness.logistics_requests`, `readiness.shipments` | DU-14 | TST-SHIPMENT-SM, TST-SLC18-INVARIANTS |
| REQ-LOG-005 | R3 | UC-151 | SHIPMENT | — | 10 | 10 | `readiness.shipments` | DU-14 | TST-SHIPMENT-SM |
| REQ-LOG-006 | R3 | UC-152 | LOGISTICS-REQUEST, SHIPMENT | — | 22 | 15 | `readiness.logistics_requests`, `readiness.shipments` | DU-14 | TST-SHIPMENT-SM, TST-SLC18-INVARIANTS |
| REQ-LOG-007 | R3 | UC-152 | SHIPMENT | — | 10 | 10 | `readiness.shipments` | DU-14 | TST-SHIPMENT-SM |
| REQ-LOG-008 | R3 | UC-152 | ALLOCATION, LOGISTICS-REQUEST, SHIPMENT | — | 34 | 22 | `readiness.allocations`, `readiness.logistics_requests`, `readiness.shipments` | DU-14 | TST-LOGISTICS-REQUEST-SM, TST-SLC18-INVARIANTS |
| REQ-LOG-009 | R3 | UC-152 | LOGISTICS-REQUEST, SHIPMENT | — | 22 | 15 | `readiness.logistics_requests`, `readiness.shipments` | DU-14 | TST-LOGISTICS-REQUEST-SM, TST-SHIPMENT-SM, TST-SLC18-INVARIANTS |
| REQ-LOG-010 | R3 | UC-150 | — | QRY-LGR-GET, QRY-LGR-LIST | 2 | 2 | `readiness.logistics_requests` | DU-14 | — |
| REQ-LOG-011 | R3 | UC-151 | — | QRY-SHP-GET, QRY-SHP-LIST | 2 | 2 | `readiness.shipments` | DU-14 | — |
| REQ-LOG-012 | R3 | UC-151 | — | QRY-SHP-TRACKING | 1 | 1 | `readiness.shipments` | DU-14 | — |
| REQ-LOG-013 | R3 | UC-150 | LOGISTICS-REQUEST | — | 12 | 5 | `readiness.logistics_requests` | DU-14 | TST-LOGISTICS-REQUEST-SM |
| REQ-LOG-014 | R3 | UC-150 | ALLOCATION, LOGISTICS-REQUEST | — | 24 | 12 | `readiness.allocations`, `readiness.logistics_requests` | DU-14 | TST-LOGISTICS-REQUEST-SM |
| REQ-RDY-001 | R1 | UC-102 | QUALIFICATION-RECORD | QRY-QUAL-LIST | 7 | 6 | `readiness.qualification_records` | DU-08 | TST-QUALIFICATION-RECORD-SM, TST-SLC03-INVARIANTS |
| REQ-RDY-002 | R1 | UC-102 | QUALIFICATION-RECORD | QRY-ELIG-CHECK | 8 | 7 | `readiness.qualification_records` | DU-08 | TST-QUALIFICATION-RECORD-SM, TST-SLC03-INVARIANTS |
| REQ-RES-001 | R2 | UC-050 | ASSET | QRY-AST-GET | 14 | 14 | `readiness.assets` | DU-14 | TST-ASSET-SM, TST-SLC09-INVARIANTS |
| REQ-RES-002 | R2 | UC-053 | ASSET | — | 14 | 14 | `readiness.assets` | DU-14 | TST-ASSET-SM, TST-SLC09-INVARIANTS |
| REQ-RES-003 | R2 | UC-051, UC-053 | ASSET, ASSET-ASSIGNMENT | QRY-AST-AVAILABILITY | 18 | 17 | `readiness.asset_assignments`, `readiness.assets` | DU-14 | TST-ASSET-ASSIGNMENT-SM, TST-ASSET-SM, TST-SLC09-INVARIANTS |
| REQ-RES-004 | R2 | UC-051 | MAINTENANCE-ORDER | QRY-MNT-SCHEDULE | 6 | 6 | `readiness.maintenance_orders` | DU-14 | TST-MAINTENANCE-ORDER-SM, TST-SLC09-INVARIANTS |
| REQ-RES-005 | R2 | UC-050 | ASSET | — | 14 | 14 | `readiness.assets` | DU-14 | TST-ASSET-SM, TST-SLC09-INVARIANTS |
| REQ-RES-006 | R2 | UC-054 | RESOURCE-POOL | QRY-POL-TIMELINE | 6 | 6 | `readiness.resource_pools` | DU-14 | TST-RESOURCE-POOL-SM, TST-SLC09-INVARIANTS |
| REQ-RES-007 | R2 | UC-054 | ALLOCATION | QRY-ALC-LIST | 12 | 7 | `readiness.allocations` | DU-14 | TST-ALLOCATION-SM, TST-SLC09-INVARIANTS |
| REQ-RES-008 | R2 | UC-054 | ALLOCATION | — | 12 | 7 | `readiness.allocations` | DU-14 | TST-ALLOCATION-SM, TST-SLC09-INVARIANTS |
| REQ-RES-009 | R2 | UC-054 | ALLOCATION | — | 12 | 7 | `readiness.allocations` | DU-14 | TST-ALLOCATION-SM, TST-SLC09-INVARIANTS |
| REQ-RES-010 | R2 | UC-055 | ALLOCATION | — | 12 | 7 | `readiness.allocations` | DU-14 | TST-ALLOCATION-SM, TST-SLC09-INVARIANTS |
| REQ-RES-011 | R2 | UC-054 | ALLOCATION | — | 12 | 7 | `readiness.allocations` | DU-14 | TST-ALLOCATION-SM, TST-SLC09-INVARIANTS |
| REQ-RES-012 | R2 | UC-053, UC-054 | ALLOCATION, ASSET-ASSIGNMENT | — | 16 | 10 | `readiness.allocations`, `readiness.asset_assignments` | DU-14 | TST-ALLOCATION-SM, TST-ASSET-ASSIGNMENT-SM, TST-SLC09-INVARIANTS |
| REQ-RES-013 | R2 | UC-102 | ROLE-REQUIREMENT | QRY-READINESS | 5 | 5 | `readiness.role_requirements` | DU-14 | TST-ROLE-REQUIREMENT-SM, TST-SLC09-INVARIANTS |
| REQ-RES-014 | R2 | UC-052 | ASSET-RESERVATION | — | 6 | 4 | `readiness.asset_reservations` | DU-14 | TST-ASSET-RESERVATION-SM, TST-SLC09-INVARIANTS |
| REQ-TRX-001 | R3 | UC-160 | SCENARIO | — | 6 | 6 | `readiness.scenarios` | DU-14 | TST-SCENARIO-SM |
| REQ-TRX-002 | R3 | UC-160 | EXERCISE, SCENARIO | — | 14 | 12 | `readiness.exercises`, `readiness.scenarios` | DU-14 | TST-SCENARIO-SM, TST-SLC19-INVARIANTS |
| REQ-TRX-003 | R3 | UC-161 | EXERCISE | — | 8 | 6 | `readiness.exercises` | DU-14 | TST-EXERCISE-SM, TST-SLC19-INVARIANTS |
| REQ-TRX-004 | R3 | UC-161 | EXERCISE | — | 8 | 6 | `readiness.exercises` | DU-14 | TST-EXERCISE-SM |
| REQ-TRX-005 | R3 | UC-162 | EXERCISE, SIMULATION | — | 18 | 16 | `readiness.exercises`, `readiness.simulations` | DU-14 | TST-EXERCISE-SM, TST-SLC19-INVARIANTS |
| REQ-TRX-006 | R3 | UC-162 | EXERCISE | — | 8 | 6 | `readiness.exercises` | DU-14 | TST-EXERCISE-SM, TST-SLC19-INVARIANTS |
| REQ-TRX-007 | R3 | UC-161 | EXERCISE | — | 8 | 6 | `readiness.exercises` | DU-14 | TST-EXERCISE-SM |
| REQ-TRX-008 | R3 | UC-162 | SIMULATION | — | 10 | 10 | `readiness.simulations` | DU-14 | TST-SIMULATION-SM |
| REQ-TRX-009 | R3 | UC-162 | SIMULATION | — | 10 | 10 | `readiness.simulations` | DU-14 | TST-SIMULATION-SM |
| REQ-TRX-010 | R3 | UC-162 | SIMULATION | — | 10 | 10 | `readiness.simulations` | DU-14 | TST-SIMULATION-SM, TST-SLC19-INVARIANTS |
| REQ-TRX-011 | R3 | UC-162 | SIMULATION | — | 10 | 10 | `readiness.simulations` | DU-14 | TST-SIMULATION-SM |
| REQ-TRX-012 | R3 | UC-163 | QUALIFICATION-RECORD | — | 7 | 6 | `readiness.qualification_records` | DU-08 | TST-SLC19-INVARIANTS |
| REQ-TRX-013 | R3 | UC-163 | KNOWLEDGE-OBJECT | — | 12 | 11 | `knowledge.knowledge_objects` | DU-15 | TST-SLC19-INVARIANTS |
| REQ-TRX-014 | R3 | UC-161 | — | QRY-EXR-GET, QRY-EXR-LIST, QRY-SCN-GET, QRY-SCN-LIST, QRY-SIM-GET, QRY-SIM-LIST | 6 | 6 | `readiness.exercises`, `readiness.scenarios`, `readiness.simulations` | DU-14 | — |
| REQ-TRX-015 | R3 | UC-162 | — | QRY-SIM-TIMELINE | 1 | 1 | `readiness.simulations` | DU-14 | — |

#### CAP-09

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-RCM-001 | R3 | UC-140 | RISK | — | 8 | 7 | `operations.risks` | DU-08 | TST-RISK-SM |
| REQ-RCM-002 | R3 | UC-140 | RISK | — | 8 | 7 | `operations.risks` | DU-08 | TST-RISK-SM, TST-SLC17-INVARIANTS |
| REQ-RCM-003 | R3 | UC-140 | RISK | — | 8 | 7 | `operations.risks` | DU-08 | TST-RISK-SM, TST-SLC17-INVARIANTS |
| REQ-RCM-004 | R3 | UC-141 | RISK | — | 8 | 7 | `operations.risks` | DU-08 | TST-RISK-SM, TST-SLC17-INVARIANTS |
| REQ-RCM-005 | R3 | UC-141 | RISK | — | 8 | 7 | `operations.risks` | DU-08 | TST-RISK-SM, TST-SLC17-INVARIANTS |
| REQ-RCM-006 | R3 | UC-142 | INCIDENT | — | 14 | 13 | `operations.incidents` | DU-08 | TST-INCIDENT-SM |
| REQ-RCM-007 | R3 | UC-142 | INCIDENT | — | 14 | 13 | `operations.incidents` | DU-08 | TST-INCIDENT-SM |
| REQ-RCM-008 | R3 | UC-143 | INCIDENT | — | 14 | 13 | `operations.incidents` | DU-08 | TST-INCIDENT-SM |
| REQ-RCM-009 | R3 | UC-143 | INCIDENT | — | 14 | 13 | `operations.incidents` | DU-08 | TST-INCIDENT-SM, TST-SLC17-INVARIANTS |
| REQ-RCM-010 | R3 | UC-143 | INCIDENT | — | 14 | 13 | `operations.incidents` | DU-08 | TST-INCIDENT-SM, TST-SLC17-INVARIANTS |
| REQ-RCM-011 | R3 | UC-144 | INCIDENT | — | 14 | 13 | `operations.incidents` | DU-08 | TST-INCIDENT-SM, TST-SLC17-INVARIANTS |
| REQ-RCM-012 | R3 | UC-143 | INCIDENT, RISK | — | 22 | 20 | `operations.incidents`, `operations.risks` | DU-08 | TST-INCIDENT-SM, TST-SLC17-INVARIANTS |
| REQ-RCM-013 | R3 | UC-143 | INCIDENT, TASK | — | 46 | 40 | `operations.incidents`, `operations.tasks` | DU-08 | TST-INCIDENT-SM, TST-SLC17-INVARIANTS |
| REQ-RCM-014 | R3 | UC-140 | — | QRY-RIS-GET, QRY-RIS-REGISTER | 2 | 2 | `operations.risks` | DU-08 | — |
| REQ-RCM-015 | R3 | UC-142 | — | QRY-INC-GET, QRY-INC-LIST | 2 | 2 | `operations.incidents` | DU-08 | — |
| REQ-RCM-016 | R3 | UC-144 | — | QRY-INC-RECOVERY-STATUS | 1 | 1 | `operations.incidents` | DU-08 | — |

#### CAP-10

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-COM-001 | R1 | UC-099 | NOTIFICATION, SUBSCRIPTION | QRY-NTF-INBOX | 13 | 7 | `operations.notifications`, `operations.subscriptions` | DU-08 | TST-NOTIFICATION-SM, TST-SLC06-INVARIANTS, TST-SUBSCRIPTION-SM |
| REQ-COM-002 | R1 | UC-099 | NOTIFICATION | — | 7 | 2 | `operations.notifications` | DU-08 | TST-NOTIFICATION-SM, TST-SLC06-INVARIANTS |
| REQ-INT-003 | R2 | UC-023 | CAP-MESSAGE | QRY-CAP-LIST | 6 | 5 | `intelligence.cap_messages` | DU-06 | TST-CAP-MESSAGE-SM, TST-SLC16-INVARIANTS |
| REQ-PRD-001 | R2 | UC-110 | PRODUCT, PRODUCT-TEMPLATE | QRY-PRD-LIST | 18 | 15 | `knowledge.product_templates`, `knowledge.products` | DU-15 | TST-PRODUCT-SM, TST-PRODUCT-TEMPLATE-SM, TST-SLC12-INVARIANTS |
| REQ-PRD-002 | R2 | UC-110 | PRODUCT | — | 14 | 11 | `knowledge.products` | DU-15 | TST-PRODUCT-SM, TST-SLC12-INVARIANTS |
| REQ-PRD-003 | R2 | UC-111 | PRODUCT | QRY-PRD-GET | 14 | 11 | `knowledge.products` | DU-15 | TST-PRODUCT-SM, TST-SLC12-INVARIANTS |
| REQ-PRD-004 | R2 | UC-112 | DISTRIBUTION | QRY-DST-LOG | 5 | 3 | `knowledge.distributions`, `knowledge.products` | DU-15 | TST-DISTRIBUTION-SM, TST-SLC12-INVARIANTS |
| REQ-PRD-005 | R2 | UC-112 | DISTRIBUTION | — | 4 | 2 | `knowledge.distributions` | DU-15 | TST-DISTRIBUTION-SM, TST-SLC12-INVARIANTS |

#### CAP-11

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-ARC-001 | R2 | UC-063 | ARCHIVE-PACKAGE | — | 11 | 6 | `knowledge.archive_packages` | DU-15 | TST-ARCHIVE-PACKAGE-SM, TST-SLC12-INVARIANTS |
| REQ-ARC-002 | R2 | UC-063 | ARCHIVE-PACKAGE | — | 11 | 6 | `knowledge.archive_packages` | DU-15 | TST-ARCHIVE-PACKAGE-SM, TST-SLC12-INVARIANTS |
| REQ-ARC-003 | R2 | UC-064 | ARCHIVE-PACKAGE | QRY-ARC-RETRIEVE, QRY-ARC-SEARCH | 11 | 6 | `knowledge.archive_packages` | DU-15 | TST-ARCHIVE-PACKAGE-SM, TST-SLC12-INVARIANTS |
| REQ-ARC-004 | R2 | UC-065 | RECONSTRUCTION | QRY-REC-REPORT | 6 | 3 | `knowledge.reconstructions` | DU-15 | TST-RECONSTRUCTION-SM, TST-SLC12-INVARIANTS |
| REQ-GOV-006 | R1 | UC-103 | DISPOSITION-RUN, RETENTION-SCHEDULE | QRY-DSP-GET, QRY-RTS-ACTIVE | 14 | 9 | `governance.disposition_runs`, `governance.retention_schedules` | DU-03 | TST-DISPOSITION-RUN-SM, TST-RETENTION-SCHEDULE-SM, TST-SLC12A-INVARIANTS |
| REQ-GOV-007 | R1 | UC-103 | DISPOSITION-RUN, LEGAL-HOLD | QRY-LHD-CHECK, QRY-LHD-LIST | 15 | 11 | `governance.disposition_runs`, `governance.legal_holds` | DU-03 | TST-DISPOSITION-RUN-SM, TST-LEGAL-HOLD-SM, TST-SLC12A-INVARIANTS |
| REQ-KNW-001 | R2 | UC-060, UC-061, UC-062 | KNOWLEDGE-OBJECT | QRY-KNO-SEARCH | 12 | 11 | `knowledge.knowledge_objects` | DU-15 | TST-KNOWLEDGE-OBJECT-SM, TST-SLC12-INVARIANTS |
| REQ-KNW-002 | R2 | UC-060 | KNOWLEDGE-OBJECT | — | 12 | 11 | `knowledge.knowledge_objects` | DU-15 | TST-KNOWLEDGE-OBJECT-SM, TST-SLC12-INVARIANTS |
| REQ-KNW-003 | R2 | UC-062 | KNOWLEDGE-OBJECT | QRY-KNO-SUGGEST | 12 | 11 | `knowledge.knowledge_objects` | DU-15 | TST-KNOWLEDGE-OBJECT-SM, TST-SLC12-INVARIANTS |

#### CAP-12

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-AI-001 | R2 | UC-070, UC-071, UC-072 | AI-REQUEST | QRY-AI-USAGE, QRY-AIR-GET | 12 | 5 | `ai.ai_requests` | DU-16 | TST-AI-REQUEST-SM, TST-SLC10-INVARIANTS |
| REQ-AI-002 | R2 | UC-071 | AI-REQUEST | QRY-AIR-CONTEXT | 11 | 4 | `ai.ai_requests` | DU-16 | TST-AI-REQUEST-SM, TST-SLC10-INVARIANTS |
| REQ-AI-003 | R2 | UC-072 | AI-REQUEST | — | 11 | 4 | `ai.ai_requests` | DU-16 | TST-AI-REQUEST-SM, TST-SLC10-INVARIANTS |
| REQ-AI-004 | R2 | UC-072 | AI-REQUEST | — | 11 | 4 | `ai.ai_requests` | DU-16 | TST-AI-REQUEST-SM, TST-SLC10-INVARIANTS |
| REQ-AI-005 | R2 | UC-073, UC-074 | AI-RESULT | QRY-AIRS-QUEUE | 6 | 5 | `ai.ai_results` | DU-16 | TST-AI-RESULT-SM, TST-SLC10-INVARIANTS |
| REQ-AI-006 | R2 | UC-072, UC-073 | AI-RESULT | — | 6 | 5 | `ai.ai_results` | DU-16 | TST-AI-RESULT-SM, TST-SLC10-INVARIANTS |
| REQ-AI-007 | R2 | UC-072 | AI-REQUEST | — | 11 | 4 | `ai.ai_requests` | DU-16 | TST-AI-REQUEST-SM, TST-SLC10-INVARIANTS |
| REQ-AI-008 | R2 | UC-074 | AI-REQUEST, AI-RESULT, AI-ROUTING | QRY-RTG-ACTIVE | 23 | 14 | `ai.ai_requests`, `ai.ai_results`, `ai.ai_routings` | DU-16 | TST-AI-REQUEST-SM, TST-AI-RESULT-SM, TST-AI-ROUTING-SM, TST-SLC10-INVARIANTS |
| REQ-AI-009 | R2 | UC-075 | MODEL-VERSION | QRY-MDL-LIST | 11 | 10 | `ai.model_versions` | DU-16 | TST-MODEL-VERSION-SM, TST-SLC10-INVARIANTS |
| REQ-AI-010 | R2 | UC-075, UC-076 | EVAL-SUITE, MODEL-VERSION | — | 15 | 13 | `ai.eval_suites`, `ai.model_versions` | DU-16 | TST-EVAL-SUITE-SM, TST-MODEL-VERSION-SM, TST-SLC10-INVARIANTS |
| REQ-AI-011 | R2 | UC-077 | AI-REQUEST, AI-ROUTING | — | 17 | 9 | `ai.ai_requests`, `ai.ai_routings` | DU-16 | TST-AI-REQUEST-SM, TST-AI-ROUTING-SM, TST-SLC10-INVARIANTS |
| REQ-AI-012 | R2 | UC-071 | AI-REQUEST, AI-TOOL | — | 17 | 10 | `ai.ai_requests`, `ai.ai_tools` | DU-16 | TST-AI-REQUEST-SM, TST-AI-TOOL-SM, TST-SLC10-INVARIANTS |
| REQ-AI-013 | R2 | UC-077 | AI-TOOL | QRY-TOL-LIST | 6 | 6 | `ai.ai_tools` | DU-16 | TST-AI-TOOL-SM, TST-SLC10-INVARIANTS |
| REQ-AI-014 | R2 | UC-071 | — | — | — | — | — | — | TST-SLC10-INVARIANTS |

#### CAP-13

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-FND-015 | R1 | UC-087 | — | QRY-AUD-SEARCH | 1 | 1 | — | — | TST-SLC01-INVARIANTS |
| REQ-FND-016 | R1 | UC-087 | — | QRY-AUD-VERIFY | 1 | 1 | — | — | TST-SLC01-INVARIANTS |
| REQ-FND-017 | R1 | UC-088 | SECURITY-EXCEPTION | QRY-EXC-LIST | 6 | 5 | `governance.security_exceptions` | DU-03 | TST-SECURITY-EXCEPTION-SM, TST-SLC01-INVARIANTS |
| REQ-GOV-001 | R1 | UC-085 | CLASSIFICATION-SCHEME | QRY-CLS-ACTIVE | 6 | 5 | `governance.classification_schemes` | DU-03 | TST-CLASSIFICATION-SCHEME-SM |
| REQ-GOV-002 | R1 | — | — | — | — | — | — | — | — |
| REQ-GOV-003 | R1 | UC-089 | CLEARANCE | QRY-CLR-GET | 8 | 7 | `foundation.clearances`, `foundation.users` | DU-02 | TST-CLEARANCE-SM, TST-SLC01-INVARIANTS |
| REQ-GOV-004 | R1 | UC-085, UC-089 | CLASSIFICATION-SCHEME, CLEARANCE | — | 13 | 11 | `foundation.clearances`, `governance.classification_schemes` | DU-02, DU-03 | TST-CLASSIFICATION-SCHEME-SM, TST-CLEARANCE-SM, TST-SLC01-INVARIANTS, TST-SLC05-INVARIANTS |
| REQ-GOV-005 | R1 | — | — | — | — | — | — | — | — |
| REQ-GOV-008 | R1 | UC-103 | ATTACHMENT, ERASURE-REQUEST, PERSON | QRY-ERS-GET | 21 | 13 | `foundation.persons`, `governance.erasure_requests`, `information.attachments` | DU-02, DU-03, DU-05 | TST-ATTACHMENT-SM, TST-ERASURE-REQUEST-SM, TST-PERSON-SM, TST-SLC12A-INVARIANTS |
| REQ-GOV-009 | R1 | UC-086 | CLASSIFICATION-SCHEME, POLICY-SET | QRY-POL-GET | 14 | 11 | `governance.classification_schemes`, `governance.policy_sets` | DU-03 | TST-CLASSIFICATION-SCHEME-SM, TST-POLICY-SET-SM |

#### CAP-14

| المتطلب | الإصدار | حالات الاستخدام | الـAggregates | الاستعلامات | قصص | عمليات | الجداول | الوحدات | الاختبارات |
|---|---|---|---|---|---|---|---|---|---|
| REQ-FND-018 | R1 | UC-105 | TENANT | — | 12 | 12 | `foundation.tenants` | DU-02 | TST-TENANT-SM |
| REQ-PLT-001 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-002 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-003 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-004 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-005 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-006 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-007 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-008 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-009 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-010 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-011 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-012 | R1 | — | — | — | — | — | — | — | — |
| REQ-PLT-013 | R1 | — | — | — | — | — | — | — | — |

### 4.3 لكل Aggregate

مكان الكود بقاعدة `13-project-structure.md` §5 داخل حزمة السياق (`11-hexagonal-reference.md` §7)؛ الأوامر والاستعلامات في `commands/` و`queries/` من الحزمة نفسها.

| الـAggregate | الشريحة | المتطلبات | القصص | العمليات | الجدول | الوحدة | مكان الكود | مواصفة آلة الحالة | مواصفة الثوابت + خصائص الشريحة |
|---|---|---|---|---|---|---|---|---|---|
| `AGG-ADAPTER` | SLC-02 | REQ-INF-005, REQ-INF-008, REQ-INF-009 | 7 | 7 | `integration.adapters` | DU-11 | `contexts/bc07-platform/domain/adapter/` | TST-ADAPTER-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-AI-REQUEST` | SLC-10 | REQ-AI-001, REQ-AI-002, REQ-AI-003, REQ-AI-004, REQ-AI-007, REQ-AI-008, REQ-AI-011, REQ-AI-012 | 11 | 4 | `ai.ai_requests` | DU-16 | `contexts/bc07-platform/domain/ai-request/` | TST-AI-REQUEST-SM | PROP-SLC10, TST-SLC10-INVARIANTS |
| `AGG-AI-RESULT` | SLC-10 | REQ-AI-005, REQ-AI-006, REQ-AI-008 | 6 | 5 | `ai.ai_results` | DU-16 | `contexts/bc07-platform/domain/ai-result/` | TST-AI-RESULT-SM | PROP-SLC10, TST-SLC10-INVARIANTS |
| `AGG-AI-ROUTING` | SLC-10 | REQ-AI-008, REQ-AI-011 | 6 | 5 | `ai.ai_routings` | DU-16 | `contexts/bc07-platform/domain/ai-routing/` | TST-AI-ROUTING-SM | PROP-SLC10, TST-SLC10-INVARIANTS |
| `AGG-AI-TOOL` | SLC-10 | REQ-AI-012, REQ-AI-013 | 6 | 6 | `ai.ai_tools` | DU-16 | `contexts/bc07-platform/domain/ai-tool/` | TST-AI-TOOL-SM | PROP-SLC10, TST-SLC10-INVARIANTS |
| `AGG-ALERT` | SLC-06 | REQ-SIT-004, REQ-SIT-005, REQ-SIT-006 | 8 | 4 | `intelligence.alerts` | DU-06 | `contexts/bc03-intelligence/domain/alert/` | TST-ALERT-SM | PROP-SLC06, TST-SLC06-INVARIANTS |
| `AGG-ALERT-RULE` | SLC-06 | REQ-SIT-004 | 6 | 6 | `intelligence.alert_rules` | DU-06 | `contexts/bc03-intelligence/domain/alert-rule/` | TST-ALERT-RULE-SM | PROP-SLC06, TST-SLC06-INVARIANTS |
| `AGG-ALLOCATION` | SLC-09 | REQ-LOG-002, REQ-LOG-008, REQ-LOG-014, REQ-RES-007, REQ-RES-008, REQ-RES-009, REQ-RES-010, REQ-RES-011, REQ-RES-012 | 12 | 7 | `readiness.allocations` | DU-14 | `contexts/bc05-readiness/domain/allocation/` | TST-ALLOCATION-SM | PROP-SLC09, TST-SLC09-INVARIANTS |
| `AGG-ANALYSIS-CASE` | SLC-07 | REQ-ANL-001, REQ-ANL-007 | 18 | 18 | `intelligence.analysis_cases` | DU-06 | `contexts/bc03-intelligence/domain/analysis-case/` | TST-ANALYSIS-CASE-SM | PROP-SLC07, TST-SLC07-INVARIANTS |
| `AGG-ANALYSIS-METHOD` | SLC-07 | REQ-ANL-002, REQ-ANL-003 | 5 | 5 | `intelligence.analysis_methods` | DU-06 | `contexts/bc03-intelligence/domain/analysis-method/` | TST-ANALYSIS-METHOD-SM | PROP-SLC07, TST-SLC07-INVARIANTS |
| `AGG-ANALYSIS-RUN` | SLC-07 | REQ-ANL-002, REQ-ANL-003, REQ-ANL-004, REQ-INF-035 | 8 | 5 | `intelligence.analysis_runs` | DU-06 | `contexts/bc03-intelligence/domain/analysis-run/` | TST-ANALYSIS-RUN-SM | PROP-SLC07, TST-SLC07-INVARIANTS |
| `AGG-ARCHIVE-PACKAGE` | SLC-12 | REQ-ARC-001, REQ-ARC-002, REQ-ARC-003 | 11 | 6 | `knowledge.archive_packages` | DU-15 | `contexts/bc06-knowledge/domain/archive-package/` | TST-ARCHIVE-PACKAGE-SM | PROP-SLC12, TST-SLC12-INVARIANTS |
| `AGG-ASSESSMENT` | SLC-07 | REQ-ANL-005, REQ-ANL-006, REQ-ANL-008 | 10 | 9 | `intelligence.assessment_versions` | DU-06 | `contexts/bc03-intelligence/domain/assessment/` | TST-ASSESSMENT-SM | PROP-SLC07, TST-SLC07-INVARIANTS |
| `AGG-ASSET` | SLC-09 | REQ-RES-001, REQ-RES-002, REQ-RES-003, REQ-RES-005 | 14 | 14 | `readiness.assets` | DU-14 | `contexts/bc05-readiness/domain/asset/` | TST-ASSET-SM | PROP-SLC09, TST-SLC09-INVARIANTS |
| `AGG-ASSET-ASSIGNMENT` | SLC-09 | REQ-RES-003, REQ-RES-012 | 4 | 3 | `readiness.asset_assignments` | DU-14 | `contexts/bc05-readiness/domain/asset-assignment/` | TST-ASSET-ASSIGNMENT-SM | PROP-SLC09, TST-SLC09-INVARIANTS |
| `AGG-ASSET-RESERVATION` | SLC-09 | REQ-RES-014 | 6 | 4 | `readiness.asset_reservations` | DU-14 | `contexts/bc05-readiness/domain/asset-reservation/` | TST-ASSET-RESERVATION-SM | PROP-SLC09, TST-SLC09-INVARIANTS |
| `AGG-ATTACHMENT` | SLC-02 | REQ-GOV-008, REQ-INF-003, REQ-INF-004 | 7 | 4 | `information.attachments` | DU-05 | `contexts/bc02-information/domain/attachment/` | TST-ATTACHMENT-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-AUTHORITY-GRANT` | SLC-01 | REQ-FND-007, REQ-FND-008, REQ-FND-009 | 10 | 9 | `foundation.authority_grants` | DU-02 | `contexts/bc01-foundation/domain/authority-grant/` | TST-AUTHORITY-GRANT-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-CAP-MESSAGE` | SLC-16 | REQ-INT-003 | 6 | 5 | `intelligence.cap_messages` | DU-06 | `contexts/bc03-intelligence/domain/cap-message/` | TST-CAP-MESSAGE-SM | PROP-SLC16, TST-SLC16-INVARIANTS |
| `AGG-CLAIM` | SLC-02 | REQ-INF-021, REQ-INF-022, REQ-INF-024, REQ-INF-026, REQ-INF-037 | 7 | 7 | `information.claims` | DU-04 | `contexts/bc02-information/domain/claim/` | TST-CLAIM-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-CLASSIFICATION-SCHEME` | SLC-01 | REQ-GOV-001, REQ-GOV-004, REQ-GOV-009 | 6 | 5 | `governance.classification_schemes` | DU-03 | `contexts/bc08-governance/domain/classification-scheme/` | TST-CLASSIFICATION-SCHEME-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-CLEARANCE` | SLC-01 | REQ-GOV-003, REQ-GOV-004 | 7 | 6 | `foundation.clearances` | DU-02 | `contexts/bc01-foundation/domain/clearance/` | TST-CLEARANCE-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-COLLECTION-PLAN` | SLC-14 | REQ-COL-002 | 8 | 7 | `information.collection_plans` | DU-04 | `contexts/bc02-information/domain/collection-plan/` | TST-COLLECTION-PLAN-SM | PROP-SLC14, TST-SLC14-INVARIANTS |
| `AGG-COLLECTION-REQUIREMENT` | SLC-14 | REQ-COL-001, REQ-COL-003 | 13 | 11 | `information.collection_requirements` | DU-04 | `contexts/bc02-information/domain/collection-requirement/` | TST-COLLECTION-REQUIREMENT-SM | PROP-SLC14, TST-SLC14-INVARIANTS |
| `AGG-CONFLICT` | SLC-04 | REQ-INF-024, REQ-INF-025 | 11 | 8 | `information.conflicts` | DU-04 | `contexts/bc02-information/domain/conflict/` | TST-CONFLICT-SM | PROP-SLC04, TST-SLC04-INVARIANTS |
| `AGG-COORDINATION-CASE` | SLC-15 | REQ-CRD-001, REQ-CRD-002 | 12 | 11 | `operations.coordination_cases` | DU-08 | `contexts/bc04-operations/domain/coordination-case/` | TST-COORDINATION-CASE-SM | PROP-SLC15, TST-SLC15-INVARIANTS |
| `AGG-CORRELATION-PROPOSAL` | SLC-15 | REQ-FUS-001, REQ-FUS-002 | 8 | 6 | `information.correlation_proposals` | DU-04 | `contexts/bc02-information/domain/correlation-proposal/` | TST-CORRELATION-PROPOSAL-SM | PROP-SLC15, TST-SLC15-INVARIANTS |
| `AGG-CORRELATION-RULE` | SLC-15 | REQ-FUS-001 | 4 | 4 | `information.correlation_rules` | DU-04 | `contexts/bc02-information/domain/correlation-rule/` | TST-CORRELATION-RULE-SM | PROP-SLC15, TST-SLC15-INVARIANTS |
| `AGG-DECISION` | SLC-08 | REQ-DEC-002, REQ-DEC-003, REQ-DEC-004 | 5 | 4 | `operations.decisions` | DU-08 | `contexts/bc04-operations/domain/decision/` | TST-DECISION-SM | PROP-SLC08, TST-SLC08-INVARIANTS |
| `AGG-DECISION-REQUEST` | SLC-08 | REQ-DEC-001 | 9 | 7 | `operations.decision_requests` | DU-08 | `contexts/bc04-operations/domain/decision-request/` | TST-DECISION-REQUEST-SM | PROP-SLC08, TST-SLC08-INVARIANTS |
| `AGG-DEVICE` | SLC-11 | REQ-OFF-005 | 9 | 8 | `foundation.devices` | DU-02 | `contexts/bc01-foundation/domain/device/` | TST-DEVICE-SM | PROP-SLC11, TST-SLC11-INVARIANTS |
| `AGG-DISPOSITION-RUN` | SLC-12a | REQ-GOV-006, REQ-GOV-007 | 8 | 4 | `governance.disposition_runs` | DU-03 | `contexts/bc08-governance/domain/disposition-run/` | TST-DISPOSITION-RUN-SM | PROP-SLC12A, TST-SLC12A-INVARIANTS |
| `AGG-DISTRIBUTION` | SLC-12 | REQ-PRD-004, REQ-PRD-005 | 4 | 2 | `knowledge.distributions` | DU-15 | `contexts/bc06-knowledge/domain/distribution/` | TST-DISTRIBUTION-SM | PROP-SLC12, TST-SLC12-INVARIANTS |
| `AGG-ENTITY` | SLC-02 | REQ-INF-020, REQ-INF-021, REQ-INF-036 | 11 | 11 | `information.entities` | DU-04 | `contexts/bc02-information/domain/entity/` | TST-ENTITY-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-ER-CASE` | SLC-04 | REQ-INF-032, REQ-INF-033, REQ-INF-034 | 13 | 12 | `information.er_cases` | DU-04 | `contexts/bc02-information/domain/er-case/` | TST-ER-CASE-SM | PROP-SLC04, TST-SLC04-INVARIANTS |
| `AGG-ERASURE-REQUEST` | SLC-12a | REQ-GOV-008 | 9 | 4 | `governance.erasure_requests` | DU-03 | `contexts/bc08-governance/domain/erasure-request/` | TST-ERASURE-REQUEST-SM | PROP-SLC12A, TST-SLC12A-INVARIANTS |
| `AGG-EVAL-SUITE` | SLC-10 | REQ-AI-010 | 4 | 3 | `ai.eval_suites` | DU-16 | `contexts/bc07-platform/domain/eval-suite/` | TST-EVAL-SUITE-SM | PROP-SLC10, TST-SLC10-INVARIANTS |
| `AGG-EVIDENCE` | SLC-02 | REQ-INF-003, REQ-INF-004 | 7 | 7 | `information.evidence` | DU-04 | `contexts/bc02-information/domain/evidence/` | TST-EVIDENCE-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-EVIDENCE-LINK` | SLC-02 | REQ-INF-021 | 2 | 2 | `information.evidence_links` | DU-04 | `contexts/bc02-information/domain/evidence-link/` | TST-EVIDENCE-LINK-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-EXERCISE` | SLC-19 | REQ-TRX-002, REQ-TRX-003, REQ-TRX-004, REQ-TRX-005, REQ-TRX-006, REQ-TRX-007 | 8 | 6 | `readiness.exercises` | DU-14 | `contexts/bc05-readiness/domain/exercise/` | TST-EXERCISE-SM | PROP-SLC19, TST-SLC19-INVARIANTS |
| `AGG-EXTERNAL-ID` | SLC-02 | REQ-INF-036 | 3 | 3 | `information.external_ids` | DU-04 | `contexts/bc02-information/domain/external-id/` | TST-EXTERNAL-ID-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-FINDING` | SLC-07 | REQ-ANL-005, REQ-INF-035 | 4 | 4 | `intelligence.findings` | DU-06 | `contexts/bc03-intelligence/domain/finding/` | TST-FINDING-SM | PROP-SLC07, TST-SLC07-INVARIANTS |
| `AGG-HR-SYNC-PROPOSAL` | SLC-16 | REQ-INT-004 | 6 | 3 | `foundation.hr_sync_proposals` | DU-02 | `contexts/bc01-foundation/domain/hr-sync-proposal/` | TST-HR-SYNC-PROPOSAL-SM | PROP-SLC16, TST-SLC16-INVARIANTS |
| `AGG-IMPORT-BATCH` | SLC-02 | REQ-INF-005, REQ-INF-006, REQ-INF-007, REQ-INF-008, REQ-INF-009 | 9 | 5 | `information.import_batches` | DU-05 | `contexts/bc02-information/domain/import-batch/` | TST-IMPORT-BATCH-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-INCIDENT` | SLC-17 | REQ-RCM-006, REQ-RCM-007, REQ-RCM-008, REQ-RCM-009, REQ-RCM-010, REQ-RCM-011, REQ-RCM-012, REQ-RCM-013 | 14 | 13 | `operations.incidents` | DU-08 | `contexts/bc04-operations/domain/incident/` | TST-INCIDENT-SM | PROP-SLC17, TST-SLC17-INVARIANTS |
| `AGG-INTEGRATION-CONNECTION` | SLC-16 | REQ-INT-001 | 10 | 8 | `integration.integration_connections` | DU-11 | `contexts/bc07-platform/domain/integration-connection/` | TST-INTEGRATION-CONNECTION-SM | PROP-SLC16, TST-SLC16-INVARIANTS |
| `AGG-KNOWLEDGE-OBJECT` | SLC-12 | REQ-KNW-001, REQ-KNW-002, REQ-KNW-003, REQ-TRX-013 | 12 | 11 | `knowledge.knowledge_objects` | DU-15 | `contexts/bc06-knowledge/domain/knowledge-object/` | TST-KNOWLEDGE-OBJECT-SM | PROP-SLC12, TST-SLC12-INVARIANTS |
| `AGG-LEGAL-HOLD` | SLC-12a | REQ-GOV-007 | 7 | 7 | `governance.legal_holds` | DU-03 | `contexts/bc08-governance/domain/legal-hold/` | TST-LEGAL-HOLD-SM | PROP-SLC12A, TST-SLC12A-INVARIANTS |
| `AGG-LOGISTICS-REQUEST` | SLC-18 | REQ-LOG-001, REQ-LOG-002, REQ-LOG-003, REQ-LOG-004, REQ-LOG-006, REQ-LOG-008, REQ-LOG-009, REQ-LOG-013, REQ-LOG-014 | 12 | 5 | `readiness.logistics_requests` | DU-14 | `contexts/bc05-readiness/domain/logistics-request/` | TST-LOGISTICS-REQUEST-SM | PROP-SLC18, TST-SLC18-INVARIANTS |
| `AGG-MAINTENANCE-ORDER` | SLC-09 | REQ-RES-004 | 6 | 6 | `readiness.maintenance_orders` | DU-14 | `contexts/bc05-readiness/domain/maintenance-order/` | TST-MAINTENANCE-ORDER-SM | PROP-SLC09, TST-SLC09-INVARIANTS |
| `AGG-MATCH-RULESET` | SLC-04 | REQ-INF-032, REQ-SRC-003 | 5 | 4 | `information.match_rulesets` | DU-04 | `contexts/bc02-information/domain/match-ruleset/` | TST-MATCH-RULESET-SM | PROP-SLC04, TST-SLC04-INVARIANTS |
| `AGG-MODEL-VERSION` | SLC-10 | REQ-AI-009, REQ-AI-010 | 11 | 10 | `ai.model_versions` | DU-16 | `contexts/bc07-platform/domain/model-version/` | TST-MODEL-VERSION-SM | PROP-SLC10, TST-SLC10-INVARIANTS |
| `AGG-NOTIFICATION` | SLC-06 | REQ-COM-001, REQ-COM-002 | 7 | 2 | `operations.notifications` | DU-08 | `contexts/bc04-operations/domain/notification/` | TST-NOTIFICATION-SM | PROP-SLC06, TST-SLC06-INVARIANTS |
| `AGG-OBSERVATION` | SLC-02 | REQ-INF-002, REQ-INF-028 | 8 | 8 | `information.observations` | DU-05 | `contexts/bc02-information/domain/observation/` | TST-OBSERVATION-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-ORGANIZATION` | SLC-01 | REQ-FND-002 | 9 | 9 | `foundation.organizations` | DU-02 | `contexts/bc01-foundation/domain/organization/` | TST-ORGANIZATION-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-OUTCOME-TRACKER` | SLC-08 | REQ-OPS-013 | 5 | 2 | `operations.outcome_trackers` | DU-08 | `contexts/bc04-operations/domain/outcome-tracker/` | TST-OUTCOME-TRACKER-SM | PROP-SLC08, TST-SLC08-INVARIANTS |
| `AGG-PERSON` | SLC-01 | REQ-FND-006, REQ-GOV-008 | 5 | 5 | `foundation.persons` | DU-02 | `contexts/bc01-foundation/domain/person/` | TST-PERSON-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-PLAN` | SLC-08 | REQ-OPS-001, REQ-OPS-002, REQ-OPS-003 | 14 | 12 | `operations.plans` | DU-08 | `contexts/bc04-operations/domain/plan/` | TST-PLAN-SM | PROP-SLC08, TST-SLC08-INVARIANTS |
| `AGG-PLAN-VERSION` | SLC-08 | REQ-OPS-001, REQ-OPS-003, REQ-OPS-004, REQ-OPS-005, REQ-OPS-014 | 9 | 8 | `operations.plan_versions` | DU-08 | `contexts/bc04-operations/domain/plan-version/` | TST-PLAN-VERSION-SM | PROP-SLC08, TST-SLC08-INVARIANTS |
| `AGG-POLICY-SET` | SLC-01 | REQ-FND-011, REQ-FND-012, REQ-GOV-009 | 8 | 6 | `governance.policy_sets` | DU-03 | `contexts/bc08-governance/domain/policy-set/` | TST-POLICY-SET-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-PRELOAD-PACKAGE` | SLC-11 | REQ-OFF-002, REQ-OFF-005 | 8 | 4 | `field.preload_packages` | DU-10 | `contexts/bc07-platform/domain/preload-package/` | TST-PRELOAD-PACKAGE-SM | PROP-SLC11, TST-SLC11-INVARIANTS |
| `AGG-PRODUCT` | SLC-12 | REQ-PRD-001, REQ-PRD-002, REQ-PRD-003 | 14 | 11 | `knowledge.products` | DU-15 | `contexts/bc06-knowledge/domain/product/` | TST-PRODUCT-SM | PROP-SLC12, TST-SLC12-INVARIANTS |
| `AGG-PRODUCT-TEMPLATE` | SLC-12 | REQ-PRD-001 | 4 | 4 | `knowledge.product_templates` | DU-15 | `contexts/bc06-knowledge/domain/product-template/` | TST-PRODUCT-TEMPLATE-SM | PROP-SLC12, TST-SLC12-INVARIANTS |
| `AGG-PROJECTION-VERSION` | SLC-05 | REQ-SRC-004 | 9 | 5 | — | DU-09 | `contexts/bc07-platform/domain/projection-version/` | TST-PROJECTION-VERSION-SM | PROP-SLC05, TST-SLC05-INVARIANTS |
| `AGG-QUALIFICATION-RECORD` | SLC-03 | REQ-RDY-001, REQ-RDY-002, REQ-TRX-012 | 7 | 6 | `readiness.qualification_records` | DU-08 | `contexts/bc05-readiness/domain/qualification-record/` | TST-QUALIFICATION-RECORD-SM | PROP-SLC03, TST-SLC03-INVARIANTS |
| `AGG-REALWORLD-EVENT` | SLC-02 | REQ-INF-020 | 6 | 6 | `information.realworld_events` | DU-04 | `contexts/bc02-information/domain/realworld-event/` | TST-REALWORLD-EVENT-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-RECONSTRUCTION` | SLC-12 | REQ-ARC-004 | 6 | 3 | `knowledge.reconstructions` | DU-15 | `contexts/bc06-knowledge/domain/reconstruction/` | TST-RECONSTRUCTION-SM | PROP-SLC12, TST-SLC12-INVARIANTS |
| `AGG-RELATIONSHIP` | SLC-02 | REQ-INF-027 | 4 | 4 | `information.relationships` | DU-04 | `contexts/bc02-information/domain/relationship/` | TST-RELATIONSHIP-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-RESOURCE-POOL` | SLC-09 | REQ-LOG-002, REQ-RES-006 | 6 | 6 | `readiness.resource_pools` | DU-14 | `contexts/bc05-readiness/domain/resource-pool/` | TST-RESOURCE-POOL-SM | PROP-SLC09, TST-SLC09-INVARIANTS |
| `AGG-RETENTION-SCHEDULE` | SLC-12a | REQ-GOV-006 | 6 | 5 | `governance.retention_schedules` | DU-03 | `contexts/bc08-governance/domain/retention-schedule/` | TST-RETENTION-SCHEDULE-SM | PROP-SLC12A, TST-SLC12A-INVARIANTS |
| `AGG-RISK` | SLC-17 | REQ-RCM-001, REQ-RCM-002, REQ-RCM-003, REQ-RCM-004, REQ-RCM-005, REQ-RCM-012 | 8 | 7 | `operations.risks` | DU-08 | `contexts/bc04-operations/domain/risk/` | TST-RISK-SM | PROP-SLC17, TST-SLC17-INVARIANTS |
| `AGG-ROLE` | SLC-01 | REQ-FND-014 | 4 | 4 | `foundation.roles` | DU-02 | `contexts/bc01-foundation/domain/role/` | TST-ROLE-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-ROLE-ASSIGNMENT` | SLC-01 | REQ-FND-011, REQ-OPS-005, REQ-OPS-009 | 3 | 2 | `foundation.role_assignments` | DU-02 | `contexts/bc01-foundation/domain/role-assignment/` | TST-ROLE-ASSIGNMENT-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-ROLE-REQUIREMENT` | SLC-09 | REQ-RES-013 | 4 | 4 | `readiness.role_requirements` | DU-14 | `contexts/bc05-readiness/domain/role-requirement/` | TST-ROLE-REQUIREMENT-SM | PROP-SLC09, TST-SLC09-INVARIANTS |
| `AGG-SCENARIO` | SLC-19 | REQ-TRX-001, REQ-TRX-002 | 6 | 6 | `readiness.scenarios` | DU-14 | `contexts/bc05-readiness/domain/scenario/` | TST-SCENARIO-SM | PROP-SLC19, TST-SLC19-INVARIANTS |
| `AGG-SECURITY-EXCEPTION` | SLC-01 | REQ-FND-017 | 6 | 5 | `governance.security_exceptions` | DU-03 | `contexts/bc08-governance/domain/security-exception/` | TST-SECURITY-EXCEPTION-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-SENSOR-STREAM` | SLC-16 | REQ-INT-002 | 7 | 6 | `integration.sensor_streams` | DU-11 | `contexts/bc07-platform/domain/sensor-stream/` | TST-SENSOR-STREAM-SM | PROP-SLC16, TST-SLC16-INVARIANTS |
| `AGG-SERVICE-ACCOUNT` | SLC-01 | REQ-FND-006 | 5 | 5 | `foundation.service_accounts` | DU-02 | `contexts/bc01-foundation/domain/service-account/` | TST-SERVICE-ACCOUNT-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-SHIPMENT` | SLC-18 | REQ-LOG-004, REQ-LOG-005, REQ-LOG-006, REQ-LOG-007, REQ-LOG-008, REQ-LOG-009 | 10 | 10 | `readiness.shipments` | DU-14 | `contexts/bc05-readiness/domain/shipment/` | TST-SHIPMENT-SM | PROP-SLC18, TST-SLC18-INVARIANTS |
| `AGG-SIMULATION` | SLC-19 | REQ-TRX-005, REQ-TRX-008, REQ-TRX-009, REQ-TRX-010, REQ-TRX-011 | 10 | 10 | `readiness.simulations` | DU-14 | `contexts/bc05-readiness/domain/simulation/` | TST-SIMULATION-SM | PROP-SLC19, TST-SLC19-INVARIANTS |
| `AGG-SITUATION` | SLC-06 | REQ-SIT-001, REQ-SIT-002, REQ-SIT-003 | 12 | 12 | `intelligence.situations` | DU-06 | `contexts/bc03-intelligence/domain/situation/` | TST-SITUATION-SM | PROP-SLC06, TST-SLC06-INVARIANTS |
| `AGG-SOURCE` | SLC-02 | REQ-INF-001 | 9 | 9 | `information.sources` | DU-04 | `contexts/bc02-information/domain/source/` | TST-SOURCE-SM | PROP-SLC02, TST-SLC02-INVARIANTS |
| `AGG-SUBSCRIPTION` | SLC-06 | REQ-COM-001 | 6 | 5 | `operations.subscriptions` | DU-08 | `contexts/bc04-operations/domain/subscription/` | TST-SUBSCRIPTION-SM | PROP-SLC06, TST-SLC06-INVARIANTS |
| `AGG-SYNC-CONFLICT` | SLC-11 | REQ-OFF-004 | 7 | 6 | `field.sync_conflicts` | DU-10 | `contexts/bc07-platform/domain/sync-conflict/` | TST-SYNC-CONFLICT-SM | PROP-SLC11, TST-SLC11-INVARIANTS |
| `AGG-SYNC-SESSION` | SLC-11 | REQ-OFF-001, REQ-OFF-003, REQ-OFF-004, REQ-OFF-006 | 7 | 3 | `field.sync_sessions` | DU-10 | `contexts/bc07-platform/domain/sync-session/` | TST-SYNC-SESSION-SM | PROP-SLC11, TST-SLC11-INVARIANTS |
| `AGG-TASK` | SLC-03 | REQ-OFF-001, REQ-OPS-006, REQ-OPS-007, REQ-OPS-008, REQ-OPS-009, REQ-OPS-010, REQ-OPS-011, REQ-OPS-012, REQ-RCM-013 | 32 | 27 | `operations.tasks` | DU-08 | `contexts/bc04-operations/domain/task/` | TST-TASK-SM | PROP-SLC03, TST-SLC03-INVARIANTS |
| `AGG-TASK-TYPE` | SLC-03 | REQ-OPS-007, REQ-OPS-014 | 5 | 5 | `operations.task_types` | DU-08 | `contexts/bc04-operations/domain/task-type/` | TST-TASK-TYPE-SM | PROP-SLC03, TST-SLC03-INVARIANTS |
| `AGG-TENANT` | SLC-01 | REQ-FND-001, REQ-FND-003, REQ-FND-004, REQ-FND-018 | 12 | 12 | `foundation.tenants` | DU-02 | `contexts/bc01-foundation/domain/tenant/` | TST-TENANT-SM | PROP-SLC01, TST-SLC01-INVARIANTS |
| `AGG-USER` | SLC-01 | REQ-FND-005, REQ-FND-006 | 13 | 13 | `foundation.users` | DU-02 | `contexts/bc01-foundation/domain/user/` | TST-USER-SM | PROP-SLC01, TST-SLC01-INVARIANTS |

**عمليات بلا Aggregate (13):** `QRY-AI-USAGE`, `QRY-AUD-SEARCH`, `QRY-AUD-VERIFY`, `QRY-BASE-TILE`, `QRY-ELIG-CHECK`, `QRY-GRAPH-NEIGHBORHOOD`, `QRY-GRAPH-PATHS`, `QRY-LIN-TRACE`, `QRY-PDP-DECIDE`, `QRY-READINESS`, `QRY-SEC-CONTEXT`, `QRY-SRCH-QUERY`, `QRY-SRCH-SUGGEST` — استعلامات عابرة (`05-user-stories/`، «استعلامات عابرة للـAggregates»).

**عمليات بلا كتالوج ولا قصة (1):** `QRY-LABEL-CHECK` — `QRY-LABEL-CHECK` عقد عابر للسياقات يقدمه كل سياق يملك موارد معلَّمة (CR-47، `14-api-design.md` §7)، وهو الوحيد الذي يعدّه V2 يتيمًا.

<!-- END GENERATED: build_analysis_design.py -->
